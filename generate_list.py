import random
def generate_list():
  alist = [x for x in range (random.randint(-10, 10)) ]
  return alist
  
def printIt():
  print( generate_list() )
  
def main ():
  printIt()
  
"""
If this script file is called, it will run main() directly
"""

if __name__=='_main_':
  print("test printIt(): ")
  main()
