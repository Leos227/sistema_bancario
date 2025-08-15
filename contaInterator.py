class ContaIterator:
    def __init__(self, extrato):
        self._extrato = extrato
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._extrato):
            item = self._extrato[self._index]
            self._index += 1
            return item
        raise StopIteration
