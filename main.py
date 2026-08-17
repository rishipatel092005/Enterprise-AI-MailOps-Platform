"""
🚀 Enterprise AI MailOps Platform - Main Entry Point
Continuous Email Automation Workflow
"""

import time
import sys
from pathlib import Path
from dotenv import load_dotenv
from colorama import Fore, Style, init

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

from src.graph import Workflow

# Initialize colorama for colored terminal output
init(autoreset=True)

def main():
    """Main function to run the email automation workflow continuously."""
    
    print(Fore.CYAN + "=" * 70 + Style.RESET_ALL)
    print(Fore.GREEN + "🚀 ENTERPRISE AI MAILOPS PLATFORM" + Style.RESET_ALL)
    print(Fore.CYAN + "=" * 70 + Style.RESET_ALL)
    print()
    
    try:
        # Initialize the workflow
        print(Fore.YELLOW + "⏳ Initializing workflow..." + Style.RESET_ALL)
        workflow = Workflow()
        print(Fore.GREEN + "✅ Workflow initialized successfully!" + Style.RESET_ALL)
        print()
        
        # Run the workflow continuously
        print(Fore.CYAN + "📧 Starting email automation agent..." + Style.RESET_ALL)
        print(Fore.YELLOW + "Agent will check emails every 60 seconds" + Style.RESET_ALL)
        print(Fore.YELLOW + "Press Ctrl+C to stop the agent" + Style.RESET_ALL)
        print()
        
        check_count = 0
        while True:
            check_count += 1
            print(Fore.CYAN + f"\n{'='*70}" + Style.RESET_ALL)
            print(Fore.CYAN + f"📨 Email Check #{check_count} - {time.strftime('%Y-%m-%d %H:%M:%S')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"{'='*70}" + Style.RESET_ALL)
            
            try:
                # Run the workflow with initial state
                initial_state = {"emails": []}
                result = workflow.app.invoke(initial_state)
                print(Fore.GREEN + "✅ Email check completed successfully!" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"❌ Error during workflow execution: {str(e)}" + Style.RESET_ALL)
            
            # Wait 60 seconds before next check
            print(Fore.YELLOW + "\n⏳ Waiting 60 seconds before next email check..." + Style.RESET_ALL)
            time.sleep(60)
            
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\n🛑 Agent stopped by user" + Style.RESET_ALL)
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"❌ Fatal error: {str(e)}" + Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    main()
