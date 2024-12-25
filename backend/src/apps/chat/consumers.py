import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class CourseChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.course_id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = f'chat_{self.course_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.gruop_discard(
            self.room_group_name,
            self.channel_name
        )

    from asgiref.sync import sync_to_async

    async def receive(self, text_data):
        from apps.users.models import CustomUser
        try:
            text_data_json = json.loads(text_data)
            username = text_data_json['username']
            message = text_data_json['message']

            # Используем sync_to_async для синхронного кода
            user = await sync_to_async(CustomUser.objects.get)(username=username)

            await self.save_message(user, message)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': user.username
                }
            )

        except json.JSONDecodeError:
            print("Invalid JSON data received")
        except KeyError as e:
            print(f"Missing key in JSON data: {e}")
        except CustomUser.DoesNotExist:
            print(f"User '{username}' does not exist")

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message' : message,
            'username': username
        }))


    @sync_to_async
    def save_message(self, user, message):
        from .models import CourseMessage

        CourseMessage.objects.create(
            course_id=self.course_id,
            user=user,
            text=message
        )