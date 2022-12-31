import config
import cv2
import pickle
import time

# Liste des points
points = []

# Capturer une image de la source
def get_frame():
    if config.enable_capture_delay:
        max_time = time.time() + config.capture_delay
        while time.time() < max_time:
            success, frame = config.source.read()
    else:
        success, frame = config.source.read()
    if success:
        config.source.release()
        return frame
    else:
        print("Erreur de lecture de la source...")

# Enregistrer les points dans un fichier
def save_points():
    with open('points','wb') as file:
        pickle.dump(points, file)
        print("Les points ont été enregistrés dans le fichier \"points\"")

# Recuperer les points d'un clique gauche de souris
def get_mouse_points(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])

# Definir les 4 points pour les enregistrer dans un fichier
def set_points():
    frame = get_frame()
    cv2.putText(img=frame, text=config.cornerspicker_text, org=(20, 20), fontFace=config.font, fontScale=0.5, color=(100, 255, 0), thickness=1, lineType=cv2.LINE_AA)

    while len(points) < 4:
        for point in points:
            cv2.circle(frame, point, 7, (0, 0, 255), cv2.FILLED)
        cv2.imshow("Calibrage de la cible", frame)
        cv2.setMouseCallback("Calibrage de la cible", get_mouse_points)
        cv2.waitKey(1)

    cv2.destroyWindow("Calibrage de la cible")
    print(points)
    save_points()

# Si ce fichier est execute directement 
if __name__ == '__main__':
    set_points()