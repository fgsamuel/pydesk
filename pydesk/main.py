from fastapi import FastAPI

app = FastAPI()

@app.get("/{user}")
def main_route(user:str):
    return {"Hello": f"{user}!"}

