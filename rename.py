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
    print(len(files) + " fichiers trouvés.")
    # Parcourir les fichiers
    i = 0
    for file in files:
        # Renommer le fichier
        os.rename(file, "<region>" + suffixe + "_" + str(i) + ".png") #TODO : à modifier avec votre region
        i += 1
    print("Vos fichiers sont sûrement au même niveau que rename.py")

# Renommer les fichiers du répertoire Apprentissage
rename_files("<mettre votre path>/ApprentissageProfond/DataBase/Apprentissage/<region>/", "A")  #TODO : à modifier avec votre path
# Renommer les fichiers du répertoire Validation
rename_files("<mettre votre path>/ApprentissageProfond/DataBase/Validation/<region>/", "V") #TODO : à modifier avec votre path
# Renommer les fichiers du répertoire Test
rename_files("<mettre votre path>/ApprentissageProfond/DataBase/Test/<region>/", "T") #TODO : à modifier avec votre path
