-- Stage top 5 competetors every year
USE tour_de_france;

SELECT Rank, Year, Rider
FROM (
    SELECT 
        Rank,
        Year,
        Rider,
        ROW_NUMBER() OVER (PARTITION BY Year ORDER BY Rank ASC) AS rn
    FROM Finishers
) t
WHERE rn <= 5
ORDER BY Year, Rank;
