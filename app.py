import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def application(environ, start_response):
    """
    Pure WSGI application (no frameworks).
    """
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    env_mode = os.getenv("APP_ENV", "development")
    secret = os.getenv("SECRET_KEY", "defaultsecret")

    body = f"Hello, WSGI World!<br>Env: {env_mode}<br>Secret: {secret}"
    return [body.encode("utf-8")]
