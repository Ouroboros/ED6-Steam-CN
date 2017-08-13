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
        '海泽尔',                               # 9
        '露依赛',                               # 10
        '雨果',                                 # 11
        '鲁特尔',                               # 12
        '多杰',                                 # 13
        '鲁迪',                                 # 14
        '菲',                                   # 15
        '埃里克',                               # 16
        '朵洛希',                               # 17
        '拉德米拉',                             # 18
        '卡雷尔',                               # 19
        '加鲁诺',                               # 20
        '汽油',                                 # 21
        '安东尼',                               # 22
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
        "Function_5_D96",          # 05, 5
        "Function_6_1594",         # 06, 6
        "Function_7_17B6",         # 07, 7
        "Function_8_180B",         # 08, 8
        "Function_9_1EF9",         # 09, 9
        "Function_10_300E",        # 0A, 10
        "Function_11_361B",        # 0B, 11
        "Function_12_47F4",        # 0C, 12
        "Function_13_4852",        # 0D, 13
        "Function_14_4F8C",        # 0E, 14
        "Function_15_5267",        # 0F, 15
        "Function_16_5344",        # 10, 16
        "Function_17_5565",        # 11, 17
        "Function_18_5786",        # 12, 18
        "Function_19_578B",        # 13, 19
        "Function_20_5790",        # 14, 20
        "Function_21_5885",        # 15, 21
        "Function_22_59F9",        # 16, 22
        "Function_23_6124",        # 17, 23
        "Function_24_613A",        # 18, 24
        "Function_25_629D",        # 19, 25
        "Function_26_630D",        # 1A, 26
        "Function_27_65B0",        # 1B, 27
        "Function_28_65B1",        # 1C, 28
        "Function_29_685B",        # 1D, 29
        "Function_30_68C4",        # 1E, 30
        "Function_31_6D3E",        # 1F, 31
        "Function_32_71B8",        # 20, 32
        "Function_33_72D2",        # 21, 33
        "Function_34_73D2",        # 22, 34
        "Function_35_74EC",        # 23, 35
        "Function_36_7544",        # 24, 36
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_D92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_CE3")

    ChrTalk(
        0xFE,
        (
            "啊～怎么办呢。\x01",
            "浅显易懂的说明吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但、但是除了性能以外的东西\x01",
            "我就没办法说明了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "（唉，\x01",
            "　才刚刚发生那样的事情，\x01",
            "　没有卖东西的心情了啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D92")

    label("loc_CE3")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "啊……真是为难。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "性能方面\x01",
            "这一种型号的透镜色差很小，\x01",
            "我大胆向你推荐……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯？是吗？\x01",
            "使用方便的相机吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽、虽然说使用方便，\x01",
            "也要看各人的具体情况吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D92")

    TalkEnd(0xFE)
    Return()

    # Function_4_C2F end

    def Function_5_D96(): pass

    label("Function_5_D96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1165")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10BE")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哟，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……？\x02\x03",
            "#010F啊，我还以为是谁呢……\x01",
            "真的是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯？是谁啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵，就是在洛连特\x01",
            "寻找齿轮的那个孩子啊。\x02\x03",
            "我们之前不是\x01",
            "接受过他的委托去找那碎片吗。\x02\x03",
            "了不起呢，\x01",
            "今天给母亲帮忙吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "啊啊，帮忙做一下吧。\x01",
            "差不多要回卡尔瓦德了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……我决定，等我的\x01",
            "几个妹妹再长大点之后，\x01",
            "就来这个城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为做见习生就可以进入工房，\x01",
            "然后将来就可以造飞船了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的手很巧，\x01",
            "这点连我老妈也是知道的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是吗……\x02\x03",
            "这样也挺不错啊。\x01",
            "已经找到了将来的目标。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "那当然的啦。\x01",
            "我也要考虑自己的前途才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……唉，不过\x01",
            "现在还是要先给老妈帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我有四个妹妹，\x01",
            "年纪还都很小呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯！你要努力帮忙哦。\x01",
            "就算是为了你的几个妹妹。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "啊，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再见了，\x01",
            "你们也加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1162")

    label("loc_10BE")


    ChrTalk(
        0xFE,
        (
            "……我决定，等我的\x01",
            "几个妹妹再长大点之后，\x01",
            "就来这个城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为做见习生就可以进入工房，\x01",
            "然后将来就可以造飞船了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的手很巧，\x01",
            "这点连我老妈也是知道的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1162")

    Jump("loc_1590")

    label("loc_1165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1534")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_145F")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哟，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……？\x02\x03",
            "#010F啊，我还以为是谁呢……\x01",
            "真的是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯？是谁啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵，就是在洛连特\x01",
            "寻找齿轮的那个孩子啊。\x02\x03",
            "我们之前不是\x01",
            "接受过他的委托去找那碎片吗。\x02\x03",
            "了不起呢，\x01",
            "今天给母亲帮忙吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "啊啊，帮忙做一下吧。\x01",
            "差不多要回卡尔瓦德了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……我决定，等我的\x01",
            "几个妹妹再长大点之后，\x01",
            "就来这个城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为做见习生就可以进入工房，\x01",
            "然后将来就可以造飞船了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是吗……\x02\x03",
            "这样也挺不错啊。\x01",
            "已经找到了将来的目标。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "那当然的啦。\x01",
            "我也要考虑自己的前途才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……唉，不过\x01",
            "现在还是要先给老妈帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我有四个妹妹，\x01",
            "年纪还都很小呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯！你要努力帮忙哦。\x01",
            "就算是为了你的几个妹妹。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "啊，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再见了，\x01",
            "你们也加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1531")

    label("loc_145F")


    ChrTalk(
        0xFE,
        (
            "等我家的几个妹妹\x01",
            "再长大点之后，我\x01",
            "就来这个城市。    \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为做见习生就可以进入工房，\x01",
            "然后将来就可以造飞船了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……唉，不过\x01",
            "现在还是要先给老妈帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我有四个妹妹，\x01",
            "现在还很小，\x01",
            "妈妈也很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1531")

    Jump("loc_1590")

    label("loc_1534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_1590")

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……了不起……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "导力引擎\x01",
            "是在这里做的啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1590")

    TalkEnd(0xFE)
    Return()

    # Function_5_D96 end

    def Function_6_1594(): pass

    label("Function_6_1594")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1623")

    ChrTalk(
        0xFE,
        (
            "呼，这次的生意\x01",
            "马上就要搞定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "销售很顺利，\x01",
            "进货也很顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家的卡雷尔\x01",
            "似乎也确定了什么目标。\x01",
            "嗯，这次非常好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B2")

    label("loc_1623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_16A4")

    ChrTalk(
        0xFE,
        (
            "我是来拿\x01",
            "在这里订购的导力相机的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "令人惊喜的是\x01",
            "儿子也开始给我帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "卡雷尔那孩子\x01",
            "好像有点变化了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B2")

    label("loc_16A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_17B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_170F")

    ChrTalk(
        0xFE,
        (
            "似乎发生了什么事呢，\x01",
            "不过我只知道情况很严重。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "能不能简单明了地\x01",
            "给我说明一下啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B2")

    label("loc_170F")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "哎呀，我都说了，\x01",
            "我不是询问你\x01",
            "那些具体数字方面的情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只是问问哪种相机操作简单，\x01",
            "最适合新手使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "相机不是你制造的吗？\x01",
            "你就没有考虑过这些事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B2")

    TalkEnd(0xFE)
    Return()

    # Function_6_1594 end

    def Function_7_17B6(): pass

    label("Function_7_17B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_1807")

    ChrTalk(
        0x10,
        (
            "#150F嗯～\x01",
            "来五套普通的吧。\x02\x03",
            "啊，对了对了，\x01",
            "还要买全景摄影的器材。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1807")

    TalkEnd(0xFE)
    Return()

    # Function_7_17B6 end

    def Function_8_180B(): pass

    label("Function_8_180B")

    TalkBegin(0xF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "离开\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186D")
    OP_0D()
    OP_A9(0x3C)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_186D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_187E")
    TalkEnd(0xF)
    Return()

    label("loc_187E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_18DB")

    ChrTalk(
        0xF,
        "欢迎来到维修柜台。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "虽然总是出一些乱子，\x01",
            "但我还是会调整好心情努力工作的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_18DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1947")

    ChrTalk(
        0xF,
        "嗯，怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "工房船的船员怎么\x01",
            "慌慌张张地跑来跑去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "难道是什么地方\x01",
            "发生事故了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1997")

    ChrTalk(
        0xF,
        (
            "早上好。\x01",
            "欢迎，这里是维修柜台。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "好的，\x01",
            "今天也要努力工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1A1A")

    ChrTalk(
        0xF,
        (
            "啊，谢谢了。\x01",
            "干到这么晚真是辛苦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "现在我还在工作，\x01",
            "有什么事的话请尽管说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "呼，今天出了很多事，\x01",
            "真是累啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_1BB1")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_END)), "loc_1B01")

    ChrTalk(
        0xF,
        (
            "从导力相机到导力枪，\x01",
            "加鲁诺都能从事开发，\x01",
            "真是个具有广博开发实力的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "在这个中央工房里，\x01",
            "以拉赛尔博士为首，\x01",
            "这种全能型的研究者真的很多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "研究者工作的时候， \x01",
            "肯定会毫无隔阂地彼此学习和交流吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAE")

    label("loc_1B01")

    OP_A2(0x5)

    ChrTalk(
        0xF,
        (
            "呼呼，\x01",
            "刚刚才在想骚乱终于平息了，\x01",
            "这下又来了个不得了的客人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "虽然是位大娘，\x01",
            "不过一来就开始发牢骚呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "开发部的加鲁诺来帮我给她说明了，\x01",
            "应该没有问题了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAE")

    Jump("loc_1EF5")

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1C48")

    ChrTalk(
        0xF,
        (
            "在那边自言自语的客人\x01",
            "似乎对导力器这种东西\x01",
            "还不太了解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "怎么办啊？\x01",
            "是不是需要给他详细地说明一下呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "唔～连我也开始自言自语了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1CD0")

    ChrTalk(
        0xF,
        "啊，客人您好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "怎么样？\x01",
            "不看看结晶回路吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "我自己这样说可能有点自卖自夸，\x01",
            "不过这批货质量真的不错，品种也齐全。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1DB9")

    ChrTalk(
        0xF,
        (
            "啊，谢谢了。\x01",
            "哎呀～今天一大早就开始忙碌起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "我们要检查昨天的事故\x01",
            "是否给导力器造成故障和错误……\x01",
            "光做这些应对工作就已经忙死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "嗯，其实导力器技术的相关知识\x01",
            "对于蔡斯的市民们来说\x01",
            "也并不是显得那么高深莫测。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1E69")

    ChrTalk(
        0xF,
        "欢迎来到维修柜台。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "其实我也是\x01",
            "中央工房的研究员，\x01",
            "不过现在还只是处于见习阶段。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "修理导力器\x01",
            "也是我修行的一部分。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "什么时候我也有\x01",
            "自己的研究室就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1EF5")

    ChrTalk(
        0xF,
        "欢迎来到维修柜台。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "虽说是柜台，\x01",
            "但这里可是中央工房\x01",
            "直接运营的导力器工房。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "这里和一般的工房没什么区别，\x01",
            "请放心使用吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF5")

    TalkEnd(0xF)
    Return()

    # Function_8_180B end

    def Function_9_1EF9(): pass

    label("Function_9_1EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2627")
    TalkBegin(0xFE)
    OP_A2(0x53D)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -114810, -4000, -111130, 90)
    SetChrPos(0x102, -114650, -4000, -112120, 45)
    TurnDirection(0xE, 0x101, 0)
    OP_69(0xE, 0x3E8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F75")

    ChrTalk(
        0x101,
        "#000F那个～能打扰一下吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F9D")

    label("loc_1F75")


    ChrTalk(
        0x102,
        (
            "#010F不好意思。\x01",
            "请问能打扰一下吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F9D")


    ChrTalk(
        0xE,
        "#2P怎么，有什么事吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们向管理员菲\x01",
            "说明了有关拉赛尔博士需要汽油的委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xE,
        "#2P哦～汽油啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2P保管库里\x01",
            "的确有几桶库存……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2P稍等一下，我问问。\x02",
    )

    CloseMessageWindow()

    def lambda_2068():
        OP_6D(-112600, -4000, -109400, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2068)
    OP_8C(0xE, 0, 400)
    WaitChrThread(0x101, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "菲拨通了内线电话。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xE,
        (
            "#2P我是菲。\x01",
            "有件事想问问你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2P共和国产的汽油，\x01",
            "应该还有些库存对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2P嗯、嗯……\x01",
            "给我送一桶过来行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2P要一桶可以带着走的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2P谢了，拜托啦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(
        0xE,
        (
            "#2P稍等一下。\x01",
            "马上就传送过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F传送过来……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 90, 400)
    OP_72(0x8, 0x4)
    OP_A1(0x14, 0x8)
    SetChrPos(0x14, -95360, -3300, -109080, 14)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x14, 0x4)

    def lambda_21D7():
        OP_8F(0xFE, 0xFFFE54F8, 0xFFFFF31C, 0xFFFE55A2, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_21D7)
    OP_22(0x5B, 0x1, 0x64)
    OP_76(0xFF, 0xF, 0x1, 0x2, 0x0, 0x3E8, 0x0, 0x0)
    OP_76(0xFF, 0x18, 0x1, 0x2, 0x0, 0x3E8, 0x0, 0x0)
    OP_76(0xFF, 0x24, 0x1, 0x2, 0x0, 0x3E8, 0x0, 0x0)
    OP_76(0xFF, 0x33, 0x1, 0x2, 0x0, 0x3E8, 0x0, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F哇哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "来了来了。\x02",
    )

    CloseMessageWindow()

    def lambda_227B():
        OP_6D(-105100, -4000, -108200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_227B)

    def lambda_2293():
        OP_8E(0xFE, 0xFFFE5A84, 0xFFFFF060, 0xFFFE4D3C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2293)
    Sleep(800)

    def lambda_22B3():
        OP_8E(0xFE, 0xFFFE53E0, 0xFFFFF060, 0xFFFE4E04, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22B3)
    Sleep(500)

    def lambda_22D3():
        OP_8E(0xFE, 0xFFFE4F94, 0xFFFFF060, 0xFFFE4D3C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22D3)
    WaitChrThread(0xE, 0x1)

    def lambda_22F3():

        label("loc_22F3")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_22F3")

    QueueWorkItem2(0xE, 1, lambda_22F3)
    WaitChrThread(0x101, 0x1)

    def lambda_2309():

        label("loc_2309")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2309")

    QueueWorkItem2(0x101, 1, lambda_2309)
    WaitChrThread(0x102, 0x1)

    def lambda_231F():

        label("loc_231F")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_231F")

    QueueWorkItem2(0x102, 1, lambda_231F)

    def lambda_2330():
        OP_6D(-108840, -4000, -109520, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2330)
    WaitChrThread(0x14, 0x1)
    OP_75(0xFF, 0xF, 0x5)
    OP_75(0xFF, 0x18, 0x5)
    OP_75(0xFF, 0x24, 0x5)
    OP_75(0xFF, 0x33, 0x5)
    OP_23(0x5B)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#501F哎呀～\x01",
            "难道说这个桶里就是汽油吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F『传送过来』\x01",
            "原来就是这个意思啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xE, 0xFF)
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(
        0xE,
        "#2P呵呵，了不起吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2P给你们介绍一下，\x01",
            "这个传送系统不光能运送制品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2P它还有连接着\x01",
            "广大的地下工场的功能呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xE, 400)
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(
        0x101,
        "#004F啊，很方便嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2P这也是拉赛尔博士所提出的方案哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2P原本这个传送带\x01",
            "只有运送制品的机能……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2P是那个老爷子把它改造成了\x01",
            "相当有用的系统。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2P不过话说回来，\x01",
            "在基础设施整理完善之前可是辛苦死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F啊哈哈。\x01",
            "不愧是博士的杰作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么感谢您的帮忙，\x01",
            "这桶汽油我们就带走了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(
        0xE,
        "#2P好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2P啊，不知道你们用它来干什么，\x01",
            "但处理起来一定要注意哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2P汽油这种东西\x01",
            "可是非常容易燃烧的。\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x0, 0x1)
    EventEnd(0x0)
    OP_43(0xE, 0x0, 0x0, 0x2)
    Jump("loc_300A")

    label("loc_2627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_26A0")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "不好意思，\x01",
            "还要你们专程送过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们这么忙还帮我，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "我要回去工作了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_26A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x35E)"), scpexpr(EXPR_END)), "loc_26CA")
    Call(1, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_26CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_27CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2736")

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "这难道真的是军队的所作所为……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听到真相的时候\x01",
            "对大家的打击确实不小呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C7")

    label("loc_2736")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "啊……是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "谢谢你们救出了博士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然不能完全放心，\x01",
            "不过现在的情况已经不错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望以后你们也能\x01",
            "作为市民的坚强依靠。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C7")

    Jump("loc_300A")

    label("loc_27CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2994")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_28E9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_284A")

    ChrTalk(
        0xFE,
        (
            "唉，怎么办啊。\x01",
            "我又不能放下鲁迪不管。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难得布拉姆\x01",
            "给我写封信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "真是太不凑巧了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E6")

    label("loc_284A")


    ChrTalk(
        0xFE,
        (
            "唉，怎么办啊。\x01",
            "我又不能放下鲁迪不管。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没想到，\x01",
            "我还挂念着那个没用的家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "怎么会这样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这么说，\x01",
            "我难道只能喜欢没用的男人吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E6")

    Jump("loc_2991")

    label("loc_28E9")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "唉，怎么办啊。\x01",
            "真是头痛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总觉得最近\x01",
            "好像特别在意鲁迪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实也算不上喜欢吧，\x01",
            "总之就是觉得\x01",
            "不能丢下不管……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，真是讨厌。\x01",
            "完全没有心情工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2991")

    Jump("loc_300A")

    label("loc_2994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2A89")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29FA")

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "鲁迪也罢，\x01",
            "布拉姆也罢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么我周围\x01",
            "只有这种男人呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A86")

    label("loc_29FA")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "我之前还严厉地\x01",
            "训斥了鲁迪一顿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家伙整天闷闷不乐，\x01",
            "工作也不干。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，真是没有办法。\x01",
            "于是我就说『你也拿点血性出来啊』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A86")

    Jump("loc_300A")

    label("loc_2A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_2BAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2B34")

    ChrTalk(
        0xFE,
        (
            "我正在工作的时候，\x01",
            "工房突然间浓烟滚滚。\x01",
            "我慌慌张张就逃向一楼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "鲁迪那家伙，傻呆呆的，\x01",
            "吸了一肚子烟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为慎重起见，\x01",
            "他刚刚去医务室做检查了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA9")

    label("loc_2B34")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "我正在工作的时候，\x01",
            "工房突然浓烟滚滚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我慌慌张张就逃到一楼去了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想犯人们\x01",
            "肯定是从地下进来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA9")

    Jump("loc_300A")

    label("loc_2BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2CB6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2C46")

    ChrTalk(
        0xFE,
        (
            "现在必须把信的事放一边，\x01",
            "集中精神工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不然的话，\x01",
            "就没法给布拉姆起示范……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……啊，不对。\x01",
            "就没法给鲁迪\x01",
            "起示范作用了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB3")

    label("loc_2C46")


    ChrTalk(
        0xFE,
        (
            "我刚刚才\x01",
            "怒斥过鲁迪呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家伙一直在发愣，\x01",
            "手也不动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "以前他明明不像这么没用的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CB3")

    Jump("loc_300A")

    label("loc_2CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2D98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_END)), "loc_2D1B")

    ChrTalk(
        0xFE,
        (
            "虽然不知道用它来做什么，\x01",
            "但处理起来一定要注意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "汽油这东西\x01",
            "非常容易燃烧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D95")

    label("loc_2D1B")

    OP_62(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0xE)

    ChrTalk(
        0xFE,
        "呼～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好了，菲。\x01",
            "要集中精力工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "传输方面一切正常，\x01",
            "接下来检查一下仓库吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D95")

    Jump("loc_300A")

    label("loc_2D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2E1D")

    ChrTalk(
        0xFE,
        (
            "首先要检查装置\x01",
            "有没有受昨天的现象影响\x01",
            "而出现传输问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了慎重起见，检查完那个之后\x01",
            "麻烦你去确认一下外面的器材。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300A")

    label("loc_2E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2EA9")

    ChrTalk(
        0xFE,
        (
            "我啊，\x01",
            "怎么会喜欢上\x01",
            "那样的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "长得又不帅，\x01",
            "还总是一副睡不醒的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，事到如今对我来说都是个谜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F3E")

    label("loc_2EA9")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "呼～～\x01",
            "悲哀啊～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我怎么会喜欢上\x01",
            "那样的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "长得又不帅，\x01",
            "还总是一副睡不醒的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……冷静地想一下，\x01",
            "他真是没什么优点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F3E")

    Jump("loc_300A")

    label("loc_2F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_300A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2F8D")

    ChrTalk(
        0xFE,
        "好了，工作，工作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "必须快点忘了\x01",
            "那个傻瓜的事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300A")

    label("loc_2F8D")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "哈啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个傻瓜\x01",
            "现在在做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……哎呀，不行不行，\x01",
            "我正在工作，必须集中精神。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_300A")

    TalkEnd(0xFE)
    Return()

    # Function_9_1EF9 end

    def Function_10_300E(): pass

    label("Function_10_300E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_307B")

    ChrTalk(
        0xFE,
        (
            "从工房船回来之后，\x01",
            "菲前辈还是没什么精神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难、难道说，\x01",
            "她和前男友的关系又有变化了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3617")

    label("loc_307B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_30CF")

    ChrTalk(
        0xFE,
        (
            "菲前辈\x01",
            "刚才被别人叫走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "工房船那里好像\x01",
            "接到了紧急出动的通知。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3617")

    label("loc_30CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_31B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3138")

    ChrTalk(
        0xFE,
        (
            "或许是我的错觉吧，\x01",
            "最近常常和前辈目光相交啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……反正只是我\x01",
            "自己胡思乱想吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31AD")

    label("loc_3138")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "或许是我的错觉吧，\x01",
            "最近常常和前辈目光相交啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难、难道前辈终于\x01",
            "发现我的魅力了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唉，不会吧。\x02",
    )

    CloseMessageWindow()

    label("loc_31AD")

    Jump("loc_3617")

    label("loc_31B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_320F")

    ChrTalk(
        0xFE,
        (
            "又被前辈教训，\x01",
            "还出了那样的事，\x01",
            "简直干劲全无啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼呼～～\x01",
            "真想早点回家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3617")

    label("loc_320F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3386")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_32CA")

    ChrTalk(
        0xFE,
        (
            "刚才在工作的时候\x01",
            "又被菲前辈骂了一顿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "肯定是因为前辈\x01",
            "认为我是个没用的家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呜呜，\x01",
            "好不容易前辈和男友分手，\x01",
            "我以为会有机会的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉～我真是没用啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3383")

    label("loc_32CA")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "唉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才在工作的时候\x01",
            "又被菲前辈骂了一顿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "肯定是因为前辈\x01",
            "认为我是个没用的家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呜呜，\x01",
            "好不容易前辈和男友分手，\x01",
            "我以为会有机会的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉～我真是没用啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3383")

    Jump("loc_3617")

    label("loc_3386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_346E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_33EF")

    ChrTalk(
        0xFE,
        (
            "明明我下定决心\x01",
            "要努力工作呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可总是在意着前辈的前男友，\x01",
            "根本不能专心工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346B")

    label("loc_33EF")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "嗯，菲前辈的前男友\x01",
            "到底是谁啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前也找朋友们打听过，\x01",
            "但是没人知道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，真是的！\x01",
            "根本不能专心工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_346B")

    Jump("loc_3617")

    label("loc_346E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_34AD")

    ChrTalk(
        0xFE,
        "是，我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "我去检查传输装置了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3617")

    label("loc_34AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_35A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3522")

    ChrTalk(
        0xFE,
        (
            "可是，前辈到底喜欢什么样的人\x01",
            "我完全不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……已经分手的男友\x01",
            "会不会也在工房里工作呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_359D")

    label("loc_3522")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "听说菲前辈她\x01",
            "最近刚刚和男友分手呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，\x01",
            "机会终于降临到我的头上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定要好好努力，展示一下我的优点。\x02",
    )

    CloseMessageWindow()

    label("loc_359D")

    Jump("loc_3617")

    label("loc_35A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3617")

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "加上这罐的话总共就有八罐了………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好了，和清单上的一样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "接下来就交给工场那边检查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3617")

    TalkEnd(0xFE)
    Return()

    # Function_10_300E end

    def Function_11_361B(): pass

    label("Function_11_361B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_3684")

    ChrTalk(
        0x8,
        (
            "刚刚，格斯塔夫维修长\x01",
            "急急忙忙地赶了过来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "似乎相当匆忙呢。\x01",
            "飞艇坪出什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_3684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3719")

    ChrTalk(
        0x8,
        (
            "各位。\x01",
            "营救作战大家辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然很想\x01",
            "好好向大家致谢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……为了以防万一，\x01",
            "这些话还是等以后再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那么，请务必小心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_3719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_375B")

    ChrTalk(
        0x8,
        "……各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "营救博士的事\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3825")

    label("loc_375B")

    OP_A2(0x4)

    ChrTalk(
        0x8,
        "……各位，\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "营救博士的事\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "提妲也不要\x01",
            "太过勉强哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F知道了……\x01",
            "我会小心行事的。\x02\x03",
            "#061F阿加特大哥哥已经教育我\x01",
            "不能再那样鲁莽地行动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#052F………………………\x02",
    )

    CloseMessageWindow()

    label("loc_3825")

    Jump("loc_47F0")

    label("loc_3828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3892")

    ChrTalk(
        0x8,
        "哎呀，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "提妲她\x01",
            "应该是去了四楼的医务室吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "她真是相当担心\x01",
            "阿加特的情况呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_3892")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_38E6")

    ChrTalk(
        0x8,
        (
            "刚才被抬走的\x01",
            "好像是一位游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "看起来脸色很差，\x01",
            "没关系吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_38E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_END)), "loc_3959")

    ChrTalk(
        0x8,
        (
            "根据工房长的判断，\x01",
            "拉赛尔博士被掳走的事\x01",
            "还是对大多数人保密比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "博士的事，\x01",
            "无论如何拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_3959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_3A86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_39D1")

    ChrTalk(
        0x8,
        (
            "根据工房长的判断，\x01",
            "拉赛尔博士被掳走的事\x01",
            "还是对大多数人保密比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "提妲，\x01",
            "你也不要这么灰心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A83")

    label("loc_39D1")

    OP_A2(0x4)

    ChrTalk(
        0x8,
        (
            "啊，各位……\x01",
            "提妲……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……根据工房长的判断，\x01",
            "拉赛尔博士被掳走的事\x01",
            "还是对大多数人保密比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "提妲，\x01",
            "你也不要这么灰心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F………………………\x02\x03",
            "……好的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A83")

    Jump("loc_47F0")

    label("loc_3A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3C41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 1)), scpexpr(EXPR_END)), "loc_3AE9")

    ChrTalk(
        0x8,
        (
            "我已经通知过\x01",
            "游击士协会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么，就麻烦你们\x01",
            "将提妲护送到亚尔摩那里了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C3E")

    label("loc_3AE9")

    OP_A2(0x581)

    ChrTalk(
        0x8,
        "啊，提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "亚尔摩旅馆的事，\x01",
            "我从玛多克工房长那里打听到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "提妲，\x01",
            "你是要代替爷爷去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，是的。\x02\x03",
            "我也曾经帮过忙，\x01",
            "所以应该没问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们会负责\x01",
            "把提妲护送到亚尔摩村。\x02\x03",
            "所以，请不用担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我已经通知过\x01",
            "游击士协会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么提妲\x01",
            "就拜托你们照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F那我们走了。\x02",
    )

    CloseMessageWindow()

    label("loc_3C3E")

    Jump("loc_47F0")

    label("loc_3C41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3C9F")

    ChrTalk(
        0x8,
        "竟然能够扛得动那么重的东西……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "游击士受过的锻炼\x01",
            "就是不一样啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D05")

    label("loc_3C9F")

    OP_A2(0x4)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "哇，竟然能\x01",
            "扛得动那么重的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "游击士受过的锻炼\x01",
            "就是不一样啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D05")

    Jump("loc_47F0")

    label("loc_3D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_END)), "loc_3DC4")

    ChrTalk(
        0x101,
        (
            "#505F嗯，已经有汽油了。\x01",
            "接下来就是要找那个\x01",
            "叫格斯塔夫维修长的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我想维修长\x01",
            "大概在飞艇坪那边吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "除了来中央工房汇报情况，\x01",
            "其他的时候他都不怎么回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3DC4")


    ChrTalk(
        0x101,
        (
            "#505F嗯，已经将内燃引擎设备借来了。\x01",
            "接下来该去导力器工场那里了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "要去工场的话，\x01",
            "请坐导力梯到地下一层。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E3A")

    Jump("loc_47F0")

    label("loc_3E3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_END)), "loc_3FA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3EA6")

    ChrTalk(
        0x8,
        (
            "要去工场的话，\x01",
            "请坐导力梯到地下一层。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "要找维修长的话，\x01",
            "他大概在飞艇坪那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F9E")

    label("loc_3EA6")

    OP_A2(0x4)

    ChrTalk(
        0x8,
        (
            "啊，各位。\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F唔～我们要去导力器工场，\x01",
            "还要找一个叫格斯塔夫维修长的人。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "要去工场的话，\x01",
            "请坐导力梯到地下一层。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "要找维修长的话，\x01",
            "他大概在飞艇坪那边吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "除了来中央工房汇报情况，\x01",
            "其他的时候他都不怎么回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F9E")

    Jump("loc_47F0")

    label("loc_3FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_4193")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4057")

    ChrTalk(
        0x8,
        (
            "啊，各位。\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F唔～\x01",
            "到演算室去就行了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "演算室在五楼。\x01",
            "乘导力梯的话会很方便的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果还有什么事的话，\x01",
            "请别客气，随时来找我问吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4190")

    label("loc_4057")


    ChrTalk(
        0x8,
        (
            "啊，各位。\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "【格斯塔夫维修长】\x01",
            "【导力器生产工场】\x01",
            "【没什么事】\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "格斯塔夫维修长\x01",
            "平时都会呆在飞艇坪的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "飞艇坪位于\x01",
            "工房前广场的东面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "还有什么其他的事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "工场就在地下。\x01",
            "乘导力梯的话会很方便的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "还有什么其他的事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果还有什么事的话，\x01",
            "请别客气，随时来找我问吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4190")

    Jump("loc_47F0")

    label("loc_4193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_428F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_41FA")

    ChrTalk(
        0x8,
        (
            "拉赛尔博士已经在三楼的工作室\x01",
            "开始作业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我想他应该正焦急地\x01",
            "等人去帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428C")

    label("loc_41FA")

    OP_A2(0x4)
    OP_28(0x3F, 0x1, 0x40)

    ChrTalk(
        0x8,
        (
            "提妲，还有各位。\x01",
            "昨天真是发生了不得了的事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "拉赛尔博士已经在三楼的工作室\x01",
            "开始作业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我想他应该正焦急地\x01",
            "等人去帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_428C")

    Jump("loc_47F0")

    label("loc_428F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_439B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_42D0")
    TurnDirection(0x8, 0x107, 0)

    ChrTalk(
        0x8,
        (
            "那么，提妲。\x01",
            "就麻烦你为客人带路了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4398")

    label("loc_42D0")

    OP_A2(0x4)
    TurnDirection(0x8, 0x107, 0)

    ChrTalk(
        0x8,
        (
            "哎呀，是提妲啊。\x01",
            "这是要去哪里啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊，\x01",
            "我现在要带他们去我家呢。\x02\x03",
            "他们要找\x01",
            "爷爷商量一些事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是这样啊，真是辛苦你了。\x01",
            "那就麻烦你给他们带路吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F好的，我们走了。\x02",
    )

    CloseMessageWindow()

    label("loc_4398")

    Jump("loc_47F0")

    label("loc_439B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_475A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_471E")
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
            "啊，\x01",
            "你们是刚才和提妲一起的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "欢迎来到中央工房。\x01",
            "请问有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F啊～您好。\x01",
            "我们是游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F其实是这样的……\x01",
            "我们想和你们的工房长见面。\x02",
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
            "交出了\x07\x02",
            "给工房长的介绍信\x07\x00",
            "。\x02",
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
            "哦，是这样啊。\x01",
            "请两位稍等一下……\x02",
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
            "接待员小姐拨通了内线电话。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "——啊，工房长。\x01",
            "不好意思，打扰您休息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯……是的。\x01",
            "是游击士协会的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯，我知道了。\x01",
            "那好……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 135, 400)
    OP_8E(0x8, 0x104, 0x0, 0x16A8, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x8,
        "久等了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "玛多克工房长说\x01",
            "你们直接上楼找他就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他现在就在二楼的工房长室，\x01",
            "两位可以搭乘左手边的导力梯上去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F太好了。\x01",
            "马上就能见面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我们快去二楼吧。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_4757")

    label("loc_471E")


    ChrTalk(
        0x8,
        (
            "工房长室就在二楼。\x01",
            "两位可以搭乘左手边的导力梯上去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4757")

    Jump("loc_47F0")

    label("loc_475A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_47F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47B7")

    ChrTalk(
        0x8,
        "欢迎来到蔡斯中央工房。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果有什么事的话，\x01",
            "请随时到前台这里咨询。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_47B7")


    ChrTalk(
        0x8,
        (
            "工房长室就在二楼。\x01",
            "两位可以搭乘左手边的导力梯上去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47F0")

    TalkEnd(0x8)
    Return()

    # Function_11_361B end

    def Function_12_47F4(): pass

    label("Function_12_47F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_4851")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    SetChrName("中央工房１Ｆ")

    ChrTalk(
        0xFE,
        (
            "咦，\x01",
            "调到新型导力引擎的开发项目！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是，是说我吗？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_4851")

    Return()

    # Function_12_47F4 end

    def Function_13_4852(): pass

    label("Function_13_4852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_496A")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4910")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "不好意思啊。\x01",
            "刚出了那样的事，\x01",
            "就让你过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之有些事情\x01",
            "需要尽快跟你说明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "开门见山地说吧……\x01",
            "想让你成为『埃尔赛尤号』\x01",
            "新型引擎开发工作的研究员。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4964")

    label("loc_4910")


    ChrTalk(
        0xFE,
        (
            "因为第一候补人\x01",
            "谢绝了这个工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对你来说是个好机会。\x01",
            "请好好考虑一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4964")

    TalkEnd(0xFE)
    Jump("loc_4F8B")

    label("loc_496A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4F8B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CB8")
    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "对话\x01",                # 0
            "询问烟草的事情\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49E2")
    Call(1, 0)
    Return()

    label("loc_49E2")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_END)), "loc_4AAA")

    ChrTalk(
        0xB,
        (
            "研究员辞掉了工作\x01",
            "真让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "总之，\x01",
            "必须赶快开始研究对策……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "已经发生了的事也没有办法了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就将这看作是\x01",
            "重新策划的机会，\x01",
            "我们要以积极的工作态度去应对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CA5")

    label("loc_4AAA")

    OP_A2(0x575)

    ChrTalk(
        0xB,
        (
            "啊！？\x01",
            "真、真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "新型导力引擎的研究员\x01",
            "辞退不干了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉，\x01",
            "以前明明答应下来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "是不是出了什么事啊。\x01",
            "前几天，接到了他谢绝的消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "是这样啊……\x01",
            "真是头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "本来这个开发计划\x01",
            "是为『埃尔赛尤号』设计的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "如果计划开始不了，\x01",
            "『埃尔赛尤号』正式投入使用\x01",
            "这一目标显然也就难以实现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉唉，\x01",
            "这个我明白啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "『埃尔赛尤号』\x01",
            "现在的导力引擎\x01",
            "也只是旧型号的翻版而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "总之，\x01",
            "眼下必须赶快选出代替的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就将这看作是\x01",
            "重新策划的机会，\x01",
            "我们要以积极的工作态度去应对。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CA5")

    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_4F8B")

    label("loc_4CB8")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_END)), "loc_4D80")

    ChrTalk(
        0xB,
        (
            "研究员辞掉了工作\x01",
            "真让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "总之，\x01",
            "必须赶快开始研究对策……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "已经发生了的事也没有办法了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就将这看作是\x01",
            "重新策划的机会，\x01",
            "我们要以积极的工作态度去应对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F7B")

    label("loc_4D80")

    OP_A2(0x575)

    ChrTalk(
        0xB,
        (
            "啊！？\x01",
            "真、真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "新型导力引擎的研究员\x01",
            "辞退不干了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉，\x01",
            "以前明明答应下来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "是不是出了什么事啊。\x01",
            "前几天，接到了他谢绝的消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "是这样啊……\x01",
            "真是头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "本来这个开发计划\x01",
            "是为『埃尔赛尤号』设计的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "如果计划开始不了，\x01",
            "『埃尔赛尤号』正式投入使用\x01",
            "这一目标显然也就难以实现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉唉，\x01",
            "这个我明白啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "『埃尔赛尤号』\x01",
            "现在的导力引擎\x01",
            "也只是旧型号的翻版而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "总之，\x01",
            "眼下必须赶快选出代替的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就将这看作是\x01",
            "重新策划的机会，\x01",
            "我们要以积极的工作态度去应对。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F7B")

    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_4F8B")

    Return()

    # Function_13_4852 end

    def Function_14_4F8C(): pass

    label("Function_14_4F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5266")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_END)), "loc_505B")

    ChrTalk(
        0xB,
        (
            "研究员辞掉了工作\x01",
            "真让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "总之，\x01",
            "必须赶快开始研究对策……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "已经发生了的事也没有办法了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就将这看作是\x01",
            "重新策划的机会，\x01",
            "我们要以积极的工作态度去应对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5256")

    label("loc_505B")

    OP_A2(0x575)

    ChrTalk(
        0xB,
        (
            "啊！？\x01",
            "真、真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "新型导力引擎的研究员\x01",
            "辞退不干了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉，\x01",
            "以前明明答应下来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "是不是出了什么事啊。\x01",
            "前几天，接到了他谢绝的消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "是这样啊……\x01",
            "真是头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "本来这个开发计划\x01",
            "是为『埃尔赛尤号』设计的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "如果计划开始不了，\x01",
            "『埃尔赛尤号』正式投入使用\x01",
            "这一目标显然也就难以实现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉唉，\x01",
            "这个我明白啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "『埃尔赛尤号』\x01",
            "现在的导力引擎\x01",
            "也只是旧型号的翻版而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "总之，\x01",
            "眼下必须赶快选出代替的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就将这看作是\x01",
            "重新策划的机会，\x01",
            "我们要以积极的工作态度去应对。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5256")

    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_5266")

    Return()

    # Function_14_4F8C end

    def Function_15_5267(): pass

    label("Function_15_5267")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5340")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_52B2")

    ChrTalk(
        0xFE,
        (
            "采暖用的导力器\x01",
            "竟然有那么多种……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，头痛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5340")

    label("loc_52B2")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "怎么办啊……真为难。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我一说想要\x01",
            "采暖用的导力器，\x01",
            "他就拿出厚厚一摞清单让我看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟然有那么多种……\x01",
            "究竟都是些什么我完全不懂。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5340")

    TalkEnd(0xFE)
    Return()

    # Function_15_5267 end

    def Function_16_5344(): pass

    label("Function_16_5344")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53A0")

    ChrTalk(
        0x102,
        (
            "#010F这边是出去的路……\x02\x03",
            "要是出去的话，\x01",
            "把安东尼留在工房里比较好。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53E1")

    label("loc_53A0")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#014F要出去吗？\x02\x03",
            "那样的话，\x01",
            "还是让安东尼回去比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5404")

    def lambda_53FC():
        TurnDirection(0x0, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_53FC)

    label("loc_5404")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5427")

    def lambda_541F():
        TurnDirection(0x1, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_541F)

    label("loc_5427")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_544A")

    def lambda_5442():
        TurnDirection(0x2, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5442)

    label("loc_544A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_546D")

    def lambda_5465():
        TurnDirection(0x3, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5465)

    label("loc_546D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5490")

    def lambda_5488():
        TurnDirection(0x4, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_5488)

    label("loc_5490")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【外出】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54FF")
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    label("loc_54FF")


    ChrTalk(
        0x102,
        (
            "#010F那么，安东尼。\x01",
            "我们就暂时在这里分开吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13C, 0x102, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x13C,
        "喵～呜。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3B, 0xFF)
    NewScene("ED6_DT01/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x2)
    Return()

    # Function_16_5344 end

    def Function_17_5565(): pass

    label("Function_17_5565")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55C1")

    ChrTalk(
        0x102,
        (
            "#010F这边是出去的路……\x02\x03",
            "要是出去的话，\x01",
            "把安东尼留在工房里比较好。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5602")

    label("loc_55C1")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#014F要出去吗？\x02\x03",
            "那样的话，\x01",
            "还是让安东尼回去比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5602")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5625")

    def lambda_561D():
        TurnDirection(0x0, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_561D)

    label("loc_5625")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5648")

    def lambda_5640():
        TurnDirection(0x1, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5640)

    label("loc_5648")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_566B")

    def lambda_5663():
        TurnDirection(0x2, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5663)

    label("loc_566B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_568E")

    def lambda_5686():
        TurnDirection(0x3, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5686)

    label("loc_568E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56B1")

    def lambda_56A9():
        TurnDirection(0x4, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_56A9)

    label("loc_56B1")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【外出】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5720")
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    label("loc_5720")


    ChrTalk(
        0x102,
        (
            "#010F那么，安东尼。\x01",
            "我们就暂时在这里分开吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13C, 0x102, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x13C,
        "喵～呜。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3B, 0xFF)
    NewScene("ED6_DT01/R3403   ._SN", 101, 0, 0)
    IdleLoop()
    EventEnd(0x2)
    Return()

    # Function_17_5565 end

    def Function_18_5786(): pass

    label("Function_18_5786")

    Call(0, 11)
    Return()

    # Function_18_5786 end

    def Function_19_578B(): pass

    label("Function_19_578B")

    Call(0, 8)
    Return()

    # Function_19_578B end

    def Function_20_5790(): pass

    label("Function_20_5790")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5810")
    TurnDirection(0x107, 0x1, 400)

    ChrTalk(
        0x107,
        (
            "#560F啊，\x01",
            "这个门是通往紧急通道的楼梯呢。\x02\x03",
            "要去一楼的话，\x01",
            "还是从左边的门回到走廊，\x01",
            "然后一直走比较快。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5881")

    label("loc_5810")

    TurnDirection(0x107, 0x0, 400)

    ChrTalk(
        0x107,
        (
            "#560F啊，\x01",
            "这个门是通往紧急通道的楼梯呢。\x02\x03",
            "要去一楼的话，\x01",
            "还是从左边的门回到走廊，\x01",
            "然后一直走比较快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5881")

    TalkEnd(0xFF)
    Return()

    # Function_20_5790 end

    def Function_21_5885(): pass

    label("Function_21_5885")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, -109900, 0, -101300, 180)
    SetChrPos(0x102, -110700, 0, -100900, 180)
    SetChrPos(0x107, -109300, 0, -100900, 180)

    ChrTalk(
        0x101,
        "#004F哇～这、这里……\x02",
    )

    CloseMessageWindow()

    def lambda_58E0():
        OP_8E(0xFE, 0xFFFE4F30, 0x0, 0xFFFE65D8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58E0)

    def lambda_58FB():
        OP_8E(0xFE, 0xFFFE4A80, 0x0, 0xFFFE66A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58FB)

    def lambda_5916():
        OP_8E(0xFE, 0xFFFE52B4, 0x0, 0xFFFE6510, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5916)
    OP_6D(-110500, 0, -107800, 2000)

    ChrTalk(
        0x102,
        (
            "#014F好厉害……\x01",
            "是全自动化的工场啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F嘿嘿……\x01",
            "这就是蔡斯市地下\x01",
            "庞大的导力器工场入口。\x02\x03",
            "从照明灯到飞艇部件，\x01",
            "全部都是在这里制造的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F哈～……\x01",
            "感觉好有压迫感呀。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_21_5885 end

    def Function_22_59F9(): pass

    label("Function_22_59F9")

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

    def lambda_5A7F():
        OP_6D(-4950, 0, 6440, 4000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5A7F)

    def lambda_5A97():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_5A97)
    WaitChrThread(0x107, 0x2)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    Sleep(500)

    def lambda_5ABB():
        OP_8E(0xFE, 0xFFFFECDC, 0x0, 0x1130, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5ABB)
    Sleep(500)
    OP_8E(0x107, 0xFFFFEC78, 0x0, 0x1DB0, 0xBB8, 0x0)

    def lambda_5AEF():
        OP_8E(0xFE, 0xFFFFF060, 0x0, 0x170C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5AEF)
    Sleep(200)

    def lambda_5B0F():
        OP_8E(0xFE, 0xFFFFE8F4, 0x0, 0x157C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B0F)
    Sleep(1000)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#501F哎～\x01",
            "这个地方好大呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#060F这里就是中央工房的一楼了。\x02\x03",
            "这里除了有接待柜台，\x01",
            "还有面向一般客人的导力器维修柜台。\x01",
            "所以说这里每天都是很热闹的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此。\x01",
            "从这里就能通往城镇了吧。\x02",
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
        "啊，提妲。\x02",
    )

    CloseMessageWindow()

    def lambda_5C46():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C46)

    def lambda_5C54():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5C54)

    def lambda_5C62():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C62)
    OP_6D(-1900, 0, 7200, 1500)

    ChrTalk(
        0x107,
        "#064F啊，海泽尔姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你来得正好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "特莱斯主任\x01",
            "刚才在找你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "说要你去一趟演算室。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊……\x01",
            "好的，我明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F哎呀呀。\x01",
            "看来你好像有急事呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D31():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D31)

    def lambda_5D3F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5D3F)

    def lambda_5D4D():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D4D)

    def lambda_5D5B():
        OP_6D(-4950, 0, 6440, 1500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5D5B)
    OP_8C(0x8, 180, 400)
    OP_4B(0x8, 255)
    WaitChrThread(0x107, 0x2)

    ChrTalk(
        0x102,
        (
            "#010F谢谢你。\x01",
            "要你特地带我们到城里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F哪、哪儿的话。\x02\x03",
            "刚才承蒙哥哥你们的照顾，\x01",
            "该说谢谢的其实是我才对呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F对了，提妲。\x01",
            "我们两个会在蔡斯呆一段时间。\x02\x03",
            "有机会的话，来找我们玩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064F啊……\x02\x03",
            "#067F好呢，非常乐意！\x02\x03",
            "那么，再见啦！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5E85():

        label("loc_5E85")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_5E85")

    QueueWorkItem2(0x101, 1, lambda_5E85)

    def lambda_5E96():

        label("loc_5E96")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_5E96")

    QueueWorkItem2(0x102, 1, lambda_5E96)
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
            "#019F哈哈，很可爱的孩子啊。\x01",
            "给人一种努力向上的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯嗯，同感！\x02\x03",
            "#507F啊～啊，要是我也有一个\x01",
            "那么活泼那么可爱的妹妹就好啦。\x02\x03",
            "不像某个弟弟那样，\x01",
            "一点也不可爱，老是麻烦人家～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F我可是有好几次想提醒你，\x01",
            "一直在照顾你的其实是我吧。\x02\x03",
            "想摆姐姐的架子，\x01",
            "就要表现得更加可靠才行哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#509F哼，我才不用你瞎操心。\x02\x03",
            "#000F闲话少说……\x01",
            "还是快去城里看看吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊，\x01",
            "首先要去协会打个招呼。\x02\x03",
            "然后还要……\x01",
            "和协会的人商量一下\x01",
            "父亲和那个黑色导力器的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯……没错。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x107, -4900, 0, 4400, 0)
    SetChrFlags(0x107, 0x80)
    ClearMapFlags(0x10000000)
    EventEnd(0x0)
    RemoveParty(0x6, 0xFF)
    Return()

    # Function_22_59F9 end

    def Function_23_6124(): pass

    label("Function_23_6124")

    OP_A2(0x540)
    OP_A3(0x541)
    OP_A3(0x542)
    OP_A3(0x543)
    OP_A3(0x544)
    OP_A3(0x545)
    OP_A3(0x546)
    Return()

    # Function_23_6124 end

    def Function_24_613A(): pass

    label("Function_24_613A")

    OP_A3(0x540)
    OP_A2(0x541)
    OP_A3(0x542)
    OP_A3(0x543)
    OP_A3(0x544)
    OP_A3(0x545)
    OP_A3(0x546)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_629C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_629C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_629C")
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
        "#004F看，导力梯里面……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F爷爷不在呢……\x01",
            "他们果然是在一楼停下的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F这么说来，\x01",
            "犯人是从正门逃走的吗……\x02\x03",
            "门外有那么多人看着，\x01",
            "他们究竟打算怎么离开呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#054F别管那么多了，快！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x535)
    EventEnd(0x0)
    Jump("loc_629C")

    label("loc_629C")

    Return()

    # Function_24_613A end

    def Function_25_629D(): pass

    label("Function_25_629D")

    OP_A2(0x519)
    OP_28(0x3F, 0x1, 0x1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3F, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_62B7")
    OP_28(0x3F, 0x1, 0x2000)

    label("loc_62B7")

    OP_71(0x8, 0x4)
    OP_64(0x0, 0x1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "汽油罐\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x367, 1)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_629D end

    def Function_26_630D(): pass

    label("Function_26_630D")

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
            "#002F#1P呜哇……\x01",
            "里面还真是烟雾弥漫啊。\x02\x03",
            "#505F咦……闻起来，\x01",
            "这烟好像又不怎么呛人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#6P这种烟雾……\x01",
            "应该是扰乱用的烟幕。\x02\x03",
            "据我推测……\x01",
            "这座建筑物的地上应该放有发烟筒。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F#1P咦……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x107,
        "#065F为、为什么会有那种东西……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x107, 400)

    ChrTalk(
        0x102,
        (
            "#012F#6P这就不得而知了……\x02\x03",
            "只要把发烟筒破坏掉的话，\x01",
            "我想烟雾很快就会消散的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#1P明白了。\x01",
            "找到发烟筒就马上把它破坏掉……\x02\x03",
            "拉赛尔博士\x01",
            "应该还在三楼的工作室吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F嗯、嗯……\x01",
            "我想应该还在那里……\x02\x03",
            "爷爷在专注于研究的时候，\x01",
            "是完全不会注意周围的情况的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#012F#6P总之去三楼看看吧。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_26_630D end

    def Function_27_65B0(): pass

    label("Function_27_65B0")

    Return()

    # Function_27_65B0 end

    def Function_28_65B1(): pass

    label("Function_28_65B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67FB")
    EventBegin(0x0)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_6D(-4900, 0, 8380, 1000)
    OP_A2(0x52E)
    OP_28(0x41, 0x1, 0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6635")

    ChrTalk(
        0x101,
        (
            "#004F咦……？\x01",
            "自动门打不开。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F导力断了吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6701")

    label("loc_6635")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6685")

    ChrTalk(
        0x102,
        (
            "#013F奇怪……\x01",
            "自动门没有反应。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦，导力停掉了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6701")

    label("loc_6685")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6701")
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "提妲按下按钮。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x107,
        (
            "#065F咦、咦咦……\x01",
            "自动门怎么打不开。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦，导力停掉了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_6701")


    ChrTalk(
        0x107,
        (
            "#063F唔唔……\x01",
            "好像还在运作啊。\x02\x03",
            "也许……\x01",
            "是谁正在使用导力梯吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F是谁正在……\x01",
            "难道是拉赛尔博士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F不，这一点不能马上断定。\x01",
            "为什么导力梯没有马上下来……\x02\x03",
            "既然这样的话，\x01",
            "要想上去就必须走紧急通道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F嗯……是呢。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_685A")

    label("loc_67FB")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "按了按钮，没有任何反应。\x01",
            "导力梯好像不能用了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_685A")

    Return()

    # Function_28_65B1 end

    def Function_29_685B(): pass

    label("Function_29_685B")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "按了按钮，没有任何反应。\x01",
            "导力梯好像不能用了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_29_685B end

    def Function_30_68C4(): pass

    label("Function_30_68C4")

    EventBegin(0x0)
    OP_A2(0x547)
    OP_64(0x1, 0x1)
    OP_2B(0x41, 0x1)
    OP_6D(-9770, 0, -3590, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C2F")
    OP_A2(0x52F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6949")

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "约修亚，这是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是刚才所说的发烟筒。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A47")

    label("loc_6949")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_699E")

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "约修亚，那是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯。\x01",
            "是刚才所说的发烟筒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A47")

    label("loc_699E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69F7")

    ChrTalk(
        0x107,
        (
            "#065F啊……\x01",
            "哥哥，这是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是刚才所说的发烟筒。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A47")

    label("loc_69F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A47")

    ChrTalk(
        0x106,
        (
            "#057F这个……\x01",
            "就是那发烟筒吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F阿加特兄。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A47")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚很熟练地把发烟筒拆散了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x102, -9340, 0, -4190, 315)
    SetChrPos(0x101, -10070, 0, -5250, 0)
    SetChrPos(0x107, -8820, 0, -5380, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_6AC5")
    SetChrPos(0x106, -9730, 0, -6460, 0)

    label("loc_6AC5")

    FadeToBright(600, 0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B7D")

    ChrTalk(
        0x101,
        (
            "#501F哇……\x01",
            "烟雾没有了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F约修亚哥哥，\x01",
            "好厉害……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FＯＫ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C2C")

    label("loc_6B7D")

    OP_A2(0x53E)

    ChrTalk(
        0x101,
        (
            "#501F哇……\x01",
            "烟雾没有了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F约修亚哥哥，\x01",
            "好厉害……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#052F哦……\x01",
            "还挺有两下子的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C2C")

    Jump("loc_6D3B")

    label("loc_6C2F")

    FadeToDark(600, 0, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚很熟练地把发烟筒拆散了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetChrPos(0x102, -9340, 0, -4190, 315)
    SetChrPos(0x101, -10070, 0, -5250, 0)
    SetChrPos(0x107, -8820, 0, -5380, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_6CB5")
    SetChrPos(0x106, -9730, 0, -6460, 0)

    label("loc_6CB5")

    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D3B")
    OP_A2(0x53E)

    ChrTalk(
        0x106,
        (
            "#052F哦……\x01",
            "还挺有两下子的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D3B")

    EventEnd(0x0)
    Return()

    # Function_30_68C4 end

    def Function_31_6D3E(): pass

    label("Function_31_6D3E")

    EventBegin(0x0)
    OP_A2(0x548)
    OP_64(0x2, 0x1)
    OP_2B(0x41, 0x1)
    OP_6D(-98280, -4000, -103420, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70A9")
    OP_A2(0x52F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DC3")

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "约修亚，这是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是刚才所说的发烟筒。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EC1")

    label("loc_6DC3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E18")

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "约修亚，那是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯。\x01",
            "是刚才所说的发烟筒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EC1")

    label("loc_6E18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E71")

    ChrTalk(
        0x107,
        (
            "#065F啊……\x01",
            "哥哥，这是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是刚才所说的发烟筒。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EC1")

    label("loc_6E71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EC1")

    ChrTalk(
        0x106,
        (
            "#057F这个……\x01",
            "就是那发烟筒吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F阿加特兄。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EC1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚很熟练地把发烟筒拆散了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x102, -98680, -4000, -105420, 315)
    SetChrPos(0x101, -99580, -4000, -106640, 45)
    SetChrPos(0x107, -98140, -4000, -106180, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_6F3F")
    SetChrPos(0x106, -98640, -4000, -107110, 45)

    label("loc_6F3F")

    FadeToBright(600, 0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FF7")

    ChrTalk(
        0x101,
        (
            "#501F哇……\x01",
            "烟雾没有了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F约修亚哥哥，\x01",
            "好厉害……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FＯＫ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_70A6")

    label("loc_6FF7")

    OP_A2(0x53E)

    ChrTalk(
        0x101,
        (
            "#501F哇……\x01",
            "烟雾没有了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F约修亚哥哥，\x01",
            "好厉害……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#052F哦……\x01",
            "还挺有两下子的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A6")

    Jump("loc_71B5")

    label("loc_70A9")

    FadeToDark(600, 0, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚很熟练地把发烟筒拆散了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetChrPos(0x102, -98680, -4000, -105420, 315)
    SetChrPos(0x101, -99580, -4000, -106640, 45)
    SetChrPos(0x107, -98140, -4000, -106180, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_712F")
    SetChrPos(0x106, -98640, -4000, -107110, 45)

    label("loc_712F")

    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71B5")
    OP_A2(0x53E)

    ChrTalk(
        0x106,
        (
            "#052F哦……\x01",
            "还挺有两下子的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71B5")

    EventEnd(0x0)
    Return()

    # Function_31_6D3E end

    def Function_32_71B8(): pass

    label("Function_32_71B8")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7201")

    ChrTalk(
        0x101,
        (
            "#002F（啊，这边是出口啊。\x01",
            "　现在不是出去的时候。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72B6")

    label("loc_7201")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7250")

    ChrTalk(
        0x102,
        (
            "#012F（不能随便出去啊。\x01",
            "　现在要赶快在工房内部进行调查。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72B6")

    label("loc_7250")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7291")

    ChrTalk(
        0x107,
        (
            "#062F（啊，这边是出口。\x01",
            "　要赶快找到爷爷。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72B6")

    label("loc_7291")


    ChrTalk(
        0x106,
        "#050F（……没有时间再出去了。）\x02",
    )

    CloseMessageWindow()

    label("loc_72B6")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_32_71B8 end

    def Function_33_72D2(): pass

    label("Function_33_72D2")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_731D")

    ChrTalk(
        0x101,
        (
            "#002F（犯人好像逃到一楼去了。\x01",
            "　要赶快追上他们……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B6")

    label("loc_731D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_734B")

    ChrTalk(
        0x102,
        "#012F（要赶快去一楼……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_73B6")

    label("loc_734B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_738A")

    ChrTalk(
        0x107,
        (
            "#062F（爷爷好像被他们带到一楼去了……）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B6")

    label("loc_738A")


    ChrTalk(
        0x106,
        (
            "#050F（不是这边。\x01",
            "　他们去了一层……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73B6")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_33_72D2 end

    def Function_34_73D2(): pass

    label("Function_34_73D2")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_741B")

    ChrTalk(
        0x101,
        (
            "#002F（啊，这边是出口啊。\x01",
            "　现在不是出去的时候。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74D0")

    label("loc_741B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_746A")

    ChrTalk(
        0x102,
        (
            "#012F（现在还不是回去的时候。\x01",
            "　总之先在内部调查一下吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74D0")

    label("loc_746A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74AB")

    ChrTalk(
        0x107,
        (
            "#062F（啊，这边是出口。\x01",
            "　要赶快找到爷爷。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74D0")

    label("loc_74AB")


    ChrTalk(
        0x106,
        "#050F（……没有时间再出去了。）\x02",
    )

    CloseMessageWindow()

    label("loc_74D0")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_34_73D2 end

    def Function_35_74EC(): pass

    label("Function_35_74EC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "左·中央工房导力梯\x01",
            "右·地下导力器工场\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_35_74EC end

    def Function_36_7544(): pass

    label("Function_36_7544")

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
    Return()

    # Function_36_7544 end

    SaveToFile()

Try(main)
