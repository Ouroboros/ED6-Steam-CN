from ED6ScenarioHelper import *

def main():
    # 阳光铃铛酒廊

    CreateScenaFile(
        FileName            = 'T4100   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Olivier',                              # 9
        'Soldier',                              # 10
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Soldier',                              # 16
        'Soldier',                              # 17
        'Kurt',                                 # 18
        'Bill',                                 # 19
        'Ilene',                                # 20
        'Gaspard',                              # 21
        'Finel',                                # 22
        'Nonna',                                # 23
        'Armand',                               # 24
        'Ellie',                                # 25
        'Dick',                                 # 26
        'Raleigh',                              # 27
        'Troy',                                 # 28
        'Berden',                               # 29
        'Latanya',                              # 30
        'Tran',                                 # 31
        'Soldier',                              # 32
        'Soldier',                              # 33
        'Soldier',                              # 34
        'Soldier',                              # 35
        'Special Ops Soldier',                  # 36
        'Special Ops Soldier',                  # 37
        'Special Ops Soldier',                  # 38
        'Tourist',                              # 39
        'Tourist',                              # 40
        'Tourist',                              # 41
        'Tourist',                              # 42
        'Tourist',                              # 43
        'Tourist',                              # 44
        'Tourist',                              # 45
        'Tourist',                              # 46
        'Mirano',                               # 47
        'Simon',                                # 48
        'Tourist',                              # 49
        'Tourist',                              # 50
        'Tourist',                              # 51
        'Tourist',                              # 52
        'Mayor Maybelle',                       # 53
        'Lila',                                 # 54
        'Grancel - North Block',                # 55
        'Royal Avenue',                         # 56
        'Grancel - East Block',                 # 57
        'Grancel - West Block',                 # 58
    )

    DeclEntryPoint(
        Unknown_00              = 5200,
        Unknown_04              = 0,
        Unknown_08              = 1000,
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
        'ED6_DT07/CH00102 ._CH',             # 01
        'ED6_DT06/CH20038 ._CH',             # 02
        'ED6_DT07/CH00107 ._CH',             # 03
        'ED6_DT07/CH01640 ._CH',             # 04
        'ED6_DT07/CH01620 ._CH',             # 05
        'ED6_DT07/CH01490 ._CH',             # 06
        'ED6_DT07/CH01180 ._CH',             # 07
        'ED6_DT07/CH01270 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01050 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01150 ._CH',             # 0C
        'ED6_DT07/CH01160 ._CH',             # 0D
        'ED6_DT07/CH01470 ._CH',             # 0E
        'ED6_DT07/CH01060 ._CH',             # 0F
        'ED6_DT07/CH01200 ._CH',             # 10
        'ED6_DT07/CH01210 ._CH',             # 11
        'ED6_DT07/CH01100 ._CH',             # 12
        'ED6_DT07/CH01610 ._CH',             # 13
        'ED6_DT07/CH01020 ._CH',             # 14
        'ED6_DT07/CH01220 ._CH',             # 15
        'ED6_DT07/CH01460 ._CH',             # 16
        'ED6_DT07/CH01130 ._CH',             # 17
        'ED6_DT07/CH01680 ._CH',             # 18
        'ED6_DT07/CH01690 ._CH',             # 19
        'ED6_DT07/CH01120 ._CH',             # 1A
        'ED6_DT07/CH01110 ._CH',             # 1B
        'ED6_DT07/CH01230 ._CH',             # 1C
        'ED6_DT07/CH01480 ._CH',             # 1D
        'ED6_DT07/CH01150 ._CH',             # 1E
        'ED6_DT07/CH01170 ._CH',             # 1F
        'ED6_DT07/CH01000 ._CH',             # 20
        'ED6_DT07/CH01010 ._CH',             # 21
        'ED6_DT07/CH02360 ._CH',             # 22
        'ED6_DT07/CH02370 ._CH',             # 23
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT07/CH00102P._CP',             # 01
        'ED6_DT06/CH20038P._CP',             # 02
        'ED6_DT07/CH00107P._CP',             # 03
        'ED6_DT07/CH01640P._CP',             # 04
        'ED6_DT07/CH01620P._CP',             # 05
        'ED6_DT07/CH01490P._CP',             # 06
        'ED6_DT07/CH01180P._CP',             # 07
        'ED6_DT07/CH01270P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01050P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01150P._CP',             # 0C
        'ED6_DT07/CH01160P._CP',             # 0D
        'ED6_DT07/CH01470P._CP',             # 0E
        'ED6_DT07/CH01060P._CP',             # 0F
        'ED6_DT07/CH01200P._CP',             # 10
        'ED6_DT07/CH01210P._CP',             # 11
        'ED6_DT07/CH01100P._CP',             # 12
        'ED6_DT07/CH01610P._CP',             # 13
        'ED6_DT07/CH01020P._CP',             # 14
        'ED6_DT07/CH01220P._CP',             # 15
        'ED6_DT07/CH01460P._CP',             # 16
        'ED6_DT07/CH01130P._CP',             # 17
        'ED6_DT07/CH01680P._CP',             # 18
        'ED6_DT07/CH01690P._CP',             # 19
        'ED6_DT07/CH01120P._CP',             # 1A
        'ED6_DT07/CH01110P._CP',             # 1B
        'ED6_DT07/CH01230P._CP',             # 1C
        'ED6_DT07/CH01480P._CP',             # 1D
        'ED6_DT07/CH01150P._CP',             # 1E
        'ED6_DT07/CH01170P._CP',             # 1F
        'ED6_DT07/CH01000P._CP',             # 20
        'ED6_DT07/CH01010P._CP',             # 21
        'ED6_DT07/CH02360P._CP',             # 22
        'ED6_DT07/CH02370P._CP',             # 23
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
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 54,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 55,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 56,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 57,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 58,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 59,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 0,
        Y                   = -63100,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 7810,
        Z                   = 0,
        Y                   = -1510,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 7800,
        Z                   = 0,
        Y                   = -530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -5720,
        Z                   = 0,
        Y                   = -36280,
        Direction           = 281,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -5830,
        Z                   = 0,
        Y                   = -55640,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 5550,
        Z                   = 0,
        Y                   = -54380,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
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
        TalkScenaIndex      = 21,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 5760,
        Z                   = 0,
        Y                   = -46060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -2070,
        Z                   = 0,
        Y                   = -5120,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 3520,
        Z                   = 0,
        Y                   = 10640,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 6280,
        Z                   = 0,
        Y                   = 2180,
        Direction           = 215,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -6430,
        Z                   = 0,
        Y                   = -22020,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 4760,
        Z                   = 0,
        Y                   = -39600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = -29870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 6280,
        Z                   = 0,
        Y                   = 2180,
        Direction           = 215,
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
        X                   = 4760,
        Z                   = 0,
        Y                   = -39600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = -29870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -6250,
        Z                   = 0,
        Y                   = -870,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -6250,
        Z                   = 0,
        Y                   = -1920,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = -8540,
        Z                   = 250,
        Y                   = 6040,
        Direction           = 172,
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
        X                   = -8540,
        Z                   = 250,
        Y                   = 4630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -5690,
        Z                   = 0,
        Y                   = -7580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 13060,
        Z                   = 250,
        Y                   = 4130,
        Direction           = 51,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 7390,
        Z                   = 250,
        Y                   = -15350,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 7390,
        Z                   = 250,
        Y                   = -17380,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = -7510,
        Z                   = 250,
        Y                   = -16200,
        Direction           = 99,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = -8330,
        Z                   = 250,
        Y                   = -14940,
        Direction           = 138,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = 8300,
        Z                   = 250,
        Y                   = 3500,
        Direction           = 170,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 7330,
        Z                   = 250,
        Y                   = -27330,
        Direction           = 37,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = -7120,
        Z                   = 250,
        Y                   = -30460,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 7170,
        Z                   = 250,
        Y                   = -10430,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = -80,
        Z                   = 0,
        Y                   = -49760,
        Direction           = 160,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = -990,
        Z                   = 0,
        Y                   = -50700,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 10,
        Z                   = 250,
        Y                   = 36990,
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
        X                   = -50,
        Z                   = 0,
        Y                   = -90220,
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
        X                   = 54990,
        Z                   = 0,
        Y                   = -1130,
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
        X                   = -44420,
        Z                   = 0,
        Y                   = -19990,
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
        X                   = 5270,
        Y                   = -1000,
        Z                   = -67700,
        Range               = -6090,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF0182,
        Unknown_18          = 0x0,
        Unknown_1C          = 71,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -25000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 73,
    )

    DeclEvent(
        X                   = -10280,
        Y                   = 0,
        Z                   = -11040,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 74,
    )

    DeclEvent(
        X                   = -14940,
        Y                   = 0,
        Z                   = -15750,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 74,
    )

    DeclEvent(
        X                   = -10290,
        Y                   = 0,
        Z                   = -30020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 75,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -13010,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 76,
    )

    DeclEvent(
        X                   = 15900,
        Y                   = 0,
        Z                   = 6330,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 77,
    )


    ScpFunction(
        "Function_0_8EA",          # 00, 0
        "Function_1_E19",          # 01, 1
        "Function_2_10F5",         # 02, 2
        "Function_3_127D",         # 03, 3
        "Function_4_12A1",         # 04, 4
        "Function_5_12FE",         # 05, 5
        "Function_6_138B",         # 06, 6
        "Function_7_13AF",         # 07, 7
        "Function_8_141E",         # 08, 8
        "Function_9_148D",         # 09, 9
        "Function_10_14EC",        # 0A, 10
        "Function_11_1581",        # 0B, 11
        "Function_12_15CF",        # 0C, 12
        "Function_13_1842",        # 0D, 13
        "Function_14_1AA4",        # 0E, 14
        "Function_15_1C96",        # 0F, 15
        "Function_16_1E7D",        # 10, 16
        "Function_17_2711",        # 11, 17
        "Function_18_31C2",        # 12, 18
        "Function_19_3C11",        # 13, 19
        "Function_20_3E3B",        # 14, 20
        "Function_21_4254",        # 15, 21
        "Function_22_464A",        # 16, 22
        "Function_23_49CA",        # 17, 23
        "Function_24_4EF8",        # 18, 24
        "Function_25_546B",        # 19, 25
        "Function_26_5AA4",        # 1A, 26
        "Function_27_6300",        # 1B, 27
        "Function_28_635C",        # 1C, 28
        "Function_29_63B2",        # 1D, 29
        "Function_30_66A5",        # 1E, 30
        "Function_31_66EE",        # 1F, 31
        "Function_32_679B",        # 20, 32
        "Function_33_67FD",        # 21, 33
        "Function_34_68C8",        # 22, 34
        "Function_35_693C",        # 23, 35
        "Function_36_69EF",        # 24, 36
        "Function_37_6A35",        # 25, 37
        "Function_38_6A87",        # 26, 38
        "Function_39_6B0A",        # 27, 39
        "Function_40_6B53",        # 28, 40
        "Function_41_6B73",        # 29, 41
        "Function_42_6C2C",        # 2A, 42
        "Function_43_6CBB",        # 2B, 43
        "Function_44_6D0E",        # 2C, 44
        "Function_45_70D0",        # 2D, 45
        "Function_46_71B8",        # 2E, 46
        "Function_47_71CC",        # 2F, 47
        "Function_48_7CF3",        # 30, 48
        "Function_49_7E18",        # 31, 49
        "Function_50_85A9",        # 32, 50
        "Function_51_8718",        # 33, 51
        "Function_52_89C7",        # 34, 52
        "Function_53_8F96",        # 35, 53
        "Function_54_91FC",        # 36, 54
        "Function_55_926A",        # 37, 55
        "Function_56_92D8",        # 38, 56
        "Function_57_931E",        # 39, 57
        "Function_58_9364",        # 3A, 58
        "Function_59_93AA",        # 3B, 59
        "Function_60_9418",        # 3C, 60
        "Function_61_9821",        # 3D, 61
        "Function_62_9F36",        # 3E, 62
        "Function_63_A000",        # 3F, 63
        "Function_64_A155",        # 40, 64
        "Function_65_A276",        # 41, 65
        "Function_66_A3A7",        # 42, 66
        "Function_67_A556",        # 43, 67
        "Function_68_A679",        # 44, 68
        "Function_69_A7C4",        # 45, 69
        "Function_70_A8CD",        # 46, 70
        "Function_71_AAE2",        # 47, 71
        "Function_72_ABCD",        # 48, 72
        "Function_73_ABE9",        # 49, 73
        "Function_74_ABED",        # 4A, 74
        "Function_75_ABF1",        # 4B, 75
        "Function_76_ABF5",        # 4C, 76
        "Function_77_ABF9",        # 4D, 77
    )


    def Function_0_8EA(): pass

    label("Function_0_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_8FD")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 49)

    label("loc_8FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_90E")
    OP_A3(0x3FB)
    SoundLoad(125)
    Event(0, 51)

    label("loc_90E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_91C")
    OP_A3(0x3FC)
    Event(0, 60)

    label("loc_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_92F")
    SetMapFlags(0x10000000)
    OP_A3(0x3FD)
    Event(0, 61)

    label("loc_92F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_93F"),
        (103, "loc_955"),
        (SWITCH_DEFAULT, "loc_96B"),
    )


    label("loc_93F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_952")
    OP_A2(0x608)
    Event(0, 47)

    label("loc_952")

    Jump("loc_96B")

    label("loc_955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_968")
    OP_A2(0x629)
    Event(0, 52)

    label("loc_968")

    Jump("loc_96B")

    label("loc_96B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A25")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -4270, 0, -46090, 273)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -5960, 0, -47010, 44)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -5960, 0, -45200, 140)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
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
    Jump("loc_E18")

    label("loc_A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A80")
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    Jump("loc_E18")

    label("loc_A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_AE0")
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_E18")

    label("loc_AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B6C")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -3830, 0, -46790, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -3810, 0, -44860, 180)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_E18")

    label("loc_B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B8A")
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_E18")

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BFB")
    SetChrPos(0x14, -5720, 0, -37010, 257)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_E18")

    label("loc_BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C31")
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 270)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 90)
    Jump("loc_E18")

    label("loc_C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CA9")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 5340, 0, -37270, 84)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 5410, 0, -37950, 90)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)
    Jump("loc_E18")

    label("loc_CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_D2B")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 5340, 0, -37270, 84)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 5410, 0, -37950, 90)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 270)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 90)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -5300, 0, -38930, 315)
    SetChrFlags(0x1B, 0x10)
    Jump("loc_E18")

    label("loc_D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_DA3")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -3830, 0, -46790, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -3810, 0, -44860, 180)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)
    Jump("loc_E18")

    label("loc_DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_E18")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -3830, 0, -46790, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -3810, 0, -44860, 180)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1120, 0, -52220, 315)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1040, 0, -52280, 45)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 10, 0, -50410, 180)

    label("loc_E18")

    Return()

    # Function_0_8EA end

    def Function_1_E19(): pass

    label("Function_1_E19")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x3005B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3C")
    OP_1C(0x10, 0x0, 0x30)

    label("loc_E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E50")
    OP_1B(0x3, 0x0, 0x2E)
    Jump("loc_E73")

    label("loc_E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_E63")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E73")

    label("loc_E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_E73")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EA6")
    OP_B1("t4100_y")
    Jump("loc_EAF")

    label("loc_EA6")

    OP_B1("t4100_n")

    label("loc_EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBF")
    OP_1B(0x0, 0x0, 0x3F)
    Jump("loc_F5C")

    label("loc_EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED8")
    OP_1B(0x0, 0x0, 0x32)
    Jump("loc_F5C")

    label("loc_ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EEC")
    OP_1B(0x0, 0x0, 0x40)
    Jump("loc_F5C")

    label("loc_EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F00")
    OP_1B(0x0, 0x0, 0x41)
    Jump("loc_F5C")

    label("loc_F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F14")
    OP_1B(0x0, 0x0, 0x42)
    Jump("loc_F5C")

    label("loc_F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F28")
    OP_1B(0x0, 0x0, 0x43)
    Jump("loc_F5C")

    label("loc_F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3C")
    OP_1B(0x0, 0x0, 0x44)
    Jump("loc_F5C")

    label("loc_F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F50")
    OP_1B(0x0, 0x0, 0x45)
    Jump("loc_F5C")

    label("loc_F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_F5C")
    OP_1B(0x0, 0x0, 0x46)

    label("loc_F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F86")
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x2, 0x10)
    OP_72(0x4, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x10, 0x10)

    label("loc_F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FE4")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_43(0xB, 0x1, 0x0, 0x35)
    OP_43(0xC, 0x1, 0x0, 0x35)
    OP_43(0xD, 0x1, 0x0, 0x35)
    OP_43(0xE, 0x1, 0x0, 0x35)
    OP_43(0xF, 0x1, 0x0, 0x35)
    OP_43(0x10, 0x1, 0x0, 0x35)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_10D8")
    OP_72(0x19, 0x4)
    LoadEffect(0x0, "map\\\\mp016_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -70, 0, -46310, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -70, 250, -24300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -70, 0, -5700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -70, 0, 8590, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_10D8")

    SoundDistance(0x1CB, 0x32, 0x0, 0xFFFF4A70, 0x7D0, 0x3A98, 0x64, 0x0)
    Return()

    # Function_1_E19 end

    def Function_2_10F5(): pass

    label("Function_2_10F5")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1125")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_1267")

    label("loc_1125")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_1267")

    label("loc_113E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1157")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_1267")

    label("loc_1157")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1170")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_1267")

    label("loc_1170")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1189")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_1267")

    label("loc_1189")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A2")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_1267")

    label("loc_11A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BB")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_1267")

    label("loc_11BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D4")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_1267")

    label("loc_11D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11ED")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_1267")

    label("loc_11ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1206")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_1267")

    label("loc_1206")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_1267")

    label("loc_121F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1238")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_1267")

    label("loc_1238")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1251")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_1267")

    label("loc_1251")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1267")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_1267")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_127C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1267")

    label("loc_127C")

    Return()

    # Function_2_10F5 end

    def Function_3_127D(): pass

    label("Function_3_127D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12A0")
    OP_8D(0xFE, 3700, -42040, 10110, -50100, 2000)
    Jump("Function_3_127D")

    label("loc_12A0")

    Return()

    # Function_3_127D end

    def Function_4_12A1(): pass

    label("Function_4_12A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12FD")
    OP_8E(0xFE, 0xFFFFF7EA, 0x0, 0xFFFF6E24, 0x8FC, 0x0)
    OP_8E(0xFE, 0x9CE, 0x0, 0xFFFF6E24, 0x8FC, 0x0)
    OP_8E(0xFE, 0x9CE, 0x0, 0x2166, 0x8FC, 0x0)
    OP_8E(0xFE, 0xFFFFF7EA, 0x0, 0x2166, 0x8FC, 0x0)
    Jump("Function_4_12A1")

    label("loc_12FD")

    Return()

    # Function_4_12A1 end

    def Function_5_12FE(): pass

    label("Function_5_12FE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_138A")
    OP_8E(0xFE, 0xDC0, 0x0, 0xFFFF6532, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF29A, 0x0, 0xFFFF6532, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF29A, 0x0, 0x2990, 0x7D0, 0x0)
    OP_8E(0xFE, 0xDC0, 0x0, 0x2990, 0x7D0, 0x0)
    Jump("Function_5_12FE")

    label("loc_138A")

    Return()

    # Function_5_12FE end

    def Function_6_138B(): pass

    label("Function_6_138B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13AE")
    OP_8D(0xFE, 7470, -10200, 1790, -22030, 3000)
    Jump("Function_6_138B")

    label("loc_13AE")

    Return()

    # Function_6_138B end

    def Function_7_13AF(): pass

    label("Function_7_13AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_141D")
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFFFB5A, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_7_13AF")

    label("loc_141D")

    Return()

    # Function_7_13AF end

    def Function_8_141E(): pass

    label("Function_8_141E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_148C")
    OP_8E(0xFE, 0xFFFFEE44, 0x0, 0xFFFFAFC4, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFEEB2, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    Jump("Function_8_141E")

    label("loc_148C")

    Return()

    # Function_8_141E end

    def Function_9_148D(): pass

    label("Function_9_148D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Those damned Royal Guardsmen... \x01",
            "We'll teach 'em to defy Colonel\x01",
            "Richard's orders!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_148D end

    def Function_10_14EC(): pass

    label("Function_10_14EC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "What're you lookin' at? Oh,\x01",
            "you're bracers, are you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you don't want to get \x01",
            "hurt, you'll get back to\x01",
            "your guild and stay there.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_14EC end

    def Function_11_1581(): pass

    label("Function_11_1581")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "The castle is locked down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What the hell happened in there?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1581 end

    def Function_12_15CF(): pass

    label("Function_12_15CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_16A0")

    ChrTalk(
        0xFE,
        "So, you guys are bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, just leave the police\x01",
            "work to us and enjoy a nice\x01",
            "day of festivities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We couldn't do anything during\x01",
            "the coup, so we've gotta make\x01",
            "amends, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_16A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_16AA")
    Jump("loc_183E")

    label("loc_16AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_16F2")

    ChrTalk(
        0xFE,
        (
            "The airship platforms are\x01",
            "completely closed as of today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_16F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_176B")

    ChrTalk(
        0xFE,
        (
            "Guard duty after dark is\x01",
            "always nerve-wracking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you see anybody suspicious,\x01",
            "you come let me know!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_176B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1792")

    ChrTalk(
        0xFE,
        "Nothing to report here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_1792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_180F")

    ChrTalk(
        0xFE,
        (
            "We're really cracking down on\x01",
            "security from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't want to see anything\x01",
            "else happen, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_180F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1819")
    Jump("loc_183E")

    label("loc_1819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1823")
    Jump("loc_183E")

    label("loc_1823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_182D")
    Jump("loc_183E")

    label("loc_182D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1837")
    Jump("loc_183E")

    label("loc_1837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_183E")

    label("loc_183E")

    TalkEnd(0xFE)
    Return()

    # Function_12_15CF end

    def Function_13_1842(): pass

    label("Function_13_1842")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_18E3")

    ChrTalk(
        0xFE,
        (
            "We wanted to stay in the capital\x01",
            "and fight for Her Majesty the\x01",
            "Queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Getting tricked away by fake\x01",
            "orders is a real embarrassment\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_18E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_18ED")
    Jump("loc_1AA0")

    label("loc_18ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1960")

    ChrTalk(
        0xFE,
        (
            "What's going to happen with\x01",
            "the Birthday Celebration?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about Her\x01",
            "Majesty's illness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_1960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_19CD")

    ChrTalk(
        0xFE,
        (
            "I'm glad the Martial Arts\x01",
            "Competition is finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But we can't let our guards\x01",
            "down yet!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_19CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1A1A")

    ChrTalk(
        0xFE,
        (
            "I hope the Competition finishes\x01",
            "quietly and without incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_1A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1A71")

    ChrTalk(
        0xFE,
        (
            "Don't use the tournament as \x01",
            "an excuse to get too rowdy,\x01",
            "now, you hear?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1A7B")
    Jump("loc_1AA0")

    label("loc_1A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A85")
    Jump("loc_1AA0")

    label("loc_1A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1A8F")
    Jump("loc_1AA0")

    label("loc_1A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1A99")
    Jump("loc_1AA0")

    label("loc_1A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1AA0")

    label("loc_1AA0")

    TalkEnd(0xFE)
    Return()

    # Function_13_1842 end

    def Function_14_1AA4(): pass

    label("Function_14_1AA4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1B3F")

    ChrTalk(
        0xFE,
        (
            "I just can't believe Colonel\x01",
            "Richard staged a coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whether or not they knew about\x01",
            "it, the Royal Guardsmen really\x01",
            "messed up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C92")

    label("loc_1B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1B49")
    Jump("loc_1C92")

    label("loc_1B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1B88")

    ChrTalk(
        0xFE,
        (
            "The Bracer Guild would never\x01",
            "harbor terrorists.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C92")

    label("loc_1B88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1BD7")

    ChrTalk(
        0xFE,
        (
            "If you see any Royal Guardsmen,\x01",
            "please report them immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C92")

    label("loc_1BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1C11")

    ChrTalk(
        0xFE,
        (
            "What do you want? Move! You're\x01",
            "in the way!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C92")

    label("loc_1C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1C63")

    ChrTalk(
        0xFE,
        "Oh, you're bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, don't try to play hero\x01",
            "or anything!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C92")

    label("loc_1C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1C6D")
    Jump("loc_1C92")

    label("loc_1C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C77")
    Jump("loc_1C92")

    label("loc_1C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1C81")
    Jump("loc_1C92")

    label("loc_1C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1C8B")
    Jump("loc_1C92")

    label("loc_1C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1C92")

    label("loc_1C92")

    TalkEnd(0xFE)
    Return()

    # Function_14_1AA4 end

    def Function_15_1C96(): pass

    label("Function_15_1C96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1D09")

    ChrTalk(
        0xFE,
        (
            "There're still some guys from\x01",
            "the Special Ops out there\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We've got to stay alert!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1D13")
    Jump("loc_1E79")

    label("loc_1D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1D86")

    ChrTalk(
        0xFE,
        (
            "Those Special Ops sure have\x01",
            "some big egos on them for\x01",
            "being the new guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Pisses me right off!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1DB9")

    ChrTalk(
        0xFE,
        (
            "Where are those terrorists\x01",
            "hiding?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1DF6")

    ChrTalk(
        0xFE,
        (
            "Man, I want to go see the\x01",
            "championship match!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1E4A")

    ChrTalk(
        0xFE,
        (
            "If you see anyone suspicious,\x01",
            "you let me know right away,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1E54")
    Jump("loc_1E79")

    label("loc_1E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E5E")
    Jump("loc_1E79")

    label("loc_1E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1E68")
    Jump("loc_1E79")

    label("loc_1E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1E72")
    Jump("loc_1E79")

    label("loc_1E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1E79")

    label("loc_1E79")

    TalkEnd(0xFE)
    Return()

    # Function_15_1C96 end

    def Function_16_1E7D(): pass

    label("Function_16_1E7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_200D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1F2B")

    ChrTalk(
        0xFE,
        (
            "Colonel Richard, staging a\x01",
            "coup d'etat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He looked so worried about the kingdom\x01",
            "when I saw him before, outside the castle.\x01",
            "Was it all an act?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_200A")

    label("loc_1F2B")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "Colonel Richard, staging a\x01",
            "coup d'etat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He looked so worried about the kingdom\x01",
            "when I saw him before, outside the castle.\x01",
            "Was it all an act?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't believe we got the wool\x01",
            "pulled over our eyes so badly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_200A")

    Jump("loc_270D")

    label("loc_200D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_20C2")

    ChrTalk(
        0xFE,
        (
            "I hope the Royal Guardsmen\x01",
            "rethink their actions and go\x01",
            "back to the castle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure Queen Alicia won't\x01",
            "hold it against them. They\x01",
            "were just following orders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_20C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_214F")

    ChrTalk(
        0xFE,
        "I wonder how the queen's doing...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without any news, I've been\x01",
            "so worried about her I can\x01",
            "barely sleep at night anymore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_214F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_21B9")

    ChrTalk(
        0xFE,
        "Well, another tournament done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How's the Birthday Celebration\x01",
            "going to go, though...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_21B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_222F")

    ChrTalk(
        0xFE,
        (
            "Every day I take a long walk\x01",
            "for my health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel good today. Must be\x01",
            "on account of the weather.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_222F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_22A0")

    ChrTalk(
        0xFE,
        (
            "Colonel Richard is a highly\x01",
            "respected officer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's a true patriot of the\x01",
            "Kingdom of Liberl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_22A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2329")

    ChrTalk(
        0xFE,
        "I like the tournament and all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I'm not really in the mood\x01",
            "to watch it after hearing that\x01",
            "the queen's fallen ill.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_2329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_23BD")

    ChrTalk(
        0xFE,
        (
            "This is the first time the\x01",
            "Royal Guardsman have been\x01",
            "ousted by the regular army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't imagine the circumstances\x01",
            "behind it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_23BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2583")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_246B")

    ChrTalk(
        0xFE,
        (
            "When it's not in use by officials,\x01",
            "the Erbe Royal Villa is fully opened\x01",
            "to tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But right now, the army's using it\x01",
            "as their anti-terror base.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2580")

    label("loc_246B")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "When it's not in use by officials,\x01",
            "the Erbe Royal Villa is fully opened\x01",
            "to tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These last few years, the villa's\x01",
            "only really been used in any official\x01",
            "capacity when foreign dignitaries come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But right now, the army's using it\x01",
            "as their anti-terror base.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2580")

    Jump("loc_270D")

    label("loc_2583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_26C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_260E")

    ChrTalk(
        0xFE,
        (
            "I'd love to take a walk to the\x01",
            "villa, but we're not allowed to\x01",
            "get close to it at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a real pain!\x02",
    )

    CloseMessageWindow()
    Jump("loc_26BE")

    label("loc_260E")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "The weather's so nice, I feel\x01",
            "like going on a good, long\x01",
            "walk..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I can't go to the villa\x01",
            "on account of it being locked\x01",
            "down by soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a real pain!\x02",
    )

    CloseMessageWindow()

    label("loc_26BE")

    Jump("loc_270D")

    label("loc_26C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_270D")

    ChrTalk(
        0xFE,
        "This is Grancel's main avenue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I walk this road every day.\x02",
    )

    CloseMessageWindow()

    label("loc_270D")

    TalkEnd(0xFE)
    Return()

    # Function_16_1E7D end

    def Function_17_2711(): pass

    label("Function_17_2711")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_28DF")
    Jc((scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_END)), "loc_27DF")

    ChrTalk(
        0xFE,
        (
            "I just can't believe that \x01",
            "Colonel Richard staged that\x01",
            "coup. It's inconceivable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, I know EXACTLY what that \x01",
            "word means! He's just a victim\x01",
            "of circumstance, that's all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DC")

    label("loc_27DF")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "I just can't believe that \x01",
            "Colonel Richard staged that\x01",
            "coup. It's inconceivable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, I know EXACTLY what that \x01",
            "word means! He's just a victim\x01",
            "of circumstance, that's all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I firmly believe that, and no\x01",
            "one can convince me otherwise!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DC")

    Jump("loc_31BE")

    label("loc_28DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_299D")

    ChrTalk(
        0xFE,
        (
            "This sudden increase in soldiers\x01",
            "without any kind of explanation is,\x01",
            "understandably, a bit worrisome!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was going to paint the town today,\x01",
            "but maybe I'll just go home...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_299D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2A75")

    ChrTalk(
        0xFE,
        (
            "The Martial Arts Competition is\x01",
            "always the prelude to the queen's\x01",
            "Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But with the queen having fallen ill\x01",
            "this year, what's going to happen?\x01",
            "Will the celebration still be held?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_2A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2AF8")

    ChrTalk(
        0xFE,
        (
            "The entire city is abuzz with\x01",
            "news of the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No one could have guessed the\x01",
            "outcome this year. No one!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_2AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2B8B")

    ChrTalk(
        0xFE,
        (
            "It all ends today. I wonder\x01",
            "what the final bout's going\x01",
            "to be like...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll go to the arena\x01",
            "later and watch it in person!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_2B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2C7E")

    ChrTalk(
        0xFE,
        (
            "Colonel Richard has that captain.\x01",
            "You know... The one with those\x01",
            "squinty-looking eyes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's got this condescending\x01",
            "air about her that just doesn't\x01",
            "sit right with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why does the colonel keep her\x01",
            "around all the time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_2C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2E2C")
    Jc((scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_END)), "loc_2D27")

    ChrTalk(
        0xFE,
        (
            "Colonel Richard's participated\x01",
            "in the tournament before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He knows this swordfighting\x01",
            "style called...uh...something!\x01",
            "It's pretty incredible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E29")

    label("loc_2D27")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "Colonel Richard's participated\x01",
            "in the tournament before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He knows this swordfighting\x01",
            "style called...uh...something!\x01",
            "It's pretty incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He learned it from some mysterious\x01",
            "ancient master. Yeah, I know I'm\x01",
            "lacking in some details here...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E29")

    Jump("loc_31BE")

    label("loc_2E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2F8F")
    Jc((scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_END)), "loc_2EB9")

    ChrTalk(
        0xFE,
        (
            "Colonel Richard really is\x01",
            "something, isn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been a fan of his ever\x01",
            "since he arrested those Sky\x01",
            "Bandits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F8C")

    label("loc_2EB9")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "Colonel Richard really is\x01",
            "something, isn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Isn't he just about perfect,\x01",
            "though? Smart, commanding\x01",
            "and good-looking to boot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been a fan of his ever\x01",
            "since he arrested those Sky\x01",
            "Bandits.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8C")

    Jump("loc_31BE")

    label("loc_2F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_30BC")
    Jc((scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_END)), "loc_3001")

    ChrTalk(
        0xFE,
        (
            "I don't like the idea of the\x01",
            "duke replacing the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She's got to get better soon!\x02",
    )

    CloseMessageWindow()
    Jump("loc_30B9")

    label("loc_3001")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "I don't like the idea of the\x01",
            "duke replacing the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What he's saying does make \x01",
            "sense, but would you look\x01",
            "at that ridiculous outfit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She's got to get better soon!\x02",
    )

    CloseMessageWindow()

    label("loc_30B9")

    Jump("loc_31BE")

    label("loc_30BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3120")

    ChrTalk(
        0xFE,
        (
            "I just saw this MOUNTAIN of a\x01",
            "man walking by. I wonder if \x01",
            "he's in the tournament...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_3120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_31BE")

    ChrTalk(
        0xFE,
        (
            "With the tournament in full\x01",
            "swing like this, the East\x01",
            "Block's streets are packed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's got to be about time for \x01",
            "the preliminaries to start.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31BE")

    TalkEnd(0xFE)
    Return()

    # Function_17_2711 end

    def Function_18_31C2(): pass

    label("Function_18_31C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3234")

    ChrTalk(
        0xFE,
        (
            "I heard Colonel Richard was\x01",
            "put under arrest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He never struck me as that\x01",
            "kind of person...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_3234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3298")

    ChrTalk(
        0xFE,
        (
            "I've got a bad feeling about\x01",
            "those soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "A foul premonition, if you will...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_3298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3321")

    ChrTalk(
        0xFE,
        (
            "The trees lining these streets\x01",
            "were planted to commemorate\x01",
            "Princess Klaudia's birth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Time sure does fly, doesn't it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_3321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_33CA")

    ChrTalk(
        0xFE,
        (
            "The winners of the tournament\x01",
            "get a banquet at the castle...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't like Duke Dunan very\x01",
            "much, but that's still a really\x01",
            "nice gesture on his part.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_33CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3425")

    ChrTalk(
        0xFE,
        (
            "A lot of people are out early\x01",
            "today to get good seats for\x01",
            "the championship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_3425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_35B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_34D3")

    ChrTalk(
        0xFE,
        (
            "I've seen a lot of those \x01",
            "soldiers in black creeping\x01",
            "around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are they part of that...Royal \x01",
            "Anti-Terror Squad, or whatever\x01",
            "the heck it's called?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B3")

    label("loc_34D3")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "I've seen a lot of those \x01",
            "soldiers in black creeping\x01",
            "around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ever since the queen got sick,\x01",
            "they've been out in droves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are they part of that...Royal \x01",
            "Anti-Terror Squad, or whatever\x01",
            "the heck it's called?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B3")

    Jump("loc_3C0D")

    label("loc_35B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3658")

    ChrTalk(
        0xFE,
        (
            "Tournament spectators are all\x01",
            "up early today, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There were probably plenty of\x01",
            "people who camped out last\x01",
            "night to get the best seats.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_3658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3702")

    ChrTalk(
        0xFE,
        (
            "Colonel Richard has a lot of\x01",
            "popular support amongst the\x01",
            "citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doesn't surprise me. He's\x01",
            "highly decorated, and a pretty\x01",
            "good person on top of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_3702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3802")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3764")

    ChrTalk(
        0xFE,
        (
            "This city has a full underground\x01",
            "sewer system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's pretty convenient.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37FF")

    label("loc_3764")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "This city has a full underground\x01",
            "sewer system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Accessible from all over. See those\x01",
            "grates all along the streets?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's pretty convenient.\x02",
    )

    CloseMessageWindow()

    label("loc_37FF")

    Jump("loc_3C0D")

    label("loc_3802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_38A8")

    ChrTalk(
        0xFE,
        (
            "That's a statue of a white\x01",
            "falcon up on the fountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's our national symbol-- the\x01",
            "crest of the Liberl Royal Family.\x01",
            "Even shows up on our flag.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_38A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3C0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_39FF")

    ChrTalk(
        0xFE,
        (
            "The city is split into four\x01",
            "districts, or blocks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll find the shops and the Bracer Guild here\x01",
            "in the South Block, while the castle and the\x01",
            "royal hotel can be found in the North.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The West Block's got the the cathedral and the\x01",
            "Liberl News HQ, and the East Block has the\x01",
            "embassies, arenas and general markets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0D")

    label("loc_39FF")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "Hi! Is this your first time in\x01",
            "Grancel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The city is split into four\x01",
            "districts, or blocks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here in the South Block you'll\x01",
            "find the Bracer Guild, as well\x01",
            "as a variety of shops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The North Block has the royal hotel, the\x01",
            "biggest in the country. Just beyond it,\x01",
            "farther north, is the castle itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The West Block has the Grand \x01",
            "Cathedral, as well as the main\x01",
            "offices of the Liberl News. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And over in the East Block are all \x01",
            "the embassies, the arenas and all the \x01",
            "general goods stores for the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0D")

    TalkEnd(0xFE)
    Return()

    # Function_18_31C2 end

    def Function_19_3C11(): pass

    label("Function_19_3C11")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3C3E")

    ChrTalk(
        0xFE,
        "Festivals are so much fun!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3C70")

    ChrTalk(
        0xFE,
        "Did bad guys show up or something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3C93")

    ChrTalk(
        0xFE,
        "I'm soooo huuungry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3CDA")

    ChrTalk(
        0xFE,
        (
            "You know, I didn't see that\x01",
            "red guy even break a sweat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3CE4")
    Jump("loc_3E37")

    label("loc_3CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3D3D")

    ChrTalk(
        0xFE,
        (
            "I think the bracers are\x01",
            "gonna win tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just have a feeling...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3D47")
    Jump("loc_3E37")

    label("loc_3D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3DCB")

    ChrTalk(
        0xFE,
        (
            "Each one is pretty tough alone, so if you put\x01",
            "all four of 'em together, they're like, more\x01",
            "tough. Like, SUPER tough!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3DEC")

    ChrTalk(
        0xFE,
        "That looks GREAT!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3E13")

    ChrTalk(
        0xFE,
        "Whoa, that was awesome!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E37")

    label("loc_3E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3E37")

    ChrTalk(
        0xFE,
        "Hey, where's my ticket?\x02",
    )

    CloseMessageWindow()

    label("loc_3E37")

    TalkEnd(0xFE)
    Return()

    # Function_19_3C11 end

    def Function_20_3E3B(): pass

    label("Function_20_3E3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3EEC")

    ChrTalk(
        0xFE,
        (
            "You'd better watch out. My friend\x01",
            "here is crazy about girls!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If he sees a beautiful girl, he's got\x01",
            "a 95 percent chance of falling in love\x01",
            "at first sight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_3EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3F43")

    ChrTalk(
        0xFE,
        "It's so creepy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those soldiers in black seem\x01",
            "like real bad news!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_3F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3F92")

    ChrTalk(
        0xFE,
        (
            "I wonder if the Birthday Celebration\x01",
            "will proceed as planned...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_3F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3FDE")

    ChrTalk(
        0xFE,
        "What a fight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That was almost literally a\x01",
            "show-stopper!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_3FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3FE8")
    Jump("loc_4250")

    label("loc_3FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4086")

    ChrTalk(
        0xFE,
        (
            "Personally, I was all about the\x01",
            "bracer-on-bracer action today.\x01",
            "That was a hell of a match!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You usually don't get to see\x01",
            "fights like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_4086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_40C0")

    ChrTalk(
        0xFE,
        (
            "Troy has absolutely no sense\x01",
            "of direction!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_40C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_415D")

    ChrTalk(
        0xFE,
        (
            "Troy's usually just spouting stuff\x01",
            "without thinking, but sometimes he's\x01",
            "right on the money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if this'll be one of\x01",
            "those times...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_415D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_41C4")

    ChrTalk(
        0xFE,
        (
            "If I let Troy get out of my\x01",
            "sight for even a second, he's\x01",
            "going to go get himself lost.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_41C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_420D")

    ChrTalk(
        0xFE,
        (
            "The real question is, how far\x01",
            "can a man fight on his own?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4250")

    label("loc_420D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4250")

    ChrTalk(
        0xFE,
        (
            "If we don't hurry, we won't be\x01",
            "able to get good seats!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4250")

    TalkEnd(0xFE)
    Return()

    # Function_20_3E3B end

    def Function_21_4254(): pass

    label("Function_21_4254")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_42BE")

    ChrTalk(
        0xFE,
        (
            "Princess Klaudia is so kind,\x01",
            "and so pretty, too... *sigh*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She makes my heart race.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_42BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4307")

    ChrTalk(
        0xFE,
        (
            "All these soldiers around is\x01",
            "seriously cramping my style.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_4307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4347")

    ChrTalk(
        0xFE,
        (
            "Now what? The tournament's\x01",
            "done, so what's next?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_4347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_439B")

    ChrTalk(
        0xFE,
        (
            "I really thought that guy in\x01",
            "the red helmet was going to\x01",
            "win it all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_439B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_43A5")
    Jump("loc_4646")

    label("loc_43A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4423")

    ChrTalk(
        0xFE,
        (
            "That match between him and\x01",
            "the Sky Bandits? Holy CRAP!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet the Royal Army's got\x01",
            "the championship again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_4423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_444A")

    ChrTalk(
        0xFE,
        "Man, is Troy ever late!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_444A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_456E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_44D2")

    ChrTalk(
        0xFE,
        "All the teams look good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Zane's team, though... It all\x01",
            "depends on those three 'auxiliary'\x01",
            "members he dug up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_456B")

    label("loc_44D2")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "That red guy looks tough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "All the teams look good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Zane's team, though... It all\x01",
            "depends on those three 'auxiliary'\x01",
            "members he dug up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_456B")

    Jump("loc_4646")

    label("loc_456E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_45D4")

    ChrTalk(
        0xFE,
        "Why is he always like that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just want to get to the \x01",
            "arena and find good seats.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_45D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4628")

    ChrTalk(
        0xFE,
        "That Republic guy ain't half bad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He can win it all by himself!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4646")

    label("loc_4628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4646")

    ChrTalk(
        0xFE,
        "Darn that Troy...\x02",
    )

    CloseMessageWindow()

    label("loc_4646")

    TalkEnd(0xFE)
    Return()

    # Function_21_4254 end

    def Function_22_464A(): pass

    label("Function_22_464A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4657")
    Jump("loc_49C6")

    label("loc_4657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4661")
    Jump("loc_49C6")

    label("loc_4661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_47D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4707")

    ChrTalk(
        0xFE,
        (
            "Armand's been thinking about\x01",
            "something all day, but he\x01",
            "won't tell me what it is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He can be such a meanie! Time to\x01",
            "bust out the pouty face!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D0")

    label("loc_4707")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "Armand's been talking to himself\x01",
            "all day today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know he's got something on\x01",
            "his mind, but he just won't tell\x01",
            "me what it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He can be such a meanie! Time to\x01",
            "bust out the pouty face!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47D0")

    Jump("loc_49C6")

    label("loc_47D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_47FD")

    ChrTalk(
        0xFE,
        "My sweetie is so romantic!\x02",
    )

    CloseMessageWindow()
    Jump("loc_49C6")

    label("loc_47FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4832")

    ChrTalk(
        0xFE,
        "Oh, wow!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This tastes INCREDIBLE!\x02",
    )

    CloseMessageWindow()
    Jump("loc_49C6")

    label("loc_4832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_483C")
    Jump("loc_49C6")

    label("loc_483C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4846")
    Jump("loc_49C6")

    label("loc_4846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_48A2")

    ChrTalk(
        0xFE,
        (
            "He can't take his eyes off\x01",
            "of me...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "*blush*\x02",
    )

    CloseMessageWindow()
    Jump("loc_49C6")

    label("loc_48A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_492A")

    ChrTalk(
        0xFE,
        (
            "I get to spend another whole\x01",
            "day with my man!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "I'm so glad we took this trip\x01",
            "to Grancel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C6")

    label("loc_492A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_498A")

    ChrTalk(
        0xFE,
        (
            "Even when he's watching the\x01",
            "tournament matches, my darling\x01",
            "always holds my hand!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C6")

    label("loc_498A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_49C6")

    ChrTalk(
        0xFE,
        (
            "Aww, I wanted to see the \x01",
            "inside of the castle!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49C6")

    TalkEnd(0xFE)
    Return()

    # Function_22_464A end

    def Function_23_49CA(): pass

    label("Function_23_49CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_49D7")
    Jump("loc_4EF4")

    label("loc_49D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_49E1")
    Jump("loc_4EF4")

    label("loc_49E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4A64")

    ChrTalk(
        0xFE,
        "I looked all over town...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...and the best place to pop the\x01",
            "question is right in front of the\x01",
            "gates, I think...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF4")

    label("loc_4A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4BC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4AB3")

    ChrTalk(
        0xFE,
        (
            "Ahhh, is there anything more\x01",
            "beautiful in all the world?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BC3")

    label("loc_4AB3")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "Grancel City and its castle,\x01",
            "standing in the deepening red\x01",
            "of the fading twilight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All reflected within the liquid\x01",
            "depths of your gorgeous eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahhh, is there anything more\x01",
            "beautiful in all the world?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No! There is not!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "A thousand times, no!\x02",
    )

    CloseMessageWindow()

    label("loc_4BC3")

    Jump("loc_4EF4")

    label("loc_4BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4BF4")

    ChrTalk(
        0xFE,
        "Luxury, thy name is royalty...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EF4")

    label("loc_4BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4BFE")
    Jump("loc_4EF4")

    label("loc_4BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4C08")
    Jump("loc_4EF4")

    label("loc_4C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4CA9")

    ChrTalk(
        0xFE,
        (
            "During the match I had the\x01",
            "chance to examine my darling's\x01",
            "face in perfect silhouette.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How can she be so perfect?\x01",
            "It must be against the law!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF4")

    label("loc_4CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4CF4")

    ChrTalk(
        0xFE,
        (
            "Another day with my beloved,\x01",
            "sweeter than spun sugar candy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF4")

    label("loc_4CF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4E84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4D93")

    ChrTalk(
        0xFE,
        (
            "The arena felt like it was \x01",
            "wrapped in a whirlwind of\x01",
            "heat and energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But that heat was nothing compared\x01",
            "to the power of our love!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E81")

    label("loc_4D93")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "Since we couldn't go into the \x01",
            "castle, we went to the arena\x01",
            "and watched the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The arena felt like it was \x01",
            "wrapped in a whirlwind of\x01",
            "heat and energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But that heat was nothing compared\x01",
            "to the power of our love!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E81")

    Jump("loc_4EF4")

    label("loc_4E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4EF4")

    ChrTalk(
        0xFE,
        "What is this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I come all this way with my\x01",
            "little honeypot, and we can't\x01",
            "even enter the castle!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF4")

    TalkEnd(0xFE)
    Return()

    # Function_23_49CA end

    def Function_24_4EF8(): pass

    label("Function_24_4EF8")

    TalkBegin(0x16)
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

    MenuEnd(0x4)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F58")
    OP_0D()
    OP_A9(0x72)
    OP_56(0x0)
    TalkEnd(0x16)
    Return()

    label("loc_4F58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F69")
    TalkEnd(0x16)
    Return()

    label("loc_4F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4FA7")

    ChrTalk(
        0x16,
        "Step right on up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Go ahead, don't be shy!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_4FA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5030")

    ChrTalk(
        0x16,
        (
            "Recently, the regular soldiers\x01",
            "have all been replaced by...other\x01",
            "ones, armored entirely in black.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Why would that be?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_5030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5111")

    ChrTalk(
        0x16,
        (
            "With the tournament over, the\x01",
            "streets feel a bit freer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "But with the Queen's Birthday\x01",
            "Celebration coming, that's not\x01",
            "going to last very long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Though this year? I'm not really\x01",
            "sure WHAT to expect...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_5111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5188")

    ChrTalk(
        0x16,
        (
            "I wish I could've seen the\x01",
            "tournament finals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "But I've got to work if I'm\x01",
            "going to support myself!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_5188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_51C8")

    ChrTalk(
        0x16,
        (
            "Personally, I'd recommend this\x01",
            "strawberry crepe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_51C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5263")

    ChrTalk(
        0x16,
        (
            "These seasonal part-time\x01",
            "positions pay pretty well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Of course, the tradeoff is that\x01",
            "I don't get to watch the Martial\x01",
            "Arts Competition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_5263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_52A2")

    ChrTalk(
        0x16,
        (
            "Hello! Would you like to try\x01",
            "one of our crepes?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_52A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_52E6")

    ChrTalk(
        0x16,
        (
            "It'd be nice if my hourly wage\x01",
            "were a little higher.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_52E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_534C")

    ChrTalk(
        0x16,
        "You two, over there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "You look like you could use a\x01",
            "couple warm, delicious crepes!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_534C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_53EA")

    ChrTalk(
        0x16,
        (
            "I want to live on my own, so I\x01",
            "got me this part-time job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "There's an empty place in the\x01",
            "West Block I'm hoping to move\x01",
            "into at some point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_53EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5467")

    ChrTalk(
        0x16,
        "Step right up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "We've got crepes of all kinds!\x01",
            "Don't be crepe'd out by them--\x01",
            "they won't bite, but you will!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5467")

    TalkEnd(0x16)
    Return()

    # Function_24_4EF8 end

    def Function_25_546B(): pass

    label("Function_25_546B")

    TalkBegin(0x15)
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

    MenuEnd(0x4)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54CB")
    OP_0D()
    OP_A9(0x71)
    OP_56(0x0)
    TalkEnd(0x15)
    Return()

    label("loc_54CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54DC")
    TalkEnd(0x15)
    Return()

    label("loc_54DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_55C0")

    ChrTalk(
        0x15,
        (
            "There's an ice cream shop in\x01",
            "the East Block that's doing\x01",
            "great business, I hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I went there to check them out,\x01",
            "but the lines were so long that\x01",
            "I just gave up and went home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "They can't beat us, though!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_55C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_562B")

    ChrTalk(
        0x15,
        (
            "Are all these black-clad soldiers\x01",
            "part of the Royal Army?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "They're really intimidating!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_562B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_56D1")

    ChrTalk(
        0x15,
        (
            "I plan to run this booth up through\x01",
            "the Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "But unless the queen gets better,\x01",
            "they're just going to up and cancel\x01",
            "on us, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_56D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5736")

    ChrTalk(
        0x15,
        "Looks like another fine day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I wonder if the weather's\x01",
            "this good in Bose, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_5736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5802")

    ChrTalk(
        0x15,
        (
            "These soldiers started showing\x01",
            "up everywhere last evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I'm not even doing anything and they make\x01",
            "me feel guilty! It's like we're under martial\x01",
            "law...or at least it FEELS that way!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_5802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5857")

    ChrTalk(
        0x15,
        "Hello, step right up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "What kind of ice cream do you\x01",
            "fancy today?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_5857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_590D")

    ChrTalk(
        0x15,
        (
            "The competition's been hopping ever since\x01",
            "opening day this year. The turnout's got\x01",
            "to have broken some records, even!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Hell, I can even hear the crowds\x01",
            "from here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_590D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5962")

    ChrTalk(
        0x15,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "How about something sweet to\x01",
            "recharge after that match?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_5962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_59BE")

    ChrTalk(
        0x15,
        (
            "Bose is a pretty\x01",
            "big city as well, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "...this is the Royal Capital.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_59BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5A5E")

    ChrTalk(
        0x15,
        (
            "Normally I run a booth in Bose, but\x01",
            "this year I decided to come out to\x01",
            "the capital for some big money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Let's see how well my sales'll do...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AA0")

    label("loc_5A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5AA0")

    ChrTalk(
        0x15,
        "Hello, step right up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "What flavor can I get you?\x02",
    )

    CloseMessageWindow()

    label("loc_5AA0")

    TalkEnd(0x15)
    Return()

    # Function_25_546B end

    def Function_26_5AA4(): pass

    label("Function_26_5AA4")

    TalkBegin(0x14)
    OP_A3(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5AB4")
    Jump("loc_5B24")

    label("loc_5AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5AC1")
    OP_A2(0xE)
    Jump("loc_5B24")

    label("loc_5AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5ACB")
    Jump("loc_5B24")

    label("loc_5ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5AD8")
    OP_A2(0xE)
    Jump("loc_5B24")

    label("loc_5AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5AE5")
    OP_A2(0xE)
    Jump("loc_5B24")

    label("loc_5AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5AEF")
    Jump("loc_5B24")

    label("loc_5AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5AF9")
    Jump("loc_5B24")

    label("loc_5AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5B06")
    OP_A2(0xE)
    Jump("loc_5B24")

    label("loc_5B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5B13")
    OP_A2(0xE)
    Jump("loc_5B24")

    label("loc_5B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5B1D")
    Jump("loc_5B24")

    label("loc_5B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5B24")

    label("loc_5B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_5B99")
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

    MenuEnd(0x4)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B88")
    OP_0D()
    OP_A9(0x73)
    OP_56(0x0)
    TalkEnd(0x14)
    Return()

    label("loc_5B88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B99")
    TalkEnd(0x14)
    Return()

    label("loc_5B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5D1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5C52")

    ChrTalk(
        0x14,
        (
            "Ever since the airships got grounded,\x01",
            "my merchandise shipments have been\x01",
            "getting more and more backed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I hate that I have no control\x01",
            "over this whatsoever!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D1B")

    label("loc_5C52")

    OP_A2(0x2)

    ChrTalk(
        0x14,
        (
            "My deliveries aren't getting out\x01",
            "because the airships were all grounded,\x01",
            "and everything's backed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "But I did everything I could!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I hate that I have no control\x01",
            "over this whatsoever!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D1B")

    Jump("loc_62FC")

    label("loc_5D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5D68")

    ChrTalk(
        0x14,
        "Sure are tons of soldiers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Ugh. What's broken now?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_5D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5D96")

    ChrTalk(
        0x14,
        "Tire's blown, it looks like...\x02",
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_5D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5ED7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5E4F")

    ChrTalk(
        0x14,
        (
            "I swear, these days it feels\x01",
            "anticlimactic when there's no\x01",
            "trouble to overcome!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Seems like trouble's an old\x01",
            "friend of mine, always greeting\x01",
            "me at the door...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ED4")

    label("loc_5E4F")

    OP_A2(0x2)

    ChrTalk(
        0x14,
        "No problems today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Makes me nervous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Seems like trouble's an old\x01",
            "friend of mine, always greeting\x01",
            "me at the door...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ED4")

    Jump("loc_62FC")

    label("loc_5ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5F1F")

    ChrTalk(
        0x14,
        (
            "I expect trouble, but I sure\x01",
            "hope there isn't any today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_5F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_60C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5FB9")

    ChrTalk(
        0x14,
        (
            "I'd try selling something, but\x01",
            "it'd have to be displayed on the\x01",
            "GROUND at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Seems my life revolves around\x01",
            "trouble...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60C3")

    label("loc_5FB9")

    OP_A2(0x2)

    ChrTalk(
        0x14,
        (
            "My whole shop is falling apart,\x01",
            "and no one's been available to\x01",
            "fix it due to the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I'd try selling something, but\x01",
            "it'd have to be displayed on the\x01",
            "GROUND at this point.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "Seems my life revolves around\x01",
            "trouble...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60C3")

    Jump("loc_62FC")

    label("loc_60C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6154")

    ChrTalk(
        0x14,
        (
            "This case's latch is broken.\x01",
            "It won't open properly.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "Seems my life revolves around\x01",
            "trouble...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_6154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_61EB")

    ChrTalk(
        0x14,
        (
            "Most of the big crowds show\x01",
            "up just before or just after\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Once that starts, my work goes\x01",
            "really slow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_61EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6228")

    ChrTalk(
        0x14,
        (
            "I'm glad I finished my cash\x01",
            "register repairs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_6228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_62A5")

    ChrTalk(
        0x14,
        "Busiest time of the year, you know?\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "Seems my life revolves around\x01",
            "trouble...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FC")

    label("loc_62A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_62FC")

    ChrTalk(
        0x14,
        "Hmmm... This looks bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The register's completely and\x01",
            "totally busted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62FC")

    TalkEnd(0x14)
    Return()

    # Function_26_5AA4 end

    def Function_27_6300(): pass

    label("Function_27_6300")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Wonderful! Frabjous!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huzzah for Her Majesty! Callooh,\x01",
            "callay, I say I say!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_6300 end

    def Function_28_635C(): pass

    label("Function_28_635C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Seeing Princess Klaudia again\x01",
            "makes me feel secure about\x01",
            "Liberl's future.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_635C end

    def Function_29_63B2(): pass

    label("Function_29_63B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_63BF")
    Jump("loc_66A1")

    label("loc_63BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_63C9")
    Jump("loc_66A1")

    label("loc_63C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_63D3")
    Jump("loc_66A1")

    label("loc_63D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_63DD")
    Jump("loc_66A1")

    label("loc_63DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_63E7")
    Jump("loc_66A1")

    label("loc_63E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_63F1")
    Jump("loc_66A1")

    label("loc_63F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_63FB")
    Jump("loc_66A1")

    label("loc_63FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6405")
    Jump("loc_66A1")

    label("loc_6405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6690")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_64A7")

    ChrTalk(
        0xFE,
        (
            "#840FEven with the Martial Arts\x01",
            "Competition, we bracers still\x01",
            "have a job to do!\x02\x03",
            "Now's the time to get all the\x01",
            "quick and simple stuff done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_668D")

    label("loc_64A7")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "#840FWell... Look who it is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FHi, Kurt!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FFancy meeting you in a place\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#840FJust gathering the bounties\x01",
            "on some monsters out here.\x02\x03",
            "Even with the Martial Arts\x01",
            "Competition, we bracers still\x01",
            "have a job to do!\x02\x03",
            "Now's the time to get all the\x01",
            "quick and simple stuff done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FWell, it's good to see you're\x01",
            "working hard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#841FMore like warming up.\x02\x03",
            "I wouldn't say no to a sparring\x01",
            "partner or two, though!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe'll keep that in mind!\x02",
    )

    CloseMessageWindow()

    label("loc_668D")

    Jump("loc_66A1")

    label("loc_6690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_669A")
    Jump("loc_66A1")

    label("loc_669A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_66A1")

    label("loc_66A1")

    TalkEnd(0xFE)
    Return()

    # Function_29_63B2 end

    def Function_30_66A5(): pass

    label("Function_30_66A5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "We came to the capital for the\x01",
            "Queen's Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_66A5 end

    def Function_31_66EE(): pass

    label("Function_31_66EE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "But where should we go next?\x01",
            "There's just so much to see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The cathedral might be nice, but\x01",
            "what I REALLY want to see are the\x01",
            "ruins of the Ahnenburg Wall...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_66EE end

    def Function_32_679B(): pass

    label("Function_32_679B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I didn't expect the city to\x01",
            "be this big when I invited my\x01",
            "mom to come see it with me.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_679B end

    def Function_33_67FD(): pass

    label("Function_33_67FD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm exhausted from all the\x01",
            "tourism!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do you know someplace I can \x01",
            "sit and rest for a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That store looks expensive...\x01",
            "Like I'd be spending a fortune\x01",
            "just walking through the door!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_67FD end

    def Function_34_68C8(): pass

    label("Function_34_68C8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I was so surprised to hear\x01",
            "about the coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looking at the city, I'd've\x01",
            "never imagined it...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_68C8 end

    def Function_35_693C(): pass

    label("Function_35_693C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I'm so hungry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We came all this way, so why\x01",
            "not eat out somewhere nice?\x01",
            "Perhaps...a place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They all look so mouthwatering,\x01",
            "though. I can't decide!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_693C end

    def Function_36_69EF(): pass

    label("Function_36_69EF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It's busy here, but no busier\x01",
            "than the East Block, I bet.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_69EF end

    def Function_37_6A35(): pass

    label("Function_37_6A35")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I got lost. I'm going to ask\x01",
            "for directions over at the\x01",
            "Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_6A35 end

    def Function_38_6A87(): pass

    label("Function_38_6A87")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Yeah, only an event as big as\x01",
            "the Birthday Celebration could \x01",
            "bring in crowds like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Time to make some sales!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_6A87 end

    def Function_39_6B0A(): pass

    label("Function_39_6B0A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Where's that ice cream shop I've\x01",
            "been hearing so much about?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_6B0A end

    def Function_40_6B53(): pass

    label("Function_40_6B53")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "What store is this?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_6B53 end

    def Function_41_6B73(): pass

    label("Function_41_6B73")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "After all that trouble, it's \x01",
            "good to have some peace and\x01",
            "quiet for a change!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm expecting the queen to keep\x01",
            "on as she was. This sort of thing\x01",
            "shouldn't get her down!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_6B73 end

    def Function_42_6C2C(): pass

    label("Function_42_6C2C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I was glad to finally see the\x01",
            "queen's face again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who in their right mind would\x01",
            "want to overthrow a ruler like\x01",
            "Queen Alicia?!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_6C2C end

    def Function_43_6CBB(): pass

    label("Function_43_6CBB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It took so much time getting\x01",
            "here with all of the airships\x01",
            "grounded...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_6CBB end

    def Function_44_6D0E(): pass

    label("Function_44_6D0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 0)), scpexpr(EXPR_END)), "loc_6D7D")

    ChrTalk(
        0xFE,
        (
            "#611FOh, my, that Bracer symbol\x01",
            "certainly looks good on you\x01",
            "two!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008FThank you, ma'am.\x02",
    )

    CloseMessageWindow()
    Jump("loc_70CC")

    label("loc_6D7D")

    OP_A2(0x6E8)

    ChrTalk(
        0xFE,
        (
            "#617FI was planning on going home\x01",
            "early, but...I guess that didn't\x01",
            "happen!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FWell, you've had a lot to discuss,\x01",
            "I'm sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#610FIndeed. Headmaster Collins has\x01",
            "actually suggested we start a \x01",
            "committee for royal ascendency.\x02\x03",
            "#612FThere was a lot of mess with\x01",
            "that coup, and the damage to\x01",
            "our public image is quite big.\x02\x03",
            "We're going to have to start\x01",
            "working more in concert with\x01",
            "the other countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FIt sounds to me like you're\x01",
            "in for some busy times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#610FAll the more reason to kick\x01",
            "back and relax tonight, no?\x02\x03",
            "I believe a walk to the \x01",
            "cathedral for some prayer\x01",
            "is in order...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FActually, come to think of it, the\x01",
            "first time I met you was on a day\x01",
            "when you were skipping church...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#617FAll the more reason to go now!\x02\x03",
            "Though I'm sure Aidios can forgive\x01",
            "me for a little infraction like\x01",
            "that...right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70CC")

    TalkEnd(0xFE)
    Return()

    # Function_44_6D0E end

    def Function_45_70D0(): pass

    label("Function_45_70D0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#620FWith conferences day in and day out,\x01",
            "I imagine Her Highness must be a very\x01",
            "busy woman.\x02\x03",
            "If Her Highness really wants to relax, she\x01",
            "needs to get as far away as she can. I hear\x01",
            "Bose is quite nice this time of year...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_70D0 end

    def Function_46_71B8(): pass

    label("Function_46_71B8")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x3, 0x0, 0xFFFF)
    Return()

    # Function_46_71B8 end

    def Function_47_71CC(): pass

    label("Function_47_71CC")

    EventBegin(0x0)
    SetChrPos(0x1C, 5760, 0, -46060, 270)
    OP_43(0x1C, 0x0, 0x0, 0x2)
    OP_6D(600, 250, 1950, 0)
    OP_67(0, 17690, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(571, 0)
    SetChrPos(0x101, -100, 0, -56250, 0)
    SetChrPos(0x102, -1060, 0, -58160, 0)
    SetChrPos(0x10E, 890, 0, -58220, 0)

    def lambda_725C():
        OP_6D(-270, 1500, -57160, 11000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_725C)
    Sleep(2000)

    def lambda_7279():
        OP_6B(3000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7279)

    def lambda_7289():
        OP_67(0, 4000, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7289)

    def lambda_72A1():
        OP_6C(8000, 11000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_72A1)

    def lambda_72B1():
        OP_6E(273, 9000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_72B1)
    Sleep(11000)

    ChrTalk(
        0x101,
        (
            "#001F#5PWow...\x01",
            "This city's freakin' HUGE.\x02\x03",
            "Dad used to take me here a long\x01",
            "time ago, but was it really this\x01",
            "big then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWell, it is the biggest city\x01",
            "in the kingdom.\x02\x03",
            "Grancel Castle's just past the\x01",
            "main road. That's where the\x01",
            "queen lives.\x02\x03",
            "There's also the Grancel Cathedral, the\x01",
            "Grand Arena, and all the embassies\x01",
            "for the surrounding nations.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#501F#5PHuh... You don't say.\x02\x03",
            "You sure know a lot\x01",
            "about this city.\x02\x03",
            "You must have been here\x01",
            "before, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015FYes...\x01",
            "When I was little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130FMy... No matter how many times\x01",
            "I see it, this city still amazes\x01",
            "me with its beauty.\x02\x03",
            "Purely in terms of scale, I believe the\x01",
            "Imperial and Republican capitals are larger...\x02\x03",
            "...but neither feels as elegant\x01",
            "and refined as Grancel does.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_75C1():
        TurnDirection(0xFE, 0x10E, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75C1)
    TurnDirection(0x101, 0x10E, 400)

    ChrTalk(
        0x101,
        (
            "#506F#5PHa ha, I'm glad to hear it. It's nice to hear\x01",
            "a foreigner complimenting your home country.\x02\x03",
            "#501FWhich reminds me... What do you\x01",
            "plan to do now, Professor?\x02\x03",
            "Are you going to be okay with\x01",
            "staying in a hotel?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x101, 400)

    ChrTalk(
        0x10E,
        (
            "#130FHa ha. I have something\x01",
            "else in mind.\x02\x03",
            "I intend to go bug the folks\x01",
            "at the History Museum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#5POh, cool.\x01",
            "Grancel has one of those?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThey find ancient artifacts and\x01",
            "put them on display there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130FYes, and I'll be staying there\x01",
            "as a guest associate member.\x02\x03",
            "You two should stop by to visit,\x01",
            "if you get the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#5PEhhh... Museums are awfully\x01",
            "formal for my tastes...\x02\x03",
            "#509FIf we do come by, are you going\x01",
            "to give us a bunch of lessons?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#132FHeh heh heh... If that is your \x01",
            "wish, then I shall certainly do\x01",
            "my best.\x02\x03",
            "#130FJust kidding...though I do\x01",
            "think that checking out all\x01",
            "the exhibits would be fun.\x02\x03",
            "Now, if you'll excuse me...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7961():

        label("loc_7961")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_7961")

    QueueWorkItem2(0x101, 1, lambda_7961)

    def lambda_7972():

        label("loc_7972")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_7972")

    QueueWorkItem2(0x102, 1, lambda_7972)
    OP_8C(0x10E, 45, 400)
    OP_8E(0x10E, 0xFDB, 0x0, 0xFFFF29DC, 0xFA0, 0x0)

    def lambda_799E():
        OP_8E(0xFE, 0x1356, 0x0, 0xFFFF76E4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_799E)

    def lambda_79B9():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_79B9)

    def lambda_79C9():
        OP_6D(-780, 0, -56940, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_79C9)

    def lambda_79E1():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_79E1)

    def lambda_79F9():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_79F9)

    def lambda_7A09():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x10E, 3, lambda_7A09)
    Sleep(3000)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#506F#6P*sigh*... Well, he's just as\x01",
            "happy-go-lucky as ever...\x02\x03",
            "#006FWhat's this 'guest associate' thing,\x01",
            "though...? Is he a famous scholar\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FYes, most likely.\x02\x03",
            "#010FNow...we should probably stop in\x01",
            "at the local guild branch before\x01",
            "we do anything else.\x02\x03",
            "Not only do we need to change our branch\x01",
            "affiliation, but we can discuss there how to\x01",
            "approach delivering the professor's message.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        (
            "#505F#4PHmm...\x01",
            "Yeah, you're right.\x02\x03",
            "Thinking about it, how are we even going to get\x01",
            "an audience with Her Majesty, anyway?\x02\x03",
            "#007FAnd there's no way that'll be as\x01",
            "simple as just walking up to the\x01",
            "castle and saying, 'Hi.'\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x54, 0x3, 0x2)
    OP_28(0x54, 0x3, 0x4)
    OP_28(0x45, 0x4, 0x2)
    OP_28(0x45, 0x4, 0x4)
    OP_28(0x45, 0x1, 0x1)
    OP_28(0x45, 0x1, 0x2)
    OP_28(0x45, 0x1, 0x4)
    OP_28(0x45, 0x1, 0x8)
    OP_28(0x45, 0x1, 0x10)
    OP_28(0x45, 0x1, 0x20)
    OP_28(0x45, 0x1, 0x40)
    RemoveParty(0xD, 0xFF)
    EventEnd(0x0)
    OP_43(0x1C, 0x0, 0x0, 0x3)
    Return()

    # Function_47_71CC end

    def Function_48_7CF3(): pass

    label("Function_48_7CF3")

    EventBegin(0x0)
    OP_20(0x5DC)
    OP_8C(0x0, 0, 0)
    TurnDirection(0x1, 0x0, 0)
    OP_6D(16030, 500, 7220, 1000)
    OP_21()
    OP_1D(0x48)
    OP_1F(0x4B, 0xC8)
    Sleep(2000)

    ChrTalk(
        0x101,
        (
            "#004FOh...\x02\x03",
            "Is that a piano...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FYes. Not just a record, either.\x01",
            "It sounds like someone's playing\x01",
            "inside.\x02\x03",
            "I feel like I've heard that\x01",
            "melody somewhere before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509FI've got a bad feeling about this...\x02",
    )

    CloseMessageWindow()
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_48_7CF3 end

    def Function_49_7E18(): pass

    label("Function_49_7E18")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(16020, 250, 7280, 0)
    OP_6C(315000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x102, 15830, 740, 8470, 0)
    SetChrPos(0x101, 15830, 740, 8470, 0)
    SetChrPos(0x8, 15830, 740, 8470, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x10, 0x10)
    OP_70(0x10, 0x3C)
    OP_73(0x10)
    OP_6F(0x10, 60)

    def lambda_7E9C():
        OP_8E(0xFE, 0x3B7E, 0xFA, 0xF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E9C)
    Sleep(400)

    def lambda_7EBC():
        OP_8E(0xFE, 0x4060, 0xFA, 0xE6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7EBC)
    Sleep(500)

    def lambda_7EDC():
        OP_8E(0xFE, 0x3E9E, 0xFA, 0x14FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7EDC)
    OP_6D(16100, 250, 4400, 2000)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x8, 400)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#509FHow is it 'a matter of course'\x01",
            "for you to come with us?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#035FHa ha ha...\x01",
            "Please, don't be cruel.\x02\x03",
            "Beyond my uses as a traveling\x01",
            "companion, I also wish to\x01",
            "assist in the manhunt.\x02\x03",
            "#030FUnless, of course...you two\x01",
            "want to be alone?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580FWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#031FOh, my...\x01",
            "Such an unsophisticated child.\x02\x03",
            "But when you blossom to your full\x01",
            "potential, you shall be a woman\x01",
            "to be reckoned with.\x02\x03",
            "#037F...Ha ha. And quite a desirable\x01",
            "one, I'd wager.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#503F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F???\x02\x03",
            "What are you trying to say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#031FHa ha ha, well...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)
    SetChrChipByIndex(0x101, 1)

    ChrTalk(
        0x101,
        "#08A#005F#3SHi-YAH!\x05\x02",
    )

    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)

    def lambda_81B6():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81B6)
    OP_22(0x1F4, 0x0, 0x64)
    OP_99(0x101, 0x0, 0x7, 0x9C4)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    OP_22(0x7D, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 2)

    ChrTalk(
        0x8,
        "#038FAaaaiiiieeeee...!\x05\x02",
    )


    def lambda_8226():
        OP_8F(0xFE, 0x3DD6, 0x2E4, 0x2116, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8226)
    OP_99(0x101, 0x7, 0xC, 0x9C4)
    Sleep(300)
    OP_22(0x97, 0x0, 0x64)
    Sleep(700)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)

    NpcTalk(
        0x8,
        "Man's Voice",
        "Yow! What the--?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Woman's Voice",
        "Sir! Speak to me!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Old Man's Voice",
        (
            "No good...\x01",
            "He's not waking up.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018FEstelle...\x02\x03",
            "You know, no matter how angry someone\x01",
            "makes you, you're not allowed to brain\x01",
            "them. Especially not in public...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_44(0x101, 0xFF)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x8, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#509F...It was all flash, no impact.\x02\x03",
            "I didn't do any real damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ha ha ha... It seems...that Estelle\x01",
            "is a very shy individual.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#019FWell, he doesn't SEEM to be hurt...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8504")

    ChrTalk(
        0x101,
        (
            "#582FOkay, let's get back to searching.\x02\x03",
            "We don't have time to mess around.\x01",
            "Let's just go to the embassy, okay?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8578")

    label("loc_8504")


    ChrTalk(
        0x101,
        (
            "#582FOkay, let's get back to searching.\x02\x03",
            "We don't have time to mess around.\x01",
            "Let's go to the Erbe Scenic Route.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8578")


    ChrTalk(
        0x102,
        "#017F(Okay, so why's she mad at ME...? )\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_49_7E18 end

    def Function_50_85A9(): pass

    label("Function_50_85A9")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8620")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FWe still don't know where Zane is.\x02\x03",
            "I think we should go over to\x01",
            "the Calvardian embassy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8713")

    label("loc_8620")

    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000FOh, right...\x02\x03",
            "Didn't he say he'd probably\x01",
            "be out drinking?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FYes, I believe that's what\x01",
            "Elnan said.\x02\x03",
            "Just to make sure, let's check the\x01",
            "bar on the main street before we\x01",
            "head out to the Erbe Scenic Route.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8713")

    Call(0, 72)
    Return()

    # Function_50_85A9 end

    def Function_51_8718(): pass

    label("Function_51_8718")

    EventBegin(0x0)
    OP_6D(16020, 250, 7280, 0)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, 15830, 740, 8470, 0)
    SetChrPos(0x102, 15830, 740, 8470, 0)
    OP_0D()
    OP_70(0x10, 0x3C)
    OP_73(0x10)

    def lambda_8761():
        OP_8E(0xFE, 0x3B7E, 0xFA, 0xF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8761)
    Sleep(400)

    def lambda_8781():
        OP_8E(0xFE, 0x4060, 0xFA, 0xE6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8781)
    OP_6D(16100, 250, 4400, 2000)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x102, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#000FUuugh...\x01",
            "I think I'm gonna burst.\x02\x03",
            "I can't believe those guys are\x01",
            "actually drinking after a meal\x01",
            "like that.\x02\x03",
            "They must fill up from the legs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWell, Zane's got the constitution\x01",
            "for it, and Olivier's just kind\x01",
            "of a glutton.\x02\x03",
            "As long as it doesn't interfere with\x01",
            "Zane's performance in the tournament\x01",
            "tomorrow, I think it'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FYeah... I guess worrying about\x01",
            "it won't do any good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYou want to go to the hotel\x01",
            "on the North Block?\x02\x03",
            "Our room should be ready\x01",
            "by now...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_51_8718 end

    def Function_52_89C7(): pass

    label("Function_52_89C7")

    EventBegin(0x0)
    SetChrPos(0x101, 8940, 250, -12710, 270)
    SetChrPos(0x102, 8980, 250, -13870, 270)
    SetChrPos(0x9, 1930, 0, -4430, 0)
    SetChrPos(0xA, 1040, 0, -5320, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_6D(9320, 440, -13270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    ChrTalk(
        0x101,
        "#000FWow, it's late...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe should probably get back\x01",
            "to the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hey! You two!\x02",
    )

    CloseMessageWindow()

    def lambda_8ABD():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8ABD)

    def lambda_8ACB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8ACB)

    def lambda_8AD9():
        OP_8E(0xFE, 0x1B76, 0xFA, 0xFFFFD724, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8AD9)
    Sleep(300)

    def lambda_8AF9():
        OP_8E(0xFE, 0x1720, 0x0, 0xFFFFD314, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8AF9)
    OP_6D(7460, 250, -12150, 3000)

    ChrTalk(
        0x101,
        (
            "#000FHm? Oh...\x01",
            "What's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "We're on patrol.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nighttime patrols have been\x01",
            "increased as part of the\x01",
            "counter-terrorism measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So it's best to avoid going out\x01",
            "after 9 o'clock, if at all possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "You two should go on home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FDon't you think that's a little\x01",
            "obnoxious? What if you NEED to\x01",
            "go out after 9 o'clock?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's the higher-ups who make\x01",
            "the decisions, miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sorry to cause any trouble, but\x01",
            "everyone has to abide by the rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, where is it that\x01",
            "you two live?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe're staying at the hotel on\x01",
            "the North Block.\x02\x03",
            "We'll be there for the duration\x01",
            "of the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hold on a second... I could\x01",
            "swear I've seen you two\x01",
            "somewhere before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "These kids are in the tournament!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "You know, now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FOh! Were you guys in\x01",
            "the audience?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ha ha... Well, we were on\x01",
            "security detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "That match today was pretty incredible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Tomorrow's the championship, no?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We'll escort you to the hotel, so\x01",
            "you can rest up for your big fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FVery well. We accept.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_52_89C7 end

    def Function_53_8F96(): pass

    label("Function_53_8F96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91FB")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FC9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_8FC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FEF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_8FEF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9015")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_9015")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_903C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_903C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9062")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_9062")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9088")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_9088")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90AD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_90AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90D2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E6")

    label("loc_90D2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_90E6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91F8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    OP_69(0xFE, 0x3E8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91E9")

    ChrTalk(
        0xFE,
        "What do you think you're doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F(Ah, crap...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F(Caught already...)\x02",
    )

    CloseMessageWindow()

    label("loc_91E9")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_91F8")

    Jump("Function_53_8F96")

    label("loc_91FB")

    Return()

    # Function_53_8F96 end

    def Function_54_91FC(): pass

    label("Function_54_91FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9269")
    SetChrPos(0xFE, -29750, 250, -16079, 270)
    OP_8E(0xFE, 0xFFFFE0B6, 0xFA, 0xFFFFC131, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE0B6, 0xFA, 0x2EEA, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE0B6, 0xFA, 0xFFFFC131, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF8BCA, 0xFA, 0xFFFFC131, 0xBB8, 0x0)
    Jump("Function_54_91FC")

    label("loc_9269")

    Return()

    # Function_54_91FC end

    def Function_55_926A(): pass

    label("Function_55_926A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92D7")
    SetChrPos(0xFE, -29910, 250, -23870, 270)
    OP_8E(0xFE, 0xFFFFDF08, 0xFA, 0xFFFFA2C2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDE2C, 0xFA, 0xFFFF7D88, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDF08, 0xFA, 0xFFFFA2C2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF8B2A, 0xFA, 0xFFFFA2C2, 0xBB8, 0x0)
    Jump("Function_55_926A")

    label("loc_92D7")

    Return()

    # Function_55_926A end

    def Function_56_92D8(): pass

    label("Function_56_92D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_931D")
    SetChrPos(0xFE, -6720, 0, -19860, 270)
    OP_8E(0xFE, 0xFFFF8620, 0x0, 0xFFFFB26C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE5C0, 0x0, 0xFFFFB26C, 0xBB8, 0x0)
    Jump("Function_56_92D8")

    label("loc_931D")

    Return()

    # Function_56_92D8 end

    def Function_57_931E(): pass

    label("Function_57_931E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9363")
    SetChrPos(0xFE, 3810, 0, 10100, 180)
    OP_8E(0xFE, 0xEE2, 0x0, 0xFFFF7518, 0xBB8, 0x0)
    OP_8E(0xFE, 0xEE2, 0x0, 0x2774, 0xBB8, 0x0)
    Jump("Function_57_931E")

    label("loc_9363")

    Return()

    # Function_57_931E end

    def Function_58_9364(): pass

    label("Function_58_9364")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93A9")
    SetChrPos(0xFE, -3690, 0, -34890, 180)
    OP_8E(0xFE, 0xFFFFF196, 0x0, 0x25DA, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF196, 0x0, 0xFFFF77B6, 0xBB8, 0x0)
    Jump("Function_58_9364")

    label("loc_93A9")

    Return()

    # Function_58_9364 end

    def Function_59_93AA(): pass

    label("Function_59_93AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9417")
    SetChrPos(0xFE, -1740, 0, -6830, 180)
    OP_8E(0xFE, 0xFFFFF934, 0x0, 0xFFFFAF1A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7F8, 0x0, 0xFFFFAE66, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7F8, 0x0, 0xFFFFE4B2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF934, 0x0, 0xFFFFE552, 0xBB8, 0x0)
    Jump("Function_59_93AA")

    label("loc_9417")

    Return()

    # Function_59_93AA end

    def Function_60_9418(): pass

    label("Function_60_9418")

    EventBegin(0x0)
    RemoveParty(0x0, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x3, 0xFF)
    AddParty(0x7, 0xFF)
    SetChrPos(0x1C, -4970, 0, -57100, 270)
    OP_4A(0x1C, 255)
    OP_6D(-220, 250, -32150, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(21000, 0)
    OP_6E(262, 0)
    SetChrPos(0x104, -870, 0, -62440, 0)
    SetChrPos(0x102, -80, 0, -61370, 0)
    SetChrPos(0x108, 630, 0, -62400, 0)
    FadeToBright(2000, 0)
    OP_6D(170, 0, -59880, 7000)
    Fade(1000)
    OP_6D(-80, 0, -62140, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#012FIt looks like the regular\x01",
            "soldiers have been replaced\x01",
            "with Special Ops guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072FThe enemy's probably gotten quite\x01",
            "desperate since we liberated the\x01",
            "villa...\x02\x03",
            "Security seems a lot tighter than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#6PPerhaps I can help loosen them up\x01",
            "with the dulcet tones of my lute...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_963A():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_963A)
    TurnDirection(0x102, 0x104, 400)

    ChrTalk(
        0x102,
        (
            "#017FYou do anything conspicuous and\x01",
            "that guy will be on you faster than\x01",
            "you can say, 'off key.'\x02\x03",
            "#010F'Mueller,' wasn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x104, 0x102, 400)

    ChrTalk(
        0x104,
        (
            "#036F#6PY-Yes, it was...\x02\x03",
            "Ah... You two should definitely...MUST, rather,\x01",
            "NOT go near the Erebonian embassy. It could be\x01",
            "quite dangerous. Yes! Quite perilous, indeed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FHa ha... Well, neither of us has\x01",
            "time to just drop by there.\x02\x03",
            "Once preparations are complete,\x01",
            "we have to get inside the sewers.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0x1C, 255)
    Return()

    # Function_60_9418 end

    def Function_61_9821(): pass

    label("Function_61_9821")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x11, 29)
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x11, -4100, 0, -48960, 0)
    SetChrPos(0x13, -4010, 0, -39700, 0)
    SetChrPos(0x14, -2770, 0, -39710, 0)
    SetChrPos(0x15, -4520, 0, -30260, 0)
    SetChrPos(0x16, -18010, 250, -16550, 0)
    SetChrPos(0x17, -1760, 0, -25440, 0)
    SetChrPos(0x18, -4560, 0, -18230, 0)
    SetChrPos(0x1C, -8670, 250, -15130, 0)
    SetChrPos(0x1D, -7730, 250, -16070, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x1E, -4930, 0, -48010, 0)
    SetChrPos(0x26, 8840, 250, -36590, 0)
    SetChrPos(0x27, 7970, 250, -30700, 0)
    SetChrPos(0x28, 8039, 250, -34920, 0)
    SetChrPos(0x29, 5020, 0, -32530, 0)
    SetChrPos(0x2C, 17670, 0, 1260, 270)
    SetChrPos(0x2D, 17680, 0, -70, 270)
    SetChrPos(0x2E, 1540, 0, -21430, 0)
    SetChrPos(0x2A, 2700, 0, -20310, 0)
    SetChrPos(0x2B, 1640, 0, -19200, 0)
    SetChrPos(0x12, 8390, 0, -38030, 0)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-1140, 0, -63570, 0)
    OP_67(0, 7480, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(0, 0)
    OP_6E(580, 0)

    def lambda_9BEF():
        OP_6D(50, 0, 5920, 14000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9BEF)

    def lambda_9C07():
        OP_6C(320000, 16000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9C07)

    def lambda_9C17():
        OP_67(0, 14750, -10000, 16000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_9C17)

    def lambda_9C2F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_9C2F)
    Sleep(20)

    def lambda_9C4F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_9C4F)
    Sleep(20)

    def lambda_9C6F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_9C6F)
    Sleep(20)

    def lambda_9C8F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_9C8F)
    Sleep(20)

    def lambda_9CAF():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x8FC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_9CAF)
    Sleep(20)
    Sleep(20)

    def lambda_9CD4():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_9CD4)
    Sleep(20)

    def lambda_9CF4():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0xB54, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_9CF4)
    Sleep(20)

    def lambda_9D14():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_9D14)
    Sleep(20)

    def lambda_9D34():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_9D34)

    def lambda_9D4F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_9D4F)
    Sleep(20)

    def lambda_9D6F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_9D6F)
    Sleep(20)

    def lambda_9D8F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_9D8F)
    Sleep(20)

    def lambda_9DAF():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 0, lambda_9DAF)
    Sleep(20)

    def lambda_9DCF():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_9DCF)
    Sleep(20)

    def lambda_9DEF():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_9DEF)
    Sleep(20)

    def lambda_9E0F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_9E0F)
    Sleep(20)

    def lambda_9E2F():
        OP_90(0xFE, 0x0, 0x0, 0xC350, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_9E2F)
    Sleep(1000)

    def lambda_9E4F():
        OP_8E(0xFE, 0xFFFFE296, 0xFA, 0xFFFFC05E, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_9E4F)
    Sleep(1700)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x1B, 4090, 0, -66400, 0)
    SetChrPos(0x19, 4090, 0, -68100, 0)
    SetChrPos(0x1A, 4090, 0, -69800, 0)
    OP_43(0x1B, 0x0, 0x0, 0x3E)
    Sleep(100)
    OP_43(0x19, 0x0, 0x0, 0x3E)
    Sleep(100)
    OP_43(0x1A, 0x0, 0x0, 0x3E)
    Sleep(20)

    def lambda_9EE4():
        OP_8E(0xFE, 0x1702, 0x0, 0x604, 0x546, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_9EE4)

    def lambda_9EFF():
        OP_8E(0xFE, 0x155E, 0x0, 0x19A, 0x53C, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_9EFF)
    Sleep(7000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_61_9821 end

    def Function_62_9F36(): pass

    label("Function_62_9F36")

    OP_8E(0xFE, 0x1324, 0x0, 0xFFFF5B64, 0x2710, 0x0)
    OP_8E(0xFE, 0x8DE, 0x0, 0xFFFFA45C, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_97(0xFE, 0x0, 0xFFFFA45C, 0xFFFEA070, 0x24B8, 0x1)
    OP_97(0xFE, 0x0, 0xFFFFB910, 0x15F90, 0x24B8, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFF66E, 0x0, 0xFFFFE070, 0x2710, 0x0)
    OP_8E(0xFE, 0x30C, 0x0, 0xFFFFED68, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x2)

    def lambda_9FC5():
        OP_99(0xFE, 0x0, 0x7, 0x708)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9FC5)
    OP_96(0xFE, 0xFF0, 0x0, 0xFFFFF29A, 0x9C4, 0x7D0)
    ClearChrFlags(0xFE, 0x2)
    OP_8E(0xFE, 0x1630, 0x0, 0x82E6, 0x2710, 0x0)
    Return()

    # Function_62_9F36 end

    def Function_63_A000(): pass

    label("Function_63_A000")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0BF")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010FFirst, we should stop in at\x01",
            "the local guild branch.\x02\x03",
            "We can start the registration\x01",
            "process and also see about\x01",
            "the professor's request.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FOkay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A150")

    label("loc_A0BF")


    ChrTalk(
        0x102,
        (
            "#010FFirst, we should stop in at\x01",
            "the local guild branch.\x02\x03",
            "We can start the registration\x01",
            "process and also see about\x01",
            "the professor's request.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A150")

    Call(0, 72)
    Return()

    # Function_63_A000 end

    def Function_64_A155(): pass

    label("Function_64_A155")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A201")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010FCome on, let's go to\x01",
            "the guild branch.\x02\x03",
            "If we waste too much time, it'll\x01",
            "be night before you know it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006FYeah, you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A271")

    label("loc_A201")


    ChrTalk(
        0x102,
        (
            "#010FCome on, let's go to\x01",
            "the guild branch.\x02\x03",
            "If we waste too much time, it'll\x01",
            "be night before you know it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A271")

    Call(0, 72)
    Return()

    # Function_64_A155 end

    def Function_65_A276(): pass

    label("Function_65_A276")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A338")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010FIt's late... We should just\x01",
            "go back to the hotel.\x02\x03",
            "We really need to get what\x01",
            "rest we can.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000FLet's see... The hotel is in\x01",
            "the North Block, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3A2")

    label("loc_A338")


    ChrTalk(
        0x102,
        (
            "#010FIt's late... We should just\x01",
            "go back to the hotel.\x02\x03",
            "We need to rest up for\x01",
            "tomorrow's big match.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3A2")

    Call(0, 72)
    Return()

    # Function_65_A276 end

    def Function_66_A3A7(): pass

    label("Function_66_A3A7")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4DA")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A446")

    ChrTalk(
        0x102,
        (
            "#010FNial must be waiting for us.\x02\x03",
            "He should be at the News Service\x01",
            "building in the West Block.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FOkay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A4D7")

    label("loc_A446")


    ChrTalk(
        0x102,
        (
            "#010FThat's the exit, Estelle...\x02\x03",
            "Nial's supposed to be at the News\x01",
            "Service building in the West Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FOkay, okay...\x01",
            "My mistake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4D7")

    Jump("loc_A551")

    label("loc_A4DA")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FI'd imagine that Nial's waiting for us.\x02\x03",
            "He should be at the News Service\x01",
            "building in the West Block.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A551")

    Call(0, 72)
    Return()

    # Function_66_A3A7 end

    def Function_67_A556(): pass

    label("Function_67_A556")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A603")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010FFor now, let's report in at the guild.\x02\x03",
            "We ought to let them know what\x01",
            "Nial's investigation turned up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006FYeah, you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A674")

    label("loc_A603")


    ChrTalk(
        0x102,
        (
            "#010FFor now, let's report in at the guild.\x02\x03",
            "We ought to let them know what\x01",
            "Nial's investigation turned up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A674")

    Call(0, 72)
    Return()

    # Function_67_A556 end

    def Function_68_A679(): pass

    label("Function_68_A679")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A724")

    ChrTalk(
        0x108,
        (
            "#070FWow... Night already. It feels\x01",
            "a little weird being outside\x01",
            "like this.\x02\x03",
            "Since we're done for today,\x01",
            "why don't we check in at that\x01",
            "dinner party?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7BF")

    label("loc_A724")

    TurnDirection(0x108, 0x0, 400)

    ChrTalk(
        0x108,
        (
            "#070FHey... You're not thinking of\x01",
            "leaving already, are you?\x02\x03",
            "Your devotion to training is\x01",
            "admirable, but we do have a\x01",
            "dinner party to attend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7BF")

    Call(0, 72)
    Return()

    # Function_68_A679 end

    def Function_69_A7C4(): pass

    label("Function_69_A7C4")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A84B")

    ChrTalk(
        0x108,
        (
            "#070FThis is no time to go on the road.\x02\x03",
            "If everything's set up, then\x01",
            "why don't we head for the \x01",
            "Grancel Sewers?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C8")

    label("loc_A84B")

    TurnDirection(0x108, 0x0, 400)

    ChrTalk(
        0x108,
        (
            "#070FThis is no time to go on the road.\x02\x03",
            "If everything's set up, then\x01",
            "why don't we head for the \x01",
            "Grancel Sewers?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8C8")

    Call(0, 72)
    Return()

    # Function_69_A7C4 end

    def Function_70_A8CD(): pass

    label("Function_70_A8CD")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9F8")

    ChrTalk(
        0x101,
        "#501FOh, this way leads outside...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000FWhy don't we explore some more\x01",
            "of the city before we leave?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FYeah, you're right. There's\x01",
            "plenty more to see.\x02\x03",
            "If you're tired, there's a rest\x01",
            "area over in the East Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FI like the sound of that.侓\x02",
    )

    CloseMessageWindow()
    Jump("loc_AADD")

    label("loc_A9F8")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000FWhy don't we walk around\x01",
            "town a little longer?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FYeah, you're right. There's\x01",
            "plenty more to see.\x02\x03",
            "If you're tired, there's a rest\x01",
            "area over in the East Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FI like the sound of that.侓\x02",
    )

    CloseMessageWindow()

    label("loc_AADD")

    Call(0, 72)
    Return()

    # Function_70_A8CD end

    def Function_71_AAE2(): pass

    label("Function_71_AAE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABCC")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB80")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012FWe've still got time before we\x01",
            "need to go, Estelle.\x02\x03",
            "For now, let's go to the cathedral.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002FOkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_ABC8")

    label("loc_AB80")


    ChrTalk(
        0x102,
        (
            "#012FIt's not time to go yet.\x02\x03",
            "For now, let's go to the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABC8")

    Call(0, 72)

    label("loc_ABCC")

    Return()

    # Function_71_AAE2 end

    def Function_72_ABCD(): pass

    label("Function_72_ABCD")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_72_ABCD end

    def Function_73_ABE9(): pass

    label("Function_73_ABE9")

    SetPlaceName(0xB9) # 阳光铃铛酒廊
    Return()

    # Function_73_ABE9 end

    def Function_74_ABED(): pass

    label("Function_74_ABED")

    SetPlaceName(0xB0) # 阳光铃铛酒廊
    Return()

    # Function_74_ABED end

    def Function_75_ABF1(): pass

    label("Function_75_ABF1")

    SetPlaceName(0xB2) # 阳光铃铛酒廊
    Return()

    # Function_75_ABF1 end

    def Function_76_ABF5(): pass

    label("Function_76_ABF5")

    SetPlaceName(0xAE) # 阳光铃铛酒廊
    Return()

    # Function_76_ABF5 end

    def Function_77_ABF9(): pass

    label("Function_77_ABF9")

    SetPlaceName(0xB3) # 阳光铃铛酒廊
    Return()

    # Function_77_ABF9 end

    SaveToFile()

Try(main)
