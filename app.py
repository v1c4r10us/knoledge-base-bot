from fastapi import FastAPI
import json
import pandas as pd

with open("data.json") as f:
    data=json.load(f)
f.close()

app=FastAPI(
                title="TurismoPE",
                version="1.0",
                contact={
                            "name": "v1c4r10us",
                            "email": "v1c4r10us.29@gmail.com",
                },
                license_info={
                            "name": "Apache 2.0",
                            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
                }
            )

@app.get('/', tags=['Welcome'])
def welcome():
    return {'version': 'v1.0', 
            'published':'2023',
            'contributors': 'Edgard Huanca',
            'github':'',
            'documentation':''}

@app.get("/tours")
def get_tours(keyword:str):
    df=pd.DataFrame.from_dict(data)
    df['title']=df['title'].str.lower()
    df_filtered=df[df['title'].str.contains(keyword)]
    search_idx=list(df_filtered.index)
    return [data[i] for i in search_idx]
