from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4105   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4105.x',
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
        '索菲娜',                               # 9
        '鲁特尔',                               # 10
        '菲丝',                                 # 11
        '卡鲁尼洛',                             # 12
        '蒂法露',                               # 13
        '修理员佩顿',                           # 14
        '王国军士兵',                           # 15
        '王国军士兵',                           # 16
        '王国军士兵',                           # 17
        '王国军士兵',                           # 18
        '特务兵',                               # 19
        '特务兵',                               # 20
        '特务兵',                               # 21
        '王国军士兵',                           # 22
        '菲',                                   # 23
        '鲁迪',                                 # 24
        '士兵布拉姆',                           # 25
        '王都格兰赛尔·东街区',                 # 26
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01540 ._CH',             # 02
        'ED6_DT07/CH01450 ._CH',             # 03
        'ED6_DT07/CH01550 ._CH',             # 04
        'ED6_DT07/CH01450 ._CH',             # 05
        'ED6_DT07/CH01640 ._CH',             # 06
        'ED6_DT07/CH01610 ._CH',             # 07
        'ED6_DT07/CH01500 ._CH',             # 08
        'ED6_DT07/CH01300 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01540P._CP',             # 02
        'ED6_DT07/CH01450P._CP',             # 03
        'ED6_DT07/CH01550P._CP',             # 04
        'ED6_DT07/CH01450P._CP',             # 05
        'ED6_DT07/CH01640P._CP',             # 06
        'ED6_DT07/CH01610P._CP',             # 07
        'ED6_DT07/CH01500P._CP',             # 08
        'ED6_DT07/CH01300P._CP',             # 09
    )

    DeclNpc(
        X                   = 56030,
        Z                   = 250,
        Y                   = 133380,
        Direction           = 258,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 77500,
        Z                   = 1500,
        Y                   = 142010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58770,
        Z                   = 250,
        Y                   = 137000,
        Direction           = 281,
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
        X                   = 93960,
        Z                   = 1500,
        Y                   = 144440,
        Direction           = 293,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 84910,
        Z                   = 1500,
        Y                   = 141950,
        Direction           = 187,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 67710,
        Z                   = -10000,
        Y                   = 159300,
        Direction           = 84,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 73000,
        Z                   = -9800,
        Y                   = 158970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 63050,
        Z                   = -3000,
        Y                   = 160490,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 63040,
        Z                   = -3000,
        Y                   = 159620,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 73620,
        Z                   = 1500,
        Y                   = 143000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 63050,
        Z                   = -3000,
        Y                   = 160490,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 63040,
        Z                   = -3000,
        Y                   = 159620,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 73620,
        Z                   = 1500,
        Y                   = 143000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 72120,
        Z                   = -9800,
        Y                   = 158930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 72480,
        Z                   = -10000,
        Y                   = 169900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 72480,
        Z                   = -10000,
        Y                   = 170720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 72480,
        Z                   = -10000,
        Y                   = 170720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 51050,
        Z                   = 0,
        Y                   = 83440,
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


    DeclActor(
        TriggerX            = 56800,
        TriggerZ            = 250,
        TriggerY            = 136940,
        TriggerRange        = 800,
        ActorX              = 58770,
        ActorZ              = 1750,
        ActorY              = 137000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53710,
        TriggerZ            = 250,
        TriggerY            = 137720,
        TriggerRange        = 800,
        ActorX              = 53710,
        ActorZ              = 2450,
        ActorY              = 137720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71160,
        TriggerZ            = -10000,
        TriggerY            = 151550,
        TriggerRange        = 800,
        ActorX              = 71160,
        ActorZ              = -8500,
        ActorY              = 151550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3A6",          # 00, 0
        "Function_1_563",          # 01, 1
        "Function_2_689",          # 02, 2
        "Function_3_806",          # 03, 3
        "Function_4_82A",          # 04, 4
        "Function_5_ECF",          # 05, 5
        "Function_6_174E",         # 06, 6
        "Function_7_1FDF",         # 07, 7
        "Function_8_1FE4",         # 08, 8
        "Function_9_28E8",         # 09, 9
        "Function_10_2AED",        # 0A, 10
        "Function_11_2C86",        # 0B, 11
        "Function_12_3179",        # 0C, 12
        "Function_13_320E",        # 0D, 13
        "Function_14_32B2",        # 0E, 14
        "Function_15_332A",        # 0F, 15
        "Function_16_3350",        # 10, 16
        "Function_17_33CD",        # 11, 17
        "Function_18_3448",        # 12, 18
        "Function_19_35BF",        # 13, 19
        "Function_20_377C",        # 14, 20
        "Function_21_3A9B",        # 15, 21
        "Function_22_3B70",        # 16, 22
    )


    def Function_0_3A6(): pass

    label("Function_0_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3E8")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xD, 73000, -9800, 158970, 270)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_3E0")
    ClearChrFlags(0x18, 0x80)
    Jump("loc_3E5")

    label("loc_3E0")

    ClearChrFlags(0x17, 0x80)

    label("loc_3E5")

    Jump("loc_562")

    label("loc_3E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_432")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xB, 68580, 250, 147780, 45)
    SetChrPos(0xC, 66400, 0, 145250, 135)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_562")

    label("loc_432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_477")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xB, 68580, 250, 147780, 45)
    SetChrPos(0xC, 66400, 0, 145250, 135)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_562")

    label("loc_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4A3")
    SetChrPos(0xC, 66860, 250, 147300, 90)
    SetChrPos(0xD, 68610, 250, 147270, 270)
    Jump("loc_562")

    label("loc_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4BE")
    SetChrPos(0xD, 68470, 250, 147030, 90)
    Jump("loc_562")

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrPos(0xC, 77380, 1500, 144440, 270)
    SetChrPos(0xD, 76010, 1500, 144460, 90)
    Jump("loc_562")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_505")
    SetChrPos(0xB, 83030, 1700, 141250, 180)
    Jump("loc_562")

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_520")
    SetChrPos(0xB, 83030, 1700, 141250, 180)
    Jump("loc_562")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_540")
    SetChrPos(0xB, 83030, 1700, 141250, 180)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_562")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_55B")
    SetChrPos(0xB, 83030, 1700, 141250, 180)
    Jump("loc_562")

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_562")

    label("loc_562")

    Return()

    # Function_0_3A6 end

    def Function_1_563(): pass

    label("Function_1_563")

    OP_16(0x2, 0xFA0, 0xFFFF5808, 0x7148, 0x3005F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_605")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B5")
    OP_B1("t4105_y0")
    Jump("loc_602")

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CE")
    OP_B1("t4105_y1")
    Jump("loc_602")

    label("loc_5CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E7")
    OP_B1("t4105_y2")
    Jump("loc_602")

    label("loc_5E7")

    OP_B1("t4105_y0")
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_6F(0x5, 100)

    label("loc_602")

    Jump("loc_667")

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61D")
    OP_B1("t4105_0")
    Jump("loc_667")

    label("loc_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_635")
    OP_B1("t4105_1")
    Jump("loc_667")

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64D")
    OP_B1("t4105_2")
    Jump("loc_667")

    label("loc_64D")

    OP_B1("t4105_0")
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_6F(0x5, 100)

    label("loc_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_677")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_688")
    OP_72(0x6, 0x10)

    label("loc_688")

    Return()

    # Function_1_563 end

    def Function_2_689(): pass

    label("Function_2_689")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AE")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_7F0")

    label("loc_6AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C7")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_7F0")

    label("loc_6C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E0")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_7F0")

    label("loc_6E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F9")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_7F0")

    label("loc_6F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_712")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_7F0")

    label("loc_712")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_7F0")

    label("loc_72B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_744")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_7F0")

    label("loc_744")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75D")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_7F0")

    label("loc_75D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_776")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_7F0")

    label("loc_776")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78F")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_7F0")

    label("loc_78F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A8")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_7F0")

    label("loc_7A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C1")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_7F0")

    label("loc_7C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DA")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_7F0")

    label("loc_7DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F0")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_7F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_805")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7F0")

    label("loc_805")

    Return()

    # Function_2_689 end

    def Function_3_806(): pass

    label("Function_3_806")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_829")
    OP_8D(0xFE, 52840, 136880, 55890, 126400, 3000)
    Jump("Function_3_806")

    label("loc_829")

    Return()

    # Function_3_806 end

    def Function_4_82A(): pass

    label("Function_4_82A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_896")

    ChrTalk(
        0xFE,
        (
            "定期船总算可以\x01",
            "正常地航行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为维修主任的我\x01",
            "从现在开始也要更加努力才行啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_949")

    ChrTalk(
        0xFE,
        (
            "代替王国军士兵的\x01",
            "黑衣士兵来站岗了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "与之前的士兵相比\x01",
            "有一种恐怖的威慑力……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_9ED")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "军方把我的工作地点封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在定期船\x01",
            "也不能运行了，\x01",
            "究竟会怎样呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_9ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_A54")

    ChrTalk(
        0xFE,
        (
            "呼，今天总算是\x01",
            "按原定计划送走定期船了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要是总能这样就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_A9D")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "预定今天抵达的定期船终于要来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_B48")

    ChrTalk(
        0xFE,
        (
            "『埃尔赛尤号』是\x01",
            "技术部全体人员憧憬的目标。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "什么时候我也能\x01",
            "在那上面工作呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C2E")

    ChrTalk(
        0xFE,
        (
            "嗯，这样一来，\x01",
            "修理就应该全部完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为不知道飞船\x01",
            "什么时候才会进港，\x01",
            "所以比平时辛苦许多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CBE")

    ChrTalk(
        0xFE,
        (
            "原定的『赛希莉亚号』还没抵达，\x01",
            "军队的警备飞艇却突然进港了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "『赛希莉亚号』\x01",
            "在今天内能到达吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_D1A")

    ChrTalk(
        0xFE,
        "怎么回事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "定期船一点都没有要到达的迹象。\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_D71")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "机体部分的检查完成了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔，接下来要检查的项目是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_ECB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E15")

    ChrTalk(
        0xFE,
        (
            "自从我当上维修主任以来，\x01",
            "发生了许多事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "像是空贼事件，\x01",
            "还有这次的恐怖事件……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_E15")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "自从我当上维修主任以来，\x01",
            "发生了许多事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "像是空贼事件，\x01",
            "还有这次的恐怖事件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是不吉利啊。\x02",
    )

    CloseMessageWindow()

    label("loc_ECB")

    TalkEnd(0xFE)
    Return()

    # Function_4_82A end

    def Function_5_ECF(): pass

    label("Function_5_ECF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_F46")

    ChrTalk(
        0xFE,
        (
            "这下终于\x01",
            "可以回到工作岗位了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了能取回客人们的信赖，\x01",
            "一定要加油干才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174A")

    label("loc_F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_FC4")

    ChrTalk(
        0xFE,
        (
            "军队的那些家伙\x01",
            "该知道适可而止了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "早点滚出这里。\x02",
    )

    CloseMessageWindow()
    Jump("loc_174A")

    label("loc_FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_10D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1004")

    ChrTalk(
        0xFE,
        "哎…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "佩顿师傅到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D5")

    label("loc_1004")

    OP_A2(0x4)
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "啊～气死人了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "都这么久了，\x01",
            "还没抓到那些恐怖分子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "什么嘛，我受够了……\x02",
    )

    CloseMessageWindow()

    label("loc_10D5")

    Jump("loc_174A")

    label("loc_10D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1169")

    ChrTalk(
        0xFE,
        (
            "不愧是蔡斯的\x01",
            "中央工房那里\x01",
            "派来的佩顿师傅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是能做我们的\x01",
            "技术顾问就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174A")

    label("loc_1169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_11C8")

    ChrTalk(
        0xFE,
        "好了，『赛希莉亚号』就要抵达了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要预先做好准备才行。\x02",
    )

    CloseMessageWindow()
    Jump("loc_174A")

    label("loc_11C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1339")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1260")

    ChrTalk(
        0xFE,
        (
            "军队的那些家伙\x01",
            "能不能赶快离开啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "又不能给我们工作帮忙，\x01",
            "就会来打扰！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1336")

    label("loc_1260")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "我向佩顿师傅询问过很多\x01",
            "有关『埃尔赛尤号』的情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然还未完成，\x01",
            "但却是一艘很棒的飞艇呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有那些军人的话，\x01",
            "我就能到飞艇里面去参观一下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1336")

    Jump("loc_174A")

    label("loc_1339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_13F3")

    ChrTalk(
        0xFE,
        (
            "就算定期船再怎么延误，\x01",
            "我们要做的也只有一件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那就是全力保证\x01",
            "飞艇和乘客的安全。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174A")

    label("loc_13F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_155E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_14AC")

    ChrTalk(
        0xFE,
        (
            "那个女性军官的态度，\x01",
            "也太蛮不讲理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对本来就过于软弱的主任，\x01",
            "她更是变本加厉的蛮横。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155B")

    label("loc_14AC")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "那个女性军官的态度，\x01",
            "好像自以为有多了不起似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么蛮不讲理，我也只有忍了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但对本来就过于软弱的主任，\x01",
            "她更是变本加厉的蛮横。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_155B")

    Jump("loc_174A")

    label("loc_155E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_15E3")

    ChrTalk(
        0xFE,
        "还没来啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不会又卷入\x01",
            "什么事件了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174A")

    label("loc_15E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1651")

    ChrTalk(
        0xFE,
        "发动机部分没有异常。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "导力压调整完毕，\x01",
            "分配给我的部分已经全部完成。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174A")

    label("loc_1651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_174A")

    ChrTalk(
        0xFE,
        (
            "说实话，新来的维修主任的\x01",
            "技术和态度都不太可靠。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望他能作为一个男人\x01",
            "再好好地加把劲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174A")

    TalkEnd(0xFE)
    Return()

    # Function_5_ECF end

    def Function_6_174E(): pass

    label("Function_6_174E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_18E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_17F1")

    ChrTalk(
        0xFE,
        (
            "终于看到让『埃尔赛尤号』\x01",
            "再次试飞的希望了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "拉赛尔博士现在也没事了，\x01",
            "这个项目也就可以\x01",
            "向前跨一大步了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E3")

    label("loc_17F1")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "终于看到让『埃尔赛尤号』\x01",
            "再次试飞的希望了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "中央工房的新型引擎开发\x01",
            "也得加快速度才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "拉赛尔博士现在也没事了，\x01",
            "这个项目也就可以\x01",
            "向前跨一大步了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好～的，加油干～！\x02",
    )

    CloseMessageWindow()

    label("loc_18E3")

    Jump("loc_1FDB")

    label("loc_18E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_18F0")
    Jump("loc_1FDB")

    label("loc_18F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_18FA")
    Jump("loc_1FDB")

    label("loc_18FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1936")

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "年轻人就是有热情呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDB")

    label("loc_1936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1B72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1A37")

    ChrTalk(
        0xFE,
        (
            "（我听中央工房的同事说，\x01",
            "　拉赛尔博士好像被\x01",
            "　不知道什么人绑架走了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "（不过，我觉得\x01",
            "　博士一定会平安无事逃走，\x01",
            "　然后回到工房来的。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6F")

    label("loc_1A37")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "我在这里小声告诉你哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "（我听中央工房的同事说，\x01",
            "　拉赛尔博士好像被\x01",
            "　不知道什么人绑架走了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "（而且听说提妲也在一起，\x01",
            "　我真是有些担心呢……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "（不过，我觉得\x01",
            "　博士一定会平安无事逃走，\x01",
            "　然后回到工房来的。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6F")

    Jump("loc_1FDB")

    label("loc_1B72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1C46")

    ChrTalk(
        0xFE,
        (
            "憋了一肚子的火\x01",
            "就要爆发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好想快点继续进行\x01",
            "『埃尔赛尤号』的测试工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDB")

    label("loc_1C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1C9C")

    ChrTalk(
        0xFE,
        (
            "唔～反正我很无聊，\x01",
            "『林德号』的检修工作\x01",
            "我也去帮帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDB")

    label("loc_1C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D48")

    ChrTalk(
        0xFE,
        (
            "那艘警备飞艇是最近\x01",
            "才归雷斯顿要塞所有的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这个时候来到这里，\x01",
            "难道发生了什么事件吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDB")

    label("loc_1D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1DFC")

    ChrTalk(
        0xFE,
        (
            "『埃尔赛尤号』\x01",
            "现在还处于未完工状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来很快就要\x01",
            "进行下一轮测试的，\x01",
            "但现在这种状况……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDB")

    label("loc_1DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1E85")

    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "我有些担心尤莉亚中尉他们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说是由她发动了政变什么的，\x01",
            "肯定是哪里搞错了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDB")

    label("loc_1E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1FDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1F13")

    ChrTalk(
        0xFE,
        (
            "『埃尔赛尤号』\x01",
            "是王家所拥有的高速飞船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "也不应该由王国军来保管。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDB")

    label("loc_1F13")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "『埃尔赛尤号』\x01",
            "是王家所拥有的高速飞船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "也不应该由王国军来保管。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这真的是经过了\x01",
            "女王陛下许可的吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FDB")

    TalkEnd(0xFE)
    Return()

    # Function_6_174E end

    def Function_7_1FDF(): pass

    label("Function_7_1FDF")

    Call(0, 8)
    Return()

    # Function_7_1FDF end

    def Function_8_1FE4(): pass

    label("Function_8_1FE4")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2061")

    ChrTalk(
        0xA,
        (
            "在不知不觉中，\x01",
            "我们就被卷入了\x01",
            "这次政变活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "真是太令人惊讶了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28E4")

    label("loc_2061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_20B1")

    ChrTalk(
        0xA,
        (
            "唉，究竟要到何时\x01",
            "才能正常开工啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E4")

    label("loc_20B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_227A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2182")

    ChrTalk(
        0xA,
        (
            "因为今天王国军要\x01",
            "搜捕恐怖分子，\x01",
            "航运全部中止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我可以为您\x01",
            "办理退票手续。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2277")

    label("loc_2182")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        "非常抱歉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "因为今天王国军要\x01",
            "搜捕恐怖分子，\x01",
            "航运全部中止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我可以为您\x01",
            "办理退票手续。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2277")

    Jump("loc_28E4")

    label("loc_227A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_22D2")

    ChrTalk(
        0xA,
        (
            "呼，\x01",
            "明天定期船要是也能这样\x01",
            "按原定计划起航就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E4")

    label("loc_22D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_237B")

    ChrTalk(
        0xA,
        (
            "每次定期船延时到达，\x01",
            "我都想到柏斯那件空贼事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这样的惯性思维真不好啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28E4")

    label("loc_237B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_245C")

    ChrTalk(
        0xA,
        (
            "最近一段时间\x01",
            "王国军频繁地\x01",
            "在这附近巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "这段时间发生了不少事，\x01",
            "让人有些不安呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E4")

    label("loc_245C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_24F2")

    ChrTalk(
        0xA,
        (
            "现在，停在港里的定期船\x01",
            "是去往洛连特方向的『林德号』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "要乘坐的客人\x01",
            "请前往普通登机口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E4")

    label("loc_24F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2578")

    ChrTalk(
        0xA,
        (
            "因为王国军飞艇要出入港的关系，\x01",
            "今天的定期船航班\x01",
            "出发和到达时间又要推迟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "真叫人难办啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_28E4")

    label("loc_2578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_26AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25EB")

    ChrTalk(
        0xA,
        (
            "奇怪了啊。\x01",
            "『林德号』到现在都还没有抵达。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "今天明明可以\x01",
            "按时到达这里的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A8")

    label("loc_25EB")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "奇怪了啊。\x01",
            "『林德号』到现在都还没有抵达。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "今天明明可以\x01",
            "按时到达这里的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "我该怎么向旅客说明呢。\x02",
    )

    CloseMessageWindow()

    label("loc_26A8")

    Jump("loc_28E4")

    label("loc_26AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2711")

    ChrTalk(
        0xA,
        (
            "预定中午到达的『赛希莉亚号』\x01",
            "现在终于抵达了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E4")

    label("loc_2711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_28E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27D1")

    ChrTalk(
        0xA,
        (
            "因为王国军要盘查的缘故，\x01",
            "所以出发和到达的时间都大幅度推迟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "飞船一旦到达了，\x01",
            "我就会通知你们搭乘的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E4")

    label("loc_27D1")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "让你们久等了，\x01",
            "实在很抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "因为王国军要盘查的缘故，\x01",
            "所以出发和到达的时间都大幅度推迟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "飞船一旦到达了，\x01",
            "我就会通知你们搭乘的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E4")

    TalkEnd(0xA)
    Return()

    # Function_8_1FE4 end

    def Function_9_28E8(): pass

    label("Function_9_28E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_28F5")
    Jump("loc_2AE9")

    label("loc_28F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_28FF")
    Jump("loc_2AE9")

    label("loc_28FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2909")
    Jump("loc_2AE9")

    label("loc_2909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2913")
    Jump("loc_2AE9")

    label("loc_2913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_291D")
    Jump("loc_2AE9")

    label("loc_291D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2927")
    Jump("loc_2AE9")

    label("loc_2927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2931")
    Jump("loc_2AE9")

    label("loc_2931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_293B")
    Jump("loc_2AE9")

    label("loc_293B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2AD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_29CB")

    ChrTalk(
        0xFE,
        (
            "我本来是来公社\x01",
            "推销新型飞船的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过这里异常的忙乱，\x01",
            "看来我来得不是时候……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD5")

    label("loc_29CB")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "我本来是来公社\x01",
            "推销新型飞船的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过这里异常的忙乱，\x01",
            "看来我来得不是时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且我有些担心\x01",
            "新型引擎的研发计划，\x01",
            "还是先回蔡斯一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD5")

    Jump("loc_2AE9")

    label("loc_2AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2AE2")
    Jump("loc_2AE9")

    label("loc_2AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2AE9")

    label("loc_2AE9")

    TalkEnd(0xFE)
    Return()

    # Function_9_28E8 end

    def Function_10_2AED(): pass

    label("Function_10_2AED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2B5A")

    ChrTalk(
        0xFE,
        (
            "定期船现在终于\x01",
            "可以正常航行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来我就\x01",
            "可以回柏斯去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C82")

    label("loc_2B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2BAF")

    ChrTalk(
        0xFE,
        (
            "既然不能乘坐定期船，\x01",
            "至少也得和家里取得联络才行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C82")

    label("loc_2BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2C35")

    ChrTalk(
        0xFE,
        (
            "空港好像被\x01",
            "王国军给封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真糟糕啊。\x01",
            "怎么会这样呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C82")

    label("loc_2C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2C3F")
    Jump("loc_2C82")

    label("loc_2C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2C49")
    Jump("loc_2C82")

    label("loc_2C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2C53")
    Jump("loc_2C82")

    label("loc_2C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2C5D")
    Jump("loc_2C82")

    label("loc_2C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C67")
    Jump("loc_2C82")

    label("loc_2C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2C71")
    Jump("loc_2C82")

    label("loc_2C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2C7B")
    Jump("loc_2C82")

    label("loc_2C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2C82")

    label("loc_2C82")

    TalkEnd(0xFE)
    Return()

    # Function_10_2AED end

    def Function_11_2C86(): pass

    label("Function_11_2C86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2C93")
    Jump("loc_3175")

    label("loc_2C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2C9D")
    Jump("loc_3175")

    label("loc_2C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2CA7")
    Jump("loc_3175")

    label("loc_2CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2DB1")

    ChrTalk(
        0xFE,
        (
            "有谣言说\x01",
            "亲卫队的残党们\x01",
            "已经潜入王都了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然已经严密警戒，\x01",
            "可一个人也抓不到啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只能认为是有人把他们藏起来了。\x01",
            "我想你也有同感吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3175")

    label("loc_2DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2E57")

    ChrTalk(
        0xFE,
        (
            "呼～好困啊。\x01",
            "交班时间早点来就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "照这个样子看来，\x01",
            "今年是没法去观看武术大会了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3175")

    label("loc_2E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2F10")

    ChrTalk(
        0xFE,
        (
            "从今天开始似乎要\x01",
            "加强市内的警戒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来真的是想要把\x01",
            "亲卫队的残余分子揪出来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3175")

    label("loc_2F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2F67")

    ChrTalk(
        0xFE,
        (
            "亲卫队的那些人\x01",
            "要是突然改变主意\x01",
            "恐怖事件呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3175")

    label("loc_2F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2FB1")

    ChrTalk(
        0xFE,
        "那艘飞艇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是谁从要塞来了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3175")

    label("loc_2FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3060")

    ChrTalk(
        0xFE,
        (
            "因为是最新的机型，\x01",
            "如果被逃窜中的亲卫队员\x01",
            "夺走了就麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以很抱歉，\x01",
            "无论是谁都不许接近这艘飞艇。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3175")

    label("loc_3060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_310F")

    ChrTalk(
        0xFE,
        (
            "因为是最新的机型，\x01",
            "如果被逃窜中的亲卫队员\x01",
            "夺走了就麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以很抱歉，\x01",
            "无论是谁都不许接近这艘飞艇。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3175")

    label("loc_310F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3175")

    ChrTalk(
        0xFE,
        "『埃尔赛尤号』现由王国军保管。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "普通群众不得接近。\x02",
    )

    CloseMessageWindow()

    label("loc_3175")

    TalkEnd(0xFE)
    Return()

    # Function_11_2C86 end

    def Function_12_3179(): pass

    label("Function_12_3179")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3186")
    Jump("loc_320A")

    label("loc_3186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3190")
    Jump("loc_320A")

    label("loc_3190")


    ChrTalk(
        0xFE,
        (
            "很抱歉，就算是游击士，\x01",
            "现在也不能予以信任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好了，你们快走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_320A")

    TalkEnd(0xFE)
    Return()

    # Function_12_3179 end

    def Function_13_320E(): pass

    label("Function_13_320E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_321B")
    Jump("loc_32AE")

    label("loc_321B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3225")
    Jump("loc_32AE")

    label("loc_3225")


    ChrTalk(
        0xFE,
        (
            "平民应该没有什么事情\x01",
            "要到这里来办吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "老是在这里晃悠干吗？\x01",
            "是要我们抓你们去问话吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32AE")

    TalkEnd(0xFE)
    Return()

    # Function_13_320E end

    def Function_14_32B2(): pass

    label("Function_14_32B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_32BF")
    Jump("loc_3326")

    label("loc_32BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_32C9")
    Jump("loc_3326")

    label("loc_32C9")


    ChrTalk(
        0xFE,
        (
            "格兰赛尔空港\x01",
            "暂时处于封锁状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这也是为了市民们的安全着想。\x02",
    )

    CloseMessageWindow()

    label("loc_3326")

    TalkEnd(0xFE)
    Return()

    # Function_14_32B2 end

    def Function_15_332A(): pass

    label("Function_15_332A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "……游击士算个什么呀？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_332A end

    def Function_16_3350(): pass

    label("Function_16_3350")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "你们要干什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不想挨揍的话\x01",
            "就乖乖回家睡觉去。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_3350 end

    def Function_17_33CD(): pass

    label("Function_17_33CD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "可疑的家伙……\x01",
            "你们是恐怖分子的同伴吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "快点滚开，\x01",
            "别让我再看见。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_33CD end

    def Function_18_3448(): pass

    label("Function_18_3448")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_351A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_34BC")

    ChrTalk(
        0xFE,
        (
            "我说布拉姆，你快看，\x01",
            "那个流线型的舰桥构造！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "应该是最棒的对吧？\x01",
            "我的心情好激动啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3517")

    label("loc_34BC")


    ChrTalk(
        0xFE,
        (
            "我说鲁迪，你快看，\x01",
            "那个流线型的舰桥构造！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "应该是最棒的对吧？\x01",
            "我的心情好激动啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3517")

    Jump("loc_35BB")

    label("loc_351A")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "哇啊～……\x01",
            "好优美的形态啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "能够离这么近\x01",
            "见到『埃尔赛尤号』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特意赶来诞辰庆典\x01",
            "真的是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35BB")

    TalkEnd(0xFE)
    Return()

    # Function_18_3448 end

    def Function_19_35BF(): pass

    label("Function_19_35BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_36B6")

    ChrTalk(
        0xFE,
        (
            "我邀请心仪已久的前辈来参加诞辰庆典，\x01",
            "她竟然一下就答应了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，好不容易来了王都，\x01",
            "却一直都逗留在空港这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呜～我一定要想办法把她\x01",
            "带到更加有情调的地方才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3778")

    label("loc_36B6")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "我邀请心仪已久的前辈来参加诞辰庆典，\x01",
            "她竟然一下就答应了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我的工作非常艰苦，\x01",
            "但我还是努力坚持到了现在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呜呜，\x01",
            "我怎么不知不觉就哭起来了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3778")

    TalkEnd(0xFE)
    Return()

    # Function_19_35BF end

    def Function_20_377C(): pass

    label("Function_20_377C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_37FA")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "今天对你我来说\x01",
            "都是决胜的日子！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "祝你们两个\x01",
            "诞辰庆典玩得愉快！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A97")

    label("loc_37FA")

    TalkBegin(0xFE)
    OP_A2(0x7)
    OP_28(0x31, 0x1, 0x200)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0xFE,
        "啊，是你们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F？？？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "是我，是我啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我是曾经让你们帮忙送信的\x01",
            "沃尔费堡垒的布拉姆！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊～你是那个时候的士兵嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F很久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "真的不知道该怎么感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "多亏了那封信，\x01",
            "我和菲又重归于好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F真是不错啊。\x01",
            "恭喜你们了⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎，说起来你们俩\x01",
            "今天也在一起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F哎……！？\x02\x03",
            "#503F是、是啊，\x01",
            "说得没错……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯嗯，看样子今天　\x01",
            "对你我来说都是决胜的日子！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "愿你们两个\x01",
            "也能得到幸福！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F啊，嗯……谢谢。\x02",
    )

    CloseMessageWindow()

    label("loc_3A97")

    TalkEnd(0xFE)
    Return()

    # Function_20_377C end

    def Function_21_3A9B(): pass

    label("Function_21_3A9B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "定期船起降坪\x01",
            "≡　开往洛连特市\x01",
            "≡　开往蔡斯市\x01",
            "≡　开往卡尔瓦德共和国\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※请勿携带易燃物和危险品\x01",
            "　　　　　利贝尔飞艇公社\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_21_3A9B end

    def Function_22_3B70(): pass

    label("Function_22_3B70")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　飞艇坪塔台　　　　\x01",
            "　※无关人员禁止入内　　\x01",
            "『利贝尔飞艇公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_3B70 end

    SaveToFile()

Try(main)
