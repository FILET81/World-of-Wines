import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from WinesDatasetCleaning import wine_dataset_cleaning as wdc

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
    st.image("Images\Best Regions for Grape Growing.jpg", caption="The Wine Belt", width=950)
    st.markdown("- There are **18 noble grapes' varieties** -> '*planted **across the Globe**, and producing **high-quality** wines'*:")
    st.markdown("**Red** (lightest to darkest) -> ***Pinot Noir***, *Grenache*, ***Merlot***, *Sangiovese*, *Nebbiolo*, *Tempranillo*, ***Cabernet Sauvignon***, ***Syrah*** and *Malbec*.")
    st.markdown("**White** (lightest to richest) -> *Pinot Gris*, ***Riesling***, ***Sauvignon Blanc***, *Chenin Blanc*, *Moscato*, *Gewürztraminer*, *Sémillon*, *Viognier* and ***Chardonnay***.")
    #st.image("Images\Noble Varieties.jpg", caption="Noble Varieties", width=650)





elif selection=="Vizzes":     # Embedding "Tableau Public" vizzes
    st.header("Let's play a bit with the data! :grapes:")





elif selection=="Wine Searcher":     # Displaying the wine Searcher out of the treated DataFrame
    def wine_searcher():
        #from WinesDatasetCleaning import wine_dataset_cleaning as wdc
        # Loading the dataset:
        wines_dataset = wdc()
        
        # Getting unique values:
        w_country = sorted(wines_dataset["country"].unique().tolist(), reverse=False)
        w_type = sorted(wines_dataset["wine_type"].unique().tolist(), reverse=False)
        w_monovarietal = ["yes", "no"]     # Boolean values!!!
        w_noble = ["yes", "no"]     # Boolean values!!!
        w_vintage = sorted(wines_dataset["vintage"].unique().tolist(), reverse=True)
        #w_min_price, w_max_price = wines_dataset["price_usd"].min(), wines_dataset["price_usd"].max()

        # Coding Streamlit:
        st.header("Let's look for a tasty wine! :face_with_monocle:")
        st.image("Images\Vineyards-6.jpg", caption="Vineyards somewhere in the World", width=950) 

        # Determining all other filters:
        # Selecting countries with option "All" included:
        selected_country = st.multiselect("Please choose a country from the list:", ["All Countries"] + w_country)
        if "All Countries" in selected_country:
            selected_country = w_country
        if selected_country:
            filtered_country = wines_dataset[wines_dataset["country"].isin(selected_country)]
        else:
            filtered_country = wines_dataset
        
        # Determining "min" and "max" price based on the filtered data in order to have a dynamic "st.slider":
        #w_min_price = filtered_country["price_usd"].min()
        #w_max_price = filtered_country["price_usd"].max()

        # Selecting wine types with option "All" included:
        selected_type = st.multiselect("What type of wine would you like to find?", ["All Types"] + w_type)
        if "All Types" in selected_type:
            selected_type = w_type
        if selected_type:
            filtered_type = wines_dataset[wines_dataset["wine_type"].isin(selected_type)]
        else:
            filtered_type = wines_dataset
        
        #
        selected_monovarietal = st.radio("Would you like a monovarietal wine?", w_monovarietal) == "no"     # "== "yes/no"" avoids empty DataFrame in case user doesn't select
        
        #
        selected_noble = st.radio("Would you like a noble grape variety?", w_noble) == "no"     # "== "yes/no"" avoids empty DataFrame in case user doesn't select
        
        # Selecting wine vintages with option "All" included:
        selected_vintage = st.multiselect("Please choose a vintage from the list:", ["All Vintages"] + w_vintage)
        if "All Vintages" in selected_vintage:
            selected_vintage = w_vintage
        if selected_vintage:
            filtered_vintage = wines_dataset[wines_dataset["vintage"].isin(selected_vintage)]
        else:
            filtered_vintage = wines_dataset
        
        ### Filtering the dataset in order to have a dynamic "st.slider":
        filtered_data = wines_dataset[
                (wines_dataset["country"].isin(selected_country) if selected_country else True) &     # "if selected_type else True" avoids empty DataFrame in case user doesn't select
                (wines_dataset["wine_type"].isin(selected_type) if selected_type else True) &     # "if selected_type else True" avoids empty DataFrame in case user doesn't select
                (wines_dataset["monovarietal"]==selected_monovarietal) &
                (wines_dataset["noble_international"]==selected_noble) &
                (wines_dataset["vintage"].isin(selected_vintage) if selected_vintage else True)     # "if selected_type else True" avoids empty DataFrame in case user doesn't select
                ]     
        
        # Determining "min" and "max" price based on the filtered data:
        if not filtered_data.empty:
            w_min_price = filtered_data["price_usd"].min()
            w_max_price = filtered_data["price_usd"].max()
        else:
            w_min_price = wines_dataset["price_usd"].min()
            w_max_price = wines_dataset["price_usd"].max()

        #
        selected_max_price = st.slider("What's the maximum price ($) would you like to pay?", int(w_min_price), int(w_max_price), value=int(w_max_price))

        if st.button("Find"):
            st.progress(100)
            wines_found = filtered_data[
                filtered_data["price_usd"] < selected_max_price
                ].sort_values(by=["points", "price_usd", "vintage"], ascending=[False, False, False])#.head(15)

            if not wines_found.empty:
                st.success("Congrats, wines matching your criteria are found! :smiley:\n"
                           "Find below a list of the 15 best wines according to such criteria:")

                # Reseting index and setting it up in order to start from 1:
                wines_found.reset_index(drop=True, inplace=True)
                wines_found.index = np.arange(1, len(wines_found) + 1)

                # Showing the resulting DataFrame:
                st.dataframe(wines_found[["points",
                                          "price_usd",
                                          "vintage",
                                          "country",
                                          "winery",
                                          "apellation",
                                          "wine_type",
                                          "variety",                                          
                                          "taste_dry-sweet",
                                          "taste_body",
                                          "taste_tannins",
                                          "taste_acidity",
                                          "avg_abv_%",
                                          "avg_serve_temp_c",
                                          "primary_flavors"]])
            else:
                st.error("Pity, no wines are found with these criteria! :disappointed_relieved:\n"
                         "Try to modify them for a successful search!")
    
    if __name__ == "__main__":
        wine_searcher()
            





elif selection=="Price Predictor":     # Displaying a Machine Learning model
    st.header("Let's try to predict some prices! :gear:")
    
    
    #Tabs:
    tab1, tab2, tab3=st.tabs(["Logistic Regression", "K-Nearest Neighbors", "Random Forest"])
    with tab1:
        tab1.write("I'm the first tab")

        st.button("Guess1")
    with tab2:
        st.write("That's the second tab")
    
        st.button("Guess2")

    with tab3:
            st.write("You are the third tab")
        
            st.button("Guess3")



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