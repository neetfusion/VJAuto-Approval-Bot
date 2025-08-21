# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27846034"))
    API_HASH = getenv("API_HASH", "980caee71c20f6babaf86d985f5af9e5")
    BOT_TOKEN = getenv("BOT_TOKEN", "8312957393:AAH1-aotfhS7y0Qg07K0Qn3AhxgX7cr9A48")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002220587356")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "1320989352").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://neetfusionin:neetfusionin@cluster0.c7aecmc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @NEET_Fusion
# Ask Doubt on telegram @Sciencemade
