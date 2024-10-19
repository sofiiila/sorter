class BaseSort:
    @staticmethod
    def sort(arr, key=None):
        raise NotImplementedError("Subclasses should implement this method!")

    @staticmethod
    def _swap(arr, i, j):
        """Utility method to swap elements in an array."""
        arr[i], arr[j] = arr[j], arr[i]
