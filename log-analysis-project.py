#! /usr/bin/env python3

import psycopg2
DBNAME = "news"

def get_most_popular_articles():
	"""Returns the most popular three articles of
	all times, by number of accesses"""
	db = psycopg2.connect(database=DBNAME)
	cursor = db.cursor()
	cursor.execute('''select count(*) as accesses, articles.title from articles inner 
	join log on log.path like concat('%', articles.slug, '%') where log.status 
	like '%200%' group by articles.title order by accesses desc limit 3;''')
	top_three_articles = cursor.fetchall()
	print("The most popular three articles are:\n")
	for article in top_three_articles:
  		print("Accesses: " + str(article[0])+ ";     Article: " + str(article[1]))

def get_most_popular_authors():
	"""Returns the most popular authors of all time, list
	presented with most popular author at the top"""
	db = psycopg2.connect(database=DBNAME)
	cursor = db.cursor()
	cursor.execute('''select authors.name, count(log.path) as accesses from articles,
	log, authors where log.path like concat('%', articles.slug, '%')
	and articles.author = authors.id group by authors.name order by 
	accesses desc;''')
	authors = cursor.fetchall()

	print("\n\nThe most popular authors are:\n")
	for author in authors:
		print("Author: " + str(author[0])+ ";     Accesses: " + str(author[1]))

def get_day_with_most_errors():
	"""Returns the day on which more than 1% of
	errors occured, including a column with http code
	sent to browser"""
	"""c.execute('''create view totalrequests as select count(*) as total, date(TIME) 
	as date from log group by date;''')
	c.execute('''create view errorrequests as select count(*) as total, date(TIME) 
	as date from log where status != '200 OK' group by date;''')
	c.execute('''create view requests_and_errors as select sum(errorrequests.total) 
	as total_errors, sum(totalrequests.total) as total_requests, errorrequests.date 
	from errorrequests, totalrequests where errorrequests.date = totalrequests.date 
	group by errorrequests.date;''')"""
	db = psycopg2.connect(database=DBNAME)
	cursor = db.cursor()
	cursor.execute('''select date, to_char(100.0*total_errors/total_requests,'999D99%') 
	as percentage from requests_and_errors group by (date,total_errors,total_requests) 
	order by percentage limit 1;''')

	day_with_most_errors = cursor.fetchall()

	print("\n\nThe day with most errors was:\n")
	for day in day_with_most_errors:
		print(str(day[0]) + " at " + str(day[1] + " of the total requests."))
    
get_most_popular_articles()
get_day_with_most_errors()
get_most_popular_authors()
