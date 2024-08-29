import sys

print('Hello world!')


def main():
    a = input("Enter: ")

    if a == "1":
        sys.exit()

    else:
        print("Nice!")

main()


def answer():
    ans = input("Do you want?: ")

    print(ans)


answer()