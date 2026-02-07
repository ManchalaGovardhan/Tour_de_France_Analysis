from sqlalchemy import create_engine
from sqlalchemy import text


# connecting to database
def connect_to_db():
    server = "GOVARDHAN\\SQLEXPRESS"
    database = "tour_de_france"

    engine = create_engine(
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&trusted_connection=yes"
    "&Encrypt=yes"
    "&TrustServerCertificate=yes"
    )

    return engine
connection =connect_to_db().connect()

# basic imformation of statistics for cards
def basic_information(connection):
  queries =  {
    "Total Editions": "SELECT COUNT(*) FROM Tours",
    "completion rate":"SELECT ROUND(AVG((Finishers * 100.0) / NULLIF(Starters, 0)),2) AS [avg completion %] FROM Tours",
    "top winning country":"select top 1 Country from Winners group by Country order by Count(*) desc",
    "top winner":"select top 1 Rider from Winners group by Rider order by Count(*) desc"

}
  results={}
  for title, query in queries.items():
    res = connection.execute(text(query))
    results[title] = res.scalar()
  return results




# insights in form of tables
def table_query_execution(connection):
    queries = {
        'winners of year': '''
            SELECT T.Year, W.Country, W.Rider
            FROM Tours AS T
            LEFT JOIN Winners AS W
            ON T.Year = W.Year
        ''',
        'Stage top 5 competitors every year': '''
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
            ORDER BY Year, Rank
        '''
    }

    results = {}

    for title, query in queries.items():
        result_proxy = connection.execute(text(query))
        results[title] = result_proxy.mappings().all()  # full result set

    return results



# adding data to tour win data table
def add_tour_win(connection, Year, Dates, Stages, Distance, Starters, Finishers,
                 Country, Rider, Team, TimeTaken, Margin, StagesWon,
                 StagesLed, AvgSpeed, Height, Weight, Born, Died):

    AddData_call = text("""
        EXEC AddData
        :Year, :Dates, :Stages, :Distance, :Starters, :Finishers,
        :Country, :Rider, :Team, :TimeTaken, :Margin,
        :StagesWon, :StagesLed, :AvgSpeed, :Height, :Weight, :Born, :Died
    """)

    params = {
        "Year": Year,
        "Dates": Dates,
        "Stages": Stages,
        "Distance": Distance,
        "Starters": Starters,
        "Finishers": Finishers,
        "Country": Country,
        "Rider": Rider,
        "Team": Team,
        "TimeTaken": TimeTaken,
        "Margin": Margin,
        "StagesWon": StagesWon,
        "StagesLed": StagesLed,
        "AvgSpeed": AvgSpeed,
        "Height": Height,
        "Weight": Weight,
        "Born": Born,
        "Died": Died
    }

    # cursor.execute(...) equivalent
    connection.execute(AddData_call, params)

    # db.commit() equivalent
    connection.commit()

    # getting history of tour
# getting distinct year for history bar


def dist_year(connection):
    query = text("SELECT DISTINCT Year FROM Tours ORDER BY Year")
    result = connection.execute(query)
    return result.fetchall()


def Tour_history(connection, Year):
    query = text("""
        SELECT *
        FROM History
        WHERE Tour_year = :Year
        ORDER BY Stage_date
    """)

    result = connection.execute(query, {"Year": Year})
    return result.fetchall()


#-----------------Adding details to Stages Table---------------------------


def add_stage(connection, Year, StageDate, Stage, Course, Distance, StageType, Winner):
    AddStage_call = text("""
        EXEC AddStage
        :Year, :StageDate, :Stage, :Course, :Distance, :StageType, :Winner
    """)

    params = {
        "Year": Year,
        "StageDate": StageDate,
        "Stage": Stage,
        "Course": Course,
        "Distance": Distance,
        "StageType": StageType,
        "Winner": Winner
    }

    connection.execute(AddStage_call, params)
    connection.commit()

#-------------------adding data to Finishers function----------------------
def add_finisher(connection, Year, rank, rider, time_gap, team):
    AddFinisher_call = text("""
        EXEC AddFinishers
        :Year, :rank, :rider, :time_gap, :team
    """)

    params = {
        "Year": Year,
        "rank": rank,
        "rider": rider,
        "time_gap": time_gap,
        "team": team,

    }

    connection.execute(AddFinisher_call, params)
    connection.commit()
