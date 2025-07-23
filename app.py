import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="A Gift For You",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- CUSTOM STYLING & FONT IMPORT (DARK THEME) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400..700;1,400..700&family=Montserrat:wght@400;700&display=swap');
    
    /* Set background for the main app area */
    [data-testid="stAppViewContainer"] {
        background-color: #121212; /* Very dark grey, almost black */
    }

    html, body, [class*="st-"], h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat', sans-serif;
        color: #e0e0e0; /* Light grey for high contrast on dark background */
    }

    /* Main content block styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        padding-top: 3rem;
        background-color: #1e1e1e; /* Slightly lighter dark grey for sidebar */
    }

    /* Poem container styling */
    .poem-container {
        background-color: #2a2a2a; /* Dark container background */
        border-radius: 15px;
        padding: 2rem 3rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        border-left: 8px solid #03dac6; /* A vibrant teal accent */
    }
    
    /* Poem text styling */
    .poem-text {
        font-family: 'Lora', serif;
        font-size: 1.2rem;
        line-height: 1.9;
        text-align: left;
        white-space: pre-wrap;
        margin-bottom: 2rem;
        color: #f5f5f5; /* Off-white for poem text */
    }

    /* Author name styling */
    .author-name {
        font-family: 'Montserrat', sans-serif;
        font-style: italic;
        text-align: right;
        font-size: 1.1rem;
        color: #a0a0a0; /* Softer grey for the author */
    }

    /* Personal note styling */
    .personal-note {
        font-family: 'Lora', serif;
        font-size: 1.15rem;
        line-height: 1.8;
        background-color: rgba(3, 218, 198, 0.1); /* Faded teal background */
        border-left: 5px solid #03dac6;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        color: #e0e0e0;
    }
    
    /* FIX: Make selected icon visible against background */
    .nav-link-selected svg {
        color: #121212 !important;
    }

</style>
""", unsafe_allow_html=True)


# --- POEM & POET DATA (UPDATED) ---
poems = {
    "For My Sussy Guy 😎": {
        "author": "Aniket",
        "text": """

We met through chance — a random match,<br>
Just strangers once in a CODM patch.<br>
Who knew from bullets and bouncing grenades,<br>
A bond would bloom in shifting shades?<br><br>

From Discord chaos to Insta spam,<br>
You showed up loud like a meme with glam.<br>
Your gameplay’s cracked, your aim’s unfair,<br>
But it's your wild soul that keeps me there.<br><br>

You call me Diddy — not soft, but sly,<br>
With that sussy smirk and a devilish eye.<br>
Like you know it drives me mad each time,<br>
Yet you drop it again with that smug lil’ rhyme 😤😆<br><br>

You carry weights you never show,<br>
Behind the memes, there’s more below.<br>
But still you vibe, still bring that light,<br>
Still crash my DMs at 2AM night.<br><br>

My little chaos — sweet menace you are,<br>
A storm in lobbies, my favorite star.<br>
So here’s a poem, no cap, no lie,<br>
For Samu — my gremlin, my sussy guy 😎💛
"""
    }
}

# --- LOGIN FUNCTION ---
def login_page():
    """Displays the login page and handles authentication."""
    st.title("A Private Gift 💌")
    st.write("Please enter the details I shared with you to unlock the note.")

    with st.form("login_form"):
        name = st.text_input("Your Name")
        nickname = st.text_input("Your Nickname given by me", type="password")
        submitted = st.form_submit_button("Unlock")

        if submitted:
            # Check credentials (case-insensitive)
            if name.strip().lower() == "samrat" and nickname.strip().lower() == "samu":
                st.session_state.authenticated = True
                st.rerun() # Rerun the app to show the main content
            else:
                st.error("Hmm, that's not quite right. Please try again!")


# --- MAIN APP FUNCTION ---
def main_app():
    """The main application logic after successful authentication."""
    # --- SIDEBAR NAVIGATION ---
    with st.sidebar:
        # st.image("https://i.imgur.com/r6yTtoQ.png", use_container_width=True)
        st.title("A Gift of Words")
        
        menu_options = ["A Note for You"] + list(poems.keys())
        
        selected = option_menu(
            menu_title=None,
            options=menu_options,
            icons=["pencil-square", "book-heart"], # Changed icon for the poem
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#1e1e1e"},
                "icon": {"color": "#03dac6", "font-size": "20px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin":"0px",
                    "--hover-color": "#3a3a3a",
                    "color": "#e0e0e0" 
                },
                "nav-link-selected": {"background-color": "#03dac6", "color": "#121212"},
            }
        )

    # --- MAIN PAGE CONTENT ---
    if selected == "A Note for You":
        st.title("A Note for You, My Friend")
        st.write("")
        st.markdown("""
        <p class="personal-note">
        Hey Samu,<br><br>
        I wanted to share this particular poem with you. It's one that means a lot to me, and I thought you might appreciate it too.<br><br>
        Consider it a small way of saying thank you for being such an amazing person in my life. I hope you find a moment of joy and inspiration in its lines.<br><br>
        With love,<br>
        Aniket
        </p>
        """, unsafe_allow_html=True)

    elif selected in poems:
        poem = poems[selected]
        
        st.markdown(f"""
        <div class="poem-container">
            <h1 style="text-align: center; font-family: 'Montserrat', sans-serif; color: #f5f5f5;">{selected}</h1>
            <p class="poem-text">{poem["text"]}</p>
            <p class="author-name">— {poem["author"]}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # "About the Poet" section is removed as it's not needed for a personal poem.


# --- SCRIPT EXECUTION ---
if __name__ == "__main__":
    # Initialize session state for authentication if it doesn't exist
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    # Conditionally display the login page or the main app
    if st.session_state.authenticated:
        main_app()
    else:
        login_page()
