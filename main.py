import plotly.express as px
import streamlit as st
from weather_backend import get_location_data

# Add a title, text input, slider, selectbox, and a subheader
st.title("Weather Forecast")
location = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Forecast for how many days?")
option = st.selectbox("Which weather data would you like to view",
                      ("Temperature", "Conditions"))
st.subheader(f"{option} for the next {days} days in {location}")

if location:
    # Get the temperature/conditions data
    filtered_data = get_location_data(location, days)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Plot the temperature data
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Conditions":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(image_paths, width=115)