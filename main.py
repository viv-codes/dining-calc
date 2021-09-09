from datetime import  date,datetime
print(date.today())

def calc():
    mealplan=input("Please enter the number corresponding to your meal plan: 1=$3500/semester 2=$3020/semester:")
    if(mealplan==1):
        funds=3500
        weekly=219
        daily=(weekly/7)
    else:
        funds=3020
        weekly=189
        daily=(weekly/7)
    d1=input("Please enter the day that you moved in in the format yyyy-mm-dd: ")
    totaldays=daysbetween(d1)
    possiblespent=totaldays*daily
    balence=input("Please enter how much funds you have remaining: ")
    surplus=(int(funds)-int(balence))-int(possiblespent)
    print("You have a surplus of ",surplus," dining dollars. ")



def daysbetween(d1):
    d1 = datetime.strptime(str(d1), "%Y-%m-%d")
    d2 = datetime.strptime(str(date.today()), "%Y-%m-%d")
    return abs((d2 - d1).days)

def main():
    calc()

main()