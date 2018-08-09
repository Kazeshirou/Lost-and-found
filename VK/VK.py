import requests
import os, re, io
from VKPostParser import VKPostParser
from VKTool import VKPostGet
import nltk# import sent_tokenize, word_tokenize
import pickle

token = "" #»стекает через сутки



class Writter(object):
    def __init__(self, group_id = None, group_name = None):
        self.group_id = group_id
        self.group_name = group_name
        self.offset = 0
        self.count = 100
        self.all_mess = None





    def get_json(self):
        global token
        Server = None
        if self.group_name is None:
            Server = VKPostGet(token,self.group_id,self.offset,count=self.count)
        elif self.group_id is None:
            Server = VKPostGet(token,None,self.offset,count=self.count,domain=self.group_name)
        else:
            raise Exception("Group name!!!")
        json = Server.get_json()
        self.offset += self.count
        return json


    def __update_id_table(self, posts):
        f = open("id_table.txt","a")
        for post in posts:
            row = "%d %s" % (post.local_id, post.id)
            print(row,file = f)
        f.close()

        script_dir = os.path.dirname(__file__)
        rel_path = "pickles/%s.pickle" % posts[0].id
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path,'wb') as f:
            pickle.dump(posts,f)



    def get_posts(self, json):
        all_posts = []
        Parser = VKPostParser()
        posts = Parser.parse(json)
        self.__update_id_table(posts)
        for p in posts:
            if len(p.text) == 0:
                continue
            lst = self.separator(p.text)
            lst.insert(0,p.local_id)
            prol_text = self.prolog_syntax(lst)
            all_posts.append(prol_text)
        return all_posts

    def write_posts(self, all_posts):
        f = open("postinput.pl","a",encoding='utf-8')
        for p in all_posts:
            f.write(p + '\n')
        f.close()
       



        

    def separator(self, text):
        #document = document.replace("\n"," ",100)
        #result = re.split(r'(?<=\w[.!?]) ', document)

        list_of_list = []
        text = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", text)
        sentences = nltk.sent_tokenize(text)
        for s in sentences:
            words = nltk.word_tokenize(s)
            list_of_list.append(words)

        for i in range(len(list_of_list)):
            for j in range(len(list_of_list[i])):
                list_of_list[i][j] = list_of_list[i][j].lower()
        return list_of_list

    def prolog_syntax(self, lst):
        result = "post(%d, [" % lst[0]
        del lst[0]
        for s in lst:
            sent = str(s)
            sent = 'sentence(' + sent[1:-1] + '), '
            result += sent
        result = result[:-2] + "])."
        return result

    def run(self):
        for i in range(10):
            try:
                jsons = self.get_json()
            except:
                print("The end!")
                d = 9
            all_text = self.get_posts(jsons)
            self.write_posts(all_text)

    def remove_emoji(self):
        text = ""
        with io.open("postinput.pl",mode="r", encoding="utf-8") as f:
            text = f.read()
        emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F1E0-\U0001F1FF"
                           "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)
        with io.open("postinput1234.pl",mode="w", encoding="utf-8") as f:
            f.write(text)

    def white_list(self, lst):
        spec_symb = set('!,.? \n')
        for i in range(len(lst)-1,-1,-1):
            if not (lst[i].isalnum() or (lst[i] in spec_symb)):
                del lst[i]

        curr = 0
        while(curr < len(lst)):
            if not lst[curr].isalnum():
                symb = lst[curr]
                del lst[curr]
                lst.insert(curr, ' ')
                lst.insert(curr, symb)
                lst.insert(curr, ' ')
                curr += 2
            curr += 1

        return lst

    def debug_run(self):
        posts = self.load_pickles()
        result = []
        for p in posts:
            test = None
        
            test = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", p.text)
            curr = 0
            AAA = test
            test = list(test)
            test = self.white_list(test)
            test = ''.join(test)

            lst_post = self.separator(test)
            if len(lst_post) == 0:
                continue
            lst_post.insert(0,p.local_id)
            prol_text = self.prolog_syntax(lst_post)
            result.append(prol_text)
        self.write_posts(result)



    def load_pickles(self):
        raw_data = []
        for filename in os.listdir(os.path.dirname(__file__) + "/pickles/"):
            data = []
            with open(os.path.dirname(__file__) + "/pickles/" + filename, 'rb') as f:
                data = pickle.load(f)
            raw_data += data
    
        return raw_data


A = Writter(None,"poisk_ul")
A.debug_run()






