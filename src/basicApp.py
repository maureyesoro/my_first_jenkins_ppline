import logging

logging.basicConfig(level=DEBUG, filename='./logs.txt')

def createApp():
    logging.debug('creating app')
    print('creating app')

createApp()
print('this was created from feature 2')