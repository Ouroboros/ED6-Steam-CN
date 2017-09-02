from ED6ScenarioHelper import *

def main():
    # 帝国大使馆

    CreateScenaFile(
        FileName            = 'T4101   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T4101   ._SN',
            'ED6_DT01/T4101_1 ._SN',
            'ED6_DT01/T4101_2 ._SN',
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
        '穆拉',                                 # 10
        '莉珐',                                 # 11
        '接待员',                               # 12
        '迪恩',                                 # 13
        '雷斯',                                 # 14
        '洛克',                                 # 15
        '士兵',                                 # 16
        '士兵',                                 # 17
        '士兵',                                 # 18
        '士兵',                                 # 19
        '士兵',                                 # 20
        '士兵',                                 # 21
        '士兵',                                 # 22
        '士兵',                                 # 23
        '士兵',                                 # 24
        '士兵',                                 # 25
        '士兵',                                 # 26
        '士兵',                                 # 27
        '士兵',                                 # 28
        '士兵',                                 # 29
        '士兵',                                 # 30
        '士兵',                                 # 31
        '亚妮拉丝',                             # 32
        '亚鲁瓦教授',                           # 33
        '拉尔夫',                               # 34
        '士兵贝尔坎',                           # 35
        '士兵达克特',                           # 36
        '娜碧',                                 # 37
        '米亚尔',                               # 38
        '戈万',                                 # 39
        '帕菲',                                 # 40
        '娜娜',                                 # 41
        '安敦',                                 # 42
        '利库斯',                               # 43
        '索露贝',                               # 44
        '卡拉',                                 # 45
        '卢希娅',                               # 46
        '卡拉莉丝',                             # 47
        '尼莫',                                 # 48
        '拉奥尼',                               # 49
        '梅夏',                                 # 50
        '维尔娜婆婆',                           # 51
        '士兵',                                 # 52
        '士兵',                                 # 53
        '士兵',                                 # 54
        '特务兵',                               # 55
        '特务兵',                               # 56
        '特务兵',                               # 57
        '游客',                                 # 58
        '游客',                                 # 59
        '游客',                                 # 60
        '游客',                                 # 61
        '游客',                                 # 62
        '游客',                                 # 63
        '游客',                                 # 64
        '游客',                                 # 65
        '游客',                                 # 66
        '游客',                                 # 67
        '游客',                                 # 68
        '游客',                                 # 69
        '游客',                                 # 70
        '游客',                                 # 71
        '游客',                                 # 72
        '游客',                                 # 73
        '游客',                                 # 74
        '游客',                                 # 75
        '游客',                                 # 76
        '游客',                                 # 77
        '游客',                                 # 78
        '游客',                                 # 79
        '游客',                                 # 80
        '游客',                                 # 81
        '游客',                                 # 82
        '游客',                                 # 83
        '游客',                                 # 84
        '游客',                                 # 85
        '游客',                                 # 86
        '游客',                                 # 87
        '游客',                                 # 88
        '王都格兰赛尔·北街区',                 # 89
        '王都格兰赛尔·南街区',                 # 90
        '王都格兰赛尔·空港',                   # 91
        '目标用摄像机',                         # 92
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
        'ED6_DT07/CH02190 ._CH',             # 01
        'ED6_DT07/CH01540 ._CH',             # 02
        'ED6_DT07/CH01640 ._CH',             # 03
        'ED6_DT07/CH02510 ._CH',             # 04
        'ED6_DT07/CH02520 ._CH',             # 05
        'ED6_DT07/CH02530 ._CH',             # 06
        'ED6_DT07/CH01630 ._CH',             # 07
        'ED6_DT07/CH02050 ._CH',             # 08
        'ED6_DT07/CH00110 ._CH',             # 09
        'ED6_DT06/CH20101 ._CH',             # 0A
        'ED6_DT07/CH01200 ._CH',             # 0B
        'ED6_DT07/CH02630 ._CH',             # 0C
        'ED6_DT07/CH01150 ._CH',             # 0D
        'ED6_DT07/CH01040 ._CH',             # 0E
        'ED6_DT07/CH01120 ._CH',             # 0F
        'ED6_DT07/CH02480 ._CH',             # 10
        'ED6_DT07/CH02490 ._CH',             # 11
        'ED6_DT07/CH01480 ._CH',             # 12
        'ED6_DT07/CH01143 ._CH',             # 13
        'ED6_DT07/CH01350 ._CH',             # 14
        'ED6_DT07/CH01030 ._CH',             # 15
        'ED6_DT07/CH01070 ._CH',             # 16
        'ED6_DT06/CH20101 ._CH',             # 17
        'ED6_DT07/CH01470 ._CH',             # 18
        'ED6_DT07/CH01100 ._CH',             # 19
        'ED6_DT07/CH01210 ._CH',             # 1A
        'ED6_DT07/CH01110 ._CH',             # 1B
        'ED6_DT07/CH01610 ._CH',             # 1C
        'ED6_DT06/CH20090 ._CH',             # 1D
        'ED6_DT06/CH20091 ._CH',             # 1E
        'ED6_DT06/CH20147 ._CH',             # 1F
        'ED6_DT06/CH20099 ._CH',             # 20
        'ED6_DT06/CH20103 ._CH',             # 21
        'ED6_DT06/CH20107 ._CH',             # 22
        'ED6_DT06/CH20108 ._CH',             # 23
        'ED6_DT07/CH01570 ._CH',             # 24
        'ED6_DT06/CH20038 ._CH',             # 25
        'ED6_DT07/CH00003 ._CH',             # 26
        'ED6_DT07/CH00013 ._CH',             # 27
        'ED6_DT07/CH01050 ._CH',             # 28
        'ED6_DT07/CH01690 ._CH',             # 29
        'ED6_DT07/CH02640 ._CH',             # 2A
        'ED6_DT07/CH01020 ._CH',             # 2B
        'ED6_DT07/CH01490 ._CH',             # 2C
        'ED6_DT07/CH01180 ._CH',             # 2D
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT07/CH02190P._CP',             # 01
        'ED6_DT07/CH01540P._CP',             # 02
        'ED6_DT07/CH01640P._CP',             # 03
        'ED6_DT07/CH02510P._CP',             # 04
        'ED6_DT07/CH02520P._CP',             # 05
        'ED6_DT07/CH02530P._CP',             # 06
        'ED6_DT07/CH01630P._CP',             # 07
        'ED6_DT07/CH02050P._CP',             # 08
        'ED6_DT07/CH00110P._CP',             # 09
        'ED6_DT06/CH20101P._CP',             # 0A
        'ED6_DT07/CH01200P._CP',             # 0B
        'ED6_DT07/CH02630P._CP',             # 0C
        'ED6_DT07/CH01150P._CP',             # 0D
        'ED6_DT07/CH01040P._CP',             # 0E
        'ED6_DT07/CH01120P._CP',             # 0F
        'ED6_DT07/CH02480P._CP',             # 10
        'ED6_DT07/CH02490P._CP',             # 11
        'ED6_DT07/CH01480P._CP',             # 12
        'ED6_DT07/CH01143P._CP',             # 13
        'ED6_DT07/CH01350P._CP',             # 14
        'ED6_DT07/CH01030P._CP',             # 15
        'ED6_DT07/CH01070P._CP',             # 16
        'ED6_DT06/CH20101P._CP',             # 17
        'ED6_DT07/CH01470P._CP',             # 18
        'ED6_DT07/CH01100P._CP',             # 19
        'ED6_DT07/CH01210P._CP',             # 1A
        'ED6_DT07/CH01110P._CP',             # 1B
        'ED6_DT07/CH01610P._CP',             # 1C
        'ED6_DT06/CH20090P._CP',             # 1D
        'ED6_DT06/CH20091P._CP',             # 1E
        'ED6_DT06/CH20147P._CP',             # 1F
        'ED6_DT06/CH20099P._CP',             # 20
        'ED6_DT06/CH20103P._CP',             # 21
        'ED6_DT06/CH20107P._CP',             # 22
        'ED6_DT06/CH20108P._CP',             # 23
        'ED6_DT07/CH01570P._CP',             # 24
        'ED6_DT06/CH20038P._CP',             # 25
        'ED6_DT07/CH00003P._CP',             # 26
        'ED6_DT07/CH00013P._CP',             # 27
        'ED6_DT07/CH01050P._CP',             # 28
        'ED6_DT07/CH01690P._CP',             # 29
        'ED6_DT07/CH02640P._CP',             # 2A
        'ED6_DT07/CH01020P._CP',             # 2B
        'ED6_DT07/CH01490P._CP',             # 2C
        'ED6_DT07/CH01180P._CP',             # 2D
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 109490,
        Z                   = 1450,
        Y                   = 23040,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 1,
    )

    DeclNpc(
        X                   = 109630,
        Z                   = 1500,
        Y                   = 33010,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 2,
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
        X                   = 70000,
        Z                   = 250,
        Y                   = 69110,
        Direction           = 18,
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
        X                   = 79960,
        Z                   = 250,
        Y                   = 69120,
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
        X                   = 76080,
        Z                   = 250,
        Y                   = -7320,
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
        X                   = 65990,
        Z                   = 250,
        Y                   = -7150,
        Direction           = 360,
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
        X                   = 44730,
        Z                   = 250,
        Y                   = 46870,
        Direction           = 90,
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
        X                   = 44900,
        Z                   = 250,
        Y                   = 28910,
        Direction           = 90,
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
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 18,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 19,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 20,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 21,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 22,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 23,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 24,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 25,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 26,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 27,
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
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 3,
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
        X                   = 107860,
        Z                   = 1250,
        Y                   = 32850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 74970,
        Z                   = 0,
        Y                   = 69190,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 71040,
        Z                   = 0,
        Y                   = -6930,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 105230,
        Z                   = 1250,
        Y                   = 36670,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 101110,
        Z                   = 250,
        Y                   = 31490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 104590,
        Z                   = 1000,
        Y                   = 29040,
        Direction           = 24,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 99900,
        Z                   = 250,
        Y                   = 35240,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 101180,
        Z                   = 250,
        Y                   = 36470,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 70490,
        Z                   = 250,
        Y                   = 6990,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 71500,
        Z                   = 750,
        Y                   = 7870,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 37580,
        Z                   = 1250,
        Y                   = 49800,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 40270,
        Z                   = 1250,
        Y                   = 51990,
        Direction           = 91,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 40960,
        Z                   = 1250,
        Y                   = 50060,
        Direction           = 169,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 36250,
        Z                   = 1250,
        Y                   = 42940,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 38980,
        Z                   = 1250,
        Y                   = 41620,
        Direction           = 254,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 81160,
        Z                   = 0,
        Y                   = -2940,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 69020,
        Z                   = 250,
        Y                   = 4960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 63010,
        Z                   = 0,
        Y                   = 62930,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 93700,
        Z                   = 0,
        Y                   = 32900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 47210,
        Z                   = 250,
        Y                   = 4820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 250,
        Y                   = 10090,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 93700,
        Z                   = 0,
        Y                   = 32900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 47210,
        Z                   = 250,
        Y                   = 4820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 54000,
        Z                   = 250,
        Y                   = 10090,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 48190,
        Z                   = 250,
        Y                   = 52050,
        Direction           = 111,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 48120,
        Z                   = 250,
        Y                   = 51230,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 48030,
        Z                   = 250,
        Y                   = 47650,
        Direction           = 248,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 48730,
        Z                   = 250,
        Y                   = 44340,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 48460,
        Z                   = 250,
        Y                   = 45120,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 53030,
        Z                   = 250,
        Y                   = 48510,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 53030,
        Z                   = 250,
        Y                   = 47600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 40260,
        Z                   = 1250,
        Y                   = 49220,
        Direction           = 226,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 41010,
        Z                   = 1250,
        Y                   = 49820,
        Direction           = 206,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 44130,
        Z                   = 250,
        Y                   = 67000,
        Direction           = 185,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 47760,
        Z                   = 250,
        Y                   = 74930,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 48690,
        Z                   = 250,
        Y                   = 75760,
        Direction           = 293,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 56730,
        Z                   = 250,
        Y                   = 24550,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 55820,
        Z                   = 250,
        Y                   = 23780,
        Direction           = 36,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 58580,
        Z                   = 1250,
        Y                   = 24420,
        Direction           = 276,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 53090,
        Z                   = 250,
        Y                   = 21320,
        Direction           = 269,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = 48730,
        Z                   = 250,
        Y                   = 35180,
        Direction           = 136,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = 68250,
        Z                   = 0,
        Y                   = 1870,
        Direction           = 35,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 69310,
        Z                   = 250,
        Y                   = 3150,
        Direction           = 211,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 46,
    )

    DeclNpc(
        X                   = 72270,
        Z                   = 0,
        Y                   = 2150,
        Direction           = 142,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 47,
    )

    DeclNpc(
        X                   = 70950,
        Z                   = 0,
        Y                   = -1170,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 48,
    )

    DeclNpc(
        X                   = 51120,
        Z                   = 0,
        Y                   = 1090,
        Direction           = 214,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 49,
    )

    DeclNpc(
        X                   = 56190,
        Z                   = 250,
        Y                   = 6020,
        Direction           = 215,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 50,
    )

    DeclNpc(
        X                   = 61700,
        Z                   = 250,
        Y                   = 3050,
        Direction           = 189,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 51,
    )

    DeclNpc(
        X                   = 48860,
        Z                   = 250,
        Y                   = 8420,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 52,
    )

    DeclNpc(
        X                   = 49200,
        Z                   = 250,
        Y                   = 9460,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 53,
    )

    DeclNpc(
        X                   = 48880,
        Z                   = 250,
        Y                   = 15620,
        Direction           = 63,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 54,
    )

    DeclNpc(
        X                   = 69950,
        Z                   = 250,
        Y                   = 60930,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 55,
    )

    DeclNpc(
        X                   = 59720,
        Z                   = 250,
        Y                   = 66950,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 56,
    )

    DeclNpc(
        X                   = 60800,
        Z                   = 250,
        Y                   = 66950,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 57,
    )

    DeclNpc(
        X                   = 51510,
        Z                   = 0,
        Y                   = 67330,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 58,
    )

    DeclNpc(
        X                   = 17760,
        Z                   = 0,
        Y                   = 63880,
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
        X                   = 29270,
        Z                   = 0,
        Y                   = -950,
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
        X                   = 51010,
        Z                   = 0,
        Y                   = 102170,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 73540,
        Y                   = -1000,
        Z                   = 49000,
        Range               = 66420,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xA028,
        Unknown_18          = 0x0,
        Unknown_1C          = 33,
    )

    DeclEvent(
        X                   = 37600,
        Y                   = -1000,
        Z                   = 49280,
        Range               = 5000,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = 109720,
        Y                   = 1000,
        Z                   = 32980,
        Range               = 2000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 42,
    )

    DeclEvent(
        X                   = 76740,
        Y                   = 1000,
        Z                   = 23010,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = 69950,
        Y                   = 1000,
        Z                   = 14290,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = 63260,
        Y                   = 1000,
        Z                   = 22960,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = 69910,
        Y                   = 1000,
        Z                   = 31710,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = 42920,
        Y                   = 0,
        Z                   = 81110,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 44,
    )

    DeclEvent(
        X                   = 70940,
        Y                   = 0,
        Z                   = -9490,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 45,
    )

    DeclEvent(
        X                   = 75010,
        Y                   = 0,
        Z                   = 71300,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 46,
    )


    DeclActor(
        TriggerX            = 124880,
        TriggerZ            = -3500,
        TriggerY            = 70940,
        TriggerRange        = 800,
        ActorX              = 124880,
        ActorZ              = -2500,
        ActorY              = 70940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75060,
        TriggerZ            = 0,
        TriggerY            = 71950,
        TriggerRange        = 800,
        ActorX              = 75060,
        ActorZ              = 1000,
        ActorY              = 71950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 39,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 70950,
        TriggerZ            = 0,
        TriggerY            = -9930,
        TriggerRange        = 800,
        ActorX              = 70950,
        ActorZ              = 1000,
        ActorY              = -9930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 40,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 108180,
        TriggerZ            = 1250,
        TriggerY            = 23100,
        TriggerRange        = 800,
        ActorX              = 109490,
        ActorZ              = 2950,
        ActorY              = 23040,
        Flags               = 0x7E,
        TalkScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72040,
        TriggerZ            = 250,
        TriggerY            = 44930,
        TriggerRange        = 3000,
        ActorX              = 74100,
        ActorZ              = 750,
        ActorY              = 45100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68020,
        TriggerZ            = 250,
        TriggerY            = 44970,
        TriggerRange        = 3000,
        ActorX              = 66070,
        ActorZ              = 750,
        ActorY              = 45100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38820,
        TriggerZ            = 1250,
        TriggerY            = 36920,
        TriggerRange        = 800,
        ActorX              = 38820,
        ActorZ              = 2250,
        ActorY              = 36920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 41,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_ED6",          # 00, 0
        "Function_1_146C",         # 01, 1
        "Function_2_178A",         # 02, 2
        "Function_3_1912",         # 03, 3
        "Function_4_1936",         # 04, 4
        "Function_5_195A",         # 05, 5
        "Function_6_1A47",         # 06, 6
        "Function_7_1C50",         # 07, 7
        "Function_8_1D30",         # 08, 8
        "Function_9_1DDD",         # 09, 9
        "Function_10_1E82",        # 0A, 10
        "Function_11_20DF",        # 0B, 11
        "Function_12_21E4",        # 0C, 12
        "Function_13_2271",        # 0D, 13
        "Function_14_23D3",        # 0E, 14
        "Function_15_2437",        # 0F, 15
        "Function_16_3632",        # 10, 16
        "Function_17_3BE0",        # 11, 17
        "Function_18_3E44",        # 12, 18
        "Function_19_3EDA",        # 13, 19
        "Function_20_3F20",        # 14, 20
        "Function_21_3F66",        # 15, 21
        "Function_22_3FD4",        # 16, 22
        "Function_23_4042",        # 17, 23
        "Function_24_4088",        # 18, 24
        "Function_25_40CE",        # 19, 25
        "Function_26_413C",        # 1A, 26
        "Function_27_41AA",        # 1B, 27
        "Function_28_4218",        # 1C, 28
        "Function_29_4FC3",        # 1D, 29
        "Function_30_521B",        # 1E, 30
        "Function_31_6C4D",        # 1F, 31
        "Function_32_6F30",        # 20, 32
        "Function_33_7032",        # 21, 33
        "Function_34_70BA",        # 22, 34
        "Function_35_9FCD",        # 23, 35
        "Function_36_AC88",        # 24, 36
        "Function_37_AC92",        # 25, 37
        "Function_38_B0D9",        # 26, 38
        "Function_39_B196",        # 27, 39
        "Function_40_B1E0",        # 28, 40
        "Function_41_B22A",        # 29, 41
        "Function_42_B2BD",        # 2A, 42
        "Function_43_B2C1",        # 2B, 43
        "Function_44_B2C5",        # 2C, 44
        "Function_45_B2C9",        # 2D, 45
        "Function_46_B2CD",        # 2E, 46
    )


    def Function_0_ED6(): pass

    label("Function_0_ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_EF2")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 13)

    label("loc_EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_F05")
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 15)

    label("loc_F05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_F13")
    OP_A3(0x3FC)
    Event(0, 16)

    label("loc_F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_F21")
    OP_A3(0x3FD)
    Event(0, 28)

    label("loc_F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 6)), scpexpr(EXPR_END)), "loc_F2F")
    OP_A3(0x3FE)
    Event(0, 30)

    label("loc_F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 7)), scpexpr(EXPR_END)), "loc_F42")
    SetMapFlags(0x10000000)
    OP_A3(0x3FF)
    Event(0, 31)

    label("loc_F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_F5E")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3F0)
    Event(0, 32)

    label("loc_F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_F77")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 35)

    label("loc_F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1104")
    SetChrFlags(0x2B, 0x10)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrPos(0x24, 37580, 1250, 48810, 279)
    SetChrPos(0x27, 38460, 1250, 48810, 90)
    SetChrPos(0x28, 39430, 1250, 48810, 270)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2E, 36280, 1250, 42890, 45)
    SetChrPos(0x2C, 37150, 1250, 43970, 225)
    SetChrPos(0x2D, 40850, 1250, 45260, 0)
    SetChrPos(0x2F, 40050, 1250, 45290, 0)
    SetChrFlags(0x2D, 0x10)
    SetChrFlags(0x2F, 0x10)
    OP_43(0x2D, 0x0, 0x0, 0x2)
    OP_43(0x2F, 0x0, 0x0, 0x2)
    OP_43(0x31, 0x0, 0x0, 0x7)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    OP_43(0x35, 0x0, 0x0, 0xC)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    SetChrFlags(0x3C, 0x10)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x10)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x4A, 0x80)
    SetChrFlags(0x4A, 0x10)
    ClearChrFlags(0x4B, 0x80)
    SetChrFlags(0x4B, 0x10)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4E, 0x80)
    ClearChrFlags(0x4F, 0x80)
    SetChrFlags(0x4F, 0x10)
    ClearChrFlags(0x50, 0x80)
    ClearChrFlags(0x51, 0x80)
    ClearChrFlags(0x52, 0x80)
    ClearChrFlags(0x53, 0x80)
    ClearChrFlags(0x54, 0x80)
    ClearChrFlags(0x55, 0x80)
    SetChrFlags(0x55, 0x10)
    ClearChrFlags(0x56, 0x80)
    SetChrFlags(0x56, 0x10)
    ClearChrFlags(0x57, 0x80)
    Jump("loc_146B")

    label("loc_1104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_11A8")
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrPos(0x24, 48500, 250, 41910, 90)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2E, 36280, 1250, 42890, 45)
    SetChrPos(0x2C, 37150, 1250, 43970, 225)
    SetChrFlags(0x2E, 0x10)
    SetChrFlags(0x2C, 0x10)
    SetChrPos(0x2D, 40150, 1250, 48060, 180)
    SetChrPos(0x2F, 40150, 1250, 46580, 0)
    OP_43(0x2D, 0x0, 0x0, 0x2)
    OP_43(0x2F, 0x0, 0x0, 0x2)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    Jump("loc_146B")

    label("loc_11A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1262")
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrPos(0x24, 53110, 250, 44970, 270)
    SetChrPos(0x25, 53210, 250, 25020, 270)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2E, 36280, 1250, 42890, 45)
    SetChrPos(0x2C, 37150, 1250, 43970, 225)
    SetChrFlags(0x2E, 0x10)
    SetChrFlags(0x2C, 0x10)
    SetChrPos(0x2D, 40150, 1250, 48060, 180)
    SetChrPos(0x2F, 40150, 1250, 46580, 0)
    SetChrFlags(0x2D, 0x10)
    SetChrFlags(0x2F, 0x10)
    OP_43(0x2D, 0x0, 0x0, 0x2)
    OP_43(0x2F, 0x0, 0x0, 0x2)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    Jump("loc_146B")

    label("loc_1262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1306")
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrPos(0x24, 48500, 250, 41910, 90)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x25, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2E, 36280, 1250, 42890, 45)
    SetChrPos(0x2C, 37150, 1250, 43970, 225)
    SetChrPos(0x2D, 40150, 1250, 48060, 180)
    SetChrPos(0x2F, 40150, 1250, 46580, 0)
    SetChrFlags(0x2D, 0x10)
    SetChrFlags(0x2F, 0x10)
    OP_43(0x2D, 0x0, 0x0, 0x2)
    OP_43(0x2F, 0x0, 0x0, 0x2)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    Jump("loc_146B")

    label("loc_1306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1357")
    SetChrPos(0x2C, 40920, 1250, 52020, 190)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2F, 38410, 1250, 45900, 45)
    SetChrFlags(0x2F, 0x10)
    OP_43(0x2F, 0x0, 0x0, 0x2)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    Jump("loc_146B")

    label("loc_1357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_13CA")
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    SetChrPos(0x28, 72000, 250, 44380, 0)
    SetChrPos(0x27, 72000, 250, 45900, 180)
    SetChrPos(0x24, 48500, 250, 41910, 90)
    SetChrPos(0x26, 99020, 250, 30860, 270)
    SetChrPos(0x25, 100930, 250, 35130, 315)
    Jump("loc_146B")

    label("loc_13CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_13D4")
    Jump("loc_146B")

    label("loc_13D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1450")
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, 39000, 1250, 49410, 270)
    OP_43(0x1F, 0x0, 0x0, 0x2)
    SetChrPos(0x28, 72000, 250, 44380, 0)
    SetChrPos(0x27, 72000, 250, 45900, 180)
    SetChrPos(0x24, 40440, 1250, 49390, 270)
    SetChrPos(0x26, 99020, 250, 30860, 270)
    SetChrPos(0x25, 100930, 250, 35130, 315)
    Jump("loc_146B")

    label("loc_1450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_145A")
    Jump("loc_146B")

    label("loc_145A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1464")
    Jump("loc_146B")

    label("loc_1464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_146B")

    label("loc_146B")

    Return()

    # Function_0_ED6 end

    def Function_1_146C(): pass

    label("Function_1_146C")

    OP_16(0x2, 0xFA0, 0xFFFF4C50, 0xFFFEA070, 0x3005C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B1")
    OP_B1("t4101_y")
    Jump("loc_14D0")

    label("loc_14B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_14C7")
    OP_B1("t4101_y")
    OP_A3(0x3F1)
    Jump("loc_14D0")

    label("loc_14C7")

    OP_B1("t4101_n")

    label("loc_14D0")

    OP_72(0xE, 0x20)
    OP_72(0xF, 0x20)
    OP_6F(0xE, 118)
    OP_6F(0xF, 118)
    OP_72(0x5, 0x10)
    OP_72(0x8, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x7, 0x10)
    OP_72(0x9, 0x10)
    OP_72(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1544")
    OP_1B(0xA, 0x2, 0x2)
    OP_6F(0x6, 60)
    OP_6F(0x7, 60)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_1549")

    label("loc_1544")

    SetChrFlags(0xB, 0x80)

    label("loc_1549")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1562")
    OP_72(0xB, 0x10)
    OP_65(0x0, 0x1)

    label("loc_1562")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1575")
    OP_1B(0x9, 0x0, 0x26)

    label("loc_1575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159F")
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x2, 0x10)
    OP_72(0x3, 0x10)
    OP_72(0xB, 0x10)
    OP_72(0x4, 0x10)

    label("loc_159F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1675")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    OP_43(0xF, 0x1, 0x0, 0x11)
    OP_43(0x10, 0x1, 0x0, 0x11)
    OP_43(0x11, 0x1, 0x0, 0x11)
    OP_43(0x12, 0x1, 0x0, 0x11)
    OP_43(0x13, 0x1, 0x0, 0x11)
    OP_43(0x14, 0x1, 0x0, 0x11)
    OP_43(0x15, 0x1, 0x0, 0x11)
    OP_43(0x16, 0x1, 0x0, 0x11)
    OP_43(0x17, 0x1, 0x0, 0x11)
    OP_43(0x18, 0x1, 0x0, 0x11)
    OP_43(0x19, 0x1, 0x0, 0x11)
    OP_43(0x1A, 0x1, 0x0, 0x11)
    OP_43(0x1B, 0x1, 0x0, 0x11)
    OP_43(0x1C, 0x1, 0x0, 0x11)
    OP_43(0x1D, 0x1, 0x0, 0x11)
    OP_43(0x1E, 0x1, 0x0, 0x11)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_1681")
    OP_72(0x10, 0x4)

    label("loc_1681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1781")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "map\\\\mp016_00.eff")
    PlayEffect(0x0, 0x4, 0xFF, 45590, 250, 45800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 55330, 250, 22770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 70130, 250, 6410, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 86040, 250, 22980, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1789")

    label("loc_1781")

    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)

    label("loc_1789")

    Return()

    # Function_1_146C end

    def Function_2_178A(): pass

    label("Function_2_178A")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17BA")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_18FC")

    label("loc_17BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D3")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_18FC")

    label("loc_17D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17EC")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_18FC")

    label("loc_17EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1805")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_18FC")

    label("loc_1805")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_181E")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_18FC")

    label("loc_181E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1837")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_18FC")

    label("loc_1837")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1850")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_18FC")

    label("loc_1850")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1869")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_18FC")

    label("loc_1869")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1882")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_18FC")

    label("loc_1882")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_18FC")

    label("loc_189B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B4")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_18FC")

    label("loc_18B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18CD")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_18FC")

    label("loc_18CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E6")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_18FC")

    label("loc_18E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18FC")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_18FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1911")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_18FC")

    label("loc_1911")

    Return()

    # Function_2_178A end

    def Function_3_1912(): pass

    label("Function_3_1912")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1935")
    OP_8D(0xFE, 39320, 51160, 42580, 48520, 3000)
    Jump("Function_3_1912")

    label("loc_1935")

    Return()

    # Function_3_1912 end

    def Function_4_1936(): pass

    label("Function_4_1936")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1959")
    OP_8D(0xFE, 37230, 39170, 41090, 44360, 4000)
    Jump("Function_4_1936")

    label("loc_1959")

    Return()

    # Function_4_1936 end

    def Function_5_195A(): pass

    label("Function_5_195A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A46")
    OP_8E(0xFE, 0xCCF6, 0x0, 0xFFFFF484, 0x9C4, 0x0)
    OP_8E(0xFE, 0xC472, 0x0, 0x8C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xC472, 0x0, 0xF32A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xCFE4, 0x0, 0x100A4, 0x9C4, 0x0)
    OP_8E(0xFE, 0x15AC2, 0x0, 0xFCBC, 0x9C4, 0x0)
    OP_8E(0xFE, 0x16314, 0x0, 0xFB86, 0x9C4, 0x0)
    OP_8E(0xFE, 0x164E0, 0x0, 0x826E, 0x9C4, 0x0)
    OP_8C(0x30, 90, 400)
    Sleep(4000)
    OP_8E(0xFE, 0x164E0, 0x0, 0x7E86, 0x9C4, 0x0)
    OP_8C(0x30, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x16152, 0x0, 0x4CE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x15B12, 0x0, 0xFFFFF8BC, 0x9C4, 0x0)
    Jump("Function_5_195A")

    label("loc_1A46")

    Return()

    # Function_5_195A end

    def Function_6_1A47(): pass

    label("Function_6_1A47")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C4F")
    OP_8E(0xFE, 0xD6EC, 0xFA, 0x1360, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6EC, 0xFA, 0x59EC, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEA2E, 0x4E2, 0x59EC, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEA2E, 0x4E2, 0x84B2, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFA5A, 0x4E2, 0x8CC8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10928, 0x4E2, 0x8CC8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x11148, 0x4E2, 0x9470, 0x9C4, 0x0)
    OP_8E(0xFE, 0x111CA, 0x4E2, 0xCAB2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x130BA, 0x4E2, 0xCAB2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x130BA, 0x4E2, 0xBA36, 0x9C4, 0x0)
    OP_8E(0xFE, 0x138D0, 0x4E2, 0xABF4, 0x9C4, 0x0)
    OP_8E(0xFE, 0x138D0, 0x4E2, 0x2DBE, 0x9C4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B71")
    OP_62(0x31, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(500)
    OP_8C(0x31, 225, 400)
    OP_A2(0x15)
    OP_4A(0x31, 255)

    label("loc_1B71")

    OP_8E(0xFE, 0x11968, 0x4E2, 0x2DBE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10CE8, 0x4E2, 0x272E, 0x9C4, 0x0)
    OP_8C(0x31, 180, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C33")
    TurnDirection(0x29, 0x31, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1BD8")
    OP_62(0x29, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(500)
    OP_A2(0xC)
    Jump("loc_1C27")

    label("loc_1BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1C01")
    OP_62(0x29, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(500)
    OP_A2(0xB)
    Jump("loc_1C27")

    label("loc_1C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1C27")
    OP_62(0x29, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(500)
    OP_A2(0xA)

    label("loc_1C27")

    Sleep(500)
    OP_8C(0x29, 180, 400)

    label("loc_1C33")

    Sleep(1500)
    OP_8E(0xFE, 0x10CE8, 0xFA, 0x16C6, 0x9C4, 0x0)
    Jump("Function_6_1A47")

    label("loc_1C4F")

    Return()

    # Function_6_1A47 end

    def Function_7_1C50(): pass

    label("Function_7_1C50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D2F")
    OP_8E(0xFE, 0xD6EC, 0xFA, 0x1360, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6EC, 0xFA, 0xE68C, 0x9C4, 0x0)
    OP_8E(0xFE, 0x14C26, 0xFA, 0xE68C, 0x9C4, 0x0)
    OP_8E(0xFE, 0x14C26, 0xFA, 0x59D8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x1390C, 0x4E2, 0x59D8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x138D0, 0x4E2, 0x2DBE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x11968, 0x4E2, 0x2DBE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10CE8, 0x4E2, 0x272E, 0x9C4, 0x0)
    OP_8C(0x31, 0, 400)
    TurnDirection(0x29, 0x31, 400)
    Sleep(500)
    OP_8C(0x29, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x10CE8, 0xFA, 0x16C6, 0x9C4, 0x0)
    Jump("Function_7_1C50")

    label("loc_1D2F")

    Return()

    # Function_7_1C50 end

    def Function_8_1D30(): pass

    label("Function_8_1D30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DDC")
    OP_8E(0xFE, 0xCE9A, 0x0, 0xF5D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCB0C, 0x0, 0xF258, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCB0C, 0x0, 0x816, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCEEA, 0x0, 0x33E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15590, 0x0, 0x33E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x158D8, 0x0, 0x6B8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x158D8, 0x0, 0xEF56, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15572, 0x28, 0xF5D2, 0x7D0, 0x0)
    Jump("Function_8_1D30")

    label("loc_1DDC")

    Return()

    # Function_8_1D30 end

    def Function_9_1DDD(): pass

    label("Function_9_1DDD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E81")
    OP_8E(0xFE, 0x16E04, 0x0, 0x9DBC, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x16E04, 0x0, 0x8084, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x16E04, 0x0, 0x61EE, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x16E04, 0x0, 0x8084, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    Jump("Function_9_1DDD")

    label("loc_1E81")

    Return()

    # Function_9_1DDD end

    def Function_10_1E82(): pass

    label("Function_10_1E82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20DE")
    OP_8E(0xFE, 0xB86A, 0xFA, 0xE60A, 0x9C4, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xA80C, 0xFA, 0xE9F2, 0x9C4, 0x0)
    OP_8E(0xFE, 0xA80C, 0xFA, 0x10D56, 0x9C4, 0x0)
    OP_8E(0xFE, 0xB7B6, 0xFA, 0x10D56, 0x9C4, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xB7B6, 0xFA, 0x13CAE, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xD67E, 0xFA, 0x13CAE, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD67E, 0xFA, 0x10CDE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x11BB6, 0xFA, 0x10CDE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x12502, 0x0, 0x1061C, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x15694, 0xFA, 0x1061C, 0x9C4, 0x0)
    OP_8E(0xFE, 0x15CAC, 0xFA, 0x10A90, 0x9C4, 0x0)
    OP_8E(0xFE, 0x16F44, 0xFA, 0x109D2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x16F44, 0xFA, 0xAE88, 0x9C4, 0x0)
    OP_8E(0xFE, 0x17E3A, 0xFA, 0xAE88, 0x9C4, 0x0)
    OP_8E(0xFE, 0x17E3A, 0xFA, 0x53E8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x16F3A, 0xFA, 0x53E8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x16F3A, 0xFA, 0x143C, 0x9C4, 0x0)
    OP_8E(0xFE, 0x16396, 0x0, 0xB86, 0x9C4, 0x0)
    OP_8E(0xFE, 0x16396, 0x0, 0xFFFFF43E, 0x9C4, 0x0)
    OP_8E(0xFE, 0x11C56, 0x0, 0xFFFFF43E, 0x9C4, 0x0)
    OP_8E(0xFE, 0x11580, 0x0, 0xFFFFEDF4, 0x9C4, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x10F68, 0x0, 0xFFFFF43E, 0x9C4, 0x0)
    OP_8E(0xFE, 0xB5CC, 0x0, 0xFFFFF43E, 0x9C4, 0x0)
    OP_8E(0xFE, 0xA9F6, 0x0, 0xFFFFFC7C, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xA938, 0xFA, 0x1342, 0x9C4, 0x0)
    OP_8E(0xFE, 0xBAEA, 0xFA, 0x139C, 0x9C4, 0x0)
    Jump("Function_10_1E82")

    label("loc_20DE")

    Return()

    # Function_10_1E82 end

    def Function_11_20DF(): pass

    label("Function_11_20DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21E3")
    OP_8E(0xFE, 0xD2F0, 0xFA, 0x1086, 0x9C4, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x14F64, 0xFA, 0x1086, 0x9C4, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x14C44, 0xFA, 0xE6AA, 0x9C4, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x10F86, 0xFA, 0xE6AA, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10F86, 0x4E2, 0xD2AA, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEE7A, 0x4E2, 0xD2AA, 0x9C4, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xEE7A, 0x4E2, 0xB84C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6F6, 0xFA, 0xB84C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6F6, 0xFA, 0x6586, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD246, 0xFA, 0x5E24, 0x9C4, 0x0)
    Jump("Function_11_20DF")

    label("loc_21E3")

    Return()

    # Function_11_20DF end

    def Function_12_21E4(): pass

    label("Function_12_21E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2270")
    OP_8E(0xFE, 0xD1C4, 0xFA, 0xF32, 0x9C4, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x1502C, 0xFA, 0xF32, 0x9C4, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x1502C, 0xFA, 0xEACE, 0x9C4, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xD246, 0xFA, 0xEACE, 0x9C4, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(1500)
    Jump("Function_12_21E4")

    label("loc_2270")

    Return()

    # Function_12_21E4 end

    def Function_13_2271(): pass

    label("Function_13_2271")

    EventBegin(0x0)
    SetChrPos(0x8, 66340, 6500, -8490, 0)
    ClearChrFlags(0x8, 0x80)
    OP_6D(69990, 250, 45010, 0)
    OP_67(0, 13780, -10000, 0)
    OP_6B(1890, 0)
    OP_6C(315000, 0)
    OP_6E(576, 0)
    OP_77(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    LoadEffect(0x0, "map\\\\mp014_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 69990, 250, 45010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 74960, 1650, 71540, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x1, 0x2, 0x0, 0xE)

    def lambda_235A():
        OP_6C(0, 11000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_235A)
    Sleep(3000)

    def lambda_236F():
        OP_6D(74960, 1650, 71540, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_236F)

    def lambda_2387():
        OP_67(0, 8880, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2387)

    def lambda_239F():
        OP_6B(3490, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_239F)

    def lambda_23AF():
        OP_6E(262, 8000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_23AF)
    Sleep(6000)
    SetPlaceName(0xBD) # 帝国大使馆
    Sleep(2000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4112   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2271 end

    def Function_14_23D3(): pass

    label("Function_14_23D3")

    Sleep(700)
    OP_24(0x1C9, 0x28)
    Sleep(300)
    OP_24(0x1C9, 0x32)
    Sleep(300)
    OP_24(0x1C9, 0x3C)
    Sleep(300)
    OP_24(0x1C9, 0x41)
    Sleep(300)
    OP_24(0x1C9, 0x46)
    Sleep(300)
    OP_24(0x1C9, 0x4B)
    Sleep(300)
    OP_24(0x1C9, 0x50)
    Sleep(300)
    OP_24(0x1C9, 0x55)
    Sleep(300)
    OP_24(0x1C9, 0x5A)
    Sleep(300)
    OP_24(0x1C9, 0x5F)
    Sleep(300)
    OP_24(0x1C9, 0x64)
    Return()

    # Function_14_23D3 end

    def Function_15_2437(): pass

    label("Function_15_2437")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(110500, 8440, 40040, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(69000, 0)
    OP_6E(446, 0)
    SetChrPos(0x101, 108200, 1250, 33360, 0)
    SetChrPos(0x102, 108300, 1250, 31990, 0)
    SetChrPos(0x108, 106150, 1250, 33250, 0)
    SetChrPos(0x104, 106480, 1250, 31500, 0)
    TurnDirection(0x101, 0x108, 0)
    TurnDirection(0x102, 0x108, 0)
    TurnDirection(0x104, 0x101, 0)
    TurnDirection(0x108, 0x101, 0)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x30, 0x80)
    FadeToBright(2000, 0)

    def lambda_2508():
        OP_6D(108600, 1250, 33560, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2508)

    def lambda_2520():
        OP_6E(333, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2520)

    def lambda_2530():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2530)
    Sleep(5000)

    ChrTalk(
        0x108,
        (
            "#070F这样……\x01",
            "我们就顺利地进入第二轮了。\x02\x03",
            "虽然不知道能走多远，\x01",
            "不过明天也能继续保持这种气势就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5P那当然了！\x02\x03",
            "#007F不过从今天各队的战果来看，\x01",
            "剩下的都是强敌啊～\x02\x03",
            "协会的前辈、空贼团，\x01",
            "还有情报部的那些家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P是啊……\x01",
            "不做好充足的准备不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F没什么，不用担心啦。\x02\x03",
            "恋爱的力量是不会停止的。\x01",
            "不管什么障碍也能够突破的哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        "#509F#5P我根本听不懂你在说什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F今天我们要好好地养精蓄锐，\x01",
            "为明天的半决赛做好准备。\x02\x03",
            "我现在就去酒廊吃饭，\x01",
            "你们三个打算怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F呵呵……\x01",
            "本人很荣幸和你一起去。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F#2P（我们最好先向协会报告一下吧。）\x01",
            "　\x02\x03",
            "（说不定会得到和委托有关的情报。）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F#5P（啊，也是……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    TurnDirection(0x102, 0x104, 400)

    ChrTalk(
        0x101,
        (
            "#506F#5P不好意思，金先生。\x01",
            "我们两个就不跟你们去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F那么，今天就此分别吧。\x01",
            "　\x02\x03",
            "明天早上，我们还是在酒店集合。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FAu revoir.\x01",
            "可爱的小猫咪。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A40():

        label("loc_2A40")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2A40")

    QueueWorkItem2(0x102, 1, lambda_2A40)
    OP_8C(0x108, 270, 400)

    def lambda_2A58():
        OP_8E(0xFE, 0x1645E, 0x0, 0x843A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2A58)
    OP_8C(0x104, 270, 400)

    def lambda_2A7A():
        OP_8E(0xFE, 0x1645E, 0x0, 0x7C6A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A7A)
    Sleep(3000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F#5P那么……我们去协会吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#013F#2P……嗯……\x02\x03",
            "还有……\x01",
            "去哪里收集情报呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#5P哎……？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xC, 98320, 250, 32830, 90)
    SetChrPos(0xD, 97140, 250, 33540, 90)
    SetChrPos(0xE, 96950, 250, 32180, 90)

    NpcTalk(
        0xC,
        "青年的声音",
        (
            "#2P嘿嘿～\x01",
            "干嘛呆呆地站在那里啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2BF3():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BF3)

    def lambda_2C01():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C01)
    OP_6D(103750, 1250, 32810, 2000)

    def lambda_2C20():
        OP_8E(0xFE, 0x19D98, 0x4E2, 0x800C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2C20)
    Sleep(200)

    def lambda_2C40():
        OP_8E(0xFE, 0x19B2C, 0x4E2, 0x835E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2C40)
    Sleep(200)

    def lambda_2C60():
        OP_8E(0xFE, 0x19BD6, 0x4E2, 0x7BCA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2C60)
    OP_6D(107020, 1250, 33610, 3000)

    ChrTalk(
        0x101,
        (
            "#000F啊，是你们……\x01",
            "今天的比赛真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "哼……\x01",
            "可不要得意忘形哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这次是因为时间不够，\x01",
            "锻炼不够充分而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "下次再战的时候，我们一定会赢的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "哎～还要打吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈，可以啊。\x02\x03",
            "如果还有机会的话，\x01",
            "什么时候交手都可以哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F等一下，艾丝蒂尔……\x01",
            "这么轻易就答应下来，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F哎呀哎呀～有什么不好的。\x02\x03",
            "而且他们如果认真修行的话，\x01",
            "就没有空闲去做坏事了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "哼……\x01",
            "真是不知天高地厚的小鬼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "给你们这个吧，\x01",
            "拿好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0xC, 0x101, 0x4B0, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "地下水路的钥匙Ａ\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x36D, 1)
    OP_94(0x1, 0xC, 0xB4, 0x320, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        "#505F这、这是什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F好像是把很古老的钥匙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这个钥匙可以打开\x01",
            "西街区的那个栅栏门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "从那里能通往地下水路。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我们偶然得到了那把钥匙，\x01",
            "就每天去那里探险呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "里面盘踞着很强的魔兽，\x01",
            "是个不错的修行场所呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎，那么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "可、可不要搞错哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "你们赢得了胜利是你们的实力。\x01",
            "如果你们轻易输给别人，我们会很不甘心的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "听好了……一定要拿冠军哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "除此之外是绝不允许的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "那么，告辞了～\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 270, 400)

    def lambda_31BA():
        OP_8E(0xFE, 0x1645E, 0x0, 0x7C6A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_31BA)
    OP_8C(0xE, 270, 400)

    def lambda_31DC():
        OP_8E(0xFE, 0x1645E, 0x0, 0x7C6A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_31DC)
    OP_8C(0xC, 270, 400)

    def lambda_31FE():
        OP_8E(0xFE, 0x1645E, 0x0, 0x7C6A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_31FE)
    Sleep(3000)

    def lambda_321E():
        OP_6D(109230, 1250, 33610, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_321E)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F#5P哎～刚才难道是……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，好像是在鼓励我们呢。\x01",
            "　\x02\x03",
            "是让我们去那个地下水路锻炼，\x01",
            "为接下来的比赛做准备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#5P果、果然是这样啊。\x02\x03",
            "嗯……\x01",
            "他们果然是洗心革面了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈……\x01",
            "说不定是被你的大肚量所感染了哦。\x02\x03",
            "真是意外啊，\x01",
            "艾丝蒂尔很适合当他们的头儿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#5P大肚量……头儿……\x01",
            "真是让人高兴不起来呢。\x02\x03",
            "#007F不过算了，\x01",
            "我们就满怀感激地收下他们的好意吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过，今天已经这么晚了，\x01",
            "我们就不要去地下水路了吧。\x02\x03",
            "明天早上比赛之前\x01",
            "去试试身手反而会比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5P嗯，明白了。\x02\x03",
            "那么，我们就去协会\x01",
            "向艾南哥哥报告一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x61E)
    OP_28(0x47, 0x1, 0x40)
    OP_28(0x47, 0x1, 0x80)
    OP_28(0x47, 0x1, 0x100)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrPos(0x104, 107840, 1250, 25920, 0)
    SetChrPos(0x108, 107840, 1250, 25920, 0)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x30, 0x80)
    RemoveParty(0x7, 0xFF)
    RemoveParty(0x3, 0xFF)
    SetChrPos(0x101, 106440, 1250, 32490, 270)
    SetChrPos(0x102, 106440, 1250, 32490, 270)
    OP_6D(106440, 1250, 32490, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_15_2437 end

    def Function_16_3632(): pass

    label("Function_16_3632")

    EventBegin(0x0)
    OP_6D(110500, 8440, 40040, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(69000, 0)
    OP_6E(446, 0)
    SetChrPos(0x101, 108200, 1250, 33360, 0)
    SetChrPos(0x102, 108300, 1250, 31990, 0)
    SetChrPos(0x108, 106150, 1250, 33250, 0)
    SetChrPos(0x104, 106480, 1250, 31500, 0)
    TurnDirection(0x101, 0x108, 0)
    TurnDirection(0x102, 0x108, 0)
    TurnDirection(0x104, 0x101, 0)
    TurnDirection(0x108, 0x101, 0)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x30, 0x80)
    FadeToBright(2000, 0)

    def lambda_3703():
        OP_6D(108600, 1250, 33560, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3703)

    def lambda_371B():
        OP_6E(333, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_371B)

    def lambda_372B():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_372B)
    Sleep(5000)

    ChrTalk(
        0x101,
        (
            "#007F#5P呼……\x01",
            "不管怎么说，今天也赢了。\x02\x03",
            "#006F明天总算要进行决赛了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F要为即将到来的激烈战斗做准备，\x01",
            "必须得养精蓄锐才行啊。\x02\x03",
            "#071F所以……\x01",
            "今晚也去酒馆吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F呵呵，好主意。\x01",
            "我也和你一起去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#5P怎么觉得有点不对劲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P我们两个还有别的事，\x01",
            "所以今晚也不跟你们去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哦，那么就再见了。\x02\x03",
            "明天早上我还在酒店前台等着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#035F晚安，我的两个小甜心㈱\x02",
    )

    CloseMessageWindow()

    def lambda_39AC():

        label("loc_39AC")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_39AC")

    QueueWorkItem2(0x102, 1, lambda_39AC)
    OP_8C(0x108, 270, 400)

    def lambda_39C4():
        OP_8E(0xFE, 0x1645E, 0x0, 0x843A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_39C4)
    OP_8C(0x104, 270, 400)

    def lambda_39E6():
        OP_8E(0xFE, 0x1645E, 0x0, 0x7C6A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39E6)
    Sleep(3000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F#5P那么……\x02\x03",
            "奈尔一定在等着，\x01",
            "我们赶快去杂志社吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#2P是啊……\x02\x03",
            "如果能知道关于\x01",
            "情报部成员的一些事情就好了……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x48, 0x1, 0x20)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrPos(0x104, 107450, 1250, 31370, 0)
    SetChrPos(0x108, 107450, 1250, 31370, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x30, 0x80)
    RemoveParty(0x7, 0xFF)
    RemoveParty(0x3, 0xFF)
    SetChrPos(0x101, 106440, 1250, 32490, 270)
    SetChrPos(0x102, 106440, 1250, 32490, 270)
    OP_6D(106440, 1250, 32490, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_16_3632 end

    def Function_17_3BE0(): pass

    label("Function_17_3BE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E43")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C13")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D30")

    label("loc_3C13")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C39")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D30")

    label("loc_3C39")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C5F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D30")

    label("loc_3C5F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C86")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D30")

    label("loc_3C86")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CAC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D30")

    label("loc_3CAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CD2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D30")

    label("loc_3CD2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CF7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D30")

    label("loc_3CF7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D1C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D30")

    label("loc_3D1C")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D30")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E40")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    OP_69(0xFE, 0x3E8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E31")

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

    label("loc_3E31")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_3E40")

    Jump("Function_17_3BE0")

    label("loc_3E43")

    Return()

    # Function_17_3BE0 end

    def Function_18_3E44(): pass

    label("Function_18_3E44")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3ED9")
    SetChrPos(0xFE, 48010, 250, 59980, 270)
    OP_8E(0xFE, 0x8980, 0xFA, 0xEA4C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xBB8A, 0xFA, 0xEA4C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xBB8A, 0xFA, 0x10D6, 0xBB8, 0x0)
    OP_8E(0xFE, 0xA42E, 0xFA, 0x10D6, 0xBB8, 0x0)
    OP_8E(0xFE, 0xBB8A, 0xFA, 0x10D6, 0xBB8, 0x0)
    OP_8E(0xFE, 0xBB8A, 0xFA, 0xEA4C, 0xBB8, 0x0)
    Jump("Function_18_3E44")

    label("loc_3ED9")

    Return()

    # Function_18_3E44 end

    def Function_19_3EDA(): pass

    label("Function_19_3EDA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F1F")
    SetChrPos(0xFE, 39910, 0, 63710, 270)
    OP_8E(0xFE, 0x15E96, 0x0, 0xF8DE, 0xBB8, 0x0)
    OP_8E(0xFE, 0x9BE6, 0x0, 0xF8DE, 0xBB8, 0x0)
    Jump("Function_19_3EDA")

    label("loc_3F1F")

    Return()

    # Function_19_3EDA end

    def Function_20_3F20(): pass

    label("Function_20_3F20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F65")
    SetChrPos(0xFE, 50960, 0, 16800, 0)
    OP_8E(0xFE, 0xC710, 0x0, 0xE6D2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xC710, 0x0, 0x41A0, 0xBB8, 0x0)
    Jump("Function_20_3F20")

    label("loc_3F65")

    Return()

    # Function_20_3F20 end

    def Function_21_3F66(): pass

    label("Function_21_3F66")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FD3")
    SetChrPos(0xFE, 55970, 250, 6050, 0)
    OP_8E(0xFE, 0xDAA2, 0xFA, 0xE2E0, 0xBB8, 0x0)
    OP_8E(0xFE, 0x148CA, 0xFA, 0xE2E0, 0xBB8, 0x0)
    OP_8E(0xFE, 0x148CA, 0xFA, 0x1766, 0xBB8, 0x0)
    OP_8E(0xFE, 0xDAA2, 0xFA, 0x17A2, 0xBB8, 0x0)
    Jump("Function_21_3F66")

    label("loc_3FD3")

    Return()

    # Function_21_3F66 end

    def Function_22_3FD4(): pass

    label("Function_22_3FD4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4041")
    SetChrPos(0xFE, 53970, 250, 3940, 90)
    OP_8E(0xFE, 0x1502C, 0xFA, 0xF64, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1502C, 0xFA, 0xEA38, 0xBB8, 0x0)
    OP_8E(0xFE, 0xD2A0, 0xFA, 0xEA38, 0xBB8, 0x0)
    OP_8E(0xFE, 0xD2D2, 0xFA, 0xF64, 0xBB8, 0x0)
    Jump("Function_22_3FD4")

    label("loc_4041")

    Return()

    # Function_22_3FD4 end

    def Function_23_4042(): pass

    label("Function_23_4042")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4087")
    SetChrPos(0xFE, 54120, 250, 67800, 270)
    OP_8E(0xFE, 0x174F8, 0xFA, 0x108D8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xD368, 0xFA, 0x108D8, 0xBB8, 0x0)
    Jump("Function_23_4042")

    label("loc_4087")

    Return()

    # Function_23_4042 end

    def Function_24_4088(): pass

    label("Function_24_4088")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40CD")
    SetChrPos(0xFE, 95540, 250, -5740, 90)
    OP_8E(0xFE, 0xA6D6, 0xFA, 0xFFFFE994, 0xBB8, 0x0)
    OP_8E(0xFE, 0x17534, 0xFA, 0xFFFFE994, 0xBB8, 0x0)
    Jump("Function_24_4088")

    label("loc_40CD")

    Return()

    # Function_24_4088 end

    def Function_25_40CE(): pass

    label("Function_25_40CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_413B")
    SetChrPos(0xFE, 42960, 0, -1020, 90)
    OP_8E(0xFE, 0x15F86, 0x0, 0xFFFFFC04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x15F86, 0x0, 0xE57E, 0xBB8, 0x0)
    OP_8E(0xFE, 0x15F86, 0x0, 0xFFFFFC04, 0xBB8, 0x0)
    OP_8E(0xFE, 0xA7D0, 0x0, 0xFFFFFC04, 0xBB8, 0x0)
    Jump("Function_25_40CE")

    label("loc_413B")

    Return()

    # Function_25_40CE end

    def Function_26_413C(): pass

    label("Function_26_413C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41A9")
    SetChrPos(0xFE, 61020, 1250, 53050, 180)
    OP_8E(0xFE, 0xEE5C, 0x4E2, 0x9088, 0xBB8, 0x0)
    OP_8E(0xFE, 0x134C0, 0x4E2, 0x9088, 0xBB8, 0x0)
    OP_8E(0xFE, 0x134C0, 0x4E2, 0xCE4A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xEE5C, 0x4E2, 0xCF3A, 0xBB8, 0x0)
    Jump("Function_26_413C")

    label("loc_41A9")

    Return()

    # Function_26_413C end

    def Function_27_41AA(): pass

    label("Function_27_41AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4217")
    SetChrPos(0xFE, 77980, 1250, 52000, 180)
    OP_8E(0xFE, 0x1309C, 0x4E2, 0x945C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF262, 0x4E2, 0x945C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF262, 0x4E2, 0xCAF8, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1309C, 0x4E2, 0xCB20, 0xBB8, 0x0)
    Jump("Function_27_41AA")

    label("loc_4217")

    Return()

    # Function_27_41AA end

    def Function_28_4218(): pass

    label("Function_28_4218")

    EventBegin(0x0)
    OP_6D(69830, 1250, 37910, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(1750, 0)
    OP_6C(224000, 0)
    OP_6E(508, 0)
    SetChrPos(0x101, 68870, 1250, 37520, 0)
    SetChrPos(0x102, 70330, 1250, 37670, 0)

    def lambda_427F():
        OP_8E(0xFE, 0x10F5E, 0xFA, 0xAE38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_427F)
    Sleep(300)

    def lambda_429F():
        OP_8E(0xFE, 0x10EF0, 0xFA, 0xA92E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_429F)
    OP_6D(68880, 250, 42980, 3000)

    ChrTalk(
        0x101,
        (
            "呼……\x01",
            "躲避着巡逻的士兵，\x01",
            "没想到来到这种地方了呢。\x02\x03",
            "看起来，\x01",
            "这边好像已经没有士兵了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯……没有人的气息了。\x02\x03",
            "夜间的巡逻\x01",
            "也差不多该结束了吧。\x02\x03",
            "我们稍微休息一下就回旅馆吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FＯＫ。\x02",
    )

    CloseMessageWindow()

    def lambda_43F5():
        OP_8E(0xFE, 0x10374, 0xFA, 0xAE42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43F5)
    Sleep(400)

    def lambda_4415():
        OP_8E(0xFE, 0x1037E, 0xFA, 0xB1B2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4415)

    def lambda_4430():
        OP_67(0, 5940, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4430)
    OP_6D(66840, 250, 45270, 3000)

    ChrTalk(
        0x101,
        (
            "#000F啊～发生了这么多事，\x01",
            "脑子还处于不清醒状态呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哈哈……确实。\x02\x03",
            "没想到在大圣堂\x01",
            "等着我们的人是中尉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，对了……\x02\x03",
            "刚开始约修亚以为\x01",
            "送信的不是尤莉亚小姐吧？\x02\x03",
            "那是谁呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F………那是……………\x02\x03",
            "…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊……\x02\x03",
            "对不起，算我没说。\x02\x03",
            "犯规了犯规了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是最初的约定之一嘛。\x02\x03",
            "在约修亚愿意自己说出来之前，\x01",
            "不能问我们相遇前的事情。\x02\x03",
            "虽然我一直在注意，\x01",
            "不过还是不小心忘记了呢～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F…………………………………\x02\x03",
            "艾丝蒂尔，我……\x02\x03",
            "我，和你一起旅行，\x01",
            "觉得自己稍微变坚强了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F在同一片天空下生活的\x01",
            "各种各样的人，各种各样的人生……\x02\x03",
            "无数交织在一起的思念的轨迹……\x02\x03",
            "每当感受到这些，\x01",
            "就似乎找回了自己丢失的东西……\x02\x03",
            "这种感觉……真美好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F……约修亚……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F大概这是错觉吧。\x02\x03",
            "尽管如此，我也……\x02\x03",
            "我也要感谢\x01",
            "和你一起生活的这些日子……\x02\x03",
            "和这片天空，和父亲……\x02\x03",
            "当然还有艾丝蒂尔……你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F所以……我们约定。\x02\x03",
            "如果这次的事情能够结束，\x01",
            "父亲平安地回来的话……\x02\x03",
            "我就告诉你和你相遇之前的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F真、真的……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯。\x02\x03",
            "和这星空做个约定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F…………………………………\x02\x03",
            "……好，决定了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x10586, 0xFA, 0xAEE2, 0xBB8, 0x0)

    ChrTalk(
        0x102,
        "#010F艾丝蒂尔……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F该怎么说呢……\x01",
            "沉重的心情一扫而光呢。\x02\x03",
            "全部结束之后，\x01",
            "我也有话想对约修亚说呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哎……啊啊。\x02\x03",
            "难道是那个烦恼的事情？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F对对，就是那个。\x02\x03",
            "嘿嘿……\x01",
            "我已经做好准备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F准备……\x01",
            "是很让人烦恼的事情吗？\x02\x03",
            "那么现在说出来也……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不～行！\x02\x03",
            "说那种话，\x01",
            "果然还是要时机的。\x02\x03",
            "嗯～虽然现在\x01",
            "这个气氛相当的好呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F为了这个，\x01",
            "明天的比赛一定不能输……\x02\x03",
            "看我用少女的力量，\x01",
            "把那些特务兵们打飞！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F打飞……\x02\x03",
            "……呼……\x02\x03",
            "呼……啊哈哈哈……！\x02\x03",
            "你……果然……\x01",
            "……不愧是父亲的女儿啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F什么啊，这样说真是失礼呢。\x02\x03",
            "我跟那样的不良中年\x01",
            "到底有那点像啦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯……是啊。\x02\x03",
            "明天的比赛，\x01",
            "我也有取胜的信心了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4132   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_28_4218 end

    def Function_29_4FC3(): pass

    label("Function_29_4FC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x36E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_501A")
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
    Jump("loc_521A")

    label("loc_501A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51B2")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 0)), scpexpr(EXPR_END)), "loc_510D")

    ChrTalk(
        0x102,
        (
            "#010F今天已经很晚了，\x01",
            "就不要到地下水路去了。\x02\x03",
            "明天再和金先生他们一起进去看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51AC")

    label("loc_510D")


    ChrTalk(
        0x102,
        (
            "#010F看起来这里就是\x01",
            "艾南先生所说的地下水路的入口了。\x01",
            "　\x02\x03",
            "今天已经很晚了，\x01",
            "明天再和金先生他们一起进去看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51AC")

    TalkEnd(0xFF)
    Jump("loc_521A")

    label("loc_51B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_521A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x73, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "使用了\x07\x02",
            "地下水路的钥匙Ｂ\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x630)
    OP_64(0x0, 0x1)
    OP_71(0xB, 0x10)
    TalkEnd(0xFF)

    label("loc_521A")

    Return()

    # Function_29_4FC3 end

    def Function_30_521B(): pass

    label("Function_30_521B")

    EventBegin(0x0)
    OP_6D(110500, 8440, 40040, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(69000, 0)
    OP_6E(446, 0)
    SetChrPos(0x101, 108200, 1250, 33060, 0)
    SetChrPos(0x102, 108300, 1250, 31690, 0)
    SetChrPos(0x108, 106860, 1250, 33260, 0)
    SetChrPos(0x104, 106480, 1250, 31500, 0)
    TurnDirection(0x101, 0x108, 0)
    TurnDirection(0x102, 0x108, 0)
    TurnDirection(0x104, 0x101, 0)
    TurnDirection(0x108, 0x101, 0)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x33, 0x80)
    OP_4A(0x34, 255)
    FadeToBright(2000, 0)

    def lambda_52F5():
        OP_6D(108600, 1250, 33260, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52F5)

    def lambda_530D():
        OP_6E(333, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_530D)

    def lambda_531D():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_531D)
    Sleep(5000)

    ChrTalk(
        0x101,
        (
            "#001F#5P哈啊～该怎么说呢。\x01",
            "真是激烈的战斗啊。\x02\x03",
            "那个洛伦斯少尉比想象中还要厉害呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P嗯……终于赢了。\x02\x03",
            "到现在我还不敢相信呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#074F……真不爽啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#5P哎？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#070F不……没什么。\x02\x03",
            "说起来，晚宴就是今天晚上吧。\x01",
            "　\x02\x03",
            "因为会进行到很晚，\x01",
            "好像也为我们准备了房间呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F哎呀哎呀，真是王家典范的服务啊。\x02\x03",
            "虽然能和各位社会名流同席，\x01",
            "但是总觉得有点拘谨啊……\x02\x03",
            "不过可以享受到利贝尔的宫廷料理，\x01",
            "我这就赏面应邀参加一下吧。\x02\x03",
            "#035F呼～现在只是想象一下，\x01",
            "口水也就要流出来了呢～啧啧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#5P出来了，出来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#2P呵呵，一听奥利维尔这些话，\x01",
            "好像感觉自己什么压力都没有了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哈·哈·哈。\x01",
            "那么我们赶快去吧！\x02\x03",
            "到盛情邀请我们的爱与希望的天堂去！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x104, 0xFF)
    OP_44(0x108, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 98000, 250, 32890, 90)

    NpcTalk(
        0x9,
        "男性的声音",
        "#2P……就这样走吗。\x02",
    )

    CloseMessageWindow()

    def lambda_5787():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5787)

    def lambda_5795():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5795)

    def lambda_57A3():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_57A3)

    def lambda_57B1():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_57B1)
    OP_6D(103750, 1250, 32810, 1500)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#033F啊，你是……\x02",
    )

    CloseMessageWindow()

    def lambda_581A():

        label("loc_581A")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_581A")

    QueueWorkItem2(0x101, 2, lambda_581A)

    def lambda_582B():

        label("loc_582B")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_582B")

    QueueWorkItem2(0x102, 2, lambda_582B)

    def lambda_583C():

        label("loc_583C")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_583C")

    QueueWorkItem2(0x104, 2, lambda_583C)

    def lambda_584D():

        label("loc_584D")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_584D")

    QueueWorkItem2(0x108, 2, lambda_584D)

    def lambda_585E():
        OP_8E(0xFE, 0x19ADC, 0x4E2, 0x7D00, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_585E)
    OP_6D(107020, 1250, 33310, 3000)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x104, 400)

    ChrTalk(
        0x9,
        (
            "#274F你这人啊……\x02\x03",
            "我还以为你每天不打招呼就出去\x01",
            "是去干什么呢……\x02\x03",
            "没想到你根本没考虑到自己的立场\x01",
            "就去参加什么武术大会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F真、真讨厌啊，穆拉君。\x02\x03",
            "不要做出那样恐怖的表情嘛。\x01",
            "　\x02\x03",
            "微笑才能招福嘛。\x01",
            "笑一个，笑一个～㈱\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x9,
        "#271F#3S谁做出恐怖的表情了！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F（那个制服，难道是……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（嗯……\x01",
            "　是埃雷波尼亚帝国的军服……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F（嗯……\x01",
            "　看起来是个很能干的小哥嘛。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#270F……初次见面。\x02\x03",
            "我的名字叫穆拉。\x01",
            "是前一段时间来上任的\x01",
            "埃雷波尼亚帝国大使馆的武官。\x02\x03",
            "我和这个超级大赖皮蛋……\x01",
            "唉……算是很久以前认识的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x104, 0xFF)
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(
        0x104,
        (
            "#031F就是所谓的『青梅竹马』啦。\x02\x03",
            "呵呵，平时总是一幅严肃的面孔，\x01",
            "没想到还有这样可爱的地方嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#274F#3S快·给·我·闭·嘴。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#034F是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x9, 400)

    ChrTalk(
        0x9,
        (
            "#272F咳，失礼了。\x02\x03",
            "#270F看起来……\x01",
            "这个大赖皮蛋给你们添了很多麻烦。\x02\x03",
            "我代表帝国大使馆向你们道歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊，没什么……\x01",
            "也没有什么麻烦啦。\x02\x03",
            "在比赛中，奥利维尔的枪法和魔法\x01",
            "给予了我们很大的帮忙呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F我说，奥利维尔。\x02\x03",
            "参加武术大会的事情，\x01",
            "你一直瞒着大使馆的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哈·哈·哈。\x01",
            "我没有故意隐瞒啊。\x02\x03",
            "只是没有告诉他们罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#271F#3S这不是隐瞒又是什么！\x01",
            "　\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x9,
        (
            "#272F算了……\x01",
            "过去的事情再说也没用了。\x02\x03",
            "赶快回大使馆去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F哎……\x02\x03",
            "#036F请、请等一下。\x02\x03",
            "我们正要去王城应邀出席一场\x01",
            "美妙豪华的晚宴呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#270F正因为是美妙豪华的晚宴，\x01",
            "所以让你去了我就更加难办了。\x02\x03",
            "这段时间，\x01",
            "你还是给我老老实实地呆在大使馆吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#033F………………真的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#272F我从不开玩笑的。\x02",
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x104,
        (
            "#036F这、这简直是杀人啦～……\x02\x03",
            "我全心全意地为晚宴努力到如此地步……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F确、确实……\x01",
            "这样不是有点可怜吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F只是出席晚宴，\x01",
            "不会有什么问题的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F有什么原因吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(
        0x104,
        (
            "#031F你们，说得太好了！\x02\x03",
            "啊啊……\x01",
            "『伙伴』是多么美妙的词语……\x02\x03",
            "比起某个寡情薄幸的青梅竹马来说\x01",
            "简直就是温暖太多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#272F……你们好像还不了解事情的严重程度。\x01",
            "　\x02\x03",
            "#270F仔细想象一下。\x02\x03",
            "利贝尔王家主办的晚宴，\x01",
            "各地的有权有势的人士齐聚一堂……\x02\x03",
            "在那里，有个弄不清楚自己立场的\x01",
            "旁若无人的我行我素的大赖皮蛋在捣乱……\x02\x03",
            "如果被人知道他是帝国人的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#074F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F等、等一下各位。\x01",
            "为什么都突然沉默了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F……不好意思，奥利维尔。\x01",
            "你那位朋友的担心也很有道理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F没错，如果在王城的晚宴中\x01",
            "也像平常那样胡作非为的话就糟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#075F嗯……\x01",
            "说不定会发展成国际问题呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#036F哇，这样就叛变了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#270F百日战役结束后的第十个年头……\x01",
            "……这是个非常微妙的时间啊。\x02\x03",
            "忍耐一下吧，奥利维尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)

    def lambda_673C():

        label("loc_673C")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_673C")

    QueueWorkItem2(0x104, 2, lambda_673C)
    OP_8E(0x9, 0x19E74, 0x4E2, 0x7D3C, 0x7D0, 0x0)
    TurnDirection(0x9, 0x104, 400)
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x104,
        (
            "#031F稍、稍微等一下嘛～\x01",
            "穆拉先生～\x02\x03",
            "隐瞒了真相的事情，我道歉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#272F说什么也没用。\x02",
    )

    CloseMessageWindow()

    def lambda_6804():

        label("loc_6804")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_6804")

    QueueWorkItem2(0x101, 2, lambda_6804)

    def lambda_6815():

        label("loc_6815")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_6815")

    QueueWorkItem2(0x102, 2, lambda_6815)

    def lambda_6826():

        label("loc_6826")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_6826")

    QueueWorkItem2(0x104, 2, lambda_6826)

    def lambda_6837():

        label("loc_6837")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_6837")

    QueueWorkItem2(0x108, 2, lambda_6837)
    OP_44(0x104, 0xFF)
    OP_8C(0x9, 270, 400)

    def lambda_6853():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6853)
    Sleep(200)
    SetChrChipByIndex(0x104, 37)
    SetChrSubChip(0x104, 0)
    SetChrFlags(0x104, 0x20)

    def lambda_6875():
        OP_6D(107020, 1250, 33610, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6875)

    def lambda_688D():
        OP_8F(0xFE, 0x17700, 0xFA, 0x7B0C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_688D)

    def lambda_68A8():
        OP_8E(0xFE, 0x17700, 0xFA, 0x7D3C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_68A8)

    ChrTalk(
        0x104,
        "#15A#2P我的晚宴～！\x05\x02",
    )

    Sleep(1500)

    ChrTalk(
        0x104,
        "#15A#2P我的宫廷料理～！\x05\x02",
    )

    Sleep(1500)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_6D(108020, 1250, 33310, 1000)

    ChrTalk(
        0x101,
        "#506F#5P哎……这样好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P虽然表面上有点可怜……\x01",
            "不过他应该想到最后还是这样的，嗯。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x102, 400)

    ChrTalk(
        0x108,
        (
            "#071F哈哈，算了算了。\x01",
            "正所谓『塞翁失马焉知非福』。\x02\x03",
            "我们连他的那份也一起享受算了～！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#5P嗯……没办法。\x02\x03",
            "#006F那么，我们就打起精神，\x01",
            "马上向格兰赛尔城出发吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_3E(0x371, 1)
    OP_28(0x49, 0x1, 0x40)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x104, 106850, 1250, 30720, 0)
    RemoveParty(0x3, 0xFF)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrPos(0x24, 48500, 250, 41910, 90)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x25, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2E, 36280, 1250, 42890, 45)
    SetChrPos(0x2C, 37150, 1250, 43970, 225)
    SetChrPos(0x2D, 40150, 1250, 48060, 180)
    SetChrPos(0x2F, 40150, 1250, 46580, 0)
    SetChrFlags(0x2D, 0x10)
    SetChrFlags(0x2F, 0x10)
    OP_43(0x2D, 0x0, 0x0, 0x2)
    OP_43(0x2F, 0x0, 0x0, 0x2)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    OP_4B(0x34, 255)
    SetChrPos(0x101, 106440, 1250, 32490, 270)
    SetChrPos(0x102, 106440, 1250, 32490, 270)
    SetChrPos(0x108, 106440, 1250, 32490, 270)
    OP_6D(106440, 1250, 32490, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_30_521B end

    def Function_31_6C4D(): pass

    label("Function_31_6C4D")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(72150, 250, 45780, 0)
    OP_6C(45000, 0)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, 72830, 250, 45190, 270)
    SetChrPos(0x101, 71410, 250, 45750, 125)
    SetChrPos(0x102, 71380, 250, 44240, 45)
    SetChrPos(0x108, 70360, 250, 45070, 90)
    OP_4A(0x31, 255)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1F,
        (
            "#814F………………啊。\x02\x03",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F刚才所说的句句属实，绝非戏言。\x01",
            "　\x02\x03",
            "这是一个非常重要的任务，\x01",
            "需要亚妮拉丝小姐你的帮助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#819F……嗯。\x02\x03",
            "抱歉，我头脑有一些混乱了，\x01",
            "不太能把握现在的状况。\x02\x03",
            "#812F虽然不太明白，\x01",
            "但大家是不是要在协会集合呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，没错。\x01",
            "可以向艾南哥哥询问详细的情况哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "我知道了……！\x01",
            "我先去那里等着吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6EAF():

        label("loc_6EAF")

        TurnDirection(0xFE, 0x1F, 0)
        OP_48()
        Jump("loc_6EAF")

    QueueWorkItem2(0x101, 1, lambda_6EAF)

    def lambda_6EC0():

        label("loc_6EC0")

        TurnDirection(0xFE, 0x1F, 0)
        OP_48()
        Jump("loc_6EC0")

    QueueWorkItem2(0x102, 1, lambda_6EC0)

    def lambda_6ED1():

        label("loc_6ED1")

        TurnDirection(0xFE, 0x1F, 0)
        OP_48()
        Jump("loc_6ED1")

    QueueWorkItem2(0x108, 1, lambda_6ED1)
    OP_8E(0x1F, 0x11634, 0xFA, 0xA1CC, 0xFA0, 0x0)
    OP_8E(0x1F, 0x1154E, 0x4E2, 0x93DA, 0xFA0, 0x0)
    OP_8E(0x1F, 0xF032, 0x4E2, 0x945C, 0xFA0, 0x0)
    SetChrFlags(0x1F, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_4B(0x31, 255)
    EventEnd(0x0)
    Return()

    # Function_31_6C4D end

    def Function_32_6F30(): pass

    label("Function_32_6F30")

    EventBegin(0x0)
    OP_6F(0xE, 118)
    OP_6F(0xF, 120)
    OP_6D(44210, 5550, 35490, 0)
    OP_67(0, 9330, -10000, 0)
    OP_6C(294000, 0)
    OP_6E(212, 0)
    OP_6B(4490, 0)

    def lambda_6F83():
        OP_6D(37610, 5550, 36790, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6F83)

    def lambda_6F9B():
        OP_67(0, 5170, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6F9B)

    def lambda_6FB3():
        OP_6C(270000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6FB3)

    def lambda_6FC3():
        OP_6E(149, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6FC3)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    Sleep(9000)
    OP_6F(0xE, 118)
    OP_6F(0xF, 120)
    OP_70(0xE, 0x78)
    OP_70(0xF, 0x78)
    OP_22(0x82, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xB6, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB6, 0x0, 0x64)
    SetMapFlags(0x100000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4102   ._SN", 100, 1, 0)
    IdleLoop()
    Return()

    # Function_32_6F30 end

    def Function_33_7032(): pass

    label("Function_33_7032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70B9")
    EventBegin(0x0)
    Fade(1500)
    SetChrPos(0x101, 68590, 250, 45300, 270)
    SetChrPos(0x102, 69280, 250, 44330, 270)
    OP_6D(68980, 250, 44840, 1500)
    OP_0D()

    ChrTalk(
        0x102,
        "#010F这里就是休息处了。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Call(0, 34)

    label("loc_70B9")

    Return()

    # Function_33_7032 end

    def Function_34_70BA(): pass

    label("Function_34_70BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 5)), scpexpr(EXPR_END)), "loc_70C3")
    EventBegin(0x0)

    label("loc_70C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 4)), scpexpr(EXPR_END)), "loc_70D4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 5)), scpexpr(EXPR_END)), "loc_70E5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 6)), scpexpr(EXPR_END)), "loc_70F6")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 7)), scpexpr(EXPR_END)), "loc_7107")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 0)), scpexpr(EXPR_END)), "loc_7118")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 1)), scpexpr(EXPR_END)), "loc_7129")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 2)), scpexpr(EXPR_END)), "loc_713A")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_713A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 3)), scpexpr(EXPR_END)), "loc_714B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_714B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 4)), scpexpr(EXPR_END)), "loc_715C")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_715C")

    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_71D4")

    ChrTalk(
        0x102,
        (
            "#014F我们还有很多地方都没逛呢，\x01",
            "现在就要休息了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_729E")

    label("loc_71D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7245")

    ChrTalk(
        0x102,
        (
            "#010F还没有逛过所有地方呢，\x01",
            "现在就要休息了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_729E")

    label("loc_7245")


    ChrTalk(
        0x102,
        (
            "#019F已经有点累了呢。\x01",
            "现在就休息吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_729E")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【继续参观诞辰庆典】\x01",        # 0
            "【已经累了，休息一下】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7329"),
        (1, "loc_7407"),
        (SWITCH_DEFAULT, "loc_9FCC"),
    )


    label("loc_7329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73FD")
    OP_A2(0x66D)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F嗯，\x01",
            "还想再看看别的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，把王都转遍了之后\x01",
            "我们再回到这里来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，就坐在那边的长椅上休息吧。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_73FF")

    label("loc_73FD")

    EventEnd(0x1)

    label("loc_73FF")

    SetMapFlags(0x2000000)
    Jump("loc_9FCC")

    label("loc_7407")

    OP_A2(0x66F)
    OP_28(0x55, 0x4, 0x40)
    OP_82(0x4, 0x0)
    Fade(1000)
    OP_6D(70100, 250, 42490, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, 70660, 250, 42400, 0)
    SetChrPos(0x102, 69570, 250, 42530, 0)
    ClearMapFlags(0x800)

    def lambda_746F():
        OP_67(0, 5350, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_746F)

    def lambda_7487():
        OP_6C(135000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7487)

    def lambda_7497():
        OP_6D(73240, 250, 45110, 3500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7497)

    def lambda_74AF():
        OP_6B(2800, 3500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_74AF)

    def lambda_74BF():
        OP_8E(0xFE, 0x11E18, 0xFA, 0xAF5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_74BF)
    Sleep(400)

    def lambda_74DF():
        OP_8E(0xFE, 0x11E18, 0xFA, 0xB324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_74DF)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 38)

    def lambda_7510():
        OP_96(0xFE, 0x12016, 0x1C2, 0xAF5A, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7510)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 270, 400)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 39)

    def lambda_7544():
        OP_96(0xFE, 0x12016, 0x1C2, 0xB324, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7544)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x101,
        (
            "#007F哈啊……\x01",
            "到处逛还真是累呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#010F就在这里稍微休息一下吧。\x02\x03",
            "真是难得的安逸时刻……\x01",
            "王都也没有发生其他骚动的迹象。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#004F约修亚你真是的……\x01",
            "难道还在担心那件事吗。\x02\x03",
            "#006F今天就把所有的事情都扔给老爸吧。\x01",
            "　\x02\x03",
            "谁让他迟到了，\x01",
            "多做点工作也是理所应当的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，说的也是。\x02\x03",
            "#010F不管怎么说这也是他的职责啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呼，真是没办法啊。\x02\x03",
            "#501F话说回来……\x01",
            "我们已经是正游击士了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，以后就可以在\x01",
            "不受支部监督的情况下自由行动了。\x02\x03",
            "而且人手不足的支部会发来支援请求，\x01",
            "乘坐定期船的机会也会变多。\x01",
            "　\x02\x03",
            "#019F相应地，我们所要承担的责任也增加了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，不管怎么说，\x01",
            "我们俩都会继续努力下去的。\x02\x03",
            "而且这次连政变都成功阻止了。\x01",
            "　\x02\x03",
            "#001F哈哈，老爸再也不会说\x01",
            "『约修亚不在的话很让人担心』\x01",
            "这类又讨厌又没根据的话了呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈……\x01",
            "我想父亲他应该不会再说了。\x02\x03",
            "#010F不过，我以后也想继续和你在一起。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F……哎……\x02\x03",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        "#005F#3S哎哎哎哎哎哎哎哎！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F啊，这样让你很为难吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F不是，该说是为难呢还是……\x02\x03",
            "在一起……\x01",
            "那个……是指什么……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那个啊，因为我们互相了解对方的脾气，\x01",
            "而且也知道各自的习惯和爱好。\x02\x03",
            "所以我觉得，\x01",
            "我们俩以后继续搭档也很好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊……是指游击士的工作啊……\x02\x03",
            "#506F什么嘛，我还以为是告白呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F哎……\x02",
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_7CC1():
        OP_6E(251, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7CC1)
    Sleep(250)

    ChrTalk(
        0x101,
        (
            "#504F#3S哇啊啊啊啊啊啊！#2S\x02\x03",
            "#3S我什么都没说！快给我忘掉！#2S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F艾丝蒂尔，你……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7D4E():
        OP_67(0, 7000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D4E)

    def lambda_7D66():
        OP_6C(115000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7D66)

    def lambda_7D76():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_7D76)
    Sleep(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)

    def lambda_7D95():
        OP_96(0xFE, 0x11D28, 0xFA, 0xAF5A, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D95)
    WaitChrThread(0x101, 0x1)
    OP_8E(0x101, 0x11B34, 0xFA, 0xAF5A, 0x7D0, 0x0)
    SetChrSubChip(0x102, 0)
    WaitChrThread(0x101, 0x3)
    TurnDirection(0x101, 0x102, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 6)), scpexpr(EXPR_END)), "loc_7E94")

    ChrTalk(
        0x101,
        (
            "#008F不、不过今天还真是热啊！？\x01",
            "　\x02\x03",
            "#008F热的时候吃冰淇淋是最好了！\x02\x03",
            "#504F之前说好我要请客的！\x01",
            "在这等我一会儿！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F38")

    label("loc_7E94")


    ChrTalk(
        0x101,
        (
            "#008F不、不过\x01",
            "今天还真是热啊！？\x02\x03",
            "#008F热的时候吃冰淇淋是最好了！\x02\x03",
            "#504F我请客，\x01",
            "在这等我一会儿！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F38")

    ClearChrFlags(0x101, 0x4)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0x101, 0x40)

    def lambda_7F5A():
        OP_6D(73240, 250, 46110, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7F5A)

    def lambda_7F72():
        OP_8E(0xFE, 0x1129C, 0xFA, 0xED1C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F72)
    SetChrSubChip(0x102, 2)
    Sleep(500)

    ChrTalk(
        0x102,
        "#014F#5P啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x102,
        (
            "#017F#5P艾丝蒂尔……\x01",
            "卖冰淇淋的地方不是那边啊……\x02\x03",
            "……………………………………\x02\x03",
            "#014F难道……刚才……艾丝蒂尔……\x02\x03",
            "#013F不……\x01",
            "……应该不可能吧………\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 71640, 1250, 37000, 0)

    NpcTalk(
        0x20,
        "男性的声音",
        (
            "#3P哎呀……\x01",
            "年轻人还真是令人羡慕啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0xBB8)

    def lambda_80AA():
        OP_6C(153000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_80AA)

    def lambda_80BA():
        OP_6D(71700, 1250, 39000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80BA)

    def lambda_80D2():
        OP_67(0, 5170, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_80D2)

    def lambda_80EA():
        OP_6E(251, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_80EA)

    def lambda_80FA():
        OP_6B(3340, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_80FA)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 1)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    def lambda_8123():
        OP_8E(0xFE, 0x118DC, 0xFA, 0xA3DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8123)
    Sleep(200)

    def lambda_8143():
        OP_6D(72850, 250, 43180, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8143)

    def lambda_815B():
        OP_67(0, 7230, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_815B)

    def lambda_8173():
        OP_6E(262, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8173)

    def lambda_8183():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8183)

    def lambda_8193():
        OP_6C(135000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8193)
    WaitChrThread(0x20, 0x1)

    ChrTalk(
        0x102,
        "#014F亚鲁瓦教授……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#130F哎呀，真是好久不见了。\x02\x03",
            "最近发生了不少事情，\x01",
            "不过，最后能恢复和平真是太好了。\x02\x03",
            "人类这种生物，\x01",
            "还是最适合过着平安无事的生活啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#131F哎，怎么了？\x01",
            "你的脸色看起来不太好哦……\x02\x03",
            "好不容易才当上了正游击士，\x01",
            "不是应该高兴点才对吗？\x02\x03",
            "#132F对了，我也送你点什么礼物吧。\x01",
            "　\x02\x03",
            "虽然不是什么很值钱的东西。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_1D(0x21)

    def lambda_83BE():
        OP_6E(276, 20000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_83BE)

    ChrTalk(
        0x102,
        (
            "#013F第一次在洛连特见到你的时候……\x01",
            "我就开始感到很不对劲……\x02\x03",
            "虽说现在有些习惯了……\x02\x03",
            "但是，每当你出现之时，\x01",
            "我的身体都会不由得感到颤抖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#132F哦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F而且……各地所发生的事情……\x02\x03",
            "那些记忆被操纵的人……\x02\x03",
            "凡是有事情发生的地方，\x01",
            "你都会以调查为由出现在那里……\x02\x03",
            "而且……\x01",
            "出现的时间也未免太巧了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#132F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F决定性的证据……\x01",
            "就是克鲁茨先生的反应……\x02\x03",
            "被抹去记忆的克鲁茨先生……\x02\x03",
            "在竞技场的观众席上，\x01",
            "他也无故地突然感觉不舒服……\x02\x03",
            "而那时……\x01",
            "你也在同一个地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#132F……………………………\x02",
    )

    CloseMessageWindow()

    def lambda_8643():
        OP_6D(72320, 250, 43180, 1000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_8643)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 65535)

    def lambda_8665():
        OP_96(0xFE, 0x11D50, 0xFA, 0xB324, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8665)
    WaitChrThread(0x102, 0x1)
    OP_8E(0x102, 0x11A08, 0xFA, 0xB324, 0x7D0, 0x0)
    TurnDirection(0x102, 0x20, 400)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#015F亚鲁瓦教授……\x02\x03",
            "#012F是你干的……没错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#136F呵呵……\x02\x03",
            "被操纵了记忆和认知之后还能\x01",
            "察觉到这种地步，真是不简单啊。\x02\x03",
            "不愧是我制造出来的杰作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F……哎……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#134F那么，我就来解开暗示吧。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x20, 29)
    SetChrSubChip(0x20, 0)

    def lambda_87C0():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_87C0)
    OP_8E(0x20, 0x118DC, 0xFA, 0xA7F8, 0x3E8, 0x0)
    SetChrChipByIndex(0x20, 30)
    SetChrSubChip(0x20, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    Sleep(500)
    SetChrSubChip(0x20, 1)
    Sleep(100)
    OP_20(0x0)
    OP_22(0xBC, 0x0, 0x64)
    SetChrSubChip(0x20, 2)
    OP_AD(0x40037, 0x0, 0x0, 0x7D0)
    Sleep(500)
    OP_AD(0x4002F, 0x0, 0x0, 0x3E8)
    Sleep(300)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_AD(0x40030, 0x0, 0x0, 0x3E8)
    Sleep(300)
    OP_AD(0x40031, 0x0, 0x0, 0x3E8)
    Sleep(300)
    OP_AD(0x40032, 0x0, 0x0, 0x3E8)
    Sleep(300)
    OP_AD(0x40033, 0x0, 0x0, 0x3E8)
    Sleep(300)
    OP_AD(0x40038, 0x0, 0x0, 0x3E8)
    Sleep(400)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x4)
    OP_43(0x102, 0x3, 0x0, 0x24)
    OP_AE(0x1F4)
    Sleep(500)

    ChrTalk(
        0x102,
        "#514F………………啊…………\x02",
    )

    CloseMessageWindow()
    OP_9E(0x102, 0x1E, 0x0, 0x190, 0xBB8)

    def lambda_88F1():
        OP_6C(153000, 100000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_88F1)

    def lambda_8901():
        OP_67(0, 6900, -10000, 100000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8901)
    OP_1D(0x5A)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#514F你是……\x02\x03",
            "……你是……！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "？？？",
        (
            "#133F哼哼……\x01",
            "看来你终于想起我是谁了。\x02\x03",
            "想起了那个把你那七零八落的心\x01",
            "重新组合并修复完整的我。\x02\x03",
            "想起了那个赐予虚无的人偶以灵魂的我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#510F拥有能够扭曲和操纵对方的\x01",
            "记忆和认知的特殊能力……！\x02\x03",
            "七人组『蛇之使徒』其中的一员！\x02\x03",
            "『白面』怀斯曼……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 9)

    def lambda_8AA7():
        OP_6B(2800, 1000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8AA7)

    def lambda_8AB7():
        OP_6D(72010, 650, 45100, 1000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_8AB7)
    OP_22(0x1F5, 0x0, 0x64)
    OP_96(0x102, 0x11A08, 0xFA, 0xB798, 0x2BC, 0x1F40)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#134F嘿嘿……\x01",
            "我刚才不是说了『真是好久不见了』吗。\x02\x03",
            "『执行者』No.XIII。\x02\x03",
            "『漆黑之牙』——\x01",
            "约修亚·阿斯特雷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#510F是、是你……\x02\x03",
            "是你在背后操纵这次的事件！\x01",
            "　\x02\x03",
            "果然……\x01",
            "那个洛伦斯少尉真的是……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#134F猜得没错。\x02\x03",
            "我并没有消除他的记忆，\x01",
            "所以他很快就察觉到你的真实身份。\x02\x03",
            "哈哈，他也应该感到很高兴吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#516F你……你是……\x02\x03",
            "…………………………………\x02\x03",
            "#510F……是来了结我的吗。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#134F哼哼……\x01",
            "没必要摆出这副架势。\x02\x03",
            "计划的第一阶段已经顺利完成了。\x02\x03",
            "我只是稍微有点空闲，\x01",
            "顺道过来和你叙一下旧而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#510F第一阶段……\x02\x03",
            "是指那个地下遗迹的封印吗……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#134F阻塞通往『环』之路的『门』……\x02\x03",
            "将其开启，就是计划的第一阶段。\x01",
            "　\x02\x03",
            "#136F哼哼……\x01",
            "要想再次关上已经是不可能的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#510F果然……\x01",
            "总觉得事情还没那么容易结束……\x02\x03",
            "#515F『辉之环』到底是什么！？\x02\x03",
            "『结社』……\x01",
            "你到底有什么企图！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#134F如果想知道的话，\x01",
            "不如考虑一下重返『结社』吧？\x02\x03",
            "是你的话，应该很快就能重操旧业的。\x02\x03",
            "虽然意识上稍微有点迟钝，\x01",
            "不过治疗一下就能立刻恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#516F………………………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#133F嘿嘿，不要摆出\x01",
            "那么一副狰狞可怕的表情嘛。\x02\x03",
            "我知道……我知道\x01",
            "你现在有两位很重要的家人。\x02\x03",
            "令人尊敬的父亲，\x01",
            "还有那个值得自己全心守护的女孩……\x02\x03",
            "就算『他』现在站在你面前，\x01",
            "你也不会舍得离开那两个人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F………………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#136F所以，我今天才来找你。\x02\x03",
            "作为协助完成计划的谢礼，\x01",
            "我现在让你正式脱离『结社』。\x02\x03",
            "#134F……祝贺你，约修亚。\x01",
            "你已经从『结社』解放出来了。\x02\x03",
            "这五年来，真的辛苦你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F………………………………\x02\x03",
            "#514F………………哎………\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#137F什么呀，真是没意思。\x02\x03",
            "还以为你听了之后会表现得很高兴……\x01",
            "　\x02\x03",
            "#136F唔，难道是感情的那部分结构\x01",
            "至今仍存在着缺陷吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#590F我……协助计划……\x02\x03",
            "……哈哈……说什么……\x01",
            "你在说什么傻话呀……？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#134F啊啊，抱歉。\x01",
            "还忘了跟你说明一件事。\x02\x03",
            "你真正的任务不是暗杀，而是谍报。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F哎……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#134F一个被『结社』丢弃的孩子，\x01",
            "受到别人的同情、无微不至的照顾。\x02\x03",
            "而这个孩子不但没有感恩图报，\x01",
            "还定期向结社的联络员传达各种报告。\x02\x03",
            "包括游击士协会的动向……\x01",
            "以及卡西乌斯·布莱特的情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#514F#4S！！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#136F当然，你所做过的这些事，\x01",
            "你本人并不会留有丝毫印象。\x02\x03",
            "因为我对你施加了暗示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#518F………………………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#135FＳ级游击士——卡西乌斯·布莱特。\x02\x03",
            "毫无疑问，\x01",
            "这个人是本次计划的最大障碍。\x02\x03",
            "假如他当时还在利贝尔，\x01",
            "上校的政变必定很快就会被识破和阻止。\x01",
            "　\x02\x03",
            "#136F为了分析他的性格和行动方式，\x01",
            "并将他在毫不知情的情况下引到国外……\x02\x03",
            "你的情报真的是立了大功哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x102, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 31)
    SetChrSubChip(0x102, 0)

    def lambda_987B():
        OP_99(0x102, 0x0, 0x2, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_987B)
    OP_9E(0x102, 0x1E, 0x0, 0x320, 0xBB8)

    ChrTalk(
        0x102,
        "#517F…………骗……人……………\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#134F所以……我再次对你表示感谢。\x02\x03",
            "这五年来，真是辛苦你了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9916():
        OP_99(0x102, 0x2, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9916)
    OP_9E(0x102, 0x1E, 0x0, 0x4B0, 0xBB8)

    ChrTalk(
        0x102,
        "#517F#3S骗人，你在骗人！\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    def lambda_995D():
        OP_99(0x102, 0x3, 0x6, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_995D)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        "#519F#5S这不是真的啊啊啊啊啊啊啊！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_99A7():
        OP_99(0x102, 0x6, 0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_99A7)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#517F#50W……我……\x02\x03",
            "和艾丝蒂尔一起度过的……\x01",
            "………这些日子……………\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#133F嘿嘿……\x01",
            "为什么要变得这么难过啊？\x02\x03",
            "装作什么都不知道，\x01",
            "继续和家人幸福地生活在一起不就行了吗？\x02\x03",
            "只要你不说，他们永远也不会知道的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#517F………………………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#134F不过嘛……\x01",
            "仔细想想这也真是残酷的对比。\x02\x03",
            "布莱特家的父女实在是太过完美了。\x01",
            "　\x02\x03",
            "对于你这样的怪物来说，\x01",
            "他们所绽放出的光芒是不是太过刺眼了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#518F…………啊………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#134F虽然你能过着人类的正常生活，\x01",
            "不过，本质上还是和普通人不一样的。\x02\x03",
            "这种在任何时候都能想到合理手段、\x01",
            "并用以成功完成任务的思考模式。\x02\x03",
            "这种能够独自与大部队抗衡的\x01",
            "被强化至极限的肉体和反射神经。\x02\x03",
            "我所造出来的最强人类兵器，\x01",
            "那就是你——『漆黑之牙』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#518F……………………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#134F这样的你，\x01",
            "终究还是不可能和普通人类交往的。\x02\x03",
            "就算今后仍然和他们生活在一起，\x01",
            "这样的你，也不可能感到幸福。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#518F……………………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#136F所以，要是觉得难受的话，\x01",
            "什么时候回来都可以。\x02\x03",
            "由伟大的主人所统率的魂之结社。\x02\x03",
            "#138F我们『噬身之蛇』……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x20, 29)
    SetChrSubChip(0x20, 0)
    OP_44(0x101, 0xFF)

    def lambda_9EA9():
        OP_6D(72320, 250, 46180, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_9EA9)
    OP_8E(0x20, 0x112BA, 0xFA, 0xB748, 0x7D0, 0x0)

    def lambda_9ED5():
        OP_6C(134000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9ED5)

    def lambda_9EE5():
        OP_8E(0xFE, 0x11260, 0xFA, 0xE13C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_9EE5)
    Sleep(6000)
    OP_20(0x7D0)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x20, 0x1)

    def lambda_9F14():
        OP_6B(2300, 12000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9F14)
    OP_21()
    OP_1D(0x53)
    Sleep(2000)

    ChrTalk(
        0x102,
        (
            "#517F#5P#40W……………………………\x02\x03",
            "这是……惩罚吗……\x02\x03",
            "……姐姐……莱维………\x02\x03",
            "…………我是……………………\x02\x03",
            "………………………………\x01",
            "………………我是………………\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_51(0x102, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x4)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x3F1)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 1)
    IdleLoop()
    Jump("loc_9FCC")

    label("loc_9FCC")

    Return()

    # Function_34_70BA end

    def Function_35_9FCD(): pass

    label("Function_35_9FCD")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x20, 0xFF)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x31, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x101, 32)
    SetChrPos(0x101, 42010, 1250, 46960, 102)
    SetChrPos(0x20, 58940, 1250, 47080, 263)
    OP_7E(0x258, 0xFCE0, 0xFC7C, 0x50, 0x0)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x39, 0x80)
    SetChrFlags(0x3A, 0x80)
    SetChrFlags(0x3B, 0x80)
    SetChrFlags(0x3C, 0x80)
    SetChrFlags(0x3D, 0x80)
    SetChrFlags(0x3E, 0x80)
    SetChrFlags(0x3F, 0x80)
    SetChrFlags(0x40, 0x80)
    SetChrFlags(0x41, 0x80)
    SetChrFlags(0x42, 0x80)
    SetChrFlags(0x43, 0x80)
    SetChrFlags(0x44, 0x80)
    SetChrFlags(0x45, 0x80)
    SetChrFlags(0x46, 0x80)
    SetChrFlags(0x47, 0x80)
    SetChrFlags(0x48, 0x80)
    SetChrFlags(0x49, 0x80)
    SetChrFlags(0x4A, 0x80)
    SetChrFlags(0x4B, 0x80)
    SetChrFlags(0x4C, 0x80)
    SetChrFlags(0x4D, 0x80)
    SetChrFlags(0x4E, 0x80)
    SetChrFlags(0x4F, 0x80)
    SetChrFlags(0x50, 0x80)
    SetChrFlags(0x51, 0x80)
    SetChrFlags(0x52, 0x80)
    SetChrFlags(0x53, 0x80)
    SetChrFlags(0x54, 0x80)
    SetChrFlags(0x55, 0x80)
    SetChrFlags(0x56, 0x80)
    SetChrFlags(0x57, 0x80)
    OP_6D(49840, 0, 46640, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0xBDF6, 0xFA, 0xB748, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        (
            "#007F哈啊……\x01",
            "竟然等了这么长时间啊……\x02\x03",
            "天色都已经快黑了……\x02\x03",
            "#503F约修亚……\x01",
            "刚才是怎么想的呢……\x02\x03",
            "唔～……\x01",
            "一想起来脸还会发热呢……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "男性的声音",
        "#1P哦，是艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_A2E4():
        TurnDirection(0xFE, 0x20, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A2E4)

    def lambda_A2F2():
        OP_6D(51060, 0, 46780, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A2F2)

    def lambda_A30A():
        OP_8E(0xFE, 0xCA58, 0x0, 0xB784, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A30A)
    Sleep(2000)
    OP_8E(0x101, 0xC418, 0x0, 0xB784, 0x7D0, 0x0)
    SetChrFlags(0x101, 0x1000)
    WaitChrThread(0x20, 0x1)

    ChrTalk(
        0x101,
        (
            "#004F咦，亚鲁瓦教授。\x01",
            "在这种地方遇见你真是难得啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#130F#4P哈哈，也许吧。\x02\x03",
            "对了，刚才我也见到约修亚了。\x01",
            "　\x02\x03",
            "还有，在此恭喜一下。\x01",
            "听说你们终于成为了正游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嘿嘿……还好啦。\x02\x03",
            "#004F哎……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#131F#4P……怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F教授你……\x01",
            "和平时看起来感觉不太一样啊？\x02\x03",
            "总觉得你的样子好像特别的高兴。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#132F#4P………………………………\x02\x03",
            "#130F哈哈，被你看穿了吗。\x02\x03",
            "其实也不是什么特别高兴的事，\x01",
            "只是考古学的研究取得了进展而已。\x02\x03",
            "所以有点喜出望外了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F哎～那不是很好嘛。\x02\x03",
            "#004F啊……对不起！\x02\x03",
            "冰淇淋快融化了，我得赶快走了！\x01",
            "　\x02\x03",
            "#001F那么，回头见啦！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A5F2():
        OP_6D(53990, 250, 46840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A5F2)

    def lambda_A60A():

        label("loc_A60A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_A60A")

    QueueWorkItem2(0x20, 1, lambda_A60A)
    OP_8E(0x101, 0xC8DC, 0x0, 0xBB3A, 0xFA0, 0x0)
    OP_8E(0x101, 0xEAD8, 0x4E2, 0xBB80, 0xFA0, 0x0)
    OP_8E(0x101, 0xF5B4, 0x4E2, 0xC8DC, 0xFA0, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    NpcTalk(
        0x20,
        "怀斯曼",
        (
            "#136F哼哼，原来如此。\x01",
            "卡西乌斯·布莱特的女儿……\x02\x03",
            "#134F让我感到越来越有趣了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_82(0x4, 0x0)
    OP_6D(67120, 250, 45170, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    ClearChrFlags(0x102, 0x2)
    SetChrPos(0x102, 67120, 250, 45170, 270)
    SetChrPos(0x101, 68100, 1250, 54590, 180)

    def lambda_A757():
        OP_6D(67810, 250, 44960, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A757)
    OP_8E(0x101, 0x10D42, 0xFA, 0xAFD2, 0xFA0, 0x0)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#506F不好意思，我回来晚了！\x02\x03",
            "人太多了，好不容易才买到呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F是吗，真是辛苦了。\x02\x03",
            "那么我就不客气了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0x10B1C, 0xFA, 0xAF64, 0x7D0, 0x0)
    SetChrFlags(0x102, 0x80)
    SetChrChipByIndex(0x101, 33)
    OP_99(0x101, 0x0, 0x2, 0x5DC)
    Sleep(500)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x40)
    SetChrChipByIndex(0x101, 34)
    SetChrChipByIndex(0x102, 35)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    OP_8F(0x102, 0x107AC, 0xFA, 0xAFA0, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        (
            "#008F……嗯……\x02\x03",
            "#503F那个，刚才的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F啊啊，刚才真抱歉。\x01",
            "那种说话方式让你误会了。\x02\x03",
            "我刚才所说的那些话，\x01",
            "的确好像是那种很差劲的告白呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F哎……嗯……\x02\x03",
            "倒也不是什么很差劲的啦……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过，仔细想想的话，\x01",
            "其实也不用这么着急地下结论。\x02\x03",
            "既然已经成为了正游击士，\x01",
            "当然可以各自发展去做自己想做的事情。\x02\x03",
            "说不定……\x01",
            "现在应该考虑一下大家的未来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F确、确实……\x02\x03",
            "#503F（如果结婚的话，就会生小孩呢……）\x01",
            "　\x02\x03",
            "#504F（……哎呀！我想到哪里去了啊！）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F那么，都已经傍晚了，\x01",
            "我们吃完冰淇淋就回城去吧。\x02\x03",
            "父亲和大家都在等着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F………………………………\x02\x03",
            "#002F……约修亚？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F怎么了，艾丝蒂尔？\x02\x03",
            "是不是想谈关于未来的事情？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F不、不是啦！\x02\x03",
            "#582F总之赶快回城里去吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    ClearMapFlags(0x2000000)
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4204   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_35_9FCD end

    def Function_36_AC88(): pass

    label("Function_36_AC88")

    OP_77(0x64, 0x64, 0x64, 0x177000, 0x0)
    Return()

    # Function_36_AC88 end

    def Function_37_AC92(): pass

    label("Function_37_AC92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AC9F")
    Return()

    label("loc_AC9F")

    OP_A2(0x66E)
    EventBegin(0x0)
    OP_6D(37600, 1250, 49080, 2000)
    OP_8B(0x101, 0x90E2, 0xBF72, 0x190)
    OP_8B(0x102, 0x90E2, 0xBF72, 0x190)

    ChrTalk(
        0x101,
        (
            "#004F哇啊……\x01",
            "好多人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F因为今天特别热嘛。\x02\x03",
            "冰淇淋店生意红火也是情理之中的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唔～一看到这样的场景，\x01",
            "我就更想吃了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearMapFlags(0x1)
    OP_51(0x5B, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5B, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5B, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_AE3B():
        OP_69(0x5B, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE3B)
    TurnDirection(0x101, 0x102, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#501F啊，对了……\x01",
            "那个时候的约定。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F约定……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#507F在王城里面穿女佣服的时候，\x01",
            "约修亚，你不是在那里闹别扭吗。\x02\x03",
            "那时我就答应要请你吃冰淇淋的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F你怎么偏偏想起了那件无聊的事情……\x01",
            "　\x02\x03",
            "#018F我刚才还以为是在那个小公园\x01",
            "互相约定的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F啊……哦。\x01",
            "那、那个我当然还记得啦。\x02\x03",
            "可是在白天我实在平静不下来。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F？？？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        (
            "#509F总、总而言之等逛了一圈之后，\x01",
            "就到百货店后面的小公园去休息！\x02\x03",
            "那时我就请你吃冰淇淋！\x02\x03",
            "这样就ＯＫ了吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FＯ、ＯＫ……\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    SetMapFlags(0x2000000)
    Return()

    # Function_37_AC92 end

    def Function_38_B0D9(): pass

    label("Function_38_B0D9")

    EventBegin(0x2)

    ChrTalk(
        0x102,
        (
            "#010F看起来这里就是\x01",
            "艾南先生所说的地下水路的入口。\x01",
            "　\x02\x03",
            "今天已经很晚了，\x01",
            "明天再和金先生他们一起进去看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_38_B0D9 end

    def Function_39_B196(): pass

    label("Function_39_B196")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门紧紧地关着，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_39_B196 end

    def Function_40_B1E0(): pass

    label("Function_40_B1E0")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门紧紧地关着，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_40_B1E0 end

    def Function_41_B22A(): pass

    label("Function_41_B22A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《导力时钟第２号》\x01",
            "　七耀历１１６３年·蔡斯技术工房制造\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_41_B22A end

    def Function_42_B2BD(): pass

    label("Function_42_B2BD")

    SetPlaceName(0xBA) # 帝国大使馆
    Return()

    # Function_42_B2BD end

    def Function_43_B2C1(): pass

    label("Function_43_B2C1")

    SetPlaceName(0xB1) # 帝国大使馆
    Return()

    # Function_43_B2C1 end

    def Function_44_B2C5(): pass

    label("Function_44_B2C5")

    SetPlaceName(0xBB) # 帝国大使馆
    Return()

    # Function_44_B2C5 end

    def Function_45_B2C9(): pass

    label("Function_45_B2C9")

    SetPlaceName(0xBC) # 帝国大使馆
    Return()

    # Function_45_B2C9 end

    def Function_46_B2CD(): pass

    label("Function_46_B2CD")

    SetPlaceName(0xBD) # 帝国大使馆
    Return()

    # Function_46_B2CD end

    SaveToFile()

Try(main)
