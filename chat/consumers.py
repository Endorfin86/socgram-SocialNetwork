import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Chat

class ChatConsumer(AsyncWebsocketConsumer):
    # + Функция соединение клиента и сервера
    async def connect(self):
        # Перехватываем данные из ссылки
        self.name = self.scope['url_route']['kwargs']['user']
        # Задаем имя группы клиентов общающихся по вебсокету
        self.group_name = 'chat_%s' % self.name

        # Добавляем группу в канальный слой
        await self.channel_layer.group_add(
            # Имя группы в канале
            self.group_name,
            # Имя канала (назначается автоматически и имеет стандартную переменную - channel_name)
            self.channel_name
        )
        # Принимаем все параметры
        await self.accept()
    
    # + Функция разрыва соединения клиента и сервера
    async def disconnect(self):
        # Указывается все то же самое что и при добавлении группы, только вместо group_add указываем group_discard
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # 1. Получаем данные от клиента (с шаблона) из вебсокета
    async def receive(self, text_data):
        # Выгружаем в переменную переконвертированные данные в словарь из JSON
        data = json.loads(text_data)
        # Записываем данные из словаря data в отдельные переменные
        message = data['message']
        user = data['username']
        friend = data['friendname']
        # Запускаем функцию для сохранения данных в базу данных, передав ей параметры - username, room, message
        await self.save_message(user, friend, message)

        # 2. Передаем в группу канального слоя данные
        await self.channel_layer.group_send(
            # Указываем имя группы
            self.group_name,
            {
                # Эта функция chat_message() будет запущена сразу после передачи данных в группу
                'type': 'chat_message',
                # Данные передающиеся в группу
                'message': message,
                'user': user
            }
        )

    # 3. Получаем данные из группы
    # В переменной event записан словарь {'type': 'chat_message', 'message': message, 'user': user}
    # Словарь распаковываем и записываем в отдельные переменные
    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        # 4. Передаем данные обратно в вебсокет (шаблон), упаковывая их в JSON
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user
        }))

    # Декоратор для взаимодействия с синхронизируемыми частями Django
    @sync_to_async
    # Функция для записи данных в базу данных
    def save_message(self, user, friend, message):
        sender = Chat.objects.create(sender=user, friend=friend, message=message)
        sender.save()

    

    

