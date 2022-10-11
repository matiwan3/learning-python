# Asynchronous Iterator
# anext()
import asyncio

class AsyncIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        
    def __aiter__(self):
        self.cur = self.start
        return self
    
    async def __anext__(self):
        await asyncio.sleep(1)
        if self.cur >= self.stop:
            raise StopAsyncIteration
        
        self.cur += 1
        return self.cur - 1
    
async def example():
    custom_obj = AsyncIterator(1, 10)
    obj_iter = aiter(custom_obj)
    print(await anext(obj_iter))
    print(await anext(obj_iter))
    print(await anext(obj_iter))

asyncio.run(example())