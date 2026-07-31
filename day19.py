
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"
    
print(check_age(20))
print(check_age(15))

# mini challenge

def pass_or_fail(score):
    if score >= 50:
        return "Pass"
    else:
        if score < 50:
            return "Fail"
        
print(pass_or_fail(75))
print(pass_or_fail(40))
