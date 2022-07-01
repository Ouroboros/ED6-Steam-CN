from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4200   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '士兵丹',                               # 9
        '士兵阿尔兹',                           # 10
        '杜南公爵',                             # 11
        '管家菲利普',                           # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '卡露娜',                               # 15
        '亚妮拉丝',                             # 16
        '库拉茨',                               # 17
        '克鲁茨',                               # 18
        '尤莉亚中尉',                           # 19
        '亲卫队员',                             # 20
        '亲卫队员',                             # 21
        '亲卫队员',                             # 22
        '亲卫队员',                             # 23
        '亲卫队员',                             # 24
        '亲卫队员',                             # 25
        '亲卫队员',                             # 26
        '亲卫队员',                             # 27
        '卡西乌斯',                             # 28
        '卡西乌斯',                             # 29
        '观众',                                 # 30
        '观众',                                 # 31
        '观众',                                 # 32
        '观众',                                 # 33
        '观众',                                 # 34
        '观众',                                 # 35
        '观众',                                 # 36
        '观众',                                 # 37
        '观众',                                 # 38
        '观众',                                 # 39
        '观众',                                 # 40
        '观众',                                 # 41
        '观众',                                 # 42
        '观众',                                 # 43
        '观众',                                 # 44
        '观众',                                 # 45
        '观众',                                 # 46
        '观众',                                 # 47
        '观众',                                 # 48
        '观众',                                 # 49
        '观众',                                 # 50
        '观众',                                 # 51
        '观众',                                 # 52
        '观众',                                 # 53
        '观众',                                 # 54
        '观众',                                 # 55
        '观众',                                 # 56
        '观众',                                 # 57
        '观众',                                 # 58
        '观众',                                 # 59
        '观众',                                 # 60
        '观众',                                 # 61
        '观众',                                 # 62
        '观众',                                 # 63
        '观众',                                 # 64
        '阿鲁姆',                               # 65
        '艾娅莉',                               # 66
        '游客',                                 # 67
        '游客',                                 # 68
        '游客',                                 # 69
        '游客',                                 # 70
        '王都格兰赛尔·北街区',                 # 71
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH02140 ._CH',             # 01
        'ED6_DT07/CH02470 ._CH',             # 02
        'ED6_DT07/CH01610 ._CH',             # 03
        'ED6_DT07/CH00401 ._CH',             # 04
        'ED6_DT07/CH00421 ._CH',             # 05
        'ED6_DT07/CH00391 ._CH',             # 06
        'ED6_DT07/CH00411 ._CH',             # 07
        'ED6_DT06/CH20114 ._CH',             # 08
        'ED6_DT06/CH20116 ._CH',             # 09
        'ED6_DT07/CH02000 ._CH',             # 0A
        'ED6_DT06/CH20155 ._CH',             # 0B
        'ED6_DT06/CH20156 ._CH',             # 0C
        'ED6_DT06/CH20123 ._CH',             # 0D
        'ED6_DT06/CH20124 ._CH',             # 0E
        'ED6_DT06/CH20125 ._CH',             # 0F
        'ED6_DT07/CH01140 ._CH',             # 10
        'ED6_DT07/CH01150 ._CH',             # 11
        'ED6_DT07/CH01100 ._CH',             # 12
        'ED6_DT07/CH01480 ._CH',             # 13
        'ED6_DT07/CH01050 ._CH',             # 14
        'ED6_DT07/CH01040 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT07/CH02470P._CP',             # 02
        'ED6_DT07/CH01610P._CP',             # 03
        'ED6_DT07/CH00401P._CP',             # 04
        'ED6_DT07/CH00421P._CP',             # 05
        'ED6_DT07/CH00391P._CP',             # 06
        'ED6_DT07/CH00411P._CP',             # 07
        'ED6_DT06/CH20114P._CP',             # 08
        'ED6_DT06/CH20116P._CP',             # 09
        'ED6_DT07/CH02000P._CP',             # 0A
        'ED6_DT06/CH20155P._CP',             # 0B
        'ED6_DT06/CH20156P._CP',             # 0C
        'ED6_DT06/CH20123P._CP',             # 0D
        'ED6_DT06/CH20124P._CP',             # 0E
        'ED6_DT06/CH20125P._CP',             # 0F
        'ED6_DT07/CH01140P._CP',             # 10
        'ED6_DT07/CH01150P._CP',             # 11
        'ED6_DT07/CH01100P._CP',             # 12
        'ED6_DT07/CH01480P._CP',             # 13
        'ED6_DT07/CH01050P._CP',             # 14
        'ED6_DT07/CH01040P._CP',             # 15
    )

    DeclNpc(
        X                   = -790,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 950,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2660,
        Z                   = 0,
        Y                   = 27180,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65550,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1310,
        Z                   = 0,
        Y                   = 26540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131085,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -240,
        Z                   = 0,
        Y                   = 27230,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 480,
        Z                   = 0,
        Y                   = 26860,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 393230,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1600,
        Z                   = 0,
        Y                   = 26120,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65549,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2350,
        Z                   = 0,
        Y                   = 27390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 393230,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3680,
        Z                   = 0,
        Y                   = 26400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2140,
        Z                   = 0,
        Y                   = 25650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458765,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -520,
        Z                   = 0,
        Y                   = 25640,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262158,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 950,
        Z                   = 0,
        Y                   = 25560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 393230,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3100,
        Z                   = 0,
        Y                   = 25890,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327694,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2260,
        Z                   = 0,
        Y                   = 24940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -10,
        Z                   = 0,
        Y                   = 24790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131085,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1370,
        Z                   = 0,
        Y                   = 24770,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262157,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3170,
        Z                   = 0,
        Y                   = 24640,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3830,
        Z                   = 0,
        Y                   = 26870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262159,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4590,
        Z                   = 0,
        Y                   = 25090,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327695,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2070,
        Z                   = 0,
        Y                   = 24370,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65549,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1570,
        Z                   = 0,
        Y                   = 24240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131085,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3520,
        Z                   = 0,
        Y                   = 24060,
        Direction           = 3,
        Unknown2            = 0,
        Unknown3            = 393229,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1000,
        Z                   = 0,
        Y                   = 23340,
        Direction           = 343,
        Unknown2            = 0,
        Unknown3            = 262157,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2820,
        Z                   = 0,
        Y                   = 22600,
        Direction           = 13,
        Unknown2            = 0,
        Unknown3            = 196622,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4730,
        Z                   = 0,
        Y                   = 22830,
        Direction           = 353,
        Unknown2            = 0,
        Unknown3            = 262157,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -670,
        Z                   = 0,
        Y                   = 21410,
        Direction           = 12,
        Unknown2            = 0,
        Unknown3            = 327693,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1120,
        Z                   = 0,
        Y                   = 23290,
        Direction           = 2,
        Unknown2            = 0,
        Unknown3            = 327694,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2340,
        Z                   = 0,
        Y                   = 22560,
        Direction           = 359,
        Unknown2            = 0,
        Unknown3            = 65550,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4380,
        Z                   = 0,
        Y                   = 25570,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 262158,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1240,
        Z                   = 0,
        Y                   = 21910,
        Direction           = 357,
        Unknown2            = 0,
        Unknown3            = 393230,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2670,
        Z                   = 0,
        Y                   = 21140,
        Direction           = 358,
        Unknown2            = 0,
        Unknown3            = 458766,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 21580,
        Direction           = 1,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6810,
        Z                   = 0,
        Y                   = 23940,
        Direction           = 46,
        Unknown2            = 0,
        Unknown3            = 393229,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5270,
        Z                   = 0,
        Y                   = 24130,
        Direction           = 36,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1790,
        Z                   = 0,
        Y                   = 22220,
        Direction           = 21,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 310,
        Z                   = 0,
        Y                   = 22190,
        Direction           = 13,
        Unknown2            = 0,
        Unknown3            = 196623,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3970,
        Z                   = 0,
        Y                   = 22250,
        Direction           = 349,
        Unknown2            = 0,
        Unknown3            = 131087,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1370,
        Z                   = 0,
        Y                   = 10340,
        Direction           = 352,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -2340,
        Z                   = 0,
        Y                   = 9870,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -3590,
        Z                   = 0,
        Y                   = 14380,
        Direction           = 54,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -2690,
        Z                   = 0,
        Y                   = 13710,
        Direction           = 353,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 4310,
        Z                   = 0,
        Y                   = 13350,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4960,
        Z                   = 0,
        Y                   = 3770,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -22550,
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
        X                   = -5630,
        Y                   = -1000,
        Z                   = 30090,
        Range               = 6050,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x69BE,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )


    ScpFunction(
        "Function_0_95A",          # 00, 0
        "Function_1_A78",          # 01, 1
        "Function_2_B83",          # 02, 2
        "Function_3_D00",          # 03, 3
        "Function_4_D72",          # 04, 4
        "Function_5_DE5",          # 05, 5
        "Function_6_175C",         # 06, 6
        "Function_7_1FC9",         # 07, 7
        "Function_8_212D",         # 08, 8
        "Function_9_21F2",         # 09, 9
        "Function_10_227C",        # 0A, 10
        "Function_11_22DA",        # 0B, 11
        "Function_12_2387",        # 0C, 12
        "Function_13_23D9",        # 0D, 13
        "Function_14_424F",        # 0E, 14
        "Function_15_5115",        # 0F, 15
        "Function_16_55DA",        # 10, 16
        "Function_17_59F4",        # 11, 17
        "Function_18_6CC1",        # 12, 18
        "Function_19_6CD6",        # 13, 19
        "Function_20_6CFC",        # 14, 20
        "Function_21_6D22",        # 15, 21
    )


    def Function_0_95A(): pass

    label("Function_0_95A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_976")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 15)

    label("loc_976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_984")
    OP_A3(0x3FB)
    Event(0, 16)

    label("loc_984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_992")
    OP_A3(0x3FC)
    Event(0, 17)

    label("loc_992")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_9A2"),
        (101, "loc_9A2"),
        (SWITCH_DEFAULT, "loc_9B8"),
    )


    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B5")
    OP_A2(0x60B)
    Event(0, 13)

    label("loc_9B5")

    Jump("loc_9B8")

    label("loc_9B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_9E0")
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    Jump("loc_A77")

    label("loc_9E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A20")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, -790, 0, 41980, 180)
    SetChrPos(0xD, 950, 0, 41980, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_A77")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_A2A")
    Jump("loc_A77")

    label("loc_A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_A34")
    Jump("loc_A77")

    label("loc_A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_A3E")
    Jump("loc_A77")

    label("loc_A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_A48")
    Jump("loc_A77")

    label("loc_A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_A52")
    Jump("loc_A77")

    label("loc_A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A5C")
    Jump("loc_A77")

    label("loc_A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A66")
    Jump("loc_A77")

    label("loc_A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A70")
    Jump("loc_A77")

    label("loc_A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A77")

    label("loc_A77")

    Return()

    # Function_0_95A end

    def Function_1_A78(): pass

    label("Function_1_A78")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x30060)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABD")
    OP_B1("t4200_y")
    Jump("loc_AC6")

    label("loc_ABD")

    OP_B1("t4200_n")

    label("loc_AC6")

    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_AE3")
    OP_6F(0x0, 450)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)

    label("loc_AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_B7D")
    LoadEffect(0x0, "map\\\\mp016_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -770, 750, 23720, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -520, 750, 42700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_B7D")

    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_A78 end

    def Function_2_B83(): pass

    label("Function_2_B83")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA8")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_CEA")

    label("loc_BA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC1")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_CEA")

    label("loc_BC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_CEA")

    label("loc_BDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_CEA")

    label("loc_BF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_CEA")

    label("loc_C0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C25")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_CEA")

    label("loc_C25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_CEA")

    label("loc_C3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C57")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_CEA")

    label("loc_C57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C70")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_CEA")

    label("loc_C70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C89")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_CEA")

    label("loc_C89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA2")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_CEA")

    label("loc_CA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBB")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_CEA")

    label("loc_CBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_CEA")

    label("loc_CD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_CEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CFF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_CEA")

    label("loc_CFF")

    Return()

    # Function_2_B83 end

    def Function_3_D00(): pass

    label("Function_3_D00")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "格兰赛尔城完全封锁。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "上面下了命令，\x01",
            "无论是谁也不能通行。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_D00 end

    def Function_4_D72(): pass

    label("Function_4_D72")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "你们是在武术大会\x01",
            "取得优胜的游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "晚宴已经结束了。\x01",
            "快回游击士协会去吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_D72 end

    def Function_5_DE5(): pass

    label("Function_5_DE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_FAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E96")

    ChrTalk(
        0xFE,
        (
            "尤莉亚中尉是恐怖分子的说法\x01",
            "让我难以置信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而理查德上校\x01",
            "是政变的主谋这一点\x01",
            "同样让我难以置信……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA8")

    label("loc_E96")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "尤莉亚中尉是恐怖分子的说法\x01",
            "让我难以置信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而理查德上校\x01",
            "是政变的主谋这一点\x01",
            "同样让我难以置信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么优秀的一个人，\x01",
            "怎么会做出这种事来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA8")

    Jump("loc_1758")

    label("loc_FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_FB5")
    Jump("loc_1758")

    label("loc_FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_FF3")

    ChrTalk(
        0xFE,
        (
            "哟，\x01",
            "在王城里面好好参观了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1758")

    label("loc_FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_106E")

    ChrTalk(
        0xFE,
        (
            "欢迎来到\x01",
            "女王陛下的格兰赛尔城！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们从这里进去，\x01",
            "就会有接待人员前来迎接。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1758")

    label("loc_106E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_111F")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "不知道尤莉亚中尉现在怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每天向中尉打招呼\x01",
            "可是我日常工作当中的一大乐趣啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1758")

    label("loc_111F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1268")

    ChrTalk(
        0xFE,
        (
            "我们从今晚开始\x01",
            "必须在市内巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为恐怖分子还未抓到，\x01",
            "所以必须严加防范。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么特务部队的工作\x01",
            "要由我们正规军来善后啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1758")

    label("loc_1268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1306")

    ChrTalk(
        0xFE,
        (
            "特务部队的那群人\x01",
            "在大会中连续获胜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比起去参加比赛，\x01",
            "我倒希望他们\x01",
            "快点去搜捕亲卫队的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1758")

    label("loc_1306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_14B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13D2")

    ChrTalk(
        0xFE,
        (
            "女王陛下生病后，\x01",
            "就几乎很少能在城外\x01",
            "看见理查德上校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来情报部的本部\x01",
            "好像也要暂时转移到王城里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B1")

    label("loc_13D2")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "好像非常忙碌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女王陛下生病后，\x01",
            "几乎很少能在城外看见他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来情报部的本部\x01",
            "好像也要暂时转移到王城里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B1")

    Jump("loc_1758")

    label("loc_14B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_158B")

    ChrTalk(
        0xFE,
        (
            "说起理查德上校，\x01",
            "我当然是很尊敬他啦。\x01",
            "可是那些情报部的黑衣家伙们啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我承认他们有实力，\x01",
            "可他们给人的感觉很不舒服，\x01",
            "在军队里面关于他们的流言也不少。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1758")

    label("loc_158B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_163F")

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "的确是个优秀的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为在王国军中颇具人气，\x01",
            "有许多人都慕名\x01",
            "转到情报部去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1758")

    label("loc_163F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1758")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_16FC")

    ChrTalk(
        0xFE,
        (
            "虽然不能进城参观，\x01",
            "也不要这么灰心丧气嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "格兰赛尔的大街上\x01",
            "还有很多观光胜地呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1758")

    label("loc_16FC")


    ChrTalk(
        0xFE,
        "请你们站住。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，\x01",
            "王城现在禁止无关人等进入。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1758")

    TalkEnd(0xFE)
    Return()

    # Function_5_DE5 end

    def Function_6_175C(): pass

    label("Function_6_175C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1843")

    ChrTalk(
        0xFE,
        (
            "这次政变竟然是由\x01",
            "城内的情报部发起的，\x01",
            "的确让我感到震惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过庆典总算能够平安无事地进行，\x01",
            "真的是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC5")

    label("loc_1843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_184D")
    Jump("loc_1FC5")

    label("loc_184D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_18D6")

    ChrTalk(
        0xFE,
        (
            "你们好啊，\x01",
            "晚宴怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "宫廷料理什么的，\x01",
            "我只在执行警卫时见过，\x01",
            "从来都没机会品尝过呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC5")

    label("loc_18D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_18F9")

    ChrTalk(
        0xFE,
        "那么，祝各位晚上玩得愉快。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC5")

    label("loc_18F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1969")

    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "宫廷料理的材料都已经运到城内来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大概那就是\x01",
            "用来烹制今晚晚宴的食材吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC5")

    label("loc_1969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1ACC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A09")

    ChrTalk(
        0xFE,
        (
            "从今天开始\x01",
            "全城的警戒都加强了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这项工作似乎是由\x01",
            "上校的副官凯诺娜上尉负责的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC9")

    label("loc_1A09")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "从今天开始\x01",
            "全城的警戒都加强了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这项工作似乎是由\x01",
            "上校的副官凯诺娜上尉负责的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "果然相当忙呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC9")

    Jump("loc_1FC5")

    label("loc_1ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1B50")

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "关于女王陛下病情的详细情况，\x01",
            "我们也不太了解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "的确感觉有些不安呢，\x01",
            "也不知道到底会怎么样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC5")

    label("loc_1B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1BC2")

    ChrTalk(
        0xFE,
        (
            "大会正式赛第一回合\x01",
            "好像已经结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "代表王国警备队出场的\x01",
            "那些人怎么样了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC5")

    label("loc_1BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1C7A")

    ChrTalk(
        0xFE,
        (
            "杜南公爵\x01",
            "就算在王城里也很招人讨厌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "理查德上校不在的话，\x01",
            "不知道会变成什么样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D5D")

    label("loc_1C7A")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "杜南公爵\x01",
            "就算在王城里也很招人讨厌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为无论是谁，\x01",
            "都只看到过他在吃、睡、玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "理查德上校不在的话，\x01",
            "不知道会变成什么样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5D")

    Jump("loc_1FC5")

    label("loc_1D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1F44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E44")

    ChrTalk(
        0xFE,
        (
            "因为今年的武术大会是团体战，\x01",
            "比赛场次比以往减少了一些呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正式赛和预选赛不一样，\x01",
            "是在下午进行的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F41")

    label("loc_1E44")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "武术大会的预选赛\x01",
            "好像已经结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今年因为是团体战，\x01",
            "比赛场次比以往减少了一些呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正式赛和预选赛不一样，\x01",
            "是在下午进行的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F41")

    Jump("loc_1FC5")

    label("loc_1F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1F90")

    ChrTalk(
        0xFE,
        (
            "好不容易来一次王都，\x01",
            "就请舒舒服服地享受观光的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC5")

    label("loc_1F90")


    ChrTalk(
        0xFE,
        "现在不能进城参观。\x02",
    )

    CloseMessageWindow()

    label("loc_1FC5")

    TalkEnd(0xFE)
    Return()

    # Function_6_175C end

    def Function_7_1FC9(): pass

    label("Function_7_1FC9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "刚才我正打算\x01",
            "在王城前向她求婚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
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
    TalkEnd(0xFE)
    Return()

    # Function_7_1FC9 end

    def Function_8_212D(): pass

    label("Function_8_212D")

    TalkBegin(0xFE)

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
            "不过，我们俩这趟旅程的最高潮\x01",
            "从现在才开始哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_212D end

    def Function_9_21F2(): pass

    label("Function_9_21F2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "没想到呢，\x01",
            "今年也能和孙子一起\x01",
            "一睹女王陛下的风采。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀，太好了太好了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_21F2 end

    def Function_10_227C(): pass

    label("Function_10_227C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "公主殿下真的好漂亮哦～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我只能用『哇啊～』来形容了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_227C end

    def Function_11_22DA(): pass

    label("Function_11_22DA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "女王陛下生病的事\x01",
            "只是谣言吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "太好了……\x01",
            "我对此事一直很担心呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_22DA end

    def Function_12_2387(): pass

    label("Function_12_2387")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我也要去街区那边\x01",
            "好好逛一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这会儿那里\x01",
            "肯定非常热闹。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_2387 end

    def Function_13_23D9(): pass

    label("Function_13_23D9")

    EventBegin(0x0)
    StopSound(0x186A0, 0x2BF20, 0x3E8)
    OP_6C(30000, 0)

    def lambda_23F7():
        OP_6D(-930, 750, 44710, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23F7)

    def lambda_240F():
        OP_67(0, 4250, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_240F)

    def lambda_2427():
        OP_6B(11000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2427)

    def lambda_2437():
        OP_6C(0, 15000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2437)
    Sleep(12000)
    SetChrPos(0x101, -910, 0, 8880, 0)
    SetChrPos(0x102, 1000, 0, 10110, 0)

    def lambda_246E():
        OP_6D(-290, 0, 32350, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_246E)

    def lambda_2486():
        OP_6B(7180, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2486)

    def lambda_2496():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2496)

    def lambda_24A6():
        OP_8E(0xFE, 0xFFFFFD62, 0x0, 0x4808, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24A6)

    def lambda_24C1():
        OP_8E(0xFE, 0x258, 0x0, 0x4808, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24C1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#001F哇～……\x01",
            "这就是格兰赛尔城啊。\x02\x03",
            "女王住的地方，\x01",
            "果然是又气派又漂亮呢……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x01",
            "看起来不仅是漂亮，\x01",
            "而且也十分的坚固呢。\x02\x03",
            "那个巨大的城门就是很好的例子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F确实……\x01",
            "不可能那么简单就能进得去呢。\x02\x03",
            "总之……\x01",
            "只能先向那边的士兵打听一下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们先暗中调查一下吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015F……就像刚从乡下来，\x01",
            "想进王城参观那样。\x02\x03",
            "想借此机会拜见女王，\x01",
            "哪怕看一眼也好。\x02\x03",
            "#010F——这种设定不错吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F还是老样子，摆出一幅若无其事的表情，\x01",
            "立刻就能说出想法来……\x02\x03",
            "老是让人家吃了一惊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#019F这句话我就当成是夸奖收下了。\x02",
    )

    CloseMessageWindow()

    def lambda_282C():
        OP_6D(0, 250, 42590, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_282C)

    def lambda_2844():
        OP_6B(5100, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2844)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x9, 400)
    WaitChrThread(0x101, 0x2)
    SetChrPos(0x101, -850, 0, 25330, 0)
    SetChrPos(0x102, 1090, 0, 22700, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "喂～你们好～\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_28C8():

        label("loc_28C8")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_28C8")

    QueueWorkItem2(0x8, 1, lambda_28C8)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_28F0():

        label("loc_28F0")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_28F0")

    QueueWorkItem2(0x9, 1, lambda_28F0)

    def lambda_2901():
        OP_8E(0xFE, 0x258, 0x0, 0x9290, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2901)

    def lambda_291C():
        OP_8E(0xFE, 0xFFFFFD62, 0x0, 0x9290, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_291C)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#1P哦，你们好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P欢迎来到格兰赛尔城。\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F我们是刚从洛连特来到王都观光的。\x01",
            "　\x02\x03",
            "借此机会，\x01",
            "想进城里面参观一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1P啊，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P两位游客，很抱歉。\x01",
            "格兰赛尔城是禁止无关人员入内的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P由于恐怖分子骚乱，\x01",
            "现在的检查更为严格了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P不过，抓到了恐怖分子之后，\x01",
            "应该就允许大家参观了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F是这样啊……真可惜。\x02\x03",
            "唉，难道见女王陛下一面的梦想\x01",
            "还是没办法实现吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1P对了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P诞辰庆典那天，\x01",
            "女王会照例在王城的露台上对市民致意，\x01",
            "我想应该会有见面的机会的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P不过最近，\x01",
            "陛下的身体状况不是很好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P例行的致意还会不会有呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F请问……\x01",
            "女王陛下生病了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P是啊……\x01",
            "大概是因为操劳过度……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P而且，因为自己十分信赖的亲卫队\x01",
            "被当成恐怖事件的嫌疑犯这件事，\x01",
            "也受了相当大的打击吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P最近都没有出现在谒见室，\x01",
            "应该是在女王宫静养吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P真是的，亲卫队那些家伙，\x01",
            "对陛下的信赖反倒恩将仇报……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P平常我就不喜欢\x01",
            "这些所谓的精英。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "#2P可、可是，\x01",
            "尤莉亚中尉平时不是很亲切的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 800)

    ChrTalk(
        0x9,
        (
            "#2P对我们这些普通的士兵，\x01",
            "也亲自教授剑术和行事方法……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P说她是恐怖分子，\x01",
            "我有点不太相信呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x8,
        "#1P这、这是肯定的啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P可能因为部下的胡作非为而感到责任重大，\x01",
            "所以才就这样突然失踪的啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P啊啊……\x01",
            "尤莉亚小姐真是可怜啊……\x02",
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
        (
            "#509F（看起来，这些人……）\x02\x03",
            "（只是因为尤莉亚小姐的关系，\x01",
            "　在嫉妒其他的队员呢……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F（嗯，的确是这样……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "#1P咳咳……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P总之，就是这个原因，\x01",
            "格兰赛尔城禁止入内。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        "#2P抱歉，请回去吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唉，这样的话，\x01",
            "也只好暂时打消这个念头了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F不过，我还是有点担心呢。\x02\x03",
            "女王陛下的健康暂且不论，\x01",
            "政务方面不用管理吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P嗯……\x01",
            "这个担心很有道理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P虽然这样，\x01",
            "还是有名义上的代理人的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F名义上的代理人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P哈哈。\x01",
            "顾名思义，只是『名义上的』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P那一位大人和政务\x01",
            "还真是八竿子打不着啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        "#2P喂喂，说话要小心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P不过确实，\x01",
            "我也觉得公主更为适合呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        "#1P看，你不也是这样想的……\x02",
    )

    CloseMessageWindow()
    OP_22(0xD2, 0x0, 0x64)
    OP_73(0x0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -270, 750, 48420, 180)
    SetChrPos(0xB, 550, 750, 49230, 180)

    ChrTalk(
        0x101,
        "#004F什、什么……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 400)
    TurnDirection(0x9, 0xA, 400)

    ChrTalk(
        0x8,
        "#1P哦，好像出来了。\x02",
    )

    CloseMessageWindow()

    def lambda_34C2():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34C2)

    def lambda_34DA():
        OP_6B(3800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34DA)

    def lambda_34EA():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_34EA)
    Sleep(100)
    TurnDirection(0x8, 0x9, 400)

    def lambda_3506():
        OP_8F(0xFE, 0xFFFFF6F0, 0x0, 0xA406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3506)
    TurnDirection(0x9, 0x8, 400)

    def lambda_3528():
        OP_8F(0xFE, 0x910, 0x0, 0xA4A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3528)
    OP_6D(-10, 750, 48050, 3000)

    def lambda_3554():

        label("loc_3554")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_3554")

    QueueWorkItem2(0x101, 1, lambda_3554)

    def lambda_3565():

        label("loc_3565")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_3565")

    QueueWorkItem2(0x102, 1, lambda_3565)
    SetChrPos(0x101, -2130, 0, 39490, 0)
    SetChrPos(0x102, -2130, 0, 37840, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    OP_73(0x0)

    def lambda_35A9():
        OP_8E(0xFE, 0xFFFFFEFC, 0x2EE, 0xAE2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_35A9)
    Sleep(500)

    def lambda_35C9():
        OP_8E(0xFE, 0x276, 0x2EE, 0xB090, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_35C9)
    OP_6D(0, 750, 44920, 2000)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xB, 0x1)
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(
        0xA,
        (
            "#222F哼，这叫什么事啊！\x02\x03",
            "现在预选赛不是已经开始了吗！？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(
        0xA,
        (
            "#224F菲利普！\x01",
            "都是因为你没有叫我！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(
        0xB,
        (
            "#722F实在是抱歉，公爵大人。\x02\x03",
            "不过，这也是因为\x01",
            "公爵大人不注意生活规律啊……\x02\x03",
            "这几天连续大摆宴席，\x01",
            "又是吃又是唱地大闹……\x02\x03",
            "啤酒和油炸食品放在一起大量地吃，\x01",
            "还彻夜地看漫画杂志一直到早上……\x01",
            "　\x02\x03",
            "总是这样，\x01",
            "睡过头也是理所当然的了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#225F闭嘴，菲利普！\x01",
            "你的这些话我已经听够了！\x02\x03",
            "作为下任国王的我，\x01",
            "有权力想干什么就干什么！\x02\x03",
            "#224F哎呀，时间紧迫！\x01",
            "赶快去王立竞技场才行！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)

    def lambda_38ED():
        OP_8E(0xFE, 0xFFFFFEF2, 0x0, 0x6D74, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_38ED)
    Sleep(500)

    def lambda_390D():
        OP_8E(0xFE, 0x42E, 0x0, 0x6BF8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_390D)
    OP_6F(0x0, 450)
    OP_70(0x0, 0x0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_6D(-30, 0, 40870, 5000)

    def lambda_396B():
        OP_8F(0xFE, 0xFFFFFCEA, 0x0, 0xA3FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_396B)

    def lambda_3986():
        OP_8F(0xFE, 0x3B6, 0x0, 0xA3FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3986)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 180, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_63(0x101)
    OP_63(0x102)
    Sleep(400)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        "#509F……哎…………\x02",
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xFFFFFAD8, 0x0, 0x96E6, 0x7D0, 0x0)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        "#014F#6P……我说，难道……\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    TurnDirection(0x9, 0x101, 400)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "#5P我知道，不用再说了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P刚才那位就是陛下的代理人，\x01",
            "现在主理政务的杜南公爵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F我……\x01",
            "我的头开始疼了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P总、总之不用担心。\x01",
            "有个可靠的人在辅佐，所以没问题的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P多亏了那个人，\x01",
            "至今还没出什么大乱子呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_3B85():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B85)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        "#012F#6P可靠的辅佐人……吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P嘿嘿，那个人就是\x01",
            "王国军情报部的理查德上校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P可以说，他代替放荡的杜南公爵，\x01",
            "一手处理王国的政务呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F（果、果然……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#6P（比想象中还要更加深入地\x01",
            "　控制了国家的核心呢……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P不过，虽然不能进城参观，\x01",
            "也不要这么灰心丧气嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P王都格兰赛尔还有\x01",
            "很多观光胜地呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "#2P好不容易来一次王都，\x01",
            "就请慢慢地享受观光的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F嗯，说的也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F#6P感谢你们的好意。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x8, -790, 0, 41980, 180)
    SetChrPos(0x9, 950, 0, 41980, 180)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_6D(-170, 0, 24540, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    StopSound(0x0, 0x0, 0x1)
    SetChrPos(0x102, 660, 0, 34050, 18)
    SetChrPos(0x101, -860, 0, 33870, 45)

    def lambda_3EB7():
        OP_8E(0xFE, 0xFFFFFCA4, 0x0, 0x623E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EB7)
    Sleep(300)

    def lambda_3ED7():
        OP_8E(0xFE, 0x294, 0x0, 0x6108, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3ED7)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    def lambda_3F01():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F01)
    WaitChrThread(0x102, 0x1)

    def lambda_3F14():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F14)

    ChrTalk(
        0x101,
        (
            "#006F#3P嗯……\x01",
            "比想象中收获更大呢。\x02\x03",
            "#007F而且，那个胖子公爵\x01",
            "竟然是女王陛下的代理人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F实际掌权的，是理查德上校吧。\x01",
            "　\x02\x03",
            "而且……\x01",
            "自己的阴谋周围的人都浑然不觉。\x02\x03",
            "#012F操纵情报的手段还真是高明啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#3P真是的，约修亚。\x01",
            "这可不是称赞敌人的时候啊。\x02\x03",
            "#006F对了对了，\x01",
            "那个公爵好像去看武术大会了呢。\x02\x03",
            "我们也去看看如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F是啊……\x02\x03",
            "#010F调查一下公爵的行动，\x01",
            "也许会有什么收获也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#3P那么就决定了！\x02\x03",
            "#505F#3P嗯……\x01",
            "王立竞技场是在哪个方向呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我记得应该是在东街区吧。\x02\x03",
            "先回到大街上然后往东走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x45, 0x1, 0x200)
    OP_28(0x45, 0x1, 0x400)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_13_23D9 end

    def Function_14_424F(): pass

    label("Function_14_424F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_425C")
    Return()

    label("loc_425C")

    EventBegin(0x0)

    def lambda_4264():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4264)

    def lambda_4272():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4272)
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#073F哦，现在就进城去吗？\x02\x03",
            "晚宴结束之后要在城里的客房过夜，\x01",
            "明天才能回到街上来。\x01",
            "　\x02",
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
            "【进入格兰赛尔城】\x01",      # 0
            "【等一会儿再来】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_439F"),
        (1, "loc_446D"),
        (SWITCH_DEFAULT, "loc_44A1"),
    )


    label("loc_439F")


    ChrTalk(
        0x108,
        (
            "#070F那么就把请帖给那边的门卫看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嗯～\x01",
            "总觉得很紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F没错，像这样被招待进王城的体验，\x01",
            "对我们这些普通百姓来说还真是难得啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44A1")

    label("loc_446D")


    ChrTalk(
        0x108,
        "#070F知道了，一会儿再来吧。\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    label("loc_44A1")


    def lambda_44A7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44A7)

    def lambda_44B5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44B5)

    def lambda_44C3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_44C3)

    def lambda_44D1():
        OP_67(0, 5220, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_44D1)

    def lambda_44E9():
        OP_6E(287, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_44E9)
    OP_6D(110, 0, 41220, 3000)
    SetChrPos(0x101, -620, 0, 32729, 0)
    SetChrPos(0x102, 920, 0, 32590, 0)
    SetChrPos(0x108, 90, 0, 32000, 0)

    def lambda_453D():
        OP_8E(0xFE, 0xFFFFFCFE, 0x0, 0x9B82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_453D)
    Sleep(300)

    def lambda_455D():
        OP_8E(0xFE, 0x4E2, 0x0, 0x9BD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_455D)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#1P这里是女王陛下\x01",
            "居住的格兰赛尔城。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果没有事情的话，\x01",
            "就请离开这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哎。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#006F晚上好～\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        "#010F#4P那天麻烦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "怎么，原来是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "你们还呆在王都吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯，稍微有点事情。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P今天是因为受到正式邀请才来这里的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "正式的……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "邀请……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#1P……是公爵亲自给我们的请帖。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47E5():
        OP_8E(0xFE, 0x12C, 0x0, 0x9862, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_47E5)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "巨、巨人！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x108, 0x1)

    ChrTalk(
        0x108,
        "#070F#4P给，这就是请帖。\x02",
    )

    CloseMessageWindow()
    OP_8F(0x108, 0x168, 0x0, 0xA1D6, 0x7D0, 0x0)
    OP_3F(0x371, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "晚宴请帖\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_8F(0x108, 0x12C, 0x0, 0x9E98, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        "嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "『金·瓦赛克等四人\x01",
            "　在武术大会获得优胜，\x01",
            "　特此邀请参加晚宴……』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这样啊……\x01",
            "你们是武术大会的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我记得，\x01",
            "获得优胜的是来自东方的\x01",
            "武术家所率领的小组……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "难道……\x01",
            "你们就是那个小组的成员？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F嘿嘿，其实就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P只不过是帮了点微不足道的小忙而已。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "原来如此，是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……你们的事情\x01",
            "我从女官长那里听说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过，好像少一个人啊。\x01",
            "那一位怎么没有来呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#4P因为有点私事，\x01",
            "所以没办法来参加了。\x02\x03",
            "出席的只有我们而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "是吗，那真是遗憾啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "算了……\x01",
            "现在就让你们进城吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4C0B():
        OP_6D(70, 750, 44190, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C0B)

    def lambda_4C23():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C23)

    def lambda_4C33():
        OP_6E(438, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4C33)
    OP_8E(0x9, 0x6E, 0x2EE, 0xADD4, 0x7D0, 0x0)
    OP_8C(0x9, 0, 400)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x9,
        (
            "武术大会的优胜者，\x01",
            "金选手等三人前来光临！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "开门！\x02",
    )

    CloseMessageWindow()

    def lambda_4CC5():
        OP_6D(70, 3450, 44190, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CC5)

    def lambda_4CDD():
        OP_67(0, 7620, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4CDD)

    def lambda_4CF5():
        OP_8E(0x8, 0xFFFFF704, 0x2EE, 0xAE38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4CF5)
    OP_8E(0x9, 0x992, 0x2EE, 0xAE38, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 180, 400)
    OP_22(0xD2, 0x0, 0x64)
    Sleep(2000)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    OP_73(0x0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#004F哇啊……\x02\x03",
            "和哈肯大门一样，\x01",
            "这个城门也非常的有魄力啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F而且，只有王城才能建造得如此坚固。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1P这是不可能被攻陷的城堡呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P建国以来，\x01",
            "虽然亚宁堡没有被外敌突破过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P但因为贵族的叛乱，\x01",
            "王都数次被卷入战火之中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P那个时候，多亏了这座城堡，\x01",
            "王家才得以击退反叛军的进攻，\x01",
            "保护了王族成员和避难的人民……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P有很多这种故事流传下来呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哎～有这样的事啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯，有悠久历史的国家\x01",
            "总会有种种古代的传奇故事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P好了，请进吧！\x01",
            "欢迎来到女王陛下的格兰赛尔城！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P进去之后，\x01",
            "就会有接待人员迎接你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P祝你们晚上过得愉快。\x02",
    )

    CloseMessageWindow()

    def lambda_50B7():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_50B7)
    Sleep(100)

    def lambda_50D2():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50D2)
    Sleep(100)

    def lambda_50ED():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_50ED)
    OP_A2(0x638)
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/T4250   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_424F end

    def Function_15_5115(): pass

    label("Function_15_5115")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_6D(70, -1900, 45200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(357, 0)
    SetChrPos(0xC, -790, 0, 41980, 180)
    SetChrPos(0xD, 950, 0, 41980, 180)
    OP_22(0xD2, 0x0, 0x64)
    Sleep(500)

    def lambda_51AE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_51AE)
    Sleep(200)

    def lambda_51C1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_51C1)
    OP_6D(70, 2550, 45150, 2000)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)

    ChrTalk(
        0xC,
        "怎、怎么回事……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "奇怪了啊……\x01",
            "不是说已经完全封闭了吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5281():
        OP_8C(0xFE, 180, 800)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5281)
    Sleep(100)

    def lambda_5294():
        OP_8C(0xFE, 180, 800)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5294)
    OP_6D(70, -1900, 45200, 1000)

    ChrTalk(
        0xC,
        "#1P什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2P怎么会！！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-1030, 0, 9000, 0)
    OP_67(0, 9340, -13360, 0)
    OP_6B(1000, 0)
    OP_6C(135000, 0)
    OP_6E(747, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x12, 1730, 0, -280, 0)
    SetChrPos(0x13, 1730, 0, -2790, 180)
    SetChrPos(0x14, 1730, 0, -5480, 180)
    SetChrPos(0x15, 1730, 0, -8070, 180)
    SetChrPos(0x16, 1730, 0, -10050, 180)
    SetChrPos(0xE, 3230, 0, -4350, 0)
    SetChrPos(0x10, 3230, 0, -1480, 0)
    SetChrPos(0x17, -1770, 0, -380, 260)
    SetChrPos(0x18, -1770, 0, -2970, 180)
    SetChrPos(0x19, -1770, 0, -5140, 180)
    SetChrPos(0x1A, -1770, 0, -7650, 180)
    SetChrPos(0xF, -3240, 0, -1470, 360)
    SetChrPos(0x11, -3240, 0, -4130, 360)

    def lambda_543C():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_543C)

    def lambda_5457():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5457)

    def lambda_5472():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5472)

    def lambda_548D():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_548D)

    def lambda_54A8():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_54A8)

    def lambda_54C3():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_54C3)

    def lambda_54DE():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_54DE)

    def lambda_54F9():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_54F9)

    def lambda_5514():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5514)

    def lambda_552F():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_552F)

    def lambda_554A():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_554A)

    def lambda_5565():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5565)

    def lambda_5580():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5580)

    def lambda_559B():
        OP_6D(-390, 0, 29050, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_559B)

    def lambda_55B3():
        OP_6C(44000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_55B3)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_5115 end

    def Function_16_55DA(): pass

    label("Function_16_55DA")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
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
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(50, 4200, 30840, 0)
    OP_67(0, 6310, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(61000, 0)
    OP_6E(391, 0)

    def lambda_56F5():
        OP_6D(50, 100, 30840, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_56F5)

    def lambda_570D():
        OP_6C(50000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_570D)
    Sleep(5000)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x23, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x25, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x26, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x27, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x28, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x29, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x31, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x32, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x33, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x35, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x36, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x37, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x38, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x39, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_599D():
        OP_6D(20, 13000, 44770, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_599D)

    def lambda_59B5():
        OP_67(0, 3640, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_59B5)

    def lambda_59CD():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_59CD)
    Sleep(2500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_55DA end

    def Function_17_59F4(): pass

    label("Function_17_59F4")

    EventBegin(0x0)
    OP_6F(0x0, 450)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x1C, 3420, 0, -7500, 0)
    SetChrPos(0x1B, 2600, 0, -6950, 0)
    SetChrPos(0x101, 3420, 0, -8400, 0)
    SetChrPos(0x102, 4150, 0, -7140, 0)
    SetChrChipByIndex(0x102, 11)
    SetChrChipByIndex(0x1B, 12)
    ClearChrFlags(0x1B, 0x80)
    SetMapFlags(0x1)
    OP_69(0x1C, 0x0)
    OP_6A(0x1C)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_5AA4():
        OP_6C(135000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5AA4)

    def lambda_5AB4():
        OP_91(0xFE, 0xFFFFF272, 0x0, 0x9470, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5AB4)
    OP_43(0x101, 0x1, 0x0, 0x12)
    OP_43(0x102, 0x1, 0x0, 0x13)
    OP_43(0x1B, 0x1, 0x0, 0x14)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F老爸也真是的……\x02\x03",
            "就不能陪我们一起参加诞辰庆典吗，\x01",
            "至少一起参观一下王都也好啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#080F抱歉，我还有紧急的军事会议要出席。\x02\x03",
            "虽然理查德被逮捕了，\x01",
            "但是逃亡中的特务兵还有很多。\x02\x03",
            "凯诺娜上尉也不知道什么时候\x01",
            "从那个地下遗迹中失踪了。\x02\x03",
            "而且，参加武术大会的空贼团\x01",
            "也趁混乱的时候逃走了。\x02\x03",
            "为了不让诞辰庆典发生任何骚动，\x01",
            "我们还得加强警备工作才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F真是的……\x01",
            "那些臭味相投的顽固家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F确实，无论哪一伙人，\x01",
            "都不像是会就此善罢甘休的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#082F总之，警备方面可以放心。\x02\x03",
            "问题是，在那个地下遗迹里发生的事情，\x01",
            "到底隐含着什么含义呢。\x02\x03",
            "理查德解开的那个封印，\x01",
            "到底会产生什么样的影响呢……\x02\x03",
            "『辉之环』是什么……\x02\x03",
            "这些事情必须要弄清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯……确实是这样。\x02\x03",
            "而且，和上校战斗的时候，\x01",
            "我们发现他的记忆好像有些混乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#085F嗯，和克鲁茨一样，\x01",
            "有些重要的事情想不起来了。\x02\x03",
            "#082F虽然如此，\x01",
            "我在审讯他时还是弄清楚了一件事。\x02\x03",
            "就是那个黑色导力器的来历。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F查到制造它的人了吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#082F不……仅仅是一些线索。\x01",
            "只是知道是谁将这东西带到了情报部。\x02\x03",
            "那个人就是情报部特务部队队长\x01",
            "洛伦斯·博格少尉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F是、是那个人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#085F在被招入情报部的时候，\x01",
            "他把那个东西交给了理查德。\x02\x03",
            "而且，理查德的政变计划，\x01",
            "大概也是从那个时候开始的。\x01",
            "　\x02\x03",
            "#082F总之，有必要调查清楚\x01",
            "那个洛伦斯少尉的真实身份。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F原来是这样啊……\x01",
            "虽然不知道他的真正目的是什么……\x02\x03",
            "#006F说起来，那次的战斗还真不可思议，\x01",
            "我和雪拉姐她们看见他的样子了呢。 \x02\x03",
            "如果有需要的话，\x01",
            "我可以画一张肖像画给你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#080F啊，那到时候就拜托了。 \x02\x03",
            "#081F虽然对你的绘画水平不敢抱有期望……\x01",
            "　\x02\x03",
            "不过，既然还有其他人见过，\x01",
            "拜托雪拉扎德或者陛下帮忙也可以嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F哼，你这是什么意思！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x1C, 0xFF)
    Fade(1000)
    SetChrChipByIndex(0x1B, 10)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x1B, 0)
    TurnDirection(0x102, 0x101, 0)
    TurnDirection(0x1B, 0x101, 0)
    OP_6C(0, 0)
    OP_6B(2600, 0)
    ClearMapFlags(0x1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#014F#2P艾丝蒂尔……\x02\x03",
            "洛伦斯少尉的脸，你看见过了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#501F哎，我没告诉过你吗？\x02\x03",
            "在女王宫露台上交手的时候，\x01",
            "那个少尉把自己的头盔摘掉了。\x02\x03",
            "看样子大概是２５岁左右吧，\x01",
            "一头银灰色的头发。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#514F#2P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F而且女王当时说他的眼神深邃，\x01",
            "给人的感觉好像经历过巨大的苦难一样。\x02\x03",
            "#003F该怎么说呢……表面看来非常冷漠， \x01",
            "却从内心深处散发出炽热的情感……\x02\x03",
            "而且，逃走的时候还对女王说\x01",
            "『您并没有怜悯我的资格』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P『您并没有怜悯我的资格』……\x02\x03",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F约修亚……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#080F唉，我说你这孩子，\x01",
            "从以前开始就总是顾虑得太多。\x02\x03",
            "后面的事情交给我们处理就行了，\x01",
            "你和艾丝蒂尔还是尽情享受诞辰庆典吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1B, 400)

    ChrTalk(
        0x102,
        (
            "#014F#2P啊……\x02\x03",
            "#010F嗯，说的也是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F是啊是啊。\x01",
            "我们一定要玩个痛快。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1B, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#006F对了，\x01",
            "我们今天晚上要在城里住吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x101, 400)

    ChrTalk(
        0x1B,
        (
            "#080F对，女王陛下安排了\x01",
            "王城右翼的两间客房给我们。\x02\x03",
            "我和约修亚在右边，\x01",
            "艾丝蒂尔和雪拉扎德在左边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "我和雪拉姐住一起吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#084F难道还有更好的组合吗？\x02\x03",
            "那么，我和艾丝蒂尔，\x01",
            "约修亚和雪拉扎德，这样安排好了。\x02\x03",
            "#081F你可以尽情向老爸撒娇了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F……真、真讨厌～\x01",
            "还是和雪拉姐一起比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#081F哇哈哈，真是害羞啊。\x02\x03",
            "#080F那么，晚上再见了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1B, 0, 400)

    def lambda_6936():

        label("loc_6936")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_6936")

    QueueWorkItem2(0x101, 1, lambda_6936)

    def lambda_6947():

        label("loc_6947")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_6947")

    QueueWorkItem2(0x102, 1, lambda_6947)
    OP_43(0x1B, 0x1, 0x0, 0x15)
    Sleep(5000)
    SetChrFlags(0x1B, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#2P反正已经好久不见了，\x01",
            "和父亲住同一个房间不是很好吗。\x02\x03",
            "关于你的母亲……\x01",
            "不是有很多话想跟父亲说吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F虽然是这样没错……\x02\x03",
            "让约修亚和雪拉姐住同一个房间，\x01",
            "这样我是怎么也不能允……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#2P哎？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#503F没、没什么啦！\x02\x03",
            "#008F不说这个了……\x01",
            "我们还是到王城外面逛逛吧！\x02\x03",
            "街上好像很热闹呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P是啊，我们到处转转吧。\x01",
            "　\x02\x03",
            "如果逛得感到累了，\x01",
            "就去东街区的休息处歇歇脚好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，是百货商店后面的休息处吗。\x02\x03",
            "#001F那么，我们先在街上参观，\x01",
            "最后再去那里休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0x0, 0x0)
    OP_6A(0x0)
    OP_92(0x1, 0x0, 0x0, 0x2710, 0x0)
    OP_8C(0x101, 180, 0)
    OP_8C(0x102, 180, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    Sleep(500)
    OP_28(0x4F, 0x1, 0x20)
    OP_28(0x4F, 0x1, 0x40)
    OP_28(0x4F, 0x1, 0x80)
    OP_28(0x4F, 0x1, 0x100)
    OP_28(0x4F, 0x1, 0x200)
    OP_28(0x4F, 0x1, 0x400)
    OP_28(0x4F, 0x1, 0x800)
    OP_28(0x50, 0x4, 0x40)
    OP_28(0x51, 0x4, 0x40)
    ClearMapFlags(0x800)
    ClearMapFlags(0x2000000)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_17_59F4 end

    def Function_18_6CC1(): pass

    label("Function_18_6CC1")

    OP_90(0xFE, 0xFFFFF272, 0x0, 0x9470, 0x320, 0x0)
    Return()

    # Function_18_6CC1 end

    def Function_19_6CD6(): pass

    label("Function_19_6CD6")

    OP_90(0xFE, 0xFFFFF272, 0x0, 0x9470, 0x320, 0x0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    TurnDirection(0x102, 0x1B, 400)
    Return()

    # Function_19_6CD6 end

    def Function_20_6CFC(): pass

    label("Function_20_6CFC")

    OP_90(0xFE, 0xFFFFF272, 0x0, 0x9470, 0x320, 0x0)
    SetChrChipByIndex(0x1B, 10)
    SetChrSubChip(0x1B, 0)
    TurnDirection(0x1B, 0x101, 400)
    Return()

    # Function_20_6CFC end

    def Function_21_6D22(): pass

    label("Function_21_6D22")

    OP_8E(0x1B, 0x46, 0x2EE, 0xAAD2, 0x7D0, 0x0)
    OP_8E(0x1B, 0x190, 0x2EE, 0xBBBC, 0x7D0, 0x0)
    Return()

    # Function_21_6D22 end

    SaveToFile()

Try(main)
