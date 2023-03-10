import gspread

bot_token = '5671800655:AAF_wGj1B_4cAtUYm42X4ArfIALWrE3uf-Q'
googlesheet_id = '1MZIJ6fY8_mKgvGk1WXAmNvERoz9Gs5x3BoL43Ds4OL8'
gc = gspread.service_account('my-cct-project-c5b41f676155.json')
sh_kom = gc.open_by_key('1MZIJ6fY8_mKgvGk1WXAmNvERoz9Gs5x3BoL43Ds4OL8')
sh_kam = gc.open_by_key('1TfdXVDB49qCtHLuc4ZtzjpyJLdpr2s1zlvg3cI4U7Rk')

series = ["Первая", "Вторая", "Третья", "Четвёртая", "Пятая", "Шестая", "Седьмая", "Восьмая", "Девятая", "Десятая"]


TEAMS = {"Космос": ["Космос", "B2:H2", "A4"],
         "Мишутка": ["Мишутки", "B3:H3", "A12"],
         "Логика": ["Логики", "B4:H4", "A20"],
         "Алиот": ["Алиота", "B5:H5", "A28"],
         "Белиал": ["Белиала", "B6:H6", "A36"],
         "Факер": ["Факера", "B7:H7", "A44"],
         "Душебой": ["Душебоя", "B8:H8", "A52"],
         "Малина": ["Малины", "B9:H9", "A60"],
         "Кукла": ["Куклы", "B10:H10", "A68"],
         "Олки": ["Олки", "B11:H11", "A76"]
         }

PLAYERS = {"Интерактив": ["B4:M4", "1", "Космос"],
           "F5": ["B5:M5", "2", "Космос"],
           "Bonger": ["B6:M6", "3", "Космос"],
           "Альпака": ["B7:M7", "4", "Космос"],
           "Nero": ["B8:M8", "5", "Космос"],
           "Lijo": ["B9:M9", "6", "Космос"],
           "Davatar": ["B10:M10", "7", "Космос"],
           "Америка": ["B12:M12", "1", "Мишутка"],
           "Изанами": ["B13:M13", "2", "Мишутка"],
           "Милка": ["B14:M14", "3", "Мишутка"],
           "Фреско": ["B15:M15", "4", "Мишутка"],
           "Dark": ["B16:M16", "5", "Мишутка"],
           "Sky": ["B17:M17", "6", "Мишутка"],
           "Usernameandnumber": ["B18:M18", "7", "Мишутка"],
           "Фенке": ["B20:M20", "1", "Логика"],
           "Miracle": ["B21:M21", "2", "Логика"],
           "Марта": ["B22:M22", "3", "Логика"],
           "Tony": ["B23:M23", "4", "Логика"],
           "Поварец": ["B24:M24", "5", "Логика"],
           "49": ["B25:M25", "6", "Логика"],
           "dor": ["B26:M26", "7", "Логика"],
           "День": ["B28:M28", "1", "Алиот"],
           "Шахматист": ["B29:M29", "2", "Алиот"],
           "Пим": ["B30:M30", "3", "Алиот"],
           "Артик": ["B31:M31", "4", "Алиот"],
           "Дари": ["B32:M32", "5", "Алиот"],
           "Вальхалла": ["B33:M33", "6", "Алиот"],
           "Batman": ["B34:M34", "7", "Алиот"],
           "deeelis": ["B36:M36", "1", "Белиал"],
           "Тоторо": ["B37:M37", "2", "Белиал"],
           "Жирафа": ["B38:M38", "3", "Белиал"],
           "Taras": ["B39:M39", "4", "Белиал"],
           "Red": ["B40:M40", "5", "Белиал"],
           "tkzoid": ["B41:M41", "6", "Белиал"],
           "Nongrata": ["B42:M42", "7", "Белиал"],
           "Мартовский_кот": ["B44:M44", "1", "Факер"],
           "Maddie": ["B45:M45", "2", "Факер"],
           "Мячо": ["B46:M46", "3", "Факер"],
           "hanna_ross": ["B47:M47", "4", "Факер"],
           "Koverhunter": ["B48:M48", "5", "Факер"],
           "Утка": ["B49:M49", "6", "Факер"],
           "Broniak": ["B50:M50", "7", "Факер"],
           "Klauz": ["B52:M52", "1", "Душебой"],
           "Фокс": ["B53:M53", "2", "Душебой"],
           "Nefelim": ["B54:M54", "3", "Душебой"],
           "Шершень": ["B55:M55", "4", "Душебой"],
           "Mango": ["B56:M56", "5", "Душебой"],
           "Хохольчик": ["B57:M57", "6", "Душебой"],
           "Leo": ["B58:M58", "7", "Душебой"],
           "4yba": ["B60:M60", "1", "Малина"],
           "Goblak": ["B61:M61", "2", "Малина"],
           "Kamille": ["B62:M62", "3", "Малина"],
           "Комар": ["B63:M63", "4", "Малина"],
           "Снайпер": ["B64:M64", "5", "Малина"],
           "Yoliver": ["B65:M65", "6", "Малина"],
           "ZodiacBC": ["B66:M66", "7", "Малина"],
           "22": ["B68:M68", "1", "Кукла"],
           "Molomus": ["B69:M69", "2", "Кукла"],
           "Byrbon4eg": ["B70:M70", "3", "Кукла"],
           "pkt": ["B71:M71", "4", "Кукла"],
           "Aleksa": ["B72:M72", "5", "Кукла"],
           "bggclr": ["B73:M73", "6", "Кукла"],
           "Коклюш": ["B74:M74", "7", "Кукла"],
           "Ганди": ["B76:M76", "1", "Олки"],
           "Space_cadet": ["B77:M77", "2"],
           "Senpai": ["B78:M78", "3", "Олки"],
           "derekoy": ["B79:M79", "4", "Олки"],
           "Мистер_Кусака": ["B80:M80", "5", "Олки"],
           "Мандарин": ["B81:M81", "6", "Олки"],
           "Mr.Fox": ["B82:M82", "7", "Олки"]}