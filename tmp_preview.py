from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path('.env'))
from src.agents import Agents

email = "Hi, I am interested in your AI agent platform. Could you please share your pricing plans, key features, and support response time? I want to understand how your solution can help my customer support team."

agents = Agents()
cat = agents.categorize_email.invoke({'email': email})
print('CATEGORY:', cat.category.value)
writer = agents.email_writer.invoke({
    'email_information': f'# **EMAIL CATEGORY:** {cat.category.value}\n\n# **EMAIL CONTENT:**\n{email}\n\n# **INFORMATION:**\n',
    'history': []
})
print('DRAFT:\n')
print(writer.email)
