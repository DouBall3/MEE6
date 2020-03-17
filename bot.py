import chatservice

if __name__ == '__main__':
    cs = chatservice.ChatService()
    print(cs.spaces()[0]['name'], '\n')
    print(cs.members(cs.spaces()[0]['name'])[0]['member']['name'])
    print(cs.ping(cs.members(cs.spaces()[0]['name'])[0]['member']['name'], cs.spaces()[0]['name'], 'test'))