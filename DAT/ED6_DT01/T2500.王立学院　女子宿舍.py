from ED6ScenarioHelper import *

def main():
    # 王立学院　女子宿舍

    CreateScenaFile(
        FileName            = 'T2500   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2500.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2500   ._SN',
            'ED6_DT01/T2500_1 ._SN',
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
        '基库',                                 # 11
        '艾福托老师',                           # 12
        '罗迪',                                 # 13
        '黛拉',                                 # 14
        '亚吉鲁',                               # 15
        '莫妮卡',                               # 16
        '莉秋尔',                               # 17
        '巴托姆',                               # 18
        '德尼斯',                               # 19
        '芙拉瑟',                               # 20
        '蕾娜',                                 # 21
        '勤务员巴克斯',                         # 22
        '奈尔',                                 # 23
        '凯诺娜上尉',                           # 24
        '卡露娜',                               # 25
        '雷克斯',                               # 26
        '卡拉',                                 # 27
        '卢希娅',                               # 28
        '波尔多斯',                             # 29
        '诺莉雅',                               # 30
        '参观客',                               # 31
        '参观客',                               # 32
        '参观客',                               # 33
        '参观客',                               # 34
        '参观客',                               # 35
        '参观客',                               # 36
        '参观客',                               # 37
        '参观客',                               # 38
        '参观客',                               # 39
        '参观客',                               # 40
        '参观客',                               # 41
        '参观客',                               # 42
        '参观客',                               # 43
        '参观客',                               # 44
        '参观客',                               # 45
        '基尔巴特',                             # 46
        '王立学院·小道',                       # 47
        '街景林道方向',                         # 48
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
        'ED6_DT07/CH02320 ._CH',             # 02
        'ED6_DT07/CH01460 ._CH',             # 03
        'ED6_DT07/CH01360 ._CH',             # 04
        'ED6_DT07/CH01370 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01590 ._CH',             # 07
        'ED6_DT07/CH01580 ._CH',             # 08
        'ED6_DT07/CH01090 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH02060 ._CH',             # 0B
        'ED6_DT07/CH02100 ._CH',             # 0C
        'ED6_DT07/CH01240 ._CH',             # 0D
        'ED6_DT07/CH01020 ._CH',             # 0E
        'ED6_DT07/CH01030 ._CH',             # 0F
        'ED6_DT07/CH01070 ._CH',             # 10
        'ED6_DT07/CH01680 ._CH',             # 11
        'ED6_DT07/CH01690 ._CH',             # 12
        'ED6_DT06/CH20051 ._CH',             # 13
        'ED6_DT07/CH01480 ._CH',             # 14
        'ED6_DT07/CH01040 ._CH',             # 15
        'ED6_DT07/CH01230 ._CH',             # 16
        'ED6_DT07/CH01060 ._CH',             # 17
        'ED6_DT07/CH01070 ._CH',             # 18
        'ED6_DT07/CH01050 ._CH',             # 19
        'ED6_DT07/CH01490 ._CH',             # 1A
        'ED6_DT07/CH01180 ._CH',             # 1B
        'ED6_DT07/CH01130 ._CH',             # 1C
        'ED6_DT07/CH01003 ._CH',             # 1D
        'ED6_DT07/CH01023 ._CH',             # 1E
        'ED6_DT07/CH01153 ._CH',             # 1F
        'ED6_DT07/CH01033 ._CH',             # 20
        'ED6_DT07/CH01160 ._CH',             # 21
        'ED6_DT07/CH01220 ._CH',             # 22
        'ED6_DT07/CH02420 ._CH',             # 23
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH02320P._CP',             # 02
        'ED6_DT07/CH01460P._CP',             # 03
        'ED6_DT07/CH01360P._CP',             # 04
        'ED6_DT07/CH01370P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01590P._CP',             # 07
        'ED6_DT07/CH01580P._CP',             # 08
        'ED6_DT07/CH01090P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH02060P._CP',             # 0B
        'ED6_DT07/CH02100P._CP',             # 0C
        'ED6_DT07/CH01240P._CP',             # 0D
        'ED6_DT07/CH01020P._CP',             # 0E
        'ED6_DT07/CH01030P._CP',             # 0F
        'ED6_DT07/CH01070P._CP',             # 10
        'ED6_DT07/CH01680P._CP',             # 11
        'ED6_DT07/CH01690P._CP',             # 12
        'ED6_DT06/CH20051P._CP',             # 13
        'ED6_DT07/CH01480P._CP',             # 14
        'ED6_DT07/CH01040P._CP',             # 15
        'ED6_DT07/CH01230P._CP',             # 16
        'ED6_DT07/CH01060P._CP',             # 17
        'ED6_DT07/CH01070P._CP',             # 18
        'ED6_DT07/CH01050P._CP',             # 19
        'ED6_DT07/CH01490P._CP',             # 1A
        'ED6_DT07/CH01180P._CP',             # 1B
        'ED6_DT07/CH01130P._CP',             # 1C
        'ED6_DT07/CH01003P._CP',             # 1D
        'ED6_DT07/CH01023P._CP',             # 1E
        'ED6_DT07/CH01153P._CP',             # 1F
        'ED6_DT07/CH01033P._CP',             # 20
        'ED6_DT07/CH01160P._CP',             # 21
        'ED6_DT07/CH01220P._CP',             # 22
        'ED6_DT07/CH02420P._CP',             # 23
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
        X                   = 800,
        Z                   = 6000,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 23200,
        Z                   = 0,
        Y                   = 46000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 39500,
        Z                   = -2000,
        Y                   = 36400,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 28300,
        Z                   = -2000,
        Y                   = 36260,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 27300,
        Z                   = -2000,
        Y                   = 38300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 39000,
        Z                   = -2000,
        Y                   = 38100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 40400,
        Z                   = -2000,
        Y                   = 50900,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 46100,
        Z                   = 0,
        Y                   = 63100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 29000,
        Z                   = 0,
        Y                   = 28100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 28500,
        Z                   = -2000,
        Y                   = 54600,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 27600,
        Z                   = -2000,
        Y                   = 54790,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 35800,
        Z                   = 0,
        Y                   = 78000,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 29600,
        Z                   = -2000,
        Y                   = 56200,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 28300,
        Z                   = -2000,
        Y                   = 37100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 47280,
        Z                   = 0,
        Y                   = 48810,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 29200,
        Z                   = -2000,
        Y                   = 51000,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 29500,
        Z                   = -2000,
        Y                   = 52500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 29700,
        Z                   = -2000,
        Y                   = 51300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 39400,
        Z                   = -2000,
        Y                   = 39700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 38900,
        Z                   = -2000,
        Y                   = 41300,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 39850,
        Z                   = -2000,
        Y                   = 45950,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 48940,
        Z                   = 0,
        Y                   = 27010,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 21080,
        Z                   = 0,
        Y                   = 31060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 34850,
        Z                   = 0,
        Y                   = 74970,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 36840,
        Z                   = 0,
        Y                   = 68820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 43200,
        Z                   = -750,
        Y                   = 48790,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 30480,
        Z                   = -2000,
        Y                   = 34130,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 25790,
        Z                   = -1750,
        Y                   = 43460,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 39090,
        Z                   = -2000,
        Y                   = 50780,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 34620,
        Z                   = 200,
        Y                   = 22890,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 43410,
        Z                   = 200,
        Y                   = 20470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 42080,
        Z                   = 200,
        Y                   = 21850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 42150,
        Z                   = 200,
        Y                   = 16239,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = 37080,
        Z                   = 0,
        Y                   = 18890,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = 45250,
        Z                   = 0,
        Y                   = 45990,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 19030,
        Z                   = 0,
        Y                   = 46080,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
    )

    DeclNpc(
        X                   = 84080,
        Z                   = 0,
        Y                   = 28010,
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
        X                   = -3490,
        Z                   = 0,
        Y                   = 46180,
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
        X                   = 12290,
        Y                   = -1000,
        Z                   = 47300,
        Range               = 14900,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xAE38,
        Unknown_18          = 0x0,
        Unknown_1C          = 52,
    )

    DeclEvent(
        X                   = 41180,
        Y                   = 0,
        Z                   = 74060,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 56,
    )

    DeclEvent(
        X                   = 53030,
        Y                   = 0,
        Z                   = 67260,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 56,
    )

    DeclEvent(
        X                   = 53150,
        Y                   = 0,
        Z                   = 59630,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 57,
    )

    DeclEvent(
        X                   = 48380,
        Y                   = 0,
        Z                   = 45960,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 57,
    )

    DeclEvent(
        X                   = 52870,
        Y                   = 0,
        Z                   = 32110,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 57,
    )

    DeclEvent(
        X                   = 53030,
        Y                   = 0,
        Z                   = 24850,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 58,
    )

    DeclEvent(
        X                   = 47120,
        Y                   = 0,
        Z                   = 19010,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 58,
    )

    DeclEvent(
        X                   = 22030,
        Y                   = 0,
        Z                   = 25660,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 59,
    )

    DeclEvent(
        X                   = 22010,
        Y                   = 0,
        Z                   = 67170,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 60,
    )


    DeclActor(
        TriggerX            = 13480,
        TriggerZ            = 1000,
        TriggerY            = 45900,
        TriggerRange        = 1000,
        ActorX              = 13480,
        ActorZ              = 1000,
        ActorY              = 45900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 51,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22030,
        TriggerZ            = 500,
        TriggerY            = 24930,
        TriggerRange        = 800,
        ActorX              = 22030,
        ActorZ              = 1500,
        ActorY              = 24930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 54,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22030,
        TriggerZ            = 500,
        TriggerY            = 68110,
        TriggerRange        = 800,
        ActorX              = 22030,
        ActorZ              = 1500,
        ActorY              = 68110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 53,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22030,
        TriggerZ            = 500,
        TriggerY            = 24930,
        TriggerRange        = 1500,
        ActorX              = 22030,
        ActorZ              = 3000,
        ActorY              = 24930,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41770,
        TriggerZ            = 0,
        TriggerY            = 69260,
        TriggerRange        = 1500,
        ActorX              = 41770,
        ActorZ              = 3000,
        ActorY              = 69260,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 54350,
        TriggerZ            = 0,
        TriggerY            = 28820,
        TriggerRange        = 1500,
        ActorX              = 54350,
        ActorZ              = 3000,
        ActorY              = 28820,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_8E2",          # 00, 0
        "Function_1_C06",          # 01, 1
        "Function_2_F79",          # 02, 2
        "Function_3_F84",          # 03, 3
        "Function_4_FA8",          # 04, 4
        "Function_5_1156",         # 05, 5
        "Function_6_117A",         # 06, 6
        "Function_7_11D7",         # 07, 7
        "Function_8_1234",         # 08, 8
        "Function_9_1258",         # 09, 9
        "Function_10_127C",        # 0A, 10
        "Function_11_12A0",        # 0B, 11
        "Function_12_12FD",        # 0C, 12
        "Function_13_14C1",        # 0D, 13
        "Function_14_178E",        # 0E, 14
        "Function_15_1981",        # 0F, 15
        "Function_16_1AB5",        # 10, 16
        "Function_17_1D78",        # 11, 17
        "Function_18_2298",        # 12, 18
        "Function_19_24F9",        # 13, 19
        "Function_20_2581",        # 14, 20
        "Function_21_2692",        # 15, 21
        "Function_22_2790",        # 16, 22
        "Function_23_2B7B",        # 17, 23
        "Function_24_2D49",        # 18, 24
        "Function_25_2DB8",        # 19, 25
        "Function_26_2ED9",        # 1A, 26
        "Function_27_2F2F",        # 1B, 27
        "Function_28_2F55",        # 1C, 28
        "Function_29_2F78",        # 1D, 29
        "Function_30_2FCE",        # 1E, 30
        "Function_31_3079",        # 1F, 31
        "Function_32_3121",        # 20, 32
        "Function_33_31EA",        # 21, 33
        "Function_34_32C0",        # 22, 34
        "Function_35_333A",        # 23, 35
        "Function_36_33AB",        # 24, 36
        "Function_37_342E",        # 25, 37
        "Function_38_34A0",        # 26, 38
        "Function_39_3551",        # 27, 39
        "Function_40_35F5",        # 28, 40
        "Function_41_368E",        # 29, 41
        "Function_42_372C",        # 2A, 42
        "Function_43_37DD",        # 2B, 43
        "Function_44_3853",        # 2C, 44
        "Function_45_38FD",        # 2D, 45
        "Function_46_3996",        # 2E, 46
        "Function_47_3C92",        # 2F, 47
        "Function_48_40A9",        # 30, 48
        "Function_49_4973",        # 31, 49
        "Function_50_4DBF",        # 32, 50
        "Function_51_5621",        # 33, 51
        "Function_52_604F",        # 34, 52
        "Function_53_632A",        # 35, 53
        "Function_54_637E",        # 36, 54
        "Function_55_63D2",        # 37, 55
        "Function_56_6410",        # 38, 56
        "Function_57_6414",        # 39, 57
        "Function_58_6418",        # 3A, 58
        "Function_59_641C",        # 3B, 59
        "Function_60_6420",        # 3C, 60
    )


    def Function_0_8E2(): pass

    label("Function_0_8E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_907")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 30130, 0, 26060, 180)
    Jump("loc_B89")

    label("loc_907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_927")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 42490, 0, 17270, 135)
    Jump("loc_B89")

    label("loc_927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_9FE")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 39800, -2000, 39200, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39530, -2000, 52980, 270)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2D, 23030, 250, 26410, 180)
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
    SetChrPos(0x2B, 49710, 0, 30200, 90)
    OP_43(0x2B, 0x0, 0x0, 0x4)
    SetChrFlags(0x2B, 0x10)
    ClearChrFlags(0x2C, 0x80)
    Jump("loc_B89")

    label("loc_9FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_A8C")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 39400, -2000, 54190, 270)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x2D, 0x80)
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
    Jump("loc_B89")

    label("loc_A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_AD1")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 39000, -2000, 37100, 90)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 47880, 0, 56070, 135)
    Jump("loc_B89")

    label("loc_AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_AFB")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 39000, -2000, 37100, 90)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_B89")

    label("loc_AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_B1B")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 34000, -2000, 39780, 180)
    Jump("loc_B89")

    label("loc_B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_B3B")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 39960, 0, 26140, 135)
    Jump("loc_B89")

    label("loc_B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_B5B")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 34250, 0, 63640, 180)
    Jump("loc_B89")

    label("loc_B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_B89")
    ClearChrFlags(0x11, 0x80)
    OP_43(0x11, 0x0, 0x0, 0x3)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 44010, 0, 51050, 315)

    label("loc_B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_BA5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x800)
    OP_A3(0x3FA)
    Event(0, 48)

    label("loc_BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_BB3")
    OP_A3(0x3FB)
    Event(0, 49)

    label("loc_BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_BCD")
    OP_A2(0x434)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FC)
    Event(0, 50)

    label("loc_BCD")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_BD9"),
        (SWITCH_DEFAULT, "loc_BF4"),
    )


    label("loc_BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF1")
    OP_A2(0x42E)
    ClearMapFlags(0x10000000)
    Event(0, 47)

    label("loc_BF1")

    Jump("loc_BF4")

    label("loc_BF4")

    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_8E2 end

    def Function_1_C06(): pass

    label("Function_1_C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C27")
    OP_B1("t2500_y")
    Jump("loc_C30")

    label("loc_C27")

    OP_B1("t2500_n")

    label("loc_C30")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFEBFB0, 0x3004C)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C96")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C76")
    OP_65(0x3, 0x1)

    label("loc_C76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C86")
    OP_65(0x4, 0x1)

    label("loc_C86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C96")
    OP_65(0x5, 0x1)

    label("loc_C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_D4A")
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)
    OP_71(0x15, 0x4)
    OP_71(0x16, 0x4)
    OP_71(0x17, 0x4)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    OP_71(0x20, 0x4)
    OP_71(0x23, 0x4)
    OP_71(0x24, 0x4)
    OP_71(0x25, 0x4)
    OP_71(0x26, 0x4)
    OP_71(0x27, 0x4)
    OP_71(0x28, 0x4)
    OP_71(0x29, 0x4)
    OP_71(0x2A, 0x4)
    OP_71(0x2B, 0x4)
    OP_71(0x2C, 0x4)
    Jump("loc_E33")

    label("loc_D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_D5D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E33")

    label("loc_D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_D7A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x800)
    OP_1B(0xA, 0x0, 0x2)
    Jump("loc_E33")

    label("loc_D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D89")
    Jump("loc_E33")

    label("loc_D89")

    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)
    OP_71(0x15, 0x4)
    OP_71(0x16, 0x4)
    OP_71(0x17, 0x4)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    OP_71(0x20, 0x4)
    OP_71(0x23, 0x4)
    OP_71(0x24, 0x4)
    OP_71(0x25, 0x4)
    OP_71(0x26, 0x4)
    OP_71(0x27, 0x4)
    OP_71(0x28, 0x4)
    OP_71(0x29, 0x4)
    OP_71(0x2A, 0x4)
    OP_71(0x2B, 0x4)
    OP_71(0x2C, 0x4)

    label("loc_E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6F")
    OP_10(0x19, 0x1)
    OP_10(0x1A, 0x1)
    OP_10(0x1B, 0x1)
    OP_10(0x1C, 0x1)
    OP_10(0x1D, 0x1)
    OP_10(0x3, 0x0)
    OP_10(0x4, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x6, 0x0)
    OP_10(0x7, 0x0)
    OP_10(0x13, 0x1)
    OP_10(0x14, 0x1)
    OP_10(0x8, 0x0)
    OP_10(0x9, 0x0)
    Jump("loc_EA1")

    label("loc_E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA1")
    OP_10(0xE, 0x1)
    OP_10(0xF, 0x1)
    OP_10(0x10, 0x1)
    OP_10(0x11, 0x1)
    OP_10(0x12, 0x1)
    OP_10(0x13, 0x1)
    OP_10(0x14, 0x1)
    OP_10(0x3, 0x0)
    OP_10(0x4, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x6, 0x0)
    OP_10(0x7, 0x0)
    OP_10(0x8, 0x0)
    OP_10(0x9, 0x0)

    label("loc_EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_EBB")
    OP_64(0x0, 0x1)
    OP_72(0x21, 0x10)
    OP_6F(0x21, 60)
    Jump("loc_F78")

    label("loc_EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_EE7")
    OP_64(0x0, 0x1)
    OP_72(0x21, 0x10)
    OP_6F(0x21, 60)
    OP_72(0x4, 0x10)
    OP_72(0x3, 0x10)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    Jump("loc_F78")

    label("loc_EE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3F")
    OP_72(0x21, 0x10)
    OP_71(0xA, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x1A, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_F1C")
    OP_72(0x1E, 0x4)

    label("loc_F1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_F2C")
    OP_72(0x12, 0x4)

    label("loc_F2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_F3C")
    OP_72(0x1A, 0x4)

    label("loc_F3C")

    Jump("loc_F78")

    label("loc_F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_F73")
    OP_64(0x0, 0x1)
    OP_72(0x21, 0x10)
    OP_6F(0x21, 60)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F70")
    OP_72(0x4, 0x10)
    OP_72(0x3, 0x10)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)

    label("loc_F70")

    Jump("loc_F78")

    label("loc_F73")

    OP_72(0x21, 0x10)

    label("loc_F78")

    Return()

    # Function_1_C06 end

    def Function_2_F79(): pass

    label("Function_2_F79")

    ClearMapFlags(0x800)
    OP_1B(0xA, 0x0, 0xFFFF)
    Return()

    # Function_2_F79 end

    def Function_3_F84(): pass

    label("Function_3_F84")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FA7")
    OP_8D(0xFE, 49260, 65690, 45050, 60310, 3000)
    Jump("Function_3_F84")

    label("loc_FA7")

    Return()

    # Function_3_F84 end

    def Function_4_FA8(): pass

    label("Function_4_FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_FB2")
    Jump("loc_FD9")

    label("loc_FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_FC7")
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD9")

    label("loc_FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_FD9")
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FD9")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFE")
    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_1140")

    label("loc_FFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1017")
    OP_99(0xFE, 0x1, 0x7, 0x514)
    Jump("loc_1140")

    label("loc_1017")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1030")
    OP_99(0xFE, 0x2, 0x7, 0x4E2)
    Jump("loc_1140")

    label("loc_1030")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1049")
    OP_99(0xFE, 0x3, 0x7, 0x4B0)
    Jump("loc_1140")

    label("loc_1049")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1062")
    OP_99(0xFE, 0x4, 0x7, 0x47E)
    Jump("loc_1140")

    label("loc_1062")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107B")
    OP_99(0xFE, 0x5, 0x7, 0x44C)
    Jump("loc_1140")

    label("loc_107B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1094")
    OP_99(0xFE, 0x6, 0x7, 0x41A)
    Jump("loc_1140")

    label("loc_1094")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AD")
    OP_99(0xFE, 0x0, 0x7, 0x54B)
    Jump("loc_1140")

    label("loc_10AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C6")
    OP_99(0xFE, 0x1, 0x7, 0x519)
    Jump("loc_1140")

    label("loc_10C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DF")
    OP_99(0xFE, 0x2, 0x7, 0x4E7)
    Jump("loc_1140")

    label("loc_10DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F8")
    OP_99(0xFE, 0x3, 0x7, 0x4B5)
    Jump("loc_1140")

    label("loc_10F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1111")
    OP_99(0xFE, 0x4, 0x7, 0x483)
    Jump("loc_1140")

    label("loc_1111")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112A")
    OP_99(0xFE, 0x5, 0x7, 0x451)
    Jump("loc_1140")

    label("loc_112A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1140")
    OP_99(0xFE, 0x6, 0x7, 0x41F)

    label("loc_1140")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1155")
    OP_99(0xFE, 0x0, 0x7, 0x4B0)
    Jump("loc_1140")

    label("loc_1155")

    Return()

    # Function_4_FA8 end

    def Function_5_1156(): pass

    label("Function_5_1156")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1179")
    OP_8D(0xFE, 41490, 48770, 38300, 42820, 3500)
    Jump("Function_5_1156")

    label("loc_1179")

    Return()

    # Function_5_1156 end

    def Function_6_117A(): pass

    label("Function_6_117A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11D6")
    OP_8E(0xFE, 0xB0D6, 0x0, 0x70BC, 0xBB8, 0x0)
    OP_8E(0xFE, 0xB432, 0x0, 0xFA3C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x55D2, 0x0, 0xFA3C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x58CA, 0x0, 0x70B2, 0xBB8, 0x0)
    Jump("Function_6_117A")

    label("loc_11D6")

    Return()

    # Function_6_117A end

    def Function_7_11D7(): pass

    label("Function_7_11D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1233")
    OP_8E(0xFE, 0x515E, 0x0, 0xFDB6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB75C, 0x0, 0xFEA6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x515E, 0x0, 0xFDB6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x50AA, 0x0, 0x6EA0, 0x7D0, 0x0)
    Jump("Function_7_11D7")

    label("loc_1233")

    Return()

    # Function_7_11D7 end

    def Function_8_1234(): pass

    label("Function_8_1234")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1257")
    OP_8D(0xFE, 36860, 76920, 34270, 72430, 3500)
    Jump("Function_8_1234")

    label("loc_1257")

    Return()

    # Function_8_1234 end

    def Function_9_1258(): pass

    label("Function_9_1258")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_127B")
    OP_8D(0xFE, 37000, 71270, 33980, 67090, 3500)
    Jump("Function_9_1258")

    label("loc_127B")

    Return()

    # Function_9_1258 end

    def Function_10_127C(): pass

    label("Function_10_127C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_129F")
    OP_8D(0xFE, 39610, 24560, 36410, 15240, 3500)
    Jump("Function_10_127C")

    label("loc_129F")

    Return()

    # Function_10_127C end

    def Function_11_12A0(): pass

    label("Function_11_12A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12FC")
    OP_8E(0xFE, 0xACEE, 0x0, 0x7418, 0x9C4, 0x0)
    OP_8E(0xFE, 0x5C12, 0x0, 0x742C, 0x9C4, 0x0)
    OP_8E(0xFE, 0x5C8A, 0x0, 0xF384, 0x9C4, 0x0)
    OP_8E(0xFE, 0xACF8, 0x0, 0xF2BC, 0x9C4, 0x0)
    Jump("Function_11_12A0")

    label("loc_12FC")

    Return()

    # Function_11_12A0 end

    def Function_12_12FD(): pass

    label("Function_12_12FD")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F6")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "刚刚才结束\x01",
            "今天体育课的教学。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "学生不仅要学习，\x01",
            "身心也应该得到健全的发展才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "至少在我的课上\x01",
            "我要好好地锻炼他们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14BD")

    label("loc_13F6")


    ChrTalk(
        0xFE,
        (
            "学生不仅要学习，\x01",
            "身心也应该得到健全的发展才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "至少在我的课上\x01",
            "我要好好地锻炼他们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14BD")

    TalkEnd(0xB)
    Return()

    # Function_12_12FD end

    def Function_13_14C1(): pass

    label("Function_13_14C1")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_15FF")
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

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1528")
    OP_0D()
    OP_A9(0x2E)
    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_1528")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1539")
    TalkEnd(0xC)
    Return()

    label("loc_1539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DC")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "欢迎！欢迎！\x01",
            "欢～迎呀！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "来吧，那边的姐姐们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "来点很美味很美味的\x01",
            "爆米花怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FC")

    label("loc_15DC")


    ChrTalk(
        0xFE,
        (
            "欢迎！欢迎！\x01",
            "欢～迎呀！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FC")

    Jump("loc_178A")

    label("loc_15FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1651")

    ChrTalk(
        0xFE,
        "好，准备稳妥了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "接下来就等明天了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_178A")

    label("loc_1651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_178A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1726")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "呵呵呵，\x01",
            "今年又到了这个时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比起上课，\x01",
            "还是学园祭更能提起干劲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嘿，精神百倍了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_178A")

    label("loc_1726")


    ChrTalk(
        0xFE,
        (
            "比起上课，\x01",
            "还是学园祭更能提起干劲啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178A")

    TalkEnd(0xC)
    Return()

    # Function_13_14C1 end

    def Function_14_178E(): pass

    label("Function_14_178E")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1907")
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

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F5")
    OP_0D()
    OP_A9(0x2F)
    OP_56(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_17F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1806")
    TalkEnd(0xD)
    Return()

    label("loc_1806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B8")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "唔，那个……\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "要不要买些点心呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这、这个是\x01",
            "很好吃的点心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1904")

    label("loc_18B8")


    ChrTalk(
        0xFE,
        (
            "呼，还是不习惯，\x01",
            "怎么说都有点害羞……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1904")

    Jump("loc_197D")

    label("loc_1907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_197D")

    ChrTalk(
        0xFE,
        "呼，总算准备完毕了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明天就和社团的各位\x01",
            "轮流来担当店员吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197D")

    TalkEnd(0xD)
    Return()

    # Function_14_178E end

    def Function_15_1981(): pass

    label("Function_15_1981")

    TalkBegin(0xE)
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

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19E1")
    OP_0D()
    OP_A9(0x2F)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_19E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19F2")
    TalkEnd(0xE)
    Return()

    label("loc_19F2")


    ChrTalk(
        0xE,
        "想吃美味的点心吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "各种各样的味道都有哦。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_15_1981 end

    def Function_16_1AB5(): pass

    label("Function_16_1AB5")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_1C27")
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

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B1C")
    OP_0D()
    OP_A9(0x2E)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_1B1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B2D")
    TalkEnd(0xF)
    Return()

    label("loc_1B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAA")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "欢迎～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "来一份精挑细选的\x01",
            "美味爆米花怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C24")

    label("loc_1BAA")


    ChrTalk(
        0xFE,
        (
            "作为材料的玉米\x01",
            "是从洛连特运过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那边的蔬菜很美味。\x02",
    )

    CloseMessageWindow()

    label("loc_1C24")

    Jump("loc_1D74")

    label("loc_1C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1CA0")

    ChrTalk(
        0xFE,
        "嗯，器具和材料都准备好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "制作方面我也练习过了，\x01",
            "你们放心吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D74")

    label("loc_1CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D37")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "好，就选这里吧。\x01",
            "摆摊的地点是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们弓道部\x01",
            "决定摆摊卖爆米花。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D74")

    label("loc_1D37")


    ChrTalk(
        0xFE,
        (
            "罗迪只有在这个时候\x01",
            "才会干劲十足呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D74")

    TalkEnd(0xF)
    Return()

    # Function_16_1AB5 end

    def Function_17_1D78(): pass

    label("Function_17_1D78")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1E3A")
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

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DDF")
    OP_0D()
    OP_A9(0x2C)
    OP_56(0x0)
    TalkEnd(0x10)
    Return()

    label("loc_1DDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF0")
    TalkEnd(0x10)
    Return()

    label("loc_1DF0")


    ChrTalk(
        0xFE,
        (
            "啊，是前辈你们呀。\x01",
            "来一个冰淇淋怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嘿嘿，很好吃的哦㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_1E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1F79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F31")
    OP_A2(0x5)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "啊，前辈。\x01",
            "明天就要正式表演了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过明天我不能去看\x01",
            "前辈扮成苍骑士的样子………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "一想到这个就觉得可惜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F是、是吗……\x01",
            "真是谢谢你的支持了，莉秋尔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F76")

    label("loc_1F31")


    ChrTalk(
        0xFE,
        (
            "科洛丝前辈和艾丝蒂尔，\x01",
            "你们都好棒啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊呀……\x02",
    )

    CloseMessageWindow()

    label("loc_1F76")

    Jump("loc_2294")

    label("loc_1F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2294")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224F")
    OP_A2(0x5)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "前辈！\x01",
            "你回来啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "我们已经开始准备社团的摊位了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F对不起，莉秋尔。\x01",
            "我都帮不上忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没关系，\x01",
            "前辈一直在忙舞台剧嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，舞台剧的演员人选\x01",
            "定下来了没有呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#041F呵呵，那个就不用担心了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……？？\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "难不成就是你身边的这两位？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#008F啊，感觉好紧张呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F嗯……\x02",
    )

    CloseMessageWindow()
    OP_63(0x10)

    ChrTalk(
        0xFE,
        "果然如此！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(
        0xFE,
        (
            "的确是非常合适呀，\x01",
            "真不愧是前辈选中的演员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "能找到合适的演员，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，我也要演出舞台剧，\x01",
            "大家一起加油吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，请多指教了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_224F")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "我也要演出舞台剧。\x01",
            "大家一起加油吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2294")

    TalkEnd(0x10)
    Return()

    # Function_17_1D78 end

    def Function_18_2298(): pass

    label("Function_18_2298")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_23B4")
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

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22FF")
    OP_0D()
    OP_A9(0x2C)
    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_22FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2310")
    TalkEnd(0x11)
    Return()

    label("loc_2310")


    ChrTalk(
        0xFE,
        "怎么样～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这是击剑部的\x01",
            "冰淇淋店哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "会出乎你意料地美味哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_23B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_24F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B5")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "啊，科洛丝。\x01",
            "你最近好像很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F巴托姆，不好意思。\x01",
            "最近我连社团活动都没空来参加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，\x01",
            "因为你那边也有很多事嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不要太介意了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_24B5")


    ChrTalk(
        0xFE,
        (
            "科洛丝，有时间的话，\x01",
            "请来出席一下社团练习吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F5")

    TalkEnd(0x11)
    Return()

    # Function_18_2298 end

    def Function_19_24F9(): pass

    label("Function_19_24F9")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_257D")

    ChrTalk(
        0xFE,
        (
            "虽然今天没有课，\x01",
            "不过我是来教室自习的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "趁大家休息的时候学习\x01",
            "才是缩短差距的好机会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_257D")

    TalkEnd(0x12)
    Return()

    # Function_19_24F9 end

    def Function_20_2581(): pass

    label("Function_20_2581")

    TalkBegin(0x13)
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

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E1")
    OP_0D()
    OP_A9(0x2D)
    OP_56(0x0)
    TalkEnd(0x13)
    Return()

    label("loc_25E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25F2")
    TalkEnd(0x13)
    Return()

    label("loc_25F2")


    ChrTalk(
        0xFE,
        (
            "因为我是美术部的，\x01",
            "我想肖像画也能做出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，因为我很擅长烹饪，\x01",
            "所以大家都没意见。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_20_2581 end

    def Function_21_2692(): pass

    label("Function_21_2692")

    TalkBegin(0x14)
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

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F2")
    OP_0D()
    OP_A9(0x2D)
    OP_56(0x0)
    TalkEnd(0x14)
    Return()

    label("loc_26F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2703")
    TalkEnd(0x14)
    Return()

    label("loc_2703")


    ChrTalk(
        0xFE,
        (
            "我很擅长科学和生物实验，\x01",
            "可对烹饪却没什么经验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……不过，\x01",
            "不管学什么要领都是努力再努力。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_21_2692 end

    def Function_22_2790(): pass

    label("Function_22_2790")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_27E7")

    ChrTalk(
        0xFE,
        (
            "差不多应该\x01",
            "修剪一下树丛了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B77")

    label("loc_27E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2859")

    ChrTalk(
        0xFE,
        (
            "辛苦你们了。\x01",
            "总算完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还剩下一点，\x01",
            "我待会儿再收拾吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B77")

    label("loc_2859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_29F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_2926")

    ChrTalk(
        0xFE,
        "哦，刚才真是感谢啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "下面只剩这里了，\x01",
            "我一个人就足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明天的学园祭，\x01",
            "大家都非常期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F4")

    label("loc_2926")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_29F0")

    ChrTalk(
        0xFE,
        (
            "如果看到没有装饰的地方，\x01",
            "还请告诉我一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要稍微注意一下\x01",
            "应该就可以发现的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 135, 400)

    ChrTalk(
        0xFE,
        (
            "接下来……\x01",
            "首先从这里开始干吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F4")

    label("loc_29F0")

    Call(1, 0)

    label("loc_29F4")

    Jump("loc_2B77")

    label("loc_29F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_2A7D")

    ChrTalk(
        0xFE,
        (
            "每年一到这个时期，\x01",
            "同学们总是准备到很晚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也不得不\x01",
            "巡逻到夜深才能回去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B77")

    label("loc_2A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2ABF")

    ChrTalk(
        0xFE,
        "呀，要出去吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要小心点哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B77")

    label("loc_2ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_2B21")

    ChrTalk(
        0xFE,
        (
            "今天也没有体育课，\x01",
            "现在我正在整理学院的庭园呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B77")

    label("loc_2B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2B77")

    ChrTalk(
        0xFE,
        "啊，你们是来参观的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我对详细情况不是很清楚，\x01",
            "去找接待员问问吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B77")

    TalkEnd(0x15)
    Return()

    # Function_22_2790 end

    def Function_23_2B7B(): pass

    label("Function_23_2B7B")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D0B")
    OP_A2(0x455)

    ChrTalk(
        0xFE,
        (
            "#143F哟，这不是艾丝蒂尔和约修亚嘛。\x02\x03",
            "你们怎么会在这里的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊，奈尔……\x02\x03",
            "连你也来这里玩啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F肯定是因为王立学院\x01",
            "邀请了各界的名人嘛。\x02\x03",
            "奈尔先生是来这里取材的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#141F嗯，差不多啦。\x02\x03",
            "呵呵，\x01",
            "刚才正好有点饿了。\x02\x03",
            "所以就买了点吃的填肚子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D45")

    label("loc_2D0B")


    ChrTalk(
        0xFE,
        (
            "#141F刚才正好有点饿了，\x01",
            "所以就买了点吃的填肚子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D45")

    TalkEnd(0x16)
    Return()

    # Function_23_2B7B end

    def Function_24_2D49(): pass

    label("Function_24_2D49")

    TalkBegin(0x17)

    ChrTalk(
        0x17,
        (
            "#182F呵呵，让人怀念的点心啊……\x02\x03",
            "这种东西到底是在哪儿做出来的呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    # Function_24_2D49 end

    def Function_25_2DB8(): pass

    label("Function_25_2DB8")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E99")
    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "#832F哦？怎么了，\x01",
            "这么慌张……\x02\x03",
            "难道发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊、不……\x01",
            "不是什么大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#830F是吗，那就好……\x02\x03",
            "如果有什么事件发生，\x01",
            "一定要立刻告诉我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ED5")

    label("loc_2E99")


    ChrTalk(
        0xFE,
        (
            "#830F如果有什么事件发生，\x01",
            "一定要立刻告诉我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED5")

    TalkEnd(0x18)
    Return()

    # Function_25_2DB8 end

    def Function_26_2ED9(): pass

    label("Function_26_2ED9")

    TalkBegin(0x19)

    ChrTalk(
        0xFE,
        (
            "一到学园祭，\x01",
            "钱就像水一样地流走了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x19)
    Return()

    # Function_26_2ED9 end

    def Function_27_2F2F(): pass

    label("Function_27_2F2F")

    TalkBegin(0x1A)

    ChrTalk(
        0xFE,
        "哎，真是好吃呀。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1A)
    Return()

    # Function_27_2F2F end

    def Function_28_2F55(): pass

    label("Function_28_2F55")

    TalkBegin(0x1B)

    ChrTalk(
        0xFE,
        "爸爸，我想吃这个。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1B)
    Return()

    # Function_28_2F55 end

    def Function_29_2F78(): pass

    label("Function_29_2F78")

    TalkBegin(0x1C)

    ChrTalk(
        0xFE,
        "哎呀，真是好有活力。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "年轻人果然\x01",
            "精力都很充沛啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1C)
    Return()

    # Function_29_2F78 end

    def Function_30_2FCE(): pass

    label("Function_30_2FCE")

    TalkBegin(0x1D)

    ChrTalk(
        0xFE,
        (
            "虽然学园祭也不错，\x01",
            "但我更想看看平时的上课情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "身为母亲的我当然很想知道\x01",
            "自己的孩子是怎么生活的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1D)
    Return()

    # Function_30_2FCE end

    def Function_31_3079(): pass

    label("Function_31_3079")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_30EE")

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "我用零用钱买了一个冰淇淋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "店里的哥哥\x01",
            "还给我多加了点呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_311D")

    label("loc_30EE")


    ChrTalk(
        0xFE,
        (
            "嗯，好香呀……\x01",
            "肚子饿扁扁了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_311D")

    TalkEnd(0x1E)
    Return()

    # Function_31_3079 end

    def Function_32_3121(): pass

    label("Function_32_3121")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_31B2")

    ChrTalk(
        0xFE,
        (
            "最近这里的\x01",
            "入学考试好像很难啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过真羡慕那些学生\x01",
            "能在这种地方学习。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31E6")

    label("loc_31B2")


    ChrTalk(
        0xFE,
        (
            "嘿，这就是学院啊……\x01",
            "真是好大啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E6")

    TalkEnd(0x1F)
    Return()

    # Function_32_3121 end

    def Function_33_31EA(): pass

    label("Function_33_31EA")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_325E")

    ChrTalk(
        0xFE,
        "舞台剧可是一定不能错过啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在我还是学生的时候，\x01",
            "就已经是传统惯例呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BC")

    label("loc_325E")


    ChrTalk(
        0xFE,
        (
            "我好久没来\x01",
            "拜访母校了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是怀念呀……\x02",
    )

    CloseMessageWindow()

    label("loc_32BC")

    TalkEnd(0x20)
    Return()

    # Function_33_31EA end

    def Function_34_32C0(): pass

    label("Function_34_32C0")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3318")

    ChrTalk(
        0xFE,
        (
            "这里有舞台剧演出吧。\x01",
            "快点开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3336")

    label("loc_3318")


    ChrTalk(
        0xFE,
        "从哪儿开始玩好呢。\x02",
    )

    CloseMessageWindow()

    label("loc_3336")

    TalkEnd(0x21)
    Return()

    # Function_34_32C0 end

    def Function_35_333A(): pass

    label("Function_35_333A")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3389")

    ChrTalk(
        0xFE,
        (
            "今年真的能\x01",
            "看到传说中的公主吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A7")

    label("loc_3389")


    ChrTalk(
        0xFE,
        (
            "我们可是每年\x01",
            "都会来这里玩的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33A7")

    TalkEnd(0x22)
    Return()

    # Function_35_333A end

    def Function_36_33AB(): pass

    label("Function_36_33AB")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_33F9")

    ChrTalk(
        0xFE,
        (
            "展示很有趣，\x01",
            "舞台剧也很值得期待呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_342A")

    label("loc_33F9")


    ChrTalk(
        0xFE,
        (
            "哎，\x01",
            "有好多各种各样的摊子啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_342A")

    TalkEnd(0x23)
    Return()

    # Function_36_33AB end

    def Function_37_342E(): pass

    label("Function_37_342E")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_346F")

    ChrTalk(
        0xFE,
        (
            "刚刚才吃了一个，\x01",
            "又想再吃一个了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_349C")

    label("loc_346F")


    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "这里好像是点心店。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_349C")

    TalkEnd(0x24)
    Return()

    # Function_37_342E end

    def Function_38_34A0(): pass

    label("Function_38_34A0")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_351B")

    ChrTalk(
        0xFE,
        "这里真是个恬静的场所。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这里学习\x01",
            "想必进步一定很快吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354D")

    label("loc_351B")


    ChrTalk(
        0xFE,
        "孙女的教室在哪里呢……\x02",
    )

    CloseMessageWindow()

    label("loc_354D")

    TalkEnd(0x25)
    Return()

    # Function_38_34A0 end

    def Function_39_3551(): pass

    label("Function_39_3551")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_35C6")

    ChrTalk(
        0xFE,
        (
            "这个店是由\x01",
            "击剑部来主办的呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "味道十分好，\x01",
            "真是吓我一跳。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35F1")

    label("loc_35C6")


    ChrTalk(
        0xFE,
        "哎呀，真便宜呀。\x02",
    )

    CloseMessageWindow()

    label("loc_35F1")

    TalkEnd(0x26)
    Return()

    # Function_39_3551 end

    def Function_40_35F5(): pass

    label("Function_40_35F5")

    TalkBegin(0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3640")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "稀里糊涂地又转回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_368A")

    label("loc_3640")


    ChrTalk(
        0xFE,
        (
            "呼，先喘口气，\x01",
            "再接着逛吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_368A")

    TalkEnd(0x27)
    Return()

    # Function_40_35F5 end

    def Function_41_368E(): pass

    label("Function_41_368E")

    TalkBegin(0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_36B5")

    ChrTalk(
        0xFE,
        "哎呀，累死了累死了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3728")

    label("loc_36B5")


    ChrTalk(
        0xFE,
        "我是被女儿硬拉来的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "学园祭什么的我还是第一次参加。\x02",
    )

    CloseMessageWindow()

    label("loc_3728")

    TalkEnd(0x28)
    Return()

    # Function_41_368E end

    def Function_42_372C(): pass

    label("Function_42_372C")

    TalkBegin(0x29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3794")

    ChrTalk(
        0xFE,
        (
            "我也想进\x01",
            "这个学院学习呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在开始拼命学习的话，\x01",
            "能通过入学考试吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37D9")

    label("loc_3794")


    ChrTalk(
        0xFE,
        (
            "以前就听说过，\x01",
            "这个学校环境真不错啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37D9")

    TalkEnd(0x29)
    Return()

    # Function_42_372C end

    def Function_43_37DD(): pass

    label("Function_43_37DD")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_381E")

    ChrTalk(
        0xFE,
        "呼，稍微有点走累了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_384F")

    label("loc_381E")


    ChrTalk(
        0xFE,
        (
            "连露天茶座也有，\x01",
            "真不错啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_384F")

    TalkEnd(0x2A)
    Return()

    # Function_43_37DD end

    def Function_44_3853(): pass

    label("Function_44_3853")

    TalkBegin(0x2B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_38D7")

    ChrTalk(
        0xFE,
        (
            "……刚才有个\x01",
            "黑发的哥哥跑过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那边是不是\x01",
            "有什么有趣的事呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F9")

    label("loc_38D7")


    ChrTalk(
        0xFE,
        "我是来找姐姐的。\x02",
    )

    CloseMessageWindow()

    label("loc_38F9")

    TalkEnd(0x2B)
    Return()

    # Function_44_3853 end

    def Function_45_38FD(): pass

    label("Function_45_38FD")

    TalkBegin(0x2C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3947")

    ChrTalk(
        0xFE,
        (
            "下午开始有演出……\x01",
            "那真让人期待呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3992")

    label("loc_3947")


    ChrTalk(
        0xFE,
        (
            "好漂亮的建筑物啊，\x01",
            "真不愧是杰尼丝王立学院。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3992")

    TalkEnd(0x2C)
    Return()

    # Function_45_38FD end

    def Function_46_3996(): pass

    label("Function_46_3996")

    TalkBegin(0x2D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3A31")

    ChrTalk(
        0xFE,
        (
            "#670F我也是在这个宿舍\x01",
            "度过自己的学生时代的。\x02\x03",
            "#670F当时有不少出现幽灵之类的传闻哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C8E")

    label("loc_3A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C0B")
    OP_A2(0xE)

    ChrTalk(
        0x105,
        "#044F啊，是基尔巴特前辈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#670F是科洛丝你们啊……\x01",
            "准备已经好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，好了。\x01",
            "就等着开始演出了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#670F是吗，那我真是期待啊。\x02\x03",
            "#673F真是好久没回来了，\x01",
            "还是母校好啊。\x02\x03",
            "在这里能回忆起\x01",
            "学生时代的各种往事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C8E")

    label("loc_3C0B")


    ChrTalk(
        0xFE,
        (
            "#673F真是好久没回来了，\x01",
            "还是母校好啊。\x02\x03",
            "在这里能回忆起\x01",
            "学生时代的各种往事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C8E")

    TalkEnd(0x2D)
    Return()

    # Function_46_3996 end

    def Function_47_3C92(): pass

    label("Function_47_3C92")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(61060, 0, 55000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(6110, 0)
    OP_6C(75000, 0)
    OP_6E(262, 0)
    StopSound(0x9470, 0x3D090, 0x0)
    SetChrPos(0x105, 17200, 0, 46000, 90)
    SetChrPos(0x102, 16100, 0, 45600, 90)
    SetChrPos(0x101, 16200, 0, 46800, 90)
    FadeToBright(1000, 0)

    def lambda_3D25():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3D25)

    def lambda_3D35():
        OP_6D(15540, 0, 46430, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3D35)
    Sleep(2000)
    StopSound(0x9470, 0x14C08, 0x1F40)

    def lambda_3D5F():
        OP_6B(2800, 8000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_3D5F)

    def lambda_3D6F():
        OP_67(0, 9500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3D6F)
    Sleep(8000)

    ChrTalk(
        0x101,
        (
            "#501F啊～这里就是王立学院啊。\x02\x03",
            "该怎么说好呢……\x01",
            "真是个充满祥和气息的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P而且这里也很安静，\x01",
            "在这种环境下念书是再好不过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 270, 400)

    ChrTalk(
        0x105,
        (
            "#045F呵呵，因为学生们现在还在上课。\x02\x03",
            "不过，再过一会儿\x01",
            "整个校园就会热闹起来了。\x02\x03",
            "毕竟学园祭也马上就要到了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 0)
    Sleep(100)
    TurnDirection(0x102, 0x105, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#019F#1P是吗。\x01",
            "大家都要忙着准备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F是的。\x02\x03",
            "本来想把你们介绍给学生会长的，\x01",
            "不过她现在应该还在上课……\x02\x03",
            "就先带你们到校长室一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F校长室？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯，就是王立学院的负责人\x01",
            "科林兹校长的办公室。\x02\x03",
            "在主楼第一层的最右边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P那我们就先去\x01",
            "和你们的校长打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3D, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_47_3C92 end

    def Function_48_40A9(): pass

    label("Function_48_40A9")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(16440, 0, 46820, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, 37340, 0, 73890, 225)
    SetChrPos(0x102, 38420, 0, 73100, 225)
    SetChrPos(0x105, 37160, 0, 72790, 225)
    SetChrPos(0x8, 35910, 0, 71960, 225)
    SetChrPos(0x9, 36980, 0, 71630, 225)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x1D, 0x80)
    OP_4A(0x1E, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x20, 0)
    OP_4A(0x21, 0)
    OP_4A(0x22, 0)
    OP_4A(0x23, 0)
    OP_4A(0x24, 0)
    OP_4A(0x25, 0)
    OP_4A(0x26, 0)
    OP_4A(0x19, 0)
    OP_4A(0x1A, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x2B, 0)
    OP_4A(0x2C, 0)
    SetChrPos(0x1E, 11300, 0, 46800, 90)
    SetChrPos(0x21, 11300, 0, 45500, 90)
    SetChrPos(0x20, 10300, 0, 46800, 90)
    SetChrPos(0x1F, 10300, 0, 45500, 90)
    SetChrPos(0x22, 9300, 0, 46800, 90)
    SetChrPos(0x23, 9300, 0, 45500, 90)
    SetChrPos(0x24, 8300, 0, 46800, 90)
    SetChrPos(0x25, 8300, 0, 45500, 90)
    SetChrPos(0x26, 7300, 0, 46800, 90)
    SetChrPos(0x19, 7300, 0, 45500, 90)
    SetChrPos(0x1A, 6300, 0, 46800, 90)
    SetChrPos(0x1B, 6300, 0, 45500, 90)
    SetChrPos(0x1C, 5300, 0, 46800, 90)
    SetChrPos(0x2B, 5300, 0, 45500, 90)
    SetChrPos(0x2C, 4300, 0, 46800, 90)
    OP_4A(0xC, 0)
    OP_4A(0xD, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 14270, 0, 44100, 0)
    OP_72(0x21, 0x20)
    OP_6F(0x21, 0)
    OP_70(0x21, 0x3C)
    OP_73(0x21)
    OP_71(0x21, 0x20)

    def lambda_42C6():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_42C6)

    def lambda_42E1():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0x1130, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_42E1)
    Sleep(150)

    def lambda_4301():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0xA28, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4301)
    Sleep(100)

    def lambda_4321():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4321)

    def lambda_433C():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0x960, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_433C)

    def lambda_4357():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_4357)
    Sleep(50)
    Sleep(150)

    def lambda_437C():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0x960, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_437C)

    def lambda_4397():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0xD48, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4397)

    def lambda_43B2():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0x960, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_43B2)
    Sleep(50)
    Sleep(100)

    def lambda_43D7():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_43D7)

    def lambda_43F2():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_43F2)
    Sleep(150)

    def lambda_4412():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0x1068, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4412)

    def lambda_442D():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0xC80, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_442D)
    Sleep(150)

    def lambda_444D():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0x960, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_444D)

    def lambda_4468():
        OP_8E(0xFE, 0xA99C, 0xFFFFFE0C, 0xB310, 0xD48, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_4468)
    Sleep(900)

    def lambda_4488():
        OP_6D(37180, 0, 72820, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4488)
    OP_6C(45000, 4000)

    ChrTalk(
        0x101,
        (
            "#004F#1P哇～……\x01",
            "这么多客人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P真不愧是享有盛名的\x01",
            "杰尼丝王立学院。\x02\x03",
            "真不敢相信这只是学院级的活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F#1P呵呵，今年的客人\x01",
            "似乎比往年多很多呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        (
            "#640F#3P好极了，终于开始了啊。\x02\x03",
            "汉斯，快点走吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        "#730F#4P好。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(
        0x9,
        (
            "#730F#4P我们就在学生会室，\x01",
            "有什么事的话就过来找我们吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4667():

        label("loc_4667")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4667")

    QueueWorkItem2(0x101, 1, lambda_4667)

    def lambda_4678():

        label("loc_4678")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4678")

    QueueWorkItem2(0x102, 1, lambda_4678)

    def lambda_4689():

        label("loc_4689")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4689")

    QueueWorkItem2(0x105, 1, lambda_4689)

    ChrTalk(
        0x102,
        (
            "#010F明白。\x01",
            "你们两个要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)

    def lambda_46CC():
        OP_8E(0xFE, 0x85DE, 0x0, 0xFCB2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_46CC)
    Sleep(500)
    OP_8C(0x9, 135, 400)
    OP_8E(0x9, 0x85DE, 0x0, 0xFCB2, 0x1388, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)

    def lambda_471D():
        OP_6D(37840, 0, 73580, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_471D)
    OP_8C(0x105, 45, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x105,
        (
            "#041F艾丝蒂尔、约修亚，\x01",
            "我们就开始参观学园祭吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，走吧！\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1E, 39850, -2000, 45950, 270)
    SetChrPos(0x1F, 48940, 0, 27010, 270)
    SetChrPos(0x20, 21080, 0, 31060, 0)
    SetChrPos(0x21, 30350, 0, 64730, 225)
    SetChrPos(0x22, 31080, 0, 64010, 324)
    SetChrPos(0x23, 43200, -750, 48790, 270)
    SetChrPos(0x24, 30480, -2000, 34130, 315)
    SetChrPos(0x25, 25790, -1750, 43460, 90)
    SetChrPos(0x26, 39090, -2000, 50780, 45)
    SetChrPos(0x19, 29200, -2000, 51000, 315)
    SetChrPos(0x1A, 29500, -2000, 52500, 270)
    SetChrPos(0x1B, 29700, -2000, 51300, 270)
    SetChrPos(0x1C, 39400, -2000, 39700, 180)
    SetChrPos(0x2B, 37080, 0, 18890, 0)
    SetChrPos(0x2C, 45250, 0, 45990, 270)
    SetChrPos(0xC, 39500, -2000, 36400, 315)
    SetChrPos(0xD, 28300, -2000, 36260, 90)
    OP_4B(0xC, 0)
    OP_4B(0xD, 0)
    OP_44(0x1E, 0x1)
    OP_44(0x1F, 0x1)
    OP_44(0x20, 0x1)
    OP_44(0x21, 0x1)
    OP_44(0x22, 0x1)
    OP_44(0x23, 0x1)
    OP_44(0x24, 0x1)
    OP_44(0x25, 0x1)
    OP_44(0x26, 0x1)
    OP_44(0x19, 0x1)
    OP_44(0x1A, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x1C, 0x1)
    OP_44(0x2B, 0x1)
    OP_44(0x2C, 0x1)
    OP_4B(0x1E, 0)
    OP_4B(0x1F, 0)
    OP_4B(0x20, 0)
    OP_4B(0x21, 0)
    OP_4B(0x22, 0)
    OP_4B(0x23, 0)
    OP_4B(0x24, 0)
    OP_4B(0x25, 0)
    OP_4B(0x26, 0)
    OP_4B(0x19, 0)
    OP_4B(0x1A, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x2B, 0)
    OP_4B(0x2C, 0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    EventEnd(0x0)
    Return()

    # Function_48_40A9 end

    def Function_49_4973(): pass

    label("Function_49_4973")

    EventBegin(0x0)
    ClearChrFlags(0xA, 0x80)
    OP_6D(39830, 0, 74030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 39550, 0, 73430, 0)
    SetChrPos(0x105, 39540, 0, 74630, 180)
    SetChrPos(0xA, 38790, 6000, 63670, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002F总之……\x01",
            "先去找找约修亚吧。\x02\x03",
            "虽然不知道\x01",
            "那个银发男子是谁……\x02\x03",
            "#003F但不知怎么的，总有种不好的预感。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xA, 400)

    ChrTalk(
        0x105,
        (
            "#047F先等一下。\x02\x03",
            "#042F……基库！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4ACD():

        label("loc_4ACD")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4ACD")

    QueueWorkItem2(0x101, 1, lambda_4ACD)

    def lambda_4ADE():

        label("loc_4ADE")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4ADE")

    QueueWorkItem2(0x105, 1, lambda_4ADE)

    def lambda_4AEF():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4AEF)
    OP_22(0x8C, 0x0, 0x64)
    OP_92(0xA, 0x136, 0x1388, 0x2710, 0x0)
    OP_92(0xA, 0x136, 0xFA0, 0x1F40, 0x0)
    OP_92(0xA, 0x136, 0xBB8, 0x1770, 0x0)
    OP_92(0xA, 0x136, 0x7D0, 0xBB8, 0x0)

    def lambda_4B3C():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_4B3C)
    OP_8F(0xA, 0x96B4, 0x3E8, 0x121D8, 0x5DC, 0x0)
    OP_44(0x105, 0xFF)
    SetChrFlags(0x105, 0x20)

    def lambda_4B67():
        OP_8C(0xFE, 225, 200)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_4B67)

    def lambda_4B75():
        OP_8C(0xFE, 180, 200)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_4B75)
    SetChrChipByIndex(0x105, 19)
    SetChrSubChip(0x105, 2)
    OP_8F(0xA, 0x993E, 0x0, 0x1241C, 0x3E8, 0x0)
    WaitChrThread(0xA, 0x3)
    Sleep(100)
    OP_44(0x101, 0xFF)
    Fade(250)
    SetChrFlags(0xA, 0x80)
    SetChrSubChip(0x105, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xA,
        "#310F啾？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F有事想问你。\x02\x03",
            "你知道\x01",
            "约修亚去哪儿了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#311F啾～☆\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0xA, 0x80)
    SetChrSubChip(0x105, 2)
    OP_0D()

    def lambda_4C40():

        label("loc_4C40")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4C40")

    QueueWorkItem2(0x101, 2, lambda_4C40)

    def lambda_4C51():

        label("loc_4C51")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4C51")

    QueueWorkItem2(0x105, 2, lambda_4C51)

    def lambda_4C62():
        OP_6C(135000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C62)

    def lambda_4C72():
        OP_6D(39670, 0, 71450, 2000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4C72)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_4C8F():
        OP_8E(0xFE, 0x99C0, 0xFA0, 0x1041E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4C8F)
    Sleep(400)

    def lambda_4CAF():
        OP_8E(0xFE, 0x99C0, 0xFA0, 0x1041E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4CAF)
    Sleep(400)
    OP_44(0x101, 0x2)
    OP_44(0x105, 0x2)
    SetChrChipByIndex(0x105, 65535)
    ClearChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 0)

    def lambda_4CE6():
        OP_8E(0xFE, 0xB1EE, 0x1770, 0xEB32, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4CE6)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x1)

    ChrTalk(
        0x101,
        (
            "#004F它还是那么厉害啊～\x02\x03",
            "#004F啊，那个方向是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F嗯……\x01",
            "是主楼后面的旧校舍。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    SetChrFlags(0xA, 0x80)
    OP_28(0x3D, 0x1, 0x1000)
    EventEnd(0x0)
    Return()

    # Function_49_4973 end

    def Function_50_4DBF(): pass

    label("Function_50_4DBF")

    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x10)
    SetChrFlags(0x2C, 0x80)
    EventBegin(0x0)
    OP_6D(17970, 0, 46050, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, 17580, 0, 46020, 90)
    SetChrPos(0x102, 17920, 0, 45160, 90)
    SetChrPos(0x105, 17860, 0, 46810, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 19290, 0, 46470, 270)
    SetChrPos(0x9, 19430, 0, 45420, 270)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#640F……难得来学院一次，\x01",
            "怎么不多留一晚再走呢？\x02\x03",
            "接下来还有\x01",
            "学园祭的庆功宴哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊哈哈……\x01",
            "虽然我也很想参加，不过还是算了。\x02\x03",
            "我们还是新人，\x01",
            "太久不回协会也不大好啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们想在今天把报告完成，\x01",
            "所以不好意思，这就要告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#730F是吗……\x02\x03",
            "#734F约修亚啊，\x01",
            "从今晚起我又孤身一人了。\x02\x03",
            "孤枕而眠太寂寞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F汉斯……\x01",
            "玩笑开过头了吧。\x02\x03",
            "#018F艾丝蒂尔别把他的鬼话当真。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F啊、啊哈哈，是玩笑啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#641F这可是真心话啊，\x01",
            "跟你们在一起就绝不会感到无聊。\x02\x03",
            "有机会的话或者有空的话，\x01",
            "你们一定要再来玩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#730F当然也一定要过夜哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯……谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们一定会再来的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F呵呵……\x01",
            "那我们走吧。\x02\x03",
            "不抓紧的话，\x01",
            "天很快就要黑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#640F你现在要去\x01",
            "玛诺利亚村吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F嗯，我有好多话\x01",
            "想和老师他们说呢……\x02\x03",
            "而且学校也允许我今晚在外留宿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#645F本来热热闹闹的庆功宴，\x01",
            "主角居然一个都不在，\x01",
            "真是太没意思了……\x02\x03",
            "#648F不过，也没办法啦。\x01",
            "我们就自己好好轻松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#732F说起来，特蕾莎院长他们……\x02\x03",
            "带着那么一大笔钱走回去，\x01",
            "不觉得有点危险吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F哦，这个不用担心。\x02\x03",
            "因为担任这次学园祭警卫的\x01",
            "卡露娜姐姐会负责护送他们回去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F而且，这还是校长\x01",
            "委托协会一定要做的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#731F不愧是校长。\x01",
            "处理事情还真是滴水不漏。\x02\x03",
            "#730F……好了，那么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#644F多保重啊。\x01",
            "艾丝蒂尔、约修亚。\x02\x03",
            "以正游击士为目标，\x01",
            "你们两个一定要继续努力哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，看我们的吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F你们也要努力念书哦。\x02",
    )

    CloseMessageWindow()
    OP_28(0x1C, 0x4, 0x40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/R2301   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_50_4DBF end

    def Function_51_5621(): pass

    label("Function_51_5621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5683")
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
    Jump("loc_604E")

    label("loc_5683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_56F2")
    EventBegin(0x2)

    ChrTalk(
        0x136,
        (
            "#040F这里是我就读的杰尼丝王立学院。\x01",
            "　\x01",
            "下次我再带你们好好参观吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_5971")

    label("loc_56F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58A2")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(13480, 0, 45900, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, 12200, 0, 46050, 90)
    SetChrPos(0x102, 11100, 0, 45460, 90)
    SetChrPos(0x136, 11200, 0, 46920, 90)
    Sleep(800)

    ChrTalk(
        0x101,
        "#000F哎，这里是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F是我就读的杰尼丝王立学院。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        (
            "#004F哎～是这样啊……\x02\x03",
            "真是好大啊。\x01",
            "你就在这种地方学习吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(
        0x136,
        (
            "#043F是啊，如果有时间的话\x01",
            "真想带你们好好参观一下呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F不过现在必须得赶快\x01",
            "回卢安找克拉姆才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F是、是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)
    OP_A2(0x451)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_5971")

    label("loc_58A2")

    EventBegin(0x2)

    ChrTalk(
        0x101,
        (
            "#000F哎，\x01",
            "这里就是科洛丝就读的学校吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F嗯，是啊。\x02\x03",
            "#043F如果有时间的话\x01",
            "真想带你们好好参观一下呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F不过现在必须得赶快\x01",
            "回卢安找克拉姆才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F是、是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)
    EventEnd(0x1)

    label("loc_5971")

    Jump("loc_604E")

    label("loc_5974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_END)), "loc_5BDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_59D8")
    EventBegin(0x2)

    ChrTalk(
        0x102,
        (
            "#010F这里就是科洛丝就读的学校吧。\x01",
            "　\x02\x03",
            "我们还是赶快去玛诺利亚村吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_5BD7")

    label("loc_59D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_5A19")
    EventBegin(0x2)

    ChrTalk(
        0x101,
        (
            "#004F这里是王立学院……\x01",
            "真是好大啊。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_5BD7")

    label("loc_5A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BA0")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(13480, 0, 45900, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, 12200, 0, 46050, 90)
    SetChrPos(0x102, 11100, 0, 45460, 90)
    SetChrPos(0x136, 11200, 0, 46920, 90)
    Sleep(800)

    ChrTalk(
        0x136,
        (
            "#040F这里是我就读的杰尼丝王立学院。\x01",
            "　\x02\x03",
            "不过因为现在正在放假，\x01",
            "不能带你们参观校园……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F哎，就是这里啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F这么大啊。\x01",
            "就在这种地方学习吗？\x02\x03",
            "和主日学校果然不一样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    OP_A2(0x451)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_5BD7")

    label("loc_5BA0")

    EventBegin(0x2)

    ChrTalk(
        0x101,
        (
            "#004F这里是王立学院……\x01",
            "真是好大啊。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)

    label("loc_5BD7")

    Jump("loc_604E")

    label("loc_5BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_5E8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_5C58")
    EventBegin(0x2)

    ChrTalk(
        0x102,
        (
            "#010F这里就是科洛丝就读的学校吧。\x01",
            "　\x02\x03",
            "我们还是赶快去孤儿院调查吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_5E8B")

    label("loc_5C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_5C99")
    EventBegin(0x2)

    ChrTalk(
        0x101,
        (
            "#004F这里是王立学院……\x01",
            "真是好大啊。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_5E8B")

    label("loc_5C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DFE")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(13480, 0, 45900, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, 12200, 0, 46050, 90)
    SetChrPos(0x102, 11100, 0, 45460, 90)
    Sleep(800)

    ChrTalk(
        0x101,
        "#000F……这里是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F有好多建筑设施呢。\x02\x03",
            "难道说这里就是\x01",
            "科洛丝就读的杰尼丝王立学院？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F这么大啊。\x01",
            "就在这种地方学习吗？\x02\x03",
            "和主日学校果然不一样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    OP_A2(0x451)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_5E8B")

    label("loc_5DFE")

    EventBegin(0x2)

    ChrTalk(
        0x101,
        "#000F哎，这里是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是科洛丝就读的学校呢。\x02\x03",
            "我们还是赶快去孤儿院调查吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    EventEnd(0x1)

    label("loc_5E8B")

    Jump("loc_604E")

    label("loc_5E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_604E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6017")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(13480, 0, 45900, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, 12200, 0, 46050, 90)
    SetChrPos(0x102, 11100, 0, 45460, 90)
    SetChrPos(0x136, 11200, 0, 46920, 90)
    Sleep(800)

    ChrTalk(
        0x136,
        (
            "#040F这里是我就读的杰尼丝王立学院。\x01",
            "　\x02\x03",
            "不过因为现在正在放假，\x01",
            "不能带你们参观校园……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F哎，这里是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F这么大啊。\x01",
            "在这种地方学习吗？\x02\x03",
            "和主日学校果然不一样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    OP_A2(0x451)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_604E")

    label("loc_6017")

    EventBegin(0x2)

    ChrTalk(
        0x101,
        (
            "#004F这里是王立学院……\x01",
            "真是好大啊。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)

    label("loc_604E")

    Return()

    # Function_51_5621 end

    def Function_52_604F(): pass

    label("Function_52_604F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60FA")
    EventBegin(0x1)
    OP_8B(0x101, 0x3124, 0xB39C, 0x190)

    ChrTalk(
        0x101,
        (
            "#002F啊，现在不能出去……\x02\x03",
            "……要赶快去北边的旧校舍。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#042F嗯，赶快走吧。\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_6329")

    label("loc_60FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6329")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6284")
    OP_A2(0xF)
    OP_8B(0x101, 0x3124, 0xB39C, 0x190)

    ChrTalk(
        0x101,
        (
            "#000F啊，这里是校门……\x02\x03",
            "门还打开着，\x01",
            "是不是还会有客人来呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F可能是吧。\x02\x03",
            "到舞台剧开始还有一些时间呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#040F嗯，专门为了看舞台剧\x01",
            "而来的人也有不少呢。\x02\x03",
            "那我们继续参观吧。\x01",
            "要尽情地玩也只有趁现在了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#001F嗯，走吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_630E")

    label("loc_6284")

    OP_8B(0x101, 0x3124, 0xB39C, 0x190)

    ChrTalk(
        0x101,
        "#000F现在不能出去……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F我们还是回去吧。\x02\x03",
            "趁还有空的时候\x01",
            "好好享受一下学园祭吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_630E")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_6329")

    Return()

    # Function_52_604F end

    def Function_53_632A(): pass

    label("Function_53_632A")

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

    # Function_53_632A end

    def Function_54_637E(): pass

    label("Function_54_637E")

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

    # Function_54_637E end

    def Function_55_63D2(): pass

    label("Function_55_63D2")

    EventBegin(0x2)
    OP_A3(0x451)

    ChrTalk(
        0x101,
        (
            "#004F就像第一次来一样呢……\x01",
            "真是好大啊。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x2)
    Return()

    # Function_55_63D2 end

    def Function_56_6410(): pass

    label("Function_56_6410")

    SetPlaceName(0x5F) # 王立学院　女子宿舍
    Return()

    # Function_56_6410 end

    def Function_57_6414(): pass

    label("Function_57_6414")

    SetPlaceName(0x5C) # 王立学院　女子宿舍
    Return()

    # Function_57_6414 end

    def Function_58_6418(): pass

    label("Function_58_6418")

    SetPlaceName(0x5D) # 王立学院　女子宿舍
    Return()

    # Function_58_6418 end

    def Function_59_641C(): pass

    label("Function_59_641C")

    SetPlaceName(0x6C) # 王立学院　女子宿舍
    Return()

    # Function_59_641C end

    def Function_60_6420(): pass

    label("Function_60_6420")

    SetPlaceName(0x6D) # 王立学院　女子宿舍
    Return()

    # Function_60_6420 end

    SaveToFile()

Try(main)
