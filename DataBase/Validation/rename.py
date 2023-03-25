# Script permettant de renommer les fichiers des répertoires : 
#  /database/Apprentissage/ : AsieN_A_<compteur>.png
#  /database/Validation/ : AsieN_V_<compteur>.png
#  /database/Test/ : AsieN_T_<compteur>.png

# Format des noms de labels : AmeriqueN / AmeriqueS / AsieN / AsieS / Europe / MoyenOrient

#!/usr/bin/env python3

import os
import glob

# Renommer les fichiers
def rename_files(path, suffixe):
    # Récupérer les fichiers
    files = glob.glob(path + "/*")
    print(str(len(files)) + "fichier(s) ont été trouvés");
    # Parcourir les fichiers
    i = 0
    for file in files:
        # Renommer le fichier
        os.rename(file, "LABEL" + "_" + suffixe + "_" + str(i) + ".png")	#TODO : mettre VOTRE région (voir labels au début)
        i += 1
    print("Vos fichiers sont sûrement au même niveau que rename.py")

# Renommer les fichiers du répertoire Apprentissage
rename_files("/home/lucas/Documents/N7/2A_S8/Appr_Profond/ApprentissageProfond/DataBase/Apprentissage/AmeriqueDuSud", "A")  #TODO : à modifier avec VOTRE path
# Renommer les fichiers du répertoire Validation
rename_files("/home/lucas/Documents/N7/2A_S8/Appr_Profond/ApprentissageProfond/DataBase/Validation/AmeriqueDuSud", "V") #TODO : à modifier avec VOTRE path
# Renommer les fichiers du répertoire Test
rename_files("/home/lucas/Documents/N7/2A_S8/Appr_Profond/ApprentissageProfond/DataBase/Test/AmeriqueDuNord", "T") #TODO : à modifier avec VOTRE path
