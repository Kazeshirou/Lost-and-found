from VKTool import VKPost


class VKPostParser(object):
    def __init__(self, **kwargs):
        self.post_id = 0
        self.__read_id()
        return super().__init__(**kwargs)

    def parse_item(self,item):
        is_ads = None
        try:
            is_ads = item['marked_as_ads']
        except:
            pass
        owner_id = item['owner_id']
        text = item['text']
        id = item['id']
        date = item['date']

        Post = VKPost(id,date,text,owner_id)
        Post.local_id = self.post_id
        self.post_id += 1
        self.__write_id()
        return Post

    def parse_items(self,json_items):
        posts = []
        for item in json_items:
            post = self.parse_item(item)
            posts.append(post)
        return posts

    def parse(self,json):
        response = None
        try:
            response = json['response']
        except:
            response = json['error']
            code = response['error_code']
            message = response['error_msg']
            raise Exception('%s \ncode: %d' % (message, code))
        items = response['items']
        posts = self.parse_items(items)
        return posts 


    def __read_id(self):
        f = open("curr_id.txt",'r')
        self.post_id = int(f.read())
        f.close()
    def __write_id(self):
        f = open("curr_id.txt",'w')
        f.write(str(self.post_id))
        f.close()
