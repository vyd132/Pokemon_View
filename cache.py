import requests,json,os
from os import path

class Cache():
    def __init__(self):
        self.cache_dict = {}


    def add(self,url:str,image):
        self.cache_dict[url]=image

        file=open(f'cache\{url}','wb+')
        file.write(image)
        file.close()


    def exists(self, url):
        return path.exists(f'cache\{url}')


    def data_get(self, url):
        url_name=url.replace(':','').replace('/','')
        if not self.exists(url_name):
            print(url)
            pok_dict=requests.get(url)
            self.add(url_name,pok_dict.content)
        file=open(f'cache\{url_name}', 'rb')
        obj=file.read()
        file.close()
        return obj


