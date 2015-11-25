from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3111   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3111   ._SN',
            'ED6_DT01/T3111_1 ._SN',
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
        'Hazel',                                # 9
        'Louise',                               # 10
        'Hugo',                                 # 11
        'Rutherford',                           # 12
        'Dodge',                                # 13
        'Rudi',                                 # 14
        'Faye',                                 # 15
        'Erick',                                # 16
        'Dorothy',                              # 17
        'Radmira',                              # 18
        'Charles',                              # 19
        'Karl',                                 # 20
        'Gasoline',                             # 21
        'Antoine',                              # 22
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
        'ED6_DT07/CH01540 ._CH',             # 00
        'ED6_DT07/CH01550 ._CH',             # 01
        'ED6_DT07/CH01430 ._CH',             # 02
        'ED6_DT07/CH01680 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH01140 ._CH',             # 05
        'ED6_DT07/CH01500 ._CH',             # 06
        'ED6_DT07/CH01550 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH02070 ._CH',             # 09
        'ED6_DT07/CH01690 ._CH',             # 0A
        'ED6_DT07/CH02640 ._CH',             # 0B
        'ED6_DT07/CH01190 ._CH',             # 0C
        'ED6_DT07/CH01700 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH01540P._CP',             # 00
        'ED6_DT07/CH01550P._CP',             # 01
        'ED6_DT07/CH01430P._CP',             # 02
        'ED6_DT07/CH01680P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH01140P._CP',             # 05
        'ED6_DT07/CH01500P._CP',             # 06
        'ED6_DT07/CH01550P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH02070P._CP',             # 09
        'ED6_DT07/CH01690P._CP',             # 0A
        'ED6_DT07/CH02640P._CP',             # 0B
        'ED6_DT07/CH01190P._CP',             # 0C
        'ED6_DT07/CH01700P._CP',             # 0D
    )

    DeclNpc(
        X                   = 260,
        Z                   = 0,
        Y                   = 5800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 8,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Direction           = 14,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -203000,
        Y                   = -1000,
        Z                   = 137400,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = -5000,
        Y                   = -1000,
        Z                   = 7500,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = -5860,
        Y                   = -1000,
        Z                   = 7630,
        Range               = -3720,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x227E,
        Unknown_18          = 0x0,
        Unknown_1C          = 27,
    )


    DeclActor(
        TriggerX            = -109100,
        TriggerZ            = -3500,
        TriggerY            = -109000,
        TriggerRange        = 1200,
        ActorX              = -109100,
        ActorZ              = -3500,
        ActorY              = -109000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9880,
        TriggerZ            = 0,
        TriggerY            = -3600,
        TriggerRange        = 1200,
        ActorX              = -9880,
        ActorZ              = 0,
        ActorY              = -3600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -98280,
        TriggerZ            = -4000,
        TriggerY            = -103420,
        TriggerRange        = 1200,
        ActorX              = -98280,
        ActorZ              = -4000,
        ActorY              = -103420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 31,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 50,
        TriggerZ            = 0,
        TriggerY            = 3900,
        TriggerRange        = 400,
        ActorX              = 260,
        ActorZ              = 1500,
        ActorY              = 5800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6900,
        TriggerZ            = 0,
        TriggerY            = -1410,
        TriggerRange        = 400,
        ActorX              = 8650,
        ActorZ              = 1500,
        ActorY              = -1120,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -103970,
        TriggerZ            = 0,
        TriggerY            = -99940,
        TriggerRange        = 1200,
        ActorX              = -103970,
        ActorZ              = 1000,
        ActorY              = -99940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5050,
        TriggerZ            = 0,
        TriggerY            = 8080,
        TriggerRange        = 800,
        ActorX              = -5050,
        ActorZ              = 1000,
        ActorY              = 8080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -202970,
        TriggerZ            = 0,
        TriggerY            = 138010,
        TriggerRange        = 800,
        ActorX              = -202970,
        ActorZ              = 1000,
        ActorY              = 138010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -200120,
        TriggerZ            = 0,
        TriggerY            = 118010,
        TriggerRange        = 1200,
        ActorX              = -200120,
        ActorZ              = 1500,
        ActorY              = 118010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 35,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -121030,
        TriggerZ            = -4000,
        TriggerY            = -99900,
        TriggerRange        = 800,
        ActorX              = -121030,
        ActorZ              = -3000,
        ActorY              = -99900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4A2",          # 00, 0
        "Function_1_8FC",          # 01, 1
        "Function_2_C0E",          # 02, 2
        "Function_3_C24",          # 03, 3
        "Function_4_C2F",          # 04, 4
        "Function_5_DD3",          # 05, 5
        "Function_6_1770",         # 06, 6
        "Function_7_19DF",         # 07, 7
        "Function_8_1A39",         # 08, 8
        "Function_9_22BA",         # 09, 9
        "Function_10_3785",        # 0A, 10
        "Function_11_3EAF",        # 0B, 11
        "Function_12_567A",        # 0C, 12
        "Function_13_56D5",        # 0D, 13
        "Function_14_601B",        # 0E, 14
        "Function_15_63D1",        # 0F, 15
        "Function_16_6512",        # 10, 16
        "Function_17_675B",        # 11, 17
        "Function_18_69A4",        # 12, 18
        "Function_19_69A9",        # 13, 19
        "Function_20_69AE",        # 14, 20
        "Function_21_6B25",        # 15, 21
        "Function_22_6CF8",        # 16, 22
        "Function_23_7596",        # 17, 23
        "Function_24_75AC",        # 18, 24
        "Function_25_7769",        # 19, 25
        "Function_26_77E2",        # 1A, 26
        "Function_27_7B27",        # 1B, 27
        "Function_28_7B28",        # 1C, 28
        "Function_29_7EAA",        # 1D, 29
        "Function_30_7F32",        # 1E, 30
        "Function_31_84DD",        # 1F, 31
        "Function_32_8A88",        # 20, 32
        "Function_33_8BC9",        # 21, 33
        "Function_34_8CFB",        # 22, 34
        "Function_35_8E3B",        # 23, 35
        "Function_36_8E9D",        # 24, 36
    )


    def Function_0_4A2(): pass

    label("Function_0_4A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_4B0")
    OP_A3(0x3FA)
    Event(0, 22)

    label("loc_4B0")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_4C8"),
        (100, "loc_4DC"),
        (106, "loc_4F2"),
        (101, "loc_4F2"),
        (SWITCH_DEFAULT, "loc_4FA"),
    )


    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DC")
    OP_A2(0x508)
    Event(0, 21)

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    OP_A2(0x52D)
    Event(0, 26)

    label("loc_4EF")

    Jump("loc_4FA")

    label("loc_4F2")

    OP_22(0xE, 0x0, 0x64)
    Jump("loc_4FA")

    label("loc_4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_530")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -116000, -4000, -113000, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8650, 0, -1120, 274)
    Jump("loc_8FB")

    label("loc_530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_592")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -100740, -4000, -111030, 12)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8650, 0, -1120, 274)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -7440, 0, -6000, 2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 8720, 0, 3970, 39)
    Jump("loc_8FB")

    label("loc_592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_60A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -100740, -4000, -111030, 12)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -116000, -4000, -113000, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8650, 0, -1120, 274)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -7440, 0, -6000, 2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 8720, 0, 3970, 39)
    Jump("loc_8FB")

    label("loc_60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_656")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -100740, -4000, -111030, 12)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -116000, -4000, -113000, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8650, 0, -1120, 274)
    Jump("loc_8FB")

    label("loc_656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_72B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_67F")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 10930, 0, -5500, 9)
    SetChrFlags(0x10, 0x10)

    label("loc_67F")

    SetChrPos(0x9, -9980, 0, -1060, 171)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -10100, 0, -2700, 347)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -116000, -4000, -113000, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8650, 0, -1120, 274)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 6890, 0, -3020, 169)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -7870, 0, -1230, 263)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 6870, 0, -4430, 11)
    SetChrFlags(0x13, 0x10)
    Jump("loc_8FB")

    label("loc_72B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_73A")
    SetChrFlags(0x8, 0x80)
    Jump("loc_8FB")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_7B2")
    SetChrPos(0xB, -9980, 0, -1060, 171)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -10100, 0, -2700, 347)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 6870, 0, 50, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -116000, -4000, -113000, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8650, 0, -1120, 274)
    Jump("loc_8FB")

    label("loc_7B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_81C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -100400, 0, -101990, 103)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -113390, -4000, -111160, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_803")
    SetChrPos(0xE, -116000, -4000, -113000, 270)
    SetChrFlags(0xE, 0x10)

    label("loc_803")

    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8650, 0, -1120, 274)
    Jump("loc_8FB")

    label("loc_81C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_872")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -120940, -4000, -106020, 182)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -120920, -4000, -107100, 355)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8650, 0, -1120, 274)
    Jump("loc_8FB")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_8C3")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -100740, -4000, -111030, 12)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -116000, -4000, -113000, 270)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8650, 0, -1120, 274)
    Jump("loc_8FB")

    label("loc_8C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8FB")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -116000, -4000, -113000, 270)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8650, 0, -1120, 274)

    label("loc_8FB")

    Return()

    # Function_0_4A2 end

    def Function_1_8FC(): pass

    label("Function_1_8FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91E")
    SetMapFlags(0x800)
    OP_1B(0x3, 0x0, 0x3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_94B")

    label("loc_91E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_936")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_94B")

    label("loc_936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_94B")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_95B"),
        (109, "loc_95B"),
        (SWITCH_DEFAULT, "loc_993"),
    )


    label("loc_95B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98B")
    OP_71(0x6, 0x4)
    OP_75(0xFF, 0xF, 0x5)
    OP_75(0xFF, 0x18, 0x5)
    OP_75(0xFF, 0x24, 0x5)
    OP_75(0xFF, 0x33, 0x5)
    Jump("loc_990")

    label("loc_98B")

    OP_22(0xA0, 0x1, 0x64)

    label("loc_990")

    Jump("loc_999")

    label("loc_993")

    OP_23(0xA0)
    Jump("loc_999")

    label("loc_999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B0")
    OP_6F(0x5, 0)
    OP_72(0x5, 0x10)
    Jump("loc_9B4")

    label("loc_9B0")

    OP_64(0x5, 0x1)

    label("loc_9B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E2")
    OP_65(0x0, 0x1)
    OP_72(0x8, 0x4)
    OP_A1(0x14, 0x8)
    SetChrPos(0x14, -109320, -3300, -109150, 14)
    Jump("loc_9E6")

    label("loc_9E2")

    OP_64(0x0, 0x1)

    label("loc_9E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA7")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    PlayEffect(0x0, 0x0, 0xFF, -9880, 0, -3600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_AAB")

    label("loc_AA7")

    OP_64(0x1, 0x1)

    label("loc_AAB")

    Jump("loc_B4A")

    label("loc_AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B46")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    PlayEffect(0x0, 0x2, 0xFF, -98280, -4000, -103420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_B4A")

    label("loc_B46")

    OP_64(0x2, 0x1)

    label("loc_B4A")

    OP_72(0x0, 0x10)
    OP_72(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_B73")
    OP_72(0x0, 0x10)
    OP_6F(0x0, 30)
    OP_72(0x0, 0x10)
    OP_10(0x1, 0x0)
    OP_64(0x6, 0x1)

    label("loc_B73")

    Jump("loc_B86")

    label("loc_B76")

    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)

    label("loc_B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_B90")
    Jump("loc_B9F")

    label("loc_B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B9F")
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)

    label("loc_B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB0")
    OP_1B(0x0, 0x0, 0x22)

    label("loc_BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC4")
    OP_1B(0x3, 0x0, 0x21)
    Jump("loc_BD5")

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD5")
    OP_1B(0x3, 0x0, 0x20)

    label("loc_BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE7")
    OP_10(0xC, 0x1)
    OP_10(0x0, 0x0)

    label("loc_BE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFA")
    OP_1B(0x0, 0x0, 0x10)

    label("loc_BFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0D")
    OP_1B(0x3, 0x0, 0x11)

    label("loc_C0D")

    Return()

    # Function_1_8FC end

    def Function_2_C0E(): pass

    label("Function_2_C0E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C23")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_C0E")

    label("loc_C23")

    Return()

    # Function_2_C0E end

    def Function_3_C24(): pass

    label("Function_3_C24")

    ClearMapFlags(0x800)
    OP_1B(0x3, 0x0, 0xFFFF)
    Return()

    # Function_3_C24 end

    def Function_4_C2F(): pass

    label("Function_4_C2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_DCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_CEE")

    ChrTalk(
        0xFE,
        (
            "Hmm. Okay. To put things in\x01",
            "simple terms...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's all about performance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(*sigh* After an incident like\x01",
            "that I'm really not in the mood\x01",
            "to sell anything...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCF")

    label("loc_CEE")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "Uh...okay, look...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This model here has only the\x01",
            "tiniest differences and honestly,\x01",
            "I recommend it more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What? No? You want a\x01",
            "user-friendly camera?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'User-friendly' can be such a\x01",
            "relative term nowadays...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCF")

    TalkEnd(0xFE)
    Return()

    # Function_4_C2F end

    def Function_5_DD3(): pass

    label("Function_5_DD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_126F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_117D")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F...?\x02\x03",
            "#010FAh, hey.\x01",
            "It HAS been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FWho's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYou remember that kid who was\x01",
            "looking for that piece of quartz in\x01",
            "Rolent, don't you?\x02\x03",
            "Remember? We took a request\x01",
            "to find it a while back.\x02\x03",
            "Are you helping your mother?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "Yeah, a little. I've got to get\x01",
            "back to Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y'know, once my sisters get\x01",
            "a little bigger, I'm getting out\x01",
            "of this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to get into the Central\x01",
            "Factory, start at the bottom, and\x01",
            "learn to build airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm good with my hands, so my\x01",
            "mom ought to understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWow...\x02\x03",
            "Good for you! That's a pretty\x01",
            "big ambition!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "No kidding. I got my whole\x01",
            "life ahead of me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I should get back to\x01",
            "helping out my mom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got four little sisters, you know.\x01",
            "Real little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FOkay, then.\x01",
            "Good luck!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "Yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Good luck to you guys, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_126C")

    label("loc_117D")


    ChrTalk(
        0xFE,
        (
            "Y'know, once my sisters get\x01",
            "a little bigger, I'm getting out\x01",
            "of this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to get into the Central\x01",
            "Factory, start at the bottom, and\x01",
            "learn to build airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm good with my hands, so my\x01",
            "mom ought to understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126C")

    Jump("loc_176C")

    label("loc_126F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_171B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15DA")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F...?\x02\x03",
            "#010FAh, hey.\x01",
            "It HAS been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FWho's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYou remember that kid who was\x01",
            "looking for that piece of quartz in\x01",
            "Rolent, don't you?\x02\x03",
            "Remember? We took a request\x01",
            "to find it a while back.\x02\x03",
            "Are you helping your mother?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "Yeah, a little. I've got to get\x01",
            "back to Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y'know, once my sisters get\x01",
            "a little bigger, I'm getting out\x01",
            "of this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to get into the Central\x01",
            "Factory, start at the bottom, and\x01",
            "learn to build airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWow...\x02\x03",
            "Good for you! That's a pretty\x01",
            "big ambition!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "No kidding. I got my whole\x01",
            "life ahead of me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I should get back to\x01",
            "helping out my mom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got four little sisters, you know.\x01",
            "Real little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FOkay, then.\x01",
            "Good luck!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "Yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Good luck to you guys, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1718")

    label("loc_15DA")


    ChrTalk(
        0xFE,
        (
            "Y'know, once my sisters get\x01",
            "a little bigger, I'm getting out\x01",
            "of this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to get into the Central\x01",
            "Factory, start at the bottom, and\x01",
            "learn to build airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got to help my mom out for\x01",
            "the time being, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mom can get pretty swamped\x01",
            "having to take care of four little\x01",
            "baby sisters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1718")

    Jump("loc_176C")

    label("loc_171B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_176C")

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Whoa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So this is where they make\x01",
            "orbal engines, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_176C")

    TalkEnd(0xFE)
    Return()

    # Function_5_DD3 end

    def Function_6_1770(): pass

    label("Function_6_1770")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_182C")

    ChrTalk(
        0xFE,
        "Time to close up shop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've sold a good lot and stocked\x01",
            "up on plenty of goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And my little Charles looks like\x01",
            "he finally wants to do something\x01",
            "with himself!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19DB")

    label("loc_182C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_18AD")

    ChrTalk(
        0xFE,
        (
            "I came to pick up some\x01",
            "orbal cameras...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...and my son actually HELPED\x01",
            "me with it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What's come over him?\x02",
    )

    CloseMessageWindow()
    Jump("loc_19DB")

    label("loc_18AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_19DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1934")

    ChrTalk(
        0xFE,
        (
            "I know things have been a\x01",
            "little difficult lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if you could explain it\x01",
            "to me in simpler terms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19DB")

    label("loc_1934")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "I don't have a degree in mathematics,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard this camera is the most\x01",
            "user-friendly model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You make cameras, don't you?\x01",
            "What do you think?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19DB")

    TalkEnd(0xFE)
    Return()

    # Function_6_1770 end

    def Function_7_19DF(): pass

    label("Function_7_19DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_1A35")

    ChrTalk(
        0x10,
        (
            "#150FHmm, I usually go for set 5.\x02\x03",
            "Oh yeah, I need a panoramic,\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A35")

    TalkEnd(0xFE)
    Return()

    # Function_7_19DF end

    def Function_8_1A39(): pass

    label("Function_8_1A39")

    TalkBegin(0xF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                 # 0
            "Modify/Exchange\x01",      # 1
            "Leave\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA4")
    OP_0D()
    OP_A9(0x3C)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_1AA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AB5")
    TalkEnd(0xF)
    Return()

    label("loc_1AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1AFB")

    ChrTalk(
        0xF,
        "Welcome to Maintenance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "We're ready to serve you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B6")

    label("loc_1AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1BA2")

    ChrTalk(
        0xF,
        "What happened over there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It looks like the factory ship\x01",
            "crew are all getting hustled\x01",
            "out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Was there some kind of\x01",
            "accident somewhere?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B6")

    label("loc_1BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1BF8")

    ChrTalk(
        0xF,
        (
            "Good morning, welcome\x01",
            "to Maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "We're ready to do our best!\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B6")

    label("loc_1BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1CA9")

    ChrTalk(
        0xF,
        "Wow, you're here late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'll still be here though, so if\x01",
            "you need anything just come\x01",
            "on over and ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Man, what a hectic day.\x01",
            "I am completely exhausted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B6")

    label("loc_1CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_1E48")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_END)), "loc_1D8C")

    ChrTalk(
        0xF,
        (
            "Karl's invented everything,\x01",
            "from orbal cameras to guns!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The Central Factory is full of\x01",
            "geniuses, thanks to Professor\x01",
            "Russell running it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The inspiration probably just\x01",
            "spreads through everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E45")

    label("loc_1D8C")

    OP_A2(0x5)

    ChrTalk(
        0xF,
        (
            "Just when everything looks like\x01",
            "it's back to normal, we get the\x01",
            "visitor from hell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "That old lady over there has\x01",
            "done nothing but complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I hope Karl can handle her.\x02",
    )

    CloseMessageWindow()

    label("loc_1E45")

    Jump("loc_22B6")

    label("loc_1E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1F43")

    ChrTalk(
        0xF,
        (
            "See that customer over there? He's\x01",
            "what you might call a layman. No\x01",
            "orbment knowledge whatsoever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "You think I should try to explain\x01",
            "how they work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hmm...not a good idea. He'd\x01",
            "probably just start moaning\x01",
            "and groaning and such.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B6")

    label("loc_1F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1FD4")

    ChrTalk(
        0xF,
        "Hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Would you like to see our\x01",
            "selection of quartz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We have quite a wide variety of\x01",
            "quality crystals to peruse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B6")

    label("loc_1FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_20DA")

    ChrTalk(
        0xF,
        (
            "Good morning! It's been quite\x01",
            "a busy day so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We've had so many customers coming\x01",
            "in thinking last night's incident\x01",
            "was due to broken orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It makes you realize just how\x01",
            "many of Zeiss' citizens don't\x01",
            "understand orbment technology.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B6")

    label("loc_20DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_21D1")

    ChrTalk(
        0xF,
        "Welcome to Maintenance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "To tell you the truth, I'm \x01",
            "really a factory researcher.\x01",
            "Well, a junior researcher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm studying orbment service\x01",
            "and maintenance right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "One day I'd love to have my\x01",
            "own research laboratory!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B6")

    label("loc_21D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_22B6")

    ChrTalk(
        0xF,
        "Welcome to Maintenance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "This may seem like just a service window,\x01",
            "but we're a full part of the factory's orbment\x01",
            "division, as fully equipped as any shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Please feel free to make full\x01",
            "use of our facilities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B6")

    TalkEnd(0xF)
    Return()

    # Function_8_1A39 end

    def Function_9_22BA(): pass

    label("Function_9_22BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AE7")
    TalkBegin(0xFE)
    OP_A2(0x53D)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -114810, -4000, -111130, 90)
    SetChrPos(0x102, -114650, -4000, -112120, 45)
    TurnDirection(0xE, 0x101, 0)
    OP_69(0xE, 0x3E8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_232C")

    ChrTalk(
        0x101,
        "#000FExcuse me?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2354")

    label("loc_232C")


    ChrTalk(
        0x102,
        "#010FWe have a small favor to ask.\x02",
    )

    CloseMessageWindow()

    label("loc_2354")


    ChrTalk(
        0xE,
        "#2PWhat's that? May I help you?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle and Joshua explained the task set to them by Professor Russell.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xE,
        "#2PYou need gasoline?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2PI think we have a tank of it\x01",
            "back in storage somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2PI'll check for you.\x02",
    )

    CloseMessageWindow()

    def lambda_2458():
        OP_6D(-112600, -4000, -109400, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2458)
    OP_8C(0xE, 0, 400)
    WaitChrThread(0x101, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Faye used the intercom.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xE,
        (
            "#2PThis is Faye. Got a request\x01",
            "down here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2PWe still have that tank of\x01",
            "Calvard gasoline there in\x01",
            "the warehouse, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2PCan you send some down?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2PYeah, enough to carry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2PThanks.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(
        0xE,
        (
            "#2PThey're sending some\x01",
            "for you right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FSending...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 90, 400)
    OP_72(0x8, 0x4)
    OP_A1(0x14, 0x8)
    SetChrPos(0x14, -95360, -3300, -109080, 14)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x14, 0x4)

    def lambda_25F8():
        OP_8F(0xFE, 0xFFFE54F8, 0xFFFFF31C, 0xFFFE55A2, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_25F8)
    OP_22(0x5B, 0x1, 0x64)
    OP_76(0xFF, 0xF, 0x1, 0x2, 0x0, 0x3E8, 0x0, 0x0)
    OP_76(0xFF, 0x18, 0x1, 0x2, 0x0, 0x3E8, 0x0, 0x0)
    OP_76(0xFF, 0x24, 0x1, 0x2, 0x0, 0x3E8, 0x0, 0x0)
    OP_76(0xFF, 0x33, 0x1, 0x2, 0x0, 0x3E8, 0x0, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004FHoly...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "There we are.\x02",
    )

    CloseMessageWindow()

    def lambda_269F():
        OP_6D(-105100, -4000, -108200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_269F)

    def lambda_26B7():
        OP_8E(0xFE, 0xFFFE5A84, 0xFFFFF060, 0xFFFE4D3C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_26B7)
    Sleep(800)

    def lambda_26D7():
        OP_8E(0xFE, 0xFFFE53E0, 0xFFFFF060, 0xFFFE4E04, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26D7)
    Sleep(500)

    def lambda_26F7():
        OP_8E(0xFE, 0xFFFE4F94, 0xFFFFF060, 0xFFFE4D3C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_26F7)
    WaitChrThread(0xE, 0x1)

    def lambda_2717():

        label("loc_2717")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2717")

    QueueWorkItem2(0xE, 1, lambda_2717)
    WaitChrThread(0x101, 0x1)

    def lambda_272D():

        label("loc_272D")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_272D")

    QueueWorkItem2(0x101, 1, lambda_272D)
    WaitChrThread(0x102, 0x1)

    def lambda_2743():

        label("loc_2743")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2743")

    QueueWorkItem2(0x102, 1, lambda_2743)

    def lambda_2754():
        OP_6D(-108840, -4000, -109520, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2754)
    WaitChrThread(0x14, 0x1)
    OP_75(0xFF, 0xF, 0x5)
    OP_75(0xFF, 0x18, 0x5)
    OP_75(0xFF, 0x24, 0x5)
    OP_75(0xFF, 0x33, 0x5)
    OP_23(0x5B)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        "#501FIs THIS gasoline?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FSo that's what 'sending' is.\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xE, 0xFF)
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(
        0xE,
        "#2PNeat, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2PThis conveyor belt system isn't\x01",
            "just for ordering goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2PIt's an entire network that\x01",
            "connects the whole facility.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xE, 400)
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(
        0x101,
        "#004F#5PConvenient.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2PProfessor Russell invented it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2POriginally it was just a series\x01",
            "of tubes for sending products\x01",
            "back and forth...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2PBut the professor completely\x01",
            "rebuilt the system into \x01",
            "something a lot more useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2POf course, getting all of the\x01",
            "infrastructure in place was\x01",
            "a gigantic pain in the...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#5PHa ha.\x01",
            "I can only imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe have to be on our way.\x01",
            "Thank you for your help.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(
        0xE,
        "#2PNo problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2PI don't know what you're using\x01",
            "it for, but be careful with that\x01",
            "gasoline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2PIt has a tendency to...fireball.\x02",
    )

    CloseMessageWindow()
    OP_65(0x0, 0x1)
    EventEnd(0x0)
    OP_43(0xE, 0x0, 0x0, 0x2)
    Jump("loc_3781")

    label("loc_2AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2B53")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Thanks for the delivery!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I really appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I need to get back to work...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_2B53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B7D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x35E)"), scpexpr(EXPR_END)), "loc_2B7D")
    Call(1, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_2B7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2CA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2BE1")

    ChrTalk(
        0xFE,
        (
            "But still, I can't believe the\x01",
            "army was behind it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I was shocked!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2BE1")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "Hey...it's you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks again for saving the\x01",
            "professor like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know it's not over yet,\x01",
            "but at least he's safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't forget you've got friends\x01",
            "here if you need us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA5")

    Jump("loc_3781")

    label("loc_2CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2E24")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D3F")

    ChrTalk(
        0xFE,
        (
            "*sigh* Rudi... I can't stop\x01",
            "thinking about him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just sent a letter to Brahm, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have the worst timing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E21")

    label("loc_2D3F")


    ChrTalk(
        0xFE,
        (
            "*sigh* Rudi... I can't stop\x01",
            "thinking about him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it about him? It's not like\x01",
            "he's very smart, or handsome,\x01",
            "or dependable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But at the same time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must have a nurturer's personality\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E21")

    Jump("loc_2EFB")

    label("loc_2E24")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "This is really bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have not been able to stop \x01",
            "thinking about Rudi lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not that I like him or anything.\x01",
            "It's just that he...needs me to\x01",
            "take care of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't work like this!\x02",
    )

    CloseMessageWindow()

    label("loc_2EFB")

    Jump("loc_3781")

    label("loc_2EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3036")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F78")

    ChrTalk(
        0xFE,
        "*sigh* \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Rudi... Brahm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why is it that I always end up\x01",
            "around these kind of guys?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3033")

    label("loc_2F78")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "I just had to sit Rudi down and\x01",
            "chew him out, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He gets so preoccupied with\x01",
            "himself that he can't do his\x01",
            "job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's kind of sad, really. I had\x01",
            "to tell him to grow up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3033")

    Jump("loc_3781")

    label("loc_3036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_31CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_311B")

    ChrTalk(
        0xFE,
        (
            "We were working and suddenly\x01",
            "smoke just poured in. We bolted\x01",
            "to the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But Rudi...like an idiot, inhaled\x01",
            "a lung-full of the stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're going to the clinic,\x01",
            "just to be on the safe side.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31CA")

    label("loc_311B")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "We were working and suddenly\x01",
            "smoke just poured in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We bolted out the door and\x01",
            "down to the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just know those guys snuck\x01",
            "in from the underground.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31CA")

    Jump("loc_3781")

    label("loc_31CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3330")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3292")

    ChrTalk(
        0xFE,
        (
            "I've got to forget about that\x01",
            "letter and focus on my work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I don't I'll be setting a bad\x01",
            "example for Brahm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Rudi. I'll be setting a bad\x01",
            "example for Rudi.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_332D")

    label("loc_3292")


    ChrTalk(
        0xFE,
        (
            "I just had to give Rudi a scolding\x01",
            "something fierce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That boy just spaces out and\x01",
            "completely forgets his work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He didn't used to be so bad.\x02",
    )

    CloseMessageWindow()

    label("loc_332D")

    Jump("loc_3781")

    label("loc_3330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_344A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_END)), "loc_33B8")

    ChrTalk(
        0xFE,
        (
            "I don't know what you're using\x01",
            "it for, but be careful around\x01",
            "that gasoline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It has a tendency to...fireball.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3447")

    label("loc_33B8")

    OP_62(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0xE)

    ChrTalk(
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come on, Faye.\x01",
            "Time to work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The conveyor's in order. Let's take\x01",
            "a look at the warehouse next.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3447")

    Jump("loc_3781")

    label("loc_344A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3521")

    ChrTalk(
        0xFE,
        (
            "I'd like you to start by checking the conveyor\x01",
            "to make sure there aren't any problems as a\x01",
            "result of yesterday's little...incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When that's done, run a safety\x01",
            "check on the outside machines. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3781")

    label("loc_3521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3697")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_35D1")

    ChrTalk(
        0xFE,
        "What did I see in that guy?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's not good-looking, with that\x01",
            "half-asleep expression on his\x01",
            "face all the time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just don't get it sometimes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3694")

    label("loc_35D1")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "I am pathetic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What did I see in that guy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's not good-looking, with that\x01",
            "half-asleep expression on his\x01",
            "face all the time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He didn't have any real\x01",
            "redeeming qualities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3694")

    Jump("loc_3781")

    label("loc_3697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3781")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_36FE")

    ChrTalk(
        0xFE,
        "But, enough! Work. WORK!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should be able to forget all\x01",
            "about that loser...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3781")

    label("loc_36FE")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what he's doing\x01",
            "right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Okay, enough of that. Get\x01",
            "your head into the job, girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3781")

    TalkEnd(0xFE)
    Return()

    # Function_9_22BA end

    def Function_10_3785(): pass

    label("Function_10_3785")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_381B")

    ChrTalk(
        0xFE,
        (
            "After getting back from the\x01",
            "factory ship, Faye just hasn't\x01",
            "been herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did something happen with her\x01",
            "ex-boyfriend, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAB")

    label("loc_381B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_38AA")

    ChrTalk(
        0xFE,
        (
            "Someone called for Faye and\x01",
            "she went off somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was some kind of emergency\x01",
            "call for the factory ship, I think...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAB")

    label("loc_38AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_39C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3938")

    ChrTalk(
        0xFE,
        (
            "It might just be me, but I think\x01",
            "I saw Faye looking at me from\x01",
            "the corner of my eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's probably my imagination.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39C5")

    label("loc_3938")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "It might just be me, but I think\x01",
            "I saw Faye looking at me from\x01",
            "the corner of my eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe she...likes me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Yeah, right.\x02",
    )

    CloseMessageWindow()

    label("loc_39C5")

    Jump("loc_3EAB")

    label("loc_39C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3A56")

    ChrTalk(
        0xFE,
        (
            "I get yelled at by Faye, then all\x01",
            "this orbment craziness happened...\x01",
            "I don't want to do any work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just want to go home.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EAB")

    label("loc_3A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3BD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3B0E")

    ChrTalk(
        0xFE,
        (
            "Man, Faye chewed me out\x01",
            "so bad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet she thinks I'm\x01",
            "totally worthless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She just broke up with that guy,\x01",
            "too. My one chance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...and I blew it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BCE")

    label("loc_3B0E")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "Good job, loser.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, Faye chewed me out\x01",
            "so bad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet she thinks I'm\x01",
            "totally worthless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She just broke up with that guy,\x01",
            "too. My one chance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...and I blew it.\x02",
    )

    CloseMessageWindow()

    label("loc_3BCE")

    Jump("loc_3EAB")

    label("loc_3BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_3CF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3C70")

    ChrTalk(
        0xFE,
        (
            "I know I've got to impress her\x01",
            "with my hard work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I can't stop thinking about\x01",
            "Faye and her ex, and I just\x01",
            "can't keep working.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CF3")

    label("loc_3C70")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "What kind of guy is he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I tried asking her friends,\x01",
            "but they didn't tell me much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Gah! I just can't concentrate!\x02",
    )

    CloseMessageWindow()

    label("loc_3CF3")

    Jump("loc_3EAB")

    label("loc_3CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3D35")

    ChrTalk(
        0xFE,
        "Roger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll start with the conveyor, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EAB")

    label("loc_3D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3E3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3DB5")

    ChrTalk(
        0xFE,
        (
            "I actually don't know what kind\x01",
            "of guy Faye likes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wonder if her ex was\x01",
            "someone in the factory?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3B")

    label("loc_3DB5")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "I heard a rumor that Faye just\x01",
            "broke up with her boyfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now's my chance!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll wow her with my mad\x01",
            "work skills. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E3B")

    Jump("loc_3EAB")

    label("loc_3E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3EAB")

    ChrTalk(
        0xFE,
        "...Okay, that makes eight cans.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Check and double check!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's check in on the factory.\x02",
    )

    CloseMessageWindow()

    label("loc_3EAB")

    TalkEnd(0xFE)
    Return()

    # Function_10_3785 end

    def Function_11_3EAF(): pass

    label("Function_11_3EAF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_3F50")

    ChrTalk(
        0x8,
        (
            "Maintenance Chief Gustav?\x01",
            "Yes, he's still here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But he was in quite a hurry and\x01",
            "ran off to the boarding area.\x01",
            "I hope everything's okay...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5676")

    label("loc_3F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4003")

    ChrTalk(
        0x8,
        (
            "Everyone, congratulations on a\x01",
            "successful rescue operation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I wish I could thank you more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...I think I've said enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please be careful, everyone.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5676")

    label("loc_4003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4146")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4053")

    ChrTalk(
        0x8,
        "Please...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Make sure the professor comes\x01",
            "back safely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4143")

    label("loc_4053")

    OP_A2(0x4)

    ChrTalk(
        0x8,
        "Please...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Make sure the professor comes\x01",
            "back safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Tita, you take extra care, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560FThank you. I will.\x02\x03",
            "#061FAgate here has taught me all\x01",
            "about the dangers of trying to\x01",
            "overextend my capabilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#052F...\x02",
    )

    CloseMessageWindow()

    label("loc_4143")

    Jump("loc_5676")

    label("loc_4146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_41E8")

    ChrTalk(
        0x8,
        "Good morning, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I believe Tita's in the clinic on\x01",
            "the fourth floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems she was very anxious\x01",
            "to see if Agate was all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5676")

    label("loc_41E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4246")

    ChrTalk(
        0x8,
        "That was a bracer, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He was awfully pale...\x01",
            "I hope he was all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5676")

    label("loc_4246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_END)), "loc_42FA")

    ChrTalk(
        0x8,
        (
            "By order of the factory chief, we've \x01",
            "kept news about the professor a secret\x01",
            "from all but a select number of people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Make sure the professor comes\x01",
            "back safely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5676")

    label("loc_42FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_449D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_43B4")

    ChrTalk(
        0x8,
        (
            "By order of the factory chief, we've \x01",
            "kept news about the professor a secret\x01",
            "from all but a select number of people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please try to keep up your\x01",
            "spirits, Tita.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_449A")

    label("loc_43B4")

    OP_A2(0x4)

    ChrTalk(
        0x8,
        "Everyone...Tita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By order of the factory chief, we've \x01",
            "kept news about the professor a secret\x01",
            "from all but a select number of people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please try to keep up your\x01",
            "spirits, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F...\x02\x03",
            "Thank you. I will.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_449A")

    Jump("loc_5676")

    label("loc_449D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_46E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 1)), scpexpr(EXPR_END)), "loc_4514")

    ChrTalk(
        0x8,
        (
            "I've already contacted the\x01",
            "Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please see to it that Tita\x01",
            "arrives safely in Elmo.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46E4")

    label("loc_4514")

    OP_A2(0x581)

    ChrTalk(
        0x8,
        "Hello, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard about what happened at the\x01",
            "inn in Elmo from the factory chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You're going to Elmo,\x01",
            "I hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060FThat's right.\x02\x03",
            "I've helped there before,\x01",
            "so it makes sense that I go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe also have a responsibility to\x01",
            "protect you on your trip.\x02\x03",
            "We will see you there safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've already contacted the\x01",
            "Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please see to it that Tita\x01",
            "arrives safely in Elmo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FNo worries.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060FShall we go then?\x02",
    )

    CloseMessageWindow()

    label("loc_46E4")

    Jump("loc_5676")

    label("loc_46E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4757")

    ChrTalk(
        0x8,
        "That baggage looks so heavy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bracers certainly have to keep\x01",
            "themselves in shape.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47CC")

    label("loc_4757")

    OP_A2(0x4)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "That baggage looks so heavy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bracers certainly have to keep\x01",
            "themselves in shape.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47CC")

    Jump("loc_5676")

    label("loc_47CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4973")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_END)), "loc_48DB")

    ChrTalk(
        0x101,
        (
            "#505FWe've got the gasoline, so now\x01",
            "we need to see Maintenance\x01",
            "Chief Gustav...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The maintenance chief is probably\x01",
            "at the airship boarding platform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He only comes back to the factory if\x01",
            "there's some kind of official business\x01",
            "for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4970")

    label("loc_48DB")


    ChrTalk(
        0x101,
        (
            "#505FWe have the Combustion Engine.\x01",
            "Now we need to go to the orbment\x01",
            "production facility...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Take the elevator down to \x01",
            "basement level one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4970")

    Jump("loc_5676")

    label("loc_4973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_END)), "loc_4B88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4A06")

    ChrTalk(
        0x8,
        (
            "Take the elevator down to \x01",
            "basement level one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The maintenance chief will probably\x01",
            "be at the airship boarding platform.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B85")

    label("loc_4A06")

    OP_A2(0x4)

    ChrTalk(
        0x8,
        (
            "Hello, everyone. Is there anything\x01",
            "I can help you with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FWe need to go to the orbment\x01",
            "production facility and talk to\x01",
            "Maintenance Chief Gustav...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Take the elevator down to \x01",
            "basement level one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The maintenance chief will\x01",
            "probably be at the airship\x01",
            "boarding platform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He only comes back to the factory if\x01",
            "there's some kind of official business\x01",
            "for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B85")

    Jump("loc_5676")

    label("loc_4B88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_4E4A")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C79")

    ChrTalk(
        0x8,
        (
            "Hello, everyone. Is there anything\x01",
            "I can help you with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FWe need to go to...Operations?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Operations is up on the fifth floor.\x01",
            "Take the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you need anything else,\x01",
            "don't be afraid to ask me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E47")

    label("loc_4C79")


    ChrTalk(
        0x8,
        (
            "Hello, everyone. Is there anything\x01",
            "I can help you with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "[Maintenance Chief Gustav]\x01",
            "[Orbment Production Facility]\x01",
            "[Never mind]\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maintenance Chief Gustav is\x01",
            "usually at the airship boarding\x01",
            "platform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The boarding platform is just\x01",
            "to the east of the square in\x01",
            "front of the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Anything else?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The production facility is\x01",
            "underground. Please use\x01",
            "the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Anything else?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there's anything else,\x01",
            "please come and ask me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E47")

    Jump("loc_5676")

    label("loc_4E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_4FA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4EE8")

    ChrTalk(
        0x8,
        (
            "Professor Russell is in his \x01",
            "workshop on the third floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He seemed pretty impatient,\x01",
            "like he was waiting on something\x01",
            "or someone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FA0")

    label("loc_4EE8")

    OP_A2(0x4)
    OP_28(0x3F, 0x1, 0x40)

    ChrTalk(
        0x8,
        (
            "Tita! Everyone!\x01",
            "How are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Professor Russell is in his \x01",
            "workshop on the third floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He seemed pretty impatient,\x01",
            "like he was waiting on something\x01",
            "or someone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FA0")

    Jump("loc_5676")

    label("loc_4FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_50BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4FEB")
    TurnDirection(0x8, 0x107, 0)

    ChrTalk(
        0x8,
        (
            "Bye, Tita! Good luck with\x01",
            "the guided tour!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50BA")

    label("loc_4FEB")

    OP_A2(0x4)
    TurnDirection(0x8, 0x107, 0)

    ChrTalk(
        0x8,
        (
            "Hello, Tita! Where are you\x01",
            "off to today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560FI'm going to show these two\x01",
            "where I live.\x02\x03",
            "They have something to discuss\x01",
            "with Grandpa, it would seem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061FBye, Hazel!\x02",
    )

    CloseMessageWindow()

    label("loc_50BA")

    Jump("loc_5676")

    label("loc_50BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_55A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5544")
    OP_A2(0x50D)
    OP_28(0x3F, 0x1, 0x2)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(220, 0, 5230, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 440, 0, 3680, 0)
    SetChrPos(0x102, -560, 0, 3680, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Oh, you were the ones with Tita\x01",
            "before, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Welcome to the Central Factory.\x01",
            "Can I help you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FWe...are from the Bracer Guild!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe'd like to meet with the\x01",
            "factory head, if we may.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Estelle reached into her pouch, paused for dramatic effect,\x01",
            "then flourished the introduction note to meet the factory\x01",
            "chief. Joshua looked stoic and tried not to roll his eyes.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x360, 1)

    ChrTalk(
        0x8,
        (
            "I-I...see.\x01",
            "Just a moment, please.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 315, 400)
    OP_8E(0x8, 0xFFFFFC54, 0x0, 0x1D4C, 0x7D0, 0x0)
    OP_8C(0x8, 0, 400)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hazel used the intercom, keeping one wary eye on Estelle all the while.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "Sir? I'm terribly sorry to bother\x01",
            "you during your...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes... Yes, sir. The people from\x01",
            "the Bracer Guild are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, sir. Right away.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 135, 400)
    OP_8E(0x8, 0x104, 0x0, 0x16A8, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x8,
        "Thank you for waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Factory Chief Murdock will\x01",
            "see you now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "His office is upstairs on the\x01",
            "second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FNice. I didn't think he'd see\x01",
            "us so quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FLet's not keep him waiting.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_55A3")

    label("loc_5544")


    ChrTalk(
        0x8,
        (
            "The factory chief's office is on\x01",
            "the second floor. You can take\x01",
            "the elevator on the left.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55A3")

    Jump("loc_5676")

    label("loc_55A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5676")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5617")

    ChrTalk(
        0x8,
        (
            "Welcome to the Zeiss\x01",
            "Central Factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have any questions,\x01",
            "please let me know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5676")

    label("loc_5617")


    ChrTalk(
        0x8,
        (
            "The factory chief's office is on\x01",
            "the second floor. You can take\x01",
            "the elevator on the left.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5676")

    TalkEnd(0x8)
    Return()

    # Function_11_3EAF end

    def Function_12_567A(): pass

    label("Function_12_567A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_56D4")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm being transferred?! \x01",
            "TO THE ORBAL ENGINE PROJECT?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "M-Me?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_56D4")

    Return()

    # Function_12_567A end

    def Function_13_56D5(): pass

    label("Function_13_56D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_5836")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57CF")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "I'm sorry to be calling you\x01",
            "up so soon after the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've received a message that\x01",
            "needs your attention at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't beat around the bush.\x01",
            "They want you on the project\x01",
            "for the Arseille's new engine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5830")

    label("loc_57CF")


    ChrTalk(
        0xFE,
        "The first assistant just quit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But...this is your big chance,\x01",
            "so you'd better produce.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5830")

    TalkEnd(0xFE)
    Jump("loc_601A")

    label("loc_5836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_601A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C6C")
    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Talk\x01",                          # 0
            "Ask about the cigarettes\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58BB")
    Call(1, 0)
    Return()

    label("loc_58BB")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_END)), "loc_59CA")

    ChrTalk(
        0xB,
        (
            "This resignation business is a\x01",
            "serious problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We NEED to get the project\x01",
            "moving ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There's nothing we can do about\x01",
            "getting him back now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We should look at it as...\x01",
            "an opportunity for a fresh\x01",
            "perspective on the project.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C59")

    label("loc_59CA")

    OP_A2(0x575)

    ChrTalk(
        0xB,
        "What?! Are you serious?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "One of the researchers on the\x01",
            "Orbal Engine Project quit?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes. We thought we had talked\x01",
            "him into reconsidering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But apparently there were...\x01",
            "circumstances. His official\x01",
            "resignation notice came today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I see...this is a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This whole project was to\x01",
            "be for the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If we can't get this started,\x01",
            "our hopes of actually USING\x01",
            "the Arseille are finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I know, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We can't keep the old-model\x01",
            "engine in the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And I understand how quickly\x01",
            "we need to find a replacement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But we should look at it as a \x01",
            "chance to get a fresh point\x01",
            "of view on the project.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C59")

    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_601A")

    label("loc_5C6C")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_END)), "loc_5D7B")

    ChrTalk(
        0xB,
        (
            "This resignation business is a\x01",
            "serious problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We NEED to get the project\x01",
            "moving ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There's nothing we can do about\x01",
            "getting him back now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We should look at it as...\x01",
            "an opportunity for a fresh\x01",
            "perspective on the project.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_600A")

    label("loc_5D7B")

    OP_A2(0x575)

    ChrTalk(
        0xB,
        "What?! Are you serious?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "One of the researchers on the\x01",
            "Orbal Engine Project quit?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes. We thought we had talked\x01",
            "him into reconsidering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But apparently there were...\x01",
            "circumstances. His official\x01",
            "resignation notice came today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I see...this is a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This whole project was to\x01",
            "be for the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If we can't get this started,\x01",
            "our hopes of actually USING\x01",
            "the Arseille are finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I know, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We can't keep the old-model\x01",
            "engine in the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And I understand how quickly\x01",
            "we need to find a replacement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But we should look at it as a \x01",
            "chance to get a fresh point\x01",
            "of view on the project.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_600A")

    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_601A")

    Return()

    # Function_13_56D5 end

    def Function_14_601B(): pass

    label("Function_14_601B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_63D0")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_END)), "loc_6131")

    ChrTalk(
        0xB,
        (
            "This resignation business is a\x01",
            "serious problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We NEED to get the project\x01",
            "moving ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There's nothing we can do about\x01",
            "getting him back now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We should look at it as...\x01",
            "an opportunity for a fresh\x01",
            "perspective on the project.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C0")

    label("loc_6131")

    OP_A2(0x575)

    ChrTalk(
        0xB,
        "What?! Are you serious?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "One of the researchers on the\x01",
            "Orbal Engine Project quit?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes. We thought we had talked\x01",
            "him into reconsidering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But apparently there were...\x01",
            "circumstances. His official\x01",
            "resignation notice came today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I see...this is a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This whole project was to\x01",
            "be for the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If we can't get this started,\x01",
            "our hopes of actually USING\x01",
            "the Arseille are finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I know, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We can't keep the old-model\x01",
            "engine in the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And I understand how quickly\x01",
            "we need to find a replacement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But we should look at it as a \x01",
            "chance to get a fresh point\x01",
            "of view on the project.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63C0")

    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_63D0")

    Return()

    # Function_14_601B end

    def Function_15_63D1(): pass

    label("Function_15_63D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_650E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_644B")

    ChrTalk(
        0xFE,
        (
            "Are there really this many different\x01",
            "kinds of orbments just for heating?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm so confused...\x02",
    )

    CloseMessageWindow()
    Jump("loc_650E")

    label("loc_644B")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "I'm so confused...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All I did was ask for a heating\x01",
            "orbment and they hand me\x01",
            "this telephone book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All these different models...\x01",
            "I don't have a clue where I\x01",
            "should start looking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_650E")

    TalkEnd(0xFE)
    Return()

    # Function_15_63D1 end

    def Function_16_6512(): pass

    label("Function_16_6512")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6575")

    ChrTalk(
        0x102,
        (
            "#010FThis way leads outside...\x02\x03",
            "We'll have to send Antoine\x01",
            "home if we leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65CA")

    label("loc_6575")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#014FDo you want to go outside?\x02\x03",
            "If so, we'll have to send\x01",
            "Antoine home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65ED")

    def lambda_65E5():
        TurnDirection(0x0, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_65E5)

    label("loc_65ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6610")

    def lambda_6608():
        TurnDirection(0x1, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6608)

    label("loc_6610")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6633")

    def lambda_662B():
        TurnDirection(0x2, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_662B)

    label("loc_6633")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6656")

    def lambda_664E():
        TurnDirection(0x3, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_664E)

    label("loc_6656")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6679")

    def lambda_6671():
        TurnDirection(0x4, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_6671)

    label("loc_6679")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Leave]\x01",       # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66EA")
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    label("loc_66EA")


    ChrTalk(
        0x102,
        (
            "#010FWell, Antoine... I guess\x01",
            "this is goodbye, for now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13C, 0x102, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x13C,
        "Nya乣on.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3B, 0xFF)
    NewScene("ED6_DT01/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x2)
    Return()

    # Function_16_6512 end

    def Function_17_675B(): pass

    label("Function_17_675B")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67BE")

    ChrTalk(
        0x102,
        (
            "#010FThis way leads outside...\x02\x03",
            "We'll have to send Antoine\x01",
            "home if we leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6813")

    label("loc_67BE")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#014FDo you want to go outside?\x02\x03",
            "If so, we'll have to\x01",
            "send Antoine home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6813")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6836")

    def lambda_682E():
        TurnDirection(0x0, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_682E)

    label("loc_6836")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6859")

    def lambda_6851():
        TurnDirection(0x1, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6851)

    label("loc_6859")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_687C")

    def lambda_6874():
        TurnDirection(0x2, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_6874)

    label("loc_687C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_689F")

    def lambda_6897():
        TurnDirection(0x3, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_6897)

    label("loc_689F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68C2")

    def lambda_68BA():
        TurnDirection(0x4, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_68BA)

    label("loc_68C2")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Leave]\x01",       # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6933")
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    label("loc_6933")


    ChrTalk(
        0x102,
        (
            "#010FWell, Antoine... I guess\x01",
            "this is goodbye, for now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13C, 0x102, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x13C,
        "Nya乣on.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3B, 0xFF)
    NewScene("ED6_DT01/R3403   ._SN", 101, 0, 0)
    IdleLoop()
    EventEnd(0x2)
    Return()

    # Function_17_675B end

    def Function_18_69A4(): pass

    label("Function_18_69A4")

    Call(0, 11)
    Return()

    # Function_18_69A4 end

    def Function_19_69A9(): pass

    label("Function_19_69A9")

    Call(0, 8)
    Return()

    # Function_19_69A9 end

    def Function_20_69AE(): pass

    label("Function_20_69AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A6F")
    TurnDirection(0x107, 0x1, 400)

    ChrTalk(
        0x107,
        (
            "#560FOh, there's only an emergency\x01",
            "staircase through that door.\x02\x03",
            "If you want to go up to the ground\x01",
            "floor, just go back the way you came \x01",
            "and straight down the hall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B21")

    label("loc_6A6F")

    TurnDirection(0x107, 0x0, 400)

    ChrTalk(
        0x107,
        (
            "#560FOh, there's only an emergency\x01",
            "staircase through that door.\x02\x03",
            "If you want to go up to the ground\x01",
            "floor, just go back the way you came \x01",
            "and straight down the hall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B21")

    TalkEnd(0xFF)
    Return()

    # Function_20_69AE end

    def Function_21_6B25(): pass

    label("Function_21_6B25")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, -109900, 0, -101300, 180)
    SetChrPos(0x102, -110700, 0, -100900, 180)
    SetChrPos(0x107, -109300, 0, -100900, 180)

    ChrTalk(
        0x101,
        "#004FWhoa... What's this place?\x02",
    )

    CloseMessageWindow()

    def lambda_6B8A():
        OP_8E(0xFE, 0xFFFE4F30, 0x0, 0xFFFE65D8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B8A)

    def lambda_6BA5():
        OP_8E(0xFE, 0xFFFE4A80, 0x0, 0xFFFE66A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BA5)

    def lambda_6BC0():
        OP_8E(0xFE, 0xFFFE52B4, 0x0, 0xFFFE6510, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_6BC0)
    OP_6D(-110500, 0, -107800, 2000)

    ChrTalk(
        0x102,
        (
            "#014FWow... It looks like almost the\x01",
            "entire factory is completely\x01",
            "automated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061FHee hee... Below the city there\x01",
            "are lots of orbment factories.\x02\x03",
            "They make everything from\x01",
            "lights to airship parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FThat's awesome... A little\x01",
            "overwhelming, but awesome.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_21_6B25 end

    def Function_22_6CF8(): pass

    label("Function_22_6CF8")

    EventBegin(0x0)
    OP_22(0xE, 0x0, 0x64)
    OP_6D(3680, 0, -4580, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -4700, 0, 9200, 180)
    SetChrPos(0x102, -4700, 0, 9200, 180)
    SetChrPos(0x107, -4700, 0, 9200, 180)
    FadeToBright(1000, 0)

    def lambda_6D7E():
        OP_6D(-4950, 0, 6440, 4000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_6D7E)

    def lambda_6D96():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_6D96)
    WaitChrThread(0x107, 0x2)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    Sleep(500)

    def lambda_6DBA():
        OP_8E(0xFE, 0xFFFFECDC, 0x0, 0x1130, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DBA)
    Sleep(500)
    OP_8E(0x107, 0xFFFFEC78, 0x0, 0x1DB0, 0xBB8, 0x0)

    def lambda_6DEE():
        OP_8E(0xFE, 0xFFFFF060, 0x0, 0x170C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_6DEE)
    Sleep(200)

    def lambda_6E0E():
        OP_8E(0xFE, 0xFFFFE8F4, 0x0, 0x157C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E0E)
    Sleep(1000)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#501FWhoa... Check out the\x01",
            "size of this place!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#060FThis is the Central Factory's\x01",
            "main floor.\x02\x03",
            "It's where the reception desk\x01",
            "and consumer maintenance\x01",
            "windows are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI see. So we can get out\x01",
            "to town from here.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 270, 400)

    ChrTalk(
        0x8,
        "Oh, Tita!\x02",
    )

    CloseMessageWindow()

    def lambda_6F5C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F5C)

    def lambda_6F6A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_6F6A)

    def lambda_6F78():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F78)
    OP_6D(-1900, 0, 7200, 1500)

    ChrTalk(
        0x107,
        "#064FMiss Hazel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "There you are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Supervisor Travis has been\x01",
            "looking for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He'd like for you to go straight\x01",
            "to the Operations room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560FOh... Okay, I will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FUh-oh...\x01",
            "Sounds urgent.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7070():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7070)

    def lambda_707E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_707E)

    def lambda_708C():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_708C)

    def lambda_709A():
        OP_6D(-4950, 0, 6440, 1500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_709A)
    OP_8C(0x8, 180, 400)
    OP_4B(0x8, 255)
    WaitChrThread(0x107, 0x2)

    ChrTalk(
        0x102,
        (
            "#010FThank you for showing\x01",
            "us around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560FI-It's no big deal.\x02\x03",
            "It's the least I can do\x01",
            "after you beat up those\x01",
            "monsters for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#4PWell, we're planning to be\x01",
            "in Zeiss for a little while.\x02\x03",
            "Would you mind if we stopped\x01",
            "by to see you again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064FI...\x02\x03",
            "#067FI'd love that!\x02\x03",
            "Bye-bye, then!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_71F9():

        label("loc_71F9")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_71F9")

    QueueWorkItem2(0x101, 1, lambda_71F9)

    def lambda_720A():

        label("loc_720A")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_720A")

    QueueWorkItem2(0x102, 1, lambda_720A)
    OP_8E(0x107, 0xFFFFEC78, 0x0, 0x1DB0, 0xBB8, 0x0)
    OP_8C(0x107, 0, 400)
    Sleep(500)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_8E(0x107, 0xFFFFEDA4, 0x0, 0x23F0, 0xBB8, 0x0)
    Sleep(500)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x102,
        (
            "#019F#1PHa ha... What a sweet kid. I get\x01",
            "the impression that she's a lot\x01",
            "tougher than she looks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FI agree.\x02\x03",
            "#507F*sigh* I always wanted a\x01",
            "sweet, lovable little sister\x01",
            "like her.\x02\x03",
            "INSTEAD OF, might I add, an\x01",
            "obnoxious little brother.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F#1PYou keep saying things like\x01",
            "that, but you're the one who's \x01",
            "always following ME around.\x02\x03",
            "If you want to be more like a real older\x01",
            "sister, you need to get your head out of\x01",
            "the clouds every now and then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#509F*Pffffft* Look who's talking.\x02\x03",
            "#000FAnyway, all sibling rivalries aside...\x01",
            "Want to head into the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1PYeah... First, I'd like to switch\x01",
            "assignments at the guild.\x02\x03",
            "Plus, we can see if there's\x01",
            "any new information on the\x01",
            "orbment or Dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FSounds like a plan.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x107, -4900, 0, 4400, 0)
    SetChrFlags(0x107, 0x80)
    ClearMapFlags(0x10000000)
    EventEnd(0x0)
    RemoveParty(0x6, 0xFF)
    Return()

    # Function_22_6CF8 end

    def Function_23_7596(): pass

    label("Function_23_7596")

    OP_A2(0x540)
    OP_A3(0x541)
    OP_A3(0x542)
    OP_A3(0x543)
    OP_A3(0x544)
    OP_A3(0x545)
    OP_A3(0x546)
    Return()

    # Function_23_7596 end

    def Function_24_75AC(): pass

    label("Function_24_75AC")

    OP_A3(0x540)
    OP_A2(0x541)
    OP_A3(0x542)
    OP_A3(0x543)
    OP_A3(0x544)
    OP_A3(0x545)
    OP_A3(0x546)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_7768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7768")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-5490, 0, 5460, 0)
    SetChrPos(0x101, -5140, 0, 5030, 0)
    SetChrPos(0x102, -5030, 0, 3560, 0)
    SetChrPos(0x107, -6390, 0, 5230, 0)
    SetChrPos(0x106, -6860, 0, 3810, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#004FLook! It's open!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065FSo they DID come down here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F...which means they probably left\x01",
            "through the main entrance.\x02\x03",
            "But with all those people out\x01",
            "there? How do they intend to\x01",
            "get away unseen?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#054FWe'll worry about that later.\x01",
            "Come on! We've gotta catch up\x01",
            "to them!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x535)
    EventEnd(0x0)
    Jump("loc_7768")

    label("loc_7768")

    Return()

    # Function_24_75AC end

    def Function_25_7769(): pass

    label("Function_25_7769")

    OP_A2(0x519)
    OP_28(0x3F, 0x1, 0x1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3F, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_7783")
    OP_28(0x3F, 0x1, 0x2000)

    label("loc_7783")

    OP_71(0x8, 0x4)
    OP_64(0x0, 0x1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained \x07\x02",
            "Gasoline Tank\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x367, 1)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_7769 end

    def Function_26_77E2(): pass

    label("Function_26_77E2")

    EventBegin(0x0)
    OP_6D(-140, 0, 7500, 0)
    SetChrPos(0x101, -80, 0, -7570, 0)
    SetChrPos(0x102, -990, 0, -8530, 0)
    SetChrPos(0x107, 370, 0, -8440, 0)
    FadeToBright(1000, 0)
    OP_6D(100, 0, -6040, 4000)

    ChrTalk(
        0x101,
        (
            "#002F#1PUgh...\x01",
            "So much smoke...\x02\x03",
            "#505FHuh... Not so bad that you\x01",
            "can't breathe, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#1PThis haze is...probably a smokescreen\x01",
            "for something else, I think.\x02\x03",
            "There must be a smoke canister\x01",
            "nearby...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F#1PHuh...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x107,
        (
            "#065FBut why would something\x01",
            "like that even...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x107, 400)

    ChrTalk(
        0x102,
        (
            "#012F#1PI can't speculate on why...\x02\x03",
            "...but if we can put out that\x01",
            "canister, the smoke should\x01",
            "clear up quickly enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#1PGot it. Find it and put it out.\x02\x03",
            "Professor Russell is in the\x01",
            "third floor workshop, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063FY-Yes... At least, I think so.\x02\x03",
            "Grandpa sometimes gets so wrapped up\x01",
            "in his research that he loses sight\x01",
            "of what's going on around him.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#012F#1PWell, let's get to the third floor.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_26_77E2 end

    def Function_27_7B27(): pass

    label("Function_27_7B27")

    Return()

    # Function_27_7B27 end

    def Function_28_7B28(): pass

    label("Function_28_7B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E2B")
    EventBegin(0x0)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_6D(-4900, 0, 8380, 1000)
    OP_A2(0x52E)
    OP_28(0x41, 0x1, 0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BCA")

    ChrTalk(
        0x101,
        (
            "#004FHuh... The automatic door\x01",
            "isn't opening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FDid the orbal power shut off?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CD9")

    label("loc_7BCA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C3D")

    ChrTalk(
        0x102,
        (
            "#013FStrange... The automatic door\x01",
            "isn't opening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FHuh? Did the orbal power\x01",
            "shut off?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CD9")

    label("loc_7C3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CD9")
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tita pressed the button.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x107,
        (
            "#065FWeird. The automatic door\x01",
            "won't open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FHuh? Did the orbal power\x01",
            "shut off?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CD9")


    ChrTalk(
        0x107,
        (
            "#063FNo...\x01",
            "It looks like it's operational.\x02\x03",
            "Someone's probably using\x01",
            "the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FCould that 'someone' possibly\x01",
            "be Professor Russell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FLet's hope not, since it doesn't\x01",
            "seem to be going anywhere.\x02\x03",
            "Either way, the only way we're\x01",
            "getting upstairs is via that\x01",
            "emergency stairway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063FYeah... You're right.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_7EA9")

    label("loc_7E2B")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pressing the button does nothing. The elevator cannot be used at the moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_7EA9")

    Return()

    # Function_28_7B28 end

    def Function_29_7EAA(): pass

    label("Function_29_7EAA")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pressing the button does nothing. The elevator cannot be used at the moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_29_7EAA end

    def Function_30_7F32(): pass

    label("Function_30_7F32")

    EventBegin(0x0)
    OP_A2(0x547)
    OP_64(0x1, 0x1)
    OP_2B(0x41, 0x1)
    OP_6D(-9770, 0, -3590, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_839F")
    OP_A2(0x52F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FE3")

    ChrTalk(
        0x101,
        (
            "#004FHey...\x01",
            "Joshua, that's...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FLooks like a smoke canister...\x01",
            "Like that one the Sky Bandits\x01",
            "used before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8157")

    label("loc_7FE3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8073")

    ChrTalk(
        0x101,
        (
            "#004FHey...\x01",
            "Joshua, look at this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FYeah. Looks like a smoke canister...\x01",
            "Like that one the Sky Bandits\x01",
            "used before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8157")

    label("loc_8073")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80FD")

    ChrTalk(
        0x107,
        (
            "#065FHey...\x01",
            "Joshua! What's this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FLooks like a smoke canister...\x01",
            "Like that one the Sky Bandits\x01",
            "used before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8157")

    label("loc_80FD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8157")

    ChrTalk(
        0x106,
        "#057FThis is...a smoke canister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FAgate, let me see that a sec.\x02",
    )

    CloseMessageWindow()

    label("loc_8157")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Joshua quickly dismantled the smoke canister.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x102, -9340, 0, -4190, 315)
    SetChrPos(0x101, -10070, 0, -5250, 0)
    SetChrPos(0x107, -8820, 0, -5380, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_81E4")
    SetChrPos(0x106, -9730, 0, -6460, 0)

    label("loc_81E4")

    FadeToBright(600, 0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82C5")

    ChrTalk(
        0x101,
        (
            "#501FWhoa...\x01",
            "The smoke's cleared up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560FWow, that was cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FThere are probably more canisters\x01",
            "like this around.\x02\x03",
            "Let's find them, and I'll take\x01",
            "them apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FOkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_839C")

    label("loc_82C5")

    OP_A2(0x53E)

    ChrTalk(
        0x101,
        (
            "#501FWhoa...\x01",
            "The smoke's cleared up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560FWow, that was cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#052FHuh... Neat trick, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FThere are probably more\x01",
            "canisters like this around.\x02\x03",
            "Let's find them, and I'll take\x01",
            "them apart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_839C")

    Jump("loc_84DA")

    label("loc_839F")

    FadeToDark(600, 0, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Joshua quickly dismantled the smoke canister.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetChrPos(0x102, -9340, 0, -4190, 315)
    SetChrPos(0x101, -10070, 0, -5250, 0)
    SetChrPos(0x107, -8820, 0, -5380, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_8434")
    SetChrPos(0x106, -9730, 0, -6460, 0)

    label("loc_8434")

    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84DA")
    OP_A2(0x53E)

    ChrTalk(
        0x106,
        "#052FHuh... Neat trick, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThere are probably more\x01",
            "canisters like this around.\x02\x03",
            "Let's find them, and I'll take\x01",
            "them apart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84DA")

    EventEnd(0x0)
    Return()

    # Function_30_7F32 end

    def Function_31_84DD(): pass

    label("Function_31_84DD")

    EventBegin(0x0)
    OP_A2(0x548)
    OP_64(0x2, 0x1)
    OP_2B(0x41, 0x1)
    OP_6D(-98280, -4000, -103420, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_894A")
    OP_A2(0x52F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_858E")

    ChrTalk(
        0x101,
        (
            "#004FHey...\x01",
            "Joshua, that's...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FLooks like a smoke canister...\x01",
            "Like that one the Sky Bandits\x01",
            "used before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8702")

    label("loc_858E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_861E")

    ChrTalk(
        0x101,
        (
            "#004FHey...\x01",
            "Joshua, look at this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FYeah. Looks like a smoke canister...\x01",
            "Like that one the Sky Bandits\x01",
            "used before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8702")

    label("loc_861E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86A8")

    ChrTalk(
        0x107,
        (
            "#065FHey...\x01",
            "Joshua! What's this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FLooks like a smoke canister...\x01",
            "Like that one the Sky Bandits\x01",
            "used before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8702")

    label("loc_86A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8702")

    ChrTalk(
        0x106,
        "#057FThis is...a smoke canister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FAgate, let me see that a sec.\x02",
    )

    CloseMessageWindow()

    label("loc_8702")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Joshua quickly dismantled the smoke canister.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x102, -98680, -4000, -105420, 315)
    SetChrPos(0x101, -99580, -4000, -106640, 45)
    SetChrPos(0x107, -98140, -4000, -106180, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_878F")
    SetChrPos(0x106, -98640, -4000, -107110, 45)

    label("loc_878F")

    FadeToBright(600, 0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8870")

    ChrTalk(
        0x101,
        (
            "#501FWhoa...\x01",
            "The smoke's cleared up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560FWow, that was cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FThere are probably more canisters\x01",
            "like this around.\x02\x03",
            "Let's find them, and I'll take\x01",
            "them apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FOkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8947")

    label("loc_8870")

    OP_A2(0x53E)

    ChrTalk(
        0x101,
        (
            "#501FWhoa...\x01",
            "The smoke's cleared up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560FWow, that was cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#052FHuh... Neat trick, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FThere are probably more\x01",
            "canisters like this around.\x02\x03",
            "Let's find them, and I'll take\x01",
            "them apart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8947")

    Jump("loc_8A85")

    label("loc_894A")

    FadeToDark(600, 0, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Joshua quickly dismantled the smoke canister.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetChrPos(0x102, -98680, -4000, -105420, 315)
    SetChrPos(0x101, -99580, -4000, -106640, 45)
    SetChrPos(0x107, -98140, -4000, -106180, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_89DF")
    SetChrPos(0x106, -98640, -4000, -107110, 45)

    label("loc_89DF")

    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A85")
    OP_A2(0x53E)

    ChrTalk(
        0x106,
        "#052FHuh... Neat trick, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FThere are probably more\x01",
            "canisters like this around.\x02\x03",
            "Let's find them, and I'll take\x01",
            "them apart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A85")

    EventEnd(0x0)
    Return()

    # Function_31_84DD end

    def Function_32_8A88(): pass

    label("Function_32_8A88")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ADB")

    ChrTalk(
        0x101,
        (
            "#002F(Oops, this is the way out. \x01",
            "Now's no time to go back.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BAD")

    label("loc_8ADB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B2F")

    ChrTalk(
        0x102,
        (
            "#012F(We can't leave yet. We have \x01",
            "an investigation to pursue.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BAD")

    label("loc_8B2F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B80")

    ChrTalk(
        0x107,
        (
            "#062F(Oh, this is the exit. We \x01",
            "still have to find Grandpa.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BAD")

    label("loc_8B80")


    ChrTalk(
        0x106,
        "#050F(We ain't got time to go outside.)\x02",
    )

    CloseMessageWindow()

    label("loc_8BAD")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_32_8A88 end

    def Function_33_8BC9(): pass

    label("Function_33_8BC9")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C21")

    ChrTalk(
        0x101,
        (
            "#002F(Seems like they ran to the first\x01",
            "floor. We've gotta hurry!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CDF")

    label("loc_8C21")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C63")

    ChrTalk(
        0x102,
        "#012F(We have to hurry to the first floor...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CDF")

    label("loc_8C63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CAF")

    ChrTalk(
        0x107,
        (
            "#062F(Looks like Grandpa was\x01",
            "taken to the first floor.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CDF")

    label("loc_8CAF")


    ChrTalk(
        0x106,
        "#050F(Wrong way. Back to the first floor.)\x02",
    )

    CloseMessageWindow()

    label("loc_8CDF")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_33_8BC9 end

    def Function_34_8CFB(): pass

    label("Function_34_8CFB")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D4E")

    ChrTalk(
        0x101,
        (
            "#002F(Oops, this is the way out. \x01",
            "Now's no time to go back.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E1F")

    label("loc_8D4E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DA1")

    ChrTalk(
        0x102,
        (
            "#012F(We can't leave yet. We have\x01",
            "an investigation to pursue.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E1F")

    label("loc_8DA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DF2")

    ChrTalk(
        0x107,
        (
            "#062F(Oh, this is the exit. We \x01",
            "still have to find Grandpa.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E1F")

    label("loc_8DF2")


    ChrTalk(
        0x106,
        "#050F(We ain't got time to go outside.)\x02",
    )

    CloseMessageWindow()

    label("loc_8E1F")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_34_8CFB end

    def Function_35_8E3B(): pass

    label("Function_35_8E3B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Left: Elevator\x01",
            "Right: Basement Orbment Workshop\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_35_8E3B end

    def Function_36_8E9D(): pass

    label("Function_36_8E9D")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_36_8E9D end

    SaveToFile()

Try(main)
