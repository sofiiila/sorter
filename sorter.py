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

    @staticmethod
    def insertion_sort(arr, key=None):
        for i in range(1, len(arr)):
            insertion_index = Sorter.__find_insertion_index(arr, i, key)
            if insertion_index != i:
                Sorter.__shift_elements(arr, insertion_index, i)
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

    @staticmethod
    def quick_sort(arr, start=0, end=None, key=None):
        if end is None:
            end = len(arr) - 1
        if start < end:
            pivot_index = Sorter.__partition(arr, start, end, key)
            Sorter.quick_sort(arr, start, pivot_index - 1, key)
            Sorter.quick_sort(arr, pivot_index + 1, end, key)
        return arr

    @staticmethod
    def __partition(arr, start, end, key=None):
        pivot_value = arr[end] if not key else key(arr[end])

        pivot_index = start

        for i in range(start, end):
            if key:
                if key(arr[i]) <= pivot_value:
                    Sorter.__swap(arr, i, pivot_index)
                    pivot_index += 1
            else:
                if arr[i] <= pivot_value:
                    Sorter.__swap(arr, i, pivot_index)
                    pivot_index += 1

        Sorter.__swap(arr, pivot_index, end)

        return pivot_index

    @staticmethod
    def __swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def merge_sort(arr, start=0, end=None, buffer=None, key=None):
        if end is None:
            end = len(arr) - 1
        if end <= start:
            return arr

        if not buffer:
            buffer = [None] * len(arr)

        mid = (start + end) // 2

        Sorter.merge_sort(arr, start, mid, buffer, key)
        Sorter.merge_sort(arr, mid + 1, end, buffer, key)

        Sorter.__merge(arr, buffer, start, mid, end, key)

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

