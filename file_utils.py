import os
import json


def read_file(path):
    if os.path.isfile(path):
        with open(path) as json_file:
            data = json.load(json_file)
        
    else:
#         with open(path, 'w') as f: # Doing this because TA code wasn't creating an empty [] in training_losses.txt and val_losses.txt
#             f.write(str([]))  
        
#         with open(path) as json_file:
#             data = json.load(json_file)
#     return data
        raise Exception("file doesn't exist: ", path)
    return data


def read_file_in_dir(root_dir, file_name):
    path = os.path.join(root_dir, file_name)
    return read_file(path)


def write_to_file(path, data):
    with open(path, "w") as outfile:
        json.dump(data, outfile)


def write_to_file_in_dir(root_dir, file_name, data):
    path = os.path.join(root_dir, file_name)
    write_to_file(path, data)


def log_to_file(path, log_str):
    with open(path, 'a') as f:
        f.write(log_str + '\n')


def log_to_file_in_dir(root_dir, file_name, log_str):
    path = os.path.join(root_dir, file_name)
    log_to_file(path, log_str)
