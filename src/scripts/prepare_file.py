import pandas as pd


class PrepareFile:
    def __init__(self, input_path):
        self.data = None
        self.__load_csv(input_path)
        self.__remove_unecessary_columns()
        self.__rename_columns()

    def __load_csv(self, path):
        print("> Load file from ", path, "...")
        self.data = pd.read_excel(path)

    def __rename_columns(self):
        print("> Renaming sheet columns...")

        self.data.rename(
            columns={
                "Conc.": "contest",
                "Unnamed: 2": "number_01",
                "Unnamed: 3": "number_02",
                "Unnamed: 4": "number_03",
                "Unnamed: 5": "number_04",
                "Unnamed: 6": "number_05",
                "Unnamed: 7": "number_06",
            },
            inplace=True,
        )

    def __remove_unecessary_columns(self):
        print("> Remove unecessary columns...")
        self.data.drop(columns=["Gan.", "Prêmio", "Data"], inplace=True)

    def to_csv(self, path):
        print("> Save file to csv .")
        self.data.to_csv(path, index=False)


if __name__ == "__main__":
    mega_sena = PrepareFile("data/resultados.xlsx")
    mega_sena.to_csv("data/games.csv")
