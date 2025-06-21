import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# --- Custom Page Styling ---
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1581093588401-9e8f01d2e37d");
    background-size: cover;
    background-position: center;
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Load user credentials from YAML or define inline ---
with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status is False:
    st.error("❌ Incorrect username or password.")

if authentication_status is None:
    st.warning("Please enter your credentials.")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome, {name} 👋")

    # Replace this with your actual app
    st.title("🔐 SmartShield Dashboard")
    st.write("Welcome to the Intrusion Detection System powered by AI.")
    import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

config = yaml.load("""
credentials:
  usernames:
    admin_user:
      name: Admin
      password: '$2b$12$KIXfQXq2Ihz2fTfQzya4VOGUErFei/mZ4eZPKP6zTyMuFkeVO/Sm6'
      email: admin@example.com
    analyst_user:
      name: Analyst
      password: '$2b$12$Wb5P6xP.HHRR2j5CrKyt7OFNHiOwFX7Ljkmu.y3yU2LuJpxdHITbK'
      email: analyst@example.com

cookie:
  name: smartshield_cookie
  key: some_signature_key
  expiry_days: 3

preauthorized:
  emails:
    - admin@example.com
    - analyst@example.com
""", Loader=SafeLoader)


