#!/usr/bin/python3

import psycopg2

DBNAME = "news"

print("-------------------------------------------------------------\n")
print("Internal Reporting Tool - Logs Analysis\n")
print("-------------------------------------------------------------\n")

print("\n 1. The most popular articles of all time are:")
print("-------------------------------------------------------------")


# Function to retrieve data on most popular articles of all time
def get_popular_articles():

    db = psycopg2.connect(database=DBNAME)  # Connect to the database
    c = db.cursor()
    c.execute('''select articles.title, count(*) as views
              from articles,log
              where articles.slug = substring(log.path,10)
              group by articles.title
              order by views desc limit 3''')
    ans1 = c.fetchall()  # Fetch results
    db.close()
    return ans1


results = get_popular_articles()

for row in results:
    print('* The article with title "'+row[0]+'" has '+str(row[1])+' views.')

print("\n 2. The most popular authors of all time are:")
print("-------------------------------------------------------------")


# Function to retrieve data on most popular authors of all time
def get_popular_authors():

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''select authors.name, stats.views
              from authors, stats
              where authors.id = stats.author''')
    ans2 = c.fetchall()
    db.close()
    return ans2


author = get_popular_authors()
for row in author:
    print("* The author "+row[0]+" has "+str(row[1])+" views.")

print("\n 3. Days on which more that 1% of requests led to errors:")
print("-------------------------------------------------------------")


# Function to find the days on which error percentage was greater than 1%
def get_error_percentage():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''select round(percenterror,2),time
              from errorpercent
              where percenterror > 2''')
    ans2 = c.fetchall()
    db.close()
    return ans2


errors = get_error_percentage()
for row in errors:
    print("* On "+str(row[1])+", "+str(row[0])+"% of requests led to errors.")
