# Freedman Bank: Analyzing advertisement data


NLP project analyzing a comprehensive dataset of bank ads spanning 1865 to 1874 with particular focus on the advertising by the Freedman’s Savings Bank. We measure the persuasion intensity across advertisements.

---
## Requirements
The code in this repository is a combination of python and jupyter notebooks. The packages required to run this repository can be found either in `requirements.txt` or `pyproject.toml`.

---
## Setup
Once you have cloned this repository, you can either use poetry or pip to install the required pacakges in your (virtual) environment.

### Using pip
```bash
pip install -r requirements.txt 
```

### Using poetry
```bash
pip install poetry # if poetry isn't already installed 
poetry install 
```
---

## `dictionaryEmbeddings/dictionaryEmbeddingGeneration.ipynb`
This jupyter notebook handles the workflow of generating embeddings given a excel file of dictionary words/phrases. Upload the file to the `dictionaryEmbeddings` folder.

To run the embedding generation the following parameters can be tweaked:
1. `MODEL_NAME`: By default it is set *distilroberta* but the notebook is setup in a way such that the model is compatible with any model from the [SBERT pre-trained models list](https://www.sbert.net/docs/pretrained_models.html).
2. `DICTIONARY_SRC`: The excel file name (without extension) referring to the dictionary whose embeddings you wish to generate.
3. `TARGET_FILE_NAME`: The name of the file you wish to save the embeddings to. This file name will be required in `inference.ipynb`.

---

## `adEmbeddings/adEmbeddingGeneration.ipynb`
This jupyter notebook handles the workflow of generating embeddings given a excel file of the advertisement database. Upload the excel file to the `data_src` folder.

To run the embedding generation the following parameters can be tweaked:
1. `MODEL_NAME`: By default it is set *distilroberta* but the notebook is setup in a way such that the model is compatible with any model from the [SBERT pre-trained models list](https://www.sbert.net/docs/pretrained_models.html).
2. `IN_FILE`: The excel file name (without extension) referring to the advertisement database excel file whose embeddings you wish to generate.
3. `OUT_FILE`: The name of the file you wish to save the embeddings to. This file name will be required in `inference.ipynb`.

---

## `inference.ipynb`
Assuming you have already generated and serialized the advertisements and dictionary embeddings, this jupyter notebook handles the workflow of computing cosine similarity values and saving them to a file under `similarityValues`.

To run the embedding generation the following parameters can be tweaked:
1. `AD_EMBEDDINGS_FILE`: Refers to the ad embeddings file whose  cosine similarity is computed. Typically will be the version of `OUT_FILE` from `adEmbeddings/adEmbeddingGeneration.ipynb.`
2. `DICTIONARY_EMBEDDINGS_FILE`: Refers to the dictionary embeddings file whose  cosine similarity is computed. Typically will be the version of `TARGET_FILE_NAME` from `dictionaryEmbeddings/dictionaryEmbeddingGeneration.ipynb`.
3. `OUT_FILE`: The name of the file you wish to save the similarity values to. 
