#!/usr/bin/python3

maison_estime = 467000.0
pret_restant = 300000
pret_initi2 = 467000.0
nom_1= 'Joséphine'
nom_2= 'Bertrand'
depense_1 = 18000.0
depense_2 = depense_1 + 100000.0 # Apport de 100k
gain_2 = 6000.0
gain_1 = 10000.0 # Joséphine est resté 4 mois aprés séparation dans l'appartement, on lui compte qu'une part de loyer car on est gentil
gain_total = gain_2 + gain_1
pret_deja_paye = depense_1 + depense_2
quotepart_1 = depense_1 / (depense_1 + depense_2)
quotepart_2 = 1-quotepart_1
print(f'quotepart de {nom_1}: {quotepart_1}')
print(f'quotepart de {nom_2}: {quotepart_2}')
redistribution_gains_1 = gain_total * quotepart_1
redistribution_gains_2 = gain_total * quotepart_2
print(f'gains aprés redistribution de {nom_1}: {redistribution_gains_1}')
print(f'gains aprés redistribution de {nom_2}: {redistribution_gains_2}')
valeur_appart = maison_estime - pret_restant 

appart_part_1 = valeur_appart * quotepart_1
appart_part_2 = valeur_appart * quotepart_2
part_1 = appart_part_1 + redistribution_gains_1 - gain_1
part_2 = appart_part_2 + redistribution_gains_2 - gain_2
print (f'part finale de {nom_1}: {part_1}')
print (f'part finale {nom_2}: {part_1}')

