#!/usr/bin/env python3

import get_reports


def print_top_articles():
    print("")
    getreports = get_reports.Q1_get_top_3_articles()
    print("The three most popular articles for all time are:")
    for x in getreports:
        print(x[0] + " @ " + str(x[1]) + " views")


def print_top_authors():
    print("")
    getreports2 = get_reports.Q2_author_popularity()
    print("The most popular article authors of all time are:")
    for g in getreports2:
        print(g[0] + " @ " + str(g[1]) + " views")


def print_top_error_days():
    print("")
    getreports3 = get_reports.Q3_days_over_one_percent_errors()
    print("More than 1% of the web led to errors on the following days:")
    for r in getreports3:
        if r[1] > 1.0:
            thisdate = r[0].strftime("%B %d, %Y")
            percent = str(round(r[1], 2))
            print(thisdate + " -- " + percent + "% errors")

if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_top_error_days()
