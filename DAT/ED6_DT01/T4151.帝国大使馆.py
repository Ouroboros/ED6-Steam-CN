from ED6ScenarioHelper import *

def main():
    # 帝国大使馆

    CreateScenaFile(
        FileName            = 'T4151   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4151.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T4101   ._SN',
            'ED6_DT01/T4101_1 ._SN',
            'ED6_DT01/T4101_2 ._SN',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '士兵',                                 # 9
        '士兵',                                 # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        '士兵',                                 # 14
        '士兵',                                 # 15
        '士兵',                                 # 16
        '士兵',                                 # 17
        '士兵',                                 # 18
        '士兵',                                 # 19
        '士兵',                                 # 20
        '士兵',                                 # 21
        '士兵',                                 # 22
        '士兵',                                 # 23
        '士兵',                                 # 24
        '王都格兰赛尔·北街区',                 # 25
        '王都格兰赛尔·南街区',                 # 26
        '王都格兰赛尔·空港',                   # 27
    )

    DeclEntryPoint(
        Unknown_00              = 54000,
        Unknown_04              = 250,
        Unknown_08              = 4000,
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
        'ED6_DT07/CH01650 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH00003 ._CH',             # 02
        'ED6_DT07/CH00013 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01650P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH00003P._CP',             # 02
        'ED6_DT07/CH00013P._CP',             # 03
    )

    DeclNpc(
        X                   = 74950,
        Z                   = 0,
        Y                   = 70230,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 79960,
        Z                   = 250,
        Y                   = 69120,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 83030,
        Z                   = 750,
        Y                   = -6740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 86990,
        Z                   = 750,
        Y                   = 68660,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 43000,
        Z                   = 1250,
        Y                   = 47060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 43000,
        Z                   = 1250,
        Y                   = 28960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 14,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17760,
        Z                   = 0,
        Y                   = 63880,
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
        X                   = 29270,
        Z                   = 0,
        Y                   = -950,
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
        X                   = 51010,
        Z                   = 0,
        Y                   = 102170,
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
        X                   = 109720,
        Y                   = 1000,
        Z                   = 32980,
        Range               = 2000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 76740,
        Y                   = 1000,
        Z                   = 23010,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 69950,
        Y                   = 1000,
        Z                   = 14290,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 63260,
        Y                   = 1000,
        Z                   = 22960,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 69910,
        Y                   = 1000,
        Z                   = 31710,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 42920,
        Y                   = 0,
        Z                   = 81110,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 70940,
        Y                   = 0,
        Z                   = -9490,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 75010,
        Y                   = 0,
        Z                   = 71300,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 24,
    )


    DeclActor(
        TriggerX            = 124880,
        TriggerZ            = -3500,
        TriggerY            = 70940,
        TriggerRange        = 800,
        ActorX              = 124880,
        ActorZ              = -2500,
        ActorY              = 70940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75060,
        TriggerZ            = 0,
        TriggerY            = 71950,
        TriggerRange        = 800,
        ActorX              = 75060,
        ActorZ              = 1000,
        ActorY              = 71950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 70950,
        TriggerZ            = 0,
        TriggerY            = -9930,
        TriggerRange        = 800,
        ActorX              = 70950,
        ActorZ              = 1000,
        ActorY              = -9930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_496",          # 00, 0
        "Function_1_4AE",          # 01, 1
        "Function_2_6AD",          # 02, 2
        "Function_3_82A",          # 03, 3
        "Function_4_A8C",          # 04, 4
        "Function_5_CEE",          # 05, 5
        "Function_6_D84",          # 06, 6
        "Function_7_DCA",          # 07, 7
        "Function_8_E10",          # 08, 8
        "Function_9_E7E",          # 09, 9
        "Function_10_EEC",         # 0A, 10
        "Function_11_F32",         # 0B, 11
        "Function_12_F78",         # 0C, 12
        "Function_13_FE6",         # 0D, 13
        "Function_14_1054",        # 0E, 14
        "Function_15_10C2",        # 0F, 15
        "Function_16_21B0",        # 10, 16
        "Function_17_236F",        # 11, 17
        "Function_18_242C",        # 12, 18
        "Function_19_2476",        # 13, 19
        "Function_20_24C0",        # 14, 20
        "Function_21_24C4",        # 15, 21
        "Function_22_24C8",        # 16, 22
        "Function_23_24CC",        # 17, 23
        "Function_24_24D0",        # 18, 24
    )


    def Function_0_496(): pass

    label("Function_0_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_4AD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FD)
    Event(0, 15)

    label("loc_4AD")

    Return()

    # Function_0_496 end

    def Function_1_4AE(): pass

    label("Function_1_4AE")

    OP_16(0x2, 0xFA0, 0xFFFF4C50, 0xFFFEA070, 0x3005C)
    OP_72(0xE, 0x20)
    OP_72(0xF, 0x20)
    OP_6F(0xE, 118)
    OP_6F(0xF, 118)
    OP_72(0x5, 0x10)
    OP_72(0x8, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x7, 0x10)
    OP_72(0x9, 0x10)
    OP_72(0xA, 0x10)
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50B")
    OP_72(0xB, 0x10)
    OP_65(0x0, 0x1)

    label("loc_50B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51E")
    OP_1B(0x9, 0x0, 0x11)

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_548")
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x2, 0x10)
    OP_72(0x3, 0x10)
    OP_72(0xB, 0x10)
    OP_72(0x4, 0x10)

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AC")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_43(0x8, 0x1, 0x0, 0x4)
    OP_43(0xA, 0x1, 0x0, 0x4)
    OP_43(0xB, 0x1, 0x0, 0x4)
    OP_43(0xC, 0x1, 0x0, 0x4)
    OP_43(0xD, 0x1, 0x0, 0x4)
    OP_43(0xE, 0x1, 0x0, 0x3)
    OP_43(0xF, 0x1, 0x0, 0x3)
    OP_43(0x10, 0x1, 0x0, 0x3)
    OP_43(0x11, 0x1, 0x0, 0x3)
    OP_43(0x12, 0x1, 0x0, 0x3)
    OP_43(0x13, 0x1, 0x0, 0x3)
    OP_43(0x14, 0x1, 0x0, 0x3)
    OP_43(0x15, 0x1, 0x0, 0x3)
    OP_43(0x16, 0x1, 0x0, 0x3)
    OP_43(0x17, 0x1, 0x0, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_613")

    label("loc_613")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_639")
    SetChrFlags(0x17, 0x80)
    OP_44(0x17, 0xFF)
    SetChrFlags(0x12, 0x80)
    OP_44(0x12, 0xFF)
    SetChrFlags(0x11, 0x80)
    OP_44(0x11, 0xFF)

    label("loc_639")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_671")
    SetChrFlags(0xC, 0x80)
    OP_44(0xC, 0xFF)
    SetChrFlags(0xD, 0x80)
    OP_44(0xD, 0xFF)
    SetChrFlags(0xE, 0x80)
    OP_44(0xE, 0xFF)
    SetChrFlags(0x13, 0x80)
    OP_44(0x13, 0xFF)
    SetChrFlags(0x14, 0x80)
    OP_44(0x14, 0xFF)

    label("loc_671")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_68E")
    SetChrFlags(0xF, 0x80)
    OP_44(0xF, 0xFF)
    SetChrFlags(0x16, 0x80)
    OP_44(0x16, 0xFF)

    label("loc_68E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_699")

    label("loc_699")

    OP_6B(4200, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AC")

    Return()

    # Function_1_4AE end

    def Function_2_6AD(): pass

    label("Function_2_6AD")

    RunExpression(0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D2")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_814")

    label("loc_6D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EB")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_814")

    label("loc_6EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_704")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_814")

    label("loc_704")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_814")

    label("loc_71D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_736")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_814")

    label("loc_736")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_814")

    label("loc_74F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_768")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_814")

    label("loc_768")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_781")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_814")

    label("loc_781")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_814")

    label("loc_79A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_814")

    label("loc_7B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_814")

    label("loc_7CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E5")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_814")

    label("loc_7E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FE")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_814")

    label("loc_7FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_814")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_814")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_829")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_814")

    label("loc_829")

    Return()

    # Function_2_6AD end

    def Function_3_82A(): pass

    label("Function_3_82A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A8B")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97A")

    label("loc_85D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_883")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97A")

    label("loc_883")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97A")

    label("loc_8A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97A")

    label("loc_8D0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97A")

    label("loc_8F6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97A")

    label("loc_91C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_941")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97A")

    label("loc_941")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_966")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97A")

    label("loc_966")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_97A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A88")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A79")

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

    label("loc_A79")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 106, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_A88")

    Jump("Function_3_82A")

    label("loc_A8B")

    Return()

    # Function_3_82A end

    def Function_4_A8C(): pass

    label("Function_4_A8C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CED")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDC")

    label("loc_ABF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDC")

    label("loc_AE5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDC")

    label("loc_B0B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B32")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDC")

    label("loc_B32")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B58")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDC")

    label("loc_B58")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B7E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDC")

    label("loc_B7E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDC")

    label("loc_BA3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDC")

    label("loc_BC8")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDB")

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

    label("loc_CDB")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 105, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_CEA")

    Jump("Function_4_A8C")

    label("loc_CED")

    Return()

    # Function_4_A8C end

    def Function_5_CEE(): pass

    label("Function_5_CEE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D83")
    SetChrPos(0xFE, 48010, 250, 59980, 270)
    OP_8E(0xFE, 0x8980, 0xFA, 0xEA4C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xBB8A, 0xFA, 0xEA4C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xBB8A, 0xFA, 0x10D6, 0xBB8, 0x0)
    OP_8E(0xFE, 0xA42E, 0xFA, 0x10D6, 0xBB8, 0x0)
    OP_8E(0xFE, 0xBB8A, 0xFA, 0x10D6, 0xBB8, 0x0)
    OP_8E(0xFE, 0xBB8A, 0xFA, 0xEA4C, 0xBB8, 0x0)
    Jump("Function_5_CEE")

    label("loc_D83")

    Return()

    # Function_5_CEE end

    def Function_6_D84(): pass

    label("Function_6_D84")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DC9")
    SetChrPos(0xFE, 39910, 0, 63710, 270)
    OP_8E(0xFE, 0x15E96, 0x0, 0xF8DE, 0xBB8, 0x0)
    OP_8E(0xFE, 0x9BE6, 0x0, 0xF8DE, 0xBB8, 0x0)
    Jump("Function_6_D84")

    label("loc_DC9")

    Return()

    # Function_6_D84 end

    def Function_7_DCA(): pass

    label("Function_7_DCA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E0F")
    SetChrPos(0xFE, 50960, 0, 16800, 0)
    OP_8E(0xFE, 0xC710, 0x0, 0xE6D2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xC710, 0x0, 0x41A0, 0xBB8, 0x0)
    Jump("Function_7_DCA")

    label("loc_E0F")

    Return()

    # Function_7_DCA end

    def Function_8_E10(): pass

    label("Function_8_E10")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E7D")
    SetChrPos(0xFE, 55970, 250, 6050, 0)
    OP_8E(0xFE, 0xDAA2, 0xFA, 0xE2E0, 0xBB8, 0x0)
    OP_8E(0xFE, 0x148CA, 0xFA, 0xE2E0, 0xBB8, 0x0)
    OP_8E(0xFE, 0x148CA, 0xFA, 0x1766, 0xBB8, 0x0)
    OP_8E(0xFE, 0xDAA2, 0xFA, 0x17A2, 0xBB8, 0x0)
    Jump("Function_8_E10")

    label("loc_E7D")

    Return()

    # Function_8_E10 end

    def Function_9_E7E(): pass

    label("Function_9_E7E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EEB")
    SetChrPos(0xFE, 53970, 250, 3940, 90)
    OP_8E(0xFE, 0x1502C, 0xFA, 0xF64, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1502C, 0xFA, 0xEA38, 0xBB8, 0x0)
    OP_8E(0xFE, 0xD2A0, 0xFA, 0xEA38, 0xBB8, 0x0)
    OP_8E(0xFE, 0xD2D2, 0xFA, 0xF64, 0xBB8, 0x0)
    Jump("Function_9_E7E")

    label("loc_EEB")

    Return()

    # Function_9_E7E end

    def Function_10_EEC(): pass

    label("Function_10_EEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F31")
    SetChrPos(0xFE, 54120, 250, 67800, 270)
    OP_8E(0xFE, 0x174F8, 0xFA, 0x108D8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xD368, 0xFA, 0x108D8, 0xBB8, 0x0)
    Jump("Function_10_EEC")

    label("loc_F31")

    Return()

    # Function_10_EEC end

    def Function_11_F32(): pass

    label("Function_11_F32")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F77")
    SetChrPos(0xFE, 95540, 250, -5740, 90)
    OP_8E(0xFE, 0xA6D6, 0xFA, 0xFFFFE994, 0xBB8, 0x0)
    OP_8E(0xFE, 0x17534, 0xFA, 0xFFFFE994, 0xBB8, 0x0)
    Jump("Function_11_F32")

    label("loc_F77")

    Return()

    # Function_11_F32 end

    def Function_12_F78(): pass

    label("Function_12_F78")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FE5")
    SetChrPos(0xFE, 42960, 0, -1020, 90)
    OP_8E(0xFE, 0x15F86, 0x0, 0xFFFFFC04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x15F86, 0x0, 0xE57E, 0xBB8, 0x0)
    OP_8E(0xFE, 0x15F86, 0x0, 0xFFFFFC04, 0xBB8, 0x0)
    OP_8E(0xFE, 0xA7D0, 0x0, 0xFFFFFC04, 0xBB8, 0x0)
    Jump("Function_12_F78")

    label("loc_FE5")

    Return()

    # Function_12_F78 end

    def Function_13_FE6(): pass

    label("Function_13_FE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1053")
    SetChrPos(0xFE, 61020, 1250, 53050, 180)
    OP_8E(0xFE, 0xEE5C, 0x4E2, 0x9088, 0xBB8, 0x0)
    OP_8E(0xFE, 0x134C0, 0x4E2, 0x9088, 0xBB8, 0x0)
    OP_8E(0xFE, 0x134C0, 0x4E2, 0xCE4A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xEE5C, 0x4E2, 0xCF3A, 0xBB8, 0x0)
    Jump("Function_13_FE6")

    label("loc_1053")

    Return()

    # Function_13_FE6 end

    def Function_14_1054(): pass

    label("Function_14_1054")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10C1")
    SetChrPos(0xFE, 77980, 1250, 52000, 180)
    OP_8E(0xFE, 0x1309C, 0x4E2, 0x945C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF262, 0x4E2, 0x945C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF262, 0x4E2, 0xCAF8, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1309C, 0x4E2, 0xCB20, 0xBB8, 0x0)
    Jump("Function_14_1054")

    label("loc_10C1")

    Return()

    # Function_14_1054 end

    def Function_15_10C2(): pass

    label("Function_15_10C2")

    EventBegin(0x0)
    OP_6D(39290, 1250, 35000, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(225000, 0)
    OP_6E(508, 0)
    SetChrPos(0x101, 65430, 1250, 36430, 90)
    SetChrPos(0x102, 63950, 1250, 36430, 90)
    FadeToBright(2000, 0)

    def lambda_1132():
        OP_6D(70100, 250, 42490, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1132)
    Sleep(4000)

    def lambda_114F():
        OP_8E(0xFE, 0x11526, 0x4E2, 0x960A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_114F)

    def lambda_116A():
        OP_8E(0xFE, 0x110A8, 0x4E2, 0x9272, 0xB54, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_116A)
    WaitChrThread(0x101, 0x1)

    def lambda_118A():
        OP_8E(0xFE, 0x11404, 0xFA, 0xA5A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_118A)
    WaitChrThread(0x102, 0x1)

    def lambda_11AA():
        OP_8E(0xFE, 0x10FC2, 0xFA, 0xA622, 0xB54, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11AA)
    WaitChrThread(0x101, 0x2)
    Fade(1000)
    OP_6B(1330, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#501F呼……\x01",
            "躲避着巡逻的士兵，\x01",
            "没想到不知不觉来到这种地方了呢。\x02\x03",
            "看起来，\x01",
            "这边好像已经没有士兵了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯……他们好像都撤退了。\x02\x03",
            "夜间巡逻也差不多该结束了。\x01",
            "　\x02\x03",
            "我们稍微休息一下就回旅馆吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006FＯＫ！\x02",
    )

    CloseMessageWindow()

    def lambda_1306():
        OP_67(0, 5350, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1306)

    def lambda_131E():
        OP_6C(135000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_131E)

    def lambda_132E():
        OP_6D(73240, 250, 45110, 3500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_132E)

    def lambda_1346():
        OP_6B(1600, 3500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1346)

    def lambda_1356():
        OP_8E(0xFE, 0x11E18, 0xFA, 0xAF5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1356)
    Sleep(400)

    def lambda_1376():
        OP_8E(0xFE, 0x11E18, 0xFA, 0xB324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1376)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 2)

    def lambda_13A7():
        OP_96(0xFE, 0x12016, 0x1C2, 0xAF5A, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13A7)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 270, 400)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 3)

    def lambda_13DB():
        OP_96(0xFE, 0x12016, 0x1C2, 0xB324, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13DB)
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#007F啊～发生了这么多事，\x01",
            "脑子还处于不清醒状态呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#019F哈哈……确实。\x02\x03",
            "#010F没想到在大圣堂等着我们的人\x01",
            "是尤莉亚中尉呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#501F啊，对了……\x02\x03",
            "约修亚最初认为那个送信的人\x01",
            "肯定不是尤莉亚小姐吧？\x02\x03",
            "不会是……\x01",
            "是我们以前见过的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F……那是…………\x02\x03",
            "#013F…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊……\x02\x03",
            "#506F对不起，算我没说。\x02\x03",
            "犯规了犯规了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F在约修亚愿意自己说出来之前，\x01",
            "是不会问你自己以前经历过的事情的。\x02\x03",
            "#505F虽然我一直在注意这个，\x01",
            "不过还是不小心忘记了呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F…………………………\x02\x03",
            "艾丝蒂尔，我……\x02\x03",
            "#010F我，和你一起旅行，\x01",
            "觉得自己已经变得坚强起来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#015F在同一片天空下生活的各种各样的人，\x01",
            "各种各样的人生……\x02\x03",
            "无数交织在一起的思念轨迹……\x02\x03",
            "每当感受到这些的时候，\x01",
            "就似乎找回了自己丢失的东西……\x02\x03",
            "这种感觉……真美好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F……约修亚……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F……大概这是错觉吧。\x02\x03",
            "尽管如此，我也……\x02\x03",
            "#015F我也要感谢和你一起生活的这些日子……\x01",
            "　\x02\x03",
            "这片天空，以及父亲……\x02\x03",
            "#010F当然还有艾丝蒂尔……你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F约修亚……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 1)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#015F所以……我们就此约定吧。\x02\x03",
            "如果这次的事情能够结束，\x01",
            "父亲平安地回来的话……\x02\x03",
            "#010F我就告诉你我自己以前种种的经历。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580F真、真的……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯。\x02\x03",
            "就和这片星空做个约定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F……………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#582F#3S……好，决定了！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_1B90():
        OP_67(0, 7000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B90)

    def lambda_1BA8():
        OP_6C(115000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1BA8)

    def lambda_1BB8():
        OP_6B(1400, 1500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1BB8)
    Sleep(500)
    SetChrChipByIndex(0x101, 65535)

    def lambda_1BD2():
        OP_96(0xFE, 0x11D28, 0xFA, 0xAF5A, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BD2)
    WaitChrThread(0x101, 0x1)
    OP_8E(0x101, 0x11B34, 0xFA, 0xAF5A, 0x7D0, 0x0)
    SetChrSubChip(0x102, 0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x102,
        "#014F艾丝蒂尔……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F该怎么说呢……\x01",
            "沉重的心情一扫而光呢。\x02\x03",
            "全部事情结束之后，\x01",
            "我也有话想对约修亚说呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F哎……啊啊。\x02\x03",
            "难道是那个烦恼的事情？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F对对，就是那个。\x02\x03",
            "#008F嘿嘿……\x01",
            "我已经做好准备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F准备……\x01",
            "是很让人烦恼的事情吗？\x02\x03",
            "#012F那么现在说出来也……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F不～行！\x02\x03",
            "说那种话，是要挑选时机的。\x01",
            "　\x02\x03",
            "#007F嗯～\x01",
            "虽然现在这气氛相当的好～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F？？？\x01",
            "虽然不太明白……\x02\x03",
            "#010F为了我们今天的约定，\x01",
            "明天的比赛一定不能输……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F那当然了！\x01",
            "怎么能让那种家伙们阻碍了呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#005F#3S看我用少女的力量，\x01",
            "把那些特务兵的家伙通通打飞！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F打飞……\x02\x03",
            "#011F……呼……\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x102, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x102,
        (
            "#512F呼……啊哈哈哈……！\x02\x03",
            "你……果然……\x01",
            "……不愧是父亲的女儿啊……\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F什么呀，这样说真是讨厌呢。\x02\x03",
            "我跟那样的不良中年到底有哪点像啦？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F嗯……是啊。\x02\x03",
            "明天的决赛，\x01",
            "我也有取胜的信心了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x100000)
    OP_22(0xD, 0x0, 0x64)
    Sleep(2000)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4132   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_10C2 end

    def Function_16_21B0(): pass

    label("Function_16_21B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2202")
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
    Jump("loc_236E")

    label("loc_2202")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2300")
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
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F看起来这里就是艾南先生所说的\x01",
            "地下水路的入口了。\x01",
            "　\x02\x03",
            "今天已经很晚了，\x01",
            "明天再和金先生他们一起进去看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_236E")

    label("loc_2300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236E")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "使用了\x07\x02",
            "地下水路的钥匙Ｂ\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x630)
    OP_70(0xB, 0x3C)
    OP_73(0xB)
    OP_64(0x0, 0x1)
    OP_71(0xB, 0x10)
    TalkEnd(0xFF)

    label("loc_236E")

    Return()

    # Function_16_21B0 end

    def Function_17_236F(): pass

    label("Function_17_236F")

    EventBegin(0x2)

    ChrTalk(
        0x102,
        (
            "#010F看起来这里就是艾南先生所说的\x01",
            "地下水路的入口了。\x01",
            "　\x02\x03",
            "今天已经很晚了，\x01",
            "明天再和金先生他们一起进去看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_17_236F end

    def Function_18_242C(): pass

    label("Function_18_242C")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门紧紧地关着，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_242C end

    def Function_19_2476(): pass

    label("Function_19_2476")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门紧紧地关着，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_2476 end

    def Function_20_24C0(): pass

    label("Function_20_24C0")

    SetPlaceName(0xBA) # 帝国大使馆
    Return()

    # Function_20_24C0 end

    def Function_21_24C4(): pass

    label("Function_21_24C4")

    SetPlaceName(0xB1) # 帝国大使馆
    Return()

    # Function_21_24C4 end

    def Function_22_24C8(): pass

    label("Function_22_24C8")

    SetPlaceName(0xBB) # 帝国大使馆
    Return()

    # Function_22_24C8 end

    def Function_23_24CC(): pass

    label("Function_23_24CC")

    SetPlaceName(0xBC) # 帝国大使馆
    Return()

    # Function_23_24CC end

    def Function_24_24D0(): pass

    label("Function_24_24D0")

    SetPlaceName(0xBD) # 帝国大使馆
    Return()

    # Function_24_24D0 end

    SaveToFile()

Try(main)
