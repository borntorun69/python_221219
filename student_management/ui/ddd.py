import tkinter as tk



class LoginForm(tk.Tk):
  def __init__(self):
    super().__init__()

    # create label for username
    self.username_label = tk.Label(self, text="Username:")
    self.username_label.grid(row=0, column=0)

    # create entry for username
    self.username_entry = tk.Entry(self)
    self.username_entry.grid(row=0, column=1)

    # create label for password
    self.password_label = tk.Label(self, text="Password:")
    self.password_label.grid(row=1, column=0)

    # create entry for password
    self.password_entry = tk.Entry(self, show="*")
    self.password_entry.grid(row=1, column=1)

    # create button for submission
    self.submit_button = tk.Button(self, text="Submit", command=self.submit)
    self.submit_button.grid(row=2, column=0, columnspan=2)

  def submit(self):
    # get the values from the entries
    username = self.username_entry.get()
    password = self.password_entry.get()

    # connect to the database
    conn = sqlite3.connector.connect(
      host="localhost",
      user="your_username",
      password="your_password",
      database="your_database"
    )

    # create a cursor
    cursor = conn.cursor()

    # execute a SELECT query to check if the user exists
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    # check if the query returned any rows
    if cursor.fetchone():
      # login successful
      tk.messagebox.showinfo("Success", "Login successful")
    else:
      # login failed
      tk.messagebox.showerror("Error", "Invalid username or password")

    # close the cursor and connection
    cursor.close()
    conn.close()


# create and run the form
form = LoginForm()
form.mainloop()