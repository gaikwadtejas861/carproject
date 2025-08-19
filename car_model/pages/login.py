import streamlit as st

st.set_page_config(page_title="Login System", page_icon="🔑", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
    .stApp {
        background: linear-gradient(135deg, #e0eafc, #cfdef3);
        font-family: 'Poppins', sans-serif;
        padding-top: 10px;
    }
    h1 {
        color: #243B55 !important;
        font-weight: 900 !important;
        text-align: center !important;
        margin-bottom: 36px !important;
        letter-spacing: 2px;
        user-select: none;
        text-shadow: 0 2px 18px #fff8;
    }
    label, .stTextInput label, .stTextInput input, .stPasswordInput label, .stPasswordInput input, .stSelectbox label, .stForm label {
        color: #222 !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        letter-spacing: 1px;
        user-select: none;
        text-shadow: 0 0 8px #fff6;
    }
    input[type="text"], input[type="password"] {
        color: #252525 !important;
        font-weight: 700 !important;
        background-color: #f7fbff !important;
        border: 2px solid #243B55 !important;
        font-size: 1.08rem !important;
    }
    .stForm {
        background: #fff !important;
        border-radius: 18px !important;
        box-shadow: 0 14px 30px rgba(36,59,85,0.15) !important;
        padding: 40px 50px !important;
        margin-bottom: 30px !important;
    }
    div.stButton > button {
        background: #243B55;
        color: #fff !important;
        font-weight: 900 !important;
        font-size: 1.18rem !important;
        border-radius: 30px !important;
        box-shadow: 0 8px 16px rgba(36,59,85,0.25);
        border: none !important;
        width: 100% !important;
        margin-top: 16px !important;
    }
    div.stButton > button:hover {
        background: #486d9f !important;
        transform: scale(1.04);
    }
    .stInfo {
        color: #243B55 !important;
        font-weight: 700 !important;
        background-color: #dbeafe !important;
        border-left: 6px solid #3b82f6 !important;
        border-radius: 10px !important;
        box-shadow: 0 6px 12px rgba(59,130,246,0.13);
        font-size: 1.08rem !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🔐 Login System with Profile Page</h1>", unsafe_allow_html=True)

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.is_admin = False
    st.session_state.username = ""

def login(username, password):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        st.session_state.logged_in = True
        st.session_state.is_admin = True
        st.session_state.username = username
        return "Welcome Admin!"
    elif username and password:
        st.session_state.logged_in = True
        st.session_state.is_admin = False
        st.session_state.username = username
        return f"Welcome {username}!"
    else:
        return "Please enter valid credentials."

if not st.session_state.logged_in:
    st.subheader("Login to Continue")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            message = login(username, password)
            st.info(message)
