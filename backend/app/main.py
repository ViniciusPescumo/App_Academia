from fastapi import FastAPI
import backend.app.models as models

app = FastAPI(title="EM DESENVOLVIMENTO")

#ROTAS#


@app.get("/")
async def root():
    ...


@app.post("/")
async def search():
    ...

@app.post("/{id}")
async def search_id():
    ...

@app.put("/{id}")
async def refresh():
    ...



@app.delete("/{id}")
async def delete():
    ...