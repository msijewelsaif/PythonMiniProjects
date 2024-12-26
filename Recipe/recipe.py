import tkinter as tk
from tkinter import messagebox

# Static user credentials (email and password)
users = {
    'admin@example.com': {'password': 'admin123', 'role': 'admin'},
    'user@example.com': {'password': 'user123', 'role': 'user'}
}

# Static list of recipes
recipes = [
    {'name': 'Pasta', 'ingredients': 'Pasta, Tomato, Garlic, Olive oil', 'instructions': 'Boil pasta, add sauce.'},
    {'name': 'Salad', 'ingredients': 'Lettuce, Tomato, Cucumber, Olive oil', 'instructions': 'Mix all ingredients.'},
]

# Global variable to store windows for logout
current_window = None


def logout():
    global current_window
    if current_window:
        current_window.destroy()
    login_window()


# Function to add a recipe
def add_recipe():
    name = name_entry.get()
    ingredients = ingredients_text.get("1.0", "end-1c")
    instructions = instructions_text.get("1.0", "end-1c")

    if not name or not ingredients or not instructions:
        messagebox.showerror("Error", "All fields are required!")
        return

    new_recipe = {'name': name, 'ingredients': ingredients, 'instructions': instructions}
    recipes.append(new_recipe)

    messagebox.showinfo("Success", "Recipe added successfully!")
    view_recipes_admin()


# Function to view recipes for Admin
def view_recipes_admin():
    for widget in recipes_frame.winfo_children():
        widget.destroy()

    for recipe in recipes:
        recipe_label = tk.Label(recipes_frame, text=f"Name: {recipe['name']}\nIngredients: {recipe['ingredients']}\n"
                                                    f"Instructions: {recipe['instructions']}\n",
                                bg="#f7f7f7", anchor="w", justify="left", font=("Arial", 12), padx=10, pady=5)
        recipe_label.pack(fill="x", pady=2)


# Admin Dashboard
def admin_dashboard():
    global recipes_frame, name_entry, ingredients_text, instructions_text, current_window

    if current_window:
        current_window.destroy()

    admin_window = tk.Tk()
    admin_window.title("Admin Dashboard")
    admin_window.geometry("600x600")
    admin_window.configure(bg="#3E497A")
    current_window = admin_window

    tk.Label(admin_window, text="Admin Dashboard", font=("Arial", 16, "bold"), bg="#3E497A", fg="white").pack(pady=10)

    tk.Label(admin_window, text="Recipe Name", font=("Arial", 12), bg="#3E497A", fg="white").pack()
    name_entry = tk.Entry(admin_window, width=50)
    name_entry.pack(pady=5)

    tk.Label(admin_window, text="Ingredients", font=("Arial", 12), bg="#3E497A", fg="white").pack()
    ingredients_text = tk.Text(admin_window, height=5, width=50)
    ingredients_text.pack(pady=5)

    tk.Label(admin_window, text="Instructions", font=("Arial", 12), bg="#3E497A", fg="white").pack()
    instructions_text = tk.Text(admin_window, height=5, width=50)
    instructions_text.pack(pady=5)

    tk.Button(admin_window, text="Add Recipe", command=add_recipe, bg="#FF6F61", fg="white", font=("Arial", 12)).pack(pady=10)

    tk.Label(admin_window, text="All Recipes:", font=("Arial", 12, "bold"), bg="#3E497A", fg="white").pack(pady=10)

    recipes_frame = tk.Frame(admin_window, bg="#f7f7f7")
    recipes_frame.pack(fill="both", expand=True, padx=10, pady=10)

    tk.Button(admin_window, text="Logout", command=logout, bg="#FF6F61", fg="white", font=("Arial", 12)).pack(pady=10)

    admin_window.mainloop()


# Function to view recipes for User
def view_recipes_user():
    global current_window
    if current_window:
        current_window.destroy()

    user_window = tk.Tk()
    user_window.title("User Dashboard")
    user_window.geometry("500x500")
    user_window.configure(bg="#3E497A")
    current_window = user_window

    tk.Label(user_window, text="User Dashboard", font=("Arial", 16, "bold"), bg="#3E497A", fg="white").pack(pady=10)

    for recipe in recipes:
        recipe_label = tk.Label(user_window, text=f"Name: {recipe['name']}\nIngredients: {recipe['ingredients']}\n"
                                                  f"Instructions: {recipe['instructions']}\n",
                                bg="#f7f7f7", anchor="w", justify="left", font=("Arial", 12), padx=10, pady=5)
        recipe_label.pack(fill="x", pady=5, padx=10)

    tk.Button(user_window, text="Logout", command=logout, bg="#FF6F61", fg="white", font=("Arial", 12)).pack(pady=10)

    user_window.mainloop()


# Function to validate login credentials
def validate_login(username, password, role):
    if username in users and users[username]['password'] == password and users[username]['role'] == role:
        messagebox.showinfo("Login Successful", f"Welcome {username}")
        if role == "admin":
            admin_dashboard()
        else:
            view_recipes_user()
    else:
        messagebox.showerror("Login Failed", "Invalid email or password")


# Function to create login window
def login_window():
    global current_window

    if current_window:
        current_window.destroy()

    login_win = tk.Tk()
    login_win.title("Login")
    login_win.geometry("400x300")
    login_win.configure(bg="#3E497A")
    current_window = login_win

    tk.Label(login_win, text="Login", font=("Arial", 16, "bold"), bg="#3E497A", fg="white").pack(pady=20)

    tk.Label(login_win, text="Email", font=("Arial", 12), bg="#3E497A", fg="white").pack()
    username_entry = tk.Entry(login_win, width=40)
    username_entry.pack(pady=5)

    tk.Label(login_win, text="Password", font=("Arial", 12), bg="#3E497A", fg="white").pack()
    password_entry = tk.Entry(login_win, show="*", width=40)
    password_entry.pack(pady=5)

    def login_action(role):
        username = username_entry.get()
        password = password_entry.get()
        validate_login(username, password, role)

    tk.Button(login_win, text="Admin Login", command=lambda: login_action("admin"), bg="#FF6F61", fg="white",
              font=("Arial", 12)).pack(pady=10)
    tk.Button(login_win, text="User Login", command=lambda: login_action("user"), bg="#FF6F61", fg="white",
              font=("Arial", 12)).pack()

    login_win.mainloop()


# Run the login window
login_window()
