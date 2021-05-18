import pandas as pd


class PrepareFile:
    def __init__(self, input_path):
        self.data = None
        self._load_csv(input_path)
        self._remove_unecessary_columns()
        self._rename_columns()
        # self._convert_award_to_number()

    def _load_csv(self, path):
        print('> Load file from ', path, '...')
        self.data = pd.read_excel(path)

    def _rename_columns(self):
        print('> Renaming sheet columns...')

        self.data.rename(
            columns={
                'Conc.': 'contest',
                'Unnamed: 2': 'number_01',
                'Unnamed: 3': 'number_02',
                'Unnamed: 4': 'number_03',
                'Unnamed: 5': 'number_04',
                'Unnamed: 6': 'number_05',
                'Unnamed: 7': 'number_06',
            }, inplace=True)

    def _convert_award_to_number(self):
        print('> Convert award values to numeric values...')
        self.data['award'] = self.data['award'].fillna(0)

    def save_as_csv(self, path):
        print('> Save file to csv .')
        self.data.to_csv(path, index=False)

    def _remove_unecessary_columns(self):
        print('> Remove unecessary columns...')
        self.data.drop(columns=['Gan.', 'Prêmio', 'Data'], inplace=True)


if __name__ == "__main__":
    mega_sena = PrepareFile('inputs/resultados.xlsx')
    mega_sena.save_as_csv('outputs/converted-file.csv')
