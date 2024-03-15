score = 39
rating = ""

if score > 80:
    rating = "Passed with Distinction"
elif score <= 50:
    rating = "Fair"
elif score <= 70:
    rating = "Passed with Credit"
else:
    rating = "Failed"

print(rating)
