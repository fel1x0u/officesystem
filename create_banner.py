import pyfiglet

words = input('What sentence do you want to make into a banner? ')
banner = pyfiglet.figlet_format(words)

print("%s" % banner)
