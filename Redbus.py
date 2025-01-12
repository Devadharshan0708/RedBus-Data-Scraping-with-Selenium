import pandas as pd
import mysql.connector
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import time
from PIL import Image

# kerala bus
lists_kerala=[]
df_k=pd.read_csv("df_k.csv")
for i,r in df_k.iterrows():
    lists_kerala.append(r["Route_name"])

#Andhra bus
lists_Aandhra=[]
df_a=pd.read_csv("df_a.csv")
for i,r in df_a.iterrows():
    lists_Aandhra.append(r["Route_name"])

#Telungana bus
lists_Telungana=[]
df_t=pd.read_csv("df_t.csv")
for i,r in df_t.iterrows():
    lists_Telungana.append(r["Route_name"])


#Rajastan bus
lists_Rajastan=[]
df_r=pd.read_csv("df_r.csv")
for i,r in df_r.iterrows():
    lists_Rajastan.append(r["Route_name"])


# South bengal bus 
lists_South_Bengal=[]
df_s=pd.read_csv("df_s.csv")
for i,r in df_s.iterrows():
    lists_South_Bengal.append(r["Route_name"])
    
# Punjab bus 
lists_Punjab=[]
df_pb=pd.read_csv("df_pb.csv")
for i,r in df_pb.iterrows():
    lists_Punjab.append(r["Route_name"])

# Haryana bus
lists_Haryana=[]
df_h=pd.read_csv("df_h.csv")
for i,r in df_h.iterrows():
    lists_Haryana.append(r["Route_name"])

#Assam bus
lists_Assam=[]
df_as=pd.read_csv("df_as.csv")
for i,r in df_as.iterrows():
    lists_Assam.append(r["Route_name"])

#Uttra_pradesh bus
lists_Uttra_pradesh=[]
df_up=pd.read_csv("df_up.csv")
for i,r in df_up.iterrows():
    lists_Uttra_pradesh.append(r["Route_name"])

#West bengal bus
lists_West_bengal=[]
df_wb=pd.read_csv("df_wb.csv")
for i,r in df_wb.iterrows():
    lists_West_bengal.append(r["Route_name"])

# # Home page setting
st.set_page_config(page_title="Streamlit Home Page", layout="wide")

# Sidebar with columns
with st.sidebar:
    st.title("Navigation")
    choice = st.radio("Go to", ("🏠Home", "🚌Booking"))

# Main page content based on sidebar selection
if choice == "🏠Home":
    st.title("🏠Welcome to the Home Page")
    st.image("redbus new (1).png",width=500)
    st.title("Redbus Data Scraping with Selenium & Streamlit")
    st.subheader(":blue[Domain:]  Transportation")
    st.subheader(":blue[Skill-take:]")
    st.markdown("Selenium, Python, Pandas, XAMPP,mysql-connector-python, Streamlit.")
    st.subheader(":blue[Developed-by:]  Devadharshan R")
elif choice == "🚌Booking":
    st.title("Routes Information")
    st.write("This section can be used to display information about Bus routes,Bus Type, Bus Timing.")

# Footer or any additional content
st.markdown("---")

# # States and Routes page setting
if choice  == "🚌Booking":
    S = st.selectbox("Lists of States", ["Kerala", "Aandhra", "Telungana", "Punjab", "Rajastan", 
                                          "South_Bengal", "Haryana", "Assam", "Uttra_pradesh", "West_bengal"])
    
    col1,col2=st.columns(2)
    with col1:
        select_type = st.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
    with col2:
        select_fare = st.radio("Choose bus fare range", ("50-1000", "1000-2000", "2000 and above"))
    TIME=st.time_input("select the time")

    # Kerala bus fare filtering
    if S == "Kerala":
        K = st.selectbox("List of routes", lists_kerala)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "127.0.0.1",port = 3306,user = "root",password = "070820#deva")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM REDBUS.REDBUSdetails
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

        # Aandhra bus fare filtering
    if S == "Aandhra":
        K = st.selectbox("List of routes",lists_Aandhra)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "127.0.0.1",port = 3306,user = "root",password = "070820#deva")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM REDBUS.REDBUSdetails
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

        #Telungana bus fare filtering
    if S == "Telungana":
        K = st.selectbox("List of routes",lists_Telungana)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "127.0.0.1",port = 3306,user = "root",password = "070820#deva")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM REDBUS.REDBUSdetails
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

        #Goa bus fare filtering
    if S == "Punjab":
        K = st.selectbox("List of routes",lists_Punjab)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "127.0.0.1",port = 3306,user = "root",password = "070820#deva")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM REDBUS.REDBUSdetails
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

     #Rajastan bus fare filtering
    if S == "Rajastan":
        K = st.selectbox("List of routes",lists_Rajastan)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "127.0.0.1",port = 3306,user = "root",password = "070820#deva")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM REDBUS.bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

        #South_Bengal bus fare filtering
    if S == "South_Bengal":
        K = st.selectbox("List of routes",lists_South_Bengal)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "127.0.0.1",port = 3306,user = "root",password = "070820#deva")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM REDBUS.REDBUSdetails
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

     #Haryana bus fare filtering
    if S == "Haryana":
        K = st.selectbox("List of routes",lists_Haryana)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "127.0.0.1",port = 3306,user = "root",password = "070820#deva")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM REDBUS.REDBUSdetails
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

     # Assam bus fare filtering
    if S == "Assam":
        K = st.selectbox("List of routes",lists_Assam)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "127.0.0.1",port = 3306,user = "root",password = "070820#deva")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM REDBUS.REDBUSdetails
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

     # Uttra_pradesh bus fare filtering
    if S == "Uttra_pradesh":
        K = st.selectbox("List of routes",lists_Uttra_pradesh)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "127.0.0.1",port = 3306,user = "root",password = "070820#deva")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM REDBUS.REDBUSdetails
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

     # West_bengal bus fare filtering
    if S == "West_bengal":
        K = st.selectbox("List of routes",lists_West_bengal)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "127.0.0.1",port = 3306,user = "root",password = "070820#deva")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM REDBUS.REDBUSdetails
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)
