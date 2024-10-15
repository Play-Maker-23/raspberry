# coding: utf-8
import tkinter as tk
import serial  # Module pour communiquer avec l'Arduino

# Crée une fenêtre principale
fenetre = tk.Tk()
fenetre.title("Affichage des valeurs du DHT11")

# Connexion à l'Arduino (remplacez le port série par celui de votre Arduino)
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)  # Adding a timeout to the serial connection
except serial.SerialException as e:
    print(f"Erreur de connexion à l'Arduino : {e}")
    # Add error handling or user notification here
    # For example, creating a label to display the error message to the user

# Fonction pour lire les valeurs du DHT11
def lire_donnees():
    try:
        donnees = ser.readline().decode().strip()  # Lecture des données depuis l'Arduino
        temperature, humidite = map(float, donnees.split(','))  # Séparation des valeurs
        label_temperature.config(text=f"Température : {temperature:.2f} °C")
        label_humidite.config(text=f"Humidité : {humidite:.2f} %")
    except (ValueError, UnicodeDecodeError) as e:
        print(f"Erreur lors de la lecture des données : {e}")
        # Add error handling or user notification here
        # For example, creating a label to display the error message to the user

# Ajoute des labels pour afficher les valeurs
label_temperature = tk.Label(fenetre, text="Température :")
label_temperature.pack()

label_humidite = tk.Label(fenetre, text="Humidité :")
label_humidite.pack()

# Bouton pour rafraîchir les valeurs
bouton_actualiser = tk.Button(fenetre, text="Actualiser", command=lire_donnees)
bouton_actualiser.pack()

# Boucle principale pour afficher la fenêtre
fenetre.mainloop()
