from ED6ScenarioHelper import *

def main():
    # 阳光铃铛酒廊

    CreateScenaFile(
        FileName            = 'T4100   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4100.x',
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
        '奥利维尔',                             # 9
        '士兵',                                 # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        '士兵',                                 # 14
        '士兵',                                 # 15
        '士兵',                                 # 16
        '士兵',                                 # 17
        '克鲁茨',                               # 18
        '比尔爷爷',                             # 19
        '伊鲁妮婆婆',                           # 20
        '嘉瑟',                                 # 21
        '芬尼尔',                               # 22
        '诺娜',                                 # 23
        '阿鲁姆',                               # 24
        '艾娅莉',                               # 25
        '蒂库',                                 # 26
        '拉尔斯',                               # 27
        '托伊',                                 # 28
        '伯登',                                 # 29
        '拉塔娜',                               # 30
        '托朗老人',                             # 31
        '士兵',                                 # 32
        '士兵',                                 # 33
        '士兵',                                 # 34
        '士兵',                                 # 35
        '特务兵',                               # 36
        '特务兵',                               # 37
        '特务兵',                               # 38
        '游客',                                 # 39
        '游客',                                 # 40
        '游客',                                 # 41
        '游客',                                 # 42
        '游客',                                 # 43
        '游客',                                 # 44
        '游客',                                 # 45
        '游客',                                 # 46
        '米拉诺',                               # 47
        '西蒙',                                 # 48
        '游客',                                 # 49
        '游客',                                 # 50
        '游客',                                 # 51
        '游客',                                 # 52
        '梅贝尔市长',                           # 53
        '莉拉',                                 # 54
        '王都格兰赛尔·北街区',                 # 55
        '庭园大道方向',                         # 56
        '王都格兰赛尔·东街区',                 # 57
        '王都格兰赛尔·西街区',                 # 58
    )

    DeclEntryPoint(
        Unknown_00              = 5200,
        Unknown_04              = 0,
        Unknown_08              = 1000,
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
        'ED6_DT07/CH00102 ._CH',             # 01
        'ED6_DT06/CH20038 ._CH',             # 02
        'ED6_DT07/CH00107 ._CH',             # 03
        'ED6_DT07/CH01640 ._CH',             # 04
        'ED6_DT07/CH01620 ._CH',             # 05
        'ED6_DT07/CH01490 ._CH',             # 06
        'ED6_DT07/CH01180 ._CH',             # 07
        'ED6_DT07/CH01270 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01050 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01150 ._CH',             # 0C
        'ED6_DT07/CH01160 ._CH',             # 0D
        'ED6_DT07/CH01470 ._CH',             # 0E
        'ED6_DT07/CH01060 ._CH',             # 0F
        'ED6_DT07/CH01200 ._CH',             # 10
        'ED6_DT07/CH01210 ._CH',             # 11
        'ED6_DT07/CH01100 ._CH',             # 12
        'ED6_DT07/CH01610 ._CH',             # 13
        'ED6_DT07/CH01020 ._CH',             # 14
        'ED6_DT07/CH01220 ._CH',             # 15
        'ED6_DT07/CH01460 ._CH',             # 16
        'ED6_DT07/CH01130 ._CH',             # 17
        'ED6_DT07/CH01680 ._CH',             # 18
        'ED6_DT07/CH01690 ._CH',             # 19
        'ED6_DT07/CH01120 ._CH',             # 1A
        'ED6_DT07/CH01110 ._CH',             # 1B
        'ED6_DT07/CH01230 ._CH',             # 1C
        'ED6_DT07/CH01480 ._CH',             # 1D
        'ED6_DT07/CH01150 ._CH',             # 1E
        'ED6_DT07/CH01170 ._CH',             # 1F
        'ED6_DT07/CH01000 ._CH',             # 20
        'ED6_DT07/CH01010 ._CH',             # 21
        'ED6_DT07/CH02360 ._CH',             # 22
        'ED6_DT07/CH02370 ._CH',             # 23
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT07/CH00102P._CP',             # 01
        'ED6_DT06/CH20038P._CP',             # 02
        'ED6_DT07/CH00107P._CP',             # 03
        'ED6_DT07/CH01640P._CP',             # 04
        'ED6_DT07/CH01620P._CP',             # 05
        'ED6_DT07/CH01490P._CP',             # 06
        'ED6_DT07/CH01180P._CP',             # 07
        'ED6_DT07/CH01270P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01050P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01150P._CP',             # 0C
        'ED6_DT07/CH01160P._CP',             # 0D
        'ED6_DT07/CH01470P._CP',             # 0E
        'ED6_DT07/CH01060P._CP',             # 0F
        'ED6_DT07/CH01200P._CP',             # 10
        'ED6_DT07/CH01210P._CP',             # 11
        'ED6_DT07/CH01100P._CP',             # 12
        'ED6_DT07/CH01610P._CP',             # 13
        'ED6_DT07/CH01020P._CP',             # 14
        'ED6_DT07/CH01220P._CP',             # 15
        'ED6_DT07/CH01460P._CP',             # 16
        'ED6_DT07/CH01130P._CP',             # 17
        'ED6_DT07/CH01680P._CP',             # 18
        'ED6_DT07/CH01690P._CP',             # 19
        'ED6_DT07/CH01120P._CP',             # 1A
        'ED6_DT07/CH01110P._CP',             # 1B
        'ED6_DT07/CH01230P._CP',             # 1C
        'ED6_DT07/CH01480P._CP',             # 1D
        'ED6_DT07/CH01150P._CP',             # 1E
        'ED6_DT07/CH01170P._CP',             # 1F
        'ED6_DT07/CH01000P._CP',             # 20
        'ED6_DT07/CH01010P._CP',             # 21
        'ED6_DT07/CH02360P._CP',             # 22
        'ED6_DT07/CH02370P._CP',             # 23
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 54,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 55,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 56,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 57,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 58,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 59,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 0,
        Y                   = -63100,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 7810,
        Z                   = 0,
        Y                   = -1510,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 7800,
        Z                   = 0,
        Y                   = -530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -5720,
        Z                   = 0,
        Y                   = -36280,
        Direction           = 281,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -5830,
        Z                   = 0,
        Y                   = -55640,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 5550,
        Z                   = 0,
        Y                   = -54380,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
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
        TalkScenaIndex      = 23,
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
        TalkScenaIndex      = 22,
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
        TalkScenaIndex      = 21,
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
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 5760,
        Z                   = 0,
        Y                   = -46060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -2070,
        Z                   = 0,
        Y                   = -5120,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 3520,
        Z                   = 0,
        Y                   = 10640,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 6280,
        Z                   = 0,
        Y                   = 2180,
        Direction           = 215,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -6430,
        Z                   = 0,
        Y                   = -22020,
        Direction           = 45,
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
        X                   = 4760,
        Z                   = 0,
        Y                   = -39600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = -29870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 6280,
        Z                   = 0,
        Y                   = 2180,
        Direction           = 215,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4760,
        Z                   = 0,
        Y                   = -39600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = -29870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -6250,
        Z                   = 0,
        Y                   = -870,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -6250,
        Z                   = 0,
        Y                   = -1920,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = -8540,
        Z                   = 250,
        Y                   = 6040,
        Direction           = 172,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -8540,
        Z                   = 250,
        Y                   = 4630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -5690,
        Z                   = 0,
        Y                   = -7580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 13060,
        Z                   = 250,
        Y                   = 4130,
        Direction           = 51,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 7390,
        Z                   = 250,
        Y                   = -15350,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 7390,
        Z                   = 250,
        Y                   = -17380,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = -7510,
        Z                   = 250,
        Y                   = -16200,
        Direction           = 99,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = -8330,
        Z                   = 250,
        Y                   = -14940,
        Direction           = 138,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = 8300,
        Z                   = 250,
        Y                   = 3500,
        Direction           = 170,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 7330,
        Z                   = 250,
        Y                   = -27330,
        Direction           = 37,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = -7120,
        Z                   = 250,
        Y                   = -30460,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 7170,
        Z                   = 250,
        Y                   = -10430,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = -80,
        Z                   = 0,
        Y                   = -49760,
        Direction           = 160,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = -990,
        Z                   = 0,
        Y                   = -50700,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 10,
        Z                   = 250,
        Y                   = 36990,
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
        X                   = -50,
        Z                   = 0,
        Y                   = -90220,
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
        X                   = 54990,
        Z                   = 0,
        Y                   = -1130,
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
        X                   = -44420,
        Z                   = 0,
        Y                   = -19990,
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
        X                   = 5270,
        Y                   = -1000,
        Z                   = -67700,
        Range               = -6090,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF0182,
        Unknown_18          = 0x0,
        Unknown_1C          = 71,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -25000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 73,
    )

    DeclEvent(
        X                   = -10280,
        Y                   = 0,
        Z                   = -11040,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 74,
    )

    DeclEvent(
        X                   = -14940,
        Y                   = 0,
        Z                   = -15750,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 74,
    )

    DeclEvent(
        X                   = -10290,
        Y                   = 0,
        Z                   = -30020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 75,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -13010,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 76,
    )

    DeclEvent(
        X                   = 15900,
        Y                   = 0,
        Z                   = 6330,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 77,
    )


    ScpFunction(
        "Function_0_8EA",          # 00, 0
        "Function_1_E19",          # 01, 1
        "Function_2_10F5",         # 02, 2
        "Function_3_127D",         # 03, 3
        "Function_4_12A1",         # 04, 4
        "Function_5_12FE",         # 05, 5
        "Function_6_138B",         # 06, 6
        "Function_7_13AF",         # 07, 7
        "Function_8_141E",         # 08, 8
        "Function_9_148D",         # 09, 9
        "Function_10_14EC",        # 0A, 10
        "Function_11_1581",        # 0B, 11
        "Function_12_15CF",        # 0C, 12
        "Function_13_1842",        # 0D, 13
        "Function_14_1AA4",        # 0E, 14
        "Function_15_1C96",        # 0F, 15
        "Function_16_1E7D",        # 10, 16
        "Function_17_2711",        # 11, 17
        "Function_18_31C2",        # 12, 18
        "Function_19_3C11",        # 13, 19
        "Function_20_3E3B",        # 14, 20
        "Function_21_4254",        # 15, 21
        "Function_22_464A",        # 16, 22
        "Function_23_49CA",        # 17, 23
        "Function_24_4EF8",        # 18, 24
        "Function_25_546B",        # 19, 25
        "Function_26_5AA4",        # 1A, 26
        "Function_27_6300",        # 1B, 27
        "Function_28_635C",        # 1C, 28
        "Function_29_63B2",        # 1D, 29
        "Function_30_66A5",        # 1E, 30
        "Function_31_66EE",        # 1F, 31
        "Function_32_679B",        # 20, 32
        "Function_33_67FD",        # 21, 33
        "Function_34_68C8",        # 22, 34
        "Function_35_693C",        # 23, 35
        "Function_36_69EF",        # 24, 36
        "Function_37_6A35",        # 25, 37
        "Function_38_6A87",        # 26, 38
        "Function_39_6B0A",        # 27, 39
        "Function_40_6B53",        # 28, 40
        "Function_41_6B73",        # 29, 41
        "Function_42_6C2C",        # 2A, 42
        "Function_43_6CBB",        # 2B, 43
        "Function_44_6D0E",        # 2C, 44
        "Function_45_70D0",        # 2D, 45
        "Function_46_71B8",        # 2E, 46
        "Function_47_71CC",        # 2F, 47
        "Function_48_7CF3",        # 30, 48
        "Function_49_7E18",        # 31, 49
        "Function_50_85A9",        # 32, 50
        "Function_51_8718",        # 33, 51
        "Function_52_89C7",        # 34, 52
        "Function_53_8F96",        # 35, 53
        "Function_54_91FC",        # 36, 54
        "Function_55_926A",        # 37, 55
        "Function_56_92D8",        # 38, 56
        "Function_57_931E",        # 39, 57
        "Function_58_9364",        # 3A, 58
        "Function_59_93AA",        # 3B, 59
        "Function_60_9418",        # 3C, 60
        "Function_61_9821",        # 3D, 61
        "Function_62_9F36",        # 3E, 62
        "Function_63_A000",        # 3F, 63
        "Function_64_A155",        # 40, 64
        "Function_65_A276",        # 41, 65
        "Function_66_A3A7",        # 42, 66
        "Function_67_A556",        # 43, 67
        "Function_68_A679",        # 44, 68
        "Function_69_A7C4",        # 45, 69
        "Function_70_A8CD",        # 46, 70
        "Function_71_AAE2",        # 47, 71
        "Function_72_ABCD",        # 48, 72
        "Function_73_ABE9",        # 49, 73
        "Function_74_ABED",        # 4A, 74
        "Function_75_ABF1",        # 4B, 75
        "Function_76_ABF5",        # 4C, 76
        "Function_77_ABF9",        # 4D, 77
    )


    def Function_0_8EA(): pass

    label("Function_0_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_8FD")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 49)

    label("loc_8FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_90E")
    OP_A3(0x3FB)
    SoundLoad(125)
    Event(0, 51)

    label("loc_90E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_91C")
    OP_A3(0x3FC)
    Event(0, 60)

    label("loc_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_92F")
    SetMapFlags(0x10000000)
    OP_A3(0x3FD)
    Event(0, 61)

    label("loc_92F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_93F"),
        (103, "loc_955"),
        (SWITCH_DEFAULT, "loc_96B"),
    )


    label("loc_93F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_952")
    OP_A2(0x608)
    Event(0, 47)

    label("loc_952")

    Jump("loc_96B")

    label("loc_955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_968")
    OP_A2(0x629)
    Event(0, 52)

    label("loc_968")

    Jump("loc_96B")

    label("loc_96B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A25")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -4270, 0, -46090, 273)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -5960, 0, -47010, 44)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -5960, 0, -45200, 140)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    Jump("loc_E18")

    label("loc_A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A80")
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    Jump("loc_E18")

    label("loc_A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_AE0")
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_E18")

    label("loc_AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B6C")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -3830, 0, -46790, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -3810, 0, -44860, 180)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_E18")

    label("loc_B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B8A")
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_E18")

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BFB")
    SetChrPos(0x14, -5720, 0, -37010, 257)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_E18")

    label("loc_BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C31")
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 270)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 90)
    Jump("loc_E18")

    label("loc_C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CA9")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 5340, 0, -37270, 84)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 5410, 0, -37950, 90)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)
    Jump("loc_E18")

    label("loc_CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_D2B")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 5340, 0, -37270, 84)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 5410, 0, -37950, 90)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 270)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 90)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -5300, 0, -38930, 315)
    SetChrFlags(0x1B, 0x10)
    Jump("loc_E18")

    label("loc_D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_DA3")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -3830, 0, -46790, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -3810, 0, -44860, 180)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)
    Jump("loc_E18")

    label("loc_DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_E18")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -3830, 0, -46790, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -3810, 0, -44860, 180)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)

    label("loc_E18")

    Return()

    # Function_0_8EA end

    def Function_1_E19(): pass

    label("Function_1_E19")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x3005B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3C")
    OP_1C(0x10, 0x0, 0x30)

    label("loc_E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E50")
    OP_1B(0x3, 0x0, 0x2E)
    Jump("loc_E73")

    label("loc_E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_E63")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E73")

    label("loc_E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_E73")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EA6")
    OP_B1("t4100_y")
    Jump("loc_EAF")

    label("loc_EA6")

    OP_B1("t4100_n")

    label("loc_EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBF")
    OP_1B(0x0, 0x0, 0x3F)
    Jump("loc_F5C")

    label("loc_EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED8")
    OP_1B(0x0, 0x0, 0x32)
    Jump("loc_F5C")

    label("loc_ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EEC")
    OP_1B(0x0, 0x0, 0x40)
    Jump("loc_F5C")

    label("loc_EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F00")
    OP_1B(0x0, 0x0, 0x41)
    Jump("loc_F5C")

    label("loc_F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F14")
    OP_1B(0x0, 0x0, 0x42)
    Jump("loc_F5C")

    label("loc_F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F28")
    OP_1B(0x0, 0x0, 0x43)
    Jump("loc_F5C")

    label("loc_F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3C")
    OP_1B(0x0, 0x0, 0x44)
    Jump("loc_F5C")

    label("loc_F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F50")
    OP_1B(0x0, 0x0, 0x45)
    Jump("loc_F5C")

    label("loc_F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_F5C")
    OP_1B(0x0, 0x0, 0x46)

    label("loc_F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F86")
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x2, 0x10)
    OP_72(0x4, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x10, 0x10)

    label("loc_F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FE4")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_43(0xB, 0x1, 0x0, 0x35)
    OP_43(0xC, 0x1, 0x0, 0x35)
    OP_43(0xD, 0x1, 0x0, 0x35)
    OP_43(0xE, 0x1, 0x0, 0x35)
    OP_43(0xF, 0x1, 0x0, 0x35)
    OP_43(0x10, 0x1, 0x0, 0x35)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_10D8")
    OP_72(0x19, 0x4)
    LoadEffect(0x0, "map\\\\mp016_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -70, 0, -46310, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -70, 250, -24300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -70, 0, -5700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -70, 0, 8590, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_10D8")

    SoundDistance(0x1CB, 0x32, 0x0, 0xFFFF4A70, 0x7D0, 0x3A98, 0x64, 0x0)
    Return()

    # Function_1_E19 end

    def Function_2_10F5(): pass

    label("Function_2_10F5")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1125")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_1267")

    label("loc_1125")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_1267")

    label("loc_113E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1157")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_1267")

    label("loc_1157")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1170")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_1267")

    label("loc_1170")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1189")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_1267")

    label("loc_1189")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A2")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_1267")

    label("loc_11A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BB")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_1267")

    label("loc_11BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D4")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_1267")

    label("loc_11D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11ED")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_1267")

    label("loc_11ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1206")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_1267")

    label("loc_1206")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_1267")

    label("loc_121F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1238")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_1267")

    label("loc_1238")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1251")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_1267")

    label("loc_1251")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1267")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_1267")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_127C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1267")

    label("loc_127C")

    Return()

    # Function_2_10F5 end

    def Function_3_127D(): pass

    label("Function_3_127D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12A0")
    OP_8D(0xFE, 3700, -42040, 10110, -50100, 2000)
    Jump("Function_3_127D")

    label("loc_12A0")

    Return()

    # Function_3_127D end

    def Function_4_12A1(): pass

    label("Function_4_12A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12FD")
    OP_8E(0xFE, 0xFFFFF7EA, 0x0, 0xFFFF6E24, 0x8FC, 0x0)
    OP_8E(0xFE, 0x9CE, 0x0, 0xFFFF6E24, 0x8FC, 0x0)
    OP_8E(0xFE, 0x9CE, 0x0, 0x2166, 0x8FC, 0x0)
    OP_8E(0xFE, 0xFFFFF7EA, 0x0, 0x2166, 0x8FC, 0x0)
    Jump("Function_4_12A1")

    label("loc_12FD")

    Return()

    # Function_4_12A1 end

    def Function_5_12FE(): pass

    label("Function_5_12FE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_138A")
    OP_8E(0xFE, 0xDC0, 0x0, 0xFFFF6532, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF29A, 0x0, 0xFFFF6532, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF29A, 0x0, 0x2990, 0x7D0, 0x0)
    OP_8E(0xFE, 0xDC0, 0x0, 0x2990, 0x7D0, 0x0)
    Jump("Function_5_12FE")

    label("loc_138A")

    Return()

    # Function_5_12FE end

    def Function_6_138B(): pass

    label("Function_6_138B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13AE")
    OP_8D(0xFE, 7470, -10200, 1790, -22030, 3000)
    Jump("Function_6_138B")

    label("loc_13AE")

    Return()

    # Function_6_138B end

    def Function_7_13AF(): pass

    label("Function_7_13AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_141D")
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFFFB5A, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_7_13AF")

    label("loc_141D")

    Return()

    # Function_7_13AF end

    def Function_8_141E(): pass

    label("Function_8_141E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_148C")
    OP_8E(0xFE, 0xFFFFEE44, 0x0, 0xFFFFAFC4, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFEEB2, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    Jump("Function_8_141E")

    label("loc_148C")

    Return()

    # Function_8_141E end

    def Function_9_148D(): pass

    label("Function_9_148D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "亲卫队那群家伙竟敢\x01",
            "反抗理查德上校，不可饶恕。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_148D end

    def Function_10_14EC(): pass

    label("Function_10_14EC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "干嘛，你这家伙是游击士吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不想挨揍的话\x01",
            "就乖乖地回协会去。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_14EC end

    def Function_11_1581(): pass

    label("Function_11_1581")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "王城已经完全封锁了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生了什么事吗……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1581 end

    def Function_12_15CF(): pass

    label("Function_12_15CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_16A0")

    ChrTalk(
        0xFE,
        "呀，你们是游击士吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "街道的警备就交给我们了，\x01",
            "今天你们就好好享受庆典带来的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "政变的时候\x01",
            "我们没能做什么，\x01",
            "现在我们会努力的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_16A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_16AA")
    Jump("loc_183E")

    label("loc_16AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_16F2")

    ChrTalk(
        0xFE,
        (
            "从今天起空港\x01",
            "好像被完全封锁了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_16F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_176B")

    ChrTalk(
        0xFE,
        (
            "随着天色变晚，\x01",
            "巡逻也加紧了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果发现可疑的人\x01",
            "请马上告诉我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_176B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1792")

    ChrTalk(
        0xFE,
        "嗯，没有任何异常。\x02",
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_1792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_180F")

    ChrTalk(
        0xFE,
        (
            "从今天开始\x01",
            "街上加强了警备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这也是为了\x01",
            "保证大家的安全。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_180F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1819")
    Jump("loc_183E")

    label("loc_1819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1823")
    Jump("loc_183E")

    label("loc_1823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_182D")
    Jump("loc_183E")

    label("loc_182D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1837")
    Jump("loc_183E")

    label("loc_1837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_183E")

    label("loc_183E")

    TalkEnd(0xFE)
    Return()

    # Function_12_15CF end

    def Function_13_1842(): pass

    label("Function_13_1842")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_18E3")

    ChrTalk(
        0xFE,
        (
            "我们也想留在王都\x01",
            "为女王陛下而战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是假传的命令把我们从王都撤走了，\x01",
            "真是可恶啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_18E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_18ED")
    Jump("loc_1AA0")

    label("loc_18ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1960")

    ChrTalk(
        0xFE,
        (
            "诞辰庆典\x01",
            "会怎么样呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "女王陛下的病情很让人担心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_1960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_19CD")

    ChrTalk(
        0xFE,
        (
            "武术大会结束以后，\x01",
            "我心里的石头也落地了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，不能放松，\x01",
            "必须要继续保持警惕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_19CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1A1A")

    ChrTalk(
        0xFE,
        (
            "希望武术大会\x01",
            "能圆满顺利地闭幕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_1A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1A71")

    ChrTalk(
        0xFE,
        (
            "武术大会正在进行，\x01",
            "千万不能太放松警惕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1A7B")
    Jump("loc_1AA0")

    label("loc_1A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A85")
    Jump("loc_1AA0")

    label("loc_1A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1A8F")
    Jump("loc_1AA0")

    label("loc_1A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1A99")
    Jump("loc_1AA0")

    label("loc_1A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1AA0")

    label("loc_1AA0")

    TalkEnd(0xFE)
    Return()

    # Function_13_1842 end

    def Function_14_1AA4(): pass

    label("Function_14_1AA4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1B3F")

    ChrTalk(
        0xFE,
        (
            "理查德上校是这起政变的发动者，\x01",
            "对此至今我都无法相信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也许你们不知道，\x01",
            "亲卫队那些家伙\x01",
            "真的是干了不少坏事的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C92")

    label("loc_1B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1B49")
    Jump("loc_1C92")

    label("loc_1B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1B88")

    ChrTalk(
        0xFE,
        (
            "游击士协会\x01",
            "应该没有窝藏\x01",
            "恐怖分子吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C92")

    label("loc_1B88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1BD7")

    ChrTalk(
        0xFE,
        (
            "如果发现亲卫队的人，\x01",
            "请立刻通报。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C92")

    label("loc_1BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1C11")

    ChrTalk(
        0xFE,
        "怎么了，不许妨碍我们。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C92")

    label("loc_1C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1C63")

    ChrTalk(
        0xFE,
        "你们是游击士吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可不要做出什么\x01",
            "奇怪的举动哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C92")

    label("loc_1C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1C6D")
    Jump("loc_1C92")

    label("loc_1C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C77")
    Jump("loc_1C92")

    label("loc_1C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1C81")
    Jump("loc_1C92")

    label("loc_1C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1C8B")
    Jump("loc_1C92")

    label("loc_1C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1C92")

    label("loc_1C92")

    TalkEnd(0xFE)
    Return()

    # Function_14_1AA4 end

    def Function_15_1C96(): pass

    label("Function_15_1C96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1D09")

    ChrTalk(
        0xFE,
        (
            "王都还存在着\x01",
            "特务部队余党的可能性很高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定要做好戒备才行。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1D13")
    Jump("loc_1E79")

    label("loc_1D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1D86")

    ChrTalk(
        0xFE,
        (
            "特务部队那些人明明是新来的，\x01",
            "还一副了不起的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "气死人了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1DB9")

    ChrTalk(
        0xFE,
        (
            "那些恐怖分子……\x01",
            "到底躲在哪儿呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1DF6")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "我也想去看总决赛啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1E4A")

    ChrTalk(
        0xFE,
        (
            "看见可疑的人\x01",
            "要马上过来报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1E54")
    Jump("loc_1E79")

    label("loc_1E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E5E")
    Jump("loc_1E79")

    label("loc_1E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1E68")
    Jump("loc_1E79")

    label("loc_1E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1E72")
    Jump("loc_1E79")

    label("loc_1E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1E79")

    label("loc_1E79")

    TalkEnd(0xFE)
    Return()

    # Function_15_1C96 end

    def Function_16_1E7D(): pass

    label("Function_16_1E7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_200D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1F2B")

    ChrTalk(
        0xFE,
        (
            "那位理查德上校\x01",
            "是政变的发动者啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前我在城外见过他，\x01",
            "从他的目光里真的可以看出\x01",
            "他是为了王国着想的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_200A")

    label("loc_1F2B")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "那位理查德上校\x01",
            "是政变的发动者啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前我在城外见过他，\x01",
            "从他的目光里真的可以看出\x01",
            "他是为了王国着想的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那难道也是演技吗……\x02",
    )

    CloseMessageWindow()

    label("loc_200A")

    Jump("loc_270D")

    label("loc_200D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_20C2")

    ChrTalk(
        0xFE,
        (
            "亲卫队的那些人\x01",
            "要是突然改变主意\x01",
            "来进攻王城怎么办……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望不要给艾莉茜雅女王\x01",
            "造成什么威胁。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_20C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_214F")

    ChrTalk(
        0xFE,
        (
            "女王陛下的病情\x01",
            "到底怎么样了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "目前一点新消息都没有，\x01",
            "我担心得夜夜都睡不好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_214F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_21B9")

    ChrTalk(
        0xFE,
        (
            "武术大会\x01",
            "平安地结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "诞辰庆典\x01",
            "又会怎么样呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_21B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_222F")

    ChrTalk(
        0xFE,
        (
            "每日散步\x01",
            "就是我健康的秘诀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天天气很好啊，\x01",
            "而且还吹着清爽的风。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_222F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_22A0")

    ChrTalk(
        0xFE,
        (
            "谈到理查德上校啊，\x01",
            "他确实是个很优秀的人物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他才是真正\x01",
            "为利贝尔王国着想的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_22A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2329")

    ChrTalk(
        0xFE,
        (
            "我虽然也很\x01",
            "喜欢武术大会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但听说女王陛下病了，\x01",
            "就没有心情兴高采烈地\x01",
            "去看比赛了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_2329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_23BD")

    ChrTalk(
        0xFE,
        (
            "像这种亲卫队被\x01",
            "王国军追捕的事情\x01",
            "是前所未闻的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总感觉\x01",
            "会发生什么大事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_23BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2583")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_246B")

    ChrTalk(
        0xFE,
        (
            "艾尔贝离宫没有举行仪式的时候\x01",
            "是对市民们开放的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过现在好像是作为\x01",
            "王国军对付恐怖分子的\x01",
            "总部来使用了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2580")

    label("loc_246B")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "艾尔贝离宫没有举行仪式的时候\x01",
            "是对市民们开放的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这几年里，\x01",
            "要说王家用到离宫的时候，\x01",
            "也就只有外国的重要人物来访时了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过现在好像是作为\x01",
            "王国军对付恐怖分子的\x01",
            "总部来使用了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2580")

    Jump("loc_270D")

    label("loc_2583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_26C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_260E")

    ChrTalk(
        0xFE,
        (
            "本来打算去艾尔贝离宫散步的，\x01",
            "不过现在那里不让一般人接近了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是无聊啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_26BE")

    label("loc_260E")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "天气不错，我本来打算到\x01",
            "艾尔贝离宫去好好散散步的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是最近王国军贴出了公告，\x01",
            "现在那里不让一般人接近了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是无聊啊。\x02",
    )

    CloseMessageWindow()

    label("loc_26BE")

    Jump("loc_270D")

    label("loc_26C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_270D")

    ChrTalk(
        0xFE,
        (
            "这条大道是\x01",
            "格兰赛尔的繁华大街啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这大道中央散步，\x01",
            "已经成了我每天必做之事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_270D")

    TalkEnd(0xFE)
    Return()

    # Function_16_1E7D end

    def Function_17_2711(): pass

    label("Function_17_2711")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_28DF")
    Jc((scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_END)), "loc_27DF")

    ChrTalk(
        0xFE,
        (
            "那位理查德上校\x01",
            "是政变主谋的说法，\x01",
            "我怎么也无法相信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算是真的，\x01",
            "肯定也是因为有\x01",
            "比山高比海深的原因。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DC")

    label("loc_27DF")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "那位理查德上校\x01",
            "是政变主谋的说法，\x01",
            "我怎么也无法相信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算是真的，\x01",
            "肯定也是因为有\x01",
            "比山高比海深的原因。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，肯定是这样！\x02",
    )

    CloseMessageWindow()

    label("loc_28DC")

    Jump("loc_31BE")

    label("loc_28DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_299D")

    ChrTalk(
        0xFE,
        (
            "士兵的数量增加了不少，\x01",
            "却也不发表一下声明，真让人担忧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来想外出的，\x01",
            "现在看来还是回家为好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_299D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2A75")

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "武术大会历来都是\x01",
            "诞辰庆典的开胃菜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，女王陛下生病了，\x01",
            "诞辰庆典会怎么样呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_2A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2AF8")

    ChrTalk(
        0xFE,
        "街上的人都在谈论武术大会呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像这次优胜者\x01",
            "出乎大家的预料哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_2AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2B8B")

    ChrTalk(
        0xFE,
        "今天是决赛哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也要去竞技场\x01",
            "好好看一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_2B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2C7E")

    ChrTalk(
        0xFE,
        (
            "理查德上校身后\x01",
            "总是跟着一个狐媚的副官。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她那蔑视别人的眼神\x01",
            "真让人讨厌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么那样的人\x01",
            "会跟在上校身边呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_2C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2E2C")
    Jc((scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_END)), "loc_2D27")

    ChrTalk(
        0xFE,
        (
            "理查德上校以前也是\x01",
            "从武术大会里脱颖而出的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "使得一手变幻莫测的剑术，\x01",
            "相当的强悍呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E29")

    label("loc_2D27")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "理查德上校以前也是\x01",
            "从武术大会里脱颖而出的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "使得一手变幻莫测的剑术，\x01",
            "相当的强悍呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说好像是从一位\x01",
            "相当厉害的剑术老师那里学来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E29")

    Jump("loc_31BE")

    label("loc_2E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2F8F")
    Jc((scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_END)), "loc_2EB9")

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "真的是一个很酷的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从在柏斯逮捕空贼以来，\x01",
            "我已经完全为上校而着迷了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F8C")

    label("loc_2EB9")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "真的是一个很酷的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "长得又帅，头脑又好，\x01",
            "简直是完美的男人啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从在柏斯逮捕空贼以来，\x01",
            "我已经完全为上校而着迷了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8C")

    Jump("loc_31BE")

    label("loc_2F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_30BC")
    Jc((scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_END)), "loc_3001")

    ChrTalk(
        0xFE,
        (
            "我很讨厌那个公爵\x01",
            "做女王的代理人什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女王陛下，\x01",
            "请早日康复吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B9")

    label("loc_3001")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "我很讨厌那个公爵\x01",
            "做女王的代理人什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然最近他的一些发言\x01",
            "还算说得过去，\x01",
            "不过我还是觉得那副打扮很奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女王陛下，\x01",
            "请早日康复吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B9")

    Jump("loc_31BE")

    label("loc_30BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3120")

    ChrTalk(
        0xFE,
        (
            "刚才有一个\x01",
            "非常高大的壮汉走了过去，\x01",
            "好像是大会的选手。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_3120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_31BE")

    ChrTalk(
        0xFE,
        (
            "因为武术大会要开始了，\x01",
            "所以东街区现在热闹的不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "预选赛\x01",
            "很快就要开始了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31BE")

    TalkEnd(0xFE)
    Return()

    # Function_17_2711 end

    def Function_18_31C2(): pass

    label("Function_18_31C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3234")

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "已经被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他竟然是个坏人，\x01",
            "我怎么看不出来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_3234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3298")

    ChrTalk(
        0xFE,
        "那些士兵好可怕。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "感觉不是很太平啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_3298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3321")

    ChrTalk(
        0xFE,
        (
            "这条大街旁边的树\x01",
            "是科洛蒂娅公主\x01",
            "降生的时候种植的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是光阴似箭啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_3321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_33CA")

    ChrTalk(
        0xFE,
        (
            "大会的优胜者\x01",
            "能参加城里的晚宴啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我对那个\x01",
            "主办者公爵没好印象，\x01",
            "但肯定是个很华丽的宴会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_33CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3425")

    ChrTalk(
        0xFE,
        (
            "因为今天是总决赛的日子，\x01",
            "所以有很多人很早就出门了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_3425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_35B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_34D3")

    ChrTalk(
        0xFE,
        (
            "最近，\x01",
            "常常能看见身穿黑色铠甲的士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那就是传闻中\x01",
            "王国军的反恐精英吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B3")

    label("loc_34D3")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "最近，\x01",
            "常常能看见身穿黑色铠甲的士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正好就是从\x01",
            "女王病倒的时候开始呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那就是传闻中\x01",
            "王国军的反恐精英吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B3")

    Jump("loc_3C0D")

    label("loc_35B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3658")

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "喜欢武术大会的人\x01",
            "一大早就会到会场去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了占到好位置，\x01",
            "好像还有人彻夜排队呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_3658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3702")

    ChrTalk(
        0xFE,
        (
            "在格兰赛尔的市民中，\x01",
            "理查德上校的人气\x01",
            "可以说是直线上升。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，作为一个男人而言，\x01",
            "他是个既帅又厉害的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_3702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3802")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3764")

    ChrTalk(
        0xFE,
        (
            "这个格兰赛尔的\x01",
            "地下水路经过了一番整修。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这样还真是方便多了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37FF")

    label("loc_3764")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "这个格兰赛尔的\x01",
            "地下水路经过了一番整修。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看，\x01",
            "大街上到处都是排水口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这样还真是方便多了。\x02",
    )

    CloseMessageWindow()

    label("loc_37FF")

    Jump("loc_3C0D")

    label("loc_3802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_38A8")

    ChrTalk(
        0xFE,
        (
            "这个喷水的雕像\x01",
            "是只白隼哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "它是利贝尔的国鸟，\x01",
            "国旗上有它的图案，\x01",
            "王家的徽章上也有它。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_38A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3C0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_39FF")

    ChrTalk(
        0xFE,
        (
            "这个城市一共分为\x01",
            "四个主要区域哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个南街区有游击士协会和商店，\x01",
            "北街区有王国最大的酒店，\x01",
            "往北直走就是格兰赛尔城了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "西街区有大圣堂和出版社，\x01",
            "东街区则有各国大使馆、\x01",
            "竞技场和百货店。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_39FF")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        "哟，是第一次来到格兰赛尔吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个城市一共分为\x01",
            "四个主要区域哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里是南街区，有游击士协会\x01",
            "以及鳞次栉比的各种商店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "北街区有王国最大的酒店，\x01",
            "往北直走就是格兰赛尔城了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "西街区有大圣堂和\x01",
            "利贝尔通讯社，\x01",
            "是众人皆知的公共设施之地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后是东街区，\x01",
            "有着各国大使馆和竞技场，\x01",
            "还有大型的百货店。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0D")

    TalkEnd(0xFE)
    Return()

    # Function_18_31C2 end

    def Function_19_3C11(): pass

    label("Function_19_3C11")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3C3E")

    ChrTalk(
        0xFE,
        "庆典真的很好玩呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3C70")

    ChrTalk(
        0xFE,
        "坏蛋来了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3C93")

    ChrTalk(
        0xFE,
        "呜呜～肚子好饿啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3CDA")

    ChrTalk(
        0xFE,
        (
            "说起来，比赛结束的时候\x01",
            "只有那个红头盔没有气喘吁吁的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3CE4")
    Jump("loc_3E37")

    label("loc_3CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3D3D")

    ChrTalk(
        0xFE,
        (
            "我想明天游击士的\x01",
            "那个小组会取胜吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "只是直觉而已啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3D47")
    Jump("loc_3E37")

    label("loc_3D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3DCB")

    ChrTalk(
        0xFE,
        (
            "一个人就那么强，\x01",
            "四个人在一起的话\x01",
            "不就是最强了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3DEC")

    ChrTalk(
        0xFE,
        "哇啊～好像很好吃呀！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3E13")

    ChrTalk(
        0xFE,
        "实在是酷得不得了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3E37")

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "门票掉到哪里去了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E37")

    TalkEnd(0xFE)
    Return()

    # Function_19_3C11 end

    def Function_20_3E3B(): pass

    label("Function_20_3E3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3EEC")

    ChrTalk(
        0xFE,
        "蒂库他对美女毫无抵抗力。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据我统计，\x01",
            "他只要一看到美女，\x01",
            "有９５％的概率都会一见钟情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_3EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3F43")

    ChrTalk(
        0xFE,
        "奇怪啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们不觉得\x01",
            "那些士兵有些慌乱吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_3F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3F92")

    ChrTalk(
        0xFE,
        (
            "今年的诞辰庆典\x01",
            "能照原计划举办吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_3F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3FDE")

    ChrTalk(
        0xFE,
        "好精彩的比赛呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "简直可以称为『激斗』。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_3FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3FE8")
    Jump("loc_4250")

    label("loc_3FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4086")

    ChrTalk(
        0xFE,
        (
            "我对游击士之间的比赛\x01",
            "很有兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为平时看不到这样的场面。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_4086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_40C0")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "托伊他确实是一个路痴……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_40C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_415D")

    ChrTalk(
        0xFE,
        (
            "托伊发表的意见\x01",
            "有时没有根据，\x01",
            "但却能够抓住问题的核心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过，这次会怎样呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_415D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_41C4")

    ChrTalk(
        0xFE,
        (
            "托伊他趁我不留神的时候\x01",
            "一下就跑得不见了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_41C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_420D")

    ChrTalk(
        0xFE,
        (
            "问题是只靠一个人\x01",
            "究竟能走多远……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_420D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4250")

    ChrTalk(
        0xFE,
        (
            "如果不快点的话\x01",
            "就找不到座位了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4250")

    TalkEnd(0xFE)
    Return()

    # Function_20_3E3B end

    def Function_21_4254(): pass

    label("Function_21_4254")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_42BE")

    ChrTalk(
        0xFE,
        (
            "哇～\x01",
            "科洛蒂娅公主既温柔又漂亮呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我好心动啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_42BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4307")

    ChrTalk(
        0xFE,
        (
            "大街上怎么全是士兵\x01",
            "在跑来跑去呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_4307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4347")

    ChrTalk(
        0xFE,
        (
            "武术大会也结束了，\x01",
            "今天玩什么好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_4347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_439B")

    ChrTalk(
        0xFE,
        (
            "我还以为戴红头盔的\x01",
            "那个人会赢呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_439B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_43A5")
    Jump("loc_4646")

    label("loc_43A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4423")

    ChrTalk(
        0xFE,
        (
            "红头盔的那家伙和空贼的比赛\x01",
            "很有魄力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然今年的冠军\x01",
            "还是会被王国军夺得吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_4423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_444A")

    ChrTalk(
        0xFE,
        (
            "喂喂，\x01",
            "托伊那家伙今天迟到了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_444A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_456E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_44D2")

    ChrTalk(
        0xFE,
        (
            "差不多能看出来\x01",
            "各个组的实力水平了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个叫做金的选手\x01",
            "也请了另外三个人来助拳了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_456B")

    label("loc_44D2")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "那个戴红头盔的人\x01",
            "相当强嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "差不多能看出来\x01",
            "各个组的实力水平了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个叫做金的选手\x01",
            "也请了另外三个人来助拳了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_456B")

    Jump("loc_4646")

    label("loc_456E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_45D4")

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "为什么他总是这样呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想早点去竞技场\x01",
            "占个好座位啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_45D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4628")

    ChrTalk(
        0xFE,
        "那个共和国的人好强。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "单打独斗就获胜了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_4628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4646")

    ChrTalk(
        0xFE,
        "真是的，托伊那家伙……\x02",
    )

    CloseMessageWindow()

    label("loc_4646")

    TalkEnd(0xFE)
    Return()

    # Function_21_4254 end

    def Function_22_464A(): pass

    label("Function_22_464A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4657")
    Jump("loc_49C6")

    label("loc_4657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4661")
    Jump("loc_49C6")

    label("loc_4661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_47D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4707")

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
    Jump("loc_47D0")

    label("loc_4707")

    OP_A2(0x6)

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

    label("loc_47D0")

    Jump("loc_49C6")

    label("loc_47D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_47FD")

    ChrTalk(
        0xFE,
        "嘻嘻，他真是热情啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_49C6")

    label("loc_47FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4832")

    ChrTalk(
        0xFE,
        "哇，这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是难以置信地好吃啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_49C6")

    label("loc_4832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_483C")
    Jump("loc_49C6")

    label("loc_483C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4846")
    Jump("loc_49C6")

    label("loc_4846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_48A2")

    ChrTalk(
        0xFE,
        (
            "他呀，\x01",
            "那时一直都在盯着我的脸看……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "讨厌，真让人家害羞。\x02",
    )

    CloseMessageWindow()
    Jump("loc_49C6")

    label("loc_48A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_492A")

    ChrTalk(
        0xFE,
        (
            "今天一整天\x01",
            "又和他一起渡过了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "到格兰赛尔来旅行\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C6")

    label("loc_492A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_498A")

    ChrTalk(
        0xFE,
        (
            "他啊，在看比赛的时候\x01",
            "也紧紧地握住我的手呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C6")

    label("loc_498A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_49C6")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "好想到王城里去看看啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49C6")

    TalkEnd(0xFE)
    Return()

    # Function_22_464A end

    def Function_23_49CA(): pass

    label("Function_23_49CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_49D7")
    Jump("loc_4EF4")

    label("loc_49D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_49E1")
    Jump("loc_4EF4")

    label("loc_49E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4A64")

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
            "感情的地方果然还是\x01",
            "王城前面啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF4")

    label("loc_4A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4BC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4AB3")

    ChrTalk(
        0xFE,
        (
            "啊啊，\x01",
            "这世上还有比这更加美丽的东西吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BC3")

    label("loc_4AB3")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "在火红的黄昏中屹立着\x01",
            "美丽的王都和格兰赛尔城……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且，\x01",
            "还有映出那样美景的你的双眸……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊，\x01",
            "这世上还有比这更加美丽的东西吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不，绝对没有！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "没有就是没有！\x02",
    )

    CloseMessageWindow()

    label("loc_4BC3")

    Jump("loc_4EF4")

    label("loc_4BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4BF4")

    ChrTalk(
        0xFE,
        "唔～不愧是王室御用店呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EF4")

    label("loc_4BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4BFE")
    Jump("loc_4EF4")

    label("loc_4BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4C08")
    Jump("loc_4EF4")

    label("loc_4C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4CA9")

    ChrTalk(
        0xFE,
        (
            "呼，看比赛的过程中\x01",
            "不自觉地侧过脸去凝视她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "究竟有多少魅力呢，\x01",
            "她的美丽难道也是罪过吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF4")

    label("loc_4CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4CF4")

    ChrTalk(
        0xFE,
        (
            "好～的，\x01",
            "今天也要和她一起度过\x01",
            "比这个糖果还要甜美的时刻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF4")

    label("loc_4CF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4E84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4D93")

    ChrTalk(
        0xFE,
        (
            "竞技场正在被\x01",
            "鼎沸的热情所包围着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了不辜负这股热情，\x01",
            "我俩也要热恋起来才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E81")

    label("loc_4D93")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "既然不能进入王城，\x01",
            "那就先去看看武术大会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竞技场正在被\x01",
            "鼎沸的热情所包围着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了不辜负这股热情，\x01",
            "我俩也要热恋起来才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E81")

    Jump("loc_4EF4")

    label("loc_4E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4EF4")

    ChrTalk(
        0xFE,
        "哦，怎么会这样！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我和心肝宝贝儿\x01",
            "一起到王都来旅行，\x01",
            "可现在竟然不能进入王城。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF4")

    TalkEnd(0xFE)
    Return()

    # Function_23_49CA end

    def Function_24_4EF8(): pass

    label("Function_24_4EF8")

    TalkBegin(0x16)
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

    MenuEnd(0x4)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F58")
    OP_0D()
    OP_A9(0x72)
    OP_56(0x0)
    TalkEnd(0x16)
    Return()

    label("loc_4F58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F69")
    TalkEnd(0x16)
    Return()

    label("loc_4F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4FA7")

    ChrTalk(
        0x16,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "请慢慢挑选！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_4FA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5030")

    ChrTalk(
        0x16,
        (
            "与之前在这里的士兵不同，\x01",
            "新来的是一些黑衣士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "发生什么事了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_5030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5111")

    ChrTalk(
        0x16,
        (
            "武术大会结束以后，\x01",
            "街道上也安静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "随着女王陛下的诞辰庆典临近，\x01",
            "街上应该又会热闹起来的吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "不过今年的情况究竟会如何呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_5111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5188")

    ChrTalk(
        0x16,
        (
            "唔～\x01",
            "至少想去看看决赛呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "不过为了能独立生活，\x01",
            "就必须得努力工作才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_5188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_51C8")

    ChrTalk(
        0x16,
        (
            "欢迎光临，\x01",
            "我这里的草莓薄饼非常好吃哦，\x01",
            "向你们强烈推荐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_51C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5263")

    ChrTalk(
        0x16,
        (
            "在这个时期打工\x01",
            "会得到更高的工钱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "但代价就是\x01",
            "不能去看武术大会了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_5263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_52A2")

    ChrTalk(
        0x16,
        (
            "欢迎光临！\x01",
            "本店的薄饼十分美味哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_52A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_52E6")

    ChrTalk(
        0x16,
        (
            "啊～啊，\x01",
            "就不能多卖一些吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_52E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_534C")

    ChrTalk(
        0x16,
        "那边的哥哥姐姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "来一些美味的薄饼如何？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_534C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_53EA")

    ChrTalk(
        0x16,
        (
            "我为了独立生活，\x01",
            "所以就在这里打工。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "西街区有一间\x01",
            "正在出售的空的房子，\x01",
            "我准备把那里买下来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_53EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5467")

    ChrTalk(
        0x16,
        "欢迎～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "来尝尝吧，很好吃的哦！\x02",
    )

    CloseMessageWindow()

    label("loc_5467")

    TalkEnd(0x16)
    Return()

    # Function_24_4EF8 end

    def Function_25_546B(): pass

    label("Function_25_546B")

    TalkBegin(0x15)
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

    MenuEnd(0x4)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54CB")
    OP_0D()
    OP_A9(0x71)
    OP_56(0x0)
    TalkEnd(0x15)
    Return()

    label("loc_54CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54DC")
    TalkEnd(0x15)
    Return()

    label("loc_54DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_55C0")

    ChrTalk(
        0x15,
        (
            "东街区的冰淇淋小店\x01",
            "很受欢迎呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "我虽然去侦察过，\x01",
            "可排的队太长了，没能买到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "好～的，我绝对不能输！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_55C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_562B")

    ChrTalk(
        0x15,
        (
            "那些黑衣士兵们\x01",
            "也是属于王国军的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "他们很有压迫感，\x01",
            "我都有些害怕了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_562B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_56D1")

    ChrTalk(
        0x15,
        (
            "在诞辰庆典之前，\x01",
            "我打算一直在格兰赛尔摆摊子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "不过，女王陛下的病无法痊愈的话，\x01",
            "诞辰庆典恐怕就要中止了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_56D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5736")

    ChrTalk(
        0x15,
        (
            "呼，\x01",
            "今天天气也很好嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "柏斯地区\x01",
            "也应该很晴朗吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_5736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5802")

    ChrTalk(
        0x15,
        (
            "昨天从傍晚开始，\x01",
            "大街上的士兵就增多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "虽然我是个奉公守法的市民，\x01",
            "不过看到这种场面也有点紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_5802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5857")

    ChrTalk(
        0x15,
        "您好，欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "好吃的冰淇淋，\x01",
            "来品尝一个好吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_5857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_590D")

    ChrTalk(
        0x15,
        (
            "大赛从第一天开始\x01",
            "就非常热闹了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "竞技场里传来的欢呼声\x01",
            "连这里都能听见。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_590D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5962")

    ChrTalk(
        0x15,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "在为大会加油而疲惫的时候，\x01",
            "难道不想要来点甘甜的东西吗！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_5962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_59BE")

    ChrTalk(
        0x15,
        (
            "我原以为柏斯\x01",
            "就算很大的了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "不愧是王都啊，\x01",
            "光是街上行人的数量就这么多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_59BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5A5E")

    ChrTalk(
        0x15,
        (
            "我平时是在\x01",
            "柏斯做生意的，\x01",
            "这次出差到了王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "我为了做好买卖\x01",
            "而到各个地方\x01",
            "去寻找机遇。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_5A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5AA0")

    ChrTalk(
        0x15,
        "您好，欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "来一个冰淇淋怎么样？\x02",
    )

    CloseMessageWindow()

    label("loc_5AA0")

    TalkEnd(0x15)
    Return()

    # Function_25_546B end

    def Function_26_5AA4(): pass

    label("Function_26_5AA4")

    TalkBegin(0x14)
    OP_A3(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5AB4")
    Jump("loc_5B24")

    label("loc_5AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5AC1")
    OP_A2(0xE)
    Jump("loc_5B24")

    label("loc_5AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5ACB")
    Jump("loc_5B24")

    label("loc_5ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5AD8")
    OP_A2(0xE)
    Jump("loc_5B24")

    label("loc_5AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5AE5")
    OP_A2(0xE)
    Jump("loc_5B24")

    label("loc_5AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5AEF")
    Jump("loc_5B24")

    label("loc_5AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5AF9")
    Jump("loc_5B24")

    label("loc_5AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5B06")
    OP_A2(0xE)
    Jump("loc_5B24")

    label("loc_5B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5B13")
    OP_A2(0xE)
    Jump("loc_5B24")

    label("loc_5B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5B1D")
    Jump("loc_5B24")

    label("loc_5B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5B24")

    label("loc_5B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_5B99")
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

    MenuEnd(0x4)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B88")
    OP_0D()
    OP_A9(0x73)
    OP_56(0x0)
    TalkEnd(0x14)
    Return()

    label("loc_5B88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B99")
    TalkEnd(0x14)
    Return()

    label("loc_5B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5D1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5C52")

    ChrTalk(
        0x14,
        (
            "飞艇停运了，\x01",
            "商品也就送不过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "这回的这个麻烦事\x01",
            "就不能怪在我头上了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D1B")

    label("loc_5C52")

    OP_A2(0x2)

    ChrTalk(
        0x14,
        (
            "呼，飞艇停运了，\x01",
            "商品也就送不过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "真让人着急啊，\x01",
            "为什么总是这么巧呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "这回的这个麻烦事\x01",
            "就不能怪在我头上了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D1B")

    Jump("loc_62FC")

    label("loc_5D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5D68")

    ChrTalk(
        0x14,
        "怎么那么多士兵啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "啊！\x01",
            "又、又有什么麻烦了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_5D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5D96")

    ChrTalk(
        0x14,
        (
            "天哪～！\x01",
            "轮胎爆胎啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_5D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5ED7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5E4F")

    ChrTalk(
        0x14,
        (
            "没有麻烦\x01",
            "反而让我有些失望啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "我的人生似乎就是\x01",
            "与麻烦形影不离的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ED4")

    label("loc_5E4F")

    OP_A2(0x2)

    ChrTalk(
        0x14,
        (
            "今天没有\x01",
            "出现什么麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "不过这反而\x01",
            "让人有些失望呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "我的人生似乎就是\x01",
            "与麻烦形影不离的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ED4")

    Jump("loc_62FC")

    label("loc_5ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5F1F")

    ChrTalk(
        0x14,
        (
            "呼，\x01",
            "今天要是没有麻烦就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_5F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_60C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5FB9")

    ChrTalk(
        0x14,
        (
            "货物拿不出来，\x01",
            "今日的销售额为零。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "呜呜，\x01",
            "我怎么总是这么倒霉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60C3")

    label("loc_5FB9")

    OP_A2(0x2)

    ChrTalk(
        0x14,
        (
            "因为一直在\x01",
            "修理货箱的缘故，\x01",
            "所以今天很忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "货物拿不出来，\x01",
            "今日的销售额为零。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "呜呜，\x01",
            "我怎么总是这么倒霉啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60C3")

    Jump("loc_62FC")

    label("loc_60C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6154")

    ChrTalk(
        0x14,
        (
            "这、这回箱子坏了，\x01",
            "彻底打不开了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "呜呜，\x01",
            "我怎么总是这么倒霉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_6154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_61EB")

    ChrTalk(
        0x14,
        (
            "比赛的前后\x01",
            "是顾客最多的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "比赛开始时\x01",
            "就可以松一口气了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_61EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6228")

    ChrTalk(
        0x14,
        (
            "呼，\x01",
            "总算是把现金出纳机修好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_6228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_62A5")

    ChrTalk(
        0x14,
        (
            "好不容易等到武术大会，\x01",
            "正是客人多的时候……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "呜呜，\x01",
            "我怎么总是这么倒霉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_62A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_62FC")

    ChrTalk(
        0x14,
        "唔～糟糕了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "现金出纳机坏掉了。\x01",
            "怎么办好呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62FC")

    TalkEnd(0x14)
    Return()

    # Function_26_5AA4 end

    def Function_27_6300(): pass

    label("Function_27_6300")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哎呀，可喜可贺可喜可贺！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "女王陛下万岁，公主殿下万岁！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_6300 end

    def Function_28_635C(): pass

    label("Function_28_635C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "当我看到科洛蒂娅公主的身影时，\x01",
            "一下就感觉到利贝尔王国的未来\x01",
            "将是平稳安泰的了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_635C end

    def Function_29_63B2(): pass

    label("Function_29_63B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_63BF")
    Jump("loc_66A1")

    label("loc_63BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_63C9")
    Jump("loc_66A1")

    label("loc_63C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_63D3")
    Jump("loc_66A1")

    label("loc_63D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_63DD")
    Jump("loc_66A1")

    label("loc_63DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_63E7")
    Jump("loc_66A1")

    label("loc_63E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_63F1")
    Jump("loc_66A1")

    label("loc_63F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_63FB")
    Jump("loc_66A1")

    label("loc_63FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6405")
    Jump("loc_66A1")

    label("loc_6405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6690")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_64A7")

    ChrTalk(
        0xFE,
        (
            "#840F虽然参加了武术大会，\x01",
            "但游击士的任务\x01",
            "并不能因此而怠慢。\x02\x03",
            "我正要去处理\x01",
            "一些简单的委托。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_668D")

    label("loc_64A7")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "#840F哦……是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，克鲁茨大哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F怎么了？\x01",
            "在这种地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#840F我现在正要去\x01",
            "剿灭通缉魔兽。\x02\x03",
            "虽然参加了武术大会，\x01",
            "但游击士的任务\x01",
            "并不能因此而怠慢。\x02\x03",
            "我正要去处理\x01",
            "一些简单的委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F啊～不愧是前辈～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#841F哈哈，\x01",
            "就算是稍微热热身吧。\x02\x03",
            "对了，\x01",
            "如果我们在比赛中相遇了，\x01",
            "还请你们手下留情哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F彼此彼此，\x01",
            "请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_668D")

    Jump("loc_66A1")

    label("loc_6690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_669A")
    Jump("loc_66A1")

    label("loc_669A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_66A1")

    label("loc_66A1")

    TalkEnd(0xFE)
    Return()

    # Function_29_63B2 end

    def Function_30_66A5(): pass

    label("Function_30_66A5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我们是借诞辰庆典的机会\x01",
            "来王都参观游览的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_66A5 end

    def Function_31_66EE(): pass

    label("Function_31_66EE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "接下来去哪儿好呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说大圣堂也是个好去处，\x01",
            "但我又想去看看长城『亚宁堡』。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_66EE end

    def Function_32_679B(): pass

    label("Function_32_679B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "是老妈带我\x01",
            "到王都来的，\x01",
            "这里的街道真宽啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_679B end

    def Function_33_67FD(): pass

    label("Function_33_67FD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "我已经累得不行了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是到处都没有\x01",
            "可以休息的地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "去酒廊里又要花钱……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_67FD end

    def Function_34_68C8(): pass

    label("Function_34_68C8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "当听说发生了政变时，\x01",
            "我吓了一大跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过看着街道这么热闹的样子，\x01",
            "怎么也无法想象发生过那样的事情。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_68C8 end

    def Function_35_693C(): pass

    label("Function_35_693C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "肚子好饿呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好不容易来了王都一趟，\x01",
            "想要到一些有名的餐馆去，\x01",
            "不知道这家如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像每家餐馆都很不错，\x01",
            "简直让我眼花缭乱……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_693C end

    def Function_36_69EF(): pass

    label("Function_36_69EF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "这里是很热闹，\x01",
            "但东街区的人更多。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_69EF end

    def Function_37_6A35(): pass

    label("Function_37_6A35")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我找不到路了，\x01",
            "要去游击士协会问问。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_6A35 end

    def Function_38_6A87(): pass

    label("Function_38_6A87")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哈～不愧是诞辰庆典，\x01",
            "好热闹呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "诞辰庆典时期\x01",
            "就应该到这里来做生意。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_6A87 end

    def Function_39_6B0A(): pass

    label("Function_39_6B0A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "传说中\x01",
            "最好吃的那个冰淇淋店\x01",
            "在哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_6B0A end

    def Function_40_6B53(): pass

    label("Function_40_6B53")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "那个商店是卖什么的呢？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_6B53 end

    def Function_41_6B73(): pass

    label("Function_41_6B73")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "各种事件相继发生，\x01",
            "能够回归和平的日子真好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了女王陛下，\x01",
            "我以后也要好好加油啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_6B73 end

    def Function_42_6C2C(): pass

    label("Function_42_6C2C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "终于看到好久不见的女王陛下，\x01",
            "我已经很满足了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有这么好的一位女王陛下，\x01",
            "却还要发动什么政变，\x01",
            "不知道那些人是怎么想的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_6C2C end

    def Function_43_6CBB(): pass

    label("Function_43_6CBB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "因为飞艇停航的缘故，\x01",
            "我来到格兰赛尔时\x01",
            "已经耽误很长时间了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_6CBB end

    def Function_44_6D0E(): pass

    label("Function_44_6D0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 0)), scpexpr(EXPR_END)), "loc_6D7D")

    ChrTalk(
        0xFE,
        (
            "#611F呵呵，正游击士的徽章\x01",
            "和你们二人很相配呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F啊……嗯，谢谢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_70CC")

    label("loc_6D7D")

    OP_A2(0x6E8)

    ChrTalk(
        0xFE,
        (
            "#617F……呵呵，晚宴之后\x01",
            "就知道想要很快回去是不可能的了，\x01",
            "只有在这里多滞留一会儿了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈，\x01",
            "各位市长是要进行一些商议对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#610F嗯，科林兹校长的提案是\x01",
            "召开一个临时王国会议。\x02\x03",
            "#612F由于政变的混乱，\x01",
            "这次的事件给市民带来的影响绝对不能小视。\x01",
            "　\x02\x03",
            "因此现在各个地区保持联系合作是必要的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊～\x01",
            "看来市长姐姐又要变得越来越忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#610F呵呵，\x01",
            "至少今天可以不受拘束地放松一下。\x02\x03",
            "这就准备散步到大圣堂去做礼拜呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F说起来，我们第一次见面时\x01",
            "市长姐姐就逃掉了礼拜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#617F嗯，\x01",
            "所以这次我更要好好地祷告了。\x01",
            "　\x02\x03",
            "看来到大圣堂还得把至今为止偷的懒\x01",
            "一起做个忏悔才行呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70CC")

    TalkEnd(0xFE)
    Return()

    # Function_44_6D0E end

    def Function_45_70D0(): pass

    label("Function_45_70D0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#620F就算连日参加会议，\x01",
            "和小姐平常的工作量相比也轻松了许多。\x01",
            "　\x02\x03",
            "看来想要让小姐休息，\x01",
            "还是离开柏斯最好……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_70D0 end

    def Function_46_71B8(): pass

    label("Function_46_71B8")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x3, 0x0, 0xFFFF)
    Return()

    # Function_46_71B8 end

    def Function_47_71CC(): pass

    label("Function_47_71CC")

    EventBegin(0x0)
    SetChrPos(0x1C, 5760, 0, -46060, 270)
    OP_43(0x1C, 0x0, 0x0, 0x2)
    OP_6D(600, 250, 1950, 0)
    OP_67(0, 17690, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(571, 0)
    SetChrPos(0x101, -100, 0, -56250, 0)
    SetChrPos(0x102, -1060, 0, -58160, 0)
    SetChrPos(0x10E, 890, 0, -58220, 0)

    def lambda_725C():
        OP_6D(-270, 1500, -57160, 11000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_725C)
    Sleep(2000)

    def lambda_7279():
        OP_6B(3000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7279)

    def lambda_7289():
        OP_67(0, 4000, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7289)

    def lambda_72A1():
        OP_6C(8000, 11000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_72A1)

    def lambda_72B1():
        OP_6E(273, 9000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_72B1)
    Sleep(11000)

    ChrTalk(
        0x101,
        (
            "#001F#5P哇～～\x01",
            "好大的城市啊。\x02\x03",
            "以前和老爸一起来的时候，\x01",
            "就有这么大吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F当然了，这是王国最大的城市嘛。\x02\x03",
            "这条大街的最前方，\x01",
            "就是女王陛下所居住的格兰赛尔城……\x02\x03",
            "还有七耀教会的大圣堂、王立竞技场，\x01",
            "以及各国的大使馆之类的设施呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#501F#5P哎～是这样啊。\x02\x03",
            "不过约修亚，你还真是了解啊。\x02\x03",
            "以前也来过这里吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015F嗯……\x01",
            "也是小时候的事情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F真的是……\x01",
            "这城市无论何时看起来都是这么美丽呢。\x02\x03",
            "不过单从规模上来说，\x01",
            "帝国和共和国的首都比这里要更大一些。\x01",
            "　\x02\x03",
            "不过这个格兰赛尔，\x01",
            "可是有着其他地方比不上的舒适感呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_75C1():
        TurnDirection(0xFE, 0x10E, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75C1)
    TurnDirection(0x101, 0x10E, 400)

    ChrTalk(
        0x101,
        (
            "#506F#5P嘿嘿，真是高兴啊。\x01",
            "能听到外国的朋友这么说。\x02\x03",
            "#501F对了……\x01",
            "教授，你接下来打算怎么样呢？\x02\x03",
            "日常生活的费用有着落吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x101, 400)

    ChrTalk(
        0x10E,
        (
            "#130F哈哈，其实是有保障的。\x02\x03",
            "我会暂时寄住在一个叫\x01",
            "『历史资料馆』的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#5P哎，还有这样的地方啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是个展示发掘出来的文物\x01",
            "和美术品之类的博物馆吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F对，作为那里的名誉会员，\x01",
            "我可以在那里借住一段时间。\x02\x03",
            "艾丝蒂尔、约修亚，\x01",
            "如果方便的话你们也过来玩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#5P唔……说到博物馆，\x01",
            "就有一种很严肃的气氛……\x02\x03",
            "#509F是不是要说『既然来了，就学习吧』？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#132F呵呵，如果你真的愿意的话，\x01",
            "我也可以认真地教教你。\x02\x03",
            "#130F……开玩笑的。\x01",
            "去那里只要参观一下展示品，\x01",
            "就已经会感到很开心的。\x02\x03",
            "那么，我就此告辞了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7961():

        label("loc_7961")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_7961")

    QueueWorkItem2(0x101, 1, lambda_7961)

    def lambda_7972():

        label("loc_7972")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_7972")

    QueueWorkItem2(0x102, 1, lambda_7972)
    OP_8C(0x10E, 45, 400)
    OP_8E(0x10E, 0xFDB, 0x0, 0xFFFF29DC, 0xFA0, 0x0)

    def lambda_799E():
        OP_8E(0xFE, 0x1356, 0x0, 0xFFFF76E4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_799E)

    def lambda_79B9():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_79B9)

    def lambda_79C9():
        OP_6D(-780, 0, -56940, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_79C9)

    def lambda_79E1():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_79E1)

    def lambda_79F9():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_79F9)

    def lambda_7A09():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x10E, 3, lambda_7A09)
    Sleep(3000)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#506F#5P哈～该怎么说呢，\x01",
            "还是老样子，是个乐天派的人呢。\x02\x03",
            "#006F不过说到名誉会员，\x01",
            "他应该是个相当有名的学者吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F嗯，说不定就是呢。\x02\x03",
            "#010F那么，我们先去拜访一下\x01",
            "游击士协会格兰赛尔支部吧？\x02\x03",
            "要办理转属手续……\x01",
            "而且要完成博士交待的委托，\x01",
            "也要先和协会商量一下才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        (
            "#505F#5P嗯，没错……\x02\x03",
            "仔细想想，\x01",
            "该怎么和女王陛下会面呢？\x02\x03",
            "#007F肯定不会是去城里就能见到\x01",
            "那样简单容易吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x54, 0x3, 0x2)
    OP_28(0x54, 0x3, 0x4)
    OP_28(0x45, 0x4, 0x2)
    OP_28(0x45, 0x4, 0x4)
    OP_28(0x45, 0x1, 0x1)
    OP_28(0x45, 0x1, 0x2)
    OP_28(0x45, 0x1, 0x4)
    OP_28(0x45, 0x1, 0x8)
    OP_28(0x45, 0x1, 0x10)
    OP_28(0x45, 0x1, 0x20)
    OP_28(0x45, 0x1, 0x40)
    RemoveParty(0xD, 0xFF)
    EventEnd(0x0)
    OP_43(0x1C, 0x0, 0x0, 0x3)
    Return()

    # Function_47_71CC end

    def Function_48_7CF3(): pass

    label("Function_48_7CF3")

    EventBegin(0x0)
    OP_20(0x5DC)
    OP_8C(0x0, 0, 0)
    TurnDirection(0x1, 0x0, 0)
    OP_6D(16030, 500, 7220, 1000)
    OP_21()
    OP_1D(0x48)
    OP_1F(0x4B, 0xC8)
    Sleep(2000)

    ChrTalk(
        0x101,
        (
            "#004F啊……\x02\x03",
            "这是……钢琴声？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F嗯，不像是放唱片的。\x01",
            "应该是有人在里面弹钢琴吧。\x02\x03",
            "这个旋律，\x01",
            "好像觉得在哪里听过呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F有点不好的预感呢……\x02",
    )

    CloseMessageWindow()
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_48_7CF3 end

    def Function_49_7E18(): pass

    label("Function_49_7E18")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(16020, 250, 7280, 0)
    OP_6C(315000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x102, 15830, 740, 8470, 0)
    SetChrPos(0x101, 15830, 740, 8470, 0)
    SetChrPos(0x8, 15830, 740, 8470, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x10, 0x10)
    OP_70(0x10, 0x3C)
    OP_73(0x10)
    OP_6F(0x10, 60)

    def lambda_7E9C():
        OP_8E(0xFE, 0x3B7E, 0xFA, 0xF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E9C)
    Sleep(400)

    def lambda_7EBC():
        OP_8E(0xFE, 0x4060, 0xFA, 0xE6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7EBC)
    Sleep(500)

    def lambda_7EDC():
        OP_8E(0xFE, 0x3E9E, 0xFA, 0x14FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7EDC)
    OP_6D(16100, 250, 4400, 2000)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x8, 400)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#509F我说，为什么你又这么\x01",
            "理所当然地跟了出来啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#035F哈·哈·哈。\x01",
            "别说如此无情的话嘛。\x02\x03",
            "旅行要结伴才会愉快的，\x01",
            "而且我也可以帮忙找人嘛。\x02\x03",
            "#030F还是说……\x01",
            "……我妨碍到你们两个了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580F什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#031F哎呀哎呀。\x01",
            "真是天真啊。\x02\x03",
            "刚刚意识到自己心中爱情花蕾的存在，\x01",
            "却又害怕它绽放的少女……\x02\x03",
            "#037F……嘻嘻，感觉不错啊，\x01",
            "让我都有一些春心萌动了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#503F…………呜………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F？？？\x02\x03",
            "你说的是什么意思啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#031F嘻嘻，那就是……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)
    SetChrChipByIndex(0x101, 1)

    ChrTalk(
        0x101,
        "#08A#005F#3S嘿呀！\x05\x02",
    )

    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)

    def lambda_81B6():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81B6)
    OP_22(0x1F4, 0x0, 0x64)
    OP_99(0x101, 0x0, 0x7, 0x9C4)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    OP_22(0x7D, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 2)

    ChrTalk(
        0x8,
        "#038F啊～～……！#10A\x05\x02",
    )


    def lambda_8226():
        OP_8F(0xFE, 0x3DD6, 0x2E4, 0x2116, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8226)
    OP_99(0x101, 0x7, 0xC, 0x9C4)
    Sleep(300)
    OP_22(0x97, 0x0, 0x64)
    Sleep(700)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)

    NpcTalk(
        0x8,
        "青年的声音",
        "哇哇，怎么了！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "女性的声音",
        "这位客人，请振作一点！\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "老人的声音",
        (
            "不行了……\x01",
            "已经翻白眼了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018F艾丝蒂尔……\x02\x03",
            "不知道你在生什么气，\x01",
            "不过这么做好像也太过分了……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_44(0x101, 0xFF)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x8, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#509F……我已经避开了要害，\x01",
            "只是把他打飞而已。\x02\x03",
            "不会受很重的伤的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嘻嘻嘻……\x01",
            "艾丝蒂尔君……真害羞啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#019F……看起来的确是没什么事呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8504")

    ChrTalk(
        0x101,
        (
            "#582F好啦，接着去找人吧。\x02\x03",
            "别磨磨蹭蹭的了，\x01",
            "赶快去大使馆看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8578")

    label("loc_8504")


    ChrTalk(
        0x101,
        (
            "#582F好啦，接着去找人吧。\x02\x03",
            "别磨磨蹭蹭的了，\x01",
            "赶快去周游道看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8578")


    ChrTalk(
        0x102,
        (
            "#017F（……为什么\x01",
            "　要把气撒在我身上？）\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_49_7E18 end

    def Function_50_85A9(): pass

    label("Function_50_85A9")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8620")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，还不知道\x01",
            "金先生到底去了哪里呢。\x02\x03",
            "我们去东街区的\x01",
            "卡尔瓦德大使馆问问吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8713")

    label("loc_8620")

    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，对了……\x02\x03",
            "不是说金大哥\x01",
            "时常在酒廊喝酒吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F啊，艾南先生\x01",
            "确实这么说过。\x02\x03",
            "为了慎重起见，去周游道之前\x01",
            "先到酒廊看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8713")

    Call(0, 72)
    Return()

    # Function_50_85A9 end

    def Function_51_8718(): pass

    label("Function_51_8718")

    EventBegin(0x0)
    OP_6D(16020, 250, 7280, 0)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, 15830, 740, 8470, 0)
    SetChrPos(0x102, 15830, 740, 8470, 0)
    OP_0D()
    OP_70(0x10, 0x3C)
    OP_73(0x10)

    def lambda_8761():
        OP_8E(0xFE, 0x3B7E, 0xFA, 0xF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8761)
    Sleep(400)

    def lambda_8781():
        OP_8E(0xFE, 0x4060, 0xFA, 0xE6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8781)
    OP_6D(16100, 250, 4400, 2000)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x102, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#000F呼～……\x01",
            "肚子已经鼓鼓的了。\x02\x03",
            "那两个人，都已经吃了那么多，\x01",
            "还在不停地狼吞虎咽……\x02\x03",
            "他们还真是合得来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F金先生是那样的体格，\x01",
            "奥利维尔先生又很能吃嘛。\x02\x03",
            "只要不影响到明天的比赛\x01",
            "就没什么关系啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，确实他们两个\x01",
            "都不用让人担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，\x01",
            "我们也该去北街区的旅馆了吧？\x02\x03",
            "艾南先生一定\x01",
            "已经给我们订好房间了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_51_8718 end

    def Function_52_89C7(): pass

    label("Function_52_89C7")

    EventBegin(0x0)
    SetChrPos(0x101, 8940, 250, -12710, 270)
    SetChrPos(0x102, 8980, 250, -13870, 270)
    SetChrPos(0x9, 1930, 0, -4430, 0)
    SetChrPos(0xA, 1040, 0, -5320, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_6D(9320, 440, -13270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    ChrTalk(
        0x101,
        (
            "#000F哇……\x01",
            "已经这么晚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们还是\x01",
            "赶快回旅馆去比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "喂，那边的人！\x02",
    )

    CloseMessageWindow()

    def lambda_8ABD():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8ABD)

    def lambda_8ACB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8ACB)

    def lambda_8AD9():
        OP_8E(0xFE, 0x1B76, 0xFA, 0xFFFFD724, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8AD9)
    Sleep(300)

    def lambda_8AF9():
        OP_8E(0xFE, 0x1720, 0x0, 0xFFFFD314, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8AF9)
    OP_6D(7460, 250, -12150, 3000)

    ChrTalk(
        0x101,
        (
            "#000F哎……\x01",
            "士兵先生，怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "我们是巡逻人员。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "作为恐怖活动的对策之一\x01",
            "从今天开始，夜间的巡视\x01",
            "要进行强化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "因此，晚上９点之后请尽量\x01",
            "控制行动，不要外出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你们也赶快回家吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F晚上９点……\x01",
            "是不是早了点呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这是上面的决定。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "虽然很抱歉，还是请你们服从命令。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "对了……\x01",
            "你们住在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们住在北街区的\x01",
            "罗恩鲍姆酒店。\x02\x03",
            "在武术大会期间\x01",
            "都会住在那里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "武术大会期间……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "等一下，你们的脸\x01",
            "好像在哪里见过的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "啊啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这两个孩子，不是进入\x01",
            "武术大会决赛的选手吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你这样一说，还真是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，士兵先生，\x01",
            "你们也去看比赛了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "哈哈，是借着做警卫的时候呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "特别是今天白热化的比赛\x01",
            "让我感到很兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "明天就是决赛了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们送你们回旅馆，\x01",
            "好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎，这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F明白了。\x01",
            "谢谢你们的好意。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_52_89C7 end

    def Function_53_8F96(): pass

    label("Function_53_8F96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91FB")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FC9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_8FC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FEF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_8FEF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9015")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_9015")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_903C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_903C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9062")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_9062")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9088")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_9088")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90AD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_90AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90D2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_90D2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_90E6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91F8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    OP_69(0xFE, 0x3E8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91E9")

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

    label("loc_91E9")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_91F8")

    Jump("Function_53_8F96")

    label("loc_91FB")

    Return()

    # Function_53_8F96 end

    def Function_54_91FC(): pass

    label("Function_54_91FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9269")
    SetChrPos(0xFE, -29750, 250, -16079, 270)
    OP_8E(0xFE, 0xFFFFE0B6, 0xFA, 0xFFFFC131, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE0B6, 0xFA, 0x2EEA, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE0B6, 0xFA, 0xFFFFC131, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF8BCA, 0xFA, 0xFFFFC131, 0xBB8, 0x0)
    Jump("Function_54_91FC")

    label("loc_9269")

    Return()

    # Function_54_91FC end

    def Function_55_926A(): pass

    label("Function_55_926A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92D7")
    SetChrPos(0xFE, -29910, 250, -23870, 270)
    OP_8E(0xFE, 0xFFFFDF08, 0xFA, 0xFFFFA2C2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDE2C, 0xFA, 0xFFFF7D88, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDF08, 0xFA, 0xFFFFA2C2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF8B2A, 0xFA, 0xFFFFA2C2, 0xBB8, 0x0)
    Jump("Function_55_926A")

    label("loc_92D7")

    Return()

    # Function_55_926A end

    def Function_56_92D8(): pass

    label("Function_56_92D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_931D")
    SetChrPos(0xFE, -6720, 0, -19860, 270)
    OP_8E(0xFE, 0xFFFF8620, 0x0, 0xFFFFB26C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE5C0, 0x0, 0xFFFFB26C, 0xBB8, 0x0)
    Jump("Function_56_92D8")

    label("loc_931D")

    Return()

    # Function_56_92D8 end

    def Function_57_931E(): pass

    label("Function_57_931E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9363")
    SetChrPos(0xFE, 3810, 0, 10100, 180)
    OP_8E(0xFE, 0xEE2, 0x0, 0xFFFF7518, 0xBB8, 0x0)
    OP_8E(0xFE, 0xEE2, 0x0, 0x2774, 0xBB8, 0x0)
    Jump("Function_57_931E")

    label("loc_9363")

    Return()

    # Function_57_931E end

    def Function_58_9364(): pass

    label("Function_58_9364")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93A9")
    SetChrPos(0xFE, -3690, 0, -34890, 180)
    OP_8E(0xFE, 0xFFFFF196, 0x0, 0x25DA, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF196, 0x0, 0xFFFF77B6, 0xBB8, 0x0)
    Jump("Function_58_9364")

    label("loc_93A9")

    Return()

    # Function_58_9364 end

    def Function_59_93AA(): pass

    label("Function_59_93AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9417")
    SetChrPos(0xFE, -1740, 0, -6830, 180)
    OP_8E(0xFE, 0xFFFFF934, 0x0, 0xFFFFAF1A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7F8, 0x0, 0xFFFFAE66, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7F8, 0x0, 0xFFFFE4B2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF934, 0x0, 0xFFFFE552, 0xBB8, 0x0)
    Jump("Function_59_93AA")

    label("loc_9417")

    Return()

    # Function_59_93AA end

    def Function_60_9418(): pass

    label("Function_60_9418")

    EventBegin(0x0)
    RemoveParty(0x0, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x3, 0xFF)
    AddParty(0x7, 0xFF)
    SetChrPos(0x1C, -4970, 0, -57100, 270)
    OP_4A(0x1C, 255)
    OP_6D(-220, 250, -32150, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(21000, 0)
    OP_6E(262, 0)
    SetChrPos(0x104, -870, 0, -62440, 0)
    SetChrPos(0x102, -80, 0, -61370, 0)
    SetChrPos(0x108, 630, 0, -62400, 0)
    FadeToBright(2000, 0)
    OP_6D(170, 0, -59880, 7000)
    Fade(1000)
    OP_6D(-80, 0, -62140, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#012F……不是一般的士兵在巡逻了，\x01",
            "全部都已经换成特务兵了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F离宫被攻陷之后，\x01",
            "敌人也开始豁出来了。\x02\x03",
            "不过这种气氛感觉还是太夸张了一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#5P很好，此刻我就用鲁特琴来\x01",
            "缓和一下这里的紧张气氛吧……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_963A():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_963A)
    TurnDirection(0x102, 0x104, 400)

    ChrTalk(
        0x102,
        (
            "#017F如果你做了那么引人注目的事情，\x01",
            "那个人一定又会飞奔而来的。\x02\x03",
            "#010F我记得他是叫穆拉对吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x104, 0x102, 400)

    ChrTalk(
        0x104,
        (
            "#036F#5P是、是啊……\x02\x03",
            "你们两个千万不要接近帝国大使馆啊！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈哈，我们才没有那份闲心\x01",
            "跑去大使馆那里呢。\x02\x03",
            "准备完毕之后就进地下水路里去吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0x1C, 255)
    Return()

    # Function_60_9418 end

    def Function_61_9821(): pass

    label("Function_61_9821")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x11, 29)
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x11, -4100, 0, -48960, 0)
    SetChrPos(0x13, -4010, 0, -39700, 0)
    SetChrPos(0x14, -2770, 0, -39710, 0)
    SetChrPos(0x15, -4520, 0, -30260, 0)
    SetChrPos(0x16, -18010, 250, -16550, 0)
    SetChrPos(0x17, -1760, 0, -25440, 0)
    SetChrPos(0x18, -4560, 0, -18230, 0)
    SetChrPos(0x1C, -8670, 250, -15130, 0)
    SetChrPos(0x1D, -7730, 250, -16070, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x1E, -4930, 0, -48010, 0)
    SetChrPos(0x26, 8840, 250, -36590, 0)
    SetChrPos(0x27, 7970, 250, -30700, 0)
    SetChrPos(0x28, 8039, 250, -34920, 0)
    SetChrPos(0x29, 5020, 0, -32530, 0)
    SetChrPos(0x2C, 17670, 0, 1260, 270)
    SetChrPos(0x2D, 17680, 0, -70, 270)
    SetChrPos(0x2E, 1540, 0, -21430, 0)
    SetChrPos(0x2A, 2700, 0, -20310, 0)
    SetChrPos(0x2B, 1640, 0, -19200, 0)
    SetChrPos(0x12, 8390, 0, -38030, 0)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-1140, 0, -63570, 0)
    OP_67(0, 7480, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(0, 0)
    OP_6E(580, 0)

    def lambda_9BEF():
        OP_6D(50, 0, 5920, 14000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9BEF)

    def lambda_9C07():
        OP_6C(320000, 16000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9C07)

    def lambda_9C17():
        OP_67(0, 14750, -10000, 16000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_9C17)

    def lambda_9C2F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_9C2F)
    Sleep(20)

    def lambda_9C4F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_9C4F)
    Sleep(20)

    def lambda_9C6F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_9C6F)
    Sleep(20)

    def lambda_9C8F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_9C8F)
    Sleep(20)

    def lambda_9CAF():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x8FC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_9CAF)
    Sleep(20)
    Sleep(20)

    def lambda_9CD4():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_9CD4)
    Sleep(20)

    def lambda_9CF4():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0xB54, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_9CF4)
    Sleep(20)

    def lambda_9D14():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_9D14)
    Sleep(20)

    def lambda_9D34():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_9D34)

    def lambda_9D4F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_9D4F)
    Sleep(20)

    def lambda_9D6F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_9D6F)
    Sleep(20)

    def lambda_9D8F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_9D8F)
    Sleep(20)

    def lambda_9DAF():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 0, lambda_9DAF)
    Sleep(20)

    def lambda_9DCF():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_9DCF)
    Sleep(20)

    def lambda_9DEF():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_9DEF)
    Sleep(20)

    def lambda_9E0F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_9E0F)
    Sleep(20)

    def lambda_9E2F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_9E2F)
    Sleep(1000)

    def lambda_9E4F():
        OP_8E(0xFE, 0xFFFFE296, 0xFA, 0xFFFFC05E, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_9E4F)
    Sleep(1700)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x1B, 4090, 0, -66400, 0)
    SetChrPos(0x19, 4090, 0, -68100, 0)
    SetChrPos(0x1A, 4090, 0, -69800, 0)
    OP_43(0x1B, 0x0, 0x0, 0x3E)
    Sleep(100)
    OP_43(0x19, 0x0, 0x0, 0x3E)
    Sleep(100)
    OP_43(0x1A, 0x0, 0x0, 0x3E)
    Sleep(20)

    def lambda_9EE4():
        OP_8E(0xFE, 0x1702, 0x0, 0x604, 0x546, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_9EE4)

    def lambda_9EFF():
        OP_8E(0xFE, 0x155E, 0x0, 0x19A, 0x53C, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_9EFF)
    Sleep(7000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_61_9821 end

    def Function_62_9F36(): pass

    label("Function_62_9F36")

    OP_8E(0xFE, 0x1324, 0x0, 0xFFFF5B64, 0x2710, 0x0)
    OP_8E(0xFE, 0x8DE, 0x0, 0xFFFFA45C, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_97(0xFE, 0x0, 0xFFFFA45C, 0xFFFEA070, 0x24B8, 0x1)
    OP_97(0xFE, 0x0, 0xFFFFB910, 0x15F90, 0x24B8, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFF66E, 0x0, 0xFFFFE070, 0x2710, 0x0)
    OP_8E(0xFE, 0x30C, 0x0, 0xFFFFED68, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x2)

    def lambda_9FC5():
        OP_99(0xFE, 0x0, 0x7, 0x708)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9FC5)
    OP_96(0xFE, 0xFF0, 0x0, 0xFFFFF29A, 0x9C4, 0x7D0)
    ClearChrFlags(0xFE, 0x2)
    OP_8E(0xFE, 0x1630, 0x0, 0x82E6, 0x2710, 0x0)
    Return()

    # Function_62_9F36 end

    def Function_63_A000(): pass

    label("Function_63_A000")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0BF")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010F还是先去协会支部打声招呼吧。\x01",
            "　\x02\x03",
            "要先办理转属手续……\x01",
            "而且还有博士的委托。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A150")

    label("loc_A0BF")


    ChrTalk(
        0x102,
        (
            "#010F还是先去协会支部打声招呼吧。\x01",
            "　\x02\x03",
            "要先办理转属手续……\x01",
            "而且还有博士的委托。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A150")

    Call(0, 72)
    Return()

    # Function_63_A000 end

    def Function_64_A155(): pass

    label("Function_64_A155")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A201")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010F赶快回协会报告吧。\x02\x03",
            "再磨磨蹭蹭的天就要黑了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006F嗯，现在就去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A271")

    label("loc_A201")


    ChrTalk(
        0x102,
        (
            "#010F赶快回协会报告吧。\x02\x03",
            "再磨磨蹭蹭的天就要黑了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A271")

    Call(0, 72)
    Return()

    # Function_64_A155 end

    def Function_65_A276(): pass

    label("Function_65_A276")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A338")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010F已经很晚了，\x01",
            "我们回酒店去吧。\x02\x03",
            "该休息的时候就是要好好休息。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F酒店在北街区对吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A3A2")

    label("loc_A338")


    ChrTalk(
        0x102,
        (
            "#010F已经很晚了，\x01",
            "我们回酒店去吧。\x02\x03",
            "明天还有比赛，\x01",
            "我们最好早点休息。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3A2")

    Call(0, 72)
    Return()

    # Function_65_A276 end

    def Function_66_A3A7(): pass

    label("Function_66_A3A7")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4DA")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A446")

    ChrTalk(
        0x102,
        (
            "#010F我想奈尔先生正在等我们吧。\x01",
            "　\x02\x03",
            "去西街区的通讯社看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A4D7")

    label("loc_A446")


    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，那边是城门哦。\x02\x03",
            "奈尔先生的通讯社应该在西街区吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F哦～呵呵，知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_A4D7")

    Jump("loc_A551")

    label("loc_A4DA")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F我想奈尔先生正在等我们吧。\x01",
            "　\x02\x03",
            "去西街区的通讯社看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A551")

    Call(0, 72)
    Return()

    # Function_66_A3A7 end

    def Function_67_A556(): pass

    label("Function_67_A556")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A603")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010F总之我们先回协会报告吧。\x02\x03",
            "最好把奈尔的调查结果也告诉艾南先生。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006F嗯，现在就去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A674")

    label("loc_A603")


    ChrTalk(
        0x102,
        (
            "#010F总之我们先回协会报告吧。\x02\x03",
            "最好把奈尔的调查结果也告诉艾南先生。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A674")

    Call(0, 72)
    Return()

    # Function_67_A556 end

    def Function_68_A679(): pass

    label("Function_68_A679")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A724")

    ChrTalk(
        0x108,
        (
            "#070F呼，已经傍晚了。\x01",
            "我们尽量不要外出了。\x02\x03",
            "今天就别修行了，\x01",
            "赶快去城里参加晚宴吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7BF")

    label("loc_A724")

    TurnDirection(0x108, 0x0, 400)

    ChrTalk(
        0x108,
        (
            "#070F喂喂，\x01",
            "难道你们还打算外出吗？\x02\x03",
            "就算是再热衷于修炼，\x01",
            "现在还是快去参加晚宴吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7BF")

    Call(0, 72)
    Return()

    # Function_68_A679 end

    def Function_69_A7C4(): pass

    label("Function_69_A7C4")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A84B")

    ChrTalk(
        0x108,
        (
            "#070F现在没空去街道外面。\x02\x03",
            "做好准备后就向地下水路进发吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C8")

    label("loc_A84B")

    TurnDirection(0x108, 0x0, 400)

    ChrTalk(
        0x108,
        (
            "#070F现在没空去街道外面。\x02\x03",
            "做好准备后就向地下水路进发吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8C8")

    Call(0, 72)
    Return()

    # Function_69_A7C4 end

    def Function_70_A8CD(): pass

    label("Function_70_A8CD")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9F8")

    ChrTalk(
        0x101,
        "#501F啊，这边是城外……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F我说，\x01",
            "我们还是在城里再散散步吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，好啊。\x01",
            "还有很多地方没看呢。\x02\x03",
            "如果觉得累了，\x01",
            "就去东街区那个小公园休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，好吧⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_AADD")

    label("loc_A9F8")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F我说，\x01",
            "我们还是在城里再散散步吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，好啊。\x01",
            "还有很多地方没看呢。\x02\x03",
            "如果觉得累了，\x01",
            "就去东街区那个小公园休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，好吧⊙\x02",
    )

    CloseMessageWindow()

    label("loc_AADD")

    Call(0, 72)
    Return()

    # Function_70_A8CD end

    def Function_71_AAE2(): pass

    label("Function_71_AAE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABCC")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB80")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F艾丝蒂尔，\x01",
            "已经快到指定的时间了。\x02\x03",
            "我们赶快去大圣堂吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F嗯……明白！\x02",
    )

    CloseMessageWindow()
    Jump("loc_ABC8")

    label("loc_AB80")


    ChrTalk(
        0x102,
        (
            "#012F已经快到指定的时间了。\x01",
            "　\x02\x03",
            "我们赶快去大圣堂吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABC8")

    Call(0, 72)

    label("loc_ABCC")

    Return()

    # Function_71_AAE2 end

    def Function_72_ABCD(): pass

    label("Function_72_ABCD")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_72_ABCD end

    def Function_73_ABE9(): pass

    label("Function_73_ABE9")

    SetPlaceName(0xB9) # 阳光铃铛酒廊
    Return()

    # Function_73_ABE9 end

    def Function_74_ABED(): pass

    label("Function_74_ABED")

    SetPlaceName(0xB0) # 阳光铃铛酒廊
    Return()

    # Function_74_ABED end

    def Function_75_ABF1(): pass

    label("Function_75_ABF1")

    SetPlaceName(0xB2) # 阳光铃铛酒廊
    Return()

    # Function_75_ABF1 end

    def Function_76_ABF5(): pass

    label("Function_76_ABF5")

    SetPlaceName(0xAE) # 阳光铃铛酒廊
    Return()

    # Function_76_ABF5 end

    def Function_77_ABF9(): pass

    label("Function_77_ABF9")

    SetPlaceName(0xB3) # 阳光铃铛酒廊
    Return()

    # Function_77_ABF9 end

    SaveToFile()

Try(main)
