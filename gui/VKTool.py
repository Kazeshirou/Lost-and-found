import requests, json


class VKPost():
    def __init__(self,id, date, text,owner_id):
        self.mess_id = id
        self.unixtime = date
        self.text = text
        self.owner_id = owner_id
        self.local_id = 0
        self.id = str(owner_id)+'_'+str(id)









class VKPostGet():
    def __init__(self,token,owner_id = None,offset = 0,count = 1,domain="",version="5.52"):
        self.https = "https://api.vk.com/method/wall.get?"
        if owner_id is None:
            self.https +="domain=%s&" % domain
        else:
            self.https += "owner_id=%s&" % - owner_id
        self.https += "count=%d&" % count
        self.https += "offset=%d&" % offset
        self.https += "v=5.52&"
        self.https += "access_token=%s" % token

        self.js_object = None
    def send_request(self):
        answer = requests.get(self.https)
        text = answer.text
        return text

    def create_json(self, text):
        self.js_object = json.loads(text)
        
    def get_json(self):
        text = self.send_request()
        self.create_json(text)
        return self.js_object




if __name__ == "__main__":
    A = VKPostGet(token,1)
    d = A.get_json()
    h = 9
    




