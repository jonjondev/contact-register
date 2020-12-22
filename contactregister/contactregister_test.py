from contextlib import redirect_stdout
from models.Contact import Contact
from display import html
import contactregister
import unittest
import helpers
import json
import glob
import csv
import os
import io


class ContactRegisterTestCase(unittest.TestCase):

    def tearDown(self):
        files = glob.glob('../data/*')
        for f in files:
            os.remove(f)
        contactregister.contacts = []


class AddContact(ContactRegisterTestCase):

    def test_add_single(self):
        contactregister.add_contact("Jon Jon", "123 Hello Rd", "+614090000")
        self.assertEqual(1, len(contactregister.contacts))

    def test_add_multi(self):
        contactregister.add_contact("Ron Ron", "125 Welcome Plc", "+614090002")
        contactregister.add_contact("Bon Bon", "124 Goodbye St", "+614090001")
        self.assertEqual(2, len(contactregister.contacts))


class ListContacts(ContactRegisterTestCase):

    def test_list_empty(self):
        self.assertEqual(0, len(contactregister.get_all_contacts()))

    def test_list_single(self):
        contactregister.contacts.append(Contact("Jon Jon", "123 Hello Rd", "+614090000"))
        self.assertEqual(1, len(contactregister.get_all_contacts()))

    def test_list_multi(self):
        contactregister.contacts.append(Contact("Ron Ron", "125 Welcome Plc", "+614090002"))
        contactregister.contacts.append(Contact("Bon Bon", "124 Goodbye St", "+614090001"))
        self.assertEqual(2, len(contactregister.get_all_contacts()))


class SearchContacts(ContactRegisterTestCase):

    def test_search_empty(self):
        self.assertEqual(0, len(contactregister.search_contacts("name=Jon*")))

    def test_search_one(self):
        jon_jon = Contact("Jon Jon", "123 Hello Rd", "+614090000")
        contactregister.contacts.append(jon_jon)
        matches = contactregister.search_contacts("name=Jon*")
        self.assertEqual(1, len(matches))
        self.assertEqual([jon_jon], matches)
        self.assertEqual(0, len(contactregister.search_contacts("name=Bon*")))
        self.assertEqual(1, len(contactregister.search_contacts("address=12? Hello*")))
        self.assertEqual(1, len(contactregister.search_contacts("name=Jon*, address=12? Hello*")))
        self.assertEqual(1, len(contactregister.search_contacts("phone=+6*")))
        self.assertEqual(0, len(contactregister.search_contacts("phone=+6*, address = 124*")))

    def test_search_multi(self):
        jon_jon = Contact("Jon Jon", "123 Hello Rd", "+614090000")
        ron_ron = Contact("Ron Ron", "125 Welcome Plc", "+614090002")
        jon_bon = Contact("Jon Bon", "124 Goodbye St", "+614090001")
        contactregister.contacts.extend([jon_jon, ron_ron, jon_bon])
        matches = contactregister.search_contacts("address=12*")
        self.assertEqual(3, len(matches))
        self.assertEqual([jon_jon, ron_ron, jon_bon], matches)
        self.assertEqual(3, len(contactregister.search_contacts("name=*on*")))
        self.assertEqual(2, len(contactregister.search_contacts("name=Jon*")))
        self.assertEqual(1, len(contactregister.search_contacts("name=Jon*, phone = *01")))
        self.assertEqual(2, len(contactregister.search_contacts("address = *el*")))


class DisplayContacts(ContactRegisterTestCase):

    @staticmethod
    def get_text_display_output():
        f = io.StringIO()
        with redirect_stdout(f):
            contactregister.display_contacts("text")
        return f.getvalue()

    @staticmethod
    def get_html_format(elements=""):
        return '<html>\n\t<head>\n\t\t<title>Data Value</title>\n\t</head>\n\t<body>\n' \
               f'\t\t<h1>All Contacts</h1>\n\t\t<ul>\n{elements}\n\t\t</ul>\n\t</body>\n</html>'

    @staticmethod
    def get_html_file_output():
        with open("../data/contacts.html", 'r', newline='') as file:
            return file.read()

    def test_display_text_empty(self):
        output = DisplayContacts.get_text_display_output()
        self.assertEqual("name    address    phone\n"
                         "------  ---------  -------\n", output)

    def test_display_text_single(self):
        contactregister.contacts.append(Contact("Jon Jon", "123 Hello Rd", "+614090000"))
        output = DisplayContacts.get_text_display_output()
        self.assertEqual("name     address            phone\n"
                         "-------  ------------  ----------\n"
                         "Jon Jon  123 Hello Rd  +614090000\n", output)

    def test_display_text_multi(self):
        contactregister.contacts.append(Contact("Ron Ron", "125 Welcome Plc", "+614090002"))
        contactregister.contacts.append(Contact("Bon Bon", "124 Goodbye St", "+614090001"))
        output = DisplayContacts.get_text_display_output()
        self.assertEqual("name     address               phone\n"
                         "-------  ---------------  ----------\n"
                         "Ron Ron  125 Welcome Plc  +614090002\n"
                         "Bon Bon  124 Goodbye St   +614090001\n", output)

    def test_display_html_empty(self):
        contactregister.display_contacts("html")
        self.assertEqual(DisplayContacts.get_html_format(), DisplayContacts.get_html_file_output())

    def test_display_html_single(self):
        jon_jon = Contact("Jon Jon", "123 Hello Rd", "+614090000")
        contactregister.contacts.append(jon_jon)
        contactregister.display_contacts("html")
        self.assertEqual(DisplayContacts.get_html_format(html.contacts_to_list_items([jon_jon])),
                         DisplayContacts.get_html_file_output())

    def test_display_html_multi(self):
        jon_jon = Contact("Jon Jon", "123 Hello Rd", "+614090000")
        ron_ron = Contact("Ron Ron", "125 Welcome Plc", "+614090002")
        contactregister.contacts.extend([jon_jon, ron_ron])
        contactregister.display_contacts("html")
        self.assertEqual(DisplayContacts.get_html_format(html.contacts_to_list_items([jon_jon, ron_ron])),
                         DisplayContacts.get_html_file_output())


