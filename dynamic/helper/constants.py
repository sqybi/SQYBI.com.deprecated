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
        u"""我并不是什么都知道，只是知道我所知道的事情。""",
        u"《化物语》"
    ),
    (
        u"""努力是不会背叛自己的，虽然梦想有时会背叛。 
努力不一定能实现梦想，但是曾经努力过的事实却足以安慰自己。""",
        u"《我的青春恋爱物语果然有问题》"
    ),
    (
        u"""人生在世何其痛苦，所以咖啡至少该甜一点。""",
        u"《我的青春恋爱物语果然有问题》"
    ),
    (
        u"""对于连最低限度的努力都不愿意的人。是没有资格羡慕有才能之人的。
无法成功的人，就是因为他们想象不到成功者到底积聚了多少努力。""",
        u"《我的青春恋爱物语果然有问题》"
    ),
    (
        u"""“太阳快落下去了，你们的孩子居然不害怕？”
“当然不害怕，她知道明天太阳还会升起来的。”""",
        u"《三体II·黑暗森林》"
    ),
    (
        u"""只要一个人独处就不会伤害到任何人，这是事实。因为跟他人在一起，才会伤害到别人。可是，有许多东西是必须跟他人在一起才能获得的。""",
        u"《恋爱随意链接》"
    ),
    (
        u"""所谓的实现梦想，实际上就意味着体味到自己梦想的乏味之处。""",
        u"《倾物语》"
    ),
    (
        u"""我讨厌的人，也会有他们自己的朋友。 
我讨厌的人，也会有喜欢着他们的人。
在没有认识到这个显而易见的事实之前，人大概是无法走出社会的。""",
        u"《花物语》"
    ),
    (
        u"""在这个世界上，你到底做了些什么，这倒无关紧要。要紧的是，你如何能够使人相信你做了些什么。""",
        u"《福尔摩斯全集》"
    ),
    (
        u"""没有人在遭受别人责难与训斥时，还能愉快起来，但我却从人们生气的怒容中看到比狮子、鳄鱼、巨龙更可怕的动物本性。
平时他们都将这些本性隐藏着，可一旦找到机会，就会像那些在草原上温文尔雅的牛，忽然甩动自己的尾巴抽死自己肚子上的牛虻。""",
        u"《人间失格》"
    ),
    (
        u"""胆小鬼连幸福都会害怕，碰到棉花都会受伤，有时甚至会被幸福所伤。""",
        u"《人间失格》"
    ),
    (
        u"""“我的生活很单调。我追逐鸡，人追逐我。所有的鸡都一个模样。所有的人也是。所以，我感到有点无聊。”
“但是，如果你驯养了我，我的生活将充满阳光。我将辨别出一种与众不同的脚步声。别的脚步声会让我钻入地下，而你的脚步声却会像音乐一样，把我从洞穴里召唤出来。”
“我不吃面包，小麦对我来说毫无用处。麦田也不会让我联想到任何事。这是很可悲的！”
“但是你长着金黄色头发。当你驯养我以后，这将是非常美妙的一件事！麦子的颜色也是金黄色的，它会让我想起你。而且我也将喜欢聆听风儿吹过麦田的声音……”""",
        u"《小王子》"
    ),
    (
        u"""一个人可以很天真简单的活下去，必是身边无数人用更大的代价守护而来的。""",
        u"《小王子》"
    ),
    (
        u"""所有的大人都曾经是小孩，虽然，只有少数的人记得。""",
        u"《小王子》"
    ),
    (
        u"""成人们对数字情有独钟。如果你为他们介绍一个朋友，他们从不会问你“他的嗓子怎么样？他爱玩什么游戏？他会采集蝴蝶标本嘛？”而是问“他几岁了？有多少个兄弟？体重多少？他的父亲挣多少钱？”他们认为知道了这些，就了解了这个人。""",
        u"《小王子》"
    ),
]

# Blog settings
blog_article_per_page = 5
blog_title = u"三千院大小姐的紫公馆"

# User page settings
user_recent_blog_article_count = 5
user_recent_blog_comment_count = 5