import time

from config.config import MOXA_1, MOXA_2
from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ConnectionException
import logging

logger = logging.getLogger(__name__)

client_MOXA_1 = ModbusTcpClient(MOXA_1)
client_MOXA_2 = ModbusTcpClient(MOXA_2)


def read_moxa_1_do_1():
    """
    Читаем coils на MOXA_1, пароль от веб версии "moxa".
    def read_coils(self,
       address: int,
       count: int = 1)

    Params:
    address – Start address to read from
    count – (optional) Number of coils to read
    """
    try:
        result = client_MOXA_1.read_coils(0, 1)
    except ConnectionException:
        error = "Ошибка подключения к MOXA 1214, проверьте соединение"
        return error
    else:
        return result.bits[0]
    finally:
        client_MOXA_1.close()


def read_moxa_1_do_2():
    try:
        result = client_MOXA_1.read_coils(1, 1)
    except ConnectionException as err:
        logger.warning(f"error in read_moxa_1_do_2 == {err}")
        error = "Ошибка подключения к MOXA 1214, проверьте соединение"
        return error
    else:
        return result.bits[0]
    finally:
        client_MOXA_1.close()


def read_moxa_1_do_3():
    try:
        result = client_MOXA_1.read_coils(2, 1)
    except ConnectionException as err:
        logger.warning(f'error in read_moxa_1_do_3 == {err}')
        error = "Ошибка подключения к MOXA 1214, проверьте соединение"
        return error
    else:
        return result.bits[0]
    finally:
        client_MOXA_1.close()


def read_moxa_1_do_4():
    try:
        result = client_MOXA_1.read_coils(3, 1)
    except ConnectionException as err:
        logger.warning(f'error in read_moxa_1_do_4 == {err}')
        error = "Ошибка подключения к MOXA 1214, проверьте соединение"
        return error
    else:
        return result.bits[0]
    finally:
        client_MOXA_1.close()


# два входа и два выхода 0 и 1 и там и там


def read_input_register_moxa_2():
    """
    Читаем RTD Multiplied Engineering Value с адресом 1536. Данный input registr выдает значеие нашего еденственного
    датчика температуры. Температура измеряется в десятичных числах. Читается в целых. Точность измерение не нужна.
    Можно оставить допуски +- 10 градусов. Решил разделить на 10 и вывести привычное число
    """
    try:
        result = client_MOXA_2.read_input_registers(address=1536)
        time.sleep(1)
    except Exception as err:
        logger.warning(f'error in read_moxa_1_do_3 == {err}')
        error = "Ошибка подключения к MOXA 1260, проверьте соединение"
        return error
    else:
        return result.registers[0] // 10
    finally:
        client_MOXA_2.close()



# while True:
#     print(read_input_register_moxa_2())