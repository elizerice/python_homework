def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence = sequence.append(next_element) 


sequence = [1, 1]
continue_fibonacci_sequence(sequence, 1)
print(*sequence)
