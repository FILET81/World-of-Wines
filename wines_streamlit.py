import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 

st.set_page_config(page_title="World of Wines", page_icon=":wine_glass:", layout="wide")
                   
st.title("***World of Wines*** :wine_glass:")

with st.sidebar:
    selection=st.radio("Menu:", ["Introduction","Vizzes", "Wine Searcher", "Price Predictor", "Bibliography"])

if selection=="Introduction":     # Providing some info about the world of wines
    st.header("Let's first get some interesting info about this amazing world! :confetti_ball:")    
    st.image("Images\Vineyards-1.jpg", caption="Vineyards somewhere in the World", width=950)   
    st.subheader("Did you know that?:")
    st.markdown("- Wine production dates back to at least **6000 BC** in **Georgia**, **5000 BC** in **Iran** or **4100 BC** in **Armenia**.")
    st.markdown("- Ancient civilizations like the **Egyptians**, **Greeks** and **Romans** further developed **winemaking techniques**.")
    st.markdown("- Grapevines can be seeded in **different types of soils** such as ***Limestone***, ***Clay***, ***Volcanic***, ***Granite***, ***Slate***, ***Sand*** or ***Gravel***.")
    st.markdown("- In general, all wines go through **2 types of fermentations** minimum -> ***Alcoholic*** and ***Malolactic***.")
    st.markdown("- The **ABV** -*Alcohol by Volume*- of **regular wine** goes from **5%** to **16%**.")
    st.markdown("- There are currently over **10.000 different wine grape -*Vitis Vinifera*- varieties** worldwide.")
    st.markdown("- Best grape's **growing regions** for wine production are placed in **latitudes** between **30°** and **50°** of both hemispheres.")
    st.image("Images\Best Regions for Grape Growing.jpg", caption="The Wine Belt", width=650)

elif selection=="Vizzes":     # Embedding "Tableau Public" vizzes
    st.header("Let's play a bit with the data! :grapes:")

elif selection=="Wine Searcher":     # Displaying the wine Searcher out of the treated DataFrame
    st.header("Let's look for a tasty wine! :face_with_monocle:")

    st.button("Find")

elif selection=="Price Predictor":     # Displaying a Machine Learning model
    st.header("Let's try to predict some prices! :gear:")

    st.button("Guess")

else:     # Closing the Presentation
    st.subheader("Main Data Sources:")
    st.markdown("https://mavenanalytics.io/")
    st.markdown("https://winefolly.com/")
    st.markdown("https://www.wikipedia.org/")
    st.markdown("https://www.oiv.int/")
    st.markdown("https://www.oecd.org/")
    st.markdown("And many others...")
    st.subheader("Thanks for listening!!!")
    st.image("Images\Vineyards-7.jpg", caption="Vineyards somewhere in the World", width=950)