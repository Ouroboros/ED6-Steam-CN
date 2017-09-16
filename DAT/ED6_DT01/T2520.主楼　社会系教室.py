from ED6ScenarioHelper import *

def main():
    # 主楼　社会系教室

    CreateScenaFile(
        FileName            = 'T2520   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2520.x',
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
        '科林兹校长',                           # 9
        '波利',                                 # 10
        '特蕾莎院长',                           # 11
        '达尼艾尔',                             # 12
        '玛丽',                                 # 13
        '克拉姆',                               # 14
        '基库',                                 # 15
        '珐奥娜',                               # 16
        '拉迪奥老师',                           # 17
        '碧欧拉老师',                           # 18
        '米丽亚老师',                           # 19
        '艾福托老师',                           # 20
        '罗迪',                                 # 21
        '坎诺',                                 # 22
        '雅莉丝',                               # 23
        '黛拉',                                 # 24
        '帕布尔',                               # 25
        '罗基克',                               # 26
        '亚吉鲁',                               # 27
        '罗伊斯',                               # 28
        '莫妮卡',                               # 29
        '塞尔玛',                               # 30
        '莉秋尔',                               # 31
        '巴托姆',                               # 32
        '基诺奇奥',                             # 33
        '妮吉塔',                               # 34
        '芙拉瑟',                               # 35
        '蕾娜',                                 # 36
        '梅贝尔市长',                           # 37
        '杜南公爵',                             # 38
        '管家菲利普',                           # 39
        '奈尔',                                 # 40
        '卡露娜',                               # 41
        '亚鲁瓦教授',                           # 42
        '希艾尔',                               # 43
        '爱蕾塔',                               # 44
        '爱珐',                                 # 45
        '西加罗',                               # 46
        '艾德尔',                               # 47
        '波尔多斯',                             # 48
        '诺莉雅',                               # 49
        '丽泽',                                 # 50
        '托尼奥',                               # 51
        '莉拉',                                 # 52
        '戴尔蒙市长',                           # 53
        '参观客',                               # 54
        '参观客',                               # 55
        '参观客',                               # 56
        '参观客',                               # 57
        '参观客',                               # 58
        '参观客',                               # 59
        '参观客',                               # 60
        '参观客',                               # 61
        '参观客',                               # 62
        'CH22000',                              # 63
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
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02640 ._CH',             # 02
        'ED6_DT07/CH02630 ._CH',             # 03
        'ED6_DT07/CH02570 ._CH',             # 04
        'ED6_DT07/CH02320 ._CH',             # 05
        'ED6_DT07/CH02490 ._CH',             # 06
        'ED6_DT07/CH01660 ._CH',             # 07
        'ED6_DT07/CH01210 ._CH',             # 08
        'ED6_DT07/CH01430 ._CH',             # 09
        'ED6_DT07/CH01460 ._CH',             # 0A
        'ED6_DT07/CH02600 ._CH',             # 0B
        'ED6_DT07/CH01360 ._CH',             # 0C
        'ED6_DT07/CH01580 ._CH',             # 0D
        'ED6_DT07/CH01590 ._CH',             # 0E
        'ED6_DT07/CH01370 ._CH',             # 0F
        'ED6_DT07/CH01090 ._CH',             # 10
        'ED6_DT07/CH01080 ._CH',             # 11
        'ED6_DT07/CH01360 ._CH',             # 12
        'ED6_DT07/CH01590 ._CH',             # 13
        'ED6_DT07/CH02360 ._CH',             # 14
        'ED6_DT07/CH02140 ._CH',             # 15
        'ED6_DT07/CH02470 ._CH',             # 16
        'ED6_DT07/CH02060 ._CH',             # 17
        'ED6_DT07/CH01240 ._CH',             # 18
        'ED6_DT07/CH02050 ._CH',             # 19
        'ED6_DT07/CH01540 ._CH',             # 1A
        'ED6_DT07/CH01170 ._CH',             # 1B
        'ED6_DT07/CH01210 ._CH',             # 1C
        'ED6_DT07/CH01040 ._CH',             # 1D
        'ED6_DT07/CH01130 ._CH',             # 1E
        'ED6_DT07/CH01680 ._CH',             # 1F
        'ED6_DT07/CH01030 ._CH',             # 20
        'ED6_DT07/CH02410 ._CH',             # 21
        'ED6_DT07/CH02370 ._CH',             # 22
        'ED6_DT07/CH02500 ._CH',             # 23
        'ED6_DT06/CH20021 ._CH',             # 24
        'ED6_DT07/CH01200 ._CH',             # 25
        'ED6_DT07/CH02480 ._CH',             # 26
        'ED6_DT07/CH01120 ._CH',             # 27
        'ED6_DT07/CH01030 ._CH',             # 28
        'ED6_DT07/CH01130 ._CH',             # 29
        'ED6_DT07/CH01140 ._CH',             # 2A
        'ED6_DT07/CH01100 ._CH',             # 2B
        'ED6_DT07/CH01180 ._CH',             # 2C
        'ED6_DT07/CH01470 ._CH',             # 2D
        'ED6_DT07/CH01770 ._CH',             # 2E
        'ED6_DT07/CH01780 ._CH',             # 2F
        'ED6_DT07/CH02363 ._CH',             # 30
        'ED6_DT07/CH01373 ._CH',             # 31
        'ED6_DT07/CH01213 ._CH',             # 32
        'ED6_DT07/CH01593 ._CH',             # 33
        'ED6_DT07/CH01043 ._CH',             # 34
        'ED6_DT07/CH01033 ._CH',             # 35
        'ED6_DT07/CH01363 ._CH',             # 36
        'ED6_DT07/CH01690 ._CH',             # 37
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02640P._CP',             # 02
        'ED6_DT07/CH02630P._CP',             # 03
        'ED6_DT07/CH02570P._CP',             # 04
        'ED6_DT07/CH02320P._CP',             # 05
        'ED6_DT07/CH02490P._CP',             # 06
        'ED6_DT07/CH01660P._CP',             # 07
        'ED6_DT07/CH01210P._CP',             # 08
        'ED6_DT07/CH01430P._CP',             # 09
        'ED6_DT07/CH01460P._CP',             # 0A
        'ED6_DT07/CH02600P._CP',             # 0B
        'ED6_DT07/CH01360P._CP',             # 0C
        'ED6_DT07/CH01580P._CP',             # 0D
        'ED6_DT07/CH01590P._CP',             # 0E
        'ED6_DT07/CH01370P._CP',             # 0F
        'ED6_DT07/CH01090P._CP',             # 10
        'ED6_DT07/CH01080P._CP',             # 11
        'ED6_DT07/CH01360P._CP',             # 12
        'ED6_DT07/CH01590P._CP',             # 13
        'ED6_DT07/CH02360P._CP',             # 14
        'ED6_DT07/CH02140P._CP',             # 15
        'ED6_DT07/CH02470P._CP',             # 16
        'ED6_DT07/CH02060P._CP',             # 17
        'ED6_DT07/CH01240P._CP',             # 18
        'ED6_DT07/CH02050P._CP',             # 19
        'ED6_DT07/CH01540P._CP',             # 1A
        'ED6_DT07/CH01170P._CP',             # 1B
        'ED6_DT07/CH01210P._CP',             # 1C
        'ED6_DT07/CH01040P._CP',             # 1D
        'ED6_DT07/CH01210P._CP',             # 1E
        'ED6_DT07/CH01680P._CP',             # 1F
        'ED6_DT07/CH01030P._CP',             # 20
        'ED6_DT07/CH02410P._CP',             # 21
        'ED6_DT07/CH02370P._CP',             # 22
        'ED6_DT07/CH02500P._CP',             # 23
        'ED6_DT06/CH20021P._CP',             # 24
        'ED6_DT07/CH01200P._CP',             # 25
        'ED6_DT07/CH02480P._CP',             # 26
        'ED6_DT07/CH01120P._CP',             # 27
        'ED6_DT07/CH01030P._CP',             # 28
        'ED6_DT07/CH01130P._CP',             # 29
        'ED6_DT07/CH01140P._CP',             # 2A
        'ED6_DT07/CH01100P._CP',             # 2B
        'ED6_DT07/CH01180P._CP',             # 2C
        'ED6_DT07/CH01470P._CP',             # 2D
        'ED6_DT07/CH01770P._CP',             # 2E
        'ED6_DT07/CH01780P._CP',             # 2F
        'ED6_DT07/CH02363P._CP',             # 30
        'ED6_DT07/CH01373P._CP',             # 31
        'ED6_DT07/CH01213P._CP',             # 32
        'ED6_DT07/CH01593P._CP',             # 33
        'ED6_DT07/CH01043P._CP',             # 34
        'ED6_DT07/CH01033P._CP',             # 35
        'ED6_DT07/CH01363P._CP',             # 36
        'ED6_DT07/CH01690P._CP',             # 37
    )

    DeclNpc(
        X                   = 116010,
        Z                   = 0,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
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
        X                   = 6000,
        Z                   = 200,
        Y                   = 22200,
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
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 22900,
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
        X                   = 800,
        Z                   = 6000,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
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
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 87700,
        Z                   = 0,
        Y                   = 1000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 84400,
        Z                   = 0,
        Y                   = 1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 89260,
        Z                   = 0,
        Y                   = 1520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -2800,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -700,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -3100,
        Z                   = 0,
        Y                   = 5400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -2900,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -5500,
        Z                   = 0,
        Y                   = 35500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -3400,
        Z                   = 0,
        Y                   = 28800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -2000,
        Z                   = 0,
        Y                   = 700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 0,
        Y                   = 34700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -6000,
        Z                   = 0,
        Y                   = 700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 82700,
        Z                   = 0,
        Y                   = 33000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 90900,
        Z                   = 0,
        Y                   = 33400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 92300,
        Z                   = 0,
        Y                   = 33400,
        Direction           = 180,
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
        X                   = 85900,
        Z                   = 0,
        Y                   = 30400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 83500,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -3900,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -3900,
        Z                   = 0,
        Y                   = 34700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = -3000,
        Z                   = 0,
        Y                   = 34100,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 0,
        Y                   = 32600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 43480,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 2700,
        Z                   = 0,
        Y                   = 32500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 89800,
        Z                   = 0,
        Y                   = 29200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 88400,
        Z                   = 0,
        Y                   = 30800,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = -6100,
        Z                   = 0,
        Y                   = 34900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 3060,
        Z                   = 0,
        Y                   = 30300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 30900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = -100,
        Z                   = 0,
        Y                   = 32600,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 55,
        ChipIndex           = 0x37,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 300,
        Z                   = 0,
        Y                   = 29800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 47,
    )

    DeclNpc(
        X                   = 3090,
        Z                   = 0,
        Y                   = 32340,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
    )

    DeclNpc(
        X                   = -5900,
        Z                   = 0,
        Y                   = -300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 49,
    )

    DeclNpc(
        X                   = 41520,
        Z                   = 0,
        Y                   = 1170,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
    )

    DeclNpc(
        X                   = 30590,
        Z                   = 0,
        Y                   = 1500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 50,
    )

    DeclNpc(
        X                   = 38380,
        Z                   = 0,
        Y                   = 1600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 51,
    )

    DeclNpc(
        X                   = 26440,
        Z                   = 0,
        Y                   = -160,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 52,
    )

    DeclNpc(
        X                   = 39730,
        Z                   = 0,
        Y                   = 31370,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 53,
    )

    DeclNpc(
        X                   = 28810,
        Z                   = 0,
        Y                   = 31500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 54,
    )

    DeclNpc(
        X                   = 45020,
        Z                   = 0,
        Y                   = 30260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 55,
    )

    DeclNpc(
        X                   = 57380,
        Z                   = 0,
        Y                   = 30950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 56,
    )

    DeclNpc(
        X                   = 43840,
        Z                   = 0,
        Y                   = 35940,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 57,
    )

    DeclNpc(
        X                   = 24710,
        Z                   = 0,
        Y                   = 29820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 58,
    )

    DeclNpc(
        X                   = 85590,
        Z                   = 700,
        Y                   = 3050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835044,
        ChipIndex           = 0x24,
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
        Unknown_1C          = 75,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 76,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 77,
    )

    DeclEvent(
        X                   = 58990,
        Y                   = 0,
        Z                   = 31330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 78,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 31400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 79,
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
        TalkFunctionIndex   = 10,
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
        TalkFunctionIndex   = 61,
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
        TalkFunctionIndex   = 62,
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
        TalkFunctionIndex   = 63,
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
        TalkFunctionIndex   = 64,
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
        TalkFunctionIndex   = 65,
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
        TalkFunctionIndex   = 66,
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
        TalkFunctionIndex   = 67,
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
        TalkFunctionIndex   = 68,
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
        TalkFunctionIndex   = 69,
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
        TalkFunctionIndex   = 70,
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
        TalkFunctionIndex   = 71,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 93560,
        TriggerZ            = 0,
        TriggerY            = 33350,
        TriggerRange        = 800,
        ActorX              = 93560,
        ActorZ              = 1000,
        ActorY              = 33350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 72,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 87220,
        TriggerZ            = 0,
        TriggerY            = 34060,
        TriggerRange        = 800,
        ActorX              = 87220,
        ActorZ              = 1000,
        ActorY              = 34060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 73,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85030,
        TriggerZ            = 0,
        TriggerY            = 33920,
        TriggerRange        = 800,
        ActorX              = 85030,
        ActorZ              = 1000,
        ActorY              = 33920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 74,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_C06",          # 00, 0
        "Function_1_1308",         # 01, 1
        "Function_2_1340",         # 02, 2
        "Function_3_14EE",         # 03, 3
        "Function_4_153B",         # 04, 4
        "Function_5_1640",         # 05, 5
        "Function_6_1664",         # 06, 6
        "Function_7_1688",         # 07, 7
        "Function_8_16AC",         # 08, 8
        "Function_9_16D0",         # 09, 9
        "Function_10_1EE2",        # 0A, 10
        "Function_11_1EE7",        # 0B, 11
        "Function_12_289D",        # 0C, 12
        "Function_13_2BF6",        # 0D, 13
        "Function_14_2FB2",        # 0E, 14
        "Function_15_350A",        # 0F, 15
        "Function_16_393C",        # 10, 16
        "Function_17_3B39",        # 11, 17
        "Function_18_3B3E",        # 12, 18
        "Function_19_3FB7",        # 13, 19
        "Function_20_426F",        # 14, 20
        "Function_21_44FD",        # 15, 21
        "Function_22_4590",        # 16, 22
        "Function_23_4E89",        # 17, 23
        "Function_24_4ECD",        # 18, 24
        "Function_25_52DE",        # 19, 25
        "Function_26_53D9",        # 1A, 26
        "Function_27_554A",        # 1B, 27
        "Function_28_55AD",        # 1C, 28
        "Function_29_55FC",        # 1D, 29
        "Function_30_5751",        # 1E, 30
        "Function_31_5916",        # 1F, 31
        "Function_32_5A0C",        # 20, 32
        "Function_33_5A93",        # 21, 33
        "Function_34_5EF9",        # 22, 34
        "Function_35_62D6",        # 23, 35
        "Function_36_63F2",        # 24, 36
        "Function_37_6576",        # 25, 37
        "Function_38_68A2",        # 26, 38
        "Function_39_68E2",        # 27, 39
        "Function_40_6A88",        # 28, 40
        "Function_41_6ADB",        # 29, 41
        "Function_42_6C63",        # 2A, 42
        "Function_43_6CC5",        # 2B, 43
        "Function_44_6CEA",        # 2C, 44
        "Function_45_6D1E",        # 2D, 45
        "Function_46_6D95",        # 2E, 46
        "Function_47_6E56",        # 2F, 47
        "Function_48_6F5B",        # 30, 48
        "Function_49_70FE",        # 31, 49
        "Function_50_756B",        # 32, 50
        "Function_51_7676",        # 33, 51
        "Function_52_773E",        # 34, 52
        "Function_53_7859",        # 35, 53
        "Function_54_7909",        # 36, 54
        "Function_55_7994",        # 37, 55
        "Function_56_7A40",        # 38, 56
        "Function_57_7AF4",        # 39, 57
        "Function_58_7B91",        # 3A, 58
        "Function_59_7C37",        # 3B, 59
        "Function_60_800E",        # 3C, 60
        "Function_61_8FEA",        # 3D, 61
        "Function_62_9052",        # 3E, 62
        "Function_63_90C7",        # 3F, 63
        "Function_64_912D",        # 40, 64
        "Function_65_9190",        # 41, 65
        "Function_66_9200",        # 42, 66
        "Function_67_926B",        # 43, 67
        "Function_68_92BF",        # 44, 68
        "Function_69_931F",        # 45, 69
        "Function_70_93A1",        # 46, 70
        "Function_71_93F8",        # 47, 71
        "Function_72_9457",        # 48, 72
        "Function_73_94EF",        # 49, 73
        "Function_74_9580",        # 4A, 74
        "Function_75_ABDF",        # 4B, 75
        "Function_76_ABE3",        # 4C, 76
        "Function_77_ABE7",        # 4D, 77
        "Function_78_ABEB",        # 4E, 78
        "Function_79_ABEF",        # 4F, 79
    )


    def Function_0_C06(): pass

    label("Function_0_C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_C14")
    OP_A3(0x3FA)
    Event(0, 59)

    label("loc_C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_C7B")
    SetChrPos(0x10, 5320, 250, 2110, 270)
    SetChrPos(0x11, 5300, 250, 32080, 267)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x14, 400, 0, 0, 90)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x19, -2900, 0, 30000, 90)
    Jump("loc_12BA")

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_CBC")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1D, 0x80)
    Jump("loc_12BA")

    label("loc_CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_F31")
    SetChrPos(0x12, 95370, 250, 34220, 225)
    SetChrPos(0x8, 43470, 0, 5280, 225)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 42090, 0, 3930, 45)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, 42970, 0, 2640, 0)
    SetChrPos(0x17, -1590, 0, 34700, 0)
    SetChrPos(0x10, 2790, 0, 5460, 225)
    SetChrPos(0x15, 4500, 250, 2970, 270)
    SetChrPos(0x16, -990, 0, -1260, 0)
    SetChrChipByIndex(0x16, 47)
    OP_43(0x16, 0x0, 0x0, 0x3)
    SetChrPos(0x18, -4990, 0, 5010, 180)
    SetChrChipByIndex(0x18, 46)
    OP_43(0x18, 0x0, 0x0, 0x4)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1E, 51)
    SetChrPos(0x1E, -6000, 100, 700, 90)
    OP_44(0x1E, 0xFF)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x10)
    ClearChrFlags(0x32, 0x80)
    SetChrChipByIndex(0x32, 52)
    SetChrPos(0x32, -5960, 0, 3010, 90)
    OP_44(0x32, 0xFF)
    SetChrFlags(0x32, 0x4)
    SetChrFlags(0x32, 0x10)
    ClearChrFlags(0x31, 0x80)
    SetChrPos(0x31, -4000, 0, 4100, 270)
    SetChrChipByIndex(0x31, 53)
    OP_44(0x31, 0xFF)
    SetChrFlags(0x31, 0x4)
    SetChrFlags(0x31, 0x10)
    SetChrPos(0x14, -70, 0, 3050, 270)
    SetChrChipByIndex(0x14, 54)
    OP_44(0x14, 0xFF)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x11, -6910, 0, 33220, 90)
    SetChrPos(0x19, 1300, 0, 28510, 90)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 89110, 0, 29220, 90)
    SetChrFlags(0x21, 0x10)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 89160, 0, 34290, 0)
    ClearChrFlags(0x33, 0x80)
    SetChrPos(0x33, 85890, 0, 32890, 315)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x2C, 90550, 0, 29250, 270)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x10)
    ClearChrFlags(0x2A, 0x80)
    SetChrPos(0x2A, 31660, 0, 100, 0)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2B, 0x10)
    SetChrPos(0x2B, 32619, 0, 320, 270)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    Jump("loc_12BA")

    label("loc_F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1143")
    SetChrPos(0x11, -6910, 0, 33220, 90)
    SetChrPos(0x12, 95370, 250, 34220, 225)
    SetChrPos(0x8, 42940, 0, 1070, 270)
    SetChrFlags(0x8, 0x10)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x10)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrPos(0x10, 2790, 0, 5460, 225)
    SetChrPos(0x15, 4500, 250, 2970, 270)
    SetChrPos(0x16, -990, 0, -1260, 0)
    SetChrChipByIndex(0x16, 47)
    OP_43(0x16, 0x0, 0x0, 0x3)
    SetChrPos(0x18, -4990, 0, 5010, 180)
    SetChrChipByIndex(0x18, 46)
    OP_43(0x18, 0x0, 0x0, 0x4)
    ClearChrFlags(0x24, 0x80)
    SetChrChipByIndex(0x24, 48)
    SetChrPos(0x24, -4019, 100, 3080, 270)
    OP_44(0x24, 0xFF)
    SetChrFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x10)
    ClearChrFlags(0x33, 0x80)
    SetChrPos(0x33, -5040, 100, 2050, 0)
    ClearChrFlags(0x2C, 0x80)
    SetChrChipByIndex(0x2C, 50)
    SetChrPos(0x2C, -130, 0, 4000, 270)
    OP_44(0x2C, 0xFF)
    SetChrFlags(0x2C, 0x4)
    SetChrFlags(0x2C, 0x10)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -1960, 0, -300, 90)
    SetChrChipByIndex(0x1C, 49)
    OP_44(0x1C, 0xFF)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x10)
    SetChrPos(0x19, 1300, 0, 28510, 90)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x10)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x10)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x10)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8B, 2)), scpexpr(EXPR_END)), "loc_1140")
    SetChrPos(0x25, 88600, 0, 34670, 0)
    SetChrPos(0x26, 89570, 0, 34410, 270)
    SetChrPos(0x29, -1680, 0, 34680, 0)
    ClearChrFlags(0x29, 0x80)

    label("loc_1140")

    Jump("loc_12BA")

    label("loc_1143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1199")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x15, -5200, 0, 2050, 0)
    SetChrPos(0x16, 4500, 250, 4019, 270)
    SetChrPos(0x19, 790, 0, 34680, 0)
    Jump("loc_12BA")

    label("loc_1199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_11C8")
    SetChrPos(0x11, 5300, 250, 32080, 267)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    Jump("loc_12BA")

    label("loc_11C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_11FF")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_12BA")

    label("loc_11FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_123B")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_12BA")

    label("loc_123B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_127C")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_12BA")

    label("loc_127C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_12BA")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)

    label("loc_12BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12D4")
    OP_A2(0x443)

    label("loc_12D4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (110, "loc_12E0"),
        (SWITCH_DEFAULT, "loc_12F6"),
    )


    label("loc_12E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8B, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F3")
    OP_A2(0x432)
    Event(0, 60)

    label("loc_12F3")

    Jump("loc_12F6")

    label("loc_12F6")

    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_C06 end

    def Function_1_1308(): pass

    label("Function_1_1308")

    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_131B")
    OP_65(0x1, 0x1)

    label("loc_131B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_132F")
    OP_64(0x1, 0x1)
    SetChrFlags(0x3E, 0x80)

    label("loc_132F")

    OP_75(0x6, 0x0, 0x0)
    OP_74(0x6, 0x0, 0x0)
    Return()

    # Function_1_1308 end

    def Function_2_1340(): pass

    label("Function_2_1340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_134A")
    Jump("loc_1371")

    label("loc_134A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_135F")
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1371")

    label("loc_135F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1371")
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1371")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1396")
    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_14D8")

    label("loc_1396")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AF")
    OP_99(0xFE, 0x1, 0x7, 0x514)
    Jump("loc_14D8")

    label("loc_13AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C8")
    OP_99(0xFE, 0x2, 0x7, 0x4E2)
    Jump("loc_14D8")

    label("loc_13C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E1")
    OP_99(0xFE, 0x3, 0x7, 0x4B0)
    Jump("loc_14D8")

    label("loc_13E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13FA")
    OP_99(0xFE, 0x4, 0x7, 0x47E)
    Jump("loc_14D8")

    label("loc_13FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1413")
    OP_99(0xFE, 0x5, 0x7, 0x44C)
    Jump("loc_14D8")

    label("loc_1413")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142C")
    OP_99(0xFE, 0x6, 0x7, 0x41A)
    Jump("loc_14D8")

    label("loc_142C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1445")
    OP_99(0xFE, 0x0, 0x7, 0x54B)
    Jump("loc_14D8")

    label("loc_1445")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145E")
    OP_99(0xFE, 0x1, 0x7, 0x519)
    Jump("loc_14D8")

    label("loc_145E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1477")
    OP_99(0xFE, 0x2, 0x7, 0x4E7)
    Jump("loc_14D8")

    label("loc_1477")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1490")
    OP_99(0xFE, 0x3, 0x7, 0x4B5)
    Jump("loc_14D8")

    label("loc_1490")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A9")
    OP_99(0xFE, 0x4, 0x7, 0x483)
    Jump("loc_14D8")

    label("loc_14A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C2")
    OP_99(0xFE, 0x5, 0x7, 0x451)
    Jump("loc_14D8")

    label("loc_14C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D8")
    OP_99(0xFE, 0x6, 0x7, 0x41F)

    label("loc_14D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14ED")
    OP_99(0xFE, 0x0, 0x7, 0x4B0)
    Jump("loc_14D8")

    label("loc_14ED")

    Return()

    # Function_2_1340 end

    def Function_3_14EE(): pass

    label("Function_3_14EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_153A")
    OP_8E(0xFE, 0xFFFFEC5A, 0x0, 0xFFFFFB14, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFFC22, 0x0, 0xFFFFFB14, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_3_14EE")

    label("loc_153A")

    Return()

    # Function_3_14EE end

    def Function_4_153B(): pass

    label("Function_4_153B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_163F")
    OP_8E(0xFE, 0xFFFFFC0E, 0x0, 0x1356, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x5D2, 0x0, 0x1356, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D2, 0x0, 0xD98, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7C6, 0x0, 0xC12, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9EC, 0x0, 0xB86, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x7C6, 0x0, 0xC12, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D2, 0x0, 0xD98, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D2, 0x0, 0x1356, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFC0E, 0x0, 0x1356, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFEC82, 0x0, 0x1392, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(3000)
    Jump("Function_4_153B")

    label("loc_163F")

    Return()

    # Function_4_153B end

    def Function_5_1640(): pass

    label("Function_5_1640")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1663")
    OP_8D(0xFE, 24420, 1500, 29350, -1300, 1500)
    Jump("Function_5_1640")

    label("loc_1663")

    Return()

    # Function_5_1640 end

    def Function_6_1664(): pass

    label("Function_6_1664")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1687")
    OP_8D(0xFE, 38740, 33660, 43330, 28250, 1500)
    Jump("Function_6_1664")

    label("loc_1687")

    Return()

    # Function_6_1664 end

    def Function_7_1688(): pass

    label("Function_7_1688")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16AB")
    OP_8D(0xFE, 42670, 31640, 49420, 28690, 2000)
    Jump("Function_7_1688")

    label("loc_16AB")

    Return()

    # Function_7_1688 end

    def Function_8_16AC(): pass

    label("Function_8_16AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16CF")
    OP_8D(0xFE, 23100, 31490, 27030, 28520, 3000)
    Jump("Function_8_16AC")

    label("loc_16CF")

    Return()

    # Function_8_16AC end

    def Function_9_16D0(): pass

    label("Function_9_16D0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1848")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AF")
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
    Jump("loc_1845")

    label("loc_17AF")


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

    label("loc_1845")

    Jump("loc_1EDE")

    label("loc_1848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_195E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FD")
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
    Jump("loc_195B")

    label("loc_18FD")


    ChrTalk(
        0xFE,
        (
            "#780F我听说特蕾莎院长的事情了。\x02\x03",
            "怎么说呢……\x01",
            "实在是很过分的事啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_195B")

    Jump("loc_1EDE")

    label("loc_195E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_1AFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A64")
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
    Jump("loc_1AF7")

    label("loc_1A64")


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

    label("loc_1AF7")

    Jump("loc_1EDE")

    label("loc_1AFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_1C14")
    ClearChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAF")
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
    Jump("loc_1C11")

    label("loc_1BAF")


    ChrTalk(
        0xFE,
        (
            "#780F大家都很期待舞台剧。\x01",
            "请务必让学园祭圆满成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C11")

    Jump("loc_1EDE")

    label("loc_1C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1DE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2A")
    OP_A2(0x457)
    OP_4A(0x34, 255)

    ChrTalk(
        0x8,
        (
            "#781F戴尔蒙市长，\x01",
            "自从去年的王国会议之后我们也好久不见了。\x02\x03",
            "这段时间，你身体怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#661F就像你看到的，结实着呢。\x01",
            "科林兹校长也很精神嘛。\x02\x03",
            "今天我打算好好放松一下。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x34, 0x10)
    OP_4B(0x34, 255)
    Jump("loc_1DE1")

    label("loc_1D2A")


    ChrTalk(
        0x8,
        (
            "#781F我还要找时间和市长先生谈谈\x01",
            "关于学院运营的事情呢。\x01",
            "　\x02\x03",
            "虽说是王立的教育机构，\x01",
            "但也要重视地方上的建议。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE1")

    Jump("loc_1EDE")

    label("loc_1DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1EDE")

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

    label("loc_1EDE")

    TalkEnd(0x8)
    Return()

    # Function_9_16D0 end

    def Function_10_1EE2(): pass

    label("Function_10_1EE2")

    Call(0, 11)
    Return()

    # Function_10_1EE2 end

    def Function_11_1EE7(): pass

    label("Function_11_1EE7")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F6B")
    OP_A2(0x2)

    ChrTalk(
        0xF,
        (
            "啊，怎么了？\x01",
            "你们要找人吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "现在正好是\x01",
            "上课结束的时间。\x01",
            "你们可以去和同学们见面。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F8A")

    label("loc_1F6B")


    ChrTalk(
        0xF,
        (
            "啊，怎么了？\x01",
            "你们要找人吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F8A")

    Jump("loc_2899")

    label("loc_1F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_201D")

    ChrTalk(
        0xF,
        "呵呵，学园祭很成功呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "学生们正在\x01",
            "礼堂那里庆祝胜利呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2899")

    label("loc_201D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_20DA")

    ChrTalk(
        0xF,
        (
            "说起来\x01",
            "真是出乎意料的盛况啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "很多人还带了孩子来，\x01",
            "要是有小孩迷路就糟了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2899")

    label("loc_20DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2273")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E4")
    OP_A2(0x2)

    ChrTalk(
        0xF,
        (
            "各种活动都在\x01",
            "校园和主楼里进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "下午礼堂那边\x01",
            "预定要演出舞台剧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "食堂作为休息场所开放，\x01",
            "你们可以好好利用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2270")

    label("loc_21E4")


    ChrTalk(
        0xF,
        (
            "各种活动都在\x01",
            "校园和主楼里进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "下午礼堂那边\x01",
            "预定要演出舞台剧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2270")

    Jump("loc_2899")

    label("loc_2273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230F")
    OP_A2(0x2)

    ChrTalk(
        0xF,
        (
            "准备完成了吗？\x01",
            "明天就要正式表演了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "到了明天\x01",
            "就会有许多客人来参观了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234E")

    label("loc_230F")


    ChrTalk(
        0xF,
        (
            "准备完成了吗？\x01",
            "明天就要正式表演了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_234E")

    Jump("loc_2899")

    label("loc_2351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_244E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_240B")
    OP_A2(0x2)

    ChrTalk(
        0xF,
        (
            "呵呵，一到下课时间，\x01",
            "校园里就会变得热闹起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "学园祭就要开始了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "希望同学们\x01",
            "都能加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_244B")

    label("loc_240B")


    ChrTalk(
        0xF,
        (
            "呵呵，一到下课时间，\x01",
            "校园里就会变得热闹起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_244B")

    Jump("loc_2899")

    label("loc_244E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_25C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255C")
    OP_A2(0x2)

    ChrTalk(
        0xF,
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
        0xF,
        "呵呵，回来就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "要找校长的话，\x01",
            "他就在办公室里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
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
    Jump("loc_25C5")

    label("loc_255C")


    ChrTalk(
        0xF,
        (
            "要找校长的话，\x01",
            "他就在办公室里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "他也很担心\x01",
            "科洛丝你呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C5")

    Jump("loc_2899")

    label("loc_25C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_26C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A0")
    OP_A2(0x2)

    ChrTalk(
        0xF,
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
        0xF,
        (
            "是吗。\x01",
            "外出时请务必要小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C2")

    label("loc_26A0")


    ChrTalk(
        0xF,
        (
            "科洛丝，\x01",
            "外出时请务必要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26C2")

    Jump("loc_2899")

    label("loc_26C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_2744")

    ChrTalk(
        0xF,
        "啊，是想参观吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "很抱歉，\x01",
            "现在学生们正在上课，\x01",
            "不能带您参观。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2899")

    label("loc_2744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2848")
    OP_A2(0x2)

    ChrTalk(
        0xF,
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
        0xF,
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
    Jump("loc_2899")

    label("loc_2848")


    ChrTalk(
        0xF,
        (
            "科洛丝，\x01",
            "难得的假日，\x01",
            "就好好地放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2899")

    TalkEnd(0xF)
    Return()

    # Function_11_1EE7 end

    def Function_12_289D(): pass

    label("Function_12_289D")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_28EE")

    ChrTalk(
        0xFE,
        (
            "课虽然上完了，\x01",
            "但还有学生们的问题要回答。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF2")

    label("loc_28EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2964")

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
    Jump("loc_2BF2")

    label("loc_2964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_29DA")

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
    Jump("loc_2BF2")

    label("loc_29DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2B43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB1")
    OP_A2(0x3)

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
    Jump("loc_2B40")

    label("loc_2AB1")


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

    label("loc_2B40")

    Jump("loc_2BF2")

    label("loc_2B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2BF2")

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

    label("loc_2BF2")

    TalkEnd(0x10)
    Return()

    # Function_12_289D end

    def Function_13_2BF6(): pass

    label("Function_13_2BF6")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C59")
    OP_A2(0x4)

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
    ClearChrFlags(0x11, 0x10)
    Jump("loc_2C8B")

    label("loc_2C59")


    ChrTalk(
        0xFE,
        (
            "呼，这里的学生\x01",
            "都很热心于学习呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C8B")

    Jump("loc_2FAE")

    label("loc_2C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2D28")

    ChrTalk(
        0xFE,
        (
            "呼，真没劲……\x01",
            "还没到演出的时间吗？\x02",
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
    Jump("loc_2FAE")

    label("loc_2D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2E10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DDE")
    OP_A2(0x4)

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
    Jump("loc_2E0D")

    label("loc_2DDE")


    ChrTalk(
        0xFE,
        (
            "决不能输给\x01",
            "米丽亚的班级……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E0D")

    Jump("loc_2FAE")

    label("loc_2E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2FAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F66")
    OP_A2(0x4)

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
    Jump("loc_2FAE")

    label("loc_2F66")


    ChrTalk(
        0xFE,
        (
            "我还是趁现在\x01",
            "批改一下考试卷子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FAE")

    TalkEnd(0x11)
    Return()

    # Function_13_2BF6 end

    def Function_14_2FB2(): pass

    label("Function_14_2FB2")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3047")

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
    Jump("loc_3506")

    label("loc_3047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_31B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3136")
    OP_A2(0x5)

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

    ChrTalk(
        0xFE,
        (
            "那个班的老师不行，\x01",
            "学生们却都很优秀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B0")

    label("loc_3136")


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

    label("loc_31B0")

    Jump("loc_3506")

    label("loc_31B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3212")

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
    Jump("loc_3506")

    label("loc_3212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_331A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C7")
    OP_A2(0x5)

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
    Jump("loc_3317")

    label("loc_32C7")


    ChrTalk(
        0xFE,
        (
            "嗯，明天就能好好看到\x01",
            "同学们努力的成果了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3317")

    Jump("loc_3506")

    label("loc_331A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_3506")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_343C")
    OP_A2(0x5)

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
    Jump("loc_3506")

    label("loc_343C")


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

    label("loc_3506")

    TalkEnd(0x12)
    Return()

    # Function_14_2FB2 end

    def Function_15_350A(): pass

    label("Function_15_350A")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_358B")

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
    Jump("loc_3938")

    label("loc_358B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_36F8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_3632")

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
    Jump("loc_36F5")

    label("loc_3632")


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

    label("loc_36F5")

    Jump("loc_3938")

    label("loc_36F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_389B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37F0")
    OP_A2(0x6)

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
    Jump("loc_3898")

    label("loc_37F0")


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

    label("loc_3898")

    Jump("loc_3938")

    label("loc_389B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_390E")
    OP_A2(0x6)

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
    Jump("loc_3938")

    label("loc_390E")


    ChrTalk(
        0xFE,
        (
            "要有外出许可证\x01",
            "才能出去哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3938")

    TalkEnd(0x13)
    Return()

    # Function_15_350A end

    def Function_16_393C(): pass

    label("Function_16_393C")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_39FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C1")
    OP_A2(0x7)

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
    Jump("loc_39FB")

    label("loc_39C1")


    ChrTalk(
        0xFE,
        (
            "下午的课\x01",
            "一定会睡着的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FB")

    Jump("loc_3B35")

    label("loc_39FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AB2")
    OP_A2(0x7)

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
        (
            "嗯，\x01",
            "感觉真是很充实呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B35")

    label("loc_3AB2")


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
            "都顾不上照顾\x01",
            "班里的茶座了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B35")

    TalkEnd(0x14)
    Return()

    # Function_16_393C end

    def Function_17_3B39(): pass

    label("Function_17_3B39")

    Call(0, 18)
    Return()

    # Function_17_3B39 end

    def Function_18_3B3E(): pass

    label("Function_18_3B3E")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3B4B")
    Jump("loc_3BC3")

    label("loc_3B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3BC3")
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

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BAF")
    OP_0D()
    OP_A9(0x31)
    OP_56(0x0)
    TalkEnd(0x15)
    Return()

    label("loc_3BAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BC0")
    TalkEnd(0x15)
    Return()

    label("loc_3BC0")

    Jump("loc_3BC3")

    label("loc_3BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3C23")

    ChrTalk(
        0x15,
        "那么，该去社团活动了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "今天要把\x01",
            "画到一半的绘画完成！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB3")

    label("loc_3C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3CB9")

    ChrTalk(
        0x15,
        (
            "嗯，\x01",
            "茶座还是要办成这样才对啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "辛苦也值得了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FB3")

    label("loc_3CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3D65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CFE")
    OP_A2(0x8)

    ChrTalk(
        0x15,
        (
            "……那边桌子的客人\x01",
            "难道是真正的女佣？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D62")

    label("loc_3CFE")


    ChrTalk(
        0x15,
        (
            "因为通宵工作，\x01",
            "现在好困啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D62")

    Jump("loc_3FB3")

    label("loc_3D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_3E56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DFC")
    OP_A2(0x8)

    ChrTalk(
        0x15,
        (
            "唔哇哇！\x01",
            "怎么回事！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "呆在这里\x01",
            "会来不及准备的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E53")

    label("loc_3DFC")


    ChrTalk(
        0x15,
        (
            "……难道说\x01",
            "这样下去要通宵赶工了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "呼，\x01",
            "做衣服花了太多时间了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E53")

    Jump("loc_3FB3")

    label("loc_3E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_3FB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F7C")
    OP_A2(0x8)

    ChrTalk(
        0x15,
        "啦啦啦～～⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "我正在做\x01",
            "摆摊时穿的衣服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "唔～就是要在这种时候集中精力！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "因为做这种东西\x01",
            "是我最喜欢干的事情了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB3")

    label("loc_3F7C")


    ChrTalk(
        0x15,
        "接下来还要做房间的装饰。\x02",
    )

    CloseMessageWindow()

    label("loc_3FB3")

    TalkEnd(0x15)
    Return()

    # Function_18_3B3E end

    def Function_19_3FB7(): pass

    label("Function_19_3FB7")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3FFC")

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
    Jump("loc_426B")

    label("loc_3FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4057")

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
    Jump("loc_426B")

    label("loc_4057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4131")

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
    Jump("loc_426B")

    label("loc_4131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_426B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F5")
    OP_A2(0x9)

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
    Jump("loc_426B")

    label("loc_41F5")


    ChrTalk(
        0xFE,
        (
            "就算是演出用的女佣服装\x01",
            "也是他自己做的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426B")

    TalkEnd(0x16)
    Return()

    # Function_19_3FB7 end

    def Function_20_426F(): pass

    label("Function_20_426F")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_439E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4350")
    OP_A2(0xA)

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
    Jump("loc_439B")

    label("loc_4350")


    ChrTalk(
        0xFE,
        (
            "米丽亚老师\x01",
            "才刚上完课\x01",
            "就马上回办公室了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_439B")

    Jump("loc_44F9")

    label("loc_439E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_44F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4498")
    OP_A2(0xA)

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
    Jump("loc_44F9")

    label("loc_4498")


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

    label("loc_44F9")

    TalkEnd(0x17)
    Return()

    # Function_20_426F end

    def Function_21_44FD(): pass

    label("Function_21_44FD")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_4531")

    ChrTalk(
        0xFE,
        (
            "欢迎光临。\x01",
            "这里是我们的茶座『芳塔娜』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458C")

    label("loc_4531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_458C")

    ChrTalk(
        0xFE,
        (
            "穿成这个样子\x01",
            "虽然有点不好意思，\x01",
            "但为了学园祭，忍了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_458C")

    TalkEnd(0x18)
    Return()

    # Function_21_44FD end

    def Function_22_4590(): pass

    label("Function_22_4590")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_45CC")

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "今天也是很有意义的一课啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E85")

    label("loc_45CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_4787")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46AA")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "有很多前辈\x01",
            "和市民们前来参观。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然办娱乐活动很有意思，\x01",
            "不过公布我们的研究成果也是很重要的。\x02",
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
    Jump("loc_4784")

    label("loc_46AA")


    ChrTalk(
        0xFE,
        (
            "有很多前辈\x01",
            "和市民们前来参观。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然办娱乐活动很有意思，\x01",
            "不过公布我们的研究成果也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4784")

    Jump("loc_4E85")

    label("loc_4787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4BB5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_4922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48EE")
    OP_A2(0xC)

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
            "如果有兴趣的话\x01",
            "就请看一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491F")

    label("loc_48EE")


    ChrTalk(
        0xFE,
        (
            "如果有兴趣的话\x01",
            "就请看一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_491F")

    Jump("loc_4BB2")

    label("loc_4922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A90")
    OP_A2(0xC)

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
        (
            "如果有兴趣的话\x01",
            "就请看一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BB2")

    label("loc_4A90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_4B81")

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
    Jump("loc_4BB2")

    label("loc_4B81")


    ChrTalk(
        0xFE,
        "如果有兴趣的话就请看一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_4BB2")

    Jump("loc_4E85")

    label("loc_4BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4CD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C87")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "唔，还是需要一些\x01",
            "辅助研究的资料啊。\x02",
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
    Jump("loc_4CD6")

    label("loc_4C87")


    ChrTalk(
        0xFE,
        (
            "唔，还是需要一些\x01",
            "辅助研究的资料啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD6")

    Jump("loc_4E85")

    label("loc_4CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_4E85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E63")
    OP_A2(0xC)

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
    Jump("loc_4E85")

    label("loc_4E63")


    ChrTalk(
        0xFE,
        "科洛丝，我们互相加油吧。\x02",
    )

    CloseMessageWindow()

    label("loc_4E85")

    TalkEnd(0x19)
    Return()

    # Function_22_4590 end

    def Function_23_4E89(): pass

    label("Function_23_4E89")

    TalkBegin(0x1A)

    ChrTalk(
        0xFE,
        (
            "今年怎么没有\x01",
            "鬼怪屋呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这明明是惯例的……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1A)
    Return()

    # Function_23_4E89 end

    def Function_24_4ECD(): pass

    label("Function_24_4ECD")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_4F7A")

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
    Jump("loc_52DA")

    label("loc_4F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_50B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5032")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "我太过忙于这里的活动，\x01",
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
    Jump("loc_50AD")

    label("loc_5032")


    ChrTalk(
        0xFE,
        (
            "来这里参观的人\x01",
            "真是多啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还有热心人向我们\x01",
            "提出不少尖锐的问题呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50AD")

    Jump("loc_52DA")

    label("loc_50B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_51DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5165")
    OP_A2(0xE)

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
        (
            "我认为这是\x01",
            "很有意义的一件事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51D7")

    label("loc_5165")


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

    label("loc_51D7")

    Jump("loc_52DA")

    label("loc_51DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_52DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_526E")
    OP_A2(0xE)

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
    Jump("loc_52DA")

    label("loc_526E")


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

    label("loc_52DA")

    TalkEnd(0x1B)
    Return()

    # Function_24_4ECD end

    def Function_25_52DE(): pass

    label("Function_25_52DE")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5352")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "下午我就要\x01",
            "为社团去看店了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此我只有\x01",
            "趁现在可以玩一会。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53D5")

    label("loc_5352")


    ChrTalk(
        0xFE,
        (
            "上午是同社团的\x01",
            "罗迪在看店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为太热闹了，\x01",
            "所以我想很快就能知道了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D5")

    TalkEnd(0x1C)
    Return()

    # Function_25_52DE end

    def Function_26_53D9(): pass

    label("Function_26_53D9")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_5442")

    ChrTalk(
        0xFE,
        (
            "……碧欧拉老师\x01",
            "从刚才开始就在打哈欠。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难得她那么漂亮，\x01",
            "可以吸引客人来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5546")

    label("loc_5442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5546")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54F3")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "今天我们给客人当导游。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "根据大家的需要，\x01",
            "我们会对社会系的研究成果\x01",
            "进行浅显易懂的说明。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5546")

    label("loc_54F3")


    ChrTalk(
        0xFE,
        (
            "根据大家的需要，\x01",
            "我们会对社会系的研究成果\x01",
            "进行浅显易懂的说明。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5546")

    TalkEnd(0x1D)
    Return()

    # Function_26_53D9 end

    def Function_27_554A(): pass

    label("Function_27_554A")

    TalkBegin(0x1E)

    ChrTalk(
        0xFE,
        "啊，是前辈们呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿，我呀，\x01",
            "上午负责看店，\x01",
            "下午就可以玩了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1E)
    Return()

    # Function_27_554A end

    def Function_28_55AD(): pass

    label("Function_28_55AD")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_55F8")

    ChrTalk(
        0xFE,
        "呵呵，我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真让人欣慰呀，\x01",
            "连基诺奇奥也做得很好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55F8")

    TalkEnd(0x1F)
    Return()

    # Function_28_55AD end

    def Function_29_55FC(): pass

    label("Function_29_55FC")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_56D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5698")
    OP_A2(0x13)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "好像比我想象的更加有趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不知道提出这个方案的人\x01",
            "是怎么想出来的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D6")

    label("loc_5698")


    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔……好困呀……\x02",
    )

    CloseMessageWindow()

    label("loc_56D6")

    Jump("loc_574D")

    label("loc_56D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_574D")

    ChrTalk(
        0xFE,
        (
            "哎……\x01",
            "为什么妈妈和妹妹会来呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不是说因为工作\x01",
            "不能来了吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_574D")

    TalkEnd(0x20)
    Return()

    # Function_29_55FC end

    def Function_30_5751(): pass

    label("Function_30_5751")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_57AF")

    ChrTalk(
        0xFE,
        (
            "姐姐！？\x01",
            "家里的店没人管不要紧吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5912")

    label("loc_57AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5912")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58A3")
    OP_A2(0x14)

    ChrTalk(
        0xFE,
        (
            "结果昨天我们\x01",
            "还是没能完成展示的准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是今天早上来看，\x01",
            "已经全部完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天回去的时候\x01",
            "的确是只做到一半啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5912")

    label("loc_58A3")


    ChrTalk(
        0xFE,
        (
            "昨天回去的时候\x01",
            "的确还没有完成啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我问过大家，\x01",
            "但每个人都说不知道。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5912")

    TalkEnd(0x21)
    Return()

    # Function_30_5751 end

    def Function_31_5916(): pass

    label("Function_31_5916")

    TalkBegin(0x22)

    ChrTalk(
        0xFE,
        (
            "我和蕾娜不仅\x01",
            "属于同一个班级和社团，\x01",
            "就连宿舍也是在同一个房间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "这可真是受不了呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只有现在\x01",
            "才能享受点自由。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x22)
    Return()

    # Function_31_5916 end

    def Function_32_5A0C(): pass

    label("Function_32_5A0C")

    TalkBegin(0x23)

    ChrTalk(
        0xFE,
        (
            "差不多把展示的\x01",
            "所有内容都看完了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过把看店的芙拉瑟给冷落了……\x01",
            "不，要好好地鼓励她才行。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x23)
    Return()

    # Function_32_5A0C end

    def Function_33_5A93(): pass

    label("Function_33_5A93")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_5B05")

    ChrTalk(
        0xFE,
        (
            "#610F呵呵，\x01",
            "这个真是很有趣呢。\x02\x03",
            "演出是在下午吧，\x01",
            "我很期待哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EF5")

    label("loc_5B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5EF5")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B2E")
    SetChrSubChip(0xFE, 2)
    Jump("loc_5B5F")

    label("loc_5B2E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B44")
    SetChrSubChip(0xFE, 1)
    Jump("loc_5B5F")

    label("loc_5B44")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B5A")
    SetChrSubChip(0xFE, 0)
    Jump("loc_5B5F")

    label("loc_5B5A")

    SetChrSubChip(0xFE, 2)

    label("loc_5B5F")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E65")
    OP_A2(0x453)

    ChrTalk(
        0x101,
        "#004F啊，梅贝尔市长！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#613F啊，\x01",
            "这不是艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F市长您为什么会在这里呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#611F呵呵，\x01",
            "其实我是这个学院的毕业生。\x02\x03",
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
            "　\x02\x03",
            "难道是为了协会的工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嘿嘿，其实呢……\x02",
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
            "#613F哦，是协助演出啊。\x02\x03",
            "#611F我也认为演出是很考功夫的。\x01",
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
            "#017F（唔，真不想让\x01",
            "　认识的人看到啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EF0")

    label("loc_5E65")


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

    label("loc_5EF0")

    SetChrSubChip(0xFE, 0)

    label("loc_5EF5")

    TalkEnd(0x24)
    Return()

    # Function_33_5A93 end

    def Function_34_5EF9(): pass

    label("Function_34_5EF9")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_6080")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FF1")
    OP_A2(0x18)

    ChrTalk(
        0xFE,
        (
            "#220F哦，下午要演出啊。\x02\x03",
            "虽然这里及不上\x01",
            "在王都举办的华丽舞台剧……\x02\x03",
            "毕竟应酬还是应酬啊，\x01",
            "哈哈，身为未来国王的我就凑合看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_607D")

    label("loc_5FF1")


    ChrTalk(
        0xFE,
        (
            "#220F哦，下午要演出啊。\x02\x03",
            "毕竟应酬还是应酬啊。\x01",
            "哈哈，身为未来国王的我就凑合看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_607D")

    Jump("loc_62D2")

    label("loc_6080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_62D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61F3")
    OP_A2(0x454)

    ChrTalk(
        0xFE,
        (
            "#220F这里可是王家出钱办的学院。\x01",
            "　\x02\x03",
            "我作为女王的外甥，\x01",
            "一定要好好视察。\x02\x03",
            "#221F呵呵呵，想必这里的学生\x01",
            "一定感到万分的光荣吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F（怎么把这个大叔也邀请过来了……）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（嗯，\x01",
            "　好像不邀请也不行啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62D2")

    label("loc_61F3")


    ChrTalk(
        0x25,
        (
            "#220F这里可是王家出钱办的学院。\x01",
            "　\x02\x03",
            "我作为女王的外甥，\x01",
            "一定要好好视察。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62D2")

    TalkEnd(0x25)
    Return()

    # Function_34_5EF9 end

    def Function_35_62D6(): pass

    label("Function_35_62D6")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_635C")

    ChrTalk(
        0xFE,
        (
            "#720F这里真不愧是杰尼丝王立学院啊。\x01",
            "　\x02\x03",
            "就连学园祭也办得像模像样的……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63EE")

    label("loc_635C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_63EE")
    OP_62(0x26, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "#722F大、大人，\x01",
            "请恕冒昧直言……\x02\x03",
            "在公众面前，\x01",
            "请务必注意一下您的言词。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63EE")

    TalkEnd(0x26)
    Return()

    # Function_35_62D6 end

    def Function_36_63F2(): pass

    label("Function_36_63F2")

    TalkBegin(0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64D7")
    OP_A2(0x1A)

    ChrTalk(
        0xFE,
        (
            "#140F原来下午有演出啊。\x02\x03",
            "#142F而且还是古典名作『白花恋诗』……\x01",
            "　\x02\x03",
            "不过话说回来，这舞台剧对\x01",
            "学生们来说是不是有点太难了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6572")

    label("loc_64D7")


    ChrTalk(
        0xFE,
        (
            "#142F演出剧目是『白花恋诗』啊。\x02\x03",
            "不过话说回来，这舞台剧对\x01",
            "学生们来说是不是有点太难了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6572")

    TalkEnd(0x27)
    Return()

    # Function_36_63F2 end

    def Function_37_6576(): pass

    label("Function_37_6576")

    TalkBegin(0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_683F")
    OP_A2(0x456)

    ChrTalk(
        0x101,
        "#000F啊，是卡露娜姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F您好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#830F呀，是你们啊……\x01",
            "我听嘉恩说了哦。\x02\x03",
            "你们是来给\x01",
            "学园祭帮忙的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嘿嘿，差不多这样啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F卡露娜前辈\x01",
            "是来做警卫之类的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#830F没错。\x02\x03",
            "这里的毕业生大多都是\x01",
            "在利贝尔各界活跃的著名人士。\x02\x03",
            "每年的学园祭，\x01",
            "他们都会作为客人被邀请到在这里来聚会。\x02\x03",
            "担任警卫的我\x01",
            "必须要十分仔细才行。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_END)), "loc_6783")

    ChrTalk(
        0x102,
        (
            "#010F说起来，\x01",
            "梅贝尔市长也是这里的毕业生呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67D4")

    label("loc_6783")


    ChrTalk(
        0x101,
        (
            "#000F哎……说起来，\x01",
            "那个谁好像也是这里的毕业生……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67D4")


    ChrTalk(
        0xFE,
        (
            "嗯，警备方面就交给我，\x01",
            "你们就尽心帮助学院其他工作吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x456)
    Jump("loc_689E")

    label("loc_683F")


    ChrTalk(
        0xFE,
        (
            "警备工作就交给我，\x01",
            "你们就尽心帮助学院其他工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_689E")

    TalkEnd(0x28)
    Return()

    # Function_37_6576 end

    def Function_38_68A2(): pass

    label("Function_38_68A2")

    TalkBegin(0x29)

    ChrTalk(
        0xFE,
        (
            "#130F哦哦……\x02\x03",
            "原来如此，\x01",
            "学生们调查得很详细啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x29)
    Return()

    # Function_38_68A2 end

    def Function_39_68E2(): pass

    label("Function_39_68E2")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_691F")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "在这里稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A84")

    label("loc_691F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6A84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69F4")
    OP_A2(0x1C)

    ChrTalk(
        0xFE,
        (
            "今天特地请假\x01",
            "来看我儿子的英姿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "爱蕾塔好像\x01",
            "也玩得十分开心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在开始我要\x01",
            "显出更具母亲魅力的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A84")

    label("loc_69F4")


    ChrTalk(
        0xFE,
        (
            "今天特地请假\x01",
            "来看我儿子的英姿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在开始我要\x01",
            "显出更具母亲魅力的样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A84")

    TalkEnd(0x2A)
    Return()

    # Function_39_68E2 end

    def Function_40_6A88(): pass

    label("Function_40_6A88")

    TalkBegin(0x2B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_6AAF")

    ChrTalk(
        0xFE,
        (
            "爱蕾塔渴了，\x01",
            "好想喝果汁啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AD7")

    label("loc_6AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6AD7")

    ChrTalk(
        0xFE,
        (
            "嘿嘿，哥哥～\x01",
            "我们来玩了～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AD7")

    TalkEnd(0x2B)
    Return()

    # Function_40_6A88 end

    def Function_41_6ADB(): pass

    label("Function_41_6ADB")

    TalkBegin(0x2C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_6B9C")

    ChrTalk(
        0xFE,
        "呼，找到妹妹了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她在学校里\x01",
            "也和基诺奇奥很要好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C5F")

    label("loc_6B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6C5F")

    ChrTalk(
        0xFE,
        (
            "呼，只有在这个时候\x01",
            "才能进到学院里面看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，妹妹的教室在哪呢……\x01",
            "作为监护人我有应尽的义务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C5F")

    TalkEnd(0x2C)
    Return()

    # Function_41_6ADB end

    def Function_42_6C63(): pass

    label("Function_42_6C63")

    TalkBegin(0x2D)

    ChrTalk(
        0xFE,
        (
            "唔唔，\x01",
            "百日战役后经济发展的相关考察……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x2D)
    Return()

    # Function_42_6C63 end

    def Function_43_6CC5(): pass

    label("Function_43_6CC5")

    TalkBegin(0x2E)

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "好想在什么地方休息一下啊……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x2E)
    Return()

    # Function_43_6CC5 end

    def Function_44_6CEA(): pass

    label("Function_44_6CEA")

    TalkBegin(0x2F)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "好像都是些十分深奥的东西啊……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x2F)
    Return()

    # Function_44_6CEA end

    def Function_45_6D1E(): pass

    label("Function_45_6D1E")

    TalkBegin(0x30)

    ChrTalk(
        0xFE,
        "虽然在学校学习是很好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是想把孩子\x01",
            "培育得更加富有感情些。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x30)
    Return()

    # Function_45_6D1E end

    def Function_46_6D95(): pass

    label("Function_46_6D95")

    TalkBegin(0x32)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_6E17")

    ChrTalk(
        0xFE,
        (
            "母亲老是对\x01",
            "入学的事唠叨个不停。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "必须要考试合格\x01",
            "才能进来这里读书的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E52")

    label("loc_6E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6E52")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "平时就是在这里上课的吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E52")

    TalkEnd(0x32)
    Return()

    # Function_46_6D95 end

    def Function_47_6E56(): pass

    label("Function_47_6E56")

    TalkBegin(0x31)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_6EC3")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "学园祭的活动好充实啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "越来越想让我的孩子\x01",
            "来这儿读书了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F57")

    label("loc_6EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6F57")

    ChrTalk(
        0xFE,
        (
            "今天我和儿子一起来\x01",
            "侦察著名的王立学院。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他以明年的考试为目标，\x01",
            "信心很足呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F57")

    TalkEnd(0x31)
    Return()

    # Function_47_6E56 end

    def Function_48_6F5B(): pass

    label("Function_48_6F5B")

    TalkBegin(0x34)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_70FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7074")
    OP_A2(0x457)
    OP_4A(0x8, 255)

    ChrTalk(
        0x8,
        (
            "#781F戴尔蒙市长，\x01",
            "自从去年的王国会议之后我们也好久不见了。\x02\x03",
            "这段时间，你身体怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#661F就像你看到的，结实着呢。\x01",
            "科林兹校长也很精神嘛。\x02\x03",
            "今天我打算好好放松一下。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x34, 0x10)
    OP_4B(0x8, 255)
    Jump("loc_70FA")

    label("loc_7074")


    ChrTalk(
        0x34,
        (
            "#661F啊，你们也来了。\x02\x03",
            "我每年都受到王立学院的邀请来参加学园祭。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70FA")

    TalkEnd(0x34)
    Return()

    # Function_48_6F5B end

    def Function_49_70FE(): pass

    label("Function_49_70FE")

    TalkBegin(0x33)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_7169")

    ChrTalk(
        0xFE,
        (
            "#620F刚才看到约修亚先生\x01",
            "一脸紧张地走过去……\x02\x03",
            "发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7567")

    label("loc_7169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7567")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7523")
    OP_A2(0x453)

    ChrTalk(
        0x101,
        "#004F啊，莉拉小姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#621F……二位真是好久没见了。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x24, 0x10)
    TurnDirection(0x24, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x24, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_71DD")
    SetChrSubChip(0x24, 2)
    Jump("loc_720E")

    label("loc_71DD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x24, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_71F3")
    SetChrSubChip(0x24, 1)
    Jump("loc_720E")

    label("loc_71F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x24, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7209")
    SetChrSubChip(0x24, 0)
    Jump("loc_720E")

    label("loc_7209")

    SetChrSubChip(0x24, 2)

    label("loc_720E")

    OP_8C(0x24, 270, 0)
    SetChrFlags(0x24, 0x10)

    ChrTalk(
        0x24,
        (
            "#613F啊，这不是\x01",
            "艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x24, 0)
    TurnDirection(0x102, 0x24, 0)
    TurnDirection(0x105, 0x24, 0)

    ChrTalk(
        0x101,
        (
            "#004F啊，梅贝尔市长也在！？\x02\x03",
            "你们两位为什么会在这里呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#611F呵呵，\x01",
            "其实我是这个学院的毕业生。\x02\x03",
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
        0x24,
        (
            "#610F那么你们俩是为什么来这儿的啊？\x01",
            "　\x02\x03",
            "难道是为了协会的工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嘿嘿，其实呢……\x02",
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
        0x24,
        (
            "#613F哦，是协助演出啊。\x02\x03",
            "#611F我也认为演出是很考功夫的。\x01",
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
            "#017F（唔，真不想让\x01",
            "　认识的人看到啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0)
    Jump("loc_7567")

    label("loc_7523")


    ChrTalk(
        0xFE,
        (
            "#621F……二位真是好久没见了。\x01",
            "还是那么有精神呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7567")

    TalkEnd(0x33)
    Return()

    # Function_49_70FE end

    def Function_50_756B(): pass

    label("Function_50_756B")

    TalkBegin(0x35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_75E4")

    ChrTalk(
        0xFE,
        (
            "过去的学园祭，\x01",
            "班级展示全都是研究发表……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "时代变迁啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7672")

    label("loc_75E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7672")

    ChrTalk(
        0xFE,
        (
            "在我们的学生时代，\x01",
            "还没有这个校舍呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这北面的古老建筑物\x01",
            "就是以前的校舍。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7672")

    TalkEnd(0x35)
    Return()

    # Function_50_756B end

    def Function_51_7676(): pass

    label("Function_51_7676")

    TalkBegin(0x36)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_76EC")

    ChrTalk(
        0xFE,
        (
            "……期末考试成绩优秀者\x01",
            "……科洛丝·琳希……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎，\x01",
            "她和乔儿那孩子都好厉害……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_773A")

    label("loc_76EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_773A")

    ChrTalk(
        0xFE,
        (
            "和主日学校相比，\x01",
            "这里的学习更专业呀……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_773A")

    TalkEnd(0x36)
    Return()

    # Function_51_7676 end

    def Function_52_773E(): pass

    label("Function_52_773E")

    TalkBegin(0x37)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_77EA")

    ChrTalk(
        0xFE,
        (
            "下午的舞台剧\x01",
            "好像有很有趣的看点呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我问过女儿，\x01",
            "但她没告诉我详细情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7855")

    label("loc_77EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7855")

    ChrTalk(
        0xFE,
        "这里就是学院啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然女儿在这里上学，\x01",
            "不过我还是第一次来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7855")

    TalkEnd(0x37)
    Return()

    # Function_52_773E end

    def Function_53_7859(): pass

    label("Function_53_7859")

    TalkBegin(0x38)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_78B7")

    ChrTalk(
        0xFE,
        (
            "走得好累呀，\x01",
            "去茶座休息一下吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7905")

    label("loc_78B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7905")

    ChrTalk(
        0xFE,
        (
            "在二楼的是自然系\x01",
            "和社会系的教室……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7905")

    TalkEnd(0x38)
    Return()

    # Function_53_7859 end

    def Function_54_7909(): pass

    label("Function_54_7909")

    TalkBegin(0x39)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_7963")

    ChrTalk(
        0xFE,
        (
            "各种展示都很有趣啊，\x01",
            "孩子们也感到很开心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7990")

    label("loc_7963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7990")

    ChrTalk(
        0xFE,
        "从什么地方开始看好呢……\x02",
    )

    CloseMessageWindow()

    label("loc_7990")

    TalkEnd(0x39)
    Return()

    # Function_54_7909 end

    def Function_55_7994(): pass

    label("Function_55_7994")

    TalkBegin(0x3A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_7A05")

    ChrTalk(
        0xFE,
        "我看了很多展示。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不仅很有趣，\x01",
            "也能从中看到学生们平时的学习成果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A3C")

    label("loc_7A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7A3C")

    ChrTalk(
        0xFE,
        (
            "真没想到这个建筑物里\x01",
            "有这么多地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A3C")

    TalkEnd(0x3A)
    Return()

    # Function_55_7994 end

    def Function_56_7A40(): pass

    label("Function_56_7A40")

    TalkBegin(0x3B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_7AA9")

    ChrTalk(
        0xFE,
        "哎呀，这个班级真让人吃惊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那些学生竟然\x01",
            "能做出那种东西来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AF0")

    label("loc_7AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7AF0")

    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "这里就是自然系的教室啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AF0")

    TalkEnd(0x3B)
    Return()

    # Function_56_7A40 end

    def Function_57_7AF4(): pass

    label("Function_57_7AF4")

    TalkBegin(0x3C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_7B48")

    ChrTalk(
        0xFE,
        (
            "展示好像快要结束了，\x01",
            "要快点看完才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B8D")

    label("loc_7B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7B8D")

    ChrTalk(
        0xFE,
        (
            "今年来的人\x01",
            "好像特别多啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B8D")

    TalkEnd(0x3C)
    Return()

    # Function_57_7AF4 end

    def Function_58_7B91(): pass

    label("Function_58_7B91")

    TalkBegin(0x3D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_7BED")

    ChrTalk(
        0xFE,
        "一早我就在想着舞台剧了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "快点开始吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C33")

    label("loc_7BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7C33")

    ChrTalk(
        0xFE,
        (
            "这里是学习的地方？\x01",
            "不是玩的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C33")

    TalkEnd(0x3D)
    Return()

    # Function_58_7B91 end

    def Function_59_7C37(): pass

    label("Function_59_7C37")

    EventBegin(0x0)
    OP_6D(-5190, 0, 34000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x31, 3150, 0, 31480, 90)
    SetChrPos(0x19, -5600, 0, 29020, 90)
    SetChrPos(0x25, 88600, 0, 34670, 0)
    SetChrPos(0x26, 89570, 0, 34410, 270)
    ClearChrFlags(0x29, 0x80)
    OP_4A(0x29, 255)
    SetChrPos(0x101, 2630, 0, 29470, 0)
    SetChrPos(0x102, 2510, 0, 28440, 0)
    SetChrPos(0x105, 1400, 0, 28920, 0)
    SetChrPos(0x29, 1690, 0, 30250, 0)
    FadeToBright(2000, 0)
    OP_6D(2050, 0, 29480, 4000)

    ChrTalk(
        0x29,
        (
            "#132F呀～这里就是了。\x01",
            "的确是十分正规的展览啊。\x02\x03",
            "从历史到经济，\x01",
            "各个领域的作品都有啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x29, 180, 400)

    ChrTalk(
        0x29,
        (
            "#130F哎呀，真是太好了。\x01",
            "我对这里的展览十分感兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F您太过奖了。\x02\x03",
            "我也是社会系专业的，\x01",
            "十分荣幸您会对展览感兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯～不过我对这种复杂的东西\x01",
            "就比较头痛了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F唉，我说你啊，\x01",
            "偶尔也该对这类东西有点兴趣嘛。\x02\x03",
            "#010F因为游击士也经常\x01",
            "会用到各种各样的知识哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "#130F哈哈，\x01",
            "那么我这就开始参观了。\x02\x03",
            "真是感谢你们带我来这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x29, 315, 400)

    def lambda_7FD7():
        OP_6D(1000, 0, 31440, 2000)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7FD7)
    OP_8E(0x29, 0xFFFFF970, 0x0, 0x8778, 0x7D0, 0x0)
    OP_8C(0x29, 0, 400)
    OP_4B(0x29, 255)
    OP_A2(0x45A)
    EventEnd(0x0)
    Return()

    # Function_59_7C37 end

    def Function_60_800E(): pass

    label("Function_60_800E")

    EventBegin(0x0)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    SetChrPos(0x9, 41350, -250, -3330, 0)
    SetChrPos(0xA, 40790, -250, -4570, 0)
    SetChrPos(0xB, 39420, 0, -2040, 0)
    SetChrPos(0xC, 41420, -250, -2220, 0)
    SetChrPos(0xD, 40840, 0, -1870, 0)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xA, 0x40)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x101, 46630, 2000, 7580, 180)
    SetChrPos(0x102, 46550, 2000, 8570, 180)
    SetChrPos(0x105, 45690, 2000, 8960, 180)
    OP_0D()

    ChrTalk(
        0xD,
        "#1P啊，是姐姐他们！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_814C():
        OP_6D(44200, 0, 1160, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_814C)
    WaitChrThread(0x101, 0x1)

    def lambda_8169():
        OP_8E(0xFE, 0xB27A, 0x0, 0xEE2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8169)

    def lambda_8184():
        OP_8E(0xFE, 0xA7C6, 0x0, 0x5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8184)
    Sleep(200)

    def lambda_81A4():
        OP_8E(0xFE, 0xABC2, 0x0, 0xFFFFFD6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_81A4)

    def lambda_81BF():
        OP_8E(0xFE, 0xA4CE, 0x0, 0x10E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_81BF)
    Sleep(200)

    def lambda_81DF():
        OP_8E(0xFE, 0xA848, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_81DF)
    Sleep(100)

    def lambda_81FF():
        OP_8E(0xFE, 0xB798, 0x0, 0xBEA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_81FF)
    Sleep(500)

    def lambda_821F():
        OP_8E(0xFE, 0xB27A, 0x0, 0xEE2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_821F)
    WaitChrThread(0x101, 0x1)

    def lambda_823F():
        OP_8E(0xFE, 0xA870, 0x0, 0x618, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_823F)
    WaitChrThread(0x102, 0x1)

    def lambda_825F():
        OP_8E(0xFE, 0xAF28, 0x0, 0x1A4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_825F)
    WaitChrThread(0x105, 0x1)

    def lambda_827F():
        OP_8E(0xFE, 0xAD02, 0x0, 0x55A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_827F)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 225, 400)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 225, 400)

    ChrTalk(
        0x105,
        (
            "#041F孩子们……\x01",
            "你们来了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#1P你们终于来了，小家伙们⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F#2P怎么样，玩得开心吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯～！\x01",
            "很开心哦～⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我今天吃了\x01",
            "好多好多点心呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "你就知道吃，\x01",
            "去哪儿吃到哪儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F呵呵……\x01",
            "你们是和特蕾莎老师一起来的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(
        0xD,
        (
            "#770F嗯，\x01",
            "她在那边和别人聊天……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#771F啊，来啦来啦⊙\x02",
    )

    CloseMessageWindow()

    def lambda_8439():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_8439)

    def lambda_8447():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8447)

    def lambda_8455():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_8455)

    def lambda_8463():

        label("loc_8463")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_8463")

    QueueWorkItem2(0x101, 2, lambda_8463)

    def lambda_8474():

        label("loc_8474")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_8474")

    QueueWorkItem2(0x102, 2, lambda_8474)

    def lambda_8485():

        label("loc_8485")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_8485")

    QueueWorkItem2(0x105, 2, lambda_8485)
    ClearChrFlags(0xA, 0x80)
    OP_8E(0xA, 0xA410, 0x0, 0xFFFFFBB4, 0x7D0, 0x0)
    TurnDirection(0xA, 0x105, 400)
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(
        0xA,
        "#750F呵呵，你们好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P啊，特蕾莎院长！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#048F老师……您好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#751F今天邀请我们来参加学园祭，\x01",
            "真的是感谢你啊。\x02\x03",
            "我和孩子们\x01",
            "今天真的玩得很开心。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x105, 400)

    ChrTalk(
        0xD,
        (
            "#770F对了，科洛丝姐姐。\x02\x03",
            "姐姐演的舞台剧\x01",
            "什么时候才开始啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_85D6():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_85D6)

    def lambda_85E4():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_85E4)

    def lambda_85F2():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_85F2)
    TurnDirection(0xC, 0x105, 400)

    ChrTalk(
        0xC,
        (
            "对啊对啊。\x01",
            "我们都很期待呢☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F是啊……\x01",
            "还要再等一会儿哦。\x02\x03",
            "#041F顺便说一句，不光是我，\x01",
            "艾丝蒂尔他们也会参加演出哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "真的？\x01",
            "哇，好期待呢～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "约修亚哥哥\x01",
            "演的是什么角色啊～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F#2P这个……\x01",
            "该怎么说好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#1P啊哈哈……\x01",
            "总之你们看了一定会喜欢的㈱\x02\x03",
            "#000F对了，特蕾莎院长。\x01",
            "你们还住在玛诺利亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F是的，承蒙旅店主人的好意，\x01",
            "让我们用很便宜的价钱租了个房间。\x02\x03",
            "#757F但是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#1P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P…………………………\x02\x03",
            "#010F好了，孩子们。\x01",
            "想去看看舞台剧的服装吗？\x02\x03",
            "有好多漂亮的\x01",
            "晚礼服和骑士装哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_88F0():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_88F0)

    def lambda_88FE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88FE)

    def lambda_890C():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_890C)

    def lambda_891A():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_891A)
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(
        0xC,
        "漂亮的晚礼服！？\x02",
    )

    CloseMessageWindow()

    def lambda_8945():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8945)
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(
        0xD,
        "#774F骑士装！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F呵呵……\x01",
            "看来你们很有兴趣啊。\x02\x03",
            "那么哥哥就破例，\x01",
            "带你们到舞台后面参观一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "好呀！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "波利也要去～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F（我们先到舞台休息室去，\x01",
            "　你们待会儿过来吧。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A5A():

        label("loc_8A5A")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8A5A")

    QueueWorkItem2(0x105, 1, lambda_8A5A)

    def lambda_8A6B():

        label("loc_8A6B")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8A6B")

    QueueWorkItem2(0x101, 1, lambda_8A6B)

    def lambda_8A7C():

        label("loc_8A7C")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8A7C")

    QueueWorkItem2(0xA, 1, lambda_8A7C)

    def lambda_8A8D():

        label("loc_8A8D")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8A8D")

    QueueWorkItem2(0xD, 1, lambda_8A8D)

    def lambda_8A9E():

        label("loc_8A9E")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8A9E")

    QueueWorkItem2(0xC, 1, lambda_8A9E)

    def lambda_8AAF():

        label("loc_8AAF")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8AAF")

    QueueWorkItem2(0x9, 1, lambda_8AAF)

    def lambda_8AC0():

        label("loc_8AC0")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8AC0")

    QueueWorkItem2(0xB, 1, lambda_8AC0)
    SetChrFlags(0x102, 0x4)
    OP_8C(0x102, 180, 400)
    OP_8E(0x102, 0xB004, 0x0, 0xFFFFFC68, 0x7D0, 0x0)
    OP_8E(0x102, 0xA8B6, 0x0, 0xFFFFF902, 0x7D0, 0x0)
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(
        0x102,
        "#010F那么大家跟我来吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)
    OP_8E(0x102, 0xA438, 0xFFFFFF06, 0xFFFFF5EC, 0x7D0, 0x0)
    ClearChrFlags(0x102, 0x4)

    def lambda_8B4B():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B4B)

    def lambda_8B66():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8B66)
    Sleep(700)

    def lambda_8B86():
        OP_8E(0xFE, 0xA622, 0xFFFFFF06, 0xFFFFF6FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8B86)
    WaitChrThread(0x102, 0x1)
    SetChrFlags(0x102, 0x80)

    def lambda_8BAB():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8BAB)

    def lambda_8BC6():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8BC6)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)

    def lambda_8BEB():
        OP_8E(0xFE, 0xA136, 0x0, 0xFFFFFCCC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8BEB)
    WaitChrThread(0xB, 0x1)

    def lambda_8C0B():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8C0B)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0xD, 0x1)
    SetChrFlags(0xD, 0x80)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xA, 0xFF)

    def lambda_8C55():
        OP_6D(42780, 0, 270, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8C55)

    def lambda_8C6D():
        OP_8E(0xFE, 0xA8FC, 0x0, 0xFFFFFFBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8C6D)
    Sleep(400)

    def lambda_8C8D():
        OP_8E(0xFE, 0xA474, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C8D)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0xA, 400)
    WaitChrThread(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "#750F呵呵，\x01",
            "约修亚真是个敏锐的孩子呢。\x02\x03",
            "#757F其实我是有些话\x01",
            "不方便在孩子们面前说……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8D30():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8D30)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        "#002F#1P这么说，难道……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "#754F嗯，因为已经考虑了好几天，\x01",
            "所以我还是决定接受市长的提议。\x02\x03",
            "毕竟不能再给\x01",
            "玛诺利亚的村民们添麻烦了。\x02\x03",
            "#750F今天的学园祭结束之后，\x01",
            "我就会告诉孩子们这件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#049F#2P这样……啊……\x02\x03",
            "虽然以后会很寂寞……\x01",
            "但我尊重老师您的决定……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#751F呵呵，别这么没精打采嘛。\x02\x03",
            "虽说要搬到王都，\x01",
            "但坐定期船的话一下子就到了。\x02\x03",
            "#750F而且我打算\x01",
            "到了王都之后去找份工作。\x02\x03",
            "我会慢慢地赚钱，\x01",
            "总有一天孤儿院能再重建的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#1P特蕾莎院长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#049F#2P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#751F好了……\x01",
            "你们不去找那些孩子吗？\x02\x03",
            "怎么说也不能把孩子们\x01",
            "全扔给约修亚一个人管啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2523   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_60_800E end

    def Function_61_8FEA(): pass

    label("Function_61_8FEA")

    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x3E, 0x80)
    OP_64(0x1, 0x1)
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

    # Function_61_8FEA end

    def Function_62_9052(): pass

    label("Function_62_9052")

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

    # Function_62_9052 end

    def Function_63_90C7(): pass

    label("Function_63_90C7")

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

    # Function_63_90C7 end

    def Function_64_912D(): pass

    label("Function_64_912D")

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

    # Function_64_912D end

    def Function_65_9190(): pass

    label("Function_65_9190")

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

    # Function_65_9190 end

    def Function_66_9200(): pass

    label("Function_66_9200")

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

    # Function_66_9200 end

    def Function_67_926B(): pass

    label("Function_67_926B")

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

    # Function_67_926B end

    def Function_68_92BF(): pass

    label("Function_68_92BF")

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

    # Function_68_92BF end

    def Function_69_931F(): pass

    label("Function_69_931F")

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

    # Function_69_931F end

    def Function_70_93A1(): pass

    label("Function_70_93A1")

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

    # Function_70_93A1 end

    def Function_71_93F8(): pass

    label("Function_71_93F8")

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

    # Function_71_93F8 end

    def Function_72_9457(): pass

    label("Function_72_9457")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　《导力演算器的存储装置》　　\x01",
            "※这个展示品是从\x01",
            "　蔡斯的中央工房借来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_72_9457 end

    def Function_73_94EF(): pass

    label("Function_73_94EF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《导力相性占卜机》\x01",
            "　 ※好评工作中！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_73_94EF end

    def Function_74_9580(): pass

    label("Function_74_9580")

    EventBegin(0x0)
    Fade(1000)

    def lambda_958D():
        OP_6D(84960, 1650, 32920, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_958D)

    def lambda_95A5():
        OP_67(0, 1300, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_95A5)

    def lambda_95BD():
        OP_6B(1400, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_95BD)

    def lambda_95CD():
        OP_6C(0, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_95CD)

    def lambda_95DD():
        OP_6E(262, 1000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_95DD)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_9605")
    Jump("loc_9652")

    label("loc_9605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_960F")
    Jump("loc_9652")

    label("loc_960F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_9637")
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x2C, 0x80)
    Jump("loc_9652")

    label("loc_9637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_9652")
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)

    label("loc_9652")

    Sleep(1000)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Fade(500)
    OP_74(0x6, 0x0, 0x1)
    OP_0D()
    Sleep(500)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "导力相性占卜机\x01",
            "Version:1.0014.4082\x01",
            "(C)Genis Royal School 1202\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 290, 56, 3)
    SetChrName("占卜机")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "想要占卜一下吗？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB4C")
    SetMessageWindowPos(72, 290, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_9751"),
        (1, "loc_9754"),
        (SWITCH_DEFAULT, "loc_9761"),
    )


    label("loc_9751")

    Jump("loc_976E")

    label("loc_9754")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96FD")

    label("loc_9761")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96FD")

    label("loc_976E")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要输入谁的资料呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        55,
        5,
        0,
        (
            "【艾丝蒂尔】\x01",      # 0
            "【约修亚】\x01",        # 1
            "【雪拉扎德】\x01",      # 2
            "【奥利维尔】\x01",      # 3
            "【科洛丝】\x01",        # 4
            "【奈尔】\x01",          # 5
            "【朵洛希】\x01",        # 6
        )
    )

    MenuEnd(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_9817"),
        (1, "loc_985E"),
        (2, "loc_98A5"),
        (3, "loc_98F0"),
        (4, "loc_9937"),
        (5, "loc_997B"),
        (6, "loc_99BF"),
        (SWITCH_DEFAULT, "loc_9A05"),
    )


    label("loc_9817")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【艾丝蒂尔·布莱特】\x01",
            "七耀历１１８６年８月７日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_985E")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【约修亚·布莱特】\x01",
            "七耀历１１８５年１２月２０日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_98A5")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【雪拉扎德·哈维】\x01",
            "七耀历１１７９年５月１４日生出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_98F0")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【奥利维尔·朗海姆】\x01",
            "七耀历１１７７年４月１日生出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_9937")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【科洛丝·琳希】\x01",
            "七耀历１１８６年１０月１１日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_997B")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【奈尔·班兹】\x01",
            "七耀历１１７２年１１月２５日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_99BF")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【朵洛希·海娅特】\x01",
            "七耀历１１８２年１月２２日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_9A05")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "接下来请输入\x01",
            "对方的资料。\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        426,
        5,
        0,
        (
            "【艾丝蒂尔】\x01",      # 0
            "【约修亚】\x01",        # 1
            "【雪拉扎德】\x01",      # 2
            "【奥利维尔】\x01",      # 3
            "【科洛丝】\x01",        # 4
            "【奈尔】\x01",          # 5
            "【朵洛希】\x01",        # 6
        )
    )

    MenuEnd(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_9AAB"),
        (1, "loc_9AF2"),
        (2, "loc_9B39"),
        (3, "loc_9B84"),
        (4, "loc_9BCB"),
        (5, "loc_9C0F"),
        (6, "loc_9C53"),
        (SWITCH_DEFAULT, "loc_9C99"),
    )


    label("loc_9AAB")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【艾丝蒂尔·布莱特】\x01",
            "七耀历１１８６年８月７日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9AF2")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【约修亚·布莱特】\x01",
            "七耀历１１８５年１２月２０日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9B39")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【雪拉扎德·哈维】\x01",
            "七耀历１１７９年５月１４日生出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9B84")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【奥利维尔·朗海姆】\x01",
            "七耀历１１７７年４月１日生出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9BCB")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【科洛丝·琳希】\x01",
            "七耀历１１８６年１０月１１日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9C0F")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【奈尔·班兹】\x01",
            "七耀历１１７２年１１月２５日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9C53")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【朵洛希·海娅特】\x01",
            "七耀历１１８２年１月２２日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9C99")

    SetChrName("占卜机")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那么，占卜现在开始。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x27, 0x0, 0x64)
    OP_75(0x6, 0x0, 0x0)
    Sleep(50)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    Sleep(60)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x2)
    Sleep(70)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(80)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(90)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x5)
    Sleep(100)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(110)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(120)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    Sleep(130)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x2)
    Sleep(140)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(150)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(160)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x5)
    Sleep(170)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(180)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(190)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    Sleep(200)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x2)
    Sleep(210)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(220)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(230)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x5)
    Sleep(240)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(260)
    SetChrName("占卜机")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (4, "loc_9F31"),
        (40, "loc_9F31"),
        (12, "loc_9F31"),
        (21, "loc_9F31"),
        (24, "loc_9F31"),
        (42, "loc_9F31"),
        (36, "loc_9F31"),
        (63, "loc_9F31"),
        (5, "loc_A0E9"),
        (50, "loc_A0E9"),
        (14, "loc_A0E9"),
        (41, "loc_A0E9"),
        (26, "loc_A0E9"),
        (62, "loc_A0E9"),
        (2, "loc_A2A6"),
        (20, "loc_A2A6"),
        (6, "loc_A2A6"),
        (60, "loc_A2A6"),
        (15, "loc_A2A6"),
        (51, "loc_A2A6"),
        (1, "loc_A49C"),
        (10, "loc_A49C"),
        (13, "loc_A49C"),
        (31, "loc_A49C"),
        (25, "loc_A49C"),
        (52, "loc_A49C"),
        (46, "loc_A49C"),
        (64, "loc_A49C"),
        (16, "loc_A659"),
        (61, "loc_A659"),
        (23, "loc_A659"),
        (32, "loc_A659"),
        (34, "loc_A659"),
        (43, "loc_A659"),
        (56, "loc_A659"),
        (65, "loc_A659"),
        (3, "loc_A834"),
        (30, "loc_A834"),
        (35, "loc_A834"),
        (53, "loc_A834"),
        (45, "loc_A834"),
        (54, "loc_A834"),
        (0, "loc_A9E8"),
        (11, "loc_A9E8"),
        (22, "loc_A9E8"),
        (33, "loc_A9E8"),
        (44, "loc_A9E8"),
        (55, "loc_A9E8"),
        (66, "loc_A9E8"),
        (SWITCH_DEFAULT, "loc_AB11"),
    )


    label("loc_9F31")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(1000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天是你们\x01",
            "彼此都很主动的一天。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要主动采取行动，\x01",
            "这样两人应该能度过快乐的一天。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "谈话很容易投机，\x01",
            "只要能够两人独处，\x01",
            "很快就能得到对方的心。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果被邀请的话，\x01",
            "不要犹豫，马上接受。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有共同兴趣和目的的情况下，\x01",
            "两人的关系会发展得十分顺利。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB11")

    label("loc_A0E9")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(1000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天两人的意识很协调，\x01",
            "能度过开心的一天。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在两人中的一个遇到麻烦的情况下，\x01",
            "不要嫌麻烦，马上帮助对方。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有共同意识的情况下，\x01",
            "能知道对方隐蔽的一面，\x01",
            "两人的友情也会进一步加深。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天两人会有爱情\x01",
            "或注意到对方是特别的朋友这种意识。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB11")

    label("loc_A2A6")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x5)
    Sleep(1000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天两人会对\x01",
            "事物的看法非常乐观。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "即使各自的主张\x01",
            "有出入也没有关系，\x01",
            "很快就能安稳度过的。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "平时可能有一方会\x01",
            "将自己的意见强加于对方，\x01",
            "使关系变得紧张……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不过在这一天\x01",
            "两人的情绪会非常安定。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "平时不能说的话，\x01",
            "今天就有机会说了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB11")

    label("loc_A49C")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x2)
    Sleep(1000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天两人非常主动。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果有两人都想做的事，\x01",
            "一起来做是个\x01",
            "绝好的机会。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不过，不要太过\x01",
            "把自己的意见强加于对方，\x01",
            "这一点必须要注意。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "尊重对方的步调，\x01",
            "关系会有快速进展的机会。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "总之首先考虑\x01",
            "对方的心情是最重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB11")

    label("loc_A659")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(1000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天两人就算在一起，\x01",
            "无论到哪儿都会是不顺利的一天。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "隐藏的秘密会暴露，\x01",
            "如果欺骗对方的话，\x01",
            "会让对方感到不可信任。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "找不到共同的话题，\x01",
            "谈话也总是不投机。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这样的日子还是不要硬靠近，\x01",
            "下决心做其他的事吧。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "留出距离和时间，\x01",
            "应该能再确认一下对方的重要性。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB11")

    label("loc_A834")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(1000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天两人会\x01",
            "对某事都不做出让步，\x01",
            "可能会导致吵架。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "吵架拖太长的话，\x01",
            "可能会发展到非本意的离别。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这样的日子最好\x01",
            "不要两人单独相处，\x01",
            "应该和共同的朋友一起行动。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果对方说了什么不好的话，\x01",
            "不要太过在意，\x01",
            "要用自己宽容的心去听。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB11")

    label("loc_A9E8")

    OP_74(0x6, 0x0, 0x0)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xF7, 0x0, 0x64)
    OP_20(0x0)
    FadeToDark(500, 0, -1)
    OP_5F(0x1)
    OP_5F(0x0)
    OP_56(0x0)
    OP_0D()
    Sleep(500)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "4 Error(s)...  0 Warning(s)...\x01",
            "导力相性占卜机...强制中止\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "导力相性占卜机\x01",
            "Version:1.0014.4082\x01",
            "(C)Genis Royal School 1202\x01",
            "#200W　#20W\x01",
            "MEMORY_CHECK#100W..........#20WOK!\x01",
            "#200W　#20W\x01",
            "重启动\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 290, 56, 3)
    OP_56(0x0)
    FadeToBright(500, 0)
    OP_1E()
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    OP_0D()
    Jump("loc_AB11")

    label("loc_AB11")

    SetMessageWindowPos(72, 290, 56, 3)
    OP_5F(0x1)
    OP_5F(0x0)
    OP_74(0x6, 0x0, 0x1)
    SetChrName("占卜机")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要继续占卜吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96FD")

    label("loc_AB4C")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Fade(1000)
    OP_74(0x6, 0x0, 0x0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_AB8F")
    Jump("loc_ABDC")

    label("loc_AB8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_AB99")
    Jump("loc_ABDC")

    label("loc_AB99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_ABC1")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x2C, 0x80)
    Jump("loc_ABDC")

    label("loc_ABC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_ABDC")
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)

    label("loc_ABDC")

    EventEnd(0x1)
    Return()

    # Function_74_9580 end

    def Function_75_ABDF(): pass

    label("Function_75_ABDF")

    SetPlaceName(0x6F) # 主楼　社会系教室
    Return()

    # Function_75_ABDF end

    def Function_76_ABE3(): pass

    label("Function_76_ABE3")

    SetPlaceName(0x5E) # 主楼　社会系教室
    Return()

    # Function_76_ABE3 end

    def Function_77_ABE7(): pass

    label("Function_77_ABE7")

    SetPlaceName(0x6E) # 主楼　社会系教室
    Return()

    # Function_77_ABE7 end

    def Function_78_ABEB(): pass

    label("Function_78_ABEB")

    SetPlaceName(0x74) # 主楼　社会系教室
    Return()

    # Function_78_ABEB end

    def Function_79_ABEF(): pass

    label("Function_79_ABEF")

    SetPlaceName(0x73) # 主楼　社会系教室
    Return()

    # Function_79_ABEF end

    SaveToFile()

Try(main)
