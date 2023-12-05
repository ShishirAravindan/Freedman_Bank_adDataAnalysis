import sys
sys.path.append('..')
from transformers import AutoTokenizer
from transformers import TFAutoModelForSequenceClassification
import tensorflow as tf
from textblob import TextBlob
from Scripts.adsApi import *
import pandas as pd
# twitter model
MODEL = "cardiffnlp/twitter-roberta-base-sentiment"

# tokenizing based on the model
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)


class SentimentAnalysis:
    def __init__(self, text):
        self.text = text

    """
    This function will use the vader model to analyze the sentiment of the text
    This is more of a basic or naive approach to sentiment analysis as it 
    checks for the polarity of each word in the text and then gives the
    sentiment of the text based on average of the polarity of each word.
    """
    def vaderModel(self):
        textblob = TextBlob(self.text)
        return textblob.sentiment.polarity

    """
    This function will use the roBERTa model to analyze the sentiment of the text.
    This is a more advanced approach to sentiment analysis as it uses a deep learning
    model to analyze the sentiment of the text.
    As shown in the code above, the roBERTa model is using a pre-trained model
    of 500 million twitter posts to analyze the sentiment of the text.
    """
    def roBERTaModel(self):
        encoded_text = tokenizer(self.text, return_tensors='tf')
        output = model(**encoded_text)
        scores = output[0][0].numpy()
        scores = tf.nn.softmax(scores)
        scores_dict = {
            'roberta_neg' : scores[0].numpy(),
            'roberta_neu' : scores[1].numpy(),
            'roberta_pos' : scores[2].numpy()
        }
        return scores_dict

    def roBERTaModelResult(self):
        result = self.roBERTaModel()
        return result['roberta_neg'] * -1 + result['roberta_neu'] * 0 + result['roberta_pos'] * 1

    """
    This function will return the sentiment of the text.
    If the roBERTa model is able to analyze the sentiment of the text, then
    the sentiment of the text will be returned. Otherwise, the vader model
    will be used to analyze the sentiment of the text.
    
    :return: sentiment of the text
    """
    def getValues(self):
        value = 0
        try:
            value = self.roBERTaModelResult()
        except:
            value = self.vaderModel()
        return value

# sea = SentimentAnalysis("you are very very very very bad")
# print(sea.roBERTaModelResult())
# print(sea.vaderModel())
def getSentimentVals(filename:str)->dict:
    identifier_text_map=getAllAdTexts(filename)
    identifier_sentimentval_map={}
    for identifier in identifier_text_map:
        text=identifier_text_map[identifier]
        result=[]
        if identifier not in identifier_sentimentval_map:
            identifier_sentimentval_map[identifier]=result
        sav=SentimentAnalysis(text)
        roberta_result=sav.roBERTaModelResult()
        vader_result=sav.vaderModel()
        identifier_sentimentval_map[identifier].append(roberta_result)
        identifier_sentimentval_map[identifier].append(vader_result)
        print(f"Identifier: {identifier}, Vals:{identifier_sentimentval_map[identifier]} done")
    return identifier_sentimentval_map

def converttoExcel(dictionary:dict,filename:str):
    column_names=['Identifier','roBERTa','Vader']
    df=pd.DataFrame(columns=column_names)
    for identifier in dictionary:
        new_row={'Identifier':identifier,'roBERTa':dictionary[identifier][0],'Vader':dictionary[identifier][1]}
        df.loc[len(df)]=new_row
    df.to_excel(f"sentimentValues/{filename}.xlsx",index=False)
    
if __name__ == "__main__":
    identifier_sentimentval_map=getSentimentVals("dataset_nov23")
    converttoExcel(identifier_sentimentval_map,"SentimentVal_dataset_nov23")
    print("Done")
        
            
        
        
        
    
    
    
