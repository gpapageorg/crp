import customtkinter
import stations
import player
import tkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        
        self.title("Custom Radio Player")
        self.geometry(f"{800}x280")
        self.resizable(False,False)

        self.icon_image = tkinter.PhotoImage(file="radio.png")
        self.iconphoto(False, self.icon_image)


        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Custom\nRadio Player", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Play", command=self.play_station)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Pause", command=self.pause_station)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        
        # self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Hide", command=self.hide)
        # self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=50)

        # create main frame for station display and volume control
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, columnspan=3, rowspan=4, sticky="nsew")
        self.main_frame.grid_rowconfigure(4, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        self.station_var = tkinter.StringVar(value="No station playing")
        self.station_label = customtkinter.CTkLabel(self.main_frame, textvariable=self.station_var, font=customtkinter.CTkFont(size=20, weight="bold"))
        self.station_label.grid(row=0, column=1, padx=20, pady=(20, 10))

        self.volume_label = customtkinter.CTkLabel(self.main_frame, text="Volume", font=customtkinter.CTkFont(size=15),)
        self.volume_label.grid(row=1, column=0, padx=20, pady=(20, 10))

        self.volume_slider = customtkinter.CTkSlider(self.main_frame, from_=0, to=100, command=self.set_volume)
        self.volume_slider.set(90)
        self.volume_slider.grid(row=1, column=1, padx=20, pady=(20, 10), sticky="ew")

        self.station_menu_label = customtkinter.CTkLabel(self.main_frame, text="Select Station:", font=customtkinter.CTkFont(size=15))
        self.station_menu_label.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="ew")

        self.stations = stations.stations
        self.station_menu = customtkinter.CTkOptionMenu(self.main_frame, values=list(self.stations.keys()), command=self.change_station)
        self.station_menu.grid(row=2, column=1, padx=20, pady=(20, 10), sticky="ew")

        self.play_station()
        

    def play_station(self):
        current_station = self.station_menu.get()
        self.station_var.set(f"Playing {current_station}...")
        self.player = player.Player(stations.stations[str(self.station_menu.get())])
        self.player.play()
       

    def pause_station(self):
        current_station = self.station_menu.get()
        self.station_var.set(f"{current_station} paused.")
        self.player.pause()

    def stop_station(self):
        self.station_var.set("No station playing.")
        self.pause_station()
        del self.player

    def set_volume(self, value):
        # For now, just print the volume level
        #print(f"Volume set to: {value}")
        self.player.setVolume(int(value))

    def change_station(self, station: str):
        self.station_var.set(f"Selected {station}")
        self.stop_station()
        self.play_station()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def hide(self):
        # self.protocol("WM_DELETE_WINDOW", self.iconify)
        pass





if __name__ == "__main__":
    app = App()
    app.mainloop()
