"""Algorithn
-Step1:get marks from the student
-Step2:check that marks, if less than 40, display "you are fail",otherwise display:you are pass
end"""

try:
    conter = 0
    rang = []
    while conter < 5:
        Rating = int(input("enter you Rating\t"))
        rang.append(Rating)
        conter+=1
    average = (sum(rang)/len(rang))
    if average > 40:
        print("you are pass".center(50,"="))
    else:
        print("you are fail".center(50,"="))
except Exception as e:
    print(f"error{e}")