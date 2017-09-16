from ED6ScenarioHelper import *

def main():
    # 蔡斯飞艇坪

    CreateScenaFile(
        FileName            = 'T3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '玛多克工房长',                         # 10
        '特莱斯主任',                           # 11
        '海泽尔',                               # 12
        '索黛丽娅',                             # 13
        '阿利瑟',                               # 14
        '米优',                                 # 15
        '斯坦因',                               # 16
        '温丝',                                 # 17
        '埃尔文',                               # 18
        '王',                                   # 19
        '莱恩',                                 # 20
        '科奇莫爷爷',                           # 21
        '莫妮卡',                               # 22
        '布鲁诺',                               # 23
        '伊格尔',                               # 24
        '普利亚姆',                             # 25
        '爱玲',                                 # 26
        '雷曼',                                 # 27
        '鲁迪',                                 # 28
        '菲',                                   # 29
        '埃里克',                               # 30
        '康丝坦茨',                             # 31
        '雨果',                                 # 32
        '安东尼',                               # 33
        '普罗梅笛',                             # 34
        '雷伊',                                 # 35
        '蒂亚利',                               # 36
        '米妮亚姆',                             # 37
        '威尔姆',                               # 38
        '格斯塔夫维修长',                       # 39
        ' ',                                    # 40
        '蔡斯飞艇坪',                           # 41
        '蔡斯市·市街区',                       # 42
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
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT07/CH02620 ._CH',             # 01
        'ED6_DT07/CH01190 ._CH',             # 02
        'ED6_DT07/CH01540 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01050 ._CH',             # 06
        'ED6_DT07/CH01200 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01760 ._CH',             # 0A
        'ED6_DT07/CH01450 ._CH',             # 0B
        'ED6_DT07/CH01100 ._CH',             # 0C
        'ED6_DT07/CH02490 ._CH',             # 0D
        'ED6_DT07/CH01530 ._CH',             # 0E
        'ED6_DT07/CH01250 ._CH',             # 0F
        'ED6_DT07/CH01140 ._CH',             # 10
        'ED6_DT07/CH01150 ._CH',             # 11
        'ED6_DT07/CH01450 ._CH',             # 12
        'ED6_DT07/CH01500 ._CH',             # 13
        'ED6_DT07/CH01550 ._CH',             # 14
        'ED6_DT07/CH01450 ._CH',             # 15
        'ED6_DT07/CH01230 ._CH',             # 16
        'ED6_DT07/CH01680 ._CH',             # 17
        'ED6_DT07/CH01700 ._CH',             # 18
        'ED6_DT07/CH01100 ._CH',             # 19
        'ED6_DT07/CH01220 ._CH',             # 1A
        'ED6_DT07/CH01660 ._CH',             # 1B
        'ED6_DT07/CH01430 ._CH',             # 1C
        'ED6_DT07/CH01450 ._CH',             # 1D
        'ED6_DT07/CH02440 ._CH',             # 1E
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT07/CH02620P._CP',             # 01
        'ED6_DT07/CH01190P._CP',             # 02
        'ED6_DT07/CH01540P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01050P._CP',             # 06
        'ED6_DT07/CH01200P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01760P._CP',             # 0A
        'ED6_DT07/CH01450P._CP',             # 0B
        'ED6_DT07/CH01100P._CP',             # 0C
        'ED6_DT07/CH02490P._CP',             # 0D
        'ED6_DT07/CH01530P._CP',             # 0E
        'ED6_DT07/CH01250P._CP',             # 0F
        'ED6_DT07/CH01140P._CP',             # 10
        'ED6_DT07/CH01150P._CP',             # 11
        'ED6_DT07/CH01450P._CP',             # 12
        'ED6_DT07/CH01500P._CP',             # 13
        'ED6_DT07/CH01550P._CP',             # 14
        'ED6_DT07/CH01450P._CP',             # 15
        'ED6_DT07/CH01230P._CP',             # 16
        'ED6_DT07/CH01680P._CP',             # 17
        'ED6_DT07/CH01700P._CP',             # 18
        'ED6_DT07/CH01100P._CP',             # 19
        'ED6_DT07/CH01220P._CP',             # 1A
        'ED6_DT07/CH01660P._CP',             # 1B
        'ED6_DT07/CH01430P._CP',             # 1C
        'ED6_DT07/CH01450P._CP',             # 1D
        'ED6_DT07/CH02440P._CP',             # 1E
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
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
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
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
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
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
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
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
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
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
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
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
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
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = -23030,
        Z                   = 8000,
        Y                   = 86970,
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
        Z                   = 8000,
        Y                   = 58980,
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
        X                   = -10910,
        Y                   = 7000,
        Z                   = 63300,
        Range               = -12900,
        Unknown_10          = 0x2328,
        Unknown_14          = 0xD480,
        Unknown_18          = 0x0,
        Unknown_1C          = 45,
    )

    DeclEvent(
        X                   = -19010,
        Y                   = 7000,
        Z                   = 74090,
        Range               = -26870,
        Unknown_10          = 0x2328,
        Unknown_14          = 0x12714,
        Unknown_18          = 0x0,
        Unknown_1C          = 52,
    )

    DeclEvent(
        X                   = -50430,
        Y                   = 24000,
        Z                   = 53980,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = -35690,
        Y                   = 9750,
        Z                   = 58940,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 54,
    )

    DeclEvent(
        X                   = -23010,
        Y                   = 7750,
        Z                   = 74850,
        Range               = 1500,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 55,
    )


    DeclActor(
        TriggerX            = -50000,
        TriggerZ            = 25000,
        TriggerY            = 54010,
        TriggerRange        = 800,
        ActorX              = -50000,
        ActorZ              = 26000,
        ActorY              = 54010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 44,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_6A6",          # 00, 0
        "Function_1_E70",          # 01, 1
        "Function_2_10C0",         # 02, 2
        "Function_3_10F6",         # 03, 3
        "Function_4_127E",         # 04, 4
        "Function_5_12A2",         # 05, 5
        "Function_6_12C6",         # 06, 6
        "Function_7_12EA",         # 07, 7
        "Function_8_130E",         # 08, 8
        "Function_9_1332",         # 09, 9
        "Function_10_1356",        # 0A, 10
        "Function_11_137A",        # 0B, 11
        "Function_12_137B",        # 0C, 12
        "Function_13_13E0",        # 0D, 13
        "Function_14_1445",        # 0E, 14
        "Function_15_14AB",        # 0F, 15
        "Function_16_14F2",        # 10, 16
        "Function_17_154C",        # 11, 17
        "Function_18_15F0",        # 12, 18
        "Function_19_1676",        # 13, 19
        "Function_20_17F8",        # 14, 20
        "Function_21_18B0",        # 15, 21
        "Function_22_18D1",        # 16, 22
        "Function_23_1BD8",        # 17, 23
        "Function_24_1C7C",        # 18, 24
        "Function_25_1CEE",        # 19, 25
        "Function_26_1D4F",        # 1A, 26
        "Function_27_1DCC",        # 1B, 27
        "Function_28_1DF3",        # 1C, 28
        "Function_29_1E5B",        # 1D, 29
        "Function_30_2039",        # 1E, 30
        "Function_31_2938",        # 1F, 31
        "Function_32_2D9D",        # 20, 32
        "Function_33_2E46",        # 21, 33
        "Function_34_2F88",        # 22, 34
        "Function_35_2F8F",        # 23, 35
        "Function_36_2F96",        # 24, 36
        "Function_37_3042",        # 25, 37
        "Function_38_34EF",        # 26, 38
        "Function_39_35C8",        # 27, 39
        "Function_40_3615",        # 28, 40
        "Function_41_3890",        # 29, 41
        "Function_42_3D8A",        # 2A, 42
        "Function_43_4383",        # 2B, 43
        "Function_44_4399",        # 2C, 44
        "Function_45_4421",        # 2D, 45
        "Function_46_477F",        # 2E, 46
        "Function_47_4AD9",        # 2F, 47
        "Function_48_5917",        # 30, 48
        "Function_49_6273",        # 31, 49
        "Function_50_6778",        # 32, 50
        "Function_51_6ECF",        # 33, 51
        "Function_52_7169",        # 34, 52
        "Function_53_7383",        # 35, 53
        "Function_54_7BFF",        # 36, 54
        "Function_55_7C03",        # 37, 55
    )


    def Function_0_6A6(): pass

    label("Function_0_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_6B4")
    OP_A3(0x3FA)
    Event(0, 50)

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_6CB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 51)

    label("loc_6CB")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_6E3"),
        (103, "loc_722"),
        (107, "loc_722"),
        (104, "loc_735"),
        (SWITCH_DEFAULT, "loc_73D"),
    )


    label("loc_6E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F9")
    OP_A2(0x51B)
    Event(0, 46)
    Jump("loc_71F")

    label("loc_6F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70C")
    Event(0, 48)
    Jump("loc_71F")

    label("loc_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71F")
    OP_A2(0x537)
    Event(0, 49)

    label("loc_71F")

    Jump("loc_73D")

    label("loc_722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_732")
    Event(0, 47)

    label("loc_732")

    Jump("loc_73D")

    label("loc_735")

    OP_22(0xE, 0x0, 0x64)
    Jump("loc_73D")

    label("loc_73D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_79F")
    SetChrPos(0xD, -14600, 8000, 63040, 6)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0x10, -15440, 8000, 63040, 3)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_E6F")

    label("loc_79F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_832")
    SetChrPos(0xD, -21460, 8000, 58770, 270)
    SetChrPos(0x10, -20870, 8000, 59640, 270)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -23240, 8000, 57820, 45)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -23310, 8000, 59800, 135)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_E6F")

    label("loc_832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_868")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_E6F")

    label("loc_868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_89E")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -25190, 8000, 66790, 275)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -17150, 8000, 63800, 358)
    Jump("loc_E6F")

    label("loc_89E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_98D")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -23800, 10000, 46930, 180)
    OP_43(0x11, 0x0, 0x0, 0x3)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -23170, 8000, 59080, 91)
    OP_43(0x12, 0x0, 0x0, 0x5)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -25200, 8000, 67400, 272)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -31870, 10000, 49240, 326)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -33120, 10000, 50470, 135)
    SetChrFlags(0x17, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -23610, 8000, 70240, 5)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -48310, 22000, 49830, 163)
    Jump("loc_E6F")

    label("loc_98D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_CF9")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -30660, 9000, 60810, 69)
    OP_43(0xA, 0x0, 0x0, 0x3)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, -24500, 8750, 51360, 18)
    OP_51(0x25, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -34110, 10000, 62990, 166)
    OP_43(0x11, 0x0, 0x0, 0x4)
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    OP_51(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -23610, 8000, 70240, 5)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    OP_51(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -27110, 8000, 60420, 69)
    SetChrFlags(0x1B, 0x10)
    OP_51(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -27070, 8000, 59620, 359)
    SetChrFlags(0x1C, 0x10)
    OP_51(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -33870, 10000, 57010, 292)
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -30810, 10000, 48800, 320)
    OP_43(0x1D, 0x0, 0x0, 0x7)
    OP_51(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32630, 10000, 58920, 255)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -26600, 8000, 55790, 279)
    OP_51(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -21730, 8000, 53410, 270)
    OP_43(0x1F, 0x0, 0x0, 0x8)
    OP_51(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -29430, 8000, 57220, 85)
    SetChrFlags(0x17, 0x10)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, -22660, 8000, 61960, 82)
    OP_43(0x21, 0x0, 0x0, 0xA)
    OP_51(0x21, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -33530, 10000, 52430, 296)
    OP_51(0x22, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, -33770, 10000, 51140, 330)
    OP_51(0x23, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, -25860, 8000, 60310, 263)
    OP_51(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, -21670, 8000, 66490, 242)
    OP_51(0x26, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -23200, 10000, 47850, 272)
    OP_43(0x20, 0x0, 0x0, 0x9)
    OP_51(0x20, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -30230, 10000, 47900, 298)
    OP_51(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E6F")

    label("loc_CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_D4C")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -23610, 8000, 70240, 5)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    Jump("loc_E6F")

    label("loc_D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_D82")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_E6F")

    label("loc_D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_DB8")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_E6F")

    label("loc_DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_E10")
    SetChrPos(0xD, -14600, 8000, 63040, 6)
    SetChrPos(0x10, -15440, 8000, 63040, 3)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_E6F")

    label("loc_E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E6F")
    SetChrPos(0xD, -14600, 8000, 63040, 6)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0x10, -15440, 8000, 63040, 3)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)

    label("loc_E6F")

    Return()

    # Function_0_6A6 end

    def Function_1_E70(): pass

    label("Function_1_E70")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFEF278, 0x30052)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E9A")
    OP_B1("t3101_y")
    Jump("loc_EA3")

    label("loc_E9A")

    OP_B1("t3101_n")

    label("loc_EA3")

    OP_6F(0x5, 40)
    OP_70(0x5, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF6")

    label("loc_EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF6")

    label("loc_EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F0A")
    OP_72(0x3, 0x10)
    Jump("loc_F0E")

    label("loc_F0A")

    OP_64(0x0, 0x1)

    label("loc_F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1090")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1090")
    LoadEffect(0x0, "map\\\\mp011_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -49690, 25000, 54030, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x0, 0xFF, 0xFF, -39390, 22000, 56200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x0, 0xFF, 0xFF, -39390, 22000, 61640, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x0, 0xFF, 0xFF, -39850, 19620, 65980, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x0, 0xFF, 0xFF, -39770, 17290, 50070, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x0, 0xFF, 0xFF, -37130, 10000, 58950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)

    label("loc_1090")

    OP_72(0x0, 0x10)
    OP_6F(0x0, 60)

    label("loc_109C")

    SoundDistance(0xA0, 0xFFFFEDF4, 0x14C8, 0xE790, 0x2710, 0x7530, 0x64, 0x0)
    OP_43(0x27, 0x0, 0x0, 0x2)
    Return()

    # Function_1_E70 end

    def Function_2_10C0(): pass

    label("Function_2_10C0")

    OP_72(0x5, 0x20)
    OP_72(0x4, 0x20)

    label("loc_10CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10F5")
    OP_6F(0x5, 40)
    OP_70(0x5, 0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x28)
    OP_73(0x5)
    Jump("loc_10CA")

    label("loc_10F5")

    Return()

    # Function_2_10C0 end

    def Function_3_10F6(): pass

    label("Function_3_10F6")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1126")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_1268")

    label("loc_1126")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113F")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_1268")

    label("loc_113F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1158")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_1268")

    label("loc_1158")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1171")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_1268")

    label("loc_1171")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118A")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_1268")

    label("loc_118A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A3")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_1268")

    label("loc_11A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BC")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_1268")

    label("loc_11BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D5")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_1268")

    label("loc_11D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EE")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_1268")

    label("loc_11EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1207")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_1268")

    label("loc_1207")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1220")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_1268")

    label("loc_1220")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1239")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_1268")

    label("loc_1239")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1252")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_1268")

    label("loc_1252")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1268")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_1268")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_127D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1268")

    label("loc_127D")

    Return()

    # Function_3_10F6 end

    def Function_4_127E(): pass

    label("Function_4_127E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12A1")
    OP_8D(0xFE, -35270, 61360, -33040, 64150, 3000)
    Jump("Function_4_127E")

    label("loc_12A1")

    Return()

    # Function_4_127E end

    def Function_5_12A2(): pass

    label("Function_5_12A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12C5")
    OP_8D(0xFE, -26390, 55950, -19770, 61950, 3000)
    Jump("Function_5_12A2")

    label("loc_12C5")

    Return()

    # Function_5_12A2 end

    def Function_6_12C6(): pass

    label("Function_6_12C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12E9")
    OP_8D(0xFE, -25190, 68440, -20920, 71850, 3000)
    Jump("Function_6_12C6")

    label("loc_12E9")

    Return()

    # Function_6_12C6 end

    def Function_7_12EA(): pass

    label("Function_7_12EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_130D")
    OP_8D(0xFE, -32689, 46510, -30620, 50700, 3000)
    Jump("Function_7_12EA")

    label("loc_130D")

    Return()

    # Function_7_12EA end

    def Function_8_130E(): pass

    label("Function_8_130E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1331")
    OP_8D(0xFE, -25190, 54660, -20780, 60740, 3000)
    Jump("Function_8_130E")

    label("loc_1331")

    Return()

    # Function_8_130E end

    def Function_9_1332(): pass

    label("Function_9_1332")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1355")
    OP_8D(0xFE, -26510, 46520, -19100, 49060, 3000)
    Jump("Function_9_1332")

    label("loc_1355")

    Return()

    # Function_9_1332 end

    def Function_10_1356(): pass

    label("Function_10_1356")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1379")
    OP_8D(0xFE, -23960, 59250, -21170, 66410, 3000)
    Jump("Function_10_1356")

    label("loc_1379")

    Return()

    # Function_10_1356 end

    def Function_11_137A(): pass

    label("Function_11_137A")

    Return()

    # Function_11_137A end

    def Function_12_137B(): pass

    label("Function_12_137B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_13DC")

    ChrTalk(
        0xFE,
        (
            "#690F这烟真是好大啊。\x02\x03",
            "连中央工房的换气能力\x01",
            "也应付不过来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13DC")

    TalkEnd(0xFE)
    Return()

    # Function_12_137B end

    def Function_13_13E0(): pass

    label("Function_13_13E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1441")

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "好久没有这么拼命地奔跑了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊，真糟糕。\x01",
            "情况糟透了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1441")

    TalkEnd(0xFE)
    Return()

    # Function_13_13E0 end

    def Function_14_1445(): pass

    label("Function_14_1445")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_14A7")

    ChrTalk(
        0xFE,
        (
            "工房里面\x01",
            "已经到处是浓烟了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼呼～～～～\x01",
            "我还以为死定了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A7")

    TalkEnd(0xFE)
    Return()

    # Function_14_1445 end

    def Function_15_14AB(): pass

    label("Function_15_14AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_14EE")

    ChrTalk(
        0xFE,
        "有没有受伤的人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有的话\x01",
            "要马上通知我啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EE")

    TalkEnd(0xFE)
    Return()

    # Function_15_14AB end

    def Function_16_14F2(): pass

    label("Function_16_14F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1548")

    ChrTalk(
        0xFE,
        (
            "前、前辈！\x01",
            "怎么办呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "发生火灾的话，\x01",
            "研究数据就要毁掉了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1548")

    TalkEnd(0xFE)
    Return()

    # Function_16_14F2 end

    def Function_17_154C(): pass

    label("Function_17_154C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_15EC")

    ChrTalk(
        0xFE,
        "……呼，好奇怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论怎么看\x01",
            "都不像火灾所冒出的烟啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "大家也都没有能冒烟的实验装置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么这些烟\x01",
            "是从哪里出来的？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15EC")

    TalkEnd(0xFE)
    Return()

    # Function_17_154C end

    def Function_18_15F0(): pass

    label("Function_18_15F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1672")

    ChrTalk(
        0xFE,
        (
            "我都不清楚\x01",
            "自己是怎么逃出来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在逃生的途中\x01",
            "我突然想起了空贼事件……\x01",
            "脚差点踩空了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1672")

    TalkEnd(0xFE)
    Return()

    # Function_18_15F0 end

    def Function_19_1676(): pass

    label("Function_19_1676")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_17AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1721")

    ChrTalk(
        0xFE,
        (
            "说起来\x01",
            "的确没有看到拉赛尔呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过那家伙应该不用让人担心。\x01",
            "肯定已经逃出来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A7")

    label("loc_1721")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "紧急通道也是很有用处的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没那玩意儿的话\x01",
            "就只能从阳台上跳下来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A7")

    Jump("loc_17F4")

    label("loc_17AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_17F4")

    ChrTalk(
        0xFE,
        "痛、痛痛痛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不小心踏空楼梯，\x01",
            "扭到腰了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F4")

    TalkEnd(0xFE)
    Return()

    # Function_19_1676 end

    def Function_20_17F8(): pass

    label("Function_20_17F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_18AC")

    ChrTalk(
        0xFE,
        (
            "我正在做实验的时候，\x01",
            "突然冒起了漫天烟雾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "我是拼命逃出来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想大家也\x01",
            "应该都逃出来了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AC")

    TalkEnd(0xFE)
    Return()

    # Function_20_17F8 end

    def Function_21_18B0(): pass

    label("Function_21_18B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_18CD")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵呀～噢！\x02",
    )

    CloseMessageWindow()

    label("loc_18CD")

    TalkEnd(0xFE)
    Return()

    # Function_21_18B0 end

    def Function_22_18D1(): pass

    label("Function_22_18D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_1B82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_END)), "loc_1951")

    ChrTalk(
        0xFE,
        (
            "呼，建筑物里都是烟，\x01",
            "好讨厌呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天还是早点回家吧。\x01",
            "不管再发生什么我都要回家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7F")

    label("loc_1951")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19D1")

    ChrTalk(
        0xFE,
        (
            "呼，建筑物里都是烟，\x01",
            "好讨厌呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天还是早点回家吧。\x01",
            "不管再发生什么我都要回家。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)
    Jump("loc_1B7F")

    label("loc_19D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1A6C")

    ChrTalk(
        0xFE,
        (
            "呼，建筑物里都是烟，\x01",
            "好讨厌呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……唔，这种情况下\x01",
            "还是不要谈工作的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是不好意思，\x01",
            "明天再把书给我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)
    Jump("loc_1B7F")

    label("loc_1A6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1B08")

    ChrTalk(
        0xFE,
        (
            "呼，建筑物里都是烟，\x01",
            "好讨厌呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……唔，这种情况下\x01",
            "还是不要谈工作的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "委托的事\x01",
            "只好拖到明天了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)
    Jump("loc_1B7F")

    label("loc_1B08")


    ChrTalk(
        0xFE,
        (
            "呼，因为刚才拼命地跑，\x01",
            "身上的肌肉痛得受不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天还是早点回家吧。\x01",
            "不管再发生什么我都要回家。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)

    label("loc_1B7F")

    Jump("loc_1BD4")

    label("loc_1B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1BD4")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "好久没有这样剧烈运动过了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀哎呀，痛啊……\x02",
    )

    CloseMessageWindow()

    label("loc_1BD4")

    TalkEnd(0xFE)
    Return()

    # Function_22_18D1 end

    def Function_23_1BD8(): pass

    label("Function_23_1BD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1C78")

    ChrTalk(
        0x9,
        (
            "#800F博士应该在三楼的工作室。\x01",
            "　\x02\x03",
            "首先去那里确认一下。\x01",
            "如果危险的话就马上撤离。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C78")

    TalkEnd(0xFE)
    Return()

    # Function_23_1BD8 end

    def Function_24_1C7C(): pass

    label("Function_24_1C7C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1CEA")

    ChrTalk(
        0x8,
        (
            "#150F我也想一起去呀。\x01",
            "但没办法了……\x02\x03",
            "小艾你们千万要小心呀。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CEA")

    TalkEnd(0xFE)
    Return()

    # Function_24_1C7C end

    def Function_25_1CEE(): pass

    label("Function_25_1CEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1D4B")

    ChrTalk(
        0xFE,
        (
            "客、客人，\x01",
            "你们都顺利逃出来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这、这烟也太大了。\x02",
    )

    CloseMessageWindow()

    label("loc_1D4B")

    TalkEnd(0xFE)
    Return()

    # Function_25_1CEE end

    def Function_26_1D4F(): pass

    label("Function_26_1D4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1DC8")

    ChrTalk(
        0xFE,
        (
            "哪里都找不到\x01",
            "拉赛尔博士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说不定……\x01",
            "难道还在工房里面吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，该怎么办才好。\x02",
    )

    CloseMessageWindow()

    label("loc_1DC8")

    TalkEnd(0xFE)
    Return()

    # Function_26_1D4F end

    def Function_27_1DCC(): pass

    label("Function_27_1DCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1DEF")

    ChrTalk(
        0xFE,
        "鲁迪，你没事吧？\x02",
    )

    CloseMessageWindow()

    label("loc_1DEF")

    TalkEnd(0xFE)
    Return()

    # Function_27_1DCC end

    def Function_28_1DF3(): pass

    label("Function_28_1DF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1E57")

    ChrTalk(
        0xFE,
        "咳咳、咳咳。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "烟、烟……\x01",
            "咳咳、咳咳咳、咳咳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "肺、肺……\x01",
            "咳咳、咳咳！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E57")

    TalkEnd(0xFE)
    Return()

    # Function_28_1DF3 end

    def Function_29_1E5B(): pass

    label("Function_29_1E5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1F46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_1EE1")

    ChrTalk(
        0xFE,
        (
            "不过……\x01",
            "那些从里面出来的\x01",
            "穿着军装的家伙是谁呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明那么大的烟，\x01",
            "他们却好像一点事也没有。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F43")

    label("loc_1EE1")

    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "中央工房\x01",
            "开始冒烟的时候，\x01",
            "我可紧张坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，都怪这烟，\x01",
            "喉咙又开始渴了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F43")

    Jump("loc_2035")

    label("loc_1F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1F85")

    ChrTalk(
        0xFE,
        "啊啊啊，怎么会这样！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到、到底\x01",
            "发生什么事情了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2035")

    label("loc_1F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2035")

    ChrTalk(
        0xFE,
        (
            "在整个王国中，\x01",
            "穿着作业服的驾驶员也只有我一个了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，这和衣服没有关系，\x01",
            "关键在于技术。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2035")

    TalkEnd(0xFE)
    Return()

    # Function_29_1E5B end

    def Function_30_2039(): pass

    label("Function_30_2039")

    TalkBegin(0x18)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2099")
    OP_0D()
    OP_A9(0x4D)
    OP_56(0x0)
    TalkEnd(0x18)
    Return()

    label("loc_2099")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20AA")
    TalkEnd(0x18)
    Return()

    label("loc_20AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_END)), "loc_2126")

    ChrTalk(
        0x18,
        (
            "军队的警备飞艇\x01",
            "好像停在港口呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "又没有发生什么事件，\x01",
            "实在是很少见呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_2126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_221B")

    ChrTalk(
        0x18,
        "哟，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "前些日子，\x01",
            "进出工房船的人好频繁呢，\x01",
            "不过这两天又恢复平静了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "今天的飞艇坪\x01",
            "从早上开始就很安静。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_221B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_22FA")

    ChrTalk(
        0x18,
        "哟，你们今天也很忙嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "说到忙，\x01",
            "刚才雷曼那家伙\x01",
            "慌张地跑向飞艇坪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "看来很着急\x01",
            "要出动工房船的样子。\x01",
            "他还真是辛苦呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_22FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2367")

    ChrTalk(
        0x18,
        "哟，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "早上最好还是\x01",
            "喝杯营养丰富的饮料。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_2367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_241E")

    ChrTalk(
        0x18,
        "哟，这么晚还在辛苦工作啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "哎呀哎呀，\x01",
            "今天也累得要命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "差不多该关店了，\x01",
            "想要什么就快点选吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_241E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2532")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_24AA")

    ChrTalk(
        0x18,
        (
            "从中央工房出来的\x01",
            "穿蓝色军装的家伙，\x01",
            "到底是什么人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "不知道那些军人\x01",
            "在工房里面干了些什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252F")

    label("loc_24AA")

    OP_A2(0xB)

    ChrTalk(
        0x18,
        (
            "呼～\x01",
            "看来骚动总算结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "说起来，那些军人\x01",
            "在那么浓重的烟雾里干了什么呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252F")

    Jump("loc_2934")

    label("loc_2532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_259A")

    ChrTalk(
        0x18,
        (
            "这、这种时候\x01",
            "必须冷静地行动！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "那么，\x01",
            "大家请先喝点清凉的饮料，\x01",
            "稍微冷静一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_259A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_26B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2632")

    ChrTalk(
        0x18,
        (
            "那边的雷曼\x01",
            "其实是飞艇的驾驶员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "我说的飞艇\x01",
            "不是定期船而是工房船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "嗯，\x01",
            "反正都是在天上飞的家伙啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B6")

    label("loc_2632")

    OP_A2(0xB)

    ChrTalk(
        0x18,
        (
            "那边的雷曼\x01",
            "怎么看都是个维修员吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "不过，\x01",
            "其实他是飞艇的驾驶员哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "哈哈哈～\x01",
            "真是人不可貌相啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B6")

    Jump("loc_2934")

    label("loc_26B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_27FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2772")

    ChrTalk(
        0x18,
        (
            "做生意不只是买卖商品，\x01",
            "还必须要考虑经营的手段。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "想开间有人情味的店，\x01",
            "嘴上说起来简单，\x01",
            "但是实现起来却很难呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27F8")

    label("loc_2772")

    OP_A2(0xB)

    ChrTalk(
        0x18,
        (
            "我们的愿望是\x01",
            "拥有一间属于我们自己的店子，\x01",
            "就算规模很小也好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "可以的话，最好能开间\x01",
            "像这座城里的『贝尔杂货店』\x01",
            "那样有人情味的小店。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F8")

    Jump("loc_2934")

    label("loc_27FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2876")

    ChrTalk(
        0x18,
        (
            "对面卖花的爱玲\x01",
            "是我的妹妹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "如果可以的话，\x01",
            "希望大家也到那边去看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_2876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2934")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_28E1")

    ChrTalk(
        0x18,
        (
            "要不要喝点\x01",
            "清凉的饮料呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "我这里卖的饮料不仅美味，\x01",
            "对身体也很有益哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_28E1")

    OP_A2(0xB)

    ChrTalk(
        0x18,
        "哟，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "要不要喝点\x01",
            "清凉的饮料呀？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2934")

    TalkEnd(0x18)
    Return()

    # Function_30_2039 end

    def Function_31_2938(): pass

    label("Function_31_2938")

    TalkBegin(0x19)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2998")
    OP_0D()
    OP_A9(0x4E)
    OP_56(0x0)
    TalkEnd(0x19)
    Return()

    label("loc_2998")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29A9")
    TalkEnd(0x19)
    Return()

    label("loc_29A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_END)), "loc_2A09")

    ChrTalk(
        0x19,
        (
            "哎，从飞艇坪那边\x01",
            "传来了汽笛的声音……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "……发生什么事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2A89")

    ChrTalk(
        0x19,
        (
            "来，请看一看。\x01",
            "这里卖的都是很漂亮的花哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "忘记讨厌的事，\x01",
            "买一盆来舒缓心情吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2B1A")

    ChrTalk(
        0x19,
        (
            "啊，客人们都在议论最近的事情，\x01",
            "没人来好好欣赏花了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "毕竟发生了那样的事情……\x01",
            "不过我还是觉得有些寂寞呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2B59")

    ChrTalk(
        0x19,
        "啊，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "请随意看吧。\x01",
            "就算是只闻闻花香\x01",
            "也能让你心情愉快的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2BA4")

    ChrTalk(
        0x19,
        "啊，晚上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "虽然马上要关店了，\x01",
            "不过趁现在挑选鲜花也没关系。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2C34")

    ChrTalk(
        0x19,
        (
            "我正想着烟可能快要散了，\x01",
            "工房里就出来了几位军人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "难道是他们\x01",
            "把烟止住的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2C53")

    ChrTalk(
        0x19,
        (
            "不、不好了！\x01",
            "怎么回事！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2CC2")

    ChrTalk(
        0x19,
        (
            "蔡斯城里的绿色\x01",
            "越来越少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "就算一次也好，\x01",
            "好想去参观一下那个\x01",
            "以花闻名的玛诺利亚村啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D40")

    ChrTalk(
        0x19,
        (
            "那边卖饮料的\x01",
            "是我的哥哥哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "我们的梦想是兄妹一起加油，\x01",
            "将来开间属于自己的店子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D99")

    ChrTalk(
        0x19,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "这里有各种漂亮的鲜花，\x01",
            "请各位客人慢慢观赏。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D99")

    TalkEnd(0x19)
    Return()

    # Function_31_2938 end

    def Function_32_2D9D(): pass

    label("Function_32_2D9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2DF3")

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "喝了点饮料，\x01",
            "终于放松下来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E42")

    label("loc_2DF3")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个案件真是让人震惊啊。\x01",
            "没办法安心回去工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E42")

    TalkEnd(0xFE)
    Return()

    # Function_32_2D9D end

    def Function_33_2E46(): pass

    label("Function_33_2E46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2EEF")

    ChrTalk(
        0xFE,
        (
            "你们没事实在是太好了，\x01",
            "不过没看到拉赛尔呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然如果他没事的时候\x01",
            "就会给别人带来各种各样的麻烦，\x01",
            "不过还是有点担心他啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F84")

    label("loc_2EEF")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "哦哦，伊格尔。\x01",
            "你没受伤真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是从紧急楼梯下来的吗？\x01",
            "想必一定很累吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F84")

    TalkEnd(0xFE)
    Return()

    # Function_33_2E46 end

    def Function_34_2F88(): pass

    label("Function_34_2F88")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_34_2F88 end

    def Function_35_2F8F(): pass

    label("Function_35_2F8F")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_35_2F8F end

    def Function_36_2F96(): pass

    label("Function_36_2F96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_303E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2FE6")

    ChrTalk(
        0xFE,
        (
            "亲卫队的制服……\x01",
            "的确是让人在意呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_303E")

    label("loc_2FE6")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "工房袭击犯竟然\x01",
            "穿着亲卫队的制服吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_303E")

    TalkEnd(0xFE)
    Return()

    # Function_36_2F96 end

    def Function_37_3042(): pass

    label("Function_37_3042")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3159")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_30AF")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "越来越想不明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "买盆花来\x01",
            "调节一下心情吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3156")

    label("loc_30AF")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "尽管如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "袭击中央工房的犯人\x01",
            "到现在都还没抓到吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王国军和游击士协会\x01",
            "到底都在干什么呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3156")

    Jump("loc_34EB")

    label("loc_3159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3204")

    ChrTalk(
        0xFE,
        (
            "很多人都说\x01",
            "从工房出来的是穿蓝色军装的军人，\x01",
            "所以应该是不会有错的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且温丝也说他看见了。\x01",
            "亲卫队果然很可疑啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34EB")

    label("loc_3204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3474")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_328F")

    ChrTalk(
        0xFE,
        (
            "我一要买什么，\x01",
            "温丝就处处有意见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "这个孩子就喜欢斤斤计较。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3471")

    label("loc_328F")

    OP_A2(0x1)
    TurnDirection(0xD, 0x107, 400)

    ChrTalk(
        0xFE,
        (
            "呀，提妲，\x01",
            "在为客人带路吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，您好，阿利瑟阿姨。\x02\x03",
            "在挑选鲜花吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎，是呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我一要买什么，\x01",
            "温丝就处处有意见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "这个孩子就喜欢斤斤计较。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xD, 400)

    ChrTalk(
        0x10,
        (
            "不是我斤斤计较，\x01",
            "而是妈妈太浪费啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 300)
    OP_62(0xD, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "你说什么！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x107,
        "#065F哎，这个……请别生气……\x02",
    )

    CloseMessageWindow()

    label("loc_3471")

    Jump("loc_34EB")

    label("loc_3474")


    ChrTalk(
        0xFE,
        "哇，好漂亮的花呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过种在阳台上的话，\x01",
            "颜色有些不合适。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34EB")

    TalkEnd(0xFE)
    Return()

    # Function_37_3042 end

    def Function_38_34EF(): pass

    label("Function_38_34EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_35C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_358D")

    ChrTalk(
        0xFE,
        (
            "就连亲卫队\x01",
            "也在这里出现了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果顺利的话，\x01",
            "我就能出名啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "决定了！\x01",
            "我一定要成为工房的接待小姐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C4")

    label("loc_358D")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "哎！亲卫队！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果顺利的话，\x01",
            "我就能出名啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35C4")

    TalkEnd(0xFE)
    Return()

    # Function_38_34EF end

    def Function_39_35C8(): pass

    label("Function_39_35C8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "看起来\x01",
            "不像是火灾呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但那么多烟是怎么回事呢？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_35C8 end

    def Function_40_3615(): pass

    label("Function_40_3615")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_371F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_36A0")

    ChrTalk(
        0xFE,
        (
            "结果最后还是不知道\x01",
            "那些穿军装的人的真面目。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们到底\x01",
            "是什么人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371C")

    label("loc_36A0")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "妈妈，王国军和协会\x01",
            "都已经尽力去调查了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只不过那些情况\x01",
            "是不可能让我们知道的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_371C")

    Jump("loc_388C")

    label("loc_371F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_378B")

    ChrTalk(
        0xFE,
        (
            "妈妈，我看见的是\x01",
            "『穿蓝色军装的军人』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可没说过\x01",
            "我看见的是亲卫队哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_388C")

    label("loc_378B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3856")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_37D5")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "提妲，\x01",
            "工房的工作要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3853")

    label("loc_37D5")

    TurnDirection(0xFE, 0x107, 0)
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "提妲，你好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560F你好，温丝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天也要去工房工作吗？\x01",
            "要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    label("loc_3853")

    Jump("loc_388C")

    label("loc_3856")


    ChrTalk(
        0xFE,
        (
            "妈妈，\x01",
            "阳台的花坛已经放满花盆了呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_388C")

    TalkEnd(0xFE)
    Return()

    # Function_40_3615 end

    def Function_41_3890(): pass

    label("Function_41_3890")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3A4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3972")

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "我也差不多该回店里去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "擅自把商品分发给大家，\x01",
            "妻子一定会很生气吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但能对大家有点用，\x01",
            "我就非常满足了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A4C")

    label("loc_3972")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "看来烟总算是散了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说没有人受伤，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然有东西被偷走了，\x01",
            "只要再做个一样的不就行了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "我也差不多该回店里去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A4C")

    Jump("loc_3D86")

    label("loc_3A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3D86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3A9E")

    ChrTalk(
        0xFE,
        (
            "遇到有困难的人\x01",
            "一定要帮助他们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，你们要小心哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D86")

    label("loc_3A9E")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "你们没事吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我是杂货店的埃尔文。\x01",
            "一听到有事就赶来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从店里带来很多东西，\x01",
            "想要什么就尽管说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这种非常时刻，\x01",
            "当然不会收你们钱。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【替身木偶】\x01",      # 0
            "【圣灵药】\x01",        # 1
            "【石化之刃】\x01",      # 2
        )
    )

    MenuEnd(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C76")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "替身木偶\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x145, 1)
    Jump("loc_3D30")

    label("loc_3C76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CDB")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "圣灵药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x1FD, 1)
    Jump("loc_3D30")

    label("loc_3CDB")

    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "石化之刃\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x27F, 1)

    label("loc_3D30")

    Sleep(100)

    ChrTalk(
        0xFE,
        "好，这个就给你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果遇到有困难的人\x01",
            "一定要帮助他们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，你们要小心哦！\x02",
    )

    CloseMessageWindow()

    label("loc_3D86")

    TalkEnd(0xFE)
    Return()

    # Function_41_3890 end

    def Function_42_3D8A(): pass

    label("Function_42_3D8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_END)), "loc_3ECC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3E41")

    ChrTalk(
        0xFE,
        (
            "可是，我不在的时候\x01",
            "竟然发生这样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "冈多夫先生外出时让我留守，\x01",
            "发生了这样的事，我简直没脸见他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC9")

    label("loc_3E41")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "工房被袭击了……\x01",
            "竟然会发生这样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之要先回协会，\x01",
            "确认一下状况才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EC9")

    Jump("loc_437F")

    label("loc_3ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_437F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3F80")

    ChrTalk(
        0xFE,
        (
            "我不在的时候\x01",
            "竟然发生这样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "冈多夫先生外出时让我留守，\x01",
            "发生了这样的事，我简直没脸见他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_437F")

    label("loc_3F80")

    OP_A2(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x0, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4272")
    OP_A2(0x5CD)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "啊！是你们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，是王先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我、我刚刚\x01",
            "才回到蔡斯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这到底发生什么事了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F嗯，其实啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(
        0x106,
        (
            "#050F喂，你在干什么。\x02\x03",
            "赶快回协会去吧。\x01",
            "我们可没时间再磨蹭了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x106, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#009F唔唔……\x02\x03",
            "#007F哼，虽然不甘心，\x01",
            "但阿加特说得没错。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#018F……有什么不甘心的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x12, 400)

    ChrTalk(
        0x106,
        (
            "#053F还有你。\x02\x03",
            "作为游击士，\x01",
            "应该自己去确认当前的状况。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(
        0xFE,
        "……确实是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不好意思，\x01",
            "我有点自乱阵脚了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F呼……\x02\x03",
            "算了，既然已经发生了，\x01",
            "现在就考虑一下对策吧。\x02\x03",
            "#050F……喂，走啦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_421A():
        TurnDirection(0x102, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_421A)
    TurnDirection(0x101, 0x12, 400)

    ChrTalk(
        0x101,
        "#000F回头见，王先生……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "啊啊，刚刚真是对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_42F7")

    label("loc_4272")


    ChrTalk(
        0xFE,
        (
            "工房被袭击了……\x01",
            "竟然会发生这样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之要先回协会，\x01",
            "确认一下状况才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F7")

    Jump("loc_437F")

    label("loc_42FA")


    ChrTalk(
        0xFE,
        (
            "工房被袭击了……\x01",
            "竟然会发生这样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之要先回协会，\x01",
            "确认一下状况才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_437F")

    TalkEnd(0xFE)
    Return()

    # Function_42_3D8A end

    def Function_43_4383(): pass

    label("Function_43_4383")

    OP_A3(0x540)
    OP_A3(0x541)
    OP_A3(0x546)
    OP_A3(0x543)
    OP_A3(0x544)
    OP_A3(0x545)
    OP_A2(0x546)
    Return()

    # Function_43_4383 end

    def Function_44_4399(): pass

    label("Function_44_4399")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "按了按钮，没有任何反应。\x01",
            "导力梯好像不能用了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_44_4399 end

    def Function_45_4421(): pass

    label("Function_45_4421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_451A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449C")
    TurnDirection(0x102, 0x1, 400)

    ChrTalk(
        0x102,
        (
            "#012F我担心博士的情况。\x01",
            "赶快去工房里面调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44FC")

    label("loc_449C")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#012F我担心博士的情况。\x01",
            "赶快去工房里面调查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44FC")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_477E")

    label("loc_451A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_477E")
    OP_A2(0x50B)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_8C(0x102, 90, 0)
    OP_8C(0x101, 90, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F这，这是什么？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(6010, 2000, 59020, 0)
    OP_67(0, 2920, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -13400, 8000, 59680, 90)
    SetChrPos(0x102, -13620, 8000, 58750, 90)
    OP_0D()

    def lambda_45FA():
        OP_6D(-13820, 9000, 59010, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_45FA)
    Sleep(1000)
    OP_67(0, 11000, -10000, 5000)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    Fade(1000)
    OP_6D(-13480, 8000, 59160, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#014F好像是……会移动的楼梯。\x02\x03",
            "这楼梯看上去好长啊，\x01",
            "自己走下去应该会很辛苦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F话、话是这样说，\x01",
            "但是用机械移动也太……\x02\x03",
            "#509F自从到了这个城镇之后，\x01",
            "感觉除了惊讶之外就没有其他反应了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F我也有同感。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_477E")

    Return()

    # Function_45_4421 end

    def Function_46_477F(): pass

    label("Function_46_477F")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-35180, 10000, 58970, 0)
    OP_6B(2410, 0)
    OP_6C(270000, 0)
    SetChrPos(0x101, -34470, 10000, 59690, 225)
    SetChrPos(0x102, -34480, 10000, 58410, 315)
    SetChrPos(0x107, -35490, 10000, 59000, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_497F")

    ChrTalk(
        0x101,
        (
            "#501F亚尔摩村啊～\x01",
            "我已经开始有点期待呢。\x02\x03",
            "那里是个以温泉著名的胜地吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F是的。\x01",
            "是个非常棒的地方哦。\x02\x03",
            "之前我跟爷爷\x01",
            "去过那里好几次呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F要去那个村子的话，\x01",
            "该怎么走呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F我想想。\x02\x03",
            "出了城镇的南面出口\x01",
            "就是宽广的平原道……\x02\x03",
            "沿着托兰特平原道\x01",
            "一直向南走就到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FＯＫ！\x01",
            "沿着平原道一直往南走对吧。\x02\x03",
            "#001F那么，我们出发吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AD0")

    label("loc_497F")


    ChrTalk(
        0x101,
        (
            "#501F亚尔摩村啊～\x01",
            "我已经开始有点期待呢。\x02\x03",
            "那里是个以温泉著名的胜地吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F是的。\x01",
            "是个非常棒的地方哦。\x02\x03",
            "之前我跟爷爷\x01",
            "去过那里好几次呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F的确是个让人期待的地方，\x01",
            "那么我们就赶快前往亚尔摩吧。\x02\x03",
            "是从南面的门口出去对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F是呢，出去之后，\x01",
            "沿着托兰特平原道向南走就到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FＯＫ！\x01",
            "那么，我们出发吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AD0")

    OP_28(0x40, 0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_46_477F end

    def Function_47_4AD9(): pass

    label("Function_47_4AD9")

    EventBegin(0x0)
    OP_28(0x41, 0x4, 0x2)
    OP_28(0x41, 0x4, 0x4)
    OP_28(0x41, 0x1, 0x1)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 60)
    OP_4A(0x21, 0)
    OP_4A(0x11, 0)
    OP_4A(0x1F, 0)
    OP_6D(-14970, 8000, 55370, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(224000, 0)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0xB, 255)
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    RemoveParty(0xF, 0xFF)
    SetChrPos(0x101, -14050, 8000, 56120, 270)
    SetChrPos(0x102, -13280, 8000, 55260, 270)
    SetChrPos(0x107, -13040, 8000, 57050, 270)
    SetChrPos(0x8, -12520, 8000, 56020, 270)
    SetChrPos(0x1C, -37650, 10000, 59010, 0)
    SetChrPos(0x1B, -37650, 10000, 59010, 0)
    SetChrPos(0x17, -37650, 10000, 59010, 0)
    SetChrPos(0xB, -37650, 10000, 59010, 0)
    SetChrPos(0xA, -37650, 10000, 59010, 0)
    SetChrPos(0x9, -26520, 8000, 57300, 0)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0xB, 0x80)

    def lambda_4C22():

        label("loc_4C22")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4C22")

    QueueWorkItem2(0xB, 1, lambda_4C22)

    def lambda_4C33():
        OP_8E(0xFE, 0xFFFF9E12, 0x1F40, 0xE2CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4C33)
    FadeToBright(2000, 0)
    OP_20(0x5DC)
    OP_0D()
    OP_21()
    OP_1D(0x51)

    ChrTalk(
        0x101,
        "#004F啊啊！？\x02",
    )

    CloseMessageWindow()

    def lambda_4C73():
        OP_6D(-25700, 8000, 55810, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C73)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0xFF)
    FadeToBright(2000, 0)
    StopSound(0x0, 0x3D090, 0x0)
    OP_6D(-35690, 20250, 58940, 0)
    OP_67(0, 20360, -10000, 0)
    OP_6B(3390, 0)
    OP_6C(294000, 0)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x22, 0x4)
    SetChrFlags(0x23, 0x4)
    SetChrFlags(0xA, 0x80)
    OP_4A(0x21, 0)
    OP_4A(0x11, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x17, 0)
    OP_4A(0xB, 0)
    OP_4A(0xA, 0)
    OP_4A(0x24, 0)
    SetChrPos(0x11, -37650, 10000, 59010, 0)
    SetChrPos(0x22, -37650, 10000, 59010, 0)
    SetChrPos(0x23, -37650, 10000, 59010, 0)
    StopSound(0x0, 0x0, 0x2710)

    def lambda_4DA2():
        OP_6C(225000, 11000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_4DA2)
    ClearChrFlags(0xB, 0x80)

    def lambda_4DB7():

        label("loc_4DB7")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4DB7")

    QueueWorkItem2(0xB, 1, lambda_4DB7)

    def lambda_4DC8():
        OP_8E(0xFE, 0xFFFF9E12, 0x1F40, 0xE2CC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4DC8)
    Sleep(500)
    ClearChrFlags(0x11, 0x80)

    def lambda_4DED():

        label("loc_4DED")

        OP_8C(0xFE, 166, 0)
        OP_48()
        Jump("loc_4DED")

    QueueWorkItem2(0x11, 1, lambda_4DED)

    def lambda_4DFE():
        OP_8E(0xFE, 0xFFFF7CAC, 0x2710, 0xF000, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4DFE)
    Sleep(500)
    ClearChrFlags(0x17, 0x80)

    def lambda_4E23():

        label("loc_4E23")

        OP_8C(0xFE, 90, 0)
        OP_48()
        Jump("loc_4E23")

    QueueWorkItem2(0x17, 1, lambda_4E23)

    def lambda_4E34():
        OP_8E(0xFE, 0xFFFF8D0A, 0x1F40, 0xDF84, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_4E34)
    Sleep(1000)
    ClearChrFlags(0x22, 0x80)

    def lambda_4E59():

        label("loc_4E59")

        OP_8C(0xFE, 296, 0)
        OP_48()
        Jump("loc_4E59")

    QueueWorkItem2(0x22, 1, lambda_4E59)

    def lambda_4E6A():
        OP_8E(0xFE, 0xFFFF7F36, 0x2710, 0xDBF6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_4E6A)

    def lambda_4E85():
        OP_6D(-35440, 14790, 58910, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E85)
    Sleep(1000)

    def lambda_4EA2():
        OP_67(0, 12040, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4EA2)
    ClearChrFlags(0x23, 0x80)

    def lambda_4EBF():

        label("loc_4EBF")

        OP_8C(0xFE, 330, 0)
        OP_48()
        Jump("loc_4EBF")

    QueueWorkItem2(0x23, 1, lambda_4EBF)

    def lambda_4ED0():
        OP_8E(0xFE, 0xFFFF7E6E, 0x2710, 0xD886, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_4ED0)
    Sleep(1000)
    ClearChrFlags(0x1C, 0x80)

    def lambda_4EF5():

        label("loc_4EF5")

        OP_8C(0xFE, 0, 0)
        OP_48()
        Jump("loc_4EF5")

    QueueWorkItem2(0x1C, 1, lambda_4EF5)

    def lambda_4F06():
        OP_8E(0xFE, 0xFFFF9642, 0x1F40, 0xE8E4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_4F06)
    Sleep(1000)
    ClearChrFlags(0x1B, 0x80)

    def lambda_4F2B():

        label("loc_4F2B")

        OP_8C(0xFE, 90, 0)
        OP_48()
        Jump("loc_4F2B")

    QueueWorkItem2(0x1B, 1, lambda_4F2B)

    def lambda_4F3C():
        OP_8E(0xFE, 0xFFFF961A, 0x1F40, 0xEC04, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_4F3C)
    Sleep(2000)

    def lambda_4F5C():
        OP_6D(-26430, 8000, 57990, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F5C)

    def lambda_4F74():
        OP_67(0, 11000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F74)

    def lambda_4F8C():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F8C)

    def lambda_4F9C():

        label("loc_4F9C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4F9C")

    QueueWorkItem2(0x9, 1, lambda_4F9C)
    Sleep(300)
    ClearChrFlags(0xA, 0x80)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xA, 0xFFFF96E2, 0x1F40, 0xE54C, 0xFA0, 0x0)
    Sleep(1000)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "呼呼……\x01",
            "还、还以为死定了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#800F没事比什么都好。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 400)

    ChrTalk(
        0x9,
        "#804F好，所有人都没事吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 400)

    ChrTalk(
        0xB,
        "是、是的，普通员工都……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2P工房长先生！\x02",
    )

    CloseMessageWindow()

    def lambda_50CF():
        OP_6D(-25700, 8000, 55810, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50CF)

    def lambda_50E7():

        label("loc_50E7")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_50E7")

    QueueWorkItem2(0x9, 1, lambda_50E7)

    def lambda_50F8():

        label("loc_50F8")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_50F8")

    QueueWorkItem2(0xB, 1, lambda_50F8)

    def lambda_5109():

        label("loc_5109")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5109")

    QueueWorkItem2(0xA, 1, lambda_5109)

    def lambda_511A():
        OP_8E(0xFE, 0xFFFFA010, 0x1F40, 0xDD9A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_511A)
    Sleep(300)

    def lambda_513A():
        OP_8E(0xFE, 0xFFFF9F16, 0x1F40, 0xDA0C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_513A)
    Sleep(300)

    def lambda_515A():
        OP_8E(0xFE, 0xFFFFA2D6, 0x1F40, 0xE146, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_515A)
    Sleep(300)

    def lambda_517A():
        OP_8E(0xFE, 0xFFFFA52E, 0x1F40, 0xDBA6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_517A)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x9, 0)

    ChrTalk(
        0x9,
        (
            "#802F#2P哦哦，是你们……\x01",
            "已经从亚尔摩回来了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F这骚动究竟是怎么回事！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#804F#2P看来是建筑物内部哪里的\x01",
            "瓦斯泄漏了出来！\x02\x03",
            "从地下到五楼都是烟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F难道是火灾吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#803F#2P灭火装置没有运作，\x01",
            "所以应该不用担心是火灾。\x02\x03",
            "但是，为什么会漏烟，\x01",
            "这一点我实在是想不通……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F那、那个，工房长叔叔。\x01",
            "爷爷他在哪呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)

    ChrTalk(
        0x9,
        "#802F#2P咦，他不是在……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 400)

    ChrTalk(
        0x9,
        (
            "#802F#2P海泽尔。\x01",
            "你不是已经确认过了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 400)

    ChrTalk(
        0xB,
        "那、那个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0xB, 0)

    ChrTalk(
        0xB,
        (
            "普通员工都已经确认过了，\x01",
            "不过唯独拉赛尔博士还没……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#804F#2P你说什么！\x01",
            "他还留在里面吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F工房长先生！\x01",
            "博士的事就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F我们进去看看情况。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 0)

    ChrTalk(
        0x9,
        (
            "#805F#2P不、不好意思。\x01",
            "又要拜托你们俩了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        "#065F我、我也去……！\x02",
    )

    CloseMessageWindow()

    def lambda_5519():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5519)

    def lambda_5527():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5527)

    def lambda_5535():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5535)

    def lambda_5543():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5543)

    def lambda_5551():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5551)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F#2P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#802F#2P提妲？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#062F我对中央工房里面的环境\x01",
            "比较熟悉……\x02\x03",
            "所以所以……\x01",
            "我可以为艾丝蒂尔姐姐你们带路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#2P提妲……\x02\x03",
            "#002F明白了，一起来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#5P不过，一旦有危险的话，\x01",
            "你一定要马上离开，知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#155F那、那个～\x01",
            "我也要跟你们一起……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_56B3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56B3)

    def lambda_56C1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_56C1)

    def lambda_56CF():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_56CF)
    Sleep(400)

    ChrTalk(
        0x101,
        "#002F#2P不行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#5P对不起。\x01",
            "你还是留在这里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#154F唔～好果断的回答啊……\x02\x03",
            "不过没办法了。\x01",
            "你们三个要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#800F#2P假如博士在里面的话，\x01",
            "你们上三楼的工作室就应该能找到他。\x02\x03",
            "先去那里确认一下吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5805():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5805)

    def lambda_5813():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5813)

    def lambda_5821():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5821)
    Sleep(400)

    ChrTalk(
        0x101,
        "#006F嗯，明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F那么我们去了。\x02",
    )

    CloseMessageWindow()
    OP_44(0x21, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x1F, 0x1)
    OP_44(0x1C, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x24, 0x1)
    OP_4B(0x21, 0)
    OP_4B(0x11, 0)
    OP_4B(0x1F, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x17, 0)
    OP_4B(0xB, 0)
    OP_4B(0xA, 0)
    OP_4B(0x24, 0)
    ClearChrFlags(0x1C, 0x40)
    ClearChrFlags(0x1B, 0x40)
    ClearChrFlags(0x17, 0x40)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x22, 0x40)
    ClearChrFlags(0x23, 0x40)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    OP_4B(0xA, 255)
    OP_4B(0x9, 255)
    OP_4B(0xB, 255)
    OP_4B(0x8, 255)
    OP_43(0x9, 0x0, 0x0, 0x3)
    OP_43(0xA, 0x0, 0x0, 0x3)
    OP_43(0xB, 0x0, 0x0, 0x3)
    OP_8C(0x8, 270, 0)
    SetMapFlags(0x2000000)
    SetMapFlags(0x800)
    OP_A2(0x52C)
    EventEnd(0x0)
    Return()

    # Function_47_4AD9 end

    def Function_48_5917(): pass

    label("Function_48_5917")

    EventBegin(0x0)
    OP_6D(-35220, 10000, 59310, 0)
    OP_4A(0x21, 0)
    OP_4A(0x11, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x21, 0)
    OP_4A(0x11, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x17, 0)
    OP_4A(0xB, 0)
    OP_4A(0xA, 0)
    OP_4A(0x24, 0)
    SetChrPos(0x1C, -26070, 8000, 62840, 63)
    SetChrPos(0x1B, -25060, 8000, 63650, 180)
    SetChrPos(0x24, -24740, 8000, 62540, 3)
    SetChrPos(0xB, -37650, 10000, 59010, 0)
    SetChrPos(0xA, -28440, 8000, 62590, 129)
    SetChrPos(0x9, -26520, 8000, 57300, 0)
    SetChrPos(0x101, -34600, 10000, 59260, 90)
    SetChrPos(0x106, -35290, 10000, 58430, 90)
    SetChrPos(0x102, -35240, 10000, 60170, 90)
    SetChrPos(0x107, -35880, 10000, 59390, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -26240, 8000, 58320, 270)
    SetChrPos(0x8, -27270, 8000, 58010, 270)
    OP_4A(0x9, 255)
    OP_4A(0x8, 255)

    def lambda_5A3E():

        label("loc_5A3E")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5A3E")

    QueueWorkItem2(0x8, 1, lambda_5A3E)

    def lambda_5A4F():

        label("loc_5A4F")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5A4F")

    QueueWorkItem2(0x9, 1, lambda_5A4F)

    def lambda_5A60():
        OP_8E(0xFE, 0xFFFF9232, 0x1F40, 0xE6AA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_5A60)

    def lambda_5A7B():
        OP_8E(0xFE, 0xFFFF9458, 0x1F40, 0xEA1A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A7B)

    def lambda_5A96():
        OP_8E(0xFE, 0xFFFF9764, 0x1F40, 0xED3A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5A96)

    def lambda_5AB1():
        OP_8E(0xFE, 0xFFFF8F30, 0x1F40, 0xEC86, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5AB1)

    def lambda_5ACC():
        OP_6D(-27780, 8000, 59800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5ACC)

    def lambda_5AE4():
        OP_6B(2700, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_5AE4)
    FadeToBright(1000, 0)

    def lambda_5AFD():

        label("loc_5AFD")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_5AFD")

    QueueWorkItem2(0x106, 1, lambda_5AFD)

    def lambda_5B0E():

        label("loc_5B0E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5B0E")

    QueueWorkItem2(0x101, 1, lambda_5B0E)

    def lambda_5B1F():

        label("loc_5B1F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5B1F")

    QueueWorkItem2(0x102, 1, lambda_5B1F)

    def lambda_5B30():

        label("loc_5B30")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5B30")

    QueueWorkItem2(0x107, 1, lambda_5B30)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x8,
        "#151F啊，小艾你们出来了～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#801F哦哦，你们没事吧。\x02\x03",
            "刚才军队的人从里面走出来，\x01",
            "我还在想出什么事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#055F#1P军队的人……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F等、等一下！\x01",
            "不是穿黑衣服的家伙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#802F你说什么呀？\x02\x03",
            "是身着蓝白色军装、\x01",
            "礼仪端正的王国军军人啊……\x02\x03",
            "听说他们是从\x01",
            "艾尔·雷登关所派来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#151F从那军装来看，\x01",
            "他们的确是女王陛下的亲卫队呢～\x02\x03",
            "他们样子好帅哦～\x01",
            "我毫不犹豫地拍了照片呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F亲卫队……的人！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F就是在卢安\x01",
            "把市长逮捕的那些军人吧。\x02\x03",
            "但是，他们怎么会在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#062F那、那个！\x02\x03",
            "工房长叔叔，\x01",
            "那些人没带着爷爷吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#805F带、带着拉赛尔博士！？\x02\x03",
            "没、没有……\x01",
            "可是他们带着很大包的货物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F没错，就是他们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F#1P那些杂碎……\x01",
            "在导力梯里换成军服吗……\x02\x03",
            "#056F哼，太瞧不起人了吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#802F等、等一下！\x01",
            "这到底是怎么回事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#016F详细情况我们之后会向您汇报。\x02\x03",
            "请问工房长先生，\x01",
            "那些军人往哪个方向去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#805F说、说是有急事，\x01",
            "往城镇市街区方向去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#054F#1P快追！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x106, 0x40)

    def lambda_603E():
        OP_8E(0xFE, 0xFFFFCC7A, 0x1F40, 0xEB1E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_603E)
    Sleep(200)

    ChrTalk(
        0x101,
        "#005F决不能让他们逃走！\x02",
    )

    CloseMessageWindow()

    def lambda_608A():
        OP_8E(0xFE, 0xFFFFCC7A, 0x1F40, 0xEB1E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_608A)
    Sleep(400)

    def lambda_60AA():
        OP_8E(0xFE, 0xFFFFCC7A, 0x1F40, 0xEB1E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_60AA)
    Sleep(100)

    def lambda_60CA():
        OP_8E(0xFE, 0xFFFFCC7A, 0x1F40, 0xEB1E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_60CA)
    Sleep(2000)
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    SoundDistance(0xA0, 0xFFFFEDF4, 0x14C8, 0xE790, 0x2710, 0x7530, 0x1, 0x0)
    Sleep(500)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "虽然艾丝蒂尔他们\x01",
            "分头在蔡斯市的市街区寻找犯人的踪迹……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "但即使是挨家挨户地寻找，\x01",
            "仍然没能找到博士和绑架博士的黑衣人。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不久，位于湖畔上的雷斯顿要塞接到通报，\x01",
            "派出了王国军的部队前来中央工房……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    ClearMapFlags(0x40000000)
    ClearMapFlags(0x2000000)
    OP_A2(0x536)
    OP_28(0x41, 0x1, 0x40)
    ClearMapFlags(0x800)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3115   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_48_5917 end

    def Function_49_6273(): pass

    label("Function_49_6273")

    EventBegin(0x0)
    OP_6D(-36480, 10000, 59730, 0)
    OP_67(0, 7190, -10000, 0)
    OP_6B(3350, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x11, 0xFF)
    SetChrPos(0x11, -23800, 10000, 46930, 180)
    OP_43(0x11, 0x0, 0x0, 0x3)
    RemoveParty(0xF, 0xFF)
    SetChrPos(0x101, -34420, 10000, 58850, 270)
    SetChrPos(0x107, -34550, 10000, 57970, 315)
    SetChrPos(0x106, -33590, 10000, 59410, 270)
    SetChrPos(0x102, -34780, 10000, 59820, 225)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -36000, 10000, 58980, 90)
    OP_4A(0x8, 255)
    OP_6F(0x0, 60)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#153F#1P啊，对了～\x01",
            "还得去买感光结晶回路才行呢。\x02\x03",
            "#150F那我先告辞啦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，嗯。\x01",
            "朵洛希也辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#154F#1P没有啦。\x01",
            "我可是一点忙也没帮上呢～\x02\x03",
            "我也会去问问编辑部，\x01",
            "调查看看有没有什么情报。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(
        0x8,
        (
            "#150F#1P所以……\x01",
            "小提，打起精神来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊……\x02\x03",
            "好的……\x01",
            "谢谢……朵洛希姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#150F#1P不用担心啦～\x01",
            "小艾和小约还有红头发大哥\x01",
            "一定会平安无事地救出你爷爷的。\x02\x03",
            "#151F那么，再见啦～\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    def lambda_652F():
        OP_6D(-35480, 10000, 59730, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_652F)
    OP_8E(0x8, 0xFFFF6D02, 0x2710, 0xE66E, 0xBB8, 0x0)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x8, 0x2)

    ChrTalk(
        0x107,
        "#063F…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_6581():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_6581)

    def lambda_658F():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_658F)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        (
            "#006F#5P提妲……\x02\x03",
            "#006F打起精神来吧，\x01",
            "博士他一定会没事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P是啊，他们应该不会\x01",
            "伤害王国第一的天才学者的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x107,
        (
            "#063F艾丝蒂尔姐姐、约修亚哥哥……\x02\x03",
            "#067F嗯……是呢。\x01",
            "爷爷一定会没事的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#552F…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        "#004F#5P怎么啦，又板着一张严肃脸？\x02",
    )

    CloseMessageWindow()

    def lambda_6710():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6710)

    def lambda_671E():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_671E)

    ChrTalk(
        0x106,
        (
            "#053F……没什么。\x02\x03",
            "#050F时间紧迫，\x01",
            "我们快点去协会吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x41, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_49_6273 end

    def Function_50_6778(): pass

    label("Function_50_6778")

    EventBegin(0x0)
    OP_6D(-22950, 8000, 63790, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, -22960, 8000, 73260, 0)
    SetChrPos(0x101, -21990, 8000, 74030, 0)
    SetChrPos(0x107, -23770, 8000, 73860, 0)

    def lambda_67F0():
        OP_8E(0xFE, 0xFFFFA646, 0x1F40, 0xF5F0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_67F0)
    Sleep(300)

    def lambda_6810():
        OP_8E(0xFE, 0xFFFFA934, 0x1F40, 0xF9BA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6810)
    Sleep(300)

    def lambda_6830():
        OP_8E(0xFE, 0xFFFFA4C0, 0x1F40, 0xFABE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_6830)
    FadeToBright(1000, 0)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 0, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 135, 400)

    ChrTalk(
        0x102,
        (
            "#010F接下来，\x01",
            "我们先去游击士协会一趟吧。\x02\x03",
            "说不定雾香小姐已经问到\x01",
            "有关黑衣人那艘飞艇的情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，如果能从王国军那里\x01",
            "得到什么情报就好了……\x02\x03",
            "#004F啊，提妲也一起来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F那、那个……\x02\x03",
            "不好意思呢。\x01",
            "我想去照看阿加特大哥哥。\x02\x03",
            "他还没醒过来，\x01",
            "我有点放心不下呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F提妲……\x02\x03",
            "#001F明白了。\x01",
            "博士的事就交给我们吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F对不起……\x01",
            "我老是给姐姐你们添麻烦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F你这孩子真是的～\x01",
            "又在跟我们客气起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F虽然阿加特兄现在还没醒来，\x01",
            "不过只要有朋友陪在旁边，\x01",
            "自己休息的时候也会安心许多吧。\x02\x03",
            "阿加特兄就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560F嗯、嗯……！\x02",
    )

    CloseMessageWindow()

    def lambda_6B54():

        label("loc_6B54")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_6B54")

    QueueWorkItem2(0x101, 1, lambda_6B54)

    def lambda_6B65():

        label("loc_6B65")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_6B65")

    QueueWorkItem2(0x102, 1, lambda_6B65)
    OP_8C(0x107, 225, 400)

    def lambda_6B7D():
        OP_6C(270000, 2000)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_6B7D)

    def lambda_6B8D():
        OP_6D(-22510, 8000, 63590, 2000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_6B8D)
    OP_8E(0x107, 0xFFFF9124, 0x1F40, 0xEDBC, 0x1388, 0x0)
    OP_8E(0x107, 0xFFFF770C, 0x2710, 0xE95C, 0x1388, 0x0)
    SetChrFlags(0x107, 0x80)

    ChrTalk(
        0x101,
        (
            "#006F啊啊～\x01",
            "提妲这孩子真是又坚强又可爱。\x02\x03",
            "对那个爱闹别扭的刀子嘴\x01",
            "根本用不着那么温柔嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F好了好了，别吃醋了。\x02\x03",
            "说起来，\x01",
            "你和阿加特兄性格倒挺相似的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F啊！？\x02\x03",
            "#009F真、真讨厌～\x01",
            "我和那家伙哪里相似了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F行事比较冲动啦，\x01",
            "又爱做老好人啦。\x02\x03",
            "#010F阿加特兄虽然说话刻薄了点，\x01",
            "但却很会为对方着想。\x02\x03",
            "这一点，\x01",
            "我想提妲也应该很清楚吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F唔唔……\x01",
            "虽然有点难以理解……\x02\x03",
            "#007F不说这个了，\x01",
            "总之先去协会问问看吧。\x02\x03",
            "希望在那刀子嘴伤势康复之前，\x01",
            "能够查到什么线索，然后做点成绩给他看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F哈哈，是啊。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x107, -22820, 8000, 62610, 0)
    EventEnd(0x0)
    RemoveParty(0x6, 0xFF)
    Return()

    # Function_50_6778 end

    def Function_51_6ECF(): pass

    label("Function_51_6ECF")

    ClearMapFlags(0x2000000)
    EventBegin(0x0)
    OP_6D(-23500, 8000, 69230, 0)
    OP_67(0, 8490, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(306000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -24660, 8000, 82550, 0)
    SetChrPos(0x102, -22920, 8000, 83030, 0)

    def lambda_6F3B():
        OP_8E(0xFE, 0xFFFFA146, 0x1F40, 0x10E28, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F3B)
    Sleep(500)

    def lambda_6F5B():
        OP_8E(0xFE, 0xFFFFA7CC, 0x1F40, 0x111DE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F5B)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        "#007F哈啊～吓了我一跳呢。\x02",
    )

    WaitChrThread(0x101, 0x1)
    TurnDirection(0x102, 0x101, 400)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F再磨磨蹭蹭的话，\x01",
            "情报部那些人就要过来了……\x02\x03",
            "我们直接出城吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F嗯，知道了。\x02\x03",
            "唔……去王都的话，\x01",
            "应该从东边的街道走吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F没错，沿着利塔街道往北走，\x01",
            "到达『圣海姆门』就可以了。\x02\x03",
            "穿过大门，\x01",
            "就进入王都格兰赛尔地区了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x54, 0x1, 0x10)
    OP_20(0x5DC)
    Sleep(500)
    EventEnd(0x0)
    OP_1D(0xD)
    Return()

    # Function_51_6ECF end

    def Function_52_7169(): pass

    label("Function_52_7169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_END)), "loc_7264")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71E4")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F我们最好不要靠近飞艇坪了。\x01",
            "　\x02\x03",
            "还是赶快出城去吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7246")

    label("loc_71E4")


    ChrTalk(
        0x101,
        (
            "#002F……情报部的人要从飞艇坪过来了。\x01",
            "　\x02\x03",
            "还是不要靠近为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7246")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_7382")

    label("loc_7264")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x35E)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7295")
    Call(0, 53)
    Jump("loc_7382")

    label("loc_7295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7382")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7309")

    ChrTalk(
        0x102,
        (
            "#012F我担心博士的情况。\x01",
            "赶快去工房里面调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7367")

    label("loc_7309")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#012F我担心博士的情况。\x01",
            "赶快去工房里面调查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7367")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7382")

    Return()

    # Function_52_7169 end

    def Function_53_7383(): pass

    label("Function_53_7383")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x35E)"), scpexpr(EXPR_END)), "loc_73B4")
    OP_A2(0x1C)
    Jump("loc_73B7")

    label("loc_73B4")

    OP_A2(0x1A)

    label("loc_73B7")

    Jump("loc_73EC")

    label("loc_73BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x35E)"), scpexpr(EXPR_END)), "loc_73EC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73E9")
    OP_A2(0x1C)
    Jump("loc_73EC")

    label("loc_73E9")

    OP_A2(0x1B)

    label("loc_73EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_763C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_755D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_7486")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F我说，艾丝蒂尔。\x01",
            "还是先把资料室的书还回去吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#008F啊，对、对啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_755A")

    label("loc_7486")

    OP_A2(0x19)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，\x01",
            "说起来我们还没有把资料室的书还回去呢。\x02\x03",
            "在办理搭乘手续之前\x01",
            "赶快去一趟中央工房吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，对了。\x01",
            "要赶快去一趟中央工房。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_755A")

    Jump("loc_7639")

    label("loc_755D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_75AA")

    ChrTalk(
        0x102,
        (
            "#010F在办理搭乘手续之前\x01",
            "先要把书还给资料室。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7639")

    label("loc_75AA")

    OP_A2(0x19)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F说起来，\x01",
            "我们还没有把资料室的书还回去呢。\x02\x03",
            "在办理搭乘手续之前\x01",
            "赶快去一趟中央工房吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7639")

    Jump("loc_7BE3")

    label("loc_763C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_7868")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7781")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_76DE")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F我说，艾丝蒂尔。\x01",
            "要先去地下工场\x01",
            "把信交给菲小姐啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_777E")

    label("loc_76DE")

    OP_A2(0x19)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，\x01",
            "我们最好先去把信送给菲小姐。\x02\x03",
            "在办理搭乘手续之前\x01",
            "去一趟地下工场吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F哦，对了。\x02",
    )

    CloseMessageWindow()

    label("loc_777E")

    Jump("loc_7865")

    label("loc_7781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_77DA")

    ChrTalk(
        0x102,
        (
            "#010F我们要先去把信交给菲小姐啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7865")

    label("loc_77DA")

    OP_A2(0x19)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F说起来，\x01",
            "还没有还没把信送给菲小姐呢。\x02\x03",
            "在办理搭乘手续之前\x01",
            "赶快去地下工场吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7865")

    Jump("loc_7BE3")

    label("loc_7868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_END)), "loc_7BE3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_794F")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F我说，艾丝蒂尔。\x01",
            "书和信都还没送到呢，\x01",
            "赶快去一趟中央工房吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F对啊。\x02\x03",
            "是二楼的资料室\x01",
            "和地下工场的菲小姐对吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A74")

    label("loc_794F")

    OP_A2(0x19)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F说起来，\x01",
            "我们还没有把书还回资料室……\x02\x03",
            "而且还得把信送给菲小姐。\x01",
            "　\x02\x03",
            "在办理搭乘手续之前\x01",
            "赶快去一趟中央工房吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，对了。\x02\x03",
            "菲小姐在地下工场，\x01",
            "而资料室在二楼对吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A74")

    Jump("loc_7BE3")

    label("loc_7A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_7B24")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F我们还没有把书还回资料室，\x01",
            "而且信也没有送到。\x01",
            "　\x02\x03",
            "要赶快去一趟\x01",
            "中央工房的资料室和地下工场。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BE3")

    label("loc_7B24")

    OP_A2(0x19)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F说起来，\x01",
            "我们还没有把书还回资料室……\x02\x03",
            "而且还得把信送给菲小姐。\x01",
            "　\x02\x03",
            "在办理搭乘手续之前\x01",
            "赶快去中央工房把它们送到吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BE3")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_53_7383 end

    def Function_54_7BFF(): pass

    label("Function_54_7BFF")

    SetPlaceName(0x85) # 蔡斯飞艇坪
    Return()

    # Function_54_7BFF end

    def Function_55_7C03(): pass

    label("Function_55_7C03")

    SetPlaceName(0x81) # 蔡斯飞艇坪
    Return()

    # Function_55_7C03 end

    SaveToFile()

Try(main)
