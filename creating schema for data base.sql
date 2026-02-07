USE tour_de_france;
GO 
  
-- creating Table tours
CREATE TABLE dbo.Tours (
    [Year] INT PRIMARY KEY,
    Dates NVARCHAR(50),
    Stages NVARCHAR(50),
    Distance NVARCHAR(50),
    Starters INT,
    Finishers INT
);
GO


-- creating Stages
CREATE TABLE dbo.Stages (
    StageID INT IDENTITY(1,1) PRIMARY KEY,
    [Year] INT NOT NULL,
    StageDate NVARCHAR(300),
    Stage NVARCHAR(300),
    Course NVARCHAR(300),
    Distance NVARCHAR(100),
    StageType NVARCHAR(100),
    Winner NVARCHAR(150),

    CONSTRAINT FK_Stages_Tours
    FOREIGN KEY ([Year]) REFERENCES dbo.Tours([Year])
);
GO
-- creating winn table
CREATE TABLE dbo.Winners (
    [Year] INT PRIMARY KEY,
    Country NVARCHAR(50),
    Rider NVARCHAR(100),
    Team NVARCHAR(100),
    TimeTaken NVARCHAR(50),
    Margin NVARCHAR(50),
    StagesWon INT,
    StagesLed INT,
    AvgSpeed NVARCHAR(20),
    Height NVARCHAR(10),
    Weight NVARCHAR(10),
    Born NVARCHAR(20),
    Died NVARCHAR(20),

    CONSTRAINT FK_Winners_Tours
    FOREIGN KEY ([Year]) REFERENCES dbo.Tours([Year])
);
GO
-- Creating Finishers table with 
CREATE TABLE dbo.Finishers (
    [Year] INT NOT NULL,
    Rank NVARCHAR(100) NOT NULL,
    Rider NVARCHAR(100),
    TimeGap NVARCHAR(50),
    Team NVARCHAR(100),

    -- Foreign key
    CONSTRAINT FK_Finishers_Tours
    FOREIGN KEY ([Year]) REFERENCES dbo.Tours([Year]),
    
    -- UNIQUE constraint to prevent duplicate Year/Rank combinations
    CONSTRAINT UQ_Finishers_Year_Rank 
    UNIQUE ([Year], [Rank])
);
GO
