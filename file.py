import excel2json

# excel2json.convert_from_file('1005C_SarlTotal_AdjustmentstoUSGAAP_07-2022 (1).xlsx')


import pandas as pd

file_name = "1005C_SarlTotal_AdjustmentstoUSGAAP_07-2022.xlsx"
sheets_obj = pd.ExcelFile(file_name)
sheet_names = sheets_obj.sheet_names

s_file = file_name.rsplit('.',1)

for s_name in sheet_names:
    excel_data_df = pd.read_excel(file_name, sheet_name=s_name)

    json_str = excel_data_df.to_json(orient='records')

    final_file = f'{s_file[0]}_{s_name}_{s_file[1]}'

    with open(final_file, "w") as outfile:
        outfile.write(json_str)


print('Excel file converted into json')