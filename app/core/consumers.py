from unittest import result
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class CoreConsumer(AsyncJsonWebsocketConsumer):


    async def connect(self):
      await self.channel_layer.group_add('core', self.channel_name)
      await self.accept()


    async def disconnect(self,code):
         await self.channel_layer.group_discard('core', self.channel_name)

    async def scrape_result (self,event):
        results =event['text']

        await self.send(json.dumps(results))