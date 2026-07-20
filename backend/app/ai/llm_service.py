from app.ai.groq_client import client
from app.core.config import settings
import json, re

from app.ai.prompts import (
    SUMMARIZE_INTERACTION_PROMPT,
    EXTRACT_INTERACTION_PROMPT,
    INTENT_DETECTION_PROMPT
)


def generate_response(
    user_prompt: str,
    system_prompt: str | None = None,
    temperature: float = 0.3
) -> str:
    """
    Generate a response from the Groq LLM.

    Args:
        user_prompt: The user's input.
        system_prompt: Optional system instructions.
        temperature: Optional model temperature

    Returns:
        The generated response text.
    """

    messages = []

    if system_prompt:
        messages.append(
            {
                "role": "system",
                "content": system_prompt
            }
        )

    messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    response = client.chat.completions.create(
        model=settings.GROQ_MODEL,
        messages=messages,
        temperature=temperature,
    )

    return response.choices[0].message.content


def generate_summary(conversation: str) -> str:
    """
    Generate a concise CRM-friendly summary of an HCP interaction.
    """

    response = generate_response(conversation, system_prompt= SUMMARIZE_INTERACTION_PROMPT, temperature=0.2)

    return response



def extract_interaction_details(conversation: str) -> dict:
    print(" Extracting interaction details")
    response = generate_response(
        conversation,
        system_prompt=EXTRACT_INTERACTION_PROMPT,
        temperature=0.0
    )
    print("got res from llm ", response)
    cleaned = response.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\n|\n```$", "", cleaned).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"Failed to parse CRM extraction response: {e}\nRaw: {response!r}")
        raise

def detect_intent(user_input: str) -> str:
    """
    Detect the user's intent using the LLM.
    """

    intent = generate_response(
        user_prompt=user_input,
        system_prompt=INTENT_DETECTION_PROMPT,
        temperature=0
    )

    return intent.strip().upper()

if __name__ == "__main__":
    res = generate_response("Ramayan")
    print(res)