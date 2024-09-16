// This pseudocode is intended to determine whether students have
// passed or failed a course; students need to average 60 or
// more on two tests.
start
    Declarations
        num firstTest
        num secondTest
        num average
        num PASSING = 60

    output "Enter first score or 0 to quit"
    input firstTest

    while firstTest not equal to 0 do
        output "Enter second score"
        input secondTest

        average = (firstTest + secondTest) / 2
        output "Average is", average

        if average >= PASSING then
            output "Pass"
        else
            output "Fail"
        endif

        output "Enter first score or 0 to quit"
        input firstTest
    endwhile

    output "End of program"
stop
