from tkinter import *
import speedtest

def speedCheck():
    speed = speedtest.Speedtest()
    speed.get_servers()
    down = str(round(speed.download() / (10**6), 3)) + " Mbps"
    up = str(round(speed.upload() / (10**6), 3)) + " Mbps"
    lab_download.config(text=down)
    lab_upload.config(text=up)

speed = Tk()

speed.title("Internet Speed Test")
speed.geometry("500x600")
speed.config(bg="aqua")

# Title Label
lab_title = Label(speed, text="Internet Speed Test", font=("Times New Roman", 25, "bold"), fg="Black", bg="Aqua")
lab_title.place(x=90, y=40, height=50, width=380)

# Download Label
lab_down_text = Label(speed, text="Download Speed", font=("Times New Roman", 20, "bold"), bg="aqua")
lab_down_text.place(x=90, y=130, height=50, width=380)

lab_download = Label(speed, text="00", font=("Times New Roman", 20, "bold"), bg="white")
lab_download.place(x=90, y=200, height=50, width=380)

# Upload Label
lab_up_text = Label(speed, text="Upload Speed", font=("Times New Roman", 20, "bold"), bg="aqua")
lab_up_text.place(x=90, y=290, height=50, width=380)

lab_upload = Label(speed, text="00", font=("Times New Roman", 20, "bold"), bg="white")
lab_upload.place(x=90, y=360, height=30, width=380)

# Button
button = Button(speed, text="Check Speed", font=("Times New Roman", 20, "bold"), relief=RAISED, bg="green", command=speedCheck)
button.place(x=90, y=460, height=50, width=380)

speed.mainloop()


