import pandas as pd
import pickle as pk
import streamlit as st

# Load your saved model
model = pk.load(open('model.pkl', 'rb'))

# CSS styles for professional UI with bright font
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #e0eafc, #cfdef3);
        font-family: 'Poppins', sans-serif;
        color: #FFF !important;       /* Bright white main text */
        padding-bottom: 40px;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #141E30, #243B55);
        color: #FFD700 !important;    /* Gold text in sidebar */
        font-weight: 600;
    }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] span {
        color: #FFD700 !important;
        text-shadow: 0 0 6px rgba(255,215,0,0.7);
    }

    /* Sidebar Logo styling */
    .sidebar .sidebar-content img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 15px;
        width: 75px;
        border-radius: 15px;
    }

    /* Main title */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: #FFF !important;       /* Bright white */
        text-align: center;
        margin-bottom: 0;
        letter-spacing: 2px;
        user-select: none;
        text-shadow: 0 0 10px #243B55;
    }

    /* Subtitle */
    .sub-title {
        font-size: 1.25rem;
        font-weight: 400;
        color: #FFD700 !important;    /* Gold subtitle */
        text-align: center;
        margin-top: 0;
        margin-bottom: 40px;
        user-select: none;
        text-shadow: 0 0 6px #243B55;
    }

    /* Input container */
    .input-card {
        background: white;
        border-radius: 20px;
        box-shadow: 0 14px 30px rgba(36, 59, 85, 0.15);
        padding: 30px 40px;
        max-width: 900px;
        margin: auto;
        margin-bottom: 45px;
        color: #243B55 !important;
    }

    /* Label styling */
    label[data-baseweb="select"] > div > div > div > div > div > div > div span {
        font-weight: 600 !important;
        color: #243B55 !important;
    }
    /* Slider label */
    .stSlider > label, .stSelectbox > label {
        font-weight: 600 !important;
        color: #243B55 !important;
        user-select: none;
    }
    /* Text inside selects and sliders */
    div[data-baseweb="select"] span, div[data-baseweb="slider"] span {
        color: #444 !important;
        font-weight: 500 !important;
    }

    /* Use columns nicely spaced */
    .stColumn {
        padding-left: 15px !important;
        padding-right: 15px !important;
    }

    /* Button styling */
    div.stButton > button {
        background: #243B55;
        color: #FFD700; /* Gold text on button */
        font-weight: 700;
        padding: 14px 30px;
        font-size: 1.1rem;
        border-radius: 30px;
        border: none;
        transition: background-color 0.3s ease, transform 0.2s ease;
        width: 100%;
        user-select: none;
        cursor: pointer;
        margin-top: 15px;
        box-shadow: 0 6px 12px rgba(36, 59, 85, 0.4);
    }
    div.stButton > button:hover {
        background: #486d9f;
        color: #fff;
        transform: translateY(-3px);
    }
    div.stButton > button:active {
        transform: translateY(-1px);
    }

    /* Result box */
    .result-container {
        max-width: 650px;
        background: #f0f4ff;
        border-radius: 25px;
        box-shadow: 0 0 25px rgba(36,59,85,0.25);
        padding: 30px;
        margin: auto;
        text-align: center;
        user-select: none;
        color: #243B55;
        font-weight: 700;
        font-size: 1.75rem;
        margin-bottom: 50px;
    }
    .price-highlight {
        color: #ff4b2b;
        font-weight: 900;
        font-size: 2.25rem;
        text-shadow: 0 0 10px #ff6c50;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Inject custom CSS for logo container remains unchanged
st.markdown("""
    <style>
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 40px;
        margin-bottom: 40px;
    }
    .logo-img {
        width: 350px;   /* Adjust width as needed */
        border-radius: 20px;
        box-shadow: 0 4px 18px rgba(0,0,0,0.2);
        border: 3px solid #AD8A4B;
        background: #fff;
        padding: 15px;
    }
    </style>
    """, unsafe_allow_html=True)


# Sidebar Content
st.sidebar.image("logo.jpg", width=75)
st.sidebar.title("Car Predictor Pro")
st.sidebar.markdown("### Predict car prices instantly with AI")


# Page Title
st.markdown('<h1 class="main-title">Tech Fusion Car Predictors</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Welcome to the future of car prediction!</p>', unsafe_allow_html=True)


# Load data
df = pd.read_csv(r"C:\\Users\\Tejas Gaikwad\\Downloads\\cardekho.csv")

def extract_brand(name):
    return name.split(" ")[0].strip()
df["brand"] = df["name"].apply(extract_brand)


# Input Card Container
st.markdown('<div class="input-card">', unsafe_allow_html=True)

left_col, right_col = st.columns(2)

with left_col:
    brand = st.selectbox("🚗 Select Car Brand", df["brand"].unique())
    models_available = df[df["brand"] == brand]["name"].unique()
    car_model = st.selectbox("📌 Select Car Model", models_available)
    year = st.slider("📅 Manufactured Year", 1994, 2025, 2015)
    km_driven = st.slider("🛣 Kilometers Driven", 0, 200000, 50000)
    fuel = st.selectbox("⛽ Fuel Type", df["fuel"].unique())
    seller_type = st.selectbox("👤 Seller Type", df["seller_type"].unique())

with right_col:
    transmission = st.selectbox("⚙ Transmission", df["transmission"].unique())
    owner = st.selectbox("👨‍🔧 Owner Type", df["owner"].unique())
    mileage = st.slider("⚡ Mileage (km/l)", 10, 40, 18)
    engine = st.slider("🔧 Engine CC", 700, 5000, 1500)
    max_power = st.slider("💥 Max Power", 0, 200, 75)
    seats = st.slider("💺 Seat Count", 2, 10, 5)

st.markdown("</div>", unsafe_allow_html=True)


if st.button("🚀 Predict Car Price"):
    x_test = pd.DataFrame(
        [[car_model, brand, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
        columns=["name", "brand", "year", "km_driven", "fuel", "seller_type", "transmission", "owner", "mileage", "engine", "max_power", "seats"],
    )

    # Encoding categorical variables
    x_test["owner"].replace(
        ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"], [1, 2, 3, 4, 5], inplace=True
    )
    x_test["fuel"].replace(["Diesel", "Petrol", "LPG", "CNG"], [1, 2, 3, 4], inplace=True)
    x_test["seller_type"].replace(["Individual", "Dealer", "Trustmark Dealer"], [1, 2, 3], inplace=True)
    x_test["transmission"].replace(["Manual", "Automatic"], [1, 2], inplace=True)
    
    x_test["brand"] = x_test["brand"].replace(
        [
            "Maruti", "Skoda", "Honda", "Hyundai", "Toyota", "Ford", "Renault", "Mahindra",
            "Tata", "Chevrolet", "Datsun", "Jeep", "Mercedes-Benz", "Mitsubishi", "Audi",
            "Volkswagen", "BMW", "Nissan", "Lexus", "Jaguar", "Land", "MG", "Volvo", "Daewoo",
            "Kia", "Fiat", "Force", "Ambassador", "Ashok", "Isuzu", "Opel",
        ],
        list(range(1, 32)),
    )
    x_test = x_test.rename(columns={"mileage": "mileage(km/ltr/kg)"})

    car_price = model.predict(x_test.drop("name", axis=1))

    st.markdown(
        f'<div class="result-container">💰 Predicted Car Price: <span class="price-highlight">₹ {car_price[0]:,.2f}</span></div>',
        unsafe_allow_html=True,
    )
    st.balloons()
