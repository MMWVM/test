# Requier Modules 
import json , os, datetime


# Class data
class JSData:

    def __init__(self):
        self.PAT = './databesas/usersdata.json'
        # obj 
        _userdata = {'statistics':{'sessions':0},'users':{}}
        # check data
        if not os.path.isfile(self.PAT):
            json.dump(_userdata, open(self.PAT, 'w'), indent=3)

        
    def GET_DATA(self):
        return json.load(open(self.PAT, 'r'))
    
    def UPDATE_DATA(self, NEW_DATA: dict):
        json.dump(NEW_DATA, open(self.PAT, 'w'), indent=3)

    def ADD_USER(self, user_id: int):
        data = self.GET_DATA()
        data['users'].update({user_id:{'date':str(datetime.datetime.now())}})
        self.UPDATE_DATA(data)

    def ADD_SESSIONS_CROVET(self):
        data = self.GET_DATA()
        data['statistics']['sessions'] +=1
        self.UPDATE_DATA(data)

    def GET_USERSCOUNT(self):
        return len(self.GET_DATA()['users'])

    def USER_EXISTS(self, user_id: int):
        data = self.GET_DATA()
        return True if str(user_id) in data['users'] else False
    

