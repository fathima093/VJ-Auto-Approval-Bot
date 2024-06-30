# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "14068901"))
    API_HASH = getenv("API_HASH", "d7531af850ce4ed27d8200724fefb6b8")
    BOT_TOKEN = getenv("BOT_TOKEN", "5909705836:AAEal6gpo_WuLLqvlOLaBDkFUD7wa_e43io")
    FSUB = getenv("FSUB", "NewMoviez2023")
    CHID = int(getenv("CHID", "-1001760564192"))
    SUDO = list(map(int, getenv("SUDO", "674638158 1454231644").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://autofilterv3:autofilterv3@cluster0.pvrrx86.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
