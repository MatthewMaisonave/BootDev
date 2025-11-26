import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_name = function_call_part.name
    chosen_function = function_map.get(function_name)
    if chosen_function is None:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    args = dict(function_call_part.args)
    args['working_directory'] = "./calculator"
    function_result = chosen_function(**args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
         

def main():
    print("Hello from agent!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    model_name = "gemini-2.0-flash-001"

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )
    
    if len(sys.argv) > 1:
        user_prompt = sys.argv[1]
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
        for i in range(20):
            lst = []
            response = client.models.generate_content(
                model=model_name,
                contents=messages,
                config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
            )
            for candidate in response.candidates:
                messages.append(candidate.content)

            if response.function_calls is not None:
                for function_call_part in response.function_calls:
                    function_call_result = call_function(function_call_part, verbose="--verbose" in sys.argv)
                    if function_call_result.parts[0].function_response.response is None:
                        raise Exception("Fatal Error")
                    elif function_call_result.parts[0].function_response.response is not None:
                        lst.append(function_call_result.parts[0])
                    if "--verbose" in sys.argv:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
            else:
                if response.text is not None:
                    print(response.text)
                    break
            messages.append(types.Content(role="user", parts=lst))
            
    else:
        print("Error: No CLI prompt provided") 
        sys.exit(1)


if __name__ == "__main__":
    main()
