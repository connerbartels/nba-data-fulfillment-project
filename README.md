# NBA Data Fulfillment Project

## Project Overview
This project is part of a portfolio initiative to demonstrate SQL, data collection, and ETL pipeline skills. It focuses on NBA data, using one API source and one web-scraped source to simulate real-world data engineering tasks.

---

## Data Sources

### Web Scraped Source
- **URL:** [ESPN NBA Scoreboard – April 13, 2025](https://www.espn.com/nba/scoreboard/_/date/20250413)
- **Output File:** `nba_espn_scores_20250413.csv`
- **Details:** Collected NBA game scores, teams, and matchups using BeautifulSoup.

### API Source
- **API:** [BallDontLie API](https://www.balldontlie.io/)
- **Endpoint:** `/v1/teams`
- **Output File:** `nba_teams.csv`
- **Details:** Pulled NBA team info including names, cities, conferences, and abbreviations.

---

## Extract & Load Notebooks
- `notebooks/ESPN Web Scrape Extract Load.ipynb`
- `notebooks/balldontlie_API_Extract_Load_Raw.ipynb`

---

## Milestone 01 Complete
Raw data from both the API and web scraping sources has been collected and saved into CSV files under the `data/` folder, fulfilling the requirements of Milestone 01.
