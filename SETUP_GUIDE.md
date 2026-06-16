# 🚀 Setup Guide - Email Automation Agent

## Step-by-Step Setup (1-2 Hours)

### ⏱️ STEP 1: Get Your API Keys (15 minutes)

#### 1.1 Groq API Key
1. Go to: https://console.groq.com
2. Sign up or login
3. Go to **API Keys** section
4. Click **Create New API Key**
5. Copy the key (starts with `gsk_`)
6. Paste it in `.env` file as `GROQ_API_KEY`

#### 1.2 Gmail OAuth Credentials
1. Go to: https://console.cloud.google.com
2. Create a new project (name it "Email Automation")
3. Search for **Gmail API** and enable it
4. Go to **Credentials** → Create Credentials → **OAuth 2.0 Desktop**
5. Download the JSON file
6. **Rename it to `credentials.json`**
7. Place it in the **root directory** (same folder as `main.py`)

---

### ⏱️ STEP 2: Update .env File (2 minutes)

Open `.env` file and replace:
```env
GROQ_API_KEY=gsk_YOUR_GROQ_API_KEY_HERE  
→ GROQ_API_KEY=gsk_xxxxxxxxxxxx (your actual key)

MY_EMAIL=your-email@gmail.com
→ MY_EMAIL=your-actual-email@gmail.com
```

---

### ⏱️ STEP 3: Update Knowledge Base (10 minutes)

Open `agency.txt` and replace the template content with **YOUR ACTUAL BUSINESS INFORMATION**:
- Your products/services
- Pricing information
- Company policies
- FAQ answers
- Contact information

This is used by the AI to answer customer questions!

---

### ⏱️ STEP 4: Install Dependencies (10 minutes)

Open PowerShell and run:
```powershell
cd c:\Users\Admin\Downloads\langgraph-email-automation-main
pip install -r requirements.txt
```

---

### ⏱️ STEP 5: Verify Gmail OAuth (5 minutes)

1. Run: `python main.py`
2. A browser window will open asking you to **authorize Gmail access**
3. Click **Allow**
4. A `token.json` file will be created automatically
5. The script will start processing emails

---

### ⏱️ STEP 6: Create Database (5 minutes)

1. Run: `python create_index.py`
   - This loads your `agency.txt` into the vector database (Chroma)
   - Creates the embeddings needed for RAG

---

### ✅ You're Done! 

Your email automation agent is ready. It will:
- ✅ Check Gmail every few minutes
- ✅ Categorize emails automatically
- ✅ Draft responses using AI
- ✅ Use your knowledge base (agency.txt) for product questions
- ✅ Check quality before sending

---

## 📋 **Files Checklist**

- [ ] `.env` file (created with GROQ_API_KEY & MY_EMAIL)
- [ ] `credentials.json` (from Google Cloud)
- [ ] `agency.txt` (updated with your business info)
- [ ] `requirements.txt` (dependencies installed)

---

## 🐛 Troubleshooting

**Error: "GROQ_API_KEY not found"**
- Make sure `.env` file exists in root directory
- Check the key is correct (starts with `gsk_`)

**Error: "GOOGLE_API_KEY not found"**
- Make sure `.env` file has the key
- Visit https://aistudio.google.com to get a new key

**Error: "credentials.json not found"**
- Download from Google Cloud Console
- Place in root directory (same level as main.py)
- Rename to exactly `credentials.json`

**Gmail authorization fails**
- Delete `token.json` if it exists
- Run `python main.py` again
- Authorize in the browser popup

---

## 🚀 Running the Agent

```powershell
python main.py
```

The agent will:
1. Fetch new emails from Gmail
2. Categorize them
3. Generate responses
4. Send them as drafts

Monitor the colored output to see what's happening!
