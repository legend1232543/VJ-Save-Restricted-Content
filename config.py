import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27039000"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5397095439b5ae9d00634ed2e98ff3e0")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sachinkumar0989770:<db_KgY6lo10lz3H4xs6>@cluster0.klz8w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
