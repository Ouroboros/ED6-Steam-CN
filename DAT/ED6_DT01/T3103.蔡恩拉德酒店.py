from ED6ScenarioHelper import *

def main():
    # 蔡恩拉德酒店

    CreateScenaFile(
        FileName            = 'T3103   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '索黛丽娅',                             # 9
        '阿利瑟',                               # 10
        '米优',                                 # 11
        '温丝',                                 # 12
        '加雷利',                               # 13
        '库诺',                                 # 14
        '呆呆',                                 # 15
        '莱恩',                                 # 16
        '科奇莫爷爷',                           # 17
        '莫妮卡',                               # 18
        '布鲁诺',                               # 19
        '伊格尔',                               # 20
        '拉德米拉',                             # 21
        '卡雷尔',                               # 22
        ' ',                                    # 23
        '蔡斯中央工房方向',                     # 24
        '托兰特平原道方向',                     # 25
        '利塔街道方向',                         # 26
    )

    DeclEntryPoint(
        Unknown_00              = 67000,
        Unknown_04              = 0,
        Unknown_08              = 53000,
        Unknown_0C              = 4,
        Unknown_0E              = 315,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH01070 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01050 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01200 ._CH',             # 06
        'ED6_DT07/CH01130 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01060 ._CH',             # 0A
        'ED6_DT07/CH01160 ._CH',             # 0B
        'ED6_DT07/CH01160 ._CH',             # 0C
        'ED6_DT07/CH01100 ._CH',             # 0D
        'ED6_DT07/CH02490 ._CH',             # 0E
        'ED6_DT07/CH01530 ._CH',             # 0F
        'ED6_DT07/CH01250 ._CH',             # 10
        'ED6_DT07/CH01690 ._CH',             # 11
        'ED6_DT07/CH02640 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH01070P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01050P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01200P._CP',             # 06
        'ED6_DT07/CH01130P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01060P._CP',             # 0A
        'ED6_DT07/CH01160P._CP',             # 0B
        'ED6_DT07/CH01160P._CP',             # 0C
        'ED6_DT07/CH01100P._CP',             # 0D
        'ED6_DT07/CH02490P._CP',             # 0E
        'ED6_DT07/CH01530P._CP',             # 0F
        'ED6_DT07/CH01250P._CP',             # 10
        'ED6_DT07/CH01690P._CP',             # 11
        'ED6_DT07/CH02640P._CP',             # 12
    )

    DeclNpc(
        X                   = 17600,
        Z                   = 3500,
        Y                   = 53760,
        Direction           = 283,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 18000,
        Z                   = 3500,
        Y                   = 52580,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 24380,
        Z                   = 3500,
        Y                   = 53780,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
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
        TalkScenaIndex      = 17,
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
        TalkScenaIndex      = 18,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 6,
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
        TalkScenaIndex      = 8,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        X                   = -17220,
        Z                   = 8000,
        Y                   = 59000,
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
        X                   = 81330,
        Z                   = 0,
        Y                   = 53110,
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
        X                   = 42990,
        Z                   = 0,
        Y                   = 104270,
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
        X                   = 39600,
        Y                   = -1000,
        Z                   = 90600,
        Range               = 46400,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x16828,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 69400,
        Y                   = -1000,
        Z                   = 56700,
        Range               = 71000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xB734,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 43700,
        Y                   = 0,
        Z                   = 63080,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 40200,
        Y                   = 0,
        Z                   = 66870,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 52230,
        Y                   = 0,
        Z                   = 54590,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 47450,
        Y                   = 450,
        Z                   = 51500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 47450,
        Y                   = 450,
        Z                   = 48500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 59950,
        Y                   = 0,
        Z                   = 25220,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 36000,
        Y                   = 0,
        Z                   = 54740,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 27020,
        Y                   = 0,
        Z                   = 63460,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 23130,
        Y                   = 0,
        Z                   = 82450,
        Range               = 1200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 64030,
        Y                   = 0,
        Z                   = 69550,
        Range               = 1200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )


    ScpFunction(
        "Function_0_502",          # 00, 0
        "Function_1_A43",          # 01, 1
        "Function_2_A87",          # 02, 2
        "Function_3_ABD",          # 03, 3
        "Function_4_C3A",          # 04, 4
        "Function_5_C5E",          # 05, 5
        "Function_6_C82",          # 06, 6
        "Function_7_DAA",          # 07, 7
        "Function_8_1147",         # 08, 8
        "Function_9_1257",         # 09, 9
        "Function_10_1A33",        # 0A, 10
        "Function_11_2187",        # 0B, 11
        "Function_12_26E8",        # 0C, 12
        "Function_13_2CD8",        # 0D, 13
        "Function_14_2D06",        # 0E, 14
        "Function_15_2F95",        # 0F, 15
        "Function_16_304F",        # 10, 16
        "Function_17_34E2",        # 11, 17
        "Function_18_36AD",        # 12, 18
        "Function_19_3EA6",        # 13, 19
        "Function_20_3FBC",        # 14, 20
        "Function_21_4108",        # 15, 21
        "Function_22_4254",        # 16, 22
        "Function_23_4258",        # 17, 23
        "Function_24_425C",        # 18, 24
        "Function_25_4260",        # 19, 25
        "Function_26_4264",        # 1A, 26
        "Function_27_4268",        # 1B, 27
        "Function_28_426C",        # 1C, 28
    )


    def Function_0_502(): pass

    label("Function_0_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_57A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 47810, 0, 37590, 185)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 38650, 0, 46790, 258)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_A42")

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_5E6")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 38910, 0, 69580, 177)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    Jump("loc_A42")

    label("loc_5E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_6B1")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16250, 3500, 71750, 39)
    OP_43(0x9, 0x0, 0x0, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 38910, 0, 69580, 177)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 38650, 0, 46790, 258)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 32970, 500, 85010, 175)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39900, 0, 67550, 4)
    Jump("loc_A42")

    label("loc_6B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_6BB")
    Jump("loc_A42")

    label("loc_6BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_6F1")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 22230, 0, 80520, 215)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_A42")

    label("loc_6F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_74C")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 20340, 0, 80730, 227)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 11290, 0, 64040, 258)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_A42")

    label("loc_74C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_7F7")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16780, 3500, 73480, 97)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17830, 3500, 72380, 8)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 8690, 0, 54740, 180)
    OP_43(0xC, 0x0, 0x0, 0x5)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 47290, 0, 54830, 275)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 45580, 0, 54810, 97)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_A42")

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_859")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16780, 3500, 73480, 97)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17830, 3500, 72380, 8)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    Jump("loc_A42")

    label("loc_859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_929")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16780, 3500, 73480, 97)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17830, 3500, 72380, 8)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 41900, 0, 61970, 17)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 38650, 0, 46790, 258)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 46850, 0, 87800, 238)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 9770, 0, 59280, 277)
    Jump("loc_A42")

    label("loc_929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_9B7")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 8690, 0, 54740, 306)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 47810, 0, 37590, 185)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 38650, 0, 46790, 258)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_A42")

    label("loc_9B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A42")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 8690, 0, 54740, 306)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 47810, 0, 37590, 185)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 38650, 0, 46790, 258)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)

    label("loc_A42")

    Return()

    # Function_0_502 end

    def Function_1_A43(): pass

    label("Function_1_A43")

    OP_16(0x2, 0xFA0, 0xFFFE94B8, 0xFFFEF278, 0x30051)
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    SoundDistance(0xA0, 0x1CC, 0xADC, 0xE63C, 0x2710, 0x9C40, 0x64, 0x0)
    OP_43(0x16, 0x0, 0x0, 0x2)
    Return()

    # Function_1_A43 end

    def Function_2_A87(): pass

    label("Function_2_A87")

    OP_72(0x10, 0x20)
    OP_72(0xE, 0x20)

    label("loc_A91")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ABC")
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    OP_6F(0xE, 0)
    OP_70(0xE, 0x28)
    OP_73(0x10)
    Jump("loc_A91")

    label("loc_ABC")

    Return()

    # Function_2_A87 end

    def Function_3_ABD(): pass

    label("Function_3_ABD")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE2")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_C24")

    label("loc_AE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFB")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_C24")

    label("loc_AFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B14")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_C24")

    label("loc_B14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_C24")

    label("loc_B2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B46")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_C24")

    label("loc_B46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_C24")

    label("loc_B5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B78")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_C24")

    label("loc_B78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B91")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_C24")

    label("loc_B91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_C24")

    label("loc_BAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_C24")

    label("loc_BC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_C24")

    label("loc_BDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF5")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_C24")

    label("loc_BF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_C24")

    label("loc_C0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C24")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_C24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C39")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_C24")

    label("loc_C39")

    Return()

    # Function_3_ABD end

    def Function_4_C3A(): pass

    label("Function_4_C3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C5D")
    OP_8D(0xFE, 17510, 71160, 14830, 73220, 3000)
    Jump("Function_4_C3A")

    label("loc_C5D")

    Return()

    # Function_4_C3A end

    def Function_5_C5E(): pass

    label("Function_5_C5E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C81")
    OP_8D(0xFE, 11460, 51180, 8590, 67130, 3000)
    Jump("Function_5_C5E")

    label("loc_C81")

    Return()

    # Function_5_C5E end

    def Function_6_C82(): pass

    label("Function_6_C82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_DA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_D06")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "兰达那家伙也在很拼命地工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家伙，\x01",
            "从什么时候开始在酒馆工作了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA6")

    label("loc_D06")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "怎么了，\x01",
            "街上的钟变慢了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "原来如此。\x01",
            "看来导力停止过的事情\x01",
            "是真的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好，我明白了。\x01",
            "等一下去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA6")

    TalkEnd(0xFE)
    Return()

    # Function_6_C82 end

    def Function_7_DAA(): pass

    label("Function_7_DAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1143")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C2")
    OP_A2(0x583)

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哟，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……？\x02\x03",
            "#010F啊，我还以为是谁呢……\x01",
            "真的是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯？是谁啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵，就是在洛连特\x01",
            "寻找齿轮的那个孩子啊。\x02\x03",
            "我们之前不是\x01",
            "接受过他的委托去找那碎片吗。\x02\x03",
            "你要回卡尔瓦德共和国去了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "不，在那之前要先去中央工房。\x01",
            "因为在格兰赛尔卖了些东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "老妈说用那些米拉\x01",
            "买些导力器回去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，反正老妈也开始知道\x01",
            "什么东西才是有价值的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F怎么样都好啦，\x01",
            "你还是老样子，那么自大傲慢呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "是吗？我觉得自己 \x01",
            "只不过是说了理所当然的话而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尽管如此……\x01",
            "这种自动导力梯真是太棒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "看多少次都不会厌烦啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1143")

    label("loc_10C2")


    ChrTalk(
        0xFE,
        "这种自动导力梯，真是太棒了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "走着上下楼梯\x01",
            "的确有点麻烦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "所以，就让楼梯动起来吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1143")

    TalkEnd(0xFE)
    Return()

    # Function_7_DAA end

    def Function_8_1147(): pass

    label("Function_8_1147")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1253")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_11A9")

    ChrTalk(
        0xFE,
        (
            "哎呀……？\x01",
            "说起来卡雷尔在哪儿呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个笨蛋儿子，\x01",
            "又在什么地方闲逛吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1253")

    label("loc_11A9")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "唉，真是的。\x01",
            "好不容易来到蔡斯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来的行程是\x01",
            "要到一个叫中央工房的地方\x01",
            "去看看那些导力制品……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过在那之前，我还是想稍微落一下脚。\x01",
            "找个合适的地方歇歇吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1253")

    TalkEnd(0xFE)
    Return()

    # Function_8_1147 end

    def Function_9_1257(): pass

    label("Function_9_1257")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_13DF")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_131D")

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "之后是回收破碎的结晶回路……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉～～\x01",
            "怎么一大早就觉得没有干劲呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还是去礼拜堂\x01",
            "祈祷一下吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DC")

    label("loc_131D")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "唔，一盒８号的螺丝，\x01",
            "两套导力压的测定仪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，总觉得每周\x01",
            "都在干一成不变的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在仓库里检查零件\x01",
            "其实是很辛苦的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13DC")

    Jump("loc_1A2F")

    label("loc_13DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_149A")

    ChrTalk(
        0xFE,
        (
            "总是很难找到\x01",
            "要找的箱子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然跟耶鲁克说了让他把这里整理一下，\x01",
            "不过他肯定会拖到下次再做的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2F")

    label("loc_149A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_152B")

    ChrTalk(
        0xFE,
        (
            "好吧，从今早开始\x01",
            "要以全新的精神面貌进行工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天一定要对\x01",
            "武器店的耶鲁克说清楚，\x01",
            "叫他把箱子里的零件都整理好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2F")

    label("loc_152B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_157D")

    ChrTalk(
        0xFE,
        "工房的人们呢！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "已经都去避难了吧！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A2F")

    label("loc_157D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_16B2")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_1620")

    ChrTalk(
        0xFE,
        (
            "本来是想去\x01",
            "和耶鲁克店长商量\x01",
            "把这里好好整理一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是我又拿不出\x01",
            "和他说话的勇气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是我也不能去向\x01",
            "斯坦因老板告密，\x01",
            "打小报告总是不好的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AF")

    label("loc_1620")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "该死，\x01",
            "又找不到想要的零件箱子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来是想去\x01",
            "和耶鲁克店长商量\x01",
            "把这里好好整理一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是我又拿不出\x01",
            "和他说话的勇气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AF")

    Jump("loc_1A2F")

    label("loc_16B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1831")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_1753")

    ChrTalk(
        0xFE,
        (
            "尽管如此……\x01",
            "这里的整理还真是乱七八糟呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，等找到需要的零件，\x01",
            "也不知道花了多长时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "进步总是伴随着牺牲的呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_182E")

    label("loc_1753")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "昨天真是大吃一惊呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "照明被切断的时候\x01",
            "大伙都惊呆了好一会儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "演算室的那些家伙\x01",
            "脸色比我还要苍白呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……唉，\x01",
            "进步总是伴随着牺牲的呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182E")

    Jump("loc_1A2F")

    label("loc_1831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_18BF")

    ChrTalk(
        0xFE,
        (
            "哦，提妲。\x01",
            "总是要你帮忙整理零件，谢谢啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "回去请和你爷爷说，\x01",
            "如果有零件用完了，\x01",
            "就尽管来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2F")

    label("loc_18BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A2F")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_1918")

    ChrTalk(
        0xFE,
        "嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "剩下的任务\x01",
            "就只剩回收破损的结晶回路啦……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2F")

    label("loc_1918")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "嗯，一盒８号的螺丝，\x01",
            "两套导力压的测定仪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，清点各个仓库的零件\x01",
            "这种工作也不轻松啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为在蔡斯，\x01",
            "到处都有大大小小的研究所啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里有博士的孙女儿\x01",
            "来帮忙进行整理，\x01",
            "工作起来还是很容易的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A2F")

    TalkEnd(0xFE)
    Return()

    # Function_9_1257 end

    def Function_10_1A33(): pass

    label("Function_10_1A33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1A9E")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "今天时钟走得也很准呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不确认一下这个，\x01",
            "我的一天就无法开始呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2183")

    label("loc_1A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1B48")

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "时钟终于走准了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要这个钟还在工作，\x01",
            "我们这一代人就必须努力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不然的话，\x01",
            "就没有别人\x01",
            "会照顾这个时钟了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2183")

    label("loc_1B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1D5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1B92")

    ChrTalk(
        0x13,
        (
            "那么，\x01",
            "这就开始校正时间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D5A")

    label("loc_1B92")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "抱歉，在你正忙的时候麻烦你。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "哪里，\x01",
            "其实我也没什么忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "反正我也就是个\x01",
            "落后于时代的技师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你在说什么呀。\x01",
            "你要知道自己是参与了\x01",
            "『埃尔赛尤号』建造的技术人员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明参与了\x01",
            "世上最新的高速飞艇的建造工作，\x01",
            "却还常说跟不上时代什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "哈哈，多谢夸奖了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "本来想在建造『埃尔赛尤号』的工作中\x01",
            "给拉赛尔帮点忙的，\x01",
            "果然还是太勉强了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "唉，不能不服老啊。\x01",
            "还是尽全力发挥余热吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5A")

    Jump("loc_2183")

    label("loc_1D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1D92")

    ChrTalk(
        0xFE,
        "啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那些烟是什么？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2183")

    label("loc_1D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1EC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1E27")

    ChrTalk(
        0xFE,
        (
            "哎呀，像我和兰达这样年纪的人\x01",
            "已经很害怕摆弄机械了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有困难的时候\x01",
            "也只有依靠年轻人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC5")

    label("loc_1E27")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "喂喂，伊格尔。\x01",
            "还是那么有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一会儿帮我瞧瞧街上的钟表吧。\x01",
            "因为昨天的那件事，今天似乎有点慢了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC5")

    Jump("loc_2183")

    label("loc_1EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1F61")

    ChrTalk(
        0xFE,
        (
            "果然是因为昨晚\x01",
            "导力停止的原因呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之现在需要调整时间，\x01",
            "待会儿去叫伊格尔那家伙来修理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FCA")

    label("loc_1F61")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "喔，钟慢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然是因为昨晚\x01",
            "导力停止的原因呀……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCA")

    Jump("loc_2183")

    label("loc_1FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2183")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_207F")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "导力器是从钟表技术中发展起来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近又把导力作为动力源\x01",
            "制作出一些导力钟表。\x01",
            "『技术』这东西还真是有趣啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2183")

    label("loc_207F")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "呼，每次看到都让人感到怀念。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个啊，是以前我和拉赛尔他们\x01",
            "一起制造的导力钟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "它是用导力器驱动的。\x01",
            "只要导力不停止，就会永远转动下去哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个钟是蔡斯还是钟表之城时\x01",
            "为数不多的纪念品之一了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2183")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A33 end

    def Function_11_2187(): pass

    label("Function_11_2187")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2299")

    ChrTalk(
        0xFE,
        (
            "呵呵，教你们一个\x01",
            "买东西不用犹豫的好办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不知道想买哪个，\x01",
            "就选最右边的那个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样的话， \x01",
            "就算不知道东西是好是坏，\x01",
            "也可以很顺利地把东西买回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E4")

    label("loc_2299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_23B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2324")

    ChrTalk(
        0xFE,
        (
            "话又说回来，\x01",
            "商品的标示最好能再清楚些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不写上一大堆参数的话，\x01",
            "会让消费者很为难的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23B6")

    label("loc_2324")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "今天我\x01",
            "是来买罐头的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯！比买面包要简单哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为标签上写了\x01",
            "里面装了些什么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B6")

    Jump("loc_26E4")

    label("loc_23B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_241A")

    ChrTalk(
        0xFE,
        (
            "呼～太好了。\x01",
            "看来终于安静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "我又可以专心去买东西了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E4")

    label("loc_241A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2499")

    ChrTalk(
        0xFE,
        (
            "杂货铺的老板\x01",
            "不知道跑到什么地方去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是不是去看\x01",
            "工房那边的骚乱了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E4")

    label("loc_2499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_256B")

    ChrTalk(
        0xFE,
        (
            "我爸爸是导力技师，\x01",
            "平时我习惯去买机器零件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "机器零件都附有说明书的，\x01",
            "选起来也非常简单轻松……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "为什么偏偏就面包没有说明书呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E9")

    label("loc_256B")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "面包啊面包……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊，\x01",
            "到底哪一个才是好面包呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "至少也要附张说明书\x01",
            "让我看看才能判断啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E9")

    Jump("loc_26E4")

    label("loc_25EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_266B")

    ChrTalk(
        0xFE,
        (
            "我还是头一次\x01",
            "自己来买吃的东西呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可所有面包看起来都一样。\x01",
            "它们到底有什么不同呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E4")

    label("loc_266B")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "啊，怎么办呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天爸爸\x01",
            "让我自己来买面包……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可所有面包看起来都一样。\x01",
            "它们到底有什么不同呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E4")

    TalkEnd(0xFE)
    Return()

    # Function_11_2187 end

    def Function_12_26E8(): pass

    label("Function_12_26E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_27EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_276E")

    ChrTalk(
        0xFE,
        (
            "我自己很累就不用说了，\x01",
            "做护卫的游击士也很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，这也是我们的工作，\x01",
            "没办法啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27EB")

    label("loc_276E")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "呼，今天下午又要去\x01",
            "沃尔费堡垒那里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "共和国的那些家伙真是的，\x01",
            "要给他们出口多少导力器\x01",
            "他们才会满意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27EB")

    Jump("loc_2CD4")

    label("loc_27EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_28EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_286A")

    ChrTalk(
        0xFE,
        "呼，没办法啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然现在时间还早，\x01",
            "不过还是赶快去委托\x01",
            "游击士协会承担护卫工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EB")

    label("loc_286A")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "刚想好不容易回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "马上又要去\x01",
            "沃尔费堡垒那里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "连发牢骚的空闲也没有啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28EB")

    Jump("loc_2CD4")

    label("loc_28EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2A8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_29DC")

    ChrTalk(
        0xFE,
        "唉，这些家伙都是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "光在这里聊昨天的事，\x01",
            "也不动手做点事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就我一个人需要\x01",
            "马上去沃尔费堡垒送货。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……哎，\x01",
            "能干的男人就是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8C")

    label("loc_29DC")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "好，货物都装好了，\x01",
            "再过一阵就要出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最后再对货物\x01",
            "进行一次检查吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……呀，对了。\x01",
            "还要连络一下\x01",
            "护卫的游击士才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A8C")

    Jump("loc_2CD4")

    label("loc_2A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2B26")

    ChrTalk(
        0xFE,
        (
            "虽然想让搬运车进行一次检查，\x01",
            "可这里的维修员也很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就像他们的名字一样，\x01",
            "一直在这里那里的到处跑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC9")

    label("loc_2B26")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "这辆搬运车也要尽快\x01",
            "让修理员检查一下才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "车子可不能在魔兽\x01",
            "出没的地方抛锚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC9")

    Jump("loc_2CD4")

    label("loc_2BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2CD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2C47")

    ChrTalk(
        0xFE,
        (
            "其实要是能用飞艇\x01",
            "来运送出口货物就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，直航共和国的运输艇\x01",
            "只会从王都出发。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD4")

    label("loc_2C47")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "差不多该按计划\x01",
            "去确认货物了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "把预定的货物装好，\x01",
            "用这部搬运车把这些\x01",
            "向共和国出口的货物运往沃尔费堡垒。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD4")

    TalkEnd(0xFE)
    Return()

    # Function_12_26E8 end

    def Function_13_2CD8(): pass

    label("Function_13_2CD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2D02")

    ChrTalk(
        0xFE,
        "怎么了？那股烟……\x02",
    )

    CloseMessageWindow()

    label("loc_2D02")

    TalkEnd(0xFE)
    Return()

    # Function_13_2CD8 end

    def Function_14_2D06(): pass

    label("Function_14_2D06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2DDE")

    ChrTalk(
        0xFE,
        (
            "袭击中央工房的\x01",
            "好像是亲卫队的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家的温丝\x01",
            "说看见了那些是\x01",
            "穿着蓝色军装的军人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说这话很难让人相信，\x01",
            "但那孩子从不说谎啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F91")

    label("loc_2DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2E06")

    ChrTalk(
        0xFE,
        "不，不是火灾吧！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F91")

    label("loc_2E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2EC0")

    ChrTalk(
        0xFE,
        (
            "嗯，确实像孩子说的那样，\x01",
            "花坛里面已经放不下更多的花了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "分一点花\x01",
            "给对面的索黛丽娅吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F91")

    label("loc_2EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F31")

    ChrTalk(
        0xFE,
        (
            "我说，温丝。\x01",
            "这样搭配怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不觉得花色间的平衡感\x01",
            "很不错吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F91")

    label("loc_2F31")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "听我家的老公说，\x01",
            "昨天的现象\x01",
            "是因为导力停止所造成的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真的会有这样的事吗？\x02",
    )

    CloseMessageWindow()

    label("loc_2F91")

    TalkEnd(0xFE)
    Return()

    # Function_14_2D06 end

    def Function_15_2F95(): pass

    label("Function_15_2F95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_304B")

    ChrTalk(
        0xFE,
        (
            "总觉得妈妈\x01",
            "似乎是弄错了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我很想做一名\x01",
            "中央工房的接待小姐呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "海泽尔也年纪也不小了，\x01",
            "要我跟她比肯定不在话下！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304B")

    TalkEnd(0xFE)
    Return()

    # Function_15_2F95 end

    def Function_16_304F(): pass

    label("Function_16_304F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_31C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_30F0")

    ChrTalk(
        0xFE,
        (
            "这样说来，\x01",
            "中央工房的防范体制\x01",
            "会因为这件事而被重新评估吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "要是工房那种自由的风气被限制了，\x01",
            "总觉得有点可惜呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C6")

    label("loc_30F0")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "有一群穿着蓝色制服的军人\x01",
            "刚刚从这里跑过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "恰好在这个时候出现，\x01",
            "我想那些人和中央工房\x01",
            "被袭的事件脱不了干系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可惜……没有带着导力相机，\x01",
            "真是有点不甘心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C6")

    Jump("loc_34DE")

    label("loc_31C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_324B")

    ChrTalk(
        0xFE,
        (
            "怎么回事？\x01",
            "看起来不像是火灾的浓烟……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那些气体是\x01",
            "从什么实验装置排出的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DE")

    label("loc_324B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_33F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3343")

    ChrTalk(
        0xFE,
        (
            "有机会的话，\x01",
            "我很想去资料室查阅一下\x01",
            "关于那个现象的资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，在那之前，\x01",
            "必须让康丝坦茨\x01",
            "整理一下资料室才行啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比起调查原因，\x01",
            "整理资料室所花费的工夫要多得多吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F3")

    label("loc_3343")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "导力停止现象……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这方面的资料\x01",
            "我也从来没看见过啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说实验就是导力停止的原因，\x01",
            "不过到底做了什么样的实验\x01",
            "会导致那种事情发生呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F3")

    Jump("loc_34DE")

    label("loc_33F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_344A")

    ChrTalk(
        0xFE,
        "我说，妈妈。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个花坛\x01",
            "哪里变得不一样了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DE")

    label("loc_344A")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "导力这东西\x01",
            "竟然会自己停下来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前读过的初等导力理论\x01",
            "都没有记载过这种现象呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来得要阅读一下\x01",
            "更详细的专业书籍才行呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34DE")

    TalkEnd(0xFE)
    Return()

    # Function_16_304F end

    def Function_17_34E2(): pass

    label("Function_17_34E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3622")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_358D")

    ChrTalk(
        0xFE,
        (
            "那里似乎是个\x01",
            "非常富有东方风情的温泉胜地啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "实际上我对东方的文化\x01",
            "抱有相当浓烈的兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "真是让人相当期待呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_361F")

    label("loc_358D")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "我听说\x01",
            "这附近好像有温泉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既然来到这城市了，\x01",
            "有机会一定要去那里看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_361F")

    Jump("loc_36A9")

    label("loc_3622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3671")

    ChrTalk(
        0xFE,
        "嗯，可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是不习惯的话，\x01",
            "还是很难掌握乘上去的时机。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A9")

    label("loc_3671")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "哦哦，好厉害呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "和传闻一样，楼梯会动呀。\x02",
    )

    CloseMessageWindow()

    label("loc_36A9")

    TalkEnd(0xFE)
    Return()

    # Function_17_34E2 end

    def Function_18_36AD(): pass

    label("Function_18_36AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_382B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3763")

    ChrTalk(
        0xFE,
        (
            "好的，今天就从罐子的摆放开始\x01",
            "好好整理一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯……将卖剩下的罐子\x01",
            "摆到前列的最右边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "将最想卖掉的东西\x01",
            "摆放在手容易够到的地方，\x01",
            "这可是商品摆放技术里基本中的基本哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3828")

    label("loc_3763")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "我很想快点将\x01",
            "商品摆放的要领\x01",
            "教给我的弟弟呆呆……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "或许还是太早了点吧。\x01",
            "那家伙很快就会厌烦不干的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "看来暂时还是必须由我来干啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xFE, 0x10)

    label("loc_3828")

    Jump("loc_3EA2")

    label("loc_382B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_38A1")

    ChrTalk(
        0xFE,
        (
            "哎呀，呆呆，\x01",
            "你摆放得太靠边了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那样的话，\x01",
            "不就破坏了整体的平衡吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_392D")

    label("loc_38A1")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "嗯，小心点。\x01",
            "我觉得将右边的罐子移动到左边的话\x01",
            "一定更美观呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我说呆呆，\x01",
            "快点照我说的那样做啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_392D")

    Jump("loc_3EA2")

    label("loc_3930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3A38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_39BF")

    ChrTalk(
        0xFE,
        (
            "我觉得也差不多\x01",
            "该让弟弟来尝试一下工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "商品摆放包涵的学问多着呢，\x01",
            "我很想早点多教他点知识。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A35")

    label("loc_39BF")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "听好了，呆呆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要将客人动过的商品\x01",
            "整整齐齐地放回原位啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_3A35")

    Jump("loc_3EA2")

    label("loc_3A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3C2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3AB4")

    ChrTalk(
        0xFE,
        (
            "原来真正的夜晚\x01",
            "竟然那么黑暗啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我往窗外一看，\x01",
            "真是吓坏我了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C2B")

    label("loc_3AB4")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "啊，提妲。\x01",
            "欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了对了，\x01",
            "昨天怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "提妲家的导力\x01",
            "也都全部停止了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F哎……！？\x02\x03",
            "……啊，嗯、是啊！\x01",
            "停了停了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～也就是说\x01",
            "城里的导力都停了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "原来真正的夜晚竟然那么黑暗啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我往窗外一看，\x01",
            "真是吓坏我了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C2B")

    Jump("loc_3EA2")

    label("loc_3C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3DD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3C99")

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "果然还是不够美观啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次把左边的那个罐子\x01",
            "再往左边挪一点试试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DD6")

    label("loc_3C99")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "唔……为什么\x01",
            "整体的协调感还是这么差呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……嗯？\x01",
            "哎，是提妲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你今天也要\x01",
            "去给爷爷帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F嗯，是啊。\x02\x03",
            "库诺也在店里帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是啊，\x01",
            "我负责摆放商品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "接下来该摆放水果了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "回头见，提妲。\x01",
            "下次主日学校见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F嗯。\x01",
            "加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DD6")

    Jump("loc_3EA2")

    label("loc_3DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3EA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3E40")

    ChrTalk(
        0xFE,
        "唔，不好看……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "把右边的罐子\x01",
            "重新垒一遍试试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EA2")

    label("loc_3E40")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "为什么整体的协调感还是这么差呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "把这个左边的罐子\x01",
            "再往左边挪一点试试。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EA2")

    TalkEnd(0xFE)
    Return()

    # Function_18_36AD end

    def Function_19_3EA6(): pass

    label("Function_19_3EA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3F07")

    ChrTalk(
        0xFE,
        "哎～我已经烦了啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哥哥真是的～\x01",
            "没办法～啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB8")

    label("loc_3F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3FB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3F80")
    OP_8C(0xFE, 90, 400)

    ChrTalk(
        0xFE,
        (
            "导力引擎，开动！\x01",
            "将罐子抓住！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………好的！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FB8")

    label("loc_3F80")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "了解，库诺博士。\x02",
    )

    CloseMessageWindow()

    label("loc_3FB8")

    TalkEnd(0xFE)
    Return()

    # Function_19_3EA6 end

    def Function_20_3FBC(): pass

    label("Function_20_3FBC")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF2")

    ChrTalk(
        0x101,
        "#002F（啊，这边是城外……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_40EC")

    label("loc_3FF2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4045")

    ChrTalk(
        0x102,
        (
            "#012F（这里是城的出口啊……\x01",
            "　现在没有必要出城去吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EC")

    label("loc_4045")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_407A")

    ChrTalk(
        0x107,
        "#062F（啊，这边是出口……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_40EC")

    label("loc_407A")


    ChrTalk(
        0x108,
        (
            "#070F（呼，晚上的街道吗。）\x02\x03",
            "（虽然是个不错的修行场所，\x01",
            "　不过下次有机会再说吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40EC")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_20_3FBC end

    def Function_21_4108(): pass

    label("Function_21_4108")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_413E")

    ChrTalk(
        0x101,
        "#002F（啊，这边是城外……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4238")

    label("loc_413E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4191")

    ChrTalk(
        0x102,
        (
            "#012F（这里是城的出口啊……\x01",
            "　现在没有必要出城去吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4238")

    label("loc_4191")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C6")

    ChrTalk(
        0x107,
        "#062F（啊，这边是出口……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4238")

    label("loc_41C6")


    ChrTalk(
        0x108,
        (
            "#070F（呼，晚上的街道吗。）\x02\x03",
            "（虽然是个不错的修行场所，\x01",
            "　不过下次有机会再说吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4238")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_21_4108 end

    def Function_22_4254(): pass

    label("Function_22_4254")

    SetPlaceName(0x7D) # 蔡恩拉德酒店
    Return()

    # Function_22_4254 end

    def Function_23_4258(): pass

    label("Function_23_4258")

    SetPlaceName(0x7F) # 蔡恩拉德酒店
    Return()

    # Function_23_4258 end

    def Function_24_425C(): pass

    label("Function_24_425C")

    SetPlaceName(0x82) # 蔡恩拉德酒店
    Return()

    # Function_24_425C end

    def Function_25_4260(): pass

    label("Function_25_4260")

    SetPlaceName(0x7C) # 蔡恩拉德酒店
    Return()

    # Function_25_4260 end

    def Function_26_4264(): pass

    label("Function_26_4264")

    SetPlaceName(0x7A) # 蔡恩拉德酒店
    Return()

    # Function_26_4264 end

    def Function_27_4268(): pass

    label("Function_27_4268")

    SetPlaceName(0x7B) # 蔡恩拉德酒店
    Return()

    # Function_27_4268 end

    def Function_28_426C(): pass

    label("Function_28_426C")

    SetPlaceName(0x80) # 蔡恩拉德酒店
    Return()

    # Function_28_426C end

    SaveToFile()

Try(main)
