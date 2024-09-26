class CountedIterator:
    """Defining CountedIterator class"""
    def __init__(self, iterable):
        """Initializing 2 attributes: iter and counter"""
        self.iterator = iter(iterable)
        self.count = 0


    def __iter__(self):
        return self


    def get_count(self):
        """Defining get_count method"""
        return self.count


    def __next__(self):
        """Defining remove method"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
