import pyautogui as PyAuto
import tkinter as Tkinter
import time
import keyboard

vDict_Configs = {
    "Keyboard_ClickKey" : '0',
    "Keyboard_ExitKey" : 'esc'
}

vBool_Clicking : bool = False

vWindow_MainWindow = Tkinter.Tk()
vWindow_MainWindow.title("AllDorothy")
vWindow_MainWindow.geometry("900x900")

vText_MainTextBox = Tkinter.Label(vWindow_MainWindow, text="Hello, world!\nh\nh")

vText_MainTextBox.pack(pady=5)

vWindow_MainWindow.mainloop()

# while True:
#     if keyboard.is_pressed(vDict_Configs['Keyboard_ExitKey']):
#         break
#     if keyboard.is_pressed(vDict_Configs["Keyboard_ClickKey"]):
#         print("Entry")
#         vBool_Clicking = not vBool_Clicking
#         time.sleep(0.2)
#         print(vBool_Clicking)
        
#     if vBool_Clicking:
#         PyAuto.leftClick()
#         time.sleep(0.0001)
        