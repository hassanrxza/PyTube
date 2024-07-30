import tkinter
import customtkinter
from pytube import YouTube

hiddenimports = ["Tkinter", "pytube", "customtkinter"]


def start_download():
    try:
        ytLink = link.get()
        ytObj = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObj.streams.get_highest_resolution()
        video.download()
        title_label.configure(text=ytObj.title, text_color="white")
        finishlabel.configure(text="Download Complete!", text_color="green")
    except:
        finishlabel.configure(text="Downloading Error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))

    progress_percentage.configure(text=per + "%")
    progress_percentage.update()

    progressBar.set(float(percentage_of_completion) / 100)


# System Settings

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme("blue")

# App Frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Creating Label

title_label = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title_label.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finish Label

finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

# Progress Percentage Label and Bar

progress_percentage = customtkinter.CTkLabel(app, text="0%", text_color="white")
progress_percentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button

button = customtkinter.CTkButton(app, text="Download", command=start_download)
button.pack(padx=10, pady=10)

# Make sure App not closes

app.mainloop()
