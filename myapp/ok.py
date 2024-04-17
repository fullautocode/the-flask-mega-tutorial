import pyautogui
import time

# Wait for 5 seconds to give you time to select the text field
time.sleep(2)

for i in range(20):
    # Type 'ok'
    pyautogui.write('katy wants to be part of the conversation, also wheres porter at @Mack Porter')

    # Press 'enter'
    pyautogui.press('enter')

    time.sleep(1)




        