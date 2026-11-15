def search_book_isbn(isbn_list, target_isbn):
    left = 0
    right = len(isbn_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if isbn_list[mid] == target_isbn:
            return mid
        elif isbn_list[mid] < target_isbn:
            left = mid + 1
        else:
            right = mid - 1

    return -1
