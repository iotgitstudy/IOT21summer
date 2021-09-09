import keyboard
from PIL import ImageGrab
import time
def screenshot():
    # 2021년 9월 9일 21시 40분 30초 -> 20210909_214030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F9", screenshot) # 사용자가 F9누를 때 스크린 샷 저장

keyboard.wait("esc") #사용자가 esc를 누를 때까지 프로그램 수행