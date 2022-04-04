import requests
import img2pdf

def get_data():
    headers = {
        "User-Agent": "..."
    }

    img_list = []
    for i in range(1, 49):
        url = f'https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg'
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            img_list.append(f'media/{i}.jpg')
            print(f"Скачано {i} из 48")

    # Открываем запись файла в двоичном формате
    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))

    print("PDF файл создан")

    print('_' * 25)
    print(img_list)

#второй вариант
def write_to_pdf():
    img_list = [f'media/{i}.jpg' for i in range(1, 49)]

    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))

    print("PDF файл создан")

def main():
    #get_data()
    write_to_pdf()
if __name__ == "__main__":
    main()
