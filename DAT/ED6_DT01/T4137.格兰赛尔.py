from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4137   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4137.x',
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
        'Olivier',                              # 9
        'Nial',                                 # 10
        'Dorothy',                              # 11
        'Editor-in-Chief',                      # 12
        'Grant',                                # 13
        'Kurt',                                 # 14
        'Cready',                               # 15
        'Spencer',                              # 16
        'Zane',                                 # 17
        'Olivier',                              # 18
        'Miele',                                # 19
        'Godfrey',                              # 20
        'Phoebe',                               # 21
        'Nana',                                 # 22
        'Baral',                                # 23
        'Connor',                               # 24
        'Noticia',                              # 25
        'Faults',                               # 26
        'Sariah',                               # 27
        'Private Dan',                          # 28
        'Private Aluts',                        # 29
        'Agate',                                # 30
        'Tita',                                 # 31
        'Russell',                              # 32
        ' ',                                    # 33
        ' ',                                    # 34
        ' ',                                    # 35
        ' ',                                    # 36
        ' ',                                    # 37
        ' ',                                    # 38
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
        'ED6_DT07/CH00030 ._CH',             # 00
        'ED6_DT07/CH02060 ._CH',             # 01
        'ED6_DT07/CH02070 ._CH',             # 02
        'ED6_DT07/CH01120 ._CH',             # 03
        'ED6_DT07/CH01260 ._CH',             # 04
        'ED6_DT07/CH01620 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT07/CH00070 ._CH',             # 08
        'ED6_DT06/CH20050 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01120 ._CH',             # 0B
        'ED6_DT07/CH02480 ._CH',             # 0C
        'ED6_DT07/CH02490 ._CH',             # 0D
        'ED6_DT07/CH01100 ._CH',             # 0E
        'ED6_DT07/CH01140 ._CH',             # 0F
        'ED6_DT07/CH01050 ._CH',             # 10
        'ED6_DT07/CH01140 ._CH',             # 11
        'ED6_DT07/CH01540 ._CH',             # 12
        'ED6_DT07/CH01300 ._CH',             # 13
        'ED6_DT07/CH00050 ._CH',             # 14
        'ED6_DT07/CH00060 ._CH',             # 15
        'ED6_DT07/CH02020 ._CH',             # 16
        'ED6_DT07/CH00003 ._CH',             # 17
        'ED6_DT07/CH00013 ._CH',             # 18
        'ED6_DT06/CH20086 ._CH',             # 19
        'ED6_DT06/CH20020 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT07/CH02060P._CP',             # 01
        'ED6_DT07/CH02070P._CP',             # 02
        'ED6_DT07/CH01120P._CP',             # 03
        'ED6_DT07/CH01260P._CP',             # 04
        'ED6_DT07/CH01620P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT07/CH00070P._CP',             # 08
        'ED6_DT06/CH20050P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01120P._CP',             # 0B
        'ED6_DT07/CH02480P._CP',             # 0C
        'ED6_DT07/CH02490P._CP',             # 0D
        'ED6_DT07/CH01100P._CP',             # 0E
        'ED6_DT07/CH01140P._CP',             # 0F
        'ED6_DT07/CH01050P._CP',             # 10
        'ED6_DT07/CH01140P._CP',             # 11
        'ED6_DT07/CH01540P._CP',             # 12
        'ED6_DT07/CH01300P._CP',             # 13
        'ED6_DT07/CH00050P._CP',             # 14
        'ED6_DT07/CH00060P._CP',             # 15
        'ED6_DT07/CH02020P._CP',             # 16
        'ED6_DT07/CH00003P._CP',             # 17
        'ED6_DT07/CH00013P._CP',             # 18
        'ED6_DT06/CH20086P._CP',             # 19
        'ED6_DT06/CH20020P._CP',             # 1A
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
        TalkScenaIndex      = 22,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -54180,
        Z                   = 0,
        Y                   = 61080,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x111,
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
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 5200,
        Z                   = 4000,
        Y                   = 2130,
        Direction           = 182,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 4560,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 186,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 4460,
        Z                   = 0,
        Y                   = -3910,
        Direction           = 94,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1D6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = -2029,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -3520,
        Z                   = 0,
        Y                   = -4540,
        Direction           = 6,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 58680,
        Z                   = 0,
        Y                   = -3720,
        Direction           = 188,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 59970,
        Z                   = 0,
        Y                   = -4990,
        Direction           = 263,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 61020,
        Z                   = 0,
        Y                   = 2490,
        Direction           = 197,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 61340,
        Z                   = 0,
        Y                   = 550,
        Direction           = 347,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -57020,
        Z                   = 0,
        Y                   = 61110,
        Direction           = 327,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -59180,
        Z                   = 0,
        Y                   = 59600,
        Direction           = 5,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -56630,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -3620,
        Z                   = 0,
        Y                   = -2020,
        Direction           = 171,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -3550,
        Z                   = 0,
        Y                   = -4570,
        Direction           = 9,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65562,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65562,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65562,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572890,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572890,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572890,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_542",          # 00, 0
        "Function_1_8AD",          # 01, 1
        "Function_2_8BE",          # 02, 2
        "Function_3_8D4",          # 03, 3
        "Function_4_8F8",          # 04, 4
        "Function_5_91C",          # 05, 5
        "Function_6_940",          # 06, 6
        "Function_7_9FE",          # 07, 7
        "Function_8_C02",          # 08, 8
        "Function_9_DD9",          # 09, 9
        "Function_10_EAB",         # 0A, 10
        "Function_11_1022",        # 0B, 11
        "Function_12_1762",        # 0C, 12
        "Function_13_2310",        # 0D, 13
        "Function_14_2D90",        # 0E, 14
        "Function_15_3231",        # 0F, 15
        "Function_16_3466",        # 10, 16
        "Function_17_3C18",        # 11, 17
        "Function_18_46F1",        # 12, 18
        "Function_19_488F",        # 13, 19
        "Function_20_49ED",        # 14, 20
        "Function_21_4AC2",        # 15, 21
        "Function_22_4C80",        # 16, 22
        "Function_23_50C3",        # 17, 23
        "Function_24_5721",        # 18, 24
        "Function_25_63C7",        # 19, 25
        "Function_26_6C37",        # 1A, 26
        "Function_27_6E8F",        # 1B, 27
        "Function_28_782F",        # 1C, 28
        "Function_29_7830",        # 1D, 29
        "Function_30_8EE2",        # 1E, 30
        "Function_31_A64B",        # 1F, 31
        "Function_32_C4B5",        # 20, 32
        "Function_33_DF41",        # 21, 33
    )


    def Function_0_542(): pass

    label("Function_0_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_550")
    OP_A3(0x3FA)
    Event(0, 28)

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_55E")
    OP_A3(0x3FB)
    Event(0, 29)

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_56C")
    OP_A3(0x3FC)
    Event(0, 30)

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_57A")
    OP_A3(0x3FD)
    Event(0, 33)

    label("loc_57A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_586"),
        (SWITCH_DEFAULT, "loc_5AF"),
    )


    label("loc_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_599")
    OP_A2(0x627)
    Event(0, 31)

    label("loc_599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AC")
    OP_A2(0x64E)
    Event(0, 32)

    label("loc_5AC")

    Jump("loc_5AF")

    label("loc_5AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D1")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 4650, 0, 600, 0)

    label("loc_5D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_675")
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 57670, 0, -5070, 111)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, 59920, 0, -5060, 275)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5860, 4000, -4760, 350)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -3620, 0, -2160, 186)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -3600, 0, -4420, 359)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 62780, 0, -3550, 162)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_8AC")

    label("loc_675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6C8")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -54200, 0, 63010, 194)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -53520, 0, 123230, 98)
    OP_43(0x18, 0x0, 0x0, 0x2)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_8AC")

    label("loc_6C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_6F9")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -54200, 0, 63010, 194)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Jump("loc_8AC")

    label("loc_6F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_74F")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5860, 4000, -4760, 350)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 62780, 0, -3550, 162)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_8AC")

    label("loc_74F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_759")
    Jump("loc_8AC")

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7C9")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -3620, 0, -2160, 186)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -3690, 0, -4720, 344)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x18, -60680, 0, 122710, 160)
    OP_43(0x18, 0x0, 0x0, 0x5)
    SetChrPos(0x19, -54350, 0, 1120, 265)
    OP_43(0x19, 0x0, 0x0, 0x2)
    Jump("loc_8AC")

    label("loc_7C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7D3")
    Jump("loc_8AC")

    label("loc_7D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_830")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -3620, 0, -2160, 186)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -3690, 0, -4720, 344)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x18, -63230, 0, 59560, 338)
    OP_43(0x18, 0x0, 0x0, 0x2)
    SetChrFlags(0x19, 0x80)
    Jump("loc_8AC")

    label("loc_830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_83A")
    Jump("loc_8AC")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_872")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_86F")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 910, 0, -3650, 189)
    SetChrPos(0xE, 610, 0, -3020, 146)

    label("loc_86F")

    Jump("loc_8AC")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_8AC")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5860, 4000, -4760, 350)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0x18, -63230, 0, 59560, 338)
    OP_43(0x18, 0x0, 0x0, 0x2)

    label("loc_8AC")

    Return()

    # Function_0_542 end

    def Function_1_8AD(): pass

    label("Function_1_8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_8BD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8BD")

    Return()

    # Function_1_8AD end

    def Function_2_8BE(): pass

    label("Function_2_8BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8D3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_8BE")

    label("loc_8D3")

    Return()

    # Function_2_8BE end

    def Function_3_8D4(): pass

    label("Function_3_8D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8F7")
    OP_8D(0xFE, 61240, -1420, 64280, -5700, 3000)
    Jump("Function_3_8D4")

    label("loc_8F7")

    Return()

    # Function_3_8D4 end

    def Function_4_8F8(): pass

    label("Function_4_8F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_91B")
    OP_8D(0xFE, -57970, 64269, -56460, 57520, 3000)
    Jump("Function_4_8F8")

    label("loc_91B")

    Return()

    # Function_4_8F8 end

    def Function_5_91C(): pass

    label("Function_5_91C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93F")
    OP_8D(0xFE, -62670, 124500, -59560, 120770, 3000)
    Jump("Function_5_91C")

    label("loc_93F")

    Return()

    # Function_5_91C end

    def Function_6_940(): pass

    label("Function_6_940")

    TalkBegin(0xFE)

    ChrTalk(
        0x10B,
        (
            "#100FWhew... The life of a fugitive is\x01",
            "most certainly not for the old!\x02\x03",
            "But thanks to you, I'm finally able\x01",
            "to retire from life on the lam, and\x01",
            "return to my prior days of peace.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_940 end

    def Function_7_9FE(): pass

    label("Function_7_9FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_A7E")

    ChrTalk(
        0x1E,
        (
            "#060FGrandpa promised he'd have\x01",
            "ice cream with me.\x02\x03",
            "I asked Agate to come too, but\x01",
            "he said he didn't want to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFE")

    label("loc_A7E")

    OP_A2(0x16)

    ChrTalk(
        0x1E,
        "#060FEstelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FWow, Tita, you look happy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#060F*giggle* Grandpa promised me\x01",
            "we could have ice cream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FOoh, ice cream! Ice cream is\x01",
            "goooood!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#060FYou bet it is!\x02\x03",
            "I asked Agate to come too, but\x01",
            "he said he didn't want to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FAgate eating ice cream... I'd\x01",
            "pay good money to see that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#060FI bet he'd like it if he tried\x01",
            "it, though!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFE")

    TalkEnd(0xFE)
    Return()

    # Function_7_9FE end

    def Function_8_C02(): pass

    label("Function_8_C02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_C6A")

    ChrTalk(
        0x106,
        (
            "#050FThe Martial Arts Tournament...\x02\x03",
            "Could be a good opportunity to\x01",
            "hone my skills...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD5")

    label("loc_C6A")

    OP_A2(0x15)

    ChrTalk(
        0x106,
        (
            "#050FThe Martial Arts Tournament...\x02\x03",
            "Could be a good opportunity to\x01",
            "hone my skills...\x02\x03",
            "And if 'Zane the Immovable' made\x01",
            "an appearance there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWhy don't you try to get in\x01",
            "next year, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050FMaybe. It might be nice, but it's\x01",
            "become such a circus...and I don't\x01",
            "like doing tricks for a crowd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F...Well, whatever floats your\x01",
            "boat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD5")

    TalkEnd(0xFE)
    Return()

    # Function_8_C02 end

    def Function_9_DD9(): pass

    label("Function_9_DD9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The Special Ops are supposedly keeping\x01",
            "watch over the capital, so the Royal\x01",
            "Garrison have been told to pull back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't agree with the order,\x01",
            "though. Honestly, I'm not even\x01",
            "sure who gave it!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_DD9 end

    def Function_10_EAB(): pass

    label("Function_10_EAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_F40")

    ChrTalk(
        0xFE,
        (
            "We have absolutely NO idea\x01",
            "what's going on around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are almost no regular\x01",
            "military troops in the capital\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101E")

    label("loc_F40")

    OP_A2(0x14)

    ChrTalk(
        0xFE,
        (
            "We have absolutely NO idea\x01",
            "what's going on around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are almost no regular\x01",
            "military troops in the capital\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have no idea whatsoever as to\x01",
            "the proper course of action from\x01",
            "here on out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101E")

    TalkEnd(0xFE)
    Return()

    # Function_10_EAB end

    def Function_11_1022(): pass

    label("Function_11_1022")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_10C4")

    ChrTalk(
        0xFE,
        (
            "I was shocked when I heard \x01",
            "Colonel Richard had tried\x01",
            "to stage a coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm just glad it was stopped\x01",
            "before it actually got started!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175E")

    label("loc_10C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1135")

    ChrTalk(
        0xFE,
        "What in the world is going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of the soldiers are being\x01",
            "called to pull out of the city!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175E")

    label("loc_1135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_11CB")

    ChrTalk(
        0xFE,
        (
            "Everyone is all caught up in the\x01",
            "Queen's Birthday Celebration...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But with all this hubbub, is it\x01",
            "even going to happen this year?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175E")

    label("loc_11CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1266")

    ChrTalk(
        0xFE,
        (
            "Dorothy seems to know the\x01",
            "team that won the Martial\x01",
            "Arts Competition this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She was practically dancing on\x01",
            "air when she came home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175E")

    label("loc_1266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_13BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_12EC")

    ChrTalk(
        0xFE,
        (
            "Dorothy's already gone; she\x01",
            "snatched up her camera and\x01",
            "ran off to the arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She seemed unusually focused!\x02",
    )

    CloseMessageWindow()
    Jump("loc_13B7")

    label("loc_12EC")

    OP_A2(0x12)

    ChrTalk(
        0xFE,
        (
            "Good morning! So, today's\x01",
            "the big day, no? The day of\x01",
            "the championship match!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dorothy's already gone; she\x01",
            "snatched up her camera and\x01",
            "ran off to the arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She seemed unusually focused!\x02",
    )

    CloseMessageWindow()

    label("loc_13B7")

    Jump("loc_175E")

    label("loc_13BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1445")

    ChrTalk(
        0xFE,
        (
            "It seems like the Royal Army\x01",
            "has been around constantly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My company's not to blame for\x01",
            "their heightened alert, I hope!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175E")

    label("loc_1445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_151C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_149C")

    ChrTalk(
        0xFE,
        "I love Colonel Richard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd love to do an exclusive\x01",
            "on him!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1519")

    label("loc_149C")

    OP_A2(0x12)

    ChrTalk(
        0xFE,
        "I love Colonel Richard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's smart, he's macho, he's\x01",
            "fit...he's HOT...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd love to do an exclusive\x01",
            "on him!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1519")

    Jump("loc_175E")

    label("loc_151C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_15C7")

    ChrTalk(
        0xFE,
        (
            "Nial's finally back from\x01",
            "his recent assignment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's known to just disappear for days\x01",
            "at a time, so every return of his is\x01",
            "kind of a special occasion!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175E")

    label("loc_15C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1623")

    ChrTalk(
        0xFE,
        (
            "A lot of reporters are gone\x01",
            "during the day; they're off\x01",
            "doing their legwork.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175E")

    label("loc_1623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_169D")

    ChrTalk(
        0xFE,
        (
            "After work I was going to go\x01",
            "hang out with Dorothy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But she seems to have her hands\x01",
            "full right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175E")

    label("loc_169D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_175E")

    ChrTalk(
        0xFE,
        (
            "Welcome to the Liberl News!\x01",
            "Despite our name, we're totally\x01",
            "nonpartisan, I SWEAR! *wink*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First floor is information,\x01",
            "second floor is the newsroom,\x01",
            "and third floor is printing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175E")

    TalkEnd(0xFE)
    Return()

    # Function_11_1022 end

    def Function_12_1762(): pass

    label("Function_12_1762")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_17C2")

    ChrTalk(
        0xFE,
        (
            "I'm off to cover this ice\x01",
            "cream shop that people've\x01",
            "been lining up to eat at.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230C")

    label("loc_17C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_18C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_182F")

    ChrTalk(
        0xFE,
        "Nial got arrested by the army?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man... Glad I got assigned\x01",
            "to the culture section!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C1")

    label("loc_182F")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        "Nial got arrested by the army?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it was bound to happen\x01",
            "sooner or later!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man... Glad I got assigned\x01",
            "to the culture section!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C1")

    Jump("loc_230C")

    label("loc_18C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1A14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1956")

    ChrTalk(
        0xFE,
        (
            "I was all ready to go cover\x01",
            "the Anterose in Bose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I have to come up with\x01",
            "something else to write about.\x01",
            "Le sigh!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A11")

    label("loc_1956")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        "Aww, the airships are stopped!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was all ready to go cover\x01",
            "the Anterose in Bose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I have to think of something\x01",
            "else to write! Cruel fate, why\x01",
            "must you mock me so?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A11")

    Jump("loc_230C")

    label("loc_1A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1C04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1AE2")

    ChrTalk(
        0xFE,
        (
            "Only the culture reporter gets\x01",
            "to go to different restaurants\x01",
            "and comment on the cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't wait to see the look\x01",
            "on Nial's face when I tell him\x01",
            "what I'm getting paid to do!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C01")

    label("loc_1AE2")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "Heh, my newest article is a \x01",
            "showcase piece for all of the\x01",
            "most popular restaurants here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Only the culture reporter gets\x01",
            "to go to different restaurants\x01",
            "and comment on the cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't wait to see the look\x01",
            "on Nial's face when I tell him\x01",
            "what I'm getting paid to do!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C01")

    Jump("loc_230C")

    label("loc_1C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1E3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1CFE")

    ChrTalk(
        0xFE,
        (
            "Dorothy only just started, but let me tell\x01",
            "you, she's got a TON of initiative...but not\x01",
            "enough Faults, if you get my drift! Eh? Eh?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think the real hero here, though,\x01",
            "is the editor brave enough to hire\x01",
            "a girl like her...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E39")

    label("loc_1CFE")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "Dorothy only just started, but let me tell\x01",
            "you, she's got a TON of initiative...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's a real shutterbug, snapping photos of\x01",
            "everything from the tournament to restaurant\x01",
            "cuisine-- and all of 'em look great!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think the real hero here, though,\x01",
            "is the editor brave enough to hire\x01",
            "a girl like her...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E39")

    Jump("loc_230C")

    label("loc_1E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1FC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1ED2")

    ChrTalk(
        0xFE,
        (
            "Lots of my editors and writers\x01",
            "always get sick as the deadline\x01",
            "approaches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And let me tell you, that's no\x01",
            "good for anyone!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FBF")

    label("loc_1ED2")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "Lots of my editors and writers\x01",
            "always get sick near deadline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's an unfortunate cocktail of\x01",
            "stress, insomnia and poor diet,\x01",
            "if you ask me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Or they're just playing\x01",
            "hooky. The results are still\x01",
            "the same, either way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FBF")

    Jump("loc_230C")

    label("loc_1FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_213D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_2058")

    ChrTalk(
        0xFE,
        (
            "I grabbed an airship to go pick\x01",
            "up a much-needed manuscript the\x01",
            "other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But wouldn't you know it, it\x01",
            "wasn't done yet!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_213A")

    label("loc_2058")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "I grabbed an airship to go pick\x01",
            "up a much-needed manuscript the\x01",
            "other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But wouldn't you know it, it\x01",
            "wasn't done yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If more people used orbal\x01",
            "communications, it'd be so much\x01",
            "easier to stay in touch...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_213A")

    Jump("loc_230C")

    label("loc_213D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2147")
    Jump("loc_230C")

    label("loc_2147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_21EC")

    ChrTalk(
        0xFE,
        (
            "Today I'm taking an airship\x01",
            "to go get a manuscript.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I don't finish getting ready\x01",
            "soon, though, I'll miss my flight!\x01",
            "So if you'll excuse me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230C")

    label("loc_21EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_228A")

    ChrTalk(
        0xFE,
        (
            "I'm in charge of the Liberl\x01",
            "News' culture section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's mostly book reviews, or\x01",
            "articles on popular local inns,\x01",
            "restaurants and so forth.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230C")

    label("loc_228A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_230C")

    ChrTalk(
        0xFE,
        (
            "If I don't get that manuscript\x01",
            "soon, my editor'll kill me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nial and Noticia are SO much\x01",
            "stricter than the chief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_230C")

    TalkEnd(0xFE)
    Return()

    # Function_12_1762 end

    def Function_13_2310(): pass

    label("Function_13_2310")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_234F")

    ChrTalk(
        0xFE,
        (
            "Heh... Nial really let me have\x01",
            "it this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D8C")

    label("loc_234F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_238F")

    ChrTalk(
        0xFE,
        (
            "Something seems...off...about\x01",
            "the town lately...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D8C")

    label("loc_238F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_242F")

    ChrTalk(
        0xFE,
        (
            "Nial was so reckless when he\x01",
            "first started this job. Really,\x01",
            "he still is pretty reckless!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But that's probably why he\x01",
            "always gets the goods!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D8C")

    label("loc_242F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_25C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_24C9")

    ChrTalk(
        0xFE,
        (
            "That squinty witch captain \x01",
            "just pisses me right off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She can never go two seconds\x01",
            "without making some sort of\x01",
            "snarky comment!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C4")

    label("loc_24C9")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "I admire Colonel Richard, but I still\x01",
            "don't approve of his Intelligence \x01",
            "Division or those Special Ops. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially that witch captain\x01",
            "with the squinty eyes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She can never go two seconds\x01",
            "without making some sort of\x01",
            "snarky comment!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C4")

    Jump("loc_2D8C")

    label("loc_25C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2677")

    ChrTalk(
        0xFE,
        (
            "The Intelligence Division is always\x01",
            "breathing down our necks. Doesn't\x01",
            "help us one bit, let me tell you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're almost like the MP\x01",
            "of the Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D8C")

    label("loc_2677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2837")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_274E")

    ChrTalk(
        0xFE,
        (
            "Both Nial and I get into it sometimes\x01",
            "with our editor over matters of...\x01",
            "journalistic integrity, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it's really hard to stay\x01",
            "mad when he's always got that\x01",
            "huge grin on his face!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2834")

    label("loc_274E")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        "Our editor...is a real oddball!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both Nial and I get into it sometimes\x01",
            "with him over matters of...journalistic\x01",
            "integrity, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it's really hard to stay\x01",
            "mad when he's always got that\x01",
            "huge grin on his face!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2834")

    Jump("loc_2D8C")

    label("loc_2837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_294A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_28A7")

    ChrTalk(
        0xFE,
        (
            "Nial's been up all night doing\x01",
            "some kind of research...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I bet he's found a hot lead!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2947")

    label("loc_28A7")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "Nial's been up all night doing\x01",
            "some kind of research...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I bet he's found a hot lead!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I'm not going to let him\x01",
            "hog all the glory, nosiree!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2947")

    Jump("loc_2D8C")

    label("loc_294A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_29E3")

    ChrTalk(
        0xFE,
        (
            "This year was all group \x01",
            "fighting, so getting good\x01",
            "pictures wasn't easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...My kingdom for a cameraman\x01",
            "with some real shutter skill!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D8C")

    label("loc_29E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2B89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_2A9E")

    ChrTalk(
        0xFE,
        (
            "The Liberl News is putting \x01",
            "together a special issue for\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got some real legwork to\x01",
            "do if I want to leave my mark\x01",
            "on this one!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_2A9E")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "The main event starts today.\x01",
            "I'm super-duper excited!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Liberl News is putting \x01",
            "together a special issue for\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got some real legwork to\x01",
            "do if I want to leave my mark\x01",
            "on this one!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B86")

    Jump("loc_2D8C")

    label("loc_2B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2D07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_2C20")

    ChrTalk(
        0xFE,
        "That Nial is a shark!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You think he's at rest after a hard\x01",
            "day's work...but no! He's already\x01",
            "out sniffing up his next scoop!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D04")

    label("loc_2C20")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        "That Nial is a shark!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You think he's at rest after a hard\x01",
            "day's work...but no! He's already\x01",
            "out sniffing up his next scoop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't let that pale complexion\x01",
            "and the endless cigarettes \x01",
            "fool you. He's a wily one!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D04")

    Jump("loc_2D8C")

    label("loc_2D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2D8C")

    ChrTalk(
        0xFE,
        (
            "Aaah! The prelims are gonna\x01",
            "start here soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Camera? Check. Press pass?\x01",
            "Check, and double check.\x01",
            "Checkbook? ...Yes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D8C")

    TalkEnd(0xFE)
    Return()

    # Function_13_2310 end

    def Function_14_2D90(): pass

    label("Function_14_2D90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3031")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2E23")

    ChrTalk(
        0x110,
        (
            "#150FYou know, Nial was telling me\x01",
            "something interesting...\x02\x03",
            "...He said this story's going\x01",
            "to win us the Fuelitzer Prize!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302E")

    label("loc_2E23")

    OP_A2(0xF)

    ChrTalk(
        0x110,
        (
            "#150FYay, it's Estelle and Joshua!\x02\x03",
            "You know, Nial was telling me\x01",
            "something interesting...\x02\x03",
            "...He said this story's going\x01",
            "to win us the Fuelitzer Prize!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FThe what, now? Don't you mean\x01",
            "the Pu--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FShhh! You want to get sued? The Fuelitzer is\x01",
            "an annual award presented to the very best\x01",
            "examples of journalism, literature and music.\x02\x03",
            "There's no higher honor for\x01",
            "any reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FAh. Well...good for you, then,\x01",
            "I guess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#150FEheh! It's actually all thanks to\x01",
            "YOU two! You're my whole story!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_302E")

    Jump("loc_322D")

    label("loc_3031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3081")

    ChrTalk(
        0x110,
        (
            "#150FOh, thank the Goddess Nial is\x01",
            "still alive! *weep* *sniffle*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_322D")

    label("loc_3081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_30C4")

    ChrTalk(
        0x110,
        (
            "#150FPlease, Estelle! I beg you!\x02\x03",
            "Please save Nial!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_322D")

    label("loc_30C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_31EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_315B")

    ChrTalk(
        0x110,
        (
            "#150FThe editor told me to go look\x01",
            "for Nial...\x02\x03",
            "But I have no idea where he\x01",
            "could possibly be! I don't\x01",
            "even know where to begin!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31E7")

    label("loc_315B")

    OP_A2(0xF)

    ChrTalk(
        0x110,
        (
            "#150FEstelle and company!\x02\x03",
            "Congratulations! That was\x01",
            "a simply AMAZING match!\x02\x03",
            "I have so many great shots!\x01",
            "I can't wait to show you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E7")

    Jump("loc_322D")

    label("loc_31EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_31F4")
    Jump("loc_322D")

    label("loc_31F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_31FE")
    Jump("loc_322D")

    label("loc_31FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3208")
    Jump("loc_322D")

    label("loc_3208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3212")
    Jump("loc_322D")

    label("loc_3212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_321C")
    Jump("loc_322D")

    label("loc_321C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3226")
    Jump("loc_322D")

    label("loc_3226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_322D")

    label("loc_322D")

    TalkEnd(0xFE)
    Return()

    # Function_14_2D90 end

    def Function_15_3231(): pass

    label("Function_15_3231")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_32C9")

    ChrTalk(
        0x10F,
        (
            "#140FYour interview is going to \x01",
            "be quite the must-read, too.\x02\x03",
            "I smell a big scoop here, for sure.\x01",
            "Don't you guys let me down!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_32C9")

    OP_A2(0xE)

    ChrTalk(
        0x10F,
        (
            "#140FJoshua! Estelle! Great job!\x02\x03",
            "Our special coup edition has\x01",
            "been flying off the stands.\x02\x03",
            "Your interview is going to \x01",
            "be quite the must-read, too.\x02\x03",
            "Two young heroes, standing\x01",
            "up to the legendary Colonel\x01",
            "Richard, thwarting his coup...\x02\x03",
            "I smell a big scoop here, for sure.\x01",
            "Don't you guys let me down!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FE")

    Jump("loc_3462")

    label("loc_3401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_340B")
    Jump("loc_3462")

    label("loc_340B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3415")
    Jump("loc_3462")

    label("loc_3415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_341F")
    Jump("loc_3462")

    label("loc_341F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3429")
    Jump("loc_3462")

    label("loc_3429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3433")
    Jump("loc_3462")

    label("loc_3433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_343D")
    Jump("loc_3462")

    label("loc_343D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3447")
    Jump("loc_3462")

    label("loc_3447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3451")
    Jump("loc_3462")

    label("loc_3451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_345B")
    Jump("loc_3462")

    label("loc_345B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3462")

    label("loc_3462")

    TalkEnd(0xFE)
    Return()

    # Function_15_3231 end

    def Function_16_3466(): pass

    label("Function_16_3466")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3619")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3527")

    ChrTalk(
        0xFE,
        (
            "The bracers and the Royal Guard,\x01",
            "storming Grancel Castle...it's\x01",
            "sure great for tourism!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's no wonder the Birthday Celebration\x01",
            "is more packed than ever before...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3616")

    label("loc_3527")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "It's been a long time since we've\x01",
            "had a story this juicy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bracers and the Royal Guard,\x01",
            "storming Grancel Castle...it's\x01",
            "sure great for tourism!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's no wonder the Birthday Celebration\x01",
            "is more packed than ever before...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3616")

    Jump("loc_3C14")

    label("loc_3619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_36E3")

    ChrTalk(
        0xFE,
        (
            "Spending your day poring over\x01",
            "books and news articles teaches\x01",
            "you to...notice things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like, that there's something going\x01",
            "on behind our backs that we're not\x01",
            "supposed to know about...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C14")

    label("loc_36E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3789")

    ChrTalk(
        0xFE,
        (
            "The Royal Guard may seem a bit\x01",
            "antiquated by modern standards...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But to see them sticking to their\x01",
            "rules of discipline was...simply\x01",
            "breathtaking!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C14")

    label("loc_3789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3837")

    ChrTalk(
        0xFE,
        (
            "There haven't been any details\x01",
            "yet about the queen's illness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And she hasn't said anything\x01",
            "herself...so maybe this is all\x01",
            "just an out-of-control rumor...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C14")

    label("loc_3837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_387E")

    ChrTalk(
        0xFE,
        (
            "Aaah. A cafe ole does wonders\x01",
            "for morning drowsiness...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C14")

    label("loc_387E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_38C5")

    ChrTalk(
        0xFE,
        (
            "Oy vey... When did 'soldier'\x01",
            "become a four-letter word?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C14")

    label("loc_38C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_38F2")

    ChrTalk(
        0xFE,
        "Reading is food for the soul.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C14")

    label("loc_38F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_39A0")

    ChrTalk(
        0xFE,
        (
            "I'm pretty sure the owner \x01",
            "here used to work over in\x01",
            "diplomatic affairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That'd explain why he's been\x01",
            "to the Empire and the Republic\x01",
            "so often, I suppose!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C14")

    label("loc_39A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3A01")

    ChrTalk(
        0xFE,
        (
            "I'm the kind of guy who only\x01",
            "needs to know the results of\x01",
            "the tournament matches.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C14")

    label("loc_3A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3BA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3ABF")

    ChrTalk(
        0xFE,
        (
            "The articles in the Liberl \x01",
            "News have been pretty...\x01",
            "tame?...as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's been no shock; no sensationalism.\x01",
            "Goes against everything I love about\x01",
            "Liberlism!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA3")

    label("loc_3ABF")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "The articles in the Liberl \x01",
            "News have been pretty...\x01",
            "tame?...as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's almost all just a parade\x01",
            "of fluff pieces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's been no shock; no sensationalism.\x01",
            "Goes against everything I love about\x01",
            "Liberlism!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BA3")

    Jump("loc_3C14")

    label("loc_3BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3C14")

    ChrTalk(
        0xFE,
        "This is a really relaxing place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I kill many an hour here, just\x01",
            "sipping a cuppa and reading.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C14")

    TalkEnd(0xFE)
    Return()

    # Function_16_3466 end

    def Function_17_3C18(): pass

    label("Function_17_3C18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3CCF")

    ChrTalk(
        0xFE,
        (
            "I didn't think that the Martial\x01",
            "Arts Competition would be used\x01",
            "as a cover for a coup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But Colonel Richard didn't\x01",
            "seem very content with his\x01",
            "position as it was.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46ED")

    label("loc_3CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3E3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3D61")

    ChrTalk(
        0xFE,
        (
            "The army seems to have really\x01",
            "tightened its hold on the\x01",
            "city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but us? We have absolutely\x01",
            "no idea what's going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3D61")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "The army seems to have really\x01",
            "tightened its hold on the\x01",
            "city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but us? We have absolutely\x01",
            "no idea what's going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People get nervous when they\x01",
            "can tell something fishy is\x01",
            "starting to happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E37")

    Jump("loc_46ED")

    label("loc_3E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4037")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3F1D")

    ChrTalk(
        0xFE,
        (
            "Those Special Ops guys were\x01",
            "grumbling about some search\x01",
            "mission...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I caught bits and pieces of it: 'Royal Guard,'\x01",
            "'citizen,' 'uncooperative'...and, er, some...\x01",
            "shall we say...more colorful metaphors?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4034")

    label("loc_3F1D")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "Those Special Ops guys were\x01",
            "grumbling about some search\x01",
            "mission...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I caught bits and pieces of it: 'Royal Guard,'\x01",
            "'citizen,' 'uncooperative'...and, er, some...\x01",
            "shall we say...more colorful metaphors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What do they expect? The Royal\x01",
            "Guard is very well-respected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4034")

    Jump("loc_46ED")

    label("loc_4037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_40A0")

    ChrTalk(
        0xFE,
        "So, the competition's done, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A victory banquet in the castle...\x01",
            "lucky winners!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46ED")

    label("loc_40A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_40EA")

    ChrTalk(
        0xFE,
        (
            "Would you like to try a cup\x01",
            "of our famous espresso?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413D")

    label("loc_40EA")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Would you like to try a cup\x01",
            "of our famous espresso?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_413D")

    Jump("loc_46ED")

    label("loc_4140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_42F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4205")

    ChrTalk(
        0xFE,
        (
            "Seems there's a curfew now.\x01",
            "Everyone off the streets by\x01",
            "nine o'clock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not great for business, but it'll be\x01",
            "nice to close up early, put on some\x01",
            "music and do some reading.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F6")

    label("loc_4205")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "Some Royal Army soldiers came\x01",
            "in here a while ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seems there's a curfew now.\x01",
            "Everyone off the streets by\x01",
            "nine o'clock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not great for business, but it'll be\x01",
            "nice to close up early, put on some\x01",
            "music and do some reading.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F6")

    Jump("loc_46ED")

    label("loc_42F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_43BC")

    ChrTalk(
        0xFE,
        (
            "The West Block of Grancel\x01",
            "is overall one of the quieter\x01",
            "parts of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I put a lot of time into finding\x01",
            "the best location for this shop,\x01",
            "and this seemed the ideal choice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46ED")

    label("loc_43BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_454D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4443")

    ChrTalk(
        0xFE,
        (
            "I had to travel all over the\x01",
            "world for my old job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The culture of cuisine is some\x01",
            "really fascinating stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_454A")

    label("loc_4443")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "I had to travel all over the\x01",
            "world for my old job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tried a whole lot of different\x01",
            "foods, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One of the curries I serve here\x01",
            "comes from a recipe I discovered\x01",
            "along the way, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The culture of cuisine is some\x01",
            "really fascinating stuff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_454A")

    Jump("loc_46ED")

    label("loc_454D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_45FC")

    ChrTalk(
        0xFE,
        (
            "Welcome, welcome! Please, make\x01",
            "yourselves at home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Home is what I was going for here.\x01",
            "I wanted to make this establishment\x01",
            "feel just like a person's house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46ED")

    label("loc_45FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_46B2")

    ChrTalk(
        0xFE,
        (
            "The building next door is the\x01",
            "headquarters and main office\x01",
            "for the Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their reporters and editors\x01",
            "and such all come in here to\x01",
            "eat, or to take a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46ED")

    label("loc_46B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_46ED")

    ChrTalk(
        0xFE,
        "Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Welcome to the Baral Coffee House!\x02",
    )

    CloseMessageWindow()

    label("loc_46ED")

    TalkEnd(0xFE)
    Return()

    # Function_17_3C18 end

    def Function_18_46F1(): pass

    label("Function_18_46F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_46FB")
    Jump("loc_488E")

    label("loc_46FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4759")

    ChrTalk(
        0xFE,
        (
            "Oooh, do you wanna go get\x01",
            "some ice cream sometime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I know the BEST place.\x02",
    )

    CloseMessageWindow()
    Jump("loc_488E")

    label("loc_4759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_479F")

    ChrTalk(
        0xFE,
        (
            "I have nothing to do until\x01",
            "the Birthday Celebration...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_488E")

    label("loc_479F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_484B")

    ChrTalk(
        0xFE,
        (
            "They so need to go back to one-\x01",
            "on-one fights for next year's\x01",
            "Martial Arts Competition!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That way there can be an actual\x01",
            "Team Joshua for us to cheer on!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_488E")

    label("loc_484B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4855")
    Jump("loc_488E")

    label("loc_4855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_485F")
    Jump("loc_488E")

    label("loc_485F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4869")
    Jump("loc_488E")

    label("loc_4869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4873")
    Jump("loc_488E")

    label("loc_4873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_487D")
    Jump("loc_488E")

    label("loc_487D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4887")
    Jump("loc_488E")

    label("loc_4887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_488E")

    label("loc_488E")

    Return()

    # Function_18_46F1 end

    def Function_19_488F(): pass

    label("Function_19_488F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4899")
    Jump("loc_49EC")

    label("loc_4899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_48D4")

    ChrTalk(
        0xFE,
        "I'm so bored...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anything you wanna do?\x02",
    )

    CloseMessageWindow()
    Jump("loc_49EC")

    label("loc_48D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_496D")

    ChrTalk(
        0xFE,
        (
            "Are they even HAVING the Birthday\x01",
            "Celebration this year?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard the queen's gotten sick,\x01",
            "so maybe the party's gonna get\x01",
            "canceled...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49EC")

    label("loc_496D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_49A9")

    ChrTalk(
        0xFE,
        (
            "I can't believe Lorence lost!\x01",
            "Soooo laaaame!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49EC")

    label("loc_49A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_49B3")
    Jump("loc_49EC")

    label("loc_49B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_49BD")
    Jump("loc_49EC")

    label("loc_49BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_49C7")
    Jump("loc_49EC")

    label("loc_49C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_49D1")
    Jump("loc_49EC")

    label("loc_49D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_49DB")
    Jump("loc_49EC")

    label("loc_49DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_49E5")
    Jump("loc_49EC")

    label("loc_49E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_49EC")

    label("loc_49EC")

    Return()

    # Function_19_488F end

    def Function_20_49ED(): pass

    label("Function_20_49ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_49FA")
    Jump("loc_4ABE")

    label("loc_49FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4A04")
    Jump("loc_4ABE")

    label("loc_4A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4A0E")
    Jump("loc_4ABE")

    label("loc_4A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4A7B")

    ChrTalk(
        0xFE,
        "Congratulations, Zane!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew you were a shoe-in from\x01",
            "the very beginning. You rule,\x01",
            "man!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ABE")

    label("loc_4A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4A85")
    Jump("loc_4ABE")

    label("loc_4A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4A8F")
    Jump("loc_4ABE")

    label("loc_4A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4A99")
    Jump("loc_4ABE")

    label("loc_4A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4AA3")
    Jump("loc_4ABE")

    label("loc_4AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4AAD")
    Jump("loc_4ABE")

    label("loc_4AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4AB7")
    Jump("loc_4ABE")

    label("loc_4AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4ABE")

    label("loc_4ABE")

    TalkEnd(0xFE)
    Return()

    # Function_20_49ED end

    def Function_21_4AC2(): pass

    label("Function_21_4AC2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4ACF")
    Jump("loc_4C7C")

    label("loc_4ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4AD9")
    Jump("loc_4C7C")

    label("loc_4AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4AE3")
    Jump("loc_4C7C")

    label("loc_4AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4B76")

    ChrTalk(
        0xFE,
        (
            "I met him when we were both\x01",
            "cheering for the same team\x01",
            "at the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the match, we went\x01",
            "out for some drinks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C36")

    label("loc_4B76")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "I met him when we were both\x01",
            "cheering for the same team\x01",
            "at the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the match, we went\x01",
            "out for some drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're going for an all-nighter\x01",
            "tonight! Whoo hoo hoo!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C36")

    Jump("loc_4C7C")

    label("loc_4C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4C43")
    Jump("loc_4C7C")

    label("loc_4C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4C4D")
    Jump("loc_4C7C")

    label("loc_4C4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4C57")
    Jump("loc_4C7C")

    label("loc_4C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4C61")
    Jump("loc_4C7C")

    label("loc_4C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4C6B")
    Jump("loc_4C7C")

    label("loc_4C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4C75")
    Jump("loc_4C7C")

    label("loc_4C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4C7C")

    label("loc_4C7C")

    TalkEnd(0xFE)
    Return()

    # Function_21_4AC2 end

    def Function_22_4C80(): pass

    label("Function_22_4C80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4C8D")
    Jump("loc_50BF")

    label("loc_4C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4C97")
    Jump("loc_50BF")

    label("loc_4C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4CA1")
    Jump("loc_50BF")

    label("loc_4CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4CAB")
    Jump("loc_50BF")

    label("loc_4CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4CB5")
    Jump("loc_50BF")

    label("loc_4CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4D87")

    ChrTalk(
        0x104,
        (
            "#030FHeaven's tears! I couldn't \x01",
            "possibly drink with Schera any\x01",
            "harder or faster than I do.\x02\x03",
            "An evening of drinks with her is\x01",
            "a bacchanal beginning in Elysium\x01",
            "and ending in...well, vomit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E79")

    label("loc_4D87")

    OP_A2(0x5)

    ChrTalk(
        0x104,
        (
            "#030FHa, ha, ha, ha, ha!\x01",
            "...\x01",
            "...Are you for true?\x02\x03",
            "Heaven's tears! I couldn't \x01",
            "possibly drink with Schera any\x01",
            "harder or faster than I do.\x02\x03",
            "An evening of drinks with her is\x01",
            "a bacchanal beginning in Elysium\x01",
            "and ending in...well, vomit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E79")

    Jump("loc_50BF")

    label("loc_4E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4E86")
    Jump("loc_50BF")

    label("loc_4E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4FE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4F0E")

    ChrTalk(
        0x104,
        (
            "#030FAaah, repast. Comfort for the\x01",
            "soul and fuel for the flesh.\x02\x03",
            "A profession worthy of song is\x01",
            "that of the chef!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FDE")

    label("loc_4F0E")

    OP_A2(0x5)

    ChrTalk(
        0x104,
        (
            "#030FHa, ha, ha! Why, the night's\x01",
            "festivities have only just\x01",
            "begun!\x02\x03",
            "There are selge to go before\x01",
            "we sleep!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWhere is he PUTTING all of\x01",
            "that food? Does he have, like,\x01",
            "a vortex in his belly?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FDE")

    Jump("loc_50BF")

    label("loc_4FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4FEB")
    Jump("loc_50BF")

    label("loc_4FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_50B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_50B5")

    ChrTalk(
        0x104,
        (
            "#030FRed...orange...yellow...g-gold...\x01",
            "peri...p-periwinkle... Lookit all\x01",
            "the colors! Such bea-uty!\x02\x03",
            "I will be...with...you...\x01",
            "aaaaalways... I will...be...\x01",
            "true to you...aaaaalways...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50B5")

    Jump("loc_50BF")

    label("loc_50B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_50BF")

    label("loc_50BF")

    TalkEnd(0xFE)
    Return()

    # Function_22_4C80 end

    def Function_23_50C3(): pass

    label("Function_23_50C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_551E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_516B")

    ChrTalk(
        0x10,
        (
            "#070FI think I'll stick around a\x01",
            "little while longer.\x02\x03",
            "As long as I'm here, It would be\x01",
            "a waste to leave without testing\x01",
            "my mettle a bit more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_551B")

    label("loc_516B")

    OP_A2(0x4)

    ChrTalk(
        0x10,
        "#070FHey, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FZane!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FSo, what's your next move?\x02\x03",
            "Back to the Republic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#070FI'm in no rush. There doesn't seem to be\x01",
            "any crisis in the Republic so bad that I\x01",
            "absolutely have to be there for it.\x02\x03",
            "Besides, this country is full\x01",
            "of fine opponents from your\x01",
            "Bracer Guild!\x02\x03",
            "As long as I'm here, it would be\x01",
            "a waste to leave without testing\x01",
            "my mettle a bit more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F'Fine opponents?' Who'd you\x01",
            "have in mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#070FFor starters, you've got Agate...the\x01",
            "so-called 'Heavy Blade.' Not to mention \x01",
            "your 'Silver Streak,' Scherazard.\x02\x03",
            "And who could forget...\x02\x03",
            "...the champions of this year's\x01",
            "Martial Arts Competition? Perhaps\x01",
            "the strongest of them all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FAww, Zane, that's so sweet!\x02\x03",
            "...But don't think it means I'll\x01",
            "go any easier on you. And don't\x01",
            "you hold back on us! It's ON, man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F...She doesn't speak for both of us.\x01",
            "Feel free to hold back, if you'd like.\x01",
            "In fact, I might even prefer it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_551B")

    Jump("loc_571D")

    label("loc_551E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5528")
    Jump("loc_571D")

    label("loc_5528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5532")
    Jump("loc_571D")

    label("loc_5532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_553C")
    Jump("loc_571D")

    label("loc_553C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5546")
    Jump("loc_571D")

    label("loc_5546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_55C6")

    ChrTalk(
        0x10,
        (
            "#070FThe final fight is tomorrow.\x02\x03",
            "Tonight, you need to go home,\x01",
            "eat a good meal, get plenty of\x01",
            "rest...and pray.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_571D")

    label("loc_55C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_55D0")
    Jump("loc_571D")

    label("loc_55D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5702")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5611")

    ChrTalk(
        0x10,
        (
            "#070F*hic* Woo you guysh like a\x01",
            "grink too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56FF")

    label("loc_5611")

    OP_A2(0x4)

    ChrTalk(
        0x10,
        (
            "#070FESHTELL! JOSHUWA!\x02\x03",
            "*hic* Woo you guysh like a\x01",
            "grink too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FUh, we're underage, you know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#070FWazzat? You guysh don wanna\x01",
            "grink...? Grink...heh. I said\x01",
            "grink instead of dring!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWell, this is just prime.\x02",
    )

    CloseMessageWindow()

    label("loc_56FF")

    Jump("loc_571D")

    label("loc_5702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_570C")
    Jump("loc_571D")

    label("loc_570C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5716")
    Jump("loc_571D")

    label("loc_5716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_571D")

    label("loc_571D")

    TalkEnd(0xFE)
    Return()

    # Function_23_50C3 end

    def Function_24_5721(): pass

    label("Function_24_5721")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_58AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_57E0")

    ChrTalk(
        0xFE,
        (
            "I would never have guessed\x01",
            "Colonel Richard would plan\x01",
            "a coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything he said in that magazine\x01",
            "interview... It was all just propaganda.\x01",
            "All just lies!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58AA")

    label("loc_57E0")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "I would never have guessed\x01",
            "Colonel Richard would plan\x01",
            "a coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything he said in that magazine\x01",
            "interview... It was all just propaganda.\x01",
            "All just lies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm...utterly shocked.\x02",
    )

    CloseMessageWindow()

    label("loc_58AA")

    Jump("loc_63C3")

    label("loc_58AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5947")

    ChrTalk(
        0xFE,
        (
            "There's something strange in\x01",
            "the air around town lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's like...that quiet time\x01",
            "before a big storm. Yeah,\x01",
            "like that...but worse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C3")

    label("loc_5947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_59F0")

    ChrTalk(
        0xFE,
        (
            "With the Birthday Celebration\x01",
            "so close, I hope there'll be\x01",
            "some news from the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I pray it's not that the\x01",
            "festivities have been canceled...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C3")

    label("loc_59F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5AB6")

    ChrTalk(
        0xFE,
        (
            "The tournament may be over and done\x01",
            "with, but there are still just as many\x01",
            "soldiers on patrol...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They make me nervous, what \x01",
            "with all these rumors about\x01",
            "Her Highness being sick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C3")

    label("loc_5AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5BF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5B46")

    ChrTalk(
        0xFE,
        (
            "There were so many soldiers in\x01",
            "the streets last night, I got\x01",
            "stopped at least four times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do I look THAT suspicious?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BF6")

    label("loc_5B46")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "There were so many soldiers in\x01",
            "the streets last night, I got\x01",
            "stopped at least four times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do I look THAT suspicious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It makes me feel a bit self-conscious...\x02",
    )

    CloseMessageWindow()

    label("loc_5BF6")

    Jump("loc_63C3")

    label("loc_5BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5C96")

    ChrTalk(
        0xFE,
        (
            "Ever since that exclusive in \x01",
            "the Liberl News, Colonel \x01",
            "Richard's been quite popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's won over a lot of people,\x01",
            "both young and old.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C3")

    label("loc_5C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5D21")

    ChrTalk(
        0xFE,
        (
            "The Imperial breakfast at\x01",
            "Baral Coffee House is quite\x01",
            "delicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but I actually prefer the\x01",
            "Liberl breakfast here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C3")

    label("loc_5D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5EF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5DE7")

    ChrTalk(
        0xFE,
        (
            "So man, was I ever taken aback\x01",
            "when those Sky Bandits from Bose\x01",
            "showed up in the tournament!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is it really okay to have\x01",
            "convicted criminals serving\x01",
            "in a sporting event...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EF0")

    label("loc_5DE7")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "So man, was I ever taken aback\x01",
            "when those Sky Bandits from Bose\x01",
            "showed up in the tournament!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were more skilled than I\x01",
            "would've expected, though, I\x01",
            "have to admit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is it really okay to have\x01",
            "convicted criminals serving\x01",
            "in a sporting event...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EF0")

    Jump("loc_63C3")

    label("loc_5EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_60BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5FBA")

    ChrTalk(
        0xFE,
        (
            "The Martial Arts Competition\x01",
            "was originally held to show\x01",
            "off new military techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When Queen Alicia took the \x01",
            "throne, she opened it to the\x01",
            "public as a spectator event.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60BC")

    label("loc_5FBA")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "The Martial Arts Competition\x01",
            "was originally held to show\x01",
            "off new military techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When Queen Alicia took the \x01",
            "throne, she opened it to the\x01",
            "public as a spectator event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And shortly thereafter, the\x01",
            "public was also invited to\x01",
            "participate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60BC")

    Jump("loc_63C3")

    label("loc_60BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_6164")

    ChrTalk(
        0xFE,
        (
            "This is the first year the\x01",
            "tournament's been fought with\x01",
            "teams, rather than one-on-one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Supposedly the duke's idea...\x01",
            "and not a bad one, really!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C3")

    label("loc_6164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_63C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_61CA")

    ChrTalk(
        0xFE,
        (
            "*GULP* Don't surprise me like\x01",
            "that! I almost choked on my\x01",
            "forkful of spaghetti!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C3")

    label("loc_61CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_628B")

    ChrTalk(
        0xFE,
        (
            "The Royal Guard is under the magnifying\x01",
            "glass right now, what with all those\x01",
            "allegations of terrorist involvement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sure seems like a lot's been\x01",
            "going down, these days...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C3")

    label("loc_628B")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "The Royal Guard is under the magnifying\x01",
            "glass right now, what with all those\x01",
            "allegations of terrorist involvement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First the Sky Bandits in Bose, then the\x01",
            "corrupt mayor of Ruan, and now that business\x01",
            "with the orbal blackout in Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sure seems like a lot's been\x01",
            "going down, these days...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63C3")

    TalkEnd(0xFE)
    Return()

    # Function_24_5721 end

    def Function_25_63C7(): pass

    label("Function_25_63C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_651B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_643E")

    ChrTalk(
        0xFE,
        (
            "A lot's been happening lately,\x01",
            "but I think things are finally\x01",
            "starting to get back to normal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6518")

    label("loc_643E")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "Seeing the queen healthy \x01",
            "was a real comfort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All that suspicion from the \x01",
            "Royal Guardsmen was unfounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot's been happening lately,\x01",
            "but I think things are finally\x01",
            "starting to get back to normal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6518")

    Jump("loc_6C33")

    label("loc_651B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6579")

    ChrTalk(
        0xFE,
        (
            "I just saw a bunch of soldiers \x01",
            "running off somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Something happen?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C33")

    label("loc_6579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_6609")

    ChrTalk(
        0xFE,
        (
            "The city's just been CRAWLING\x01",
            "with soldiers lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Were the Royal Guardsmen really\x01",
            "the ones responsible for the\x01",
            "attack?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C33")

    label("loc_6609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_668C")

    ChrTalk(
        0xFE,
        (
            "Seems like Olivier's not coming\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanted to congratulate him\x01",
            "on winning the Martial Arts\x01",
            "Competition...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C33")

    label("loc_668C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_675F")

    ChrTalk(
        0xFE,
        (
            "Maaan, I wish I could go to the\x01",
            "arena and watch the matches...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But in this line of work, I'm at my busiest\x01",
            "when other people are out and about, having\x01",
            "the time of their lives! It's not fair!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C33")

    label("loc_675F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_67E9")

    ChrTalk(
        0xFE,
        (
            "Some soldiers came by earlier,\x01",
            "and told me I had to close my\x01",
            "store at nine o'clock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Apparently, there's a curfew now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C33")

    label("loc_67E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6887")

    ChrTalk(
        0xFE,
        "Aren't you in today's matches?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since the Royal Guardsmen aren't in\x01",
            "the tournament, I might as well cheer\x01",
            "for you guys. Rah, rah, go team!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C33")

    label("loc_6887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_68DB")

    ChrTalk(
        0xFE,
        (
            "So, there we have it. Day one,\x01",
            "at an end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder how it went?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C33")

    label("loc_68DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6A41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6937")

    ChrTalk(
        0xFE,
        "Are you all Olivier's friends?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hope the match goes well for you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A3E")

    label("loc_6937")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "Ah, Olivier! Is your head\x01",
            "feeling any better today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030FHa ha ha! But of course!\x02\x03",
            "Trivialities such as head wounds mean nothing\x01",
            "to me, as long as there exists a spark of love\x01",
            "to fuel the towering inferno of my heart!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...So, that's a yes, then.\x02",
    )

    CloseMessageWindow()

    label("loc_6A3E")

    Jump("loc_6C33")

    label("loc_6A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_6B13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_6AC0")

    ChrTalk(
        0xFE,
        (
            "Well, if it isn't our prodigal\x01",
            "musician, Olivier!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Been striking out with the women\x01",
            "again, I assume?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B10")

    label("loc_6AC0")


    ChrTalk(
        0xFE,
        (
            "Well, I guess the prelims are\x01",
            "over, given the swarm of people\x01",
            "coming in...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B10")

    Jump("loc_6C33")

    label("loc_6B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6C33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6B87")

    ChrTalk(
        0xFE,
        (
            "I can't believe the Royal\x01",
            "Guardsmen are terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's got to be some kind of\x01",
            "mistake!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C33")

    label("loc_6B87")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "I can't believe the Royal\x01",
            "Guardsmen are terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every one of them that comes in\x01",
            "here is an upstanding young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's got to be some kind of\x01",
            "mistake!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C33")

    TalkEnd(0xFE)
    Return()

    # Function_25_63C7 end

    def Function_26_6C37(): pass

    label("Function_26_6C37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6E8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6CE8")

    ChrTalk(
        0xFE,
        (
            "Based on your performance\x01",
            "I'd say you two are already\x01",
            "fine, full-fledged bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But never forget, these are only\x01",
            "the first steps in your career!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E8B")

    label("loc_6CE8")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "You did a remarkable job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Based on your performance\x01",
            "I'd say you two are already\x01",
            "fine, full-fledged bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But never forget, these are only\x01",
            "the first steps in your career!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FThank you, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FSo Kurt, are you feeling any better?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm fine. Just fine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I remember just about everything, EXCEPT\x01",
            "the identity of the bastard who erased my\x01",
            "memories. That's the only missing piece!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E8B")

    TalkEnd(0xFE)
    Return()

    # Function_26_6C37 end

    def Function_27_6E8F(): pass

    label("Function_27_6E8F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_731D")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 3930, 0, -620, 0)
    SetChrPos(0x102, 5070, 0, -540, 0)
    SetChrPos(0x108, 4540, 0, -1430, 0)
    TurnDirection(0xC, 0x108, 0)
    OP_A2(0x64A)
    OP_6D(4720, 0, 250, 1000)

    ChrTalk(
        0x101,
        "#000FHey, it's Grant!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, well. If it isn't the\x01",
            "big, bad champions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hear you guys spent the night at\x01",
            "the castle. Frankly, I'm surprised\x01",
            "to see you back so early!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Did you eat anything good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FYeah, we did...but that's not\x01",
            "what we're here to talk about!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh? Something on your mind?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained the situation and the queen's request to Grant.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xC,
        (
            "...Holy crap! You're not pulling\x01",
            "my leg, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FWe are not. Every word is true.\x02\x03",
            "I'd stake my reputation on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If Zane the Immovable is moved\x01",
            "by this, that's all the proof\x01",
            "I need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'll do whatever I can to help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "You can count on it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FThanks, Grant!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe'll all be meeting at the guild\x01",
            "to plan our strategy, as soon as\x01",
            "possible.\x02\x03",
            "So if you'd please, head over\x01",
            "there when you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Understood. Go well, friends.\x01",
            "I'll catch up with you there.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7278():

        label("loc_7278")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_7278")

    QueueWorkItem2(0x101, 1, lambda_7278)

    def lambda_7289():

        label("loc_7289")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_7289")

    QueueWorkItem2(0x102, 1, lambda_7289)

    def lambda_729A():

        label("loc_729A")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_729A")

    QueueWorkItem2(0x108, 1, lambda_729A)
    OP_8E(0xC, 0xBEA, 0x0, 0x1E, 0xBB8, 0x0)
    OP_8E(0xC, 0x406, 0x0, 0xFFFFF402, 0xBB8, 0x0)
    OP_8E(0xC, 0x2C6, 0xFFFFFF06, 0xFFFFEA8E, 0xBB8, 0x0)

    def lambda_72E7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_72E7)
    OP_8E(0xC, 0x2C6, 0xFFFFFF06, 0xFFFFE2D2, 0xBB8, 0x0)
    SetChrFlags(0xC, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    EventEnd(0x0)
    Jump("loc_782B")

    label("loc_731D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_7505")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7364")

    ChrTalk(
        0xFE,
        "Guess this makes us partners.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Here's to us!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7502")

    label("loc_7364")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "Welcome back, brave heroes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FGrant...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You guys were amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Better than any other junior\x01",
            "bracers I've met, that's for\x01",
            "damn sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FYay us!\x02\x03",
            "We couldn't have done it without\x01",
            "everyone's help, though.\x02\x03",
            "I mean, my dad ended up saving\x01",
            "my butt in there, so I'm not\x01",
            "exactly solo heroine material!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You guys are something else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Guess this makes us partners.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Here's to us!\x02",
    )

    CloseMessageWindow()

    label("loc_7502")

    Jump("loc_782B")

    label("loc_7505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_750F")
    Jump("loc_782B")

    label("loc_750F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_7519")
    Jump("loc_782B")

    label("loc_7519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_7644")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7570")

    ChrTalk(
        0xFE,
        "Hey, where'd the blondie go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He was quite the sharpshooter!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7641")

    label("loc_7570")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "Looks like the band's back\x01",
            "together again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's see that dance that\x01",
            "won you the tournament!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, I'd've preferred to win\x01",
            "it myself...but I'm not bitter!\x01",
            "I was beaten, fair and square!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7641")

    Jump("loc_782B")

    label("loc_7644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_764E")
    Jump("loc_782B")

    label("loc_764E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7658")
    Jump("loc_782B")

    label("loc_7658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7662")
    Jump("loc_782B")

    label("loc_7662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_766C")
    Jump("loc_782B")

    label("loc_766C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_781A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_76B7")

    ChrTalk(
        0xFE,
        (
            "Bracers gotta eat and bracers\x01",
            "gotta sleep, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7817")

    label("loc_76B7")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "Hey! Had breakfast yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FHey there, Grant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bracers gotta eat and bracers\x01",
            "gotta sleep, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hope that was drilled into your\x01",
            "head at the guild-- a lack of\x01",
            "sleep impairs one's judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIronically enough, that was\x01",
            "the one lesson Estelle DIDN'T\x01",
            "sleep through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FThat's not true! I was\x01",
            "awake for plen--HEY!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7817")

    Jump("loc_782B")

    label("loc_781A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_7824")
    Jump("loc_782B")

    label("loc_7824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_782B")

    label("loc_782B")

    TalkEnd(0xC)
    Return()

    # Function_27_6E8F end

    def Function_28_782F(): pass

    label("Function_28_782F")

    Return()

    # Function_28_782F end

    def Function_29_7830(): pass

    label("Function_29_7830")

    EventBegin(0x0)
    SetChrFlags(0x108, 0x4)
    SetChrPos(0x108, -3800, 0, -2180, 180)
    SetChrPos(0x101, -3460, 0, -4600, 0)
    SetChrPos(0x102, -4940, 0, -4600, 0)
    OP_6D(-3770, 0, -3540, 0)

    ChrTalk(
        0x108,
        (
            "#070FSo that's how it is, eh?\x02\x03",
            "Tell me something, though.\x01",
            "Why do you want to take part\x01",
            "in the tournament?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWell, uh... I've been kinda itching\x01",
            "to do something like this ever since\x01",
            "I caught those preliminary matches.\x02\x03",
            "You know, really throw down\x01",
            "with some tough opponents...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe're traveling all over the\x01",
            "kingdom to help prepare us to\x01",
            "become full-fledged bracers.\x02\x03",
            "This would be the perfect opportunity\x01",
            "to test ourselves and see if our\x01",
            "training has paid off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FHmmmm...\x02\x03",
            "All right. Let's do it.\x02\x03",
            "We can get you registered tomorrow,\x01",
            "before the tourney begins, so no\x01",
            "worries on that score.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWoohoo! 噴\x02\x03",
            "Hey... Are you sure you're okay with\x01",
            "giving us an answer so quickly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FHey, it'll give me a chance to\x01",
            "see just how skilled you are.\x02\x03",
            "You just watch my back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FRoger that!\x01",
            "Thank you, Zane!\x02\x03",
            "I'm gonna give it everything\x01",
            "I've got!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FIt's no bother.\x02\x03",
            "I had been planning to enter\x01",
            "as a solo competitor...\x02\x03",
            "...but I suppose that having\x01",
            "some help could improve my\x01",
            "chances of overall victory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FNaturally! Once I'm in the ring,\x01",
            "that championship's in the bag!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe're still one person short\x01",
            "of the requirement, though...\x02\x03",
            "Since we have to face four-person\x01",
            "teams, one more would give us\x01",
            "the best possible odds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FOh, right... Hmmm...\x02\x03",
            "Hey, I'll bet we could beat\x01",
            "them without a fourth!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FNo... If you really want to come out\x01",
            "on top, you have to be prepared.\x02\x03",
            "A battle is waged well before\x01",
            "the first blow is struck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FErr...well, yeah, I guess.\x02\x03",
            "I sure wish Schera were with us.\x01",
            "That'd keep my spirits up.\x02\x03",
            "Hey, do you suppose we could ask\x01",
            "Elnan to try getting in touch\x01",
            "with her in Rolent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI think she's kind of busy\x01",
            "at the moment.\x02\x03",
            "Since Dad's not there, and we're\x01",
            "not there, that branch is pretty\x01",
            "short-handed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FYeah, that's true...\x02\x03",
            "Grrrr! Isn't there someone who\x01",
            "can partner up with us?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, -1920, 4000, 4680, 180)
    ClearChrFlags(0x8, 0x80)

    ChrTalk(
        0x8,
        (
            "Heh... And here I was, thinking\x01",
            "you might never see your way\x01",
            "clear to asking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FTh-That voice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYou don't think...\x02",
    )

    CloseMessageWindow()
    OP_6D(-1290, 4000, 5210, 3000)

    def lambda_80BF():
        OP_6D(-2350, 0, -630, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80BF)
    OP_8E(0x8, 0xFFFFEDAE, 0x7D0, 0x11C6, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFED36, 0x0, 0xFFFFFE7A, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        (
            "#000FAh...\x01",
            "Enter the pervert, stage left.\x02\x03",
            "Don't tell me you were\x01",
            "hiding out upstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWere you listening in on\x01",
            "our conversation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030FHeh heh heh... Indeed, I heard\x01",
            "every tragic syllable!\x02\x03",
            "Therefore, it seemed the appropriate\x01",
            "time to make an appearance.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    OP_96(0x8, 0xFFFFEC64, 0x0, 0xFFFFF722, 0x3E8, 0x1388)

    ChrTalk(
        0x101,
        (
            "#000FHey!\x01",
            "Who asked you to sit down?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FHe was the one who was playing\x01",
            "the piano before, wasn't he?\x02\x03",
            "You know him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FReplace 'know' with 'can't get rid\x01",
            "of,' and that about covers it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAnd we haven't even known\x01",
            "him for that long, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030FMany call me Olivier Lenheim, the\x01",
            "wandering minstrel from Erebonia.\x02\x03",
            "It was Estelle and Joshua's\x01",
            "pleasure to make my acquaintance\x01",
            "on an earlier case.\x02\x03",
            "And ever since, we seem to keep\x01",
            "running into each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FQuit trying to trick him!\x01",
            "Zane, don't listen to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FHmm... I'm not entirely sure what's\x01",
            "going on, but there's no harm in\x01",
            "introductions, I suppose.\x02\x03",
            "Zane Vathek. Bracer from Calvard\x01",
            "and perpetual traveler of the\x01",
            "path of Wushu.\x02\x03",
            "I've enjoyed your piano playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030FHa ha... You do me great honor,\x01",
            "good sir.\x02\x03",
            "I have also heard tales of your\x01",
            "prowess in the preliminary matches.\x02\x03",
            "Tell me, did you truly defeat a\x01",
            "team of four, entirely on your own?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FAll I can say is that I had\x01",
            "the good fortune of them all\x01",
            "being rank amateurs.\x02\x03",
            "So what does a wandering minstrel,\x01",
            "as you say, want with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FWait, wait! Hold it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FOlivier, I'd like for you to\x01",
            "verify something for me...\x02\x03",
            "By any chance, do you have a lot\x01",
            "of spare time on your hands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030FAnd you say that I haven't changed,\x01",
            "good Joshua. You were ever one for\x01",
            "the pointed questions.\x02\x03",
            "It has been nearly a month since\x01",
            "I came to Grancel...\x02\x03",
            "I've traveled the length and breadth of the city,\x01",
            "enjoying all the sights...except the castle. Those\x01",
            "boorish soldiers would not allow me to pass.\x02\x03",
            "To be certain, there are other places that I'd\x01",
            "like to visit, but I could not bear to leave\x01",
            "with the birthday celebrations so close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FIn other words, you're bored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030FNow, what is this talk of being\x01",
            "a man short that I happened\x01",
            "to overhear?\x02\x03",
            "I have heard that the winner of\x01",
            "this competition will be invited\x01",
            "to an extravagant dinner party...\x02\x03",
            "Surely, this can only be\x01",
            "divine providence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYeah, pretty much what we\x01",
            "figured you were thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030FI had, in fact, wondered if\x01",
            "you might invite me to join\x01",
            "you in this tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070FYou okay with that?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#000FW-Wait, Zane.\x01",
            "It's not that simple...\x02\x03",
            "I mean, you don't even know if\x01",
            "he's any good in a fight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FHis specialty is orbal firearms,\x01",
            "right?\x02\x03",
            "I think the team would be pretty well\x01",
            "served by a broad range of tactics.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000FWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030FOh, my...\x01",
            "This is a surprise.\x02\x03",
            "I presume you could tell from\x01",
            "my walk and the musculature of\x01",
            "my shoulders...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FThat, and the way your eyes move.\x02\x03",
            "A martial artist and swordsman\x01",
            "each have distinct ways that\x01",
            "they track their surroundings.\x02\x03",
            "You track for a specific point\x01",
            "on any possible target.\x02\x03",
            "It's characteristic of someone\x01",
            "who's familiar with small arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWhooooaaaa...\x01",
            "That's awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI see...\x01",
            "It certainly makes sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030FHm... I'll have to be more\x01",
            "careful in the future, then.\x02\x03",
            "And in your eyes, do I pass\x01",
            "muster for participating in\x01",
            "the tournament with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FYeah, I think so.\x01",
            "Welcome aboard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FI'm not sure I like this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThank you for your assistance,\x01",
            "Olivier.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_7830 end

    def Function_30_8EE2(): pass

    label("Function_30_8EE2")

    EventBegin(0x0)
    OP_6D(63970, 200, 7220, 0)
    OP_67(0, 7860, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x101, 23)
    SetChrChipByIndex(0x102, 24)
    SetChrChipByIndex(0x9, 25)
    SetChrPos(0x20, 58830, 640, -4430, 0)
    SetChrPos(0x25, 58360, 640, -4450, 0)
    SetChrPos(0x22, 59290, 640, -4980, 0)
    SetChrPos(0x23, 59290, 640, -4720, 0)
    SetChrPos(0x21, 58740, 640, -5400, 0)
    SetChrPos(0x24, 58930, 640, -5550, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x101, 60050, 200, -4970, 270)
    SetChrPos(0x9, 58770, 200, -3750, 180)
    SetChrPos(0x102, 58770, 200, -6150, 0)
    SetChrPos(0x16, 62360, 0, 2910, 0)
    ClearChrFlags(0x9, 0x80)
    FadeToBright(1000, 0)
    OP_6D(59510, 200, -4760, 5000)

    ChrTalk(
        0x101,
        (
            "#001FWhew... The food in here sure\x01",
            "is spicy. Tasty, though!\x02\x03",
            "#008FNothing beats ribs covered in\x01",
            "sauce with some potatoes that\x01",
            "are cooked just right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FI like a good cup of coffee\x01",
            "after a meal myself.\x02\x03",
            "I've always heard it's difficult\x01",
            "to make it well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142FBah... Way to eat up a man's\x01",
            "paycheck, you guys.\x02\x03",
            "I don't know how I'm supposed to\x01",
            "afford all this on a reporter's\x01",
            "salary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502FNow, now...\x01",
            "It was a great meal. And great\x01",
            "meals don't come cheap.\x02\x03",
            "#006FOkay now, you were saying something\x01",
            "about an interview...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142FHmph. I could write a story\x01",
            "about extortion...\x02\x03",
            "#145FMoving on. There ain't been much to confirm\x01",
            "that the queen's really taken ill after\x01",
            "the Guardsmen went all terrorist.\x02\x03",
            "What I need is some clear info\x01",
            "that HASN'T been combed over\x01",
            "and 'cleaned up' by the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FI heard a little from Dorothy\x01",
            "about the kidnapping in Zeiss...\x02\x03",
            "Look, let me get right to the point.\x02\x03",
            "I know you've got Colonel Richard by\x01",
            "the proverbial tail...I just need to\x01",
            "know how hard you're holding on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FWay to be blunt, there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FSounds like you've already figured\x01",
            "out an awful lot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145FI KNEW he was crooked...\x02\x03",
            "Before that interview in our magazine\x01",
            "bumped up his popularity, he wasn't really\x01",
            "well known or worth paying attention to.\x02\x03",
            "#142FSeems like this guy has been\x01",
            "planning his moves every step of the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FRight now, we can't say for sure\x01",
            "that he's planning some kind of\x01",
            "treason against the throne.\x02\x03",
            "But it does look like he's\x01",
            "manipulating the duke somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142FDuke Dunan...\x02\x03",
            "He's taking advantage of the queen's\x01",
            "poor health and acting like he owns\x01",
            "Grancel Castle, all right...\x02\x03",
            "But what I don't get is why\x01",
            "none of the military bigwigs\x01",
            "are making their move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FWell, about that...\x02\x03",
            "#505F...What do you think, Joshua?\x01",
            "Should we tell him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FWell, we could definitely use\x01",
            "some fresh intel ourselves.\x02\x03",
            "#010FAs long as he scratches our\x01",
            "backs...let's scratch his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#143FHey, now... You two know\x01",
            "something, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWe would have told you sooner...\x02\x03",
            "But anything we say from here\x01",
            "on out has to be completely\x01",
            "off the record.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#507FI hope you're ready for this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142FAhh, shit. I'm really not\x01",
            "going to like this, am I?\x02\x03",
            "But fine.\x01",
            "Say what you're gonna say.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x9, 3)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#145F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F*sigh* You said you were\x01",
            "ready for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145FThat's just...\x01",
            "No way...\x02\x03",
            "#142FAre you really serious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FI'm afraid so.\x02\x03",
            "The Special Ops soldiers were\x01",
            "behind the Sky Bandit incident,\x01",
            "as well as the arson.\x02\x03",
            "Not to mention the kidnapping of the\x01",
            "kingdom's greatest scientific mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FGeneral Morgan is at the top of\x01",
            "the chain of command, and even\x01",
            "he's basically under arrest.\x02\x03",
            "All of the terrorist-style activities\x01",
            "are being made out to look like the\x01",
            "Guardsmen are doing it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x9, 0)

    ChrTalk(
        0x9,
        (
            "#144FOkay, enough!\x01",
            "You've made your point!\x02\x03",
            "#145FDammit all... I can't even\x01",
            "report a word of this.\x02\x03",
            "The army's censors already have their\x01",
            "stamp all over the latest issue.\x02\x03",
            "They did their work at the\x01",
            "final printing stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142FAnd I'm left with nothing to cover\x01",
            "except for this damn tournament.\x02\x03",
            "#143F...Hey, wait a minute.\x02\x03",
            "You two have something up your\x01",
            "sleeves, don't you? That's why\x01",
            "you're in the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FYou could say that...\x02\x03",
            "We can't give you all the details\x01",
            "on our current request...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe do, however, think that we\x01",
            "need to make a move, just to\x01",
            "break the deadlock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142FYou don't say...\x02\x03",
            "#145F...\x02\x03",
            "...All right, then.\x02\x03",
            "#142FSince I can't do anything as \x01",
            "a reporter, I might as well\x01",
            "pitch in.\x02\x03",
            "I'll see what I can dig up. I've\x01",
            "got a few...sources...with fingers\x01",
            "in places the guild would never go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FThat'll be a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FDoing anything to oppose the\x01",
            "military's going to be a risky\x01",
            "proposition, you know.\x02\x03",
            "Are you sure you're okay\x01",
            "with this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#144FLet me deal with that.\x02\x03",
            "Now's as good a chance as ever\x01",
            "to prove that the pen really\x01",
            "is mightier than the sword!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FNial...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015FUnderstood... Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141FYeah, just leave it to me.\x02\x03",
            "So, what do you want more\x01",
            "information on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FInfo about the army's movements\x01",
            "would be good.\x02\x03",
            "As would knowing whether or not\x01",
            "all of the Royal Guardsmen have\x01",
            "been arrested...\x02\x03",
            "And also where General Morgan\x01",
            "is being held...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142FGot it. All stuff that I've\x01",
            "been thinking about, too.\x02\x03",
            "I'll check them out.\x01",
            "Anything else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013FUhh...\x02\x03",
            "Maybe some background info on someone\x01",
            "in the Intelligence Division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#143FYou mean like a background check?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FOn Colonel Richard, Captain Amalthea\x01",
            "and 2nd Lieutenant Lorence.\x02\x03",
            "If we have to face any of them, the\x01",
            "more we know, the better our odds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F'If you know the enemy and know\x01",
            "yourself, you need not fear the\x01",
            "result of a hundred battles.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FAnd you can bet that the colonel's\x01",
            "working on the same principle.\x02\x03",
            "He'll probably be watching the\x01",
            "fights tomorrow and the next day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FDo you think you can manage\x01",
            "it, Nial?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145FI do know a few army folks...\x02\x03",
            "I can't get you anything classified,\x01",
            "but I might be able to scare up that\x01",
            "profile info.\x02\x03",
            "#141FOkay, then...\x01",
            "I'll see what I can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FThank you!\x01",
            "You're a lifesaver!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141FHey, don't sweat it.\x02\x03",
            "You can pay me back by winning that\x01",
            "championship and filling me in on\x01",
            "what you hear at that dinner party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007FI figured as much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe'll do everything we can.\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterward, Estelle and Joshua returned to their hotel room, where they\x01",
            "retired early for the night.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The next morning...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_56(0x0)
    Sleep(500)
    OP_22(0xD, 0x0, 0x64)
    Sleep(3000)
    SetMapFlags(0x100000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4132   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_8EE2 end

    def Function_31_A64B(): pass

    label("Function_31_A64B")

    EventBegin(0x0)
    OP_6D(-61470, 0, 67180, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x9, -56660, 0, 64750, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, -61900, 0, 67420, 135)
    SetChrPos(0x102, -63460, 0, 66810, 135)

    ChrTalk(
        0x101,
        "#000FHeeeey! Nial!\x02",
    )

    CloseMessageWindow()

    def lambda_A6E0():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A6E0)

    ChrTalk(
        0x102,
        "#010FPardon us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FHey, you're here.\x02\x03",
            "Amazing. Dorothy actually got the message\x01",
            "to you guys, and didn't screw it up.\x01",
            "Will miracles never cease?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A78A():
        OP_6D(-57890, 0, 65099, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A78A)

    def lambda_A7A2():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_A7A2)

    def lambda_A7B2():

        label("loc_A7B2")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_A7B2")

    QueueWorkItem2(0x101, 1, lambda_A7B2)

    def lambda_A7C3():

        label("loc_A7C3")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_A7C3")

    QueueWorkItem2(0x9, 1, lambda_A7C3)

    def lambda_A7D4():
        OP_8E(0xFE, 0xFFFF18F2, 0x0, 0xFC94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A7D4)
    OP_8E(0x102, 0xFFFF1370, 0x0, 0x1046E, 0xBB8, 0x0)

    def lambda_A803():
        OP_8E(0xFE, 0xFFFF1F6E, 0x0, 0xFB9A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A803)
    OP_8E(0x102, 0xFFFF13B6, 0x0, 0xFC30, 0xBB8, 0x0)
    OP_8E(0x102, 0xFFFF1A28, 0x0, 0xF988, 0xBB8, 0x0)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x9,
        (
            "#140FSo...I hear you won your match today.\x02\x03",
            "Dorothy was in an absurdly cheerful\x01",
            "mood when she got back from it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FHa ha... Cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FNial, about what we discussed earlier...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FStraight to business, I see.\x02\x03",
            "Take a look... Got some background\x01",
            "on those big shots.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Nial held out a black file folder.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#000FIs this from the Royal Army?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FYeah... Nothing super-secret, but I\x01",
            "was able to get out some documents.\x02\x03",
            "Let's just say they're...on loan\x01",
            "from some of my army contacts. But\x01",
            "keep that under your hat, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FAbsolutely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWell, let's go ahead and\x01",
            "read it here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle and Joshua opened the black folder.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AB16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4E2")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABA8")

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Colonel Richard]\x01",             # 0
            "[Captain Amalthea]\x01",            # 1
            "[2nd Lieutenant Lorence]\x01",      # 2
            "[Close folder]\x01",                # 3
        )
    )

    Jump("loc_ABEF")

    label("loc_ABA8")


    Menu(
        0,
        10,
        10,
        0,
        (
            "[Colonel Richard]\x01",             # 0
            "[Captain Amalthea]\x01",            # 1
            "[2nd Lieutenant Lorence]\x01",      # 2
        )
    )


    label("loc_ABEF")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AC22"),
        (1, "loc_AF8B"),
        (2, "loc_B233"),
        (3, "loc_B4CF"),
        (SWITCH_DEFAULT, "loc_B4DF"),
    )


    label("loc_AC22")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Colonel Alan Richard.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Born 1168, in the Ruan region of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Graduated head of his class from the military academy, later assigned to the\x01",
            "mobile task force led by Cassius Bright.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "1192: Recognized for distinguished service under Cassius Bright in the\x01",
            "Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Appointed to staff of the military operations office after Colonel Bright's\x01",
            "retirement.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "1201: Suggested formation of Intelligence Division. Queen Alicia approves the\x01",
            "request and appoints him as the first commander of the new branch.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF88")
    OP_A2(0x673)

    ChrTalk(
        0x101,
        (
            "#000FWow... Pretty impressive.\x02\x03",
            "Well, he IS the man in charge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FHe always seemed to\x01",
            "be pretty sharp.\x02\x03",
            "Looks like Major Cid was right about\x01",
            "him serving under Dad ten years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FSo Dad really WAS a colonel...\x02\x03",
            "I wonder why he retired... I mean, he\x01",
            "had respect and fame and all that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF88")

    Jump("loc_B4DF")

    label("loc_AF8B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Captain Kanone Amalthea.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Born 1175, in Liberl's capital city of Grancel.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Her excellent grades at the military academy earned her a place on the staff\x01",
            "of the military operations office shortly after graduation.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "1201: Reassigned to the newly-formed Intelligence Division on Colonel\x01",
            "Richard's recommendation.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Later appointed as Colonel Richard's aide-de-camp, assisting directly with\x01",
            "military operational command.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B230")
    OP_A2(0x674)

    ChrTalk(
        0x101,
        (
            "#000F'Excellent grades' again. Another\x01",
            "intellectual big shot, looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThat appointment means that she's\x01",
            "been working for Colonel Richard\x01",
            "for a long time.\x02\x03",
            "No wonder she's so loyal to him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B230")

    Jump("loc_B4DF")

    label("loc_B233")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "2nd Lieutenant Lorence Belgar.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Age and nationality unknown.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A member of Jester who was invited by Colonel Richard to join the\x01",
            "Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Previous activities unknown.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4CC")
    OP_A2(0x675)

    ChrTalk(
        0x101,
        (
            "#000FHe's been in disguise all along...\x01",
            "He's not even from Liberl.\x02\x03",
            "And what's up with his old job as a\x01",
            "mercenary being one big blank spot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F...I don't know.\x02\x03",
            "Jaeger corps are known as the best\x01",
            "mercenaries in the business for good\x01",
            "reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FNo kidding?\x02\x03",
            "So maybe the colonel was just looking\x01",
            "for a really skilled fighter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's a possibility.\x02\x03",
            "And I think I've heard of this 'Jester'\x01",
            "somewhere before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4CC")

    Jump("loc_B4DF")

    label("loc_B4CF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_B4DF")

    label("loc_B4DF")

    Jump("loc_AB16")

    label("loc_B4E2")


    ChrTalk(
        0x101,
        (
            "#000FThanks for this, Nial. At least\x01",
            "we know a little more about\x01",
            "who we're dealing with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FAs long as it's useful.\x02\x03",
            "I've learned a few juicy tidbits\x01",
            "while I was digging around, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        "#010F'Juicy tidbits'...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FFor example, 1st Lieutenant Julia Schwarz\x01",
            "of the Royal Guardsman, currently\x01",
            "wanted for questioning...\x02\x03",
            "...was in the academy the same\x01",
            "year as Captain Amalthea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FReally, now...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThey never gave off the impression\x01",
            "that they got along all that well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FMaybe because they were\x01",
            "academy rivals.\x02\x03",
            "Kanone's got the brains, and\x01",
            "Julia's got the combat skills...\x01",
            "Pretty big difference there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FAhh, I see. I'd imagine so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FLooks like Julia's always been the\x01",
            "super-serious knightly type, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FNext up...and this has nothing to\x01",
            "do with the military, mind you...\x02\x03",
            "You kids know about\x01",
            "Princess Klaudia, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FPrincess Klaudia...\x01",
            "Sounds familiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIf memory serves, she was orphaned when\x01",
            "the crown prince and his wife died.\x02\x03",
            "She's the granddaughter of Her\x01",
            "Majesty, Queen Alicia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FRight. She's not well known, but\x01",
            "she is the direct descendant of\x01",
            "the queen.\x02\x03",
            "From what I could dig up, she lives\x01",
            "in the Royal Keep, and pretty much\x01",
            "stays there most of the time.\x02\x03",
            "And it seems someone's been\x01",
            "looking for prospective marriage\x01",
            "candidates for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FHuh...\x02\x03",
            "That's not super-unusual for\x01",
            "rich families, but still...\x02\x03",
            "Just...gross.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThat's not the point.\x02\x03",
            "The issue here is, who is\x01",
            "this 'someone'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#140FHa ha... Spot on, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FIt could be...\x02",
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
            "[Queen Alicia]\x01",         # 0
            "[Duke Dunan]\x01",           # 1
            "[Colonel Richard]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BB8B"),
        (1, "loc_BC4B"),
        (2, "loc_BD20"),
        (SWITCH_DEFAULT, "loc_BDD9"),
    )


    label("loc_BB8B")


    ChrTalk(
        0x9,
        (
            "#140FOn paper, sure.\x02\x03",
            "But it's Colonel Richard who's\x01",
            "scouring foreign countries for\x01",
            "a suitable candidate, looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FYou've gotta be kidding!\x02\x03",
            "But isn't that kind of weird?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDD9")

    label("loc_BC4B")


    ChrTalk(
        0x9,
        (
            "#140FClose, but no cigar, kid.\x02\x03",
            "Actually, it's Colonel Richard who's\x01",
            "been scouring foreign countries for\x01",
            "a suitable candidate, looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FYou've gotta be kidding!\x02\x03",
            "But isn't that kind of weird?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDD9")

    label("loc_BD20")


    ChrTalk(
        0x9,
        (
            "#140FHey, not bad, kid.\x02\x03",
            "It is Colonel Richard who's been\x01",
            "scouring foreign countries for a\x01",
            "suitable candidate, looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FI knew it...\x02\x03",
            "But isn't that kind of weird?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDD9")

    label("loc_BDD9")


    ChrTalk(
        0x101,
        (
            "#000FWhy would he even be involved in\x01",
            "setting up an arranged marriage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FPretty interesting, ain't it?\x02\x03",
            "And now...there's something\x01",
            "I want from you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYou want us to win the tournament\x01",
            "and get you some information at the\x01",
            "dinner party...right?\x02\x03",
            "Is that about the long\x01",
            "and short of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FOh, okay...\x02\x03",
            "You're not shy about asking\x01",
            "for stuff, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FHey, I got you information.\x01",
            "This is called 'give and\x01",
            "take,' sweetheart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FTrue, and it's been helpful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FOh, all right. We'll let you\x01",
            "know if we find out anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FThat's what I like to hear.\x02\x03",
            "Though if all goes well today, I might not even\x01",
            "need to rely on you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_44(0x9, 0xFF)
    OP_8E(0x9, 0xFFFF2630, 0x0, 0xFBCB, 0xBB8, 0x0)

    ChrTalk(
        0x9,
        (
            "#140FHello, Liberl News.\x02\x03",
            "Oh, it's you! I've been waiting\x01",
            "for you to call in.\x02\x03",
            "What...\x01",
            "Starting now?\x02\x03",
            "Okay, got it.\x01",
            "I'll meet you there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FWhat's going on?\x02",
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFF1F6E, 0x0, 0xFB9A, 0xBB8, 0x0)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "#140FSorry to cut and run on you, but\x01",
            "I've gotta go meet someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FSounds like you're in for a\x01",
            "late night. The sun's going\x01",
            "down as it is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FHey, I'm a night owl, anyways.\x02\x03",
            "I'm only up during the daytime while\x01",
            "the crazy chick is being trained.\x02\x03",
            "But hey, no biggie.\x02\x03",
            "You kids can just kick back\x01",
            "and relax while I'm out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FGotcha.\x02\x03",
            "Good luck with your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FYou too. Don't screw up\x01",
            "tomorrow's match!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C34A():

        label("loc_C34A")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_C34A")

    QueueWorkItem2(0x101, 1, lambda_C34A)

    def lambda_C35B():

        label("loc_C35B")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_C35B")

    QueueWorkItem2(0x102, 1, lambda_C35B)
    OP_8E(0x9, 0xFFFF1B9A, 0x0, 0xFF14, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF1564, 0x0, 0xFF14, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF1258, 0x0, 0x1039C, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF0736, 0x0, 0x1039C, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF0736, 0xFFFFF74A, 0xF406, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000FWell, then...\x01",
            "What should we do now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FHmmm... I guess we should stop\x01",
            "by the guild, then go back to\x01",
            "the hotel.\x02\x03",
            "We ought to report in the info\x01",
            "that Nial got for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FFine by me.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_31_A64B end

    def Function_32_C4B5(): pass

    label("Function_32_C4B5")

    EventBegin(0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -56250, 0, 60940, 90)
    SetChrPos(0x101, -60190, 0, 65280, 135)
    SetChrPos(0x102, -61190, 0, 64849, 135)
    SetChrPos(0x108, -60700, 0, 66190, 135)
    OP_6D(-54490, 0, 61730, 0)

    ChrTalk(
        0xA,
        (
            "#150FThis is weird, Chief.\x02\x03",
            "We haven't heard anything\x01",
            "in two days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmmm... Well, he does tend to get \x01",
            "completely wrapped up when he's\x01",
            "looking for the next big story...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...but given how close we are to a state\x01",
            "of martial law, I don't much like that\x01",
            "he hasn't contacted us, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(
        0xB,
        "Hm...?\x02",
    )

    CloseMessageWindow()

    def lambda_C668():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C668)
    OP_6D(-56640, 0, 63970, 2000)

    ChrTalk(
        0xA,
        "#150FOh, hi, guys!\x02",
    )

    CloseMessageWindow()

    def lambda_C69F():

        label("loc_C69F")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C69F")

    QueueWorkItem2(0xA, 1, lambda_C69F)

    def lambda_C6B0():

        label("loc_C6B0")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_C6B0")

    QueueWorkItem2(0x101, 1, lambda_C6B0)

    def lambda_C6C1():

        label("loc_C6C1")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_C6C1")

    QueueWorkItem2(0x102, 1, lambda_C6C1)

    def lambda_C6D2():

        label("loc_C6D2")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_C6D2")

    QueueWorkItem2(0x108, 1, lambda_C6D2)

    def lambda_C6E3():
        OP_8E(0xFE, 0xFFFF2AF4, 0x0, 0xF532, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C6E3)
    Sleep(100)

    def lambda_C703():
        OP_8E(0xFE, 0xFFFF26EE, 0x0, 0xF51E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C703)
    Sleep(300)

    def lambda_C723():
        OP_8E(0xFE, 0xFFFF22D4, 0x0, 0xF4EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_C723)
    OP_6D(-54340, 0, 62290, 3000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)

    ChrTalk(
        0xB,
        "Hey, it's the tournament champions...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm the editor-in-chief of\x01",
            "the Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Nial and Dorothy have told me\x01",
            "quite a bit about the two of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Estelle and Joshua, of the\x01",
            "Bracer Guild, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FGood afternoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's a pleasure to meet you.\x02\x03",
            "I've always enjoyed your magazine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ha ha ha... Well, that's always\x01",
            "good to hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Weren't you two doing something\x01",
            "for Nial?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, uh, yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, it's you...\x01",
            "Perfect timing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FGood afternoon...\x02\x03",
            "We're here to talk to Nial, but\x01",
            "I'm guessing he's not around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That's what we were just\x01",
            "talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Actually, Nial hasn't shown up\x01",
            "here today or yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "No word from him or anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYesterday or today...?\x02\x03",
            "We spoke with him in the\x01",
            "evening, two days ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        "#150FR-Really...?!\x02",
    )

    CloseMessageWindow()

    def lambda_CAA5():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CAA5)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        (
            "#000FWhat do you mean 'really'?!\x01",
            "YOU gave us the message to\x01",
            "meet him, for Aidios' sake!\x02\x03",
            "We came here to talk to him\x01",
            "after the semifinals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150FOh, right...\x01",
            "Now that you mention it...\x02\x03",
            "So, did he say anything to you?\x02\x03",
            "Like where he was going...?\x02",
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
            "[Out researching an article.]\x01",       # 0
            "[Someone had just called him.]\x01",      # 1
            "[We went out to dinner.]\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CC5F"),
        (1, "loc_CD11"),
        (2, "loc_CD7A"),
        (SWITCH_DEFAULT, "loc_CE14"),
    )


    label("loc_CC5F")


    ChrTalk(
        0x102,
        (
            "#010FHe might have gone to do some\x01",
            "research for an article...\x02\x03",
            "But I can say that he got a call\x01",
            "from someone, then he said he\x01",
            "had to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FYeah, I remember...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE14")

    label("loc_CD11")


    ChrTalk(
        0x102,
        (
            "#010FRight. I remember what happened.\x02\x03",
            "He got a call from someone,\x01",
            "then he said he had to leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE14")

    label("loc_CD7A")


    ChrTalk(
        0x102,
        (
            "#010FNo, that was three days ago.\x02\x03",
            "Two days ago, though, someone\x01",
            "called him up, and then he\x01",
            "said he had to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FWas that how it went?\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE14")

    label("loc_CE14")


    ChrTalk(
        0xB,
        "Are you serious?\x02",
    )

    CloseMessageWindow()

    def lambda_CE30():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CE30)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(
        0x102,
        (
            "#010FYes.\x02\x03",
            "We haven't seen hide nor\x01",
            "hair of him since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150FOh, noooo!\x01",
            "I can't believe Nial's dead!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        (
            "#000FWha...\x01",
            "Who said he was dead?!\x02\x03",
            "Today's when all the airliner\x01",
            "traffic gets shut down...\x02\x03",
            "Everything was normal yesterday,\x01",
            "though...so maybe he went to\x01",
            "another province?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I already inquired with the\x01",
            "landing port's passenger registry,\x01",
            "and there was no sign of him.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CFCE():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CFCE)

    def lambda_CFDC():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CFDC)

    ChrTalk(
        0xB,
        (
            "So, I figure he has to still\x01",
            "be somewhere in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FHmmmm...\x02\x03",
            "You two were the last ones to\x01",
            "see this reporter fellow...\x02\x03",
            "Weren't you talking to him about\x01",
            "something for a news article?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D0B0():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D0B0)

    def lambda_D0BE():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D0BE)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        "#000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FThese are the times we live in.\x02\x03",
            "Controlling the media is a big\x01",
            "deal for the military.\x02\x03",
            "What do you think, Chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I certainly can't argue with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Particularly in the case of the\x01",
            "Intelligence Division. They monitor\x01",
            "and censor everything we do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You wouldn't believe how\x01",
            "frustrating it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FWhich means that you can't get\x01",
            "much information for your stories.\x02\x03",
            "But it's in a reporter's nature\x01",
            "to want to get as much as possible\x01",
            "into the hands of the readers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI see...\x02\x03",
            "So he went to check out a new subject\x01",
            "that the Intelligence Division hasn't\x01",
            "started censoring yet...\x02\x03",
            "What was the last thing\x01",
            "he told us about...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FI think it was about...\x02",
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
            "[The tournament winners.]\x01",                         # 0
            "[An arranged marriage for Princess Klaudia.]\x01",      # 1
            "[Julia and Kanone's history.]\x01",                     # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D44C"),
        (1, "loc_D603"),
        (2, "loc_D651"),
        (SWITCH_DEFAULT, "loc_D840"),
    )


    label("loc_D44C")


    ChrTalk(
        0x108,
        (
            "#070FThat's the story he was working\x01",
            "on, but we talked to him the day\x01",
            "before the championship bout.\x02\x03",
            "Maybe he was short on material.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FOh, okay...\x02\x03",
            "It looked like those Special Ops\x01",
            "guys were going to win...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI think I have an idea.\x02\x03",
            "Nial seemed particularly interested in the\x01",
            "marriage prospect thing for the princess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FHey, yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FAnd the duke mentioned something\x01",
            "about it at the dinner party...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D840")

    label("loc_D603")


    ChrTalk(
        0x108,
        (
            "#070FAnd the duke mentioned something\x01",
            "about it at the dinner party...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D840")

    label("loc_D651")


    ChrTalk(
        0x108,
        (
            "#070FColonel Richard's aide-de-camp\x01",
            "and a woman in the Guardsmen were\x01",
            "rivals in military academy...\x02\x03",
            "Which is interesting, but wouldn't\x01",
            "the Intelligence Division have\x01",
            "already made that connection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FOops, yeah... So he probably couldn't\x01",
            "print a story about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI think I have an idea.\x02\x03",
            "Nial seemed particularly interested in the\x01",
            "marriage prospect thing for the princess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FHey, yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FAnd the duke mentioned something\x01",
            "about it at the dinner party...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D840")

    label("loc_D840")


    ChrTalk(
        0xB,
        "Oh, Nial told you about that too?\x02",
    )

    CloseMessageWindow()

    def lambda_D86D():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D86D)

    def lambda_D87B():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D87B)

    ChrTalk(
        0xB,
        "It'd make a hell of a story if it's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He mentioned having to get some\x01",
            "evidence at any cost...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FHow did a reporter like Nial even\x01",
            "learn about something like that?\x02\x03",
            "I'd have thought that something\x01",
            "like that would be known only\x01",
            "to the royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150FWell, he did say he's friends\x01",
            "with someone who works in the\x01",
            "Erbe Royal Villa...\x02\x03",
            "Completely off the record, but\x01",
            "the terrorists are supposedly\x01",
            "after the princess.\x02\x03",
            "So she's secretly staying in\x01",
            "the villa for her own safety.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_DAC3():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DAC3)

    def lambda_DAD1():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DAD1)

    def lambda_DADF():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_DADF)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F...I knew it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070FHa...and the veil is lifted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FMaybe the person he was talking\x01",
            "to was his friend in the villa...\x02\x03",
            "...which would mean that Nial's\x01",
            "probably there, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You don't say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, if I know Nial, he probably\x01",
            "tried to worm his way in for an\x01",
            "interview with the princess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And if the soldiers saw him, they'd\x01",
            "have arrested him on the spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#150FNooooo! Nial's a goner!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWhy do you keep coming\x01",
            "back to that...?\x02\x03",
            "But if he HAS been arrested,\x01",
            "getting him out isn't going\x01",
            "to be easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYeah...\x02\x03",
            "I'm betting that he and Princess\x01",
            "Klaudia are pretty much in the\x01",
            "same situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What exactly do you\x01",
            "people know...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Do you have inside information\x01",
            "about what's going on in this\x01",
            "city...in all of Liberl?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DDF8():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DDF8)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(
        0x101,
        (
            "#000FSorry...but we really can't\x01",
            "talk about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FJust let the Bracer Guild take\x01",
            "care of Nial.\x02\x03",
            "If he has been arrested, we'll\x01",
            "see to it that he's released.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "All right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Please do whatever you can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150FPlease, you guys!\x02\x03",
            "You gotta bring Nial back!!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        "#000FLeave it to us!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_32_C4B5 end

    def Function_33_DF41(): pass

    label("Function_33_DF41")

    EventBegin(0x0)
    OP_6D(-53660, 0, 62750, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(33000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -59130, 0, 59600, 0)
    SetChrPos(0x9, -53500, 0, 62630, 90)
    OP_6D(-54490, 0, 61730, 0)

    ChrTalk(
        0x9,
        (
            "#140FDamn...\x01",
            "Looks like it's started!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DFF3():
        OP_6D(-56110, 0, 62480, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DFF3)
    OP_8E(0x9, 0xFFFF2400, 0x0, 0xF44C, 0xBB8, 0x0)
    TurnDirection(0x9, 0xA, 400)

    ChrTalk(
        0x9,
        (
            "#140FLet's go, Dorothy!\x02\x03",
            "We've got to get a good\x01",
            "spot to watch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150FW-Wait!\x02\x03",
            "Let me set up the exposure quartz!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hey, what's going on?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You haven't shown up in\x01",
            "three days, and...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 400)

    ChrTalk(
        0x9,
        (
            "#140FBig story!\x02\x03",
            "Biggest in the history of\x01",
            "the Liberl News!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4240   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_33_DF41 end

    SaveToFile()

Try(main)
