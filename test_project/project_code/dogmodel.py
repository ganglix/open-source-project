from bark import bark_fun as bk

class Dog:
    """creat a dog object
    """
    def __init__(self,dog_type):
        """initialize the dog object

        Parameters
        ----------
        dog_type : string
            any dog type
        """
        self.dog_type = dog_type

    def bark(self):
        """print woof
        Parameters:
        None
        """
        bk()