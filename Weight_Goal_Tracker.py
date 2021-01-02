#This program tracks weightloss goals based on a few parameters. 
# The entries of initial weight and current weight establish the daily weight loss change/rate 
# which is used to extrapolate the target weight loss date

from datetime import datetime, timedelta

initial_weight = float(input("Enter initial weight in lbs: > "))

date_initial_weight = str(input("Enter your weigh-in date as YYYY-MM-DD: > "))
initial_weighin_date = datetime.strptime(date_initial_weight, "%Y-%m-%d")
current_weight = float(input("Enter current weight in lbs: > "))

if current_weight > initial_weight:
    print("\nYou're actually gaining weight and I am unable to establish a date when you will achieve your goal.")

else:
    target_weight = float(input("Enter target weight in lbs: > ")) 
    weight_change = current_weight - initial_weight
    w = weight_change
    date_current_weight = datetime.today()

    print("\n\nYour weight change since the weigh-in on", initial_weighin_date,"is", w,"lbs.")
    print("\nThe current date is", date_current_weight,"and your current weight is",current_weight,"lbs.")

    days_since_initial_weight = date_current_weight - initial_weighin_date
    d = days_since_initial_weight.days
    print ("\nIt's been" ,d ,"days since your first weigh-in on", initial_weighin_date,".")

    daily_weight_change = w/d
    dwc = round(daily_weight_change,3)
    print("\nSo far your daily weight change has been", dwc, "lbs.")


    unmet_weight_loss = current_weight - target_weight
    uwl = unmet_weight_loss
    ("\nYou still have", uwl, "lbs to lose.")
    days_to_target_weight_date = round(abs(uwl/dwc))
    target_weight_loss_date = date_current_weight + timedelta(days_to_target_weight_date)
    print("\nAt your current rate, you have",days_to_target_weight_date,"days to meet your goal.")  
    print("\nYou will meet your weight loss goal on", target_weight_loss_date,".")

    
          
                