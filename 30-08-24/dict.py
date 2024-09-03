import colorama

brazillian_culture = {
    "lang": "Portuguese",
    "food": ["Feijoada", "Maniçoba", "Buchada de Bode"],
    "branches": ["Executive", "Legislative", "Judiciary"]
}

foodFormated = ', '.join(brazillian_culture['food'])
branchesFormated = ', '.join(brazillian_culture['branches'])

print(f"{brazillian_culture['lang']} is the language spoken in Brazil.")
print(f"People in Brazil often eat {foodFormated}.")
print(f"The goverment is ruled by the {branchesFormated}.\n")

age = int(input("How old are you?: "))

print(f"You're {age} years old!")