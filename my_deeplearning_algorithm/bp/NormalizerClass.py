from functools import reduce
class Normalizer(object):
    def __init__(self):
        self.mask = [
            0x1, 0x2, 0x4, 0x8, 0x10, 0x20, 0x40, 0x80
        ]

    def norm(self, number):
        return map(lambda m: 0.9 if number & m else 0.1, self.mask)

    def denorm(self, vec):
        binary = map(lambda i: 1 if i > 0.5 else 0, vec)
        list_binary = list(binary)
        list_mask = list(self.mask)
        for i in range(len(list_mask)):
            list_binary[i] = list_binary[i] * list_mask[i]
        return reduce(lambda x, y: x + y, list_binary)

