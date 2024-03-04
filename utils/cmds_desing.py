from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.functions import symbol

text_home = """𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝘼𝙠𝙖𝙩𝙨𝙪𝙠𝙞 -» >_
<code>This bot promises you fast and safe checkups with different gateways and perfect tools for your use! ✨</code>
                  
<a href='tg://user?id={}'>朱 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 </a> -» <code>1.3</code>"""

exit_button = InlineKeyboardButton("𝙀𝙭𝙞𝙩 ⚠️", "exit")

buttons_cmds = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("𝙂𝙖𝙩𝙚𝙨 ♻️", "gates"),
            InlineKeyboardButton("𝙏𝙤𝙤𝙡𝙨 🛠", "tools"),
        ],
        [InlineKeyboardButton("𝘾𝙝𝙖𝙣𝙣𝙚𝙡 💫", url="https://t.me/akatsukichk")],
        [exit_button],
    ]
)

buttons_gates = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("𝘼𝙪𝙩𝙝 🥷", "auths"),
            InlineKeyboardButton("𝘾𝙝𝙖𝙧𝙜𝙚𝙙 🤑", "chargeds"),
        ],
        [InlineKeyboardButton("𝙎𝙥𝙚𝙘𝙞𝙖𝙡 🥷", "specials")],
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
        [exit_button],
    ]
)


# RETURN & EXIT GATES
return_and_exit_gates = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "gates")],
        [exit_button],
    ]
)

# RETURN HOME & EXIT
return_home_and_exit = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
        [exit_button],
    ]
)


# GATES AUTH

text_gates_auth = f"""
𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘼𝙪𝙩𝙝

{symbol("朱 𝙍𝙤𝙝𝙚𝙚")} -» <code>Adyen -» Auth</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.rh</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝑜𝑑𝑎𝑙𝑖")} -» <code>Shopify -» Auth</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.od</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙎𝙚𝙭𝙤")} -» <code>Braintree -» Auth</code> 
{symbol("零 𝘾𝙢𝙙")} -» <code>.sexo</code> -» <code>Free</code> 
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙋𝙪𝙨𝙨𝙮")} -» <code>Braintree -» Auth</code> 
{symbol("零 𝘾𝙢𝙙")} -» <code>.ps</code> -» <code>Premium</code> 
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝑀𝒶𝒾𝓇𝒾𝓃")} -» <code>Braintree Avs Vbv -» Auth</code> 
{symbol("零 𝘾𝙢𝙙")} -» <code>.mai</code> -» <code>Premium</code> 
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙄𝙩𝙖𝙘𝙝𝙞")} -» <code>Payflow Avs codes -» Auth</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.it</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙕𝙪𝙠𝙚𝙨𝙞𝙩𝙤")} -» <code>Payflow -» Auth</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.zu</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>
"""

text_gates_auth_2 = f"""
𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘼𝙪𝙩𝙝

{symbol("零 𝕃𝕪𝕟𝕩")} -» <code>Stripe[Ccn] -» Auth</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.lynx</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("零 𝙆𝙤𝙣𝙖𝙣")} -» <code>Stripe[Ccn] -» Auth</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ko</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘼𝙠𝙩𝙯")} -» <code>Stripe -» Auth</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ak</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("零 𝙋𝙞𝙘𝙘𝙤𝙡𝙤")} -» <code>Stripe[Ccn] -» Auth</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.pi</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("零 𝘼𝙨𝙩𝙝𝙖𝙧𝙤𝙩𝙝")} -» <code>Stripe[Ccn] -» Auth</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.at</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>
"""

buttons_auth_page_1 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 2", "auths_2")],
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
    ]
)

buttons_auth_page_2 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 1", "auths")],
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
    ]
)

# GATES CHARGED

text_gates_charged = f"""
𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘾𝙝𝙖𝙧𝙜𝙚𝙙

𝙋𝙖𝙜 -» <code>1</code>

{symbol("朱 𝙋𝙖𝙮𝙋𝙖𝙡")} -» <code>PayPal -» $0.01</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.pp</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙋𝙖𝙮𝙋𝙖𝙡")} -» <code>PayPal -» $1</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ppa</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝗔𝗱𝗿𝗶𝗮𝗻𝗮")} -» <code>Unk -» $3</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.adr</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙆𝙖𝙗𝙪𝙩𝙤")} -» <code>Braintree -» $3.99</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ka</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘼𝙨𝙨")} -» <code>fatZebra Vbv -» $4</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ass</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘿𝙟 𝘽𝙖𝙗𝙮")} -» <code>eWay -» $9.95</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.dj</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘿𝙚𝙫𝙞𝙡𝙨𝙭")} -» <code>UsaePay -» $10</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.dx</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙂𝙝𝙤𝙪𝙡")} -» <code>SquareUp -» $10</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.gh</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙋𝙚𝙥𝙚")} -» <code>Braintree -» $13.85</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.pe</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>
"""

