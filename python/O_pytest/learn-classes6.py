# name the file color_module
# in another file import this: from color_module import Color
class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue
    def __str__(self):
        return "Color: R={0:d}, G={1:d}, B={2:d}".format (self._red, self._green, self._blue)

c = Color(15,25,3)
print(c)    