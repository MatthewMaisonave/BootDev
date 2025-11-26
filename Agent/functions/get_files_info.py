import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_working = os.path.abspath(working_directory)
    abs_target = os.path.abspath(full_path)

    if not abs_target.startswith(abs_working):
        return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_target):
        return f'    Error: "{directory}" is not a directory'
    file_list = os.listdir(abs_target)
    output = []
    for name in file_list:
        entry_path = os.path.join(abs_target, name)
        # use entry_path for size and is_dir
        size = os.path.getsize(entry_path)
        is_dir = os.path.isdir(entry_path)
        output.append(f" - {name}: file_size={size} bytes, is_dir={is_dir}")
    return "\n".join(output)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)