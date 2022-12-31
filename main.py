import config
import cv2
import pickle
import target
import time

# Recuperation des points de reference
if config.enable_test_cornerpoints:
    corner_points = config.test_cornerpoints
else:
    try:
        with open('points', 'rb') as file:
            corner_points = pickle.load(file)
    except:
        target.set_cornerpoints()

# Menu du programme
print("[ESC] pour quitter")
print("[p]   pour recalibrer la cible")

# Point d'entrée du programme
while True:
    # Met la video en pause a la derniere image
    config.frame_counter += 1
    if config.frame_counter == config.source.get(cv2.CAP_PROP_FRAME_COUNT):
        cv2.waitKey(0)

    # Capture la video image par image
    success, frame = config.source.read()

    if success:
        # Traitement de chaque image de la video (temps reel + delai)
        target_frame = target.processing(frame, corner_points)
        config.frames.append(target_frame) # On stock l'image dans une liste pour le delai
        target_frame_delay = config.frames[0]

        # Traitement de chaque image de la video pour detection des impacts
        #target_frame_mask = target.detect_bullets(target_frame)
        #target_frame_contours = target.processing(frame, corner_points)
        #target.draw_contours(target_frame_mask, target_frame_contours)

        # Pour voir les 4 points de reference sur l'image originale
        if config.enable_show_cornerpoints:
            target.show_cornerpoints(frame, corner_points)

        # Affichage des fenetres
        if config.enable_show_source:
            cv2.imshow("Webcam", frame)
        if config.enable_video_delay:
            if time.time() - config.start_time > config.video_delay:
                cv2.imshow("Cible avec delai", target_frame_delay)
                del config.frames[0]
        else:
            cv2.imshow("Cible temp reel", target_frame)
        #cv2.imshow("Cible masque", target_frame_mask)
        #cv2.imshow("Cible contours", target_frame_contours)

        # Permet de fermer les fenetres avec la touche ESC
        if cv2.waitKey(33) == 27:
            break
        # Permet de capturer les points avec la touche p
        elif cv2.waitKey(33) == 112:
            cv2.destroyAllWindows()
            target.set_cornerpoints()
    else:
        print("Erreur de lecture de la source...")
        break

config.source.release()
cv2.destroyAllWindows()