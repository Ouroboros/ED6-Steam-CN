from ED6ScenarioHelper import *

def main():
    # 蔡恩拉德酒店

    CreateScenaFile(
        FileName            = 'T3100   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3100.x',
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
        '蔡斯市·工房区',                       # 24
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
        Unknown_36              = 270,
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
        'ED6_DT07/CH01450 ._CH',             # 0C
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
        'ED6_DT07/CH01450P._CP',             # 0C
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
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 23890,
        Z                   = 3500,
        Y                   = 53440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 9,
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
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 69400,
        Y                   = -1000,
        Z                   = 56700,
        Range               = 71000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xB734,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 7780,
        Y                   = -1000,
        Z                   = 63930,
        Range               = 6420,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xEA1A,
        Unknown_18          = 0x0,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 6420,
        Y                   = -1000,
        Z                   = 58250,
        Range               = 7860,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xD5D4,
        Unknown_18          = 0x0,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 43700,
        Y                   = 0,
        Z                   = 63080,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 40200,
        Y                   = 0,
        Z                   = 66870,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 52230,
        Y                   = 0,
        Z                   = 54590,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 47450,
        Y                   = 450,
        Z                   = 51500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 47450,
        Y                   = 450,
        Z                   = 48500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 59950,
        Y                   = 0,
        Z                   = 25220,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 32,
    )

    DeclEvent(
        X                   = 36000,
        Y                   = 0,
        Z                   = 54740,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 33,
    )

    DeclEvent(
        X                   = 27020,
        Y                   = 0,
        Z                   = 63460,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 23130,
        Y                   = 0,
        Z                   = 82450,
        Range               = 1200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 35,
    )

    DeclEvent(
        X                   = 64030,
        Y                   = 0,
        Z                   = 69550,
        Range               = 1200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )


    DeclActor(
        TriggerX            = 33000,
        TriggerZ            = 500,
        TriggerY            = 85510,
        TriggerRange        = 800,
        ActorX              = 33000,
        ActorZ              = 1500,
        ActorY              = 85510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_566",          # 00, 0
        "Function_1_B57",          # 01, 1
        "Function_2_BD2",          # 02, 2
        "Function_3_C08",          # 03, 3
        "Function_4_D85",          # 04, 4
        "Function_5_DA9",          # 05, 5
        "Function_6_DCD",          # 06, 6
        "Function_7_E32",          # 07, 7
        "Function_8_1182",         # 08, 8
        "Function_9_1522",         # 09, 9
        "Function_10_1632",        # 0A, 10
        "Function_11_1E15",        # 0B, 11
        "Function_12_257C",        # 0C, 12
        "Function_13_2ADD",        # 0D, 13
        "Function_14_30CD",        # 0E, 14
        "Function_15_30FB",        # 0F, 15
        "Function_16_3391",        # 10, 16
        "Function_17_3444",        # 11, 17
        "Function_18_38DE",        # 12, 18
        "Function_19_3AA7",        # 13, 19
        "Function_20_43F0",        # 14, 20
        "Function_21_4504",        # 15, 21
        "Function_22_4FB2",        # 16, 22
        "Function_23_5CCC",        # 17, 23
        "Function_24_5CE8",        # 18, 24
        "Function_25_5D04",        # 19, 25
        "Function_26_5D8D",        # 1A, 26
        "Function_27_5F82",        # 1B, 27
        "Function_28_61C9",        # 1C, 28
        "Function_29_648B",        # 1D, 29
        "Function_30_6519",        # 1E, 30
        "Function_31_651D",        # 1F, 31
        "Function_32_6521",        # 20, 32
        "Function_33_6525",        # 21, 33
        "Function_34_6529",        # 22, 34
        "Function_35_652D",        # 23, 35
        "Function_36_6531",        # 24, 36
    )


    def Function_0_566(): pass

    label("Function_0_566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_574")
    OP_A3(0x3FA)
    Event(0, 25)

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_582")
    OP_A3(0x3FB)
    Event(0, 26)

    label("loc_582")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_58E"),
        (SWITCH_DEFAULT, "loc_5AD"),
    )


    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    OP_A2(0x52B)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 27)

    label("loc_5AA")

    Jump("loc_5AD")

    label("loc_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_625")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41020, 0, 53780, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 39400, 0, 46910, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_B56")

    label("loc_625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_691")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 38910, 0, 69580, 90)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    Jump("loc_B56")

    label("loc_691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_76B")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16250, 3500, 71750, 39)
    OP_43(0x9, 0x0, 0x0, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 45110, 0, 62220, 90)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 46310, 0, 62180, 0)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41020, 0, 53780, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 39400, 0, 46910, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 32970, 500, 85010, 175)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 38670, 0, 68820, 90)
    Jump("loc_B56")

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_775")
    Jump("loc_B56")

    label("loc_775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_7AB")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 22230, 0, 80520, 215)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_B56")

    label("loc_7AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_806")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 20340, 0, 80730, 227)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 14670, 0, 60890, 270)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_B56")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_8BB")
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
    SetChrPos(0x10, 45910, 0, 57120, 270)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 44430, 0, 57110, 90)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_B56")

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_95F")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16780, 3500, 73480, 97)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17830, 3500, 72380, 8)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 46850, 0, 87800, 238)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 9770, 0, 59280, 277)
    Jump("loc_B56")

    label("loc_95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_A2F")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16780, 3500, 73480, 97)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17830, 3500, 72380, 8)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 41900, 0, 61970, 17)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 39400, 0, 46910, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 46850, 0, 87800, 238)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 9770, 0, 59280, 277)
    Jump("loc_B56")

    label("loc_A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_AC4")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 10650, 0, 59050, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 35280, 0, 69150, 90)
    OP_43(0xD, 0x0, 0x0, 0x6)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41020, 0, 53780, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 39400, 0, 46910, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_B56")

    label("loc_AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B56")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 10650, 0, 59050, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 35280, 0, 69150, 90)
    OP_43(0xD, 0x0, 0x0, 0x6)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41020, 0, 53780, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 39400, 0, 46910, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)

    label("loc_B56")

    Return()

    # Function_0_566 end

    def Function_1_B57(): pass

    label("Function_1_B57")

    OP_16(0x2, 0xFA0, 0xFFFE94B8, 0xFFFEF278, 0x30051)
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_B81")
    Jump("loc_BAE")

    label("loc_B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_B90")
    OP_71(0x11, 0x4)
    Jump("loc_BAE")

    label("loc_B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B9F")
    OP_71(0x11, 0x4)
    Jump("loc_BAE")

    label("loc_B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_BAE")
    OP_71(0x11, 0x4)
    Jump("loc_BAE")

    label("loc_BAE")

    SoundDistance(0xA0, 0x1CC, 0xADC, 0xE63C, 0x2710, 0x7530, 0x64, 0x0)
    OP_43(0x16, 0x0, 0x0, 0x2)
    Return()

    # Function_1_B57 end

    def Function_2_BD2(): pass

    label("Function_2_BD2")

    OP_72(0x10, 0x20)
    OP_72(0xE, 0x20)

    label("loc_BDC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C07")
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    OP_6F(0xE, 0)
    OP_70(0xE, 0x28)
    OP_73(0x10)
    Jump("loc_BDC")

    label("loc_C07")

    Return()

    # Function_2_BD2 end

    def Function_3_C08(): pass

    label("Function_3_C08")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_D6F")

    label("loc_C2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C46")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_D6F")

    label("loc_C46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_D6F")

    label("loc_C5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C78")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_D6F")

    label("loc_C78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C91")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_D6F")

    label("loc_C91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAA")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_D6F")

    label("loc_CAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC3")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_D6F")

    label("loc_CC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDC")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_D6F")

    label("loc_CDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF5")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_D6F")

    label("loc_CF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_D6F")

    label("loc_D0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D27")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_D6F")

    label("loc_D27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D40")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_D6F")

    label("loc_D40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D59")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_D6F")

    label("loc_D59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_D6F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D84")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_D6F")

    label("loc_D84")

    Return()

    # Function_3_C08 end

    def Function_4_D85(): pass

    label("Function_4_D85")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DA8")
    OP_8D(0xFE, 17510, 71160, 14830, 73220, 3000)
    Jump("Function_4_D85")

    label("loc_DA8")

    Return()

    # Function_4_D85 end

    def Function_5_DA9(): pass

    label("Function_5_DA9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DCC")
    OP_8D(0xFE, 11460, 51180, 8590, 67130, 3000)
    Jump("Function_5_DA9")

    label("loc_DCC")

    Return()

    # Function_5_DA9 end

    def Function_6_DCD(): pass

    label("Function_6_DCD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E31")
    OP_8E(0xFE, 0x9808, 0x0, 0x10E1E, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_63(0xD)
    OP_8E(0xFE, 0x89D0, 0x0, 0x10E1E, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0xD)
    Jump("Function_6_DCD")

    label("loc_E31")

    Return()

    # Function_6_DCD end

    def Function_7_E32(): pass

    label("Function_7_E32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_105D")
    OP_4A(0x13, 255)
    OP_4A(0x10, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_E87")

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "这就开始校正时间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1052")

    label("loc_E87")

    OP_A2(0xB)
    OP_A2(0x8)

    ChrTalk(
        0x10,
        "抱歉，在你正忙的时候麻烦你。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哪里，\x01",
            "其实我也没什么忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正我也就是个\x01",
            "落后于时代的技师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "你在说什么呀。\x01",
            "你要知道自己是参与了\x01",
            "『埃尔赛尤号』建造的技术人员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "明明参与了\x01",
            "世上最新的高速飞艇的建造工作，\x01",
            "却还常说跟不上时代什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
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

    label("loc_1052")

    OP_4B(0x13, 255)
    OP_4B(0x10, 255)
    Jump("loc_117E")

    label("loc_105D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_117E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_10DE")

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
    Jump("loc_117E")

    label("loc_10DE")

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

    label("loc_117E")

    TalkEnd(0xFE)
    Return()

    # Function_7_E32 end

    def Function_8_1182(): pass

    label("Function_8_1182")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_151E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_149D")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

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
            "寻找结晶回路碎片的那个孩子啊。\x02\x03",
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
            "老妈说要用那些米拉\x01",
            "买些导力器回去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿，老妈也开始知道\x01",
            "什么东西才是有价值的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F怎么样都好啦。\x01",
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
    Jump("loc_151E")

    label("loc_149D")


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

    label("loc_151E")

    TalkEnd(0xFE)
    Return()

    # Function_8_1182 end

    def Function_9_1522(): pass

    label("Function_9_1522")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_162E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1584")

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
    Jump("loc_162E")

    label("loc_1584")

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

    label("loc_162E")

    TalkEnd(0xFE)
    Return()

    # Function_9_1522 end

    def Function_10_1632(): pass

    label("Function_10_1632")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_17BA")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_16F8")

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
    Jump("loc_17B7")

    label("loc_16F8")

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

    label("loc_17B7")

    Jump("loc_1E11")

    label("loc_17BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1875")

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
    Jump("loc_1E11")

    label("loc_1875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1906")

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
    Jump("loc_1E11")

    label("loc_1906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1958")

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
    Jump("loc_1E11")

    label("loc_1958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1A8D")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_19FB")

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
    Jump("loc_1A8A")

    label("loc_19FB")

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

    label("loc_1A8A")

    Jump("loc_1E11")

    label("loc_1A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C0C")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_1B2E")

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
    Jump("loc_1C09")

    label("loc_1B2E")

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

    label("loc_1C09")

    Jump("loc_1E11")

    label("loc_1C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1CA1")
    TurnDirection(0xFE, 0x107, 0)

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
    Jump("loc_1E11")

    label("loc_1CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1E11")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_1CFA")

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
    Jump("loc_1E11")

    label("loc_1CFA")

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

    label("loc_1E11")

    TalkEnd(0xFE)
    Return()

    # Function_10_1632 end

    def Function_11_1E15(): pass

    label("Function_11_1E15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1E80")

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
    Jump("loc_2578")

    label("loc_1E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1F2A")

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
    Jump("loc_2578")

    label("loc_1F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2152")
    OP_4A(0x13, 255)
    OP_4A(0x10, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1F7C")

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
    Jump("loc_2147")

    label("loc_1F7C")

    OP_A2(0xB)
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

    label("loc_2147")

    OP_4B(0x13, 255)
    OP_4B(0x10, 255)
    Jump("loc_2578")

    label("loc_2152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2187")

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
    Jump("loc_2578")

    label("loc_2187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_22BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_221C")

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
    Jump("loc_22BA")

    label("loc_221C")

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

    label("loc_22BA")

    Jump("loc_2578")

    label("loc_22BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2356")

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
    Jump("loc_23BF")

    label("loc_2356")

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

    label("loc_23BF")

    Jump("loc_2578")

    label("loc_23C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2578")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2474")

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
    Jump("loc_2578")

    label("loc_2474")

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

    label("loc_2578")

    TalkEnd(0xFE)
    Return()

    # Function_11_1E15 end

    def Function_12_257C(): pass

    label("Function_12_257C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_268E")

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
    Jump("loc_2AD9")

    label("loc_268E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_27AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2719")

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
    Jump("loc_27AB")

    label("loc_2719")

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

    label("loc_27AB")

    Jump("loc_2AD9")

    label("loc_27AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_280F")

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
    Jump("loc_2AD9")

    label("loc_280F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_288E")

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
    Jump("loc_2AD9")

    label("loc_288E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2960")

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
    Jump("loc_29DE")

    label("loc_2960")

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

    label("loc_29DE")

    Jump("loc_2AD9")

    label("loc_29E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2A60")

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
    Jump("loc_2AD9")

    label("loc_2A60")

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

    label("loc_2AD9")

    TalkEnd(0xFE)
    Return()

    # Function_12_257C end

    def Function_13_2ADD(): pass

    label("Function_13_2ADD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2BE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2B63")

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
    Jump("loc_2BE0")

    label("loc_2B63")

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

    label("loc_2BE0")

    Jump("loc_30C9")

    label("loc_2BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2CE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2C5F")

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
    Jump("loc_2CE0")

    label("loc_2C5F")

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

    label("loc_2CE0")

    Jump("loc_30C9")

    label("loc_2CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2E84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2DD1")

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
    Jump("loc_2E81")

    label("loc_2DD1")

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

    label("loc_2E81")

    Jump("loc_30C9")

    label("loc_2E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2FC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2F1B")

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
            "就像文字上写的那样，\x01",
            "一直在这里那里的到处跑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FBE")

    label("loc_2F1B")

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

    label("loc_2FBE")

    Jump("loc_30C9")

    label("loc_2FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_30C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_303C")

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
    Jump("loc_30C9")

    label("loc_303C")

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

    label("loc_30C9")

    TalkEnd(0xFE)
    Return()

    # Function_13_2ADD end

    def Function_14_30CD(): pass

    label("Function_14_30CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_30F7")

    ChrTalk(
        0xFE,
        "怎么了？那股烟……\x02",
    )

    CloseMessageWindow()

    label("loc_30F7")

    TalkEnd(0xFE)
    Return()

    # Function_14_30CD end

    def Function_15_30FB(): pass

    label("Function_15_30FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_31D3")

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
    Jump("loc_338D")

    label("loc_31D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_31FB")

    ChrTalk(
        0xFE,
        "不、不是火灾吧！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_338D")

    label("loc_31FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_32B5")

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
    Jump("loc_338D")

    label("loc_32B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_338D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_332D")
    TurnDirection(0x9, 0xB, 0)

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
    Jump("loc_338D")

    label("loc_332D")

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

    label("loc_338D")

    TalkEnd(0xFE)
    Return()

    # Function_15_30FB end

    def Function_16_3391(): pass

    label("Function_16_3391")

    TalkBegin(0xFE)

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
    TalkEnd(0xFE)
    Return()

    # Function_16_3391 end

    def Function_17_3444(): pass

    label("Function_17_3444")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_35BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_34E5")

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
    Jump("loc_35BB")

    label("loc_34E5")

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

    label("loc_35BB")

    Jump("loc_38DA")

    label("loc_35BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3640")

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
    Jump("loc_38DA")

    label("loc_3640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_37EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3738")

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
    Jump("loc_37E8")

    label("loc_3738")

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

    label("loc_37E8")

    Jump("loc_38DA")

    label("loc_37EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3846")
    TurnDirection(0xFE, 0x9, 0)

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
    Jump("loc_38DA")

    label("loc_3846")

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

    label("loc_38DA")

    TalkEnd(0xFE)
    Return()

    # Function_17_3444 end

    def Function_18_38DE(): pass

    label("Function_18_38DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3988")

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
    Jump("loc_3A19")

    label("loc_3988")

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

    label("loc_3A19")

    Jump("loc_3AA3")

    label("loc_3A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3A6B")

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
    Jump("loc_3AA3")

    label("loc_3A6B")

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

    label("loc_3AA3")

    TalkEnd(0xFE)
    Return()

    # Function_18_38DE end

    def Function_19_3AA7(): pass

    label("Function_19_3AA7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3C2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3B5D")

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
    Jump("loc_3C29")

    label("loc_3B5D")

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
    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)

    label("loc_3C29")

    Jump("loc_43EC")

    label("loc_3C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3D31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3CA2")

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
    Jump("loc_3D2E")

    label("loc_3CA2")

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

    label("loc_3D2E")

    Jump("loc_43EC")

    label("loc_3D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3E39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3DC0")

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
    Jump("loc_3E36")

    label("loc_3DC0")

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

    label("loc_3E36")

    Jump("loc_43EC")

    label("loc_3E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_4073")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3EB5")

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
    Jump("loc_4070")

    label("loc_3EB5")

    OP_A2(0x5)
    TurnDirection(0xD, 0x107, 400)

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
        "哎呀，昨天吓死人了。\x02",
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
    TurnDirection(0x107, 0xD, 400)
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x107,
        (
            "#061F啊，嗯……\x02\x03",
            "是、是呀，全都停了，\x01",
            "真是吓了一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "果然城里的导力全都停了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我往窗外一看，\x01",
            "城里漆黑一片，吓死我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没有了导力灯，\x01",
            "夜晚竟然那么黑暗啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F是、是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4070")

    Jump("loc_43EC")

    label("loc_4073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4323")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_40DE")

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
    Jump("loc_4320")

    label("loc_40DE")

    OP_A2(0x5)
    OP_63(0xD)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "我都已经很注重商品的摆放了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么整体的协调感\x01",
            "还是这么差呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x107, 400)

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
        "你今天也要去工房帮忙吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F嗯，是啊。\x02\x03",
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
            "因为爸爸他\x01",
            "对这方面很不在行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊，那些东西摆放得这么漂亮，\x01",
            "原来都是库诺你的功劳啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嘿嘿，还好啦。\x02",
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
            "#061F嗯，再见了。\x02\x03",
            "不过你要乖乖地\x01",
            "完成作业才行哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4320")

    Jump("loc_43EC")

    label("loc_4323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_43EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_438A")

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
    Jump("loc_43EC")

    label("loc_438A")

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

    label("loc_43EC")

    TalkEnd(0xFE)
    Return()

    # Function_19_3AA7 end

    def Function_20_43F0(): pass

    label("Function_20_43F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4451")

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
    Jump("loc_4500")

    label("loc_4451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4500")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_44C8")
    OP_8C(0xFE, 0, 400)

    ChrTalk(
        0xFE,
        (
            "导力引擎，开动！\x01",
            "将苹果抓住！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………好的！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4500")

    label("loc_44C8")

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

    label("loc_4500")

    TalkEnd(0xFE)
    Return()

    # Function_20_43F0 end

    def Function_21_4504(): pass

    label("Function_21_4504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_457B")
    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F首先我们要去飞艇坪去把票退掉。\x01",
            "　\x02\x03",
            "然后我们再出发。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 23)
    Jump("loc_4FB1")

    label("loc_457B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4793")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4669")
    OP_A2(0xE)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F这边是街道啊……\x02\x03",
            "#502F嘿嘿⊙\x01",
            "这次不用再走路了吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，\x01",
            "总觉得很不习惯呢。\x02\x03",
            "那么，去飞艇坪吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_478C")

    label("loc_4669")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46AF")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F艾丝蒂尔，去飞艇坪吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_478C")

    label("loc_46AF")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F这边是街道呢。\x02\x03",
            "虽然时间比较充裕，\x01",
            "不过还是不要跑得太远吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F嗯，确实……\x02\x03",
            "好不容易有次空中旅行，\x01",
            "绝对不能错过啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_478C")

    Call(0, 23)
    Jump("loc_4FB1")

    label("loc_4793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4963")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4886")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4836")
    OP_A2(0xE)

    ChrTalk(
        0x101,
        (
            "#000F啊，\x01",
            "总之现在要先回协会。\x02\x03",
            "在没有情报的情况下\x01",
            "是不能随便行动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x01",
            "赶快走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4883")

    label("loc_4836")


    ChrTalk(
        0x101,
        (
            "#000F总之，\x01",
            "现在要先回协会。\x02\x03",
            "在没有情报的情况下\x01",
            "是不能随便行动的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4883")

    Jump("loc_495C")

    label("loc_4886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4905")
    OP_A2(0xE)

    ChrTalk(
        0x102,
        (
            "#010F总之现在先回协会\x01",
            "听听雾香姐怎么说。\x02\x03",
            "说不定能发现什么有价值的线索呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_495C")

    label("loc_4905")


    ChrTalk(
        0x102,
        (
            "#010F总之现在先回协会\x01",
            "听听雾香姐怎么说。\x02\x03",
            "说不定能发现什么有价值的线索呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_495C")

    Call(0, 23)
    Jump("loc_4FB1")

    label("loc_4963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ACE")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A56")
    OP_A2(0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49E7")

    ChrTalk(
        0x106,
        (
            "#050F嘁……\x01",
            "现在再追也不会有线索的。\x02\x03",
            "总之先回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A53")

    label("loc_49E7")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(
        0x106,
        (
            "#050F喂，你们去哪儿。\x02\x03",
            "赶快回协会去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A53")

    Jump("loc_4AC7")

    label("loc_4A56")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A6C")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_4A73")

    label("loc_4A6C")

    TurnDirection(0x106, 0x0, 400)

    label("loc_4A73")


    ChrTalk(
        0x106,
        (
            "#050F往那边追也不会有线索的。\x01",
            "总之先回协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AC7")

    Call(0, 23)
    Jump("loc_4FB1")

    label("loc_4ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C00")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B3A")

    ChrTalk(
        0x101,
        (
            "#002F啊，这边是街道……\x01",
            "要快点赶到中央工房才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF9")

    label("loc_4B3A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B95")

    ChrTalk(
        0x102,
        (
            "#012F中央工房的样子看起来有点怪……\x01",
            "我们最好还是快点过去看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF9")

    label("loc_4B95")


    ChrTalk(
        0x107,
        (
            "#062F中央工房似乎发生了什么事……\x01",
            "快点过去看看情况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF9")

    Call(0, 23)
    Jump("loc_4FB1")

    label("loc_4C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D6E")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CDF")
    TurnDirection(0x102, 0x101, 400)
    OP_A2(0xE)

    ChrTalk(
        0x102,
        (
            "#010F博士要的东西还没有送过去呢。\x01",
            "　\x02\x03",
            "……委托的事情，\x01",
            "你有没有好好记下来啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#009F真、真讨厌～\x02\x03",
            "这不是清清楚楚地记下来了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D67")

    label("loc_4CDF")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F博士要的东西还没有送过去呢。\x01",
            "　\x02\x03",
            "总之现在要帮忙工作机械的改造。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D67")

    Call(0, 23)
    Jump("loc_4FB1")

    label("loc_4D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DFB")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D92")
    TurnDirection(0x107, 0x1, 400)
    Jump("loc_4D99")

    label("loc_4D92")

    TurnDirection(0x107, 0x0, 400)

    label("loc_4D99")


    ChrTalk(
        0x107,
        (
            "#060F那个，这边是街道呢。\x02\x03",
            "中央工房在城里的北边。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 23)
    Jump("loc_4FB1")

    label("loc_4DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E80")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E1F")
    TurnDirection(0x107, 0x1, 400)
    Jump("loc_4E26")

    label("loc_4E1F")

    TurnDirection(0x107, 0x0, 400)

    label("loc_4E26")


    ChrTalk(
        0x107,
        (
            "#060F啊，从这里出去\x01",
            "就是通往王都的街道了。\x02\x03",
            "我家是在城里的西南边呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 23)
    Jump("loc_4FB1")

    label("loc_4E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FB1")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F39")
    TurnDirection(0x102, 0x101, 400)
    OP_A2(0xE)

    ChrTalk(
        0x102,
        (
            "#010F在出城之前， \x01",
            "先到游击士协会打个招呼吧。\x02\x03",
            "有很多事情需要商量一下呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，那就这样吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FAD")

    label("loc_4F39")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F在出城之前， \x01",
            "先到游击士协会打个招呼吧。\x02\x03",
            "有很多事情需要商量一下呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FAD")

    Call(0, 23)

    label("loc_4FB1")

    Return()

    # Function_21_4504 end

    def Function_22_4FB2(): pass

    label("Function_22_4FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5029")
    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F首先我们要去飞艇坪去把票退掉。\x01",
            "　\x02\x03",
            "然后我们再出发。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    Jump("loc_5CCB")

    label("loc_5029")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_522E")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5123")
    OP_A2(0xE)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F这边是街道啊……\x02\x03",
            "#502F嘿嘿⊙\x01",
            "这次不用再走路了吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，\x01",
            "总觉得很不习惯呢。\x02\x03",
            "那么，去飞艇坪吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5227")

    label("loc_5123")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5162")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F艾丝蒂尔，去飞艇坪吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5227")

    label("loc_5162")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F这边是平原道哦。\x02\x03",
            "虽然时间比较充裕，\x01",
            "不过还是不要跑得太远吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F嗯，确实……\x02\x03",
            "好不容易有次空中旅行，\x01",
            "绝对不能错过啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5227")

    Call(0, 24)
    Jump("loc_5CCB")

    label("loc_522E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5474")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5300")
    OP_A2(0xE)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔，方向不对啊。\x02\x03",
            "去雷斯顿要塞的话，\x01",
            "要从城东门出去啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F呀？\x01",
            "是、是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F……真是的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5380")

    label("loc_5300")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F去雷斯顿要塞的话，\x01",
            "要从城东门出去才行啊。\x02\x03",
            "你刚才不是记下来了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5380")

    Jump("loc_546D")

    label("loc_5383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53FE")
    OP_A2(0xE)

    ChrTalk(
        0x102,
        (
            "#012F这边是托兰特平原道啊。\x02\x03",
            "去雷斯顿要塞的话，\x01",
            "要从城东门出去啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_546D")

    label("loc_53FE")


    ChrTalk(
        0x102,
        (
            "#012F这边是托兰特平原道啊……\x02\x03",
            "去雷斯顿要塞的话，\x01",
            "要从城东门出去啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_546D")

    Call(0, 24)
    Jump("loc_5CCB")

    label("loc_5474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5682")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_557F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5523")
    OP_A2(0xE)

    ChrTalk(
        0x101,
        (
            "#000F啊，\x01",
            "总之现在要先回协会。\x02\x03",
            "在没有情报的情况下\x01",
            "是不能随便行动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x01",
            "赶快走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_557C")

    label("loc_5523")


    ChrTalk(
        0x101,
        (
            "#000F总之，\x01",
            "现在要先回协会。\x02\x03",
            "在没有情报的情况下\x01",
            "是不能随便行动的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_557C")

    Jump("loc_567B")

    label("loc_557F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5611")
    OP_A2(0xE)

    ChrTalk(
        0x102,
        (
            "#010F总之现在先回协会\x01",
            "听听雾香姐怎么说。\x02\x03",
            "说不定能发现什么有价值的线索呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_567B")

    label("loc_5611")


    ChrTalk(
        0x102,
        (
            "#010F总之现在先回协会\x01",
            "听听雾香姐怎么说。\x02\x03",
            "说不定能发现什么有价值的线索呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_567B")

    Call(0, 24)
    Jump("loc_5CCB")

    label("loc_5682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57ED")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5775")
    OP_A2(0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5706")

    ChrTalk(
        0x106,
        (
            "#050F嘁……\x01",
            "现在再追也不会有线索的。\x02\x03",
            "总之先回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5772")

    label("loc_5706")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(
        0x106,
        (
            "#050F喂，你们去哪儿。\x02\x03",
            "赶快回协会去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5772")

    Jump("loc_57E6")

    label("loc_5775")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_578B")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_5792")

    label("loc_578B")

    TurnDirection(0x106, 0x0, 400)

    label("loc_5792")


    ChrTalk(
        0x106,
        (
            "#050F往那边追也不会有线索的。\x01",
            "总之先回协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57E6")

    Call(0, 24)
    Jump("loc_5CCB")

    label("loc_57ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_591F")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5859")

    ChrTalk(
        0x101,
        (
            "#002F啊，这边是街道……\x01",
            "要快点赶到中央工房才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5918")

    label("loc_5859")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58B4")

    ChrTalk(
        0x102,
        (
            "#012F中央工房的样子看起来有点怪……\x01",
            "我们最好还是快点过去看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5918")

    label("loc_58B4")


    ChrTalk(
        0x107,
        (
            "#062F中央工房似乎发生了什么事……\x01",
            "快点过去看看情况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5918")

    Call(0, 24)
    Jump("loc_5CCB")

    label("loc_591F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A8D")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59FE")
    TurnDirection(0x102, 0x101, 400)
    OP_A2(0xE)

    ChrTalk(
        0x102,
        (
            "#010F博士要的东西还没有送过去呢。\x01",
            "　\x02\x03",
            "……委托的事情，\x01",
            "你有没有好好记下来啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#009F真、真讨厌～\x02\x03",
            "这不是清清楚楚地记下来了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A86")

    label("loc_59FE")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F博士要的东西还没有送过去呢。\x01",
            "　\x02\x03",
            "总之现在要帮忙工作机械的改造。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A86")

    Call(0, 24)
    Jump("loc_5CCB")

    label("loc_5A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B1B")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AB1")
    TurnDirection(0x107, 0x1, 400)
    Jump("loc_5AB8")

    label("loc_5AB1")

    TurnDirection(0x107, 0x0, 400)

    label("loc_5AB8")


    ChrTalk(
        0x107,
        (
            "#060F啊，这边是平原道呢。\x02\x03",
            "中央工房在城里的北边。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    Jump("loc_5CCB")

    label("loc_5B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B9A")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B3F")
    TurnDirection(0x107, 0x1, 400)
    Jump("loc_5B46")

    label("loc_5B3F")

    TurnDirection(0x107, 0x0, 400)

    label("loc_5B46")


    ChrTalk(
        0x107,
        (
            "#060F啊，\x01",
            "从这里出去就是平原道了。\x02\x03",
            "我的家就在这西边。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    Jump("loc_5CCB")

    label("loc_5B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CCB")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C53")
    TurnDirection(0x102, 0x101, 400)
    OP_A2(0xE)

    ChrTalk(
        0x102,
        (
            "#010F在出城之前， \x01",
            "先到游击士协会打个招呼吧。\x02\x03",
            "有很多事情需要商量一下呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，那就这样吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CC7")

    label("loc_5C53")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F在出城之前， \x01",
            "先到游击士协会打个招呼吧。\x02\x03",
            "有很多事情需要商量一下呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CC7")

    Call(0, 24)

    label("loc_5CCB")

    Return()

    # Function_22_4FB2 end

    def Function_23_5CCC(): pass

    label("Function_23_5CCC")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_23_5CCC end

    def Function_24_5CE8(): pass

    label("Function_24_5CE8")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_24_5CE8 end

    def Function_25_5D04(): pass

    label("Function_25_5D04")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_67(0, 5600, -10000, 0)
    OP_6D(58400, 3900, 51600, 0)
    OP_6B(4700, 0)
    OP_6C(276000, 0)

    def lambda_5D45():
        OP_6D(57400, 3900, 23700, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D45)
    OP_6C(204000, 6000)

    def lambda_5D66():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D66)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T3133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_5D04 end

    def Function_26_5D8D(): pass

    label("Function_26_5D8D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(60080, 0, 26320, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 60090, 0, 27140, 180)
    SetChrPos(0x102, 60590, 0, 25950, 315)
    SetChrPos(0x107, 59500, 0, 26070, 0)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿～\x01",
            "美味的早饭已经享用完了……\x02\x03",
            "我们这就去中央工房吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F在此之前，\x01",
            "我们先回游击士协会一趟吧。\x02\x03",
            "为了慎重起见，\x01",
            "还是向雾香小姐报告昨天的事比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F啊，也对……\x02\x03",
            "提妲，\x01",
            "稍微绕个道好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F#2P好的，当然可以。\x02",
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
    EventEnd(0x0)
    Return()

    # Function_26_5D8D end

    def Function_27_5F82(): pass

    label("Function_27_5F82")

    EventBegin(0x0)
    OP_6D(66850, 0, 53050, 0)
    OP_6C(270000, 0)
    SetChrPos(0x101, 66140, 0, 53000, 270)
    SetChrPos(0x107, 66790, 0, 52290, 270)
    SetChrPos(0x102, 66830, 0, 53720, 270)
    SetChrPos(0x110, 67900, 0, 52960, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F咦……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#064F怎么了？\x01",
            "艾丝蒂尔姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F可能是我的心理作用吧，\x01",
            "总觉得好像有什么骚动似的……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 315, 400)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(
        0x102,
        (
            "#012F……不是心理作用，\x01",
            "我听到远处的确有嘈杂声。\x02\x03",
            "是中央工房的方向。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6134():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_6134)

    def lambda_6142():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6142)
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x107,
        "#065F咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        "#154F咦咦，怎么回事～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F不知道……\x01",
            "我们最好快点过去看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0xD)
    EventEnd(0x0)
    Return()

    # Function_27_5F82 end

    def Function_28_61C9(): pass

    label("Function_28_61C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_648A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6393")
    OP_A2(0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_629F")
    TurnDirection(0x102, 0x107, 400)

    ChrTalk(
        0x102,
        (
            "#010F提妲，等一下。\x02\x03",
            "能不能稍微绕个远路呢？\x01",
            "我们想去协会打个招呼。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x107,
        (
            "#060F啊，好的。\x01",
            "当然可以啦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6390")

    label("loc_629F")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F虽然会绕个远路，\x01",
            "不过还是去协会打个招呼吧。\x02\x03",
            "为慎重起见，\x01",
            "还是把昨天发生的事报告上去比较好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，嗯。\x01",
            "这样也好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6390")

    Jump("loc_646F")

    label("loc_6393")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63A9")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_63B0")

    label("loc_63A9")

    TurnDirection(0x102, 0x0, 400)

    label("loc_63B0")


    ChrTalk(
        0x102,
        (
            "#010F虽然会绕个远路，\x01",
            "不过还是去协会打个招呼吧。\x02\x03",
            "为慎重起见，\x01",
            "还是把昨天发生的事报告上去比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_646F")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_648A")

    Return()

    # Function_28_61C9 end

    def Function_29_648B(): pass

    label("Function_29_648B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《导力式时钟第１号机》\x01",
            "　七耀历１１６２年·蔡斯技术工房制造\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_29_648B end

    def Function_30_6519(): pass

    label("Function_30_6519")

    SetPlaceName(0x7D) # 蔡恩拉德酒店
    Return()

    # Function_30_6519 end

    def Function_31_651D(): pass

    label("Function_31_651D")

    SetPlaceName(0x7F) # 蔡恩拉德酒店
    Return()

    # Function_31_651D end

    def Function_32_6521(): pass

    label("Function_32_6521")

    SetPlaceName(0x82) # 蔡恩拉德酒店
    Return()

    # Function_32_6521 end

    def Function_33_6525(): pass

    label("Function_33_6525")

    SetPlaceName(0x7C) # 蔡恩拉德酒店
    Return()

    # Function_33_6525 end

    def Function_34_6529(): pass

    label("Function_34_6529")

    SetPlaceName(0x7A) # 蔡恩拉德酒店
    Return()

    # Function_34_6529 end

    def Function_35_652D(): pass

    label("Function_35_652D")

    SetPlaceName(0x7B) # 蔡恩拉德酒店
    Return()

    # Function_35_652D end

    def Function_36_6531(): pass

    label("Function_36_6531")

    SetPlaceName(0x80) # 蔡恩拉德酒店
    Return()

    # Function_36_6531 end

    SaveToFile()

Try(main)
