import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    parent_dir = os.path.dirname(abs_file_path)
    try:
        os.makedirs(parent_dir, exist_ok=True)
    except Exception as e:
        return f"Could not create directory {parent_dir}: {str(e)}"

    try:
        with open(abs_file_path, 'w') as f:
            f.write(content)
            return(f"File wrote to {file_path} ({len(content)} characters)")
    except Exception as e:
        return f"Failed to write to file: {file_path}, {e}"