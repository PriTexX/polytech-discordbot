import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")
DSN = os.environ.get("DSN")