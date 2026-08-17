# 🚀 Enterprise AI MailOps Platform

**Intelligent Email Automation System powered by LangGraph and RAG**

> Transform your customer support with AI-driven email automation. Automate categorization, draft generation, and quality assurance using advanced AI agents and retrieval-augmented generation.

---

## 📋 Overview

The **Enterprise AI MailOps Platform** is an enterprise-grade email automation system that leverages multi-agent AI orchestration to intelligently manage customer emails. Using LangGraph's workflow engine and Retrieval-Augmented Generation (RAG), this platform automatically categorizes emails, generates contextual responses, and ensures quality before sending.

### Key Capabilities

✅ **Email Inbox Automation** - Continuous Gmail monitoring and management  
✅ **Categorization Agent** - AI-powered intelligent email classification (complaints, inquiries, feedback, unrelated)  
✅ **RAG-Powered Response Generation** - Context-aware drafts using Retrieval-Augmented Generation and Groq LLM  
✅ **Quality Assurance Agent** - Automated verification checks for quality, formatting, and relevance  
✅ **Knowledge-Based Responses** - Chroma vector database with HuggingFace embeddings for accurate product/service information  
✅ **Production-Ready Architecture** - Scalable, secure, enterprise-grade state management and workflow orchestration  

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────┐
│            Gmail Inbox (Email Source)               │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│         Email Loader & Categorizer Agent             │
│  (LangGraph + AI - Classify: Complaint/Inquiry/ FB.)  │
└──────────────┬──────────────────────────────────────┘
               │
        ┌──────┴──────┐
        ▼             ▼
   ┌────────┐    ┌──────────┐
   │Complaint│    │ Inquiry  │
   │ Response│    │  RAG     │
   │Generator│    │ Search   │
   └────┬───┘    └─────┬────┘
        │              │
        └──────┬───────┘
               ▼
    ┌─────────────────────┐
    │  Quality Checker    │
    │ (Verification Agent)│
    └────────┬────────────┘
             ▼
    ┌─────────────────────┐
    │   Draft Email       │
    │  (Ready to Send)    │
    └─────────────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Workflow Orchestration** | LangGraph with multi-agent coordination |
