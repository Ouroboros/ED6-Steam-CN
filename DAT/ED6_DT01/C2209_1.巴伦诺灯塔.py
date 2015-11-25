from ED6ScenarioHelper import *

def main():
    # 巴伦诺灯塔

    CreateScenaFile(
        FileName            = 'C2209_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C2200.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60031",
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
        "Function_0_66",           # 00, 0
        "Function_1_9D",           # 01, 1
        "Function_2_E7D",          # 02, 2
        "Function_3_1C8E",         # 03, 3
        "Function_4_1F43",         # 04, 4
        "Function_5_2713",         # 05, 5
        "Function_6_2C16",         # 06, 6
        "Function_7_332D",         # 07, 7
        "Function_8_4CFE",         # 08, 8
        "Function_9_4D10",         # 09, 9
        "Function_10_4D62",        # 0A, 10
        "Function_11_4DB4",        # 0B, 11
        "Function_12_4E06",        # 0C, 12
        "Function_13_4E0E",        # 0D, 13
        "Function_14_4E23",        # 0E, 14
        "Function_15_4E4C",        # 0F, 15
        "Function_16_4E75",        # 10, 16
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E")
    OP_A2(0x0)
    Call(1, 1)
    Jump("loc_95")

    label("loc_8E")

    OP_A2(0x0)
    Call(1, 2)

    label("loc_95")

    Jump("loc_9C")

    label("loc_98")

    Call(1, 4)

    label("loc_9C")

    Return()

    # Function_0_66 end

    def Function_1_9D(): pass

    label("Function_1_9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B2")
    Return()

    label("loc_B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E7C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_D6")
    Call(1, 2)
    Jump("loc_E7C")

    label("loc_D6")

    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0x9, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEF")
    OP_28(0x1C, 0x4, 0x2)
    OP_28(0x1C, 0x4, 0x4)
    OP_28(0x1C, 0x1, 0x1)
    OP_28(0x1C, 0x1, 0x2)
    OP_69(0x9, 0x7D0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E")
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "…………唉，\x01",
            "接下来应该怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果去叫人帮忙的话，\x01",
            "灯塔不就没人看守了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这么说只有在这里等着了……\x02",
    )

    CloseMessageWindow()

    label("loc_21E")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        "……哦，你们是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "到巴伦诺灯塔来有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没有啊，\x01",
            "并没有什么特别的事情。\x02\x03",
            "倒是老爷爷您，\x01",
            "在这里做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "我是这里的管理员，\x01",
            "也就是看守灯塔的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这个大型的灯塔\x01",
            "管理起来是很费力的…………\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_428")

    ChrTalk(
        0x8,
        "…………嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哎呀，你们俩，\x01",
            "胸前的徽章是…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#508F啊，没错，是的。\x02\x03",
            "我们是游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F准确地说\x01",
            "现在还只是准游击士。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542")

    label("loc_428")

    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "…………哦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "喂，年轻人。\x01",
            "你们胸前的徽章是…………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#007F呜…………\x01",
            "徽、徽章…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F（真是的……）\x02\x03",
            "#010F嗯，是啊。\x01",
            "我们是游击士。\x02\x03",
            "准确地说\x01",
            "现在还只是准游击士。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_542")

    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "啊，\x01",
            "为什么不早说！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "难道你们对一位老人\x01",
            "陷入如此的困境视而不见吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F啊！？\x02\x03",
            "困难什么的\x01",
            "您刚才一个字也没有提到啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "那是因为\x01",
            "你们刚才没有问过我啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "『您有什么困难吗？』\x01",
            "你们为什么不这样问问？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "真是的…………\x01",
            "年轻的游击士就只有力气，\x01",
            "一点观察能力都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "…………对了。\x01",
            "在这一点上，那个壮年的游击士\x01",
            "就表现得完全不一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那是……嗯，\x01",
            "大概七八年前的事情吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F喂喂，老爷爷？\x01",
            "您的困难究竟是什么啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "…………嗯？\x01",
            "啊，对了对了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是这样的，刚才我去割草的时候，\x01",
            "不小心忘了关门……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "一群魔兽\x01",
            "就趁机冲入了灯塔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这样一来\x01",
            "我也没有办法进去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F就是说，\x01",
            "只要把里面的魔兽全部消灭就行了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嗯，就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过我不知道里面究竟有多少只。\x01",
            "你们千万要小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯……不过魔兽\x01",
            "为什么要跑到灯塔里面去呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    TurnDirection(0x101, 0x102, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BFD")
    TurnDirection(0x105, 0x102, 400)
    Jump("loc_C11")

    label("loc_BFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C11")
    TurnDirection(0x136, 0x102, 400)

    label("loc_C11")


    ChrTalk(
        0x102,
        (
            "#010F我想可能是受到了七耀石吸引的缘故吧。\x01",
            "　\x02\x03",
            "因为灯塔使用的是\x01",
            "特大号的导力器。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "嗯，说得没错。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDB")
    TurnDirection(0x105, 0x8, 400)
    Jump("loc_CEF")

    label("loc_CDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CEF")
    TurnDirection(0x136, 0x8, 400)

    label("loc_CEF")


    ChrTalk(
        0x8,
        (
            "以前被侵入的时候，\x01",
            "那些魔兽都是集中在\x01",
            "灯塔的最上层。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        (
            "那么，\x01",
            "现在就可以进去消灭魔兽吧？\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 3)
    Jump("loc_E79")

    label("loc_DEF")

    OP_69(0x9, 0x3E8)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        (
            "怎么样，\x01",
            "可以进去消灭魔兽了吧？\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 3)

    label("loc_E79")

    TalkEnd(0x8)

    label("loc_E7C")

    Return()

    # Function_1_9D end

    def Function_2_E7D(): pass

    label("Function_2_E7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C8D")
    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0x9, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BFD")
    OP_28(0x1C, 0x4, 0x2)
    OP_28(0x1C, 0x4, 0x4)
    OP_28(0x1C, 0x1, 0x1)
    OP_28(0x1C, 0x1, 0x2)
    OP_28(0x1C, 0x1, 0x4)
    OP_28(0x1D, 0x1, 0x8)
    OP_28(0x1D, 0x1, 0x1000)
    OP_69(0x9, 0x7D0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE2")
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "…………唉，\x01",
            "接下来应该怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果去叫人帮忙的话，\x01",
            "灯塔不就没人看守了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这么说只有在这里等着了……\x02",
    )

    CloseMessageWindow()

    label("loc_FE2")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        "……哦，你们是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "到巴伦诺灯塔来有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F请问一下，\x01",
            "您是看守灯塔的弗科特爷爷吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "嗯？\x01",
            "正是本人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哎呀，你们俩，\x01",
            "胸前的徽章是…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#508F啊，没错，是的。\x02\x03",
            "我们是游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F准确地说\x01",
            "现在还只是准游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "啊，\x01",
            "为什么不早说！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "难道你们对一位老人\x01",
            "陷入如此的困境视而不见吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F啊！？\x02\x03",
            "困难什么的\x01",
            "您刚才一个字也没有提到啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "那是因为\x01",
            "你们刚才没有问过我啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "『您有什么困难吗？』\x01",
            "你们为什么不这样问问？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "真是的…………\x01",
            "年轻的游击士就只有力气，\x01",
            "一点观察能力都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "…………对了。\x01",
            "在这一点上，那个壮年的游击士\x01",
            "就表现得完全不一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那是……嗯，\x01",
            "大概七八年前的事情吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F喂喂，老爷爷？\x01",
            "您的困难究竟是什么啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F（呵呵，\x01",
            "　果然和工房老板说的一样。）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "…………嗯？\x01",
            "啊，对了对了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是这样的，刚才我去割草的时候，\x01",
            "不小心忘了关门……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "一群魔兽\x01",
            "就趁机冲入了灯塔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这样一来\x01",
            "我也没有办法进去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F……这样啊，\x01",
            "在把维修工具箱交给您之前\x01",
            "要先消灭魔兽对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F也只有这个选择了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "什么？\x01",
            "维修工具箱？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，我们接受了委托\x01",
            "从卢安把维修工具箱带给您。\x02\x03",
            "…………不然的话，\x01",
            "我们现在就不会在这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯，嗯嗯。\x01",
            "你们说得没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果进不了灯塔，\x01",
            "就连检查都没法进行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F您知道里面有多少魔兽吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "具体数目我也不太清楚，\x01",
            "不过肯定不止一只。\x01",
            "你们千万要小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F知道了。\x01",
            "就是说有很多只吧。\x02\x03",
            "#505F嗯……不过魔兽\x01",
            "为什么要跑到灯塔里面去呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    def lambda_1A2E():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A2E)

    def lambda_1A3C():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1A3C)

    ChrTalk(
        0x102,
        (
            "#010F我想可能是受到了七耀石吸引的缘故吧。\x01",
            "　\x02\x03",
            "因为灯塔使用的是\x01",
            "特大号的导力器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嗯，说得没错。\x02",
    )

    CloseMessageWindow()

    def lambda_1AE0():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1AE0)

    def lambda_1AEE():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AEE)

    def lambda_1AFC():
        TurnDirection(0x105, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1AFC)

    ChrTalk(
        0x8,
        (
            "以前被侵入的时候，\x01",
            "那些魔兽都是集中在\x01",
            "灯塔的最上层。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么，\x01",
            "现在就可以进去消灭魔兽吧？\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 3)
    Jump("loc_1C87")

    label("loc_1BFD")

    OP_69(0x9, 0x3E8)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        (
            "怎么样，\x01",
            "可以进去消灭魔兽了吧？\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 3)

    label("loc_1C87")

    TalkEnd(0x8)
    Jump("loc_1C8D")

    label("loc_1C8D")

    Return()

    # Function_2_E7D end

    def Function_3_1C8E(): pass

    label("Function_3_1C8E")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D00"),
        (1, "loc_1E5A"),
        (SWITCH_DEFAULT, "loc_1F36"),
    )


    label("loc_1D00")

    OP_28(0x1C, 0x4, 0x8)
    OP_28(0x1C, 0x1, 0x4)

    ChrTalk(
        0x101,
        "#006F嗯，没问题。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "就快到定期检查的时间了，\x01",
            "所以请尽量快一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那些魔兽很敏捷，\x01",
            "注意不要让他们逃掉啊。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F好。\x01",
            "那我们就进去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_21()
    NewScene("ED6_DT01/C2219   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1F36")

    label("loc_1E5A")


    ChrTalk(
        0x101,
        (
            "#505F对不起啊，\x01",
            "现在可能还不行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "很快就要到\x01",
            "定期检查的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "所以请你们\x01",
            "尽可能快一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F36")

    label("loc_1F36")

    EventEnd(0x1)
    TalkEnd(0x8)
    OP_8C(0x8, 0, 0)
    Return()

    # Function_3_1C8E end

    def Function_4_1F43(): pass

    label("Function_4_1F43")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_24C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_21A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2069")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "喂，我说小姑娘你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "魔兽消灭得怎么样了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#505F唔～\x01",
            "还需要一点时间呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "是这样吗……\x01",
            "你们得抓紧点儿才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果进不了灯塔，\x01",
            "我就无法进行定期检查呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A3")

    label("loc_2069")


    ChrTalk(
        0x8,
        (
            "什么？\x01",
            "难道说你们还要去别的地方吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我倒是不介意…………\x01",
            "不过要早点回来呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果进不了灯塔，\x01",
            "我就无法进行定期检查呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A3")

    Jump("loc_24C4")

    label("loc_21A6")

    OP_28(0x1D, 0x1, 0x1000)

    ChrTalk(
        0x8,
        "喂，我说小姑娘你们。   \x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "嗯…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦，那个大箱子是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，这是维修工具箱。\x02\x03",
            "给老爷爷您检查设备用的。\x01",
            "工具都在里面吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哦，果然如此。\x01",
            "原来已经到定期检查的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F刚好我们接到委托，\x01",
            "所以就马上把工具箱送来了……\x02\x03",
            "……可是眼下这种状况\x01",
            "想要进行设备检查也不行啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "嗯，嗯嗯。\x01",
            "你们说得没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果进不了灯塔，\x01",
            "想要检查都没办法进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F还是先得把魔兽消灭了才行啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，速战速决吧。\x01",
            "这种下去肯定是没法开工的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那就拜托你们了。\x02",
    )

    CloseMessageWindow()

    label("loc_24C4")

    Jump("loc_270F")

    label("loc_24C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D5")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "喂，我说小姑娘你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "魔兽消灭得怎么样了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#505F唔～\x01",
            "还需要一点时间呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0xFE,
        "唔～这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就快到定期检查的时间了，\x01",
            "你们得抓紧点儿才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270F")

    label("loc_25D5")


    ChrTalk(
        0x8,
        (
            "什么？\x01",
            "难道说你们还要去别的地方吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我倒是不介意…………\x01",
            "不过要早点回来呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "定期检查的时间就要到了。\x02",
    )

    CloseMessageWindow()

    label("loc_270F")

    TalkEnd(0x8)
    Return()

    # Function_4_1F43 end

    def Function_5_2713(): pass

    label("Function_5_2713")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_8C(0x8, 180, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2740")
    SetChrFlags(0x105, 0x80)
    Jump("loc_2752")

    label("loc_2740")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2752")
    SetChrFlags(0x136, 0x80)

    label("loc_2752")

    SetChrPos(0x101, -20, 750, 2830, 0)
    SetChrPos(0x102, -20, 750, 2830, 0)
    OP_6D(-20, 750, 830, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27A6")
    SetChrPos(0x105, -20, 750, 2830, 0)
    Jump("loc_27C4")

    label("loc_27A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27C4")
    SetChrPos(0x136, -20, 750, 2830, 0)

    label("loc_27C4")

    Sleep(2000)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0x8, 0, 400)
    Sleep(1200)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x50)
    OP_73(0x0)

    def lambda_27FE():

        label("loc_27FE")

        TurnDirection(0x8, 0x101, 0)
        OP_48()
        Jump("loc_27FE")

    QueueWorkItem2(0x8, 1, lambda_27FE)
    OP_43(0x9, 0x1, 0x1, 0x8)
    OP_43(0x101, 0x1, 0x1, 0x9)
    Sleep(500)
    OP_43(0x102, 0x1, 0x1, 0xA)
    Sleep(500)
    OP_43(0x105, 0x1, 0x1, 0xB)
    WaitChrThread(0x102, 0x1)
    Sleep(1000)
    OP_72(0x0, 0x800)
    OP_22(0xD3, 0x0, 0x64)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_44(0x8, 0xFF)

    ChrTalk(
        0x8,
        "哦，还算顺利吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F哈哈，已经全部解决了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F魔兽已经被消灭，\x01",
            "没问题了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "真的吗，太好了！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B12")
    OP_28(0x1D, 0x1, 0x1000)

    ChrTalk(
        0x8,
        (
            "哎呀，\x01",
            "这下可以放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呵呵，真的是这样呢。\x02\x03",
            "这下就可以\x01",
            "把维修工具箱交给您了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "什么？\x01",
            "维修工具箱？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F其实我们是接到委托\x01",
            "前来把工具箱送给您的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "哦哦，原来如此啊。\x01",
            "已经到定期检查的时候了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA3")

    label("loc_2B12")


    ChrTalk(
        0x8,
        (
            "哎呀，\x01",
            "这下终于可以\x01",
            "收下维修工具箱了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA3")


    ChrTalk(
        0x8,
        (
            "好的，\x01",
            "总之我们先进入灯塔里再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C2219   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_2713 end

    def Function_6_2C16(): pass

    label("Function_6_2C16")

    OP_28(0x1D, 0x4, 0x10)
    OP_28(0x1D, 0x1, 0x80)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrPos(0x101, 200, 750, 2830, 0)
    SetChrPos(0x102, -500, 750, 2830, 0)
    SetChrPos(0x105, 500, 750, 2830, 0)
    Sleep(2000)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x50)
    OP_73(0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)

    def lambda_2C95():
        OP_90(0x101, 0x0, 0x0, 0xFFFFDECC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C95)
    Sleep(500)

    def lambda_2CB5():
        OP_90(0x102, 0x0, 0x0, 0xFFFFE2B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CB5)
    Sleep(600)

    def lambda_2CD5():
        OP_90(0x105, 0x0, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2CD5)
    Sleep(1200)
    OP_72(0x0, 0x800)
    OP_22(0xD3, 0x0, 0x64)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_6D(200, 0, -4800, 3000)
    WaitChrThread(0x105, 0x1)

    ChrTalk(
        0x101,
        "#505F………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F…………喂，约修亚。\x01",
            "对刚才的话你怎么想？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F不用想也可以知道。\x02\x03",
            "如果是七八年前，\x01",
            "在时间上就很吻合了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#040F请问，难道说……\x02\x03",
            "刚才老爷爷提起的那位壮年游击士，\x01",
            "是你们认识的人吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#505F唔～\x01",
            "说认识是理所当然的啦……\x02\x03",
            "因为那就是我们的老爸嘛。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044F啊………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F……不过，\x01",
            "想要和父亲相比的确很难啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F呼，真不甘心。\x02\x03",
            "如果是拿其他的游击士和我们做对比，\x01",
            "那个老爷爷就不会有这种抱怨了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F只要我们每天都努力加油，\x01",
            "一定可以赶上父亲的。\x02\x03",
            "…………不能因为对手太强而灰心丧气哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F哈哈哈，说的也是。\x02\x03",
            "#006F不过我也坚信，\x01",
            "总有一天我们可以超越他。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#041F呵呵，\x01",
            "这样才像艾丝蒂尔嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，谢谢。\x02\x03",
            "就这么决定了。\x01",
            "我们绝对不会偷懒的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，对啊。\x02\x03",
            "那我们出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【扫荡灯塔的魔兽】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【运送维修工具箱】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_6_2C16 end

    def Function_7_332D(): pass

    label("Function_7_332D")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_8C(0x8, 180, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_335A")
    SetChrFlags(0x105, 0x80)
    Jump("loc_336C")

    label("loc_335A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_336C")
    SetChrFlags(0x136, 0x80)

    label("loc_336C")

    SetChrPos(0x101, -20, 750, 2830, 0)
    SetChrPos(0x102, -20, 750, 2830, 0)
    OP_6D(-20, 750, 830, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_33C0")
    SetChrPos(0x105, -20, 750, 2830, 0)
    Jump("loc_33DE")

    label("loc_33C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_33DE")
    SetChrPos(0x136, -20, 750, 2830, 0)

    label("loc_33DE")

    Sleep(2000)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0x8, 0, 400)
    Sleep(1200)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x50)
    OP_73(0x0)

    def lambda_3418():

        label("loc_3418")

        TurnDirection(0x8, 0x101, 0)
        OP_48()
        Jump("loc_3418")

    QueueWorkItem2(0x8, 1, lambda_3418)
    OP_43(0x9, 0x1, 0x1, 0x8)
    OP_43(0x101, 0x1, 0x1, 0x9)
    Sleep(500)
    OP_43(0x102, 0x1, 0x1, 0xA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3459")
    Sleep(500)
    OP_43(0x105, 0x1, 0x1, 0xB)
    Jump("loc_3472")

    label("loc_3459")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3472")
    Sleep(500)
    OP_43(0x136, 0x1, 0x1, 0xB)

    label("loc_3472")

    WaitChrThread(0x102, 0x1)
    Sleep(1000)
    OP_72(0x0, 0x800)
    OP_22(0xD3, 0x0, 0x64)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_44(0x8, 0xFF)

    ChrTalk(
        0x8,
        "哦，还算顺利吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F哈哈，已经全部解决了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F魔兽已经被消灭，\x01",
            "没问题了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "真的吗，太好了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哎呀，\x01",
            "这下可以放心了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "你们也辛苦了。\x01",
            "干得不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从今往后也要记得\x01",
            "把关心别人放在首位哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#508F嗯，知道了。\x01",
            "老爷爷要好好保重哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()

    def lambda_36FF():

        label("loc_36FF")

        TurnDirection(0x8, 0x101, 0)
        OP_48()
        Jump("loc_36FF")

    QueueWorkItem2(0x8, 1, lambda_36FF)
    SetChrPos(0x9, 300, 750, -5000, 0)
    OP_51(0x9, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x9, 0x1, 0x1, 0xC)
    OP_43(0x101, 0x1, 0x1, 0xD)
    Sleep(300)
    OP_43(0x102, 0x1, 0x1, 0xE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3790")
    Sleep(300)
    OP_43(0x105, 0x1, 0x1, 0xF)
    Jump("loc_37A9")

    label("loc_3790")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_37A9")
    Sleep(300)
    OP_43(0x136, 0x1, 0x1, 0xF)

    label("loc_37A9")


    ChrTalk(
        0x8,
        "………………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    OP_44(0x8, 0xFF)

    ChrTalk(
        0x8,
        "……我说你们俩啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    def lambda_380A():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_380A)

    def lambda_3818():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3818)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_383E")

    def lambda_3833():
        TurnDirection(0x105, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3833)
    Jump("loc_3859")

    label("loc_383E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3859")

    def lambda_3851():
        TurnDirection(0x136, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_3851)

    label("loc_3859")


    ChrTalk(
        0x101,
        "#501F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你们没有忘记什么吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯？\x01",
            "好像没有忘记什么啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是不是还应该说\x01",
            "『您还有什么别的需要吗？』呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "为什么你们不问一下我\x01",
            "『您还有什么别的需要吗？』啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在完成了委托之后，\x01",
            "还应该记得问问委托人\x01",
            "有没有其他的需要才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3AC8")
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#043F（呼，\x01",
            "　做游击士也真是辛苦啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B52")

    label("loc_3AC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3B4D")
    OP_62(0x136, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x136,
        (
            "#043F（呼，\x01",
            "　做游击士也真是辛苦啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B52")

    label("loc_3B4D")

    Sleep(1000)

    label("loc_3B52")


    ChrTalk(
        0x8,
        (
            "当年那个壮年的游击士\x01",
            "离开的时候就这么问过的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呼，真是的。\x01",
            "你们果然不能与之相提并论呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哼，从刚才开始就啰里啰嗦的～\x02\x03",
            "那个壮年的游击士\x01",
            "究竟是什么样的家伙啊？\x02\x03",
            "听老爷爷您这么说，\x01",
            "他好像是个很了不起的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "七八年前，我承蒙过他的关照。\x01",
            "但是很遗憾，我并不知道他的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他可真是一个了不起的男子汉啊。\x01",
            "你们是肯定\x01",
            "无法和他相提并论的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果说\x01",
            "他和小姑娘你有相同的地方，\x01",
            "那就只有头发的颜色是完全一样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那个男人的头发，\x01",
            "也是红色中带有一丝茶色。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "……嗯？怎么回事，\x01",
            "越看你的眼睛的颜色，\x01",
            "越是感觉和他很相似。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……红色的头发，\x01",
            "和艾丝蒂尔相同的眼睛颜色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F那、那个游击士难道是…………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3FE3")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#044F？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4003")

    label("loc_3FE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4003")
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(
        0x136,
        "#044F？\x02",
    )

    CloseMessageWindow()

    label("loc_4003")


    ChrTalk(
        0x8,
        (
            "你们还远远没有\x01",
            "达到他那样的水平啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……把理想定得太高，\x01",
            "就容易忽视一些细小的方面。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_40D4")
    TurnDirection(0x105, 0x8, 400)
    Jump("loc_40E8")

    label("loc_40D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_40E8")
    TurnDirection(0x136, 0x8, 400)

    label("loc_40E8")


    ChrTalk(
        0x8,
        (
            "好了，\x01",
            "总之今后你们要好好加油就是了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "那么就这样吧，\x01",
            "我要去继续看守灯塔了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_41E8():

        label("loc_41E8")

        TurnDirection(0x101, 0x8, 0)
        OP_48()
        Jump("loc_41E8")

    QueueWorkItem2(0x101, 1, lambda_41E8)

    def lambda_41F9():

        label("loc_41F9")

        TurnDirection(0x102, 0x8, 0)
        OP_48()
        Jump("loc_41F9")

    QueueWorkItem2(0x102, 1, lambda_41F9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4225")

    def lambda_4217():

        label("loc_4217")

        TurnDirection(0x105, 0x8, 0)
        OP_48()
        Jump("loc_4217")

    QueueWorkItem2(0x105, 1, lambda_4217)
    Jump("loc_4243")

    label("loc_4225")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4243")

    def lambda_4238():

        label("loc_4238")

        TurnDirection(0x136, 0x8, 0)
        OP_48()
        Jump("loc_4238")

    QueueWorkItem2(0x136, 1, lambda_4238)

    label("loc_4243")

    OP_8E(0x8, 0x0, 0x2EE, 0xFFFFFB6E, 0x7D0, 0x0)
    OP_8C(0x8, 0, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x50)
    OP_73(0x0)
    OP_8E(0x8, 0xFFFFFFEC, 0x2EE, 0xB0E, 0x7D0, 0x0)
    OP_72(0x0, 0x800)
    OP_22(0xD3, 0x0, 0x64)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_42C4")
    OP_44(0x105, 0xFF)
    Jump("loc_42D5")

    label("loc_42C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_42D5")
    OP_44(0x136, 0xFF)

    label("loc_42D5")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#002F…………………………\x02\x03",
            "……约修亚，你是怎么想的？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x102,
        (
            "#010F不用想也可以知道。\x02\x03",
            "如果是七八年前，\x01",
            "在时间上就很吻合了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_44E7")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#040F请问，难道说……\x02\x03",
            "刚才老爷爷提起的那位壮年游击士，\x01",
            "是你们认识的人吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#505F唔～\x01",
            "说认识是理所当然的啦……\x02\x03",
            "因为那就是我们的老爸嘛。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044F啊………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……不过，\x01",
            "想要和父亲相比的确很难啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46C0")

    label("loc_44E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4632")
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(
        0x136,
        (
            "#040F请问，难道说……\x02\x03",
            "刚才老爷爷提起的那位壮年游击士，\x01",
            "是你们认识的人吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        (
            "#505F唔～\x01",
            "说认识是理所当然的啦……\x02\x03",
            "因为那就是我们的老爸嘛。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#044F啊………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……不过，\x01",
            "想要和父亲相比的确很难啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46C0")

    label("loc_4632")


    ChrTalk(
        0x101,
        (
            "#004F那么，\x01",
            "刚才老爷爷所说的那个游击士\x01",
            "果然就是老爸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F应该是的。\x02\x03",
            "……不过，\x01",
            "想要和父亲相比的确很难啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46C0")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F呼，真不甘心。\x02\x03",
            "如果是拿其他的游击士和我们做对比，\x01",
            "那个老爷爷就不会有这种抱怨了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F只要我们每天都努力加油，\x01",
            "一定可以赶上父亲的。\x02\x03",
            "…………不能因为对手太强而灰心丧气哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49B0")

    ChrTalk(
        0x101,
        (
            "#506F哈哈哈，说的也是。\x02\x03",
            "#006F不过我也坚信，\x01",
            "总有一天我们可以超越他。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#041F呵呵，\x01",
            "这样才像艾丝蒂尔嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，谢谢。\x02\x03",
            "#508F就这么决定了。\x01",
            "我们绝对不会偷懒的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C43")

    label("loc_49B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4B39")

    ChrTalk(
        0x101,
        (
            "#506F哈哈哈，说的也是。\x02\x03",
            "#006F不过我也坚信，\x01",
            "总有一天我们可以超越他。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(
        0x136,
        (
            "#041F呵呵，\x01",
            "这样才像艾丝蒂尔嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，谢谢。\x02\x03",
            "#508F就这么决定了。\x01",
            "我们绝对不会偷懒的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C43")

    label("loc_4B39")


    ChrTalk(
        0x101,
        (
            "#506F哈哈哈，说的也是。\x02\x03",
            "#006F不过我也坚信，\x01",
            "总有一天我们可以超越他。\x02\x03",
            "就这么决定了。\x01",
            "我们绝对不会偷懒的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C43")


    ChrTalk(
        0x102,
        (
            "#010F嗯，对啊。\x02\x03",
            "那我们出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【扫荡灯塔的魔兽】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    Return()

    # Function_7_332D end

    def Function_8_4CFE(): pass

    label("Function_8_4CFE")

    OP_6D(-750, 750, -2430, 2000)
    Return()

    # Function_8_4CFE end

    def Function_9_4D10(): pass

    label("Function_9_4D10")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4D26():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D26)
    OP_8E(0xFE, 0x0, 0x2EE, 0xFFFFFB6E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFD12, 0x2EE, 0xFFFFF682, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_9_4D10 end

    def Function_10_4D62(): pass

    label("Function_10_4D62")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4D78():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D78)
    OP_8E(0xFE, 0x0, 0x2EE, 0xFFFFFB6E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFD1C, 0x2EE, 0xFFFFFA24, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_10_4D62 end

    def Function_11_4DB4(): pass

    label("Function_11_4DB4")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4DCA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4DCA)
    OP_8E(0xFE, 0x0, 0x2EE, 0xFFFFFB6E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x208, 0x2EE, 0xFFFFFACE, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_11_4DB4 end

    def Function_12_4E06(): pass

    label("Function_12_4E06")

    OP_69(0x9, 0x7D0)
    Return()

    # Function_12_4E06 end

    def Function_13_4E0E(): pass

    label("Function_13_4E0E")

    OP_8E(0xFE, 0x12C, 0x2EE, 0xFFFFEC78, 0x7D0, 0x0)
    Return()

    # Function_13_4E0E end

    def Function_14_4E23(): pass

    label("Function_14_4E23")

    OP_8E(0xFE, 0xFFFFFD12, 0x2EE, 0xFFFFF682, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFDA8, 0x2EE, 0xFFFFF18C, 0x7D0, 0x0)
    Return()

    # Function_14_4E23 end

    def Function_15_4E4C(): pass

    label("Function_15_4E4C")

    OP_8E(0xFE, 0xFFFFFD1C, 0x2EE, 0xFFFFFA24, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFD12, 0x2EE, 0xFFFFF682, 0x7D0, 0x0)
    Return()

    # Function_15_4E4C end

    def Function_16_4E75(): pass

    label("Function_16_4E75")

    Return()

    # Function_16_4E75 end

    SaveToFile()

Try(main)
