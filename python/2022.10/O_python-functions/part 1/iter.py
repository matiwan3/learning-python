# Iterator

class Iterator:
    def __init__(self, start, stop):
        self.start = start 
        self.stop = stop
        
    def __iter__(self):
        self.cur = self.start
        return self
    
    def __next__(self):
        if self.cur >= self.stop:
            raise StopIteration
        
        self.cur += 1
        return self.cur - 1
    
def example():
    custom_obj = Iterator(1, 10)
    obj_iter = iter(custom_obj)
    print(obj_iter)
    for num in obj_iter:
        print(num)