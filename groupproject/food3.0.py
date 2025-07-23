import streamlit as st
st.set_page_config(page_title="World Food Explorer", layout="centered")

# Set page title
st.title("Smart Food Recommender")

# Add header
st.header("Choose a country and discover some delicious food!")

# Add text
st.write("This is a simple demonstration of Streamlit capabilities")


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
    ],
    "Italy": [
        {"name": "Pizza", "image": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Supreme_pizza.jpg"},
        {"name": "Pasta Carbonara", "image": "https://upload.wikimedia.org/wikipedia/commons/9/97/Spaghetti_alla_Carbonara.jpg"},
        {"name": "Tiramisu", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Tiramisu_-_Ristorante_Le_Cucine_del_Negresco.jpg"},
        {"name": "Lasagna", "image": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Lasagna_served.jpg"},
        {"name": "Risotto", "image": "https://upload.wikimedia.org/wikipedia/commons/d/d8/Risotto_ai_funghi_porcin.jpg"},
        {"name": "Gelato", "image": "https://upload.wikimedia.org/wikipedia/commons/f/f2/Gelato_Cart.jpg"}
    ],
    "Korea": [
        {"name": "Kimchi", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Kimchi_on_a_plate.jpg"},
        {"name": "Bibimbap", "image": "https://upload.wikimedia.org/wikipedia/commons/1/11/Dolsot-bibimbap.jpg"},
        {"name": "Tteokbokki", "image": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Tteokbokki_by_stu_spivack.jpg"},
        {"name": "Samgyeopsal", "image": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Samgyeopsal.jpg"},
        {"name": "Japchae", "image": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Japchae.jpg"},
        {"name": "Kimbap", "image": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Kimbap.jpg"}
    ],
    "Thailand": [
        {"name": "Pad Thai", "image": "https://upload.wikimedia.org/wikipedia/commons/3/30/Pad_Thai_kung_Chang_Khon.jpg"},
        {"name": "Green Curry", "image": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Green_curry_chicken.jpg"},
        {"name": "Tom Yum", "image": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Tom_yum_kung_1.jpg"},
        {"name": "Som Tum", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Som_Tam_Thai.jpg"},
        {"name": "Mango Sticky Rice", "image": "https://upload.wikimedia.org/wikipedia/commons/1/15/Mango_sticky_rice_-_Khao_Niao_Mamuang.jpg"},
        {"name": "Massaman Curry", "image": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Massaman_curry.jpg"}
    ],
    "India": [
        {"name": "Biryani", "image": "https://upload.wikimedia.org/wikipedia/commons/4/49/Biryani_India.jpg"},
        {"name": "Butter Chicken", "image": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Chicken_makhani.jpg"},
        {"name": "Samosa", "image": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Samosachutney.jpg"},
        {"name": "Masala Dosa", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Masala_dosa.jpg"},
        {"name": "Paneer Tikka", "image": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Paneer_Tikka.jpg"},
        {"name": "Chole Bhature", "image": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Chole_Bhature.jpg"}
    ],
    "China": [
        {"name": "Peking Duck", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Peking_Duck_-_Beijing.jpg"},
        {"name": "Xiao Long Bao", "image": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Xiao_Long_Bao.jpg"},
        {"name": "Mapo Tofu", "image": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Mapo_doufu.jpg"},
        {"name": "Hotpot", "image": "https://upload.wikimedia.org/wikipedia/commons/5/55/Chongqing_Hot_Pot.jpg"},
        {"name": "Dim Sum", "image": "https://upload.wikimedia.org/wikipedia/commons/d/df/Dim_sum_at_the_riverfront.jpg"},
        {"name": "Sweet and Sour Pork", "image": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Sweet_and_sour_pork.jpg"}
    ],
    "France": [
        {"name": "Croissant", "image": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Croissant-Petr_Kratochvil.jpg"},
        {"name": "Ratatouille", "image": "https://upload.wikimedia.org/wikipedia/commons/5/58/Confit_Byaldi.jpg"},
        {"name": "Quiche Lorraine", "image": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Quiche_Lorraine.jpg"},
        {"name": "Bouillabaisse", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Bouillabaisse_marseillaise.jpg"},
        {"name": "Crepes", "image": "https://upload.wikimedia.org/wikipedia/commons/6/67/Crepes_suzette_1.jpg"},
        {"name": "Macarons", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Macarons_in_Paris.jpg"}
    ],
    "Mexico": [
        {"name": "Tacos", "image": "https://upload.wikimedia.org/wikipedia/commons/8/85/Tacos_de_carnitas.jpg"},
        {"name": "Guacamole", "image": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Guacamole.jpg"},
        {"name": "Enchiladas", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Enchiladas_suizas.jpg"},
        {"name": "Tamales", "image": "https://upload.wikimedia.org/wikipedia/commons/b/be/Mexican_Tamale.jpg"},
        {"name": "Churros", "image": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Churros_in_Madrid.jpg"},
        {"name": "Pozole", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Pozole_rojo.jpg"}
    ],
    "USA": [
        {"name": "Burger", "image": "https://upload.wikimedia.org/wikipedia/commons/0/0b/RedDot_Burger.jpg"},
        {"name": "Fried Chicken", "image": "https://upload.wikimedia.org/wikipedia/commons/3/35/Fried_chicken_2.jpg"},
        {"name": "Hot Dog", "image": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Hotdog.jpg"},
        {"name": "Mac and Cheese", "image": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Macaroni_and_cheese.jpg"},
        {"name": "Buffalo Wings", "image": "https://upload.wikimedia.org/wikipedia/commons/8/8f/Buffalo_wings.jpg"},
        {"name": "Apple Pie", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Apple_pie.jpg"}
    ]
}


st.title("🍽️ World Food Recommendation Website")
st.write("Choose a country and explore its most iconic dishes!")

selected_country = st.selectbox("🌍 Select a country", sorted(food_data.keys()))

st.header(f"🍴 Popular Foods in {selected_country}")
for food in food_data[selected_country]:
    st.subheader(food["name"])
    st.image(food["image"], use_column_width=True)
    st.markdown("---")

import streamlit as st
import random

# Page settings
st.set_page_config(page_title="🍽️ Random Food Recommender", layout="centered")

st.title("🍲 What Should I Eat?")
st.write("Click the button to get a random food recommendation!")

# Default food list
if "food_list" not in st.session_state:
    st.session_state.food_list = [
        "Pizza", "Burger", "Sushi", "Nasi Lemak", "Ramen",
        "Fried Chicken", "Tacos", "Salad", "Pasta", "Steak"
    ]

# Show current food list
st.subheader("Available Foods:")
st.write(", ".join(st.session_state.food_list))

# Random Dish Button
if st.button("🎲 Get Random Dish"):
    chosen_food = random.choice(st.session_state.food_list)
    st.success(f"🍽️ You should eat: **{chosen_food}**!")

# Sidebar for adding custom foods
st.sidebar.header("➕ Add Your Own Food")
new_food = st.sidebar.text_input("Enter a food to add:")

if st.sidebar.button("Add Food"):
    if new_food.strip():
        st.session_state.food_list.append(new_food.strip())
        st.sidebar.success(f"Added: {new_food.strip()}")
    else:
        st.sidebar.error("Please enter a valid food name.")

# Page settings
st.set_page_config(page_title="🍽️ Food Recommender", layout="centered")

st.title("🍽️ Food Recommender Spin Wheel")
st.write("Click the button to spin the wheel and let fate decide your meal!")

# Default food choices
if "food_options" not in st.session_state:
    st.session_state.food_options = ["Pizza", "Burger", "Sushi", "Nasi Lemak", "Ramen", "Fried Chicken", "Tacos", "Salad", "Pasta", "Steak"]

# Create the spin wheel
def draw_wheel(options):
    fig = go.Figure(data=[go.Pie(
        labels=options,
        values=[1] * len(options),  # equal size
        hole=0.3,
        textinfo='label',
        marker=dict(colors=[
            "#FF9999", "#FFCC99", "#99FF99", "#66B3FF", "#C2C2F0",
            "#FFB3E6", "#FF6666", "#FFDB4D", "#D1B3FF", "#B2F0E6"
        ])
    )])
    fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0))
    return fig

# Show the wheel
st.plotly_chart(draw_wheel(st.session_state.food_options), use_container_width=True)

# Spin button
if st.button("🎡 Spin the Wheel"):
    choice = random.choice(st.session_state.food_options)
    st.success(f"🎉 You should eat: **{choice}**!")

# Sidebar to add more food options
st.sidebar.header("➕ Add Your Own Food")
new_food = st.sidebar.text_input("Add a food item:")

if st.sidebar.button("Add"):
    if new_food.strip():
        st.session_state.food_options.append(new_food.strip())
        st.sidebar.success(f"Added: {new_food.strip()}")
    else:
        st.sidebar.error("Please enter a food name.")