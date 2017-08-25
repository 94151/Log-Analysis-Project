#!/usr/bin/env python3

import psycopg2
# 1. What are the most popular three articles of all time?
ques_1 = 'What are the most popular three articles of all time?'
query_1 = """SELECT title, count(path) AS num FROM articles, \
                 log WHERE articles.slug = substring(path from 10 for 100)\
                 GROUP BY title ORDER BY num DESC LIMIT 3;;"""
# 2. Who are the most popular article authors of all time?
ques_2 = 'Who are the most popular article authors of all time?'
query_2 = '''WITH authors_count AS(select author, count(title) as views from articles
, log where log.path like concat('%',articles.slug)
GROUP BY author
order by views DESC)
select authors.name, authors_count.views from authors, authors_count
where authors.id = authors_count.author;
 '''
# 3. On which days did more than 1% of requests lead to errors?
ques_3 = 'On which days did more than 1% of requests lead to errors?'
query_3 = """
select * from (
    select a.day,
    round(cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2)
    as errp from
        (select date(time) as day, count(*) as hits from log group by day) as a
        inner join
        (select date(time) as day, count(*) as hits from log where status
        like '%404%' group by day) as b
    on a.day = b.day)
as t where errp > 1.0;
"""


class Problem:
    def __init__(self):
        try:
            self.db = psycopg2.connect('dbname=news')
            self.cursor = self.db.cursor()
        except Exception as e:
            print e

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def solve(self, ques, query, suffix='views'):
        query = query.replace('\n', ' ')
        result = self.execute_query(query)
        print ques
        for i in range(len(result)):
            print '\t', i + 1, '.', result[i][0], '--', result[i][1], suffix
        # blank line
        print ''

    def exit(self):
        self.db.close()


if __name__ == '__main__':
    problem = Problem()
    problem.solve(ques_1, query_1)
    problem.solve(ques_2, query_2)
    problem.solve(ques_3, query_3, '% error')
    problem.exit()
