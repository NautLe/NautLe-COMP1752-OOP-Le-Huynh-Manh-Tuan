import tkinter as tk
from tkinter import ttk
import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideoList
from update_videos import UpdateVideos

def check_videos_clicked():
    status_lbl.configure(text="Checking videos...")
    CheckVideos(tk.Toplevel(window))
    status_lbl.configure(text="")

def create_video_list_clicked():
    status_lbl.configure(text="Creating video list...")
    CreateVideoList(tk.Toplevel(window))
    status_lbl.configure(text="")

def update_videos_clicked():
    status_lbl.configure(text="Updating videos...")
    UpdateVideos(tk.Toplevel(window), window)
    status_lbl.configure(text="")

# Set up the main window
window = tk.Tk()
window.geometry("800x250")
window.title("Video Player")

# Apply custom fonts
fonts.configure()

# Style configurations
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 14))
style.configure('TButton', font=('Helvetica', 12), padding=10)

# Header label
header_lbl = ttk.Label(window, text="Select an option by clicking one of the buttons below", style='TLabel')
header_lbl.pack(pady=20)

# Buttons frame
buttons_frame = tk.Frame(window)
buttons_frame.pack(pady=10)

# Buttons
check_videos_btn = ttk.Button(buttons_frame, text="Check Videos", command=check_videos_clicked, width=20)
check_videos_btn.grid(row=0, column=0, padx=10)

create_video_list_btn = ttk.Button(buttons_frame, text="Create Video List", command=create_video_list_clicked, width=20)
create_video_list_btn.grid(row=0, column=1, padx=10)

update_videos_btn = ttk.Button(buttons_frame, text="Update Videos", command=update_videos_clicked, width=20)
update_videos_btn.grid(row=0, column=2, padx=10)

# Status label
status_lbl = ttk.Label(window, text="", style='TLabel')
status_lbl.pack(pady=20)

# Start the main loop
window.mainloop()
