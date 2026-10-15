import streamlit as st

# Initialize session state for user session tracking
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "users_db" not in st.session_state:
    # Dummy user database (Username: Password)
    st.session_state["users_db"] = {"admin": "admin123", "bhargav": "retailpulse2026"}

def show_auth_page():
    st.title("🔐 RetailPulse - Authentication")
    
    tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
    
    with tab1:
        st.subheader("Sign In")
        username = st.text_input("Username", key="signin_user")
        password = st.text_input("Password", type="password", key="signin_pass")
        if st.button("Sign In"):
            users = st.session_state["users_db"]
            if username in users and users[username] == password:
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.success(f"Welcome back, {username}!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

    with tab2:
        st.subheader("Create an Account")
        new_user = st.text_input("New Username", key="signup_user")
        new_pass = st.text_input("New Password", type="password", key="signup_pass")
        confirm_pass = st.text_input("Confirm Password", type="password", key="confirm_pass")
        if st.button("Sign Up"):
            if new_user in st.session_state["users_db"]:
                st.warning("Username already exists.")
            elif new_pass != confirm_pass:
                st.error("Passwords do not match.")
            elif new_user and new_pass:
                st.session_state["users_db"][new_user] = new_pass
                st.success("Account created successfully! Please Sign In.")
            else:
                st.error("Please fill in all fields.")

# Authentication Gatekeeper
if not st.session_state["authenticated"]:
    show_auth_page()
else:
    # Sidebar Logout Button
    st.sidebar.write(f"Logged in as: **{st.session_state['username']}**")
    if st.sidebar.button("Log Out"):
        st.session_state["authenticated"] = False
        st.rerun()
        
    # --- YOUR EXISTING DASHBOARD CODE GOES HERE ---
    st.title("📊 RetailPulse Analytics Dashboard")
    # (Rest of your tabs, charts, and metrics...)