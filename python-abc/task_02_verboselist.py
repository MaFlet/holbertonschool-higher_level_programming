class VerboseList(list):
    """Class VerboseList in list class"""
    def append(self, item):
        """Defining append method"""
        super().append(item)
        print(f"Added {[item]} to the list.")


    def extend(self, iterable):
        """Defining extend method"""
        original_length = len(self)
        super().extend(iterable)
        items_added = len(self) - original_length
        print(f"Extended the list with [{items_added}] items.")


    def remove(self, item):
        """Defining remove method"""
        if item in self:
            super().remove(item)
            print(f"Removed [{item}] from the list.")


    def pop(self, index=-1):
        """Defining pop method"""
        if not self:
            raise IndexError("pop from empty list")
        if index < -len(self) or index >= len(self):
            raise IndexError("pop index out of range")
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
