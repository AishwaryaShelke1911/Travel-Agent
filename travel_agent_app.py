import streamlit as st
from datetime import date

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Smart Itinerary Travel Agent",
    page_icon="🧳",
    layout="wide"
)

# ---------------- CUSTOM FONT ---------------- #
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# ---------------- IMAGE FIX ---------------- #
def get_image(url):
    if not url:
        return "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?auto=format&fit=crop&w=1400&q=80"
    if "?" not in url:
        return url + "?auto=format&fit=crop&w=1400&q=80"
    return url

# ---------------- DATA ---------------- #

DESTINATIONS = {

    "Goa": {
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        "budget": {"Family": 3500, "Couple": 3000, "Solo": 2000, "Group": 2800},
        "stay": "Beachside Resort / Airbnb",
        "activities": [
            {"title": "Beaches", "details": ["Baga Beach", "Calangute Beach", "Anjuna Beach"]},
            {"title": "Food", "details": ["Britto’s", "Thalassa", "Fisherman’s Wharf"]},
            {"title": "Nightlife", "details": ["Tito’s Lane", "Club Cubana"]},
            {"title": "Forts", "details": ["Fort Aguada", "Chapora Fort"]},
            {"title": "Water Sports", "details": ["Parasailing Candolim", "Jet Ski Calangute"]}
        ]
    },

    "Manali": {
        "image": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
        "budget": {"Family": 4000, "Couple": 3500, "Solo": 2500, "Group": 3200},
        "stay": "Mountain Chalet",
        "activities": [
            {"title": "Temples", "details": ["Hadimba Temple", "Manu Temple"]},
            {"title": "Adventure", "details": ["Solang Valley", "Rohtang Pass"]},
            {"title": "Snow Sports", "details": ["Skiing", "Snowboarding"]},
            {"title": "Shopping", "details": ["Mall Road Market"]},
            {"title": "Food", "details": ["Cafe 1947", "Johnson’s Cafe"]}
        ]
    },

    "Jaipur": {
        "image": "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1",
        "budget": {"Family": 3200, "Couple": 2800, "Solo": 2000, "Group": 2600},
        "stay": "Heritage Haveli",
        "activities": [
            {"title": "Forts", "details": ["Amber Fort", "Nahargarh Fort"]},
            {"title": "Palaces", "details": ["City Palace", "Hawa Mahal"]},
            {"title": "Markets", "details": ["Johari Bazaar", "Bapu Bazaar"]},
            {"title": "Cultural Shows", "details": ["Chokhi Dhani"]},
            {"title": "Food", "details": ["LMB Restaurant", "Rawat Mishthan"]}
        ]
    },

    "Kerala": {
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        "budget": {"Family": 3600, "Couple": 3200, "Solo": 2200, "Group": 3000},
        "stay": "Houseboat Resort",
        "activities": [
            {"title": "Backwaters", "details": ["Alleppey", "Kumarakom"]},
            {"title": "Beaches", "details": ["Varkala Beach", "Kovalam Beach"]},
            {"title": "Wildlife", "details": ["Periyar Sanctuary"]},
            {"title": "Ayurveda", "details": ["Somatheeram Centre"]},
            {"title": "Food", "details": ["Paragon Restaurant", "Kashi Art Cafe"]}
        ]
    },

    "Mumbai": {
    "image": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f",
        "budget": {"Family": 3800, "Couple": 3400, "Solo": 2500, "Group": 3200},
        "stay": "City Hotel",
        "activities": [
            {"title": "Landmarks", "details": ["Gateway of India", "Marine Drive"]},
            {"title": "Markets", "details": ["Colaba Causeway", "Chor Bazaar"]},
            {"title": "Beaches", "details": ["Juhu Beach", "Girgaon Chowpatty"]},
            {"title": "Nightlife", "details": ["Bandra Clubs", "Lower Parel"]},
            {"title": "Food", "details": ["Leopold Cafe", "Cafe Mondegar"]}
        ]
    }
}

# ---------------- UI ---------------- #

st.title("🧳 Smart Itinerary Travel Agent")
st.caption("Plan your trip like booking an Airbnb")
st.divider()

destination = st.selectbox("📍 Choose Destination", list(DESTINATIONS.keys()))

travel_type = st.radio(
    "👥 Travel Type",
    ["Family", "Couple", "Solo", "Group"],
    horizontal=True
)

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("📅 Check-in Date", min_value=date.today())
with col2:
    end_date = st.date_input("📅 Check-out Date", min_value=date.today())

st.divider()

# ---------------- GENERATE PLAN ---------------- #

if st.button("✨ Generate Travel Plan", use_container_width=True):

    if end_date < start_date:
        st.error("Check-out date cannot be before check-in date")

    else:
        days = (end_date - start_date).days + 1
        data = DESTINATIONS[destination]

        total_budget = data["budget"][travel_type] * days

        st.image(get_image(data["image"]), use_container_width=True)
        st.success("Your personalized itinerary is ready!")

        with st.container(border=True):
            st.subheader("Trip Summary")
            st.write("Destination:", destination)
            st.write("Travel Type:", travel_type)
            st.write("Duration:", days, "days")
            st.write("Stay:", data["stay"])
            st.write("Estimated Budget: ₹", total_budget)

        st.subheader("Day-wise Plan")

        for i in range(days):
            activity = data["activities"][i % len(data["activities"])]
            with st.container(border=True):
                st.markdown(f"### Day {i+1}")
                st.markdown(f"**{activity['title']}**")
                for place in activity["details"]:
                    st.write("-", place)

        st.divider()
        st.caption("Tip: Book early for better prices ✈️")