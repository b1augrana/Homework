import os
from pprint import pprint


FILE_DIR = "files"
ROOT_PATH = os.getcwd()
file_path = os.path.join(ROOT_PATH, FILE_DIR)
files = os.listdir(file_path)


files_dict = {}
for file in files:
    filename = os.path.join(file_path, file)
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
        text = []
        text_len = len(lines)
        for line in lines:
            text.append(line.strip())
        files_dict[file] = (text_len, text)    

sorted_values = sorted(files_dict.values())   
sorted_dict = {}

for val in sorted_values:
    for k in files_dict.keys():
        if files_dict[k] == val:
            sorted_dict[k] = files_dict[k]     
            break
        
with open("sorted_text.txt", "w", encoding="utf-8") as file_object:
    for key, value in sorted_dict.items():
        file_object.write(f"{key}\n")     
        file_object.write(f"{value[0]}\n")  
        for val in value[1]:
            file_object.write(f"{val}\n")   
            
            