import psycopg2

DBNAME = "news"

def Q1_get_top_3_articles():
    try:
        conn = psycopg2.connect(database=DBNAME)
    except Exception as e:
        print("Can't connect to data base! -" + str(e.message))
    cur = conn.cursor()
    cur.execute("select articles.slug, count(*) from log, articles where log.path ilike '%' || articles.slug || '%'"
                " group by articles.slug order by count desc limit 3;")
    results = cur.fetchall()
    conn.close()
    return results

def Q2_author_popularity():
    try:
        conn = psycopg2.connect(database=DBNAME)
    except Exception as e:
        print("Can't connect to data base! -" + str(e.message))
    cur = conn.cursor()
    cur.execute("select authors.name, count(*) from log, authors, articles where log.path ilike '%' || articles.slug ||"
                "'%' and authors.id=articles.author group by articles.author, authors.id order by count desc;")
    results = cur.fetchall()
    conn.close()
    return results

def Q3_days_over_one_percent_errors():
    try:
        conn = psycopg2.connect(database=DBNAME)
    except Exception as e:
        print("Can't connect to data base! -" + str(e.message))
    cur = conn.cursor()
    cur.execute("select date, ((1.0 * errCount)/allerrs) * 100 as percentage from"
                "(select time::date as date, sum(case when status like '4%%' then 1 else 0 end) errCount,"
                "count(*) allerrs from log group by time::date order by errCount desc) t;")
    results = cur.fetchall()
    conn.close()
    return results

#print(Q1_get_top_3_articles())
#print(Q2_author_popularity())
#print(Q3_days_over_one_percent_errors())