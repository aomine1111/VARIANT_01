def merge_sort(arr):
    """
    Функция сортировки слиянием (Merge Sort).
    Рекурсивно делит список на две части, сортирует их и сливает обратно.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Слияние двух отсортированных половин
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Если остались элементы в left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Если остались элементы в right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

if __name__ == '__main__':
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный список:", sample_list)
    sorted_list = merge_sort(sample_list.copy())
    print("Отсортированный список:", sorted_list)
