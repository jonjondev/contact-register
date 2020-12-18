

NULL_FIELD = "-"


class Contact:

    def __init__(self, name, address, phone):
        self.name = name or NULL_FIELD
        self.address = address or NULL_FIELD
        self.phone = phone or NULL_FIELD

    def __repr__(self):
        return f'{self.name}: {self.address}, {self.phone}'
