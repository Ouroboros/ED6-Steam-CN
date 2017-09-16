from ED6ScenarioHelper import *

def main():
    # 主楼　社会系教室

    CreateScenaFile(
        FileName            = 'T2530   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2530.x',
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
        '科林兹校长',                           # 9
        '乔儿',                                 # 10
        '珐奥娜',                               # 11
        '拉迪奥老师',                           # 12
        '碧欧拉老师',                           # 13
        '米丽亚老师',                           # 14
        '艾福托老师',                           # 15
        '罗迪',                                 # 16
        '坎诺',                                 # 17
        '雅莉丝',                               # 18
        '黛拉',                                 # 19
        '帕布尔',                               # 20
        '罗基克',                               # 21
        '罗伊斯',                               # 22
        '塞尔玛',                               # 23
        '巴托姆',                               # 24
        '基诺奇奥',                             # 25
        '妮吉塔',                               # 26
        '戴尔蒙市长',                           # 27
        'CH22000',                              # 28
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
        'ED6_DT07/CH02600 ._CH',             # 00
        'ED6_DT07/CH02390 ._CH',             # 01
        'ED6_DT07/CH02490 ._CH',             # 02
        'ED6_DT07/CH01660 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT07/CH01430 ._CH',             # 05
        'ED6_DT07/CH01460 ._CH',             # 06
        'ED6_DT07/CH01360 ._CH',             # 07
        'ED6_DT07/CH01580 ._CH',             # 08
        'ED6_DT07/CH01590 ._CH',             # 09
        'ED6_DT07/CH01370 ._CH',             # 0A
        'ED6_DT07/CH01090 ._CH',             # 0B
        'ED6_DT07/CH01080 ._CH',             # 0C
        'ED6_DT06/CH20021 ._CH',             # 0D
        'ED6_DT07/CH01663 ._CH',             # 0E
        'ED6_DT07/CH01213 ._CH',             # 0F
        'ED6_DT07/CH01433 ._CH',             # 10
        'ED6_DT07/CH01463 ._CH',             # 11
        'ED6_DT07/CH02603 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH02600P._CP',             # 00
        'ED6_DT07/CH02390P._CP',             # 01
        'ED6_DT07/CH02490P._CP',             # 02
        'ED6_DT07/CH01660P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT07/CH01430P._CP',             # 05
        'ED6_DT07/CH01460P._CP',             # 06
        'ED6_DT07/CH01360P._CP',             # 07
        'ED6_DT07/CH01580P._CP',             # 08
        'ED6_DT07/CH01590P._CP',             # 09
        'ED6_DT07/CH01370P._CP',             # 0A
        'ED6_DT07/CH01090P._CP',             # 0B
        'ED6_DT07/CH01080P._CP',             # 0C
        'ED6_DT06/CH20021P._CP',             # 0D
        'ED6_DT07/CH01663P._CP',             # 0E
        'ED6_DT07/CH01213P._CP',             # 0F
        'ED6_DT07/CH01433P._CP',             # 10
        'ED6_DT07/CH01463P._CP',             # 11
        'ED6_DT07/CH02603P._CP',             # 12
    )

    DeclNpc(
        X                   = 116010,
        Z                   = 200,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 30700,
        Z                   = 0,
        Y                   = 55110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 41400,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 87700,
        Z                   = 0,
        Y                   = 1000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 87700,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 84400,
        Z                   = 0,
        Y                   = 1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 84400,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -2800,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -700,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -3100,
        Z                   = 0,
        Y                   = 5400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -2900,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -2600,
        Z                   = 0,
        Y                   = 30800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -6200,
        Z                   = 0,
        Y                   = 35300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 86000,
        Z                   = 0,
        Y                   = 30400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 86600,
        Z                   = 0,
        Y                   = 32700,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 84800,
        Z                   = 0,
        Y                   = 33200,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 85590,
        Z                   = 700,
        Y                   = 3050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835021,
        ChipIndex           = 0xD,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 51000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 33,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 35,
    )

    DeclEvent(
        X                   = 58990,
        Y                   = 0,
        Z                   = 31330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 31400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )


    DeclActor(
        TriggerX            = 85590,
        TriggerZ            = 700,
        TriggerY            = 3400,
        TriggerRange        = 1000,
        ActorX              = 85590,
        ActorZ              = 1000,
        ActorY              = 3050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 48200,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = 48200,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31580,
        TriggerZ            = 0,
        TriggerY            = 1450,
        TriggerRange        = 800,
        ActorX              = 31580,
        ActorZ              = 1000,
        ActorY              = 1450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51020,
        TriggerZ            = 0,
        TriggerY            = 31860,
        TriggerRange        = 800,
        ActorX              = 51020,
        ActorZ              = 1500,
        ActorY              = 31860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57380,
        TriggerZ            = 0,
        TriggerY            = 31460,
        TriggerRange        = 800,
        ActorX              = 57380,
        ActorZ              = 1000,
        ActorY              = 31460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31630,
        TriggerZ            = 0,
        TriggerY            = 31460,
        TriggerRange        = 800,
        ActorX              = 31630,
        ActorZ              = 1000,
        ActorY              = 31460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3420,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = 3420,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3570,
        TriggerZ            = 0,
        TriggerY            = 34450,
        TriggerRange        = 800,
        ActorX              = 3570,
        ActorZ              = 1200,
        ActorY              = 34450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 790,
        TriggerZ            = 0,
        TriggerY            = 35530,
        TriggerRange        = 800,
        ActorX              = 790,
        ActorZ              = 1200,
        ActorY              = 35530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5010,
        TriggerZ            = 0,
        TriggerY            = 29180,
        TriggerRange        = 800,
        ActorX              = -5010,
        ActorZ              = 1200,
        ActorY              = 29180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 31,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1970,
        TriggerZ            = 0,
        TriggerY            = 30780,
        TriggerRange        = 800,
        ActorX              = -1970,
        ActorZ              = 1200,
        ActorY              = 30780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41160,
        TriggerZ            = 0,
        TriggerY            = 6230,
        TriggerRange        = 400,
        ActorX              = 41400,
        ActorZ              = 1500,
        ActorY              = 7500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_612",          # 00, 0
        "Function_1_9F1",          # 01, 1
        "Function_2_A43",          # 02, 2
        "Function_3_BC0",          # 03, 3
        "Function_4_1478",         # 04, 4
        "Function_5_147D",         # 05, 5
        "Function_6_1E5C",         # 06, 6
        "Function_7_223E",         # 07, 7
        "Function_8_25CB",         # 08, 8
        "Function_9_2B32",         # 09, 9
        "Function_10_2F64",        # 0A, 10
        "Function_11_3161",        # 0B, 11
        "Function_12_358F",        # 0C, 12
        "Function_13_3847",        # 0D, 13
        "Function_14_3AD5",        # 0E, 14
        "Function_15_3B68",        # 0F, 15
        "Function_16_430A",        # 10, 16
        "Function_17_471A",        # 11, 17
        "Function_18_47AA",        # 12, 18
        "Function_19_481C",        # 13, 19
        "Function_20_4A15",        # 14, 20
        "Function_21_4C2C",        # 15, 21
        "Function_22_51D6",        # 16, 22
        "Function_23_523E",        # 17, 23
        "Function_24_52B3",        # 18, 24
        "Function_25_5319",        # 19, 25
        "Function_26_5395",        # 1A, 26
        "Function_27_5405",        # 1B, 27
        "Function_28_5470",        # 1C, 28
        "Function_29_54C4",        # 1D, 29
        "Function_30_5524",        # 1E, 30
        "Function_31_55A6",        # 1F, 31
        "Function_32_55FD",        # 20, 32
        "Function_33_565C",        # 21, 33
        "Function_34_5660",        # 22, 34
        "Function_35_5664",        # 23, 35
        "Function_36_5668",        # 24, 36
        "Function_37_566C",        # 25, 37
    )


    def Function_0_612(): pass

    label("Function_0_612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_668")
    SetChrPos(0xB, 5320, 250, 2110, 270)
    SetChrPos(0xC, 5300, 250, 32080, 267)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xF, 400, 0, 0, 90)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_9C1")

    label("loc_668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_6AE")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    Jump("loc_9C1")

    label("loc_6AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_740")
    SetChrPos(0xB, 1710, 0, 4970, 180)
    SetChrPos(0xC, -6910, 0, 33220, 90)
    SetChrPos(0xD, 95370, 250, 34220, 225)
    SetChrPos(0x8, 43470, 0, 5280, 225)
    SetChrPos(0x10, -7060, 0, 1680, 90)
    SetChrPos(0x11, 920, 0, -1500, 0)
    SetChrPos(0x12, -1590, 0, 34700, 0)
    SetChrPos(0x14, 1300, 0, 28510, 90)
    Jump("loc_9C1")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7C4")
    SetChrPos(0xB, 1710, 0, 4970, 180)
    SetChrPos(0xC, -6910, 0, 33220, 90)
    SetChrPos(0xD, 95370, 250, 34220, 225)
    SetChrPos(0x8, 42940, 0, 1070, 270)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x10, -7060, 0, 1680, 90)
    SetChrPos(0x11, 920, 0, -1500, 0)
    SetChrFlags(0x14, 0x80)
    Jump("loc_9C1")

    label("loc_7C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_887")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x10, -5200, 0, 2050, 0)
    SetChrPos(0x11, 4500, 250, 4019, 270)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x10)
    SetChrChipByIndex(0xD, 16)
    SetChrPos(0xD, 84450, 250, 2790, 90)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    OP_44(0xD, 0xFF)
    SetChrChipByIndex(0xB, 14)
    SetChrPos(0xB, 84450, 250, 1030, 90)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    OP_44(0xB, 0xFF)
    OP_44(0x8, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 18)
    Jump("loc_9C1")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_8BB")
    SetChrPos(0xC, 5300, 250, 32080, 267)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x15, 0x80)
    Jump("loc_9C1")

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_8F7")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jump("loc_9C1")

    label("loc_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_938")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jump("loc_9C1")

    label("loc_938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_97E")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jump("loc_9C1")

    label("loc_97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_9C1")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_9C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_9D1")
    SetChrFlags(0x1B, 0x80)

    label("loc_9D1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (114, "loc_9DD"),
        (SWITCH_DEFAULT, "loc_9F0"),
    )


    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9ED")
    Event(0, 21)

    label("loc_9ED")

    Jump("loc_9F0")

    label("loc_9F0")

    Return()

    # Function_0_612 end

    def Function_1_9F1(): pass

    label("Function_1_9F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A12")
    OP_B1("t2530_y")
    Jump("loc_A1B")

    label("loc_A12")

    OP_B1("t2530_n")

    label("loc_A1B")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_A2E")
    OP_65(0x0, 0x1)

    label("loc_A2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_A42")
    OP_64(0x0, 0x1)
    SetChrFlags(0x1B, 0x80)

    label("loc_A42")

    Return()

    # Function_1_9F1 end

    def Function_2_A43(): pass

    label("Function_2_A43")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A68")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_BAA")

    label("loc_A68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A81")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_BAA")

    label("loc_A81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_BAA")

    label("loc_A9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_BAA")

    label("loc_AB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACC")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_BAA")

    label("loc_ACC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE5")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_BAA")

    label("loc_AE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFE")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_BAA")

    label("loc_AFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B17")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_BAA")

    label("loc_B17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B30")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_BAA")

    label("loc_B30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B49")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_BAA")

    label("loc_B49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B62")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_BAA")

    label("loc_B62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_BAA")

    label("loc_B7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B94")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_BAA")

    label("loc_B94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_BAA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BBF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_BAA")

    label("loc_BBF")

    Return()

    # Function_2_A43 end

    def Function_3_BC0(): pass

    label("Function_3_BC0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_D38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9F")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#780F是艾丝蒂尔和约修亚啊。\x02\x03",
            "犯人总算给逮捕归案了，\x01",
            "实在是太好了。\x02\x03",
            "等会儿我想听你们\x01",
            "说明一下事情的经过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D35")

    label("loc_C9F")


    ChrTalk(
        0xFE,
        (
            "#780F抓到袭击孤儿院的犯人\x01",
            "总算是让大家安心了。\x02\x03",
            "你们等会儿可以把\x01",
            "把事情的经过告诉我吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D35")

    Jump("loc_1474")

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DED")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#780F艾丝蒂尔、约修亚……\x02\x03",
            "我听说特蕾莎院长的事情了。\x02\x03",
            "怎么说呢……\x01",
            "实在是很过分的事啊……\x02\x03",
            "这件事实在无法用语言表达……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4B")

    label("loc_DED")


    ChrTalk(
        0xFE,
        (
            "#780F我听说特蕾莎院长的事情了。\x02\x03",
            "怎么说呢……\x01",
            "实在是很过分的事啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4B")

    Jump("loc_1474")

    label("loc_E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F54")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#780F艾丝蒂尔、约修亚，\x01",
            "这次真是麻烦你们了。\x02\x03",
            "舞台剧的演出很成功。\x01",
            "特别是约修亚饰演的塞茜莉亚公主，\x01",
            "演技和扮相实在是太感人了。\x02\x03",
            "下次有机会的话\x01",
            "请务必再到我们学院来玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE7")

    label("loc_F54")


    ChrTalk(
        0xFE,
        (
            "#780F艾丝蒂尔、约修亚，\x01",
            "这次真是麻烦你们了。\x02\x03",
            "下次有机会的话\x01",
            "请务必再到我们学院来玩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE7")

    Jump("loc_1474")

    label("loc_FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_10FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109A")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#780F哦，是你们。\x01",
            "这次真是史无前例的盛况啊。\x02\x03",
            "大家都很期待舞台剧，\x01",
            "请务必让学园祭圆满成功。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FC")

    label("loc_109A")


    ChrTalk(
        0xFE,
        (
            "#780F大家都很期待舞台剧。\x01",
            "请务必让学园祭圆满成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FC")

    Jump("loc_1474")

    label("loc_10FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_12C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1208")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#780F戴尔蒙市长，\x01",
            "自从去年的王国会议之后我们也好久不见了。\x02\x03",
            "这段时间，你身体怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#660F就像你看到的，结实着呢。\x01",
            "科林兹校长也很精神嘛。\x02\x03",
            "今天我打算好好放松一下。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    Jump("loc_12BF")

    label("loc_1208")


    ChrTalk(
        0xFE,
        (
            "#780F我还要找时间和市长先生谈谈\x01",
            "关于学院运营的事情呢。\x01",
            "　\x02\x03",
            "虽说是王立的教育机构，\x01",
            "但也要重视地方上的建议。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BF")

    Jump("loc_1474")

    label("loc_12C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 0)), scpexpr(EXPR_END)), "loc_137A")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12EB")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1306")

    label("loc_12EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1301")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1306")

    label("loc_1301")

    SetChrSubChip(0xFE, 2)

    label("loc_1306")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0x8,
        (
            "#780F呵呵，可别玩得太过火，\x01",
            "影响到明天的活动就不好了哦。\x02\x03",
            "那么，你们开心地去玩吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_1474")

    label("loc_137A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1474")

    ChrTalk(
        0xFE,
        (
            "#780F你们住宿的地方我们已经给安排好了。\x01",
            "　\x02\x03",
            "学院里也有食堂，\x01",
            "你们就安心准备好舞台剧吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1474")

    TalkEnd(0x8)
    Return()

    # Function_3_BC0 end

    def Function_4_1478(): pass

    label("Function_4_1478")

    Call(0, 5)
    Return()

    # Function_4_1478 end

    def Function_5_147D(): pass

    label("Function_5_147D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1523")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1501")
    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "啊，怎么了？\x01",
            "你们要找人吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "现在正好是\x01",
            "上课结束的时间。\x01",
            "你们可以去和同学们见面。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1520")

    label("loc_1501")


    ChrTalk(
        0xA,
        (
            "啊，怎么了？\x01",
            "你们要找人吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1520")

    Jump("loc_1E58")

    label("loc_1523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_15B3")

    ChrTalk(
        0xA,
        "呵呵，学园祭很成功呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "学生们正在\x01",
            "礼堂那里庆祝胜利呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E58")

    label("loc_15B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_16D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167B")
    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "说起来\x01",
            "真是出乎意料的盛况啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "有很多带孩子来的家长，\x01",
            "我担心会有孩子走失。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D5")

    label("loc_167B")


    ChrTalk(
        0xA,
        "请问您想找哪位呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我可以使用广播\x01",
            "来帮您寻找想找的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D5")

    Jump("loc_1E58")

    label("loc_16D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_184B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E7")
    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "各种活动都在\x01",
            "校园和主楼里进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "下午礼堂那边\x01",
            "预定要演出舞台剧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "食堂作为休息场所开放，\x01",
            "你们可以好好利用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1848")

    label("loc_17E7")


    ChrTalk(
        0xA,
        (
            "为了以防万一，\x01",
            "学园祭举行的时候\x01",
            "宿舍楼都是锁住的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1848")

    Jump("loc_1E58")

    label("loc_184B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1910")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CE")
    OP_A2(0x1)

    ChrTalk(
        0xA,
        "准备完成了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "到了明天\x01",
            "就会有许多客人来参观了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_18CE")


    ChrTalk(
        0xA,
        (
            "准备完成了吗？\x01",
            "明天就要正式表演了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190D")

    Jump("loc_1E58")

    label("loc_1910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1A0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CA")
    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "呵呵，一到下课时间，\x01",
            "校园里就会变得热闹起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "学园祭就要开始了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "希望同学们\x01",
            "都能加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0A")

    label("loc_19CA")


    ChrTalk(
        0xA,
        (
            "呵呵，一到下课时间，\x01",
            "校园里就会变得热闹起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0A")

    Jump("loc_1E58")

    label("loc_1A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_1B87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1B")
    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "啊，科洛丝。\x01",
            "你回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F对不起，\x01",
            "我到现在才回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "呵呵，回来就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "要找校长的话，\x01",
            "他就在办公室里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "他也很担心\x01",
            "科洛丝你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F啊，是的。\x01",
            "我们现在就过去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B84")

    label("loc_1B1B")


    ChrTalk(
        0xA,
        (
            "要找校长的话，\x01",
            "他就在办公室里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "他也很担心\x01",
            "科洛丝你呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B84")

    Jump("loc_1E58")

    label("loc_1B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5F")
    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "啊，科洛丝。\x01",
            "你们外出回来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F啊，不是的……\x02\x03",
            "对不起，\x01",
            "我们还没有办完事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "是吗。\x01",
            "外出时请务必要小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1C5F")


    ChrTalk(
        0xA,
        (
            "科洛丝，\x01",
            "外出时请务必要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C81")

    Jump("loc_1E58")

    label("loc_1C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_1D03")

    ChrTalk(
        0xA,
        "啊，是想参观吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "很抱歉，\x01",
            "现在学生们正在上课，\x01",
            "不能带您参观。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E58")

    label("loc_1D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E07")
    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "啊，科洛丝。\x01",
            "已经回来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F不是，\x01",
            "我正要带这两位朋友去卢安呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "是吗，难得的假日，\x01",
            "就好好地放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F嗯，谢谢了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E58")

    label("loc_1E07")


    ChrTalk(
        0xA,
        (
            "科洛丝，\x01",
            "难得的假日，\x01",
            "就好好地放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E58")

    TalkEnd(0xA)
    Return()

    # Function_5_147D end

    def Function_6_1E5C(): pass

    label("Function_6_1E5C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1EAD")

    ChrTalk(
        0xFE,
        (
            "课虽然上完了，\x01",
            "但还有学生们的问题要回答。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223A")

    label("loc_1EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_1F23")

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "我们班的同学干劲热火朝天啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家做布景\x01",
            "也非常地努力嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223A")

    label("loc_1F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1F99")

    ChrTalk(
        0xFE,
        (
            "学园祭的主角\x01",
            "果然还是学生们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家都比平时\x01",
            "要活跃许多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223A")

    label("loc_1F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_218B")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FC2")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1FF3")

    label("loc_1FC2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FD8")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1FF3")

    label("loc_1FD8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FEE")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1FF3")

    label("loc_1FEE")

    SetChrSubChip(0xFE, 1)

    label("loc_1FF3")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20CF")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "你们好像是\x01",
            "从洛连特来的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实我也是\x01",
            "洛连特出身的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来我父母\x01",
            "也要来参观学园祭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……我要是能招待他们就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2183")

    label("loc_20CF")


    ChrTalk(
        0xFE,
        (
            "对了对了……\x01",
            "舞台剧表演我也看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是热闹啊。\x01",
            "那天真是很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2183")

    SetChrSubChip(0xFE, 0)
    Jump("loc_223A")

    label("loc_218B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_223A")

    ChrTalk(
        0xFE,
        (
            "学园祭快到了，\x01",
            "同学们就连上课\x01",
            "都开始坐不安定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵，这也是没办法的呀。\x02",
    )

    CloseMessageWindow()

    label("loc_223A")

    TalkEnd(0xB)
    Return()

    # Function_6_1E5C end

    def Function_7_223E(): pass

    label("Function_7_223E")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_22D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A1")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "唔唔，\x01",
            "这个问题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么做好呢？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    Jump("loc_22D3")

    label("loc_22A1")


    ChrTalk(
        0xFE,
        (
            "呼，这里的学生\x01",
            "都很热心于学习呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D3")

    Jump("loc_25C7")

    label("loc_22D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2341")

    ChrTalk(
        0xFE,
        (
            "下午终于要上演\x01",
            "万众瞩目的舞台剧了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "拜托你们二位了！\x01",
            "我相信一定能取得成功的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C7")

    label("loc_2341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2429")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F7")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "我们班的同学相当认真呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我觉得\x01",
            "研究发表什么的太朴素了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过这样也好，\x01",
            "有很多客人来看呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2426")

    label("loc_23F7")


    ChrTalk(
        0xFE,
        (
            "决不能输给\x01",
            "米丽亚的班级……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2426")

    Jump("loc_25C7")

    label("loc_2429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_25C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257F")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "啊，科洛丝。\x01",
            "你回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F碧欧拉老师，\x01",
            "我刚刚才回来。\x02\x03",
            "对不起，\x01",
            "我又没来上课。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵，没关系。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你不是有重要的事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有时间的话来一下办公室，\x01",
            "我给你漏下的上课笔记。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F嗯，我过会儿就去。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25C7")

    label("loc_257F")


    ChrTalk(
        0xFE,
        (
            "我还是趁现在\x01",
            "批改一下考试卷子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C7")

    TalkEnd(0xC)
    Return()

    # Function_7_223E end

    def Function_8_25CB(): pass

    label("Function_8_25CB")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2660")

    ChrTalk(
        0xFE,
        (
            "我是今年\x01",
            "入学考试的出题老师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我已经跃跃欲试了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B2E")

    label("loc_2660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2752")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EF")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "为什么我们班的同学\x01",
            "尽办些游戏和占卜的活动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "维奥拉的班级\x01",
            "都是很正经的东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_274F")

    label("loc_26EF")


    ChrTalk(
        0xFE,
        (
            "那个班的老师不行，\x01",
            "学生们却都很优秀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_274F")

    Jump("loc_2B2E")

    label("loc_2752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_27D6")

    ChrTalk(
        0xFE,
        "人还真是多呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "大家都很闲吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B2E")

    label("loc_27D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2942")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_27FF")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2830")

    label("loc_27FF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2815")
    SetChrSubChip(0xFE, 0)
    Jump("loc_2830")

    label("loc_2815")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_282B")
    SetChrSubChip(0xFE, 2)
    Jump("loc_2830")

    label("loc_282B")

    SetChrSubChip(0xFE, 1)

    label("loc_2830")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28EA")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "嗯，明天就能好好看到\x01",
            "同学们努力的成果了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论怎样，\x01",
            "那天我可不能再啰嗦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293A")

    label("loc_28EA")


    ChrTalk(
        0xFE,
        (
            "嗯，明天就能好好看到\x01",
            "同学们努力的成果了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_293A")

    SetChrSubChip(0xFE, 0)
    Jump("loc_2B2E")

    label("loc_2942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2B2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A64")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "在学园祭的准备期间，\x01",
            "大家学习都提不起精神来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算在课上\x01",
            "也开始不愿动脑筋了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要不要明天\x01",
            "来次突击测验呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B2E")

    label("loc_2A64")


    ChrTalk(
        0xFE,
        (
            "在学园祭的准备期间，\x01",
            "大家学习都提不起精神来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要不要明天\x01",
            "来次突击测验呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B2E")

    TalkEnd(0xD)
    Return()

    # Function_8_25CB end

    def Function_9_2B32(): pass

    label("Function_9_2B32")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2BB3")

    ChrTalk(
        0xFE,
        "嗯，差不多该去巡视了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要看看\x01",
            "有没有同学太过懒散了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F60")

    label("loc_2BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2D20")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2C5A")

    ChrTalk(
        0xFE,
        "哦，昨天真是辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我真是个不称职的老师啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了防止再发生突发事件，\x01",
            "我在这里待命。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D1D")

    label("loc_2C5A")


    ChrTalk(
        0xFE,
        (
            "昨天，\x01",
            "有学生说在旧校舍看到了魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了慎重起见，\x01",
            "我把旧校舍的门锁紧了。\x01",
            "不过一会儿还是再去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D1D")

    Jump("loc_2F60")

    label("loc_2D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_2EC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E18")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "这个学园一共设立了\x01",
            "三个方向的专业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我教的科目则是\x01",
            "所有专业都必修的科目——体育。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在这个时候我没有课，\x01",
            "就来整理一下教案了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC0")

    label("loc_2E18")


    ChrTalk(
        0xFE,
        (
            "我教的科目则是\x01",
            "所有专业都必修的科目——体育。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在这个时候我没有课，\x01",
            "就来整理一下教案了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC0")

    Jump("loc_2F60")

    label("loc_2EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2F60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F36")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "唔，怎么，\x01",
            "你们是哪个班的学生？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在正在上课哦。\x01",
            "要有外出许可证\x01",
            "才能出去哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F60")

    label("loc_2F36")


    ChrTalk(
        0xFE,
        (
            "要有外出许可证\x01",
            "才能出去哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F60")

    TalkEnd(0xE)
    Return()

    # Function_9_2B32 end

    def Function_10_2F64(): pass

    label("Function_10_2F64")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3026")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE9")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "今天的课总算上完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "下午的课\x01",
            "一定会睡着的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3023")

    label("loc_2FE9")


    ChrTalk(
        0xFE,
        (
            "下午的课\x01",
            "一定会睡着的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3023")

    Jump("loc_315D")

    label("loc_3026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_315D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30DA")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "我一直在照顾\x01",
            "我们社团的店面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "班里的活动\x01",
            "就没办法参加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，感觉真是很充实呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_315D")

    label("loc_30DA")


    ChrTalk(
        0xFE,
        (
            "我一直在照顾\x01",
            "我们社团的店面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "班里的活动\x01",
            "就没办法参加了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_315D")

    TalkEnd(0xF)
    Return()

    # Function_10_2F64 end

    def Function_11_3161(): pass

    label("Function_11_3161")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_31C4")

    ChrTalk(
        0xFE,
        "那么，该去社团活动了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天要把\x01",
            "画到一半的绘画完成！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_358B")

    label("loc_31C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_325A")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "茶座还是要办成这样才对啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "辛苦也值得了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_358B")

    label("loc_325A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3326")

    ChrTalk(
        0xFE,
        (
            "嗯，不管怎么说\x01",
            "准备工作还是赶上了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为通宵工作，\x01",
            "现在好困啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_358B")

    label("loc_3326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_342E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D4")
    OP_A2(0x7)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "唔哇哇！\x01",
            "怎么回事！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呆在这里\x01",
            "会来不及准备的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_342B")

    label("loc_33D4")


    ChrTalk(
        0xFE,
        (
            "……难道说\x01",
            "这样下去要通宵赶工了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "做衣服花了太多时间了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_342B")

    Jump("loc_358B")

    label("loc_342E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_358B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3554")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "啦啦啦～～⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我正在做\x01",
            "摆摊时穿的衣服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔～就是要在这种时候集中精力！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为做这种东西\x01",
            "是我最喜欢干的事情了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_358B")

    label("loc_3554")


    ChrTalk(
        0xFE,
        "接下来还要做房间的装饰。\x02",
    )

    CloseMessageWindow()

    label("loc_358B")

    TalkEnd(0x10)
    Return()

    # Function_11_3161 end

    def Function_12_358F(): pass

    label("Function_12_358F")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_35D4")

    ChrTalk(
        0xFE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果需要的话，\x01",
            "我可以帮你们找空位。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3843")

    label("loc_35D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_362F")

    ChrTalk(
        0xFE,
        "嘿嘿，这件制服很可爱吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "坎诺还为我准备了好多呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3843")

    label("loc_362F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_3709")

    ChrTalk(
        0xFE,
        (
            "一想时间还很充裕\x01",
            "就不由自主地松懈了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过应该还来得及。\x01",
            "努力把店面打扮得漂亮一些吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3843")

    label("loc_3709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_3843")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37CD")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "坎诺君的手\x01",
            "可巧啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次他缝了个\x01",
            "布娃娃给我呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3843")

    label("loc_37CD")


    ChrTalk(
        0xFE,
        (
            "就算是演出用的女佣服装\x01",
            "也是他自己做的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3843")

    TalkEnd(0x11)
    Return()

    # Function_12_358F end

    def Function_13_3847(): pass

    label("Function_13_3847")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3928")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "刚才讲的课，\x01",
            "有一些地方不明白……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "我还想问问老师呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "米丽亚老师\x01",
            "才刚上完课\x01",
            "就马上回办公室了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3973")

    label("loc_3928")


    ChrTalk(
        0xFE,
        (
            "米丽亚老师\x01",
            "才刚上完课\x01",
            "就马上回办公室了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3973")

    Jump("loc_3AD1")

    label("loc_3976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3AD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A70")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "社会系各位的作品\x01",
            "都是研究成果发表啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哇……真是厉害啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们系的同学\x01",
            "只会办茶座或者\x01",
            "鬼怪屋什么的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD1")

    label("loc_3A70")


    ChrTalk(
        0xFE,
        (
            "社会系各位的作品\x01",
            "都是研究成果发表啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哇……真是厉害啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3AD1")

    TalkEnd(0x12)
    Return()

    # Function_13_3847 end

    def Function_14_3AD5(): pass

    label("Function_14_3AD5")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3B09")

    ChrTalk(
        0xFE,
        (
            "欢迎光临。\x01",
            "这里是我们的茶座『芳塔娜』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B64")

    label("loc_3B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3B64")

    ChrTalk(
        0xFE,
        (
            "穿成这个样子\x01",
            "虽然有点不好意思，\x01",
            "但为了学园祭，忍了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B64")

    TalkEnd(0x13)
    Return()

    # Function_14_3AD5 end

    def Function_15_3B68(): pass

    label("Function_15_3B68")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3BA4")

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "今天也是很有意义的一课啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4306")

    label("loc_3BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C91")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "虽然办娱乐活动很有意思，\x01",
            "不过让大家知道我们\x01",
            "平日的研究成果也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尤其是有很多前辈\x01",
            "和市民们前来参观。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……虽说如此，\x01",
            "考试也不会得到更高的分数。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D1F")

    label("loc_3C91")


    ChrTalk(
        0xFE,
        (
            "虽然办娱乐活动很有意思，\x01",
            "不过让大家知道我们\x01",
            "平日的研究成果也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D1F")

    Jump("loc_4306")

    label("loc_3D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4150")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_3EBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E89")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "我们社会系发表了\x01",
            "从各种产业的经济指标上\x01",
            "进行经济动向的预测的研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且也收集了\x01",
            "通俗易懂的关于卢安地区\x01",
            "历史和发展的资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "如果有兴趣的话就请看一下吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EBA")

    label("loc_3E89")


    ChrTalk(
        0xFE,
        "如果有兴趣的话就请看一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3EBA")

    Jump("loc_414D")

    label("loc_3EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402B")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "我们社会系发表了\x01",
            "从各种产业的经济指标上\x01",
            "进行经济动向的预测的研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且也收集了\x01",
            "通俗易懂的关于卢安地区\x01",
            "历史和发展的资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然有几份资料没到手，\x01",
            "但在这么点时间里，\x01",
            "能做成这么完善的内容也算不错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "如果有兴趣的话就请看一下吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_414D")

    label("loc_402B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_411C")

    ChrTalk(
        0xFE,
        (
            "虽然没赶上这次发表，\x01",
            "但是《卢安经济史》是很贵重的资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果你们看到那三本书的话，\x01",
            "麻烦帮我放回资料室的书架上。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_414D")

    label("loc_411C")


    ChrTalk(
        0xFE,
        "如果有兴趣的话就请看一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_414D")

    Jump("loc_4306")

    label("loc_4150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_415A")
    Jump("loc_4306")

    label("loc_415A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_4306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E4")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "啊，科洛丝。\x01",
            "你终于回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们班级的节目\x01",
            "准备工作进展得很顺利啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们舞台剧方面怎么样了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说连主要演员\x01",
            "都还没决定下来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F呵呵，罗基克，\x01",
            "那件事已经解决了。\x02\x03",
            "舞台剧方面我们不会输的。\x01",
            "敬请期待哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那我们互相加油吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4306")

    label("loc_42E4")


    ChrTalk(
        0xFE,
        "科洛丝，我们互相加油吧。\x02",
    )

    CloseMessageWindow()

    label("loc_4306")

    TalkEnd(0x14)
    Return()

    # Function_15_3B68 end

    def Function_16_430A(): pass

    label("Function_16_430A")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_43B7")

    ChrTalk(
        0xFE,
        (
            "这次的女王诞辰庆典上\x01",
            "要召开武术大会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们的击剑部\x01",
            "也好想参加啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4716")

    label("loc_43B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_44E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_446F")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "我太过忙于班里的活动，\x01",
            "连社团开的店\x01",
            "都没能去帮上忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "等到店员需要换班的时候\x01",
            "我再过去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44E2")

    label("loc_446F")


    ChrTalk(
        0xFE,
        (
            "来这里参观的人\x01",
            "真是多啊……\x01",
            "还有热心人问了我们很多问题呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44E2")

    Jump("loc_4716")

    label("loc_44E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_460F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_459A")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "我是从卡尔瓦德共和国\x01",
            "来这里进修的留学生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次我从研究发表的\x01",
            "准备中也学到不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我认为这是很有意义的一件事情。\x02",
    )

    CloseMessageWindow()
    Jump("loc_460C")

    label("loc_459A")


    ChrTalk(
        0xFE,
        (
            "我是从卡尔瓦德共和国\x01",
            "来这里进修的留学生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次我从研究发表的\x01",
            "准备中也学到不少。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_460C")

    Jump("loc_4716")

    label("loc_460F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46AA")
    OP_A2(0xC)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        "啊，科洛丝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们班的活动\x01",
            "大致都准备好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过罗基克\x01",
            "好像还有些不放心，\x01",
            "去了资料室。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4716")

    label("loc_46AA")


    ChrTalk(
        0xFE,
        (
            "我们班的活动\x01",
            "大致都准备好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过罗基克\x01",
            "好像还有些不放心，\x01",
            "去了资料室。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4716")

    TalkEnd(0x15)
    Return()

    # Function_16_430A end

    def Function_17_471A(): pass

    label("Function_17_471A")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4782")
    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "罗基克真是个完美主义者啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得这样\x01",
            "就已经足够了嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47A6")

    label("loc_4782")


    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "罗基克真是个完美主义者啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47A6")

    TalkEnd(0x16)
    Return()

    # Function_17_471A end

    def Function_18_47AA(): pass

    label("Function_18_47AA")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4818")

    ChrTalk(
        0xFE,
        (
            "这两个人是青梅竹马，\x01",
            "都是住在卢安市里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，关系总是那么好，\x01",
            "真让人羡慕呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4818")

    TalkEnd(0x17)
    Return()

    # Function_18_47AA end

    def Function_19_481C(): pass

    label("Function_19_481C")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49F4")
    TalkBegin(0x19)
    OP_A2(0xF)
    OP_A2(0x10)

    ChrTalk(
        0x18,
        "……喂，妮吉塔。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)
    OP_62(0x19, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x18,
        "这样应该就可以了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "明天早上收尾，\x01",
            "叫大家一起来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "你怎么老是\x01",
            "说那么天真的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "其他同学\x01",
            "还有他们要办的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "再说一般早上起来都会很忙，\x01",
            "都不知道有没有空来帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "哦，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "好饿啊，肚子好饿啊。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x19, 0x10)
    ClearChrFlags(0x18, 0x10)
    TalkEnd(0x19)
    Jump("loc_4A11")

    label("loc_49F4")


    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "好饿啊，肚子好饿啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A11")

    TalkEnd(0x18)
    Return()

    # Function_19_481C end

    def Function_20_4A15(): pass

    label("Function_20_4A15")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4C28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BED")
    TalkBegin(0x18)
    OP_A2(0xF)
    OP_A2(0x10)

    ChrTalk(
        0x18,
        "喂，妮吉塔。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)
    OP_62(0x19, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x18,
        "这样应该就可以了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "明天早上收尾，\x01",
            "叫大家一起来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "你怎么老是\x01",
            "说那么天真的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "其他同学\x01",
            "还有他们要办的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "再说一般早上起来\x01",
            "大家都会很忙，\x01",
            "都不知道有没有空来帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "哦，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "好饿啊，肚子好饿啊。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x19, 0x10)
    ClearChrFlags(0x18, 0x10)
    TalkEnd(0x18)
    Jump("loc_4C28")

    label("loc_4BED")


    ChrTalk(
        0xFE,
        (
            "怎么办，\x01",
            "这样下去会来不及的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C28")

    TalkEnd(0x19)
    Return()

    # Function_20_4A15 end

    def Function_21_4C2C(): pass

    label("Function_21_4C2C")

    AddParty(0x3A, 0xFF)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(116200, 0, 4240, 0)
    SetChrPos(0x101, 116870, 0, -3740, 0)
    SetChrPos(0x105, 116870, 0, -3740, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x105, 0x80)
    OP_4A(0x8, 255)
    SetChrPos(0x13B, 115990, 0, 2740, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x13B,
        (
            "#643F#4P原来如此……\x01",
            "这主意的确一举两得！\x02\x03",
            "#641F不愧是校长，太英明了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#781F哈哈哈……\x01",
            "拍我马屁也不会给你奖励哦。\x02\x03",
            "#780F这样的话，\x01",
            "名单就交给你负责行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13B,
        "#644F#4P没问题，包在我身上！\x02",
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x101,
        "#1P打扰了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_4DB7():
        OP_6D(117520, 0, 2870, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4DB7)

    def lambda_4DCF():
        OP_8E(0xFE, 0x1CAF2, 0x0, 0x5B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DCF)

    def lambda_4DEA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4DEA)
    Sleep(700)

    def lambda_4E01():
        OP_8E(0xFE, 0x1C75A, 0x0, 0x1CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4E01)

    def lambda_4E1C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_4E1C)
    OP_8C(0x13B, 180, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 315, 0)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x105,
        (
            "#044F啊，对不起……\x01",
            "没有打扰你们谈话吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#781F不不。\x01",
            "刚好谈完了。\x02\x03",
            "其实是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x8, 400)

    ChrTalk(
        0x13B,
        (
            "#646F哎呀，校长！\x01",
            "别这么快说出来啦！\x02\x03",
            "让大家知道的话，\x01",
            "明天就没有什么惊喜了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13B, 400)

    ChrTalk(
        0x101,
        (
            "#008F#2P是、是什么？\x01",
            "好像神神秘秘的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F乔儿真是的……\x01",
            "又在打什么鬼主意了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x105, 400)

    ChrTalk(
        0x13B,
        (
            "#649F呵、呵、呵……\x01",
            "这就等着明天揭晓吧。\x02\x03",
            "#640F倒是你们来做什么？\x01",
            "找我有事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F嗯，其实是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "科洛丝告诉乔儿等会大家在食堂共进晚餐，\x01",
            "同时预祝明天学园祭成功的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x13B,
        (
            "#640F啊，不错啊。\x02\x03",
            "#641F那么，为了预祝明天学园祭的成功，\x01",
            "我们今晚就好好热闹一下吧。\x02\x03",
            "痛痛快快玩一场，痛痛快快地！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#780F呵呵，可别玩得太过火，\x01",
            "影响到明天的活动就不好了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#2P那么，乔儿。\x01",
            "一起去食堂吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13B,
        "#644F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x448)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_21_4C2C end

    def Function_22_51D6(): pass

    label("Function_22_51D6")

    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x1B, 0x80)
    OP_64(0x0, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "卢安经济史·中\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x33E, 1)
    OP_28(0x27, 0x1, 0x80)
    TalkEnd(0xFF)
    Return()

    # Function_22_51D6 end

    def Function_23_523E(): pass

    label("Function_23_523E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　前面是校长室和办公室　　　　\x01",
            "※谢绝外来人员进入。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_23_523E end

    def Function_24_52B3(): pass

    label("Function_24_52B3")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "人文系模拟店铺\x01",
            "茶座『芳塔娜』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_52B3 end

    def Function_25_5319(): pass

    label("Function_25_5319")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　走　\x01",
            "　　廊　\x01",
            "　　里　\x01",
            "　　请　\x01",
            "　　保　\x01",
            "　学持　\x01",
            "　生安　\x01",
            "　指静　\x01",
            "　导！　\x01",
            "　部　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_5319 end

    def Function_26_5395(): pass

    label("Function_26_5395")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "自然系成果展示\x01",
            "『结晶回路与导力技术』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_5395 end

    def Function_27_5405(): pass

    label("Function_27_5405")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　社会系成果展示\x01",
            "『卢安地区的历史与经济』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_5405 end

    def Function_28_5470(): pass

    label("Function_28_5470")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "欢迎光临！\x01",
            "这里是茶座『芳塔娜』！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_28_5470 end

    def Function_29_54C4(): pass

    label("Function_29_54C4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里分析了导力器产业的发展动向。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_29_54C4 end

    def Function_30_5524(): pass

    label("Function_30_5524")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里用图表展示了每年观光客数量的变化。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_30_5524 end

    def Function_31_55A6(): pass

    label("Function_31_55A6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里整理了国内主要产品的出口方向。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_31_55A6 end

    def Function_32_55FD(): pass

    label("Function_32_55FD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里归纳了人口移动的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_32_55FD end

    def Function_33_565C(): pass

    label("Function_33_565C")

    SetPlaceName(0x6F) # 主楼　社会系教室
    Return()

    # Function_33_565C end

    def Function_34_5660(): pass

    label("Function_34_5660")

    SetPlaceName(0x5E) # 主楼　社会系教室
    Return()

    # Function_34_5660 end

    def Function_35_5664(): pass

    label("Function_35_5664")

    SetPlaceName(0x6E) # 主楼　社会系教室
    Return()

    # Function_35_5664 end

    def Function_36_5668(): pass

    label("Function_36_5668")

    SetPlaceName(0x74) # 主楼　社会系教室
    Return()

    # Function_36_5668 end

    def Function_37_566C(): pass

    label("Function_37_566C")

    SetPlaceName(0x73) # 主楼　社会系教室
    Return()

    # Function_37_566C end

    SaveToFile()

Try(main)
