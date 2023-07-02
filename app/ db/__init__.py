from tinydb import TinyDB, Query
from typing import List, Optional
from ..models.message import Message


class Database:
    def __init__(self):
        self.db = TinyDB('db.json')
        self.messages = self.db.table('messages')
        self.likes = self.db.table('likes')

    def get_messages(self) -> List[Message]:
        messages = self.messages.all()
        return [Message(**message) for message in messages]

    def get_message(self, message_id: int) -> Optional[Message]:
        message = self.messages.get(doc_id=message_id)
        if message:
            return Message(**message)
        return None

    def create_message(self, message: Message) -> Message:
        message_dict = message.dict()
        message_dict['id'] = self.messages.insert(message_dict)
        return Message(**message_dict)

    def update_message(self, message_id: int, message: Message) -> Optional[Message]:
        if self.messages.contains(doc_id=message_id):
            message_dict = message.dict()
            message_dict['id'] = message
