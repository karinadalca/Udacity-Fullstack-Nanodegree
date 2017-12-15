import urllib

def read_text():
  file = open("checkProfanity.txt", "r")
  contents = file.read()
  print(contents)
  check_profanity(contents)
  file.close()

def check_profanity(contents):
  connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+contents)
  output = connection.read()
  connection.close()

  if "true" in output:
    print("Profanity Alert!")
  elif "false" in output:
    print("This document has not curse words.")
  else:
    print("Could not scan the document properly")
      

read_text()