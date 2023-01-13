from flask import Flask, jsonify, request
import pyrebase
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime 
from flask_cors import CORS

firebaseConfig = {
  'apiKey': "AIzaSyCXbpCdXSN3pworSC_B_mBxos05Aoqdzdc",
 'authDomain': "facecall-26b9b.firebaseapp.com",
 'databaseURL': "https://facecall-26b9b-default-rtdb.firebaseio.com",
 'projectId': "facecall-26b9b",
 'storageBucket': "facecall-26b9b.appspot.com",
 'messagingSenderId': "196172910629",
 'appId': "1:196172910629:web:692d1a9bec0383f2042fcc",
 'measurementId': "G-5K8GR4SPVQ",
  'databaseURL':"https://facecall-26b9b-default-rtdb.firebaseio.com/"
}
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
auth=firebase.auth()
storage=firebase.storage()
# creating a Flask app
app = Flask(__name__)
user=""
CORS(app)
cors=CORS(app,resources={
    r"/*":{
        "origins":""
    }
})
#Create account
@app.route('/create', methods=['GET', 'POST'])
def create():
    datax=request.get_json()
    Cemail=datax['Cemail'] #input
    username=datax['username']#input("enter username: ")
    Cpassword=datax['Cpassword']#input
    auth.create_user_with_email_and_password(Cemail,Cpassword)
    global user
    user=username
    return jsonify('Account created')
#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    data=request.get_json()
    Lemail=data['Lemail']#input("enter mail: ")
    username=data['username']#input("enter username: ")
    global user
    user=username 
    Lpassword=data['Lpassword']#input("enter password: ")
    try:    
        auth.sign_in_with_email_and_password(Lemail,Lpassword)
        return jsonify('Logged-in')     
    except:
        return jsonify('Invalid password')
#url for adding new student
@app.route('/add', methods=['GET', 'POST'])
def add():
    dataz=request.get_json()
    global user
    namey=dataz['namey']#input("enter name of student")
    namey=namey.upper()
    data={"name":namey,"time":"","date":"","attn":0}
    db.child(user).child(namey).set(data)
    return jsonify('Students added')
    
#url for taking attendance           
@app.route('/atten', methods=['GET', 'POST'])
def atten():
    try:
        cap()
        return jsonify('Attendance Taken')
    except:
        cv2.destroyAllWindows()
        return jsonify('Reload page')
#URL to get data
@app.route('/getdata', methods=['GET', 'POST'])
def getdata():
    global user
    people=db.child(user).get()
    for person in people.each():
        list=[person.val()]
    return jsonify(people.val())
#Code for attendance
def cap():
    path='img'
    imgs=[]
    stu_nm=[]
    myclass=os.listdir(path)
    # print(myclass)
    for captured in myclass:
        current=cv2.imread(f'{path}/{captured}')
        imgs.append(current)
        stu_nm.append(os.path.splitext(captured)[0])
    print(stu_nm)
    #Extract face features
    def encode(imgs):
        encodelist=[]
        for img in imgs:
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encd=face_recognition.face_encodings(img)[0]
            encodelist.append(encd)
        return encodelist
    ENCODEDONE=encode(imgs)    
    # print("encoded")   

    # Add Name to Database
    def attn(name):
        with open('attn.csv','r+') as f:
            data=f.readlines()
            namelist=[]
            for i in data:
                entry=i.split(',')
                namelist.append(entry[0])
            if name not in namelist:
                time_now=datetime.now()
                tstr=time_now.strftime('%H:%M:%S')
                dstr=time_now.strftime('%Y/%m/%d')

                f.writelines(f'{name},{tstr},{dstr}\n')
                #database              
                people=db.child(user).get()
                for person in people.each():
                    if person.val()['name']==name:
                            #  db.child(user).child(user).update({"name":name,"time":tstr,"date":dstr})
                            attn=db.child(user).child(name).get()
                            attn=attn.val()["attn"]
                            db.child(user).child(name).update({"attn":attn+1,"time":tstr,"date":dstr})
    #readwithcamera 
    cap=cv2.VideoCapture(0)
    while True:
        ret, frame=cap.read()
        faces=cv2.resize(frame,(0,0),None,0.25,0.25)
        faces=cv2.cvtColor(faces,cv2.COLOR_BGR2RGB)
        faces_current=face_recognition.face_locations(faces)
        encd_current=face_recognition.face_encodings(faces,faces_current)
        for eface,loc in zip(encd_current,faces_current):
            matches=face_recognition.compare_faces(ENCODEDONE,eface)
            dist=face_recognition.face_distance(ENCODEDONE,eface)
    #match both image
            matchindex= np.argmin(dist)
            if matches[matchindex]:
                name=stu_nm[matchindex].upper()
                print(name)  
                y1,x2,y2,x1=loc
                y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(frame,(x1,y1),(x2,y2),(125,0,125),2) 
                cv2.rectangle(frame,(x1,y2-35),(x2,y2),(255,255,0),cv2.FILLED) 
                cv2.putText(frame,name,(x1+10,y2-6),cv2.FONT_ITALIC,1,(0,0,0),2) 
                attn(name)  
        cv2.imshow("Camera",frame)
        if cv2.waitKey(50)==13:
            break
    cap.release()
    cv2.destroyAllWindows() 
                  
# driver function
if __name__ == '__main__':
     app.run(debug=True)
