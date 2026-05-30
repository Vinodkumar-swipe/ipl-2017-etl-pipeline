# Databricks notebook source
!pip install pandas

# COMMAND ----------

import pandas as pd





# COMMAND ----------


players_df = pd.read_csv("https://raw.githubusercontent.com/ritesh-ojha/IPL-DATASET/refs/heads/main/csv/2024_players_details.csv")

# COMMAND ----------

players_df.head()

# COMMAND ----------

ball_by_ball_df = pd.read_csv("https://raw.githubusercontent.com/ritesh-ojha/IPL-DATASET/refs/heads/main/csv/Ball_By_Ball_Match_Data.csv")

# COMMAND ----------

ball_by_ball_df.head()

# COMMAND ----------

match_info_df = pd.read_csv("https://raw.githubusercontent.com/ritesh-ojha/IPL-DATASET/refs/heads/main/csv/Match_Info.csv")

# COMMAND ----------

match_info_df.head()

# COMMAND ----------

teams_df = pd.read_csv("https://raw.githubusercontent.com/ritesh-ojha/IPL-DATASET/refs/heads/main/csv/teams_info.csv")

# COMMAND ----------

teams_df.head()

# COMMAND ----------

#manual data profing
print(players_df.info())
print(ball_by_ball_df.info())
print(match_info_df.info())
print(teams_df.info())

# COMMAND ----------

# Missing values count
print(players_df.isnull().sum())

# Percentage of missing values
print((players_df.isnull().sum() / len(players_df)) * 100)

# Duplicates
print(players_df.duplicated().sum())

# COMMAND ----------

#handing null values in players_df
#dropping columns with more than 50% null values
players_df.fillna(players_df.mode().iloc[0], inplace=True)
print(players_df.isnull().sum())

# COMMAND ----------

# Missing values count - 
print(ball_by_ball_df.isnull().sum())

# Percentage of missing values
print((ball_by_ball_df.isnull().sum() / len(ball_by_ball_df)) * 100)

# Duplicates
print(ball_by_ball_df.duplicated().sum())

# COMMAND ----------

#handing null values in players_df
#dropping columns with more than 50% null values
ball_by_ball_df.fillna(ball_by_ball_df.mode().iloc[0], inplace=True)
print(ball_by_ball_df.isnull().sum())

# COMMAND ----------


# Missing values count - 
print(match_info_df.isnull().sum())

# Percentage of missing values
print((match_info_df.isnull().sum() / len(match_info_df)) * 100)

# Duplicates
print(match_info_df.duplicated().sum())

# COMMAND ----------

#handing null values in players_df
#dropping columns with more than 50% null values
match_info_df.fillna(match_info_df.mode().iloc[0], inplace=True)
print(match_info_df.isnull().sum())

# COMMAND ----------


# Missing values count - 
print(teams_df.isnull().sum())

# Percentage of missing values
print((teams_df.isnull().sum() / len(teams_df)) * 100)

# Duplicates
print(teams_df.duplicated().sum())

# COMMAND ----------

from ydata_profiling import ProfileReport

# COMMAND ----------

player_profile = ProfileReport(players_df, title="IPL Players Profiling Report", explorative=True)

# COMMAND ----------

# MAGIC %pip install sweetviz
# MAGIC import sweetviz as sv

# COMMAND ----------

report = sv.analyze(players_df)

# COMMAND ----------

report.show_html("players_df.html")

# COMMAND ----------

report.show_html("players_df.pdf")

# COMMAND ----------

report_ball_by_ball_df = sv.analyze(ball_by_ball_df)

# COMMAND ----------

report_ball_by_ball_df.show_html("report_ball_by_ball_df.html")

# COMMAND ----------

report_ball_by_ball_df.show_html("report_ball_by_ball_df.pdf")

# COMMAND ----------

report_match_info_df = sv.analyze(match_info_df)

# COMMAND ----------

report_match_info_df.show_html("report_match_info_df.pdf")

# COMMAND ----------

report_teams_df = sv.analyze(teams_df)

# COMMAND ----------

report_teams_df.show_html("report_teams_df.pdf")

# COMMAND ----------

# MAGIC %md
# MAGIC Problem Statement 1: Top 10 Batsmen by Runs

# COMMAND ----------

top_batsmen = (
    ball_by_ball_df.groupby("Batter")["BatsmanRun"]
    .sum()
    .reset_index()
    .sort_values(by="BatsmanRun", ascending=False)
    .head(10)
)
print(top_batsmen)


# COMMAND ----------

# MAGIC %md
# MAGIC Problem Statement 2: Teams with Most Wins

# COMMAND ----------

team_wins = (
    match_info_df.groupby("winner")["match_number"]  # match_number as unique match ID
    .count()
    .reset_index()
    .rename(columns={"match_number": "wins"})
    .sort_values(by="wins", ascending=False)
)
print(team_wins)



# COMMAND ----------

# MAGIC %md
# MAGIC Statement 3: Top 10 Most Valuable Players (MVPs) by Player of the Match Awards

# COMMAND ----------

top_mvp = (
    match_info_df.groupby("player_of_match")["match_number"]
    .count()
    .reset_index()
    .rename(columns={"match_number": "awards"})
    .sort_values(by="awards", ascending=False)
    .head(10)
)
print(top_mvp)
