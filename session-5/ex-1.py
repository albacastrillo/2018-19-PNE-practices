def count_a(seq):
    """Counting the number of As in the sequence"""

    # Counter for the As
    result = 0

    for b in seq:
        if b == 'A':
            result += 1

    # Return the result
    return result


# Main program
sequence = input("Please enter the sequence: ")
number_a = count_a(sequence)
print("The number of As is: {}".format(number_a))

# Calculate the total sequence
total_length = len(sequence)

# Calculate the percentage of As in the sequence
if total_length > 0:
    percentage = round(100.0 * number_a / total_length, 1)
else:
    percentage = 0

print("The total lenght is: {}".format(total_length))
print("The percentage of As is {}%".format(percentage))