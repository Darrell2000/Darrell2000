// This pseudocode segment is intended to compute and display
// the cost of home ownership for any number of users
// The program ends when a user enters 0 for the mortgage payment
start
    Declarations
        num mortgagePayment
        num utilities
        num taxes
        num upkeep
        num total
   
    startUp()

    while mortgagePayment not equal to 0 do
        mainLoop()
        startUp()  // Prompt for next mortgage payment or to quit
    endwhile

    finishUp()
stop

function startUp()
    output "Enter your mortgage payment or 0 to quit"
    input mortgagePayment
    return
endfunction

function mainLoop()
    output "Enter utilities"
    input utilities
   
    output "Enter taxes"
    input taxes
   
    output "Enter amount for upkeep"
    input upkeep
   
    total = mortgagePayment + utilities + taxes + upkeep
    output "Total is", total
    return
endfunction

function finishUp()
    output "End of program"
    return
endfunction
