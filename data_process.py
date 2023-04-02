import pygame, csv
from setting import block_size
from block import SimpleBlock, Block, Coin, Diamond

def csv_parser(path):
    map_data = []
    with open(path, 'r') as fp:
        map = csv.reader(fp, delimiter=',')
        for row in map:
            map_data.append(row)
    return map_data

def create_ground_block(block_data):
    ground_sprites_group = pygame.sprite.Group()

    for rownum, row in enumerate(block_data):
        for colnum, col in enumerate(row):
            if col != '-1':
                x = block_size * colnum
                y = block_size * rownum
                
                if col == "0":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0000.png"))
                if col == "7":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0020.png"))
                if col == "8":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0021.png"))
                if col == "9":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0022.png"))  
                if col == "10":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0023.png"))   
                if col == "11":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0024.png"))
                if col == "12":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0025.png"))
                if col == "18":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0061.png"))
                if col == "19":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0062.png"))
                if col == "20":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0063.png"))
                if col == "26":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0101.png"))
                if col == "27":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0102.png"))
                if col == "28":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0103.png"))
                if col == "29":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0120.png"))
                if col == "30":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0121.png"))
                if col == "31":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0122.png"))
                if col == "32":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0123.png"))
                if col == "33":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0140.png"))
                if col == "34":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0141.png"))
                if col == "35":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0142.png"))  
                if col == "36":
                    ground_sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/ground/tile_0143.png"))
    return ground_sprites_group

def create_other_block(block_data, block_name):
    sprites_group = pygame.sprite.Group()
    
    for rownum, row in enumerate(block_data):
        for colnum, col in enumerate(row):
            if col != '-1':
                x = block_size * colnum
                y = block_size * rownum

                if block_name == "grass" and col == "6":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/grass/tile_0124.png"))
                if block_name == "grass" and col == "7":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/grass/tile_0125.png"))
                if block_name == "grass" and col == "8":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/grass/tile_0126.png"))
                if block_name == "grass" and col == "9":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/grass/tile_0127.png"))
                if block_name == "grass" and col == "10":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/grass/tile_0128.png"))
                if block_name == "grass" and col == "11":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/grass/tile_0129.png"))
                if block_name == "grass" and col == "12":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/grass/tile_0144.png"))
                if block_name == "grass" and col == "13":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/grass/tile_0145.png"))

                if block_name == "sign" and col == "0":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/sign/tile_0088.png"))

                if block_name == "water" and col == "0":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/water/tile_0033.png"))
                if block_name == "water" and col == "3":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/water/tile_0053.png"))
                if block_name == "water" and col == "6":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/water/tile_0073.png"))

                if block_name == "flag" and col == "4":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/flag/tile_0112.png"))
                if block_name == "flag" and col == "5":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/flag/tile_0131.png"))

                if block_name == "crate" and col == "0":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/crate/tile_0026.png"))
                if block_name == "crate" and col == "1":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/crate/tile_0104.png"))

                if block_name == "cloud" and col == "3":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/cloud/tile_0153.png"))
                if block_name == "cloud" and col == "4":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/cloud/tile_0154.png"))
                if block_name == "cloud" and col == "5":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/cloud/tile_0155.png"))

                if block_name == "stab" and col == "0":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/stab/tile_0068.png"))
                
                if block_name == "barrier" and col == "0":
                    sprites_group.add(SimpleBlock((x, y), block_size))
                
                if block_name == "coin" and col == "1":
                    sprites_group.add(Coin((x, y), block_size, 1))
                if block_name == "coin" and col == "2":
                    sprites_group.add(Diamond((x, y), block_size, "./assets/block/Tiles/coin/tile_0067.png", 3))
                
                if block_name == "tree" and col == "5":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0017.png"))
                if block_name == "tree" and col == "6":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0018.png"))
                if block_name == "tree" and col == "7":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0019.png"))
                if block_name == "tree" and col == "10":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0037.png"))
                if block_name == "tree" and col == "11":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0038.png"))
                if block_name == "tree" and col == "12":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0039.png"))
                if block_name == "tree" and col == "15":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0057.png"))
                if block_name == "tree" and col == "16":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0058.png"))
                if block_name == "tree" and col == "17":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0059.png"))
                if block_name == "tree" and col == "23":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0096.png"))
                if block_name == "tree" and col == "24":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0097.png"))
                if block_name == "tree" and col == "25":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0098.png"))
                if block_name == "tree" and col == "26":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0099.png"))
                if block_name == "tree" and col == "27":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0116.png"))
                if block_name == "tree" and col == "30":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0119.png"))
                if block_name == "tree" and col == "31":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0136.png"))
                if block_name == "tree" and col == "33":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0138.png"))
                if block_name == "tree" and col == "34":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/tree/tile_0139.png"))
                
                if block_name == "pipe" and col == "0":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/pipe/tile_0093.png"))
                if block_name == "pipe" and col == "1":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/pipe/tile_0094.png"))
                if block_name == "pipe" and col == "5":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/pipe/tile_0115.png"))
                if block_name == "pipe" and col == "7":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/pipe/tile_0133.png"))
                if block_name == "pipe" and col == "9":
                    sprites_group.add(Block((x, y), block_size, "./assets/block/Tiles/pipe/tile_0135.png"))

    return sprites_group