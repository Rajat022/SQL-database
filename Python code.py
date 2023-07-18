import pyodbc
import pandas as pd 
import datetime

# Check available ODBC drivers
pyodbc.drivers()

# Connecting SQL Server database
conn = pyodbc.connect(
    Trusted_Connection="Yes",
    Driver='{ODBC Driver 17 for SQL Server}',
    Server='STUDENT-LAPTOP\SQLEXPRESS',
    Database='Test'
)
cursor = conn.cursor()

# Read the CSV file directly from the URL into a DataFrame

url = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-all-cities-with-a-population-1000/exports/csv?lang=en&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B'

df = pd.read_csv(url, delimiter=';')
print(df.head())

# Create the table in the database
cursor.execute('''
    CREATE TABLE Country5 (
        [Geoname ID] INT,
        [Name] NVARCHAR(255),
        [ASCII Name] NVARCHAR(255),
        [Alternate Names] NVARCHAR(255),
        [Feature Class] NVARCHAR(50),
        [Feature Code] NVARCHAR(50),
        [Country Code] NVARCHAR(10),
        [Country name EN] NVARCHAR(255),
        [Country Code 2] NVARCHAR(255),  
        [Admin1 Code] NVARCHAR(20),
        [Admin2 Code] NVARCHAR(80),
        [Admin3 Code] NVARCHAR(20),
        [Admin4 Code] NVARCHAR(20),
        [Population] BIGINT,
        [Elevation] FLOAT,
        [DIgital Elevation Model] INTEGER,
        [Timezone] NVARCHAR(50),
        [Modification date] DATE,
        [LABEL EN] NVARCHAR(255),
        [Coordinates] NVARCHAR(255)
    )
''')

# Retrieve the column names of the table
cursor.execute("SELECT * FROM Country5")
columns = [column[0] for column in cursor.description]
print(columns)

# Insert data into the table from the DataFrame
for row in df.itertuples():
    
    # Truncate the Alternate Names if necessary
    alternate_names = row[4][:255]  # Limit the length to 255 characters

    # Convert the Modification date string to a datetime object
    modification_date_str = row[18]
    modification_date = datetime.datetime.strptime(modification_date_str, '%Y-%m-%d')

    # Execute the INSERT statement
    cursor.execute('''
        INSERT INTO Country5 ([Geoname ID], [Name], [ASCII Name], [Alternate Names], [Feature Class], [Feature Code], [Country Code], [Country name EN], [Country Code 2], [Admin1 Code], [Admin2 Code], [Admin3 Code], [Admin4 Code], [Population], [Elevation], [DIgital Elevation Model], [Timezone], [Modification date], [LABEL EN], [Coordinates])
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row[1], row[2], row[3], alternate_names, row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], modification_date, row[19], row[20]))
conn.commit()
