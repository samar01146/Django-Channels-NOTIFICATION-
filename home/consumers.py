from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({"status":'connected from django channels'}))
        
    def receive(self, text_data):
        print("_________----text", text_data)
        self.send(text_data=json.dumps({"status":'we got you'}))

    
    def disconnect(self, *args, **kwargs):
        print("________________--disconnected")
        
    def send_notification(self, event):
        print("________________Send_notification")
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({"payload":data}))
        
        
class NewConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "new_consumer"
        self.room_group_name = "new_consumer_group"
        await (self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({"status":'connected from django new async json consumer'}))
        
    async def receive(self, text_data):
        print("_________----text", text_data)
        await self.send(text_data=json.dumps({"status":'we got you'}))

    
    async def disconnect(self, *args, **kwargs):
        print("________________--disconnected")
        
    async def send_notification(self, event):
        print("________________Send_notification")
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({"payload":data}))
    