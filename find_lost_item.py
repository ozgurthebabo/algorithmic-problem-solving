def find_lost_item(item_list, target_item):
    for i in range(len(item_list)):
        if item_list[i] == target_item:
            return i
    return -1
