import pandas as pd

#index_col="Name" will help set index as name
df = pd.read_csv("pokemon.csv") 


#           FILTERING = KEEPING THE ROWS THAT MATCH A CONDITION

# tall_pokemon = df[ df ["Height"] >= 2 ]
# print(tall_pokemon)


# heavy_pokemon = df[df ["Weight"] > 100 ]
# print(heavy_pokemon)


# legendary_pokemon = df[df["Legendary"] == 1]  #True/1
# print(legendary_pokemon)


# water_pokemon = df[df["Type1"] == "Water"]
# water_pokemon = df[ ( df["Type1"]=="Water" ) | ( df["Type2"]=="Water" ) ]

# print(water_pokemon)

#ff_pokemon = df[(df["Type1"]=="Fire") &
#                (df["Type2"]=="Flying")]

#print(ff_pokemon)