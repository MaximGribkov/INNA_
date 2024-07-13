import time

from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException
from pymodbus.pdu import ExceptionResponse

from config.config import (
    TIMEOUT,
    BAUDRATE,
    BYTESIZE,
    PARITY,
    STOPBITS,
    PORT
)


def run_sync_client_temp():
    """Run sync client."""

    # Получение клиента modbusRTU
    client = ModbusSerialClient(
        port=PORT,
        timeout=TIMEOUT,
        baudrate=BAUDRATE,
        bytesize=BYTESIZE,
        parity=PARITY,
        stopbits=STOPBITS,
    )

    # Подключение с задержкой
    client.connect()
    time.sleep(0.02)

    try:
        # Чтение 2 регистров с темературой
        rr = client.read_input_registers(address=0x01F4, count=0x02, slave=0x05)
        time.sleep(0.03)
        # Вывод связян с особенности ответа от устройства чесел с плавающей точкой, нужно смотреть AN0103 раздел 7,2
        # Для мониторинга достаточно целого числа температуры
        # -2 градуса делается поправка, чтобы приблизится к показателям из программы EE-PCS,
        # показатели по modbus отличаюся на +2 градуса
        value_modbus = str(hex(rr.registers[1]))
        exponent = int((value_modbus[3] + value_modbus[4]), 16) - 2

    except ModbusException as exc:
        print(f"Received ModbusException({exc}) from library")
        client.close()
        return
    if rr.isError():
        print(f"Received Modbus library error({rr})")
        client.close()
        return
    if isinstance(rr, ExceptionResponse):
        print(f"Received Modbus library exception ({rr})")
        # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
        client.close()

    client.close()
    return exponent


def run_sync_client_flow():
    """Run sync client."""

    # Получение клиента modbusRTU
    client = ModbusSerialClient(
        port=PORT,
        timeout=TIMEOUT,
        baudrate=BAUDRATE,
        bytesize=BYTESIZE,
        parity=PARITY,
        stopbits=STOPBITS,
    )

    # Подключение с задержкой
    client.connect()
    time.sleep(0.02)

    try:
        # Чтение 2 регистров с Standard volume flow
        rr = client.read_input_registers(address=0x0208, count=0x02, slave=0x05)
        time.sleep(0.03)
        # Вывод связан с особенности ответа от устройства чисел с плавающей точкой, нужно смотреть AN0103 раздел 7,2
        # Для мониторинга достаточно целого числа
        try:  # Если нет потока, то возвращается 0х0 и выходим за размер строки
            value_modbus = str(hex(rr.registers[1]))
            exponent = int((value_modbus[3] + value_modbus[4]), 16)
        except IndexError:
            client.close()
            return "Нет потока гелия."

    except ModbusException as exc:
        print(f"Received ModbusException({exc}) from library")
        client.close()
        return
    if rr.isError():
        print(f"Received Modbus library error({rr})")
        client.close()
        return
    if isinstance(rr, ExceptionResponse):
        print(f"Received Modbus library exception ({rr})")
        # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
        client.close()

    client.close()
    return exponent


# print(run_sync_client_flow(), run_sync_client_temp())
