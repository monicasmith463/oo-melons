"""Classes for melon orders."""


class AbstactOrder(object):
    """Creates abstract melon order with species and quantity attributes."""


    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True





class DomesticMelonOrder(AbstactOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty)
    


class InternationalMelonOrder(AbstactOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Total for int'l orders including flat shipping fee."""

        result = super(InternationalMelonOrder,self).get_total()

        if self.qty < 10:
            result += 3

        return result


class GovernmentMelonOrder(AbstactOrder):
    """A melon order from the Government OMG."""

    order_type = "government"
    tax = 0.00
    passed_inspection = False

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(GovernmentMelonOrder, self).__init__(species, qty)


    def mark_inspection(self, is_passed):
        passed_inspection = is_passed
