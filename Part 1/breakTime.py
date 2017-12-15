import webbrowser
import time

n = 0

print("This program stated at "+time.ctime())

while(n<=2):
  time.sleep(2*60*60)
  webbrowser.open("https://www.youtube.com/watch?v=q2mHegrncZo")
  n=n+1