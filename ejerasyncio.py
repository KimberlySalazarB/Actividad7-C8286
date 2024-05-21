import asyncio
import aiohttp
#Define la funciòn asincronica para hacer solicitudes HTTP
async def fetch(url, session):
    async with session.get(url) as response:
        print(f"Status:{response.status}")
        data=await response.text()
        print(f"Data from{url} fetched")
        return data

# crea una terea sincronica principal que maneje multiples solicitudes
async def main(urls):
    async with aiohttp.ClientSession() as session:
        #fech maneja la solicitud
        tasks=[fetch(url, session)for url in urls]
        #Iniciar todas las tareas definidas en paralelo
        await asyncio.gather(*tasks)

urls=["https://code.visualstudio.com/download"]*5
asyncio.run(main(urls))

