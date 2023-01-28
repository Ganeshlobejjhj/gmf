import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "26545949"))
    API_HASH = os.environ.get("API_HASH", "e3db4ee830581dcc11a20d140c883b2c")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION = os.environ.get("BOT_SESSION", "Gm Forward Bot")
    OWNER_ID = os.environ.get("OWNER_ID", "5869058469")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://GaneshFB:77249094@cluster0.uqftbeh.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "GaneshFB")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'DataBase')
    SESSION = os.environ.get("SESSION", "BQBj4o-f1qGSFzNbv5TEDrLaVax64QJ0Hl04pqfsbfut349F5J4foXp2F0a6Q9Ud3er8YG3WxDxpHPmKiA9wUcFgSL8dTSq_w3Gd4Nkq3xIawpQS0K0pMQEJF-wsFa9lG3XY1mMJtaEfbsAWr8rhHYJyuR6cf9fR8JFV1ROH5Ct5WnJPbkPT98HFd-SkyWmVSFq2BO_putBsdEJoRvV7qh1-jyYOFNE-oV9EN5DrG5iM1HKLkfv4UY6a4oAfj7OZj3TK0gpcbnAK-8csioDZQsp_8UScHJFA7SK4oAbwn7HMPdoVAH6x4Fvr_52OXTT4SzSHfNbyb5XsaMd5u5QWmRNsAAAAAUA5XQsA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001744041619"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "gmforward7724bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
