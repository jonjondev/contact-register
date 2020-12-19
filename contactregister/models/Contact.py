from models import NULL_FIELD


class Contact:
    """
    A class defining contacts
    ...
    Attributes
    ----------
    supported_search_fields : [str]
        a list of fields that support searching
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

    supported_search_fields = ["name", "address", "phone"]

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
        ...
        Returns
        -------
        Contact
            a new Contact object
        """
        self.name = name or NULL_FIELD
        self.address = address or NULL_FIELD
        self.phone = phone or NULL_FIELD

    def __repr__(self):
        """
        Returns a string representation of the class
        ...
        Returns
        -------
        str
            the string representation of a the object
        """
        return f'{self.name} | {self.address} | {self.phone}'

    def to_dict(self) -> {str: str}:
        """
        Returns a dictionary representation of the class
        ...
        Returns
        -------
        {str: str}
            a dictionary of object fields and values
        """
        return {"name": self.name, "address": self.address, "phone": self.phone}

    def to_list(self) -> [str]:
        """
        Returns a list representation of the class
        ...
        Returns
        -------
        [str]
            a list of object field values
        """
        return [self.name, self.address, self.phone]
