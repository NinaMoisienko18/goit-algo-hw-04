from pathlib import Path

text_file = "cat_info.txt"

with open(text_file, "w") as ct:
    info = "60b90c1c13067a15887e1ae1,Tayson,3\n" \
           "60b90c2413067a15887e1ae2,Vika,1\n" \
           "60b90c2e13067a15887e1ae3,Barsik,2\n" \
           "60b90c3b13067a15887e1ae4,Simon,12\n" \
            "60b90c4613067a15887e1ae5,Tessi,5"
    ct.write(info)


path = Path(text_file).absolute()


def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as ctp_read:
            lines = [ctp.strip().split(",") for ctp in ctp_read.readlines()]

        dict_list = []
        for line in lines:

            cat_dict = {
                "id": line[0],
                "name": line[1],
                "age": line[2]
            }
            dict_list.append(cat_dict)

        path.unlink()
        return dict_list


    except FileNotFoundError:
        return f">>> Файлу - {path.name} - НЕ знайдено."

cats_info = get_cats_info(path)
print(cats_info)

