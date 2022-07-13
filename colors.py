from colorama import init
init()


# text colors
tred = "\033[1;31;48m"
tred2 = "\033[0;31;48m"
tgreen = "\033[1;32;48m"
tgreen2 = "\033[0;32;48m"
tyellow = "\033[1;33;48m"
tmagenta = "\033[1;35;48m"
tblue = "\033[1;34;48m"
tcyan = "\033[1;36;48m"

# background colors
bgrey = "\033[1;37;47m"
bgreen = "\033[1;37;42m"
bcyan = "\033[1;37;46m"
bred = "\033[1;37;41m"

# reset default color
endc = "\033[m"


def input_colorama(color, message):
    print(color + message + endc + "\n", end="")
    input()


if __name__ == "__main__":
    print(tred + "Ciao")
    input_colorama(tcyan, "PRESS ENTER")
    input("back to normal")
