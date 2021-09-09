from datetime import  date,datetime

def calc():
    mealplan=input("Please enter the number corresponding to your meal plan: 1=$3500/semester 2=$3020/semester:")
    if(mealplan==1) {
        funds=3500 #WHY DOESNT THIS WORK WTF PYTHON
        weekly=219
        daily=(weekly/7)
    } else {
        funds=3020
        weekly=189
        daily=(weekly/7)
    }
    movein=input("Please enter the day in August that you moved in: ")
    d1= date(2021,8,movein)
    d2=date.today()
    totaldays=daysbetween(d1,d2)
    possiblespent=totaldays*daily
    balence=input("Please enter how much funds you have remaining: ")
    surplus=(funds-balence)-possiblespent
    print("You have: ",surplus," dining dollars remaining. ")



def daysbetween(d1,d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def main():
    calc()
main()