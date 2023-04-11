import tkinter as tk
import customtkinter as ct

ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")
root = ct.CTk()
root.title("Cinema Booking")
root.geometry("950x650")

welcome_label = ct.CTkLabel(root,
                            text="Welcome to Cinema Booking Service",
                            font=("Source Sans Pro", 22, "bold", "underline"))
welcome_label.pack()


def genrate_ticket(place, center, movie, screen, seat, time):

    farewell_label = ct.CTkLabel(root,
                                 text=f"Enjoy {movie} 🎬 at {center} Cinemas",
                                 font=("Source Sans Pro", 22, "bold"),
                                 text_color="#0fc5dd")
    farewell_label.pack()
    price = 0
    if screen == "Silver : ₹150":
        price = 150
    elif screen == "Gold : ₹350":
        price = 350
    elif screen == "Platinum : ₹500":
        price = 500

    total = price * int(seat)
    frame = ct.CTkFrame(root)
    frame.pack()

    listbox = tk.Listbox(frame)
    listbox.pack()

    ticket_details = {
        "City": place,
        "Center": center,
        "Movie": movie,
        "Screen": screen,
        "Seats": seat,
        "Time": time,
        "Total Fare": total
    }
    for key, value in ticket_details.items():
        listbox.insert(tk.END, f"{key}: {value}")


start = ct.CTkLabel(root,
                    text=" Book Movie Ticket 🎟️",
                    font=("Source Sans Pro", 25, "bold"),
                    text_color="yellow")
start.pack(padx=12, pady=10)

place = tk.StringVar(value="Select City")
City_but = ct.CTkOptionMenu(root,
                            variable=place,
                            values=["Ahmedabad", "Surat", "Rajkot"],
                            dropdown_font=("Source Sans Pro", 13, "bold"),
                            dropdown_hover_color="#808080")
City_but.pack(padx=10, pady=10)

center = tk.StringVar(value="Select Center")
cent_but = ct.CTkOptionMenu(root,
                            variable=center,
                            values=["Inox", "NY", "PVR"],
                            dropdown_font=("Source Sans Pro", 13, "bold"))
cent_but.pack(padx=10, pady=10)

movie = tk.StringVar(value="Select Movie")
movie_items = ct.CTkOptionMenu(root,
                               variable=movie,
                               values=["Avatar2", "Pathan", "Chello Divas"],
                               dropdown_font=("Source Sans Pro", 13, "bold"))
movie_items.pack(padx=10, pady=10)

screen = tk.StringVar(value="Select Screen")
Screens = ct.CTkOptionMenu(
    root,
    variable=screen,
    values=["Silver : ₹150 ", "Gold : ₹350", "Platinum : ₹500"],
    dropdown_font=("Source Sans Pro", 13, "bold"))
Screens.pack(pady=10, padx=10)

seat = tk.StringVar(value="Select seat")
seat_option = ct.CTkOptionMenu(root,
                               variable=seat,
                               values=["1", "2", "3", "4", "5"],
                               dropdown_font=("Source Sans Pro", 13, "bold"))
seat_option.pack(pady=10, padx=10)

time = tk.StringVar(value="Select Time:")
time_option = ct.CTkOptionMenu(
    root,
    variable=time,
    values=["10:00-1:00", "1:10-4:10", "4:20-7:20", "7:30-10:30"],
    dropdown_font=("Source Sans Pro", 13, "bold"))
time_option.pack(pady=10, padx=10)

Genrate = ct.CTkButton(root,
                       text="Genrate ticket",
                       font=("Source Sans Pro", 13, "bold"),
                       command=lambda: genrate_ticket(place.get(), center.get(
                       ), movie.get(), screen.get(), seat.get(), time.get()))
Genrate.pack()

root.mainloop()