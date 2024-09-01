#MadLib.py
#Name: Jakob Cimino
#Date: 9/1/2024
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter a noun")
  noun2 = input("Enter a noun")
  noun3 = input("Enter a noun")
  noun4 = input("Enter a noun")
  noun5 = input("Enter a noun")
  noun6 = input("Enter a noun")
  #Print the story with the user supplied words.

  print("I like to ride a" , noun1 ,  "with my friend" , noun2 , "is fun.")
  print("I like to play" , noun3 ,  "with my team" , noun4 , "are great.")
  print("I like to eat at" , noun5 ,  "with my family because the" , noun6 , "is good.")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
