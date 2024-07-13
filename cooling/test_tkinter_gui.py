import tkinter as tk
import modbusTCP
import modbusRTU


def change_color_tcp():
    # Проверка на вход DO
    if modbusTCP.read_DO_1():
        label_valve_1_color.config(background="green")
    else:
        label_valve_1_color.config(background="red")

    if modbusTCP.read_DO_2():
        label_valve_2_color.config(background="green")
    else:
        label_valve_2_color.config(background="red")

    if modbusTCP.read_DO_3():
        label_manometer_1_color.config(background="green")
    else:
        label_manometer_1_color.config(background="red")

    if modbusTCP.read_DO_4():
        label_manometer_2_color.config(background="green")
    else:
        label_manometer_2_color.config(background="red")

    root.after(5000, change_color_tcp)  # Вызываем функцию каждые 5 секунд


def change_color_rtu():
    if modbusRTU.run_sync_client_temp() < 27:
        label_temp_device.config(background="green", text=modbusRTU.run_sync_client_temp(), font="Arial 10 bold")
    else:
        label_temp_device.config(background="red", text=modbusRTU.run_sync_client_temp(), font="Arial 10 bold")

    if isinstance(modbusRTU.run_sync_client_flow(), int) > 10:
        label_flow.config(background="green", text=modbusRTU.run_sync_client_flow(), font="Arial 10 bold")
    else:
        label_flow.config(background="red")

    if isinstance(modbusRTU.run_sync_client_flow(), str):
        label_flow.config(background="red", text=modbusRTU.run_sync_client_flow(), font="Arial 10 bold")
    else:
        label_flow.config(background="red", text=modbusRTU.run_sync_client_flow(), font="Arial 10 bold")

    root.after(5000, change_color_rtu)


root = tk.Tk()
root.geometry("400x260")
root.title(" ")

# ---------------- Поля с названиями
label_general = tk.Label(root, text="Состояние системы охлаждения", font="Arial 14 bold")
label_general.place(x=5, y=5)

label_valve_1 = tk.Label(root, text="Клапан 1", font="Arial 9 bold")
label_valve_1.place(x=10, y=40)

label_valve_2 = tk.Label(root, text="Клапан 2", font="Arial 9 bold")
label_valve_2.place(x=10, y=75)

label_manometer_1 = tk.Label(root, text="Манометр 1", font="Arial 9 bold")
label_manometer_1.place(x=10, y=110)

label_manometer_2 = tk.Label(root, text="Манометр 2", font="Arial 9 bold")
label_manometer_2.place(x=10, y=145)

label_flow = tk.Label(root, text="Скорость потока гелия в l/min", font="Arial 9 bold")
label_flow.place(x=10, y=180)

label_temp_device = tk.Label(root, text="Температура внутриканального устройства", font="Arial 9 bold") # температура охлаждающего газа
label_temp_device.place(x=10, y=215)

# ----------------- Поля с состояниями

label_valve_1_color = tk.Label(root)
label_valve_1_color.place(x=100, y=40, width=270)

label_valve_2_color = tk.Label(root)
label_valve_2_color.place(x=100, y=75, width=270)

label_manometer_1_color = tk.Label(root)
label_manometer_1_color.place(x=100, y=110, width=270)

label_manometer_2_color = tk.Label(root)
label_manometer_2_color.place(x=100, y=145, width=270)

label_flow = tk.Label(root)
label_flow.place(x=200, y=180, width=170)

label_temp_device = tk.Label(root)
label_temp_device.place(x=270, y=215, width=100)

# -------------------------------

change_color_tcp()  # Запускаем функцию для изменения цвета
change_color_rtu()

root.mainloop()     # запуск gui
