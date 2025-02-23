def wine_variety_scrapping():
    # Importing necessary libraries:
    import warnings
    warnings.filterwarnings("ignore")
    import numpy as np
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup

    # Defining iterable items to scrap the Wikipedia, for both red and white grapes varieties:
    wiki = ["until", "from"]

    # Scrapping red grapes varieties: 
    pages_red = []

    for i in range(len(wiki)):
        headers = {"User-Agent":"MiAplicacion/1.0"}
        url_red = f"https://en.wikipedia.org/w/index.php?title=Category:Red_wine_grape_varieties&page{wiki[i]}=Marzemino#mw-pages"
        response_red = requests.get(url_red, headers=headers)
        pages_red.append(response_red.content)

    pages_wiki_red = []
    varieties_red = []

    for k in range(len(pages_red)):
        pages_wiki_red.append(BeautifulSoup(pages_red[k], "html.parser"))
        for j in pages_wiki_red[k].find_all("div", class_="mw-category-group"):
            for i in j.find_all("li"):
                varieties_red.append(i.get_text().title().replace("(Grape)","").replace("Grape","").replace("Mourvèdre","Mourvèdre/Monastrell").replace("Durif","Petite Sirah/Durif").replace("Carignan","Carignan/Mazuelo").replace("Alicante Bouschet","Alicante Bouschet/Garnacha Tintorera").strip())

    # Creating a DataFrame for red grapes varieties:
    wines_red = pd.DataFrame({"variety":varieties_red, "wine_type":"Red"})

    # Scrapping white grapes varieties: 
    pages_white = []

    for i in range(len(wiki)):
        headers = {"User-Agent":"MiAplicacion/1.0"}
        url_white = f"https://en.wikipedia.org/w/index.php?title=Category:White_wine_grape_varieties&page{wiki[i]}=Marsanne#mw-pages"
        response_white = requests.get(url_white, headers=headers)
        pages_white.append(response_white.content)

    pages_wiki_white = []
    varieties_white = []

    for k in range(len(pages_white)):
        pages_wiki_white.append(BeautifulSoup(pages_white[k], "html.parser"))
        for j in pages_wiki_white[k].find_all("div", class_="mw-category-group"):
            for i in j.find_all("li"):
                varieties_white.append(i.get_text().title().replace("(Grape)","").replace("(Spanish Grape)","").replace("(Wine)","").replace("À","à").replace("Of","of").replace("Macabeo","Viura/Macabeo").replace("Prosecco","Glera/Prosecco").replace("Sauvignonasse","Sauvignonasse/Friulano").strip())

    # Creating a DataFrame for white grapes varieties:
    wines_white = pd.DataFrame({"variety":varieties_white, "wine_type":"White"})

    # Defining and creating a DataFrame with 'extra' varieties, to be also considered in further steps of the project:
    data_extra = [{"variety":"Cabernet Sauvignon-Carménère", "wine_type":"Red"}, 
                  {"variety":"Cabernet Sauvignon-Malbec", "wine_type":"Red"}, 
                  {"variety":"Cabernet Sauvignon-Merlot", "wine_type":"Red"}, 
                  {"variety":"Cabernet Sauvignon-Syrah", "wine_type":"Red"},
                  {"variety":"Cabernet Sauvignon-Tempranillo", "wine_type":"Red"},
                  {"variety":"Malbec-Merlot", "wine_type":"Red"},
                  {"variety":"Port", "wine_type":"Red"},
                  {"variety":"Red Blend", "wine_type":"Red"},
                  {"variety":"Rosé", "wine_type":"Rosé"},
                  {"variety":"Sauvignon Blanc-Sémillon", "wine_type":"White"},
                  {"variety":"Sherry", "wine_type":"White"},
                  {"variety":"Sparkling Blend", "wine_type":"Sparkling"},
                  {"variety":"Syrah-Grenache", "wine_type":"Red"},
                  {"variety":"Tinta De Toro", "wine_type":"Red"},
                  {"variety":"Tinto Fino", "wine_type":"Red"},
                  {"variety":"Turbiana", "wine_type":"White"},
                  {"variety":"White Blend", "wine_type":"White"},
                  {"variety":"Pinot Noir-Chardonnay-Pinot Meunier", "wine_type":"Sparkling"},     # Champagne Blend       
                  {"variety":"Cabernet Sauvignon-Merlot-Other Bordeaux", "wine_type":"Red"},     # Bordeaux-style Red Blend
                  {"variety":"Sauvignon Blanc-Sémillon-Other Bordeaux", "wine_type":"White"},     # Bordeaux-style White Blend
                  {"variety":"Grenache-Syrah-Mourvèdre/Monastrell", "wine_type":"Red"},     # Rhône-style Red Blend + G-S-M
                  {"variety":"Marsanne-Roussane-Viognier", "wine_type":"White"}]     # Rhône-style White Blend

    wines_extra = pd.DataFrame(data_extra)

    # Putting all DataFrames together, in a single one:
    wines_type = pd.concat([wines_red, wines_white, wines_extra], axis=0, ignore_index=True)
    return wines_type
