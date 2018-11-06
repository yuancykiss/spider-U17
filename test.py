class Asc():
    pass

class Bsc():
    pass

a = Asc()
b = Bsc()

print(str(type(a))[-5:-2])
print(str(type(b)))
print(isinstance(a, Asc))
print(isinstance(b, Asc))