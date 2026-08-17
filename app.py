"""
🚀 Enterprise AI MailOps Platform - FastAPI Web Server
Access via: http://YOUR_IP:8000
"""

from dotenv import load_dotenv
import os

# Load environment variables FIRST
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import asyncio
import threading
import time
from src.graph import Workflow
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Create FastAPI app
app = FastAPI(
    title="Enterprise AI MailOps Platform",
    description="Intelligent Email Automation System powered by LangGraph and RAG",
    version="1.0.0"
)

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global workflow instance
workflow = None
is_running = False
last_check_time = None
email_stats = {
    "total_checks": 0,
    "emails_processed": 0,
    "successful_sends": 0,
    "last_check": None
}

class EmailCheckRequest(BaseModel):
    """Request model for manual email check"""
    run_once: bool = False

@app.on_event("startup")
async def startup_event():
    """Initialize workflow on startup"""
    global workflow
    try:
        print(Fore.GREEN + "🚀 Initializing workflow on startup..." + Style.RESET_ALL)
        workflow = Workflow()
        print(Fore.GREEN + "✅ Workflow initialized successfully!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"❌ Error initializing workflow: {str(e)}" + Style.RESET_ALL)

@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "🚀 Enterprise AI MailOps Platform",
        "status": "running",
        "endpoints": {
            "health": "/health",
            "check_emails": "/check-emails",
            "start_automation": "/start-automation",
            "stop_automation": "/stop-automation",
            "status": "/status",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "workflow_initialized": workflow is not None,
        "automation_running": is_running,
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }

@app.get("/status")
async def get_status():
    """Get current automation status and statistics"""
    return {
        "automation_running": is_running,
        "statistics": email_stats,
        "last_check": last_check_time,
        "workflow_initialized": workflow is not None
    }

@app.post("/check-emails")
async def check_emails_manual():
    """Manually trigger an email check"""
    global workflow, email_stats
    
    if workflow is None:
        raise HTTPException(status_code=500, detail="Workflow not initialized")
    
    try:
        print(Fore.CYAN + "\n📨 MANUAL EMAIL CHECK TRIGGERED" + Style.RESET_ALL)
        initial_state = {"emails": []}
        result = workflow.app.invoke(initial_state)
        
        email_stats["total_checks"] += 1
        email_stats["last_check"] = time.strftime('%Y-%m-%d %H:%M:%S')
        
        return {
            "status": "success",
            "message": "Email check completed",
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "statistics": email_stats
        }
    except Exception as e:
        print(Fore.RED + f"❌ Error during email check: {str(e)}" + Style.RESET_ALL)
        raise HTTPException(status_code=500, detail=str(e))

def continuous_email_check():
    """Background task to check emails continuously"""
    global workflow, email_stats, last_check_time
    check_count = 0
    
    while is_running:
        check_count += 1
        last_check_time = time.strftime('%Y-%m-%d %H:%M:%S')
        
        print(Fore.CYAN + f"\n{'='*70}" + Style.RESET_ALL)
        print(Fore.CYAN + f"📨 Automated Check #{check_count} - {last_check_time}" + Style.RESET_ALL)
        print(Fore.CYAN + f"{'='*70}" + Style.RESET_ALL)
        
        try:
            initial_state = {"emails": []}
            result = workflow.app.invoke(initial_state)
            
            email_stats["total_checks"] += 1
            email_stats["last_check"] = last_check_time
            
            print(Fore.GREEN + "✅ Email check completed successfully!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"❌ Error during automated check: {str(e)}" + Style.RESET_ALL)
        
        # Wait 60 seconds before next check
        for i in range(60):
            if not is_running:
                break
            time.sleep(1)

@app.post("/start-automation")
async def start_automation():
    """Start continuous email automation"""
    global is_running
    
    if workflow is None:
        raise HTTPException(status_code=500, detail="Workflow not initialized")
    
    if is_running:
        return {"status": "already_running", "message": "Automation is already running"}
    
    is_running = True
    print(Fore.GREEN + "🚀 Starting continuous email automation..." + Style.RESET_ALL)
    
    # Start automation in background thread
    automation_thread = threading.Thread(target=continuous_email_check, daemon=True)
    automation_thread.start()
    
    return {
        "status": "started",
        "message": "Email automation started",
        "check_interval": "60 seconds",
        "api_url": "http://YOUR_IP:8000",
        "status_url": "http://YOUR_IP:8000/status"
    }

@app.post("/stop-automation")
async def stop_automation():
    """Stop continuous email automation"""
    global is_running
    
    if not is_running:
        return {"status": "not_running", "message": "Automation is not running"}
    
    is_running = False
    print(Fore.YELLOW + "🛑 Stopping email automation..." + Style.RESET_ALL)
    
    return {
        "status": "stopped",
        "message": "Email automation stopped",
        "final_statistics": email_stats
    }

if __name__ == "__main__":
    import uvicorn
    
    print(Fore.GREEN + "=" * 70 + Style.RESET_ALL)
    print(Fore.CYAN + "🚀 ENTERPRISE AI MAILOPS PLATFORM - API SERVER" + Style.RESET_ALL)
    print(Fore.GREEN + "=" * 70 + Style.RESET_ALL)
    print(Fore.YELLOW + f"\n📍 Access the API at:" + Style.RESET_ALL)
    print(Fore.GREEN + f"   http://localhost:8000" + Style.RESET_ALL)
    print(Fore.GREEN + f"   http://127.0.0.1:8000" + Style.RESET_ALL)
    print(Fore.YELLOW + f"\n📚 API Documentation:" + Style.RESET_ALL)
    print(Fore.GREEN + f"   http://localhost:8000/docs (Swagger UI)" + Style.RESET_ALL)
    print(Fore.GREEN + f"   http://localhost:8000/redoc (ReDoc)" + Style.RESET_ALL)
    print()
    
    # Run the server
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
