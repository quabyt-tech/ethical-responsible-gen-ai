import os
import random
import asyncio
from google.genai import Client
from google.genai import types as genai_types
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
INVARIANT_API_KEY = os.getenv("INVARIANT_API_KEY")
INVARIANT_PROJECT_ID = os.getenv("INVARIANT_PROJECT_ID")

client = Client(
    api_key=GEMINI_API_KEY,
    http_options={
        "base_url": f"https://explorer.invariantlabs.ai/api/v1/gateway/{INVARIANT_PROJECT_ID}/gemini",
        "headers": {"Invariant-Authorization": f"Bearer {INVARIANT_API_KEY}"},
    },
)


def main():
    print("Hello from ethical-responsible-gen-ai!")


if __name__ == "__main__":
    main()
