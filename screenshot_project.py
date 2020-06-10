from PIL import Image, ImageGrab
import os


def screenshot(area):
  img = ImageGrab.grab()
  cropped_img = img.crop(area)
  img.show()
  return cropped_img

def save(img, name, i, folder):
  if not os.path.isdir(folder):
    os.mkdir(folder)
  img.save(f'{folder}/{name}{i}.png')


def main():
  name = input("what is the name of the files? ")
  folder = input("folder name to save the pictures? ")
  top_left_x = int(input("top left x "))
  top_left_y = int(input("top left y "))
  
  bottom_right_x = int(input("bottom right x "))
  bottom_right_y = int(input("bottom right y "))

  area = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
  print(area)
  i = 0
  while True:
    i+=1
    command = input("press any key to take a screenshot, press q to stop the program ")
    if command == "q":
      break
    screenshot(area)
    img = screenshot(area)
    save(img, name, i, folder)

main()


