from ED6ScenarioHelper import *

def main():
    # 社团大楼　学生会室

    CreateScenaFile(
        FileName            = 'T2511   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2511.x',
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
        '米克',                                 # 11
        '帕布尔',                               # 12
        '黛拉',                                 # 13
        '罗伊斯',                               # 14
        '巴托姆',                               # 15
        '芙拉瑟',                               # 16
        '蕾娜',                                 # 17
        '德波拉',                               # 18
        '巴克斯',                               # 19
        'CH22000',                              # 20
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
        'ED6_DT07/CH01080 ._CH',             # 02
        'ED6_DT07/CH01090 ._CH',             # 03
        'ED6_DT07/CH01370 ._CH',             # 04
        'ED6_DT07/CH01580 ._CH',             # 05
        'ED6_DT07/CH01130 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH00003 ._CH',             # 08
        'ED6_DT07/CH00013 ._CH',             # 09
        'ED6_DT07/CH00043 ._CH',             # 0A
        'ED6_DT07/CH01083 ._CH',             # 0B
        'ED6_DT07/CH01373 ._CH',             # 0C
        'ED6_DT06/CH20021 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH01080P._CP',             # 02
        'ED6_DT07/CH01090P._CP',             # 03
        'ED6_DT07/CH01370P._CP',             # 04
        'ED6_DT07/CH01580P._CP',             # 05
        'ED6_DT07/CH01130P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH00003P._CP',             # 08
        'ED6_DT07/CH00013P._CP',             # 09
        'ED6_DT07/CH00043P._CP',             # 0A
        'ED6_DT07/CH01083P._CP',             # 0B
        'ED6_DT07/CH01373P._CP',             # 0C
        'ED6_DT06/CH20021P._CP',             # 0D
    )

    DeclNpc(
        X                   = 30800,
        Z                   = 0,
        Y                   = 55110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = -6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -31590,
        Z                   = 0,
        Y                   = 58850,
        Direction           = 0,
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
        X                   = 4100,
        Z                   = 0,
        Y                   = -4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -29000,
        Z                   = 0,
        Y                   = 53100,
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
        X                   = -28800,
        Z                   = 0,
        Y                   = 27800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 27700,
        Z                   = 0,
        Y                   = 23300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 29700,
        Z                   = 0,
        Y                   = 23300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -30000,
        Z                   = 0,
        Y                   = 56000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -31350,
        Z                   = 330,
        Y                   = 23900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835021,
        ChipIndex           = 0xD,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -2200,
        Y                   = 0,
        Z                   = 50000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = -2200,
        Y                   = 0,
        Z                   = 42000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 2130,
        Y                   = 0,
        Z                   = 42010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 2200,
        Y                   = 0,
        Z                   = 50000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 22,
    )


    DeclActor(
        TriggerX            = -31560,
        TriggerZ            = 0,
        TriggerY            = 59430,
        TriggerRange        = 800,
        ActorX              = -31560,
        ActorZ              = 1000,
        ActorY              = 59430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3060,
        TriggerZ            = 0,
        TriggerY            = 2500,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -31350,
        TriggerZ            = 330,
        TriggerY            = 23900,
        TriggerRange        = 500,
        ActorX              = -31350,
        ActorZ              = 500,
        ActorY              = 23900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_386",          # 00, 0
        "Function_1_572",          # 01, 1
        "Function_2_5F2",          # 02, 2
        "Function_3_76F",          # 03, 3
        "Function_4_A6A",          # 04, 4
        "Function_5_C7B",          # 05, 5
        "Function_6_CF2",          # 06, 6
        "Function_7_E29",          # 07, 7
        "Function_8_110C",         # 08, 8
        "Function_9_14E8",         # 09, 9
        "Function_10_1876",        # 0A, 10
        "Function_11_1A5F",        # 0B, 11
        "Function_12_1DB1",        # 0C, 12
        "Function_13_1DB6",        # 0D, 13
        "Function_14_24D4",        # 0E, 14
        "Function_15_252A",        # 0F, 15
        "Function_16_3AE9",        # 10, 16
        "Function_17_3DAA",        # 11, 17
        "Function_18_3E17",        # 12, 18
        "Function_19_3FC9",        # 13, 19
        "Function_20_3FCD",        # 14, 20
        "Function_21_3FD1",        # 15, 21
        "Function_22_3FD5",        # 16, 22
    )


    def Function_0_386(): pass

    label("Function_0_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_400")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 11)
    SetChrPos(0xA, -3680, 200, -5980, 270)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    OP_44(0xA, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -32240, 0, 58170, 270)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 28700, 0, 54820, 90)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 30850, 0, 55030, 270)
    Jump("loc_4F2")

    label("loc_400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_40A")
    Jump("loc_4F2")

    label("loc_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_414")
    Jump("loc_4F2")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_434")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -31700, 0, 58360, 0)
    Jump("loc_4F2")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_443")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_4F2")

    label("loc_443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_4CD")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 11)
    SetChrPos(0xA, -3680, 200, -5980, 270)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    OP_44(0xA, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 12)
    SetChrPos(0xC, 4050, 200, -4080, 180)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    OP_44(0xC, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B8")
    SetChrFlags(0xF, 0x10)

    label("loc_4B8")

    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA")
    SetChrFlags(0x10, 0x10)

    label("loc_4CA")

    Jump("loc_4F2")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_4D7")
    Jump("loc_4F2")

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_4E1")
    Jump("loc_4F2")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_4EB")
    Jump("loc_4F2")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_4F2")

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_509")
    OP_A3(0x3FA)
    Event(0, 16)
    OP_B1("t2511_n")

    label("loc_509")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_515"),
        (SWITCH_DEFAULT, "loc_571"),
    )


    label("loc_515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56E")
    OP_A2(0x430)
    OP_28(0x1F, 0x4, 0x40)
    OP_28(0x1D, 0x4, 0x40)
    OP_28(0x22, 0x4, 0x40)
    OP_28(0x23, 0x4, 0x40)
    OP_28(0x24, 0x4, 0x40)
    OP_28(0x1C, 0x4, 0x40)
    OP_28(0x20, 0x4, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x334)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_555")
    OP_28(0x21, 0x4, 0x40)

    label("loc_555")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_565")
    OP_28(0x1E, 0x4, 0x40)

    label("loc_565")

    OP_28(0x26, 0x4, 0x40)
    Event(0, 15)

    label("loc_56E")

    Jump("loc_571")

    label("loc_571")

    Return()

    # Function_0_386 end

    def Function_1_572(): pass

    label("Function_1_572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_593")
    OP_B1("t2511_y")
    Jump("loc_59C")

    label("loc_593")

    OP_B1("t2511_n")

    label("loc_59C")

    OP_64(0x0, 0x1)
    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_5B3")
    OP_65(0x2, 0x1)

    label("loc_5B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_5C7")
    OP_64(0x2, 0x1)
    SetChrFlags(0x13, 0x80)

    label("loc_5C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F1")
    OP_65(0x0, 0x1)

    label("loc_5F1")

    Return()

    # Function_1_572 end

    def Function_2_5F2(): pass

    label("Function_2_5F2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_617")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_759")

    label("loc_617")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_630")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_759")

    label("loc_630")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_649")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_759")

    label("loc_649")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_662")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_759")

    label("loc_662")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67B")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_759")

    label("loc_67B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_694")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_759")

    label("loc_694")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AD")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_759")

    label("loc_6AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C6")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_759")

    label("loc_6C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DF")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_759")

    label("loc_6DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F8")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_759")

    label("loc_6F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_711")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_759")

    label("loc_711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72A")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_759")

    label("loc_72A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_743")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_759")

    label("loc_743")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_759")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_759")

    label("loc_76E")

    Return()

    # Function_2_5F2 end

    def Function_3_76F(): pass

    label("Function_3_76F")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_7D8")

    ChrTalk(
        0xFE,
        "呼啊啊啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，终于完了。\x01",
            "稍微休息一下就回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A66")

    label("loc_7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_8F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_892")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我一点也不想\x01",
            "参加学园祭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "稍微偷下懒，\x01",
            "混过这一天算了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "为什么我要参加这种活动……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F4")

    label("loc_892")


    ChrTalk(
        0xFE,
        (
            "稍微偷下懒，\x01",
            "混过这一天算了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "为什么我要参加这种活动……\x02",
    )

    CloseMessageWindow()

    label("loc_8F4")

    Jump("loc_A66")

    label("loc_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_9EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98A")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "呼啊～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀哎呀～～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果在教室里无所事事，\x01",
            "那个多事的学生会长又会啰嗦了。\x01",
            "还是在这里打发时间吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EB")

    label("loc_98A")


    ChrTalk(
        0xFE,
        (
            "如果在教室里无所事事，\x01",
            "那个多事的学生会长又会啰嗦了。\x01",
            "还是在这里打发时间吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EB")

    Jump("loc_A66")

    label("loc_9EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_A66")

    ChrTalk(
        0xFE,
        (
            "学园祭的准备工作\x01",
            "真是麻烦死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "让想干的家伙\x01",
            "去干个够不就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A66")

    TalkEnd(0xA)
    Return()

    # Function_3_76F end

    def Function_4_A6A(): pass

    label("Function_4_A6A")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C07")
    OP_A2(0x4CC)

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "是这里吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我为了写小说，\x01",
            "正在寻找资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "受了最近读的书的影响，\x01",
            "我的创作欲望不断增强哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果可以的话，\x01",
            "你们也来读读那本书吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x217, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "红耀石　第６卷\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        "呵呵，书是心灵的养料。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C77")

    label("loc_C07")


    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "是这里吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我为了写小说，\x01",
            "正在寻找资料。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C77")

    TalkEnd(0xB)
    Return()

    # Function_4_A6A end

    def Function_5_C7B(): pass

    label("Function_5_C7B")

    TalkBegin(0xC)

    ChrTalk(
        0xFE,
        "吹奏部的人怎么还不来啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就靠我一个人开始准备\x01",
            "没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_5_C7B end

    def Function_6_CF2(): pass

    label("Function_6_CF2")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DED")
    OP_A2(0x3)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "啊，科洛丝。\x01",
            "你回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F啊，罗伊斯，\x01",
            "你看起来好像很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了做好班级展示，\x01",
            "我正在调查资料呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，不快点完成的话\x01",
            "又要听罗基克啰嗦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E25")

    label("loc_DED")


    ChrTalk(
        0xFE,
        (
            "为了做我们的班级展示，\x01",
            "我正在调查东西呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E25")

    TalkEnd(0xD)
    Return()

    # Function_6_CF2 end

    def Function_7_E29(): pass

    label("Function_7_E29")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_F23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDB")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "现在开始要社团练习了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为学园祭休息了一阵子，\x01",
            "感觉都变得迟钝了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再怎么每天坚持练习，\x01",
            "休息一阵子就会变成这样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F20")

    label("loc_EDB")


    ChrTalk(
        0xFE,
        "现在开始要社团练习了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为学园祭休息了一阵子，\x01",
            "感觉都变得迟钝了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F20")

    Jump("loc_1108")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1108")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDE")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "学园祭的准备期间\x01",
            "连社团的训练都中止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我今天来这儿\x01",
            "是来拿道具的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，\x01",
            "因为是很重要的东西呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1108")

    label("loc_FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_108C")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "我和科洛丝一样\x01",
            "是击剑部的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来必须要\x01",
            "去社团的摊位帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我很担心莉秋尔呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1108")

    label("loc_108C")


    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "接下来要去社团的摊位帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我很担心莉秋尔呀。\x02",
    )

    CloseMessageWindow()

    label("loc_1108")

    TalkEnd(0xE)
    Return()

    # Function_7_E29 end

    def Function_8_110C(): pass

    label("Function_8_110C")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_14E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148C")
    OP_A2(0x6)
    OP_A2(0x7)
    OP_4A(0x10, 255)

    ChrTalk(
        0xF,
        "啊，忙死了忙死了，\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "班级展示、舞台剧，\x01",
            "还要准备社团的摊位……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "想不到我也有么辛苦的时候呀。\x01",
            "要推辞掉哪一边才好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "……人的语言\x01",
            "有时候是个暧昧的东西。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 500)

    ChrTalk(
        0xF,
        "…………哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "工作总是拼尽全力，\x01",
            "得到好结果的人说自己很忙，\x01",
            "这样谁都能接受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "而固执于一件事\x01",
            "却没有什么进展的人，\x01",
            "倒是也有权利说自己很忙……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        "你到底想说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "不，我想知道芙拉瑟\x01",
            "你说的忙是哪种情况呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "当然啦，你那么厉害，\x01",
            "我想应该是前者吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        "……啊，我知道啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "我都做就好了吧，都做！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4B(0x10, 255)
    Jump("loc_14E4")

    label("loc_148C")


    ChrTalk(
        0xFE,
        "真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "蕾娜老是\x01",
            "喜欢这样在旁边\x01",
            "煽风点火的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E4")

    TalkEnd(0xF)
    Return()

    # Function_8_110C end

    def Function_9_14E8(): pass

    label("Function_9_14E8")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1872")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1828")
    TalkBegin(0xF)
    OP_A2(0x6)
    OP_A2(0x7)
    OP_4A(0xF, 255)

    ChrTalk(
        0xF,
        (
            "啊，忙死了忙死了，\x01",
            "班级展示、舞台剧，\x01",
            "还要准备社团的摊位……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "好忙呀好忙呀，\x01",
            "想不到我也有么辛苦的时候呀……\x01",
            "要推辞掉哪一边才好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "……人的语言\x01",
            "有时候是个暧昧的东西。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 500)

    ChrTalk(
        0xF,
        "哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "工作总是拼尽全力，\x01",
            "得到好结果的人说自己很忙，\x01",
            "这样谁都能接受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "而固执于一件事\x01",
            "却没有什么进展的人，\x01",
            "倒是也有权利说自己很忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "你到底想说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "不，我想知道芙拉瑟\x01",
            "你说的忙是哪种情况呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "当然啦，你那么厉害，\x01",
            "我想应该是前者吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "……啊，我知道啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "我都做就好了吧，都做！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4B(0xF, 255)
    TalkEnd(0xF)
    Jump("loc_1872")

    label("loc_1828")


    ChrTalk(
        0xFE,
        (
            "呵呵，我知道你有能力，\x01",
            "就不要推托了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1872")

    TalkEnd(0x10)
    Return()

    # Function_9_14E8 end

    def Function_10_1876(): pass

    label("Function_10_1876")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D0")
    OP_A2(0x8)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "#643F艾丝蒂尔、约修亚……\x01",
            "你们是特地过来找我们的吗？\x02\x03",
            "#640F……在这一段不算长的时间里，\x01",
            "好事呀坏事呀，\x01",
            "真是发生不少了。\x02\x03",
            "啊，\x01",
            "能遇到你们实在是太好了。\x02\x03",
            "总之最后全部\x01",
            "都是好结果呢。\x01",
            "就这样保持乐观继续前进吧。\x02\x03",
            "#648F到了蔡斯也要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A5B")

    label("loc_19D0")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "#640F总之最后\x01",
            "全部都是好结果呢。\x01",
            "就这样保持乐观继续前进吧。\x02\x03",
            "到了蔡斯也要继续加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A5B")

    TalkEnd(0x8)
    Return()

    # Function_10_1876 end

    def Function_11_1A5F(): pass

    label("Function_11_1A5F")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC5")
    OP_A2(0xA)
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "#733F……是约修亚你们啊。\x02\x03",
            "#732F我读过《利贝尔通讯》了……\x01",
            "那个戴尔蒙市长竟然是幕后黑手啊。\x02\x03",
            "背地里策划那种坏事，\x01",
            "来学园祭捐款的时候还能面不改色。\x01",
            "　\x02\x03",
            "而且后来还袭击特蕾莎院长……\x01",
            "　\x02\x03",
            "…………哼，\x01",
            "真是坏到骨子里去了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAD")

    label("loc_1BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF4")
    OP_A2(0xB)
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "#730F对了，\x01",
            "你们俩不是要去蔡斯吗？\x02\x03",
            "那我们就暂时见不到面了……\x01",
            "　\x02\x03",
            "不过，只要活着的话，\x01",
            "总会再见面的吧，\x01",
            "那我就不说再见了。\x02\x03",
            "为了成为一流的正游击士，\x01",
            "你们一定要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAD")

    label("loc_1CF4")

    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "#730F只要活着的话，\x01",
            "总会再见面的吧，\x01",
            "那我就不说再见了。\x02\x03",
            "为了成为一流的正游击士，\x01",
            "你们一定要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAD")

    TalkEnd(0x9)
    Return()

    # Function_11_1A5F end

    def Function_12_1DB1(): pass

    label("Function_12_1DB1")

    Call(0, 13)
    Return()

    # Function_12_1DB1 end

    def Function_13_1DB6(): pass

    label("Function_13_1DB6")

    TalkBegin(0x11)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                             # 0
            "买东西\x01",                           # 1
            "欢迎品尝「学院午餐」500米拉\x01",      # 2
            "离开\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2F")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x30)
    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_1E2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F35")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EFB")
    SubMira(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "尝了尝\x07\x02",
            "学院午餐\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2BC)
    OP_31(0x1, 0xFD, 0x2BC)
    OP_31(0x2, 0xFD, 0x2BC)
    OP_31(0x3, 0xFD, 0x2BC)
    OP_31(0x4, 0xFD, 0x2BC)
    OP_31(0x5, 0xFD, 0x2BC)
    OP_31(0x6, 0xFD, 0x2BC)
    OP_31(0x7, 0xFD, 0x2BC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x9)"), scpexpr(EXPR_END)), "loc_1EC0")
    Jump("loc_1EED")

    label("loc_1EC0")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "学院午餐\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EED")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_1F23")

    label("loc_1EFB")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_1F23")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x11)
    Return()

    label("loc_1F35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F4F")
    FadeToBright(300, 0)
    TalkEnd(0x11)
    Return()

    label("loc_1F4F")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1F89")

    ChrTalk(
        0x11,
        (
            "欢迎光临。\x01",
            "想要点些什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_1F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_210F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C6")

    ChrTalk(
        0x11,
        (
            "舞台剧我也看了哦。\x01",
            "你们真是非常努力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "辛苦你们了，\x01",
            "这是一点小意思，\x01",
            "就当是我看演出的门票吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "不用客气，吃吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x452)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "沙拉三明治\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x193, 1)
    Jump("loc_210C")

    label("loc_20C6")


    ChrTalk(
        0x11,
        (
            "舞台剧我也看了哦。\x01",
            "你们真是非常努力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210C")

    Jump("loc_24D0")

    label("loc_210F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2172")

    ChrTalk(
        0x11,
        "你们要参加演出吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "阿姨我也要去看。\x01",
            "真是很期待呀，你们要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_2172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_21CE")

    ChrTalk(
        0x11,
        (
            "今天这里作为\x01",
            "休息的场所对公众开放。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不过和平时一样，\x01",
            "也可以点菜哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_21CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2268")

    ChrTalk(
        0x11,
        (
            "一直忙于学园祭的准备，\x01",
            "都还没吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "像你们这样的孩子\x01",
            "必须要好好摄取营养\x01",
            "身体才能健康成长啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_2268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_22F1")

    ChrTalk(
        0x11,
        "学园祭的准备还顺利吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "这段时间我特别准备了丰盛的饭菜，\x01",
            "你们随时都能来用餐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_22F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_2369")

    ChrTalk(
        0x11,
        "啊，马上就要下课了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "同学们要来吃饭了，\x01",
            "必须加把劲呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_2369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_23E0")

    ChrTalk(
        0x11,
        (
            "呀，是科洛丝啊。\x01",
            "现在应该还在上课啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不好意思，\x01",
            "现在这边还在准备中。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_23E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_245A")

    ChrTalk(
        0x11,
        (
            "啊，\x01",
            "你们两个是想来入学的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "就算不是学生也能来这里吃饭哦。\x01",
            "作为参观纪念想吃些什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_245A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_24D0")

    ChrTalk(
        0x11,
        (
            "这个学生食堂\x01",
            "假日里也会开放的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "如果饿了，\x01",
            "就不要客气，尽管点菜吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D0")

    TalkEnd(0x11)
    Return()

    # Function_13_1DB6 end

    def Function_14_24D4(): pass

    label("Function_14_24D4")

    TalkBegin(0x12)

    ChrTalk(
        0xFE,
        "这里没有别人了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还是把门锁起来吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_14_24D4 end

    def Function_15_252A(): pass

    label("Function_15_252A")

    EventBegin(0x0)
    SetMapFlags(0x10000000)
    OP_6D(31070, 0, 57740, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x40)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#644F#1P啊～忙死了、忙死了。\x02\x03",
            "各货摊的检查\x01",
            "还有预算的分配都ＯＫ了……\x02\x03",
            "请柬的发送也没问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#734F剩下的问题就只有舞台剧了啊……\x02\x03",
            "再找不到人选的话，\x01",
            "恐怕就只有我们亲自上阵了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        (
            "#645F#1P我自己就暂且不说，\x01",
            "你……我看还是算了吧。\x02\x03",
            "一想起你试穿戏服时\x01",
            "那个恐怖十足的打扮我就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#732F别提啦……\x01",
            "我也是不堪回首啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x102, 24910, 0, 55980, 243)
    SetChrPos(0x101, 24910, 0, 55980, 243)
    SetChrPos(0x105, 24910, 0, 55980, 243)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    ChrTalk(
        0x105,
        (
            "#2P我回来了。\x01",
            "乔儿、汉斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 400)
    TurnDirection(0x9, 0x105, 400)

    def lambda_287A():
        OP_6D(29890, 0, 55890, 1500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_287A)
    ClearChrFlags(0x105, 0x80)

    def lambda_2897():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_2897)
    OP_8E(0x105, 0x6928, 0x0, 0xD99E, 0x7D0, 0x0)

    def lambda_28BD():
        OP_8E(0xFE, 0x6D06, 0x0, 0xD480, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_28BD)
    OP_8C(0x9, 270, 0)
    ClearChrFlags(0x101, 0x80)

    def lambda_28E4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_28E4)
    OP_8E(0x101, 0x6928, 0x0, 0xD99E, 0x7D0, 0x0)

    def lambda_290A():
        OP_8E(0xFE, 0x6996, 0x0, 0xD5AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_290A)
    ClearChrFlags(0x102, 0x80)

    def lambda_292A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_292A)

    def lambda_293C():
        OP_8E(0xFE, 0x6B30, 0x0, 0xD9C6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_293C)
    WaitChrThread(0x105, 0x1)

    def lambda_295C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_295C)
    WaitChrThread(0x101, 0x1)

    def lambda_296F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_296F)
    WaitChrThread(0x102, 0x1)

    def lambda_2982():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2982)

    def lambda_2990():

        label("loc_2990")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2990")

    QueueWorkItem2(0x102, 1, lambda_2990)

    def lambda_29A1():

        label("loc_29A1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_29A1")

    QueueWorkItem2(0x101, 1, lambda_29A1)

    def lambda_29B2():

        label("loc_29B2")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_29B2")

    QueueWorkItem2(0x105, 1, lambda_29B2)

    ChrTalk(
        0x8,
        (
            "#642F啊，科洛丝！？\x02\x03",
            "火灾的事我们听也说了。\x01",
            "事情好像很严重啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#732F特蕾莎院长和小家伙们\x01",
            "都平安无事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯……\x01",
            "还好，大家总算没事。\x02\x03",
            "#049F最遗憾的是，\x01",
            "孤儿院的房子被完全烧毁了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#732F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#644F打起精神来嘛。\x01",
            "发愁也解决不了问题啊。\x02\x03",
            "为了让那些小家伙高兴起来，\x01",
            "我们一定要把学园祭办好哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F嗯，特蕾莎老师\x01",
            "也是这样和我说的。\x02\x03",
            "所以，我一定会全力以赴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#641F你要是认真起来，足以以一当百。\x01",
            "我可是很期待你的精彩演出哦。\x02\x03",
            "#640F对了，\x01",
            "刚才就想问了……\x02\x03",
            "这两位是谁呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F初次见面。\x01",
            "我叫艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我叫约修亚，请多关照。\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#643F那么，你们两个就是\x01",
            "科洛丝昨天提过的……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F呵呵，我如约把他们带来了哦。\x02\x03",
            "他们两人都答应帮我们的忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#641F啊～这回有救了！\x02\x03",
            "#641F初次见面。\x01",
            "艾丝蒂尔、约修亚。\x02\x03",
            "我是学院的学生会长\x01",
            "乔儿·利德那。\x02\x03",
            "也是这次舞台剧的导演。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#730F我是副会长汉斯。\x01",
            "负责剧本和组织工作。\x02\x03",
            "还请两位多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请多关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#644F嗯，不过话说回来……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x8)

    ChrTalk(
        0x101,
        "#004F什、什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#640F不愧是游击士，\x01",
            "看上去真的充满运动细胞啊。\x02\x03",
            "艾丝蒂尔，你会用剑吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F这个，也不是很擅长啦……\x02\x03",
            "我主要学的是棒术，\x01",
            "不过倒也跟老爸学过一点剑法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#641F太好了，那就这么定了。\x02\x03",
            "你就用细剑\x01",
            "和科洛丝来场精彩的决斗吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F决、决斗！？\x02",
    )

    CloseMessageWindow()
    OP_44(0x105, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x105, 400)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#040F#2P当然是在舞台剧的时候。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#640F舞台剧的高潮部分，\x01",
            "会有两位骑士决斗的剧情。\x02\x03",
            "总之，这是今年学园祭里\x01",
            "最扣人心弦的压轴好戏啦……\x02\x03",
            "#645F可惜到现在还找不到一个\x01",
            "能在剑法上和科洛丝一拼的女生。\x02\x03",
            "这丫头甚至在学院的击剑大赛里\x01",
            "打赢了男生取得优胜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哇～好厉害！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#649F顺便一提，在决赛中输给她的\x01",
            "就是我旁边的这位汉斯哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#734F真不好意思，输掉了。\x02\x03",
            "不过可不是我太弱，\x01",
            "而是科洛丝实在太强了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F#2P太、太夸奖了，\x01",
            "其实我也只是业余水准……\x02\x03",
            "跟职业水平的艾丝蒂尔比起来，\x01",
            "我也是小巫见大巫呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F又来了又来了，你太谦虚了。\x02\x03",
            "不过，这种事的话\x01",
            "或许我真的能帮上点忙。\x02\x03",
            "#001F科洛丝，我们一起加油哦⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F#2P是。\x01",
            "请多多指教。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#1P哈哈，不过话说回来……\x02\x03",
            "女骑士之间的对决，\x01",
            "这题材真是挺独一无二的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "#733F女骑士？\x02\x03",
            "她们要演的可是\x01",
            "受人仰慕的男性骑士哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_33F1():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_33F1)
    TurnDirection(0x102, 0x9, 0)
    Sleep(400)

    ChrTalk(
        0x102,
        "#014F#1P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#649F不过约修亚也真是无可挑剔，\x01",
            "另一个重要角色非你莫属呢……\x02\x03",
            "期待你的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#731F嗯嗯，虽然不甘心，不过我也有同感。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F？？？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#014F那个，这出舞台剧……\x01",
            "大致的故事情节是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#640F剧名叫『白花恋诗』。\x02\x03",
            "是以废除贵族制度时期的王都为舞台，\x01",
            "一个非常有名的故事哦。\x02\x03",
            "#647F贵族出身的骑士和\x01",
            "平民出身的骑士同时\x01",
            "爱上了王族公主的爱情诗剧……\x02\x03",
            "#642F这三个人虽然身份地位悬殊，\x01",
            "但却是从小一起长大的好朋友。\x02\x03",
            "而剧情当中又夹杂着\x01",
            "贵族势力和平民势力的明争暗斗。\x02\x03",
            "#648F不过最后还是大团圆，\x01",
            "无可挑剔的完满结局哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F哎～听起来很有趣啊⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F那、那么……\x02\x03",
            "为什么要由女孩来演男性角色？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#731F这是今年的学园祭才有的，\x01",
            "可说是独创且又刺激的安排哦。\x02\x03",
            "由男女演员反串出演，\x01",
            "以一种新鲜的形式表现舞台剧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F男女反串？\x02\x03",
            "哎～这样子安排，\x01",
            "老师居然也会批准啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#644F摆脱性别歧视！\x01",
            "从性别中解放出来！\x02\x03",
            "我们诌了一堆这样那样的理由，\x01",
            "好不容易才逼他们同意的哦。\x02\x03",
            "#641F不过话说回来，\x01",
            "其实也只是因为好玩啦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#045F乔儿你真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#734F唉，这种家伙居然当上了学生会长，\x01",
            "看来这世道也快到头了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈☆\x01",
            "嗯，看来的确很好玩。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#018F#1P等、等一下！\x01",
            "照你们这样说的话……\x02\x03",
            "那个非我莫属的\x01",
            "『重要角色』难道是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#731F哎呀，你能参与可真是帮了大忙呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#641F科洛丝，多谢你啦。\x01",
            "介绍了这么好的两个人来㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F#4P啊、啊哈哈……\x02\x03",
            "对不起呢，约修亚……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_28(0x3D, 0x1, 0x20)
    OP_28(0x3D, 0x1, 0x40)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2513   ._SN", 113, 0, 0)
    IdleLoop()
    Return()

    # Function_15_252A end

    def Function_16_3AE9(): pass

    label("Function_16_3AE9")

    EventBegin(0x0)
    OP_6D(6500, 0, -150, 0)
    OP_77(0xFF, 0xC8, 0x96, 0x0, 0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x105, 6070, 100, -420, 180)
    SetChrPos(0x101, 6070, 100, -2400, 0)
    SetChrPos(0x8, 5150, 0, -260, 180)
    SetChrChipByIndex(0x101, 8)
    SetChrChipByIndex(0x105, 10)
    SetChrPos(0x102, -230, -250, -7260, 0)
    SetChrPos(0x9, 280, -250, -6290, 0)
    OP_62(0x101, 0x0, 1850, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x105, 0x0, 1850, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    OP_62(0x101, 0x0, 1850, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x105, 0x0, 1850, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)

    def lambda_3C0B():
        OP_6D(5210, 0, -1580, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3C0B)

    def lambda_3C23():
        OP_8E(0xFE, 0x8E8, 0x0, 0xFFFFF8EE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3C23)
    Sleep(500)

    def lambda_3C43():
        OP_8E(0xFE, 0x8FC, 0x0, 0xFFFFF4AC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C43)
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0x105, 2)

    def lambda_3C68():

        label("loc_3C68")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_3C68")

    QueueWorkItem2(0x8, 1, lambda_3C68)
    WaitChrThread(0x9, 0x1)

    def lambda_3C7E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3C7E)
    WaitChrThread(0x102, 0x1)

    def lambda_3C91():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C91)
    Sleep(500)
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    OP_62(0x101, 0x0, 1850, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x105, 0x0, 1850, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "中午，他们就和大家一起在饭堂里\x01",
            "共进午餐、谈天说地……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2513   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3AE9 end

    def Function_17_3DAA(): pass

    label("Function_17_3DAA")

    OP_A3(0xD)
    OP_A3(0xE)
    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x13, 0x80)
    OP_64(0x2, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "卢安经济史·上\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x33D, 1)
    OP_28(0x27, 0x1, 0x40)
    TalkEnd(0xFF)
    Return()

    # Function_17_3DAA end

    def Function_18_3E17(): pass

    label("Function_18_3E17")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【归还卢安经济史】\x01",      # 0
            "【不归还】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E8F"),
        (1, "loc_3FA9"),
        (SWITCH_DEFAULT, "loc_3FAC"),
    )


    label("loc_3E8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_END)), "loc_3EEB")
    OP_3F(0x33D, 1)
    OP_28(0x27, 0x1, 0x200)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "卢安经济史·上\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3EEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_END)), "loc_3F48")
    OP_3F(0x33E, 1)
    OP_28(0x27, 0x1, 0x400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "卢安经济史·中\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3F48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_END)), "loc_3FA6")
    OP_3F(0x33F, 1)
    OP_28(0x27, 0x1, 0x800)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "卢安经济史·下\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3FA6")

    Jump("loc_3FAC")

    label("loc_3FA9")

    Jump("loc_3FAC")

    label("loc_3FAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FC5")
    OP_64(0x0, 0x1)

    label("loc_3FC5")

    TalkEnd(0xFF)
    Return()

    # Function_18_3E17 end

    def Function_19_3FC9(): pass

    label("Function_19_3FC9")

    SetPlaceName(0x71) # 社团大楼　学生会室
    Return()

    # Function_19_3FC9 end

    def Function_20_3FCD(): pass

    label("Function_20_3FCD")

    SetPlaceName(0x72) # 社团大楼　学生会室
    Return()

    # Function_20_3FCD end

    def Function_21_3FD1(): pass

    label("Function_21_3FD1")

    SetPlaceName(0x75) # 社团大楼　学生会室
    Return()

    # Function_21_3FD1 end

    def Function_22_3FD5(): pass

    label("Function_22_3FD5")

    SetPlaceName(0x70) # 社团大楼　学生会室
    Return()

    # Function_22_3FD5 end

    SaveToFile()

Try(main)
