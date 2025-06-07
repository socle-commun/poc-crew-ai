from typing import Optional
from pydantic import BaseModel

class GitHubConfig(BaseModel):
    """Configuration pour la connexion GitHub."""
    organization: str
    token: Optional[str] = None
    base_url: str = "https://api.github.com"
    
    class Config:
        env_prefix = "GITHUB_" 