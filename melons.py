"""Classes for melon orders."""


class AbstactOrder(object):

    #def init

    #get total

    #mark shipped


    def __init__(self, species, qty):
            """Initialize melon order attributes."""

            self.species = species
            self.qty = qty
            self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True





class DomesticMelonOrder(AbstactOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

    

class InternationalMelonOrder(AbstactOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
