'''
Quiz for basic Git and GitHub Commands
Python 3
'''

#import Python library for color and formatting
from termcolor import colored

print("Welcome to the Git & GitHub Quiz!")

#Loop to allow user redo quiz multiple times
while True:

  #Set total score to 0
  scoreTotal = 0

  print("\nLets get started, there are 20 questions total - Good Luck!")

# -----------------------------------------------------------------
  print("\nList all the files in this branch")
  print(colored("KingKong@DESKTOP-TIKKIRIKKI MINGW64 /c/repos/my-branch-tutorial",'green'))  
  q1 = input("$ ")
  a1 = "ls"

  if q1 == a1:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:",colored(a1, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nList all the files in this branch, including hidden files")
  print(colored("KingKong@DESKTOP-TIKKIRIKKI MINGW64 /c/repos/my-branch-tutorial",'green'))  
  q2 = input("$ ")
  a2 = "ls -a"

  if q2 == a2:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:",colored(a2, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nCreate a new directory named my-best-program")
  
  q3 = input("$ ")
  a3 = "mkdir my-best-program"

  if q3 == a3:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a3, 'blue'), ". Check for typos!")
 
# -----------------------------------------------------------------
  print("\nChange directory to my-best-program")
  
  q4 = input("$ ")
  a4 = "cd my-best-program"

  if q4 == a4:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a4, 'blue'), ". Check for typos!")
 
# -----------------------------------------------------------------

  print("\nEnter command to check what GitHub URL the current repo is connected to")
  
  q5 = input("$ ")
  a5 = "git remote -v"

  if q5 == a5:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a5, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nEnter the command to initialize a git repository")
  
  q6 = input("$ ")
  a6 = "git init"

  if q6 == a6:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a6, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nEnter the command to move all changes to the staging area")
  
  q7 = input("$ ")
  a7 = "git add ."

  if q7 == a7:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a7, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nEnter the command to check the state of your local git repository.")
  print("This will show changes that have been staged and which files aren't being tracked")
  
  q8 = input("$ ")
  a8 = "git status"

  if q8 == a8:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a8, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nEnter command to save changes in repository and add message \"Fixed it\"")
  
  q9 = input("$ ")
  a9 = 'git commit -m "Fixed it"'
  a9b = "git commit -m 'Fixed it'"

  if ((q9 == a9) or (q9 == a9b)):
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a9, 'blue'), ". Check for typos!")
# -----------------------------------------------------------------

  print("\nYour GitHub site is https://github.com/kingkong/my-cool-code.git")
  print("Enter the command to link to your GitHub repository")
  
  q10 = input("$ ")
  a10 = "git remote add origin https://github.com/kingkong/my-cool-code.git"
  
  if q10 == a10:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a10, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nEnter command to push commits to remote repository. Don't forget -u.")
  
  q11 = input("$ ")
  a11 = "git push -u origin master"

  if q11 == a11:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a11, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nLook at the following path below. What is the name of the branch?")
  print(colored("KingKong@DESKTOP-TIKKIRIKKI /c/repos/my-branch-tutorial (master)",'green'))
  
  q12 = input("$ ")
  a12 = "master"

  if q12 == a12:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a12, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nLook at the following path below. What is the name of the branch?")
  print(colored("KingKong@DESKTOP-TIKKIRIKKI /c/repos/my-branch-tutorial (enhancement)",'green'))
  
  q13 = input("$ ")
  a13 = "enhancement"

  if q13 == a13:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a13, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nEnter the command to create a new branch called bugfix, but stay in the current branch")
  
  q14 = input("$ ")
  a14 = "git branch bugfix"

  if q14 == a14:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a14, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nEnter the command to show all branches")
  
  q15 = input("$ ")
  a15 = "git branch"

  if q15 == a15:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a15, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nEnter the one-line command to create a new branch called hotfix and switch to it.")
  
  q16 = input("$ ")
  a16 = "git checkout -b hotfix"

  if q16 == a16:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a16, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nLook at the following path below. Switch to bugfix branch")
  print(colored("KingKong@DESKTOP-TIKKIRIKKI /c/repos/my-branch-tutorial (master)",'green'))  

  
  q17 = input("$ ")
  a17 = "git checkout bugfix"

  if q17 == a17:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a17, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nEnter the command to view history of previous commits")
  
  q18 = input("$ ")
  a18 = "git log"

  if q18 == a18:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a18, 'blue'), ". Check for typos!")
    
# -----------------------------------------------------------------
  print("\nYou are currently in the master branch. Merge in changes from branch called hotfix")
  print(colored("KingKong@DESKTOP-TIKKIRIKKI /c/repos/my-branch-tutorial (master)",'green'))  

  q19 = input("$ ")
  a19 = "git merge hotfix"

  if q19 == a19:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a19, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------
  print("\nEnter the command to delete the branch 'bugfix'")
  
  q20 = input("$ ")
  a20 = "git branch -d bugfix"

  if q20 == a20:
    print("Correct!")
    scoreTotal = scoreTotal + 1
  else:
    print("Incorrect. The answer is:", colored(a20, 'blue'), ". Check for typos!")

# -----------------------------------------------------------------

  #Calculate score percentage
  scorePrc = (scoreTotal/20)*100

  #Display total score to user
  if scorePrc >= 80:
    print("\nCongraduations! You've passed the quiz!")
    print("Your total score is: ", scoreTotal, "/20. Which is ", scorePrc, "%")
  else:
    print("\nOh man. You did not pass...keep trying, you'll get it!")
    print("Your total score is: ", scoreTotal, "/20. Which is ", "{:.2f}".format(scorePrc), "%")

  #Allow user to jump back into loop and retake quiz
  print("\nDo you want to redo this quiz? ")
  userInput = input("Yes or No? ")
  if ((userInput == "No") or (userInput == "no")):
    break

#Out of loop message - Bid user farewell
print(colored('\nAlrightly, have a good one!', 'yellow'))