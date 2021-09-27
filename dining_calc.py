from datetime import date,datetime
from main import daysbetween

def calc():
    print("You have",int(input("Enter amount of dining dollars you have remaining: "))/daysbetween(date.today(),"2021-12-17"),"dining dollars per day for the rest of the semester.")

def main():
    calc()

if __name__=="__main__":
    main()
