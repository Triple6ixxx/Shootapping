import tkinter as tk
from tkinter import filedialog
from detection import load_image, detect_hits
from analysis import analyze_hits
from database import save_results, get_user_history
import cv2

def upload_and_process_image():
    image_path = filedialog.askopenfilename()
    if image_path:
        image = load_image(image_path)
        hits = detect_hits(image)
        analysis = analyze_hits(hits)
        
        user_id = 'user_123'
        save_results(user_id, image_path, analysis)
        
        history = get_user_history(user_id)
        print(history)
        
        cv2.imshow("Detected Hits", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

app = tk.Tk()
app.title("Target Recognition App")
app.geometry("400x200")

upload_button = tk.Button(app, text="Upload Image", command=upload_and_process_image)
upload_button.pack(pady=20)

app.mainloop()
