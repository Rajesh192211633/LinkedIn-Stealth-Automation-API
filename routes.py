from fastapi import APIRouter
from pydantic import BaseModel
from app.browser_manager import BrowserManager
from app.automation import LinkedInAutomation

router = APIRouter()

browser = BrowserManager()
automation = None

class LoginRequest(BaseModel):
    username: str
    password: str

class ProfileRequest(BaseModel):
    profile_url: str
    message_if_connected: str = None

@router.post("/login")
def login(request: LoginRequest):
    global automation
    driver = browser.start()
    automation = LinkedInAutomation(driver)
    automation.login(request.username, request.password)
    return {"status": "Logged in"}

@router.post("/connect")
def connect(req: ProfileRequest):
    if not automation:
        return {"error": "Not logged in"}
    automation.go_to_profile_and_connect(req.profile_url, req.message_if_connected)
    return {"status": "Connection attempt complete"}

@router.post("/shutdown")
def shutdown():
    browser.stop()
    return {"status": "Browser closed"}