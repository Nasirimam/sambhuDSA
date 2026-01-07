# Test the Rank of a student

# int marks = 72;

# Output: "Distinction" (>=75), "First Class"
# (>=60), "Second Class" (>=50), “Pass“
# (>=35), or “Fail”

a = 72

res = (
    "Distinction"
    if (a >= 75)
    else (
        "First Class"
        if (a >= 60)
        else "Second Class" if (a >= 50) else "Pass" if (a >= 35) else "Fail"
    )
)
print(res)
