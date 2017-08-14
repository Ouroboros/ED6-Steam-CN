from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60020",
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
        '朵洛希',                               # 9
        '魔兽',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '魔兽',                                 # 13
        '魔兽',                                 # 14
        '东方打扮的男人',                       # 15
        '蔡斯方向',                             # 16
        '亚尔摩村方向',                         # 17
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
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT09/CH10060 ._CH',             # 01
        'ED6_DT09/CH10061 ._CH',             # 02
        'ED6_DT09/CH10063 ._CH',             # 03
        'ED6_DT07/CH00100 ._CH',             # 04
        'ED6_DT07/CH00101 ._CH',             # 05
        'ED6_DT07/CH00102 ._CH',             # 06
        'ED6_DT07/CH00110 ._CH',             # 07
        'ED6_DT07/CH00111 ._CH',             # 08
        'ED6_DT07/CH00112 ._CH',             # 09
        'ED6_DT07/CH00070 ._CH',             # 0A
        'ED6_DT09/CH10610 ._CH',             # 0B
        'ED6_DT09/CH10611 ._CH',             # 0C
        'ED6_DT09/CH10080 ._CH',             # 0D
        'ED6_DT09/CH10081 ._CH',             # 0E
        'ED6_DT09/CH10120 ._CH',             # 0F
        'ED6_DT09/CH10121 ._CH',             # 10
        'ED6_DT09/CH10140 ._CH',             # 11
        'ED6_DT09/CH10141 ._CH',             # 12
        'ED6_DT09/CH10620 ._CH',             # 13
        'ED6_DT09/CH10621 ._CH',             # 14
        'ED6_DT09/CH10600 ._CH',             # 15
        'ED6_DT09/CH10601 ._CH',             # 16
        'ED6_DT09/CH10400 ._CH',             # 17
        'ED6_DT09/CH10401 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT09/CH10060P._CP',             # 01
        'ED6_DT09/CH10061P._CP',             # 02
        'ED6_DT09/CH10063P._CP',             # 03
        'ED6_DT07/CH00100P._CP',             # 04
        'ED6_DT07/CH00101P._CP',             # 05
        'ED6_DT07/CH00102P._CP',             # 06
        'ED6_DT07/CH00110P._CP',             # 07
        'ED6_DT07/CH00111P._CP',             # 08
        'ED6_DT07/CH00112P._CP',             # 09
        'ED6_DT07/CH00070P._CP',             # 0A
        'ED6_DT09/CH10610P._CP',             # 0B
        'ED6_DT09/CH10611P._CP',             # 0C
        'ED6_DT09/CH10080P._CP',             # 0D
        'ED6_DT09/CH10081P._CP',             # 0E
        'ED6_DT09/CH10120P._CP',             # 0F
        'ED6_DT09/CH10121P._CP',             # 10
        'ED6_DT09/CH10140P._CP',             # 11
        'ED6_DT09/CH10141P._CP',             # 12
        'ED6_DT09/CH10620P._CP',             # 13
        'ED6_DT09/CH10621P._CP',             # 14
        'ED6_DT09/CH10600P._CP',             # 15
        'ED6_DT09/CH10601P._CP',             # 16
        'ED6_DT09/CH10400P._CP',             # 17
        'ED6_DT09/CH10401P._CP',             # 18
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -21960,
        Z                   = 0,
        Y                   = 68390,
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
        X                   = 68320,
        Z                   = 0,
        Y                   = -37930,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 31840,
        Z                   = -140,
        Y                   = -14910,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x211,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21310,
        Z                   = 20,
        Y                   = 1100,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x211,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6650,
        Z                   = 10,
        Y                   = 6470,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7960,
        Z                   = -70,
        Y                   = 22900,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7300,
        Z                   = 80,
        Y                   = -13910,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8220,
        Z                   = 70,
        Y                   = -25600,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18960,
        Z                   = 10,
        Y                   = -47120,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19200,
        Z                   = 50,
        Y                   = -40070,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2840,
        Z                   = 20,
        Y                   = -43880,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -23970,
        Z                   = -60,
        Y                   = -56200,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -47630,
        Z                   = 40,
        Y                   = -38230,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -41100,
        Z                   = 30,
        Y                   = -42080,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -46340,
        Z                   = -10,
        Y                   = -47090,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39960,
        Z                   = -50,
        Y                   = -46350,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35370,
        Z                   = 60,
        Y                   = -38180,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39680,
        Z                   = -30,
        Y                   = -43880,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31310,
        Z                   = -20,
        Y                   = -44150,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -37830,
        Z                   = -40,
        Y                   = -49270,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20630,
        Z                   = -50,
        Y                   = -21460,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x213,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -6340,
        Z                   = -20,
        Y                   = 12260,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -9790,
        Z                   = 30,
        Y                   = -7150,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -7920,
        Z                   = -70,
        Y                   = -27310,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22580,
        Z                   = 10,
        Y                   = 23060,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35830,
        Z                   = 30,
        Y                   = 26470,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31840,
        Z                   = -140,
        Y                   = -14910,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x351,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21310,
        Z                   = 20,
        Y                   = 1100,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x351,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6650,
        Z                   = 10,
        Y                   = 6470,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7960,
        Z                   = -70,
        Y                   = 22900,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7300,
        Z                   = 80,
        Y                   = -13910,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8220,
        Z                   = 70,
        Y                   = -25600,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18960,
        Z                   = 10,
        Y                   = -47120,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19200,
        Z                   = 50,
        Y                   = -40070,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2840,
        Z                   = 20,
        Y                   = -43880,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -23970,
        Z                   = -60,
        Y                   = -56200,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -47630,
        Z                   = 40,
        Y                   = -38230,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -41100,
        Z                   = 30,
        Y                   = -42080,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -46340,
        Z                   = -10,
        Y                   = -47090,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39960,
        Z                   = -50,
        Y                   = -46350,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35370,
        Z                   = 60,
        Y                   = -38180,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39680,
        Z                   = -30,
        Y                   = -43880,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31310,
        Z                   = -20,
        Y                   = -44150,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -37830,
        Z                   = -40,
        Y                   = -49270,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20630,
        Z                   = -50,
        Y                   = -21460,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x353,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -6340,
        Z                   = -20,
        Y                   = 12260,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -9790,
        Z                   = 30,
        Y                   = -7150,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -7920,
        Z                   = -70,
        Y                   = -27310,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22580,
        Z                   = 10,
        Y                   = 23060,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35830,
        Z                   = 30,
        Y                   = 26470,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -47070,
        Y                   = -2000,
        Z                   = 850,
        Range               = 5000,
        Unknown_10          = 0x3A98,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -26870,
        Y                   = -1000,
        Z                   = 40570,
        Range               = -17040,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x94DE,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = 36090,
        TriggerZ            = -130,
        TriggerY            = -4970,
        TriggerRange        = 1000,
        ActorX              = 36580,
        ActorZ              = 1370,
        ActorY              = -4390,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -43660,
        TriggerZ            = -50,
        TriggerY            = -54700,
        TriggerRange        = 1000,
        ActorX              = -44130,
        ActorZ              = 1450,
        ActorY              = -55170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21630,
        TriggerZ            = -10,
        TriggerY            = 8540,
        TriggerRange        = 1000,
        ActorX              = -21750,
        ActorZ              = 1490,
        ActorY              = 7880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_89E",          # 00, 0
        "Function_1_8C1",          # 01, 1
        "Function_2_A3F",          # 02, 2
        "Function_3_A72",          # 03, 3
        "Function_4_C7F",          # 04, 4
        "Function_5_212F",         # 05, 5
        "Function_6_2CC0",         # 06, 6
        "Function_7_2E23",         # 07, 7
        "Function_8_2F5A",         # 08, 8
    )


    def Function_0_89E(): pass

    label("Function_0_89E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_8AA"),
        (SWITCH_DEFAULT, "loc_8C0"),
    )


    label("loc_8AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8BD")
    OP_A2(0x521)
    Event(0, 3)

    label("loc_8BD")

    Jump("loc_8C0")

    label("loc_8C0")

    Return()

    # Function_0_89E end

    def Function_1_8C1(): pass

    label("Function_1_8C1")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x3002E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EB")
    OP_B1("R3101_y")
    Jump("loc_8F4")

    label("loc_8EB")

    OP_B1("R3101_n")

    label("loc_8F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97B")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
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
    Jump("loc_9F3")

    label("loc_97B")

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
    SetChrFlags(0x3A, 0x80)
    SetChrFlags(0x3B, 0x80)
    SetChrFlags(0x3C, 0x80)
    SetChrFlags(0x3D, 0x80)
    SetChrFlags(0x3E, 0x80)
    SetChrFlags(0x3F, 0x80)
    SetChrFlags(0x40, 0x80)
    SetChrFlags(0x41, 0x80)

    label("loc_9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A05")
    OP_6F(0x0, 0)
    Jump("loc_A0C")

    label("loc_A05")

    OP_6F(0x0, 60)

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1E")
    OP_6F(0x2, 0)
    Jump("loc_A25")

    label("loc_A1E")

    OP_6F(0x2, 60)

    label("loc_A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A37")
    OP_6F(0x1, 0)
    Jump("loc_A3E")

    label("loc_A37")

    OP_6F(0x1, 60)

    label("loc_A3E")

    Return()

    # Function_1_8C1 end

    def Function_2_A3F(): pass

    label("Function_2_A3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A71")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A65")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_A6E")

    label("loc_A65")

    OP_99(0xFE, 0x0, 0x7, 0x578)

    label("loc_A6E")

    Jump("Function_2_A3F")

    label("loc_A71")

    Return()

    # Function_2_A3F end

    def Function_3_A72(): pass

    label("Function_3_A72")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(47020, 0, -37820, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(89000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 46440, 0, -37370, 135)
    SetChrPos(0x102, 47530, 0, -38220, 315)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002F对了……\x02\x03",
            "托兰特平原道那么大，\x01",
            "我们要从哪里找起才好呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F这个嘛……\x01",
            "因为那个客人是要找景色漂亮的场所。\x02\x03",
            "#012F所以很有可能去了\x01",
            "铺设了砖块的大路以外的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F糟糕～……\x01",
            "那不是更危险了嘛。\x02\x03",
            "#002F不管了！\x01",
            "赶紧找到，然后带她回来！\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x40, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_3_A72 end

    def Function_4_C7F(): pass

    label("Function_4_C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_212E")
    OP_A2(0x522)
    OP_28(0x40, 0x1, 0x100)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -46310, 110, 840, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, -47620, -30, -2150, 0)
    SetChrPos(0xA, -45450, -50, -2620, 0)
    SetChrPos(0xB, -44530, 40, -1070, 0)
    SetChrPos(0xC, -42950, 40, 330, 0)
    SetChrPos(0xD, -43940, 10, 2780, 0)
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0xA, 0x8, 0)
    TurnDirection(0xB, 0x8, 0)
    TurnDirection(0xC, 0x8, 0)
    TurnDirection(0xD, 0x8, 0)
    TurnDirection(0x8, 0xB, 0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)

    NpcTalk(
        0x8,
        "女孩的声音",
        (
            "呜～哇……！\x01",
            "讨厌讨厌，救命啦～～～！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x101,
        "#002F刚刚的声音是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F嗯，很近了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "女孩的声音",
        (
            "女神啊～！\x01",
            "爸爸，妈妈～！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "女孩的声音",
        (
            "奈尔前辈～！\x01",
            "快来救救我呀～～！\x02",
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
        "#509F这、这好像是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F果然不出我所料。\x01",
            "……我们赶快上吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Sleep(100)
    Fade(1000)
    OP_6D(-46630, 80, 1280, 0)
    OP_6C(0, 0)
    OP_B7(0xF, 0x1)
    AddParty(0xF, 0xFF)
    SetChrFlags(0x110, 0x8)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    OP_0D()
    OP_21()
    OP_1D(0x51)
    Sleep(500)
    OP_22(0x193, 0x0, 0x64)

    ChrTalk(
        0xB,
        "……嗷呜呜呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#154F#1P各、各位狗大哥……\x01",
            "我们稍微先商量一下行吗？\x02\x03",
            "我、我可是\x01",
            "一点儿也不好吃的哦～\x02\x03",
            "我每天睡１２个小时以上，\x01",
            "吃的都是些蔬菜水果，\x01",
            "而且皮肤也很光滑……\x02\x03",
            "#153F……哎呀，我怎么反而\x01",
            "说得自己又健康又美味的呢！？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x193, 0x0, 0x64)

    ChrTalk(
        0xB,
        "嗷呜呜呜……！\x02",
    )

    CloseMessageWindow()

    def lambda_108D():

        label("loc_108D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_108D")

    QueueWorkItem2(0x9, 2, lambda_108D)

    def lambda_109E():

        label("loc_109E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_109E")

    QueueWorkItem2(0xA, 1, lambda_109E)

    def lambda_10AF():

        label("loc_10AF")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_10AF")

    QueueWorkItem2(0xB, 1, lambda_10AF)

    def lambda_10C0():

        label("loc_10C0")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_10C0")

    QueueWorkItem2(0xC, 1, lambda_10C0)

    def lambda_10D1():

        label("loc_10D1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_10D1")

    QueueWorkItem2(0xD, 2, lambda_10D1)

    def lambda_10E2():
        OP_6D(-48670, -60, 3500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10E2)
    SetChrChipByIndex(0xB, 2)

    def lambda_10FF():
        OP_8E(0xFE, 0xFFFF4C82, 0x64, 0x1CC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_10FF)
    Sleep(300)
    SetChrChipByIndex(0x9, 2)

    def lambda_1124():
        OP_8F(0xFE, 0xFFFF3D82, 0x1E, 0x140, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1124)
    Sleep(100)
    SetChrChipByIndex(0xD, 2)

    def lambda_1149():
        OP_8F(0xFE, 0xFFFF4A70, 0xFFFFFFE2, 0x1072, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1149)
    Sleep(200)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_117B():
        OP_8F(0x8, 0xFFFF3F80, 0xFFFFFFBA, 0xD0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_117B)
    Sleep(500)
    SetChrChipByIndex(0xA, 2)

    def lambda_11A0():
        OP_8E(0xFE, 0xFFFF4458, 0x3C, 0x96, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_11A0)
    Sleep(300)
    SetChrChipByIndex(0xC, 2)

    def lambda_11C5():
        OP_8E(0xFE, 0xFFFF4D2C, 0x0, 0xA50, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_11C5)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 1)
    WaitChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 1)
    WaitChrThread(0xB, 0x2)
    SetChrChipByIndex(0xB, 1)
    WaitChrThread(0xA, 0x2)
    SetChrChipByIndex(0xA, 1)
    WaitChrThread(0xC, 0x2)
    SetChrChipByIndex(0xC, 1)

    ChrTalk(
        0x8,
        (
            "#152F#1P呜～呜。\x01",
            "早知道会这样，\x01",
            "就应该预支薪水大吃特吃的啦！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 8)
    SetChrChipByIndex(0xC, 1)
    SetChrPos(0x101, -44480, -70, -4400, 0)
    SetChrPos(0x102, -40040, 10, -840, 0)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    Sleep(100)

    def lambda_12D2():
        OP_6D(-47620, 30, 2760, 2500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12D2)
    SetChrChipByIndex(0x101, 6)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_12F4():
        OP_99(0x101, 0x0, 0xC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_12F4)

    def lambda_1304():
        OP_8E(0xFE, 0xFFFF4CDC, 0x32, 0xFFFFFCCC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1304)

    def lambda_131F():
        OP_8E(0xFE, 0xFFFF4F16, 0x5A, 0x1AE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_131F)
    WaitChrThread(0x101, 0x1)

    def lambda_133F():

        label("loc_133F")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_133F")

    QueueWorkItem2(0x101, 2, lambda_133F)

    def lambda_1350():
        OP_96(0xFE, 0xFFFF45FC, 0xFFFFFFE2, 0xAC8, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1350)
    Sleep(50)
    OP_44(0xB, 0xFF)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x1000)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    PlayEffect(0x8, 0xFF, 0xB, 0, 2000, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_13C0():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0xFA0, 0x1F40)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13C0)
    Sleep(50)

    def lambda_13E3():

        label("loc_13E3")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_13E3")

    QueueWorkItem2(0xC, 2, lambda_13E3)

    def lambda_13F4():

        label("loc_13F4")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_13F4")

    QueueWorkItem2(0xD, 2, lambda_13F4)

    def lambda_1405():
        OP_8F(0xFE, 0xFFFF5286, 0xA, 0xA82, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1405)

    def lambda_1420():
        OP_8F(0xFE, 0xFFFF4B9C, 0x0, 0x1554, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1420)
    SetChrChipByIndex(0x102, 9)
    PlayEffect(0x12, 0xFF, 0x102, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_1475():
        OP_99(0x102, 0x0, 0xC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1475)

    def lambda_1485():
        OP_96(0xFE, 0xFFFF4444, 0x32, 0x5A0, 0xBB8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1485)
    Sleep(350)
    OP_22(0x1F5, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xB, 0, 1000, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_14E2():
        OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14E2)
    OP_8F(0xB, 0xFFFF487C, 0x64, 0x352, 0x3A98, 0x0)

    def lambda_1508():

        label("loc_1508")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_1508")

    QueueWorkItem2(0x102, 2, lambda_1508)

    def lambda_1519():

        label("loc_1519")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1519")

    QueueWorkItem2(0x9, 2, lambda_1519)

    def lambda_152A():

        label("loc_152A")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_152A")

    QueueWorkItem2(0xA, 2, lambda_152A)

    def lambda_153B():
        OP_8F(0xFE, 0xFFFF3BC0, 0x1E, 0xFFFFFDBC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_153B)

    def lambda_1556():
        OP_8F(0xFE, 0xFFFF4548, 0xFFFFFFEC, 0xFFFFFB78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1556)
    OP_95(0xB, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0xBB8)
    Sleep(2000)

    ChrTalk(
        0x8,
        (
            "#153F哈……\x01",
            "你、你们是～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F呼……\x01",
            "果然不出所料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F朵洛希小姐，\x01",
            "已经不用担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#155F…………………………\x01",
            "……你们，是什么人来着？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F……（晕倒）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F……我们是游击士协会的\x01",
            "艾丝蒂尔·布莱特和约修亚·布莱特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#151F哦呵呵，开玩笑的啦。\x02\x03",
            "小艾、小约。\x01",
            "能在这里碰面，我们真是有缘呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F真、真是受不了她……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#016F艾丝蒂尔，来了！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 2)

    def lambda_1749():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1749)
    SetChrChipByIndex(0xC, 2)

    def lambda_1764():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1764)
    Sleep(50)
    SetChrChipByIndex(0xA, 2)

    def lambda_1784():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1784)
    SetChrChipByIndex(0xD, 2)

    def lambda_179F():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_179F)
    Sleep(200)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    Battle(0x3A5, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_17E1"),
        (SWITCH_DEFAULT, "loc_17E4"),
    )


    label("loc_17E1")

    OP_B4(0x0)
    Return()

    label("loc_17E4")

    EventBegin(0x0)
    OP_6D(-48280, -30, 2740, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x110, 0x8)
    SetChrPos(0x110, -51180, 0, 4520, 135)
    SetChrPos(0x101, -47620, -30, 2760, 90)
    SetChrPos(0x102, -48060, 50, 1440, 225)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#006F呼……\x01",
            "总算是收拾它们了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)
    SetChrChipByIndex(0x101, 65535)

    ChrTalk(
        0x102,
        "#012F艾丝蒂尔，你发现了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F嗯……\x01",
            "是袭击山顶关所的魔兽吧。\x02\x03",
            "为什么会在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#151F哇～厉害厉害。\x01",
            "真不愧是游击士呢～～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_19AD():

        label("loc_19AD")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_19AD")

    QueueWorkItem2(0x101, 1, lambda_19AD)

    def lambda_19BE():

        label("loc_19BE")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_19BE")

    QueueWorkItem2(0x102, 1, lambda_19BE)

    def lambda_19CF():
        OP_6B(2690, 2300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_19CF)
    OP_8E(0x110, 0xFFFF4106, 0xFFFFFFE2, 0xA28, 0xBB8, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x110,
        (
            "#151F我们好久不见啦～～\x01",
            "小艾，小约。\x02\x03",
            "真没想到会在\x01",
            "这么特别的地方碰上你们～\x02\x03",
            "#155F啊～～\x01",
            "难道这就是所谓命运的重逢吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F是厄运吧，厄运……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，朵洛希小姐。\x02\x03",
            "你就是那个\x01",
            "住在亚尔摩旅馆的客人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#153F是啊……\x01",
            "咦～小约你是怎么知道的？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们向朵洛希说明了\x01",
            "亚尔摩旅馆的老板娘委托保护客人的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x110,
        (
            "#151F啊，是这样啊～\x01",
            "你们还真是辛苦了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F什～么～呀，\x01",
            "别说得好像事不关己似的。\x02\x03",
            "#000F话说回来，\x01",
            "你来街道外面到底想要干什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#151F嘻嘻嘻……\x01",
            "这还不知道吗～？\x02\x03",
            "哦呵呵呵，\x01",
            "小艾的洞察力还是不够呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#150F公布答案～我是来找\x01",
            "用在这次特辑上的照片素材～的哦。\x02\x03",
            "对了对了，\x01",
            "还要顺便完成奈尔前辈给我的作业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F原来如此，是为了工作啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F就算是这样，\x01",
            "也不用在这种地方找素材啊……\x02\x03",
            "啊啊，真是的～\x01",
            "总觉得对你讲道理比战斗还要累人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#154F你不要紧吧～小艾？\x02\x03",
            "别生气别生气，小艾是最乖的了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#3S害我们这么累还想逃避责任吗！\x01",
            "别说得那么顺理成章的！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F（还真是少见啊……\x01",
            "竟然有人可以让艾丝蒂尔如此没辙。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F好了，艾丝蒂尔。\x01",
            "总之先回村子去吧？\x02\x03",
            "导力泵的修理\x01",
            "也应该差不多结束了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唉唉……是、是啊……\x02\x03",
            "#509F听到了没有……\x01",
            "朵洛希也要一起回去哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        "#154F咦～我还想拍照片呢～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#3S一·起·回·去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        "#152F小艾……好吓人哦……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    EventEnd(0x0)

    label("loc_212E")

    Return()

    # Function_4_C7F end

    def Function_5_212F(): pass

    label("Function_5_212F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2911")
    OP_A2(0x52A)
    EventBegin(0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -21840, 0, 52760, 180)

    NpcTalk(
        0xE,
        "男人的声音",
        "哦哦，你们来得正好。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x110, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(-22010, 0, 41300, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -21580, 0, 38890, 0)
    SetChrPos(0x102, -22680, 0, 38930, 0)
    SetChrPos(0x107, -21390, 0, 37530, 0)
    SetChrPos(0x110, -22380, 0, 37650, 0)

    def lambda_224F():

        label("loc_224F")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_224F")

    QueueWorkItem2(0x101, 2, lambda_224F)

    def lambda_2260():

        label("loc_2260")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2260")

    QueueWorkItem2(0x102, 2, lambda_2260)

    def lambda_2271():

        label("loc_2271")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2271")

    QueueWorkItem2(0x107, 2, lambda_2271)

    def lambda_2282():

        label("loc_2282")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2282")

    QueueWorkItem2(0x110, 2, lambda_2282)
    OP_0D()
    OP_8E(0xE, 0xFFFFAA10, 0x0, 0xA528, 0xFA0, 0x0)

    ChrTalk(
        0xE,
        (
            "#070F哟，各位小姐，\x01",
            "有样东西想请问一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F哇，好高大的叔叔啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        "#153F哇哇～～熊、熊先生吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#074F熊……咳咳，也罢了。\x02\x03",
            "#070F我不是什么坏人，\x01",
            "只是想问个路而已。\x02\x03",
            "你们知道那个\x01",
            "叫亚尔摩的温泉乡在哪吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F哦，你说亚尔摩村啊～\x01",
            "那地方正好在我们刚刚走来的方向。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，再走一段路就到了。\x01",
            "请从这里沿着大路一直向南走吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#071F哦哦，是啊。\x01",
            "多谢你们指路了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#073F哦？你们……\x02\x03",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#073F嗯，原来如此。\x02\x03",
            "你们难道是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们有什么奇怪的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#070F啊，不好意思。\x01",
            "没什么大不了的事。\x02\x03",
            "那么再见了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_254D():
        OP_6C(0, 2500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_254D)

    def lambda_255D():
        OP_6D(-22090, 0, 38340, 2500)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_255D)

    def lambda_2575():
        OP_8E(0xFE, 0xFFFFB12C, 0x0, 0x9F9C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2575)
    WaitChrThread(0xE, 0x1)
    OP_8E(0xE, 0xFFFFB12C, 0x0, 0x6590, 0xFA0, 0x0)
    SetChrFlags(0xE, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x110, 0xFF)

    ChrTalk(
        0x101,
        (
            "#505F总觉得有种外国人的感觉呢。\x02\x03",
            "#505F穿着东方风格的服装，\x01",
            "刚才那大叔应该是从外国来的吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2625():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2625)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F蔡斯地区的东面是\x01",
            "与卡尔瓦德共和国接壤的地方，\x01",
            "那里有一座名为『沃尔费堡垒』的关所。\x02\x03",
            "说不定他就是从那边过来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x110, 0, 600)
    OP_8C(0x107, 0, 600)

    ChrTalk(
        0x107,
        (
            "#060F嗯，我也觉得是这样。\x02\x03",
            "毛婆婆也是东方人呢。\x01",
            "反正蔡斯地区一直都住着\x01",
            "很多从共和国那边过来的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，的确是啊。\x01",
            "说起来雾香姐也是东方人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#151F不过不过～\x01",
            "那个熊先生真的好高大啊～\x02\x03",
            "吓了我一大跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F呵呵……\x01",
            "也真的很像熊那样魁梧呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F身材的确就像熊那样魁梧，\x01",
            "不过，可没有熊那样简单哦。\x02\x03",
            "看得出他有着相当深厚的武术造诣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F姐姐看得出来吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F那当然啦～\x01",
            "好歹我也是个武术家嘛。\x02\x03",
            "那个大叔不仅身材高大，\x01",
            "而且体格也经过了相当的锻炼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊……\x01",
            "走起路来沉稳有力、毫不拖泥带水。\x02\x03",
            "说不定和艾丝蒂尔说的一样，\x01",
            "那位先生真的是位武术高人。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_2CBF")

    label("loc_2911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CBF")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B0F")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A2A")

    ChrTalk(
        0x101,
        (
            "#002F唔～找不到啊。\x02\x03",
            "我觉得不可能往再远的地方去了啊……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F确实，根据时间来推算\x01",
            "应该不会走得这么远。\x02\x03",
            "还是在附近的平原再仔细找找吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F嗯，就这样吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B0C")

    label("loc_2A2A")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F喂，约修亚。\x02\x03",
            "我觉得不可能往再远的地方去了啊……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F确实，根据时间来推算\x01",
            "应该不会走得这么远。\x02\x03",
            "还是在附近的平原再仔细找找吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯，就这样吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2B0C")

    Jump("loc_2B8A")

    label("loc_2B0F")


    def lambda_2B15():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B15)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F根据时间来推算\x01",
            "应该不会走得这么远。\x02\x03",
            "还是在附近的平原再仔细找找吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8A")

    Jump("loc_2CA4")

    label("loc_2B8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3B")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，\x01",
            "赶快回亚尔摩村吧。\x02\x03",
            "旅馆的人们肯定还在担心呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F啊，说得对。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA4")

    label("loc_2C3B")


    ChrTalk(
        0x102,
        (
            "#010F这边是蔡斯啊……\x02\x03",
            "旅馆的人们肯定还在担心呢。\x01",
            "还是赶快回亚尔摩村吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA4")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_2CBF")

    Return()

    # Function_5_212F end

    def Function_6_2CC0(): pass

    label("Function_6_2CC0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_2D37")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "大回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x59B)
    Jump("loc_2DAF")

    label("loc_2D37")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "大回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "大回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_2DAF")

    Jump("loc_2E15")

    label("loc_2DB2")

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
    OP_83(0xF, 0x8F)

    label("loc_2E15")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_2CC0 end

    def Function_7_2E23(): pass

    label("Function_7_2E23")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F15")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_2E9A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "大回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x59C)
    Jump("loc_2F12")

    label("loc_2E9A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "大回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "大回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_2F12")

    Jump("loc_2F4C")

    label("loc_2F15")

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
    OP_83(0xF, 0x90)

    label("loc_2F4C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_2E23 end

    def Function_8_2F5A(): pass

    label("Function_8_2F5A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3119")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3058")
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, -44130, 1500, -55170, 320)
    TurnDirection(0x11, 0x0, 0)

    def lambda_2FA9():
        OP_8F(0xFE, 0xFFFF539E, 0x3E8, 0xFFFF287E, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2FA9)

    def lambda_2FC4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2FC4)
    ClearChrFlags(0x11, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_300D")
    Battle(0x356, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_301A")

    label("loc_300D")

    Battle(0x216, 0x0, 0x0, 0x0, 0xFF)

    label("loc_301A")

    SetChrFlags(0x11, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3033"),
        (2, "loc_3045"),
        (1, "loc_3055"),
        (SWITCH_DEFAULT, "loc_3058"),
    )


    label("loc_3033")

    OP_A2(0x59E)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_3058")

    label("loc_3045")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_3055")

    OP_B4(0x0)
    Return()

    label("loc_3058")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x26C, 1)"), scpexpr(EXPR_END)), "loc_30AA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "命中３\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x59D)
    Jump("loc_3116")

    label("loc_30AA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "命中３\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "命中３\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_3116")

    Jump("loc_3194")

    label("loc_3119")

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
    OP_83(0xF, 0x91)

    label("loc_3194")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_2F5A end

    SaveToFile()

Try(main)
