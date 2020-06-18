from sklearn.tree import DecisionTreeClassifier
import csv, os


csv_file_path = os.path.dirname(__file__) + r"\mobile_info.csv"

# ['price', 'brand', 'op', 'memmory', 'ram', 'camera', 'network', 'battry']
# y_train = list of prices
# x_train = ['brand', 'op', 'memmory', 'ram', 'camera', 'network', 'battry']
# brands_code = {'Samsung': 8397109115117110103, 'Lamborghini': 769710998111114103104105110105, 'Apple': 65112112108101, 'Xiaomi': 8810597111109105, 'CaterPillar': 67971161011148010510810897114, 'Huawei': 7211797119101105, 'HONOR': 7279787982, 'Tecno': 8410199110111, 'OnePlus': 7911010180108117115, 'Vivo': 86105118111, 'BlackBerry': 66108979910766101114114121, 'HTC': 728467, 'Motorola': 7711111611111411110897, 'Meizu': 77101105122117, 'Gplus': 71112108117115, 'Pantech': 809711011610199104, 'LAVA': 76658665}


with open(csv_file_path, "r") as csv_file:
    x_train = []
    y_train = []

    brands_code = {'Samsung': 8397109115117110103, 'Lamborghini': 769710998111114103104105110105, 'Apple': 65112112108101, 'Xiaomi': 8810597111109105, 'CaterPillar': 67971161011148010510810897114, 'Huawei': 7211797119101105, 'HONOR': 7279787982, 'Tecno': 8410199110111, 'OnePlus': 7911010180108117115, 'Vivo': 86105118111, 'BlackBerry': 66108979910766101114114121, 'HTC': 728467, 'Motorola': 7711111611111411110897, 'Meizu': 77101105122117, 'Gplus': 71112108117115, 'Pantech': 809711011610199104, 'LAVA': 76658665}

    dtcf   = DecisionTreeClassifier()

    reader = csv.reader(csv_file)

    for row in list(reader)[1:]:
        price      = int(row[0])
        brand_code = int(''.join(list(map(str,map(ord,row[1]))))) #encode brand name

        try:
            list_x = list(map(float, row[2:]))
            list_x.insert(0, brand_code)
            x_train.append(list_x)
            y_train.append(price)
        except:
            continue


    dtcf.fit(x_train, y_train)


# example:
# for predict use these:
    # brand_code  = brands_code["Samsung"]
    # list_x_data = [[brand_code, 11, 32, 2, 12, 4, 3000]]
    # list_pred_y = dtcf.predict(list_x_data)

    # print(f"\n\nmy x values are:\n{list_x_data}\n\nmy y is:\n{list_pred_y}\n\n")



















