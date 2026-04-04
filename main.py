import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types  
from functions.get_files_info import schema_get_files_info, get_files_info

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

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

    available_functions = types.Tool(
    function_declarations=[schema_get_files_info],
    )

    config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config = config,
    )

    if response is None or response.usage_metadata is None:
        print("Error: Response is malformed")
        return

    if verbose_flag:
        print(f"User Prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            
            # Handle function calls
            # Agent can chose to call get_files_info() function
            if function_call_part.name == "get_files_info":
                directory = function_call_part.args.get("directory", ".")
                result = get_files_info(".", directory)
                print(result)
                return 
    
    print(response.text)


if __name__ == "__main__":
    main()
