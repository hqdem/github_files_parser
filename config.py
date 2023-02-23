from dataclasses import dataclass


@dataclass
class Config:
    github_access_token: str = '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'
    db_uri: str = 'sqlite:///data.db'
