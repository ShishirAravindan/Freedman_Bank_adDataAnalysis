import pandas as pd

def generateCSVFile(data):
    data.to_csv('dataset_oct23.csv', index=False)

def generateJSONFile(data):
    data.to_json('dataset_oct23.json', orient='records')

if __name__ == "__main__":
    data = pd.read_stata("../data_src/dataset_v2.dta")
    generateCSVFile(data)
    generateJSONFile(data)
