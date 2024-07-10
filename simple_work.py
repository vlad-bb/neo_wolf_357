import os
import json

FILE_DIR = 'data'
FILE_NAME = 'simpe_txt.txt'
FILE_NAME_JSON = 'simpe_json.json'

FILE_PATH = os.path.join(FILE_DIR, FILE_NAME)
FILE_PATH_JSON = os.path.join(FILE_DIR, FILE_NAME_JSON)

"""
mode
r - read (default)
w - write
a - append


t - text
b - byte

"""

# read mode

# option 1
try:
    file = open(file=FILE_PATH, mode='r', encoding='utf-8')
    file.read()
    file.close()
except FileNotFoundError:
    print(f"{FILE_PATH} not exist")

# option 2
if os.path.exists(FILE_PATH):
    file = open(file=FILE_PATH, mode='r', encoding='utf-8')
    file.read()
    file.close()
else:
    print(f"{FILE_NAME} not exist")

# option 3
if os.path.exists(FILE_PATH):
    with open(file=FILE_PATH, mode='r', encoding='utf-8') as reader:
        text = reader.read()
    print(f"{text=}")


# write mode 1
if not os.path.exists(FILE_DIR):
    os.mkdir(FILE_DIR)
    file = open(file=FILE_PATH, mode='w', encoding='utf-8')
    file.write("First line")
    file.close()

# write mode 2
if not os.path.exists(FILE_DIR):
    os.mkdir(FILE_DIR)
    with open(file=FILE_PATH, mode='w', encoding='utf-8') as writer:
        writer.write("Next line")


# append mode

# option 1
if not os.path.exists(FILE_DIR):
    os.mkdir(FILE_DIR)
file = open(file=FILE_PATH, mode='a', encoding='utf-8')
#chars = file.tell() # повертає позицію курсора
#file.seek(chars)  # встановлює курсор в потрібну позицію
#print(f"{chars=}")
file.write('\n')
file.write("Second line")
file.close()
print("Data appended succesfully")

# option 2
# https://stackoverflow.com/questions/12994442/how-to-append-data-to-a-json-file 
test_dict = {"name": "Олег", "age": 18}

if not os.path.exists(FILE_DIR):
    os.mkdir(FILE_DIR)
with open(file=FILE_PATH_JSON, mode='r+', encoding='utf-8') as file_handler:
    history = json.load(file_handler)
    history.append(test_dict)
    file_handler.seek(0)  # встановлює курсор в потрібну позицію
    json.dump(obj=history, fp=file_handler, indent=2, ensure_ascii=False)

print("Data appended succesfully")




