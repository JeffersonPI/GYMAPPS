class Trainer:
    def __init__(self, trainer_id, name, specialist, price_per_session):
        self.trainer_id = trainer_id
        self.name = name
        self.specialist = specialist
        self.price_per_session = price_per_session

    def info(self):
        return f"""
ID          : {self.trainer_id}
Name        : {self.name}
Specialist  : {self.specialist}
Price       : Rp {self.price_per_session}
-------------------------
"""
class Trainer:
    def __init__(self, trainer_id, name, specialist, price_per_session):
        self.trainer_id = trainer_id
        self.name = name
        self.specialist = specialist
        self.price_per_session = price_per_session

    def info(self):
        return f"""
ID          : {self.trainer_id}
Name        : {self.name}
Specialist  : {self.specialist}
Price       : Rp {self.price_per_session}
-------------------------
"""