from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3200   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '毛婆婆',                             # 9
        '朵洛希',                               # 10
        '加雷利',                               # 11
        '拜舍尔',                               # 12
        '艾德',                                 # 13
        '林',                                   # 14
        '莉西亚',                               # 15
        '希利尔',                               # 16
        '艾缇',                                 # 17
        '拉克',                                 # 18
        '希玛',                                 # 19
        '库安',                                 # 20
        '西加罗',                               # 21
        '艾德尔',                               # 22
        '东方打扮的男人',                       # 23
        '托兰特平原道方向',                     # 24
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
        'ED6_DT07/CH02430 ._CH',             # 00
        'ED6_DT07/CH02070 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01460 ._CH',             # 03
        'ED6_DT07/CH01270 ._CH',             # 04
        'ED6_DT07/CH01030 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01120 ._CH',             # 07
        'ED6_DT07/CH01130 ._CH',             # 08
        'ED6_DT07/CH01160 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH01060 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH01210 ._CH',             # 0D
        'ED6_DT07/CH01153 ._CH',             # 0E
        'ED6_DT07/CH00070 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH02430P._CP',             # 00
        'ED6_DT07/CH02070P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01460P._CP',             # 03
        'ED6_DT07/CH01270P._CP',             # 04
        'ED6_DT07/CH01030P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01120P._CP',             # 07
        'ED6_DT07/CH01130P._CP',             # 08
        'ED6_DT07/CH01160P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH01060P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH01210P._CP',             # 0D
        'ED6_DT07/CH01153P._CP',             # 0E
        'ED6_DT07/CH00070P._CP',             # 0F
    )

    DeclNpc(
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        TalkScenaIndex      = 6,
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
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 13610,
        Z                   = 2500,
        Y                   = 16860,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -30790,
        Z                   = -2000,
        Y                   = 15330,
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
        X                   = 4000,
        Y                   = 0,
        Z                   = 18870,
        Range               = 7100,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x2D82,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = -13210,
        Y                   = -3000,
        Z                   = 9240,
        Range               = -19510,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x5BAE,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 28950,
        Y                   = 1000,
        Z                   = 4030,
        Range               = 2500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 980,
        Y                   = -250,
        Z                   = 18420,
        Range               = 1250,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 42330,
        Y                   = 5750,
        Z                   = 36020,
        Range               = 1250,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )


    DeclActor(
        TriggerX            = 43290,
        TriggerZ            = 6250,
        TriggerY            = 35890,
        TriggerRange        = 800,
        ActorX              = 43290,
        ActorZ              = 6500,
        ActorY              = 35890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 6000,
        TriggerY            = 49730,
        TriggerRange        = 800,
        ActorX              = 40000,
        ActorZ              = 7000,
        ActorY              = 49730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 42130,
        TriggerZ            = 0,
        TriggerY            = -860,
        TriggerRange        = 1250,
        ActorX              = 44880,
        ActorZ              = 3000,
        ActorY              = 1020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_436",          # 00, 0
        "Function_1_71D",          # 01, 1
        "Function_2_7EB",          # 02, 2
        "Function_3_968",          # 03, 3
        "Function_4_98C",          # 04, 4
        "Function_5_BEE",          # 05, 5
        "Function_6_D52",          # 06, 6
        "Function_7_E9A",          # 07, 7
        "Function_8_EA1",          # 08, 8
        "Function_9_EA8",          # 09, 9
        "Function_10_123E",        # 0A, 10
        "Function_11_1245",        # 0B, 11
        "Function_12_124C",        # 0C, 12
        "Function_13_15C3",        # 0D, 13
        "Function_14_15CA",        # 0E, 14
        "Function_15_18C2",        # 0F, 15
        "Function_16_1B02",        # 10, 16
        "Function_17_1B49",        # 11, 17
        "Function_18_1E6C",        # 12, 18
        "Function_19_1FA6",        # 13, 19
        "Function_20_2463",        # 14, 20
        "Function_21_2B3D",        # 15, 21
        "Function_22_2EB1",        # 16, 22
        "Function_23_2F01",        # 17, 23
        "Function_24_2FE5",        # 18, 24
        "Function_25_3086",        # 19, 25
        "Function_26_3130",        # 1A, 26
        "Function_27_31B1",        # 1B, 27
        "Function_28_31B5",        # 1C, 28
        "Function_29_31B9",        # 1D, 29
    )


    def Function_0_436(): pass

    label("Function_0_436")

    OP_A2(0x5D2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_447")
    OP_A3(0x3FA)
    Event(0, 20)

    label("loc_447")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_453"),
        (SWITCH_DEFAULT, "loc_469"),
    )


    label("loc_453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_466")
    OP_A2(0x51C)
    Event(0, 17)

    label("loc_466")

    Jump("loc_469")

    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_473")
    Jump("loc_4BE")

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_49A")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -450, 0, 12380, 180)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_4BE")

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4BE")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -450, 0, 12380, 180)
    OP_43(0xA, 0x0, 0x0, 0x3)

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_519")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 30590, 4500, 35260, 249)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 28630, 4000, 36530, 176)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 28800, 4000, 33220, 0)
    SetChrFlags(0x13, 0x10)
    Jump("loc_71C")

    label("loc_519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_565")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 11420, 2000, 14520, 273)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 9750, 2000, 15450, 181)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 9820, 2000, 13580, 351)
    Jump("loc_71C")

    label("loc_565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_5B6")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39080, 6000, 47390, 7)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 40560, 6000, 47840, 342)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 39640, 6000, 44670, 353)
    SetChrFlags(0xE, 0x10)
    Jump("loc_71C")

    label("loc_5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 2)), scpexpr(EXPR_END)), "loc_5C5")
    ClearChrFlags(0x16, 0x80)
    Jump("loc_71C")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_5CF")
    Jump("loc_71C")

    label("loc_5CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_5EF")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 49070, 2500, -2340, 12)
    Jump("loc_71C")

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_625")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17100, 2500, 20360, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39080, 6000, 47390, 7)
    Jump("loc_71C")

    label("loc_625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_671")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 13770, 2500, 18660, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 17040, 2500, 13580, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 15970, 2500, 13580, 45)
    Jump("loc_71C")

    label("loc_671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_6D3")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 14240, 2500, 16170, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 14200, 2500, 17020, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 15630, 2500, 13690, 45)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 17390, 2500, 13750, 0)
    Jump("loc_71C")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_71C")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 12180, 2000, 15020, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 9850, 2000, 13940, 45)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 10210, 2000, 16010, 135)

    label("loc_71C")

    Return()

    # Function_0_436 end

    def Function_1_71D(): pass

    label("Function_1_71D")

    OP_16(0x2, 0xFA0, 0xFFFE8130, 0xFFFE5E08, 0x30054)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_747")
    OP_B1("t3200_y")
    Jump("loc_750")

    label("loc_747")

    OP_B1("t3200_n")

    label("loc_750")

    OP_72(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_765")
    OP_72(0x3, 0x10)
    Jump("loc_769")

    label("loc_765")

    OP_64(0x0, 0x1)

    label("loc_769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_773")
    Jump("loc_7A7")

    label("loc_773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_782")
    OP_1B(0x0, 0x0, 0x19)
    Jump("loc_7A7")

    label("loc_782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_796")
    OP_1B(0x0, 0x0, 0x18)
    Jump("loc_7A7")

    label("loc_796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A7")
    OP_1B(0x0, 0x0, 0x17)

    label("loc_7A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BB")
    OP_28(0x2A, 0x1, 0x800)

    label("loc_7BB")

    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DB")
    OP_65(0x2, 0x1)

    label("loc_7DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EA")
    OP_82(0x8D, 0x0)

    label("loc_7EA")

    Return()

    # Function_1_71D end

    def Function_2_7EB(): pass

    label("Function_2_7EB")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_810")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_952")

    label("loc_810")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_829")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_952")

    label("loc_829")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_842")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_952")

    label("loc_842")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_952")

    label("loc_85B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_874")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_952")

    label("loc_874")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88D")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_952")

    label("loc_88D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A6")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_952")

    label("loc_8A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BF")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_952")

    label("loc_8BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D8")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_952")

    label("loc_8D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F1")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_952")

    label("loc_8F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_952")

    label("loc_90A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_923")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_952")

    label("loc_923")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_952")

    label("loc_93C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_952")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_952")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_967")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_952")

    label("loc_967")

    Return()

    # Function_2_7EB end

    def Function_3_968(): pass

    label("Function_3_968")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98B")
    OP_8D(0xFE, 2630, 16300, -3360, 10300, 3000)
    Jump("Function_3_968")

    label("loc_98B")

    Return()

    # Function_3_968 end

    def Function_4_98C(): pass

    label("Function_4_98C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_999")
    Jump("loc_BEA")

    label("loc_999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_9A3")
    Jump("loc_BEA")

    label("loc_9A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_9AD")
    Jump("loc_BEA")

    label("loc_9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_9B7")
    Jump("loc_BEA")

    label("loc_9B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_A07")

    ChrTalk(
        0xFE,
        (
            "月光映照下的\x01",
            "东方风格的庭园……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "简直就像梦幻一样啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEA")

    label("loc_A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_AB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_A5F")

    ChrTalk(
        0xFE,
        "唔～我想去后山看看啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "村子里都已经\x01",
            "没有可以去探险的地方了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0")

    label("loc_A5F")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "这里面的后山\x01",
            "好像有温泉的源头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我很想去看看，\x01",
            "但是村民不允许进去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB0")

    Jump("loc_BEA")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_ABD")
    Jump("loc_BEA")

    label("loc_ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_BE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_B3C")

    ChrTalk(
        0xFE,
        (
            "虽说好不容易来到这里，\x01",
            "想好好调养一路疲劳的身体……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我更想去买些特产，\x01",
            "好好地品尝一下东方料理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE0")

    label("loc_B3C")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "我丈夫把这当成是女神的试炼，\x01",
            "我才不这么想呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说好不容易来到这里，\x01",
            "想好好调养一路疲劳的身体……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我更想去买些特产，\x01",
            "好好地品尝一下东方料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE0")

    Jump("loc_BEA")

    label("loc_BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_BEA")

    label("loc_BEA")

    TalkEnd(0xFE)
    Return()

    # Function_4_98C end

    def Function_5_BEE(): pass

    label("Function_5_BEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_BFB")
    Jump("loc_D4E")

    label("loc_BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_C05")
    Jump("loc_D4E")

    label("loc_C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_C0F")
    Jump("loc_D4E")

    label("loc_C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_C19")
    Jump("loc_D4E")

    label("loc_C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_C23")
    Jump("loc_D4E")

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_C2D")
    Jump("loc_D4E")

    label("loc_C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_C68")

    ChrTalk(
        0xFE,
        "哎呀…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "艾德尔那家伙\x01",
            "到哪里去了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4E")

    label("loc_C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_CD5")

    ChrTalk(
        0xFE,
        (
            "水泵出故障了， \x01",
            "热水就抽不上来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然很遗憾， \x01",
            "但这说不定是女神给我们的试炼呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D44")

    label("loc_CD5")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        "唔，完全冷掉了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "泵坏掉了， \x01",
            "热水就抽不上来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然很遗憾， \x01",
            "但这也是女神给我们的试炼呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D44")

    Jump("loc_D4E")

    label("loc_D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D4E")

    label("loc_D4E")

    TalkEnd(0xFE)
    Return()

    # Function_5_BEE end

    def Function_6_D52(): pass

    label("Function_6_D52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_D5F")
    Jump("loc_E96")

    label("loc_D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_D69")
    Jump("loc_E96")

    label("loc_D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_D73")
    Jump("loc_E96")

    label("loc_D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_D7D")
    Jump("loc_E96")

    label("loc_D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_D87")
    Jump("loc_E96")

    label("loc_D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_E7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DE9")

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这口井……\x01",
            "大小正好适合做钓鱼池啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E78")

    label("loc_DE9")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "哎呀～太舒服了！\x01",
            "温泉最棒了！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "连身为钓公师团成员的我\x01",
            "都要把钓鱼的事情给忘掉了。\x01",
            "心情真好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "简直感觉\x01",
            "像心灵被清洗了一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E78")

    Jump("loc_E96")

    label("loc_E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_E85")
    Jump("loc_E96")

    label("loc_E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_E8F")
    Jump("loc_E96")

    label("loc_E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E96")

    label("loc_E96")

    TalkEnd(0xFE)
    Return()

    # Function_6_D52 end

    def Function_7_E9A(): pass

    label("Function_7_E9A")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_E9A end

    def Function_8_EA1(): pass

    label("Function_8_EA1")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_EA1 end

    def Function_9_EA8(): pass

    label("Function_9_EA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_F87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_F25")

    ChrTalk(
        0xFE,
        "啊，喂，库安。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你在刚才的战斗中\x01",
            "一直在用导力魔法，\x01",
            "那可不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "使用魔法\x01",
            "需要待机时间啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F84")

    label("loc_F25")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "还在玩武术大会游戏……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且是在大马路上，\x01",
            "不觉得害羞吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是个小鬼头。\x02",
    )

    CloseMessageWindow()

    label("loc_F84")

    Jump("loc_123A")

    label("loc_F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_106D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_FF7")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "在蔡斯发生大事的同时，\x01",
            "这边的水泵也出了故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不愧是解乏又温暖的\x01",
            "亚尔摩温泉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106A")

    label("loc_FF7")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "嗯，不愧是蔡斯啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "恐怖事件……\x01",
            "真是了不得的大新闻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "《利贝尔通讯》中\x01",
            "也会登载这个爆炸性新闻吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106A")

    Jump("loc_123A")

    label("loc_106D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1110")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10C6")

    ChrTalk(
        0xFE,
        (
            "好啦，拉克。\x01",
            "不能去栅栏那边啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要不然我又要\x01",
            "被毛婆婆骂了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_110D")

    label("loc_10C6")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "只是去后山而已，\x01",
            "有什么了不起的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们啊，\x01",
            "真是一群小鬼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_110D")

    Jump("loc_123A")

    label("loc_1110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_111A")
    Jump("loc_123A")

    label("loc_111A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1124")
    Jump("loc_123A")

    label("loc_1124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_112E")
    Jump("loc_123A")

    label("loc_112E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_1138")
    Jump("loc_123A")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1142")
    Jump("loc_123A")

    label("loc_1142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_123A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_11AA")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "蔡斯的人果然都很酷啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "该怎么说呢，\x01",
            "就像这样给人以干练的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123A")

    label("loc_11AA")

    OP_A2(0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D2")

    ChrTalk(
        0xFE,
        "哇，哥哥真帅呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11FC")

    label("loc_11D2")

    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "哇，\x01",
            "那边的哥哥看起来真帅呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FC")


    ChrTalk(
        0xFE,
        (
            "喂，喂？\x01",
            "你们是从蔡斯来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在那边\x01",
            "正流行什么啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123A")

    TalkEnd(0xFE)
    Return()

    # Function_9_EA8 end

    def Function_10_123E(): pass

    label("Function_10_123E")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_123E end

    def Function_11_1245(): pass

    label("Function_11_1245")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_1245 end

    def Function_12_124C(): pass

    label("Function_12_124C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_12DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_128F")

    ChrTalk(
        0xFE,
        (
            "上啊～！\x01",
            "看我的导力魔法！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "咚～～啪！\x02",
    )

    CloseMessageWindow()
    Jump("loc_12D9")

    label("loc_128F")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "喂，莉西亚姐姐。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xE, 400)

    ChrTalk(
        0xFE,
        (
            "你是裁判，\x01",
            "要好好看着才行哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 180, 0)

    label("loc_12D9")

    Jump("loc_15BF")

    label("loc_12DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_136A")

    ChrTalk(
        0xFE,
        (
            "嘿，你知道吗？\x01",
            "蔡斯出事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像是不得了的大事件。\x01",
            "这个村子里\x01",
            "也有游击士来调查了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "好想看看真正的游击士呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15BF")

    label("loc_136A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1428")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_13BB")

    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "真想去后山探险一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "村子里面\x01",
            "我都已经玩够了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1425")

    label("loc_13BB")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "温泉的源头\x01",
            "一定非常大吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "温泉水从那里\x01",
            "涌出了几十年，\x01",
            "也没有见它干涸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊～真想去看看。\x02",
    )

    CloseMessageWindow()

    label("loc_1425")

    Jump("loc_15BF")

    label("loc_1428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1432")
    Jump("loc_15BF")

    label("loc_1432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_143C")
    Jump("loc_15BF")

    label("loc_143C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_14E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1494")

    ChrTalk(
        0xFE,
        "唔～我想去后山看看啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "村子里都已经\x01",
            "没有可以去探险的地方了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E5")

    label("loc_1494")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "这里面的后山\x01",
            "好像有温泉的源头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我很想去看看，\x01",
            "但是村民不允许进去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E5")

    Jump("loc_15BF")

    label("loc_14E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_153D")

    ChrTalk(
        0xFE,
        (
            "我正在想温泉\x01",
            "为什么越来越凉了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在热水已经完全没有了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BF")

    label("loc_153D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_15BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1585")

    ChrTalk(
        0xFE,
        (
            "这么年轻\x01",
            "就来泡温泉啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "肯定是相当累了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BF")

    label("loc_1585")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "啊，有客人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎～真少见啊。\x01",
            "这么年轻的客人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BF")

    TalkEnd(0xFE)
    Return()

    # Function_12_124C end

    def Function_13_15C3(): pass

    label("Function_13_15C3")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_13_15C3 end

    def Function_14_15CA(): pass

    label("Function_14_15CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1658")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1619")

    ChrTalk(
        0xFE,
        (
            "可恶！不能认输！\x01",
            "我也发动魔法！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嘿呀呀呀呀～～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1655")

    label("loc_1619")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿～说起诞辰庆典，\x01",
            "果然还是武术大会最吸引人吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1655")

    Jump("loc_18BE")

    label("loc_1658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_16DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_16A4")

    ChrTalk(
        0xFE,
        "真是件大事啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然好像和我们村子\x01",
            "没什么关系。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D7")

    label("loc_16A4")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "蔡斯出了大事吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "城市里果然可怕啊。\x02",
    )

    CloseMessageWindow()

    label("loc_16D7")

    Jump("loc_18BE")

    label("loc_16DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_17E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_175C")

    ChrTalk(
        0xFE,
        (
            "……但是，\x01",
            "莉西亚姐姐也真是的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们都已经是大人了，\x01",
            "不要管我们那么多嘛。\x01",
            "有这时间倒不如去旅馆帮帮忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E0")

    label("loc_175C")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "后山的温泉源头吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我经常听说，\x01",
            "但是从来没有亲眼见过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "虽说不能越过这个栅栏，\x01",
            "但我还是很想去看看啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E0")

    Jump("loc_18BE")

    label("loc_17E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_17ED")
    Jump("loc_18BE")

    label("loc_17ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_17F7")
    Jump("loc_18BE")

    label("loc_17F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_1801")
    Jump("loc_18BE")

    label("loc_1801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1838")

    ChrTalk(
        0xFE,
        (
            "不冒热气的温泉\x01",
            "总觉得有点不习惯啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BE")

    label("loc_1838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_18BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_188E")

    ChrTalk(
        0xFE,
        "嘿嘿，拉克真是小鬼啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说到情侣，\x01",
            "果然要一起去温泉才浪漫。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BE")

    label("loc_188E")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，很浪漫啊。\x01",
            "情侣一起到温泉旅游。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BE")

    TalkEnd(0xFE)
    Return()

    # Function_14_15CA end

    def Function_15_18C2(): pass

    label("Function_15_18C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_19BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1935")

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "我还是很想亲眼看看\x01",
            "真正的东方文化啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来要委托游击士\x01",
            "护卫我到沃尔费堡垒了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B9")

    label("loc_1935")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "蔡斯好像发生了不得了的大事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实我想过\x01",
            "要不要去共和国旅游。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是发生了那种事件之后，\x01",
            "总觉得旅行不太安全。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B9")

    Jump("loc_1AFE")

    label("loc_19BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1AFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A64")

    ChrTalk(
        0xFE,
        (
            "这么说来，\x01",
            "在这里的途中……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我迷了路，\x01",
            "结果被一种身手敏捷的魔兽追赶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还想着死定了呢，\x01",
            "但它们只是不停地在闪光。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到底是什么呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_1A64")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "喔喔～很厉害的热气啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "建物的风格也很有意思……\x01",
            "嗯，呆在这里真是享受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "原来如此。\x01",
            "这就是东方风格吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我越来越想\x01",
            "去东方看看了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AFE")

    TalkEnd(0xFE)
    Return()

    # Function_15_18C2 end

    def Function_16_1B02(): pass

    label("Function_16_1B02")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#070F哦，真不错……\x02\x03",
            "赶快去泡个澡，\x01",
            "驱除一下旅途的劳累吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1B02 end

    def Function_17_1B49(): pass

    label("Function_17_1B49")

    EventBegin(0x0)
    OP_6D(17070, 6660, 16820, 0)
    OP_67(0, 3960, -10000, 0)
    OP_6B(4370, 0)
    OP_6C(39000, 0)
    SetChrPos(0x101, -17420, -2000, 15200, 90)
    SetChrPos(0x102, -18340, -2000, 16000, 90)
    SetChrPos(0x107, -18340, -2000, 14400, 90)
    FadeToBright(1000, 0)

    def lambda_1BC1():
        OP_6C(90000, 8500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1BC1)
    Sleep(4000)

    def lambda_1BD6():
        OP_6D(-16149, -2000, 14900, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BD6)

    def lambda_1BEE():
        OP_67(0, 9500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BEE)

    def lambda_1C06():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C06)
    Sleep(4500)

    ChrTalk(
        0x101,
        (
            "#501F#5P哎～这里就是亚尔摩村啊。\x01",
            "环境真的很不错呢。\x02\x03",
            "#505F不过……好像有什么怪味……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊～～\x01",
            "这是温泉里硫磺散发出来的气味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F有温泉涌出来的地方，\x01",
            "似乎大多都有这种气味吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x107, 400)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        (
            "#004F#5P哦～\x01",
            "好像烧糊的鸡蛋气味呢。\x02\x03",
            "#006F嗯，不过也不是特别难闻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F嘿嘿……那就好。\x02\x03",
            "#064F啊～不过不过，\x01",
            "今天的气味好像比平时淡了点……\x02\x03",
            "好像是热气没放出来的感觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我想大概就是因为\x01",
            "水泵发生了故障的缘故。\x02\x03",
            "我们现在就去修理吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x107,
        (
            "#060F嗯，好啊。\x01",
            "不过水泵小屋的钥匙\x01",
            "在旅馆的毛婆婆那里。\x02\x03",
            "得先去借钥匙才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5PＯＫ！\x01",
            "那就先去旅馆吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x40, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_17_1B49 end

    def Function_18_1E6C(): pass

    label("Function_18_1E6C")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA2")
    EventBegin(0x0)
    OP_A2(0x51E)
    OP_28(0x40, 0x1, 0x8)

    ChrTalk(
        0x101,
        "#501F啊，这里就是水泵小屋啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F嗯，是呢。\x02\x03",
            "这里可以把深山里的温泉\x01",
            "运送到旅馆和广场的井里哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，\x01",
            "用刚才的钥匙开门吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x73, 0x0, 0x64)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "使用水泵小屋的钥匙。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_71(0x3, 0x10)
    OP_64(0x0, 0x1)
    EventEnd(0x1)
    Jump("loc_1FA5")

    label("loc_1FA2")

    TalkEnd(0xFF)

    label("loc_1FA5")

    Return()

    # Function_18_1E6C end

    def Function_19_1FA6(): pass

    label("Function_19_1FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2462")
    OP_A2(0x523)
    OP_28(0x40, 0x1, 0x200)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_8C(0x101, 90, 400)
    OP_8C(0x102, 90, 400)
    OP_8C(0x110, 90, 400)

    ChrTalk(
        0x101,
        (
            "#501F啊……\x02\x03",
            "快看，温泉涌出来了呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        "#153F哇～真的！\x02",
    )

    CloseMessageWindow()

    def lambda_201B():
        OP_6D(15680, 2830, 16620, 2600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_201B)

    def lambda_2033():
        OP_6C(56000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2033)
    Sleep(2500)
    SetChrPos(0x101, 8210, 2000, 16740, 90)
    SetChrPos(0x102, 7680, 2000, 15580, 90)
    SetChrPos(0x110, 6840, 2000, 16430, 90)

    def lambda_207B():
        OP_8E(0xFE, 0x3520, 0x9C4, 0x424A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_207B)
    Sleep(300)

    def lambda_209B():
        OP_8E(0xFE, 0x3250, 0x9C4, 0x3E62, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_209B)
    Sleep(300)

    def lambda_20BB():
        OP_8F(0xFE, 0x30F2, 0x8CA, 0x44DE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_20BB)
    WaitChrThread(0x110, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F看来提妲那孩子\x01",
            "已经将导力泵顺利修好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#151F好棒～\x01",
            "这下总算可以泡温泉了。\x02\x03",
            "死而无憾了～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x110, 400)

    ChrTalk(
        0x101,
        "#506F#2P没那么夸张吧……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x110, 400)

    ChrTalk(
        0x102,
        (
            "#010F#2P朵洛希小姐你\x01",
            "那么喜欢泡温泉吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x110, 0x102, 400)

    ChrTalk(
        0x110,
        (
            "#150F嘿嘿，那当然啦。\x02\x03",
            "没有什么比泡好温泉后\x01",
            "喝杯水果牛奶更棒的事了。\x02\x03",
            "#151F那么～～\x01",
            "我就先去泡温泉了～！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2211():
        OP_6D(16100, 2000, 12100, 3600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2211)

    def lambda_2229():
        OP_6C(135000, 3600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2229)

    def lambda_2239():

        label("loc_2239")

        TurnDirection(0xFE, 0x110, 0)
        OP_48()
        Jump("loc_2239")

    QueueWorkItem2(0x101, 3, lambda_2239)

    def lambda_224A():

        label("loc_224A")

        TurnDirection(0xFE, 0x110, 0)
        OP_48()
        Jump("loc_224A")

    QueueWorkItem2(0x102, 3, lambda_224A)
    OP_8E(0x110, 0x2ABC, 0x7D0, 0x3DD6, 0xBB8, 0x0)
    OP_8E(0x110, 0x2C10, 0x7D0, 0x300C, 0xBB8, 0x0)
    OP_8E(0x110, 0x427C, 0x7D0, 0x2A26, 0xBB8, 0x0)
    OP_62(0x110, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x110,
        "#153F#2P啊，对了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x110, 0x101, 400)

    ChrTalk(
        0x110,
        (
            "#151F#2P小艾、小约。\x02\x03",
            "刚才真是谢谢了～！\x01",
            "在危难之中救了我。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_230E():
        OP_6D(14030, 2500, 16360, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_230E)

    def lambda_2326():
        OP_6C(90000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2326)
    OP_8C(0x110, 90, 400)
    OP_8E(0x110, 0x5A50, 0x7D0, 0xFFA, 0xBB8, 0x0)
    SetChrFlags(0x110, 0x80)
    SetChrPos(0x110, 13600, 2500, 16970, 0)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x3)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#007F#1P这个朵洛希……\x01",
            "现在才想起说这种客气话……\x02\x03",
            "#008F真受不了她，\x01",
            "做什么事都少根筋似的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F哈哈，这就是朵洛希的风格。\x02\x03",
            "#010F那么，\x01",
            "我们去水泵小屋看看吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F#1P啊，对呢。\x02\x03",
            "提妲那孩子\x01",
            "可能还留在那里呢。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    RemoveParty(0xF, 0xFF)

    label("loc_2462")

    Return()

    # Function_19_1FA6 end

    def Function_20_2463(): pass

    label("Function_20_2463")

    EventBegin(0x0)
    OP_6D(26330, 2000, 4950, 0)
    OP_6C(44000, 0)
    SetChrPos(0x101, 23790, 2000, 4370, 90)
    SetChrPos(0x102, 23900, 2000, 3160, 90)
    SetChrPos(0x107, 25060, 2000, 3830, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 27590, 2000, 3840, 270)
    OP_3F(0x369, 1)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#006F那么再见了，毛婆婆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F承蒙您的多方照顾。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#681F不用这么客气，\x01",
            "你们能玩得高兴我就很开心了。\x02\x03",
            "哈哈，\x01",
            "提妲也很高兴的样子嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F嘿嘿……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#680F看来昨天有开心的事情是吧。\x01",
            "我觉得你们三个已经像是兄妹那样了。\x02\x03",
            "#683F说起来……\x01",
            "怎么没看到那个带眼镜的姑娘呢。\x01",
            "那个傻丫头怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯……\x01",
            "她好像还在睡呢。\x02\x03",
            "怎么叫都叫不醒，\x01",
            "所以我们就没再去打扰她了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F朵洛希小姐起来的话，\x01",
            "请代我们向她问候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#680F好，知道了。\x02\x03",
            "提妲，\x01",
            "也麻烦你代为问候拉赛尔那家伙。\x02\x03",
            "叫他不要整天只顾着研究，\x01",
            "要多注意一下生活规律才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F呵呵，我会转告的。\x02\x03",
            "#061F婆婆您也要保重。\x01",
            "以后我还会再来玩的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#681F啊啊，我等着你过来。\x02\x03",
            "#680F你们俩也是，\x01",
            "有空的话记得多来这里玩哦。\x02\x03",
            "总之，想泡温泉的话就过来，\x01",
            "反正这里随时为你们准备着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#508F嗯！\x01",
            "一定会再来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F而且料理也很美味，\x01",
            "我们下次一定会再来品尝的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_8E(0x8, 0x73B4, 0x9C4, 0x1022, 0x7D0, 0x0)
    OP_70(0x4, 0x1D)
    OP_73(0x4)
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0x7C88, 0x9C4, 0xFBE, 0x7D0, 0x0)
    OP_72(0x4, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x4, 29)
    OP_70(0x4, 0x0)
    OP_73(0x4)
    OP_71(0x4, 0x800)

    def lambda_288B():
        OP_6D(24380, 2000, 3780, 1500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_288B)
    OP_8C(0x107, 270, 400)
    WaitChrThread(0x107, 0x1)

    ChrTalk(
        0x101,
        (
            "#001F这次任务可说是最轻松的了，\x01",
            "我呢，感觉整个人更加有干劲呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F没错。\x01",
            "这也是托修理水泵的福啊。\x02\x03",
            "真要多谢提妲了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F哪、哪儿的话，\x01",
            "其实我也没做什么啦。\x02\x03",
            "#066F倒是艾丝蒂尔姐姐你们辛苦了。\x01",
            "昨天特地护送我过来，真是谢谢呢。\x02\x03",
            "我……过得非常开心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嘿嘿～\x01",
            "能帮上忙我也很开心啊。\x02\x03",
            "#001F算是彼此彼此啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F嗯。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F那么接下来，\x01",
            "我们差不多该回蔡斯了吧。\x02\x03",
            "说不定我们回到工房的时候，\x01",
            "『黑色导力器』的解体也已经完成了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F啊，对了……\x01",
            "还有那么一回事呢。\x02\x03",
            "#506F哎呀～完全忘记了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F唉……\x01",
            "就知道你会这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F呵呵～\x01",
            "艾丝蒂尔姐姐真是的。\x02",
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
    OP_44(0x101, 0xFF)
    ClearMapFlags(0x10000000)
    EventEnd(0x0)
    Return()

    # Function_20_2463 end

    def Function_21_2B3D(): pass

    label("Function_21_2B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EB0")
    OP_A2(0x529)
    EventBegin(0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5790, 1000, 14450, 0)

    ChrTalk(
        0x9,
        "等一下～～！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)

    def lambda_2B86():
        OP_6C(45000, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2B86)
    SetChrFlags(0xA, 0x80)
    OP_6D(-11320, -2000, 15580, 0)
    SetChrPos(0x9, -2260, 0, 14820, 270)
    SetChrPos(0x101, -11140, -2000, 15290, 90)
    SetChrPos(0x102, -12050, -2000, 16190, 90)
    SetChrPos(0x107, -12260, -2000, 14680, 90)
    OP_0D()

    def lambda_2BF1():
        OP_8E(0xFE, 0xFFFFD99A, 0xFFFFF830, 0x3C50, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2BF1)
    WaitChrThread(0x9, 0x1)

    ChrTalk(
        0x101,
        (
            "#501F啊，朵洛希。\x01",
            "你总算起床了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#152F哈啊哈啊哈啊……\x01",
            "大、大家好过分呢～！\x02\x03",
            "竟然丢下我一个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F朵洛希小姐，\x01",
            "你不是说要拍报道用的照片，\x01",
            "所以还要留在村子里一段时间吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#153F咦，我有说过吗？\x02\x03",
            "#151F这个不重要啦～\x01",
            "你们不要把我排除在外嘛。\x02\x03",
            "小提也同意吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F小提……\x01",
            "是、是在叫我吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F你、你还叫得真随便啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#154F哎呀～\x01",
            "因为『小提妲』叫起来太拗口了嘛～\x02\x03",
            "不行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F不会啊，挺好的呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#151F谢谢，小提⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唉……\x01",
            "真不愧是我行我素的类型。\x02\x03",
            "#006F好了，闲话少说。\x01",
            "你就跟我们一起回蔡斯吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#150F嘿嘿，这样才对嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，\x01",
            "我们一起出发吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)

    def lambda_2E8D():
        OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2E8D)
    EventEnd(0x0)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearMapFlags(0x10000000)
    AddParty(0xF, 0xFF)

    label("loc_2EB0")

    Return()

    # Function_21_2B3D end

    def Function_22_2EB1(): pass

    label("Function_22_2EB1")

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
    TalkEnd(0xFF)
    Return()

    # Function_22_2EB1 end

    def Function_23_2F01(): pass

    label("Function_23_2F01")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F42")

    ChrTalk(
        0x107,
        (
            "#060F（这边是村口。\x01",
            "　赶快去水泵小屋吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC9")

    label("loc_2F42")

    TurnDirection(0x107, 0x0, 400)

    ChrTalk(
        0x107,
        (
            "#060F啊，那个……\x01",
            "再往前走就到平原上去了。\x01",
            "　\x02\x03",
            "水泵小屋在村子的另外一边哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2FA3():
        TurnDirection(0x102, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FA3)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        "#000F嗯，明白了～\x02",
    )

    CloseMessageWindow()

    label("loc_2FC9")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_23_2F01 end

    def Function_24_2FE5(): pass

    label("Function_24_2FE5")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F在修理好之前，\x01",
            "我们就在旅馆等着吧。\x02\x03",
            "那种情况，\x01",
            "我们也帮不上什么忙。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F是啊，\x01",
            "偶尔清闲一下也不错。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_24_2FE5 end

    def Function_25_3086(): pass

    label("Function_25_3086")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30C7")

    ChrTalk(
        0x102,
        (
            "#010F太阳快下山了……\x01",
            "村子外面会很危险的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3114")

    label("loc_30C7")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#014F太阳就快下山了，\x01",
            "村子外面会很危险的。\x02\x03",
            "我们还是不要出去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3114")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_25_3086 end

    def Function_26_3130(): pass

    label("Function_26_3130")

    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "发现了一个油纸包。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "里面放着\x07\x02",
            "艾尔贝啄木鸟的生态\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x343, 1)
    OP_64(0x2, 0x1)
    OP_28(0x2E, 0x1, 0x10)
    TalkEnd(0xFF)
    Return()

    # Function_26_3130 end

    def Function_27_31B1(): pass

    label("Function_27_31B1")

    SetPlaceName(0x88)
    Return()

    # Function_27_31B1 end

    def Function_28_31B5(): pass

    label("Function_28_31B5")

    SetPlaceName(0x87)
    Return()

    # Function_28_31B5 end

    def Function_29_31B9(): pass

    label("Function_29_31B9")

    SetPlaceName(0x89)
    Return()

    # Function_29_31B9 end

    SaveToFile()

Try(main)
