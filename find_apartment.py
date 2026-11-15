import math

def find_apartment(door_list, target_door):
    n = len(door_list)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and door_list[min(step, n) - 1] < target_door:
        prev = step
        step += int(math.sqrt(n))

    for i in range(prev, min(step, n)):
        if door_list[i] == target_door:
            return i

    return -1
