# x = int(input(f"What's your x "))
# y = int(input(f"What's your y "))


# print(x + y)

# FUNCTIONS WITH RETURN VALUES

def main():  # main es convencional en python para declarar que una funcion es la principal.
    x = int(input("What's your number "))
    print("x squared is", square(x))


def square(n):
    # or return n **2
    # or return pow(n, 2)ç
    return n * n


main()
