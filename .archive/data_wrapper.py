class Tokenized:
    def __init__(self, text: list[str]=None, index: list[int]=None, segments: list[int]=None) -> None:
        self.text = text
        self.index = index
        self.segments = segments