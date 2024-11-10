from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Crear la red bayesiana
def create_model():
    model = BayesianNetwork([
        ('Fiebre', 'Sintomas_Principales'),
        ('Dolor_Cabeza', 'Sintomas_Principales'),
        ('Dolor_Muscular', 'Sintomas_Principales'),
        ('Nauseas', 'Sintomas_Principales'),
        ('Malestar_General', 'Sintomas_Principales'),
        ('Sarpullido', 'Sintomas_Principales'),
        ('Sintomas_Principales', 'Diagnostico'),
        ('Dolor_Abdominal', 'Sintomas_Secundarios'),
        ('Irritabilidad', 'Sintomas_Secundarios'),
        ('Sangrado', 'Sintomas_Secundarios'),
        ('Vomito', 'Sintomas_Secundarios'),
        ('Dificultad_Respiratoria', 'Sintomas_Secundarios'),
        ('Sintomas_Secundarios', 'Diagnostico')
    ])

    # Los valores de los CPDs proporcionados por ti
    cpd_fiebre = TabularCPD(variable='Fiebre', variable_card=2, values=[[0.7], [0.3]])
    cpd_dolor_cabeza = TabularCPD(variable='Dolor_Cabeza', variable_card=2, values=[[0.8], [0.2]])
    cpd_dolor_muscular = TabularCPD(variable='Dolor_Muscular', variable_card=2, values=[[0.75], [0.25]])
    cpd_sarpullido = TabularCPD(variable='Sarpullido', variable_card=2, values=[[0.7], [0.3]])
    cpd_nauseas = TabularCPD(variable='Nauseas', variable_card=2, values=[[0.85], [0.15]])
    cpd_malestar_general = TabularCPD(variable='Malestar_General', variable_card=2,values=[[0.85], [0.15]])

    cpd_dolor_abdominal = TabularCPD(variable='Dolor_Abdominal', variable_card=2, values=[[0.9], [0.1]])
    cpd_irritabilidad = TabularCPD(variable='Irritabilidad', variable_card=2, values=[[0.8], [0.2]])
    cpd_sangrado = TabularCPD(variable='Sangrado', variable_card=2, values=[[0.7], [0.3]])
    cpd_vomito = TabularCPD(variable='Vomito', variable_card=2, values=[[0.85], [0.15]])
    cpd_dif_resp = TabularCPD(variable='Dificultad_Respiratoria', variable_card=2, values=[[0.85], [0.15]])

    # CPD para síntomas principales con los valores que me diste
    cpd_sintomas_principales = TabularCPD(
        variable='Sintomas_Principales',
        variable_card=4,  # 4 posibles salidas: Ninguno, Leve, Moderado, Severo
        values=[
            #TABLA SINTOMAS INICIALES
            #NINGUNO:
            [1.0, 0.8, 0.8, 0.4, 0.6, 0.4, 0.3, 0.2, 0.6, 0.5, 0.5, 0.3, 0.4, 0.3, 0.3, 0.2, 0.5, 0.6, 0.6, 0.2, 0.6, 0.2, 0.3, 0.2, 0.5, 0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 0.1, 0.8, 0.5, 0.4, 0.3, 0.4, 0.4, 0.3, 0.2, 0.4, 0.3, 0.3, 0.2, 0.2, 0.2, 0.1, 0.0, 0.4, 0.2, 0.3, 0.1, 0.3, 0.2, 0.2, 0.1, 0.4, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.0],
            #LEVE:
            [0.0, 0.2, 0.2, 0.5, 0.3, 0.4, 0.4, 0.5, 0.3, 0.3, 0.3, 0.6, 0.4, 0.4, 0.5, 0.4, 0.4, 0.3, 0.3, 0.5, 0.3, 0.5, 0.4, 0.2, 0.3, 0.4, 0.4, 0.2, 0.5, 0.2, 0.2, 0.1, 0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.3, 0.5, 0.4, 0.3, 0.3, 0.4, 0.3, 0.4, 0.2, 0.4, 0.4, 0.4, 0.3, 0.4, 0.3, 0.4, 0.3, 0.4, 0.3, 0.3, 0.1, 0.4, 0.2, 0.2, 0.0],
            #MODERADO:
            [0.0, 0.0, 0.0, 0.1, 0.1, 0.2, 0.3, 0.3, 0.1, 0.2, 0.2, 0.1, 0.2, 0.3, 0.2, 0.3, 0.1, 0.1, 0.1, 0.3, 0.1, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.2, 0.2, 0.3, 0.3, 0.1, 0.3, 0.4, 0.2, 0.3, 0.3, 0.2, 0.4, 0.2, 0.4, 0.3, 0.4, 0.3, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.5],
            #SEVERO:
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.3, 0.0, 0.3, 0.3, 0.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.3, 0.1, 0.2, 0.3, 0.4, 0.0, 0.0, 0.0, 0.2, 0.0, 0.2, 0.1, 0.2, 0.0, 0.2, 0.2, 0.4, 0.1, 0.3, 0.3, 0.5]
        ],
        evidence=['Fiebre', 'Dolor_Cabeza', 'Dolor_Muscular', 'Nauseas','Malestar_General','Sarpullido'],
        evidence_card=[2, 2, 2, 2, 2, 2]
    )

    # CPD para síntomas secundarios con los valores que me diste
    cpd_sintomas_secundarios = TabularCPD(
        variable='Sintomas_Secundarios',
        variable_card=4,  # 4 posibles salidas: Ninguno, Leve, Moderado, Severo
        values=[
            #TABLA SINTOMAS SECUNDARIOS
            #NINGUNO:
            [1.0, 0.8, 0.8, 0.6, 0.8, 0.4, 0.6, 0.3, 0.8, 0.6, 0.6, 0.4, 0.5, 0.3, 0.3, 0.2, 0.8, 0.5, 0.5, 0.3, 0.5, 0.4, 0.4, 0.1, 0.5, 0.4, 0.2, 0.1, 0.3, 0.2, 0.2, 0.1],
            #LEVE:
            [0.0, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.2, 0.3, 0.3, 0.3, 0.5, 0.3, 0.3, 0.2, 0.3, 0.4, 0.4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.6, 0.3, 0.4, 0.3, 0.3, 0.2],
            #MODERADO:
            [0.0, 0.0, 0.0, 0.1, 0.0, 0.3, 0.1, 0.3, 0.0, 0.2, 0.1, 0.3, 0.2, 0.2, 0.4, 0.4, 0.0, 0.2, 0.1, 0.3, 0.2, 0.3, 0.3, 0.3, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.3],
            #SEVERO:
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.3, 0.1, 0.2, 0.2, 0.4]
        ],
        evidence=['Dolor_Abdominal', 'Irritabilidad', 'Sangrado', 'Vomito','Dificultad_Respiratoria'],
        evidence_card=[2, 2, 2, 2, 2]
    )

    # CPD para diagnóstico con los valores que me diste
    cpd_diagnostico = TabularCPD(
        variable='Diagnostico',
        variable_card=4,  # 4 posibles estados: Sin enfermedad, Dengue sin signo de alarma, Dengue con signo de alarma, Dengue severo
        values=[
            #TABLA DIAGNOSTICO
            #SIN ENFERMEDAD:
            [0.8, 0.5, 0.3, 0.2, 0.3, 0.2, 0.2, 0.1, 0.2, 0.3, 0.1, 0.0, 0.1, 0.1, 0.0, 0.0],
            #DENGUE SIN SIGNO DE ALARMA:
            [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.3, 0.2, 0.3, 0.3, 0.3, 0.2, 0.2, 0.1, 0.1],
            #DENGUE CON SIGNO DE ALARMA:
            [0.0, 0.1, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.3, 0.4, 0.5, 0.5, 0.3, 0.4, 0.3],
            #DENGUE SEVERO:
            [0.0, 0.0, 0.0, 0.1, 0.0, 0.1, 0.1, 0.3, 0.2, 0.1, 0.2, 0.2, 0.2, 0.4, 0.5, 0.6]
        ],
        evidence=['Sintomas_Principales', 'Sintomas_Secundarios'],
        evidence_card=[4, 4]
    )

    model.add_cpds(cpd_fiebre, cpd_dolor_cabeza, cpd_dolor_muscular, cpd_nauseas,
                   cpd_dolor_abdominal, cpd_irritabilidad, cpd_sarpullido, cpd_vomito,
                   cpd_sintomas_principales, cpd_sintomas_secundarios, cpd_diagnostico,cpd_malestar_general,cpd_sangrado,cpd_dif_resp)

    model.check_model()
    return model

# Función para inferir el diagnóstico
def inferir_diagnostico(sintomas):
    model = create_model()
    infer = VariableElimination(model)

    sintomas_dict = {
        'Fiebre': sintomas["Fiebre"],
        'Dolor_Cabeza': sintomas['Dolor_Cabeza'],
        'Dolor_Muscular': sintomas['Dolor_Muscular'],
        'Nauseas': sintomas['Nauseas'],
        'Dolor_Abdominal': sintomas['Dolor_Abdominal'],
        'Irritabilidad': sintomas['Irritabilidad'],
        'Sarpullido': sintomas['Sarpullido'],
        'Vomito': sintomas['Vomito'],
        'Sangrado' : sintomas['Sangrado'],
        'Malestar_General' : sintomas['Malestar_General'],
        'Dificultad_Respiratoria' : sintomas['Dificultad_Respiratoria'],
    }
    
    # Realizar la inferencia
    resultado = infer.query(variables=['Diagnostico'], evidence=sintomas_dict, show_progress=True)
    print(resultado)
    return resultado
