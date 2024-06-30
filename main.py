from detection import load_image, detect_hits
from database import save_results
import cv2
import os
import sys

# Ustawienie kodowania na utf-8
sys.stdout.reconfigure(encoding='utf-8')

def main():
    user_id = 'user123'  # Przykładowy ID użytkownika
    image_path = r'C:\Users\The_vill\target_recognition_app\Images\TarczaSterylna.png'  # Używamy surowego ciągu znaków
    
    if not os.path.exists(image_path):
        print(f"Plik nie istnieje: {image_path}")
        return

    print(f"Wczytywanie obrazu: {image_path}")
    image = load_image(image_path)
    
    if image is not None:
        print("Obraz został wczytany poprawnie")
    else:
        print("Błąd wczytywania obrazu")
        return

    hits = detect_hits(image)
    
    if hits:
        print(f"Trafienia: {hits}")
        for (x, y, r) in hits:
            cv2.circle(image, (x, y), r, (0, 255, 0), 4)
        
        analysis = {'hits': hits}
        save_results(user_id, image_path, analysis)
        print("Wyniki zapisane do bazy danych.")
        
        cv2.imshow("Detected Hits", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Nie wykryto trafień.")

if __name__ == "__main__":
    main()
