# class tweets:
#     def setuser(self,user):
#         self.user = user
#     def getuser(self):
#         return self.user
#     def setid(self,id):
#         self.id = id
#     def getid(self):
#         return self.id
#     def settime(self,time):
#         self.time = time
#     def gettime(self):
#         return self.time
#     def setcontent(self,content):
#         self.content = content
#     def getcontent(self):
#         return self.content

class Tweet:
    def __init__(self, user, id, t , content):
        self.user = user#username
        self.id = id#tweets id
        self.t = t#createtime
        self.content = content#tweets content