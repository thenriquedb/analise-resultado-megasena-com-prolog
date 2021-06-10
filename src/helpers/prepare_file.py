import pandas as pd


class PrepareFile:
    def __init__(self, input_path):
        self.data = None
        self.__read_file(input_path)
        # self.__remove_unecessary_columns()
        # self.__rename_columns()

    def __read_file(self, path):
        file_extension = path.strip()[-3:]

        if file_extension == 'csv':
            self.data = pd.read_csv(path)
        elif file_extension == 'xlsx':
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

    def itertuples(self):
        return self.data.itertuples()

    def to_csv(self, path):
        print("> Save file to csv...")
        self.data.to_csv(path, index=False)
