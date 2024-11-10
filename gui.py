import tkinter as tk
import customtkinter as ctk
from fontawesome import icons  # Importar FontAwesome para los iconos
from app import inferir_diagnostico  # La función que hace la inferencia

# Configuración de la ventana principal
ctk.set_appearance_mode("System")  # Modo claro/oscuro según configuración del sistema
ctk.set_default_color_theme("green")  # Tema verde

root = ctk.CTk()  # Crear la ventana principal
root.geometry("800x600")  # Establecer el tamaño de la ventana
root.minsize(800, 600)  # Definir el tamaño mínimo

# Título de la ventana
title_label = ctk.CTkLabel(root, text="Salud Rural Inteligente", font=("Arial", 30, "bold"))
title_label.place(x=200, y=20)  # Posicionar el título

# Subtítulo de la ventana
subtitle_label = ctk.CTkLabel(root, text="Realiza tu consulta de DENGUE", font=("Arial", 20))
subtitle_label.place(x=230, y=70)  # Posicionar el subtítulo

# Función para obtener los resultados y hacer la inferencia
def obtener_resultados():
    sintomas_seleccionados = {
        "Fiebre": int(check_var_fiebre.get()),
        "Dolor_Cabeza": int(check_var_dolor_cabeza.get()),
        "Dolor_Muscular": int(check_var_dolor_muscular.get()),
        "Nauseas": int(check_var_nauseas.get()),
        "Dolor_Abdominal": int(check_var_dolor_abdominal.get()),
        "Irritabilidad": int(check_var_irritabilidad.get()),
        "Sarpullido": int(check_var_sarpullido.get()),
        "Vomito": int(check_var_vomito.get())
    }
    
    diagnostico = inferir_diagnostico(sintomas_seleccionados)
    
    resultado_label = ctk.CTkLabel(root, text=f"Diagnóstico: {diagnostico}", font=("Arial", 18))
    resultado_label.place(x=300, y=500)

# Checkbox para los síntomas
check_var_fiebre = tk.BooleanVar()
check_box_fiebre = ctk.CTkCheckBox(root, text="Fiebre", variable=check_var_fiebre, font=("Arial", 18))
check_box_fiebre.place(x=50, y=150)

check_var_dolor_cabeza = tk.BooleanVar()
check_box_dolor_cabeza = ctk.CTkCheckBox(root, text="Dolor de cabeza", variable=check_var_dolor_cabeza, font=("Arial", 18))
check_box_dolor_cabeza.place(x=50, y=200)

check_var_dolor_muscular = tk.BooleanVar()
check_box_dolor_muscular = ctk.CTkCheckBox(root, text="Dolor muscular", variable=check_var_dolor_muscular, font=("Arial", 18))
check_box_dolor_muscular.place(x=50, y=250)

check_var_nauseas = tk.BooleanVar()
check_box_nauseas = ctk.CTkCheckBox(root, text="Náuseas", variable=check_var_nauseas, font=("Arial", 18))
check_box_nauseas.place(x=50, y=300)

check_var_dolor_abdominal = tk.BooleanVar()
check_box_dolor_abdominal = ctk.CTkCheckBox(root, text="Dolor abdominal", variable=check_var_dolor_abdominal, font=("Arial", 18))
check_box_dolor_abdominal.place(x=50, y=350)

check_var_irritabilidad = tk.BooleanVar()
check_box_irritabilidad = ctk.CTkCheckBox(root, text="Irritabilidad", variable=check_var_irritabilidad, font=("Arial", 18))
check_box_irritabilidad.place(x=400, y=150)

check_var_sarpullido = tk.BooleanVar()
check_box_sarpullido = ctk.CTkCheckBox(root, text="Sarpullido", variable=check_var_sarpullido, font=("Arial", 18))
check_box_sarpullido.place(x=400, y=200)

check_var_vomito = tk.BooleanVar()
check_box_vomito = ctk.CTkCheckBox(root, text="Vómito", variable=check_var_vomito, font=("Arial", 18))
check_box_vomito.place(x=400, y=250)

# Botón para mostrar los resultados
result_button = ctk.CTkButton(root, text="Resultados", font=("Arial", 20), fg_color="green", command=obtener_resultados)
result_button.place(x=300, y=450)  # Posicionar el botón

# Iniciar la ventana
root.mainloop()
