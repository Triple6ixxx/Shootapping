import cv2
import numpy as np

def load_image(image_path):
    print(f"Próba wczytania obrazu: {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Nie udało się wczytać obrazu. Sprawdź ścieżkę do pliku: {image_path}")
    return image

def detect_hits(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Zapisywanie przetworzonych obrazów do debugowania
    cv2.imwrite("gray.png", gray)
    cv2.imwrite("blurred.png", blurred)
    cv2.imwrite("edges.png", edges)

    # Dostosowanie parametrów do wykrywania trafień
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20, param1=30, param2=15, minRadius=5, maxRadius=30)
    
    hits = []
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (hx, hy, hr) in circles:
            hits.append((hx, hy, hr))
            cv2.circle(image, (hx, hy), hr, (0, 255, 0), 4)
        print(f"Znaleziono {len(hits)} trafień")
    else:
        print("Nie znaleziono kół za pomocą HoughCircles")

    return hits
