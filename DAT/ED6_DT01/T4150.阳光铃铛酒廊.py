from ED6ScenarioHelper import *

def main():
    # 阳光铃铛酒廊

    CreateScenaFile(
        FileName            = 'T4150   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4150.x',
        MapIndex            = 1,
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
        '奥利维尔',                             # 9
        '士兵',                                 # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        '士兵',                                 # 14
        '士兵',                                 # 15
        '士兵',                                 # 16
        '士兵',                                 # 17
        '王都格兰赛尔·北街区',                 # 18
        '庭园大道方向',                         # 19
        '王都格兰赛尔·东街区',                 # 20
        '王都格兰赛尔·西街区',                 # 21
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 4200,
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
        'ED6_DT07/CH00030 ._CH',             # 00
        'ED6_DT07/CH00102 ._CH',             # 01
        'ED6_DT07/CH00133 ._CH',             # 02
        'ED6_DT07/CH00107 ._CH',             # 03
        'ED6_DT07/CH01650 ._CH',             # 04
        'ED6_DT07/CH01620 ._CH',             # 05
        'ED6_DT07/CH01490 ._CH',             # 06
        'ED6_DT07/CH01180 ._CH',             # 07
        'ED6_DT07/CH01270 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01050 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01150 ._CH',             # 0C
        'ED6_DT07/CH01160 ._CH',             # 0D
        'ED6_DT07/CH01470 ._CH',             # 0E
        'ED6_DT07/CH01060 ._CH',             # 0F
        'ED6_DT07/CH01200 ._CH',             # 10
        'ED6_DT07/CH01210 ._CH',             # 11
        'ED6_DT07/CH01100 ._CH',             # 12
        'ED6_DT07/CH01320 ._CH',             # 13
        'ED6_DT07/CH01640 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT07/CH00102P._CP',             # 01
        'ED6_DT07/CH00133P._CP',             # 02
        'ED6_DT07/CH00107P._CP',             # 03
        'ED6_DT07/CH01650P._CP',             # 04
        'ED6_DT07/CH01620P._CP',             # 05
        'ED6_DT07/CH01490P._CP',             # 06
        'ED6_DT07/CH01180P._CP',             # 07
        'ED6_DT07/CH01270P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01050P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01150P._CP',             # 0C
        'ED6_DT07/CH01160P._CP',             # 0D
        'ED6_DT07/CH01470P._CP',             # 0E
        'ED6_DT07/CH01060P._CP',             # 0F
        'ED6_DT07/CH01200P._CP',             # 10
        'ED6_DT07/CH01210P._CP',             # 11
        'ED6_DT07/CH01100P._CP',             # 12
        'ED6_DT07/CH01320P._CP',             # 13
        'ED6_DT07/CH01640P._CP',             # 14
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 12,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 13,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 14,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 15,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 10,
        Z                   = 250,
        Y                   = 36990,
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

    DeclNpc(
        X                   = -50,
        Z                   = 0,
        Y                   = -90220,
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

    DeclNpc(
        X                   = 54990,
        Z                   = 0,
        Y                   = -1130,
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

    DeclNpc(
        X                   = -44420,
        Z                   = 0,
        Y                   = -19990,
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
        X                   = 5270,
        Y                   = -1000,
        Z                   = -67700,
        Range               = -6090,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF0182,
        Unknown_18          = 0x0,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -25000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = -10280,
        Y                   = 0,
        Z                   = -11040,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = -14940,
        Y                   = 0,
        Z                   = -15750,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = -10290,
        Y                   = 0,
        Z                   = -30020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -13010,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 15900,
        Y                   = 0,
        Z                   = 6330,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 32,
    )


    ScpFunction(
        "Function_0_3D2",          # 00, 0
        "Function_1_44C",          # 01, 1
        "Function_2_606",          # 02, 2
        "Function_3_61C",          # 03, 3
        "Function_4_1070",         # 04, 4
        "Function_5_1137",         # 05, 5
        "Function_6_172C",         # 06, 6
        "Function_7_189B",         # 07, 7
        "Function_8_1B6E",         # 08, 8
        "Function_9_2250",         # 09, 9
        "Function_10_24B4",        # 0A, 10
        "Function_11_2522",        # 0B, 11
        "Function_12_2590",        # 0C, 12
        "Function_13_25D6",        # 0D, 13
        "Function_14_261C",        # 0E, 14
        "Function_15_2662",        # 0F, 15
        "Function_16_26D0",        # 10, 16
        "Function_17_2A7E",        # 11, 17
        "Function_18_2B1F",        # 12, 18
        "Function_19_2C74",        # 13, 19
        "Function_20_2D95",        # 14, 20
        "Function_21_2EC6",        # 15, 21
        "Function_22_3075",        # 16, 22
        "Function_23_3198",        # 17, 23
        "Function_24_32E3",        # 18, 24
        "Function_25_33EC",        # 19, 25
        "Function_26_3548",        # 1A, 26
        "Function_27_3633",        # 1B, 27
        "Function_28_364F",        # 1C, 28
        "Function_29_3653",        # 1D, 29
        "Function_30_3657",        # 1E, 30
        "Function_31_365B",        # 1F, 31
        "Function_32_365F",        # 20, 32
    )


    def Function_0_3D2(): pass

    label("Function_0_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3E0")
    OP_A3(0x3FA)
    Event(0, 5)

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_3F3")
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 7)

    label("loc_3F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_401")
    OP_A3(0x3FC)
    Event(0, 16)

    label("loc_401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_40F")
    OP_A3(0x3FD)
    Event(0, 17)

    label("loc_40F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_41F"),
        (103, "loc_435"),
        (SWITCH_DEFAULT, "loc_44B"),
    )


    label("loc_41F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_432")
    OP_A2(0x608)
    Event(0, 3)

    label("loc_432")

    Jump("loc_44B")

    label("loc_435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_448")
    OP_A2(0x629)
    Event(0, 8)

    label("loc_448")

    Jump("loc_44B")

    label("loc_44B")

    Return()

    # Function_0_3D2 end

    def Function_1_44C(): pass

    label("Function_1_44C")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x3005B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46F")
    OP_1C(0x10, 0x0, 0x4)

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47F")
    OP_1B(0x0, 0x0, 0x12)
    Jump("loc_51C")

    label("loc_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_498")
    OP_1B(0x0, 0x0, 0x6)
    Jump("loc_51C")

    label("loc_498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AC")
    OP_1B(0x0, 0x0, 0x13)
    Jump("loc_51C")

    label("loc_4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C0")
    OP_1B(0x0, 0x0, 0x14)
    Jump("loc_51C")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D4")
    OP_1B(0x0, 0x0, 0x15)
    Jump("loc_51C")

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E8")
    OP_1B(0x0, 0x0, 0x16)
    Jump("loc_51C")

    label("loc_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FC")
    OP_1B(0x0, 0x0, 0x17)
    Jump("loc_51C")

    label("loc_4FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_510")
    OP_1B(0x0, 0x0, 0x18)
    Jump("loc_51C")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_51C")
    OP_1B(0x0, 0x0, 0x19)

    label("loc_51C")

    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x2, 0x10)
    OP_72(0x4, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x10, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_605")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_43(0xB, 0x1, 0x0, 0x9)
    OP_43(0xC, 0x1, 0x0, 0x9)
    OP_43(0xD, 0x1, 0x0, 0x9)
    OP_43(0xE, 0x1, 0x0, 0x9)
    OP_43(0xF, 0x1, 0x0, 0x9)
    OP_43(0x10, 0x1, 0x0, 0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_599")

    label("loc_599")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_5A4")

    label("loc_5A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_5C1")
    SetChrFlags(0xE, 0x80)
    OP_44(0xE, 0xFF)
    SetChrFlags(0xF, 0x80)
    OP_44(0xF, 0xFF)

    label("loc_5C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_5DE")
    SetChrFlags(0xB, 0x80)
    OP_44(0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    OP_44(0xC, 0xFF)

    label("loc_5DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_5F2")
    SetChrFlags(0x10, 0x80)
    OP_44(0x10, 0xFF)

    label("loc_5F2")

    OP_6B(4200, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_605")

    Return()

    # Function_1_44C end

    def Function_2_606(): pass

    label("Function_2_606")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_606")

    label("loc_61B")

    Return()

    # Function_2_606 end

    def Function_3_61C(): pass

    label("Function_3_61C")

    EventBegin(0x0)
    OP_6D(600, 250, 1950, 0)
    OP_67(0, 17690, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(571, 0)
    SetChrPos(0x101, -340, 0, -51790, 0)
    SetChrPos(0x102, -1140, 0, -53240, 0)
    SetChrPos(0x10E, 710, 0, -53630, 0)

    def lambda_694():
        OP_6D(-450, 290, -49040, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_694)

    def lambda_6AC():
        OP_6B(3600, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6AC)

    def lambda_6BC():
        OP_67(0, 6190, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6BC)

    def lambda_6D4():
        OP_6C(315000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6D4)

    def lambda_6E4():
        OP_6E(262, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6E4)
    Sleep(8500)

    ChrTalk(
        0x101,
        (
            "#000F哇～～\x01",
            "好大的城市啊。\x02\x03",
            "以前和老爸一起来的时候，\x01",
            "就有这么大吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F当然了，这是王国最大的城市嘛。\x02\x03",
            "这条大街的最前方，\x01",
            "就是女王陛下所居住的格兰赛尔城……\x02\x03",
            "还有七耀教会的大圣堂、王立竞技场，\x01",
            "以及各国的大使馆之类的设施呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F哎～是这样啊。\x02\x03",
            "不过约修亚，你还真是了解啊。\x02\x03",
            "以前也来过这里吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x01",
            "也是小时候的事情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F真的是……\x01",
            "这城市无论何时看起来都是这么美丽呢。\x02\x03",
            "不过单从规模上来说，\x01",
            "帝国和共和国的首都比这里要更大一些。\x01",
            "　\x02\x03",
            "不过这个格兰赛尔，\x01",
            "可是有着其他地方比不上的舒适感呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9EE():
        TurnDirection(0xFE, 0x10E, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9EE)
    TurnDirection(0x101, 0x10E, 400)

    ChrTalk(
        0x101,
        (
            "#000F嘿嘿，真是高兴啊。\x01",
            "能听到外国的人这么说。\x02\x03",
            "说起来……\x01",
            "教授，接下来打算干什么呢？\x02\x03",
            "留在这里的费用没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x101, 400)

    ChrTalk(
        0x10E,
        (
            "#130F哈哈，其实是有保障的。\x02\x03",
            "我要暂时寄住在一个叫\x01",
            "『历史资料馆』的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎，还有这样的地方啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是展示发掘出来的文物\x01",
            "和美术品之类的博物馆吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F对，作为那里的名誉会员，\x01",
            "我要在那里借住一段时间。\x02\x03",
            "艾丝蒂尔、约修亚，\x01",
            "如果方便的话你们也过来玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呜……说到博物馆，\x01",
            "就有一种很严肃的气氛……\x02\x03",
            "是不是要说『既然来了，就学习吧』？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F呵呵，如果你愿意的话，\x01",
            "我也可以认真地教教你。\x02\x03",
            "……开玩笑的，\x01",
            "只是参观一下展示品，\x01",
            "就会感到很开心的。\x02\x03",
            "那么，我就此告辞了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D76():

        label("loc_D76")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_D76")

    QueueWorkItem2(0x101, 1, lambda_D76)

    def lambda_D87():

        label("loc_D87")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_D87")

    QueueWorkItem2(0x102, 1, lambda_D87)
    OP_8E(0x10E, 0xF78, 0x0, 0xFFFF3D78, 0x7D0, 0x0)

    def lambda_DAC():
        OP_8E(0xFE, 0x1356, 0x0, 0xFFFF76E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_DAC)

    def lambda_DC7():
        OP_6D(-1030, 0, -52400, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DC7)
    Sleep(2000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x101,
        (
            "#000F哈～怎么说呢，\x01",
            " \x02\x03",
            "不过说到名誉会员，\x01",
            "应该是个相当有名的学者吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，说不定就是呢。\x02\x03",
            "那么，我们先去\x01",
            "拜访一下游击士协会吧？\x02\x03",
            "要办理转属手续……\x01",
            "而且要完成博士的委托，\x01",
            "也要先和协会商量一下才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F嗯，没错……\x02\x03",
            "仔细想想，\x01",
            "该怎么和女王陛下会面呢？\x02\x03",
            "肯定不会是去城里\x01",
            "就能见到那样简单吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x10E, -100, 0, -52250, 0)
    SetChrFlags(0x10E, 0x80)
    EventEnd(0x0)
    RemoveParty(0xD, 0xFF)
    Return()

    # Function_3_61C end

    def Function_4_1070(): pass

    label("Function_4_1070")

    EventBegin(0x0)
    OP_6D(16030, 500, 7220, 1000)

    ChrTalk(
        0x101,
        (
            "#000F啊……\x02\x03",
            "这是……钢琴？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，不是放唱片。\x01",
            "好像是里面有人在弹吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F有点不好的预感呢……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_1070 end

    def Function_5_1137(): pass

    label("Function_5_1137")

    EventBegin(0x0)
    OP_6D(16020, 250, 7280, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x101, 15830, 740, 8470, 0)
    SetChrPos(0x102, 15830, 740, 8470, 0)
    SetChrPos(0x8, 15830, 740, 8470, 0)
    OP_0D()
    OP_70(0x10, 0x3C)
    OP_73(0x10)

    def lambda_1198():
        OP_8E(0xFE, 0x3B7E, 0xFA, 0xF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1198)
    Sleep(400)

    def lambda_11B8():
        OP_8E(0xFE, 0x4060, 0xFA, 0xE6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11B8)
    Sleep(500)

    def lambda_11D8():
        OP_8E(0xFE, 0x3E9E, 0xFA, 0x14FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11D8)
    OP_6D(16100, 250, 4400, 2000)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#000F我说，为什么这么\x01",
            "理所当然地就跟出来了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F哈·哈·哈。\x01",
            "别说这么无情的话啊。\x02\x03",
            "旅行要结伴才愉快嘛，\x01",
            "而且我也可以帮忙找人。\x02\x03",
            "还是……\x01",
            "……我妨碍到你们了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F哈·哈·哈。\x01",
            "真是天真啊。\x02\x03",
            "刚刚意识到自己心中爱情花蕾的存在，\x01",
            "却又害怕它开放的少女……\x02\x03",
            "……嘻嘻，感觉不错啊， \x01",
            "让我都有一些春心萌动了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F…………呜………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F？？？\x02\x03",
            "你说的是什么意思啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#030F嘻嘻，那就是……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 1)

    ChrTalk(
        0x101,
        "#000F嘿呀！\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 2)

    ChrTalk(
        0x8,
        "#030F啊～～……！#10A\x05\x02",
    )


    def lambda_1486():
        OP_8F(0xFE, 0x3DD6, 0x2E4, 0x2116, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1486)
    OP_99(0x101, 0x7, 0xC, 0x7D0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "哇哇，怎么了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这位客人，请振作一点！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不行了……\x01",
            "已经翻白眼了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔……\x02\x03",
            "不知道你在生什么气，\x01",
            "不过这也太过分了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 3)
    SetChrFlags(0x101, 0x2)
    OP_99(0x101, 0x0, 0x13, 0x7D0)

    ChrTalk(
        0x101,
        (
            "#000F……我已经避开了要害，\x01",
            "只是把他打飞而已。\x02\x03",
            "不会受很重的伤的。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)

    ChrTalk(
        0x8,
        (
            "#030F呵呵……\x01",
            "艾丝蒂尔……真害羞啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……确实没什么事啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D9")

    ChrTalk(
        0x101,
        (
            "#000F好啦，再去找人吧。\x02\x03",
            "赶快去大使馆吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1729")

    label("loc_16D9")


    ChrTalk(
        0x101,
        (
            "#000F好啦，再去找人吧。\x02\x03",
            "赶快去周游道吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1729")

    EventEnd(0x0)
    Return()

    # Function_5_1137 end

    def Function_6_172C(): pass

    label("Function_6_172C")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A3")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，还不知道\x01",
            "金先生到底去了哪里呢。\x02\x03",
            "我们去东街区的\x01",
            "卡尔瓦德大使馆问问吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1896")

    label("loc_17A3")

    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，对了……\x02\x03",
            "不是说金大哥\x01",
            "时常在酒廊喝酒吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F啊，艾南先生\x01",
            "确实这么说过。\x02\x03",
            "为了慎重起见，去周游道之前\x01",
            "先到酒廊看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1896")

    Call(0, 27)
    Return()

    # Function_6_172C end

    def Function_7_189B(): pass

    label("Function_7_189B")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(16020, 250, 7280, 0)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, 15830, 740, 8470, 0)
    SetChrPos(0x102, 15830, 740, 8470, 0)
    OP_0D()
    OP_70(0xD, 0x3B)
    OP_73(0xD)

    def lambda_18E9():
        OP_8E(0xFE, 0x3B7E, 0xFA, 0xF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18E9)
    Sleep(400)

    def lambda_1909():
        OP_8E(0xFE, 0x4060, 0xFA, 0xE6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1909)
    OP_6D(16100, 250, 4400, 2000)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 90, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 270, 400)
    Fade(1000)
    OP_6B(3000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#008F呼～……\x01",
            "吃得肚子鼓鼓的了。\x02\x03",
            "#007F那两个人，都已经吃了那么多了，\x01",
            "还在不停地狼吞虎咽……\x02\x03",
            "他们还真是合得来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F金先生是那样的体格，\x01",
            "奥利维尔又很能吃嘛。\x02\x03",
            "只要不影响到明天的正式赛，\x01",
            "就应该没什么关系啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，确实他们两个都不用让人担心。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F天色已经黑了，\x01",
            "我们也该去北街区的酒店了吧？\x02\x03",
            "艾南先生一定已经给我们订好房间了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_189B end

    def Function_8_1B6E(): pass

    label("Function_8_1B6E")

    EventBegin(0x0)
    OP_6F(0x1, 60)
    SetChrPos(0x101, 8940, 250, -12710, 270)
    SetChrPos(0x102, 8980, 250, -13870, 270)
    SetChrPos(0x9, 1930, 0, -4430, 0)
    SetChrPos(0xA, 1040, 0, -5320, 0)
    SetChrChipByIndex(0x9, 20)
    SetChrChipByIndex(0xA, 20)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_6D(9320, 440, -13270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToDark(0, 0, -1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1500)
    FadeToBright(1500, 0)
    OP_72(0x1, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x800)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#004F哇……\x01",
            "已经这么晚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们还是赶快回到旅馆比较好吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "男人的声音",
        "#4P喂，那边的人！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1CF0():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CF0)

    def lambda_1CFE():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CFE)

    def lambda_1D0C():
        OP_6D(8710, 250, -11760, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D0C)

    def lambda_1D24():
        OP_6C(90000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1D24)

    def lambda_1D34():
        OP_8E(0xFE, 0x1B76, 0xFA, 0xFFFFD724, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D34)
    Sleep(300)

    def lambda_1D54():
        OP_8E(0xFE, 0x1720, 0x0, 0xFFFFD314, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D54)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#004F哎……\x01",
            "士兵先生，怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P我们是巡逻人员。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P从今天开始，\x01",
            "作为恐怖活动的应付对策之一，\x01",
            "夜间的巡视要进行强化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "因此，晚上请尽量克制一下，\x01",
            "最好不要擅自外出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你们也赶快回家吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F晚上不让外出……\x01",
            "这不是很不方便吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这是上面的决定。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P虽然很抱歉，还是请你们服从指示。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P对了……\x01",
            "你们住在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们住在北街区的罗恩鲍姆酒店。\x01",
            "　\x02\x03",
            "武术大会期间都会住在那里的……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "武术大会期间……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "等一下，\x01",
            "我好像在哪里见过你们……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#3S#1P啊啊！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P这两个孩子，\x01",
            "不就是进入武术大会决赛的选手吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你这样一说，还真是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，士兵先生，\x01",
            "你们也去看比赛了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "哈哈，是趁着做警卫的时候呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "特别是今天白热化的比赛，\x01",
            "真是让我感到很兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P明天就是决赛了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P我们送你们回旅馆，\x01",
            "好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F哎、这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F知道了。\x01",
            "谢谢你们的好意。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1B6E end

    def Function_9_2250(): pass

    label("Function_9_2250")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B3")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2283")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A0")

    label("loc_2283")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22A9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A0")

    label("loc_22A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22CF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A0")

    label("loc_22CF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22F6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A0")

    label("loc_22F6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_231C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A0")

    label("loc_231C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2342")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A0")

    label("loc_2342")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2367")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A0")

    label("loc_2367")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_238C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A0")

    label("loc_238C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23A0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24B0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A1")

    ChrTalk(
        0xFE,
        "你们是干什么的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F（糟糕……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F（被发现了吗……）\x02",
    )

    CloseMessageWindow()

    label("loc_24A1")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_24B0")

    Jump("Function_9_2250")

    label("loc_24B3")

    Return()

    # Function_9_2250 end

    def Function_10_24B4(): pass

    label("Function_10_24B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2521")
    SetChrPos(0xFE, -29750, 250, -16079, 270)
    OP_8E(0xFE, 0xFFFFE0B6, 0xFA, 0xFFFFC131, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE0B6, 0xFA, 0x2EEA, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE0B6, 0xFA, 0xFFFFC131, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF8BCA, 0xFA, 0xFFFFC131, 0xBB8, 0x0)
    Jump("Function_10_24B4")

    label("loc_2521")

    Return()

    # Function_10_24B4 end

    def Function_11_2522(): pass

    label("Function_11_2522")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_258F")
    SetChrPos(0xFE, -29910, 250, -23870, 270)
    OP_8E(0xFE, 0xFFFFDF08, 0xFA, 0xFFFFA2C2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDE2C, 0xFA, 0xFFFF7D88, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDF08, 0xFA, 0xFFFFA2C2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF8B2A, 0xFA, 0xFFFFA2C2, 0xBB8, 0x0)
    Jump("Function_11_2522")

    label("loc_258F")

    Return()

    # Function_11_2522 end

    def Function_12_2590(): pass

    label("Function_12_2590")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25D5")
    SetChrPos(0xFE, -6720, 0, -19860, 270)
    OP_8E(0xFE, 0xFFFF8620, 0x0, 0xFFFFB26C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE5C0, 0x0, 0xFFFFB26C, 0xBB8, 0x0)
    Jump("Function_12_2590")

    label("loc_25D5")

    Return()

    # Function_12_2590 end

    def Function_13_25D6(): pass

    label("Function_13_25D6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_261B")
    SetChrPos(0xFE, 3810, 0, 10100, 180)
    OP_8E(0xFE, 0xEE2, 0x0, 0xFFFF7518, 0xBB8, 0x0)
    OP_8E(0xFE, 0xEE2, 0x0, 0x2774, 0xBB8, 0x0)
    Jump("Function_13_25D6")

    label("loc_261B")

    Return()

    # Function_13_25D6 end

    def Function_14_261C(): pass

    label("Function_14_261C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2661")
    SetChrPos(0xFE, -3690, 0, -34890, 180)
    OP_8E(0xFE, 0xFFFFF196, 0x0, 0x25DA, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF196, 0x0, 0xFFFF77B6, 0xBB8, 0x0)
    Jump("Function_14_261C")

    label("loc_2661")

    Return()

    # Function_14_261C end

    def Function_15_2662(): pass

    label("Function_15_2662")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26CF")
    SetChrPos(0xFE, -1740, 0, -6830, 180)
    OP_8E(0xFE, 0xFFFFF934, 0x0, 0xFFFFAF1A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7F8, 0x0, 0xFFFFAE66, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7F8, 0x0, 0xFFFFE4B2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF934, 0x0, 0xFFFFE552, 0xBB8, 0x0)
    Jump("Function_15_2662")

    label("loc_26CF")

    Return()

    # Function_15_2662 end

    def Function_16_26D0(): pass

    label("Function_16_26D0")

    EventBegin(0x0)
    RemoveParty(0x0, 0xFF)
    AddParty(0x3, 0xFF)
    FadeToBright(2000, 0)
    OP_6D(-90, 0, -64700, 0)
    OP_67(0, 6090, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(196000, 0)
    OP_6E(372, 0)
    SetChrPos(0x104, -190, 0, -63320, 197)
    SetChrPos(0x102, 560, 0, -64300, 200)
    SetChrPos(0x108, -890, 0, -64430, 197)

    def lambda_2757():
        OP_8E(0xFE, 0x96, 0x0, 0xFFFF2C8E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2757)

    def lambda_2772():
        OP_8E(0xFE, 0x3F2, 0x0, 0xFFFF2702, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2772)

    def lambda_278D():
        OP_8E(0xFE, 0xFFFFFCB8, 0x0, 0xFFFF25F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_278D)
    OP_6D(280, 0, -55900, 3000)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 0, 400)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F……虽然没有巡逻兵了，\x01",
            "不过街上的气氛十分紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯……\x01",
            "确实有种大乱来临的感觉呢。\x02\x03",
            "和昨天的气氛明显不一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F很好，此刻就让我\x01",
            "用鲁特琴缓和一下\x01",
            "这里的紧张空气吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28C5():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_28C5)
    TurnDirection(0x102, 0x104, 400)

    ChrTalk(
        0x102,
        (
            "#010F如果你做了那么引人注目的事情，\x01",
            "那个人一定又会飞奔而来的。\x02\x03",
            "我记得他是叫穆拉对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F是、是呀……\x02\x03",
            "你们两个千万不能\x01",
            "接近帝国大使馆啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈，我们才没有\x01",
            "那份闲心跑去大使馆那儿呢。\x02\x03",
            "准备完毕之后\x01",
            "就进地下水路里去吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_16_26D0 end

    def Function_17_2A7E(): pass

    label("Function_17_2A7E")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-1140, 0, -63570, 0)
    OP_67(0, 7480, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(320000, 0)
    OP_6E(580, 0)

    def lambda_2AE0():
        OP_6D(-20, 250, 7140, 20000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2AE0)

    def lambda_2AF8():
        OP_6C(0, 20000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2AF8)
    Sleep(17000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2A7E end

    def Function_18_2B1F(): pass

    label("Function_18_2B1F")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BDE")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010F还是先去协会支部打声招呼吧。\x01",
            "　\x02\x03",
            "要先办理转属手续……\x01",
            "而且还有博士的委托。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C6F")

    label("loc_2BDE")


    ChrTalk(
        0x102,
        (
            "#010F还是先去协会支部打声招呼吧。\x01",
            "　\x02\x03",
            "要先办理转属手续……\x01",
            "而且还有博士的委托。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6F")

    Call(0, 27)
    Return()

    # Function_18_2B1F end

    def Function_19_2C74(): pass

    label("Function_19_2C74")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D20")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010F赶快回协会报告吧。\x02\x03",
            "再磨磨蹭蹭的天就要黑了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006F嗯，现在就去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D90")

    label("loc_2D20")


    ChrTalk(
        0x102,
        (
            "#010F赶快回协会报告吧。\x02\x03",
            "再磨磨蹭蹭的天就要黑了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D90")

    Call(0, 27)
    Return()

    # Function_19_2C74 end

    def Function_20_2D95(): pass

    label("Function_20_2D95")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E57")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010F已经很晚了，\x01",
            "我们回酒店去吧。\x02\x03",
            "该休息的时候就是要好好休息。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F酒店在北街区对吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EC1")

    label("loc_2E57")


    ChrTalk(
        0x102,
        (
            "#010F已经很晚了，\x01",
            "我们回酒店去吧。\x02\x03",
            "明天还有比赛，\x01",
            "我们最好早点休息。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC1")

    Call(0, 27)
    Return()

    # Function_20_2D95 end

    def Function_21_2EC6(): pass

    label("Function_21_2EC6")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF9")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F65")

    ChrTalk(
        0x102,
        (
            "#010F我想奈尔先生正在等我们吧。\x01",
            "　\x02\x03",
            "去西街区的通讯社看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FF6")

    label("loc_2F65")


    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，那边是城门哦。\x02\x03",
            "奈尔先生的通讯社应该在西街区吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F哦～呵呵，知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_2FF6")

    Jump("loc_3070")

    label("loc_2FF9")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F我想奈尔先生正在等我们吧。\x01",
            "　\x02\x03",
            "去西街区的通讯社看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3070")

    Call(0, 27)
    Return()

    # Function_21_2EC6 end

    def Function_22_3075(): pass

    label("Function_22_3075")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3122")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010F总之我们先回协会报告吧。\x02\x03",
            "最好把奈尔的调查结果也告诉艾南先生。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006F嗯，现在就去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3193")

    label("loc_3122")


    ChrTalk(
        0x102,
        (
            "#010F总之我们先回协会报告吧。\x02\x03",
            "最好把奈尔的调查结果也告诉艾南先生。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3193")

    Call(0, 27)
    Return()

    # Function_22_3075 end

    def Function_23_3198(): pass

    label("Function_23_3198")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3243")

    ChrTalk(
        0x108,
        (
            "#070F呼，已经傍晚了。\x01",
            "我们尽量不要外出了。\x02\x03",
            "今天就别修行了，\x01",
            "赶快去城里参加晚宴吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32DE")

    label("loc_3243")

    TurnDirection(0x108, 0x0, 400)

    ChrTalk(
        0x108,
        (
            "#070F喂喂，\x01",
            "难道你们还打算外出吗？\x02\x03",
            "就算是再热衷于修炼，\x01",
            "现在还是快去参加晚宴吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32DE")

    Call(0, 27)
    Return()

    # Function_23_3198 end

    def Function_24_32E3(): pass

    label("Function_24_32E3")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_336A")

    ChrTalk(
        0x108,
        (
            "#070F现在没空去街道外面。\x02\x03",
            "做好准备后就向地下水路进发吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E7")

    label("loc_336A")

    TurnDirection(0x108, 0x0, 400)

    ChrTalk(
        0x108,
        (
            "#070F现在没空去街道外面。\x02\x03",
            "做好准备后就向地下水路进发吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E7")

    Call(0, 27)
    Return()

    # Function_24_32E3 end

    def Function_25_33EC(): pass

    label("Function_25_33EC")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B3")

    ChrTalk(
        0x101,
        "#501F啊，这边是城外……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F我说，\x01",
            "我们还是在城里再散散步吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，好啊。\x01",
            "还有很多地方没看呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3543")

    label("loc_34B3")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F我说，约修亚。\x02\x03",
            "在城里面再散会儿步吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，好啊。\x01",
            "还有很多地方没看呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3543")

    Call(0, 27)
    Return()

    # Function_25_33EC end

    def Function_26_3548(): pass

    label("Function_26_3548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3632")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35E6")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F艾丝蒂尔，\x01",
            "已经快到指定的时间了。\x02\x03",
            "我们赶快去大圣堂吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F嗯……明白！\x02",
    )

    CloseMessageWindow()
    Jump("loc_362E")

    label("loc_35E6")


    ChrTalk(
        0x102,
        (
            "#012F已经快到指定的时间了。\x01",
            "　\x02\x03",
            "我们赶快去大圣堂吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_362E")

    Call(0, 27)

    label("loc_3632")

    Return()

    # Function_26_3548 end

    def Function_27_3633(): pass

    label("Function_27_3633")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_27_3633 end

    def Function_28_364F(): pass

    label("Function_28_364F")

    SetPlaceName(0xB9) # 阳光铃铛酒廊
    Return()

    # Function_28_364F end

    def Function_29_3653(): pass

    label("Function_29_3653")

    SetPlaceName(0xB0) # 阳光铃铛酒廊
    Return()

    # Function_29_3653 end

    def Function_30_3657(): pass

    label("Function_30_3657")

    SetPlaceName(0xB2) # 阳光铃铛酒廊
    Return()

    # Function_30_3657 end

    def Function_31_365B(): pass

    label("Function_31_365B")

    SetPlaceName(0xAE) # 阳光铃铛酒廊
    Return()

    # Function_31_365B end

    def Function_32_365F(): pass

    label("Function_32_365F")

    SetPlaceName(0xB3) # 阳光铃铛酒廊
    Return()

    # Function_32_365F end

    SaveToFile()

Try(main)
