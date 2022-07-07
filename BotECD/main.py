import pyautogui

for i in range(1):
    pyautogui.PAUSE = 2
    pyautogui.doubleClick(x=590, y=227)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'tab')
    pyautogui.click(x=1139, y=707)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('alt', 'tab')
    pyautogui.press('esc')
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('alt', 'tab')
    pyautogui.press('down')
    pyautogui.press('left')



