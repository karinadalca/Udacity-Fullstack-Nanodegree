class brad:
  b = "My name is brad"

def check_if_instance():
  newBrad = brad()
  checkInstance = isinstance(newBrad, brad)
  print(checkInstance)

check_if_instance()