from smartphone import Smartphone
catalog = []
phone1 = Smartphone("Nokia", "3310", "+79012345678")
phone2 = Smartphone("Apple", "iPhone 15 pro max", "+77771112222")
phone3 = Smartphone("Xiaomi", "13 Ultra", "+78881114521")
phone4 = Smartphone("Google Pixel", "Pixel 9", "+79013332244")
phone5 = Smartphone("Asus", "Zenfone 11", "+78085012234")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phoneNumber}")