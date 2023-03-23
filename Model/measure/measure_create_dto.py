class MeasureCreateDto:
    def __init__(self, measure_id: int, name: str):
        self.measure_id = measure_id
        self.measure_name = name