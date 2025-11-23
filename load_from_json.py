import json

def load_trivia_from_json(file_name: str):
    file_location = f"./data/{file_name}"
    try:
        with open(file_location, 'r', encoding='utf-8') as f:
            data = json.load(f)

    except FileNotFoundError:
        print(f"🚫 The file {file_name} is not found. Make sure that provided file is in directory 'data'.")
        raise

    if not isinstance(data, dict):
        raise