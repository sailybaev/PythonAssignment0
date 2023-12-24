num = int(input())

if num >= 0:
    days = num // (24 * 3600)
    rem = num % (24 * 3600)
    hours = rem // 3600
    rem %= 3600
    minutes = rem // 60
    rem %= 60

    time_format = f"{days:02d}:{hours:02d}:{minutes:02d}:{rem:02d}"
    print(f"Equivalent time: {time_format}")

else:
    print("Number is < 0")
