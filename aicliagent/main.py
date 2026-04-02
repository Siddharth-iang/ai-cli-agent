import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types  

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if api_key is None:
        raise ValueError("GEMINI_API_KEY not found in .env file")

    if len(sys.argv) < 2:
        print("I need a prompt")
        sys.exit(1)
    verbose_flag = False
    if len(sys.argv) ==3 and sys.argv[2] == "--verbose":
        verbose_flag = True
    prompt = sys.argv[1]

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
    )

    if response is None or response.usage_metadata is None:
        print("Error: Response is malformed")
        return

    if verbose_flag:
        print(f"User Prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



if __name__ == "__main__":
    main()


