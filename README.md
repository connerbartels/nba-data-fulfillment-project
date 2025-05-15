# NBA Popularity vs Performance: A Data-Driven Playbook

## Overview

This project explores the relationship between NBA team performance and fan popularity metrics including social media presence, jersey sales, and game attendance. Built to reflect the real-world duties of a Junior Data Engineer / Data Analyst, this project demonstrates how to extract, transform, and analyze data from APIs and web scraping workflows to derive business insights.

**GitHub Repository:** https://github.com/connerbartels/nba-data-fulfillment-project

---

## Objective

**Who is this for?**  
NBA media, marketing, and operations teams

**What problem does it solve?**  
Helps identify whether fan engagement is driven by on-court success or brand popularity

**How was it solved?**  
Integrated data from APIs and web scraping pipelines into a PostgreSQL database. Used SQL and Python to analyze patterns and generate actionable insights.

---

## Tools and Technologies

- **Languages**: Python, SQL  
- **Database**: AWS RDS (PostgreSQL)  
- **Libraries**: `pandas`, `sqlalchemy`, `requests`, `beautifulsoup4`, `praw`, `psycopg2`, `dotenv`  
- **ETL Automation**: GitHub Actions  
- **Visualization**: Matplotlib  
- **Version Control**: Git, GitHub  

---

## Data Sources

### API Source

- **Name**: BallDontLie API  
- **Data**: NBA team metadata (team name, abbreviation, conference, city)  
- **Job Relevance**: Reflects role requirements for data ingestion via APIs  
- **Pipeline**: Python script pulls JSON → cleans with pandas → loads to PostgreSQL  

### Web-Scraped Sources

- **YouTube Statistics**: Subscribers, views, uploads  
- **Reddit**: Subreddit subscriber count  
- **X (Twitter)**: Follower counts  
- **Jersey Sales**: Top-selling NBA jerseys by player/team  
- **ESPN Standings**: Season wins and rankings  
- **Job Relevance**: Demonstrates scraping and transforming external data sources  
- **Pipeline**: BeautifulSoup + requests → transform with pandas → load to PostgreSQL  

---

## Folder Structure

nba-data-fulfillment-project/

├── data/  (CSV files from API and scrape outputs)

├── notebooks/ (Jupyter notebooks for analysis and SQL queries used for insights)

├── reports/ (Visualizations.pdf's, visualization.ipynb, and Presentation.pdf)

├── proposal/ (Job_Description.pdf and Project_Proposal.pdf)

└── README.md (This file)


---

## Key Insights

### Insight 1: Winning Doesn’t Guarantee Popularity  
Teams like the Lakers dominate social media but may not always win. Meanwhile, high-performing teams like the Nuggets remain under-followed.

- **Business Question**: Does team popularity match performance?
- **Recommendation**: Promote underrated but successful teams
- **Prediction**: Increase fan engagement with balanced exposure

### Insight 2: Jersey Sales Driven by Star Power, Not Team Wins  
Jersey rankings reflect individual player hype rather than team success.

- **Business Question**: What influences jersey sales?
- **Recommendation**: Focus marketing on high-profile players
- **Prediction**: Boosted jersey and merchandise revenue

---

## Visualizations

Four visualizations were created from SQL queries and included in `reports/Visualizations.pdf`:
- Performance Rank vs Social Rank
- Jersey Sales vs Social Metrics
- Performance vs Popularity Gaps
- Total Wins vs Social Media Following

---
