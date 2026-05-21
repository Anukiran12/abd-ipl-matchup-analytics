# AB de Villiers IPL Matchup Analytics Dashboard

## Project Overview

This project analyzes AB de Villiers' performance against elite IPL bowlers using ball-by-ball IPL data from 2008–2022. The analysis combines overall matchup statistics, phase-wise performance trends, and contextual relative metrics to evaluate ABD’s batting dominance against some of the greatest bowlers in IPL history.

The dashboard was built using Python, Pandas, Matplotlib, Seaborn, and Streamlit.

---

## Live Dashboard

https://abd-ipl-matchup-analytics-17.streamlit.app/

---

## Dashboard Preview

![alt text](image-1.png)
![alt text](image.png)

---

## Objectives

- Analyze AB de Villiers' batting performance against elite IPL bowlers
- Compare strike rate, dot-ball percentage, and boundary percentage
- Study phase-wise batting trends across:
  - Powerplay
  - Middle Overs
  - Death Overs
- Compare ABD’s metrics with bowlers’ baseline IPL metrics
- Build an interactive analytics dashboard using Streamlit

---

## Elite Bowlers Selected

The selected bowlers were identified based on:

- IPL longevity
- Wicket-taking ability
- Economy rate
- Match impact
- Reputation across different IPL eras

### Bowlers Included

- DJ Bravo
- DW Steyn
- JJ Bumrah
- R Ashwin
- RA Jadeja
- SL Malinga
- SP Narine

---

## Dataset

### Source
IPL Ball-by-Ball Dataset (2008–2022)

### Data Used
- Ball-by-ball IPL delivery data
- Matchup filtering for AB de Villiers vs selected bowlers
- Phase classification:
  - Powerplay
  - Middle Overs
  - Death Overs

---

## Features & Analysis

### Overall Matchup Analysis
- Strike Rate vs Bowlers
- Dot-Ball Percentage vs Bowlers

### Phase-Wise Matchup Analysis
- Phase-wise Strike Rate
- Phase-wise Boundary Percentage

### Relative Metrics Analysis
Comparison between:
- ABD’s matchup metrics
- Bowlers’ baseline IPL metrics

---

## Key Insights

- AB de Villiers maintained exceptionally high strike rates against elite death bowlers like Lasith Malinga and DJ Bravo.
- Dale Steyn and Sunil Narine restricted most IPL batters effectively, yet ABD sustained aggressive scoring rates against them.
- R Ashwin and Ravindra Jadeja were among the few bowlers who consistently controlled ABD’s scoring.
- ABD showed his strongest acceleration during death overs, significantly outperforming bowlers' baseline conceded strike rates.
- Relative metrics reveal that ABD consistently scored faster than the average IPL batter against most elite bowlers analyzed.

---

## Tech Stack

### Programming Language
- Python

### Libraries Used
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

---

## Project Workflow

1. Data Understanding
2. Data Cleaning & Filtering
3. Feature Engineering
4. Exploratory Data Analysis
5. Relative Metrics Creation
6. Dashboard Development
7. GitHub Version Control
8. Streamlit Deployment

---

## Folder Structure

```text
abd-ipl-matchup-analytics/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_cleaning_filtering.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_visualizations_advanced.ipynb

Future Improvements
Add interactive filters for bowlers and phases
Include dismissal analysis
Add advanced visualizations using Plotly
Deploy with custom Streamlit theme
Expand analysis to other IPL batters
Author

Anukiran Bathula