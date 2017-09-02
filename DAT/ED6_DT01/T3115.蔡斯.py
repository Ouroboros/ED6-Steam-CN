from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3115   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3115.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3115   ._SN',
            'ED6_DT01/T3115_1 ._SN',
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
        '玛多克工房长',                         # 9
        '凯诺娜上尉',                           # 10
        '将校',                                 # 11
        '士兵',                                 # 12
        '露依赛',                               # 13
        '加鲁诺',                               # 14
        '雨果',                                 # 15
        '格斯塔夫维修长',                       # 16
        '康丝坦茨',                             # 17
        '安东尼',                               # 18
        '伊格尔',                               # 19
        '普罗梅笛',                             # 20
        '威尔姆',                               # 21
        '玻璃杯',                               # 22
        '烟灰缸',                               # 23
        '香烟',                                 # 24
        '书1',                                  # 25
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
        'ED6_DT07/CH02620 ._CH',             # 00
        'ED6_DT07/CH02100 ._CH',             # 01
        'ED6_DT07/CH01310 ._CH',             # 02
        'ED6_DT07/CH01430 ._CH',             # 03
        'ED6_DT07/CH01190 ._CH',             # 04
        'ED6_DT07/CH01680 ._CH',             # 05
        'ED6_DT07/CH02440 ._CH',             # 06
        'ED6_DT07/CH01230 ._CH',             # 07
        'ED6_DT07/CH01700 ._CH',             # 08
        'ED6_DT07/CH01250 ._CH',             # 09
        'ED6_DT07/CH01100 ._CH',             # 0A
        'ED6_DT07/CH01450 ._CH',             # 0B
        'ED6_DT07/CH01640 ._CH',             # 0C
        'ED6_DT06/CH20021 ._CH',             # 0D
        'ED6_DT07/CH02623 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02620P._CP',             # 00
        'ED6_DT07/CH02100P._CP',             # 01
        'ED6_DT07/CH01310P._CP',             # 02
        'ED6_DT07/CH01430P._CP',             # 03
        'ED6_DT07/CH01190P._CP',             # 04
        'ED6_DT07/CH01680P._CP',             # 05
        'ED6_DT07/CH02440P._CP',             # 06
        'ED6_DT07/CH01230P._CP',             # 07
        'ED6_DT07/CH01700P._CP',             # 08
        'ED6_DT07/CH01250P._CP',             # 09
        'ED6_DT07/CH01100P._CP',             # 0A
        'ED6_DT07/CH01450P._CP',             # 0B
        'ED6_DT07/CH01640P._CP',             # 0C
        'ED6_DT06/CH20021P._CP',             # 0D
        'ED6_DT07/CH02623P._CP',             # 0E
    )

    DeclNpc(
        X                   = 2400,
        Z                   = 0,
        Y                   = 5300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 10,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917517,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 520,
        Z                   = 775,
        Y                   = 100690,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572877,
        ChipIndex           = 0xD,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1100,
        Z                   = 800,
        Y                   = 100800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638413,
        ChipIndex           = 0xD,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -105970,
        Z                   = 800,
        Y                   = 105440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703949,
        ChipIndex           = 0xD,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -101920,
        TriggerZ            = 0,
        TriggerY            = 93750,
        TriggerRange        = 1200,
        ActorX              = -101920,
        ActorZ              = 0,
        ActorY              = 93750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2950,
        TriggerZ            = 0,
        TriggerY            = 8029,
        TriggerRange        = 800,
        ActorX              = -2950,
        ActorZ              = 1000,
        ActorY              = 8029,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4150,
        TriggerZ            = 0,
        TriggerY            = 6850,
        TriggerRange        = 800,
        ActorX              = 4070,
        ActorZ              = 1000,
        ActorY              = 7610,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4700,
        TriggerZ            = 0,
        TriggerY            = 2240,
        TriggerRange        = 800,
        ActorX              = 5490,
        ActorZ              = 1000,
        ActorY              = 2270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1600,
        TriggerZ            = 0,
        TriggerY            = 3910,
        TriggerRange        = 800,
        ActorX              = 1600,
        ActorZ              = 1200,
        ActorY              = 3910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4430,
        TriggerZ            = 0,
        TriggerY            = 3760,
        TriggerRange        = 800,
        ActorX              = -5500,
        ActorZ              = 1200,
        ActorY              = 3500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 190,
        TriggerZ            = 0,
        TriggerY            = 101690,
        TriggerRange        = 1200,
        ActorX              = 720,
        ActorZ              = 800,
        ActorY              = 100680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -105970,
        TriggerZ            = 0,
        TriggerY            = 105440,
        TriggerRange        = 1500,
        ActorX              = -105970,
        ActorZ              = 800,
        ActorY              = 105440,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -100460,
        TriggerZ            = 0,
        TriggerY            = -3070,
        TriggerRange        = 800,
        ActorX              = -100460,
        ActorZ              = 1200,
        ActorY              = -3070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -100460,
        TriggerZ            = 0,
        TriggerY            = -4700,
        TriggerRange        = 800,
        ActorX              = -100460,
        ActorZ              = 1200,
        ActorY              = -4700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -100460,
        TriggerZ            = 0,
        TriggerY            = -6860,
        TriggerRange        = 800,
        ActorX              = -100460,
        ActorZ              = 1200,
        ActorY              = -6860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -103830,
        TriggerZ            = 0,
        TriggerY            = 5890,
        TriggerRange        = 800,
        ActorX              = -103830,
        ActorZ              = 1200,
        ActorY              = 5890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -104800,
        TriggerZ            = 0,
        TriggerY            = 9210,
        TriggerRange        = 800,
        ActorX              = -104800,
        ActorZ              = 1200,
        ActorY              = 9210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 31,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -101680,
        TriggerZ            = 0,
        TriggerY            = 9240,
        TriggerRange        = 800,
        ActorX              = -101680,
        ActorZ              = 1200,
        ActorY              = 9240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -100410,
        TriggerZ            = 0,
        TriggerY            = 8100,
        TriggerRange        = 800,
        ActorX              = -100410,
        ActorZ              = 1200,
        ActorY              = 8100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 33,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_55E",          # 00, 0
        "Function_1_BB5",          # 01, 1
        "Function_2_E95",          # 02, 2
        "Function_3_EAB",          # 03, 3
        "Function_4_ECF",          # 04, 4
        "Function_5_EF3",          # 05, 5
        "Function_6_1098",         # 06, 6
        "Function_7_118F",         # 07, 7
        "Function_8_1A46",         # 08, 8
        "Function_9_2665",         # 09, 9
        "Function_10_2684",        # 0A, 10
        "Function_11_41F9",        # 0B, 11
        "Function_12_5BF7",        # 0C, 12
        "Function_13_6439",        # 0D, 13
        "Function_14_696D",        # 0E, 14
        "Function_15_76AA",        # 0F, 15
        "Function_16_9305",        # 10, 16
        "Function_17_98AC",        # 11, 17
        "Function_18_A96D",        # 12, 18
        "Function_19_A9B7",        # 13, 19
        "Function_20_AA0B",        # 14, 20
        "Function_21_AA55",        # 15, 21
        "Function_22_AC17",        # 16, 22
        "Function_23_ACC0",        # 17, 23
        "Function_24_AD77",        # 18, 24
        "Function_25_AE33",        # 19, 25
        "Function_26_AEC2",        # 1A, 26
        "Function_27_B35C",        # 1B, 27
        "Function_28_B420",        # 1C, 28
        "Function_29_B4E5",        # 1D, 29
        "Function_30_B5AA",        # 1E, 30
        "Function_31_B66D",        # 1F, 31
        "Function_32_B734",        # 20, 32
        "Function_33_B7F8",        # 21, 33
    )


    def Function_0_55E(): pass

    label("Function_0_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_56C")
    OP_A3(0x3FA)
    Event(0, 17)

    label("loc_56C")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_578"),
        (SWITCH_DEFAULT, "loc_58E"),
    )


    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58B")
    OP_A2(0x50E)
    Event(0, 15)

    label("loc_58B")

    Jump("loc_58E")

    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_62F")
    SetChrPos(0xF, 2240, 0, 3050, 6)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -102890, 0, 97500, 280)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -108280, 0, 100340, 215)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -103290, 0, 108340, 355)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_6B5")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -102890, 0, 97500, 280)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -108280, 0, 100340, 215)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -103290, 0, 108340, 355)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_6B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_723")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xC, -104580, 0, 101850, 186)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -102890, 0, 97500, 280)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -103290, 0, 108340, 355)
    Jump("loc_B99")

    label("loc_723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_7AE")
    SetChrPos(0xC, -102800, 0, 96960, 277)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, -102800, 0, 97960, 270)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -101470, 0, 105910, 180)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_7AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_808")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -102890, 0, 97500, 280)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -101150, 0, -4440, 100)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_84C")
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -101430, 0, 102440, 267)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_84C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_85B")
    SetChrFlags(0x8, 0x80)
    Jump("loc_B99")

    label("loc_85B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_909")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86F")
    SetChrFlags(0x8, 0x80)

    label("loc_86F")

    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    SetChrPos(0xC, -103490, 0, 98980, 184)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xD, -102800, 0, 97960, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -102960, 0, 8850, 9)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -101660, 0, 107300, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    Jump("loc_B99")

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_9B4")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -102800, 0, 97440, 277)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2180, 0, 3050, 352)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -101150, 0, -4440, 100)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -106230, 0, 107410, 325)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_9B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_A5F")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -106270, 0, 103210, 195)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -106210, 0, 102010, 343)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -101150, 0, -4440, 100)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -103290, 0, 108340, 355)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_B07")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -102890, 0, 97500, 280)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -104980, 0, 101930, 319)
    OP_43(0x11, 0x0, 0x0, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -108240, 0, 100430, 225)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -103290, 0, 108340, 355)
    SetChrFlags(0x13, 0x10)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B99")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -102780, 0, 97390, 350)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -102830, 0, 98700, 178)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -103290, 0, 108340, 355)
    SetChrFlags(0x13, 0x10)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)

    label("loc_B99")

    SetChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB4")
    ClearChrFlags(0x18, 0x80)

    label("loc_BB4")

    Return()

    # Function_0_55E end

    def Function_1_BB5(): pass

    label("Function_1_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BCD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BFA")

    label("loc_BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BFA")

    label("loc_BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BFA")

    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D27")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C88")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_C88")

    Jump("loc_D27")

    label("loc_C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D23")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    PlayEffect(0x0, 0x0, 0xFF, -101920, 0, 93750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_D27")

    label("loc_D23")

    OP_64(0x0, 0x1)

    label("loc_D27")

    Jump("loc_D2E")

    label("loc_D2A")

    OP_64(0x0, 0x1)

    label("loc_D2E")

    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x400)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D72")
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)

    label("loc_D72")

    OP_64(0x6, 0x1)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x8000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA9")
    OP_65(0x6, 0x1)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_DA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x8000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DC4")
    OP_71(0x0, 0x10)
    OP_64(0x1, 0x1)

    label("loc_DC4")

    OP_64(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE4")
    OP_65(0x7, 0x1)

    label("loc_DE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF4")
    OP_64(0xD, 0x1)

    label("loc_DF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E04")
    OP_64(0x9, 0x1)

    label("loc_E04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E14")
    OP_64(0xE, 0x1)

    label("loc_E14")

    OP_64(0xA, 0x1)
    OP_64(0xB, 0x1)
    OP_64(0xC, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E35")
    OP_65(0xA, 0x1)

    label("loc_E35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4A")
    OP_65(0xB, 0x1)

    label("loc_E4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E5F")
    OP_65(0xC, 0x1)

    label("loc_E5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E94")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7A")
    OP_65(0xA, 0x1)

    label("loc_E7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E87")
    OP_65(0xB, 0x1)

    label("loc_E87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E94")
    OP_65(0xC, 0x1)

    label("loc_E94")

    Return()

    # Function_1_BB5 end

    def Function_2_E95(): pass

    label("Function_2_E95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EAA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_E95")

    label("loc_EAA")

    Return()

    # Function_2_E95 end

    def Function_3_EAB(): pass

    label("Function_3_EAB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ECE")
    OP_8D(0xFE, -105470, 104540, -101970, 99920, 3000)
    Jump("Function_3_EAB")

    label("loc_ECE")

    Return()

    # Function_3_EAB end

    def Function_4_ECF(): pass

    label("Function_4_ECF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EF2")
    OP_8D(0xFE, -106870, 104010, -102300, 99050, 3000)
    Jump("Function_4_ECF")

    label("loc_EF2")

    Return()

    # Function_4_ECF end

    def Function_5_EF3(): pass

    label("Function_5_EF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_F58")

    ChrTalk(
        0xF,
        (
            "#690F王国军的对应措施\x01",
            "采取得也太快了点。\x02\x03",
            "可以看出来\x01",
            "他们也十分焦急吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1094")

    label("loc_F58")

    OP_A2(0xB)

    ChrTalk(
        0xF,
        (
            "#690F『莱普尼兹号』\x01",
            "正在定期检修中，\x01",
            "目前停放在地下。\x02\x03",
            "已经把可能露出马脚的东西\x01",
            "都处理干净了，\x01",
            "应该没问题了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#803F是吗，那我就放心了……\x02\x03",
            "#800F说起来\x01",
            "军队的反应也太过迅速了。\x02\x03",
            "如果我们动作再慢一点，\x01",
            "说不定就会被他们抓住把柄了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1094")

    TalkEnd(0xFE)
    Return()

    # Function_5_EF3 end

    def Function_6_1098(): pass

    label("Function_6_1098")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_118B")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "『卡佩尔』的情况好转\x01",
            "果然是与导力停止有关系的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大概是因为导力停止，\x01",
            "才让整个系统重启了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "搞不好，\x01",
            "可以将其作为\x01",
            "新的维修方法使用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118B")

    TalkEnd(0xFE)
    Return()

    # Function_6_1098 end

    def Function_7_118F(): pass

    label("Function_7_118F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1249")
    TalkBegin(0x13)

    ChrTalk(
        0xFE,
        "据说…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "『埃尔赛尤号』的照片\x01",
            "很快会在王都的\x01",
            "历史资料馆里展出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，什么时候有空，\x01",
            "我也一定要去参观一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A42")

    label("loc_1249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_12E4")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哼，真是的，\x01",
            "资料怎么都找不到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来必须再次彻底地评估\x01",
            "整个工房的管理体制了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A42")

    label("loc_12E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1421")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1389")

    ChrTalk(
        0xFE,
        (
            "『埃尔赛尤号』\x01",
            "肯定也期待着能够\x01",
            "拥有一双崭新的翅膀。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果计划能够像这样\x01",
            "顺利进行下去的话就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141E")

    label("loc_1389")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "那位年轻的女士\x01",
            "是导力引擎开发项目里\x01",
            "新来的成员吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是气质高雅啊。\x01",
            "让人非常期待。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141E")

    Jump("loc_1A42")

    label("loc_1421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_14A5")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哦哦，太好了。\x01",
            "研究室内似乎没事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样很快就可以\x01",
            "将计划继续进行下去了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A42")

    label("loc_14A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1762")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x346)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15E1")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1556")

    ChrTalk(
        0xFE,
        (
            "通过这次的事，\x01",
            "我再次领会到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……我们还是没有\x01",
            "理解导力的本质。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15DE")

    label("loc_1556")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "据资料显示……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "上次那个现象\x01",
            "只能解释为\x01",
            "导力本身停止了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15DE")

    Jump("loc_175F")

    label("loc_15E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15FC")
    Call(1, 3)
    Jump("loc_175F")

    label("loc_15FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_172A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_169F")

    ChrTalk(
        0xFE,
        (
            "通过这次的事，\x01",
            "我再次领会到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……我们还是没有\x01",
            "理解导力的本质。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1727")

    label("loc_169F")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "据资料显示……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "上次那个现象\x01",
            "只能解释为\x01",
            "导力本身停止了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1727")

    Jump("loc_175F")

    label("loc_172A")


    ChrTalk(
        0xFE,
        "咦，还有什么事吗？\x02",
    )

    CloseMessageWindow()

    label("loc_175F")

    Jump("loc_1A42")

    label("loc_1762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1850")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "昨天发生的现象\x01",
            "还真让人吃惊啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据我所知，\x01",
            "以现在的导力理论\x01",
            "应该还不足以解释那种现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，我也算是个理论家，\x01",
            "对此次事件也十分关注。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A42")

    label("loc_1850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_18E9")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "呼，真是的。\x01",
            "资料都放在哪里了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样的话重新\x01",
            "设计一下图纸似乎还比较快。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A42")

    label("loc_18E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A42")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1991")

    ChrTalk(
        0xFE,
        (
            "从王立学院回来的途中\x01",
            "竟然被空贼抓作人质了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "现在回想起来还是觉得很恐怖呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A42")

    label("loc_1991")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "咦，\x01",
            "以前准备的资料都放到哪儿去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在去王立学院演讲之前\x01",
            "我都应该准备好了啊……\x01",
            "这已经是很早之前的事了呢。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_1A42")

    TalkEnd(0xFE)
    Return()

    # Function_7_118F end

    def Function_8_1A46(): pass

    label("Function_8_1A46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1B9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1AF4")

    ChrTalk(
        0xFE,
        (
            "真的是不得不佩服\x01",
            "你们游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟然敢深入王国军后方，\x01",
            "还顺利把拉赛尔救了出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B99")

    label("loc_1AF4")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "哦，是小姑娘你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "非常感谢你们\x01",
            "把拉赛尔救出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没～事，别担心啦\x01",
            "那家伙很顽强的。\x01",
            "肯定可以安然无恙地逃掉的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B99")

    Jump("loc_2661")

    label("loc_1B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1DF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1C8F")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "我要的资料怎么也找不到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "亏我经常严厉地\x01",
            "告诫康丝坦茨，\x01",
            "让她把资料整理好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "那个女的今天也很早就回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……真是的，头痛啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DEF")

    label("loc_1C8F")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "因为之前出现了导力停止现象，\x01",
            "街头时钟的时间已经不太准确了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要把时间调整回来，\x01",
            "就要找到建造当时的资料……\x01",
            "但现在完全找不到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……康丝坦茨那家伙真是的，\x01",
            "我总是说让她把资料室整理好，\x01",
            "她就是当作耳旁风。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "关键的时刻派不上用场，\x01",
            "那还叫做什么资料室啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DEF")

    Jump("loc_2661")

    label("loc_1DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1FC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1EC4")

    ChrTalk(
        0xFE,
        (
            "唉，真是的。\x01",
            "要查的书完全找不到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "脑子老是得不到满足，\x01",
            "现在连肚子都饿了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "一会儿去吃点东西吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC1")

    label("loc_1EC4")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "唉，真是的。\x01",
            "想查阅的书完全找不到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，有意思的是， \x01",
            "和眼下研究无关的资料\x01",
            "倒是一个接一个地发现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，这个也想看看，\x01",
            "那个也要回头翻一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……但是重要的是\x01",
            "还是找不到现在就需要的书。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC1")

    Jump("loc_2661")

    label("loc_1FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2064")
    TurnDirection(0x12, 0x10, 400)

    ChrTalk(
        0xFE,
        "喂，康丝坦茨！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你就不能\x01",
            "稍微用心点工作吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个资料室里的书\x01",
            "已经乱七八糟了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2136")

    label("loc_2064")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "我想来调查一下昨天发生的现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这书架还是那么脏啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这就说明\x01",
            "那个康丝坦茨\x01",
            "根本就没有好好整理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "不好好工作光拿薪水……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2136")

    Jump("loc_2661")

    label("loc_2139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2469")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_21FA")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "哦，提妲丫头。\x01",
            "辛苦你们啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "最好在游击士的陪同下\x01",
            "去做这种工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这是我年轻时遭遇过很多次危险后\x01",
            "总结出的经验教训呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2466")

    label("loc_21FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 6)), scpexpr(EXPR_END)), "loc_2297")

    ChrTalk(
        0xFE,
        (
            "好了，趁现在有空，\x01",
            "就找找相关的资料吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算光是浏览论文，\x01",
            "都要花费相当的时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2466")

    label("loc_2297")

    OP_A2(0x8)
    OP_A2(0x586)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        "哦，提妲丫头。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "卡鲁迪亚隧道的照明设备\x01",
            "更换工作进行得还顺利吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F嗯，那个……\x02\x03",
            "#067F那个……\x01",
            "还、还可以啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还可以？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我不知道你说的是什么意思，\x01",
            "总之更换好了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F嗯，是的。\x01",
            "那个已经没有问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦，那样就好。\x01",
            "辛苦你们啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过呢，\x01",
            "最好在游击士的陪同下\x01",
            "去做这种工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这是我年轻时遭遇过很多次危险后\x01",
            "总结出的经验教训呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F呵呵……\x01",
            "您说得没错。\x02\x03",
            "#562F嗯，今后我会注意的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2466")

    Jump("loc_2661")

    label("loc_2469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2661")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2583")

    ChrTalk(
        0xFE,
        (
            "关于新型引擎的开发，\x01",
            "本来应该是由拉赛尔\x01",
            "担当所有工作的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是他把中枢部分的\x01",
            "驱动导力器设计完成之后，\x01",
            "就去开始别的研究了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "全是因为他，\x01",
            "所以事情才会变成现在这样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2661")

    label("loc_2583")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "唔唔，研究员谢绝了邀请，\x01",
            "真的是很麻烦啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说『埃尔赛尤号』上\x01",
            "搭载的是改良的飞艇引擎，\x01",
            "但那只不过是暂时应付一下的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是没有正式的新型引擎，\x01",
            "好不容易建造的新型飞艇就毫无意义了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2661")

    TalkEnd(0xFE)
    Return()

    # Function_8_1A46 end

    def Function_9_2665(): pass

    label("Function_9_2665")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2680")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵－噢。\x02",
    )

    CloseMessageWindow()

    label("loc_2680")

    TalkEnd(0xFE)
    Return()

    # Function_9_2665 end

    def Function_10_2684(): pass

    label("Function_10_2684")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_26D9")

    ChrTalk(
        0xFE,
        "真是辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，再有什么事的话，\x01",
            "还会拜托你们的哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_26D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2F71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2705")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2705")
    Call(1, 6)
    TalkEnd(0xFE)
    Return()

    label("loc_2705")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2720")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_2720")
    Call(1, 8)
    TalkEnd(0xFE)
    Return()

    label("loc_2720")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_273B")
    Call(1, 10)
    TalkEnd(0xFE)
    Return()

    label("loc_273B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2756")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_2756")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_2756")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_28E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_27FE")

    ChrTalk(
        0xFE,
        (
            "……啊，\x01",
            "工作已经做得差不多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说有点早，\x01",
            "不过现在去吃午饭也好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到了中午，\x01",
            "店里面就很拥挤了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E6")

    label("loc_27FE")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "工房终于平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里老是出现混乱，\x01",
            "都没有工作的时间了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过安排好预算的话\x01",
            "还是能全部处理完的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呜呜…………\x02",
    )

    CloseMessageWindow()

    label("loc_28E6")

    Jump("loc_2F6E")

    label("loc_28E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_2A82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_29A9")

    ChrTalk(
        0xFE,
        (
            "……啊，\x01",
            "工作已经做得差不多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说有点早，\x01",
            "不过现在去吃午饭也好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天又没吃早点，\x01",
            "这样下去会伤身体的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_29A9")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "工房终于平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里老是出现混乱，\x01",
            "都没有工作的时间了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "干脆使用一点预算\x01",
            "让别人帮忙整理一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A7F")

    Jump("loc_2F6E")

    label("loc_2A82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E16")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2B60")

    ChrTalk(
        0xFE,
        (
            "虽然对你们有点不好意思， \x01",
            "但是委托已经中止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "剩下的工作就交给蔡斯支部来做，\x01",
            "请放心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果以后还有委托的话，\x01",
            "就请你们一定要做到底。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，你们多保重。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E13")

    label("loc_2B60")

    OP_28(0x2D, 0x1, 0x8000)

    ChrTalk(
        0xFE,
        "咦，是你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然对你们有点不好意思， \x01",
            "但是委托已经中止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F嗯？为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我从协会那里听说了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们马上就要\x01",
            "调到别的支部去了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以调离之前，\x01",
            "必须将委托的事宜整理好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F是吗……\x02\x03",
            "对不起。\x01",
            "委托半途而废……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F真的很抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，别在意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为你们还有别的重要工作，\x01",
            "这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "剩下的工作交给\x01",
            "蔡斯支部接手就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F好吧，\x01",
            "这样也算帮了我们大忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那以后也要继续努力哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果以后还有委托的话，\x01",
            "就请你们一定要做到底。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F感谢最近一段时间\x01",
            "您对我们的诸多照顾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E13")

    Jump("loc_2F6E")

    label("loc_2E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2ECB")

    ChrTalk(
        0xFE,
        (
            "……啊，\x01",
            "工作已经做得差不多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说有点早，\x01",
            "不过现在去吃午饭也好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天又没吃早点，\x01",
            "这样下去会伤身体的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F6E")

    label("loc_2ECB")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "工房终于平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里老是出现混乱，\x01",
            "都没有工作的时间了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "快点开始整理资料吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F6E")

    Jump("loc_41F5")

    label("loc_2F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3172")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F9D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F9D")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_2F9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_2FB8")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_2FB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_2FD3")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_2FD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FEE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_2FEE")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_2FEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30AC")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "我怎么又有种不太稳当的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "工房长不知道去哪儿了不说，\x01",
            "维修员也是到处乱跑……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是的，一点都不安下心来。\x02",
    )

    CloseMessageWindow()
    Jump("loc_316F")

    label("loc_30AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30C5")
    Call(1, 4)
    Jump("loc_316F")

    label("loc_30C5")


    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "我怎么又有种不太稳当的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "工房长不知道去哪儿了不说，\x01",
            "维修员也是到处乱跑……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是的，一点都不安下心来。\x02",
    )

    CloseMessageWindow()

    label("loc_316F")

    Jump("loc_41F5")

    label("loc_3172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3326")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_319E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_319E")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_319E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_31B9")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_31B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_31D4")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_31D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31EF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_31EF")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_31EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3245")

    ChrTalk(
        0xFE,
        "啊，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天一整天能平平安安就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3323")

    label("loc_3245")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_32C1")

    ChrTalk(
        0xFE,
        "啊，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天一整天能平平安安就好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要的书\x01",
            "也能快点找到就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3323")

    label("loc_32C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32DA")
    Call(1, 4)
    Jump("loc_3323")

    label("loc_32DA")


    ChrTalk(
        0xFE,
        "啊，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天一整天能平平安安就好了。\x02",
    )

    CloseMessageWindow()

    label("loc_3323")

    Jump("loc_41F5")

    label("loc_3326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_35EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_33AF")

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
    Jump("loc_35E9")

    label("loc_33AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3437")

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
    OP_A2(0xD)
    Jump("loc_35E9")

    label("loc_3437")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_34D4")

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
    OP_A2(0xD)
    Jump("loc_35E9")

    label("loc_34D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3572")

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
    OP_A2(0xD)
    Jump("loc_35E9")

    label("loc_3572")


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
    OP_A2(0xD)

    label("loc_35E9")

    Jump("loc_41F5")

    label("loc_35EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3855")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3618")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3618")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_3618")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3633")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_3633")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_3633")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_364E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_364E")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_364E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3669")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_3669")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_3669")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_375B")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "那是演算室的威尔姆吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "第一次靠得这么近看，\x01",
            "原来也就是个普通的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且……\x01",
            "感觉他有点神经质啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3852")

    label("loc_375B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3774")
    Call(1, 4)
    Jump("loc_3852")

    label("loc_3774")


    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "那是演算室的威尔姆吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "第一次靠得这么近看，\x01",
            "原来也就是个普通的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且……\x01",
            "感觉他有点神经质啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3852")

    Jump("loc_41F5")

    label("loc_3855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_39BC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3881")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3881")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_3881")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_389C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_389C")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_389C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_38B7")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_38B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_38D2")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_38D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3943")

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "伊格尔就不能安静地看会儿书吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这种场合下\x01",
            "保持安静可是常识啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39B9")

    label("loc_3943")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_395C")
    Call(1, 4)
    Jump("loc_39B9")

    label("loc_395C")


    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "伊格尔就不能安静地看会儿书吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这种场合下\x01",
            "保持安静可是常识啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39B9")

    Jump("loc_41F5")

    label("loc_39BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3B5B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39E8")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_39E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A03")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_3A03")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_3A03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A1E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_3A1E")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_3A1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A39")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_3A39")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_3A39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AC6")

    ChrTalk(
        0xFE,
        (
            "那边的伊格尔\x01",
            "还真不是一般的啰嗦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我总算知道为什么\x01",
            "他那种岁数还是单身。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B58")

    label("loc_3AC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3ADF")
    Call(1, 4)
    Jump("loc_3B58")

    label("loc_3ADF")


    ChrTalk(
        0xFE,
        (
            "那边的伊格尔\x01",
            "还真不是一般的啰嗦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我总算知道为什么\x01",
            "他那种岁数还是单身。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B58")

    Jump("loc_41F5")

    label("loc_3B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3F28")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B87")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B87")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_3B87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_3BA2")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_3BA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BBD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_3BBD")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_3BBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_3BD8")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_3BD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3C91")

    ChrTalk(
        0xFE,
        (
            "啊，我以为是谁呢，\x01",
            "这不是各位游击士和提妲吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们特地为我把书收集回来，\x01",
            "真是很感谢呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "多亏你们，\x01",
            "看来我暂时不用工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F25")

    label("loc_3C91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_3CFD")

    ChrTalk(
        0xFE,
        (
            "那么，再找到其他书的话，\x01",
            "记得送到这里来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "各位游击士，\x01",
            "之前多亏你们了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F25")

    label("loc_3CFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D16")
    Call(1, 4)
    Jump("loc_3F25")

    label("loc_3D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3D91")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "提妲你偶尔\x01",
            "也来帮忙整理一下书嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "光让我一个人干的话，\x01",
            "我会有种资料室将发生\x01",
            "不得了的事的预感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F25")

    label("loc_3D91")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "欢迎来到资料室。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD4")

    ChrTalk(
        0xFE,
        "啊，这不是提妲吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DF5")

    label("loc_3DD4")

    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "这不是提妲吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF5")


    ChrTalk(
        0x107,
        (
            "#060F啊，康丝坦茨阿姨。\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是好久不见了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "提妲你偶尔\x01",
            "也来帮忙整理一下书嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "光让我一个人干的话，\x01",
            "我会有种资料室将发生\x01",
            "不得了的事的预感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，啊哈哈……\x01",
            "我、我知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "提妲你可真是一个好孩子㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么就拜托了～\x02",
    )

    CloseMessageWindow()

    label("loc_3F25")

    Jump("loc_41F5")

    label("loc_3F28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F4D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F4D")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_3F4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F68")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_3F68")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_3F68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F83")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_3F83")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_3F83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_3F9E")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_3F9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4048")

    ChrTalk(
        0xFE,
        (
            "啊，我以为是谁呢，\x01",
            "各位游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们特地为我把书收集回来，\x01",
            "真是很感谢呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有想要看的书，\x01",
            "就请随便看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F5")

    label("loc_4048")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_40D1")

    ChrTalk(
        0xFE,
        (
            "如果有想要看的资料，\x01",
            "就请随便看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "拜托你们了，\x01",
            "找到了书的话，\x01",
            "就请拿到这里来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F5")

    label("loc_40D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40EA")
    Call(1, 4)
    Jump("loc_41F5")

    label("loc_40EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_416D")

    ChrTalk(
        0xFE,
        (
            "如果有想要看的书，\x01",
            "就请随便看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，看完之后，\x01",
            "请务必把书放回原处。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F5")

    label("loc_416D")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "哎，我好像没见过你们啊……\x01",
            "啊，这种事倒也无所谓。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "欢迎你们来资料室。\x01",
            "我是这里的管理员康丝坦茨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有想要看的书，\x01",
            "就请随便看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F5")

    TalkEnd(0xFE)
    Return()

    # Function_10_2684 end

    def Function_11_41F9(): pass

    label("Function_11_41F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_43B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4277")

    ChrTalk(
        0x8,
        (
            "#800F说起来\x01",
            "军队的反应也太过迅速了。\x02\x03",
            "他们也会抱着\x01",
            "拼命的决心来搜查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43AF")

    label("loc_4277")

    OP_A2(0x3)
    OP_4A(0xF, 255)

    ChrTalk(
        0xF,
        (
            "#690F『莱普尼兹号』\x01",
            "正在定期检修中，\x01",
            "目前停放在地下。\x02\x03",
            "已经把可能露出马脚的东西\x01",
            "都处理干净了，\x01",
            "应该没问题了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#803F是吗，那我就放心了……\x02\x03",
            "#800F说起来\x01",
            "军队的反应也太过迅速了。\x02\x03",
            "如果我们动作再慢一点，\x01",
            "说不定就会被他们抓住把柄了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xF, 255)

    label("loc_43AF")

    SetChrSubChip(0xFE, 0)
    Jump("loc_5BF3")

    label("loc_43B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_45A2")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43E0")
    SetChrSubChip(0xFE, 1)
    Jump("loc_43FB")

    label("loc_43E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43F6")
    SetChrSubChip(0xFE, 0)
    Jump("loc_43FB")

    label("loc_43F6")

    SetChrSubChip(0xFE, 2)

    label("loc_43FB")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_44D9")

    ChrTalk(
        0x8,
        (
            "#803F呼，\x01",
            "总之『卡佩尔』已经隐藏好了……\x02\x03",
            "之后的问题就是\x01",
            "『莱普尼兹号』了吧。\x02\x03",
            "#800F这事还是和格斯塔夫\x01",
            "商量一下比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459A")

    label("loc_44D9")

    OP_A2(0x3)

    ChrTalk(
        0x8,
        (
            "#802F咦，艾丝蒂尔、约修亚。\x01",
            "还没有出发吗？\x02\x03",
            "#801F这里的事你们不用担心。\x01",
            "就算军队来检查，\x01",
            "我也会设法应付他们的。\x02\x03",
            "总之去王都的路上要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_459A")

    SetChrSubChip(0xFE, 0)
    Jump("loc_5BF3")

    label("loc_45A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4A7F")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45CB")
    SetChrSubChip(0xFE, 1)
    Jump("loc_45E6")

    label("loc_45CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45E1")
    SetChrSubChip(0xFE, 0)
    Jump("loc_45E6")

    label("loc_45E1")

    SetChrSubChip(0xFE, 2)

    label("loc_45E6")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4840")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4667")

    ChrTalk(
        0x8,
        (
            "#800F就算是为了提妲，\x01",
            "你们也要救出拉赛尔博士啊。\x02\x03",
            "那我就等着你们的好消息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_483D")

    label("loc_4667")

    OP_A2(0x3)

    ChrTalk(
        0x8,
        (
            "#800F哟，早上好。\x02\x03",
            "找到什么线索没有？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯，\x01",
            "现在要去协会确认一下情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#802F咦，\x01",
            "说起来提妲没和你们一起吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F她去医务室\x01",
            "照看阿加特兄了。\x02\x03",
            "提妲她似乎相当担心\x01",
            "阿加特兄的情况呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#803F……是吗？\x02\x03",
            "就算是为了提妲，\x01",
            "你们也要救出拉赛尔博士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯，我会加油的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F一定全力以赴。\x02\x03",
            "那么，我们先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#800F嗯，等你们的好消息。\x02",
    )

    CloseMessageWindow()

    label("loc_483D")

    Jump("loc_4A77")

    label("loc_4840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_48B4")

    ChrTalk(
        0x8,
        (
            "#800F有力的线索吗……\x02\x03",
            "我很期待呢。\x01",
            "博士的事就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A77")

    label("loc_48B4")

    OP_A2(0x3)

    ChrTalk(
        0x8,
        (
            "#800F哟，各位。\x01",
            "找到什么线索没有？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯，\x01",
            "虽然得到了一些情报……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F抱歉，工房长先生。\x02\x03",
            "现在还在搜查当中，\x01",
            "详细的情况暂时不便透露。\x02\x03",
            "#012F不过……确实已经得到\x01",
            "与犯人有关的有力线索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#802F哦哦，是吗！\x02\x03",
            "#801F看来调查也取得了\x01",
            "相当大的进展啊。\x02\x03",
            "我等着你们的好消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，我们一定会努力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么，我们先告辞了。\x02",
    )

    CloseMessageWindow()

    label("loc_4A77")

    SetChrSubChip(0xFE, 0)
    Jump("loc_5BF3")

    label("loc_4A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4EA8")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4AA8")
    SetChrSubChip(0xFE, 1)
    Jump("loc_4AC3")

    label("loc_4AA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4ABE")
    SetChrSubChip(0xFE, 0)
    Jump("loc_4AC3")

    label("loc_4ABE")

    SetChrSubChip(0xFE, 2)

    label("loc_4AC3")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4B21")

    ChrTalk(
        0x8,
        (
            "#800F现在不是闲聊的场合吧。\x01",
            "　\x02\x03",
            "你们赶快去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EA0")

    label("loc_4B21")

    OP_A2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 6)), scpexpr(EXPR_END)), "loc_4BB4")

    ChrTalk(
        0x8,
        (
            "#800F据说受伤的游击士\x01",
            "已经送到医务室去了。\x02\x03",
            "现在似乎不是闲聊的场合吧。\x01",
            "　\x02\x03",
            "你们赶快去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EA0")

    label("loc_4BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_4D5A")

    ChrTalk(
        0x8,
        (
            "#800F哦哦，是你们啊。\x02\x03",
            "据说受伤的游击士\x01",
            "已经被送回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯，\x01",
            "他是中了某种未知的毒……\x02\x03",
            "我们刚刚向皮克赛恩教区长\x01",
            "请教了治疗方法。\x02\x03",
            "现在马上就去钟乳石洞\x01",
            "采集做药的材料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F嗯，\x01",
            "那么这可不是闲聊的时候呢。\x02\x03",
            "你们赶快去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F是的，我们这就去。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EA0")

    label("loc_4D5A")


    ChrTalk(
        0x8,
        (
            "#800F哦哦，是你们啊。\x02\x03",
            "据说受伤的游击士\x01",
            "已经被送回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯，\x01",
            "他是中了某种未知的毒……\x02\x03",
            "我们正准备去找\x01",
            "皮克塞恩教区长询问治疗方法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F嗯，\x01",
            "那么这可不是闲聊的时候呢。\x02\x03",
            "你们赶快去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F是的，我们这就去。\x02",
    )

    CloseMessageWindow()

    label("loc_4EA0")

    SetChrSubChip(0xFE, 0)
    Jump("loc_5BF3")

    label("loc_4EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_END)), "loc_4FAC")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4ED1")
    SetChrSubChip(0xFE, 1)
    Jump("loc_4EEC")

    label("loc_4ED1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EE7")
    SetChrSubChip(0xFE, 0)
    Jump("loc_4EEC")

    label("loc_4EE7")

    SetChrSubChip(0xFE, 2)

    label("loc_4EEC")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0x8,
        (
            "#800F根据我的判断，\x01",
            "拉赛尔博士被掳走的事\x01",
            "还是瞒着大多数人比较好。\x02\x03",
            "这样子你们行动起来\x01",
            "也会比较方便吧。\x02\x03",
            "博士的事\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_5BF3")

    label("loc_4FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_5238")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4FD5")
    SetChrSubChip(0xFE, 1)
    Jump("loc_4FF0")

    label("loc_4FD5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4FEB")
    SetChrSubChip(0xFE, 0)
    Jump("loc_4FF0")

    label("loc_4FEB")

    SetChrSubChip(0xFE, 2)

    label("loc_4FF0")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_50B7")

    ChrTalk(
        0x8,
        (
            "#803F根据我的判断，\x01",
            "拉赛尔博士被掳走的事\x01",
            "还是瞒着大多数人比较好。\x02\x03",
            "#800F这样子你们行动起来\x01",
            "也会比较方便吧。\x02\x03",
            "博士的事\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5230")

    label("loc_50B7")

    OP_A2(0x3)

    ChrTalk(
        0x8,
        (
            "#803F…………………………\x02\x03",
            "……根据我的判断，\x01",
            "拉赛尔博士被掳走的事\x01",
            "还是瞒着大多数人比较好。\x02\x03",
            "这样子你们行动起来\x01",
            "也会比较方便吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F我认为这个判断相当正确。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F嗯，要不然肯定会引起恐慌的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F各位游击士。\x01",
            "博士的事就拜托了。\x02\x03",
            "……提妲，\x01",
            "你也不要太过沮丧哦。\x02\x03",
            "没事的，\x01",
            "博士一定会平安的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F好的…………\x02\x03",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5230")

    SetChrSubChip(0xFE, 0)
    Jump("loc_5BF3")

    label("loc_5238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5473")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529B")

    ChrTalk(
        0x8,
        (
            "#800F提妲就拜托你们两个照顾了。\x01",
            "　\x02\x03",
            "提妲，\x01",
            "去的时候要当心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5470")

    label("loc_529B")

    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52BD")
    SetChrSubChip(0xFE, 1)
    Jump("loc_52D8")

    label("loc_52BD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52D3")
    SetChrSubChip(0xFE, 0)
    Jump("loc_52D8")

    label("loc_52D3")

    SetChrSubChip(0xFE, 2)

    label("loc_52D8")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_53AA")

    ChrTalk(
        0x8,
        (
            "#805F啊，是你们啊。\x01",
            "刚才很抱歉呢。\x02\x03",
            "从现在起我要好好休养，\x01",
            "还要努力争取\x01",
            "早日和香烟一刀两断啊。\x02\x03",
            "#800F那么，到亚尔摩去的路上\x01",
            "提妲就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_546B")

    label("loc_53AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_53D9")

    ChrTalk(
        0x8,
        (
            "#805F发、发现什么了吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_546B")

    label("loc_53D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53FB")
    SetChrSubChip(0xFE, 0)
    Call(1, 2)
    Jump("loc_546B")

    label("loc_53FB")


    ChrTalk(
        0x8,
        (
            "#800F咦，怎么了？\x02\x03",
            "去亚尔摩村的话，\x01",
            "要从西南方的门口出城啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_546B")

    SetChrSubChip(0xFE, 0)

    label("loc_5470")

    Jump("loc_5BF3")

    label("loc_5473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_5574")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_54F2")

    ChrTalk(
        0x8,
        (
            "#800F我听说了，\x01",
            "卢安的库莱泽谢绝此次工作邀请了。\x02\x03",
            "代替他的人……\x01",
            "不是那么容易可以找到的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5571")

    label("loc_54F2")

    OP_A2(0x3)

    ChrTalk(
        0x8,
        (
            "#800F哦，雨果。\x02\x03",
            "我都听说了，\x01",
            "卢安的库莱泽谢绝此次工作邀请了。\x02\x03",
            "代替他的人……\x01",
            "不是那么容易可以找到的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5571")

    Jump("loc_5BF3")

    label("loc_5574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_5AD1")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_559D")
    SetChrSubChip(0xFE, 1)
    Jump("loc_55B8")

    label("loc_559D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_55B3")
    SetChrSubChip(0xFE, 0)
    Jump("loc_55B8")

    label("loc_55B3")

    SetChrSubChip(0xFE, 2)

    label("loc_55B8")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 4)), scpexpr(EXPR_END)), "loc_5681")

    ChrTalk(
        0x8,
        (
            "#800F博士应该在\x01",
            "三楼的工作室里面。\x02\x03",
            "#805F拜托了， \x01",
            "千万不要太过蛮干。\x02\x03",
            "#806F再发生昨天那样的事，\x01",
            "短时间内就无法进行实验了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AC9")

    label("loc_5681")

    OP_A2(0x584)
    OP_28(0x3F, 0x1, 0x40)

    ChrTalk(
        0x8,
        "#800F哟，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F早上好，工房长叔叔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560F早上好～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#805F唉，真是的，\x01",
            "昨天的事让人头疼啊。\x02\x03",
            "一大清早，\x01",
            "市民就来发泄不满，忙得我团团转。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F哇，好可怜哦。\x02\x03",
            "其实这又不是\x01",
            "工房长叔叔的错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#561F抱歉，工房长叔叔。\x02\x03",
            "都怪我们，\x01",
            "引起了这样的麻烦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#802F啊，没有没有，\x01",
            "你们不用道歉啊。\x02\x03",
            "这样的事故\x01",
            "在实验过程中时而发生\x01",
            "也是可以理解的。\x02\x03",
            "#803F……唉，要是拉赛尔博士的话，\x01",
            "简直就是经常性的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F博士已经来了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F哦哦，似乎相当有干劲呢。\x01",
            "这么一大清早就来了。\x02\x03",
            "他肯定需要人帮忙，\x01",
            "你们现在就去看看吧。\x02\x03",
            "他现在肯定在\x01",
            "三楼的工作室里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F三楼的工作室吗。\x02\x03",
            "我们马上过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，我们也很在意呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#800F啊，提妲！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F嗯？什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#805F千、千万不要\x01",
            "让博士再乱来哦。\x01",
            "千万不要太过蛮干。\x02\x03",
            "#806F再发生昨天那样的事，\x01",
            "短时间内就无法进行实验了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F好的，我明白了。\x02\x03",
            "#060F那么，工房长叔叔，告辞了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AC9")

    SetChrSubChip(0xFE, 0)
    Jump("loc_5BF3")

    label("loc_5AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5BF3")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5AFA")
    SetChrSubChip(0xFE, 1)
    Jump("loc_5B15")

    label("loc_5AFA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B10")
    SetChrSubChip(0xFE, 0)
    Jump("loc_5B15")

    label("loc_5B10")

    SetChrSubChip(0xFE, 2)

    label("loc_5B15")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0x8,
        (
            "#802F哦，怎么了？\x02\x03",
            "博士的工房\x01",
            "在城市的西南方哦。\x02\x03",
            "#801F如果有什么新发现，\x01",
            "记得一定要先来告诉我啊。\x02\x03",
            "对于我们这些技术工作者来说，\x01",
            "这个可是非常让人感兴趣的哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)

    label("loc_5BF3")

    TalkEnd(0xFE)
    Return()

    # Function_11_41F9 end

    def Function_12_5BF7(): pass

    label("Function_12_5BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_5D95")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C9F")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "刚才我们关于新型导力引擎\x01",
            "开了一个讨论会，\x01",
            "现在刚刚结束。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天没想出什么好点子，真是急坏我了。\x01",
            "但不管怎么说好歹混了过去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D8F")

    label("loc_5C9F")


    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "当思考遇到瓶颈的时候，\x01",
            "吃点东西也是很有效果的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天刚喝了些汤，\x01",
            "霎时间灵光一现……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再遇到大脑停电，\x01",
            "就把乌尔斯叫来，\x01",
            "让他给我炖汤。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D8F")

    TalkEnd(0xFE)
    Jump("loc_6438")

    label("loc_5D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_6180")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_44(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6026")
    OP_A2(0x2)

    ChrTalk(
        0xC,
        (
            "我们面临的现状是，\x01",
            "就算将翼层断面和导力系统进行改良，\x01",
            "推进效率也很难提高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "所以，不妨转变一下视点，\x01",
            "从操作简便性的方面\x01",
            "重新考虑一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "重新评估机体各部件的配置，\x01",
            "按照减阻装置的形状， \x01",
            "将连接外部的通路简化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "原来如此，是采用最适合\x01",
            "『埃尔赛尤号』的发动机短舱形式，\x01",
            "追求完备性吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "着眼点很有意思呢。\x01",
            "比起极限性能，运转效率的重要性\x01",
            "在应用方面是得到大家一致认同的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6177")

    label("loc_6026")


    ChrTalk(
        0xFE,
        (
            "这个引擎在功率输出方面\x01",
            "已经得到保证了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果可以将拉赛尔博士\x01",
            "新设计的驱动导力器实现的话，\x01",
            "实际性能可以大大超出要求吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以，\x01",
            "希望今后在设计上\x01",
            "能够多多考虑完备性的方面。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6177")

    OP_85(0xE)
    TalkEnd(0xFE)
    Jump("loc_6438")

    label("loc_6180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_6438")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0xD, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6368")
    OP_A2(0x1)
    SetChrName("设计室")

    ChrTalk(
        0xD,
        (
            "嗯，这个枪身的设计\x01",
            "希望可以短一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不然的话，我想就不能充分发挥\x01",
            "苦心设计的导力高压的性能了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "嗯，确实，\x01",
            "从工学的角度上来说是这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "可是如果再短的话， \x01",
            "会变得头重脚轻吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "考虑到握持方法的话，\x01",
            "这种设计似乎……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "虽然我也\x01",
            "考虑了这方面的因素，\x01",
            "不过这不符合我的方针。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "总之我希望\x01",
            "可以严格按照\x01",
            "发挥最佳性能的方针进行设计。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "啊，是吗。\x01",
            "是这样啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6431")

    label("loc_6368")


    ChrTalk(
        0xC,
        "不、不过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "还是稍微考虑一下\x01",
            "操作的简易性比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "但是，那样的话，\x01",
            "性能方面必然有所牺牲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我希望露依赛你\x01",
            "也能够做一个\x01",
            "敢于挑战极限的技术人员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "啊，是、是吗……\x02",
    )

    CloseMessageWindow()

    label("loc_6431")

    OP_4B(0xD, 255)
    TalkEnd(0xFE)

    label("loc_6438")

    Return()

    # Function_12_5BF7 end

    def Function_13_6439(): pass

    label("Function_13_6439")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_670B")
    OP_4A(0xC, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_661C")
    OP_A2(0x1)
    SetChrName("设计室")

    ChrTalk(
        0xD,
        (
            "嗯，这个枪身的设计\x01",
            "希望可以短一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不然的话，我想就不能充分发挥\x01",
            "苦心设计的导力高压的性能了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "嗯，确实，\x01",
            "从工学的角度上来说是这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "可是如果再短的话， \x01",
            "会变得头重脚轻吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "考虑到握持方法的话，\x01",
            "这种设计似乎……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "虽然我也\x01",
            "考虑了这方面的因素，\x01",
            "不过这不符合我的方针。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "总之我希望\x01",
            "可以严格按照\x01",
            "发挥最佳性能的方针进行设计。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "啊，是吗。\x01",
            "是这样啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6704")

    label("loc_661C")


    ChrTalk(
        0xC,
        "不、不过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "还是稍微考虑一下\x01",
            "操作的简易性比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "但是，那样的话，\x01",
            "性能方面必然有所牺牲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我希望露依赛你\x01",
            "也能够做一个\x01",
            "敢于挑战极限的技术人员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "（这是最后一次机会了，\x01",
            "　不好好做的话……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6704")

    OP_4B(0xC, 255)
    Jump("loc_6964")

    label("loc_670B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_67F1")

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "露依赛要调到其他部门了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "能调到她最想去的飞艇部门，\x01",
            "真是可喜可贺呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，我也不能输给她。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要努力争取早日让\x01",
            "新型的导力枪成品化。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6964")

    label("loc_67F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_6964")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_689C")

    ChrTalk(
        0xFE,
        (
            "她是个优秀的研究员，\x01",
            "经验也积累了不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "让她去做自己想做的事情，\x01",
            "我想对工房也有好处。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6964")

    label("loc_689C")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "露依赛啊……\x01",
            "嗯，她是个优秀的研究员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过真可惜呀……\x01",
            "她好像已经对\x01",
            "导力枪开发失去了热情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要她做其他开发项目我也赞成，\x01",
            "这对她来说也是件好事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6964")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_13_6439 end

    def Function_14_696D(): pass

    label("Function_14_696D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_6B09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6A19")

    ChrTalk(
        0xFE,
        (
            "不过，加鲁诺也是\x01",
            "有着实际成就的研究员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果是他的话，\x01",
            "继续进行导力枪的研究是没问题的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B06")

    label("loc_6A19")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "虽然经历了一些波折，\x01",
            "不过导力引擎的开发计划\x01",
            "终于开始有进展了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "中途加入的露依赛\x01",
            "做得比预想还要好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然这让加鲁诺失去了一个优秀助手，\x01",
            "总感觉有点对不起他，\x01",
            "不过确实对我们帮助很大。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B06")

    Jump("loc_76A6")

    label("loc_6B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_6BA2")

    ChrTalk(
        0xFE,
        (
            "呼～第一次的商讨很顺利，\x01",
            "真是让我松了一口气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "感觉对新的工作越来越顺手了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76A6")

    label("loc_6BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_6EF3")
    OP_44(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E29")
    OP_A2(0x2)

    ChrTalk(
        0xC,
        (
            "我们面临的现状是，\x01",
            "就算将翼层断面和导力系统进行改良，\x01",
            "推进效率也很难提高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "所以，不妨转变一下视点，\x01",
            "从操作简便性的方面\x01",
            "重新考虑一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "重新评估机体各部件的配置，\x01",
            "按照减阻装置的形状， \x01",
            "将连接外部的通路简化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "原来如此，是采用最适合\x01",
            "『埃尔赛尤号』的发动机短舱形式，\x01",
            "追求完备性吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "着眼点很有意思呢。\x01",
            "比起极限性能，运转效率的重要性\x01",
            "在应用方面是得到大家一致认同的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EED")

    label("loc_6E29")


    ChrTalk(
        0xFE,
        (
            "虽然还处在概念阶段，\x01",
            "不过这个方法真的很有前途。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "用整备性的观点\x01",
            "对内部构造重新观察分析，\x01",
            "是至今为止从没有过的想法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EED")

    OP_85(0xC)
    Jump("loc_76A6")

    label("loc_6EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_7017")

    ChrTalk(
        0xFE,
        (
            "新型导力引擎的开发\x01",
            "大胆邀请了新手露依赛\x01",
            "共同参加开发工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于她是一个相当大的考验，\x01",
            "而对于我们来说也是一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果年轻一代的想法\x01",
            "能够有利于研究就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过说实话我还是很担心。\x01",
            "真是的，胃又开始疼了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76A6")

    label("loc_7017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_7098")

    ChrTalk(
        0xFE,
        "对不起，我正忙着呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实是关于\x01",
            "『埃尔赛尤号』\x01",
            "新型导力引擎的开发工程……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76A6")

    label("loc_7098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_726B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7123")

    ChrTalk(
        0xFE,
        (
            "我想露依赛她\x01",
            "也差不多该独立了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果你的意见和我一样的话，\x01",
            "我可以马上向工房长提出申请。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7268")

    label("loc_7123")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "虽然我知道昨晚发生了那样的事，\x01",
            "你现在应该非常忙……\x01",
            "不过请借用我一点时间可以吗，加鲁诺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我听说了露依赛的事，\x01",
            "她的志愿是做飞艇方面的研究吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可以的话，\x01",
            "能不能让她参加这次的\x01",
            "『埃尔赛尤号』新型引擎开发呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……你作为她的主管，\x01",
            "意见如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7268")

    Jump("loc_76A6")

    label("loc_726B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_74CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7380")

    ChrTalk(
        0xFE,
        (
            "『埃尔赛尤号』\x01",
            "是以新型引擎为前提\x01",
            "设计出来的机体。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果借用旧的引擎，\x01",
            "就不能发挥出原本的性能了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼～在这点上说不定需要\x01",
            "大胆地转换思考的方向才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x11, 400)

    ChrTalk(
        0xFE,
        (
            "喂，安东尼。\x01",
            "如果是你，会选择谁呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74C8")

    label("loc_7380")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "能够担任开发『埃尔赛尤号』的\x01",
            "新型引擎研究员……吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "心脏部分的设计\x01",
            "不是谁都能轻易胜任的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然这样的人不容易找，\x01",
            "不过也不能随便就让『埃尔赛尤号』\x01",
            "用替代引擎去飞行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼～在这点上说不定需要\x01",
            "大胆地转换思考的方向才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74C8")

    Jump("loc_76A6")

    label("loc_74CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_76A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_75A3")

    ChrTalk(
        0xFE,
        (
            "库莱泽他\x01",
            "为了养育年幼的弟弟，\x01",
            "已经决心留在卢安了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他本人其实应该\x01",
            "也很想在研究所工作的。\x01",
            "我们是不会怪他的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76A6")

    label("loc_75A3")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "呼，『埃尔赛尤号』\x01",
            "使用的新型导力引擎\x01",
            "在开发过程中遇上了点问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "卢安的库莱泽\x01",
            "本来是要和我们一起研究的，\x01",
            "最后竟然辞掉了这个工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样下去整个工程\x01",
            "就要陷入停滞状态了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76A6")

    TalkEnd(0xFE)
    Return()

    # Function_14_696D end

    def Function_15_76AA(): pass

    label("Function_15_76AA")

    EventBegin(0x0)
    OP_6D(1050, 0, 2760, 0)
    AddParty(0x6, 0xFF)
    SetChrPos(0x101, -200, 0, 1000, 0)
    SetChrPos(0x102, -1600, 0, 900, 0)
    SetChrSubChip(0x8, 2)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    SetChrFlags(0x107, 0x80)
    SetChrPos(0x107, -1100, 0, -1600, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#801F#3P哟，我正等着你们呢。\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，您好。\x01",
            "初次见面，工房长先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F在您百忙之中前来打扰。\x02",
    )

    CloseMessageWindow()

    def lambda_77D2():
        OP_6D(2680, 0, 4730, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_77D2)

    def lambda_77EA():
        OP_8E(0xFE, 0xA32, 0x0, 0xBEA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77EA)
    Sleep(500)

    def lambda_780A():
        OP_8E(0xFE, 0x6A4, 0x0, 0xBEA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_780A)
    WaitChrThread(0x101, 0x1)
    SetChrSubChip(0x8, 0)

    def lambda_782F():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_782F)
    WaitChrThread(0x102, 0x1)

    def lambda_7842():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7842)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x8,
        (
            "#800F哪里哪里，\x01",
            "都不用那么客气。\x02\x03",
            "因为我们以前\x01",
            "总是受到游击士协会……\x01",
            "特别是卡西乌斯先生的关照。\x02\x03",
            "他的孩子来了，\x01",
            "一定要好好欢迎才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎！？\x02\x03",
            "工房长先生\x01",
            "认识我们的老爸吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#803F哈哈，何止是认识，\x01",
            "卡西乌斯先生还是我的大恩人呢。\x02\x03",
            "#800F这个中央工房，\x01",
            "就算说是整个大陆上\x01",
            "导力技术最先进的地方也不为过。\x02\x03",
            "而这种技术带来的这样那样的麻烦\x01",
            "也是源源不绝啊。\x02\x03",
            "以前每到实在难以应付的时候，\x01",
            "我们就会联络洛连特支部，\x01",
            "请他过来帮忙解决。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，\x01",
            "怪不得父亲经常出差呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#801F没想到今天\x01",
            "恩人的孩子们特地前来拜访。\x02\x03",
            "务必让我一尽地主之宜哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嘿嘿……\x01",
            "谢谢，工房长先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F这件事说来话长……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们向工房长\x01",
            "详细地说明了迄今为止有关黑色导力器的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#800F原来如此，\x01",
            "竟然有这样的事啊……\x02\x03",
            "不介意的话，\x01",
            "可以让我看看那个导力器吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，当然可以了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔从行李中取出黑色导力器，\x01",
            "然后交给了玛多克工房长。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Fade(500)
    OP_22(0x82, 0x0, 0x64)
    SetChrPos(0x15, 2290, 800, 4650, 0)
    ClearChrFlags(0x15, 0x80)
    OP_0D()
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x8)

    ChrTalk(
        0x8,
        (
            "#802F唔……\x01",
            "的确是很奇妙的东西……\x02\x03",
            "很明显是最近才制造的，\x01",
            "不过奇怪的是……没有刻上序列号啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F序列号？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F就是刻在导力器外壳上的\x01",
            "生产序号吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F嗯，说得没错。\x02\x03",
            "不管是什么样的导力器，\x01",
            "都无一例外地刻有\x01",
            "表示产地及日期的生产序号。\x02\x03",
            "这一点不光是利贝尔，\x01",
            "在大陆的其他各国也是一样的。\x02\x03",
            "这是从五十年前刚发明导力器时\x01",
            "就保留下来的传统啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哦～是这样啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在一番好奇心之下，\x01",
            "艾丝蒂尔从怀里取出自己的战术导力器。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#004F……啊，真的。\x02\x03",
            "这上面也刻有号码呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F唉……\x01",
            "难道你以前都没发觉吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F要、要你啰嗦～\x02\x03",
            "#501F不过不过，\x01",
            "没有生产序号是那么奇怪的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#803F嗯，没错。\x01",
            "对导力技术者来说，\x01",
            "在产品上刻上序号是基本的常识。\x02\x03",
            "就算是试制品也是一样……\x02\x03",
            "#800F照此看来，制作这个东西的背后\x01",
            "很有可能藏有什么隐秘的目的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F隐秘的目的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F唔，更详细的情况\x01",
            "不调查其内部是弄不清楚的……\x02\x03",
            "#802F…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#805F奇怪了……\x01",
            "找不到可以打开的地方。\x02\x03",
            "仔细看连接缝都没有……\x01",
            "到底是怎么组装起来的呢？\x02\x03",
            "唔……\x01",
            "这样的话很难调查里面啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F哎～怎么会……\x02\x03",
            "#501F啊，要不这样吧。\x01",
            "把导力器的外壳切开不就好了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#805F唔……\x01",
            "这样的确是最简单方便的做法。\x02\x03",
            "但这是指名送给\x01",
            "卡西乌斯先生的东西，\x01",
            "随便破坏的话还是有点说不过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F这、这倒也是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F……………………………\x02\x03",
            "#015F如果那位博士在的话，\x01",
            "我想我们也许可以拜托他……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "一起寄来的便条……\x02\x03",
            "#006F的确，如果那位博士在的话，\x01",
            "说不定会有办法呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#802F？？？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#002F其实，和那个导力器一起送来的\x01",
            "还有这张便条……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔把寄给卡西乌斯的包裹里的便条交给工房长。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        "#802F『委托Ｒ博士调查………』\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F关于那个Ｒ博士，\x01",
            "不知道您有什么线索吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#802F线索嘛……\x02\x03",
            "首字母是Ｒ，\x01",
            "又是卡西乌斯先生认识的人，\x01",
            "那就一定是『拉赛尔博士』了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F果然是他吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F拉赛尔博士？\x02\x03",
            "这么说……\x01",
            "也是约修亚认识的人？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(400)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不，我没见过他。\x02\x03",
            "不过我知道他是一位\x01",
            "将导力技术带进利贝尔王国的名人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#800F哦，你也知道啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#803F导力器的发明者\x01",
            "是一位名叫爱普斯泰恩的博士……\x02\x03",
            "而拉赛尔博士就是\x01",
            "那位爱普斯泰恩博士的\x01",
            "嫡传弟子的其中一个。\x02\x03",
            "４０年前，\x01",
            "多亏他带回了导力器技术，\x01",
            "才让利贝尔成为了先进的导力技术王国。\x02\x03",
            "#800F因此，他可以称得上是\x01",
            "利贝尔的『导力革命之父』呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎哎……\x01",
            "是那么厉害的人啊。\x02\x03",
            "#007F老爸这家伙，\x01",
            "竟然有这么了不起的人际关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#803F但是，要把这个导力器交给博士……\x01",
            "真是让人有点担心啊。\x02\x03",
            "不知道会发生什么样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#805F怎么说呢……\x01",
            "他是个在好坏各方面都算得上天才的人。\x02\x03",
            "一旦燃起了研究之心，\x01",
            "就会经常引起各种各样的事。\x02\x03",
            "#806F对了，\x01",
            "导力飞艇刚开发出来的时候也是……\x02\x03",
            "#806F…………呼…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F（为、为什么在眺望远方……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F（看来以前发生过很多事……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#803F……咳咳，失礼了。\x02\x03",
            "#800F总之，如果是博士的话，\x01",
            "我想他应该能帮你们\x01",
            "查清这个黑色导力器的真面目。\x02\x03",
            "我帮你们引见一下，和他商量看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F谢谢，工房长先生！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那我们到哪里\x01",
            "才能见到拉赛尔博士呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F这个啊……\x01",
            "你们稍微等一下。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x8, 0)
    ClearChrFlags(0x8, 0x10)
    SetChrPos(0x8, 1720, 0, 5540, 270)
    OP_0D()
    OP_8C(0x8, 0, 400)
    OP_8E(0x8, 0x550, 0x0, 0x1C52, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "玛多克工房长拨通了内线电话。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#800F喂喂……\x01",
            "#802F哦，来得正好。\x02\x03",
            "其实我正要找你呢。\x02\x03",
            "不好意思，\x01",
            "能到我这里来一下吗？\x02\x03",
            "#801F嗯、嗯，我等着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F难道说，\x01",
            "刚才是和那位拉赛尔博士通话吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_8E(0x8, 0x6B8, 0x0, 0x15A4, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "#800F不不，当然不是。\x02\x03",
            "其实，\x01",
            "博士在城镇里有自己的工房。\x02\x03",
            "那里全是最新式的设备，\x01",
            "所以他一般都在那里做研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F哦～\x01",
            "真不愧是位天才博士啊。\x02\x03",
            "#505F……咦？\x01",
            "那么，刚才是和谁通话啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#801F啊，其实拉赛尔博士的孙女\x01",
            "也在中央工房工作哦。\x02\x03",
            "所以嘛，\x01",
            "我想拜托那孩子为你们带路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F那孩子？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x107,
        "女孩子的声音",
        "#1P打扰了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x6D, 0x0, 0x64)

    def lambda_8F3B():
        OP_6D(1170, 0, 3070, 2000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_8F3B)

    def lambda_8F53():

        label("loc_8F53")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_8F53")

    QueueWorkItem2(0x101, 1, lambda_8F53)

    def lambda_8F64():

        label("loc_8F64")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_8F64")

    QueueWorkItem2(0x102, 1, lambda_8F64)
    ClearChrFlags(0x107, 0x80)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8F85():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_8F85)
    OP_8E(0x107, 0xFFFFFCE0, 0x0, 0x4B0, 0xBB8, 0x0)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x101,
        "#004F#2P咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#2P你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064F咦咦……\x01",
            "艾丝蒂尔姐姐、约修亚哥哥？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8FFF():
        OP_6D(2680, 0, 4730, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8FFF)

    def lambda_9017():
        OP_8E(0xFE, 0x190, 0x0, 0xC62, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_9017)
    WaitChrThread(0x107, 0x2)
    TurnDirection(0x107, 0x101, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x8,
        (
            "#802F怎么怎么？\x01",
            "难道说你们认识吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P嗯。\x01",
            "刚认识不久呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P这么说，\x01",
            "她就是博士的孙女了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#800F嗯，正是。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#800F提妲。\x02\x03",
            "其实是这样的，\x01",
            "艾丝蒂尔他们有事想找博士商量。\x02\x03",
            "#800F能带他们去你家里吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(
        0x107,
        (
            "#560F去见爷爷吗……\x01",
            "嗯，好的，我知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#801F那就拜托你了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0x107, 0x101, 400)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#800F对了，有什么发现的话，\x01",
            "希望你们也能顺便告诉我一下。\x02\x03",
            "作为一个技术工作者，\x01",
            "我对这个可是非常感兴趣哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#001F啊哈哈，好的，我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们告辞了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x3F, 0x1, 0x4)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3114   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_15_76AA end

    def Function_16_9305(): pass

    label("Function_16_9305")

    EventBegin(0x0)
    OP_A2(0x54A)
    OP_64(0x0, 0x1)
    OP_2B(0x41, 0x1)
    OP_6D(-101920, 0, 93750, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9770")
    OP_A2(0x52F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93B6")

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "约修亚，这是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是刚才所说的发烟筒。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_952A")

    label("loc_93B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9446")

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "约修亚，那是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯。\x01",
            "是刚才所说的发烟筒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_952A")

    label("loc_9446")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94D0")

    ChrTalk(
        0x107,
        (
            "#065F啊……\x01",
            "哥哥，这是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是刚才所说的发烟筒。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_952A")

    label("loc_94D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_952A")

    ChrTalk(
        0x106,
        (
            "#057F这个……\x01",
            "就是那发烟筒吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F阿加特兄。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_952A")

    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚很熟练地把发烟筒拆散了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x102, -102470, 0, 94470, 135)
    SetChrPos(0x101, -102530, 0, 95560, 135)
    SetChrPos(0x107, -103610, 0, 94520, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_95B5")
    SetChrPos(0x106, -101550, 0, 95550, 225)

    label("loc_95B5")

    FadeToBright(600, 0)
    OP_82(0x1, 0x2)
    OP_82(0x0, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9696")

    ChrTalk(
        0x101,
        (
            "#501F哇……\x01",
            "烟雾没有了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F约修亚哥哥，\x01",
            "好厉害……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FＯＫ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_976D")

    label("loc_9696")

    OP_A2(0x53E)

    ChrTalk(
        0x101,
        (
            "#501F哇……\x01",
            "烟雾没有了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F约修亚哥哥，\x01",
            "好厉害……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#052F哦……\x01",
            "还挺有两下子的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_976D")

    Jump("loc_98A9")

    label("loc_9770")

    FadeToDark(600, 0, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚很熟练地把发烟筒拆散了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetChrPos(0x102, -102470, 0, 94470, 135)
    SetChrPos(0x101, -102530, 0, 95560, 135)
    SetChrPos(0x107, -103610, 0, 94520, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_9803")
    SetChrPos(0x106, -101550, 0, 95550, 225)

    label("loc_9803")

    OP_82(0x1, 0x2)
    OP_82(0x0, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98A9")
    OP_A2(0x53E)

    ChrTalk(
        0x106,
        (
            "#052F哦……\x01",
            "还挺有两下子的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98A9")

    EventEnd(0x0)
    Return()

    # Function_16_9305 end

    def Function_17_98AC(): pass

    label("Function_17_98AC")

    AddParty(0xF, 0xFF)
    EventBegin(0x0)
    OP_6D(2860, 0, 5340, 0)
    OP_6B(3200, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x9, 2360, 0, 2680, 0)
    SetChrPos(0x110, 4670, 0, 3000, 270)
    SetChrPos(0xA, 250, 0, 2990, 90)
    SetChrPos(0xB, 250, 0, 2040, 90)
    SetChrPos(0x102, -820, 0, 5490, 135)
    SetChrPos(0x101, -540, 0, 4290, 90)
    SetChrPos(0x106, 230, 0, 5620, 180)
    SetChrPos(0x107, -1830, 0, 4760, 90)

    def lambda_9968():

        label("loc_9968")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_9968")

    QueueWorkItem2(0x101, 1, lambda_9968)

    def lambda_9979():

        label("loc_9979")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_9979")

    QueueWorkItem2(0x102, 1, lambda_9979)

    def lambda_998A():

        label("loc_998A")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_998A")

    QueueWorkItem2(0x107, 1, lambda_998A)
    OP_A2(0x533)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#182F详细情况我明白了。\x02\x03",
            "不管怎么说，\x01",
            "那些人可真是明目张胆地犯罪啊。\x02\x03",
            "就算将这件事\x01",
            "称为恐怖袭击事件也毫不为过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#805F#1P恐怖袭击事件……\x01",
            "怎、怎么会有这种事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#181F用发烟筒制造混乱，\x01",
            "绑架了王国智慧象征的博士……\x02\x03",
            "而且还抢夺了\x01",
            "王国最新技术的导力演算器。\x02\x03",
            "所作所为不可原谅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F#1P说了那么多，\x01",
            "究竟王国军方面准备怎么行动？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#182F我们已经在艾尔·雷登、\x01",
            "沃尔费堡垒、佐达特军用道\x01",
            "以及圣海姆门等地实行严密的盘查。\x02\x03",
            "只要我们布下天罗地网，\x01",
            "绑架犯想逃出蔡斯地区也是空谈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎～\x01",
            "的确是很高明的方法啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#181F呵呵……\x01",
            "对突发事件做出迅速果断的应对\x01",
            "是我们情报部的基本职责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F有件事想请问一下……\x02\x03",
            "据说那些犯人换装成亲卫队队员，\x01",
            "并在大庭广众面前走出了中央工房。\x01",
            "请问您对这一点有何看法？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#182F那也是啊……\x01",
            "这可说是相当严重的事态。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x110, 400)

    ChrTalk(
        0x9,
        (
            "#181F这样的话……\x01",
            "朵洛希·海娅特小姐。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x110, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_9DF4():

        label("loc_9DF4")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_9DF4")

    QueueWorkItem2(0x110, 1, lambda_9DF4)

    ChrTalk(
        0x110,
        (
            "#153F#2P哎……？\x02\x03",
            "是、是叫我吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#182F听说案发的当时，\x01",
            "你拍到了逃走的绑架犯的样子是吧。\x02\x03",
            "这样说可能有点冒昧……\x01",
            "那个感光结晶回路可以交给我们保管吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#152F#2P咦！？\x02\x03",
            "但是但是，\x01",
            "这可是超级难得的独家报道～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#182F我并非打算包庇同僚，\x01",
            "毕竟王室亲卫队是王国军的荣耀。\x02\x03",
            "为了确保他们的清白，\x01",
            "更是为了顾全女王陛下的名誉，\x01",
            "在真相查明之前希望你们能做出客观的报道。\x02\x03",
            "#181F虽然是非正式的请求，\x01",
            "但这也是我们全体王国军的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#154F#2P唔～没办法了。\x02\x03",
            "等真相大白之后，\x01",
            "记得一定要还给我哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x110, 0xBA4, 0x0, 0xA6E, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "朵洛希把自己拍照专用的感光结晶回路\x01",
            "交给了凯诺娜上尉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x110, 0xDF2, 0x0, 0xB18, 0x7D0, 0x0)

    ChrTalk(
        0x9,
        "#182F谢谢你的合作。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)

    ChrTalk(
        0x9,
        (
            "#182F此外，虽然这样说有点失礼，\x01",
            "但为了军方的调查能顺利进展下去，\x01",
            "希望你们游击士协会也要限制一下行动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F#1P这个办不到。\x02\x03",
            "那些穿黑衣的家伙，\x01",
            "我可是从很久以前就开始追查了。\x02\x03",
            "不是不给军队面子，\x01",
            "只是我没理由在这时候撤手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#181F………………………………\x02\x03",
            "#182F唉，没办法。\x01",
            "那就请继续调查下去吧。\x02\x03",
            "我们军方和协会向来有合作关系。\x01",
            "总之，如果发现了什么，\x01",
            "请务必向雷斯顿要塞的情报部报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F#1P知道了。\x02\x03",
            "你们如果查到了什么，\x01",
            "也麻烦联络一下蔡斯支部。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#182F明白了。\x02\x03",
            "#181F那么我们就告辞了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x9, 0x40)
    OP_8C(0x9, 225, 400)

    def lambda_A460():

        label("loc_A460")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_A460")

    QueueWorkItem2(0xA, 1, lambda_A460)

    def lambda_A471():

        label("loc_A471")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_A471")

    QueueWorkItem2(0xB, 1, lambda_A471)

    def lambda_A482():
        OP_6D(640, 0, 1650, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A482)
    OP_8E(0x9, 0xFFFFFC2C, 0x0, 0x1EA, 0x7D0, 0x0)
    OP_43(0x9, 0x1, 0x0, 0x12)
    OP_43(0xA, 0x1, 0x0, 0x13)
    OP_43(0xB, 0x1, 0x0, 0x14)
    WaitChrThread(0xA, 0x1)
    OP_44(0x110, 0xFF)
    OP_44(0x106, 0xFF)
    OP_6D(190, 0, 5120, 1500)

    ChrTalk(
        0x101,
        (
            "#505F呼……\x01",
            "真、真是觉得好紧张啊。\x02\x03",
            "刚才那个女人是\x01",
            "理查德上校的副官凯诺娜上尉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3P嗯，没错。\x01",
            "应该是代替上校前来调查的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F哼……\x01",
            "我可是怎样都和当兵的合不来的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)

    ChrTalk(
        0x106,
        (
            "#050F算了，不管王国军如何做出行动，\x01",
            "总之那些黑衣人一定还\x01",
            "潜伏在蔡斯地区的某个地方。\x02\x03",
            "向协会报告之后，\x01",
            "我们就到城镇外面好好搜索吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A6B3():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A6B3)

    def lambda_A6C1():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A6C1)

    def lambda_A6CF():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A6CF)

    def lambda_A6DD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_A6DD)

    ChrTalk(
        0x101,
        (
            "#004F也好……等等。\x02\x03",
            "#009F你吃错药啦，\x01",
            "这次怎么不说要我们别跟去之类的话？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F啊啊。\x01",
            "你们看起来似乎还有点用处。\x02\x03",
            "就让你们做我的助手好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F看来你那种嚣张的性格是不会改的～\x02\x03",
            "#007F算了，已经习惯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那就请多指教了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#053F啊啊，可别大意了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(
        0x106,
        (
            "#050F工房长，\x01",
            "那么我们就出发了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 2)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#800F啊……拜托你们了。\x02\x03",
            "#803F无论如何……\x01",
            "请你们一定要救出博士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F…………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x8, 0)
    SetChrPos(0x101, -1150, 0, 2880, 180)
    SetChrPos(0x102, -1150, 0, 2880, 180)
    SetChrPos(0x107, -1150, 0, 2880, 180)
    SetChrPos(0x106, -1150, 0, 2880, 180)
    SetChrPos(0x110, -1150, 0, 2880, 180)
    OP_6D(-1150, 0, 2880, 0)
    OP_6B(3000, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_17_98AC end

    def Function_18_A96D(): pass

    label("Function_18_A96D")

    OP_8E(0xFE, 0xFFFFFC7C, 0x0, 0x12C, 0x7D0, 0x0)
    OP_22(0x6D, 0x0, 0x64)

    def lambda_A98C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A98C)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFC7C, 0x0, 0xFFFFF650, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_A96D end

    def Function_19_A9B7(): pass

    label("Function_19_A9B7")

    Sleep(300)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFFBD2, 0x0, 0xFFFFFEFC, 0x7D0, 0x0)

    def lambda_A9DB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A9DB)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFB3C, 0x0, 0xFFFFF650, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_22(0x6D, 0x0, 0x64)
    Return()

    # Function_19_A9B7 end

    def Function_20_AA0B(): pass

    label("Function_20_AA0B")

    Sleep(300)
    OP_8E(0xFE, 0xFFFFFBD2, 0x0, 0xFFFFFEFC, 0x7D0, 0x0)

    def lambda_AA2A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AA2A)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFB3C, 0x0, 0xFFFFF650, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_AA0B end

    def Function_21_AA55(): pass

    label("Function_21_AA55")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x356)"), scpexpr(EXPR_END)), "loc_AB0C")
    FadeToDark(300, 0, 100)
    OP_22(0x73, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "使用了\x07\x02",
            "里面房间的钥匙\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_71(0x0, 0x10)
    OP_64(0x1, 0x1)
    OP_3F(0x356, 1)
    OP_28(0x2C, 0x1, 0x8000)
    OP_65(0x6, 0x1)
    Jump("loc_AC13")

    label("loc_AB0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC13")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x13C,
        "喵呀～～呵。\x02",
    )

    CloseMessageWindow()

    def lambda_AB45():
        TurnDirection(0x102, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB45)

    def lambda_AB53():
        TurnDirection(0x107, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AB53)
    TurnDirection(0x101, 0x13C, 400)

    ChrTalk(
        0x101,
        "#002F……在这里面吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13C, 0x101, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x13C,
        "喵～噢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F找一下钥匙吧。\x02\x03",
            "应该就在这个房间里的某个地方。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F嗯，明白。\x02",
    )

    CloseMessageWindow()
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_28(0x2C, 0x1, 0x400)

    label("loc_AC13")

    TalkEnd(0xFF)
    Return()

    # Function_21_AA55 end

    def Function_22_AC17(): pass

    label("Function_22_AC17")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "调查了书架。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "没有找到什么特别的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_AC17 end

    def Function_23_ACC0(): pass

    label("Function_23_ACC0")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "调查了资料。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "没有找到什么特别的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_23_ACC0 end

    def Function_24_AD77(): pass

    label("Function_24_AD77")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "调查了笔筒。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "没有找到什么特别的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_AD77 end

    def Function_25_AE33(): pass

    label("Function_25_AE33")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "调查了桌子上的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "里面房间的钥匙\x07\x00",
            "找到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2C, 0x1, 0x800)
    OP_3E(0x356, 1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_25_AE33 end

    def Function_26_AEC2(): pass

    label("Function_26_AEC2")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(710, 0, 100700, 0)
    SetChrPos(0x101, 60, 0, 101680, 189)
    SetChrPos(0x102, 780, 0, 102660, 179)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF1B")
    SetChrPos(0x107, -600, 0, 102530, 168)

    label("loc_AF1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF3A")
    SetChrPos(0x106, 120, 0, 102990, 182)

    label("loc_AF3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF59")
    SetChrPos(0x13C, -1020, 0, 101070, 101)

    label("loc_AF59")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF73")

    def lambda_AF6B():
        TurnDirection(0x0, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_AF6B)

    label("loc_AF73")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF8D")

    def lambda_AF85():
        TurnDirection(0x1, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AF85)

    label("loc_AF8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFA7")

    def lambda_AF9F():
        TurnDirection(0x2, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AF9F)

    label("loc_AFA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFC1")

    def lambda_AFB9():
        TurnDirection(0x3, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_AFB9)

    label("loc_AFC1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFDB")

    def lambda_AFD3():
        TurnDirection(0x4, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_AFD3)

    label("loc_AFDB")

    OP_0D()
    Sleep(400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "烟草\x07\x00",
            "找到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        "#001F哈哈，找到了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#561F没想到犯人竟然是工房长先生……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        (
            "#003F嗯，预料之外呢～\x02\x03",
            "果真是人不可貌相……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x10)

    def lambda_B12D():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B12D)
    SetChrPos(0x8, -3380, 0, 98500, 0)

    ChrTalk(
        0x8,
        "你、你们几个！搞错了！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_B18B():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B18B)
    OP_8E(0x8, 0xFFFFF7B8, 0x0, 0x18D80, 0xFA0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1C5")

    def lambda_B1BD():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B1BD)

    label("loc_B1C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1DF")

    def lambda_B1D7():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B1D7)

    label("loc_B1DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1F9")

    def lambda_B1F1():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B1F1)

    label("loc_B1F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B213")

    def lambda_B20B():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B20B)

    label("loc_B213")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B22D")

    def lambda_B225():
        TurnDirection(0x4, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_B225)

    label("loc_B22D")

    TurnDirection(0x8, 0x101, 400)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#805F不、不要误会啊！\x02\x03",
            "就、就抽一支嘛，\x01",
            "马上就还回去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F工房长…………\x02\x03",
            "想要解释的话，\x01",
            "就请去找米妮亚姆医生吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_28(0x2C, 0x1, 0x1000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3118   ._SN", 100, 0, 0)
    IdleLoop()
    OP_64(0x6, 0x1)
    EventEnd(0x0)
    Return()

    # Function_26_AEC2 end

    def Function_27_B35C(): pass

    label("Function_27_B35C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放着《哈茨少年冒险记·上》。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B41C")
    OP_B9(0x374, 0x0)

    label("loc_B41C")

    TalkEnd(0xFF)
    Return()

    # Function_27_B35C end

    def Function_28_B420(): pass

    label("Function_28_B420")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放着《哈茨少年冒险记·下》。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4E1")
    OP_B9(0x344, 0x0)

    label("loc_B4E1")

    TalkEnd(0xFF)
    Return()

    # Function_28_B420 end

    def Function_29_B4E5(): pass

    label("Function_29_B4E5")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放着《结晶光学论集》。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5A6")
    OP_B9(0x342, 0x0)

    label("loc_B5A6")

    TalkEnd(0xFF)
    Return()

    # Function_29_B4E5 end

    def Function_30_B5AA(): pass

    label("Function_30_B5AA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放着《明日料理》。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B669")
    OP_B9(0x341, 0x0)

    label("loc_B669")

    TalkEnd(0xFF)
    Return()

    # Function_30_B5AA end

    def Function_31_B66D(): pass

    label("Function_31_B66D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放着《猫语日常会话入门》。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B730")
    OP_B9(0x340, 0x0)

    label("loc_B730")

    TalkEnd(0xFF)
    Return()

    # Function_31_B66D end

    def Function_32_B734(): pass

    label("Function_32_B734")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放着《艾尔贝啄木鸟的生态》。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7F4")
    OP_B9(0x343, 0x0)

    label("loc_B7F4")

    TalkEnd(0xFF)
    Return()

    # Function_32_B734 end

    def Function_33_B7F8(): pass

    label("Function_33_B7F8")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放着《３１棵丝柏树》。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8B5")
    OP_B9(0x345, 0x0)

    label("loc_B8B5")

    TalkEnd(0xFF)
    Return()

    # Function_33_B7F8 end

    SaveToFile()

Try(main)
