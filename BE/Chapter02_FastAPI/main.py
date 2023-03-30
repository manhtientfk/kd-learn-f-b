# from fastapi import FastAPI
# app = FastAPI()


# @app.get("/hello")
# async def hello(name: str, age: int):
#     return {"name": name, "age": age}


def chia(a: int, b: int) -> float:
    return a/b


print(chia('2.3', 4))
