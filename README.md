#  A1.3 Real-Time AI Meeting Assistant

A Real-Time AI Meeting Assistant that captures meeting conversations, displays a live transcript, maintains a continuously updated summary, and allows users to ask questions based on the meeting context.

This project demonstrates real-time data flow, backend–frontend integration, and intelligent meeting understanding using a modular and extensible architecture.

---

##  Features

-  Live meeting transcript (real-time updates)
-  Live meeting summary (key points & decisions)
-  Question & Answer interface based on meeting context
-  Clean REST API using FastAPI
-  Simple, responsive frontend using HTML, CSS, and JavaScript
-  Modular backend design (easy to extend to real audio & LLMs)

---

##  Project Structure
<img width="663" height="599" alt="image" src="https://github.com/user-attachments/assets/4ba05d46-7afb-46f1-8d1f-4b37aed40c82" />


---

##  Tech Stack

### Backend
- Python
- FastAPI
- AsyncIO
- REST APIs

### Frontend
- HTML
- CSS
- JavaScript (Vanilla)

---

##  Assumptions

- This version uses **mock meeting audio** to ensure reliability and ease of local testing.
- No external API keys (LLMs) are required for running the demo.
- The architecture is intentionally designed to support real-time audio ingestion and LLM-based Q&A in future extensions.

---

##  Dependencies

All backend dependencies are listed in `requirements.txt`.

Main dependencies include:
- fastapi
- uvicorn
- pydantic
- python-dotenv

---

##  Setup Instructions

### 1) Clone the Repository
```bash
git clone <your-github-repo-url>
cd real-time-ai-meeting-assistant
```
### 2) Create & Activate Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate

##OR

python3 -m venv .venv
source .venv/bin/activate
```
### 3) Install Dependencies
```bash
pip install -r requirements.txt
```
### 4) Environment Variables
```bash
git clone <your-github-repo-url>
cd real-time-ai-meeting-assistant
```
---

## Running the Assignment Locally
### 1)Start Backend Server

```bash
python -m uvicorn backend.main:app --reload
```
Backend will run at: http://localhost:8000

### 2)Start Frontend Server

```bash
cd frontend
python -m http.server 5500
```

Frontend will be available at: http://localhost:5500
