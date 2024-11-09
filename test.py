from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir el modelo de la red bayesiana
model = BayesianNetwork([
    ('Sintomas_Iniciales', 'Diagnostico'),
    ('Sintomas_Secundarios', 'Diagnostico')
])

# CPT para Sintomas_Iniciales
cpd_sintomas_iniciales = TabularCPD(
    variable='Sintomas_Iniciales',
    variable_card=4,
    values=[
        [1.0, 0.8, 0.8, 0.6, 0.8, 0.6, 0.6, 0.4, 0.8, 0.6, 0.6, 0.4, 0.6, 0.4, 0.4, 0.2],
        [0.0, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.4, 0.3, 0.4, 0.4, 0.4],
        [0.0, 0.0, 0.0, 0.1, 0.0, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3],
        [0.0, 0.0, 0.1, 0.1, 0.0, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3]
    ],
    evidence=['Sintomas_Secundarios'],
    evidence_card=[4]
)

# CPT para Sintomas_Secundarios
cpd_sintomas_secundarios = TabularCPD(
    variable='Sintomas_Secundarios',
    variable_card=4,
    values=[
        [1.0, 0.8, 0.8, 0.6, 0.8, 0.6, 0.6, 0.4, 0.8, 0.6, 0.6, 0.4, 0.6, 0.4, 0.4, 0.2],
        [0.0, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.4, 0.3, 0.4, 0.4, 0.4],
        [0.0, 0.0, 0.0, 0.1, 0.0, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3],
        [0.0, 0.0, 0.1, 0.1, 0.0, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3]
    ]
)

# CPT para Diagnostico
cpd_diagnostico = TabularCPD(
    variable='Diagnostico',
    variable_card=4,
    values=[
        [0.9, 0.8, 0.5, 0.2, 0.8, 0.4, 0.2, 0.1, 0.5, 0.3, 0.1, 0.0, 0.2, 0.1, 0.0, 0.0],
        [0.0, 0.2, 0.3, 0.3, 0.2, 0.5, 0.5, 0.3, 0.4, 0.5, 0.4, 0.2, 0.3, 0.3, 0.2, 0.1],
        [0.0, 0.0, 0.2, 0.3, 0.0, 0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.4, 0.3, 0.3, 0.4, 0.3],
        [0.0, 0.0, 0.0, 0.2, 0.0, 0.0, 0.1, 0.3, 0.0, 0.0, 0.2, 0.4, 0.2, 0.3, 0.4, 0.6]
    ],
    evidence=['Sintomas_Iniciales', 'Sintomas_Secundarios'],
    evidence_card=[4, 4]
)

# Añadir las CPDs al modelo
model.add_cpds(cpd_sintomas_iniciales, cpd_sintomas_secundarios, cpd_diagnostico)

# Comprobar si el modelo es válido
assert model.check_model()

# Realizar inferencia en el modelo
infer = VariableElimination(model)

# Ejemplo de consulta: Probabilidad de diagnóstico dado síntomas iniciales y secundarios
query_result = infer.query(variables=['Diagnostico'], evidence={'Sintomas_Iniciales': 1, 'Sintomas_Secundarios': 2})
print(query_result)
