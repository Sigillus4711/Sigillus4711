Proteins = {'Protein1':{'name':'alactalbum',' length': 234, 'function': 'Signalmol', 'location':'Oedinghausen', 'DNAreads':['aattgggctaa','tctgaga'], 'persfavourite': 1, "cost": 6879234},
            'Protein2':{'name':'blactalbum', 'length': 123, 'function': 'Signalmol', 'location':   'prb23567',  'DNAreads':['aattccctaa', 'tctgaga'], 'persfavourite': 1, "cost": 8796234},
            'Protein3':{'name':'clactalbum', 'length': 345, 'function': 'Hormone',   'location':  'fkf678676',  'DNAreads':['aattgggctaa','tctgaga'], 'persfavourite': 1, "cost":  696234},
            'Protein4':{'name':'bcaseine',   'length': 456, 'function': 'calffood',  'location':  'hkjff6575',  'DNAreads':['aaccggctaa', 'ttctgaa'], 'persfavourite': 1, "cost":  796234},
            'Protein5':{'name':'aCaseine',   'length': 999, 'function': 'calffood',  'location':  'Weyershagen','DNAreads':['atccgggctaa','ttctgga'], 'persfavourite': 2 , "cost": 686234},
            'Protein6':{'name':'collagene',  'length':3243, 'function': 'unknown',   'location':  'fischbach',  'DNAreads':['aattccgctaa','ttctaga'], 'persfavourite': 4 , "cost":8796234},
            'Protein7':{'name':'ptyaline',   'length': 243, 'function': 'spit',      'location':  'gland',      'DNAreads':['aatccggctaa','ttcgaga'], 'persfavourite': 3, "cost":  696234},
            'Protein8':{'name':'eggmogg',    'length': 113, 'function': 'nourish',   'location':  'egg',        'DNAreads':['atccgggctaa','ttctgag'], 'persfavourite': 6, "cost": 1696234}

            }
respons = str(input("wanna display? (w), add sthg (a), or del sthg (d)? "))
if (respons == 'w'):
  respons = str(input("wanna watch - whole Dict ? (1), keys (3), or Values (2)? "))
  if (respons   == '1'):
   print(Proteins, "   ")
  elif  (respons == '2'):
   print(" VALUES: ", Proteins.values(), "   ")
  elif (respons == '3'):
   print(" KEYS: ", Proteins.keys(), "   ")
  else:
   print("TYPO")

elif (respons == 'a'):
  nam1 = str(input("type in the ProteinName, e.g. Protein6          "))
  nam2 = str(input("type in a more detailled name, e.g. Caseine     "))
  nam3 = int(input("type in the Protein Length, e.g. 231423         "))
  nam4 = str(input("type in the Protein Function, e.g. None         "))
  nam5 = str(input("type in the Protein Location, e.g. gallbladder  "))
  nam6 = str(input("type in the Protein 1st DNA reads, separated by comma: e.g. aaatttcccggg, tttaaagggccc "))
  nam7 = str(input("type in Ur personal preference for d Protein (1-9) "))
  Proteins[nam1]={'name':nam2,'length':nam3,'function':nam4,'location':nam5, 'DNAreads': nam6, 'perspreference': nam7}
  print(Proteins)
elif (respons == 'd'):
  nam1 = str(input("type in the ProteinName to kill, e.g. Protein6      "))
  del Proteins[nam1]
  print(Proteins)
else:
 print("TYPO")
"""

respons = str(input("wanna change(c), delete (d), or add (a)? "))

if (respons == 'd'):
    nam = str(input("type in the ProteinName, e.g. Protein6      "))
    del Proteins[nam]
    print(Proteins)

elif (respons == 'a'):
    nam1 = str(input("type in the ProteinName, e.g. Protein6          "))
    nam2 = str(input("type in a more detailled name, e.g. Caseine     "))
    nam3 = int(input("type in the Protein Length, e.g. 231423         "))
    nam4 = str(input("type in the Protein Function, e.g. None         "))
    nam5 = str(input("type in the Protein Location, e.g. Stockhausen  "))
    Proteins[nam1]={'name':nam2,'length':nam3,'function':nam4,'location':nam5}
    print(Proteins)
elif (respons == 'c'):
    nam = str(input("type in the ProteinName to overwrite, e.g. Protein6   "))
    del Proteins[nam]
    nam1 = str(input("deleted, now type in the ProteinName, e.g. Protein7  "))
    nam2 = str(input("type in a more detailled name, e.g. Caseine     "))
    nam3 = int(input("type in the Protein Length, e.g. 231423         "))
    nam4 = str(input("type in the Protein Function, e.g. None         "))
    nam5 = str(input("type in the Protein Location, e.g. Stockhausen  "))
    Proteins[nam1]={'name':nam2,'length':nam3,'function':nam4,'location':nam5}
    print(Proteins)
else: print("typo")




#print(dickti)

#nu1 = str(input(" Please search a sick celebs name "))
#nu2 = str(input(" Please search a sick celebs Diagnosis "))
if (nu1 in dickti):
    # or (nu2 in dickti.values)):
 del dickti[nu1]
 print( nu1, " was removed from List ", dickti)
else:
 nu2 = str(input(" Please search a sick celebs Diagnosis "))
 dickti[nu1]=nu2
print( nu1 , "was added",  dickti)
lesch = input("Which Celeb U wanna kill ? ")
if (lesch in dickti):
 #dickti.pop(lesch)
 del dickti[lesch]
else: print("Typo ")
"""

#print(dickti)
#input()
