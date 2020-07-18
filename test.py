print("myname")


class num_class:
    pass

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        try:
            z = x + y
            return z
        except:
            raise NotImplementedError

    def substract(self, x, y):
        try:
            z = x - y
            return z
        except:
            raise NotImplementedError


nums = num_class(4, 7)
sub = nums.substract
add = nums.add

print(sub)
