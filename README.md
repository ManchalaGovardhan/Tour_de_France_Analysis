🚴 Tour de France Data Analysis



📌 What is Tour de France?
        
        The Tour de France is the world’s most prestigious professional cycling race held annually, primarily in France.
        
        It spans ~3 weeks
        
        Consists of ~21 stages
        
        Cyclists compete for the lowest total time
        
        Includes flat, hilly, and mountain stages
        
        It is widely considered the most challenging and iconic event in professional cycling.

⚙️ How the Project Works (End-to-End Flow)

    This project is designed as a complete data pipeline + interactive analytics system.

                             ┌──────────────────────┐
                         │        User          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Streamlit App       │
                         │──────────────────────│
                         │ • View Insights      │
                         │ • Add New Data       │
                         └───────┬───────┬──────┘
                                 │       │
                 ┌───────────────┘       └───────────────┐
                 │                                       │
                 ▼                                       ▼
     ┌────────────────────────┐           ┌────────────────────────┐
     │ Fetch Data             │           │ Insert New Data         │
     │ (for Insights)         │           │ (User Input)            │
     └──────────┬─────────────┘           └──────────┬─────────────┘
                │                                    │
                ▼                                    ▼
        ┌────────────────────────┐         ┌────────────────────────┐
        │   Database (Raw)       │         │ Data Cleaning (Python) │
        │ (Relational Tables)    │         │ • Missing Values       │
        └──────────┬─────────────┘         │ • Invalid Data         │
                   │                       │ • Inconsistent Data    │
                   │                       └──────────┬─────────────┘
                   │                                  │
                   ▼                                  ▼
        ┌────────────────────────┐         ┌────────────────────────┐
        │ Streamlit Insights     │         │ Cleaned Tables         │
        │ (Auto Updated when     │         │ (Final Structured Data)│
        │  new data arrives)     │         └──────────┬─────────────┘
        └────────────────────────┘                    │
                                                     │
                                ┌────────────────────┼────────────────────┐
                                │                                         │
                                ▼                                         ▼
                      ┌────────────────────┐               ┌────────────────────────────┐
                      │     Power BI       │               │ SQL Validation (Manual)   │
                      │   (Direct Query)   │               │ • Checked by Developer    │
                      │   Auto Updates     │               │ • Ensures Accuracy        │
                      └─────────┬──────────┘               └─────────┬────────────────┘
                                │                                    │
                                └──────────────┬─────────────────────┘
                                               ▼
                                ┌────────────────────────────┐
                                │  Real-Time Insights         │
                                │ (Streamlit + Power BI)      │
                                └────────────────────────────┘
    
    
    
    🔹 1. User Interaction (Streamlit App)
    
        Users interact through a Streamlit application with two main options:
        
        I. Basic Information
        
        View key insights (top winners, fastest stages, etc.)
        
        Get a quick overview of Tour statistics
        
        II. Interact with Database
        
        Explore data dynamically
        
        Filter by year, stage, riders
        
        View historical data trends
    
    
    
    🔹 2. Data Visualization (Power BI)
    
        Interactive dashboards built using Power BI
        
        Connected using Direct Query
        
        Provides:
        
        Stage performance insights
        
        Winner analysis
        
        Time trends across years
        
    🔹 3. Data Validation (SQL)
    
        SQL queries are used to:
        
        Validate Power BI results
        
        Cross-check aggregations
        
        Ensure data accuracy
    
    🔹 4. Real-Time Updates
    
        When a new entry is added via Streamlit:
        
        Data is inserted into the database
        
        Cleaning functions are triggered automatically
        
        Power BI dashboards update instantly
        
        Streamlit insights refresh in real-time
        

🧠 Project Architecture (Deep Flow)
    📊 Data Source
    
        Dataset (~100,000 rows) from Maven Analytics
        
        Tables used:
        
        tdf_finishers.csv
        
        tdf_stages.csv
        
        tdf_tours.csv
        
        tdf_winners.csv
        
    🗄️ Database Design
    
        Relational database created
        
        Tables structured with proper relationships
        
        Data inserted using Python scripts
        👉 Refer: python_database.ipynb
    
    🧹 Data Cleaning
    
          Handled using reusable Python functions:
          
          Missing values
          
          Invalid entries
          
          Inconsistent formats
          
          Duplicate records
    
         📂 Files:
    
          cleaning_data.py
    
          cleaning_functions.py
    
        👉 These functions automatically clean new incoming data
    
    📈 Power BI Layer
    
          Cleaned data connected via Direct Query
          
          Dashboards created in: tourbi.pbix
          
          Provides real-time business insights
          
    📊 Data Analysis (SQL)
    
          SQL queries written for:
          
          KPI validation
          
          Insight verification
          
          File: untitled.docx
          
    🌐 Streamlit Application
    
          Main app: app.py
          
          Features:
          
          Displays key insights
          
          Allows user interaction with data
          
          Inserts new data using stored procedures
          
          Shows historical data via database views
          
          Supporting files:
          
          stored_procedure_for_inserting_data.py
          
          functions_db.py
 <img width="1895" height="848" alt="image" src="https://github.com/user-attachments/assets/a505769f-fef2-4ef1-a15a-682ff8ccc960" /> <img width="1317" height="747" alt="image" src="https://github.com/user-attachments/assets/16541d95-602d-4800-b03c-46d13b926137" />
<img width="1322" height="726" alt="image" src="https://github.com/user-attachments/assets/fdbad926-4ed7-410a-944c-d8fdaf32b38d" />
<img width="1322" height="726" alt="image" src="https://github.com/user-attachments/assets/c381b81c-960d-4fce-999e-426f47bab5ac" />
<img width="1331" height="756" alt="image" src="https://github.com/user-attachments/assets/42e1696c-b53e-412c-bc1b-714b5d52a63d" />
<img width="1206" height="496" alt="image" src="https://github.com/user-attachments/assets/f9ef39d0-c2ed-45f2-bcb6-c2ef9b4bba13" />
![Uploading image.png…]()
<img width="1324" height="751" alt="image" src="https://github.com/user-attachments/assets/17bc63cd-2806-4348-9825-08ab29284349" />

