import config
import cornerspicker
import cv2
import numpy as np
import os
import pickle

# Creation des points de reference pour calibrer la cible
def set_cornerpoints():
    cornerspicker.set_points()
    config.script_restart()

def set_cornerpoints_gui():
    cornerspicker.set_points()

# Recuperation des points de reference
def get_cornerpoints():
    if config.enable_test_cornerpoints:
        corner_points = config.test_cornerpoints
    elif os.path.exists('points'):
        with open('points', 'rb') as file:
            corner_points = pickle.load(file)
    else:
        corner_points = []
    return corner_points

# Suppression des points de reference
def delete_cornerpoints():
    if os.path.exists('points'):
        os.remove('points')
        print("Le fichier \"points\" a été supprimé")

# Affichage des points de reference sur l'image
def show_cornerpoints(frame, cornerpoints: list):
    for x in range(4):
        cv2.circle(img=frame, center=(cornerpoints[x][0], cornerpoints[x][1]), radius=15, color=(0, 255, 0), thickness=cv2.FILLED)

# Traitement de l'image pour afficher la cible correctement
def processing(frame, cornerpoints: list):
    pts1 = np.float32(cornerpoints)
    pts2 = np.float32([[0, 0], [config.target_width, 0], [0, config.target_height], [config.target_width, config.target_height]])
    matrix = cv2.getPerspectiveTransform(src=pts1, dst=pts2)
    frame = cv2.warpPerspective(src=frame, M=matrix, dsize=(config.target_width, config.target_height))
    if config.enable_target_rotation:
        match config.target_rotation:
            case 90:
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            case 180:
                frame = cv2.rotate(frame, cv2.ROTATE_180)
            case 270:
                frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
            case _:
                print("La rotation supporte uniquement les angles de 90, 180 et 270 degrés !")
    return frame

# (en cours) Detection des impacts
def detect_bullets(frame):
    imgGray = cv2.cvtColor(src=frame, code=cv2.COLOR_RGB2GRAY)
    imgBlur = cv2.blur(src=imgGray, ksize=(5,5))
    _, thresh1 = cv2.threshold(src=imgBlur, thresh=5, maxval=255, type=cv2.THRESH_BINARY)
    mask = thresh1
    return mask

# (en cours) Encerclage des objets detectes
def draw_contours(mask, frame):
    contours, _ = cv2.findContours(image=mask, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        #if cv2.contourArea(contour) > 500 or cv2.contourArea(contour) < 200:
        #    continue
        (x,y),radius = cv2.minEnclosingCircle(contour)
        center = (int(x),int(y))
        radius = int(radius)
        cv2.circle(img=frame, center=center, radius=radius, color=(0,255,0), thickness=2)

# Si ce fichier est execute directement 
if __name__ == '__main__':
    print("Ce module n'est pas prévu pour être exécuté directement !")