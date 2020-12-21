# noinspection PyUnresolvedReferences
from models import Contact
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
    ...
    Methods
    -------
    to_dict()
        returns the object as a dictionary
    to_list()
        returns the object as a list
    from_dict(contact_dict)
        returns a dictionary as a contact
    from_list(contact_list)
        returns a list as a contact
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

    @staticmethod
    def from_dict(contact_dict) -> Contact:
        """
        Returns a contact object from dictionary values

        Assumes dictionary format to be:
        {
            "name": "<contact name>",
            "address": "<contact address>",
            "phone": "<contact phone>",
        }
        ...
        Parameters
        ----------
        contact_dict : {str:str}
            a dictionary object containing contact data
        ...
        Returns
        -------
        Contact
            a newly created contact object
        """
        return Contact(contact_dict["name"], contact_dict["address"], contact_dict["phone"])

    @staticmethod
    def from_list(contact_list) -> Contact:
        """
        Returns a contact object from list values

        Assumes list format to be:
        ["<contact name>", "<contact address>", "<contact phone>"]
        ...
        Parameters
        ----------
        contact_list : [str]
            a list object containing contact data
        ...
        Returns
        -------
        Contact
            a newly created contact object
        """
        return Contact(contact_list[0], contact_list[1], contact_list[2])
