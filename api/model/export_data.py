import csv
from api.model import models
from api.model.database import SessionLocal, engine


class Data:

    def __init__(self):
        pass

    def export_data(self, db):

        with open("api/model/food_data_alter.csv", "r") as f:
            csv_reader = csv.DictReader(f)

            for row in csv_reader:
                db_alimentos = models.Alimento(
                    nome=(row["Nome"]),
                    valor=0.0,
                    energia=row["Energia"],
                    proteinas=row["Proteína"],
                    carboidratos=row["Carboidrato"],
                    lipideos=row["Lipídeos"],
                    fibras=row["Fibra"],
                    calcio=row["Cálcio"],
                    ferro=row["Ferro"],
                    zinco=row["Zinco"],
                    magnesio=row["Magnésio"],
                )

                db.add(db_alimentos)

            db.commit()

        db.close()

data_alimentos = Data()
