class Sorter:
    @staticmethod
    def bubble_sort(arr, key=None):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(arr) - 1):
                if key:
                    if key(arr[i]) > key(arr[i + 1]):
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        swapped = True
                else:
                    if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
        return arr



