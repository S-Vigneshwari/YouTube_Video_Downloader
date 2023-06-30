from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror, showinfo
from pytube import YouTube


def download():
    video_link = link_entry.get()
    if not video_link:
        showerror("Error", "Please enter a video link.")
        return

    save_path = askdirectory(title='Select Folder')
    download_type = file_type.get()
    resolution = resolution_var.get()

    try:
        video = YouTube(video_link)
        if download_type == "audio":
            file = video.streams.filter(only_audio=True).first()
        else:
            file = video.streams.filter(resolution=resolution).first()

        file.download(save_path)
        showinfo("Download Completed", f"{download_type} Downloaded!")
    except:
        showerror("Error", "Unable to download video at this moment.")


bg_color = "#aaddff"
root = Tk()
root.geometry("450x300")
root.resizable(0, 0)
root.configure(bg=bg_color)
root.title("YT Downloader")

label_title = Label(root, text="YouTube Downloader", bg=bg_color, font=("Arial", 15, "bold"), fg="#00008B")
label_title.pack(pady=10)

frame = Frame(root, pady=20, bg=bg_color, height=150)
frame.pack(fill="both")

link_entry = Entry(frame)
link_entry.place(anchor="c", relx=.5, rely=0.0, relheight=0.3, relwidth=0.8)

label_file_type = Label(frame, text="File Type", bg=bg_color)
label_file_type.place(anchor="c", relx=.25, rely=.325)

file_type = StringVar()
file_type.set("Video")
option_menu_file_type = OptionMenu(frame, file_type, "Video", "Audio")
option_menu_file_type.place(anchor="c", relx=.25, rely=.575)

label_resolution = Label(frame, text="Resolution", bg=bg_color)
label_resolution.place(anchor="c", relx=.75, rely=.325)

resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p"]
resolution_var = StringVar()
resolution_var.set(resolutions[-2])
option_menu_resolution = OptionMenu(frame, resolution_var, *resolutions)
option_menu_resolution.place(anchor="c", relx=.75, rely=.575)

button_download = Button(root, command=download, text="DOWNLOAD", font=("Arial", 10, "bold"))
button_download.place(in_=frame, anchor="c", relx=.5, rely=.9, relheight=0.3)

root.mainloop()

