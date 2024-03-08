# Thes Radfx2 Dev  @R_AFX CH @radfx2
# requier Modules 
from pyrogram import Client, types, filters ,enums
from pyromod import listen
import asyncio
# requier PLugins  
from config import Config

# start Client 
app = Client(
    name=".sessions/rad",
    bot_token=Config.API_KEY, 
    api_id=Config.API_ID, 
    api_hash=Config.API_HASH, 
    parse_mode=enums.ParseMode.DEFAULT,
    plugins=dict(root='Plugins')
)

# start CLient Loop
asyncio.run(app.run())