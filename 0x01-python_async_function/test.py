import asyncio


async def main():
    print('Damola')
    task = asyncio.create_task(foo('Tolu'))
    await asyncio.sleep(0.5)
    print('finished')
    
async def foo(text):
    print(text)
    await asyncio.sleep(10)
    
asyncio.run(main())