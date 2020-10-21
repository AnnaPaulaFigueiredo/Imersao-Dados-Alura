import pandas as pd


i = 0
for chunk in pd.read_csv("MICRODADOS_ENEM_2019.csv", delimiter=";",encoding="ISO-8859-1",low_memory=False,chunksize=50000):
    
    data = chunk.query("NU_IDADE < 18")

    if i == 0:

        dfAges = pd.DataFrame(data)

    if len(data) > 0:

        
        dfAges.append(data, ignore_index=True)

    i = i + 1 
    
   

print(dfAges.head())
dfAges.to_csv("dataUnderAge.csv", sep=";", encoding="UTF-8" )

