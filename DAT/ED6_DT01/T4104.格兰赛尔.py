from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4104   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4104.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60018",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T4104   ._SN',
            'ED6_DT01/T4104_1 ._SN',
            'ED6_DT01/T4104_2 ._SN',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Zane',                                 # 9
        'Carna',                                # 10
        'Anelace',                              # 11
        'Grant',                                # 12
        'Kurt',                                 # 13
        'Sky Bandit',                           # 14
        'Don',                                  # 15
        'Kyle',                                 # 16
        'Josette',                              # 17
        'Delinquent',                           # 18
        'Deen',                                 # 19
        'Rais',                                 # 20
        'Rocco',                                # 21
        'Soldier',                              # 22
        'Soldier',                              # 23
        'Soldier',                              # 24
        'Soldier',                              # 25
        '1st Lieutenant Riel',                  # 26
        '1st Lieutenant Bern',                  # 27
        'CWO Dale',                             # 28
        'Special Ops Soldier',                  # 29
        'Special Ops Soldier',                  # 30
        'Special Ops Soldier',                  # 31
        '2nd Lieutenant Lorence',               # 32
        'Butler Phillip',                       # 33
        'Duke Dunan',                           # 34
        'Professor Alba',                       # 35
        'Dorothy',                              # 36
        'Referee',                              # 37
        'Delinquent',                           # 38
        'Delinquent',                           # 39
        'Delinquent',                           # 40
        'Captain Amalthea',                     # 41
        'Colonel Richard',                      # 42
        'Patty',                                # 43
        'Ralph',                                # 44
        'Dick',                                 # 45
        'Raleigh',                              # 46
        'Troy',                                 # 47
        'Mayor Klaus',                          # 48
        'Spectator',                            # 49
        'Spectator',                            # 50
        'Spectator',                            # 51
        'Spectator',                            # 52
        'Spectator',                            # 53
        'Spectator',                            # 54
        'Spectator',                            # 55
        'Spectator',                            # 56
        'Spectator',                            # 57
        'Spectator',                            # 58
        'Spectator',                            # 59
        'Spectator',                            # 60
        'Spectator',                            # 61
        'Spectator',                            # 62
        'Spectator',                            # 63
        'Spectator',                            # 64
        'Spectator',                            # 65
        'Spectator',                            # 66
        'Spectator',                            # 67
        'Spectator',                            # 68
        'Spectator',                            # 69
        'Spectator',                            # 70
        'Spectator',                            # 71
        'Spectator',                            # 72
        'Spectator',                            # 73
        'Spectator',                            # 74
        'Spectator',                            # 75
        'Spectator',                            # 76
        'Spectator',                            # 77
        'Spectator',                            # 78
        'Spectator',                            # 79
        'Spectator',                            # 80
        'Spectator',                            # 81
        'Spectator',                            # 82
        'Spectator',                            # 83
        'Spectator',                            # 84
        'Spectator',                            # 85
        'Spectator',                            # 86
        'Spectator',                            # 87
        'Spectator',                            # 88
        'Spectator',                            # 89
        'Spectator',                            # 90
        'Spectator',                            # 91
        'Spectator',                            # 92
        'Spectator',                            # 93
        'Spectator',                            # 94
        'Spectator',                            # 95
        'Spectator',                            # 96
        'Spectator',                            # 97
        'Spectator',                            # 98
        'Spectator',                            # 99
        'Spectator',                            # 100
        'Spectator',                            # 101
        'Spectator',                            # 102
        'Spectator',                            # 103
        'Spectator',                            # 104
        'Spectator',                            # 105
        'Spectator',                            # 106
        'Spectator',                            # 107
        'Spectator',                            # 108
        'Spectator',                            # 109
        'Spectator',                            # 110
        'Spectator',                            # 111
        'Spectator',                            # 112
        'Spectator',                            # 113
        'Spectator',                            # 114
        'Spectator',                            # 115
        'Spectator',                            # 116
        'Spectator',                            # 117
        'Spectator',                            # 118
        'Spectator',                            # 119
        'Spectator',                            # 120
        'Spectator',                            # 121
        'Spectator',                            # 122
        'Spectator',                            # 123
        'Spectator',                            # 124
        'Spectator',                            # 125
        'Spectator',                            # 126
        'Spectator',                            # 127
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
        'ED6_DT07/CH00070 ._CH',             # 00
        'ED6_DT07/CH01240 ._CH',             # 01
        'ED6_DT07/CH01630 ._CH',             # 02
        'ED6_DT07/CH01260 ._CH',             # 03
        'ED6_DT07/CH01620 ._CH',             # 04
        'ED6_DT07/CH01380 ._CH',             # 05
        'ED6_DT07/CH02110 ._CH',             # 06
        'ED6_DT07/CH02120 ._CH',             # 07
        'ED6_DT07/CH02130 ._CH',             # 08
        'ED6_DT07/CH01390 ._CH',             # 09
        'ED6_DT07/CH02510 ._CH',             # 0A
        'ED6_DT07/CH02520 ._CH',             # 0B
        'ED6_DT07/CH02530 ._CH',             # 0C
        'ED6_DT07/CH01640 ._CH',             # 0D
        'ED6_DT07/CH01310 ._CH',             # 0E
        'ED6_DT07/CH01330 ._CH',             # 0F
        'ED6_DT07/CH02200 ._CH',             # 10
        'ED6_DT07/CH02470 ._CH',             # 11
        'ED6_DT07/CH02140 ._CH',             # 12
        'ED6_DT07/CH02050 ._CH',             # 13
        'ED6_DT06/CH20064 ._CH',             # 14
        'ED6_DT07/CH01560 ._CH',             # 15
        'ED6_DT07/CH00100 ._CH',             # 16
        'ED6_DT07/CH00110 ._CH',             # 17
        'ED6_DT07/CH00130 ._CH',             # 18
        'ED6_DT07/CH00170 ._CH',             # 19
        'ED6_DT06/CH20123 ._CH',             # 1A
        'ED6_DT06/CH20124 ._CH',             # 1B
        'ED6_DT06/CH20125 ._CH',             # 1C
        'ED6_DT06/CH20126 ._CH',             # 1D
        'ED6_DT07/CH02100 ._CH',             # 1E
        'ED6_DT07/CH02030 ._CH',             # 1F
        'ED6_DT06/CH20088 ._CH',             # 20
    )

    AddCharChipPat(
        'ED6_DT07/CH00070P._CP',             # 00
        'ED6_DT07/CH01240P._CP',             # 01
        'ED6_DT07/CH01630P._CP',             # 02
        'ED6_DT07/CH01260P._CP',             # 03
        'ED6_DT07/CH01620P._CP',             # 04
        'ED6_DT07/CH01380P._CP',             # 05
        'ED6_DT07/CH02110P._CP',             # 06
        'ED6_DT07/CH02120P._CP',             # 07
        'ED6_DT07/CH02130P._CP',             # 08
        'ED6_DT07/CH01390P._CP',             # 09
        'ED6_DT07/CH02510P._CP',             # 0A
        'ED6_DT07/CH02520P._CP',             # 0B
        'ED6_DT07/CH02530P._CP',             # 0C
        'ED6_DT07/CH01640P._CP',             # 0D
        'ED6_DT07/CH01310P._CP',             # 0E
        'ED6_DT07/CH01330P._CP',             # 0F
        'ED6_DT07/CH02200P._CP',             # 10
        'ED6_DT07/CH02470P._CP',             # 11
        'ED6_DT07/CH02140P._CP',             # 12
        'ED6_DT07/CH02050P._CP',             # 13
        'ED6_DT06/CH20064P._CP',             # 14
        'ED6_DT07/CH01560P._CP',             # 15
        'ED6_DT07/CH00100P._CP',             # 16
        'ED6_DT07/CH00110P._CP',             # 17
        'ED6_DT07/CH00130P._CP',             # 18
        'ED6_DT07/CH00170P._CP',             # 19
        'ED6_DT06/CH20123P._CP',             # 1A
        'ED6_DT06/CH20124P._CP',             # 1B
        'ED6_DT06/CH20125P._CP',             # 1C
        'ED6_DT06/CH20126P._CP',             # 1D
        'ED6_DT07/CH02100P._CP',             # 1E
        'ED6_DT07/CH02030P._CP',             # 1F
        'ED6_DT06/CH20088P._CP',             # 20
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
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 37,
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
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 36,
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
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 43,
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
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 46,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -12680,
        Z                   = 4700,
        Y                   = -4790,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 65562,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = -12660,
        Z                   = 4700,
        Y                   = -3750,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 131098,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = -14750,
        Z                   = 5200,
        Y                   = 3290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 131099,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = -14750,
        Z                   = 5200,
        Y                   = 3960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 65564,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = -14750,
        Z                   = 5200,
        Y                   = 4700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196634,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 393244,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = -14740,
        Z                   = 5200,
        Y                   = -13430,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 65563,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = -15730,
        Z                   = 5450,
        Y                   = -5010,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 131098,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 1,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = 3270,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -15820,
        Z                   = 5450,
        Y                   = -9240,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 393243,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -15850,
        Z                   = 5450,
        Y                   = 1890,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 65562,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = -6590,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 393243,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -12680,
        Z                   = 4700,
        Y                   = -17670,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -14720,
        Z                   = 5200,
        Y                   = -3720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 458778,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = 1670,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262171,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -13710,
        Z                   = 4950,
        Y                   = -13580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 393243,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -14750,
        Z                   = 5200,
        Y                   = -8060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 327707,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -14720,
        Z                   = 5200,
        Y                   = 510,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -12660,
        Z                   = 4700,
        Y                   = -9280,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 131098,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -13750,
        Z                   = 4950,
        Y                   = 4710,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262170,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -13770,
        Z                   = 4950,
        Y                   = -6540,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196636,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -14850,
        Z                   = 5200,
        Y                   = -15970,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262172,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = -13490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 327708,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -15610,
        Z                   = 5450,
        Y                   = -17700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 65562,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -15900,
        Z                   = 5450,
        Y                   = -14800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 131098,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -16640,
        Z                   = 5700,
        Y                   = -13560,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 393242,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -13720,
        Z                   = 4950,
        Y                   = -9500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262170,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -13810,
        Z                   = 4950,
        Y                   = -4800,
        Direction           = 91,
        Unknown2            = 0,
        Unknown3            = 196635,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -14870,
        Z                   = 5200,
        Y                   = -4980,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262170,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -15810,
        Z                   = 5450,
        Y                   = -6530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 327706,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -15850,
        Z                   = 5450,
        Y                   = 3270,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 327707,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = 520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 65563,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -13720,
        Z                   = 4950,
        Y                   = 3330,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262171,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -14730,
        Z                   = 5200,
        Y                   = 1860,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 393243,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -13780,
        Z                   = 4950,
        Y                   = -8039,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 458779,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -15680,
        Z                   = 5450,
        Y                   = 550,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = -12660,
        Z                   = 4700,
        Y                   = 4760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 393242,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -13930,
        Z                   = 4950,
        Y                   = -3700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = -16620,
        Z                   = 5700,
        Y                   = -3710,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -15860,
        Z                   = 5450,
        Y                   = 4750,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196636,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -12730,
        Z                   = 4700,
        Y                   = -8010,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 131100,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = -16720,
        Z                   = 5700,
        Y                   = -13930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262172,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13800,
        Z                   = 4950,
        Y                   = -14740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 327708,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -14800,
        Z                   = 5200,
        Y                   = -14740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 65562,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -15640,
        Z                   = 5450,
        Y                   = -15910,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 131098,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -15790,
        Z                   = 5450,
        Y                   = -13450,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 393242,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16820,
        Z                   = 5700,
        Y                   = -17670,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262170,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16710,
        Z                   = 5700,
        Y                   = -16280,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196635,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16710,
        Z                   = 5700,
        Y                   = -14840,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262170,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -15840,
        Z                   = 5450,
        Y                   = -16740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 327706,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -14720,
        Z                   = 5200,
        Y                   = -16740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 327707,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -14860,
        Z                   = 5200,
        Y                   = -14050,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 65563,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -12700,
        Z                   = 4700,
        Y                   = -14100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262171,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -14670,
        Z                   = 5200,
        Y                   = -9220,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 393243,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -15900,
        Z                   = 5450,
        Y                   = -7990,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 458779,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -14820,
        Z                   = 5200,
        Y                   = -6520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -15740,
        Z                   = 5450,
        Y                   = -3710,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 393242,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -14700,
        Z                   = 5200,
        Y                   = -7290,
        Direction           = 90,
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
        X                   = -13790,
        Z                   = 4950,
        Y                   = -5620,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262172,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16740,
        Z                   = 5700,
        Y                   = -5620,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196636,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16690,
        Z                   = 5700,
        Y                   = -8690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 131100,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -15800,
        Z                   = 5450,
        Y                   = -5790,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 393243,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = -5670,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = -7390,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 458778,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -14700,
        Z                   = 5200,
        Y                   = -4400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262171,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16690,
        Z                   = 5700,
        Y                   = -7210,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 393243,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13760,
        Z                   = 4950,
        Y                   = -8770,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 327707,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13760,
        Z                   = 4950,
        Y                   = 530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13760,
        Z                   = 4950,
        Y                   = 1760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 131098,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -15870,
        Z                   = 5450,
        Y                   = 1130,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262170,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13900,
        Z                   = 4950,
        Y                   = 2470,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -12680,
        Z                   = 4700,
        Y                   = 4050,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 65563,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -15780,
        Z                   = 5450,
        Y                   = 4019,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 131098,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -14710,
        Z                   = 5200,
        Y                   = 2590,
        Direction           = 90,
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
        X                   = -12650,
        Z                   = 4950,
        Y                   = 1110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 393243,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = 2550,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 65562,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14670,
        Z                   = 4700,
        Y                   = 1910,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 262172,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14660,
        Z                   = 4700,
        Y                   = 680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 327708,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15770,
        Z                   = 4950,
        Y                   = 680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 65562,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16860,
        Z                   = 5200,
        Y                   = 680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 131098,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17850,
        Z                   = 5450,
        Y                   = 680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 393242,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18800,
        Z                   = 5700,
        Y                   = 680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 262170,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15910,
        Z                   = 4950,
        Y                   = 1830,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 196635,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16760,
        Z                   = 5200,
        Y                   = 1830,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 262170,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17780,
        Z                   = 5450,
        Y                   = 1990,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 327706,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1092",         # 00, 0
        "Function_1_154F",         # 01, 1
        "Function_2_155A",         # 02, 2
        "Function_3_40B0",         # 03, 3
        "Function_4_46A1",         # 04, 4
        "Function_5_488D",         # 05, 5
        "Function_6_4E28",         # 06, 6
        "Function_7_594E",         # 07, 7
        "Function_8_5E05",         # 08, 8
        "Function_9_63DD",         # 09, 9
        "Function_10_6982",        # 0A, 10
        "Function_11_6A73",        # 0B, 11
        "Function_12_76F4",        # 0C, 12
        "Function_13_812B",        # 0D, 13
        "Function_14_877C",        # 0E, 14
        "Function_15_8A41",        # 0F, 15
    )


    def Function_0_1092(): pass

    label("Function_0_1092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1224")
    ClearChrFlags(0x53, 0x80)
    ClearChrFlags(0x54, 0x80)
    ClearChrFlags(0x55, 0x80)
    ClearChrFlags(0x56, 0x80)
    ClearChrFlags(0x57, 0x80)
    ClearChrFlags(0x58, 0x80)
    ClearChrFlags(0x59, 0x80)
    ClearChrFlags(0x5A, 0x80)
    ClearChrFlags(0x5B, 0x80)
    ClearChrFlags(0x5C, 0x80)
    ClearChrFlags(0x5D, 0x80)
    ClearChrFlags(0x5E, 0x80)
    ClearChrFlags(0x5F, 0x80)
    ClearChrFlags(0x60, 0x80)
    ClearChrFlags(0x61, 0x80)
    ClearChrFlags(0x62, 0x80)
    ClearChrFlags(0x63, 0x80)
    ClearChrFlags(0x64, 0x80)
    ClearChrFlags(0x65, 0x80)
    ClearChrFlags(0x66, 0x80)
    ClearChrFlags(0x67, 0x80)
    ClearChrFlags(0x68, 0x80)
    ClearChrFlags(0x69, 0x80)
    ClearChrFlags(0x6A, 0x80)
    ClearChrFlags(0x6B, 0x80)
    ClearChrFlags(0x6C, 0x80)
    ClearChrFlags(0x6D, 0x80)
    ClearChrFlags(0x6E, 0x80)
    ClearChrFlags(0x6F, 0x80)
    ClearChrFlags(0x70, 0x80)
    ClearChrFlags(0x71, 0x80)
    ClearChrFlags(0x72, 0x80)
    ClearChrFlags(0x73, 0x80)
    ClearChrFlags(0x74, 0x80)
    ClearChrFlags(0x75, 0x80)
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
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4E, 0x80)
    ClearChrFlags(0x4F, 0x80)
    ClearChrFlags(0x50, 0x80)
    ClearChrFlags(0x51, 0x80)
    ClearChrFlags(0x52, 0x80)

    label("loc_1224")

    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, 17290, 9500, -4880, 270)
    SetChrPos(0x16, 17290, 9500, -8150, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_125E")
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_125E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_126C")
    OP_A3(0x3FB)
    Event(0, 4)

    label("loc_126C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_127A")
    OP_A3(0x3FC)
    Event(0, 5)

    label("loc_127A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_1288")
    OP_A3(0x3FD)
    Event(0, 7)

    label("loc_1288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 6)), scpexpr(EXPR_END)), "loc_1296")
    OP_A3(0x3FE)
    Event(0, 8)

    label("loc_1296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 7)), scpexpr(EXPR_END)), "loc_12A4")
    OP_A3(0x3FF)
    Event(0, 9)

    label("loc_12A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_12B2")
    OP_A3(0x3F0)
    Event(0, 10)

    label("loc_12B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_12C0")
    OP_A3(0x3F1)
    Event(0, 12)

    label("loc_12C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 2)), scpexpr(EXPR_END)), "loc_12CE")
    OP_A3(0x3F2)
    Event(0, 13)

    label("loc_12CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 3)), scpexpr(EXPR_END)), "loc_12DC")
    OP_A3(0x3F3)
    Event(0, 14)

    label("loc_12DC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_12F0"),
        (100, "loc_12F0"),
        (103, "loc_1306"),
        (SWITCH_DEFAULT, "loc_1342"),
    )


    label("loc_12F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1303")
    OP_A2(0x60E)
    Event(0, 2)

    label("loc_1303")

    Jump("loc_1342")

    label("loc_1306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1319")
    OP_A2(0x637)
    Event(0, 15)

    label("loc_1319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_132C")
    OP_A2(0x61E)
    Event(0, 6)

    label("loc_132C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133F")
    OP_A2(0x626)
    Event(0, 11)

    label("loc_133F")

    Jump("loc_1342")

    label("loc_1342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13D2")
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x22, -17490, 5950, -9620, 90)
    SetChrPos(0x23, -10510, 4200, -6570, 90)
    SetChrPos(0x9, -12660, 4700, -16340, 90)
    SetChrPos(0xA, -12670, 4700, -15020, 90)
    SetChrPos(0xB, -13760, 4950, -17160, 90)
    SetChrPos(0xC, -14580, 5200, -17680, 90)

    label("loc_13D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_13DC")
    Jump("loc_154E")

    label("loc_13DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_13E6")
    Jump("loc_154E")

    label("loc_13E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_13F0")
    Jump("loc_154E")

    label("loc_13F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_13FA")
    Jump("loc_154E")

    label("loc_13FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_149E")
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_END)), "loc_1437")
    ClearChrFlags(0x2F, 0x80)
    SetChrPos(0x2F, -14380, 5200, 4380, 98)

    label("loc_1437")

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
    ClearChrFlags(0x4E, 0x80)
    ClearChrFlags(0x4F, 0x80)
    ClearChrFlags(0x50, 0x80)
    ClearChrFlags(0x51, 0x80)
    ClearChrFlags(0x52, 0x80)
    Jump("loc_154E")

    label("loc_149E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_14A8")
    Jump("loc_154E")

    label("loc_14A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_14FA")
    ClearChrFlags(0x2A, 0x80)
    SetChrPos(0x2A, -14850, 5200, 4019, 90)
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
    Jump("loc_154E")

    label("loc_14FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1504")
    Jump("loc_154E")

    label("loc_1504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_153D")
    ClearChrFlags(0x2A, 0x80)
    SetChrPos(0x2A, -12690, 4700, -4810, 90)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    Jump("loc_154E")

    label("loc_153D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1547")
    Jump("loc_154E")

    label("loc_1547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_154E")

    label("loc_154E")

    Return()

    # Function_0_1092 end

    def Function_1_154F(): pass

    label("Function_1_154F")

    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    Return()

    # Function_1_154F end

    def Function_2_155A(): pass

    label("Function_2_155A")

    ClearChrFlags(0x53, 0x80)
    ClearChrFlags(0x54, 0x80)
    ClearChrFlags(0x55, 0x80)
    ClearChrFlags(0x56, 0x80)
    ClearChrFlags(0x57, 0x80)
    ClearChrFlags(0x58, 0x80)
    ClearChrFlags(0x59, 0x80)
    ClearChrFlags(0x5A, 0x80)
    ClearChrFlags(0x5B, 0x80)
    ClearChrFlags(0x5C, 0x80)
    ClearChrFlags(0x5D, 0x80)
    ClearChrFlags(0x5E, 0x80)
    ClearChrFlags(0x5F, 0x80)
    ClearChrFlags(0x60, 0x80)
    ClearChrFlags(0x61, 0x80)
    ClearChrFlags(0x62, 0x80)
    ClearChrFlags(0x63, 0x80)
    ClearChrFlags(0x64, 0x80)
    ClearChrFlags(0x65, 0x80)
    ClearChrFlags(0x66, 0x80)
    ClearChrFlags(0x67, 0x80)
    ClearChrFlags(0x68, 0x80)
    ClearChrFlags(0x69, 0x80)
    ClearChrFlags(0x6A, 0x80)
    ClearChrFlags(0x6B, 0x80)
    ClearChrFlags(0x6C, 0x80)
    ClearChrFlags(0x6D, 0x80)
    ClearChrFlags(0x6E, 0x80)
    ClearChrFlags(0x6F, 0x80)
    ClearChrFlags(0x70, 0x80)
    ClearChrFlags(0x71, 0x80)
    ClearChrFlags(0x72, 0x80)
    ClearChrFlags(0x73, 0x80)
    ClearChrFlags(0x74, 0x80)
    ClearChrFlags(0x75, 0x80)
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
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4E, 0x80)
    ClearChrFlags(0x4F, 0x80)
    ClearChrFlags(0x50, 0x80)
    ClearChrFlags(0x51, 0x80)
    ClearChrFlags(0x52, 0x80)
    SetChrPos(0x53, -13710, 4950, -16760, 90)
    SetChrPos(0x5D, -12690, 4700, -15820, 90)
    SetChrPos(0x35, -14950, 5200, 4040, 90)
    SetChrPos(0x68, -12650, 4700, -3710, 90)
    SetChrPos(0x69, -16730, 5700, 2520, 90)
    ClearChrFlags(0x76, 0x80)
    ClearChrFlags(0x77, 0x80)
    ClearChrFlags(0x78, 0x80)
    ClearChrFlags(0x79, 0x80)
    ClearChrFlags(0x7A, 0x80)
    ClearChrFlags(0x7B, 0x80)
    ClearChrFlags(0x7C, 0x80)
    ClearChrFlags(0x7D, 0x80)
    ClearChrFlags(0x7E, 0x80)
    OP_22(0xAE, 0x0, 0x64)
    EventBegin(0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x4)
    SetChrChipByIndex(0x21, 32)
    SetChrPos(0x21, 13860, 9850, -6510, 270)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 14630, 9750, -5420, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A8")
    SetChrPos(0x102, -10510, 4200, 5460, 270)
    SetChrPos(0x101, -10500, 4200, 4210, 270)
    Jump("loc_17CA")

    label("loc_17A8")

    SetChrPos(0x101, -10510, 4200, -16790, 270)
    SetChrPos(0x102, -10510, 4200, -17970, 270)

    label("loc_17CA")

    OP_6D(12190, 5450, -6580, 0)
    OP_67(0, 5170, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(180000, 0)
    OP_6E(441, 0)
    OP_66(0x0)

    def lambda_1810():
        OP_6D(-4240, 7800, 50, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1810)
    Sleep(6000)
    Fade(1000)
    OP_66(0x1)
    OP_48()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1859")
    OP_6D(-10980, 4200, 5030, 0)
    OP_6C(315000, 0)
    Jump("loc_1873")

    label("loc_1859")

    OP_6D(-10520, 4200, -17340, 0)
    OP_6C(224000, 0)

    label("loc_1873")

    OP_67(0, 6050, -10000, 0)
    OP_6B(3300, 0)
    OP_6E(262, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004FOh, wow...\x01",
            "Look at all these people!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYeah... There's some serious\x01",
            "enthusiasm in the air.\x02\x03",
            "Judging by the number of\x01",
            "spectators, this must\x01",
            "be a major event.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1950():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1950)
    Sleep(200)
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        (
            "#006FI wonder how far the\x01",
            "prelim rounds go.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thank you for your patience.\x01",
            "The 7th round is now starting.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006FOh... Looks like they're\x01",
            "starting up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FWell, let's go find ourselves\x01",
            "a place to sit down.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    SetChrPos(0x102, -12660, 4700, -6310, 90)
    SetChrPos(0x101, -12650, 4700, -7170, 90)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 5550, 0, -6570, 270)
    OP_6D(1000, 0, -6610, 0)
    OP_67(0, 18930, -27990, 0)
    OP_6B(700, 0)
    OP_6C(90000, 0)
    OP_6E(532, 0)
    OP_66(0x0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South side, blue team...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Border Patrol, 2nd Regiment team...\x01",
            "Captain is 2nd Lieutenant Sammy.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x19, 2260, 120, -24190, 0)
    SetChrPos(0x15, 1380, 120, -24190, 0)
    SetChrPos(0x16, 300, 120, -24190, 0)
    SetChrPos(0x17, -560, 120, -24190, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_6D(1200, 0, -21730, 2000)
    OP_70(0x0, 0x64)
    OP_73(0x0)
    Sleep(500)
    OP_22(0xAF, 0x0, 0x64)

    def lambda_1C02():
        OP_8E(0xFE, 0x8D4, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1C02)
    Sleep(300)

    def lambda_1C22():
        OP_8E(0xFE, 0xFFFFFDD0, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1C22)
    Sleep(50)

    def lambda_1C42():
        OP_8E(0xFE, 0x564, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1C42)
    Sleep(50)

    def lambda_1C62():
        OP_8E(0xFE, 0x12C, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1C62)
    OP_6D(1000, 0, -6610, 6000)

    ChrTalk(
        0x101,
        (
            "#004FHuh...? I thought the matches\x01",
            "were one-on-one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FI guess this one's a team outing.\x02\x03",
            "I could have sworn it was\x01",
            "individual bouts only, though...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "North side, red team...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Bracer Guild, Grancel branch\x01",
            "team... Captain is Kurt.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#501FHey, it's Carna's team!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWow. We got here just in\x01",
            "time to see them fight.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 2260, 120, 11000, 180)
    SetChrPos(0xA, 1380, 120, 11000, 180)
    SetChrPos(0xB, 300, 120, 11000, 180)
    SetChrPos(0xC, -560, 120, 11000, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_6D(880, 0, 8980, 2000)
    OP_70(0x1, 0x64)
    OP_73(0x1)
    Sleep(500)
    OP_22(0xAF, 0x0, 0x64)

    def lambda_1E89():
        OP_8E(0xFE, 0x8D4, 0x0, 0xFFFFEAAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E89)

    def lambda_1EA4():
        OP_8E(0xFE, 0x12C, 0x0, 0xFFFFEAAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1EA4)
    Sleep(60)

    def lambda_1EC4():
        OP_8E(0xFE, 0xFFFFFDD0, 0x0, 0xFFFFEAAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1EC4)
    Sleep(100)

    def lambda_1EE4():
        OP_8E(0xFE, 0x564, 0x0, 0xFFFFEAAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1EE4)
    OP_6D(1000, 0, -6610, 6000)
    Sleep(500)
    OP_8E(0x24, 0xB54, 0x0, 0xFFFFE6B0, 0xBB8, 0x0)

    ChrTalk(
        0x24,
        "This begins the 7th preliminary match.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Both teams, go to your\x01",
            "starting places.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F82():

        label("loc_1F82")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1F82")

    QueueWorkItem2(0x19, 1, lambda_1F82)

    def lambda_1F93():

        label("loc_1F93")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1F93")

    QueueWorkItem2(0x17, 1, lambda_1F93)

    def lambda_1FA4():

        label("loc_1FA4")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1FA4")

    QueueWorkItem2(0x15, 1, lambda_1FA4)

    def lambda_1FB5():

        label("loc_1FB5")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1FB5")

    QueueWorkItem2(0x16, 1, lambda_1FB5)

    def lambda_1FC6():
        OP_8E(0xFE, 0x406, 0x0, 0xFFFFCAAE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_1FC6)
    Sleep(200)

    def lambda_1FE6():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFD3C8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1FE6)

    def lambda_2001():
        OP_8E(0xFE, 0xA14, 0x0, 0xFFFFCE28, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2001)

    def lambda_201C():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xFFFFCE28, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_201C)

    def lambda_2037():

        label("loc_2037")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_2037")

    QueueWorkItem2(0xB, 1, lambda_2037)

    def lambda_2048():

        label("loc_2048")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_2048")

    QueueWorkItem2(0xA, 1, lambda_2048)

    def lambda_2059():

        label("loc_2059")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_2059")

    QueueWorkItem2(0x9, 1, lambda_2059)

    def lambda_206A():

        label("loc_206A")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_206A")

    QueueWorkItem2(0xC, 1, lambda_206A)

    def lambda_207B():
        OP_8E(0xFE, 0x186, 0x0, 0xFFFFF948, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_207B)

    def lambda_2096():
        OP_8E(0xFE, 0x596, 0x0, 0xFFFFF902, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2096)

    def lambda_20B1():
        OP_8E(0xFE, 0x8D4, 0x0, 0xFFFFFE48, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_20B1)

    def lambda_20CC():
        OP_8E(0xFE, 0xFFFFFDD0, 0x0, 0xFFFFFE48, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_20CC)
    Sleep(100)
    OP_8F(0x24, 0x190A, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    Sleep(1000)

    ChrTalk(
        0x24,
        "Take your positions!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    SetChrChipByIndex(0x19, 29)
    SetChrChipByIndex(0x15, 29)
    SetChrChipByIndex(0x16, 29)
    SetChrChipByIndex(0x17, 29)
    SetChrFlags(0x19, 0x2)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x16, 0x2)
    SetChrFlags(0x17, 0x2)
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x34), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 29)
    SetChrChipByIndex(0xA, 29)
    SetChrChipByIndex(0x9, 29)
    SetChrChipByIndex(0xC, 29)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0xC, 0x2)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    ChrTalk(
        0x24,
        "Begin!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x19, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xC, 0xFF)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_23(0xAE)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBB9, 0x100002, 0x0, 0x200, 0xFF)
    OP_22(0xAE, 0x0, 0x64)
    EventBegin(0x0)
    SetChrPos(0x19, 670, 0, -8630, 0)
    SetChrPos(0x15, 2400, 0, -9100, 0)
    SetChrPos(0x16, -120, 0, -9870, 0)
    SetChrPos(0x17, -1110, 0, -8890, 0)
    SetChrPos(0xB, 1480, 0, -4830, 180)
    SetChrPos(0xA, -1050, 0, -4440, 180)
    SetChrPos(0x9, 80, 0, -3240, 180)
    SetChrPos(0xC, 2650, 0, -3550, 180)
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x35), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x19, 0, 0)
    OP_8C(0x15, 45, 0)
    OP_8C(0x16, 315, 0)
    OP_8C(0x17, 45, 0)
    SetChrPos(0x102, -12660, 4700, -6310, 90)
    SetChrPos(0x101, -12650, 4700, -7170, 90)
    OP_66(0x0)
    OP_6D(1000, 0, -6610, 0)
    OP_67(-26990, 18930, -7100, 0)
    OP_6B(790, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x24,
        (
            "K.O.!\x01",
            "Winner is Kurt's Team!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_66(0x1)
    OP_6D(-12660, 4700, -6670, 0)
    OP_67(0, 4970, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)

    ChrTalk(
        0x101,
        (
            "#001FWOOHOOOOOO!!\x02\x03",
            "Goooooo, Carna!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThat was a good match.\x02\x03",
            "The soldiers move well, but the\x01",
            "bracers are better at working\x01",
            "as a team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FYeah! You could use their moves\x01",
            "for teaching lessons!\x02\x03",
            "#506FWow... I don't know what it is,\x01",
            "but watching martial artists at\x01",
            "work really gets me hyped up!\x02\x03",
            "I wish we had put off going to\x01",
            "the castle! I'd have liked to\x01",
            "see this from the beginning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FHa ha... Yeah, I know\x01",
            "how you feel.\x02\x03",
            "But part of being an adult is putting\x01",
            "one's own feelings aside in favor of\x01",
            "doing what needs to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009FHmph! Well, I like NOT being\x01",
            "an adult, yet.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Next up, we have the 8th\x01",
            "preliminary match.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "First, would the remaining\x01",
            "competitors step forward?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    Fade(1000)
    SetChrPos(0x102, -12660, 4700, -6310, 90)
    SetChrPos(0x101, -12650, 4700, -7170, 90)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 5550, 0, -6570, 270)
    OP_6D(1000, 0, -6610, 0)
    OP_67(0, 18930, -27990, 0)
    OP_6B(700, 0)
    OP_6C(90000, 0)
    OP_6E(532, 0)
    OP_66(0x0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South side, blue team...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Team Raven, captain is Belden.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x11, 2260, 120, -24190, 0)
    SetChrPos(0x25, 1380, 120, -24190, 0)
    SetChrPos(0x26, 300, 120, -24190, 0)
    SetChrPos(0x27, -560, 120, -24190, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    OP_6D(1200, 0, -21730, 2000)
    OP_70(0x0, 0x64)
    OP_73(0x0)
    Sleep(500)
    OP_22(0xAF, 0x0, 0x64)

    def lambda_2854():
        OP_8E(0xFE, 0xFFFFFDD0, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_2854)
    Sleep(50)

    def lambda_2874():
        OP_8E(0xFE, 0x564, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_2874)
    Sleep(50)

    def lambda_2894():
        OP_8E(0xFE, 0x12C, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_2894)

    def lambda_28AF():
        OP_8E(0xFE, 0x8D4, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_28AF)
    OP_6D(1000, 0, -6610, 6000)

    ChrTalk(
        0x101,
        (
            "#005FWha... What are those\x01",
            "guys doing here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FOh, yeah... It's that group from\x01",
            "the warehouse district in Ruan.\x02\x03",
            "Ah, I see. The competition's\x01",
            "open to the general public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FUgh... They stick out like\x01",
            "sore thumbs.\x02\x03",
            "They really don't deserve to\x01",
            "be counted among professional\x01",
            "soldiers and martial artists.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "North side, red team...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "From the neighboring Calvard\x01",
            "Republic, appearing alone,\x01",
            "is Zane.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004FZ-Zane?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FAnother familiar face, eh?\x01",
            "Small world.\x02\x03",
            "#012FBut fighting alone is going to\x01",
            "be a real handicap for him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FNo kidding...\x02\x03",
            "He may be fighting a bunch of\x01",
            "punks, but if they surround\x01",
            "him, he's in real trouble.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 2260, 120, 11000, 180)
    ClearChrFlags(0x8, 0x80)
    OP_6D(880, 0, 8980, 2000)
    OP_70(0x1, 0x64)
    OP_73(0x1)
    Sleep(500)
    OP_22(0xAF, 0x0, 0x64)

    def lambda_2BD4():
        OP_8E(0xFE, 0x352, 0x0, 0xFFFFEA84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2BD4)
    OP_6D(1000, 0, -6610, 6000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Zane will be competing in this\x01",
            "prelim bout solo, with no team\x01",
            "to stand at his side.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "He fights at a considerable disadvantage,\x01",
            "but his prodigious skill will make this\x01",
            "match a sight to behold.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We ask all in attendance to\x01",
            "understand the arrangement.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x24, 5550, 0, -6570, 270)
    OP_8E(0x24, 0xB54, 0x0, 0xFFFFE6B0, 0xBB8, 0x0)

    ChrTalk(
        0x24,
        "This begins the 8th preliminary match.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Both teams, go to your\x01",
            "starting places.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2DB5():

        label("loc_2DB5")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2DB5")

    QueueWorkItem2(0x11, 1, lambda_2DB5)

    def lambda_2DC6():

        label("loc_2DC6")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2DC6")

    QueueWorkItem2(0x25, 1, lambda_2DC6)

    def lambda_2DD7():

        label("loc_2DD7")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2DD7")

    QueueWorkItem2(0x26, 1, lambda_2DD7)

    def lambda_2DE8():

        label("loc_2DE8")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2DE8")

    QueueWorkItem2(0x27, 1, lambda_2DE8)

    def lambda_2DF9():
        OP_8E(0xFE, 0x406, 0x0, 0xFFFFCAAE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2DF9)
    Sleep(200)

    def lambda_2E19():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFD3C8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_2E19)

    def lambda_2E34():
        OP_8E(0xFE, 0xA14, 0x0, 0xFFFFCE28, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_2E34)

    def lambda_2E4F():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xFFFFCE28, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_2E4F)

    def lambda_2E6A():

        label("loc_2E6A")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_2E6A")

    QueueWorkItem2(0x8, 1, lambda_2E6A)

    def lambda_2E7B():
        OP_8E(0xFE, 0x2F8, 0x0, 0xFFFFFD44, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2E7B)
    Sleep(100)
    OP_8F(0x24, 0x190A, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    Sleep(1000)

    ChrTalk(
        0x24,
        "Ready...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    SetChrChipByIndex(0x11, 29)
    SetChrChipByIndex(0x25, 29)
    SetChrChipByIndex(0x26, 29)
    SetChrChipByIndex(0x27, 29)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x25, 0x2)
    SetChrFlags(0x26, 0x2)
    SetChrFlags(0x27, 0x2)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 25)
    Sleep(2000)

    ChrTalk(
        0x24,
        "Begin!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x11, 0xFF)
    OP_44(0x25, 0xFF)
    OP_44(0x26, 0xFF)
    OP_44(0x27, 0xFF)
    OP_44(0x8, 0xFF)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_23(0xAE)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBA, 0x100003, 0x0, 0x200, 0xFF)
    OP_22(0xAE, 0x0, 0x64)
    EventBegin(0x0)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x11, 1870, 0, -9140, 0)
    SetChrPos(0x25, -60, 0, -9780, 0)
    SetChrPos(0x26, 1090, 0, -10320, 0)
    SetChrPos(0x27, 2720, 0, -10150, 0)
    SetChrPos(0x8, 1120, 0, -4070, 180)
    SetChrPos(0x102, -12660, 4700, -6310, 90)
    SetChrPos(0x101, -12650, 4700, -7170, 90)
    OP_66(0x0)
    OP_6D(1000, 0, -6610, 0)
    OP_67(-26990, 18930, -7100, 0)
    OP_6B(790, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x24,
        (
            "K.O.!\x01",
            "Winner is Zane!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xB0, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_66(0x1)
    OP_6D(-12660, 4700, -6670, 0)
    OP_67(0, 4970, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x8, 0x80)

    ChrTalk(
        0x101,
        (
            "#001FYAAAAHOOOOOOOOOO!!!\x02\x03",
            "Goooo, Zane! That'll show 'em\x01",
            "what bracers are made of!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FLooks like I was worrying\x01",
            "over nothing.\x02\x03",
            "His build, speed and technique\x01",
            "make him a real force to be\x01",
            "reckoned with.\x02\x03",
            "#010FFor anyone else, though, I'd\x01",
            "say four-on-one is insane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007FYeah... Seriously...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The current match will mark\x01",
            "the end of the preliminaries.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Eight teams will be competing\x01",
            "in the no-holds-barred matches.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The competition opens tomorrow,\x01",
            "and over three days, the ultimate\x01",
            "champions will be decided.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Now, we will hear some words\x01",
            "from the tournament sponsor,\x01",
            "Duke Dunan.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_66(0x1)
    OP_6D(7100, 10100, -6310, 0)
    OP_67(0, 4570, -10000, 0)
    OP_6B(1160, 0)
    OP_6C(306000, 0)
    OP_6E(823, 0)
    SetChrChipByIndex(0x21, 18)
    SetChrPos(0x21, 11990, 9750, -6500, 270)
    SetChrPos(0x20, 14000, 9750, -7520, 270)
    OP_0D()

    ChrTalk(
        0x21,
        (
            "#225F#2P*a-HEM*\x02\x03",
            "#220FMy dear ladies and gentlemen.\x01",
            "I thank you for your efforts\x01",
            "in today's fine matches.\x02\x03",
            "I regret that government affairs\x01",
            "forced me to miss the first half\x01",
            "of them...\x02\x03",
            "#221F...but I was here for the second half, and\x01",
            "what I saw was an exciting and enjoyable\x01",
            "display of technique and talent.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x112, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x21,
        (
            "#225F#2PThe distressing news of recent terrorist\x01",
            "activities has had an unfortunate impact\x01",
            "on Her Majesty's health...\x02\x03",
            "#220FBut I ask that you take heart!\x02\x03",
            "She has entrusted her governmental duties\x01",
            "to me, Dunan von Auslese, and I will do all\x01",
            "that I can to live up to your expectations!\x02\x03",
            "Let us all remember the spirit and enthusiasm\x01",
            "we feel during this competition, and recall it\x01",
            "in the days ahead!\x02\x03",
            "#221FI hope you will all enjoy tomorrow's\x01",
            "no-holds-barred battle royale!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_66(0x1)
    OP_6D(-12660, 4700, -6670, 0)
    OP_67(0, 4970, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#509FI'm...uh... I'm not used to\x01",
            "hearing the duke speak so\x01",
            "decently to people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FHe probably just memorized\x01",
            "something written by the\x01",
            "Intelligence Division staff.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_66(0x1)
    OP_6D(7100, 10100, -6310, 0)
    OP_67(0, 4570, -10000, 0)
    OP_6B(1160, 0)
    OP_6C(306000, 0)
    OP_6E(823, 0)
    SetChrChipByIndex(0x21, 18)
    SetChrPos(0x21, 11990, 9750, -6500, 270)
    OP_0D()

    ChrTalk(
        0x21,
        (
            "#221F#2PHa ha ha... Ah, yes.\x02\x03",
            "#220FThe winner of the competition will not\x01",
            "only receive a prize in mira, but will\x01",
            "also get a special gift from me!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x20, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x20, 0x21, 400)

    ChrTalk(
        0x20,
        (
            "#721F(Y-Your Excellency... Are you\x01",
            "certain that this is wise?)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x20, 400)

    ChrTalk(
        0x21,
        (
            "#222F#5P(You be silent. This is a fine\x01",
            "opportunity to show my generosity.)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x21, 270, 400)
    OP_8C(0x20, 270, 400)

    ChrTalk(
        0x21,
        (
            "#225F#2PThis gift is to be...\x02\x03",
            "#224FA written invitation to a Royal\x01",
            "Court dinner party at Grancel\x01",
            "Castle, to be held in three days!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xB0, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x21,
        (
            "#221F#2PSadly, Her Majesty's presence will be\x01",
            "missed, but it will be attended by\x01",
            "celebrated persons of great renown!\x02\x03",
            "Arrangements have been made for\x01",
            "only the finest royal and noble\x01",
            "cuisine to be served.\x02\x03",
            "I trust that this will serve as\x01",
            "incentive for those competing\x01",
            "to excel and advance!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    FadeToDark(1500, 0, -1)
    OP_0D()
    TurnDirection(0x101, 0x102, 0)
    TurnDirection(0x102, 0x101, 0)
    OP_66(0x1)
    OP_6D(-12660, 4700, -6880, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2350, 0)
    OP_6C(134000, 0)
    OP_6E(261, 0)
    OP_23(0xAE)
    Sleep(3000)
    SetChrFlags(0x53, 0x80)
    SetChrFlags(0x54, 0x80)
    SetChrFlags(0x55, 0x80)
    SetChrFlags(0x56, 0x80)
    SetChrFlags(0x57, 0x80)
    SetChrFlags(0x58, 0x80)
    SetChrFlags(0x59, 0x80)
    SetChrFlags(0x5A, 0x80)
    SetChrFlags(0x5B, 0x80)
    SetChrFlags(0x5C, 0x80)
    SetChrFlags(0x5D, 0x80)
    SetChrFlags(0x5E, 0x80)
    SetChrFlags(0x5F, 0x80)
    SetChrFlags(0x60, 0x80)
    SetChrFlags(0x61, 0x80)
    SetChrFlags(0x62, 0x80)
    SetChrFlags(0x63, 0x80)
    SetChrFlags(0x64, 0x80)
    SetChrFlags(0x65, 0x80)
    SetChrFlags(0x66, 0x80)
    SetChrFlags(0x67, 0x80)
    SetChrFlags(0x68, 0x80)
    SetChrFlags(0x69, 0x80)
    SetChrFlags(0x6A, 0x80)
    SetChrFlags(0x6B, 0x80)
    SetChrFlags(0x6C, 0x80)
    SetChrFlags(0x6D, 0x80)
    SetChrFlags(0x6E, 0x80)
    SetChrFlags(0x6F, 0x80)
    SetChrFlags(0x70, 0x80)
    SetChrFlags(0x71, 0x80)
    SetChrFlags(0x72, 0x80)
    SetChrFlags(0x73, 0x80)
    SetChrFlags(0x74, 0x80)
    SetChrFlags(0x75, 0x80)
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
    SetChrFlags(0x76, 0x80)
    SetChrFlags(0x77, 0x80)
    SetChrFlags(0x78, 0x80)
    SetChrFlags(0x79, 0x80)
    SetChrFlags(0x7A, 0x80)
    SetChrFlags(0x7B, 0x80)
    SetChrFlags(0x7C, 0x80)
    SetChrFlags(0x7D, 0x80)
    SetChrFlags(0x7E, 0x80)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#003F#4PHey, Joshua...\x02\x03",
            "Are you thinking what\x01",
            "I'm thinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FYes... It would be ideal if\x01",
            "Carna got that invitation.\x02\x03",
            "If they win the championship, they'll\x01",
            "be allowed into the castle. It'll all\x01",
            "be above-board.\x02\x03",
            "That could give her the chance to\x01",
            "get that message to Her Majesty.\x02\x03",
            "#010FOr were you thinking something else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#4PNo, that's it, but...I hate the\x01",
            "idea of leaving someone else to \x01",
            "deliver the professor's message...\x02\x03",
            "Beggars can't be choosers,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI'd have no objections.\x02\x03",
            "Shall we try to catch them\x01",
            "in their waiting room before\x01",
            "they leave the arena?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#4PSure.\x02\x03",
            "Let's see... Carna's team came\x01",
            "out from the north gate, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FRight. If they're still here, that's\x01",
            "probably where we'll find them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x60E)
    OP_A2(0x60F)
    OP_28(0x45, 0x1, 0x1000)
    EventEnd(0x0)
    Return()

    # Function_2_155A end

    def Function_3_40B0(): pass

    label("Function_3_40B0")

    OP_22(0xAE, 0x0, 0x64)
    EventBegin(0x0)
    SetChrPos(0x2A, -12650, 4700, -3680, 90)
    SetChrPos(0x53, -12650, 4700, -16700, 90)
    SetChrPos(0x5E, -12650, 4700, -14700, 90)
    SetChrPos(0x6A, -13730, 4950, -16780, 90)
    SetChrPos(0x74, -12660, 4700, -15720, 90)
    SetChrPos(0x6F, -14780, 5200, 3980, 90)
    SetChrPos(0x5D, -13830, 4950, -15790, 90)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x104, 0x80)
    OP_9F(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x21, 19870, 9500, -6460, 270)
    SetChrPos(0x20, 20800, 9500, -5950, 270)
    OP_6D(-9450, 0, -6730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(500, 0)

    def lambda_41D1():
        OP_6E(339, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41D1)

    def lambda_41E1():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_41E1)

    def lambda_41F1():
        OP_6D(13540, 9750, -6540, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_41F1)
    FadeToBright(2000, 0)
    Sleep(3500)
    SetChrPos(0x30, 14650, 4700, 250, 270)
    SetChrPos(0x31, 15730, 4950, 250, 270)
    SetChrPos(0x32, 16860, 5200, 250, 270)
    SetChrPos(0x33, 17850, 5450, 250, 270)
    SetChrPos(0x34, 18880, 5700, 250, 270)
    SetChrPos(0x35, 19640, 5950, 250, 270)
    SetChrPos(0x36, 14650, 4700, 1200, 270)
    SetChrPos(0x37, 15730, 4950, 1200, 270)
    SetChrPos(0x38, 16860, 5200, 1200, 270)
    SetChrPos(0x39, 17850, 5450, 1200, 270)
    SetChrPos(0x3A, 18880, 5700, 1200, 270)
    SetChrPos(0x3B, 19640, 5950, 1200, 270)
    SetChrPos(0x3C, 14650, 4700, 2390, 270)
    SetChrPos(0x3D, 15730, 4950, 2390, 270)
    SetChrPos(0x3E, 16860, 5200, 2390, 270)
    SetChrPos(0x3F, 17850, 5450, 2390, 270)
    SetChrPos(0x40, 18880, 5700, 2390, 270)
    SetChrPos(0x41, 19640, 5950, 2390, 270)
    SetChrPos(0x42, 14650, 4700, 3550, 270)
    SetChrPos(0x43, 15730, 4950, 3550, 270)
    SetChrPos(0x44, 16860, 5200, 3550, 270)
    SetChrPos(0x45, 17850, 5450, 3550, 270)
    SetChrPos(0x46, 18880, 5700, 3550, 270)
    SetChrPos(0x47, 19640, 5950, 3550, 270)
    SetChrPos(0x48, 14650, 4700, 4830, 270)
    SetChrPos(0x49, 15730, 4950, 4830, 270)
    SetChrPos(0x4A, 16860, 5200, 4830, 270)
    SetChrPos(0x4B, 17850, 5450, 4830, 270)
    SetChrPos(0x4C, 18880, 5700, 4830, 270)
    SetChrPos(0x4D, 19640, 5950, 4830, 270)
    SetChrPos(0x4E, 14650, 4700, -13300, 270)
    SetChrPos(0x4F, 15730, 4950, -13300, 270)
    SetChrPos(0x50, 16860, 5200, -13300, 270)
    SetChrPos(0x51, 17850, 5450, -13300, 270)
    SetChrPos(0x52, 18880, 5700, -13300, 270)
    SetChrPos(0x53, 19640, 5950, -13300, 270)
    SetChrPos(0x54, 14650, 4700, -14500, 270)
    SetChrPos(0x55, 15730, 4950, -14500, 270)
    SetChrPos(0x56, 16860, 5200, -14500, 270)
    SetChrPos(0x57, 17850, 5450, -14500, 270)
    SetChrPos(0x58, 18880, 5700, -14500, 270)
    SetChrPos(0x59, 19640, 5950, -14500, 270)
    SetChrPos(0x5A, 14650, 4700, -15600, 270)
    SetChrPos(0x5B, 15730, 4950, -15600, 270)
    SetChrPos(0x5C, 16860, 5200, -15600, 270)
    SetChrPos(0x5D, 17850, 5450, -15600, 270)
    SetChrPos(0x5E, 18880, 5700, -15600, 270)
    SetChrPos(0x5F, 19640, 5950, -15600, 270)
    SetChrPos(0x60, 14650, 4700, -16920, 270)
    SetChrPos(0x61, 15730, 4950, -16920, 270)
    SetChrPos(0x62, 16860, 5200, -16920, 270)
    SetChrPos(0x63, 17850, 5450, -16920, 270)
    SetChrPos(0x64, 18880, 5700, -16920, 270)
    SetChrPos(0x65, 19640, 5950, -16920, 270)
    SetChrPos(0x66, 14650, 4700, -18030, 270)
    SetChrPos(0x67, 15730, 4950, -18030, 270)
    SetChrPos(0x68, 16860, 5200, -18030, 270)
    SetChrPos(0x69, 17850, 5450, -18030, 270)
    SetChrPos(0x6A, 18880, 5700, -18030, 270)
    SetChrPos(0x6B, 19640, 5950, -18030, 270)
    Sleep(6000)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    Sleep(1000)

    def lambda_4630():
        OP_8E(0xFE, 0x2A8A, 0x251C, 0xFFFFE6F6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4630)

    def lambda_464B():
        OP_8E(0xFE, 0x2A8A, 0x251C, 0xFFFFE6F6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_464B)

    def lambda_4666():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_4666)

    def lambda_4678():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_4678)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_40B0 end

    def Function_4_46A1(): pass

    label("Function_4_46A1")

    EventBegin(0x0)
    OP_22(0xAE, 0x0, 0x64)
    AddParty(0x1, 0xFF)
    AddParty(0x3, 0xFF)
    AddParty(0x7, 0xFF)
    OP_6D(810, 0, -6480, 0)
    OP_67(0, 15230, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(269000, 0)
    OP_6E(96, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, -4240, 0, -6480, 0)

    def lambda_470A():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_470A)

    def lambda_471A():
        OP_6E(524, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_471A)

    def lambda_472A():
        OP_67(0, 8010, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_472A)

    def lambda_4742():
        OP_8E(0xFE, 0x1734, 0x0, 0xFFFFE6B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4742)
    WaitChrThread(0x24, 0x1)
    OP_8C(0x24, 270, 400)
    WaitChrThread(0x101, 0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Without further ado, let's announce\x01",
            "the fight card for the first bout.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South side, blue team... Bracer\x01",
            "Guild, Grancel branch. Team\x01",
            "captain is Kurt!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "North side, red team... Royal Army\x01",
            "Assault Cavalry. Team captain is\x01",
            "1st Lieutenant Jed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_46A1 end

    def Function_5_488D(): pass

    label("Function_5_488D")

    EventBegin(0x0)
    OP_22(0xAE, 0x0, 0x64)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 5550, 0, -6570, 270)
    OP_6D(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    OP_6B(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x19, 2260, 0, -5460, 180)
    SetChrPos(0x15, 300, 0, -5460, 180)
    SetChrPos(0x16, -560, 0, -5460, 180)
    SetChrPos(0x17, 1380, 0, -5460, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, 2260, 0, -7590, 0)
    SetChrPos(0xB, 1380, 0, -7590, 0)
    SetChrPos(0xC, 300, 0, -7590, 0)
    SetChrPos(0xA, -560, 0, -7590, 0)
    Sleep(1000)

    ChrTalk(
        0x24,
        (
            "We now begin the 1st match of\x01",
            "the no-holds-barred tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Both teams, go to your\x01",
            "starting places.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)

    def lambda_4A3A():

        label("loc_4A3A")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_4A3A")

    QueueWorkItem2(0xB, 1, lambda_4A3A)

    def lambda_4A4B():

        label("loc_4A4B")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_4A4B")

    QueueWorkItem2(0xA, 1, lambda_4A4B)

    def lambda_4A5C():

        label("loc_4A5C")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_4A5C")

    QueueWorkItem2(0x9, 1, lambda_4A5C)

    def lambda_4A6D():

        label("loc_4A6D")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_4A6D")

    QueueWorkItem2(0xC, 1, lambda_4A6D)

    def lambda_4A7E():
        OP_8E(0xFE, 0x92E, 0x0, 0xFFFFCC8E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4A7E)
    Sleep(100)

    def lambda_4A9E():
        OP_8E(0xFE, 0xFFFFFF56, 0x0, 0xFFFFCC8E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_4A9E)
    Sleep(200)

    def lambda_4ABE():
        OP_8E(0xFE, 0x622, 0x0, 0xFFFFD35A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4ABE)

    def lambda_4AD9():
        OP_8E(0xFE, 0x186, 0x0, 0xFFFFD382, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4AD9)

    def lambda_4AF4():

        label("loc_4AF4")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_4AF4")

    QueueWorkItem2(0x19, 1, lambda_4AF4)

    def lambda_4B05():

        label("loc_4B05")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_4B05")

    QueueWorkItem2(0x17, 1, lambda_4B05)

    def lambda_4B16():

        label("loc_4B16")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_4B16")

    QueueWorkItem2(0x15, 1, lambda_4B16)

    def lambda_4B27():

        label("loc_4B27")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_4B27")

    QueueWorkItem2(0x16, 1, lambda_4B27)

    def lambda_4B38():
        OP_8E(0xFE, 0x438, 0x0, 0x2A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_4B38)
    Sleep(200)

    def lambda_4B58():
        OP_8E(0xFE, 0xFFFFFECA, 0x0, 0xFFFFFEDE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_4B58)
    Sleep(100)

    def lambda_4B78():
        OP_8E(0xFE, 0xA6E, 0x0, 0xFFFFFEC0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_4B78)
    Sleep(200)

    def lambda_4B98():
        OP_8E(0xFE, 0x438, 0x0, 0xFFFFF858, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_4B98)
    Sleep(100)
    OP_8F(0x24, 0x190A, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    Sleep(1000)

    ChrTalk(
        0x24,
        "Ready...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    SetChrChipByIndex(0x19, 29)
    SetChrChipByIndex(0x15, 29)
    SetChrChipByIndex(0x16, 29)
    SetChrChipByIndex(0x17, 29)
    SetChrFlags(0x19, 0x2)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x16, 0x2)
    SetChrFlags(0x17, 0x2)
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x36), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 29)
    SetChrChipByIndex(0xA, 29)
    SetChrChipByIndex(0x9, 29)
    SetChrChipByIndex(0xC, 29)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0xC, 0x2)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    ChrTalk(
        0x24,
        "Begin!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x19, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xC, 0xFF)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_23(0xAE)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBB, 0x100004, 0x0, 0x200, 0xFF)
    OP_22(0xAE, 0x0, 0x64)
    EventBegin(0x0)
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x37), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 1570, 0, -9320, 0)
    SetChrPos(0xA, -10, 0, -9870, 0)
    SetChrPos(0x9, 2360, 0, -10500, 0)
    SetChrPos(0xC, -1470, 0, -9110, 0)
    SetChrPos(0x19, 1690, 0, -4090, 180)
    SetChrPos(0x15, 20, 0, -3980, 180)
    SetChrPos(0x16, 2390, 0, -2970, 180)
    SetChrPos(0x17, -970, 0, -2780, 180)
    OP_6D(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    OP_6B(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x24,
        (
            "K.O.!\x01",
            "Winner is Kurt's Team!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_488D end

    def Function_6_4E28(): pass

    label("Function_6_4E28")

    EventBegin(0x0)
    OP_22(0xAE, 0x0, 0x64)
    SetMapFlags(0x100000)
    OP_66(0x0)
    OP_6D(1450, 0, -21650, 0)
    OP_67(-6800, 5030, -14300, 0)
    OP_6B(1530, 0)
    OP_6C(229000, 0)
    OP_6E(733, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 5550, 0, -6570, 270)
    SetChrPos(0x11, 2260, 0, -5460, 180)
    SetChrPos(0x13, 300, 0, -5460, 180)
    SetChrPos(0x14, -560, 0, -5460, 180)
    SetChrPos(0x12, 1380, 0, -5460, 180)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x11, 0x80)
    FadeToBright(2000, 0)
    SetChrPos(0x108, 2260, 0, -24190, 0)
    SetChrPos(0x101, 1380, 0, -24190, 0)
    SetChrPos(0x102, 300, 0, -24190, 0)
    SetChrPos(0x104, -560, 0, -24190, 0)
    OP_70(0x0, 0x64)
    OP_73(0x0)
    OP_66(0x0)

    def lambda_4F42():
        OP_6D(1160, 0, -6810, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F42)
    Sleep(500)
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)

    def lambda_4F69():
        OP_8E(0xFE, 0x8D4, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4F69)
    Sleep(300)

    def lambda_4F89():
        OP_8E(0xFE, 0xFFFFFDD0, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4F89)
    Sleep(50)

    def lambda_4FA9():
        OP_8E(0xFE, 0x564, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FA9)
    Sleep(50)

    def lambda_4FC9():
        OP_8E(0xFE, 0x12C, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4FC9)
    Sleep(6000)
    OP_66(0x1)
    Fade(1000)
    OP_6D(1130, 0, -6520, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3320, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x12,
        (
            "Heh heh... Never thought we'd\x01",
            "get a chance at revenge so soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I guess the Goddess smiles\x01",
            "on everyone at least once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#6PYou may have found our weaknesses\x01",
            "before, but we've been through\x01",
            "some insane training since then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#6PTime to let you see\x01",
            "the results!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FHa! Well, you've got spirit,\x01",
            "at least!\x02\x03",
            "I hope you're not expecting\x01",
            "us to take it easy on you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#4P(Umm... Is it just me, or is Estelle \x01",
            "a little livelier than usual?)\x02\x03",
            "(I'd almost call her attitude 'manly.')\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F(If she hears you saying that,\x01",
            "I'm not helping you.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F#4PAll right, it's just about time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "This begins the 2nd no-holds-\x01",
            "barred match of the competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Both teams, go to your\x01",
            "starting places.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    OP_6B(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    SetChrFlags(0x108, 0x40)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x104, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x11, 0x40)

    def lambda_5372():

        label("loc_5372")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_5372")

    QueueWorkItem2(0x108, 1, lambda_5372)

    def lambda_5383():

        label("loc_5383")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_5383")

    QueueWorkItem2(0x101, 1, lambda_5383)

    def lambda_5394():

        label("loc_5394")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_5394")

    QueueWorkItem2(0x102, 1, lambda_5394)

    def lambda_53A5():

        label("loc_53A5")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_53A5")

    QueueWorkItem2(0x104, 1, lambda_53A5)

    def lambda_53B6():
        OP_8E(0xFE, 0x406, 0x0, 0xFFFFCAAE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_53B6)
    Sleep(200)

    def lambda_53D6():
        OP_8E(0xFE, 0xA14, 0x0, 0xFFFFCEF0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_53D6)

    def lambda_53F1():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xFFFFCEF0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_53F1)
    Sleep(200)

    def lambda_5411():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFD3C8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5411)

    def lambda_542C():

        label("loc_542C")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_542C")

    QueueWorkItem2(0x12, 1, lambda_542C)

    def lambda_543D():

        label("loc_543D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_543D")

    QueueWorkItem2(0x13, 1, lambda_543D)

    def lambda_544E():

        label("loc_544E")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_544E")

    QueueWorkItem2(0x14, 1, lambda_544E)

    def lambda_545F():

        label("loc_545F")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_545F")

    QueueWorkItem2(0x11, 1, lambda_545F)

    def lambda_5470():
        OP_8E(0xFE, 0x438, 0x0, 0x2A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5470)
    Sleep(200)

    def lambda_5490():
        OP_8E(0xFE, 0xFFFFFECA, 0x0, 0xFFFFFCE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5490)

    def lambda_54AB():
        OP_8E(0xFE, 0xA6E, 0x0, 0xFFFFFCE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_54AB)
    Sleep(200)

    def lambda_54CB():
        OP_8E(0xFE, 0x438, 0x0, 0xFFFFF858, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_54CB)
    Sleep(100)
    OP_8F(0x24, 0x190A, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    Sleep(1000)

    ChrTalk(
        0x24,
        "Ready...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    SetChrChipByIndex(0x12, 29)
    SetChrChipByIndex(0x13, 29)
    SetChrChipByIndex(0x14, 29)
    SetChrChipByIndex(0x11, 29)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x13, 0x2)
    SetChrFlags(0x14, 0x2)
    SetChrFlags(0x11, 0x2)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x108, 25)
    SetChrChipByIndex(0x101, 22)
    SetChrChipByIndex(0x102, 23)
    SetChrChipByIndex(0x104, 24)
    Sleep(2000)

    ChrTalk(
        0x24,
        "Begin!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x104, 0xFF)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_23(0xAE)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x39D, 0x0, 0x0, 0x0, 0xFF)
    OP_22(0xAE, 0x0, 0x64)
    EventBegin(0x0)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 1100, 0, -8740, 0)
    SetChrPos(0x102, -160, 0, -9400, 0)
    SetChrPos(0x108, 2380, 0, -9800, 0)
    SetChrPos(0x104, 1070, 0, -10590, 0)
    SetChrPos(0x12, 1830, 0, -3910, 180)
    SetChrPos(0x13, 900, 0, -2670, 180)
    SetChrPos(0x14, 320, 0, -3480, 180)
    SetChrPos(0x11, 2610, 0, -2850, 180)
    OP_66(0x0)
    OP_6D(2410, 0, -7040, 0)
    OP_67(-26990, 18930, -7100, 0)
    OP_6B(660, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x24,
        (
            "K.O.!\x01",
            "Winner is Zane's Team!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x12,
        (
            "#5P*huff* *huff*...\x01",
            "Damn it... Lost again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#5PH-He's too damned tough...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5PShit! Shit, shit, SHIT!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#2PNow, now...\x01",
            "Don't get so discouraged.\x02\x03",
            "#006FTo be honest, I'm impressed. You\x01",
            "gave us a good run for our mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2PI agree.\x02\x03",
            "You're a lot stronger than when we\x01",
            "fought in the Varenne Lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5PR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5PI...uh, don't really remember\x01",
            "it too well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F#4PI wouldn't know, but it seems\x01",
            "we all gave it all we had.\x02\x03",
            "I think we can all return to\x01",
            "the waiting rooms with our\x01",
            "heads held high.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FE)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_4E28 end

    def Function_7_594E(): pass

    label("Function_7_594E")

    EventBegin(0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x19, 2260, 0, -7590, 0)
    SetChrPos(0x15, 300, 0, -7590, 0)
    SetChrPos(0x16, -560, 0, -7590, 0)
    SetChrPos(0x17, 1380, 0, -7590, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 5550, 0, -6570, 270)
    OP_6D(1000, 0, -6610, 0)
    OP_67(0, 18930, -27990, 0)
    OP_6B(700, 0)
    OP_6C(90000, 0)
    OP_6E(532, 0)
    OP_66(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrPos(0xD, 2260, 120, 11000, 180)
    SetChrPos(0xE, 1380, 120, 11000, 180)
    SetChrPos(0xF, 300, 120, 11000, 180)
    SetChrPos(0x10, -560, 120, 11000, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_6D(880, 0, 8980, 2000)
    OP_70(0x1, 0x64)
    OP_73(0x1)
    Sleep(500)
    OP_22(0xB0, 0x0, 0x64)

    def lambda_5A95():
        OP_8E(0xFE, 0x564, 0x0, 0xFFFFEA84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5A95)
    Sleep(50)

    def lambda_5AB5():
        OP_8E(0xFE, 0xFFFFFDD0, 0x0, 0xFFFFEA84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5AB5)
    Sleep(50)

    def lambda_5AD5():
        OP_8E(0xFE, 0x12C, 0x0, 0xFFFFEA84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5AD5)
    Sleep(50)

    def lambda_5AF5():
        OP_8E(0xFE, 0x8D4, 0x0, 0xFFFFEA84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5AF5)

    def lambda_5B10():
        OP_6D(1000, 0, -6610, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B10)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ladies and gentlemen.\x01",
            "We have a...unique match\x01",
            "for you up next.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Somewhat notorious, always in the news...\x01",
            "They are the Capua family, the Sky Bandits\x01",
            "who terrorized the Bose region!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Today they present themselves to you in\x01",
            "a physical display of contrition, eager\x01",
            "to fight in a fair and honest manner.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In doing so, they hope to atone for\x01",
            "all the problems they've caused the\x01",
            "Kingdom's citizens.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This wish to make amends is\x01",
            "foremost in their hearts as\x01",
            "they take the field.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And thanks to the sponsorship\x01",
            "of Duke Dunan, they are here\x01",
            "to show you that remorse.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We hope you enjoy this shocking\x01",
            "match-up and first ever public\x01",
            "apology in tournament history!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x3FF)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_594E end

    def Function_8_5E05(): pass

    label("Function_8_5E05")

    EventBegin(0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 5550, 0, -6570, 270)
    OP_6D(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    OP_6B(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x104, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x19, 2260, 0, -7590, 0)
    SetChrPos(0x15, 1380, 0, -7590, 0)
    SetChrPos(0x16, 300, 0, -7590, 0)
    SetChrPos(0x17, -560, 0, -7590, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0xD, 2260, 0, -5460, 180)
    SetChrPos(0xF, 300, 0, -5460, 180)
    SetChrPos(0x10, -560, 0, -5460, 180)
    SetChrPos(0xE, 1380, 0, -5460, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x24,
        (
            "Can I have your attention,\x01",
            "please!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "We now begin the 3rd match of\x01",
            "the no-holds-barred tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Both teams, go to your\x01",
            "starting places.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)

    def lambda_5FEE():

        label("loc_5FEE")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_5FEE")

    QueueWorkItem2(0xE, 1, lambda_5FEE)

    def lambda_5FFF():

        label("loc_5FFF")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_5FFF")

    QueueWorkItem2(0xF, 1, lambda_5FFF)

    def lambda_6010():

        label("loc_6010")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_6010")

    QueueWorkItem2(0x10, 1, lambda_6010)

    def lambda_6021():

        label("loc_6021")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_6021")

    QueueWorkItem2(0xD, 1, lambda_6021)

    def lambda_6032():
        OP_8E(0xFE, 0x406, 0x0, 0xFFFFCAAE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_6032)
    Sleep(200)

    def lambda_6052():
        OP_8E(0xFE, 0xA14, 0x0, 0xFFFFCE28, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_6052)

    def lambda_606D():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xFFFFCE28, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_606D)
    Sleep(200)

    def lambda_608D():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFD3C8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_608D)

    def lambda_60A8():

        label("loc_60A8")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_60A8")

    QueueWorkItem2(0x19, 1, lambda_60A8)

    def lambda_60B9():

        label("loc_60B9")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_60B9")

    QueueWorkItem2(0x17, 1, lambda_60B9)

    def lambda_60CA():

        label("loc_60CA")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_60CA")

    QueueWorkItem2(0x15, 1, lambda_60CA)

    def lambda_60DB():

        label("loc_60DB")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_60DB")

    QueueWorkItem2(0x16, 1, lambda_60DB)

    def lambda_60EC():
        OP_8E(0xFE, 0x8D4, 0x0, 0xFFFFFE48, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_60EC)

    def lambda_6107():
        OP_8E(0xFE, 0xFFFFFDD0, 0x0, 0xFFFFFE48, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6107)
    Sleep(200)

    def lambda_6127():
        OP_8E(0xFE, 0x186, 0x0, 0xFFFFF948, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_6127)

    def lambda_6142():
        OP_8E(0xFE, 0x596, 0x0, 0xFFFFF902, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_6142)
    Sleep(100)
    OP_8F(0x24, 0x190A, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    Sleep(1000)

    ChrTalk(
        0x24,
        "Take your positions!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    SetChrChipByIndex(0x19, 29)
    SetChrChipByIndex(0x15, 29)
    SetChrChipByIndex(0x16, 29)
    SetChrChipByIndex(0x17, 29)
    SetChrFlags(0x19, 0x2)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x16, 0x2)
    SetChrFlags(0x17, 0x2)
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x34), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 29)
    SetChrChipByIndex(0xF, 29)
    SetChrChipByIndex(0x10, 29)
    SetChrChipByIndex(0xD, 29)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0xD, 0x2)
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    ChrTalk(
        0x24,
        "Begin!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x19, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0xD, 0xFF)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_23(0xAE)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBC, 0x100005, 0x0, 0x200, 0xFF)
    OP_22(0xAE, 0x0, 0x64)
    EventBegin(0x0)
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x35), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x19, 1260, 0, -8950, 0)
    SetChrPos(0x15, 320, 0, -9900, 0)
    SetChrPos(0x16, 2130, 0, -10270, 0)
    SetChrPos(0x17, 2940, 0, -9340, 0)
    SetChrPos(0xE, 40, 0, -2660, 180)
    SetChrPos(0xF, 1100, 0, -3990, 180)
    SetChrPos(0x10, 2230, 0, -2600, 180)
    SetChrPos(0xD, 2040, 0, -3690, 180)
    OP_6D(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    OP_6B(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x24,
        (
            "K.O.!\x01",
            "Winner is Don's Team!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x3F0)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_5E05 end

    def Function_9_63DD(): pass

    label("Function_9_63DD")

    EventBegin(0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 5550, 0, -6570, 270)
    OP_6D(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    OP_6B(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1C, 2260, 0, -5460, 180)
    SetChrPos(0x1D, 300, 0, -5460, 180)
    SetChrPos(0x1E, -560, 0, -5460, 180)
    SetChrPos(0x1F, 1380, 0, -5460, 180)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x19, 2260, 0, -7590, 0)
    SetChrPos(0x15, 1380, 0, -7590, 0)
    SetChrPos(0x16, 300, 0, -7590, 0)
    SetChrPos(0x17, -560, 0, -7590, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x24,
        (
            "We now begin the 4th match of\x01",
            "the no-holds-barred tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Both teams, go to your\x01",
            "starting places.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1F, 0x40)

    def lambda_658A():

        label("loc_658A")

        TurnDirection(0xFE, 0x1F, 0)
        OP_48()
        Jump("loc_658A")

    QueueWorkItem2(0x19, 1, lambda_658A)

    def lambda_659B():

        label("loc_659B")

        TurnDirection(0xFE, 0x1F, 0)
        OP_48()
        Jump("loc_659B")

    QueueWorkItem2(0x15, 1, lambda_659B)

    def lambda_65AC():

        label("loc_65AC")

        TurnDirection(0xFE, 0x1F, 0)
        OP_48()
        Jump("loc_65AC")

    QueueWorkItem2(0x16, 1, lambda_65AC)

    def lambda_65BD():

        label("loc_65BD")

        TurnDirection(0xFE, 0x1F, 0)
        OP_48()
        Jump("loc_65BD")

    QueueWorkItem2(0x17, 1, lambda_65BD)

    def lambda_65CE():
        OP_8E(0xFE, 0x406, 0x0, 0xFFFFCAAE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_65CE)
    Sleep(200)

    def lambda_65EE():
        OP_8E(0xFE, 0xA14, 0x0, 0xFFFFCE28, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_65EE)

    def lambda_6609():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xFFFFCE28, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_6609)
    Sleep(200)

    def lambda_6629():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFD3C8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_6629)

    def lambda_6644():

        label("loc_6644")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_6644")

    QueueWorkItem2(0x1C, 1, lambda_6644)

    def lambda_6655():

        label("loc_6655")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_6655")

    QueueWorkItem2(0x1D, 1, lambda_6655)

    def lambda_6666():

        label("loc_6666")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_6666")

    QueueWorkItem2(0x1E, 1, lambda_6666)

    def lambda_6677():

        label("loc_6677")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_6677")

    QueueWorkItem2(0x1F, 1, lambda_6677)

    def lambda_6688():
        OP_8E(0xFE, 0x438, 0x0, 0x2A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_6688)
    Sleep(200)

    def lambda_66A8():
        OP_8E(0xFE, 0xFFFFFECA, 0x0, 0xFFFFFEDE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_66A8)

    def lambda_66C3():
        OP_8E(0xFE, 0xA6E, 0x0, 0xFFFFFEC0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_66C3)
    Sleep(200)

    def lambda_66E3():
        OP_8E(0xFE, 0x438, 0x0, 0xFFFFF858, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_66E3)
    Sleep(100)
    OP_8F(0x24, 0x190A, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    Sleep(1000)

    ChrTalk(
        0x24,
        "Take your positions!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    SetChrChipByIndex(0x19, 29)
    SetChrChipByIndex(0x15, 29)
    SetChrChipByIndex(0x16, 29)
    SetChrChipByIndex(0x17, 29)
    SetChrFlags(0x19, 0x2)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x16, 0x2)
    SetChrFlags(0x17, 0x2)
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x34), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1C, 29)
    SetChrChipByIndex(0x1D, 29)
    SetChrChipByIndex(0x1E, 29)
    SetChrChipByIndex(0x1F, 29)
    SetChrFlags(0x1C, 0x2)
    SetChrFlags(0x1D, 0x2)
    SetChrFlags(0x1E, 0x2)
    SetChrFlags(0x1F, 0x2)
    OP_51(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    ChrTalk(
        0x24,
        "Begin!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x19, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_23(0xAE)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBD, 0x100006, 0x0, 0x200, 0xFF)
    OP_22(0xAE, 0x0, 0x64)
    EventBegin(0x0)
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x35), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x19, 320, 0, -9150, 0)
    SetChrPos(0x15, 3630, 0, -8680, 0)
    SetChrPos(0x16, 1900, 0, -10130, 0)
    SetChrPos(0x17, -1110, 0, -10190, 0)
    SetChrPos(0x1C, 790, 0, -2710, 180)
    SetChrPos(0x1D, -400, 0, -3530, 180)
    SetChrPos(0x1E, 2470, 0, -3700, 180)
    SetChrPos(0x1F, 940, 0, -4430, 180)
    OP_6D(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    OP_6B(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x24,
        (
            "K.O.!\x01",
            "Winner is Lorence's Team!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x3F1)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_63DD end

    def Function_10_6982(): pass

    label("Function_10_6982")

    OP_22(0xAE, 0x0, 0x64)
    EventBegin(0x0)
    OP_6D(-13010, 4700, -19290, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(190000, 0)
    OP_6E(620, 0)
    SetChrPos(0x53, -12650, 4700, -16700, 90)
    SetChrPos(0x5E, -12650, 4700, -14700, 90)
    SetChrPos(0x6A, -13730, 4950, -16780, 90)
    SetChrPos(0x74, -12660, 4700, -15720, 90)
    SetChrPos(0x6F, -14780, 5200, 3980, 90)
    SetChrPos(0x5D, -13830, 4950, -15790, 90)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)

    def lambda_6A46():
        OP_6D(-13480, 4950, 3760, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A46)
    OP_6C(315000, 6000)
    SetMapFlags(0x100000)
    OP_A2(0x3F2)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_6982 end

    def Function_11_6A73(): pass

    label("Function_11_6A73")

    EventBegin(0x0)
    OP_22(0xAE, 0x0, 0x64)
    SetMapFlags(0x100000)
    OP_6D(-6270, 0, -6280, 0)
    OP_67(0, 11870, -10000, 0)
    OP_6B(3320, 0)
    OP_6C(90000, 0)
    OP_6E(505, 0)
    SetChrPos(0x53, -12650, 4700, -16700, 90)
    SetChrPos(0x5E, -12650, 4700, -14700, 90)
    SetChrPos(0x6A, -13730, 4950, -16780, 90)
    SetChrPos(0x74, -12660, 4700, -15720, 90)
    SetChrPos(0x6F, -14780, 5200, 3980, 90)
    SetChrPos(0x5D, -13830, 4950, -15790, 90)
    FadeToBright(2000, 0)

    def lambda_6B31():
        OP_6D(1840, 0, -7130, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B31)

    def lambda_6B49():
        OP_67(0, 5770, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B49)

    def lambda_6B61():
        OP_6C(135000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6B61)

    def lambda_6B71():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6B71)
    SetChrPos(0x108, 2260, 0, -7590, 0)
    SetChrPos(0x101, 1380, 0, -7590, 0)
    SetChrPos(0x102, 300, 0, -7590, 0)
    SetChrPos(0x104, -560, 0, -7590, 0)
    SetChrPos(0x9, 2260, 0, -5460, 180)
    SetChrPos(0xA, 1380, 0, -5460, 180)
    SetChrPos(0xB, 300, 0, -5460, 180)
    SetChrPos(0xC, -560, 0, -5460, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 5550, 0, -6570, 270)
    Sleep(5000)

    ChrTalk(
        0x9,
        (
            "#830F#3PHey, guys.\x01",
            "So you made it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#811F#3PHiya, rookies!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F#4PHa ha... Hi, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#4PWe gave as good as we got.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#822F#1P'Zane the Immovable.' I always\x01",
            "wanted to go up against you,\x01",
            "at least once.\x02\x03",
            "#1PWhat do you say we see if my sword\x01",
            "can match up to your skill?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#4PHa ha... Fine by me. But just to\x01",
            "warn you, I'm not big on pulling\x01",
            "my punches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#845F#1PHa ha... I was hoping to fight\x01",
            "in the final round...\x02\x03",
            "#1PI guess we'll see who fate\x01",
            "favors today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#4POn one hand, you have an advanced\x01",
            "group of veteran bracers.\x02\x03",
            "And on the other, a talented group\x01",
            "of novice bracers and one genius\x01",
            "performing musician.\x02\x03",
            "#035FI imagine even Aidios herself\x01",
            "might have difficulty at\x01",
            "guessing the outcome.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x24, 0xB54, 0x0, 0xFFFFE6B0, 0xBB8, 0x0)

    ChrTalk(
        0x24,
        (
            "We now begin the 5th match of\x01",
            "the no-holds-barred tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Both teams, go to your\x01",
            "starting places.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    OP_6B(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    SetChrFlags(0x108, 0x40)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x104, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x11, 0x40)

    def lambda_7015():

        label("loc_7015")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7015")

    QueueWorkItem2(0x108, 1, lambda_7015)

    def lambda_7026():

        label("loc_7026")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7026")

    QueueWorkItem2(0x101, 1, lambda_7026)

    def lambda_7037():

        label("loc_7037")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7037")

    QueueWorkItem2(0x102, 1, lambda_7037)

    def lambda_7048():

        label("loc_7048")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7048")

    QueueWorkItem2(0x104, 1, lambda_7048)

    def lambda_7059():
        OP_8E(0xFE, 0x406, 0x0, 0xFFFFCAAE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7059)
    Sleep(200)

    def lambda_7079():
        OP_8E(0xFE, 0xA14, 0x0, 0xFFFFCEF0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_7079)

    def lambda_7094():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xFFFFCEF0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7094)
    Sleep(200)

    def lambda_70B4():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFD3C8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70B4)

    def lambda_70CF():

        label("loc_70CF")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_70CF")

    QueueWorkItem2(0xB, 1, lambda_70CF)

    def lambda_70E0():

        label("loc_70E0")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_70E0")

    QueueWorkItem2(0xA, 1, lambda_70E0)

    def lambda_70F1():

        label("loc_70F1")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_70F1")

    QueueWorkItem2(0x9, 1, lambda_70F1)

    def lambda_7102():

        label("loc_7102")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_7102")

    QueueWorkItem2(0xC, 1, lambda_7102)

    def lambda_7113():
        OP_8E(0xFE, 0x186, 0x0, 0xFFFFF948, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_7113)

    def lambda_712E():
        OP_8E(0xFE, 0x596, 0x0, 0xFFFFF902, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_712E)

    def lambda_7149():
        OP_8E(0xFE, 0x8D4, 0x0, 0xFFFFFE48, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7149)

    def lambda_7164():
        OP_8E(0xFE, 0xFFFFFDD0, 0x0, 0xFFFFFE48, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_7164)
    Sleep(100)
    OP_8F(0x24, 0x190A, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    Sleep(1000)

    ChrTalk(
        0x24,
        "Take your positions!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    SetChrChipByIndex(0x108, 25)
    SetChrChipByIndex(0x101, 22)
    SetChrChipByIndex(0x102, 23)
    SetChrChipByIndex(0x104, 24)
    SetChrChipByIndex(0xB, 29)
    SetChrChipByIndex(0xA, 29)
    SetChrChipByIndex(0x9, 29)
    SetChrChipByIndex(0xC, 29)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0xC, 0x2)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    ChrTalk(
        0x24,
        "Begin!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x108, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x104, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xC, 0xFF)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_23(0xAE)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x39E, 0x0, 0x0, 0x0, 0xFF)
    OP_22(0xAE, 0x0, 0x64)
    EventBegin(0x0)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 1100, 0, -8740, 0)
    SetChrPos(0x102, -160, 0, -9400, 0)
    SetChrPos(0x108, 2380, 0, -9800, 0)
    SetChrPos(0x104, 1070, 0, -10590, 0)
    SetChrPos(0xB, 2540, 0, -4780, 180)
    SetChrPos(0xA, -970, 0, -4310, 180)
    SetChrPos(0x9, 20, 0, -3500, 180)
    SetChrPos(0xC, 1670, 0, -3790, 180)
    OP_66(0x0)
    OP_6D(2410, 0, -7040, 0)
    OP_67(-26990, 18930, -7100, 0)
    OP_6B(660, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x24,
        (
            "#6PK.O.!\x01",
            "Winner is Zane's Team!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#847F#6PGah... Nicely done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#826F#6PI never thought that 'Zane\x01",
            "the Immovable' was really\x01",
            "that capable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#4PYou guys were no slouches,\x01",
            "yourselves.\x02\x03",
            "I don't think I'd have won, if\x01",
            "not for the others backing me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2P*huff* *huff*\x01",
            "Did... Did we win?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#2PYeah...\x01",
            "Not sure how, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#835F#5PHa ha...\x01",
            "Oh, don't be so modest.\x02\x03",
            "#5PYou may have had Zane with\x01",
            "you, but you each pulled\x01",
            "your own weight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#856F#5PWhew... I knew fighting Schera's\x01",
            "students was going to be tough...\x02\x03",
            "#854F#5PBut I had no idea the black-haired kid\x01",
            "would be such a tough cookie...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#2PHeh, and I was thinking that\x01",
            "this girl was going to put me\x01",
            "to sleep...\x02\x03",
            "Perhaps later, we can discuss\x01",
            "each other's strengths over a\x01",
            "glass of wine...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#2POh, give it a rest.\x02",
    )

    CloseMessageWindow()
    OP_28(0x48, 0x1, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3F3)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_6A73 end

    def Function_12_76F4(): pass

    label("Function_12_76F4")

    EventBegin(0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 5550, 0, -6570, 270)
    OP_6D(1130, 0, -5670, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3320, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1C, 2260, 0, -5460, 180)
    SetChrPos(0x1D, 300, 0, -5460, 180)
    SetChrPos(0x1E, -560, 0, -5460, 180)
    SetChrPos(0x1F, 1380, 0, -5460, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xE, 2260, 0, -7590, 0)
    SetChrPos(0xF, 1380, 0, -7590, 0)
    SetChrPos(0x10, 300, 0, -7590, 0)
    SetChrPos(0xD, -560, 0, -7590, 0)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#190F#4PYo, little mister 'Masked Avenger.'\x02\x03",
            "I've been waiting for a chance\x01",
            "to pay back what I owe you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#200F#4PHeh heh... Yeah, we really ought\x01",
            "to thank the duke for this chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#280F#3PHa ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#214F#4PWh-What's so damned funny?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#280F#3PYou're orphans of the Capua\x01",
            "family...one of Erebonia's\x01",
            "ruined noble families...\x02\x03",
            "You lost your territory to a corrupt\x01",
            "merchant and only survived by taking\x01",
            "to air piracy...\x02\x03",
            "I was just thinking about what\x01",
            "a touching story that is.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#196F#4P#3SWha... What the hell?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#201F#4PHow do you know about that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#280F#3PDid you forget that we're part\x01",
            "of the Intelligence Division?\x02\x03",
            "You'd be better off abandoning\x01",
            "your little quest for revenge\x01",
            "and just serving your time quietly.\x02\x03",
            "It does seem that you're trying\x01",
            "to go straight, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#216F#4PYou... WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#204F#4PYou sure do love to run\x01",
            "your mouth, don'tcha?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#196FTime for you to taste a few\x01",
            "orbal-powered bullets!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x24, 0xB54, 0x0, 0xFFFFE6B0, 0xBB8, 0x0)

    ChrTalk(
        0x24,
        (
            "We now begin the 6th match of\x01",
            "the no-holds-barred tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Both teams, go to your\x01",
            "starting places.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    OP_6B(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1F, 0x40)

    def lambda_7D38():

        label("loc_7D38")

        TurnDirection(0xFE, 0x1F, 0)
        OP_48()
        Jump("loc_7D38")

    QueueWorkItem2(0xE, 1, lambda_7D38)

    def lambda_7D49():

        label("loc_7D49")

        TurnDirection(0xFE, 0x1F, 0)
        OP_48()
        Jump("loc_7D49")

    QueueWorkItem2(0xF, 1, lambda_7D49)

    def lambda_7D5A():

        label("loc_7D5A")

        TurnDirection(0xFE, 0x1F, 0)
        OP_48()
        Jump("loc_7D5A")

    QueueWorkItem2(0x10, 1, lambda_7D5A)

    def lambda_7D6B():

        label("loc_7D6B")

        TurnDirection(0xFE, 0x1F, 0)
        OP_48()
        Jump("loc_7D6B")

    QueueWorkItem2(0xD, 1, lambda_7D6B)

    def lambda_7D7C():
        OP_8E(0xFE, 0x92E, 0x0, 0xFFFFCC8E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_7D7C)

    def lambda_7D97():
        OP_8E(0xFE, 0xFFFFFF56, 0x0, 0xFFFFCC8E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_7D97)
    Sleep(200)

    def lambda_7DB7():
        OP_8E(0xFE, 0x622, 0x0, 0xFFFFD35A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_7DB7)

    def lambda_7DD2():
        OP_8E(0xFE, 0x186, 0x0, 0xFFFFD382, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_7DD2)

    def lambda_7DED():

        label("loc_7DED")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_7DED")

    QueueWorkItem2(0x1C, 1, lambda_7DED)

    def lambda_7DFE():

        label("loc_7DFE")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_7DFE")

    QueueWorkItem2(0x1D, 1, lambda_7DFE)

    def lambda_7E0F():

        label("loc_7E0F")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_7E0F")

    QueueWorkItem2(0x1E, 1, lambda_7E0F)

    def lambda_7E20():

        label("loc_7E20")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_7E20")

    QueueWorkItem2(0x1F, 1, lambda_7E20)

    def lambda_7E31():
        OP_8E(0xFE, 0x438, 0x0, 0x2A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_7E31)
    Sleep(200)

    def lambda_7E51():
        OP_8E(0xFE, 0xFFFFFECA, 0x0, 0xFFFFFEDE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_7E51)

    def lambda_7E6C():
        OP_8E(0xFE, 0xA6E, 0x0, 0xFFFFFEC0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_7E6C)
    Sleep(200)

    def lambda_7E8C():
        OP_8E(0xFE, 0x438, 0x0, 0xFFFFF858, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_7E8C)
    Sleep(100)
    OP_8F(0x24, 0x190A, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    Sleep(1000)

    ChrTalk(
        0x24,
        "Take your positions!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    SetChrChipByIndex(0xE, 29)
    SetChrChipByIndex(0xF, 29)
    SetChrChipByIndex(0x10, 29)
    SetChrChipByIndex(0xD, 29)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0xD, 0x2)
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x24), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1C, 29)
    SetChrChipByIndex(0x1D, 29)
    SetChrChipByIndex(0x1E, 29)
    SetChrChipByIndex(0x1F, 29)
    SetChrFlags(0x1C, 0x2)
    SetChrFlags(0x1D, 0x2)
    SetChrFlags(0x1E, 0x2)
    SetChrFlags(0x1F, 0x2)
    OP_51(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    ChrTalk(
        0x24,
        "Begin!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_23(0xAE)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBE, 0x100007, 0x0, 0x200, 0xFF)
    OP_22(0xAE, 0x0, 0x64)
    EventBegin(0x0)
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x25), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xE, 1540, 0, -9380, 0)
    SetChrPos(0xF, -170, 0, -9030, 0)
    SetChrPos(0x10, 730, 0, -10360, 0)
    SetChrPos(0xD, 2770, 0, -8750, 0)
    SetChrPos(0x1C, 790, 0, -2710, 180)
    SetChrPos(0x1D, -400, 0, -3530, 180)
    SetChrPos(0x1E, 2470, 0, -3700, 180)
    SetChrPos(0x1F, 940, 0, -4430, 180)
    OP_6D(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    OP_6B(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x24,
        (
            "K.O.!\x01",
            "Winner is Lorence's Team!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x3F4)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_76F4 end

    def Function_13_812B(): pass

    label("Function_13_812B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0xAE, 0x0, 0x64)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x104, 0x80)
    OP_9F(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x29, 0x4)
    SetChrFlags(0x28, 0x4)
    SetChrPos(0x21, 19870, 9500, -6460, 270)
    SetChrPos(0x20, 20800, 9500, -5950, 270)
    SetChrPos(0x29, 20290, 9750, -7200, 270)
    SetChrPos(0x28, 21100, 9500, -6600, 270)
    OP_6D(1210, 11600, -6480, 0)
    OP_67(0, 3630, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(269000, 0)
    OP_6E(428, 0)

    def lambda_822B():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_822B)
    FadeToBright(2000, 0)
    Sleep(4000)
    SetChrPos(0x30, 14650, 4700, 250, 270)
    SetChrPos(0x31, 15730, 4950, 250, 270)
    SetChrPos(0x32, 16860, 5200, 250, 270)
    SetChrPos(0x33, 17850, 5450, 250, 270)
    SetChrPos(0x34, 18880, 5700, 250, 270)
    SetChrPos(0x35, 19640, 5950, 250, 270)
    SetChrPos(0x36, 14650, 4700, 1200, 270)
    SetChrPos(0x37, 15730, 4950, 1200, 270)
    SetChrPos(0x38, 16860, 5200, 1200, 270)
    SetChrPos(0x39, 17850, 5450, 1200, 270)
    SetChrPos(0x3A, 18880, 5700, 1200, 270)
    SetChrPos(0x3B, 19640, 5950, 1200, 270)
    SetChrPos(0x3C, 14650, 4700, 2390, 270)
    SetChrPos(0x3D, 15730, 4950, 2390, 270)
    SetChrPos(0x3E, 16860, 5200, 2390, 270)
    SetChrPos(0x3F, 17850, 5450, 2390, 270)
    SetChrPos(0x40, 18880, 5700, 2390, 270)
    SetChrPos(0x41, 19640, 5950, 2390, 270)
    SetChrPos(0x42, 14650, 4700, 3550, 270)
    SetChrPos(0x43, 15730, 4950, 3550, 270)
    SetChrPos(0x44, 16860, 5200, 3550, 270)
    SetChrPos(0x45, 17850, 5450, 3550, 270)
    SetChrPos(0x46, 18880, 5700, 3550, 270)
    SetChrPos(0x47, 19640, 5950, 3550, 270)
    SetChrPos(0x48, 14650, 4700, 4830, 270)
    SetChrPos(0x49, 15730, 4950, 4830, 270)
    SetChrPos(0x4A, 16860, 5200, 4830, 270)
    SetChrPos(0x4B, 17850, 5450, 4830, 270)
    SetChrPos(0x4C, 18880, 5700, 4830, 270)
    SetChrPos(0x4D, 19640, 5950, 4830, 270)
    SetChrPos(0x4E, 14650, 4700, -13300, 270)
    SetChrPos(0x4F, 15730, 4950, -13300, 270)
    SetChrPos(0x50, 16860, 5200, -13300, 270)
    SetChrPos(0x51, 17850, 5450, -13300, 270)
    SetChrPos(0x52, 18880, 5700, -13300, 270)
    SetChrPos(0x53, 19640, 5950, -13300, 270)
    SetChrPos(0x54, 14650, 4700, -14500, 270)
    SetChrPos(0x55, 15730, 4950, -14500, 270)
    SetChrPos(0x56, 16860, 5200, -14500, 270)
    SetChrPos(0x57, 17850, 5450, -14500, 270)
    SetChrPos(0x58, 18880, 5700, -14500, 270)
    SetChrPos(0x59, 19640, 5950, -14500, 270)
    SetChrPos(0x5A, 14650, 4700, -15600, 270)
    SetChrPos(0x5B, 15730, 4950, -15600, 270)
    SetChrPos(0x5C, 16860, 5200, -15600, 270)
    SetChrPos(0x5D, 17850, 5450, -15600, 270)
    SetChrPos(0x5E, 18880, 5700, -15600, 270)
    SetChrPos(0x5F, 19640, 5950, -15600, 270)
    SetChrPos(0x60, 14650, 4700, -16920, 270)
    SetChrPos(0x61, 15730, 4950, -16920, 270)
    SetChrPos(0x62, 16860, 5200, -16920, 270)
    SetChrPos(0x63, 17850, 5450, -16920, 270)
    SetChrPos(0x64, 18880, 5700, -16920, 270)
    SetChrPos(0x65, 19640, 5950, -16920, 270)
    SetChrPos(0x66, 14650, 4700, -18030, 270)
    SetChrPos(0x67, 15730, 4950, -18030, 270)
    SetChrPos(0x68, 16860, 5200, -18030, 270)
    SetChrPos(0x69, 17850, 5450, -18030, 270)
    SetChrPos(0x6A, 18880, 5700, -18030, 270)
    SetChrPos(0x6B, 19640, 5950, -18030, 270)
    Sleep(5000)

    def lambda_864A():
        OP_6D(9560, 14150, -6480, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_864A)

    def lambda_8662():
        OP_67(0, 6940, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8662)

    def lambda_867A():
        OP_6E(314, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_867A)
    Sleep(1500)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    Sleep(2000)

    def lambda_86A7():
        OP_8E(0xFE, 0x2A8A, 0x251C, 0xFFFFE6F6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_86A7)

    def lambda_86C2():
        OP_8E(0xFE, 0x2A8A, 0x251C, 0xFFFFE6F6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_86C2)

    def lambda_86DD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_86DD)

    def lambda_86EF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_86EF)
    Sleep(300)

    def lambda_8706():
        OP_8E(0xFE, 0xEF6, 0x2616, 0xFFFFE3AE, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8706)

    def lambda_8721():
        OP_8E(0xFE, 0xEF6, 0x2616, 0xFFFFE3AE, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8721)

    def lambda_873C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_873C)

    def lambda_874E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_874E)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x100000)
    OP_A2(0x3F6)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_812B end

    def Function_14_877C(): pass

    label("Function_14_877C")

    EventBegin(0x0)
    OP_6D(-4350, 1700, -6590, 0)
    OP_67(0, 9590, -10000, 0)
    OP_6B(3970, 0)
    OP_6C(90000, 0)
    OP_6E(389, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 870, 0, -6590, 0)

    def lambda_87D7():
        OP_6B(2940, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_87D7)

    def lambda_87E7():
        OP_6D(1020, 0, -6570, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_87E7)

    def lambda_87FF():
        OP_8E(0xFE, 0x1734, 0x0, 0xFFFFE6B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_87FF)
    WaitChrThread(0x24, 0x1)
    OP_8C(0x24, 270, 400)
    WaitChrThread(0x101, 0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This arena has been abuzz with\x01",
            "preparations and fighting for\x01",
            "the better part of a week now...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...and it all culminates right\x01",
            "here, right now.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Which team will seize ultimate\x01",
            "victory this day?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Without further ado, I present\x01",
            "the fight card for this, the\x01",
            "championship match!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South side, blue team: From the\x01",
            "Calvard republic. Captain is Zane.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "North side, red team: From the Royal Army\x01",
            "Intelligence Division Special Forces:\x01",
            "Captain is 2nd Lieutenant Lorence!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x3F7)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_877C end

    def Function_15_8A41(): pass

    label("Function_15_8A41")

    EventBegin(0x0)
    SetMapFlags(0x100000)
    OP_22(0xAE, 0x0, 0x64)
    OP_6D(1010, 0, -20480, 0)
    OP_67(0, 2060, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(180000, 0)
    OP_6E(316, 0)
    OP_71(0x1, 0x4)
    FadeToDark(0, 0, -1)

    def lambda_8A9F():
        OP_6B(1380, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A9F)

    def lambda_8AAF():
        OP_6E(840, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8AAF)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 5550, 0, -6570, 270)
    Sleep(500)
    FadeToBright(2000, 0)
    SetChrPos(0x108, 2260, 0, -24190, 0)
    SetChrPos(0x101, 1380, 0, -24190, 0)
    SetChrPos(0x102, 300, 0, -24190, 0)
    SetChrPos(0x104, -560, 0, -24190, 0)
    SetChrPos(0x1C, 2260, 0, 11000, 180)
    SetChrPos(0x1D, 1380, 0, 11000, 180)
    SetChrPos(0x1E, 300, 0, 11000, 180)
    SetChrPos(0x1F, -560, 0, 11000, 180)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Sleep(2000)
    OP_70(0x0, 0x64)
    OP_70(0x1, 0x64)
    Sleep(3000)

    def lambda_8B97():
        OP_6D(1650, 0, -6810, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8B97)

    def lambda_8BAF():
        OP_6C(134000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8BAF)

    def lambda_8BBF():
        OP_67(0, 5420, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8BBF)
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)

    def lambda_8BE1():
        OP_8E(0xFE, 0x8D4, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_8BE1)
    Sleep(300)

    def lambda_8C01():
        OP_8E(0xFE, 0xFFFFFDD0, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8C01)
    Sleep(50)

    def lambda_8C21():
        OP_8E(0xFE, 0x564, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C21)
    Sleep(50)

    def lambda_8C41():
        OP_8E(0xFE, 0x12C, 0x0, 0xFFFFE25A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8C41)
    SetChrPos(0x1C, 2260, 0, -5460, 180)
    SetChrPos(0x1D, 1380, 0, -5460, 180)
    SetChrPos(0x1E, 300, 0, -5460, 180)
    SetChrPos(0x1F, -560, 0, -5460, 180)
    OP_72(0x1, 0x4)
    Sleep(6000)
    Fade(1000)
    OP_6B(1020, 0)
    OP_6C(45000, 0)
    OP_6D(910, 0, -6640, 0)
    OP_0D()

    ChrTalk(
        0x1C,
        (
            "(Everyone we've fought so far has\x01",
            "been about as tough as tapioca...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "(That, and half THIS team\x01",
            "is a pair of rookies.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "(I doubt they'd be able\x01",
            "to stand up to us.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#280F(Ha ha... Don't be so sure.)\x02\x03",
            "(Both of them are part\x01",
            "of the Bracer Guild.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "(Indeed...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "(We've been reading up on them...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#281F(Good. Now, stay focused. And\x01",
            "don't underestimate them.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "(...Yes, sir!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "(...Yes, sir!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#4POkay, what are those guys\x01",
            "grousing about over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#4PJust let them be, Estelle.\x02\x03",
            "If they're covering their faces like\x01",
            "that, I can't imagine they have much\x01",
            "in the way of self-confidence.\x02\x03",
            "Since they lack my dazzling good looks,\x01",
            "there's probably a lot of sniping and\x01",
            "backbiting in their ranks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "Wh-What the hell's THAT\x01",
            "supposed to mean?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I'll have you know I'm considered\x01",
            "VERY attractive to women!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4PUmm... 2nd Lieutenant Lorence,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#281FWhat is it, boy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4PJoshua...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#4PThat sword technique...\x02\x03",
            "#015F...no...never mind.\x02\x03",
            "#012FBest of luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#280FHeh... And to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#4P???\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#4PHey, don't let their talk get\x01",
            "you all depressed.\x02\x03",
            "We're about to start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "We now begin the final match of\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Both teams, go to your\x01",
            "starting places.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    OP_6B(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    SetChrFlags(0x108, 0x40)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x104, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1F, 0x40)

    def lambda_9247():

        label("loc_9247")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_9247")

    QueueWorkItem2(0x108, 1, lambda_9247)

    def lambda_9258():

        label("loc_9258")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_9258")

    QueueWorkItem2(0x101, 1, lambda_9258)

    def lambda_9269():

        label("loc_9269")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_9269")

    QueueWorkItem2(0x102, 1, lambda_9269)

    def lambda_927A():

        label("loc_927A")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_927A")

    QueueWorkItem2(0x104, 1, lambda_927A)

    def lambda_928B():
        OP_8E(0xFE, 0x406, 0x0, 0xFFFFCAAE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_928B)
    Sleep(200)

    def lambda_92AB():
        OP_8E(0xFE, 0xA14, 0x0, 0xFFFFCEF0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_92AB)

    def lambda_92C6():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xFFFFCEF0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_92C6)
    Sleep(200)

    def lambda_92E6():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFD3C8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_92E6)

    def lambda_9301():

        label("loc_9301")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_9301")

    QueueWorkItem2(0x1C, 1, lambda_9301)

    def lambda_9312():

        label("loc_9312")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_9312")

    QueueWorkItem2(0x1D, 1, lambda_9312)

    def lambda_9323():

        label("loc_9323")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_9323")

    QueueWorkItem2(0x1E, 1, lambda_9323)

    def lambda_9334():

        label("loc_9334")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_9334")

    QueueWorkItem2(0x1F, 1, lambda_9334)

    def lambda_9345():
        OP_8E(0xFE, 0x438, 0x0, 0x2A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_9345)
    Sleep(200)

    def lambda_9365():
        OP_8E(0xFE, 0xFFFFFECA, 0x0, 0xFFFFFEDE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_9365)

    def lambda_9380():
        OP_8E(0xFE, 0xA6E, 0x0, 0xFFFFFEC0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9380)
    Sleep(200)

    def lambda_93A0():
        OP_8E(0xFE, 0x438, 0x0, 0xFFFFF858, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_93A0)
    Sleep(100)
    OP_8F(0x24, 0x190A, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    Sleep(1000)

    ChrTalk(
        0x24,
        "Aidios be with you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "Ready...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    SetChrChipByIndex(0x1C, 29)
    SetChrChipByIndex(0x1D, 29)
    SetChrChipByIndex(0x1E, 29)
    SetChrChipByIndex(0x1F, 29)
    SetChrFlags(0x1C, 0x2)
    SetChrFlags(0x1D, 0x2)
    SetChrFlags(0x1E, 0x2)
    SetChrFlags(0x1F, 0x2)
    OP_51(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x108, 25)
    SetChrChipByIndex(0x101, 22)
    SetChrChipByIndex(0x102, 23)
    SetChrChipByIndex(0x104, 24)
    Sleep(2000)

    ChrTalk(
        0x24,
        "Begin!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x104, 0xFF)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_23(0xAE)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x39F, 0x0, 0x0, 0x0, 0xFF)
    OP_22(0xAE, 0x0, 0x64)
    EventBegin(0x0)
    OP_51(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 1100, 0, -8740, 0)
    SetChrPos(0x102, -160, 0, -9400, 0)
    SetChrPos(0x108, 2380, 0, -9800, 0)
    SetChrPos(0x104, 1070, 0, -10590, 0)
    SetChrPos(0x1C, 790, 0, -2710, 180)
    SetChrPos(0x1D, -400, 0, -3530, 180)
    SetChrPos(0x1E, 2470, 0, -3700, 180)
    SetChrPos(0x1F, 940, 0, -4430, 180)
    OP_66(0x0)
    OP_6D(2410, 0, -7040, 0)
    OP_67(-26990, 18930, -7100, 0)
    OP_6B(660, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x24,
        (
            "#6PK.O.!\x01",
            "Winner is Zane's Team!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PIt... It can't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PWe're the best of the best that\x01",
            "the Special Ops have to offer...\x01",
            "How could we lose...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#280F#5PBah... We're beaten...?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x101,
        "#001F#4P#5SYAHOOOOOOOOOOO!!!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#2PWe won...\x01",
            "We really won...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#034F#4P*huff*...*gasp*...\x01",
            "And I'm exhausted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#072F#4P...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_66(0x1)
    OP_6D(860, 0, -6420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrPos(0x20, 5470, 0, -6520, 270)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x19, 3500, 0, -5190, 270)
    SetChrPos(0x1B, 3500, 0, -7920, 270)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrChipByIndex(0x104, 65535)
    SetChrPos(0x20, 3290, 0, -7050, 270)
    SetChrPos(0x21, 2500, 0, -6550, 270)
    SetChrPos(0x101, -1310, 0, -5190, 90)
    SetChrPos(0x102, -1310, 0, -6120, 90)
    SetChrPos(0x108, -1310, 0, -6940, 90)
    SetChrPos(0x104, -1310, 0, -7920, 90)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Now, the winning team will be\x01",
            "blessed with a few words from\x01",
            "Duke Dunan.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Representing the team will\x01",
            "be Zane Vathek!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please, come forward.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x108,
        "#070FYes, sir.\x02",
    )

    CloseMessageWindow()

    def lambda_996C():
        OP_6D(1860, 0, -6420, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_996C)
    OP_8E(0x108, 0x3A2, 0x0, 0xFFFFE64C, 0x3E8, 0x0)
    TurnDirection(0x108, 0x21, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x21,
        (
            "#223F#6PWow... You look even\x01",
            "bigger up-close!\x02\x03",
            "Are all Easterners as\x01",
            "huge as you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#4PNo, I'm a little outside\x01",
            "the ordinary.\x02\x03",
            "I just ate well, slept well and\x01",
            "trained diligently, ever since I\x01",
            "was very young.\x02\x03",
            "I'm the way I am because I tend\x01",
            "to think about everything very\x01",
            "carefully and deeply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#221F#6PHa ha ha...\x01",
            "I see, I see.\x02\x03",
            "#220FI like you, Zane.\x02\x03",
            "Allow me to present you with the prize\x01",
            "of one hundred thousand mira, and the\x01",
            "invitation to the dinner party!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#074F#4PThank you very much, sir.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x21, 0x76C, 0x0, 0xFFFFE66A, 0x3E8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "Invitation\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x04",
            "100000\x07\x00",
            " mira.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    AddMira(50000)
    AddMira(50000)
    OP_8F(0x21, 0x9C4, 0x0, 0xFFFFE66A, 0x7D0, 0x0)
    OP_3F(0x375, 1)
    OP_3F(0x372, 1)

    ChrTalk(
        0x21,
        (
            "#220F#6PAidios shine her light and glory\x01",
            "upon you and your friends!\x02\x03",
            "#221FMy beloved citizens! Let's hear \x01",
            "a big round of applause for the\x01",
            "victors!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    OP_28(0x49, 0x1, 0x20)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3F8)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_8A41 end

    SaveToFile()

Try(main)
