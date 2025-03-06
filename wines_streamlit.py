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

# Providing some info about the world of wines:
if selection=="Introduction":     
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
    st.image("https://media.winefolly.com/18-noble-grapes-diagram-winefolly.jpg", caption="Noble Varieties", width=950)

# Embedding "Tableau Public" vizzes:
elif selection=="Vizzes":     
    st.header("Let's play a bit with the data! :grapes:")
    
    def vizzes():
        html_temp="""<div class='tableauPlaceholder' id='viz1741271631515' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;wi&#47;wine_vizzes&#47;VarietiesbyCountry&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='wine_vizzes&#47;VarietiesbyCountry' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;wi&#47;wine_vizzes&#47;VarietiesbyCountry&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1741271631515');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='800px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, width=1500, height=1200)
    if __name__ == '__main__':
            vizzes()

# Defining the wine Searcher:
elif selection=="Wine Searcher":

    # Charging flags for each country:
    arg_image = "https://flagcdn.com/h20/ar.webp"     # "https://flagpedia.net/data/flags/w1160/ar.webp"
    aus_image = "https://flagcdn.com/h20/au.webp"     # "https://flagpedia.net/data/flags/w1160/au.webp"
    chl_image = "https://flagcdn.com/h20/cl.webp"     # "https://flagpedia.net/data/flags/w1160/cl.webp"
    esp_image = "https://flagcdn.com/h20/es.webp"     # "https://flagpedia.net/data/flags/w1160/es.webp"
    ita_image = "https://flagcdn.com/h20/it.webp"     # "https://flagpedia.net/data/flags/w1160/it.webp"
    deu_image = "https://flagcdn.com/h20/de.webp"     # "https://flagpedia.net/data/flags/w1160/de.webp"
    aut_image = "https://flagcdn.com/h20/at.webp"     # "https://flagpedia.net/data/flags/w1160/at.webp"
    nzl_image = "https://flagcdn.com/h20/nz.webp"     # "https://flagpedia.net/data/flags/w1160/nz.webp"
    zaf_image = "https://flagcdn.com/h20/za.webp"     # "https://flagpedia.net/data/flags/w1160/za.webp"
    prt_image = "https://flagcdn.com/h20/pt.webp"     # "https://flagpedia.net/data/flags/w1160/pt.webp"
    fra_image = "https://flagcdn.com/h20/fr.webp"     # "https://flagpedia.net/data/flags/w1160/fr.webp"
    usa_image = "https://flagcdn.com/h20/us.webp"     # "https://flagpedia.net/data/flags/w1160/us.webp"
    
    #Creating a dictionary to link each country of the dataset with the corresponding flag:
    flags_dict = {"Argentina":arg_image,
                  "Australia":aus_image,
                  "Chile":chl_image,
                  "Spain":esp_image,
                  "Italy":ita_image,
                  "Germany":deu_image,
                  "Austria":aut_image,
                  "New Zealand":nzl_image,
                  "South Africa":zaf_image,
                  "Portugal":prt_image,
                  "France":fra_image,
                  "United States":usa_image}
    
    # Displaying the wine Searcher out of the treated DataFrame:
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
        st.image("Images\Vineyards-6.jpg", caption="Vineyards somewhere in the World", width=900) 

        # Determining all other filters:
        # Selecting countries with option "All" included:
        selected_country = st.multiselect("Please choose a country from the list:", ["All Countries"] + w_country)
        if "All Countries" in selected_country or len(selected_country) == 0:
            selected_country = w_country
        #if selected_country:
        #    filtered_country = wines_dataset[wines_dataset["country"].isin(selected_country)]
        #else:
        #    filtered_country = wines_dataset
        
        # Determining "min" and "max" price based on the filtered data in order to have a dynamic "st.slider":
        #w_min_price = filtered_country["price_usd"].min()
        #w_max_price = filtered_country["price_usd"].max()

        # Selecting wine types with option "All" included:
        selected_type = st.multiselect("What type of wine would you like to find?", ["All Types"] + w_type)
        if "All Types" in selected_type:
            selected_type = w_type
        #if selected_type:
        #    filtered_type = wines_dataset[wines_dataset["wine_type"].isin(selected_type)]
        #else:
        #    filtered_type = wines_dataset
        
        # Selecting monovarietal wines (yes/no):
        selected_monovarietal = st.radio("Would you like a monovarietal wine?", w_monovarietal) == "yes"     # "== "yes/no"" avoids empty DataFrame in case user doesn't select
        
        # Selecting noble grape's varieties (yes/no):
        selected_noble = st.radio("Would you like a noble grape variety?", w_noble) == "yes"     # "== "yes/no"" avoids empty DataFrame in case user doesn't select
        
        # Selecting wine vintages with option "All" included:
        selected_vintage = st.multiselect("Please choose a vintage from the list:", ["All Vintages"] + w_vintage)
        if "All Vintages" in selected_vintage:
            selected_vintage = w_vintage
        #if selected_vintage:
        #    filtered_vintage = wines_dataset[wines_dataset["vintage"].isin(selected_vintage)]
        #else:
        #    filtered_vintage = wines_dataset
        
        ### Filtering the dataset in order to have a dynamic "st.slider":
        filtered_data = wines_dataset[
                (wines_dataset["country"].isin(selected_country)) &     # "if selected_type else True" avoids empty DataFrame in case user doesn't select
                (wines_dataset["wine_type"].isin(selected_type))  &     # "if selected_type else True" avoids empty DataFrame in case user doesn't select
                (wines_dataset["monovarietal"]==selected_monovarietal) &
                (wines_dataset["noble_international"]==selected_noble) &
                (wines_dataset["vintage"].isin(selected_vintage))     # "if selected_type else True" avoids empty DataFrame in case user doesn't select
                ]     
        # Determining "min" and "max" price based on the filtered data:
        if not filtered_data.empty:
            w_min_price = filtered_data["price_usd"].min()
            w_max_price = filtered_data["price_usd"].max()
            if w_min_price == w_max_price:
                w_max_price = w_min_price + 1     # Adjustment to avoid slider issues (when min_price = max_price)!
        else:
            w_min_price = wines_dataset["price_usd"].min()
            w_max_price = wines_dataset["price_usd"].max()

        # Selecting "max" price the user would like to pay through "st.slider":
        selected_max_price = st.slider("What's the maximum price ($) would you like to pay?", int(w_min_price), int(w_max_price), value=int(w_max_price))

        if st.button("Find"):
            st.progress(100)
            wines_found = filtered_data[
                filtered_data["price_usd"] < selected_max_price
                ].sort_values(by=["points", "price_usd", "vintage"], ascending=[False, False, False])
            if not wines_found.empty:
                st.success("Congrats, wines matching your criteria are found! :smiley:\n"
                           "Find below a list of the best wines according to such criteria:")

                displayed_wines = set()
                counter = 0
                for index, row in wines_found.head(15).iterrows():

                    wine_key = (row["title_new"], row["vintage"], row["apellation"])

                    if wine_key in displayed_wines:
                        continue
    
                    displayed_wines.add(wine_key)

                    with st.container():
                        col1, col2 = st.columns(2)

                        with col1:                    
                            counter += 1
                            st.header(f"{counter}. {row["title_new"]}")
                            st.image(flags_dict[row["country"]], width=30)
                            st.write(f"**Country:** {row["country"]}")
                            st.write(f"**Points:** {row["points"]}")
                            st.write(f"**Price:** ${row["price_usd"]} USD")
                            st.write(f"**Vintage:** {row["vintage"]}")
                            st.write(f"**Apellation:** {row["apellation"]}")
                            st.write(f"**Type:** {row["wine_type"]}")
                            st.write(f"**Variety:** {row["variety"]}")
                                      
                        with col2:
                            st.header("Tasting Notes")
                            st.image("Images\White Background Landscape.jpg", width=30)
                            st.write(f"**Rating Sweetness:** {row["taste_dry-sweet"]}")
                            st.write(f"**Rating Body:** {row["taste_body"]}")
                            st.write(f"**Rating Tannins:** {row["taste_tannins"]}")
                            st.write(f"**Rating Acidity:** {row["taste_acidity"]}")
                            st.write(f"**ABV (Avg):** {row["avg_abv_%"]} %")
                            st.write(f"**Service Temperature (Avg):** {row["avg_serve_temp_c"]}° Celsius")
                            st.write(f"**Primary Flavors:** {row["primary_flavors"]}")
                            
                        st.markdown("---")
                
            else:
                st.error("Pity, no wines are found with these criteria! :disappointed_relieved:\n"
                         "Try to modify them for a successful search!")
    
    if __name__ == "__main__":
        wine_searcher()

# Displaying a Machine Learning model:
elif selection=="Price Predictor":     
    st.header("Let's try to predict some prices! :gear:")
    
    #Tabs:
    tabml1, tabml2, tabml3, tabml4=st.tabs(["Linear Regression", "Random Forest Regressor", "Support Vector Regressor", "Predictor"])
    with tabml1:
        st.write("I'm the first tab")


        
    with tabml2:
        st.write("I'm the second tab")
    
        

    with tabml3:
        st.write("What a NIGHTMARE!!!")
        
        
    
    with tabml4:
        st.write("Let's predict an affordable wine's price:")

        #st.button("Guess", on_click=lambda: predict())

# Finishing the Presentation:
else:     
    st.subheader("Main Data Sources:")
    st.markdown("https://mavenanalytics.io/")
    st.markdown("https://winefolly.com/")
    st.markdown("https://www.wikipedia.org/")
    st.markdown("https://flagpedia.net/")
    st.markdown("And many others...")
    st.markdown("")
    st.subheader("THANKS FOR LISTENING!!!")
    st.image("Images\Vineyards-7.jpg", caption="Vineyards somewhere in the World", width=950)