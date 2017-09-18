from ED6ScenarioHelper import *

def main():
    # 王立学院　礼堂

    CreateScenaFile(
        FileName            = 'T2533   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2533.x',
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
        '米克',                                 # 17
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
        Direction           = 180,
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
        X                   = -6300,
        Z                   = 0,
        Y                   = 300,
        Direction           = 90,
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
        X                   = 5900,
        Z                   = 0,
        Y                   = 3800,
        Direction           = 270,
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
        X                   = -4100,
        Z                   = 0,
        Y                   = -4200,
        Direction           = 0,
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
        X                   = -6300,
        Z                   = 0,
        Y                   = 6900,
        Direction           = 135,
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
        X                   = -4600,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 5900,
        Direction           = 270,
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
        X                   = -5700,
        Z                   = 0,
        Y                   = 4500,
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
        X                   = -2000,
        Z                   = 0,
        Y                   = 7200,
        Direction           = 0,
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
        X                   = -500,
        Z                   = 0,
        Y                   = 6700,
        Direction           = 0,
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
        X                   = -4000,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 225,
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
        X                   = -1900,
        Z                   = 0,
        Y                   = -1700,
        Direction           = 315,
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
        X                   = -1000,
        Z                   = 0,
        Y                   = 1200,
        Direction           = 270,
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
        X                   = -2800,
        Z                   = 0,
        Y                   = 900,
        Direction           = 270,
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
        X                   = -5400,
        Z                   = 0,
        Y                   = -2300,
        Direction           = 0,
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
        X                   = -1500,
        Z                   = 0,
        Y                   = 2700,
        Direction           = 270,
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
        Direction           = 180,
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
        X                   = 1900,
        Z                   = 0,
        Y                   = 200,
        Direction           = 90,
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
        X                   = 2000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 90,
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
        X                   = 4000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 270,
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
        X                   = 1780,
        Z                   = 0,
        Y                   = -1860,
        Direction           = 90,
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


    ScpFunction(
        "Function_0_552",          # 00, 0
        "Function_1_678",          # 01, 1
        "Function_2_6A3",          # 02, 2
        "Function_3_820",          # 03, 3
        "Function_4_8C1",          # 04, 4
        "Function_5_9C8",          # 05, 5
        "Function_6_A21",          # 06, 6
        "Function_7_ABC",          # 07, 7
        "Function_8_B47",          # 08, 8
        "Function_9_BC5",          # 09, 9
        "Function_10_C50",         # 0A, 10
        "Function_11_C7D",         # 0B, 11
        "Function_12_D08",         # 0C, 12
        "Function_13_D75",         # 0D, 13
        "Function_14_DE0",         # 0E, 14
        "Function_15_E3A",         # 0F, 15
        "Function_16_ECF",         # 10, 16
        "Function_17_FEB",         # 11, 17
        "Function_18_1073",        # 12, 18
        "Function_19_10C9",        # 13, 19
        "Function_20_1133",        # 14, 20
        "Function_21_117E",        # 15, 21
        "Function_22_11FB",        # 16, 22
        "Function_23_1236",        # 17, 23
        "Function_24_13FC",        # 18, 24
        "Function_25_1571",        # 19, 25
        "Function_26_1669",        # 1A, 26
        "Function_27_1714",        # 1B, 27
        "Function_28_17A1",        # 1C, 28
        "Function_29_20B9",        # 1D, 29
    )


    def Function_0_552(): pass

    label("Function_0_552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_55C")
    Jump("loc_652")

    label("loc_55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_600")
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
    SetChrPos(0x8, 320, 0, 4890, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1040, 0, 4970, 0)
    Jump("loc_652")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_60A")
    Jump("loc_652")

    label("loc_60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_614")
    Jump("loc_652")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_61E")
    Jump("loc_652")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_62D")
    ClearChrFlags(0x20, 0x80)
    Jump("loc_652")

    label("loc_62D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_637")
    Jump("loc_652")

    label("loc_637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_641")
    Jump("loc_652")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_64B")
    Jump("loc_652")

    label("loc_64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_652")

    label("loc_652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_660")
    OP_A3(0x3FA)
    Event(0, 28)

    label("loc_660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_677")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 29)

    label("loc_677")

    Return()

    # Function_0_552 end

    def Function_1_678(): pass

    label("Function_1_678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_699")
    OP_B1("t2533_y")
    Jump("loc_6A2")

    label("loc_699")

    OP_B1("t2533_n")

    label("loc_6A2")

    Return()

    # Function_1_678 end

    def Function_2_6A3(): pass

    label("Function_2_6A3")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C8")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_80A")

    label("loc_6C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E1")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_80A")

    label("loc_6E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_80A")

    label("loc_6FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_713")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_80A")

    label("loc_713")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_80A")

    label("loc_72C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_745")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_80A")

    label("loc_745")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_80A")

    label("loc_75E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_777")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_80A")

    label("loc_777")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_790")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_80A")

    label("loc_790")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_80A")

    label("loc_7A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C2")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_80A")

    label("loc_7C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DB")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_80A")

    label("loc_7DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_80A")

    label("loc_7F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_80A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_81F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_80A")

    label("loc_81F")

    Return()

    # Function_2_6A3 end

    def Function_3_820(): pass

    label("Function_3_820")

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

    # Function_3_820 end

    def Function_4_8C1(): pass

    label("Function_4_8C1")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97B")
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
    Jump("loc_9C4")

    label("loc_97B")


    ChrTalk(
        0xFE,
        (
            "这次结束后，\x01",
            "就和米丽亚一起去城里玩吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C4")

    TalkEnd(0xB)
    Return()

    # Function_4_8C1 end

    def Function_5_9C8(): pass

    label("Function_5_9C8")

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

    # Function_5_9C8 end

    def Function_6_A21(): pass

    label("Function_6_A21")

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

    # Function_6_A21 end

    def Function_7_ABC(): pass

    label("Function_7_ABC")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B11")
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
    Jump("loc_B43")

    label("loc_B11")


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

    label("loc_B43")

    TalkEnd(0xE)
    Return()

    # Function_7_ABC end

    def Function_8_B47(): pass

    label("Function_8_B47")

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

    # Function_8_B47 end

    def Function_9_BC5(): pass

    label("Function_9_BC5")

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

    # Function_9_BC5 end

    def Function_10_C50(): pass

    label("Function_10_C50")

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

    # Function_10_C50 end

    def Function_11_C7D(): pass

    label("Function_11_C7D")

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

    # Function_11_C7D end

    def Function_12_D08(): pass

    label("Function_12_D08")

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

    # Function_12_D08 end

    def Function_13_D75(): pass

    label("Function_13_D75")

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

    # Function_13_D75 end

    def Function_14_DE0(): pass

    label("Function_14_DE0")

    TalkBegin(0x15)

    ChrTalk(
        0xFE,
        "顺利地结束了啊……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x15)
    Return()

    # Function_14_DE0 end

    def Function_15_E3A(): pass

    label("Function_15_E3A")

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

    # Function_15_E3A end

    def Function_16_ECF(): pass

    label("Function_16_ECF")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCD")
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
    Jump("loc_FE7")

    label("loc_FCD")


    ChrTalk(
        0xFE,
        (
            "嘿嘿。\x01",
            "啊，好开心啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE7")

    TalkEnd(0x17)
    Return()

    # Function_16_ECF end

    def Function_17_FEB(): pass

    label("Function_17_FEB")

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

    # Function_17_FEB end

    def Function_18_1073(): pass

    label("Function_18_1073")

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

    # Function_18_1073 end

    def Function_19_10C9(): pass

    label("Function_19_10C9")

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

    # Function_19_10C9 end

    def Function_20_1133(): pass

    label("Function_20_1133")

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

    # Function_20_1133 end

    def Function_21_117E(): pass

    label("Function_21_117E")

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

    # Function_21_117E end

    def Function_22_11FB(): pass

    label("Function_22_11FB")

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

    # Function_22_11FB end

    def Function_23_1236(): pass

    label("Function_23_1236")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_137C")
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
    Jump("loc_13F8")

    label("loc_137C")


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

    ChrTalk(
        0x1E,
        "求你了，放过我吧……\x02",
    )

    CloseMessageWindow()

    label("loc_13F8")

    TalkEnd(0x1E)
    Return()

    # Function_23_1236 end

    def Function_24_13FC(): pass

    label("Function_24_13FC")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1542")
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
    Jump("loc_156D")

    label("loc_1542")


    ChrTalk(
        0xFE,
        "呵呵呵……\x02",
    )

    CloseMessageWindow()

    label("loc_156D")

    TalkEnd(0x1F)
    Return()

    # Function_24_13FC end

    def Function_25_1571(): pass

    label("Function_25_1571")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1608")
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
    Jump("loc_1665")

    label("loc_1608")


    ChrTalk(
        0xFE,
        (
            "#640F不赶快回到卢安\x01",
            "没有关系吗？\x02\x03",
            "如果想参加庆祝会的话十分欢迎哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1665")

    TalkEnd(0x8)
    Return()

    # Function_25_1571 end

    def Function_26_1669(): pass

    label("Function_26_1669")

    TalkBegin(0x9)

    ChrTalk(
        0xFE,
        (
            "#730F哦，\x01",
            "你们是不是舍不得庆祝会啊？\x02\x03",
            "今天全部由老师们请客呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_26_1669 end

    def Function_27_1714(): pass

    label("Function_27_1714")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_179D")

    ChrTalk(
        0xFE,
        "这里只能在下午使用时才开放。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我现在正照科林兹校长的吩咐\x01",
            "进行安全检查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179D")

    TalkEnd(0x20)
    Return()

    # Function_27_1714 end

    def Function_28_17A1(): pass

    label("Function_28_17A1")

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

    def lambda_1C3D():
        OP_6D(61500, 2310, 14620, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C3D)

    def lambda_1C55():
        OP_6B(850, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C55)

    def lambda_1C65():

        label("loc_1C65")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C65")

    QueueWorkItem2(0x101, 1, lambda_1C65)

    def lambda_1C76():

        label("loc_1C76")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C76")

    QueueWorkItem2(0x105, 1, lambda_1C76)

    def lambda_1C87():

        label("loc_1C87")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C87")

    QueueWorkItem2(0x8, 1, lambda_1C87)

    def lambda_1C98():

        label("loc_1C98")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1C98")

    QueueWorkItem2(0x9, 1, lambda_1C98)

    def lambda_1CA9():
        OP_8F(0xFE, 0xF582, 0x3E8, 0x3B10, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1CA9)
    Sleep(800)

    def lambda_1CC9():
        OP_8F(0xFE, 0xF71C, 0x3E8, 0x3DFE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CC9)
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
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2512   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_28_17A1 end

    def Function_29_20B9(): pass

    label("Function_29_20B9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，学园祭的前一天——\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
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
    OP_22(0x1F9, 0x0, 0x64)
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
            "#357F#1P然而，此刻驱使着身体的，\x01",
            "这近乎疯狂的热情究竟是什么？\x02\x03",
            "我似乎再次不可避免地\x01",
            "在此与你一决高下……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x105, 24)
    SetChrSubChip(0x105, 5)
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
            "空之女神将见证你我二人的灵魂!\x02\x03",
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
    OP_22(0xD5, 0x0, 0x64)
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
    OP_8C(0x105, 180, 400)
    Sleep(500)

    def lambda_28C7():
        OP_6D(58730, 2850, 2760, 5000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_28C7)

    def lambda_28DF():
        OP_6C(18000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_28DF)

    def lambda_28EF():
        OP_67(0, 2930, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_28EF)
    Sleep(1000)

    def lambda_290C():
        OP_8E(0xFE, 0xE7D6, 0x3E8, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_290C)
    Sleep(500)
    OP_8C(0x101, 225, 400)

    def lambda_2933():
        OP_8E(0xFE, 0xECA4, 0x3E8, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2933)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 180, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x105,
        (
            "#350F终于，明天就要正式演出了呢。\x02\x03",
            "不知道特蕾莎老师和孩子们\x01",
            "会不会喜欢呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        (
            "#340F#2P呵呵，你真的很关心\x01",
            "特蕾莎院长他们呢……\x02\x03",
            "#341F简直就像一家人似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#353F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#344F#2P啊，对不起。\x01",
            "我说错什么话了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 135, 400)

    ChrTalk(
        0x105,
        (
            "#355F不……\x01",
            "就像艾丝蒂尔所说的那样。\x02\x03",
            "是老师他们让我知道\x01",
            "家人才是世上最宝贵的东西……\x02\x03",
            "#350F因为我刚出生不久，\x01",
            "父母就在一次意外中去世了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#344F#2P哎……？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(60080, 1000, 14330, 0)
    OP_67(0, 5210, -10000, 0)
    OP_6B(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    OP_0D()

    ChrTalk(
        0x105,
        (
            "#357F#1P虽然被富裕的亲戚收养，\x01",
            "过着自由自在随心所欲的生活……\x02\x03",
            "但我却从来都不知道，\x01",
            "所谓的家人究竟是什么样的存在。\x02\x03",
            "#358F直到１０年前……\x01",
            "遇到老师他们的那一天开始。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#344F#2P１０年前……\x02\x03",
            "#342F难道是『百日战役』的时候？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#359F#1P是的，\x01",
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
        "#343F#2P是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#358F#1P战争结束后，我就被亲戚接回去了。\x01",
            "虽然只是短短的几个月……\x02\x03",
            "但是，特蕾莎老师和约瑟夫叔叔\x01",
            "对我的关心和照顾却是无微不至的……\x02\x03",
            "#357F那时候，我才第一次知道。\x02\x03",
            "拥有父亲和母亲，\x01",
            "是一种什么样的感觉。\x02\x03",
            "全家人能够生活在一起，\x01",
            "又是一种何等温暖的幸福……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#340F#2P科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#355F#1P对、对不起……\x02\x03",
            "情不自禁之下，\x01",
            "说了那么一大堆无聊的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#346F#2P不，没这回事呢。\x02\x03",
            "#341F明天的舞台剧……\x01",
            "我们一起加油，来场绝佳的演出吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#358F#1P……好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#346F#2P由我来说可能有点自卖自夸，\x01",
            "不过，我想绝对会很精彩的！\x02\x03",
            "不单是我们，\x01",
            "乔儿和汉斯也都很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#350F#1P呵呵，是啊。\x02\x03",
            "不过，功劳最大的\x01",
            "应该还是非约修亚莫属吧。\x02\x03",
            "想不到他的演技居然那么好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#340F#2P嗯、嗯……\x02\x03",
            "明明那么不情愿，\x01",
            "却还能把公主演得活灵活现呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#350F#1P不论是发音还是时机的把握，\x01",
            "真的丝毫也不比职业演员逊色呢。\x02\x03",
            "约修亚过去曾经演过戏吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#343F#2P啊，嗯……\x02\x03",
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
            "#353F#1P啊……\x02\x03",
            "对不起……\x01",
            "问了不该问的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#340F#2P啊哈哈，没什么啦。\x02\x03",
            "#346F嗯～约修亚确实就是\x01",
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
            "#355F#1P呵呵……\x02\x03",
            "#357F……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#340F#2P怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#359F#1P其实我们两个的角色\x01",
            "换过来扮演或许会比较好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#344F#2P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#353F#1P尤利乌斯和奥斯卡啊。\x02\x03",
            "我觉得奥斯卡还是\x01",
            "由艾丝蒂尔来演比较好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#340F#2P哎？为什么？\x02\x03",
            "不过我和\x01",
            "贵族出身的尤利乌斯\x01",
            "在身份上的确有点不大相称……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#353F#1P不，我不是这个意思。\x02\x03",
            "#355F……就是，舞台剧的最后……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#344F#2P哦、哦哦……\x01",
            "是公主对奥斯卡做那个……是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#355F#1P是、是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#348F#2P真是便宜了约修亚啊～\x02\x03",
            "难道说科洛丝\x01",
            "不想和约修亚演那个？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#354F#1P我、我不是这个意思！\x02\x03",
            "#359F不过，总觉得有点\x01",
            "对不起你们两个呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#348F#2P讨、讨厌啦～\x01",
            "别像乔儿那样说这种话嘛。\x02\x03",
            "#343F反正约修亚也只是把我当作\x01",
            "妹妹那样照顾而已……\x01",
            "  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#353F#1P是……这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#347F#2P他呀，总是站在老爸那边，\x01",
            "把我当作小孩子。\x02\x03",
            "真是气死我了……\x02\x03",
            "#346F总之呢，我觉得你完全\x01",
            "没必要为这种事和我介意！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#354F#1P是、是吗……\x02",
    )

    CloseMessageWindow()
    OP_4A(0x9, 255)
    SetChrPos(0x9, 65530, 0, 570, 0)
    SetChrPos(0x102, 64700, 0, 520, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x102, 0x80)

    ChrTalk(
        0x102,
        "#1P……啊，你们在这里啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_375C():

        label("loc_375C")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_375C")

    QueueWorkItem2(0x101, 1, lambda_375C)

    def lambda_376D():

        label("loc_376D")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_376D")

    QueueWorkItem2(0x105, 1, lambda_376D)

    def lambda_377E():
        OP_6D(62650, 1000, 10120, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_377E)

    def lambda_3796():
        OP_67(0, 4550, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3796)

    def lambda_37AE():
        OP_8E(0xFE, 0x10036, 0x0, 0x1C98, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_37AE)
    Sleep(500)

    def lambda_37CE():
        OP_8E(0xFE, 0xFCB2, 0x0, 0x191E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37CE)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 315, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 315, 400)
    OP_44(0x105, 0xFF)
    OP_44(0x101, 0xFF)

    ChrTalk(
        0x101,
        "#344F约、约修亚！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#354F汉斯也在……\x02",
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
            "#346F当然，就交给我们吧！\x01",
            "一定让你看到完美无缺的表演！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F是吗……\x01",
            "嗯，那我就拭目以待了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#350F说起来，\x01",
            "你们两个怎么会来这里？\x02\x03",
            "难道是在找我们吗……\x02",
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
            "#340F啊，是这样啊。\x02\x03",
            "#341F好，我也赞成！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#351F也请让我一同参加哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F说起来……\x01",
            "乔儿没和你们在一起吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#350F你说乔儿啊，\x01",
            "她刚才被校长叫走了……\x02\x03",
            "我去找她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#340F啊，我也去！\x02\x03",
            "约修亚你们\x01",
            "就先去食堂占位子吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F嗯，好的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        "#010F那我们就先去食堂吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        "#731F#2P好！老大。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F谁是你的老大……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 400)

    def lambda_3BC4():
        OP_8E(0xFE, 0xFCBC, 0x0, 0x208, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BC4)
    Sleep(200)
    OP_8C(0x9, 180, 400)
    OP_8E(0x9, 0xFFFA, 0x0, 0x23A, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x102, 0x80)
    Fade(1000)
    OP_6D(60080, 1000, 14330, 0)
    OP_67(0, 5210, -10000, 0)
    OP_6B(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#346F#2P呵呵，看来他们两个\x01",
            "也相处得不错啊。\x02\x03",
            "约修亚他有时候\x01",
            "会有拒人于千里之外的一面，\x01",
            "我本来还有点担心呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 135, 400)

    ChrTalk(
        0x105,
        "#358F#1P呵呵……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        "#344F#2P咦？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#351F#1P不不……\x01",
            "也没什么啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#340F#2P嗯～好了。\x01",
            "我们先去换衣服吧。\x02\x03",
            "穿成这样招摇过市的话，\x01",
            "实在是有点难为情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#358F#1P呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-34830, 1000, 10350, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    RemoveParty(0x1, 0xFF)
    SetChrPos(0x105, -36520, 1000, 8430, 90)
    SetChrPos(0x101, -35180, 1000, 8580, 270)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x101, 65535)
    Sleep(300)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#006F#2P……好了。\x02\x03",
            "那我们现在\x01",
            "就去接乔儿回来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F#3P好。\x01",
            "去校长室吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    ClearMapFlags(0x10000000)

    def lambda_3ED9():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3ED9)
    EventEnd(0x2)
    SetMapFlags(0x80)
    WaitChrThread(0x0, 0x1)
    ClearMapFlags(0x80)
    SetMapFlags(0x1)
    Return()

    # Function_29_20B9 end

    SaveToFile()

Try(main)
