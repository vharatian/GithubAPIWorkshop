import json
import os

output_folder = "../results"


def create_result_file(file_name):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    return open(f"{output_folder}/{file_name}", 'w')


def write_json_file(file_name, data):
    with create_result_file(file_name) as f:
        f.write(json.dumps(data))

