sequence_name = input("Sequence name: ")
sequence = input("DNA sequence: ").upper()

a_count = sequence.count("A")
t_count = sequence.count("T")
g_count = sequence.count("G")
c_count = sequence.count("C")

gc_count = g_count + c_count
gc_percent = gc_count / len(sequence) * 100

print("Sequence name:", sequence_name)
print("DNA sequence:", sequence)
print("Length:", len(sequence))
print("A count:", a_count)
print("T count:", t_count)
print("G count:", g_count)
print("C count:", c_count)
print(f"GC percentage: {gc_percent:.2f}%")
