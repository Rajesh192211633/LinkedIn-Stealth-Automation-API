# LinkedIn Stealth Automation API

## Setup Instructions

1. Create virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # or source venv/bin/activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the API server:
   ```
   uvicorn app.main:app --reload
   ```

4. Open your browser at:
   ```
   http://127.0.0.1:8000/docs
   ```

## Features

- Login to LinkedIn
- Send connection requests
- Send messages if already connected
- Close browser session
