import datetime

import pandas as pd
import streamlit as stl



df = pd.read_excel(io="Overall Daily Report.xlsx", engine="openpyxl",sheet_name="report",usecols="A:Q",nrows=1000)

summary = df.groupby(by=["Location"]).sum()[["Activity Utilize","Activity utilize in min","Down time in hrs"]]

stl.set_page_config(layout="wide")
stl.title("Summary Of Dashboard")
stl.markdown("##")

location = stl.sidebar.header("Please filter here").multiselect("Please select here",options=df["Location"].unique(),default=df["Location"].unique())
main_category = stl.sidebar.header("Please filter here").multiselect("Please select here",options=df["maincategory"].unique(),default=df["maincategory"].unique())

df_selection = df.query("Location ==@location & maincategory == @main_category")


activity_utilize = int(df_selection["Activity Utilize"].sum())
utilize_in_min = int(df_selection["Activity utilize in min"].sum())
downhrs_in_hrs = int(df_selection["Down time in hrs"].sum())


col1, col2,col3 = stl.columns(3)

with col1:
    stl.subheader(":red[Activity Utilize Hrs]" ,)
    stl.subheader(f"{activity_utilize} Hrs")

with col2:
    stl.subheader(":blue[Down Hours]")
    stl.subheader(f"{downhrs_in_hrs} Hrs")
with col3:
    stl.subheader(":green[Activity Utilize Mins]")
    stl.subheader(f":red[{utilize_in_min}] Hrs")

stl.markdown("---")


stl.dataframe(df_selection)
stl.download_button(label="Download",data=df_selection.to_csv().encode("utf-8"),file_name="report.csv",mime="text/csv")

stl.markdown("---")
stl.title("test title")

stl.date_input("Choose date here",datetime.datetime.now())
# KPI


