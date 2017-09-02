from ED6ScenarioHelper import *

def main():
    # 社团大楼　学生会室

    CreateScenaFile(
        FileName            = 'T2521   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2521.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2521   ._SN',
            'ED6_DT01/T2521_1 ._SN',
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
        '米克',                                 # 9
        '德尼斯',                               # 10
        '乔儿',                                 # 11
        '汉斯',                                 # 12
        '约修亚',                               # 13
        '德波拉',                               # 14
        '凯诺娜上尉',                           # 15
        '雷克斯',                               # 16
        '卡拉',                                 # 17
        '卢希娅',                               # 18
        '亚鲁瓦教授',                           # 19
        '西加罗',                               # 20
        '艾德尔',                               # 21
        '罗基克',                               # 22
        'CH22000',                              # 23
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
        'ED6_DT07/CH01080 ._CH',             # 00
        'ED6_DT07/CH01360 ._CH',             # 01
        'ED6_DT07/CH02390 ._CH',             # 02
        'ED6_DT07/CH02550 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH02103 ._CH',             # 06
        'ED6_DT07/CH01023 ._CH',             # 07
        'ED6_DT07/CH01033 ._CH',             # 08
        'ED6_DT07/CH01070 ._CH',             # 09
        'ED6_DT07/CH02050 ._CH',             # 0A
        'ED6_DT07/CH01043 ._CH',             # 0B
        'ED6_DT07/CH01213 ._CH',             # 0C
        'ED6_DT07/CH01080 ._CH',             # 0D
        'ED6_DT06/CH20021 ._CH',             # 0E
        'ED6_DT07/CH00013 ._CH',             # 0F
        'ED6_DT07/CH02553 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH01080P._CP',             # 00
        'ED6_DT07/CH01360P._CP',             # 01
        'ED6_DT07/CH02390P._CP',             # 02
        'ED6_DT07/CH02550P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH02103P._CP',             # 06
        'ED6_DT07/CH01023P._CP',             # 07
        'ED6_DT07/CH01033P._CP',             # 08
        'ED6_DT07/CH01070P._CP',             # 09
        'ED6_DT07/CH02050P._CP',             # 0A
        'ED6_DT07/CH01043P._CP',             # 0B
        'ED6_DT07/CH01213P._CP',             # 0C
        'ED6_DT07/CH01080P._CP',             # 0D
        'ED6_DT06/CH20021P._CP',             # 0E
        'ED6_DT07/CH00013P._CP',             # 0F
        'ED6_DT07/CH02553P._CP',             # 10
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = -6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -31200,
        Z                   = 0,
        Y                   = 52500,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 28700,
        Z                   = 0,
        Y                   = 55100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 29600,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 29600,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -4970,
        Z                   = 250,
        Y                   = -4830,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -1700,
        Z                   = 250,
        Y                   = -1000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -3000,
        Z                   = 250,
        Y                   = 300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 550,
        Z                   = 0,
        Y                   = -2060,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4120,
        Z                   = 0,
        Y                   = 2470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 3960,
        Z                   = 100,
        Y                   = -5890,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 100,
        Y                   = -4200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -31470,
        Z                   = 0,
        Y                   = 58630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = -31350,
        Z                   = 330,
        Y                   = 23900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835022,
        ChipIndex           = 0xE,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -2200,
        Y                   = 0,
        Z                   = 50000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = -2200,
        Y                   = 0,
        Z                   = 42000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 2130,
        Y                   = 0,
        Z                   = 42010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 2200,
        Y                   = 0,
        Z                   = 50000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 24,
    )


    DeclActor(
        TriggerX            = 3340,
        TriggerZ            = 0,
        TriggerY            = 3110,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -31350,
        TriggerZ            = 330,
        TriggerY            = 23900,
        TriggerRange        = 500,
        ActorX              = -31350,
        ActorZ              = 500,
        ActorY              = 23900,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2920,
        TriggerZ            = 0,
        TriggerY            = 49990,
        TriggerRange        = 800,
        ActorX              = 2920,
        ActorZ              = 1000,
        ActorY              = 49990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -31560,
        TriggerZ            = 0,
        TriggerY            = 59430,
        TriggerRange        = 800,
        ActorX              = -31560,
        ActorZ              = 1000,
        ActorY              = 59430,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = 53550,
        TriggerRange        = 800,
        ActorX              = 0,
        ActorZ              = 1000,
        ActorY              = 53550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_446",          # 00, 0
        "Function_1_5BD",          # 01, 1
        "Function_2_680",          # 02, 2
        "Function_3_7FD",          # 03, 3
        "Function_4_821",          # 04, 4
        "Function_5_B1C",          # 05, 5
        "Function_6_D14",          # 06, 6
        "Function_7_F4D",          # 07, 7
        "Function_8_1613",         # 08, 8
        "Function_9_1BAB",         # 09, 9
        "Function_10_217E",        # 0A, 10
        "Function_11_28DC",        # 0B, 11
        "Function_12_28E1",        # 0C, 12
        "Function_13_2FDA",        # 0D, 13
        "Function_14_31B3",        # 0E, 14
        "Function_15_322A",        # 0F, 15
        "Function_16_325D",        # 10, 16
        "Function_17_329D",        # 11, 17
        "Function_18_3A48",        # 12, 18
        "Function_19_3AAC",        # 13, 19
        "Function_20_3B11",        # 14, 20
        "Function_21_3B86",        # 15, 21
        "Function_22_3B8A",        # 16, 22
        "Function_23_3B8E",        # 17, 23
        "Function_24_3B92",        # 18, 24
    )


    def Function_0_446(): pass

    label("Function_0_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_455")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_5BC")

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_45F")
    Jump("loc_5BC")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_49F")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 250, 0, -1810, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 280, 0, -3490, 0)
    Jump("loc_5BC")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4FB")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -28900, 0, 22980, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_5BC")

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_588")
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 0)), scpexpr(EXPR_END)), "loc_563")
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xB, 16)
    SetChrSubChip(0xB, 0)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -1800, 250, -1090, 270)
    SetChrPos(0xB, -3030, 250, 290, 180)
    Jump("loc_585")

    label("loc_563")

    SetChrPos(0xB, 3610, 0, 50080, 0)
    SetChrPos(0xC, 3610, 0, 50080, 0)

    label("loc_585")

    Jump("loc_5BC")

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_597")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_5BC")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_5A1")
    Jump("loc_5BC")

    label("loc_5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5AB")
    Jump("loc_5BC")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_5B5")
    Jump("loc_5BC")

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_5BC")

    label("loc_5BC")

    Return()

    # Function_0_446 end

    def Function_1_5BD(): pass

    label("Function_1_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5DE")
    OP_B1("t2521_y")
    Jump("loc_5E7")

    label("loc_5DE")

    OP_B1("t2521_n")

    label("loc_5E7")

    OP_64(0x1, 0x1)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_5FE")
    OP_65(0x1, 0x1)

    label("loc_5FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_612")
    OP_64(0x1, 0x1)
    SetChrFlags(0x16, 0x80)

    label("loc_612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_629")
    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    Jump("loc_62D")

    label("loc_629")

    OP_64(0x2, 0x1)

    label("loc_62D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_66A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x400)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_666")
    Jump("loc_66A")

    label("loc_666")

    OP_65(0x3, 0x1)

    label("loc_66A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67F")

    Return()

    # Function_1_5BD end

    def Function_2_680(): pass

    label("Function_2_680")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A5")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_7E7")

    label("loc_6A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_7E7")

    label("loc_6BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_7E7")

    label("loc_6D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_7E7")

    label("loc_6F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_709")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_7E7")

    label("loc_709")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_722")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_7E7")

    label("loc_722")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_7E7")

    label("loc_73B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_754")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_7E7")

    label("loc_754")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_7E7")

    label("loc_76D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_786")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_7E7")

    label("loc_786")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_7E7")

    label("loc_79F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_7E7")

    label("loc_7B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_7E7")

    label("loc_7D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_7E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7E7")

    label("loc_7FC")

    Return()

    # Function_2_680 end

    def Function_3_7FD(): pass

    label("Function_3_7FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_820")
    OP_8D(0xFE, -590, -1050, 1740, -4800, 3000)
    Jump("Function_3_7FD")

    label("loc_820")

    Return()

    # Function_3_7FD end

    def Function_4_821(): pass

    label("Function_4_821")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_88A")

    ChrTalk(
        0xFE,
        "呼啊啊啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，终于完了。\x01",
            "稍微休息一下就回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B18")

    label("loc_88A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_9A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_944")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我一点也不想\x01",
            "参加学园祭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "稍微偷下懒，\x01",
            "混过这一天算了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "为什么我要参加这种活动……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A6")

    label("loc_944")


    ChrTalk(
        0xFE,
        (
            "稍微偷下懒，\x01",
            "混过这一天算了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "为什么我要参加这种活动……\x02",
    )

    CloseMessageWindow()

    label("loc_9A6")

    Jump("loc_B18")

    label("loc_9A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_AA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3C")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "呼啊～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀哎呀～～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果在教室里无所事事，\x01",
            "那个多事的学生会长又会啰嗦了。\x01",
            "还是在这里打发时间吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9D")

    label("loc_A3C")


    ChrTalk(
        0xFE,
        (
            "如果在教室里无所事事，\x01",
            "那个多事的学生会长又会啰嗦了。\x01",
            "还是在这里打发时间吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9D")

    Jump("loc_B18")

    label("loc_AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_B18")

    ChrTalk(
        0xFE,
        (
            "学园祭的准备工作\x01",
            "真是麻烦死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "让想干的家伙\x01",
            "去干个够不就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B18")

    TalkEnd(0x8)
    Return()

    # Function_4_821 end

    def Function_5_B1C(): pass

    label("Function_5_B1C")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_CA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C58")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "为什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有那样杰出的求婚者，\x01",
            "而且还是两位……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 800)

    ChrTalk(
        0xFE,
        "哇，你们什么时候来的……\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "不、不要误会了，\x01",
            "刚才的是舞台剧的台词。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    Jump("loc_CA5")

    label("loc_C58")


    ChrTalk(
        0xFE,
        (
            "我可不想在\x01",
            "演出的时候弄错台词，\x01",
            "像个傻瓜一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "咕噜咕噜……\x02",
    )

    CloseMessageWindow()

    label("loc_CA5")

    Jump("loc_D10")

    label("loc_CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_D10")

    ChrTalk(
        0xFE,
        "唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们在干什么？\x01",
            "不要妨碍我学习呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D10")

    TalkEnd(0x9)
    Return()

    # Function_5_B1C end

    def Function_6_D14(): pass

    label("Function_6_D14")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_E88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E23")
    OP_A2(0x2)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "#640F啊，科洛丝……\x01",
            "孤儿院的孩子们都来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯，\x01",
            "大家都来玩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#640F是吗，把讨厌的事忘掉，\x01",
            "尽情地玩个够吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_E85")

    label("loc_E23")


    ChrTalk(
        0xFE,
        (
            "#640F让孤儿院的孩子们\x01",
            "把讨厌的事忘掉，\x01",
            "尽情地玩个够吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E85")

    Jump("loc_F49")

    label("loc_E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_F49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F11")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "#640F嗯，完成了。\x01",
            "估计就这些东西了。\x02\x03",
            "只要有这些东西，一定……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    Jump("loc_F49")

    label("loc_F11")


    ChrTalk(
        0xFE,
        (
            "#640F怎么了，你们三个。\x01",
            "玩得还愉快吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F49")

    TalkEnd(0xA)
    Return()

    # Function_6_D14 end

    def Function_7_F4D(): pass

    label("Function_7_F4D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_108F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF4")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "#733F咦，科洛丝和艾丝蒂尔……\x02\x03",
            "#730F放着两个可爱的女孩子不管，\x01",
            "约修亚那小子跑到哪里去了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_108C")

    label("loc_FF4")


    ChrTalk(
        0xFE,
        (
            "#730F演出一开始，\x01",
            "这座建筑物就要锁起来了。\x02\x03",
            "这也是为了保证安全啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108C")

    Jump("loc_160F")

    label("loc_108F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_10F7")

    ChrTalk(
        0xFE,
        (
            "#730F文件方面准备好了。\x02\x03",
            "接着只要取得校长的同意就行了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_160F")

    label("loc_10F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 2)), scpexpr(EXPR_END)), "loc_1604")

    ChrTalk(
        0xFE,
        (
            "#730F怎么了？\x02\x03",
            "现在就点菜吧？\x02",
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
            "【现在点菜】\x01",      # 0
            "【还有点事】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_119D"),
        (0, "loc_11E0"),
        (SWITCH_DEFAULT, "loc_1601"),
    )


    label("loc_119D")


    ChrTalk(
        0xFE,
        (
            "#730F好吧，\x01",
            "事情办完了赶快回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1601")

    label("loc_11E0")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-1640, 0, -1220, 0)
    SetChrPos(0x101, -1160, 0, -1960, 315)
    SetChrPos(0x105, -1530, 0, -3000, 0)
    SetChrPos(0x13B, -2250, 0, -2380, 0)
    SetChrSubChip(0xC, 1)
    OP_0D()

    ChrTalk(
        0x13B,
        (
            "#645F#3P啊～肚子咕咕叫了。\x02\x03",
            "忙着搞舞台剧的最后加工，\x01",
            "今天在学院里跑了整整一天……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F呵呵……\x01",
            "不过也就到今天为止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13B,
        (
            "#644F#3P是啊，真的呢。\x01",
            "得重新调整节奏了。\x02\x03",
            "而且又有新的事情要做……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#733F新的事情？\x01",
            "是什么事啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13B,
        (
            "#640F#3P嗯，一会儿再告诉你。\x02\x03",
            "#641F那么，为了预祝学园祭的成功，\x01",
            "今晚就好好地狂欢一番吧！\x02\x03",
            "艾丝蒂尔、约修亚。\x01",
            "明天就拜托你们了哦！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13B, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#006F嗯，看我们的吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#019F必定全力以赴演出。\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当晚，艾丝蒂尔他们\x01",
            "在食堂度过了开心热闹的一晚……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "最后，为了预祝舞台剧的成功，大家一起用饮料干杯。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "回宿舍之后，\x01",
            "艾丝蒂尔他们为了明天的活动都早早就寝了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "学园祭当天的早晨——\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x431)
    OP_A2(0x3FA)
    RemoveParty(0x3A, 0xFF)
    NewScene("ED6_DT01/T2523   ._SN", 113, 0, 0)
    IdleLoop()
    Jump("loc_1601")

    label("loc_1601")

    Jump("loc_160F")

    label("loc_1604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 0)), scpexpr(EXPR_END)), "loc_160F")
    Call(0, 9)

    label("loc_160F")

    TalkEnd(0xB)
    Return()

    # Function_7_F4D end

    def Function_8_1613(): pass

    label("Function_8_1613")

    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1638")
    SetChrSubChip(0xC, 2)
    Jump("loc_1669")

    label("loc_1638")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_164E")
    SetChrSubChip(0xC, 1)
    Jump("loc_1669")

    label("loc_164E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1664")
    SetChrSubChip(0xC, 0)
    Jump("loc_1669")

    label("loc_1664")

    SetChrSubChip(0xC, 2)

    label("loc_1669")

    OP_8C(0xC, 270, 0)
    SetChrFlags(0xC, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 2)), scpexpr(EXPR_END)), "loc_1B9C")

    ChrTalk(
        0xC,
        "#010F现在点菜吗？\x02",
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
            "【现在点菜】\x01",      # 0
            "【还有点事】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_171B"),
        (0, "loc_176A"),
        (SWITCH_DEFAULT, "loc_1B99"),
    )


    label("loc_171B")


    ChrTalk(
        0xC,
        (
            "#010F我们占着座位，\x01",
            "办完事情就赶快回来。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    Jump("loc_1B99")

    label("loc_176A")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-1640, 0, -1220, 0)
    SetChrPos(0x101, -1160, 0, -1960, 315)
    SetChrPos(0x105, -1530, 0, -3000, 0)
    SetChrPos(0x13B, -2250, 0, -2380, 0)
    SetChrSubChip(0xC, 1)
    OP_0D()

    ChrTalk(
        0x13B,
        (
            "#645F#3P啊～肚子咕咕叫了。\x02\x03",
            "忙着搞舞台剧的最后加工，\x01",
            "今天在学院里跑了整整一天……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F呵呵……\x01",
            "不过也就到今天为止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13B,
        (
            "#644F#3P是啊，真的呢。\x01",
            "得重新调整节奏了。\x02\x03",
            "而且又有新的事情要做……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#733F新的事情？\x01",
            "是什么事啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13B,
        (
            "#640F#3P嗯，一会儿再告诉你。\x02\x03",
            "#641F那么，为了预祝学园祭的成功，\x01",
            "今晚就好好地狂欢一番吧！\x02\x03",
            "艾丝蒂尔、约修亚。\x01",
            "明天就拜托你们了哦！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13B, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#006F嗯，看我们的吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#019F必定全力以赴演出。\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当晚，艾丝蒂尔他们\x01",
            "在食堂度过了开心热闹的一晚……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "最后，为了预祝舞台剧的成功，大家一起用饮料干杯。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "回宿舍之后，\x01",
            "艾丝蒂尔他们为了明天的活动都早早就寝了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "学园祭当天的早晨——\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMapFlags(0x100000)
    OP_22(0xD, 0x0, 0x64)
    OP_A2(0x431)
    OP_A2(0x3FA)
    RemoveParty(0x3A, 0xFF)
    NewScene("ED6_DT01/T2523   ._SN", 113, 0, 0)
    IdleLoop()
    Jump("loc_1B99")

    label("loc_1B99")

    Jump("loc_1BA7")

    label("loc_1B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 0)), scpexpr(EXPR_END)), "loc_1BA7")
    Call(0, 9)

    label("loc_1BA7")

    TalkEnd(0xC)
    Return()

    # Function_8_1613 end

    def Function_9_1BAB(): pass

    label("Function_9_1BAB")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-1640, 0, -1220, 0)
    SetChrPos(0x101, -1160, 0, -1960, 315)
    SetChrPos(0x105, -1530, 0, -3000, 0)
    SetChrPos(0x13B, -2250, 0, -2380, 0)
    SetChrSubChip(0xC, 1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 1)), scpexpr(EXPR_END)), "loc_1C23")

    ChrTalk(
        0x101,
        (
            "#503F嗯……\x01",
            "我们把她带来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C46")

    label("loc_1C23")


    ChrTalk(
        0x101,
        (
            "#001F呀嗬～⊙\x01",
            "我们把她带来了哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C46")


    ChrTalk(
        0x13B,
        "#641F#3P呵呵～大家辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#010F辛苦了，乔儿。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#730F哟，已经等你好久了。\x02\x03",
            "我们快点菜吧。\x02",
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
            "【现在点菜】\x01",      # 0
            "【还有点事】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1D45"),
        (0, "loc_1D99"),
        (SWITCH_DEFAULT, "loc_217D"),
    )


    label("loc_1D45")


    ChrTalk(
        0xC,
        (
            "#010F我们占着座位，\x01",
            "办完事情就赶快回来。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    OP_A2(0x44A)
    EventEnd(0x0)
    Jump("loc_217D")

    label("loc_1D99")


    ChrTalk(
        0x13B,
        (
            "#645F#3P啊～肚子咕咕叫了。\x02\x03",
            "忙着搞舞台剧的最后加工，\x01",
            "今天在学院里跑了整整一天……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F呵呵……\x01",
            "不过也就到今天为止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13B,
        (
            "#644F#3P是啊，真的呢。\x01",
            "得重新调整节奏了。\x02\x03",
            "而且又有新的事情要做……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#733F新的事情？\x01",
            "是什么事啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13B,
        (
            "#640F#3P嗯，一会儿再告诉你。\x02\x03",
            "#641F那么，为了预祝学园祭的成功，\x01",
            "今晚就好好地狂欢一番吧！\x02\x03",
            "艾丝蒂尔、约修亚。\x01",
            "明天就拜托你们了哦！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13B, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#006F嗯，看我们的吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#019F必定全力以赴演出。\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当晚，艾丝蒂尔他们\x01",
            "在食堂度过了开心热闹的一晚……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "最后，为了预祝舞台剧的成功，大家一起用饮料干杯。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "回宿舍之后，\x01",
            "艾丝蒂尔他们为了明天的活动都早早就寝了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "学园祭当天的早晨——\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMapFlags(0x100000)
    OP_22(0xD, 0x0, 0x64)
    OP_A2(0x431)
    OP_28(0x3D, 0x1, 0x800)
    OP_A2(0x3FA)
    RemoveParty(0x3A, 0xFF)
    NewScene("ED6_DT01/T2523   ._SN", 113, 0, 0)
    IdleLoop()
    Jump("loc_217D")

    label("loc_217D")

    Return()

    # Function_9_1BAB end

    def Function_10_217E(): pass

    label("Function_10_217E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285C")
    OP_A2(0x449)
    EventBegin(0x0)

    NpcTalk(
        0xB,
        "汉斯的声音",
        (
            "#2P……碧欧拉老师真是个美人啊。\x02\x03",
            "就算不怎么特意打扮，\x01",
            "也是十分漂亮呢。\x02\x03",
            "不过我对米丽亚老师\x01",
            "那冰冷眼镜后的美貌\x01",
            "也是心跳不止啊。\x02\x03",
            "眼镜这东西果然\x01",
            "还是和成熟的女性最相配。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "约修亚的声音",
        (
            "#1P唔，我对你的说法\x01",
            "没什么反对意见……\x02\x03",
            "不过这么说来，\x01",
            "你觉得乔儿怎么样？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "汉斯的声音",
        (
            "#2P并、并不是\x01",
            "带眼镜就一定会漂亮的。\x02\x03",
            "还必须要有大人的魅力才行。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "约修亚的声音",
        "#1P哈哈，你有点紧张哦。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "汉斯的声音",
        "#2P才没这回事呢。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x105)

    ChrTalk(
        0x101,
        (
            "#007F（说是去占座，\x01",
            "　竟然在聊这种事……）\x02\x03",
            "（真是拿男生没办法啊。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F（就连约修亚\x01",
            "　也在聊这种事……）\x02\x03",
            "（真是很意外呢。）\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "汉斯的声音",
        (
            "#2P……约修亚你呢，\x01",
            "和艾丝蒂尔发展到什么地步了？\x02\x03",
            "难道说……\x01",
            "已经到了『那个』的程度吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "约修亚的声音",
        (
            "#1P不好意思，\x01",
            "我们不是你想象的那样。\x02\x03",
            "该怎么说好呢……\x01",
            "总之不是那种关系啦。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "汉斯的声音",
        (
            "#2P哎……是吗。\x01",
            "我觉得你们是不错的一对呢。\x02\x03",
            "要不然，\x01",
            "你就大胆地去追科洛丝怎么样？\x02\x03",
            "你们练习的时候很合拍，\x01",
            "我想一定很般配的。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "约修亚的声音",
        "#1P你瞎说什么呢……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x105)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#503F（……我们还是去校长室吧。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#542F（是，是啊。\x01",
            "　还是去找乔儿吧……）\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_28DB")

    label("loc_285C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28AC")

    ChrTalk(
        0x101,
        (
            "#503F（还、还是去校长室\x01",
            "　叫乔儿去吃饭吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D9")

    label("loc_28AC")


    ChrTalk(
        0x105,
        (
            "#540F（啊、这个……\x01",
            "　还是不要打扰他们了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D9")

    EventEnd(0x1)

    label("loc_28DB")

    Return()

    # Function_10_217E end

    def Function_11_28DC(): pass

    label("Function_11_28DC")

    Call(0, 12)
    Return()

    # Function_11_28DC end

    def Function_12_28E1(): pass

    label("Function_12_28E1")

    TalkBegin(0xD)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                             # 0
            "买东西\x01",                           # 1
            "欢迎品尝「学院午餐」500米拉\x01",      # 2
            "离开\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_295A")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x30)
    OP_56(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_295A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A60")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2A26")
    SubMira(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "尝了尝\x07\x02",
            "学院午餐\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2BC)
    OP_31(0x1, 0xFD, 0x2BC)
    OP_31(0x2, 0xFD, 0x2BC)
    OP_31(0x3, 0xFD, 0x2BC)
    OP_31(0x4, 0xFD, 0x2BC)
    OP_31(0x5, 0xFD, 0x2BC)
    OP_31(0x6, 0xFD, 0x2BC)
    OP_31(0x7, 0xFD, 0x2BC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A18")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x9)"), scpexpr(EXPR_END)), "loc_29EB")
    Jump("loc_2A18")

    label("loc_29EB")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "学院午餐\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A18")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_2A4E")

    label("loc_2A26")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_2A4E")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xD)
    Return()

    label("loc_2A60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A7A")
    FadeToBright(300, 0)
    TalkEnd(0xD)
    Return()

    label("loc_2A7A")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2AB4")

    ChrTalk(
        0xD,
        (
            "欢迎光临。\x01",
            "想要点些什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2C15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BCC")
    OP_A2(0x4)

    ChrTalk(
        0xD,
        (
            "舞台剧我也看了哦。\x01",
            "你们真是非常努力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "辛苦你们了，\x01",
            "这是一点小意思，\x01",
            "就当是我看演出的门票吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "不用客气，吃吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC9")
    OP_A2(0x452)
    OP_3E(0x384, 1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "荧光菇\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2BC9")

    Jump("loc_2C12")

    label("loc_2BCC")


    ChrTalk(
        0xD,
        (
            "舞台剧我也看了哦。\x01",
            "你们真是非常努力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C12")

    Jump("loc_2FD6")

    label("loc_2C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2C78")

    ChrTalk(
        0xD,
        "你们要参加演出吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "阿姨我也要去看。\x01",
            "真是很期待呀，你们要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2CD4")

    ChrTalk(
        0xD,
        (
            "今天这里作为\x01",
            "休息的场所对公众开放。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不过和平时一样，\x01",
            "也可以点菜哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2D6E")

    ChrTalk(
        0xD,
        (
            "一直忙于学园祭的准备，\x01",
            "都还没吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "像你们这样的孩子\x01",
            "必须要好好摄取营养才能健康成长啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2DF7")

    ChrTalk(
        0xD,
        (
            "学园祭的准备，\x01",
            "还顺利吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "在准备期间我特别准备了丰盛的饭菜，\x01",
            "你们随时都能来用餐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_2E6F")

    ChrTalk(
        0xD,
        (
            "啊～\x01",
            "马上就要下课了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "同学们要来吃饭了，\x01",
            "必须加把劲呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2EE6")

    ChrTalk(
        0xD,
        (
            "呀，是科洛丝啊。\x01",
            "现在应该还在上课啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不好意思，\x01",
            "现在这边还在准备中。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_2F60")

    ChrTalk(
        0xD,
        (
            "啊，\x01",
            "你们两个是想来入学的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "就算不是学生也能来这里吃饭哦。\x01",
            "作为参观纪念想吃些什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2FD6")

    ChrTalk(
        0xD,
        (
            "这个学生食堂\x01",
            "假日里也会开放的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "如果饿了，\x01",
            "就不要客气，尽管点菜吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FD6")

    TalkEnd(0xD)
    Return()

    # Function_12_28E1 end

    def Function_13_2FDA(): pass

    label("Function_13_2FDA")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_310C")
    OP_A2(0x5)

    ChrTalk(
        0x101,
        (
            "#501F（啊，这个人……\x01",
            "　我好像在哪儿见到过。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（她是那个在空贼基地里\x01",
            "　和理查德上校一起出现的女性军官。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#181F呵呵，\x01",
            "上校他很久以前就想来\x01",
            "王立学院这里拜访了……\x02\x03",
            "可实在是抽不出空……\x02\x03",
            "相信不久之后\x01",
            "他就有空好好拜访这里了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31AF")

    label("loc_310C")


    ChrTalk(
        0xFE,
        (
            "#181F呵呵，\x01",
            "上校他很久以前就想来\x01",
            "王立学院这里拜访了……\x02\x03",
            "可实在是抽不出空……\x02\x03",
            "相信不久之后\x01",
            "他就有空好好拜访这里了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AF")

    TalkEnd(0xE)
    Return()

    # Function_13_2FDA end

    def Function_14_31B3(): pass

    label("Function_14_31B3")

    TalkBegin(0xF)

    ChrTalk(
        0xFE,
        (
            "我和妻子移居到\x01",
            "玛诺利亚村好几年了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "可王立学院还是第一次来。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xF)
    Return()

    # Function_14_31B3 end

    def Function_15_322A(): pass

    label("Function_15_322A")

    TalkBegin(0x10)

    ChrTalk(
        0xFE,
        (
            "真让人吃惊，\x01",
            "学园祭竟然这么热闹……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_15_322A end

    def Function_16_325D(): pass

    label("Function_16_325D")

    TalkBegin(0x11)

    ChrTalk(
        0xFE,
        (
            "嘿嘿，卢希娅我啊，\x01",
            "是和克拉姆他们一起来的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x11)
    Return()

    # Function_16_325D end

    def Function_17_329D(): pass

    label("Function_17_329D")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3921")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 4710, 0, 1390, 0)
    SetChrPos(0x105, 3350, 0, 1120, 0)
    SetChrPos(0x102, 3900, 0, 320, 0)
    OP_6D(4270, 0, 2180, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_8C(0xFE, 180, 0)
    OP_4A(0xFE, 255)
    OP_0D()
    OP_A2(0x459)

    ChrTalk(
        0x101,
        (
            "#004F…………咦？\x02\x03",
            "这不是亚鲁瓦教授吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#130F哎呀，\x01",
            "原来是艾丝蒂尔和约修亚啊。\x02\x03",
            "我们真是有缘啊。\x01",
            "看起来你们俩还是那么充满干劲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F教授也收到了\x01",
            "参加学园祭的邀请吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#130F不，很遗憾并不是这样。\x01",
            "我来学院是为了其他事情的。\x02\x03",
            "我来卢安是为了\x01",
            "考察这里的『绀碧之塔』。\x02\x03",
            "顺便来王立学院\x01",
            "看看有没有相关的研究资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F啊～还是那么热衷于工作呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#130F哈哈，在没钱的情况下，\x01",
            "支撑着自己的学术研究的\x01",
            "就只有这股热情和体力了啊。\x02\x03",
            "#132F说起来，这个学院的全部课程\x01",
            "似乎分为几大学科。\x02\x03",
            "请问有没有举办什么学术展览呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F有呢，不过三个学科之中\x01",
            "只有社会系办了展览……\x02\x03",
            "展览里面发表的都是\x01",
            "学生们的自主研究的作品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#130F哦哦，真是不错啊。\x01",
            "让我想起自己的学生时代来了。\x02\x03",
            "那请问学术展览\x01",
            "在哪里可以看到呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F这个嘛，\x01",
            "教授还是第一次来学院吧……\x02\x03",
            "嗯……该怎么跟你说呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F是啊。\x01",
            "这学院的建筑太多了……\x02\x03",
            "#040F如果可以的话，不如我们带您去吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#131F这样的话当然是最好不过……\x02\x03",
            "可是，大家都在高高兴兴地参加学园祭，\x01",
            "要麻烦你们实在是太不好意思了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F没事没事。\x01",
            "费不了什么事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#130F这样啊……\x01",
            "那就麻烦你们在方便的时候\x01",
            "带我到展览室一趟就行了。\x02\x03",
            "在那之前，\x01",
            "我就在这学生食堂等着好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    OP_4B(0xFE, 255)
    EventEnd(0x0)
    Jump("loc_3A44")

    label("loc_3921")


    ChrTalk(
        0xFE,
        (
            "#130F呵呵，话说回来，\x01",
            "在这时代做学生真是好啊……\x02\x03",
            "每天用那么少钱就可以吃饱睡饱，\x01",
            "真是羡慕死人了。\x02",
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
            "【继续参观学园祭】\x01",              # 0
            "【带教授到社会系教室参观】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A27"),
        (1, "loc_3A2A"),
        (SWITCH_DEFAULT, "loc_3A44"),
    )


    label("loc_3A27")

    Jump("loc_3A44")

    label("loc_3A2A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2520   ._SN", 123, 0, 0)
    IdleLoop()
    Jump("loc_3A44")

    label("loc_3A44")

    TalkEnd(0x12)
    Return()

    # Function_17_329D end

    def Function_18_3A48(): pass

    label("Function_18_3A48")

    TalkBegin(0x13)

    ChrTalk(
        0xFE,
        (
            "哎，\x01",
            "最近的学校真是好先进啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起上学，\x01",
            "我只读过主日学校呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_18_3A48 end

    def Function_19_3AAC(): pass

    label("Function_19_3AAC")

    TalkBegin(0x14)

    ChrTalk(
        0xFE,
        (
            "在旅行时听说了王立学院，\x01",
            "所以我们就想来看看。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_19_3AAC end

    def Function_20_3B11(): pass

    label("Function_20_3B11")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　学生会办公室　　　　\x01",
            "※谢绝外来人员进入。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_3B11 end

    def Function_21_3B86(): pass

    label("Function_21_3B86")

    SetPlaceName(0x71) # 社团大楼　学生会室
    Return()

    # Function_21_3B86 end

    def Function_22_3B8A(): pass

    label("Function_22_3B8A")

    SetPlaceName(0x72) # 社团大楼　学生会室
    Return()

    # Function_22_3B8A end

    def Function_23_3B8E(): pass

    label("Function_23_3B8E")

    SetPlaceName(0x75) # 社团大楼　学生会室
    Return()

    # Function_23_3B8E end

    def Function_24_3B92(): pass

    label("Function_24_3B92")

    SetPlaceName(0x70) # 社团大楼　学生会室
    Return()

    # Function_24_3B92 end

    SaveToFile()

Try(main)
