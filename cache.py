import requests,json


class Cache():
    def __init__(self):
        self.cache_dict = {}


    def add(self,url,image):
        self.cache_dict[url]=image


    def exists(self, url):
        return url in self.cache_dict


    def data_get(self, url):
        if not self.exists(url):
            print(url)
            pok_dict=requests.get(url)
            self.add(url,pok_dict.content)
        return self.cache_dict[url]


