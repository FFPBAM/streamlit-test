import streamlit as st

# Secrets laden (Benutzername und Passwörter)
USERS = st.secrets["passwords"]

# Session State initialisieren
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# Login-Funktion
def check_password():
    username = st.session_state.get("username_input", "")
    password = st.session_state.get("password_input", "")
    
    if username in USERS and USERS[username] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        return True
    return False

# Login-Interface
if not st.session_state.logged_in:
    st.title("🔐 Login")
    st.write("Bitte melde dich an, um fortzufahren.")
    
    st.text_input("Benutzername", key="username_input")
    st.text_input("Passwort", type="password", key="password_input")
    
    if st.button("Einloggen"):
        if check_password():
            st.success("Erfolgreich eingeloggt!")
            st.rerun()
        else:
            st.error("❌ Falscher Benutzername oder Passwort")
else:
    # Die eigentliche App nach dem Login
    st.title(f"👋 Willkommen, {st.session_state.username}!")
    
    # Hello World Ausgabe
    st.write("# Hello World! 🌍")
    st.write("Dies ist deine geschützte Streamlit-App.")
    
    # Logout-Button
    st.divider()
    if st.button("Ausloggen"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
