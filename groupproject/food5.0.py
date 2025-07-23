import streamlit as st
import random
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(page_title="Smart Food Recommender", layout="centered")
st.title("🍽️ Smart Food Recommender")

# --- Country-Based Food Dictionary with Images ---
food_data = {
    "Malaysia": [
        {"name": "Nasi Lemak", "image": "https://upload.wikimedia.org/wikipedia/commons/6/63/Nasi_Lemak.jpg"},
        {"name": "Char Kway Teow", "image": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Char_kway_teow_served_on_banana_leaf.jpg"},
        {"name": "Roti Canai", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Roti_Canai.jpg"},
        {"name": "Satay", "image": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Satay.jpg"},
        {"name": "Laksa", "image": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Penang_Assam_Laksa.jpg"},
        {"name": "Cendol", "image": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Cendol_pulut.jpg"}
    ],
    "Japan": [
        {"name": "Sushi", "image": "https://upload.wikimedia.org/wikipedia/commons/6/60/Sushi_platter.jpg"},
        {"name": "Ramen", "image": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Ramen_in_Sapporo_20100101.jpg"},
        {"name": "Okonomiyaki", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Okonomiyaki_by_ayustety_in_Osaka.jpg"},
        {"name": "Tempura", "image": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Tempura_and_Soba.jpg"},
        {"name": "Takoyaki", "image": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Takoyaki_by_yomi955.jpg"},
        {"name": "Udon", "image": "https://upload.wikimedia.org/wikipedia/commons/f/fd/Udon_soup_with_tempura.jpg"}
    ]
}

# --- Food List Initialization ---
if "food_list" not in st.session_state:
    st.session_state.food_list = []
    st.session_state.food_images = {}
    for country, items in food_data.items():
        for dish in items:
            st.session_state.food_list.append(dish["name"])
            st.session_state.food_images[dish["name"]] = dish["image"]

# --- Country Selector ---
selected_country = st.selectbox("🌍 Select a country to explore its dishes", sorted(food_data.keys()))
st.subheader(f"🍴 Dishes from {selected_country}")
for dish in food_data[selected_country]:
    st.image(dish["image"], caption=dish["name"], use_column_width=True)

st.markdown("---")

# --- Spin Wheel Chart ---
def draw_spin_wheel(options):
    fig = go.Figure(data=[go.Pie(
        labels=options,
        values=[1]*len(options),
        hole=0.3,
        textinfo='label'
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
        if food_choice in st.session_state.food_images:
            st.image(st.session_state.food_images[food_choice], caption=food_choice)

with col2:
    if st.button("🤖 AI Suggestion"):
        hour = datetime.now().hour
        if hour < 11:
            suggestion = "Roti Canai"
        elif hour < 17:
            suggestion = "Sushi"
        else:
            suggestion = "Ramen"
        st.info(f"💡 AI Suggestion: Try **{suggestion}**")
        if suggestion in st.session_state.food_images:
            st.image(st.session_state.food_images[suggestion], caption=suggestion)

# --- Sidebar to Add Food ---
st.sidebar.header("➕ Add Your Own Food")
new_food = st.sidebar.text_input("Enter food name:")
new_image = st.sidebar.text_input("Optional: Image URL")

if st.sidebar.button("Add Food"):
    if new_food.strip():
        st.session_state.food_list.append(new_food.strip())
        if new_image.strip():
            st.session_state.food_images[new_food.strip()] = new_image.strip()
        st.sidebar.success(f"✅ {new_food.strip()} added!")
    else:
        st.sidebar.error("⚠️ Please enter a valid food name.")