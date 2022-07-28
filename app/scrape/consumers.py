from unittest import result
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class ScrapeConsumer(AsyncJsonWebsocketConsumer):


    async def connect(self):
      await self.channel_layer.group_add('scrape', self.channel_name)
      await self.accept()


    async def disconnect(self,code):
         await self.channel_layer.group_discard('scrape', self.channel_name)

    async def scrape_result (self,event):
        results =event['text']

        await self.send(json.dumps(results))