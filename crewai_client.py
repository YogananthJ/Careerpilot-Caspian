import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

CREWAI_API_URL = os.getenv("CREWAI_API_URL")
CREWAI_BEARER_TOKEN = os.getenv("CREWAI_BEARER_TOKEN")


def ask_careerpilot(user_message: str) -> str:

    headers = {
        "Authorization": f"Bearer {CREWAI_BEARER_TOKEN}",
        "Content-Type": "application/json",
    }

    # Start CrewAI execution
    kickoff_response = requests.post(
        f"{CREWAI_API_URL}/kickoff",
        headers=headers,
        json={
            "inputs": {
                "user_message": user_message
            }
        },
        timeout=30,
    )

    kickoff_response.raise_for_status()

    kickoff_data = kickoff_response.json()

    kickoff_id = kickoff_data["kickoff_id"]

    print(f"✓ CrewAI started: {kickoff_id}")

    # Wait for CrewAI result
    for _ in range(30):

        status_response = requests.get(
            f"{CREWAI_API_URL}/status/{kickoff_id}",
            headers=headers,
            timeout=30,
        )

        status_response.raise_for_status()

        data = status_response.json()

        state = data.get("state")

        print(f"→ CrewAI status: {state}")

        if state == "SUCCESS":

            result = data.get("result", {})

            return result.get(
                "raw",
                "CareerPilot completed but returned no text."
            )

        if state in ["FAILURE", "FAILED"]:
            raise RuntimeError(
                f"CrewAI execution failed: {data}"
            )

        time.sleep(2)

    raise TimeoutError(
        "CareerPilot took too long to respond."
    )