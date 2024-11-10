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
        ('Sintomas_Principales', 'Diagnostico'),
        ('Dolor_Abdominal', 'Sintomas_Secundarios'),
        ('Irritabilidad', 'Sintomas_Secundarios'),
        ('Sarpullido', 'Sintomas_Secundarios'),
        ('Vomito', 'Sintomas_Secundarios'),
        ('Sintomas_Secundarios', 'Diagnostico')
    ])

    # Los valores de los CPDs proporcionados por ti
    cpd_fiebre = TabularCPD(variable='Fiebre', variable_card=2, values=[[0.7], [0.3]])
    cpd_dolor_cabeza = TabularCPD(variable='Dolor_Cabeza', variable_card=2, values=[[0.8], [0.2]])
    cpd_dolor_muscular = TabularCPD(variable='Dolor_Muscular', variable_card=2, values=[[0.75], [0.25]])
    cpd_nauseas = TabularCPD(variable='Nauseas', variable_card=2, values=[[0.85], [0.15]])

    cpd_dolor_abdominal = TabularCPD(variable='Dolor_Abdominal', variable_card=2, values=[[0.9], [0.1]])
    cpd_irritabilidad = TabularCPD(variable='Irritabilidad', variable_card=2, values=[[0.8], [0.2]])
    cpd_sarpullido = TabularCPD(variable='Sarpullido', variable_card=2, values=[[0.7], [0.3]])
    cpd_vomito = TabularCPD(variable='Vomito', variable_card=2, values=[[0.85], [0.15]])

    # CPD para síntomas principales con los valores que me diste
    cpd_sintomas_principales = TabularCPD(
        variable='Sintomas_Principales',
        variable_card=4,  # 4 posibles salidas: Ninguno, Leve, Moderado, Severo
        values=[
            [0.9, 0.8, 0.5, 0.2, 0.8, 0.4, 0.2, 0.1, 0.5, 0.3, 0.1, 0.0, 0.2, 0.1, 0.0, 0.0],  # Ninguno
            [0.0, 0.2, 0.3, 0.3, 0.2, 0.5, 0.5, 0.3, 0.4, 0.5, 0.4, 0.2, 0.3, 0.3, 0.2, 0.1],  # Leve
            [0.0, 0.0, 0.2, 0.3, 0.0, 0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.4, 0.3, 0.3, 0.4, 0.3],  # Moderado
            [0.1, 0.0, 0.0, 0.2, 0.0, 0.0, 0.1, 0.3, 0.0, 0.0, 0.2, 0.4, 0.2, 0.3, 0.4, 0.6],  # Severo
        ],
        evidence=['Fiebre', 'Dolor_Cabeza', 'Dolor_Muscular', 'Nauseas'],
        evidence_card=[2, 2, 2, 2]
    )

    # CPD para síntomas secundarios con los valores que me diste
    cpd_sintomas_secundarios = TabularCPD(
        variable='Sintomas_Secundarios',
        variable_card=4,  # 4 posibles salidas: Ninguno, Leve, Moderado, Severo
        values=[
            [1.0, 0.8, 0.8, 0.6, 0.8, 0.6, 0.6, 0.4, 0.8, 0.6, 0.6, 0.4, 0.6, 0.4, 0.4, 0.2],  # Primer grupo de valores
            [0.0, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.4, 0.3, 0.4, 0.4, 0.4],  # Segundo grupo de valores
            [0.0, 0.0, 0.0, 0.1, 0.0, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3],  # Tercer grupo de valores
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1]   # Cuarto grupo de valores
        ],
        evidence=['Dolor_Abdominal', 'Irritabilidad', 'Sarpullido', 'Vomito'],
        evidence_card=[2, 2, 2, 2]
    )

    # CPD para diagnóstico con los valores que me diste
    cpd_diagnostico = TabularCPD(
        variable='Diagnostico',
        variable_card=4,  # 4 posibles estados: Sin enfermedad, Dengue sin signo de alarma, Dengue con signo de alarma, Dengue severo
        values=[
            [0.9, 0.8, 0.5, 0.2, 0.8, 0.4, 0.2, 0.1, 0.5, 0.3, 0.1, 0.0, 0.2, 0.1, 0.0, 0.0],  # Estado 0: Ninguno
            [0.0, 0.2, 0.3, 0.3, 0.2, 0.5, 0.5, 0.3, 0.4, 0.5, 0.4, 0.2, 0.3, 0.3, 0.2, 0.1],  # Estado 1: Leve
            [0.0, 0.0, 0.2, 0.3, 0.0, 0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.4, 0.3, 0.3, 0.4, 0.3],  # Estado 2: Moderado
            [0.1, 0.0, 0.0, 0.2, 0.0, 0.0, 0.1, 0.3, 0.0, 0.0, 0.2, 0.4, 0.2, 0.3, 0.4, 0.6],  # Estado 3: Severo
        ],
        evidence=['Sintomas_Principales', 'Sintomas_Secundarios'],
        evidence_card=[4, 4]
    )

    model.add_cpds(cpd_fiebre, cpd_dolor_cabeza, cpd_dolor_muscular, cpd_nauseas,
                   cpd_dolor_abdominal, cpd_irritabilidad, cpd_sarpullido, cpd_vomito,
                   cpd_sintomas_principales, cpd_sintomas_secundarios, cpd_diagnostico)

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
    }
    
    # Realizar la inferencia
    resultado = infer.query(variables=['Diagnostico'], evidence=sintomas_dict, show_progress=True)
    return resultado
