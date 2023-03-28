# QAP 4 - One Stop Insurance Company - Python Program
# Author: Matthew Davis
# Last Updated: March 16, 2023

# Import Statements
import datetime
import re
import time

# Constants - Read from OSICDef.dat file
f = open('OSICDef.dat', 'r')  # Opening file to access stored information

POLICY_NUM = int(f.readline())
BASIC_PREM_RATE = float(f.readline())
ADD_DISCOUNT_RATE = float(f.readline())
EX_LIABILITY_RATE = float(f.readline())
GLASS_COV_RATE = float(f.readline())
LOANER_RATE = float(f.readline())
HST_RATE = float(f.readline())
MON_PRO_FEE = float(f.readline())

f.close() # Closing file to stop accessing stored information

# Validation Lists
valid_prov = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]



while True:
# While true to allow users to make as many entries as they need, option to break from statement at end of each receipt 

# User Validated Inputs
# First name, mandatory input, alpha only, converted to Title-case
    while True:
        f_name = input("First Name:                    ").title()
        if f_name == "":
            print("First name cannot be empty, Please re-enter")
        elif not f_name.isalpha():
            print("Please enter a valid name")
        else:
            break

# Last name, mandatory input, alpha only, converted to Title-case
    while True:
        l_name = input("Last Name:                     ").title()
        if l_name == "":
            print("Last name cannot be empty, Please re-enter")
        elif not l_name.isalpha():
            print("Please enter a valid name")
        else:
            break

# Street Address, mandatory input, converted to Title-case
    while True:
        str_add = input("Street Address:                ").title()
        if str_add == "":
            print("Street address cannot be empty, Please re-enter")
        else:
            break

# City, mandatory input,  converted to Title-case
    while True:
        city = input("City:                          ")
        if city == "":
            print("City cannot be empty, Please re-enter")
        else:
            break

# Province, mandatory input,converted to Upper-case, compared to valid list of provinces
    while True:
        prov = input("Province (XX):                 ").upper()
        if len(prov) != 2:
            print("Please re-enter province as (XX)")
        elif prov == "":
            print("Province field cannot be empty, Please re-enter")
        elif not prov in valid_prov:
            print("Please enter a valid province")
        else:
            break

# Postal Code, mandatory input, must be valid format as X0X 0X0 ------ADD REPLACE STATEMENTS 
# The pattern below is used to compare against user input, this will be done using Regular Expressions
# The pattern will accept a space or dash between postal code
    pattern = r"^[A-Z]\d[A-Z][ -]?\d[A-Z]\d$"

    while True:
        post_code = input("Postal Code: (e.g. A1A 1A1):   ").upper()
        if re.match(pattern, post_code):
            break
        else:
            print("Invalid postal code. Please re-enter")

# Phone Number, mandatory input, 10 characters long
    while True:
        phone_num = input("Phone number (Without Spaces): ")
        phone_num = phone_num.replace("-", "")
        phone_num = phone_num.replace("/", "")
        if len(phone_num) != 10:
            print("Please format phone number as 10 digits without spaces")
        elif not phone_num.isdigit():
            print("Please enter a valid phone number")
        else:
            formatted_phone_num = phone_num[:3] + "-" + phone_num[3:6] + "-" + phone_num[6:]
            break
    
# Number of cars to insure, valid number greater than 0, mandatory input
    while True:
        try:
            num_cars = int(input("Number of cars to insure:      "))
        except:
            print("Please enter a valid number")
        else:
            if num_cars < 1:
                print("Please enter a number greater than 1")
            else:
                break
    
# Option for extra liability, Y/N, mandatory input
    while True:
        ex_insurance = input("Would you like to purchase extra insurance (Y/N):                ").upper()
        if ex_insurance == "Y" or ex_insurance == "N":
            break
        else:
            print("Please select Y for yes, or N for no")

# Option for glass coverage, Y/N, mandatory input
    while True:
        glass_cov = input("Would you like to purchase additional glass coverage (Y/N):      ").upper()
        if glass_cov == "Y" or glass_cov == "N":
            break
        else:
            print("Please select Y for yes, or N for no")

# Option for car loaner, Y/N, mandatory input
    while True:
        loaner_car = input("Would you like to purchase additional loaner car coverage (Y/N): ").upper()
        if loaner_car == "Y" or loaner_car == "N":
            break
        else:
            print("Please select Y for yes, or N for no")

# Option for Monthly or Yearly Payments, F/M, mandatory input
    while True:
        pay_method = input("Would you like to pay in monthly or yearly installments (M/Y)    ").upper()
        if pay_method == "M" or pay_method == "Y":
            break
        else:
            print("Please select M for Monthly, or Y for Yearly")
    
# Variable to store text for payment frequency on receipt
    if pay_method == "M":
        payment_text = "Monthly"
    else:
        payment_text = "Yearly"

# Date variables for invoice
    today = datetime.date.today()
    first_payment = datetime.date(today.year, today.month + 1, 1)


# Calculated variables

# First car rate is the Constant Basic Premium Rate
    first_car = BASIC_PREM_RATE

# Each additional car is discounted at 25% off
    add_cars = ((num_cars - 1) * BASIC_PREM_RATE) * (1 - ADD_DISCOUNT_RATE) 

# The Basic Premium Cost is the sum of the First Car cost and Additional Car Costs
    basic_prem = first_car + add_cars

# This portion calculates the cost of each additional add-on, if selected, the cost is multiplied by the number of cars in the plan.
    if ex_insurance == "Y":
        ex_insurance_cost = num_cars * EX_LIABILITY_RATE
    else:
        ex_insurance_cost = 0

    if glass_cov == "Y":
        glass_cov_cost = num_cars * GLASS_COV_RATE
    else:
        glass_cov_cost = 0
    
    if loaner_car == "Y":
        loaner_car_cost = num_cars * LOANER_RATE
    else:
        loaner_car_cost = 0

