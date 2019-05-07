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
    Click "Run" to execute the query for both Aircloak and native. You can cancel a query by canceling the page load on your browser.
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

