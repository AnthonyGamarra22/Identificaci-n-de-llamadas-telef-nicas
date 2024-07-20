import pandas as pd
import numpy as np

# Cargar datos
data = pd.read_csv('calls_data.csv')

# Preprocesamiento de datos
data['fraud'] = data['fraud'].apply(lambda x: 1 if x == 'fraudulent' else 0)
data['day_of_week'] = pd.Categorical(data['day_of_week'], categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], ordered=True)

# Estadísticas descriptivas
summary = data.describe()

# Guardar estadísticas descriptivas
summary.to_csv('data_summary.csv', index=False)

print(summary)
