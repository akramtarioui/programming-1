age = eval(input("Voer uw leeftijd in: "))
passport = input("Bent u in het bezit van een nederlands paspoort?:")

if age > 17 and passport == "ja":
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Helaas je mag niet stemmen")
print("Bedankt.")