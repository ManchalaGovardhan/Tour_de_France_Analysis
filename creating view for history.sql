use tour_de_france;
Go
select * from Tours;
select * from Winners;
select * from Stages;
select * from Finishers;



-- for history
CREATE OR ALTER VIEW History AS
SELECT
    t.Year        AS Tour_year,
    t.Dates       AS Tour_date,
    t.Distance    AS Tour_distance,

    w.Country     AS Winning_country,
    w.Rider       AS Winner_name,
    w.Team        AS Winning_Team,
    w.TimeTaken,
    w.Margin,
    w.StagesWon,
    w.StagesLed,
    w.AvgSpeed,

    s.StageDate   AS Stage_date,
    s.Course      AS Stage_course,
    s.Distance    AS Stage_distance,
    s.StageType,
    s.Winner      AS Stage_winner,

    f.[Rank]      AS Rank_of_year_by_riders,
    f.Rider       AS Riders_name
FROM Tours AS t
JOIN Winners   AS w ON t.Year = w.Year
JOIN Stages    AS s ON t.Year = s.Year
JOIN Finishers AS f ON t.Year = f.Year;

 -- checking view
 select * from History where Tour_year=2013 order by Stage_date;