from ED6ScenarioHelper import *

def main():
    # 格兰赛尔大圣堂

    CreateScenaFile(
        FileName            = 'T4102   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4102.x',
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
        '奈尔',                                 # 9
        '士兵',                                 # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        '士兵',                                 # 14
        '士兵',                                 # 15
        '鸽子',                                 # 16
        '鸽子',                                 # 17
        '鸽子',                                 # 18
        '鸽子',                                 # 19
        '鸽子',                                 # 20
        '鸽子',                                 # 21
        '鸽子',                                 # 22
        '鸽子',                                 # 23
        '鸽子',                                 # 24
        '鸽子',                                 # 25
        '阿鲁姆',                               # 26
        '艾娅莉',                               # 27
        '达丽娅',                               # 28
        '菲利奥',                               # 29
        '拉科舒',                               # 30
        '士兵达登',                             # 31
        '比卡',                                 # 32
        '夏妮',                                 # 33
        '士兵',                                 # 34
        '士兵',                                 # 35
        '士兵',                                 # 36
        '特务兵',                               # 37
        '特务兵',                               # 38
        '莉安妮',                               # 39
        '游客',                                 # 40
        '游客',                                 # 41
        '游客',                                 # 42
        '游客',                                 # 43
        '游客',                                 # 44
        '游客',                                 # 45
        '游客',                                 # 46
        '游客',                                 # 47
        '游客',                                 # 48
        '鸽子',                                 # 49
        '鸽子',                                 # 50
        '鸽子',                                 # 51
        '鸽子',                                 # 52
        '鸽子',                                 # 53
        '鸽子',                                 # 54
        '鸽子',                                 # 55
        '王都格兰赛尔·北街区',                 # 56
        '王都格兰赛尔·南街区',                 # 57
    )

    DeclEntryPoint(
        Unknown_00              = -80000,
        Unknown_04              = 0,
        Unknown_08              = 0,
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH01730 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT07/CH01350 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01030 ._CH',             # 07
        'ED6_DT07/CH01640 ._CH',             # 08
        'ED6_DT07/CH01680 ._CH',             # 09
        'ED6_DT07/CH01690 ._CH',             # 0A
        'ED6_DT07/CH01610 ._CH',             # 0B
        'ED6_DT07/CH01480 ._CH',             # 0C
        'ED6_DT07/CH01143 ._CH',             # 0D
        'ED6_DT07/CH01023 ._CH',             # 0E
        'ED6_DT07/CH01003 ._CH',             # 0F
        'ED6_DT07/CH01220 ._CH',             # 10
        'ED6_DT07/CH01120 ._CH',             # 11
        'ED6_DT07/CH01200 ._CH',             # 12
        'ED6_DT07/CH01180 ._CH',             # 13
        'ED6_DT07/CH01050 ._CH',             # 14
        'ED6_DT07/CH01070 ._CH',             # 15
        'ED6_DT07/CH01730 ._CH',             # 16
        'ED6_DT07/CH01731 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH01730P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT07/CH01350P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01030P._CP',             # 07
        'ED6_DT07/CH01640P._CP',             # 08
        'ED6_DT07/CH01680P._CP',             # 09
        'ED6_DT07/CH01690P._CP',             # 0A
        'ED6_DT07/CH01610P._CP',             # 0B
        'ED6_DT07/CH01480P._CP',             # 0C
        'ED6_DT07/CH01143P._CP',             # 0D
        'ED6_DT07/CH01023P._CP',             # 0E
        'ED6_DT07/CH01003P._CP',             # 0F
        'ED6_DT07/CH01220P._CP',             # 10
        'ED6_DT07/CH01120P._CP',             # 11
        'ED6_DT07/CH01200P._CP',             # 12
        'ED6_DT07/CH01180P._CP',             # 13
        'ED6_DT07/CH01050P._CP',             # 14
        'ED6_DT07/CH01070P._CP',             # 15
        'ED6_DT07/CH01730P._CP',             # 16
        'ED6_DT07/CH01731P._CP',             # 17
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
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 36,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 37,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 38,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 39,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 40,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 41,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
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
        TalkScenaIndex      = 21,
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
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -55940,
        Z                   = 250,
        Y                   = 30,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -58170,
        Z                   = -3500,
        Y                   = -16100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -59550,
        Z                   = -3500,
        Y                   = -16100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -88950,
        Z                   = 0,
        Y                   = -3950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -78290,
        Z                   = 0,
        Y                   = -2530,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -40940,
        Z                   = 0,
        Y                   = -5120,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -55400,
        Z                   = 0,
        Y                   = -3050,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -78990,
        Z                   = 1250,
        Y                   = 8029,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -62950,
        Z                   = -3750,
        Y                   = -31290,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -55890,
        Z                   = 0,
        Y                   = -1830,
        Direction           = 185,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -78990,
        Z                   = 1250,
        Y                   = 8029,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -55990,
        Z                   = 250,
        Y                   = -1280,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -58060,
        Z                   = -3250,
        Y                   = -23920,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -60050,
        Z                   = -3250,
        Y                   = -24510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -58590,
        Z                   = -3250,
        Y                   = -22150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -55610,
        Z                   = -3750,
        Y                   = -27100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -60830,
        Z                   = -3500,
        Y                   = -28840,
        Direction           = 204,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -61010,
        Z                   = 250,
        Y                   = -870,
        Direction           = 189,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = -82230,
        Z                   = 250,
        Y                   = 4330,
        Direction           = 41,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -79740,
        Z                   = 250,
        Y                   = 4870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = -78570,
        Z                   = 250,
        Y                   = 4270,
        Direction           = 4,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -39960,
        Z                   = 0,
        Y                   = 43920,
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
        X                   = -7520,
        Z                   = 300,
        Y                   = -20000,
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
        X                   = -82190,
        Y                   = 0,
        Z                   = 123740,
        Range               = -75710,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x292C,
        Unknown_18          = 0x0,
        Unknown_1C          = 42,
    )

    DeclEvent(
        X                   = -63040,
        Y                   = -3750,
        Z                   = -33480,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 48,
    )

    DeclEvent(
        X                   = -63390,
        Y                   = -3750,
        Z                   = -24940,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 49,
    )

    DeclEvent(
        X                   = -78840,
        Y                   = 1250,
        Z                   = 12430,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 50,
    )


    DeclActor(
        TriggerX            = -76990,
        TriggerZ            = -3500,
        TriggerY            = -30450,
        TriggerRange        = 800,
        ActorX              = -76990,
        ActorZ              = -2500,
        ActorY              = -30450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -92000,
        TriggerZ            = 800,
        TriggerY            = -4000,
        TriggerRange        = 800,
        ActorX              = -92000,
        ActorZ              = 1800,
        ActorY              = -4000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -72220,
        TriggerZ            = -3180,
        TriggerY            = -15630,
        TriggerRange        = 800,
        ActorX              = -72220,
        ActorZ              = -2000,
        ActorY              = -15630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 47,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_876",          # 00, 0
        "Function_1_A1B",          # 01, 1
        "Function_2_B97",          # 02, 2
        "Function_3_D14",          # 03, 3
        "Function_4_D99",          # 04, 4
        "Function_5_E26",          # 05, 5
        "Function_6_EB7",          # 06, 6
        "Function_7_EDB",          # 07, 7
        "Function_8_F38",          # 08, 8
        "Function_9_F5C",          # 09, 9
        "Function_10_115F",        # 0A, 10
        "Function_11_141E",        # 0B, 11
        "Function_12_18D0",        # 0C, 12
        "Function_13_1BB2",        # 0D, 13
        "Function_14_1CAC",        # 0E, 14
        "Function_15_1DD2",        # 0F, 15
        "Function_16_241B",        # 10, 16
        "Function_17_2DD1",        # 11, 17
        "Function_18_3754",        # 12, 18
        "Function_19_37D3",        # 13, 19
        "Function_20_382D",        # 14, 20
        "Function_21_3856",        # 15, 21
        "Function_22_3A3B",        # 16, 22
        "Function_23_3C71",        # 17, 23
        "Function_24_3D03",        # 18, 24
        "Function_25_3D34",        # 19, 25
        "Function_26_3D68",        # 1A, 26
        "Function_27_3DAE",        # 1B, 27
        "Function_28_3E29",        # 1C, 28
        "Function_29_3E8B",        # 1D, 29
        "Function_30_3ED1",        # 1E, 30
        "Function_31_3F43",        # 1F, 31
        "Function_32_3F6F",        # 20, 32
        "Function_33_3F9B",        # 21, 33
        "Function_34_4558",        # 22, 34
        "Function_35_47A2",        # 23, 35
        "Function_36_49F2",        # 24, 36
        "Function_37_4A38",        # 25, 37
        "Function_38_4A7E",        # 26, 38
        "Function_39_4AEC",        # 27, 39
        "Function_40_4B5A",        # 28, 40
        "Function_41_4BC8",        # 29, 41
        "Function_42_4C36",        # 2A, 42
        "Function_43_4DBA",        # 2B, 43
        "Function_44_504F",        # 2C, 44
        "Function_45_5073",        # 2D, 45
        "Function_46_51C3",        # 2E, 46
        "Function_47_5241",        # 2F, 47
        "Function_48_52A3",        # 30, 48
        "Function_49_52A7",        # 31, 49
        "Function_50_52AB",        # 32, 50
    )


    def Function_0_876(): pass

    label("Function_0_876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_884")
    OP_A3(0x3FA)
    Event(0, 33)

    label("loc_884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_8A0")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 43)

    label("loc_8A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8FF")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x10)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x10)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x10)
    Jump("loc_A08")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_913")
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    Jump("loc_A08")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_92C")
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_A08")

    label("loc_92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_94A")
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_A08")

    label("loc_94A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_963")
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x26, 0x80)
    Jump("loc_A08")

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9A8")
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -85310, 0, -4390, 270)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -84980, 0, -3470, 270)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_A08")

    label("loc_9A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9E3")
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -79040, 500, 6080, 0)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -79040, 1250, 7750, 180)
    Jump("loc_A08")

    label("loc_9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9ED")
    Jump("loc_A08")

    label("loc_9ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_9F7")
    Jump("loc_A08")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A01")
    Jump("loc_A08")

    label("loc_A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A08")

    label("loc_A08")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_A14"),
        (SWITCH_DEFAULT, "loc_A1A"),
    )


    label("loc_A14")

    OP_A2(0x622)
    Jump("loc_A1A")

    label("loc_A1A")

    Return()

    # Function_0_876 end

    def Function_1_A1B(): pass

    label("Function_1_A1B")

    OP_16(0x2, 0xFA0, 0xFFFD2D58, 0xFFFE0048, 0x3005D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A60")
    OP_B1("t4102_y")
    Jump("loc_A69")

    label("loc_A60")

    OP_B1("t4102_n")

    label("loc_A69")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A82")
    OP_72(0xA, 0x10)
    OP_65(0x0, 0x1)

    label("loc_A82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A95")
    OP_1B(0x3, 0x0, 0x2D)

    label("loc_A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ADA")
    OP_72(0xE, 0x8)
    OP_72(0xE, 0x20)
    OP_72(0xE, 0x2)
    OP_6F(0xE, 0)
    OP_72(0xB, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x7, 0x10)
    OP_72(0xD, 0x10)
    OP_72(0x5, 0x10)
    OP_72(0x9, 0x10)
    OP_72(0xA, 0x10)

    label("loc_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B38")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_43(0x9, 0x1, 0x0, 0x23)
    OP_43(0xA, 0x1, 0x0, 0x23)
    OP_43(0xB, 0x1, 0x0, 0x23)
    OP_43(0xC, 0x1, 0x0, 0x23)
    OP_43(0xD, 0x1, 0x0, 0x23)
    OP_43(0xE, 0x1, 0x0, 0x23)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_B96")
    OP_72(0x10, 0x4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "map\\\\mp016_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -63240, -3240, -25080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_B96")

    Return()

    # Function_1_A1B end

    def Function_2_B97(): pass

    label("Function_2_B97")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBC")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_CFE")

    label("loc_BBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD5")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_CFE")

    label("loc_BD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEE")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_CFE")

    label("loc_BEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C07")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_CFE")

    label("loc_C07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C20")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_CFE")

    label("loc_C20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C39")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_CFE")

    label("loc_C39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C52")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_CFE")

    label("loc_C52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_CFE")

    label("loc_C6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C84")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_CFE")

    label("loc_C84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9D")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_CFE")

    label("loc_C9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB6")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_CFE")

    label("loc_CB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_CFE")

    label("loc_CCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE8")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_CFE")

    label("loc_CE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFE")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_CFE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D13")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_CFE")

    label("loc_D13")

    Return()

    # Function_2_B97 end

    def Function_3_D14(): pass

    label("Function_3_D14")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D98")
    OP_8E(0xFE, 0xFFFF63CA, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF291E, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF259A, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    Jump("Function_3_D14")

    label("loc_D98")

    Return()

    # Function_3_D14 end

    def Function_4_D99(): pass

    label("Function_4_D99")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E25")
    OP_8E(0xFE, 0xFFFED716, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFEC014, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    Jump("Function_4_D99")

    label("loc_E25")

    Return()

    # Function_4_D99 end

    def Function_5_E26(): pass

    label("Function_5_E26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EB6")
    OP_8E(0xFE, 0xFFFF1FB4, 0xFFFFF15A, 0xFFFF85C6, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFEF5F2, 0xFFFFF15A, 0xFFFF85C6, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF09F2, 0xFFFFF15A, 0xFFFF85C6, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_5_E26")

    label("loc_EB6")

    Return()

    # Function_5_E26 end

    def Function_6_EB7(): pass

    label("Function_6_EB7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EDA")
    OP_8D(0xFE, -83110, 1920, -74690, -5430, 3000)
    Jump("Function_6_EB7")

    label("loc_EDA")

    Return()

    # Function_6_EB7 end

    def Function_7_EDB(): pass

    label("Function_7_EDB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F37")
    OP_8E(0xFE, 0xFFFF6014, 0x0, 0xFFFF711C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF2C52, 0xFFFFF15A, 0xFFFF727A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF2C0C, 0x0, 0xFFFFEC82, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6014, 0x0, 0xFFFFEC00, 0x9C4, 0x0)
    Jump("Function_7_EDB")

    label("loc_F37")

    Return()

    # Function_7_EDB end

    def Function_8_F38(): pass

    label("Function_8_F38")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F5B")
    OP_8D(0xFE, -59380, 250, -52780, -3730, 3000)
    Jump("Function_8_F38")

    label("loc_F5B")

    Return()

    # Function_8_F38 end

    def Function_9_F5C(): pass

    label("Function_9_F5C")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, -74920, -1510, -82870, 5610, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_115E")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1127")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1017")

    def lambda_FFB():

        label("loc_FFB")

        OP_97(0xFE, 0xFFFECB7C, 0x3926, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_FFB")

    QueueWorkItem2(0xFE, 1, lambda_FFB)
    Jump("loc_1036")

    label("loc_1017")


    def lambda_101D():

        label("loc_101D")

        OP_97(0xFE, 0xFFFECB7C, 0x3926, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_101D")

    QueueWorkItem2(0xFE, 1, lambda_101D)

    label("loc_1036")

    SetChrChipByIndex(0xFE, 22)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_1045")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_107D")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1075")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_107D")

    label("loc_1075")

    Sleep(15)
    Jump("loc_1045")

    label("loc_107D")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -78690, 0, -40, 74)

    label("loc_109C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1124")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_111C")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 23)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -74920, -1510, -82870, 5610, 0)
    Jump("loc_1124")

    label("loc_111C")

    Sleep(500)
    Jump("loc_109C")

    label("loc_1124")

    Jump("loc_115B")

    label("loc_1127")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115B")

    def lambda_1143():
        OP_8D(0xFE, -74920, -1510, -82870, 5610, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1143)

    label("loc_115B")

    Jump("loc_F90")

    label("loc_115E")

    Return()

    # Function_9_F5C end

    def Function_10_115F(): pass

    label("Function_10_115F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_11EB")

    ChrTalk(
        0xFE,
        (
            "摩尔根将军的孙女\x01",
            "也被捉去做了人质呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那位理查德上校\x01",
            "原来是这么心狠手辣的人吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141A")

    label("loc_11EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_11F5")
    Jump("loc_141A")

    label("loc_11F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1276")

    ChrTalk(
        0xFE,
        (
            "这家人的女孩子\x01",
            "似乎一直未回家呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我已经向本部\x01",
            "报告了这个情况，\x01",
            "希望早日能找到她。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141A")

    label("loc_1276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1376")

    ChrTalk(
        0xFE,
        (
            "今天白天难得\x01",
            "获得了一次休息机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "多亏这样，\x01",
            "我的身体得到了充分休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，\x01",
            "为什么只让我休息呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这样很对不起其他人的呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_141A")

    label("loc_1376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1380")
    Jump("loc_141A")

    label("loc_1380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_13EB")

    ChrTalk(
        0xFE,
        (
            "据说摩尔根将军\x01",
            "为了对付恐怖分子，\x01",
            "忙得不可开交。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141A")

    label("loc_13EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_13F5")
    Jump("loc_141A")

    label("loc_13F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_13FF")
    Jump("loc_141A")

    label("loc_13FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1409")
    Jump("loc_141A")

    label("loc_1409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1413")
    Jump("loc_141A")

    label("loc_1413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_141A")

    label("loc_141A")

    TalkEnd(0xFE)
    Return()

    # Function_10_115F end

    def Function_11_141E(): pass

    label("Function_11_141E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1449")

    ChrTalk(
        0xFE,
        (
            "王都的戒备果然还是\x01",
            "由我们王都守卫队来做合适！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CC")

    label("loc_1449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1453")
    Jump("loc_18CC")

    label("loc_1453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_14F6")

    ChrTalk(
        0xFE,
        (
            "女王陛下的病况如何\x01",
            "连我们也不知道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎样，\x01",
            "还是像平常一样继续警戒吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CC")

    label("loc_14F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_173A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_15F8")

    ChrTalk(
        0xFE,
        (
            "就算发现亲卫队的人，\x01",
            "我也不想和他们战斗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来都是王国军的队伍，\x01",
            "而且我想我们也打不过他们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1737")

    label("loc_15F8")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "就算发现亲卫队的人，\x01",
            "我也不想和他们战斗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来都是王国军的队伍，\x01",
            "而且我想我们也打不过他们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们要是能投降\x01",
            "就帮了我们大忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1737")

    Jump("loc_18CC")

    label("loc_173A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_184E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_17AA")

    ChrTalk(
        0xFE,
        "嘿嘿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才，这里的一位修女\x01",
            "向我打招呼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_184B")

    label("loc_17AA")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "嘿嘿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才，这里的一位修女\x01",
            "向我打招呼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好的，为了王都的和平，\x01",
            "我也要好好努力！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184B")

    Jump("loc_18CC")

    label("loc_184E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_189D")

    ChrTalk(
        0xFE,
        (
            "上头命令\x01",
            "要定时巡逻重要的设施。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CC")

    label("loc_189D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_18A7")
    Jump("loc_18CC")

    label("loc_18A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_18B1")
    Jump("loc_18CC")

    label("loc_18B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_18BB")
    Jump("loc_18CC")

    label("loc_18BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_18C5")
    Jump("loc_18CC")

    label("loc_18C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_18CC")

    label("loc_18CC")

    TalkEnd(0xFE)
    Return()

    # Function_11_141E end

    def Function_12_18D0(): pass

    label("Function_12_18D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_19B2")

    ChrTalk(
        0xFE,
        (
            "情报部的残党\x01",
            "有可能会袭击这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这段时间还是要\x01",
            "继续加强戒备才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAE")

    label("loc_19B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_19BC")
    Jump("loc_1BAE")

    label("loc_19BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1A30")

    ChrTalk(
        0xFE,
        (
            "从刚才起这里的员工\x01",
            "就一直慌慌张张的，\x01",
            "发生什么事了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真让人担心……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BAE")

    label("loc_1A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1AAF")

    ChrTalk(
        0xFE,
        "已经傍晚了呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "马上就是换班时间了，\x01",
            "今晚我还要值班巡逻呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAE")

    label("loc_1AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1B0F")

    ChrTalk(
        0xFE,
        (
            "我叫刚才出来的女孩\x01",
            "帮我拍了一张照片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她对我说\x01",
            "『叔叔，你很可爱哦』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAE")

    label("loc_1B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1B7F")

    ChrTalk(
        0xFE,
        "来这里有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我正在监控这里的员工。\x01",
            "上头不知道出于什么原因\x01",
            "下达了这样的命令。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAE")

    label("loc_1B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1B89")
    Jump("loc_1BAE")

    label("loc_1B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B93")
    Jump("loc_1BAE")

    label("loc_1B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1B9D")
    Jump("loc_1BAE")

    label("loc_1B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1BA7")
    Jump("loc_1BAE")

    label("loc_1BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1BAE")

    label("loc_1BAE")

    TalkEnd(0xFE)
    Return()

    # Function_12_18D0 end

    def Function_13_1BB2(): pass

    label("Function_13_1BB2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1BBF")
    Jump("loc_1CA8")

    label("loc_1BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1C51")

    ChrTalk(
        0xFE,
        (
            "你们是……\x01",
            "好像是武术大会的优胜者吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可不要做出什么\x01",
            "可疑的行动哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA8")

    label("loc_1C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1C5B")
    Jump("loc_1CA8")

    label("loc_1C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1C65")
    Jump("loc_1CA8")

    label("loc_1C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1C6F")
    Jump("loc_1CA8")

    label("loc_1C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1C79")
    Jump("loc_1CA8")

    label("loc_1C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1C83")
    Jump("loc_1CA8")

    label("loc_1C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C8D")
    Jump("loc_1CA8")

    label("loc_1C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1C97")
    Jump("loc_1CA8")

    label("loc_1C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1CA1")
    Jump("loc_1CA8")

    label("loc_1CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1CA8")

    label("loc_1CA8")

    TalkEnd(0xFE)
    Return()

    # Function_13_1BB2 end

    def Function_14_1CAC(): pass

    label("Function_14_1CAC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1CB9")
    Jump("loc_1DCE")

    label("loc_1CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1D77")

    ChrTalk(
        0xFE,
        (
            "王城里有洛伦斯队长把守，\x01",
            "自然没问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "市街区这里\x01",
            "就交给我们吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCE")

    label("loc_1D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1D81")
    Jump("loc_1DCE")

    label("loc_1D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1D8B")
    Jump("loc_1DCE")

    label("loc_1D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1D95")
    Jump("loc_1DCE")

    label("loc_1D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1D9F")
    Jump("loc_1DCE")

    label("loc_1D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1DA9")
    Jump("loc_1DCE")

    label("loc_1DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1DB3")
    Jump("loc_1DCE")

    label("loc_1DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1DBD")
    Jump("loc_1DCE")

    label("loc_1DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1DC7")
    Jump("loc_1DCE")

    label("loc_1DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1DCE")

    label("loc_1DCE")

    TalkEnd(0xFE)
    Return()

    # Function_14_1CAC end

    def Function_15_1DD2(): pass

    label("Function_15_1DD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1E71")

    ChrTalk(
        0xFE,
        (
            "女王陛下和科洛蒂娅公主，\x01",
            "她们二位看起来都很有精神呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过没有见到\x01",
            "杜南公爵的身影啊，\x01",
            "这是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2417")

    label("loc_1E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1E97")

    ChrTalk(
        0xFE,
        "发、发生了什么事吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2417")

    label("loc_1E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1F50")

    ChrTalk(
        0xFE,
        (
            "诞辰庆典上至少\x01",
            "要见一见科洛蒂娅公主的\x01",
            "美妙英姿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她非常乖巧可爱哦。\x01",
            "我要是有这么一个女儿就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2417")

    label("loc_1F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1FFD")

    ChrTalk(
        0xFE,
        (
            "今年因为到处有士兵的缘故，\x01",
            "所以没有什么闹事的人出现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这样倒也不错……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2417")

    label("loc_1FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2089")

    ChrTalk(
        0xFE,
        (
            "每年大会的最后一天，\x01",
            "大街肯定会非常的热闹的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不知道今年会怎样呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2417")

    label("loc_2089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_20EB")

    ChrTalk(
        0xFE,
        "哎呀，已经傍晚了呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，年纪一大，\x01",
            "觉得一天过得都很快。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2417")

    label("loc_20EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2164")

    ChrTalk(
        0xFE,
        (
            "在武术大会进行的时候，\x01",
            "我就去百货商店看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比赛期间店里面比较清静，\x01",
            "感觉很舒畅呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2417")

    label("loc_2164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_21A6")

    ChrTalk(
        0xFE,
        (
            "必须快点\x01",
            "回家准备晚饭了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2417")

    label("loc_21A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_226F")

    ChrTalk(
        0xFE,
        (
            "今年武术大会的门票不打折，\x01",
            "这可怎么办好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "买不起门票，\x01",
            "这次就只有不去看了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2417")

    label("loc_226F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2394")

    ChrTalk(
        0xFE,
        (
            "女王陛下身体欠佳，\x01",
            "却要召开武术大会，\x01",
            "乐趣也会减半。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "主办人又是那个差劲的杜南公爵，\x01",
            "有种让人说不出来的滋味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "理查德上校还要当这种人的助手，\x01",
            "真是难为他了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2417")

    label("loc_2394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2417")

    ChrTalk(
        0xFE,
        (
            "听说有恐怖事件，\x01",
            "是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对我而言，\x01",
            "只要不导致物价上涨就万事大吉了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2417")

    TalkEnd(0xFE)
    Return()

    # Function_15_1DD2 end

    def Function_16_241B(): pass

    label("Function_16_241B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_246C")

    ChrTalk(
        0xFE,
        (
            "呼～诞辰庆典顺利举行了，\x01",
            "终于让我松了一口气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_246C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_252C")

    ChrTalk(
        0xFE,
        (
            "据说亲卫队的人\x01",
            "都藏在王都里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "恐怖事件的传闻难道是真的。\x01",
            "我最好还是去避难吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260F")

    label("loc_252C")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "啊呀呀，\x01",
            "我听那些士兵说了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说亲卫队的人\x01",
            "都藏在王都里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "恐怖事件的传闻难道是真的。\x01",
            "我最好还是去避难吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260F")

    Jump("loc_2DCD")

    label("loc_2612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_26AA")

    ChrTalk(
        0xFE,
        (
            "今天早上\x01",
            "我和一位大圣堂的\x01",
            "修女擦肩而过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么一大清早\x01",
            "究竟是去哪里呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_26AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2745")

    ChrTalk(
        0xFE,
        (
            "以往总有\x01",
            "通宵吵闹的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今年在这种情况下也不会再有了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_2745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2801")

    ChrTalk(
        0xFE,
        (
            "昨天晚上开始，\x01",
            "巡逻的士兵增加了不少啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难得武术大会能够搞得热热闹闹的，\x01",
            "结果什么店铺都要早早关门，\x01",
            "想提高营业额也不行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_2801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2878")

    ChrTalk(
        0xFE,
        "巡逻的士兵数量增加了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "总觉得世道不太平啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_2878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2934")

    ChrTalk(
        0xFE,
        (
            "王城、离宫、港口，\x01",
            "全都被封锁了，\x01",
            "总觉得心里憋得慌呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还是去看看武术大会吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_2934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2A00")

    ChrTalk(
        0xFE,
        (
            "这附近的大圣堂\x01",
            "也是个观光胜地呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在人们都\x01",
            "跑去看武术大会了，\x01",
            "平时这里要更热闹一些。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B02")

    label("loc_2A00")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "这附近的大圣堂\x01",
            "也是个观光胜地呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说那是王国中\x01",
            "所有七耀教会的建筑里\x01",
            "年代最久远的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在人们都\x01",
            "跑去看武术大会了，\x01",
            "平时这里要更热闹一些。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B02")

    Jump("loc_2DCD")

    label("loc_2B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2BAB")

    ChrTalk(
        0xFE,
        (
            "著名的利贝尔通讯社\x01",
            "就在这个街区。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在附近的咖啡厅里\x01",
            "时常可以看到记者们\x01",
            "在商讨工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_2BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2D57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2C71")

    ChrTalk(
        0xFE,
        (
            "因为摩尔根将军很忙，\x01",
            "所以很少看到他\x01",
            "回到在王都这里的家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "每年的诞辰庆典他都会回来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D54")

    label("loc_2C71")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "这个西街区的住宅很多，\x01",
            "那位摩尔根将军的家也在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为将军很忙，\x01",
            "所以很少看到他回家一趟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "每年的诞辰庆典他都会回来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D54")

    Jump("loc_2DCD")

    label("loc_2D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2DCD")

    ChrTalk(
        0xFE,
        (
            "刚才有几个戴手铐的家伙\x01",
            "被士兵押送过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看起来好像是\x01",
            "从封锁了的港口\x01",
            "那边过来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCD")

    TalkEnd(0xFE)
    Return()

    # Function_16_241B end

    def Function_17_2DD1(): pass

    label("Function_17_2DD1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2E5A")

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "竟然是这次政变的幕后黑手……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果早知道是这样，\x01",
            "我们就不会协助他了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3750")

    label("loc_2E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2F19")

    ChrTalk(
        0xFE,
        (
            "还没弄清楚是怎么回事，\x01",
            "王都守卫队就撤离了，\x01",
            "然后情报部的特务兵就来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王城那边究竟\x01",
            "发生了什么事呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3750")

    label("loc_2F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2FC9")

    ChrTalk(
        0xFE,
        (
            "有传闻说恐怖分子打着\x01",
            "游击士的名义到处逃亡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们在突破\x01",
            "蔡斯关所的盘查后，\x01",
            "目前行踪不明。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3750")

    label("loc_2FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3072")

    ChrTalk(
        0xFE,
        (
            "武术大会\x01",
            "已经平安结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大会上没有发生恐怖袭击\x01",
            "可真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3750")

    label("loc_3072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_312F")

    ChrTalk(
        0xFE,
        (
            "说起来，国境守备队那些兄弟\x01",
            "为了参加这次的武术大会，\x01",
            "也来了王都这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和摩尔根将军联络不上，\x01",
            "真是不知道该怎么办啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3213")

    label("loc_312F")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "说起来，国境守备队那些兄弟\x01",
            "为了参加这次的武术大会，\x01",
            "也来了王都这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和摩尔根将军联络不上，\x01",
            "真是不知道该怎么办啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道说帝国方面\x01",
            "有什么动静吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3213")

    Jump("loc_3750")

    label("loc_3216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_33CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_32C7")

    ChrTalk(
        0xFE,
        (
            "自从理查德上校\x01",
            "进入格兰赛尔城之后，\x01",
            "就再也没出现过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既然是为了对付恐怖分子，\x01",
            "不在艾尔贝离宫本部行吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33CA")

    label("loc_32C7")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "自从理查德上校\x01",
            "进入格兰赛尔城之后，\x01",
            "就再也没出现过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既然是为了对付恐怖分子，\x01",
            "不在艾尔贝离宫本部行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个公爵也不可靠，\x01",
            "所以只能相信女王陛下了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33CA")

    Jump("loc_3750")

    label("loc_33CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3474")

    ChrTalk(
        0xFE,
        (
            "听说特务部队是从\x01",
            "情报部里培养出来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之物色的成员\x01",
            "似乎都是很有本事的家伙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3750")

    label("loc_3474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_351F")

    ChrTalk(
        0xFE,
        (
            "提到拉赛尔博士，\x01",
            "他是那位发明导力器的\x01",
            "高人的徒弟吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "绑架了博士，\x01",
            "亲卫队到底意欲何为呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3750")

    label("loc_351F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_35D8")

    ChrTalk(
        0xFE,
        (
            "被通缉的犯人\x01",
            "全部都是亲卫队的成员……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既然正被通缉，\x01",
            "他们肯定就不会穿着亲卫队的队服\x01",
            "在街道上招摇过市了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3750")

    label("loc_35D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3709")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3645")

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "真是好酷啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "头脑又聪明，\x01",
            "武艺又精通，\x01",
            "不用说当然会有很高的人气了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3706")

    label("loc_3645")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "几天前\x01",
            "理查德上校到王城来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他是从雷斯顿要塞\x01",
            "到这个港口来的，\x01",
            "真是个好酷的人啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "头脑又聪明，\x01",
            "武艺又精通，\x01",
            "不用说当然会有很高的人气了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3706")

    Jump("loc_3750")

    label("loc_3709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3750")

    ChrTalk(
        0xFE,
        (
            "前面是港口，\x01",
            "出于防止恐怖活动的原因，\x01",
            "现在禁止入内。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3750")

    TalkEnd(0xFE)
    Return()

    # Function_17_2DD1 end

    def Function_18_3754(): pass

    label("Function_18_3754")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "为何那么有名的军人\x01",
            "会发动政变呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，幸好大街这边\x01",
            "没有被卷进事端里去啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3754 end

    def Function_19_37D3(): pass

    label("Function_19_37D3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "等大街安静下来之后，\x01",
            "一定要叫我老公\x01",
            "去找工作才行。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_37D3 end

    def Function_20_382D(): pass

    label("Function_20_382D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "莉安妮小姐～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你在哪儿啊？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_382D end

    def Function_21_3856(): pass

    label("Function_21_3856")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3863")
    Jump("loc_3A37")

    label("loc_3863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_386D")
    Jump("loc_3A37")

    label("loc_386D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3877")
    Jump("loc_3A37")

    label("loc_3877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3881")
    Jump("loc_3A37")

    label("loc_3881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_388B")
    Jump("loc_3A37")

    label("loc_388B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_38D2")

    ChrTalk(
        0xFE,
        "港口那边似乎不能去了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉，真遗憾……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A37")

    label("loc_38D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3A12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3947")

    ChrTalk(
        0xFE,
        (
            "以大圣堂为背景，\x01",
            "伫立在王都街道上的你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔～就像一幅画。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A0F")

    label("loc_3947")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "以大圣堂为背景，\x01",
            "伫立在王都街道上的你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～就像一幅画。\x01",
            "如果有一台导力相机该多好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "至少也要将这幅光景\x01",
            "深深地印在脑海中。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0F")

    Jump("loc_3A37")

    label("loc_3A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3A1C")
    Jump("loc_3A37")

    label("loc_3A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3A26")
    Jump("loc_3A37")

    label("loc_3A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3A30")
    Jump("loc_3A37")

    label("loc_3A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3A37")

    label("loc_3A37")

    TalkEnd(0xFE)
    Return()

    # Function_21_3856 end

    def Function_22_3A3B(): pass

    label("Function_22_3A3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3A48")
    Jump("loc_3C6D")

    label("loc_3A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3A52")
    Jump("loc_3C6D")

    label("loc_3A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3A5C")
    Jump("loc_3C6D")

    label("loc_3A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3A66")
    Jump("loc_3C6D")

    label("loc_3A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3A70")
    Jump("loc_3C6D")

    label("loc_3A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3ADC")

    ChrTalk(
        0xFE,
        (
            "格兰赛尔港的夜景\x01",
            "相当漂亮呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就连观光手册上\x01",
            "都有它的介绍。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C6D")

    label("loc_3ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3C48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3B89")

    ChrTalk(
        0xFE,
        (
            "所有这些\x01",
            "都是头一次见到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在洛连特约会地点都是一成不变的，\x01",
            "所以感觉这儿很新鲜呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C45")

    label("loc_3B89")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "所有这些\x01",
            "都是头一次见到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在洛连特约会地点都是一成不变的，\x01",
            "所以感觉这儿很新鲜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "旅行真不错啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3C45")

    Jump("loc_3C6D")

    label("loc_3C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3C52")
    Jump("loc_3C6D")

    label("loc_3C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3C5C")
    Jump("loc_3C6D")

    label("loc_3C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3C66")
    Jump("loc_3C6D")

    label("loc_3C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3C6D")

    label("loc_3C6D")

    TalkEnd(0xFE)
    Return()

    # Function_22_3A3B end

    def Function_23_3C71(): pass

    label("Function_23_3C71")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "今年爷爷都没有回来呢，\x01",
            "而且也没看到他在武术大会上出现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "太无聊了，所以我自己一个人出来玩。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_3C71 end

    def Function_24_3D03(): pass

    label("Function_24_3D03")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哇哇，五彩纸屑飘到杯子里来了！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_3D03 end

    def Function_25_3D34(): pass

    label("Function_25_3D34")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "恰好这里有空座位，\x01",
            "真不错啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_3D34 end

    def Function_26_3D68(): pass

    label("Function_26_3D68")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "王都的咖啡香浓得无可匹敌啊，\x01",
            "的确很高级。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_3D68 end

    def Function_27_3DAE(): pass

    label("Function_27_3DAE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "这家酒廊气氛很不错啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然还不是很累，\x01",
            "但也想进去休息一下呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_3DAE end

    def Function_28_3E29(): pass

    label("Function_28_3E29")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "呵呵，那就是有名的\x01",
            "利贝尔通讯社大楼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不知道能不能\x01",
            "去里面参观学习一下呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_3E29 end

    def Function_29_3E8B(): pass

    label("Function_29_3E8B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "不愧是格兰赛尔，\x01",
            "连住宅区也是那么优雅。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_3E8B end

    def Function_30_3ED1(): pass

    label("Function_30_3ED1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "你们今天\x01",
            "去教堂祈祷了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在女王的诞辰庆典日做礼拜\x01",
            "是一个很好的纪念呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_3ED1 end

    def Function_31_3F43(): pass

    label("Function_31_3F43")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "啊，这里就是格兰赛尔大圣堂啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_3F43 end

    def Function_32_3F6F(): pass

    label("Function_32_3F6F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "咦～这里就是\x01",
            "格兰赛尔大～圣～堂呀。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_3F6F end

    def Function_33_3F9B(): pass

    label("Function_33_3F9B")

    EventBegin(0x0)
    OP_6D(-63290, -3220, -25240, 0)
    OP_67(0, 12660, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(269000, 0)
    OP_6E(442, 0)

    def lambda_3FE0():
        OP_67(0, 9500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FE0)

    def lambda_3FF8():
        OP_6B(2800, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3FF8)

    def lambda_4008():
        OP_6C(315000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4008)

    def lambda_4018():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4018)
    SetChrPos(0x101, -61850, -3500, -25070, 270)
    SetChrPos(0x102, -62010, -3500, -26170, 270)
    SetChrPos(0x8, -63080, -3500, -25100, 270)
    ClearChrFlags(0x8, 0x80)
    Sleep(6000)

    ChrTalk(
        0x101,
        (
            "#000F哎～这家店的气氛真不错呢。\x02\x03",
            "与其说是酒馆，\x01",
            "不如称为咖啡店更好呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        "#010F这种香气，就是咖啡的味道吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    ChrTalk(
        0x8,
        (
            "#140F这可是老板\x01",
            "按照自己的兴趣布置的呢。\x02\x03",
            "用玻璃器具煮出来的咖啡，\x01",
            "不能不说是绝品呢。\x02\x03",
            "另外，用本地产的调料做的咖喱饭\x01",
            "也很值得推荐哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F咖喱……\x01",
            "吃起来应该很辣吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F虽然是有点辣，\x01",
            "不过就是这样才香呢。\x02\x03",
            "以前我吃过，\x01",
            "留下了很深的印象呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F咕嘟……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#140F呵呵，只要吃一次\x01",
            "就会上瘾的。\x02\x03",
            "不过，吃饭和喝咖啡的事\x01",
            "一会儿再说，我们先……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F等一下！\x02\x03",
            "我们比赛已经很累了，\x01",
            "肚子都快饿扁啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F就是这样，\x01",
            "我们能不能先吃晚饭呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#140F呼呼……\x01",
            "你们这些孩子真是不讨人喜欢啊。\x02\x03",
            "哼，算了，\x01",
            "你们想吃多少就吃多少吧！\x02\x03",
            "待会儿取材的时候，\x01",
            "可要给我把你们知道的通通说出来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F果然是为了这个来的啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，\x01",
            "朵洛希今天没有一起来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#140F嗯，\x01",
            "她去做别的工作去了……\x02\x03",
            "不说这个了，我们赶快进去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_33_3F9B end

    def Function_34_4558(): pass

    label("Function_34_4558")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x36D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45AF")
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
    Jump("loc_47A1")

    label("loc_45AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4739")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 2)), scpexpr(EXPR_END)), "loc_4687")

    ChrTalk(
        0x102,
        (
            "#010F今天已经很晚了，\x01",
            "就不要到地下水路去了。\x02\x03",
            "明天再和金大哥他们\x01",
            "一起进去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4733")

    label("loc_4687")


    ChrTalk(
        0x102,
        (
            "#010F看起来这里就是\x01",
            "『渡鸦帮』那些家伙说的\x01",
            "地下水路的入口。\x02\x03",
            "今天已经很晚了，\x01",
            "明天再和金大哥他们\x01",
            "一起进去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4733")

    TalkEnd(0xFF)
    Jump("loc_47A1")

    label("loc_4739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47A1")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x73, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "使用了\x07\x02",
            "地下水路的钥匙Ａ\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x622)
    OP_71(0xA, 0x10)
    OP_64(0x0, 0x1)
    TalkEnd(0xFF)

    label("loc_47A1")

    Return()

    # Function_34_4558 end

    def Function_35_47A2(): pass

    label("Function_35_47A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49F1")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47D5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48F2")

    label("loc_47D5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47FB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48F2")

    label("loc_47FB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4821")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48F2")

    label("loc_4821")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4848")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48F2")

    label("loc_4848")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_486E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48F2")

    label("loc_486E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4894")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48F2")

    label("loc_4894")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48B9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48F2")

    label("loc_48B9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48DE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48F2")

    label("loc_48DE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48F2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49EE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    OP_69(0xFE, 0x3E8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49DF")

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

    label("loc_49DF")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_49EE")

    Jump("Function_35_47A2")

    label("loc_49F1")

    Return()

    # Function_35_47A2 end

    def Function_36_49F2(): pass

    label("Function_36_49F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A37")
    SetChrPos(0xFE, -43700, 250, -8520, 0)
    OP_8E(0xFE, 0xFFFF554C, 0xFA, 0xFFFF7D1A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF554C, 0xFA, 0xFFFFDEB8, 0xBB8, 0x0)
    Jump("Function_36_49F2")

    label("loc_4A37")

    Return()

    # Function_36_49F2 end

    def Function_37_4A38(): pass

    label("Function_37_4A38")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A7D")
    SetChrPos(0xFE, -39120, 0, -7690, 180)
    OP_8E(0xFE, 0xFFFF6730, 0x0, 0xFFFF7E5A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF6730, 0x0, 0xFFFFE1F6, 0xBB8, 0x0)
    Jump("Function_37_4A38")

    label("loc_4A7D")

    Return()

    # Function_37_4A38 end

    def Function_38_4A7E(): pass

    label("Function_38_4A7E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AEB")
    SetChrPos(0xFE, -54990, -3750, -18870, 180)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFFB5C8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFFB64A, 0xBB8, 0x0)
    Jump("Function_38_4A7E")

    label("loc_4AEB")

    Return()

    # Function_38_4A7E end

    def Function_39_4AEC(): pass

    label("Function_39_4AEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B59")
    SetChrPos(0xFE, -74820, -3500, -19000, 180)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFFB64A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFFB5C8, 0xBB8, 0x0)
    Jump("Function_39_4AEC")

    label("loc_4B59")

    Return()

    # Function_39_4AEC end

    def Function_40_4B5A(): pass

    label("Function_40_4B5A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BC7")
    SetChrPos(0xFE, -74820, -3500, -30850, 180)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFFB5C8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFFB64A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFF877E, 0xBB8, 0x0)
    Jump("Function_40_4B5A")

    label("loc_4BC7")

    Return()

    # Function_40_4B5A end

    def Function_41_4BC8(): pass

    label("Function_41_4BC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C35")
    SetChrPos(0xFE, -54990, -3750, -30850, 180)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFFB5C8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFFB64A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFF877E, 0xBB8, 0x0)
    Jump("Function_41_4BC8")

    label("loc_4C35")

    Return()

    # Function_41_4BC8 end

    def Function_42_4C36(): pass

    label("Function_42_4C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DB9")
    OP_A2(0x62E)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -78280, 1760, 11580, 0)
    SetChrPos(0x102, -79290, 1760, 11770, 45)

    def lambda_4C74():
        OP_6C(350000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C74)
    OP_6D(-79030, 1760, 13490, 2000)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F（太好了，终于到了！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（不要丧失警惕，艾丝蒂尔……）\x02\x03",
            "（我先进去，\x01",
            "你跟在我后面。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（嗯、好的……！）\x02",
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xFFFECB04, 0x6E0, 0x30C0, 0x7D0, 0x0)
    OP_8C(0x102, 0, 400)
    OP_70(0xC, 0x3C)
    OP_73(0xC)

    def lambda_4D3D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4D3D)

    def lambda_4D4F():
        OP_8E(0xFE, 0xFFFECBB8, 0x6E0, 0x369C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4D4F)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_8E(0x101, 0xFFFECCDA, 0x6E0, 0x30A2, 0x3E8, 0x0)

    def lambda_4D8D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D8D)
    OP_8E(0x101, 0xFFFECBB8, 0x6E0, 0x369C, 0x3E8, 0x0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4134   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4DB9")

    Return()

    # Function_42_4C36 end

    def Function_43_4DBA(): pass

    label("Function_43_4DBA")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_6D(-79450, 4770, 11320, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(39000, 0)
    OP_6E(478, 0)
    SetChrFlags(0x25, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrPos(0xF, -80280, 1520, 11070, 218)
    SetChrPos(0x10, -77730, 1490, 10600, 146)
    SetChrPos(0x11, -81930, 1250, 9130, 327)
    SetChrPos(0x12, -79450, 1250, 9450, 44)
    SetChrPos(0x13, -76040, 1250, 8290, 156)
    SetChrPos(0x14, -81880, 750, 6280, 145)
    SetChrPos(0x15, -79420, 250, 5000, 190)
    SetChrPos(0x16, -77590, 750, 6270, 7)

    def lambda_4F0E():
        OP_67(0, 11700, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F0E)

    def lambda_4F26():
        OP_6C(351000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F26)

    def lambda_4F36():
        OP_6E(544, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4F36)
    OP_43(0x101, 0x0, 0x0, 0x2C)

    def lambda_4F4D():
        OP_90(0xFE, 0xFFFFEC78, 0x27B0, 0xFFFFB1E0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F4D)
    Sleep(500)
    OP_22(0x8D, 0x0, 0x64)

    def lambda_4F72():
        OP_90(0xFE, 0xFFFFF63C, 0x6630, 0xFFFFADF8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4F72)

    def lambda_4F8D():
        OP_90(0xFE, 0x2710, 0x4EC0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4F8D)
    Sleep(200)

    def lambda_4FAD():
        OP_90(0xFE, 0x3A98, 0x3B38, 0xFFFFC568, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4FAD)
    Sleep(200)

    def lambda_4FCD():
        OP_90(0xFE, 0x3A98, 0x4EC0, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4FCD)

    def lambda_4FE8():
        OP_90(0xFE, 0xFFFFEC78, 0x3B38, 0xFFFFD8F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4FE8)
    Sleep(500)

    def lambda_5008():
        OP_90(0xFE, 0x3A98, 0x3B38, 0xFFFFEC78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5008)
    Sleep(300)

    def lambda_5028():
        OP_90(0xFE, 0xFFFFD8F0, 0x3B38, 0xFFFFC568, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5028)
    Sleep(6000)
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_43_4DBA end

    def Function_44_504F(): pass

    label("Function_44_504F")

    OP_22(0xB4, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB4, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB4, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB4, 0x0, 0x64)
    Return()

    # Function_44_504F end

    def Function_45_5073(): pass

    label("Function_45_5073")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 2)), scpexpr(EXPR_END)), "loc_50FB")

    ChrTalk(
        0x102,
        (
            "#010F今天已经很晚了，\x01",
            "就不要到地下水路去了。\x02\x03",
            "明天再和金大哥他们\x01",
            "一起进去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A7")

    label("loc_50FB")


    ChrTalk(
        0x102,
        (
            "#010F看起来这里就是\x01",
            "『渡鸦帮』那些家伙说的\x01",
            "地下水路的入口。\x02\x03",
            "今天已经很晚了，\x01",
            "明天再和金大哥他们\x01",
            "一起进去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51A7")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_45_5073 end

    def Function_46_51C3(): pass

    label("Function_46_51C3")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　前面是港湾区　　　　\x01",
            "※为强化警备体制，禁止通行\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_46_51C3 end

    def Function_47_5241(): pass

    label("Function_47_5241")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　 房屋出租\x01",
            "※可以经营饭店\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_47_5241 end

    def Function_48_52A3(): pass

    label("Function_48_52A3")

    SetPlaceName(0xB8) # 格兰赛尔大圣堂
    Return()

    # Function_48_52A3 end

    def Function_49_52A7(): pass

    label("Function_49_52A7")

    SetPlaceName(0xB7) # 格兰赛尔大圣堂
    Return()

    # Function_49_52A7 end

    def Function_50_52AB(): pass

    label("Function_50_52AB")

    SetPlaceName(0xAF) # 格兰赛尔大圣堂
    Return()

    # Function_50_52AB end

    SaveToFile()

Try(main)
