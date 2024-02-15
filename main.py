import streamlit as st
import hmtai

def generate_image(category):
    if category in sfw_categories:
        return hmtai.get("hmtai", category)
    elif category in nsfw_categories:
        return hmtai.get("hmtai", category)
    else:
        return "Invalid category"

# SFW and NSFW categories
sfw_categories = ["bite", "boop", "coffee_arts", "cry", "cuddle", "dance", "depression", "feed",
                  "hug", "jahy_arts", "kill", "kiss", "lick", "like", "nosebleed",
                  "neko_arts", "pat", "poke", "punch", "sleep", "slap", "tea", "threaten", "tickle",
                  "wave"]
nsfw_categories = ["anal", "ass", "bdsm", "cum", "classic", "creampie", "manga", "femdom", "hentai",
                   "incest", "masturbation", "public", "ero", "orgy", "elves", "yuri", "pantsu", 
                   "glasses", "cuckold", "blowjob", "boobjob", "footjob", "handjob", "boobs", "thighs", 
                   "pussy", "ahegao", "uniform", "gangbang", "tentacles", "gif", "nsfwNeko", 
                   "nsfwMobileWallpaper", "zettaiRyouiki"]

# Streamlit app
st.title("Welcome to Hanimator")

# Category selection
category_type = st.radio("Select category type:", ("SFW", "NSFW"))
if category_type == "SFW":
    category = st.selectbox("Select a SFW category:", sfw_categories)
elif category_type == "NSFW":
    category = st.selectbox("Select a NSFW category:", nsfw_categories)

# Generate and display image
if st.button("Generate Image"):
    image_url = generate_image(category)
    if image_url:
        with st.spinner("Generating Image..."):
            st.image(image_url, caption=f"Generated Image for {category}", use_column_width=True)
    else:
        st.warning("Invalid category selected.")

# Footer section positioned to the right bottom
st.markdown("<div style='position: absolute; right: 10px; bottom: 10px;'>Creator: Prasanna Kotyal</div>", unsafe_allow_html=True)

# Run the app
