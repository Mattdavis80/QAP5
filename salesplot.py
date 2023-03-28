# Yearly Sales Graph Generator - QAP4
# Author: Matthew Davis - Keyin College Software Development Student
# Last Updated: March 19, 2023

# Import Statements
import calendar
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Variables defined to store information as a list
x_axis = []
y_axis = []

# User input to select the current month in their program, validated as number between 1-12
while True:
    try:
        curr_month = int(input("Please enter the current month as as number(1-12): "))
    except:
        print("Please enter a valid number")
    else:
        if curr_month < 1 or curr_month > 12:
            print("Please enter a valid month between 1 and 12")
        else:
            break

# This section uses an in range loop to iterate over the 12 months of the year
for i in range(1, 13):
# Using the calendar library, the abbreviated month name is appended to the x-axis list
    x_axis.append(calendar.month_abbr[i])

# While the current loop is less than the current user entered month, they will be prompted to enter a valid positive number
# of the total sales of that month
    if i <= curr_month:
        while True:
            try:
                sales_amt = float(input("Enter the total sales for {}: ".format(calendar.month_name[i])))
                sales_amt = round(sales_amt,2)
            except:
                print("Please enter a valid number")
            else:
                if sales_amt < 0:
                    print("Please enter a positive number")
                else:
                    break
        y_axis.append(sales_amt)
    else:
# Once the current month is surpassed there are no sales to record, therefore the value is set to 0
        y_axis.append(0)

# Average of sales, not including months past current month
avg_sales = sum(y_axis[:curr_month]) / curr_month

# Variable used to change color of bar graph, if sales is less than average bar color will be Red
# If sales are above average, bar color will be green
# bar_color = ['red' if value < avg_sales else 'green' for value in y_axis ]
col = []
for val in y_axis:
    if val > avg_sales:
        col.append("green")
    elif val == avg_sales:
        col.append("orange")
    else:
        col.append("red")

# Variable used to store labels for graph, if value == 0, label is hidden
labels = []
for num in y_axis:
        if num == 0:
            labels.append("")
        else:
            labels.append(num)

# Defining custom legend using mathplotlib patches
below_avg = mpatches.Patch(color='red', label='Less Than Average Sales')
above_avg = mpatches.Patch(color='green', label='Greater Than Average Sales')
avg = mpatches.Patch(color='Orange', label='Average Sales')


# Plot the bar graph with modified legend labels and colors
bar_graph = plt.bar(x_axis, y_axis, color=col)
plt.xlabel("Month")
plt.ylabel("Sales in $")
if curr_month == 1:
    plt.title(f"January Sales")
else:
    plt.title("Sales from {} to {}".format(calendar.month_name[1], calendar.month_name[curr_month]))
plt.bar_label(bar_graph, labels=labels, label_type="center")
plt.axhline(avg_sales, color="orange")
plt.legend(handles=[avg, above_avg, below_avg], loc="best")

# Show the graph
plt.show()





