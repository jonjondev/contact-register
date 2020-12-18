from models.Contact import Contact


def print_hi(name):
    contact = Contact(name, "158 Military Road", "93719000")
    print(contact)


if __name__ == '__main__':
    print_hi('PyCharm')
