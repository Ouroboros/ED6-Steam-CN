from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4107   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4107.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60018",
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
        'Carna',                                # 9
        'Anelace',                              # 10
        'Grant',                                # 11
        'Kurt',                                 # 12
        'Butler Phillip',                       # 13
        'Duke Dunan',                           # 14
        'Professor Alba',                       # 15
        'Dorothy',                              # 16
        'Patty',                                # 17
        'Ralph',                                # 18
        'Dick',                                 # 19
        'Raleigh',                              # 20
        'Troy',                                 # 21
        'Mayor Klaus',                          # 22
        'Spectator',                            # 23
        'Spectator',                            # 24
        'Spectator',                            # 25
        'Spectator',                            # 26
        'Spectator',                            # 27
        'Spectator',                            # 28
        'Spectator',                            # 29
        'Spectator',                            # 30
        'Spectator',                            # 31
        'Spectator',                            # 32
        'Spectator',                            # 33
        'Spectator',                            # 34
        'Spectator',                            # 35
        'Spectator',                            # 36
        'Spectator',                            # 37
        'Spectator',                            # 38
        'Spectator',                            # 39
        'Spectator',                            # 40
        'Spectator',                            # 41
        'Spectator',                            # 42
        'Spectator',                            # 43
        'Spectator',                            # 44
        'Spectator',                            # 45
        'Spectator',                            # 46
        'Spectator',                            # 47
        'Spectator',                            # 48
        'Spectator',                            # 49
        'Spectator',                            # 50
        'Spectator',                            # 51
        'Spectator',                            # 52
        'Spectator',                            # 53
        'Spectator',                            # 54
        'Spectator',                            # 55
        'Spectator',                            # 56
        'Spectator',                            # 57
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
        'ED6_DT07/CH01240 ._CH',             # 00
        'ED6_DT07/CH01630 ._CH',             # 01
        'ED6_DT07/CH01260 ._CH',             # 02
        'ED6_DT07/CH01620 ._CH',             # 03
        'ED6_DT07/CH02470 ._CH',             # 04
        'ED6_DT07/CH02140 ._CH',             # 05
        'ED6_DT07/CH02050 ._CH',             # 06
        'ED6_DT06/CH20063 ._CH',             # 07
        'ED6_DT07/CH01030 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01160 ._CH',             # 0A
        'ED6_DT07/CH01470 ._CH',             # 0B
        'ED6_DT07/CH01060 ._CH',             # 0C
        'ED6_DT07/CH02350 ._CH',             # 0D
        'ED6_DT07/CH01150 ._CH',             # 0E
        'ED6_DT07/CH01020 ._CH',             # 0F
        'ED6_DT07/CH01220 ._CH',             # 10
        'ED6_DT07/CH01460 ._CH',             # 11
        'ED6_DT07/CH01130 ._CH',             # 12
        'ED6_DT07/CH01200 ._CH',             # 13
        'ED6_DT07/CH01210 ._CH',             # 14
        'ED6_DT07/CH01100 ._CH',             # 15
        'ED6_DT07/CH01140 ._CH',             # 16
        'ED6_DT07/CH01680 ._CH',             # 17
        'ED6_DT07/CH01690 ._CH',             # 18
        'ED6_DT07/CH01120 ._CH',             # 19
        'ED6_DT07/CH01180 ._CH',             # 1A
        'ED6_DT07/CH01110 ._CH',             # 1B
        'ED6_DT07/CH01230 ._CH',             # 1C
        'ED6_DT07/CH01490 ._CH',             # 1D
        'ED6_DT07/CH01480 ._CH',             # 1E
        'ED6_DT06/CH20063 ._CH',             # 1F
    )

    AddCharChipPat(
        'ED6_DT07/CH01240P._CP',             # 00
        'ED6_DT07/CH01630P._CP',             # 01
        'ED6_DT07/CH01260P._CP',             # 02
        'ED6_DT07/CH01620P._CP',             # 03
        'ED6_DT07/CH02470P._CP',             # 04
        'ED6_DT07/CH02140P._CP',             # 05
        'ED6_DT07/CH02050P._CP',             # 06
        'ED6_DT06/CH20063P._CP',             # 07
        'ED6_DT07/CH01030P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01160P._CP',             # 0A
        'ED6_DT07/CH01470P._CP',             # 0B
        'ED6_DT07/CH01060P._CP',             # 0C
        'ED6_DT07/CH02350P._CP',             # 0D
        'ED6_DT07/CH01150P._CP',             # 0E
        'ED6_DT07/CH01020P._CP',             # 0F
        'ED6_DT07/CH01220P._CP',             # 10
        'ED6_DT07/CH01460P._CP',             # 11
        'ED6_DT07/CH01130P._CP',             # 12
        'ED6_DT07/CH01200P._CP',             # 13
        'ED6_DT07/CH01210P._CP',             # 14
        'ED6_DT07/CH01100P._CP',             # 15
        'ED6_DT07/CH01140P._CP',             # 16
        'ED6_DT07/CH01680P._CP',             # 17
        'ED6_DT07/CH01690P._CP',             # 18
        'ED6_DT07/CH01120P._CP',             # 19
        'ED6_DT07/CH01180P._CP',             # 1A
        'ED6_DT07/CH01110P._CP',             # 1B
        'ED6_DT07/CH01230P._CP',             # 1C
        'ED6_DT07/CH01490P._CP',             # 1D
        'ED6_DT07/CH01480P._CP',             # 1E
        'ED6_DT06/CH20063P._CP',             # 1F
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
        TalkScenaIndex      = 40,
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
        TalkScenaIndex      = 39,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 49,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 47,
    )

    DeclNpc(
        X                   = -12680,
        Z                   = 4700,
        Y                   = -4790,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = -12660,
        Z                   = 4700,
        Y                   = -3750,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = -14750,
        Z                   = 5200,
        Y                   = 3290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = -14750,
        Z                   = 5200,
        Y                   = 3960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = -14750,
        Z                   = 5200,
        Y                   = 4700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = -14740,
        Z                   = 5200,
        Y                   = -13430,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -15550,
        Z                   = 5450,
        Y                   = -5010,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = 3270,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -15550,
        Z                   = 5450,
        Y                   = -9240,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -15550,
        Z                   = 5450,
        Y                   = 1890,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = -6590,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -12680,
        Z                   = 4700,
        Y                   = -17670,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -14720,
        Z                   = 5200,
        Y                   = -3720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = 1670,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -13550,
        Z                   = 4950,
        Y                   = -13580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -14750,
        Z                   = 5200,
        Y                   = -8060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -14720,
        Z                   = 5200,
        Y                   = 510,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -12660,
        Z                   = 4700,
        Y                   = -9280,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -13550,
        Z                   = 4950,
        Y                   = 4710,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -14720,
        Z                   = 5200,
        Y                   = 4019,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -14520,
        Z                   = 5200,
        Y                   = -15970,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = -13490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -15610,
        Z                   = 5450,
        Y                   = -17700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -15610,
        Z                   = 5450,
        Y                   = -14800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -16640,
        Z                   = 5700,
        Y                   = -13560,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -13520,
        Z                   = 4950,
        Y                   = -9500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -13520,
        Z                   = 4950,
        Y                   = -4800,
        Direction           = 91,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -15440,
        Z                   = 5450,
        Y                   = -5520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -15440,
        Z                   = 5450,
        Y                   = -6530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -15440,
        Z                   = 5450,
        Y                   = 3270,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = 520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -13520,
        Z                   = 4950,
        Y                   = 3330,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = -14520,
        Z                   = 5200,
        Y                   = 1860,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -13520,
        Z                   = 4950,
        Y                   = -8039,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = -15440,
        Z                   = 5450,
        Y                   = 550,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -12660,
        Z                   = 4700,
        Y                   = 4760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -13520,
        Z                   = 4950,
        Y                   = -3700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = -16620,
        Z                   = 5700,
        Y                   = -3710,
        Direction           = 90,
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
        X                   = -15440,
        Z                   = 5450,
        Y                   = 4750,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = -12730,
        Z                   = 4700,
        Y                   = -8010,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )


    ScpFunction(
        "Function_0_7CA",          # 00, 0
        "Function_1_A1B",          # 01, 1
        "Function_2_A1C",          # 02, 2
        "Function_3_BA4",          # 03, 3
        "Function_4_BCE",          # 04, 4
        "Function_5_BF6",          # 05, 5
        "Function_6_C17",          # 06, 6
        "Function_7_C7D",          # 07, 7
        "Function_8_CAB",          # 08, 8
        "Function_9_DC5",          # 09, 9
        "Function_10_DF1",         # 0A, 10
        "Function_11_E4B",         # 0B, 11
        "Function_12_E98",         # 0C, 12
        "Function_13_F0C",         # 0D, 13
        "Function_14_F4A",         # 0E, 14
        "Function_15_F94",         # 0F, 15
        "Function_16_FFB",         # 10, 16
        "Function_17_1028",        # 11, 17
        "Function_18_1059",        # 12, 18
        "Function_19_1082",        # 13, 19
        "Function_20_10C4",        # 14, 20
        "Function_21_1133",        # 15, 21
        "Function_22_1199",        # 16, 22
        "Function_23_1214",        # 17, 23
        "Function_24_1280",        # 18, 24
        "Function_25_12C9",        # 19, 25
        "Function_26_12FE",        # 1A, 26
        "Function_27_1341",        # 1B, 27
        "Function_28_138D",        # 1C, 28
        "Function_29_1424",        # 1D, 29
        "Function_30_144F",        # 1E, 30
        "Function_31_14B8",        # 1F, 31
        "Function_32_153C",        # 20, 32
        "Function_33_159F",        # 21, 33
        "Function_34_160D",        # 22, 34
        "Function_35_167B",        # 23, 35
        "Function_36_16D1",        # 24, 36
        "Function_37_1760",        # 25, 37
        "Function_38_1784",        # 26, 38
        "Function_39_180A",        # 27, 39
        "Function_40_1981",        # 28, 40
        "Function_41_1A4B",        # 29, 41
        "Function_42_1A75",        # 2A, 42
        "Function_43_1B08",        # 2B, 43
        "Function_44_1B2E",        # 2C, 44
        "Function_45_1C88",        # 2D, 45
        "Function_46_1F19",        # 2E, 46
        "Function_47_2009",        # 2F, 47
        "Function_48_22F3",        # 30, 48
        "Function_49_26B4",        # 31, 49
    )


    def Function_0_7CA(): pass

    label("Function_0_7CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85A")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xE, -16580, 5700, -9620, 90)
    SetChrPos(0xF, -10500, 4200, -6510, 90)
    SetChrPos(0x8, -12710, 4700, -15880, 90)
    SetChrPos(0x9, -12670, 4700, -15020, 90)
    SetChrPos(0xA, -12650, 4700, -16690, 90)
    SetChrPos(0xB, -12650, 4700, -17560, 90)

    label("loc_85A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_864")
    Jump("loc_A1A")

    label("loc_864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_86E")
    Jump("loc_A1A")

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_878")
    Jump("loc_A1A")

    label("loc_878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_882")
    Jump("loc_A1A")

    label("loc_882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_948")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -12660, 4700, -6420, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -12660, 4700, -5620, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_END)), "loc_8E1")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -14490, 5200, 70, 90)

    label("loc_8E1")

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
    Jump("loc_A1A")

    label("loc_948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_952")
    Jump("loc_A1A")

    label("loc_952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9C6")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -13550, 4950, -6540, 90)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 4)), scpexpr(EXPR_END)), "loc_9C3")
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 31)
    SetChrPos(0xF, -10500, 4200, -6450, 90)

    label("loc_9C3")

    Jump("loc_A1A")

    label("loc_9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9D0")
    Jump("loc_A1A")

    label("loc_9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A09")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -12690, 4700, -4810, 90)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_A1A")

    label("loc_A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A13")
    Jump("loc_A1A")

    label("loc_A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A1A")

    label("loc_A1A")

    Return()

    # Function_0_7CA end

    def Function_1_A1B(): pass

    label("Function_1_A1B")

    Return()

    # Function_1_A1B end

    def Function_2_A1C(): pass

    label("Function_2_A1C")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4C")
    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_B8E")

    label("loc_A4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A65")
    OP_99(0xFE, 0x1, 0x7, 0x514)
    Jump("loc_B8E")

    label("loc_A65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7E")
    OP_99(0xFE, 0x2, 0x7, 0x4E2)
    Jump("loc_B8E")

    label("loc_A7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A97")
    OP_99(0xFE, 0x3, 0x7, 0x4B0)
    Jump("loc_B8E")

    label("loc_A97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB0")
    OP_99(0xFE, 0x4, 0x7, 0x47E)
    Jump("loc_B8E")

    label("loc_AB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC9")
    OP_99(0xFE, 0x5, 0x7, 0x44C)
    Jump("loc_B8E")

    label("loc_AC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE2")
    OP_99(0xFE, 0x6, 0x7, 0x41A)
    Jump("loc_B8E")

    label("loc_AE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFB")
    OP_99(0xFE, 0x0, 0x7, 0x54B)
    Jump("loc_B8E")

    label("loc_AFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B14")
    OP_99(0xFE, 0x1, 0x7, 0x519)
    Jump("loc_B8E")

    label("loc_B14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2D")
    OP_99(0xFE, 0x2, 0x7, 0x4E7)
    Jump("loc_B8E")

    label("loc_B2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B46")
    OP_99(0xFE, 0x3, 0x7, 0x4B5)
    Jump("loc_B8E")

    label("loc_B46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5F")
    OP_99(0xFE, 0x4, 0x7, 0x483)
    Jump("loc_B8E")

    label("loc_B5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B78")
    OP_99(0xFE, 0x5, 0x7, 0x451)
    Jump("loc_B8E")

    label("loc_B78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8E")
    OP_99(0xFE, 0x6, 0x7, 0x41F)

    label("loc_B8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BA3")
    OP_99(0xFE, 0x0, 0x7, 0x4B0)
    Jump("loc_B8E")

    label("loc_BA3")

    Return()

    # Function_2_A1C end

    def Function_3_BA4(): pass

    label("Function_3_BA4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I hope the match starts soon.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_BA4 end

    def Function_4_BCE(): pass

    label("Function_4_BCE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Can't wait to see who wins!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_BCE end

    def Function_5_BF6(): pass

    label("Function_5_BF6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "This is so exciting!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_BF6 end

    def Function_6_C17(): pass

    label("Function_6_C17")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "My excitement got the better of\x01",
            "me, and I showed up waaaaaaaaay\x01",
            "earlier than I needed to.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_C17 end

    def Function_7_C7D(): pass

    label("Function_7_C7D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Who should I cheer for this year?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_C7D end

    def Function_8_CAB(): pass

    label("Function_8_CAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_D2D")

    ChrTalk(
        0xFE,
        (
            "I...feel like someone behind me\x01",
            "is giving me the evil eye. Real,\x01",
            "real bad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is it...just my imagination...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_DC1")

    label("loc_D2D")

    OP_A2(0x5)
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "I...feel like someone behind me\x01",
            "is giving me the evil eye. Real,\x01",
            "real bad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is it...just my imagination...?\x02",
    )

    CloseMessageWindow()

    label("loc_DC1")

    TalkEnd(0xFE)
    Return()

    # Function_8_CAB end

    def Function_9_DC5(): pass

    label("Function_9_DC5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Crap, I forgot my orbal camera!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_DC5 end

    def Function_10_DF1(): pass

    label("Function_10_DF1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Wait, so the Royal Guardsmen\x01",
            "aren't in the tournament this\x01",
            "year?! That sucks!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_DF1 end

    def Function_11_E4B(): pass

    label("Function_11_E4B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This team battle thing is more\x01",
            "interesting than I'd anticipated.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_E4B end

    def Function_12_E98(): pass

    label("Function_12_E98")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The Special Ops team is totally\x01",
            "gonna win it all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Black suits them well. They look\x01",
            "tough as nails!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_E98 end

    def Function_13_F0C(): pass

    label("Function_13_F0C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "What do you think today's match-ups\x01",
            "will be like?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_F0C end

    def Function_14_F4A(): pass

    label("Function_14_F4A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Two bracer teams remain...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Go for the gold, both of you!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_F4A end

    def Function_15_F94(): pass

    label("Function_15_F94")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Those Special Ops guys are creepy...\x01",
            "but they've got it goin' on strength-\x01",
            "wise, for sure!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_F94 end

    def Function_16_FFB(): pass

    label("Function_16_FFB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Just hurry up and start already!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_FFB end

    def Function_17_1028(): pass

    label("Function_17_1028")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I've been waiting for this all\x01",
            "year!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1028 end

    def Function_18_1059(): pass

    label("Function_18_1059")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Championship today! WOOOOOO!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1059 end

    def Function_19_1082(): pass

    label("Function_19_1082")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I wonder who'll win...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's going to be amazing!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_1082 end

    def Function_20_10C4(): pass

    label("Function_20_10C4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I like that blond boy on the\x01",
            "bracer team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He looks laid back, but he's\x01",
            "got such a quick draw!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_10C4 end

    def Function_21_1133(): pass

    label("Function_21_1133")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I want to see the masked guy\x01",
            "and the big guy go at it head-\x01",
            "to-head. That'd be something!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_1133 end

    def Function_22_1199(): pass

    label("Function_22_1199")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Everybody came super-early because it's\x01",
            "the finals. Guess they figured seats\x01",
            "would fill up fast. And they did!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_1199 end

    def Function_23_1214(): pass

    label("Function_23_1214")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Two first-year teams making it\x01",
            "to the finals...and both poised\x01",
            "to win it all! Which will it be?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_1214 end

    def Function_24_1280(): pass

    label("Function_24_1280")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "There's a girl on the bracer team,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Good for her!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_1280 end

    def Function_25_12C9(): pass

    label("Function_25_12C9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "On with the show, ya' whipper-\x01",
            "snappers!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_12C9 end

    def Function_26_12FE(): pass

    label("Function_26_12FE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Grandpa and I love watching\x01",
            "the tournament every year.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_12FE end

    def Function_27_1341(): pass

    label("Function_27_1341")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I was so excited for today's events,\x01",
            "I couldn't sleep one wink!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_1341 end

    def Function_28_138D(): pass

    label("Function_28_138D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I really think the Special Ops\x01",
            "team is a shoe-in this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, just the name 'Special\x01",
            "Ops' alone has such an awesome\x01",
            "ring to it!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_138D end

    def Function_29_1424(): pass

    label("Function_29_1424")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I'm gonna shout myself hoarse!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_1424 end

    def Function_30_144F(): pass

    label("Function_30_144F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I'll be cheering for the bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're always there to help when\x01",
            "people are in need.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_144F end

    def Function_31_14B8(): pass

    label("Function_31_14B8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Maybe I should have packed a\x01",
            "lunch today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was in line from such an ungoddessly\x01",
            "hour, I'm already hungry again...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_14B8 end

    def Function_32_153C(): pass

    label("Function_32_153C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The Martial Arts Competition\x01",
            "is always so much fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Every year, I get so INTO it!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_153C end

    def Function_33_159F(): pass

    label("Function_33_159F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "That boy on the bracer team\x01",
            "looks about as old as my son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think I'll cheer for them today.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_159F end

    def Function_34_160D(): pass

    label("Function_34_160D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If teamwork is the deciding factor,\x01",
            "then Special Ops have the champion-\x01",
            "ship in the bag for sure.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_160D end

    def Function_35_167B(): pass

    label("Function_35_167B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I would've never predicted the\x01",
            "match-ups to go in the direction\x01",
            "they did.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_167B end

    def Function_36_16D1(): pass

    label("Function_36_16D1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Royal Army vs. Bracer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both of them fight to protect people as\x01",
            "part of their jobs. Now...I guess we see\x01",
            "who's better at it!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_16D1 end

    def Function_37_1760(): pass

    label("Function_37_1760")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Time to start cheering!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_1760 end

    def Function_38_1784(): pass

    label("Function_38_1784")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1806")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_END)), "loc_1806")

    ChrTalk(
        0x15,
        (
            "#600FI haven't watched the Martial\x01",
            "Arts Competition since I was\x01",
            "a young man.\x02\x03",
            "Good luck out there, you two!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1806")

    TalkEnd(0xFE)
    Return()

    # Function_38_1784 end

    def Function_39_180A(): pass

    label("Function_39_180A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_18C2")

    ChrTalk(
        0xFE,
        (
            "#816FI heard your opponents are really\x01",
            "tough...but you guys should be able\x01",
            "to take 'em, no sweat!\x02\x03",
            "We'll be screaming ourselves hoarse\x01",
            "for you, so go knock 'em dead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197D")

    label("loc_18C2")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#850FHey, newbies!\x02\x03",
            "Your opponents are tough, but\x01",
            "you guys should be able to take\x01",
            "'em, no sweat.\x02\x03",
            "#816FBreak a leg out there. We'll be\x01",
            "cheering for you like you wouldn't\x01",
            "believe!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197D")

    TalkEnd(0xFE)
    Return()

    # Function_39_180A end

    def Function_40_1981(): pass

    label("Function_40_1981")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_19E1")

    ChrTalk(
        0xFE,
        (
            "#830FListen, just relax and do what\x01",
            "you've always done.\x02\x03",
            "There's no pressure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A47")

    label("loc_19E1")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "#830FHey, you guys.\x02\x03",
            "Listen, just relax and do what\x01",
            "you've always done.\x02\x03",
            "There's no pressure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A47")

    TalkEnd(0xFE)
    Return()

    # Function_40_1981 end

    def Function_41_1A4B(): pass

    label("Function_41_1A4B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I hope the match starts soon.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_1A4B end

    def Function_42_1A75(): pass

    label("Function_42_1A75")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I got up extra-early today so\x01",
            "I could rouse these two and get\x01",
            "some good seats at the arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd never miss a spectacle like this!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_1A75 end

    def Function_43_1B08(): pass

    label("Function_43_1B08")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Who'll win, do you think?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_1B08 end

    def Function_44_1B2E(): pass

    label("Function_44_1B2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1B3B")
    Jump("loc_1C84")

    label("loc_1B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1B45")
    Jump("loc_1C84")

    label("loc_1B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1B4F")
    Jump("loc_1C84")

    label("loc_1B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1B59")
    Jump("loc_1C84")

    label("loc_1B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1C4B")

    ChrTalk(
        0xFE,
        (
            "I was gonna camp out to get\x01",
            "some good seats, but the night\x01",
            "patrol made me go home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, I did the only sensible thing. I snuck out\x01",
            "of the house, hid in my bushes, and waited for\x01",
            "the soldiers to leave. Then bam...line city!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C84")

    label("loc_1C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1C55")
    Jump("loc_1C84")

    label("loc_1C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1C5F")
    Jump("loc_1C84")

    label("loc_1C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C69")
    Jump("loc_1C84")

    label("loc_1C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1C73")
    Jump("loc_1C84")

    label("loc_1C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1C7D")
    Jump("loc_1C84")

    label("loc_1C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1C84")

    label("loc_1C84")

    TalkEnd(0xFE)
    Return()

    # Function_44_1B2E end

    def Function_45_1C88(): pass

    label("Function_45_1C88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1C95")
    Jump("loc_1F15")

    label("loc_1C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1C9F")
    Jump("loc_1F15")

    label("loc_1C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1CA9")
    Jump("loc_1F15")

    label("loc_1CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1CB3")
    Jump("loc_1F15")

    label("loc_1CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1D43")

    ChrTalk(
        0xFE,
        (
            "My husband went through a lot to\x01",
            "get us some good seats yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe he went through\x01",
            "all of that just for me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F15")

    label("loc_1D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1D4D")
    Jump("loc_1F15")

    label("loc_1D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1ECD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1DF9")

    ChrTalk(
        0xFE,
        (
            "Front row center is my seat of\x01",
            "choice, don't you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, as they say, the early bird\x01",
            "gets the worm! Best get here even\x01",
            "earlier tomorrow...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ECA")

    label("loc_1DF9")

    OP_A2(0x1)
    OP_62(0xFE, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Ugh, this sucks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Front row center is my seat of\x01",
            "choice, don't you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, as they say, the early bird\x01",
            "gets the worm! Best get here even\x01",
            "earlier tomorrow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECA")

    Jump("loc_1F15")

    label("loc_1ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1ED7")
    Jump("loc_1F15")

    label("loc_1ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1F04")

    ChrTalk(
        0xFE,
        "It's that time of year again!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F15")

    label("loc_1F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1F0E")
    Jump("loc_1F15")

    label("loc_1F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1F15")

    label("loc_1F15")

    TalkEnd(0xFE)
    Return()

    # Function_45_1C88 end

    def Function_46_1F19(): pass

    label("Function_46_1F19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1F26")
    Jump("loc_2005")

    label("loc_1F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1F30")
    Jump("loc_2005")

    label("loc_1F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1F3A")
    Jump("loc_2005")

    label("loc_1F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1F44")
    Jump("loc_2005")

    label("loc_1F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1FCC")

    ChrTalk(
        0xFE,
        (
            "#820FWe're all here to root for you\x01",
            "today!\x02\x03",
            "You're representing the Bracer\x01",
            "Guild out there. So be sure to\x01",
            "make us proud!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2005")

    label("loc_1FCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1FD6")
    Jump("loc_2005")

    label("loc_1FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1FE0")
    Jump("loc_2005")

    label("loc_1FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1FEA")
    Jump("loc_2005")

    label("loc_1FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1FF4")
    Jump("loc_2005")

    label("loc_1FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1FFE")
    Jump("loc_2005")

    label("loc_1FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2005")

    label("loc_2005")

    TalkEnd(0xFE)
    Return()

    # Function_46_1F19 end

    def Function_47_2009(): pass

    label("Function_47_2009")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_225E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2215")
    OP_A2(0x633)

    ChrTalk(
        0xF,
        (
            "#151FHeeey! Esteeeelle!\x02\x03",
            "You did it! The fiinaaal fiiiight!\x02\x03",
            "It's soooo exciiiiting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FDeep breaths, Dorothy. Come\x01",
            "on now, do it with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIf you don't relax and keep yourself\x01",
            "still and focused, you won't be able\x01",
            "to get any good shots...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#150FOh, don't you worry about THAT.\x02\x03",
            "I take my best pictures when\x01",
            "I'm all hyped up like this!\x02\x03",
            "They're more natural, you see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019FOh. I...guess they would be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FDorothy...I think you're some\x01",
            "kind of savant or something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225B")

    label("loc_2215")


    ChrTalk(
        0xF,
        (
            "#151FOoh, stop flattering me. Now\x01",
            "come on, show me whatcha' got!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_225B")

    Jump("loc_22EF")

    label("loc_225E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 4)), scpexpr(EXPR_END)), "loc_22EF")

    ChrTalk(
        0xF,
        (
            "#150FIt shouldn't be hard to get good\x01",
            "shots of you, what with these super-\x01",
            "awesome press seats!\x02\x03",
            "Better keep my camera at the ready!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22EF")

    TalkEnd(0xF)
    Return()

    # Function_47_2009 end

    def Function_48_22F3(): pass

    label("Function_48_22F3")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2641")
    OP_A2(0x632)

    ChrTalk(
        0xE,
        "#130FEstelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FProfessor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FYou came to watch us...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#130FBut of course! You've always\x01",
            "been such a big help to me.\x02\x03",
            "I owe you two at least THAT much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FThanks, Professor!\x02\x03",
            "#006FBut...how'd you scrape together\x01",
            "the mira for a ticket?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#130FWell, that was a bit of a lucky\x01",
            "break on my part, actually.\x02\x03",
            "The museum director had some\x01",
            "sudden business to attend to,\x01",
            "so he couldn't make it today.\x02\x03",
            "And I am here in his stead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FHa! Should have guessed you'd\x01",
            "never be able to get in here\x01",
            "out of your OWN pocket!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#130FHa! Not that I wouldn't try, of\x01",
            "course. I'm sure I could find a\x01",
            "way, if I put my mind to it...\x02\x03",
            "At any rate, I am here, and here\x01",
            "I am. And I'll be shouting your\x01",
            "names for sure.\x02\x03",
            "Knock 'em dead, you two!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FYou bet we will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FThank you, Professor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26B0")

    label("loc_2641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_26B0")

    ChrTalk(
        0xE,
        (
            "#130FI am here, and here I am. And\x01",
            "I'll be shouting your names for\x01",
            "sure.\x02\x03",
            "Knock 'em dead, you two!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B0")

    TalkEnd(0xE)
    Return()

    # Function_48_22F3 end

    def Function_49_26B4(): pass

    label("Function_49_26B4")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D38")
    OP_A2(0x634)
    OP_8C(0xB, 90, 0)

    ChrTalk(
        0xB,
        "#847F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FIs something wrong, Kurt?\x02",
    )

    CloseMessageWindow()
    OP_9E(0xB, 0xF, 0x0, 0x12C, 0xFA0)
    TurnDirection(0xB, 0x0, 400)

    ChrTalk(
        0xB,
        (
            "#840FHmm? Oh, it's you guys.\x02\x03",
            "Guess it's time for the final match.\x01",
            "Give it all you've got, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FYou bet!\x02\x03",
            "#505F...You don't look so good there,\x01",
            "Kurt. Are you okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FYou do seem pale.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#845FNah, just a little light-headed,\x01",
            "that's all.\x02\x03",
            "#844FThough it's kind of odd...I don't\x01",
            "feel sick, so why am I light-headed?\x02\x03",
            "I think I'm having...a flashback...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580FFlashback? From what, yesterday?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#841FNo, no no. From an accident I had\x01",
            "about three months ago.\x02\x03",
            "Seems I screwed up on a job and\x01",
            "messed myself up pretty bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FWhat do you mean, 'seems'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FYou don't mean...amnesia, do you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#845FI do. It's kind of embarrassing, and perhaps\x01",
            "even a bit cliched...but, I actually don't\x01",
            "remember a thing about it. Or didn't, anyway.\x02\x03",
            "I still can't even remember what\x01",
            "job I was doing that got me hurt\x01",
            "in the first place!\x02\x03",
            "The doctor said it wasn't shock or\x01",
            "anything, but offered no other explanations\x01",
            "as to what it could be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003FWow, what a story...\x02\x03",
            "#002FBut you were still okay to\x01",
            "participate in the match,\x01",
            "even in that condition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#841FI told you, physically there\x01",
            "isn't a thing wrong with me.\x02\x03",
            "In fact...I'm feeling a lot better\x01",
            "just talking it over with you.\x02\x03",
            "And in time, these flashbacks will start to\x01",
            "take shape, and I'll remember what happened.\x01",
            "So don't worry about me, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FUh, okay, I guess...if you say so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYou are starting to look a little\x01",
            "better than you did a minute ago.\x02\x03",
            "Just be careful, though, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#841FThanks.\x02\x03",
            "You guys too. Good luck out there.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 90, 400)
    Jump("loc_2D82")

    label("loc_2D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2D82")

    ChrTalk(
        0xFE,
        (
            "#841FYou've got to fight hard enough\x01",
            "for me, too, you got it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D82")

    TalkEnd(0xB)
    Return()

    # Function_49_26B4 end

    SaveToFile()

Try(main)
