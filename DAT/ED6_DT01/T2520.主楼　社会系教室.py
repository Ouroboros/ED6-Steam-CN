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
        'Dean Collins',                         # 9
        'Polly',                                # 10
        'Matron Theresa',                       # 11
        'Daniel',                               # 12
        'Mary',                                 # 13
        'Clem',                                 # 14
        'Sieg',                                 # 15
        'Fauna',                                # 16
        'Mr. Ratio',                            # 17
        'Ms. Wiola',                            # 18
        'Ms. Millia',                           # 19
        'Mr. Effort',                           # 20
        'Rhody',                                # 21
        'Kaden',                                # 22
        'Alice',                                # 23
        'Taylor',                               # 24
        'Purity',                               # 25
        'Logic',                                # 26
        'Argyle',                               # 27
        'Roy',                                  # 28
        'Monika',                               # 29
        'Thelma',                               # 30
        'Richelle',                             # 31
        'Patrick',                              # 32
        'Gerome',                               # 33
        'Nikita',                               # 34
        'Felicity',                             # 35
        'Reina',                                # 36
        'Mayor Maybelle',                       # 37
        'Duke Dunan',                           # 38
        'Butler Phillip',                       # 39
        'Nial',                                 # 40
        'Carna',                                # 41
        'Professor Alba',                       # 42
        'Ciel',                                 # 43
        'Eletta',                               # 44
        'Eva',                                  # 45
        'Seagaro',                              # 46
        'Edel',                                 # 47
        'Portos',                               # 48
        'Noria',                                # 49
        'Liz',                                  # 50
        'Antonio',                              # 51
        'Lila',                                 # 52
        'Mayor Dalmore',                        # 53
        'Visitor',                              # 54
        'Visitor',                              # 55
        'Visitor',                              # 56
        'Visitor',                              # 57
        'Visitor',                              # 58
        'Visitor',                              # 59
        'Visitor',                              # 60
        'Visitor',                              # 61
        'Visitor',                              # 62
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
            "#780FAh, hello there.\x02\x03",
            "First of all, I'd like to say how\x01",
            "relieved I am that the criminals\x01",
            "have been caught.\x02\x03",
            "I'll be waiting for when you turn\x01",
            "your investigations toward your\x01",
            "academic pursuits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1845")

    label("loc_17AF")


    ChrTalk(
        0xFE,
        (
            "#780FThank goodness that the\x01",
            "attackers have been arrested.\x02\x03",
            "I'll be waiting for when you turn\x01",
            "your investigations toward your\x01",
            "academic pursuits.\x02",
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
            "#780FAh, you're here.\x02\x03",
            "I heard about Matron Theresa\x01",
            "and the children.\x02\x03",
            "They certainly didn't deserve this.\x02\x03",
            "What words are there to describe\x01",
            "such a thing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_195B")

    label("loc_18FD")


    ChrTalk(
        0xFE,
        (
            "#780FI heard about Matron Theresa\x01",
            "and her children.\x02\x03",
            "They certainly didn't deserve this.\x02",
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
            "#780FWell, we certainly are in\x01",
            "your debt this time...\x02\x03",
            "The play was magnificent. Joshua's\x01",
            "portrayal of Princess Cecilia was\x01",
            "particularly memorable.\x02\x03",
            "I hope that you'll be able to come\x01",
            "to the campus again, hopefully to\x01",
            "stay for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF7")

    label("loc_1A64")


    ChrTalk(
        0xFE,
        (
            "#780FWell, we certainly are in\x01",
            "your debt this time...\x02\x03",
            "I hope that you'll be able to come\x01",
            "to the campus again, hopefully to\x01",
            "stay for a while.\x02",
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
            "#780FAh, hello there. Everything's been\x01",
            "quite a big success.\x02\x03",
            "I'm looking forward to seeing the\x01",
            "play. I expect it will be a big hit\x01",
            "for the festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C11")

    label("loc_1BAF")


    ChrTalk(
        0xFE,
        (
            "#780FI'm looking forward to seeing the\x01",
            "play. I expect it will be a big hit\x01",
            "for the festival.\x02",
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
            "#781FI've not seen you since last year's\x01",
            "Royal Council, Mayor Dalmore.\x02\x03",
            "Has much changed since then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#661FAs you can see, I'm feeling\x01",
            "quite well. You look to be in\x01",
            "good health, also.\x02\x03",
            "I expect that today will be\x01",
            "quite enjoyable.\x02",
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
            "#781FI'd like to get your input on some\x01",
            "of the school's affairs, if you have\x01",
            "the time.\x02\x03",
            "Though we may be chartered by\x01",
            "the monarchy, it's still important\x01",
            "to hear the local views.\x02",
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
            "#780FDon't worry, I'll make sure you have a place\x01",
            "to stay. And I'm greatly looking forward to\x01",
            "your...erm...'transformation'...\x02\x03",
            "There's also a cafeteria on campus, which\x01",
            "you may use at your leisure. Just relax,\x01",
            "and work hard on the play.\x02",
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
        "Hmm? Did someone need me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Classes just ended, so the students\x01",
            "should be milling about any moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F8A")

    label("loc_1F6B")


    ChrTalk(
        0xF,
        "Hmm? Did someone need me?\x02",
    )

    CloseMessageWindow()

    label("loc_1F8A")

    Jump("loc_2899")

    label("loc_1F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_201D")

    ChrTalk(
        0xF,
        (
            "Ha ha...the festival was a\x01",
            "huge success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I always worry that the people\x01",
            "with children will lose track of\x01",
            "them in the crowd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2899")

    label("loc_201D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_20DA")

    ChrTalk(
        0xF,
        (
            "Success! This is possibly our\x01",
            "best turnout yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Though I do always worry that the people\x01",
            "with children will lose track of them in\x01",
            "the crowd. But so far...no fatalities!\x02",
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
            "The event will be held on the\x01",
            "grounds and in the main building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The play's scheduled to be held\x01",
            "in the auditorium this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The Student Council has set up the\x01",
            "cafeteria as the rest area, so please,\x01",
            "feel free to relax there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2270")

    label("loc_21E4")


    ChrTalk(
        0xF,
        (
            "The event will be held on the\x01",
            "grounds and in the main building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The play's scheduled to be held\x01",
            "in the auditorium this afternoon.\x02",
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
            "Have you finished getting ready?\x01",
            "Tomorrow isn't far away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It looks like we'll have more\x01",
            "attendees tomorrow than\x01",
            "ever before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234E")

    label("loc_230F")


    ChrTalk(
        0xF,
        (
            "Have you finished getting ready?\x01",
            "Tomorrow isn't far away.\x02",
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
            "Ha ha...even with classes done,\x01",
            "it's still extremely busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "It's almost festival time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I hope all of the students are\x01",
            "trying their hardest for this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_244B")

    label("loc_240B")


    ChrTalk(
        0xF,
        (
            "Ha ha...even with classes done,\x01",
            "it's still extremely busy.\x02",
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
        "Oh, hello, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040FPardon me, Fauna...I just got back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Ha ha, welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "If you're looking for the dean,\x01",
            "he just went to his office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "He's been quite worried about you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040FOh, all right. I'll go and see\x01",
            "him now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C5")

    label("loc_255C")


    ChrTalk(
        0xF,
        (
            "If you're looking for the dean,\x01",
            "he just went to his office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "He's been quite worried about you.\x02",
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
            "Hello, Kloe. Are you already done\x01",
            "with your off-campus errands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040FOh, not yet...\x02\x03",
            "I'm sorry, but I still have some\x01",
            "errands left to run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "That's fine. Just take care\x01",
            "of yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C2")

    label("loc_26A0")


    ChrTalk(
        0xF,
        "Take care of yourself, Kloe.\x02",
    )

    CloseMessageWindow()

    label("loc_26C2")

    Jump("loc_2899")

    label("loc_26C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_2744")

    ChrTalk(
        0xF,
        "Oh, did you want a guided tour?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm terribly sorry, but I can't\x01",
            "show you around while class\x01",
            "is in session.\x02",
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
            "Oh, hello, Kloe. Are you back\x01",
            "to stay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040FNo...I'm just showing some folks\x01",
            "around on the way to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I see...well, since this is your\x01",
            "vacation, make sure you let\x01",
            "your hair down and have fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040FI will...thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2899")

    label("loc_2848")


    ChrTalk(
        0xF,
        (
            "Since this is your vacation,\x01",
            "make sure you let your hair\x01",
            "down and have fun.\x02",
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
            "Class may be over, but I still\x01",
            "get questions from my students.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF2")

    label("loc_28EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2964")

    ChrTalk(
        0xFE,
        (
            "Hmmm...my class has done a\x01",
            "fine job on the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They really put a lot of work\x01",
            "into this set.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF2")

    label("loc_2964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_29DA")

    ChrTalk(
        0xFE,
        (
            "The lead roles will be played\x01",
            "by students, will they not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone's even more active\x01",
            "than usual.\x02",
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
            "You kids came from Rolent,\x01",
            "didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm actually from there, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Speaking of which, my parents will\x01",
            "be visiting to attend the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's good that they were invited.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B40")

    label("loc_2AB1")


    ChrTalk(
        0xFE,
        (
            "Ah, yes...I had a chance to\x01",
            "watch the rehearsals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm quite looking forward to\x01",
            "the performance. The, uh,\x01",
            "princess is something else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B40")

    Jump("loc_2BF2")

    label("loc_2B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2BF2")

    ChrTalk(
        0xFE,
        (
            "With the festival coming up, the\x01",
            "kids practically vibrate in their\x01",
            "seats when class is almost out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha...but I suppose there's\x01",
            "nothing to be done about it.\x02",
        )
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
        "Let's see...this problem here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How do you do it?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    Jump("loc_2C8B")

    label("loc_2C59")


    ChrTalk(
        0xFE,
        (
            "Wow, the students here are\x01",
            "really dedicated.\x02",
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
            "Ahh, I'm so bored...I wonder how\x01",
            "much longer it will be until the\x01",
            "play starts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good thing you two seem like\x01",
            "the really reliable sort.\x02",
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
        "Hmmm...my class is fairly low-key...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, I think the research\x01",
            "periodical is pretty plain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it's okay. I'm just glad we\x01",
            "have readers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E0D")

    label("loc_2DDE")


    ChrTalk(
        0xFE,
        "I don't want to lose to Millia's class...\x02",
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
        "Oh, hello, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040FHello, Ms. Wiola.\x02\x03",
            "I'm sorry I missed your class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha...you don't need to worry\x01",
            "about that, dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You did have important business\x01",
            "to attend to, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you stop by the staff room later,\x01",
            "I can give you a printout of the\x01",
            "work you missed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040FYes, ma'am. I will.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FAE")

    label("loc_2F66")


    ChrTalk(
        0xFE,
        (
            "Now, then...I suppose I should get\x01",
            "started on grading these tests.\x02",
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
            "I've been put in charge of writing\x01",
            "up the entrance examinations\x01",
            "for this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I look forward to the challenge.\x02",
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
            "Why is my class doing fortune-\x01",
            "telling and games, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wiola's kids are doing something\x01",
            "far more direct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The students in that class are\x01",
            "impressive...though the same\x01",
            "can't be said for the teacher.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B0")

    label("loc_3136")


    ChrTalk(
        0xFE,
        (
            "Why is my class doing fortune-\x01",
            "telling and games, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wiola's kids are doing something\x01",
            "far more direct.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B0")

    Jump("loc_3506")

    label("loc_31B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3212")

    ChrTalk(
        0xFE,
        (
            "Have you seen the size\x01",
            "of the crowd?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if they're all on vacation.\x02",
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
            "Well, the students will show\x01",
            "everyone the fruits of their\x01",
            "labors tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll do my best to keep my criticisms\x01",
            "to myself...as valid as they may be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3317")

    label("loc_32C7")


    ChrTalk(
        0xFE,
        (
            "Well, the students will show\x01",
            "everyone the fruits of their\x01",
            "labors tomorrow.\x02",
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
            "Everyone tends to slack off in\x01",
            "the lead-up to the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose all the instruction in\x01",
            "the world can't change that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps tomorrow, I'll give the kids a pop quiz.\x01",
            "And just to show them...it will NOT be multiple\x01",
            "choice! Mwa ha ha ha...ha...*ahem*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3506")

    label("loc_343C")


    ChrTalk(
        0xFE,
        (
            "Everyone tends to slack off in the\x01",
            "lead-up to the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps tomorrow, I'll give the kids a pop quiz.\x01",
            "And just to show them...it will NOT be multiple\x01",
            "choice! Mwa ha ha ha...ha...*ahem*\x02",
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
        "I should make my rounds, soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The students are generally\x01",
            "well-behaved enough to not\x01",
            "require me to hover.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3938")

    label("loc_358B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_36F8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_3632")

    ChrTalk(
        0xFE,
        (
            "Ah, thanks for everything you\x01",
            "did yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really have anything\x01",
            "I need to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm just staying here,\x01",
            "in case I'm needed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F5")

    label("loc_3632")


    ChrTalk(
        0xFE,
        (
            "I heard some students talking\x01",
            "yesterday about having seen\x01",
            "monsters in the old building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be making sure everything is\x01",
            "locked up tight before my rounds,\x01",
            "just to be on the safe side.\x02",
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
            "There are three major courses\x01",
            "offered at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of them are important,\x01",
            "but I'm personally in charge\x01",
            "of physical education.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are no classes at the\x01",
            "moment. Perfect time to get\x01",
            "the papers sorted out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3898")

    label("loc_37F0")


    ChrTalk(
        0xFE,
        (
            "All of them are important,\x01",
            "but I'm personally in charge\x01",
            "of physical education.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are no classes at the\x01",
            "moment. Perfect time to get\x01",
            "the papers sorted out.\x02",
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
        "Hey, aren't you students?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Class is in session. You'll need\x01",
            "a pass to go off-campus.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3938")

    label("loc_390E")


    ChrTalk(
        0xFE,
        "You'll need a pass to go off-campus.\x02",
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
            "Ahhh...finally, classes are done\x01",
            "for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Afternoon classes always make\x01",
            "me want to take a nap.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_39C1")


    ChrTalk(
        0xFE,
        (
            "Afternoon classes always make\x01",
            "me want to take a nap.\x02",
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
            "I've been involved in the club's\x01",
            "food stand the whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't have a chance to get\x01",
            "involved in the class project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yep, I'm feeling good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B35")

    label("loc_3AB2")


    ChrTalk(
        0xFE,
        (
            "I've been involved in the club's\x01",
            "food stand the whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't have a chance to get\x01",
            "involved in the class project.\x02",
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
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
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
        "Okay, time for the club activities.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I've GOT to finish this painting today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FB3")

    label("loc_3C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3CB9")

    ChrTalk(
        0x15,
        (
            "Since I'm working on the coffee house,\x01",
            "I've got to push myself! And to do that...\x01",
            "I NEED MORE COFFEEEEEE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "This is pretty tough...\x02",
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
            "Is the guest at that table\x01",
            "a real maid...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D62")

    label("loc_3CFE")


    ChrTalk(
        0x15,
        (
            "Ugh...staying up all night has left\x01",
            "me completely drained. Or is that\x01",
            "the caffeine withdrawal?\x02",
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
            "Whoa! What the hell?!\x01",
            "This is a cappuccino...\x01",
            "I ordered an espresso! Nooooo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I'll never finish up in time\x01",
            "at this rate!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E53")

    label("loc_3DFC")


    ChrTalk(
        0x15,
        "Hmmm...maybe if I work all night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Ahhh...that should give me\x01",
            "plenty of time!\x02",
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
        (
            "Hmm-hmm-hmmmmm... 侓\x01",
            "They've got an awful lot of coffee... 侓\x01",
            "An awful lot of coffee... 侓\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I'm making outfits to wear at\x01",
            "the food stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I've got to really throw myself\x01",
            "into this! And to do that...\x01",
            "I NEED MORE COFFEEEEEE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I love making stuff like this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FB3")

    label("loc_3F7C")


    ChrTalk(
        0x15,
        (
            "I've got to make decorations for\x01",
            "the room, too...\x02",
        )
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
        "Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd be glad to show you to\x01",
            "your seats.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426B")

    label("loc_3FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4057")

    ChrTalk(
        0xFE,
        "Hee hee...isn't this a cute outfit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Kaden's been making a lot of them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_426B")

    label("loc_4057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4131")

    ChrTalk(
        0xFE,
        (
            "He thought we had more time than we actually\x01",
            "do. Thankfully, with enough coffee in him, we\x01",
            "can still make the deadline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So worry not, we'll be ready!\x01",
            "I want this to be the cutest\x01",
            "little place ever!\x02",
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
            "Kaden's really good with his hands,\x01",
            "and if you give him a little coffee,\x01",
            "then he can do just about anything! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I can get him to make\x01",
            "some stuffed dolls next...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426B")

    label("loc_41F5")


    ChrTalk(
        0xFE,
        (
            "Despite the fact that he's appearing\x01",
            "in the play, he still managed to find\x01",
            "the time to make maid outfits for us!\x02",
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
            "I didn't really understand the\x01",
            "lesson in my last class...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Umm...I thought maybe I should\x01",
            "ask some questions, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ms. Millia always goes straight to\x01",
            "the staff room once class is over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_439B")

    label("loc_4350")


    ChrTalk(
        0xFE,
        (
            "Ms. Millia always goes straight to\x01",
            "the staff room once class is over.\x02",
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
            "Everyone in the social studies\x01",
            "class is working on the research\x01",
            "periodical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My class is doing either a tea house or a\x01",
            "haunted house. Not sure which, though,\x01",
            "frankly I think there's cross-over potential.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44F9")

    label("loc_4498")


    ChrTalk(
        0xFE,
        (
            "Everyone in the social studies\x01",
            "class is working on the research\x01",
            "periodical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, wow...\x02",
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
        "Welcome to the Fontana Tea House.\x02",
    )

    CloseMessageWindow()
    Jump("loc_458C")

    label("loc_4531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_458C")

    ChrTalk(
        0xFE,
        (
            "I'm kind of embarrassed to be\x01",
            "dressed like this, but it is for\x01",
            "the festival...\x02",
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
            "Hmm...today's lesson was\x01",
            "very worthwhile.\x02",
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
        "Man, being a senior is rough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand the need to enjoy oneself,\x01",
            "but at the end of the day, I still need to\x01",
            "hand in my research results, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Getting good grades is paramount.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4784")

    label("loc_46AA")


    ChrTalk(
        0xFE,
        (
            "There are a great many alumni\x01",
            "coming, as well as the general\x01",
            "audience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand the need to engage in outside\x01",
            "activities, but at the end of the day, I still\x01",
            "need to hand in my research results, you know?\x02",
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
            "My social studies class has been using various\x01",
            "economic indicators to predict future trends\x01",
            "and we'll be displaying the results here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We also have a collection of materials\x01",
            "summarising the history and development of this\x01",
            "region in a simple, easy to read format.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491F")

    label("loc_48EE")


    ChrTalk(
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
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
            "My social studies class will be\x01",
            "researching various economic\x01",
            "indicators to predict future trends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Reviewing the history and growth\x01",
            "of Ruan should provide useful\x01",
            "data for this project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If any details are missing, you just\x01",
            "have to go with what makes the most\x01",
            "sense from the data available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BB2")

    label("loc_4A90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_4B81")

    ChrTalk(
        0xFE,
        (
            "It may push me past deadline, but I'd\x01",
            "love to get my hands on a copy of 'Ruan\x01",
            "Economics.' Very useful data in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you should happen to see any\x01",
            "of the volumes, would you please\x01",
            "return them to the reference room?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BB2")

    label("loc_4B81")


    ChrTalk(
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
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
            "Hm, I need more research materials\x01",
            "to better substantiate my findings...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't think there's enough time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose I'll just have to do the\x01",
            "best I can with what I have.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CD6")

    label("loc_4C87")


    ChrTalk(
        0xFE,
        (
            "Hmm, I need more research materials\x01",
            "to better substantiate my findings...\x02",
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
            "Hello, Kloe.\x01",
            "So, you've come back to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The preparations for the class\x01",
            "program appear to be coming\x01",
            "along well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How fares the play?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm told the casting has not yet\x01",
            "been finalized, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040FHa ha. That was done some\x01",
            "time ago, Logic.\x02\x03",
            "It's going to be great.\x01",
            "I hope you'll enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, yes, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Then I wish you the best of luck.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E85")

    label("loc_4E63")


    ChrTalk(
        0xFE,
        "I wish you the best of luck.\x02",
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
        "No haunted houses this year?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Too cliched, I guess.\x02",
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
            "Rumor has it the queen's birthday\x01",
            "celebration is going to feature the\x01",
            "biggest competition yet this year!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd love for my Fencing Club\x01",
            "to participate.\x02",
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
            "I'm too busy with classes to do\x01",
            "much with the club, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've been switching off who's\x01",
            "supervising the club shop, so \x01",
            "I was thinking of checking in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50AD")

    label("loc_5032")


    ChrTalk(
        0xFE,
        (
            "In my case, there's a lot of\x01",
            "people to watch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But the more enthusiastic ones\x01",
            "have some pretty sharp questions.\x02",
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
            "I'm an exchange student from the\x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been busy with this year's\x01",
            "research periodical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's eaten up most of my time, actually.\x02",
    )

    CloseMessageWindow()
    Jump("loc_51D7")

    label("loc_5165")


    ChrTalk(
        0xFE,
        (
            "I'm an exchange student from the\x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been busy with this year's\x01",
            "research periodical.\x02",
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
        "Oh, hi, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The class has finished up most\x01",
            "of its setup duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Logic is still at work in the\x01",
            "reference room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52DA")

    label("loc_526E")


    ChrTalk(
        0xFE,
        (
            "The class has finished up most\x01",
            "of its setup duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Logic is still at work in the\x01",
            "reference room.\x02",
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
            "I'll be manning the club's food\x01",
            "stand all afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "So, I need to have fun while I can.\x02",
    )

    CloseMessageWindow()
    Jump("loc_53D5")

    label("loc_5352")


    ChrTalk(
        0xFE,
        (
            "Rhody's in the same club, and he\x01",
            "runs the stand in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll get an idea of how\x01",
            "annoying it can be soon.\x02",
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
            "Ms. Wiola has been yawning\x01",
            "non-stop for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And the pretty lady came, too...\x02",
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
            "Ha ha...today, we're on standby.\x01",
            "We're like...the information desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can explain the social studies\x01",
            "periodical in plainer terms if anyone\x01",
            "asks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5546")

    label("loc_54F3")


    ChrTalk(
        0xFE,
        (
            "We can explain the social studies\x01",
            "periodical in plainer terms if anyone\x01",
            "asks.\x02",
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
        "Oh, hi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm tending the store in the morning,\x01",
            "so I can have fun in the afternoon.\x02",
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
        "Ha ha...I know all about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Gerome did a bang-up job.\x02",
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
            "Huh...I'm having more fun than\x01",
            "I expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had no idea how I'd get it all\x01",
            "done when we came up with the\x01",
            "plans for it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D6")

    label("loc_5698")


    ChrTalk(
        0xFE,
        "*yaaaaawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ugh...so sleepy...\x01",
            "My kingdom for a nap!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56D6")

    Jump("loc_574D")

    label("loc_56D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_574D")

    ChrTalk(
        0xFE,
        (
            "Err...wh-what are my mom and kid\x01",
            "sister doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I told them not to come...\x01",
            "I said I'd be busy.\x02",
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
            "S-Sis? Shouldn't you be...working?!\x01",
            "Is the shop gonna be okay without\x01",
            "you?!\x02",
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
            "In the end, we weren't able to finish\x01",
            "setting up the displays yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow, though, it was all done\x01",
            "when we came back in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We were still in the middle of\x01",
            "working when it was time to\x01",
            "go home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5912")

    label("loc_58A3")


    ChrTalk(
        0xFE,
        (
            "We still weren't done when it was\x01",
            "time to go home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We asked around, but no one\x01",
            "knew who'd done it.\x02",
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
            "Reina and I don't share any classes\x01",
            "or clubs, but we still room together\x01",
            "at the dorm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew...at this rate, it's going\x01",
            "to be difficult to breathe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I should take advantage\x01",
            "of the freedom to enjoy it while\x01",
            "I still can.\x02",
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
        "Okay, general viewing is over...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll go see Felicity in the\x01",
            "shop and torture her...uh, I mean\x01",
            "encourage her.\x02",
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
            "#610FHa ha...this is rather fun.\x02\x03",
            "The play is this afternoon, right?\x01",
            "I'm looking forward to it.\x02",
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
        "#004FMayor Maybelle?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#613FOh! Well, if it isn't Estelle\x01",
            "and Joshua!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FWhat are you doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#611FHa ha...to tell you the truth,\x01",
            "I actually graduated from here.\x02\x03",
            "I always make a point of going\x01",
            "to the campus festival each year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, okay. That's cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#610FBut enough about me. How\x01",
            "have you two been doing?\x02\x03",
            "Are you here on guild business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FHeh heh...well, actually...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle told Mayor Maybelle what had been going on.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0xFE,
        (
            "#613FOh, so you're helping out\x01",
            "with the play?\x02\x03",
            "#611FI've always found them to be\x01",
            "slightly tiresome.\x02\x03",
            "Ha ha...but if you're going to be\x01",
            "on stage, I certainly don't want\x01",
            "to miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F(Ugh...I'd really rather not have\x01",
            "anyone I KNOW in the audience\x01",
            "for this...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EF0")

    label("loc_5E65")


    ChrTalk(
        0xFE,
        (
            "#610FI've always found plays to be\x01",
            "slightly tiresome.\x02\x03",
            "Ha ha...but if you're going to be\x01",
            "on stage, I certainly don't want\x01",
            "to miss it.\x02",
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
            "#220FWell, well...so the play starts\x01",
            "this afternoon.\x02\x03",
            "I can't imagine it will come\x01",
            "anywhere near to the splendor\x01",
            "of Grancel's theater...\x02\x03",
            "But this is official business,\x01",
            "after all. I suppose I will go\x01",
            "see it. If I must.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_607D")

    label("loc_5FF1")


    ChrTalk(
        0xFE,
        (
            "#220FWell, well...so the play starts\x01",
            "this afternoon.\x02\x03",
            "But this is official business,\x01",
            "after all. I suppose I will go\x01",
            "see it. If I must.\x02",
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
            "#220FSo this is the campus which is\x01",
            "funded through the royal coffers.\x02\x03",
            "As the queen's nephew, I ought\x01",
            "to give it a thorough inspection.\x02\x03",
            "#221FHa ha ha...I'm sure that the students\x01",
            "will consider it a great honor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F(Was the old fart even invited?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F(I imagine he was. NOT inviting\x01",
            "him would have just been asking\x01",
            "for trouble...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62D2")

    label("loc_61F3")


    ChrTalk(
        0x25,
        (
            "#220FSo THIS is the campus which is funded through the\x01",
            "royal coffers. Hmmm...I find it somewhat lacking.\x01",
            "They haven't even a single gilded bird feeder.\x02\x03",
            "As the queen's nephew, I ought\x01",
            "to give it a thorough inspection.\x02",
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
            "#720FThe Jenis Royal Academy...it's\x01",
            "as magnificent as I'd expected.\x02\x03",
            "The campus festival is quite\x01",
            "the event, I see.\x02",
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
            "#722FY-Your Excellency, I hate to say\x01",
            "this once more...\x02\x03",
            "But please consider your words\x01",
            "when among the public.\x02",
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
            "#140FAhh, okay. The play starts\x01",
            "this afternoon.\x02\x03",
            "#142FAnd it's based on the old classic,\x01",
            "'Madrigal of the White Magnolia,'\x01",
            "huh?\x02\x03",
            "Sad to say, I'm not so sure that\x01",
            "a bunch of students can pull\x01",
            "that one off...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6572")

    label("loc_64D7")


    ChrTalk(
        0xFE,
        (
            "#142FSo, the show's going to be\x01",
            "'Madrigal of the White Magnolia,'\x01",
            "huh?\x02\x03",
            "Sad to say, I'm not so sure that\x01",
            "a bunch of students can pull\x01",
            "that one off...\x02",
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
        "#000FHey, Carna.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FGood afternoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#830FHi, guys. Jean told me what's\x01",
            "been going on.\x02\x03",
            "So, you're just helping out wherever\x01",
            "you're needed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FHeh heh...more or less.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAre you working as security,\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#830FBasically.\x02\x03",
            "The alumni here tend to be Liberlian\x01",
            "celebrities from all walks of life.\x02\x03",
            "Every year, they're all invited back.\x02\x03",
            "Thus, the need for heightened\x01",
            "security.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_END)), "loc_6783")

    ChrTalk(
        0x102,
        (
            "#010FSpeaking of which, Mayor Maybelle\x01",
            "told us she graduated from here,\x01",
            "also.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67D4")

    label("loc_6783")


    ChrTalk(
        0x101,
        (
            "#000FWow...I wonder who else went here.\x01",
            "The who's who of Liberl, I guess...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67D4")


    ChrTalk(
        0xFE,
        (
            "#830FWell, just leave security up to\x01",
            "me and you two can focus on\x01",
            "helping out with the festival.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x456)
    Jump("loc_689E")

    label("loc_683F")


    ChrTalk(
        0xFE,
        (
            "#830FJust leave security up to me\x01",
            "and you two can focus on\x01",
            "helping out with the festival.\x02",
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
            "#130FWell, now...\x02\x03",
            "I see that you're studying hard.\x02",
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
            "Let's see...maybe I should just\x01",
            "rest here?\x02",
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
            "I took a day off of work to see\x01",
            "how my son has matured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eletta seems to be quite pleased,\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to be a better mother from\x01",
            "here on out. Gotta turn the doting\x01",
            "up to 9!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A84")

    label("loc_69F4")


    ChrTalk(
        0xFE,
        (
            "I took a day off of work to see\x01",
            "how my son has matured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to be a better mother from\x01",
            "here on out. Gotta turn the doting\x01",
            "up to 9!\x02",
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
        "I want some juice...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AD7")

    label("loc_6AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6AD7")

    ChrTalk(
        0xFE,
        "Hey! I wanna plaaaaayyy...!\x02",
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
        (
            "Hah... Found her! Thought she\x01",
            "could get away from her big\x01",
            "sis, did she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She seems pretty close to that Gerome\x01",
            "fellow, I've noticed. I wonder if there's\x01",
            "anything there...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C5F")

    label("loc_6B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6C5F")

    ChrTalk(
        0xFE,
        (
            "Heh... Under normal circumstances,\x01",
            "I'd never be able to get in here.\x01",
            "It's exciting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, where is my little sister's\x01",
            "classroom...? Got to fulfill my\x01",
            "obligations as her guardian.\x02",
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
            "Hmmm...okay, the economic\x01",
            "development after the Hundred\x01",
            "Days War hinged upon these...\x02",
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
        "*sigh* I need a break...\x02",
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
        "Ugh...I hate these writing assignments.\x02",
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
        "Schoolwork is all well and good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I'd like for my kid to be more\x01",
            "thoughtful, first and foremost.\x02",
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
            "My mom's really eager for me\x01",
            "to get in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So I've got to really bust my butt\x01",
            "to pass the entrance exam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E52")

    label("loc_6E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6E52")

    ChrTalk(
        0xFE,
        (
            "I wonder what typical classes\x01",
            "here are like...\x02",
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
        "*sigh* The festival is just PERFECT.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I want my son to enroll\x01",
            "here more than ever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F57")

    label("loc_6EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6F57")

    ChrTalk(
        0xFE,
        (
            "I came here with my son to check\x01",
            "out the Royal Academy campus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got to get him focused on\x01",
            "passing next year's entrance\x01",
            "exams!\x02",
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
            "#781FI've not seen you since last year's\x01",
            "Royal Council, Mayor Dalmore.\x02\x03",
            "Has much changed since then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#661FAs you can see, I'm feeling\x01",
            "quite well. You look to be in\x01",
            "good health, also.\x02\x03",
            "I expect that today will be\x01",
            "quite enjoyable.\x02",
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
            "#661FAh, so you kids are here, too.\x02\x03",
            "I come to the campus festival\x01",
            "every year at the invitation of\x01",
            "the dean and Student Council.\x02",
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
            "#620FI saw Joshua running off earlier.\x01",
            "He looked quite serious.\x02\x03",
            "Has something happened?\x02",
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
        "#004FAh, Lila?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#621FIt's good to see you both again.\x02",
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
        "#613FOh! Well, if it isn't Estelle and Joshua!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x24, 0)
    TurnDirection(0x102, 0x24, 0)
    TurnDirection(0x105, 0x24, 0)

    ChrTalk(
        0x101,
        (
            "#004FMayor Maybelle, too?!\x02\x03",
            "What are you two doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#611FHa ha...to tell you the truth,\x01",
            "I actually graduated from here.\x02\x03",
            "I always make a point of going\x01",
            "to the campus festival each year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, okay. That's cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#610FBut enough about me. How\x01",
            "have you two been doing?\x02\x03",
            "Are you here on guild business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FHeh heh...well, actually...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle told Mayor Maybelle what had been going on.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x24,
        (
            "#613FOh, so you're helping out\x01",
            "with the play?\x02\x03",
            "#611FI've always found them to be\x01",
            "slightly tiresome.\x02\x03",
            "Ha ha...but if you're going to be\x01",
            "on stage, I certainly don't want\x01",
            "to miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F(Ugh...I'd really rather not have\x01",
            "anyone I KNOW in the audience\x01",
            "for this...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0)
    Jump("loc_7567")

    label("loc_7523")


    ChrTalk(
        0xFE,
        (
            "#621FLong time no see, you two.\x01",
            "You look as energetic as ever.\x02",
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
            "Time was, all of the students'\x01",
            "displays were research papers\x01",
            "of some kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Times change, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7672")

    label("loc_75E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7672")

    ChrTalk(
        0xFE,
        (
            "When we were students, \x01",
            "this building wasn't even\x01",
            "around yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The building to the north used\x01",
            "to be the main school building.\x02",
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
            "The highest final exam grade\x01",
            "was from...one Kloe Rinz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow, she and Jill must be\x01",
            "really smart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_773A")

    label("loc_76EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_773A")

    ChrTalk(
        0xFE,
        (
            "Sunday school is nice and all, but\x01",
            "this? This is REAL learning...\x02",
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
            "They must have something\x01",
            "interesting up their sleeves\x01",
            "for this afternoon's play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I asked my daughter about it,\x01",
            "but she wouldn't tell me any\x01",
            "details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7855")

    label("loc_77EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7855")

    ChrTalk(
        0xFE,
        "So, this is the academy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My daughter attends here, but\x01",
            "this is my first time on campus.\x02",
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
            "All this walking has tired me\x01",
            "out. Maybe I should rest in\x01",
            "the coffee house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7905")

    label("loc_78B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7905")

    ChrTalk(
        0xFE,
        (
            "The natural science and\x01",
            "social studies classes\x01",
            "are up here. Neat!\x02",
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
            "All the displays were fun.\x01",
            "The children seem to be\x01",
            "having a great time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7990")

    label("loc_7963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7990")

    ChrTalk(
        0xFE,
        "I'm not sure where to go next...\x02",
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
        "There are displays everywhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can see that the students\x01",
            "put a lot of work into them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A3C")

    label("loc_7A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7A3C")

    ChrTalk(
        0xFE,
        (
            "I wasn't expecting so many\x01",
            "buildings here.\x02",
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
        "I'm really amazed at this class...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These students have really\x01",
            "accomplished a lot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AF0")

    label("loc_7AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7AF0")

    ChrTalk(
        0xFE,
        (
            "Well, well...this is the natural\x01",
            "sciences exhibition, eh? \x02",
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
            "I think the exhibitions will be\x01",
            "shut down soon. I'd better hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B8D")

    label("loc_7B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7B8D")

    ChrTalk(
        0xFE,
        (
            "Is it just me, or are there more\x01",
            "people here than usual?\x02",
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
        (
            "I'm going to see the play\x01",
            "this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope it'll start soon...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C33")

    label("loc_7BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7C33")

    ChrTalk(
        0xFE,
        (
            "You attend classes here? Do\x01",
            "you ever get to have any fun?\x02",
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
            "#132FWell, well...you've certainly pulled out all\x01",
            "the stops, haven't you?\x02\x03",
            "So many areas of interest, from history to\x01",
            "economics...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x29, 180, 400)

    ChrTalk(
        0x29,
        (
            "#130FThank you so much. This looks like smashing\x01",
            "fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048FIt was my pleasure to help, sir.\x02\x03",
            "Social studies is my major, so I hope you enjoy\x01",
            "looking around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FI've never been any good at this whole\x01",
            "academics thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F*sigh* One of these days, you're really going to\x01",
            "have to get over that.\x02\x03",
            "#010FBeing a bracer requires knowledge in many\x01",
            "different areas of study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "#130FHa ha. Well, I'm itching to start looking\x01",
            "around, so if you'll excuse me.\x02\x03",
            "Thank you again for showing me the way here.\x02",
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
        "#1PMiss Kloe!\x02",
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
        "#041FOh... You're all here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#3PHeya, kiddos! Glad you could\x01",
            "make it! 侓\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F#4PAre you having fun?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yeah! It's awesome! 侓\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I ate so much candy I puked!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I told you not to be such\x01",
            "a pig...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048FHa ha... Is Matron Theresa\x01",
            "with you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(
        0xD,
        (
            "#770FYep, she's talkin' to those\x01",
            "people over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#771FHere she is!\x02",
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
        "#750FGood afternoon, all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#3PMatron Theresa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#048FGood afternoon, Matron.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#751FThank you very much for\x01",
            "inviting us here today.\x02\x03",
            "The children and I have\x01",
            "enjoyed it greatly.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x105, 400)

    ChrTalk(
        0xD,
        (
            "#770FHey, Miss Kloe?\x02\x03",
            "When's your play thingy\x01",
            "supposed to start?\x02",
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
            "We've all been looking forward\x01",
            "to it. 仚\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040FI see... Well, you'll have to\x01",
            "wait just a little bit longer.\x02\x03",
            "#041FDid you know that both Estelle and Joshua are\x01",
            "going to be in the play with me?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        "Really? That's gonna be so cool!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "What part are you going to be playing, Mister\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F#4PUmm... Well, how to put this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#3PHa ha ha! You'll just have to wait and see,\x01",
            "won't you? 噴\x02\x03",
            "#000FOh, by the way...are you guys\x01",
            "still staying in Manoria?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750FYes, through the continued good will\x01",
            "of the innkeepers.\x02\x03",
            "#757FThat said, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#3P???\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P...\x02\x03",
            "#010FHey, guys. Do you want to see\x01",
            "the costumes that'll be used\x01",
            "in the play?\x02\x03",
            "There are pretty dresses and\x01",
            "suits of armor...\x02",
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
        "Pretty dresses?!\x02",
    )

    CloseMessageWindow()

    def lambda_8945():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8945)
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(
        0xD,
        "#774F#1PSuits of armor?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FHa ha... I guess I have your\x01",
            "attention.\x02\x03",
            "I'll give you an exclusive\x01",
            "sneak peek at them, before\x01",
            "the play even starts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yaaaaaay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I wanna go, too!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F(I'll be backstage. Come\x01",
            "when you're ready.)\x02",
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
        "#010FOkay. Now follow me.\x02",
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
            "#750F#5P*chuckle* Joshua is such a\x01",
            "thoughtful boy.\x02\x03",
            "#757FI didn't want to speak of this\x01",
            "in front of the children.\x02",
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
        "#002F#3PYou mean...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "#754FYes. I've chosen to accept the\x01",
            "mayor's offer.\x02\x03",
            "We will impose upon the\x01",
            "Manorians no longer.\x02\x03",
            "#750FI will tell the children today,\x01",
            "after the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#049F#4PI... I see...\x02\x03",
            "That's sad...but I suppose\x01",
            "you have no choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#751F*chuckle* Please, don't look\x01",
            "at me so...\x02\x03",
            "Grancel is easily reachable\x01",
            "by airship.\x02\x03",
            "#750FMoreover, I can look for work\x01",
            "while I am there.\x02\x03",
            "If I save enough mira, I'll be\x01",
            "able to rebuild the orphanage,\x01",
            "some day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#3PMatron...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#049F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#751FNow, then... Let us find the\x01",
            "children, shall we?\x02\x03",
            "I would imagine that they're a\x01",
            "bit much for Joshua to handle\x01",
            "on his own.\x02",
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
            "Found \x07\x02",
            "Ruan Economics II\x07\x00",
            ".\x02",
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
            "Ahead: Dean's Room, Staff Lounge\x01\x01",
            "* Academy personnel ONLY, please\x02",
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
            "Humanities Refreshment Booth\x01",
            "     Fontana Tea House\x02",
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
            "KEEP OUR HALLWAYS QUIET\x01\x01",
            "      --Student Council\x02",
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
            "Natural Sciences Demonstration\x01",
            "'Quartz Circuits & Orbal Arts'\x02",
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
            "Social Studies Demonstration\x01",
            "'Ruanian History & Economy'\x02",
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
            "Welcome to the Fontana Tea House!\x02",
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
            "It summarizes the trends in\x01",
            "orbal arts usage.\x02",
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
            "It has a graph, depicting changes in the\x01",
            "tourist industry's annual growth rate.\x02",
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
            "It lists the most important exports.\x02",
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
            "It concerns population growth and\x01",
            "migration.\x02",
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
            "              Orbal Functional Unit Memory\x01\x01",
            "* Displayed items are on loan from the\x01",
            "Zeiss Central Lab.\x02",
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
            "               Orbal Compatibility Tester\x01\x01",
            "* Now working! No more electric shocks! We promise!\x02",
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
            "Orbal Compatibility Tester\x01",
            "Version:1.0014.4082\x01",
            "(C) 1202 Jenis Royal Academy\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 290, 56, 3)
    SetChrName("Tester")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Begin test?\x02",
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
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
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
            "Whose profile will you input?\x02",
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
            "[Estelle]\x01",         # 0
            "[Joshua]\x01",          # 1
            "[Scherazard]\x01",      # 2
            "[Olivier]\x01",         # 3
            "[Kloe]\x01",            # 4
            "[Nial]\x01",            # 5
            "[Dorothy]\x01",         # 6
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
            "[Estelle Bright] \x01",
            "Born 8-7-1186, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_985E")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Joshua Bright]\x01",
            "Born 12-20-1185, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_98A5")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Scherazard Harvey] \x01",
            "Born 5-14-1179, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_98F0")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Olivier Lenheim]\x01",
            "Born 4-1-1177, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_9937")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Kloe Rinz] \x01",
            "Born 10-11-1186, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_997B")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Nial Burns]\x01",
            "Born 11-25-1172, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_99BF")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Dorothy Hyatt]\x01",
            "Born 1-22-1182, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A05")

    label("loc_9A05")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please input next profile.\x02",
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
            "[Estelle]\x01",         # 0
            "[Joshua]\x01",          # 1
            "[Scherazard]\x01",      # 2
            "[Olivier]\x01",         # 3
            "[Kloe]\x01",            # 4
            "[Nial]\x01",            # 5
            "[Dorothy]\x01",         # 6
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
            "[Estelle Bright] \x01",
            "Born 8-7-1186, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9AF2")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Joshua Bright]\x01",
            "Born 12-20-1185, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9B39")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Scherazard Harvey] \x01",
            "Born 5-14-1179, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9B84")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Olivier Lenheim]\x01",
            "Born 4-1-1177, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9BCB")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Kloe Rinz] \x01",
            "Born 10-11-1186, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9C0F")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Nial Burns]\x01",
            "Born 11-25-1172, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9C53")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Dorothy Hyatt]\x01",
            "Born 1-22-1182, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9C99")

    SetChrName("Tester")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Beginning analysis.\x02",
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
    SetChrName("Tester")
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
            "Today will be an especially active day\x01",
            "for both individuals.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Your actions will cause your life\x01",
            "to be firmly enmeshed in another's. \x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because of lively conversation, when the two of you\x01",
            "can be alone, the fire in your hearts may be kindled.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Before you can be overwhelmed, take action.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Your common goals and interests will carry your\x01",
            "relationship further than it has ever been.\x02",
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
            "These two are greatly attuned to one another, and their\x01",
            "time spent together today should be very enjoyable.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They should be able to overcome any obstacle together,\x01",
            "regardless of the circumstances or consequences.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Their shared awareness will enable them to overcome\x01",
            "unknown foes, and their bond will grow ever stronger.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "These two have strong ties of love\x01",
            "and comradeship to each other.\x02",
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
            "Today is a day for them to look to the\x01",
            "future with open and optimistic eyes.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Today, in spite of their differences, they should\x01",
            "be able to pass the time together quietly without\x01",
            "argument or serious bodily injury.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Normally, these two would feel compelled\x01",
            "to push their opinions onto each other...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "But today feels like a day of peace and tranquility.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a real chance to move on from the\x01",
            "usual conversation, and speak of new things.\x02",
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
            "These are two very active individuals.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Today is the ideal day to take on\x01",
            "new challenges or foes together.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All it will take is for each to suppress the\x01",
            "impulse to force an opinion onto the other.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If these two learn to respect each other's point of view,\x01",
            "they will both grow more mature from the experience.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Most importantly, they must each learn\x01",
            "to consider the other's feelings.\x02",
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
            "Though these two are in each other's company today, there\x01",
            "seems to be a distinct awkwardness between them.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A secret will be revealed, and if one lies, it\x01",
            "will sow the seeds of distrust in the other.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If they cannot find their common ground,\x01",
            "conversation between them will do no good.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Today is the day, either for compromise\x01",
            "or for giving up altogether.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Only time and distance will likely heal the damage done.\x02",
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
            "These two are in grave need of expressing their feelings\x01",
            "to one another, or they risk a serious argument.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A prolonged argument will lead to a\x01",
            "painful and reluctant separation.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Today is a day that is, perhaps, better spent among\x01",
            "a crowd than in each other's exclusive company.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regardless of what is said, it must be heard with an\x01",
            "open mind, no matter how unwelcome it may be.\x02",
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
            "4 Error(s)...  0 Warning(s)...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Orbal Compatibility Tester\x01",
            "Version:1.0014.4082\x01",
            "(C) 1202 Jenis Royal Academy\x01",
            "#200W丂#20W\x01",
            "MEMORY_CHECK#100W........#20WOK!\x01",
            "#200W丂#20W\x01",
            "restart\x02",
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
    SetChrName("Tester")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Continue analysis?\x02",
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
