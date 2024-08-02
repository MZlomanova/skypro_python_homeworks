from adress import Address
from Mailing import Mailing

to_address = Address("100000", "Москва", "ул. Пупкина", "37", "111")
from_address = Address("123000", "Москва", "ул. Пржевальского", "12", "67")
mailing = Mailing(from_address, to_address, 12.66, 3456)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street},{mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость{mailing.cost} рублей.")