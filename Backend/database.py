import sqlite3

#Creates new database if one with the same name doesn't already exist
def create_table():
    link_lookup_table = {"Laptops and 2-in-1 PC": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sc/laptops", 
                    "XPS": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/xps-laptops", 
                    "Latitude": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/latitude-laptops", 
                    "Inspiron": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/inspiron-laptops", 
                    "Vostro": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/vostro-laptops", 
                    "Alienware": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/alienware-laptops",
                    "Precision": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/precision-laptops",
                    "Desktops": "https://www.dell.com/en-ie/shop/desktop-computers/sc/desktops",
                    "OptiPlex": "https://www.dell.com/en-ie/shop/desktop-computers/sr/desktops/optiplex-desktops", 
                    "Monitors": "https://www.dell.com/en-ie/shop/computer-monitors/ar/8605",
                    "Docking Stations": "https://www.dell.com/en-ie/shop/docks-and-stands/ar/5441/docking-stations?appliedRefinements=962", 
                    "Audio": "https://www.dell.com/en-ie/shop/audio/ac/8310", 
                    "Keyboards and Mice":"https://www.dell.com/en-ie/shop/keyboards-mice/ar/6591",
                    "Hard Drives, SSDs and Storage": "https://www.dell.com/en-ie/shop/hard-drives-storage/ar/8496", 
                    "Webcams and Video Conferencing": "https://www.dell.com/en-ie/shop/web-cameras/ar/8332", 
                    "Batteries, Chargers and Power Adapters": "https://www.dell.com/en-ie/shop/pc-accessories/ar/5436/batteries-chargers-power-adapters?appliedRefinements=44426", 
                    "Cables and Adapters": "https://www.dell.com/en-ie/shop/cables/ar/8168/cables-adapters?appliedRefinements=44427",
                    "Security and Protection": "https://www.dell.com/en-ie/shop/security-protection/ar/7664",
                    "Parts, Batteries and Upgrades": "https://www.dell.com/en-ie/shop/parts-batteries-upgrades/ar/7566", 
                    "Wi-Fi and Networking": "https://www.dell.com/en-ie/shop/wifi-and-networking/ar/4011",
                    "Gaming Accessories": "https://www.dell.com/en-ie/shop/gaming-gaming-accessories/ac/6488"
                    }
    
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS TestTable (
        name TEXT PRIMARY KEY,
        url TEXT NOT NULL,
        image_path TEXT NOT NULL,
        description TEXT NOT NULL
        )
    '''
    cur.execute(sql)
    for key, item in link_lookup_table.items():
        insert(key,item,"","")
    conn.commit()
    conn.close()

#Function to insert a row into the database
def insert(name, url, image_path, description):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('''INSERT OR REPLACE INTO TestTable (name, url, image_path, description)
                VALUES (?, ?, ?, ?)''', (name, url, image_path, description))
    conn.commit()
    conn.close()

# Retrieve a row from the database
def retrieve(name):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM TestTable WHERE name = ?''', (name,))
    row = cur.fetchone()
    conn.close()
    if row == None : return None
    res = []
    for element in row:
        res.append(element)
    return res

if __name__ == "__main__":
    create_table()



