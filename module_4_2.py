b = 800
# a = 2
# c = 12
def test_function(a):
    c = 4 + a
    def inner_function(b):
        b = c * a
        print(b)
        return b

    inner_function(5)
    print(b)
    return c

test_function(3)
print(test_function(6))
# print(inner_function(2))
# print(c)
# print(a)