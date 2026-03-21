import json
import re
import os

def clean_text(text):
    if not text: return ""
    # Strip hidden carriage returns, newlines, and tabs that crash browsers
    return re.sub(r'[\n\r\t]', ' ', text).strip()

def build_kids_root_gedcom(gedcom_file, output_file):
    # Quick check to ensure the file exists before we try to parse it
    if not os.path.exists(gedcom_file):
        print(f"Error: Could not find the GEDCOM file at {gedcom_file}")
        print("Please check your folder structure and try again.")
        return

    indis = {}
    fams = {}
    
    current_type = None
    current_id = None
    current_event = None

    with open(gedcom_file, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(' ', 2)
            if len(parts) < 2: continue
            
            level, tag = parts[0], parts[1]
            value = parts[2] if len(parts) > 2 else ""

            if level == '0' and value == 'INDI':
                current_id = tag.replace('@', '')
                current_type = 'INDI'
                indis[current_id] = {
                    'id': current_id, 'name': 'Unknown', 'famc': None, 'fams': [],
                    'birtDate': '', 'birtPlace': '', 'deatDate': '', 'deatPlace': ''
                }
            elif level == '0' and value == 'FAM':
                current_id = tag.replace('@', '')
                current_type = 'FAM'
                fams[current_id] = {'husb': None, 'wife': None, 'chil': []}
                
            elif current_type == 'INDI':
                if level == '1' and tag == 'NAME':
                    indis[current_id]['name'] = clean_text(value.replace('/', ''))
                elif level == '1' and tag == 'FAMC':
                    indis[current_id]['famc'] = value.replace('@', '')
                elif level == '1' and tag == 'FAMS':
                    indis[current_id]['fams'].append(value.replace('@', ''))
                elif level == '1' and tag in ['BIRT', 'DEAT']:
                    current_event = tag
                
                elif level == '2' and current_event == 'BIRT':
                    if tag == 'DATE': indis[current_id]['birtDate'] = clean_text(value)
                    elif tag == 'PLAC': indis[current_id]['birtPlace'] = clean_text(value)
                elif level == '2' and current_event == 'DEAT':
                    if tag == 'DATE': indis[current_id]['deatDate'] = clean_text(value)
                    elif tag == 'PLAC': indis[current_id]['deatPlace'] = clean_text(value)
                    
            elif current_type == 'FAM':
                if level == '1' and tag == 'HUSB': fams[current_id]['husb'] = value.replace('@', '')
                elif level == '1' and tag == 'WIFE': fams[current_id]['wife'] = value.replace('@', '')
                elif level == '1' and tag == 'CHIL': fams[current_id]['chil'].append(value.replace('@', ''))

    def build_ancestors(indi_id):
        if indi_id not in indis: return None
        p = indis[indi_id]
        
        node = {
            'name': p['name'],
            'birtDate': p['birtDate'],
            'birtPlace': p['birtPlace'],
            'deatDate': p['deatDate'],
            'deatPlace': p['deatPlace'],
            'children': [] 
        }
        
        if p['famc'] and p['famc'] in fams:
            fam = fams[p['famc']]
            if fam['husb']:
                father = build_ancestors(fam['husb'])
                if father: node['children'].append(father)
            if fam['wife']:
                mother = build_ancestors(fam['wife'])
                if mother: node['children'].append(mother)
                
        return node

    jeremy_id = next((i['id'] for i in indis.values() if 'Jeremy' in i['name'] and 'Wood' in i['name']), None)
    ashley_id = next((i['id'] for i in indis.values() if 'Ashley' in i['name'] and 'Brooks' in i['name']), None)

    shared_kids = []
    if jeremy_id and ashley_id:
        for fam_id in indis[jeremy_id]['fams']:
            if fam_id in indis[ashley_id]['fams']:
                for child_id in fams[fam_id]['chil']:
                    if child_id in indis:
                        shared_kids.append(indis[child_id]['name'])
                        
    kids_label = " & ".join(shared_kids) if shared_kids else "Wood-Brooks Children"

    root = {
        'name': kids_label,
        'birtDate': 'The Next Generation',
        'birtPlace': '',
        'deatDate': '',
        'deatPlace': '',
        'children': []
    }
    
    if jeremy_id: root['children'].append(build_ancestors(jeremy_id))
    if ashley_id: root['children'].append(build_ancestors(ashley_id))

    # CRITICAL FIX: Export as a MINIFIED, single-line JSON string
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(root, f, separators=(',', ':'))
        print(f"Success! Minified JSON exported to {output_file}")

# --- UPDATED PATHS ---
# Looks for the .ged file in the ../sources/ directory relative to where this script is run
ged_file_path = '../sources/Wood Family Tree.ged'
output_json_path = 'tree_data.json'

build_kids_root_gedcom(ged_file_path, output_json_path)