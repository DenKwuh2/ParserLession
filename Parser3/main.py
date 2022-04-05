import requests
import json
import datetime

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "...",
    "X-Is-Ajax-Request": "X-Is-Ajax-Request",
    "X-Requested-With": "XMLHttpRequest",

}



def get_data():
    start_time =datetime.datetime.now()
    url = "https://roscarservis.ru/catalog/legkovye/"
    r = requests.get(url=url, headers=headers)

    # with open("index.html", "w", encoding='UTF-8') as file:
    #     file.write(r.text)
    # with open('r.json', "w", encoding='UTF-8') as file:
    #     json.dump(r.json(), file, indent=4, ensure_ascii=False)

    pages_count = r.json()["pageCount"]


    data_list = []
    for page in range(1, pages_count + 1):
        url = f"https://roscarservis.ru/catalog/legkovye/?isAjax=true&PAGEN_1={page}"

        r = requests.get(url=url, headers=headers)
        data = r.json()
        items = data["items"]


        possible_stores = ["discountStores", "fortochkiStores", "commonStores"]
        for item in items:
            total_amount = 0
            item_name = item["name"]
            item_price = item["price"]
            item_img = f'https://roscarservis.ru{item["imgSrc"]}'
            item_url = f'https://roscarservis.ru{item["url"]}'

            stores = []
            for ps in possible_stores:
                if ps in item:
                    if item[ps] is None or len(item[ps]) < 1:
                        continue
                    else:
                        for store in item[ps]:
                            store_name = store['STORE_NAME']
                            store_price = store['PRICE']
                            store_amount = store["AMOUNT"]
                            total_amount += int(store["AMOUNT"])

                            stores.append(
                                {
                                "store_name": store_name,
                                "store_price": store_price,
                                "store_amount": store_amount
                                }
                            )
            data_list.append(
                {
                    "item_name": item_name,
                    "item_price": item_price,
                    "item_img": item_img,
                    "item_url": item_url,
                    "total_amount": total_amount

                }
            )
        print(f"[INFO] Обработал {page}/{pages_count}")

    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

    with open(f"data_{cur_time}.json", "a", encoding="UTF-8") as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)

    diff_time = datetime.datetime.now() - start_time
    print(diff_time)


def main():
    get_data()

if __name__ == '__main__':
    main()
