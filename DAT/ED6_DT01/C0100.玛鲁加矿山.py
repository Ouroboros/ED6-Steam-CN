from ED6ScenarioHelper import *

def main():
    # 玛鲁加矿山

    CreateScenaFile(
        FileName            = 'C0100   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0100.x',
        MapIndex            = 14,
        MapDefaultBGM       = "ed60030",
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
        '矿工迈尔德',                           # 9
        '矿工兰古',                             # 10
        '见习矿工',                             # 11
        '矿工彭兹',                             # 12
        '矿工提恩特',                           # 13
        '矿工皮尔姆',                           # 14
        '矿工海涅',                             # 15
        '加通老大',                             # 16
        '魔兽',                                 # 17
        '魔兽',                                 # 18
        '魔兽',                                 # 19
        '魔兽',                                 # 20
        '魔兽',                                 # 21
        '魔兽',                                 # 22
        '目标用摄像机',                         # 23
        '嗜杀巨蟹',                             # 24
        '嗜杀巨蟹',                             # 25
        '嗜杀巨蟹',                             # 26
        '嗜杀巨蟹',                             # 27
    )

    DeclEntryPoint(
        Unknown_00              = 25000,
        Unknown_04              = 0,
        Unknown_08              = 9000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 14,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 25000,
        Unknown_04              = 0,
        Unknown_08              = 9000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 14,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10000 ._CH',             # 00
        'ED6_DT09/CH10001 ._CH',             # 01
        'ED6_DT09/CH10050 ._CH',             # 02
        'ED6_DT09/CH10051 ._CH',             # 03
        'ED6_DT07/CH01500 ._CH',             # 04
        'ED6_DT07/CH01530 ._CH',             # 05
        'ED6_DT07/CH00100 ._CH',             # 06
        'ED6_DT07/CH00110 ._CH',             # 07
        'ED6_DT06/CH20034 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT09/CH10000P._CP',             # 00
        'ED6_DT09/CH10001P._CP',             # 01
        'ED6_DT09/CH10050P._CP',             # 02
        'ED6_DT09/CH10051P._CP',             # 03
        'ED6_DT07/CH01500P._CP',             # 04
        'ED6_DT07/CH01530P._CP',             # 05
        'ED6_DT07/CH00100P._CP',             # 06
        'ED6_DT07/CH00110P._CP',             # 07
        'ED6_DT06/CH20034P._CP',             # 08
    )

    DeclNpc(
        X                   = 22500,
        Z                   = 1000,
        Y                   = 65840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
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
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 96890,
        Z                   = 1000,
        Y                   = 91220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 130850,
        Z                   = 1000,
        Y                   = 13900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 126070,
        Z                   = 500,
        Y                   = 13270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 83580,
        Z                   = 1000,
        Y                   = 33130,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 83760,
        Z                   = 1000,
        Y                   = 31300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 84600,
        Z                   = 0,
        Y                   = 14100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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


    DeclMonster(
        X                   = 114000,
        Z                   = -500,
        Y                   = 80000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 129,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 108000,
        Z                   = 0,
        Y                   = 54000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 129,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x58,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 109000,
        Z                   = 0,
        Y                   = 35000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 129,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 105000,
        Z                   = 0,
        Y                   = 16000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 129,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x57,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 104400,
        Y                   = -1000,
        Z                   = 68900,
        Range               = 109400,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFF14,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = 92200,
        Y                   = -1000,
        Z                   = 63230,
        Range               = 4000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 90100,
        Y                   = -1000,
        Z                   = 72400,
        Range               = 97800,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x10F4A,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 123500,
        Y                   = -1000,
        Z                   = 27100,
        Range               = 132000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x7E2B,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 126240,
        Y                   = -1000,
        Z                   = 15000,
        Range               = 131400,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x2A94,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 92900,
        Y                   = -1000,
        Z                   = 33340,
        Range               = 97970,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x5762,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 84730,
        Y                   = 1000,
        Z                   = 31370,
        Range               = 88770,
        Unknown_10          = 0xFFFFFF9C,
        Unknown_14          = 0x8444,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )


    DeclActor(
        TriggerX            = 14000,
        TriggerZ            = 1000,
        TriggerY            = 31800,
        TriggerRange        = 1000,
        ActorX              = 14000,
        ActorZ              = 1000,
        ActorY              = 31800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 33,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16000,
        TriggerZ            = 1000,
        TriggerY            = 32000,
        TriggerRange        = 1500,
        ActorX              = 16000,
        ActorZ              = 1000,
        ActorY              = 32000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 35000,
        TriggerZ            = 1000,
        TriggerY            = 59500,
        TriggerRange        = 1500,
        ActorX              = 35000,
        ActorZ              = 1000,
        ActorY              = 59500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 31,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 50500,
        TriggerZ            = 1000,
        TriggerY            = 50000,
        TriggerRange        = 1500,
        ActorX              = 50500,
        ActorZ              = 1000,
        ActorY              = 50000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 54000,
        TriggerZ            = 500,
        TriggerY            = 58200,
        TriggerRange        = 600,
        ActorX              = 54000,
        ActorZ              = 500,
        ActorY              = 58200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 129000,
        TriggerZ            = 500,
        TriggerY            = 78200,
        TriggerRange        = 600,
        ActorX              = 129000,
        ActorZ              = 500,
        ActorY              = 78200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 104800,
        TriggerZ            = 0,
        TriggerY            = 39740,
        TriggerRange        = 1000,
        ActorX              = 104800,
        ActorZ              = 1000,
        ActorY              = 39740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_562",          # 00, 0
        "Function_1_629",          # 01, 1
        "Function_2_710",          # 02, 2
        "Function_3_88D",          # 03, 3
        "Function_4_88E",          # 04, 4
        "Function_5_99C",          # 05, 5
        "Function_6_C8F",          # 06, 6
        "Function_7_E8F",          # 07, 7
        "Function_8_11AC",         # 08, 8
        "Function_9_145A",         # 09, 9
        "Function_10_2AC3",        # 0A, 10
        "Function_11_2B46",        # 0B, 11
        "Function_12_2B58",        # 0C, 12
        "Function_13_2B62",        # 0D, 13
        "Function_14_2F7A",        # 0E, 14
        "Function_15_3ADF",        # 0F, 15
        "Function_16_4114",        # 10, 16
        "Function_17_429D",        # 11, 17
        "Function_18_47DE",        # 12, 18
        "Function_19_47F0",        # 13, 19
        "Function_20_49ED",        # 14, 20
        "Function_21_4A10",        # 15, 21
        "Function_22_4B81",        # 16, 22
        "Function_23_4E80",        # 17, 23
        "Function_24_4EBD",        # 18, 24
        "Function_25_4FF6",        # 19, 25
        "Function_26_53F5",        # 1A, 26
        "Function_27_541E",        # 1B, 27
        "Function_28_5C6A",        # 1C, 28
        "Function_29_5C80",        # 1D, 29
        "Function_30_6593",        # 1E, 30
        "Function_31_6847",        # 1F, 31
        "Function_32_69B1",        # 20, 32
        "Function_33_6B14",        # 21, 33
        "Function_34_6B5F",        # 22, 34
    )


    def Function_0_562(): pass

    label("Function_0_562")

    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_594"),
        (100, "loc_59B"),
        (101, "loc_59E"),
        (SWITCH_DEFAULT, "loc_5A1"),
    )


    label("loc_594")

    Event(0, 15)
    Jump("loc_5A1")

    label("loc_59B")

    Jump("loc_5A1")

    label("loc_59E")

    Jump("loc_5A1")

    label("loc_5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_5FD")
    SetChrPos(0xF, 14160, 0, 12750, 225)
    SetChrPos(0xB, 39350, 0, 26280, 0)
    SetChrPos(0xC, 24110, -40, 15950, 0)
    SetChrPos(0xD, 10800, 0, 29530, 0)
    SetChrPos(0xE, 54240, 0, 53990, 0)

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_60E")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)

    label("loc_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_61F")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)

    label("loc_61F")

    OP_A2(0x6)
    OP_A3(0x7)
    OP_A3(0x8)
    Return()

    # Function_0_562 end

    def Function_1_629(): pass

    label("Function_1_629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_63A")
    OP_6F(0x0, 0)
    Jump("loc_659")

    label("loc_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_64B")
    OP_6F(0x0, 330)
    Jump("loc_659")

    label("loc_64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_659")
    OP_6F(0x0, 900)

    label("loc_659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_66A")
    OP_6F(0x3, 25)
    Jump("loc_671")

    label("loc_66A")

    OP_6F(0x3, 0)

    label("loc_671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C6")
    LoadEffect(0x0, "map\\\\mp002_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 95730, 0, 78730, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 1000)

    label("loc_6C6")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 104880, 1000, 39790, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_629 end

    def Function_2_710(): pass

    label("Function_2_710")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_735")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_877")

    label("loc_735")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_877")

    label("loc_74E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_767")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_877")

    label("loc_767")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_780")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_877")

    label("loc_780")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_799")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_877")

    label("loc_799")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B2")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_877")

    label("loc_7B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CB")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_877")

    label("loc_7CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E4")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_877")

    label("loc_7E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FD")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_877")

    label("loc_7FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_816")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_877")

    label("loc_816")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_877")

    label("loc_82F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_848")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_877")

    label("loc_848")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_861")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_877")

    label("loc_861")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_877")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_877")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_877")

    label("loc_88C")

    Return()

    # Function_2_710 end

    def Function_3_88D(): pass

    label("Function_3_88D")

    Return()

    # Function_3_88D end

    def Function_4_88E(): pass

    label("Function_4_88E")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_933")
    OP_A2(0x5)

    ChrTalk(
        0xA,
        "哇！吓我一跳～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "哦，找我们老大呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我想老大应该在\x01",
            "过桥后更里面的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_998")

    label("loc_933")


    ChrTalk(
        0xA,
        "哦，找我们老大呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我想老大应该在\x01",
            "过桥后更里面的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_998")

    TalkEnd(0xA)
    Return()

    # Function_4_88E end

    def Function_5_99C(): pass

    label("Function_5_99C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A24")

    ChrTalk(
        0xB,
        (
            "我们把魔兽的巢穴\x01",
            "用炸药来堵住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "这下又能够继续工作，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_A9B")

    ChrTalk(
        0xB,
        "提恩特那家伙又不在……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "准是又翘班了，\x01",
            "溜到洛连特那里吃东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_B74")

    ChrTalk(
        0xB,
        (
            "老大已经很久\x01",
            "没回家好好休息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "家人肯定在等着他回去吧。\x01",
            "应该不要紧吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_BF5")

    ChrTalk(
        0xB,
        (
            "我们暂时不能往下挖掘了，\x01",
            "这里的工作也要暂停了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_BF5")


    ChrTalk(
        0xB,
        (
            "提恩特那家伙\x01",
            "好像又旷工翘班了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "明明之前\x01",
            "老大已经对他发过火了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8B")

    TalkEnd(0xB)
    Return()

    # Function_5_99C end

    def Function_6_C8F(): pass

    label("Function_6_C8F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_CC4")

    ChrTalk(
        0xC,
        "我本来应该在洛连特的哦～\x02",
    )

    CloseMessageWindow()
    Jump("loc_E8B")

    label("loc_CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_CF6")

    ChrTalk(
        0xC,
        "我本来应该在洛连特的哦～\x02",
    )

    CloseMessageWindow()
    Jump("loc_E8B")

    label("loc_CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_D7D")

    ChrTalk(
        0xC,
        (
            "哈～好饿啊，\x01",
            "已经达到极限了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "搞定这些活儿，\x01",
            "我就去好好吃一顿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8B")

    label("loc_D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_E0A")

    ChrTalk(
        0xC,
        "啊～好倒霉呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "这下我的肚子\x01",
            "真的是饿扁了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8B")

    label("loc_E0A")


    ChrTalk(
        0xC,
        (
            "唔，明明吃了很多了，\x01",
            "可一会儿又开始饿了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "再旷一会儿工，\x01",
            "到城里去吃些东西吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8B")

    TalkEnd(0xC)
    Return()

    # Function_6_C8F end

    def Function_7_E8F(): pass

    label("Function_7_E8F")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_F52")

    ChrTalk(
        0xD,
        (
            "呼呼，工作告一段落，\x01",
            "要去教会祈祷一下才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "因为最近忙于工作，\x01",
            "好久都没有去礼拜堂祈祷了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A8")

    label("loc_F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_FBF")

    ChrTalk(
        0xD,
        (
            "老大果然打算用炸药\x01",
            "来封住魔兽的巢穴啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A8")

    label("loc_FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_107D")

    ChrTalk(
        0xD,
        (
            "崩塌之前我们\x01",
            "在新的矿脉挖了很多东西，\x01",
            "虽说现在矿山还有不少的储备……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不过不早点到下层\x01",
            "看看情况的话，\x01",
            "说不定那些挖出来的东西都没有了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A8")

    label("loc_107D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_111B")

    ChrTalk(
        0xD,
        (
            "呼，\x01",
            "我刚才还以为死定了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "回到镇里后一定\x01",
            "要去礼拜堂向女神作祷告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A8")

    label("loc_111B")


    ChrTalk(
        0xD,
        (
            "因为，\x01",
            "我们能这么顺利地作业，\x01",
            "也是受到女神的指引的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "要感谢女神呀。\x02",
    )

    CloseMessageWindow()

    label("loc_11A8")

    TalkEnd(0xD)
    Return()

    # Function_7_E8F end

    def Function_8_11AC(): pass

    label("Function_8_11AC")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_123A")

    ChrTalk(
        0xE,
        "导力梯已经不能再用了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "虽然魔兽已经没有什么动静了，\x01",
            "不过为了安全起见，\x01",
            "还是要先看看情况才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1456")

    label("loc_123A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_12EC")

    ChrTalk(
        0xE,
        "巢穴被堵起来的话就好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "必须得找人\x01",
            "到下面一层去看看才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "让谁去做这样的事情好呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1456")

    label("loc_12EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_1387")

    ChrTalk(
        0xE,
        "下层还有魔兽在啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "得早点把它们收拾掉，\x01",
            "或者把它们封锁起来才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1456")

    label("loc_1387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_140B")

    ChrTalk(
        0xE,
        "下面的楼层已经暂时被封锁了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "因为魔兽很危险呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1456")

    label("loc_140B")


    ChrTalk(
        0xE,
        (
            "在找老大吗？\x01",
            "他刚刚还在这里的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1456")

    TalkEnd(0xE)
    Return()

    # Function_8_11AC end

    def Function_9_145A(): pass

    label("Function_9_145A")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_148E")

    ChrTalk(
        0xF,
        "现在应该在洛连特自己家里吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ABF")

    label("loc_148E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_152C")

    ChrTalk(
        0xF,
        (
            "现在也唯有\x01",
            "将魔兽的巢穴埋掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "这并不是说放弃新矿脉。\x01",
            "这次给游击士添了很多麻烦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ABF")

    label("loc_152C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_15BC")

    ChrTalk(
        0xF,
        (
            "崩塌的时候\x01",
            "逃出来的新矿工\x01",
            "好像再也没有回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "毕竟一来就遇到那样的事情。\x01",
            "虽然有点遗憾，不过也不能勉强别人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ABF")

    label("loc_15BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_1652")

    ChrTalk(
        0xF,
        (
            "这次真是不好意思。\x01",
            "给你们添了这么多的麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "不过真奇怪，\x01",
            "那里的岩盘不应该\x01",
            "那么脆弱的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ABF")

    label("loc_1652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ABF")
    OP_A2(0x242)
    OP_28(0x3, 0x1, 0x40)
    OP_28(0x3, 0x1, 0x80)
    ClearMapFlags(0x1)
    Fade(1000)
    EventBegin(0x0)
    AddParty(0x32, 0xFF)
    SetChrFlags(0x133, 0x80)
    SetChrPos(0x102, 85400, 0, 12650, 0)
    SetChrPos(0x101, 84250, 0, 12500, 0)
    OP_6C(315000, 0)
    TurnDirection(0xF, 0x101, 0)
    SetChrSubChip(0xF, 0)
    OP_6D(84460, 0, 13210, 1000)
    OP_0D()

    ChrTalk(
        0xF,
        "哎？小姑娘你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F叔叔你就是矿长先生吗？\x01",
            "太好了，终于找到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是游击士协会的人，\x01",
            "受克劳斯市长委托而来的。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "把\x07\x02",
            "市长的介绍信\x07\x00",
            "交给了加通矿长。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x321, 1)

    ChrTalk(
        0xF,
        (
            "哦，原来如此。\x01",
            "你们是游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "小小年纪就当游击士可真了不起啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嘿嘿，过奖了。\x02\x03",
            "#006F对了……结晶在什么地方？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "啊，稍等一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "这毕竟是不能\x01",
            "随便给别人看见的贵重物品嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "还是贴身保管比较安全。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "矿长从怀中取出大颗的结晶。\x07\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x80, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0xF, 0, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    CloseMessageWindow()
    Sleep(1500)

    ChrTalk(
        0x101,
        "#004F哇～……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#001F这么大的结晶，以前都没见过呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F好厉害……\x01",
            "像是从深处发出光芒一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "这个就是七耀石的其中一种，\x01",
            "蕴含着风之力量的翠耀石结晶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "这么大块的结晶，\x01",
            "作为宝石来讲有着很高的价值。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "你们一定要安全地送到市长那里。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯、嗯……\x02",
    )

    CloseMessageWindow()
    OP_92(0xF, 0x101, 0x3E8, 0x3E8, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrChipByIndex(0x101, 8)
    OP_82(0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x101, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "七耀石的结晶\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x323, 1)
    OP_8F(0xF, 0x14A78, 0x0, 0x3714, 0x3E8, 0x0)
    OP_6D(84250, -500, 12500, 1000)

    ChrTalk(
        0x101,
        (
            "#008F哇～……真漂亮……\x02\x03",
            "感觉就像捧着妖精一样……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_69(0x101, 0x3E8)
    OP_6A(0x101)
    SetMapFlags(0x1)
    OP_97(0x101, 0x1491A, 0x29FE, 0xFFFF15A0, 0x7D0, 0x1)

    def lambda_1DF7():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DF7)
    OP_97(0x101, 0x1491A, 0x29FE, 0xFFFF8AD0, 0xBB8, 0x1)
    OP_97(0x101, 0x1462C, 0x29FE, 0xFFFA81C0, 0xFA0, 0x1)
    OP_A2(0x2)
    OP_43(0x101, 0x1, 0x0, 0xA)

    ChrTalk(
        0x101,
        (
            "#001F啊哈，真有趣～！\x02\x03",
            "#001F快看快看，约修亚！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_6A(0x0)
    ClearMapFlags(0x1)
    OP_6D(84000, 0, 13440, 2000)

    ChrTalk(
        0x102,
        (
            "#015F确实很漂亮……\x02\x03",
            "#010F我劝你还是赶快停下来比较好。\x01",
            "万一弄掉了就糟了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x2)
    OP_A6(0x1)

    ChrTalk(
        0x101,
        (
            "#007F啧。\x01",
            "真没劲……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x1491A, 0x0, 0x30D4, 0x5DC, 0x0)
    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x102, 0x101, 0)
    Sleep(1000)
    OP_82(0x0, 0x2)
    SetChrChipByIndex(0x101, 65535)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔把结晶收在怀里。\x07\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#006F这样就行了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF, 400)

    ChrTalk(
        0x101,
        (
            "#006F那么，老大叔叔，\x01",
            "我们会把它安全地送到市长那里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "哦，拜托你们了。\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1100)
    OP_8C(0xF, 135, 400)

    ChrTalk(
        0xF,
        "嗯……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "……奇怪了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "空气的流向好像有点不对劲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F空气的流向……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F（这种感觉是……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_43(0x101, 0x1, 0x0, 0xD)
    OP_22(0x85, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        "哇！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#504F呀啊～！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 180, 400)
    OP_8C(0x101, 315, 400)
    OP_8C(0x101, 45, 400)
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x102,
        "#012F……………………\x02",
    )

    CloseMessageWindow()
    OP_A3(0x3)
    OP_24(0x85, 0x5A)
    Sleep(200)
    OP_24(0x85, 0x50)
    Sleep(200)
    OP_24(0x85, 0x46)
    Sleep(200)
    OP_24(0x85, 0x3C)
    Sleep(200)
    OP_24(0x85, 0x32)
    Sleep(200)
    OP_24(0x85, 0x28)
    Sleep(200)
    OP_24(0x85, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x14)
    Sleep(200)
    OP_24(0x85, 0xA)
    Sleep(200)
    OP_23(0x85)
    Sleep(200)
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        (
            "#007F好、好像停下来了……\x02\x03",
            "#002F刚才不会是地震吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(
        0xF,
        (
            "不是……\x01",
            "应该是坑道哪里发生了崩塌吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "是地基松软的地方受到了冲击吗？\x01",
            "不赶快到现场确认情况的话……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x10, 92200, 0, 10100, 0)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x102, 7)
    OP_8C(0x102, 135, 800)

    ChrTalk(
        0x102,
        "#016F艾丝蒂尔，小心！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 800)

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 6)

    def lambda_23FF():
        OP_6D(91250, 0, 7500, 2600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23FF)

    def lambda_2417():
        OP_6B(2000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2417)
    OP_8E(0x10, 0x158EC, 0x0, 0x2904, 0x1B58, 0x0)
    OP_92(0x10, 0x101, 0x7D0, 0x2710, 0x0)
    OP_44(0x101, 0xFF)
    Battle(0x384, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2460"),
        (SWITCH_DEFAULT, "loc_2465"),
    )


    label("loc_2460")

    OP_B4(0x0)
    Jump("loc_2465")

    label("loc_2465")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrFlags(0x10, 0x80)
    OP_6B(2800, 0)
    OP_6D(84460, 0, 13210, 0)
    SetChrPos(0x101, 85400, 0, 12650, 0)
    SetChrPos(0x102, 86100, -500, 13380, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0xF, 0x101, 0)
    TurnDirection(0x101, 0xF, 0)
    TurnDirection(0x102, 0xF, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#580F为、为什么会有魔兽……\x02\x03",
            "矿长叔叔，这里也会出现魔兽吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "在这么深的地方出现还是头一次！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "魔兽对七耀石的光芒非常敏感，\x01",
            "被吸引过来也不奇怪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "以前也曾有一些魔兽闯进来，\x01",
            "不过都只徘徊在入口附近……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F难道说……\x02\x03",
            "刚才的崩塌，\x01",
            "把坑道的一部分和魔兽的巢穴连在了一起？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#005F魔、魔兽的巢穴～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "不能排除这种可能性……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "这、这下糟了。\x01",
            "要赶快通知弟兄们逃出去才行啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF, 400)

    ChrTalk(
        0x101,
        (
            "#002F这种事情就交给我们吧！\x01",
            "我们也来帮忙！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F打倒魔兽对我们来说只是小事一桩。\x01",
            "现在要分秒必争，就别考虑那么多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "抱歉……就拜托你们帮忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F顺便问一下，\x01",
            "这里的矿工一共有多少人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "在地下工作的……\x01",
            "应该是四个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F明白了，赶快去救他们吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "麻烦你们了……\x01",
            "啊，对了，必要的时候用这东西吧。\x02",
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
            "得到了２个\x07\x02",
            "回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x1F5, 2)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    LoadEffect(0x0, "map\\\\mp002_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 95730, 0, 78730, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x11, 85530, 1000, 32350, 270)
    SetChrPos(0x12, 128360, 1000, 12900, 180)
    SetChrPos(0x13, 92200, 0, 63230, 225)
    SetChrPos(0x14, 92600, 0, 62100, 270)
    SetChrPos(0x15, 90800, 0, 63630, 180)
    OP_8C(0xA, 225, 0)
    OP_8C(0xB, 225, 0)
    OP_8C(0xD, 225, 0)
    OP_8C(0xD, 90, 0)
    OP_8C(0xE, 90, 0)
    SetChrFlags(0xF, 0x40)

    def lambda_2A9F():
        OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2A9F)
    EventEnd(0x0)
    ClearChrFlags(0x133, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)

    label("loc_2ABF")

    TalkEnd(0xF)
    Return()

    # Function_9_145A end

    def Function_10_2AC3(): pass

    label("Function_10_2AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2AE2")
    OP_97(0x101, 0x1462C, 0x29FE, 0xFFFEA070, 0xFA0, 0x1)
    Jump("Function_10_2AC3")

    label("loc_2AE2")

    OP_97(0x101, 0x1462C, 0x29FE, 0xFFFEA070, 0xFA0, 0x1)
    OP_97(0x101, 0x1462C, 0x29FE, 0xFFFEC780, 0xBB8, 0x1)
    OP_97(0x101, 0x1462C, 0x29FE, 0xFFFEEE90, 0x7D0, 0x1)
    OP_97(0x101, 0x1462C, 0x29FE, 0xFFFF8AD0, 0x3E8, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)
    OP_A2(0x1)
    Return()

    # Function_10_2AC3 end

    def Function_11_2B46(): pass

    label("Function_11_2B46")

    OP_6D(91250, 0, 7500, 2600)
    Return()

    # Function_11_2B46 end

    def Function_12_2B58(): pass

    label("Function_12_2B58")

    OP_6B(200, 1500)
    Return()

    # Function_12_2B58 end

    def Function_13_2B62(): pass

    label("Function_13_2B62")

    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)

    label("loc_2C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2C5A")
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 400, 13440, 20)
    Jump("loc_2C2E")

    label("loc_2C5A")

    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    Return()

    # Function_13_2B62 end

    def Function_14_2F7A(): pass

    label("Function_14_2F7A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_308A")

    ChrTalk(
        0x8,
        (
            "老大自己到下层去\x01",
            "用炸药把魔兽的巢穴给封住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们即使跟着他也不能帮上什么，\x01",
            "说不定还会帮倒忙啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不愧是加通老大啊。\x01",
            "再也没有比他更有男子气概的矿工了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_308A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_3118")

    ChrTalk(
        0x8,
        "呼呼，这里也已经采掘完了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "希望下层的作业能早点重开。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_3118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_31D9")

    ChrTalk(
        0x8,
        (
            "好不容易找到了新的矿脉，\x01",
            "没想到还没有挖了多久就崩塌了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "希望能早点\x01",
            "回到下层去作业就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_31D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_3261")

    ChrTalk(
        0x8,
        (
            "我听到脚下有地响的时候\x01",
            "可真是吓了一跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "老大和大家都没事，\x01",
            "实在是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_3261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377A")
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    OP_A2(0x23E)

    ChrTalk(
        0x8,
        (
            "呀？你们……\x01",
            "为什么会在这里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "是哪个矿工的熟人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不是呢。我们是受市长的委托，\x01",
            "来这儿找矿长的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊，是为了结晶的事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "矿长应该在地下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "另一边尽头处有一部导力梯，\x01",
            "可以通到地下去的。\x01",
            "你们自己坐矿车到导力梯那里吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A7")

    ChrTalk(
        0x101,
        "#004F另一边的尽头？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们乘矿车过来的时候\x01",
            "没看到有条岔路吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "导力梯就在\x01",
            "那条岔路的终点处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在矿车出发点有一个控制杆，\x01",
            "把它推一下就可以切换终点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3775")

    label("loc_35A7")

    OP_A2(0x23F)
    OP_28(0x3, 0x1, 0x20)

    ChrTalk(
        0x101,
        (
            "#002F我们找到那部导力梯了，\x01",
            "可是不知道怎么让它动起来。\x02\x03",
            "#002F你可以帮帮我们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是这样吗……\x01",
            "对了，要有启动开关的钥匙才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "没办法，先借给你们吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "借来了\x07\x02",
            "导力梯的钥匙\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x322, 1)

    ChrTalk(
        0x101,
        (
            "#001F谢谢矿工叔叔，\x01",
            "用完之后就还你哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3775")

    EventEnd(0x1)
    Jump("loc_3ADB")

    label("loc_377A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3921")
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    OP_A2(0x23F)
    OP_28(0x3, 0x1, 0x20)

    ChrTalk(
        0x8,
        (
            "啊？\x01",
            "导力梯不能动？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是这样吗……\x01",
            "要有启动开关的钥匙才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "没办法，先借给你们吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "借来了\x07\x02",
            "导力梯的钥匙\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x322, 1)

    ChrTalk(
        0x101,
        (
            "#001F谢谢矿工叔叔，\x01",
            "用完之后就还你哦。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_3ADB")

    label("loc_3921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 7)), scpexpr(EXPR_END)), "loc_39B1")

    ChrTalk(
        0x8,
        (
            "把钥匙插进开关里面，\x01",
            "导力梯就可以用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "用完之后还给我就行了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_39B1")


    ChrTalk(
        0x8,
        (
            "你们乘矿车过来的时候\x01",
            "没看到有条岔路吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "导力梯就在\x01",
            "那条岔路的终点处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在矿车出发点有一个控制杆，\x01",
            "把它推一下就可以切换终点了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADB")

    TalkEnd(0x8)
    Return()

    # Function_14_2F7A end

    def Function_15_3ADF(): pass

    label("Function_15_3ADF")

    EventBegin(0x0)
    SetChrPos(0xF, 27100, -500, 13125, 180)
    SetChrPos(0x101, 26230, 0, 10530, 0)
    SetChrPos(0x102, 27600, 0, 10640, 0)
    SetChrPos(0xB, 39350, 0, 26280, 0)
    SetChrPos(0xC, 24110, -40, 15950, 0)
    SetChrPos(0xD, 10800, 0, 29530, 0)
    SetChrPos(0xE, 54240, 0, 53990, 0)
    OP_3F(0x322, 1)
    OP_4A(0xF, 0)
    ClearMapFlags(0x1)
    OP_69(0x101, 0x0)

    ChrTalk(
        0xF,
        (
            "这次真是不好意思。\x01",
            "给你们添了这么多的麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "之后我会和协会进行联络，\x01",
            "好好答谢你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哈哈，别客气啦。\x01",
            "我们只是做了该做的事情而已。\x02\x03",
            "#000F这也算是一种修练吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了……\x01",
            "地下坑道打算怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "我们自己想办法处理吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "可以尝试用炸药\x01",
            "把那个魔兽的巢穴封住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "不过，如果实在有困难，\x01",
            "说不定还会请你们协会帮忙哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，到时候就交给我们吧。\x02\x03",
            "#006F那么，\x01",
            "我们就把结晶带回去给市长爷爷了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔……\x01",
            "没有把它弄丢吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F你、你这什么意思啊？\x01",
            "我才不会那么粗心呢。\x02\x03",
            "#007F你看，在这儿呢……\x02\x03",
            "#007F…………………………\x01",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x102,
        "#018F不、不会吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "丢、丢了吗！？\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_22(0x80, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0x101, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x101, 8)
    OP_8C(0x101, 180, 500)
    OP_8C(0x101, 270, 500)
    OP_8C(0x101, 0, 500)
    OP_8C(0x101, 90, 500)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#001F才不会呢⊙\x01",
            "它还乖乖地藏在这里啊。\x02\x03",
            "#001F好了，赶快把它送回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    OP_82(0x0, 0x2)
    OP_84(0x0)
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#017F我说你真是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "我的心脏差点受不了啊，小姑娘……\x02",
    )

    CloseMessageWindow()
    ClearMapFlags(0x400000)
    OP_4B(0xF, 0)
    EventEnd(0x0)
    Return()

    # Function_15_3ADF end

    def Function_16_4114(): pass

    label("Function_16_4114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_429C")
    SetMapFlags(0x8000000)
    OP_A2(0x24A)
    OP_A2(0x24D)
    OP_62(0x133, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrPos(0xA, 90000, 0, 61740, 90)
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0x102, 0xA, 0)
    TurnDirection(0x133, 0xA, 0)
    EventBegin(0x0)

    ChrTalk(
        0xA,
        "嘿咿——！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "怎么会这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "救命啊～～～～～！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4235")
    Jump("loc_4295")

    label("loc_4235")


    ChrTalk(
        0x133,
        (
            "什么！\x01",
            "还有其他人在！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F赶快去救他吧！\x02",
    )

    CloseMessageWindow()

    label("loc_4295")

    EventEnd(0x1)
    ClearMapFlags(0x8000000)

    label("loc_429C")

    Return()

    # Function_16_4114 end

    def Function_17_429D(): pass

    label("Function_17_429D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47DD")
    EventBegin(0x0)
    TurnDirection(0x0, 0x13, 0)
    TurnDirection(0x1, 0x13, 0)
    TurnDirection(0x2, 0x13, 0)
    OP_A2(0x24B)
    SetChrFlags(0xA, 0x40)
    OP_A3(0x9)
    TurnDirection(0x13, 0x101, 800)
    OP_43(0x13, 0x1, 0x0, 0x12)
    TurnDirection(0x15, 0x101, 800)
    OP_43(0x15, 0x1, 0x0, 0x12)
    TurnDirection(0x14, 0x101, 800)
    OP_43(0x14, 0x1, 0x0, 0x12)
    OP_A6(0x9)
    OP_44(0x13, 0xFF)
    OP_44(0x15, 0xFF)
    Battle(0x384, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_4319"),
        (SWITCH_DEFAULT, "loc_431E"),
    )


    label("loc_4319")

    OP_B4(0x0)
    Jump("loc_431E")

    label("loc_431E")

    EventBegin(0x0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    SetChrPos(0x133, 91310, 0, 62810, 225)
    SetChrPos(0x102, 91630, 0, 64090, 225)
    SetChrPos(0x101, 92380, 0, 62140, 270)
    OP_6D(91000, 0, 62560, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_8C(0xA, 45, 0)
    OP_44(0xA, 0xFF)
    Sleep(1000)

    ChrTalk(
        0xA,
        "得、得救了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F放心吧，已经没事了。\x02\x03",
            "#006F只要有游击士出马，\x01",
            "一两只魔兽算不了什么。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 600)

    ChrTalk(
        0xA,
        "游、游击士？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "为什么会在这里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        (
            "哦？你好像是……\x01",
            "昨天刚来的那个新人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        "现在还用不着你来地下干活啊！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x133, 600)

    ChrTalk(
        0xA,
        "这、这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我、我只是想\x01",
            "见识一下前辈们的工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "没想到那边的墙壁突然崩塌，\x01",
            "从里面冲出了好多魔兽！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        (
            "果然是和魔兽的巢穴连在一起……\x01",
            "和这位小哥推测的一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "那、那边真的很危险，\x01",
            "有很多魔兽在里面游荡着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "那、那我还是快点出去了！\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0xA, 0x2, 0x0, 0x14)
    OP_8E(0xA, 0x17598, 0x0, 0xF03C, 0x36B0, 0x0)
    OP_8E(0xA, 0x1ACA2, 0x0, 0x11044, 0x36B0, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    ChrTalk(
        0x101,
        (
            "#000F逃得真快……\x01",
            "看样子吓得不轻呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……是啊。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_44(0xA, 0xFF)

    label("loc_47DD")

    Return()

    # Function_17_429D end

    def Function_18_47DE(): pass

    label("Function_18_47DE")

    OP_92(0xFE, 0x0, 0x262, 0x1388, 0x0)
    OP_A2(0x9)
    Return()

    # Function_18_47DE end

    def Function_19_47F0(): pass

    label("Function_19_47F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_END)), "loc_49EC")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_496D")
    OP_A2(0x4)
    TurnDirection(0x133, 0x0, 400)

    ChrTalk(
        0x133,
        (
            "我说你们两个想去哪儿？\x01",
            "那边好像是魔兽的巢穴啊。\x02\x03",
            "崩塌之后可能还存在危险性，\x01",
            "我们还是不要靠近那边好。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_492A")
    TurnDirection(0x101, 0x133, 400)

    ChrTalk(
        0x101,
        "#002F的确可能有危险呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#012F嗯，我们回去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_496A")

    label("loc_492A")


    def lambda_4930():
        TurnDirection(0x101, 0x133, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4930)
    TurnDirection(0x102, 0x133, 400)

    ChrTalk(
        0x102,
        (
            "#012F是啊。\x01",
            "我们回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_496A")

    Jump("loc_49D1")

    label("loc_496D")


    ChrTalk(
        0x133,
        (
            "那边好像有魔兽的巢穴啊。\x01",
            "我们还是不要靠近那边比较安全。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49D1")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_49EC")

    Return()

    # Function_19_47F0 end

    def Function_20_49ED(): pass

    label("Function_20_49ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A0F")
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    TurnDirection(0x2, 0xFE, 0)
    OP_48()
    Jump("Function_20_49ED")

    label("loc_4A0F")

    Return()

    # Function_20_49ED end

    def Function_21_4A10(): pass

    label("Function_21_4A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B80")
    SetMapFlags(0x8000000)
    OP_A2(0x244)
    SetChrPos(0xB, 130840, 1000, 15040, 270)
    SetChrPos(0xC, 130850, 1000, 13860, 270)
    OP_62(0x133, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0xB, 0)
    TurnDirection(0x102, 0xB, 0)
    TurnDirection(0x133, 0xB, 0)
    EventBegin(0x0)

    ChrTalk(
        0xB,
        "不、不要过来！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不是我夸张，\x01",
            "我身上的筋太多，一点也不好吃！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "我、我也很难吃的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "脂肪太多了，\x01",
            "吃了肯定会有害健康！\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    ClearMapFlags(0x8000000)

    label("loc_4B80")

    Return()

    # Function_21_4A10 end

    def Function_22_4B81(): pass

    label("Function_22_4B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E7F")
    OP_A2(0x245)
    EventBegin(0x0)
    TurnDirection(0x0, 0x12, 0)
    TurnDirection(0x1, 0x12, 0)
    TurnDirection(0x2, 0x12, 0)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    TurnDirection(0x12, 0x101, 500)
    Sleep(200)
    OP_92(0x12, 0x0, 0x1F4, 0x1B58, 0x0)
    Battle(0x384, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_4BE4"),
        (SWITCH_DEFAULT, "loc_4BE9"),
    )


    label("loc_4BE4")

    OP_B4(0x0)
    Jump("loc_4BE9")

    label("loc_4BE9")

    EventBegin(0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8)
    SetChrPos(0x133, 129000, 1000, 12980, 45)
    SetChrPos(0x102, 126780, 1000, 11750, 45)
    SetChrPos(0x101, 127660, 1000, 11490, 45)
    OP_6D(128919, 1000, 12950, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    TurnDirection(0xB, 0x101, 0)
    TurnDirection(0xC, 0x101, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F已经没事了，矿工叔叔们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "得、得救了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "呼唉唉～\x01",
            "还以为再也没机会吃饭了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        "还说那么多废话干吗啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        (
            "都赶快给我逃出去！\x01",
            "再这么磨蹭，是不是想被魔兽吃进肚子啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "知、知道了，老大！\x02",
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x0, 0x17)
    Sleep(300)

    ChrTalk(
        0xC,
        "多谢救命之恩～！\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0xC, 0x2, 0x0, 0x14)
    OP_8E(0xC, 0x1EBAE, 0x1F4, 0x3138, 0x1770, 0x0)
    OP_8E(0xC, 0x1DE84, 0xFA, 0x4010, 0x1B58, 0x0)
    OP_8E(0xC, 0x1F07C, 0x0, 0x620C, 0x1F40, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    EventEnd(0x0)
    OP_44(0xC, 0xFF)

    label("loc_4E7F")

    Return()

    # Function_22_4B81 end

    def Function_23_4E80(): pass

    label("Function_23_4E80")

    OP_8E(0xB, 0x1EBAE, 0x1F4, 0x3138, 0x1770, 0x0)
    OP_8E(0xB, 0x1DE84, 0xFA, 0x4010, 0x1B58, 0x0)
    OP_8E(0xB, 0x1F07C, 0x0, 0x620C, 0x1F40, 0x0)
    Return()

    # Function_23_4E80 end

    def Function_24_4EBD(): pass

    label("Function_24_4EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FF5")
    SetMapFlags(0x8000000)
    OP_A2(0x247)
    OP_62(0x133, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0xD, 0)
    TurnDirection(0x102, 0xD, 0)
    TurnDirection(0x133, 0xD, 0)
    EventBegin(0x0)

    ChrTalk(
        0xD,
        (
            "啊啊，女神爱德丝……\x01",
            "请来救救我们吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "笨、笨蛋！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "有向神祈祷的工夫，\x01",
            "还不如快点帮忙赶走这些东西！\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    ClearMapFlags(0x8000000)

    label("loc_4FF5")

    Return()

    # Function_24_4EBD end

    def Function_25_4FF6(): pass

    label("Function_25_4FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53F4")
    OP_A2(0x248)
    EventBegin(0x0)
    TurnDirection(0x0, 0x11, 0)
    TurnDirection(0x1, 0x11, 0)
    TurnDirection(0x2, 0x11, 0)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    TurnDirection(0x11, 0x101, 500)
    Sleep(200)
    OP_92(0x11, 0x0, 0x1F4, 0x1B58, 0x0)
    Battle(0x384, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_5059"),
        (SWITCH_DEFAULT, "loc_505E"),
    )


    label("loc_5059")

    OP_B4(0x0)
    Jump("loc_505E")

    label("loc_505E")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x133, 86770, -500, 30250, 315)
    SetChrPos(0x102, 87730, 0, 28260, 315)
    SetChrPos(0x101, 88160, 0, 29600, 315)
    OP_6D(84700, -290, 30790, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(300000, 0)
    OP_6E(262, 0)
    TurnDirection(0xD, 0x101, 0)
    TurnDirection(0xE, 0x101, 0)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#010F没有受伤吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "没、没事……\x01",
            "多亏你们救了我们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "啊啊，这一定就是爱德丝的引导。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(
        0xE,
        "真是头脑简单的家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "如果真的有女神引导，\x01",
            "一开始就不会遇到这种事啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xD, 0xE, 400)

    ChrTalk(
        0xD,
        (
            "正、正是因为有你这种不虔诚的人，\x01",
            "才会引起这样不幸的事故！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(
        0xE,
        "你说什么～！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x133, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x133,
        (
            "现在是吵架的时候吗？\x01",
            "都赶快给我离开这里！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x133, 600)
    TurnDirection(0xE, 0x133, 600)

    ChrTalk(
        0xD,
        "是、是，老大！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "老大你们也要小心啊！\x02",
    )

    CloseMessageWindow()
    OP_43(0xE, 0x1, 0x0, 0x1A)
    Sleep(500)
    OP_43(0xD, 0x2, 0x0, 0x14)
    OP_8E(0xD, 0x14DFC, 0x3E8, 0x7FBC, 0x1770, 0x0)
    OP_8E(0xD, 0x17FFC, 0x0, 0x69DC, 0x1770, 0x0)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    EventEnd(0x0)
    OP_44(0xD, 0xFF)

    label("loc_53F4")

    Return()

    # Function_25_4FF6 end

    def Function_26_53F5(): pass

    label("Function_26_53F5")

    OP_8E(0xE, 0x14DFC, 0x3E8, 0x7FBC, 0x1770, 0x0)
    OP_8E(0xE, 0x17FFC, 0x0, 0x69DC, 0x1770, 0x0)
    Return()

    # Function_26_53F5 end

    def Function_27_541E(): pass

    label("Function_27_541E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_546E")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力梯的开关被锁上了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x1)
    Jump("loc_5C69")

    label("loc_546E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B4C")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 7)), scpexpr(EXPR_END)), "loc_5704")
    Fade(1000)
    SetChrPos(0x0, 53590, 50, 57020, 0)
    SetChrPos(0x1, 54570, 50, 57080, 0)
    OP_6D(53780, 50, 58370, 1000)
    OP_A2(0x241)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔。\x01",
            "用刚才借的钥匙试试看吧。\x02\x03",
            "#010F这次导力梯应该能用了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "使用了\x07\x05",
            "导力梯的钥匙\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x73, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x102,
        (
            "#010F这样导力梯应该就可以动了。\x01",
            "　\x02\x03",
            "#010F我们赶快下去吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【乘坐导力梯】\x01",      # 0
            "【不乘坐】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5654")
    Sleep(300)
    EventEnd(0x0)
    Return()

    label("loc_5654")

    Fade(1000)
    SetChrPos(0x0, 53590, 50, 57020, 0)
    SetChrPos(0x1, 54570, 50, 57080, 0)
    OP_6D(54090, 50, 57700, 1000)
    Sleep(120)
    OP_22(0x66, 0x0, 0x64)
    OP_70(0x1, 0x78)
    OP_73(0x1)
    OP_6F(0x1, 120)
    Fade(1000)
    OP_6D(129000, 0, 76700, 0)
    SetChrPos(0x0, 128580, 8000, 77050, 180)
    SetChrPos(0x1, 129560, 8000, 77060, 180)
    OP_6F(0x2, 360)
    Sleep(120)
    OP_70(0x2, 0xF0)
    OP_73(0x2)
    EventEnd(0x0)
    OP_6F(0x2, 240)
    Return()

    label("loc_5704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_591F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D6")
    Fade(1000)
    SetChrPos(0x101, 53800, 50, 57690, 0)
    SetChrPos(0x102, 54180, 50, 56280, 0)
    OP_6D(53780, 50, 58370, 1000)

    ChrTalk(
        0x101,
        (
            "#002F这个是导力梯吧？\x02\x03",
            "#002F怎么看起来不能动呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F让我看看。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    def lambda_57EA():

        label("loc_57EA")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_57EA")

    QueueWorkItem2(0x101, 1, lambda_57EA)
    OP_8F(0x101, 0xD08E, 0x32, 0xDEE4, 0x7D0, 0x0)
    OP_8E(0x102, 0xD336, 0x32, 0xE15A, 0x7D0, 0x0)
    Sleep(300)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F虽然导力还通着，\x01",
            "不过开关好像被锁上了。\x02\x03",
            "#012F问问这里的矿工比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    EventEnd(0x0)
    Jump("loc_591C")

    label("loc_58D6")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力梯的开关被锁上了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x1)

    label("loc_591C")

    Jump("loc_5B40")

    label("loc_591F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AF8")
    Fade(1000)
    SetChrPos(0x101, 53800, 50, 57690, 0)
    SetChrPos(0x102, 54180, 50, 56280, 0)
    OP_6D(53780, 50, 58370, 1000)

    ChrTalk(
        0x101,
        (
            "#505F这个就是通到地下的导力梯吧。\x02\x03",
            "#505F不过好像不能动啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F让我看看。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    def lambda_59FD():

        label("loc_59FD")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_59FD")

    QueueWorkItem2(0x101, 1, lambda_59FD)
    OP_8F(0x101, 0xD08E, 0x32, 0xDEE4, 0x7D0, 0x0)
    OP_8E(0x102, 0xD336, 0x32, 0xE15A, 0x7D0, 0x0)
    Sleep(300)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015F虽然导力还通着，\x01",
            "不过开关好像被锁上了。\x02\x03",
            "#010F去问问刚才的那个矿工吧。\x01",
            "他可能知道开动这导力梯的方法。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    EventEnd(0x0)
    Jump("loc_5B40")

    label("loc_5AF8")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力梯的开关被锁上了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x1)

    label("loc_5B40")

    OP_A2(0x240)
    OP_28(0x3, 0x1, 0x10)
    Jump("loc_5C69")

    label("loc_5B4C")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【乘坐导力梯】\x01",      # 0
            "【不乘坐】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BBE")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_5BBE")

    Fade(1000)
    SetChrPos(0x0, 53590, 50, 57020, 0)
    SetChrPos(0x1, 54570, 50, 57080, 0)
    OP_6D(54090, 50, 57700, 1000)
    Sleep(120)
    OP_22(0x66, 0x0, 0x64)
    OP_70(0x1, 0x78)
    OP_73(0x1)
    OP_6F(0x1, 120)
    Fade(1000)
    OP_6D(129000, 0, 76700, 0)
    SetChrPos(0x0, 128580, 8000, 77050, 180)
    SetChrPos(0x1, 129560, 8000, 77060, 180)
    OP_6F(0x2, 360)
    Sleep(120)
    OP_70(0x2, 0xF0)
    OP_73(0x2)
    EventEnd(0x0)
    OP_6F(0x2, 240)
    Return()

    label("loc_5C69")

    Return()

    # Function_27_541E end

    def Function_28_5C6A(): pass

    label("Function_28_5C6A")

    OP_92(0x0, 0x1, 0x0, 0xBB8, 0x0)
    TurnDirection(0x0, 0x1, 0)
    Return()

    # Function_28_5C6A end

    def Function_29_5C80(): pass

    label("Function_29_5C80")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D85")
    ClearMapFlags(0x1)
    OP_51(0x16, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x16, 0x320)
    TurnDirection(0x0, 0x2, 400)
    TurnDirection(0x1, 0x2, 400)
    TurnDirection(0x2, 0x0, 400)

    ChrTalk(
        0x133,
        (
            "不好意思……\x01",
            "好像还有兄弟在这里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        "拜托你们再帮帮忙吧。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_5D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EEF")
    OP_A2(0x24D)
    SetChrPos(0xA, 90000, 0, 61740, 90)

    ChrTalk(
        0xA,
        (
            "嘿咿——！\x01",
            "怎么会这样……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0x102, 0xA, 0)
    TurnDirection(0x133, 0xA, 0)

    ChrTalk(
        0xA,
        "救命啊～～～～～！\x02",
    )

    CloseMessageWindow()
    ClearMapFlags(0x1)
    OP_51(0x16, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x16, 0x320)

    ChrTalk(
        0x133,
        (
            "什么！\x01",
            "还有其他人在！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F赶快去救他吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FC5")

    label("loc_5EEF")

    ClearMapFlags(0x1)
    OP_51(0x16, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x16, 0x320)
    TurnDirection(0x101, 0x133, 0)
    TurnDirection(0x102, 0x133, 0)
    TurnDirection(0x133, 0x101, 0)

    ChrTalk(
        0x133,
        (
            "不好意思……\x01",
            "无论怎样也要先找到他们再说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        "拜托你们再帮帮忙吧。\x02",
    )

    CloseMessageWindow()

    label("loc_5FC5")

    EventEnd(0x1)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_5FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60D4")
    ClearMapFlags(0x1)
    OP_51(0x16, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x16, 0x320)
    TurnDirection(0x101, 0x133, 0)
    TurnDirection(0x102, 0x133, 0)
    TurnDirection(0x133, 0x101, 0)

    ChrTalk(
        0x101,
        "#000F老大叔叔，全部人都离开这里了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        "啊啊……应该没问题了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那好，\x01",
            "我们也上去吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x133, 129070, 50, 76680, 0)
    Jump("loc_614B")

    label("loc_60D4")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【乘坐导力梯】\x01",      # 0
            "【不乘坐】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6146")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_6146")

    Fade(1000)

    label("loc_614B")

    SetChrPos(0x0, 128440, 50, 77690, 0)
    SetChrPos(0x1, 129410, 50, 77690, 0)
    OP_6D(129020, 50, 77590, 1000)
    Sleep(120)
    OP_22(0x66, 0x0, 0x64)
    OP_70(0x2, 0x168)
    OP_73(0x2)
    OP_6F(0x2, 360)
    Fade(1000)
    OP_6F(0x1, 120)
    Sleep(120)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62A5")
    SetChrPos(0xD, 51560, 0, 55100, 0)
    SetChrPos(0xE, 51880, 0, 53800, 0)
    SetChrPos(0x9, 53210, 0, 54100, 0)
    SetChrPos(0x8, 55190, 0, 54000, 0)
    SetChrPos(0xB, 55250, 0, 51960, 0)
    SetChrPos(0xC, 56100, 0, 52360, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x133, 0x8)
    ClearChrFlags(0x133, 0x80)
    ClearChrFlags(0x133, 0x4)
    SetChrBattleFlags(0x133, 0x20)
    OP_89(0x133, 54000, 0, 56400, 180)
    TurnDirection(0xD, 0x133, 0)
    TurnDirection(0xE, 0x133, 0)
    TurnDirection(0xC, 0x133, 0)
    TurnDirection(0xB, 0x133, 0)
    TurnDirection(0x9, 0x133, 0)
    TurnDirection(0x8, 0x133, 0)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)

    label("loc_62A5")

    OP_6D(54110, 50, 57680, 0)
    SetChrPos(0x0, 53380, -6000, 57690, 180)
    SetChrPos(0x1, 54620, -6000, 57470, 180)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_6F(0x1, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6586")

    def lambda_62FB():
        OP_6D(54030, 0, 55920, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62FB)
    OP_8E(0x133, 0xD41C, 0x0, 0xD714, 0xFA0, 0x0)
    OP_A2(0x24E)
    OP_28(0x3, 0x1, 0x100)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x8,
        "老大，没事吧！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "哎哎～幸好平安无事呢！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x133, 0x101, 400)

    ChrTalk(
        0x133,
        "多亏了小姑娘你们啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x133, 0x9, 400)

    ChrTalk(
        0x133,
        "对了，弟兄们都在这里吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "没错，都在这里了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过，刚才那个见习的新人\x01",
            "慌慌忙忙地逃走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "看来真是受了很大的惊吓啊，那家伙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        (
            "是这样吗……\x01",
            "可别为这种事受打击就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        (
            "总之，\x01",
            "地下很可能还有魔兽残存着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        (
            "在未确认安全之前，\x01",
            "这个导力梯暂时禁止使用了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    RemoveParty(0x32, 0xFF)
    ClearMapFlags(0x8000000)
    NewScene("ED6_DT01/R0303   ._SN", 3, 0, 0)
    IdleLoop()

    label("loc_6586")

    ClearMapFlags(0x400000)
    EventEnd(0x0)
    ClearMapFlags(0x8000000)
    Return()

    # Function_29_5C80 end

    def Function_30_6593(): pass

    label("Function_30_6593")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6656")
    OP_6D(15980, 0, 32049, 1000)
    OP_A2(0x23D)

    ChrTalk(
        0x101,
        (
            "#000F是矿车啊……\x01",
            "这东西也是靠导力运转的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F好像是。\x01",
            "我们赶快坐上去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6656")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "乘坐矿车\x01",      # 0
            "不乘坐\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66C3")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_66C3")

    SetMapFlags(0x1)
    Fade(500)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrPos(0x0, 15900, 400, 32299, 0)
    SetChrPos(0x1, 15900, 400, 32299, 0)
    SetChrPos(0x2, 15900, 400, 32299, 0)
    SetChrPos(0x3, 15900, 400, 32299, 0)
    Sleep(500)
    OP_22(0x65, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67BA")
    OP_A3(0x6)
    OP_A2(0x7)
    OP_A3(0x8)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x14A)
    OP_73(0x0)
    OP_6F(0x0, 330)
    Sleep(500)
    Fade(500)
    OP_69(0x0, 0x0)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x0, 34200, 100, 61400, 315)
    SetChrPos(0x1, 34200, 100, 61400, 315)
    SetChrPos(0x2, 34200, 100, 61400, 315)
    SetChrPos(0x3, 34200, 100, 61400, 315)
    Jump("loc_683F")

    label("loc_67BA")

    OP_A3(0x6)
    OP_A3(0x7)
    OP_A2(0x8)
    OP_6F(0x0, 500)
    OP_70(0x0, 0x384)
    OP_73(0x0)
    OP_6F(0x0, 900)
    Sleep(500)
    Fade(500)
    OP_69(0x0, 0x0)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x0, 50500, 0, 51900, 45)
    SetChrPos(0x1, 50500, 0, 51900, 45)
    SetChrPos(0x2, 50500, 0, 51900, 45)
    SetChrPos(0x3, 50500, 0, 51900, 45)

    label("loc_683F")

    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_30_6593 end

    def Function_31_6847(): pass

    label("Function_31_6847")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "乘坐矿车\x01",      # 0
            "不乘坐\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68B6")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_68B6")

    OP_A2(0x6)
    OP_A3(0x7)
    OP_A3(0x8)
    SetMapFlags(0x1)
    Fade(500)
    OP_69(0x0, 0x0)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrPos(0x0, 34800, 400, 59200, 225)
    SetChrPos(0x1, 34800, 400, 59200, 225)
    SetChrPos(0x2, 34800, 400, 59200, 225)
    SetChrPos(0x3, 34800, 400, 59200, 225)
    Sleep(500)
    OP_22(0x65, 0x0, 0x64)
    OP_6F(0x0, 330)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_6F(0x0, 0)
    Sleep(500)
    Fade(500)
    OP_69(0x0, 0x0)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x0, 16000, 50, 29700, 180)
    SetChrPos(0x1, 16000, 50, 29700, 180)
    SetChrPos(0x2, 16000, 50, 29700, 180)
    SetChrPos(0x3, 16000, 50, 29700, 180)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_31_6847 end

    def Function_32_69B1(): pass

    label("Function_32_69B1")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "乘坐矿车\x01",      # 0
            "不乘坐\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A20")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_6A20")

    OP_A2(0x6)
    OP_A3(0x7)
    OP_A3(0x8)
    SetMapFlags(0x1)
    Fade(500)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrPos(0x0, 50200, 400, 49900, 270)
    SetChrPos(0x1, 50200, 400, 49900, 270)
    SetChrPos(0x2, 50200, 400, 49900, 270)
    SetChrPos(0x3, 50200, 400, 49900, 270)
    Sleep(500)
    OP_22(0x65, 0x0, 0x64)
    OP_6F(0x0, 900)
    OP_70(0x0, 0x1F4)
    OP_73(0x0)
    OP_6F(0x0, 500)
    Sleep(500)
    Fade(500)
    OP_69(0x0, 0x0)
    SetChrPos(0x0, 16000, 50, 29700, 180)
    SetChrPos(0x1, 16000, 50, 29700, 180)
    SetChrPos(0x2, 16000, 50, 29700, 180)
    SetChrPos(0x3, 16000, 50, 29700, 180)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_32_69B1 end

    def Function_33_6B14(): pass

    label("Function_33_6B14")

    SetMapFlags(0x80)
    Sleep(30)
    OP_22(0x64, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B42")
    OP_70(0x3, 0x19)
    OP_73(0x3)
    OP_6F(0x3, 25)
    OP_A2(0x0)
    Jump("loc_6B56")

    label("loc_6B42")

    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_6F(0x3, 0)
    OP_A3(0x0)

    label("loc_6B56")

    OP_73(0x3)
    ClearMapFlags(0x80)
    Return()

    # Function_33_6B14 end

    def Function_34_6B5F(): pass

    label("Function_34_6B5F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在此休息\x01",      # 0
            "离开\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D75")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 104880, 1000, 39790, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x33, 0)
    OP_70(0x33, 0x32)
    OP_73(0x33)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 104880, 1000, 39790, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, 106750, 0, 39530, 285)
    SetChrPos(0x1, 106750, 0, 39530, 285)
    SetChrPos(0x2, 106750, 0, 39530, 285)
    SetChrPos(0x3, 106750, 0, 39530, 285)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 104880, 1000, 39790, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x33, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_6D75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D8F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_6D8F")

    Return()

    # Function_34_6B5F end

    SaveToFile()

Try(main)
