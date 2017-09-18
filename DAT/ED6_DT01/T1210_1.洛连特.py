from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T1210_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T1210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        "Function_1_918",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77C")
    EventBegin(0x0)
    OP_69(0xFE, 0x3E8)
    OP_28(0xE, 0x4, 0x8)
    OP_28(0xE, 0x4, 0x4)
    OP_28(0xE, 0x1, 0x1)
    OP_28(0xE, 0x1, 0x2)
    OP_28(0xE, 0x1, 0x4)
    OP_A2(0x2)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0xFE,
        "哦…………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道说，\x01",
            "你们就是游击士协会派来的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定是看了公告板\x01",
            "而赶过来的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_22E")

    ChrTalk(
        0x101,
        "#000F嗯，是的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "哦，那真是太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "老朽名叫莱森，\x01",
            "是本村的村长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正如你们所知的那样，\x01",
            "最近村庄深处的山道上\x01",
            "出现了一只凶暴的魔兽。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B5")

    label("loc_22E")

    OP_28(0xE, 0x4, 0x2)

    ChrTalk(
        0x101,
        "#000F公告板？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "老朽名叫莱森。\x01",
            "是本村的村长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实最近在村庄深处的山道上\x01",
            "出现了一只凶暴的魔兽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望游击士协会的各位\x01",
            "能够帮忙消灭它。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B5")

    ChrTalk(
        0x101,
        (
            "#004F咦……？！\x01",
            "有这样的事情？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F能告诉我们详细的情况吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B5")


    ChrTalk(
        0x102,
        (
            "#012F您知道出没的是什么样的魔兽吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "我也不太清楚，\x01",
            "因为还没有可靠的目击者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "恐怕是一种潜伏等待猎物到来，\x01",
            "然后出来将其捕获的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在矿山还很兴旺的时候\x01",
            "也曾经出现过这种魔兽，\x01",
            "大家对此都感到十分苦恼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F……原来如此，是潜伏着的魔兽啊。\x01",
            "这就有些麻烦了。\x02\x03",
            "必须在山道上仔细搜索，\x01",
            "把魔兽隐藏的地点找出来才行。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "矿山荒废之后就没人再去那里了，\x01",
            "我以为那些魔兽\x01",
            "已经进入了休眠状态……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到底为什么\x01",
            "又再次出现了呢…………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "过一阵就是今年\x01",
            "开始种植树苗的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "村里的人为此都很担心。\x01",
            "你们还可以去找守门人菲戈，\x01",
            "也许他能告诉你们更多的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刻不容缓，\x01",
            "请务必帮我们消灭掉魔兽啊。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_917")

    label("loc_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_809")

    ChrTalk(
        0xFE,
        (
            "过一阵就是今年\x01",
            "开始种植树苗的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在已经刻不容缓了，\x01",
            "请务必帮我们消灭掉魔兽啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_917")

    label("loc_809")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "哦，各位，\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "有没有什么成果呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F抱歉，\x01",
            "可能还要花些时间。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "过一阵就是今年\x01",
            "开始种植树苗的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在已经刻不容缓了，\x01",
            "请务必帮我们消灭掉魔兽啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_917")

    Return()

    # Function_0_66 end

    def Function_1_918(): pass

    label("Function_1_918")

    OP_28(0xE, 0x1, 0x800)
    OP_A2(0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_9D5")

    ChrTalk(
        0xFE,
        "哦，各位，\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "有没有什么成果呢？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#001F呵呵呵呵呵⊙\x02\x03",
            "已经解决掉啦☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A97")

    label("loc_9D5")


    ChrTalk(
        0xFE,
        (
            "哦，是你们。\x01",
            "你们就是游击士协会派来的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定是看了公告板\x01",
            "而赶过来的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#001F呵呵呵呵呵⊙\x02\x03",
            "通缉魔兽的话，\x01",
            "已经解决掉啦☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A97")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "哦哦，那真是好消息！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "太好了，\x01",
            "这样我们今年就可以\x01",
            "安安心心地种植树苗了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真的是辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们这个偏僻的小村，\x01",
            "随时都欢迎你们的到来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，谢谢村长先生。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_1_918 end

    SaveToFile()

Try(main)
