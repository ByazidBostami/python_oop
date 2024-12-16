def passwordChecker(passw):
    is_lower = any(i.islower() for i in passw)
    is_upper = any(i.isupper() for i in passw)
    is_digit = any(i.isdigit() for i in passw)
    is_special = any(i in "_$#@!" for i in passw)

    missing_condition = []
    if not is_lower:
        missing_condition.append("Lower case missing")
    if not is_upper:
        missing_condition.append("Upper case missing")
    if not is_digit:
        missing_condition.append("Digit missing")
    if not is_special:
        missing_condition.append("Special character missing")

    if not missing_condition:
        return "Ok"
    else:
        return ",".join(missing_condition)
    
user = input("Please input a password for check: ")

print(passwordChecker(user))

   

