# 💬 WhatsApp Business Support Automation

A lightweight **WhatsApp Business Support Automation** system built with **Python, FastAPI, Twilio, and WhatsApp Webhooks**.

The application receives incoming WhatsApp messages through a webhook, processes user requests, and automatically sends structured responses for common business-support queries.

The project demonstrates how messaging platforms, backend APIs, and automation workflows can be combined to build practical customer communication systems.

---

## 🚀 Overview

Businesses often receive repetitive customer queries such as:

- Company information
- Service enquiries
- Contact details
- Office locations
- Consultation requests
- Basic customer support questions

This project automates these interactions through **WhatsApp**.

Instead of manually responding to every initial enquiry, the system provides a structured menu and automatically routes the user to the appropriate response.

---

## ✨ Features

- 💬 WhatsApp automated responses
- 📋 Menu-driven customer interaction
- 🔗 Twilio WhatsApp integration
- ⚡ FastAPI backend
- 🪝 Webhook-based message processing
- 🏢 Business information automation
- 📑 Service enquiry workflow
- 📍 Contact and office information
- 🗓 Consultation request workflow
- 🔄 Automatic message routing
- 📡 REST/Webhook architecture
- 📤 TwiML response generation
- 🐍 Lightweight Python implementation

---

## 🛠 Tech Stack

### Backend

