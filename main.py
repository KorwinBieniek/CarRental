import tkinter as tk
import mysql.connector


def register():
    global screen1
    screen1 = tk.Toplevel(screen)
    screen1.title("Rejestracja")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(screen1, text="Proszę o wprowadzenie danych poniżej").pack()
    tk.Label(screen1, text="").pack()
    tk.Label(screen1, text="Nazwa użytkownika * ").pack()
    username_entry = tk.Entry(screen1, textvariable=username)
    username_entry.pack()
    tk.Label(screen1, text="Hasło * ").pack()
    password_entry = tk.Entry(screen1, textvariable=password)
    password_entry.pack()
    tk.Label(screen1, text="").pack()
    tk.Button(screen1, text="Rejestracja", width=10, height=1, command=register_user).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    with open(f'{username_info}.txt', "w") as file:
        file.write(username_info)
        file.write("\n")
        file.write(password_info)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    tk.Label(text="Rejestracja zakończona sukcesem")
    screen1.destroy()


def main_app():
    window = tk.Tk()
    window.title("Wypożyczalnia Samochodów")

    def connect_to_database():
        connection = mysql.connector.connect(host='localhost',
                                             database='car_rental',
                                             user='root',
                                             password='root',
                                             autocommit=True)
        if connection.is_connected():
            global cursor
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

            return connection, cursor

    def close_database_connection(connection):
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    def select_sample_customers_query():
        cursor.execute('SELECT * FROM tbl_customer LIMIT 5')
        myresult = cursor.fetchall()
        columns = ""
        for x in myresult:
            for i in x:
                columns += str(i) + " "
            columns += '\n'
        return columns

    def select_sample_vehicles_query():
        cursor.execute('''SELECT review.car_review_id, review.car_segment, vehicle.vehicle_type, vehicle.capacity, vehicle.manufactured_year, vehicle.sec_pay_status
                            FROM tbl_car_review review JOIN tbl_vehicle vehicle ON review.vehicle_id = vehicle .vehicle_id
                            WHERE vehicle.availability = TRUE LIMIT 5;''')
        myresult = cursor.fetchall()
        columns = ""
        for x in myresult:
            for i in x:
                columns += str(i) + " "
            columns += '\n'
        return columns

    def add_customers_query(sample_name, sample_surname, sample_number, sample_address):
        cursor.execute(
            "INSERT INTO tbl_customer (name, surname, tel_number, addres) VALUES (%s, %s, %s, %s);", (sample_name, sample_surname, sample_number, sample_address))


    def select_specific_customer(name):
        cursor.execute('SELECT * FROM tbl_customer WHERE name = (%s)', (name,))
        myresult = cursor.fetchall()
        columns = ""
        for x in myresult:
            for i in x:
                columns += str(i) + " "
            columns += '\n'
        return columns

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

    def show_customers(show_customers_window):
        result = str(select_sample_customers_query())
        tk.Label(show_customers_window,
                 text=result).pack()

    def show_cars(show_customers_window):
        result = str(select_sample_vehicles_query())
        tk.Label(show_customers_window,
                 text=result).pack()

    def add_customer(add_customers_window):
        add_customers_query("Korwin", "Bieniek", "123456789", "Gliwice, Polska")
        result = str(select_specific_customer("Korwin"))
        print(result)
        tk.Label(add_customers_window,
                 text=result).pack()

    def open_rent_car_window():
        rent_car_window = tk.Toplevel(window)
        rent_car_window.title("Wypożycz Samochód")
        rent_car_window.geometry("300x200")
        tk.Label(rent_car_window,
                 text="Tutaj możesz wypożyczyć samochód").pack()
        show_surnames_button = tk.Button(
            rent_car_window,
            text="Pokaż pojazdy",
            width=12,
            height=2,
            bg="white",
            fg="black",
            command=lambda: show_cars(rent_car_window)
        )
        show_surnames_button.pack()
        add_return_button(rent_car_window, window)
        window.iconify()

    def open_add_customer_window():
        add_customer_window = tk.Toplevel(window)
        add_customer_window.title("Dodaj Klienta")
        add_customer_window.geometry("300x200")
        tk.Label(add_customer_window,
                 text="Tutaj możesz dodać klienta").pack()
        show_surnames_button = tk.Button(
            add_customer_window,
            text="Dodaj klienta",
            width=12,
            height=2,
            bg="white",
            fg="black",
            command=lambda: add_customer(add_customer_window)
        )
        show_surnames_button.pack()
        add_return_button(add_customer_window, window)
        window.iconify()

    def open_show_customers_window():
        show_customers_window = tk.Toplevel(window)
        show_customers_window.title("Wyświetl klientów")
        show_customers_window.geometry("300x400")
        tk.Label(show_customers_window,
                 text="Tutaj możesz wyświetlić klientów").pack()
        show_surnames_button = tk.Button(
            show_customers_window,
            text="Pokaż klientów",
            width=12,
            height=2,
            bg="white",
            fg="black",
            command=lambda: show_customers(show_customers_window)
        )
        show_surnames_button.pack()
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

    conn, cursor = connect_to_database()
    create_main()
    window.mainloop()
    close_database_connection(conn)


def log_user():
    username_info = username.get()
    password_info = password.get()

    with open(f'{username_info}.txt', "r") as file:

        credentials = file.readlines()
        print(credentials)
        if password_info == credentials[1]:
            tk.Label(screen1, text="Logowanie zakończone sukcesem")
            screen.destroy()
            main_app()
        else:
            wrong_password_label = tk.Label(screen1, text="Błędne hasło")
            wrong_password_label.pack()


def login():
    global screen1
    screen1 = tk.Toplevel(screen)
    screen1.title("Logowanie")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(screen1, text="Proszę o wprowadzenie danych poniżej").pack()
    tk.Label(screen1, text="").pack()
    tk.Label(screen1, text="Nazwa użytkownika * ").pack()
    username_entry = tk.Entry(screen1, textvariable=username)
    username_entry.pack()
    tk.Label(screen1, text="Hasło * ").pack()
    password_entry = tk.Entry(screen1, textvariable=password)
    password_entry.pack()
    tk.Label(screen1, text="").pack()
    tk.Button(screen1, text="Logowanie", width=10, height=1, command=log_user).pack()


def main_screen():
    global screen
    screen = tk.Tk()
    screen.geometry("300x250")
    screen.title("Wypożyczalnia Samochodów - autoryzacja")
    tk.Label(text="Autoryzacja", bg="grey", width="300", height="2", font=("Calibry", 13)).pack()
    tk.Label(screen, text="").pack()
    tk.Button(screen, text="Logowanie", width=30, height=2, command=login).pack()
    tk.Label(screen, text="").pack()
    tk.Button(screen, text="Rejestracja", width=30, height=2, command=register).pack()

    screen.mainloop()


main_screen()
