from fastapi_users.authentication.transport import BearerTransport
from core.config import settings


bearer_transport = BearerTransport(tokenUrl=settings.api.bearer_token_to_url)
