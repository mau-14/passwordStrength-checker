import string

password = "helloworld"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password]) 
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password]) 
special = any([1 if c in string.punctuation else 0 for c in password]) 
upper_case = any([1 if c in string.digits else 0 for c in password]) 


print(string.digits)

