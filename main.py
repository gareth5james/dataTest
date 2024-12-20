import json

items = []

with open("./data.csv", "r", encoding="utf-8") as data:
    #your code here
    pass
    #end of your code here
    
with open("./output.json", "w") as file:
    var_to_dump = {"items": items}

    json.dump(var_to_dump, file, ensure_ascii=False)