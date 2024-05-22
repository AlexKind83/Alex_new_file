import sqlite3


with sqlite3.connect('homework_44.db') as con:
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS seller (
        line INTEGER PRIMARY KEY AUTOINCREMENT,
        shop TEXT NOT NULL,
        id_seller INTEGER,
        FOREIGN KEY (id_seller) REFERENCES Products (id_seller)
    );
    CREATE TABLE IF NOT EXISTS Products (
        id_seller INTEGER,
        id_product INTEGER,
        name_product TEXT NOT NULL,
        price INTEGER,
        count INTEGER,
        FOREIGN KEY (id_seller) REFERENCES seller (id_seller),
        FOREIGN KEY (id_product) REFERENCES System_Block (id_product),
        FOREIGN KEY (id_product) REFERENCES Monitor (id_product),
        FOREIGN KEY (id_product) REFERENCES Printer (id_product)

    );
    CREATE TABLE IF NOT EXISTS System_Block (
        id_product TEXT,
        brand TEXT,
        processor TEXT,
        op TEXT,
        sdd INTEGER,
        video_card TEXT,
        FOREIGN KEY (id_product) REFERENCES Products (id_product)
    );
    CREATE TABLE IF NOT EXISTS Monitor (
        id_product TEXT,
        brand TEXT, 
        diagonal INTEGER,
        screen_resolution INTEGER,
        matrix TEXT,
        FOREIGN KEY (id_product) REFERENCES Products (id_product)
    );
    CREATE TABLE IF NOT EXISTS Printer (
        id_product TEXT,
        brand TEXT,
        print_color TEXT,
        type TEXT,
        FOREIGN KEY (id_product) REFERENCES Products (id_product)
    );
    """)

    sellers_tpl = [
        ('ТехноСити', 1),
        ('TurboBoost', 2),
        ('LiveComp', 3),
    ]

    products_tpl = [
        (sellers_tpl[0][1], 'p1', 'системный блок', 82285, 14),
        (sellers_tpl[0][1], 'p2', 'системный блок', 57138, 10),
        (sellers_tpl[1][1], 'p3', 'системный блок', 78325, 4),
        (sellers_tpl[2][1], 'p4', 'системный блок', 96053, 4),
        (sellers_tpl[0][1], 'p5',  'монитор', 14525, 7),
        (sellers_tpl[1][1], 'p6',  'монитор', 28414, 8),
        (sellers_tpl[1][1], 'p7',  'монитор', 5910, 5),
        (sellers_tpl[2][1], 'p8', 'монитор', 16367, 9),
        (sellers_tpl[0][1], 'p9', 'принтер', 12534, 4),
        (sellers_tpl[1][1], 'p10', 'принтер', 37982, 3),
        (sellers_tpl[2][1], 'p11', 'принтер', 16756, 7),
        (sellers_tpl[2][1], 'p12', 'принтер', 53139, 5),
    ]

    system_block_tpl = [
        (products_tpl[0][1], 'intel', 'intel Core i7-5820K', '32 гб', 1000, 'NVIDIA GeForce RTX 3060 (12 гб)'),
        (products_tpl[1][1], 'HP', 'intel Core i5-11400F', '8 гб', 256, 'NVIDIA GeForce GTX 1650 (4 гб)'),
        (products_tpl[2][1], 'AMD', 'AMD Ryzen 5 5500', '16 гб', 1024, 'NVIDIA GeForce GTX 1660 SUPER (6 гб)'),
        (products_tpl[3][1], 'ASUS', 'intel Core i5-11400F', '8 гб', 512, 'NVIDIA GeForce GTX 1660 Ti (6 гб)'),
    ]

    monitor_tpl = [
        (products_tpl[4][1], 'Hartens', 32, '1920x1080 Full HD', 'VA'),
        (products_tpl[5][1], 'Xiaomi', 34, '3440x1440 Ultra WQHD', 'VA'),
        (products_tpl[6][1], 'Digma', 21.5, '1920x1080 Full HD', 'VA'),
        (products_tpl[7][1], 'Lenovo', 27, '1920x1080 Full HD', 'VA'),
    ]

    printer_tpl = [
        (products_tpl[8][1], 'Pantum M6500', 'Монохромный', 'Лазерный'),
        (products_tpl[9][1], 'Canon', 'Монохромный Цветной', 'Струйный'),
        (products_tpl[10][1], 'HP', 'Монохромный', 'Лазерный'),
        (products_tpl[11][1], 'Epson', 'Монохромный Цветной', 'Струйный'),
    ]

    cur.executemany(f"INSERT INTO seller VALUES(NULL, ?, ?)", sellers_tpl)
    cur.executemany(f'INSERT INTO Products VALUES(?, ?, ?, ?, ?)', products_tpl)
    cur.executemany(f'INSERT INTO System_Block VALUES(?, ?, ?, ?, ?, ?)', system_block_tpl)
    cur.executemany(f'INSERT INTO Monitor VALUES(?, ?, ?, ?, ?)', monitor_tpl)
    cur.executemany(f'INSERT INTO Printer VALUES(?, ?, ?, ?)', printer_tpl)
