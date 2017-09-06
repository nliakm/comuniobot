import configparser
import os

def createConfig():
    if (not checkIfFileExists('config.ini')):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'1': '2000', '2': '1500', '3': '1000', '4': '500' }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        return True
    return False

def checkIfFileExists(filename):
    return os.path.isfile(filename)

def updateConfig(filename):
    if (checkIfFileExists(filename)):
        config = configparser.ConfigParser()
        config.sections()

        config.read(filename)
        for i in config['DEFAULT']:
            print i
        return True
    return False

def readConfig(filename, placement):
    if (checkIfFileExists(filename)):
        config = configparser.ConfigParser()
        config.sections()

        config.read(filename)   
        return config['DEFAULT'][str(placement)]
    return -1  