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

def getSegmentIDs(marked_text:str) -> list[int]:
    """
    Given a marked version of text return the segment IDs.
    A segment corresponds to a sentence in the token.
    Ex: token = "[CLS] a b [SEP] c [SEP] d [SEP]"
    return: [0,0,0,0, 1, 1, 2, 2]
    """
    segment_index = 0
    segment_count = 0
    segment_IDs = []
    eos = False

    for token in marked_text.split(' '):
        segment_count += 1
        if token == "[SEP]": eos = True

        if eos:
            segment_IDs.extend([segment_index] * segment_count)
            eos = not eos
            segment_index += 1
            segment_count = 0
    return segment_IDs
            


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