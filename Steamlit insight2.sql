use tour_de_france;
Go
-- completion rate
SELECT
    ROUND(AVG((Finishers * 100.0) / Starters),2) AS [avg completion %]
FROM Tours;

-- top winning country
select top 1 Country from Winners group by Country order by Count(*) desc;

-- top winner 
select top 1 Rider from Winners group by Rider order by Count(*) desc;

-- selecting year,country,winner 
select T.Year,W.Country, W.Rider from Tours as T left join Winners as W on T.Year=W.Year 

