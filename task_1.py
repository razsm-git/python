from sys import argv

script_name, cash_per_hour, hours, premium = argv

payment = (int(cash_per_hour) * int(hours)) + (int(cash_per_hour) * int(hours)) * (int(premium) / 100)
print(
    f"За час работник получает: {cash_per_hour} рублей, отработал {hours} часов, премию получит в размере {100}%, "
    f"итоговый доход составит {payment:.2f} рублей.")
