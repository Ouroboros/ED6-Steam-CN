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
        'Olivier',                              # 9
        'Mueller',                              # 10
        'Lifa',                                 # 11
        'Receptionist',                         # 12
        'Deen',                                 # 13
        'Rais',                                 # 14
        'Rocco',                                # 15
        'Soldier',                              # 16
        'Soldier',                              # 17
        'Soldier',                              # 18
        'Soldier',                              # 19
        'Soldier',                              # 20
        'Soldier',                              # 21
        'Soldier',                              # 22
        'Soldier',                              # 23
        'Soldier',                              # 24
        'Soldier',                              # 25
        'Soldier',                              # 26
        'Soldier',                              # 27
        'Soldier',                              # 28
        'Soldier',                              # 29
        'Soldier',                              # 30
        'Soldier',                              # 31
        'Anelace',                              # 32
        'Professor Alba',                       # 33
        'Ralph',                                # 34
        'Private Bergan',                       # 35
        'Private Tact',                         # 36
        'Robyn',                                # 37
        'Miele',                                # 38
        'Godfrey',                              # 39
        'Phoebe',                               # 40
        'Nana',                                 # 41
        'Anton',                                # 42
        'Ricky',                                # 43
        'Sorbet',                               # 44
        'Carla',                                # 45
        'Lucia',                                # 46
        'Clarice',                              # 47
        'Nemo',                                 # 48
        'Laone',                                # 49
        'Marsha',                               # 50
        'Builna',                               # 51
        'Soldier',                              # 52
        'Soldier',                              # 53
        'Soldier',                              # 54
        'Special Ops Soldier',                  # 55
        'Special Ops Soldier',                  # 56
        'Special Ops Soldier',                  # 57
        'Tourist',                              # 58
        'Tourist',                              # 59
        'Tourist',                              # 60
        'Tourist',                              # 61
        'Tourist',                              # 62
        'Tourist',                              # 63
        'Tourist',                              # 64
        'Tourist',                              # 65
        'Tourist',                              # 66
        'Tourist',                              # 67
        'Tourist',                              # 68
        'Tourist',                              # 69
        'Tourist',                              # 70
        'Tourist',                              # 71
        'Tourist',                              # 72
        'Tourist',                              # 73
        'Tourist',                              # 74
        'Tourist',                              # 75
        'Tourist',                              # 76
        'Tourist',                              # 77
        'Tourist',                              # 78
        'Tourist',                              # 79
        'Tourist',                              # 80
        'Tourist',                              # 81
        'Tourist',                              # 82
        'Tourist',                              # 83
        'Tourist',                              # 84
        'Tourist',                              # 85
        'Tourist',                              # 86
        'Tourist',                              # 87
        'Tourist',                              # 88
        'Grancel - North Block',                # 89
        'Grancel - South Block',                # 90
        'Grancel - Landing Port',               # 91
        'Targeting Camera',                     # 92
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
            "#070FAll right, then...\x01",
            "Two days down, two days to go!\x02\x03",
            "I don't know what'll happen tomorrow,\x01",
            "but we're moving on to the next round.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4POf course!\x02\x03",
            "#007FSeriously, though... We've got\x01",
            "some really tough opponents\x01",
            "left to face.\x02\x03",
            "Our fellow Guild members, plus\x01",
            "the Sky Bandits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4PTrue... We can't afford to\x01",
            "let our guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FOh, come now. What, truly, is there\x01",
            "for us to be concerned over?\x02\x03",
            "We have built this dream together,\x01",
            "to stand strong forever! Nothing\x01",
            "is going to stop us now!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        (
            "#509F#6PMy fist is going to stop you, if\x01",
            "you don't stop spouting nonsense\x01",
            "and take this seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FWell, positive thinking isn't a bad thing.\x01",
            "We've got to keep each other's spirits up from\x01",
            "today, so that we'll be ready for tomorrow.\x02\x03",
            "So in the interest of that...\x01",
            "I'm going to the bar!\x01",
            "What about you guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FFor my part, I would most\x01",
            "graciously join you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F#4P(We should go report in\x01",
            "at the guild.)\x02\x03",
            "(They might have some new\x01",
            "info on our assignment.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F#6P(Yeah, maybe...)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    TurnDirection(0x102, 0x104, 400)

    ChrTalk(
        0x101,
        (
            "#506F#4PSorry, Zane...\x01",
            "We'll have to take a rain check.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FAll right...\x01",
            "Goodbye for now, then.\x02\x03",
            "We'll meet up again tomorrow\x01",
            "morning, in the hotel lobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#031FAu revoir, my dear pussycats.\x02",
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
        "#006F#6POkay...so, off to the guild.\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#013F#4PRight.\x02\x03",
            "And it wouldn't hurt to try getting\x01",
            "some information from around town,\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6PLike...what, exactly?\x02",
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
        "Young Man's Voice",
        (
            "#2PHeh, check you two out. You got\x01",
            "time to just stand around?\x02",
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
            "#000FO-Oh... Hi, there. You guys\x01",
            "must be tired from today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmph. Don't start acting all\x01",
            "cocky on us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "This last time, we didn't have a\x01",
            "whole lotta time to train properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Next time, though, we'll win...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Huh...?\x01",
            "You wanna do this again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FHa ha ha... It's fine.\x02\x03",
            "If we have another chance, we'll\x01",
            "be happy to have a rematch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FHey, Estelle... Don't you think\x01",
            "you're being a little hasty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FOh, what's the big deal?\x02\x03",
            "If we keep up with our own\x01",
            "training, we'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Heh... Aren't you the optimistic\x01",
            "little twerp?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well, here. Take this.\x02",
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
            "Received \x07\x02",
            "Grancel Sewer Key A\x07\x00",
            ".\x02",
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
        "#505FWh-What's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FLooks like an extremely old key.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It'll open up that barred-off\x01",
            "passage in the West Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It leads to a huge underground\x01",
            "sewer system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We got that key by pure chance,\x01",
            "so we go down there every day\x01",
            "to explore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "There's a ton of really tough monsters\x01",
            "in there, so you'd better make sure\x01",
            "you're absolutely ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FW-Well, I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hey, don't get us wrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Losing to you just pissed\x01",
            "us off, is all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Listen...\x01",
            "You'd better win that tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "We won't accept any less.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We've said what we came to\x01",
            "say, so we'll see you later.\x02",
        )
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
            "#505F#6PUhh...okay.\x01",
            "So what was that about?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FI think they were trying to show\x01",
            "us that they're rooting for us.\x02\x03",
            "Maybe they're telling us to use\x01",
            "the sewers to train ourselves\x01",
            "before the big match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#6PI...guess that makes sense.\x02\x03",
            "Hmmm... Maybe they really have\x01",
            "turned over a new leaf?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FHa ha... Maybe they just like\x01",
            "your manly nature.\x02\x03",
            "After all, you are the most\x01",
            "violent person I've ever met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#6PManly...violent...\x01",
            "What are you trying to say, Joshua?\x02\x03",
            "#007FWell, whatever. I say we should accept\x01",
            "whatever good will is offered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's late, though. I think we should\x01",
            "wait before we go underground.\x02\x03",
            "We can give it a try before\x01",
            "tomorrow's match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#6POkay...\x02\x03",
            "Let's stop in at the guild, then,\x01",
            "and report in to Elnan.\x02",
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
            "#007F#6PWhew... I don't know how we\x01",
            "did it, but we did it.\x02\x03",
            "#006FTomorrow's the final match...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FWe're really going to have to keep\x01",
            "our spirits up, because that's going\x01",
            "to be one tough match.\x02\x03",
            "#071FSo I propose that we go to the\x01",
            "bar and let it all hang out, so\x01",
            "to speak!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FHeh. I like the way you think, good\x01",
            "sir. I should like to join you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#6PSo this is 'adult' logic...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PWe've got some stuff we have to do,\x01",
            "so not tonight for us, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FNo problem.\x01",
            "See you later, then.\x02\x03",
            "We'll meet up with you tomorrow\x01",
            "morning, out front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#035FGoodnight, my sweethearts. 噴\x02",
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
            "#006F#6PNow, let's see...\x02\x03",
            "I'll bet Nial's waiting for us, so\x01",
            "why don't we go to the Liberl News\x01",
            "Service and see what he has to say?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#4PYeah...\x02\x03",
            "Hopefully, he's managed to learn\x01",
            "something useful about those\x01",
            "Intelligence Division members.\x02",
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
        "What do you think you're doing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F(Crap...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F(Spotted already...)\x02",
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
            "#000FWhew... Well, we managed to\x01",
            "avoid the patrols so far...\x02\x03",
            "It doesn't look like there are\x01",
            "any soldiers this way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FYeah...\x01",
            "I'm not sensing anyone.\x02\x03",
            "I guess the night patrols\x01",
            "are finally done.\x02\x03",
            "Let's rest for a moment here,\x01",
            "then head back to the hotel.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FOkay.\x02",
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
            "#000FUgh... So much is going on. It's\x01",
            "starting to give me a headache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FHa ha... I'll bet.\x02\x03",
            "I never would have imagined it to be\x01",
            "Lt. Schwarz waiting for us at the\x01",
            "cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWait, so...\x02\x03",
            "...she WASN'T who you were\x01",
            "expecting to find there?\x02\x03",
            "Could it be...you were thinking it'd\x01",
            "be someone you'd known before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWell...\x02\x03",
            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FOh...\x02\x03",
            "Sorry. Forget I said anything.\x02\x03",
            "Gotta remember the rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FA promise is a promise.\x02\x03",
            "I won't ask you anything about\x01",
            "before we met until you're ready\x01",
            "to tell me.\x02\x03",
            "I try to be careful, but sometimes\x01",
            "it just slips my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F...\x02\x03",
            "Estelle, I...\x02\x03",
            "I think you've gotten a little\x01",
            "stronger during our travels...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's overwhelming to think about all the people\x01",
            "around us. Each and every one of them living his\x01",
            "or her own life, all under this same sky...\x02\x03",
            "...and every person you meet has a personality,\x01",
            "and a history, and a story to tell. Every one\x01",
            "of them is just like us, living day by day...\x02\x03",
            "Sometimes, I just have to remind myself that\x01",
            "no one acts without cause. Nothing happens\x01",
            "without a reason, or a motive...or an excuse.\x02\x03",
            "And it's only when I remember that that I\x01",
            "start to feel like I might be able to reclaim\x01",
            "the parts of me I've lost...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FJoshua...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI'm probably just fooling myself.\x01",
            "Tricking myself into accepting\x01",
            "things I can't change.\x02\x03",
            "But even so...\x02\x03",
            "I'm grateful for having someone\x01",
            "with me...\x02\x03",
            "The sky... Dad...\x02\x03",
            "But most of all...you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FJoshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FSo...I promise.\x02\x03",
            "Once this whole matter is settled,\x01",
            "and if Dad comes back safely...\x02\x03",
            "I'll tell you everything there\x01",
            "is to know about my past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FReally.\x02\x03",
            "With the stars as my witness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F...\x02\x03",
            "...Okay, then! We have\x01",
            "ourselves a deal!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x10586, 0xFA, 0xAEE2, 0xBB8, 0x0)

    ChrTalk(
        0x102,
        "#010FEstelle...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000FAll my gloom's gone fluttering away...\x02\x03",
            "...'cause once you've told me what\x01",
            "you've gotta tell me, then I'll\x01",
            "tell you what I've gotta tell you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FUhh...what?\x02\x03",
            "...Oh, wait, is this about that\x01",
            "thing you've had on your mind? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FYep!\x02\x03",
            "Heh heh... Gonna have to\x01",
            "psych myself up for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FPsych yourself up? Is it really\x01",
            "something so...dramatic?\x02\x03",
            "I mean, if it's THAT important, \x01",
            "I really don't mind hearing\x01",
            "about it now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FAbsolutely not!\x02\x03",
            "It's a...delicate matter.\x01",
            "And timing is crucial!\x02\x03",
            "Though...I guess the situation\x01",
            "DOES feel kinda right...but\x01",
            "still, no dice! Not yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F???\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FThere's no way I'm gonna\x01",
            "lose tomorrow...\x02\x03",
            "I'm gonna show those Special Ops\x01",
            "types how a touch of girl power can\x01",
            "ruin their whole day! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FRuin their...?\x02\x03",
            "...*snicker*...\x02\x03",
            "HAHAHAHAHAHAHA!!\x02\x03",
            "You...really are your father's daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FHey, what's that supposed to mean?\x02\x03",
            "You'd better not be comparing\x01",
            "me to a middle-aged man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYeah, I guess you're right.\x02\x03",
            "Somehow...I think we're\x01",
            "going to do just fine\x01",
            "tomorrow.\x02",
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
            "It's locked.\x02",
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
            "It's locked.\x02",
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
            "#010FIt's late, so why don't we wait\x01",
            "before we try our luck in the\x01",
            "sewers?\x02\x03",
            "We'd probably be best off if we\x01",
            "have Zane and Olivier with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51AC")

    label("loc_510D")


    ChrTalk(
        0x102,
        (
            "#010FThis looks like the entrance to\x01",
            "the sewers that Elnan told us\x01",
            "about.\x02\x03",
            "It's too late to go tonight.\x01",
            "We can come back when we have\x01",
            "the others with us.\x02",
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
            "Used \x07\x02",
            "Grancel Sewer Key B\x07\x00",
            ".\x02",
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
            "#001F#6PPhew! Now THAT was one\x01",
            "hell of a fight.\x02\x03",
            "I had no clue that Lieutenant\x01",
            "Lorence was so freakin' strong...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PYes... I think we got lucky.\x02\x03",
            "Even now, it's hard to believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#074F...I don't like it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6PHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#070FEh...it's nothing.\x02\x03",
            "More importantly, that fancy\x01",
            "shindig is supposed to be\x01",
            "happening tonight.\x02\x03",
            "From what I understand, it's going\x01",
            "to run late into the night, so \x01",
            "they're setting up rooms for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030FAhh, most generous of them.\x02\x03",
            "Rubbing shoulders with all of those stuffed\x01",
            "shirts is sure to chafe in the worst way,\x01",
            "in uncomfortable places...\x02\x03",
            "But dining? Liberl royal dining? The\x01",
            "very prospect of such decadence... \x02\x03",
            "#035FLook at me. My mouth can barely contain\x01",
            "itself! Where is my handkerchief...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#6PAh--it's getting on your--Aww, gross!! \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#4PIt's good to see that you haven't lost\x01",
            "your sense of perspective, Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FHa, ha, ha! Indeed!\x01",
            "Let us be off, then!\x02\x03",
            "Off to gorge our souls upon the\x01",
            "seven courses of courtly affection!\x02",
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
        "Man's Voice",
        "#2POh, that's the plan, is it?\x02",
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
        (
            "#033FWell, well! Fancy meeting\x01",
            "you here!\x02",
        )
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
            "#6P#274FYou son of a bitch...\x02\x03",
            "You wander all over the place, every\x01",
            "damn day, and leave me wondering what\x01",
            "the hell you're up to...\x02\x03",
            "Have you gone COMPLETELY mad? What\x01",
            "possessed you to participate in a\x01",
            "martial arts competition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FO-Oh, come now, my dear Mueller...\x02\x03",
            "There's no need to crease your\x01",
            "lovely face with such an ill-\x01",
            "tempered expression.\x02\x03",
            "After all, is it not true that good\x01",
            "fortune comes to those who favor\x01",
            "those around them with a smile? 噴\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x9,
        "#6P#271F#3SI AM SMILING!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F(Is it just me, or do you recognize\x01",
            "that uniform?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F(Yeah, looks like Imperial\x01",
            "military to me...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F(Hmm... He looks like he could\x01",
            "be a tough one to take on in a\x01",
            "fight, too... )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#270FI don't believe we've met.\x02\x03",
            "My name is Mueller. I was just recently\x01",
            "appointed as the resident military\x01",
            "officer at the Erebonian embassy.\x02\x03",
            "I've known this whack-job\x01",
            "for a VERY long time.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x104, 0xFF)
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(
        0x104,
        (
            "#031FOne might even call us schoolyard chums!\x02\x03",
            "Ha ha... Fret not over his dark demeanor.\x01",
            "Without it, his presence wouldn't light\x01",
            "up the room the way it does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#274F#3SOkay, you really need to\x01",
            "shut up now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#034FRight...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x9, 400)

    ChrTalk(
        0x9,
        (
            "#6P#272F*ahem*\x01",
            "Now, where was I...?\x02\x03",
            "#270FFrom the looks of things, this...\x01",
            "fellow has caused you some trouble.\x02\x03",
            "As a representative of the Erebonian\x01",
            "embassy, I sincerely apologize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FOh, it's okay. He hasn't\x01",
            "really been a bother.\x02\x03",
            "Actually, he was a big help\x01",
            "to us in the tournament...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FUh, Olivier...?\x02\x03",
            "Did you deliberately try to keep your\x01",
            "participation in the tournament a\x01",
            "secret from the embassy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FHa ha ha!\x01",
            "Oh, perish the thought.\x02\x03",
            "No, no...\x01",
            "Rather, I simply never told them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#271F#3SHow is that any different\x01",
            "from hiding it?!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x9,
        (
            "#6P#272FBut okay, fine.\x01",
            "What's done is done.\x02\x03",
            "Now, though, we're going back to the\x01",
            "embassy. Yes, you're coming with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033FEh...?\x02\x03",
            "#036FP-Please, do wait a moment.\x02\x03",
            "We have all been invited to a\x01",
            "delightful, indeed, wondrous\x01",
            "dinner party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#270FDelightful and wondrous, eh? Sounds\x01",
            "nice. Too bad you won't be attending.\x02\x03",
            "You're going to be confined to\x01",
            "the embassy for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#033F...Are you serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#272FWhen do I ever joke?\x02",
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x104,
        (
            "#036FOh, cruel fate... Truly, you drive\x01",
            "a knife into my very heart.\x02\x03",
            "The promise of this dinner party\x01",
            "has been all that's helped me\x01",
            "maintain my will to live...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FYou know, I actually feel kinda\x01",
            "bad for him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FIs it really that big a deal if\x01",
            "you let him go to the party?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWhat's your reasoning behind this?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(
        0x104,
        (
            "#031FI knew I could count on you!\x02\x03",
            "Ahh, but how lovely a thing is\x01",
            "true friendship...\x02\x03",
            "Such warmth and affection, as\x01",
            "opposed to the cruel frigidity\x01",
            "of my schoolyard chum...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#272F...I don't think you folks really\x01",
            "understand just how serious this is.\x02\x03",
            "#270FBut try to picture this.\x02\x03",
            "A dinner party, populated by royalty\x01",
            "and its influential guests from across\x01",
            "the country...\x02\x03",
            "And also in attendance, an arrogant\x01",
            "fool who never shuts his mouth because\x01",
            "his foot is lodged so far into it.\x02\x03",
            "And if they found out that this\x01",
            "uncouth imbecile was an Erebonian\x01",
            "citizen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#074F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033FMy beautiful and gracious comrades...\x01",
            "Why have you suddenly fallen so silent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F...I'm sorry, Olivier. But he\x01",
            "does kinda have a point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018FYeah... Your usual behavior\x01",
            "might not be appreciated in\x01",
            "the royal castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#075FHmmm... True. We wouldn't want to\x01",
            "start an international incident,\x01",
            "would we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#036FWha... You would turn on me\x01",
            "so easily?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#270FThe war only ended ten years ago.\x01",
            "Relations between our countries\x01",
            "can still be strained, at times.\x02\x03",
            "You'll just have to grin and\x01",
            "bear it, Olivier.\x02",
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
            "#031FPlease, Mueller, hear me out.\x02\x03",
            "I'm sorry that I didn't say anything\x01",
            "before, you know, when you--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#272FThis isn't a debate.\x02",
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
        "#15A#2PMy dinner party!\x05\x02",
    )

    Sleep(1500)

    ChrTalk(
        0x104,
        "#15A#2PMy royal cuisine!\x05\x02",
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
        (
            "#506F#6PUhh...\x01",
            "Is this really okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4PI can't say I really like it,\x01",
            "but the facts are the facts.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x102, 400)

    ChrTalk(
        0x108,
        (
            "#071FWell, there's nothing much\x01",
            "we can do about it now.\x02\x03",
            "We'll just have to enjoy ourselves\x01",
            "twice as much, in order to make up\x01",
            "for him not being able to join us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6POh, well...\x01",
            "I guess you're right.\x02\x03",
            "#006FLet's get our stuff together and\x01",
            "go to Grancel Castle, then!\x02",
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
            "#814F...Huh?\x02\x03",
            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FJust to make it absolutely clear,\x01",
            "this isn't a joke.\x02\x03",
            "Things could get serious in a\x01",
            "big hurry, and if they do, we'll\x01",
            "need your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#819F...Let's see.\x02\x03",
            "Sorry, my head's just a little\x01",
            "scrambled from how screwed up\x01",
            "this whole situation is.\x02\x03",
            "#812FI don't really get all of this, \x01",
            "but you want everyone to meet\x01",
            "up at the guildhouse, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FRight. Elnan will fill you in\x01",
            "on all the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#815FOkay, then.\x01",
            "I'll go and see what's up.\x02",
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
        (
            "#010FOkay... We finally made it\x01",
            "to the rest area.\x02",
        )
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
            "#014FYou sure you don't want to look\x01",
            "around more? Or are you finally\x01",
            "ready to take a break?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_729E")

    label("loc_71D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7245")

    ChrTalk(
        0x102,
        (
            "#010FYou sure you don't want to look\x01",
            "around more? Or are you finally\x01",
            "ready to take a break?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_729E")

    label("loc_7245")


    ChrTalk(
        0x102,
        (
            "#019FYou look pretty tired. You want\x01",
            "to sit down and take a break for\x01",
            "a little bit?\x02",
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
            "[Let's keep looking around.]\x01",      # 0
            "[Let's stop and rest a bit.]\x01",      # 1
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
            "#505FActually, I still have some\x01",
            "stuff I want to check out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAll right... We can just come back\x01",
            "when we're done walking around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FSure, we can sit down\x01",
            "on that bench.\x02",
        )
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
            "#007FWhew... Walking all over the\x01",
            "place like that can really take\x01",
            "it out of you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#010FGlad we can get off our feet for\x01",
            "a minute, then.\x02\x03",
            "For the moment, at least, Grancel\x01",
            "seems like it's genuinely at peace.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#4P#004FYou really think so?\x02\x03",
            "#006FI'm just glad that we can leave\x01",
            "it all up to Dad and everyone else,\x01",
            "at least for today.\x02\x03",
            "Of course, I really think it should\x01",
            "be his responsibility to begin with,\x01",
            "since he showed up so late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FHa ha... Yeah, I suppose so.\x02\x03",
            "#010FMaybe it's just part of his nature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4P#007F*sigh*... Oh, well. It's not like\x01",
            "we can do anything about it.\x02\x03",
            "#501FBut check us out! We're actually full\x01",
            "bracers now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWhich means we're not beholden\x01",
            "to any specific branch and can\x01",
            "go wherever we want.\x02\x03",
            "Anytime a branch is short-handed\x01",
            "and requests help, we'll just\x01",
            "take an airliner to get there.\x02\x03",
            "#019FBut our newfound freedom will also\x01",
            "mean greater responsibilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4P#006FSure, but I think we'll be\x01",
            "able to handle it.\x02\x03",
            "I mean, hey! We actually played\x01",
            "a major part in stopping a coup.\x02\x03",
            "#001FAnd it means I'll never have to hear Dad\x01",
            "going on about how it worries him when\x01",
            "you're not around to keep an eye on me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FHa ha... Yeah, I think his days of\x01",
            "saying that are at an end. You really\x01",
            "showed him what you can do!\x02\x03",
            "#010FStill, I think I'd like to stay\x01",
            "with you from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4P#004F...Err?\x02\x03",
            "...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        "#4P#005F#3SHUH?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FOh...\x01",
            "Would I just get on your nerves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4P#503FNo, no, nothing like that...\x02\x03",
            "But...what do you mean by,\x01",
            "'stay with' me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FJust that we know each other so\x01",
            "well, and we can practically\x01",
            "read each other's minds.\x02\x03",
            "I think we make a good team,\x01",
            "and I'd hate to break it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4P#008FOh...you mean like for\x01",
            "bracer business...\x02\x03",
            "#506FAnd here I was thinking you\x01",
            "were going to tell me your big\x01",
            "confession or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FWha...?\x02",
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
            "#4P#504F#3SAAAAAHH!\x02\x03",
            "#3SNothing! Forget I said anything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FEstelle...what was that all--\x02",
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
            "#008FB-Boy, it sure is hot out today, huh?!\x02\x03",
            "#008FAnd there's nothing to beat hot\x01",
            "weather like ice cream, huh?!\x02\x03",
            "#504FMy treat, just like I promised!\x01",
            "So you wait right here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F38")

    label("loc_7E94")


    ChrTalk(
        0x101,
        (
            "#008FB-Boy, it sure is hot out today, huh?!\x02\x03",
            "#008FAnd there's nothing to beat hot\x01",
            "weather like ice cream, huh?!\x02\x03",
            "#504FI'll even treat!\x01",
            "So you wait right here!\x02",
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
        "#014F#6POh...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x102,
        (
            "#017F#6PI don't think there's an ice\x01",
            "cream stand over that way...\x02\x03",
            "...\x02\x03",
            "#014FI wonder if she...\x02\x03",
            "#013FNah... There's no way...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 71640, 1250, 37000, 0)

    NpcTalk(
        0x20,
        "Man's Voice",
        (
            "#3PMy, but I do envy you your\x01",
            "youth sometimes.\x02",
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
        "#014FProfessor Alba...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#130FIt's been a long time since we\x01",
            "last met, hasn't it?\x02\x03",
            "So much has happened lately,\x01",
            "but things are finally settling\x01",
            "down again.\x02\x03",
            "People truly thrive the most\x01",
            "in peaceful times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#131FOh, is something the matter?\x01",
            "You look a bit pale.\x02\x03",
            "I would have thought you'd generally\x01",
            "be in better spirits, now that you've\x01",
            "attained full bracer status.\x02\x03",
            "#132FSpeaking of which, I truly must\x01",
            "congratulate you on your success.\x02\x03",
            "So long as, of course, I'm not\x01",
            "being too forward in doing so.\x02",
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
            "#013FEver since we first met...\x01",
            "you always made me really\x01",
            "uncomfortable.\x02\x03",
            "I'm a little more used to you now...\x02\x03",
            "...but I still get the shakes a\x01",
            "little bit, whenever you look at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#132FOh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013FAnd in all the cases we've dealt with...\x02\x03",
            "There have been people who\x01",
            "just 'forget' things...\x02\x03",
            "You're always there, investigating...\x01",
            "No matter where we've gone...\x02\x03",
            "Your timing's almost a little too good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#132F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FWhat really clued me in\x01",
            "was Kurt's reaction.\x02\x03",
            "He lost his memories, too...\x02\x03",
            "He said he wasn't feeling so well\x01",
            "when he was in the stands...\x02\x03",
            "And you were right there with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#132F...\x02",
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
            "#015FProfessor Alba...\x02\x03",
            "#012FWas it you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#136FHa ha...\x02\x03",
            "Impressive. Even with your cognizance and\x01",
            "recollection being puppeteered, you were\x01",
            "still able to piece it all together...\x02\x03",
            "Indeed, it was I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#134FAllow me to clear away your confusion.\x02",
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
        "#514FOh...\x02",
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
            "#514FYou...\x02\x03",
            "You're...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "???",
        (
            "#133FHa ha... So you finally remember\x01",
            "me, do you?\x02\x03",
            "When your heart was in tatters,\x01",
            "it was I who rebuilt it...\x01",
            "I who RESTORED it.\x02\x03",
            "It was I who poured a soul back\x01",
            "into that empty vessel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#510FYou have the power to twist the\x01",
            "minds and memories of men...!\x02\x03",
            "The seven Snake Apostles...\x01",
            "The Anguis... You're one of them!\x02\x03",
            "Weissmann the Faceless...!\x02",
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
        "Weissmann",
        (
            "#134FHa... I've not heard that name\x01",
            "pass your lips in ages.\x02\x03",
            "Enforcer...Legion XIII.\x02\x03",
            "The Black Fang...Joshua Astray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#510FY-You...\x02\x03",
            "You were behind all of this!\x02\x03",
            "Which means that Lieutenant\x01",
            "Lorence has to be...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#134FIt is as you surmise.\x02\x03",
            "I was kind enough not to erase your memories\x01",
            "of him. I'm not surprised you were able to\x01",
            "make the connection so quickly.\x02\x03",
            "Ha ha... I'm sure he'd be pleased\x01",
            "to know you were thinking of him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#516FSo...y-you...\x02\x03",
            "...\x02\x03",
            "#510FYou're here to finish me off?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#134FHeh... No, nothing of the sort.\x02\x03",
            "The first phase of our plan went\x01",
            "off without a hitch.\x02\x03",
            "Since I've a moment to spare,\x01",
            "I simply thought I'd come to\x01",
            "see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#510FFirst phase...?\x02\x03",
            "The seal in the old ruins...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#134FThe 'Gate' which blocks the\x01",
            "path to the 'Ring'...\x02\x03",
            "Wrenching it open was but the\x01",
            "first step of many...\x02\x03",
            "#136FHmm-hmm-hmm... And already,\x01",
            "there exists no means of closing\x01",
            "it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#510FI knew this wouldn't be the end of it...\x02\x03",
            "#515FWhat the hell is the 'Shining Ring'?!\x02\x03",
            "And what is your little 'society' after?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#134FIf you really wish to know,\x01",
            "why don't you rejoin?\x02\x03",
            "I'm certain that you'd be able to\x01",
            "return to active duty in no time.\x02\x03",
            "You needn't look so glum. We can\x01",
            "get you back into fighting form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#516F...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#133FHa ha... Please, spare me your\x01",
            "withering looks.\x02\x03",
            "I do understand that you have\x01",
            "a family now, whom you regard\x01",
            "as important.\x02\x03",
            "You greatly admire your father,\x01",
            "to say nothing of the girl you\x01",
            "so adore...\x02\x03",
            "Even with HIM on our side, throwing\x01",
            "those gifts away would be the actions\x01",
            "of an idiot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#136FAnd so, I've come here to see you.\x02\x03",
            "I came to offer you true freedom from\x01",
            "our association, as thanks for the integral\x01",
            "role you so perfectly played...\x02\x03",
            "#134FWhich means that I must congratulate\x01",
            "you, Joshua. You are already a free man.\x02\x03",
            "I am most grateful for the work that\x01",
            "you've done over the past five years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F...\x02\x03",
            "#514F...What?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#137FOh, don't be so boring.\x02\x03",
            "I was expecting a bit more cheer\x01",
            "out of you at hearing such news.\x02\x03",
            "#136FHrm... Perhaps there's a flaw in the\x01",
            "design of your emotions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#590FI've...been helping you...?\x02\x03",
            "Ha ha... What kind of bullshit\x01",
            "are you expecting me to swallow?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#134FOh, pardon me. I completely\x01",
            "forgot to tell you.\x02\x03",
            "I never intended you to be an\x01",
            "assassin, but rather a spy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FWha...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#134FThe society abandoned you. We played on\x01",
            "the pities of a noble-hearted man...and\x01",
            "it worked. You were given a loving home.\x02\x03",
            "And while you were there, our contacts\x01",
            "would check in on you from time to time.\x01",
            "And you'd tell them EVERYTHING.\x02\x03",
            "We were particularly interested in your reports\x01",
            "on the movements of the Bracer Guild...as well\x01",
            "as your intel on one Cassius Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#514F#4S!!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#136FBut of course, YOU wouldn't remember\x01",
            "having done things such as that.\x02\x03",
            "You were...not yourself, at the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#518F...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#135FCassius Bright, S-ranked bracer...\x02\x03",
            "He was the foremost impediment\x01",
            "to the success of this plan.\x02\x03",
            "We felt certain he would be quick\x01",
            "to act in order to stop any coup\x01",
            "d'etat that should occur.\x02\x03",
            "#136FBut through a detailed analysis of his behavioral\x01",
            "patterns, we finally devised a plan that would\x01",
            "lead him out of the country...and out of our way.\x02\x03",
            "The intel you've unknowingly been feeding\x01",
            "us has been most useful indeed!\x02",
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
        "#517FNo...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#134FAnd so, I must thank you again.\x02\x03",
            "The past five years have been\x01",
            "of inestimable help.\x02",
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
        "#517F#3SNo! You're lying!\x02",
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
        "#519F#5SYOU HAVE TO BE LYING!!\x02",
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
            "#517F#50W...I...\x02\x03",
            "All that time...I spent with Estelle...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#133FHa ha... Why are you so sad?\x02\x03",
            "Has your feigned ignorance not\x01",
            "earned you a beloved family, as\x01",
            "well as a happy home?\x02\x03",
            "If you say nothing,\x01",
            "they will never know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#517F...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#134FHowever...it is the sort of \x01",
            "thing that might weigh heavily \x01",
            "on a fellow.\x02\x03",
            "Since your fellow members of\x01",
            "the Bright household are such\x01",
            "good people.\x02\x03",
            "Perhaps a little too good for\x01",
            "a monster such as yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#518F...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#134FHowever much you may model your\x01",
            "behavior after a normal, decent\x01",
            "person, you are no such thing.\x02\x03",
            "You must surely have noticed. Your ability\x01",
            "to reason through and execute a solution\x01",
            "to a problem, no matter the circumstances...\x02\x03",
            "Your physical strength and reflexes,\x01",
            "better than an entire squadron of\x01",
            "normal soldiers...\x02\x03",
            "You are my greatest creation...my\x01",
            "human weapon. That is who and what\x01",
            "you truly are...the Black Fang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#518F...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#134FYou have no place in the lives\x01",
            "of normal people.\x02\x03",
            "You'll never be happy in their\x01",
            "presence again. You can't be!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#518F...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Weissmann",
        (
            "#136FWhen it becomes too much for you,\x01",
            "you are always welcome to return.\x02\x03",
            "To the Grandmaster's society\x01",
            "of souls...\x02\x03",
            "#138FBack to Ouroboros.\x02",
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
            "#517F#6P#40W...\x02\x03",
            "Is this...my punishment?\x02\x03",
            "My sister...and Loewe...\x02\x03",
            "...I...\x02\x03",
            "What do I do...?\x02",
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
            "#007F*sigh* I don't know how to face him\x01",
            "after all that...but I've kept him\x01",
            "waiting for waaaay too long.\x02\x03",
            "...It's getting late, too...\x02\x03",
            "#503FI'm such an idiot. I need to learn to\x01",
            "think before I open my mouth. I wonder\x01",
            "if Joshua's figured me out...\x02\x03",
            "...Gotta cool down. I feel like\x01",
            "I'm stuck in perma-blush mode...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Man's Voice",
        (
            "#1PAh, Estelle! I thought I might\x01",
            "find you around here somewhere.\x02",
        )
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
            "#004FHi, Professor Alba.\x01",
            "Fancy seeing you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#130F#4PHa ha... Indeed.\x02\x03",
            "I was actually just speaking\x01",
            "with Joshua.\x02\x03",
            "Congratulations on your promotion\x01",
            "to full bracer status.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FHee hee... Thanks.\x02\x03",
            "#004FHmm...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#131F#4PIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FI don't know... Something just\x01",
            "seems different about you.\x02\x03",
            "What's got you looking so cheerful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#132F#4P...\x02\x03",
            "#130FHa ha... Okay, you've got me.\x02\x03",
            "To tell the truth, I've made\x01",
            "several major advances in my\x01",
            "archaeological research.\x02\x03",
            "You might say that it's put\x01",
            "me in a good mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FHey, that's awesome!\x02\x03",
            "#004FOh...sorry!\x02\x03",
            "The ice cream's going to melt,\x01",
            "so I'd better get going!\x02\x03",
            "#001FI'll see you later!\x02",
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
        "Weissmann",
        (
            "#136FHa ha... I see.\x01",
            "Cassius Bright's daughter...\x02\x03",
            "#134FI think she's going to be\x01",
            "quite a lot of fun.\x02",
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
            "#506FHey! Sorry it took so long.\x02\x03",
            "It was SUPER crowded there,\x01",
            "but I have returned with our\x01",
            "valuable loot!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FCool. Thanks.\x02\x03",
            "Now we can eat like kings.\x02",
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
            "#008FYeah...\x02\x03",
            "#503FUm...so, about earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FYeah, I want to apologize for that.\x01",
            "I didn't mean to be so vague.\x02\x03",
            "It just wasn't an appropriate\x01",
            "time for confessions, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503FOh...sure...\x02\x03",
            "I didn't really mind so much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWell, when I gave it some more\x01",
            "thought, it seemed kind of\x01",
            "silly to try and rush things.\x02\x03",
            "We may be full bracers now, but\x01",
            "that just means that we have\x01",
            "different work to focus on.\x02\x03",
            "We might have to really consider\x01",
            "our future prospects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FR-Right...\x02\x03",
            "#503F(If we get married, we'll have to\x01",
            "think about raising children...)\x02\x03",
            "#504F(Ack! I've gotta stop getting\x01",
            "so far ahead of myself!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FWell...it's evening already, so\x01",
            "why don't we eat our ice cream\x01",
            "on the way back?\x02\x03",
            "Everyone's probably waiting for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F...\x02\x03",
            "#002F...Hey, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FWhat is it?\x02\x03",
            "Did you have something you wanted\x01",
            "to discuss about the future?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509FN-No! What would give\x01",
            "you THAT idea?\x02\x03",
            "#582FCome on!\x01",
            "Let's get back to the castle!\x02",
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
            "#004FWow...\x01",
            "Look at the size of this crowd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's because it's so warm out today.\x02\x03",
            "Anyone selling ice cream is sure\x01",
            "to make a ton of mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FHmmm... You know, looking at all\x01",
            "this kinda makes me want to eat\x01",
            "everything they've got.\x02",
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
            "#501FWhich reminds me...\x01",
            "I made you a promise.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F...What promise?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#507FWhen we were dressed up as maids\x01",
            "in the castle, you were all sulky\x01",
            "and pouty.\x02\x03",
            "And I said I'd buy you\x01",
            "some ice cream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017FWhy do you remember the\x01",
            "most trivial things...?\x02\x03",
            "#018FAnd as I recall, I also made you\x01",
            "a promise in that rest area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503FOh...yeah, I guess you did.\x02\x03",
            "Why don't we wait for the day to\x01",
            "settle down a little bit first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F???\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        (
            "#509FA-Anyway, we can walk around some\x01",
            "more, then go to the rest area\x01",
            "behind those stores!\x02\x03",
            "And then, I'll buy you\x01",
            "some ice cream!\x02\x03",
            "Okay?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FUh, okay...\x02",
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
            "#010FThis looks like the entrance\x01",
            "to the sewers that Elnan\x01",
            "told us about.\x02\x03",
            "It's too late to go tonight.\x01",
            "We can come back when we\x01",
            "have the others with us.\x02",
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
            "It won't open.\x02",
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
            "It won't open.\x02",
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
            "'The Second Orbally-Powered Clock'\x01",
            "Made in year 1163 of the Septian Calendar,\x01",
            "by Zeissian manufacturers.\x02",
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
