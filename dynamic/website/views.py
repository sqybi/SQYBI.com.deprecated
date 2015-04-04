# -*- coding: utf-8 -*-

from django.shortcuts import render
import random


def home(request):
    daily_quotes = [
        u"""
“大家都很正常地怀有着梦想呢……”<br/>
“没错没错，大家都在朝着梦想拼命奋斗呢。这就是所谓的活着哦。”<br/>
“梦想啊，目标啊之类的，根本用不着吧？”<br/>
“为什么总说这种冷峻无情的话呢！”<br/>
“因为你不觉得很奇怪吗，只有那些成天念叨着梦想的人，才看不清现实啦。”""",
        u"""
我从不认为这些年的青春被狗吃了，以我对狗的了解，他们才不会吃这么没营养的东西。""",
        u"""
人类一生中最绚烂的时刻，就是面对着失败的命运顽强抗争，最终彻底地失败。""",
    ]

    context = {
        "title": "Home | SQYBI.com",
        "app": "Home",
        "daily_quote": random.choice(daily_quotes)
    }

    return render(request, "website/index.html", context)
