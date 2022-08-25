"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(
        self,
        first_name,
        last_name,
        customer_email,
        customer_password
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.customer_email = customer_email
        self.customer_password = customer_password


    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return (
            f"<Customer: {self.first_name}, {self.last_name}, {self.customer_email}, {self.customer_password}>"
        )


def read_customer_data_from_file(filepath):
    """Read customer data and populate dictionary of customers.

    Ex:
    Jane|Melonista|jane@jane.com|secret
    {"jane@jane.com" : Customer object with attributes: first_name, etc.}

    Dictionary will be {id: Customer object}
    """

    customer_data= {}

    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                customer_email,
                customer_password
            ) = line.strip().split("|")




            customer_data[customer_email] = Customer(
                first_name,
                last_name,
                customer_email,
                customer_password
            )

    return customer_data


def get_by_email(customer_email):
    """Return a customer, given its email."""

    # This relies on access to the global dictionary `customer_data`

    #calling customer data at the key returns the customer object
    return customer_data[customer_email]




#creating a variable so we can use it outside of the function
customer_data = read_customer_data_from_file("customers.txt")