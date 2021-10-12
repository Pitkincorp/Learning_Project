class Money:

    def __init__(self,dollars,cents):
        self.total_cents=100*dollars + cents

    @property
    def dollars(self):
        return self.total_cents//100

    @dollars.setter
    def dollars(self,dollars):
        if not isinstance(dollars,int) or dollars<0:
            print('Error dollars')
        else: self.total_cents=self.total_cents%100 + 100*dollars

    @property
    def cents(self):
        return self.total_cents%100

    @cents.setter
    def cents(self,cents):
        if not isinstance(cents,int) or cents>=100 or cents<0:
            print('Error cents')
        else: self.total_cents = self.total_cents//100*100 + cents

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"