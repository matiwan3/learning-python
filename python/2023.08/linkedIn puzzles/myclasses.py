my_array = [1,2,3,4,5]
suma = 0
for x in range(len(my_array)): # first loop
    for y in my_array:
        # print(y)
        suma += y # then sum
print(suma)


class Book:
    def __init__(self, BookType, name):
        self.BookType = BookType
              
    def name(self,name):
        self.name = name
        
Book.name = "Magic Tree"
print(Book.name)

class triangle90:
    def __init__(self,a,b,c):
        if a + b >= c:
            raise Exception("cannot initialize 90triangle. Wrong measurements")
        else:
            self.a = a
            self.b = b
            self.c = c
      
    def perimeter(self):
        return self.a+self.b+self.c
    
    def area(self):
        return round(float((((self.a)+(self.b))*(self.c))/2),3)
    
    def LongestSide(self):
        return max(self.a,self.b,self.c)
    
print(triangle90(3,4,8).perimeter())
print(triangle90(3,2,7).area())
print(triangle90(4,4,15).LongestSide())



