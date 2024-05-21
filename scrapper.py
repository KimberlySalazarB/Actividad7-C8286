# -*- coding: utf-8 -*-
import asyncio

async def asyn_corrutina():
 for i in range(1,11):
     await asyncio.sleep(i)
     print('hello')

 
asyncio.run(asyn_corrutina())
