from fastapi import FastAPI

app = FastAPI(title="Hybrid NIDS")

app.get("/")
def root():
    return {"Status:Phase0"}