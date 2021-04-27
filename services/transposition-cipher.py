from math import ceil


def encode(secret: str, text: str):
    width = len(secret)
    height = ceil(len(text)/width)
    length = width * height
    text = text.ljust(length)
    s = []
    u = []

    for index, letter in enumerate(secret):
        s.append([index, ord(letter)])
        u.append([0 for row in range(height)])

    for i in range(width):
        for j in range(height):
            u[i][j] = text[(j * width) + i]

    s.sort(key=lambda item: item[1])

    result = ''

    for i in range(width):
        idx = s[i][0]
        for j in range(height):
            result += u[idx][j]
            idx = idx - 1 + width if idx == 0 else idx - 1

    return result


def decode(secret: str, text: str):
    width = len(secret)
    height = ceil(len(text) / width)
    length = width * height
    text = text.ljust(length)
    s = []
    u = []

    for index, letter in enumerate(secret):
        s.append([index, ord(letter)])
        u.append([0 for row in range(height)])

    s.sort(key=lambda item: item[1])

    for i in range(width):
        idx = s[i][0]
        for j in range(height):
            u[idx][j] = text[0]
            text = text[1:]
            idx = idx - 1 + width if idx == 0 else idx - 1

    result = ''

    for i in range(height):
        for j in range(width):
            try:
                result += u[j][i]
            except IndexError:
                pass

    return result
