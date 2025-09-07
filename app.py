import streamlit as st
from streamlit.web.server.server import Server

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Smart Timetable Scheduler",
    page_icon="🗓️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- LOGOUT FUNCTION ---
def logout():
    st.session_state['logged_in'] = False
    st.info("Logged out successfully!")
    time.sleep(1)
    st.rerun()

# --- LOGIN FUNCTIONALITY ---
# Streamlit reruns the script on every interaction. We use session_state to keep track of the login status.
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def check_login(username, password):
    """For the demo, any username/password will work."""
    if username and password:
        st.session_state['logged_in'] = True
        # When login is successful, we need to rerun the script to hide the login form
        # and show the "Logged in successfully" message.
        st.rerun()
    else:
        st.error("Please enter both username and password.")

# --- UI DISPLAY ---
if not st.session_state['logged_in']:
    # --- LOGIN FORM ---
    st.title("🗓️ Smart Timetable Scheduler")
    st.subheader("Admin Login")

    with st.form("login_form"):
        username = st.text_input("Username", placeholder="e.g., admin")
        password = st.text_input("Password", type="password", placeholder="• • • • • • • •")
        submitted = st.form_submit_button("Login")

        if submitted:
            check_login(username, password)

else:
    # --- LOGGED IN VIEW ---
    st.sidebar.success("Logged in successfully!")
    st.title("Welcome to the Admin Panel!")
    st.write("Please use the sidebar to navigate to the dashboard and other pages.")
    st.info("This is the main page. All other functionalities are in the sidebar navigation.")

    # --- ADD LOGOUT BUTTON TO SIDEBAR ---
    st.sidebar.button("Logout", on_click=logout)
