from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4131   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4131.x',
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
        '卡兰大主教',                           # 9
        '利瓦尔牧师',                           # 10
        '修女诺雅',                             # 11
        '修女艾伦',                             # 12
        '希丝娜',                               # 13
        '西加罗',                               # 14
        '尤莉亚中尉',                           # 15
        '莉拉',                                 # 16
        '梅贝尔市长',                           # 17
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01670 ._CH',             # 01
        'ED6_DT07/CH01410 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT07/CH02090 ._CH',             # 05
        'ED6_DT07/CH02370 ._CH',             # 06
        'ED6_DT07/CH02360 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01670P._CP',             # 01
        'ED6_DT07/CH01410P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH02090P._CP',             # 05
        'ED6_DT07/CH02370P._CP',             # 06
        'ED6_DT07/CH02360P._CP',             # 07
    )

    DeclNpc(
        X                   = -50,
        Z                   = 1000,
        Y                   = 20410,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -131900,
        Z                   = 0,
        Y                   = 6270,
        Direction           = 3,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 2140,
        Z                   = 0,
        Y                   = 15980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -3470,
        Z                   = 0,
        Y                   = 510,
        Direction           = 110,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -3160,
        Z                   = 0,
        Y                   = 13260,
        Direction           = 352,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 4180,
        Z                   = 0,
        Y                   = 9260,
        Direction           = 2,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 200,
        Z                   = 0,
        Y                   = 14310,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = 200,
        TriggerZ            = 1000,
        TriggerY            = 17890,
        TriggerRange        = 400,
        ActorX              = -50,
        ActorZ              = 2500,
        ActorY              = 20410,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -74990,
        TriggerZ            = 0,
        TriggerY            = 66030,
        TriggerRange        = 800,
        ActorX              = -74990,
        ActorZ              = 1000,
        ActorY              = 66030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_252",          # 00, 0
        "Function_1_437",          # 01, 1
        "Function_2_507",          # 02, 2
        "Function_3_51D",          # 03, 3
        "Function_4_629",          # 04, 4
        "Function_5_68C",          # 05, 5
        "Function_6_A0F",          # 06, 6
        "Function_7_B60",          # 07, 7
        "Function_8_136F",         # 08, 8
        "Function_9_184F",         # 09, 9
        "Function_10_21D7",        # 0A, 10
        "Function_11_2E2C",        # 0B, 11
        "Function_12_2E31",        # 0C, 12
        "Function_13_4593",        # 0D, 13
    )


    def Function_0_252(): pass

    label("Function_0_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26F")
    SetChrPos(0x8, 72000, 4000, 6060, 0)

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_2A5")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3020, 0, 13250, 340)
    SetChrPos(0xF, 4040, 0, 13250, 1)
    Jump("loc_2EF")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2CA")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, 71980, 4000, 6250, 0)
    Jump("loc_2EF")

    label("loc_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_2D4")
    Jump("loc_2EF")

    label("loc_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_2DE")
    Jump("loc_2EF")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_2E8")
    Jump("loc_2EF")

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_2EF")

    label("loc_2EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2FE")
    SetChrFlags(0xB, 0x80)
    Jump("loc_436")

    label("loc_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_30D")
    SetChrFlags(0xB, 0x80)
    Jump("loc_436")

    label("loc_30D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_32D")
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x8, 72000, 4000, 6060, 0)
    Jump("loc_436")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_341")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_436")

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_36D")
    SetChrPos(0xB, -2130, 0, 15890, 180)
    SetChrPos(0x9, 2440, 1000, 18600, 180)
    Jump("loc_436")

    label("loc_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3AA")
    SetChrPos(0xB, -133770, 0, 64950, 15)
    SetChrPos(0x9, 72000, 4000, 5780, 0)
    SetChrPos(0xA, -71370, 0, 3320, 90)
    Jump("loc_436")

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3DB")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, -2130, 0, 15890, 180)
    SetChrPos(0x9, 2440, 1000, 18600, 180)
    Jump("loc_436")

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3EA")
    SetChrFlags(0xB, 0x80)
    Jump("loc_436")

    label("loc_3EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_416")
    SetChrPos(0xB, -2130, 0, 15890, 180)
    SetChrPos(0x9, 2440, 1000, 18600, 180)
    Jump("loc_436")

    label("loc_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_42A")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_436")

    label("loc_42A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_436")
    SetChrFlags(0xB, 0x80)

    label("loc_436")

    Return()

    # Function_0_252 end

    def Function_1_437(): pass

    label("Function_1_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46A")
    OP_B1("t4131_y")
    Jump("loc_473")

    label("loc_46A")

    OP_B1("t4131_n")

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_483")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_493")
    OP_64(0x0, 0x1)

    label("loc_493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4A1")
    OP_64(0x0, 0x1)
    Jump("loc_506")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4AB")
    Jump("loc_506")

    label("loc_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4B9")
    OP_64(0x0, 0x1)
    Jump("loc_506")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4C3")
    Jump("loc_506")

    label("loc_4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4CD")
    Jump("loc_506")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4D7")
    Jump("loc_506")

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4E1")
    Jump("loc_506")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4EB")
    Jump("loc_506")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4F5")
    Jump("loc_506")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4FF")
    Jump("loc_506")

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_506")

    label("loc_506")

    Return()

    # Function_1_437 end

    def Function_2_507(): pass

    label("Function_2_507")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_507")

    label("loc_51C")

    Return()

    # Function_2_507 end

    def Function_3_51D(): pass

    label("Function_3_51D")

    TalkBegin(0xFE)

    ChrTalk(
        0x10,
        (
            "#610F因为平时太忙，\x01",
            "所以这次我更要好好地祷告了。\x01",
            "　\x02\x03",
            "看来到大圣堂\x01",
            "还得把至今为止偷的懒\x01",
            "一起做个忏悔才行呢……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_51D end

    def Function_4_629(): pass

    label("Function_4_629")

    TalkBegin(0xFE)

    ChrTalk(
        0xF,
        (
            "#620F真是难得，\x01",
            "今天小姐竟然说要去教会。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_629 end

    def Function_5_68C(): pass

    label("Function_5_68C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6FF")

    ChrTalk(
        0xE,
        (
            "#170F对了，\x01",
            "你们也是来找大主教的吗？\x02\x03",
            "大主教他刚才到祭器室去了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0B")

    label("loc_6FF")

    OP_A2(0x6)

    ChrTalk(
        0xE,
        "#170F哦，艾丝蒂尔、约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F是尤莉亚中尉啊，\x01",
            "在这里做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#170F在教会潜伏期间，\x01",
            "我受到了大主教的诸多关照。\x02\x03",
            "这次是来向他表示谢意，\x01",
            "并说明事情的详细情况的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，原来是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#170F对了，\x01",
            "我也要向你们表示感谢。\x02\x03",
            "这回能够救出女王陛下和公主殿下，\x01",
            "真的多亏了你们两个。\x02\x03",
            "如果只靠我们是无法做到的……\x01",
            "真是太感谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哪里，如果只有我们\x01",
            "而没有尤莉亚中尉的话，\x01",
            "也不知道能不能成功呢……\x02\x03",
            "而且救助女王陛下这件事\x01",
            "是我们理所当然应该协助的。\x02\x03",
            "#001F所以啦，不用那么客气嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#173F…………………………\x02\x03",
            "#171F是吗，谢谢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0B")

    TalkEnd(0xFE)
    Return()

    # Function_5_68C end

    def Function_6_A0F(): pass

    label("Function_6_A0F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A1C")
    Jump("loc_B5C")

    label("loc_A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A26")
    Jump("loc_B5C")

    label("loc_A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_A30")
    Jump("loc_B5C")

    label("loc_A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_A9D")

    ChrTalk(
        0xFE,
        (
            "大主教的教导\x01",
            "真的很有意义哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家要是\x01",
            "都能常来听听就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5C")

    label("loc_A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_AA7")
    Jump("loc_B5C")

    label("loc_AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_AB1")
    Jump("loc_B5C")

    label("loc_AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_B37")

    ChrTalk(
        0xFE,
        (
            "呼，大圣堂的礼拜堂\x01",
            "不愧是洗涤心灵之处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "愿妻子也能得到\x01",
            "女神的祝福……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5C")

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B41")
    Jump("loc_B5C")

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B4B")
    Jump("loc_B5C")

    label("loc_B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B55")
    Jump("loc_B5C")

    label("loc_B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B5C")

    label("loc_B5C")

    TalkEnd(0xFE)
    Return()

    # Function_6_A0F end

    def Function_7_B60(): pass

    label("Function_7_B60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BE9")

    ChrTalk(
        0xFE,
        (
            "虽然发生了许多事，\x01",
            "但最终还是回归到了和平的日子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这也是因为女神的指引啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_136B")

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_C9B")

    ChrTalk(
        0xFE,
        (
            "从刚才就听到\x01",
            "外面在吵吵闹闹的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不行啊……\x01",
            "不能集中精神祈祷了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136B")

    label("loc_C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_D17")

    ChrTalk(
        0xFE,
        (
            "那位最近新来的修女\x01",
            "今天不在呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是生病了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_136B")

    label("loc_D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_DC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_D5D")

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "本来想再祈祷一会儿的，\x01",
            "但也不能在这里呆到太晚。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBD")

    label("loc_D5D")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "已经这么晚了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "本来想再祈祷一会儿的，\x01",
            "但也不能在这里呆到太晚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DBD")

    Jump("loc_136B")

    label("loc_DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_E2C")

    ChrTalk(
        0xFE,
        (
            "我今天来大圣堂这里，\x01",
            "是为了祈祷女王陛下的身体\x01",
            "能够早日康复。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136B")

    label("loc_E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_FF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_EC0")

    ChrTalk(
        0xFE,
        (
            "大崩坏以后，\x01",
            "这个世界是以教会为中心重新建立的，\x01",
            "难道大家都忘记了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FEE")

    label("loc_EC0")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "导力器发明之后，\x01",
            "生活就更加方便了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "人们渐渐地不再信仰女神了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大崩坏以后，\x01",
            "这个世界是以教会为中心重新建立的，\x01",
            "难道大家都忘记了吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FEE")

    Jump("loc_136B")

    label("loc_FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_11EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10DA")

    ChrTalk(
        0xFE,
        (
            "来教会祈祷的人数\x01",
            "最近一直在减少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从主日学校毕业后\x01",
            "很快就不来教会的人，\x01",
            "却变得多起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E8")

    label("loc_10DA")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "来教会祈祷的人数\x01",
            "最近一直在减少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从主日学校毕业后\x01",
            "很快就不来教会的人，\x01",
            "却变得多起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我觉得真是很遗憾啊。\x02",
    )

    CloseMessageWindow()

    label("loc_11E8")

    Jump("loc_136B")

    label("loc_11EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1264")

    ChrTalk(
        0xFE,
        (
            "大主教和牧师的布教\x01",
            "都讲得非常棒哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "方便的话，你们也来听听吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_136B")

    label("loc_1264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_12BE")

    ChrTalk(
        0xFE,
        (
            "孕育了我生命的女神啊，\x01",
            "我每天都会虔诚祈祷的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136B")

    label("loc_12BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1301")

    ChrTalk(
        0xFE,
        (
            "女神啊，今天又平平安安地过去了，\x01",
            "感谢之至……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136B")

    label("loc_1301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_136B")

    ChrTalk(
        0xFE,
        (
            "女神爱德丝\x01",
            "一直都在保佑着我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要珍惜每一天的幸福生活。\x02",
    )

    CloseMessageWindow()

    label("loc_136B")

    TalkEnd(0xFE)
    Return()

    # Function_7_B60 end

    def Function_8_136F(): pass

    label("Function_8_136F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_137C")
    Jump("loc_184B")

    label("loc_137C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1386")
    Jump("loc_184B")

    label("loc_1386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1390")
    Jump("loc_184B")

    label("loc_1390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_139A")
    Jump("loc_184B")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_14B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_13CD")

    ChrTalk(
        0xFE,
        "呵呵，今天的决赛请加油哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14AF")

    label("loc_13CD")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "啊，艾丝蒂尔小姐、约修亚先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天你们\x01",
            "平安无事地回去了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊，嗯，是的。\x01",
            "平安无事地回去了。\x02\x03",
            "#007F（唔……\x01",
            "　其实我知道她就是尤莉亚小姐，\x01",
            "　不过不知道该怎么去和她谈话才好呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（我想跟平时一样就可以吧。）\x02",
    )

    CloseMessageWindow()

    label("loc_14AF")

    Jump("loc_184B")

    label("loc_14B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1514")

    ChrTalk(
        0xFE,
        (
            "现在是休息时间，\x01",
            "可以从这里看看云彩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_184B")

    label("loc_1514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1579")

    ChrTalk(
        0xFE,
        "早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "早晨的弥撒\x01",
            "马上就要开始了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_184B")

    label("loc_1579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1583")
    Jump("loc_184B")

    label("loc_1583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_183A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 5)), scpexpr(EXPR_END)), "loc_15C4")

    ChrTalk(
        0xFE,
        (
            "昨天真的是\x01",
            "多谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1837")

    label("loc_15C4")

    OP_A2(0x67D)

    ChrTalk(
        0xFE,
        "啊……你们几位是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天承蒙你们的帮助，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，你是昨天的修女。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个……\x01",
            "真是感到抱歉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "得到了你们的帮助，\x01",
            "但因为我的缘故，\x01",
            "让你们遇到不愉快的事情了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F不愉快？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F你不记得了吗，\x01",
            "昨天那些士兵在那里胡搅蛮缠。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊～那件事啊，\x01",
            "不用在意啦。\x02\x03",
            "#009F是那些家伙太可恶了嘛。\x01",
            "根本就是脑袋有问题。\x02\x03",
            "#000F对了，\x01",
            "那之后他们有平安护送你回来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是、是的，请别担心。\x01",
            "他们平安地把我送了回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是这样啊，\x01",
            "那么以后外出的时候要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好的，\x01",
            "真是多谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1837")

    Jump("loc_184B")

    label("loc_183A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1844")
    Jump("loc_184B")

    label("loc_1844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_184B")

    label("loc_184B")

    TalkEnd(0xFE)
    Return()

    # Function_8_136F end

    def Function_9_184F(): pass

    label("Function_9_184F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_18AF")

    ChrTalk(
        0xFE,
        (
            "大街上的人们脸上都带着愉快的表情，\x01",
            "看着他们让我的心情很舒畅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "愿大家都受到\x01",
            "女神爱德丝的祝福……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D3")

    label("loc_18AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1950")

    ChrTalk(
        0xFE,
        (
            "士兵们好像\x01",
            "还在搜捕亲卫队啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是说起来，\x01",
            "他们至今也没能找到\x01",
            "一个亲卫队的人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D3")

    label("loc_1950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 7)), scpexpr(EXPR_END)), "loc_1A40")

    ChrTalk(
        0xFE,
        (
            "艾伦虽然是个路痴，\x01",
            "不过却相当懂得礼仪，\x01",
            "而且也很热心帮助别人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "她这么忙也是没办法的事。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D3")

    label("loc_1A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1B04")

    ChrTalk(
        0xFE,
        (
            "你们……\x01",
            "是来找艾伦的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想大主教应该知道\x01",
            "她现在在哪儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大主教在这个大圣堂\x01",
            "东南方的祭祀用具室里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D3")

    label("loc_1B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1B71")

    ChrTalk(
        0xFE,
        "啊，空之女神爱德丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天又平安度过了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D3")

    label("loc_1B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1C2B")

    ChrTalk(
        0xFE,
        (
            "诞辰庆典结束之后，\x01",
            "我想在大圣堂这里\x01",
            "举行一个义卖会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "从现在开始就要着手准备了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D3")

    label("loc_1C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1CAC")

    ChrTalk(
        0xFE,
        (
            "今天必须将典礼上\x01",
            "使用的圣歌集整理好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "咦，\x01",
            "艾伦她去了哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE0")

    label("loc_1CAC")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "今天之内必须将典礼上\x01",
            "使用的圣歌集整理好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "至今为止还剩两百多本，\x01",
            "看来够得辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "咦，\x01",
            "艾伦她去了哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不会又在\x01",
            "什么地方迷路了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE0")

    Jump("loc_21D3")

    label("loc_1DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1E2E")

    ChrTalk(
        0xFE,
        (
            "空之女神爱德丝啊……\x01",
            "今天也请您护佑我们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D3")

    label("loc_1E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1EA1")

    ChrTalk(
        0xFE,
        "奇怪……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来还想拜托她办点事的……\x01",
            "艾伦又跑到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F19")

    label("loc_1EA1")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "奇怪……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来还想拜托她办点事的……\x01",
            "艾伦又跑到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "头疼啊……\x02",
    )

    CloseMessageWindow()

    label("loc_1F19")

    Jump("loc_21D3")

    label("loc_1F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1F98")

    ChrTalk(
        0xFE,
        "好，新的一天开始了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天也要努力啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D3")

    label("loc_1F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2021")

    ChrTalk(
        0xFE,
        (
            "修女艾伦\x01",
            "不会出了什么事吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她去了艾尔贝周游道，\x01",
            "到现在都还没有回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D3")

    label("loc_2021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_21D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_209A")

    ChrTalk(
        0xFE,
        (
            "几天前这里\x01",
            "新来了一位修女，\x01",
            "刚才出去采摘药草了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D3")

    label("loc_209A")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "不知道到洛连特教会\x01",
            "赴任的梅现在可好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我是担任\x01",
            "教育任务的修女。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "几天前这里\x01",
            "新来了一位修女，\x01",
            "刚才出去采摘药草了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D3")

    TalkEnd(0xFE)
    Return()

    # Function_9_184F end

    def Function_10_21D7(): pass

    label("Function_10_21D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_225A")

    ChrTalk(
        0xFE,
        (
            "能够顺利地举行诞辰庆典，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这也是因为\x01",
            "有女神的保佑啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E28")

    label("loc_225A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_22CA")

    ChrTalk(
        0xFE,
        (
            "怎么那些士兵\x01",
            "看上去很慌张呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生了什么事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E28")

    label("loc_22CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_25C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23DC")

    ChrTalk(
        0xFE,
        (
            "分离正是新的相聚的开始，\x01",
            "人的一生就在\x01",
            "这个过程中循环不息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "人生，就是这样由一根\x01",
            "所谓命运的丝线所编织而成的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C4")

    label("loc_23DC")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "落叶聚还散，寒鸦栖复惊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "分离正是新的相聚的开始，\x01",
            "人的一生就在\x01",
            "这个过程中循环不息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "人生，就是这样由一根\x01",
            "所谓命运的丝线所编织而成的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们人类\x01",
            "虽然难以预测\x01",
            "自身的命运……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但女神应该\x01",
            "是知晓一切的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C4")

    Jump("loc_2E28")

    label("loc_25C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_267C")

    ChrTalk(
        0xFE,
        (
            "格兰赛尔大圣堂历史悠久，\x01",
            "今年是设立后的１１２０周年呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "应该是同利贝尔王家\x01",
            "在大致相同的时候兴建的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E28")

    label("loc_267C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_271F")

    ChrTalk(
        0xFE,
        (
            "如同游击士协会那样，\x01",
            "七耀教会在整个大陆都遍布了\x01",
            "等同于协会支部的分支设施。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当然，\x01",
            "格兰赛尔大圣堂也是其中之一。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E28")

    label("loc_271F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_298D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2830")

    ChrTalk(
        0xFE,
        (
            "大崩坏之后的人们\x01",
            "那种努力生存的精神\x01",
            "可以说焕发出了生命之光。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果换一种角度看问题，\x01",
            "大崩坏也许是女神的试练呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_298A")

    label("loc_2830")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "大崩坏之后，幸存下来的人们\x01",
            "熬过了暗无天日的时代，活了下去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "生活状况虽然凄苦，\x01",
            "但是那种努力生存的精神\x01",
            "可以说焕发出了生命之光。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果换一种角度看问题，\x01",
            "大崩坏也许是女神的试练呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_298A")

    Jump("loc_2E28")

    label("loc_298D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2AED")

    ChrTalk(
        0xFE,
        (
            "只要世界存在，\x01",
            "就会有夏去冬来，昼夜更替……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "播种收获都在不断重复，\x01",
            "永无休止。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大崩坏之后，人们虽然饱受苦痛，\x01",
            "但最后仍生存下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然看着同样的事情不断重复，\x01",
            "但这个世界总是一点一点地\x01",
            "向着美好的方向前进。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E28")

    label("loc_2AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B9E")

    ChrTalk(
        0xFE,
        (
            "世界起源之初，\x01",
            "大地无形无态，\x01",
            "由黑暗与狂风所支配。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "将光明赋予大地的\x01",
            "就是女神爱德丝。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E28")

    label("loc_2B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2D92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C44")

    ChrTalk(
        0xFE,
        (
            "昨天多亏了你们\x01",
            "救了修女艾伦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是非常感谢。\x01",
            "愿你们的前路充满光明。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D8F")

    label("loc_2C44")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "哦，你们是游击士协会的朋友吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天多亏了你们\x01",
            "救了修女艾伦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她外出采摘药草却一直未归，\x01",
            "让我们很是担心了一场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是非常感谢。\x01",
            "愿你们的前路充满光明。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D8F")

    Jump("loc_2E28")

    label("loc_2D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2DD5")

    ChrTalk(
        0xFE,
        (
            "大街上也\x01",
            "开始变得热闹起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E28")

    label("loc_2DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2E28")

    ChrTalk(
        0xFE,
        "欢迎来到七耀教会的大圣堂。\x02",
    )

    CloseMessageWindow()

    label("loc_2E28")

    TalkEnd(0xFE)
    Return()

    # Function_10_21D7 end

    def Function_11_2E2C(): pass

    label("Function_11_2E2C")

    Call(0, 12)
    Return()

    # Function_11_2E2C end

    def Function_12_2E31(): pass

    label("Function_12_2E31")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3583")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 71280, 4000, 4900, 0)
    SetChrPos(0x102, 72450, 4000, 4890, 0)
    SetChrPos(0x108, 71610, 4000, 4030, 0)
    TurnDirection(0x8, 0x108, 0)
    OP_A2(0x64F)
    OP_28(0x4B, 0x1, 0x400)
    OP_6D(71530, 4000, 5910, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "哦，你们几位是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，那个……\x01",
            "我们是游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F请问那位名叫艾伦的修女\x01",
            "现在在大圣堂这里吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这么说，\x01",
            "你们就是她的协助者了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F咦……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F……看来您对情况也相当了解呢。\x01",
            "　\x02\x03",
            "#012F她的委托完成了，我们是来报告的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "很遗憾，\x01",
            "她现在已经不在大圣堂里面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "今天早晨，她向我打了声招呼，\x01",
            "然后就自己离开这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F到、到哪里去了呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "很遗憾，我不清楚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "因为我们和王家长期保持着良好的关系，\x01",
            "所以这次就让她隐藏在了教会里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过关于这回的事件，\x01",
            "她并没有告诉我详情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "很可能是因为\x01",
            "不想给教会带来麻烦吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不过请放心吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在离开这里时，\x01",
            "她的眼中充满了希望的光芒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "绝不是因为穷途末路、\x01",
            "自暴自弃而离开的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F听、听您这么一说，\x01",
            "我就放心了……\x02\x03",
            "#505F可是这么一来，\x01",
            "就不能和亲卫队取得联络了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F也只能暂时这样了。\x01",
            "毕竟我们也不是那么容易就能找到他们。\x02\x03",
            "#074F暂且只有把亲卫队的事放置在一旁了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F没办法，也只有这样了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "看起来，\x01",
            "你们好像遇到了很大的困难啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "女神啊，帮助那些自强不息的人吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "只要你们能够全力以赴的话，\x01",
            "女神一定为你们指明方向的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3576():
        OP_8C(0x8, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3576)
    EventEnd(0x0)
    Jump("loc_458F")

    label("loc_3583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_37DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3648")

    ChrTalk(
        0x8,
        "导力文明是个值得谈论的话题啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "塞姆里亚人凭借他们的睿智，\x01",
            "将世界以现在这个形态\x01",
            "传承了下来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37D7")

    label("loc_3648")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        "导力文明是个值得谈论的话题啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "塞姆里亚人凭借他们的睿智，\x01",
            "将世界以现在这个形态\x01",
            "传承了下来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们必须要\x01",
            "切实地守护好它……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F？？？\x02",
    )

    CloseMessageWindow()

    label("loc_37D7")

    Jump("loc_458F")

    label("loc_37DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3881")

    ChrTalk(
        0x8,
        (
            "用你们的眼睛\x01",
            "去洞悉未知的一切吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "赶快前往应该去的地方吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "愿女神引导你们。\x02",
    )

    CloseMessageWindow()
    Jump("loc_458F")

    label("loc_3881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3954")

    ChrTalk(
        0x8,
        "女神啊，帮助那些自强不息的人吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "只要你们能够全力以赴的话，\x01",
            "女神一定为你们指明方向的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458F")

    label("loc_3954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3A0D")

    ChrTalk(
        0x8,
        "武术大会结束了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然不知道诞辰庆典会如何，\x01",
            "但还是先做好准备吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458F")

    label("loc_3A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3AA5")

    ChrTalk(
        0x8,
        (
            "我今年还没见过\x01",
            "科洛蒂娅公主\x01",
            "来大圣堂这边……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "想必她一直在王城里\x01",
            "陪伴着身体欠佳的陛下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BB4")

    label("loc_3AA5")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "这么说来，\x01",
            "每年这个时候\x01",
            "科洛蒂娅公主都会来大圣堂的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "为了庆祝女王的诞辰庆典，\x01",
            "公主都会来这里诚心祈祷……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过我今年还没见到\x01",
            "公主来过大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "想必她一直在王城里\x01",
            "陪伴着身体欠佳的陛下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BB4")

    Jump("loc_458F")

    label("loc_3BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3D21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3C52")

    ChrTalk(
        0x8,
        (
            "从今天开始市内的主要设施\x01",
            "都成了重点巡逻的对象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "刚才，\x01",
            "这里也接到王国军的通告了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D1E")

    label("loc_3C52")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "王国军似乎\x01",
            "加强了全城的警戒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从今天开始市内的主要设施\x01",
            "都成了重点巡逻的对象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "刚才，\x01",
            "这里也接到王国军的通告了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D1E")

    Jump("loc_458F")

    label("loc_3D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3F32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D93")

    ChrTalk(
        0x8,
        (
            "教会也很想和王室\x01",
            "构筑良好的关系呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F2F")

    label("loc_3D93")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "百日战役时，\x01",
            "七耀教会和游击士协会\x01",
            "一同担当了调停的角色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然政教互相干涉\x01",
            "绝非什么好事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过只要双方充分理解，\x01",
            "并能在机会适当时联手，\x01",
            "就能将事情处理得很完美。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "教会也很想和王室\x01",
            "构筑良好的关系呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F2F")

    Jump("loc_458F")

    label("loc_3F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4007")

    ChrTalk(
        0x8,
        (
            "七耀教会和利贝尔王室\x01",
            "常年保持着良好的关系呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "自从大崩坏之后，\x01",
            "合作的关系至少\x01",
            "维持了一千多年。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4125")

    label("loc_4007")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "七耀教会和利贝尔王室\x01",
            "常年保持着良好的关系呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "自从大崩坏之后，\x01",
            "合作的关系至少\x01",
            "维持了一千多年。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "当然现在和艾莉茜雅女王的\x01",
            "关系也很密切。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4125")

    Jump("loc_458F")

    label("loc_4128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_42D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_41BD")

    ChrTalk(
        0x8,
        (
            "大圣堂从混乱的时代开始直到今天，\x01",
            "一直在这片土地上\x01",
            "不懈地履行着属于自己的使命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "据说在利贝尔王国之中，\x01",
            "还存在着更加古老的\x01",
            "七耀教会的设施。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42D3")

    label("loc_41BD")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "七耀教会是在大崩坏之后成立的，\x01",
            "以为人们指明道路为己任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "大圣堂从混乱的时代开始直到今天，\x01",
            "一直在这片土地上\x01",
            "不懈地履行着属于自己的使命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "据说在利贝尔王国之中，\x01",
            "还存在着更加古老的\x01",
            "七耀教会的设施。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42D3")

    Jump("loc_458F")

    label("loc_42D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_438E")

    ChrTalk(
        0x8,
        (
            "为了让市民更有热情\x01",
            "而举办的武术大会吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "杜南公爵是这么说的，\x01",
            "真让人捉摸不透……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458F")

    label("loc_438E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_458F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4451")

    ChrTalk(
        0x8,
        (
            "城里竟然没有一个人\x01",
            "知道陛下的具体情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我想女管事希尔丹夫人应该知道，\x01",
            "于是就想和她当面谈谈，\x01",
            "却被身穿黑色盔甲的人断然拒绝了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458F")

    label("loc_4451")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "我本想为身体欠佳的陛下\x01",
            "送些药草去的，\x01",
            "于是向王城里的人询问了陛下的病状……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "可是竟然没有一个人\x01",
            "知道陛下的具体情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我想女管事希尔丹夫人应该知道，\x01",
            "于是就想和她当面谈谈，\x01",
            "却被身穿黑色盔甲的人断然拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_458F")

    TalkEnd(0x8)
    Return()

    # Function_12_2E31 end

    def Function_13_4593(): pass

    label("Function_13_4593")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_4593 end

    SaveToFile()

Try(main)
