import pandas as pd
import numpy as np
import streamlit as st
import datetime
from functions_db import(connect_to_db,basic_information,table_query_execution,add_tour_win,dist_year,Tour_history,add_stage,add_finisher)


# creating side bar
st.sidebar.title('Tour de france Dashboard')
button=st.sidebar.radio("select option",["basic information","interaction database"])


# creating main space
st.title("Tour De France Dashboard")
db=connect_to_db()
connection =db.connect()


# creating basic information dashboard
if button=="basic information":
    st.header("Basic information")
    basic_info=basic_information(connection)

# creating metric of 3 cols

    cols=st.columns(2)
    keys=list(basic_info.keys())



    for i in range(2):
        cols[i].metric(label=keys[i],value=basic_info[keys[i]])


# creating metric of another 3 col

    cols=st.columns(2)
    keys=list(basic_info.keys())



    for i in range(2,4):
        cols[i-2].metric(label=keys[i],value=basic_info[keys[i]])

# creating a divider
    st.divider()



# table insights
    tables=table_query_execution(connection)
    for labels,data in tables.items():
        st.header(labels)
        df=pd.DataFrame(data)
        st.dataframe(df)
        st.divider()

# ------------Operational task---------------#

elif button=="interaction database":
    st.header("Interaction database")
    selected_Task=st.selectbox("Choose a Task",['Add new tour details',"Add stage details",'Add finisher details','check history'])
    # ---------------------------------------if we select  add tour details------------------------------
    if selected_Task=='Add new tour details':
        st.header("Add new tour details")
        with st.form("Add new tour form"):
            tour_year=st.number_input("Year",min_value=1900,max_value=datetime.datetime.now().year)
            tour_date=st.date_input("Select Date")
            tour_stages=st.text_input("Select Stages")
            tour_distance=st.text_input("Select Distance")
            tour_starters=st.number_input("Select Starters")
            tour_finishers=st.number_input("Select Finishers")
            winner_country=st.text_input("Select Country")
            winner_rider=st.text_input("Select Rider")
            winner_team=st.text_input("Select Team")
            winner_time=st.text_input("Select Time")
            winner_margin=st.text_input("Select Margin")
            winner_stages_won=st.number_input("Select Stages Won")
            winner_stages_lead=st.number_input("Select Stages Lead")
            winner_avg_speed=st.number_input("Select Avg Speed")
            winner_height=st.number_input("Select Height in meters")
            winner_weight=st.number_input("Select Weight ")
            winner_born=st.date_input("Select Born")
            winner_died=st.date_input("select died date")
            submitted=st.form_submit_button("Submit")

            if submitted:
                if not tour_year:
                    st.error("Please select a year")
                else:
                    try:
                        add_tour_win(connection, tour_year,tour_date, tour_stages, tour_distance, tour_starters,tour_finishers,
                                     winner_country, winner_rider,winner_team, winner_time,winner_margin, winner_stages_won,
                                     winner_stages_lead, winner_avg_speed,winner_height,winner_weight,winner_born,winner_died)
                        st.success("tour {tour_year} added to database".format(tour_year=tour_year))
                    except Exception as e:
                        st.error("error while adding tour {tour_year}".format(tour_year=tour_year))

    # -----------------------if we select check history-------------------------
    if selected_Task=='check history':
        st.header("checking history")
        distinct_year=dist_year(connection)
        distinct_year=[p[0] for p in distinct_year]

    # creating select box
        selected_year=st.selectbox("Select Year",distinct_year)

        if selected_year:
            history=Tour_history(connection,selected_year)
            if history:
                df=pd.DataFrame(history)
                st.dataframe(df)
            else:
                st.info("no history for selected year")
    #-----------------stages form---------------------
    if selected_Task == 'Add stage details':
        st.header("Add new stage details")

        with st.form("Add new stage form"):
            stage_year = st.number_input("Year", min_value=1900, max_value=datetime.datetime.now().year)
            stage_date = st.date_input("Stage Date")
            stage_name = st.text_input("Stage Name")
            stage_course = st.text_input("Course")
            stage_distance = st.text_input("Distance")
            stage_type = st.text_input("Stage Type")
            stage_winner = st.text_input("Winner")

            submitted = st.form_submit_button("Submit")

            if submitted:
                if not stage_year or not stage_name or not stage_course:
                    st.error("Please fill all required fields")
                else:
                    try:
                        add_stage(
                            connection,
                            Year=stage_year,
                            StageDate=stage_date,
                            Stage=stage_name,
                            Course=stage_course,
                            Distance=stage_distance,
                            StageType=stage_type,
                            Winner=stage_winner
                        )
                        st.success(f"Stage {stage_name} for year {stage_year} added successfully!")
                    except Exception as e:
                        st.error(f"Error while adding stage {stage_name}: {e}")

    # --------------------------if user clicks finishers -------------------------
    if selected_Task == 'Add finisher details':
        st.header("Add new finisher details")

        with st.form("Add finisher form"):
            finisher_year = st.number_input("Year", min_value=1900, max_value=datetime.datetime.now().year)
            finisher_rank = st.text_input("Rank")
            finisher_rider = st.text_input("Rider Name")
            finisher_time_gap = st.text_input("Time Gap")
            finisher_team = st.text_input("Team")


            submitted = st.form_submit_button("Submit")

            if submitted:
                # Check required fields
                if not finisher_year or not finisher_rank or not finisher_rider:
                    st.error("Please fill all required fields")
                else:
                    try:
                        add_finisher(
                            connection,
                            Year=finisher_year,
                            rank=finisher_rank,
                            rider=finisher_rider,
                            time_gap=finisher_time_gap,
                            team=finisher_team

                        )
                        st.success(f"Finisher {finisher_rider} for year {finisher_year} added successfully!")
                    except Exception as e:
                        st.error(f"Error while adding finisher {finisher_rider}: {e}")
