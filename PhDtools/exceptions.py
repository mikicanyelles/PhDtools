class NotDNASequenceError(Exception):
    """
        Raised when a DNA sequence contains any value different from A, C, G, T.
    """
    def __init__(self):
        print("DNA sequence is not correct, it contains other value than A, C, G, T")
        pass
