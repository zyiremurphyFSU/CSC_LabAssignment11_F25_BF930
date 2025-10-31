def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.
    @param celsius (float): Temperature in Celsius.
    @return (float) equivalent temperature in F
    """
    return 9 / 5 * celsius + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius.
    @param fahrenheit (float): Temperature in Fahrenheit.
    @return float: Equivalent temperature in Celsius.
    """
    return 5 / 9 * (fahrenheit - 32)


def main():
    c = 36.5
    f_from_c = celsius_to_fahrenheit(c)
    print(f"{c} C is equal to {f_from_c} F")

    f = 101.3
    c_from_f = fahrenheit_to_celsius(f)
    print(f"{f} F is equal to {c_from_f} C")


if __name__ == "__main__":
    main()
