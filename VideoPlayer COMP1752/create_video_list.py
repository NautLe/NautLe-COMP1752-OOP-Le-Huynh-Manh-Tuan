import csv
import tkinter as tk
from tkinter import ttk,filedialog
from PIL import Image, ImageTk
import os
import library_item as lib
import video_library as lib
import font_manager as fonts
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb


class CreateVideoList():
    def __init__(self, window):
        self.window = window
        self.window.geometry('1200x850')
        self.window.title('Create Video List')
        self.playlist = []
        self.window.configure(bg='#f0f0f0') 

        


         # Main Buttons
        self.back_to_menu_btn = tk.Button(self.window, text="Back to Menu", width=11, command=self.back_to_menu, bg='#d1e7dd', fg='#0d6efd')
        self.back_to_menu_btn.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        # Video List and Information Frame
        self.video_list_info_frame = tk.Frame(self.window, borderwidth=5, relief="sunken")
        self.video_list_info_frame.grid(row=1, column=0, columnspan=5, rowspan=6, padx=10, pady=10, sticky="nsew")

        # Upper - Video List
        self.lbl_list = ttk.Label(self.video_list_info_frame, text='Video List', background='#e2e3e5')
        self.lbl_list.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.video_listbox = tk.Listbox(self.video_list_info_frame, width=55, height=10, selectmode=tk.SINGLE)
        self.video_listbox.grid(row=1, column=0, columnspan=3, rowspan=5, sticky="W", padx=10, pady=10)
        self.video_listbox.bind("<<ListboxSelect>>", self.video_item_selected)

        # Video Information Frame
        self.cover_photo = tk.Label(self.video_list_info_frame, text='Video Information', background='#e2e3e5')
        self.cover_photo.grid(row=0, column=4, columnspan=3, padx=10, pady=10)

        self.video_info_frame = tk.Frame(self.video_list_info_frame, borderwidth=5, relief="groove", bg='#f8d7da')  # Set background color for the frame
        self.video_info_frame.grid(row=1, column=3, columnspan=5, rowspan=5, padx=10, pady=10, sticky="nsew")

        self.video_name_frame = ttk.Frame(self.video_info_frame)
        self.video_name_frame.grid(row=1, column=1, rowspan=3, padx=10, pady=10, sticky="W")

        self.cover_frame = ttk.Frame(self.video_info_frame, borderwidth=5, relief="raised")
        self.cover_frame.grid(row=1, column=3, columnspan=4, rowspan=3, padx=10, pady=10, sticky='e')

        self.cover_photo_label = tk.Label(self.cover_frame, bg='#f8f9fa')  # Set background color for the cover photo label
        self.cover_photo_label.grid(row=0, column=0)

        self.video_name_label = tkst.ScrolledText(self.video_name_frame, width=20, height=12, wrap="word", bg='#ffffff', fg='#495057')  # Set colors for the ScrolledText
        self.video_name_label.grid(row=1, column=5, padx=10, pady=10)

        self.video_name_label.config(width=27)

        self.error_label = tk.Label(self.window, text="", font=("Helvetica", 10), fg="red", bg='#f0f0f0')  # Set background color of the window and text color to red
        self.error_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.window)
        self.notebook.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

        self.create_playlist_tab()
        

        # Display video list
        self.list_videos_clicked()

    

    
    def create_playlist_tab(self):
        #PLAYLIST TAB
        playlist_frame = ttk.Frame(self.notebook)
        self.notebook.add(playlist_frame, text='Playlist', padding=5)

        #PLAYLIST WIDGET
        self.lbl_playlist = tk.Label(playlist_frame, text='Playlist',background='#e2e3e5')
        self.lbl_playlist.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.playlist_listbox = tk.Listbox(playlist_frame, width=55, height=10, selectmode=tk.SINGLE,background='#e2e3e5')
        self.playlist_listbox.grid(row=1, column=0, columnspan=2, rowspan=5, sticky="W", padx=10, pady=10)
        self.playlist_listbox.bind("<<ListboxSelect>>", self.video_item_selected)

        self.add_to_playlist_btn = tk.Button(playlist_frame, text="Add to Playlist", width=18, command=self.add_to_playlist, bg='#d1e7dd', fg='#0d6efd')
        self.add_to_playlist_btn.grid(row=2, column=3, padx=10, pady=10)

        self.play_playlist_btn = tk.Button(playlist_frame, text="Play Playlist", width=18, command=self.play_playlist, bg='#d1e7dd', fg='#0d6efd')
        self.play_playlist_btn.grid(row=3, column=3, padx=10, pady=10)

        self.remove_from_playlist_btn = tk.Button(playlist_frame, text="Remove from Playlist", width=18, command=self.remove_from_playlist, bg='#d1e7dd', fg='#0d6efd')
        self.remove_from_playlist_btn.grid(row=4, column=3, padx=10, pady=10)

        self.clear_playlist_btn = tk.Button(playlist_frame, text="Clear Playlist", width=18, command=self.clear_playlist, bg='#d1e7dd', fg='#0d6efd')
        self.clear_playlist_btn.grid(row=4, column=4, padx=10, pady=10)

        self.save_playlist_btn = tk.Button(playlist_frame, text="Save Playlist", width=18, command=self.save_playlist, bg='#d1e7dd', fg='#0d6efd')
        self.save_playlist_btn.grid(row=2, column=4, padx=10, pady=10)

        self.load_playlist_btn = tk.Button(playlist_frame, text="Load Playlist", width=18, command=self.load_playlist, bg='#d1e7dd', fg='#0d6efd')
        self.load_playlist_btn.grid(row=3, column=4, padx=10, pady=10)

        self.vid_num_frame = ttk.Frame(playlist_frame, borderwidth=5, relief='ridge')
        self.vid_num_frame.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

        self.lbl_vid_num = tk.Label(self.vid_num_frame, text='Video Number')
        self.lbl_vid_num.grid(row=0, column=1, padx=10, pady=10)

        self.txt_vid_num = tk.Entry(self.vid_num_frame, width=10)  # entry box to enter video number to be added to playlist
        self.txt_vid_num.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        self.total_duration = 0

        self.total_duration_var = tk.StringVar()
        self.total_duration_label = tk.Label(playlist_frame, textvariable=self.total_duration_var, font=("Helvetica", 15), fg="red")  # Set text color to red
        self.total_duration_label.grid(row=0, column=3, columnspan=3, padx=10, pady=10)

        self.update_total_duration()


   


    def save_playlist(self):
        if self.playlist == []: #If the playlist is empty
            msb.showerror('Error', 'Playlist is empty')
            return
        else:
            file_path = tk.filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")]) 
            with open(file_path, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                # Write the header row
                csv_writer.writerow(['Video Number', 'Video Name', 'Video Director'])
                # Write each playlist item to the CSV file
                for playlist_item in self.playlist_listbox.get(0, tk.END):
                    video_number = playlist_item.split(' ')[0]
                    video_name = lib.get_name(video_number)
                    video_director = lib.get_director(video_number)
                    csv_writer.writerow([video_number, video_name, video_director])# Write the video information to the CSV file
            msb.showinfo('Success', 'Playlist saved successfully')
            print(f"Playlist saved to {file_path}")


    def load_playlist(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return  # If the user cancels the dialog, return immediately

        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader, None)  # Skip the header row
            
            for row in csv_reader:
                video_number, video_name, video_director = row
                playlist_item = f"{video_number} - {video_name} - {video_director}"
                
                # Check if the video number is already in the playlist
                if video_number not in self.playlist:
                    self.playlist.append(video_number)  # Add to the playlist
                    self.playlist_listbox.insert(tk.END, playlist_item)  # Insert into the Listbox
                    
                    # Update the total duration
                    video_duration = lib.get_duration(video_number)
                    self.total_duration += video_duration
            
            # Update the total duration display
            self.update_total_duration()

        msb.showinfo('Success', 'Playlist loaded and updated successfully')




    def back_to_menu(self):
        self.window.destroy()  # Close the current window




    def remove_from_playlist(self):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:  #If an item is selected in the playlist_listbox
            removed_item = self.playlist_listbox.get(selected_index)
            video_number = removed_item.split(' ')[0]
            video_duration = lib.get_duration(video_number)
            # Subtract the duration of the removed video
            self.total_duration -= video_duration
            # Update the total duration label
            self.update_total_duration()
            # Remove the video_number from the playlist
            self.playlist.remove(video_number)
            # Remove the item from the playlist_listbox
            self.playlist_listbox.delete(selected_index)
            msb.showinfo('Success', f'Removed video {video_number} - {lib.get_name(video_number)} - {lib.get_director(video_number)} from Playlist')
        else:  # If no item is selected in the playlist_listbox
            msb.showerror('Error', 'Please select a video from the playlist')


    def play_playlist(self):
        if self.playlist == []:
            msb.showerror('Error', 'Playlist is empty')
        else:
            for playlist_item in self.playlist_listbox.get(0, tk.END): 
                video_number = playlist_item.split()[0] # Extract the video number from the playlist item by splitting the string into substring such as [video_number, - , video_name, - , video_director] and taking the first part of the resulting list.
                lib.increment_play_count(video_number)
                msb.showinfo("Success", f"Playing video {video_number} - Play count: {lib.get_play_count(video_number)}")


    def update_total_duration(self):
        result = divmod(self.total_duration, 60) # Calculate the total duration in hours and minutes
        hours = result[0] #get the first index of the result
        minutes = result[1] # get the second index of the result
        self.total_duration_var.set(f"Total Duration: {hours} hours {minutes} minutes") # Update the total duration label



    def add_to_playlist(self):
        try:
            # Check if an item is selected in the video_listbox
            if self.video_listbox.curselection():
                video_number = self.video_list[self.video_listbox.curselection()[0]]
            else:
                # If no video is selected from the listbox, use the video number from the entry field instead.
                video_number = self.txt_vid_num.get().strip()

            # Check if the entered video number exists in the video library
            if video_number not in lib.library:
                msb.showerror("Error", "Video number does not exist in video library")
                return

            # Check if the video number is already in the playlist
            if video_number in self.playlist:
                msb.showerror("Error", "Video already in playlist")
                return

            # Add video number to the playlist
            self.playlist.append(video_number)
            
            # Get video duration and update the total duration
            video_duration = lib.get_duration(video_number)
            self.total_duration += video_duration
            self.update_total_duration()
            
            # Update the playlist listbox information
            self.update_playlist_text()
            msb.showinfo('Success', 'Video added to playlist successfully')

        except ValueError:
            msb.showerror("Error", "Invalid video number. Please enter a valid integer.")
        
        except IndexError:
            msb.showerror("Error", "No video selected from the listbox.")

    def display_cover_photo(self, video_number):
        script_directory = "C:\\Users\\ADMIN\\Desktop\\VideoPlayer COMP1752" 
        cover_photo_path = script_directory + '\\' + "covers" + '\\' + str(video_number) + '.jpg' # Construct the path to the cover photo
        try:
            image = Image.open(cover_photo_path) # Open the cover photo
            image.thumbnail((150, 200))  # Resize the cover photo
        except FileNotFoundError as e: # If the cover photo is not found
            msb.showerror('Error', f"Cover photo not found for video number {video_number}")
            return
        photo = ImageTk.PhotoImage(image)# Convert the Image object to a PhotoImage object
        self.cover_photo_label.config(image=photo, width=150, height=200)# Update the PhotoImage of the cover photo label
        self.cover_photo_label.image = photo # Update the PhotoImage each time the cover photo label is updated



    def update_playlist_text(self):
        video_number = self.playlist[-1]  # Get the last video number in the playlist
        video_name = lib.get_name(str(video_number))  # Convert video_number to a string
        video_director = lib.get_director(str(video_number))  # Convert video_number to a string
        self.playlist_listbox.insert(tk.END, f'{video_number} - {video_name} - {video_director}')  # Add the video to the playlist


    def clear_playlist(self):
        if not self.playlist:  # Check if the playlist is empty
            msb.showerror('Error', 'Playlist is already empty')
        else:
            self.playlist = []  # Reset the self.playlist list to an empty list
            self.playlist_listbox.delete(0, tk.END)  # Delete all items in the Listbox
            self.total_duration = 0  # Set the total duration back to zero and update the total duration label in the UI
            self.update_total_duration() 
            self.video_listbox.selection_clear(0, tk.END)  # Clear any selection in the video listbox
            msb.showinfo('Success', 'Playlist cleared')




    def show_video_info(self, video_number):
        try:
            # Retrieve LibraryItem based on the video number
            video_item = lib.library[video_number]
            # Create a string with video information
            info_text = f"Name: {video_item.name}\n\n"
            info_text += f"Director: {video_item.director}\n\n"
            info_text += f"Rating: {video_item.stars()} ({video_item.rating})\n\n"
            info_text += f"Play Count: {video_item.play_count}\n\n"
            # # Assuming duration is available in LibraryItem, adjust as needed
            info_text += f"Duration: {video_item.duration} minutes\n\n"
            info_text += f"Short Description: {video_item.short_description}"
            # Set the text in the video_name_label (ScrolledText)
            self.video_name_label.delete(1.0, tk.END)  # Clear existing text
            self.video_name_label.insert(tk.END, info_text)
            self.display_cover_photo(video_number)
        except KeyError:
            msb.showerror('Error', f"Video not found for number {video_number}")


    def list_videos_clicked(self):
        video_list = lib.library.keys()  # Get a list of all video numbers
        self.video_listbox.delete(0, tk.END)  # Clear the video_listbox
        self.video_list = list(video_list)  # Convert video_list to a list
        for video_number in video_list:  
            video_name = lib.get_name(str(video_number)) 
            video_director = lib.get_director(str(video_number))
            star_rating = lib.library[video_number].stars()
            self.video_listbox.insert(tk.END, f'{video_number} - {video_name} - {video_director} - Rating: {star_rating}')


    

    def video_item_selected(self, event):
        selected_index_video_list = self.video_listbox.curselection()
        selected_index_playlist = self.playlist_listbox.curselection()
        
        if selected_index_video_list:
            selected_video_number = self.video_list[selected_index_video_list[0]]
            self.txt_vid_num.delete(0, tk.END)  # Clear the entry field
            self.txt_vid_num.insert(0, selected_video_number)  # Insert the selected video number
            self.show_video_info(selected_video_number)
            
        elif selected_index_playlist:
            selected_playlist_item = self.playlist_listbox.get(selected_index_playlist[0])
            selected_video_number = selected_playlist_item.split(' ')[0]
            self.txt_vid_num.delete(0, tk.END)  # Clear the entry field
            self.txt_vid_num.insert(0, selected_video_number)  # Insert the selected video number
            self.show_video_info(selected_video_number)

            


if __name__ == "__main__":
    window = tk.Tk()    
    fonts.configure()
    CreateVideoList(window)
    window.mainloop()