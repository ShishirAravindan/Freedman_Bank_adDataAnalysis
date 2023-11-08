#!/usr/bin/env python
# coding: utf-8


# get_ipython().run_line_magic('pip', 'install transformers')

import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def getMeanPooledEmbedding(ad_sentence:str):
    MODEL_NAME = "sentence-transformers/bert-base-nli-mean-tokens"
    
    # pre-processing data
    sentences = ad_sentence.split(".")[:-1]
    sentences = [sentence.strip() for sentence in sentences]
    
    # Setting up environment variables 
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModel.from_pretrained(MODEL_NAME)
    tokens = {'input_ids': [], 'attention_mask': []}
    
    # Generating encodings
    for sentence in sentences:
        new_tokens = tokenizer.encode_plus(sentence, max_length=128, truncation=True, padding='max_length', return_tensors='pt')
        tokens['input_ids'].append(new_tokens['input_ids'][0])
        tokens['attention_mask'].append(new_tokens['attention_mask'][0])
    
    if len(tokens['input_ids']) == 0:
        return (-1,-1)
    
    # Vectorization
    tokens['input_ids'] = torch.stack(tokens['input_ids'])
    tokens['attention_mask'] = torch.stack(tokens['attention_mask'])

    # Creating embeddings
    outputs = model(**tokens)
    embeddings = outputs.last_hidden_state

    attention = tokens['attention_mask']
    mask = attention.unsqueeze(-1).expand(embeddings.shape).float()
    mask_embeddings = embeddings * mask

    summed = torch.sum(mask_embeddings, 1)
    counts = torch.clamp(mask.sum(1), min=1e-9)
    mean_pooled = summed / counts
    mean_pooled = mean_pooled.detach().numpy()
    return mean_pooled
    
def adSimilarity(ad_sentence:str):
    mean_pooled=getMeanPooledEmbedding(ad_sentence)
    return getCosineSimilarity(mean_pooled)

def getCosineSimilarity(mean_pooled):
    # Building NP-array of Dictionary embeddings
    with open("dictionaryEmbeddings/serializedDictionaryEmbeddings_unified.pkl", "rb") as f:
        deserializedDictEmbeddings = pickle.load(f)
        output=[]
        for dictionary in deserializedDictEmbeddings:
            cosine_similarity_list=[]
            dict_mean_pooled=deserializedDictEmbeddings[dictionary]
            
            for sentence in mean_pooled:
                try:
                    cosine_similarity_list.append(cosine_similarity([sentence],dict_mean_pooled))
                except:
                    return [-1]*len(deserializedDictEmbeddings)
            output.append(np.amax(cosine_similarity_list))
    return output

def getDictionaryColumns():
    with open("dictionaryEmbeddings/serializedDictionaryEmbeddings_unified.pkl", "rb") as f:
        deserializedDictEmbeddings = pickle.load(f)
        column_names=['Identifier']+list(deserializedDictEmbeddings.keys())
        return column_names
        
#getDictionaryColumns()
            


    # dict_a=np.load("./staticEmbeddings/oldDictionaryEmbeddings/prescriptive_stereotypes_embeddings.npy")
    # dict_b=np.load("./staticEmbeddings/oldDictionaryEmbeddings/false_claims_safety_embeddings.npy")
    # cosine_similarity_list_a=[]
    # cosine_similarity_list_b=[]
    # for sentence in mean_pooled:
    # #Call the file with the dictionary to compare the cosine similarity
    #     cosine_similarity_list_a.append(cosine_similarity([sentence],dict_a))
    #     cosine_similarity_list_b.append(cosine_similarity([sentence],dict_b))
    # return (np.amax(cosine_similarity_list_a),np.amax(cosine_similarity_list_b))
#print(adSimilarity("the fsb. a national savings bank. established march, 1865. chartered by the government of the united states. banking house 1507 pennsylvania avenue, opposite the treasury. deposits of five cents or any larger amounts received. six per cent interest paid on sums of five dollars or more. all deposits payable on demand, with interest due. all accounts strictly private and confidential. principal office, washington, d. c. branch offices in all the larger cities of the south and southwest. this great national savings institution, established by the authority of the united states government for the benefit of the freedmen, knows no distinction of race or color, and offers its great advantages to all classes alike. save the small sums. cut off your vices - don't smoke - don't drink - don't buy lottery tickets. put the money you save into the fsb. open from 9 a. m. to  4 p. m. each day, and on wednesday and saturday nights, to receive deposits only, from 6 1\/2 to 8 o'clock."))





