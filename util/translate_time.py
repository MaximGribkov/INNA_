def translate_to_second(h, m, s):
    return h * 3600 + m * 60 + s


def translate_to_ms(h, m, s):
    return h * 3600000 + m * 60000 + s * 1000


# print(translate_to_second(1, 1, 0))
# print(translate_to_ms(h=1, m=3, s=25))