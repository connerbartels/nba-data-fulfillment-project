# NBA Data Fulfillment Project

## Project Overview
This portfolio project showcases end-to-end data engineering skills through a simulation of a real NBA Data Fulfillment Analyst role. It focuses on extracting and analyzing fan engagement and team performance data from multiple sources, using SQL, ETL pipelines, and data visualization tools to derive actionable insights for marketing optimization.

---

## Tech Stack
- **Python** (requests, BeautifulSoup, pandas)
- **SQL** (PostgreSQL)
- **AWS RDS** (PostgreSQL DB hosting)
- **GitHub Actions** (ETL automation)
- **Power BI / Tableau** (data visualization)
- **Papermill** (for notebook automation)
- **Jupyter Notebooks**

---

## Project Objective
**Who are you helping?**  
NBA’s Global Partnerships & Marketing team

**What problem are you solving?**  
How to optimize ad targeting strategies based on fan engagement and merchandising trends

**How will you solve their problem?**  
By extracting Reddit and ESPN data, loading it into a PostgreSQL data warehouse, analyzing patterns with SQL, and presenting insights through dashboards.

---

## Job Description
**Company:** National Basketball Association (NBA)  
**Title:** Data Fulfillment Analyst  
**Key Responsibilities:**  
- Use SQL to analyze partner data  
- Build segmentation models for ad targeting  
- Collaborate across marketing, engineering, and data strategy teams

📄 [Job_Description.pdf](proposal/Job_Description.pdf)

---

## Data Sources

### Web Scraped Source
- **URL:** [ESPN NBA Scoreboard – April 13, 2025](https://www.espn.com/nba/scoreboard/_/date/20250413)
- **Method:** Python + BeautifulSoup
- **Output:** `nba_espn_scores_20250413.csv`
- **Details:** Collected game scores and teams

### API Source
- **API:** [Reddit API via PRAW](https://praw.readthedocs.io/en/latest/)
- **Subreddits:** Team-specific communities
- **Output:** `reddit_api_call_fan_social_metrics.csv`
- **Details:** Collected subscriber counts as a proxy for fan engagement

---

## Notebooks / Python Scripts

| Notebook | Description |
|----------|-------------|
| `balldontlie_API_Extract_Load_Raw.ipynb` | Used for pulling team metadata from BallDontLie API |
| `ESPN_Web_Scrape_Extract_Load.ipynb` | Scrapes game score data |
| `Reddit API call.ipynb` | Pulls subreddit fan engagement metrics |
| `Team Google Trends Scrape.ipynb` | (Optional enrichment) Tracks fan interest via Google Trends |

---

## SQL Analysis
(Coming in Milestone 03)

- Descriptive and diagnostic SQL queries using CTEs, JOINs, aggregation, and window functions
- Executed via `pandas.read_sql()` from Jupyter Notebooks
- Stored in:
  - `reddit_api_SQL_Analysis.ipynb`
  - `espn_scores_SQL_Analysis.ipynb`

---

## Visualizations
(Coming in Milestone 04)

- Dashboards created in Tableau or Power BI
- Each SQL query linked to a paired visualization
- Summary in `reports/Visualizations.pdf`

---

## Future Improvements
- Expand sentiment analysis using Reddit comments or Twitter feeds
- Incorporate real-time data ingestion via streaming tools
- Build automated data validation in the pipeline

---

