import json

def explore_data():
    with open("data_src/db.json", encoding='utf8') as JSONFile:
        data = json.load(JSONFile)
    uniqueValues = set()
    for i in range(len(data)):
        date = (data[i]["Year"], data[i]["Month"], data[i]["Day"])
        text = data[i]["Text"]
        data_point = (date, text)
        if data_point is not None:
            uniqueValues.add(data_point)

    print(len(uniqueValues))


if __name__ == "__main__":
    explore_data()