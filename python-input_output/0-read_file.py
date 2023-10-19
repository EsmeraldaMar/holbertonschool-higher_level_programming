""" Function which reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ Reads UFT-8 File """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
