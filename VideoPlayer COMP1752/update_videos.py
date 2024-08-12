import tkinter as tk
from tkinter import messagebox as msb
import font_manager as fonts
import video_library as lib

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateVideos:
    def __init__(self, window, main_menu_window):
        self.window = window
        self.main_menu_window = main_menu_window
        self.window.geometry("800x400")
        self.window.title("Update Videos")
        self.window.configure(bg="#f0f0f0")

        self.__create_widgets() 
        self.__display_all_videos()  # Display all videos when the window is opened

    def __create_widgets(self):
        self.__title = tk.Label(self.window, text="Update Video Information", font=("Helvetica", 16, "bold"), bg="#34495e", fg="white")
        self.__title.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="ew")

        self.__lbl_vid_number = tk.Label(self.window, text="Enter Video Number", font=("Helvetica", 12), bg="#f0f0f0")
        self.__lbl_vid_number.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        self.__txt_vid_number = tk.Entry(self.window, width=5, font=("Helvetica", 12))
        self.__txt_vid_number.grid(row=1, column=1, padx=10, pady=10)

        self.__btn_check = tk.Button(self.window, text="Check", command=self.check_video_clicked, font=("Helvetica", 12), bg="#3498db", fg="white")
        self.__btn_check.grid(row=1, column=2, padx=10, pady=10)

        self.__lbl_new_rating = tk.Label(self.window, text="Enter New Rating", font=("Helvetica", 12), bg="#f0f0f0")
        self.__lbl_new_rating.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        self.__txt_new_rating = tk.Entry(self.window, width=5, font=("Helvetica", 12))
        self.__txt_new_rating.grid(row=2, column=1, padx=10, pady=10)

        self.__btn_update = tk.Button(self.window, text="Update", command=self.update_video_clicked, font=("Helvetica", 12), bg="#e67e22", fg="white")
        self.__btn_update.grid(row=2, column=2, padx=10, pady=10)

        self.video_txt = tk.Text(self.window, width=50, height=8, wrap="word", font=("Helvetica", 12))
        self.video_txt.grid(row=1, column=3, rowspan=2, padx=10, pady=10, sticky="NW")

        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10), bg="#f0f0f0")
        self.status_lbl.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        self.__btn_back = tk.Button(self.window, text="Back to Menu", command=self.go_back_to_menu, font=("Helvetica", 12), bg="#95a5a6", fg="white")
        self.__btn_back.grid(row=4, column=0, columnspan=4, pady=20)

    def go_back_to_menu(self):
        self.window.destroy()  # Close the update window
        self.main_menu_window.deiconify()  # Show the main menu window

    def check_video_clicked(self):
        key = self.__txt_vid_number.get()

        if not key.isdigit() or int(key) <= 0:
            msb.showerror("Error", "Please enter a valid positive integer for the video number")
            return

        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"Name: {name}\nDirector: {director}\nRating: {rating}\nPlays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            msb.showerror("Error", "Video not found")

    def update_video_clicked(self):
        video_number = self.__txt_vid_number.get()
        new_rating = self.__txt_new_rating.get()

        if not video_number.isdigit() or int(video_number) <= 0:
            msb.showerror("Error", "Please enter a valid positive integer for the video number")
            return

        if not new_rating:
            msb.showerror("Error", "Please enter a new rating")
            return

        try:
            new_rating = int(new_rating)
        except ValueError:
            msb.showerror("Error", "New rating must be a valid number")
            return

        if not (1 <= new_rating <= 5):
            msb.showerror("Error", "Rating must be between 1 and 5")
            return

        current_rating = lib.get_rating(video_number)

        if current_rating is not None:
            lib.set_rating(video_number, new_rating)
            msb.showinfo("Success", "Video updated successfully!")

            # Refresh the displayed information after update
            director = lib.get_director(video_number)
            play_count = lib.get_play_count(video_number)
            video_details = f"Name: {lib.get_name(video_number)}\nDirector: {director}\nRating: {new_rating}\nPlays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            msb.showerror("Error", f"Video {video_number} not found")

        self.__txt_vid_number.delete(0, tk.END)
        self.__txt_new_rating.delete(0, tk.END)

    def __display_all_videos(self):
        all_videos = lib.list_all()
        set_text(self.video_txt, all_videos)
