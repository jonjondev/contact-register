from models import NULL_FIELD


class Contact:
    """
    A class defining contacts
    ...
    Attributes
    ----------
    name : str
        the name of the contact
    address : str
        the contact's address
    phone : str
        the contact's phone number

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    def __init__(self, name, address, phone):
        """
        Initialises the class with relevant parameters
        ...
        Parameters
        ----------
        name : str
            the name of the contact (default is NULL_FIELD string)
        address : str
            the contact's address (default is NULL_FIELD string)
        phone : str
            the contact's phone number (default is NULL_FIELD string)
        """
        self.name = name or NULL_FIELD
        self.address = address or NULL_FIELD
        self.phone = phone or NULL_FIELD

    def __repr__(self):
        """
        Returns a string representation of the class
        """
        return f'{self.name} | {self.address} | {self.phone}'
