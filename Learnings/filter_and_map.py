#filter(function,sequence) filter out element from the sequence for which function is true.


seq = [1, 2, 3, 4]

# take keep od numbers from seq

odd = lambda x: True if x % 2 == 1 else False

filtered_output = filter(odd, seq) # filters true condition from sequence.

mapped_output = map(odd, seq) # tracks record of true and false or sequence.
print(list(filtered_output))
print(list(mapped_output))
