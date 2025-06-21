def to_celsius(value, unit):
    """
    Konversi suhu ke Celsius.

    Parameters:
    - value (float): Nilai suhu
    - unit (str): Satuan suhu ('celsius', 'fahrenheit', 'kelvin')

    Returns:
    - float: Nilai suhu dalam Celsius
    """
    unit = unit.lower()
    if unit == 'celsius':
        return value
    elif unit == 'fahrenheit':
        return (value - 32) * 5/9
    elif unit == 'kelvin':
        return value - 273.15
    else:
        raise ValueError("Satuan suhu tidak dikenali.")

def to_fahrenheit(value, unit):
    """
    Konversi suhu ke Fahrenheit.

    Parameters:
    - value (float): Nilai suhu
    - unit (str): Satuan suhu ('celsius', 'fahrenheit', 'kelvin')

    Returns:
    - float: Nilai suhu dalam Fahrenheit
    """
    celsius = to_celsius(value, unit)
    return (celsius * 9/5) + 32

def to_kelvin(value, unit):
    """
    Konversi suhu ke Kelvin.

    Parameters:
    - value (float): Nilai suhu
    - unit (str): Satuan suhu ('celsius', 'fahrenheit', 'kelvin')

    Returns:
    - float: Nilai suhu dalam Kelvin
    """
    celsius = to_celsius(value, unit)
    return celsius + 273.15

def average_temperature(values, unit='celsius'):
    """
    Menghitung rata-rata suhu dari list suhu dalam satuan tertentu.

    Parameters:
    - values (list of float): List nilai suhu
    - unit (str): Satuan hasil rata-rata ('celsius', 'fahrenheit', 'kelvin')

    Returns:
    - float: Rata-rata suhu dalam satuan yang diminta

    Raises:
    - ValueError: Jika ada elemen bukan angka
    """
    try:
        total = sum([float(v) for v in values])
        avg_celsius = total / len(values)
    # Konversi ke unit target
        if unit == 'celsius':
            return avg_celsius
        elif unit == 'fahrenheit':
            return to_fahrenheit(avg_celsius, 'celsius')
        elif unit == 'kelvin':
            return to_kelvin(avg_celsius, 'celsius')
        else:
            raise print("Satuan rata-rata tidak dikenali.")
    except:
        print("Semua nilai suhu harus berupa angka.")
    