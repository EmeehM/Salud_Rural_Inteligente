import tkinter as tk
import customtkinter as ctk
from app import inferir_diagnostico  # La función que hace la inferencia

# Configuración de la ventana principal
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("600x400")  # Tamaño más compacto
root.minsize(600, 400)

# Título y subtítulo
title_label = ctk.CTkLabel(root, text="Salud Rural Inteligente", font=("Arial", 24, "bold"))
title_label.place(x=150, y=10)

subtitle_label = ctk.CTkLabel(root, text="Realiza tu consulta de DENGUE", font=("Arial", 16))
subtitle_label.place(x=170, y=50)

# Función para obtener el resultado del diagnóstico
def obtener_resultados():
    sintomas_seleccionados = {
        "Fiebre": int(check_var_fiebre.get()),
        "Dolor_Cabeza": int(check_var_dolor_cabeza.get()),
        "Dolor_Muscular": int(check_var_dolor_muscular.get()),
        "Nauseas": int(check_var_nauseas.get()),
        "Dolor_Abdominal": int(check_var_dolor_abdominal.get()),
        "Irritabilidad": int(check_var_irritabilidad.get()),
        "Sarpullido": int(check_var_sarpullido.get()),
        "Vomito": int(check_var_vomito.get()),
        "Sangrado": int(check_var_sangrado.get()),
        "Malestar_General": int(check_var_malestar_general.get()),
        "Dificultad_Respiratoria": int(check_var_DR.get())

    }
    
    resultado = inferir_diagnostico(sintomas_seleccionados)
    prob_diagnostico = resultado.values  # Extraer valores de probabilidad
    
    # Determinar el diagnóstico con mayor probabilidad
    max_index = prob_diagnostico.argmax()
    mensajes_diagnostico = [
        "Sin enfermedad",
        "Dengue sin signos de alarma",
        "Dengue con signos de alarma",
        "Dengue severo"
    ]
    mensaje_resultado = mensajes_diagnostico[max_index]

    # Crear una ventana emergente para mostrar el resultado
    result_window = ctk.CTkToplevel(root)
    result_window.geometry("300x200")
    result_window.title("Resultado del Diagnóstico")
    result_label = ctk.CTkLabel(result_window, text=mensaje_resultado, font=("Arial", 18, "bold"))
    result_label.pack(pady=50)

# Checkbox de síntomas
check_var_fiebre = tk.BooleanVar()
check_box_fiebre = ctk.CTkCheckBox(root, text="Fiebre", variable=check_var_fiebre, font=("Arial", 14))
check_box_fiebre.place(x=50, y=100)

check_var_dolor_cabeza = tk.BooleanVar()
check_box_dolor_cabeza = ctk.CTkCheckBox(root, text="Dolor de cabeza", variable=check_var_dolor_cabeza, font=("Arial", 14))
check_box_dolor_cabeza.place(x=50, y=130)

check_var_dolor_muscular = tk.BooleanVar()
check_box_dolor_muscular = ctk.CTkCheckBox(root, text="Dolor muscular", variable=check_var_dolor_muscular, font=("Arial", 14))
check_box_dolor_muscular.place(x=50, y=160)

check_var_nauseas = tk.BooleanVar()
check_box_nauseas = ctk.CTkCheckBox(root, text="Náuseas", variable=check_var_nauseas, font=("Arial", 14))
check_box_nauseas.place(x=50, y=190)

check_var_dolor_abdominal = tk.BooleanVar()
check_box_dolor_abdominal = ctk.CTkCheckBox(root, text="Dolor abdominal", variable=check_var_dolor_abdominal, font=("Arial", 14))
check_box_dolor_abdominal.place(x=50, y=220)

check_var_irritabilidad = tk.BooleanVar()
check_box_irritabilidad = ctk.CTkCheckBox(root, text="Irritabilidad", variable=check_var_irritabilidad, font=("Arial", 14))
check_box_irritabilidad.place(x=300, y=100)

check_var_sarpullido = tk.BooleanVar()
check_box_sarpullido = ctk.CTkCheckBox(root, text="Sarpullido", variable=check_var_sarpullido, font=("Arial", 14))
check_box_sarpullido.place(x=300, y=130)

check_var_vomito = tk.BooleanVar()
check_box_vomito = ctk.CTkCheckBox(root, text="Vómito", variable=check_var_vomito, font=("Arial", 14))
check_box_vomito.place(x=300, y=160)

check_var_malestar_general = tk.BooleanVar()
check_box_MG = ctk.CTkCheckBox(root, text="Malestar General", variable=check_var_malestar_general, font=("Arial", 14))
check_box_MG.place(x=300, y=190)

check_var_sangrado = tk.BooleanVar()
check_box_sangrado = ctk.CTkCheckBox(root, text="Sangrado", variable=check_var_sangrado, font=("Arial", 14))
check_box_sangrado.place(x=300, y=220)

check_var_DR= tk.BooleanVar()
check_box_DR = ctk.CTkCheckBox(root, text="Dificultad Respiratoria", variable=check_var_DR, font=("Arial", 14))
check_box_DR.place(x=300, y=250)

# Botón para obtener resultados
result_button = ctk.CTkButton(root, text="Resultados", font=("Arial", 18), fg_color="green", command=obtener_resultados)
result_button.place(x=240, y=300)

# Iniciar la ventana
root.mainloop()
