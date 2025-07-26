import urllib.parse
import secrets

from state_storage import state_storage
from config import settings


def generate_google_oauth_redirect_uri():
    random_state = secrets.token_urlsafe(16)
    state_storage.add(random_state)

    query_params = {
        "client_id": settings.OUATH_GOOGLE_CLIENT_ID,
        "redirect_uri": "http://localhost:3000/auth/google",
        "response_type": "code",
        "scope": " ".join([
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/calendar",
            "openid",
            "profile",
            "email",
        ]),
        "access_type": "offline",
        "state": random_state,
    }

    query_string = urllib.parse.urlencode(query_params, quote_via=urllib.parse.quote)
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    return f"{base_url}?{query_string}"
