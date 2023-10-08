from Scripts import adsApi
def getMarkedAdText(text:str)-> str:
    """
    Returns the Marked version of the Ad Text/ 
    E.g : ad = A.B.C
    return "[CLS] A [SEP] B [SEP] C [SEP]"
    """
    list_sentences= text.split('.')
    list_sentences.pop()
    sentence_container = ""
    for sentence in list_sentences:
        sentence_container+=sentence+ " [SEP]"
    return ("[CLS] "+sentence_container)

def main():
    """
    Returns a map with identifier as key and the marked ad text as values.
    """
    identifier_markedtext_map={}
    result = adsApi.getAllAdTexts()
    for ads in result:
        marked_text = getMarkedAdText(result[ads])
        identifier_markedtext_map[ads] = marked_text
    return identifier_markedtext_map

    
    