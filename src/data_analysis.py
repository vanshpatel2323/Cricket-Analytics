```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==========================================
# CRICKET ANALYTICS PROJECT
# ==========================================

print("=" * 50)
print("       CRICKET ANALYTICS PROJECT")
print("=" * 50)

# ------------------------------------------
# 1. Load Dataset
# ------------------------------------------

file_path = "../data/cricket_data.csv"

df = pd.read_csv(file_path)

print("\nDataset loaded successfully!")
print(f"Total Records: {len(df)}")
print(f"Total Columns: {len(df.columns)}")

# ------------------------------------------
# 2. Basic Dataset Information
# ------------------------------------------

print("\n--- Dataset Information ---")
print(df.info())

print("\n--- First 5 Records ---")
print(df.head())

print("\n--- Missing Values ---")
print(df.isnull().sum())

# ------------------------------------------
# 3. Remove Duplicate Records
# ------------------------------------------

duplicates = df.duplicated().sum()

print(f"\nDuplicate Records: {duplicates}")

if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicates removed successfully.")

# ------------------------------------------
# 4. Dataset Statistics
# ------------------------------------------

print("\n--- Statistical Summary ---")
print(df.describe(include="all"))

# ------------------------------------------
# 5. Identify Important Columns
# ------------------------------------------

print("\n--- Available Columns ---")

for column in df.columns:
    print(column)

# ------------------------------------------
# 6. Team Performance Analysis
# ------------------------------------------

if "winner" in df.columns:

    print("\n--- Top Winning Teams ---")

    team_wins = df["winner"].value_counts()

    print(team_wins.head(10))

    # Visualization
    plt.figure(figsize=(10, 6))

    team_wins.head(10).plot(kind="bar")

    plt.title("Top 10 IPL Teams by Match Wins")
    plt.xlabel("Team")
    plt.ylabel("Number of Wins")
    plt.xticks(rotation=45)
    plt.tight_layout()

    os.makedirs("../visualizations", exist_ok=True)

    plt.savefig("../visualizations/team_wins.png")

    plt.show()

# ------------------------------------------
# 7. Player of the Match Analysis
# ------------------------------------------

if "player_of_match" in df.columns:

    print("\n--- Top Players of the Match ---")

    top_players = df["player_of_match"].value_counts()

    print(top_players.head(10))

    plt.figure(figsize=(10, 6))

    top_players.head(10).plot(kind="bar")

    plt.title("Top 10 Players by Player of the Match Awards")
    plt.xlabel("Player")
    plt.ylabel("Awards")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("../visualizations/top_players.png")

    plt.show()

# ------------------------------------------
# 8. Season Analysis
# ------------------------------------------

if "season" in df.columns:

    print("\n--- Matches by Season ---")

    season_matches = df["season"].value_counts().sort_index()

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

# ------------------------------------------
# 9. Toss Decision Analysis
# ------------------------------------------

if "toss_decision" in df.columns:

    print("\n--- Toss Decisions ---")

    toss_decisions = df["toss_decision"].value_counts()

    print(toss_decisions)

    plt.figure(figsize=(7, 5))

    toss_decisions.plot(kind="pie", autopct="%1.1f%%")

    plt.title("Toss Decision Distribution")
    plt.ylabel("")

    plt.tight_layout()

    plt.savefig("../visualizations/toss_decisions.png")

    plt.show()

# ------------------------------------------
# 10. Final Summary
# ------------------------------------------

print("\n" + "=" * 50)
print("       ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 50)

print("\nGenerated visualizations:")
print("- team_wins.png")
print("- top_players.png")
print("- matches_by_season.png")
print("- toss_decisions.png")

print("\nThank you for using Cricket Analytics!")
```
