import cv2
import os
import sys
import time

######################
# Parametres de base #
######################

# Chemin dans lequel se trouve le fichier courant
script_path = os.path.dirname(os.path.realpath(__file__))

# Heure actuelle (timestamp)
start_time = time.time()

# Liste vide pour stocker chaque image avec delai
frames = []

# Conteur d'images initialise a zero
frame_counter = 0

# Font pour les textes a afficher
font = cv2.FONT_HERSHEY_SIMPLEX

# Texte a afficher pour la capture des points
cornerspicker_text = "Cliquer sur les 4 coins de la cible dans l'ordre : haut gauche, haut droite, bas gauche, bas droite"

# Redemarrage du script
def script_restart():
    if os.name == 'nt': # Windows
        os.execv(sys.executable, ["python"] + sys.argv)
    elif os.name == 'posix': # Linux/macOS
        os.execv(sys.executable, ["python3"] + sys.argv)
    else:
        print("Système non reconnu")

##########################
# Parametres modifiables #
##########################

# Couleur de fond de la fenetre
gui_background_color = "#333333"
# Icone dans la barre de titre de la fenetre
gui_icon = f"{script_path}/target-icon.ico"

# Points de reference (haut gauche, haut droite, bas gauche, bas droite) pour la transformation geometrique de la cible
enable_test_cornerpoints = False
test_cornerpoints = [[374,61], [1000,33], [242,692], [1154,694]]

# Rotation de la cible
enable_target_rotation = True
target_rotation = 90 # sens horaire : 90, 180 ou 270 degres

# Affichage de la source
enable_show_source = False
# Affichage des points de reference sur la source
enable_show_cornerpoints = True

# Delai de capture en secondes (pour attendre l'autofocus si on lance directement cornerspicker.py)
enable_capture_delay = False # False si la source est une video
capture_delay = 3

# Delai d'affichage en secondes (pour avoir le temps de voir l'impact apres le tir)
enable_video_delay = True
video_delay = 3

# Echelle pour la resolution
res_scale = 0.75

# Resolution de la source de capture
res_width = 1920 * res_scale
res_height = 1080 * res_scale

# Dimensions d'affichage de la cible
target_width = target_height = 770

# Source video
#source = cv2.VideoCapture(f"{script_path}/videos/cible_webcam.mp4") # video de test
source = cv2.VideoCapture(0) # webcam
source.set(cv2.CAP_PROP_FRAME_WIDTH, res_width)
source.set(cv2.CAP_PROP_FRAME_HEIGHT, res_height)

# Si ce fichier est execute directement 
if __name__ == '__main__':
    print("Ce module n'est pas prévu pour être exécuté directement !")