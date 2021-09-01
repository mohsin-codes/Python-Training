# AND, OR, NOT

good_grades = False
athletic = False

# AND Operator
if good_grades and athletic:
    print('''
        Admission can ve availed in any domains :
        1. Tech
        2. Architect
        3. Commerce
        4. Arts
        5. Sports
    ''')
# OR Operator
elif good_grades or athletic:
    print('''
        Admissions can only be availed in any domains :
        1. Sports
        2. Arts
        3. Architecture
    ''')
else:
    print("Admission cannot be availed!")


# NOT Operator
print(not True)
print(not False)