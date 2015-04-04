# -*- coding: utf-8 -*-

"""
Settings for the whole website.

Administrator should modify these settings before deploy this web application to production environment,
for customization and security reasons.
"""

# Base string for salt generator
salt_base = "salt_base_string"

# Database settings
db_host = ""
db_name = "website_test"
db_user = "sqybi_test"
db_password = "000000"

# Django secret key
django_secret_key = '=erw^b=h7gqntcy%x%fqg*f%mj3hl8odxg7kp@h6hwu647blh$'

# Website alert
alert_level = None
alert_message = None

# Daily Quotes
daily_quotes = [
    u"""“大家都很正常地怀有着梦想呢……”<br/>
“没错没错，大家都在朝着梦想拼命奋斗呢。这就是所谓的活着哦。”<br/>
“梦想啊，目标啊之类的，根本用不着吧？”<br/>
“为什么总说这种冷峻无情的话呢！”<br/>
“因为你不觉得很奇怪吗，只有那些成天念叨着梦想的人，才看不清现实啦。”""",
    u"""我从不认为这些年的青春被狗吃了，以我对狗的了解，他们才不会吃这么没营养的东西。""",
    u"""人类一生中最绚烂的时刻，就是面对着失败的命运顽强抗争，最终彻底地失败。""",
]

# Blog settings
blog_article_per_page = 5