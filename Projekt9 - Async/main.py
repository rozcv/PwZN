import aiofiles
import aiohttp
import asyncio
import cv2

urls = ['https://s3.party.pl/newsy/maly-pudel-w-domu-406396-4_3.jpg',
        'https://i.pinimg.com/originals/37/5a/1a/375a1a44ff48b0cd8e34a8c65f439042.jpg', ]

async def main():
    for url in urls:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print("Status:", resp.status)
                print("Content-type:", resp.headers['content-type'])
                if resp.status == 200:
                    f = await aiofiles.open('file.png', mode='wb')
                    await f.write(await resp.read())
                    await f.close()

asyncio.run(main())
