from fastapi import FastAPI
from app.automation import LinkedInBot

app = FastAPI()
bot = LinkedInBot()

@app.post("/login")
def login(username: str, password: str):
    return bot.login(username, password)

@app.post("/connect")
def connect(profile_url: str):
    return bot.connect(profile_url)

@app.post("/message")
def message(profile_url: str, text: str):
    return bot.send_message(profile_url, text)

@app.post("/close")
def close():
    bot.close()
    return {"status": "Session closed"}