| **State Management** | LangGraph StateGraph with persistent state tracking |
| **LLM** | Groq (llama-3.3-70b-versatile - high-speed inference) |
| **Vector Database** | Chroma with HuggingFace Embeddings (all-MiniLM-L6-v2) |
| **Email Integration** | Gmail API with OAuth 2.0 authentication |
| **Backend Framework** | FastAPI, LangServe (production-ready) |
| **Language** | Python 3.10+ |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Groq API Key ([Get it here](https://console.groq.com))
- Gmail API Credentials ([Setup guide](https://developers.google.com/gmail/api/quickstart/python))
- Virtual environment (venv)

### Run the Project on Windows (PowerShell)

**1. Open PowerShell in the project folder**
```powershell
cd "c:\Users\Admin\Downloads\Enterprise AI MailOps Platform\Enterprise AI MailOps Platform"
```

**2. Create a virtual environment**
```powershell
python -m venv venv
```

**3. Activate the virtual environment**
```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this first:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

**4. Install dependencies**
```powershell
pip install -r requirements.txt
```

**5. Create the environment file**
Create a file named `.env` in the project root and add:
```env
GROQ_API_KEY=your_groq_api_key_here
MY_EMAIL=your_email@gmail.com
```

**6. Add Gmail credentials**
- Download `credentials.json` from Google Cloud Console
- Place it in the project root folder
- The app will create `token.json` automatically after first run

**7. Build the vector database**
```powershell
python create_index.py
```

**8. Run the project**
```powershell
python main.py
```

**9. Test the workflow**
- Send a test email from a different Gmail account
- The app will check inbox every 60 seconds
- If the email is eligible, it will create a draft reply in your Gmail Drafts folder

### Example test email
```text
Subject: Question about pricing and features

Hi, I am interested in your AI agent platform. Can you please share your pricing plans, key features, and support response time?
```

---

## 📁 Project Structure

```
enterprise-ai-mailops-platform/
├── src/
│   ├── agents.py          # AI agents definition
│   ├── graph.py           # LangGraph workflow
│   ├── nodes.py           # Node functions
│   ├── prompts.py         # AI prompts
│   ├── state.py           # State management
│   ├── structure_outputs.py
│   └── tools/
│       └── GmailTools.py   # Gmail API integration
├── data/
│   └── agency.txt         # Knowledge base (customize this!)
├── db/                    # Vector database (auto-created)
├── main.py                # Entry point
├── create_index.py        # Vector DB creation
├── requirements.txt       # Dependencies
├── .env.example          # Environment template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

---

## ⚙️ Configuration

### Update Your Business Knowledge Base

Edit `data/agency.txt` with your actual information:

```
## Your Company Name
Description and services...

## Products & Services
1. Product A - Features and benefits
2. Product B - Features and benefits
3. Product C - Features and benefits

## Pricing
- Basic: $X/month
- Professional: $Y/month
- Enterprise: Custom

## Support
- Email: support@company.com
- Phone: +1-XXX-XXX-XXXX
- Response time: 24 hours
```

### Customize AI Behavior

Edit prompts in `src/prompts.py` to adjust:
- Email categorization logic
- Response generation style
- Quality check criteria

---

## 🔄 Workflow Process

1. **Email Monitoring** - Continuous Gmail inbox monitoring via Gmail API
2. **Categorization Agent** - AI-powered email classification (complaints, inquiries, feedback, unrelated)
3. **RAG-Powered Response Generation** - Intelligent draft creation:
   - **Complaints/Feedback** - Direct response via Groq LLM
   - **Product Inquiries** - Chroma vector DB RAG retrieval + Groq LLM synthesis
4. **Quality Assurance Agent** - Automated quality verification and formatting checks
5. **State Management** - Persistent workflow state tracking across all nodes
6. **Ready for Review** - Production-ready draft available for human approval before sending

---

## 📊 Example Output

```
Email Received:
From: customer@example.com
Subject: Pricing Question

Agent Processing Pipeline:
✓ Load & Inbox Check: Email loaded via Gmail API
✓ Categorization Agent: Classified as Product Inquiry
✓ RAG Search: Chroma vector DB retrieved 3 relevant documents
✓ Response Generation: Groq LLM (llama-3.3-70b-versatile) generated response
✓ Quality Assurance Agent: Verification passed ✅
✓ State Management: Workflow state updated and persisted
✓ Status: Production-ready draft ready for review
```

---

## 🔐 Security

- **API Keys**: Protected via `.env` (never committed)
- **OAuth 2.0**: Secure Gmail authentication
- **Token Storage**: Local `token.json` (excluded from git)
- **Credentials**: `credentials.json` not tracked
- **Database**: Local vector DB, no external calls

---

## 📝 Environment Variables

```env
# .env file (create from .env.example)
GROQ_API_KEY=your_groq_api_key          # From console.groq.com
MY_EMAIL=your-email@gmail.com           # Gmail account to monitor
```

---

## 🎯 Use Cases

- **Customer Support Automation** - Auto-respond to common inquiries
- **Lead Qualification** - Categorize and route leads
- **Email Categorization** - Organize inbox automatically
- **Knowledge-Based Support** - Answer questions from company docs
- **Email Quality Control** - Ensure professional responses

---


## 👨‍💻 Author

**Rishi Patel**  
## 👨‍💻 Author

**Rishi Patel**

- GitHub: https://github.com/rishipatel092005
- Project Repository: https://github.com/rishipatel092005/Enterprise-AI-MailOps-Platform

---

## 🙌 Acknowledgments

- Built with [LangChain](https://langchain.com) and [LangGraph](https://langgraph.dev)
- Powered by [Groq](https://console.groq.com) LLMs
- Vector embeddings from [HuggingFace](https://huggingface.co)
- Storage with [Chroma](https://www.trychroma.com)

---

## ❓ Support

For issues, questions, or suggestions:
- Open a GitHub Issue
- Check existing documentation
- Review setup guide in project root

---


