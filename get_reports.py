#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def get_query_results(this_query):
    try:
        conn = psycopg2.connect(database=DBNAME)
    except Exception as e:
        print("Can't connect to data base! -" + str(e.message))
        return []
    cur = conn.cursor()
    cur.execute(this_query)
    results = cur.fetchall()
    conn.close()
    return results


def Q1_get_top_3_articles():
    query = "select articles.slug, count(*) from log, articles where"
    "log.path ilike '%' || articles.slug || '%' group by articles.slug"
    "order by count desc limit 3;"
    results = get_query_results(query)
    return results


def Q2_author_popularity():
    query = "select authors.name, count(*) from log, authors, articles where"
    "log.path ilike '%' || articles.slug || '%' and authors.id="
    "articles.author group by articles.author, authors.id"
    "order by count desc;"
    results = get_query_results(query)
    return results


def Q3_days_over_one_percent_errors():
    query = "select date, ((1.0 * errCount)/allerrs) * 100 as"
    "percentage from(select time::date as date, sum(case when status like "
    "'4%%' then 1 else 0 end) errCount, count(*) allerrs from log group "
    "by time::date order by errCount desc) t;"
    results = get_query_results(query)
    return results
