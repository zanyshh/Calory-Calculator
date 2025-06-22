import customtkinter
import matplotlib.pyplot as plt 


def calculate_calories():
    try:
        carbs = float(entry_carbs.get())
        protein = float(entry_protein.get())
        fat = float(entry_fat.get())
        calories = (carbs * 4) + (protein * 4) + (fat * 9)
        result_label.configure(text=f"Total Calories: {calories:.2f}")
    except ValueError:
        result_label.configure(text="Invalid input")

def open_settings():
    settings = customtkinter.CTkToplevel(app)
    settings.geometry("400x400")
    settings.title("settings")

    toggle_1 = customtkinter.CTkSwitch(settings, text="enable dark theme")
    toggle_1.pack(pady=20)

    toggle_2 = customtkinter.CTkSwitch(settings, text="enable push notifications service")
    toggle_2.pack(pady=20)

    toggle_3 = customtkinter.CTkSwitch(settings, text="save input on closing app")
    toggle_3.pack(pady=20)

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("400x300")
app.title("Calorie Calculator")

entry_carbs = customtkinter.CTkEntry(app, placeholder_text="Carbs (g)")
entry_carbs.pack(pady=10)

entry_protein = customtkinter.CTkEntry(app, placeholder_text="Protein (g)")
entry_protein.pack(pady=10)

entry_fat = customtkinter.CTkEntry(app, placeholder_text="Fat (g)")
entry_fat.pack(pady=10)

calc_button = customtkinter.CTkButton(app, text="Calculate", command=calculate_calories)
calc_button.pack(pady=20)

result_label = customtkinter.CTkLabel(app, text="")
result_label.pack(pady=10)

settings_button = customtkinter.CTkButton(app, text="Settings", command=open_settings)
settings_button.pack(pady=10)

app.mainloop()
