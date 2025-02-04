def is_palindrom(s: str) -> bool:
    # print(s)
    sl = s.lower()
    # print (sl)
    slw = sl.replace(' ', '')
    # print(slw)
    slw_reversed = slw[::-1]
    return slw == slw_reversed


def is_palindrom2(s: str) -> bool:
    sl = s.lower()
    # print (sl)
    slw = sl.replace(' ', '')
    x = len(slw)
    x2 = x // 2
    b = 0
    for i in range(0, x2):
        if (slw[i] != slw[x - i - 1]):
            b = b + 1
    return b == 0

if __name__ == '__main__':
    print(is_palindrom2('Able was I ere I saw Elba'))
    print(is_palindrom2('this is now palindrom'))
