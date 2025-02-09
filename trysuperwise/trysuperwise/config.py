import os
from dotenv import load_dotenv

load_dotenv()

APPROVAL_TIMEOUT_DURATION_SECONDS=100 
BACKEND_URL='https://api.trysuperwise.com'
SUPERWISE_PROJECT_ID=os.getenv('SUPERWISE_PROJECT_ID')
SUPERWISE_API_KEY=os.getenv('SUPERWISE_API_KEY')