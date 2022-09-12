
from aiogram import types,Dispatcher,Bot,executor
from aiogram.dispatcher.filters import Text
from loader import instagramdownloader,tiktok_downloader, youtubedownloader

import json
import uuid
API_TOKEN='5796481105:AAFk80b4qWB3ChrGpUTB0EU4tmITcrLP6c8'
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)


@dp.message_handler(commands=['start','/help'])
async def send_welcome(message:types.Message):
    await message.reply("we begin please send the link")

@dp.message_handler(Text(startswith='https://www.tiktok.com/'))
async def test(message:types.Message):
    res=tiktok_downloader(message.text)
    
    await message.answer_audio(res['video'][0])
  
@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media(message:types.Message):
    link=message.text
    data=instagramdownloader(link)
    if data==False:
        await message.answer("ther is no anything with this URL")
    else:
        if data['type']=='image':
            await message.answer_photo(photo=data['media'])
        elif data['type']=='video':
            await message.answer_video(video=data['media'])
        elif data['type']=='carousel':
            for i in data['media']:
                await message.answer_photo(i)
        else:
            await message.answer("there is nothing found")


@dp.message_handler(Text(startswith="https://www.youtube.com/"))#it only works for 
async def download_youtube_video(messege:types.Message):
    s1 = messege.text
    s2 = "="

    llink=s1[s1.index(s2) + len(s2):]
    res=youtubedownloader(llink)
    
   
    


    
    try:

        await messege.answer_video(res['videos']['items'][0]['url'])
    except Exception as e:
        print(" smth with the meomry of the video bad happened")

    
    



if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)