text_gates_charged_2 = f"""
𝙋𝙖𝙜 -» <code>2</code>

{symbol("朱 𝙃𝙞𝙣𝙖𝙩𝙖")} -» <code>Checkout + Unk -» $20</code> 
{symbol("零 𝘾𝙢𝙙")} -» <code>.hn</code> -» <code>Premium</code> 
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝔻𝔸ℝ𝕜𝟜𝕀𝕋𝕆")} -» <code>Payflow -» $28.57</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.dkt</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘽𝙧𝙚𝙣𝙙𝙖 ")} -» <code>Onrally + Braintree -» $28.99</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.br</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝕤𝕖𝕓𝕒𝕤_𝟟𝕫")} -» <code>Payflow -» CA$39.99</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.sb</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙎𝙖𝙠𝙪𝙧𝙖")} -» <code>Shopify + Payflow[Code]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.su</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙆𝙖𝙧𝙞𝙣")} -» <code>Shopify + Braintree</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.kr</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙈𝙤𝙧𝙖")} -» <code>Shopify + Braintree</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.mo</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙐𝙘𝙝𝙞𝙝𝙖")} -» <code>Shopify + Braintree</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.uc</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙂𝙪𝙩")} -» <code>Shopify + Braintree</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.gu</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>
"""

text_gates_charged_3 = f"""𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘾𝙝𝙖𝙧𝙜𝙚𝙙

𝙋𝙖𝙜 -» <code>3</code>

{symbol("朱 𝙅𝙪𝙙𝙚")} -» <code>Shopify + Payflow</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ju</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙎𝙠𝙚𝙩𝙞𝙩")} -» <code>Shopify + Cybersource</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.st</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙆𝙮𝙪𝙨𝙪𝙠𝙚")} -» <code>Shopify + Cybersource</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ky</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘽𝙚𝙡𝙡𝙞𝙣𝙜𝙝𝙖𝙢")} -» <code>Shopify + Cybersource</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.bl</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘽𝙚𝙖𝙨𝙩𝙡𝙤𝙧𝙙")} -» <code>Shopify + Braintree</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.be</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙃𝙞𝙙𝙖𝙣")} -» <code>Shopify + Braintree</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.hi</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙎𝙖𝙣𝙞𝙣")} -» <code>Shopify + Braintree</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.sn</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘼𝙨𝙪𝙢𝙖")} -» <code>Shopify + Braintree</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.as</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙎𝙖𝙞𝙠𝙚𝙣")} -» <code>Shopify + Cybersource</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.si</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>
"""

text_gates_charged_4 = f"""𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘾𝙝𝙖𝙧𝙜𝙚𝙙

𝙋𝙖𝙜 -» <code>4</code>

<code>emptier than her love for you</code>
"""

text_gates_charged_5 = f"""𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘾𝙝𝙖𝙧𝙜𝙚𝙙

𝙋𝙖𝙜 -» <code>5</code>

<code>emptier than her love for you</code>
"""

buttons_charged_page_1 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 2", "chargeds_2")],
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
    ]
)

buttons_charged_page_2 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 1", "chargeds")],
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 3", "chargeds_3")],
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
    ]
)

buttons_charged_page_3 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 1", "chargeds")],
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 2", "chargeds_2")],
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 4", "chargeds_4")],
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
    ]
)

buttons_charged_page_4 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 1", "chargeds")],
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 2", "chargeds_2")],
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 3", "chargeds_3")],
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 5", "chargeds_5")],
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
    ]
)

buttons_charged_page_5 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 1", "chargeds")],
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 2", "chargeds_2")],
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 3", "chargeds_3")],
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 4", "chargeds_4")],
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
    ]
)

