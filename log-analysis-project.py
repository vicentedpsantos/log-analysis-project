#!/usr/bin/env python3

# importing module psycopg2
import psycopg2

# defining name of database to be used
DBNAME = "news"

try:
    db = psycopg2.connect(database=DBNAME)
except:
    print ("Unable to connect to the database")

articles_query = '''select count(*) as accesses, articles.title
from articles inner	join log on log.path like concat('%',
articles.slug, '%') where log.status = '200 OK' group
by articles.title order by accesses desc limit 3'''

authors_query = '''select authors.name, count(*) as accesses from
articles inner join log on log.path like concat('%', articles.slug,
'%') inner join authors on articles.author = authors.id
where log.status = '200 OK' group by authors.name order by accesses desc;'''

errors_query = '''select date, to_char(100.0*total_errors/
total_requests,'999D99%') as percentage from
requests_and_errors group by (date,total_errors,total_requests)
order by percentage limit 1;'''


def get_most_popular_articles():
    """Returns the most popular three articles of
    all times, by number of accesses"""
    cursor = db.cursor()
    cursor.execute(articles_query)
    top_three_articles = cursor.fetchall()
    print("The most popular three articles are:\n")
    for article in top_three_articles:
        print("Accesses: " + str(article[0]) + ";     Article: " +
              str(article[1]))


def get_most_popular_authors():
    """Returns the most popular authors of all time, list
    presented with most popular author at the top"""
    cursor = db.cursor()
    cursor.execute(authors_query)
    authors = cursor.fetchall()
    print("\n\nThe most popular authors are:\n")
    for author in authors:
        print("Author: " + str(author[0]) + ";     Accesses: " +
              str(author[1]))


def get_day_with_most_errors():
    """Returns the day on which more than 1% of
    errors occured, including a column with http code
    sent to browser"""
    cursor = db.cursor()
    cursor.execute(errors_query)
    day_with_most_errors = cursor.fetchall()
    print("\n\nThe day with most errors was:\n")
    for day in day_with_most_errors:
        print(str(day[0]) + " at " + str(day[1] + " of the total" +
              " requests."))

get_most_popular_articles()
get_day_with_most_errors()
get_most_popular_authors()
db.close()

