class gemeter:
    """
    Kelas untuk melakukan konversi suhu dan operasi suhu lainnya.
    """

    def __init__(self, value, unit):
        """
        Inisialisasi nilai suhu dan satuannya.

        Parameters:
        - value (float): Nilai suhu
        - unit (str): Satuan suhu ('celsius', 'fahrenheit', 'kelvin')
        """
        try:
            self.value = float(value)
        except ValueError:
            raise ValueError("Nilai suhu harus berupa angka.")

        self.unit = unit.lower()
        if self.unit not in ['celsius', 'fahrenheit', 'kelvin']:
            raise ValueError("Satuan suhu tidak dikenali.")

    def to_celsius(self):
        if self.unit == 'celsius':
            return self.value
        elif self.unit == 'fahrenheit':
            return (self.value - 32) * 5/9
        elif self.unit == 'kelvin':
            return self.value - 273.15

    def to_fahrenheit(self):
        celsius = self.to_celsius()
        return (celsius * 9/5) + 32

    def to_kelvin(self):
        celsius = self.to_celsius()
        return celsius + 273.15

    @staticmethod
    def average_temperature(values, unit='celsius'):
        """
        Menghitung rata-rata suhu dari list suhu dalam satuan tertentu.

        Parameters:
        - values (float): List nilai suhu
        - unit (str): Satuan hasil rata-rata ('celsius', 'fahrenheit', 'kelvin')

        Returns:
        - float: rata-rata suhu dalam satuan yang diminta

        Raises:
        - ValueError: jika ada elemen bukan angka
        """
        try:
            total = sum([float(v) for v in values])
            avg_celsius = total / len(values)
        except:
            raise ValueError("Semua nilai suhu harus berupa angka.")

        # konversi ke unit target
        temp = gemeter(avg_celsius, 'celsius')
        if unit == 'celsius':
            return temp.to_celsius()
        elif unit == 'fahrenheit':
            return temp.to_fahrenheit()
        elif unit == 'kelvin':
            return temp.to_kelvin()
        else:
            raise ValueError("Satuan rata-rata tidak dikenali.")
