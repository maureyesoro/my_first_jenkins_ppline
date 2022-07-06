import logging

logging.basicConfig(level=DEBUG, filename='/Users/mro/Documents/Enroute/Repos/my_first_jenkins_ppline/src/logs.txt')

def createApp():
    logging.debug('creating app')
    print('creating app')

createApp()