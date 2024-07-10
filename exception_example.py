
number = None

while True:
    try:
        number = int(input('>>> '))
    except ValueError as err:
        print(f"ERROR: {err}")
        print("You should enter only digits")
    if type(number) == int:
        break

print(f"{number=}")
