from ED6ScenarioHelper import *

def main():
    # 帕赛尔农场

    CreateScenaFile(
        FileName            = 'T0401   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0401.x',
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
        '魔兽',                                 # 9
        '魔兽',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '魔兽',                                 # 13
        '魔兽',                                 # 14
        '魔兽',                                 # 15
        '缇欧',                                 # 16
        '维鲁',                                 # 17
        '查儿',                                 # 18
        '弗兰兹',                               # 19
        '汉娜',                                 # 20
        '艾丝蒂尔',                             # 21
        '牛',                                   # 22
        '牛',                                   # 23
        '目标用摄像机',                         # 24
        '米尔西街道方向',                       # 25
    )

    DeclEntryPoint(
        Unknown_00              = 21000,
        Unknown_04              = 0,
        Unknown_08              = 24000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 262,
        Unknown_30              = 45,
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
        Unknown_00              = 21000,
        Unknown_04              = 0,
        Unknown_08              = 24000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 262,
        Unknown_30              = 45,
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
        'ED6_DT09/CH10100 ._CH',             # 00
        'ED6_DT09/CH10101 ._CH',             # 01
        'ED6_DT07/CH02480 ._CH',             # 02
        'ED6_DT07/CH01060 ._CH',             # 03
        'ED6_DT07/CH01070 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH00100 ._CH',             # 07
        'ED6_DT07/CH01710 ._CH',             # 08
        'ED6_DT07/CH00107 ._CH',             # 09
        'ED6_DT07/CH00102 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT09/CH10100P._CP',             # 00
        'ED6_DT09/CH10101P._CP',             # 01
        'ED6_DT07/CH02480P._CP',             # 02
        'ED6_DT07/CH01060P._CP',             # 03
        'ED6_DT07/CH01070P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH00100P._CP',             # 07
        'ED6_DT07/CH01710P._CP',             # 08
        'ED6_DT07/CH00107P._CP',             # 09
        'ED6_DT07/CH00102P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -75800,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1730,
        Z                   = 0,
        Y                   = 24300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1730,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -75800,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -75800,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39010,
        Z                   = 600,
        Y                   = 23300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 40980,
        Z                   = 600,
        Y                   = 23300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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

    DeclNpc(
        X                   = 23910,
        Z                   = 30,
        Y                   = 66820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 41200,
        Y                   = -500,
        Z                   = 21800,
        Range               = 48300,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x4FB0,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 34900,
        Y                   = -1000,
        Z                   = 33900,
        Range               = 43000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xAD70,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 38700,
        Y                   = -500,
        Z                   = 37000,
        Range               = 35200,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xB4DC,
        Unknown_18          = 0x0,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = 26000,
        Y                   = -500,
        Z                   = 26000,
        Range               = 19000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x7148,
        Unknown_18          = 0x0,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 42360,
        Y                   = -500,
        Z                   = 15300,
        Range               = 50900,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x490C,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 35830,
        Y                   = -1000,
        Z                   = 26140,
        Range               = 34270,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x5D2A,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 39000,
        Y                   = -500,
        Z                   = 42000,
        Range               = 1000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = 22700,
        Y                   = -500,
        Z                   = 25300,
        Range               = 1000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 46100,
        Y                   = -500,
        Z                   = 15200,
        Range               = 1000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 20,
    )


    ScpFunction(
        "Function_0_486",          # 00, 0
        "Function_1_552",          # 01, 1
        "Function_2_58D",          # 02, 2
        "Function_3_5A3",          # 03, 3
        "Function_4_5DE",          # 04, 4
        "Function_5_5E4",          # 05, 5
        "Function_6_5EA",          # 06, 6
        "Function_7_61D",          # 07, 7
        "Function_8_62C",          # 08, 8
        "Function_9_643",          # 09, 9
        "Function_10_857",         # 0A, 10
        "Function_11_861",         # 0B, 11
        "Function_12_92E",         # 0C, 12
        "Function_13_C37",         # 0D, 13
        "Function_14_F16",         # 0E, 14
        "Function_15_1178",        # 0F, 15
        "Function_16_119B",        # 10, 16
        "Function_17_11A3",        # 11, 17
        "Function_18_11B8",        # 12, 18
        "Function_19_11CC",        # 13, 19
        "Function_20_11E0",        # 14, 20
        "Function_21_11F4",        # 15, 21
        "Function_22_225A",        # 16, 22
        "Function_23_229E",        # 17, 23
        "Function_24_230E",        # 18, 24
        "Function_25_2323",        # 19, 25
        "Function_26_2338",        # 1A, 26
        "Function_27_234D",        # 1B, 27
        "Function_28_238A",        # 1C, 28
        "Function_29_2392",        # 1D, 29
        "Function_30_2424",        # 1E, 30
        "Function_31_24A2",        # 1F, 31
        "Function_32_2534",        # 20, 32
        "Function_33_2A62",        # 21, 33
        "Function_34_2A6A",        # 22, 34
    )


    def Function_0_486(): pass

    label("Function_0_486")

    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_END)), "loc_4C7")
    OP_A2(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 39000, 0, 42000, 270)
    OP_43(0x9, 0x3, 0x0, 0x2)

    label("loc_4C7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_4DB"),
        (102, "loc_53A"),
        (103, "loc_53A"),
        (SWITCH_DEFAULT, "loc_551"),
    )


    label("loc_4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A")
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    OP_6D(28000, 0, 41000, 0)
    OP_6C(200000, 0)
    OP_6B(5000, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    FadeToBright(3000, 0)
    Event(0, 6)
    Jump("loc_537")

    label("loc_52A")

    FadeToBright(3000, 0)
    Event(0, 9)

    label("loc_537")

    Jump("loc_551")

    label("loc_53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54E")
    Event(0, 14)

    label("loc_54E")

    Jump("loc_551")

    label("loc_551")

    Return()

    # Function_0_486 end

    def Function_1_552(): pass

    label("Function_1_552")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x393), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_570")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_570")

    OP_16(0x2, 0xFA0, 0xFFFE8518, 0xFFFE8900, 0x30004)
    OP_1B(0x4, 0x0, 0x22)
    OP_22(0x1CF, 0x0, 0x64)
    Return()

    # Function_1_552 end

    def Function_2_58D(): pass

    label("Function_2_58D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_58D")

    label("loc_5A2")

    Return()

    # Function_2_58D end

    def Function_3_5A3(): pass

    label("Function_3_5A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5DD")
    OP_95(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x258, 0x640)
    OP_95(0xFE, 0x3E8, 0x0, 0x0, 0x258, 0x640)
    Jump("Function_3_5A3")

    label("loc_5DD")

    Return()

    # Function_3_5A3 end

    def Function_4_5DE(): pass

    label("Function_4_5DE")

    OP_22(0x190, 0x0, 0x64)
    Return()

    # Function_4_5DE end

    def Function_5_5E4(): pass

    label("Function_5_5E4")

    OP_22(0x191, 0x0, 0x64)
    Return()

    # Function_5_5E4 end

    def Function_6_5EA(): pass

    label("Function_6_5EA")

    EventBegin(0x0)
    Sleep(500)
    OP_43(0x0, 0x2, 0x0, 0x8)
    OP_43(0x0, 0x1, 0x0, 0x7)
    OP_6C(225000, 9000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/T0411   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_6_5EA end

    def Function_7_61D(): pass

    label("Function_7_61D")

    Sleep(2000)
    OP_6B(3000, 9000)
    Return()

    # Function_7_61D end

    def Function_8_62C(): pass

    label("Function_8_62C")

    Sleep(2000)
    OP_6D(16700, 0, 18800, 9000)
    Return()

    # Function_8_62C end

    def Function_9_643(): pass

    label("Function_9_643")

    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    OP_6D(26700, 0, 14500, 0)
    OP_6C(225000, 0)
    OP_6B(3500, 0)
    SetChrPos(0x101, 28000, 0, 14200, 90)
    SetChrPos(0x102, 25350, 570, 15020, 90)
    EventBegin(0x0)
    OP_43(0x0, 0x1, 0x0, 0xA)
    OP_8E(0x102, 0x6E28, 0x0, 0x3C28, 0x5DC, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F哇～天色已经这么暗了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x1, 400)

    ChrTalk(
        0x101,
        (
            "#000F喂，约修亚。\x01",
            "该怎么巡逻比较好呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010F是呀……\x02\x03",
            "#010F屋子周围、田地里、牲口棚\x01",
            "和温室都要巡视一遍吧。\x02\x03",
            "#010F这样整个农场都能照顾到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，知道了。\x02\x03",
            "#001F好的～我们出发吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    Return()

    # Function_9_643 end

    def Function_10_857(): pass

    label("Function_10_857")

    OP_6B(3000, 4500)
    Return()

    # Function_10_857 end

    def Function_11_861(): pass

    label("Function_11_861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92D")
    OP_A2(0x231)
    OP_28(0x2, 0x1, 0x10)
    EventBegin(0x0)
    OP_6D(48090, 480, 19550, 3000)
    Fade(1000)
    SetChrPos(0x101, 43760, 280, 21120, 135)
    SetChrPos(0x102, 42420, 370, 21480, 135)
    OP_6D(43760, 280, 21120, 0)
    OP_6C(315000, 0)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)

    ChrTalk(
        0x101,
        "#000F……魔兽好像也不在这里。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是啊，到别的地方看看吧。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_92D")

    Return()

    # Function_11_861 end

    def Function_12_92E(): pass

    label("Function_12_92E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C36")
    OP_A2(0x233)
    OP_28(0x2, 0x1, 0x40)
    EventBegin(0x0)
    OP_6D(39020, -300, 38660, 2000)
    Fade(1000)
    SetChrPos(0x101, 42390, -40, 37580, 270)
    SetChrPos(0x102, 42500, 30, 38900, 270)
    OP_6D(40310, -300, 38250, 0)
    OP_6C(135000, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#000F#4P真安静啊～……\x01",
            "只能听到虫子的声音。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P看样子那些魔兽\x01",
            "还没有进入菜园里面。\x02\x03",
            "#010F是因为我们在巡逻吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#501F#4P对了，约修亚。\x01",
            "你小时候有没有听过这种说法？\x02\x03",
            "#501F就是说，\x01",
            "婴儿是从白菜地里长出来的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F#4P又突然说这些了……\x02\x03",
            "#010F我倒是听说过\x01",
            "是长着银色翅膀的天使送过来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#4P嗯……不同的地方说法也不同啊。\x02\x03",
            "#501F…………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P…………………………\x02\x03",
            "#010F我们继续巡逻吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#4P嗯。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_C36")

    Return()

    # Function_12_92E end

    def Function_13_C37(): pass

    label("Function_13_C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F15")
    OP_A2(0x233)
    OP_A2(0x234)
    OP_28(0x2, 0x1, 0x80)
    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrPos(0x9, 24900, 50, 30180, 86)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x3, 0x0, 0x2)

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 35400, 350, 25540, 267)
    SetChrPos(0x102, 35360, 340, 24500, 261)

    def lambda_CCC():

        label("loc_CCC")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_CCC")

    QueueWorkItem2(0x101, 1, lambda_CCC)

    def lambda_CDD():

        label("loc_CDD")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_CDD")

    QueueWorkItem2(0x102, 1, lambda_CDD)
    OP_0D()

    def lambda_CEF():
        OP_6D(34540, 80, 30070, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CEF)

    def lambda_D07():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D07)

    def lambda_D17():
        OP_8E(0x9, 0x8656, 0x46, 0x758A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D17)
    WaitChrThread(0x9, 0x1)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0x101, 200)
    Sleep(1000)
    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_22(0x194, 0x0, 0x64)

    ChrTalk(
        0x9,
        "咪呜！\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x9, 0xAF64, 0x118, 0x9042, 0x2EE0, 0x0)
    SetChrPos(0x9, 39000, 0, 42000, 270)

    ChrTalk(
        0x101,
        "#004F啊，逃跑了！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_8E(0x101, 0x89C6, 0x140, 0x6EAA, 0x1388, 0x0)
    OP_8C(0x101, 45, 400)
    OP_44(0x101, 0xFF)

    ChrTalk(
        0x101,
        "#005F喂！给我等一下！\x02",
    )

    CloseMessageWindow()
    OP_8E(0x102, 0x8994, 0x136, 0x68CE, 0x7D0, 0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F气息还没有消失……\x02\x03",
            "#012F那只魔兽应该还在菜园里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哼哼，正合我意……\x02\x03",
            "#005F绝对要抓住它！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_A2(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    Sleep(50)
    EventEnd(0x4)
    ClearMapFlags(0x400000)
    OP_43(0x9, 0x3, 0x0, 0x2)

    label("loc_F15")

    Return()

    # Function_13_C37 end

    def Function_14_F16(): pass

    label("Function_14_F16")

    OP_A2(0x233)
    OP_A2(0x234)
    OP_28(0x2, 0x1, 0x80)
    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrPos(0x9, 24100, 0, 54800, 0)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x3, 0x0, 0x2)
    OP_90(0x101, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x11)
    OP_43(0x102, 0x1, 0x0, 0x11)
    OP_43(0x9, 0x1, 0x0, 0xF)
    OP_8E(0x9, 0x5BCC, 0x0, 0x9C40, 0xBB8, 0x0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0x101, 200)
    Sleep(1000)
    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_22(0x194, 0x0, 0x64)

    ChrTalk(
        0x9,
        "咪呜！\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x10)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x9, 0x7148, 0x0, 0x7148, 0x2EE0, 0x0)
    SetChrPos(0x9, 39000, 0, 42000, 270)

    ChrTalk(
        0x101,
        "#004F啊，逃跑了！\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x55BE, 0x0, 0x98F8, 0x1388, 0x0)
    OP_8C(0x101, 135, 400)

    ChrTalk(
        0x101,
        "#005F喂！给我等一下！\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F气息还没有消失……\x02\x03",
            "#012F那只魔兽应该还在菜园里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哼哼，正合我意……\x02\x03",
            "#005F绝对要抓住它！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_A2(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    OP_43(0x9, 0x3, 0x0, 0x2)
    Return()

    # Function_14_F16 end

    def Function_15_1178(): pass

    label("Function_15_1178")

    OP_6D(24100, 0, 47800, 1000)
    OP_6D(23500, 0, 40000, 4000)
    Return()

    # Function_15_1178 end

    def Function_16_119B(): pass

    label("Function_16_119B")

    OP_69(0x101, 0x3E8)
    Return()

    # Function_16_119B end

    def Function_17_11A3(): pass

    label("Function_17_11A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11B7")
    TurnDirection(0xFE, 0x9, 0)
    OP_48()
    Jump("Function_17_11A3")

    label("loc_11B7")

    Return()

    # Function_17_11A3 end

    def Function_18_11B8(): pass

    label("Function_18_11B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11CB")
    Call(0, 21)
    Call(0, 29)

    label("loc_11CB")

    Return()

    # Function_18_11B8 end

    def Function_19_11CC(): pass

    label("Function_19_11CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11DF")
    Call(0, 21)
    Call(0, 30)

    label("loc_11DF")

    Return()

    # Function_19_11CC end

    def Function_20_11E0(): pass

    label("Function_20_11E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11F3")
    Call(0, 21)
    Call(0, 31)

    label("loc_11F3")

    Return()

    # Function_20_11E0 end

    def Function_21_11F4(): pass

    label("Function_21_11F4")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    TurnDirection(0x0, 0x9, 0)
    TurnDirection(0x1, 0x9, 0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0x194, 0x0, 0x64)
    OP_44(0x9, 0xFF)
    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    TurnDirection(0x9, 0x0, 400)

    ChrTalk(
        0x101,
        (
            "#006F太好了，终于抓住了！\x02\x03",
            "#006F这次一定要给你们点颜色看看！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F接下来才是动真格的。\x01",
            "切记不可疏忽大意啊！\x02",
        )
    )

    CloseMessageWindow()
    Battle(0x393, 0x0, 0x0, 0x2, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1310"),
        (3, "loc_1315"),
        (0, "loc_1316"),
        (SWITCH_DEFAULT, "loc_2259"),
    )


    label("loc_1310")

    OP_B4(0x0)
    Jump("loc_2259")

    label("loc_1315")

    Return()

    label("loc_1316")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x3, 0x0, 0x2)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x3, 0x0, 0x2)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x3, 0x0, 0x2)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xD, 0x80)
    OP_43(0xD, 0x3, 0x0, 0x2)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xE, 0x80)
    OP_43(0xE, 0x3, 0x0, 0x2)
    SetChrPos(0xC, 33150, 0, 16129, 225)
    SetChrPos(0xD, 33390, 0, 15210, 270)
    SetChrPos(0xE, 32990, 0, 14530, 315)
    SetChrPos(0x12, 29700, 0, 16600, 0)
    SetChrPos(0xF, 29000, 0, 14200, 0)
    SetChrPos(0x10, 28100, 0, 15300, 0)
    SetChrPos(0x13, 28300, 0, 16400, 0)
    SetChrPos(0x11, 29300, 0, 17100, 0)
    SetChrPos(0x101, 30920, 0, 15780, 270)
    SetChrPos(0x102, 30630, 0, 14650, 315)
    TurnDirection(0xF, 0xE, 0)
    TurnDirection(0x10, 0xD, 0)
    TurnDirection(0x11, 0xE, 0)
    TurnDirection(0x12, 0x101, 0)
    TurnDirection(0x13, 0x102, 0)
    OP_44(0x12, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_43(0x11, 0x3, 0x0, 0x17)
    OP_6D(30470, 0, 16280, 0)
    OP_6C(315000, 0)
    OP_6B(3000, 0)
    OP_6B(2800, 3000)
    OP_22(0x194, 0x0, 0x64)

    ChrTalk(
        0xC,
        "咪呜～～……\x02",
    )

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0x16)
    OP_22(0x194, 0x0, 0x64)

    ChrTalk(
        0xE,
        "咪～～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "哎呀，真不愧是游击士啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "这么轻松就把\x01",
            "这群敏捷的家伙抓住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#4P嘿嘿，过奖了。\x02\x03",
            "#000F话说回来，该怎么处理它们呢？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "『应该不会再做坏事了吧……』\x01",        # 0
            "『……非要把它们杀掉不可吗？』\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1688"),
        (1, "loc_188C"),
        (SWITCH_DEFAULT, "loc_1A26"),
    )


    label("loc_1688")


    ChrTalk(
        0x101,
        (
            "#000F#4P已经教训过它们了，\x01",
            "应该不会再做坏事了吧……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F#3P艾丝蒂尔……\x01",
            "你怎么能感情用事呢？\x02\x03",
            "#012F我们不是为了打倒魔兽而来的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#003F#4P可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#3P而且，我们这次是\x01",
            "代替父亲来执行任务的……\x02\x03",
            "#015F如果下次再出现同类的事件，\x01",
            "你打算怎么向协会交代？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#4P唔唔……\x01",
            "说的也是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A26")

    label("loc_188C")


    ChrTalk(
        0x101,
        "#003F#4P……非要把它们杀掉不可吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F#3P这当然无庸置疑了，艾丝蒂尔。\x01",
            "我们是为了打倒魔兽而来的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#003F#4P可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#3P游击士的使命\x01",
            "是保卫百姓、维护正义……\x02\x03",
            "#015F绝对不能存有同情魔兽的心态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#4P唔唔……\x01",
            "说的也是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A26")

    label("loc_1A26")


    ChrTalk(
        0xF,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "算了算了，\x01",
            "反正受害的只有我们家种的菜而已……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "就放了它们吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "反正它们已经得到应有的教训，\x01",
            "这件事就算了吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        "#501F#4P缇欧，阿姨……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x13, 400)

    ChrTalk(
        0x102,
        "#012F#3P但是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……我也反对杀掉它们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "它们虽然是魔兽，\x01",
            "却也和我们生活在同一片土地上啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "有时候还是要互相忍让的，\x01",
            "大家和睦相处不是很好吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "约修亚……\x01",
            "这次就放了它们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#3P……………………\x02\x03",
            "#010F……我明白了。\x02\x03",
            "#010F既然受害者都同意放过它们，\x01",
            "那我也没有反对的理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "真是抱歉，\x01",
            "还让你们特地来这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "我们以后也要加固栅栏，\x01",
            "想办法避免再遇到这样的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#4P那就这样决定了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(
        0x101,
        (
            "#006F就是这么回事，\x01",
            "你们还不感谢大家？\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x7AD0, 0x0, 0x3DA4, 0x7D0, 0x0)
    Sleep(100)
    SetChrFlags(0x101, 0x800)
    SetChrChipByIndex(0x101, 10)
    OP_22(0x1F4, 0x0, 0x64)
    OP_99(0x101, 0x0, 0xC, 0x7D0)
    OP_44(0x11, 0xFF)
    OP_44(0x10, 0xFF)

    ChrTalk(
        0x101,
        "#005F再有下次的话就送你们下地狱！\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0xC, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    TurnDirection(0xC, 0x101, 0)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0xD, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    TurnDirection(0xD, 0x101, 0)
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0xE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    TurnDirection(0xE, 0x101, 0)
    OP_22(0x194, 0x0, 0x64)

    ChrTalk(
        0xC,
        "咪嘎～～！！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A2(0x3)
    SetChrPos(0xC, 0, 0, 0, 0)
    SetChrPos(0x9, 33150, 0, 16129, 0)
    OP_22(0x81, 0x0, 0x64)
    OP_43(0x9, 0x1, 0x0, 0x18)
    Sleep(200)
    OP_43(0xB, 0x2, 0x0, 0x1B)
    SetChrPos(0xD, 0, 0, 0, 0)
    SetChrPos(0xA, 33390, 0, 15210, 0)
    OP_22(0x81, 0x0, 0x64)
    OP_43(0xA, 0x1, 0x0, 0x19)
    Sleep(200)
    SetChrPos(0xE, 0, 0, 0, 0)
    SetChrPos(0xB, 32990, 0, 14530, 0)
    OP_22(0x81, 0x0, 0x64)
    OP_43(0xB, 0x1, 0x0, 0x1A)
    Sleep(1000)
    OP_A3(0x3)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    TurnDirection(0x101, 0xB, 0)
    Sleep(2000)
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(
        0x12,
        (
            "好了，终于解决了。\x01",
            "已经这么晚了，都该睡了。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xF, 0x1, 0x0, 0x1C)
    OP_43(0x10, 0x1, 0x0, 0x1C)
    OP_43(0x11, 0x1, 0x0, 0x1C)
    OP_43(0x13, 0x1, 0x0, 0x1C)
    OP_44(0x101, 0xFF)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x800)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x10, 400)
    TurnDirection(0x102, 0x12, 400)

    ChrTalk(
        0x12,
        "你们也留下好好休息吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#4P好～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#3P又给你们添麻烦了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221E")
    OP_2B(0x2, 0x2)
    Jump("loc_222B")

    label("loc_221E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222B")
    OP_2B(0x2, 0x1)

    label("loc_222B")

    OP_A2(0x239)
    OP_28(0x2, 0x1, 0x800)
    OP_28(0x2, 0x1, 0x1000)
    OP_28(0x2, 0x4, 0x10)
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    NewScene("ED6_DT01/T0411   ._SN", 1, 0, 0)
    IdleLoop()

    label("loc_2259")

    Return()

    # Function_21_11F4 end

    def Function_22_225A(): pass

    label("Function_22_225A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229D")
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(2500)
    Jump("Function_22_225A")

    label("loc_229D")

    Return()

    # Function_22_225A end

    def Function_23_229E(): pass

    label("Function_23_229E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230D")
    Sleep(3000)
    OP_8F(0xFE, 0x733C, 0x0, 0x4394, 0x12C, 0x0)
    Sleep(2000)
    OP_8F(0xFE, 0x7274, 0x0, 0x42CC, 0x5DC, 0x0)
    Sleep(3000)
    OP_8F(0xFE, 0x72D8, 0x0, 0x4330, 0x12C, 0x0)
    Sleep(500)
    OP_8F(0xFE, 0x7274, 0x0, 0x42CC, 0x2BC, 0x0)
    Jump("Function_23_229E")

    label("loc_230D")

    Return()

    # Function_23_229E end

    def Function_24_230E(): pass

    label("Function_24_230E")

    OP_8E(0x9, 0x85AC, 0x32, 0x740E, 0x2EE0, 0x0)
    Return()

    # Function_24_230E end

    def Function_25_2323(): pass

    label("Function_25_2323")

    OP_8E(0xA, 0x85AC, 0x32, 0x740E, 0x2EE0, 0x0)
    Return()

    # Function_25_2323 end

    def Function_26_2338(): pass

    label("Function_26_2338")

    OP_8E(0xB, 0x85AC, 0x32, 0x740E, 0x2EE0, 0x0)
    Return()

    # Function_26_2338 end

    def Function_27_234D(): pass

    label("Function_27_234D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2389")
    TurnDirection(0xF, 0xA, 0)
    TurnDirection(0x10, 0xA, 0)
    TurnDirection(0x11, 0xA, 0)
    TurnDirection(0x12, 0xA, 0)
    TurnDirection(0x13, 0xA, 0)
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0x102, 0xA, 0)
    OP_48()
    Jump("Function_27_234D")

    label("loc_2389")

    Return()

    # Function_27_234D end

    def Function_28_238A(): pass

    label("Function_28_238A")

    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_28_238A end

    def Function_29_2392(): pass

    label("Function_29_2392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2423")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_A3(0x0)
    OP_A2(0x1)
    OP_A3(0x2)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_69(0x9, 0x1F4)
    OP_43(0x101, 0x1, 0x0, 0x11)
    OP_43(0x102, 0x1, 0x0, 0x11)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x9, 0xB1BC, 0x0, 0xB220, 0x2EE0, 0x0)
    OP_8E(0x9, 0xBB80, 0x0, 0xC738, 0x2EE0, 0x0)
    SetChrPos(0x9, 22700, 0, 25300, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Call(0, 32)

    label("loc_2423")

    Return()

    # Function_29_2392 end

    def Function_30_2424(): pass

    label("Function_30_2424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24A1")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A2(0x2)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_69(0x9, 0x1F4)
    OP_43(0x101, 0x1, 0x0, 0x11)
    OP_43(0x102, 0x1, 0x0, 0x11)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x9, 0x846C, 0x0, 0x3A98, 0x2EE0, 0x0)
    SetChrPos(0x9, 46100, 0, 15200, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Call(0, 32)

    label("loc_24A1")

    Return()

    # Function_30_2424 end

    def Function_31_24A2(): pass

    label("Function_31_24A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2533")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_A2(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_69(0x9, 0x1F4)
    OP_43(0x101, 0x1, 0x0, 0x11)
    OP_43(0x102, 0x1, 0x0, 0x11)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x9, 0xA4D8, 0x0, 0x2A94, 0x2EE0, 0x0)
    OP_8E(0x9, 0x927C, 0x0, 0x27D8, 0x2EE0, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    SetChrPos(0x9, 39000, 0, 42000, 270)
    Call(0, 32)

    label("loc_2533")

    Return()

    # Function_31_24A2 end

    def Function_32_2534(): pass

    label("Function_32_2534")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E0")

    ChrTalk(
        0x101,
        "#000F啊啊。又逃走了～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这么小的家伙，\x01",
            "逃跑起来动作也特别的灵活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好好想一下战斗的方法哦，艾丝蒂尔。（※仮）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A4C")

    label("loc_25E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 6)), scpexpr(EXPR_END)), "loc_26AC")
    OP_A2(0x237)
    OP_28(0x2, 0x1, 0x400)

    ChrTalk(
        0x101,
        "#007F啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F真可惜啊。\x02\x03",
            "#012F总之当它跳得起劲的时候\x01",
            "从背后靠近它，然后再去抓它。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4C")

    label("loc_26AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 5)), scpexpr(EXPR_END)), "loc_2991")
    OP_A2(0x236)
    OP_28(0x2, 0x1, 0x200)

    ChrTalk(
        0x101,
        (
            "#009F又、又逃走了！？\x02\x03",
            "#009F这家伙身子圆圆胖胖的，\x01",
            "怎么动作还这么灵活啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1, 0x0, 0)

    ChrTalk(
        0x102,
        (
            "#012F动作的确是很灵活，\x01",
            "而且反应也相当灵敏。\x02\x03",
            "#012F不过，掌握好时机就没问题了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x1, 500)
    ClearMapFlags(0x1)
    OP_51(0x17, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x17, 0x320)

    ChrTalk(
        0x101,
        "#004F掌握时机？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F看得出这种魔兽跳起来的时候\x01",
            "警戒性会相对减弱。\x02\x03",
            "#012F瞄准这个空档，然后从背后靠近它，\x01",
            "这样就应该可以抓住它了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F原来是这样啊……\x01",
            "当它跳得起劲的时候从背后靠近它对吧。\x02\x03",
            "#006F嗯，一定要试试看才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4C")

    label("loc_2991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_END)), "loc_2A4C")
    OP_A2(0x235)
    OP_28(0x2, 0x1, 0x100)

    ChrTalk(
        0x101,
        "#004F啊啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F真可惜，被它发现了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F唔～下次一定抓到你！\x02",
    )

    CloseMessageWindow()

    label("loc_2A4C")

    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x9, 0xFF)
    EventEnd(0x1)
    OP_43(0x9, 0x3, 0x0, 0x2)
    Return()

    # Function_32_2534 end

    def Function_33_2A62(): pass

    label("Function_33_2A62")

    OP_69(0x101, 0x3E8)
    Return()

    # Function_33_2A62 end

    def Function_34_2A6A(): pass

    label("Function_34_2A6A")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_END)), "loc_2B58")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE9")

    ChrTalk(
        0x102,
        (
            "#012F魔兽一定还在农场里面。\x01",
            "　\x02\x03",
            "我们还是不要去别的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B55")

    label("loc_2AE9")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F魔兽一定还在农场里面某个地方。\x01",
            "　\x02\x03",
            "我们还是回去巡逻吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B55")

    Jump("loc_2C08")

    label("loc_2B58")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BB6")

    ChrTalk(
        0x102,
        (
            "#012F这里是农场的出口……\x01",
            "我们要在农场里面巡逻才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C08")

    label("loc_2BB6")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F那里是农场的出口呢。\x01",
            "我们要在农场里面巡逻才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C08")

    OP_8E(0x0, 0x5E24, 0x14, 0xD1C4, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_34_2A6A end

    SaveToFile()

Try(main)
