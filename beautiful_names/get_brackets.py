from decouple import config
import pandas as pd
import os
import warnings

if __name__ == '__main__':
    file_w_street_names = config('file_w_street_names', default='')
    street_types = config('street_types', default='')
    print(file_w_street_names)
    print(os.getcwd())
    warnings.simplefilter("ignore")
    if os.path.exists(file_w_street_names):
        df = pd.read_excel(file_w_street_names)
        print('OK')
    else:
        print('file does not exist')
        exit(1)

    print(df.head())
    print(df.columns)

    df_brackets_names = df[df['Название'].str.contains("\(", na=False)]
    print(df_brackets_names.head())
    df_brackets_names.to_csv(street_types, index=False)
     # df_brackets_names['draft_types'] = df[df['Название'].str.extract('.*\((.*)\).*')]
    # df_brackets_names['draft_types'] = df_brackets_names['Название'].str.findall(r"(?<=\()((^))+)(?=\))")
    # df_brackets_names['draft_types'] = df_brackets_names['Название'].str.findall(r".*\((.*)\).*")

    # df_types_unique = df_brackets_names['draft_types'].drop_duplicates()
    # df_types_unique.to_csv(street_types, index=False)
    # print(df_types_unique)
    # df_types_unique.to_csv(street_types, index=False)

    # print(df_brackets_names['draft_types'].head())

