#Payroll program to calculate a weekly paycheck after taxes and deductions

# Constants
FEDERAL_TAX_RATE = 0.079
STATE_TAX_RATE = 0.056
OVERTIME_MULTIPLIER = 1.5
REGULAR_HOURS = 40

RATES = {
    # Employee ID : Hourly Rate
    'E001': 30.00, 'E002': 25.00, 'E003': 22.00, 'E004': 22.00, 'E005': 22.00,
    'E006': 22.00, 'E007': 22.00, 'E008': 22.00, 'E009': 22.00, 'E010': 22.00,
    'E011': 22.00, 'E012': 22.00, 'E013': 22.00, 'E014': 15.00, 'E015': 15.00
}
# Function to determine if user wants to continue
def prompt_continue():
    if input("Calculate payroll (y/n)?").lower() != 'y':
        print("End of job, program complete.")
        return False
    else:
        return True
# Function to get employee input
def get_input():
    employeeId = input("Enter employee ID: ")
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    hoursWorked = float(input("Enter hours worked: "))
    return [employeeId, firstName, lastName, hoursWorked]
def get_employee_rate(employeeId):
    return RATES.get(employeeId)
def calculate_gross_pay(hoursWorked, hourlyRate):
    if hoursWorked <= REGULAR_HOURS:
        grossPay = hoursWorked * hourlyRate
    else:
        overtimeHours = hoursWorked - REGULAR_HOURS
        grossPay = (REGULAR_HOURS * hourlyRate) + (overtimeHours * hourlyRate * OVERTIME_MULTIPLIER)
    return grossPay
def calculate_deductions(grossPay):
    federalTax = grossPay * FEDERAL_TAX_RATE
    stateTax = grossPay * STATE_TAX_RATE
    totalDeductions = federalTax + stateTax
    return totalDeductions
def display_paycheck(employeeId, firstName, lastName, hoursWorked, hourlyRate, grossPay, totalDeductions, netPay):
    print("\nPayroll Summary")
    print("----------------------------")
    print(f"Employee ID: {employeeId}")
    print(f"Name: {firstName} {lastName}")
    print(f"Hours Worked: {hoursWorked:.2f}")
    print(f"Hourly Rate: ${hourlyRate:.2f}")
    print(f"Gross Pay: ${grossPay:.2f}")
    print(f"Total Deductions: ${totalDeductions:.2f}")
    print(f"Net Pay: ${netPay:.2f}")
    print("----------------------------\n")
# Main program loop
while prompt_continue():
    employeeId, firstName, lastName, hoursWorked = get_input()
    hourlyRate = get_employee_rate(employeeId)
    if hourlyRate is None:
        print("Invalid employee ID. Please try again.")
        continue
    grossPay = calculate_gross_pay(hoursWorked, hourlyRate)
    totalDeductions = calculate_deductions(grossPay)
    netPay = grossPay - totalDeductions
    display_paycheck(employeeId, firstName, lastName, hoursWorked, hourlyRate, grossPay, totalDeductions, netPay)

