from ED6ScenarioHelper import *

def main():
    # 托兰特平原道

    CreateScenaFile(
        FileName            = 'R3102   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3102.x',
        MapIndex            = 144,
        MapDefaultBGM       = "ed60020",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/R3102   ._SN',
            'ED6_DT01/R3102_1 ._SN',
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
        '王',                                   # 9
        '布鲁诺',                               # 10
        '装甲兔',                               # 11
        '装甲兔',                               # 12
        '装甲兔',                               # 13
        '装甲兔',                               # 14
        '装甲兔',                               # 15
        '装甲兔',                               # 16
        '车',                                   # 17
        '装甲兔',                               # 18
        '装甲兔',                               # 19
        '装甲兔',                               # 20
        '装甲兔',                               # 21
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
        Unknown_3A              = 144,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01760 ._CH',             # 00
        'ED6_DT07/CH01530 ._CH',             # 01
        'ED6_DT09/CH10123 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00101 ._CH',             # 04
        'ED6_DT07/CH00490 ._CH',             # 05
        'ED6_DT07/CH00491 ._CH',             # 06
        'ED6_DT09/CH10120 ._CH',             # 07
        'ED6_DT09/CH10121 ._CH',             # 08
        'ED6_DT07/CH00110 ._CH',             # 09
        'ED6_DT07/CH00111 ._CH',             # 0A
        'ED6_DT07/CH00492 ._CH',             # 0B
        'ED6_DT07/CH00494 ._CH',             # 0C
        'ED6_DT07/CH00160 ._CH',             # 0D
        'ED6_DT06/CH20119 ._CH',             # 0E
        'ED6_DT09/CH10610 ._CH',             # 0F
        'ED6_DT09/CH10611 ._CH',             # 10
        'ED6_DT07/CH00000 ._CH',             # 11
        'ED6_DT07/CH00000 ._CH',             # 12
        'ED6_DT09/CH10120 ._CH',             # 13
        'ED6_DT09/CH10121 ._CH',             # 14
        'ED6_DT09/CH10140 ._CH',             # 15
        'ED6_DT09/CH10141 ._CH',             # 16
        'ED6_DT09/CH10620 ._CH',             # 17
        'ED6_DT09/CH10621 ._CH',             # 18
        'ED6_DT09/CH10600 ._CH',             # 19
        'ED6_DT09/CH10601 ._CH',             # 1A
        'ED6_DT09/CH10400 ._CH',             # 1B
        'ED6_DT09/CH10401 ._CH',             # 1C
        'ED6_DT09/CH11240 ._CH',             # 1D
        'ED6_DT09/CH11241 ._CH',             # 1E
    )

    AddCharChipPat(
        'ED6_DT07/CH01760P._CP',             # 00
        'ED6_DT07/CH01530P._CP',             # 01
        'ED6_DT09/CH10123P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00101P._CP',             # 04
        'ED6_DT07/CH00490P._CP',             # 05
        'ED6_DT07/CH00491P._CP',             # 06
        'ED6_DT09/CH10120P._CP',             # 07
        'ED6_DT09/CH10121P._CP',             # 08
        'ED6_DT07/CH00110P._CP',             # 09
        'ED6_DT07/CH00111P._CP',             # 0A
        'ED6_DT07/CH00492P._CP',             # 0B
        'ED6_DT07/CH00494P._CP',             # 0C
        'ED6_DT07/CH00160P._CP',             # 0D
        'ED6_DT06/CH20119P._CP',             # 0E
        'ED6_DT09/CH10610P._CP',             # 0F
        'ED6_DT09/CH10611P._CP',             # 10
        'ED6_DT09/CH10080P._CP',             # 11
        'ED6_DT09/CH10081P._CP',             # 12
        'ED6_DT09/CH10120P._CP',             # 13
        'ED6_DT09/CH10121P._CP',             # 14
        'ED6_DT09/CH10140P._CP',             # 15
        'ED6_DT09/CH10141P._CP',             # 16
        'ED6_DT09/CH10620P._CP',             # 17
        'ED6_DT09/CH10621P._CP',             # 18
        'ED6_DT09/CH10600P._CP',             # 19
        'ED6_DT09/CH10601P._CP',             # 1A
        'ED6_DT09/CH10400P._CP',             # 1B
        'ED6_DT09/CH10401P._CP',             # 1C
        'ED6_DT09/CH11240P._CP',             # 1D
        'ED6_DT09/CH11241P._CP',             # 1E
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -27260,
        Z                   = 20,
        Y                   = -22270,
        Direction           = 357,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -74130,
        Z                   = 0,
        Y                   = 3100,
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
        X                   = 64319,
        Z                   = 10,
        Y                   = -52920,
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
        X                   = 10040,
        Z                   = -130,
        Y                   = 67800,
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


    DeclMonster(
        X                   = -36940,
        Z                   = -10,
        Y                   = 10890,
        Unknown_0C          = 180,
        Unknown_0E          = 23,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28070,
        Z                   = 80,
        Y                   = 10280,
        Unknown_0C          = 180,
        Unknown_0E          = 23,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17490,
        Z                   = 0,
        Y                   = -1540,
        Unknown_0C          = 180,
        Unknown_0E          = 23,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4150,
        Z                   = -60,
        Y                   = 15540,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x21B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32970,
        Z                   = -30,
        Y                   = 25660,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 26690,
        Z                   = 50,
        Y                   = 5570,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13500,
        Z                   = -20,
        Y                   = -4890,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x211,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34620,
        Z                   = -50,
        Y                   = -10530,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x211,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37440,
        Z                   = -50,
        Y                   = -24530,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x212,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15930,
        Z                   = 0,
        Y                   = -38970,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x211,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35920,
        Z                   = -20,
        Y                   = -35400,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -29740,
        Z                   = -110,
        Y                   = -7150,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19490,
        Z                   = 0,
        Y                   = -17710,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12390,
        Z                   = 50,
        Y                   = -16010,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x21B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5230,
        Z                   = 0,
        Y                   = -27150,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 11730,
        Z                   = -30,
        Y                   = 7970,
        Unknown_0C          = 0,
        Unknown_0E          = 29,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x5E0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -36940,
        Z                   = -10,
        Y                   = 10890,
        Unknown_0C          = 180,
        Unknown_0E          = 23,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28070,
        Z                   = 80,
        Y                   = 10280,
        Unknown_0C          = 180,
        Unknown_0E          = 23,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17490,
        Z                   = 0,
        Y                   = -1540,
        Unknown_0C          = 180,
        Unknown_0E          = 23,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4150,
        Z                   = -60,
        Y                   = 15540,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x35B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32970,
        Z                   = -30,
        Y                   = 25660,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 26690,
        Z                   = 50,
        Y                   = 5570,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13500,
        Z                   = -20,
        Y                   = -4890,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x351,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34620,
        Z                   = -50,
        Y                   = -10530,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x351,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37440,
        Z                   = -50,
        Y                   = -24530,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x352,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15930,
        Z                   = 0,
        Y                   = -38970,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x351,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35920,
        Z                   = -20,
        Y                   = -35400,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -29740,
        Z                   = -110,
        Y                   = -7150,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19490,
        Z                   = 0,
        Y                   = -17710,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12390,
        Z                   = 50,
        Y                   = -16010,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x35B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5230,
        Z                   = 0,
        Y                   = -27150,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 11730,
        Z                   = -30,
        Y                   = 7970,
        Unknown_0C          = 0,
        Unknown_0E          = 29,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x5E1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -27260,
        Y                   = -1000,
        Z                   = -22270,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = 13630,
        TriggerZ            = 0,
        TriggerY            = 35620,
        TriggerRange        = 1500,
        ActorX              = 13630,
        ActorZ              = 1200,
        ActorY              = 35620,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3130,
        TriggerZ            = 30,
        TriggerY            = -11320,
        TriggerRange        = 1000,
        ActorX              = -3130,
        ActorZ              = 30,
        ActorY              = -10750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_7CA",          # 00, 0
        "Function_1_879",          # 01, 1
        "Function_2_9F8",          # 02, 2
        "Function_3_AC6",          # 03, 3
        "Function_4_B9A",          # 04, 4
        "Function_5_F65",          # 05, 5
        "Function_6_F70",          # 06, 6
        "Function_7_1043",         # 07, 7
        "Function_8_10A1",         # 08, 8
        "Function_9_12BE",         # 09, 9
    )


    def Function_0_7CA(): pass

    label("Function_0_7CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_7D4")
    Jump("loc_86C")

    label("loc_7D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_7DE")
    Jump("loc_86C")

    label("loc_7DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_7E8")
    Jump("loc_86C")

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_7F2")
    Jump("loc_86C")

    label("loc_7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_7FC")
    Jump("loc_86C")

    label("loc_7FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_806")
    Jump("loc_86C")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_847")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_844")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -19060, -10, -40450, 145)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -17490, 10, -39610, 182)

    label("loc_844")

    Jump("loc_86C")

    label("loc_847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_851")
    Jump("loc_86C")

    label("loc_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_85B")
    Jump("loc_86C")

    label("loc_85B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_865")
    Jump("loc_86C")

    label("loc_865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_86C")

    label("loc_86C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_7CA end

    def Function_1_879(): pass

    label("Function_1_879")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x3002F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A3")
    OP_B1("R3102_y")
    Jump("loc_8AC")

    label("loc_8A3")

    OP_B1("R3102_n")

    label("loc_8AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90B")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
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
    Jump("loc_95B")

    label("loc_90B")

    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)

    label("loc_95B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96C")
    OP_1B(0x3, 0x0, 0x6)

    label("loc_96C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_983")
    Jump("loc_988")

    label("loc_983")

    OP_71(0x0, 0x4)

    label("loc_988")

    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0x32, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x32, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B6")
    ClearChrFlags(0x16, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_9B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C8")
    OP_6F(0x1, 0)
    Jump("loc_9CF")

    label("loc_9C8")

    OP_6F(0x1, 60)

    label("loc_9CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E0")
    OP_1B(0x1, 0x0, 0x5)

    label("loc_9E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9F7")
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x39, 0x80)

    label("loc_9F7")

    Return()

    # Function_1_879 end

    def Function_2_9F8(): pass

    label("Function_2_9F8")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_AB0")

    label("loc_A1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A36")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_AB0")

    label("loc_A36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_AB0")

    label("loc_A4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A68")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_AB0")

    label("loc_A68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A81")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_AB0")

    label("loc_A81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_AB0")

    label("loc_A9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB0")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_AB0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_AB0")

    label("loc_AC5")

    Return()

    # Function_2_9F8 end

    def Function_3_AC6(): pass

    label("Function_3_AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_B99")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x346)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEB")
    Call(1, 3)
    Jump("loc_B99")

    label("loc_AEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFE")
    Call(1, 2)
    Jump("loc_B99")

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B49")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "怎么样，布鲁诺先生？\x01",
            "是不是相当麻烦啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B96")

    label("loc_B49")

    TalkBegin(0xFE)
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我们要留在这里\x01",
            "继续努力试试。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们也要小心啊。\x02",
    )

    CloseMessageWindow()

    label("loc_B96")

    TalkEnd(0xFE)

    label("loc_B99")

    Return()

    # Function_3_AC6 end

    def Function_4_B9A(): pass

    label("Function_4_B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_F64")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x346)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BBF")
    Call(1, 3)
    Jump("loc_F64")

    label("loc_BBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD2")
    Call(1, 2)
    Jump("loc_F64")

    label("loc_BD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_C4B")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "呼，果然还是要\x01",
            "亲自去把零件给取回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也罢，自己的事情\x01",
            "还是只有靠自己来做了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F64")

    label("loc_C4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_E33")
    TalkBegin(0xFE)
    OP_A2(0x1)
    OP_28(0x29, 0x1, 0x4000)

    ChrTalk(
        0xFE,
        (
            "哦，怎么样了。\x01",
            "和普罗梅笛先生取得联系了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F唔～嗯，是的……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔告诉了他们\x01",
            "普罗梅笛已经不是运输车的管理员的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x101,
        "#000F……就是这样的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么会这样。\x01",
            "既然这样，真是抱歉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，果然还是要\x01",
            "亲自去把零件给取回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "给你们俩添了不少麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也罢，自己的事情\x01",
            "还是只有靠自己来做了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那就再见了，\x01",
            "到亚尔摩的路上要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F64")

    label("loc_E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_EBD")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    ClearChrFlags(0x9, 0x10)

    ChrTalk(
        0xFE,
        (
            "唔～唔，除了引擎故障，\x01",
            "实在想不出什么别的原因啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只好再全部\x01",
            "重新检查一下了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F61")

    label("loc_EBD")

    TalkBegin(0xFE)
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "如果你们有空的话，\x01",
            "请帮忙联络一下普罗梅笛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他应该一直都在中央工房\x01",
            "三楼的设计室里面。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F61")

    TalkEnd(0xFE)

    label("loc_F64")

    Return()

    # Function_4_B9A end

    def Function_5_F65(): pass

    label("Function_5_F65")

    OP_20(0x5DC)
    OP_1B(0x1, 0x0, 0xFFFF)
    Return()

    # Function_5_F65 end

    def Function_6_F70(): pass

    label("Function_6_F70")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCD")

    ChrTalk(
        0x106,
        (
            "#050F……方向走反了。\x02\x03",
            "总之现在还是回蔡斯吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1027")

    label("loc_FCD")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(
        0x106,
        (
            "#050F喂，方向走反了。\x02\x03",
            "总之现在赶快回蔡斯吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1027")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_6_F70 end

    def Function_7_1043(): pass

    label("Function_7_1043")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　红莲之塔\x01",
            "※魔兽较多，请注意！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_1043 end

    def Function_8_10A1(): pass

    label("Function_8_10A1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1275")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119F")
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, -3130, 1500, -10750, 320)
    TurnDirection(0x15, 0x0, 0)

    def lambda_10F0():
        OP_8F(0xFE, 0xFFFFF3C6, 0x3E8, 0xFFFFD602, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10F0)

    def lambda_110B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_110B)
    ClearChrFlags(0x15, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1154")
    Battle(0x357, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1161")

    label("loc_1154")

    Battle(0x217, 0x0, 0x0, 0x0, 0xFF)

    label("loc_1161")

    SetChrFlags(0x15, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_117A"),
        (2, "loc_118C"),
        (1, "loc_119C"),
        (SWITCH_DEFAULT, "loc_119F"),
    )


    label("loc_117A")

    OP_A2(0x5A0)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_119F")

    label("loc_118C")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_119C")

    OP_B4(0x0)
    Return()

    label("loc_119F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x130, 1)"), scpexpr(EXPR_END)), "loc_11F8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "黑色手镯\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x59F)
    Jump("loc_1272")

    label("loc_11F8")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "黑色手镯\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "黑色手镯\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_1272")

    Jump("loc_12B0")

    label("loc_1275")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x92)

    label("loc_12B0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_10A1 end

    def Function_9_12BE(): pass

    label("Function_9_12BE")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡中。\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (1, "loc_13B6"),
        (SWITCH_DEFAULT, "loc_1450"),
    )


    label("loc_13B6")

    Fade(1000)
    SetChrPos(0x0, -26250, -10, -14890, 192)
    SetChrPos(0x1, -26250, -10, -14890, 192)
    SetChrPos(0x2, -26250, -10, -14890, 192)
    SetChrPos(0x3, -26250, -10, -14890, 192)
    SetChrPos(0x4, -26250, -10, -14890, 192)
    SetChrPos(0x5, -26250, -10, -14890, 192)
    SetChrPos(0x6, -26250, -10, -14890, 192)
    SetChrPos(0x7, -26250, -10, -14890, 192)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_1450")

    Battle(0x3FE, 0x0, 0x0, 0x0, 0xFF)
    SetChrPos(0x0, -26250, -10, -14890, 192)
    SetChrPos(0x1, -26250, -10, -14890, 192)
    SetChrPos(0x2, -26250, -10, -14890, 192)
    SetChrPos(0x3, -26250, -10, -14890, 192)
    SetChrPos(0x4, -26250, -10, -14890, 192)
    SetChrPos(0x5, -26250, -10, -14890, 192)
    SetChrPos(0x6, -26250, -10, -14890, 192)
    SetChrPos(0x7, -26250, -10, -14890, 192)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_14FE"),
        (1, "loc_1501"),
        (SWITCH_DEFAULT, "loc_1504"),
    )


    label("loc_14FE")

    EventEnd(0x0)
    Return()

    label("loc_1501")

    OP_B4(0x0)
    Return()

    label("loc_1504")

    EventBegin(0x1)
    SetChrFlags(0x16, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "成功消灭了托兰特平原道中被通缉的魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x32, 0x4, 0x10)
    OP_28(0x32, 0x1, 0x1)
    OP_A2(0x5C9)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_9_12BE end

    SaveToFile()

Try(main)
