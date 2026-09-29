class User:
    def __init__(self, ism, telefon, balans=0):
        self.ism = ism
        self._telefon = telefon
        self.__balans = balans

    @property
    def balans(self):
        return self.__balans

    @balans.setter
    def balans(self, yangi_balans):
        if yangi_balans >= 0:
            self.__balans = yangi_balans
        else:
            print("Balans manfiy bo'lishi mumkin emas!!")

    def __str__(self):
        return f"{self.ism} | Balance: {self.balans} so'm"

    def __repr__(self):
        return f"User(name={self.ism!r}, phone={self._telefon!r})"


class Client(User):
    def __init__(self, ism, telefon, karta_raqami, balans=0):
        super().__init__(ism, telefon, balans)
        self.karta_raqami = karta_raqami

    def deposit(self, summa):
        if summa > 0:
            self.balans = self.balans + summa
            print(f"{summa} so'm qo'shildi")
        else:
            print("Summa 0 dan katta bo'lishi kerak")

    def withdraw(self, summa):
        if summa <= 0:
            print("Summa 0 dan katta bo'lishi kerak")
        elif summa > self.balans:
            print("Balansda mablag' yetarli emas")
        else:
            self.balans = self.balans - summa
            print(f"{summa} so'm yechildi")

    def info(self):
        print(f"Mijoz: {self.ism}, tel: {self._telefon}, karta: {self.karta_raqami}, balans: {self.balans} so'm")


class Employee(User):
    def __init__(self, ism, telefon, xodim_id, maosh, balans=0):
        super().__init__(ism, telefon, balans)
        self.xodim_id = xodim_id
        self.maosh = maosh

    def work(self):
        print(f"{self.ism} bank xodimi sifatida ishlayapti.")

    def info(self):
        print(f"Xodim: {self.ism}, tel: {self._telefon}, ID: {self.xodim_id}, maosh: {self.maosh} so'm")


class Bank:
    def __init__(self):
        self.clients = []
        self.employees = []

    def add_client(self, client):
        self.clients.append(client)

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_clients(self):
        for client in self.clients:
            print(client)

    def show_employees(self):
        for employee in self.employees:
            print(employee)

    def find_client(self, qidiruv):
        for client in self.clients:
            if client._telefon == qidiruv or client.karta_raqami == qidiruv:
                return client
        return None


bank = Bank()

klient_1 = Client("Ali", "901111111", "8600 1111 2222 3333", 1000000)
klient_2 = Client("Vali", "902222222", "8600 4444 5555 6666", 500000)
klient_3 = Client("Hasan", "905555555", "8600 7777 8888 9999", 750000)

xodim_1 = Employee("Sobir", "903333333", 101, 5000000)
xodim_2 = Employee("Kama", "904444444", 102, 6000000)

bank.add_client(klient_1)
bank.add_client(klient_2)
bank.add_client(klient_3)
bank.add_employee(xodim_1)
bank.add_employee(xodim_2)

klient_1.deposit(200000)
klient_2.withdraw(100000)

print(klient_1.balans)
print(klient_2.balans)

bank.show_clients()
bank.show_employees()

xodim_1.work()

for foydalanuvchi in bank.clients + bank.employees:
    foydalanuvchi.info()

print(str(klient_1))
print(repr(klient_1))
print(str(xodim_1))
print(repr(xodim_1))

print(klient_1.ism)
print(klient_1._telefon)

try:
    print(klient_1.__balans)
except AttributeError:
    print("Xato: __balans private, tashqaridan murojaat qilib bo'lmaydi")

print(bank.find_client("902222222"))
print(bank.find_client("000"))