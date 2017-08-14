from ED6ScenarioHelper import *

def main():
    # 卢安飞艇坪

    CreateScenaFile(
        FileName            = 'T2100   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2100   ._SN',
            'ED6_DT01/T2100_1 ._SN',
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
        '奈尔',                                 # 9
        '克拉姆',                               # 10
        '穆拉德老人',                           # 11
        '特蕾莎院长',                           # 12
        '基库',                                 # 13
        '利顿',                                 # 14
        '希艾尔',                               # 15
        '鲁特尔',                               # 16
        '兰达老人',                             # 17
        '米优',                                 # 18
        '男性的声音',                           # 19
        '梅尔茨',                               # 20
        '哈尔德',                               # 21
        '拜舍尔',                               # 22
        '西加罗',                               # 23
        '艾德尔',                               # 24
        '雷加洛',                               # 25
        '希尔碧',                               # 26
        '鲁蓓',                                 # 27
        '阿杰',                                 # 28
        '玛奇尔达',                             # 29
        '戴尔蒙市长',                           # 30
        '船',                                   # 31
        '船',                                   # 32
        '梅威海道方向',                         # 33
        '卢安市·南街区',                       # 34
        '卢安飞艇坪',                           # 35
    )

    DeclEntryPoint(
        Unknown_00              = 26000,
        Unknown_04              = 0,
        Unknown_08              = 112000,
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH02570 ._CH',             # 03
        'ED6_DT07/CH02320 ._CH',             # 04
        'ED6_DT07/CH01290 ._CH',             # 05
        'ED6_DT07/CH01540 ._CH',             # 06
        'ED6_DT07/CH01760 ._CH',             # 07
        'ED6_DT06/CH20159 ._CH',             # 08
        'ED6_DT07/CH01050 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT07/CH01020 ._CH',             # 0C
        'ED6_DT07/CH00005 ._CH',             # 0D
        'ED6_DT07/CH00015 ._CH',             # 0E
        'ED6_DT07/CH00045 ._CH',             # 0F
        'ED6_DT07/CH02323 ._CH',             # 10
        'ED6_DT07/CH00005 ._CH',             # 11
        'ED6_DT07/CH00015 ._CH',             # 12
        'ED6_DT07/CH00045 ._CH',             # 13
        'ED6_DT07/CH02410 ._CH',             # 14
        'ED6_DT07/CH01220 ._CH',             # 15
        'ED6_DT07/CH02490 ._CH',             # 16
        'ED6_DT07/CH01030 ._CH',             # 17
        'ED6_DT07/CH01070 ._CH',             # 18
        'ED6_DT07/CH01153 ._CH',             # 19
        'ED6_DT07/CH01003 ._CH',             # 1A
        'ED6_DT07/CH01053 ._CH',             # 1B
        'ED6_DT07/CH01023 ._CH',             # 1C
        'ED6_DT07/CH01120 ._CH',             # 1D
        'ED6_DT06/CH20160 ._CH',             # 1E
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH02570P._CP',             # 03
        'ED6_DT07/CH02320P._CP',             # 04
        'ED6_DT07/CH01290P._CP',             # 05
        'ED6_DT07/CH01540P._CP',             # 06
        'ED6_DT07/CH01760P._CP',             # 07
        'ED6_DT06/CH20159P._CP',             # 08
        'ED6_DT07/CH01050P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT07/CH01020P._CP',             # 0C
        'ED6_DT07/CH00005P._CP',             # 0D
        'ED6_DT07/CH00015P._CP',             # 0E
        'ED6_DT07/CH00045P._CP',             # 0F
        'ED6_DT07/CH02323P._CP',             # 10
        'ED6_DT07/CH00005P._CP',             # 11
        'ED6_DT07/CH00015P._CP',             # 12
        'ED6_DT07/CH00045P._CP',             # 13
        'ED6_DT07/CH02410P._CP',             # 14
        'ED6_DT07/CH01220P._CP',             # 15
        'ED6_DT07/CH02490P._CP',             # 16
        'ED6_DT07/CH01030P._CP',             # 17
        'ED6_DT07/CH01070P._CP',             # 18
        'ED6_DT07/CH01153P._CP',             # 19
        'ED6_DT07/CH01003P._CP',             # 1A
        'ED6_DT07/CH01053P._CP',             # 1B
        'ED6_DT07/CH01023P._CP',             # 1C
        'ED6_DT07/CH01120P._CP',             # 1D
        'ED6_DT06/CH20160P._CP',             # 1E
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
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
        X                   = 37220,
        Z                   = 1700,
        Y                   = -36830,
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
        X                   = 2420,
        Z                   = -250,
        Y                   = 94980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
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
        X                   = -4300,
        Z                   = 4000,
        Y                   = 3300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 1700,
        Z                   = 0,
        Y                   = 5200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 21800,
        Z                   = 0,
        Y                   = 73300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 21000,
        Z                   = 0,
        Y                   = 74300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 20400,
        Z                   = 0,
        Y                   = 72900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        X                   = 16600,
        Z                   = -1800,
        Y                   = 111000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 41290,
        Z                   = -1970,
        Y                   = 66200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 16430,
        Z                   = -1800,
        Y                   = 111960,
        Direction           = 280,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x115,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 47400,
        Z                   = 0,
        Y                   = 81500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 45940,
        Z                   = 0,
        Y                   = 80850,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 49870,
        Z                   = 0,
        Y                   = 79770,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 49320,
        Z                   = 0,
        Y                   = 81240,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 31510,
        Z                   = 0,
        Y                   = 89810,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 29470,
        Z                   = 0,
        Y                   = 87520,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 23580,
        Z                   = 2160,
        Y                   = 102820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 25260,
        Z                   = 0,
        Y                   = 128199,
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
        X                   = 51060,
        Z                   = 400,
        Y                   = 27190,
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
        X                   = 81750,
        Z                   = 0,
        Y                   = 80640,
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
        X                   = 52790,
        Y                   = 2000,
        Z                   = 67850,
        Range               = 49030,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xFD8E,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 47550,
        Y                   = 2000,
        Z                   = 53890,
        Range               = 55410,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xC33C,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 35920,
        Y                   = 5000,
        Z                   = 88550,
        Range               = 99180,
        Unknown_10          = 0xFFFFEC78,
        Unknown_14          = 0xFCEE,
        Unknown_18          = 0x0,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 27150,
        Y                   = 2000,
        Z                   = 78400,
        Range               = 25490,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x11F80,
        Unknown_18          = 0x0,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = 44990,
        Y                   = 0,
        Z                   = 89330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 44,
    )

    DeclEvent(
        X                   = 38080,
        Y                   = 0,
        Z                   = 78540,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 45,
    )

    DeclEvent(
        X                   = 37930,
        Y                   = 0,
        Z                   = 89380,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 46,
    )

    DeclEvent(
        X                   = 30610,
        Y                   = 0,
        Z                   = 96060,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 46,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 108200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 47,
    )

    DeclEvent(
        X                   = 20930,
        Y                   = -1500,
        Z                   = 93960,
        Range               = 3500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 48,
    )

    DeclEvent(
        X                   = 61000,
        Y                   = 0,
        Z                   = 78900,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 49,
    )

    DeclEvent(
        X                   = 66890,
        Y                   = -500,
        Z                   = 93800,
        Range               = 2200,
        Unknown_10          = 0x898,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 50,
    )

    DeclEvent(
        X                   = 73630,
        Y                   = 0,
        Z                   = 80790,
        Range               = 3500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 51,
    )


    DeclActor(
        TriggerX            = 13500,
        TriggerZ            = 0,
        TriggerY            = 73400,
        TriggerRange        = 1000,
        ActorX              = 13500,
        ActorZ              = 1500,
        ActorY              = 73400,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23750,
        TriggerZ            = 1000,
        TriggerY            = 102860,
        TriggerRange        = 1000,
        ActorX              = 23580,
        ActorZ              = 4000,
        ActorY              = 102820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_6EA",          # 00, 0
        "Function_1_B4B",          # 01, 1
        "Function_2_C83",          # 02, 2
        "Function_3_E00",          # 03, 3
        "Function_4_E4D",          # 04, 4
        "Function_5_E71",          # 05, 5
        "Function_6_EE2",          # 06, 6
        "Function_7_1944",         # 07, 7
        "Function_8_1C19",         # 08, 8
        "Function_9_1E1A",         # 09, 9
        "Function_10_1FD2",        # 0A, 10
        "Function_11_20DE",        # 0B, 11
        "Function_12_293B",        # 0C, 12
        "Function_13_2C26",        # 0D, 13
        "Function_14_2D09",        # 0E, 14
        "Function_15_2E95",        # 0F, 15
        "Function_16_2FA1",        # 10, 16
        "Function_17_3098",        # 11, 17
        "Function_18_3378",        # 12, 18
        "Function_19_3607",        # 13, 19
        "Function_20_3A7B",        # 14, 20
        "Function_21_3D89",        # 15, 21
        "Function_22_3D8E",        # 16, 22
        "Function_23_438E",        # 17, 23
        "Function_24_47C5",        # 18, 24
        "Function_25_495E",        # 19, 25
        "Function_26_4DEF",        # 1A, 26
        "Function_27_5434",        # 1B, 27
        "Function_28_5467",        # 1C, 28
        "Function_29_549F",        # 1D, 29
        "Function_30_54D9",        # 1E, 30
        "Function_31_5DF5",        # 1F, 31
        "Function_32_607F",        # 20, 32
        "Function_33_6512",        # 21, 33
        "Function_34_6612",        # 22, 34
        "Function_35_6B0A",        # 23, 35
        "Function_36_6B33",        # 24, 36
        "Function_37_79FC",        # 25, 37
        "Function_38_808F",        # 26, 38
        "Function_39_8562",        # 27, 39
        "Function_40_9168",        # 28, 40
        "Function_41_92C5",        # 29, 41
        "Function_42_949B",        # 2A, 42
        "Function_43_966F",        # 2B, 43
        "Function_44_9716",        # 2C, 44
        "Function_45_971A",        # 2D, 45
        "Function_46_971E",        # 2E, 46
        "Function_47_9722",        # 2F, 47
        "Function_48_9726",        # 30, 48
        "Function_49_972A",        # 31, 49
        "Function_50_972E",        # 32, 50
        "Function_51_9732",        # 33, 51
    )


    def Function_0_6EA(): pass

    label("Function_0_6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_727")
    SetChrPos(0x15, 14980, 0, 68500, 180)
    SetChrPos(0x18, 45320, 0, 82680, 270)
    SetChrPos(0x19, 43580, 0, 82680, 90)
    Jump("loc_A73")

    label("loc_727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_764")
    SetChrPos(0x15, 14980, 0, 68500, 180)
    SetChrPos(0x18, 51500, 1000, 103610, 270)
    SetChrPos(0x19, 51500, 1000, 102530, 270)
    Jump("loc_A73")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_7CD")
    SetChrPos(0x15, 14980, 0, 68500, 180)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 13750, 0, 69100, 180)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 12090, 0, 69000, 180)
    SetChrPos(0x18, 64440, 0, 89630, 280)
    SetChrPos(0x19, 65900, 0, 99540, 0)
    Jump("loc_A73")

    label("loc_7CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_885")
    SetChrPos(0x15, 14980, 0, 68500, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 26)
    OP_44(0x10, 0x0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, 42710, -1800, 69570, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 27)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 39480, -1800, 69500, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 28)
    OP_44(0xF, 0x0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xF, 0x4)
    SetChrPos(0xF, 36220, -1800, 69550, 180)
    SetChrPos(0x18, 45320, 0, 82680, 270)
    SetChrPos(0x19, 43580, 0, 82680, 90)
    Jump("loc_A73")

    label("loc_885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_935")
    SetChrPos(0x15, 10810, 0, 72960, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 46060, 0, 79390, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 17800, 0, 73500, 90)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 48870, 0, 80920, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 48270, 0, 78680, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 49650, 0, 78980, 180)
    SetChrPos(0x18, 24590, 0, 69200, 135)
    SetChrPos(0x19, 22240, 0, 68440, 180)
    Jump("loc_A73")

    label("loc_935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_9F6")
    SetChrPos(0x15, 10810, 0, 72960, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 45860, 0, 78450, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 17800, 0, 73500, 90)
    ClearChrFlags(0x13, 0x80)
    OP_43(0x13, 0x0, 0x0, 0x5)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 18050, -1800, 111280, 270)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 18320, -1800, 113600, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 18190, -1800, 110060, 270)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x18, 19630, 0, 72720, 270)
    SetChrPos(0x19, 20110, 0, 74150, 270)
    Jump("loc_A73")

    label("loc_9F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_A22")
    SetChrPos(0x18, 47130, 0, 78430, 180)
    SetChrPos(0x19, 45970, 0, 78440, 180)
    Jump("loc_A73")

    label("loc_A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_A73")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 47840, 0, 78500, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 17800, 0, 73500, 90)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_A73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A91")
    OP_64(0x0, 0x1)

    label("loc_A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_A9F")
    OP_A3(0x3FA)
    Event(0, 26)

    label("loc_A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_AAD")
    OP_A3(0x3FB)
    Event(0, 30)

    label("loc_AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_ABB")
    OP_A3(0x3FC)
    Event(0, 31)

    label("loc_ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_AD2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FD)
    Event(0, 32)

    label("loc_AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 6)), scpexpr(EXPR_END)), "loc_AE0")
    OP_A3(0x3FE)
    Event(0, 36)

    label("loc_AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 7)), scpexpr(EXPR_END)), "loc_AF1")
    OP_A3(0x3FF)
    Event(0, 39)
    OP_A2(0x412)

    label("loc_AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_B08")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3F0)
    Event(0, 38)

    label("loc_B08")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_B14"),
        (SWITCH_DEFAULT, "loc_B39"),
    )


    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B23")
    OP_A2(0x412)
    Event(0, 23)

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B36")
    OP_A2(0x429)
    Event(0, 33)

    label("loc_B36")

    Jump("loc_B39")

    label("loc_B39")

    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_6EA end

    def Function_1_B4B(): pass

    label("Function_1_B4B")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFF5420, 0x30047)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B7E")
    OP_B1("t2100_y")
    Jump("loc_B87")

    label("loc_B7E")

    OP_B1("t2100_n")

    label("loc_B87")

    SetChrBattleFlags(0xA, 0x20)
    OP_89(0xA, -960, -2780, 92980, 135)
    OP_72(0x12, 0x2)
    OP_71(0x12, 0x400)
    OP_71(0x12, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BCA")
    OP_64(0x0, 0x1)

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_BD4")
    Jump("loc_C71")

    label("loc_BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_BEA")
    OP_6F(0x11, 1020)
    OP_72(0x1A, 0x2)
    Jump("loc_C71")

    label("loc_BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_BF4")
    Jump("loc_C71")

    label("loc_BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_C0F")
    OP_1B(0x0, 0x0, 0x2B)
    OP_6F(0x11, 1020)
    OP_72(0x1A, 0x2)
    Jump("loc_C71")

    label("loc_C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_END)), "loc_C25")
    OP_6F(0x11, 1020)
    OP_72(0x1A, 0x2)
    Jump("loc_C71")

    label("loc_C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_C2F")
    Jump("loc_C71")

    label("loc_C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_C3E")
    OP_1B(0x0, 0x0, 0x2A)
    Jump("loc_C71")

    label("loc_C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_END)), "loc_C59")
    OP_1B(0x0, 0x0, 0x29)
    OP_6F(0x11, 1020)
    OP_72(0x1A, 0x2)
    Jump("loc_C71")

    label("loc_C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_C71")
    OP_1B(0x0, 0x0, 0x28)
    OP_6F(0x11, 1020)
    OP_72(0x1A, 0x2)

    label("loc_C71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C82")
    OP_22(0x1C5, 0x1, 0x64)

    label("loc_C82")

    Return()

    # Function_1_B4B end

    def Function_2_C83(): pass

    label("Function_2_C83")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA8")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_DEA")

    label("loc_CA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC1")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_DEA")

    label("loc_CC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_DEA")

    label("loc_CDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_DEA")

    label("loc_CF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_DEA")

    label("loc_D0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D25")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_DEA")

    label("loc_D25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_DEA")

    label("loc_D3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D57")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_DEA")

    label("loc_D57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D70")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_DEA")

    label("loc_D70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D89")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_DEA")

    label("loc_D89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA2")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_DEA")

    label("loc_DA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBB")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_DEA")

    label("loc_DBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_DEA")

    label("loc_DD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_DEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DFF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_DEA")

    label("loc_DFF")

    Return()

    # Function_2_C83 end

    def Function_3_E00(): pass

    label("Function_3_E00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E4C")
    OP_99(0xFE, 0x0, 0x3, 0x5DC)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2B")
    Sleep(1000)
    Jump("loc_E49")

    label("loc_E2B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E44")
    Sleep(2000)
    Jump("loc_E49")

    label("loc_E44")

    Sleep(3000)

    label("loc_E49")

    Jump("Function_3_E00")

    label("loc_E4C")

    Return()

    # Function_3_E00 end

    def Function_4_E4D(): pass

    label("Function_4_E4D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E70")
    OP_8D(0xFE, 28870, 90550, 28960, 83580, 4000)
    Jump("Function_4_E4D")

    label("loc_E70")

    Return()

    # Function_4_E4D end

    def Function_5_E71(): pass

    label("Function_5_E71")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EE1")
    OP_8E(0xFE, 0x4038, 0xFFFFF8F8, 0x1AC20, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_8E(0xFE, 0x4092, 0xFFFFF8F8, 0x1B9C2, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    Jump("Function_5_E71")

    label("loc_EE1")

    Return()

    # Function_5_E71 end

    def Function_6_EE2(): pass

    label("Function_6_EE2")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_103E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB2")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "不管是爆发战争也好，\x01",
            "市长被逮捕也罢，\x01",
            "我还是会和平常一样生活……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且今后会出现什么情况\x01",
            "也是未知的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "就算哀怨也无济于事。\x02",
    )

    CloseMessageWindow()
    Jump("loc_103B")

    label("loc_FB2")


    ChrTalk(
        0xFE,
        (
            "不管是爆发战争也好，\x01",
            "市长被逮捕也罢，\x01",
            "我还是会和平常一样生活……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "就算哀怨也无济于事。\x02",
    )

    CloseMessageWindow()

    label("loc_103B")

    Jump("loc_1940")

    label("loc_103E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1141")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1101")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "最近的年轻人处理事情\x01",
            "都显得太马马虎虎了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "应该要先了解在这世上\x01",
            "什么事情才值得在第一时间完成……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这是我活了这几十年\x01",
            "所领悟出来的真理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_113E")

    label("loc_1101")


    ChrTalk(
        0xFE,
        (
            "最近的年轻人处理事情\x01",
            "都显得太马马虎虎了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113E")

    Jump("loc_1940")

    label("loc_1141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_121E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F7")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "水真是不可思议的东西……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每个时候都会有\x01",
            "不同的表情呈现出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这几十年来我一直这样看着这片水面，\x01",
            "一天也没有感到过厌倦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121B")

    label("loc_11F7")


    ChrTalk(
        0xFE,
        "水真是不可思议的东西……\x02",
    )

    CloseMessageWindow()

    label("loc_121B")

    Jump("loc_1940")

    label("loc_121E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 3)), scpexpr(EXPR_END)), "loc_12FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B2")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "是你们几个啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "只要小船能帮上你们的忙就好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "下次希望你们\x01",
            "能来尽兴地玩一次。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F7")

    label("loc_12B2")


    ChrTalk(
        0xFE,
        (
            "是你们几个啊……\x01",
            "下次希望你们能来尽兴地玩一次。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F7")

    Jump("loc_1940")

    label("loc_12FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_184E")
    OP_A2(0x42B)
    OP_28(0x3C, 0x1, 0x10)
    EventBegin(0x0)
    OP_69(0xFE, 0x3E8)

    ChrTalk(
        0xFE,
        (
            "唔……？\x01",
            "怎么了，你们几个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F这船可以租给我们吗！？\x01",
            "我们急着要去对岸！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很遗憾，\x01",
            "这船已经被那个什么公爵给订下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他等一下好像要乘船戏水……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F怎、怎么会这样～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#043F拜托了……\x01",
            "请您一定要帮帮我们！\x02\x03",
            "如果我们不快点过去的话， \x01",
            "有个小男孩可能会遇到危险呢！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x136, 400)

    ChrTalk(
        0xFE,
        (
            "哎呀呀，别哭别哭。\x01",
            "一看到小姑娘哭我就想起自己孙女来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好了，船先借给你们吧。\x01",
            "总之救人要紧嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "快点上来开船吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#048F谢、谢谢您！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F老爷爷，谢谢您哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，反正我会跟公爵说\x01",
            "这船还在维修当中。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "小子，你会开船吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯，还可以。\x02\x03",
            "你们两个快上船吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6C(45000, 0)
    OP_6D(-740, -2260, 92790, 0)
    SetChrPos(0x1E, -810, -2850, 92590, 90)
    SetChrFlags(0x1E, 0x40)
    OP_A1(0x1E, 0x12)
    OP_72(0x12, 0x4)
    OP_72(0x12, 0x2)
    OP_71(0x12, 0x400)
    OP_71(0x12, 0x40)
    OP_48()
    Sleep(1)
    SetChrBattleFlags(0x0, 0x20)
    SetChrBattleFlags(0x1, 0x20)
    SetChrBattleFlags(0x2, 0x20)
    ClearChrFlags(0x0, 0x4)
    ClearChrFlags(0x1, 0x4)
    ClearChrFlags(0x2, 0x4)
    SetChrPos(0x102, 300, -2760, 92400, 45)
    SetChrPos(0x101, -980, -2750, 92300, 270)
    SetChrPos(0x136, -1000, -2750, 93000, 270)
    SetChrFlags(0x0, 0x20)
    SetChrFlags(0x1, 0x20)
    SetChrFlags(0x2, 0x20)
    ClearChrBattleFlags(0xA, 0x20)
    SetChrPos(0xA, -760, -2260, 94400, 180)

    def lambda_16E1():

        label("loc_16E1")

        TurnDirection(0xFE, 0x136, 0)
        OP_48()
        Jump("loc_16E1")

    QueueWorkItem2(0xA, 1, lambda_16E1)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_22(0x92, 0x0, 0x64)
    LoadEffect(0x4, "map\\\\mp013_00.eff")
    LoadEffect(0x5, "map\\\\mp013_01.eff")
    PlayEffect(0x4, 0x0, 0x1E, 0, 0, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x1E, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_179D():
        OP_8F(0xFE, 0xFFFFB334, 0xFFFFF63C, 0x16C2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_179D)
    Sleep(500)

    def lambda_17BD():
        OP_8F(0xFE, 0xFFFFB334, 0xFFFFF63C, 0x16C2E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_17BD)
    Sleep(500)

    def lambda_17DD():
        OP_8F(0xFE, 0xFFFFB334, 0xFFFFF63C, 0x16C2E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_17DD)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x92, 0x5A)
    Sleep(100)
    OP_24(0x92, 0x50)
    Sleep(100)
    OP_24(0x92, 0x46)
    Sleep(100)
    OP_24(0x92, 0x3C)
    Sleep(100)
    OP_24(0x92, 0x32)
    Sleep(100)
    OP_24(0x92, 0x28)
    Sleep(100)
    OP_24(0x92, 0x1E)
    Sleep(100)
    OP_23(0x92)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1940")

    label("loc_184E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_18AC")

    ChrTalk(
        0xFE,
        (
            "卢安很早以前\x01",
            "就被称为水上之都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "理由显而易见。\x01",
            "谁都能明白吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1940")

    label("loc_18AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_1916")

    ChrTalk(
        0xFE,
        (
            "今天的晚霞\x01",
            "依旧是这么美丽呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再没有什么地方比卢安\x01",
            "更加配得上晚霞的美景了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1940")

    label("loc_1916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1940")

    ChrTalk(
        0xFE,
        "怎么了，要坐船吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1940")

    TalkEnd(0xA)
    Return()

    # Function_6_EE2 end

    def Function_7_1944(): pass

    label("Function_7_1944")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1A39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F9")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "本酒店也为各位\x01",
            "准备了一艘小船，\x01",
            "大家可以泛舟眺望卢安的街道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请务必游览一下。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    Jump("loc_1A36")

    label("loc_19F9")


    ChrTalk(
        0xFE,
        (
            "很抱歉，请不要打扰我。\x01",
            "现在我正在招待旅客。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A36")

    Jump("loc_1C15")

    label("loc_1A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1AED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB9")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "嗯，下午的安排是\x01",
            "带客人们去参观艾尔·雷登……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为是以体味大海为主题的旅游，\x01",
            "晚饭还是在拉旺塔尔解决吧……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    Jump("loc_1AEA")

    label("loc_1AB9")


    ChrTalk(
        0xFE,
        (
            "很抱歉，\x01",
            "现在我正忙着呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AEA")

    Jump("loc_1C15")

    label("loc_1AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1C15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BD8")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "各位，请看一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在可以在我的左手边看到\x01",
            "海港都市卢安的标志——\x01",
            "伦格兰德大桥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "降下的时候，\x01",
            "开合桥的全长约为１０９亚矩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "将桥吊起的机器是\x01",
            "蔡斯中央工房制造的\x01",
            "特制导力引擎。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    Jump("loc_1C15")

    label("loc_1BD8")


    ChrTalk(
        0xFE,
        (
            "很抱歉，请不要打扰我。\x01",
            "现在我正在招待旅客。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C15")

    TalkEnd(0xD)
    Return()

    # Function_7_1944 end

    def Function_8_1C19(): pass

    label("Function_8_1C19")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1C9C")

    ChrTalk(
        0xFE,
        (
            "虽然马上就要到儿子学校的学园祭了，\x01",
            "但是我工作很忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不知道能不能请到假……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E16")

    label("loc_1C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1DC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5E")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "这里的灯塔是在大约４０年，\x01",
            "也就是和伦格兰德大桥\x01",
            "同时期建造起来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这也是这个城市\x01",
            "免遭战火摧残的建筑物之一。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    Jump("loc_1DC5")

    label("loc_1D5E")


    ChrTalk(
        0xFE,
        "今天放弃休假继续工作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女儿能够帮忙做家务\x01",
            "真是替我分忧了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC5")

    Jump("loc_1E16")

    label("loc_1DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1E16")

    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "然后就是带领各位去酒店了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E16")

    TalkEnd(0xE)
    Return()

    # Function_8_1C19 end

    def Function_9_1E1A(): pass

    label("Function_9_1E1A")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F88")
    OP_A2(0x2)
    OP_A2(0x3)

    ChrTalk(
        0x13,
        (
            "唔～\x01",
            "您的假牙就是掉在这附近的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "不素不素，\x01",
            "在靠今海便那里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "什么？在海面上？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "偶素说在海便！\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "唔……\x01",
            "我听不懂啊……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_1FCE")

    label("loc_1F88")


    ChrTalk(
        0xFE,
        (
            "这样的话，\x01",
            "我就跳下去一点一点找，\x01",
            "直到把假牙找回来！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCE")

    TalkEnd(0x13)
    Return()

    # Function_9_1E1A end

    def Function_10_1FD2(): pass

    label("Function_10_1FD2")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A1")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "好吧……\x01",
            "今天没什么事干，\x01",
            "就放松一下吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "人们一提到柏斯的商人，\x01",
            "总是说他们\x01",
            "日夜不停地工作工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要真是那样的话，\x01",
            "身体怎么可能受得了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DA")

    label("loc_20A1")


    ChrTalk(
        0xFE,
        (
            "好吧……\x01",
            "今天没什么事干，\x01",
            "就放松一下吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DA")

    TalkEnd(0x14)
    Return()

    # Function_10_1FD2 end

    def Function_11_20DE(): pass

    label("Function_11_20DE")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2168")

    ChrTalk(
        0xFE,
        (
            "接下来我打算\x01",
            "到蔡斯地区去钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是第一次去蔡斯，\x01",
            "不知道会钓到什么，真是期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2937")

    label("loc_2168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_234F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FF")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "即使在同一个钓鱼场，\x01",
            "按照同样的钓鱼方式，\x01",
            "也不见得就会钓到相同的猎物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "经常分析每天的状况，\x01",
            "从而得出自己的结论是非常有必要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个结论谁也不会告诉你。\x01",
            "要自己经常去探索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那才正是垂钓的\x01",
            "真正乐趣所在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……我的意思可不是说\x01",
            "这样就无法钓鱼了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234C")

    label("loc_22FF")


    ChrTalk(
        0xFE,
        (
            "……我的意思可不是说\x01",
            "这样就无法钓鱼了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_234C")

    Jump("loc_2937")

    label("loc_234F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_23C9")

    ChrTalk(
        0xFE,
        "唉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管名人怎么有名，\x01",
            "钓不到的时候就是钓不到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2937")

    label("loc_23C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_24BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2473")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "对垂钓来说，\x01",
            "地点的选择也是非常重要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在鱼游不到的地方\x01",
            "一直守着不动也是没有用的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B7")

    label("loc_2473")


    ChrTalk(
        0xFE,
        (
            "对垂钓来说，\x01",
            "地点的选择也是非常重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B7")

    Jump("loc_2937")

    label("loc_24BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_2547")

    ChrTalk(
        0xFE,
        (
            "嘘——！\x01",
            "请千万不要发出响声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为鱼对声音特别敏感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2937")

    label("loc_2547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_25F7")

    ChrTalk(
        0xFE,
        (
            "我不知道你们在急什么，\x01",
            "不过请千万不要发出响声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为鱼对声音特别敏感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2937")

    label("loc_25F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2765")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E3")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "今天的钓鱼成果只是一般啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "仅仅满足于此可不是我的风格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我一定会超过纪录，\x01",
            "钓到大鱼给你们看！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "赌上我们『钓公师团』的名声！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2762")

    label("loc_26E3")


    ChrTalk(
        0xFE,
        (
            "我一定会钓到一条大鱼，\x01",
            "破个纪录给你们看！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "赌上我们『钓公师团』的名声！\x02",
    )

    CloseMessageWindow()

    label("loc_2762")

    Jump("loc_2937")

    label("loc_2765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_2861")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2820")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "现在这个时候——\x01",
            "也就是傍晚时分，\x01",
            "正是鱼儿们特别活跃的时间呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "当然这也是鱼儿最容易上钩的时候哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯……\x02",
    )

    CloseMessageWindow()
    Jump("loc_285E")

    label("loc_2820")


    ChrTalk(
        0xFE,
        (
            "现在这个时候——\x01",
            "也就是傍晚时分，\x01",
            "正是鱼儿们特别活跃的时间呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_285E")

    Jump("loc_2937")

    label("loc_2861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2937")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F2")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "千里迢～迢\x01",
            "来到～这～水上之都～⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，在亚瑟利亚湾的某处\x01",
            "有一只传说中的庞然大物……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2937")

    label("loc_28F2")


    ChrTalk(
        0xFE,
        (
            "唔，在亚瑟利亚湾的某处\x01",
            "有一只传说中的庞然大物……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2937")

    TalkEnd(0x15)
    Return()

    # Function_11_20DE end

    def Function_12_293B(): pass

    label("Function_12_293B")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_29D0")

    ChrTalk(
        0xFE,
        (
            "在翻烂了导游手册之后，\x01",
            "我决定今天就在这儿吃饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "父亲和女儿对这里也很满意，\x01",
            "真让我高兴啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C22")

    label("loc_29D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_2A36")

    ChrTalk(
        0xFE,
        (
            "看着这座桥，\x01",
            "我再次感到导力器的发明\x01",
            "真的是太厉害了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C22")

    label("loc_2A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2AAC")

    ChrTalk(
        0xFE,
        "你们怎么了，这么慌张。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道说，\x01",
            "你们找刚才的男孩子有事？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C22")

    label("loc_2AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2B43")

    ChrTalk(
        0xFE,
        (
            "父亲不小心\x01",
            "把假牙掉到海里了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C22")

    label("loc_2B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD4")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "我带着父亲和女儿\x01",
            "来卢安旅游……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，但是我必须\x01",
            "随时盯住他们两个啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C22")

    label("loc_2BD4")


    ChrTalk(
        0xFE,
        (
            "如果没有我在的话，\x01",
            "真不知道会怎么样……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C22")

    TalkEnd(0xF)
    Return()

    # Function_12_293B end

    def Function_13_2C26(): pass

    label("Function_13_2C26")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2C48")

    ChrTalk(
        0xFE,
        "这还真是特等席啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D05")

    label("loc_2C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2C6F")

    ChrTalk(
        0xFE,
        "真是一座富有生命的桥！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D05")

    label("loc_2C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C88")
    TalkEnd(0x10)
    Call(0, 9)
    Jump("loc_2CC1")

    label("loc_2C88")


    ChrTalk(
        0xFE,
        (
            "真素的……\x01",
            "真不番便……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "偶地牙……\x02",
    )

    CloseMessageWindow()

    label("loc_2CC1")

    Jump("loc_2D05")

    label("loc_2CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2D05")

    ChrTalk(
        0xFE,
        (
            "哈哈，原来如此原来如此。\x01",
            "王国军也非常有创意嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D05")

    TalkEnd(0x10)
    Return()

    # Function_13_2C26 end

    def Function_14_2D09(): pass

    label("Function_14_2D09")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2D7B")

    ChrTalk(
        0xFE,
        (
            "啊，好舒服～！\x01",
            "要在这种地方吃饭吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟然知道这么好的饭店，\x01",
            "爸爸真是不赖！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E91")

    label("loc_2D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2D98")

    ChrTalk(
        0xFE,
        "真厉害，太厉害了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E91")

    label("loc_2D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2E54")

    ChrTalk(
        0xFE,
        (
            "在旅游中遇到困难的话，\x01",
            "还是要找游击士协会啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "在外国也没问题。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E91")

    label("loc_2E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2E91")

    ChrTalk(
        0xFE,
        (
            "爸爸他呀，\x01",
            "总是提不起劲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E91")

    TalkEnd(0x11)
    Return()

    # Function_14_2D09 end

    def Function_15_2E95(): pass

    label("Function_15_2E95")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2F40")

    ChrTalk(
        0xFE,
        (
            "一开始我就在热切期待了，\x01",
            "学园祭果然很有趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小摊上的食物\x01",
            "又便宜又好吃。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9D")

    label("loc_2F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2F9D")

    ChrTalk(
        0xFE,
        (
            "虽然我在明信片上看到过，\x01",
            "但这还是我第一次看到实物啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9D")

    TalkEnd(0x16)
    Return()

    # Function_15_2E95 end

    def Function_16_2FA1(): pass

    label("Function_16_2FA1")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_306D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3048")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "那出剧真是杰作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然最开始男女角色反串演出\x01",
            "有些让人感到奇怪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是马上就能被这个故事本身吸引住，\x01",
            "真是不可思议呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306A")

    label("loc_3048")


    ChrTalk(
        0xFE,
        "那出剧真是杰作。\x02",
    )

    CloseMessageWindow()

    label("loc_306A")

    Jump("loc_3094")

    label("loc_306D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3094")

    ChrTalk(
        0xFE,
        "这可真是壮观……\x02",
    )

    CloseMessageWindow()

    label("loc_3094")

    TalkEnd(0x17)
    Return()

    # Function_16_2FA1 end

    def Function_17_3098(): pass

    label("Function_17_3098")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_30C4")

    ChrTalk(
        0xFE,
        "街上在吵闹什么啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_30C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3116")

    ChrTalk(
        0xFE,
        (
            "如果随便借走那艘船的话，\x01",
            "估计会被骂的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_3116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_31C4")

    ChrTalk(
        0xFE,
        (
            "今天的弥撒，\x01",
            "卢安的市长也来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然是位非常\x01",
            "威严且沉着冷静的人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_31C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_31F3")

    ChrTalk(
        0xFE,
        "接下来去哪个地方看看呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_31F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3280")

    ChrTalk(
        0xFE,
        (
            "绀碧之空与海之缝隙中\x01",
            "漂浮着的白色街道……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "卢安真是个\x01",
            "美丽的城市啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_3280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_32CD")

    ChrTalk(
        0xFE,
        (
            "这里也残留着\x01",
            "百日战役的痕迹。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_32CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_334F")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "幸好我事先问了拉桥的时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没想到这么大的东西\x01",
            "也能动起来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_334F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3374")

    ChrTalk(
        0xFE,
        "嗯……这真厉害！\x02",
    )

    CloseMessageWindow()

    label("loc_3374")

    TalkEnd(0x18)
    Return()

    # Function_17_3098 end

    def Function_18_3378(): pass

    label("Function_18_3378")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_33B3")

    ChrTalk(
        0xFE,
        "是不是出什么事情了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_33B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_344D")

    ChrTalk(
        0xFE,
        (
            "如果要租船的话\x01",
            "应该到哪里去呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果去问游击士协会\x01",
            "他们会告诉我吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_344D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_349F")

    ChrTalk(
        0xFE,
        "真不愧是传说中的水之教会。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "非常浪漫呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_349F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_34D4")

    ChrTalk(
        0xFE,
        (
            "卢安这个地方\x01",
            "值得一看的地方还真多啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_34D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_353C")

    ChrTalk(
        0xFE,
        "在水上还真是不可思议……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得能从生活中解放自己，\x01",
            "这里给了我安逸祥和的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_353C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3583")

    ChrTalk(
        0xFE,
        (
            "虽然景色很漂亮，\x01",
            "但是也向人传达了悲惨的历史。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_3583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_35D1")

    ChrTalk(
        0xFE,
        (
            "伫立在夕阳中的\x01",
            "大桥的风景也非常美丽啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_35D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3603")

    ChrTalk(
        0xFE,
        "比想象中的要大呢……\x02",
    )

    CloseMessageWindow()

    label("loc_3603")

    TalkEnd(0x19)
    Return()

    # Function_18_3378 end

    def Function_19_3607(): pass

    label("Function_19_3607")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_36BD")

    ChrTalk(
        0xFE,
        (
            "《利贝尔通讯》\x01",
            "刊登的事情是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道市长\x01",
            "真的是纵火犯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然他平时的为人\x01",
            "并不是令人十分爱戴……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_36BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3701")

    ChrTalk(
        0xFE,
        (
            "港口的负责人波尔多斯\x01",
            "是一个非常有声望的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_3701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_3756")

    ChrTalk(
        0xFE,
        "已经这个时候了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "差不多该回家\x01",
            "准备晚饭了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_3756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_37E7")

    ChrTalk(
        0xFE,
        (
            "玛西亚孤儿院被人放火，\x01",
            "犯人真是过分了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那里的孩子们\x01",
            "好像和我的女儿差不多年龄呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_37E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_3881")

    ChrTalk(
        0xFE,
        (
            "刚才的那个男孩子……\x01",
            "他的妈妈好像来接他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然不知道发生了什么，\x01",
            "不过这样我就放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_3881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_38E6")

    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "有个男孩子飞奔过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生什么事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_38E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_397F")

    ChrTalk(
        0xFE,
        "最近，观光客增加了许多。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要仓库里那群家伙们\x01",
            "不要惹出什么麻烦来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_397F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_39DB")

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "已经到这个时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "赶快把东西买好，\x01",
            "然后回家吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_39DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3A77")

    ChrTalk(
        0xFE,
        (
            "空贼终于被抓住了，\x01",
            "我也回到了久违的故乡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然还是\x01",
            "卢安清爽的空气最宜人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A77")

    TalkEnd(0x1A)
    Return()

    # Function_19_3607 end

    def Function_20_3A7B(): pass

    label("Function_20_3A7B")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3AC4")

    ChrTalk(
        0xFE,
        "市长干了坏事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "市长不是个好人吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3B33")

    ChrTalk(
        0xFE,
        "我好期待下一次的主日学校。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "又可以见到朋友了，\x01",
            "而且神父也很有趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_3B64")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        "嘿嘿，今天玩得很尽兴哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_3C61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BFA")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "姐姐的制服，\x01",
            "看上去真是可爱呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#041F呵呵，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果主日学校\x01",
            "也有制服就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C5E")

    label("loc_3BFA")


    ChrTalk(
        0xFE,
        (
            "姐姐的制服，\x01",
            "看上去真是可爱呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果主日学校\x01",
            "也有制服就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C5E")

    Jump("loc_3D85")

    label("loc_3C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_3C8C")

    ChrTalk(
        0xFE,
        (
            "可不能让妈妈\x01",
            "为自己担心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD5")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        "喂！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在大街上这样奔跑\x01",
            "是很危险的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFF")

    label("loc_3CD5")


    ChrTalk(
        0xFE,
        (
            "在大街上这样奔跑\x01",
            "是很危险的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CFF")

    Jump("loc_3D85")

    label("loc_3D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3D37")

    ChrTalk(
        0xFE,
        (
            "不要一个人\x01",
            "到大桥的对面去哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_3D57")

    ChrTalk(
        0xFE,
        "我的肚子已经饿扁了～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3D85")

    ChrTalk(
        0xFE,
        "嘿嘿，我正在和妈妈一起玩呢㈱\x02",
    )

    CloseMessageWindow()

    label("loc_3D85")

    TalkEnd(0x1B)
    Return()

    # Function_20_3A7B end

    def Function_21_3D89(): pass

    label("Function_21_3D89")

    Call(0, 22)
    Return()

    # Function_21_3D89 end

    def Function_22_3D8E(): pass

    label("Function_22_3D8E")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3E11")

    ChrTalk(
        0x1C,
        (
            "如果就这样无所事事度过自己的一生，\x01",
            "那真是不幸啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "因此我们一定要\x01",
            "好好活下去才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_438A")

    label("loc_3E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3E71")

    ChrTalk(
        0x1C,
        (
            "……为什么在无法回来的时候\x01",
            "才会看到它的光芒呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_438A")

    label("loc_3E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_3F9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6A")
    OP_A2(0x4CB)

    ChrTalk(
        0x1C,
        (
            "我知道很唐突，\x01",
            "不过这本书还是送给你们吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x216, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "红耀石　第５卷\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x1C,
        "……问我为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "因为人生充满矛盾，\x01",
            "是非常捉摸不透的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F9A")

    label("loc_3F6A")


    ChrTalk(
        0x1C,
        "……在这里看夕阳真美。\x02",
    )

    CloseMessageWindow()

    label("loc_3F9A")

    Jump("loc_438A")

    label("loc_3F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4123")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4082")
    OP_A2(0xF)

    ChrTalk(
        0x1C,
        "……卢安是个很大的城市哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "众多来往的人们，\x01",
            "各自交错的人生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "在那之中，\x01",
            "有时候会觉得自己好像是一颗\x01",
            "被丢弃在路边的小石子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "这是为什么呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4120")

    label("loc_4082")


    ChrTalk(
        0x1C,
        (
            "众多来往的人们，\x01",
            "各自交错的人生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "在那之中，\x01",
            "有时候会觉得自己好像是一颗\x01",
            "被丢弃在路边的小石子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4120")

    Jump("loc_438A")

    label("loc_4123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_4187")

    ChrTalk(
        0x1C,
        (
            "蓝天的彼方，\x01",
            "星星是否在闪耀呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "……啊啊，太远了，我看不到。\x02",
    )

    CloseMessageWindow()
    Jump("loc_438A")

    label("loc_4187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_42B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_426B")
    OP_A2(0xF)

    ChrTalk(
        0x1C,
        "鸟啊，鸟儿们啊，你们飞向哪里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "展开庞大的翅膀，\x01",
            "向着未知的大地飞去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "在天空之中\x01",
            "它们显得如此渺小，\x01",
            "却又为何是如此坚强的生物呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "我也想像它们那样\x01",
            "自由自在地生活啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42B4")

    label("loc_426B")


    ChrTalk(
        0x1C,
        "鸟啊，鸟儿们啊，你们飞向哪里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "我也想像它们那样\x01",
            "自由自在地生活啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42B4")

    Jump("loc_438A")

    label("loc_42B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_4351")

    ChrTalk(
        0x1C,
        (
            "啊啊……\x01",
            "我仿佛要被夕阳射穿了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "不行，太耀眼了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_438A")

    label("loc_4351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_438A")

    ChrTalk(
        0x1C,
        (
            "呵呵……\x01",
            "欢迎来到水上之都。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_438A")

    TalkEnd(0x1C)
    Return()

    # Function_22_3D8E end

    def Function_23_438E(): pass

    label("Function_23_438E")

    EventBegin(0x0)
    OP_67(0, 5600, -10000, 0)
    OP_6C(315000, 0)
    OP_6B(6800, 0)
    OP_6D(52424, 0, 68700, 0)
    StopSound(0x9470, 0x30D40, 0x0)
    SetChrPos(0x101, 25470, 0, 115060, 180)
    SetChrPos(0x102, 24790, 0, 116060, 180)
    SetChrPos(0x136, 26160, 0, 116640, 180)

    def lambda_440A():
        OP_6C(45000, 13000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_440A)
    Sleep(5000)

    def lambda_441F():
        OP_67(0, 9500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_441F)

    def lambda_4437():
        OP_6B(2800, 8000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4437)

    def lambda_4447():
        OP_6D(25850, 0, 115000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4447)
    StopSound(0x9470, 0x14C08, 0x1F40)
    Sleep(8000)

    ChrTalk(
        0x101,
        (
            "#501F哇～……\x01",
            "这里就是卢安市啊。\x02\x03",
            "真是个好漂亮的城市呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F蓝色的大海，白色的建筑……\x01",
            "真是眩目的对比。\x02\x03",
            "的确是海港都市的感觉。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(
        0x136,
        (
            "#041F呵呵，\x01",
            "这里有很多值得一看的地方呢。\x02\x03",
            "这附近就有一个\x01",
            "竖立着灯台的海边小公园。\x02\x03",
            "街道后面就是教堂，\x01",
            "那里的建筑风格也十分独特。\x02\x03",
            "#040F还有，最值得一看的地方\x01",
            "也许就要数『伦格兰德大桥』了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_462F():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_462F)
    Sleep(200)

    def lambda_4642():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4642)
    Sleep(400)

    ChrTalk(
        0x101,
        "#000F#4P『伦格兰德大桥』？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F是连接这里\x01",
            "与对岸南街区的大桥。\x02\x03",
            "那是一座\x01",
            "装有卷轴装置的开合桥哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3P开合桥吗……\x01",
            "听起来挺有意思的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F对了，\x01",
            "游击士协会就在这个北街区的中央。\x02\x03",
            "正好在大桥的前面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4PＯＫ～\x01",
            "就先去那边看看吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_23_438E end

    def Function_24_47C5(): pass

    label("Function_24_47C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_495D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48E2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x445)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    TurnDirection(0x136, 0x0, 400)

    ChrTalk(
        0x136,
        (
            "#040F啊，游击士协会支部就在这个街区。\x01",
            "　\x02\x03",
            "看，就是那幢建筑物。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x136, 0, 400)

    def lambda_4854():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4854)

    def lambda_4862():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4862)

    def lambda_4870():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_4870)
    OP_6D(44460, 0, 92190, 4000)

    ChrTalk(
        0x101,
        "#501F#1P啊，真的呢。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_69(0x0, 0x0)
    OP_4F(0x64, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(
        0x102,
        "#010F我们赶快过去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4942")

    label("loc_48E2")

    EventBegin(0x1)
    TurnDirection(0x136, 0x0, 400)

    ChrTalk(
        0x136,
        (
            "#040F游击士协会支部就在这个街区。\x01",
            "　\x02\x03",
            "就是那幢建筑物。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4942")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_495D")

    Return()

    # Function_24_47C5 end

    def Function_25_495E(): pass

    label("Function_25_495E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DEE")
    OP_A2(0x415)
    EventBegin(0x0)
    OP_51(0x136, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x136, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        (
            "#004F呜哇……\x01",
            "这就是伦格兰德大桥吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_49DE():
        OP_6C(90000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_49DE)

    def lambda_49EE():
        OP_67(0, 6115, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49EE)

    def lambda_4A06():
        OP_6B(7760, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A06)

    def lambda_4A16():
        OP_6D(51680, 400, 52400, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4A16)
    StopSound(0x9470, 0x3D090, 0x1770)
    OP_8C(0x102, 270, 400)

    def lambda_4A42():
        OP_8C(0x136, 270, 400)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_4A42)
    Sleep(9000)
    Fade(1000)
    OP_6C(45000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6D(48350, 400, 52340, 0)
    StopSound(0x9470, 0x14C08, 0x0)
    SetChrPos(0x101, 49512, 400, 51770, 270)
    SetChrPos(0x102, 49512, 400, 50400, 270)
    SetChrPos(0x136, 49512, 400, 53040, 270)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#501F真的是好大哦。\x01",
            "恐怕有威尔特桥的几倍大呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(
        0x136,
        (
            "#040F听说这座桥是在\x01",
            "大约４０年前建造的。\x02\x03",
            "在那之前，\x01",
            "这里的市民一直是用渡船来往于两岸的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        (
            "#004F哎……？\x01",
            "那为什么不早点建座大桥呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F是因为卢比诺川是连接\x01",
            "大海与瓦雷利亚湖的唯一河流吧。\x02\x03",
            "要是去位于湖畔的王都时，\x01",
            "船被大桥挡住可就糟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F没错，完全正确。\x02\x03",
            "直到５０年前，\x01",
            "因为导力革命的出现，\x01",
            "才让建造这种大规模的开合桥成为了可能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F原来是这样啊……\x01",
            "导力器真是神通广大。\x02\x03",
            "#001F话说回来，\x01",
            "真想亲眼看看这桥被分开的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F这座开合桥\x01",
            "每天会按时分离三次。\x02\x03",
            "从现在算起的话……\x01",
            "我想到傍晚就可以看见了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F好～吧，\x01",
            "到时候我们一定要来这看看哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F是啊。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_4DEE")

    Return()

    # Function_25_495E end

    def Function_26_4DEF(): pass

    label("Function_26_4DEF")

    EventBegin(0x0)
    OP_6D(45290, 0, 87610, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 45000, 500, 91157, 0)
    SetChrPos(0x102, 45000, 500, 91157, 0)
    SetChrPos(0x136, 45000, 500, 91157, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_43(0x101, 0x1, 0x0, 0x1B)
    OP_43(0x102, 0x1, 0x0, 0x1C)
    OP_43(0x136, 0x1, 0x0, 0x1D)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x136, 0x1)

    ChrTalk(
        0x101,
        (
            "#501F哇，已经傍晚了……\x02\x03",
            "#001F看看，好漂亮的夕阳呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这里的夕阳很特别，\x01",
            "与白色的街道相映生辉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F呵呵，我也很喜欢呢。\x02\x03",
            "#040F对了……\x01",
            "我想差不多该到时间了哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x136, 400)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        "#004F哎？到什么时间？\x02",
    )

    CloseMessageWindow()
    OP_22(0x94, 0x1, 0x64)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6F(0x11, 0)
    Fade(1000)
    OP_67(0, 6115, -10000, 0)
    OP_6B(7760, 0)
    OP_6D(51680, 400, 52400, 0)
    OP_6C(36000, 0)
    StopSound(0x9470, 0x3D090, 0x0)
    Sleep(1500)
    OP_22(0x93, 0x1, 0x64)
    OP_70(0x11, 0x3E8)
    OP_6C(315000, 18000)
    OP_73(0x11)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x93)
    OP_23(0x94)
    OP_6F(0x11, 1000)
    OP_70(0x11, 0x3FC)
    Sleep(1000)
    Fade(1000)
    OP_6C(315000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    StopSound(0x9470, 0x14C08, 0x1F40)
    OP_6D(58250, -1800, 70690, 0)
    SetChrPos(0x101, 59330, -1800, 70537, 180)
    SetChrPos(0x102, 58480, -1800, 70537, 180)
    SetChrPos(0x136, 60300, -1800, 70537, 180)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#501F#3P哇～好精彩的压轴戏啊。\x02\x03",
            "对了对了，\x01",
            "开合桥分开的状态会维持多久呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F#4P应该是３０分钟左右。\x02\x03",
            "清晨、上午、傍晚共３次，\x01",
            "一直到所有的船都通过为止。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P原来如此，\x01",
            "是选择了来往行人比较少的时间段啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F#4P呵呵，刚到这里的人\x01",
            "最初都会有点摸不着规律呢。\x02\x03",
            "#044F啊，说起来……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 400)
    Sleep(400)

    ChrTalk(
        0x136,
        (
            "#040F#4P艾丝蒂尔你们\x01",
            "今晚住在哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x136, 400)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        (
            "#000F#3P嗯～这个嘛……\x01",
            "其实我们原定住在协会的二楼的。\x02\x03",
            "不过刚来这几天，\x01",
            "我还是想找家酒店好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F#4P这样的话，\x01",
            "那你们快点去订个房间比较好。\x02\x03",
            "因为现在是旅游旺季，\x01",
            "我想酒店很快就会住满人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P这样啊……\x01",
            "看来要快点才行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#3P嗯，现在去酒店吧。\x02",
    )

    CloseMessageWindow()
    OP_72(0x1A, 0x2)
    EventEnd(0x0)
    Return()

    # Function_26_4DEF end

    def Function_27_5434(): pass

    label("Function_27_5434")

    OP_8E(0xFE, 0xB0B8, 0x0, 0x158F6, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xB3EC, 0x0, 0x154B4, 0xBB8, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_27_5434 end

    def Function_28_5467(): pass

    label("Function_28_5467")

    Sleep(300)
    OP_8E(0xFE, 0xB0B8, 0x0, 0x158F6, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xAEE2, 0x0, 0x154B4, 0xBB8, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_28_5467 end

    def Function_29_549F(): pass

    label("Function_29_549F")

    Sleep(600)
    OP_8E(0xFE, 0xB0B8, 0x0, 0x158F6, 0xBB8, 0x0)
    OP_72(0x5, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x5, 30)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    OP_71(0x5, 0x800)
    Return()

    # Function_29_549F end

    def Function_30_54D9(): pass

    label("Function_30_54D9")

    EventBegin(0x0)
    OP_6D(24380, 0, 94810, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 24040, 0, 94400, 90)
    SetChrPos(0x102, 23870, 0, 93300, 90)
    SetChrPos(0x136, 25410, 0, 93880, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x136,
        (
            "#040F#4P今天能让我陪着你们，\x01",
            "我真是十分感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#1P啊哈哈，别这么说嘛。\x01",
            "应该是我们多谢你才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#1P说得没错。\x01",
            "谢谢你带我们参观了这么多好地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#045F#4P你们太客气了，而且我又没做什么。\x02\x03",
            "#040F对了，\x01",
            "你们两个会在卢安呆上一段时间吧？\x02\x03",
            "如果你们不介意的话，\x01",
            "可以来参加下周末的学园祭吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P学园祭？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P这个名字听起来\x01",
            "似乎是某种活动吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F#4P嗯，是获得校方许可的\x01",
            "由学生自发组织和筹办的活动。\x02\x03",
            "这可是王立学院的传统活动哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#1P啊，学生活动……\x01",
            "听起来真的挺有趣呢！\x02\x03",
            "#001F会有货摊和节目表演吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F#4P呵呵，当然了。\x01",
            "而且都是很正规的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#1P我去我去，绝～对要去！\x02\x03",
            "其实我很想和你们\x01",
            "一起为学园祭做准备呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018F#3P我说艾丝蒂尔……\x02\x03",
            "刚刚嘉恩先生才说了我们可能会很忙，\x01",
            "你这么快就忘了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#007F哦哦，还有这档子事啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#3P不过，只是学园祭当天去的话，\x01",
            "倒也刚好可以作为休息的节目……\x02\x03",
            "在那之前先好好工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#2P哦～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#045F#4P呵呵……\x02\x03",
            "#048F艾丝蒂尔、约修亚。\x01",
            "那么我这就告辞了。\x02\x03",
            "过两天再见……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        "#006F#1P嗯，再见！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x136, 400)

    ChrTalk(
        0x102,
        "#010F#1P路上小心。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x136, 0, 400)

    def lambda_5AF0():
        OP_6D(25200, 0, 97530, 2000)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_5AF0)

    def lambda_5B08():

        label("loc_5B08")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_5B08")

    QueueWorkItem2(0x101, 2, lambda_5B08)

    def lambda_5B19():

        label("loc_5B19")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_5B19")

    QueueWorkItem2(0x102, 2, lambda_5B19)
    OP_8E(0x136, 0x6608, 0x0, 0x1AB94, 0xBB8, 0x0)
    SetChrFlags(0x136, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_5B4B():
        OP_6D(23990, 0, 93830, 1500)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_5B4B)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)
    WaitChrThread(0x136, 0x2)

    ChrTalk(
        0x101,
        (
            "#501F嗯～真的是个惹人怜爱的女孩子，\x01",
            "而且又有正义感，给人一种靠得住的感觉。\x02\x03",
            "我要是男孩子的话，\x01",
            "毫无疑问一定会喜欢上她的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F嗯，这个暂且不说……\x02\x03",
            "#010F不像有什么企图的样子，\x01",
            "看得出她的确是个好女孩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F那还用说。\x01",
            "她又不是那个傲慢的女空贼。\x02\x03",
            "#000F不过，既认识了好朋友，\x01",
            "又订到了酒店顶楼的好房间……\x02\x03",
            "#001F在玛诺利亚村的瞭望台上看见了基库，\x01",
            "果然是件好事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F呵呵，也许吧。\x02\x03",
            "#010F……那么，\x01",
            "我们先回房间整理一下行李吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，是顶楼呢⊙\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x136, 0x80)
    SetChrPos(0x136, 27020, 0, 94830, 180)
    EventEnd(0x0)
    RemoveParty(0x35, 0xFF)
    Return()

    # Function_30_54D9 end

    def Function_31_5DF5(): pass

    label("Function_31_5DF5")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 9880, 4200, 91480, 270)
    SetChrPos(0x102, 10260, 4200, 92590, 270)
    OP_6D(-10010, 4200, 90430, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    StopSound(0x9470, 0x186A0, 0x0)
    FadeToBright(2000, 0)
    OP_6D(10690, 4200, 93000, 5000)

    ChrTalk(
        0x102,
        (
            "#014F#1P真壮观啊……\x01",
            "居然还有这么漂亮的露台。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯……真的是绝佳的风景呢。\x02\x03",
            "#007F不过，这房间光我们两个住，\x01",
            "我觉得真是有点太浪费呢……\x02\x03",
            "#003F……要是老爸也在的话，\x01",
            "那该多好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#1P是啊……\x02\x03",
            "#015F父亲他在哪里，\x01",
            "现在又在做些什么呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x12, 12770, 4200, 93110, 0)

    NpcTalk(
        0x12,
        "男性的声音",
        (
            "#3P呵呵……\x01",
            "这房间倒是很不错嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F刚才那是……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F#1P嗯，\x01",
            "似乎是从房间里传来的声音……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_21()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2132   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_5DF5 end

    def Function_32_607F(): pass

    label("Function_32_607F")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(24130, 0, 93980, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 23540, 0, 94500, 90)
    SetChrPos(0x102, 23610, 0, 93330, 45)
    SetChrPos(0x8, 25170, 0, 94000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8)
    FadeToDark(0, 0, -1)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_22(0xD, 0x0, 0x64)
    Sleep(5000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "——次日早晨，卢安市街道。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    OP_1D(0xC)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x1C5, 0x1, 0x64)

    ChrTalk(
        0x8,
        (
            "#145F哈～～～～～欠……\x02\x03",
            "头好痛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F真是标准的宿醉啊。\x02\x03",
            "明明没酒量，\x01",
            "却偏要喝那么多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F要我去买点药来吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#142F不用……没事。\x02\x03",
            "好了， \x01",
            "我要去取材了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F这样啊……\x01",
            "#001F多谢你昨天让我们留宿哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F也非常感谢您请我们吃饭。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#141F小意思，要是有什么有趣的新闻，\x01",
            "你们可要记得告诉我啊……\x02\x03",
            "我最近也会呆在卢安的……\x01",
            "　\x02\x03",
            "#145F那么，干活去了～……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 300)

    def lambda_63DD():
        OP_6D(25330, 0, 91170, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_63DD)

    def lambda_63F5():

        label("loc_63F5")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_63F5")

    QueueWorkItem2(0x101, 2, lambda_63F5)

    def lambda_6406():

        label("loc_6406")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_6406")

    QueueWorkItem2(0x102, 2, lambda_6406)
    OP_8E(0x8, 0x6662, 0x0, 0x16058, 0x7D0, 0x0)
    OP_8E(0x8, 0x7814, 0x0, 0x14E92, 0x7D0, 0x0)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    Sleep(200)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Sleep(300)

    def lambda_6461():
        OP_6D(23600, 0, 93950, 1200)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6461)
    TurnDirection(0x102, 0x101, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(
        0x102,
        (
            "#010F好了，\x01",
            "我们也差不多该去协会了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F嗯，好啊。\x02\x03",
            "去嘉恩哥哥那看看有什么工作。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x8)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1B, 0x8)
    EventEnd(0x0)
    Return()

    # Function_32_607F end

    def Function_33_6512(): pass

    label("Function_33_6512")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 25470, 0, 115060, 180)
    SetChrPos(0x102, 24790, 0, 116060, 180)
    SetChrPos(0x136, 26160, 0, 116640, 180)
    OP_6C(45000, 0)
    OP_6D(25850, 0, 115000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#003F#4P……街道上不见那孩子啊。\x02\x03",
            "难道已经闯到了\x01",
            "那帮流氓的地盘里去吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F总之赶快去南街区的仓库吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x3C, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_33_6512 end

    def Function_34_6612(): pass

    label("Function_34_6612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B09")
    OP_A2(0x42A)
    OP_28(0x3C, 0x1, 0x4)
    OP_28(0x3C, 0x1, 0x8)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_22(0x94, 0x1, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x136, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#012F糟了，已经是晌午了……！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    ClearChrFlags(0x9, 0x80)
    Fade(1000)
    SetChrPos(0x9, 50820, 400, 57120, 0)
    OP_6C(45000, 0)
    OP_6D(50820, 400, 50000, 0)

    def lambda_66ED():
        OP_6D(50820, 200, 35000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_66ED)
    OP_8E(0x9, 0xC684, 0xC8, 0x922C, 0x1770, 0x0)
    OP_43(0x9, 0x3, 0x0, 0x23)

    def lambda_6720():
        OP_8E(0x9, 0xC684, 0xC8, 0x6590, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6720)
    Sleep(2000)

    def lambda_6740():
        OP_6D(50890, 0, 70000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6740)
    Sleep(1000)
    SetChrPos(0x101, 50210, 0, 90000, 180)
    SetChrPos(0x102, 51440, 0, 90000, 180)
    SetChrPos(0x136, 50920, 0, 90000, 225)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x136, 0x40)

    def lambda_679F():
        OP_8E(0xFE, 0xC6E8, 0x0, 0x1145E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_679F)
    Sleep(200)

    def lambda_67BF():
        OP_8E(0xFE, 0xC422, 0x0, 0x119AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67BF)
    Sleep(200)

    def lambda_67DF():
        OP_8E(0xFE, 0xC8F0, 0x0, 0x11986, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_67DF)
    OP_6C(135000, 3600)
    SetChrFlags(0x9, 0x80)

    ChrTalk(
        0x136,
        (
            "#043F#2P啊啊……！\x02\x03",
            "克拉姆，等等！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#1P没用的……\x01",
            "看来他根本听不见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#4P真是的！\x01",
            "桥怎么偏偏在这种时候分开！\x02\x03",
            "这下要足足等３０分钟啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#049F#2P怎能这样呢……\x01",
            "这样下去的话，那孩子……\x02\x03",
            "怎么办……该怎么办才好……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x136, 400)

    ChrTalk(
        0x102,
        (
            "#012F#1P科洛丝，冷静点。\x02\x03",
            "你忘记了吗？\x01",
            "昨天你还告诉过我们的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x102, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x136,
        "#044F#2P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P这座桥还未建成的时候，\x01",
            "是用什么工具来往于两岸的？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x136, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#4P啊，是小船！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#042F#2P……对了！\x02\x03",
            "我记得酒店后面\x01",
            "好像有出租用的小船！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        (
            "#006F#4P好极了！\x01",
            "就乘那个去对岸吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x1A, 0x2)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x136, 0x40)
    EventEnd(0x0)

    label("loc_6B09")

    Return()

    # Function_34_6612 end

    def Function_35_6B0A(): pass

    label("Function_35_6B0A")

    OP_22(0x93, 0x1, 0x64)
    OP_70(0x11, 0x3E8)
    OP_73(0x11)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x93)
    OP_23(0x94)
    OP_6F(0x11, 1000)
    OP_70(0x11, 0x3FC)
    Return()

    # Function_35_6B0A end

    def Function_36_6B33(): pass

    label("Function_36_6B33")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 24790, 0, 116060, 180)
    SetChrPos(0x9, 26160, 0, 116640, 180)
    SetChrPos(0x101, 24790, 0, 114060, 0)
    SetChrPos(0x105, 26160, 0, 114640, 0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 26225, 0, 104380, 0)
    OP_6C(45000, 0)
    OP_6D(25850, 0, 115000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#750F#1P真是太感谢各位了。\x01",
            "都不知该怎么报答你们才好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F不用这么客气啦。\x01",
            "这也是我们份内的工作嘛。\x02\x03",
            "#000F话说回来，真的不用我们\x01",
            "送你们回玛诺利亚村吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#751F嗯，没问题的。\x01",
            "梅威海道就像我家的花园一样。\x02\x03",
            "如果再继续给你们添麻烦的话，\x01",
            "恐怕就要受到天罚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F其实不用介意啦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F老师……至少让我陪你们回去吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#750F呵呵，\x01",
            "你就继续专心准备学园祭的事情吧。\x02\x03",
            "而且， \x01",
            "这些孩子也都很期待你的表演哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F……是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1P太好了，赶上了。\x02",
    )

    CloseMessageWindow()

    def lambda_6E80():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E80)

    def lambda_6E8E():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6E8E)
    OP_8E(0x102, 0x6504, 0x0, 0x1B968, 0xFA0, 0x0)
    ClearChrFlags(0x102, 0x4)

    ChrTalk(
        0x102,
        "#010F船已经还回去了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊，谢了☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F真不好意思……\x01",
            "让你自己一个人去还。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F别客气。\x01",
            "又不是什么麻烦事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#750F约修亚……\x01",
            "这次真是太感谢你了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F93():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F93)
    TurnDirection(0x105, 0x9, 400)

    ChrTalk(
        0x9,
        (
            "#775F科洛丝姐姐……\x02\x03",
            "还有艾丝蒂尔姐姐和\x01",
            "约修亚哥哥……\x02\x03",
            "今天真是谢谢你们。\x01",
            "谢谢你们救了我。\x02\x03",
            "我……真的是个笨蛋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F克拉姆……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#773F明明一点本事都没有，\x01",
            "却硬着头皮去报仇……\x02\x03",
            "最后反而要\x01",
            "姐姐你们来救我……\x02\x03",
            "#777F真是……太丢脸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F没、没这回事呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F我觉得一点都不丢脸。\x02",
    )

    CloseMessageWindow()

    def lambda_70FF():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_70FF)

    def lambda_710D():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_710D)

    def lambda_711B():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_711B)

    def lambda_7129():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7129)

    ChrTalk(
        0x9,
        "#777F哎……？\x02",
    )

    CloseMessageWindow()

    def lambda_7148():
        OP_6D(25850, 0, 117000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7148)

    def lambda_7160():

        label("loc_7160")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_7160")

    QueueWorkItem2(0x9, 1, lambda_7160)

    def lambda_7171():

        label("loc_7171")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_7171")

    QueueWorkItem2(0xB, 1, lambda_7171)

    def lambda_7182():

        label("loc_7182")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_7182")

    QueueWorkItem2(0x101, 1, lambda_7182)

    def lambda_7193():

        label("loc_7193")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_7193")

    QueueWorkItem2(0x105, 1, lambda_7193)
    OP_8E(0x102, 0x6A2C, 0x0, 0x1BE04, 0xBB8, 0x0)
    OP_8E(0x102, 0x6932, 0x0, 0x1C642, 0xBB8, 0x0)
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x102,
        (
            "#010F为了保护自己身边重要的人，\x01",
            "奋不顾身挺身而出……\x02\x03",
            "这种事有时候\x01",
            "连大人都不一定做得到。\x02\x03",
            "#019F所以我觉得\x01",
            "你的勇气真的非常可嘉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#775F#1P约修亚哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F只不过，搜捕犯人和\x01",
            "惩治犯人这种事可以由我们来做。\x02\x03",
            "而你，应该用自己力所能及的方法，\x01",
            "去保护老师和其他孩子。\x02\x03",
            "陪在他们身边、互相帮忙、\x01",
            "互相鼓励、成为大家信赖的伙伴。\x02\x03",
            "#011F克拉姆……\x01",
            "这是只有你才做得到的事哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#774F#1P…………………………\x02\x03",
            "只有我才做得到的事……\x02\x03",
            "#770F嗯，知道了。\x01",
            "我明白哥哥的意思了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F怎么样，能做到吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#771F#1P那当然啦！\x01",
            "就包在我身上吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7441():

        label("loc_7441")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7441")

    QueueWorkItem2(0x102, 1, lambda_7441)

    def lambda_7452():

        label("loc_7452")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7452")

    QueueWorkItem2(0x101, 1, lambda_7452)

    def lambda_7463():

        label("loc_7463")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7463")

    QueueWorkItem2(0x105, 1, lambda_7463)

    ChrTalk(
        0xB,
        (
            "#751F呵呵，太好了。\x01",
            "真的是太谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xB, 0xFF)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "#750F那么各位，\x01",
            "我们这就告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    TurnDirection(0x9, 0x105, 400)

    ChrTalk(
        0x9,
        (
            "#770F#1P啊，科洛丝姐姐！\x01",
            "我等着看你的舞台剧哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F嗯，我会加油的，\x01",
            "大家要一起来看哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#770F#1P那当然啦！\x02\x03",
            "#771F再见，哥哥姐姐！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 0, 400)

    def lambda_75B1():
        OP_8E(0xFE, 0x60E0, 0x0, 0x207C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_75B1)
    OP_8C(0x9, 0, 400)

    def lambda_75D3():
        OP_8E(0xFE, 0x6590, 0x0, 0x207C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_75D3)
    Sleep(4000)

    ChrTalk(
        0x101,
        (
            "#007F#3P呼～太好了。\x01",
            "总算又打起精神来了……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F#3P约修亚你呀，\x01",
            "什么时候都那么会说话㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x105, 0xFF)

    def lambda_7689():

        label("loc_7689")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_7689")

    QueueWorkItem2(0x105, 1, lambda_7689)

    ChrTalk(
        0x105,
        (
            "#048F呵呵，我也吃了一惊呢。\x01",
            "那孩子这么快又活泼起来了。\x02\x03",
            "#041F约修亚……\x01",
            "真的是太谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#1P不……\x01",
            "其实我又没说什么了不起的话。\x02\x03",
            "#013F保护身边重要的人……吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 270, 400)

    def lambda_77C1():
        OP_6D(25400, 0, 115000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_77C1)
    OP_8E(0x102, 0x61A8, 0x0, 0x1C3E0, 0x7D0, 0x0)
    OP_44(0x102, 0xFF)
    OP_8C(0x102, 180, 400)
    OP_44(0x105, 0xFF)
    OP_8C(0x105, 270, 0)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x102,
        (
            "#010F#1P总之，\x01",
            "那孩子没事真是太好了。\x02\x03",
            "科洛丝，谢谢你帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F怎能这样呢……\x01",
            "其实该道谢的是我才对。\x02\x03",
            "#044F啊，说起来……\x02\x03",
            "不知道对那些人的调查\x01",
            "进行得怎样了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，那个阿加特说了\x01",
            "会好好审问那些家伙的。\x02\x03",
            "不知道有没有结果了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P总之，先回协会去吧。\x02\x03",
            "科洛丝也一起来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F嗯，可以的话，\x01",
            "我也想知道真相到底是怎样的。\x02\x03",
            "犯人究竟是什么人呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F那么，我们出发吧！\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_36_6B33 end

    def Function_37_79FC(): pass

    label("Function_37_79FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_808E")
    OP_A2(0x450)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_808E")
    EventBegin(0x0)
    OP_44(0xE, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0xF, 0xFF)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0xF, 0)

    def lambda_7A3B():
        OP_6D(18500, 0, 73800, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A3B)

    def lambda_7A53():
        OP_6C(225000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A53)
    Sleep(3000)
    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "……这里就是为了纪念\x01",
            "百日战役结束而建造的公园。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "嗯……那么，\x01",
            "现在考大家一个问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "众所周知，\x01",
            "沿着这条卢比诺川溯流而上，\x01",
            "就可以通到座落于湖畔的王都。\x02\x03",
            "在百日战役的时候，\x01",
            "为了防止帝国海军的入侵，\x01",
            "王国军曾在这里采取了一项措施。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "有谁知道那项措施究竟是什么呢？\x02",
    )

    CloseMessageWindow()
    OP_95(0x10, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x10,
        "我！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "好，请回答！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "嘿嘿，\x01",
            "这个我知道哦。\x02\x03",
            "他们在卢安市里\x01",
            "调集了很多大炮对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "唔～答错了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "当时的确调集了很多大炮过来，\x01",
            "但由于帝国的攻击太猛烈了，\x01",
            "所以没能来得及装上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "给大家一点提示吧。\x01",
            "是更直接有效的措施哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D48():
        OP_95(0x11, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7D48)
    Sleep(10)
    OP_8C(0x11, 30, 2200)
    OP_8C(0x11, 150, 2200)
    OP_8C(0x11, 270, 2200)
    OP_8C(0x11, 30, 2200)
    OP_8C(0x11, 150, 2200)
    OP_8C(0x11, 270, 2200)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x11,
        "我知道我知道！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "好的。\x01",
            "那位小姐，请回答！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "是不是炸沉了\x01",
            "那座伦格兰德大桥啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "啊啊，可惜！\x01",
            "答案完～全不对啊！\x02\x03",
            "当时大桥一直处于分离状态，\x01",
            "听说是导力器发生故障了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x11,
        "嘁～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "公布正确答案～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "其实是调集了许多已经要废弃的船，\x01",
            "然后让它们从上游顺流而下，\x01",
            "最后在河口将它们炸沉。\x02\x03",
            "因为河口变浅了，\x01",
            "所以帝国军就无法\x01",
            "由卢比诺川入侵王都了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "啊～真厉害，\x01",
            "不过这么做好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "怎么说这也有点过激了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "那么接下来，\x01",
            "大家可以自由活动。\x02\x03",
            "在规定的时间之前，\x01",
            "就请在附近好好游览一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_85(0xE)
    OP_85(0x10)
    OP_85(0x11)
    OP_85(0xF)
    EventEnd(0x0)

    label("loc_808E")

    Return()

    # Function_37_79FC end

    def Function_38_808F(): pass

    label("Function_38_808F")

    EventBegin(0x0)
    LoadEffect(0x4, "map\\\\mp013_00.eff")
    LoadEffect(0x5, "map\\\\mp013_01.eff")
    OP_22(0x94, 0x1, 0x64)
    PlayEffect(0x4, 0x4, 0x1F, 0, 50, 2700, 180, 0, 0, 2500, 500, 10000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x1E, 0, 50, 2400, 180, 0, 0, 1600, 500, 10000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x1F, 0, -300, -3000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x1E, 0, -300, -1800, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x18, 0x2)
    OP_71(0x18, 0x20)
    OP_71(0x18, 0x40)
    OP_6F(0x18, 301)
    OP_70(0x18, 0x168)
    OP_72(0x19, 0x2)
    OP_71(0x19, 0x20)
    OP_71(0x19, 0x40)
    OP_6F(0x19, 301)
    OP_70(0x19, 0x168)
    ClearChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x20)
    OP_89(0x1D, 89820, -2850, 52390, 270)
    SetChrPos(0x101, 98260, -1000, 52020, 270)
    SetChrPos(0x102, 100490, -1000, 51980, 90)
    SetChrPos(0x105, 99510, -1000, 52230, 270)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x101, 17)
    SetChrChipByIndex(0x102, 18)
    SetChrChipByIndex(0x105, 19)
    OP_A1(0x1F, 0x18)
    OP_A1(0x1E, 0x19)
    SetChrPos(0x1F, 90000, -3000, 53000, 90)
    SetChrPos(0x1E, 100000, -3000, 52000, 90)
    FadeToBright(2000, 0)
    OP_6D(50010, 400, 40640, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(336000, 0)
    OP_6E(371, 0)
    SetChrPos(0x11, 52500, 400, 59820, 90)
    SetChrPos(0xF, 51400, 400, 60600, 90)
    SetChrPos(0x10, 52190, 400, 58970, 90)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    def lambda_82F2():
        OP_6C(322000, 5500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_82F2)
    OP_6D(51480, 400, 59800, 4000)
    OP_44(0xF, 0xFF)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_44(0x10, 0xFF)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_44(0x11, 0xFF)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    StopSound(0x9470, 0x3D090, 0x2710)
    Sleep(700)
    OP_22(0x93, 0x0, 0x64)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x3FC)
    Sleep(300)

    ChrTalk(
        0x10,
        "#10A#3P哇啊啊……！\x05\x02",
    )

    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_83C2():
        OP_8E(0xFE, 0xC6A2, 0x0, 0x108EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_83C2)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_83F4():
        OP_8E(0xFE, 0xC6A2, 0x0, 0x108EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_83F4)

    ChrTalk(
        0x11,
        "#10A#2P啊啊啊啊啊！\x05\x02",
    )

    Sleep(100)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_843D():
        OP_8E(0xFE, 0xC6A2, 0x0, 0x108EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_843D)

    def lambda_8458():
        OP_6D(51130, 400, 52010, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8458)

    def lambda_8470():
        OP_67(0, 6250, -10000, 8600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8470)

    def lambda_8488():
        OP_6C(270000, 8600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8488)

    def lambda_8498():
        OP_6E(729, 8600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8498)
    Sleep(2000)
    OP_63(0x10)
    OP_63(0xF)
    OP_63(0x11)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x0, 0x4)
    SetChrFlags(0x1, 0x4)
    SetChrFlags(0x2, 0x4)
    Sleep(1800)

    def lambda_84DE():
        OP_8F(0xFE, 0xFFFFE9EE, 0x190, 0xCF08, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_84DE)
    Sleep(1800)
    OP_22(0xD9, 0x0, 0x64)

    def lambda_8503():
        OP_8F(0xFE, 0xFFFFE9EE, 0x190, 0xCADA, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8503)
    Sleep(3000)

    def lambda_8523():
        OP_6D(26670, -810, 52180, 3500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8523)

    def lambda_853B():
        OP_6B(1750, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_853B)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_38_808F end

    def Function_39_8562(): pass

    label("Function_39_8562")

    OP_A2(0x500)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(51000, 400, 61600, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(21000, 0)
    FadeToBright(2000, 0)
    SetChrPos(0xC, 62600, 6000, 68000, 0)
    SetChrPos(0x105, 50500, 0, 67700, 0)
    SetChrPos(0x101, 50500, 0, 67700, 0)
    SetChrPos(0x102, 50500, 0, 67700, 0)

    def lambda_85F3():
        OP_8E(0xFE, 0xC6D4, 0x190, 0xCB84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_85F3)

    def lambda_860E():
        OP_6D(50900, 400, 52100, 4800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_860E)

    def lambda_8626():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8626)
    Sleep(500)

    def lambda_863B():
        OP_8E(0xFE, 0xCB84, 0x190, 0xCE40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_863B)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#501F#3P……果然，\x01",
            "好像还没有来呢。\x02\x03",
            "我们是不是来得太早了点？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x01",
            "要不先去酒吧打发一会儿时间吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#001F#3P不用了，吹吹风也挺舒服的。\x01",
            "我们就在这里等吧。\x02\x03",
            "站在桥上看着河水流动，\x01",
            "完全不会感到无聊呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F嗯，那好吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    def lambda_878F():
        OP_6D(49130, 400, 51740, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_878F)

    def lambda_87A7():
        OP_8E(0xFE, 0xC15C, 0x190, 0xC800, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_87A7)
    OP_8C(0x102, 270, 400)

    def lambda_87C9():
        OP_8E(0xFE, 0xC15C, 0x190, 0xCC4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_87C9)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 0)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x101,
        (
            "#006F#2P话说回来，\x01",
            "卢安也终于恢复了以往的平静呢。\x02\x03",
            "前阵子戴尔蒙市长被捕的时候，\x01",
            "整个城市还闹得沸沸扬扬的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#1P因为现任市长被捕\x01",
            "确实是前所未闻的事情啊。\x02\x03",
            "假如说洛连特的\x01",
            "克劳斯市长遭到了逮捕，\x01",
            "我想也一样会闹得沸沸扬扬的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2P哇，要是发生了那种事情，\x01",
            "肯定不是一般的轰动……\x02\x03",
            "#000F不过这样一比较，\x01",
            "卢安的百姓反而还算冷静呢。\x02\x03",
            "虽然大家都非常吃惊，\x01",
            "但看来并没有受到太大打击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P嗯，因为卢安的市长\x01",
            "一直都是按照传统继任的，\x01",
            "由戴尔蒙家族的主人担任这个角色。\x02\x03",
            "并不是因为市长本人\x01",
            "受到卢安市民仰慕的缘故。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2P和受洛连特市民爱戴的\x01",
            "克劳斯市长完全不一样啊。\x02\x03",
            "嗯……虽说是自作自受，\x01",
            "不过想起来还是觉得他挺可怜的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x105, 300)

    ChrTalk(
        0x102,
        "#010F#1P好像来了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()

    def lambda_8BE2():
        OP_6D(51540, 400, 57590, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8BE2)

    def lambda_8BFA():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8BFA)
    ClearChrFlags(0xC, 0x80)
    OP_22(0x8C, 0x0, 0x64)
    OP_8E(0xC, 0xD28C, 0x514, 0xDEA8, 0xFA0, 0x0)
    SetChrFlags(0xC, 0x20)

    def lambda_8C2D():

        label("loc_8C2D")

        OP_99(0xFE, 0x0, 0x7, 0x1388)
        OP_48()
        Jump("loc_8C2D")

    QueueWorkItem2(0xC, 2, lambda_8C2D)
    TurnDirection(0x102, 0xC, 400)
    TurnDirection(0x101, 0xC, 400)

    def lambda_8C4E():
        OP_8C(0xFE, 270, 100)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_8C4E)
    OP_8F(0xC, 0xD228, 0x44C, 0xDEA8, 0x1F4, 0x0)
    OP_44(0xC, 0x2)
    SetChrChipByIndex(0xC, 16)
    SetChrSubChip(0xC, 3)
    Sleep(100)
    SetChrSubChip(0xC, 4)
    Sleep(100)
    SetChrSubChip(0xC, 0)
    ClearChrFlags(0xC, 0x20)

    ChrTalk(
        0x101,
        "#001F啊，基库！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 1)
    Sleep(300)

    ChrTalk(
        0xC,
        "#310F#5P啾。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x105,
        "女孩的声音",
        "#4P艾丝蒂尔、约修亚！\x02",
    )

    CloseMessageWindow()
    OP_8E(0x105, 0xC738, 0x190, 0xE164, 0x1388, 0x0)

    ChrTalk(
        0x105,
        (
            "#045F#1P哈啊哈啊……\x02\x03",
            "对不起，我迟到了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8D50():
        OP_8E(0xFE, 0xC4E0, 0x190, 0xDB24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D50)
    Sleep(200)

    def lambda_8D70():
        OP_8E(0xFE, 0xC864, 0x190, 0xDA5C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D70)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F没关系呢，\x01",
            "其实我们也是刚到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F难、难道说\x01",
            "你是特地一路跑过来的？\x02\x03",
            "不用那么着急嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F#1P不行呢，我可是来送行的，\x01",
            "怎么能慢悠悠地走过来呢。\x02\x03",
            "幸好你们通知了我，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F哎呀～科洛丝真是的。\x01",
            "该说谢谢的是我们两个啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(
        0x101,
        (
            "#001F还有基库……\x01",
            "谢谢你来送我们哦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#311F#2P啾～☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，那么……\x01",
            "我们是时候出发了吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#006F嗯，好吧。\x02\x03",
            "要前往蔡斯地区的话，\x01",
            "是从南街区的门口出去对吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_905F")

    ChrTalk(
        0x105,
        (
            "#040F#1P嗯，南面街道的尽头有个\x01",
            "通往蔡斯方面的『艾尔·雷登』关所。\x02\x03",
            "由于那里有一座非常宏伟的瀑布，\x01",
            "所以作为观光地也非常有名哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F哎～那还真是值得期待啊。\x02\x03",
            "#001F好，我们出发吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FC")

    label("loc_905F")


    ChrTalk(
        0x105,
        (
            "#040F#1P嗯，南面街道的尽头有个\x01",
            "叫做『艾尔·雷登』的关所。\x02\x03",
            "从那里一直走，\x01",
            "就是通往蔡斯的街道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，明白了。\x02\x03",
            "#001F那么，我们出发吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90FC")


    ChrTalk(
        0xC,
        "#311F#2P啾～！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)
    SetChrSubChip(0xC, 4)
    Sleep(100)
    SetChrSubChip(0xC, 3)
    Sleep(100)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_9142():
        OP_8E(0xFE, 0xC864, 0x1770, 0x9C40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_9142)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x0)
    SetChrFlags(0xC, 0x80)
    Return()

    # Function_39_8562 end

    def Function_40_9168(): pass

    label("Function_40_9168")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9227")
    OP_A2(0xA)
    TurnDirection(0x136, 0x0, 400)

    ChrTalk(
        0x136,
        (
            "#040F嗯～\x01",
            "我想还是先去预定好房间吧。\x02\x03",
            "现在这个旅游旺季\x01",
            "酒店很容易客满的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9201():
        TurnDirection(0x102, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9201)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，是这样，\x01",
            "那就赶快去预定吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92A9")

    label("loc_9227")

    TurnDirection(0x136, 0x0, 400)

    ChrTalk(
        0x136,
        (
            "#040F我想还是先去预定好房间吧。\x01",
            "　\x02\x03",
            "现在这个旅游旺季\x01",
            "酒店很容易客满的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92A9")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_40_9168 end

    def Function_41_92C5(): pass

    label("Function_41_92C5")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93D6")
    OP_A2(0xA)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F已经是傍晚时分了，\x01",
            "还是别去街道那边比较好。\x02\x03",
            "就算在城里散步，\x01",
            "也要先去房间把东西放好吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，说的也是。\x02\x03",
            "我们的房间在酒店的最顶层对吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_947F")

    label("loc_93D6")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F已经是傍晚时分了，\x01",
            "还是别去街道那边比较好。\x02\x03",
            "就算在城里散步，\x01",
            "也要先去房间把东西放好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_947F")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_41_92C5 end

    def Function_42_949B(): pass

    label("Function_42_949B")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95EB")
    OP_A2(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_953E")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F在去城外之前先到协会报到吧。\x01",
            "　\x02\x03",
            "嘉恩先生不是说\x01",
            "要给我们分配工作吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F啊，没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_95E8")

    label("loc_953E")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F哎……\x01",
            "要到城外去吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F不了，\x01",
            "还是先去协会吧。\x02\x03",
            "嘉恩先生不是说\x01",
            "要给我们分配工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F啊，没错。\x02",
    )

    CloseMessageWindow()

    label("loc_95E8")

    Jump("loc_9653")

    label("loc_95EB")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F在去城外之前去协会报到吧。\x01",
            "　\x02\x03",
            "嘉恩先生不是说\x01",
            "要给我们分配工作吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9653")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_42_949B end

    def Function_43_966F(): pass

    label("Function_43_966F")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9687")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_968E")

    label("loc_9687")

    TurnDirection(0x102, 0x0, 400)

    label("loc_968E")


    ChrTalk(
        0x102,
        (
            "#010F还是先回协会吧。\x02\x03",
            "调查的结果说不定已经出来了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_43_966F end

    def Function_44_9716(): pass

    label("Function_44_9716")

    SetPlaceName(0x48) # 卢安飞艇坪
    Return()

    # Function_44_9716 end

    def Function_45_971A(): pass

    label("Function_45_971A")

    SetPlaceName(0x4D) # 卢安飞艇坪
    Return()

    # Function_45_971A end

    def Function_46_971E(): pass

    label("Function_46_971E")

    SetPlaceName(0x4C) # 卢安飞艇坪
    Return()

    # Function_46_971E end

    def Function_47_9722(): pass

    label("Function_47_9722")

    SetPlaceName(0x4A) # 卢安飞艇坪
    Return()

    # Function_47_9722 end

    def Function_48_9726(): pass

    label("Function_48_9726")

    SetPlaceName(0x4E) # 卢安飞艇坪
    Return()

    # Function_48_9726 end

    def Function_49_972A(): pass

    label("Function_49_972A")

    SetPlaceName(0x4B) # 卢安飞艇坪
    Return()

    # Function_49_972A end

    def Function_50_972E(): pass

    label("Function_50_972E")

    SetPlaceName(0x49) # 卢安飞艇坪
    Return()

    # Function_50_972E end

    def Function_51_9732(): pass

    label("Function_51_9732")

    SetPlaceName(0x4F) # 卢安飞艇坪
    Return()

    # Function_51_9732 end

    SaveToFile()

Try(main)
