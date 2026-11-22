import streamlit as st
from datetime import date
from app.data import DESTINATIONS
from app.planner import calculate_budget, generate_day_plan


def run_ui():

    st.title("🧳 Smart Itinerary Travel Agent")
    st.caption("Plan your trip like booking an Airbnb")
    st.divider()

    destination = st.selectbox("Choose Destination", list(DESTINATIONS.keys()))

    travel_type = st.radio(
        "Travel Type",
        ["Family", "Couple", "Solo", "Group"],
        horizontal=True
    )

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Check-in", min_value=date.today())
    with col2:
        end_date = st.date_input("Check-out", min_value=date.today())

    if st.button("Generate Travel Plan"):

        if end_date < start_date:
            st.error("Check-out date cannot be before check-in date")
            return

        days = (end_date - start_date).days + 1
        data = DESTINATIONS[destination]

        total_budget = calculate_budget(data, travel_type, days)

        st.image(data["image"], use_container_width=True)
        st.success("Your itinerary is ready!")

        st.subheader("Trip Summary")
        st.write("Destination:", destination)
        st.write("Duration:", days, "days")
        st.write("Stay:", data["stay"])
        st.write("Budget: ₹", total_budget)

        st.subheader("Day-wise Plan")

        for i in range(days):
            activity = generate_day_plan(data, i)
            with st.container(border=True):
                st.markdown(f"### Day {i+1}")
                st.markdown(f"**{activity['title']}**")
                for place in activity["details"]:
                    st.write("-", place)