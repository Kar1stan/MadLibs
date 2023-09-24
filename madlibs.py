try:
    adj = input("Adjective:")
    verb1 = input("Verb1:")
    verb2 = input("Verb2:")
    famous_person = input("Famous person:")

except EOFError as e:
    print(e)

madlib = f"Computer programming is so {adj}! I love to {verb1}.Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
