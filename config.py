import os


class Config(object):
    API_HASH = os.environ.get("90d16b7e658fed5fdb5f7660875081ff")
    BOT_TOKEN = os.environ.get("5823378009:AAEE10wpbgg0qEmFXCIrQdKKIfZC952NYJg")
    TELEGRAM_API = os.environ.get["19962151"]
    OWNER = os.environ.get("1769481979")
    OWNER_USERNAME = os.environ.get("Svaraz")
    PASSWORD = os.environ.get("12345")
    DATABASE_URL = os.environ.get("mongodb+srv://Leechbot:$nopassword0$@cluster0.96aznin.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1001707403763")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("BQEwmScAej2wc0hA3BpYvoJYwJQnwhQtXCYSGrMe1G9nMjZ5TIWv-AY4pBQCiPRvM85PLpKFPdkBaUs8QU3r1QpXIyWKVzHZo6pLkncG7w7UZVtbj_xRJ0H7F7Umnl2bxeEEeQuFPytfAfiaMxjtva_iCtjXacFdOsLnK4mhA-6VL-4WBzcjmuhfjHBEzT6aCGUuV9M3tfg8yMzewEIaG1CDmjdslX58B6ENWYbcRD23kkCtdXSBjXH3s97XD-2ASLPD2yIF3eAT64wrEBNiiTcFVCHS4f9Sj7M_UWp7QZZ0BwrO5sbhQNaOKwJrmWVmfGj5tkx2NHdmnQwGUZ044_NVJ19UwgAAAABpeCb7AA", None)
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
