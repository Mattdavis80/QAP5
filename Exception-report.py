# QAP5 - The Final
# Author: Matthew Davis
# Last Updated: March 28, 2023
# Purpose of program is to create both an Exception Report from the Polices.dat file

# Import Statements
import datetime

# Constants
# Opening OSICDef.dat file to access stored variables
f = open("OSICDef.dat", 'r')

# Creating empty list to store constants
CONSTANTS = []

# Iterating through each line in OSICDef.dat file,stripping whitespace, then adding it to our constants list
for line in f:
    CONSTANTS.append(line.strip())

# Closing file
f.close

# Declaring constants from position in constant list
EX_LIABILITY_RATE = float(CONSTANTS[3])
GLASS_COVERAGE_RATE = float(CONSTANTS[4])
LOANER_CAR_RATE = float(CONSTANTS[5])
HST_RATE = float(CONSTANTS[6])
PROCESS_FEE = float(CONSTANTS[7])

# Initializing Counter/Sum Variables
tot_policies = 0
total_premium_sum = 0
hst_sum = 0
tot_cost_sum = 0
monthly_pay_sum = 0

# Date variable for report
today = datetime.date.today()

# Printing header for report
print()
print()
print("ONE STOP INSURANCE COMPANY")
print(f"MONTHLY PAYMENT LISTING AS OF {today}")
print()
print("POLICY CUSTOMER                 TOTAL                   TOTAL        MONTHLY")
print("NUMBER NAME                    PREMIUM       HST        COST         PAYMENT")
print("=" * 76)

# Opening Policies.dat file
f = open("Policies.dat", 'r')

# Defining loop to iterate over each line in Policies.dat
for policy_data in f:

# Creating a list from each line in Policies.dat, Separating each item at ","
    policy = policy_data.split(",")

# Variables needed for display and calculation, taken from list
    policy_num = policy[0].strip()
    cust_first = policy[2].strip()
    cust_last = policy[3].strip()
    insur_prem = float(policy[14].strip())
    num_cars = int(policy[9].strip())
    ex_liability = (policy[10].strip())
    glass_coverage = (policy[11].strip())
    loaner_car = (policy[12].strip())
    monthly_payment = (policy[13].strip())

# If statement only taking into account records with a monthly payment
    if monthly_payment == "M":
    # Calculated Variables
        extra_costs = 0 # Initializing extra costs variable, will reset with each loop iteration

        # If statements that add value to extra_costs variable if selected in records, indicated by "Y"
        if ex_liability == "Y":
            extra_costs += (num_cars * EX_LIABILITY_RATE)
        if glass_coverage == "Y":
            extra_costs += (num_cars * GLASS_COVERAGE_RATE)
        if loaner_car == "Y":
            extra_costs += (num_cars * LOANER_CAR_RATE)
    
        total_premium = insur_prem + extra_costs
        hst_amt = total_premium * HST_RATE
        total_cost = total_premium + hst_amt
        monthly_payment = (total_cost + PROCESS_FEE) / 12

    # Display Variables
        full_name  = (f"{cust_first} {cust_last}")
        dsp_tot_premium = "${:,.2f}".format(total_premium)
        dsp_hst_amt = "${:,.2f}".format(hst_amt)
        dsp_total_cost = "${:,.2f}".format(total_cost)
        dsp_monthly_payment = "${:,.2f}".format(monthly_payment)

    # Print Statement for inner report - shows policy information and calculated variables
        print(f" {policy_num}  {full_name:<20s}   {dsp_tot_premium:>9s}    {dsp_hst_amt:>7s}    {dsp_total_cost:>9s}    {dsp_monthly_payment:>9s}")

    # Adding to Counter/Sum variables to document totals
        tot_policies += 1
        total_premium_sum += (total_premium)
        hst_sum += (hst_amt)
        tot_cost_sum += (total_cost)
        monthly_pay_sum += (monthly_payment)

print("=" * 76)

# Display variables for totals
dsp_total_premium_sum ="${:,.2f}".format(total_premium_sum)
dsp_hst_sum= "${:,.2f}".format(hst_sum)
dsp_tot_cost_sum = "${:,.2f}".format(tot_cost_sum)
dsp_monthly_pay_sum = "${:,.2f}".format(monthly_pay_sum)

# Print statement for totals
print(f"Total Policies: {tot_policies:>3d}          {dsp_total_premium_sum:>10s} {dsp_hst_sum:>10s}   {dsp_tot_cost_sum:>10s}  {dsp_monthly_pay_sum:>11s}")

# Closing file
f.close




