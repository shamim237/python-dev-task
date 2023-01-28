import streamlit as st
from multiapp import MultiApp
from apps import paraphraseApp, summarizerApp, scraperrApp

app = MultiApp()

st.title("Python Dev Task @SkyRanko")
st.write("==================_Completed by_ **Shamim Mahbub**==================")
st.markdown("This app provides three services - :red[Scraping], :orange[Paraphrasing] and :blue[Summarizing]")
# Enter this link- https://www.amazon.com/dp/B09B9TB61G!

# Add all your application here
app.add_app("Scraper", scraperrApp.app)
app.add_app("Paraphraser", paraphraseApp.app)
app.add_app("Summarizer", summarizerApp.app)
# The main app
app.run()