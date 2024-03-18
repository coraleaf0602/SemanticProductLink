import sqlite3

#Creates new database if one with the same name doesn't already exist
def create_table():
    link_lookup_table = {
        "Laptops and 2-in-1 PC": {
            "url" : "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sc/laptops",
            "image_path" : "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/page/category/laptop/xps/fy24-family-launch/prod-312204-laptop-xps-16-9640-14-9440-13-9340-sl-800x620.png?fmt=png-alpha&wid=640&hei=496"
        }, 
        "XPS": {
            "url" : "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/xps-laptops",
            "image_path" : "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/xps-notebooks/xps-13-9320/media-gallery/xs9320t-cnb-00005ff090-sl-oled.psd?qlt=90,0&op_usm=1.75,0.3,2,0&resMode=sharp&pscan=auto&fmt=png-alpha&hei=500"
        }, 
        "Latitude": {
            "url" : "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/latitude-laptops",
            "image_path" : "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/latitude-notebooks/latitude-14-3440-laptop/media-gallery/notebook-latitude-14-3440-t-dgpu-ir-gray-gallery-12.psd?qlt=90,0&op_usm=1.75,0.3,2,0&resMode=sharp&pscan=auto&fmt=png-alpha&hei=500"
        },
        "Inspiron": {
            "url": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/inspiron-laptops",
            "image_path": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/inspiron-notebooks/16-7640/media-gallery-ai-key/fpr/laptop-inspiron-16-plus-7640nt-bl-dis-fpr-ai-key-gallery-2.psd?qlt=90,0&op_usm=1.75,0.3,2,0&resMode=sharp&pscan=auto&fmt=png-alpha&hei=500"
        }, 
        "Vostro": {
            "url": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/vostro-laptops",
            "image_path": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/vostro-notebooks/vostro-15-3520/media-gallery/black/notebook-vostro-15-3520-gallery-3.psd?qlt=90,0&op_usm=1.75,0.3,2,0&resMode=sharp&pscan=auto&fmt=png-alpha&hei=500"
        }, 
        "Alienware": {
            "url": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/alienware-laptops",
            "image_path": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/alienware-notebooks/alienware-m16-r2-intel/media-gallery/laptop-aw-m16r2-nt-bk-gallery-3.psd?qlt=90,0&op_usm=1.75,0.3,2,0&resMode=sharp&pscan=auto&fmt=png-alpha&hei=500"
        },
        "Precision": {
            "url": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/precision-laptops",
            "image_path": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/workstations/mobile-workstations/precision/15-3581/media-gallery/workstation-notebook-precision-15-3581-gray-gallery-2.psd?qlt=90,0&op_usm=1.75,0.3,2,0&resMode=sharp&pscan=auto&fmt=png-alpha&hei=500"
        },
        "Desktops": {
            "url": "https://www.dell.com/en-ie/shop/desktop-computers/sc/desktops",
            "image_path": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/desktops/optiplex-desktops/optiplex-d13-tower/spi/7010-tower-plus/prod/prod-275100-desktop-optiplex-7010-plus-mt-800x550.png?fmt=png-alpha&wid=800&hei=550"
        },
        "OptiPlex": {
            "url": "https://www.dell.com/en-ie/shop/desktop-computers/sr/desktops/optiplex-desktops",
            "image_path": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/page/banners/optiplex-d13-module-banner-desktop-1023x842.png?qlt=95&fit=constrain,1&hei=800&wid=620&fmt=png-alpha"
        }, 
        "Monitors": {
            "url": "https://www.dell.com/en-ie/shop/computer-monitors/ar/8605",
            "image_path": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/page/category/desktop/dbcs-255750-aio-desktop-optiplex-7410-keyboard-mouse-km7321w-inspiron-27-7710-km5221w-800x620.png?fmt=png-alpha&wid=640&hei=496"
        },
        "Docking Stations": {
            "url": "https://www.dell.com/en-ie/shop/docks-and-stands/ar/5441/docking-stations?appliedRefinements=962",
            "image_path": "https://i.dell.com/is/image/DellContent//content/dam/images/products/electronics-and-accessories/dell/docks-and-stands/wd19s-130w/wd19s-130w-gnb-shot04-bk-singleusbc.psd?qlt=90,0&op_usm=1.75,0.3,2,0&resMode=sharp&pscan=auto&fmt=png-alpha&hei=500"
        }, 
        "Audio": {
            "url": "https://www.dell.com/en-ie/shop/audio/ac/8310",
            "image_path": "https://i.dell.com/is/image/DellContent/bb2303g0045-676544-gl-bb-fy23q4-site-banner-wh5024-wl5024-800x620"
        }, 
        "Keyboards and Mice": {
            "url": "https://www.dell.com/en-ie/shop/keyboards-mice/ar/6591",
            "image_path": "https://i.dell.com/is/image/DellContent//content/dam/ss2/product-images/peripherals/input-devices/dell/keyboards/km7321w/pdp/dell-keyboard-mouse-km7321w-pdp-campaign-hero-504x350.jpg?fmt=jpg&wid=504&hei=350"
        },
        "Hard Drives, SSDs and Storage": {
            "url": "https://www.dell.com/en-ie/shop/hard-drives-storage/ar/8496",
            "image_path": "https://snpi.dell.com/snp/images/products/large/en-ie~400-BKFK_V1/400-BKFK_V1.jpg"
        }, 
        "Webcams and Video Conferencing": {
            "url": "https://www.dell.com/en-ie/shop/web-cameras/ar/8332",
            "image_path": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/peripherals/webcams/wb5023-dell-pro-webcam/media-gallery/webcam-wb5023-black-gallery-1-zoom.psd?qlt=90,0&op_usm=1.75,0.3,2,0&resMode=sharp&pscan=auto&fmt=png-alpha&hei=500"
        }, 
        "Batteries, Chargers and Power Adapters": {
            "url": "https://www.dell.com/en-ie/shop/pc-accessories/ar/5436/batteries-chargers-power-adapters?appliedRefinements=44426",
            "image_path": "https://snpi.dell.com/snp/images/products/large/en-ie~492-BBSC_V3/492-BBSC_V3.jpg"
        }, 
        "Cables and Adapters": {
            "url": "https://www.dell.com/en-ie/shop/cables/ar/8168/cables-adapters?appliedRefinements=44427",
            "image_path": "https://snpi.dell.com/snp/images/products/large/en-ie~470-AEGY/470-AEGY.jpg"
        },
        "Security and Protection": {
            "url": "https://www.dell.com/en-ie/shop/security-protection/ar/7664",
            "image_path": "https://snpi.dell.com/snp/images/products/large/en-ie~461-AAFB_V2/461-AAFB_V2.jpg"
        },
        "Parts, Batteries and Upgrades": {
            "url": "https://www.dell.com/en-ie/shop/parts-batteries-upgrades/ar/7566",
            "image_path": "https://snpi.dell.com/snp/images/products/large/en-ie~161-BBUS/161-BBUS.jpg"
        }, 
        "Wi-Fi and Networking": {
            "url": "https://www.dell.com/en-ie/shop/wifi-and-networking/ar/4011",
            "image_path": "https://snpi.dell.com/snp/images/products/large/en-ie~470-AEUP/470-AEUP.jpg"
        },
        "Gaming Accessories": {
            "url": "https://www.dell.com/en-ie/shop/gaming-gaming-accessories/ac/6488",
            "image_path": "https://i.dell.com/is/image/DellContent/content/dam/documents-and-videos/dv2/csbg/en/product-launch/alienware/alienware-pro-wireless-gaming-peripherals/site-banners/keyboard/black/cs2404g0010-680531-gl-cs-co-site-banner-aw-pro-keyboard-800x620-bk-right-transparent.png"
        }
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
        insert(key,item['url'],item.get('image_path', ''), "")
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



