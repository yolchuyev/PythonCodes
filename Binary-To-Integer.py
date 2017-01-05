print("Enter Binary to convert to integer!")
bin = input()
binlist = list(bin)
bin_to_int = 0
rbinlist = list(reversed(binlist))
for i in range(len(rbinlist)):
    bin_to_int+=int(rbinlist[i])*2**i
print(bin_to_int)

