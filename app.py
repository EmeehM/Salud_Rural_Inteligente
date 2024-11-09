from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianNetwork

# Definir el modelo de la red bayesiana
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

# Definir CPDs para cada variable
cpd_fiebre = TabularCPD(variable='Fiebre', variable_card=2, values=[[0.7], [0.3]])  # Probabilidad de presencia/ausencia

cpd_dolor_cabeza = TabularCPD(variable='Dolor_Cabeza', variable_card=2, values=[[0.8], [0.2]])
cpd_dolor_muscular = TabularCPD(variable='Dolor_Muscular', variable_card=2, values=[[0.75], [0.25]])
cpd_nauseas = TabularCPD(variable='Nauseas', variable_card=2, values=[[0.85], [0.15]])

# Valores que proporcionaste, organizados en formato adecuado para la CPD
cpd_sintomas_principales = TabularCPD(
    variable='Sintomas_Principales',
    variable_card=4,  # 4 posibles salidas: Ninguno, Leve, Moderado, Severo
    values=[
        [1.0, 0.8, 0.8, 0.6, 0.8, 0.6, 0.6, 0.4, 0.8, 0.6, 0.6, 0.4, 0.6, 0.4, 0.4, 0.2],  # Ninguno
        [0.0, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.4, 0.3, 0.4, 0.4, 0.4],   # Leve
        [0.0, 0.0, 0.0, 0.1, 0.0, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3],   # Moderado
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1]    # Severo
    ],
    evidence=['Fiebre', 'Dolor_Cabeza', 'Dolor_Muscular', 'Nauseas'],
    evidence_card=[2, 2, 2, 2]  # 2 valores posibles para cada una de las 4 variables condicionales
)



cpd_dolor_abdominal = TabularCPD(variable='Dolor_Abdominal', variable_card=2, values=[[0.85], [0.15]])
cpd_irritabilidad = TabularCPD(variable='Irritabilidad', variable_card=2, values=[[0.9], [0.1]])
cpd_sarpullido = TabularCPD(variable='Sarpullido', variable_card=2, values=[[0.88], [0.12]])
cpd_vomito = TabularCPD(variable='Vomito', variable_card=2, values=[[0.87], [0.13]])

# Definir la tabla para Sintomas_Secundarios
cpd_sintomas_secundarios = TabularCPD(
    variable='Sintomas_Secundarios',
    variable_card=4,  # Sintomas_Secundarios tiene 4 posibles estados
    values=[
        [1.0, 0.8, 0.8, 0.6, 0.8, 0.6, 0.6, 0.4, 0.8, 0.6, 0.6, 0.4, 0.6, 0.4, 0.4, 0.2],  # Primer grupo de valores
        [0.0, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.4, 0.3, 0.4, 0.4, 0.4],  # Segundo grupo de valores
        [0.0, 0.0, 0.0, 0.1, 0.0, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3],  # Tercer grupo de valores
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1]   # Cuarto grupo de valores
    ],
    evidence=['Dolor_Abdominal', 'Irritabilidad', 'Sarpullido', 'Vomito'],
    evidence_card=[2, 2, 2, 2]  # 2 valores posibles para cada una de las 4 variables condicionales
)

cpd_diagnostico = TabularCPD(
    variable='Diagnostico',
    variable_card=4,  # 4 posibles estados: Sin enfermedad, Dengue sin signo de alarma, Dengue con signo de alarma, Dengue severo
    values=[
        # Sin enfermedad
        [0.9, 0.8, 0.5, 0.2, 0.8, 0.4, 0.2, 0.1, 0.5, 0.3, 0.1, 0.0, 0.2, 0.1, 0.0, 0.0],  # Estado 0: Ninguno
        [0.0, 0.2, 0.3, 0.3, 0.2, 0.5, 0.5, 0.3, 0.4, 0.5, 0.4, 0.2, 0.3, 0.3, 0.2, 0.1],  # Estado 1: Leve
        [0.0, 0.0, 0.2, 0.3, 0.0, 0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.4, 0.3, 0.3, 0.4, 0.3],  # Estado 2: Moderado
        [0.1, 0.0, 0.0, 0.2, 0.0, 0.0, 0.1, 0.3, 0.0, 0.0, 0.2, 0.4, 0.2, 0.3, 0.4, 0.6],  # Estado 3: Severo
    ],
    evidence=['Sintomas_Principales', 'Sintomas_Secundarios'],  # Las variables de evidencia son solo los síntomas principales y secundarios
    evidence_card=[4, 4]  # 4 valores posibles para cada uno de los síntomas principales y secundarios
)

# Agregar todos los CPDs al modelo
model.add_cpds(cpd_fiebre, cpd_dolor_cabeza, cpd_dolor_muscular, cpd_nauseas,
               cpd_sintomas_principales, cpd_dolor_abdominal, cpd_irritabilidad, cpd_sarpullido, cpd_vomito,
               cpd_sintomas_secundarios, cpd_diagnostico)

# Verificar si el modelo es consistente
assert model.check_model()

# Si el modelo es válido, puedes proceder con las consultas
print("El modelo es válido")
