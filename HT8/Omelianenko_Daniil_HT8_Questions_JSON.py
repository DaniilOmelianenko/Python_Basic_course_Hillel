import json

with open("questions.json", "r") as file:
    data = json.load(file)

for value_1st in data.values():
    for value_2nd in value_1st:
        list_key_value2 = list(value_2nd.keys())
        print(value_2nd[list_key_value2[0]])
        value_2nd[list_key_value2[1]] = input(f"{list_key_value2[1]}: ")

with open("questions.json", "w+") as file:
    file.write(json.dumps(data))