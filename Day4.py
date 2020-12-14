import re

passports = []
entry = []
valid_passports = []
invalid_passports = []

valid_eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

with open("Inputs/day4.txt", "r") as file:
    for line in file:
        line = line.rstrip().split(' ')
        if line != ['']:
            entry += line
        else:
            passports.append(entry)
            entry = []
    passports.append(entry)

entity_number = 0
for entity in passports:
    d = {}
    for ent in entity:
        key, value = ent.split(':')
        d[key] = value
    passports[entity_number] = d
    entity_number += 1

for passport in passports:
    # Years
    if 'byr' in passport:
        if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
            continue
    else:
        continue

    if 'iyr' in passport:
        if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
            continue
    else:
        continue

    if 'eyr' in passport:
        if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
            continue
    else:
        continue

    # Physical attributes
    if 'hgt' in passport:
        if passport['hgt'][-2:] == "in":
            if int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 79:
                continue
        elif passport['hgt'][-2:] == "cm":
            if int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193:
                continue
        else:
            continue
    else:
        continue

    if 'hcl' in passport:
        if not passport['hcl'].startswith('#'):
            continue
        elif len(passport['hcl']) != 7:
            continue
        elif re.match('[0-9][a-f]', passport['hcl']):
            continue
    else:
        continue

    if 'ecl' in passport:
        if passport['ecl'] not in valid_eye_colours:
            continue
    else:
        continue

    # IDs
    if 'pid' in passport:
        if len(passport['pid']) != 9:
            continue
    else:
        continue

    if 'cid' in passport:
        if len(passport) == 8:
            valid_passports.append(passport)
    else:
        if len(passport) == 7:
            valid_passports.append(passport)

print(len(passports))
print(len(valid_passports))
