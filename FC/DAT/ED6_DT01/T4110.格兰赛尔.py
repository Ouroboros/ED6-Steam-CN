from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4110   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4110.x',
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
        '芭蒂',                                 # 9
        '拉尔夫',                               # 10
        '比尔爷爷',                             # 11
        '伊鲁妮婆婆',                           # 12
        '菲利奥',                               # 13
        '拉科舒',                               # 14
        '丹克',                                 # 15
        '西加罗',                               # 16
        '艾德尔',                               # 17
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
        'ED6_DT07/CH01030 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01490 ._CH',             # 02
        'ED6_DT07/CH01180 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
        'ED6_DT07/CH01030 ._CH',             # 05
        'ED6_DT07/CH01460 ._CH',             # 06
        'ED6_DT07/CH01043 ._CH',             # 07
        'ED6_DT07/CH01210 ._CH',             # 08
        'ED6_DT07/CH01183 ._CH',             # 09
        'ED6_DT07/CH01033 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01030P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01490P._CP',             # 02
        'ED6_DT07/CH01180P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
        'ED6_DT07/CH01030P._CP',             # 05
        'ED6_DT07/CH01460P._CP',             # 06
        'ED6_DT07/CH01043P._CP',             # 07
        'ED6_DT07/CH01210P._CP',             # 08
        'ED6_DT07/CH01183P._CP',             # 09
        'ED6_DT07/CH01033P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 26550,
        Z                   = 0,
        Y                   = -2980,
        Direction           = 77,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 32860,
        Z                   = 100,
        Y                   = 1000,
        Direction           = 175,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 51890,
        Z                   = 0,
        Y                   = 56160,
        Direction           = 84,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 59860,
        Z                   = 0,
        Y                   = 58240,
        Direction           = 9,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 90200,
        Z                   = 0,
        Y                   = -2190,
        Direction           = 169,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 7200,
        Z                   = 200,
        Y                   = 53270,
        Direction           = 254,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 10450,
        Z                   = 0,
        Y                   = 53510,
        Direction           = 106,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    ScpFunction(
        "Function_0_222",          # 00, 0
        "Function_1_4E5",          # 01, 1
        "Function_2_532",          # 02, 2
        "Function_3_548",          # 03, 3
        "Function_4_56C",          # 04, 4
        "Function_5_590",          # 05, 5
        "Function_6_5B4",          # 06, 6
        "Function_7_F6E",          # 07, 7
        "Function_8_153F",         # 08, 8
        "Function_9_2496",         # 09, 9
        "Function_10_2B8A",        # 0A, 10
        "Function_11_32AA",        # 0B, 11
        "Function_12_38D6",        # 0C, 12
        "Function_13_3E3E",        # 0D, 13
        "Function_14_45CF",        # 0E, 14
    )


    def Function_0_222(): pass

    label("Function_0_222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_27D")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -28640, 0, 1890, 183)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32060, 0, -2000, 187)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_4E4")

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2C6")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -27680, 0, -3510, 10)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32060, 0, -2000, 187)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0x10, 0x80)
    Jump("loc_4E4")

    label("loc_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_30A")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -27310, 0, -4370, 81)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32060, 0, -2000, 187)
    OP_43(0x9, 0x0, 0x0, 0x3)
    Jump("loc_4E4")

    label("loc_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_364")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -27680, 0, -3510, 10)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -31960, 0, -1490, 135)
    OP_43(0x9, 0x0, 0x0, 0x2)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x10, 1950, 0, 56650, 90)
    Jump("loc_4E4")

    label("loc_364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_373")
    SetChrFlags(0x10, 0x80)
    Jump("loc_4E4")

    label("loc_373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3A2")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 10)
    SetChrPos(0x8, -28640, 150, 1890, 180)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    Jump("loc_4E4")

    label("loc_3A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3D3")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32060, 0, -2000, 187)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_4E4")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_424")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 10)
    SetChrPos(0x8, -28640, 150, 1890, 180)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30620, 0, -1960, 0)
    SetChrFlags(0x9, 0x10)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_4E4")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_450")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32060, 0, -2000, 187)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0x10, 0x80)
    Jump("loc_4E4")

    label("loc_450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4B4")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 10)
    SetChrPos(0x8, -28640, 150, 1890, 180)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32060, 0, -2000, 187)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xB, 9)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x4)
    OP_44(0xB, 0xFF)
    Jump("loc_4E4")

    label("loc_4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4E4")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32369, 0, 790, 0)
    SetChrChipByIndex(0xB, 9)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x4)
    OP_44(0xB, 0xFF)

    label("loc_4E4")

    Return()

    # Function_0_222 end

    def Function_1_4E5(): pass

    label("Function_1_4E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_518")
    OP_B1("t4110_y")
    Jump("loc_521")

    label("loc_518")

    OP_B1("t4110_n")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_531")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_531")

    Return()

    # Function_1_4E5 end

    def Function_2_532(): pass

    label("Function_2_532")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_547")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_532")

    label("loc_547")

    Return()

    # Function_2_532 end

    def Function_3_548(): pass

    label("Function_3_548")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56B")
    OP_8D(0xFE, -33020, -920, -30290, -3790, 4000)
    Jump("Function_3_548")

    label("loc_56B")

    Return()

    # Function_3_548 end

    def Function_4_56C(): pass

    label("Function_4_56C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58F")
    OP_8D(0xFE, 24820, -4110, 30930, -1350, 1800)
    Jump("Function_4_56C")

    label("loc_58F")

    Return()

    # Function_4_56C end

    def Function_5_590(): pass

    label("Function_5_590")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B3")
    OP_8D(0xFE, 89790, -700, 91780, -4740, 2000)
    Jump("Function_5_590")

    label("loc_5B3")

    Return()

    # Function_5_590 end

    def Function_6_5B4(): pass

    label("Function_6_5B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_681")

    ChrTalk(
        0xFE,
        (
            "在大主教的鼓励下，\x01",
            "我准备出一本书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要把在各地巡礼的\x01",
            "经验记录下来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6A")

    label("loc_681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6D1")

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "终于把家里打扫完毕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "我差不多该去大圣堂看看了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6A")

    label("loc_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_791")

    ChrTalk(
        0xFE,
        (
            "妻子总是早早就出门了，\x01",
            "早饭只好我来做了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "午饭各自解决，\x01",
            "晚饭的话则是谁到家早\x01",
            "就由谁来做。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6A")

    label("loc_791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_79B")
    Jump("loc_F6A")

    label("loc_79B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_821")

    ChrTalk(
        0xFE,
        (
            "今天是去大圣堂\x01",
            "祈祷的日子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要在中午之前\x01",
            "把家里收拾得干干净净才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6A")

    label("loc_821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_8D0")

    ChrTalk(
        0xFE,
        (
            "有的时候\x01",
            "我很羡慕妻子的生活方式呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她的这种洒脱\x01",
            "大概就是她的魅力所在。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BB")

    label("loc_8D0")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "悄悄告诉你啊，\x01",
            "有时候我很羡慕妻子的生活方式呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "我怎么都不能学会像她那样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她的这种洒脱\x01",
            "大概就是她的魅力所在。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BB")

    Jump("loc_F6A")

    label("loc_9BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9C8")
    Jump("loc_F6A")

    label("loc_9C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_A10")

    ChrTalk(
        0xFE,
        (
            "有个大款妻子\x01",
            "还真是辛苦啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2B")

    label("loc_A10")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "作为一个宗教信徒，\x01",
            "我希望妻子也能够花钱适度，\x01",
            "过有节制的生活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，巡礼所花的费用\x01",
            "妻子却全部替我掏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且我又\x01",
            "是个上门女婿，\x01",
            "面子上真有点挂不住啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉唉……\x02",
    )

    CloseMessageWindow()

    label("loc_B2B")

    Jump("loc_F6A")

    label("loc_B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BDB")

    ChrTalk(
        0xFE,
        (
            "妻子继承她父亲的事业\x01",
            "经营百货店，\x01",
            "已经赚了很多钱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "旅行结束之后，\x01",
            "今天立刻就开始\x01",
            "到店里去工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6A")

    label("loc_BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_EC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_CE3")

    ChrTalk(
        0xFE,
        (
            "分布在王国各地的七耀教会\x01",
            "在几百年前就已经存在了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了纪念大崩坏之后\x01",
            "引导人们的女神而在王国各地旅行，\x01",
            "的确非常的有意义啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC6")

    label("loc_CE3")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "分布在王国各地的七耀教会\x01",
            "在几百年前就已经存在了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了纪念大崩坏之后\x01",
            "引导人们的女神而在王国各地旅行，\x01",
            "的确非常的有意义啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我平日里就和忙碌的妻子\x01",
            "一起度过这些时光。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "日子虽然过得很平淡，\x01",
            "但是能够买到许多好东西，\x01",
            "妻子也很满足了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC6")

    Jump("loc_F6A")

    label("loc_EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_F6A")

    ChrTalk(
        0xFE,
        (
            "巡礼过王国所有的七耀教会之后，\x01",
            "我终于又回到了自己的家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好久没有去大圣堂看看了，\x01",
            "才发现来了一位新的修女。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6A")

    TalkEnd(0xFE)
    Return()

    # Function_6_5B4 end

    def Function_7_F6E(): pass

    label("Function_7_F6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_F7B")
    Jump("loc_153B")

    label("loc_F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_F85")
    Jump("loc_153B")

    label("loc_F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_FC6")

    ChrTalk(
        0xFE,
        (
            "那～么，\x01",
            "差不多该去店里上班了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_153B")

    label("loc_FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_102A")

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "老公还没有回来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么今天只好我来做饭了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_153B")

    label("loc_102A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1034")
    Jump("loc_153B")

    label("loc_1034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_11D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_10DD")

    ChrTalk(
        0xFE,
        (
            "丈夫要是能够\x01",
            "学会享受人生就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果这也不行，\x01",
            "那也不行的话，\x01",
            "会很没意思的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D4")

    label("loc_10DD")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "丈夫要是能够\x01",
            "学会享受人生就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果这也不行，\x01",
            "那也不行的话，\x01",
            "会很没意思的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过那股认真劲\x01",
            "也是他的优点呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D4")

    Jump("loc_153B")

    label("loc_11D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_11E1")
    Jump("loc_153B")

    label("loc_11E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1320")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_127D")

    ChrTalk(
        0xFE,
        (
            "因为呢，一回到王都，\x01",
            "自己就是经营百货店的店主，\x01",
            "所以购物的乐趣也享受不到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉呀，还是想出去旅行啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_131D")

    label("loc_127D")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "呼～工作得真辛苦啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，一回到王都，\x01",
            "自己就是经营百货店的店主，\x01",
            "所以购物的乐趣也享受不到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉呀，还是想出去旅行啊。\x02",
    )

    CloseMessageWindow()

    label("loc_131D")

    Jump("loc_153B")

    label("loc_1320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_132A")
    Jump("loc_153B")

    label("loc_132A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_13B8")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "明天开始要回去工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "武术大会和诞辰庆典\x01",
            "是绝好的赚钱机会哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_153B")

    label("loc_13B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_153B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1447")

    ChrTalk(
        0xFE,
        (
            "我丈夫很高兴能到各地的教会去礼拜，\x01",
            "而我也因为能在各地尽情购物而特别愉快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对夫妻而言，\x01",
            "是一次很有意义的旅行呢㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_153B")

    label("loc_1447")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "哈～太忙了太忙了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在旅行中买的东西\x01",
            "整理起来好费力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我丈夫很高兴能到各地的教会去，\x01",
            "而我也因为能在各地尽情购物而特别愉快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对夫妻而言，\x01",
            "是一次很有意义的旅行呢㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153B")

    TalkEnd(0xFE)
    Return()

    # Function_7_F6E end

    def Function_8_153F(): pass

    label("Function_8_153F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_16BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_15E8")

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀～～～\x01",
            "空港被封锁原来是\x01",
            "因为政变导致的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "诞辰庆典结束之后，\x01",
            "又要回去面对\x01",
            "像山一样多的工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16BA")

    label("loc_15E8")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀～～～\x01",
            "空港被封锁原来是\x01",
            "因为政变导致的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是托那些军人的福，\x01",
            "给我带来了这么多麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "诞辰庆典结束之后，\x01",
            "又要回去面对\x01",
            "像山一样多的工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BA")

    Jump("loc_2492")

    label("loc_16BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_185D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1773")

    ChrTalk(
        0xFE,
        (
            "那些吓人的黑衣士兵\x01",
            "究竟是什么来头！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大白天的\x01",
            "还在王都里面巡逻，\x01",
            "果然不对劲啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185A")

    label("loc_1773")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "那些吓人的黑衣士兵\x01",
            "究竟是什么来头！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "趾高气扬横行霸道，\x01",
            "太讨厌了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大白天的\x01",
            "还在王都里面巡逻，\x01",
            "果然不对劲啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185A")

    Jump("loc_2492")

    label("loc_185D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_193B")

    ChrTalk(
        0xFE,
        (
            "很多人好像还不知道\x01",
            "女王陛下身体欠佳，\x01",
            "为了诞辰庆典纷纷来到了王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果庆典中止的话，\x01",
            "他们肯定很不满吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A68")

    label("loc_193B")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "武术大会结束以后，\x01",
            "诞辰庆典终于就要临近了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很多人好像还不知道\x01",
            "女王陛下身体欠佳，\x01",
            "为了诞辰庆典纷纷来到了王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果庆典中止的话，\x01",
            "他们肯定很不满吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A68")

    Jump("loc_2492")

    label("loc_1A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1B66")

    ChrTalk(
        0xFE,
        (
            "公爵邀请了大会优胜者\x01",
            "去参加王城中的晚宴，\x01",
            "可是女王还在生病，这样好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公爵做的事\x01",
            "总是那么让人觉得不舒服。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2492")

    label("loc_1B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1CE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1BA9")

    ChrTalk(
        0xFE,
        (
            "希望一切都能\x01",
            "回复到正常状态就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE6")

    label("loc_1BA9")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "不单是港口，\x01",
            "现在连艾尔贝离宫都不能进入了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就连王城也禁止游客进入参观，\x01",
            "这是怎么搞的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在唯一积极的话题\x01",
            "就是武术大会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望一切都能\x01",
            "回复到正常状态就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE6")

    Jump("loc_2492")

    label("loc_1CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1F48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1DDE")

    ChrTalk(
        0xFE,
        (
            "诞辰庆典到来的时候估计封锁会解除，\x01",
            "但这样仍旧要无所事事一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "军队又不会在我\x01",
            "无事可做时给我发薪水，\x01",
            "真让人烦恼啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F45")

    label("loc_1DDE")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "军队加强了警戒，\x01",
            "这样看来港口的封锁\x01",
            "暂时是无法解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "诞辰庆典到来的时候估计封锁会解除，\x01",
            "但这样仍旧要无所事事一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "军队又不会在我\x01",
            "无事可做时给我发薪水，\x01",
            "真让人烦恼啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F45")

    Jump("loc_2492")

    label("loc_1F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2103")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2008")

    ChrTalk(
        0xFE,
        (
            "呼，港口解除封锁以后，\x01",
            "工作马上就会重新开始，\x01",
            "我只能在家里等着随时回到工作岗位。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "武术大会也去不成，\x01",
            "无聊得不行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2100")

    label("loc_2008")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "呼，港口解除封锁以后，\x01",
            "工作马上就会重新开始，\x01",
            "我只能在家里等着随时回到工作岗位。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "武术大会也去不成，\x01",
            "无聊得不行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "好想放假啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2100")

    Jump("loc_2492")

    label("loc_2103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_22D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_21C1")

    ChrTalk(
        0xFE,
        (
            "军方口中的恐怖分子\x01",
            "就是指亲卫队吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "让我说的话，\x01",
            "昨天参加比赛的\x01",
            "特务部队倒真的有点像坏人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D1")

    label("loc_21C1")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "军方口中的恐怖分子\x01",
            "就是指亲卫队吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "亲卫队虽说\x01",
            "有些刻板守旧，\x01",
            "但我不认为他们是坏人呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "让我说的话，\x01",
            "昨天参加比赛的\x01",
            "特务部队倒真的有点像坏人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D1")

    Jump("loc_2492")

    label("loc_22D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2376")

    ChrTalk(
        0xFE,
        (
            "希望王国军\x01",
            "早日从港口撤离。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从卢安来的船只\x01",
            "不能进入港口，\x01",
            "在湖面上进退两难。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2492")

    label("loc_2376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_244F")

    ChrTalk(
        0xFE,
        (
            "从卢安运来的货物\x01",
            "是要从格兰赛尔的\x01",
            "港口卸下来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，\x01",
            "现在王国军为了对付恐怖组织\x01",
            "而把港口封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这下我们的工作就不得不停滞了，\x01",
            "真是困扰啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2492")

    label("loc_244F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2492")

    ChrTalk(
        0xFE,
        (
            "呼，格兰赛尔港口的封锁\x01",
            "要到什么时候才结束啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2492")

    TalkEnd(0xFE)
    Return()

    # Function_8_153F end

    def Function_9_2496(): pass

    label("Function_9_2496")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_24A3")
    Jump("loc_2B86")

    label("loc_24A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2503")

    ChrTalk(
        0xFE,
        (
            "港口被封锁了，\x01",
            "我现在也没事可做了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "接下来该轮到什么地方遭殃了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_2503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2646")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2580")

    ChrTalk(
        0xFE,
        (
            "这儿附近有一间\x01",
            "在出售的房子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我这个家太小，\x01",
            "很想住到那边去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2643")

    label("loc_2580")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "这儿附近有一间\x01",
            "在出售的房子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我这个家太小，\x01",
            "很想住到那边去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "努力工作，再借点钱，\x01",
            "应该就可以了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2643")

    Jump("loc_2B86")

    label("loc_2646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_26DF")

    ChrTalk(
        0xFE,
        (
            "呀～\x01",
            "决赛真是十分精彩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明天开始要加油工作。\x01",
            "我感觉到活力\x01",
            "源源不断地涌上来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_26DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2794")

    ChrTalk(
        0xFE,
        (
            "今天我要和妻子\x01",
            "一起去看总决赛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以这个为起点，\x01",
            "从现在开始我要努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_2794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_288F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_280D")

    ChrTalk(
        0xFE,
        (
            "我和妻子约定，\x01",
            "以后少抽烟，赶快去找工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后，\x01",
            "妻子就允许我\x01",
            "去看武术大会了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_288C")

    label("loc_280D")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "我和妻子约定，\x01",
            "以后少抽烟，赶快去找工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后，\x01",
            "妻子就允许我\x01",
            "去看武术大会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既然这样，\x01",
            "我就要更加努力才行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_288C")

    Jump("loc_2B86")

    label("loc_288F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2938")

    ChrTalk(
        0xFE,
        "好，我也是个男人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我决定了，\x01",
            "要好好努力！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "认真去找工作吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_2938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_29B5")

    ChrTalk(
        0xFE,
        (
            "唔～这样下去的话\x01",
            "生活确实也会很辛苦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来想着一定\x01",
            "要去找工作的，\x01",
            "但不知不觉又被耽搁了下来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_29B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2A63")

    ChrTalk(
        0xFE,
        (
            "总算是搬到\x01",
            "向往已久的王都来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "诞辰庆典期间\x01",
            "一定要好好轻松一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_2A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2B0F")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "武术大会的门票也太贵了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且一点折扣都不打，\x01",
            "杜南公爵果然一点都不精明。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_2B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2B86")

    ChrTalk(
        0xFE,
        (
            "我们家是最近\x01",
            "才搬到格兰赛尔来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从孩提时代开始，\x01",
            "我就一直向往着能够\x01",
            "在华丽的王都生活。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B86")

    TalkEnd(0xFE)
    Return()

    # Function_9_2496 end

    def Function_10_2B8A(): pass

    label("Function_10_2B8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2B97")
    Jump("loc_32A6")

    label("loc_2B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2BEF")

    ChrTalk(
        0xFE,
        (
            "那些士兵究竟\x01",
            "要在街上呆到什么时候啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_2BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2E78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2CF8")

    ChrTalk(
        0xFE,
        (
            "之前还说\x01",
            "为了将来出生的孩子\x01",
            "要去买布娃娃回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "首先，还不知道宝宝\x01",
            "会是男孩还是女孩呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么就不能\x01",
            "先考虑一下再行动呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E75")

    label("loc_2CF8")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "刚刚出门没多久，\x01",
            "马上就跑回来了，\x01",
            "竟然说想买房子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明现在这间房子的\x01",
            "房租都没有付清，\x01",
            "竟然还去异想天开。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在那之前还是\x01",
            "快点找好工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉，前路漫漫……\x02",
    )

    CloseMessageWindow()

    label("loc_2E75")

    Jump("loc_32A6")

    label("loc_2E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2F48")

    ChrTalk(
        0xFE,
        (
            "作为去观看大会的条件，\x01",
            "他说会去找工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我担心他是否会\x01",
            "好好遵守诺言……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_2F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2F9E")

    ChrTalk(
        0xFE,
        (
            "现在想想的话，\x01",
            "我也已经很久没有和他约会了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_2F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_304E")

    ChrTalk(
        0xFE,
        (
            "最后还是我先开口\x01",
            "说了关于大会的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "我还是心太软了一些。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_304E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_30B4")

    ChrTalk(
        0xFE,
        "好，决定了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "必须要把我的想法\x01",
            "告诉他才行，\x01",
            "要好好和他谈谈。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_30B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3119")

    ChrTalk(
        0xFE,
        (
            "他这个人\x01",
            "确实是个懒鬼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是会变成那样\x01",
            "我也有责任，\x01",
            "是我太娇惯他了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_3119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_31F1")

    ChrTalk(
        0xFE,
        (
            "他完全没有打算\x01",
            "要去找点事情做，\x01",
            "哪怕『一点点』都没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "对这样的人是没什么指望了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_31F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3244")

    ChrTalk(
        0xFE,
        "真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "家里哪有那么多钱\x01",
            "去看武术大会啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_3244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_32A6")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "虽说能搬到憧憬已久的王都是很不错，\x01",
            "但我丈夫现在变得就知道游手好闲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32A6")

    TalkEnd(0xFE)
    Return()

    # Function_10_2B8A end

    def Function_11_32AA(): pass

    label("Function_11_32AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_32B7")
    Jump("loc_38D2")

    label("loc_32B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3308")

    ChrTalk(
        0xFE,
        (
            "今天的士兵\x01",
            "比平日多了不少……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好可怕……\x02",
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_3308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_338A")

    ChrTalk(
        0xFE,
        (
            "女王陛下不但是国家的支柱，\x01",
            "而且也是格兰赛尔市民的骄傲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真希望她能够早日康复。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_338A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_33F8")

    ChrTalk(
        0xFE,
        (
            "我啊～\x01",
            "太过专注于比赛了，\x01",
            "不由自主地就站了起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵呵，真是不好意思……\x02",
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_33F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3432")

    ChrTalk(
        0xFE,
        "呵呵呵，老头子啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "再等一下嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_3432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_349A")

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "今天的晚饭做什么好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "油炸土豆和\x01",
            "爆炒野生菌，\x01",
            "做哪一个呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_349A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3697")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3588")

    ChrTalk(
        0xFE,
        "说起来，那些人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像在昨天的\x01",
            "比赛中出场了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "记得好像还输给了\x01",
            "共和国的那个选手。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3694")

    label("loc_3588")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "今天一早就和老头子\x01",
            "去百货店采购了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没想到东西很沉，\x01",
            "正在发愁……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这时，\x01",
            "路过的一群围红头巾的小伙子\x01",
            "帮我们把东西全部抬回家了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3694")

    Jump("loc_38D2")

    label("loc_3697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3748")

    ChrTalk(
        0xFE,
        (
            "我们老俩口已经\x01",
            "从王城里得到了门票，\x01",
            "去看了比赛的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵呵，老头子他\x01",
            "就像小孩子一样欢呼雀跃……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_3748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_37B3")

    ChrTalk(
        0xFE,
        (
            "对了，午后还要出门，\x01",
            "得早点打扫完房间呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_37B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_386C")

    ChrTalk(
        0xFE,
        (
            "武术大会开始了，\x01",
            "人们的心情也一下子活跃起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "保持愉快的生活态度\x01",
            "才能够更加长寿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_386C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_38D2")

    ChrTalk(
        0xFE,
        "呼，外面好热闹啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说岁月不饶人，\x01",
            "但也会跟着兴奋起来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D2")

    TalkEnd(0xFE)
    Return()

    # Function_11_32AA end

    def Function_12_38D6(): pass

    label("Function_12_38D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_38E3")
    Jump("loc_3E3A")

    label("loc_38E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3911")

    ChrTalk(
        0xFE,
        (
            "总感觉\x01",
            "外面有些不大对劲……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_39CE")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "真是挂念女王陛下的病情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说我也很担心恐怖事件，\x01",
            "但更加希望陛下可以\x01",
            "健康长寿啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_39CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3A57")

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀～\x01",
            "比赛真的是很精彩呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我虽然不太懂武术，\x01",
            "看不明白那些招式，\x01",
            "不过也能乐在其中。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3AA7")

    ChrTalk(
        0xFE,
        (
            "老婆子，不快点的话，\x01",
            "就占不到好的位子了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3B03")

    ChrTalk(
        0xFE,
        (
            "老婆子做的饭我虽然吃了几十年，\x01",
            "但仍旧觉得是极品啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3BC3")

    ChrTalk(
        0xFE,
        (
            "我们上了年纪的人总爱对\x01",
            "年轻人的行为说三道四……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但回想一下，\x01",
            "我们年轻的时候，\x01",
            "也是经常被教训啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3C4B")

    ChrTalk(
        0xFE,
        "哎呀，愉快愉快。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们的孙子和其他孩子们\x01",
            "能够在这样一个和平的时代生活，\x01",
            "实在是幸福啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3C8A")

    ChrTalk(
        0xFE,
        (
            "早上好，\x01",
            "今天又是一个清爽的早晨呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3E3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D1E")

    ChrTalk(
        0xFE,
        (
            "我们这些老人\x01",
            "都是从呱呱坠地到现在\x01",
            "一直在格兰赛尔居住的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这条街道\x01",
            "还是没有变啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3D1E")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "听说女王陛下身体欠佳时，\x01",
            "大家的心情都很沉重，\x01",
            "到现在才稍微好一些了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们这些老人\x01",
            "都是从呱呱坠地到现在\x01",
            "一直在格兰赛尔居住的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这条街道\x01",
            "还是没有变啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E3A")

    TalkEnd(0xFE)
    Return()

    # Function_12_38D6 end

    def Function_13_3E3E(): pass

    label("Function_13_3E3E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3ED3")

    ChrTalk(
        0xFE,
        (
            "这起政变竟然是\x01",
            "理查德上校策划的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们一直都被\x01",
            "上校给欺骗了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CB")

    label("loc_3ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3F3C")

    ChrTalk(
        0xFE,
        (
            "一群黑衣士兵在外面警备着，\x01",
            "气氛似乎很不妙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "最好还是不要出去了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_45CB")

    label("loc_3F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3FCB")

    ChrTalk(
        0xFE,
        (
            "我简直难以相信恐怖事件\x01",
            "是亲卫队一手策划的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过既然是那位理查德上校说的，\x01",
            "那应该就是真的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CB")

    label("loc_3FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4205")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_40D2")

    ChrTalk(
        0xFE,
        (
            "比起我得不断地提醒她，\x01",
            "最好还是让她能\x01",
            "自觉去做家务……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "夫妻间的协调很难呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4202")

    label("loc_40D2")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "今天我妻子把\x01",
            "家务都做好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比起我得不断地提醒她，\x01",
            "最好还是让她能\x01",
            "自觉去做家务……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "夫妻间的协调很难呢。\x02",
    )

    CloseMessageWindow()

    label("loc_4202")

    Jump("loc_45CB")

    label("loc_4205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_420F")
    Jump("loc_45CB")

    label("loc_420F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4219")
    Jump("loc_45CB")

    label("loc_4219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_42FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_426B")

    ChrTalk(
        0xFE,
        (
            "为了以后不再吵架\x01",
            "也要好好做家务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F9")

    label("loc_426B")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "嗯，我下定决心了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明天一定要\x01",
            "把心里话告诉妻子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F9")

    Jump("loc_45CB")

    label("loc_42FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4336")

    ChrTalk(
        0xFE,
        (
            "请、请问，\x01",
            "晚饭准备得怎么样了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CB")

    label("loc_4336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_442B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4374")

    ChrTalk(
        0xFE,
        "我还是先做完扫除再说吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4428")

    label("loc_4374")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "今天我醒来时，\x01",
            "妻子就不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像是大清早就\x01",
            "跑到竞技场去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，都结婚五年了……\x01",
            "还为这种事情……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4428")

    Jump("loc_45CB")

    label("loc_442B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4578")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_44A9")

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "去看武术大会虽然没什么不好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过至少也要\x01",
            "分担一些家务啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4575")

    label("loc_44A9")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "去看武术大会虽然没什么不好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过至少也要\x01",
            "分担一些家务啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉唉……\x01",
            "和结婚前的约定截然不同啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4575")

    Jump("loc_45CB")

    label("loc_4578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_45CB")

    ChrTalk(
        0xFE,
        (
            "呼，妻子外出了，\x01",
            "可以好好地收拾一下房间了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45CB")

    TalkEnd(0xFE)
    Return()

    # Function_13_3E3E end

    def Function_14_45CF(): pass

    label("Function_14_45CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4667")

    ChrTalk(
        0xFE,
        (
            "虽然好久没见面了，\x01",
            "但科洛蒂娅公主的确\x01",
            "是成长了许多呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她是比杜南公爵要合适\x01",
            "１００００００００００倍的\x01",
            "王位继承者。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BDC")

    label("loc_4667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_46D0")

    ChrTalk(
        0xFE,
        (
            "无论哪里，到处都是士兵，\x01",
            "就像是在监视我们一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "感觉不太舒服啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BDC")

    label("loc_46D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4769")

    ChrTalk(
        0xFE,
        (
            "一般武术大会结束以后，\x01",
            "马上就要开始诞辰庆典的准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过，今年会怎么样呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BDC")

    label("loc_4769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4889")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_47B1")

    ChrTalk(
        0xFE,
        (
            "哈～\x01",
            "决赛真是眼花缭乱的攻防战呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4886")

    label("loc_47B1")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "哈～\x01",
            "决赛真是眼花缭乱的攻防战呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们是在非常好的\x01",
            "坐席看比赛的……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "而且我也更加明白\x01",
            "丈夫对我的爱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天是最美的一天啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4886")

    Jump("loc_4BDC")

    label("loc_4889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4893")
    Jump("loc_4BDC")

    label("loc_4893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4A44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_494D")

    ChrTalk(
        0xFE,
        (
            "因为上次没能占到好位子，\x01",
            "今天本打算熬夜排队的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "丈夫说很危险，\x01",
            "就去替我排队了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A41")

    label("loc_494D")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "因为上次没能占到好位子，\x01",
            "今天本打算熬夜排队的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "丈夫说很危险，\x01",
            "就去替我排队了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……啊、啊呀，作为男人，\x01",
            "同时作为丈夫，那样也是应该的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A41")

    Jump("loc_4BDC")

    label("loc_4A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4A4E")
    Jump("loc_4BDC")

    label("loc_4A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4B17")

    ChrTalk(
        0xFE,
        (
            "果然在那个时机\x01",
            "应该用射程远的导力枪牵制敌人，\x01",
            "然后对其进行斩击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "攻守的转换\x01",
            "还是不够协调啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BDC")

    label("loc_4B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4B21")
    Jump("loc_4BDC")

    label("loc_4B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4BD5")

    ChrTalk(
        0xFE,
        (
            "虽说是预选赛，\x01",
            "不过今天的比赛\x01",
            "每一场都很精彩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然就是要从预选赛开始\x01",
            "一场不漏地看啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BDC")

    label("loc_4BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4BDC")

    label("loc_4BDC")

    TalkEnd(0xFE)
    Return()

    # Function_14_45CF end

    SaveToFile()

Try(main)
