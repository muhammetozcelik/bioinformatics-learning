sequence = input("DNA sequence: ").upper()
complement = ""

for base in sequence:
    if base == "A":
        complement = complement + "T"
    elif base == "T":
        complement = complement + "A"
    elif base == "G":
        complement = complement + "C"
    elif base == "C":
        complement = complement + "G"
    else:
        complement = complement + "?"

reverse_complement = complement[::-1]

print("DNA sequence:", sequence)
print("Complement:", complement)
print("Reverse complement:", reverse_complement)
