# 🏏 Cricket Analytics

A data analytics project focused on cleaning, exploring, and analyzing cricket match data to discover meaningful patterns, trends, and performance insights.

---

## 📊 Project Overview

**Cricket Analytics** uses Python and data analytics libraries to analyze IPL match-level data.

The project performs data cleaning, exploratory data analysis (EDA), statistical exploration, and data visualization to understand team performance, player achievements, match outcomes, toss decisions, and venue statistics.

---

## 🎯 Objectives

* Clean and preprocess cricket match data
* Explore IPL match statistics
* Analyze team performance
* Identify top-performing players
* Study toss decisions and match outcomes
* Analyze winning margins
* Explore match distribution across seasons
* Identify frequently used venues
* Create meaningful data visualizations

---

## ✨ Key Features

* 🧹 Data cleaning and preprocessing
* 🔍 Exploratory Data Analysis (EDA)
* 🏆 Team performance analysis
* ⭐ Player of the Match analysis
* 🪙 Toss decision analysis
* 📈 Winning margin analysis
* 🏟️ Venue analysis
* 📅 Season-wise match analysis
* 📊 Statistical exploration
* 📉 Data visualization

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Jupyter Notebook**
* **Excel / XLSX Dataset**

---

## 📁 Project Structure

```text
Cricket-Analytics/
│
├── data/
│   └── cricket_data.xlsx
│
├── notebooks/
│   └── cricket_analysis.ipynb
│
├── src/
│   └── data_analysis.py
│
├── visualizations/
│   ├── team_wins.png
│   ├── top_players.png
│   ├── matches_by_season.png
│   ├── toss_decisions.png
│   ├── win_by_runs.png
│   ├── win_by_wickets.png
│   └── top_venues.png
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📂 Dataset

The dataset contains **1,169 IPL match records** with **23 columns** covering information such as:

* Match ID
* Date
* Season
* City
* Venue
* Match Type
* Teams
* Toss Winner
* Toss Decision
* Match Winner
* Winning Margin
* Player of the Match
* Match Result

The dataset is used for match-level cricket analytics and exploratory analysis.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vanshpatel2323/Cricket-Analytics.git
```

### 2. Open the Project

```bash
cd Cricket-Analytics
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Run the Analysis

Navigate to the `src` folder:

```bash
cd src
```

Run the Python analysis script:

```bash
python data_analysis.py
```

The script loads the dataset, performs analysis, displays statistical results, and generates visualizations.

---

## 📓 Jupyter Notebook

The complete analysis is also available in:

```text
notebooks/cricket_analysis.ipynb
```

The notebook contains step-by-step analysis including:

* Dataset loading
* Dataset overview
* Missing value analysis
* Duplicate analysis
* Team performance
* Player performance
* Season analysis
* Toss analysis
* Winning margin analysis
* Venue analysis
* Key insights

---

## 📈 Key Insights

Based on the analysis:

### 🏆 Team Performance

**Mumbai Indians** recorded the highest number of wins in the dataset with **151 wins**.

### ⭐ Player Performance

**AB de Villiers** recorded the highest number of Player of the Match awards with **25 awards**.

### 🪙 Toss Analysis

Teams chose to **field first** more frequently than they chose to bat first after winning the toss.

* Field: **764**
* Bat: **405**

### 📊 Winning by Runs

Among matches won by runs:

* Average winning margin: **30.30 runs**
* Maximum winning margin: **146 runs**

### 🏏 Winning by Wickets

Among matches won by wickets:

* Average winning margin: **6.20 wickets**
* Maximum winning margin: **10 wickets**

### 🏟️ Venue Analysis

**Eden Gardens** recorded the highest number of matches in the analyzed venue data with **77 matches**.

---

## 📊 Visualizations

The project generates visualizations for:

| Visualization           | Description                                  |
| ----------------------- | -------------------------------------------- |
| `team_wins.png`         | Top 10 teams by wins                         |
| `top_players.png`       | Top 10 players by Player of the Match awards |
| `matches_by_season.png` | Matches played across seasons                |
| `toss_decisions.png`    | Toss decision distribution                   |
| `win_by_runs.png`       | Distribution of winning margins by runs      |
| `win_by_wickets.png`    | Distribution of winning margins by wickets   |
| `top_venues.png`        | Top 10 venues by number of matches           |

---

## 🔍 Analysis Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Data Exploration
   ↓
Statistical Analysis
   ↓
Visualization
   ↓
Insights
```

---

## 🔮 Future Enhancements

* Add interactive dashboards using **Power BI**
* Add advanced player performance metrics
* Analyze team win percentages
* Analyze toss impact on match results
* Add player-vs-player comparisons
* Add season-wise team performance
* Build an interactive web dashboard
* Apply machine learning for match outcome prediction

---

## 👨‍💻 Author

**Vansh Patel**

BSc IT | Software & Mobile Application | Data Analytics

---

## ⭐ Project Goal

The goal of this project is to demonstrate practical skills in **Python, Pandas, NumPy, data cleaning, exploratory data analysis, statistical analysis, and data visualization** using real-world cricket data.
