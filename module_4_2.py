b = 800
def test_function(a):
    def inner_function(b):
        # b = 1
        print(b)
        return b
    c = inner_function(b)
    inner_function(2)
    print(c)
    print(b)
test_function(3)
inner_function(9000) # специальная ошибка для выполнения пункта 4 в задании