![Python](https://img.shields.io/badge/Python-Backend-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688)

- Python
- FastAPI

### Messaging & Integration

![Twilio](https://img.shields.io/badge/Twilio-WhatsApp-red)
![WhatsApp](https://img.shields.io/badge/WhatsApp-Automation-25D366)

- Twilio
- WhatsApp
- Webhooks
- TwiML

### API

- REST APIs
- HTTP POST Webhooks
- Form Data Processing

### Deployment

- Procfile-based deployment support
- Python dependency management using `requirements.txt`

---

## 🧠 How It Works

The application follows a simple webhook-driven architecture.

```text
WhatsApp User
      │
      ▼
Twilio WhatsApp
      │
      ▼
Incoming Webhook
      │
      ▼
FastAPI /webhook
      │
      ▼
Extract Message Body
      │
      ▼
Message Processing
      │
      ▼
Business Logic / Menu Routing
      │
      ▼
Generate TwiML Response
      │
      ▼
Twilio
      │
      ▼
WhatsApp User
```

---

## 💬 Conversation Flow

A user starts the conversation by sending:

```text
Hi
Hello
Start
```

The application responds with a structured menu:

```text
👋 Welcome to Business Support

How can we assist you today?

1️⃣ About Business
2️⃣ Services Overview
3️⃣ Contact & Offices
4️⃣ Request a Consultation

Reply with a number.
```

The user can then select an option.

### Option 1 — About Business

Returns information about the organization and its services.

### Option 2 — Services Overview

Returns available business and professional services.

### Option 3 — Contact & Offices

Returns contact and office information.

### Option 4 — Request a Consultation

Asks the customer to provide information required for a consultation request.

---

## 🔌 API Endpoint

### WhatsApp Webhook

```http
POST /webhook
```

The endpoint receives incoming WhatsApp messages forwarded by Twilio.

### Processing Flow

```text
Incoming WhatsApp Message
        │
        ▼
request.form()
        │
        ▼
Extract "Body"
        │
        ▼
handle_message()
        │
        ▼
Business Logic
        │
        ▼
MessagingResponse()
        │
        ▼
Generate TwiML
        │
        ▼
Return Response
```

---

## 🧩 Core Logic

The application uses a simple message handler to determine the appropriate response.

Example:

```python
def handle_message(message: str) -> str:
    msg = message.strip().lower()

    if msg in ["hi", "hello", "start"]:
        return "Welcome! Please select an option."

    elif msg == "1":
        return "About Business"

    elif msg == "2":
        return "Services Overview"

    elif msg == "3":
        return "Contact Information"

    elif msg == "4":
        return "Request a Consultation"

    return "Please type Hi to start."
```

This keeps the initial implementation simple while providing a foundation for more advanced conversational automation.

---

## 📂 Project Structure

```text
ai-auto-reply/
│
├── app/
│   └── main.py
│
├── data/
│
├── .gitignore
├── Procfile
├── requirements.txt
├── test_webhook.json
└── README.md
```

---

## ⚙️ Local Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
```

Move into the project:

```bash
cd ai-auto-reply
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
uvicorn app.main:app --reload
```

The application should start at:

```text
http://127.0.0.1:8000
```

---

## 📚 FastAPI Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### OpenAPI Schema

```text
http://127.0.0.1:8000/openapi.json
```

---

## 🔗 Twilio WhatsApp Integration

Twilio acts as the communication layer between WhatsApp and the FastAPI backend.

The basic flow is:

```text
WhatsApp
   ↓
Twilio
   ↓
FastAPI Webhook
   ↓
Response Generation
   ↓
Twilio
   ↓
WhatsApp
```

Configure the Twilio WhatsApp webhook to send incoming messages to:

```text
POST https://your-domain.com/webhook
```

During local development, a secure tunneling service can be used to expose the local FastAPI server to Twilio.

Example:

```text
Local FastAPI
http://127.0.0.1:8000

        ↓

Secure Tunnel

        ↓

Public HTTPS URL

        ↓

Twilio WhatsApp Webhook
```

---

## 🔐 Security

Secrets and credentials should **never be committed to GitHub**.

Sensitive configuration should be stored using environment variables.

Examples:

```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
```

Local environment files should be excluded through `.gitignore`.

Example:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

Before deploying or making the repository public, verify that the repository and its Git history do not contain:

- API keys
- Access tokens
- Twilio credentials
- Passwords
- Private customer information
- Internal business documents
- Production configuration secrets

---

## 🚀 Deployment Architecture

The application is designed to run as a lightweight backend service.

```text
WhatsApp
    ↓
Twilio
    ↓
Public HTTPS Endpoint
    ↓
FastAPI Application
    ↓
Message Processing
    ↓
Business Logic
    ↓
TwiML Response
```

A typical production deployment can follow:

```text
Development
    ↓
Testing
    ↓
Git
    ↓
Deployment
    ↓
Webhook Configuration
    ↓
Monitoring
```

---

## 🧪 Testing

Webhook requests can be tested using tools such as:

- Postman
- cURL
- Twilio Sandbox
- FastAPI Swagger UI
- Local webhook tunneling

The repository also contains:

```text
test_webhook.json
```

for webhook-related testing.

---

## 🔮 Future Improvements

The current version uses **structured menu-based automation**.

The architecture can be extended into a more advanced AI-powered customer-support platform.

Potential improvements include:

### 🤖 Generative AI

Integrate LLMs for natural conversational responses instead of relying only on predefined menu options.

```text
Customer Message
      ↓
LLM
      ↓
Intent Understanding
      ↓
Context-Aware Response
```

### 🧠 RAG

Connect the assistant with company documents and business knowledge.

```text
User Question
     ↓
Knowledge Retrieval
     ↓
Relevant Business Context
     ↓
LLM
     ↓
Grounded Response
```

### 🤖 AI Agents

Introduce agentic workflows capable of using tools and backend APIs.

Possible capabilities:

- Check customer information
- Create support requests
- Schedule consultations
- Retrieve business information
- Trigger backend workflows
- Escalate conversations

### 🗄 Database Integration

Store:

- Customer conversations
- Leads
- Consultation requests
- Support tickets
- Interaction history

### 👤 Human Agent Escalation

Automatically transfer complex requests to a human support representative.

### 📊 Analytics

Track:

- Number of conversations
- Common customer queries
- Response patterns
- Leads generated
- Consultation requests

### 🏢 Multi-Business SaaS

The architecture could eventually support multiple businesses from a single platform.

```text
Business A ─┐
Business B ─┼── AI Messaging Platform
Business C ─┘
                  ↓
            WhatsApp Automation
```

---

## 🗺 Evolution Roadmap

```text
Menu-Based Bot
      ↓
Intent Detection
      ↓
LLM Integration
      ↓
RAG Knowledge Base
      ↓
Conversation Memory
      ↓
Tool / Function Calling
      ↓
AI Agents
      ↓
Human Escalation
      ↓
Analytics
      ↓
Multi-Tenant SaaS Platform
```

---

## 🎯 Project Goal

The goal of this project is to explore how **WhatsApp, backend APIs, webhooks, and automation workflows** can be combined to create practical business communication systems.

The current implementation provides the core messaging and webhook infrastructure while creating a foundation for future **AI-powered conversational and agentic workflows**.

---

## 👨‍💻 Author

**Akash Gupta**

**AI Engineer | Agentic AI | Mobile & On-Device AI | GenAI | Computer Vision**

Focused on building production-oriented AI applications, intelligent mobile experiences, backend services, AI agents, and automation systems.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐.

Contributions, suggestions, and ideas for improving the project are welcome.
