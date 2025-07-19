A=("make a lot of money") 
B=("buy now") 
C=("subscribe this")
D=("click this")
Check=input("Enter your comment")
if (A or B or C or D in Check):
  print("Spam detected")
else:
  print("Genuine message")