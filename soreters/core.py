from soreters.base import BaseSort


class BubleSort(BaseSort):
    @staticmethod
    def sort(arr, key=None):
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


class InsertionSort(BaseSort):

    @staticmethod
    def sort(arr, key=None):
        for i in range(1, len(arr)):
            insertion_index = InsertionSort.__find_insertion_index(arr, i, key)
            if insertion_index != i:
                InsertionSort.__shift_elements(arr, insertion_index, i)
        return arr

    @staticmethod
    def __find_insertion_index(arr, i, key=None):
        if key:
            value = key(arr[i])
        else:
            value = arr[i]
        for j in range(i - 1, -1, -1):
            if key:
                if key(arr[j]) <= value:
                    return j + 1
            else:
                if arr[j] <= value:
                    return j + 1
        return 0

    @staticmethod
    def __shift_elements(arr, insertion_index, i):
        value = arr[i]
        for j in range(i, insertion_index, -1):
            arr[j] = arr[j - 1]
        arr[insertion_index] = value


class QuickSort(BaseSort):

    @staticmethod
    def sort(arr, start=0, end=None, key=None):
        if end is None:
            end = len(arr) - 1
        if start < end:
            pivot_index = QuickSort.__partition(arr, start, end, key)
            QuickSort.sort(arr, start, pivot_index - 1, key)
            QuickSort.sort(arr, pivot_index + 1, end, key)
        return arr

    @staticmethod
    def __partition(arr, start, end, key=None):
        pivot_value = arr[end] if not key else key(arr[end])
        pivot_index = start
        for i in range(start, end):
            if key:
                if key(arr[i]) <= pivot_value:
                    QuickSort._swap(arr, i, pivot_index)
                    pivot_index += 1
            else:
                if arr[i] <= pivot_value:
                    QuickSort._swap(arr, i, pivot_index)
                    pivot_index += 1
        QuickSort._swap(arr, pivot_index, end)
        return pivot_index


class MergeSort(BaseSort):
    @staticmethod
    def sort(arr, start=0, end=None, buffer=None, key=None):
        if end is None:
            end = len(arr) - 1
        if end <= start:
            return arr
        if not buffer:
            buffer = [None] * len(arr)
        mid = (start + end) // 2
        MergeSort.sort(arr, start, mid, buffer, key)
        MergeSort.sort(arr, mid + 1, end, buffer, key)
        MergeSort.__merge(arr, buffer, start, mid, end, key)
        return arr

    @staticmethod
    def __merge(arr, buffer, start, mid, end, key=None):
        for i in range(start, end + 1):
            buffer[i] = arr[i]
        l = start
        r = mid + 1
        i = start
        while l < mid + 1 and r < end + 1:
            if key:
                if key(buffer[l]) <= key(buffer[r]):
                    arr[i] = buffer[l]
                    l += 1
                else:
                    arr[i] = buffer[r]
                    r += 1
            else:
                if buffer[l] <= buffer[r]:
                    arr[i] = buffer[l]
                    l += 1
                else:
                    arr[i] = buffer[r]
                    r += 1
            i += 1
        while l < mid + 1:
            arr[i] = buffer[l]
            l += 1
            i += 1
        while r < end + 1:
            arr[i] = buffer[r]
            r += 1
            i += 1
