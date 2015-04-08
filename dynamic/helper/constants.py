# -*- coding: utf-8 -*-

import re

"""
Settings for the whole website.

Administrator should modify these settings before deploy this web application to production environment,
for customization and security reasons.
"""

# *********************
# * Dev/Prod settings *
# *********************
#
# Here are the Settings which should be different for dev and prod environments
# Remember to modify before move to production!!!
#

# Base string for salt generator
salt_base = "salt_base_string"

# Database settings
db_host = ""
db_name = "website_test"
db_user = "sqybi_test"
db_password = "000000"

# Django secret key
django_secret_key = "=erw^b=h7gqntcy%x%fqg*f%mj3hl8odxg7kp@h6hwu647blh$"

# Debug mode
IS_DEBUG_MODE = True


# ********************
# * Website Settings *
# ********************
#
# Customized settings for the website
#

# Encrypt round for password
# Warning: changes on this field may cause previous passwords unavailable!!!
password_encrypt_round = 10

# Password length limit
password_min_length = 6

# Cookie settings
cookie_max_age_in_days = 30
cookie_max_age_in_seconds = 60 * 60 * 24 * cookie_max_age_in_days

# Patterns
# Only '_' in user name will be converted to '-' in url, so please do not use other symbols such as '.' and ';'
user_name_pattern = re.compile(r"^[a-z0-9_]{3,20}$")

# Region and format settings
time_zone = "Asia/Shanghai"
language_code = "zh-cn"

# Website alert
alert_level = None
alert_message = None
ALERT_LEVELS = {
    "error": "danger",
    "warning": "warning",
    "info": "info",
}

# Daily Quotes
daily_quotes = [
    (
        u"""“大家都很正常地怀有着梦想呢……”<br/>
“没错没错，大家都在朝着梦想拼命奋斗呢。这就是所谓的活着哦。”<br/>
“梦想啊，目标啊之类的，根本用不着吧？”<br/>
“为什么总说这种冷峻无情的话呢！”<br/>
“因为你不觉得很奇怪吗，只有那些成天念叨着梦想的人，才看不清现实啦。”""",
        u"《白箱》"
    ),
    (
        u"""我从不认为这些年的青春被狗吃了，以我对狗的了解，他们才不会吃这么没营养的东西。""",
        u"sqybi"
    ),
    (
        u"""人类一生中最绚烂的时刻，就是面对着失败的命运顽强抗争，最终彻底地失败。""",
        u"sqybi"
    ),
    (
        u"""在虚构的故事中寻求真实感的人脑袋一定有问题。""",
        u"《凉宫春日的忧郁》"
    ),
    (
        u"""何でもは知らないわよ。知ってることだけ。""",
        u"《物语系列》"
    ),
]

# Blog settings
blog_article_per_page = 5
blog_title = u"三千院大小姐的紫公馆"

# User page settings
user_recent_blog_article_count = 5
user_recent_blog_comment_count = 5