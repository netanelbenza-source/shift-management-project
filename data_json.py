import json 
try:
    with open(r"C:\X\e\hanged_man\project1\__pycache__\data.json","r",encoding="utf-8")as file:
        the_data_of_solder = json.load(file)
except FileNotFoundError,json.JSONDecodeError:
     the_data_of_solder = []