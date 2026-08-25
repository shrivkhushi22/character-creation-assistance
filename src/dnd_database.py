import json
import glob
import os
import pandas as pd

dfs = {}
for path in glob.glob("dnd-data/data/**/*.json", recursive=True):
    with open(path, encoding="utf-8") as f:
        obj = json.load(f)
    name = os.path.splitext(os.path.basename(path))[0]  # e.g. "spells"
    dfs[name] = pd.json_normalize(obj)

print(list(dfs.keys()))  # sanity check — confirm "spells" is actually in there
spells = dfs.get("spells")
classes = dfs.get("classes")
phb_name_and_desc = classes[(classes['book'] == "Player's Handbook (2024)")][['name', 'description']]
subclasses = [sc.split('.')[-1] for sc in phb_name_and_desc['description'].tolist()]

known_sc = {
    'Barbarian': ['Path of the Berserker', 'Path of the Wild Heart', 'Path of the World Tree', 'Path of the Zealot'],
    'Bard': ['College of Dance', 'College of Glamour', 'College of Lore', 'College of Valor'],
    'Cleric': ['Life Domain', 'Light Domain', 'Trickery Domain', 'War Domain'],
    'Druid': ['Circle of the Land', 'Circle of the Moon', 'Circle of the Sea', 'Circle of the Stars'],
    'Fighter': ['Battle Master', 'Champion', 'Eldritch Knight', 'Psi Warrior'],
    'Monk': ['Warrior of Mercy', 'Warrior of Shadow', 'Warrior of the Elements', 'Warrior of the Open Hand'],
    'Paladin': ['Oath of Devotion', 'Oath of Glory', 'Oath of the Ancients', 'Oath of Vengeance'],
    'Ranger': ['Beast Master', 'Fey Wanderer', 'Gloom Stalker', 'Hunter'],
    'Rogue': ['Arcane Trickster', 'Assassin', 'Soulknife', 'Thief'],
    'Sorcerer': ['Aberrant Sorcery', 'Clockwork Sorcery', 'Draconic Sorcery', 'Wild Magic Sorcery'],
    'Warlock': ['Archfey Patron', 'Celestial Patron', 'Fiend Patron', 'Great Old One Patron'],
    'Wizard': ['Abjurer', 'Diviner', 'Evoker', 'Illusionist'],
}


phb_name_sc = pd.DataFrame()
phb_name_sc['name'] = phb_name_and_desc['name']
phb_name_sc['subclasses'] = subclasses
phb_name_sc.reset_index()

phb_name_sc
phb_name_and_desc.iloc[0]['description']