from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4251   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4251.x',
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
        '理查德上校',                           # 9
        '凯诺娜上尉',                           # 10
        '杜南公爵',                             # 11
        '管家菲利普',                           # 12
        '克劳斯市长',                           # 13
        '科林兹校长',                           # 14
        '玛多克工房长',                         # 15
        '莉拉',                                 # 16
        '梅贝尔市长',                           # 17
        '索蕾拉',                               # 18
        '妮舒',                                 # 19
        '布莉姆',                               # 20
        '艾科尔',                               # 21
        '\u3000',                               # 22
        '\u3000',                               # 23
        '\u3000',                               # 24
        '\u3000',                               # 25
        '\u3000',                               # 26
        '\u3000',                               # 27
        '\u3000',                               # 28
        '\u3000',                               # 29
        '\u3000',                               # 30
        '\u3000',                               # 31
        '\u3000',                               # 32
        '\u3000',                               # 33
        '\u3000',                               # 34
        '\u3000',                               # 35
        '\u3000',                               # 36
        '\u3000',                               # 37
        '\u3000',                               # 38
        '\u3000',                               # 39
        '\u3000',                               # 40
        '\u3000',                               # 41
        '\u3000',                               # 42
        '\u3000',                               # 43
        '\u3000',                               # 44
        '\u3000',                               # 45
        '\u3000',                               # 46
        '\u3000',                               # 47
        '\u3000',                               # 48
        '\u3000',                               # 49
        '\u3000',                               # 50
        '\u3000',                               # 51
        '\u3000',                               # 52
        '\u3000',                               # 53
        '\u3000',                               # 54
        '\u3000',                               # 55
        '\u3000',                               # 56
        '\u3000',                               # 57
        '\u3000',                               # 58
        '\u3000',                               # 59
        '\u3000',                               # 60
        '\u3000',                               # 61
        '\u3000',                               # 62
        '\u3000',                               # 63
        '\u3000',                               # 64
        '\u3000',                               # 65
        '\u3000',                               # 66
        '\u3000',                               # 67
        '\u3000',                               # 68
        '\u3000',                               # 69
        '\u3000',                               # 70
        '\u3000',                               # 71
        '\u3000',                               # 72
        '\u3000',                               # 73
        '\u3000',                               # 74
        '\u3000',                               # 75
        '\u3000',                               # 76
        '\u3000',                               # 77
        '\u3000',                               # 78
        '\u3000',                               # 79
        '\u3000',                               # 80
        '\u3000',                               # 81
        '\u3000',                               # 82
        '\u3000',                               # 83
        '\u3000',                               # 84
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
        'ED6_DT07/CH02030 ._CH',             # 00
        'ED6_DT07/CH02100 ._CH',             # 01
        'ED6_DT07/CH02140 ._CH',             # 02
        'ED6_DT07/CH02470 ._CH',             # 03
        'ED6_DT07/CH02353 ._CH',             # 04
        'ED6_DT07/CH02603 ._CH',             # 05
        'ED6_DT07/CH02623 ._CH',             # 06
        'ED6_DT07/CH02370 ._CH',             # 07
        'ED6_DT07/CH02363 ._CH',             # 08
        'ED6_DT07/CH02460 ._CH',             # 09
        'ED6_DT07/CH02230 ._CH',             # 0A
        'ED6_DT07/CH02240 ._CH',             # 0B
        'ED6_DT07/CH01350 ._CH',             # 0C
        'ED6_DT07/CH02033 ._CH',             # 0D
        'ED6_DT07/CH02103 ._CH',             # 0E
        'ED6_DT06/CH20088 ._CH',             # 0F
        'ED6_DT07/CH00003 ._CH',             # 10
        'ED6_DT07/CH00013 ._CH',             # 11
        'ED6_DT07/CH00073 ._CH',             # 12
        'ED6_DT06/CH20020 ._CH',             # 13
        'ED6_DT06/CH20021 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH02030P._CP',             # 00
        'ED6_DT07/CH02100P._CP',             # 01
        'ED6_DT07/CH02140P._CP',             # 02
        'ED6_DT07/CH02470P._CP',             # 03
        'ED6_DT07/CH02353P._CP',             # 04
        'ED6_DT07/CH02603P._CP',             # 05
        'ED6_DT07/CH02623P._CP',             # 06
        'ED6_DT07/CH02370P._CP',             # 07
        'ED6_DT07/CH02363P._CP',             # 08
        'ED6_DT07/CH02460P._CP',             # 09
        'ED6_DT07/CH02230P._CP',             # 0A
        'ED6_DT07/CH02240P._CP',             # 0B
        'ED6_DT07/CH01350P._CP',             # 0C
        'ED6_DT07/CH02033P._CP',             # 0D
        'ED6_DT07/CH02103P._CP',             # 0E
        'ED6_DT06/CH20088P._CP',             # 0F
        'ED6_DT07/CH00003P._CP',             # 10
        'ED6_DT07/CH00013P._CP',             # 11
        'ED6_DT07/CH00073P._CP',             # 12
        'ED6_DT06/CH20020P._CP',             # 13
        'ED6_DT06/CH20021P._CP',             # 14
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
        X                   = -1020,
        Z                   = 0,
        Y                   = 85000,
        Direction           = 175,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 0,
        Y                   = 76500,
        Direction           = 53,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 0,
        Y                   = 81150,
        Direction           = 255,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -5950,
        Z                   = 0,
        Y                   = 68110,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65555,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65555,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65555,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65555,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65555,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65555,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65555,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65555,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65555,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327700,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327700,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327700,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327700,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327700,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327700,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327700,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1179667,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1179667,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1179667,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1179667,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 983059,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 983059,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 983059,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 983059,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1376275,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1179667,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1179667,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1179667,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1179667,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 983059,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 983059,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 983059,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 983059,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1376275,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1245203,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1245203,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1245203,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1245203,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1048595,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1048595,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1048595,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1048595,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1441811,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1245203,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1245203,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1245203,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1245203,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1048595,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1048595,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1048595,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1048595,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1441811,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327699,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327699,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327699,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1769491,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1769491,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1835027,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1835027,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1835027,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1835027,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_AD2",          # 00, 0
        "Function_1_B8A",          # 01, 1
        "Function_2_BA4",          # 02, 2
        "Function_3_BBA",          # 03, 3
        "Function_4_D33",          # 04, 4
        "Function_5_EAE",          # 05, 5
        "Function_6_FD5",          # 06, 6
        "Function_7_13DC",         # 07, 7
        "Function_8_4A57",         # 08, 8
        "Function_9_4AB6",         # 09, 9
        "Function_10_4AE6",        # 0A, 10
        "Function_11_4B59",        # 0B, 11
        "Function_12_4B9D",        # 0C, 12
    )


    def Function_0_AD2(): pass

    label("Function_0_AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_AE0")
    OP_A3(0x3FA)
    Event(0, 7)

    label("loc_AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B0A")
    SetChrChipByIndex(0x0, 9)
    SetChrChipByIndex(0x1, 10)
    SetChrChipByIndex(0x138, 11)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_B28")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_B89")

    label("loc_B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_B3C")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_B89")

    label("loc_B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_B5A")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_B89")

    label("loc_B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_B78")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_B89")

    label("loc_B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_B82")
    Jump("loc_B89")

    label("loc_B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_B89")

    label("loc_B89")

    Return()

    # Function_0_AD2 end

    def Function_1_B8A(): pass

    label("Function_1_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_B9A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B9A")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_B8A end

    def Function_2_BA4(): pass

    label("Function_2_BA4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_BA4")

    label("loc_BB9")

    Return()

    # Function_2_BA4 end

    def Function_3_BBA(): pass

    label("Function_3_BBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_BC7")
    Jump("loc_D2F")

    label("loc_BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_C40")

    ChrTalk(
        0xFE,
        (
            "因为诞辰庆典，\x01",
            "今天大街上很热闹呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要不是还有工作，\x01",
            "也会出去好好玩玩的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2F")

    label("loc_C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_C4A")
    Jump("loc_D2F")

    label("loc_C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_C54")
    Jump("loc_D2F")

    label("loc_C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "茜亚和希尔丹夫人到哪儿去了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2F")

    label("loc_C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_D2F")

    ChrTalk(
        0xFE,
        (
            "还要让客人们专程\x01",
            "来陪公爵他消磨时间，\x01",
            "真是够麻烦的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "明明大家都那么忙。\x02",
    )

    CloseMessageWindow()

    label("loc_D2F")

    TalkEnd(0xFE)
    Return()

    # Function_3_BBA end

    def Function_4_D33(): pass

    label("Function_4_D33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_D40")
    Jump("loc_EAA")

    label("loc_D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_D4A")
    Jump("loc_EAA")

    label("loc_D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_D54")
    Jump("loc_EAA")

    label("loc_D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_D5E")
    Jump("loc_EAA")

    label("loc_D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_DC8")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "理查德上校实在是帅呆了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和那个公爵相比\x01",
            "根本就是天壤之别嘛～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAA")

    label("loc_DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E27")

    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "公爵用那双讨厌的眼睛\x01",
            "在我身上转来转去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哼，太无礼了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EAA")

    label("loc_E27")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "刚才在走廊上\x01",
            "和杜南公爵擦肩而过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公爵他用\x01",
            "那双讨厌的眼睛\x01",
            "在我身上转来转去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哼，太无礼了。\x02",
    )

    CloseMessageWindow()

    label("loc_EAA")

    TalkEnd(0xFE)
    Return()

    # Function_4_D33 end

    def Function_5_EAE(): pass

    label("Function_5_EAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_EBB")
    Jump("loc_FD1")

    label("loc_EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_EC5")
    Jump("loc_FD1")

    label("loc_EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_ECF")
    Jump("loc_FD1")

    label("loc_ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_ED9")
    Jump("loc_FD1")

    label("loc_ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_F61")

    ChrTalk(
        0xFE,
        "终于结束了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "赶快收拾好东西，\x01",
            "早点回家去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD1")

    label("loc_F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_FD1")

    ChrTalk(
        0xFE,
        "有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对不起呀，\x01",
            "我现在正忙着晚宴的准备工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD1")

    TalkEnd(0xFE)
    Return()

    # Function_5_EAE end

    def Function_6_FD5(): pass

    label("Function_6_FD5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_FE2")
    Jump("loc_13D8")

    label("loc_FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1133")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_107B")

    ChrTalk(
        0xFE,
        (
            "特务部队的队长\x01",
            "取下面具之后，\x01",
            "真是帅呆了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，\x01",
            "为何他要戴面具呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1130")

    label("loc_107B")


    ChrTalk(
        0xFE,
        "我悄悄对你们说哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特务部队的队长\x01",
            "取下面具之后，\x01",
            "真是帅呆了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，\x01",
            "为何他要戴面具呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1130")

    Jump("loc_13D8")

    label("loc_1133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_113D")
    Jump("loc_13D8")

    label("loc_113D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_1147")
    Jump("loc_13D8")

    label("loc_1147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_1292")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11DD")

    ChrTalk(
        0xFE,
        (
            "公爵喝醉之后\x01",
            "会变得更加无耻下流……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "简直不敢相信他和女王陛下\x01",
            "还有公主殿下是同一血脉的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128F")

    label("loc_11DD")


    ChrTalk(
        0xFE,
        "我悄悄对你们说哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公爵喝醉之后\x01",
            "会变得更加无耻下流……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "简直不敢相信他和女王陛下\x01",
            "还有公主殿下是同一血脉的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_128F")

    Jump("loc_13D8")

    label("loc_1292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_13D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1327")

    ChrTalk(
        0xFE,
        (
            "虽然人手已经足够了，\x01",
            "但公爵还要叫希尔丹夫人\x01",
            "不断增加侍女的数量……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正他肯定是\x01",
            "不怀什么好意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D8")

    label("loc_1327")


    ChrTalk(
        0xFE,
        "我悄悄对你们说哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然人手已经足够了，\x01",
            "但公爵还要叫希尔丹夫人\x01",
            "不断增加侍女的数量……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正他肯定是\x01",
            "不怀什么好意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D8")

    TalkEnd(0xFE)
    Return()

    # Function_6_FD5 end

    def Function_7_13DC(): pass

    label("Function_7_13DC")

    EventBegin(0x0)
    OP_6D(810, 0, 78760, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(1850, 0)
    OP_6C(39000, 0)
    OP_6E(492, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xC, -2450, 200, 82370, 90)
    SetChrPos(0xD, -2450, 200, 79820, 90)
    SetChrPos(0xE, -2450, 200, 77340, 90)
    SetChrPos(0x10, -2450, 200, 74860, 90)
    SetChrPos(0xF, -3070, 200, 74030, 90)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x108, 0x4)
    SetChrPos(0x108, 2490, 200, 79820, 270)
    SetChrPos(0x102, 2490, 200, 74860, 270)
    SetChrPos(0x101, 2490, 200, 77340, 270)
    SetChrChipByIndex(0x101, 16)
    SetChrChipByIndex(0x102, 17)
    SetChrChipByIndex(0x108, 18)
    SetChrPos(0x11, 6840, -10000, 80920, 270)
    SetChrPos(0x12, 6840, -10000, 79460, 270)
    SetChrPos(0x13, 6840, -10000, 77970, 270)
    SetChrPos(0x14, 6840, -10000, 76490, 270)
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
    SetChrPos(0x15, 1600, 650, 82450, 0)
    SetChrPos(0x16, 1600, 650, 79950, 0)
    SetChrPos(0x17, 1600, 650, 77440, 0)
    SetChrPos(0x18, 1600, 650, 74950, 0)
    SetChrPos(0x19, -1600, 670, 82350, 0)
    SetChrPos(0x1A, -1600, 670, 79950, 0)
    SetChrPos(0x1B, -1600, 670, 77450, 0)
    SetChrPos(0x1C, -1600, 670, 74850, 0)
    SetChrPos(0x1D, 0, 650, 83860, 0)
    SetChrPos(0x4A, -500, 640, 83860, 0)
    SetChrPos(0x41, -700, 640, 83860, 0)
    SetChrPos(0x38, 200, 640, 83860, 0)
    SetChrPos(0x2F, 400, 640, 83860, 0)
    SetChrPos(0x39, 1600, 640, 82700, 0)
    SetChrPos(0x3A, 1600, 640, 80200, 0)
    SetChrPos(0x3B, 1600, 640, 77600, 0)
    SetChrPos(0x3C, 1600, 640, 75200, 0)
    SetChrPos(0x2B, -1600, 640, 82700, 0)
    SetChrPos(0x2C, -1600, 640, 80200, 0)
    SetChrPos(0x2D, -1600, 640, 77700, 0)
    SetChrPos(0x2E, -1600, 640, 75200, 0)
    SetChrPos(0x42, 1600, 640, 82900, 0)
    SetChrPos(0x43, 1600, 640, 80400, 0)
    SetChrPos(0x44, 1600, 640, 77800, 0)
    SetChrPos(0x45, 1600, 640, 75400, 0)
    SetChrPos(0x34, -1600, 640, 82900, 0)
    SetChrPos(0x35, -1600, 640, 80400, 0)
    SetChrPos(0x36, -1600, 640, 77900, 0)
    SetChrPos(0x37, -1600, 640, 75400, 0)
    SetChrPos(0x27, 1600, 640, 82000, 0)
    SetChrPos(0x28, 1600, 640, 79600, 0)
    SetChrPos(0x29, 1600, 640, 77000, 0)
    SetChrPos(0x2A, 1600, 640, 74500, 0)
    SetChrPos(0x3D, -1600, 640, 81900, 0)
    SetChrPos(0x3E, -1600, 640, 79500, 0)
    SetChrPos(0x3F, -1600, 640, 77000, 0)
    SetChrPos(0x40, -1600, 640, 74400, 0)
    SetChrPos(0x30, 1600, 640, 81800, 0)
    SetChrPos(0x31, 1600, 640, 79400, 0)
    SetChrPos(0x32, 1600, 640, 76800, 0)
    SetChrPos(0x33, 1600, 640, 74300, 0)
    SetChrPos(0x46, -1600, 640, 81700, 0)
    SetChrPos(0x47, -1600, 640, 79300, 0)
    SetChrPos(0x48, -1600, 640, 76800, 0)
    SetChrPos(0x49, -1600, 640, 74200, 0)
    SetChrSubChip(0xC, 2)
    SetChrSubChip(0xD, 2)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x108, 1)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 2)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#505F唔……\x01",
            "这就是传说中的晚宴吗？\x02\x03",
            "可是为什么餐具摆放好了，\x01",
            "那些听说非常好吃的料理却没有呢？\x02\x03",
            "为什么这些刀子啊叉子啊\x01",
            "要这样整整齐齐并排放在一起呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P因为这是很正式的晚宴啊。\x02\x03",
            "先是凉菜，\x01",
            "然后接着才上各种各样的料理。\x02\x03",
            "还有就是刀子和叉子要从侧边来拿。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F真麻烦……\x01",
            "这就是所谓的餐桌礼仪吧。\x02\x03",
            "#007F我还真是有些紧张了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#611F嘻嘻……不用那么在意。\x01",
            "　\x02\x03",
            "因为品尝料理的美味才是最重要的。\x01",
            "　\x02\x03",
            "什么礼仪礼貌的都是其次的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#601F对啊对啊。\x02\x03",
            "更何况，你们两人对\x01",
            "在场出席的各位不都是很熟悉的嘛。\x01",
            "　\x02\x03",
            "没有必要那么拘束哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊，说的也是啊?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F#2P这样一来就没办法了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#610F对了，请问这位先生\x01",
            "对于这里的刀子和叉子习惯吗？\x02\x03",
            "我听说东方那边主要是使用筷子的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F哦，您知道得很清楚啊。\x02\x03",
            "#070F不过俗话说得好，入乡随俗嘛。\x01",
            "　\x02\x03",
            "虽说用得不好，\x01",
            "但还是会一点用刀子和叉子的方法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#611F啊……很了不起呢。\x02\x03",
            "不愧是取得武术大会优胜的武术高手，\x01",
            "说起话来都和普通人不同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F哈哈哈……\x01",
            "哪里哪里，小姐您过奖了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F（确实是对美人没有抵抗力呢……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P（可是我并不觉得\x01",
            "　他是一个喜好女色的人……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#805F话说回来……\x01",
            "公爵大人怎么这么慢呢。\x02\x03",
            "究竟想要做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#600F嗯……的确。\x02\x03",
            "而且，如果说上座是公爵大人的，\x01",
            "那么那边的座位又是给谁的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#783F是啊……\x02\x03",
            "大概，科洛蒂娅公主坐在那里的\x01",
            "可能性会比较高……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -250, 0, 62670, 0)
    SetChrPos(0x9, 460, 0, 62290, 0)
    SetChrPos(0xA, -110, 0, 64099, 0)
    SetChrPos(0xB, 10, 0, 62670, 0)

    ChrTalk(
        0xB,
        (
            "#1P各位……\x01",
            "让你们久等了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20FA():
        OP_6D(370, 0, 72370, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20FA)
    SetChrSubChip(0xC, 2)
    SetChrSubChip(0xE, 2)
    Sleep(100)
    SetChrSubChip(0x108, 1)
    SetChrSubChip(0x10, 2)
    Sleep(100)
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xD, 2)
    Sleep(100)
    SetChrSubChip(0x102, 1)
    Sleep(700)

    def lambda_2149():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_2149)

    def lambda_215B():
        OP_8E(0xFE, 0xA, 0x0, 0x10586, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_215B)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0xB,
        "#720F公爵大人大驾光临。\x02",
    )

    CloseMessageWindow()

    def lambda_21AF():
        OP_8E(0xFE, 0xFFFFF772, 0x0, 0x105F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_21AF)
    WaitChrThread(0xB, 0x1)
    OP_8C(0xB, 0, 400)
    Sleep(300)

    def lambda_21DB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_21DB)

    def lambda_21ED():
        OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x10DE2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_21ED)
    Sleep(300)

    def lambda_220D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_220D)

    def lambda_221F():
        OP_8E(0xFE, 0x438, 0x0, 0x10C3E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_221F)
    Sleep(600)

    def lambda_223F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_223F)

    def lambda_2251():
        OP_8E(0xFE, 0x190, 0x0, 0x1070C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2251)
    WaitChrThread(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "#220F哎呀，诸位亲爱的朋友，\x01",
            "让你们等那么久真是不好意思。\x02\x03",
            "因为刚才稍稍有点事要协商一下，\x01",
            "所以拖延了一点儿的时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)

    ChrTalk(
        0xA,
        (
            "#220F这位是理查德上校，\x01",
            "王国军情报部的负责人。\x02\x03",
            "为了解决恐怖事件，\x01",
            "他日夜操劳、尽心尽力，\x01",
            "作为对他工作的奖赏我就邀请他来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)

    ChrTalk(
        0x8,
        (
            "#110F初次与大家见面。\x01",
            "我是王国军情报部的理查德。\x02\x03",
            "承蒙公爵大人的好意，\x01",
            "我今天得以有幸参加这次晚宴。\x02\x03",
            "这身与场合不相称的军服有些失礼了，\x01",
            "但还请允许我与各位同席。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xA, 0x1, 0x0, 0xA)
    Sleep(300)
    Sleep(100)

    def lambda_24BE():
        OP_6D(810, 0, 78760, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_24BE)
    OP_43(0x8, 0x1, 0x0, 0x8)
    Sleep(200)
    OP_43(0xB, 0x1, 0x0, 0xB)
    OP_43(0x9, 0x1, 0x0, 0x9)
    OP_43(0x108, 0x1, 0x0, 0xC)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#509F（竟、竟然会和上校一起在餐桌上用餐……）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#2P（虽然猜到了几分，\x01",
            "　但果然还是些紧张……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(0, 0, 72440, 0)
    OP_67(0, 9430, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(45000, 0)
    OP_6E(492, 0)
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4D, 0x80)
    SetChrPos(0x4B, 0, 700, 81230, 0)
    SetChrPos(0x4C, 0, 700, 78740, 0)
    SetChrPos(0x4D, 0, 700, 76070, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x1E, 1500, 640, 83150, 0)
    SetChrPos(0x1F, 1500, 640, 80650, 0)
    SetChrPos(0x20, 1500, 640, 78140, 0)
    SetChrPos(0x21, 1500, 640, 75650, 0)
    SetChrPos(0x22, -1600, 640, 81450, 0)
    SetChrPos(0x23, -1600, 640, 79050, 0)
    SetChrPos(0x24, -1600, 640, 76650, 0)
    SetChrPos(0x25, -1600, 640, 74050, 0)
    SetChrPos(0x26, -800, 640, 83860, 0)
    SetChrSubChip(0x15, 28)
    SetChrSubChip(0x15, 9)
    SetChrSubChip(0x16, 9)
    SetChrSubChip(0x17, 9)
    SetChrSubChip(0x18, 9)
    SetChrSubChip(0x19, 9)
    SetChrSubChip(0x1A, 9)
    SetChrSubChip(0x1B, 9)
    SetChrSubChip(0x1C, 9)
    SetChrSubChip(0x1D, 9)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x39, 0x80)
    SetChrFlags(0x3A, 0x80)
    SetChrFlags(0x3B, 0x80)
    SetChrFlags(0x3C, 0x80)
    SetChrFlags(0x3D, 0x80)
    SetChrFlags(0x3E, 0x80)
    SetChrFlags(0x3F, 0x80)
    SetChrFlags(0x49, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x41, 0x80)
    SetChrPos(0x11, -3100, 0, 86090, 339)
    SetChrPos(0x12, 4910, 0, 72190, 265)
    SetChrPos(0x13, -220, 0, 71290, 2)
    SetChrPos(0x14, -5050, 0, 78270, 84)
    OP_72(0xC, 0x4)
    OP_72(0xD, 0x4)
    ClearChrFlags(0x4E, 0x80)
    ClearChrFlags(0x4F, 0x80)
    ClearChrFlags(0x50, 0x80)
    ClearChrFlags(0x51, 0x80)
    ClearChrFlags(0x52, 0x80)
    ClearChrFlags(0x53, 0x80)
    SetChrPos(0x4E, -3280, 750, 87230, 0)
    SetChrPos(0x50, -2630, 700, 87630, 0)
    SetChrPos(0x51, -2470, 700, 87240, 0)
    SetChrPos(0x4F, 3960, 750, 70260, 0)
    SetChrPos(0x52, 3990, 700, 70960, 0)
    SetChrPos(0x53, 4440, 700, 70760, 0)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xD, 1)
    SetChrSubChip(0xE, 1)
    SetChrSubChip(0x10, 1)
    SetChrSubChip(0x108, 2)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x102, 2)
    WaitChrThread(0xB, 0x1)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_6D(-50, 0, 85000, 5000)
    OP_22(0xE8, 0x0, 0x64)
    Fade(1000)
    OP_6D(1080, 0, 79800, 0)
    OP_67(0, 3950, -10000, 0)
    OP_6B(2113, 0)
    OP_6C(39000, 0)
    OP_6E(492, 0)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#221F哈～哈～哈，哎呀，愉快愉快。\x02\x03",
            "#220F怎么样，梅贝尔市长。\x01",
            "格兰赛尔城这里的厨艺怎么样？\x02\x03",
            "与柏斯的『安特洛丝餐厅』相比\x01",
            "也毫不逊色对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#610F嗯，很精妙的厨艺呢。\x02\x03",
            "配上葡萄酒的话可以说是非常完美了，\x01",
            "的确是出乎预料的极品佳肴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#221F哈哈哈～～～\x01",
            "既然都这么说了肯定就不是吹牛的了。\x02\x03",
            "#220F对了，你是叫金对吧。\x01",
            "东方人对于这些可能会不大合胃口吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哪里，非常美味啊。\x02\x03",
            "虽说在下的舌头很迟钝，\x01",
            "但也能感觉得出其中蕴涵的美味。\x02\x03",
            "品味出了利贝尔料理的精髓所在。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#225F嗯嗯，说得好。\x02\x03",
            "#220F怎么样啊，两位年轻的游击士？\x02\x03",
            "如此豪华的料理还是第一次品尝到吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#4P唔～～\x01",
            "的确非常非常美味啊。\x02\x03",
            "邀请的人就先不论如何，\x01",
            "就这个料理来说还真的很美妙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#221F哈哈哈。\x01",
            "说得好、说得好…………啊……？\x02\x03",
            "#223F……唔？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#019F#4P呵呵，没错没错。\x01",
            "实在是十分优秀的料理呢。\x02\x03",
            "而且至今为止我们还没有过这样\x01",
            "能够和各界名流一起共聚晚宴的机会，\x01",
            "说起来还真是有些不习惯呢。\x02\x03",
            "#010F承蒙公爵大人您的款待，\x01",
            "我们真是感激不尽啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#221F哈哈哈。\x01",
            "这位小男孩很会说话嘛。\x02\x03",
            "#220F不过刚才经管家的提醒，\x01",
            "我现在总算是想起来了……\x02\x03",
            "你们两个就是曾经在卢安事件中\x01",
            "和我见过一面的小孩嘛。\x02\x03",
            "缘分这个东西真是奇妙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#4P哈、哈哈……是～是啊。\x02\x03",
            "#505F（管家没有提醒之前\x01",
            "　难道自己就不会想起来吗……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#221F好啊，今晚不醉不归！\x02\x03",
            "料理和美酒都是应有尽有，\x01",
            "不要有顾虑，诸位想享用就尽管说！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F#2P公爵大人……\x02\x03",
            "要不我们先告诉大家\x01",
            "刚才商量后达成的决定如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#223F……哦哦！\x01",
            "对啊，还有这么回事呢。\x02\x03",
            "#220F事实上把作为王国代表的诸位\x01",
            "集中在这里没有什么别的意思……\x02\x03",
            "就是借这个晚宴的机会\x01",
            "向大家宣布一件重大的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#604F#6P重大的事情……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#800F这究竟……\x01",
            "是什么样的事情呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#225F嗯。\x02\x03",
            "在此首先由理查德上校来为我\x01",
            "说明相关的内容。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#115F#2P……惶恐之至。\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    SetChrSubChip(0x8, 1)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#110F#5P女王陛下身体欠佳，\x01",
            "是各位之前已知的事实。\x02\x03",
            "不过陛下正在缓缓的康复中，\x01",
            "很快就会以往日的姿态与人们见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#601F#6P哦……这就好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#611F那去探望陛下也是可以的了？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#115F#5P真是抱歉，照陛下的意向，\x01",
            "还是希望暂时先谢绝各位的探望。\x02\x03",
            "#110F然而，这几天扰乱王都周边\x01",
            "秩序的恐怖组织要先予以铲除。\x02\x03",
            "这件事成功之后，\x01",
            "女王陛下的诞辰庆典才能按期顺利进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#783F嗯……听起来相当有道理。\x01",
            "这样能让市民安居乐业、安心生活，\x01",
            "能做到的确是值得庆贺的事。\x02\x03",
            "#780F不过……\x01",
            "想要说的应该不止是这些吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#803F……是啊，如果只是这些的话，\x01",
            "联络我们并说明就可以了的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#111F#5P呵呵，能察觉到就好啊。\x02\x03",
            "#115F女王陛下的健康状况正在恢复，\x01",
            "之前也已经说到了……\x02\x03",
            "陛下因为这次身体欠佳，\x01",
            "所以先前已经做出了一个决定。\x02\x03",
            "那个决定就是——\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetChrSubChip(0x8, 0)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#112F#5P艾莉茜雅女王陛下自动退位，\x01",
            "让在座的杜南公爵大人继承王位。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#804F什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#613F真、真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F#4P（约修亚，这是……！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4P（嗯……\x01",
            "阴谋终于浮出水面了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#225F……我也感到有些意外，\x01",
            "不过女王陛下确实有些力不从心了。\x02\x03",
            "这也是陛下迫不得已的决定，\x01",
            "一名女性能领导经历了诸多动荡的王国\x01",
            "长达４０年已经是实属不易的事情。\x02\x03",
            "#220F所以，陛下打算在诞辰庆典之后，\x01",
            "从王国的政务俗事中解放出来……\x02\x03",
            "转交王位的继承权的决定\x01",
            "就是出于这样的一个原因。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#603F#6P竟然……\x01",
            "陛下一直为此而深感苦恼……\x02\x03",
            "每年见到她的时候都没感觉到，\x01",
            "是我们的不对啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#612F可、可是……\x01",
            "怎能在这样一个觥筹交错的宴席上\x01",
            "宣布如此重大的决议呢。\x02\x03",
            "冒昧地问一句，\x01",
            "您刚才这番话究竟算不算数的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#222F唔……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#110F#5P哼哼，梅贝尔市长。\x02\x03",
            "公爵大人的话毫无信用可言，\x01",
            "……这就是你的意思吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#614F我、我没有那么说过！\x02\x03",
            "倘若女王陛下真的要退位，\x01",
            "也只能通过市长的投票来表决王位继承人，\x01",
            "我不解的是为何连这项程序都不执行！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#803F是啊……\x02\x03",
            "可以的话，我们想直接\x01",
            "向陛下询问一下刚才那些决议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#226F呜、呜～嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#115F#5P各位不解的情绪我很理解。\x02\x03",
            "不过还是请冷静下来，\x01",
            "暂且先知道就可以了。\x02\x03",
            "#110F更进一步地来说，\x01",
            "女王陛下本人将会在诞辰庆典之时\x01",
            "亲自公布这项重大的决议。\x02\x03",
            "是真是假到那时就可以见分晓了对吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#805F这、这……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#112F#5P问题在于公布这项决议时\x01",
            "会给普通市民带来什么样的影响。\x02\x03",
            "为了避免无益的混乱，\x01",
            "所以才把各地区的负责人也就是在座的\x01",
            "各位召集到这里来传达这项决议……\x02\x03",
            "公爵大人也是这么认为的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#225F咳咳……\x01",
            "嗯，就是这样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#112F#5P而且陛下如果退位的话，\x01",
            "这个消息肯定不止是流传于国内。\x02\x03",
            "大陆诸国，尤其是我们最大的威胁\x01",
            "埃雷波尼亚帝国肯定会注意到这个变动。\x02\x03",
            "正因为如此，\x01",
            "在座的各位应该扶植新的国王陛下，\x01",
            "如果不团结起来是绝对不行的……\x02\x03",
            "特别是在这样一个关键时期即将来临的时刻。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(
        0x101,
        (
            "#509F#4P（居、居然说得如此冠冕堂皇……）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P（嗯……\x01",
            "　好一个煽动者啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE)
    OP_63(0xC)
    OP_63(0x10)
    OP_63(0xD)

    ChrTalk(
        0xE,
        (
            "#800F正式的决定可以在诞辰庆典时\x01",
            "向陛下直接请示……\x02\x03",
            "不过要事先做好心里准备，\x01",
            "就是这样对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#111F#5P哼哼……\x01",
            "能够理解真是万幸啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#603F#6P唔～……\x02\x03",
            "一旦这件事情落实了，\x01",
            "我们日后的工作就有得忙碌了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#615F是呢……\x01",
            "还要向市民们宣布。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#782F……我还有一事想请教一下。\x02\x03",
            "公爵大人具有王位的继承权\x01",
            "这点我也承认……\x02\x03",
            "我认为具有同样资格的继承者\x01",
            "应该还有另外一位吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#226F这、这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F#5P还有陛下的孙女科洛蒂娅殿下。\x01",
            "　\x02\x03",
            "的确，依据王室典范的规定，\x01",
            "她和公爵大人拥有同等资格……\x02\x03",
            "但是，毕竟她的年纪尚幼，\x01",
            "所以陛下就推选了公爵大人。\x02\x03",
            "#115F而且之前也说到过……\x01",
            "要一位小姑娘来承担一种女性\x01",
            "所不能所承担的重责是不可取的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#221F对呀对呀，就是这样的！\x02\x03",
            "#220F对了，现在正打算为\x01",
            "科洛蒂娅公主寻找良缘佳偶。\x02\x03",
            "虽然是非正式的，但是之前其他国家的王族\x01",
            "已经提出过了相关的事宜……\x02\x03",
            "如果时机成熟的话，\x01",
            "准备在今年年中实现这个婚约。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#613F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#783F……唔，您说的话我明白了。\x02\x03",
            "#780F这么一来就可以让好事成双了对吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#604F#6P唔……公主殿下……\x02\x03",
            "要此时结婚似乎也太过早了吧……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F……打搅一下。\x01",
            "我问个问题好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4P金、金先生？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F哦……？\x02\x03",
            "没关系，但说无妨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F很抱歉，刚才听到那番话之后，\x01",
            "本来作为外人的我们是不应该对此多言的，\x01",
            "但是有些问题不能不问。\x02\x03",
            "况且我并非是王国的国民。\x02\x03",
            "#070F那就是……为何要特地在\x01",
            "这样的酒席间发表如此重大的决议？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F#5P这是因为取得优胜的几位\x01",
            "恰好就是游击士的缘故。\x02\x03",
            "陛下退位这个重大的事情\x01",
            "也需要拜托你们传达给游击士协会。\x02\x03",
            "所以我才给公爵大人提议，\x01",
            "让你们参加晚宴来得知这件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F原来如此……\x02\x03",
            "在利贝尔王国，军队和协会有着\x01",
            "良好的关系的传言看来果真不假。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#111F#5P哈哈，和帝国及共和国相比，\x01",
            "我国的军力不是很充实。\x02\x03",
            "只有携起手来，\x01",
            "才能面对苛刻的现实……\x02\x03",
            "#110F总之就是这样的，\x01",
            "你明白其中的意思了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F呼……明白了。\x02\x03",
            "我会把今天从宴席中得知的情况\x01",
            "转达给王都支部的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4262   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_7_13DC end

    def Function_8_4A57(): pass

    label("Function_8_4A57")

    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x10D6, 0x0, 0x10FC2, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1112, 0x0, 0x13AE2, 0xBB8, 0x0)
    OP_8E(0xFE, 0x92E, 0x0, 0x13FB0, 0xBB8, 0x0)
    SetChrPos(0xFE, 2500, 200, 82410, 270)
    SetChrChipByIndex(0xFE, 13)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_8_4A57 end

    def Function_9_4AB6(): pass

    label("Function_9_4AB6")

    OP_8E(0xFE, 0x10D6, 0x0, 0x10FC2, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1176, 0x0, 0x14460, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_4AB6 end

    def Function_10_4AE6(): pass

    label("Function_10_4AE6")

    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFEEE4, 0x0, 0x117EC, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFEF48, 0x0, 0x14D02, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFFBFA, 0x0, 0x14D02, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFFDF8, 0x0, 0x14C08, 0x7D0, 0x0)
    SetChrPos(0xFE, -20, 200, 84940, 180)
    SetChrChipByIndex(0xFE, 15)
    OP_8C(0xFE, 180, 0)
    Return()

    # Function_10_4AE6 end

    def Function_11_4B59(): pass

    label("Function_11_4B59")

    OP_8E(0xFE, 0xFFFFEEE4, 0x0, 0x117EC, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFEF48, 0x0, 0x14D02, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFFC72, 0x0, 0x15126, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_11_4B59 end

    def Function_12_4B9D(): pass

    label("Function_12_4B9D")

    Sleep(2000)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xE, 0)
    Sleep(1000)
    SetChrSubChip(0x108, 0)
    SetChrSubChip(0xD, 0)
    Sleep(1000)
    SetChrSubChip(0xC, 0)
    Return()

    # Function_12_4B9D end

    SaveToFile()

Try(main)
