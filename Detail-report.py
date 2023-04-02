# QAP5 - The Final
# Author: Matthew Davis
# Last Updated: March 28, 2023
# Purpose of program is to create both a Detail Report from the Polices.dat file

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

# Counter/Sum Variables
tot_policies = 0
insurance_prem_sum = 0
extras_sum = 0
total_premium_sum = 0

# Date variable for report
today = datetime.date.today()

# Printing header for report
print()
print()
print("ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTING AS OF {today}")
print()
print("POLICY CUSTOMER              INSURANCE       EXTRA        TOTAL")
print("NUMBER NAME                   PREMIUM        COSTS       PREMIUM")
print("=" * 64)

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

# Calculated Variables
    extra_costs = 0 # Initializing extra costs variable, will reset with each loop iteration
    if ex_liability == "Y":
        extra_costs += (num_cars * EX_LIABILITY_RATE)
    if glass_coverage == "Y":
        extra_costs += (num_cars * GLASS_COVERAGE_RATE)
    if loaner_car == "Y":
        extra_costs += (num_cars * LOANER_CAR_RATE)

    total_premium = insur_prem + extra_costs

# Display Variables
    full_name  = (f"{cust_first} {cust_last}")
    dsp_insur_prem = "${:,.2f}".format(insur_prem)
    dsp_extra_costs = "${:,.2f}".format(extra_costs)
    dsp_tot_premium = "${:,.2f}".format(total_premium)

# Print Statement for inner report - shows policy information and calculated variables
    print(f" {policy_num}  {full_name:<20s}  {dsp_insur_prem:>9s}    {dsp_extra_costs:>9s}    {dsp_tot_premium:>9s}")

# Adding to Counter/Sum variables to document totals
    tot_policies += 1
    insurance_prem_sum += insur_prem
    extras_sum += extra_costs
    total_premium_sum += total_premium

print("=" * 64)

# Display variables for totals
dsp_insurance_prem_sum = "${:,.2f}".format(insurance_prem_sum)
dsp_extras_sum = "${:,.2f}".format(extras_sum)
dsp_total_premium_sum = "${:,.2f}".format(total_premium_sum)

# Print statement for totals
print(f"Total Policies: {tot_policies:>3d}        {dsp_insurance_prem_sum:>11s}  {dsp_extras_sum:>11s}  {dsp_total_premium_sum:>11s}")

# Closing file  
f.close




