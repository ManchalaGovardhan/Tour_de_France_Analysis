-- creating a new stored procedure to add data into Stages
use tour_de_france;
Go


CREATE OR ALTER PROCEDURE AddStage
    @Year INT,
    @StageDate DATE,
    @Stage NVARCHAR(300),
    @Course NVARCHAR(300),
    @Distance NVARCHAR(100),
    @StageType NVARCHAR(100),
    @Winner NVARCHAR(150)
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        BEGIN TRANSACTION;

        INSERT INTO dbo.Stages
            (Year, StageDate, Stage, Course, Distance, StageType, Winner)
        VALUES
            (@Year, @StageDate, @Stage, @Course, @Distance, @StageType, @Winner);

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH
END;

Go

-- calling stored procedure
EXEC AddStage
    1903,
    '1903-07-01',
    'Stage 1',
    'Florence – Rimini',
    '206 km',
    'Flat',
    'Rider Name';


 -- creating add finishers stored procedure 



-- Create or alter the procedure
CREATE OR ALTER PROCEDURE AddFinishers
    @Year INT,
    @rank NVARCHAR(300),
    @rider NVARCHAR(300),
    @time_gap NVARCHAR(100),
    @team NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        BEGIN TRANSACTION;

        INSERT INTO Finishers(Year, [Rank], Rider, [TimeGap], Team)
        VALUES (@Year, @rank, @rider, @time_gap, @team);

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH
END;
GO

-- calling stored procedure AddFinishers
EXEC AddFinishers
    @Year = 1903,
    @rank = '1',
    @rider = 'Jonas Vingegaard',
    @time_gap = '00:02:15',
    @team = 'Jumbo-Visma',
 
