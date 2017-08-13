from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3102   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '格斯塔夫维修长',                       # 9
        '吉拉尔',                               # 10
        '玛多克工房长',                         # 11
        '朵洛希',                               # 12
        '安东尼',                               # 13
        '凯诺娜上尉',                           # 14
        '鲁特尔',                               # 15
        '多杰',                                 # 16
        '巴拉特',                               # 17
        '船',                                   # 18
        '船影',                                 # 19
        '士兵',                                 # 20
        '士兵',                                 # 21
        '士兵',                                 # 22
        '蔡斯市·工房区',                       # 23
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
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH02440 ._CH',             # 01
        'ED6_DT07/CH02620 ._CH',             # 02
        'ED6_DT07/CH02070 ._CH',             # 03
        'ED6_DT07/CH01700 ._CH',             # 04
        'ED6_DT07/CH02100 ._CH',             # 05
        'ED6_DT07/CH01020 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01640 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH02440P._CP',             # 01
        'ED6_DT07/CH02620P._CP',             # 02
        'ED6_DT07/CH02070P._CP',             # 03
        'ED6_DT07/CH01700P._CP',             # 04
        'ED6_DT07/CH02100P._CP',             # 05
        'ED6_DT07/CH01020P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01640P._CP',             # 09
    )

    DeclNpc(
        X                   = -37000,
        Z                   = -3800,
        Y                   = 145500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -20110,
        Z                   = 8000,
        Y                   = 121830,
        Direction           = 177,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -18770,
        Z                   = 8000,
        Y                   = 89560,
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
        X                   = -43700,
        Y                   = -4000,
        Z                   = 146000,
        Range               = -41600,
        Unknown_10          = 0xFFFFF830,
        Unknown_14          = 0x22A4C,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )

    DeclEvent(
        X                   = -43200,
        Y                   = -5000,
        Z                   = 145000,
        Range               = -48600,
        Unknown_10          = 0xFFFFF830,
        Unknown_14          = 0x22B78,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = -15210,
        Y                   = 7000,
        Z                   = 100600,
        Range               = -22980,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x1938E,
        Unknown_18          = 0x0,
        Unknown_1C          = 26,
    )


    DeclActor(
        TriggerX            = -19980,
        TriggerZ            = 8000,
        TriggerY            = 119710,
        TriggerRange        = 400,
        ActorX              = -20110,
        ActorZ              = 9500,
        ActorY              = 121830,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41010,
        TriggerZ            = 8000,
        TriggerY            = 122500,
        TriggerRange        = 800,
        ActorX              = -41010,
        ActorZ              = 10200,
        ActorY              = 122500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38900,
        TriggerZ            = 8400,
        TriggerY            = 122040,
        TriggerRange        = 800,
        ActorX              = -38900,
        ActorZ              = 9900,
        ActorY              = 122040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3A6",          # 00, 0
        "Function_1_661",          # 01, 1
        "Function_2_872",          # 02, 2
        "Function_3_9EF",          # 03, 3
        "Function_4_A13",          # 04, 4
        "Function_5_A37",          # 05, 5
        "Function_6_A5B",          # 06, 6
        "Function_7_A7F",          # 07, 7
        "Function_8_109F",         # 08, 8
        "Function_9_17D7",         # 09, 9
        "Function_10_1815",        # 0A, 10
        "Function_11_3A4B",        # 0B, 11
        "Function_12_4872",        # 0C, 12
        "Function_13_4AFE",        # 0D, 13
        "Function_14_4BA2",        # 0E, 14
        "Function_15_4BA7",        # 0F, 15
        "Function_16_53FF",        # 10, 16
        "Function_17_5D63",        # 11, 17
        "Function_18_634A",        # 12, 18
        "Function_19_63CB",        # 13, 19
        "Function_20_733B",        # 14, 20
        "Function_21_735E",        # 15, 21
        "Function_22_7381",        # 16, 22
        "Function_23_73A4",        # 17, 23
        "Function_24_73C7",        # 18, 24
        "Function_25_7461",        # 19, 25
        "Function_26_74DA",        # 1A, 26
    )


    def Function_0_3A6(): pass

    label("Function_0_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3BD")
    OP_A3(0x3FA)
    Event(0, 16)
    OP_B1("T3102_1")

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF")
    SetChrPos(0xA, -44860, -4000, 141600, 270)
    ClearChrFlags(0xA, 0x80)

    label("loc_3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_41C")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -40990, 8000, 129460, 12)
    OP_43(0xE, 0x0, 0x0, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44660, 8000, 129500, 5)
    Jump("loc_660")

    label("loc_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_459")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -40990, 8000, 129460, 12)
    OP_43(0xE, 0x0, 0x0, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44660, 8000, 129500, 5)
    Jump("loc_660")

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_479")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -40990, 8000, 122890, 180)
    Jump("loc_660")

    label("loc_479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4E2")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -47500, -4000, 151780, 261)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -47500, -4000, 152840, 261)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -40130, 8000, 125930, 237)
    OP_43(0xC, 0x0, 0x0, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_660")

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_522")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -44530, -4000, 142000, 176)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44510, -4000, 140610, 21)
    SetChrFlags(0x10, 0x10)
    Jump("loc_660")

    label("loc_522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_55F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -58040, 4000, 125930, 187)
    OP_43(0x8, 0x0, 0x0, 0x6)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_660")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_569")
    Jump("loc_660")

    label("loc_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5A6")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -49800, 8000, 117400, 3)
    OP_43(0x8, 0x0, 0x0, 0x5)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_660")

    label("loc_5A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_END)), "loc_5C6")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44440, -4000, 153380, 90)
    Jump("loc_660")

    label("loc_5C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_5E6")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_660")

    label("loc_5E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_606")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_660")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_626")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_660")

    label("loc_626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_660")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -40130, 8000, 125930, 237)
    OP_43(0xC, 0x0, 0x0, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)

    label("loc_660")

    Return()

    # Function_0_3A6 end

    def Function_1_661(): pass

    label("Function_1_661")

    OP_16(0x2, 0xFA0, 0xFFFD6020, 0x4E20, 0x30053)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A3")
    OP_B1("T3102_3")
    OP_6F(0x0, 1001)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_6F(0x3, 100)
    Jump("loc_871")

    label("loc_6A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70C")
    OP_B1("T3102_2")
    OP_6F(0x4, 1)
    OP_6F(0x3, 200)
    OP_71(0x6, 0x4)
    OP_6F(0x0, 1001)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -43100, -3800, 144030, 270)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x64, 0x0)
    Jump("loc_871")

    label("loc_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73C")
    OP_B1("T3102_2")
    OP_6F(0x0, 250)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_6F(0x3, 100)
    Jump("loc_871")

    label("loc_73C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_767")
    OP_B1("T3102_2")
    OP_6F(0x0, 250)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_6F(0x3, 100)
    Jump("loc_871")

    label("loc_767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_END)), "loc_7BB")
    OP_B1("T3102_2")
    OP_6F(0x4, 1)
    OP_6F(0x3, 200)
    OP_71(0x6, 0x4)
    OP_6F(0x0, 1001)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -42710, -3800, 144020, 270)
    Jump("loc_824")

    label("loc_7BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_803")
    OP_B1("T3102_2")
    OP_6F(0x4, 1)
    OP_6F(0x3, 200)
    OP_71(0x6, 0x4)
    OP_6F(0x0, 1001)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -36900, -3800, 140550, 90)
    Jump("loc_824")

    label("loc_803")

    OP_B1("T3102_2")
    OP_6F(0x0, 1001)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_6F(0x3, 100)

    label("loc_824")

    Jump("loc_871")

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_850")
    OP_B1("T3102_1")
    OP_6F(0x4, 1)
    OP_6F(0x3, 200)
    OP_6F(0x0, 1001)
    Jump("loc_871")

    label("loc_850")

    OP_B1("T3102_2")
    OP_6F(0x0, 1001)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_6F(0x3, 100)

    label("loc_871")

    Return()

    # Function_1_661 end

    def Function_2_872(): pass

    label("Function_2_872")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_897")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_9D9")

    label("loc_897")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B0")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_9D9")

    label("loc_8B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C9")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_9D9")

    label("loc_8C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E2")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_9D9")

    label("loc_8E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FB")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_9D9")

    label("loc_8FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_914")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_9D9")

    label("loc_914")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92D")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_9D9")

    label("loc_92D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_946")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_9D9")

    label("loc_946")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95F")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_9D9")

    label("loc_95F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_978")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_9D9")

    label("loc_978")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_991")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_9D9")

    label("loc_991")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AA")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_9D9")

    label("loc_9AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C3")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_9D9")

    label("loc_9C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D9")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_9D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9EE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_9D9")

    label("loc_9EE")

    Return()

    # Function_2_872 end

    def Function_3_9EF(): pass

    label("Function_3_9EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A12")
    OP_8D(0xFE, -19390, 119560, -16690, 116060, 3000)
    Jump("Function_3_9EF")

    label("loc_A12")

    Return()

    # Function_3_9EF end

    def Function_4_A13(): pass

    label("Function_4_A13")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A36")
    OP_8D(0xFE, -35820, 123780, -43940, 129220, 3000)
    Jump("Function_4_A13")

    label("loc_A36")

    Return()

    # Function_4_A13 end

    def Function_5_A37(): pass

    label("Function_5_A37")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A5A")
    OP_8D(0xFE, -45240, 117320, -51970, 121500, 2000)
    Jump("Function_5_A37")

    label("loc_A5A")

    Return()

    # Function_5_A37 end

    def Function_6_A5B(): pass

    label("Function_6_A5B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7E")
    OP_8D(0xFE, -56420, 122640, -59470, 129340, 2000)
    Jump("Function_6_A5B")

    label("loc_A7E")

    Return()

    # Function_6_A5B end

    def Function_7_A7F(): pass

    label("Function_7_A7F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_AD0")

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "都不通知一下就检查，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王国军真是的，\x01",
            "实在太乱来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109B")

    label("loc_AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_B2A")

    ChrTalk(
        0xFE,
        (
            "一会儿『赛希莉亚号』\x01",
            "就要开过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "必须马上开始\x01",
            "确认下拢岸的状况了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109B")

    label("loc_B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_B9E")

    ChrTalk(
        0xFE,
        (
            "工房船现在\x01",
            "马上就要出航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "却比预定去要塞的时间提前了很多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那边发生了什么事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_109B")

    label("loc_B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_BF6")

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "这样飞船起航就告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "趁这段时间整理一下货物吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109B")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_CC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_C7A")

    ChrTalk(
        0xFE,
        (
            "话说回来，这种时候\x01",
            "真是羡慕雷曼那家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家伙兼任驾驶员，\x01",
            "飞行前为了调整身体状态，\x01",
            "早早地就回家去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBD")

    label("loc_C7A")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "呼，明天还是要去要塞啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近的工作\x01",
            "好像很多啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_CBD")

    Jump("loc_109B")

    label("loc_CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_D3D")

    ChrTalk(
        0xFE,
        (
            "中央工房的事件\x01",
            "应该解决了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎？\x01",
            "犯人到现在都还没抓到？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那还真是糟糕啊。\x01",
            "下次不会来袭击工房船吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109B")

    label("loc_D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_ED5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_DF8")

    ChrTalk(
        0xFE,
        (
            "呼，都是因为那个公爵大人，\x01",
            "搞得大家都对王家的印象变差了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哼，很久以前\x01",
            "那种快乐纯粹的女王诞辰庆典\x01",
            "是很难再出现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "该死，那个混账公爵。\x01",
            "还我的诞辰庆典来！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED2")

    label("loc_DF8")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "之前的休假\x01",
            "我去参观了\x01",
            "艾尔·雷登瀑布……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟遇到那个叫杜什么的公爵，\x01",
            "那个王家的人微服出行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且那个人\x01",
            "还蛮横任性得要命。\x01",
            "真是倒了大霉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，大家都没想到\x01",
            "王家的人竟会是那个样子。\x01",
            "真是失望透了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED2")

    Jump("loc_109B")

    label("loc_ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_F58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0C")

    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "差不多该到返航的时候了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F55")

    label("loc_F0C")


    ChrTalk(
        0xFE,
        "怎么样？很漂亮吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这可是中央工房引以为傲的\x01",
            "『莱普尼兹号』啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F55")

    Jump("loc_109B")

    label("loc_F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_104D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_FC3")

    ChrTalk(
        0xFE,
        (
            "工房好像还没找出\x01",
            "昨天那种现象的原因所在吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎样，\x01",
            "希望不要再发生这种事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_104A")

    label("loc_FC3")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "昨天晚上，导力供应停止了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过还好不是在白天发生，\x01",
            "真是万幸呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果在飞艇上出现这种情况，\x01",
            "真不知道会发生什么事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104A")

    Jump("loc_109B")

    label("loc_104D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_109B")

    ChrTalk(
        0xFE,
        "好的，拢岸准备好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来，\x01",
            "要快点进行出发前的检查了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109B")

    TalkEnd(0xFE)
    Return()

    # Function_7_A7F end

    def Function_8_109F(): pass

    label("Function_8_109F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12B2")
    EventBegin(0x0)

    ChrTalk(
        0x8,
        "这就出发去雷斯顿要塞吗？\x02",
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
            "【出发】\x01",          # 0
            "【整理装备】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1135"),
        (1, "loc_1278"),
        (SWITCH_DEFAULT, "loc_12AF"),
    )


    label("loc_1135")

    OP_4A(0xA, 255)
    OP_8C(0xA, 315, 400)

    ChrTalk(
        0x8,
        (
            "#693F好！\x01",
            "那么快上去吧！\x02\x03",
            "工房船『莱普尼兹号』，\x01",
            "向目的地雷斯顿要塞进发！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#803F#2P各位游击士……\x01",
            "博士的事就拜托你们了。\x02\x03",
            "#800F还有的是……\x01",
            "麻烦你们好好保护提妲。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11F2():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11F2)

    def lambda_1200():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1200)

    def lambda_120E():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_120E)
    TurnDirection(0x107, 0xA, 400)

    ChrTalk(
        0x107,
        "#560F工房长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，都包在我们身上吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们走了。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Call(0, 17)
    Jump("loc_12AF")

    label("loc_1278")

    OP_A2(0x572)

    ChrTalk(
        0x8,
        (
            "#691F明白了。\x01",
            "准备好了就说一声。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    OP_4B(0x8, 255)
    EventEnd(0x1)
    Return()

    label("loc_12AF")

    Jump("loc_17D3")

    label("loc_12B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_134E")

    ChrTalk(
        0xFE,
        (
            "#690F哦，稍微晚了些真是不好意思。\x02\x03",
            "要塞那边又来要求我们出动了。\x01",
            "我想今天之内\x01",
            "就可以做好准备了。\x02\x03",
            "嗯，希望和平时一样\x01",
            "不要发生什么意外就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D3")

    label("loc_134E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_END)), "loc_13E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1391")

    ChrTalk(
        0xFE,
        (
            "#690F骚乱中没有人员伤亡\x01",
            "就是不幸中的大幸了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E3")

    label("loc_1391")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#690F不过，\x01",
            "事情真是糟糕啊。\x02\x03",
            "唔，骚乱中没有人员伤亡\x01",
            "就是不幸中的大幸了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E3")

    Jump("loc_17D3")

    label("loc_13E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1557")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1429")

    ChrTalk(
        0xFE,
        (
            "#690F骚乱中没有人员伤亡\x01",
            "就是不幸中的大幸了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1554")

    label("loc_1429")

    OP_A2(0x4)
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(
        0xFE,
        (
            "#690F哦，是提妲丫头。\x02\x03",
            "事情真是糟糕啊。\x01",
            "没有受伤吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F…………………………\x02\x03",
            "#064F啊……是、是的！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "#692F……发生什么事了？\x01",
            "你一直在发呆啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#066F嗯、嗯。\x01",
            "没事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#691F是吗，没受伤的话，\x01",
            "那比什么都好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_1554")

    Jump("loc_17D3")

    label("loc_1557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1741")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1590")

    ChrTalk(
        0xFE,
        (
            "#690F哦，是提妲丫头。\x01",
            "多多保重哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173E")

    label("loc_1590")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#690F哦，是提妲丫头。\x01",
            "又成了拉赛尔老爷子的差使吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，是呢。\x01",
            "要到亚尔摩村去一趟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#692F亚尔摩村？\x01",
            "喂喂，没问题吗？\x02\x03",
            "之前在卡鲁迪亚隧道\x01",
            "不是受到袭击了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F嘿嘿，\x01",
            "这次有两个游击士做我的护卫啊，\x01",
            "所以怎么说都不要紧的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#692F你们好像是上次\x01",
            "来拿内燃引擎设备的……\x02\x03",
            "#691F哎，你也是游击士啊。\x01",
            "我还以为只是个盛气凌人的丫头呢。\x02\x03",
            "那么就没什么问题了。\x01",
            "路上小心点啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F嗯，\x01",
            "那么我们就出发了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_173E")

    Jump("loc_17D3")

    label("loc_1741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_END)), "loc_17D3")

    ChrTalk(
        0x8,
        (
            "#691F话说回来， \x01",
            "这也真是个有趣的巧合啊。\x02\x03",
            "那东西刚被军方还回来，\x01",
            "马上就又被老爷子借走了。\x02\x03",
            "那可是一般仓库都没有的\x01",
            "十分稀有的物件啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D3")

    TalkEnd(0xFE)
    Return()

    # Function_8_109F end

    def Function_9_17D7(): pass

    label("Function_9_17D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_17F7")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵－噢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1811")

    label("loc_17F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1811")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵～噢？\x02",
    )

    CloseMessageWindow()

    label("loc_1811")

    TalkEnd(0xFE)
    Return()

    # Function_9_17D7 end

    def Function_10_1815(): pass

    label("Function_10_1815")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2435")
    OP_A2(0x604)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -20510, 8000, 119230, 0)
    SetChrPos(0x102, -18980, 8000, 119430, 0)

    def lambda_1856():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1856)

    def lambda_1866():
        OP_6B(2750, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1866)
    OP_6D(-20140, 8000, 120700, 2000)

    ChrTalk(
        0x9,
        "啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "就像刚才我说的，\x01",
            "飞艇什么时候能来还不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "实在抱歉，\x01",
            "你们在游击士协会等一会儿吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯～其实……\x01",
            "我们稍微改变了一下计划。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F非常抱歉。\x01",
            "请问搭乘手续能取消吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这样啊……\x01",
            "唉，也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "在定期船到来之前，\x01",
            "是不需要支付取消手续费的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "把刚才的船票\x01",
            "还给我就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "把两张\x07\x02",
            "船票\x07\x00",
            "还了回去。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x370, 2)
    Sleep(500)
    OP_22(0xE2, 0x0, 0x64)
    OP_20(0x3E8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x56)

    ChrTalk(
        0x9,
        (
            "哎呀……\x01",
            "好像是军用警备飞艇来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "来得还真早啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F那、那么我们赶快……！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 600)

    def lambda_1AE4():
        OP_8E(0xFE, 0xFFFFB12C, 0x1F40, 0x192A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AE4)

    ChrTalk(
        0x102,
        (
            "#010F麻烦您了。\x01",
            "真是非常不好意思。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 600)

    def lambda_1B2E():
        OP_8E(0xFE, 0xFFFFB7F8, 0x1F40, 0x192A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B2E)

    ChrTalk(
        0x9,
        (
            "没什么。\x01",
            "欢迎两位下次再来乘坐。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6F(0x0, 1001)
    OP_A1(0x11, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x4, 0x20)
    SetChrPos(0x11, -34000, 17000, 180000, 0)
    SetChrFlags(0x11, 0x4)
    OP_A1(0x12, 0x5)
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    SetChrPos(0x12, -34000, -10000, 180000, 0)
    SetChrFlags(0x12, 0x4)
    OP_6F(0x3, 100)
    OP_B0(0x4, 0x1E)
    OP_6D(-34000, 17000, 170000, 0)
    OP_67(0, 26070, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(156000, 0)
    OP_6E(239, 0)
    StopSound(0x186A0, 0x3D090, 0x0)
    OP_6F(0x4, 470)
    OP_70(0x4, 0x24E)

    def lambda_1C2C():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x29810, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C2C)

    def lambda_1C47():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x29810, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1C47)
    OP_22(0x79, 0x1, 0x28)
    Sleep(100)
    OP_24(0x79, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x41)
    Sleep(100)
    OP_24(0x79, 0x46)
    Sleep(100)
    OP_24(0x79, 0x4B)
    Sleep(100)
    OP_24(0x79, 0x50)
    Sleep(100)
    OP_24(0x79, 0x55)
    Sleep(100)
    OP_24(0x79, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x5F)
    Sleep(100)
    OP_24(0x79, 0x64)
    WaitChrThread(0x11, 0x1)
    OP_66(0x0)
    OP_6A(0x11)

    def lambda_1CC3():
        OP_8C(0xFE, 180, 5)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1CC3)

    def lambda_1CD1():
        OP_8C(0xFE, 180, 5)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1CD1)

    def lambda_1CDF():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1CDF)

    def lambda_1CFA():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1CFA)
    Sleep(200)

    def lambda_1D1A():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1D1A)

    def lambda_1D28():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1D28)

    def lambda_1D36():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1D36)

    def lambda_1D51():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1D51)
    Sleep(200)

    def lambda_1D71():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1D71)

    def lambda_1D7F():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1D7F)

    def lambda_1D8D():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1D8D)

    def lambda_1DA8():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1DA8)
    Sleep(200)

    def lambda_1DC8():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1DC8)

    def lambda_1DD6():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1DD6)

    def lambda_1DE4():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1DE4)

    def lambda_1DFF():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1DFF)
    Sleep(200)

    def lambda_1E1F():
        OP_8C(0xFE, 180, 60)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1E1F)

    def lambda_1E2D():
        OP_8C(0xFE, 180, 60)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1E2D)

    def lambda_1E3B():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E3B)

    def lambda_1E56():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1E56)
    Sleep(200)

    def lambda_1E76():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E76)

    def lambda_1E91():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1E91)
    Sleep(200)

    def lambda_1EB1():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1EB1)

    def lambda_1ECC():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1ECC)
    Sleep(200)

    def lambda_1EEC():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1EEC)

    def lambda_1F07():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1F07)
    Sleep(200)

    def lambda_1F27():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F27)

    def lambda_1F42():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1F42)
    Sleep(200)

    def lambda_1F62():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F62)

    def lambda_1F7D():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1F7D)
    Sleep(200)

    def lambda_1F9D():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F9D)

    def lambda_1FB8():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1FB8)
    Sleep(800)

    def lambda_1FD8():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1FD8)

    def lambda_1FE6():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1FE6)
    Sleep(100)

    def lambda_1FF9():
        OP_8C(0xFE, 180, 40)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1FF9)

    def lambda_2007():
        OP_8C(0xFE, 180, 40)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2007)
    Sleep(100)

    def lambda_201A():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_201A)

    def lambda_2028():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2028)
    Sleep(100)

    def lambda_203B():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_203B)

    def lambda_2049():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2049)
    Sleep(100)

    def lambda_205C():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_205C)

    def lambda_206A():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_206A)
    OP_22(0xCC, 0x0, 0x64)
    OP_6F(0x4, 590)
    OP_70(0x4, 0x2B2)
    WaitChrThread(0x11, 0x1)

    def lambda_2090():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD508, 0x23280, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2090)

    def lambda_20AB():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD8F0, 0x23280, 0x29A, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_20AB)
    Sleep(100)

    def lambda_20CB():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD508, 0x23280, 0x618, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_20CB)

    def lambda_20E6():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD8F0, 0x23280, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_20E6)
    Sleep(100)
    OP_6A(0x0)
    ClearMapFlags(0x1)

    def lambda_210E():
        OP_67(-48240, 40960, 201970, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_210E)

    def lambda_2126():
        OP_6E(262, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2126)

    def lambda_2136():
        OP_6D(-32150, -6000, 142270, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2136)

    def lambda_214E():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD508, 0x23280, 0x79E, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_214E)

    def lambda_2169():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD8F0, 0x23280, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2169)
    Sleep(100)

    def lambda_2189():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD508, 0x23280, 0xA28, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2189)

    def lambda_21A4():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD8F0, 0x23280, 0x535, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_21A4)
    Sleep(100)

    def lambda_21C4():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD508, 0x23280, 0xF3C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21C4)

    def lambda_21DF():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD8F0, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_21DF)
    Sleep(100)

    def lambda_21FF():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD508, 0x23280, 0x1450, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21FF)

    def lambda_221A():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD8F0, 0x23280, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_221A)
    Sleep(100)
    WaitChrThread(0x11, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(600)
    OP_22(0x6D, 0x0, 0x64)
    OP_6F(0x4, 1)
    OP_70(0x4, 0xF)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_66(0x1)
    OP_44(0x101, 0xFF)
    OP_6D(-44580, -3800, 144110, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(3330, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x11, -33620, -11600, 144000, 180)
    SetChrPos(0x12, -33620, -10000, 144000, 180)
    OP_51(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x15, 0x1, 0x0, 0x17)
    OP_43(0x14, 0x1, 0x0, 0x16)
    OP_43(0x13, 0x1, 0x0, 0x15)
    OP_43(0xD, 0x1, 0x0, 0x14)
    FadeToBright(1000, 0)

    def lambda_234F():
        OP_6D(-34960, -3480, 144150, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_234F)

    def lambda_2367():
        OP_6B(3330, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2367)
    OP_6F(0x3, 100)
    OP_70(0x3, 0xC4)
    Sleep(500)
    OP_22(0x78, 0x0, 0x64)
    Sleep(3000)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#180F哼哼……\x01",
            "这段时间还真是忙啊。\x02\x03",
            "第一件事……\x01",
            "就是去拜会一下玛多克工房长。\x02\x03",
            "#188F不过，不愧是上校……\x01",
            "连这样的方法也能想得出来。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3A47")

    label("loc_2435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_END)), "loc_249B")

    ChrTalk(
        0x9,
        (
            "再等一会儿\x01",
            "『赛希莉亚号』就会来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "定期船到了之后，\x01",
            "把这个出示给乘务员就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A47")

    label("loc_249B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2651")
    OP_A2(0x602)
    OP_28(0x54, 0x1, 0x2)
    EventBegin(0x0)
    OP_69(0x9, 0x3E8)

    ChrTalk(
        0x9,
        "啊，你们好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我已经从雾香那里听说了。\x01",
            "现在就办理搭乘手续吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，麻烦您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那么，请你们在这张单子上\x01",
            "填写姓名和联络方式吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚办理了搭乘手续。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x9,
        (
            "好了，\x01",
            "这就是你们的船票。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "定期船到了之后，\x01",
            "向乘务员出示船票就可以了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到两张\x07\x02",
            "船票\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x370, 2)
    EventEnd(0x1)
    Jump("loc_3A47")

    label("loc_2651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3488")
    EventBegin(0x0)
    OP_A2(0x517)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -19410, 8000, 119800, 0)
    SetChrPos(0x102, -20670, 8000, 119780, 0)

    def lambda_2691():
        OP_6C(315000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2691)

    def lambda_26A1():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_26A1)
    OP_69(0x9, 0x7D0)

    ChrTalk(
        0x9,
        "#2P哟！客人是来乘坐定期船的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P很不巧，\x01",
            "上一班定期船刚刚开走……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F唔，不是呢。\x01",
            "我们不是来坐定期船的。\x02\x03",
            "我们是有事来找\x01",
            "那位叫格斯塔夫的维修长的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P怎么，要找大叔啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P不过很遗憾，\x01",
            "大叔他现在不在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎，出去了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P嗯，没错。\x01",
            "这两三天他去了雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P好像是突然接到了\x01",
            "那边军用飞艇的维修委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F说到雷斯顿要塞……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是位于瓦雷利亚湖畔的\x01",
            "王国军最大的军事基地。\x02\x03",
            "就在蔡斯地区的北面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唔～这样的话，\x01",
            "看来维修长可没有那么快回来啊。\x02\x03",
            "那博士要的东西该怎么办啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P虽然不知道你们有什么事，\x01",
            "不过我想他差不多也该回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P刚刚有连络通信过来……\x02",
    )

    CloseMessageWindow()
    OP_22(0xE2, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F咦……\x01",
            "下一班定期船已经来了？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(
        0x9,
        "啊，就是这个传说中的飞艇。\x02",
    )

    CloseMessageWindow()
    OP_A1(0x11, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x4, 0x20)
    SetChrPos(0x11, -34000, 9000, 177000, 180)
    SetChrFlags(0x11, 0x4)
    OP_A1(0x12, 0x5)
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    SetChrPos(0x12, -34000, -11150, 177000, 180)
    SetChrFlags(0x12, 0x4)
    OP_66(0x0)

    def lambda_2A13():
        OP_67(2310, 43070, 99410, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A13)

    def lambda_2A2B():
        OP_6D(-32150, 15520, 142270, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A2B)

    def lambda_2A43():
        OP_6B(900, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2A43)
    Sleep(2000)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 161)
    OP_70(0x4, 0x104)

    def lambda_2A6B():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2A6B)

    def lambda_2A86():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x26548, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2A86)
    OP_22(0x79, 0x1, 0x28)
    Sleep(100)
    OP_24(0x79, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x41)
    Sleep(100)
    OP_24(0x79, 0x46)
    Sleep(100)
    OP_24(0x79, 0x4B)
    Sleep(100)
    OP_24(0x79, 0x50)
    Sleep(100)
    OP_24(0x79, 0x55)
    Sleep(100)
    OP_24(0x79, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x5F)
    Sleep(100)
    OP_24(0x79, 0x64)
    Sleep(100)
    Sleep(2000)
    Sleep(100)

    def lambda_2B06():
        OP_67(2310, 60560, 99410, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B06)

    def lambda_2B1E():
        OP_8C(0xFE, 0, 5)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2B1E)

    def lambda_2B2C():
        OP_8C(0xFE, 0, 5)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2B2C)
    Sleep(100)

    def lambda_2B3F():
        OP_8C(0xFE, 0, 8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2B3F)

    def lambda_2B4D():
        OP_8C(0xFE, 0, 8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2B4D)
    Sleep(100)

    def lambda_2B60():
        OP_8C(0xFE, 0, 10)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2B60)

    def lambda_2B6E():
        OP_8C(0xFE, 0, 10)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2B6E)
    Sleep(100)

    def lambda_2B81():
        OP_8C(0xFE, 0, 13)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2B81)

    def lambda_2B8F():
        OP_8C(0xFE, 0, 13)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2B8F)
    Sleep(100)

    def lambda_2BA2():
        OP_8C(0xFE, 0, 15)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2BA2)

    def lambda_2BB0():
        OP_8C(0xFE, 0, 15)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2BB0)
    Sleep(100)

    def lambda_2BC3():
        OP_8C(0xFE, 0, 18)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2BC3)

    def lambda_2BD1():
        OP_8C(0xFE, 0, 18)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2BD1)

    def lambda_2BDF():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BDF)
    Sleep(85)

    def lambda_2BFF():
        OP_8C(0xFE, 0, 20)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2BFF)

    def lambda_2C0D():
        OP_8C(0xFE, 0, 20)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2C0D)
    Sleep(85)

    def lambda_2C20():
        OP_8C(0xFE, 0, 23)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2C20)

    def lambda_2C2E():
        OP_8C(0xFE, 0, 23)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2C2E)

    def lambda_2C3C():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C3C)
    Sleep(85)

    def lambda_2C5C():
        OP_8C(0xFE, 0, 25)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2C5C)

    def lambda_2C6A():
        OP_8C(0xFE, 0, 25)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2C6A)
    Sleep(85)

    def lambda_2C7D():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C7D)

    def lambda_2C98():
        OP_8C(0xFE, 0, 28)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2C98)

    def lambda_2CA6():
        OP_8C(0xFE, 0, 28)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2CA6)
    Sleep(85)

    def lambda_2CB9():
        OP_8C(0xFE, 0, 30)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2CB9)

    def lambda_2CC7():
        OP_8C(0xFE, 0, 30)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2CC7)
    Sleep(85)

    def lambda_2CDA():
        OP_8C(0xFE, 0, 33)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2CDA)

    def lambda_2CE8():
        OP_8C(0xFE, 0, 33)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2CE8)

    def lambda_2CF6():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2CF6)
    Sleep(85)
    Sleep(85)

    def lambda_2D1B():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2D1B)
    Sleep(170)

    def lambda_2D3B():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2D3B)
    Sleep(170)

    def lambda_2D5B():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2D5B)
    Sleep(170)

    def lambda_2D7B():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2D7B)
    Sleep(170)

    def lambda_2D9B():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2D9B)
    Sleep(170)
    WaitChrThread(0x11, 0x1)
    Sleep(1900)
    Sleep(200)

    def lambda_2DCA():
        OP_8C(0xFE, 0, 25)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2DCA)

    def lambda_2DD8():
        OP_8C(0xFE, 0, 25)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2DD8)
    Sleep(200)

    def lambda_2DEB():
        OP_8C(0xFE, 0, 20)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2DEB)

    def lambda_2DF9():
        OP_8C(0xFE, 0, 20)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2DF9)
    Sleep(200)

    def lambda_2E0C():
        OP_8C(0xFE, 0, 15)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2E0C)

    def lambda_2E1A():
        OP_8C(0xFE, 0, 15)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2E1A)
    Sleep(200)

    def lambda_2E2D():
        OP_8C(0xFE, 0, 10)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2E2D)

    def lambda_2E3B():
        OP_8C(0xFE, 0, 10)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2E3B)
    Sleep(200)

    def lambda_2E4E():
        OP_8C(0xFE, 0, 7)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2E4E)

    def lambda_2E5C():
        OP_8C(0xFE, 0, 7)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2E5C)
    WaitChrThread(0x11, 0x2)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 261)
    OP_70(0x4, 0x19A)

    def lambda_2E82():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2E82)

    def lambda_2E9D():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2E9D)
    Sleep(100)

    def lambda_2EBD():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2EBD)
    Sleep(100)

    def lambda_2EDD():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2EDD)
    Sleep(100)

    def lambda_2EFD():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2EFD)

    def lambda_2F18():
        OP_6D(-32150, 3000, 135270, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F18)
    Sleep(100)

    def lambda_2F35():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2F35)
    Sleep(100)

    def lambda_2F55():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2F55)
    Sleep(100)

    def lambda_2F75():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2F75)
    Sleep(100)

    def lambda_2F95():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2F95)
    Sleep(100)

    def lambda_2FB5():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2FB5)
    Sleep(100)

    def lambda_2FD5():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2FD5)
    Sleep(100)

    def lambda_2FF5():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2FF5)
    Sleep(100)

    def lambda_3015():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3015)
    Sleep(4500)
    Sleep(100)

    def lambda_303A():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_303A)
    Sleep(100)

    def lambda_305A():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_305A)
    Sleep(100)

    def lambda_307A():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_307A)
    Sleep(100)

    def lambda_309A():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_309A)
    Sleep(100)

    def lambda_30BA():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_30BA)
    Sleep(100)

    def lambda_30DA():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_30DA)
    Sleep(100)

    def lambda_30FA():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_30FA)
    Sleep(100)

    def lambda_311A():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_311A)
    Sleep(100)

    def lambda_313A():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_313A)
    Sleep(100)

    def lambda_315A():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_315A)
    OP_44(0x11, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x11, -34000, -11150, 148000, 0)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x46)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x1)
    Sleep(1100)
    OP_6F(0x3, 100)
    OP_70(0x3, 0xC8)
    Sleep(2500)
    OP_44(0x101, 0x1)
    Fade(1000)
    OP_44(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -36900, -3800, 140550, 90)
    OP_66(0x1)
    SetChrPos(0x101, -24600, 8000, 121410, 0)
    SetChrPos(0x102, -23560, 8000, 121480, 0)
    TurnDirection(0x9, 0x101, 0)
    OP_44(0x101, 0xFF)
    OP_6D(-23460, 8000, 121550, 0)
    OP_67(0, 9450, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_71(0x6, 0x4)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#004F橙色的定期船……\x02\x03",
            "咦咦。\x01",
            "有那样的定期船吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不……\x01",
            "好像不是定期船。\x02\x03",
            "很多地方的形状都和定期船不同，\x01",
            "而且还带有作业用的扶手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F啊，的确……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P这是中央工房所属的工房船\x01",
            "『莱普尼兹号』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P虽然和定期船是相同型号，\x01",
            "但追加了各种设备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P主要是用于\x01",
            "大型设备的维护和制品的搬运。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿～！\x01",
            "是在天上飞的工房啊。\x02\x03",
            "#006F工房船回来了，\x01",
            "那么维修长应该在飞艇里面吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P你们不是有事吗？\x01",
            "快点去找他吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        "#006F嗯，好的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        "#010F那么我们先告辞了。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_3A47")

    label("loc_3488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_34E6")

    ChrTalk(
        0x9,
        (
            "嗯？怎么了？\x01",
            "手续已经办好了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "定期船到了之后，\x01",
            "凭刚才的票就可以乘坐了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A47")

    label("loc_34E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3546")

    ChrTalk(
        0x9,
        "哟，你们也很忙呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好像工房船\x01",
            "有很紧急的任务要执行。\x01",
            "这边也已经乱成一团了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A47")

    label("loc_3546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_35BA")

    ChrTalk(
        0x9,
        (
            "『赛希莉亚号』\x01",
            "已经按预定的时间出航了………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔，就趁现在难得的空闲\x01",
            "集中精神看《利贝尔通讯》吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A47")

    label("loc_35BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3661")

    ChrTalk(
        0x9,
        "嗯嗯，对了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "说到封面……\x01",
            "最近《利贝尔通讯》上面的照片\x01",
            "都变得好漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯，一想到这个，\x01",
            "就很期待下期的封面啊。\x01",
            "……偷偷告诉你们啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3702")

    label("loc_3661")

    OP_A2(0x0)

    ChrTalk(
        0x9,
        (
            "中央工房的骚动\x01",
            "好像是起严重的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "竟然敢袭击中央工房，\x01",
            "世上还有这样无法无天的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唉，这样一来\x01",
            "下期《利贝尔通讯》的封面\x01",
            "就会是蔡斯了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3702")

    Jump("loc_3A47")

    label("loc_3705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_37CA")

    ChrTalk(
        0x9,
        (
            "那个，你们看过\x01",
            "《利贝尔通讯》最新一期了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "听说卢安的市长\x01",
            "是个无法无天的坏家伙，\x01",
            "已经被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过，空贼事件也好，\x01",
            "这个叫戴尔蒙的家伙也好……\x01",
            "最近这个世界真是不太平啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A47")

    label("loc_37CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_38A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3836")

    ChrTalk(
        0x9,
        (
            "现在西向航线的定期船\x01",
            "正按预定时间出发。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "希望定期船今天也能够\x01",
            "太平顺畅地运行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A0")

    label("loc_3836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3886")

    ChrTalk(
        0x9,
        (
            "我们老大应该就在\x01",
            "『莱普尼兹号』里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "赶快去问问他吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38A0")

    label("loc_3886")


    ChrTalk(
        0x9,
        "你们见到维修长了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_38A0")

    Jump("loc_3A47")

    label("loc_38A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_39D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3926")

    ChrTalk(
        0x9,
        (
            "听说，最后好像是游击士\x01",
            "解决了这次空贼事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真是的，明明发生了这么严重的事情，\x01",
            "王国军却什么事也做不了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39D1")

    label("loc_3926")

    OP_A2(0x0)

    ChrTalk(
        0x9,
        (
            "我读过利贝尔通讯了，\x01",
            "前段时间柏斯的空贼骚动\x01",
            "好像闹得很大啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "定期船停航了，\x01",
            "对我们接待员来说可真是噩梦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "要把事情向客人解释清楚，\x01",
            "可是一件很难的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D1")

    Jump("loc_3A47")

    label("loc_39D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A47")

    ChrTalk(
        0x9,
        (
            "目前，西向航线的『赛希莉亚号』\x01",
            "正停靠在飞艇坪中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "去往格兰赛尔的旅客，\x01",
            "请前往入口处准备登船。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A47")

    TalkEnd(0x9)
    Return()

    # Function_10_1815 end

    def Function_11_3A4B(): pass

    label("Function_11_3A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AD8")
    TalkBegin(0xA)

    ChrTalk(
        0xA,
        (
            "#800F今天乘务员们都很忙，\x01",
            "一会儿在飞船里是不能\x01",
            "对导力器进行修理维护的。\x02\x03",
            "你们最好趁现在到街上\x01",
            "把自己的装备整理好。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Jump("loc_4871")

    label("loc_3AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_472C")
    EventBegin(0x0)
    Fade(1000)
    OP_4A(0xA, 255)
    OP_4A(0x8, 255)
    SetChrPos(0x101, -46160, -4000, 141480, 90)
    SetChrPos(0x106, -44780, -4000, 140260, 0)
    SetChrPos(0x107, -45700, -4000, 140390, 45)
    SetChrPos(0x102, -45780, -4000, 142250, 135)
    TurnDirection(0xA, 0x107, 0)

    def lambda_3B44():
        OP_6C(45000, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B44)
    OP_6D(-45150, -4000, 141460, 0)
    OP_6B(3000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#800F哦哦，正等着你们呢。\x01",
            "大家都准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#051F啊啊，随时都能出发。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F『莱普尼兹号』的准备也完成了吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#801F啊，我们这次运气真好，\x01",
            "刚好要塞那边急着要我们发货。\x02\x03",
            "正好准备前往雷斯顿要塞。\x01",
            "　\x02\x03",
            "随时都可以出发哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    Sleep(200)
    OP_8C(0x101, 0, 400)
    Sleep(200)
    TurnDirection(0x101, 0xA, 400)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#505F随时……\x02\x03",
            "可是没看到那艘橙色的飞艇啊……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 315, 400)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0x102, 0xFFFF467E, 0xFFFFF060, 0x230F0, 0x7D0, 0x0)

    ChrTalk(
        0x102,
        "#010F艾丝蒂尔，看下面。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    def lambda_3D17():

        label("loc_3D17")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3D17")

    QueueWorkItem2(0xA, 2, lambda_3D17)

    def lambda_3D28():

        label("loc_3D28")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3D28")

    QueueWorkItem2(0x107, 2, lambda_3D28)

    def lambda_3D39():

        label("loc_3D39")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3D39")

    QueueWorkItem2(0x106, 2, lambda_3D39)

    def lambda_3D4A():
        OP_6D(-48810, -4000, 144860, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D4A)

    def lambda_3D62():
        OP_6C(314000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D62)

    def lambda_3D72():
        OP_6B(3500, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D72)
    Sleep(3000)

    def lambda_3D87():
        OP_8E(0x101, 0xFFFF4688, 0xFFFFF060, 0x22CE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3D87)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#501F#1P啊，在那里啊……\x02\x03",
            "那我们也要到下面去吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F#1P呵呵，姐姐。\x01",
            "我们不用下去啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        "#004F#1P咦……\x02",
    )

    CloseMessageWindow()
    OP_22(0xA7, 0x1, 0x55)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 315, 400)

    ChrTalk(
        0x101,
        "#004F#1P什、什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#2P飞艇的轨道……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F#2P怎么，你们连这都不知道吗？\x02\x03",
            "这个城镇的飞艇坪是\x01",
            "用超乎常识的方法来建造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#1P超、超乎常识？\x02",
    )

    CloseMessageWindow()
    OP_24(0xA7, 0x64)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 250)
    OP_70(0x0, 0x258)

    def lambda_3F13():
        OP_6C(339000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F13)
    OP_6D(-55390, -4000, 147110, 3000)
    StopSound(0xC350, 0x3D090, 0xFA0)
    Sleep(100)
    OP_22(0x9A, 0x0, 0x64)

    def lambda_3F4B():
        OP_6B(2200, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F4B)
    OP_67(0, 21600, -10000, 3500)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0xBB8, 0x64)
    Sleep(500)

    def lambda_3F87():
        OP_6B(3500, 6200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F87)

    def lambda_3F97():
        OP_6C(27000, 6100)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F97)
    OP_6D(-36640, -4000, 148800, 6100)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0xBB8, 0x64)
    Sleep(100)

    def lambda_3FD3():

        label("loc_3FD3")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3FD3")

    QueueWorkItem2(0x102, 0, lambda_3FD3)

    def lambda_3FE4():

        label("loc_3FE4")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3FE4")

    QueueWorkItem2(0x101, 0, lambda_3FE4)

    def lambda_3FF5():
        OP_8E(0xFE, 0xFFFF4B60, 0xFFFFF060, 0x226C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3FF5)

    def lambda_4010():
        OP_8E(0xFE, 0xFFFF4B38, 0xFFFFF060, 0x22B28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_4010)

    def lambda_402B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_402B)

    def lambda_4039():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_4039)

    def lambda_4047():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_4047)

    def lambda_4055():
        OP_6B(5500, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4055)

    def lambda_4065():
        OP_67(0, 4000, -10000, 11800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4065)
    OP_6C(90000, 9800)
    OP_73(0x0)
    OP_44(0x101, 0x1)
    OP_23(0xA7)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(1000)
    Fade(1000)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x64, 0x0)
    OP_71(0x6, 0x4)
    OP_A1(0x11, 0x4)
    OP_72(0x4, 0x4)
    OP_6F(0x4, 60)
    SetChrPos(0x11, -34000, -11150, 148000, 0)
    SetChrFlags(0x11, 0x4)
    OP_6B(3500, 0)
    OP_67(0, 11000, -10000, 0)
    StopSound(0xC350, 0x1FBD0, 0x0)
    OP_6D(-45210, -4000, 142090, 0)
    OP_6F(0x0, 1001)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#509F怎么说呢……\x01",
            "我还以为已经对这种玩意习惯了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，就是啊。\x01",
            "没想到还有这么厉害的设施啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#803F顺带说一下，\x01",
            "这个飞艇坪的构建理念也是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F知道啦。\x01",
            "又是拉赛尔博士的杰作对吧。\x02\x03",
            "#008F提妲啊，\x01",
            "你的爷爷还真是无所不能呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F#2P嘿嘿……\x01",
            "我也有同感呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -36460, -4000, 144380, 270)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x1)
    Sleep(1100)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 100)
    OP_70(0x3, 0xC8)
    OP_73(0x3)

    ChrTalk(
        0x8,
        "#6P哟，久等了。\x02",
    )

    CloseMessageWindow()
    OP_6D(-40270, -4000, 143040, 1000)

    ChrTalk(
        0x107,
        "#560F啊，维修长叔叔！\x02",
    )

    CloseMessageWindow()

    def lambda_42EE():
        OP_8E(0xFE, 0xFFFF57A4, 0xFFFFF128, 0x2329E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_42EE)

    def lambda_4309():

        label("loc_4309")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4309")

    QueueWorkItem2(0xA, 2, lambda_4309)

    def lambda_431A():
        OP_6D(-44110, -3800, 143890, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_431A)
    Sleep(100)

    def lambda_4337():
        OP_8E(0xFE, 0xFFFF4C0A, 0xFFFFF060, 0x2385C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_4337)
    Sleep(100)

    def lambda_4357():
        OP_8E(0xFE, 0xFFFF4A8E, 0xFFFFF060, 0x2341A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4357)
    Sleep(100)

    def lambda_4377():
        OP_8E(0xFE, 0xFFFF4AFC, 0xFFFFF060, 0x23082, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_4377)
    Sleep(100)

    def lambda_4397():
        OP_8E(0xFE, 0xFFFF4B56, 0xFFFFF060, 0x22CFE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_4397)
    WaitChrThread(0x102, 0x3)

    def lambda_43B7():

        label("loc_43B7")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_43B7")

    QueueWorkItem2(0x102, 2, lambda_43B7)
    WaitChrThread(0x101, 0x3)

    def lambda_43CD():

        label("loc_43CD")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_43CD")

    QueueWorkItem2(0x101, 2, lambda_43CD)
    WaitChrThread(0x107, 0x3)

    def lambda_43E3():

        label("loc_43E3")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_43E3")

    QueueWorkItem2(0x107, 2, lambda_43E3)
    WaitChrThread(0x106, 0x3)

    def lambda_43F9():

        label("loc_43F9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_43F9")

    QueueWorkItem2(0x106, 2, lambda_43F9)
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "#690F提妲啊，\x01",
            "详细情况我已经听工房长说了。\x02\x03",
            "没想到老爷子会遇到那样的事。\x01",
            "　\x02\x03",
            "#691F能帮上忙的话，\x01",
            "我们全体维修员随时乐意效劳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F谢、谢谢！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#051F抱歉，麻烦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#691F不要客气。\x01",
            "因为老爷子也是我的恩人啊。\x02\x03",
            "好了。\x01",
            "这边准备ＯＫ了。\x02\x03",
            "这就出发去雷斯顿要塞吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0xA, 0xFF)
    OP_8C(0xA, 315, 400)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【出发】\x01",          # 0
            "【整理装备】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_45A3"),
        (1, "loc_46EE"),
        (SWITCH_DEFAULT, "loc_4729"),
    )


    label("loc_45A3")

    OP_A2(0x561)
    OP_28(0x43, 0x1, 0x400)
    OP_28(0x44, 0x4, 0x2)
    OP_28(0x44, 0x4, 0x4)

    ChrTalk(
        0x8,
        (
            "#693F好！\x01",
            "那么快上去吧！\x02\x03",
            "工房船『莱普尼兹号』，\x01",
            "向目的地雷斯顿要塞进发！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#803F#2P各位游击士……\x01",
            "博士的事就拜托你们了。\x02\x03",
            "#800F还有的是……\x01",
            "麻烦你们好好保护提妲。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4668():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4668)

    def lambda_4676():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4676)

    def lambda_4684():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4684)
    TurnDirection(0x107, 0xA, 400)

    ChrTalk(
        0x107,
        "#560F工房长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，都包在我们身上吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们走了。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Call(0, 17)
    Jump("loc_4729")

    label("loc_46EE")

    OP_A2(0x572)

    ChrTalk(
        0x8,
        (
            "#691F明白了。\x01",
            "准备好了就说一声。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    OP_4B(0x8, 255)
    OP_43(0xA, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    label("loc_4729")

    Jump("loc_4871")

    label("loc_472C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_47A5")

    ChrTalk(
        0xA,
        (
            "#800F现在这边也正由格斯塔夫维修长\x01",
            "指挥进行起飞前的准备呢。\x01",
            "　\x02\x03",
            "如果你们准备好了，\x01",
            "就再到这儿来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486E")

    label("loc_47A5")

    OP_A2(0x3)

    ChrTalk(
        0xA,
        (
            "#800F哦哦，是你们啊。\x01",
            "已经准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F非常抱歉，\x01",
            "可能还要再费些时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#800F是吗。\x01",
            "现在这边也正由格斯塔夫维修长\x01",
            "指挥进行起飞前的准备呢。\x02\x03",
            "如果你们准备好了，\x01",
            "就再到这儿来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486E")

    TalkEnd(0xA)

    label("loc_4871")

    Return()

    # Function_11_3A4B end

    def Function_12_4872(): pass

    label("Function_12_4872")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_4924")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_48D0")

    ChrTalk(
        0xFE,
        (
            "看起来定期船\x01",
            "好像会晚点很长时间啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是先回家\x01",
            "再做打算吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4921")

    label("loc_48D0")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "看起来定期船\x01",
            "好像会晚点很长时间啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说军队要盘检，\x01",
            "真是麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4921")

    Jump("loc_4AFA")

    label("loc_4924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_49DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4956")

    ChrTalk(
        0xFE,
        (
            "说起来\x01",
            "我是不是来得太早了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49DA")

    label("loc_4956")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "哦～早上好啊。\x01",
            "你们也是要去王都吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我呀，\x01",
            "是要去飞艇公社办些事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且还想赶快把工作搞定，\x01",
            "顺便参观诞辰庆典……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49DA")

    Jump("loc_4AFA")

    label("loc_49DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4AFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4A45")

    ChrTalk(
        0xFE,
        (
            "飞艇的技术\x01",
            "真是越来越进步了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "乘坐定期船\x01",
            "到多杰的故乡\x01",
            "也不再是遥远的梦想了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AFA")

    label("loc_4A45")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "今天早上，\x01",
            "偶然遇到了来自共和国的\x01",
            "导力器商人多杰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为他要在飞艇坪参观，\x01",
            "我就热情地为他介绍了一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 270, 400)

    ChrTalk(
        0xFE,
        (
            "看，多杰。\x01",
            "那是器材的搬入口，\x01",
            "造船设施就在那个地下哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AFA")

    TalkEnd(0xFE)
    Return()

    # Function_12_4872 end

    def Function_13_4AFE(): pass

    label("Function_13_4AFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4B9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4B62")

    ChrTalk(
        0xFE,
        (
            "我将来也要\x01",
            "把飞艇作为商品……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但在那之前，\x01",
            "我的城镇得有个飞艇坪才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9E")

    label("loc_4B62")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "现在只能感叹眼前的景象了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "实在是太棒了。\x02",
    )

    CloseMessageWindow()

    label("loc_4B9E")

    TalkEnd(0xFE)
    Return()

    # Function_13_4AFE end

    def Function_14_4BA2(): pass

    label("Function_14_4BA2")

    Call(0, 10)
    Return()

    # Function_14_4BA2 end

    def Function_15_4BA7(): pass

    label("Function_15_4BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53FE")
    OP_A2(0x518)
    OP_28(0x3F, 0x1, 0x800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3F, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_4BCD")
    OP_28(0x3F, 0x1, 0x2000)

    label("loc_4BCD")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x0, 400)

    NpcTalk(
        0x8,
        "年长的维修员",
        (
            "#690F唔……\x01",
            "哎哟，小姑娘你们是……\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x0, -44000, -3800, 144340, 135)
    SetChrPos(0x1, -44420, -3800, 143430, 90)
    OP_6D(-40020, -3800, 143530, 0)
    OP_67(0, 6510, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(124000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#004F#6P啊……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "年长的维修员",
        (
            "#690F这个『莱普尼兹号』上\x01",
            "堆积着像山一样的各种器材。\x02\x03",
            "随便靠近可是很危险的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#6P啊，其实我们想找人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6P我们有点事情，\x01",
            "请问格斯塔夫维修长在里面吗……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "年长的维修员",
        "#692F怎么，找我有事啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#6P哎呀……\x01",
            "原来大叔就是维修长啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们向格斯塔夫维修长\x01",
            "说明了拉赛尔博士委托借用内燃引擎一事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#691F怎么。\x01",
            "原来是拉赛尔老爷子啊。\x02\x03",
            "要内燃引擎设备吗？\x01",
            "你们来得还真是时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#690F稍等一下……\x02",
    )

    CloseMessageWindow()

    def lambda_4E8C():

        label("loc_4E8C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4E8C")

    QueueWorkItem2(0x101, 0, lambda_4E8C)

    def lambda_4E9D():

        label("loc_4E9D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4E9D")

    QueueWorkItem2(0x102, 0, lambda_4E9D)

    def lambda_4EAE():
        OP_6D(-37020, -3800, 144870, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4EAE)
    OP_8E(0x8, 0xFFFF6E74, 0xFFFFF128, 0x23096, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFF85EE, 0xFFFFF128, 0x24432, 0xBB8, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#501F#1P难道就放在工房船上？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#1P嗯，好像是这样呢。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFF74C8, 0xFFFFF128, 0x23794, 0xBB8, 0x0)

    def lambda_4F4C():
        OP_6D(-42590, -3800, 143930, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F4C)
    OP_8E(0x8, 0xFFFF592A, 0xFFFFF128, 0x23294, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x8,
        (
            "#691F来。\x01",
            "很重的，小心哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x0, 0x2BC, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "内燃引擎设备\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x368, 1)
    OP_8F(0x8, 0xFFFF592A, 0xFFFFF128, 0x23294, 0xBB8, 0x0)
    OP_8C(0x8, 270, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50CB")

    ChrTalk(
        0x101,
        (
            "#004F哇哇……\x01",
            "的确是沉甸甸的啊。\x02\x03",
            "#006F但也不是重到拿不动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#692F嘿嘿，\x01",
            "想不到小姑娘还挺能干的嘛！\x02\x03",
            "#693F我很中意你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F嘿嘿，过奖啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_516A")

    label("loc_50CB")


    ChrTalk(
        0x102,
        (
            "#010F确实是很重……\x01",
            "不过也不至于重到拿不动就是了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#692F哦……\x01",
            "小伙子好样的。\x01",
            "现在的年轻人还是挺能干的嘛！\x02\x03",
            "#693F我挺中意你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F您过奖了。\x02",
    )

    CloseMessageWindow()

    label("loc_516A")


    ChrTalk(
        0x8,
        (
            "#691F话说回来，\x01",
            "这也真是个有趣的巧合啊。\x02\x03",
            "这东西刚从军方那里还回来，\x01",
            "马上就被老爷子借走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F从军方那里还回来？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F啊，没错啊。\x01",
            "那个货样被王国军借走了一阵子。\x02\x03",
            "说是什么研究要用。\x02\x03",
            "一直用到今天，\x01",
            "总算是还给我们工房了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F这样啊～\x01",
            "的确是有趣的巧合呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F约修亚，怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_END)), "loc_5335")

    ChrTalk(
        0x102,
        (
            "#015F不……没什么。\x02\x03",
            "#010F需要的东西都已经拿到了，\x01",
            "我们快点回博士那里吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5388")

    label("loc_5335")


    ChrTalk(
        0x102,
        (
            "#015F不……没什么。\x02\x03",
            "#010F……剩下的就是汽油了。\x01",
            "马上去中央工房的地下工场吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5388")


    ChrTalk(
        0x101,
        "#006F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#001F维修长大叔，谢谢您！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#691F别客气。\x01",
            "顺便帮我向老爷子问好哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    EventEnd(0x0)

    label("loc_53FE")

    Return()

    # Function_15_4BA7 end

    def Function_16_53FF(): pass

    label("Function_16_53FF")

    EventBegin(0x0)
    AddParty(0x6, 0xFF)
    SetChrPos(0x108, -45670, -4000, 146000, 0)
    SetChrPos(0x101, -46540, -4000, 147540, 0)
    SetChrPos(0x102, -47220, -4000, 146840, 0)
    SetChrPos(0x107, -47150, -4000, 145610, 0)
    TurnDirection(0x101, 0x108, 0)
    TurnDirection(0x102, 0x108, 0)
    TurnDirection(0x107, 0x108, 0)
    TurnDirection(0x108, 0x102, 0)
    OP_6D(-45760, -4000, 146000, 0)
    OP_67(0, 9090, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(111000, 0)
    OP_6E(262, 0)
    OP_6F(0x4, 1)
    OP_6F(0x3, 0)
    OP_71(0x6, 0x4)
    OP_6F(0x0, 1001)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x64, 0x0)
    OP_A2(0x559)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x10, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x108,
        (
            "#070F……真是抱歉，\x01",
            "要你们特地来为我送行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F这是当然的啦。\x01",
            "昨天真是受到你诸多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F金先生，\x01",
            "这就乘定期船直接去王都吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F啊啊……\x01",
            "我还有要事必须去办。\x02\x03",
            "要不是有事在身的话，\x01",
            "我一定会留在这里帮你们\x01",
            "调查绑架事件的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x107, 400)
    Sleep(400)

    ChrTalk(
        0x108,
        "#075F抱歉了，小姑娘。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F哪、哪儿的话呢。\x01",
            "您已经帮了我们很多忙了……\x02\x03",
            "金大哥哥，\x01",
            "真的非常感谢您呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈……\x01",
            "你能这么说真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开往王都的定期船\x01",
            "『赛希莉亚号』马上就要起飞了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请尚未登机的乘客尽快登机。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    ChrTalk(
        0x108,
        (
            "#070F哎呀……\x01",
            "差不多要出发了。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x108, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_574E():
        OP_6D(-40990, -4000, 146200, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_574E)

    def lambda_5766():
        OP_6B(3360, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5766)

    def lambda_5776():
        OP_6C(32000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5776)
    OP_8E(0x108, 0xFFFF4B9C, 0xFFFFF060, 0x23294, 0xBB8, 0x0)
    OP_8E(0x108, 0xFFFF5754, 0xFFFFF128, 0x2328A, 0xBB8, 0x0)
    SetChrFlags(0x108, 0x4)

    def lambda_57B3():
        OP_8E(0xFE, 0xFFFF50B0, 0xFFFFF060, 0x23A50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57B3)

    def lambda_57CE():
        OP_8E(0xFE, 0xFFFF4BD8, 0xFFFFF060, 0x23898, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57CE)

    def lambda_57E9():
        OP_8E(0xFE, 0xFFFF4BF6, 0xFFFFF060, 0x23532, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_57E9)
    OP_8E(0x108, 0xFFFF6FA0, 0xFFFFF128, 0x23294, 0xBB8, 0x0)
    TurnDirection(0x108, 0x107, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x108,
        (
            "#070F那再见了。\x01",
            "有机会我们再聚吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，嗯！\x02\x03",
            "想问一下，\x01",
            "金先生会在王国呆多久呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F明确时间还不知道……\x01",
            "我想会呆到女王诞辰庆典吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊，那样的话，\x01",
            "说不定我们还会再见面哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F到时就请多关照了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#071F哈哈，彼此彼此。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    OP_73(0x3)
    Fade(2000)
    OP_6D(-33750, -7050, 155120, 0)
    OP_67(0, -600, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(163000, 0)
    OP_6E(536, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x108, 0x80)
    Sleep(1000)
    OP_A1(0x11, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x4, 0x20)
    SetChrPos(0x11, -34000, -11150, 148000, 0)
    SetChrFlags(0x11, 0x4)
    OP_A1(0x12, 0x5)
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    SetChrPos(0x12, -34000, -11150, 148000, 0)
    SetChrFlags(0x12, 0x4)
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    OP_73(0x4)
    Sleep(1000)
    OP_22(0x77, 0x1, 0x64)
    OP_6F(0x4, 61)
    OP_70(0x4, 0xA0)
    OP_73(0x4)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 161)
    OP_70(0x4, 0x104)

    def lambda_5A2C():
        OP_6D(-33750, -5050, 155120, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A2C)

    def lambda_5A44():
        OP_67(0, 1800, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A44)
    OP_91(0x11, 0x0, 0x12C, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0x0, 0x320, 0x0, 0x1F4, 0x0)
    Sleep(2000)

    def lambda_5A89():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5A89)
    OP_94(0x1, 0x11, 0x0, 0x3E8, 0x3E8, 0x0)

    def lambda_5AAE():
        OP_94(0x1, 0xFE, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5AAE)
    OP_94(0x1, 0x11, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_5AD3():
        OP_94(0x1, 0xFE, 0x0, 0x578, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5AD3)
    OP_94(0x1, 0x11, 0x0, 0x578, 0xBB8, 0x0)

    def lambda_5AF8():
        OP_94(0x1, 0xFE, 0x0, 0x640, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5AF8)
    OP_94(0x1, 0x11, 0x0, 0x640, 0xFA0, 0x0)

    def lambda_5B1D():
        OP_94(0x1, 0xFE, 0x0, 0x708, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5B1D)
    FadeToDark(2000, 0, -1)
    OP_94(0x1, 0x11, 0x0, 0x708, 0x1388, 0x0)

    def lambda_5B4C():
        OP_94(0x1, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5B4C)
    OP_94(0x1, 0x11, 0x0, 0x7D0, 0x1770, 0x0)

    def lambda_5B71():
        OP_94(0x1, 0xFE, 0x0, 0x898, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5B71)
    OP_94(0x1, 0x11, 0x0, 0x898, 0x1B58, 0x0)

    def lambda_5B96():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5B96)

    def lambda_5BAC():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5BAC)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x5A, 0x0)
    OP_24(0x77, 0x5A)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x50, 0x0)
    OP_24(0x77, 0x50)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x46, 0x0)
    OP_24(0x77, 0x46)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x3C, 0x0)
    OP_24(0x77, 0x3C)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x32, 0x0)
    OP_24(0x77, 0x32)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x28, 0x0)
    OP_24(0x77, 0x28)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x1E, 0x0)
    OP_24(0x77, 0x1E)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x14, 0x0)
    OP_24(0x77, 0x14)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0xA, 0x0)
    OP_24(0x77, 0xA)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x1, 0x0)
    OP_23(0x77)
    OP_0D()
    OP_B8(0x7)
    RemoveParty(0x7, 0xFF)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_53FF end

    def Function_17_5D63(): pass

    label("Function_17_5D63")

    Sleep(100)
    OP_20(0x3E8)
    Fade(1000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0xA, 0xFF)
    OP_8C(0xA, 45, 0)
    SetChrPos(0xB, -45980, 0, 129680, 0)
    ClearChrFlags(0xB, 0x80)
    OP_23(0x75)
    OP_22(0x75, 0x1, 0x64)
    OP_6D(-36160, -4000, 150300, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(112000, 0)
    OP_6E(415, 0)
    OP_0D()
    OP_1D(0x57)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    OP_73(0x3)
    OP_72(0x4, 0x4)
    OP_A1(0x11, 0x4)
    OP_72(0x9, 0x4)
    OP_72(0x9, 0x20)
    SetChrPos(0x11, -34000, -11150, 148000, 0)
    SetChrFlags(0x11, 0x4)
    OP_A1(0x12, 0x5)
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    SetChrPos(0x12, -34000, -11150, 148000, 0)
    SetChrFlags(0x12, 0x4)

    def lambda_5E6F():
        OP_67(0, 7880, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E6F)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0x4, 1)
    OP_70(0x4, 0x3C)
    OP_73(0x4)
    OP_22(0x77, 0x1, 0x64)
    OP_6F(0x4, 61)
    OP_70(0x4, 0xA0)
    OP_73(0x4)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 161)
    OP_70(0x4, 0x104)

    def lambda_5EC6():
        OP_6E(465, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5EC6)

    def lambda_5ED6():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5ED6)
    OP_91(0x11, 0x0, 0x1F4, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0x0, 0x3E8, 0x0, 0x258, 0x0)
    Sleep(500)

    def lambda_5F13():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5F13)
    OP_94(0x1, 0x11, 0x0, 0x1F4, 0x3E8, 0x0)

    def lambda_5F38():
        OP_94(0x1, 0xFE, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5F38)
    OP_94(0x1, 0x11, 0x0, 0x258, 0x7D0, 0x0)

    def lambda_5F5D():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5F5D)
    OP_94(0x1, 0x11, 0x0, 0x2BC, 0xBB8, 0x0)

    def lambda_5F82():
        OP_94(0x1, 0xFE, 0x0, 0x320, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5F82)
    OP_94(0x1, 0x11, 0x0, 0x320, 0xFA0, 0x0)

    def lambda_5FA7():
        OP_94(0x1, 0xFE, 0x0, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5FA7)
    OP_94(0x1, 0x11, 0x0, 0x384, 0x1388, 0x0)

    def lambda_5FCC():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5FCC)
    OP_94(0x1, 0x11, 0x0, 0x3E8, 0x1770, 0x0)

    def lambda_5FF1():
        OP_94(0x1, 0xFE, 0x0, 0x44C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5FF1)
    OP_94(0x1, 0x11, 0x0, 0x44C, 0x1B58, 0x0)

    def lambda_6016():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6016)

    def lambda_602C():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_602C)
    OP_43(0x11, 0x3, 0x0, 0x12)
    OP_8C(0xA, 0, 400)

    ChrTalk(
        0xA,
        "#800F#5P拜托你们了，各位游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1P等、等一下～！\x02",
    )

    CloseMessageWindow()

    def lambda_608F():
        OP_6D(-44410, -4000, 143480, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_608F)

    def lambda_60A7():
        OP_6E(273, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_60A7)

    def lambda_60B7():

        label("loc_60B7")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_60B7")

    QueueWorkItem2(0xA, 1, lambda_60B7)
    OP_8E(0xB, 0xFFFF4A52, 0xFFFFF060, 0x23348, 0x1388, 0x0)

    ChrTalk(
        0xB,
        (
            "#152F#1P哈啊哈啊……\x02\x03",
            "啊啊～走掉了～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#802F#2P啊……\x01",
            "这不是朵洛希吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_8E(0xA, 0xFFFF4A2A, 0xFFFFF060, 0x22AC4, 0x7D0, 0x0)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(
        0xB,
        (
            "#152F#1P啊，工房长先生！\x02\x03",
            "刚才飞走的那艘飞艇，\x01",
            "是小艾和小约他们坐的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#802F#2P是啊……\x01",
            "你怎么知道的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#152F#1P我刚刚去了协会，\x01",
            "是那里的负责人告诉我的。\x02\x03",
            "刚才我和编辑部联络的时候，\x01",
            "知道了一件非常非常不得了的大事，\x01",
            "不告诉他们不行啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#805F#2P不得了的大事……？\x02\x03",
            "#806F唔……以现在的状况，\x01",
            "实在想不出还有什么更不得了的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#154F#1P这个嘛……\x01",
            "虽然是非公开发表的～\x02\x03",
            "女王陛下的王室亲卫队\x01",
            "好像以谋反的罪名被逮捕了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#804F#2P#3S什、什么！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/E0002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_5D63 end

    def Function_18_634A(): pass

    label("Function_18_634A")

    Sleep(1000)
    OP_24(0x77, 0x5F)
    OP_24(0x75, 0x5F)
    Sleep(200)
    OP_24(0x77, 0x5A)
    OP_24(0x75, 0x5A)
    Sleep(200)
    OP_24(0x77, 0x55)
    OP_24(0x75, 0x55)
    Sleep(200)
    OP_24(0x77, 0x50)
    OP_24(0x75, 0x50)
    Sleep(200)
    OP_24(0x77, 0x4B)
    OP_24(0x75, 0x4B)
    Sleep(200)
    OP_24(0x77, 0x46)
    OP_24(0x75, 0x46)
    Sleep(200)
    OP_24(0x77, 0x41)
    OP_24(0x75, 0x41)
    Sleep(200)
    OP_24(0x77, 0x3C)
    OP_24(0x75, 0x3C)
    Sleep(200)
    OP_24(0x77, 0x32)
    OP_24(0x75, 0x32)
    Sleep(200)
    OP_23(0x77)
    OP_23(0x75)
    Return()

    # Function_18_634A end

    def Function_19_63CB(): pass

    label("Function_19_63CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_733A")
    EventBegin(0x0)
    OP_A2(0x603)
    OP_28(0x54, 0x1, 0x4)
    OP_28(0x54, 0x1, 0x8)
    SetChrPos(0xC, -46060, 0, 127820, 0)
    ClearChrFlags(0xC, 0x80)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xC,
        "喵～呵。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6440():

        label("loc_6440")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_6440")

    QueueWorkItem2(0x101, 3, lambda_6440)

    def lambda_6451():

        label("loc_6451")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_6451")

    QueueWorkItem2(0x102, 3, lambda_6451)

    def lambda_6462():
        OP_6D(-46010, -1000, 131740, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6462)

    def lambda_647A():
        OP_67(0, 7390, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_647A)

    def lambda_6492():
        OP_6B(3700, 4000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6492)

    def lambda_64A2():
        OP_6C(158000, 4000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_64A2)
    Sleep(3000)
    SetChrPos(0x101, -45400, -4000, 140210, 0)
    SetChrPos(0x102, -46640, -4000, 140440, 0)

    def lambda_64D9():
        OP_8E(0xFE, 0xFFFF4DA4, 0xFFFFF060, 0x21D2C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_64D9)

    def lambda_64F4():
        OP_6D(-45610, -4000, 139000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_64F4)
    Sleep(3000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6656")

    ChrTalk(
        0x101,
        "#004F啊，安东尼！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F哟，昨天辛苦你了啊。\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xC,
        "喵呜～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F真是的，都是因为你，\x01",
            "昨天害我吓了一大跳呢。\x02\x03",
            "你是不是该反省一下呢，嗯？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xC,
        "咪呜？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F都不听我说话啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，说不定它是在装傻呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F唉，算了。\x01",
            "总之承蒙你的关照啦。\x02\x03",
            "多谢了，安东尼。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xC,
        "咪～呜嗯。\x02",
    )

    CloseMessageWindow()
    Jump("loc_678C")

    label("loc_6656")


    ChrTalk(
        0x101,
        "#004F啊，那只猫是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F就是那个时候\x01",
            "钻进集装箱里的那只猫吧。\x02\x03",
            "我记得，\x01",
            "好像是叫做安东尼。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xC,
        "喵呜～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈～真可爱。\x02\x03",
            "#006F真是的，都是因为你，\x01",
            "昨天害我吓了一大跳呢。\x02\x03",
            "你是不是该反省一下呢，嗯？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xC,
        "咪呜？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F都不听我说话啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，说不定它是在装傻呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_678C")

    SetChrPos(0x8, -47160, 0, 129750, 0)
    ClearChrFlags(0x8, 0x80)

    ChrTalk(
        0x8,
        "#3P哦，是你们啊！\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_67EC():
        OP_6D(-46010, -4000, 137720, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_67EC)

    def lambda_6804():

        label("loc_6804")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_6804")

    QueueWorkItem2(0x101, 3, lambda_6804)

    def lambda_6815():

        label("loc_6815")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_6815")

    QueueWorkItem2(0x102, 3, lambda_6815)

    def lambda_6826():
        OP_8E(0xFE, 0xFFFF4B92, 0xFFFFF060, 0x21E44, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6826)
    Sleep(1000)

    def lambda_6846():

        label("loc_6846")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_6846")

    QueueWorkItem2(0x101, 3, lambda_6846)

    def lambda_6857():

        label("loc_6857")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_6857")

    QueueWorkItem2(0x102, 3, lambda_6857)
    OP_8C(0xC, 192, 800)

    def lambda_686F():
        OP_8F(0xFE, 0xFFFF4DA4, 0x0, 0x1F521, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_686F)
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x101,
        "#501F啊，维修长先生！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#691F#2P工房长都告诉我了。\x01",
            "博士救出作战干得真是漂亮啊。\x02\x03",
            "博士对我们这些技术人员来说，\x01",
            "算是师傅一样的人物了。\x02\x03",
            "我也要好好感谢你们呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x101,
        (
            "#008F嘿嘿……\x01",
            "这也多亏了维修长你们的帮忙啊。\x02\x03",
            "不过我真是被那孩子吓坏了呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那个安东尼，\x01",
            "果然是您故意放进去的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#693F#2P啊哈哈，要想欺骗敌人，\x01",
            "首先要瞒过伙伴才行啊。\x02\x03",
            "#691F话说回来，\x01",
            "你们来飞艇坪有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，受博士的委托，\x01",
            "我们现在要赶往王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F要乘坐１１点的定期船，\x01",
            "看来好像来得早了点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#692F#2P啊啊……\x01",
            "好像要稍微晚到一会儿。\x02\x03",
            "#691F因为还要花点时间卸货，\x01",
            "你们到街上再转一会也没关系啦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F嗯，这样啊……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, -45980, 0, 128889, 0)
    OP_4A(0x9, 255)

    ChrTalk(
        0x9,
        "#3P喂，你们两位！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6B78():
        OP_8E(0x9, 0xFFFF4F8E, 0xFFFFF060, 0x21BC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6B78)

    def lambda_6B93():
        OP_6D(-46700, -2500, 134910, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6B93)

    def lambda_6BAB():

        label("loc_6BAB")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_6BAB")

    QueueWorkItem2(0x101, 2, lambda_6BAB)

    def lambda_6BBC():

        label("loc_6BBC")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_6BBC")

    QueueWorkItem2(0x102, 2, lambda_6BBC)

    def lambda_6BCD():

        label("loc_6BCD")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_6BCD")

    QueueWorkItem2(0x8, 2, lambda_6BCD)
    Sleep(1500)

    def lambda_6BE3():

        label("loc_6BE3")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6BE3")

    QueueWorkItem2(0x101, 2, lambda_6BE3)

    def lambda_6BF4():

        label("loc_6BF4")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6BF4")

    QueueWorkItem2(0x102, 2, lambda_6BF4)

    def lambda_6C05():

        label("loc_6C05")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6C05")

    QueueWorkItem2(0x8, 2, lambda_6C05)

    def lambda_6C16():
        OP_6D(-46010, -4000, 137720, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6C16)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x102, 0)

    ChrTalk(
        0x8,
        (
            "#692F#2P什么啊，这不是吉拉尔吗。\x02\x03",
            "怎么，发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "正好，\x01",
            "大叔您也在啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "实际上，事情变得麻烦起来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#692F#2P你说什么，麻烦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯，是啊……\x01",
            "飞艇公社发来的联络说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "定期船可能要\x01",
            "晚几个小时才能到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#6P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#692F#2P喂喂……\x01",
            "到底是怎么回事啊。\x02\x03",
            "又有空贼作乱吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "啊，说起来也差不多。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "据说，有一伙打算妨碍\x01",
            "女王陛下的诞辰庆典的恐怖分子\x01",
            "可能在王国的某个地方潜伏着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "为了调查这件事，\x01",
            "所有的飞艇坪都被军队设下了哨卡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F（那、那个是……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#6P（大概是为了搜寻博士他们吧……）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "所以，开往王都的定期船\x01",
            "现在还滞留在卢安那里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "取而代之的好像是\x01",
            "雷斯顿要塞的军用警备飞艇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#691F#2P原来如此，是这样啊。\x02\x03",
            "不过这样一来，\x01",
            "你不是就要很忙了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "是啊……\x01",
            "不把这件事告诉旅客们不行啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "就因为这样，\x01",
            "你们也得再等一段时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "对了……\x01",
            "如果你们愿意在游击士协会等的话，\x01",
            "我去帮你们联系一下吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F嗯，好的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#6P真是麻烦您了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 190, 400)
    OP_8F(0x9, 0xFFFF4C3C, 0x0, 0x1F982, 0xBB8, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    SetChrPos(0x9, -20110, 8000, 121830, 177)
    OP_4B(0x9, 255)
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#690F#2P……真是可疑啊。\x02\x03",
            "如果军队那帮家伙这样干的话，\x01",
            "莱普尼兹号肯定也会被检查的。\x02\x03",
            "我这就去和工房长说这件事。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_70D1():

        label("loc_70D1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_70D1")

    QueueWorkItem2(0x101, 2, lambda_70D1)

    def lambda_70E2():

        label("loc_70E2")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_70E2")

    QueueWorkItem2(0x102, 2, lambda_70E2)

    ChrTalk(
        0x101,
        (
            "#002F对啊，要是查起昨天那件事的话，\x01",
            "那中央工房就不好办了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F请一定要小心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#691F#2P哈哈，我还没有不中用到\x01",
            "让你们这些小孩子担心的份儿上呢。\x02\x03",
            "#693F那么告辞了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 190, 600)
    OP_8F(0x8, 0xFFFF4B92, 0x0, 0x1F8E2, 0xFA0, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_71D0():
        OP_6D(-45920, -4000, 139870, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71D0)
    TurnDirection(0x101, 0x102, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#002F约修亚……\x01",
            "这样不就很麻烦了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#013F嗯……\x01",
            "这样的话乘定期船就有点危险了。\x02\x03",
            "#012F虽然要花点时间，\x01",
            "不过还是走街道比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F唔，还以为好不容易\x01",
            "可以坐上久违的飞艇了呢。\x02\x03",
            "我跟你没完，理查德上校！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F算了算了，\x01",
            "当成是继续修行不也很好吗？\x02\x03",
            "#010F那么，我们赶快去接待处那里\x01",
            "把搭乘手续取消吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xC, 0x80)
    EventEnd(0x0)

    label("loc_733A")

    Return()

    # Function_19_63CB end

    def Function_20_733B(): pass

    label("Function_20_733B")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -34090, -4000, 144010, 270)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_20_733B end

    def Function_21_735E(): pass

    label("Function_21_735E")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -35750, -4000, 143010, 90)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_21_735E end

    def Function_22_7381(): pass

    label("Function_22_7381")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -35770, -4000, 144120, 90)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_22_7381 end

    def Function_23_73A4(): pass

    label("Function_23_73A4")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -36170, -4000, 145050, 90)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_23_73A4 end

    def Function_24_73C7(): pass

    label("Function_24_73C7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "定期船起降坪\x01",
            "≡　开往王都格兰赛尔\x01",
            "≡　开往卢安市\x02",
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

    # Function_24_73C7 end

    def Function_25_7461(): pass

    label("Function_25_7461")

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

    # Function_25_7461 end

    def Function_26_74DA(): pass

    label("Function_26_74DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7551")
    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F首先去把搭乘手续\x01",
            "去把票退掉吧。\x02\x03",
            "还是过会儿\x01",
            "然后我们再出发。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7551")

    Return()

    # Function_26_74DA end

    SaveToFile()

Try(main)
