# Logs Analysis
It contains source code for the Logs Analysis Project.

## Getting Started
These instructions will get the project up and running on your local machine for development and testing purposes.

### Prerequisites
* You must have a downloaded copy of the Project on your local system. It is a zip file so you will need to extract its contents.
* You must have the data downloaded on your system. You can get it from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
* You must have PostgreSQL installed on your system. You can get it from [here](https://www.python.org/downloads/).
* You will also need to have Python 2.7.x installed on your system. You can get it from [here](https://www.postgresql.org/download/).

## Project Description
The project is created as an internal reporting tool that answers some of the important question by analysing the provided data.

There are 3 main functions in the program that answer three questions respectively.

1.get\_popular_articles()

This function will return a list of top 3 articles and the number of views from the database.

2.get\_popular_authors()

This function will return a list of popular authors along with the number of views from the database.

3.get\_error_percentage()

This function will return the day of month along with the error percentage from the database where the error percentage is greater than 1%.

## Setting Up the Environment

Before we execute the program, there are certain things that are to be done.

1.Load the data using the following command.

```psql -d news -f newsdata.sql```

2.Create views in your database. The commands to create the required views are as follows:

```
CREATE VIEW stats AS
SELECT articles.author, COUNT(*) AS views
FROM articles,log
WHERE articles.slug = SUBSTRING(log.path,10)
GROUP BY articles.author
ORDER BY views DESC;
```
```
CREATE VIEW totalrequests AS
SELECT time::date, COUNT(*) AS requests
FROM log
GROUP BY time::date;
```
```
CREATE VIEW totalerrors AS
SELECT time::date, COUNT(status) AS errors
FROM log
WHERE status != '200 OK'
GROUP BY time::date
ORDER BY time::date ASC;
```
```
CREATE VIEW errorpercent AS
SELECT (totalerrors.errors*100)::numeric/totalrequests.requests AS percenterror, totalrequests.time
FROM totalrequests, totalerrors
WHERE totalrequests.time = totalerrors.time;
```
After following through with these steps, you are all set to execute the program.

## Execution

Open the Command Line and change directory to where you have stored the program file. Thereafter, type the following command:

```
python loganalysis_db.py
```

This will provide the desired result.

## Built With
* [Python 2.7.13](https://www.python.org/) - Programming language
* [Pycharm Community Edition](https://www.jetbrains.com/pycharm/) - IDE

## Author

* __Premanshu Pareek__ - [premanshupareek](https://github.com/premanshupareek)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

