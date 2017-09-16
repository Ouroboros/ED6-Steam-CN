from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3120   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3120.x',
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
        '雾香',                                 # 9
        '亚鲁瓦教授',                           # 10
        '朵洛希',                               # 11
        '玛多克工房长',                         # 12
        '斯坦因',                               # 13
        '埃尔文',                               # 14
        '艾妲',                                 # 15
        '库诺',                                 # 16
        '呆呆',                                 # 17
        '耶鲁克',                               # 18
        '冈多夫',                               # 19
        '王',                                   # 20
        '布鲁诺',                               # 21
        '莫妮卡',                               # 22
        '加鲁诺',                               # 23
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
        'ED6_DT07/CH02610 ._CH',             # 00
        'ED6_DT07/CH02050 ._CH',             # 01
        'ED6_DT07/CH02070 ._CH',             # 02
        'ED6_DT07/CH02620 ._CH',             # 03
        'ED6_DT07/CH01200 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH01060 ._CH',             # 07
        'ED6_DT07/CH01160 ._CH',             # 08
        'ED6_DT07/CH01140 ._CH',             # 09
        'ED6_DT07/CH01750 ._CH',             # 0A
        'ED6_DT07/CH01760 ._CH',             # 0B
        'ED6_DT07/CH01530 ._CH',             # 0C
        'ED6_DT07/CH02490 ._CH',             # 0D
        'ED6_DT07/CH01190 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02610P._CP',             # 00
        'ED6_DT07/CH02050P._CP',             # 01
        'ED6_DT07/CH02070P._CP',             # 02
        'ED6_DT07/CH02620P._CP',             # 03
        'ED6_DT07/CH01200P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH01060P._CP',             # 07
        'ED6_DT07/CH01160P._CP',             # 08
        'ED6_DT07/CH01140P._CP',             # 09
        'ED6_DT07/CH01750P._CP',             # 0A
        'ED6_DT07/CH01760P._CP',             # 0B
        'ED6_DT07/CH01530P._CP',             # 0C
        'ED6_DT07/CH02490P._CP',             # 0D
        'ED6_DT07/CH01190P._CP',             # 0E
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 1200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 15,
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
        TalkScenaIndex      = 16,
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
        TalkScenaIndex      = 17,
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
        TalkScenaIndex      = 7,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = 3480,
        TriggerZ            = 0,
        TriggerY            = -710,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 1200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1830,
        TriggerZ            = 1000,
        TriggerY            = 51000,
        TriggerRange        = 400,
        ActorX              = 1780,
        ActorZ              = 2500,
        ActorY              = 53000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53210,
        TriggerZ            = 0,
        TriggerY            = 520,
        TriggerRange        = 400,
        ActorX              = 52970,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1320,
        TriggerZ            = 0,
        TriggerY            = -4700,
        TriggerRange        = 1400,
        ActorX              = -1320,
        ActorZ              = 2000,
        ActorY              = -4700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_392",          # 00, 0
        "Function_1_952",          # 01, 1
        "Function_2_974",          # 02, 2
        "Function_3_98A",          # 03, 3
        "Function_4_9AE",          # 04, 4
        "Function_5_B1C",          # 05, 5
        "Function_6_B90",          # 06, 6
        "Function_7_C11",          # 07, 7
        "Function_8_CD4",          # 08, 8
        "Function_9_D21",          # 09, 9
        "Function_10_21E7",        # 0A, 10
        "Function_11_2369",        # 0B, 11
        "Function_12_2E6A",        # 0C, 12
        "Function_13_37E7",        # 0D, 13
        "Function_14_3A13",        # 0E, 14
        "Function_15_3D87",        # 0F, 15
        "Function_16_4B41",        # 10, 16
        "Function_17_56B8",        # 11, 17
        "Function_18_62E9",        # 12, 18
        "Function_19_6305",        # 13, 19
        "Function_20_630A",        # 14, 20
        "Function_21_6EDC",        # 15, 21
        "Function_22_7FCC",        # 16, 22
        "Function_23_9742",        # 17, 23
        "Function_24_BB35",        # 18, 24
        "Function_25_D395",        # 19, 25
        "Function_26_E52F",        # 1A, 26
    )


    def Function_0_392(): pass

    label("Function_0_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3A0")
    OP_A3(0x3FA)
    Event(0, 23)

    label("loc_3A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_3B1")
    SoundLoad(131)
    OP_A3(0x3FB)
    Event(0, 25)

    label("loc_3B1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3BD"),
        (SWITCH_DEFAULT, "loc_412"),
    )


    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC")
    OP_A2(0x50C)
    Event(0, 20)

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF")
    OP_A2(0x538)
    Event(0, 21)

    label("loc_3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F7")
    SetMapFlags(0x10000000)
    OP_A2(0x55A)
    Event(0, 22)

    label("loc_3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40F")
    SetMapFlags(0x10000000)
    OP_A2(0x560)
    Event(0, 24)

    label("loc_40F")

    Jump("loc_412")

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4A7")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53610, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 55570, 0, 51740, 63)
    OP_43(0x10, 0x0, 0x0, 0x3)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 25360, 0, -2660, 102)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54960, 4000, 2770, 11)
    Jump("loc_951")

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_51F")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -1150, 1000, 50950, 91)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 22260, 0, 2140, 270)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 51500, 4000, 3030, 274)
    Jump("loc_951")

    label("loc_51F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_5A5")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53610, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 25360, 0, -2660, 102)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_5A2")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3790, 0, -2310, 278)
    OP_43(0xA, 0x0, 0x0, 0x2)

    label("loc_5A2")

    Jump("loc_951")

    label("loc_5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_61D")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53610, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 52110, 0, 50520, 255)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 59030, 0, 54500, 355)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    Jump("loc_951")

    label("loc_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_69A")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1780, 1000, 53000, 183)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -710, 1000, 50990, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2940, 1000, 53000, 269)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 4070, 0, -700, 0)
    Jump("loc_951")

    label("loc_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_6E6")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1780, 1000, 53000, 183)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 54570, 0, 540, 351)
    Jump("loc_951")

    label("loc_6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_732")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -970, 1000, 51000, 352)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    Jump("loc_951")

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_799")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 61100, 2000, 2280, 11)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 3500, 0, 47710, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    Jump("loc_951")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_856")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 61100, 2000, 2280, 11)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53610, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 55570, 0, 51740, 63)
    OP_43(0x10, 0x0, 0x0, 0x3)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 25360, 0, -2660, 102)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 27160, 0, -2710, 284)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_853")
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x13, 0x10)

    label("loc_853")

    Jump("loc_951")

    label("loc_856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_8D5")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53610, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 55570, 0, 51740, 63)
    OP_43(0x10, 0x0, 0x0, 0x3)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54960, 4000, 2770, 11)
    Jump("loc_951")

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_951")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53610, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 55570, 0, 51740, 63)
    OP_43(0x10, 0x0, 0x0, 0x3)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54960, 4000, 2770, 11)

    label("loc_951")

    Return()

    # Function_0_392 end

    def Function_1_952(): pass

    label("Function_1_952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96A")
    OP_B1("t3120_y")
    Jump("loc_973")

    label("loc_96A")

    OP_B1("t3120_n")

    label("loc_973")

    Return()

    # Function_1_952 end

    def Function_2_974(): pass

    label("Function_2_974")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_989")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_974")

    label("loc_989")

    Return()

    # Function_2_974 end

    def Function_3_98A(): pass

    label("Function_3_98A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9AD")
    OP_8D(0xFE, 52620, 51160, 59990, 53120, 3000)
    Jump("Function_3_98A")

    label("loc_9AD")

    Return()

    # Function_3_98A end

    def Function_4_9AE(): pass

    label("Function_4_9AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_A11")

    ChrTalk(
        0xFE,
        (
            "呼，说起来\x01",
            "外面还真是吵啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "又是主日学校的孩子们\x01",
            "在翘课打闹吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B18")

    label("loc_A11")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "这把导力枪\x01",
            "可以将内部驱动导力器的性能\x01",
            "发挥至极限呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说平衡性确实差了点，\x01",
            "很有必要加以改进，\x01",
            "不过也算是在可以忍受的范围内吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总而言之一切还算顺利。\x01",
            "这样的话，\x01",
            "应该可以比预定时间更早做出成品来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B18")

    TalkEnd(0xFE)
    Return()

    # Function_4_9AE end

    def Function_5_B1C(): pass

    label("Function_5_B1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_B8C")

    ChrTalk(
        0xA,
        (
            "#150F小艾，\x01",
            "了解到什么的话要告诉我哦。\x02\x03",
            "我想让这次的特辑\x01",
            "有更多独家新闻。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8C")

    TalkEnd(0xFE)
    Return()

    # Function_5_B1C end

    def Function_6_B90(): pass

    label("Function_6_B90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_C0D")

    ChrTalk(
        0xFE,
        (
            "唉，商品的说明果然\x01",
            "必须像这样写才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "射程……精度……驱动时间……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，多么具体啊。\x02",
    )

    CloseMessageWindow()

    label("loc_C0D")

    TalkEnd(0xFE)
    Return()

    # Function_6_B90 end

    def Function_7_C11(): pass

    label("Function_7_C11")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_CD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_C74")

    ChrTalk(
        0xFE,
        "……杨？好像不是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那就是……汪？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不，好像两个都不对。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD0")

    label("loc_C74")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "之前给我担任护卫的那个兄弟……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "他到底叫什么来着？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD0")

    TalkEnd(0xFE)
    Return()

    # Function_7_C11 end

    def Function_8_CD4(): pass

    label("Function_8_CD4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_D1D")

    ChrTalk(
        0x9,
        (
            "#130F看来发生了不得了的事情啊……\x01",
            "　\x02\x03",
            "请务必要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1D")

    TalkEnd(0xFE)
    Return()

    # Function_8_CD4 end

    def Function_9_D21(): pass

    label("Function_9_D21")

    TalkBegin(0x8)
    FadeToDark(300, 0, 70)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "报告\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8C")
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x40)"), scpexpr(EXPR_END)), "loc_E11")
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#790F辛苦了。\x01",
            "看来你们很顺利地完成了任务呢。\x02\x03",
            "如果完成其他任务的话，\x01",
            "别忘记回协会报告一下哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_E11")

    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#790F啊，\x01",
            "现在没有需要报告的工作呢。\x02\x03",
            "如果完成其他任务的话，\x01",
            "别忘记回协会报告一下哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E83")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_E8C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9D")
    TalkEnd(0x8)
    Return()

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_10D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 3)), scpexpr(EXPR_END)), "loc_F2A")

    ChrTalk(
        0x8,
        (
            "#790F你们还是尽快动身离开这个地方吧。\x01",
            "　\x02\x03",
            "愿女神保佑。\x01",
            "你们俩都要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D6")

    label("loc_F2A")

    OP_A2(0x57B)

    ChrTalk(
        0x8,
        "#790F哎呀，搭乘手续办好了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F嗯，那个……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔说明了有关王国军盘查的消息\x01",
            "和退掉船票准备步行去王都的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x8,
        (
            "#792F是这样啊……\x02\x03",
            "#790F对方的行动比想象的还要快啊。\x01",
            "　\x02\x03",
            "你们最好也尽快动身离开这个地方吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，这就出发。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F再见了，雾香姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F愿女神保佑。\x01",
            "你们俩都要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D6")

    Jump("loc_21E3")

    label("loc_10D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1177")

    ChrTalk(
        0x8,
        (
            "#790F去往王都的船是１１点出发的……\x01",
            "　\x02\x03",
            "你们最好赶快去飞艇坪办理搭乘手续吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_1177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1295")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F9")

    ChrTalk(
        0x8,
        (
            "#790F你们去把提妲所说的那个装置拿来。\x01",
            "　\x02\x03",
            "在这段时间里， \x01",
            "我会将要塞的资料准备好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1292")

    label("loc_11F9")


    ChrTalk(
        0x8,
        (
            "#790F工房船也差不多应该准备好了。\x01",
            "　\x02\x03",
            "你们准备好的话\x01",
            "就马上去飞艇坪吧。\x02\x03",
            "愿女神保佑。\x01",
            "你们要小心行事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1292")

    Jump("loc_21E3")

    label("loc_1295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1348")

    ChrTalk(
        0x8,
        (
            "#790F去雷斯顿要塞的话，\x01",
            "要从城里的东门出去。\x02\x03",
            "街道的途中会有一个三岔路，\x01",
            "从那里往北走就行了。\x02\x03",
            "……千万要小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_1348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1390")

    ChrTalk(
        0x8,
        (
            "#790F我这里会跟王国军事先联络好。\x01",
            "　\x02\x03",
            "好了，快点动身吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1406")

    label("loc_1390")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#790F这边如果有什么事情，\x01",
            "我会交给王去处理。\x02\x03",
            "你们快点到『红莲之塔』那里吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1406")

    Jump("loc_21E3")

    label("loc_1409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1659")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1493")

    ChrTalk(
        0x8,
        (
            "#790F你们俩赶快去中央工房那边看看吧。\x01",
            "　\x02\x03",
            "如果发生什么紧急情况，\x01",
            "就在现场果断处理就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1656")

    label("loc_1493")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#790F太好了。\x01",
            "你们俩来得正好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F雾香姐，发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F中央工房那边似乎发生了什么骚乱。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F不巧，\x01",
            "我在这里无法了解到现场的事态。\x02\x03",
            "因为游击士都在外面执行任务，\x01",
            "我自己没法行动。\x02\x03",
            "你们俩可以马上赶去中央工房吗？\x01",
            "　\x02\x03",
            "如果发生什么紧急情况，\x01",
            "就在现场果断处理就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_1656")

    Jump("loc_21E3")

    label("loc_1659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_19A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 2)), scpexpr(EXPR_END)), "loc_16E3")

    ChrTalk(
        0x8,
        (
            "#790F代替博士去办事\x01",
            "也是在替他分担工作量啊。\x02\x03",
            "虽说到亚尔摩并不算太远，\x01",
            "你们路上也不要大意哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A1")

    label("loc_16E3")

    OP_A2(0x57A)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1782")

    ChrTalk(
        0x8,
        (
            "#790F啊，提妲。\x02\x03",
            "我已经听说了。\x01",
            "你们要去亚尔摩那里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊……对，是啊。\x02\x03",
            "这次是代替爷爷\x01",
            "去修理村里的水泵。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C8")

    label("loc_1782")


    ChrTalk(
        0x8,
        (
            "#790F啊，是你们两个人。\x02\x03",
            "我听说了哦。\x01",
            "你们要去亚尔摩那里吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 1)), scpexpr(EXPR_END)), "loc_183B")

    ChrTalk(
        0x101,
        (
            "#000F啊，对了。\x02\x03",
            "海泽尔小姐说\x01",
            "已经跟这里联系过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#790F嗯，是的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_183B")


    ChrTalk(
        0x101,
        (
            "#004F哇～不愧是雾香姐姐。\x01",
            "这么快就知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F工房接待处的海泽尔\x01",
            "已经跟我这里联系过了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CE")


    ChrTalk(
        0x8,
        (
            "#790F我已经了解情况了。\x02\x03",
            "你们这次的工作内容\x01",
            "就是代替博士去办事吧。\x02\x03",
            "虽说到亚尔摩并不算太远，\x01",
            "你们路上也不要大意哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，交给我们吧。\x02\x03",
            "那我们出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F告辞了。\x02",
    )

    CloseMessageWindow()

    label("loc_19A1")

    Jump("loc_21E3")

    label("loc_19A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1A9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A11")

    ChrTalk(
        0x8,
        (
            "#790F艾丝蒂尔、约修亚。\x01",
            "就拜托你们给博士帮忙了。\x02\x03",
            "#791F协会这边也会密切关注\x01",
            "那个导力器的真面目。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9C")

    label("loc_1A11")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#790F啊，艾丝蒂尔、约修亚。\x02\x03",
            "#791F呵呵，你们真是辛苦了。\x01",
            "就拜托你们给博士帮忙了。\x02\x03",
            "协会这边也会密切关注\x01",
            "那个导力器的真面目。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A9C")

    Jump("loc_21E3")

    label("loc_1A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1EA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE3")
    OP_A2(0x512)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(3730, 0, 600, 0)
    SetChrPos(0x102, 4430, 0, -700, 0)
    SetChrPos(0x101, 3170, 0, -710, 0)
    SetChrPos(0x107, 4059, 0, -1760, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#791F#2P早上好。\x01",
            "昨晚真是虚惊一场啊。\x02\x03",
            "你们俩还是赶快\x01",
            "把详细情况报告给我听吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F啊，雾香姐还真是开门见山。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F#2P虽然大致情况\x01",
            "已经从工房长那里听说了……\x02\x03",
            "不过还是想听\x01",
            "实际在场的目击者说明一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F好吧，那就……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们向雾香报告了\x01",
            "昨晚发生的『导力停止现象』的详细情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#790F#2P原来如此……\x02\x03",
            "真不愧是匿名寄给\x01",
            "卡西乌斯先生的东西，\x01",
            "看来那个导力器不是简单的物品。\x02\x03",
            "协会方面对此事也很在意，\x01",
            "就请你们继续协助博士的研究吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，正打算这么做呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F如果发现什么的话，我们再回来报告。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1EA0")

    label("loc_1DE3")


    ChrTalk(
        0x8,
        (
            "#790F那个黑色导力器\x01",
            "果然不是什么简单的东西啊。\x02\x03",
            "协会这边也对它很感兴趣，\x01",
            "你们就继续协助博士调查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA0")

    Jump("loc_21E3")

    label("loc_1EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_213F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F3F")
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#790F拉赛尔博士的研究所\x01",
            "在蔡斯城的西南边。\x02\x03",
            "出了协会门口之后往左前方走，\x01",
            "到了城门再向右拐就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_213C")

    label("loc_1F3F")

    OP_A2(0x0)
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#790F啊，艾丝蒂尔、约修亚。\x02\x03",
            "……拉赛尔博士的研究所\x01",
            "在蔡斯城的西南边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F雾香姐姐， \x01",
            "你、你好厉害哦。\x02\x03",
            "你怎么知道\x01",
            "我们要去博士家啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F……怎么会不知道呢。\x02\x03",
            "你们不是和博士的孙女儿在一起吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F哦，对啊。\x02\x03",
            "呵呵，\x01",
            "这回可省下报告的功夫了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F博士是个很忙的人，\x01",
            "你们俩可不要失礼哦。\x02\x03",
            "那再见了，提妲。\x01",
            "他们俩就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，好的。\x01",
            "我知道了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_213C")

    Jump("loc_21E3")

    label("loc_213F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21E3")

    ChrTalk(
        0x8,
        (
            "#790F你们先去拜会一下\x01",
            "玛多克工房长吧。\x02\x03",
            "说不定能够了解到一些\x01",
            "有关那个导力器的线索。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E3")

    TalkEnd(0x8)
    Return()

    # Function_9_D21 end

    def Function_10_21E7(): pass

    label("Function_10_21E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2365")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2232")

    ChrTalk(
        0xFE,
        (
            "店里面也没有受到损失，\x01",
            "暂且可以安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2365")

    label("loc_2232")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "昨天晚上导力停止了，\x01",
            "真是把我吓坏了呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说以前也听说过\x01",
            "只有在特殊的结晶回路中\x01",
            "才会有那种力量……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想不到会产生\x01",
            "影响到那么大范围的现象呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果这力量用于武器研制的话，\x01",
            "恐怕会导致各国的军力失去平衡。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2365")

    TalkEnd(0xFE)
    Return()

    # Function_10_21E7 end

    def Function_11_2369(): pass

    label("Function_11_2369")

    TalkBegin(0xD)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E1")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_23CA")
    OP_A9(0x4C)
    Jump("loc_23D8")

    label("loc_23CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_23D6")
    OP_A9(0x4B)
    Jump("loc_23D8")

    label("loc_23D6")

    OP_A9(0x3E)

    label("loc_23D8")

    OP_56(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_23E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23F2")
    TalkEnd(0xD)
    Return()

    label("loc_23F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_24DC")

    ChrTalk(
        0xD,
        (
            "哦～早上好啊。\x01",
            "这里是贝尔杂货店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "本店商品种类非常齐全，\x01",
            "能充分满足各位顾客的要求哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "所以……\x01",
            "想买什么就请来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "本店的经营\x01",
            "也要靠大家的支持。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E66")

    label("loc_24DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2533")

    ChrTalk(
        0xD,
        "啊，你们好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "贝尔杂货店\x01",
            "今天也会以齐全的商品\x01",
            "来满足大家的要求。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E66")

    label("loc_2533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_276B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25E4")

    ChrTalk(
        0xD,
        (
            "妻子她表示了\x01",
            "对我想法的理解呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "她说店里以后也要像以前那样\x01",
            "保持商品种类的齐全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "妻子为了我也很努力。\x01",
            "我以后也要\x01",
            "更加努力才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2768")

    label("loc_25E4")

    OP_A2(0x2)

    ChrTalk(
        0xD,
        "啊，早上好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "今天一大早\x01",
            "就有开心的事哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "妻子头一次\x01",
            "对我的想法表示理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "她说店里以后也要像以前那样\x01",
            "保持商品种类的齐全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "虽说经营方面形势严峻，\x01",
            "但是只要节约开支的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "这样的话\x01",
            "我就能安心地和顾客面对面了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2768")

    Jump("loc_2E66")

    label("loc_276B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_28C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27F8")

    ChrTalk(
        0xD,
        (
            "唔～通常情况下， \x01",
            "只要我擅作主张降了价，她就会生气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "今天，她心情很不错呢，\x01",
            "发生了什么好事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BF")

    label("loc_27F8")

    OP_A2(0x2)

    ChrTalk(
        0xD,
        (
            "总觉得最近\x01",
            "妻子的态度有点奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "她应该知道，出事的时候\x01",
            "我在给镇里面的人分派商品……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "……为什么她不生气呢？\x02",
    )

    CloseMessageWindow()

    label("loc_28BF")

    Jump("loc_2E66")

    label("loc_28C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2A2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_293A")

    ChrTalk(
        0xD,
        (
            "妻子艾妲\x01",
            "肩膀酸疼得厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "今天也要去\x01",
            "礼拜堂拿药呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2B")

    label("loc_293A")

    OP_A2(0x2)

    ChrTalk(
        0xD,
        (
            "妻子艾妲\x01",
            "肩膀酸疼得厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "今天也要去\x01",
            "礼拜堂拿药呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "中央工房里面\x01",
            "也有研究医学的老师……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "但效果还是比不上\x01",
            "传统的医疗法呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A2B")

    Jump("loc_2E66")

    label("loc_2A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2B56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2AC9")

    ChrTalk(
        0xD,
        (
            "我家大儿子\x01",
            "似乎对商品陈列很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "放着他不管的话，\x01",
            "他会整整一天都在搞那些东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B53")

    label("loc_2AC9")

    OP_A2(0x2)
    TurnDirection(0xD, 0xF, 400)

    ChrTalk(
        0xD,
        "喂喂，库诺。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不要再动\x01",
            "那些商品了好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不是说好了\x01",
            "一天只整理一次商品吗？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)

    label("loc_2B53")

    Jump("loc_2E66")

    label("loc_2B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2CEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2BDC")

    ChrTalk(
        0xD,
        (
            "整个城市的导力\x01",
            "全部都停止了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "世界上还有\x01",
            "这么不可思议的事呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CE9")

    label("loc_2BDC")

    OP_A2(0x2)

    ChrTalk(
        0xD,
        (
            "昨天晚上\x01",
            "你们没事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我以为是照明灯出故障了，\x01",
            "打算立即去工房看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "谁知一走到外面，\x01",
            "发现整个城镇就像森林里一样漆黑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我马上就意识到\x01",
            "这不是什么简单的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CE9")

    Jump("loc_2E66")

    label("loc_2CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2DE6")

    ChrTalk(
        0xD,
        (
            "我立志要把这个店\x01",
            "经营成受大家喜爱的店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不管什么样的人来，\x01",
            "都能在这里找到称心的商品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "虽然这样采购的时候会很麻烦，\x01",
            "不过毕竟不努力就不会成功啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E66")

    label("loc_2DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E66")

    ChrTalk(
        0xD,
        (
            "您好，欢迎光临。\x01",
            "这里是贝尔杂货店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "从食品到日用品，\x01",
            "这里都一应俱全。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E66")

    TalkEnd(0xD)
    Return()

    # Function_11_2369 end

    def Function_12_2E6A(): pass

    label("Function_12_2E6A")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2E77")
    Jump("loc_2F04")

    label("loc_2E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2F04")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF3")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_2EDC")
    OP_A9(0x4C)
    Jump("loc_2EEA")

    label("loc_2EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2EE8")
    OP_A9(0x4B)
    Jump("loc_2EEA")

    label("loc_2EE8")

    OP_A9(0x3E)

    label("loc_2EEA")

    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_2EF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F04")
    TalkEnd(0xE)
    Return()

    label("loc_2F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2F74")

    ChrTalk(
        0xE,
        (
            "呼，这样子的话\x01",
            "下个月可能也很辛苦吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过，我早已经有思想准备了，\x01",
            "一定要努力渡过难关。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E3")

    label("loc_2F74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2FA8")

    ChrTalk(
        0xE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这里是贝尔杂货店。\x01",
            "请慢慢挑选喜欢的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E3")

    label("loc_2FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_30BF")

    ChrTalk(
        0xE,
        (
            "今天早上，我和丈夫商量了一下，\x01",
            "制定了今后的经营方针。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "我们决定努力\x01",
            "让商品种类更加齐全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "和以前不同， \x01",
            "采购的活儿由我全部负责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这样做到底会怎么样。\x01",
            "不尝试一下不会知道呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E3")

    label("loc_30BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_32C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_31E6")

    ChrTalk(
        0xE,
        (
            "我似乎也开始明白\x01",
            "丈夫的目标了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "他只会常常做梦，\x01",
            "不能说是个会做生意的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "他总想让我们的店\x01",
            "能给大家带来最大的方便和好处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "如果真能做成这样的店，\x01",
            "的确是很了不起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BD")

    label("loc_31E6")

    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "听说今天在出事现场，\x01",
            "丈夫给避难的人们\x01",
            "配发了必要物资。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这样的话， \x01",
            "这个月又会是赤字了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "唉，没办法啦。\x01",
            "就当是捐赠，算了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32BD")

    Jump("loc_37E3")

    label("loc_32C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3353")

    ChrTalk(
        0xE,
        (
            "真是让人难以置信。\x01",
            "中央工房竟然会遭到袭击……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "为什么丈夫\x01",
            "会发现这件事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3402")

    label("loc_3353")

    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "刚才听说，\x01",
            "中央工房遭到袭击了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "我丈夫也是，\x01",
            "出去后到现在还没有回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "真是让人担心啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3402")

    Jump("loc_37E3")

    label("loc_3405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_34BC")

    ChrTalk(
        0xE,
        (
            "丈夫他嘴里说着\x01",
            "出了点奇怪的事什么的，\x01",
            "就跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "而且还擅自将\x01",
            "店里面的商品也带走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "唉，\x01",
            "他究竟在想什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E3")

    label("loc_34BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_35D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3557")

    ChrTalk(
        0xE,
        (
            "呼呼，\x01",
            "说起来还有工作没完成呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "时间早的话，收拾一下，\x01",
            "然后去礼拜堂拿点治肩酸的药。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35D2")

    label("loc_3557")

    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "导力器使用不了的话，\x01",
            "我们就什么都干不了了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "昨天发生了那样的事情之后，\x01",
            "我们不得不考虑一下这件事情呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D2")

    Jump("loc_37E3")

    label("loc_35D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_374C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3681")

    ChrTalk(
        0xE,
        (
            "如果不进一些好卖的商品，\x01",
            "那就谈不上有什么利润了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "啊，不但肩膀重，\x01",
            "头也开始疼了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3749")

    label("loc_3681")

    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "我丈夫也不考虑\x01",
            "商品能不能卖出去，\x01",
            "只会一味地进货又进货。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "如果不清楚这些商品能不能卖掉，\x01",
            "经营起来真的是很辛苦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "都不知道他有没有想过\x01",
            "怎么去把生意做好？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3749")

    Jump("loc_37E3")

    label("loc_374C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_37E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_37A4")

    ChrTalk(
        0xE,
        (
            "呼，一看见账簿\x01",
            "我就觉得肩膀好沉重……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E3")

    label("loc_37A4")

    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "哈啊……\x01",
            "真令人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "这个月又快超支了。\x02",
    )

    CloseMessageWindow()

    label("loc_37E3")

    TalkEnd(0xE)
    Return()

    # Function_12_2E6A end

    def Function_13_37E7(): pass

    label("Function_13_37E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3834")

    ChrTalk(
        0xFE,
        "唔，真是少见呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "妈妈她\x01",
            "竟然会表扬爸爸。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0F")

    label("loc_3834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_38CA")

    ChrTalk(
        0xFE,
        (
            "爸爸他为什么要拿走\x01",
            "各种各样的东西啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "药品、食品什么的也就罢了，\x01",
            "带着人偶打算干什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且还一副\x01",
            "慌慌张张的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0F")

    label("loc_38CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_390E")

    ChrTalk(
        0xFE,
        "……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……嗯。\x01",
            "这下就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "已经没有我\x01",
            "去帮忙的必要了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0F")

    label("loc_390E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_3A0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3998")

    ChrTalk(
        0xFE,
        (
            "虽然爸爸说\x01",
            "一天整理一次商品就行了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过客人已经动过了，\x01",
            "必须按照原样放好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0F")

    label("loc_3998")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "然后将这条鱼放回左边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……嗯，这下就好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，终于又回到\x01",
            "最完美的陈列状态了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0F")

    TalkEnd(0xFE)
    Return()

    # Function_13_37E7 end

    def Function_14_3A13(): pass

    label("Function_14_3A13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3AAA")

    ChrTalk(
        0xFE,
        "博士！不得了了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "妈妈的肩\x01",
            "好像开始疼起来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "什么！赶快啊。\x01",
            "快点和教区长联系！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D83")

    label("loc_3AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3AE6")

    ChrTalk(
        0xFE,
        (
            "今天去\x01",
            "肯定还来得及。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D83")

    label("loc_3AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3B15")

    ChrTalk(
        0xFE,
        "我说，妈妈。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "爸爸在哪儿呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D83")

    label("loc_3B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3B77")

    ChrTalk(
        0xFE,
        (
            "昨天晚上\x01",
            "外面好暗呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我睡在床上\x01",
            "都看见了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D83")

    label("loc_3B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3C37")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "博士！\x01",
            "导力压下降了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "什么！\x01",
            "导力引擎的功率很正常啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D4E")

    label("loc_3C37")

    OP_A2(0x5)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "哇～啊，\x01",
            "是提妲姐～姐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们来玩导力技师游戏吧。\x01",
            "玩导力技师游戏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F不好意思啊，呆呆。\x01",
            "姐姐现在要给客人们带路啊。\x02\x03",
            "#061F所以呢，还是下次玩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，好吧～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我明白～了，提妲博士。\x02",
    )

    CloseMessageWindow()

    label("loc_3D4E")

    Jump("loc_3D83")

    label("loc_3D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3D83")

    ChrTalk(
        0xFE,
        "姐姐～你们是谁～啊？\x02",
    )

    CloseMessageWindow()

    label("loc_3D83")

    TalkEnd(0xFE)
    Return()

    # Function_14_3A13 end

    def Function_15_3D87(): pass

    label("Function_15_3D87")

    TalkBegin(0x11)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF3")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_3DE8")
    OP_A9(0x42)
    Jump("loc_3DEA")

    label("loc_3DE8")

    OP_A9(0x3D)

    label("loc_3DEA")

    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_3DF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E04")
    TalkEnd(0x11)
    Return()

    label("loc_3E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3EE2")

    ChrTalk(
        0x11,
        (
            "不管怎么说\x01",
            "老板也是个成功的人，\x01",
            "值得学习的地方我也要学着点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "唉，\x01",
            "就是觉得他思想有点顽固……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "把这些也算在\x01",
            "学习范围之内吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FF4")

    label("loc_3EE2")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "昨天，和斯坦因老板\x01",
            "商量了一下采购的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "暂时先决定按照\x01",
            "老板的意向来选择商品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不过我并没有完全理解\x01",
            "这位重视可靠性的\x01",
            "斯坦因老板的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "啊，这也是需要学习的地方吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3FF4")

    Jump("loc_4B3D")

    label("loc_3FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_413B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4085")

    ChrTalk(
        0x11,
        (
            "唔，\x01",
            "那个加鲁诺竟然会这么说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "我也渐渐觉得\x01",
            "老板的话有些合理了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "……不、不行。\x01",
            "不能受别人的影响。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4138")

    label("loc_4085")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "今天一大清早加鲁诺就来了，\x01",
            "只说了一句『我明白老板话里的意思了』，\x01",
            "之后就回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "唔，\x01",
            "那个加鲁诺竟然会这么说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "老板的想法\x01",
            "到底哪里正确了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4138")

    Jump("loc_4B3D")

    label("loc_413B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4224")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_419E")

    ChrTalk(
        0x11,
        "唔，加鲁诺那家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不知道怎么\x01",
            "就被斯坦因老板给教唆了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4221")

    label("loc_419E")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "今天一大清早加鲁诺就来了，\x01",
            "只说了一句『我明白老板话里的意思了』，\x01",
            "之后就回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "那家伙\x01",
            "到底怎么了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4221")

    Jump("loc_4B3D")

    label("loc_4224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4281")

    ChrTalk(
        0x11,
        "哦，这么晚还有客人来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "店还没有关门，\x01",
            "请放心挑选我们的商品吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3D")

    label("loc_4281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4363")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_42E8")

    ChrTalk(
        0x11,
        "有什么损失吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "要是研究计划\x01",
            "没受影响就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4360")

    label("loc_42E8")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "喂，你们听说了吗？\x01",
            "中央工房遭到袭击了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "当时我在店里面忙着聊天，\x01",
            "一点都没有注意到啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4360")

    Jump("loc_4B3D")

    label("loc_4363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_44E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_43D1")

    ChrTalk(
        0x11,
        (
            "哇，\x01",
            "真的是一把非常棒的导力枪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "平衡性若是再好些，\x01",
            "我想肯定会更加畅销的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44E1")

    label("loc_43D1")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "中央工房的加鲁诺\x01",
            "把研究中的导力枪带来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "那家伙真厉害。\x01",
            "真是把很棒的导力枪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不过整体的平衡性有些特殊\x01",
            "导致难以操作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "就算操作多多少少有点难，\x01",
            "不过只要威力强大就足以弥补了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44E1")

    Jump("loc_4B3D")

    label("loc_44E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_46FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4568")

    ChrTalk(
        0x11,
        (
            "啊啊，加鲁诺……\x01",
            "快把试制品拿来看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "最近唯一的期盼\x01",
            "就是能看到那件产品了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46FA")

    label("loc_4568")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        "呵呵，欢迎啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "哎呀，\x01",
            "又和斯坦因老板因为采购的事\x01",
            "而发生争执了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不管我们怎么说，\x01",
            "他就是不愿意引进\x01",
            "还处于研究阶段的导力枪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "虽然我已经尽可能劝说他了，\x01",
            "不过我只是个被雇来的店长，没有权利管他啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "啊啊，加鲁诺……\x01",
            "快把试制品拿来看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "最近嘛，\x01",
            "只有这么点期盼了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46FA")

    Jump("loc_4B3D")

    label("loc_46FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4789")

    ChrTalk(
        0x11,
        (
            "中央工房里面\x01",
            "现在一定乱成一团了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "因为那里\x01",
            "全都是测量用的机器呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4824")

    label("loc_4789")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "昨天晚上，\x01",
            "我正在调整导力枪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "突然，\x01",
            "测量器停止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "我还以为把商品弄坏了，\x01",
            "当时一下子傻了眼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4824")

    Jump("loc_4B3D")

    label("loc_4827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4A7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_48C3")

    ChrTalk(
        0x11,
        (
            "我虽然也明白老板\x01",
            "把武器的可靠性放在第一位的信条……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不过稍微想想，\x01",
            "老板是否有点太过固执了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A7A")

    label("loc_48C3")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "我们这里的老板是斯坦因，\x01",
            "就住在这附近……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "根据斯坦因先生的原则，\x01",
            "我们是绝对不会引进\x01",
            "最先进的高尖端武器的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "这好像是因为\x01",
            "过于先进的武器\x01",
            "可靠性还得不到认可……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "有个工房的研究员亲自来出售\x01",
            "正在研究中的超级导力枪，\x01",
            "也被老板拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A7A")

    Jump("loc_4B3D")

    label("loc_4A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4B3D")

    ChrTalk(
        0x11,
        (
            "哦，欢迎光临。\x01",
            "这里是斯坦因武器商会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "本店全是各种各样的好商品。\x01",
            "请慢慢地看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B3D")

    TalkEnd(0x11)
    Return()

    # Function_15_3D87 end

    def Function_16_4B41(): pass

    label("Function_16_4B41")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4CB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4BE1")

    ChrTalk(
        0xFE,
        (
            "虽说我也很在意博士这件事，\x01",
            "不过现在也只有相信阿加特那家伙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "毕竟我们身上也有些\x01",
            "非做不可的任务啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB6")

    label("loc_4BE1")


    ChrTalk(
        0xFE,
        (
            "哦，是你们啊。\x01",
            "我听说你们的营救作战了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然事情还不算完美解决，\x01",
            "不过现在也只有相信阿加特那家伙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果是那家伙出马， \x01",
            "应该能让博士他们安全逃离的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB6")

    Jump("loc_56B4")

    label("loc_4CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_5194")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 6)), scpexpr(EXPR_END)), "loc_4D8D")

    ChrTalk(
        0xFE,
        (
            "王那家伙好像也是充满干劲地工作着，\x01",
            "这样我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前还担心他会因为\x01",
            "觉得自己应该对事故负责\x01",
            "而意志消沉下来呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是不是雾香\x01",
            "用什么巧妙的办法激励他了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5191")

    label("loc_4D8D")

    OP_A2(0x57E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_END)), "loc_4E4F")

    ChrTalk(
        0x101,
        "#000F啊，冈多夫先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是刚从王都回来的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦，我刚得知了消息。\x01",
            "然后就匆匆忙忙赶回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "雾香她已经告诉我\x01",
            "这边大概的事情了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "阿加特那家伙\x01",
            "已经没事了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F33")

    label("loc_4E4F")


    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们就是那两个准游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我是蔡斯所属的游击士，\x01",
            "名叫冈多夫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我听到消息之后， \x01",
            "就从出差地王都赶了回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大体情况我已经问过雾香了……\x01",
            "呃，阿加特他没事吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F33")


    ChrTalk(
        0x101,
        (
            "#000F嗯，还好度过了危险期……\x02\x03",
            "……哎，你认识阿加特吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，因为工作的关系\x01",
            "我们已经见过很多次面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很久之前他\x01",
            "就已经是个非常有名的家伙啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……总之，\x01",
            "他没事就好啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，搜查的工作\x01",
            "就交给你们和阿加特了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而我们就尽量去\x01",
            "处理一些日常的零碎工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，谢谢。\x02\x03",
            "那就拜托您了。\x01",
            "冈多夫先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们告辞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，你们要保重哦。\x02",
    )

    CloseMessageWindow()

    label("loc_5191")

    Jump("loc_56B4")

    label("loc_5194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_56B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5638")
    OP_A2(0x57D)
    OP_4A(0x13, 255)
    OP_4A(0x12, 255)

    ChrTalk(
        0x13,
        "嗯？　出差！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "冈多夫先生你……吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "啊，不好意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "因为军方直接点名……\x01",
            "我必须去一趟王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "又不是只剩下你一个，\x01",
            "那些准游击士也在嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "你们同心协力的话，\x01",
            "两三天肯定能应付过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "是啊，是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "我明白了。\x01",
            "我会拼命努力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "哦……\x01",
            "总之乐观一点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x0, 400)

    ChrTalk(
        0x12,
        (
            "……哦，\x01",
            "这就是传闻中的两个人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "你们两个\x01",
            "来得真是时候啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5429")
    OP_A2(0x57C)

    ChrTalk(
        0x13,
        "……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x0, 400)

    ChrTalk(
        0x13,
        (
            "难道……\x01",
            "你们就是那些准游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F……嗯？\x02\x03",
            "啊，没错。\x01",
            "我们就是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面。\x01",
            "我是准游击士约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊。\x01",
            "我是准游击士艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5477")

    label("loc_5429")

    TurnDirection(0x13, 0x0, 400)

    ChrTalk(
        0x13,
        (
            "啊，\x01",
            "是艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "你们来得正是时候。\x02",
    )

    CloseMessageWindow()

    label("loc_5477")


    ChrTalk(
        0x12,
        "呵呵，果然是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "看到你们，\x01",
            "我终于明白雾香说的话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，\x01",
            "请问您要去王都吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "啊啊，没错。\x01",
            "那边有很紧急的任务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "蔡斯支部的工作\x01",
            "就交给你们和王负责了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "你们就好好努力吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "……就是这样。\x01",
            "总之希望能借助你们的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好，我们会尽全力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "那就这样吧。\x01",
            "拜托你们留守了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x13, 255)
    OP_4B(0x12, 255)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x10)
    Jump("loc_56B4")

    label("loc_5638")


    ChrTalk(
        0x12,
        (
            "不好意思，\x01",
            "拜托你们在这里留守了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "你们要和王那家伙\x01",
            "好好合作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56B4")

    TalkEnd(0x12)
    Return()

    # Function_16_4B41 end

    def Function_17_56B8(): pass

    label("Function_17_56B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_5808")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5758")

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "听说你们要去王都了对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没关系，\x01",
            "你们肯定能够很快成为正游击士的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以后也要精力充沛地\x01",
            "努力工作哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5805")

    label("loc_5758")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "啊，是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我听说了哦，\x01",
            "营救作战按照计划顺利实行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然博士他们以后会怎样\x01",
            "现在还不能放心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之，很感谢你们。\x01",
            "谢谢把他们救了出来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5805")

    Jump("loc_62E5")

    label("loc_5808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_5D2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CAC")
    OP_A2(0x57D)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)

    ChrTalk(
        0x13,
        "嗯？　出差！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "冈多夫先生你……吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "啊，不好意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "因为军方直接点名……\x01",
            "我必须去一趟王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "又不是只剩下你一个，\x01",
            "那些准游击士也在嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "你们同心协力的话，\x01",
            "两三天肯定能应付过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "是啊，是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "我明白了。\x01",
            "我会拼命努力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "哦……\x01",
            "总之乐观一点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x0, 400)

    ChrTalk(
        0x12,
        (
            "……哦，\x01",
            "这就是传闻中的两个人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "你们两个\x01",
            "来得真是时候啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A9D")
    OP_A2(0x57C)

    ChrTalk(
        0x13,
        "……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x0, 400)

    ChrTalk(
        0x13,
        (
            "难道……\x01",
            "你们就是那些准游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F……嗯？\x02\x03",
            "啊，没错。\x01",
            "我们就是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面。\x01",
            "我是准游击士约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊。\x01",
            "我是准游击士艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AEB")

    label("loc_5A9D")

    TurnDirection(0x13, 0x0, 400)

    ChrTalk(
        0x13,
        (
            "啊，\x01",
            "是艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "你们来得正是时候。\x02",
    )

    CloseMessageWindow()

    label("loc_5AEB")


    ChrTalk(
        0x12,
        "呵呵，果然是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "看到你们，\x01",
            "我终于明白雾香说的话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，\x01",
            "请问您要去王都吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "啊啊，没错。\x01",
            "那边有很紧急的任务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "蔡斯支部的工作\x01",
            "就交给你们和王负责了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "你们就好好努力吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "……就是这样。\x01",
            "总之希望能借助你们的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好，我们会尽全力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "那就这样吧。\x01",
            "拜托你们留守了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x10)
    OP_4B(0x12, 255)
    OP_4B(0x13, 255)
    Jump("loc_5D28")

    label("loc_5CAC")


    ChrTalk(
        0xFE,
        (
            "接下来一段时间\x01",
            "冈多夫先生要到别的地方出差……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好吧，今后的工作， \x01",
            "必须更加充满干劲去做才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望你们\x01",
            "也能够协助我哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D28")

    Jump("loc_62E5")

    label("loc_5D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_6186")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_611E")
    OP_A2(0x57C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D8B")

    ChrTalk(
        0xFE,
        "啊啊，提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "竟然会来武器店，真少见啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DB3")

    label("loc_5D8B")

    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        "嗯……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "原来是提妲来了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DB3")


    ChrTalk(
        0xFE,
        (
            "咦……？\x01",
            "这两位不会是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，是的。\x01",
            "他们都是游击士哦。\x02\x03",
            "我现在要带他们\x01",
            "到我家里去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，果然是这样啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的名字叫做王。\x01",
            "是蔡斯支部所属的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我现在还是个新人，\x01",
            "和你们差不多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，是这样啊。\x01",
            "彼此彼此，多多关照哦。\x02\x03",
            "我是准游击士艾丝蒂尔。\x01",
            "旁边的那位是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我是约修亚，\x02\x03",
            "请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我之前听雾香说过\x01",
            "有关你们的事情。\x01",
            "果然来了很厉害的准游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说你们在全国各地\x01",
            "都做出了相当的成绩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F嘿嘿，就算是这样吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F说到成绩，\x01",
            "我们只是尽了自己的本分而已。\x02\x03",
            "而且多亏得到了游击士前辈\x01",
            "和各地百姓的鼎力相助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，\x01",
            "我觉得能够得到百姓信任，\x01",
            "得到他们的帮助也是一种才能呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "实际上，\x01",
            "我们支部也处于人手不足的状态。\x01",
            "我相当期待你们的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以后这段时间\x01",
            "还要请你们多多关照啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F还请以后多多指教。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6183")

    label("loc_611E")


    ChrTalk(
        0xFE,
        (
            "哟，艾丝蒂尔、约修亚。\x01",
            "我相当期待你们今后的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也许相处时间不会太长，\x01",
            "还要请你们多多关照啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6183")

    Jump("loc_62E5")

    label("loc_6186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_62E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_6231")

    ChrTalk(
        0xFE,
        (
            "是选平衡性呢，\x01",
            "还是选突出的特性呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，归根到底\x01",
            "还是要看使用者的本事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我大概还没有可以\x01",
            "选择武器的实力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62E5")

    label("loc_6231")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "唔，好难啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是选性能比较平衡的武器呢，\x01",
            "还是选非常有特点的武器呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是能二者兼顾的话，\x01",
            "就不用那么烦恼了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62E5")

    TalkEnd(0xFE)
    Return()

    # Function_17_56B8 end

    def Function_18_62E9(): pass

    label("Function_18_62E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6300")
    Call(0, 12)
    Jump("loc_6304")

    label("loc_6300")

    Call(0, 11)

    label("loc_6304")

    Return()

    # Function_18_62E9 end

    def Function_19_6305(): pass

    label("Function_19_6305")

    Call(0, 15)
    Return()

    # Function_19_6305 end

    def Function_20_630A(): pass

    label("Function_20_630A")

    EventBegin(0x0)
    OP_6D(2000, 0, -5200, 0)
    SetChrPos(0x101, 2400, 0, -5400, 0)
    SetChrPos(0x102, 1300, 0, -5500, 0)
    OP_4A(0x8, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        "#501F午安～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F打扰了。\x02",
    )

    CloseMessageWindow()

    def lambda_6381():
        OP_6D(3600, 0, 520, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6381)

    def lambda_6399():
        OP_8E(0xFE, 0xED8, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6399)
    Sleep(500)

    def lambda_63B9():
        OP_8E(0xFE, 0xBB8, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63B9)
    WaitChrThread(0x101, 0x1)

    NpcTalk(
        0x8,
        "东方打扮的女性",
        "#792F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F那个～我们是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "东方打扮的女性",
        (
            "#790F……总算到了。\x02\x03",
            "#790F艾丝蒂尔、约修亚。\x01",
            "欢迎来到蔡斯支部。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F您知道我们的事吗？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "东方打扮的女性",
        (
            "#792F卢安支部的嘉恩\x01",
            "已经和我联络过了。\x02\x03",
            "栗色的双马尾，\x01",
            "黑发和琥珀色的眼睛……\x02\x03",
            "#791F就是你们了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F原、原来如此……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "东方打扮的女性",
        (
            "#790F我叫雾香，\x01",
            "是蔡斯支部的负责人。\x02\x03",
            "以后就请多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F啊～嗯，彼此彼此！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请多指教。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F那么……虽然有点仓促，\x01",
            "我们还是先办理转属手续吧。\x02\x03",
            "请在这些文件上签字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚\x01",
            "在转属手续的文件上签了字。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#792F……这就可以了。\x02\x03",
            "#790F从今天开始，\x01",
            "你们就归蔡斯支部所属了……\x02\x03",
            "不过现在还没有\x01",
            "什么紧要的任务要去执行。\x02\x03",
            "你们就检查一下公告板，\x01",
            "以自己的步调来安排工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F稍微有点失望呢。\x01",
            "不过嘛，没什么紧要的事也是好事。\x02\x03",
            "#002F对了，雾香姐。\x01",
            "有一件事情想请问你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#792F是卡西乌斯先生的事吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F请问……\x01",
            "这也是从嘉恩先生那里听说的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F大致听说了。\x02\x03",
            "不过很可惜，\x01",
            "卡西乌斯先生不在蔡斯。\x02\x03",
            "也许是忙于紧要的公务吧，\x01",
            "他已经数月没到本支部来过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F啊，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F那剩下的只有王都了，又或者……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F不过关于另一件事，\x01",
            "倒有点线索可以提供给你们。\x02\x03",
            "这个拿去吧。\x02",
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
            "得到了\x07\x02",
            "给工房长的介绍信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x360, 1)

    ChrTalk(
        0x101,
        "#004F哎，这个是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F这是给中央工房的负责人\x01",
            "玛多克工房长的介绍信。\x02\x03",
            "他在蔡斯可是一位\x01",
            "地位有如市长般的人物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F难不成……\x01",
            "是关于黑色导力器的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F单从发生在市长官邸的事来看，\x01",
            "的确是相当神秘的东西。\x02\x03",
            "你们还是先去找\x01",
            "玛多克工房长商量一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F真、真是\x01",
            "准备得太周到了呢～\x02\x03",
            "雾香姐您难道有超能力？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F支援你们游击士\x01",
            "就是我的本职工作啊。\x02\x03",
            "只不过是根据得到的情报\x01",
            "做出相应的准备罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F劳、劳您费心了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F真是帮了大忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#791F不用客气。\x02\x03",
            "要是有什么事件发生的话，\x01",
            "可还是要麻烦你们俩回来工作哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊哈哈……\x01",
            "好！到时候就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F既然如此，\x01",
            "那我们马上去见工房长吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x53, 0x3, 0x2)
    OP_28(0x53, 0x3, 0x4)
    OP_28(0x3F, 0x4, 0x2)
    OP_28(0x3F, 0x4, 0x4)
    OP_28(0x3F, 0x1, 0x1)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_20_630A end

    def Function_21_6EDC(): pass

    label("Function_21_6EDC")

    EventBegin(0x0)
    OP_6D(1370, 0, -2580, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(345000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 760, 0, -4930, 0)
    SetChrPos(0x101, 1850, 0, -5150, 0)
    SetChrPos(0x107, 1150, 0, -5860, 0)
    SetChrPos(0x106, 2350, 0, -5930, 0)

    def lambda_6F65():

        label("loc_6F65")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6F65")

    QueueWorkItem2(0x101, 1, lambda_6F65)

    def lambda_6F76():

        label("loc_6F76")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6F76")

    QueueWorkItem2(0x102, 1, lambda_6F76)

    def lambda_6F87():

        label("loc_6F87")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6F87")

    QueueWorkItem2(0x106, 1, lambda_6F87)

    def lambda_6F98():

        label("loc_6F98")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6F98")

    QueueWorkItem2(0x107, 1, lambda_6F98)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 4070, 0, -700, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#790F#3P你们回来得正好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F您是……\x02",
    )

    CloseMessageWindow()

    def lambda_7021():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7021)
    Sleep(400)

    ChrTalk(
        0x9,
        (
            "#130F哎呀……\x01",
            "艾丝蒂尔、约修亚。\x02\x03",
            "好久不见了，你们还好吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_709E():
        OP_6D(3150, 0, -410, 1500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_709E)

    def lambda_70B6():
        OP_8E(0xFE, 0xBF4, 0x0, 0xFFFFF9D4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70B6)
    Sleep(100)

    def lambda_70D6():
        OP_8E(0xFE, 0x884, 0x0, 0xFFFFFB96, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_70D6)
    Sleep(50)

    def lambda_70F6():
        OP_8E(0xFE, 0xF82, 0x0, 0xFFFFF574, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_70F6)
    Sleep(100)

    def lambda_7116():
        OP_8E(0xFE, 0xA46, 0x0, 0xFFFFF542, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_7116)
    WaitChrThread(0x9, 0x2)

    ChrTalk(
        0x101,
        (
            "#501F这不是亚鲁瓦教授嘛。\x01",
            "你也到蔡斯来了啊。\x02\x03",
            "怎么，是来委托护卫工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F并不是这样的，\x01",
            "绑架犯的下落已经清楚了。\x02\x03",
            "这位先生就是目击者。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#054F什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#131F#2P嗯……\x01",
            "那果然不是普通事件啊。\x02\x03",
            "还好我及时赶来通报了。\x02\x03",
            "其实是这样的……\x01",
            "我刚才一直在塔里面做研究调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F说到塔……\x01",
            "又是『四轮之塔』的其中一个吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F蔡斯有塔的地方……\x01",
            "是在平原道北面的『红莲之塔』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#131F#2P嗯，没错。\x01",
            "我看到有几个军人进到塔里去了。\x02\x03",
            "起初我还以为王国军也对那塔有兴趣，\x01",
            "来做调查什么的……\x02\x03",
            "但不可思议的是……\x01",
            "我在角落里听到他们说什么绑架、\x01",
            "逃跑路线之类不对劲的话。\x02\x03",
            "我觉得这件事很不寻常，\x01",
            "所以就急急忙忙来这里通报了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F请问一下……\x01",
            "那些军人穿着什么样的服装？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#130F#2P唔，是以蓝白色为基调，\x01",
            "很华丽很端庄的王国军军服……\x02\x03",
            "不愧是女王陛下的国家，\x01",
            "连军人的衣着也如此体面潇洒。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x106, 0xFF)
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(
        0x106,
        (
            "#057F就此决定了……\x01",
            "快去『红莲之塔』吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_766C():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_766C)

    def lambda_767A():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_767A)

    ChrTalk(
        0x101,
        "#005F嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F明白了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F那、那个……\x02",
    )

    CloseMessageWindow()
    OP_44(0x106, 0xFF)
    OP_44(0x107, 0xFF)

    def lambda_76CE():
        OP_6D(3060, 0, -1580, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_76CE)

    def lambda_76E6():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76E6)

    def lambda_76F4():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_76F4)
    TurnDirection(0x106, 0x107, 400)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x107,
        (
            "#062F艾丝蒂尔姐姐，请你们……\x02\x03",
            "也、也带我一起去吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2P提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F#5P这可……\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x106)

    ChrTalk(
        0x106,
        "#050F喂喂，小不点。\x02",
    )

    CloseMessageWindow()
    OP_44(0x107, 0xFF)
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(
        0x107,
        "#065F哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F我说啊……\x01",
            "我们不可能带你去的。\x02\x03",
            "用常识想想，常识啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F但、但是但是……！\x02\x03",
            "爷爷他被掳走了呢，\x01",
            "我……我……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F没时间了，\x01",
            "我就跟你直说好了……\x02\x03",
            "#057F你是个累赘，不要跟来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F……！\x02",
    )

    OP_9E(0x107, 0xF, 0x0, 0x12C, 0xFA0)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(
        0x101,
        (
            "#005F等、等一下！\x01",
            "这样说也太过分了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F闭嘴。\x01",
            "你也应该很清楚。\x02\x03",
            "她是个外行人，而且又是个小鬼，\x01",
            "我们哪有余闲来照顾她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F这、这个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 600)

    ChrTalk(
        0x101,
        "#009F约修亚，你也说点什么啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F很遗憾……我也反对。\x02\x03",
            "那些黑衣人行事几乎毫无破绽，\x01",
            "追击的困难大家可想而知。\x02\x03",
            "为了安全起见，\x01",
            "我不赞同带提妲去那么危险的地方。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x107,
        "#065F约、约修亚哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F呜～……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        (
            "#003F……抱歉，提妲。\x01",
            "看来还是不能带你去……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        "#065F艾、艾丝蒂尔姐姐也……\x02",
    )

    CloseMessageWindow()
    OP_9E(0x107, 0x14, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x107,
        "#069F……过分……好过分……\x02",
    )

    CloseMessageWindow()

    def lambda_7BFF():

        label("loc_7BFF")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_7BFF")

    QueueWorkItem2(0x101, 1, lambda_7BFF)

    def lambda_7C10():

        label("loc_7C10")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_7C10")

    QueueWorkItem2(0x102, 1, lambda_7C10)

    def lambda_7C21():

        label("loc_7C21")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_7C21")

    QueueWorkItem2(0x106, 1, lambda_7C21)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x107, 225, 800)

    def lambda_7C4B():
        OP_6D(2320, 0, -1650, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7C4B)
    OP_8E(0x107, 0x6C2, 0x0, 0xFFFFEDFE, 0x1388, 0x0)
    OP_8E(0x107, 0x5F0, 0x0, 0xFFFFE87C, 0x1388, 0x0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(100)
    OP_8E(0x107, 0x6F4, 0x0, 0xFFFFE160, 0x1388, 0x0)
    SetChrFlags(0x107, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)

    ChrTalk(
        0x101,
        "#004F提妲！\x02",
    )

    CloseMessageWindow()

    def lambda_7CCA():
        OP_8E(0xFE, 0x924, 0x0, 0xFFFFF57E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7CCA)
    Sleep(50)
    OP_8E(0x102, 0x8FC, 0x0, 0xFFFFF8E4, 0xFA0, 0x0)

    def lambda_7CFE():
        OP_8F(0xFE, 0x924, 0x0, 0xFFFFF57E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7CFE)

    def lambda_7D19():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D19)

    def lambda_7D27():

        label("loc_7D27")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_7D27")

    QueueWorkItem2(0x102, 1, lambda_7D27)

    ChrTalk(
        0x102,
        (
            "#012F等等，艾丝蒂尔。\x02\x03",
            "#015F现在就任她去吧……\x02\x03",
            "我们得尽快救出博士，\x01",
            "让她能早点安心才是。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F知道了……\x01",
            "也许这也是为了她好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F真是的……\x01",
            "又浪费了这么多时间。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7E0C():
        OP_6D(3150, 0, -410, 1000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7E0C)
    TurnDirection(0x106, 0x8, 400)

    def lambda_7E2B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E2B)
    Sleep(50)

    def lambda_7E3E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E3E)
    WaitChrThread(0x9, 0x2)

    ChrTalk(
        0x106,
        (
            "#054F雾香。\x01",
            "和军队的联络就麻烦你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F嗯嗯。\x01",
            "祝你们成功。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#131F#2P哎呀哎呀……\x01",
            "看来发生了不得了的大事呢。\x02\x03",
            "请各位务必小心。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 1570, 0, -3490, 180)
    SetChrPos(0x102, 1570, 0, -3490, 180)
    SetChrPos(0x106, 1570, 0, -3490, 180)
    OP_6D(1570, 0, -3490, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_8C(0x9, 0, 400)
    Sleep(500)
    FadeToBright(1000, 0)
    SetChrPos(0x107, 720, 0, -2310, 0)
    OP_28(0x41, 0x1, 0x100)
    OP_28(0x41, 0x1, 0x200)
    RemoveParty(0x6, 0xFF)
    EventEnd(0x0)
    Return()

    # Function_21_6EDC end

    def Function_22_7FCC(): pass

    label("Function_22_7FCC")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(2000, 0, -5200, 0)
    OP_4A(0x8, 255)
    OP_4A(0xA, 0)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, 1440, 0, -6280, 0)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x101, 2400, 0, -5400, 0)
    SetChrPos(0x102, 1300, 0, -5500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#001F雾香姐，早啊～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好。\x02",
    )

    CloseMessageWindow()

    def lambda_806C():
        OP_6D(3600, 0, 600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_806C)

    def lambda_8084():
        OP_8E(0xFE, 0xED8, 0x0, 0xFFFFFD44, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8084)
    Sleep(300)

    def lambda_80A4():
        OP_8E(0xFE, 0xBB8, 0x0, 0xFFFFFD44, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_80A4)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x8,
        (
            "#790F早啊，你们俩。\x02\x03",
            "金已经出发了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是的。\x01",
            "刚才乘定期船飞去王都了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F说起来，\x01",
            "雾香姐怎么没一起送行啊？\x02\x03",
            "还有还有……\x01",
            "雾香姐是怎么和金先生认识的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F都是些陈年往事了。\x02\x03",
            "#790F别说这些了……\x01",
            "事情好像变得迷雾重重了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#507F啊～雾香姐害羞了！\x02\x03",
            "#004F对了，迷雾重重是指……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F难道说……\x01",
            "已经查到了那艘飞艇的线索？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F不，目前还没有消息。\x02\x03",
            "迷雾重重是指王国军最近的动向。\x01",
            "　\x02\x03",
            "首先，\x01",
            "我联络过雷斯顿要塞的军方司令部，\x01",
            "但至今仍未得到任何的回音。\x02\x03",
            "接着，\x01",
            "设在各地的盘查在昨晚撤除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F咦！？\x01",
            "这是怎么回事？\x02\x03",
            "他们又打算像空贼事件时那样\x01",
            "和我们游击士协会抢功吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F不，那样的话，\x01",
            "解除盘查岂不适得其反。\x02\x03",
            "如果他们自己抓到了犯人，\x01",
            "应该会马上联络这里的……\x02\x03",
            "#012F的确是迷雾重重啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F而且最近这段时间，\x01",
            "我和雷斯顿要塞的情报部也联络不上。\x02\x03",
            "说不定王国军的内部\x01",
            "发生了什么不可告人的大事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F什么事……\x01",
            "#004F啊，难道是……！\x02\x03",
            "朵洛希拍到的……那个！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯……\x01",
            "换装成亲卫队的黑衣人的照片。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, 1440, 0, -6280, 0)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x80)
    OP_22(0x6, 0x0, 0x64)

    ChrTalk(
        0xA,
        "#2P在说我吗～？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_8729():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8729)

    def lambda_8737():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8737)
    OP_6D(2680, 0, -3240, 1500)

    ChrTalk(
        0x101,
        "#501F啊，朵洛希！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F真是说人人到啊。\x02",
    )

    CloseMessageWindow()

    def lambda_8799():
        OP_6D(3300, 0, -730, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8799)

    def lambda_87B1():

        label("loc_87B1")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_87B1")

    QueueWorkItem2(0x8, 1, lambda_87B1)

    def lambda_87C2():

        label("loc_87C2")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_87C2")

    QueueWorkItem2(0x101, 1, lambda_87C2)

    def lambda_87D3():

        label("loc_87D3")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_87D3")

    QueueWorkItem2(0x102, 1, lambda_87D3)
    OP_8E(0xA, 0xECE, 0x0, 0xFFFFF6FA, 0xBB8, 0x0)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "#152F哎呀～这次糟了啊。\x02\x03",
            "之前我联络编辑部的时候，\x01",
            "正好碰上了奈尔前辈。\x02\x03",
            "他知道我把那东西交给他们之后，\x01",
            "就不由分说地对我大发脾气。\x01",
            "还叫我无论如何都要把东西要回来。\x02\x03",
            "他们真的好过分呢～你们说是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F你的意思是说……\x01",
            "王国军还没把感光结晶回路还给你吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#154F嗯，你们也觉得过分吧～？\x02\x03",
            "他们就是不还给我，\x01",
            "所以我就特地跑到要塞去要呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F哇哈～\x01",
            "你还真有毅力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#151F嘿嘿～\x01",
            "我也就只有这个优点嘛。\x02\x03",
            "实在没办法之下，\x01",
            "我唯有拍了些要塞的照片给杂志充数。\x02\x03",
            "嘿嘿～用探照灯打光，\x01",
            "拍出来的照片可是十分可爱的哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#509F把要塞拍得十分可爱做什么用？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F没得到许可就随便拍摄军事设施，\x01",
            "这样是不是不太好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#151F没事没事。\x01",
            "别说那么死板的话嘛㈱\x02\x03",
            "给，看啦看啦。\x01",
            "照片刚刚才洗出来的哦～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8C06():
        OP_6D(3600, 0, 600, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8C06)
    OP_8E(0xA, 0x1220, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xA, 0x1234, 0x0, 0xFFFFFD3A, 0x7D0, 0x0)
    OP_8C(0x101, 45, 0)
    Sleep(500)
    OP_8C(0x101, 45, 0)
    OP_8C(0x102, 45, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "朵洛希把雷斯顿要塞的照片放在柜台上。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AD(0x40024, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#010F哦……\x01",
            "拍得的确很漂亮啊。\x02\x03",
            "#010F这就是雷斯顿要塞吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            "#006F朵洛希真的很会拍照……\x01",
            "　\x02\x03",
            "#004F………………咦咦………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        "#014F怎么了，艾丝蒂尔？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            "#505F是心理作用吗……\x01",
            "右上方好像有什么东西……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#014F咦……\x02\x03",
            "#012F…………真的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 250, -1, -1)
    SetChrName("雾香")

    AnonymousTalk(
        (
            "#790F虽然很模糊，\x01",
            "但还真的有个很小的影子呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("朵洛希")

    AnonymousTalk(
        (
            "#153F哎～\x01",
            "艾丝蒂尔看得好仔细啊。\x02\x03",
            "#153F我呢我呢，\x01",
            "拍的时候一点都没发觉呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 400, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            "#502F嘿嘿，多谢夸奖⊙\x02\x03",
            "#000F虽然只看到轮廓，\x01",
            "不过应该是军队的警备飞艇吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#012F不……\x01",
            "这不是警备飞艇……\x02\x03",
            "#012F是那时候的飞艇。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 400, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        "#004F那时候……？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 250, -1, -1)
    SetChrName("雾香")

    AnonymousTalk(
        (
            "#792F和黑衣人绑架博士时乘的飞艇\x01",
            "是一模一样的轮廓吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        "#013F是的。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x5DC)
    SetMessageWindowPos(150, 400, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            "#505F绑架博士时乘的飞艇……\x01",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_1D(0x56)
    SetMessageWindowPos(150, 400, -1, -1)

    AnonymousTalk(
        "#004F#5S咦咦咦咦咦！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_44(0x8, 0xFF)
    OP_8C(0x8, 180, 0)
    OP_8C(0xA, 270, 0)
    TurnDirection(0x101, 0x102, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#005F等、等一下！\x02\x03",
            "为什么那艘飞艇会出现在这种地方！？\x01",
            "　\x02\x03",
            "太不可思议了！\x01",
            "这里可是王国军的根据地啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015F冷静点，艾丝蒂尔。\x02\x03",
            "虽然有各种可能的情况，\x01",
            "但现在就下结论的话还是太早了。\x02\x03",
            "#012F依现在的情况，\x01",
            "我们应该直接前往雷斯顿要塞，\x01",
            "当面询问他们飞艇的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F原来如此，\x01",
            "打算去试探一下吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_932D():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_932D)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        "#012F这样做不行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F不会，我许可。\x02\x03",
            "不管怎样，\x01",
            "我们这里可是差点有人丧命。\x02\x03",
            "无论有什么原因，\x01",
            "都不能让王国军的人看不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呜哇，雾香姐，\x01",
            "眼神突然变得凌厉了……\x02\x03",
            "#002F不过……确实是这样呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_94A1():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_94A1)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        (
            "#002F朵洛希，\x01",
            "这照片能给我们一张吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150F嗯，没问题～\x02\x03",
            "嘿嘿～毕竟我一直都\x01",
            "受过小艾你们不少的关照嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F谢谢，欠你个人情了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "朵洛希拍的照片\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x358, 1)

    ChrTalk(
        0x8,
        (
            "#790F要去雷斯顿要塞的话，\x01",
            "首先从东面的门口出到利塔街道。\x02\x03",
            "#790F然后在利塔街道途中的三岔路向北走，\x01",
            "这样你们就能到达雷斯顿要塞了。\x02\x03",
            "请务必谨慎行动。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_96DB():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_96DB)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#006FＯＫ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F明白了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x43, 0x4, 0x2)
    OP_28(0x43, 0x4, 0x4)
    OP_28(0x43, 0x1, 0x1)
    OP_28(0x33, 0x4, 0x40)
    OP_4B(0xA, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_20(0x3E8)
    EventEnd(0x0)
    OP_1D(0xD)
    Return()

    # Function_22_7FCC end

    def Function_23_9742(): pass

    label("Function_23_9742")

    EventBegin(0x0)
    OP_6D(3230, 0, 280, 0)
    AddParty(0x6, 0xFF)
    AddParty(0x5, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 4500, 0, -720, 270)
    SetChrPos(0x101, 3500, 0, -710, 90)
    SetChrPos(0x102, 2390, 0, -700, 90)
    SetChrPos(0x106, 1750, 0, -6420, 0)
    SetChrPos(0x107, 680, 0, -6020, 0)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#805F拉、拉赛尔博士\x01",
            "被囚禁在雷斯顿要塞里……\x02\x03",
            "你们真的肯定吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F朵洛希小姐拍的照片\x01",
            "和大门前发生的导力停止现象。\x02\x03",
            "将以上两者联系起来，\x01",
            "这样的判断应该没错的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#805F但、但是中央工房和王国军\x01",
            "有着多年的友好合作关系。\x02\x03",
            "实在无法接受他们会做出如此……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F虽说王国军都听令于女王，\x01",
            "但也难保其内部一定坚如磐石。\x02\x03",
            "袭击工房的犯人逃走时\x01",
            "故意换装成王室亲卫队的样子，\x01",
            "很有可能是出于某种政治上的目的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A38():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9A38)

    def lambda_9A46():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9A46)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#505F哎，你的意思是……\x02",
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
            "「亲卫队和这些事件无关吗？」\x01",        # 0
            "「还是说亲卫队就是幕后主谋？」\x01",      # 1
            "「亲卫队是被别人栽赃的？」\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9B62"),
        (1, "loc_9C8F"),
        (2, "loc_9DA0"),
        (SWITCH_DEFAULT, "loc_9E3F"),
    )


    label("loc_9B62")


    ChrTalk(
        0x101,
        "#004F亲卫队和这些事件无关吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯，就是这样。\x01",
            "我认为他们和事件没有任何关系。\x02\x03",
            "从犯人的犯案手法来看，\x01",
            "亲卫队极有可能是被别人栽赃的。\x02\x03",
            "如果我没猜错的话……\x01",
            "军队内部有什么阴谋正在进行着。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x43, 0x1)
    Jump("loc_9E3F")

    label("loc_9C8F")


    ChrTalk(
        0x101,
        "#004F还是说亲卫队就是幕后主谋？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F唔……\x01",
            "不排除有幕后主谋的可能性。\x02\x03",
            "#012F不过幕后主谋另有其人，\x01",
            "亲卫队极有可能是被别人栽赃的。\x02\x03",
            "如果我没猜错的话……\x01",
            "军队内部有什么阴谋正在进行着。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E3F")

    label("loc_9DA0")


    ChrTalk(
        0x101,
        (
            "#004F难道说……\x01",
            "亲卫队是被别人栽赃的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯，我的想法和你一样。\x01",
            "幕后主谋根本不是王室亲卫队。\x02\x03",
            "如果我没猜错的话……\x01",
            "军队内部有什么阴谋正在进行着。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x43, 0x3)
    Jump("loc_9E3F")

    label("loc_9E3F")


    ChrTalk(
        0xB,
        (
            "#806F唔……是这样吗……\x02\x03",
            "但是，为什么他们\x01",
            "会把博士也卷进这个阴谋里呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(100)

    ChrTalk(
        0x106,
        (
            "#2P……看来你们找到了\x01",
            "绑架博士的那帮犯人的线索吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)

    def lambda_9F56():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9F56)

    def lambda_9F64():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F64)

    def lambda_9F72():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9F72)

    def lambda_9F80():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9F80)

    def lambda_9F8E():
        OP_6D(2020, 0, -2230, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9F8E)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        "#501F哎，阿加特！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F太好了……\x01",
            "阿加特兄你总算醒来了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9FF1():
        OP_6D(2920, 0, -480, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9FF1)

    def lambda_A009():

        label("loc_A009")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_A009")

    QueueWorkItem2(0xB, 1, lambda_A009)

    def lambda_A01A():

        label("loc_A01A")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_A01A")

    QueueWorkItem2(0x101, 1, lambda_A01A)

    def lambda_A02B():

        label("loc_A02B")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_A02B")

    QueueWorkItem2(0x102, 1, lambda_A02B)

    def lambda_A03C():
        OP_8E(0xFE, 0xDD4, 0x0, 0xFFFFF8B2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_A03C)
    Sleep(300)

    def lambda_A05C():
        OP_8E(0xFE, 0x988, 0x0, 0xFFFFF920, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A05C)
    WaitChrThread(0x106, 0x1)
    TurnDirection(0x106, 0x101, 400)
    WaitChrThread(0x107, 0x1)
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x106,
        (
            "#552F啊，刚刚才醒。\x02\x03",
            "起来后发现睡在不认识的地方，\x01",
            "真是吓了一跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#2P真是的……\x01",
            "这两天大家都很担心你啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过才刚刚醒来，\x01",
            "这样到处走动不会有问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F哈哈，\x01",
            "睡多了身体反而变得僵硬。\x02\x03",
            "还是要尽情地运动才会健康嘛。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(
        0x107,
        (
            "#065F#1P但、但是，阿加特大哥哥。\x01",
            "太勉强的话是不行的哦。\x02\x03",
            "身上的毒才刚刚清除，\x01",
            "医生说要再静养一段时间……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)

    ChrTalk(
        0x106,
        (
            "#551F好啦好啦。\x01",
            "我不是都说了没事嘛。\x02\x03",
            "我可是和你们不一样，知道吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#069F#1P呜……\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x106,
        (
            "#055F哎呀……\x01",
            "知道了，知道了啦！\x02\x03",
            "反正在伤势康复之前不会乱来，\x01",
            "这样总成了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F#1P嘿嘿……好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F真是的……\x01",
            "所以我就说小鬼是最……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#2P啊哈哈。\x01",
            "连阿加特也拿提妲没办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F因为受伤的时候是提妲一直在照顾着，\x01",
            "既然阿加特兄受了人家的恩惠，\x01",
            "那么以后说话不客气也不行啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(
        0x106,
        (
            "#551F啊～够了，真啰嗦。\x02\x03",
            "#051F不过在我休息的时候，\x01",
            "绑架事件有了很多新的进展吧。\x02\x03",
            "说给我听听吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#2P嗯，好的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们告诉阿加特\x01",
            "拉赛尔博士很有可能被捉到雷斯顿要塞的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x107,
        (
            "#065F爷、爷爷他竟然\x01",
            "被那些坏人捉到那里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F那些黑衣人竟然和军队有关系……\x01",
            "　\x02\x03",
            "#053F哼……\x01",
            "总算弄清他们的真面目了。\x02\x03",
            "看来事情也该做个了结了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#2P做个了结？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F这还用我说吗。\x01",
            "潜入雷斯顿要塞将事情解决掉。\x02\x03",
            "不仅要救出博士，\x01",
            "还要把那些家伙一网打尽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P啊，原来是这样啊。\x01",
            "看来这是最直截了当的方法呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#790F没那么简单。\x02",
    )

    CloseMessageWindow()

    def lambda_A83B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A83B)

    def lambda_A849():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A849)

    def lambda_A857():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A857)

    def lambda_A865():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A865)
    Sleep(500)

    ChrTalk(
        0x101,
        "#004F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F游击士协会的规约里有一条\x01",
            "决不干涉各国军队内政的原则。\x02\x03",
            "协会规约第三项。\x01",
            "『不对国家主权进行干涉』……\x02\x03",
            "『游击士不可对\x01",
            "　国家授权或认可的公共机关\x01",
            "　行使任何的搜查权及逮捕权。』\x02\x03",
            "#790F就是说，只要军队不认帐，\x01",
            "我们就没有权力对其进行调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#552F嘁，忘了还有这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F怎、怎么会……\x01",
            "这样太不合理了吧！\x02\x03",
            "明明看到他们做了那么多坏事，\x01",
            "难道就这样放过吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#791F不过……\x01",
            "这个规约也有空子可钻。\x02\x03",
            "协会规约第二项。\x01",
            "『对于平民有保护义务』。\x02\x03",
            "『当在平民的生命及权利\x01",
            "　受到不正当威胁或侵犯的情况下，\x01",
            "　游击士有保护他们的义务和责任。』\x02\x03",
            "#792F明白这是什么意思了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x01",
            "博士既不是佣兵也不是军人。\x02\x03",
            "只是一个受保护的平民。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F这、这么说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F接下来……\x01",
            "就要看工房长先生您了。\x02\x03",
            "这件事很可能\x01",
            "引发中央工房与王国军的对立，\x01",
            "即使这样，也要救出拉赛尔博士吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AD82():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD82)

    def lambda_AD90():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD90)

    def lambda_AD9E():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_AD9E)
    TurnDirection(0x107, 0xB, 400)

    ChrTalk(
        0xB,
        (
            "#803F……这根本不用考虑。\x02\x03",
            "博士对于中央工房……\x01",
            "不，对于整个利贝尔来说\x01",
            "是个百年难得一遇的优秀人才。\x02\x03",
            "#800F我在此委托你们营救他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F#1P工房长叔叔……！\x01",
            "真、真是太感谢您了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x107, 400)

    ChrTalk(
        0xB,
        (
            "#801F不用道什么谢啦。\x01",
            "博士也是我的恩师啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F这样我们就有合适的理由了。\x02\x03",
            "游击士阿加特，\x01",
            "还有艾丝蒂尔和约修亚。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AF18():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AF18)

    def lambda_AF26():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF26)

    def lambda_AF34():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF34)

    def lambda_AF42():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_AF42)

    def lambda_AF50():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AF50)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#791F现委托你们前往营救\x01",
            "被捉到雷斯顿要塞的拉赛尔博士。\x01",
            "　\x02\x03",
            "虽然程序不是很正规，\x01",
            "但这是游击士协会的正式委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F这样才对嘛！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F哼，正合我意。\x02\x03",
            "既然决定了，\x01",
            "就有必要策划一下潜入方法。\x02\x03",
            "不管怎样，雷斯顿要塞\x01",
            "毕竟是个以无坚不摧而著称的基地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F的确如此。\x01",
            "那里的警戒体制相当严密。\x02\x03",
            "如果有可行的潜入路线图就好了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F很遗憾……\x01",
            "那里的警戒体制可以说是接近完美。\x02\x03",
            "要塞周围散布了导力传感器，\x01",
            "就算从湖的方向潜入也相当困难。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F哼……\x01",
            "我就知道没那么容易了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F正面突破很难成功啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(
        0x101,
        (
            "#501F#2P说起来，工房长先生。\x02\x03",
            "那艘橙色的飞艇\x01",
            "不是去过雷斯顿要塞吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B359():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B359)

    def lambda_B367():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B367)

    def lambda_B375():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B375)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "#802F啊啊……\x01",
            "你说工房船『莱普尼兹号』吗。\x02\x03",
            "我们的确是要定期向要塞\x01",
            "运送材料和检查设备……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P那么那么，\x01",
            "我们藏在里面潜入要塞不就行了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#805F不可能，飞艇一降落到基地，\x01",
            "机上的所有人员都要接受严密的检查。\x02\x03",
            "想任意行动几乎不可能……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F难道说……\x01",
            "躲在货物里也行不通？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#800F嗯，他们会用生命感应器\x01",
            "逐一检查运来的所有箱子。\x02\x03",
            "那个生命感应器也是\x01",
            "拉赛尔博士发明的东西。\x02\x03",
            "是连一只老鼠也不会放过的先进机器啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#2P唉～还是不行啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x107,
        "#064F……啊…………！\x02",
    )

    CloseMessageWindow()

    def lambda_B65B():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B65B)

    def lambda_B669():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B669)

    def lambda_B677():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B677)

    ChrTalk(
        0x101,
        "#002F#2P咦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F艾丝蒂尔姐姐，你还记得吗！？\x02\x03",
            "那天姐姐你们来我家时\x01",
            "爷爷刚做好的那个新发明啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#2P我们来你家的时候……\x02\x03",
            "#004F……啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我想起来了……\x01",
            "是我们也帮忙做实验的那个导力器？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F嗯，就是那个！\x02\x03",
            "那个装置能产生\x01",
            "阻碍生命感应器扫描的导力场。\x02\x03",
            "启动测试也做过了。\x01",
            "没问题的……肯定可以帮上忙的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#054F什么……真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#803F那个博士也真是的，\x01",
            "什么时候做了这种东西……\x02\x03",
            "#800F那个装置现在在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊，我想应该是\x01",
            "放在研究室的某个地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#791F那么你们快去把那个装置取来。\x01",
            "　\x02\x03",
            "我会在这段时间里准备好\x01",
            "有关雷斯顿要塞的详细资料。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(
        0x106,
        "#051F好的，拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#791F工房长先生，\x01",
            "工房船的准备就拜托您了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 400)

    ChrTalk(
        0xB,
        (
            "#804F明、明白了。\x01",
            "我马上和格斯塔夫维修长商量。\x02\x03",
            "你们准备完了就到飞艇坪来吧！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x43, 0x1, 0x20)
    OP_28(0x43, 0x1, 0x40)

    def lambda_BA68():

        label("loc_BA68")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_BA68")

    QueueWorkItem2(0x101, 1, lambda_BA68)

    def lambda_BA79():

        label("loc_BA79")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_BA79")

    QueueWorkItem2(0x102, 1, lambda_BA79)

    def lambda_BA8A():

        label("loc_BA8A")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_BA8A")

    QueueWorkItem2(0x106, 1, lambda_BA8A)

    def lambda_BA9B():

        label("loc_BA9B")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_BA9B")

    QueueWorkItem2(0x107, 1, lambda_BA9B)
    OP_8C(0xB, 180, 400)
    OP_8E(0xB, 0x114E, 0x0, 0xFFFFF4AC, 0xFA0, 0x0)
    OP_8E(0xB, 0x65E, 0x0, 0xFFFFE80E, 0xFA0, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_BAE0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BAE0)
    OP_8E(0xB, 0x6F4, 0x0, 0xFFFFE1BA, 0xFA0, 0x0)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0xB, 0x4)
    OP_8E(0xB, 0x780, 0xFFFFFE0C, 0xFFFFDBB6, 0xFA0, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_23_9742 end

    def Function_24_BB35(): pass

    label("Function_24_BB35")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    SetChrPos(0x101, 1520, 0, -4610, 0)
    SetChrPos(0x102, 2390, 0, -5240, 0)
    SetChrPos(0x106, 640, 0, -5220, 0)
    SetChrPos(0x107, 1640, 0, -5990, 0)
    OP_4A(0x8, 255)
    OP_6D(2370, 0, -2250, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#006F雾香姐。\x01",
            "那个装置拿到了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BBDB():
        OP_6D(3130, 0, 650, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BBDB)

    def lambda_BBF3():
        OP_8E(0xFE, 0xE2E, 0x0, 0xFFFFFD1C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BBF3)
    Sleep(300)

    def lambda_BC13():
        OP_8E(0xFE, 0x104A, 0x0, 0xFFFFF916, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BC13)
    Sleep(300)

    def lambda_BC33():
        OP_8E(0xFE, 0xB04, 0x0, 0xFFFFFA92, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_BC33)
    Sleep(300)

    def lambda_BC53():
        OP_8E(0xFE, 0xC30, 0x0, 0xFFFFF6DC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_BC53)

    def lambda_BC6E():

        label("loc_BC6E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_BC6E")

    QueueWorkItem2(0x101, 1, lambda_BC6E)

    def lambda_BC7F():

        label("loc_BC7F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_BC7F")

    QueueWorkItem2(0x102, 1, lambda_BC7F)

    def lambda_BC90():

        label("loc_BC90")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_BC90")

    QueueWorkItem2(0x107, 1, lambda_BC90)

    def lambda_BCA1():

        label("loc_BCA1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_BCA1")

    QueueWorkItem2(0x106, 1, lambda_BCA1)
    WaitChrThread(0x106, 0x2)

    ChrTalk(
        0x8,
        (
            "#790F我这里也准备好了。\x02\x03",
            "顺带一提，\x01",
            "这些资料绝对不能向他人外传。\x02",
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
            "得到了\x07\x02",
            "雷斯顿要塞概略图\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x359, 1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_AD(0x40025, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#051F哈哈……\x01",
            "竟然有这么好的东西啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#014F这个是……\x01",
            "雷斯顿要塞的简略图吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 350, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(
        (
            "#064F哇……\x01",
            "好大好厉害啊。\x02\x03",
            "#062F爷爷会在哪儿呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            "#509F我说……\x01",
            "这东西不是军事机密吗？\x02\x03",
            "为什么协会会有这张地图？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 0, -1, -1)
    SetChrName("雾香")

    AnonymousTalk(
        (
            "#792F正所谓蛇行蛇道。\x01",
            "任何组织都会有其独特的门路。\x02\x03",
            "#790F你们只要记住，\x01",
            "游击士协会也有这样一面就行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        "#004F嗯、嗯……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#790F不必我多说，\x01",
            "大家也知道这次情况相当特殊。\x02\x03",
            "与其他国家相比起来，\x01",
            "王国军和协会一向保持着良好的关系。\x02\x03",
            "为了不留下任何瑕疵，\x01",
            "记住要尽量避免和士兵交战。\x02\x03",
            "特别是阿加特……明白吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F哼，真没办法。\x02\x03",
            "#057F不过，要是那帮黑衣人来碍事的话，\x01",
            "我肯定决不会手软。\x02\x03",
            "管他们是军人还是什么，\x01",
            "总之干了坏事就是犯罪者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F那些就随你便吧。\x01",
            "不过切记不能太过硬来。\x02\x03",
            "#792F艾丝蒂尔、约修亚。\x02\x03",
            "本来按道理是不能安排\x01",
            "你们准游击士做这种任务的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F等、等一下！\x01",
            "游击士的地位和那无关吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F既然走到了这一步，\x01",
            "就请让我们继续做下去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#791F……就知道你们会这么说，\x01",
            "所以我也不会阻拦你们了。\x02\x03",
            "顺带一提，\x01",
            "你们是在蔡斯支部的监督之下。\x02\x03",
            "有什么责任就由我来承担，\x01",
            "所以你们尽管放心好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F雾、雾香姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F不好意思……\x01",
            "这次真的给您添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F还有……提妲。\x02\x03",
            "你并非游击士，\x01",
            "其实本不该这么问你的……\x02\x03",
            "你真的下定决心了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064F啊……\x02\x03",
            "#062F……是！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C5A8():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C5A8)

    def lambda_C5B6():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C5B6)

    def lambda_C5C4():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C5C4)
    OP_6D(3240, 0, -550, 1000)

    ChrTalk(
        0x101,
        (
            "#004F#2P咦、咦？\x01",
            "这是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F难道说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F那、那个……\x02\x03",
            "能够操作这个感应干扰器的人\x01",
            "也许只有我一个。\x02\x03",
            "所以……\x01",
            "我也要和姐姐你们一起去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2P咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F如此构造复杂的导力器，\x01",
            "凭我们的确是无法正确使用……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#562F对不起……\x02\x03",
            "我、我一定不会\x01",
            "再给姐姐你们添麻烦的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#552F#5P……开什么玩笑。\x02",
    )

    CloseMessageWindow()

    def lambda_C756():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C756)

    def lambda_C764():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C764)
    TurnDirection(0x107, 0x106, 400)
    Sleep(400)

    ChrTalk(
        0x106,
        (
            "#057F#5P喂，小不点……\x01",
            "我可没听说过这种事……\x02\x03",
            "这么危险的任务，\x01",
            "怎可能带你这种小鬼去啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F但、但是但是……\x02\x03",
            "如果我不去的话，\x01",
            "这个装置就运作不了的呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#054F#5P那就不用这种方法好了！\x01",
            "不用了！\x02\x03",
            "我们找别的潜入方法！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#2P…………………………\x02\x03",
            "#007F我说阿加特啊，\x01",
            "你就不会稍微变通一下吗？\x02\x03",
            "怎么老是那么意气用事啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x102, 400)

    ChrTalk(
        0x106,
        "#055F#5P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#2P提妲她可是已经有所觉悟，\x01",
            "才会说要帮我们的啊。\x02\x03",
            "有了她的帮忙，\x01",
            "我们的潜入行动也会容易许多。\x02\x03",
            "而且救出博士的成功率\x01",
            "也肯定会高很多对吧？\x02\x03",
            "既然这样的话，\x01",
            "你还有什么理由去反对呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F#5P你……\x02\x03",
            "你打算让一个平民置身险境吗？\x01",
            "要知道她还是个小孩子！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P我也不想让她有危险，\x01",
            "但我们可以好好地保护她啊。\x02\x03",
            "而且这也是游击士的义务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F#5P哼……\x02\x03",
            "明明还是个经验浅薄的新人，\x01",
            "还敢摆出这么一副老练的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F……我们的确是新人，\x01",
            "但我认为这和辈分没什么关系。\x02\x03",
            "保护身边重要的人这种心情，\x01",
            "也并非游击士所专有的。\x02\x03",
            "#010F倒不如说，\x01",
            "这种心情才正是我们工作的动力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#057F#5P……………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#065F艾丝蒂尔姐姐、约修亚哥哥……\x02\x03",
            "#562F还有阿加特大哥哥。\x01",
            "对不起呢，大家为了我的事操心……\x02\x03",
            "但是但是，\x01",
            "爷爷对我来说真的很重要……\x02\x03",
            "无论如何，我都想去救他……\x02\x03",
            "所以呢……\x01",
            "我真的很想尽自己所能来帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#552F#5P……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F阿加特大哥哥昨天救了我……\x01",
            "而且他还教导了我，鼓励了我……\x02\x03",
            "所以呢，我也希望能为大家做点事情。\x01",
            "我知道自己帮不上什么忙……\x01",
            "但是，就算能帮上那么的一点点也好。\x02\x03",
            "我绝对不是在勉强自己……\x01",
            "因为我知道自己现在的心情……\x02\x03",
            "#068F所以……求求你们了……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#2P提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是这样啊……\x01",
            "你真是个会为人着想的好孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#053F#5P………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)

    ChrTalk(
        0x106,
        (
            "#057F#5P哼，都不知道你在说什么。\x02\x03",
            "要知道你自己是多么的碍事。\x01",
            "叫你别跟来也是为了你好。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(
        0x107,
        "#562F呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F#5P不过在没有其他潜入方法的情况下……\x01",
            "　\x02\x03",
            "真没办法……\x02\x03",
            "#053F既然如此，\x01",
            "这次就破例允许你跟我们去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊……\x02\x03",
            "#067F谢谢你，阿加特大哥哥！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F#5P不用道谢。\x02\x03",
            "要是你再碍事的话，\x01",
            "我会毫不留情地丢下你不管哦。\x02\x03",
            "做好心理准备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560F是、是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#2P真是的……\x01",
            "老是装模作样地闹别扭。\x02\x03",
            "就不会老老实实接受人家的心意吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F算了算了，艾丝蒂尔。\x02\x03",
            "阿加特兄是为了隐藏心中的羞涩\x01",
            "才会装得那么严肃嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x102, 400)

    ChrTalk(
        0x106,
        "#055F#5P吵、吵死了，你们两个家伙！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F嘻嘻……\x02",
    )

    CloseMessageWindow()

    def lambda_D1C2():
        OP_6D(3130, 0, 650, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D1C2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x8,
        (
            "#792F呵呵……\x01",
            "意见一致就没问题了。\x02\x03",
            "#791F工房船也差不多该安排好了。\x01",
            "　\x02\x03",
            "你们准备好的话，\x01",
            "可以随时动身前往飞艇坪。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D288():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D288)

    def lambda_D296():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D296)

    def lambda_D2A4():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_D2A4)
    TurnDirection(0x107, 0x8, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#006F嗯，明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F我们走了，雾香。\x01",
            "军队那边就拜托你应对了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#791F嗯，\x01",
            "即使被质问我也会妥善应对的。\x02\x03",
            "愿女神保佑你们。\x01",
            "请各位行事多加小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x43, 0x1, 0x200)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_24_BB35 end

    def Function_25_D395(): pass

    label("Function_25_D395")

    EventBegin(0x0)
    OP_6D(3310, 0, -200, 0)
    OP_67(0, 6580, -10000, 0)
    OP_6B(3000, 0)
    SetChrPos(0x101, 2770, 0, -720, 0)
    SetChrPos(0x102, 4310, 0, -890, 0)
    SetChrPos(0xB, 3260, 0, -2080, 0)
    ClearChrFlags(0xB, 0x80)
    TurnDirection(0x101, 0xB, 0)
    TurnDirection(0x102, 0xB, 0)
    TurnDirection(0xB, 0x8, 0)
    OP_4A(0x8, 255)
    OP_3F(0x35A, 1)
    OP_3F(0x362, 1)
    OP_3F(0x364, 1)
    FadeToBright(2000, 0)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)

    ChrTalk(
        0xB,
        (
            "#803F是吗……\x01",
            "已经把博士平安地救出来了。\x02\x03",
            "演算器也取了回来，\x01",
            "我该怎么表达我的感激之情呢……\x02\x03",
            "#800F谢谢你们。\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯～\x01",
            "我们也没有做什么啦……\x02\x03",
            "说到底……\x01",
            "我们只是给阿加特帮了一点忙而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F要感谢的话，\x01",
            "请感谢保护博士他们的阿加特兄吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#805F我当然也要感谢他。\x02\x03",
            "希望他们最后都能够\x01",
            "顺利平安地逃开军队的搜索……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F现在也只能相信阿加特了。\x01",
            "　\x02\x03",
            "#790F不过，理查德上校好像\x01",
            "正打算在王都有所行动的样子。\x02\x03",
            "用那个被称为『福音』的黑色导力器……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯……\x01",
            "虽然不知道要用它来做什么。\x02\x03",
            "只要按照博士的委托，\x01",
            "把这件事禀告给女王就行了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#803F嗯……\x01",
            "没想到会在这里听到陛下的名字。\x02\x03",
            "#800F的确……\x01",
            "博士与女王曾有过私人的来往。\x02\x03",
            "他会知道一些关于\x01",
            "王国的机密事情也不奇怪。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#012F雾香小姐，关于这件事，\x01",
            "虽然我们受到了博士的正式委托……\x02\x03",
            "#012F但在现在这样的情况下，\x01",
            "我们能够直接前往王都吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D91F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D91F)

    ChrTalk(
        0x8,
        (
            "#792F他们又没有掌握你们潜入要塞的证据，\x01",
            "现在这个时期应该没有问题。\x01",
            "　\x02\x03",
            "#790F不过你们须要尽快赶往王都。\x01",
            "　\x02\x03",
            "还有的是……\x01",
            "中央工房会有被检查的可能性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#806F没错……\x01",
            "现在必须制定出对策才行。\x02\x03",
            "#800F艾丝蒂尔、约修亚。\x01",
            "出发后一定要多加小心。\x02\x03",
            "博士的委托就靠你们了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DB1A():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB1A)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(
        0x101,
        (
            "#006F嗯，交给我们吧！\x01",
            "一定会如实传达给女王的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F请工房长您也要小心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#801F嗯，我们绝对不会被\x01",
            "情报部那些家伙抓住把柄的。\x02\x03",
            "那么，我告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 225, 400)
    OP_8E(0xB, 0x60E, 0x0, 0xFFFFE796, 0xBB8, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_DC40():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DC40)
    OP_8E(0xB, 0x690, 0x0, 0xFFFFE053, 0x7D0, 0x0)
    SetChrFlags(0xB, 0x80)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F接下来……\x01",
            "我们必须赶快行动了。\x02\x03",
            "一定要尽快见到女王才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F这样的话，\x01",
            "我们这次最好改乘定期船。\x02\x03",
            "步行到王都要半天的时间，\x01",
            "乘坐飞艇的话只要不到一个小时。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F是吗，确实……\x02\x03",
            "本来想步行环游王国一周的，\x01",
            "不过这也是没有办法的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#790F这样的话，请稍等一下。\x02",
    )

    CloseMessageWindow()

    def lambda_DE51():
        OP_6D(3570, 0, 620, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DE51)

    def lambda_DE69():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DE69)

    def lambda_DE77():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DE77)
    OP_8E(0x8, 0x14E6, 0x0, 0x4C4, 0x7D0, 0x0)

    def lambda_DE99():

        label("loc_DE99")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_DE99")

    QueueWorkItem2(0x101, 1, lambda_DE99)

    def lambda_DEAA():

        label("loc_DEAA")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_DEAA")

    QueueWorkItem2(0x102, 1, lambda_DEAA)
    OP_8E(0x8, 0x1504, 0x0, 0x9C4, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(400)
    OP_22(0x83, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x8)

    ChrTalk(
        0x8,
        (
            "#792F这里是游击士协会……\x02\x03",
            "您好。\x01",
            "总是承蒙您的照顾。\x02\x03",
            "……嗯……拜托您了。\x02\x03",
            "两张到王都格兰赛尔的……\x01",
            "嗯、嗯……和平时的要求一样。\x02\x03",
            "#791F那么就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(300)
    OP_8C(0x8, 180, 400)
    OP_8E(0x8, 0x13B0, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0x8, 0xDAC, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x101,
        (
            "#501F？？？\x01",
            "怎么了，雾香姐？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F难道是打给飞艇坪的接待处？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#791F嗯，没错。\x01",
            "我预订了两张到王都的定期船票。\x02\x03",
            "费用由蔡斯支部支付，\x01",
            "所以你们只需要去办理搭乘手续就可以了。\x02\x03",
            "还有，请收下这个。\x02",
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
            "得到了\x07\x02",
            "正游击士资格的推荐信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x33A, 1)

    ChrTalk(
        0x101,
        "#004F哎～～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F真、真是准备得很周到啊……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#791F定期船票的支出是\x01",
            "传话给女王这一任务的必要经费。\x02\x03",
            "推荐信则是对你们两个\x01",
            "完成救出博士这一重要工作的评价。\x02\x03",
            "请不要谦虚，\x01",
            "与这次的报酬一起收下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊……嗯！\x02\x03",
            "谢谢，雾香姐！\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x41, 0x4, 0x10)
    OP_28(0x43, 0x4, 0x10)
    Sleep(100)
    OP_AF(0x40, 0x41)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(100)
    OP_AF(0x40, 0x43)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#010F真的是……\x01",
            "太麻烦雾香小姐您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F呵呵，之前我不是说过了吗？\x01",
            "这只是身为支部负责人的工作而已。\x02\x03",
            "#791F顺带一提……\x01",
            "到王都的定期船１１点准时出发。\x02\x03",
            "事不宜迟，\x01",
            "赶快去飞艇坪办理搭乘手续吧。\x02\x03",
            "愿女神保佑。\x01",
            "你们俩行事时务必小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F好的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F劳您费心了。\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x601)
    OP_28(0x54, 0x1, 0x1)
    OP_28(0x42, 0x4, 0x10)
    OP_28(0x42, 0x4, 0x20)
    OP_28(0x44, 0x4, 0x10)
    OP_28(0x44, 0x4, 0x20)
    OP_28(0x2B, 0x4, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4FE")
    OP_28(0x2D, 0x4, 0x40)

    label("loc_E4FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E50C")
    OP_28(0x2E, 0x4, 0x40)

    label("loc_E50C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E51A")
    OP_28(0x2F, 0x4, 0x40)

    label("loc_E51A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E528")
    OP_28(0x30, 0x4, 0x40)

    label("loc_E528")

    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_25_D395 end

    def Function_26_E52F(): pass

    label("Function_26_E52F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_E54C")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0x34, 0xFFFF)
    Jump("loc_E5DB")

    label("loc_E54C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_E569")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0x34, 0xFFFF)
    Jump("loc_E5DB")

    label("loc_E569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_E584")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0xFFFF)
    Jump("loc_E5DB")

    label("loc_E584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_E59F")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0xFFFF)
    Jump("loc_E5DB")

    label("loc_E59F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_E5BA")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0xFFFF)
    Jump("loc_E5DB")

    label("loc_E5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_E5CD")
    OP_2A(0x2D, 0x32, 0x2A, 0xFFFF)
    Jump("loc_E5DB")

    label("loc_E5CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E5DB")
    OP_2A(0x2D, 0x32, 0xFFFF)

    label("loc_E5DB")

    TalkEnd(0xFF)
    Return()

    # Function_26_E52F end

    SaveToFile()

Try(main)
