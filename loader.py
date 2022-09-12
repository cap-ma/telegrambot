import requests
import json
  
def instagramdownloader(link):

    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "8c263d31ecmshdd825e691eaf30ap1d1d2ejsn7a7946bd507f",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jrest=json.loads(response.text)

    
    if  'error' in jrest:
        return  False
    else:
        dict={}
        if jrest["Type"]=='Post-Image':
            dict['type']='image'
            dict["media"]=jrest['media']
            return dict
        elif jrest["Type"]=='Post-Video':
            dict['type']='video'
            dict['media']=jrest['media']
            return dict
        elif jrest['Type']=='Carousel':
            dict['type']='carousel'
            dict['media']=jrest['media']
            return dict
        else:
            return False
 
def tiktok_downloader(link):
    
    print("i am here")
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "8c263d31ecmshdd825e691eaf30ap1d1d2ejsn7a7946bd507f",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result=response.text
    jrest=json.loads(result)
  
    return jrest


def youtubedownloader(link):

    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

    querystring = {"videoId":link}

    headers = {
        "X-RapidAPI-Key": "8c263d31ecmshdd825e691eaf30ap1d1d2ejsn7a7946bd507f",
        "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jrest=json.loads(response.text)
    
    return jrest




