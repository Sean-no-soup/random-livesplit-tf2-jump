from os import listdir,startfile,path
from random import choice
from tkinter import Tk
import xml.etree.ElementTree as ElementTree

#make sure this is correct
map_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Team Fortress 2\\tf\\maps"
save_path = path.dirname(__file__)+"\\" #saving to local directory

jumplist = [item[:-4] for item in listdir(map_path) if "jump" in item]
random_jump = choice(jumplist)
print(random_jump+' selected')

root = Tk()
root.after_idle(root.withdraw)
root.after_idle(root.clipboard_clear)
root.after_idle(root.clipboard_append, f"map {random_jump}")
root.after_idle(print, 'The clipboard is ready.')
root.after(15000, root.destroy) #wait 15 seconds so text is readable

try:
    startfile(f"{save_path}{random_jump}.lss")
except:
    print('failed to open file: creating a new one')
    tree = ElementTree.parse(f"{save_path}template_jump.lss")
    base = tree.getroot()
    base.findall('CategoryName')[0].text = random_jump
    tree.write(f"{save_path}{random_jump}.lss")
    print(f"{random_jump}.lss created")
    startfile(f"{save_path}{random_jump}.lss")

root.mainloop()