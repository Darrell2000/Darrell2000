// This pseudocode is intended to display employee net pay values.
// All employees have a standard $45 deduction from their checks.
// If an employee does not earn enough to cover the deduction
// an error message is displayed.
start
    Declarations
        string name
        num hours
        num rate
        num DEDUCTION = 45
        string EOFNAME = "ZZZ"
        num gross
        num net

    output "Enter first name or", EOFNAME, "to quit"
    input name

    while name not equal to EOFNAME do
        output "Enter hours worked for", name
        input hours
       
        output "Enter hourly rate for", name
        input rate

        gross = hours * rate
        net = gross - DEDUCTION

        if net > 0 then
            output "Net pay for", name, "is", net
        else
            output "Deductions not covered. Net is 0."
        endif

        output "Enter next name or", EOFNAME, "to quit"
        input name
    endwhile

    output "End of job"
stop
