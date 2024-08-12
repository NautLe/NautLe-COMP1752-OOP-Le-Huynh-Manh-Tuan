import tkinter as tk  # Import the tkinter module for creating GUI applications
import tkinter.scrolledtext as tkst  # Import ScrolledText widget from tkinter for a scrollable text area
import video_library as lib  # Import custom video library module for video-related operations
import font_manager as fonts  # Import custom font manager module for configuring fonts

# Function to set the content of a text area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear the text area from the first character to the end
    text_area.insert("1.0", content)  # Insert the new content at the beginning of the text area

# Class that defines the GUI for checking videos
class CheckVideos:
    def __init__(self, window):
        # Set the initial size and title of the window
        window.geometry("750x350")  # Set the window size to 750x350 pixels
        window.title("Check Videos")  # Set the window title to "Check Videos"

        # Button to list all videos
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)  # Position the button in the grid layout

        # Label for the video number entry
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # Position the label in the grid layout

        # Input field for entering video numbers with validation
        vcmd = (window.register(self.validate_numeric_input), '%P')  # Register the validation command
        self.input_txt = tk.Entry(window, width=3, validate="key", validatecommand=vcmd)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # Position the input field in the grid layout

        # Button to check the details of a specific video
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)  # Position the button in the grid layout

        # ScrolledText widget to display the list of all videos
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Position in grid layout

        # Text widget to display details of a selected video
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)  # Position in grid layout

        # Label to display the status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)  # Position in grid layout

        # Automatically list all videos when the application starts
        self.list_videos_clicked()

    # Validation function to ensure only numeric input is entered in the video number field
    def validate_numeric_input(self, new_value):
        if new_value.isdigit() or new_value == "":  # Check if the new input is a digit or empty
            return True  # Accept the input
        else:
            return False  # Reject the input

    # Function that gets called when the "Check Video" button is clicked
    def check_video_clicked(self):
        key = self.input_txt.get()  # Get the video number entered by the user
        name = lib.get_name(key)  # Get the name of the video using the video number
        if name is not None:  # Check if the video exists
            director = lib.get_director(key)  # Get the director of the video
            rating = lib.get_rating(key)  # Get the rating of the video
            play_count = lib.get_play_count(key)  # Get the play count of the video
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"  # Format video details
            set_text(self.video_txt, video_details)  # Display the video details in the text area
        else:
            set_text(self.video_txt, f"Video {key} not found")  # Display an error if video not found
        self.status_lbl.configure(text="Check Video button was clicked!")  # Update the status message

    # Function that gets called when the "List All Videos" button is clicked
    def list_videos_clicked(self):
        video_list = lib.list_all()  # Get the list of all videos
        set_text(self.list_txt, video_list)  # Display the video list in the scrollable text area
        self.status_lbl.configure(text="List Videos button was clicked!")  # Update the status message

# Entry point of the application
if __name__ == "__main__":  # This block only runs when the file is executed directly
    window = tk.Tk()  # Create the main Tkinter window
    fonts.configure()  # Configure the fonts using the custom font manager
    CheckVideos(window)  # Create an instance of the CheckVideos class to set up the GUI
    window.mainloop()  # Start the Tkinter main loop to keep the window open
