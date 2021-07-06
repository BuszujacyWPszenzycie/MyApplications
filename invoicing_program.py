from tkinter import *
import sqlite3


root = Tk()
root.title("Program do wystawiania faktur")
root.geometry("400x400")

#Towrzenie przycisku do dodawania klienta oraz ustawienie go na pierwszym ekranie
add_customer = Button(root, text = "Dodaj kontrahenta", command = lambda: add_customer_def())
add_customer.grid(row = 0, column = 0)

#Utwórz bazę danych
conn = sqlite3.connect("invoicing_program_database.db")

#Utwórz kursor do bazy danych
c = conn.cursor()

#Stwórz tabelę klienci - tabela została stworzona przy pierwszym uruchomieniu programu, teraz nie trzeba jej tworzyć więc ją wyłączyłem
'''c.execute("""CREATE TABLE kontrahenci (
			tax_number text,
			company_name text,
			mail text,
			street text,
			block_number text,
			local_number intiger,
			zipcode text,
			city text,
			country text
			)""")'''


show_customers = Button(root, text = "Pokaż kontrahentów", command = lambda: show())
show_customers.grid(row = 1, column = 0)

def show():
	#Połącz z bazą danych
	conn = sqlite3.connect("invoicing_program_database.db")
	#Stwórz kursor
	c = conn.cursor()

	c.execute("SELECT *, oid FROM kontrahenci")
	records = c.fetchall()

	#Loop Thru Results
	print_records = ""
	for record in records:
		print_records += str(record[0]) + "\n"

	query_label = Label(root, text = print_records)
	query_label.grid(row = 2, column = 0, columnspan = 2)


	#Commit changes
	conn.commit()
	#Cloce connection
	conn.close()


#Definicja do przycisku "dodaj kontrahenta"
def add_customer_def():
	#Tworzenie nowego okna po naciśnięciu przycisku dodaj kontrahenta
	next_window = Toplevel()
	next_window.title("Dodawanie kontrahenta")
	next_window.geometry("450x400")
	
	#Etykieta dotycząca NIP-u
	tax_number_label = Label(next_window, text = "NIP: ")
	tax_number_label.grid(row = 0, column = 0)

	#Pole tekstowe do wpisania wartości NIP-u
	tax_number_entry = Entry(next_window)
	tax_number_entry.grid(row = 0, column = 1, ipadx = 100)

	#Etykieta dotycząca nazwy firmy
	company_name_label = Label(next_window, text = "Nazwa: ")
	company_name_label.grid(row = 1, column = 0)

	#Pole tekstowe do wpisania nazwy firmy
	company_name_entry = Entry(next_window)
	company_name_entry.grid(row = 1, column = 1, ipadx = 100)

	#Etykieta dotycząca maila
	mail_label = Label(next_window, text = "Adres e-mail: ")
	mail_label.grid(row = 2, column = 0)

	#Pole tekstowe do wpisania maila
	mail_entry = Entry(next_window)
	mail_entry.grid(row = 2, column = 1, ipadx = 100)

	#Etykieta Adres siedziby - ulica
	street_label = Label(next_window, text = "Ulica: ")
	street_label.grid(row = 3, column = 0)

	#Pole tekstowe do wpisania ulicy
	street_entry = Entry(next_window)
	street_entry.grid(row = 3, column = 1, ipadx = 100)

	#Etykieta numer bloku/domu/mieszkania
	block_number_label = Label(next_window, text = "Numer domu/lokalu: ")
	block_number_label.grid(row = 4, column = 0)

	#Pole tekstowe do wpisania numeru bloku/domu
	block_number_entry = Entry(next_window)
	block_number_entry.grid(row = 4, column = 1, ipadx = 100)

	#Etykieta numer lokalu
	local_number_label = Label(next_window, text = "Numer lokalu: ")
	local_number_label.grid(row = 5, column = 0)

	#Pole tekstowe numer lokalu
	local_number_entry = Entry(next_window)
	local_number_entry.grid(row = 5, column = 1, ipadx = 100)

	#Etykieta - Kod pocztowy
	zipcode_label = Label(next_window, text = "Kod pocztowy: ")
	zipcode_label.grid(row = 6, column = 0)

	#Pole tekstowe - kod pocztowy
	zipcode_entry = Entry(next_window)
	zipcode_entry.grid(row = 6, column = 1, ipadx = 100)

	#Etykieta - miasto
	city_label = Label(next_window, text = "Miasto: ")
	city_label.grid(row = 7, column = 0)

	#Pole tekstowe - miasto
	city_entry = Entry(next_window)
	city_entry.grid(row = 7, column = 1, ipadx = 100)

	#Etykieta - państwo
	country_label = Label(next_window, text = "Państwo: ")
	country_label.grid(row = 8, column = 0)

	#Pole tekstowe - państwo
	country_entry = Entry(next_window)
	country_entry.grid(row = 8, column = 1, ipadx = 100) 

	def submit():
		#Połącz z bazą danych
		conn = sqlite3.connect("invoicing_program_database.db")
		#Stwórz kursor
		c = conn.cursor()

		c.execute("INSERT INTO kontrahenci VALUES (:tax_number, :company_name, :mail, :street, :block_number, :local_number, :zipcode, :city, :country)",
		{
			'tax_number' : tax_number_entry.get(),
			'company_name' : company_name_entry.get(),
			'mail' : mail_entry.get(),
			'street' : street_entry.get(),
			'block_number' : block_number_entry.get(),
			'local_number' : local_number_entry.get(),
			'zipcode' : zipcode_entry.get(),
			'city' : city_entry.get(),
			'country' : country_entry.get()
		})
		
		#Wprowadź zmiany
		conn.commit()
		#Zamknij połączenie
		conn.close()

		#Clear The Text Boxes
		tax_number_entry.delete(0, END)
		company_name_entry.delete(0, END)
		mail_entry.delete(0, END)
		street_entry.delete(0, END)
		block_number_entry.delete(0, END)
		local_number_entry.delete(0, END)
		zipcode_entry.delete(0, END)
		city_entry.delete(0, END)
		country_entry.delete(0, END)


		return

	submit_customer = Button(next_window, text = "Zatwierdź", command = submit)
	submit_customer.grid(row = 9, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 150)


	return

#Wprowadź zmiany
conn.commit()

#Zamknij płączenie z bazą danych
conn.close()


root.mainloop()