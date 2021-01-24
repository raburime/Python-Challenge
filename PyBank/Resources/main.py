import os

# Module for reading CSV files
import csv

budget_data.csv = os.path.join("..", "Resources", "budget_data.csv")
print("csvpath.. " + csvpath)


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Calculates the total number of monthly records

    total_number_of_months = 0
    
    # Accumulates net profits and losses
    net_monthly_profit_loss = 0
    # Save previous month's data to use for comparing current month data
    #   to previous month's data
    previous_month_profit_loss = 0
    #   Holds the change between current month and previous month
    change_in_profit_loss_from_previous_month = 0
    #   Add all the profit and losses
    total_change_in_profit_loss_over_the_entire_period = 0
    greatest_increase_in_profit = 0
    Lowest_increase_in_profit = 0
    month_of_greatest_profit = ''
    month_of_greatest_decrease_in_profit = ''
    counter = 0
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
            #   save the date 
            date = str(row[0])
            # add the number of records/lines processed
            total_number_of_months = total_number_of_months + 1
            #   Obtain the monthly profit/loss
            net_monthly_profit_loss += int(row[1])
            if total_number_of_months != 1:
                change_in_profit_loss_from_previous_month = (previous_month_profit_loss - int(row[1]))
                #print(change_in_profit_loss_from_previous_month)
                
                #   Tracking the extreme profit and loss amounts and months
                if (change_in_profit_loss_from_previous_month > 0) and (change_in_profit_loss_from_previous_month > greatest_increase_in_profit):
                    greatest_increase_in_profit = change_in_profit_loss_from_previous_month
                    month_of_greatest_profit = str(row[0])
                    
                if (change_in_profit_loss_from_previous_month < 0) and (change_in_profit_loss_from_previous_month < Lowest_increase_in_profit):
                    Lowest_increase_in_profit = change_in_profit_loss_from_previous_month
                    month_of_greatest_decrease_in_profit = str(row[0]) 
            #       counter +=1
            total_change_in_profit_loss_over_the_entire_period += change_in_profit_loss_from_previous_month  
            #   Save data to use for comparison
            previous_month_profit_loss = int(row[1])
                       
    average_change_in_profit_loss_over_the_entire_period = (total_change_in_profit_loss_over_the_entire_period / total_number_of_months)       
    print ("")    
    print ("")
    print ("")      
    print ("Financial Analysis")
    print ("----------------------------")
    print("Total Months: " + str(total_number_of_months))
    print("Total: $" + str(net_monthly_profit_loss))
    #   Commented out - Not in report
    #print("Total Change in profit over the entire period " + "$" + str(total_change_in_profit_loss_over_the_entire_period))
    print("Average  Change: " + "($" + str(average_change_in_profit_loss_over_the_entire_period) + ")")
    print("Greatest Increase in Profits: " + month_of_greatest_profit + " " + "($" + str(greatest_increase_in_profit) + ")")
    print("Greatest Decrease in Profits: " + month_of_greatest_decrease_in_profit + " " + "($" + str(Lowest_increase_in_profit) + ")")
    #print("Counter: " + str(counter))