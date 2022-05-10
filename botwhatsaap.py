import pyautogui
import pyperclip #copia caracteres especiais
import time


pyautogui.PAUSE = 1


pyautogui.hotkey("ctrl", "t") #abre nova aba
pyperclip.copy ("https://web.whatsapp.com/")
pyautogui.hotkey("ctrl", "v") #cola o link
pyautogui.press ("enter")
time.sleep(30)

#a partir daqui é necessário usar o comando time.sleep(8) pyautogui.position() para saber as coordenadas do mouse
pyautogui.click (x=366, y=321, clicks=1)
pyautogui.write ("#nome do contato#")
pyautogui.click (x=283, y=511, clicks=1)
pyautogui.click (x=831, y=895,clicks=1)
pyautogui.write ("Oie, Bom dia!")
pyautogui.press ("enter")