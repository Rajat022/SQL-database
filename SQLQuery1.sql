SELECT DISTINCT [Country name EN]
FROM Country5
WHERE [Country name EN] NOT IN (
    SELECT [Country name EN]
    FROM Country5
    WHERE Population > 10000000
	                   
);
