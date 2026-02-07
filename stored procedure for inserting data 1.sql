use tour_de_france;
Go
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
    @TimeTaken TIME,
    @Margin TIME,
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
            (Country, Rider, Team, TimeTaken, Margin,
             StagesWon, StagesLed, AvgSpeed,
             Height, Weight, Born, Died)
        VALUES
            (@Country, @Rider, @Team, @TimeTaken, @Margin,
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
