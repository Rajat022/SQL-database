# Case

## Overview

The goal of this case study is to query a SQL database and identify the countries that don't have any megapolis cities based on the population data available. The case study involves the following steps:

1. Connecting to the SQL Server database using the pyodbc library.
2. Fetching the city population data from an external source and loading it into a pandas DataFrame.
3. Creating a new table in the SQL database to store the city data.
4. Inserting the city data into the newly created table.
5. Querying the database to identify countries without megapolis cities.
6. Exporting the query result as a tab-separated value (TSV) file.
