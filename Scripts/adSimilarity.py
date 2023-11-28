#!/usr/bin/env python
# coding: utf-8

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

def getDictionaryColumns(dictionaryFileName: str):
    DictionaryEmbeddingsFile = os.path.join(os.getcwd(), f"dictionaryEmbeddings/{dictionaryFileName}.pkl")
    
    with open(DictionaryEmbeddingsFile, "rb") as f:
        deserializedDictEmbeddings = pickle.load(f)
        column_names=['Identifier']+list(deserializedDictEmbeddings.keys())
        return column_names

def getCosineSimilarity(mean_pooled, dictionaryFileName: str):
    DictionaryEmbeddingsFile = os.path.join(os.getcwd(), f"dictionaryEmbeddings/{dictionaryFileName}.pkl")
    if isinstance(mean_pooled,tuple):
        mean_pooled=np.array(mean_pooled)
    mean_pooled=mean_pooled.flatten()[:768].reshape(1,-1)
    # Building NP-array of Dictionary embeddings
    with open(DictionaryEmbeddingsFile, "rb") as f:
        deserializedDictEmbeddings = pickle.load(f)
        output=[]
        for dictionary in deserializedDictEmbeddings:
            cosine_similarity_list=[]
            dict_mean_pooled=deserializedDictEmbeddings[dictionary].flatten()
            dict_mean_pooled=dict_mean_pooled.reshape(1,-1)
            for sentence in mean_pooled:
                try:
                 cosine_similarity_list.append(cosine_similarity([sentence],dict_mean_pooled))
                except:
                    return [-1]*len(deserializedDictEmbeddings)
            output.append(np.amax(cosine_similarity_list))
    return output