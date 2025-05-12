import pandas as pd

def load_occupations(path="data/Occupation Data.txt"):
    return pd.read_csv(path, sep='\t')

def load_related(path="data/Related Occupations.txt"):
    return pd.read_csv(path, sep='\t')

def load_knowledge(path="data/Knowledge.txt"):
    return pd.read_csv(path, sep='\t')

def load_skills(path="data/Skills.txt"):
    return pd.read_csv(path, sep='\t')
