import re
import math

import pandas as pd


data = pd.read_csv("../data/mobile_price.csv")


def filter_brand(text):
    return re.sub(r"[^a-zA-Z0-9/()\s]", "", text)


def cleaning():
    filtered_brands = [filter_brand(text) for text in data["phone_name"]]
    
    valid_brands = [
    "xiaomi", "realme", "blackview", "oukitel", "doogee", "ulefone", "infinix", "samsung",
    "sigma", "oppo", "tecno", "poco", "zte", "nokia", "oneplus", "google", "apple", "cubot",
    "honor", "nomi", "hmd", "hotwav", "motorola", "umidigi", "maxcom", "asus", "panasonic",
    "servo", "agm", "ergo", "fossibot", "unihertz", "nubia", "oscal", "nothing", "sony",
    "myphone", "vivo", "huawei", "ihunt", "krugermatz", "meizu", "redmagic", "vertu", "cat",
    "cmf", "caterpillar", "tcl", "gigaset", "hoco", "coolpad", "estar", "hmobile", "evelatus",
    "gtstar", "mediatek", "mktel", "verico", "iiif150", "alcatel", "conquest", "yeemi",
    "discovery", "gzone", "hammer", "beafon", "wiko", "miniphone", "l8star", "htc", "vertex",
    "blackberry", "wisephone", "uniwa", "inmarsat", "mafam", "iqoo", "soyes", "sharp",
    "ruggear", "spc", "allview", "doro", "microsoft", "laimi", "freeyond", "hope", "easyfone",
    "vkworld", "kenxinda", "lg", "hafury", "mann", "rugtel"
    ]
    phones_names = []
    brands = []
    
    for text in filtered_brands:
        phones_names.append(text.strip().lower())
        for brand in valid_brands:
            other_phone = True  
            if re.search(rf"\b{brand}\b", text.lower()):
                brands.append(brand)
                other_phone = False
                break
        if other_phone:
            brands.append("other phone")
    data["phone_name"] = pd.DataFrame(phones_names, index=data.index, columns=["phone_name"])
    data["brand"] = pd.DataFrame(brands, index=data.index, columns=["beand"])
    
    brand_counts = data["brand"].value_counts()
    common_brands = brand_counts[brand_counts>=10].index
    data["brand"] = data["brand"].apply(lambda x: x if x in common_brands else "other phone")
    
    data["rating"] = data["rating"].replace("Залишити відгук", 0)
    data["rating"] = data["rating"].astype(int)
    
    discounts_procents = []
    for discounts, prices in zip(data["price_before_discount"], data["price"]):
        if discounts > 0:
            discounts_procents.append(math.ceil(((discounts - prices) / discounts) * 100))
        else:
            discounts_procents.append(0)
    data["discount_procent"] = pd.DataFrame(discounts_procents, index=data.index, columns=["discount_procent"])
   
    data.to_csv("../data/clean_mobile_price.csv", index=False)
    

def main():
    cleaning()


if __name__=="__main__":
    main()
