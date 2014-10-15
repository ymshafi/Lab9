############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print "Enter the temperature"
userinput = int(raw_input())
M9 = userinput * 9
D5 = M9 / 5
Final = D5 + 32
print "It is"
print Final 
print "Degrees outside" 
