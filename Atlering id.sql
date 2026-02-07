use tour_de_france ;
select * from Winners;
select * from Stages;
select * from Tours;
select * from Finishers;

-- Add a new column
ALTER TABLE Finishers
ADD id INT IDENTITY(1,1);

-- Set it as primary key
ALTER TABLE Finishers
ADD CONSTRAINT PK_TDF PRIMARY KEY (id);

ALTER TABLE Finishers
DROP CONSTRAINT UQ_Finishers_Year_Rank;
