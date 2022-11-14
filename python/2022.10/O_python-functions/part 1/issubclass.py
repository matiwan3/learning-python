# Is subclass

class A:
    pass

class B:
    pass

class C(A):
    pass

class D(C):
    pass

class E(A,B):
    pass

print(issubclass(C, A))
print(issubclass(D, C))
print(issubclass(D, A))
print(issubclass(E, A))
print(issubclass(E, B))