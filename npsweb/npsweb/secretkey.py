def get():
    file = open('/home/ubuntu/keys/Django-Secret.key')
    text = file.read()
    file.close()
    return text.replace('\n', '')
