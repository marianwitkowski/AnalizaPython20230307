# REST API
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, StreamingResponse, PlainTextResponse
import uvicorn
from typing import Optional
import numpy as np
import pandas as pd

app = FastAPI()

df = pd.read_csv("pkn_d.csv", parse_dates=True, index_col="Data")

@app.get("/voltage", description="jakiś endpoint")
async def get_voltage(param1:str, param2:int,
                      q:Optional[str]=Query(None,
                                            min_length=2, max_length=10,
                                            title="parametr opcjonalny",
                                            description="jakiś tam opis"
                                            )):
    return {
        "param1" : param1,
        "param2" : param2,
        "q" : q
    }

@app.get("/pkn")
async def get_pkn(d1:str, d2:str):
    df1 : pd.DataFrame = df.loc[d1:d2]
    return df1["Zamkniecie"].to_dict()

@app.get("/np")
async def get_numpy():
    arr = np.random.randn(10)
    #return {"data":arr}
    s = "|".join( [str(x) for x in arr] )
    #s = np.array2string(arr)
    return PlainTextResponse(s)

@app.get("/img")
async def get_image():
    fd = open("bokeh_plot.png", mode="rb")
    return StreamingResponse(fd, media_type="image/png")

@app.get("/hello1")
async def hello_world1():
    html = "<html><h1>Hello world!</h1></html>"
    return HTMLResponse(html, status_code=200)


@app.get("/hello")
async def hello_world():
    return {"message":"Hello world!"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=1234,  reload=True)