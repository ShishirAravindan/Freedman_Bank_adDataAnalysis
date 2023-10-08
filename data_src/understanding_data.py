import json

def explore_data():
    with open("data_src/db.json", encoding='utf8') as JSONFile:
        data = json.load(JSONFile)
    uniqueValues = set()
    for i in range(len(data)):
        identifiers = set()
        identifiers.add(data[i]["identifier"])
        # print(data[0].keys())
        date = (data[i]["Year"], data[i]["Month"], data[i]["Day"])
        text = data[i]["Text"]
        data_point = (date, text)
        if data_point is not None:
            uniqueValues.add(data_point)

    print(len(uniqueValues))
    print(len(identifiers))

 
    

if __name__ == "__main__":
    explore_data()