class ExportContacts(ContactRegisterTestCase):

    @staticmethod
    def get_json_file_output():
        with open("../data/contacts.json", 'r', newline='') as file:
            return json.load(file)

    @staticmethod
    def get_csv_file_output():
        with open("../data/contacts.csv", 'r', newline='') as file:
            return file.read()

    def test_export_json_empty(self):
        contactregister.export_contacts("json")
        self.assertEqual([], ExportContacts.get_json_file_output())

    def test_export_json_single(self):
        jon_jon = Contact("Jon Jon", "123 Hello Rd", "+614090000")
        contactregister.contacts.append(jon_jon)
        contactregister.export_contacts("json")
        self.assertEqual([jon_jon.to_dict()], ExportContacts.get_json_file_output())

    def test_export_json_multi(self):
        jon_jon = Contact("Jon Jon", "123 Hello Rd", "+614090000")
        ron_ron = Contact("Ron Ron", "125 Welcome Plc", "+614090002")
        contactregister.contacts.extend([jon_jon, ron_ron])
        contactregister.export_contacts("json")
        self.assertEqual([jon_jon.to_dict(), ron_ron.to_dict()], ExportContacts.get_json_file_output())

    def test_export_csv_empty(self):
        contactregister.export_contacts("csv")
        self.assertEqual('"name","address","phone"\r\n', ExportContacts.get_csv_file_output())

    def test_export_csv_single(self):
        jon_jon = Contact("Jon Jon", "123 Hello Rd", "+614090000")
        contactregister.contacts.append(jon_jon)
        contactregister.export_contacts("csv")
        self.assertEqual('"name","address","phone"\r\n'
                         '"Jon Jon","123 Hello Rd","+614090000"\r\n', ExportContacts.get_csv_file_output())

    def test_export_csv_multi(self):
        jon_jon = Contact("Jon Jon", "124 Hello Rd", "+614090000")
        ron_ron = Contact("Ron Ron", "125 Welcome Plc", "+614090002")
        contactregister.contacts.extend([jon_jon, ron_ron])
        contactregister.export_contacts("csv")
        self.assertEqual('"name","address","phone"\r\n'
                         '"Jon Jon","124 Hello Rd","+614090000"\r\n'
                         '"Ron Ron","125 Welcome Plc","+614090002"\r\n', ExportContacts.get_csv_file_output())


class ImportContacts(ContactRegisterTestCase):

    @staticmethod
    def create_json_file_with(contacts):
        helpers.try_create_dir("../data/")
        with open("../data/contacts.json", 'w', newline='') as file:
            json.dump([contact.to_dict() for contact in contacts], file, indent=4)

    @staticmethod
    def create_csv_file_with(contacts):
        helpers.try_create_dir("../data/")
        with open("../data/contacts.csv", 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(Contact.supported_search_fields)
            [writer.writerow(contact.to_list()) for contact in contacts]

    def test_import_json_empty(self):
        ImportContacts.create_json_file_with([])
        contactregister.import_contacts("json")
        self.assertEqual(0, len(contactregister.contacts))

    def test_import_json_single(self):
        jon_jon = Contact("Jon Jon", "123 Hello Rd", "+614090000")
        ImportContacts.create_json_file_with([jon_jon])
        contactregister.import_contacts("json")
        self.assertEqual(1, len(contactregister.contacts))

    def test_import_json_multi(self):
        jon_jon = Contact("Jon Jon", "124 Hello Rd", "+614090000")
        ron_ron = Contact("Ron Ron", "125 Welcome Plc", "+614090002")
        ImportContacts.create_json_file_with([jon_jon, ron_ron])
        contactregister.import_contacts("json")
        self.assertEqual(2, len(contactregister.contacts))

    def test_import_csv_empty(self):
        ImportContacts.create_csv_file_with([])
        contactregister.import_contacts("csv")
        self.assertEqual(0, len(contactregister.contacts))

    def test_import_csv_single(self):
        jon_jon = Contact("Jon Jon", "123 Hello Rd", "+614090000")
        ImportContacts.create_csv_file_with([jon_jon])
        contactregister.import_contacts("csv")
        self.assertEqual(1, len(contactregister.contacts))

    def test_import_csv_multi(self):
        jon_jon = Contact("Jon Jon", "124 Hello Rd", "+614090000")
        ron_ron = Contact("Ron Ron", "125 Welcome Plc", "+614090002")
        ImportContacts.create_csv_file_with([jon_jon, ron_ron])
        contactregister.import_contacts("csv")
        self.assertEqual(2, len(contactregister.contacts))


if __name__ == '__main__':
    unittest.main()
