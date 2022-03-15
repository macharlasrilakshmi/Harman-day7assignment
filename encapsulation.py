class Government:
    def __init__(self):
        self.__price=100

    def viewPetrolprice(self):
        print(self.__price)

    def hikeprice(self,price):
        self.__price=price

centralGovt=Government()
centralGovt.viewPetrolprice()

centralGovt.__price=130
centralGovt.viewPetrolprice()

centralGovt.hikeprice(120)
centralGovt.viewPetrolprice()
