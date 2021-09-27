from datetime import  date,datetime

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
    d2=date.today()
    totaldays=daysbetween(d1,d2)
    possiblespent=totaldays*daily
    balence=input("Please enter how much funds you have remaining: ")
    surplus=int(possiblespent)-(int(funds)-float(balence))
    print("You have a surplus of ",round(surplus,2)," dining dollars. ")



def daysbetween(d1,d2):
    d1 = datetime.strptime(str(d1), "%Y-%m-%d")
    d2 = datetime.strptime(str(d2), "%Y-%m-%d")
    return abs((d2 - d1).days)

def main():
    calc()

if __name__=="__main__":
    main()