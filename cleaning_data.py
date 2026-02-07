import pandas as pd
from sqlalchemy import create_engine
from cleaning_functions import (extract_start_date,extract_distance,total_time_seconds,margin_seconds,clean_avg_speed,
                                clean_height,clean_weight,stage_distance,clean_stage_type,extract_winner_name,clean_rider_name,
                                clean_timegap_seconds,clean_team,fix_stages,to_date,to_int)

# ---------------- DATABASE CONNECTION ----------------
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


# ---------------- CLEANING FUNCTION ----------------


def clean_tours_table(engine):
    print("Reading raw Tours table...")

    df = pd.read_sql("SELECT * FROM dbo.Tours", engine)


    print("Extracting Start_Date from Dates column...")
    df['Start_Date'] = df['Dates'].apply(extract_start_date)
    df['Stages'] = df['Stages'].apply(fix_stages)
    df['Distance(km)'] = df['Distance'].apply(extract_distance)
    df["Start_Date"] = df["Start_Date"].apply(to_date)

    print("Writing cleaned data to Cleaned_Tours table...")
    df.to_sql('Cleaned_Tours', engine, if_exists='replace', index=False)

    print("Tours table cleaned successfully!")

def clean_winners_table(engine):
    print("Reading raw Winners table...")
    df = pd.read_sql("SELECT * FROM dbo.Winners", engine)
    df['TimeTaken'] = df['TimeTaken'].apply(total_time_seconds)

    df['Margin'] = df['Margin'].apply(margin_seconds)

    df['AvgSpeed(km/h)'] = df['AvgSpeed'].apply(clean_avg_speed)
    df['Height(m)'] = df['Height'].apply(clean_height)
    df['Weight(kg)'] = df['Weight'].apply(clean_weight)
    df["Born"] = df["Born"].apply(to_date)
    df["TimeTaken"] = df["TimeTaken"].apply(to_int).astype("Int64")
    df["Margin"] = df["Margin"].apply(to_int) .astype("Int64")

    print("Writing cleaned data to Clean_Winners table...")
    df.to_sql('Cleaned_Winners', engine, if_exists='replace', index=False)

    print("Winners table cleaned successfully!")

def clean_stages_table(engine):

    print("Reading raw Stages table...")
    df = pd.read_sql("SELECT * FROM dbo.Stages", engine)


    #stages named 10 a and 10 b because they started on same day morning and after noon it majorly  happened before 1900
    # each day has seperate stages
    df['Distance(km)'] = df['Distance'].apply(stage_distance)
    df['Stage_type'] = df['StageType'].apply(clean_stage_type)
    df['Stage_winner'] = df['Winner'].apply(extract_winner_name)

    df["StageDate"] = df["StageDate"].apply(to_date)


    print("Writing cleaned data to Clean_Stages table...")
    df.to_sql('Cleaned_Stages', engine, if_exists='replace', index=False)

    print("Stages table cleaned successfully!")

def clean_finishers_table(engine):
    print("Reading raw Finishers table...")
    df = pd.read_sql("SELECT * FROM dbo.Finishers", engine)
    df['Rider'] = df['Rider'].apply(clean_rider_name)
    df['TimeGap'] = df['TimeGap'].apply(clean_timegap_seconds)

    df['Team'] = df['Team'].apply(clean_team)
    df['Rank'] = df['Rank'].apply(to_int).astype("Int64")
    df["TimeGap"] = df["TimeGap"].apply(to_int).astype("Int64")

    print("Writing cleaned data to Clean_Finishers table...")
    df.to_sql('Cleaned_Finishers', engine, if_exists='replace', index=False)

    print("Finishers table cleaned successfully!")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    engine = connect_to_db()
    clean_tours_table(engine)
    clean_winners_table(engine)
    clean_stages_table(engine)
    clean_finishers_table(engine)