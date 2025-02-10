#function which returns reversed string
def reversed(string):
        string_rev=string[::-1]
        return string_rev

#string input from the user
string= input("Enter a string: ")

#calling string revrse function and assigning value to String2
string2=reversed(string)

#printing reversed string
print("Reverse of string:",string2)


