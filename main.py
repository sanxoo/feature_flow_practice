from fastapi import FastAPI

from routers import users, items

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
def welcome():
    return {"message": "welcome to service!"}

if __name__ == "__main__":
    import uvicorn
    import config
    uvicorn.run(app, host=config.service_host, port=int(config.service_port), log_config=config.log_config)

