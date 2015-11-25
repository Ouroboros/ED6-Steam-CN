from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4204   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4204.x',
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
        'Special Ops Soldier',                  # 9
        'Special Ops Soldier',                  # 10
        'Head Maid Hilda',                      # 11
        'Captain Amalthea',                     # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Special Ops Soldier',                  # 15
        'Special Ops Soldier',                  # 16
        'Special Ops Soldier',                  # 17
        'Special Ops Soldier',                  # 18
        'Special Ops Soldier',                  # 19
        'Kloe',                                 # 20
        'Olivier',                              # 21
        'Agate',                                # 22
        'Scherazard',                           # 23
        'Zane',                                 # 24
        'Tita',                                 # 25
        'Professor Russell',                    # 26
        'Cassius',                              # 27
        'Nial',                                 # 28
        'Dorothy',                              # 29
        'Major Cid',                            # 30
        'General Morgan',                       # 31
        '1st Lieutenant Schwarz',               # 32
        'Queen Alicia',                         # 33
        'Mylene',                               # 34
        'Mayor Klaus',                          # 35
        'Lila',                                 # 36
        'Mayor Maybelle',                       # 37
        'Dean Collins',                         # 38
        'Factory Chief Murdock',                # 39
        'Royal Guardsman',                      # 40
        'Royal Guardsman',                      # 41
        'Royal Guardsman',                      # 42
        'Royal Guardsman',                      # 43
        'Royal Guardsman',                      # 44
        'Royal Guardsman',                      # 45
        'Joshua',                               # 46
        'Special Ops Frigate',                  # 47
        'Special Ops Frigate Shadow',           # 48
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
        'ED6_DT07/CH01610 ._CH',             # 00
        'ED6_DT07/CH02460 ._CH',             # 01
        'ED6_DT07/CH02230 ._CH',             # 02
        'ED6_DT07/CH02240 ._CH',             # 03
        'ED6_DT07/CH02100 ._CH',             # 04
        'ED6_DT07/CH00100 ._CH',             # 05
        'ED6_DT07/CH00101 ._CH',             # 06
        'ED6_DT07/CH00120 ._CH',             # 07
        'ED6_DT07/CH00121 ._CH',             # 08
        'ED6_DT07/CH00140 ._CH',             # 09
        'ED6_DT07/CH00141 ._CH',             # 0A
        'ED6_DT07/CH02340 ._CH',             # 0B
        'ED6_DT07/CH00030 ._CH',             # 0C
        'ED6_DT07/CH00050 ._CH',             # 0D
        'ED6_DT07/CH00020 ._CH',             # 0E
        'ED6_DT07/CH00070 ._CH',             # 0F
        'ED6_DT07/CH00060 ._CH',             # 10
        'ED6_DT07/CH02020 ._CH',             # 11
        'ED6_DT07/CH02000 ._CH',             # 12
        'ED6_DT07/CH02060 ._CH',             # 13
        'ED6_DT07/CH02070 ._CH',             # 14
        'ED6_DT07/CH02450 ._CH',             # 15
        'ED6_DT07/CH02080 ._CH',             # 16
        'ED6_DT07/CH02090 ._CH',             # 17
        'ED6_DT07/CH02010 ._CH',             # 18
        'ED6_DT07/CH01180 ._CH',             # 19
        'ED6_DT07/CH02350 ._CH',             # 1A
        'ED6_DT07/CH02370 ._CH',             # 1B
        'ED6_DT07/CH02360 ._CH',             # 1C
        'ED6_DT07/CH02600 ._CH',             # 1D
        'ED6_DT07/CH02620 ._CH',             # 1E
        'ED6_DT07/CH01320 ._CH',             # 1F
        'ED6_DT06/CH20030 ._CH',             # 20
        'ED6_DT07/CH00010 ._CH',             # 21
        'ED6_DT07/CH00341 ._CH',             # 22
        'ED6_DT06/CH20042 ._CH',             # 23
        'ED6_DT06/CH20040 ._CH',             # 24
        'ED6_DT06/CH20060 ._CH',             # 25
        'ED6_DT07/CH00004 ._CH',             # 26
        'ED6_DT06/CH20148 ._CH',             # 27
        'ED6_DT06/CH20149 ._CH',             # 28
        'ED6_DT06/CH20150 ._CH',             # 29
        'ED6_DT06/CH20151 ._CH',             # 2A
        'ED6_DT06/CH20152 ._CH',             # 2B
        'ED6_DT06/CH20153 ._CH',             # 2C
        'ED6_DT06/CH20154 ._CH',             # 2D
    )

    AddCharChipPat(
        'ED6_DT07/CH01610P._CP',             # 00
        'ED6_DT07/CH02460P._CP',             # 01
        'ED6_DT07/CH02230P._CP',             # 02
        'ED6_DT07/CH02240P._CP',             # 03
        'ED6_DT07/CH02100P._CP',             # 04
        'ED6_DT07/CH00100P._CP',             # 05
        'ED6_DT07/CH00101P._CP',             # 06
        'ED6_DT07/CH00120P._CP',             # 07
        'ED6_DT07/CH00121P._CP',             # 08
        'ED6_DT07/CH00140P._CP',             # 09
        'ED6_DT07/CH00141P._CP',             # 0A
        'ED6_DT07/CH02340P._CP',             # 0B
        'ED6_DT07/CH00030P._CP',             # 0C
        'ED6_DT07/CH00050P._CP',             # 0D
        'ED6_DT07/CH00020P._CP',             # 0E
        'ED6_DT07/CH00070P._CP',             # 0F
        'ED6_DT07/CH00060P._CP',             # 10
        'ED6_DT07/CH02020P._CP',             # 11
        'ED6_DT07/CH02000P._CP',             # 12
        'ED6_DT07/CH02060P._CP',             # 13
        'ED6_DT07/CH02070P._CP',             # 14
        'ED6_DT07/CH02450P._CP',             # 15
        'ED6_DT07/CH02080P._CP',             # 16
        'ED6_DT07/CH02090P._CP',             # 17
        'ED6_DT07/CH02010P._CP',             # 18
        'ED6_DT07/CH01180P._CP',             # 19
        'ED6_DT07/CH02350P._CP',             # 1A
        'ED6_DT07/CH02370P._CP',             # 1B
        'ED6_DT07/CH02360P._CP',             # 1C
        'ED6_DT07/CH02600P._CP',             # 1D
        'ED6_DT07/CH02620P._CP',             # 1E
        'ED6_DT07/CH01320P._CP',             # 1F
        'ED6_DT06/CH20030P._CP',             # 20
        'ED6_DT07/CH00010P._CP',             # 21
        'ED6_DT07/CH00341P._CP',             # 22
        'ED6_DT06/CH20042P._CP',             # 23
        'ED6_DT06/CH20040P._CP',             # 24
        'ED6_DT06/CH20060P._CP',             # 25
        'ED6_DT07/CH00004P._CP',             # 26
        'ED6_DT06/CH20148P._CP',             # 27
        'ED6_DT06/CH20149P._CP',             # 28
        'ED6_DT06/CH20150P._CP',             # 29
        'ED6_DT06/CH20151P._CP',             # 2A
        'ED6_DT06/CH20152P._CP',             # 2B
        'ED6_DT06/CH20153P._CP',             # 2C
        'ED6_DT06/CH20154P._CP',             # 2D
    )

    DeclNpc(
        X                   = -870,
        Z                   = 19750,
        Y                   = 107200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 910,
        Z                   = 19750,
        Y                   = 107200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 24,
        ChipIndex           = 0x18,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 27,
        ChipIndex           = 0x1B,
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
        Unknown3            = 28,
        ChipIndex           = 0x1C,
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
        Unknown3            = 29,
        ChipIndex           = 0x1D,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -4710,
        Y                   = 18000,
        Z                   = 94670,
        Range               = 5130,
        Unknown_10          = 0x3E80,
        Unknown_14          = 0x16A1C,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -4340,
        Y                   = 19000,
        Z                   = 105990,
        Range               = 4220,
        Unknown_10          = 0x4650,
        Unknown_14          = 0x1933E,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -4280,
        Y                   = 16000,
        Z                   = 78500,
        Range               = 5010,
        Unknown_10          = 0x32C8,
        Unknown_14          = 0x1270A,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -4730,
        Y                   = 18000,
        Z                   = 98010,
        Range               = 4880,
        Unknown_10          = 0x3E80,
        Unknown_14          = 0x17534,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = -33010,
        Y                   = 15000,
        Z                   = 79090,
        Range               = -37530,
        Unknown_10          = 0x4268,
        Unknown_14          = 0x11882,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -4340,
        Y                   = 21000,
        Z                   = 108990,
        Range               = 4220,
        Unknown_10          = 0x4268,
        Unknown_14          = 0x19EF6,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )


    ScpFunction(
        "Function_0_7DA",          # 00, 0
        "Function_1_8D1",          # 01, 1
        "Function_2_966",          # 02, 2
        "Function_3_97C",          # 03, 3
        "Function_4_C04",          # 04, 4
        "Function_5_1BC3",         # 05, 5
        "Function_6_2155",         # 06, 6
        "Function_7_29B9",         # 07, 7
        "Function_8_2E89",         # 08, 8
        "Function_9_2EB2",         # 09, 9
        "Function_10_2EE0",        # 0A, 10
        "Function_11_2F0E",        # 0B, 11
        "Function_12_346F",        # 0C, 12
        "Function_13_36C6",        # 0D, 13
        "Function_14_37FF",        # 0E, 14
        "Function_15_3A35",        # 0F, 15
        "Function_16_3EDF",        # 10, 16
        "Function_17_3FA8",        # 11, 17
        "Function_18_3FAF",        # 12, 18
        "Function_19_5F1D",        # 13, 19
    )


    def Function_0_7DA(): pass

    label("Function_0_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_818")
    SetChrChipByIndex(0x2D, 32)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2D, -42970, 16000, 81320, 270)
    SetChrFlags(0x2D, 0x4)

    def lambda_807():

        label("loc_807")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_807")

    QueueWorkItem2(0x2D, 1, lambda_807)
    Event(0, 17)

    label("loc_818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_829")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_837")
    OP_A3(0x3FA)
    Event(0, 7)

    label("loc_837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_845")
    OP_A3(0x3FB)
    Event(0, 11)

    label("loc_845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_853")
    OP_A3(0x3FC)
    Event(0, 15)

    label("loc_853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_86A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FD)
    Event(0, 16)

    label("loc_86A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_87A"),
        (101, "loc_890"),
        (SWITCH_DEFAULT, "loc_8A6"),
    )


    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88D")
    OP_A2(0x63D)
    Event(0, 3)

    label("loc_88D")

    Jump("loc_8A6")

    label("loc_890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A3")
    OP_A2(0x645)
    Event(0, 6)

    label("loc_8A3")

    Jump("loc_8A6")

    label("loc_8A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D0")
    SetChrChipByIndex(0x0, 1)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_8D0")

    Return()

    # Function_0_7DA end

    def Function_1_8D1(): pass

    label("Function_1_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_8E9")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F9")

    label("loc_8E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_8F9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_965")
    OP_1B(0x0, 0x0, 0xD)
    OP_A1(0x2E, 0x0)
    OP_A1(0x2F, 0x1)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x2)
    OP_71(0x0, 0x400)
    OP_71(0x0, 0x40)
    OP_72(0x1, 0x4)
    OP_72(0x1, 0x2)
    OP_71(0x1, 0x400)
    OP_71(0x1, 0x40)
    SetChrPos(0x2E, 2320, 12050, 57280, 56)
    SetChrPos(0x2F, 2320, 12050, 57280, 56)
    OP_6F(0x0, 1200)

    label("loc_965")

    Return()

    # Function_1_8D1 end

    def Function_2_966(): pass

    label("Function_2_966")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_97B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_966")

    label("loc_97B")

    Return()

    # Function_2_966 end

    def Function_3_97C(): pass

    label("Function_3_97C")

    EventBegin(0x0)
    OP_6D(-43010, 16000, 79950, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(8050, 0)
    OP_6C(69000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 29890, 9500, 76540, 0)
    SetChrPos(0x102, 31020, 9500, 76540, 0)
    FadeToBright(2000, 0)

    def lambda_9EC():
        OP_6D(31020, 10750, 79090, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9EC)

    def lambda_A04():
        OP_6C(45000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A04)
    Sleep(7500)

    def lambda_A19():
        OP_8E(0xFE, 0x733C, 0x2EE0, 0x15306, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A19)
    Sleep(400)

    def lambda_A39():
        OP_8E(0xFE, 0x745E, 0x2EE0, 0x14DDE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A39)
    WaitChrThread(0x101, 0x2)
    Fade(1000)
    OP_6D(29640, 12000, 86120, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x101,
        (
            "#008FOh, wow...\x01",
            "Check that out...\x02\x03",
            "This must be the castle's\x01",
            "Garden Terrace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI'd say so... You can see the\x01",
            "whole lake from here, and it\x01",
            "overlooks the town, too.\x02\x03",
            "#019FMust be great for reconnaissance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F*sigh*... As nice as this is,\x01",
            "we really don't have time to\x01",
            "stop and enjoy it.\x02\x03",
            "#006FWe've got a job to do.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    EventEnd(0x0)
    Return()

    # Function_3_97C end

    def Function_4_C04(): pass

    label("Function_4_C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_END)), "loc_C0C")
    Return()

    label("loc_C0C")

    OP_A2(0x63E)
    OP_28(0x49, 0x1, 0x400)
    EventBegin(0x0)
    OP_8C(0x101, 0, 0)
    OP_8C(0x102, 0, 0)

    ChrTalk(
        0x101,
        "#004FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FThis must be the Royal Keep...\x02",
    )

    CloseMessageWindow()

    def lambda_C64():

        label("loc_C64")

        OP_8C(0xFE, 0, 0)
        OP_48()
        Jump("loc_C64")

    QueueWorkItem2(0x101, 2, lambda_C64)

    def lambda_C75():

        label("loc_C75")

        OP_8C(0xFE, 0, 0)
        OP_48()
        Jump("loc_C75")

    QueueWorkItem2(0x102, 2, lambda_C75)

    def lambda_C86():
        OP_8E(0xFE, 0x370, 0x4650, 0x194BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C86)

    def lambda_CA1():
        OP_8E(0xFE, 0xFFFFFD76, 0x4650, 0x19438, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CA1)

    def lambda_CBC():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_CBC)
    OP_6D(-160, 19000, 105620, 3000)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Hm? Who are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3PHey, you two...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)

    ChrTalk(
        0x101,
        (
            "#006FUmmm...\x02\x03",
            "We're here as guests\x01",
            "of the duke...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x102,
        "#010FIs this where Her Majesty lives?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3POf course it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But for the last few days, she\x01",
            "hasn't been feeling so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She's not seeing anyone\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FO-Oh, you've got it all wrong. We\x01",
            "weren't even thinking of that.\x02\x03",
            "I just thought it would be\x01",
            "amazing if she were to even\x01",
            "take notice of us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FDoes Princess Klaudia sleep\x01",
            "here, as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "No, it's just--\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 800)

    ChrTalk(
        0x9,
        "#4P...Hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The princess is focused on\x01",
            "looking after Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Neither of them has time to\x01",
            "deal with the likes of you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, 280, 20000, 111970, 0)

    NpcTalk(
        0xA,
        "Woman's Voice",
        (
            "#4PMight I inquire as to what's\x01",
            "going on here?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0xA, 0x80)

    def lambda_1038():
        OP_8E(0xFE, 0x82, 0x4C2C, 0x1A13A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1038)

    def lambda_1053():

        label("loc_1053")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1053")

    QueueWorkItem2(0x8, 1, lambda_1053)

    def lambda_1064():
        OP_8E(0xFE, 0xFFFFF9FC, 0x4D26, 0x1A22A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1064)

    def lambda_107F():

        label("loc_107F")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_107F")

    QueueWorkItem2(0x9, 1, lambda_107F)

    def lambda_1090():
        OP_8E(0xFE, 0xFFFFFA24, 0x4B32, 0x19EEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1090)
    WaitChrThread(0x9, 0x2)

    ChrTalk(
        0x8,
        "#3PMadam...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3PWe didn't know you were\x01",
            "back already.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x2)
    TurnDirection(0xA, 0x8, 400)

    NpcTalk(
        0xA,
        "Middle-Aged Woman",
        (
            "#710F#4PThe dinner party will be starting soon, so\x01",
            "I will be returning to the maid quarters.\x02\x03",
            "And who are our guests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PThey're from the team that won\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIt's only because of that victory\x01",
            "that someone of a bracer's social\x01",
            "standing would ever be invited here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009FA 'bracer's social standing'...?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Middle-Aged Woman",
        "#717F#4P#5SSuch discourtesy!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(200)

    NpcTalk(
        0xA,
        "Middle-Aged Woman",
        (
            "#717F#4PYou would insult those who\x01",
            "were personally invited to\x01",
            "the royal castle?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x9,
        (
            "#3PNo...\x01",
            "That's not what...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Middle-Aged Woman",
        (
            "#717F#4PThose invited by the duke should be\x01",
            "treated with all the respect due to\x01",
            "those invited by Her Majesty!\x02\x03",
            "I sincerely hope you have\x01",
            "not forgotten that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3P...U-Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F(Wow, she's intense...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F(I wonder who she is...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PBut, madam... We can't just\x01",
            "allow them to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PSurely you understand the reasons\x01",
            "that the colonel laid out.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Middle-Aged Woman",
        (
            "#716F#4P...Yes, and I'm quite tired of\x01",
            "hearing them repeated to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)

    def lambda_1551():

        label("loc_1551")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_1551")

    QueueWorkItem2(0x101, 1, lambda_1551)

    def lambda_1562():

        label("loc_1562")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_1562")

    QueueWorkItem2(0x102, 1, lambda_1562)
    OP_8E(0xA, 0x8C, 0x4844, 0x19938, 0x7D0, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    NpcTalk(
        0xA,
        "Middle-Aged Woman",
        (
            "#710F#5PI am terribly sorry,\x01",
            "sir and madam.\x02\x03",
            "Security has been heightened, and\x01",
            "as such, the Royal Keep and its\x01",
            "surroundings are off limits.\x02\x03",
            "If I may ask, would you mind\x01",
            "waiting in your room until the\x01",
            "dinner party begins?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FAh... A-All right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThat's fine.\x01",
            "We'll do as you ask.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        (
            "#015FI apologize. We weren't trying\x01",
            "to cause any trouble.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "Hmph...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "#3PFine, then. Just don't let\x01",
            "it happen again.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    NpcTalk(
        0xA,
        "Middle-Aged Woman",
        "#714F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh... S-Safe return to you.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(470, 15250, 86110, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, -620, 15500, 86640, 180)
    SetChrPos(0x102, 1430, 15500, 86590, 180)
    SetChrPos(0xA, 310, 15000, 85930, 180)

    def lambda_180C():

        label("loc_180C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_180C")

    QueueWorkItem2(0x101, 1, lambda_180C)

    def lambda_181D():

        label("loc_181D")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_181D")

    QueueWorkItem2(0x102, 1, lambda_181D)

    def lambda_182E():
        OP_8E(0xFE, 0xFFFFFF24, 0x36B0, 0x139A2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_182E)

    def lambda_1849():
        OP_8E(0xFE, 0xFFFFFC72, 0x36B0, 0x13D4E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1849)

    def lambda_1864():
        OP_8E(0xFE, 0x1EA, 0x36B0, 0x13EAC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1864)

    def lambda_187F():
        OP_6D(-90, 14000, 81270, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_187F)
    WaitChrThread(0xA, 0x1)
    OP_8C(0xA, 0, 400)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x102, 0x2)

    NpcTalk(
        0xA,
        "Middle-Aged Woman",
        (
            "#711FI apologize that you were subjected\x01",
            "to such dreadful behavior.\x02\x03",
            "My name is Hilda.\x02\x03",
            "I am the head maid of Grancel\x01",
            "Castle, and I oversee all of\x01",
            "the housekeeping duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FAh-ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe had a feeling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#712FHmm?\x02\x03",
            "Forgive my rudeness, but are\x01",
            "we previously acquainted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FWell, uh... Someone told us\x01",
            "about you.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0xA, 0x258, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed '\x07\x02",
            "Julia's Letter\x07\x00",
            "' to Hilda.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x36C, 1)
    OP_8F(0x101, 0xFFFFFC72, 0x36B0, 0x13D4E, 0x7D0, 0x0)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#712FI know this handwriting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FYou see?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe also have our bracer emblems\x01",
            "and identification with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#713FI see...\x02\x03",
            "#710FPlease, come with me to the\x01",
            "maids' sitting room.\x02\x03",
            "We can discuss the matter\x01",
            "further once we are there.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4254   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_C04 end

    def Function_5_1BC3(): pass

    label("Function_5_1BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BD0")
    Return()

    label("loc_1BD0")

    OP_28(0x4A, 0x1, 0x80)
    EventBegin(0x0)
    Fade(1000)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x138, 1)
    SetChrPos(0x138, 10, 18500, 104700, 0)
    SetChrPos(0x101, -470, 18000, 103350, 0)
    SetChrPos(0x102, 740, 18000, 103280, 0)
    OP_6D(-70, 19000, 105810, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_0D()

    ChrTalk(
        0x8,
        "Hilda...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3P#3PWhat business do you have with\x01",
            "Her Majesty at this hour?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710FI'm bringing some tea and\x01",
            "spoons at her request.\x02\x03",
            "#713FThe current situation means that Her Majesty\x01",
            "is denied the right to even go about her daily\x01",
            "life as she wishes, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Such harsh words...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3PWho are these maids with you?\x01",
            "I don't recognize them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710FHis Excellency ordered me to\x01",
            "hire on some additional staff\x01",
            "to help.\x02\x03",
            "They've only just arrived\x01",
            "at the castle today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Really, now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3PHey, you're pretty cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#474FTh-Thank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#336F...(*bows*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why do I get the feeling\x01",
            "we've met before...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#323F(Crap...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#714FDo you stare so hard at every\x01",
            "young lady you see?\x02\x03",
            "I do hope you're not thinking\x01",
            "any untoward thoughts.\x02\x03",
            "I rather think that His Excellency\x01",
            "and the colonel would disapprove.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "H-Hey! It's not like that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3PWe're the elite of the Royal Army.\x01",
            "We wouldn't do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#713FAll's well, then.\x02\x03",
            "#710FNow, will you please allow\x01",
            "us to pass?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Pardon us, ladies!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    OP_8C(0x8, 90, 400)

    def lambda_2096():
        OP_8F(0xFE, 0xFFFFF704, 0x4D26, 0x1A2C0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2096)

    ChrTalk(
        0x9,
        "#3PPlease, go ahead!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)

    def lambda_20D2():
        OP_8F(0xFE, 0x92E, 0x4D26, 0x1A2C0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20D2)
    FadeToDark(2000, 0, -1)

    def lambda_20F7():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_20F7)
    Sleep(50)

    def lambda_2117():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2117)

    def lambda_2132():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2132)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4270   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1BC3 end

    def Function_6_2155(): pass

    label("Function_6_2155")

    EventBegin(0x0)
    OP_6D(-220, 20000, 107550, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x8, -2390, 19750, 107200, 180)
    SetChrPos(0x9, 2290, 19750, 107200, 180)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)

    def lambda_21A2():

        label("loc_21A2")

        TurnDirection(0xFE, 0x138, 0)
        OP_48()
        Jump("loc_21A2")

    QueueWorkItem2(0x8, 2, lambda_21A2)

    def lambda_21B3():

        label("loc_21B3")

        TurnDirection(0xFE, 0x138, 0)
        OP_48()
        Jump("loc_21B3")

    QueueWorkItem2(0x9, 2, lambda_21B3)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x138, 1)
    SetChrPos(0x101, -990, 20000, 110860, 180)
    SetChrPos(0x102, 1070, 20000, 111050, 0)
    SetChrPos(0x138, 120, 20000, 110230, 180)

    def lambda_2206():
        OP_8E(0xFE, 0xBE, 0x4B32, 0x19F64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_2206)

    def lambda_2221():
        OP_8E(0xFE, 0xFFFFFE20, 0x4D26, 0x1A310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2221)

    def lambda_223C():
        OP_8E(0xFE, 0x35C, 0x4D26, 0x1A310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_223C)
    WaitChrThread(0x138, 0x1)
    TurnDirection(0x138, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "Are you going home for\x01",
            "the day, Miss Hilda?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710FYes, I believe so.\x02\x03",
            "Just be sure not to do Her Majesty\x01",
            "any further discourtesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "That's not fair...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But please, relax. We are\x01",
            "patriots to the core.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#713FThat's good to hear.\x02\x03",
            "Now, I believe that we shall\x01",
            "be on our way.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        "#474FP-Pardon me...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 135, 400)

    ChrTalk(
        0x102,
        "#336FBy your leave...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x138, 180, 400)

    def lambda_23D0():
        OP_6D(230, 19000, 105820, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_23D0)

    def lambda_23E8():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_23E8)
    Sleep(100)

    def lambda_2408():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2408)

    def lambda_2423():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2423)

    def lambda_243E():
        OP_8F(0xFE, 0xFFFFFC9A, 0x4D26, 0x1A2C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_243E)
    Sleep(100)

    def lambda_245E():
        OP_8F(0xFE, 0x38E, 0x4D26, 0x1A2C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_245E)
    Sleep(1100)

    ChrTalk(
        0x8,
        "By the way, ladies...\x02",
    )

    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x4)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    CloseMessageWindow()

    def lambda_24DE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_24DE)

    def lambda_24EC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24EC)
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        "#324F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't think we ever\x01",
            "got your names.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "May we ask them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#473FI, uh, um...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Lena]\x01",         # 0
            "[Schera]\x01",       # 1
            "[Dorothy]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_25D1"),
        (1, "loc_264B"),
        (2, "loc_2731"),
        (SWITCH_DEFAULT, "loc_27C5"),
    )


    label("loc_25D1")

    OP_A2(0x676)

    ChrTalk(
        0x8,
        "My... Isn't that a lovely name?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It has a pleasant ring to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#328FI...uh...\x01",
            "Th-Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C5")

    label("loc_264B")

    OP_A2(0x677)

    ChrTalk(
        0x8,
        (
            "My...\x01",
            "That's certainly a sexy name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You don't...look like a 'Schera,' though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#325FH-Hey! Watch your mouths!\x02\x03",
            "#474F...Ho ho ho! Did I catch\x01",
            "you off-guard?\x02\x03",
            "S-See? I'm a very assertive,\x01",
            "s-s-sexy young woman!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C5")

    label("loc_2731")

    OP_A2(0x678)

    ChrTalk(
        0x8,
        (
            "Hmm...\x01",
            "That's a very modern name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Pardon my saying so, but it just\x01",
            "doesn't sound right for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#327F(Ain't THAT the truth...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_27C5")

    label("loc_27C5")


    ChrTalk(
        0x9,
        "#3PAnd how about you, miss?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#336FYou may call me Karin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3PKarin, you say...?\x01",
            "That's a very pretty name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#331FYou're too kind, sir.\x02\x03",
            "I'm rather fond of it myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3PAre you, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3POh! Right. We're with the\x01",
            "Special Ops. My name is--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#713FI think that's just about enough.\x02\x03",
            "I sense an ulterior motive at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3PNo... I mean, at least\x01",
            "not from us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#714F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Eep! P-Please, be safe on\x01",
            "your way home.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0x2)
    OP_44(0x9, 0x2)
    OP_8C(0x8, 180, 0)
    OP_8C(0x9, 180, 0)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    SetChrChipByIndex(0x0, 1)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    Return()

    # Function_6_2155 end

    def Function_7_29B9(): pass

    label("Function_7_29B9")

    EventBegin(0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0xB, 20, 12000, 47110, 180)
    SetChrPos(0x8, 940, 12000, 48110, 180)
    SetChrPos(0x9, -900, 12000, 48050, 180)
    SetChrPos(0xC, -60, 12000, 49430, 180)
    SetChrPos(0xD, 930, 12000, 50530, 180)
    SetChrPos(0xE, 930, 12000, 52440, 180)
    SetChrPos(0xF, 910, 12000, 54110, 180)
    SetChrPos(0x10, -890, 12000, 50560, 180)
    SetChrPos(0x11, -890, 12000, 52310, 180)
    SetChrPos(0x12, -890, 12000, 54310, 180)
    OP_6D(-20, 12000, 47150, 0)
    OP_67(0, 5910, -10000, 0)
    OP_6C(45000, 0)
    OP_6B(3400, 0)
    OP_6E(280, 0)

    ChrTalk(
        0xB,
        (
            "#180FSomeone had BETTER tell me this is\x01",
            "a bad joke. Why is the gate open...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Y-Your orders, Captain?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Enemies could breach the\x01",
            "castle at any moment!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B7F():
        OP_6D(-150, 12000, 49950, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2B7F)

    def lambda_2B97():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B97)

    def lambda_2BA5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2BA5)
    OP_8C(0xB, 0, 400)

    ChrTalk(
        0xB,
        (
            "#180FAll remaining members of the\x01",
            "first platoon to the Foyer!\x01",
            "On the double!!\x02\x03",
            "Allow no one to enter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Y-Yes, ma'am!\x02",
    )

    CloseMessageWindow()

    def lambda_2C38():

        label("loc_2C38")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2C38")

    QueueWorkItem2(0xD, 1, lambda_2C38)

    def lambda_2C49():

        label("loc_2C49")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2C49")

    QueueWorkItem2(0xE, 1, lambda_2C49)

    def lambda_2C5A():

        label("loc_2C5A")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2C5A")

    QueueWorkItem2(0xF, 1, lambda_2C5A)

    def lambda_2C6B():

        label("loc_2C6B")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2C6B")

    QueueWorkItem2(0x10, 1, lambda_2C6B)

    def lambda_2C7C():

        label("loc_2C7C")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2C7C")

    QueueWorkItem2(0x11, 1, lambda_2C7C)

    def lambda_2C8D():

        label("loc_2C8D")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2C8D")

    QueueWorkItem2(0x12, 1, lambda_2C8D)
    OP_8E(0xC, 0x906, 0x2EE0, 0xC166, 0x1388, 0x0)
    OP_8E(0xC, 0x906, 0x2EE0, 0xC5F8, 0x1388, 0x0)
    OP_43(0xD, 0x1, 0x0, 0x8)
    OP_43(0x10, 0x1, 0x0, 0x8)
    OP_8E(0xC, 0x906, 0x2EE0, 0xCCA6, 0x1388, 0x0)
    OP_43(0xE, 0x1, 0x0, 0x9)
    OP_43(0x11, 0x1, 0x0, 0x9)
    OP_8E(0xC, 0x906, 0x2EE0, 0xD796, 0x1388, 0x0)
    OP_43(0xF, 0x1, 0x0, 0xA)
    OP_43(0x12, 0x1, 0x0, 0xA)

    def lambda_2D18():
        OP_8E(0xFE, 0x92E, 0x2EE0, 0x11814, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2D18)
    OP_6D(90, 12000, 48130, 1000)

    ChrTalk(
        0xB,
        (
            "#180FWhat a disgrace...\x02\x03",
            "If the enemy is not routed\x01",
            "before I have to report to\x01",
            "His Excellency...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2DD8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2DD8)

    def lambda_2DE6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2DE6)
    Sleep(1000)

    ChrTalk(
        0x8,
        "C-Captain!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Special Ops Frigate inbound!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#180FDamn it! So that was their ploy?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/E0500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_29B9 end

    def Function_8_2E89(): pass

    label("Function_8_2E89")

    OP_8E(0xFE, 0x92E, 0x2EE0, 0xC5C6, 0x1388, 0x0)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0x11814, 0x1388, 0x0)
    Return()

    # Function_8_2E89 end

    def Function_9_2EB2(): pass

    label("Function_9_2EB2")

    Sleep(800)
    OP_8E(0xFE, 0x8F2, 0x2EE0, 0xCC92, 0x1388, 0x0)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0x11814, 0x1388, 0x0)
    Return()

    # Function_9_2EB2 end

    def Function_10_2EE0(): pass

    label("Function_10_2EE0")

    Sleep(1300)
    OP_8E(0xFE, 0x8F2, 0x2EE0, 0xD3F4, 0x1388, 0x0)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0x11814, 0x1388, 0x0)
    Return()

    # Function_10_2EE0 end

    def Function_11_2F0E(): pass

    label("Function_11_2F0E")

    EventBegin(0x0)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x0, 0xFF)
    AddParty(0x2, 0xFF)
    AddParty(0x4, 0xFF)
    OP_6D(610, 15350, 55470, 0)
    OP_67(0, 5210, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(29000, 0)
    OP_6E(413, 0)
    SetChrPos(0x8, -8650, 12000, 56840, 79)
    SetChrPos(0xB, -8029, 12000, 58490, 125)
    SetChrPos(0x9, -6650, 12000, 57720, 46)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    def lambda_2FA7():

        label("loc_2FA7")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2FA7")

    QueueWorkItem2(0xB, 1, lambda_2FA7)

    def lambda_2FB8():

        label("loc_2FB8")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2FB8")

    QueueWorkItem2(0x8, 1, lambda_2FB8)

    def lambda_2FC9():

        label("loc_2FC9")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2FC9")

    QueueWorkItem2(0x9, 1, lambda_2FC9)
    SetChrPos(0x101, 2880, 15350, 57740, 147)
    SetChrPos(0x103, 2880, 15350, 57740, 147)
    SetChrPos(0x105, 2880, 15350, 57740, 147)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x105, 9)
    FadeToBright(2000, 0)

    def lambda_3025():
        OP_67(0, 7370, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_3025)
    OP_6F(0x0, 241)
    OP_70(0x0, 0x168)
    OP_73(0x0)
    OP_6F(0x0, 1140)
    OP_70(0x0, 0x4B0)
    OP_73(0x0)

    def lambda_305F():

        label("loc_305F")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_305F")

    QueueWorkItem2(0x101, 1, lambda_305F)

    def lambda_3070():

        label("loc_3070")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_3070")

    QueueWorkItem2(0x105, 1, lambda_3070)

    def lambda_3081():

        label("loc_3081")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_3081")

    QueueWorkItem2(0x103, 1, lambda_3081)

    def lambda_3092():
        OP_6D(-7590, 12000, 54940, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3092)

    def lambda_30AA():
        OP_6E(291, 4000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_30AA)

    def lambda_30BA():
        OP_8E(0xFE, 0xFFFFECB4, 0x31A6, 0xD00C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30BA)
    Sleep(400)

    def lambda_30DA():
        OP_8E(0xFE, 0xFFFFE3C2, 0x2EE0, 0xC8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_30DA)
    Sleep(400)

    def lambda_30FA():
        OP_8E(0xFE, 0xFFFFE912, 0x2EE0, 0xCB52, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_30FA)
    WaitChrThread(0x101, 0x2)

    def lambda_311A():
        OP_96(0xFE, 0xFFFFE480, 0x2EE0, 0xCDDC, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_311A)
    WaitChrThread(0x103, 0x2)

    def lambda_313D():
        OP_8E(0xFE, 0xFFFFDE7C, 0x2EE0, 0xCD00, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_313D)
    WaitChrThread(0x105, 0x2)

    def lambda_315D():
        OP_8E(0xFE, 0xFFFFE16A, 0x2EE0, 0xC8E6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_315D)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0xB,
        (
            "#180FEstelle Bright!\x02\x03",
            "And...Princess Klaudia?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FCaptain Amalthea!\x01",
            "Stand aside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040FI'm here to demand the release\x01",
            "of my grandmother!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#180FWatch your tongue, girl!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0x3A8, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_3264"),
        (SWITCH_DEFAULT, "loc_3267"),
    )


    label("loc_3264")

    OP_B4(0x0)
    Return()

    label("loc_3267")

    EventBegin(0x0)
    OP_6D(-7800, 12000, 57810, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(9000, 0)
    OP_6E(280, 0)
    SetChrPos(0xB, -9230, 12000, 57550, 258)
    SetChrPos(0x8, -9060, 12000, 59260, 302)
    SetChrPos(0x9, -7670, 12000, 59020, 103)
    SetChrPos(0x101, -6550, 12000, 56030, 282)
    SetChrPos(0x103, -8180, 12000, 54960, 331)
    SetChrPos(0x105, -7070, 12000, 54530, 325)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 36)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 35)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 35)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 65535)
    OP_51(0x105, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 65535)

    ChrTalk(
        0x103,
        (
            "#020FUgh...\x01",
            "What a nasty woman.\x02\x03",
            "Who was that, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FColonel Richard's second-in-command.\x02\x03",
            "Your stereotypical femme fatale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FThat would explain it, yes.\x02\x03",
            "Now, on to the Royal Keep!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040FYes! Let's hurry!\x02",
    )

    CloseMessageWindow()
    OP_28(0x4E, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_11_2F0E end

    def Function_12_346F(): pass

    label("Function_12_346F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_347C")
    Return()

    label("loc_347C")

    EventBegin(0x0)
    OP_A2(0x662)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xE, 13020, 14000, 78670, 270)
    SetChrPos(0xF, 14450, 14000, 79840, 270)
    SetChrPos(0x10, 14130, 14000, 77880, 270)

    ChrTalk(
        0xE,
        "I found them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "This way!\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x101, 1230, 14000, 77770, 90)
    SetChrPos(0x103, -420, 14000, 78370, 90)
    SetChrPos(0x105, -300, 14000, 77020, 90)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x105, 9)
    OP_6D(6360, 14000, 78900, 2000)

    ChrTalk(
        0x101,
        (
            "#000FUh-oh!\x01",
            "Here they come again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FPersistent little buggers,\x01",
            "aren't they?\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 34)
    SetChrChipByIndex(0xF, 34)
    SetChrChipByIndex(0x10, 34)

    def lambda_35AB():
        OP_6D(2650, 14000, 77790, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35AB)

    def lambda_35C3():
        OP_8E(0xFE, 0xFFFFAFD8, 0x36B0, 0x130EC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_35C3)

    def lambda_35DE():
        OP_8E(0xFE, 0xFFFFAFD8, 0x36B0, 0x130EC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_35DE)

    def lambda_35F9():
        OP_8E(0xFE, 0xFFFFAFD8, 0x36B0, 0x130EC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_35F9)
    Sleep(500)
    Battle(0x3A9, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_362C"),
        (SWITCH_DEFAULT, "loc_362F"),
    )


    label("loc_362C")

    OP_B4(0x0)
    Return()

    label("loc_362F")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrPos(0x101, 1230, 14000, 77770, 90)
    SetChrPos(0x103, -420, 14000, 78370, 90)
    SetChrPos(0x105, -300, 14000, 77020, 90)
    SetChrPos(0xE, 3390, 14000, 79480, 146)
    SetChrPos(0xF, 3080, 14000, 77370, 283)
    SetChrPos(0x10, 5260, 14000, 77990, 28)
    Sleep(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)
    EventEnd(0x0)
    Return()

    # Function_12_346F end

    def Function_13_36C6(): pass

    label("Function_13_36C6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3730")

    ChrTalk(
        0x105,
        (
            "#040FEstelle! That way leads\x01",
            "into the castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020FCome on! To the Royal Keep!\x02",
    )

    CloseMessageWindow()
    Jump("loc_37E3")

    label("loc_3730")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_377B")

    ChrTalk(
        0x105,
        (
            "#040FNot that way...! We have to go\x01",
            "to the Royal Keep!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E3")

    label("loc_377B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37E3")

    ChrTalk(
        0x103,
        (
            "#020FWhoops! This isn't the way\x01",
            "to the Royal Keep!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FRight! To the north-west!\x02",
    )

    CloseMessageWindow()

    label("loc_37E3")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_13_36C6 end

    def Function_14_37FF(): pass

    label("Function_14_37FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_380C")
    Return()

    label("loc_380C")

    EventBegin(0x0)
    OP_A2(0x664)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, -870, 19750, 107400, 180)
    SetChrPos(0x9, 910, 19750, 107400, 180)
    Fade(1000)
    SetChrPos(0x101, 100, 17250, 98400, 0)
    SetChrPos(0x103, -1300, 17000, 97610, 0)
    SetChrPos(0x105, 1670, 17000, 97720, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x105, 9)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x103, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    OP_6D(290, 18000, 103070, 0)

    ChrTalk(
        0x8,
        "H-Here they come...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You shall not pass!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040FBut we must...and we WILL!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FCome on!\x01",
            "Just try and stop us!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_392B():
        OP_6D(2650, 14000, 77790, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_392B)

    def lambda_3943():
        OP_8E(0xFE, 0xFFFFFECA, 0x4B32, 0x1F676, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3943)

    def lambda_395E():
        OP_8E(0xFE, 0xFFFFFECA, 0x4B32, 0x1F676, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_395E)

    def lambda_3979():
        OP_8E(0xFE, 0xFFFFFECA, 0x4B32, 0x1F676, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3979)
    Sleep(500)
    Battle(0x3A9, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_39AC"),
        (SWITCH_DEFAULT, "loc_39AF"),
    )


    label("loc_39AC")

    OP_B4(0x0)
    Return()

    label("loc_39AF")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrPos(0x8, -2290, 19000, 105820, 236)
    SetChrPos(0x9, 2930, 18000, 103750, 112)
    SetChrPos(0x101, -10, 18000, 103540, 351)
    SetChrPos(0x103, -1250, 18000, 101680, 4)
    SetChrPos(0x105, 1290, 18000, 101820, 5)
    Sleep(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)
    EventEnd(0x0)
    Return()

    # Function_14_37FF end

    def Function_15_3A35(): pass

    label("Function_15_3A35")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_6D(30, 12000, 67150, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, -6690, 12000, 53510, 0)
    SetChrPos(0x102, -6380, 12000, 54650, 0)
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
    SetChrPos(0x14, -7210, 12000, 58180, 0)
    SetChrPos(0x15, -9680, 12000, 54680, 0)
    SetChrPos(0x16, -7920, 12000, 56380, 0)
    SetChrPos(0x17, -10390, 12000, 56310, 0)
    SetChrPos(0x18, 6170, 12000, 53150, 0)
    SetChrPos(0x19, 6210, 12000, 53870, 0)
    SetChrPos(0x1A, -7990, 12000, 54100, 0)
    SetChrPos(0x1B, -10220, 12000, 52510, 0)
    SetChrPos(0x1C, -6470, 12000, 48980, 0)
    SetChrPos(0x1D, -1110, 12000, 70820, 0)
    SetChrPos(0x1E, 1020, 12000, 70710, 0)
    SetChrPos(0x1F, 10, 12000, 71740, 0)
    SetChrPos(0x20, 20, 12000, 67080, 0)
    SetChrPos(0x13, 650, 12000, 67820, 0)
    SetChrPos(0x21, 6760, 12000, 57310, 0)
    SetChrPos(0x22, 5980, 12000, 57880, 0)
    SetChrPos(0x23, 7530, 12000, 55190, 0)
    SetChrPos(0x24, 6470, 12000, 55570, 0)
    SetChrPos(0x25, 9010, 12000, 57270, 0)
    SetChrPos(0x26, 9250, 12000, 55950, 0)
    SetChrPos(0x27, -4290, 14000, 77250, 180)
    SetChrPos(0x28, 4190, 14000, 77300, 180)
    SetChrPos(0x29, -4270, 12000, 70900, 180)
    SetChrPos(0x2A, 4210, 12000, 70900, 180)

    def lambda_3CC7():
        OP_8E(0xFE, 0xFFFFFBAA, 0x2EE0, 0xD23C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3CC7)

    def lambda_3CE2():
        OP_8E(0xFE, 0x3FC, 0x2EE0, 0xD1CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3CE2)

    def lambda_3CFD():
        OP_8E(0xFE, 0xA, 0x2EE0, 0xD5D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3CFD)

    def lambda_3D18():
        OP_8E(0xFE, 0x14, 0x2EE0, 0xC3A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3D18)

    def lambda_3D33():
        OP_8E(0xFE, 0x28A, 0x2EE0, 0xC684, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3D33)

    def lambda_3D4E():

        label("loc_3D4E")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3D4E")

    QueueWorkItem2(0x101, 1, lambda_3D4E)

    def lambda_3D5F():

        label("loc_3D5F")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3D5F")

    QueueWorkItem2(0x102, 1, lambda_3D5F)

    def lambda_3D70():

        label("loc_3D70")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3D70")

    QueueWorkItem2(0x14, 1, lambda_3D70)

    def lambda_3D81():

        label("loc_3D81")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3D81")

    QueueWorkItem2(0x15, 1, lambda_3D81)

    def lambda_3D92():

        label("loc_3D92")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3D92")

    QueueWorkItem2(0x16, 1, lambda_3D92)

    def lambda_3DA3():

        label("loc_3DA3")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3DA3")

    QueueWorkItem2(0x17, 1, lambda_3DA3)

    def lambda_3DB4():

        label("loc_3DB4")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3DB4")

    QueueWorkItem2(0x18, 1, lambda_3DB4)

    def lambda_3DC5():

        label("loc_3DC5")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3DC5")

    QueueWorkItem2(0x19, 1, lambda_3DC5)

    def lambda_3DD6():

        label("loc_3DD6")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3DD6")

    QueueWorkItem2(0x1A, 1, lambda_3DD6)

    def lambda_3DE7():

        label("loc_3DE7")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3DE7")

    QueueWorkItem2(0x1B, 1, lambda_3DE7)

    def lambda_3DF8():

        label("loc_3DF8")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3DF8")

    QueueWorkItem2(0x1C, 1, lambda_3DF8)

    def lambda_3E09():

        label("loc_3E09")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3E09")

    QueueWorkItem2(0x21, 1, lambda_3E09)

    def lambda_3E1A():

        label("loc_3E1A")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3E1A")

    QueueWorkItem2(0x22, 1, lambda_3E1A)

    def lambda_3E2B():

        label("loc_3E2B")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3E2B")

    QueueWorkItem2(0x23, 1, lambda_3E2B)

    def lambda_3E3C():

        label("loc_3E3C")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3E3C")

    QueueWorkItem2(0x24, 1, lambda_3E3C)

    def lambda_3E4D():

        label("loc_3E4D")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3E4D")

    QueueWorkItem2(0x25, 1, lambda_3E4D)

    def lambda_3E5E():

        label("loc_3E5E")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3E5E")

    QueueWorkItem2(0x26, 1, lambda_3E5E)

    def lambda_3E6F():
        OP_6D(-1510, 12000, 54280, 9000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3E6F)

    def lambda_3E87():
        OP_6E(342, 9000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3E87)
    WaitChrThread(0x0, 0x2)
    Sleep(1000)

    def lambda_3EA1():
        OP_6D(0, 12000, 47170, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3EA1)
    OP_8E(0x20, 0x1E, 0x2EE0, 0xB87E, 0x3E8, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_3A35 end

    def Function_16_3EDF(): pass

    label("Function_16_3EDF")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    OP_6D(-670, 4500, 47060, 0)
    OP_67(0, 2670, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(338000, 0)
    OP_6E(538, 0)

    def lambda_3F37():
        OP_67(0, 6660, -10000, 16000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F37)

    def lambda_3F4F():
        OP_6B(5000, 16000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F4F)

    def lambda_3F5F():
        OP_6D(390, 14500, 76830, 16000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F5F)
    Sleep(2000)

    def lambda_3F7C():
        OP_6C(50000, 14000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F7C)
    Sleep(10000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4261   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3EDF end

    def Function_17_3FA8(): pass

    label("Function_17_3FA8")

    OP_1F(0x64, 0xC8)
    Return()

    # Function_17_3FA8 end

    def Function_18_3FAF(): pass

    label("Function_18_3FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FB8")
    Return()

    label("loc_3FB8")

    EventBegin(0x0)
    SetChrFlags(0x2D, 0x40)
    SetChrChipByIndex(0x2D, 32)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2D, -42970, 16000, 81320, 270)
    SetChrFlags(0x2D, 0x4)

    def lambda_3FE5():

        label("loc_3FE5")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_3FE5")

    QueueWorkItem2(0x2D, 1, lambda_3FE5)
    Fade(1000)
    OP_6D(-47380, 16000, 81820, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(1470, 0)
    OP_6C(45000, 0)
    OP_6E(532, 0)

    def lambda_403A():
        OP_6D(-44280, 16000, 81720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_403A)
    WaitChrThread(0x101, 0x2)
    OP_20(0x7D0)
    OP_21()
    OP_44(0x2D, 0xFF)
    Sleep(1000)
    SetChrPos(0x101, -34850, 16000, 75130, 0)

    def lambda_4077():
        OP_6D(-42280, 16000, 81720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4077)

    def lambda_408F():
        OP_8E(0xFE, 0xFFFF5EAC, 0x3E80, 0x13C68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_408F)
    Sleep(2000)
    OP_51(0x2D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2D, 33)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x2D, 400)
    Sleep(500)
    TurnDirection(0x2D, 0x101, 400)
    Sleep(500)

    ChrTalk(
        0x2D,
        (
            "#011F...Hey, Estelle.\x02\x03",
            "Nice night, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FYeah...\x02\x03",
            "There's that song again.\x02\x03",
            "'The Whereabouts of Light.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#015FI've lost a lot...\x02\x03",
            "But this song, and this harmonica,\x01",
            "have always been with me.\x02\x03",
            "I've been thinking about\x01",
            "why I play it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#010FMaybe it's a habit I should quit.\x02\x03",
            "I think I want to tell you...\x02\x03",
            "...what I was doing before\x01",
            "I met you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FJoshua...\x02\x03",
            "#002FOkay...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x2D,
        (
            "#013FThis may take a while...\x01",
            "Do you mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FNot at all. I'll listen to\x01",
            "whatever you have to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#019FThank you...\x02\x03",
            "#011F...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x2D, 0xFF)

    def lambda_4317():
        OP_6C(86000, 3000)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_4317)
    Sleep(1500)
    OP_8C(0x2D, 270, 400)
    ClearChrFlags(0x2D, 0x1)
    OP_8E(0x2D, 0xFFFF5600, 0x3E1C, 0x13DDA, 0x320, 0x0)
    SetChrChipByIndex(0x2D, 39)
    SetChrFlags(0x2D, 0x2)
    SetChrSubChip(0x2D, 8)
    WaitChrThread(0x2D, 0x1)
    OP_99(0x2D, 0x8, 0xA, 0x320)
    OP_1D(0x5B)
    Sleep(1000)

    ChrTalk(
        0x2D,
        (
            "#015FOnce upon a time...\x02\x03",
            "There lived a little boy,\x01",
            "all by himself.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Joshua")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "He was the timid sort, relying on the kindness of others, without a single\x01",
            "redeeming trait.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "But he had people he cared about with him, so he was happy.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x4002F, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Joshua")

    AnonymousTalk(
        "But one day, something happened that broke his heart.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "He forgot how to speak...to feel...even to eat. All he could do was play his\x01",
            "harmonica.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "No matter how hard his caretaker tried, nothing helped his heart to mend,\x01",
            "and he grew weaker by the day.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_AD(0x40030, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetChrName("Joshua")

    AnonymousTalk(
        "One day, a wandering magician appeared before the boy.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "'I will heal the boy's heart for you,' he said.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "'Provided, of course, I am compensated.'\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "And so, the boy was given over into the magician's care.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    SetChrName("Joshua")

    AnonymousTalk(
        "As he attempted to piece the broken heart back together...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "...the magician found that he could shape the boy's existence into anything\x01",
            "he wished.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "And so, the boy's new heart...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "...became that of a murderer.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x40031, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetChrName("Joshua")

    AnonymousTalk(
        "For two years, the boy killed every single day.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "Under cover of night, he murdered dozens of soldiers.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "He slit the throat of a national cabinet minister, who was under heavily \x01",
            "armed guard.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "Sometimes, he used explosives, which maimed and killed innocent bystanders.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "At some point, he became regarded as something more than a mere killer...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "He was known as the 'Black Fang,' and the name struck fear into the hearts\x01",
            "of men.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    SetChrName("Joshua")

    AnonymousTalk(
        "One day, the magician gave the boy an assassination order.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x40032, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetChrName("Joshua")

    AnonymousTalk(
        (
            "His target was a hero: a man who had protected his queen and nation from\x01",
            "the threat of an invading northern country.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "He was a bracer who held a special rank shared only by three others in\x01",
            "in the entire land.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "But the target was too strong.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "He defeated the boy with all the ease of a tiger swatting at a playful cub.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    SetChrName("Joshua")

    AnonymousTalk(
        "At that moment, some of the magician's servants showed up.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "Since the boy's face had been seen, he was now a loose end to be tied up.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "But someone came to his aid and drove the attackers away.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x40033, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetChrName("Joshua")

    AnonymousTalk(
        "It was, of course, the man he had come to kill.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "And so, the boy...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "...The boy was taken to the man's house, where he met a young girl...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x64)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    Sleep(500)

    ChrTalk(
        0x2D,
        (
            "#015FHe lived there for five years,\x01",
            "always feeling like he was lost\x01",
            "in some wonderful dream.\x02\x03",
            "In the real world he would never\x01",
            "be allowed to have such dreams...\x02\x03",
            "But all dreams must end\x01",
            "at some point.\x02\x03",
            "The time was drawing near, when\x01",
            "reality could be avoided no longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x2D, 0xA, 0x8, 0x320)
    Sleep(500)
    Fade(500)
    SetChrPos(0x2D, -43500, 16000, 81370, 270)
    SetChrChipByIndex(0x2D, 33)
    ClearChrFlags(0x2D, 0x2)
    SetChrSubChip(0x2D, 0)
    OP_0D()

    def lambda_4DFE():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_4DFE)
    Sleep(1000)
    TurnDirection(0x2D, 0x101, 400)
    WaitChrThread(0x2D, 0x1)

    ChrTalk(
        0x2D,
        (
            "#011FAnd that's...the end of my story.\x02\x03",
            "Thank you for being patient\x01",
            "with me and listening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F...\x02\x03",
            "#506F...Umm...ha ha...\x02\x03",
            "Was all that...real?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#015FEvery syllable.\x02\x03",
            "My heart is broken.\x02\x03",
            "My hands will always be\x01",
            "stained with blood.\x02\x03",
            "I failed in the assassination\x01",
            "of your father.\x02\x03",
            "#013FI've been betraying you\x01",
            "for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#590FThe boy can't be saved from\x01",
            "his real purpose.\x02\x03",
            "His presence alone seems to\x01",
            "bring disaster and misery...\x02\x03",
            "He's just...tainted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#011FBut the boy set out on a journey...\x02\x03",
            "...in hopes that he may keep his misfortunes\x01",
            "from the ones he holds dear.\x02\x03",
            "He will find and stop the foul magician who\x01",
            "created the life he has led.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x2D, 0x2)
    SetChrFlags(0x2D, 0x1000)
    SetChrChipByIndex(0x2D, 40)

    def lambda_50EA():

        label("loc_50EA")

        OP_99(0xFE, 0x0, 0x7, 0x4B0)
        OP_48()
        Jump("loc_50EA")

    QueueWorkItem2(0x2D, 1, lambda_50EA)

    def lambda_50FD():
        OP_8F(0xFE, 0xFFFF5C0E, 0x3E80, 0x13C68, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_50FD)
    Sleep(500)
    SetChrFlags(0x2D, 0x1)
    WaitChrThread(0x2D, 0x2)
    OP_22(0x8F, 0x0, 0x50)
    OP_44(0x2D, 0x1)
    ClearChrFlags(0x2D, 0x1000)
    ClearChrFlags(0x2D, 0x2)
    SetChrChipByIndex(0x2D, 33)
    SetChrSubChip(0x2D, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 42)
    SetChrFlags(0x101, 0x2)
    Sleep(500)

    def lambda_5158():
        OP_8F(0xFE, 0xFFFF56DC, 0x3E80, 0x13C68, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_5158)
    Sleep(1000)
    ClearChrFlags(0x2D, 0x1)
    WaitChrThread(0x2D, 0x2)
    SetChrSubChip(0x101, 30)
    Sleep(100)
    SetChrSubChip(0x101, 31)
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#580FWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#011FThat's the last remnant of\x01",
            "my human heart...\x02\x03",
            "I won't be needing it any more...\x02\x03",
            "But I want you to take it.\x02\x03",
            "#019FIt's hardly an adequate way\x01",
            "to thank you for the last\x01",
            "five years...\x02\x03",
            "...yet I can't think of anything better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F...\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x0, 0x2, 0x320)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        "#582F...op it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#014FWha...?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 43)

    def lambda_52F1():

        label("loc_52F1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_52F1")

    QueueWorkItem2(0x101, 1, lambda_52F1)
    SetChrFlags(0x101, 0x1000)
    OP_8F(0x101, 0xFFFF5AC4, 0x3E80, 0x13C68, 0xBB8, 0x0)
    OP_44(0x101, 0x1)
    SetChrSubChip(0x101, 0)

    ChrTalk(
        0x101,
        "#005F#3S#4PI said, STOP IT.\x02",
    )

    SetChrChipByIndex(0x101, 42)
    OP_99(0x101, 0x3, 0x4, 0x3E8)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#003F#4PStop talking about it like\x01",
            "it's a dream...!\x02\x03",
            "You make it sound like nothing that's\x01",
            "happened was even real to you!\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x12, 0x14, 0x320)
    OP_99(0x101, 0x13, 0x12, 0x320)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#508F#4PWhat difference does the\x01",
            "past make?!\x02\x03",
            "Your heart is broken? What\x01",
            "does that even MEAN?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#013FEstelle...\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x6, 0x8, 0x320)
    OP_99(0x101, 0x7, 0x6, 0x320)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#005F#4PLook at me!\x02\x03",
            "Look into my eyes!\x02\x03",
            "#003FThey've ALWAYS seen that boy!\x02\x03",
            "In good times and bad!\x02\x03",
            "No matter how much the boy was\x01",
            "hurting...I always saw how hard\x01",
            "he'd keep holding on!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        "#504F#4P#3SJoshua...I love you!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#014F!!!\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x9, 0x10, 0x5DC)

    def lambda_55A2():

        label("loc_55A2")

        OP_99(0xFE, 0xE, 0x10, 0x320)
        OP_48()
        Jump("loc_55A2")

    QueueWorkItem2(0x101, 1, lambda_55A2)

    ChrTalk(
        0x101,
        (
            "#583F#4PYou can't just leave me\x01",
            "on my own!\x02\x03",
            "My feelings won't just go\x01",
            "away when you do!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    SetChrSubChip(0x101, 17)
    Sleep(50)
    SetChrSubChip(0x101, 18)
    Sleep(150)
    SetChrSubChip(0x101, 19)
    Sleep(50)
    SetChrSubChip(0x101, 20)
    Sleep(50)
    SetChrSubChip(0x101, 18)

    ChrTalk(
        0x101,
        "#583F#3S#4PI won't let you!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#012FEstelle...\x02\x03",
            "#015F...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5694():
        OP_6D(-41780, 16000, 81720, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5694)
    OP_99(0x101, 0x15, 0x18, 0x4B0)

    def lambda_56B5():
        OP_8E(0xFE, 0xFFFF58E4, 0x3E80, 0x13C68, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_56B5)
    Sleep(500)
    SetChrFlags(0x2D, 0x1)
    WaitChrThread(0x2D, 0x2)
    Fade(500)
    OP_20(0x7D0)
    SetChrPos(0x2D, -42300, 16000, 81000, 90)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x2D, 0x2)
    SetChrChipByIndex(0x2D, 41)
    SetChrSubChip(0x2D, 0)
    OP_0D()
    OP_99(0x2D, 0x0, 0x2, 0x708)
    Sleep(500)

    ChrTalk(
        0x101,
        "#004F#4PHuh...?\x02",
    )

    OP_99(0x2D, 0x3, 0x4, 0x5DC)
    CloseMessageWindow()
    OP_21()
    OP_1D(0x50)
    Sleep(1000)
    Fade(1000)

    def lambda_5748():
        OP_6B(1300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5748)
    SetChrSubChip(0x2D, 5)
    Sleep(500)

    ChrTalk(
        0x101,
        "#2P...Oh...\x02",
    )

    CloseMessageWindow()
    OP_99(0x2D, 0x5, 0x6, 0x320)
    Sleep(500)

    ChrTalk(
        0x101,
        "#2P(J-Joshua...)\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    SetChrSubChip(0x2D, 5)
    Sleep(500)
    ClearChrFlags(0x101, 0x80)
    SetChrChipByIndex(0x101, 42)
    SetChrSubChip(0x101, 26)
    SetChrPos(0x101, -42000, 16000, 81000, 270)
    ClearChrFlags(0x2D, 0x2)
    SetChrPos(0x2D, -42780, 16000, 81000, 90)
    SetChrChipByIndex(0x2D, 33)
    SetChrSubChip(0x2D, 0)

    def lambda_5802():
        OP_6B(1500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5802)
    OP_22(0xA4, 0x0, 0x64)
    OP_96(0x101, 0xFFFF5F10, 0x3E80, 0x13C68, 0x12C, 0x1388)
    OP_96(0x101, 0xFFFF60A0, 0x3E80, 0x13C68, 0x64, 0xFA0)
    OP_99(0x101, 0x1A, 0x1D, 0x4B0)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    SetChrSubChip(0x101, 25)
    OP_0D()

    def lambda_585E():
        OP_6C(55000, 60000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_585E)

    def lambda_586E():
        OP_6B(1300, 60000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_586E)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#580F#4PWhat was that...?!\x02\x03",
            "It's so bitter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#591F...It's just a fast-acting sedative.\x02\x03",
            "Don't worry...\x01",
            "There are no side effects.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    Sleep(250)
    FadeToBright(250, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#584F#4POh...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 44)
    OP_22(0xD1, 0x0, 0x50)
    OP_99(0x101, 0x0, 0x3, 0x3E8)
    Sleep(1000)
    OP_99(0x101, 0x3, 0x5, 0x320)

    ChrTalk(
        0x101,
        "#584F#4PWh... Why...?\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x5, 0x7, 0x320)

    ChrTalk(
        0x101,
        "#584F#4PWhy did you...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x2D,
        (
            "#594FMy Estelle...\x01",
            "You shine like the sun.\x02\x03",
            "My time with you was the happiest...and\x01",
            "the most painful...I've ever known.\x02\x03",
            "Just as the brightest light\x01",
            "casts the darkest shadow...\x02\x03",
            "If you stayed with me, you'd\x01",
            "find out just how disgusting\x01",
            "my true nature is...\x02\x03",
            "Sometimes, I think it would have been\x01",
            "better if we'd never met...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x7, 0x9, 0x320)
    Sleep(400)

    ChrTalk(
        0x101,
        "#585F#4PNo...\x02",
    )

    CloseMessageWindow()

    def lambda_5B11():
        OP_6D(-41280, 16000, 81720, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B11)
    OP_8F(0x2D, 0xFFFF5BF0, 0x3E80, 0x13CCC, 0x3E8, 0x0)
    SetChrChipByIndex(0x2D, 45)
    SetChrFlags(0x2D, 0x2)
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_99(0x2D, 0x0, 0x2, 0x4B0)
    Sleep(800)

    ChrTalk(
        0x2D,
        (
            "#592F#6PBut this time is different.\x02\x03",
            "I'm grateful that you came to see me.\x02\x03",
            "I hate that I have to run from\x01",
            "a girl who's so important to me,\x01",
            "but it's all I can do...\x02\x03",
            "But I want you to know that I'll\x01",
            "always be thinking of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x9, 0xB, 0x320)

    ChrTalk(
        0x101,
        "#585F#4PJoshua... Joshua...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x2D,
        (
            "#593F#6PThank you...for everything.\x02\x03",
            "You had me from the first moment\x01",
            "I met you. I've always loved you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_99(0x2D, 0x2, 0x5, 0x4B0)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Goodbye, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0xFA0)
    OP_21()
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_6D(-89960, 14000, -12180, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(0, 0)
    OP_0D()
    OP_21()
    PlayMovie(0x0, "ed6_dt17.dat")

    label("loc_5D89")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F1C")
    Sleep(10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_5F19")
    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "")
    Sleep(500)
    OP_83(0x15, 0x0)
    OP_AD(0x4003A, 0x0, 0x0, 0xC8)
    Sleep(2000)
    OP_56(0x3)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "              - Regarding Clear Data -\x01",
            "After saving Clear Data, you may load it from\x01",
            "the title screen to begin a second play through\x01",
            "with various statistics carried over.\x02",
        )
    )


    Menu(
        0,
        170,
        100,
        0,
        (
            "[Save Clear Data]\x01",      # 0
            "[Cancel]\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ECB")
    OP_DE()

    label("loc_5ECB")

    Sleep(1000)
    OP_AE(0x1F4)
    FadeToBright(0, 0)
    PlayMovie(0x0, "ed6_dt18.dat")

    label("loc_5EED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F19")
    Sleep(10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_5F16")
    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "")
    Sleep(1500)
    OP_B4(0x1)

    label("loc_5F16")

    Jump("loc_5EED")

    label("loc_5F19")

    Jump("loc_5D89")

    label("loc_5F1C")

    Return()

    # Function_18_3FAF end

    def Function_19_5F1D(): pass

    label("Function_19_5F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FC5")
    EventBegin(0x1)

    ChrTalk(
        0x8,
        (
            "Hello, Hilda.\x01",
            "You need something else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We're keeping watch over Her Majesty.\x01",
            "You've nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_604E")

    label("loc_5FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_604E")
    EventBegin(0x1)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        (
            "The area around the Royal Keep\x01",
            "is off limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "No one is to be admitted.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8C(0x8, 180, 0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_604E")

    Return()

    # Function_19_5F1D end

    SaveToFile()

Try(main)
