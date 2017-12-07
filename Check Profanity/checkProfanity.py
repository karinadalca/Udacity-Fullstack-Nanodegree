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
  print(output)

  connection.close()

read_text()