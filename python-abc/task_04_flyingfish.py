class Fish:
    """Defining Fish class"""
    def swim(self):
        """Defining swim method"""
        print("The fish is swimming")

    def habitat(self):
        print("The bird is flying")

class Bird:
    """Defining bird class"""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Defining FlyingFish class with Bird and Fish class"""
    def fly(self):
        print("The flying fish is soaring!")
    def swim(self):
        print("The flying fish is swimming!")
    def habitat(self):
        print("The flying fish lives both in water and the sky!")
