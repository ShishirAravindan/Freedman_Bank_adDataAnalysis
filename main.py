from adSimilarity import *
import pandas as pd
from Scripts import adsApi
def main():
    data=pd.DataFrame(columns=["Identifier","Dictionary1","Dictionary2"])
    ads=adsApi.getAllAdTexts()
    for ad in ads:
        val_1,val_2=adSimilarity(ads[ad])
        new_row={"Identifier":ad,"Dictionary1":val_1,"Dictionary2":val_2}
        data.loc[len(data)]=new_row
        
    data.to_csv("adSimilarity.csv",index=False)
    data.to_json("adSimilarity.json",orient="records",indent=4)
    data.to_excel("adSimilarity.xlsx",index=False)

    
if __name__=="__main__":
    main()
    
    
    
    
        
        


    

