import tkinter as tk
import time
import sys
import winsound

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second

window = tk.Tk()
window.title("Countdown")
sa = sys.argv

hours = int(sys.argv[1])
minutes = int(sys.argv[2])
seconds = int(sys.argv[3]) 

def display(i, j, k):
	if i == j == k == 0:
		label.configure(text = "{}:{}:{}".format(str(i).zfill(2), str(j).zfill(2), str(k).zfill(2)))
		winsound.Beep(frequency, duration)
		time.sleep(1)
		label.update()
		winsound.Beep(frequency, duration = 3000)
		time.sleep(1)
		label.configure(text = "TIME\'S UP")
		label.update()	
	elif k >= 0:
		label.configure(text = "{}:{}:{}".format(str(i).zfill(2), str(j).zfill(2), str(k).zfill(2)))
		winsound.Beep(frequency, duration)
		time.sleep(1)
		label.update()					
	else:
		pass

def start_counter():
	for i in range(hours, -1, -1):
		if i == hours:
			for j in range(minutes, -1, -1):
				if j == minutes:
					for k in range(seconds, -1, -1):
						display(i, j, k)
				else:
					for k in range(59, -1, -1):
						display(i, j, k)
		elif i >= 0 and i < hours:
			for j in range(59, -1, -1):
				for k in range(59, -1, -1):
					display(i, j, k)
		else:
			pass


window.configure(bg = "black")
label = tk.Label(window, fg = "green", bg = "black", text = "Counter", font = ("MS Gothic Bold", 150), height = 700)
label.pack()
label.config(anchor = "center")
window.overrideredirect(True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))

if len(sa) > 1:
	if minutes >= 60 or seconds >= 60:
		print("Invalid time")
	else:
		start_counter()
		window.mainloop()
