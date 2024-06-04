import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    removed = patients[patients['conditions'].str.contains(r'\bDIAB1')]

    result = removed[['patient_id', 'patient_name', 'conditions']]
    return result

