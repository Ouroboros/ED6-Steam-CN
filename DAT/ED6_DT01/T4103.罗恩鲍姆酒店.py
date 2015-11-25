from ED6ScenarioHelper import *

def main():
    # 罗恩鲍姆酒店

    CreateScenaFile(
        FileName            = 'T4103   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4103.x',
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
        '士兵',                                 # 9
        '士兵',                                 # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        '士兵',                                 # 14
        '士兵',                                 # 15
        '士兵',                                 # 16
        '阿鲁姆',                               # 17
        '艾娅莉',                               # 18
        '托伊',                                 # 19
        '马丁',                                 # 20
        '玛丽安',                               # 21
        '海伦娜',                               # 22
        '诺雅尔',                               # 23
        '维基奥',                               # 24
        '巴鲁托',                               # 25
        '士兵',                                 # 26
        '士兵',                                 # 27
        '士兵',                                 # 28
        '士兵',                                 # 29
        '特务兵',                               # 30
        '特务兵',                               # 31
        '特务兵',                               # 32
        '米亚尔',                               # 33
        '戈万',                                 # 34
        '修女艾伦',                             # 35
        '观光客',                               # 36
        '观光客',                               # 37
        '观光客',                               # 38
        '观光客',                               # 39
        '观光客',                               # 40
        '观光客',                               # 41
        '观光客',                               # 42
        '观光客',                               # 43
        '观光客',                               # 44
        '观光客',                               # 45
        '观光客',                               # 46
        '观光客',                               # 47
        '王都格兰赛尔·西街区',                 # 48
        '格兰赛尔城',                           # 49
        '王都格兰赛尔·东街区',                 # 50
        '王都格兰赛尔·南街区',                 # 51
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 66000,
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01140 ._CH',             # 01
        'ED6_DT07/CH01150 ._CH',             # 02
        'ED6_DT07/CH01060 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH01210 ._CH',             # 05
        'ED6_DT07/CH02490 ._CH',             # 06
        'ED6_DT07/CH01130 ._CH',             # 07
        'ED6_DT07/CH01290 ._CH',             # 08
        'ED6_DT07/CH01200 ._CH',             # 09
        'ED6_DT07/CH01610 ._CH',             # 0A
        'ED6_DT07/CH01040 ._CH',             # 0B
        'ED6_DT07/CH01120 ._CH',             # 0C
        'ED6_DT07/CH01410 ._CH',             # 0D
        'ED6_DT07/CH01120 ._CH',             # 0E
        'ED6_DT07/CH01060 ._CH',             # 0F
        'ED6_DT07/CH01030 ._CH',             # 10
        'ED6_DT07/CH01130 ._CH',             # 11
        'ED6_DT07/CH01230 ._CH',             # 12
        'ED6_DT07/CH01220 ._CH',             # 13
        'ED6_DT07/CH02500 ._CH',             # 14
        'ED6_DT07/CH01680 ._CH',             # 15
        'ED6_DT07/CH01100 ._CH',             # 16
        'ED6_DT07/CH01110 ._CH',             # 17
        'ED6_DT07/CH01050 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01140P._CP',             # 01
        'ED6_DT07/CH01150P._CP',             # 02
        'ED6_DT07/CH01060P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH01210P._CP',             # 05
        'ED6_DT07/CH02490P._CP',             # 06
        'ED6_DT07/CH01130P._CP',             # 07
        'ED6_DT07/CH01290P._CP',             # 08
        'ED6_DT07/CH01200P._CP',             # 09
        'ED6_DT07/CH01610P._CP',             # 0A
        'ED6_DT07/CH01040P._CP',             # 0B
        'ED6_DT07/CH01120P._CP',             # 0C
        'ED6_DT07/CH01410P._CP',             # 0D
        'ED6_DT07/CH01120P._CP',             # 0E
        'ED6_DT07/CH01060P._CP',             # 0F
        'ED6_DT07/CH01030P._CP',             # 10
        'ED6_DT07/CH01130P._CP',             # 11
        'ED6_DT07/CH01230P._CP',             # 12
        'ED6_DT07/CH01220P._CP',             # 13
        'ED6_DT07/CH02500P._CP',             # 14
        'ED6_DT07/CH01680P._CP',             # 15
        'ED6_DT07/CH01100P._CP',             # 16
        'ED6_DT07/CH01110P._CP',             # 17
        'ED6_DT07/CH01050P._CP',             # 18
    )

    DeclNpc(
        X                   = -2980,
        Z                   = 0,
        Y                   = 68330,
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
        X                   = 3120,
        Z                   = 0,
        Y                   = 68420,
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
        X                   = -32570,
        Z                   = 0,
        Y                   = 50050,
        Direction           = 90,
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
        X                   = -9530,
        Z                   = 250,
        Y                   = 32240,
        Direction           = 90,
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
        X                   = 9480,
        Z                   = 250,
        Y                   = 37480,
        Direction           = 270,
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
        X                   = 560,
        Z                   = 0,
        Y                   = 39030,
        Direction           = 225,
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
        X                   = -370,
        Z                   = 0,
        Y                   = 38160,
        Direction           = 45,
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
        X                   = 3800,
        Z                   = 0,
        Y                   = 65780,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 45,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
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
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 6490,
        Z                   = 0,
        Y                   = 43840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -2950,
        Z                   = 0,
        Y                   = 63820,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -7440,
        Z                   = 0,
        Y                   = 49400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -6340,
        Z                   = 0,
        Y                   = 52120,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 6490,
        Z                   = 0,
        Y                   = 43840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -2950,
        Z                   = 0,
        Y                   = 63820,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 3660,
        Z                   = 0,
        Y                   = 64440,
        Direction           = 356,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -7400,
        Z                   = 250,
        Y                   = 59390,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 4750,
        Z                   = 0,
        Y                   = 10320,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -710,
        Z                   = 0,
        Y                   = 68870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -5260,
        Z                   = 0,
        Y                   = 66960,
        Direction           = 131,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = -5940,
        Z                   = 0,
        Y                   = 65580,
        Direction           = 30,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -8140,
        Z                   = 250,
        Y                   = 56080,
        Direction           = 219,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -10060,
        Z                   = 250,
        Y                   = 56020,
        Direction           = 149,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = -9190,
        Z                   = 250,
        Y                   = 54240,
        Direction           = 9,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 7480,
        Z                   = 250,
        Y                   = 59730,
        Direction           = 267,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 9690,
        Z                   = 250,
        Y                   = 50490,
        Direction           = 281,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 7050,
        Z                   = 250,
        Y                   = 50520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 9510,
        Z                   = 0,
        Y                   = 44040,
        Direction           = 96,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 8700,
        Z                   = 0,
        Y                   = 44910,
        Direction           = 108,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 7190,
        Z                   = 250,
        Y                   = 38180,
        Direction           = 258,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = -7530,
        Z                   = 250,
        Y                   = 44220,
        Direction           = 37,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = -40080,
        Z                   = 0,
        Y                   = 17660,
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
        X                   = 100,
        Z                   = 0,
        Y                   = 104130,
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
        X                   = 40430,
        Z                   = 0,
        Y                   = 64060,
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
        X                   = 20,
        Z                   = 0,
        Y                   = -3500,
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
        X                   = 18520,
        Y                   = 0,
        Z                   = 44050,
        Range               = 1500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 48,
    )


    ScpFunction(
        "Function_0_6F2",          # 00, 0
        "Function_1_93C",          # 01, 1
        "Function_2_B15",          # 02, 2
        "Function_3_B2A",          # 03, 3
        "Function_4_CA7",          # 04, 4
        "Function_5_CED",          # 05, 5
        "Function_6_EFE",          # 06, 6
        "Function_7_F58",          # 07, 7
        "Function_8_FE5",          # 08, 8
        "Function_9_107C",         # 09, 9
        "Function_10_1183",        # 0A, 10
        "Function_11_11A7",        # 0B, 11
        "Function_12_11E8",        # 0C, 12
        "Function_13_147A",        # 0D, 13
        "Function_14_17DC",        # 0E, 14
        "Function_15_1856",        # 0F, 15
        "Function_16_1C2A",        # 10, 16
        "Function_17_1EB1",        # 11, 17
        "Function_18_2163",        # 12, 18
        "Function_19_2420",        # 13, 19
        "Function_20_2458",        # 14, 20
        "Function_21_2480",        # 15, 21
        "Function_22_254B",        # 16, 22
        "Function_23_3141",        # 17, 23
        "Function_24_3733",        # 18, 24
        "Function_25_45F7",        # 19, 25
        "Function_26_468F",        # 1A, 26
        "Function_27_4735",        # 1B, 27
        "Function_28_4816",        # 1C, 28
        "Function_29_48DD",        # 1D, 29
        "Function_30_4B40",        # 1E, 30
        "Function_31_4ECA",        # 1F, 31
        "Function_32_4F3E",        # 20, 32
        "Function_33_4F61",        # 21, 33
        "Function_34_4FF4",        # 22, 34
        "Function_35_50A8",        # 23, 35
        "Function_36_5131",        # 24, 36
        "Function_37_521A",        # 25, 37
        "Function_38_5266",        # 26, 38
        "Function_39_52F2",        # 27, 39
        "Function_40_53F3",        # 28, 40
        "Function_41_5449",        # 29, 41
        "Function_42_5494",        # 2A, 42
        "Function_43_54F2",        # 2B, 43
        "Function_44_55B9",        # 2C, 44
        "Function_45_55BA",        # 2D, 45
        "Function_46_5617",        # 2E, 46
        "Function_47_5856",        # 2F, 47
        "Function_48_59A3",        # 30, 48
    )


    def Function_0_6F2(): pass

    label("Function_0_6F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_70E")
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 43)
    OP_B1("t4103_n")

    label("loc_70E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (110, "loc_71A"),
        (SWITCH_DEFAULT, "loc_730"),
    )


    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D")
    OP_A2(0x62C)
    Event(0, 47)

    label("loc_72D")

    Jump("loc_730")

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_7F4")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -7310, 250, 28970, 270)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -9190, 250, 29720, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -9190, 250, 28210, 90)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x10)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x10)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x10)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x10)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x10)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x10)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x10)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    Jump("loc_93B")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_848")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, -3840, 0, 67340, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -2760, 0, 67340, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_93B")

    label("loc_848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_897")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -3820, 0, 66400, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2760, 0, 66400, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_93B")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_8B5")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_93B")

    label("loc_8B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8D3")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_93B")

    label("loc_8D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_8F1")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_93B")

    label("loc_8F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_911")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 3080, 0, 67910, 0)
    Jump("loc_93B")

    label("loc_911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_920")
    ClearChrFlags(0x22, 0x80)
    Jump("loc_93B")

    label("loc_920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_92A")
    Jump("loc_93B")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_934")
    Jump("loc_93B")

    label("loc_934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_93B")

    label("loc_93B")

    Return()

    # Function_0_6F2 end

    def Function_1_93C(): pass

    label("Function_1_93C")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFECF50, 0x3005E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_981")
    OP_B1("t4103_y")
    Jump("loc_98A")

    label("loc_981")

    OP_B1("t4103_n")

    label("loc_98A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CC")
    OP_72(0x6, 0x8)
    OP_72(0x6, 0x20)
    OP_72(0x6, 0x2)
    OP_6F(0x6, 0)
    OP_72(0x2, 0x10)
    OP_72(0x5, 0x8)
    OP_72(0x5, 0x20)
    OP_72(0x5, 0x2)
    OP_6F(0x5, 0)
    OP_72(0x3, 0x10)

    label("loc_9CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A38")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    OP_43(0x8, 0x1, 0x0, 0x2E)
    OP_43(0x9, 0x1, 0x0, 0x2E)
    OP_43(0xA, 0x1, 0x0, 0x2E)
    OP_43(0xB, 0x1, 0x0, 0x2E)
    OP_43(0xC, 0x1, 0x0, 0x2E)
    OP_43(0xD, 0x1, 0x0, 0x2E)
    OP_43(0xE, 0x1, 0x0, 0x2E)
    OP_43(0xF, 0x1, 0x0, 0x2E)

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_B14")
    OP_72(0x7, 0x4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    SetMapFlags(0x800)
    OP_1B(0x7, 0x0, 0x2)
    OP_1B(0x6, 0x0, 0x2)
    LoadEffect(0x0, "map\\\\mp016_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -40, 250, 54930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 90, 0, 39630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 90, 250, 20100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_B14")

    Return()

    # Function_1_93C end

    def Function_2_B15(): pass

    label("Function_2_B15")

    ClearMapFlags(0x800)
    ClearMapFlags(0x2000000)
    OP_1B(0x7, 0x0, 0xFFFF)
    OP_1B(0x6, 0x0, 0xFFFF)
    Return()

    # Function_2_B15 end

    def Function_3_B2A(): pass

    label("Function_3_B2A")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_C91")

    label("loc_B4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B68")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_C91")

    label("loc_B68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B81")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_C91")

    label("loc_B81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_C91")

    label("loc_B9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_C91")

    label("loc_BB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_C91")

    label("loc_BCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_C91")

    label("loc_BE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_C91")

    label("loc_BFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C17")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_C91")

    label("loc_C17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C30")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_C91")

    label("loc_C30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C49")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_C91")

    label("loc_C49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C62")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_C91")

    label("loc_C62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_C91")

    label("loc_C7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C91")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_C91")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CA6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_C91")

    label("loc_CA6")

    Return()

    # Function_3_B2A end

    def Function_4_CA7(): pass

    label("Function_4_CA7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CEC")
    SetChrPos(0xFE, 31870, 0, 62980, 270)
    OP_8E(0xFE, 0xC6C, 0x0, 0xF604, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC6C, 0x0, 0x40CE, 0x7D0, 0x0)
    Jump("Function_4_CA7")

    label("loc_CEC")

    Return()

    # Function_4_CA7 end

    def Function_5_CED(): pass

    label("Function_5_CED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EFD")
    SetChrPos(0xFE, -40860, 0, 28340, 0)
    OP_8E(0xFE, 0xFFFF6064, 0x0, 0xBAE0, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFF624E, 0x0, 0xC422, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFA33A, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_8C(0xFE, 0, 800)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFA33A, 0xFA, 0xE9DE, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFF9F48, 0xFA, 0xF1F4, 0x2328, 0x0)
    OP_8C(0xFE, 0, 800)
    Sleep(400)
    OP_8E(0xFE, 0xFFFFA33A, 0xFA, 0xE9DE, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFA33A, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFE674, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xCED6, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xF276, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFF16E, 0x0, 0xFD84, 0x2328, 0x0)
    OP_8E(0xFE, 0x9B8C, 0x0, 0xFD84, 0x2328, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 39650, 0, 62210, 90)
    OP_8E(0xFE, 0x67A2, 0x0, 0xF302, 0x2328, 0x0)
    OP_8E(0xFE, 0x56B8, 0xFA, 0xE60A, 0x2328, 0x0)
    OP_8E(0xFE, 0x2A9E, 0xFA, 0xE60A, 0x2328, 0x0)
    OP_8E(0xFE, 0x2288, 0xFA, 0xDC00, 0x2328, 0x0)
    OP_8E(0xFE, 0x2288, 0xFA, 0xC030, 0x2328, 0x0)
    OP_8E(0xFE, 0x2BE8, 0xFA, 0xB6D0, 0x2328, 0x0)
    OP_8E(0xFE, 0x402E, 0xFA, 0xB6D0, 0x2328, 0x0)
    Sleep(400)
    OP_8E(0xFE, 0x1EF0, 0xFA, 0x8E12, 0x2328, 0x0)
    OP_8E(0xFE, 0x1EF0, 0xFA, 0x1F04, 0x2328, 0x0)
    Sleep(2000)
    Jump("Function_5_CED")

    label("loc_EFD")

    Return()

    # Function_5_CED end

    def Function_6_EFE(): pass

    label("Function_6_EFE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F57")
    SetChrPos(0xFE, -4340, 0, 16160, 0)
    OP_8E(0xFE, 0xFFFFEF0C, 0x0, 0xBD74, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6866, 0x0, 0xBD74, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6866, 0x0, 0x6B58, 0x9C4, 0x0)
    Jump("Function_6_EFE")

    label("loc_F57")

    Return()

    # Function_6_EFE end

    def Function_7_F58(): pass

    label("Function_7_F58")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FE4")
    OP_8E(0xFE, 0x195A, 0x0, 0xB95A, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x195A, 0x0, 0xAB40, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x195A, 0x0, 0x9DDA, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x195A, 0x0, 0xAB40, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    Jump("Function_7_F58")

    label("loc_FE4")

    Return()

    # Function_7_F58 end

    def Function_8_FE5(): pass

    label("Function_8_FE5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_107B")
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xC300, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0x5528, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xC300, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xF94C, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_8_FE5")

    label("loc_107B")

    Return()

    # Function_8_FE5 end

    def Function_9_107C(): pass

    label("Function_9_107C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1182")
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF65E6, 0x0, 0xBBE4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0xB644, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0x9592, 0x9C4, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0xB644, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF676C, 0x0, 0xC1E8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFE2F0, 0x0, 0xC0F8, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 0, 400)
    Sleep(2000)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_9_107C")

    label("loc_1182")

    Return()

    # Function_9_107C end

    def Function_10_1183(): pass

    label("Function_10_1183")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11A6")
    OP_8D(0xFE, -7060, 65710, 5760, 62220, 3000)
    Jump("Function_10_1183")

    label("loc_11A6")

    Return()

    # Function_10_1183 end

    def Function_11_11A7(): pass

    label("Function_11_11A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11E7")
    OP_8E(0xFE, 0x11C6, 0x0, 0xEE84, 0xAF0, 0x0)
    Sleep(3000)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x128E, 0x0, 0x2850, 0xAF0, 0x0)
    Jump("Function_11_11A7")

    label("loc_11E7")

    Return()

    # Function_11_11A7 end

    def Function_12_11E8(): pass

    label("Function_12_11E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 6)), scpexpr(EXPR_END)), "loc_12DF")

    ChrTalk(
        0xFE,
        "我、我是个路痴。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对格兰赛尔的大街\x01",
            "还不是很熟悉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……是这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1476")

    label("loc_12DF")

    OP_A2(0x67E)

    ChrTalk(
        0xFE,
        "啊，是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊，是修女艾伦啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F怎么了？\x01",
            "在这种地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x22, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "这、这……我出来办点事情，\x01",
            "结果却迷了路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F如果可以的话，\x01",
            "让我们送您回大圣堂好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "士兵刚才已经告诉我怎么走了，\x01",
            "已经没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F这样啊，那你路上小心哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，谢谢你们。\x02",
    )

    CloseMessageWindow()

    label("loc_1476")

    TalkEnd(0xFE)
    Return()

    # Function_12_11E8 end

    def Function_13_147A(): pass

    label("Function_13_147A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_14B3")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "心情好久没有这么爽快了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D8")

    label("loc_14B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1565")

    ChrTalk(
        0xFE,
        "呼～啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要不要去\x01",
            "西街区的咖啡厅\x01",
            "喝杯咖啡解解困呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "士兵们从早忙到晚，真是辛苦了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_17D8")

    label("loc_1565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_178B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_160B")

    ChrTalk(
        0xFE,
        (
            "街上的警戒\x01",
            "怎么变得这么严了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过是闲逛了一会儿，\x01",
            "就被士兵盘问了好几次。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1788")

    label("loc_160B")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "呼～决赛那天好热闹啊。\x01",
            "昨天不知不觉就喝多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一觉睡到大天亮。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "街上的警戒\x01",
            "怎么变得这么严了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过是闲逛了一会儿，\x01",
            "就被士兵盘问了好几次。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1788")

    Jump("loc_17D8")

    label("loc_178B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1795")
    Jump("loc_17D8")

    label("loc_1795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_179F")
    Jump("loc_17D8")

    label("loc_179F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_17A9")
    Jump("loc_17D8")

    label("loc_17A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_17B3")
    Jump("loc_17D8")

    label("loc_17B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_17BD")
    Jump("loc_17D8")

    label("loc_17BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_17C7")
    Jump("loc_17D8")

    label("loc_17C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_17D1")
    Jump("loc_17D8")

    label("loc_17D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_17D8")

    label("loc_17D8")

    TalkEnd(0xFE)
    Return()

    # Function_13_147A end

    def Function_14_17DC(): pass

    label("Function_14_17DC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "在武术大会里大显身手的游击士\x01",
            "成功阻止了这次政变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哈～真是太棒了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_17DC end

    def Function_15_1856(): pass

    label("Function_15_1856")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_18B3")

    ChrTalk(
        0xFE,
        (
            "不要光在街上\x01",
            "站着不动，\x01",
            "请到处走走看看！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C26")

    label("loc_18B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_18BD")
    Jump("loc_1C26")

    label("loc_18BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1968")

    ChrTalk(
        0xFE,
        "很快就要到诞辰庆典了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在那之前\x01",
            "一定要千方百计将\x01",
            "恐怖分子们抓住啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C26")

    label("loc_1968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_19AF")

    ChrTalk(
        0xFE,
        "决赛好像结束了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是哪一方获胜了呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C26")

    label("loc_19AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1B46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1A71")

    ChrTalk(
        0xFE,
        (
            "我不太喜欢\x01",
            "特务部队那些家伙，\x01",
            "所以我决定支持你们游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不要告诉别人哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B43")

    label("loc_1A71")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "今天是决赛日啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我不太喜欢\x01",
            "特务部队那些家伙，\x01",
            "所以我决定支持你们游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不要告诉别人哦。\x02",
    )

    CloseMessageWindow()

    label("loc_1B43")

    Jump("loc_1C26")

    label("loc_1B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1BF7")

    ChrTalk(
        0xFE,
        (
            "难得大家都沉浸在节日的气氛当中，\x01",
            "给你们泼冷水真是很抱歉，\x01",
            "但是上面命令我们必须加强警备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "必须得到\x01",
            "广大市民的配合才行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C26")

    label("loc_1BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1C01")
    Jump("loc_1C26")

    label("loc_1C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C0B")
    Jump("loc_1C26")

    label("loc_1C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1C15")
    Jump("loc_1C26")

    label("loc_1C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1C1F")
    Jump("loc_1C26")

    label("loc_1C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1C26")

    label("loc_1C26")

    TalkEnd(0xFE)
    Return()

    # Function_15_1856 end

    def Function_16_1C2A(): pass

    label("Function_16_1C2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1C91")

    ChrTalk(
        0xFE,
        "没有异常！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为警备是轮流执行的，\x01",
            "所以我也要在街道上巡逻啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAD")

    label("loc_1C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1C9B")
    Jump("loc_1EAD")

    label("loc_1C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1CF2")

    ChrTalk(
        0xFE,
        (
            "如果有什么异常情况，\x01",
            "请马上告诉我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAD")

    label("loc_1CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1D65")

    ChrTalk(
        0xFE,
        (
            "据说亲卫队是恐怖分子，\x01",
            "这是真的吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "悄悄告诉你们，\x01",
            "我也不相信这件事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAD")

    label("loc_1D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1E04")

    ChrTalk(
        0xFE,
        (
            "就算找到了亲卫队，\x01",
            "一旦动手我们也未必有胜算。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为他们的强大是出了名的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EAD")

    label("loc_1E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1E7E")

    ChrTalk(
        0xFE,
        (
            "如果看见有像亲卫队的人，\x01",
            "请马上过来报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAD")

    label("loc_1E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1E88")
    Jump("loc_1EAD")

    label("loc_1E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E92")
    Jump("loc_1EAD")

    label("loc_1E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1E9C")
    Jump("loc_1EAD")

    label("loc_1E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1EA6")
    Jump("loc_1EAD")

    label("loc_1EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1EAD")

    label("loc_1EAD")

    TalkEnd(0xFE)
    Return()

    # Function_16_1C2A end

    def Function_17_1EB1(): pass

    label("Function_17_1EB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1F92")

    ChrTalk(
        0xFE,
        (
            "结果，\x01",
            "亲卫队的队员言而有信地\x01",
            "成功守护了女王陛下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……他们是王国军的榜样，\x01",
            "再次向他们表示敬意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215F")

    label("loc_1F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1F9C")
    Jump("loc_215F")

    label("loc_1F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2057")

    ChrTalk(
        0xFE,
        (
            "就算到现在我还是无法相信\x01",
            "亲卫队的人就是恐怖分子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正因为他们在军队中位置特殊，\x01",
            "所以才会惹来那么多非议吧，\x01",
            "但我还是觉得他们很厉害呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215F")

    label("loc_2057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_20BF")

    ChrTalk(
        0xFE,
        "这里没有异常。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "差不多该是换班的时间了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215F")

    label("loc_20BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_20F1")

    ChrTalk(
        0xFE,
        "抱歉，我们现在很忙。\x02",
    )

    CloseMessageWindow()
    Jump("loc_215F")

    label("loc_20F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2130")

    ChrTalk(
        0xFE,
        (
            "很抱歉，\x01",
            "请不要妨碍巡逻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215F")

    label("loc_2130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_213A")
    Jump("loc_215F")

    label("loc_213A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2144")
    Jump("loc_215F")

    label("loc_2144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_214E")
    Jump("loc_215F")

    label("loc_214E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2158")
    Jump("loc_215F")

    label("loc_2158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_215F")

    label("loc_215F")

    TalkEnd(0xFE)
    Return()

    # Function_17_1EB1 end

    def Function_18_2163(): pass

    label("Function_18_2163")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_21FA")

    ChrTalk(
        0xFE,
        (
            "那位理查德上校\x01",
            "是政变的策划人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不敢相信更加不愿去相信，\x01",
            "我真的很尊敬他的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_21FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2204")
    Jump("loc_241C")

    label("loc_2204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_22AC")

    ChrTalk(
        0xFE,
        "不要妨碍警备哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果让恐怖分子\x01",
            "混入诞辰庆典就不得了了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_22AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2342")

    ChrTalk(
        0xFE,
        (
            "那个特务部队\x01",
            "在决赛中竟然输了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "游击士干得不赖呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_2342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2398")

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "真是个很厉害的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们也是这么认为的吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_2398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_23ED")

    ChrTalk(
        0xFE,
        (
            "如果干了什么可疑的事，\x01",
            "就算是游击士也要逮捕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_23ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_23F7")
    Jump("loc_241C")

    label("loc_23F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2401")
    Jump("loc_241C")

    label("loc_2401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_240B")
    Jump("loc_241C")

    label("loc_240B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2415")
    Jump("loc_241C")

    label("loc_2415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_241C")

    label("loc_241C")

    TalkEnd(0xFE)
    Return()

    # Function_18_2163 end

    def Function_19_2420(): pass

    label("Function_19_2420")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "这边的情况没有异常。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_2420 end

    def Function_20_2458(): pass

    label("Function_20_2458")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "让开让开！\x01",
            "别妨碍执行公务！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2458 end

    def Function_21_2480(): pass

    label("Function_21_2480")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "王都的守卫\x01",
            "现在由我们特务兵来担当。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也好，如果原来那些家伙还在，\x01",
            "只会拖我们后腿。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2480 end

    def Function_22_254B(): pass

    label("Function_22_254B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_25F2")

    ChrTalk(
        0xFE,
        (
            "终于看到好久不见的\x01",
            "女王陛下的身影了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来所有的担心和顾虑\x01",
            "就都一扫而空了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313D")

    label("loc_25F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_26BF")

    ChrTalk(
        0xFE,
        (
            "平常的那些士兵们\x01",
            "都匆匆忙忙地撤离了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "守卫王城的人\x01",
            "变成了黑衣士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "有些不好的预感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_313D")

    label("loc_26BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_28EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2792")

    ChrTalk(
        0xFE,
        (
            "武术大会结束了，\x01",
            "离女王陛下的生日\x01",
            "也已经没有几天了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可还是得不到关于\x01",
            "陛下病情的详细情况啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EC")

    label("loc_2792")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "武术大会结束了，\x01",
            "离女王陛下的生日已经很近了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是我们还是不知道\x01",
            "陛下病情的详细情况啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，本来让那个杜南公爵\x01",
            "担任女王陛下的代理\x01",
            "我就觉得很不可思议了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28EC")

    Jump("loc_313D")

    label("loc_28EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2938")

    ChrTalk(
        0xFE,
        (
            "已经到傍晚了。\x01",
            "要快点回家了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313D")

    label("loc_2938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_29FB")

    ChrTalk(
        0xFE,
        (
            "武术大会\x01",
            "今天到了决赛日啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "至少今天\x01",
            "还是要去现场看看的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313D")

    label("loc_29FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2A71")

    ChrTalk(
        0xFE,
        (
            "常常可以看见\x01",
            "穿黑衣服的士兵\x01",
            "在王城中出入……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他们到底是什么人啊？\x02",
    )

    CloseMessageWindow()
    Jump("loc_313D")

    label("loc_2A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2C0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2B15")

    ChrTalk(
        0xFE,
        (
            "王城的城门前面\x01",
            "不是有个很大的广场吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "诞辰庆典当天可以从那里\x01",
            "一睹女王陛下的风采。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C09")

    label("loc_2B15")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "王城的城门前面\x01",
            "不是有个很大的广场吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "诞辰庆典当天可以从那里\x01",
            "一睹女王陛下的风采。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，照现在这样下去的话，\x01",
            "今年的诞辰庆典会怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C09")

    Jump("loc_313D")

    label("loc_2C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2E80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2D1B")

    ChrTalk(
        0xFE,
        (
            "站在王城的空中庭园，\x01",
            "从瓦雷利亚湖吹面而来的清爽凉风\x01",
            "和空中庭园里植被的清香让人神清气爽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然现在不能进去了，\x01",
            "不过无论如何我还是要推荐一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7D")

    label("loc_2D1B")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "以前是可以到王城的空中庭园\x01",
            "去进行参观游览的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从瓦雷利亚湖吹面而来的清爽凉风\x01",
            "和空中庭园里植被的清香让人神清气爽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然现在不能进去了，\x01",
            "不过无论如何我还是要推荐一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E7D")

    Jump("loc_313D")

    label("loc_2E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2F24")

    ChrTalk(
        0xFE,
        (
            "不久前还是\x01",
            "只要通过申请\x01",
            "就可以进王城参观的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是因为女王陛下身体欠佳，\x01",
            "所以参观的事情基本无望了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313D")

    label("loc_2F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_306A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F80")

    ChrTalk(
        0xFE,
        (
            "艾莉茜雅女王\x01",
            "是利贝尔的骄傲，\x01",
            "而杜南公爵则是耻辱。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3067")

    label("loc_2F80")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "之前，\x01",
            "那个杜南公爵又在城门外耍无赖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，就算是女王陛下身体欠佳，\x01",
            "也不该找那种代理人啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "艾莉茜雅女王\x01",
            "是利贝尔的骄傲，\x01",
            "而杜南公爵则是耻辱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3067")

    Jump("loc_313D")

    label("loc_306A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_313D")

    ChrTalk(
        0xFE,
        (
            "武术大会虽然开始了，\x01",
            "但这周围的观光客好像\x01",
            "比平时还要少了一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "肯定是因为王城\x01",
            "禁止对外开放的缘故。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_313D")

    TalkEnd(0xFE)
    Return()

    # Function_22_254B end

    def Function_23_3141(): pass

    label("Function_23_3141")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_31B3")

    ChrTalk(
        0xFE,
        (
            "诞辰庆典并不意味着\x01",
            "是邮递员的休息日。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反而是服务行业\x01",
            "最忙的时候呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372F")

    label("loc_31B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3262")

    ChrTalk(
        0xFE,
        (
            "空港被军队给封锁了，\x01",
            "已经不能进入了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "等这个货物邮递完毕后\x01",
            "就没有其他任务了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372F")

    label("loc_3262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_32D0")

    ChrTalk(
        0xFE,
        (
            "昨天，\x01",
            "空港来了好多士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到底发生了什么事……\x02",
    )

    CloseMessageWindow()
    Jump("loc_372F")

    label("loc_32D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3338")

    ChrTalk(
        0xFE,
        (
            "下次的《利贝尔通讯》\x01",
            "好像会出武术大会特辑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我从现在开始就很期待了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_372F")

    label("loc_3338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_33FC")

    ChrTalk(
        0xFE,
        (
            "最近王都大大小小的角落\x01",
            "都有一大群士兵在巡逻，\x01",
            "搞得我工作也不顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是一群给人添麻烦的人。\x02",
    )

    CloseMessageWindow()
    Jump("loc_372F")

    label("loc_33FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_345B")

    ChrTalk(
        0xFE,
        "嗯，下面要把东西送到……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "已经傍晚了，必须快点啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_372F")

    label("loc_345B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_34E3")

    ChrTalk(
        0xFE,
        "那么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "将这些货物送完之后，\x01",
            "就回空港休息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372F")

    label("loc_34E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3563")

    ChrTalk(
        0xFE,
        (
            "有时候收信人的地址\x01",
            "写得不工整导致看不清楚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "很麻烦呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_372F")

    label("loc_3563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_35FC")

    ChrTalk(
        0xFE,
        (
            "啊，如果不是因为工作的话，\x01",
            "我肯定已经去观看武术大会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "邮递员的工作很多，\x01",
            "哪有什么休息的时间啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372F")

    label("loc_35FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_36C7")

    ChrTalk(
        0xFE,
        (
            "我回空港去取邮寄的物品时，\x01",
            "却发现王家飞艇『埃尔赛尤号』\x01",
            "被士兵给包围了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "究竟发生了什么事……\x01",
            "感觉不是很太平啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372F")

    label("loc_36C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_372F")

    ChrTalk(
        0xFE,
        "嗯，接下来要送的东西是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，王都实在是太大了，\x01",
            "对于我们这些邮递员来说真是灾难啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_372F")

    TalkEnd(0xFE)
    Return()

    # Function_23_3141 end

    def Function_24_3733(): pass

    label("Function_24_3733")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3869")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_37AA")

    ChrTalk(
        0xFE,
        (
            "虽然接下来会很辛苦，\x01",
            "但是现在卡西乌斯上校回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那我们就一定要努力了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3866")

    label("loc_37AA")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀～～～\x01",
            "跟预想的一样，\x01",
            "我被安排了像山一样多的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然接下来会很辛苦，\x01",
            "但是现在卡西乌斯上校回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那我们就一定要努力了！\x02",
    )

    CloseMessageWindow()

    label("loc_3866")

    Jump("loc_45F3")

    label("loc_3869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3925")

    ChrTalk(
        0xFE,
        (
            "没有任何公告的情况下\x01",
            "王都守卫队突然撤离，\x01",
            "特务部队却出现了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么想，\x01",
            "都觉得是王城里\x01",
            "发生了什么可怕的事件……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45F3")

    label("loc_3925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_39AA")

    ChrTalk(
        0xFE,
        (
            "总觉得最近在街上\x01",
            "老是能看到特务兵的身影……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "即便如此，\x01",
            "还是没能抓到亲卫队的那些人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45F3")

    label("loc_39AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3B79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3A76")

    ChrTalk(
        0xFE,
        (
            "情报部的家伙们\x01",
            "经常用很蛮横的态度\x01",
            "来打听情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "同样是为利贝尔王国\x01",
            "服务的工作人员，\x01",
            "他们对我们很不友好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B76")

    label("loc_3A76")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "情报部的家伙们\x01",
            "经常用很蛮横的态度\x01",
            "来打听情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "同样是为利贝尔王国\x01",
            "服务的工作人员，\x01",
            "他们对我们很不友好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特别是凯诺娜上尉，\x01",
            "对她抱反感的人有不少。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B76")

    Jump("loc_45F3")

    label("loc_3B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3D65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3C34")

    ChrTalk(
        0xFE,
        (
            "传说中的『埃尔赛尤号』\x01",
            "也被军队接管起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算是那个理查德上校，\x01",
            "这样做也会让人不愉快的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D62")

    label("loc_3C34")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "传说中的『埃尔赛尤号』\x01",
            "也被军队接管起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然那艘飞艇的成员\x01",
            "和亲卫队的人有交往，\x01",
            "不过不管怎么说，那可是王家的飞艇啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算是那个理查德上校，\x01",
            "这样做也会让人不愉快的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D62")

    Jump("loc_45F3")

    label("loc_3D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3F7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3E4C")

    ChrTalk(
        0xFE,
        (
            "就算是理查德上校，\x01",
            "搜捕起亲卫队来\x01",
            "也着实非常的辛苦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "情报部初来乍到，\x01",
            "一时间很难得到\x01",
            "市民们的配合。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F78")

    label("loc_3E4C")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "就算是理查德上校，\x01",
            "搜捕起亲卫队来\x01",
            "也着实非常的辛苦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为亲卫队一直都\x01",
            "相当受王都市民的欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "情报部初来乍到，\x01",
            "一时间很难得到\x01",
            "市民们的配合。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F78")

    Jump("loc_45F3")

    label("loc_3F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_41B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4012")

    ChrTalk(
        0xFE,
        (
            "我们文官当中\x01",
            "好像也有很多人\x01",
            "同情亲卫队呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41B6")

    label("loc_4012")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "我们文官当中\x01",
            "好像也有很多人\x01",
            "同情亲卫队呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "恐怖事件发生的时候，\x01",
            "他们应该在艾尔贝离宫那边\x01",
            "进行演习吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然他们有不在场证明，\x01",
            "但没想到陛下\x01",
            "还是下了逮捕令呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41B6")

    Jump("loc_45F3")

    label("loc_41B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_428F")

    ChrTalk(
        0xFE,
        (
            "对了，我在休假的时候\x01",
            "还看到情报部的士兵\x01",
            "押送着亲卫队的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尤莉亚·舒华兹中尉\x01",
            "现在到底怎么样了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4396")

    label("loc_428F")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "对了，我在休假的时候\x01",
            "还看到情报部的士兵\x01",
            "押送着亲卫队的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像是把王城剩下的\x01",
            "亲卫队成员都逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尤莉亚·舒华兹中尉\x01",
            "现在到底怎么样了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4396")

    Jump("loc_45F3")

    label("loc_4399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4469")

    ChrTalk(
        0xFE,
        (
            "突然间可以休假了，\x01",
            "还真是有些不太习惯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于王城的公务\x01",
            "反而有些放心不下了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45F3")

    label("loc_4469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_452A")

    ChrTalk(
        0xFE,
        (
            "最近一段时间，\x01",
            "理查德上校时常在王城出入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "身体欠佳的女王陛下\x01",
            "一定很信任他，\x01",
            "才把他从要塞那里叫了回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45F3")

    label("loc_452A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_45F3")

    ChrTalk(
        0xFE,
        (
            "我本来是在王城里工作的，\x01",
            "几天前，代替女王行使政权的公爵\x01",
            "突然宣布让我们休假。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说是因为女王陛下身体欠佳\x01",
            "而暂时不进行政务，\x01",
            "休息一段时间……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45F3")

    TalkEnd(0xFE)
    Return()

    # Function_24_3733 end

    def Function_25_45F7(): pass

    label("Function_25_45F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_462A")

    ChrTalk(
        0xFE,
        (
            "哈～哈～哈，\x01",
            "接下来就开始点名吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_468B")

    label("loc_462A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4634")
    Jump("loc_468B")

    label("loc_4634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_463E")
    Jump("loc_468B")

    label("loc_463E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4648")
    Jump("loc_468B")

    label("loc_4648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4652")
    Jump("loc_468B")

    label("loc_4652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_465C")
    Jump("loc_468B")

    label("loc_465C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4666")
    Jump("loc_468B")

    label("loc_4666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4670")
    Jump("loc_468B")

    label("loc_4670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_467A")
    Jump("loc_468B")

    label("loc_467A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4684")
    Jump("loc_468B")

    label("loc_4684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_468B")

    label("loc_468B")

    TalkEnd(0xFE)
    Return()

    # Function_25_45F7 end

    def Function_26_468F(): pass

    label("Function_26_468F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_46D0")

    ChrTalk(
        0xFE,
        "今天我的老公又是状态极佳。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是没办法啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4731")

    label("loc_46D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_46DA")
    Jump("loc_4731")

    label("loc_46DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_46E4")
    Jump("loc_4731")

    label("loc_46E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_46EE")
    Jump("loc_4731")

    label("loc_46EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_46F8")
    Jump("loc_4731")

    label("loc_46F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4702")
    Jump("loc_4731")

    label("loc_4702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_470C")
    Jump("loc_4731")

    label("loc_470C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4716")
    Jump("loc_4731")

    label("loc_4716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4720")
    Jump("loc_4731")

    label("loc_4720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_472A")
    Jump("loc_4731")

    label("loc_472A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4731")

    label("loc_4731")

    TalkEnd(0xFE)
    Return()

    # Function_26_468F end

    def Function_27_4735(): pass

    label("Function_27_4735")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_47B1")

    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "爸爸他究竟要点过多少次名才罢休嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4812")

    label("loc_47B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_47BB")
    Jump("loc_4812")

    label("loc_47BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_47C5")
    Jump("loc_4812")

    label("loc_47C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_47CF")
    Jump("loc_4812")

    label("loc_47CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_47D9")
    Jump("loc_4812")

    label("loc_47D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_47E3")
    Jump("loc_4812")

    label("loc_47E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_47ED")
    Jump("loc_4812")

    label("loc_47ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_47F7")
    Jump("loc_4812")

    label("loc_47F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4801")
    Jump("loc_4812")

    label("loc_4801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_480B")
    Jump("loc_4812")

    label("loc_480B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4812")

    label("loc_4812")

    TalkEnd(0xFE)
    Return()

    # Function_27_4735 end

    def Function_28_4816(): pass

    label("Function_28_4816")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_4854")

    ChrTalk(
        0xFE,
        "哎呀～好想进城去看看呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_48D9")

    label("loc_4854")

    OP_A2(0x12)

    ChrTalk(
        0xFE,
        "咦～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这里就是格兰赛尔城吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………咦～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们约好\x01",
            "在哪里见面呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48D9")

    TalkEnd(0xFE)
    Return()

    # Function_28_4816 end

    def Function_29_48DD(): pass

    label("Function_29_48DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4A1A")

    ChrTalk(
        0xFE,
        (
            "刚才本打算在这里求婚的，\x01",
            "这时，城门突然打开了，\x01",
            "然后亲卫队和游击士冲了过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我以为是来阻止我求婚的，\x01",
            "吓了我一大跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "结果我还是\x01",
            "没能向她求成婚。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3C")

    label("loc_4A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4A6C")

    ChrTalk(
        0xFE,
        "艾娅莉，请听我说！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天对于我们俩来说，\x01",
            "是个特别有意义的日子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3C")

    label("loc_4A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4AEF")

    ChrTalk(
        0xFE,
        (
            "虽说转遍了\x01",
            "街上的各个地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但能够最好表达\x01",
            "感情的地方果然\x01",
            "还是王城前面啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3C")

    label("loc_4AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4AF9")
    Jump("loc_4B3C")

    label("loc_4AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4B03")
    Jump("loc_4B3C")

    label("loc_4B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4B0D")
    Jump("loc_4B3C")

    label("loc_4B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4B17")
    Jump("loc_4B3C")

    label("loc_4B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4B21")
    Jump("loc_4B3C")

    label("loc_4B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4B2B")
    Jump("loc_4B3C")

    label("loc_4B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4B35")
    Jump("loc_4B3C")

    label("loc_4B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4B3C")

    label("loc_4B3C")

    TalkEnd(0xFE)
    Return()

    # Function_29_48DD end

    def Function_30_4B40(): pass

    label("Function_30_4B40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4C09")

    ChrTalk(
        0xFE,
        (
            "没有想到会\x01",
            "遇到这样的麻烦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，我们俩这趟旅程的\x01",
            "最高潮从现在才开始哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C76")

    label("loc_4C09")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "女王陛下和公主殿下，\x01",
            "她们都好有气质啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个时候的骚乱\x01",
            "原来是件不得了的大事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C76")

    Jump("loc_4EC6")

    label("loc_4C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4D07")

    ChrTalk(
        0xFE,
        (
            "啊啊，阿鲁姆……\x01",
            "这一刻终于到来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我那强烈的心跳声……\x01",
            "被他听到了该怎么办啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC6")

    label("loc_4D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4E79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4DAD")

    ChrTalk(
        0xFE,
        (
            "今天他好像\x01",
            "在想什么事情，\x01",
            "可又不告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，太坏了。\x01",
            "我可要撒娇了哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E76")

    label("loc_4DAD")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "呵呵，他呀，\x01",
            "今天总是在自言自语。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像在想什么事情，\x01",
            "可又不告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，太坏了。\x01",
            "我可要撒娇了哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E76")

    Jump("loc_4EC6")

    label("loc_4E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4E83")
    Jump("loc_4EC6")

    label("loc_4E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4E8D")
    Jump("loc_4EC6")

    label("loc_4E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4E97")
    Jump("loc_4EC6")

    label("loc_4E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4EA1")
    Jump("loc_4EC6")

    label("loc_4EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4EAB")
    Jump("loc_4EC6")

    label("loc_4EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4EB5")
    Jump("loc_4EC6")

    label("loc_4EB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4EBF")
    Jump("loc_4EC6")

    label("loc_4EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4EC6")

    label("loc_4EC6")

    TalkEnd(0xFE)
    Return()

    # Function_30_4B40 end

    def Function_31_4ECA(): pass

    label("Function_31_4ECA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我的钱包应该不会被偷去的，\x01",
            "因为我把它放在腰包里面了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀？\x01",
            "怎么不见了呢……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_4ECA end

    def Function_32_4F3E(): pass

    label("Function_32_4F3E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "爸爸，我要喝果汁嘛～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_4F3E end

    def Function_33_4F61(): pass

    label("Function_33_4F61")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "对呀对呀，就在那边的拐角……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我看到了一个和科洛蒂娅公主\x01",
            "长得很相似的女孩哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "难道真的是她本人吗？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_4F61 end

    def Function_34_4FF4(): pass

    label("Function_34_4FF4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哎呀，夫人真是的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公主殿下刚才\x01",
            "还在王城的阳台上面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果说是换了着装到外面来，\x01",
            "是不是也太快了一点呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_4FF4 end

    def Function_35_50A8(): pass

    label("Function_35_50A8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "是呀，肯定是看错了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且从那里走过的女孩\x01",
            "穿的还是学校的校服呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_50A8 end

    def Function_36_5131(): pass

    label("Function_36_5131")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "果然如此，\x01",
            "既壮丽又富有历史气息，\x01",
            "这些街道真是两者兼备啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且给人以安定的感觉……\x01",
            "果然和共和国的城市不一样。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_5131 end

    def Function_37_521A(): pass

    label("Function_37_521A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "啊，又来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就是因为这样，\x01",
            "所以我讨厌和爸爸一起来这里。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_521A end

    def Function_38_5266(): pass

    label("Function_38_5266")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "准～备，咔嚓！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……我们不打算在这里住宿，\x01",
            "所以要趁现在多照一些照片作为纪念才行。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_5266 end

    def Function_39_52F2(): pass

    label("Function_39_52F2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我的女儿女婿为了给我们庆祝六十大寿，\x01",
            "特地用王都旅行作为祝寿的礼物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既然是她俩的好意，我们就来了，\x01",
            "正好也碰上女王陛下的诞辰庆典。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，哪怕只有一次机会，\x01",
            "能来王都游览一下也很不错呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_52F2 end

    def Function_40_53F3(): pass

    label("Function_40_53F3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哎呀，我说老伴儿啊，\x01",
            "就在这个旅馆里面住下如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是异常华丽的建筑呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_53F3 end

    def Function_41_5449(): pass

    label("Function_41_5449")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "好不容易来王都一趟，\x01",
            "一定要到处去逛逛。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_5449 end

    def Function_42_5494(): pass

    label("Function_42_5494")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "这附近是什么地方呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "没有地图所以迷路了……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_5494 end

    def Function_43_54F2(): pass

    label("Function_43_54F2")

    EventBegin(0x0)
    OP_6D(2190, 0, 46270, 0)
    OP_67(0, 29260, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(432, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    StopSound(0x9C40, 0x3D090, 0x0)
    FadeToBright(2000, 0)

    def lambda_5556():
        OP_6C(90000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5556)
    Sleep(1000)

    def lambda_556B():
        OP_6D(10350, 3620, 43920, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_556B)

    def lambda_5583():
        OP_67(0, 3740, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5583)
    StopSound(0x9C40, 0x249F0, 0x2710)
    Sleep(10000)
    ClearMapFlags(0x100000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4132   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_43_54F2 end

    def Function_44_55B9(): pass

    label("Function_44_55B9")

    Return()

    # Function_44_55B9 end

    def Function_45_55BA(): pass

    label("Function_45_55BA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5616")
    OP_8E(0xFE, 0xED8, 0x0, 0x9E3E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF466, 0x0, 0x9E3E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF466, 0x0, 0x10018, 0xBB8, 0x0)
    OP_8E(0xFE, 0xED8, 0x0, 0x100F4, 0xBB8, 0x0)
    Jump("Function_45_55BA")

    label("loc_5616")

    Return()

    # Function_45_55BA end

    def Function_46_5617(): pass

    label("Function_46_5617")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5855")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_564A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5767")

    label("loc_564A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5670")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5767")

    label("loc_5670")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5696")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5767")

    label("loc_5696")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56BD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5767")

    label("loc_56BD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56E3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5767")

    label("loc_56E3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5709")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5767")

    label("loc_5709")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_572E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5767")

    label("loc_572E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5753")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5767")

    label("loc_5753")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5767")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5852")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    OP_69(0xFE, 0x3E8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5843")

    ChrTalk(
        0xFE,
        "你们是干什么的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（糟了……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（被发现了……）\x02",
    )

    CloseMessageWindow()

    label("loc_5843")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_5852")

    Jump("Function_46_5617")

    label("loc_5855")

    Return()

    # Function_46_5617 end

    def Function_47_5856(): pass

    label("Function_47_5856")

    EventBegin(0x0)
    OP_6D(17700, 510, 43970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    OP_6C(90000, 0)
    SetChrPos(0x101, 17540, 510, 44210, 270)
    SetChrPos(0x102, 17540, 510, 43360, 270)

    ChrTalk(
        0x101,
        "#000F啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_58CF():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58CF)
    OP_6D(4010, 0, 38720, 3000)
    SetChrPos(0x101, 13280, 250, 49870, 225)
    SetChrPos(0x102, 14070, 250, 49980, 225)
    Sleep(1000)
    OP_6D(13610, 250, 50130, 3000)

    ChrTalk(
        0x102,
        (
            "#010F（已经在巡逻了呢。）\x02\x03",
            "（我们要想办法不被他们发现，\x01",
            "　然后找一条安全的路线到达大圣堂。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（嗯，我知道了……）\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_47_5856 end

    def Function_48_59A3(): pass

    label("Function_48_59A3")

    SetPlaceName(0xB4) # 罗恩鲍姆酒店
    Return()

    # Function_48_59A3 end

    SaveToFile()

Try(main)
