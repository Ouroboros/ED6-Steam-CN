from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4130_2 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    ScpFunction(
        "Function_0_64",           # 00, 0
        "Function_1_65",           # 01, 1
        "Function_2_66",           # 02, 2
        "Function_3_28F",          # 03, 3
        "Function_4_4D3",          # 04, 4
        "Function_5_60B",          # 05, 5
        "Function_6_67B",          # 06, 6
        "Function_7_756",          # 07, 7
        "Function_8_75B",          # 08, 8
        "Function_9_DD6",          # 09, 9
        "Function_10_1590",        # 0A, 10
        "Function_11_1CC4",        # 0B, 11
        "Function_12_201A",        # 0C, 12
        "Function_13_2204",        # 0D, 13
        "Function_14_3DE9",        # 0E, 14
        "Function_15_432D",        # 0F, 15
        "Function_16_4332",        # 10, 16
        "Function_17_51D0",        # 11, 17
        "Function_18_5304",        # 12, 18
        "Function_19_5421",        # 13, 19
        "Function_20_54DB",        # 14, 20
        "Function_21_5639",        # 15, 21
        "Function_22_5960",        # 16, 22
        "Function_23_5DA7",        # 17, 23
        "Function_24_65C9",        # 18, 24
        "Function_25_65CE",        # 19, 25
        "Function_26_6E2D",        # 1A, 26
        "Function_27_6FE8",        # 1B, 27
        "Function_28_7849",        # 1C, 28
    )


    def Function_0_64(): pass

    label("Function_0_64")

    Return()

    # Function_0_64 end

    def Function_1_65(): pass

    label("Function_1_65")

    Return()

    # Function_1_65 end

    def Function_2_66(): pass

    label("Function_2_66")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8B")
    SetChrSubChip(0xFE, 2)
    Jump("loc_BC")

    label("loc_8B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A1")
    SetChrSubChip(0xFE, 1)
    Jump("loc_BC")

    label("loc_A1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B7")
    SetChrSubChip(0xFE, 0)
    Jump("loc_BC")

    label("loc_B7")

    SetChrSubChip(0xFE, 2)

    label("loc_BC")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_11F")

    ChrTalk(
        0x1F,
        (
            "#100F阿加特与卡西乌斯相比\x01",
            "虽然还有些不够成熟。\x02\x03",
            "但这回可多亏有他在啊。 \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_286")

    label("loc_11F")

    OP_A2(0x6F0)
    OP_A2(0x17)

    ChrTalk(
        0x1F,
        (
            "#104F哎呀呀，逃亡的生活\x01",
            "对于我这一把老骨头而言真是艰苦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F阿加特给你们添了不少乱吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#100F不，并非如此。\x02\x03",
            "他把我们照顾得非常好。\x01",
            "　\x02\x03",
            "#100F选择的逃走路线\x01",
            "也没有让我们不方便，\x01",
            "都是经过了细心考虑的。\x02\x03",
            "#104F阿加特这小子真是好得没话说啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#101F与卡西乌斯相比\x01",
            "虽然还有些不够成熟，\x01",
            "但这回可多亏有他在啊。 \x02",
        )
    )

    CloseMessageWindow()

    label("loc_286")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_2_66 end

    def Function_3_28F(): pass

    label("Function_3_28F")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B4")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2E5")

    label("loc_2B4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CA")
    SetChrSubChip(0xFE, 0)
    Jump("loc_2E5")

    label("loc_2CA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E0")
    SetChrSubChip(0xFE, 2)
    Jump("loc_2E5")

    label("loc_2E0")

    SetChrSubChip(0xFE, 1)

    label("loc_2E5")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_36F")

    ChrTalk(
        0x1E,
        (
            "#560F终于实现和爷爷一起\x01",
            "吃冰淇淋的愿望了。\x01",
            "　\x02\x03",
            "#562F本来还想和阿加特大哥哥\x01",
            "一起来这里吃的，\x01",
            "结果被他拒绝了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CA")

    label("loc_36F")

    OP_A2(0x16)
    OP_A2(0x6F1)

    ChrTalk(
        0x1E,
        (
            "#560F啊……\x01",
            "艾丝蒂尔姐姐和约修亚哥哥！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F提妲，\x01",
            "你好像很开心嘛。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#061F嘿嘿，\x01",
            "因为终于实现和爷爷一起\x01",
            "吃冰淇淋的愿望了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊～真不错呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#061F嗯！\x02\x03",
            "#064F本来还想和阿加特大哥哥\x01",
            "一起来这里吃的，\x01",
            "结果被他拒绝了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F要阿加特吃冰淇淋……\x01",
            "哈哈，被拒绝也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#562F呜呜……\x01",
            "冰淇淋很好吃的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CA")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_3_28F end

    def Function_4_4D3(): pass

    label("Function_4_4D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_518")

    ChrTalk(
        0x1D,
        (
            "#053F武术大会啊……\x02\x03",
            "的确是个一试身手的好机会。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_607")

    label("loc_518")

    OP_A2(0x15)
    OP_A2(0x6EE)

    ChrTalk(
        0x1D,
        (
            "#053F武术大会啊……\x02\x03",
            "的确是个一试身手的好机会。\x01",
            "　\x02\x03",
            "#050F而且那个『不动金』这次也参加了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F阿加特，\x01",
            "你明年也来参加如何呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#053F……哼，虽然是有兴趣，\x01",
            "但我可不想被别人看热闹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F真是一点都不老实的说法～\x02",
    )

    CloseMessageWindow()

    label("loc_607")

    TalkEnd(0xFE)
    Return()

    # Function_4_4D3 end

    def Function_5_60B(): pass

    label("Function_5_60B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "由特务兵来镇守王都，\x01",
            "王都守卫队却撤离了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是难以理解，\x01",
            "而且根本不知道\x01",
            "是谁下达的这个命令啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_60B end

    def Function_6_67B(): pass

    label("Function_6_67B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_6DC")

    ChrTalk(
        0xFE,
        (
            "对于最近发生的事情，\x01",
            "我们也是一头雾水。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之王都的正规军\x01",
            "基本上都撤离了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_752")

    label("loc_6DC")

    OP_A2(0x14)

    ChrTalk(
        0xFE,
        (
            "对于发生的事情，\x01",
            "我们也是一头雾水。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之王都的正规军\x01",
            "基本上都撤离了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "这么一来可如何是好啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_752")

    TalkEnd(0xFE)
    Return()

    # Function_6_67B end

    def Function_7_756(): pass

    label("Function_7_756")

    Call(2, 8)
    Return()

    # Function_7_756 end

    def Function_8_75B(): pass

    label("Function_8_75B")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_7F4")

    ChrTalk(
        0x1A,
        (
            "政变的发动人\x01",
            "竟然是那位理查德上校……\x01",
            "让我好震惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "不过，\x01",
            "能防范于未然实在是太好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "真的是应该要感谢\x01",
            "亲卫队和游击士们啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD2")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_843")

    ChrTalk(
        0x1A,
        "要发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "那些王都的守卫队士兵\x01",
            "已经匆忙地撤离了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD2")

    label("loc_843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_8E5")

    ChrTalk(
        0x1A,
        (
            "为了筹备庆典的取材，\x01",
            "大家都在忙着做准备……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "但说实话，\x01",
            "庆典到底会怎样啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "女王陛下那边目前也\x01",
            "没有任何公告发表，\x01",
            "而且还有传言说会中止。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD2")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_94F")

    ChrTalk(
        0x1A,
        (
            "武术大会的优胜者\x01",
            "好像是朵洛希认识的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "她呀，高兴过头了，\x01",
            "一边跳着舞一边跑回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD2")

    label("loc_94F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_A2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_9AE")

    ChrTalk(
        0x1A,
        (
            "一大早，\x01",
            "朵洛希就拿着照相机\x01",
            "跑到竞技场去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "我看她好像充满干劲呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2C")

    label("loc_9AE")

    OP_A2(0x12)

    ChrTalk(
        0x1A,
        (
            "早上好。\x01",
            "今天是武术大会总决赛的日子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "一大早，\x01",
            "朵洛希就拿着照相机\x01",
            "跑到竞技场去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "我看她好像充满干劲呢。\x02",
    )

    CloseMessageWindow()

    label("loc_A2C")

    Jump("loc_DD2")

    label("loc_A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_A89")

    ChrTalk(
        0x1A,
        (
            "最近，\x01",
            "王国军的人每天都会过来检查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "我们通讯社\x01",
            "并没有做什么坏事对吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD2")

    label("loc_A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_B8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_AE4")

    ChrTalk(
        0x1A,
        (
            "理查德上校\x01",
            "真是个很棒的男人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "我也好像去\x01",
            "对他进行采访取材呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8B")

    label("loc_AE4")

    OP_A2(0x12)

    ChrTalk(
        0x1A,
        (
            "理查德上校\x01",
            "真是个很棒的男人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "举止文雅，知识渊博，\x01",
            "风度翩翩，一表人才……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "我也好像去\x01",
            "对他进行采访取材呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "下次拜托奈尔\x01",
            "看看能不能带我去吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8B")

    Jump("loc_DD2")

    label("loc_B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BFF")

    ChrTalk(
        0x1A,
        (
            "刚才奈尔记者\x01",
            "从外面回来了。\x01",
            "感觉有好一阵子没见到他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "他这个人啊，\x01",
            "经常会突然失踪好几天呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD2")

    label("loc_BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_C8B")

    ChrTalk(
        0x1A,
        (
            "本社的记者们\x01",
            "白天外出取材，\x01",
            "经常不在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "奈尔记者更是\x01",
            "很少呆在通讯社里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "经常都无法和他取得联络，\x01",
            "真是麻烦啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD2")

    label("loc_C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_CF1")

    ChrTalk(
        0x1A,
        (
            "下班之后约朵洛希\x01",
            "一起去外面玩的计划又泡汤了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "别看她那个样子，\x01",
            "其实工作很忙的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD2")

    label("loc_CF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_DD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_D42")

    ChrTalk(
        0x1A,
        (
            "现在编辑室的人\x01",
            "都外出采访去了，\x01",
            "如果有什么事可以让我转告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD2")

    label("loc_D42")

    OP_A2(0x12)

    ChrTalk(
        0x1A,
        "欢迎来到利贝尔通讯社。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "一楼是接待处，二楼是编辑室，\x01",
            "三楼是器材室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "现在编辑室的人\x01",
            "都外出采访去了，\x01",
            "如果有什么事可以让我转告。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD2")

    TalkEnd(0x1A)
    Return()

    # Function_8_75B end

    def Function_9_DD6(): pass

    label("Function_9_DD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_E44")

    ChrTalk(
        0xFE,
        (
            "接下来就去\x01",
            "最近引起热门话题的\x01",
            "冰淇淋店进行取材吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天东街区的那个店铺\x01",
            "客人特别多啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_158C")

    label("loc_E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_F00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_E95")

    ChrTalk(
        0xFE,
        (
            "奈尔前辈他\x01",
            "被军队逮捕了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "幸亏我是\x01",
            "文化专栏的负责人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFD")

    label("loc_E95")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "奈尔前辈他\x01",
            "被军队逮捕了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我就知道\x01",
            "他迟早会落到如此下场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "幸亏我是\x01",
            "文化专栏的负责人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFD")

    Jump("loc_158C")

    label("loc_F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_F71")

    ChrTalk(
        0xFE,
        (
            "本打算去到柏斯的\x01",
            "『安特洛丝餐厅』取材的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么办啊……\x01",
            "只能写一篇别的报道来代替了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FF3")

    label("loc_F71")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "哇呀呀，\x01",
            "定期船停飞了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本打算去到柏斯的\x01",
            "『安特洛丝餐厅』取材的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么办啊……\x01",
            "只能写一篇别的报道来代替了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF3")

    Jump("loc_158C")

    label("loc_FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_111B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1072")

    ChrTalk(
        0xFE,
        (
            "取材的方式是\x01",
            "去美味的店品尝料理，\x01",
            "然后展示在文化专栏里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定要做出可以向\x01",
            "奈尔前辈炫耀的东西来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1118")

    label("loc_1072")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "这次就以现在热门的餐厅\x01",
            "为主题作一期特辑吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "取材的方式是\x01",
            "去美味的店品尝料理，\x01",
            "然后展示在文化专栏里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定要做出可以向\x01",
            "奈尔前辈炫耀的东西来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1118")

    Jump("loc_158C")

    label("loc_111B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_124E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1194")

    ChrTalk(
        0xFE,
        (
            "朵洛希虽说是个新人，\x01",
            "不过实力确实非常强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，让她进入我们通讯社的\x01",
            "总编的眼光更加令人佩服。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_124B")

    label("loc_1194")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "朵洛希虽说是个新人，\x01",
            "不过实力确实非常强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管是拍武术大会的照片，\x01",
            "还是料理的照片，\x01",
            "她总能选择最佳的角度去拍摄。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，让她进入我们通讯社的\x01",
            "总编的眼光更加令人佩服。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124B")

    Jump("loc_158C")

    label("loc_124E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_133D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_12AD")

    ChrTalk(
        0xFE,
        (
            "很多作家或者撰稿人\x01",
            "每逢截稿的时间临近\x01",
            "就会犯感冒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是让人头疼……\x02",
    )

    CloseMessageWindow()
    Jump("loc_133A")

    label("loc_12AD")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "很多作家或者撰稿人\x01",
            "每逢截稿的时间临近\x01",
            "就会犯感冒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可能是太过拼命，\x01",
            "结果把身体弄坏了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再或者就是装病，\x01",
            "总之很让人头疼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133A")

    Jump("loc_158C")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1437")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_13A2")

    ChrTalk(
        0xFE,
        (
            "唉唉，\x01",
            "我乘坐定期船去外地取原稿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "结果到了之后\x01",
            "才被作者告知还没有写好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1434")

    label("loc_13A2")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "唉唉，\x01",
            "我乘坐定期船去外地取原稿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "结果到了之后\x01",
            "才被作者告知还没有写好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果导力通信能够更加普及的话，\x01",
            "联络起来就会方便了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1434")

    Jump("loc_158C")

    label("loc_1437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1441")
    Jump("loc_158C")

    label("loc_1441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_149B")

    ChrTalk(
        0xFE,
        (
            "今天我要乘坐定期船\x01",
            "去外地取原稿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要早点做好准备\x01",
            "才不至于延误乘船……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_158C")

    label("loc_149B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1526")

    ChrTalk(
        0xFE,
        (
            "《利贝尔通讯》的文化专栏\x01",
            "是由我来担当编辑的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本专栏通常会刊登\x01",
            "连载小说和读者的意见，\x01",
            "也会对一些热门话题进行取材报道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_158C")

    label("loc_1526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_158C")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "如果不能快点取回作者的原稿，\x01",
            "我会被责骂的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奈尔和诺蒂亚\x01",
            "都要比总编严厉许多呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158C")

    TalkEnd(0xFE)
    Return()

    # Function_9_DD6 end

    def Function_10_1590(): pass

    label("Function_10_1590")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_15FE")

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "这次又麻烦奈尔帮我的忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "下次一定要让他教教我\x01",
            "怎么样才能弄到好新闻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC0")

    label("loc_15FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1624")

    ChrTalk(
        0xFE,
        "街上的情况很奇怪呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CC0")

    label("loc_1624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_16A6")

    ChrTalk(
        0xFE,
        (
            "奈尔从刚来杂志社的时候\x01",
            "就会做些让人目瞪口呆的事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过大概正因为如此，\x01",
            "才能抢在别人之前报道一些独家新闻吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC0")

    label("loc_16A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_17A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1703")

    ChrTalk(
        0xFE,
        (
            "那个狐狸眼睛的女上尉，\x01",
            "实在让人生气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管走到哪里\x01",
            "都要挖苦别人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179F")

    label("loc_1703")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "理查德上校是很不错，\x01",
            "但情报部和特务兵\x01",
            "那些家伙就不敢恭维了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特别是那个\x01",
            "长着狐狸眼睛的女上尉，\x01",
            "实在让人生气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管走到哪里\x01",
            "都要挖苦别人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179F")

    Jump("loc_1CC0")

    label("loc_17A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1816")

    ChrTalk(
        0xFE,
        (
            "呼呼，情报部的监视非常严，\x01",
            "取材也寸步难行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们这样做，\x01",
            "和当年埃雷波尼亚帝国的宪兵有什么区别。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC0")

    label("loc_1816")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1943")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_18A3")

    ChrTalk(
        0xFE,
        (
            "我和奈尔常常都会\x01",
            "围绕着杂志报道方针的问题\x01",
            "与总编极力争辩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总编总能以\x01",
            "一副笑脸哄着我们，\x01",
            "我们很吃他的怀柔政策呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1940")

    label("loc_18A3")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        "总编是一个不可思议的人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我和奈尔常常都会\x01",
            "围绕着杂志报道方针的问题\x01",
            "与总编极力争辩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总编总能以\x01",
            "一副笑脸哄着我们，\x01",
            "我们很吃他的怀柔政策呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1940")

    Jump("loc_1CC0")

    label("loc_1943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1A25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_19A4")

    ChrTalk(
        0xFE,
        (
            "直到今天早上\x01",
            "奈尔还在调查什么东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道是发现了什么\x01",
            "好的新闻线索？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A22")

    label("loc_19A4")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "直到今天早上\x01",
            "奈尔还在调查什么东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道是发现了什么\x01",
            "好的新闻线索？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～作为前辈，\x01",
            "我也不能就这样输给他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A22")

    Jump("loc_1CC0")

    label("loc_1A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A9F")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "大会今年改成了团体赛，\x01",
            "想拍摄好的确很困难啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可能的话，\x01",
            "真想找个好一点的摄影师\x01",
            "来替我拍摄啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC0")

    label("loc_1A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1B5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1AF3")

    ChrTalk(
        0xFE,
        (
            "利贝尔通讯正在准备\x01",
            "出版武术大会的特刊哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要努力取材啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B5B")

    label("loc_1AF3")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        "今天终于到大会的正式赛了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "利贝尔通讯正在准备\x01",
            "出版武术大会的特刊哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要努力取材啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1B5B")

    Jump("loc_1CC0")

    label("loc_1B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1C55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1BBF")

    ChrTalk(
        0xFE,
        (
            "还是老样子，\x01",
            "奈尔又是一去不复返。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚回来没多久，\x01",
            "就立刻又飞奔出去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C52")

    label("loc_1BBF")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "还是老样子，\x01",
            "奈尔又是一去不复返。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚回来没多久，\x01",
            "就立刻又飞奔出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他脸色不太健康\x01",
            "是因为吸烟的缘故，\x01",
            "但体力至少是常人的一倍。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C52")

    Jump("loc_1CC0")

    label("loc_1C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1CC0")

    ChrTalk(
        0xFE,
        (
            "啊，真是的，\x01",
            "再不快点，预选赛就要开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，器材带上了，\x01",
            "取材用的通行许可证也带上了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC0")

    TalkEnd(0xFE)
    Return()

    # Function_10_1590 end

    def Function_11_1CC4(): pass

    label("Function_11_1CC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1D38")

    ChrTalk(
        0xA,
        (
            "#151F听我说，\x01",
            "奈尔前辈都告诉我了～\x02\x03",
            "因为这次的报道，\x01",
            "前辈和我很有可能会获得\x01",
            "菲利策奖哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E83")

    label("loc_1D38")

    OP_A2(0xF)
    OP_A2(0x6F3)

    ChrTalk(
        0xA,
        (
            "#151F啊，是小艾你们啊～！\x02\x03",
            "#150F听我说，\x01",
            "奈尔前辈都告诉我了～\x02\x03",
            "因为这次的报道，\x01",
            "前辈和我很有可能会获得\x01",
            "菲利策奖哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F菲利策？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F在新闻、文学和音乐等领域\x01",
            "取得年度最佳成绩的人被授予的奖项。\x01",
            "　\x02\x03",
            "对于记者而言，\x01",
            "毫无疑问是最高荣誉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊～真不错呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#151F嘿嘿嘿，\x01",
            "这也是托小艾你们的福啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E83")

    Jump("loc_2016")

    label("loc_1E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1EC1")

    ChrTalk(
        0xA,
        (
            "#151F呜～哇！\x01",
            "奈尔前辈还活着，\x01",
            "真是太好了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2016")

    label("loc_1EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1F05")

    ChrTalk(
        0xA,
        (
            "#152F啊，拜托了～！\x01",
            "小艾～！\x02\x03",
            "一定要救救奈尔前辈～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2016")

    label("loc_1F05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1FD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1F5E")

    ChrTalk(
        0xA,
        (
            "#154F唔～…………\x01",
            "虽然总编让我去找奈尔前辈～……\x02\x03",
            "但上哪去找呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD0")

    label("loc_1F5E")

    OP_A2(0xF)

    ChrTalk(
        0xA,
        (
            "#151F呀，是小艾你们啊～\x02\x03",
            "恭喜你们获得优胜。\x01",
            "真是激动人心的比赛呢～\x02\x03",
            "我太兴奋了，\x01",
            "就咔嚓咔嚓地拍个不停呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FD0")

    Jump("loc_2016")

    label("loc_1FD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1FDD")
    Jump("loc_2016")

    label("loc_1FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1FE7")
    Jump("loc_2016")

    label("loc_1FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1FF1")
    Jump("loc_2016")

    label("loc_1FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1FFB")
    Jump("loc_2016")

    label("loc_1FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2005")
    Jump("loc_2016")

    label("loc_2005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_200F")
    Jump("loc_2016")

    label("loc_200F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2016")

    label("loc_2016")

    TalkEnd(0xFE)
    Return()

    # Function_11_1CC4 end

    def Function_12_201A(): pass

    label("Function_12_201A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_219F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_2097")

    ChrTalk(
        0xFE,
        (
            "#141F对于你们精彩表现的话题，\x01",
            "读者的反响尤为强烈呢。\x02\x03",
            "如果以后有什么有趣的消息，\x01",
            "还要靠你们提供了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219C")

    label("loc_2097")

    OP_A2(0xE)
    OP_A2(0x6F4)

    ChrTalk(
        0xFE,
        (
            "#141F哟，艾丝蒂尔、约修亚！\x01",
            "这次真是辛苦你们了。\x02\x03",
            "多亏了你们，\x01",
            "这次与政变相关的特刊简直卖疯了。\x02\x03",
            "对于你们精彩表现的话题，\x01",
            "读者的反响尤为强烈呢。\x02\x03",
            "虽然最后根据协会的意向，\x01",
            "没有刊登出你们的名字。\x02\x03",
            "#147F对了，如果以后有什么好的线索，\x01",
            "还要靠你们提供了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219C")

    Jump("loc_2200")

    label("loc_219F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_21A9")
    Jump("loc_2200")

    label("loc_21A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_21B3")
    Jump("loc_2200")

    label("loc_21B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_21BD")
    Jump("loc_2200")

    label("loc_21BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_21C7")
    Jump("loc_2200")

    label("loc_21C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_21D1")
    Jump("loc_2200")

    label("loc_21D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_21DB")
    Jump("loc_2200")

    label("loc_21DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_21E5")
    Jump("loc_2200")

    label("loc_21E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_21EF")
    Jump("loc_2200")

    label("loc_21EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_21F9")
    Jump("loc_2200")

    label("loc_21F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2200")

    label("loc_2200")

    TalkEnd(0xFE)
    Return()

    # Function_12_201A end

    def Function_13_2204(): pass

    label("Function_13_2204")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_234C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_228B")

    ChrTalk(
        0xFE,
        (
            "理查德上校的\x01",
            "政变报道特辑反响强烈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "转瞬之间销量就已经赶上了\x01",
            "理查德上校介绍特辑\x01",
            "和戴尔蒙市长被捕特辑了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2349")

    label("loc_228B")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "理查德上校的\x01",
            "政变报道特辑反响强烈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "转瞬之间销量就已经赶上了\x01",
            "理查德上校介绍特辑\x01",
            "和戴尔蒙市长被捕特辑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如此有冲击力的事件，\x01",
            "与报道有关的质问非常多，\x01",
            "回答起来也很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2349")

    Jump("loc_3DE5")

    label("loc_234C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2410")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_23AC")

    ChrTalk(
        0xFE,
        (
            "刚才协会发联络过来，\x01",
            "说在艾贝尔离宫找到奈尔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀～太好了太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_240D")

    label("loc_23AC")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "刚才游击士协会\x01",
            "发联络过来说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在艾贝尔离宫\x01",
            "找到奈尔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀～太好了太好了。\x02",
    )

    CloseMessageWindow()

    label("loc_240D")

    Jump("loc_3DE5")

    label("loc_2410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2437")

    ChrTalk(
        0xFE,
        (
            "奈尔的事\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DE5")

    label("loc_2437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2763")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_249D")

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "我正有事要找奈尔呢……\x01",
            "他跑到哪里去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "这几天都没有看到他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2760")

    label("loc_249D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_24FB")

    ChrTalk(
        0xFE,
        (
            "我正有事要找奈尔呢，\x01",
            "可这几天都没有看到他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，\x01",
            "这种事情早已经习惯了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2760")

    label("loc_24FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_2580")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "我正有事要找奈尔呢……\x01",
            "他跑到哪里去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "这几天都没有看到他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，\x01",
            "这种事情早已经习惯了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2760")

    label("loc_2580")

    OP_A2(0x67F)
    OP_A2(0xD)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对了，你们是来找奈尔的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也正有事要找他呢，\x01",
            "可这几天都没有看到他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，\x01",
            "这种事情早已经习惯了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2760")

    Jump("loc_3DE5")

    label("loc_2763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_27BF")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "朵洛希她今天也要去竞技场取材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "碰到她的话帮我打个招呼。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A0E")

    label("loc_27BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_2821")

    ChrTalk(
        0xFE,
        (
            "哟，今天是总决赛哦。\x01",
            "我会支持你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "朵洛希她今天也要去竞技场取材。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A0E")

    label("loc_2821")

    OP_A2(0x67F)
    OP_A2(0xD)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，今天你们\x01",
            "要进行武术大会的决赛了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的工作太忙，不能去竞技场了，\x01",
            "就在这里给你们加油吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，谢谢～\x02",
    )

    CloseMessageWindow()

    label("loc_2A0E")

    Jump("loc_3DE5")

    label("loc_2A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2A4F")

    ChrTalk(
        0xFE,
        (
            "哈哈哈，\x01",
            "我们社的记者人人都很有个性呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E22")

    label("loc_2A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2A93")

    ChrTalk(
        0xFE,
        (
            "我还想着\x01",
            "他难得会呆在杂志社里，\x01",
            "原来是在等你们啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E22")

    label("loc_2A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_2B26")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "我们社的记者\x01",
            "人人都很有个性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此，\x01",
            "每到讨论问题的时候\x01",
            "场面简直就像在吵架一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过许多优秀的文章\x01",
            "也是那样诞生的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E22")

    label("loc_2B26")

    OP_A2(0x67F)
    OP_A2(0xD)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们是来找奈尔的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_END)), "loc_2DA0")

    ChrTalk(
        0x101,
        (
            "#000F嗯，是啊。\x01",
            "我们刚和他见过面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是吗，我还想着\x01",
            "他难得会呆在杂志社里，\x01",
            "原来是在等你们啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～除了开会的日子，\x01",
            "能看到他简直是太稀罕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他平常一直都在外面\x01",
            "到处奔波寻找新闻素材。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E22")

    label("loc_2DA0")


    ChrTalk(
        0x101,
        (
            "#000F嗯，是啊。\x01",
            "今天我们和他约好了的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是这样啊，\x01",
            "他现在就在编辑室里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "编辑室在出版社的二层。\x01",
            "你们赶快去找他吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E22")

    Jump("loc_3DE5")

    label("loc_2E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_31AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2E90")

    ChrTalk(
        0xFE,
        (
            "最近，军队的情报部\x01",
            "要求对我们的报道进行审查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "军队本来应该\x01",
            "没有这样的权利才对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A9")

    label("loc_2E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2EE0")

    ChrTalk(
        0xFE,
        (
            "奈尔他啊，\x01",
            "好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A9")

    label("loc_2EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_2F99")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "自从女王陛下生病以来，\x01",
            "情报部的家伙们就经常来制造麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟然还蛮横无理地\x01",
            "要求对我们的报道进行审查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "利贝尔王国\x01",
            "保障国民的言论自由，\x01",
            "他们根本没有这样的权利。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A9")

    label("loc_2F99")

    OP_A2(0x67F)
    OP_A2(0xD)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们是来找奈尔的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F啊、这个嘛，\x01",
            "其实不是的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看起来，\x01",
            "他好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31A9")

    Jump("loc_3DE5")

    label("loc_31AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3522")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3226")

    ChrTalk(
        0xFE,
        (
            "我听记者们说了，\x01",
            "你们是参加武术大会的选手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奈尔知道以后，\x01",
            "说要去采访你们，\x01",
            "然后就跑出去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_351F")

    label("loc_3226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_328B")

    ChrTalk(
        0xFE,
        (
            "听说你们\x01",
            "是参加武术大会的选手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奈尔知道以后，\x01",
            "说要去采访你们，\x01",
            "然后就跑出去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_351F")

    label("loc_328B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_332B")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我听记者们说了。\x01",
            "你们是参加武术大会的选手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奈尔知道以后\x01",
            "说要去采访你们，\x01",
            "然后就跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们没有遇见他吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_351F")

    label("loc_332B")

    OP_A2(0x67F)
    OP_A2(0xD)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说你们\x01",
            "是参加武术大会的选手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奈尔知道以后\x01",
            "说要去采访你们，\x01",
            "然后就跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们没有遇见他吗？\x02",
    )

    CloseMessageWindow()

    label("loc_351F")

    Jump("loc_3DE5")

    label("loc_3522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3895")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3596")

    ChrTalk(
        0xFE,
        (
            "从今天开始\x01",
            "武术大会终于进入正式赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为要出特刊，\x01",
            "所以本社的记者们\x01",
            "一早就外出取材了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3892")

    label("loc_3596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_35E6")

    ChrTalk(
        0xFE,
        (
            "奈尔他啊，\x01",
            "好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3892")

    label("loc_35E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_368B")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "从今天开始\x01",
            "武术大会终于进入正式赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然不知道诞辰庆典会如何，\x01",
            "但肯定也会很热闹吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为要出特刊，\x01",
            "所以本社的记者们\x01",
            "一早就外出取材了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3892")

    label("loc_368B")

    OP_A2(0x67F)
    OP_A2(0xD)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们是来找奈尔的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F啊，其实不是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看起来，\x01",
            "他好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3892")

    Jump("loc_3DE5")

    label("loc_3895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3B7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_38EC")

    ChrTalk(
        0xFE,
        (
            "奈尔他啊，\x01",
            "好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B7B")

    label("loc_38EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_396B")

    ChrTalk(
        0xFE,
        (
            "虽然本刊刊登了\x01",
            "女王陛下身体欠佳的报道，\x01",
            "但这个消息确实缺乏可信度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "还是没有得到确凿的证明呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B7B")

    label("loc_396B")

    OP_A2(0x67F)
    OP_A2(0xD)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们是来找奈尔的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F啊、这个嘛，\x01",
            "其实不是的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看起来，\x01",
            "他好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B7B")

    Jump("loc_3DE5")

    label("loc_3B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3DE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3BD5")

    ChrTalk(
        0xFE,
        (
            "奈尔他啊，\x01",
            "好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DE5")

    label("loc_3BD5")

    OP_A2(0xD)
    OP_A2(0x67F)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们是来找奈尔的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F啊、这个嘛，\x01",
            "其实不是的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看起来，\x01",
            "他好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE5")

    TalkEnd(0xFE)
    Return()

    # Function_13_2204 end

    def Function_14_3DE9(): pass

    label("Function_14_3DE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3E76")

    ChrTalk(
        0xFE,
        (
            "连游击士和亲卫队\x01",
            "攻入城内的场面都有，\x01",
            "这部分报道相当有魄力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来《利贝尔通讯》的发行量\x01",
            "又要大幅上涨了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F19")

    label("loc_3E76")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "很久没有看到过\x01",
            "如此精彩的报道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "连游击士和亲卫队\x01",
            "攻入城内的场面都有，\x01",
            "这部分报道相当有魄力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来《利贝尔通讯》的发行量\x01",
            "又要大幅上涨了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F19")

    Jump("loc_4329")

    label("loc_3F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3F8B")

    ChrTalk(
        0xFE,
        (
            "这几天阅读了\x01",
            "很多书籍和新闻，\x01",
            "从中得到了不少启示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在我们看不见的地方，\x01",
            "似乎正有暗流涌动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4329")

    label("loc_3F8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3FF3")

    ChrTalk(
        0xFE,
        (
            "我觉得亲卫队的人们\x01",
            "虽然有些作风古板……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过那份自律和严谨\x01",
            "看上去就让人心情很愉快。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4329")

    label("loc_3FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4061")

    ChrTalk(
        0xFE,
        (
            "关于女王病情的详情，\x01",
            "现在也没有对外发表。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "陛下本人也没有作出声明，\x01",
            "我怀疑真的是生病了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4329")

    label("loc_4061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_409C")

    ChrTalk(
        0xFE,
        (
            "呼～驱赶早上的睡意，\x01",
            "还是喝杯咖啡最有效了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4329")

    label("loc_409C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_40D2")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "士兵为什么都那样\x01",
            "粗暴不知礼节呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4329")

    label("loc_40D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4123")

    ChrTalk(
        0xFE,
        "呼，书籍是心灵的养料啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要更加广泛地\x01",
            "阅读各方面的书籍呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4329")

    label("loc_4123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4183")

    ChrTalk(
        0xFE,
        (
            "这里的老板以前\x01",
            "是外交使节的一员呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他好像去过帝国、共和国\x01",
            "等等很多的国家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4329")

    label("loc_4183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4202")

    ChrTalk(
        0xFE,
        (
            "我是属于那种只要知道\x01",
            "比赛结果就满足了的类型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竞技场的人太多了，\x01",
            "与其到那里去，\x01",
            "还不如静静地在这里看看书。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4329")

    label("loc_4202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_42CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_425C")

    ChrTalk(
        0xFE,
        (
            "最近的《利贝尔通讯》\x01",
            "给人的感觉有些平淡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一点都不让人吃惊啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_42C9")

    label("loc_425C")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "最近《利贝尔通讯》\x01",
            "给人的感觉有些平淡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "基本上都是\x01",
            "普普通通的新闻……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一点都不让人吃惊啊。\x02",
    )

    CloseMessageWindow()

    label("loc_42C9")

    Jump("loc_4329")

    label("loc_42CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4329")

    ChrTalk(
        0xFE,
        "哎呀，这个地方很舒适嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这里一边喝咖啡\x01",
            "一边看书的话，\x01",
            "时间很快就过去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4329")

    TalkEnd(0xFE)
    Return()

    # Function_14_3DE9 end

    def Function_15_432D(): pass

    label("Function_15_432D")

    Call(2, 16)
    Return()

    # Function_15_432D end

    def Function_16_4332(): pass

    label("Function_16_4332")

    TalkBegin(0x16)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                # 0
            "买东西\x01",                              # 1
            "欢迎品尝「巨匠咖喱饭」1000米拉\x01",      # 2
            "离开\x01",                                # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43AF")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x62)
    OP_56(0x0)
    TalkEnd(0x16)
    Return()

    label("loc_43AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44AD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4478")
    SubMira(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "尝了尝\x07\x02",
            "巨匠咖喱饭\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x3E8)
    OP_31(0x1, 0xFD, 0x3E8)
    OP_31(0x2, 0xFD, 0x3E8)
    OP_31(0x3, 0xFD, 0x3E8)
    OP_31(0x4, 0xFD, 0x3E8)
    OP_31(0x5, 0xFD, 0x3E8)
    OP_31(0x6, 0xFD, 0x3E8)
    OP_31(0x7, 0xFD, 0x3E8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_446A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0xB)"), scpexpr(EXPR_END)), "loc_4442")
    Jump("loc_446A")

    label("loc_4442")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "巨匠咖喱饭\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_446A")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_449E")

    label("loc_4478")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_449E")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x16)
    Return()

    label("loc_44AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44C7")
    FadeToBright(300, 0)
    TalkEnd(0x16)
    Return()

    label("loc_44C7")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x212)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x213)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x214)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x215)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x216)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x217)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x218)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x219)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x21A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x21B)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x21C)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49B9")

    ChrTalk(
        0x16,
        "咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "……请问，\x01",
            "难道你们有全部的《红耀石》吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "哦哦，果然！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "每当有新的一卷出版，\x01",
            "我都想在第一时间去买来看，\x01",
            "可总是错过机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "现在总算完结了，\x01",
            "我想从头到尾好好读一遍……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "可是现在到处\x01",
            "都已经销售一空了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "客人……\x01",
            "请允许我提出一个无理的愿望。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "能不能把整套书\x01",
            "转让给我呢？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_46A3"),
        (1, "loc_46D0"),
        (SWITCH_DEFAULT, "loc_46F0"),
    )


    label("loc_46A3")

    OP_A2(0x6F7)

    ChrTalk(
        0x16,
        (
            "哦哦，是真的吗？\x01",
            "太感谢你们了！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F0")

    label("loc_46D0")


    ChrTalk(
        0x16,
        "是吗……那也没办法……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    label("loc_46F0")


    ChrTalk(
        0x16,
        (
            "我曾经作为外交使节\x01",
            "被派遣到东方各国。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "那个时候我买了不少\x01",
            "引以为豪的东方收藏品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "我就从其中拿出一样\x01",
            "作为书的还礼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "看起来客人们好像是游击士。\x01",
            "对了…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "那就从这两样武器中\x01",
            "选择一样你们喜欢的吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【太极棍】\x01",              # 0
            "【黑千鸟·白千鸟】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4832"),
        (1, "loc_489B"),
        (SWITCH_DEFAULT, "loc_4910"),
    )


    label("loc_4832")


    ChrTalk(
        0x101,
        "#001F那我就要这个吧。\x02",
    )

    CloseMessageWindow()
    OP_3E(0x11, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "太极棍\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_4910")

    label("loc_489B")


    ChrTalk(
        0x102,
        "#010F那么，我就选这个吧。\x02",
    )

    CloseMessageWindow()
    OP_3E(0x30, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "黑千鸟·白千鸟\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_4910")

    label("loc_4910")


    ChrTalk(
        0x16,
        "哦哦，这个真是很适合你啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "我打算从今天起\x01",
            "早点关店停止营业，\x01",
            "一口气把小说读完。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "非常感谢你们。\x02",
    )

    CloseMessageWindow()
    OP_3F(0x212, 1)
    OP_3F(0x213, 1)
    OP_3F(0x214, 1)
    OP_3F(0x215, 1)
    OP_3F(0x216, 1)
    OP_3F(0x217, 1)
    OP_3F(0x218, 1)
    OP_3F(0x219, 1)
    OP_3F(0x21A, 1)
    OP_3F(0x21B, 1)
    OP_3F(0x21C, 1)
    TalkEnd(0x16)
    Return()

    label("loc_49B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4A41")

    ChrTalk(
        0x16,
        (
            "唉，\x01",
            "没想到表面上是在召开武术大会，\x01",
            "暗地里却是在策划政变。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "话说回来，\x01",
            "像理查德上校这样的人\x01",
            "怎么还会感到不满足呢。 \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51CC")

    label("loc_4A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4B3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4AAA")

    ChrTalk(
        0x16,
        (
            "我感到军队的警戒\x01",
            "好像又提高了一个层次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "这件事事先也没有\x01",
            "向我们市民通知一声。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3C")

    label("loc_4AAA")

    OP_A2(0xA)

    ChrTalk(
        0x16,
        (
            "王国军撤离之后，\x01",
            "街上到处都有黑衣士兵在警戒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "这件事事先也没有\x01",
            "向我们市民通知一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "虽然没有发生什么事情，\x01",
            "但总是觉得有些不安。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B3C")

    Jump("loc_51CC")

    label("loc_4B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4BA8")

    ChrTalk(
        0x16,
        (
            "刚才来的特务兵\x01",
            "嘴里嘟囔个不停……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "对于搜捕亲卫队的事，\x01",
            "市民好像不是很配合呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C36")

    label("loc_4BA8")

    OP_A2(0xA)

    ChrTalk(
        0x16,
        (
            "刚才来的特务兵\x01",
            "嘴里嘟囔个不停……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "对于搜捕亲卫队的事，\x01",
            "市民好像不是很配合呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "呵呵，主要还是因为\x01",
            "亲卫队平时很受大家欢迎吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C36")

    Jump("loc_51CC")

    label("loc_4C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4CA3")

    ChrTalk(
        0x16,
        (
            "武术大会的优胜者\x01",
            "好像已经产生了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "王城里的利贝尔宫廷料理\x01",
            "可都是十分丰盛的，好羡慕呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51CC")

    label("loc_4CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4D58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4CE9")

    ChrTalk(
        0x16,
        (
            "各位客人要不要尝尝\x01",
            "本店引以为荣的『浓缩咖啡』？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D55")

    label("loc_4CE9")

    OP_A2(0xA)

    ChrTalk(
        0x16,
        "你们好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "各位客人要不要尝尝\x01",
            "本店引以为荣的『浓缩咖啡』？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "对解除睡意非常有效哦。\x02",
    )

    CloseMessageWindow()

    label("loc_4D55")

    Jump("loc_51CC")

    label("loc_4D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4DCE")

    ChrTalk(
        0x16,
        (
            "刚才来的士兵说什么\x01",
            "晚上９点以后严禁外出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "没办法，\x01",
            "还是早些关店门，\x01",
            "一边听音乐一边看书吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E55")

    label("loc_4DCE")

    OP_A2(0xA)

    ChrTalk(
        0x16,
        (
            "刚才，\x01",
            "王国军的士兵们到店里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "他们说什么\x01",
            "晚上９点以后严禁外出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "没办法，\x01",
            "还是早些关店门，\x01",
            "一边听音乐一边看书吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E55")

    Jump("loc_51CC")

    label("loc_4E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4F34")

    ChrTalk(
        0x16,
        (
            "这个西街区，\x01",
            "在王都格兰赛尔的街区当中\x01",
            "也算是相当安静的区域了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "为了要开这家店，\x01",
            "我曾经到处寻找地方，\x01",
            "最后发现还是这里最好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "或许是在城里工作久了，\x01",
            "比起喧闹的场所，\x01",
            "我还是偏爱温馨和平静的角落。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51CC")

    label("loc_4F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5056")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4FB5")

    ChrTalk(
        0x16,
        (
            "我过去因为工作的关系\x01",
            "到过好多的国家呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "当时可以说\x01",
            "吃遍了各国的美味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "呵呵，饮食文化真是深奥啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5053")

    label("loc_4FB5")

    OP_A2(0xA)

    ChrTalk(
        0x16,
        (
            "哎呀，我过去因为工作的关系\x01",
            "去过好多的国家呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "当时可以说\x01",
            "吃遍了各国的美味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "这里卖的咖喱饭\x01",
            "就是其中一种哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "呵呵，饮食文化真是深奥啊。\x02",
    )

    CloseMessageWindow()

    label("loc_5053")

    Jump("loc_51CC")

    label("loc_5056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_50C6")

    ChrTalk(
        0x16,
        "哟，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "本店会让顾客\x01",
            "享受到宾至如归\x01",
            "而又舒适悠闲的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "各位不要有任何拘束感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_51CC")

    label("loc_50C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5140")

    ChrTalk(
        0x16,
        (
            "旁边的建筑就是现在大受欢迎的\x01",
            "《利贝尔通讯》的出版社办公楼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "那里的记者和编辑\x01",
            "也常到这里来吃饭休息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51CC")

    label("loc_5140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_51CC")

    ChrTalk(
        0x16,
        (
            "你们，欢迎光临。\x01",
            "这里是巴拉尔咖啡厅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "只要是与咖啡有关的，\x01",
            "这里可以满足你们的各种需要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "请你们放松心情，\x01",
            "好好享用吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51CC")

    TalkEnd(0x16)
    Return()

    # Function_16_4332 end

    def Function_17_51D0(): pass

    label("Function_17_51D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_51DD")
    Jump("loc_5300")

    label("loc_51DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5233")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "那么一会儿去吃冰淇淋如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我知道有一家店的\x01",
            "冰淇淋很好吃哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5300")

    label("loc_5233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_525F")

    ChrTalk(
        0xFE,
        "诞辰庆典之前都没什么事做呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_5300")

    label("loc_525F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_52BD")

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "我觉得明年肯定会变回个人战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样的话～\x01",
            "我只给约修亚君一个人加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5300")

    label("loc_52BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_52C7")
    Jump("loc_5300")

    label("loc_52C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_52D1")
    Jump("loc_5300")

    label("loc_52D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_52DB")
    Jump("loc_5300")

    label("loc_52DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_52E5")
    Jump("loc_5300")

    label("loc_52E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_52EF")
    Jump("loc_5300")

    label("loc_52EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_52F9")
    Jump("loc_5300")

    label("loc_52F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5300")

    label("loc_5300")

    TalkEnd(0xFE)
    Return()

    # Function_17_51D0 end

    def Function_18_5304(): pass

    label("Function_18_5304")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5311")
    Jump("loc_541D")

    label("loc_5311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5349")

    ChrTalk(
        0xFE,
        "超级不爽啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在要做些什么好呢～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_541D")

    label("loc_5349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_53AD")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "诞辰庆典真的会如期举办吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我刚才去打听了一下～\x01",
            "女王陛下似乎病了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_541D")

    label("loc_53AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_53DA")

    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "洛伦斯大人竟然输掉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_541D")

    label("loc_53DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_53E4")
    Jump("loc_541D")

    label("loc_53E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_53EE")
    Jump("loc_541D")

    label("loc_53EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_53F8")
    Jump("loc_541D")

    label("loc_53F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5402")
    Jump("loc_541D")

    label("loc_5402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_540C")
    Jump("loc_541D")

    label("loc_540C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5416")
    Jump("loc_541D")

    label("loc_5416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_541D")

    label("loc_541D")

    TalkEnd(0xFE)
    Return()

    # Function_18_5304 end

    def Function_19_5421(): pass

    label("Function_19_5421")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_542E")
    Jump("loc_54D7")

    label("loc_542E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5438")
    Jump("loc_54D7")

    label("loc_5438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5442")
    Jump("loc_54D7")

    label("loc_5442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5494")

    ChrTalk(
        0xFE,
        (
            "金小组，\x01",
            "优胜万岁！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最后的最后，\x01",
            "还是我支持的队伍取得了胜利！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54D7")

    label("loc_5494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_549E")
    Jump("loc_54D7")

    label("loc_549E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_54A8")
    Jump("loc_54D7")

    label("loc_54A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_54B2")
    Jump("loc_54D7")

    label("loc_54B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_54BC")
    Jump("loc_54D7")

    label("loc_54BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_54C6")
    Jump("loc_54D7")

    label("loc_54C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_54D0")
    Jump("loc_54D7")

    label("loc_54D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_54D7")

    label("loc_54D7")

    TalkEnd(0xFE)
    Return()

    # Function_19_5421 end

    def Function_20_54DB(): pass

    label("Function_20_54DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_54E8")
    Jump("loc_5635")

    label("loc_54E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_54F2")
    Jump("loc_5635")

    label("loc_54F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_54FC")
    Jump("loc_5635")

    label("loc_54FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_55F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5569")

    ChrTalk(
        0xFE,
        (
            "因为我和他都支持同一个小组，\x01",
            "所以很合得来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比赛结束之后\x01",
            "我们就来这里一起喝酒了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55EF")

    label("loc_5569")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "因为我和他都支持同一个小组，\x01",
            "所以很合得来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比赛结束之后\x01",
            "我们就来这里一起喝酒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天肯定也会彻夜狂欢吧。\x01",
            "哈哈哈～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55EF")

    Jump("loc_5635")

    label("loc_55F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_55FC")
    Jump("loc_5635")

    label("loc_55FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5606")
    Jump("loc_5635")

    label("loc_5606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5610")
    Jump("loc_5635")

    label("loc_5610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_561A")
    Jump("loc_5635")

    label("loc_561A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5624")
    Jump("loc_5635")

    label("loc_5624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_562E")
    Jump("loc_5635")

    label("loc_562E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5635")

    label("loc_5635")

    TalkEnd(0xFE)
    Return()

    # Function_20_54DB end

    def Function_21_5639(): pass

    label("Function_21_5639")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5646")
    Jump("loc_595C")

    label("loc_5646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5650")
    Jump("loc_595C")

    label("loc_5650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_565A")
    Jump("loc_595C")

    label("loc_565A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5664")
    Jump("loc_595C")

    label("loc_5664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_566E")
    Jump("loc_595C")

    label("loc_566E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_57C7")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5697")
    SetChrSubChip(0xFE, 0)
    Jump("loc_56C8")

    label("loc_5697")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56AD")
    SetChrSubChip(0xFE, 2)
    Jump("loc_56C8")

    label("loc_56AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56C3")
    SetChrSubChip(0xFE, 1)
    Jump("loc_56C8")

    label("loc_56C3")

    SetChrSubChip(0xFE, 0)

    label("loc_56C8")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5746")

    ChrTalk(
        0xFE,
        (
            "#037F哎呀，\x01",
            "和雪拉君可不是在这样的\x01",
            "节奏和气氛下喝酒呢。\x02\x03",
            "和她喝酒的时候，\x01",
            "总有一种欲生欲死的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57BF")

    label("loc_5746")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "#037F哈·哈·哈！\x02\x03",
            "哎呀～\x01",
            "和雪拉君可不是在这样的\x01",
            "节奏和气氛下喝酒呢。\x02\x03",
            "和她喝酒的时候，\x01",
            "总有一种欲生欲死的感觉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57BF")

    SetChrSubChip(0xFE, 0)
    Jump("loc_595C")

    label("loc_57C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_57D1")
    Jump("loc_595C")

    label("loc_57D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5909")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57FA")
    SetChrSubChip(0xFE, 0)
    Jump("loc_582B")

    label("loc_57FA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5810")
    SetChrSubChip(0xFE, 2)
    Jump("loc_582B")

    label("loc_5810")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5826")
    SetChrSubChip(0xFE, 1)
    Jump("loc_582B")

    label("loc_5826")

    SetChrSubChip(0xFE, 0)

    label("loc_582B")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5890")

    ChrTalk(
        0xFE,
        (
            "#037F呵，食物可以滋润心灵，\x01",
            "创造生命……\x02\x03",
            "哎呀呀，\x01",
            "厨师真是伟大的存在啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5901")

    label("loc_5890")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "#037F哈·哈·哈，\x01",
            "夜幕降临了。\x02\x03",
            "来吧，继续畅饮吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F奥利维尔明明这么瘦，\x01",
            "为什么能装下那么多……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5901")

    SetChrSubChip(0xFE, 0)
    Jump("loc_595C")

    label("loc_5909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5913")
    Jump("loc_595C")

    label("loc_5913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5955")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_5952")

    ChrTalk(
        0xFE,
        (
            "#038F唔、嗯……\x02\x03",
            "青春诚短暂，恋爱吧少女……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5952")

    Jump("loc_595C")

    label("loc_5955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_595C")

    label("loc_595C")

    TalkEnd(0xFE)
    Return()

    # Function_21_5639 end

    def Function_22_5960(): pass

    label("Function_22_5960")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5985")
    SetChrSubChip(0xFE, 1)
    Jump("loc_59A0")

    label("loc_5985")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_599B")
    SetChrSubChip(0xFE, 0)
    Jump("loc_59A0")

    label("loc_599B")

    SetChrSubChip(0xFE, 2)

    label("loc_59A0")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5C28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5A14")

    ChrTalk(
        0x10,
        (
            "#070F我打算暂时留在这里。\x02\x03",
            "难得来到这里，\x01",
            "等和各位高手较量过之后\x01",
            "再回国也不迟嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C25")

    label("loc_5A14")

    OP_A2(0x4)
    OP_A2(0x6EF)

    ChrTalk(
        0x10,
        "#073F哟，是你们俩啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F金大哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F对了，\x01",
            "金大哥你接下来准备做什么呢？\x02\x03",
            "真的要回去共和国吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#070F不，\x01",
            "在共和国没有发生什么大事，\x01",
            "我准备在这儿呆一段时间。\x02\x03",
            "这个国家有几位\x01",
            "很著名的年轻游击士。\x02\x03",
            "#071F难得来一趟，\x01",
            "等和他们切磋了技艺之后\x01",
            "再回国也不迟嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F著名的游击士？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#074F是啊……\x01",
            "首先是对面的『重剑阿加特』，\x01",
            "然后是『银闪雪拉扎德』。\x02\x03",
            "而且……\x02\x03",
            "#070F一定得和你们俩也较量一下才行。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F哇，这真有些难为情啊……\x02\x03",
            "#006F不过，我很期待！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F到时候还要请您手下留情。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C25")

    Jump("loc_5D9E")

    label("loc_5C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5C32")
    Jump("loc_5D9E")

    label("loc_5C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5C3C")
    Jump("loc_5D9E")

    label("loc_5C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5C46")
    Jump("loc_5D9E")

    label("loc_5C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5C50")
    Jump("loc_5D9E")

    label("loc_5C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5C92")

    ChrTalk(
        0x10,
        (
            "#078F明天就是决赛了。\x02\x03",
            "记得多吃点，睡个好觉哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D9E")

    label("loc_5C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5C9C")
    Jump("loc_5D9E")

    label("loc_5C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5D83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5CD5")

    ChrTalk(
        0x10,
        (
            "#079F嗝，怎么样？\x01",
            "你们也来喝吧～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D80")

    label("loc_5CD5")

    OP_A2(0x4)

    ChrTalk(
        0x10,
        (
            "#079F哦哦～！\x01",
            "艾丝蒂尔、约修亚！\x02\x03",
            "怎么样？\x01",
            "你们也来喝吧～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F我们可是未成年人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#076F什么，不愿喝我的酒吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，\x01",
            "好像已经完全喝醉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D80")

    Jump("loc_5D9E")

    label("loc_5D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5D8D")
    Jump("loc_5D9E")

    label("loc_5D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5D97")
    Jump("loc_5D9E")

    label("loc_5D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5D9E")

    label("loc_5D9E")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_22_5960 end

    def Function_23_5DA7(): pass

    label("Function_23_5DA7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5EB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5E28")

    ChrTalk(
        0xFE,
        (
            "竟然是理查德上校\x01",
            "策动的这起政变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前接受杂志的访谈\x01",
            "说的那些了不起的话，\x01",
            "也只是表面文章而已吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EB0")

    label("loc_5E28")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "竟然是理查德上校\x01",
            "策动的这起政变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前接受杂志的访谈\x01",
            "说的那些了不起的话，\x01",
            "也只是表面文章而已吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一想到就觉得震惊。\x02",
    )

    CloseMessageWindow()

    label("loc_5EB0")

    Jump("loc_65C5")

    label("loc_5EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5F02")

    ChrTalk(
        0xFE,
        "街上全是黑衣士兵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么要把以往的\x01",
            "那些士兵们替换掉了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_5F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5F64")

    ChrTalk(
        0xFE,
        (
            "诞辰庆典马上就到了，\x01",
            "王城里面如果能快点\x01",
            "发布公告就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不要这样就中止啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_5F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5FDC")

    ChrTalk(
        0xFE,
        (
            "大会明明都结束了，\x01",
            "士兵的数量却一点也没有减少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女王陛下又身体欠佳，\x01",
            "最近怎么总是令人讨厌的消息啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_5FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_60CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_604F")

    ChrTalk(
        0xFE,
        (
            "昨天晚上满街都是士兵，\x01",
            "回家的时候被他们叫住了四次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道我的样子\x01",
            "真的像是一个坏人吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60CA")

    label("loc_604F")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "昨天晚上满街都是士兵，\x01",
            "回家的时候被他们叫住了四次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道我的样子\x01",
            "真的像是一个坏人吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是让人泄气啊。\x02",
    )

    CloseMessageWindow()

    label("loc_60CA")

    Jump("loc_65C5")

    label("loc_60CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_614E")

    ChrTalk(
        0xFE,
        (
            "自从《利贝尔通讯》刊登采访以来，\x01",
            "理查德上校的人气\x01",
            "最近一段时间急剧上升啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论男女老少，\x01",
            "支持他的人都很多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_614E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_61BA")

    ChrTalk(
        0xFE,
        (
            "虽然『巴拉尔』咖啡厅的\x01",
            "帝国风味早点也很不错……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但我更喜欢这个店里的\x01",
            "利贝尔风味的早餐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_61BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_62BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_622D")

    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "难道说造成柏斯混乱的空贼\x01",
            "也参加了比武大会吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他们不在监狱服役，这样好吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_62B9")

    label("loc_622D")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "难道说造成柏斯混乱的空贼\x01",
            "也参加了比武大会吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然他们的确很有实力，\x01",
            "比赛也很有意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但是不在监狱服役好吗……\x02",
    )

    CloseMessageWindow()

    label("loc_62B9")

    Jump("loc_65C5")

    label("loc_62BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_641B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6356")

    ChrTalk(
        0xFE,
        (
            "武术大会原本是军人用来\x01",
            "展示武技和进行演习的活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从现在的女王陛下继位以来，\x01",
            "就逐渐转变成普通民众\x01",
            "也可以参与的开放式比赛了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6418")

    label("loc_6356")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "武术大会原本是军人用来\x01",
            "展示武技和进行演习的活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从现在的女王陛下继位以来，\x01",
            "就逐渐转变成普通民众\x01",
            "也可以参与的开放式比赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从那个时候开始，\x01",
            "普通民众也可以\x01",
            "报名参加大会了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6418")

    Jump("loc_65C5")

    label("loc_641B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_644A")

    ChrTalk(
        0xFE,
        (
            "哎哟，吓得我\x01",
            "被通心粉给哽住了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_644A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_64B3")

    ChrTalk(
        0xFE,
        (
            "武术大会变更为团体赛，\x01",
            "这还是头一次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然是那个\x01",
            "差劲公爵出的主意，\x01",
            "不过也算挺有趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_64B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_65C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_651F")

    ChrTalk(
        0xFE,
        (
            "亲卫队因为有制造恐怖活动的嫌疑，\x01",
            "正在被王国军追捕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "最近这类事情还真是接连不断。\x02",
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_651F")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "亲卫队因为有制造恐怖活动的嫌疑，\x01",
            "正在被王国军追捕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "柏斯的空贼带来的混乱，\x01",
            "卢安的市长被捕事件，\x01",
            "蔡斯的导力停止现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "最近这类事情还真是接连不断。\x02",
    )

    CloseMessageWindow()

    label("loc_65C5")

    TalkEnd(0xFE)
    Return()

    # Function_23_5DA7 end

    def Function_24_65C9(): pass

    label("Function_24_65C9")

    Call(2, 25)
    Return()

    # Function_24_65C9 end

    def Function_25_65CE(): pass

    label("Function_25_65CE")

    TalkBegin(0xE)
    OP_A2(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_65DE")
    Jump("loc_65E8")

    label("loc_65DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_65E8")
    OP_A3(0x19)

    label("loc_65E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_6781")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                # 0
            "买东西\x01",                              # 1
            "欢迎品尝「劲霸浓鱼汤」1000米拉\x01",      # 2
            "离开\x01",                                # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6669")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x61)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_6669")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6767")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6732")
    SubMira(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "尝了尝\x07\x02",
            "劲霸浓鱼汤\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x3E8)
    OP_31(0x1, 0xFD, 0x3E8)
    OP_31(0x2, 0xFD, 0x3E8)
    OP_31(0x3, 0xFD, 0x3E8)
    OP_31(0x4, 0xFD, 0x3E8)
    OP_31(0x5, 0xFD, 0x3E8)
    OP_31(0x6, 0xFD, 0x3E8)
    OP_31(0x7, 0xFD, 0x3E8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6724")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x2)"), scpexpr(EXPR_END)), "loc_66FC")
    Jump("loc_6724")

    label("loc_66FC")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "劲霸浓鱼汤\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6724")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_6758")

    label("loc_6732")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_6758")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xE)
    Return()

    label("loc_6767")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6781")
    FadeToBright(300, 0)
    TalkEnd(0xE)
    Return()

    label("loc_6781")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6867")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_67D2")

    ChrTalk(
        0xE,
        (
            "虽然发生了许多事情，\x01",
            "但现在终于可以平静地生活了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6864")

    label("loc_67D2")

    OP_A2(0x2)

    ChrTalk(
        0xE,
        (
            "看到女王陛下健康的样子，\x01",
            "我就放心了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "亲卫队的嫌疑\x01",
            "也只是被人嫁祸了而已……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "虽然发生了许多事情，\x01",
            "但现在终于可以平静地生活了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6864")

    Jump("loc_6E29")

    label("loc_6867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_68DD")

    ChrTalk(
        0xE,
        (
            "这几位士兵好像也对\x01",
            "当前的状况不太清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过就算发生了什么事情，\x01",
            "也不会那么容易就让我们知晓的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E29")

    label("loc_68DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_695C")

    ChrTalk(
        0xE,
        (
            "武术大会虽然结束了，\x01",
            "但士兵的数量一点都不见减少啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "亲卫队的人策划了\x01",
            "这次的恐怖事件的说法\x01",
            "果然是真的吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E29")

    label("loc_695C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_69B7")

    ChrTalk(
        0xE,
        "今天奥利维尔先生没有来呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "听说他们取得了优胜，\x01",
            "本来想特地庆贺一下的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E29")

    label("loc_69B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6A26")

    ChrTalk(
        0xE,
        (
            "啊～\x01",
            "我也想去竞技场看比赛呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "干我们这种工作，\x01",
            "在别人在玩乐的时候，\x01",
            "自己却非要工作不可啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E29")

    label("loc_6A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6AB4")

    ChrTalk(
        0xE,
        (
            "刚才，\x01",
            "王国军的人来了，\x01",
            "告诉我说只能营业到晚上９点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "唉～\x01",
            "难得最近的生意那么好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "９点就关门的话，\x01",
            "酒廊就名不副实了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E29")

    label("loc_6AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6B2B")

    ChrTalk(
        0xE,
        (
            "奥利维尔先生，\x01",
            "你们今天要参加武术大会吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "我往年支持的亲卫队\x01",
            "今年不能来参加，\x01",
            "所以就给你们加油吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E29")

    label("loc_6B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6B70")

    ChrTalk(
        0xE,
        (
            "第一天的比赛\x01",
            "好像已经结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "结果究竟如何呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E29")

    label("loc_6B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6C8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6BB9")

    ChrTalk(
        0xE,
        "你们都是奥利维尔先生的朋友吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "比赛要加油哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C88")

    label("loc_6BB9")

    OP_A2(0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x104, 0)

    ChrTalk(
        0xE,
        (
            "哎呀，奥利维尔先生，\x01",
            "昨天撞到的头没事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哈·哈·哈，你看呢。\x02\x03",
            "#030F我那充满世间博爱的热烈心跳\x01",
            "将会持续到永恒的那一刻。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "嗯，看来是没问题了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 180, 400)

    label("loc_6C88")

    Jump("loc_6E29")

    label("loc_6C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_6D44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_6D08")

    ChrTalk(
        0xE,
        (
            "哎呀……仔细看看，\x01",
            "这不是经常在这里演奏的奥利维尔先生吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "又是因为对女性纠缠不休\x01",
            "而被打飞的吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D41")

    label("loc_6D08")


    ChrTalk(
        0xE,
        (
            "大会的预选赛好像已经结束了。\x01",
            "这里客人立刻多了起来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D41")

    Jump("loc_6E29")

    label("loc_6D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6DA1")

    ChrTalk(
        0xE,
        (
            "说亲卫队的人是\x01",
            "恐怖分子什么的，\x01",
            "我难以相信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "肯定是哪里搞错了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E29")

    label("loc_6DA1")

    OP_A2(0x2)

    ChrTalk(
        0xE,
        (
            "说亲卫队的人是\x01",
            "恐怖分子什么的，\x01",
            "我难以相信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "虽说他们很少到这里来，\x01",
            "但我知道他们都是很正直的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "肯定是哪里搞错了……\x02",
    )

    CloseMessageWindow()

    label("loc_6E29")

    TalkEnd(0xE)
    Return()

    # Function_25_65CE end

    def Function_26_6E2D(): pass

    label("Function_26_6E2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6FE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6EAB")

    ChrTalk(
        0xFE,
        (
            "#840F立下了那么多功绩，\x01",
            "你们俩现在已经是\x01",
            "优秀的正游击士了。\x02\x03",
            "不要就此满足，\x01",
            "要向更高的目标发起冲击。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FE4")

    label("loc_6EAB")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#840F哟，\x01",
            "这回的事件解决得不错啊。\x02\x03",
            "立下了那么多功绩，\x01",
            "你们俩现在已经是\x01",
            "优秀的正游击士了。\x02\x03",
            "不要就此满足，\x01",
            "要向更高的目标发起冲击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嘿嘿，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F克鲁茨大哥，\x01",
            "你的身体已经没什么大碍了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#841F啊，\x01",
            "你看看，棒得很啊。\x02\x03",
            "#845遗憾的是……\x01",
            "到底是谁消除了我的记忆，\x01",
            "我怎么也想不起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FE4")

    TalkEnd(0xFE)
    Return()

    # Function_26_6E2D end

    def Function_27_6FE8(): pass

    label("Function_27_6FE8")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73D4")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 4660, 0, 540, 90)
    SetChrPos(0x102, 4870, 0, -630, 45)
    SetChrPos(0x108, 3570, 0, 140, 90)
    SetChrSubChip(0xC, 0)
    TurnDirection(0xC, 0x108, 0)
    OP_A2(0x64A)
    OP_28(0x4B, 0x1, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_706F")
    OP_28(0x4B, 0x1, 0x100)

    label("loc_706F")

    OP_6D(5350, 0, 360, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#006F库拉茨大哥，终于找到你了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#820F哦……\x01",
            "优胜组出现了。\x02\x03",
            "晚宴后不是在城里住得好好的吗。\x01",
            "怎么这么快就回来了啊？\x02\x03",
            "想必一定是吃了\x01",
            "不少美味佳肴吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F的确是很美味……\x01",
            "不过美味的同时事情却是不简单啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#820F事情却是不简单？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们向库拉茨说明了\x01",
            "至今为止发生的事情和女王的委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xC,
        (
            "#822F…………………………\x01",
            "……喂喂，没搞错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F很遗憾，确实是真的。\x01",
            "　\x02\x03",
            "我可以用我的称号作为担保。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#824F『不动金』……\x02\x03",
            "你所担保的事情\x01",
            "肯定是勿庸置疑了……\x02\x03",
            "#823F好，我明白了，\x01",
            "让我也来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F谢谢你，库拉茨大哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F首先要召开作战会议，\x01",
            "请到游击士协会去吧。\x02\x03",
            "大家都会集中在那里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#822F明白了，待会儿见！\x02",
    )

    CloseMessageWindow()

    def lambda_732F():

        label("loc_732F")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_732F")

    QueueWorkItem2(0x101, 1, lambda_732F)

    def lambda_7340():

        label("loc_7340")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_7340")

    QueueWorkItem2(0x102, 1, lambda_7340)

    def lambda_7351():

        label("loc_7351")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_7351")

    QueueWorkItem2(0x108, 1, lambda_7351)
    OP_8E(0xC, 0x15FE, 0x0, 0xFFFFFA42, 0xFA0, 0x0)
    OP_8E(0xC, 0x758, 0x0, 0xFFFFFA38, 0xFA0, 0x0)
    OP_8E(0xC, 0x2C6, 0x0, 0xFFFFEA8E, 0xFA0, 0x0)

    def lambda_739E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_739E)
    OP_8E(0xC, 0x2C6, 0xFFFFFF06, 0xFFFFE2D2, 0xFA0, 0x0)
    SetChrFlags(0xC, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    EventEnd(0x0)
    Jump("loc_7845")

    label("loc_73D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_7595")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_742B")

    ChrTalk(
        0xFE,
        (
            "我们以后可能就要\x01",
            "#820F一起执行任务了啊。\x02\x03",
            "到时候还要多多关照哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7592")

    label("loc_742B")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "#821F哟，英雄们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F库拉茨大哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#821F你们两个干得真漂亮。\x01",
            "　\x02\x03",
            "竟然还只是准游击士，\x01",
            "简直不可思议啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿……\x02\x03",
            "#000F其实这是大家共同努力\x01",
            "所换回来的美好结果呢。\x02\x03",
            "#505F到了最后还是老爸出手相助的，\x01",
            "我们的本领还没到家啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#820F……说真的，\x01",
            "你们已经做得很好了。\x02\x03",
            "我们以后可能就要\x01",
            "一起执行任务了啊。\x02\x03",
            "到时候还要多多关照哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7592")

    Jump("loc_7845")

    label("loc_7595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_759F")
    Jump("loc_7845")

    label("loc_759F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_75A9")
    Jump("loc_7845")

    label("loc_75A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_7698")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_75FF")

    ChrTalk(
        0xFE,
        (
            "#821F咦？\x01",
            "那个金发的兄弟到哪里去了？\x02\x03",
            "他的枪法\x01",
            "有相当的水准呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7695")

    label("loc_75FF")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "#821F哦哦，\x01",
            "这不是优胜组的成员吗。\x02\x03",
            "今天的比赛，\x01",
            "我们都认真地观摩了。\x02\x03",
            "虽然说我们也想取得优胜，\x01",
            "不过这个冠军让你们拿了\x01",
            "我们一点也没觉得遗憾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7695")

    Jump("loc_7845")

    label("loc_7698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_76A2")
    Jump("loc_7845")

    label("loc_76A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_76AC")
    Jump("loc_7845")

    label("loc_76AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_76B6")
    Jump("loc_7845")

    label("loc_76B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_76C0")
    Jump("loc_7845")

    label("loc_76C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_7834")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_770D")

    ChrTalk(
        0xFE,
        (
            "就算是游击士，\x01",
            "也要保证良好的睡眠，\x01",
            "早饭也要吃好才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7831")

    label("loc_770D")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "哟，\x01",
            "你们也是来吃早饭的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，是库拉茨大哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算是游击士，\x01",
            "也要保证良好的睡眠，\x01",
            "早饭也要吃好才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们在协会的研修中也学了吧。\x01",
            "如果没有休息好，判断力和身体都会迟钝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哈哈，\x01",
            "艾丝蒂尔只有对这一点是完全理解的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F喂……\x01",
            "那个『只有』是什么意思。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7831")

    Jump("loc_7845")

    label("loc_7834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_783E")
    Jump("loc_7845")

    label("loc_783E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_7845")

    label("loc_7845")

    TalkEnd(0xC)
    Return()

    # Function_27_6FE8 end

    def Function_28_7849(): pass

    label("Function_28_7849")

    TalkBegin(0x20)

    ChrTalk(
        0xFE,
        "到底是怎么回事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是被马踢了一脚吗？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x20)
    Return()

    # Function_28_7849 end

    SaveToFile()

Try(main)
