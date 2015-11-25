from ED6ScenarioHelper import *

def main():
    # 帕赛尔农场

    CreateScenaFile(
        FileName            = 'T0411   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0411.x',
        MapIndex            = 13,
        MapDefaultBGM       = "ed60084",
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
        '缇欧',                                 # 9
        '维鲁',                                 # 10
        '查儿',                                 # 11
        '弗兰兹',                               # 12
        '汉娜',                                 # 13
        '目标用摄像机',                         # 14
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02480 ._CH',             # 00
        'ED6_DT07/CH01060 ._CH',             # 01
        'ED6_DT07/CH01070 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH00003 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02480P._CP',             # 00
        'ED6_DT07/CH01060P._CP',             # 01
        'ED6_DT07/CH01070P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH00003P._CP',             # 05
    )

    DeclNpc(
        X                   = -75800,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 1730,
        Z                   = 0,
        Y                   = 24300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 1730,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -39050,
        Z                   = 0,
        Y                   = 33240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 1270,
        Z                   = 0,
        Y                   = 37600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_30A",          # 01, 1
        "Function_2_30B",          # 02, 2
        "Function_3_321",          # 03, 3
        "Function_4_377",          # 04, 4
        "Function_5_430",          # 05, 5
        "Function_6_470",          # 06, 6
        "Function_7_550",          # 07, 7
        "Function_8_5AF",          # 08, 8
        "Function_9_61F",          # 09, 9
        "Function_10_6CD",         # 0A, 10
        "Function_11_16EA",        # 0B, 11
        "Function_12_16F9",        # 0C, 12
        "Function_13_170B",        # 0D, 13
        "Function_14_191B",        # 0E, 14
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 0)), scpexpr(EXPR_END)), "loc_218")
    SetChrPos(0x9, -77350, 0, -1160, 270)
    SetChrPos(0xA, -71660, 0, 2710, 0)
    SetChrPos(0x8, 2700, 0, 34460, 180)

    label("loc_218")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_22C"),
        (112, "loc_2F1"),
        (113, "loc_2F1"),
        (SWITCH_DEFAULT, "loc_309"),
    )


    label("loc_22C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_294")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x101, -70500, 0, -32040, 287)
    SetChrPos(0x102, -70500, 0, -32040, 287)
    OP_6D(-77800, 0, -31130, 0)
    Event(0, 14)
    Jump("loc_2EE")

    label("loc_294")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrPos(0x101, -74500, 0, 2590, 0)
    SetChrPos(0x102, 735, 0, 23000, 0)
    OP_6D(700, 0, 30000, 0)
    TurnDirection(0xA, 0x1, 0)
    TurnDirection(0x9, 0x1, 0)
    FadeToBright(1000, 0)
    Event(0, 10)

    label("loc_2EE")

    Jump("loc_309")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306")
    OP_A2(0x232)
    OP_28(0x2, 0x1, 0x20)
    Event(0, 13)

    label("loc_306")

    Jump("loc_309")

    label("loc_309")

    Return()

    # Function_0_1DE end

    def Function_1_30A(): pass

    label("Function_1_30A")

    Return()

    # Function_1_30A end

    def Function_2_30B(): pass

    label("Function_2_30B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_320")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_30B")

    label("loc_320")

    Return()

    # Function_2_30B end

    def Function_3_321(): pass

    label("Function_3_321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 0)), scpexpr(EXPR_END)), "loc_34E")

    label("loc_328")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34B")
    OP_8D(0xFE, 560, 22800, 2860, 25700, 3000)
    Jump("loc_328")

    label("loc_34B")

    Jump("loc_376")

    label("loc_34E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_376")
    OP_95(0xFE, 0x0, 0x0, 0x0, 0xC8, 0x640)
    Sleep(1000)
    Jump("loc_34E")

    label("loc_376")

    Return()

    # Function_3_321 end

    def Function_4_377(): pass

    label("Function_4_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 0)), scpexpr(EXPR_END)), "loc_3A4")

    label("loc_37E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A1")
    OP_8D(0xFE, -1400, 22900, 2600, 25700, 4000)
    Jump("loc_37E")

    label("loc_3A1")

    Jump("loc_42F")

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42F")
    OP_8E(0xFE, 0x0, 0x0, 0x5EEC, 0xBB8, 0x0)
    OP_8E(0xFE, 0x0, 0x0, 0x5B04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x0, 0x0, 0x5EEC, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x102, 0)
    OP_96(0xFE, 0x6C2, 0x0, 0x5EEC, 0x258, 0x640)
    TurnDirection(0xFE, 0x102, 300)
    OP_96(0xFE, 0x0, 0x0, 0x5EEC, 0x258, 0x640)
    TurnDirection(0xFE, 0x102, 300)
    Jump("loc_3A4")

    label("loc_42F")

    Return()

    # Function_4_377 end

    def Function_5_430(): pass

    label("Function_5_430")

    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        "外面已经很暗了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们两个要小心呀。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_5_430 end

    def Function_6_470(): pass

    label("Function_6_470")

    TalkBegin(0xA)
    TurnDirection(0xFE, 0x102, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52C")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "嗯、那个……\x01",
            "约修亚哥哥要去消灭魔兽吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不害怕吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没关系啦。\x01",
            "我们已经是游击士了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……约修亚好厉害呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_54C")

    label("loc_52C")


    ChrTalk(
        0xFE,
        "……约修亚好厉害呀。\x02",
    )

    CloseMessageWindow()

    label("loc_54C")

    TalkEnd(0xA)
    Return()

    # Function_6_470 end

    def Function_7_550(): pass

    label("Function_7_550")

    TalkBegin(0x9)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "约修亚哥哥，刚才真开心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "下次再玩呀。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_7_550 end

    def Function_8_5AF(): pass

    label("Function_8_5AF")

    TalkBegin(0xB)

    ChrTalk(
        0xFE,
        (
            "虽然那些魔兽\x01",
            "不是很凶暴，\x01",
            "不过速度相当快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们千万要小心。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_8_5AF end

    def Function_9_61F(): pass

    label("Function_9_61F")

    TalkBegin(0xC)

    ChrTalk(
        0xFE,
        (
            "虽然听缇欧说\x01",
            "你们正在以游击士为目标努力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过没想到协会\x01",
            "会派你们两个来这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要小心点哦。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_9_61F end

    def Function_10_6CD(): pass

    label("Function_10_6CD")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_1D(0x54)
    EventBegin(0x0)
    OP_6D(460, 0, 35390, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    TurnDirection(0x102, 0xA, 0)
    OP_6D(460, 0, 24000, 5000)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x8, 0x101, 0)
    Fade(1000)
    SetChrChipByIndex(0x101, 5)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -74100, 350, 2590, 270)
    OP_6D(-75700, 0, 3000, 0)
    OP_6B(2800, 0)
    OP_44(0x102, 0xFF)
    Sleep(1000)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)

    ChrTalk(
        0x101,
        (
            "#001F哈～好饱啊。\x02\x03",
            "#001F真的太好吃了，\x01",
            "汉娜阿姨还是那么会做菜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P呵呵，每次家里来客人的时候，\x01",
            "妈妈她都会干劲十足的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P话说回来，\x01",
            "今天真是辛苦约修亚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P还要他陪小孩子玩。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哈哈，这不是很好吗。\x02\x03",
            "#000F约修亚和那些小孩子\x01",
            "意外地合得来啊。\x02\x03",
            "#000F明明是那种很拘谨的性格……\x01",
            "真有点不可思议呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P哎呀，才不是这样呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P的确，他总是彬彬有礼，\x01",
            "在别人面前甚至可说是拘谨……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P不过一旦熟识了，\x01",
            "就会发现他很会照顾别人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P那种不经意间流露出的温柔，\x01",
            "更让人觉得很心动呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F是、是这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P再加上端正的相貌、\x01",
            "神秘的琥珀色眼睛、乌黑的头发……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P会引起女生尖叫也是理所当然的啦㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F……………………\x02\x03",
            "#004F约修亚这么受欢迎吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P你到现在才……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P据说想和他交往的\x01",
            "女生不止一个两个呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P不过他好像全部都拒绝掉了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F我、我不知道……\x02\x03",
            "#509F那个约修亚也真是的，\x01",
            "什么都不和我说……\x02\x03",
            "#509F不知道该说他是神神秘秘呢，\x01",
            "还是冷淡无情呢。真是不够意思！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P那当然，男孩子也就罢了，\x01",
            "这话题怎么能和女孩子谈嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P更何况……是和艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……为什么？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x102, -37400, 0, -3350, 0)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x102,
        (
            "艾丝蒂尔，可以了吗？\x02\x03",
            "差不多到巡逻的时间了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#004F啊～嗯……我知道了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrChipByIndex(0x101, 65535)
    OP_96(0x101, 0xFFFEDBB2, 0x0, 0x8D4, 0x258, 0x1770)
    ClearChrFlags(0x101, 0x4)

    ChrTalk(
        0x101,
        (
            "#006F好了，\x01",
            "我要去执行任务了。\x02\x03",
            "这个话题我们下次再聊吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P啊～那好吧。\x01",
            "要小心一点哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFEDBF8, 0x0, 0x500, 0xBB8, 0x0)
    OP_8E(0x101, 0xFFFEE7CE, 0x0, 0xFFFFFD03, 0xBB8, 0x0)
    OP_8E(0x101, 0xFFFEF3A4, 0x0, 0xFFFFFB14, 0xBB8, 0x0)
    SetChrPos(0x101, -37500, 0, -1980, 0)
    OP_22(0x6, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(
        0x8,
        (
            "#5P这个艾丝蒂尔还是老样子……\x01",
            "该说她不懂事呢，还是太迟钝呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P这样的话约修亚还真是辛苦啊。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x0, 0x1, 0)
    TurnDirection(0x1, 0x0, 0)
    Fade(1000)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x0)
    OP_6D(-37800, 0, -2850, 0)
    OP_6B(2600, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#010F看样子，\x01",
            "魔兽似乎总是在这个时间出现。\x02\x03",
            "#010F我们这就开始巡逻吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F………………（盯着看）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F怎、怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F喂～约修亚。\x02\x03",
            "#009F你是不是有什么事情瞒着我？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F啊……\x02\x03",
            "#014F为什么突然这么说？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F自从约修亚来到这个家……\x01",
            "我们俩就一直在一起对吧？\x02\x03",
            "#003F虽然经常吵架，\x01",
            "不过这也是美好的回忆……\x02\x03",
            "#003F我……\x01",
            "一直都把约修亚当作自己真正的家人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F所以呢……\x01",
            "如果有什么事情一定要和我说啊！\x02\x03",
            "#007F我是说……那个……\x02\x03",
            "#503F比如……青春的烦恼之类的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F不、不说这个了！\x02\x03",
            "还是赶快开始巡逻吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x1, 0x1, 0x0, 0xB)
    OP_8E(0x101, 0xFFFF6AB4, 0x0, 0xFFFFF2B8, 0x1388, 0x0)
    OP_8E(0x101, 0xFFFF68E8, 0x0, 0xFFFFD012, 0x1770, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(
        0x102,
        (
            "#017F缇欧都和她说了些什么啊……？\x02\x03",
            "#013F………………………………\x02\x03",
            "#013F…………瞒着她……吗………\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x230)
    OP_28(0x2, 0x1, 0x8)
    FadeToDark(1000, 0, -1)
    NewScene("ED6_DT01/T0401   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_10_6CD end

    def Function_11_16EA(): pass

    label("Function_11_16EA")

    OP_8C(0x102, 315, 400)
    OP_8C(0x102, 180, 400)
    Return()

    # Function_11_16EA end

    def Function_12_16F9(): pass

    label("Function_12_16F9")

    OP_6D(-2800, 0, 22400, 8000)
    Return()

    # Function_12_16F9 end

    def Function_13_170B(): pass

    label("Function_13_170B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174F")
    SetChrPos(0x101, 42290, 0, 5450, 270)
    SetChrPos(0x102, 43520, 0, 4400, 270)
    OP_6D(38110, 0, 5520, 2000)
    Jump("loc_1782")

    label("loc_174F")

    SetChrPos(0x101, 42150, 0, 35430, 270)
    SetChrPos(0x102, 43340, 0, 34350, 270)
    OP_6D(37700, 0, 35640, 2000)

    label("loc_1782")


    ChrTalk(
        0x102,
        (
            "#012F#1P…………………………\x02\x03",
            "#012F果然不在这里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#1P不过，这里感觉很好呢，\x01",
            "导力器的光芒有种迷幻般的气氛。\x02\x03",
            "#001F心情真舒畅㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F#1P你还真是悠闲啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#509F#1P是约修亚你太不解风情啦！\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    Return()

    # Function_13_170B end

    def Function_14_191B(): pass

    label("Function_14_191B")

    EventBegin(0x0)
    OP_6D(-76360, 0, -31950, 0)
    OP_6B(2600, 0)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x102, 0x80)

    def lambda_1970():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1970)

    def lambda_1982():
        OP_8E(0xFE, 0xFFFED630, 0x0, 0xFFFF8364, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1982)
    Sleep(1600)
    ClearChrFlags(0x101, 0x80)

    def lambda_19A7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19A7)
    OP_8E(0x101, 0xFFFEDDD8, 0x0, 0xFFFF8364, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        (
            "#007F哈啊～我快累得不行了……\x02\x03",
            "#007F今天已经很晚了，\x01",
            "赶快睡吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎……\x02\x03",
            "#000F怎么了，约修亚？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F…………抱歉。\x02\x03",
            "#013F让大家感到不快了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊，是指刚才的事吗？\x02\x03",
            "#001F你真是爱担心～\x01",
            "才不会有人那么想呢。\x02\x03",
            "#001F其实按道理来说，\x01",
            "约修亚的主张是正确的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F这并不是什么正确。\x01",
            "……只是我冷酷无情而已。\x02\x03",
            "#013F到现在我还是认为，\x01",
            "应该毫不留情地把它们杀死才对。\x02\x03",
            "#013F和艾丝蒂尔、缇欧不一样，\x01",
            "我根本没有可怜它们的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F这种时候……\x01",
            "我会不由自主地厌恶起自己来。\x02\x03",
            "#013F是不是我的人格有缺陷呢。\x02\x03",
            "#019F哈哈，\x01",
            "说不定是心里的某些地方已经坏掉了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_1D59():
        OP_8E(0xFE, 0xFFFED9DC, 0x0, 0xFFFF8364, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D59)
    OP_6D(-77400, 0, -31900, 1000)

    ChrTalk(
        0x101,
        "#005F#5S约修亚是大笨蛋！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F你怎么能这样随便对自己下结论呢！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x102, 0x101, 400)
    OP_8F(0x102, 0xFFFED52C, 0x0, 0xFFFF8364, 0xBB8, 0x0)

    ChrTalk(
        0x102,
        "#014F#5P艾、艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F这五年来，\x01",
            "约修亚的事情我一直看在眼里！\x02\x03",
            "#009F好的地方、不好的地方，\x01",
            "我有自信比任何人都清楚！\x02\x03",
            "#009F说不定比你本人还要清楚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F不要无视我的存在，\x01",
            "净说些乱七八糟的话！\x02\x03",
            "#005F坏掉什么的……\x01",
            "我绝对不许你那么说！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#5P…………………………\x02\x03",
            "#013F抱歉，说了些傻话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F知道了就好。\x02\x03",
            "#002F…………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F呵呵，不过……\x02\x03",
            "今天我真的有点高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#5P啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F约修亚你啊，\x01",
            "不是一直都自己一个人忍受着吗。\x02\x03",
            "#003F痛苦的时候，烦恼的时候……\x02\x03",
            "#003F总是装出一副若无其事的样子，\x01",
            "一个人去解决问题。\x02\x03",
            "#500F你每次都这样…… \x01",
            "有考虑过我的感受吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#5P…………………………\x02\x03",
            "#013F艾丝蒂尔，我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F不过今天，\x01",
            "你很坦率地说出了自己的烦恼。\x02\x03",
            "#006F这不就意味着，\x01",
            "你对我的信赖加深了吗？\x02\x03",
            "#001F所以我觉得很高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F#5P你、你说什么呀……\x02\x03",
            "#018F这么难为情的话你也说得出来。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿，别管这个啦⊙\x02\x03",
            "#006F好了，该睡觉了。\x01",
            "今天光是抓那些魔兽就够累的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#5P这也是啊……\x01",
            "晚安，艾丝蒂尔。\x02\x03",
            "#010F……真的，谢谢你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F不要客气啦。\x02\x03",
            "#000F晚安，约修亚。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    NewScene("ED6_DT01/T0400   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_14_191B end

    SaveToFile()

Try(main)
