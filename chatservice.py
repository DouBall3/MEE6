from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials


class ChatService:
    _chat_service = None

    def __init__(self):
        account = ServiceAccountCredentials.from_json_keyfile_name(conf['credentials_file'], "https://www.googleapis.com/auth/chat.bot")
        self._chat_service = build('chat', 'v1', http=account.authorize(Http()))

    def spaces(self):
        return self._chat_service.spaces().list().execute()['spaces']

    def members(self, space):
        return self._chat_service.spaces().members().list(parent=space).execute()['memberships']

    def ping(self, user, parent, ping):
        messages = self._chat_service.spaces().messages()
        response = messages.create(
            parent=parent,
            body={'text': user + ping}
        ).execute()
        return response
