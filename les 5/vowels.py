s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinker = 'iouae'
for char in s:
    if char in klinker:
        print(char)