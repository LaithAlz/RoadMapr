import os
from dotenv import load_dotenv

load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
COHERE_API_URL = 'https://api.cohere.ai/v1/generate'


SUPABASE_URL = 'https://voenczphlgojgihwbcwi.supabase.co'
SUPABASE_KEY = os.getenv('SUPABASE_KEY')


LINKEDIN_CLIENT_ID = os.getenv('LINKEDIN_CLIENT_ID')
LINKEDIN_CLIENT_SECRET = os.getenv('LINKEDIN_CLIENT_SECRET')
REDIRECT_URI = 'http%3A%2F%2F127.0.0.1%3A5000%2Flinkedin-openid%2Fcallback'
BACKEND_REDIRECT_URI = 'http://127.0.0.1:5000/linkedin-openid/callback'
FRONTEND_REDIRECT_URI = 'http://localhost:3000/resumeupload'