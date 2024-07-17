import struct
#from confing import siemens_ip, rack_0, slot

import snap7
from snap7.types import Areas

plc = snap7.client.Client()  # создание клиента


siemens_ip = "192.168.127.10"
rack_0 = 0
slot = 1

#todo может быть реализивать постоянный пинг сименса

def connect_siemens_test():
    """
    ip адрес, rack_0 видно в tia portal на страничке с cpu, slot указывается, в котором стоит cpu
    функция проверки соединения с siemens
    """
    try:
        plc.connect(siemens_ip, rack_0, slot)
        print("Соединение с PLC установлено.")
        print("печать из сименса")
        #Ui_MainWindow.green_label_plc()

        return 1
    except RuntimeError:
        print('Соединение с PLC не удалось. Проверьте подключение!')
        return 0


#connect_siemens_test()  # вызов функции для сохрания тип данных connect и для дальнейшей работы с ним.
                        # чтение или запись данных в siemens


def read_pbs_siemens():
    """
    data = plc.read_area(Areas.DB, 5, 0, 4)
    1 параметр область памяти - база данных
    2 параметр номер базы данных
    3 параметр адрес памяти в базе данных,
    4 параметр длина данных для float 4 байта

    В базе данных siemens нужно убрать галочку с оптимизированной памяти.

    Ответ от функции чтения приходит в таком формате "bytearray(b'?}\x97\xf7')"
    перевод в дробное число с помощью value = struct.unpack('>f', data)
    ответ приходит в типе tuple, value[0] достаем нужное нам число в обычном виде

    подробнее про struct.unpack можно почитать тут:
    https://docs-python.ru/standart-library/modul-struct-struktury-python/simvoly-formata-ispolzuemye-stroke-formata-struktury/
    https://docs-python.ru/standart-library/modul-struct-struktury-python/stroka-formata-struktury-modulja-struct/
    https://docs-python.ru/standart-library/modul-struct-struktury-python/funktsii-iskljuchenija-modulja-struct/
    """
    if plc.get_connected():
        data = plc.read_area(Areas.DB, 5, 0, 4)
        value = struct.unpack('>f', data)  # big-endian
        return print(data, value[0])
    else:
        return print("Соединение с PLC не удалось.")


def write_time_siemens():
    """
     data = plc.mb_write(100, 4, bytearray(struct.pack('>i', value)))
     запись происходит в теги в область памяти siemens MD
     1 параметр номер памяти напимер MD100
     2 параметр указывает на размер передаваемого значения. В данном случае в siemens в этой области памяти находится
     переменная типа time размером 4 байта, которая принемает целое число в значении ms
     3 параметр значение, которое необходимо записать в siemens
     bytearray(struct.pack('>i', value))) данное выражение формирует правильный формат записи вида b'?}\x00\x00'
    """
    if plc.get_connected():
        value = 3000  # милисeкунды
        data = plc.mb_write(100, 4, bytearray(struct.pack('>i', value)))  # запись
        return print(data, bytearray(struct.pack('>i', value)))
    else:
        return print("Соединение с PLC не удалось.")


def read_wll_siemens_db13():
    """
    в документации по siemens написана следующая информация по адресам для тегов, 261 страница документации на русском языке
    81 = I
    82 = Q
    83 = M
    84 = DB
    эти числа относятся в Areas для библиотеки snap7
    :return:
    """




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
    if plc.get_connected():
        data = plc.read_area(Areas.DB, 13, 0, 2)
        value = struct.unpack('b', data[1:2])  # big-endian
        return print(data[1:2], value)
    else:
        return print("Соединение с PLC не удалось.")


"""
бд под номером 14 
адрес 338 0-4
адрес 575 4-8
адрес 464 8-12
нужно как-то передать некоторые данные в овен 
"""
def write_338_do():
    # b - в списке байтов говорит о том как запакуются данные для овена, будет формат bx00x00
    if plc.get_connected():
        value = 3000  # милисeкунды
        data = plc.db_write(14, 0, bytearray(struct.pack('>b', value)))  # запись
        return print(data, bytearray(struct.pack('>b', value)))
    else:
        return print("Соединение с PLC не удалось.")

def write_464_do():
    if plc.get_connected():
        value = 3000  # милисeкунды
        data = plc.db_write(14, 8, bytearray(struct.pack('>b', value)))  # запись
        return print(data, bytearray(struct.pack('>b', value)))
    else:
        return print("Соединение с PLC не удалось.")

def write_575_do():
    if plc.get_connected():
        value = 3000  # милисeкунды
        data = plc.db_write(14, 4, bytearray(struct.pack('>b', value)))  # запись
        return print(data, bytearray(struct.pack('>b', value)))
    else:
        return print("Соединение с PLC не удалось.")

print(read_wll_siemens_db13())
#print(write_time_siemens())
#print(read_pbs_siemens())
plc.disconnect()
plc.destroy()
