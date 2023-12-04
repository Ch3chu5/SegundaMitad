##Descargar Imagenes

import asyncio
import aiohttp



async def download_image(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            with open(filename, 'wb') as f:
                f.write(await response.read())

            print(f"Imagen descargada: {filename}")
        
async def main():
    tasks = [
        download_image('https://thumbs.dreamstime.com/b/paisajes-de-yosemite-46208063.jpg', 'imagen1.jpg'),
        download_image('https://img.freepik.com/fotos-premium/paisajes-yosemite_328046-14266.jpg?w=2000', 'imagen2.jpg'),
        download_image('https://img.freepik.com/fotos-premium/hermosa-vista-parque-nacional-yosemite-al-atardecer-california-ee_255553-1105.jpg', 'imagen3.jpg'),
        download_image('https://cdn.pixabay.com/photo/2016/02/10/21/59/landscape-1192669_640.jpg', 'imagen4.jpg')
    ]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
