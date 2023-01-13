import urllib
import pyrebase
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime 
firebaseConfig = {
  'apiKey': "AIzaSyBIx79XAsr6eDroBBBId0ouvS31lEY6teE",
  'authDomain': "minor-bdc68.firebaseapp.com",
  'projectId': "minor-bdc68",
  'storageBucket': "minor-bdc68.appspot.com",
  'messagingSenderId': "941481355016",
  'appId': "1:941481355016:web:27f23ab6e1a50572176ebd",
  'measurementId': "G-M3C0LHGRV4",
  'databaseURL':"https://minor-bdc68-default-rtdb.firebaseio.com"
}
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
auth=firebase.auth()
storage=firebase.storage()
#label .comm

#authorization
#ct=input("Create account:C,Login:L")
# if ct=='L' or ct=='l':
#     email=input("enter mail:")
#     password=input("enter password:")
#     try:    
#         auth.sign_in_with_email_and_password(email,password)
#         print("logged in ")
#     except:
#         print("Invalid password")
# elif ct=='c' or ct=='C':
#     email=input("enter mail:")
#     #label .again
#     password=input("enter password:")
#     re_type=input("Re-type password:")
#     if password==re_type:
#              try:
#                  auth.create_user_with_email_and_password(email,password)
#                  print("acount created")
#              except:
#                 print("user already exist")
#     else:
#         print("re-enter password")
#         #goto .again
# else:
#     print("enter write command")
#     #goto .comm

#Storage
#filename=input("enter name of file you want to upload")
fileoncloud=input("enter name of file in cloud")
#upload
#storage.child(fileoncloud).put(filename) 
#url
print(storage.child(fileoncloud).get_url(None))
#download
fileoncloud=input("enter file you want to download")
storage.child(fileoncloud).download("path","shruu.jpg")
# print data
# url=storage.child(fileoncloud).get_url(None)
# f=urllib.request.urlopen(url).read()
# print(f)
#databse
# data={"age":40,"name":"yash"}
# db.push(data)
# db.child("people").push(data)
# db.child("people").child("myownid").set(data)
# #update
# db.child("people").child("myownid").update({"name":"jain"})
# people=db.child("people").get()
# for person in people.each():
#   #print(person.val())
#   #print(person.key())
#   if person.val()['name']=='yash':
#     db.child("people").child(person.key()).update({"name":"yjain"})


# print("done")

# #delete
# db.child("people").child("myownid").child("age").remove()

# #read
# people=db.child("people").get()

#authorization
# username=input("enter username: ")
#  #allot db 
# data={"name":"","time":"","date":""}
# db.child(username).child(username).set(data)
 
# a=0
# ct=input("Create account:C,Login:L")
# if ct=='L' or ct=='l':
#     Lemail=input("enter mail:")
#     username=input("enter username: ")
#     Lpassword=input("enter password:")
    
#     try:    
#         auth.sign_in_with_email_and_password(Lemail,Lpassword)
#         print("logged in ")
#         a=1
#         #access db
#         if a==1:
#           db.child(username).child(username).update({"name":"yash"})
#     except:
#         print("Invalid password")
# elif ct=='c' or ct=='C':
#     email=input("enter mail:")
#     #label .again
#     password=input("enter password:")
#     re_type=input("Re-type password:")
#     if password==re_type:
             
#                  auth.create_user_with_email_and_password(email,password)
#                  print("acount created")
#                  username=input("enter username: ")

#                  #allot db 
#                  namex=input("enter name of student")
#                  data={"name":namex,"time":"","date":""}
#                  db.child(username).child(username).set(data)
             
#     else:
#         print("re-enter password")
#         #goto .again
# else:
#     print("enter rigte command")
# #     #goto .comm
# tstr='yjs'
# dstr='yjs'
# user="yj"
# people=db.child(user).get()
# for person in people.each():
#                       if person.val()['name']=="yash":
#                                   db.child(user).child(user).update({"time":tstr,"date":dstr})