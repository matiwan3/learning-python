import asyncio


# synchronous programming executing lines with order; sequential
# def foo():
#     return

# foo()

async def main():  # create a wraper around the function
    print('hello, function')
    # await foo('text')
    task = asyncio.create_task(foo('text'))
    await asyncio.sleep(0.5)
    # await task  # wait for task to finish and dont go further until its not finished
    print('finished')
    
async def foo(text):
    print(text)
    await asyncio.sleep(10)  # await only in async
    
asyncio.run(main())
    
    