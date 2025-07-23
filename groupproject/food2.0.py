import streamlit as st
import random

# App title
st.title("Smart Food Recommender")

st.write("Choose a country and discover some delicious food!")

# Country selection
country = st.selectbox(
    "Select a country",
    ["Malaysia, Italy, Japan, India, Mexico"]
)

# Food data with descriptions and image URLs
food_data = {
    "Malaysia": [
        {"name": "Nasi Lemak", "desc": "A fragrant rice dish cooked in coconut milk.", "image": "https://upload.wikimedia.org/wikipedia/commons/6/63/Nasi_Lemak.jpg"},
        {"name": "Char Kway Teow", "desc": "Fried flat noodles with prawns and eggs.", "image": "https://upload.wikimedia.org/wikipedia/commons/4/45/Char_kway_teow.jpg"},
        {"name": "Roti Canai", "desc": "Flaky flatbread served with curry.", "image": "https://upload.wikimedia.org/wikipedia/commons/2/2c/Roti_Canai.jpg"},
        {"name": "Cendol", "desc": "Icy dessert with green jelly and palm sugar.", "image": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Cendol.jpg"}
    ],
    "Italy": [
        {"name": "Pizza", "desc": "Baked flatbread with tomato, cheese, and toppings.", "image": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Supreme_pizza.jpg"},
        {"name": "Pasta", "desc": "Noodles served with sauces like tomato or pesto.", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Spaghetti_al_Pomodoro.JPG"},
        {"name": "Risotto", "desc": "Creamy rice cooked with broth and ingredients.", "image": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Risotto_ai_funghi_%28Milan%29.jpg"},
        {"name": "Tiramisu", "desc": "Coffee-flavored layered dessert.", "image": "https://upload.wikimedia.org/wikipedia/commons/5/57/Tiramisu_-_Raffaele_Diomede.jpg"}
    ],
    "Japan": [
        {"name": "Sushi", "desc": "Rice rolls with fish and vegetables.", "image": "https://upload.wikimedia.org/wikipedia/commons/6/60/Sushi_platter.jpg"},
        {"name": "Ramen", "desc": "Noodle soup with meat, egg, and broth.", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Japanese_Ramen.jpg"},
        {"name": "Tempura", "desc": "Lightly battered and fried seafood/vegetables.", "image": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Tendon_Tempura_Bowl.jpg"},
        {"name": "Mochi", "desc": "Sticky rice cake dessert.", "image": "https://upload.wikimedia.org/wikipedia/commons/d/d2/Mochi_on_black_plate.jpg"}
    ],
    "India": [
        {"name": "Biryani", "desc": "Aromatic rice with spices and meat/vegetables.", "image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Biryani.jpg"},
        {"name": "Butter Chicken", "desc": "Creamy tomato-based chicken curry.", "image": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Chicken_makhani.jpg"},
        {"name": "Samosa", "desc": "Fried snack with potato filling.", "image": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Samosachutney.jpg"},
        {"name": "Gulab Jamun", "desc": "Sweet syrup-soaked dough balls.", "image": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Gulab_jamun_%28Gibraltar%2C_November_2021%29.jpg"}
    ],
    "Mexico": [
        {"name": "Tacos", "desc": "Folded tortillas with meat, cheese, and salsa.", "image": "https://upload.wikimedia.org/wikipedia/commons/9/91/Street_Tacos.jpg"},
        {"name": "Burritos", "desc": "Wrapped tortilla with rice, beans, and fillings.", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Burrito.JPG"},
        {"name": "Quesadillas", "desc": "Tortilla filled with cheese and grilled.", "image": "https://upload.wikimedia.org/wikipedia/commons/4/41/Quesadillas.JPG"},
        {"name": "Churros", "desc": "Fried dough dessert with sugar and cinnamon.", "image": "https://upload.wikimedia.org/wikipedia/commons/8/89/Churros_Madrid.jpg"}
    ]
}

# Show all dishes
st.subheader(f"🍽 Recommended {country} Dishes:")

for dish in food_data[country]:
    st.image(dish["image"], width=250)
    st.markdown(f"**{dish['name']}**")
    st.write(dish["desc"])
    st.markdown("---")

# Random recommendation
if st.button("🎲 Give me a random dish!"):
    random_dish = random.choice(food_data[country])
    st.success(f"How about trying **{random_dish['name']}**?")
    st.image(random_dish["image"], width=300)
    st.caption(random_dish["desc"])

# Random recommendation
if st.button("🎲 Give me a random dish!"):
    random_dish = random.choice(food_data[country])
    st.success(f"How about trying **{random_dish['name']}**?")
    st.image(random_dish["image"], width=300)
    st.caption(random_dish["desc"])


# Displaying the image
dish = food_data["Malaysia"][0]
st.image(dish["image"], width=250)
st.markdown(f"**{dish['name']}**")
st.write(dish["desc"])

st.write("Image URL:", dish["image"])
st.image(dish["image"], width=250)


import streamlit as st
import requests

st.title("Smart Food Recommender")
country = st.selectbox("Choose a country", ["Malaysia", "Japan", "Italy"])

if country == "Malaysia":
    dish_name = "nasi lemak"
elif country == "Japan":
    dish_name = "sushi"
elif country == "Italy":
    dish_name = "pizza"

# Get food info from TheMealDB
url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={dish_name}"
response = requests.get(url).json()
meal = response["meals"][0]

st.header(f"Recommended {country} Dish: {meal['strMeal']}")
st.image(meal["strMealThumb"], width=300)
st.write(meal["strInstructions"])