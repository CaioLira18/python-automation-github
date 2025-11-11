import pyautogui as pa
import time

pa.PAUSE = 0.5

pa.press('win')
pa.write('chrome')
pa.press("ENTER")
pa.click(x=1233, y=774)
pa.click(x=1201, y=589)
pa.click(x=1600, y=350)
pa.click(x=1600, y=350)
pa.click(x=1600, y=350)
pa.click(x=1600, y=350)
pa.click(x=1600, y=350)
pa.click(x=1600, y=350)
pa.click(x=1600, y=350)
pa.click(x=1600, y=580)
print(pa.position())