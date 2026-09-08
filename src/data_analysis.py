
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==========================================
# CRICKET ANALYTICS PROJECT
# ==========================================

print("=" * 60)
print("              CRICKET ANALYTICS")
print("=" * 60)

# ------------------------------------------
# 1. Load Dataset
# ------------------------------------------

file_path = "../data/cricket_data.xlsx"

df = pd.read_excel(file_path)

print("\n✅ Dataset Loaded Successfully")
print(f"Total Matches : {len(df)}")
print(f"Total Columns : {len(df.columns)}")

# ------------------------------------------
# 2. Basic Dataset Information
# ------------------------------------------

print("\n--- Dataset Information ---")
print(df.info())

print("\n--- First 5 Records ---")
print(df.head())

# ------------------------------------------
# 3. Missing Values
# ------------------------------------------

print("\n--- Missing Values ---")

missing_values = df.isnull().sum()

print(missing_values[missing_values > 0])

# ------------------------------------------
# 4. Duplicate Records
# ------------------------------------------

duplicates = df.duplicated().sum()

print(f"\nDuplicate Records: {duplicates}")

if duplicates > 0:
    df = df.drop_duplicates()
    print("✅ Duplicate records removed.")

# ------------------------------------------
# 5. Statistical Summary
# ------------------------------------------

print("\n--- Statistical Summary ---")

print(df.describe(include="all"))

# ------------------------------------------
# Create Visualization Folder
# ------------------------------------------

os.makedirs("../visualizations", exist_ok=True)

# ==========================================
# 6. TEAM PERFORMANCE ANALYSIS
# ==========================================

print("\n" + "=" * 60)
print("TEAM PERFORMANCE ANALYSIS")
print("=" * 60)

if "winner" in df.columns:

    team_wins = df["winner"].value_counts()

    print("\n🏆 Top 10 Winning Teams:")
    print(team_wins.head(10))

    plt.figure(figsize=(10, 6))

    team_wins.head(10).plot(kind="bar")

    plt.title("Top 10 IPL Teams by Match Wins")
    plt.xlabel("Team")
    plt.ylabel("Number of Wins")
    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("../visualizations/team_wins.png")

    plt.show()

# ==========================================
# 7. PLAYER OF THE MATCH ANALYSIS
# ==========================================

print("\n" + "=" * 60)
print("PLAYER PERFORMANCE ANALYSIS")
print("=" * 60)

if "player_of_match" in df.columns:

    player_awards = df["player_of_match"].value_counts()

    print("\n⭐ Top 10 Players by Player of the Match Awards:")

    print(player_awards.head(10))

    plt.figure(figsize=(10, 6))

    player_awards.head(10).plot(kind="bar")

    plt.title("Top 10 Players by Player of the Match Awards")
    plt.xlabel("Player")
    plt.ylabel("Player of the Match Awards")
    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("../visualizations/top_players.png")

    plt.show()

# ==========================================
# 8. IPL SEASON ANALYSIS
# ==========================================

print("\n" + "=" * 60)
print("SEASON ANALYSIS")
print("=" * 60)

if "season" in df.columns:

    season_matches = df["season"].value_counts().sort_index()

    print("\n📅 Matches Played by Season:")

    print(season_matches)

    plt.figure(figsize=(10, 6))

    season_matches.plot(kind="line", marker="o")

    plt.title("IPL Matches by Season")
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.grid(True)

    plt.tight_layout()

    plt.savefig("../visualizations/matches_by_season.png")

    plt.show()

# ==========================================
# 9. TOSS DECISION ANALYSIS
# ==========================================

print("\n" + "=" * 60)
print("TOSS ANALYSIS")
print("=" * 60)

if "toss_decision" in df.columns:

    toss_decisions = df["toss_decision"].value_counts()

    print("\n🪙 Toss Decisions:")

    print(toss_decisions)

    plt.figure(figsize=(7, 7))

    toss_decisions.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Toss Decision Distribution")
    plt.ylabel("")

    plt.tight_layout()

    plt.savefig("../visualizations/toss_decisions.png")

    plt.show()

# ==========================================
# 10. WIN MARGIN ANALYSIS
# ==========================================

print("\n" + "=" * 60)
print("WIN MARGIN ANALYSIS")
print("=" * 60)

# Wins by runs

if "win_by_runs" in df.columns:

    runs_wins = df["win_by_runs"].dropna()

    print("\n🏏 Matches Won by Runs:")
    print(f"Average winning margin: {runs_wins.mean():.2f} runs")
    print(f"Maximum winning margin: {runs_wins.max():.0f} runs")

    plt.figure(figsize=(10, 6))

    plt.hist(runs_wins, bins=20)

    plt.title("Distribution of Winning Margins by Runs")
    plt.xlabel("Winning Margin (Runs)")
    plt.ylabel("Number of Matches")

    plt.tight_layout()

    plt.savefig("../visualizations/win_by_runs.png")

    plt.show()

# ==========================================
# 11. WIN BY WICKETS ANALYSIS
# ==========================================

if "win_by_wickets" in df.columns:

    wickets_wins = df["win_by_wickets"].dropna()

    print("\n🎯 Matches Won by Wickets:")
    print(f"Average winning margin: {wickets_wins.mean():.2f} wickets")
    print(f"Maximum winning margin: {wickets_wins.max():.0f} wickets")

    plt.figure(figsize=(10, 6))

    plt.hist(wickets_wins, bins=10)

    plt.title("Distribution of Winning Margins by Wickets")
    plt.xlabel("Winning Margin (Wickets)")
    plt.ylabel("Number of Matches")

    plt.tight_layout()

    plt.savefig("../visualizations/win_by_wickets.png")

    plt.show()

# ==========================================
# 12. MATCH TYPE ANALYSIS
# ==========================================

if "match_type" in df.columns:

    match_types = df["match_type"].value_counts()

    print("\n🏟️ Match Types:")
    print(match_types)

# ==========================================
# 13. VENUE ANALYSIS
# ==========================================

if "venue" in df.columns:

    top_venues = df["venue"].value_counts().head(10)

    print("\n🏟️ Top 10 Venues by Number of Matches:")
    print(top_venues)

    plt.figure(figsize=(11, 6))

    top_venues.plot(kind="bar")

    plt.title("Top 10 IPL Venues by Number of Matches")
    plt.xlabel("Venue")
    plt.ylabel("Matches")
    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("../visualizations/top_venues.png")

    plt.show()

# ==========================================
# 14. FINAL SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("           ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\n📊 Generated Visualizations:")

print("1. team_wins.png")
print("2. top_players.png")
print("3. matches_by_season.png")
print("4. toss_decisions.png")
print("5. win_by_runs.png")
print("6. win_by_wickets.png")
print("7. top_venues.png")

print("\n🏏 Cricket Analytics Project Completed!")