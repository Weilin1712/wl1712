import streamlit as st
import random
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(page_title="Smart Food Recommender", layout="centered")
st.title("🍽️ Smart Food Recommender")

# --- Country-Based Food Dictionary ---
food_data = {
    "Malaysia": ["Nasi Lemak", "Char Kway Teow", "Roti Canai", "Satay", "Laksa", "Cendol"],
    "Japan": ["Sushi", "Ramen", "Okonomiyaki", "Tempura", "Takoyaki", "Udon"],
    "Italy": ["Pizza", "Pasta Carbonara", "Tiramisu", "Lasagna", "Risotto", "Gelato"],
    "Korea": ["Kimchi", "Bibimbap", "Tteokbokki", "Samgyeopsal", "Japchae", "Kimbap"],
    "Thailand": ["Pad Thai", "Green Curry", "Tom Yum", "Som Tum", "Mango Sticky Rice", "Massaman Curry"],
    "India": ["Biryani", "Butter Chicken", "Samosa", "Masala Dosa", "Paneer Tikka", "Chole Bhature"],
    "China": ["Peking Duck", "Xiao Long Bao", "Mapo Tofu", "Hotpot", "Dim Sum", "Sweet and Sour Pork"],
    "France": ["Croissant", "Ratatouille", "Quiche Lorraine", "Bouillabaisse", "Crepes", "Macarons"],
    "Mexico": ["Tacos", "Guacamole", "Enchiladas", "Tamales", "Churros", "Pozole"],
    "USA": ["Burger", "Fried Chicken", "Hot Dog", "Mac and Cheese", "Buffalo Wings", "Apple Pie"]
}

# --- Food List State ---
if "food_list" not in st.session_state:
    st.session_state.food_list = [item for sublist in food_data.values() for item in sublist]

# --- Country Selector ---
selected_country = st.selectbox("🌍 Select a country to explore its dishes", sorted(food_data.keys()))
st.subheader(f"🍴 Dishes from {selected_country}")
for dish in food_data[selected_country]:
    st.markdown(f"- {dish}")

# --- Spin Wheel ---
def draw_spin_wheel(options):
    fig = go.Figure(data=[go.Pie(
        labels=options,
        values=[1]*len(options),
        hole=0.3,
        textinfo='label',
        marker=dict(colors=[
            "#FF9999", "#FFCC99", "#99FF99", "#66B3FF", "#C2C2F0",
            "#FFB3E6", "#FF6666", "#FFDB4D", "#D1B3FF", "#B2F0E6"
        ])
    )])
    fig.update_layout(showlegend=False, margin=dict(t=10, b=10, l=10, r=10))
    return fig

st.header("🎡 Spin the Wheel or Ask AI!")
st.plotly_chart(draw_spin_wheel(st.session_state.food_list), use_container_width=True)

# --- Buttons for Random & AI Suggestion ---
col1, col2 = st.columns(2)

with col1:
    if st.button("🎯 Random Pick!"):
        food_choice = random.choice(st.session_state.food_list)
        st.success(f"🎉 You should eat: **{food_choice}**")

with col2:
    if st.button("🤖 AI Suggestion"):
        hour = datetime.now().hour
        if hour < 11:
            st.info("🌞 Good morning! Try **Roti Canai**, **Kaya Toast**, or **Tamagoyaki**.")
        elif hour < 17:
            st.info("🌤️ It’s lunchtime! How about **Chicken Rice**, **Sushi**, or **Tacos**?")
        else:
            st.info("🌙 Dinner time! Consider **Ramen**, **Pasta**, or **Satay** tonight!")

# --- Sidebar to Add Food ---
st.sidebar.header("➕ Add Your Own Food")
new_food = st.sidebar.text_input("Enter food name:")

if st.sidebar.button("Add Food"):
    if new_food.strip():
        st.session_state.food_list.append(new_food.strip())
        st.sidebar.success(f"✅ {new_food.strip()} added!")
    else:
        st.sidebar.error("⚠️ Please enter a valid food name.")
