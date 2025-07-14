# KPA Backend Assignment - Harish

This is a backend assignment built using FastAPI and PostgreSQL to implement basic KPA Form APIs.

---

## Implemented APIs

### 1. POST `/formData/saveBasicFormData`
Saves user form data (name, gender, mobile, email) into PostgreSQL.

### 2. GET `/formData/getBasicFormDataByFormId/{form_id}`
Fetches the form data by its ID.

---

## Tech Stack

- **Backend:** Python FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Environment:** Python Dotenv
- **API Test Tool:** Postman

---
How to run:
1. Clone the repo
2. Create a virtual env and activate
3. Install dependencies: pip install -r requirements.txt
4. Set up PostgreSQL and .env file
5. Run with: uvicorn app.main:app --reload


Import the included `kpa_form_data.postman_collection.json` in Postman to test the API.




