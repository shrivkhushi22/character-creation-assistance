import requests
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

#initialization for class data
base = "https://www.dnd5eapi.co/api/2024"

class_response = requests.get(f"{base}/classes")
classes = class_response.json()["results"]

class_data = []
for c in classes:
    index = c["index"]
    resp = requests.get(f"{base}/classes/{index}")
    data = resp.json()

    class_data.append(data)

classes_df = pd.DataFrame(class_data)
print(classes_df.columns)

ability_names = [
    'STR',
    'DEX',
    'CON',
    'INT',
    'WIS',
    'CHA'
]

#---
#proficiency options and number of proficiency options for character creation 
#---

proficiency_names = [
    'Acrobatics',
    'Animal Handling',
    'Arcana',
    'Athletics',
    'Deception',
    'History',
    'Insight',
    'Intimidation',
    'Investigation',
    'Medicine',
    'Nature',
    'Perception',
    'Performance',
    'Persuasion',
    'Religion',
    'Sleight of Hand',
    'Stealth',
    'Survival'
]

proficiencies = classes_df['proficiency_choices']
proficiency_data = []
for i in range(len(proficiencies)):
    #gives number of proficiency choices for current class
    number_of_choices = proficiencies[i][0]['choose']
    dic = {'Number of Proficiency choices': number_of_choices}
    
    #current class proficiencies description of choices and number of choices
    for p in proficiency_names:
        dic[p] = 0
    class_options = proficiencies.iloc[i][0]['from']['options']
    for op in class_options:
        p_name = op['item']['name'].replace('Skill: ', '')
        dic[p_name] = 1
    proficiency_data.append(dic)

pro = pd.DataFrame(proficiency_data)
pro['name'] = classes_df['name']
pro

#---   
#primary ability for character creation
#---

pa = classes_df['primary_ability']
primary = pd.DataFrame()
primary['abilities'] = pa

primary["desc"] = primary["abilities"].apply(lambda x: x["desc"])

primary[["ability_1", "ability_2"]] = (
    primary["desc"]
    .str.split(r"\s+(?:or|and)\s+", n=1, expand=True)
)

primary



#finish this and split ability description into list of abilities

#---
#hit_die for character creation
#---
hit_dice = classes_df['hit_die']
hit_dice

#---
#saving_throws for character creation
#---



saving_throws = classes_df['saving_throws']
st_data = []
for i in range(len(saving_throws)):
    st_name = saving_throws.iloc[i][0]['name']
    dic = {}
    for s in ability_names:
        dic[s] = 0
    dic[st_name] = 1    
    st_data.append(dic)

print(st_data)
#---
#spell_casting for character creation
#---

sc = classes_df[['name', 'spellcasting']]

spellcasters = pd.DataFrame()
spellcasters['name'] = sc['name']
spellcasters['spellcasting'] = sc['spellcasting']
spellcasters['spellcaster'] = sc['spellcasting'].fillna(False).astype(bool)

casters = spellcasters[spellcasters['spellcaster']==True]
caster_names = casters['name'].tolist()

sc_ability = []
for i in range(len(spellcasters)):
    ab = None
    class_name = spellcasters['name'].iloc[i]
    if class_name in caster_names:
        ab = spellcasters['spellcasting'].iloc[i]['spellcasting_ability']['name']
    else:
        ab = None
    sc_ability.append(ab)
sc_ability

spellcasters['casting_ability'] = sc_ability


print(classes_df.columns)
print(classes_df['primary_ability'].iloc[4])
print(classes_df['primary_ability'].iloc[0])
print(classes_df[['name','spellcasting']])


print(classes_df[['name', 'proficiency_choices']].iloc[10])
