#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """

    num_bytes = 0

    for num in data:
        if 128 <= num <= 191:
            if num_bytes == 0:
                return False
            num_bytes -= 1
        else:
            if num_bytes == 0:
                if 192 <= num <= 223:
                    num_bytes = 1
                elif 224 <= num <= 239:
                    num_bytes = 2
                elif 240 <= num <= 247:
                    num_bytes = 3
                elif num >= 248:
                    return False
            else:
                return False

    return num_bytes == 0


if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105,
             115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False
