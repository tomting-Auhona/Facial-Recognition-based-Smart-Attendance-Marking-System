import numpy as np
import face_recognition as fr
import cv2
import os
from datetime import datetime
import pyttsx3 as pys

# this part of code is used for training part where we are getting images from Images Attendance folder one by one and generate their encodings and store
# in known_encodings and known_names list

# Use your path of Images Attendance here
path = 'D:\App\Images Attendance'

known_encodings = []
known_names = []
encodeList = []


def findEncodings():
    for file in os.listdir(path):
        img = cv2.imread(path + '/' + file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)
        known_encodings.append(encode[0])
        known_names.append(file.split('.')[0])
    # print(known_encodings)
    print(known_names)
    print('Encoded successfully')

findEncodings()

def markAttendance(names, Id):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        myDataList.append((names, Id))
        for i in myDataList:
            name = i[0]
            id = i[-1]
            if names in name and Id in id:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                date = now.date()
                f.writelines(f'\n{names},{dtString},{Id},{date}')
            else:
                pass

# This is used for live detection (testing purpose)

def live_camera():
    video_capture = cv2.VideoCapture(0)
    while video_capture.isOpened():
        ret, frame = video_capture.read()

        # rgb_frame = frame[:, :, ::-1]

        face_locations = fr.face_locations(frame)
        face_encodings = fr.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            matches = fr.compare_faces(known_encodings, face_encoding)
            global namee

            namee = "Unkown Entity"

            face_distances = fr.face_distance(known_encodings, face_encoding)

            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                namee = known_names[best_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, namee, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            output = namee.split('_')
            markAttendance(output[0], output[1])

        cv2.imshow('Webcam_facerecognition', frame)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            break



import tkinter as tk

root = tk.Tk()

from tkinter import *
from PIL import ImageTk, Image

# Make a Canvas (i.e, a screen for your project
canvas1 = tk.Canvas(root, width=845, height=510)
root.title("Home page")
canvas1.pack()
canvas1['bg'] = 'white'
# -------------
# Attendance marking app image
# -------------
img1 = Image.open("atten.png")
test = ImageTk.PhotoImage(img1)

label1 = tk.Label(image=test)
label1.image = test

# Position image
label1.place(x=-1, y=150)
# ------------------
# girl image
# ------------------

img2 = Image.open("girl.png")
test2 = ImageTk.PhotoImage(img2)

label2 = tk.Label(image=test2)
label2.image = test2

# Position image
label2.place(x=500, y=140)
# ---------------------------
# Created by Auhona image
# ---------------------------
img3 = Image.open("auhona1.png")
test3 = ImageTk.PhotoImage(img3)

label3 = tk.Label(image=test3)
label3.image = test3
# Positioning image
label3.place(x=-1, y=460)
# ---------------------------
# sidebar1
# ---------------------------
img4 = Image.open("sidebar1.png")
test4 = ImageTk.PhotoImage(img4)

label4 = tk.Label(image=test4)
label4.image = test4
# Positioning image
label4.place(x=500, y=77)
# ---------------------------
# sidebar2
# ---------------------------
img5 = Image.open("sidebar2.png")
test5 = ImageTk.PhotoImage(img5)

label5 = tk.Label(image=test5)
label5.image = test5
# Positioning image
label5.place(x=695, y=77)
# ---------------------------
# downbar
# ---------------------------
img6 = Image.open("log.png")
test6 = ImageTk.PhotoImage(img6)

label6 = tk.Label(image=test6)
label6.image = test6
# Positioning image
label6.place(x=497, y=331)
pys.speak("Welcome to Attendance Marking App using Facial Recognition. We hope you have a good day and encounter no issues")
# -----------------------------
# To open a new window
# ------------------------------

def createNewWindow():
    newWindow = tk.Toplevel(root)
    #buttonExample = tk.Button(newWindow, text='capbutton', command=createNewWindow)

    newWindow.title("Camera page")
    newWindow.geometry("845x510")

    #buttonExample.pack(side='top')
    newWindow['bg'] = 'white'

    # -----------------
    # Name
    # -----------------
    img7 = ImageTk.PhotoImage(Image.open("namz.png"))
    label7 = Label(newWindow, image=img7)
    label7.pack()
    # Positioning image
    label7.place(x=50, y=100)
    # -----------------
    # Date & Time
    # -----------------
    img8 = ImageTk.PhotoImage(Image.open("date.png"))
    label8 = Label(newWindow, image=img8)
    label8.pack()

    # Positioning image
    label8.place(x=50, y=300)
    # -----------------
    # Title
    # -----------------
    img9 = ImageTk.PhotoImage(Image.open("title.png"))
    label9 = Label(newWindow, image=img9)
    label9.pack()
    # Positioning image
    label9.place(x=90, y=30)
    # -----------------
    # Status
    # -----------------
    img10 = ImageTk.PhotoImage(Image.open("status.png"))
    label10 = Label(newWindow, image=img10)
    label10.pack()
    # Positioning image
    label10.place(x=600, y=100)
    # -----------------
    # Little girl icon
    # -----------------
    img11 = ImageTk.PhotoImage(Image.open("icon.png"))
    label11 = Label(newWindow, image=img11)
    label11.pack()
    # Positioning image
    label11.place(x=735, y=330)

    def onClick():
        labxl = tk.Label(newWindow, text="Clock in button clicked", font=("Times", 12))
        labxl.pack()
        labxl.place(x=602, y=180)
        pys.speak(text="Clock in button clicked")

    def offClick():
        labxl1 = tk.Label(newWindow, text="Clock out button clicked", font=("Times", 12))
        labxl1.pack()
        labxl1.place(x=602, y=180)
        pys.speak(text="Clock out button clicked")

    def time():
        timz = datetime.now()
        timetString = timz.strftime('%H:%M:%S')
        labxl2 = tk.Label(newWindow, text=timetString, font=("Times", 12))
        labxl2.pack()
        labxl2.place(x=90, y=400)
        # pys.speak("Your name and ID is" + namee)
        # pys.speak("The time right now is" + timetString)

        labxl3 = tk.Label(newWindow, text=namee, font=("Times", 12))
        labxl3.pack()
        labxl3.place(x=90, y=190)

    # -----------------
    # Clock in
    # -----------------
    def thing():
        label4.config(text="You clicked me...")

    clockin = PhotoImage(file="clockin.png")

    img_label6 = Label(image=clockin)
    # img_label6.pack(pady=0)
    # img_label6.place(x=50, y=300)
    global clinbutton
    clinbutton = Button(newWindow, image=clockin, command=lambda: [live_camera(), onClick(), time()])
    clinbutton.pack(pady=0)
    clinbutton.place(x=610, y=300)

    img_label6 = Label(root, text="")
    img_label6.pack(pady=0)

    # -----------------
    # Clock out
    # -----------------
    def thing():
        label4.config(text="You clicked me...")

    clockout = PhotoImage(file="clockout.png")

    img_label7 = Label(image=clockout)
    # img_label7.pack(pady=0)
    # img_label7.place(x=50, y=300)

    cloutbutton = Button(newWindow, image=clockout, command=lambda: [live_camera(), offClick(), time()])
    cloutbutton.pack(pady=0)
    cloutbutton.place(x=610, y=360)

    img_label7 = Label(root, text="")
    img_label7.pack(pady=0)

    newWindow.mainloop()

# ------------------------
# Capture button
# ---------------------------
def thing():
    label3.config(text="You clicked me...")


capture = PhotoImage(file="capture.png")

img_label2 = Label(image=capture)
# img_label2.pack(pady=0)
# img_label2.place(x=500, y=80)
capbutton = Button(root, image=capture, command=createNewWindow)
capbutton.pack(pady=0)
capbutton.place(x=500, y=80)

img_label2 = Label(root, text="")
img_label2.pack(pady=0)

# -------------------------
# Creating a new window for Add button
# -------------------------
def createNewWindow3():
    newWindow4 = tk.Toplevel(root)
    #buttonExample4 = tk.Button(newWindow4, text='addbutton', command=createNewWindow3)

    newWindow4.title("Add a profile")
    newWindow4.geometry("845x510")

    #buttonExample4.pack(side='top')
    newWindow4['bg'] = 'white'

    # -----------------
    # Title
    # -----------------
    img20 = ImageTk.PhotoImage(Image.open("title.png"))
    label20 = Label(newWindow4, image=img20)
    label20.pack()
    # Positioning image
    label20.place(x=90, y=40)

    # ---------------
    # Take image button
    # ---------------

    def Camera():
        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        while (result):
            ret, frame = videoCaptureObject.read()
            value = text_box.get('1.0', '1.end')
            id = text_box1.get('1.0', '1.end')
            cv2.imwrite("Images Attendance/" + value + '_' + id+ ".png", frame)
            result = False
        videoCaptureObject.release()
        cv2.destroyAllWindows()

    def thing():
        label5.config(text="You clicked me...")

    take = PhotoImage(file="Take image.png")

    img_label9 = Label(image=take)
    # img_label7.pack(pady=0)
    # img_label7.place(x=50, y=300)

    tkbutton = Button(newWindow4, image=take, command=Camera)
    tkbutton.pack(pady=0)
    tkbutton.place(x=340, y=260)

    img_label9 = Label(root, text="")
    img_label9.pack(pady=0)

    # ---------------
    # Enter name textbox
    # ---------------
    img21 = ImageTk.PhotoImage(Image.open("entername.png"))
    label21 = Label(newWindow4, image=img21)
    label21.pack()
    # Positioning image
    label21.place(x=80, y=120)

    # Textbox
    text_box = Text(newWindow4, height=2.3, width=20)
    text_box.pack(expand=True)
    text_box.place(x=170, y=160)
    text_box.config(state='normal')

    # ---------------
    # Enter ID textbox
    # ---------------
    img22 = ImageTk.PhotoImage(Image.open("enterid.png"))
    label22 = Label(newWindow4, image=img22)
    label22.pack()
    # Positioning image
    label22.place(x=500, y=120)

    # Textbox
    text_box1 = Text(newWindow4, height=2.3, width=20)
    text_box1.pack(expand=True)
    text_box1.place(x=590, y=160)
    text_box1.config(state='normal')

    newWindow4.mainloop()

# ----------------------
# Add/Remove button
# ----------------------
def thing():
    label3.config(text="You clicked me...")


add = PhotoImage(file="add.png")

img_label4 = Label(image=add)
# img_label4.pack(pady=0)
# img_label4.place(x=640, y=81)

addbutton = Button(root, image=add, command=createNewWindow3)
addbutton.pack(pady=0)
addbutton.place(x=570, y=80)

img_label4 = Label(root, text="")
img_label4.pack(pady=0)


# -------------------------
# Creating a new window for help button
# -------------------------
def createNewWindow1():
    newWindow2 = tk.Toplevel(root)
    #buttonExample2 = tk.Button(newWindow2, text='helpbutton', command=createNewWindow1)

    newWindow2.title("Help Page")
    newWindow2.geometry("845x510")

    #buttonExample2.pack(side='top')
    newWindow2['bg'] = 'white'

    # -----------------
    # Stop everything? help1
    # -----------------
    img12 = ImageTk.PhotoImage(Image.open("help1.png"))
    label12 = Label(newWindow2, image=img12)
    label12.pack()
    # Positioning image
    label12.place(x=30, y=120)

    # -----------------
    # Title
    # -----------------
    img13 = ImageTk.PhotoImage(Image.open("title.png"))
    label13 = Label(newWindow2, image=img13)
    label13.pack()
    # Positioning image
    label13.place(x=90, y=40)

    # -----------------
    # App is not working? help2
    # -----------------
    img14 = ImageTk.PhotoImage(Image.open("help2.png"))
    label14 = Label(newWindow2, image=img14)
    label14.pack()
    # Positioning image
    label14.place(x=300, y=120)

    # -----------------
    # What is Modify button? help3
    # -----------------
    img15 = ImageTk.PhotoImage(Image.open("help3.png"))
    label15 = Label(newWindow2, image=img15)
    label15.pack()
    # Positioning image
    label15.place(x=570, y=120)

    # -----------------
    # Camera not working? help4
    # -----------------
    img16 = ImageTk.PhotoImage(Image.open("help4.png"))
    label16 = Label(newWindow2, image=img16)
    label16.pack()
    # Positioning image
    label16.place(x=30, y=300)

    # -----------------
    # My name exists help5
    # -----------------
    img17 = ImageTk.PhotoImage(Image.open("help5.png"))
    label17 = Label(newWindow2, image=img17)
    label17.pack()
    # Positioning image
    label17.place(x=300, y=300)

    # -----------------
    # What is Add button? help6
    # -----------------
    img18 = ImageTk.PhotoImage(Image.open("help6.png"))
    label18 = Label(newWindow2, image=img18)
    label18.pack()
    # Positioning image
    label18.place(x=570, y=300)

    newWindow2.mainloop()


# -------------------------
# Help button
# -------------------------
def thing():
    label3.config(text="You clicked me...")


helps = PhotoImage(file="help.png")

img_label5 = Label(image=helps)
# img_label5.pack(pady=0)
# img_label5.place(x=710, y=81)

helpbutton = Button(root, image=helps, command=createNewWindow1)
helpbutton.pack(pady=0)
helpbutton.place(x=640, y=80)

img_label5 = Label(root, text="")
img_label5.pack(pady=0)

# ----------------------------
# To see the GUI screen
root.mainloop()