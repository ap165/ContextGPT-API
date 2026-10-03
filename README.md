# ContextGPT Backend API

The backend infrastructure for ContextGPT, an enterprise-grade internal knowledge base AI. Built with FastAPI, this service handles secure passwordless authentication (OTP + JWT), email notifications, document ingestion pipelines, and the core Retrieval-Augmented Generation (RAG) chat endpoints for querying company data.

## ✨ Key Features

*   **RAG Engine:** Processes user queries against a vector database of internal company documents to provide accurate, context-aware AI responses.
*   **Passwordless & OTP Authentication:** Secure login, registration, and password reset flows using email-based One-Time Passwords (OTPs).
*   **JWT Session Management:** Stateless authentication using JSON Web Tokens.
*   **Data Ingestion Pipeline:** Automated scripts to parse, chunk, and embed internal company policies and documents into the vector database.
*   **Custom Email Templates:** Beautiful, branded HTML email templates for user onboarding, security alerts, and OTP delivery.

## 🛠️ Tech Stack

*   **Framework:** FastAPI (Python)
*   **Server:** Uvicorn
*   **Database:** MongoDB Atlas (User data) & Vector Database (Document embeddings)
*   **Authentication:** JWT (JSON Web Tokens) & SMTP-based OTPs
*   **Architecture:** Modular REST API

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.10+ installed.

### 2. Installation
Clone the repository and install the required dependencies:
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```

### 3. Environment Variables

Create a `.env` file in the root directory. You will need configuration variables for your database, JWT secret, and SMTP server:

```env
# Database
MONGO_URI=mongodb+srv://:@cluster.mongodb.net/ContextGPT?retryWrites=true&w=majority

# Security
JWT_SECRET_KEY=your_super_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Email (SMTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_app_password

```

### 4. Running the Server

Start the FastAPI application using Uvicorn:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

```

The API documentation (Swagger UI) will be automatically generated and available at `http://localhost:8000/docs`.

## 📂 Architecture & File Structure

* **`/app/api/auth/`**: Authentication routes. Handles sending OTPs, verifying OTPs, logging in, registering, and issuing JWTs.
* **`/app/api/v1/chat.py`**: The core RAG chatbot endpoint. Validates the JWT, receives the user's query and 5-message conversation history, retrieves context from the vector DB, and returns the LLM response.
* **`/app/core/config.py`**: Centralized environment variable loading and configuration management.
* **`/app/data/policies/`**: The local directory for dropping raw company documents (PDFs, TXTs, Markdown) before ingestion.
* **`/app/scripts/`**: CLI utilities for database management.
* **`/app/templates/`**: HTML strings/files used by the SMTP utility to send branded ContextGPT emails.
* **`/app/utils/`**: Helper functions for database connections, JWT encoding/decoding, OTP generation, validation logic, and email dispatching.

## 🧠 Data Ingestion (RAG Setup)

Before the chatbot can answer company-specific questions, you must ingest your documents into the vector database.

1. Place your company documents (e.g., HR policies, technical docs) into the `/app/data/policies/` directory.
2. Initialize the database collections:
```bash
python -m app.scripts.create_db

```


3. Run the ingestion script to chunk, embed, and store the documents:
```bash
python -m app.scripts.ingest_data

```



## 🔒 Authentication Flow

1. **Request OTP:** Client calls `/api/auth/send-login-otp` with an email. Backend generates a 6-digit OTP, stores it temporarily, and emails it using templates in `/app/templates/`.
2. **Verify & Tokenize:** Client submits the OTP to `/api/auth/login`. Backend verifies the OTP and returns a JWT.
3. **Secure Access:** Client passes the JWT in the `Authorization: Bearer ` header to access `/api/v1/chat`. The token is validated via `/app/utils/_jwt.py`.
