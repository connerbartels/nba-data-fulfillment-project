import pandas as pd
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# PostgreSQL connection config
pg_user = os.getenv('PG_USER', 'tracy_mcgrady')
pg_password = os.getenv('PG_PASSWORD', 'shaq_attack123')
pg_host = os.getenv('PG_HOST', 'nba-project.c7g8wiquaqg7.us-east-1.rds.amazonaws.com')
pg_db = os.getenv('PG_DB', 'tmac')
pg_port = 5432
pg_schema = 'sql_project'

# Connection string with SSL
pg_conn_str = f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}?sslmode=require'
pg_engine = create_engine(pg_conn_str)

# Create schema
with pg_engine.begin() as conn:
    conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS {pg_schema};'))
    print(f"Schema '{pg_schema}' ensured.")

# File-to-table
files_to_tables = {
    "reddit_api_call_fan_social_metrics.csv": "reddit_fan_metrics",
    "jersey_sales.csv": "jersey_sales",
    "nba_teams.csv": "nba_teams",
    "nba_standings_data.csv": "nba_standings_data",
    "nba_team_valuations.csv": "nba_team_valuations",
    "nba_youtube_statistics.csv": "nba_youtube_statistics",
    "x_statistics.csv": "x_statistics"
}

latin1_files = {"nba_standings_data.csv", "nba_team_valuations.csv"}

# Upload CSVs to PostgreSQL
for file, table in files_to_tables.items():
    file_path = f'data/{file}'
    try:
        print(f"Loading {file} into {pg_schema}.{table}...")

        if file in latin1_files:
            df = pd.read_csv(file_path, encoding='latin1', engine='python')
        else:
            df = pd.read_csv(file_path, encoding='utf-8', engine='python')

        df.to_sql(table, pg_engine, schema=pg_schema, if_exists='replace', index=False)
        print(f"Loaded: {len(df)} records into {pg_schema}.{table}")
    except Exception as e:
        print(f"Failed to load {file}: {e}")

print("All done. Database connection closed.")