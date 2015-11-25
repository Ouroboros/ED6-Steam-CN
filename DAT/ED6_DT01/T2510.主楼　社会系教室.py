from ED6ScenarioHelper import *

def main():
    # 主楼　社会系教室

    CreateScenaFile(
        FileName            = 'T2510   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2510.x',
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
        '汉斯',                                 # 11
        '男学生',                               # 12
        '男学生',                               # 13
        '男学生',                               # 14
        '女学生',                               # 15
        '女教师',                               # 16
        '珐奥娜',                               # 17
        '拉迪奥老师',                           # 18
        '碧欧拉老师',                           # 19
        '米丽亚老师',                           # 20
        '艾福托老师',                           # 21
        '罗迪',                                 # 22
        '坎诺',                                 # 23
        '雅莉丝',                               # 24
        '黛拉',                                 # 25
        '帕布尔',                               # 26
        '罗基克',                               # 27
        '罗伊斯',                               # 28
        '莫妮卡',                               # 29
        '塞尔玛',                               # 30
        '基诺奇奥',                             # 31
        '妮吉塔',                               # 32
        '梅贝尔市长',                           # 33
        '戴尔蒙市长',                           # 34
        'CH22000',                              # 35
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
        'ED6_DT07/CH02393 ._CH',             # 01
        'ED6_DT07/CH02553 ._CH',             # 02
        'ED6_DT07/CH01360 ._CH',             # 03
        'ED6_DT07/CH01370 ._CH',             # 04
        'ED6_DT07/CH01430 ._CH',             # 05
        'ED6_DT07/CH02490 ._CH',             # 06
        'ED6_DT07/CH01660 ._CH',             # 07
        'ED6_DT07/CH01210 ._CH',             # 08
        'ED6_DT07/CH01430 ._CH',             # 09
        'ED6_DT07/CH01460 ._CH',             # 0A
        'ED6_DT07/CH01360 ._CH',             # 0B
        'ED6_DT07/CH01580 ._CH',             # 0C
        'ED6_DT07/CH01590 ._CH',             # 0D
        'ED6_DT07/CH01370 ._CH',             # 0E
        'ED6_DT07/CH01090 ._CH',             # 0F
        'ED6_DT07/CH01080 ._CH',             # 10
        'ED6_DT07/CH01580 ._CH',             # 11
        'ED6_DT07/CH02360 ._CH',             # 12
        'ED6_DT07/CH00003 ._CH',             # 13
        'ED6_DT07/CH00013 ._CH',             # 14
        'ED6_DT07/CH00043 ._CH',             # 15
        'ED6_DT07/CH01363 ._CH',             # 16
        'ED6_DT07/CH01083 ._CH',             # 17
        'ED6_DT07/CH01583 ._CH',             # 18
        'ED6_DT07/CH01373 ._CH',             # 19
        'ED6_DT07/CH01663 ._CH',             # 1A
        'ED6_DT07/CH01213 ._CH',             # 1B
        'ED6_DT07/CH01433 ._CH',             # 1C
        'ED6_DT07/CH01463 ._CH',             # 1D
        'ED6_DT07/CH01593 ._CH',             # 1E
        'ED6_DT07/CH01093 ._CH',             # 1F
        'ED6_DT07/CH02603 ._CH',             # 20
        'ED6_DT06/CH20021 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT07/CH02600P._CP',             # 00
        'ED6_DT07/CH02393P._CP',             # 01
        'ED6_DT07/CH02553P._CP',             # 02
        'ED6_DT07/CH01360P._CP',             # 03
        'ED6_DT07/CH01370P._CP',             # 04
        'ED6_DT07/CH01210P._CP',             # 05
        'ED6_DT07/CH02490P._CP',             # 06
        'ED6_DT07/CH01660P._CP',             # 07
        'ED6_DT07/CH01210P._CP',             # 08
        'ED6_DT07/CH01430P._CP',             # 09
        'ED6_DT07/CH01460P._CP',             # 0A
        'ED6_DT07/CH01360P._CP',             # 0B
        'ED6_DT07/CH01580P._CP',             # 0C
        'ED6_DT07/CH01590P._CP',             # 0D
        'ED6_DT07/CH01370P._CP',             # 0E
        'ED6_DT07/CH01090P._CP',             # 0F
        'ED6_DT07/CH01080P._CP',             # 10
        'ED6_DT07/CH01580P._CP',             # 11
        'ED6_DT07/CH02360P._CP',             # 12
        'ED6_DT07/CH00003P._CP',             # 13
        'ED6_DT07/CH00013P._CP',             # 14
        'ED6_DT07/CH00043P._CP',             # 15
        'ED6_DT07/CH01363P._CP',             # 16
        'ED6_DT07/CH01083P._CP',             # 17
        'ED6_DT07/CH01583P._CP',             # 18
        'ED6_DT07/CH01373P._CP',             # 19
        'ED6_DT07/CH01663P._CP',             # 1A
        'ED6_DT07/CH01213P._CP',             # 1B
        'ED6_DT07/CH01433P._CP',             # 1C
        'ED6_DT07/CH01463P._CP',             # 1D
        'ED6_DT07/CH01593P._CP',             # 1E
        'ED6_DT07/CH01093P._CP',             # 1F
        'ED6_DT07/CH02603P._CP',             # 20
        'ED6_DT06/CH20021P._CP',             # 21
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
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
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
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
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
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 84450,
        Z                   = 250,
        Y                   = 1030,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 84450,
        Z                   = 250,
        Y                   = 2790,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 87540,
        Z                   = 250,
        Y                   = 2770,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 4490,
        Z                   = 250,
        Y                   = 34880,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 4790,
        Z                   = 250,
        Y                   = -1130,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 5400,
        Z                   = 300,
        Y                   = 30500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 3040,
        Z                   = 0,
        Y                   = 35050,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 85800,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 84080,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -3900,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Unknown3            = 1835041,
        ChipIndex           = 0x21,
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
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = 58990,
        Y                   = 0,
        Z                   = 31330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 31400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )


    DeclActor(
        TriggerX            = 33000,
        TriggerZ            = 0,
        TriggerY            = 2190,
        TriggerRange        = 800,
        ActorX              = 33000,
        ActorZ              = 1000,
        ActorY              = 2190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33000,
        TriggerZ            = 0,
        TriggerY            = 32200,
        TriggerRange        = 800,
        ActorX              = 33000,
        ActorZ              = 1000,
        ActorY              = 32200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59000,
        TriggerZ            = 0,
        TriggerY            = 32000,
        TriggerRange        = 800,
        ActorX              = 59000,
        ActorZ              = 1000,
        ActorY              = 32000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41200,
        TriggerZ            = 0,
        TriggerY            = 5490,
        TriggerRange        = 400,
        ActorX              = 41400,
        ActorZ              = 1500,
        ActorY              = 7500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
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
        TriggerX            = 85590,
        TriggerZ            = 700,
        TriggerY            = 3400,
        TriggerRange        = 1000,
        ActorX              = 85590,
        ActorZ              = 1000,
        ActorY              = 3050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_692",          # 00, 0
        "Function_1_ADC",          # 01, 1
        "Function_2_B61",          # 02, 2
        "Function_3_CDE",          # 03, 3
        "Function_4_1520",         # 04, 4
        "Function_5_1525",         # 05, 5
        "Function_6_1F7F",         # 06, 6
        "Function_7_233C",         # 07, 7
        "Function_8_26EC",         # 08, 8
        "Function_9_2C99",         # 09, 9
        "Function_10_312F",        # 0A, 10
        "Function_11_332C",        # 0B, 11
        "Function_12_373F",        # 0C, 12
        "Function_13_39F7",        # 0D, 13
        "Function_14_3BA2",        # 0E, 14
        "Function_15_3C35",        # 0F, 15
        "Function_16_44FF",        # 10, 16
        "Function_17_45A6",        # 11, 17
        "Function_18_45F2",        # 12, 18
        "Function_19_479B",        # 13, 19
        "Function_20_48B5",        # 14, 20
        "Function_21_4B17",        # 15, 21
        "Function_22_4E76",        # 16, 22
        "Function_23_5672",        # 17, 23
        "Function_24_5A5E",        # 18, 24
        "Function_25_5B54",        # 19, 25
        "Function_26_5BB8",        # 1A, 26
        "Function_27_5C20",        # 1B, 27
        "Function_28_5C24",        # 1C, 28
        "Function_29_5C28",        # 1D, 29
        "Function_30_5C2C",        # 1E, 30
        "Function_31_5C30",        # 1F, 31
    )


    def Function_0_692(): pass

    label("Function_0_692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7A9")
    SetChrPos(0x11, 5320, 250, 2110, 270)
    SetChrPos(0x16, -3060, 0, 3170, 45)
    SetChrPos(0x15, 560, 100, 240, 90)
    SetChrChipByIndex(0x15, 22)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x10)
    OP_44(0x15, 0xFF)
    SetChrPos(0x12, 5300, 250, 32080, 180)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x1B, -1100, 0, 32240, 270)
    SetChrChipByIndex(0x1D, 31)
    SetChrPos(0x1D, -2660, 100, 32180, 90)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x10)
    OP_44(0x1D, 0xFF)
    SetChrChipByIndex(0x1A, 23)
    SetChrPos(0x1A, -5950, 100, 34220, 90)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x10)
    OP_44(0x1A, 0xFF)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 86430, 0, 31990, 90)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, 95400, 250, 31050, 90)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x13, 28)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x10)
    OP_44(0x13, 0xFF)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x8, 32)
    Jump("loc_A78")

    label("loc_7A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_7F4")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x8, 32)
    Jump("loc_A78")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_886")
    SetChrPos(0x11, 1710, 0, 4970, 180)
    SetChrPos(0x12, -6910, 0, 33220, 90)
    SetChrPos(0x13, 95370, 250, 34220, 225)
    SetChrPos(0x8, 42950, 0, 1120, 270)
    SetChrPos(0x16, -7060, 0, 1680, 90)
    SetChrPos(0x17, 920, 0, -1500, 0)
    SetChrPos(0x18, -1590, 0, 34700, 0)
    SetChrPos(0x1A, 1300, 0, 28510, 90)
    Jump("loc_A78")

    label("loc_886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_91B")
    SetChrPos(0x11, 1710, 0, 4970, 180)
    SetChrPos(0x12, -6910, 0, 33220, 90)
    SetChrPos(0x13, 95370, 250, 34220, 225)
    SetChrPos(0x8, 43470, 0, 5280, 225)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x16, -7060, 0, 1680, 90)
    SetChrPos(0x17, 920, 0, -1500, 0)
    SetChrPos(0x1A, 1300, 0, 28510, 90)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_A78")

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_976")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrPos(0x16, -5200, 0, 2050, 0)
    SetChrPos(0x17, 4500, 250, 4019, 270)
    SetChrPos(0x1A, 790, 0, 34680, 0)
    SetChrChipByIndex(0x8, 32)
    Jump("loc_A78")

    label("loc_976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_A27")
    SetChrPos(0x12, 5300, 250, 32080, 90)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x13, 28)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x10)
    OP_44(0x13, 0xFF)
    SetChrChipByIndex(0x11, 26)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x10)
    OP_44(0x11, 0xFF)
    SetChrChipByIndex(0x16, 24)
    SetChrPos(0x16, -2650, 100, 4200, 90)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x10)
    OP_44(0x16, 0xFF)
    SetChrChipByIndex(0x1F, 30)
    SetChrPos(0x1F, 84120, 100, 30200, 90)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x10)
    OP_44(0x1F, 0xFF)
    SetChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x8, 32)
    Jump("loc_A78")

    label("loc_A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_A78")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1D, 0x80)
    OP_44(0x8, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 32)

    label("loc_A78")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (114, "loc_A84"),
        (SWITCH_DEFAULT, "loc_AB5"),
    )


    label("loc_A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AB2")
    OP_A2(0x42F)
    OP_71(0x1, 0x10)
    OP_71(0x2, 0x10)
    OP_71(0x3, 0x10)
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    Event(0, 22)

    label("loc_AB2")

    Jump("loc_AB5")

    label("loc_AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_ADB")
    OP_A3(0x3FA)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1D, 0x80)
    Event(0, 23)
    OP_B1("t2510_n")

    label("loc_ADB")

    Return()

    # Function_0_692 end

    def Function_1_ADC(): pass

    label("Function_1_ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AFD")
    OP_B1("t2510_y")
    Jump("loc_B06")

    label("loc_AFD")

    OP_B1("t2510_n")

    label("loc_B06")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B39")
    OP_72(0x1, 0x10)
    OP_72(0x2, 0x10)
    OP_72(0x3, 0x10)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)

    label("loc_B39")

    OP_64(0x5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_B4C")
    OP_65(0x5, 0x1)

    label("loc_B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_B60")
    OP_64(0x5, 0x1)
    SetChrFlags(0x22, 0x80)

    label("loc_B60")

    Return()

    # Function_1_ADC end

    def Function_2_B61(): pass

    label("Function_2_B61")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B86")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_CC8")

    label("loc_B86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9F")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_CC8")

    label("loc_B9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB8")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_CC8")

    label("loc_BB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD1")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_CC8")

    label("loc_BD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEA")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_CC8")

    label("loc_BEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C03")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_CC8")

    label("loc_C03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1C")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_CC8")

    label("loc_C1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C35")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_CC8")

    label("loc_C35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4E")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_CC8")

    label("loc_C4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C67")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_CC8")

    label("loc_C67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C80")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_CC8")

    label("loc_C80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C99")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_CC8")

    label("loc_C99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB2")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_CC8")

    label("loc_CB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC8")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_CC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CDD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_CC8")

    label("loc_CDD")

    Return()

    # Function_2_B61 end

    def Function_3_CDE(): pass

    label("Function_3_CDE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_EF3")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D0A")
    SetChrSubChip(0xFE, 1)
    Jump("loc_D25")

    label("loc_D0A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D20")
    SetChrSubChip(0xFE, 0)
    Jump("loc_D25")

    label("loc_D20")

    SetChrSubChip(0xFE, 2)

    label("loc_D25")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E52")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#782F哦哦，是艾丝蒂尔和约修亚啊。\x02\x03",
            "我和戴尔蒙市长交往多年了，\x01",
            "自己也对这次事件深感震惊。\x01",
            "　\x02\x03",
            "#783F他的行为的确难以原谅，\x01",
            "而且也没有人会原谅他……\x02\x03",
            "我祈祷他能对自己\x01",
            "误入歧途犯下的罪行感到忏悔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EEB")

    label("loc_E52")


    ChrTalk(
        0xFE,
        (
            "#783F他的行为的确难以原谅，\x01",
            "而且也没有人会原谅他……\x02\x03",
            "我祈祷他能对自己\x01",
            "误入歧途犯下的罪行感到忏悔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEB")

    SetChrSubChip(0xFE, 0)
    Jump("loc_151C")

    label("loc_EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_10FD")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F1C")
    SetChrSubChip(0xFE, 1)
    Jump("loc_F37")

    label("loc_F1C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F32")
    SetChrSubChip(0xFE, 0)
    Jump("loc_F37")

    label("loc_F32")

    SetChrSubChip(0xFE, 2)

    label("loc_F37")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1062")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#780F艾丝蒂尔、约修亚。\x01",
            "这次实在是麻烦你们了。\x02\x03",
            "舞台剧我看了哦，\x01",
            "真的是十分精彩。\x02\x03",
            "特别是约修亚饰演的塞茜莉亚公主，\x01",
            "演技和扮相实在是太感人了。\x02\x03",
            "下次有机会的话\x01",
            "请务必再到我们学院来玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F5")

    label("loc_1062")


    ChrTalk(
        0xFE,
        (
            "#780F话说回来，\x01",
            "能帮上特蕾莎老师实在是太好了。\x02\x03",
            "那次纵火事件实在让孩子们受苦了啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F5")

    SetChrSubChip(0xFE, 0)
    Jump("loc_151C")

    label("loc_10FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_1211")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AC")
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
    Jump("loc_120E")

    label("loc_11AC")


    ChrTalk(
        0xFE,
        (
            "#780F大家都很期待舞台剧。\x01",
            "请务必让学园祭圆满成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120E")

    Jump("loc_151C")

    label("loc_1211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_13D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131A")
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
        0x21,
        (
            "#660F就像你看到的，结实着呢。\x01",
            "科林兹校长也很精神嘛。\x02\x03",
            "今天我打算好好放松一下。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    Jump("loc_13D1")

    label("loc_131A")


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

    label("loc_13D1")

    Jump("loc_151C")

    label("loc_13D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_151C")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13FD")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1418")

    label("loc_13FD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1413")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1418")

    label("loc_1413")

    SetChrSubChip(0xFE, 2)

    label("loc_1418")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)

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
    SetChrSubChip(0xFE, 0)

    label("loc_151C")

    TalkEnd(0x8)
    Return()

    # Function_3_CDE end

    def Function_4_1520(): pass

    label("Function_4_1520")

    Call(0, 5)
    Return()

    # Function_4_1520 end

    def Function_5_1525(): pass

    label("Function_5_1525")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1602")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B2")
    OP_A2(0x1)

    ChrTalk(
        0x10,
        (
            "啊，怎么了？\x01",
            "你们要找人吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "现在正好是\x01",
            "上课结束的时间。\x01",
            "我想大家都在校园里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FF")

    label("loc_15B2")


    ChrTalk(
        0x10,
        (
            "现在正好是\x01",
            "上课结束的时间。\x01",
            "我想大家都在校园里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FF")

    Jump("loc_1F7B")

    label("loc_1602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_1692")

    ChrTalk(
        0x10,
        "呵呵，学园祭很成功呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "学生们正在\x01",
            "礼堂那里庆祝胜利呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7B")

    label("loc_1692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_17B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175A")
    OP_A2(0x1)

    ChrTalk(
        0x10,
        (
            "说起来\x01",
            "真是出乎意料的盛况啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "有很多带孩子来的家长，\x01",
            "我担心会有孩子走失。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B4")

    label("loc_175A")


    ChrTalk(
        0x10,
        "请问您想找哪位呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "我可以使用广播\x01",
            "来帮您寻找想找的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B4")

    Jump("loc_1F7B")

    label("loc_17B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_192A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C6")
    OP_A2(0x1)

    ChrTalk(
        0x10,
        (
            "各种活动都在\x01",
            "校园和主楼里进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "下午礼堂那边\x01",
            "预定要演出舞台剧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "食堂作为休息场所开放，\x01",
            "你们可以好好利用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1927")

    label("loc_18C6")


    ChrTalk(
        0x10,
        (
            "为了以防万一，\x01",
            "学园祭举行的时候\x01",
            "宿舍楼都是锁住的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1927")

    Jump("loc_1F7B")

    label("loc_192A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C6")
    OP_A2(0x1)

    ChrTalk(
        0x10,
        (
            "准备完成了吗？\x01",
            "明天就要正式表演了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "到了明天\x01",
            "就会有许多客人来参观了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A05")

    label("loc_19C6")


    ChrTalk(
        0x10,
        (
            "准备完成了吗？\x01",
            "明天就要正式表演了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A05")

    Jump("loc_1F7B")

    label("loc_1A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABA")
    OP_A2(0x1)

    ChrTalk(
        0x10,
        (
            "一到下课时间，\x01",
            "校园里就会变得热闹起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "离学园祭没多久了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "同学们也都在\x01",
            "拼命加油呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1F")

    label("loc_1ABA")


    ChrTalk(
        0x10,
        "离学园祭没多久了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "同学们也都在\x01",
            "拼命加油呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1F")

    Jump("loc_1F7B")

    label("loc_1B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_1CAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C37")
    OP_A2(0x1)
    TurnDirection(0x10, 0x105, 0)

    ChrTalk(
        0x10,
        "啊，科洛丝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F对不起，珐奥娜，\x01",
            "我到现在才回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "呵呵，回来就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "要找校长的话，\x01",
            "他就在办公室里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
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
    Jump("loc_1CA7")

    label("loc_1C37")

    TurnDirection(0x10, 0x105, 0)

    ChrTalk(
        0x10,
        (
            "要找校长的话，\x01",
            "他就在办公室里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "他也很担心\x01",
            "科洛丝你呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA7")

    Jump("loc_1F7B")

    label("loc_1CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1DA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D82")
    OP_A2(0x1)

    ChrTalk(
        0x10,
        (
            "啊，科洛丝。\x01",
            "你外出回来了吗？\x02",
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
        0x10,
        (
            "是吗。\x01",
            "外出时请务必要小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA4")

    label("loc_1D82")


    ChrTalk(
        0x10,
        (
            "科洛丝，\x01",
            "外出时请务必要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA4")

    Jump("loc_1F7B")

    label("loc_1DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_1E26")

    ChrTalk(
        0x10,
        "啊，是想参观吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "很抱歉，\x01",
            "现在学生们正在上课，\x01",
            "不能带您参观。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7B")

    label("loc_1E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1F7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2A")
    OP_A2(0x1)

    ChrTalk(
        0x10,
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
        0x10,
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
    Jump("loc_1F7B")

    label("loc_1F2A")


    ChrTalk(
        0x10,
        (
            "科洛丝，\x01",
            "难得的假日，\x01",
            "就好好地放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7B")

    TalkEnd(0x10)
    Return()

    # Function_5_1525 end

    def Function_6_1F7F(): pass

    label("Function_6_1F7F")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1FD0")

    ChrTalk(
        0xFE,
        (
            "课虽然上完了，\x01",
            "但还有学生们的问题要回答。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2338")

    label("loc_1FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2046")

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
    Jump("loc_2338")

    label("loc_2046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_20BC")

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
    Jump("loc_2338")

    label("loc_20BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2225")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2193")
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
    Jump("loc_2222")

    label("loc_2193")


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
        "那天真是很开心啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2222")

    Jump("loc_2338")

    label("loc_2225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2338")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_224E")
    SetChrSubChip(0xFE, 1)
    Jump("loc_227F")

    label("loc_224E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2264")
    SetChrSubChip(0xFE, 0)
    Jump("loc_227F")

    label("loc_2264")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_227A")
    SetChrSubChip(0xFE, 2)
    Jump("loc_227F")

    label("loc_227A")

    SetChrSubChip(0xFE, 1)

    label("loc_227F")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)

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
    SetChrSubChip(0xFE, 0)

    label("loc_2338")

    TalkEnd(0x11)
    Return()

    # Function_6_1F7F end

    def Function_7_233C(): pass

    label("Function_7_233C")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_23F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23BB")
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
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "怎么做好呢？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    Jump("loc_23ED")

    label("loc_23BB")


    ChrTalk(
        0xFE,
        (
            "呼，这里的学生\x01",
            "都很热心于学习呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23ED")

    Jump("loc_26E8")

    label("loc_23F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_245B")

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
    Jump("loc_26E8")

    label("loc_245B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2543")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2511")
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
    Jump("loc_2540")

    label("loc_2511")


    ChrTalk(
        0xFE,
        (
            "决不能输给\x01",
            "米丽亚的班级……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2540")

    Jump("loc_26E8")

    label("loc_2543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_26E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A0")
    OP_A2(0x3)
    TurnDirection(0xFE, 0x105, 0)

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
            "对不起……\x01",
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
    Jump("loc_26E8")

    label("loc_26A0")


    ChrTalk(
        0xFE,
        (
            "我还是趁现在\x01",
            "批改一下考试卷子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E8")

    TalkEnd(0x12)
    Return()

    # Function_7_233C end

    def Function_8_26EC(): pass

    label("Function_8_26EC")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_27E5")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2718")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2749")

    label("loc_2718")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_272E")
    SetChrSubChip(0xFE, 0)
    Jump("loc_2749")

    label("loc_272E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2744")
    SetChrSubChip(0xFE, 2)
    Jump("loc_2749")

    label("loc_2744")

    SetChrSubChip(0xFE, 1)

    label("loc_2749")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)

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
    SetChrSubChip(0xFE, 0)
    Jump("loc_2C95")

    label("loc_27E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_28D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2874")
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
    Jump("loc_28D4")

    label("loc_2874")


    ChrTalk(
        0xFE,
        (
            "那个班的老师不行，\x01",
            "学生们却都很优秀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D4")

    Jump("loc_2C95")

    label("loc_28D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_293D")

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
    Jump("loc_2C95")

    label("loc_293D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2A45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F2")
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
    Jump("loc_2A42")

    label("loc_29F2")


    ChrTalk(
        0xFE,
        (
            "嗯，明天就能好好看到\x01",
            "同学们努力的成果了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A42")

    Jump("loc_2C95")

    label("loc_2A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2C95")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A6E")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2A9F")

    label("loc_2A6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A84")
    SetChrSubChip(0xFE, 0)
    Jump("loc_2A9F")

    label("loc_2A84")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A9A")
    SetChrSubChip(0xFE, 2)
    Jump("loc_2A9F")

    label("loc_2A9A")

    SetChrSubChip(0xFE, 1)

    label("loc_2A9F")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC6")
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
    Jump("loc_2C90")

    label("loc_2BC6")


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

    label("loc_2C90")

    SetChrSubChip(0xFE, 0)

    label("loc_2C95")

    TalkEnd(0x13)
    Return()

    # Function_8_26EC end

    def Function_9_2C99(): pass

    label("Function_9_2C99")

    TalkBegin(0x14)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CBE")
    SetChrSubChip(0xFE, 2)
    Jump("loc_2CEF")

    label("loc_2CBE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CD4")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2CEF")

    label("loc_2CD4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CEA")
    SetChrSubChip(0xFE, 0)
    Jump("loc_2CEF")

    label("loc_2CEA")

    SetChrSubChip(0xFE, 2)

    label("loc_2CEF")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2D79")

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
    Jump("loc_3126")

    label("loc_2D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2EE6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2E20")

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
    Jump("loc_2EE3")

    label("loc_2E20")


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

    label("loc_2EE3")

    Jump("loc_3126")

    label("loc_2EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_3089")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FDE")
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
    Jump("loc_3086")

    label("loc_2FDE")


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

    label("loc_3086")

    Jump("loc_3126")

    label("loc_3089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3126")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30FC")
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
    Jump("loc_3126")

    label("loc_30FC")


    ChrTalk(
        0xFE,
        (
            "要有外出许可证\x01",
            "才能出去哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3126")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0x14)
    Return()

    # Function_9_2C99 end

    def Function_10_312F(): pass

    label("Function_10_312F")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_31F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B4")
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
            "一定会睡着的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31EE")

    label("loc_31B4")


    ChrTalk(
        0xFE,
        (
            "下午的课\x01",
            "一定会睡着的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31EE")

    Jump("loc_3328")

    label("loc_31F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A5")
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
    Jump("loc_3328")

    label("loc_32A5")


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

    label("loc_3328")

    TalkEnd(0x15)
    Return()

    # Function_10_312F end

    def Function_11_332C(): pass

    label("Function_11_332C")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_338F")

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
    Jump("loc_373B")

    label("loc_338F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3425")

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
    Jump("loc_373B")

    label("loc_3425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_34E7")

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
    Jump("loc_373B")

    label("loc_34E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_35D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_357E")
    OP_A2(0x7)

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
    Jump("loc_35D5")

    label("loc_357E")


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

    label("loc_35D5")

    Jump("loc_373B")

    label("loc_35D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_373B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36DA")
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
        (
            "唔～就是要在\x01",
            "这种时候集中精力！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_373B")

    label("loc_36DA")


    ChrTalk(
        0xFE,
        (
            "因为做这种东西\x01",
            "是我最喜欢干的事情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了对了，\x01",
            "接下来还要做房间的装饰。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_373B")

    TalkEnd(0x16)
    Return()

    # Function_11_332C end

    def Function_12_373F(): pass

    label("Function_12_373F")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3784")

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
    Jump("loc_39F3")

    label("loc_3784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_37DF")

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
    Jump("loc_39F3")

    label("loc_37DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_38B9")

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
    Jump("loc_39F3")

    label("loc_38B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_39F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397D")
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
    Jump("loc_39F3")

    label("loc_397D")


    ChrTalk(
        0xFE,
        (
            "就算是演出用的女佣服装\x01",
            "也是他自己做的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39F3")

    TalkEnd(0x17)
    Return()

    # Function_12_373F end

    def Function_13_39F7(): pass

    label("Function_13_39F7")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3A43")

    ChrTalk(
        0xFE,
        (
            "就算是再微小的问题，\x01",
            "拉迪奥老师也会\x01",
            "很仔细地给我讲解。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B9E")

    label("loc_3A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3B9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B3D")
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
    Jump("loc_3B9E")

    label("loc_3B3D")


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

    label("loc_3B9E")

    TalkEnd(0x18)
    Return()

    # Function_13_39F7 end

    def Function_14_3BA2(): pass

    label("Function_14_3BA2")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3BD6")

    ChrTalk(
        0xFE,
        (
            "欢迎光临。\x01",
            "这里是我们的茶座『芳塔娜』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C31")

    label("loc_3BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3C31")

    ChrTalk(
        0xFE,
        (
            "穿成这个样子\x01",
            "虽然有点不好意思，\x01",
            "但为了学园祭，忍了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C31")

    TalkEnd(0x19)
    Return()

    # Function_14_3BA2 end

    def Function_15_3C35(): pass

    label("Function_15_3C35")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3C71")

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "今天也是很有意义的一课啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44FB")

    label("loc_3C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3DEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D5E")
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
    Jump("loc_3DEC")

    label("loc_3D5E")


    ChrTalk(
        0xFE,
        (
            "虽然办娱乐活动很有意思，\x01",
            "不过让大家知道我们\x01",
            "平日的研究成果也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DEC")

    Jump("loc_44FB")

    label("loc_3DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_421D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_3F8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F56")
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
    Jump("loc_3F87")

    label("loc_3F56")


    ChrTalk(
        0xFE,
        "如果有兴趣的话就请看一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3F87")

    Jump("loc_421A")

    label("loc_3F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F8")
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
    Jump("loc_421A")

    label("loc_40F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_41E9")

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
    Jump("loc_421A")

    label("loc_41E9")


    ChrTalk(
        0xFE,
        "如果有兴趣的话就请看一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_421A")

    Jump("loc_44FB")

    label("loc_421D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4341")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42EF")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "还是需要一些辅助研究的资料啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "时间不够了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过在有限的时间里，\x01",
            "内容已经可算是做得很完善了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_433E")

    label("loc_42EF")


    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "还是需要一些辅助研究的资料啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_433E")

    Jump("loc_44FB")

    label("loc_4341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_44FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44D2")
    OP_A2(0xB)
    TurnDirection(0xFE, 0x105, 0)

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
    Jump("loc_44FB")

    label("loc_44D2")

    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        "科洛丝，我们互相加油吧。\x02",
    )

    CloseMessageWindow()

    label("loc_44FB")

    TalkEnd(0x1A)
    Return()

    # Function_15_3C35 end

    def Function_16_44FF(): pass

    label("Function_16_44FF")

    TalkBegin(0x1B)

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
    TalkEnd(0x1B)
    Return()

    # Function_16_44FF end

    def Function_17_45A6(): pass

    label("Function_17_45A6")

    TalkBegin(0x1C)

    ChrTalk(
        0xFE,
        "啊，老师，是这里。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从这里开始\x01",
            "就完全不明白了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1C)
    Return()

    # Function_17_45A6 end

    def Function_18_45F2(): pass

    label("Function_18_45F2")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_4670")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "今天是弓道部的练习日。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一直在准备学园祭，\x01",
            "好久没有休息了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4797")

    label("loc_4670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4719")
    OP_A2(0xE)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "啊，科洛丝。\x01",
            "你回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们差不多\x01",
            "该开始装饰教室了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "先从可以着手的地方\x01",
            "开始进行吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4797")

    label("loc_4719")


    ChrTalk(
        0xFE,
        (
            "我们差不多\x01",
            "该开始装饰教室了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "先从可以着手的地方\x01",
            "开始进行吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4797")

    TalkEnd(0x1D)
    Return()

    # Function_18_45F2 end

    def Function_19_479B(): pass

    label("Function_19_479B")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_4838")

    ChrTalk(
        0xFE,
        "今天的课上完了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也没参加社团活动，\x01",
            "那就快点回家去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B1")

    label("loc_4838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_48B1")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "首先是要去采购呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要把列表上的东西\x01",
            "都买过来就行了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B1")

    TalkEnd(0x1E)
    Return()

    # Function_19_479B end

    def Function_20_48B5(): pass

    label("Function_20_48B5")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_49C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4972")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "唔，我正想要问老师\x01",
            "没听明白的地方呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "米丽亚老师一上完课\x01",
            "就马上回办公室了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C6")

    label("loc_4972")


    ChrTalk(
        0xFE,
        (
            "我答应今天要去\x01",
            "姐姐的店里帮忙，\x01",
            "必须快点回去了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49C6")

    Jump("loc_4B13")

    label("loc_49C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_4B13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC4")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "为什么你老是那么草率啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家都很忙，\x01",
            "人手也不足，\x01",
            "你提高点效率好不好？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了买东西在卢安\x01",
            "和学园之间往返了好几次呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B13")

    label("loc_4AC4")


    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "基诺奇奥做事真是很粗心呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B13")

    TalkEnd(0x1F)
    Return()

    # Function_20_48B5 end

    def Function_21_4B17(): pass

    label("Function_21_4B17")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4E72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE7")
    OP_A2(0x11)

    ChrTalk(
        0x101,
        "#000F啊，梅贝尔市长？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#610F啊，是艾丝蒂尔和约修亚！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F您为什么会在这里呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#610F呵呵，其实我是\x01",
            "这个学院的毕业生。\x02\x03",
            "每年的学园祭都要来出席的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哦，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#610F那么你们俩是为什么来这儿的啊？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嘿嘿，其实呢……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔\x01",
            "向梅贝尔市长说明了事情的经过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0xFE,
        (
            "#610F哦，是协助演出啊。\x02\x03",
            "我也认为演出是很考功夫的。\x01",
            "　\x02\x03",
            "呵呵，连艾丝蒂尔\x01",
            "和约修亚也参加演出的话，\x01",
            "那我真要好好看看才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（唉，真不想让\x01",
            "认识的人看到啊……）\x02",
        )
    )

    Jump("loc_4E72")

    label("loc_4DE7")


    ChrTalk(
        0xFE,
        (
            "#610F我也认为演出是很考功夫的。\x01",
            "　\x02\x03",
            "呵呵，连艾丝蒂尔\x01",
            "和约修亚也参加演出的话，\x01",
            "那我真要好好看看才行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E72")

    TalkEnd(0x20)
    Return()

    # Function_21_4B17 end

    def Function_22_4E76(): pass

    label("Function_22_4E76")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(116280, 0, 2160, 0)
    SetChrPos(0x101, 117450, 0, -1700, 0)
    SetChrPos(0x102, 116510, 0, -1950, 0)
    SetChrPos(0x105, 117000, 0, -1020, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x105,
        (
            "#040F校长，您好。\x01",
            "我已经回来了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4EF3():
        OP_6D(117230, 0, 4590, 2000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4EF3)

    def lambda_4F0B():
        OP_8E(0xFE, 0x1C890, 0x0, 0x690, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F0B)
    Sleep(500)

    def lambda_4F2B():
        OP_8E(0xFE, 0x1CB10, 0x0, 0x690, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F2B)
    Sleep(300)

    def lambda_4F4B():
        OP_8E(0xFE, 0x1C64C, 0x0, 0x5D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F4B)
    WaitChrThread(0x105, 0x1)

    def lambda_4F6B():
        OP_8E(0xFE, 0x1C58E, 0x0, 0x9F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F6B)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 0, 400)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x105, 400)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x8,
        (
            "#780F#1P科洛丝，你回来了啊。\x02\x03",
            "哎哟？这两位是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F初次见面，校长。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们是游击士协会的人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#780F#1P呵呵，如此年轻就成为游击士，\x01",
            "的确是后生可畏啊。\x02\x03",
            "听说孤儿院发生了火灾，\x01",
            "莫非你们是为那件事而来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#049F#4P是的，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "科洛丝向科林兹校长\x01",
            "说明了包括纵火事件在内的一系列事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#780F#1P是吗……\x01",
            "那事情可就严重了。\x02\x03",
            "要是我们也能以什么方式\x01",
            "给院长和孩子们帮上忙就好了……\x02\x03",
            "…………………………\x02\x03",
            "那么首先，一定要办好学园祭，\x01",
            "不能辜负那些孩子对我们的期待……\x02\x03",
            "而且也只能从这里做起了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F是……\x02\x03",
            "#040F校长，有件事想和您说说。\x01",
            "这次我想请艾丝蒂尔和约修亚\x01",
            "来协助参演今年的舞台剧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#781F#1P这想法不错嘛。\x02\x03",
            "#780F艾丝蒂尔、约修亚。\x01",
            "这次的舞台剧就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F啊，是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们愿尽绵薄之力。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#780F#1P与舞台剧相关的工作\x01",
            "是由学生会长乔儿全权负责的。\x02\x03",
            "导演也由她担任，\x01",
            "所以详细情形向她请教就行了。\x02\x03",
            "而我这里就……\x01",
            "帮你们两位安排宿舍吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F宿舍？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#780F#1P毕竟学园祭\x01",
            "已经迫在眉睫了啊。\x02\x03",
            "恐怕每天都需要\x01",
            "排练到很晚呢。\x02\x03",
            "这样一来，\x01",
            "就需要有个住的地方对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，原来是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F这样的确方便多了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x8A, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#780F#1P刚好也下课了。\x02\x03",
            "科洛丝，你就马上\x01",
            "把他们介绍给学生会长吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#041F好的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 135, 400)

    ChrTalk(
        0x105,
        (
            "#040F#1P艾丝蒂尔、约修亚。\x01",
            "接下来我带你们去学生会室吧。\x02\x03",
            "这座主楼的右边是社团大楼，\x01",
            "而学生会室就在大楼的第二层。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，那我们走吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x3D, 0x1, 0x8)
    OP_28(0x3D, 0x1, 0x10)
    EventEnd(0x0)
    Return()

    # Function_22_4E76 end

    def Function_23_5672(): pass

    label("Function_23_5672")

    EventBegin(0x0)
    OP_77(0xFF, 0xC8, 0x96, 0x0, 0x0)
    OP_6D(-1190, 0, 33250, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 19)
    SetChrChipByIndex(0x102, 20)
    SetChrChipByIndex(0x105, 21)
    SetChrChipByIndex(0xB, 23)
    SetChrChipByIndex(0xC, 24)
    SetChrChipByIndex(0xD, 22)
    SetChrChipByIndex(0xE, 25)
    SetChrPos(0x101, 500, 200, 32060, 90)
    SetChrPos(0x102, 500, 200, 29980, 90)
    SetChrPos(0x105, 520, 200, 34100, 90)
    SetChrPos(0xA, -2750, 200, 30010, 90)
    SetChrPos(0x9, -2750, 200, 32060, 90)
    SetChrPos(0xC, -2750, 100, 34060, 90)
    SetChrPos(0xB, -5900, 100, 30010, 90)
    SetChrPos(0xD, -5900, 100, 34160, 90)
    SetChrPos(0xE, -5900, 100, 31920, 90)
    SetChrPos(0xF, 5300, 250, 32119, 90)

    def lambda_57B1():
        OP_6D(3580, 0, 33240, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57B1)
    FadeToBright(2000, 0)
    OP_8E(0xF, 0x150E, 0xFA, 0x76FC, 0x3E8, 0x0)
    OP_8C(0xF, 90, 400)
    Sleep(500)
    OP_8E(0xF, 0x14FA, 0xFA, 0x7CD8, 0x3E8, 0x0)
    OP_8C(0xF, 90, 400)
    Sleep(500)
    OP_8E(0xF, 0x150E, 0xFA, 0x76FC, 0x3E8, 0x0)
    OP_8C(0xF, 270, 400)
    Sleep(1000)

    def lambda_5832():
        OP_6D(2000, 0, 33250, 1500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5832)
    OP_8E(0xF, 0xD2A, 0x0, 0x7710, 0x7D0, 0x0)
    OP_8E(0xF, 0xA0A, 0x0, 0x7B70, 0x7D0, 0x0)
    TurnDirection(0xF, 0x101, 400)
    SetChrSubChip(0x102, 1)
    Sleep(100)
    SetChrSubChip(0x105, 2)
    OP_62(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xF)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)
    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1500)
    Sleep(500)
    TurnDirection(0xF, 0x102, 400)
    SetChrSubChip(0x101, 2)
    Sleep(500)
    OP_62(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xF)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)
    Sleep(500)
    OP_62(0xF, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    FadeToDark(1000, 0, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "上午，他们和其他学生一起\x01",
            "在老师的教导下接受正统的课程教育……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_5672 end

    def Function_24_5A5E(): pass

    label("Function_24_5A5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AF6")
    TurnDirection(0x105, 0x1, 400)

    ChrTalk(
        0x105,
        (
            "#040F对不起，\x01",
            "现在正在上课。\x02\x03",
            "我们先去校长办公室吧。\x01",
            "就在这个建筑物的一楼走廊里面。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B50")

    label("loc_5AF6")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F现在好像在上课。\x02\x03",
            "先去校长办公室吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B50")

    TalkEnd(0xFF)
    Return()

    # Function_24_5A5E end

    def Function_25_5B54(): pass

    label("Function_25_5B54")

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

    # Function_25_5B54 end

    def Function_26_5BB8(): pass

    label("Function_26_5BB8")

    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x22, 0x80)
    OP_64(0x5, 0x1)
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

    # Function_26_5BB8 end

    def Function_27_5C20(): pass

    label("Function_27_5C20")

    SetPlaceName(0x6F) # 主楼　社会系教室
    Return()

    # Function_27_5C20 end

    def Function_28_5C24(): pass

    label("Function_28_5C24")

    SetPlaceName(0x5E) # 主楼　社会系教室
    Return()

    # Function_28_5C24 end

    def Function_29_5C28(): pass

    label("Function_29_5C28")

    SetPlaceName(0x6E) # 主楼　社会系教室
    Return()

    # Function_29_5C28 end

    def Function_30_5C2C(): pass

    label("Function_30_5C2C")

    SetPlaceName(0x74) # 主楼　社会系教室
    Return()

    # Function_30_5C2C end

    def Function_31_5C30(): pass

    label("Function_31_5C30")

    SetPlaceName(0x73) # 主楼　社会系教室
    Return()

    # Function_31_5C30 end

    SaveToFile()

Try(main)
