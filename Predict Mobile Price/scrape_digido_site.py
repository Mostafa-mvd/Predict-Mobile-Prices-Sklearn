import requests, bs4, re, csv, os



def get_posts_link_digido():
    posts_list = []
    swap = True
    page_number = 1

    while swap:
        try:
            req = requests.get("https://digido.ir/3-mobile?selected_filters=page-{}".format(page_number))
            page_number += 1

            if req.status_code == 200:
                soup = bs4.BeautifulSoup(req.text, "html.parser")
                ul_tags = soup.find("ul", attrs={"id": "product_list", "class":"product_list grid row"})
                li_tags = ul_tags.find_all("li")

                for li_tag in li_tags:
                    post_link = li_tag.find("a").get("href")
                    
                    if ("#/" not in post_link):
                        posts_list.append(post_link)
            else:
                swap = False
                return req.status_code
        except AttributeError:
            swap = False
    return posts_list




def get_description_content(posts_link):
    posts_description = []
    brands = ["Sony", "LG", "Nokia"]

    regex_1 = re.compile(r"([a-zA-Z])")
    regex_2 = re.compile(r"\d+\.?")

    for link in posts_links:
        informations = []
        req          = requests.get(link)

        if req.status_code == 200:
            soup = bs4.BeautifulSoup(req.text, "html.parser")
            span = soup.find("span", attrs={"id": "our_price_display"})

            if span != None:
                price = int(span.get("content"))

                if (price != 0) and (price != 10) and (price != 1):
                    div = soup.find("div", attrs={"id":"short_description_content"})

                    if div != None:
                        meta_content = soup.find("meta", attrs={"itemprop":"name"})

                        if meta_content != None:
                            content_artt = meta_content.get("content")
                            brand_lst    = regex_1.findall(content_artt)
                            main_brand   = ''.join(brand_lst)

                            if (main_brand not in brands):
                                informations.append(price)
                                informations.append(main_brand)
                                ul_tag = div.find("ul")

                                if ul_tag != None:
                                    li_tags = ul_tag.find_all("li")

                                    for idx, li_tag in enumerate(li_tags):
                                        list_text = regex_2.findall(li_tag.text)

                                        if len(list_text) != 0:
                                            if (idx == 3):
                                                text = list_text[0]
                                            else:
                                                text = ''.join(list_text)
                                            informations.append(text)

                                    if (len(informations) == 8) and (" " not in informations):
                                        posts_description.append(informations)
        else:
            return req.status_code
    return posts_description


def write_in_csv(posts_content):
    columns = ["price", "brand", "op", "memmory", "ram", "camera", "network", "battry"]
    csv_file_path = os.path.dirname(__file__) + r"\mobile_info.csv"

    posts_content.insert(0, columns)

    with open(csv_file_path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)

        for row in posts_content:
            writer.writerow(row)




posts_links = get_posts_link_digido()

if isinstance(posts_links, list):
    posts_content = get_description_content(posts_links)

    if isinstance( posts_content, list):
        write_in_csv(posts_content)
    else:
        print(posts_content)

else:
    print(posts_links)




