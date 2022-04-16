import tkinter as tk

window = tk.Tk()


def open_rent_car_window():
    rent_car_window = tk.Toplevel(window)
    rent_car_window.title("Wypożycz Samochód")
    rent_car_window.geometry("200x200")
    tk.Label(rent_car_window,
             text="Tutaj możesz wypożyczyć samochód").pack()
    add_return_button(rent_car_window, window)
    window.iconify()


def hide_main_window(window, main_window):
    main_window.deiconify()
    window.destroy()


def add_return_button(window, main_window):
    return_button = tk.Button(
        window,
        text="Powrót",
        width=7,
        height=1,
        bg="white",
        fg="black",
        command=lambda: hide_main_window(window, main_window)
    )
    return_button.place(x=135, y=170)


def open_add_customer_window():
    add_customer = tk.Toplevel(window)
    add_customer.title("Dodaj Klienta")
    add_customer.geometry("200x200")
    tk.Label(add_customer,
             text="Tutaj możesz dodać klienta").pack()
    add_return_button(add_customer, window)
    window.iconify()


def open_show_customers_window():
    show_customers_window = tk.Toplevel(window)
    show_customers_window.title("Wyświetl klientów")
    show_customers_window.geometry("200x200")
    tk.Label(show_customers_window,
             text="Tutaj możesz wyświetlić klientów").pack()
    add_return_button(show_customers_window, window)
    window.iconify()


def create_main():
    button_frame = tk.Frame()
    title = tk.Label(
        text="Wypożyczalnia Samochodów"
    )

    add_customer_button = tk.Button(
        master=button_frame,
        text="Dodaj Klienta",
        width=15,
        height=5,
        bg="white",
        fg="black",
        command=open_add_customer_window
    )

    show_customer_button = tk.Button(
        master=button_frame,
        text="Wyświetl Klientów",
        width=15,
        height=5,
        bg="white",
        fg="black",
        command=open_show_customers_window
    )

    rent_car_button = tk.Button(
        master=button_frame,
        text="Wypożycz samochód",
        width=15,
        height=5,
        bg="white",
        fg="black",
        command=open_rent_car_window
    )

    add_customer_button.pack(side=tk.LEFT)
    show_customer_button.pack(side=tk.LEFT)
    rent_car_button.pack(side=tk.LEFT)
    title.pack()
    button_frame.pack(fill=tk.X)


create_main()
window.mainloop()
