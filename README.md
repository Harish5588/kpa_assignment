# KPA Backend Assignment - Harish

This project implements two backend APIs based on the provided Postman collection and Swagger documentation from [Suvidhaen KPA Form API](https://app.swaggerhub.com/apis/sarvasuvidhaen/kpa-form_data/1.0.0).

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


