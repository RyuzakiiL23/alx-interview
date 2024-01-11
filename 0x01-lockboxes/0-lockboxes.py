#!/usr/bin/python3
'''LockBoxes interview'''


def canUnlockAll(boxes):
    '''Determinate if all boxes are openable'''
    if not boxes:
        return False

    keys = set([0])
    opened = set()

    while keys:
        current_key = keys.pop()
        opened.add(current_key)

        for key in boxes[current_key]:
            if key < len(boxes) and key not in opened:
                keys.add(key)

    return len(opened) == len(boxes)


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))
