class Mobile:
    dijoi = 54
    dnhijd = 54684
    daf = 44
    sfd = 454
    edcv = 7845
    sdfwr = 427

    def __init__(self, model, company, price):
        self.model = model
        self.company = company
        self.price = 0

    def __str__(self):
        return f'Mobile [{self.model},{self.company},{self.price}]'


m = Mobile('m', 45, 48)
print(m)

print(m.__sizeof__())
n = 8454546
print(n.__sizeof__())
n = 48
print(n.__sizeof__())
n = 87465231854218965741895421986541
print(n.__sizeof__())


class Mobile1:
    pass


m1 = Mobile1()
print(m1.__sizeof__())

m.