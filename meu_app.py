import pyautogui
import time
from datetime import datetime
import os

os.makedirs("prints", exist_ok=True)

print("Teste de prints a cada 2 segundos...")

for i in range(5):  # só 5 prints para teste
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = pyautogui.screenshot()
    screenshot.save(f"prints/print_{timestamp}.png")
    print(f"Print salvo: prints/print_{timestamp}.png")
    time.sleep(2)
