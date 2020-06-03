# We use python here instead of JSON so that we have the convenience of writing queries verbatim.
exampleList = [
  {
    "heading": "Welcome",
    "description": '''
    <p class="desc">
Welcome to the Aircloak Training App. Use this app to understand how to make the best use of Aircloak's anonymization. Select from the topics listed on the left.
    <p class="desc">
This app accesses Aircloak through the postgres interface provided by the Aircloak system. It also accesses the raw data residing on a PostgreSQL server.
    <p class="desc">
For more information, see the <a target=_blank href="https://demo.aircloak.com/docs">online documentation for Aircloak.</a>
    <p class="desc">
Contact <b>solutions@aircloak.com</b> for access to the Aircloak SQL client.''',
    "dbname": "",
    "cloak": {
      "sql": ""
    },
    "native": {
      "sql": ""
    }
  },
  {
    "heading": "Using the app",
    "description": '''
    <p class="desc">
A series of examples are listed on the left. Each example provides SQL queries for both Aircloak and the native data. The blue SQL window below on the left is for Aircloak, while the green one on the right is for native PostgreSQL. You may modify the queries or write new ones. While the SQL syntax for Aircloak and native SQL is usually the same, this is not always the case.
    <p class="desc">
    For users new to the system, it is useful to take the examples in the order provided.
    <p class="desc">
    The app displays the results of a cached query. Click "Run" to re-execute the query for both Aircloak and native, or to execute any changes you made to the SQL.
    <p class="desc">
    This app has access to several different databases; <a target=_blank href="https://www.gda-score.org/resources/databases/czech-banking-data/">banking</a>, <a target=_blank href="https://www.gda-score.org/resources/databases/usa-census-database/">census0</a>, <a target=_blank href="https://www.gda-score.org/resources/databases/database-2/">scihub</a>, and <a target=_blank href="https://www.gda-score.org/resources/databases/database-1/">taxi</a>. You must select the appropriate database from the pull-down menu if you write a query.
    <p class="desc">
    The app indicates how many rows are in each answer, and the query execution time for each. However, the app displays only the first 100 rows of data
    <p class="desc">
    In addition to the query results for both Aircloak and native queries, the app usually displays the absolute and relative error between the noisy Aircloak and correct native answers. The error is not displayed in cases where there is no matching column value between the cloak and the native output for the displayed rows.
    ''',
    "dbname": "",
    "cloak": {
      "sql": ""
    },
    "native": {
      "sql": ""
    }
  },
  {
    "heading": "Schema exploration",
    "description": '''<p class="desc">Aircloak provides MySQL-like commands for exploring the schema.''',
    "dbname": "",
    "cloak": {
      "sql": ""
    },
    "native": {
      "sql": ""
    }
  },
  {
    "heading": "Show tables",
    "description": '''
<p class="desc">
Aircloak accepts the MySQL "SHOW tables" command.
<p class="desc">
Note that Aircloak indicates whether a table is
<a target=_blank href="https://demo.aircloak.com/docs/ops/configuration.html#insights-cloak-configuration">
personal or non-personal</a>. Non-personal tables are not anonymized.
<p class="desc">
The table <span style="font-family:'Courier New'">cli_names</span> does nothing more than associate the integer value in column
<span style="font-family:'Courier New'">cli_district_id</span>
with the name of the city for that district. It contains no user information and so is marked non-personal.
''',
    
    "dbname": "banking",
    "cloak": {
      "sql": '''
SHOW tables'''
    },
    "native": {
      "sql": '''
SELECT table_name
FROM information_schema.tables
WHERE table_schema='public'
AND table_catalog='banking' '''
    }
  },
  {
    "heading": "Show columns",
    "description": '''
<p class="desc">
Aircloak accepts the MySQL "SHOW columns FROM table" command.
<p class="desc">
In addition to the column name and type, Aircloak displays two additional attributes. The analyst needs to be aware of these attributes when writing certain queries.
<p class="desc">
The <b>key type</b> attribute has two roles. First, it indicates which column identifies the protected entity in the database (the entity whose anonynimity is being protected). This column has key type
<span style="font-family:'Courier New'">user_id</span>.
Second, it indicates which columns can be used in the 
<span style="font-family:'Courier New'">ON</span>
clause of a
<span style="font-family:'Courier New'">JOIN</span>
statement. Only columns with the same key type may be used for joining. For instance the
<span style="font-family:'Courier New'">cli_district_id</span>
column may only be joined with other tables that have a
<span style="font-family:'Courier New'">cli_district_id</span>
key type.
Read more 
<a target=_blank href="https://demo.aircloak.com/docs/sql/restrictions.html#join-restrictions">here</a>
and <a target=_blank href="https://demo.aircloak.com/docs/ops/configuration.html#insights-cloak-configuration">here</a>.
<p class="desc">
The <b>isolator?</b> attribute indicates that a column has a large proportion of values that are distinct to individual users. Additional SQL limitations are placed on isolator columns.
Read more 
<a target=_blank href="https://demo.aircloak.com/docs/sql/restrictions.html#isolating-columns">here</a>.
<p class="desc">
''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SHOW columns FROM accounts'''
    },
    "native": {
      "sql": '''
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name   = 'accounts' '''
    }
  },
  {
    "heading": "Basic queries",
    "description": '''<p class="desc">Listed here are a few of the most basic queries that can be executed with Aircloak.''',
    "dbname": "",
    "cloak": {
      "sql": ""
    },
    "native": {
      "sql": ""
    }
  },
  {
    "heading": "Counting users",
    "description": '''<p class="desc">Count the number of distinct users with bank accounts.''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT count(DISTINCT client_id)
FROM accounts'''
    },
    "native": {
      "sql": '''
SELECT count(DISTINCT client_id)
FROM accounts'''
    }
  },
  {
    "heading": "Counting rows",
    "description": '''<p class="desc">Count the number of rides in the taxi database (one ride per row).''',
    "dbname": "taxi",
    "cloak": {
      "sql": '''
SELECT count(*)
FROM jan08'''
    },
    "native": {
      "sql": '''
SELECT count(*)
FROM jan08'''
    }
  },
  {
    "heading": "Counting distinct values",
    "description": '''
<p class="desc">
Count the number of different countries from which SciHub downloads took place.
<p class="desc">
<font color="red"> Note that this query takes ten seconds or so</font>
''',
    "dbname": "scihub",
    "cloak": {
      "sql": '''
SELECT count(DISTINCT country)
FROM sep2015'''
    },
    "native": {
      "sql": '''
SELECT count(DISTINCT country)
FROM sep2015'''
    }
  },
  {
    "heading": "Histogram",
    "description": '''<p class="desc">Count the number of customers in each CLI District.''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT cli_district_id AS cli,
       count(DISTINCT client_id)
FROM accounts
GROUP BY 1
ORDER BY 1'''
    },
    "native": {
      "sql": '''
SELECT cli_district_id AS cli,
       count(DISTINCT client_id)
FROM accounts
GROUP BY 1
ORDER BY 1'''
    }
  },
  {
    "heading": "2D Histogram (heat map)",
    "description": '''
<p class="desc">
Histogram of counts of individuals by number of marriages per 5-year age group.
<p class="desc">
<font color="red">Note query takes around 1/2 minute</font>
''',
    "dbname": "census0",
    "cloak": {
      "sql": '''
SELECT bucket(age by 5) AS age, 
       marrno AS marriages,
       count(*)
FROM uidperhousehold
GROUP BY 1,2
ORDER BY 1,2
'''
    },
    "native": {
      "sql": '''
SELECT floor(age/5)*5 as age,
       marrno AS marriages,
       count(*)
FROM uidperhousehold
GROUP BY 1,2
ORDER BY 1,2
'''
    }
  },
  {
    "heading": "Sum",
    "description": '''<p class="desc">The total sum of all transaction amounts.
    <p class="desc">Aircloak also supports min, max, median, average, stddev, and variance. Try modifying the query for these different aggregates.''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT sum(amount)
FROM transactions'''
    },
    "native": {
      "sql": '''
SELECT sum(amount)
FROM transactions'''
    }
  },
  {
    "heading": "GROUP BY / nested SELECT",
    "description": '''<p class="desc">Builds a histogram of the number of users with different total transaction amounts.''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT bucket(sums by 20000) AS amount,
       count(*)
FROM (SELECT client_id,
             sum(amount) AS sums
      FROM transactions
      GROUP BY 1) t
GROUP BY 1
ORDER BY 1'''
    },
    "native": {
      "sql": '''
SELECT floor(sums/20000)*20000 AS amount,
       count(*)
FROM (SELECT client_id,
             sum(amount) AS sums
      FROM transactions
      GROUP BY 1) t
GROUP BY 1
ORDER BY 1'''
    }
  },
  {
    "heading": "JOIN",
    "description": '''<p class="desc">Builds a histogram of the number of users in each CLI District for users with an average account balance between 0 and 50000.''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT t3.cli_district_id AS cli,
       t3.city_name AS city,
       count(DISTINCT t1.client_id)
FROM (
    SELECT client_id, cli_district_id
    FROM accounts) t1
JOIN (
    SELECT client_id
    FROM transactions
    GROUP BY 1
    HAVING avg(balance)
           BETWEEN 0 AND 50000) t2
ON t1.client_id = t2.client_id
JOIN (
    SELECT cli_district_id, city_name
    FROM cli_names) t3
ON t1.cli_district_id = t3.cli_district_id
GROUP BY 1,2
ORDER BY 3 DESC
'''
    },
    "native": {
      "sql": '''
SELECT t3.cli_district_id AS cli,
       t3.city_name AS city,
       count(DISTINCT t1.client_id)
FROM (
    SELECT client_id, cli_district_id
    FROM accounts) t1
JOIN (
    SELECT client_id
    FROM transactions
    GROUP BY 1
    HAVING avg(balance)
           BETWEEN 0 AND 50000) t2
ON t1.client_id = t2.client_id
JOIN (
    SELECT cli_district_id, city_name
    FROM cli_names) t3
ON t1.cli_district_id = t3.cli_district_id
GROUP BY 1,2
ORDER BY 3 DESC
'''
    }
  },
  {
    "heading": "A common mistake",
    "description": '''
<p class="desc">
SELECT * FROM table LIMIT X
''',
    "dbname": "",
    "cloak": {
      "sql": ""
    },
    "native": {
      "sql": ""
    }
  },
  {
    "skip": False,
    "heading": "SELECT * ... LIMIT X",
    "description": '''
<p class="desc">
One of the first things an analyst may do when presented with a new database is:
<p class="desc">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<span style="font-family:'Courier New'">SELECT * ... LIMIT X</span>
<p class="desc">
This gives the analyst an immediate impression of what data he or she is dealing with.
<p class="desc">
Aircloak cannot return any useful information with this query, because it filters out any information related to one or a few users. Rather than attempt to run the query (which would take a very long time), Aircloak recognizes that the answer would contain nothing and returns an error message to that effect.
<p class="desc">
''',
    "dbname": "scihub",
    "cloak": {
      "sql": '''
SELECT *
FROM sep2015
ORDER BY uid
LIMIT 10
'''
    },
    "native": {
      "sql": '''
SELECT *
FROM sep2015
LIMIT 10
'''
    }
  },
  {
    "heading": "Noise",
    "description": '''
<p class="desc">
Aircloak adds noise to answers. The following set of examples illustrate how noise is added, how an analyst may guage how much noise is added, and potential pitfalls.
<p class="desc">
From these examples you will learn about:
<ul>
<li>&nbsp&nbsp&nbsp&nbspRandom noise, and how to determine its amount</li>
<li>&nbsp&nbsp&nbsp&nbspFlattening of extreme values (the amount of which cannot be determined)</li>
</ul>
<p class="desc">
The following examples are best selected in order.
''',
    "dbname": "",
    "cloak": {
      "sql": ""
    },
    "native": {
      "sql": ""
    }
  },
  {
    "heading": "aggr_noise()",
    "description": '''
<p class="desc">
Aircloak provides a set of aggregate functions that indicate how much noise it adds to each answer.
The available functions are 'count_noise()', 'sum_noise()', 'avg_noise()', 'stddev_noise()', and 'variance_noise()'.
They correspond to the functions 'count()', 'sum()', 'avg()', 'stddev()', and 'variance()'.
<p class="desc">
Aircloak adds random noise according to a Gaussian distribution ("bell curve"). The 'aggr_noise()' value is the standard deviation of the Gaussian sample.
<p class="desc">
From the query below, we see that a noise value with a standard deviation of 1.0 was added to the answer.
<p class="desc">
''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT count(DISTINCT client_id),
       count_noise(DISTINCT client_id)
FROM accounts
'''
    },
    "native": {
      "sql": '''
SELECT count(DISTINCT client_id)
FROM accounts
'''
    }
  },
  {
    "heading": "Noise per condition",
    "description": '''
<p class="desc">
Aircloak has a unique way of adding noise which we call "sticky layered noise".  Sticky means that the same query produces the same noise. Try re-running the query, and you will see that you get the same noisy answer every time.
<p class="desc">
Layered means that there are multiple noise values, one or two per condition.
The query here is the same as the previous, with the exception that one condition has been added. The amount of noise has increased from standard deviation 1.0 to sqrt(2), which Aircloak rounds to 1.4.
''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT count(DISTINCT client_id),
       count_noise(DISTINCT client_id)
FROM accounts
WHERE cli_district_id = 1
'''
    },
    "native": {
      "sql": '''
SELECT count(DISTINCT client_id)
FROM accounts
WHERE cli_district_id = 1
'''
    }
  },
  {
    "heading": "Two conditions",
    "description": '''
<p class="desc">
Now with two conditions, the noise increases to standard deviation of 2.0.
''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT count(DISTINCT client_id),
       count_noise(DISTINCT client_id)
FROM accounts
WHERE cli_district_id = 1 AND
      frequency = 'POPLATEK MESICNE'
'''
    },
    "native": {
      "sql": '''
SELECT count(DISTINCT client_id)
FROM accounts
WHERE cli_district_id = 1 AND
      frequency = 'POPLATEK MESICNE'
'''
    }
  },
  {
    "heading": "User-dependent",
    "description": '''
<p class="desc">
Aircloak adds enough noise to hide the influence of individual users. Often some users contribute more to the answer than other users. This wasn't the case in the previous three queries because we were counting distinct users, so every user contributed exactly one, and the amount of noise was enough to hide each user.
<p class="desc">
In this query, however, we are taking the sum total of the amount of all banking transactions, and users with more transactions at higher amounts contribute more to the answer. As a result, the amount of noise is enough to hide the heavy contributors. In this case, the standard deviation of the noise is in the millions! Correspondingly, the absolute error is similarly high. However, the relative error is still very small!
<p class="desc">
This better illustrates the need for the aggr_noise() functions, as it is otherwise troublesome for the analyst to have to figure out roughly how much the heavy hitting users contribute.
''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT sum(amount),
       sum_noise(amount)
FROM transactions
WHERE cli_district_id = 1 AND
      frequency = 'POPLATEK MESICNE'
'''
    },
    "native": {
      "sql": '''
SELECT sum(amount)
FROM transactions
WHERE cli_district_id = 1 AND
      frequency = 'POPLATEK MESICNE'
'''
    }
  },
  {
    "heading": "Extreme value flattening",
    "description": '''
<p class="desc">
It may have occurred to you that one could determine roughly what the extreme value is by looking at the aggr_noise() value. This would be a privacy violation.
<p class="desc">
This is not, however, the case. Before determining how much noise to add, Aircloak "flattens" the highest and lowest values so that they are similar in magnitude to at least a few other high and low values.
<p class="desc">
The query below is a good example of this. The absolute error is many times greater than the noise standard deviation.
Clearly there is more distortion here than can be accounted for by the random noise alone. The extra distortion is due to the fact that there is an extreme value in the answer: one user with an unusually high number of downloads (rows) compared to the other users. Aircloak lowers the answer roughly proportionally to the contribution of the extreme value. The next example gives more detail.
<p class="desc">
Note also that the relative error is higher than in previous examples. The reason for this is that there are not many distinct users comprising this answer, so the noise is relatively higher.
''',
    "dbname": "scihub",
    "cloak": {
      "sql": '''
SELECT count(*),
       count_noise(*)
FROM sep2015
WHERE country = 'United States'
'''
    },
    "native": {
      "sql": '''
SELECT count(*)
FROM sep2015
WHERE country = 'United States'
'''
    }
  },
  {
    "heading": "-&nbsp&nbsp&nbspMore detail",
    "description": '''
<p class="desc">
This query counts the number of users that had each number of downloads, and then displays them in descending order of number of downloads. Note that this would not necessarily be the best way to query the cloak for this data, but we do it here primarily to show that a single user has an extreme number of downloads, nearly double that of the next user.
<p class="desc">
This query also illustrates why the relative error of the previous query is high: the extreme value itself accounts for 16% of the total downloads in this case. Aircloak necessarily hides this user (as would any anonymization mechanism), and so a high error is unavoidable.
''',
    "dbname": "scihub",
    "cloak": {
      "sql": '''
SELECT downloads, count(*)
FROM (
    SELECT uid,
           count(*) AS downloads
    FROM sep2015
    WHERE country = 'United States'
    GROUP BY 1 ) t
GROUP BY 1
ORDER BY 1 DESC
'''
    },
    "native": {
      "sql": '''
SELECT downloads, count(*)
FROM (
    SELECT uid,
           count(*) AS downloads
    FROM sep2015
    WHERE country = 'United States'
    GROUP BY 1 ) t
GROUP BY 1
ORDER BY 1 DESC
'''
    }
  },
  {
    "heading": "Suppression",
    "description": '''
<p class="desc">
Aircloak suppresses answers that pertain to too few individuals. The following set of example illustrate this anonymization feature.
''',
    "dbname": "",
    "cloak": {
      "sql": ""
    },
    "native": {
      "sql": ""
    }
  },
  {
    "heading": "Text",
    "description": '''
<p class="desc">
This example queries for the number of users with each last name and displays them in descending order.
<p class="desc">
Simply adding noise to an answer is not enough to preserve anonymity. If there is only one user in the database with a given last name, then merely displaying this last name would break anonymity.
<p class="desc">
The native answer here shows that there are 3895 distinct last names (rows) in the database. Aircloak, however, only reveals only a fraction of these names: those that are shared by multiple users. The remaining names are hidden.
<p class="desc">
To inform the analyst that last names have been suppressed, and to give an indication of how much data has been suppressed, Aircloak places all of the suppressed rows in a bucket labeled
&nbsp<span style="font-family:'Courier New'">*</span>&nbsp
and then displays the anonymized aggregate for that bucket.
<p class="desc">
For this query, essentially what happens is that all suppressed last names are replaced with the value
&nbsp<span style="font-family:'Courier New'">*</span>&nbsp
and then displayed as though
&nbsp<span style="font-family:'Courier New'">*</span>&nbsp
is a last name. From this we see that there are over 4100 users whose last names have been suppressed.
''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT lastname,
       count(DISTINCT client_id)
FROM accounts
GROUP BY 1
ORDER BY 2 DESC
'''
    },
    "native": {
      "sql": '''
SELECT lastname,
       count(DISTINCT client_id)
FROM accounts
GROUP BY 1
ORDER BY 2 DESC
'''
    }
  },
  {
    "heading": "Numbers",
    "description": '''
<p class="desc">
This is a similar kind of query, but this time displaying numbers instead of text.
<p class="desc">
In this case, rather than return
&nbsp<span style="font-family:'Courier New'">*</span>&nbsp
as the default symbol for identifying the suppression bucket, Aircloak returns
&nbsp<span style="font-family:'Courier New'">NULL</span>&nbsp
(which here is displayed as 'None' because of the python implementation). Aircloak can't return
&nbsp<span style="font-family:'Courier New'">*</span>&nbsp
for numbers because
&nbsp<span style="font-family:'Courier New'">*</span>&nbsp
is a string and therefore the wrong type.
<p class="desc">
Returning
&nbsp<span style="font-family:'Courier New'">NULL</span>&nbsp
as the suppression bucket label has the problem that database values that are really
&nbsp<span style="font-family:'Courier New'">NULL</span>&nbsp
and therefore may not be suppressed, would be mixed with suppressed (non-NULL) values. To avoid this confusion, the analyst can add a
&nbsp<span style="font-family:'Courier New'">WHERE ... IS NOT NULL</span>&nbsp
condition.
''',
    "dbname": "taxi",
    "cloak": {
      "sql": '''
SELECT pickup_latitude,
       count(*)
FROM jan08
WHERE pickup_latitude IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
'''
    },
    "native": {
      "sql": '''
SELECT pickup_latitude,
       count(*)
FROM jan08
GROUP BY 1
ORDER BY 2 DESC
'''
    }
  },
  {
    "heading": "-&nbsp&nbsp&nbspSmarter query",
    "description": '''
<p class="desc">
In cases where there is substantial suppression, the analyst may use the 'bucket()' function to avoid rows with too few users.
<p class="desc">
In the example below, the cloak output does show a suppression bucket (10th row labeled 'None'), but there are relatively few rows in this bucket.
<p class="desc">
Note that normally one would more likely order this output by pickup_latitude, but we order by count so as to illustrate the reduced suppression.
''',
    "dbname": "taxi",
    "cloak": {
      "sql": '''
SELECT bucket(pickup_latitude BY 0.0001)
           AS lat,
       count(*)
FROM jan08
GROUP BY 1
ORDER BY 2 DESC
'''
    },
    "native": {
      "sql": '''
SELECT floor(pickup_latitude*10000)/10000
           AS latitude,
       count(*)
FROM jan08
GROUP BY 1
ORDER BY 2 DESC
'''
    }
  },
  {
    "heading": "Two columns",
    "description": '''
<p class="desc">
This query builds a 2-column histogram of number of rides from the number of riders and trip distance.
<p class="desc">
Aircloak attempts to display as much information as it can before suppressing.
Rather than suppress the values for both columns, it shows the value of the first (riders) column, and suppresses only the values of the second (distance) column.
This can be seen in the first six displayed rows.
''',
    "dbname": "taxi",
    "cloak": {
      "sql": '''
SELECT passenger_count AS riders,
       trip_distance AS distance,
       count(*) AS rides
FROM jan08
GROUP BY 1,2
'''
    },
    "native": {
      "sql": '''
SELECT passenger_count AS riders,
       trip_distance AS distance,
       count(*) AS rides
FROM jan08
GROUP BY 1,2
'''
    }
  },
  {
    "heading": "Two columns (reversed)",
    "description": '''
<p class="desc">
By default, Aircloak attempts to display as much as it can about columns to the left, and do suppression of values on columns to the right.  
This query is the same 2-column histogram, but with the position of the first and second columns reversed.
<p class="desc">
Here we see that Aircloak is showing distance values that were suppressed in the previous query, and suppressing rider counts instead.
''',
    "dbname": "taxi",
    "cloak": {
      "sql": '''
SELECT trip_distance AS distance,
       passenger_count AS riders,
       count(*) AS rides
FROM jan08
GROUP BY 1,2
'''
    },
    "native": {
      "sql": '''
SELECT trip_distance AS distance,
       passenger_count AS riders,
       count(*) AS rides
FROM jan08
GROUP BY 1,2
'''
    }
  },
  {
    "heading": "-&nbsp&nbsp&nbspSmarter query",
    "description": '''
<p class="desc">
Suppression can be reduced by placing values in buckets. In this case, we use the round function to place distance into buckets of one mile.
<p class="desc">
Though not displayed here, there is still a small amount of suppression (the native database outputs roughly 60 more rows than the cloak). Most of the information, however, is preserved by the cloak.
<p class="desc">
(Note that the cloak automatically casts the output of the 'round()' function as an integer. To align the output of the native and cloak queries here, we explicitly cast the native distance column as 'int'.)
''',
    "dbname": "taxi",
    "cloak": {
      "sql": '''
SELECT round(trip_distance) AS distance,
       passenger_count AS riders,
       count(*) AS rides
FROM jan08
GROUP BY 1,2
ORDER BY 1,2
'''
    },
    "native": {
      "sql": '''
SELECT round(trip_distance)::int
           AS distance,
       passenger_count AS riders,
       count(*) AS rides
FROM jan08
GROUP BY 1,2
ORDER BY 1,2
'''
    }
  },
  {
    "heading": "When to suppress?",
    "description": '''
<p class="desc">
The threshold for the number of distinct users at which Aircloak decides whether or not to suppress is not a hard threshold. Rather it is based on a sticky layered noise value with mean 4. In addition, Aircloak always suppresses rows for which only a single user contributes.
<p class="desc">
Put another way, any row reported by Aircloak has at least two distinct users, but a row with two distinct users may well not be reported.
<p class="desc">
This query illustrates the noisy threshold. The native answer lists the first 100 of the 197 last names for which exactly two users have the last name. The cloak answer not only displays far fewer names, but in fact very few if any of the names in fact have two distinct users.
<p class="desc">
The reason for this is that Aircloak adds noise <b>before</b> applying the
<span style="font-family:'Courier New'">HAVING</span>
filter.
As a result, most of the names that pass the
<span style="font-family:'Courier New'">HAVING</span>
filter don't have two users, and most of the names with two users don't pass the
<span style="font-family:'Courier New'">HAVING</span>
filter.
''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT lastname
FROM accounts
GROUP BY lastname
HAVING count(DISTINCT client_id) = 2
ORDER BY lastname DESC
'''
    },
    "native": {
      "sql": '''
SELECT lastname
FROM accounts
GROUP BY lastname
HAVING count(DISTINCT client_id) = 2
ORDER BY lastname DESC
'''
    }
  },
  {
    "heading": "Low aggregates",
    "description": '''
<p class="desc">
Aircloak avoids reporting aggregate results that would be unexpected or impossible without anonymization, for instance negative counts. By doing so, Aircloak not only makes its output more sensible for an analyst, but also avoids problems with business intelligence tools that would not know how to handle unexpected outputs.
<p class="desc">
Here we provide a couple examples.
<p class="desc">
<b>Bottom line: Avoid answers with very few distinct users</b>
''',
    "dbname": "",
    "cloak": {
      "sql": ""
    },
    "native": {
      "sql": ""
    }
  },
  {
    "heading": "True count = 1",
    "description": '''
<p class="desc">
With suppression, the cloak never reports column values where only a single user contributes to the value. In the query below, however, the analyst is not asking for a column value, but only a count. Normal SQL would produce an answer even if no database entries match the condition and the count is zero.
<p class="desc">
Since it would therefore be unexpected not to produce a count, the cloak does so. When an answer would otherwise have been suppressed, the cloak always reports a count of zero, and count_noise of NULL. The latter is necessary to avoid revealing information about a single user.
''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT count(*),
       count(DISTINCT client_id) AS users,
       count_noise(*)
FROM transactions
WHERE lastname = 'Adam'
'''
    },
    "native": {
      "sql": '''
SELECT count(*),
       count(DISTINCT client_id) AS users
FROM transactions
WHERE lastname = 'Adam'
'''
    }
  },
  {
    "heading": "Noisy count < 2",
    "description": '''
<p class="desc">
Since noise can be negative, it is possible to have a situation where the noise results in a negative count, which is unexpected. Furthermore, because of suppression, the cloak will never produce a answer that pertains to a single user. Therefore, a count of 1 or 0, though normally reasonable, is non-sensical in the context of Aircloak.
<p class="desc">
When the cloak reports a row with one or more column values, and the noisy count is one or less, the cloak automatically reports a value of 2. In addition, the cloak reports a count_noise of NULL. The NULL count_noise can serve as an indication that the count has been clipped.
<p class="desc">
This reporting rule can result in outputs that appear unusual at first glance. In the query below, we have intentionally selected names that have relatively few users in order to illustrate the reporting rule. The output appears unusual, because some lastnames are reported to have hundreds of transactions, while others are reported to have just two. Most of those reporting just two have been clipped. In these cases, the reported noise is NULL (None). This can serve as an indication that clipping has occured.
<p class="desc">
Note that in spite of the fact that the cloak query requests last names with only two distinct users each, most of the last names have three or four distinct users in reality. Analysts should avoid queries that have very few users per answer row.
''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT lastname,
       count(*),
       count_noise(*) AS noise
FROM transactions
GROUP BY lastname
HAVING count(DISTINCT client_id) = 2
ORDER BY lastname
'''
    },
    "native": {
      "sql": '''
SELECT lastname as name,
       count(*),
       count(DISTINCT client_id) AS users
FROM transactions
WHERE lastname in ('Aguilar', 'Andrews', 'Armstrong', 'Austin', 'Bishop', 'Boyd', 'Burke', 'Carlson', 'Doyle', 'Duncan', 'Duran', 'Elliott', 'Ellis', 'Guzman', 'Hayes', 'Holland', 'Howell', 'Jenkins', 'Jimenez', 'Kelley', 'Kennedy', 'Matthews', 'Mendez', 'Morales', 'Munoz', 'Obrien', 'Olson', 'Schultz', 'Vasquez', 'Wells')
GROUP BY 1
ORDER BY 1
'''
    }
  },
  {
    "heading": "Visit again!",
    "description": '''
<p class="desc">
We are constantly adding new examples, so visit again from time to time!
''',
    "dbname": "",
    "cloak": {
      "sql": ""
    },
    "native": {
      "sql": ""
    }
  }
]

def getExampleList():
    return exampleList

