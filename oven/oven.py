import struct
import time

from pymodbus.client import ModbusTcpClient

# todo разобраться что за тип данных выдает овен при чтении с него
# todo отправить запрос через термит, если не получится адекватный ответ, то проще будет читать данные с сименса
def unpackInt16(data):  # извлекает из данных целое число со знаком
    dataSize = len(data)
    if dataSize < 1:
        print("<1")
    elif dataSize == 1:
        data = b'\x00' + data  # дополняем до двух байтов
    # value = ord(self.data[1]) + (ord(self.data[0])<<8 & 0xffff)
    # value = struct.unpack('>h', data[0:2])[0]
    # result = dict(value = value, time = -1, index = -1)
    return struct.unpack('>H', data)


# Параметры подключения
device_address = '192.168.127.70'
device_port = 502
unit_id = 1  # адрес устройства owen

# Установка соединения
client = ModbusTcpClient(host=device_address)
#print(client.connect())


'''
    данная заметка подходит для овена 464
    как работает чтение из овена. какие данные он передают в питон. читиается с него массив размером 1 байт
    в этом массиве лежит целое число. это целое число необходимо перевести в двоичную систему. далее нужно сверять биты со значением датчиков
    01 01 01 01 равно максимальному числу 85. первый ноль ничего не значит. второй означает выключенное состояние датчика
    первая пара это wll середина
    вторая пара это индукционный датчик
    третья пара это wll правый 
    четвертая пара тумблер
'''
# интересный формат выдаваемых значений с овена. пока не понятно с чего читать удобнее и быстрее
#
# Чтение регистра 51 обязательно нужно указать номер слейва иначе не читает
#result = client.read_holding_registers(address=0x0033, slave=1)

result = client.read_holding_registers(51, slave=1)
a = result.registers
print(type(a[0]))


print(result.registers) # todo попробовать с битами и дургими типами данных, может быть что-то получится


#print(result)
print(unpackInt16(a[0]))

# Закрытие соединения

# Вывод полученного значения
# if result.isError():
#     print("Ошибка при чтении регистра:", result)
# else:
#     print("Значение регистра 51:", result.registers)

