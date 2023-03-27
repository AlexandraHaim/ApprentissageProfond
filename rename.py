# Script permettant de renommer les fichiers des répertoires : 
#  /database/Apprentissage/ : AsieN_A_<compteur>.png
#  /database/Validation/ : AsieN_V_<compteur>.png
#  /database/Test/ : AsieN_T_<compteur>.png

#!/usr/bin/env python3

import os
import glob

# Renommer les fichiers
def rename_files(path, suffixe):
    # Récupérer les fichiers
    files = glob.glob(path + "/*")
    print(len(files) + "fichier(s) ont été trouvés");
    # Parcourir les fichiers
    i = 0
    for file in files:
        # Renommer le fichier
        os.rename(file, "AsieS_" + suffixe + "_" + str(i) + ".png")	#TODO : mettre votre région
        i += 1
    print("Vos fichiers sont sûrement au même niveau que rename.py")

# Renommer les fichiers du répertoire Apprentissage
rename_files("/home/lucas/Documents/N7/2A_S8/Appr_Profond/ApprentissageProfond/DataBase/Apprentissage/AsieDuSud", "A")  #TODO : à modifier avec votre path
# Renommer les fichiers du répertoire Validation
rename_files("/home/lucas/Documents/N7/2A_S8/Appr_Profond/ApprentissageProfond/DataBase/Validation/AsieDuSud", "V") #TODO : à modifier avec votre path
# Renommer les fichiers du répertoire Test
rename_files("/home/lucas/Documents/N7/2A_S8/Appr_Profond/ApprentissageProfond/DataBase/Test/AsieDuSud", "T") #TODO : à modifier avec votre path
