from ED6ScenarioHelper import *

def main():
    # 艾利兹街道

    CreateScenaFile(
        FileName            = 'T0100   ._SN',
        MapName             = 'rolent',
        Location            = 'T0100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0100   ._SN',
            'ED6_DT01/T0100_1 ._SN',
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
        'Aina',                                 # 9
        'Luke',                                 # 10
        'Pat',                                  # 11
        'Claire',                               # 12
        'Freemont',                             # 13
        'Ellie',                                # 14
        'Armand',                               # 15
        'Ellie',                                # 16
        'Armand',                               # 17
        'Yuni',                                 # 18
        'Charles',                              # 19
        'Radmira',                              # 20
        'Ida',                                  # 21
        'Aryll',                                # 22
        'Aryll',                                # 23
        'Professor Alba',                       # 24
        'Nial',                                 # 25
        'Dorothy',                              # 26
        'Scherazard',                           # 27
        'Target Camera',                        # 28
        'Pigeon',                               # 29
        'Pigeon',                               # 30
        'Pigeon',                               # 31
        'Pigeon',                               # 32
        'Pigeon',                               # 33
        "Rolent - Mayor's Residence",           # 34
        'Rolent Landing Port',                  # 35
        'Elize Highway',                        # 36
        'Milch Main Road',                      # 37
        'Malga Trail',                          # 38
    )

    DeclEntryPoint(
        Unknown_00              = 49000,
        Unknown_04              = 0,
        Unknown_08              = 41000,
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
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 49000,
        Unknown_04              = 0,
        Unknown_08              = 41000,
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
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 49000,
        Unknown_04              = 0,
        Unknown_08              = 41000,
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
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01160 ._CH',             # 00
        'ED6_DT07/CH01060 ._CH',             # 01
        'ED6_DT07/CH02560 ._CH',             # 02
        'ED6_DT07/CH01070 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
        'ED6_DT07/CH01170 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT07/CH02640 ._CH',             # 08
        'ED6_DT07/CH01690 ._CH',             # 09
        'ED6_DT07/CH02050 ._CH',             # 0A
        'ED6_DT07/CH02060 ._CH',             # 0B
        'ED6_DT07/CH02070 ._CH',             # 0C
        'ED6_DT07/CH01030 ._CH',             # 0D
        'ED6_DT07/CH01700 ._CH',             # 0E
        'ED6_DT07/CH01700 ._CH',             # 0F
        'ED6_DT07/CH00020 ._CH',             # 10
        'ED6_DT07/CH01153 ._CH',             # 11
        'ED6_DT07/CH01143 ._CH',             # 12
        'ED6_DT07/CH01030 ._CH',             # 13
        'ED6_DT07/CH01033 ._CH',             # 14
        'ED6_DT07/CH01730 ._CH',             # 15
        'ED6_DT07/CH01731 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT07/CH01160P._CP',             # 00
        'ED6_DT07/CH01060P._CP',             # 01
        'ED6_DT07/CH02560P._CP',             # 02
        'ED6_DT07/CH01070P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
        'ED6_DT07/CH01170P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT07/CH02640P._CP',             # 08
        'ED6_DT07/CH01690P._CP',             # 09
        'ED6_DT07/CH02050P._CP',             # 0A
        'ED6_DT07/CH02060P._CP',             # 0B
        'ED6_DT07/CH02070P._CP',             # 0C
        'ED6_DT07/CH01030P._CP',             # 0D
        'ED6_DT07/CH01700P._CP',             # 0E
        'ED6_DT07/CH01700P._CP',             # 0F
        'ED6_DT07/CH00020P._CP',             # 10
        'ED6_DT07/CH01153P._CP',             # 11
        'ED6_DT07/CH01143P._CP',             # 12
        'ED6_DT07/CH01030P._CP',             # 13
        'ED6_DT07/CH01033P._CP',             # 14
        'ED6_DT07/CH01730P._CP',             # 15
        'ED6_DT07/CH01731P._CP',             # 16
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 49900,
        Z                   = 0,
        Y                   = 72100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 46900,
        Z                   = 0,
        Y                   = 74100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 30422,
        Z                   = 0,
        Y                   = 40087,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 51829,
        Z                   = 0,
        Y                   = 35208,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 29979,
        Z                   = 0,
        Y                   = 17921,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 31832,
        Z                   = 3250,
        Y                   = 33000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 36305,
        Z                   = 100,
        Y                   = 46015,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 39160,
        Z                   = 80,
        Y                   = 47020,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x12,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 72160,
        Z                   = 0,
        Y                   = 18851,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 62400,
        Z                   = 250,
        Y                   = 22000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 33500,
        Z                   = 0,
        Y                   = 45800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 39420,
        Z                   = 250,
        Y                   = 51560,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x115,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 38700,
        Z                   = 0,
        Y                   = 50720,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 200,
        Z                   = 0,
        Y                   = 74200,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 90860,
        Z                   = 0,
        Y                   = 40240,
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
        X                   = 49150,
        Z                   = 0,
        Y                   = 95090,
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
        X                   = 48960,
        Z                   = 0,
        Y                   = 1120,
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
        X                   = 5400,
        Z                   = 0,
        Y                   = 39830,
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
        X                   = 28060,
        Z                   = 0,
        Y                   = 80870,
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
        X                   = 44000,
        Y                   = 0,
        Z                   = 12250,
        Range               = 54000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x2710,
        Unknown_18          = 0x0,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = 18000,
        Y                   = 0,
        Z                   = 44000,
        Range               = 19000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x9088,
        Unknown_18          = 0x0,
        Unknown_1C          = 55,
    )

    DeclEvent(
        X                   = 25000,
        Y                   = 0,
        Z                   = 72000,
        Range               = 31000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x11364,
        Unknown_18          = 0x0,
        Unknown_1C          = 64,
    )

    DeclEvent(
        X                   = 55000,
        Y                   = -1000,
        Z                   = 57200,
        Range               = 61500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xDB88,
        Unknown_18          = 0x10000,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 42000,
        Y                   = -1000,
        Z                   = 34400,
        Range               = 54000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x8278,
        Unknown_18          = 0x10000,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 60900,
        Y                   = -1000,
        Z                   = 35800,
        Range               = 61900,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xAFC8,
        Unknown_18          = 0x10000,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 61850,
        Y                   = -1000,
        Z                   = 30150,
        Range               = 66550,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7DC8,
        Unknown_18          = 0x10000,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 18950,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 77,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 29050,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 78,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 33020,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 79,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 21990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 80,
    )

    DeclEvent(
        X                   = 30900,
        Y                   = 0,
        Z                   = 47270,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 81,
    )

    DeclEvent(
        X                   = 34300,
        Y                   = 0,
        Z                   = 52980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 81,
    )

    DeclEvent(
        X                   = 66000,
        Y                   = 0,
        Z                   = 52470,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 82,
    )

    DeclEvent(
        X                   = 73000,
        Y                   = 0,
        Z                   = 34550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 83,
    )

    DeclEvent(
        X                   = 54800,
        Y                   = 0,
        Z                   = 49170,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 84,
    )


    DeclActor(
        TriggerX            = 55000,
        TriggerZ            = 0,
        TriggerY            = 45300,
        TriggerRange        = 1700,
        ActorX              = 55000,
        ActorZ              = 2500,
        ActorY              = 45300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45000,
        TriggerZ            = 0,
        TriggerY            = 25400,
        TriggerRange        = 500,
        ActorX              = 45000,
        ActorZ              = 0,
        ActorY              = 25400,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 76980,
        TriggerZ            = 0,
        TriggerY            = 19020,
        TriggerRange        = 800,
        ActorX              = 76980,
        ActorZ              = 0,
        ActorY              = 19020,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 44710,
        TriggerZ            = 0,
        TriggerY            = 70740,
        TriggerRange        = 1500,
        ActorX              = 44710,
        ActorZ              = 1800,
        ActorY              = 70740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 75,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45280,
        TriggerZ            = 0,
        TriggerY            = 71310,
        TriggerRange        = 1500,
        ActorX              = 45280,
        ActorZ              = 1800,
        ActorY              = 71310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 76,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_85E",          # 00, 0
        "Function_1_D0E",          # 01, 1
        "Function_2_E63",          # 02, 2
        "Function_3_FE0",          # 03, 3
        "Function_4_1119",         # 04, 4
        "Function_5_1252",         # 05, 5
        "Function_6_1276",         # 06, 6
        "Function_7_12F4",         # 07, 7
        "Function_8_1338",         # 08, 8
        "Function_9_1383",         # 09, 9
        "Function_10_13B3",        # 0A, 10
        "Function_11_15B6",        # 0B, 11
        "Function_12_172B",        # 0C, 12
        "Function_13_1F6D",        # 0D, 13
        "Function_14_23CE",        # 0E, 14
        "Function_15_433F",        # 0F, 15
        "Function_16_4BA1",        # 10, 16
        "Function_17_4D90",        # 11, 17
        "Function_18_5096",        # 12, 18
        "Function_19_5436",        # 13, 19
        "Function_20_5985",        # 14, 20
        "Function_21_614C",        # 15, 21
        "Function_22_67BD",        # 16, 22
        "Function_23_67CC",        # 17, 23
        "Function_24_67DB",        # 18, 24
        "Function_25_67EA",        # 19, 25
        "Function_26_6814",        # 1A, 26
        "Function_27_6DB3",        # 1B, 27
        "Function_28_7C20",        # 1C, 28
        "Function_29_8626",        # 1D, 29
        "Function_30_8647",        # 1E, 30
        "Function_31_8671",        # 1F, 31
        "Function_32_867B",        # 20, 32
        "Function_33_8685",        # 21, 33
        "Function_34_89D2",        # 22, 34
        "Function_35_89F2",        # 23, 35
        "Function_36_8A12",        # 24, 36
        "Function_37_8A19",        # 25, 37
        "Function_38_968C",        # 26, 38
        "Function_39_96EE",        # 27, 39
        "Function_40_973E",        # 28, 40
        "Function_41_9826",        # 29, 41
        "Function_42_98DC",        # 2A, 42
        "Function_43_98F4",        # 2B, 43
        "Function_44_9988",        # 2C, 44
        "Function_45_A2E4",        # 2D, 45
        "Function_46_A323",        # 2E, 46
        "Function_47_A362",        # 2F, 47
        "Function_48_A3AF",        # 30, 48
        "Function_49_A3B6",        # 31, 49
        "Function_50_A4A7",        # 32, 50
        "Function_51_A563",        # 33, 51
        "Function_52_A617",        # 34, 52
        "Function_53_A6D1",        # 35, 53
        "Function_54_A7AE",        # 36, 54
        "Function_55_A9E7",        # 37, 55
        "Function_56_AA83",        # 38, 56
        "Function_57_AD9A",        # 39, 57
        "Function_58_AE9F",        # 3A, 58
        "Function_59_AF9E",        # 3B, 59
        "Function_60_B0A2",        # 3C, 60
        "Function_61_B189",        # 3D, 61
        "Function_62_B242",        # 3E, 62
        "Function_63_B318",        # 3F, 63
        "Function_64_B551",        # 40, 64
        "Function_65_B5D6",        # 41, 65
        "Function_66_B856",        # 42, 66
        "Function_67_B95B",        # 43, 67
        "Function_68_BA5A",        # 44, 68
        "Function_69_BB94",        # 45, 69
        "Function_70_BC46",        # 46, 70
        "Function_71_BE7F",        # 47, 71
        "Function_72_C2A0",        # 48, 72
        "Function_73_CC23",        # 49, 73
        "Function_74_CC3F",        # 4A, 74
        "Function_75_CC8D",        # 4B, 75
        "Function_76_CCD1",        # 4C, 76
        "Function_77_CD1E",        # 4D, 77
        "Function_78_CD22",        # 4E, 78
        "Function_79_CD26",        # 4F, 79
        "Function_80_CD2A",        # 50, 80
        "Function_81_CD2E",        # 51, 81
        "Function_82_CD32",        # 52, 82
        "Function_83_CD36",        # 53, 83
        "Function_84_CD3A",        # 54, 84
        "Function_85_CD3E",        # 55, 85
        "Function_86_CD42",        # 56, 86
        "Function_87_CD46",        # 57, 87
        "Function_88_CD4A",        # 58, 88
        "Function_89_CD4E",        # 59, 89
    )


    def Function_0_85E(): pass

    label("Function_0_85E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_886")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_8DA")

    label("loc_886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_8AE")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    Jump("loc_8DA")

    label("loc_8AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_8DA")
    SetChrPos(0xD, 32000, 0, 21020, 0)
    SetChrPos(0xE, 31990, 0, 22540, 180)
    Jump("loc_8DA")

    label("loc_8DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_909")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x9, 48900, 0, 48800, 0)
    Jump("loc_A64")

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_93F")
    SetChrPos(0x9, 68600, 0, 42100, 0)
    SetChrPos(0xA, 66000, 0, 40200, 225)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_A64")

    label("loc_93F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_975")
    SetChrPos(0x9, 48900, 0, 48800, 0)
    SetChrPos(0xA, 34900, 0, 38200, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_A64")

    label("loc_975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_9AB")
    SetChrPos(0x9, 70160, 0, 16850, 0)
    SetChrPos(0xA, 72160, 0, 18850, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_A64")

    label("loc_9AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_9E8")
    SetChrPos(0x9, 70160, 0, 16850, 90)
    SetChrPos(0xA, 71160, 0, 17850, 225)
    SetChrPos(0x11, 72160, 0, 18850, 0)
    Jump("loc_A64")

    label("loc_9E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_A33")
    SetChrPos(0x11, 45200, 0, 42700, 0)
    SetChrPos(0x9, 46900, 0, 74100, 0)
    OP_43(0x9, 0x0, 0x0, 0x4)
    SetChrPos(0xA, 49900, 0, 72100, 0)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_A64")

    label("loc_A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_END)), "loc_A64")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    OP_44(0x11, 0xFF)

    label("loc_A64")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6F")

    label("loc_A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A95")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    Jump("loc_B09")

    label("loc_A95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AB8")
    SetChrPos(0x12, 62400, 250, 22000, 270)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_B09")

    label("loc_AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_ADD")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 32150, 0, 28000, 45)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_B09")

    label("loc_ADD")

    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 45660, 0, 19400, 270)
    SetChrPos(0x12, 62400, 250, 22000, 270)

    label("loc_B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 0)), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B1A")
    Jump("loc_B70")

    label("loc_B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B51")
    SetChrPos(0x14, 36320, 0, 57180, 135)
    ClearChrFlags(0x14, 0x40)
    SetChrChipByIndex(0x14, 19)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    Jump("loc_B70")

    label("loc_B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B70")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    Jump("loc_B70")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_B7E")
    OP_A3(0x3FA)
    Event(0, 71)

    label("loc_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_B95")
    OP_A3(0x3FB)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 72)

    label("loc_B95")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_BB1"),
        (119, "loc_BE9"),
        (110, "loc_C5B"),
        (122, "loc_CCA"),
        (2, "loc_CE0"),
        (SWITCH_DEFAULT, "loc_D0D"),
    )


    label("loc_BB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD8")
    OP_28(0x9, 0x4, 0x10)
    Event(1, 35)
    Jump("loc_BE6")

    label("loc_BD8")

    ClearMapFlags(0x1)
    SetMapFlags(0x80)
    Event(1, 9)

    label("loc_BE6")

    Jump("loc_D0D")

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF7")
    Jump("loc_D0D")

    label("loc_BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C58")
    EventBegin(0x0)
    SetMapFlags(0x400000)
    SetChrPos(0x101, 48300, 0, 7432, 0)
    SetChrPos(0x102, 49500, 0, 6573, 0)
    OP_6D(49336, 0, 72554, 0)
    OP_6C(36000, 0)
    OP_6B(5000, 0)
    FadeToBright(500, 0)
    Event(0, 33)

    label("loc_C58")

    Jump("loc_D0D")

    label("loc_C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC7")
    ClearMapFlags(0x1)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrPos(0x9, 57890, 0, 14350, 0)
    SetChrPos(0xA, 57890, 0, 14350, 0)
    OP_6D(49800, 0, 18520, 0)
    OP_6C(33000, 0)
    FadeToBright(500, 0)
    Event(0, 37)

    label("loc_CC7")

    Jump("loc_D0D")

    label("loc_CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDD")
    OP_A2(0x264)
    Event(0, 21)

    label("loc_CDD")

    Jump("loc_D0D")

    label("loc_CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_CEE")
    Event(0, 28)
    Jump("loc_D0A")

    label("loc_CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_D01")
    SetChrFlags(0x11, 0x80)
    Event(0, 26)
    Jump("loc_D0A")

    label("loc_D01")

    SetChrFlags(0x11, 0x80)
    Event(0, 27)

    label("loc_D0A")

    Jump("loc_D0D")

    label("loc_D0D")

    Return()

    # Function_0_85E end

    def Function_1_D0E(): pass

    label("Function_1_D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D26")
    OP_B1("t0100_y")
    Jump("loc_D2F")

    label("loc_D26")

    OP_B1("t0100_n")

    label("loc_D2F")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEA840, 0x30001)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D5A")
    OP_64(0x1, 0x1)
    Jump("loc_D6C")

    label("loc_D5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6C")
    OP_64(0x1, 0x1)
    Jump("loc_D6C")

    label("loc_D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D78")
    OP_64(0x2, 0x1)

    label("loc_D78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_D9E")
    OP_6F(0x25, 90)
    OP_6F(0x27, 90)
    OP_6F(0x29, 90)
    OP_6F(0x2B, 90)
    Jump("loc_E62")

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC9")
    OP_6F(0x25, 100)
    OP_6F(0x27, 100)
    OP_6F(0x29, 100)
    OP_6F(0x2B, 100)
    Jump("loc_E62")

    label("loc_DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF4")
    OP_6F(0x25, 50)
    OP_6F(0x27, 50)
    OP_6F(0x29, 50)
    OP_6F(0x2B, 50)
    Jump("loc_E62")

    label("loc_DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E1F")
    OP_6F(0x25, 30)
    OP_6F(0x27, 30)
    OP_6F(0x29, 30)
    OP_6F(0x2B, 30)
    Jump("loc_E62")

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E46")
    OP_6F(0x25, 90)
    OP_6F(0x27, 90)
    OP_6F(0x29, 90)
    OP_6F(0x2B, 90)
    Jump("loc_E62")

    label("loc_E46")

    OP_6F(0x25, 30)
    OP_6F(0x27, 30)
    OP_6F(0x29, 30)
    OP_6F(0x2B, 30)

    label("loc_E62")

    Return()

    # Function_1_D0E end

    def Function_2_E63(): pass

    label("Function_2_E63")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E88")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_FCA")

    label("loc_E88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA1")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_FCA")

    label("loc_EA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_FCA")

    label("loc_EBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_FCA")

    label("loc_ED3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEC")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_FCA")

    label("loc_EEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F05")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_FCA")

    label("loc_F05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_FCA")

    label("loc_F1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F37")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_FCA")

    label("loc_F37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F50")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_FCA")

    label("loc_F50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F69")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_FCA")

    label("loc_F69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F82")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_FCA")

    label("loc_F82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_FCA")

    label("loc_F9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_FCA")

    label("loc_FB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_FCA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FDF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_FCA")

    label("loc_FDF")

    Return()

    # Function_2_E63 end

    def Function_3_FE0(): pass

    label("Function_3_FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_100D")

    label("loc_FE7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_100A")
    OP_8D(0xFE, 47400, 52400, 50900, 47700, 3000)
    Jump("loc_FE7")

    label("loc_100A")

    Jump("loc_1118")

    label("loc_100D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_103A")

    label("loc_1014")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1037")
    OP_8D(0xFE, 64500, 43600, 73600, 38500, 3000)
    Jump("loc_1014")

    label("loc_1037")

    Jump("loc_1118")

    label("loc_103A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1067")

    label("loc_1041")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1064")
    OP_8D(0xFE, 47400, 52400, 50900, 47700, 3000)
    Jump("loc_1041")

    label("loc_1064")

    Jump("loc_1118")

    label("loc_1067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1094")

    label("loc_106E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1091")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 4000)
    Jump("loc_106E")

    label("loc_1091")

    Jump("loc_1118")

    label("loc_1094")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1118")
    OP_8E(0xFE, 0xBF04, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0x115BC, 0x1770, 0x0)
    OP_8E(0xFE, 0xBF04, 0x0, 0x115BC, 0x1770, 0x0)
    Jump("loc_1094")

    label("loc_1118")

    Return()

    # Function_3_FE0 end

    def Function_4_1119(): pass

    label("Function_4_1119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1146")

    label("loc_1120")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1143")
    OP_8D(0xFE, 64500, 43600, 73600, 38500, 3000)
    Jump("loc_1120")

    label("loc_1143")

    Jump("loc_1251")

    label("loc_1146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1173")

    label("loc_114D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1170")
    OP_8D(0xFE, 31500, 36600, 36600, 40300, 3000)
    Jump("loc_114D")

    label("loc_1170")

    Jump("loc_1251")

    label("loc_1173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_11A0")

    label("loc_117A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_119D")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 3000)
    Jump("loc_117A")

    label("loc_119D")

    Jump("loc_1251")

    label("loc_11A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_11CD")

    label("loc_11A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11CA")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 3000)
    Jump("loc_11A7")

    label("loc_11CA")

    Jump("loc_1251")

    label("loc_11CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1251")
    OP_8E(0xFE, 0xBF04, 0x0, 0x115BC, 0x1770, 0x0)
    OP_8E(0xFE, 0xBF04, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0x115BC, 0x1770, 0x0)
    Jump("loc_11CD")

    label("loc_1251")

    Return()

    # Function_4_1119 end

    def Function_5_1252(): pass

    label("Function_5_1252")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1275")
    OP_8D(0xFE, 25948, 43568, 37838, 41060, 3000)
    Jump("Function_5_1252")

    label("loc_1275")

    Return()

    # Function_5_1252 end

    def Function_6_1276(): pass

    label("Function_6_1276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_12A3")

    label("loc_127D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12A0")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 4000)
    Jump("loc_127D")

    label("loc_12A0")

    Jump("loc_12F3")

    label("loc_12A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_12D0")

    label("loc_12AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12CD")
    OP_8D(0xFE, 43800, 43900, 47136, 39800, 4000)
    Jump("loc_12AA")

    label("loc_12CD")

    Jump("loc_12F3")

    label("loc_12D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12F3")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 4000)
    Jump("loc_12D0")

    label("loc_12F3")

    Return()

    # Function_6_1276 end

    def Function_7_12F4(): pass

    label("Function_7_12F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1322")

    label("loc_12FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_131F")
    OP_8D(0xFE, 31735, 16555, 28343, 23211, 2000)
    Jump("loc_12FC")

    label("loc_131F")

    Jump("loc_1337")

    label("loc_1322")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1337")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1322")

    label("loc_1337")

    Return()

    # Function_7_12F4 end

    def Function_8_1338(): pass

    label("Function_8_1338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_135F")

    label("loc_1347")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_135C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1347")

    label("loc_135C")

    Jump("loc_1382")

    label("loc_135F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1382")
    OP_8D(0xFE, 63200, 17400, 61600, 22900, 2000)
    Jump("loc_135F")

    label("loc_1382")

    Return()

    # Function_8_1338 end

    def Function_9_1383(): pass

    label("Function_9_1383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B2")

    label("loc_139D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13B2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_139D")

    label("loc_13B2")

    Return()

    # Function_9_1383 end

    def Function_10_13B3(): pass

    label("Function_10_13B3")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 51380, 38050, 58760, 43900, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15B5")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157E")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_146E")

    def lambda_1452():

        label("loc_1452")

        OP_97(0xFE, 0xD6D8, 0xB824, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_1452")

    QueueWorkItem2(0xFE, 1, lambda_1452)
    Jump("loc_148D")

    label("loc_146E")


    def lambda_1474():

        label("loc_1474")

        OP_97(0xFE, 0xD6D8, 0xB824, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_1474")

    QueueWorkItem2(0xFE, 1, lambda_1474)

    label("loc_148D")

    SetChrChipByIndex(0xFE, 21)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_149C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14D4")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14CC")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_14D4")

    label("loc_14CC")

    Sleep(15)
    Jump("loc_149C")

    label("loc_14D4")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 55000, 0, 47140, 74)

    label("loc_14F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_157B")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1573")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 22)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, 51380, 38050, 58760, 43900, 0)
    Jump("loc_157B")

    label("loc_1573")

    Sleep(500)
    Jump("loc_14F3")

    label("loc_157B")

    Jump("loc_15B2")

    label("loc_157E")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B2")

    def lambda_159A():
        OP_8D(0xFE, 51380, 38050, 58760, 43900, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_159A)

    label("loc_15B2")

    Jump("loc_13E7")

    label("loc_15B5")

    Return()

    # Function_10_13B3 end

    def Function_11_15B6(): pass

    label("Function_11_15B6")

    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "乻Septian Calendar 1075乼\x01",
            "Erected in partnership with the Liberl Royal\x01",
            "Family, Septian Church and Rolent City.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "乻Septian Calendar 1192乼\x01",
            "Destroyed during the Hundred Days War when Rolent\x01",
            "was bombarded by the Erebonian Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "乻Septian Calendar 1197乼\x01",
            "Rebuilt with the cooperation\x01",
            "of the citizens of Rolent.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    Return()

    # Function_11_15B6 end

    def Function_12_172B(): pass

    label("Function_12_172B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_18EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187F")
    OP_A2(0x6)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, it's Estelle.\x01",
            "You going somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FSomething like that.\x02\x03",
            "I'll be away from Rolent for a while.\x02\x03",
            "Don't cry yourself to sleep while\x01",
            "I'm gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shaddup! Who's gonna cry themselves\x01",
            "to sleep over you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But, do you know when you'll be\x01",
            "coming back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FI have no idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_18EB")

    label("loc_187F")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Hurry and come back, all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FDid you say something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "N-Never mind.\x02",
    )

    CloseMessageWindow()

    label("loc_18EB")

    Jump("loc_1F69")

    label("loc_18EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1922")

    ChrTalk(
        0xFE,
        (
            "What happened at Mayor Klaus'\x01",
            "place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F69")

    label("loc_1922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1A16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D9")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "Some news reporters came to do\x01",
            "a story on your dad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My dad's a soldier in the Royal\x01",
            "Army, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's pretty plain and boring compared\x01",
            "to bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A13")

    label("loc_19D9")


    ChrTalk(
        0xFE,
        (
            "Yeah, bracers are definitely cooler\x01",
            "than soldiers...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A13")

    Jump("loc_1F69")

    label("loc_1A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1ACE")

    ChrTalk(
        0xFE,
        "I wish I could grow up now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd become a bracer and be\x01",
            "so successful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must really suck if I got passed\x01",
            "up by the likes of Estelle, but\x01",
            "I guess that's life. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F69")

    label("loc_1ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1CAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C3F")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "Mayor Klaus was weeding around\x01",
            "the clock tower earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do mayors have to do those\x01",
            "kinds of jobs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FThat's his hobby. There are even rumors\x01",
            "that he really enjoys gardening, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI wonder if that's why he's called\x01",
            "'Ol' Man Klaus'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FWell, aren't you glad that he's informal\x01",
            "and accessible for everyone like that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CAB")

    label("loc_1C3F")


    ChrTalk(
        0xFE,
        (
            "Mayor Klaus was weeding around\x01",
            "the clock tower earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do mayors have to do those\x01",
            "kinds of jobs?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAB")

    Jump("loc_1F69")

    label("loc_1CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1D12")
    OP_A2(0x6)
    OP_4A(0x9, 0)

    ChrTalk(
        0x9,
        "I am Cassius Bright!\x05\x02",
    )

    OP_4B(0x9, 0)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "Turn and fight, you cowardly\x01",
            "monsters!\x05\x02",
        )
    )

    OP_4B(0x9, 0)
    Jump("loc_1F69")

    label("loc_1D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1E9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2F")
    OP_A2(0x6)

    ChrTalk(
        0x9,
        (
            "H-Hmph! I just wanted to say I'm\x01",
            "grateful that you saved us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "And...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hate to admit it, but...you were\x01",
            "pretty cool, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Not as cool as your dad,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I've made up my mind!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm gonna make it my goal to\x01",
            "become a bracer, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E98")

    label("loc_1E2F")


    ChrTalk(
        0x9,
        (
            "I can't get over how cool your\x01",
            "dad is, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sure any man would want\x01",
            "to be like Cassius.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E98")

    Jump("loc_1F69")

    label("loc_1E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1ED2")

    ChrTalk(
        0x9,
        (
            "闩悏偺搩偵偄傞偼偢丅\x01",
            "壌尒偨傜僶僌偩偤丅\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F69")

    label("loc_1ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3D")
    OP_A2(0x6)
    OP_4A(0x9, 0)

    ChrTalk(
        0x9,
        "If you want to go with me...\x05\x02",
    )

    OP_4B(0x9, 0)
    Sleep(800)

    ChrTalk(
        0x9,
        "You're gonna have to catch me first!\x05\x02",
    )

    OP_4B(0x9, 0)
    Jump("loc_1F69")

    label("loc_1F3D")

    OP_4A(0x9, 0)

    ChrTalk(
        0x9,
        "I'm the one who discovered it!\x05\x02",
    )

    OP_4B(0x9, 0)

    label("loc_1F69")

    TalkEnd(0x9)
    Return()

    # Function_12_172B end

    def Function_13_1F6D(): pass

    label("Function_13_1F6D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1FCB")

    ChrTalk(
        0xFE,
        (
            "Mayor Klaus came rushing by\x01",
            "here in a hurry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what happened.\x02",
    )

    CloseMessageWindow()
    Jump("loc_23CA")

    label("loc_1FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_2056")

    ChrTalk(
        0xFE,
        (
            "The Liberl News, huh? That's the\x01",
            "magazine my dad always reads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The cover always has somebody\x01",
            "really famous or popular.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23CA")

    label("loc_2056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_20C1")

    ChrTalk(
        0xFE,
        (
            "We learned about the Bracer Guild\x01",
            "at Sunday school the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Bracers are so cool.\x02",
    )

    CloseMessageWindow()
    Jump("loc_23CA")

    label("loc_20C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_2137")

    ChrTalk(
        0xFE,
        (
            "The garden at the mayor's place\x01",
            "is so well kept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that the mayor even\x01",
            "does it all himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23CA")

    label("loc_2137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_218C")
    OP_4A(0xA, 0)

    ChrTalk(
        0xA,
        (
            "Luke, let up a little! Feels like all I\x01",
            "can do is run away...\x05\x02",
        )
    )

    OP_4B(0xA, 0)
    Jump("loc_23CA")

    label("loc_218C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_233A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A7")
    OP_A2(0x7)

    ChrTalk(
        0xA,
        (
            "Thanks for saving us today,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder what would have happened\x01",
            "to us if you and Joshua hadn't come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Luke might grumble and say some,\x01",
            "mean things, but I'm sure he's really\x01",
            "grateful to you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please don't get too angry\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2337")

    label("loc_22A7")


    ChrTalk(
        0xA,
        (
            "Luke might grumble and say some,\x01",
            "mean things, but I'm sure he's really\x01",
            "grateful to you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please don't get too angry\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2337")

    Jump("loc_23CA")

    label("loc_233A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2373")

    ChrTalk(
        0xA,
        (
            "闩悏偺搩偵偄傞偼偢乕丅\x01",
            "尒偨傜嬤摗傑偱乕丅\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23CA")

    label("loc_2373")

    OP_4A(0xA, 0)

    ChrTalk(
        0xA,
        (
            "Take me with you! I'm the one\x01",
            "who told you about the place to\x01",
            "begin with.\x05\x02",
        )
    )

    OP_4B(0xA, 0)

    label("loc_23CA")

    TalkEnd(0xA)
    Return()

    # Function_13_1F6D end

    def Function_14_23CE(): pass

    label("Function_14_23CE")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2697")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F9")
    OP_A2(0x8)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Estelle, Joshua. Are you really\x01",
            "headed to Bose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FAh ha ha...I should have guessed\x01",
            "you'd know.\x02\x03",
            "You're always one of the first to\x01",
            "hear everything.\x02\x03",
            "There's a little something we need\x01",
            "to check on, so that's why we're\x01",
            "headed to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only is Cassius gone, but\x01",
            "now you two are leaving...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Awww, I want to tag along!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        "Joshua, take me with you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FI...uh...don't think that would be\x01",
            "a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I'm concerned about other\x01",
            "incidents happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I get so worried.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2694")

    label("loc_25F9")


    ChrTalk(
        0xFE,
        (
            "Okay, this time I'll wait here for you\x01",
            "like a good girl, so hurry back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If all of you are gone, it's going to\x01",
            "be a big drain on my news sources!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2694")

    Jump("loc_433B")

    label("loc_2697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_27FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278F")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        "Ah! Estelle and Joshua! And...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 400)
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "Wow! It's Schera, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020FHi, Claire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "All three bracers spoken of in town\x01",
            "together at once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Does this mean that something\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27F9")

    label("loc_278F")


    ChrTalk(
        0xB,
        (
            "All three bracers spoken of in town\x01",
            "together at once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Does this mean that something\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F9")

    Jump("loc_433B")

    label("loc_27FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_2A64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A02")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        (
            "Estelle, Joshua. I heard that you two've\x01",
            "had your fair share of accomplishments lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Let's see... You drove the fiends\x01",
            "away from the Perzel Farm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You rescued the miners at the\x01",
            "Malga Mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And this last time you escorted\x01",
            "some reporters, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FW-Wow, you certainly know a\x01",
            "lot for your age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yep, I sure do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wish those reporters would\x01",
            "hire me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think I'm perfect for the job\x01",
            "of a reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F(That's probably true.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F(Ha ha...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A61")

    label("loc_2A02")


    ChrTalk(
        0xB,
        (
            "I wish those reporters would\x01",
            "hire me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think I'm perfect for the job\x01",
            "of a reporter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A61")

    Jump("loc_433B")

    label("loc_2A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_2BA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B70")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        (
            "I saw the mayor coming out\x01",
            "of the guild earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Other than that, I've been seeing\x01",
            "Mr. Rinon's mother out in town a\x01",
            "lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She's awfully suspicious if\x01",
            "you ask me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But, I don't know which one I\x01",
            "should follow for more details...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA0")

    label("loc_2B70")


    ChrTalk(
        0xB,
        (
            "Oh, there's a juicy story calling\x01",
            "my name.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA0")

    Jump("loc_433B")

    label("loc_2BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_2C51")

    ChrTalk(
        0xB,
        (
            "According to my sources, it looks\x01",
            "like there's been an incident at\x01",
            "the Perzel Farm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder if I should go barging into\x01",
            "the guild and report it to Aina?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_433B")

    label("loc_2C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB4")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        (
            "Hey, where did Cassius take\x01",
            "off to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FUm, he's gone away on business\x01",
            "and won't be back for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Is that so... *sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Cassius was the one who I was\x01",
            "most focused on. That's too bad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002FClaire...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think that even if Cassius dressed\x01",
            "in normal attire, he'd still shine as\x01",
            "an adult male.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By changing his style he'd express\x01",
            "himself as a characteristic beau\x01",
            "aside from the typical joe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "There's no doubt he'd be popular\x01",
            "on a whole new level, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FUm, Claire?\x01",
            "How old are you again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FHa ha, she's a precocious one,\x01",
            "isn't she?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF2")

    label("loc_2EB4")


    ChrTalk(
        0xFE,
        (
            "Awww, with Cassius gone, there's\x01",
            "not much to talk about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF2")

    Jump("loc_433B")

    label("loc_2EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_378A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_302E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE3")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        (
            "I've heard that you two have had some\x01",
            "major success recently, Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I knew I was right to keep my\x01",
            "eye on you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Tee hee, keep up the good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'm a fan of the both of you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_302B")

    label("loc_2FE3")


    ChrTalk(
        0xB,
        "Tee hee, keep up the good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'm a fan of the both of you.\x02",
    )

    CloseMessageWindow()

    label("loc_302B")

    Jump("loc_3787")

    label("loc_302E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_END)), "loc_3285")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3241")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        (
            "Hey, Estelle and Joshua. Is it true\x01",
            "that you really became bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FYou're always one of the first to\x01",
            "hear everything, aren't you, Claire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This is just what I expected!\x01",
            "I saw the potential in you both\x01",
            "way back. Yup, yup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You're going to get out there and\x01",
            "earn a lot of success, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I like Scherazard's adult charm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But I'm partial to both you\x01",
            "and Joshua.\x02",
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
        "#506FH-Huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019FI-I'll take that as a compliment.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3282")

    label("loc_3241")


    ChrTalk(
        0xB,
        "The drama's finally going to begin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'm so excited! 仛\x02",
    )

    CloseMessageWindow()

    label("loc_3282")

    Jump("loc_3787")

    label("loc_3285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A7")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        "Ah...Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Did the two of you really become\x01",
            "bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWhat? How did you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That's because working in the media is\x01",
            "my future goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm going to join the Liberl News Service and work\x01",
            "hard as a reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Don't take my information lightly, either.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#506FO-Oh, sure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My gut feeling says that the two of you are going\x01",
            "to be in the tabloids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506FAh ha ha ha, well, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Isn't it romantic that you two lovers are bracers who\x01",
            "stand for justice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have this feeling that a juicy drama is\x01",
            "about to unfold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FL-Lovers?\x02\x03",
            "Joshua and I aren't lovers,\x01",
            "we're family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You really don't understand anything,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Joshua's adopted and things could go either way\x01",
            "in the future, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Plus, leaving it at that would surely please the\x01",
            "readers.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#019FR-Readers...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FI don't have a clue what she's\x01",
            "talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, I'm looking forward to the both of\x01",
            "you in more ways than one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3787")

    label("loc_36A7")


    ChrTalk(
        0xB,
        (
            "The two valiant bracers who had each\x01",
            "others' backs and attempted  to escape from\x01",
            "the crisis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ahh...love could definitely grow between them\x01",
            "from that point.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "This is so riveting...\x02",
    )

    CloseMessageWindow()

    label("loc_3787")

    Jump("loc_433B")

    label("loc_378A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_3E47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_END)), "loc_39B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3974")
    OP_A2(0x8)
    OP_A2(0x215)

    ChrTalk(
        0xB,
        (
            "Hey, Estelle and Joshua. Is it true\x01",
            "that you really became bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FYou're always one of the first to\x01",
            "hear everything, aren't you, Claire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This is just what I expected!\x01",
            "I saw the potential in you both\x01",
            "way back. Yup, yup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You're going to get out there and\x01",
            "earn a lot of success, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I like Scherazard's adult charm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But I'm partial to both you\x01",
            "and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506FH-Huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019FI-I'll take that as a compliment.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B5")

    label("loc_3974")


    ChrTalk(
        0xB,
        "The drama's finally going to begin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'm so excited! 仛\x02",
    )

    CloseMessageWindow()

    label("loc_39B5")

    Jump("loc_3E44")

    label("loc_39B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DA9")
    OP_A2(0x8)
    OP_A2(0x215)

    ChrTalk(
        0xB,
        "Ah...Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Did the two of you really\x01",
            "become bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWhat? How did you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That's because working in the\x01",
            "media is my future goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm going to join the Liberl News\x01",
            "Service and work hard as a reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Don't take my information lightly\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#506FO-Oh, sure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My gut feeling says that the two of\x01",
            "you are going to be in the tabloids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506FAh ha ha ha, well, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Isn't it romantic that you two lovers\x01",
            "are bracers who stand for justice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have this feeling that a juicy drama is\x01",
            "about to unfold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FL-Lovers?\x02\x03",
            "#000FJoshua and I aren't lovers,\x01",
            "we're family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You really don't understand\x01",
            "anything, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Joshua's adopted and things could\x01",
            "go either way in the future, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Plus, leaving it at that would surely\x01",
            "please the readers.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#019FR-Readers...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, I'm looking forward to\x01",
            "the both of you in more ways than one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E44")

    label("loc_3DA9")


    ChrTalk(
        0xB,
        (
            "The two valiant bracers who had\x01",
            "each others' backs and attempted\x01",
            "to escape from the crisis...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "This is so riveting...\x02",
    )

    CloseMessageWindow()

    label("loc_3E44")

    Jump("loc_433B")

    label("loc_3E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_425C")
    OP_A2(0x8)
    OP_A2(0x214)

    ChrTalk(
        0x101,
        "#001FGood morning, Claire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Good morning, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Did the two of you really\x01",
            "become bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FWhat? How did you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That's because working in the\x01",
            "media is my future goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm going to join the Liberl News\x01",
            "Service and work hard as a reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Don't take my information lightly\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#506FO-Oh, sure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My gut feeling says that the two of\x01",
            "you are going to be in the tabloids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506FAh ha ha ha, well, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Isn't it romantic that you two lovers\x01",
            "are bracers who stand for justice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have this feeling that a juicy drama is\x01",
            "about to unfold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FL-Lovers?\x02\x03",
            "Joshua and I aren't lovers,\x01",
            "we're family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You really don't understand\x01",
            "anything, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Joshua's adopted and things could\x01",
            "go either way in the future, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Plus, leaving it at that would surely\x01",
            "please the readers.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#019FR-Readers...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, I'm looking forward to\x01",
            "the both of you in more ways than one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_433B")

    label("loc_425C")


    ChrTalk(
        0xB,
        (
            "The two valiant bracers who had\x01",
            "each others' backs and attempted\x01",
            "to escape from the crisis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ahh...love could definitely grow\x01",
            "between them from that point.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "This is so riveting...\x02",
    )

    CloseMessageWindow()

    label("loc_433B")

    TalkEnd(0xB)
    Return()

    # Function_14_23CE end

    def Function_15_433F(): pass

    label("Function_15_433F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_44BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4446")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "Lately, my father-in-law has\x01",
            "been giving me job advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Coming from an industry veteran\x01",
            "there's a lot I can learn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems I've been pretty conceited\x01",
            "over my work in the past...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel pretty embarrassed about\x01",
            "it now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44B8")

    label("loc_4446")


    ChrTalk(
        0xFE,
        (
            "It seems I've been pretty conceited\x01",
            "over my work in the past...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel pretty embarrassed about\x01",
            "it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44B8")

    Jump("loc_4B9D")

    label("loc_44BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_4611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_457E")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "Although the work in the woods is\x01",
            "going smooth and lumber sales are\x01",
            "increasing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't figure it out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My father-in-law just won't\x01",
            "acknowledge my efforts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_460E")

    label("loc_457E")


    ChrTalk(
        0xFE,
        (
            "Although the work in the woods is\x01",
            "going smooth and lumber sales are\x01",
            "increasing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My father-in-law just won't\x01",
            "acknowledge my efforts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_460E")

    Jump("loc_4B9D")

    label("loc_4611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_46DB")

    ChrTalk(
        0xFE,
        (
            "Lumber sales have been good and\x01",
            "I'm starting to feel confident I can\x01",
            "support my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The work is going smooth and I'm\x01",
            "even on par with the output my\x01",
            "father-in-law was once doing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9D")

    label("loc_46DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_4780")

    ChrTalk(
        0xFE,
        (
            "I got an additional lumber order\x01",
            "from the merchants in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to work hard, so I can\x01",
            "sell a ton of lumber to the other\x01",
            "regions as well!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9D")

    label("loc_4780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_48EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4859")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "In order to be with my wife,\x01",
            "I took over the timber business\x01",
            "from my father-in-law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently, I've started getting\x01",
            "used to this job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I've even begun to feel\x01",
            "satisfied doing it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E8")

    label("loc_4859")


    ChrTalk(
        0xFE,
        (
            "In order to be with my wife,\x01",
            "I took over the timber business\x01",
            "from my father-in-law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently, I've started getting\x01",
            "used to this job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E8")

    Jump("loc_4B9D")

    label("loc_48EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_4918")

    ChrTalk(
        0xC,
        (
            "偙傟傪尒偨偁側偨丅\x01",
            "僶僌偱偡丅\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9D")

    label("loc_4918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_4A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E9")
    OP_A2(0x9)

    ChrTalk(
        0xC,
        (
            "It seems like it's going to take a\x01",
            "bit longer for me to get the lumber\x01",
            "together for this order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I must work hard to get my father-\x01",
            "in-law to acknowledge me...for my\x01",
            "wife's sake.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A40")

    label("loc_49E9")


    ChrTalk(
        0xC,
        (
            "I must work hard to get my father-\x01",
            "in-law to acknowledge me...for my\x01",
            "wife's sake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A40")

    Jump("loc_4B9D")

    label("loc_4A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B22")
    OP_A2(0x9)

    ChrTalk(
        0xC,
        (
            "I'm just on my way over to the\x01",
            "forest of Mistwald to the south\x01",
            "of here for work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There was a merchant from Bose\x01",
            "who came here to buy lumber.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I need to get enough ready for\x01",
            "the order I received.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9D")

    label("loc_4B22")


    ChrTalk(
        0xC,
        (
            "There was a merchant from Bose\x01",
            "who came here to buy lumber.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I need to get enough ready for\x01",
            "the order I received.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B9D")

    TalkEnd(0xC)
    Return()

    # Function_15_433F end

    def Function_16_4BA1(): pass

    label("Function_16_4BA1")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_4BFC")

    ChrTalk(
        0x11,
        "Mayor Klaus just came by here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "He greeted me with such a\x01",
            "big voice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8C")

    label("loc_4BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_4C55")

    ChrTalk(
        0x11,
        (
            "Luke's been like that since\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Boys are so simple-minded.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D8C")

    label("loc_4C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_4C88")

    ChrTalk(
        0x11,
        (
            "I wonder where Luke and\x01",
            "Pat went...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8C")

    label("loc_4C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D63")
    OP_A2(0xA)

    ChrTalk(
        0x11,
        "Oh, Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FGood morning, Yuni.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FAren't Luke and Pat with\x01",
            "you today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "They were here just a minute\x01",
            "ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "The two of them suddenly took\x01",
            "off and went somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8C")

    label("loc_4D63")


    ChrTalk(
        0x11,
        "I wonder where Luke and Pat went...\x02",
    )

    CloseMessageWindow()

    label("loc_4D8C")

    TalkEnd(0x11)
    Return()

    # Function_16_4BA1 end

    def Function_17_4D90(): pass

    label("Function_17_4D90")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_4F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EAD")
    OP_A2(0xD)

    ChrTalk(
        0xE,
        "Yesssssss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Listen to this, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I got her to go out with me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh, Aidios... It was all worth the\x01",
            "single day of trouble I went through\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F(A single day? Uh...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F(I guess that could be called\x01",
            "a victory of perseverance.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F01")

    label("loc_4EAD")


    ChrTalk(
        0xE,
        (
            "Oh, Aidios... It was all worth the\x01",
            "single day of trouble I went through\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F01")

    Jump("loc_5092")

    label("loc_4F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_5039")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD2")
    OP_A2(0xD)

    ChrTalk(
        0xE,
        (
            "I've confessed to her several times\x01",
            "since this morning, but I can't get\x01",
            "her to accept my love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It doesn't seem like she hates me\x01",
            "or anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "What am I doing wrong...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5036")

    label("loc_4FD2")


    ChrTalk(
        0xE,
        (
            "I've confessed to her several times\x01",
            "since this morning, but I can't get\x01",
            "her to accept my love.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5036")

    Jump("loc_5092")

    label("loc_5039")


    ChrTalk(
        0xE,
        "Ahhh...that girl is so cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I've got to be courageous and\x01",
            "try to talk to her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5092")

    TalkEnd(0xE)
    Return()

    # Function_17_4D90 end

    def Function_18_5096(): pass

    label("Function_18_5096")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_5193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_514F")
    OP_A2(0xD)

    ChrTalk(
        0xFE,
        "Yesssssss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I invited her to the queen's birthday\x01",
            "celebration and she said, 'yes.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to have to get a part-time\x01",
            "job and save up some cash.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5190")

    label("loc_514F")


    ChrTalk(
        0xFE,
        (
            "I'm going to have to work hard\x01",
            "now and save up some cash...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5190")

    Jump("loc_5432")

    label("loc_5193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_530B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_528F")
    OP_A2(0xD)

    ChrTalk(
        0x10,
        (
            "It's a little ways off, but the\x01",
            "queen is having her birthday\x01",
            "celebration in the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It's held every year leading up\x01",
            "to the Martial Arts Competition.\x01",
            "I hear it's a lively event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "I invited her to the festival.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5308")

    label("loc_528F")


    ChrTalk(
        0x10,
        (
            "I invited her to the festival\x01",
            "in the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "La la la...\x01",
            "There's something I want\x01",
            "to tell that girl there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5308")

    Jump("loc_5432")

    label("loc_530B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_537F")

    ChrTalk(
        0x10,
        (
            "I meet and talk with her over\x01",
            "tea every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "But the dating spots in Rolent\x01",
            "are pretty limited.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5432")

    label("loc_537F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_53F5")

    ChrTalk(
        0x10,
        "Oh, I'm so happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Being able to spend each day with\x01",
            "someone I like...why, it's better\x01",
            "than bacon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5432")

    label("loc_53F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_5432")

    ChrTalk(
        0x10,
        (
            "La la la...\x01",
            "Today is going to be our first date.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5432")

    TalkEnd(0x10)
    Return()

    # Function_18_5096 end

    def Function_19_5436(): pass

    label("Function_19_5436")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_5636")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5608")
    OP_A2(0xB)

    ChrTalk(
        0xD,
        (
            "It was when the stars had just\x01",
            "emerged from the veil of night\x01",
            "that he asked me here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Sweetly, he whispered in my ear...\x01",
            "'I want you to be mine...'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "How romantic! 仛\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's just the situation I've always\x01",
            "wanted to be in!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F(Well, I guess it's not a bad place\x01",
            "and all, but...)\x02\x03",
            "#000F(The two of them came up\x01",
            "here just for that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F(Ha ha, I guess this type of thing\x01",
            "can only be understood by those\x01",
            "involved.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5633")

    label("loc_5608")


    ChrTalk(
        0xD,
        "Tee hee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I'm on cloud nine! 仛\x02",
    )

    CloseMessageWindow()

    label("loc_5633")

    Jump("loc_5981")

    label("loc_5636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_58FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_584B")
    OP_A2(0xB)

    ChrTalk(
        0xD,
        "I'm so distressed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "He's my type, and I'd like to\x01",
            "accept his proposal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But this place is NOT my\x01",
            "ideal situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FUm...is the place or whatever\x01",
            "really that important?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Of course it is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "This could be the memory of\x01",
            "a lifetime!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It may be the place that comes to\x01",
            "my mind when I'm an old grandma\x01",
            "and lying on my deathbed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I just can't accept an alleyway like\x01",
            "this as being THAT place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FHa ha, I guess this type of thing\x01",
            "can only be understood by those\x01",
            "involved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58FC")

    label("loc_584B")


    ChrTalk(
        0xD,
        (
            "He has passionately confessed\x01",
            "his love to me several times...\x01",
            "but the situation isn't right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It would be great if he'd just say it\x01",
            "to me in a bit more romantic place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58FC")

    Jump("loc_5981")

    label("loc_58FF")


    ChrTalk(
        0xD,
        (
            "The weather is so wonderful and\x01",
            "revitalizing today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I have this strange feeling that\x01",
            "something good is going to\x01",
            "happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5981")

    TalkEnd(0xD)
    Return()

    # Function_19_5436 end

    def Function_20_5985(): pass

    label("Function_20_5985")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_5C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A88")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "I waffled back and forth for a bit...but in the\x01",
            "end, I decided to go with him to the queen's\x01",
            "birthday celebration. As a couple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My mother is already going with\x01",
            "her friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sorry, Mother...but I want to\x01",
            "go with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C80")

    label("loc_5A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C59")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "The Royal City is like a huge\x01",
            "metropolis, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The coruscating lamps of the sleepless\x01",
            "city...the elegant Grancel Castle resting\x01",
            "silently on the lakefront...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The endless coming and going of people...the\x01",
            "energy and excitement from the stops lining the\x01",
            "streets...the festival parade and fireworks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get so excited just thinking\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And to think, I'll actually be going...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm so excited I can hardly\x01",
            "even say it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C80")

    label("loc_5C59")


    ChrTalk(
        0xFE,
        "My heart is beating so quickly...\x02",
    )

    CloseMessageWindow()

    label("loc_5C80")

    Jump("loc_6148")

    label("loc_5C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_5DDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D5B")
    OP_A2(0xC)

    ChrTalk(
        0xF,
        (
            "He invited me to go see the festival\x01",
            "with him in the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm so distressed. How am I going\x01",
            "to break the news to my mother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "What if he proposes to me\x01",
            "while we we're there?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DDA")

    label("loc_5D5B")

    OP_A2(0xC)

    ChrTalk(
        0xF,
        (
            "He invited me to go see the festival\x01",
            "with him in the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "What if he proposes to me\x01",
            "while we we're there?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DDA")

    Jump("loc_6148")

    label("loc_5DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_5F8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F0F")
    OP_A2(0xB)

    ChrTalk(
        0xF,
        (
            "I'm really happy that I can meet\x01",
            "him every day like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "But the places we go for dates\x01",
            "have really fallen into a rut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502FHow typical. Boys really need to step up\x01",
            "their game! They have no imagination.\x01",
            "They're lazy, I tell ya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F(Estelle, I can hear you...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F8B")

    label("loc_5F0F")


    ChrTalk(
        0xF,
        (
            "I'm really happy that I can meet\x01",
            "him every day like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "But the places we meet have\x01",
            "really gotten repetitive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F8B")

    Jump("loc_6148")

    label("loc_5F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_5FF3")

    ChrTalk(
        0xF,
        (
            "My boyfriend is really considerate.\x01",
            "I hope that I can be his number\x01",
            "one for all time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6148")

    label("loc_5FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_6148")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D8")
    OP_A2(0xB)

    ChrTalk(
        0xF,
        (
            "Hmm-hmm-hmm...\x01",
            "We just barely started going out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Everything looks so bright and\x01",
            "promising to me now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I wonder if the world was always\x01",
            "this beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F(Our little world together...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6148")

    label("loc_60D8")


    ChrTalk(
        0xF,
        (
            "Hmm-hmm-hmm...\x01",
            "Everything feels so fresh and bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I wonder if the world was always\x01",
            "this beautiful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6148")

    TalkEnd(0xF)
    Return()

    # Function_20_5985 end

    def Function_21_614C(): pass

    label("Function_21_614C")

    EventBegin(0x0)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrPos(0x0, 49730, 0, 79070, 180)
    SetChrPos(0x1, 50770, 0, 79870, 180)
    SetChrPos(0x2, 49620, 0, 80520, 180)
    SetChrPos(0x19, 50932, 0, 42709, 270)
    SetChrPos(0x18, 64013, 0, 42894, 270)
    OP_6C(45000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x19,
        "Girl's Voice",
        (
            "Wait up! You're running like\x01",
            "a crazed lunatic...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Man's Voice",
        (
            "Who can just walk...\x01",
            "at a time like this?!\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x1)
    TurnDirection(0x19, 0x18, 0)
    OP_6D(51350, 0, 43040, 3000)

    def lambda_6271():

        label("loc_6271")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_6271")

    QueueWorkItem2(0x19, 1, lambda_6271)
    OP_8E(0x18, 0xE25B, 0x0, 0xA926, 0x1388, 0x0)
    OP_62(0x18, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x18, 0xDC36, 0x0, 0xA85E, 0xBB8, 0x0)
    OP_8F(0x18, 0xD89B, 0x0, 0xA98A, 0xBB8, 0x0)
    OP_8F(0x18, 0xD398, 0x0, 0xA7FA, 0xBB8, 0x0)
    OP_62(0x18, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x18, 0xCE24, 0x0, 0xA926, 0xBB8, 0x0)
    OP_8F(0x18, 0xC7B3, 0x0, 0xAAA0, 0x7D0, 0x0)
    OP_44(0x19, 0xFF)

    ChrTalk(
        0x18,
        (
            "#145F#4P*wheeze* *wheeze*\x02\x03",
            "#145FMaybe I should think...about\x01",
            "cutting back...on those blasted\x01",
            "cigarettes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FWhat are the two of you up to?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrPos(0x101, 50434, 0, 54609, 270)
    SetChrPos(0x102, 48721, 0, 55602, 270)
    SetChrPos(0x103, 51196, 0, 55910, 270)
    OP_43(0x101, 0x1, 0x0, 0x16)
    OP_43(0x102, 0x1, 0x0, 0x17)
    OP_43(0x103, 0x1, 0x0, 0x18)
    OP_6D(51050, 0, 45160, 1000)
    TurnDirection(0x18, 0x101, 400)
    TurnDirection(0x19, 0x101, 400)
    Sleep(2000)

    ChrTalk(
        0x18,
        (
            "#140F#4PYou kids again, huh?\x02\x03",
            "#140FActually, we've got to get\x01",
            "to Bose ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FBut the airliner's not even\x01",
            "here yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#141F#4PI know. That's why we're heading\x01",
            "there on foot.\x02\x03",
            "#141FIt'll take some time, but it's\x01",
            "not a distance that we can't\x01",
            "cover by ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FWell, don't wear yourselves out\x01",
            "too badly. By the way, are you\x01",
            "after a scoop or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#147F#4PYeah, and the mother of all\x01",
            "scoops, too!\x02\x03",
            "#144FNo time to talk!\x01",
            "We've got to make it there today!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x18, 0x1, 0x0, 0x19)
    TurnDirection(0x19, 0x18, 0)
    OP_62(0x18, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x18, 0x998B, 0x0, 0x9FC4, 0x1770, 0x0)
    OP_44(0x18, 0xFF)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8)

    ChrTalk(
        0x19,
        (
            "#154F#2PI wonder if Nial's going\x01",
            "to be all right.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 400)
    TurnDirection(0x101, 0x19, 400)
    TurnDirection(0x102, 0x19, 400)
    TurnDirection(0x103, 0x19, 400)

    ChrTalk(
        0x19,
        "#151FSee you later, Estelle! Joshua!\x02",
    )

    CloseMessageWindow()
    OP_43(0x19, 0x1, 0x0, 0x19)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x19, 0x998B, 0x0, 0x9FC4, 0x1770, 0x0)
    OP_44(0x19, 0xFF)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8)

    ChrTalk(
        0x103,
        (
            "#020FWell, aren't they a lively pair.\x01",
            "Friends of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FThose were the reporters from\x01",
            "one of the jobs Dad asked us to\x01",
            "take over.\x02\x03",
            "#000FI wonder what's going on...\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_21_614C end

    def Function_22_67BD(): pass

    label("Function_22_67BD")

    OP_92(0x101, 0x19, 0x7D0, 0xBB8, 0x0)
    Return()

    # Function_22_67BD end

    def Function_23_67CC(): pass

    label("Function_23_67CC")

    OP_92(0x102, 0x19, 0xBB8, 0xBB8, 0x0)
    Return()

    # Function_23_67CC end

    def Function_24_67DB(): pass

    label("Function_24_67DB")

    OP_92(0x103, 0x19, 0xDAC, 0xBB8, 0x0)
    Return()

    # Function_24_67DB end

    def Function_25_67EA(): pass

    label("Function_25_67EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6813")
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    TurnDirection(0x2, 0xFE, 0)
    TurnDirection(0x19, 0xFE, 0)
    OP_48()
    Jump("Function_25_67EA")

    label("loc_6813")

    Return()

    # Function_25_67EA end

    def Function_26_6814(): pass

    label("Function_26_6814")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x8)
    SetChrPos(0x1A, 72905, 0, 18979, 90)
    SetChrPos(0x102, 74801, 0, 19516, 225)
    SetChrPos(0x101, 74801, 0, 18064, 315)
    OP_6F(0x2C, 30)
    OP_6D(74132, 0, 18793, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_28(0xA, 0x4, 0x10)
    OP_28(0xA, 0x1, 0x4)

    ChrTalk(
        0x1A,
        (
            "#020FGood work, you two.\x02\x03",
            "#020FAs a rule of training, I'm going\x01",
            "to need to confirm the items\x01",
            "in your possession.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed over \x07\x02",
            "Small Box\x07\x00",
            " x2.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x373, 2)

    ChrTalk(
        0x1A,
        (
            "#020FYep...\x01",
            "They're the real deal, all right.\x02\x03",
            "I don't see any evidence of\x01",
            "tampering, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F(That was a close one...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F(I figured she would try and\x01",
            "set us up like that...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#021FCongratulations to the both of you.\x01",
            "You have successfully passed your\x01",
            "qualification test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502FYou didn't really think something\x01",
            "that simple would be a problem\x01",
            "for us, did you?\x02\x03",
            "#000FSo...uh, Schera.\x01",
            "What's in those boxes you\x01",
            "had us get?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#020FThat's for me to know and you\x01",
            "to find out...after your training\x01",
            "is finished.\x02\x03",
            "#020FThat's enough chit-chat for now,\x01",
            "so let's get back to work.\x02\x03",
            "#020FYou two still have some things\x01",
            "left to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FSeriously?\x02\x03",
            "#004FBut didn't you just say that we\x01",
            "passed the test?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#020FYou still have to learn about how\x01",
            "to report the results of your work.\x02\x03",
            "#020FI'm aware that you're both tired,\x01",
            "but this is no time to shirk your\x01",
            "duties. Let's get back to the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FWhen is this day going to be over?\x02\x03",
            "#505FOh well. No sense in giving up\x01",
            "when the finish line is in sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAgreed. It seems like we're within\x01",
            "reaching distance of our goal.\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_26_6814 end

    def Function_27_6DB3(): pass

    label("Function_27_6DB3")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x8)
    SetChrPos(0x1A, 72905, 0, 18979, 90)
    SetChrPos(0x102, 74801, 0, 19516, 225)
    SetChrPos(0x101, 74801, 0, 18064, 315)
    OP_6F(0x2C, 30)
    OP_6D(74132, 0, 18793, 0)
    OP_0D()
    OP_28(0xA, 0x4, 0x4)
    OP_28(0xA, 0x4, 0x8)
    OP_28(0xA, 0x1, 0x1)

    ChrTalk(
        0x1A,
        (
            "#020FAll your training has finally come\x01",
            "down to this.\x02\x03",
            "#020FYour qualification test will\x01",
            "begin here.\x02\x03",
            "#020FI expect to see you both use what\x01",
            "you've learned up to this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(200)
    OP_8C(0x101, 315, 400)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010FWhat's wrong, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FUm...Schera?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#020FWhat now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F...I was kind of wondering but...\x01",
            "is there not going to be a paper\x01",
            "test or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#023F...\x01",
            "Did Cassius drop you on your\x01",
            "head as a child or something?\x02\x03",
            "You just read what it said on\x01",
            "the bulletin board not that\x01",
            "long ago, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FYeah, and?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#020FAnd I even made you jot down what\x01",
            "you read in your Bracer Notebooks...\x01",
            "unless you forgot that, too.\x02\x03",
            "#020FI'm pretty sure the job listing mentioned\x01",
            "searching for and retrieving an item from\x01",
            "the sewers... Ringin' any bells yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F...\x02\x03",
            "#007FWhat a relief!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    OP_22(0x89, 0x0, 0x64)
    OP_62(0x101, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#001FOh, Divine Aidios...\x02\x03",
            "I give thanks to thee for thy\x01",
            "infinite grace in bestowing upon\x01",
            "us such wonderful gifts as sewers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018FSo what you're really saying,\x01",
            "is that you thought it was a\x01",
            "paper test?\x02\x03",
            "No wonder you were acting all\x01",
            "crazy back at the orbal factory...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)

    ChrTalk(
        0x101,
        (
            "#502FAhhh, I can already feel the nostalgia. All\x01",
            "those horrible days stuck in a classroom are\x01",
            "starting to feel like grand memories indeed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017FI'm really starting to wonder if we'll\x01",
            "even be able to graduate at all...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#509FWhat's wrong with you? Why do you have to\x01",
            "go and say something like that when I'm\x01",
            "trying to reminisce about positive things?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_744D():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_744D)

    def lambda_745B():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_745B)

    ChrTalk(
        0x1A,
        (
            "#022FAll right, that's enough jabbering,\x01",
            "you two.\x02\x03",
            "#022FThis is supposed to be a test,\x01",
            "so how about the both of you try\x01",
            "to at least look a little anxious?\x02\x03",
            "#022FJust so you know though, if you do happen to flunk\x01",
            "the test, you don't even want to imagine the kind\x01",
            "of homework I have in store for the both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FHeh, heh.\x01",
            "We'll be fine!\x02\x03",
            "#001FJust tell us what you want us\x01",
            "to do and let us loose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#026FWell, if you're so confident then how about\x01",
            "proving that you're not just blowing hot air\x01",
            "with the results of your test?\x02\x03",
            "#020FAnyway, as you both saw on the bulletin\x01",
            "board, this test will be a search\x01",
            "conducted in Rolent's sewers.\x02\x03",
            "#020FYour objective is to retrieve the\x01",
            "contents of a chest which has been\x01",
            "placed somewhere within that area.\x02\x03",
            "#020FThe layout of the sewers is extremely\x01",
            "simple, so you don't need to worry\x01",
            "about getting lost, either.\x02\x03",
            "#020FHowever... There are real, living, breathing\x01",
            "monsters down there, so if you get careless\x01",
            "and let down your guard, you WILL be sorry.\x02\x03",
            "#020FAlso, let me give you this\x01",
            "before I forget.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "Tear Balm\x07\x00",
            " x3.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "Monster Guide\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x1F5, 3)
    OP_3E(0x20F, 1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x101,
        "#505FWhat's this book for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#020FIt's called a Monster Guide, and it's\x01",
            "used to record information about\x01",
            "monsters and other opponents you meet.\x02\x03",
            "#020FWhenever you figure out an enemy's\x01",
            "attributes, you should make an\x01",
            "immediate note of it in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FSounds pretty straightforward\x01",
            "to me.\x02\x03",
            "'He who controls the flow of\x01",
            "information, controls the tide\x01",
            "of battle,' right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#021FThat's exactly what I'm saying.\x01",
            "You've really got a good head\x01",
            "on your shoulders, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FThat's some pretty useful advice.\x02\x03",
            "#001FThanks for the tip, Schera!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe'll put it to good use.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006FAll-righty then! Let's get pumped\x01",
            "and knock out this test!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FLet's.\x02\x03",
            "#010FDon't forget, though, this IS\x01",
            "an exam. We should make sure\x01",
            "we treat it as such.\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/C0500   ._SN", 0, 0, 0)
    IdleLoop()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_27_6DB3 end

    def Function_28_7C20(): pass

    label("Function_28_7C20")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x17, 0xFF)
    SetChrPos(0x102, 29410, 0, 68310, 0)
    SetChrPos(0x101, 30510, 0, 69400, 0)
    SetChrPos(0x19, 31602, 0, 67448, 0)
    SetChrPos(0x18, 32375, 0, 68461, 0)
    SetChrPos(0x17, 33719, 0, 67665, 0)
    EventBegin(0x0)
    SetMapFlags(0x400000)
    OP_6D(31270, 0, 68330, 0)
    OP_6B(3000, 0)
    OP_6C(270000, 0)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x17, 0x40)
    TurnDirection(0x101, 0x17, 0)
    TurnDirection(0x102, 0x17, 0)
    TurnDirection(0x19, 0x17, 0)
    TurnDirection(0x18, 0x17, 0)
    TurnDirection(0x17, 0x101, 0)
    OP_A2(0x259)
    OP_28(0x19, 0x4, 0x10)
    OP_28(0x19, 0x1, 0x100)
    OP_28(0x19, 0x1, 0x200)
    OP_28(0x5, 0x4, 0x40)
    OP_28(0x9, 0x4, 0x40)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x17), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7D0F")

    label("loc_7D0F")

    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x17,
        (
            "#130FThank you so much for escorting\x01",
            "me back here.\x02\x03",
            "#130FThis is the first time I've ever been\x01",
            "able to make it back from some ruins\x01",
            "without being chased or bitten or...\x02\x03",
            "#130FI don't know how to begin to\x01",
            "express my appreciation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYou don't need to thank us.\x01",
            "It's our duty as bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FI think you'd be better off hiring some\x01",
            "bracers to begin with next time you\x01",
            "go off to investigate some ruins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#130FMy head says, yes...\x01",
            "but my wallet says, no.\x01",
            "I'll try and save up a bit, though.\x02\x03",
            "#130FWell, have a wonderful day and\x01",
            "I hope we can all meet again.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x17, 0x1, 0x0, 0x1E)
    OP_8C(0x17, 90, 400)
    OP_8E(0x17, 0xAA94, 0x0, 0x104A4, 0xBB8, 0x0)
    OP_44(0x17, 0xFF)
    TurnDirection(0x101, 0x19, 400)
    TurnDirection(0x102, 0x18, 400)
    TurnDirection(0x19, 0x101, 400)
    TurnDirection(0x18, 0x101, 400)

    ChrTalk(
        0x18,
        (
            "#141FI think it's about time we said\x01",
            "goodbye, as well.\x02\x03",
            "#141FI was a bit nervous at first,\x01",
            "but you kids did a fine job.\x02\x03",
            "#147FLet me just say thank you\x01",
            "to the both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502FThat's what I like to call\x01",
            "raw skill. 仚\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#142FNow don't get all cocky on me.\x02\x03",
            "#142FThe bracers I know would make\x01",
            "you two look like little fledglings,\x01",
            "not ready to leave the nest.\x02\x03",
            "#142FYou're going to need to\x01",
            "work harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F...I'll try to remember that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FSo are the two of you headed\x01",
            "back to the company soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#141FNah, we're going to spend a day\x01",
            "or so relaxing here in Rolent.\x02\x03",
            "#141FI need to write up a rough draft\x01",
            "for some articles and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#151FI'll head over to the orbal factory\x01",
            "and get these photographs\x01",
            "developed.\x02\x03",
            "#151FTake it easy, you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x19, 0x1, 0x0, 0x1D)
    OP_43(0x18, 0x1, 0x0, 0x1E)
    OP_8C(0x18, 90, 400)
    OP_8E(0x18, 0xAA94, 0x0, 0x104A4, 0xBB8, 0x0)
    OP_44(0x18, 0xFF)
    OP_51(0x1B, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x1B, 0x3E8)
    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#000FI guess this is the last of the\x01",
            "jobs we got from Dad...\x02\x03",
            "#000FThey were much tougher than\x01",
            "I thought they'd be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI agree with you there.\x02\x03",
            "#010FI feel like I have a greater awareness\x01",
            "now about what it means to be a bracer.\x01",
            "It's not just about fighting for justice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FThere you go again, saying all\x01",
            "the right things.\x02\x03",
            "#006FBut, yeah...I guess I get where\x01",
            "you're coming from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FIt seems like we've got a long\x01",
            "road ahead of us if we want to\x01",
            "succeed in this profession...\x02\x03",
            "#019FFor the time being, why don't\x01",
            "we report to the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FThat sounds like a good idea.\x02\x03",
            "#004FOh, but before we go, how are\x01",
            "you doing? Still not feeling well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThanks for asking.\x02\x03",
            "#010FBut I'm feeling a lot better.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8)
    Return()

    # Function_28_7C20 end

    def Function_29_8626(): pass

    label("Function_29_8626")

    Sleep(500)
    OP_8C(0x19, 90, 400)
    OP_8E(0x19, 0xAA94, 0x0, 0x104A4, 0xBB8, 0x0)
    Return()

    # Function_29_8626 end

    def Function_30_8647(): pass

    label("Function_30_8647")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8670")
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    TurnDirection(0x19, 0xFE, 0)
    TurnDirection(0x18, 0xFE, 0)
    OP_48()
    Jump("Function_30_8647")

    label("loc_8670")

    Return()

    # Function_30_8647 end

    def Function_31_8671(): pass

    label("Function_31_8671")

    OP_6B(2800, 1300)
    Return()

    # Function_31_8671 end

    def Function_32_867B(): pass

    label("Function_32_867B")

    OP_6C(270000, 1300)
    Return()

    # Function_32_867B end

    def Function_33_8685(): pass

    label("Function_33_8685")

    EventBegin(0x0)
    OP_43(0x101, 0x0, 0x0, 0x22)
    OP_43(0x102, 0x0, 0x0, 0x23)
    OP_43(0x0, 0x1, 0x0, 0x24)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x2)
    StopSound(0x9470, 0x30D40, 0x0)
    OP_6D(50063, 0, 24460, 8000)
    OP_A5(0x0)
    OP_A5(0x1)
    OP_A5(0x2)
    Fade(1000)
    OP_6D(48500, 0, 16400, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(261, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#010FIt looks like we made good time.\x02\x03",
            "Not too early or too late, either.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(0x9470, 0x186A0, 0x1F40)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007FWe just barely graduated from Sunday school...\x02\x03",
            "I never dreamed we'd have to study so hard to\x01",
            "become bracers...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FWell, you're in luck. Today is our last day of training.\x02\x03",
            "Truth be told though, you're the one who signed up to be a bracer in\x01",
            "the first place, so I don't know why you'd expect to get away with\x01",
            "any less effort.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505FOh, yeah, I guess I did...\x02\x03",
            "#006FAll right, then!\x02\x03",
            "Let's get to it and make it through this last\x01",
            "hazing from Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FYou look ready to me.\x02\x03",
            "Let's go meet with Schera at the Bracer Guild\x01",
            "over there, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_A2(0x203)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_33_8685 end

    def Function_34_89D2(): pass

    label("Function_34_89D2")

    OP_A6(0x0)
    Sleep(5000)
    OP_8E(0xFE, 0xBCAC, 0x0, 0x3C28, 0xBB8, 0x0)
    OP_A3(0x0)
    Return()

    # Function_34_89D2 end

    def Function_35_89F2(): pass

    label("Function_35_89F2")

    OP_A6(0x1)
    Sleep(5000)
    OP_8E(0xFE, 0xC15C, 0x0, 0x3B60, 0xBB8, 0x0)
    OP_A3(0x1)
    Return()

    # Function_35_89F2 end

    def Function_36_8A12(): pass

    label("Function_36_8A12")

    OP_A6(0x2)
    OP_A3(0x2)
    Return()

    # Function_36_8A12 end

    def Function_37_8A19(): pass

    label("Function_37_8A19")

    EventBegin(0x0)
    OP_43(0x101, 0x0, 0x0, 0x26)
    OP_43(0x102, 0x0, 0x0, 0x27)
    OP_43(0x9, 0x0, 0x0, 0x28)
    OP_43(0xA, 0x0, 0x0, 0x29)
    OP_43(0x0, 0x1, 0x0, 0x2A)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    OP_A2(0x3)
    OP_A5(0x3)

    ChrTalk(
        0x9,
        "Hurry up and come on!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Sleep(1500)

    ChrTalk(
        0xA,
        "W-Wait for me, Luke!\x02",
    )

    CloseMessageWindow()
    OP_A5(0x4)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x4)
    OP_6D(49690, 0, 23330, 2500)
    OP_A5(0x0)
    OP_A5(0x1)
    OP_A5(0x4)

    ChrTalk(
        0x101,
        "#501FHuh? Oh, it's you two.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_A5(0x3)
    SetChrName("Luke")

    ChrTalk(
        0x9,
        "Oh, great, it's Estelle...\x02",
    )

    CloseMessageWindow()
    SetChrName("Pat")

    ChrTalk(
        0xA,
        "Hi there, Joshua!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    ChrTalk(
        0x101,
        (
            "#007FOkay, you little twerp, what's\x01",
            "with the 'Oh, great, it's\x01",
            "Estelle...' remark?\x02\x03",
            "#006FAnd what's the big hurry?\x01",
            "How about telling us where\x01",
            "you're headed? \x02\x03",
            "#006FYou're not thinking about wandering\x01",
            "out of town alone, are you? The roads\x01",
            "are full of monsters, I hope you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You're such a pest, Estelle! \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't you know there's no room\x01",
            "for GIRLS to be sticking their big\x01",
            "fat noses in BOYS' business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Quit acting like you're a bracer,\x01",
            "you wannabe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FHmm-hmm-hmm...how wrong you\x01",
            "are, Luke! How incredibly wrong!\x02\x03",
            "#006FYou're more wrong than a fool who thinks\x01",
            "there's better tasting milk in Liberl than\x01",
            "the milk that comes from the Perzel Farm!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "What...? N-No way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You're full of it, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502FIn fact, as of just a few minutes\x01",
            "ago we qualified to become real\x01",
            "bracers!\x02\x03",
            "#502FAre you hearing what I'm saying?\x01",
            "REAL BRACERS!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FMore like bracers-in-training, really. Don't think\x01",
            "you should be getting on your high horse just yet,\x01",
            "Estelle. Now a high 'pony' on the other hand...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#509FQuit being a killjoy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Wow! You two are great!\x01",
            "I'm so happy for the both of you!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        (
            "#001FOh, Pat! You're such a good\x01",
            "little boy.\x02\x03",
            "Unlike that smart-aleck and\x01",
            "cynical brat you call a friend!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Th-This isn't fair! I was supposed\x01",
            "to become a bracer first...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I can accept that Joshua became\x01",
            "a bracer before me...but getting\x01",
            "passed by the likes of Estelle...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#005FWhat's 'the likes of Estelle'\x01",
            "supposed to mean?!\x02\x03",
            "#005FJust so you know, you can't even be\x01",
            "a bracer until you're 16 years old!\x01",
            "Get it? Only MATURE people allowed.\x02\x03",
            "#005FAnd that means no little kids who are\x01",
            "still going to Sunday school!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018FI don't know how I should put\x01",
            "this, Estelle, but...Sunday school\x01",
            "is dying to have you back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You'd better watch out, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm going to go train at my secret\x01",
            "base and before you know it,\x01",
            "I'm gonna be a bracer, too!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    ChrTalk(
        0x9,
        (
            "Come on, Pat!\x01",
            "Let's go!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    ChrTalk(
        0xA,
        "A-All right...I'm coming...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x1, 0)

    ChrTalk(
        0xA,
        (
            "See you later, Estelle!\x01",
            "Bye, Joshua!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_9361():
        OP_6D(49470, 0, 24950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9361)

    def lambda_9379():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9379)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x3)
    OP_A2(0x4)
    OP_A5(0x0)
    OP_A5(0x1)
    OP_A5(0x3)
    OP_A5(0x4)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)

    ChrTalk(
        0x101,
        (
            "#007FThat boy, Luke...he's always\x01",
            "trying to pick a fight with me.\x02\x03",
            "#007FI wonder if he just plain hates\x01",
            "me or something...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#011FRather, I think it's the\x01",
            "exact opposite.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#004FWhat do you mean by that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FDon't worry about it.\x01",
            "It's just a boy thing.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#013FAt any rate, what do you think Luke meant\x01",
            "when he said 'secret base'? I don't know why,\x01",
            "but somehow it makes me a bit curious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FI know exactly what you mean!\x01",
            "A secret base sounds really\x01",
            "intriguing!\x02\x03",
            "#001FThe pure heart of a young child\x01",
            "can be so inspiring at times!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x102,
        (
            "#018FThat's not really what I meant\x01",
            "by 'curious'...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_A2(0x206)
    EventEnd(0x0)
    Return()

    # Function_37_8A19 end

    def Function_38_968C(): pass

    label("Function_38_968C")

    OP_A6(0x0)
    OP_8E(0xFE, 0xC896, 0x0, 0x6BEE, 0xBB8, 0x0)
    OP_8E(0xFE, 0xC1F2, 0x0, 0x5FDC, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_A3(0x0)
    OP_A6(0x0)

    label("loc_96DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_96ED")
    TurnDirection(0xFE, 0x9, 0)
    OP_48()
    Jump("loc_96DB")

    label("loc_96ED")

    Return()

    # Function_38_968C end

    def Function_39_96EE(): pass

    label("Function_39_96EE")

    OP_A6(0x1)
    Sleep(1000)
    OP_8E(0xFE, 0xC896, 0x0, 0x6BEE, 0xBB8, 0x0)
    OP_8E(0xFE, 0xC710, 0x0, 0x623E, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    OP_A3(0x1)
    OP_A6(0x1)

    label("loc_972B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_973D")
    TurnDirection(0xFE, 0x9, 0)
    OP_48()
    Jump("loc_972B")

    label("loc_973D")

    Return()

    # Function_39_96EE end

    def Function_40_973E(): pass

    label("Function_40_973E")

    OP_A6(0x3)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xCBE8, 0x0, 0x37A0, 0x1388, 0x0)
    OP_8E(0xFE, 0xC3B4, 0x0, 0x3D5E, 0x1388, 0x0)
    OP_8E(0xFE, 0xBF2C, 0x0, 0x57A8, 0x1388, 0x0)
    OP_8C(0xFE, 160, 400)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
    OP_A3(0x3)
    OP_A6(0x3)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x1F40)
    OP_8C(0xFE, 0, 800)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x1770, 0x0)
    OP_A3(0x3)
    OP_A6(0x3)
    OP_8E(0xFE, 0xBD74, 0x0, 0x6090, 0x1B58, 0x0)
    OP_8E(0xFE, 0xBD74, 0x0, 0x9358, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x3)
    Return()

    # Function_40_973E end

    def Function_41_9826(): pass

    label("Function_41_9826")

    OP_A6(0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xCBE8, 0x0, 0x37A0, 0x1388, 0x0)
    OP_8E(0xFE, 0xC3B4, 0x0, 0x3D5E, 0x1388, 0x0)
    OP_8E(0xFE, 0xC2EC, 0x0, 0x4826, 0x1388, 0x0)
    OP_A3(0x4)
    OP_A6(0x4)
    OP_6C(12000, 2500)
    OP_A3(0x4)
    OP_A6(0x4)
    OP_8E(0xFE, 0xC288, 0x0, 0x5410, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_A3(0x4)
    OP_A6(0x4)
    Sleep(500)
    OP_8E(0xFE, 0xBD74, 0x0, 0x6090, 0x1B58, 0x0)
    OP_8E(0xFE, 0xBD74, 0x0, 0x9358, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x4)
    Return()

    # Function_41_9826 end

    def Function_42_98DC(): pass

    label("Function_42_98DC")

    OP_A6(0x2)
    OP_6D(49800, 0, 19520, 3000)
    OP_A3(0x2)
    Return()

    # Function_42_98DC end

    def Function_43_98F4(): pass

    label("Function_43_98F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9907")
    Call(0, 54)
    Jump("loc_9987")

    label("loc_9907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_9911")
    Jump("loc_9987")

    label("loc_9911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9924")
    Call(0, 53)
    Jump("loc_9987")

    label("loc_9924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9937")
    Call(0, 52)
    Jump("loc_9987")

    label("loc_9937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9945")
    Jump("loc_9987")

    label("loc_9945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_9953")
    Call(0, 51)
    Jump("loc_9987")

    label("loc_9953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_995D")
    Jump("loc_9987")

    label("loc_995D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_996B")
    Call(0, 50)
    Jump("loc_9987")

    label("loc_996B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_9979")
    Call(0, 44)
    Jump("loc_9987")

    label("loc_9979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_9987")
    Call(0, 49)
    Jump("loc_9987")

    label("loc_9987")

    Return()

    # Function_43_98F4 end

    def Function_44_9988(): pass

    label("Function_44_9988")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 51370, 0, 29175, 180)
    OP_43(0x101, 0x0, 0x0, 0x2D)
    OP_43(0x102, 0x0, 0x0, 0x2E)
    OP_43(0x8, 0x0, 0x0, 0x2F)
    OP_43(0x0, 0x1, 0x0, 0x30)

    ChrTalk(
        0x8,
        (
            "Estelle! Joshua!\x01",
            "Am I glad I found you two!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 49700, 0, 15020, 315)
    SetChrPos(0x102, 48380, 0, 15120, 0)
    SetChrPos(0x8, 49950, 0, 25270, 180)
    OP_6B(3000, 0)
    OP_6D(50250, 0, 16110, 0)
    OP_6C(156000, 0)
    OP_67(0, 7000, -10000, 0)
    OP_0D()
    OP_8E(0x8, 0xC030, 0x0, 0x4C22, 0x1388, 0x0)

    ChrTalk(
        0x101,
        "#004FOh, hi, Aina!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FIs something wrong?\x01",
            "You seem to be in\x01",
            "quite a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#742FWe've got a bit of a problem.\x02\x03",
            "Is your father at home today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FYes, he is. He said something\x01",
            "about having to sort out a bunch\x01",
            "of documents.\x02\x03",
            "#002FBut...what's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#742FYou know Luke and Pat, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FSure we do.\x01",
            "In fact, we saw them\x01",
            "not that long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWhat's wrong?\x01",
            "Are they in some sort of trouble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#742FI don't know how to say this, but...\x02\x03",
            "I just heard from Yuni that Luke and\x01",
            "Pat ran off to the tower that lies on\x01",
            "the northern outskirts of Rolent!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004FYou mean the Tower of Esmelas?!\x02\x03",
            "#004FIsn't that place supposed to be a\x01",
            "breeding ground for monsters?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#742FThat's what they say...\x02\x03",
            "Unfortunately, at the moment, Scherazard is\x01",
            "out on other bracer business, so I want to\x01",
            "ask your father to bring the boys home safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005FWhat are you talking about?! \x02\x03",
            "#005FThere's no time for that!\x01",
            "Joshua and I will go after them\x01",
            "and bring them back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#745FI don't know if that's such a good idea...\x01",
            "The two of you only just qualified to be\x01",
            "junior bracers today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWith all due respect, I believe\x01",
            "that Estelle's judgment is correct\x01",
            "in this situation. \x02\x03",
            "#012FIf the two of us hurry, we may even\x01",
            "be able to catch up with the boys\x01",
            "before they reach the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#744F...\x02\x03",
            "#742FI understand. I will take responsibility\x01",
            "for whatever happens.\x02\x03",
            "As an emergency request from the Bracer\x01",
            "Guild, I ask that you lose no time in bringing\x01",
            "about the safe return of these children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#742FThe Esmelas Tower can be reached\x01",
            "by taking the western path at the\x01",
            "junction along the Malga Trail.\x02\x03",
            "You can get onto the Malga Trail\x01",
            "though Rolent's northwest gate.\x02\x03",
            "I'll be on standby at the guild, so\x01",
            "if you run into any trouble, you\x01",
            "know where to find me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_8E(0x8, 0xC31E, 0x0, 0x62B6, 0x1388, 0x0)
    SetChrFlags(0x8, 0x80)

    ChrTalk(
        0x101,
        "#002FThis is our first real job...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(
        0x101,
        (
            "#6P#005FCome on, Joshua!\x01",
            "We don't have any time to lose!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        "#012FI'm right behind you!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 48920, 0, 15320, 0)
    SetChrPos(0x102, 48920, 0, 15320, 0)
    OP_6C(0, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_A2(0x20C)
    OP_28(0x1, 0x1, 0x1)
    OP_28(0x1, 0x1, 0x2)
    OP_28(0x1, 0x4, 0x4)
    EventEnd(0x0)
    Return()

    # Function_44_9988 end

    def Function_45_A2E4(): pass

    label("Function_45_A2E4")

    OP_A6(0x0)

    label("loc_A2E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A2F9")
    TurnDirection(0xFE, 0x8, 0)
    OP_48()
    Jump("loc_A2E7")

    label("loc_A2F9")

    OP_A6(0x0)

    label("loc_A2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A30E")
    TurnDirection(0xFE, 0x8, 0)
    OP_48()
    Jump("loc_A2FC")

    label("loc_A30E")

    OP_A6(0x0)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x0)
    Return()

    # Function_45_A2E4 end

    def Function_46_A323(): pass

    label("Function_46_A323")

    OP_A6(0x1)

    label("loc_A326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A338")
    TurnDirection(0xFE, 0x8, 0)
    OP_48()
    Jump("loc_A326")

    label("loc_A338")

    OP_A6(0x1)

    label("loc_A33B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A34D")
    TurnDirection(0xFE, 0x8, 0)
    OP_48()
    Jump("loc_A33B")

    label("loc_A34D")

    OP_A6(0x1)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x1)
    Return()

    # Function_46_A323 end

    def Function_47_A362(): pass

    label("Function_47_A362")

    OP_A6(0x5)
    OP_8E(0xFE, 0xC2F6, 0x0, 0x4902, 0x1388, 0x0)
    TurnDirection(0xFE, 0x101, 0)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x5)
    OP_A6(0x5)
    OP_8E(0xFE, 0xC8AA, 0x0, 0x71F7, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x5)
    Return()

    # Function_47_A362 end

    def Function_48_A3AF(): pass

    label("Function_48_A3AF")

    OP_A6(0x2)
    OP_A3(0x2)
    Return()

    # Function_48_A3AF end

    def Function_49_A3B6(): pass

    label("Function_49_A3B6")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#014FEstelle, aren't you forgetting\x01",
            "something?\x02\x03",
            "Dad asked us to pick up a copy\x01",
            "of the Liberl News for him at the\x01",
            "general goods store, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#008FOh, right.\x01",
            "Completely slipped my mind...\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_49_A3B6 end

    def Function_50_A4A7(): pass

    label("Function_50_A4A7")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#012FThe Malga Trail is through\x01",
            "the northwest gate.\x02\x03",
            "#012F...That's the smaller exit\x01",
            "next to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#002FI-I know already.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_50_A4A7 end

    def Function_51_A563(): pass

    label("Function_51_A563")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010FLet's head over to the guild,\x01",
            "Estelle.\x02\x03",
            "#010FWe'd better ask Aina what jobs\x01",
            "she has lined up for us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#000FGood thinking.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_51_A563 end

    def Function_52_A617(): pass

    label("Function_52_A617")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010FShouldn't we stop by the\x01",
            "orbal factory?\x02\x03",
            "We're supposed to meet up with\x01",
            "that camerawoman, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#000FOh, yeah...that's right.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_52_A617 end

    def Function_53_A6D1(): pass

    label("Function_53_A6D1")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#015FIf you want to go to the Esmelas\x01",
            "Tower, you'll need to go out the\x01",
            "northwest gate.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#000FAh...I knew that.\x02\x03",
            "The small gate to the side of\x01",
            "the landing port, was it?\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_53_A6D1 end

    def Function_54_A7AE(): pass

    label("Function_54_A7AE")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_END)), "loc_A8CB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A84F")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(
        0x103,
        (
            "#022FAnd where do you think\x01",
            "you're going?\x02\x03",
            "Let's get over to the landing port.\x01",
            "We may be able to catch her in time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C8")

    label("loc_A84F")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022FThere's no reason for us to head\x01",
            "out on the road now.\x02\x03",
            "Let's hurry up and get over\x01",
            "to the landing port.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8C8")

    Jump("loc_A9CB")

    label("loc_A8CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A955")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(
        0x103,
        (
            "#022FWhere in the world do you two\x01",
            "think you're going?\x02\x03",
            "Right now, we need to go\x01",
            "and check the hotel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9CB")

    label("loc_A955")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022FThere's no reason for us to head\x01",
            "out on the road now.\x02\x03",
            "Let's get over to the hotel\x01",
            "and check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9CB")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_54_A7AE end

    def Function_55_A9E7(): pass

    label("Function_55_A9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9FA")
    Call(0, 63)
    Jump("loc_AA82")

    label("loc_A9FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_AA04")
    Jump("loc_AA82")

    label("loc_AA04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA17")
    Call(0, 62)
    Jump("loc_AA82")

    label("loc_AA17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA2A")
    Call(0, 61)
    Jump("loc_AA82")

    label("loc_AA2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA38")
    Jump("loc_AA82")

    label("loc_AA38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_AA46")
    Call(0, 56)
    Jump("loc_AA82")

    label("loc_AA46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_AA54")
    Call(0, 56)
    Jump("loc_AA82")

    label("loc_AA54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_AA62")
    Call(0, 56)
    Jump("loc_AA82")

    label("loc_AA62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_AA70")
    Call(0, 56)
    Jump("loc_AA82")

    label("loc_AA70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_AA7E")
    Call(0, 56)
    Jump("loc_AA82")

    label("loc_AA7E")

    Call(0, 56)

    label("loc_AA82")

    Return()

    # Function_55_A9E7 end

    def Function_56_AA83(): pass

    label("Function_56_AA83")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_AB25")

    ChrTalk(
        0x102,
        (
            "#010FLet's head over to the guild,\x01",
            "Estelle.\x02\x03",
            "#010FWe'd better ask Aina what jobs\x01",
            "she has lined up for us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#000FGood thinking.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD7E")

    label("loc_AB25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_ABA9")

    ChrTalk(
        0x102,
        (
            "#010FIt's already evening.\x02\x03",
            "#010FI'm sure Dad's waiting for us,\x01",
            "so let's head home.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FYeah, I'm beat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD7E")

    label("loc_ABA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_AC4A")

    ChrTalk(
        0x102,
        (
            "#012FThe Malga Trail is through\x01",
            "the northwest gate.\x02\x03",
            "#012F...That's the smaller exit\x01",
            "next to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002FI-I know already.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD7E")

    label("loc_AC4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_ACE6")

    ChrTalk(
        0x102,
        (
            "#010FEstelle, let's head home.\x02\x03",
            "#010FWe should let Dad know that\x01",
            "we qualified as junior bracers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FYeah, I forgot about that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD7E")

    label("loc_ACE6")


    ChrTalk(
        0x102,
        (
            "#010FIt's almost time to start our\x01",
            "training, Estelle.\x02\x03",
            "#010FLet's head over to the guildhouse\x01",
            "on the south avenue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#007FOh, all right.\x02",
    )

    CloseMessageWindow()

    label("loc_AD7E")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_56_AA83 end

    def Function_57_AD9A(): pass

    label("Function_57_AD9A")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010FIt's almost time to start our\x01",
            "training, Estelle.\x02\x03",
            "#010FLet's head over to the guildhouse\x01",
            "on the south avenue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#007FOh, all right.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0, 22000, 0, 40000, 0)
    SetChrPos(0x1, 22000, 0, 40000, 0)
    SetChrPos(0x2, 22000, 0, 40000, 0)
    SetChrPos(0x3, 22000, 0, 40000, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_57_AD9A end

    def Function_58_AE9F(): pass

    label("Function_58_AE9F")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#010FEstelle, let's head home.\x02\x03",
            "#010FWe should let Dad know that\x01",
            "we qualified as junior bracers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FYeah, I forgot about that.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0, 22000, 0, 40000, 0)
    SetChrPos(0x1, 22000, 0, 40000, 0)
    SetChrPos(0x2, 22000, 0, 40000, 0)
    SetChrPos(0x3, 22000, 0, 40000, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_58_AE9F end

    def Function_59_AF9E(): pass

    label("Function_59_AF9E")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012FThe Malga Trail is through\x01",
            "the northwest gate.\x02\x03",
            "#012F...That's the smaller exit\x01",
            "next to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002FI-I know already.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0, 22000, 0, 40000, 0)
    SetChrPos(0x1, 22000, 0, 40000, 0)
    SetChrPos(0x2, 22000, 0, 40000, 0)
    SetChrPos(0x3, 22000, 0, 40000, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_59_AF9E end

    def Function_60_B0A2(): pass

    label("Function_60_B0A2")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FIt's already evening.\x02\x03",
            "#010FI'm sure Dad's waiting for us,\x01",
            "so let's head home.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FYeah, I'm beat.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0, 22000, 0, 40000, 0)
    SetChrPos(0x1, 22000, 0, 40000, 0)
    SetChrPos(0x2, 22000, 0, 40000, 0)
    SetChrPos(0x3, 22000, 0, 40000, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_60_B0A2 end

    def Function_61_B189(): pass

    label("Function_61_B189")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010FShouldn't we stop by the\x01",
            "orbal factory?\x02\x03",
            "We're supposed to meet up with\x01",
            "that camerawoman, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#000FOh, yeah, that's right.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_61_B189 end

    def Function_62_B242(): pass

    label("Function_62_B242")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#015FIf you want to go to the Esmelas\x01",
            "Tower, you'll need to go out the\x01",
            "northwest gate.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#000FOh, right.\x02\x03",
            "The small gate to the side of\x01",
            "the landing port, was it?\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_62_B242 end

    def Function_63_B318(): pass

    label("Function_63_B318")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_END)), "loc_B435")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B3B9")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(
        0x103,
        (
            "#022FAnd where do you think\x01",
            "you're going?\x02\x03",
            "Let's get over to the landing port.\x01",
            "We may be able to catch her in time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B432")

    label("loc_B3B9")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022FThere's no reason for us to\x01",
            "head out on the road now.\x02\x03",
            "Let's hurry up and get over\x01",
            "to the landing port.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B432")

    Jump("loc_B535")

    label("loc_B435")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B4BF")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(
        0x103,
        (
            "#022FWhere in the world do you two\x01",
            "think you're going?\x02\x03",
            "Right now, we need to go\x01",
            "and check the hotel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B535")

    label("loc_B4BF")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022FThere's no reason for us to\x01",
            "head out on the road now.\x02\x03",
            "Let's get over to the hotel\x01",
            "and check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B535")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_63_B318 end

    def Function_64_B551(): pass

    label("Function_64_B551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B564")
    Call(0, 70)
    Jump("loc_B5D5")

    label("loc_B564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_B56E")
    Jump("loc_B5D5")

    label("loc_B56E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B581")
    Call(0, 69)
    Jump("loc_B5D5")

    label("loc_B581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B58F")
    Jump("loc_B5D5")

    label("loc_B58F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_B59D")
    Call(0, 65)
    Jump("loc_B5D5")

    label("loc_B59D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_B5AB")
    Call(0, 65)
    Jump("loc_B5D5")

    label("loc_B5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_B5B5")
    Jump("loc_B5D5")

    label("loc_B5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_B5C3")
    Call(0, 65)
    Jump("loc_B5D5")

    label("loc_B5C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_B5D1")
    Call(0, 65)
    Jump("loc_B5D5")

    label("loc_B5D1")

    Call(0, 65)

    label("loc_B5D5")

    Return()

    # Function_64_B551 end

    def Function_65_B5D6(): pass

    label("Function_65_B5D6")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_B678")

    ChrTalk(
        0x102,
        (
            "#010FLet's head over to the guild,\x01",
            "Estelle.\x02\x03",
            "#010FWe'd better ask Aina what jobs\x01",
            "she has lined up for us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#000FGood thinking.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B83A")

    label("loc_B678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_B6FC")

    ChrTalk(
        0x102,
        (
            "#010FIt's already evening.\x02\x03",
            "#010FI'm sure Dad's waiting for us,\x01",
            "so let's head home.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FYeah, I'm beat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B83A")

    label("loc_B6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_B706")
    Jump("loc_B83A")

    label("loc_B706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_B7A2")

    ChrTalk(
        0x102,
        (
            "#010FEstelle, let's head home.\x02\x03",
            "#010FWe should let Dad know that\x01",
            "we qualified as junior bracers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FYeah, I forgot about that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B83A")

    label("loc_B7A2")


    ChrTalk(
        0x102,
        (
            "#010FIt's almost time to start our\x01",
            "training, Estelle.\x02\x03",
            "#010FLet's head over to the guildhouse\x01",
            "on the south avenue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#007FOh, all right.\x02",
    )

    CloseMessageWindow()

    label("loc_B83A")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_65_B5D6 end

    def Function_66_B856(): pass

    label("Function_66_B856")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010FIt's almost time to start\x01",
            "our training, Estelle.\x02\x03",
            "#010FLet's head over to the guildhouse\x01",
            "on the south avenue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#007FOh, all right.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(300000, 0)
    SetChrPos(0x0, 32000, 0, 67800, 90)
    SetChrPos(0x1, 32000, 0, 67800, 90)
    SetChrPos(0x2, 32000, 0, 67800, 90)
    SetChrPos(0x3, 32000, 0, 67800, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_66_B856 end

    def Function_67_B95B(): pass

    label("Function_67_B95B")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010FEstelle, let's head home.\x02\x03",
            "#010FWe should let Dad know that\x01",
            "we qualified as junior bracers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#000FYeah, I forgot about that.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(300000, 0)
    SetChrPos(0x0, 32000, 0, 67800, 90)
    SetChrPos(0x1, 32000, 0, 67800, 90)
    SetChrPos(0x2, 32000, 0, 67800, 90)
    SetChrPos(0x3, 32000, 0, 67800, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_67_B95B end

    def Function_68_BA5A(): pass

    label("Function_68_BA5A")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#010FWait, Estelle.\x02\x03",
            "#010FWe haven't bought a copy of the\x01",
            "Liberl News from Mr. Rinon's place.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#000FWhoops. Totally forgot about that.\x01",
            "We'd better get over to the general\x01",
            "goods store then.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(300000, 0)
    SetChrPos(0x0, 32000, 0, 67800, 90)
    SetChrPos(0x1, 32000, 0, 67800, 90)
    SetChrPos(0x2, 32000, 0, 67800, 90)
    SetChrPos(0x3, 32000, 0, 67800, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_68_BA5A end

    def Function_69_BB94(): pass

    label("Function_69_BB94")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010FShouldn't we stop by the\x01",
            "orbal factory?\x02\x03",
            "We're supposed to meet up with\x01",
            "that camerawoman, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, yeah, that's right.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_69_BB94 end

    def Function_70_BC46(): pass

    label("Function_70_BC46")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_END)), "loc_BD63")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BCE7")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(
        0x103,
        (
            "#022FAnd where do you think\x01",
            "you're going?\x02\x03",
            "Let's get over to the landing port.\x01",
            "We may be able to catch her in\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD60")

    label("loc_BCE7")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022FThere's no reason for us to\x01",
            "head out on the road now.\x02\x03",
            "Let's hurry up and get over\x01",
            "to the landing port.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD60")

    Jump("loc_BE63")

    label("loc_BD63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BDED")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(
        0x103,
        (
            "#022FWhere in the world do you two\x01",
            "think you're going?\x02\x03",
            "Right now, we need to go\x01",
            "and check the hotel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE63")

    label("loc_BDED")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022FThere's no reason for us to\x01",
            "head out on the road now.\x02\x03",
            "Let's get over to the hotel\x01",
            "and check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE63")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_70_BC46 end

    def Function_71_BE7F(): pass

    label("Function_71_BE7F")

    EventBegin(0x0)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrPos(0x102, 54640, 0, 43670, 0)
    SetChrPos(0x101, 55690, 0, 43940, 0)
    OP_6D(55160, 1000, 47020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(314000, 0)
    OP_6E(261, 0)
    FadeToBright(2000, 0)

    def lambda_BF08():
        OP_6D(55160, 9000, 47020, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF08)
    OP_6C(44000, 7000)
    Fade(1000)
    OP_6D(55310, 0, 45740, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    Sleep(1500)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "乻Septian Calendar 1075乼\x01",
            "Erected in partnership with the Liberl Royal\x01",
            "Family, Septian Church and Rolent City.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "乻Septian Calendar 1192乼\x01",
            "Destroyed during the Hundred Days War when Rolent\x01",
            "was bombarded by the Erebonian Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "乻Septian Calendar 1197乼\x01",
            "Rebuilt with the cooperation\x01",
            "of the citizens of Rolent.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#010F#1PEvery time I see this clock tower,\x01",
            "I always think...\x02\x03",
            "They sure did a superb job restoring\x01",
            "it after the war.\x02\x03",
            "You can sure feel the spirit of\x01",
            "Rolent's people from this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#500F#4P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F#1PEstelle?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#501F#4PUm, Joshua...\x02\x03",
            "What do you think about going up\x01",
            "with me and waiting until Schera\x01",
            "shows up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#1PYou mean the clock tower?\x01",
            "Sure, I don't mind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#4POkay, come on.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T0133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_71_BE7F end

    def Function_72_C2A0(): pass

    label("Function_72_C2A0")

    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    AddParty(0x2, 0xFF)
    OP_A2(0x301)
    EventBegin(0x0)
    SetMapFlags(0x1)
    SetChrPos(0x102, 51920, 0, 49090, 180)
    SetChrPos(0x101, 53010, 0, 50110, 270)
    SetChrPos(0x103, 56060, 0, 43300, 270)
    OP_6C(45000, 0)
    OP_6A(0x102)
    FadeToBright(2000, 0)
    OP_43(0x101, 0x0, 0x0, 0x4A)
    OP_8E(0x102, 0xCA12, 0x0, 0xAC9E, 0xBB8, 0x0)
    ClearMapFlags(0x1)
    OP_43(0x102, 0x0, 0x0, 0x49)
    OP_6D(55290, 0, 43570, 1500)
    OP_6A(0x0)
    ClearMapFlags(0x1)

    ChrTalk(
        0x103,
        (
            "#021FAwww...\x01",
            "The two of you had such a cute\x01",
            "scene going on up there.\x02\x03",
            "Why, my cheeks even feel a bit\x01",
            "hot just thinking about it!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#014F#4PWhat's that supposed to mean?\x02\x03",
            "#014FYou were spying on us?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027FGive me some credit, will you?\x02\x03",
            "I just happened to see you when\x01",
            "I looked up to check the time.\x02\x03",
            "#021FI sure wish I had an orbal camera\x01",
            "to get a shot of that view...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F#4PCome on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FWhat are you trying to say, Schera?\x01",
            "That's called family bonding, plain\x01",
            "and simple.\x02\x03",
            "It's kind of like your habit of\x01",
            "hugging everyone after your\x01",
            "third bottle of wine.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1300)

    ChrTalk(
        0x102,
        "#017F#4P*sigh* Let's not get into that...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#501FWhat's with the sigh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025FYou really don't know how\x01",
            "to take a joke, do you?\x02\x03",
            "#020FWell, whatever.\x01",
            "Did you say hi to Lena\x01",
            "while you were up there?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#000FYeah...\x02\x03",
            "I even asked for her to\x01",
            "watch over Dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021FI see, then I guess it looks\x01",
            "like you're all set.\x02\x03",
            "You know, Lena's protection is\x01",
            "equal to that of the Goddess,\x01",
            "herself.\x02\x03",
            "Your dad's safety is pretty\x01",
            "much guaranteed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FI think you may be giving her\x01",
            "a little too much credit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PNow that you mention it,\x01",
            "you met Estelle's mother\x01",
            "before, right, Schera?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FYeah...when I was a child.\x02\x03",
            "I was still in a troupe at the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#4PA troupe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FYeah, a troupe in a traveling\x01",
            "circus. Schera was a dancer.\x02\x03",
            "Although it was a long time ago,\x01",
            "we first met when she came to\x01",
            "Rolent with the circus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F12 years ago to be exact.\x01",
            "I was 11 and Estelle was 4.\x02\x03",
            "And because of that chance encounter,\x01",
            "when I became a bracer, I trained\x01",
            "under your father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#4PI didn't know that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FMaybe I'll tell you about it sometime\x01",
            "when I get a chance.\x02\x03",
            "Are you about ready to head\x01",
            "out for Bose?\x02\x03",
            "With airliner flights canceled, we'll\x01",
            "just have to make our way to Bose\x01",
            "the old-fashioned way: by foot.\x02\x03",
            "First, we'll need to make our way to\x01",
            "the Verte Bridge Checkpoint, which\x01",
            "sits on the border of the Bose region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PThe Verte Bridge is located at the\x01",
            "west end of the Milch Main Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FIt looks like we're all set,\x01",
            "so let's go!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x52, 0x4, 0x2)
    OP_28(0x52, 0x4, 0x4)
    OP_28(0x52, 0x1, 0x1)
    OP_3F(0x32A, 1)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x400000)
    OP_20(0x3E8)
    EventEnd(0x0)
    OP_1D(0xA)
    Return()

    # Function_72_C2A0 end

    def Function_73_CC23(): pass

    label("Function_73_CC23")

    OP_8E(0x102, 0xD50C, 0x0, 0xA690, 0xBB8, 0x0)
    OP_8C(0x102, 45, 400)
    Return()

    # Function_73_CC23 end

    def Function_74_CC3F(): pass

    label("Function_74_CC3F")

    SetChrFlags(0x101, 0x4)
    OP_8E(0x101, 0xC9B8, 0x0, 0xC468, 0xBB8, 0x0)
    OP_8E(0x101, 0xCAF8, 0x0, 0xAC94, 0xBB8, 0x0)
    OP_8E(0x101, 0xD41C, 0x0, 0xAB86, 0xBB8, 0x0)
    ClearChrFlags(0x101, 0x4)
    TurnDirection(0x101, 0x103, 400)
    Return()

    # Function_74_CC3F end

    def Function_75_CC8D(): pass

    label("Function_75_CC8D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "West: Malga Trail\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_75_CC8D end

    def Function_76_CCD1(): pass

    label("Function_76_CCD1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "North: Rolent Landing Port\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_76_CCD1 end

    def Function_77_CD1E(): pass

    label("Function_77_CD1E")

    SetPlaceName(0x4) # 艾利兹街道
    Return()

    # Function_77_CD1E end

    def Function_78_CD22(): pass

    label("Function_78_CD22")

    SetPlaceName(0x2) # 艾利兹街道
    Return()

    # Function_78_CD22 end

    def Function_79_CD26(): pass

    label("Function_79_CD26")

    SetPlaceName(0x6) # 艾利兹街道
    Return()

    # Function_79_CD26 end

    def Function_80_CD2A(): pass

    label("Function_80_CD2A")

    SetPlaceName(0x5) # 艾利兹街道
    Return()

    # Function_80_CD2A end

    def Function_81_CD2E(): pass

    label("Function_81_CD2E")

    SetPlaceName(0x7) # 艾利兹街道
    Return()

    # Function_81_CD2E end

    def Function_82_CD32(): pass

    label("Function_82_CD32")

    SetPlaceName(0x8) # 艾利兹街道
    Return()

    # Function_82_CD32 end

    def Function_83_CD36(): pass

    label("Function_83_CD36")

    SetPlaceName(0x3) # 艾利兹街道
    Return()

    # Function_83_CD36 end

    def Function_84_CD3A(): pass

    label("Function_84_CD3A")

    SetPlaceName(0xA) # 艾利兹街道
    Return()

    # Function_84_CD3A end

    def Function_85_CD3E(): pass

    label("Function_85_CD3E")

    SetPlaceName(0xC) # 艾利兹街道
    Return()

    # Function_85_CD3E end

    def Function_86_CD42(): pass

    label("Function_86_CD42")

    SetPlaceName(0x9) # 艾利兹街道
    Return()

    # Function_86_CD42 end

    def Function_87_CD46(): pass

    label("Function_87_CD46")

    SetPlaceName(0x15) # 艾利兹街道
    Return()

    # Function_87_CD46 end

    def Function_88_CD4A(): pass

    label("Function_88_CD4A")

    SetPlaceName(0x16) # 艾利兹街道
    Return()

    # Function_88_CD4A end

    def Function_89_CD4E(): pass

    label("Function_89_CD4E")

    SetPlaceName(0x17) # 艾利兹街道
    Return()

    # Function_89_CD4E end

    SaveToFile()

Try(main)
