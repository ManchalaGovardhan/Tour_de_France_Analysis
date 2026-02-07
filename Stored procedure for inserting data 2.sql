use tour_de_france;
Go 
-- dropig exted Add data stored procedure
DROP PROCEDURE IF EXISTS AddData;
GO


-- creating stored procedure  to add data into winners and Tours table
CREATE PROCEDURE AddData
(
    @Year INT,
    @DateOfTour DATE,
    @Stages NVARCHAR(255),
    @Distance NVARCHAR(255),
    @Starters INT,
    @Finishers INT,
    @Country NVARCHAR(150),
    @Rider NVARCHAR(150),
    @Team NVARCHAR(150),
    @TimeTaken NVARCHAR(150),
    @Margin NVARCHAR(150),
    @StagesWon INT,
    @StagesLead INT,
    @AverageSpeed FLOAT,
    @Height FLOAT,
    @Weight FLOAT,
    @Born DATE,
    @Died DATE
)
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        BEGIN TRANSACTION;

        -- Insert into Tours table
        INSERT INTO Tours
            ([Year], Dates, Stages, Distance, Starters, Finishers)
        VALUES
            (@Year, @DateOfTour, @Stages, @Distance, @Starters, @Finishers);

        -- Insert into Winners table
        INSERT INTO Winners
            (Year,Country, Rider, Team, TimeTaken, Margin,
             StagesWon, StagesLed, AvgSpeed,
             Height, Weight, Born, Died)
        VALUES
            (@Year,@Country, @Rider, @Team, @TimeTaken, @Margin,
             @StagesWon, @StagesLead, @AverageSpeed,
             @Height, @Weight, @Born, @Died);

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;

        -- Optional: return error details
        THROW;
    END CATCH
END;
GO



-- using stored procedure 

EXEC AddData
    @Year = 2023,
    @DateOfTour = '2023-07-01',
    @Stages = '21',
    @Distance = '3400 km',
    @Starters = 180,
    @Finishers = 150,
    @Country = 'France',
    @Rider = 'Sample Rider',
    @Team = 'Sample Team',
    @TimeTaken = '80:45:00',
    @Margin = '00:01:20',
    @StagesWon = 5,
    @StagesLead = 10,
    @AverageSpeed = 41.2,
    @Height = 1.78,
    @Weight = 70,
    @Born = '1995-05-10',
    @Died = NULL;


    select * from Tours where Starters='Sample Rider'