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
    In addition to the query results for both Aircloak and native queries, the app usually displays the absolute and relative error between the noisy Aircloak and correct native answers. The app indicates how many rows are in each answer, and the query execution time for each. However, the app displays only the first 150 rows of data''',
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
personal or non-personal</a>. Non-personal tables are not anonymized.''',
    
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
The <b>key type</b> attributes indicates which column identifies the protected entity in the database (the entity whose anonynimity is being protected). We refer to this entity as the "user".
<p class="desc">
The <b>isolator?</b> attribute indicates that a column has a large proportion of values that are distinct to individual users. Additional SQL limitations are placed on isolator columns. Read more 
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
    "heading": "Basic Queries",
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
<font color="red"> Note that this query takes a few tens of seconds </font>
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
SELECT cli_district_id AS cli,
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
GROUP BY 1
ORDER BY 2 DESC
'''
    },
    "native": {
      "sql": '''
SELECT cli_district_id AS cli,
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
GROUP BY 1
ORDER BY 2 DESC
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
    "heading": "SELECT * ... LIMIT X",
    "description": '''
<p class="desc">
One of the first things an analyst may do when presented with a new database is "SELECT * ... LIMIT X". This gives the analyst an immediate impression of what data he or she is dealing with.
<p class="desc">
With Aircloak this query neither gives an impression nor is immediate. Instead, it may take a very long time to tell the analyst nothing. In this query on the scihub dataset, the cloak aborted the query after roughly two minutes.
<p class="desc">
It doesn't give an impression because Aircloak suppresses data that pertains to too few individuals. Rather, analysts need to formulate queries that naturally result in aggregate values with at least several users.
<p class="desc">
It is not immediate because Aircloak applies LIMIT only after retrieving the data from the database. for "SELECT *", this means all rows!
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
    "heading": "Another way",
    "description": '''
<p class="desc">
By putting the LIMIT clause in a sub-query, the database does the limiting rather than the cloak. As a result much less data is transferred from the database to the cloak, and the query executes quickly.
<p class="desc">
However, the resulting data is still not useful because the cloak suppresses the values pertaining to too few individuals.
<p class="desc">
Note by the way that Aircloak requires an ORDER BY clause along with the LIMIT clause.
''',
    "dbname": "scihub",
    "cloak": {
      "sql": '''
SELECT *
FROM (
    SELECT *
    FROM sep2015
    ORDER BY uid
    LIMIT 10 ) t
'''
    },
    "native": {
      "sql": '''
SELECT *
FROM (
    SELECT *
    FROM sep2015
    LIMIT 10 ) t
'''
    }
  },
  {
    "heading": "Understanding noise",
    "description": '''
<p class="desc">
Aircloak adds noise to answers. The following set of examples illustrate how noise is added, how an analyst may guage how much noise is added, and potential pitfalls.
<p class="desc">
These examples illustrate:
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
From the query below, we see that a noise value with a standard deviation of 1.0 was added to the answer. In this particular case, it was not enough to modify the resulting count, but an analyst wouldn't normally know that.
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
The query here is the same as the previous, with the exception that one condition has been added (Aircloak treats a pair of inequalities as one condition). The amount of noise has increased from standard deviation 1.0 to sqrt(2), which Aircloak rounds to 1.4.
''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT count(DISTINCT client_id),
       count_noise(DISTINCT client_id)
FROM accounts
WHERE cli_district_id >= 0 AND
      cli_district_id < 50
'''
    },
    "native": {
      "sql": '''
SELECT count(DISTINCT client_id)
FROM accounts
WHERE cli_district_id >= 0 AND
      cli_district_id < 50
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
WHERE cli_district_id >= 0 AND
      cli_district_id < 50 AND
      frequency = 'POPLATEK MESICNE'
'''
    },
    "native": {
      "sql": '''
SELECT count(DISTINCT client_id)
FROM accounts
WHERE cli_district_id >= 0 AND
      cli_district_id < 50 AND
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
In this query, however, we are taking the sum total of the amount of all banking transactions, and users with more transactions at higher amounts contribute more to the answer. As a result, the amount of noise is enough to hide the heavy contributors. In this case, the standard deviation of the noise is around 5.4 million! Correspondingly, the absolute error is around 8 million. However, the relative error is still small (less than one tenth of a percent)!
<p class="desc">
This better illustrates the need for the aggr_noise() functions, as it is otherwise troublesome for the analyst to have to figure out roughly how much the heavy hitting users contribute.
''',
    "dbname": "banking",
    "cloak": {
      "sql": '''
SELECT sum(amount),
       sum_noise(amount)
FROM transactions
WHERE cli_district_id >= 0 AND
      cli_district_id < 50 AND
      frequency = 'POPLATEK MESICNE'
'''
    },
    "native": {
      "sql": '''
SELECT sum(amount)
FROM transactions
WHERE cli_district_id >= 0 AND
      cli_district_id < 50 AND
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
The query below is a good example of this. The noise has a standard deviation of 1250, and yet the absolute error is over 30K. Clearly there is more distortion here than can be accounted for by the random noise alone. The extra distortion is due to the fact that there is an extreme value in the answer: one user with an unusually high number of downloads (rows) compared to the other users. Aircloak lowers the answer roughly proportionally to the contribution of the extreme value. This can be seen in the next example.
<p class="desc">
Note also that the relative error, nearly 15%, is higher than in previous examples. The reason for this is that there are not many distinct users comprising this answer, so the noise is relatively higher.
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
This query also illustrates why the relative error of the previous query is high (15%): the extreme value itself accounts for 16% of the total downloads in this case. Aircloak necessarily hides this user (as would any anonymization mechanism), and so a high error is unavoidable.
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
    "heading": "",
    "description": '''<p class="desc">''',
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

