import pickle
import streamlit as st
import pandas as pd
import numpy as np

# Load model safely with error handling
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    st.sidebar.success(f"✅ Model loaded: {type(model)}")
except Exception as e:
    st.error(f"❌ Model loading failed: {e}")
    st.stop()

# Load dataset
df = pd.read_csv(r"C:\\Users\\Tejas Gaikwad\\Downloads\\cardekho.csv")

# Create 'brand' column from 'name' (full car model name)
df['brand'] = df['name'].apply(lambda x: x.split(' ')[0].strip())

# Inject CSS for styling
st.markdown("""
    <style>
        body, .stApp {background: linear-gradient(135deg,#141e30 0%,#243b55 100%);}
        .hero {
            margin: 2em auto; padding: 2em 4em; border-radius: 25px;
            background: rgba(255,255,255,0.18); backdrop-filter: blur(12px);
            box-shadow: 0 8px 32px 0 rgba(31,38,135,0.23);
            border: 1px solid rgba(255,255,255,0.25); text-align: center;
        }
        .hero h1 {
            font-family: 'Orbitron', sans-serif; font-size: 2.8em;
            color: #ffdd40; letter-spacing: 2px; text-shadow: 0 1px 20px #1ed760;
        }
        .hero p {font-size: 1.2em; color: #eaeaea;}
        .glass-card {
            background: rgba(40,80,140,0.14); border-radius: 19px; margin: 1em 0;
            padding: 1.5em 2.5em; box-shadow: 0 1.5em 3em #1ed76021; border: 1.5px solid #60f5c0;
        }
        .stButton>button {
            background: linear-gradient(90deg,#fe5f75 0%,#fc9842 100%);
            color: #fff; font-weight:700; border-radius: 23px; border: none;
            font-size: 1.3em; padding: 16px 34px; margin-top: 1em;
            box-shadow: 0 3px 8px #fe5f7544; transition: 0.24s;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg,#43e97b 0%,#38f9d7 99%);
            color: #111; transform: scale(1.05);
        }
        .prediction-result {
            font-size: 2em; font-family: 'Orbitron', sans-serif; text-align: center;
            color: #FEF768; margin-top: 2em; padding: 24px; background: rgba(255,255,255,.15);
            border-radius: 22px; box-shadow: 0 0 18px #20ffc5; letter-spacing:1px;
            animation: glow 1.7s infinite alternate;
        }
        @keyframes glow {
            from {box-shadow: 0 0 12px #20ffc5;}
            to {box-shadow: 0 0 36px #43e97b;}
        }
        .sidebar-stats {
            font-size: 1.1em; color: #ffdd40; padding: 0.8em; border-radius: 11px;
            background: rgba(31,38,85,0.33); margin-top: 1.2em;
        }
        .trend-title {
            font-family:'Orbitron',sans-serif; color:#43e97b; font-size:1.3em; text-align:center;
            margin-top:30px; text-shadow:0 2px 9px #20ffc5;
        }
        hr { border: 1px solid #1ed760; }
        .models-header {
            font-family: 'Orbitron', sans-serif; font-size: 2.1em; background: linear-gradient(90deg,#38f9d7,#43e97b);
            color: #243b55; text-align: center; padding: 10px 0 15px 0; letter-spacing: 1px;
            border-radius: 17px; box-shadow: 0 7px 28px #1ed76044; margin-bottom: 20px;
        }
        .brand-card {
            background: rgba(255,255,255,0.12); border-radius: 16px;
            box-shadow: 0 3px 19px #38f9d771; margin: 11px 0;
            padding: 14px 24px 7px 24px; border: 1.5px solid #38f9d7;
            transition: box-shadow 0.22s;
        }
        .brand-card:hover {box-shadow: 0 7px 34px #43e97b88;}
        .model-list {max-height: 140px; overflow-y: auto; padding-left: 8px;}
        .brand-title {
            font-size: 1.25em; font-weight: bold; color: #38f9d7;
            font-family:'Orbitron',sans-serif; margin-bottom:10px; letter-spacing:1px;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class='hero'>
        <h1>🚗 Futuristic Car Price Predictor</h1>
        <p>Unveiling market trends in style. AI-powered, superfast, and visually stunning!</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar Stats
st.sidebar.markdown("<div class='sidebar-stats'>", unsafe_allow_html=True)
st.sidebar.write(f"📊 Models in database: {len(df)}")
st.sidebar.write(f"🔢 Unique car brands: {len(df['brand'].unique())}")
if 'selling_price' in df.columns:
    st.sidebar.write(f"🌟 Max price: ₹ {df['selling_price'].max():,.0f}")
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Car Models by Brand Section
brand_models = df.groupby('brand')['name'].unique()
sorted_brands = sorted(brand_models.keys())
st.markdown("<div class='models-header'>🏆 Car Models by Brand</div>", unsafe_allow_html=True)

for brand in sorted_brands:
    models = sorted(list(set(brand_models[brand])))
    with st.expander(f"🚗 {brand}", expanded=False):
        st.markdown(f"<div class='brand-card'>", unsafe_allow_html=True)
        st.markdown(f"<div class='brand-title'>{brand} ({len(models)} models)</div>", unsafe_allow_html=True)
        st.markdown("<div class='model-list'>", unsafe_allow_html=True)
        for model in models:
            st.markdown(f"🟢 <span style='color:#FEF768;font-family:monospace'>{model}</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Input section: Brand and Model selection plus car specs
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    selected_brand = st.selectbox('🔥 Car Brand', df['brand'].unique())
    year = st.slider('🎂 Year of Manufacture', 1994, 2025)
    km_driven = st.slider('🏁 Kilometers Driven', 0, 210000, step=500)
    st.markdown("</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    models_for_selected_brand = sorted(list(set(df[df['brand'] == selected_brand]['name'])))
    model_name = st.selectbox('🚗 Model Name', models_for_selected_brand)
    fuel = st.selectbox('⛽ Fuel Type', df['fuel'].unique())
    transmission = st.selectbox('⚙ Gearbox', df['transmission'].unique())
    seller_type = st.selectbox('🤝 Seller Type', df['seller_type'].unique())
    owner = st.selectbox('👤 Owner Type', df['owner'].unique())
    st.markdown("</div>", unsafe_allow_html=True)

col3, col4, col5 = st.columns([1, 1, 1])
with col3:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    mileage = st.slider('🛢 Mileage', 10, 40)
    st.markdown("</div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    engine = st.slider('🔧 Engine CC', 700, 5000, step=50)
    st.markdown("</div>", unsafe_allow_html=True)
with col5:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    max_power = st.slider('💡 Max Power', 0, 500)
    seats = st.slider('💺 Seats', 2, 10)
    st.markdown("</div>", unsafe_allow_html=True)

# Prediction button and logic
if st.button("✨ Predict Futuristic Price"):
    x_test = pd.DataFrame(
        [[model_name, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
        columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats']
    )

    x_test["owner"].replace(['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'], [1, 2, 3, 4, 5], inplace=True)
    x_test["fuel"].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)
    x_test["seller_type"].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1, 2, 3], inplace=True)
    x_test["transmission"].replace(['Manual', 'Automatic'], [1, 2], inplace=True)

    car_model_list = [
        'Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault', 'Mahindra',
        'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz', 'Mitsubishi', 'Audi',
        'Volkswagen', 'BMW', 'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo',
        'Kia', 'Fiat', 'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel'
    ]
    model_brand = model_name.split()[0]
    if model_brand in car_model_list:
        x_test['name'] = x_test['name'].replace(car_model_list, list(range(1, 32)))
    if "mileage" in x_test.columns:
        x_test = x_test.rename(columns={"mileage": "mileage(km/ltr/kg)"})

    try:
        car_price = model.predict(x_test)
        st.markdown(f"<div class='prediction-result'>🚀 Car Predicted Price: ₹ {car_price[0]:,.0f}</div>", unsafe_allow_html=True)
        st.balloons()
    except Exception as e:
        st.error(f"Prediction Error: {e}")

# Brand-wise price trend chart
st.markdown("<div class='trend-title'>📈 Brand-wise Price Trend</div>", unsafe_allow_html=True)
sel_brands = st.multiselect('Choose brands for price trend:', options=df['brand'].unique(), default=df['brand'].unique().tolist())
if sel_brands and 'selling_price' in df.columns:
    import altair as alt
    filtered = df[df['brand'].isin(sel_brands)]
    trend_chart = alt.Chart(filtered).mark_line(point=True).encode(
        x='year', y='selling_price', color='brand'
    ).properties(
        width=650, height=350, title="⚡ Average Price by Year"
    )
    st.altair_chart(trend_chart, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.info("Tip: Experiment with multiple brands and years for instant market insights!", icon="🎨")
