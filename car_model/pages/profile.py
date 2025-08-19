import streamlit as st

# Initialize session state variables before use
if 'username' not in st.session_state:
    st.session_state.username = ''
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# CSS for professional styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

        .stApp {
            background: linear-gradient(135deg, #e0eafc, #cfdef3);
            font-family: 'Poppins', sans-serif;
            color: #222;
            padding: 40px 0;
        }

        .profile-card {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 30px 40px;
            border-radius: 20px;
            box-shadow: 0 12px 30px rgba(36,59,85,0.15);
            user-select: none;
        }

        .profile-header {
            font-size: 2.5rem;
            font-weight: 800;
            color: #243B55;
            text-align: center;
            margin-bottom: 25px;
            letter-spacing: 1.5px;
            user-select: none;
        }

        .profile-text {
            font-weight: 600;
            font-size: 1.1rem;
            color: #444;
            margin-bottom: 12px;
        }

        .profile-label {
            font-weight: 700;
            color: #243B55;
            margin-right: 6px;
        }

        hr {
            border: none;
            border-top: 1px solid #ddd;
            margin: 20px 0;
        }

        /* Logout button styling */
        div.stButton > button {
            background: #243B55;
            color: white;
            font-weight: 700;
            padding: 14px 36px;
            font-size: 1.1rem;
            border-radius: 30px;
            border: none;
            transition: background-color 0.3s ease, transform 0.2s ease;
            cursor: pointer;
            display: block;
            margin: 30px auto 0 auto;
            box-shadow: 0 6px 12px rgba(36, 59, 85, 0.4);
            user-select: none;
        }
        div.stButton > button:hover {
            background: #486d9f;
            transform: translateY(-3px);
        }
        div.stButton > button:active {
            transform: translateY(-1px);
        }
    </style>
""", unsafe_allow_html=True)

def profile_page():
    st.markdown('<div class="profile-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="profile-header">👤 Profile Page</h2>', unsafe_allow_html=True)

    st.markdown(f'<p class="profile-text"><span class="profile-label">Username:</span> {st.session_state.username or "N/A"}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="profile-text"><span class="profile-label">Role:</span> {"Admin" if st.session_state.is_admin else "User"}</p>', unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown('<p class="profile-text">📅 <span class="profile-label">Member Since:</span> 2025</p>', unsafe_allow_html=True)
    st.markdown('<p class="profile-text">📍 <span class="profile-label">Location:</span> Earth 🌍</p>', unsafe_allow_html=True)
    st.markdown('<p class="profile-text">📧 <span class="profile-label">Email:</span> example@example.com</p>', unsafe_allow_html=True)

    if st.button("Logout 🚪"):
        st.session_state.logged_in = False
        st.session_state.is_admin = False
        st.session_state.username = ""
        st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

st.write("My Profile:")
profile_page()
