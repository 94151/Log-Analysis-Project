LOG-ANALYSIS is a part of FSND training program. In this project you will be able to short out some of the queries.

## INTRODUCTION

In this, we have to execute complex queries on a large database (> 1000k rows) to extract intersting stats.

The database in question is a newspaper company database where we have 3 tables; articles, authors and log.

articles - Contains articles posted in the newspaper so far.
authors - Contains list of authors who have published their articles.
log - Stores log of every request sent to the newspaper server.
This project implements a single query solution for each of the question in hand. See main.py for more details.

## RUNNING
Make sure you have newsdata.sql, the SQL script file with all the data. It can be downloaded from the Udacity course page.

Then run the following command to execute it in news database. You might have to create the database before-hand.

`psql -d news -f newsdata.sql`
Finally run the script.
`python2 main.py`
It will present you with necessary stats.

## HERE YOU HAVE TO GIVEN FOLLOWING QUERIES WHICH YOU NEED TO SOLVE IT.

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.)

Example:

July 29, 2016 — 2.5% errors

