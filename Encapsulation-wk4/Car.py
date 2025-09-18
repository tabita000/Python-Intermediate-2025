class Car:
    def __init__(self, make, model, tank_size, gas_level):
        self._make = make
        self._model = model
        self._tank_size = tank_size
        self._gas_level = gas_level

    # Getter and Setter for make
    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    # Getter and Setter for model
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    # Getter and Setter for tank_size
    @property
    def tank_size(self):
        return self._tank_size

    @tank_size.setter
    def tank_size(self, value):
        self._tank_size = value

    # Getter and Setter for gas_level
    @property
    def gas_level(self):
        return self._gas_level

    @gas_level.setter
    def gas_level(self, value):
        if value > self._tank_size:
            self._gas_level = self._tank_size
        else:
            self._gas_level = value

    # Add gas method
    def add_gas(self, amount):
        if self._gas_level + amount > self._tank_size:
            self._gas_level = self._tank_size
        else:
            self._gas_level += amount

    # Car info method
    def car_info(self):
        return f"Make: {self._make}, Model: {self._model}, Tank Size: {self._tank_size} gallons, Gas Level: {self._gas_level} gallons"
