from ED6ScenarioHelper import *

def main():
    # 王立学院　礼堂

    CreateScenaFile(
        FileName            = 'T2513   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2513.x',
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
        '乔儿',                                 # 9
        '汉斯',                                 # 10
        '拉迪奥老师',                           # 11
        '碧欧拉老师',                           # 12
        '米丽亚老师',                           # 13
        '艾福托老师',                           # 14
        '罗迪',                                 # 15
        '米克',                                 # 16
        '坎诺',                                 # 17
        '雅莉丝',                               # 18
        '帕布尔',                               # 19
        '黛拉',                                 # 20
        '罗基克',                               # 21
        '亚吉鲁',                               # 22
        '罗伊斯',                               # 23
        '莫妮卡',                               # 24
        '塞尔玛',                               # 25
        '莉秋尔',                               # 26
        '巴托姆',                               # 27
        '基诺奇奥',                             # 28
        '德尼斯',                               # 29
        '妮吉塔',                               # 30
        '芙拉瑟',                               # 31
        '蕾娜',                                 # 32
        '勤务员巴克斯',                         # 33
        '侍女蕾妮',                             # 34
        '侍女玲珐',                             # 35
        '拉多公爵',                             # 36
        '科洛多议长',                           # 37
        '王都的主教',                           # 38
        '暗杀者',                               # 39
        '波利',                                 # 40
        '特蕾莎院长',                           # 41
        '达尼艾尔',                             # 42
        '玛丽',                                 # 43
        '克拉姆',                               # 44
        '科林兹校长',                           # 45
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
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH01660 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH01430 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01080 ._CH',             # 07
        'ED6_DT07/CH01580 ._CH',             # 08
        'ED6_DT07/CH01590 ._CH',             # 09
        'ED6_DT07/CH01090 ._CH',             # 0A
        'ED6_DT07/CH01370 ._CH',             # 0B
        'ED6_DT07/CH01080 ._CH',             # 0C
        'ED6_DT07/CH01020 ._CH',             # 0D
        'ED6_DT07/CH02260 ._CH',             # 0E
        'ED6_DT07/CH02270 ._CH',             # 0F
        'ED6_DT07/CH02280 ._CH',             # 10
        'ED6_DT07/CH01350 ._CH',             # 11
        'ED6_DT07/CH02540 ._CH',             # 12
        'ED6_DT07/CH01220 ._CH',             # 13
        'ED6_DT07/CH01570 ._CH',             # 14
        'ED6_DT07/CH01670 ._CH',             # 15
        'ED6_DT07/CH01040 ._CH',             # 16
        'ED6_DT06/CH20069 ._CH',             # 17
        'ED6_DT06/CH20071 ._CH',             # 18
        'ED6_DT07/CH01083 ._CH',             # 19
        'ED6_DT07/CH02590 ._CH',             # 1A
        'ED6_DT07/CH02640 ._CH',             # 1B
        'ED6_DT07/CH02630 ._CH',             # 1C
        'ED6_DT07/CH02570 ._CH',             # 1D
        'ED6_DT07/CH02600 ._CH',             # 1E
        'ED6_DT07/CH02500 ._CH',             # 1F
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH01660P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH01430P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01080P._CP',             # 07
        'ED6_DT07/CH01580P._CP',             # 08
        'ED6_DT07/CH01590P._CP',             # 09
        'ED6_DT07/CH01090P._CP',             # 0A
        'ED6_DT07/CH01370P._CP',             # 0B
        'ED6_DT07/CH01080P._CP',             # 0C
        'ED6_DT07/CH01020P._CP',             # 0D
        'ED6_DT07/CH02260P._CP',             # 0E
        'ED6_DT07/CH02270P._CP',             # 0F
        'ED6_DT07/CH02280P._CP',             # 10
        'ED6_DT07/CH01350P._CP',             # 11
        'ED6_DT07/CH02540P._CP',             # 12
        'ED6_DT07/CH01220P._CP',             # 13
        'ED6_DT07/CH01570P._CP',             # 14
        'ED6_DT07/CH01670P._CP',             # 15
        'ED6_DT07/CH01040P._CP',             # 16
        'ED6_DT06/CH20069P._CP',             # 17
        'ED6_DT06/CH20071P._CP',             # 18
        'ED6_DT07/CH01083P._CP',             # 19
        'ED6_DT07/CH02590P._CP',             # 1A
        'ED6_DT07/CH02640P._CP',             # 1B
        'ED6_DT07/CH02630P._CP',             # 1C
        'ED6_DT07/CH02570P._CP',             # 1D
        'ED6_DT07/CH02600P._CP',             # 1E
        'ED6_DT07/CH02500P._CP',             # 1F
    )

    DeclNpc(
        X                   = 59640,
        Z                   = 1000,
        Y                   = 13450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 66040,
        Z                   = 1000,
        Y                   = 16210,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 9300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2160,
        Z                   = 0,
        Y                   = 8570,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 3320,
        Z                   = 0,
        Y                   = 8570,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -2100,
        Z                   = 0,
        Y                   = 9290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2970,
        Z                   = 0,
        Y                   = 3210,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 5200,
        Z                   = 250,
        Y                   = -4530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -4160,
        Z                   = 0,
        Y                   = 5180,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -5390,
        Z                   = 0,
        Y                   = 3910,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -3890,
        Z                   = 0,
        Y                   = 1240,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -5880,
        Z                   = 0,
        Y                   = 1770,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -470,
        Z                   = 0,
        Y                   = 720,
        Direction           = 192,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -820,
        Z                   = 0,
        Y                   = -3270,
        Direction           = 1,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -3170,
        Z                   = 0,
        Y                   = -1120,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 1130,
        Z                   = 0,
        Y                   = -2530,
        Direction           = 315,
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
        X                   = 1380,
        Z                   = 0,
        Y                   = -300,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -2520,
        Z                   = 0,
        Y                   = -2890,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 3400,
        Z                   = 0,
        Y                   = 3800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 4400,
        Z                   = 0,
        Y                   = 200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 3100,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 6030,
        Z                   = 0,
        Y                   = 2120,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 6230,
        Z                   = 0,
        Y                   = 5420,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 6240,
        Z                   = 0,
        Y                   = 3780,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -510,
        Z                   = 0,
        Y                   = 4270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 61850,
        Z                   = 1000,
        Y                   = 17310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63320,
        Z                   = 1000,
        Y                   = 15250,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 57740,
        Z                   = 1000,
        Y                   = 16980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 58590,
        Z                   = 1000,
        Y                   = 17010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 59600,
        Z                   = 1000,
        Y                   = 16379,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 56830,
        Z                   = 1000,
        Y                   = 16500,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6000,
        Z                   = 200,
        Y                   = 22200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 22900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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


    ScpFunction(
        "Function_0_64A",          # 00, 0
        "Function_1_8CA",          # 01, 1
        "Function_2_8F5",          # 02, 2
        "Function_3_A7D",          # 03, 3
        "Function_4_B1E",          # 04, 4
        "Function_5_C25",          # 05, 5
        "Function_6_C7E",          # 06, 6
        "Function_7_D19",          # 07, 7
        "Function_8_DA4",          # 08, 8
        "Function_9_E22",          # 09, 9
        "Function_10_E9D",         # 0A, 10
        "Function_11_ECA",         # 0B, 11
        "Function_12_F55",         # 0C, 12
        "Function_13_FC2",         # 0D, 13
        "Function_14_102D",        # 0E, 14
        "Function_15_1087",        # 0F, 15
        "Function_16_1121",        # 10, 16
        "Function_17_123D",        # 11, 17
        "Function_18_12C5",        # 12, 18
        "Function_19_131B",        # 13, 19
        "Function_20_1385",        # 14, 20
        "Function_21_13D0",        # 15, 21
        "Function_22_144D",        # 16, 22
        "Function_23_1488",        # 17, 23
        "Function_24_1672",        # 18, 24
        "Function_25_17EF",        # 19, 25
        "Function_26_18E7",        # 1A, 26
        "Function_27_1992",        # 1B, 27
        "Function_28_1A30",        # 1C, 28
        "Function_29_2355",        # 1D, 29
        "Function_30_430B",        # 1E, 30
        "Function_31_625F",        # 1F, 31
        "Function_32_62B7",        # 20, 32
        "Function_33_631E",        # 21, 33
        "Function_34_638A",        # 22, 34
        "Function_35_63F6",        # 23, 35
        "Function_36_6462",        # 24, 36
        "Function_37_6483",        # 25, 37
    )


    def Function_0_64A(): pass

    label("Function_0_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_654")
    Jump("loc_884")

    label("loc_654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_832")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
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
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 590, 0, 4100, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -820, 0, 4100, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_82F")
    OP_51(0x8, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x9, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0xA, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0xB, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0xC, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0xD, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0xE, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0xF, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x10, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x14, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x15, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x16, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x17, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x18, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x19, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x20, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_82F")

    Jump("loc_884")

    label("loc_832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_83C")
    Jump("loc_884")

    label("loc_83C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_846")
    Jump("loc_884")

    label("loc_846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_850")
    Jump("loc_884")

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_85F")
    ClearChrFlags(0x20, 0x80)
    Jump("loc_884")

    label("loc_85F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_869")
    Jump("loc_884")

    label("loc_869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_873")
    Jump("loc_884")

    label("loc_873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_87D")
    Jump("loc_884")

    label("loc_87D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_884")

    label("loc_884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_89B")
    OP_A3(0x3FA)
    Event(0, 28)
    OP_B1("t2513_n")

    label("loc_89B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_8B2")
    OP_A3(0x3FB)
    Event(0, 29)
    OP_B1("t2513_n")

    label("loc_8B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_8C9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FD)
    Event(0, 30)

    label("loc_8C9")

    Return()

    # Function_0_64A end

    def Function_1_8CA(): pass

    label("Function_1_8CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EB")
    OP_B1("t2513_y")
    Jump("loc_8F4")

    label("loc_8EB")

    OP_B1("t2513_n")

    label("loc_8F4")

    Return()

    # Function_1_8CA end

    def Function_2_8F5(): pass

    label("Function_2_8F5")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_925")
    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_A67")

    label("loc_925")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93E")
    OP_99(0xFE, 0x1, 0x7, 0x514)
    Jump("loc_A67")

    label("loc_93E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_957")
    OP_99(0xFE, 0x2, 0x7, 0x4E2)
    Jump("loc_A67")

    label("loc_957")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_970")
    OP_99(0xFE, 0x3, 0x7, 0x4B0)
    Jump("loc_A67")

    label("loc_970")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_989")
    OP_99(0xFE, 0x4, 0x7, 0x47E)
    Jump("loc_A67")

    label("loc_989")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A2")
    OP_99(0xFE, 0x5, 0x7, 0x44C)
    Jump("loc_A67")

    label("loc_9A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BB")
    OP_99(0xFE, 0x6, 0x7, 0x41A)
    Jump("loc_A67")

    label("loc_9BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D4")
    OP_99(0xFE, 0x0, 0x7, 0x54B)
    Jump("loc_A67")

    label("loc_9D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9ED")
    OP_99(0xFE, 0x1, 0x7, 0x519)
    Jump("loc_A67")

    label("loc_9ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A06")
    OP_99(0xFE, 0x2, 0x7, 0x4E7)
    Jump("loc_A67")

    label("loc_A06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F")
    OP_99(0xFE, 0x3, 0x7, 0x4B5)
    Jump("loc_A67")

    label("loc_A1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A38")
    OP_99(0xFE, 0x4, 0x7, 0x483)
    Jump("loc_A67")

    label("loc_A38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A51")
    OP_99(0xFE, 0x5, 0x7, 0x451)
    Jump("loc_A67")

    label("loc_A51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A67")
    OP_99(0xFE, 0x6, 0x7, 0x41F)

    label("loc_A67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7C")
    OP_99(0xFE, 0x0, 0x7, 0x4B0)
    Jump("loc_A67")

    label("loc_A7C")

    Return()

    # Function_2_8F5 end

    def Function_3_A7D(): pass

    label("Function_3_A7D")

    TalkBegin(0xA)

    ChrTalk(
        0xFE,
        (
            "各位老师和同学\x01",
            "真的是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次学园祭\x01",
            "没有辜负王立学院的盛名。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_3_A7D end

    def Function_4_B1E(): pass

    label("Function_4_B1E")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD8")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "大家真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "每个人都尽全力努力了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C21")

    label("loc_BD8")


    ChrTalk(
        0xFE,
        (
            "这次结束后，\x01",
            "就和米丽亚一起去城里玩吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C21")

    TalkEnd(0xB)
    Return()

    # Function_4_B1E end

    def Function_5_C25(): pass

    label("Function_5_C25")

    TalkBegin(0xC)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "大家都干得很不错呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "就算他们合格了吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_5_C25 end

    def Function_6_C7E(): pass

    label("Function_6_C7E")

    TalkBegin(0xD)

    ChrTalk(
        0xFE,
        "能顺利地完成真是太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明天开始大家\x01",
            "还是要努力学习哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_6_C7E end

    def Function_7_D19(): pass

    label("Function_7_D19")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6E")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "好，庆祝吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "大家痛快地玩吧，痛快地玩吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_DA0")

    label("loc_D6E")


    ChrTalk(
        0xFE,
        (
            "明天开始又要上课了，\x01",
            "现实在等着我们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    label("loc_DA0")

    TalkEnd(0xE)
    Return()

    # Function_7_D19 end

    def Function_8_DA4(): pass

    label("Function_8_DA4")

    TalkBegin(0xF)

    ChrTalk(
        0xFE,
        "学园祭已经结束了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那干嘛还要特地\x01",
            "聚在一起那么吵闹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我好想快点回去啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xF)
    Return()

    # Function_8_DA4 end

    def Function_9_E22(): pass

    label("Function_9_E22")

    TalkBegin(0x10)

    ChrTalk(
        0xFE,
        "好像失去了什么的感觉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，为学园祭做准备的\x01",
            "那段时间是最快乐的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_9_E22 end

    def Function_10_E9D(): pass

    label("Function_10_E9D")

    TalkBegin(0x11)

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "庆祝胜利真是好开心啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x11)
    Return()

    # Function_10_E9D end

    def Function_11_ECA(): pass

    label("Function_11_ECA")

    TalkBegin(0x12)

    ChrTalk(
        0xFE,
        (
            "准备花了那么多时间，\x01",
            "今天却是一眨眼就过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "客人们看起来很高兴啊。\x01",
            "我自己也很高兴。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_11_ECA end

    def Function_12_F55(): pass

    label("Function_12_F55")

    TalkBegin(0x13)

    ChrTalk(
        0xFE,
        (
            "这几天虽然很忙，\x01",
            "但我很努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还是很有成就感的。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_12_F55 end

    def Function_13_FC2(): pass

    label("Function_13_FC2")

    TalkBegin(0x14)

    ChrTalk(
        0xFE,
        (
            "我家在卢安，\x01",
            "好想提前回去呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过今天就趁着余兴一起庆祝吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_13_FC2 end

    def Function_14_102D(): pass

    label("Function_14_102D")

    TalkBegin(0x15)

    ChrTalk(
        0xFE,
        "顺利地结束了啊……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x15)
    Return()

    # Function_14_102D end

    def Function_15_1087(): pass

    label("Function_15_1087")

    TalkBegin(0x16)

    ChrTalk(
        0xFE,
        (
            "击剑部的冰淇淋店\x01",
            "反响十分好哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我很高兴，\x01",
            "因为来学园祭的孩子们那么开心。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    # Function_15_1087 end

    def Function_16_1121(): pass

    label("Function_16_1121")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121F")
    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "嘿嘿。\x01",
            "啊，好开心啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，学园祭……\x01",
            "因为一年只有一次，\x01",
            "大家齐心协力做这件事才会十分开心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是每天都这样，\x01",
            "大家一定会累死了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1239")

    label("loc_121F")


    ChrTalk(
        0xFE,
        (
            "嘿嘿。\x01",
            "啊，好开心啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1239")

    TalkEnd(0x17)
    Return()

    # Function_16_1121 end

    def Function_17_123D(): pass

    label("Function_17_123D")

    TalkBegin(0x18)

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "真是个不能不参加的活动呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家都尽力了，\x01",
            "这就是最好的结局。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x18)
    Return()

    # Function_17_123D end

    def Function_18_12C5(): pass

    label("Function_18_12C5")

    TalkBegin(0x19)

    ChrTalk(
        0xFE,
        "啊，是前辈们呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不论舞台剧还是冰淇淋店都很成功。\x01",
            "莉秋尔，非常开心呢！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x19)
    Return()

    # Function_18_12C5 end

    def Function_19_131B(): pass

    label("Function_19_131B")

    TalkBegin(0x1A)

    ChrTalk(
        0xFE,
        "哈哈，我也非常开心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "舞台剧也非常好哦。\x01",
            "真是辛苦大家了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1A)
    Return()

    # Function_19_131B end

    def Function_20_1385(): pass

    label("Function_20_1385")

    TalkBegin(0x1B)

    ChrTalk(
        0xFE,
        "呼，好累呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "快点回家睡觉吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1B)
    Return()

    # Function_20_1385 end

    def Function_21_13D0(): pass

    label("Function_21_13D0")

    TalkBegin(0x1C)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "今天不看书也不要紧吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为我有\x01",
            "平时的积累啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1C)
    Return()

    # Function_21_13D0 end

    def Function_22_144D(): pass

    label("Function_22_144D")

    TalkBegin(0x1D)

    ChrTalk(
        0xFE,
        "真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "基诺奇奥\x01",
            "就只会打哈欠……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1D)
    Return()

    # Function_22_144D end

    def Function_23_1488(): pass

    label("Function_23_1488")

    TalkBegin(0x1E)
    OP_4A(0x1F, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D2")
    OP_A2(0x14)
    OP_A2(0x15)

    ChrTalk(
        0x1E,
        (
            "真是的，都怪你，\x01",
            "让我忙得焦头烂额。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "老爷子也很\x01",
            "感谢你们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "呵呵，得到你的夸奖真是光荣。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "我只是为了\x01",
            "锻炼芙拉瑟你嘛。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x10)
    Jump("loc_166A")

    label("loc_15D2")


    ChrTalk(
        0x1E,
        "唉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "哎呀，你为什么叹气啊？\x01",
            "有烦恼的话可以和我谈。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x1E,
        "求你了，放过我吧……\x02",
    )

    CloseMessageWindow()

    label("loc_166A")

    OP_4B(0x1F, 255)
    TalkEnd(0x1E)
    Return()

    # Function_23_1488 end

    def Function_24_1672(): pass

    label("Function_24_1672")

    TalkBegin(0x1F)
    OP_4A(0x1E, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BC")
    OP_A2(0x14)
    OP_A2(0x15)

    ChrTalk(
        0x1E,
        (
            "真是的，都怪你，\x01",
            "让我忙得焦头烂额。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "老爷子也很\x01",
            "感谢你们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "呵呵，得到你的夸奖真是光荣。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "我只是为了\x01",
            "锻炼芙拉瑟你嘛。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x10)
    Jump("loc_17E7")

    label("loc_17BC")


    ChrTalk(
        0xFE,
        "呵呵呵……\x02",
    )

    CloseMessageWindow()

    label("loc_17E7")

    OP_4B(0x1E, 255)
    TalkEnd(0x1F)
    Return()

    # Function_24_1672 end

    def Function_25_17EF(): pass

    label("Function_25_17EF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1886")
    OP_A2(0x16)

    ChrTalk(
        0xFE,
        (
            "#640F哎？\x01",
            "你们还在这里啊。\x02\x03",
            "不赶快回到卢安没有关系吗？\x01",
            "　\x02\x03",
            "如果想参加庆祝会的话十分欢迎哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E3")

    label("loc_1886")


    ChrTalk(
        0xFE,
        (
            "#640F不赶快回到卢安\x01",
            "没有关系吗？\x02\x03",
            "如果想参加庆祝会的话十分欢迎哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E3")

    TalkEnd(0x8)
    Return()

    # Function_25_17EF end

    def Function_26_18E7(): pass

    label("Function_26_18E7")

    TalkBegin(0x9)

    ChrTalk(
        0xFE,
        (
            "#730F哦，\x01",
            "你们是不是舍不得庆祝会啊？\x02\x03",
            "今天全部\x01",
            "由老师们请客呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_26_18E7 end

    def Function_27_1992(): pass

    label("Function_27_1992")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1A2C")

    ChrTalk(
        0xFE,
        (
            "我的工作就是\x01",
            "管理学院的设施和用品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特别是在学园祭前\x01",
            "要好好检查才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A2C")

    TalkEnd(0x20)
    Return()

    # Function_27_1992 end

    def Function_28_1A30(): pass

    label("Function_28_1A30")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_6D(-410, 4000, -4600, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(3720, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 850, 1000, 14010, 270)
    SetChrPos(0x105, -960, 1000, 14000, 90)
    SetChrPos(0x8, -80, 1000, 13250, 0)
    SetChrChipByIndex(0x101, 14)
    SetChrChipByIndex(0x105, 15)
    SetChrChipByIndex(0x102, 16)
    FadeToBright(1000, 0)
    SetPlaceName(0x5F) # 王立学院　礼堂
    OP_6D(910, 2000, 12490, 4000)
    Fade(500)
    OP_6D(60050, 2310, 14620, 0)
    OP_67(0, 2930, -10000, 0)
    OP_6B(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x101, 61000, 1000, 14250, 225)
    SetChrPos(0x105, 59080, 1000, 14210, 135)
    SetChrPos(0x8, 60000, 1000, 13140, 45)
    SetChrPos(0x102, 67180, 1000, 16860, 270)
    SetChrPos(0x9, 67180, 1000, 16860, 270)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#340F#2P嗯～这就是戏服啊。\x02\x03",
            "刚才说要演骑士，\x01",
            "我还以为要穿铠甲什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#644F#3P因为穿甲胄的话，\x01",
            "会妨碍到演员动作的流畅度。\x02\x03",
            "所以我们就照现在\x01",
            "王室亲卫队的制服式样设计了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#340F#2P哦，是这样啊。\x02\x03",
            "#341F科洛丝是短发，\x01",
            "感觉正适合这角色呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#351F#1P呵呵，谢谢。\x02\x03",
            "艾丝蒂尔也很适合呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#348F#2P嘿嘿，是吗？\x02\x03",
            "对了……\x01",
            "为什么我们的衣服颜色不同？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#350F#1P我演的是\x01",
            "平民的『苍骑士奥斯卡』。\x02\x03",
            "艾丝蒂尔演的是\x01",
            "贵族的『红骑士尤利乌斯』。\x02\x03",
            "这是双方势力的代表色。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#340F#2P哦～原来是这样啊。\x02\x03",
            "那么，约修亚是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3P牵挂着两名骑士的\x01",
            "王家『白色公主塞茜莉亚』。\x02\x03",
            "好了公主，请到这边来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3P再、再等一下。\x01",
            "……我还没做好心理准备………\x02",
        )
    )

    CloseMessageWindow()
    OP_66(0x0)

    def lambda_1ECC():
        OP_6D(61500, 2310, 14620, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1ECC)

    def lambda_1EE4():
        OP_6B(850, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1EE4)

    def lambda_1EF4():

        label("loc_1EF4")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1EF4")

    QueueWorkItem2(0x101, 1, lambda_1EF4)

    def lambda_1F05():

        label("loc_1F05")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1F05")

    QueueWorkItem2(0x105, 1, lambda_1F05)

    def lambda_1F16():

        label("loc_1F16")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1F16")

    QueueWorkItem2(0x8, 1, lambda_1F16)

    def lambda_1F27():

        label("loc_1F27")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1F27")

    QueueWorkItem2(0x9, 1, lambda_1F27)

    def lambda_1F38():
        OP_8F(0xFE, 0xF582, 0x3E8, 0x3B10, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1F38)
    Sleep(800)

    def lambda_1F58():
        OP_8F(0xFE, 0xF71C, 0x3E8, 0x3DFE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F58)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 225, 0)
    WaitChrThread(0x9, 0x2)
    Sleep(200)
    OP_8F(0x9, 0xF85C, 0x3E8, 0x378C, 0x7D0, 0x0)
    OP_44(0x9, 0xFF)
    OP_8C(0x9, 315, 0)

    ChrTalk(
        0x102,
        "#363F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#344F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#354F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#643F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#367F#2P拜托了，说点什么吧……\x02\x03",
            "在这种沉默的气氛\x01",
            "呆呆地站着实在是有点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#340F哎呀，怎么说呢……\x02\x03",
            "#341F完全没有不协调的感觉⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#351F我也吃了一惊呢。\x02\x03",
            "#358F啊啊，真的好漂亮……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#731F嗯嗯，自信一点啦。\x02\x03",
            "假如你真的是女孩子，\x01",
            "我恐怕会忍不住上来挑逗你哦㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x102,
        (
            "#368F#2P多谢你们真诚的感想。\x01",
            "不过我可一点都高兴不起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#659F哦呵呵……\x01",
            "这就是我要的效果……\x02\x03",
            "这样的人选安排\x01",
            "一定会受到各方面的认同……\x02\x03",
            "#641F各位，大家要团结一致，\x01",
            "打造最完美的舞台剧哦～！！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#341F#1P#1K好～！\x02",
    )


    ChrTalk(
        0x105,
        "#351F#1K是！\x02",
    )


    ChrTalk(
        0x9,
        "#731F#1K喔！\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    ChrTalk(
        0x102,
        "#367F#2P咳咳……\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由当晚开始，艾丝蒂尔和约修亚\x01",
            "分别住进了学院的女生宿舍和男生宿舍。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_66(0x1)
    OP_28(0x3D, 0x1, 0x80)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2512   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_28_1A30 end

    def Function_29_2355(): pass

    label("Function_29_2355")

    EventBegin(0x0)
    OP_77(0xFF, 0xC8, 0x96, 0x0, 0x0)
    OP_6D(60480, 1000, 9080, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(19000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x101, 60900, 1000, 12690, 270)
    SetChrPos(0x105, 59100, 1000, 12780, 90)
    SetChrPos(0x102, 63020, 1000, 16920, 225)
    SetChrPos(0x8, 58340, 1000, 14950, 0)
    SetChrPos(0x9, 61530, 1000, 15270, 45)
    OP_43(0x102, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0x102, 16)
    SetChrChipByIndex(0x101, 23)
    SetChrChipByIndex(0x105, 24)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x105, 0)
    FadeToBright(1000, 0)

    def lambda_2449():
        OP_6D(60970, 1000, 14570, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2449)

    def lambda_2461():
        OP_6C(30000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2461)
    OP_0D()
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x105, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x105, 0x1000)

    def lambda_2486():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2486)
    OP_99(0x101, 0x1, 0x2, 0x5DC)
    WaitChrThread(0x101, 0x1)

    def lambda_24AF():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_24AF)
    WaitChrThread(0x105, 0x1)
    Sleep(150)

    def lambda_24D4():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24D4)
    OP_99(0x101, 0x1, 0x2, 0x5DC)
    WaitChrThread(0x101, 0x1)

    def lambda_24FD():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_24FD)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    SetChrSubChip(0x101, 0)

    def lambda_2527():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2527)
    OP_99(0x105, 0x1, 0x2, 0x5DC)
    WaitChrThread(0x105, 0x1)

    def lambda_2550():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2550)
    WaitChrThread(0x101, 0x1)
    Sleep(150)

    def lambda_2575():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2575)
    OP_99(0x105, 0x1, 0x2, 0x5DC)
    WaitChrThread(0x105, 0x1)

    def lambda_259E():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_259E)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    SetChrSubChip(0x105, 0)

    def lambda_25C8():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25C8)
    OP_99(0x101, 0x1, 0x2, 0x7D0)
    WaitChrThread(0x101, 0x1)

    def lambda_25F1():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_25F1)
    WaitChrThread(0x105, 0x1)
    Sleep(120)

    def lambda_2616():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2616)
    OP_99(0x101, 0x1, 0x2, 0x7D0)
    WaitChrThread(0x101, 0x1)

    def lambda_263F():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_263F)
    WaitChrThread(0x105, 0x1)
    Sleep(120)

    def lambda_2664():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2664)
    OP_99(0x101, 0x1, 0x2, 0x7D0)
    WaitChrThread(0x101, 0x1)

    def lambda_268D():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_268D)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    SetChrSubChip(0x101, 0)
    FadeToDark(1500, 0, -1)

    def lambda_26C1():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_26C1)
    OP_99(0x105, 0x1, 0x2, 0x7D0)
    WaitChrThread(0x105, 0x1)

    def lambda_26EA():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26EA)
    WaitChrThread(0x101, 0x1)
    Sleep(120)

    def lambda_270F():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_270F)
    OP_99(0x105, 0x1, 0x2, 0x7D0)
    WaitChrThread(0x105, 0x1)

    def lambda_2738():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2738)
    WaitChrThread(0x101, 0x1)
    Sleep(120)

    def lambda_275D():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_275D)
    OP_99(0x105, 0x1, 0x2, 0x7D0)
    WaitChrThread(0x105, 0x1)

    def lambda_2786():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2786)
    WaitChrThread(0x101, 0x1)
    OP_0D()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "而放学后则要进行严格的排练，直到深夜……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，两人忙碌而快乐的校园生活\x01",
            "就在眨眼之间飞快过去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2533   ._SN", 100, 0, 0)
    IdleLoop()
    OP_6D(60050, 2310, 14620, 0)
    OP_67(0, 2930, -10000, 0)
    OP_6B(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 610, 0, -360, 0)
    SetChrPos(0x102, -400, 0, 430, 0)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrChipByIndex(0x101, 14)
    SetChrChipByIndex(0x105, 15)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x105, 0)
    SetChrPos(0x101, 62000, 1000, 14000, 270)
    SetChrPos(0x105, 58000, 1000, 14000, 90)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(2000, 0)
    OP_1D(0x61)
    OP_0D()
    Sleep(1000)

    NpcTalk(
        0x101,
        "红骑士尤利乌斯",
        (
            "#424F#2P挚友啊。\x01",
            "事已至此你我别无选择……\x02\x03",
            "命中注定\x01",
            "我们终要决一雌雄。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x16, 0x0, 0x64)
    SetChrChipByIndex(0x101, 23)
    SetChrSubChip(0x101, 5)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x101,
        "红骑士尤利乌斯",
        (
            "#421F#2P拔剑！\x01",
            "为了彼此所背负的责任！\x02\x03",
            "更为了你我心爱的公主！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x105,
        "苍骑士奥斯卡",
        (
            "#359F#1P所谓命运，\x01",
            "是凭自己的双手开拓的……\x02\x03",
            "本应承担的立场与公主的微笑，\x01",
            "此时此刻是那么的遥远……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x101,
        "红骑士尤利乌斯",
        "#422F#2P你怕了吗，奥斯卡！\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x105,
        "苍骑士奥斯卡",
        (
            "#357F#1P然而，此刻驱使着身体的、\x01",
            "这近乎疯狂的热情究竟是什么？\x02\x03",
            "我似乎再次不可避免地\x01",
            "在此与你一决高下……\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x16, 0x0, 0x64)
    SetChrChipByIndex(0x105, 24)
    SetChrSubChip(0x105, 8)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x105,
        "苍骑士奥斯卡",
        (
            "#352F#1P在以革命之名的暴风雨\x01",
            "将一切吞没之前……\x02\x03",
            "以手中的剑刃决定命运吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x101,
        "红骑士尤利乌斯",
        (
            "#420F#2P啊啊……\x01",
            "空之女神将见证你我二人的灵魂！\x02\x03",
            "来吧，一决胜负！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x105,
        "苍骑士奥斯卡",
        "#356F#1P来吧！\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x105)
    OP_21()

    ChrTalk(
        0x101,
        "#347F#2P哈～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#357F#1P呼……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x16, 0x0, 0x64)
    SetChrChipByIndex(0x101, 14)
    SetChrChipByIndex(0x105, 15)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x105, 0)
    OP_0D()
    OP_1D(0xE)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#341F#2P成功了～㈱\x02\x03",
            "终于准确无误地\x01",
            "完成了这一幕呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#351F#1P呵呵，你的演技真是逼真。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#346F#2P嘿嘿，不过跟科洛丝相比，\x01",
            "我的功夫还差的远呢。\x02\x03",
            "而且，\x01",
            "你又从来不会念错过台词。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#350F#1P那是因为我从很早之前\x01",
            "就开始看剧本了啊。\x02\x03",
            "现在我也总算能\x01",
            "跟得上艾丝蒂尔的动作了。\x02\x03",
            "#351F要你不厌其烦地指点我练剑，\x01",
            "真是太谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#340F#2P你太客气了，\x01",
            "因为你基础本来就很好嘛。\x02\x03",
            "只要你愿意，我想你随时\x01",
            "都能取得游击士的资格的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#355F#1P呵呵，你就别抬举我了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F终于，明天就要正式演出了呢。\x02\x03",
            "不知道特蕾莎老师和孩子们\x01",
            "会不会喜欢呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呵呵，你真的很关心\x01",
            "特蕾莎院长他们呢……\x02\x03",
            "简直就像一家人似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，对不起。\x01",
            "我说错什么话了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F不是呢……\x01",
            "就像艾丝蒂尔所说的那样。\x02\x03",
            "是老师他们让我知道\x01",
            "家人才是世上最宝贵的东西……\x02\x03",
            "因为我刚出生不久，\x01",
            "父母就在一次意外中去世了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F虽然被富裕的亲戚收养，\x01",
            "过着自由自在随心所欲的生活……\x02\x03",
            "但我却从来都不知道，\x01",
            "所谓的家人究竟是什么样的存在。\x02\x03",
            "直到１０年前……\x01",
            "遇到老师他们的那一天开始。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F１０年前……\x02\x03",
            "难道是『百日战役』的时候？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F是的，\x01",
            "那时候我正好来到了卢安。\x02\x03",
            "不仅要逃避帝国军追杀，\x01",
            "而且还和自己的亲戚走散了……\x02\x03",
            "是特蕾莎老师和\x01",
            "她丈夫约瑟夫先生保护了我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F战争结束后，我就被亲戚接回去了。\x01",
            "虽然只是短短的几个月……\x02\x03",
            "但是，特蕾莎老师和约瑟夫叔叔\x01",
            "对我的关心和照顾却是无微不至的……\x02\x03",
            "那时候，我才第一次知道。\x02\x03",
            "拥有父亲和母亲，\x01",
            "是一种什么样的感觉。\x02\x03",
            "全家人能够生活在一起，\x01",
            "又是一种何等温暖的幸福……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F对、对不起……\x02\x03",
            "情不自禁之下，\x01",
            "说了那么一大堆无聊的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不，没这回事呢。\x02\x03",
            "明天的舞台剧……\x01",
            "我们一起加油，来场绝佳的演出吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F……好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F由我来说可能有点自卖自夸，\x01",
            "不过，我想绝对会很精彩的！\x02\x03",
            "不单是我们，\x01",
            "乔儿和汉斯也都很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯，是呢。\x02\x03",
            "不过，功劳最大的\x01",
            "应该还是非约修亚莫属吧。\x02\x03",
            "想不到他的演技居然那么好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯、嗯……\x02\x03",
            "明明那么不情愿，\x01",
            "却还能把公主演得活灵活现呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F不论是发音还是时机的把握，\x01",
            "真的丝毫也不比职业演员逊色呢。\x02\x03",
            "约修亚过去曾经演过戏吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，嗯……\x02\x03",
            "在我和他相遇之前，\x01",
            "有关他的事我自己也不是很清楚。\x02\x03",
            "我不知道他以前经历过什么，\x01",
            "而且，他一直总不想和我说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F啊……\x02\x03",
            "对不起……\x01",
            "问了不该问的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊哈哈，没什么啦。\x02\x03",
            "嗯～约修亚确实就是\x01",
            "那种什么事都能做得很完美的人。\x02\x03",
            "真的总是优哉游哉从容不迫的，\x01",
            "一点儿都不可爱……\x02\x03",
            "倒还是偶尔慌张的时候\x01",
            "才显出他那比较可爱一面～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F呵呵……\x02\x03",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F其实我们两个的角色\x01",
            "换过来扮演或许会比较好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F尤利乌斯和奥斯卡啊。\x02\x03",
            "我觉得奥斯卡还是\x01",
            "由艾丝蒂尔来演比较好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎？为什么？\x02\x03",
            "不过我和贵族出身的尤利乌斯\x01",
            "在身份上的确有点不大相称……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F不，我不是这个意思。\x02\x03",
            "……就是，舞台剧的最后……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哦、哦哦……\x01",
            "是公主对奥斯卡做那个……是吧？\x02\x03",
            "不过，那个不只是对着脸颊吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F虽然是这样没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F真是便宜了约修亚啊～\x02\x03",
            "难道说科洛丝\x01",
            "不想和约修亚演那个？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F我、我不是这个意思！\x02\x03",
            "不过，总觉得有点\x01",
            "对不起你们两个呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F讨、讨厌啦～\x01",
            "别像乔儿那样说这种话嘛。\x02\x03",
            "我和他其实也只是家人关系而已，\x01",
            "反正约修亚也只是把我当作\x01",
            "妹妹那样照顾罢了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F是……这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F他呀，总是站在老爸那边，\x01",
            "把我当作小孩子。\x02\x03",
            "真是气死我了……\x02\x03",
            "总之呢，我觉得你完全\x01",
            "没必要为这种事和我介意！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……啊，你们在这里啊。\x02",
    )

    CloseMessageWindow()

    def lambda_3CDE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CDE)

    def lambda_3CEC():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CEC)

    def lambda_3CFA():
        OP_6D(-150, 1000, 11520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CFA)

    def lambda_3D12():
        OP_8E(0xFE, 0xDC, 0x0, 0x2030, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3D12)
    OP_8E(0x102, 0x514, 0x0, 0x21A2, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        "#000F约、约修亚！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F汉斯也在……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#730F彩排都结束了，\x01",
            "居然还在练习啊。\x02\x03",
            "你们俩还真是卖力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F决斗那场戏，没问题了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F当然，就交给我们吧！\x01",
            "一定让你看到完美无缺的表演！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这样啊……\x01",
            "嗯，那我就拭目以待了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F说起来，\x01",
            "你们难道是来找我们的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#730F是啊，今天是艾丝蒂尔和约修亚\x01",
            "在学院里住的最后一天了。\x02\x03",
            "大家不如一起吃顿晚饭，\x01",
            "也算是为了预祝明天的成功。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，是这样啊。\x02\x03",
            "好，我也赞成！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F也请让我一同参加哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了……\x01",
            "乔儿没和你们在一起吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F你说乔儿啊，\x01",
            "她刚才被校长叫走了……\x02\x03",
            "我去找她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，我也去！\x02\x03",
            "约修亚你们\x01",
            "就先去食堂占位子吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，好的。\x02\x03",
            "那我们就先去食堂吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#730F好！老大。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F谁是你的老大……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)

    def lambda_40AC():
        OP_8E(0xFE, 0x140, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_40AC)
    Sleep(500)
    OP_8E(0x102, 0x140, 0x0, 0x140, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_6D(-410, 1000, 15230, 1000)
    OP_67(0, 9500, -10000, 0)

    ChrTalk(
        0x101,
        (
            "#000F呵呵，看来他们两个\x01",
            "也相处得不错啊。\x02\x03",
            "约修亚他有时候\x01",
            "会有拒人于千里之外的一面，\x01",
            "我本来还有点担心呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F呵呵……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#000F咦？怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#040F不不……\x01",
            "也没什么啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯～好了。\x01",
            "我们先去换衣服吧。\x02\x03",
            "穿成这样招摇过市的话，\x01",
            "实在是有点难为情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F嗯，是呢。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(-35450, 1000, 8010, 0)
    OP_6C(45000, 0)
    RemoveParty(0x1, 0xFF)
    SetChrPos(0x105, -36670, 1000, 6980, 0)
    SetChrPos(0x101, -36420, 1000, 8500, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#000F……好了。\x02\x03",
            "那我们现在\x01",
            "就去接乔儿回来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F好。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_29_2355 end

    def Function_30_430B(): pass

    label("Function_30_430B")

    EventBegin(0x0)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_6D(-63840, 1000, 10070, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -64190, 1000, 9630, 225)
    SetChrPos(0x105, -63900, 1000, 8550, 270)
    SetChrPos(0x102, -65269, 1000, 9930, 180)
    SetChrPos(0x9, -66110, 1000, 8290, 45)
    SetChrPos(0x8, -65560, 1000, 7740, 45)
    OP_44(0x28, 0xFF)
    OP_44(0x2A, 0xFF)
    OP_44(0x2B, 0xFF)
    OP_44(0x29, 0xFF)
    OP_44(0x27, 0xFF)
    OP_44(0x2C, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    SetChrPos(0x28, -66100, 0, 1150, 0)
    SetChrPos(0x2A, -66100, 0, 1150, 0)
    SetChrPos(0x2B, -66100, 0, 1150, 0)
    SetChrPos(0x29, -66100, 0, 1150, 0)
    SetChrPos(0x27, -66100, 0, 1150, 0)
    SetChrPos(0x2C, -66100, 0, 1150, 0)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x2C, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#641F呀～真是辛苦大家了！\x02\x03",
            "由我做导演也许缺乏说服力，\x01",
            "不过这真的是有史以来最棒的舞台剧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F#2P虽然一开始，\x01",
            "因为男女反串而被大家笑……\x02\x03",
            "不过随着剧情的发展，\x01",
            "大家也都认真地观赏起来，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P嗯，是啊。\x01",
            "扮成那样总算是值得了。\x02\x03",
            "#017F不过我再也不想有第二次了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#731F#6P哈哈，别那么说嘛。\x02\x03",
            "摄影部的同学\x01",
            "说拍了好几张剧照……\x02\x03",
            "我可是很看好\x01",
            "公主您的照片销量哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F#1P啊？饶了我吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#649F我想艾丝蒂尔她们的照片\x01",
            "也一定会很畅销的。\x02\x03",
            "男生当然是不用说了，\x01",
            "低年级的女生也都会去买的。\x02\x03",
            "#641F而且买到手的时候还会高喊\x01",
            "『姐姐大人～』呢㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#045F#2P真是的，乔儿你啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#503F#5P……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F#1P咦……？\x02\x03",
            "怎么了，艾丝蒂尔？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x101,
        "#004F#5P#3S哎……？\x02",
    )

    OP_9E(0x101, 0x32, 0x0, 0x12C, 0x1770)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#008F#5P啊，什么？什么事！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#1P不……\x01",
            "我是说你啊……\x02\x03",
            "舞台剧结束之后\x01",
            "就好像神情恍惚的样子，\x01",
            "没事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#730F#6P哎呀，演了一场那么艰苦的决斗，\x01",
            "觉得累也是正常的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#642F如果不舒服的话，\x01",
            "我带你去医务室吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 300)

    ChrTalk(
        0x101,
        (
            "#008F#5P没、没事啦！\x02\x03",
            "怎么说我也是个游击士，\x01",
            "这点程度的辛苦，家常便饭啦。\x02\x03",
            "#503F只是，好像有点失魂落魄的，\x01",
            "或者说，头脑有点混乱什么的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F#2P啊……\x02\x03",
            "艾丝蒂尔，难道……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F#5P你、你别误会啦。\x01",
            "完全不是那么回事……\x02\x03",
            "#504F啊～不管了，总之我完全不在意！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#1P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#1P呵呵……\x01",
            "可以打扰一下吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_4B99():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4B99)

    def lambda_4BA7():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4BA7)

    def lambda_4BB5():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BB5)

    def lambda_4BC3():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BC3)

    def lambda_4BD1():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4BD1)
    Sleep(400)

    def lambda_4BE4():

        label("loc_4BE4")

        TurnDirection(0xFE, 0x2A, 0)
        OP_48()
        Jump("loc_4BE4")

    QueueWorkItem2(0x101, 1, lambda_4BE4)

    def lambda_4BF5():

        label("loc_4BF5")

        TurnDirection(0xFE, 0x29, 0)
        OP_48()
        Jump("loc_4BF5")

    QueueWorkItem2(0x102, 1, lambda_4BF5)

    def lambda_4C06():

        label("loc_4C06")

        TurnDirection(0xFE, 0x2B, 0)
        OP_48()
        Jump("loc_4C06")

    QueueWorkItem2(0x105, 1, lambda_4C06)

    def lambda_4C17():

        label("loc_4C17")

        TurnDirection(0xFE, 0x2B, 0)
        OP_48()
        Jump("loc_4C17")

    QueueWorkItem2(0x8, 1, lambda_4C17)

    def lambda_4C28():

        label("loc_4C28")

        TurnDirection(0xFE, 0x2B, 0)
        OP_48()
        Jump("loc_4C28")

    QueueWorkItem2(0x9, 1, lambda_4C28)

    def lambda_4C39():
        OP_6D(-64769, 1000, 9050, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C39)
    OP_43(0x2B, 0x1, 0x0, 0x20)
    OP_43(0x2A, 0x1, 0x0, 0x21)
    OP_43(0x27, 0x1, 0x0, 0x22)
    OP_43(0x29, 0x1, 0x0, 0x23)
    OP_43(0x28, 0x1, 0x0, 0x1F)
    Sleep(2000)
    OP_44(0x8, 0xFF)

    def lambda_4C7D():
        OP_8E(0xFE, 0xFFFF0268, 0x3E8, 0x19BE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4C7D)
    OP_44(0x9, 0xFF)

    def lambda_4C9C():
        OP_8E(0xFE, 0xFFFEFDE0, 0x3E8, 0x1932, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4C9C)
    WaitChrThread(0x8, 0x2)
    OP_8C(0x8, 270, 400)
    WaitChrThread(0x9, 0x2)
    OP_8C(0x9, 270, 400)
    WaitChrThread(0x27, 0x1)

    ChrTalk(
        0x2B,
        (
            "#771F#4P科洛丝姐姐！\x01",
            "你的奥斯卡演得很帅哦！\x02\x03",
            "那样才叫男人啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x2B, 0)

    ChrTalk(
        0x105,
        "#041F呵呵，谢谢。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x2A, 0x1)

    ChrTalk(
        0x2A,
        (
            "#6P艾丝蒂尔姐姐\x01",
            "也演得好棒呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#6P啊啊，尤利乌斯大人～㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F那、那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#3P约修亚哥哥☆\x01",
            "也很可爱哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "#3P嗯㈱\x01",
            "我都看得入迷了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F啊、啊哈哈……谢谢……\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    WaitChrThread(0x28, 0x1)

    ChrTalk(
        0x28,
        (
            "#750F呵呵，\x01",
            "大家都很高兴呢。\x02\x03",
            "既要在爱情和友情之间作抉择，\x01",
            "又要稳稳屹立于时代洪流中，\x01",
            "这就是剧里描绘出的主人公们啊……\x02\x03",
            "在扣人心弦的决斗后\x01",
            "等待着他们的悲伤考验……\x02\x03",
            "还有最终温馨的大团圆结局……\x02\x03",
            "#751F真的是精彩绝伦的舞台剧呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#641F哎呀～能听到您这么说，\x01",
            "我们的努力也没有白费了。\x02\x03",
            "#644F啊，对了……汉斯。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        "#730F#6P嗯，好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#5P哎呀，怎么了？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    ChrTalk(
        0x8,
        (
            "#648F忽然想起件事。\x02\x03",
            "我们等一下就回来，\x01",
            "你们先慢慢聊一会儿吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#5P嗯、嗯……？\x02",
    )

    CloseMessageWindow()

    def lambda_50C1():

        label("loc_50C1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_50C1")

    QueueWorkItem2(0x28, 1, lambda_50C1)

    def lambda_50D2():

        label("loc_50D2")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_50D2")

    QueueWorkItem2(0x101, 1, lambda_50D2)

    def lambda_50E3():

        label("loc_50E3")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_50E3")

    QueueWorkItem2(0x102, 1, lambda_50E3)

    def lambda_50F4():

        label("loc_50F4")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_50F4")

    QueueWorkItem2(0x105, 1, lambda_50F4)
    OP_8C(0x8, 90, 400)

    def lambda_510C():
        OP_8E(0xFE, 0xFFFF0F42, 0x3E8, 0x193C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_510C)
    Sleep(500)

    def lambda_512C():
        OP_8E(0xFE, 0xFFFF0F42, 0x3E8, 0x193C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_512C)
    WaitChrThread(0x8, 0x2)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x9, 0x2)
    SetChrFlags(0x9, 0x80)
    Sleep(500)
    OP_8E(0x28, 0xFFFEFE26, 0x3E8, 0x1F04, 0x7D0, 0x0)

    ChrTalk(
        0x28,
        (
            "#750F刚才那两个学生\x01",
            "是叫乔儿和汉斯吗？\x02\x03",
            "我记得是科洛丝的朋友，\x01",
            "好像还是学生会的人吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x28, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)

    def lambda_51E9():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51E9)

    def lambda_51F7():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51F7)
    TurnDirection(0x105, 0x28, 400)

    ChrTalk(
        0x105,
        (
            "#040F是的，这次的舞台剧\x01",
            "是由他们负责导演和组织的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#750F是吗……那得谢谢他们呢。\x02\x03",
            "#754F这一定会成为\x01",
            "我们在卢安的美好回忆……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F老师……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F这些孩子还……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x101, 0)
    Sleep(400)

    ChrTalk(
        0x28,
        (
            "#750F嗯……\x01",
            "等回到玛诺利亚村后就告诉他们。\x02\x03",
            "然后，如果快的话，\x01",
            "或许明天就会起程了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F那、那么快！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x28, 400)

    ChrTalk(
        0x2B,
        "#770F#2P什么什么，你们在说什么～？\x02",
    )

    CloseMessageWindow()

    def lambda_53BE():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_53BE)

    def lambda_53CC():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_53CC)
    TurnDirection(0x2A, 0x2B, 400)

    ChrTalk(
        0x2A,
        (
            "没礼貌哦，克拉姆！\x01",
            "大人说话时别乱插嘴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#751F没关系，玛丽。\x02\x03",
            "好了，孩子们。\x01",
            "我们早点回去旅馆吧。\x02\x03",
            "#750F吃完晚饭……\x01",
            "然后再告诉你们好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#774F#2P嗯、嗯……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#750F那么科洛丝……\x01",
            "还有艾丝蒂尔和约修亚。\x02\x03",
            "我们差不多该告辞了。\x02\x03",
            "#751F今天真是感谢你们。\x01",
            "让我们看了那么精彩的演出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F啊，再等等吧。\x01",
            "乔儿他们很快就会回来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        "#1P……打扰了。\x02",
    )

    CloseMessageWindow()

    def lambda_55E5():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_55E5)

    def lambda_55F3():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55F3)

    def lambda_5601():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5601)

    def lambda_560F():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_560F)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x4)
    OP_8E(0x2C, 0xFFFEFDB8, 0x0, 0xEE2, 0x7D0, 0x0)

    def lambda_563B():

        label("loc_563B")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_563B")

    QueueWorkItem2(0x28, 1, lambda_563B)

    def lambda_564C():

        label("loc_564C")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_564C")

    QueueWorkItem2(0x101, 1, lambda_564C)

    def lambda_565D():

        label("loc_565D")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_565D")

    QueueWorkItem2(0x102, 1, lambda_565D)

    def lambda_566E():

        label("loc_566E")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_566E")

    QueueWorkItem2(0x105, 1, lambda_566E)

    def lambda_567F():

        label("loc_567F")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_567F")

    QueueWorkItem2(0x2A, 1, lambda_567F)

    def lambda_5690():

        label("loc_5690")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_5690")

    QueueWorkItem2(0x29, 1, lambda_5690)

    def lambda_56A1():

        label("loc_56A1")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_56A1")

    QueueWorkItem2(0x27, 1, lambda_56A1)
    ClearChrFlags(0x2C, 0x4)
    OP_8E(0x2C, 0xFFFEF5DE, 0x0, 0x1130, 0x7D0, 0x0)
    OP_43(0x8, 0x1, 0x0, 0x24)
    OP_43(0x9, 0x1, 0x0, 0x25)
    OP_8E(0x2C, 0xFFFEF688, 0x3E8, 0x1E64, 0x7D0, 0x0)
    OP_8E(0x2C, 0xFFFEF976, 0x3E8, 0x1EB4, 0x7D0, 0x0)

    ChrTalk(
        0x28,
        "#753F#2P啊，科林兹校长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#780F好久不见了，特蕾莎院长。\x02\x03",
            "难得你来学院一趟，\x01",
            "我却到现在才来跟你打招呼，真是抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#750F#2P校长您太客气了……\x02\x03",
            "#751F能让我们来参加学园祭，\x01",
            "我们已经很高兴了，真的非常感谢您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#780F呵呵，能得到这样的评价，\x01",
            "学生们的努力也算有了回报啊。\x02\x03",
            "……你们的情况我听科洛丝说了。\x01",
            "真的是非常不幸的事件。\x02\x03",
            "所以，通过这次学园祭，\x01",
            "我们也想略尽绵薄之力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        "#753F#2P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        "#781F乔儿。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#644F是。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFEFE26, 0x3E8, 0x1BF8, 0x3E8, 0x0)
    OP_44(0x28, 0xFF)

    def lambda_591C():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_591C)

    def lambda_592A():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_592A)

    def lambda_5938():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5938)

    def lambda_5946():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5946)

    def lambda_5954():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_5954)

    def lambda_5962():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5962)

    def lambda_5970():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_5970)

    def lambda_597E():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_597E)

    def lambda_598C():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_598C)
    TurnDirection(0x28, 0x8, 400)
    Sleep(500)

    ChrTalk(
        0x8,
        "#640F请收下这个。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "乔儿将一个印有王立学院徽章的厚厚信封\x01",
            "交给了特蕾莎院长。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x8, 0xFFFEFDF4, 0x3E8, 0x1A54, 0x3E8, 0x0)

    ChrTalk(
        0x28,
        "#753F#1P这是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#640F这是从来访者筹集得来的捐款，\x01",
            "正好一百万米拉。\x02\x03",
            "请用来重建孤儿院吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x28, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F一、一百万米拉！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F好大的数目……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        "#756F#1P怎、怎么会有这么多……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#781F因为这次有公爵和柏斯市长\x01",
            "等等悉数名人到场参加学园祭。\x02\x03",
            "所以比往年筹到的都要多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#048F校长……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x2C, 400)

    ChrTalk(
        0x28,
        (
            "#755F#2P这、这怎么行！\x02\x03",
            "这钱我绝不能收！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#730F不必客气啦。\x02\x03",
            "每年学园祭筹集到的捐款\x01",
            "都是用于福利活动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#641F如果是用于孤儿院的重建，\x01",
            "捐款的各位也一定会很乐意的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#757F#2P但是……这……\x02\x03",
            "大家实在为我们做了太多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#049F老师……\x01",
            "就请您收下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x28, 0xFF)
    TurnDirection(0x28, 0x105, 400)

    ChrTalk(
        0x28,
        "#756F#3P科洛丝……可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#049F老师踌躇的心情我很明白。\x02\x03",
            "#047F但是……\x01",
            "请您仔细想一想。\x02\x03",
            "有了这么一大笔钱\x01",
            "不但可以重建孤儿院，\x01",
            "大家也不需要长途跋涉去王都了。\x02\x03",
            "#043F而且也不用\x01",
            "扔下那块香草田……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        "#757F#3P………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#780F科洛丝说得没错。\x02\x03",
            "为了已故的约瑟夫，\x01",
            "更重要的是为了孩子们……\x02\x03",
            "您也应该抛下顾虑，\x01",
            "接受这笔钱吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x2C, 400)
    Sleep(500)

    ChrTalk(
        0x28,
        (
            "#754F#2P……啊啊……\x02\x03",
            "我……\x01",
            "我该怎么感谢大家呢……\x02\x03",
            "#758F谢谢……\x01",
            "真是太感谢了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F呜呜……太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F嗯，这样事情终于完满解决了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#775F#2P喂、喂……\x01",
            "去王都是什么意思啊？\x02\x03",
            "到底怎么回事嘛？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x2B, 400)

    ChrTalk(
        0x28,
        (
            "#758F#3P没事了……\x01",
            "已经用不着担心了……\x02\x03",
            "孩子们……\x01",
            "真是让你们受苦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#775F#2P我、我们并不觉得\x01",
            "受了什么苦啊……\x02\x03",
            "还、还有老师……\x01",
            "你为什么要哭嘛……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 400)

    ChrTalk(
        0x2A,
        "克拉姆真是笨蛋。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "当然是因为太过高兴，\x01",
            "高兴而哭了⊙\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特蕾莎院长和孩子们起程回玛诺利亚之后……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚还有其他学生\x01",
            "就开始了学园祭的收拾工作。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当所有工作都已经整理完毕的时候，\x01",
            "天色已经是黄昏了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_430B end

    def Function_31_625F(): pass

    label("Function_31_625F")

    Sleep(2000)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEFDB8, 0x0, 0xEE2, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEF5DE, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFEF688, 0x3E8, 0x1E64, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_31_625F end

    def Function_32_62B7(): pass

    label("Function_32_62B7")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEFDB8, 0x0, 0xEE2, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEF5DE, 0x0, 0x1130, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEF688, 0x3E8, 0x1E64, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF02E0, 0x3E8, 0x203A, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x105, 0)
    Return()

    # Function_32_62B7 end

    def Function_33_631E(): pass

    label("Function_33_631E")

    Sleep(500)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEFDB8, 0x0, 0xEE2, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEF5DE, 0x0, 0x1130, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEF688, 0x3E8, 0x1E64, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF02D6, 0x3E8, 0x2350, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_33_631E end

    def Function_34_638A(): pass

    label("Function_34_638A")

    Sleep(1500)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEFDB8, 0x0, 0xEE2, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEF5DE, 0x0, 0x1130, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEF688, 0x3E8, 0x1E64, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEFE3A, 0x3E8, 0x2558, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x102, 400)
    Return()

    # Function_34_638A end

    def Function_35_63F6(): pass

    label("Function_35_63F6")

    Sleep(1000)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEFDB8, 0x0, 0xEE2, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEF5DE, 0x0, 0x1130, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEF688, 0x3E8, 0x1E64, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF001A, 0x3E8, 0x23F0, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x102, 400)
    Return()

    # Function_35_63F6 end

    def Function_36_6462(): pass

    label("Function_36_6462")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFEFDE0, 0x3E8, 0x1932, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_36_6462 end

    def Function_37_6483(): pass

    label("Function_37_6483")

    Sleep(700)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF0268, 0x3E8, 0x19BE, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_37_6483 end

    SaveToFile()

Try(main)
