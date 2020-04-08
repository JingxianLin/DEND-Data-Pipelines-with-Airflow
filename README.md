### Project Summary
A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.
You are tasked with creating high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills.

### Database Schema
To complete the project, create a star schema optimized for queries on song play analysis. This includes the following tables.

## Staging Tables
staging_events

staging_songs

## Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

## Dimension Tables
users - users in the app user_id, first_name, last_name, gender, level

songs - songs in music database song_id, title, artist_id, year, duration

artists - artists in music database artist_id, name, location, latitude, longitude

time - timestamps of records in songplays broken down into specific units start_time, hour, day, week, month, year, weekday

## Template Files
The dag template has all the imports and task templates

The operators folder with operator templates

A helper class for the SQL transformation

## Steps to Follow
Create custom operators to perform tasks such as staging the data, filling the data warehouse, and running checks on the data as the final step.

Configure the task dependencies so that after the dependencies are set, the graph view follows the flow showing the dependencies.

## ETL Pipeline
Load data from S3 to staging tables on Redshift.

Load data from staging tables to analytics tables on Redshift.