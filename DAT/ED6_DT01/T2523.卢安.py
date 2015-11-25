from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2523   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2523.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60075",
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
        '乔儿',                                 # 9
        '汉斯',                                 # 10
        '波利',                                 # 11
        '特蕾莎院长',                           # 12
        '达尼艾尔',                             # 13
        '玛丽',                                 # 14
        '克拉姆',                               # 15
        '白色公主塞茜莉亚',                     # 16
        '红骑士尤利乌斯',                       # 17
        '苍骑士奥斯卡',                         # 18
        '侍女玲珐',                             # 19
        '侍女蕾妮',                             # 20
        '拉多公爵',                             # 21
        '科洛多议长',                           # 22
        '醉汉',                                 # 23
        '平民男子',                             # 24
        '王都的主教',                           # 25
        '贵族女孩',                             # 26
        '空之女神爱德丝',                       # 27
        '科林兹校长',                           # 28
        '杜南公爵',                             # 29
        '管家菲利普',                           # 30
        '戴尔蒙市长',                           # 31
        '奈尔',                                 # 32
        '凯诺娜上尉',                           # 33
        '梅贝尔市长',                           # 34
        '莉拉',                                 # 35
        '莱维',                                 # 36
        '米克',                                 # 37
        '勤务员巴克斯',                         # 38
        '\u3000',                               # 39
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
        '观众',                                 # 65
        '观众',                                 # 66
        '观众',                                 # 67
        '观众',                                 # 68
        '观众',                                 # 69
        '观众',                                 # 70
        '观众',                                 # 71
        '观众',                                 # 72
        '观众',                                 # 73
        '观众',                                 # 74
        '观众',                                 # 75
        '观众',                                 # 76
        '观众',                                 # 77
        '观众',                                 # 78
        '观众',                                 # 79
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH02590 ._CH',             # 02
        'ED6_DT07/CH02640 ._CH',             # 03
        'ED6_DT07/CH02630 ._CH',             # 04
        'ED6_DT07/CH02570 ._CH',             # 05
        'ED6_DT07/CH02280 ._CH',             # 06
        'ED6_DT07/CH02260 ._CH',             # 07
        'ED6_DT07/CH02270 ._CH',             # 08
        'ED6_DT07/CH02540 ._CH',             # 09
        'ED6_DT07/CH01350 ._CH',             # 0A
        'ED6_DT07/CH02603 ._CH',             # 0B
        'ED6_DT07/CH01220 ._CH',             # 0C
        'ED6_DT07/CH01570 ._CH',             # 0D
        'ED6_DT06/CH20088 ._CH',             # 0E
        'ED6_DT07/CH02470 ._CH',             # 0F
        'ED6_DT07/CH02413 ._CH',             # 10
        'ED6_DT07/CH02063 ._CH',             # 11
        'ED6_DT07/CH02103 ._CH',             # 12
        'ED6_DT07/CH02363 ._CH',             # 13
        'ED6_DT07/CH02370 ._CH',             # 14
        'ED6_DT07/CH01040 ._CH',             # 15
        'ED6_DT07/CH01140 ._CH',             # 16
        'ED6_DT07/CH01670 ._CH',             # 17
        'ED6_DT07/CH01230 ._CH',             # 18
        'ED6_DT07/CH02040 ._CH',             # 19
        'ED6_DT07/CH01080 ._CH',             # 1A
        'ED6_DT07/CH01020 ._CH',             # 1B
        'ED6_DT07/CH02500 ._CH',             # 1C
        'ED6_DT06/CH20069 ._CH',             # 1D
        'ED6_DT06/CH20068 ._CH',             # 1E
        'ED6_DT06/CH20071 ._CH',             # 1F
        'ED6_DT06/CH20070 ._CH',             # 20
        'ED6_DT06/CH20072 ._CH',             # 21
        'ED6_DT06/CH20073 ._CH',             # 22
        'ED6_DT06/CH20075 ._CH',             # 23
        'ED6_DT06/CH20076 ._CH',             # 24
        'ED6_DT07/CH01223 ._CH',             # 25
        'ED6_DT07/CH01573 ._CH',             # 26
        'ED6_DT06/CH20131 ._CH',             # 27
        'ED6_DT06/CH20135 ._CH',             # 28
        'ED6_DT06/CH20136 ._CH',             # 29
        'ED6_DT07/CH02573 ._CH',             # 2A
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH02590P._CP',             # 02
        'ED6_DT07/CH02640P._CP',             # 03
        'ED6_DT07/CH02630P._CP',             # 04
        'ED6_DT07/CH02570P._CP',             # 05
        'ED6_DT07/CH02280P._CP',             # 06
        'ED6_DT07/CH02260P._CP',             # 07
        'ED6_DT07/CH02270P._CP',             # 08
        'ED6_DT07/CH02540P._CP',             # 09
        'ED6_DT07/CH01350P._CP',             # 0A
        'ED6_DT07/CH02603P._CP',             # 0B
        'ED6_DT07/CH01220P._CP',             # 0C
        'ED6_DT07/CH01570P._CP',             # 0D
        'ED6_DT06/CH20088P._CP',             # 0E
        'ED6_DT07/CH02470P._CP',             # 0F
        'ED6_DT07/CH02413P._CP',             # 10
        'ED6_DT07/CH02063P._CP',             # 11
        'ED6_DT07/CH02103P._CP',             # 12
        'ED6_DT07/CH02363P._CP',             # 13
        'ED6_DT07/CH02370P._CP',             # 14
        'ED6_DT07/CH01040P._CP',             # 15
        'ED6_DT07/CH01140P._CP',             # 16
        'ED6_DT07/CH01670P._CP',             # 17
        'ED6_DT07/CH01230P._CP',             # 18
        'ED6_DT07/CH02040P._CP',             # 19
        'ED6_DT07/CH01080P._CP',             # 1A
        'ED6_DT07/CH01020P._CP',             # 1B
        'ED6_DT07/CH02500P._CP',             # 1C
        'ED6_DT06/CH20069P._CP',             # 1D
        'ED6_DT06/CH20068P._CP',             # 1E
        'ED6_DT06/CH20071P._CP',             # 1F
        'ED6_DT06/CH20070P._CP',             # 20
        'ED6_DT06/CH20072P._CP',             # 21
        'ED6_DT06/CH20073P._CP',             # 22
        'ED6_DT06/CH20075P._CP',             # 23
        'ED6_DT06/CH20076P._CP',             # 24
        'ED6_DT07/CH01223P._CP',             # 25
        'ED6_DT07/CH01573P._CP',             # 26
        'ED6_DT06/CH20131P._CP',             # 27
        'ED6_DT06/CH20135P._CP',             # 28
        'ED6_DT06/CH20136P._CP',             # 29
        'ED6_DT07/CH02573P._CP',             # 2A
    )

    DeclNpc(
        X                   = 59640,
        Z                   = 1000,
        Y                   = 13450,
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
        X                   = 66040,
        Z                   = 1000,
        Y                   = 16210,
        Direction           = 0,
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
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 6000,
        Z                   = 200,
        Y                   = 22200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 22900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -64500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -30,
        Z                   = 0,
        Y                   = -2630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
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
        X                   = -3500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65575,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 852007,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131111,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196647,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262183,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589863,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 655399,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 720935,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327719,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 852007,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917543,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 983079,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1048615,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1114151,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1179687,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1245223,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 393255,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1376295,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1441831,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458791,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65575,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131111,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196647,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262183,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_AE2",          # 00, 0
        "Function_1_C1D",          # 01, 1
        "Function_2_C1E",          # 02, 2
        "Function_3_D9B",          # 03, 3
        "Function_4_DDA",          # 04, 4
        "Function_5_E9B",          # 05, 5
        "Function_6_1071",         # 06, 6
        "Function_7_10EE",         # 07, 7
        "Function_8_1123",         # 08, 8
        "Function_9_1171",         # 09, 9
        "Function_10_11CE",        # 0A, 10
        "Function_11_11FA",        # 0B, 11
        "Function_12_1A6B",        # 0C, 12
        "Function_13_21A2",        # 0D, 13
        "Function_14_2204",        # 0E, 14
        "Function_15_226B",        # 0F, 15
        "Function_16_22D7",        # 10, 16
        "Function_17_52F3",        # 11, 17
        "Function_18_9655",        # 12, 18
        "Function_19_96A2",        # 13, 19
        "Function_20_96EF",        # 14, 20
        "Function_21_973C",        # 15, 21
        "Function_22_9789",        # 16, 22
        "Function_23_97C7",        # 17, 23
    )


    def Function_0_AE2(): pass

    label("Function_0_AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_AEC")
    Jump("loc_BE9")

    label("loc_AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_AF6")
    Jump("loc_BE9")

    label("loc_AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_BA1")
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, -64400, 0, 3560, 270)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 140, 0, 7810, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, -37340, 1000, 5500, 0)
    SetChrPos(0xE, -33510, 1000, 7750, 90)
    SetChrPos(0xC, -34240, 1000, 8280, 45)
    SetChrPos(0xA, -37450, 1000, 9490, 0)
    SetChrPos(0xD, -36430, 1000, 8790, 0)
    OP_43(0xC, 0x0, 0x0, 0x3)
    Jump("loc_BE9")

    label("loc_BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_BB0")
    ClearChrFlags(0x25, 0x80)
    Jump("loc_BE9")

    label("loc_BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_BBA")
    Jump("loc_BE9")

    label("loc_BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_BC4")
    Jump("loc_BE9")

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_BCE")
    Jump("loc_BE9")

    label("loc_BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_BD8")
    Jump("loc_BE9")

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_BE2")
    Jump("loc_BE9")

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_BE9")

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_C00")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 11)

    label("loc_C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_C0E")
    OP_A3(0x3FB)
    Event(0, 12)

    label("loc_C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_C1C")
    OP_A3(0x3FC)
    Event(0, 16)

    label("loc_C1C")

    Return()

    # Function_0_AE2 end

    def Function_1_C1D(): pass

    label("Function_1_C1D")

    Return()

    # Function_1_C1D end

    def Function_2_C1E(): pass

    label("Function_2_C1E")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C43")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_D85")

    label("loc_C43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_D85")

    label("loc_C5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C75")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_D85")

    label("loc_C75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8E")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_D85")

    label("loc_C8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA7")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_D85")

    label("loc_CA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC0")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_D85")

    label("loc_CC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD9")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_D85")

    label("loc_CD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF2")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_D85")

    label("loc_CF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_D85")

    label("loc_D0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D24")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_D85")

    label("loc_D24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_D85")

    label("loc_D3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D56")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_D85")

    label("loc_D56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6F")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_D85")

    label("loc_D6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D85")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_D85")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D9A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_D85")

    label("loc_D9A")

    Return()

    # Function_2_C1E end

    def Function_3_D9B(): pass

    label("Function_3_D9B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DD9")
    OP_8F(0xFE, 0xFFFF76EE, 0x3E8, 0x23BE, 0x7D0, 0x0)
    Sleep(5000)
    OP_8F(0xFE, 0xFFFF7856, 0x3E8, 0x21DE, 0x7D0, 0x0)
    Sleep(5000)
    Jump("Function_3_D9B")

    label("loc_DD9")

    Return()

    # Function_3_D9B end

    def Function_4_DDA(): pass

    label("Function_4_DDA")

    TalkBegin(0x24)

    ChrTalk(
        0xFE,
        "唉，好困啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "演出什么的好麻烦，\x01",
            "真不想干呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这些都是那个\x01",
            "多事的学生会长想出来的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x24)
    Return()

    # Function_4_DDA end

    def Function_5_E9B(): pass

    label("Function_5_E9B")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_F0D")

    ChrTalk(
        0xFE,
        "再过一会儿演出就要开始了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "差不多该\x01",
            "用广播把演员们召集过来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106D")

    label("loc_F0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_106D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_FC6")

    ChrTalk(
        0xFE,
        "这里只能在下午使用时才开放。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我现在正照科林兹校长的吩咐\x01",
            "进行安全检查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106D")

    label("loc_FC6")


    ChrTalk(
        0xFE,
        (
            "呼，昨天学院的庭院装饰\x01",
            "忙得我眼都花了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次总算赶上了，\x01",
            "下次再做这个的话，\x01",
            "必须要请同学们帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106D")

    TalkEnd(0x25)
    Return()

    # Function_5_E9B end

    def Function_6_1071(): pass

    label("Function_6_1071")

    TalkBegin(0xE)

    ChrTalk(
        0xFE,
        (
            "#772F波利对各种事情都观察得很细致……\x01",
            "　\x02\x03",
            "不过平时就喜欢一直发呆……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_6_1071 end

    def Function_7_10EE(): pass

    label("Function_7_10EE")

    TalkBegin(0xC)

    ChrTalk(
        0xFE,
        (
            "姐姐们，\x01",
            "我好期待你们的演出呀。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_7_10EE end

    def Function_8_1123(): pass

    label("Function_8_1123")

    TalkBegin(0xA)

    ChrTalk(
        0xFE,
        (
            "约修亚哥哥刚才\x01",
            "神情慌张地去找那个\x01",
            "银色头发的哥哥了～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_8_1123 end

    def Function_9_1171(): pass

    label("Function_9_1171")

    TalkBegin(0xD)

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "好漂亮的连衣裙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "长大之后\x01",
            "我也一定要穿穿看。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_9_1171 end

    def Function_10_11CE(): pass

    label("Function_10_11CE")

    TalkBegin(0xB)

    ChrTalk(
        0xFE,
        (
            "#752F怎么样，\x01",
            "找到约修亚了吗？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_10_11CE end

    def Function_11_11FA(): pass

    label("Function_11_11FA")

    AddParty(0x1, 0xFF)
    EventBegin(0x0)
    OP_6D(60000, 1000, 15800, 0)
    OP_67(0, 6230, -10000, 0)
    OP_6B(1420, 0)
    OP_6C(0, 0)
    OP_6E(672, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x101, 60020, 1000, 13500, 0)
    SetChrPos(0x105, 61000, 1000, 14070, 315)
    SetChrPos(0x102, 59020, 1000, 14260, 45)
    SetChrPos(0x9, 59630, 1000, 15700, 180)
    SetChrPos(0x8, 60430, 1000, 15570, 180)
    OP_20(0x0)
    FadeToDark(0, 0, -1)
    Sleep(3000)
    OP_1E()
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#644F#2P大道具、小道具全准备妥当了……\x02\x03",
            "灯光也调整好了……\x02\x03",
            "#641F好！\x01",
            "这样一切都准备好了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#730F#1P差不多可以对外开放了。\x02\x03",
            "离上演还有点时间，\x01",
            "在那之前你们先四处玩玩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F那是当然的啦⊙\x02\x03",
            "我要去把小吃摊\x01",
            "一个个地逛个够才行～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F逛逛倒是没什么关系……\x02\x03",
            "不过可别吃得太撑，\x01",
            "万一演到一半动不了可就不妙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这、这我知道啦。\x02\x03",
            "#000F说起来……\x01",
            "大家要一起去逛吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#640F#2P我和汉斯还有学生会的事要做，\x01",
            "所以就不能陪你们去了。\x02\x03",
            "你们自己玩得开心点吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#044F学生会的事……\x01",
            "难道是昨天说的那件？\x02\x03",
            "我也去帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#648F#2P不用不用。\x02\x03",
            "你就带着艾丝蒂尔他们\x01",
            "在学院里好好逛一圈吧。\x02\x03",
            "而且，\x01",
            "那些小家伙也差不多该到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F嗯……那工作就麻烦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#730F#1P不要紧，有时间的话，\x01",
            "我们也会好好地玩一番哦。\x02\x03",
            "#733F啊，对了，约修亚……\x02\x03",
            "#731F要是在客人当中\x01",
            "看到了我喜欢的那类女生，\x01",
            "记得要悄悄地过来告诉我哦。\x02\x03",
            "我好溜出去找她搭讪㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F是是，知道啦。\x02\x03",
            "#010F漂亮的身材高的\x01",
            "有成熟魅力的大姐姐是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#731F#1P喔，这才是我的好哥们儿⊙\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 1)), scpexpr(EXPR_END)), "loc_18C5")

    ChrTalk(
        0x8,
        "#645F#2P真是的，男生就是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#503F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#045F……哎、这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#643F#2P哎，你们两个怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1925")

    label("loc_18C5")


    ChrTalk(
        0x8,
        "#645F#2P真是的，男生就是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F嗯，真是搞不懂。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#045F呵呵……\x02",
    )

    CloseMessageWindow()

    label("loc_1925")

    OP_22(0xC4, 0x0, 0x64)
    OP_20(0x5DC)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……让各位久等了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "杰尼丝王立学院第５２届学园祭，\x01",
            "现在正式开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_11FA end

    def Function_12_1A6B(): pass

    label("Function_12_1A6B")

    RemoveParty(0x1, 0xFF)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(-34250, 1000, 11220, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x101, -36570, 250, 850, 0)
    SetChrPos(0x105, -36570, 250, 850, 0)
    SetChrPos(0xB, -36570, 250, 850, 0)
    SetChrPos(0xA, -35500, 1000, 9370, 0)
    SetChrPos(0xC, -36440, 1000, 8910, 0)
    SetChrPos(0xD, -37080, 1000, 9450, 0)
    SetChrPos(0xE, -36170, 1000, 9850, 0)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xB, 255)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x105, 0x40)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#771F#4P哇～\x01",
            "看这个，太帅了！\x02\x03",
            "要是我也能穿就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "你太矮了，不行的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我也好想穿穿\x01",
            "这白礼服试试啊～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C15():
        OP_6D(-34950, 1000, 8980, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C15)
    OP_43(0x101, 0x1, 0x0, 0xD)
    OP_43(0x105, 0x1, 0x0, 0xE)
    OP_43(0xB, 0x1, 0x0, 0xF)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#001F呵～呵～\x01",
            "看来大家都很开心嘛。\x02\x03",
            "#004F咦……？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(
        0x101,
        "#004F约修亚去哪里了？\x02",
    )

    CloseMessageWindow()

    def lambda_1CC7():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1CC7)
    Sleep(100)

    def lambda_1CDA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1CDA)

    def lambda_1CE8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1CE8)
    Sleep(100)

    def lambda_1CFB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1CFB)
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(
        0xE,
        (
            "#774F约修亚哥哥？\x02\x03",
            "他把我们\x01",
            "带到这儿之后，\x01",
            "就不知跑到哪儿去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "他说要我们\x01",
            "等着姐姐们过来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F到底怎么回事呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2P嘿嘿～\x01",
            "波利知道哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2P约修亚哥哥\x01",
            "肯定是去找那个\x01",
            "银色头发的哥哥了～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xA, 400)
    TurnDirection(0x101, 0xA, 400)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#501F银色头发的哥哥？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2P就是火灾的时候\x01",
            "把波利和大家\x01",
            "救出来的那位哥哥啦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2P头发是银色的，好漂亮呢～\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#044F那、那个人\x01",
            "在学院里出现了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2P嗯～\x01",
            "不过我只看到了一眼～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2P而且约修亚哥哥\x01",
            "也把眼睛睁得圆圆的看着他呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xE, 0xFF)
    TurnDirection(0xE, 0xA, 400)

    ChrTalk(
        0xE,
        (
            "#772F波利，你这家伙。\x02\x03",
            "为什么那时候\x01",
            "没跟我们说啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2P因为因为，\x01",
            "我那时在忙着吃薄荷饼呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#042F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯……\x02\x03",
            "#002F特蕾莎院长。\x01",
            "我们失陪一下了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "#750F嗯……\x01",
            "你还是快去吧。\x02\x03",
            "科洛丝。\x01",
            "你也陪她一起去吧。\x02\x03",
            "找到约修亚要紧，\x01",
            "你们不用管我们了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xB, 400)

    ChrTalk(
        0x105,
        "#043F对不起，老师……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "哎？\x01",
            "姐姐你们也要走吗～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xE, 400)

    ChrTalk(
        0x105,
        (
            "#045F嗯……抱歉呢。\x02\x03",
            "#040F好好等着舞台剧开演吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(
        0x101,
        (
            "#006F是啊是啊，\x01",
            "大家要睁大眼睛好好看哦⊙\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2500   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1A6B end

    def Function_13_21A2(): pass

    label("Function_13_21A2")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF7478, 0x0, 0xC08, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7AD6, 0x0, 0x143C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7A40, 0x3E8, 0x1CDE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFF7068, 0x3E8, 0x1C20, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_21A2 end

    def Function_14_2204(): pass

    label("Function_14_2204")

    Sleep(500)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF7478, 0x0, 0xC08, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7AD6, 0x0, 0x143C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7A40, 0x3E8, 0x1CDE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFF74AA, 0x3E8, 0x1BEE, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_2204 end

    def Function_15_226B(): pass

    label("Function_15_226B")

    Sleep(500)
    Sleep(700)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF7478, 0x0, 0xC08, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7AD6, 0x0, 0x143C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7A40, 0x3E8, 0x1CDE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFF7842, 0x3E8, 0x2166, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_15_226B end

    def Function_16_22D7(): pass

    label("Function_16_22D7")

    AddParty(0x1, 0xFF)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(2220, 0, 290, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0x22, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x25, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
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
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4D, 0x80)
    SetChrPos(0x1D, 500, 0, 7200, 0)
    SetChrPos(0x1C, -500, 200, 7200, 0)
    SetChrPos(0x1E, -2500, 200, 7200, 0)
    SetChrPos(0x1B, -3500, 200, 7200, 0)
    SetChrPos(0x20, 2500, 200, 5200, 0)
    SetChrPos(0x21, 2500, 200, 7200, 0)
    SetChrPos(0x22, 3500, 0, 7200, 0)
    SetChrPos(0xD, -3500, 200, 3200, 0)
    SetChrPos(0xA, -2500, 200, 3200, 0)
    SetChrPos(0xB, -1500, 200, 3200, 0)
    SetChrPos(0xC, -500, 200, 3200, 0)
    SetChrPos(0xE, 500, 200, 3200, 0)
    SetChrChipByIndex(0xB, 42)
    SetChrSubChip(0xB, 0)
    OP_44(0xD, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    SetChrPos(0x1F, 3500, 200, -800, 0)
    SetChrPos(0x23, 0, -250, -5430, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 4700, 1000, 14420, 180)
    FadeToBright(2000, 0)
    OP_6D(4700, 1000, 14420, 5000)
    OP_8C(0x10, 90, 400)
    OP_8E(0x10, 0x17AC, 0x3E8, 0x394E, 0xBB8, 0x0)
    Fade(1000)
    OP_6D(-34890, 1000, 8480, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x14, -36680, 1000, 9450, 180)
    SetChrPos(0x15, -37710, 1000, 8930, 180)
    SetChrPos(0x16, -37550, 1000, 9790, 180)
    SetChrPos(0x18, 60020, 1000, 18870, 180)
    SetChrPos(0x12, -34800, 1000, 8460, 225)
    SetChrPos(0x13, -34310, 1000, 7560, 270)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0xF, -35990, 1000, 8670, 180)
    SetChrPos(0x11, -36100, 1000, 7440, 270)
    SetChrPos(0x10, -40540, 1000, 6830, 180)
    SetChrPos(0x8, -36960, 1000, 5930, 0)
    SetChrPos(0x9, -37860, 1000, 6000, 0)

    def lambda_2691():

        label("loc_2691")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_2691")

    QueueWorkItem2(0xF, 1, lambda_2691)

    def lambda_26A2():

        label("loc_26A2")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_26A2")

    QueueWorkItem2(0x8, 1, lambda_26A2)

    def lambda_26B3():

        label("loc_26B3")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_26B3")

    QueueWorkItem2(0x9, 1, lambda_26B3)
    OP_8E(0x10, 0xFFFF6D5C, 0x3E8, 0x1D9C, 0xBB8, 0x0)

    NpcTalk(
        0x10,
        "艾丝蒂尔",
        (
            "#343F哇～……\x01",
            "真的好多人呢～\x02\x03",
            "#347F啊～已经开始感到紧张了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "科洛丝",
        (
            "#355F#2P没事的，艾丝蒂尔。\x01",
            "毕竟我们练习了不少时间。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "约修亚",
        (
            "#360F#5P而且只要演出一开始，\x01",
            "就会完全注意不到其他的事了。\x02\x03",
            "因为你是那种\x01",
            "只能专注于一件事的类型嘛。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "艾丝蒂尔",
        (
            "#349F哼，就知道取笑我。\x02\x03",
            "#341F不过算啦，你现在这副样子，\x01",
            "不管说什么我都不会生气哦㈱\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "约修亚",
        "#368F#5P哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#644F好了好了。\x01",
            "打情骂俏就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x8, 400)
    TurnDirection(0x11, 0x8, 400)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#644F……今年的学园祭盛况空前。\x02\x03",
            "虽然有公爵啊市长啊\x01",
            "这样的大人物在，\x01",
            "但是我们也用不着太过紧张。\x02\x03",
            "#648F像练习时那样表演就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#730F#6P这么盛大的学园祭，\x01",
            "全是凭我们自己的双手举办的……\x02\x03",
            "#731F就让我们坚持到最后，\x01",
            "来个花团锦簇的完美结局吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Call(0, 22)
    OP_6D(63040, 4300, 7500, 0)
    OP_20(0x3E8)
    OP_72(0x9, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_44(0xF, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Sleep(1000)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x80)
    OP_22(0x8B, 0x0, 0x64)
    Sleep(9000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……让各位观众久等了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由学生会主办的历史剧『白花恋诗』，\x01",
            "现在正式开演。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请各位观众慢慢地\x01",
            "欣赏这部经典的舞台剧吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1500, 0)
    OP_0D()
    SetMapFlags(0x4)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x2E, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x26, 0x40)
    SetChrFlags(0x26, 0x4)
    SetChrPos(0x26, 63580, 2000, 13750, 180)
    SetChrPos(0x8, 63580, 1000, 13750, 180)

    label("loc_2C32")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C57")
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C53")
    Jump("loc_2C57")

    label("loc_2C53")

    OP_48()
    Jump("loc_2C32")

    label("loc_2C57")

    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#647F#5P时值七耀历１１００年……\x02\x03",
            "１００年前的利贝尔，\x01",
            "贵族制度还依然存在着。\x02\x03",
            "#642F同时，以商人为中心的\x01",
            "平民势力也开始崭露头角……\x02\x03",
            "贵族势力与平民势力之间的\x01",
            "对立和争斗日趋激烈。\x02\x03",
            "#647F王家和教会的居间调停\x01",
            "也无法化解双方的矛盾……\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0x5D)
    SetChrPos(0xF, 60000, 1000, 14400, 180)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2E82():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2E82)

    label("loc_2E8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EB3")
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EAF")
    Jump("loc_2EB3")

    label("loc_2EAF")

    OP_48()
    Jump("loc_2E8E")

    label("loc_2EB3")

    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x8,
        (
            "#644F#5P就在那样的时代……\x02\x03",
            "当时的国王病逝之后，\x01",
            "大约过了一年左右……\x02\x03",
            "一个早春的夜晚，\x01",
            "在格兰赛尔城顶层的空中庭园中，\x01",
            "故事开始了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F92():
        OP_8F(0xFE, 0xEA60, 0x8FC, 0x3CC8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_2F92)

    def lambda_2FAD():
        OP_6D(60010, 4300, 7500, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2FAD)
    OP_8C(0x8, 315, 400)
    OP_8E(0x8, 0xF30C, 0x3E8, 0x3D72, 0x7D0, 0x0)
    OP_8E(0x8, 0xF4BA, 0x3E8, 0x422C, 0x7D0, 0x0)
    OP_8E(0x8, 0x10040, 0x3E8, 0x4934, 0x7D0, 0x0)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x26, 0x1)
    SetChrPos(0x13, 55350, 1000, 17130, 90)
    SetChrPos(0x12, 55440, 1000, 18180, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_77(0x5A, 0x5A, 0x5A, 0x3E800, 0x0)
    WaitChrThread(0x26, 0x1)
    Sleep(1500)

    ChrTalk(
        0xF,
        (
            "#363F#5P街道的光华，是人的灵魂在闪耀……\x02\x03",
            "那点点灯火之下，\x01",
            "人们沉醉于各自的幸福中。\x02\x03",
            "#365F啊啊，然而我却……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)

    def lambda_30D9():
        OP_8E(0xFE, 0xEFCE, 0x3E8, 0x41F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_30D9)
    Sleep(700)

    def lambda_30F9():
        OP_8E(0xFE, 0xE54C, 0x3E8, 0x413C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_30F9)
    WaitChrThread(0x13, 0x1)

    def lambda_3119():
        OP_8C(0xFE, 135, 300)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3119)
    WaitChrThread(0x12, 0x1)

    def lambda_312C():
        OP_8C(0xFE, 225, 300)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_312C)
    Sleep(500)

    ChrTalk(
        0x13,
        (
            "#1P公主殿下……\x01",
            "原来您在这儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#2P是时候就寝了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#2P如此深夜还未作息，\x01",
            "会累坏身子的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#363F#5P不要紧。\x01",
            "如果我病倒了……\x02\x03",
            "就不会成为\x01",
            "点燃这场利贝尔纷争的火种。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1P啊，公主殿下，\x01",
            "请千万不要这么说！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#2P公主殿下是利贝尔的至宝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#2P将会与优秀的驸马殿下结合，\x01",
            "共同治理王国。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#367F#5P我，不会成婚的。\x02\x03",
            "虽说是父王的遗言，\x01",
            "但仅此一事无论如何也……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#1P为什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1P有那样杰出的求婚者，\x01",
            "而且还是两位……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#2P一位是公爵家的长子，\x01",
            "近卫骑士团长尤利乌斯大人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1P另一位是，虽为平民出身，\x01",
            "却在与帝国的战斗中功勋卓著的\x01",
            "猛将奥斯卡大人……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x12,
        "#2P#1K啊～两位都是那么无懈可击㈱\x02",
    )


    ChrTalk(
        0x13,
        "#1P#1K啊～两位都是那么无懈可击㈱\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    OP_56(0x1)
    OP_59()
    Sleep(400)

    ChrTalk(
        0xF,
        (
            "#363F#5P………………………………\x02\x03",
            "他们都是优秀的人物，\x01",
            "这点我比谁都更加清楚。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 180, 300)
    Sleep(200)
    OP_8E(0xF, 0xEA74, 0x3E8, 0x3142, 0x5DC, 0x0)
    SetChrChipByIndex(0xF, 41)
    SetChrFlags(0xF, 0x2)
    OP_99(0xF, 0x0, 0x4, 0x3E8)
    Sleep(400)

    ChrTalk(
        0xF,
        (
            "#365F#5P啊，奥斯卡、尤利乌斯……\x02\x03",
            "我到底……\x01",
            "该选择谁才好呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_1F(0x5A, 0xC8)
    OP_66(0x1)
    OP_6D(3120, 0, 7140, 0)
    Call(0, 23)
    OP_0D()

    ChrTalk(
        0x21,
        (
            "#611F#5P（啊，那名公主殿下……\x01",
            "　不就是约修亚吗。）\x02\x03",
            "（呵呵，竟然是男女反串……\x01",
            "　看来乔儿也真是煞费苦心了啊。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#621F#2P（是的，小姐。）\x02\x03",
            "#623F（约修亚先生的演技自不必说，\x01",
            "　但他身边的两名侍女实在是……）\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    Call(0, 22)
    OP_71(0x9, 0x4)
    OP_72(0xA, 0x4)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 61060, 1000, 14810, 242)
    SetChrPos(0x11, 58970, 1000, 12820, 47)
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x26, 0x0, 0x0, 0x12)
    OP_1D(0x5E)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#420F#2P还记得吗，奥斯卡？\x02\x03",
            "小时候，提着半截木棍\x01",
            "在这小胡同里四处乱跑的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#352F尤利乌斯……\x01",
            "我怎么会忘得了呢。\x02\x03",
            "那些和你、还有塞茜莉亚殿下\x01",
            "一起度过的无忧无虑的快乐日子……\x02\x03",
            "是我一生中无可取代的回忆。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    def lambda_3932():

        label("loc_3932")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_3932")

    QueueWorkItem2(0x11, 0, lambda_3932)
    OP_8E(0x10, 0xEE3E, 0x3E8, 0x323C, 0x7D0, 0x0)

    ChrTalk(
        0x10,
        (
            "#420F呵呵，那时真是吃了一惊。\x02\x03",
            "没想到偷偷溜去玩的\x01",
            "竟然不止我一个……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x11, 0xFF)
    OP_8C(0x11, 180, 300)

    ChrTalk(
        0x11,
        (
            "#358F如飘舞散落的樱花般楚楚可怜，\x01",
            "又如清水般纯洁无暇的少女。\x02\x03",
            "塞茜莉亚殿下对我们来说，\x01",
            "简直就是如同太阳般的存在。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 225, 300)

    ChrTalk(
        0x10,
        (
            "#421F然而，\x01",
            "那份光辉却日渐蒙上阴影。\x02\x03",
            "贵族势力和平民势力……\x02\x03",
            "两者的对立\x01",
            "已迎来无可回避的局面。\x02\x03",
            "#424F公主的叹息也无可奈何……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 135, 300)

    ChrTalk(
        0x11,
        (
            "#359F而且……\x01",
            "啊啊，的确是难以言表。\x02\x03",
            "加深了那叹息的并非他人，\x01",
            "正是我们二人。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_1F(0x5A, 0xC8)
    OP_6D(-1340, 0, 3500, 0)
    Call(0, 23)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#5P（呀呀！\x01",
            "　姐姐他们好酷呢！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#774F#2P（虽、虽然不服气……\x01",
            "　不过简直比男人还帅啊……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#751F#5P（呵呵……\x01",
            "　大家安安静静地看哦。）\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 22)
    OP_71(0xA, 0x4)
    OP_72(0xB, 0x4)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x14, 37)
    SetChrPos(0x14, 57800, 1200, 17630, 135)
    SetChrPos(0x10, 60510, 1000, 13460, 315)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x26, 0x0, 0x0, 0x13)
    FadeToBright(1000, 0)
    OP_1D(0x5F)
    OP_0D()

    ChrTalk(
        0x14,
        "#5P尤利乌斯，你该明白吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P不能再让平民势力\x01",
            "继续增大下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P若是有一天，\x01",
            "我们要尊奉的主人是平民出身……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P那么，拥有优秀传统的利贝尔\x01",
            "就将会威严扫地。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x10, 0xE6F0, 0x3E8, 0x3B38, 0x7D0, 0x0)

    ChrTalk(
        0x10,
        (
            "#424F#2P恕我直言，父亲大人……\x02\x03",
            "自东方的共和国建国以来，\x01",
            "到现在已过了１０年的岁月。\x02\x03",
            "#421F我想，平民势力的抬头，\x01",
            "恐怕也是时代趋势的必然。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F16():

        label("loc_3F16")

        TurnDirection(0xFE, 0x14, 0)
        OP_48()
        Jump("loc_3F16")

    QueueWorkItem2(0x10, 0, lambda_3F16)
    SetChrChipByIndex(0x14, 12)
    OP_96(0x14, 0xE0A6, 0x3E8, 0x4286, 0x12C, 0x1388)
    OP_8E(0x14, 0xE07E, 0x3E8, 0x3BB0, 0xBB8, 0x0)
    TurnDirection(0x14, 0x10, 800)

    ChrTalk(
        0x14,
        "#5P#3S别说这种混帐话！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrFlags(0x14, 0x40)
    OP_92(0x14, 0x10, 0x190, 0xBB8, 0x0)

    def lambda_3FB1():
        OP_94(0x1, 0x14, 0x0, 0x12C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3FB1)
    OP_94(0x1, 0x10, 0xB4, 0x258, 0xBB8, 0x0)
    OP_94(0x1, 0x10, 0xB4, 0x12C, 0x5DC, 0x0)
    WaitChrThread(0x14, 0x3)

    ChrTalk(
        0x14,
        "#5P#3S什么叫自由！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrFlags(0x14, 0x40)
    OP_92(0x14, 0x10, 0x190, 0xBB8, 0x0)

    def lambda_402A():
        OP_94(0x1, 0x14, 0x0, 0x12C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_402A)
    OP_94(0x1, 0x10, 0xB4, 0x258, 0xBB8, 0x0)
    OP_94(0x1, 0x10, 0xB4, 0x12C, 0x5DC, 0x0)
    WaitChrThread(0x14, 0x3)

    ChrTalk(
        0x14,
        "#5P#3S什么叫平等！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P根本就是丢弃传统，\x01",
            "将高贵和下贱混为一谈的无耻想法！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P就算向帝国投降，\x01",
            "也远比屈膝于平民之下要好！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x10,
        "#422F#2P#3S父亲大人！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_1F(0x5A, 0xC8)
    OP_44(0x10, 0xFF)
    OP_77(0x5A, 0x5A, 0x5A, 0x0, 0x0)
    OP_6D(20, 0, 6850, 0)
    Call(0, 23)
    OP_0D()

    ChrTalk(
        0x1C,
        (
            "#227F嗝……\x01",
            "这公爵说的也是理所当然啊。\x02\x03",
            "容许平民放肆的话，\x01",
            "就只会让利贝尔威严扫地而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#722F（公爵大人……\x01",
            "　请您说话时稍微小声些……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 22)
    OP_71(0xB, 0x4)
    OP_72(0xC, 0x4)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x26, 0x0, 0x0, 0x15)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x15, 58930, 1000, 17140, 138)
    SetChrPos(0x11, 61080, 1000, 15250, 336)

    def lambda_433E():

        label("loc_433E")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_433E")

    QueueWorkItem2(0x11, 1, lambda_433E)
    OP_1F(0x64, 0xC8)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x15,
        (
            "#5P奥斯卡。\x01",
            "我对你抱有很高的期望。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P只要得到王家的支持，\x01",
            "那我们必定压倒贵族派。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P这样一来，\x01",
            "我们平民派就能掌握主导权了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#352F#2P但是议长……\x01",
            "请恕我无法接受。\x02\x03",
            "我不能为了如此的政治目的，\x01",
            "而利用纯洁的塞茜莉亚殿下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5P哼哼，说得真是清高。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P虽说国王只是空有名号，\x01",
            "但这毕竟是千载难逢的机会。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x15, 0xE678, 0x3E8, 0x348A, 0x7D0, 0x0)
    OP_8C(0x15, 223, 300)
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "#5P如果你拒绝，\x01",
            "那唯有发起流血的革命了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P不要说贵族，\x01",
            "就连王族也要消失在历史的黑暗之中。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x11,
        "#356F#2P#3S议长！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_44(0x26, 0xFF)
    Sleep(100)
    Fade(1000)
    OP_1F(0x5A, 0xC8)
    OP_44(0x11, 0xFF)
    OP_77(0x5A, 0x5A, 0x5A, 0x0, 0x0)
    OP_6D(-2940, 0, 7230, 0)
    Call(0, 23)
    OP_0D()

    ChrTalk(
        0x1E,
        (
            "#661F（嗯，了不起啊。\x01",
            "　时代考证的确做得相当精细。）\x02\x03",
            "（最先听说是男女反串时，\x01",
            "　我还担心他们不知会弄出什么来呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#781F（呵呵，\x01",
            "　这都是全体学生努力的成果。）\x02\x03",
            "#780F（而且还要多亏\x01",
            "　那两名游击士的鼎力协助……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 22)
    OP_71(0xC, 0x4)
    OP_72(0xD, 0x4)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x26, 60000, 1000, 14500, 135)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x11, 59530, 1000, 13290, 135)
    SetChrPos(0x16, 64230, 1000, 18550, 60)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_1F(0x64, 0xC8)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#357F#5P我绝不能允许\x01",
            "有任何流血革命发生……\x02\x03",
            "绝不能让尤利乌斯和\x01",
            "塞茜莉亚殿下遭遇不测……\x02\x03",
            "#359F我到底……\x01",
            "该怎么做才好呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_77(0x5A, 0x5A, 0x5A, 0x7D000, 0x0)

    def lambda_48EA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_48EA)
    OP_8E(0x16, 0xF122, 0x3E8, 0x418C, 0x7D0, 0x0)

    ChrTalk(
        0x16,
        "#10A#5P呃……\x05\x02",
    )


    def lambda_4929():
        TurnDirection(0x11, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4929)
    OP_97(0x16, 0xF38E, 0x3D22, 0xFFFE2B40, 0x7D0, 0x0)
    OP_97(0x16, 0xF38E, 0x3D22, 0x2710, 0xFA0, 0x0)
    OP_97(0x16, 0xF38E, 0x3D22, 0xFFFFD8F0, 0xFA0, 0x0)

    def lambda_4976():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_4976)
    OP_9E(0x16, 0x1E, 0x0, 0x1F4, 0xBB8)

    ChrTalk(
        0x16,
        (
            "#5P呜呜……\x01",
            "不行了……好恶心……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x16, 400)
    TurnDirection(0x11, 0x16, 400)

    ChrTalk(
        0x11,
        "#354F#5P啊，你没事吧？\x02",
    )

    CloseMessageWindow()
    OP_8E(0x11, 0xEDB2, 0x3E8, 0x3610, 0x7D0, 0x0)

    ChrTalk(
        0x11,
        (
            "#352F#5P喝得太多会伤身子。\x02\x03",
            "就算已经到了春天，\x01",
            "睡在这种地方还是会着凉的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x11, 200)

    ChrTalk(
        0x16,
        (
            "#2P呜呜……好心的骑士大人……\x01",
            "真是谢谢您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#357F#5P不要叫我骑士大人了……\x01",
            "其实我并不是什么大人物。\x02\x03",
            "#359F只是一个不知自己该做什么，\x01",
            "迷失了方向的傻瓜罢了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#2P一点都没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#354F#5P什么？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x16, 0x4)
    OP_92(0x16, 0x11, 0x190, 0x1F40, 0x0)
    OP_22(0x1FD, 0x0, 0x64)

    def lambda_4BC0():
        OP_94(0x1, 0x16, 0x0, 0x12C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4BC0)
    TurnDirection(0x11, 0x16, 0)
    OP_94(0x1, 0x11, 0xB4, 0x3E8, 0x1F40, 0x0)
    OP_94(0x1, 0x11, 0xB4, 0x1F4, 0xFA0, 0x0)
    LoadEffect(0x0, "map\\\\mp020_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 60320, 1050, 12670, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x16, 0x3)
    OP_77(0xA0, 0x1E, 0x1E, 0x5DC00, 0x0)
    Fade(1000)
    SetChrChipByIndex(0x11, 34)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(500)
    OP_9E(0x11, 0x1E, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x11,
        "#430F呜，我的手……\x02",
    )

    CloseMessageWindow()
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x16, 0xF44C, 0x76C, 0x3BEC, 0x708, 0x1388)

    ChrTalk(
        0x16,
        (
            "#2P嘿嘿嘿……\x01",
            "这匕首上涂有麻药。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#2P你就老老实实地认命吧。\x02",
    )

    CloseMessageWindow()
    OP_99(0x11, 0x0, 0x4, 0x320)

    ChrTalk(
        0x11,
        (
            "#356F你……\x01",
            "是谁派你来行刺的！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x16,
        "暗杀者",
        (
            "#2P某位大人嫌你十分碍眼，\x01",
            "于是他就请了我来收拾你。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x16,
        "暗杀者",
        (
            "#2P定金也给得很大方，\x01",
            "你就给我去死吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    ClearMapFlags(0x4)
    OP_77(0x5A, 0x5A, 0x5A, 0x0, 0x0)
    SetMapFlags(0x4)
    OP_6D(5120, 0, 670, 0)
    Call(0, 23)
    OP_1F(0x5A, 0xC8)
    OP_0D()

    ChrTalk(
        0x1F,
        (
            "#141F#5P（原来如此……\x01",
            "　编剧做得很不错啊。）\x02\x03",
            "（之后的剧情又会怎样呢……）\x02\x03",
            "#143F（……坏了坏了。\x01",
            "　差点把正事给忘了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    Call(0, 22)
    OP_71(0xD, 0x4)
    OP_72(0xE, 0x4)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x2)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 40)
    SetChrPos(0x10, 66410, 1000, 16219, 90)
    SetChrPos(0xF, 58610, 1000, 14250, 315)
    FadeToBright(1000, 0)
    OP_1D(0x60)
    OP_0D()
    OP_8E(0x10, 0xF046, 0x3E8, 0x3732, 0x7D0, 0x0)
    OP_8C(0x10, 225, 400)

    ChrTalk(
        0x10,
        "#420F好久不见了，公主。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 135, 400)

    ChrTalk(
        0xF,
        (
            "#360F#5P尤利乌斯……\x01",
            "真是好久不见了……\x02\x03",
            "今天……\x01",
            "没和奥斯卡一起来吗。\x02\x03",
            "父王还健在的时候……\x01",
            "你们在宫廷谈笑风生的英姿，\x01",
            "曾经让侍女们仰慕不已呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#424F……公主您也知道，\x01",
            "王国正面临存亡的危机。\x02\x03",
            "要我和他亲密如初，\x01",
            "恐怕已是遥不可及的梦想了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#363F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#421F今天，\x01",
            "我是来向公主请求一件事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#364F#5P请求……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#421F我和奥斯卡……\x02\x03",
            "请允许我们，以近卫骑士团长\x01",
            "与青年猛将的身份进行决斗。\x02\x03",
            "并希望胜利者……\x01",
            "能有幸成为公主的夫婿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#362F#5P#3S！！！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(2830, 0, 5700, 0)
    Call(0, 23)
    OP_0D()

    ChrTalk(
        0x20,
        (
            "#182F（呵呵……\x01",
            "　很有戏剧性嘛。）\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 17)
    Return()

    # Function_16_22D7 end

    def Function_17_52F3(): pass

    label("Function_17_52F3")

    EventBegin(0x0)
    SetChrPos(0x101, 56670, 1000, 13640, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    Call(0, 22)
    OP_6D(60000, 4300, 7500, 0)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0xE, 0x4)
    OP_72(0xF, 0x4)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0x22, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x25, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
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
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4D, 0x80)
    SetChrPos(0x1D, 500, 0, 7200, 0)
    SetChrPos(0x1C, -500, 200, 7200, 0)
    SetChrPos(0x1E, -2500, 200, 7200, 0)
    SetChrPos(0x1B, -3500, 200, 7200, 0)
    SetChrPos(0x20, 2500, 200, 5200, 0)
    SetChrPos(0x21, 2500, 200, 7200, 0)
    SetChrPos(0x22, 3500, 0, 7200, 0)
    SetChrPos(0xD, -3500, 200, 3200, 0)
    SetChrPos(0xA, -2500, 200, 3200, 0)
    SetChrPos(0xB, -1500, 200, 3200, 0)
    SetChrPos(0xC, -500, 200, 3200, 0)
    SetChrPos(0xE, 500, 200, 3200, 0)
    SetChrChipByIndex(0xB, 42)
    SetChrSubChip(0xB, 0)
    OP_44(0xD, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    SetChrPos(0x1F, 3500, 200, -800, 0)
    SetChrPos(0x23, 0, -250, -5430, 0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    FadeToBright(1000, 0)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 57100, 1000, 14000, 129)
    SetChrPos(0x11, 62900, 1000, 14000, 219)
    SetChrPos(0x15, 62100, 1000, 16600, 225)
    SetChrPos(0x14, 57900, 1000, 16600, 135)
    SetChrPos(0x17, 58300, 1000, 18930, 180)
    SetChrPos(0x18, 60000, 1000, 17730, 180)
    SetChrPos(0x19, 61700, 1000, 18930, 180)
    SetChrPos(0x13, 59250, 1000, 18200, 180)
    SetChrPos(0x12, 60750, 1000, 18200, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 7)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    SetMapFlags(0x4)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x2E, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x26, 0x40)
    SetChrFlags(0x26, 0x4)
    SetChrPos(0x26, 60000, 2000, 12500, 180)
    SetChrPos(0x8, 60000, 1000, 12500, 180)

    label("loc_5725")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_574A")
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5746")
    Jump("loc_574A")

    label("loc_5746")

    OP_48()
    Jump("loc_5725")

    label("loc_574A")

    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#647F#5P在贵族势力和平民势力的\x01",
            "斗争漩涡中身不由己……\x02\x03",
            "曾亲密无间的两位骑士\x01",
            "终于走上了决斗的舞台。\x02\x03",
            "意识到他们决心的公主\x01",
            "也唯有默默无言地面对。\x02\x03",
            "#642F终于到了决斗的那一天……\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0x61)

    def lambda_5847():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5847)

    def lambda_5859():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5859)

    def lambda_586B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_586B)

    def lambda_587D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_587D)

    def lambda_588F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_588F)

    def lambda_58A1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_58A1)

    def lambda_58B3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_58B3)

    def lambda_58C5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_58C5)

    def lambda_58D7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_58D7)

    def lambda_58E9():
        OP_8F(0xFE, 0xEA60, 0x8FC, 0x3CC8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_58E9)

    label("loc_58FE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5923")
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_591F")
    Jump("loc_5923")

    label("loc_591F")

    OP_48()
    Jump("loc_58FE")

    label("loc_5923")

    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x26, 0x1)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#647F王都的王立竞技场上，\x01",
            "挺立着两位骑士的身姿。\x02\x03",
            "贵族、平民、中立人士，\x01",
            "成群结队的人们前来观战……\x02\x03",
            "但是，当中却唯独不见\x01",
            "塞茜莉亚公主的身影。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    def lambda_5A46():

        label("loc_5A46")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5A46")

    QueueWorkItem2(0x15, 1, lambda_5A46)

    def lambda_5A57():

        label("loc_5A57")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5A57")

    QueueWorkItem2(0x14, 1, lambda_5A57)

    def lambda_5A68():

        label("loc_5A68")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5A68")

    QueueWorkItem2(0x17, 1, lambda_5A68)

    def lambda_5A79():

        label("loc_5A79")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5A79")

    QueueWorkItem2(0x18, 1, lambda_5A79)

    def lambda_5A8A():

        label("loc_5A8A")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5A8A")

    QueueWorkItem2(0x19, 1, lambda_5A8A)

    def lambda_5A9B():

        label("loc_5A9B")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5A9B")

    QueueWorkItem2(0x13, 1, lambda_5A9B)

    def lambda_5AAC():

        label("loc_5AAC")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5AAC")

    QueueWorkItem2(0x12, 1, lambda_5AAC)
    OP_8E(0x8, 0xF9B0, 0x3E8, 0x2E40, 0x7D0, 0x0)

    def lambda_5AD1():
        OP_8E(0xFE, 0xFB22, 0x0, 0x1B12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5AD1)
    OP_77(0x5A, 0x5A, 0x5A, 0x7D000, 0x0)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#424F挚友啊。\x01",
            "事已至此你我别无选择……\x02\x03",
            "命中注定\x01",
            "我们终要决一雌雄。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x10, 29)
    OP_8C(0x10, 90, 0)
    SetChrSubChip(0x10, 5)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x10,
        (
            "#421F拔剑！\x01",
            "为了彼此所背负的责任！\x02\x03",
            "更为了你我心爱的公主！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x11,
        (
            "#359F所谓命运，\x01",
            "是凭自己的双手开拓的……\x02\x03",
            "本应承担的立场与公主的微笑，\x01",
            "此时此刻是那么的遥远……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#422F你怕了吗，奥斯卡！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#357F然而，此刻驱使着身体的、\x01",
            "这近乎疯狂的热情究竟是什么？\x02\x03",
            "我似乎再次不可避免地\x01",
            "在此与你一决高下……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x11, 31)
    OP_8C(0x11, 270, 0)
    SetChrSubChip(0x11, 5)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x11,
        (
            "#352F在以革命之名的暴风雨\x01",
            "将一切吞没之前……\x02\x03",
            "以手中的剑刃决定命运吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#420F啊啊，\x01",
            "空之女神将见证你我二人的灵魂！\x02\x03",
            "来吧，一决胜负！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#356F来吧！\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x26, 0x0, 0x0, 0x15)
    OP_20(0x3E8)
    OP_21()
    Sleep(1000)
    OP_1D(0x62)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrChipByIndex(0x11, 32)
    SetChrChipByIndex(0x10, 30)

    def lambda_5EDD():
        OP_8E(0xFE, 0xEDE4, 0x3E8, 0x37DC, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5EDD)

    def lambda_5EF8():
        OP_8E(0xFE, 0xE6DC, 0x3E8, 0x3584, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5EF8)
    WaitChrThread(0x11, 0x1)

    def lambda_5F18():
        OP_8E(0xFE, 0xED1C, 0x3E8, 0x37DC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5F18)

    def lambda_5F33():
        OP_8E(0xFE, 0xE7A4, 0x3E8, 0x3584, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5F33)
    SetChrChipByIndex(0x11, 31)
    SetChrChipByIndex(0x10, 29)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0x10, 2)
    WaitChrThread(0x11, 0x1)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_5F7B():
        OP_8F(0xFE, 0xED80, 0x3E8, 0x37DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5F7B)

    def lambda_5F96():
        OP_8F(0xFE, 0xE740, 0x3E8, 0x3584, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5F96)
    WaitChrThread(0x11, 0x1)

    def lambda_5FB6():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5FB6)

    def lambda_5FD0():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5FD0)

    def lambda_5FEA():
        OP_8F(0xFE, 0xEBF0, 0x3E8, 0x36B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5FEA)

    def lambda_6005():
        OP_8F(0xFE, 0xE8D0, 0x3E8, 0x36B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6005)
    Sleep(200)
    OP_8C(0x10, 135, 0)
    OP_8C(0x11, 225, 0)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x11, 0x2)
    SetChrSubChip(0x11, 13)
    SetChrSubChip(0x10, 13)
    OP_8C(0x10, 90, 0)
    OP_8C(0x11, 270, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_605A():
        OP_96(0xFE, 0xF0A0, 0x3E8, 0x36B0, 0x15E, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_605A)

    def lambda_6078():
        OP_96(0xFE, 0xE420, 0x3E8, 0x36B0, 0x15E, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6078)
    WaitChrThread(0x11, 0x1)
    SetChrSubChip(0x11, 12)
    SetChrSubChip(0x10, 12)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(400)

    def lambda_60AF():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x7530, 0x578, 0x2)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_60AF)

    def lambda_60CB():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x7530, 0x578, 0x2)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_60CB)
    WaitChrThread(0x11, 0x1)

    def lambda_60EC():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x7D00, 0x6A4, 0x2)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_60EC)

    def lambda_6108():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x7D00, 0x6A4, 0x2)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6108)
    WaitChrThread(0x11, 0x1)

    def lambda_6129():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x80E8, 0x7D0, 0x2)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6129)

    def lambda_6145():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x80E8, 0x7D0, 0x2)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6145)
    WaitChrThread(0x11, 0x1)

    def lambda_6166():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x7530, 0x5DC, 0x2)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6166)

    def lambda_6182():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x7530, 0x5DC, 0x2)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6182)
    WaitChrThread(0x11, 0x1)

    def lambda_61A3():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x3A98, 0x3E8, 0x2)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_61A3)

    def lambda_61BF():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x3A98, 0x3E8, 0x2)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_61BF)
    WaitChrThread(0x11, 0x1)
    Sleep(400)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x10, 13)

    def lambda_61EF():
        OP_96(0xFE, 0xE790, 0x3E8, 0x349E, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_61EF)
    Sleep(400)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0xD6, 0x0, 0x64)
    SetChrSubChip(0x10, 2)
    SetChrSubChip(0x11, 0)

    def lambda_6226():
        OP_8F(0xFE, 0xE344, 0x3E8, 0x2FD0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6226)
    Sleep(20)
    SetChrSubChip(0x11, 8)

    def lambda_624B():
        OP_8F(0xFE, 0xE344, 0x3E8, 0x2FD0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_624B)
    Sleep(20)

    def lambda_626B():
        OP_8F(0xFE, 0xE344, 0x3E8, 0x2FD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_626B)
    Sleep(20)

    def lambda_628B():
        OP_8F(0xFE, 0xE344, 0x3E8, 0x2FD0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_628B)
    WaitChrThread(0x11, 0x1)
    Sleep(50)
    SetChrSubChip(0x10, 3)
    SetChrSubChip(0x11, 8)

    def lambda_62BA():
        OP_97(0xFE, 0xE790, 0x349E, 0xFFFEA070, 0x1B58, 0x2)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_62BA)
    Sleep(200)

    def lambda_62DB():
        OP_8C(0xFE, 146, 800)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_62DB)
    WaitChrThread(0x11, 0x1)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x11, 9)
    OP_8F(0x11, 0xEA88, 0x3E8, 0x31BA, 0x1F40, 0x0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrSubChip(0x10, 0)
    OP_8F(0x10, 0xE498, 0x3E8, 0x38AE, 0x1F40, 0x0)

    def lambda_632F():
        OP_9E(0xFE, 0x1E, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_632F)
    OP_9E(0x10, 0x1E, 0x0, 0x190, 0xFA0)
    SetChrSubChip(0x10, 8)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    SetChrSubChip(0x10, 10)
    OP_8C(0x11, 270, 0)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x10, 11)
    SetChrSubChip(0x11, 12)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_6390():
        OP_96(0xFE, 0xEABA, 0x3E8, 0x393A, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6390)
    WaitChrThread(0x11, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x10, 5)
    Sleep(300)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x10, 7)

    def lambda_63CC():
        OP_8E(0xFE, 0xEE84, 0x3E8, 0x39A8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_63CC)
    Sleep(50)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x11, 13)

    def lambda_63F6():
        OP_96(0xFE, 0xE6FA, 0x3E8, 0x39A8, 0x640, 0x1B58)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_63F6)
    WaitChrThread(0x11, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x11, 12)
    OP_8C(0x11, 269, 0)
    WaitChrThread(0x10, 0x1)
    SetChrSubChip(0x10, 12)
    OP_8C(0x10, 91, 0)
    Sleep(300)
    SetChrSubChip(0x10, 6)
    SetChrSubChip(0x11, 6)

    def lambda_644A():
        OP_8C(0x10, 225, 700)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_644A)

    def lambda_6458():
        OP_8C(0x11, 135, 700)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6458)

    def lambda_6466():
        OP_8F(0xFE, 0xED1C, 0x3E8, 0x39A8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6466)

    def lambda_6481():
        OP_8F(0xFE, 0xE7A4, 0x3E8, 0x39A8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6481)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_64AB():
        OP_9E(0xFE, 0x14, 0x0, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_64AB)

    def lambda_64C5():
        OP_9E(0xFE, 0x14, 0x0, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_64C5)
    Sleep(100)

    def lambda_64E4():
        OP_8F(0xFE, 0xEEAC, 0x3E8, 0x39A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_64E4)

    def lambda_64FF():
        OP_8F(0xFE, 0xE614, 0x3E8, 0x39A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_64FF)
    Sleep(300)
    OP_8C(0x10, 270, 0)
    OP_8C(0x11, 90, 0)

    def lambda_652D():
        OP_8F(0xFE, 0xED1C, 0x3E8, 0x39A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_652D)

    def lambda_6548():
        OP_8F(0xFE, 0xE7A4, 0x3E8, 0x39A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6548)
    Sleep(100)
    OP_8C(0x10, 315, 0)
    OP_8C(0x11, 45, 0)
    Sleep(1000)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0x10, 270, 0)
    OP_8C(0x11, 90, 0)

    def lambda_658E():
        OP_96(0xFE, 0xE290, 0x3E8, 0x39D0, 0x190, 0x1F40)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_658E)

    def lambda_65AC():
        OP_96(0xFE, 0xF230, 0x3E8, 0x39D0, 0x190, 0x1F40)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_65AC)
    WaitChrThread(0x11, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x10, 3)
    SetChrSubChip(0x11, 3)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x10, 0x4)

    def lambda_65ED():
        OP_96(0xFE, 0xE86C, 0xBB8, 0x39D0, 0x802, 0x1F40)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_65ED)

    def lambda_660B():
        OP_96(0xFE, 0xEC54, 0xBB8, 0x39D0, 0x802, 0x1F40)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_660B)
    WaitChrThread(0x11, 0x1)
    SetChrPos(0x11, 60000, 3000, 14800, 90)
    SetChrPos(0x10, 60000, 3000, 14800, 270)
    SetChrChipByIndex(0x11, 33)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x10, 0x80)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_6664():
        OP_8C(0xFE, 270, 700)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_6664)

    def lambda_6672():
        OP_8C(0xFE, 90, 700)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_6672)

    def lambda_6680():
        OP_96(0xFE, 0xEA06, 0x3E8, 0x39D0, 0x0, 0x1770)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6680)

    def lambda_669E():
        OP_96(0xFE, 0xEABA, 0x3E8, 0x39D0, 0x0, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_669E)
    WaitChrThread(0x11, 0x1)

    def lambda_66C1():

        label("loc_66C1")

        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xDAC)
        OP_48()
        Jump("loc_66C1")

    QueueWorkItem2(0x11, 2, lambda_66C1)

    def lambda_66DE():

        label("loc_66DE")

        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xDAC)
        OP_48()
        Jump("loc_66DE")

    QueueWorkItem2(0x10, 2, lambda_66DE)
    Sleep(1000)

    ChrTalk(
        0x11,
        "#352F#2P不错啊，尤利乌斯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#420F#1P彼此彼此。\x02\x03",
            "但是，似乎……\x01",
            "你心中仍存留着迷茫吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x11, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrChipByIndex(0x11, 31)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x11, 60500, 1000, 14800, 270)
    SetChrPos(0x10, 59500, 1000, 14800, 90)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x10, 5)
    OP_96(0x10, 0xE5B0, 0x3E8, 0x39D0, 0x190, 0x1770)
    SetChrSubChip(0x10, 6)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_67D9():
        OP_8F(0xFE, 0xEA60, 0x3E8, 0x396C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_67D9)

    def lambda_67F4():
        OP_8F(0xFE, 0xF230, 0x3E8, 0x39D0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_67F4)
    Sleep(30)

    def lambda_6814():
        OP_8F(0xFE, 0xF230, 0x3E8, 0x39D0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6814)
    Sleep(30)

    def lambda_6834():
        OP_8F(0xFE, 0xF230, 0x3E8, 0x39D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6834)
    Sleep(30)

    def lambda_6854():
        OP_8F(0xFE, 0xF230, 0x3E8, 0x39D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6854)
    WaitChrThread(0x11, 0x1)
    SetChrSubChip(0x10, 5)
    Sleep(100)
    SetChrSubChip(0x10, 7)

    def lambda_6883():
        OP_8F(0xFE, 0xF0AA, 0x3E8, 0x39DA, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6883)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0xD6, 0x0, 0x64)
    OP_8C(0x11, 315, 0)

    def lambda_68AF():
        OP_8F(0xFE, 0xF618, 0x3E8, 0x37DC, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_68AF)
    Sleep(30)

    def lambda_68CF():
        OP_8F(0xFE, 0xF618, 0x3E8, 0x37DC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_68CF)
    Sleep(30)

    def lambda_68EF():
        OP_8F(0xFE, 0xF618, 0x3E8, 0x37DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_68EF)
    Sleep(30)

    def lambda_690F():
        OP_8F(0xFE, 0xF618, 0x3E8, 0x37DC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_690F)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x10, 0x1)
    SetChrSubChip(0x10, 6)

    def lambda_6939():
        OP_9E(0xFE, 0x14, 0x0, 0x258, 0xDAC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6939)

    def lambda_6953():
        OP_9E(0xFE, 0x14, 0x0, 0x258, 0xDAC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6953)
    Sleep(300)

    def lambda_6972():
        OP_8F(0xFE, 0xF348, 0x3E8, 0x3A20, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6972)

    def lambda_698D():
        OP_8F(0xFE, 0xF618, 0x3E8, 0x36B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_698D)
    WaitChrThread(0x10, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_69B2():

        label("loc_69B2")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_69B2")

    QueueWorkItem2(0x10, 1, lambda_69B2)

    def lambda_69C3():

        label("loc_69C3")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_69C3")

    QueueWorkItem2(0x11, 3, lambda_69C3)

    def lambda_69D4():
        OP_97(0xFE, 0xF0AA, 0x39DA, 0x15F90, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_69D4)
    WaitChrThread(0x11, 0x2)
    SetChrSubChip(0x10, 5)
    SetChrSubChip(0x11, 12)

    def lambda_69FF():
        OP_8F(0xFE, 0xE862, 0x3E8, 0x39EE, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_69FF)
    Sleep(30)

    def lambda_6A1F():
        OP_8F(0xFE, 0xE862, 0x3E8, 0x39EE, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A1F)
    Sleep(30)

    def lambda_6A3F():
        OP_8F(0xFE, 0xE862, 0x3E8, 0x39EE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A3F)
    Sleep(30)

    def lambda_6A5F():
        OP_8F(0xFE, 0xE862, 0x3E8, 0x39EE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A5F)
    Sleep(30)

    def lambda_6A7F():
        OP_8F(0xFE, 0xE862, 0x3E8, 0x39EE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A7F)
    Sleep(30)

    def lambda_6A9F():
        OP_8F(0xFE, 0xE862, 0x3E8, 0x39EE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A9F)
    WaitChrThread(0x11, 0x1)
    Sleep(200)
    SetChrSubChip(0x10, 4)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x11, 0xE100, 0x3E8, 0x39EE, 0x258, 0xFA0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x11, 32)
    ClearChrFlags(0x11, 0x20)
    SetChrSubChip(0x11, 0)

    def lambda_6AF9():
        OP_8F(0xFE, 0xED76, 0x3E8, 0x39A8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6AF9)
    Sleep(380)
    SetChrChipByIndex(0x11, 31)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x20)
    SetChrSubChip(0x10, 2)
    OP_22(0x84, 0x0, 0x64)

    def lambda_6B32():
        OP_8F(0xFE, 0xEFD8, 0x3E8, 0x3A20, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6B32)

    def lambda_6B4D():
        OP_8F(0xFE, 0xE4F2, 0x3E8, 0x3A20, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B4D)
    Sleep(20)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_6B72():
        OP_8F(0xFE, 0xE4F2, 0x3E8, 0x3A20, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B72)
    Sleep(20)

    def lambda_6B92():
        OP_8F(0xFE, 0xE4F2, 0x3E8, 0x3A20, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B92)
    Sleep(20)

    def lambda_6BB2():
        OP_8F(0xFE, 0xE4F2, 0x3E8, 0x3A20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6BB2)
    Sleep(20)

    def lambda_6BD2():
        OP_8F(0xFE, 0xE4F2, 0x3E8, 0x3A20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6BD2)
    Sleep(20)

    def lambda_6BF2():
        OP_8F(0xFE, 0xE4F2, 0x3E8, 0x3A20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6BF2)
    WaitChrThread(0x11, 0x1)
    SetChrSubChip(0x11, 3)
    Sleep(300)

    ChrTalk(
        0x10,
        (
            "#345F#2P怎么了奥斯卡！\x01",
            "你的剑法就仅此而已了吗！？\x02\x03",
            "击退帝国的赫赫战功，\x01",
            "靠的就只是这种程度的本领吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#359F#1P呜……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x11,
        "#356F#1P#3S哦哦哦哦哦！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_44(0x11, 0xFF)
    TurnDirection(0x11, 0x10, 0)

    def lambda_6D0B():

        label("loc_6D0B")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_6D0B")

    QueueWorkItem2(0x10, 1, lambda_6D0B)
    SetChrSubChip(0x11, 13)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_6D26():
        OP_96(0x11, 0xEDE4, 0x3E8, 0x39EE, 0x9C4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6D26)
    Sleep(300)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0x10, 3)

    def lambda_6D58():
        OP_96(0xFE, 0xF1C2, 0x3E8, 0x3354, 0x190, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6D58)
    Sleep(300)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x11, 7)

    def lambda_6D85():
        OP_8E(0x11, 0xF172, 0x3E8, 0x32F0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6D85)
    Sleep(50)
    SetChrSubChip(0x10, 3)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_6DAF():
        OP_96(0xFE, 0xF802, 0x3E8, 0x32A0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6DAF)
    WaitChrThread(0x11, 0x1)
    SetChrSubChip(0x11, 5)
    WaitChrThread(0x10, 0x1)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x11, 6)

    def lambda_6DE6():
        OP_8E(0x11, 0xFA00, 0x3E8, 0x3336, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6DE6)
    Sleep(50)
    SetChrSubChip(0x11, 7)
    SetChrSubChip(0x10, 13)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x10, 0xFD8E, 0xA50, 0x3214, 0x6A4, 0xFA0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x10, 12)
    SetChrSubChip(0x11, 5)
    Sleep(50)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_6E45():
        OP_96(0x10, 0xF028, 0x3E8, 0x3214, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6E45)
    SetChrSubChip(0x10, 12)
    Sleep(50)
    SetChrSubChip(0x11, 5)
    OP_8C(0x11, 270, 400)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x11, 7)

    def lambda_6E88():
        OP_8E(0x11, 0xF550, 0x3E8, 0x31A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6E88)
    Sleep(100)

    def lambda_6EA8():
        OP_8F(0x11, 0xF550, 0x3E8, 0x31A6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6EA8)
    OP_22(0xD6, 0x0, 0x64)
    OP_8C(0x11, 315, 0)
    SetChrSubChip(0x11, 6)
    SetChrSubChip(0x10, 3)
    Sleep(200)

    def lambda_6EDE():
        OP_8F(0x11, 0xF550, 0x3E8, 0x31A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6EDE)
    OP_8C(0x10, 225, 0)

    def lambda_6F00():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xDAC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6F00)

    def lambda_6F1A():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xDAC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6F1A)
    Sleep(400)
    SetChrSubChip(0x10, 8)

    def lambda_6F3E():
        OP_8C(0xFE, 135, 340)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6F3E)

    def lambda_6F4C():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xDAC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6F4C)

    def lambda_6F66():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xDAC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6F66)
    Sleep(400)
    SetChrSubChip(0x10, 9)
    OP_22(0x84, 0x0, 0x64)

    def lambda_6F8F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6F8F)

    def lambda_6F9D():
        OP_96(0xFE, 0xE484, 0x3E8, 0x325A, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6F9D)
    SetChrSubChip(0x11, 2)
    OP_8C(0x11, 270, 0)

    def lambda_6FC7():
        OP_94(0x1, 0x11, 0x0, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6FC7)
    WaitChrThread(0x10, 0x2)
    SetChrSubChip(0x10, 3)
    WaitChrThread(0x11, 0x2)
    Sleep(500)
    SetChrSubChip(0x11, 3)

    def lambda_6FF6():
        OP_8F(0xFE, 0xF014, 0x3E8, 0x325A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6FF6)
    OP_8C(0x11, 270, 0)
    OP_77(0x5A, 0x5A, 0x5A, 0x7D000, 0x0)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            "#357F不愧是尤利乌斯……\x01",
            "何等华丽的剑法啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x11, 0x14, 0x0, 0x1F4, 0xFA0)

    ChrTalk(
        0x11,
        "#430F呜……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#422F奥斯卡，你……\x01",
            "你的手腕受伤了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#352F不……只是擦伤而已。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#422F可我们到目前为止\x01",
            "并未伤及对方……\x02\x03",
            "莫、莫非在决斗前你就……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x15,
        (
            "#2P真卑鄙，拉多公爵！\x01",
            "都是你搞的鬼吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P呵呵呵……\x01",
            "请别含血喷人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5P有证据证明是我指使的吗？\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x10,
        "#422F父亲大人……你竟然这么做。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#357F没关系，尤利乌斯。\x01",
            "这也是因我的不成熟而造成的。\x02\x03",
            "#358F何况，这种程度的伤，\x01",
            "在战场上根本算不了什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#422F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#357F就用下一剑来决定一切吧。\x02\x03",
            "#352F我会……\x01",
            "全力出剑，绝不留情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#421F奥斯卡，你……\x02\x03",
            "#424F明白了……\x01",
            "我也会在下一剑上赌上一切。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_73C7():
        OP_96(0xFE, 0xDBEC, 0x3E8, 0x323C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_73C7)

    def lambda_73E5():
        OP_96(0xFE, 0xF8D4, 0x3E8, 0x323C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_73E5)
    WaitChrThread(0x10, 0x2)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    Fade(1000)
    OP_8C(0x10, 135, 0)
    OP_8C(0x11, 225, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#420F今后的人生、公主的笑颜，\x01",
            "以及王国的未来……\x02\x03",
            "胜者将要\x01",
            "背负所有的责任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#358F而败者则将\x01",
            "化作灵魂守护这一切……\x02\x03",
            "无论胜负如何，都同为骑士的骄傲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#420F呵呵，没错。\x02\x03",
            "#424F……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#357F……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    SetChrSubChip(0x11, 5)
    SetChrSubChip(0x10, 5)
    OP_8C(0x10, 90, 0)
    OP_8C(0x11, 270, 0)
    OP_0D()

    def lambda_759F():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_759F)

    def lambda_75B9():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_75B9)

    ChrTalk(
        0x10,
        "#10A#1P#3S喝啊啊啊啊啊！\x05\x02",
    )


    ChrTalk(
        0x11,
        "#10A#2P#3S哦哦哦哦哦哦！\x05\x02",
    )

    Sleep(1000)
    ClearChrFlags(0x11, 0x20)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x11, 32)
    SetChrChipByIndex(0x10, 30)

    def lambda_7625():
        OP_8E(0xFE, 0xE678, 0x3E8, 0x38C2, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7625)

    def lambda_7640():
        OP_8E(0xFE, 0xEE48, 0x3E8, 0x38C2, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7640)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x40)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7670():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_7670)
    SetChrPos(0xF, 62800, 1000, 18980, 0)

    def lambda_7693():
        OP_8E(0xFE, 0xEA60, 0x3E8, 0x3368, 0x2328, 0x1)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7693)
    OP_20(0x3E8)
    FadeToDark(500, 0, -1)
    Sleep(100)
    OP_22(0x9B, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女孩的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "住手——————！！\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    OP_56(0x0)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x11, 31)
    SetChrChipByIndex(0x10, 29)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0x10, 2)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x10, 0x20)
    OP_44(0xF, 0xFF)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0xF, 0x800)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 35)
    SetChrSubChip(0xF, 0)
    SetChrPos(0xF, 60000, 1000, 13160, 0)
    FadeToBright(300, 0)
    OP_44(0x26, 0xFF)
    SetChrPos(0x26, 60010, 1000, 13880, 0)
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_777A():

        label("loc_777A")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_777A")

    QueueWorkItem2(0x15, 1, lambda_777A)

    def lambda_778B():

        label("loc_778B")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_778B")

    QueueWorkItem2(0x14, 1, lambda_778B)

    def lambda_779C():

        label("loc_779C")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_779C")

    QueueWorkItem2(0x17, 1, lambda_779C)

    def lambda_77AD():

        label("loc_77AD")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_77AD")

    QueueWorkItem2(0x18, 1, lambda_77AD)

    def lambda_77BE():

        label("loc_77BE")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_77BE")

    QueueWorkItem2(0x19, 1, lambda_77BE)

    def lambda_77CF():

        label("loc_77CF")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_77CF")

    QueueWorkItem2(0x13, 1, lambda_77CF)

    def lambda_77E0():

        label("loc_77E0")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_77E0")

    QueueWorkItem2(0x12, 1, lambda_77E0)
    Sleep(1000)

    ChrTalk(
        0xF,
        "#364F啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 3)
    SetChrSubChip(0x11, 3)

    def lambda_7810():
        OP_99(0xFE, 0x0, 0xD, 0x2BC)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7810)

    def lambda_7820():
        OP_8C(0x10, 225, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7820)

    def lambda_782E():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_782E)

    ChrTalk(
        0x10,
        "#422F#13A#2P什…………\x05\x02",
    )


    ChrTalk(
        0x11,
        "#354F#13A#1P塞……茜莉亚……？\x05\x02",
    )

    Sleep(1300)
    SetChrChipByIndex(0x11, 8)

    def lambda_788A():
        OP_8E(0xFE, 0xE86C, 0x3E8, 0x38C2, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_788A)

    def lambda_78A5():

        label("loc_78A5")

        OP_8C(0xFE, 126, 0)
        OP_48()
        Jump("loc_78A5")

    QueueWorkItem2(0x11, 1, lambda_78A5)
    SetChrChipByIndex(0x10, 7)
    ClearChrFlags(0x10, 0x20)

    def lambda_78C0():
        OP_8E(0x10, 0xEE20, 0x3E8, 0x2F8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_78C0)

    def lambda_78DB():

        label("loc_78DB")

        TurnDirection(0x10, 0xF, 0)
        OP_48()
        Jump("loc_78DB")

    QueueWorkItem2(0x10, 1, lambda_78DB)
    WaitChrThread(0xF, 0x1)
    SetChrFlags(0x11, 0x80)
    OP_99(0xF, 0xE, 0x10, 0x3E8)
    Sleep(800)
    OP_1D(0x63)
    Sleep(1000)

    ChrTalk(
        0x10,
        "#422F#3S公、公主——————！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#356F#1P塞茜莉亚，为什么……\x02\x03",
            "你明明不在场的……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xF, 0x10, 0x12, 0x384)
    Sleep(200)

    ChrTalk(
        0xF,
        (
            "#361F太、太好了……\x01",
            "奥斯卡、尤利乌斯……\x02\x03",
            "我本不想目睹\x01",
            "你们两人决斗的……\x02\x03",
            "但终究还是担心……\x01",
            "所以……来阻止你们……\x02\x03",
            "#365F啊啊，幸好赶上了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#359F#5P塞茜莉亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#422F公、公主……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#361F请大家……听我说……\x02\x03",
            "看在我的份上……\x01",
            "请各位停止争斗吧……\x02\x03",
            "大家……都是深爱着利贝尔这片土地的\x01",
            "……难能可贵的伙伴……不是吗……\x02\x03",
            "只是……爱的方式……\x01",
            "有少许不同罢了……\x02\x03",
            "如果大家携起手来……\x01",
            "一定能够冲破这道墙壁的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5P公、公主殿下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#2P够了……\x01",
            "请别再多说话了……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xF, 0x12, 0x11, 0x3E8)

    ChrTalk(
        0xF,
        (
            "#363F啊……眼睛好模糊……\x02\x03",
            "对了……你们两个……\x01",
            "都在……还在……这里吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#343F是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#359F#5P就在你的身边……\x02",
    )

    CloseMessageWindow()
    OP_99(0xF, 0x13, 0x16, 0x2BC)
    Sleep(200)

    ChrTalk(
        0xF,
        (
            "#361F真不可思议……\x01",
            "我又看见那情景了……\x02\x03",
            "小时候……溜出城堡……\x01",
            "在那小胡同里玩耍……\x02\x03",
            "奥斯卡……尤利乌斯……\x01",
            "大家都那样开心地笑着……\x02\x03",
            "我……\x01",
            "好喜欢……你们的笑容……\x02\x03",
            "#365F所…以……请你们……\x02\x03",
            "……永远开心地笑……着……\x02\x03",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xF, 0x16, 0x18, 0x2BC)
    Sleep(160)
    Fade(500)
    OP_99(0xF, 0x19, 0x19, 0x2BC)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#422F#2P公主……？\x02\x03",
            "这不是真的吧，公主！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x10,
        "#423F#2P#3S求求你告诉我这不是真的！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_99(0xF, 0x19, 0x1B, 0x384)

    ChrTalk(
        0x11,
        (
            "#359F#5P塞茜莉亚……我……\x02\x03",
            "#357F………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#5P公主殿下，太不幸了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#2P啊，为什么会发生这种事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P殿下为了阻止我们的纷争，\x01",
            "连自己宝贵的生命也在所不惜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P和这份崇高的节操相比……\x01",
            "贵族的荣誉又是何等的渺小……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P若不是我们互相争斗，\x01",
            "就不会发生这样的憾事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#2P人总是要等大错铸成之后，\x01",
            "才会发觉自己的愚蠢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#2P灵魂为何要被束缚于身体上？\x01",
            "这也是人类之子的宿命吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#2P爱德丝啊，伟大的空之女神。\x01",
            "您为何如此不公……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "看来……\x01",
            "你们还是不明白。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)
    SetChrPos(0x1A, 59990, 7000, 13110, 0)
    OP_22(0xD7, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp005_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 59990, 8500, 13110, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_77(0x1E, 0x1E, 0xA0, 0xFA000, 0x0)
    Sleep(4000)
    OP_99(0xF, 0x1B, 0x19, 0x4B0)
    SetChrName("女性的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……我的确赐予了你们\x01",
            "作为寄宿灵魂而存在的肉体。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "但是，人类的灵魂，\x01",
            "本应是更加崇高而自由的存在。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "轻贱灵魂的不是他人，\x01",
            "正是你们自己。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x17,
        "#5P好、好耀眼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#2P好美妙的声音……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#5P哦哦……天啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5P诸位，真是不胜惶恐，\x01",
            "女神降临了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#422F这就是女神……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#359F#5P何等的庄严啊……\x02",
    )

    CloseMessageWindow()
    SetChrName("女神爱德丝")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "年轻的骑士们啊。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "你们的决斗，\x01",
            "我已经全部目睹了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "虽然勇猛可嘉……\x01",
            "但却缺少了至关重要的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x10,
        "#424F的确如您所说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#352F#5P一切都是\x01",
            "我们的不成熟所造成的……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("女神爱德丝")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "议长啊……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "你太过拘泥于身分的区别。\x01",
            "但是，你是否忘记了，\x01",
            "贵族与王族其实都同样是人。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x15,
        "#2P……真是惭愧万分。\x02",
    )

    CloseMessageWindow()
    SetChrName("女神爱德丝")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "公爵啊……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "自身的罪孽，\x01",
            "你应该最为清楚吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x14,
        "#5P……………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("女神爱德丝")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "还有，\x01",
            "旁观了此事的人们……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "你们也同样\x01",
            "欠缺了一些重要的东西。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请你们将手放在胸前仔细思索。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(400)
    OP_62(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x18, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1600)
    OP_63(0x17)
    OP_63(0x18)
    OP_63(0x19)
    Sleep(400)
    SetChrName("女神爱德丝")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，\x01",
            "看来大家也都各有所悟了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那么，\x01",
            "利贝尔就还应该存有未来。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请将今日之事\x01",
            "永远铭记于心……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    OP_82(0x0, 0x2)
    OP_77(0x0, 0x0, 0x0, 0xBB800, 0x0)
    Sleep(3000)
    OP_21()

    ChrTalk(
        0x13,
        "#5P啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#2P消失了……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0xF,
        "#5P…………嗯………\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_99(0xF, 0x19, 0x16, 0x2BC)
    Sleep(300)
    OP_99(0xF, 0x16, 0x14, 0x352)
    OP_99(0xF, 0x14, 0x16, 0x352)
    Sleep(100)
    OP_99(0xF, 0x16, 0x14, 0x44C)
    OP_99(0xF, 0x14, 0x16, 0x44C)

    ChrTalk(
        0xF,
        "#364F啊……这里是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#422F公、公主！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#354F#5P塞茜莉亚！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#364F啊……\x01",
            "尤利乌斯，奥斯卡……\x02\x03",
            "难道……\x01",
            "连你们也到天国来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#422F#2P#1K………………\x02",
    )


    ChrTalk(
        0x11,
        "#354F#1P#1K………………\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    ChrTalk(
        0x18,
        (
            "#5P这、这……\x01",
            "这简直就是奇迹啊！\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    LoadEffect(0x0, "map\\\\mp016_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 59990, 2000, 13110, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x20)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 59370, 1000, 13750, 126)
    SetChrChipByIndex(0xF, 40)
    ClearChrFlags(0xF, 0x2)
    SetChrSubChip(0xF, 0)
    OP_8C(0xF, 180, 0)
    OP_1D(0x64)
    OP_0D()
    OP_77(0x78, 0x78, 0x78, 0x7D000, 0x0)
    Sleep(2000)

    ChrTalk(
        0x13,
        "#10A#5P公主殿下～！！\x05\x02",
    )

    CloseMessageWindow()

    def lambda_89DA():
        OP_8E(0xFE, 0xE4E8, 0x3E8, 0x37A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_89DA)

    def lambda_89F5():

        label("loc_89F5")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_89F5")

    QueueWorkItem2(0x11, 1, lambda_89F5)

    def lambda_8A06():
        OP_8E(0xFE, 0xEFD8, 0x3E8, 0x37A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_8A06)

    def lambda_8A21():

        label("loc_8A21")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8A21")

    QueueWorkItem2(0x10, 1, lambda_8A21)

    def lambda_8A32():
        OP_8C(0xFE, 0, 300)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8A32)

    def lambda_8A40():
        OP_8E(0xFE, 0xEBF0, 0x3E8, 0x3624, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_8A40)

    def lambda_8A5B():

        label("loc_8A5B")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8A5B")

    QueueWorkItem2(0x12, 1, lambda_8A5B)

    def lambda_8A6C():
        OP_8E(0xFE, 0xE8D0, 0x3E8, 0x3624, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8A6C)

    def lambda_8A87():

        label("loc_8A87")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8A87")

    QueueWorkItem2(0x13, 1, lambda_8A87)

    def lambda_8A98():
        OP_8E(0xFE, 0xE164, 0x3E8, 0x323C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_8A98)

    def lambda_8AB3():

        label("loc_8AB3")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8AB3")

    QueueWorkItem2(0x14, 1, lambda_8AB3)

    def lambda_8AC4():
        OP_8E(0xFE, 0xF35C, 0x3E8, 0x323C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_8AC4)

    def lambda_8ADF():

        label("loc_8ADF")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8ADF")

    QueueWorkItem2(0x15, 1, lambda_8ADF)

    def lambda_8AF0():
        OP_8E(0xFE, 0xE4E8, 0x3E8, 0x41E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_8AF0)

    def lambda_8B0B():

        label("loc_8B0B")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8B0B")

    QueueWorkItem2(0x17, 1, lambda_8B0B)

    def lambda_8B1C():
        OP_8E(0xFE, 0xEFD8, 0x3E8, 0x41E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_8B1C)

    def lambda_8B37():

        label("loc_8B37")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8B37")

    QueueWorkItem2(0x19, 1, lambda_8B37)

    def lambda_8B48():
        OP_8E(0xFE, 0xEA60, 0x3E8, 0x4010, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_8B48)

    def lambda_8B63():

        label("loc_8B63")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8B63")

    QueueWorkItem2(0x18, 1, lambda_8B63)
    WaitChrThread(0x12, 0x2)

    ChrTalk(
        0x12,
        "#2P真是、真是太好了！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#364F哎……？\x01",
            "你们两个怎么会……\x02\x03",
            "啊……\x01",
            "公爵……连议长都……\x02\x03",
            "我……不是应该死了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5P啊，女神啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P感谢您！\x01",
            "将利贝尔的至宝还给了我们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#2P感谢您的大慈大悲！\x02",
    )

    CloseMessageWindow()

    def lambda_8C7A():
        OP_8F(0xFE, 0xED1C, 0x3E8, 0x3BC4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_8C7A)

    def lambda_8C95():
        OP_8F(0xFE, 0xE7A4, 0x3E8, 0x3BC4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8C95)
    WaitChrThread(0x12, 0x2)

    def lambda_8CB5():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8CB5)

    def lambda_8CC3():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8CC3)
    TurnDirection(0xF, 0x10, 300)
    Sleep(500)
    TurnDirection(0xF, 0x11, 300)

    ChrTalk(
        0xF,
        (
            "#362F奥斯卡、尤利乌斯……\x02\x03",
            "这……\x01",
            "究竟是怎么了？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x11, 0xFF)
    OP_44(0x10, 0xFF)

    ChrTalk(
        0x11,
        (
            "#357F#5P塞茜莉亚殿下……\x01",
            "您再也无须担心了。\x02\x03",
            "#358F长久以来的对立已经结束……\x01",
            "一切都开始向着好的方向发展。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#420F#2P你太天真了，奥斯卡。\x02\x03",
            "你我之间的胜负\x01",
            "还未见分晓对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#353F#5P尤利乌斯……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 300)

    ChrTalk(
        0xF,
        (
            "#363F难道……\x01",
            "你们还要继续战斗吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#424F#2P不……\x01",
            "这次的决斗就到此为止了。\x02\x03",
            "因为那个笨蛋\x01",
            "使剑的手腕受了伤。\x02\x03",
            "#420F但是，声势浩大的一场决斗却没有胜者，\x01",
            "这未免太说不过去了。\x02\x03",
            "那么，就将胜利给予在不利条件下\x01",
            "仍能毫不逊色地战斗的人吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#352F#5P等等，尤利乌斯！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x11, 300)
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(
        0x10,
        (
            "#420F#2P别误会，奥斯卡。\x01",
            "这并不代表我放弃了公主。\x02\x03",
            "等你伤愈之后，\x01",
            "我们再来以木剑一决胜负吧。\x02\x03",
            "就像小时候那样，打个痛快。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(
        0x11,
        (
            "#358F#5P这样吗……\x02\x03",
            "呵呵……\x01",
            "好的，我接受了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 300)

    ChrTalk(
        0xF,
        (
            "#367F真是的，你们两个……\x01",
            "完全忽视了我的存在吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)
    TurnDirection(0x11, 0xF, 400)

    ChrTalk(
        0x11,
        (
            "#354F#5P不、不是这个意思……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#420F#2P但是公主……\x01",
            "今天请先给予胜者胜利之吻吧。\x02\x03",
            "因为大家都期待着这一幕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#360F……好的。\x02",
    )

    CloseMessageWindow()

    def lambda_91FD():
        OP_8E(0xFE, 0xE920, 0x3E8, 0x3520, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_91FD)
    OP_8F(0xF, 0xEB28, 0x3E8, 0x3232, 0x5DC, 0x0)
    TurnDirection(0xF, 0x11, 300)
    Sleep(1000)
    SetChrFlags(0x11, 0x80)
    SetChrPos(0xF, 60000, 1000, 13160, 0)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 36)
    SetChrSubChip(0xF, 0)
    Sleep(200)
    OP_99(0xF, 0x0, 0x3, 0x384)
    Sleep(500)
    OP_99(0xF, 0x3, 0x0, 0x384)
    Sleep(200)
    OP_44(0x10, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)

    ChrTalk(
        0x13,
        "#5P哎呀哎呀㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#2P两人好般配呢㈱\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)
    Sleep(400)

    ChrTalk(
        0x10,
        "#420F#2P#3S请空之女神见证！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x10,
        (
            "#420F#2P#3S愿今日的美好，\x01",
            "永世长存！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xF, 0x20)
    ClearChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 40)
    SetChrSubChip(0xF, 0)
    OP_8F(0x11, 0xE678, 0x3E8, 0x358E, 0x3E8, 0x0)
    OP_8C(0x11, 180, 400)
    OP_8C(0xF, 180, 400)
    Sleep(500)
    OP_8C(0x14, 180, 400)
    Sleep(400)

    ChrTalk(
        0x14,
        "#5P#3S愿利贝尔永远和平！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x15, 180, 400)
    Sleep(400)

    ChrTalk(
        0x15,
        "#5P#3S愿利贝尔永远繁荣！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0xF, 0x800)
    OP_22(0xBF, 0x0, 0x64)
    OP_22(0xAF, 0x0, 0x64)
    OP_70(0x5, 0x78)
    OP_73(0x5)
    Sleep(2000)
    Fade(1000)
    OP_1F(0x5A, 0xC8)
    OP_6D(130, 0, -1840, 0)
    Call(0, 23)
    ClearChrFlags(0x23, 0x80)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x23,
        "银发青年",
        (
            "#122F#2P呵呵……\x01",
            "最后果然还是大团圆。\x02\x03",
            "#125F不过……这样也不错啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x23, 180, 400)
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)

    def lambda_94ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_94ED)
    OP_8E(0x23, 0x0, 0x0, 0xFFFFE160, 0x5DC, 0x0)
    SetChrFlags(0x23, 0x80)
    OP_0D()
    OP_21()
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，舞台剧『白花恋诗』\x01",
            "在观众的一片赞叹声中完满地落幕。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "同时，校园里\x01",
            "响起了宣告学园祭结束的广播。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "来参观的客人们\x01",
            "都带着满足的表情离开了学院……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T2513   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_52F3 end

    def Function_18_9655(): pass

    label("Function_18_9655")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96A1")
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_18_9655")

    label("loc_96A1")

    Return()

    # Function_18_9655 end

    def Function_19_96A2(): pass

    label("Function_19_96A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96EE")
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_19_96A2")

    label("loc_96EE")

    Return()

    # Function_19_96A2 end

    def Function_20_96EF(): pass

    label("Function_20_96EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_973B")
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_20_96EF")

    label("loc_973B")

    Return()

    # Function_20_96EF end

    def Function_21_973C(): pass

    label("Function_21_973C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9788")
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_21_973C")

    label("loc_9788")

    Return()

    # Function_21_973C end

    def Function_22_9789(): pass

    label("Function_22_9789")

    OP_6D(60010, 4300, 7500, 0)
    OP_67(0, 840, -10000, 0)
    OP_6B(910, 0)
    OP_6C(0, 0)
    OP_6E(581, 0)
    Return()

    # Function_22_9789 end

    def Function_23_97C7(): pass

    label("Function_23_97C7")

    OP_67(0, 6470, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Return()

    # Function_23_97C7 end

    SaveToFile()

Try(main)
