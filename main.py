import string
import getpass

password = getpass.getpass("Introduce tu contraseña:")

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password]) 
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password]) 
special = any([1 if c in string.punctuation else 0 for c in password]) 
digits = any([1 if c in string.digits else 0 for c in password]) 
characters = [upper_case,lower_case,special,digits]
length = len(password)

score = 0

with open('common.txt', 'r') as f:
    # Normalizamos las contraseñas a minúsculas al cargarlas
    common = [line.lower() for line in f.read().splitlines()]

# Comparamos la contraseña en minúsculas con las contraseñas comunes
if password.lower() in common:
    print("Tu contraseña es común. Score: 0/10")
    exit()

if length > 8:
    score += 1

if length > 12:
    score += 1

if length > 17:
    score += 1

print(f"La longitud de la contraseña es {str(length)}")

if sum(characters) > 1:
    score += 1

if sum(characters) > 2:
    score += 1

if sum(characters) > 3:
    score += 3

print(f"La contraseña tienen {str(sum(characters))} tipos diferente de caracteres")

if score < 5:
    print(f"La contraseña es muy débil. Score: {str(score)}/10")
elif score == 5:
    print(f"La contraseña esta ok! Score: {str(score)}/10")
elif score > 5 and score < 8:
    print(f"La contraseña esta muy bien! Score: {str(score)}/10")
elif score == 10:
    print(f"La contraseña es muy fuerte! Score: {str(score)}/10")
