# #!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["book_data"]
mycol = mydb["bookdata"]

book_name = "剑" 
myquery = { "book_name": { "$regex": "^{}".format(book_name)} }
 
mydoc = mycol.find(myquery)
url = []
for x in mydoc:
   url.append(x['book_url'])
 
print(url) 
book_list = [] 
for u in url:
   myquery = { "book_url": u}
   mydoc = mycol.find(myquery)
   for x in mydoc:
      a = {'书名':'','网址':''}
      a['书名'] = x['book_name']
      a['网址'] = x['book_url']
      book_list.append(a)
      # print(a)

print(book_list)
# a = "['dasef ','casd','casd','cdsa','cdsav','vas','vfsav']"
# b = a[1:-1].split(',')
# # print(b)
# # print(type(b))
# for i in range(0,len(b)):
#    b[i] = b[i][1:-1]
# print(b)