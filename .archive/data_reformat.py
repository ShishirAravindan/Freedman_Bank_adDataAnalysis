import pandas as pd

def generateCSVFile(data):
    data.to_csv('your_file.csv', index=False)

def generateJSONFile(data):
    data.to_json('your_file.json', orient='records')

if __name__ == "__main__":
    data = pd.read_stata("/Users/shishiraravindan/Documents/FSB_coding_files/Freedman_Bank_adDataAnalysis/data_src/db.dta")
    generateCSVFile(data)
    generateJSONFile(data)
