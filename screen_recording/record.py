import time,threading
from datetime import datetime
from PIL import ImageGrab
from cv2 import *
import numpy as np
from pynput import keyboard

def video_record():
  global name
  name = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
  screen = ImageGrab.grab()
  width, high = screen.size
  fourcc = VideoWriter_fourcc('X', 'V', 'I', 'D')
  video = VideoWriter('%s.avi' % name, fourcc, 15, (width, high))
  print('recording will start after 3 seconds.')
  time.sleep(3)
  print('start recording!')
  print('Stop recording using keyboard ESC')
  global start_time
  start_time = time.time()
  while True:
    if flag:
      print("finish recording")
      global final_time
      final_time = time.time()
      video.release()
      break
    im = ImageGrab.grab()
    imm = cvtColor(np.array(im), COLOR_RGB2BGR)
    video.write(imm)
    # time.sleep(5)

def on_press(key):
  global flag
  if key == keyboard.Key.esc:
    flag = True
    return False

def video_info():
  video = VideoCapture('%s.avi' % name)
  fps = video.get(CAP_PROP_FPS)
  Count = video.get(CAP_PROP_FRAME_COUNT)
  size = (int(video.get(CAP_PROP_FRAME_WIDTH)), int(video.get(CAP_PROP_FRAME_HEIGHT)))
  path = os.path.abspath('.')
  print('fps=%.1f'%fps)
  print('f_count=%.1f'%Count)
  print('resolution',size)
  print('video_timo=%.3f秒'%(int(Count)/fps))
  print('record_time=%.3f秒'%(final_time-start_time))
  print('suggested_fps=%.2f'%(fps*((int(Count)/fps)/(final_time-start_time))))
  print('video in %s.avi'%path+name)

if __name__ == '__main__':
  flag = False
  th = threading.Thread(target=video_record)
  th.start()
  with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
  time.sleep(1)
  video_info()