# The total Extra Costs is the sum of all additional benefits
    extra_costs = ex_insurance_cost + glass_cov_cost + loaner_car_cost

# Total Insurance Premium is the sum of the Basic Premium and Extra Costs
    tot_insur_premium = basic_prem + extra_costs

# HST Calculation , 15%(HST rate) of total insurance premium
    hst = HST_RATE * tot_insur_premium

# Total cost, HST + Total Insurance Premium
    total_cost = tot_insur_premium + hst

    if pay_method == "M":
        total_cost += MON_PRO_FEE


# Display variables
    full_name = (f"{f_name} {l_name}")
    dsp_first_car_cost = "${:,.2f}".format(BASIC_PREM_RATE)
    dsp_add_car_cost = "${:,.2f}".format(add_cars)
    dsp_basic_prem = "${:,.2f}".format(basic_prem)
    dsp_ex_insurance_cost = "${:,.2f}".format(ex_insurance_cost)
    dsp_glass_cov_cost = "${:,.2f}".format(glass_cov_cost)
    dsp_loaner_car_cost = "${:,.2f}".format(loaner_car_cost)
    dsp_hst = "${:,.2f}".format(hst)
    dsp_total_cost = "${:,.2f}".format(total_cost)
    dsp_extra_costs = "${:,.2f}".format(extra_costs)
    dsp_MON_PRO_FEE = "${:,.2f}".format(MON_PRO_FEE)
    dsp_monthly_payment = "${:,.2f}".format(total_cost / 8)


# Loading text for recept generation
    print()
    print("Preparing Document, please wait")
    loading_text = "...."

    for char in loading_text:
        print(char, end="", flush=True)
        time.sleep(0.5)
    print(f" Report complete for Policy: {POLICY_NUM} ")
    time.sleep(1)
# Receipt generation 
    print()
    print()
    print("One Stop Insurance Company".center(75, "-"))
    print("Insurance Claim Receipt".center(75))
    print()
    print(f"Policy Number: {POLICY_NUM}")
    print("-------------------")
    print()
    print(f"Date Processed:       {today}")
    print(f"Client Name:          {full_name}")
    print(f"Phone Number:         {formatted_phone_num}")
    print(f"Address:              {str_add}, {city}, {prov} ")
    print(f"                      {post_code}")
    print("-" * 75)
    print(" " * 42, "Basic Premium".center(33))
    print(f"Number of Cars Insured: {num_cars:>2d}                First Car Cost:           {dsp_first_car_cost:>7s} ")
    print(f"Payment Frequency:       {payment_text:<7s}          Additional Car Cost:    {dsp_add_car_cost:>9s}   ")
    print(f"                                          Basic Premium Total:   {dsp_basic_prem:>10s}")
    print(f"                                          ---------------------------------")
    print(" " * 42, "Extra Costs".center(33))
    print(f"                                          Extra Liability Cost:  {dsp_ex_insurance_cost:>10s}")
    print(f"                                          Glass Coverage Cost:   {dsp_glass_cov_cost:>10s}")
    print(f"                                          Loaner Car Cost:       {dsp_loaner_car_cost:>10s}")
    print(f"                                          Total Extra Costs:     {dsp_extra_costs:>10s}")
    print(f"                                          ---------------------------------")
    print(" " * 42, "Totals".center(33))
    print(f"                                          HST:                   {dsp_hst:>10s}")
    if pay_method == "M":
        print(f"                                          Processing Fee:            {dsp_MON_PRO_FEE:>6s}")
    print(f"                                          Total Cost:            {dsp_total_cost:>10s}")
    print()

    if pay_method == "M":
        print(f"                                          Monthly Payment:       {dsp_monthly_payment:>10s}")
    else:
        print(f"                                          Yearly Payment:        {dsp_total_cost:>10s}")

    print()
    print(f"Next Payment date: {first_payment}")
    print("-" * 75)

# Opening Policies.dat file to store information from user input
    f = open("Policies.dat", "a")
# Writing to file with information below
    f.write("{}, ".format(str(POLICY_NUM)))
    f.write("{}, ".format(today))
    f.write("{}, ".format(f_name))
    f.write("{}, ".format(l_name))
    f.write("{}, ".format(str_add))
    f.write("{}, ".format(city))
    f.write("{}, ".format(prov))
    f.write("{}, ".format(post_code))
    f.write("{}, ".format(formatted_phone_num))
    f.write("{}, ".format(str(num_cars)))
    f.write("{}, ".format(ex_insurance))
    f.write("{}, ".format(glass_cov))
    f.write("{}, ".format(loaner_car))
    f.write("{}, ".format(pay_method))
# Last input requires a line break
    f.write("{}\n".format(str(tot_insur_premium)))

# Command to close the file when finished appending
    f.close()

    
# Increment Policy Number for new invoice
    POLICY_NUM += 1
    f = open("OSICDef.dat", 'w')
    f.write("{}\n".format(str(POLICY_NUM)))
    f.write("{}\n".format(str(BASIC_PREM_RATE)))
    f.write("{}\n".format(str(ADD_DISCOUNT_RATE)))
    f.write("{}\n".format(str(EX_LIABILITY_RATE)))
    f.write("{}\n".format(str(GLASS_COV_RATE)))
    f.write("{}\n".format(str(LOANER_RATE)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(MON_PRO_FEE)))
    f.close
# ask user to continue
    while True:
        continue_script = input("Would you like to start another Invoice (Y/N):  ").upper()
        if continue_script == "Y":
            break
        elif continue_script == "N":
            exit()
        else:
            print("Please enter (Y) to continue or (N) to exit") 