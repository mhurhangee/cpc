# project/app/utils/env_loader.py
import os
from pathlib import Path
from dotenv import load_dotenv

def load_project_env(env_filename: str = ".env") -> None:
    """
    Load the .env file from the project root into environment variables.
    """
    # Go two levels up: utils/ → app/ → project root
    project_root = Path(__file__).resolve().parents[2]
    env_path = project_root / env_filename
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
    else:
        raise FileNotFoundError(f"No {env_filename} found at {env_path}")