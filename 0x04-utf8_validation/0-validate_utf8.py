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

    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False

        number_bytes -= 1

    return number_bytes == 0


if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))

    data2 = [80, 121, 116, 104, 111, 110, 32, 105,
             115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))
