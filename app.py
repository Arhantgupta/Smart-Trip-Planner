import streamlit as sl
from weather import get_weather
from attractions import get_attractions
from planner import generate_planner
from budget_helper import get_budget_tips
import folium
from streamlit_folium import st_folium
from maps import get_coordinates
from pdf_generator import create_pdf

sl.title("✈️ Smart Trip Planner")

destination= sl.text_input("Enter Destination")

days= sl.number_input("Enter number of days of stay", min_value=1, max_value=15, value=3)

budget= sl.number_input("Enter Budget", min_value=1000, value=5000, step=500)

if "generated" not in sl.session_state:
    sl.session_state.generated = False


if destination.strip() == "":
    sl.warning("Please enter a destination.")

budget_per_day = budget//days

if budget_per_day <2000:
    trip_category = "Low"

elif budget_per_day <5000:
    trip_category = "Medium"

else:
    trip_category = "High"

if sl.button("Generate"):
    sl.session_state.generated = True

if sl.session_state.generated:

    weather = get_weather(destination)

    temp = weather["main"]["temp"]
    condition = weather["weather"][0]["main"]

    sl.success("Trip Generated!")

    sl.write(f"Destination: {destination}")
    sl.write(f"No of days: {days}")
    sl.write(f"Budget: {budget}")
    sl.write(f"Trip Category: {trip_category}")

    
    attractions = get_attractions(destination)

    plan = generate_planner(attractions, days)
    
    sl.subheader("Current Weather")

    sl.write(f"🌡️ Temp: {temp}°C")
    sl.write(f"☁️ Condition: {condition}")

    sl.subheader("💰 Budget Analysis")

    sl.write(f"Budget Per day: {budget_per_day}")
    sl.write(f"Trip Type: {trip_category}")

    tips = get_budget_tips(trip_category)

    sl.subheader("💡Budget Recommendations")

    for tip in tips:
        sl.write(f"➤ {tip}")
    
    lat,lon = get_coordinates(destination)

    sl.subheader("🗓️ Smart Trip Itinerary")

    for day_num, day_places in enumerate(plan, start=1):
        sl.write(f"### Day {day_num}")

        for place in day_places:
            sl.write(f"• {place}")
    
    map_obj = folium.Map(
        location=[lat,lon],
        zoom_start = 12
    )
    
    folium.Marker(
    [lat, lon],
    popup=destination,
    tooltip=destination,
    icon=folium.Icon(color="red",icon="plane" )
    ).add_to(map_obj)

    sl.subheader("📍Destination Map")

    st_folium(map_obj,width=700,height=500)

    pdf_file = create_pdf(destination,days,budget,trip_category,temp,condition,tips,plan)

    sl.subheader("📄Download Report")

    with open(pdf_file, "rb") as file:
        sl.download_button(label = "📄 Download Smart Trip Itinerary", 
                           data = file,
                           file_name = "Smart_Trip_Itinerary.pdf",
                           mime = "application/pdf")





    



