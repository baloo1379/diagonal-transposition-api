from math import ceil


async def encode(secret: str, text: str) -> str:
    width: int = len(secret)
    height: int = ceil(len(text)/width)
    length: int = width * height
    text: str = text.ljust(length)
    s: list = []
    u: list = []

    for index, letter in enumerate(secret):
        s.append([index, ord(letter)])
        u.append([0 for row in range(height)])

    for i in range(width):
        for j in range(height):
            u[i][j] = text[(j * width) + i]

    s.sort(key=lambda item: item[1])

    result: str = ''

    for i in range(width):
        idx: int = s[i][0]
        for j in range(height):
            result += u[idx][j]
            idx = idx - 1 + width if idx == 0 else idx - 1

    return result


async def decode(secret: str, text: str) -> str:
    width: int = len(secret)
    height: int = ceil(len(text)/width)
    length: int = width * height
    text: str = text.ljust(length)
    s: list = []
    u: list = []

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

    result: str = ''

    for i in range(height):
        for j in range(width):
            try:
                result += u[j][i]
            except IndexError:
                pass

    return result
