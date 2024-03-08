# Requier Module 
import os 

# Requier Plug 
from Utils.databesas import JSData

if not os.path.exists('./.sessions'): #  check the  session file 
    os.mkdir('./.sessions') # Create the sessions file 

if not os.path.exists('./databesas'): # check the databesas file 
    os.mkdir('./databesas') # create the databesas file 
# data class 
jsdata = JSData()

class Config:
    API_KEY  : str  = "API_KEY" # BOT TOKEN  API_HASH
    SUDO     : int  = 00000000 # user_id admin
    CHANNLS  : list = ['radfx2'] # channels liste
    