# GATES SPECIALS
text_gates_especials = f"""𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝙎𝙥𝙚𝙘𝙞𝙖𝙡

𝙋𝙖𝙜 -» <code>1</code>

{symbol("朱 𝙑𝙗𝙫")} -» <code>Braintree Vbv</code> 
{symbol("零 𝘾𝙢𝙙")} -» <code>.vbv</code> -» <code>Premium</code> 
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙁𝙪𝙘𝙠𝙚𝙧")} -» <code>Braintree ¿? -» $0.01</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.fu</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>Off ❌</code>

{symbol("朱 𝙃𝙤𝙨𝙝𝙞𝙜𝙖𝙠𝙞")} -» <code>Stripe[Ccn] -» $1</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ho</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙊𝙧𝙤𝙘𝙝𝙞𝙢𝙖𝙧𝙪")} -» <code>Stripe[Ccn] -» $1</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.or</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘽𝙤𝙧𝙪𝙩𝙤")} -» <code>Stripe[Ccn] -» $26.29</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.bo</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 🎀𝐻𝒶𝓇𝓁𝑒𝓎 𝒬𝓊𝒾𝓃𝓃🎀")} -» <code>Shopify + PayEzzy[Ccn Charged]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.hq</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙠𝙚𝙠𝙠𝙚𝙞")} -» <code>Shopify + PayEzzy[Ccn Charged]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ke</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙃𝙖𝙠𝙪")} -» <code>Shopify + PayEzzy[Ccn Charged]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ha</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙕𝙖𝙗𝙪𝙯𝙖")} -» <code>Shopify + Adyen[Ccn Live]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.za</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>
"""

text_gates_especials_2 = f"""
𝙋𝙖𝙜 -» <code>2</code>

{symbol("朱 𝙊𝙗𝙞𝙩𝙤")} -» <code>Shopify + Braintree[Ccn Live v2]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ob</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙎𝙖𝙨𝙤𝙧𝙞")} -» <code>Shopify + PayPal[Amex]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.sa</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙅𝙪𝙩𝙨𝙪")} -» <code>Shopify + PayPal[Amex]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ju</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙊𝙯𝙯𝙮")} -» <code>Shopify + Eway[Ccn]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.oz</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘾𝙝𝙧𝙤𝙣𝙞𝙘")} -» <code>Shopify + PayEzzy[Ccn Charged]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ch</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙑𝙚𝙜𝙚𝙩𝙖")} -» <code>Shopify + Payflow[Ccn Live v3]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ve</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘿𝙚𝙞𝙙𝙖𝙧𝙖")} -» <code>Shopify[Ccn Charged]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.de</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙍𝙞𝙣𝙚𝙜𝙖𝙣")} -» <code>Shopify [Ccn Charged]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ri</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙇𝙚𝙡𝙤𝙪𝙘𝙝 𝙇𝙖𝙢𝙥𝙚𝙧𝙤𝙪𝙜𝙚")} -» <code>Shopify + Braintree[Ccn]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.le</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>
"""

text_gates_especials_3 = f"""

𝙋𝙖𝙜 -» <code>3</code>

{symbol("朱 𝘿𝙧𝙤𝙭𝙭")} -» <code>Shopify + Eway[Ccn]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.dr</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙈𝙞𝙣𝙖𝙩𝙤")} -» <code>Shopify + Braintree[Ccn live v3]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.mi</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙕𝙚𝙩𝙨𝙪")} -» <code>Shopify + Adyen[Ccn Charged]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ze</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙏𝙤𝙗𝙞")} -» <code>Shopify + Adyen[Ccn live]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.to</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘿𝙖𝙞𝙗𝙪𝙩𝙨𝙪")} -» <code>Shopify + Convergepay[Ccn live v?]</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.da</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>
"""

buttons_specials_page_1 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 2", "specials_2")],
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
    ]
)

buttons_specials_page_2 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 1", "specials")],
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 3", "specials_3")],
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
    ]
)

buttons_specials_page_3 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 1", "specials")],
        [InlineKeyboardButton("𝙋𝙖𝙜 -» 2", "specials_2")],
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
    ]
)

# TOOLS
text_tools = f"""
𝙏𝙤𝙤𝙡𝙨 🛠

{symbol("朱 𝙍𝙚𝙛𝙚")} -» <code>send review reference</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.refe -» reply message</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘽𝙞𝙣")} -» <code>info bin</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.bin</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘾𝙝𝙖𝙩 𝙂𝙋𝙏")} -» <code>ChatGPT</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.gpt hola</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘼𝙙𝙙𝙧𝙚𝙨𝙨")} -» <code>generate address</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.rnd us</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙎𝙠")} -» <code>info sk</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.sk</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙂𝘽𝙞𝙣")} -» <code>generate bins</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.gbin</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘾𝘾 𝙂𝙚𝙣")} -» <code>generate ccs</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.gen</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙄𝙣𝙛𝙤")} -» <code>info user</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.my</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙋𝙡𝙖𝙣")} -» <code>info plan user</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.plan</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙋𝙡𝙖𝙣𝙂")} -» <code>info plan group</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.plang</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>"""
