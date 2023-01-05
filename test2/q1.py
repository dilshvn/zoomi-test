arr_notes = [5000, 1000, 500, 100, 50, 20, 10] #example list
len = len(arr_notes)
amount = 28200 #example amount

arr_out = []

for note in arr_notes:
    num_notes = amount//note
    arr_out.append(num_notes)
    amount = amount%note

print(arr_out)