from dataclasses import dataclass


@dataclass
class Config:
    github_access_token: str = 'token here'
    db_uri: str = 'sqlite:///data.db'
