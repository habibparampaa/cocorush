import pyautogui
import cv2
import numpy as np
import time
import keyboard  # Import modul keyboard

# Fungsi untuk menemukan gambar dan klik
def find_and_click_image(target_image_path, interval=0.0):
    # Memuat gambar target
    target_image = cv2.imread(target_image_path)

    try:
        while True:
            # Cek jika tombol 'q' ditekan untuk menghentikan
            if keyboard.is_pressed('q'):
                print("Autoklik dihentikan.")
                break

            # Screenshot layar
            screenshot = pyautogui.screenshot()
            screenshot = np.array(screenshot)
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

            # Mencari gambar di layar
            result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            # Jika ditemukan gambar dengan kecocokan yang baik (threshold bisa diubah)
            threshold = 0.8
            if max_val >= threshold:
                target_x, target_y = max_loc
                target_x += target_image.shape[1] // 2
                target_y += target_image.shape[0] // 2
                # Klik di lokasi gambar
                pyautogui.click(target_x, target_y)
                print(f"Klik di ({target_x}, {target_y})")

            time.sleep(interval)

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Jalankan fungsi untuk autoklik
if __name__ == "__main__":
    find_and_click_image("C:/Users/Habibie/Desktop/bot autoklik/pler.png")
