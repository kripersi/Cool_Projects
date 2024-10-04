import gspread


def update_sheet(title, text, hashtags, link_rss, folder, name_sheet_write):
    gc = gspread.service_account(filename=fr"{folder}/credentials.json")

    sh = gc.open(name_sheet_write)
    worksheet = sh.sheet1

    values_list = int(len(worksheet.col_values(1)))

    worksheet.update([[str(values_list), str(title), str(text), str(hashtags), link_rss]], f'A{values_list+1}:E{values_list+1}')


def read_sheet(folder, name_sheet_read):
    gc = gspread.service_account(filename=fr"{folder}/credentials.json")

    sh = gc.open(name_sheet_read)
    worksheet = sh.sheet1

    values_list = worksheet.get_all_values()

    return values_list
