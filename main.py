import requests
import json


def get_data():
    cookies = {
        '__lhash_': '58d197dbb93a93f2849e7639909787c6',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'MVID_2_exp_in_1': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityR_95',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GTM_DELAY': 'true',
        'MVID_GUEST_ID': '21079542195',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '1300000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MOBILE_FILTERS': 'false',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_REGION_ID': '95',
        'MVID_REGION_SHOP': 'S898',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_SMART_BANNER_BOTTOM': 'true',
        'MVID_SUPER_FILTERS': 'true',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'searchType2': '1',
        'mindboxDeviceUUID': '55088a2a-431b-463b-83dc-5846a5f32742',
        'directCrm-session': '%7B%22deviceGuid%22%3A%2255088a2a-431b-463b-83dc-5846a5f32742%22%7D',
        '_ym_uid': '1658092685749719476',
        '_ym_d': '1658092685',
        '_ym_isad': '2',
        '_ga': 'GA1.2.1578998655.1658092685',
        '_gid': 'GA1.2.84029423.1658092685',
        'partnerSrc': 'yandex',
        'admitad_uid': '%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC',
        'utm_term': '%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC',
        '__SourceTracker': 'yandex__cpc',
        'admitad_deduplication_cookie': 'yandex__cpc',
        '__allsource': 'yandex',
        '__sourceid': 'yandex',
        '__cpatrack': 'yandex_cpc',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '3a20d5e4300b140bff1f819d654ae346',
        'tmr_lvidTS': '1658092687131',
        'advcake_track_id': '633bffa4-3362-d05a-b033-0ef28ec66818',
        'advcake_session_id': 'a2014bfb-2070-7819-6503-addd5cdee5b2',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Nn_Image_Name_Pure_search_desktop%26utm_content%3Dpid%7C21914417751_%7Ccid%7C54501827%7Cgid%7C4285491394%7Caid%7C9547803829%7Cpos%7Cpremium1%7Ckey%7C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C47%7Cregion_name%7C%25D0%259D%25D0%25B8%25D0%25B6%25D0%25BD%25D0%25B8%25D0%25B9%2520%25D0%259D%25D0%25BE%25D0%25B2%25D0%25B3%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B4%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3D%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%26reff%3Dyandex_cpc_ipr_Nn_Image_Name_Pure_Search%26yclid%3D2291047242710122495',
        'advcake_utm_partner': 'ipr_Nn_Image_Name_Pure_search_desktop',
        'advcake_utm_webmaster': 'pid%7C21914417751_%7Ccid%7C54501827%7Cgid%7C4285491394%7Caid%7C9547803829%7Cpos%7Cpremium1%7Ckey%7C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C47%7Cregion_name%7C%25D0%259D%25D0%25B8%25D0%25B6%25D0%25BD%25D0%25B8%25D0%25B9%2520%25D0%259D%25D0%25BE%25D0%25B2%25D0%25B3%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B4%7Ccoef_goal%7C0%7Cdesktop',
        'advcake_click_id': '',
        'uxs_uid': 'f41d6380-0615-11ed-be06-495ed36d8669',
        'st_uid': '95b64a4411647a17b2d9423d33267c62',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '18503323-eb60-4ade-959a-ac9d8cdcf359',
        'flocktory-uuid': 'bb297c30-e73e-4069-ad87-a1b4a92a2e89-5',
        'afUserId': '25fcf633-61ca-4ed4-9f96-67bf046b11ee-p',
        'AF_SYNC': '1658092689043',
        'BIGipServeratg-ps-prod_tcp80': '1157946378.20480.0000',
        'bIPs': '-1178626581',
        'tmr_detect': '0%7C1658092689636',
        'JSESSIONID': '2LGjvJ8BsJQPb9dkt6y0Znh2FsyM5vRdgwsjVgZ5myKTzT4mTK5H!-1216958361',
        'MVID_CART_AVAILABILITY': '2',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_ENVCLOUD': 'prod2',
        'tmr_reqNum': '16',
        '_ga_BNX5WPP3YK': 'GS1.1.1658092684.1.1.1658092808.60',
        '_ga_CFMZTSS5FM': 'GS1.1.1658092684.1.1.1658092808.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=58d197dbb93a93f2849e7639909787c6; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MVID_2_exp_in_1=2; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityR_95; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GTM_DELAY=true; MVID_GUEST_ID=21079542195; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=1300000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MOBILE_FILTERS=false; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_REGION_ID=95; MVID_REGION_SHOP=S898; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_SMART_BANNER_BOTTOM=true; MVID_SUPER_FILTERS=true; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=1; mindboxDeviceUUID=55088a2a-431b-463b-83dc-5846a5f32742; directCrm-session=%7B%22deviceGuid%22%3A%2255088a2a-431b-463b-83dc-5846a5f32742%22%7D; _ym_uid=1658092685749719476; _ym_d=1658092685; _ym_isad=2; _ga=GA1.2.1578998655.1658092685; _gid=GA1.2.84029423.1658092685; partnerSrc=yandex; admitad_uid=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC; utm_term=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC; __SourceTracker=yandex__cpc; admitad_deduplication_cookie=yandex__cpc; __allsource=yandex; __sourceid=yandex; __cpatrack=yandex_cpc; SMSError=; authError=; tmr_lvid=3a20d5e4300b140bff1f819d654ae346; tmr_lvidTS=1658092687131; advcake_track_id=633bffa4-3362-d05a-b033-0ef28ec66818; advcake_session_id=a2014bfb-2070-7819-6503-addd5cdee5b2; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Nn_Image_Name_Pure_search_desktop%26utm_content%3Dpid%7C21914417751_%7Ccid%7C54501827%7Cgid%7C4285491394%7Caid%7C9547803829%7Cpos%7Cpremium1%7Ckey%7C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C47%7Cregion_name%7C%25D0%259D%25D0%25B8%25D0%25B6%25D0%25BD%25D0%25B8%25D0%25B9%2520%25D0%259D%25D0%25BE%25D0%25B2%25D0%25B3%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B4%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3D%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%26reff%3Dyandex_cpc_ipr_Nn_Image_Name_Pure_Search%26yclid%3D2291047242710122495; advcake_utm_partner=ipr_Nn_Image_Name_Pure_search_desktop; advcake_utm_webmaster=pid%7C21914417751_%7Ccid%7C54501827%7Cgid%7C4285491394%7Caid%7C9547803829%7Cpos%7Cpremium1%7Ckey%7C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C47%7Cregion_name%7C%25D0%259D%25D0%25B8%25D0%25B6%25D0%25BD%25D0%25B8%25D0%25B9%2520%25D0%259D%25D0%25BE%25D0%25B2%25D0%25B3%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B4%7Ccoef_goal%7C0%7Cdesktop; advcake_click_id=; uxs_uid=f41d6380-0615-11ed-be06-495ed36d8669; st_uid=95b64a4411647a17b2d9423d33267c62; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=18503323-eb60-4ade-959a-ac9d8cdcf359; flocktory-uuid=bb297c30-e73e-4069-ad87-a1b4a92a2e89-5; afUserId=25fcf633-61ca-4ed4-9f96-67bf046b11ee-p; AF_SYNC=1658092689043; BIGipServeratg-ps-prod_tcp80=1157946378.20480.0000; bIPs=-1178626581; tmr_detect=0%7C1658092689636; JSESSIONID=2LGjvJ8BsJQPb9dkt6y0Znh2FsyM5vRdgwsjVgZ5myKTzT4mTK5H!-1216958361; MVID_CART_AVAILABILITY=2; MVID_CREDIT_AVAILABILITY=true; MVID_ENVCLOUD=prod2; tmr_reqNum=16; _ga_BNX5WPP3YK=GS1.1.1658092684.1.1.1658092808.60; _ga_CFMZTSS5FM=GS1.1.1658092684.1.1.1658092808.0',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.0.1842 Yowser/2.5 Safari/537.36',
        'x-kl-ajax-request': 'Ajax_Request',
        'x-set-application-id': '28d5169c-c8f2-4695-9765-6db95614d3ed',
    }

    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    # print(response)

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('2_items.json', 'w', encoding="utf-8") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json', encoding="utf-8") as file:
        products_data = json.load(file)

    with open('4_items_prices.json', encoding="utf-8") as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w',encoding="utf-8") as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()
