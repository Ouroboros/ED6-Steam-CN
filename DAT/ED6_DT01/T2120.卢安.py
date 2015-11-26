from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2120   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2120   ._SN',
            'ED6_DT01/T2120_1 ._SN',
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
        '嘉恩',                                 # 9
        '卡露娜',                               # 10
        '阿加特',                               # 11
        '索姆茨',                               # 12
        '加鲁诺',                               # 13
        '扎古',                                 # 14
        '爱珐',                                 # 15
        '妮吉塔',                               # 16
        '梅尔茨',                               # 17
        '欧尼尔',                               # 18
        '西加罗',                               # 19
        '艾德尔',                               # 20
        '目标用摄像机',                         # 21
        '玻璃杯',                               # 22
        '吉米',                                 # 23
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
        'ED6_DT07/CH01240 ._CH',             # 00
        'ED6_DT07/CH02400 ._CH',             # 01
        'ED6_DT06/CH20053 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01190 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01210 ._CH',             # 06
        'ED6_DT07/CH01590 ._CH',             # 07
        'ED6_DT07/CH01760 ._CH',             # 08
        'ED6_DT07/CH01100 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT06/CH20021 ._CH',             # 0C
        'ED6_DT06/CH20034 ._CH',             # 0D
        'ED6_DT07/CH01040 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH01240P._CP',             # 00
        'ED6_DT07/CH02400P._CP',             # 01
        'ED6_DT06/CH20053P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01190P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01210P._CP',             # 06
        'ED6_DT07/CH01590P._CP',             # 07
        'ED6_DT07/CH01760P._CP',             # 08
        'ED6_DT07/CH01100P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT06/CH20021P._CP',             # 0C
        'ED6_DT06/CH20034P._CP',             # 0D
        'ED6_DT07/CH01040P._CP',             # 0E
    )

    DeclNpc(
        X                   = -5700,
        Z                   = 0,
        Y                   = 45100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -400,
        Z                   = 0,
        Y                   = 45400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -30000,
        Z                   = 0,
        Y                   = 4910,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 3100,
        Z                   = 4000,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 42600,
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
        X                   = 1200,
        Z                   = 0,
        Y                   = 5000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 5360,
        Z                   = 4000,
        Y                   = 5510,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -38000,
        Z                   = 0,
        Y                   = 47490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 29900,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 31800,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28500,
        Z                   = 0,
        Y                   = 700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x81,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917516,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 28570,
        Z                   = 0,
        Y                   = 1980,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )


    DeclActor(
        TriggerX            = 1070,
        TriggerZ            = 0,
        TriggerY            = 43260,
        TriggerRange        = 1400,
        ActorX              = 1070,
        ActorZ              = 2000,
        ActorY              = 43260,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30020,
        TriggerZ            = 0,
        TriggerY            = 3590,
        TriggerRange        = 400,
        ActorX              = -30000,
        ActorZ              = 1500,
        ActorY              = 4910,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1020,
        TriggerZ            = 0,
        TriggerY            = 3000,
        TriggerRange        = 400,
        ActorX              = 1200,
        ActorZ              = 1500,
        ActorY              = 5000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29980,
        TriggerZ            = 0,
        TriggerY            = 3310,
        TriggerRange        = 400,
        ActorX              = 29900,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4420,
        TriggerZ            = 0,
        TriggerY            = 45090,
        TriggerRange        = 600,
        ActorX              = -5700,
        ActorZ              = 1500,
        ActorY              = 45100,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3B6",          # 00, 0
        "Function_1_5AE",          # 01, 1
        "Function_2_60F",          # 02, 2
        "Function_3_625",          # 03, 3
        "Function_4_631",          # 04, 4
        "Function_5_FEA",          # 05, 5
        "Function_6_1C75",         # 06, 6
        "Function_7_1D12",         # 07, 7
        "Function_8_1D17",         # 08, 8
        "Function_9_27E6",         # 09, 9
        "Function_10_2A78",        # 0A, 10
        "Function_11_2C3C",        # 0B, 11
        "Function_12_3D4D",        # 0C, 12
        "Function_13_43E7",        # 0D, 13
        "Function_14_4763",        # 0E, 14
        "Function_15_4768",        # 0F, 15
        "Function_16_5685",        # 10, 16
        "Function_17_5777",        # 11, 17
        "Function_18_57E0",        # 12, 18
        "Function_19_5888",        # 13, 19
        "Function_20_60C5",        # 14, 20
        "Function_21_732D",        # 15, 21
        "Function_22_79A7",        # 16, 22
        "Function_23_998D",        # 17, 23
        "Function_24_A1AC",        # 18, 24
        "Function_25_B831",        # 19, 25
    )


    def Function_0_3B6(): pass

    label("Function_0_3B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3F1")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E4")
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    Jump("loc_3EE")

    label("loc_3E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3EE")

    label("loc_3EE")

    Jump("loc_523")

    label("loc_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_436")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_429")
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    Jump("loc_433")

    label("loc_429")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_433")

    label("loc_433")

    Jump("loc_523")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_47B")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E")
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    Jump("loc_478")

    label("loc_46E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_478")

    label("loc_478")

    Jump("loc_523")

    label("loc_47B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4A5")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrPos(0x9, -36210, 0, 41450, 270)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_523")

    label("loc_4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_4CD")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_523")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_4F2")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrPos(0x9, -36210, 0, 41450, 270)
    Jump("loc_523")

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_512")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x9, -36400, 0, 41270, 270)
    Jump("loc_523")

    label("loc_512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_523")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)

    label("loc_523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_532")
    SetChrFlags(0xC, 0x80)
    Jump("loc_53F")

    label("loc_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53F")
    SetChrFlags(0xC, 0x80)

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_54D")
    OP_A3(0x3FA)
    Event(0, 23)

    label("loc_54D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_55B")
    OP_A3(0x3FB)
    Event(0, 24)

    label("loc_55B")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_567"),
        (SWITCH_DEFAULT, "loc_5AD"),
    )


    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_576")
    OP_A2(0x414)
    Event(0, 19)

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_597")
    OP_A2(0x418)
    Event(0, 20)
    SetMapFlags(0x10000000)
    OP_B1("t2120_n")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    OP_A2(0x42D)
    Event(0, 22)

    label("loc_5AA")

    Jump("loc_5AD")

    label("loc_5AD")

    Return()

    # Function_0_3B6 end

    def Function_1_5AE(): pass

    label("Function_1_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C3")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E4")
    OP_B1("t2120_y")
    Jump("loc_5ED")

    label("loc_5E4")

    OP_B1("t2120_n")

    label("loc_5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FE")
    OP_1B(0x6, 0x0, 0x19)
    OP_64(0x4, 0x1)

    label("loc_5FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_60E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60E")

    Return()

    # Function_1_5AE end

    def Function_2_60F(): pass

    label("Function_2_60F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_624")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_60F")

    label("loc_624")

    Return()

    # Function_2_60F end

    def Function_3_625(): pass

    label("Function_3_625")

    Call(0, 4)
    OP_8C(0xB, 180, 0)
    Return()

    # Function_3_625 end

    def Function_4_631(): pass

    label("Function_4_631")

    TalkBegin(0xB)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "离开\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69C")
    OP_0D()
    OP_A9(0x1E)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_69C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AD")
    TalkEnd(0xB)
    Return()

    label("loc_6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_6F4")

    ChrTalk(
        0xB,
        "辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "那么，\x01",
            "以后有什么事情还得拜托你们哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_6F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_716")
    Call(1, 1)
    Jump("loc_FE6")

    label("loc_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7B1")

    ChrTalk(
        0xB,
        (
            "市长被逮捕了，\x01",
            "真让人松了一口气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "戴尔蒙家族没有继承人，\x01",
            "下一任的市长是不是\x01",
            "必须要全民公选了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_7B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_90C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_874")
    OP_A2(0x0)

    ChrTalk(
        0xB,
        (
            "听说传闻中的公爵要到这一带来视察，\x01",
            "我就去看了一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "结果根本没有那样一个人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "倒是有一个穿着奇装异服的大叔\x01",
            "一直在用奇怪的说话方式叫嚷着。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_909")

    label("loc_874")


    ChrTalk(
        0xB,
        (
            "听说传闻中的公爵要到这一带来视察，\x01",
            "我就去看了一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我没有看到公爵，\x01",
            "倒是有一个穿着奇装异服的大叔在吵吵嚷嚷的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_909")

    Jump("loc_FE6")

    label("loc_90C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_ACB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4D")
    OP_A2(0x0)

    ChrTalk(
        0xB,
        (
            "戴尔蒙市长虽然\x01",
            "极力推进旅游业……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "但是采取了强硬的措施，\x01",
            "反对者也不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "希望他能够和本地居民\x01",
            "相处得再融洽一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……在推动旅游事业之前，\x01",
            "应该先对渡鸦帮采取些措施才对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "有他们这些人在，\x01",
            "不正是给作为旅游胜地的卢安抹黑吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC8")

    label("loc_A4D")


    ChrTalk(
        0xB,
        (
            "在推动旅游事业之前，\x01",
            "应该先对渡鸦帮采取些措施才对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "有他们这些人在，\x01",
            "不正是给作为旅游胜地的卢安抹黑吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC8")

    Jump("loc_FE6")

    label("loc_ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_B70")

    ChrTalk(
        0xB,
        (
            "最近，\x01",
            "王立学院的学生们\x01",
            "来买了不少照明和烹饪的器具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "这么说的话……\x01",
            "就快要到学园祭的时候了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C20")
    OP_A2(0x0)

    ChrTalk(
        0xB,
        (
            "啊……\x01",
            "快到吃午饭的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "饿着肚子可没法做生意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "真想吃啊……\x01",
            "卢安的孩子们最喜欢的\x01",
            "加了许多虾的杂菜烩饭。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C43")

    label("loc_C20")


    ChrTalk(
        0xB,
        (
            "啊……\x01",
            "快到吃午饭的时间了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C43")

    Jump("loc_FE6")

    label("loc_C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_DFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5A")
    OP_A2(0x0)

    ChrTalk(
        0xB,
        "我听嘉恩那小子说了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "昨天有一位王族出身的人物\x01",
            "来到卢安了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "那位与艾莉茜雅女王\x01",
            "拥有相同血统的人\x01",
            "一定是位举止高雅的人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "趁他在卢安的时候，\x01",
            "我一定要去见见他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF7")

    label("loc_D5A")


    ChrTalk(
        0xB,
        (
            "昨天有一位王族出身的人物\x01",
            "来到卢安了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "与艾莉茜雅女王拥有相同血统，\x01",
            "一定是位举止高雅的人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF7")

    Jump("loc_FE6")

    label("loc_DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_E7B")

    ChrTalk(
        0xB,
        (
            "你们去看过伦格兰德大桥了吗？\x01",
            "那里很值得一看哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不管怎么说，\x01",
            "它可是这座城市的标志。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_FE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5D")
    OP_A2(0x0)

    ChrTalk(
        0xB,
        "今天的观光客特别多。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "听说如果没有向酒店预订房间，\x01",
            "是没办法在酒店里住下来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "说起来在以前，\x01",
            "那些没有地方住宿的客人，\x01",
            "游击士协会会向他们提供住所。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_F5D")


    ChrTalk(
        0xB,
        "今天的观光客特别多。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "听说如果没有向酒店预订房间，\x01",
            "是没办法在酒店里住下来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE6")

    TalkEnd(0xB)
    Return()

    # Function_4_631 end

    def Function_5_FEA(): pass

    label("Function_5_FEA")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x67)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FFF")
    EventBegin(0x0)

    label("loc_FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1064")

    ChrTalk(
        0xFE,
        "今天谢谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再有什么事情的话，\x01",
            "还得麻烦你们哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_1064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_148A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1116")

    ChrTalk(
        0xFE,
        "呀，之前真是帮了我大忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "后来我这边的工作\x01",
            "也进行得很顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "差不多该回蔡斯去了。\x01",
            "要赶快把零碎的事情做完。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1487")

    label("loc_1116")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_11FF")

    ChrTalk(
        0xFE,
        (
            "如果在阿伊纳街道周围\x01",
            "找到导力枪的话，\x01",
            "就拿过来给我看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那可能是我\x01",
            "丢失的试制品也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我打算马上就回蔡斯去。\x01",
            "所以请尽量快一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1487")

    label("loc_11FF")


    ChrTalk(
        0xFE,
        (
            "为了对正在开发中的\x01",
            "导力枪进行市场调查，\x01",
            "我从蔡斯来到这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "途经阿伊纳街道的时候\x01",
            "遭到凶暴魔兽的追击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我丢下装有重要试制品的袋子，\x01",
            "好不容易逃到了这里。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_13C7")
    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)

    ChrTalk(
        0x101,
        (
            "#000F啊，我们从公告板上看到了。\x02\x03",
            "丢失的是试制的导力枪吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "拜托你们把它找回来。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1487")

    label("loc_13C7")

    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x4, 0x2)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)

    ChrTalk(
        0x101,
        "#002F和游击士协会联络了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "是啊，而且很快就安排好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公告板上也应该出来了，\x01",
            "一旦找到了请赶快来通知我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1487")

    Jump("loc_1C5D")

    label("loc_148A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_189D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_151F")

    ChrTalk(
        0xFE,
        "呀，之前真是帮了大忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "后来我这边的工作\x01",
            "也进行得很顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么……\x01",
            "我就先去工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189A")

    label("loc_151F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1612")

    ChrTalk(
        0xFE,
        (
            "如果在阿伊纳街道周围\x01",
            "找到导力枪的话，\x01",
            "就拿过来给我看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那可能是我\x01",
            "丢失的试制品也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么……\x01",
            "这个先放一边，工作要紧啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189A")

    label("loc_1612")


    ChrTalk(
        0xFE,
        (
            "为了对正在开发中的\x01",
            "导力枪进行市场调查，\x01",
            "我从蔡斯来到这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "途经阿伊纳街道的时候\x01",
            "遭到凶暴魔兽的追击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我丢下装有重要试制品的袋子，\x01",
            "好不容易逃到了这里。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_17DA")
    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)

    ChrTalk(
        0x101,
        (
            "#000F啊，我们从公告板上看到了。\x02\x03",
            "丢失的是试制的导力枪吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "拜托你们把它找回来。\x02",
    )

    CloseMessageWindow()
    Jump("loc_189A")

    label("loc_17DA")

    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x4, 0x2)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)

    ChrTalk(
        0x101,
        "#002F和游击士协会联络了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "是啊，而且很快就安排好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公告板上也应该出来了，\x01",
            "一旦找到了请赶快来通知我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189A")

    Jump("loc_1C5D")

    label("loc_189D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_1C5D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1937")

    ChrTalk(
        0xFE,
        "呀，之前真是帮了大忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "后来我这边的工作\x01",
            "也进行得很顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再有什么事的话，\x01",
            "到时候还得麻烦你们呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_1937")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_19DE")

    ChrTalk(
        0xFE,
        (
            "如果在阿伊纳街道周围\x01",
            "找到导力枪的话，\x01",
            "就拿过来给我看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那可能是我\x01",
            "丢失的试制品也说不定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_19DE")


    ChrTalk(
        0xFE,
        (
            "为了对正在开发中的\x01",
            "导力枪进行市场调查，\x01",
            "我从蔡斯来到这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "途经阿伊纳街道的时候\x01",
            "遭到凶暴魔兽的追击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我丢下装有重要试制品的袋子，\x01",
            "好不容易逃到了这里。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1B9D")
    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)

    ChrTalk(
        0x101,
        (
            "#000F啊，我们从公告板上看到了。\x02\x03",
            "丢失的是试制的导力枪吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "拜托你们把它找回来。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_1B9D")

    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x4, 0x2)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)

    ChrTalk(
        0x101,
        "#002F和游击士协会联络了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "是啊，而且很快就安排好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公告板上也应该出来了，\x01",
            "一旦找到了请赶快来通知我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x67)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C71")
    Call(1, 4)

    label("loc_1C71")

    TalkEnd(0xC)
    Return()

    # Function_5_FEA end

    def Function_6_1C75(): pass

    label("Function_6_1C75")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_1D0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF5")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "哈……哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从玛诺利亚村\x01",
            "一口气走到这里，\x01",
            "果然很累人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D0E")

    label("loc_1CF5")


    ChrTalk(
        0xFE,
        "哈……哈……\x02",
    )

    CloseMessageWindow()

    label("loc_1D0E")

    TalkEnd(0xD)
    Return()

    # Function_6_1C75 end

    def Function_7_1D12(): pass

    label("Function_7_1D12")

    Call(0, 8)
    Return()

    # Function_7_1D12 end

    def Function_8_1D17(): pass

    label("Function_8_1D17")

    TalkBegin(0xE)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D83")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_1D78")
    OP_A9(0x32)
    Jump("loc_1D7A")

    label("loc_1D78")

    OP_A9(0x1F)

    label("loc_1D7A")

    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_1D83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D94")
    TalkEnd(0xE)
    Return()

    label("loc_1D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1E29")

    ChrTalk(
        0xE,
        "呼～是戴尔蒙市长啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "虽然我很讨厌他那种\x01",
            "做作的演技和态度，\x01",
            "可是没想到他会做到这种地步……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_1E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1FE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3B")
    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "刚才在街上有一个\x01",
            "发型很奇怪的大叔向我搭讪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "虽然他看上去很有钱，\x01",
            "但是他太随便，不是个品德高尚的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "是卢安男人的素质都下降了呢。\x01",
            "还是说他只是个观光客……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FE2")

    label("loc_1F3B")


    ChrTalk(
        0xE,
        (
            "刚才在街上有一个\x01",
            "发型很奇怪的大叔向我搭讪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "是卢安男人的素质都下降了呢。\x01",
            "还是说他只是个观光客……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE2")

    Jump("loc_27E2")

    label("loc_1FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2186")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2145")
    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "妹妹她们的学园祭\x01",
            "真是让我很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过那孩子好像\x01",
            "不太愿意让我去看……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "呵呵，这是监护人的义务呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "我很认真地观赏了\x01",
            "她们的舞台剧哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2183")

    label("loc_2145")


    ChrTalk(
        0xE,
        (
            "妹妹她们的学园祭\x01",
            "真是让我很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2183")

    Jump("loc_27E2")

    label("loc_2186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2219")

    ChrTalk(
        0xE,
        "呼呼，马上就要到学园祭了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "我妹妹好像也要在舞台剧中登场，\x01",
            "不知道她到底演的是什么角色。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_2219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_248B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_239B")
    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "在百日战役中王国军的事迹\x01",
            "被宣传得轰轰烈烈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过实际上，\x01",
            "都是靠某位上校制定的作战计划\x01",
            "赶走帝国军的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "但是，\x01",
            "那位上校现在在哪里做什么，\x01",
            "我就完全没有听说过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "嘿嘿，我很想知道他是个怎样的人。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2488")

    label("loc_239B")


    ChrTalk(
        0xE,
        (
            "百日战役中，\x01",
            "就是靠某位上校制定的作战计划\x01",
            "赶走帝国军的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "但是，\x01",
            "那位上校现在在哪里做什么，\x01",
            "我就完全没有听说过了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2488")

    Jump("loc_27E2")

    label("loc_248B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2509")

    ChrTalk(
        0xE,
        (
            "嘿嘿，我来到这个城市\x01",
            "已经有十年了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过只有年龄在增长，\x01",
            "却没有干成什么事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_2509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_26D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2634")
    OP_A2(0x3)

    ChrTalk(
        0xE,
        "呵呵，游击士真辛苦呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "拥有很大权限的同时\x01",
            "也背负了很大的责任啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "有责任感的人\x01",
            "才能成为可靠的游击士啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过这样的人有时也会\x01",
            "为某件事过分自责而消沉下去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D3")

    label("loc_2634")


    ChrTalk(
        0xE,
        (
            "有责任感的人\x01",
            "才能成为可靠的游击士啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过这样的人有时也会\x01",
            "为某件事过分自责而消沉下去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D3")

    Jump("loc_27E2")

    label("loc_26D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_27E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B0")
    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "啊～欢迎光临。\x01",
            "好可爱的游击士呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "……不对，那个徽章，\x01",
            "确切地说应该是准游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎～你知道得真清楚呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "呵呵，我的阅历可是不浅的哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_27B0")


    ChrTalk(
        0xE,
        (
            "呵呵，欢迎欢迎。\x01",
            "两位可爱的准游击士。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E2")

    TalkEnd(0xE)
    Return()

    # Function_8_1D17 end

    def Function_9_27E6(): pass

    label("Function_9_27E6")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_284A")

    ChrTalk(
        0xFE,
        (
            "学校放假\x01",
            "就到今天为止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明天开始又要上课了，\x01",
            "我要去准备一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A74")

    label("loc_284A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2A74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A17")
    OP_A2(0x4)
    TurnDirection(0xFE, 0x136, 0)

    ChrTalk(
        0xFE,
        (
            "咦，科洛丝前辈。\x01",
            "来卢安有什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F嗯，\x01",
            "我正在带两位朋友参观这里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（是她在学院里的同学吗？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（嗯，应该没错。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F妮吉塔今天\x01",
            "在家里休息是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "今天没有社团活动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，前辈。\x01",
            "『那个』已经决定了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#045F还、还没有呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是吗……\x01",
            "如果能早点决定就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F（『那个』是什么呢……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A74")

    label("loc_2A17")

    TurnDirection(0xFE, 0x136, 0)

    ChrTalk(
        0xFE,
        (
            "科洛丝前辈，\x01",
            "难得来城里一次，\x01",
            "就好好逛逛街吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A74")

    TalkEnd(0xF)
    Return()

    # Function_9_27E6 end

    def Function_10_2A78(): pass

    label("Function_10_2A78")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "报告\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C26")
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x22)"), scpexpr(EXPR_END)), "loc_2B77")
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#650F辛苦了。\x01",
            "看来目的顺利地达成了呢。\x02\x03",
            "如果完成其他任务的话，\x01",
            "随时都可以来向我报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C1D")

    label("loc_2B77")

    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#650F你们现在好像\x01",
            "没有需要报告的任务哦。\x02\x03",
            "如果完成其他任务的话，\x01",
            "随时都可以来向我报告。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C1D")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_2C26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C37")
    TalkEnd(0x8)
    Return()

    label("loc_2C37")

    Call(0, 11)
    Return()

    # Function_10_2A78 end

    def Function_11_2C3C(): pass

    label("Function_11_2C3C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2D63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D13")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#650F这就准备前往蔡斯地区了吗？\x01",
            "　\x02\x03",
            "如果在蔡斯能找到\x01",
            "黑色导力器的线索就好了。\x02\x03",
            "#651F期待你们能早日成为正游击士，\x01",
            "并让我们也沾沾光，\x01",
            "好让大家一起庆祝一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D60")

    label("loc_2D13")


    ChrTalk(
        0x8,
        (
            "#654F不过这样一来\x01",
            "卢安这边就变得麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D60")

    Jump("loc_3D49")

    label("loc_2D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2DF7")

    ChrTalk(
        0x8,
        (
            "#652F明白了吗？\x01",
            "总之靠你们帮我拖延时间了。\x02\x03",
            "在王国军赶到之前\x01",
            "一定要想办法留住市长。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D49")

    label("loc_2DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_304C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F7C")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#653F啊呀，是你们啊……\x01",
            "院长的事情我已经听说了。\x02\x03",
            "#652F很不巧，梅尔茨出去办事了，\x01",
            "阿加特也去调查了，还没有回来。\x02\x03",
            "虽然学院的工作才刚结束，\x01",
            "不过很抱歉，\x01",
            "你们能马上去一次玛诺利亚村吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯，交给我们吧！\x01",
            "您不用这么客气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F那要赶快上路了。\x01",
            "我也很担心卡露娜小姐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_2F7C")


    ChrTalk(
        0x8,
        (
            "#652F很不巧，梅尔茨出去办事了，\x01",
            "阿加特也去调查了，还没有回来。\x02\x03",
            "虽然学院的工作才刚结束，\x01",
            "不过很抱歉，\x01",
            "你们能马上去一次玛诺利亚村吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3049")

    Jump("loc_3D49")

    label("loc_304C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_3221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3156")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#650F对平民的协助、对地区的贡献，\x01",
            "这是一份非常有意义的好工作呢。\x02\x03",
            "希望你们出演学园祭的舞台剧，\x01",
            "这个委托我还是第一次碰到呢。\x02\x03",
            "#651F那么，我就等着你们的报告了。\x01",
            "加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_321E")

    label("loc_3156")


    ChrTalk(
        0x8,
        (
            "#650F对平民的协助、对地区的贡献，\x01",
            "这是一份非常有意义的好工作呢。\x02\x03",
            "希望你们出演学园祭的舞台剧，\x01",
            "这个委托我还是第一次碰到呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_321E")

    Jump("loc_3D49")

    label("loc_3221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_33BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3359")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#653F哦，是你们俩啊。\x01",
            "孤儿院那里怎样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F啊，那个……\x01",
            "虽然调查暂时告一个段落了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F不过碰到了一点麻烦……\x02\x03",
            "#010F稍后再过来提交工作报告。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652F……你们好像很急。\x01",
            "那我就等着你们的报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BA")

    label("loc_3359")


    ChrTalk(
        0x8,
        (
            "#652F有什么事情一会儿再来报告吧。\x01",
            "　\x02\x03",
            "你们现在不是有急事吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BA")

    Jump("loc_3D49")

    label("loc_33BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_3481")

    ChrTalk(
        0x8,
        (
            "#652F孤儿院发生了火灾，\x01",
            "而且院长和孩子们的情况还没有得以确认。\x01",
            "　\x02\x03",
            "这些都是你们\x01",
            "要进行详细调查的范围。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D49")

    label("loc_3481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3C4E")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -3490, 0, 45210, 270)
    SetChrPos(0x102, -3520, 0, 44250, 270)
    OP_6D(-5640, 0, 45060, 0)
    OP_8C(0x8, 90, 0)
    OP_4A(0x8, 255)
    OP_0D()

    ChrTalk(
        0x101,
        "#001F嘉恩哥哥，早啊～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F哟，早上好。\x01",
            "这么早就来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，约好的嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F抱歉有点心急了，\x01",
            "能安排一些工作给我们做吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651F嗯，没问题！\x02\x03",
            "有很多事想请你们帮忙来着，\x01",
            "嗯，选哪一件好呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F请、请手下留情……\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x0, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#653F哎……？\x01",
            "你们稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    def lambda_36B1():

        label("loc_36B1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_36B1")

    QueueWorkItem2(0x101, 2, lambda_36B1)

    def lambda_36C2():

        label("loc_36C2")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_36C2")

    QueueWorkItem2(0x102, 2, lambda_36C2)

    def lambda_36D3():
        OP_6D(-5530, 0, 45850, 1200)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_36D3)
    OP_8E(0x8, 0xFFFFE8A4, 0x0, 0xB6B2, 0xBB8, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(500)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x0, 0xFF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x83, 0x0, 0x64)
    OP_23(0xC3)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#650F您好，这里是游击士协会。\x02\x03",
            "哟，是白之木莲亭……\x01",
            "说来你们也很久没发联络过来了。\x02\x03",
            "你那里的古董通信器\x01",
            "竟然还能用啊……\x02\x03",
            "#653F………………………………\x02\x03",
            "#652F………………什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(
        0x8,
        (
            "#652F是吗……\x01",
            "这事可严重了。\x02\x03",
            "好，知道了。\x01",
            "我马上派人过去了解情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#002F怎么了？\x01",
            "出什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#652F现在还不知道是\x01",
            "事故还是人为的案件……\x02\x03",
            "昨天晚上， \x01",
            "海道边的孤儿院发生了火灾。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x56)

    ChrTalk(
        0x101,
        "#004F不、不会吧……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F已经确定了吗？\x02",
    )

    CloseMessageWindow()

    def lambda_3A2E():
        OP_6D(-5640, 0, 45060, 1200)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3A2E)
    OP_8E(0x8, 0xFFFFE9BC, 0x0, 0xB02C, 0xBB8, 0x0)
    OP_8C(0x8, 90, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x8,
        (
            "#652F是玛诺利亚旅店的主人\x01",
            "特地发了联络通知我们的。\x02\x03",
            "是座名叫玛西亚的孤儿院，\x01",
            "你们知道那里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F何、何止知道……\x01",
            "昨天下午我们还去过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F那么，\x01",
            "特蕾莎院长和那些孩子都还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652F这个还没确认。\x02\x03",
            "总之，要先去调查一下，\x01",
            "还要确认一下他们是否平安。\x02\x03",
            "……可以拜托你们去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F那还用说！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F那我们马上\x01",
            "赶去孤儿院了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#652F好，拜托了！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x41E)
    OP_28(0x3B, 0x4, 0x2)
    OP_28(0x3B, 0x4, 0x4)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Jump("loc_3D49")

    label("loc_3C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_3D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF3")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#650F哎呀，这个时候你们能来\x01",
            "真是帮了我大忙了。\x02\x03",
            "明天开始就会有很多的工作需要你们去做，\x01",
            "到时就拜托了。\x02\x03",
            "#651F请多关照！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D49")

    label("loc_3CF3")


    ChrTalk(
        0x8,
        (
            "#650F明天开始就会有很多的工作需要你们去做，\x01",
            "到时就拜托了。\x02\x03",
            "#651F请多关照！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D49")

    TalkEnd(0x8)
    Return()

    # Function_11_2C3C end

    def Function_12_3D4D(): pass

    label("Function_12_3D4D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3F4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EBB")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "#831F呀，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊，卡露娜姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F身体已经没什么事了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#830F啊，已经好了。\x01",
            "今天开始继续执行任务。\x02\x03",
            "#835F这次给你们两个\x01",
            "添了许多麻烦，\x01",
            "不向你们道谢就太说不过去了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F哪里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#830F你们成为正游击士后\x01",
            "一定要再来卢安玩啊。\x02\x03",
            "我等着你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F4C")

    label("loc_3EBB")


    ChrTalk(
        0xFE,
        (
            "#830F这次给你们两个\x01",
            "添了许多麻烦，\x01",
            "不向你们道谢就太说不过去了啊。\x02\x03",
            "你们成为正游击士后\x01",
            "一定要再来卢安玩啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F4C")

    Jump("loc_43E3")

    label("loc_3F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_404F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE8")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "#830F事情我都听嘉恩说了。\x02\x03",
            "学园祭的警卫工作\x01",
            "已经决定由我来负责了。\x02\x03",
            "那天就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_404C")

    label("loc_3FE8")


    ChrTalk(
        0xFE,
        (
            "#830F学园祭的警卫工作\x01",
            "已经决定由我来负责了。\x02\x03",
            "那天就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_404C")

    Jump("loc_43E3")

    label("loc_404F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_41DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4139")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "#835F最近到卢安来的\x01",
            "观光游客大大增加了。\x02\x03",
            "所以事件也多了不少，\x01",
            "护送旅客啊，寻找遗失物品啊，\x01",
            "真是忙死人了啊。\x02\x03",
            "哎呀～\x01",
            "你们能来真是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41D7")

    label("loc_4139")


    ChrTalk(
        0xFE,
        (
            "#835F最近到卢安来的\x01",
            "观光游客大大增加了。\x02\x03",
            "所以事件也多了不少，\x01",
            "护送旅客啊，寻找遗失物品啊，\x01",
            "真是忙死人了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41D7")

    Jump("loc_43E3")

    label("loc_41DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_435E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E3")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "#831F转属手续完成了吗？\x01",
            "今后我们就是同伴了哦。\x02\x03",
            "#833F这个支部除了我，\x01",
            "还有一个和你们一样\x01",
            "也是准游击士的同伴。\x02\x03",
            "听说那家伙是\x01",
            "临时调配过来的……\x02\x03",
            "……………………………………\x02\x03",
            "#830F呵呵，总之以后多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_435B")

    label("loc_42E3")


    ChrTalk(
        0xFE,
        (
            "#830F这个支部除了我，\x01",
            "还有一个和你们一样\x01",
            "也是准游击士的同伴。\x02\x03",
            "听说那家伙是\x01",
            "临时调配过来的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435B")

    Jump("loc_43E3")

    label("loc_435E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_43E3")

    ChrTalk(
        0xFE,
        (
            "#830F要办转属手续的话，\x01",
            "嘉恩不回来可办不了。\x02\x03",
            "不如先去街上逛逛，\x01",
            "打发一下时间如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43E3")

    TalkEnd(0x9)
    Return()

    # Function_12_3D4D end

    def Function_13_43E7(): pass

    label("Function_13_43E7")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_443F")

    ChrTalk(
        0xFE,
        "听说市长被捕了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……到底是怎么回事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_475F")

    label("loc_443F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_44CF")

    ChrTalk(
        0xFE,
        (
            "昨天，卡露娜小姐到学园做警卫之后，\x01",
            "到现在也没有回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是不是发生什么事情了呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_475F")

    label("loc_44CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_45B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_457E")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "卡露娜小姐去学园当警卫的时候，\x01",
            "我在这里也要努力才行！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……啊、啊嚏！\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "……唉，在这之前先要把感冒治好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_45B3")

    label("loc_457E")


    ChrTalk(
        0xFE,
        (
            "卡露娜小姐去学园当警卫的时候，\x01",
            "我在这里也要努力才行！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B3")

    Jump("loc_475F")

    label("loc_45B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_475F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B4")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "你们就是嘉恩所说的\x01",
            "从柏斯来的新人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我在考试中失败了许多次，\x01",
            "前几天终于成为了准游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我们互相加油吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_475F")

    label("loc_46B4")


    ChrTalk(
        0xFE,
        (
            "我在考试中失败了许多次，\x01",
            "前几天终于成为了准游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我们互相加油吧！\x02",
    )

    CloseMessageWindow()

    label("loc_475F")

    TalkEnd(0x10)
    Return()

    # Function_13_43E7 end

    def Function_14_4763(): pass

    label("Function_14_4763")

    Call(0, 15)
    Return()

    # Function_14_4763 end

    def Function_15_4768(): pass

    label("Function_15_4768")

    TalkBegin(0x11)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47E0")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_END)), "loc_47C9")
    OP_A9(0x2B)
    Jump("loc_47D7")

    label("loc_47C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_47D5")
    OP_A9(0x26)
    Jump("loc_47D7")

    label("loc_47D5")

    OP_A9(0x20)

    label("loc_47D7")

    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_47E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47F1")
    TalkEnd(0x11)
    Return()

    label("loc_47F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4997")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4925")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "没想到那个戴尔蒙市长\x01",
            "竟然被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "卢安的市长\x01",
            "可是由戴尔蒙家族\x01",
            "代代相传的职位啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "现在也没有其他继承人了，\x01",
            "市长这一被逮捕\x01",
            "不就什么都完了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "让我这个老者也为之震惊啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4994")

    label("loc_4925")


    ChrTalk(
        0x11,
        (
            "哎呀～活了这么久，\x01",
            "什么事情都见得差不多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "哇～哈～哈！\x02",
    )

    CloseMessageWindow()

    label("loc_4994")

    Jump("loc_5681")

    label("loc_4997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_4B83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AE7")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "在这片广阔的大陆上……\x01",
            "生活着很多国家的人们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "以你们的年龄来看，\x01",
            "说不定今后能有机会\x01",
            "去大陆各国巡游哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "与那些地方的人们见面，\x01",
            "语言交流是很重要的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "如果你们想成为像我这样心胸宽广，\x01",
            "而且崇高伟大的人的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "哇～哈～哈！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B80")

    label("loc_4AE7")


    ChrTalk(
        0x11,
        (
            "在这片广阔的大陆上……\x01",
            "生活着很多国家的人们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "以你们的年龄来看，\x01",
            "说不定今后能有机会\x01",
            "去大陆各国巡游哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B80")

    Jump("loc_5681")

    label("loc_4B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_4D3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA4")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "如今每次看到海，\x01",
            "我体内水手的血又沸腾起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "但是，\x01",
            "现在船的动力装置都变成导力器了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "虽然方便了不少，\x01",
            "但是总觉得有些失落……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "呼，\x01",
            "我现在也上了年纪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D3B")

    label("loc_4CA4")


    ChrTalk(
        0x11,
        (
            "现在船的动力装置\x01",
            "都变成导力器了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "虽然方便了不少，\x01",
            "但是总觉得有些失落……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D3B")

    Jump("loc_5681")

    label("loc_4D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC3")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "以前的埃雷波尼亚帝国的版图\x01",
            "不是现在这个样子的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "反复的侵略，\x01",
            "吞并了好几个国家与民族之后，\x01",
            "成为了现在这样的大国。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "在国内，皇家掌握着绝对的权力，\x01",
            "听说直到现在他们的统治也十分严厉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "连见惯大场面的我\x01",
            "通过那个国家的领土时\x01",
            "都会不禁紧张起来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "哇～哈～哈！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F01")

    label("loc_4EC3")


    ChrTalk(
        0x11,
        (
            "怎么样，\x01",
            "还想再听听我的冒险之旅吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F01")

    Jump("loc_5681")

    label("loc_4F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5199")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5158")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "那还是在共和国\x01",
            "附近海上航行的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "那个时候的共和国\x01",
            "政治还处于动荡的年代，\x01",
            "治安也非常不好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "突然，\x01",
            "载满客人的客船被海盗袭击了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "但是，作为海上男儿的我\x01",
            "碰巧也在这艘船上，\x01",
            "可谓是那些海盗的不幸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "我把他们狠狠地打了一顿，\x01",
            "狠狠地打……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "终于我把海盗们赶走了，\x01",
            "然后就沉浸于带有异国风情的\x01",
            "东方美女们的鼓掌喝彩声中了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "哇～哈～哈！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5196")

    label("loc_5158")


    ChrTalk(
        0x11,
        (
            "怎么样，\x01",
            "还想再听听我的冒险之旅吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5196")

    Jump("loc_5681")

    label("loc_5199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5398")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5301")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "这片大陆上有利贝尔、\x01",
            "埃雷波尼亚、卡尔瓦德\x01",
            "以及其他大大小小的国家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "在卡尔瓦德的东面\x01",
            "有着与利贝尔和埃雷波尼亚\x01",
            "不同的文化圈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "所以可以说共和国\x01",
            "是融合了东方和西方\x01",
            "各种不同文化的国家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "呵呵，我以前也是\x01",
            "驾船来往于各国之间的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5395")

    label("loc_5301")


    ChrTalk(
        0x11,
        (
            "在卡尔瓦德的东面\x01",
            "有着与利贝尔和埃雷波尼亚\x01",
            "不同的文化圈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "所以可以说共和国\x01",
            "是融合了东方和西方\x01",
            "各种不同文化的国家。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5395")

    Jump("loc_5681")

    label("loc_5398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_5566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54DE")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "别看我现在这个样子，\x01",
            "想当年我年轻气盛的时候曾经乘船到处冒险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "为了寻求珍贵宝物，\x01",
            "航海走遍了天涯海角呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "以前别人说起欧尼尔船长，\x01",
            "就是指小有名气的本店长哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "就说给你们听听吧。\x01",
            "我的那些光辉的冒险故事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5563")

    label("loc_54DE")


    ChrTalk(
        0x11,
        (
            "以前别人说起欧尼尔船长，\x01",
            "就是指小有名气的本店长哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "就说给你们听听吧。\x01",
            "我的那些光辉的冒险故事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5563")

    Jump("loc_5681")

    label("loc_5566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_5681")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5625")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        "咳咳！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "我年轻的时候\x01",
            "曾经只身单船出海，\x01",
            "周游各个国家做买卖呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "卢安原本就是个\x01",
            "聚集了如此多\x01",
            "热血男人的地方啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5681")

    label("loc_5625")


    ChrTalk(
        0x11,
        (
            "我年轻的时候\x01",
            "曾经只身单船出海，\x01",
            "周游各个国家做买卖呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5681")

    TalkEnd(0x11)
    Return()

    # Function_15_4768 end

    def Function_16_5685(): pass

    label("Function_16_5685")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5707")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "最初明明说\x01",
            "只是来看看的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "最终，还是买了不少东西。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5773")

    label("loc_5707")


    ChrTalk(
        0xFE,
        (
            "不过说起来，\x01",
            "这里的店长话还真多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从我们来了之后\x01",
            "就一直讲个不停。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5773")

    TalkEnd(0x12)
    Return()

    # Function_16_5685 end

    def Function_17_5777(): pass

    label("Function_17_5777")

    TalkBegin(0x13)

    ChrTalk(
        0xFE,
        (
            "难得来一次，\x01",
            "光看可不行啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_17_5777 end

    def Function_18_57E0(): pass

    label("Function_18_57E0")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5850")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "还没有找到合适的地图。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再去找欧尼尔爷爷\x01",
            "商量一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5884")

    label("loc_5850")


    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "没有再好点的地图吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5884")

    TalkEnd(0x16)
    Return()

    # Function_18_57E0 end

    def Function_19_5888(): pass

    label("Function_19_5888")

    EventBegin(0x0)
    OP_6D(-20, 0, 40420, 0)
    OP_6B(2800, 0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x101, -170, 0, 40420, 0)
    SetChrPos(0x102, 790, 0, 39400, 0)
    SetChrPos(0x136, -610, 0, 39400, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#000F打扰了～\x02",
    )

    CloseMessageWindow()
    OP_6D(-2850, 0, 44550, 1000)

    def lambda_5917():
        OP_8E(0xFE, 0xFFFFF3B2, 0x0, 0xACB2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5917)

    def lambda_5932():

        label("loc_5932")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_5932")

    QueueWorkItem2(0x101, 1, lambda_5932)
    Sleep(400)

    def lambda_5948():
        OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xA7A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_5948)

    def lambda_5963():

        label("loc_5963")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_5963")

    QueueWorkItem2(0x136, 1, lambda_5963)
    Sleep(300)

    def lambda_5979():
        OP_8E(0xFE, 0xFFFFF8D0, 0x0, 0xAA78, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5979)

    def lambda_5994():

        label("loc_5994")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_5994")

    QueueWorkItem2(0x102, 1, lambda_5994)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x101,
        "#004F哎？负责人呢？\x02",
    )

    CloseMessageWindow()
    OP_4A(0x9, 255)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x9, 225, 400)

    ChrTalk(
        0x9,
        (
            "啊，小姑娘。\x01",
            "你们有什么委托吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊……\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x136, 0x1)

    def lambda_5A3C():

        label("loc_5A3C")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5A3C")

    QueueWorkItem2(0x101, 1, lambda_5A3C)

    def lambda_5A4D():

        label("loc_5A4D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5A4D")

    QueueWorkItem2(0x102, 1, lambda_5A4D)

    def lambda_5A5E():

        label("loc_5A5E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5A5E")

    QueueWorkItem2(0x136, 1, lambda_5A5E)
    OP_8E(0x9, 0xFFFFF5EC, 0x0, 0xB0CC, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x136, 0x1)

    ChrTalk(
        0x9,
        (
            "#830F负责接待的嘉恩\x01",
            "正在二楼和客人谈话。\x02\x03",
            "如果有什么事情，\x01",
            "可以先跟我说说吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊……\x01",
            "我们不是客人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#835F嗯？那个徽章……\x01",
            "原来你们是同行啊。\x02\x03",
            "#830F我叫卡露娜。\x01",
            "隶属于这个卢安支部。\x02\x03",
            "以前都没见过你们，是新人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯。\x01",
            "我是准游击士艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我是准游击士约修亚。\x01",
            "请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#830F艾丝蒂尔和约修亚……\x02\x03",
            "原来如此，\x01",
            "你们就是从洛连特来的新人吧。\x02\x03",
            "#831F听说你们和雪拉扎德一起\x01",
            "在柏斯有非常活跃的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊、啊哈哈……\x01",
            "也没那么了不起啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F请问您是不是\x01",
            "早就知道我们要来了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#831F是啊，因为嘉恩说过\x01",
            "会有两个有前途的新人过来。\x02\x03",
            "#830F不过要办理转属手续的话，\x01",
            "也只能等他办完事再说了。\x02\x03",
            "要不你们先在城里游览一下，\x01",
            "打发一下时间如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F说的也是……\x01",
            "反正在这里等着也做不了什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F我也赞成！\x02\x03",
            "#501F啊，对了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5ECD():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5ECD)
    Sleep(200)

    def lambda_5EE0():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5EE0)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#008F那个，如果可以的话，\x01",
            "你再陪我们一会儿好吗？\x02\x03",
            "好不容易才交到一个朋友\x01",
            "就这么分别太可惜了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(
        0x136,
        (
            "#041F嗯……我很乐意。\x02\x03",
            "#041F如果不会妨碍到你们的话，\x01",
            "我也很想带你们到处游览一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F太棒了⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那就这么决定了。\x02",
    )

    CloseMessageWindow()

    def lambda_6006():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6006)
    Sleep(200)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x102,
        (
            "#010F那么我们就先\x01",
            "在城里游览一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F过一会儿就回来哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "好啊，玩得开心点。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)
    OP_8E(0x9, 0xFFFFFE70, 0x0, 0xB158, 0x7D0, 0x0)
    OP_8C(0x9, 90, 400)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_19_5888 end

    def Function_20_60C5(): pass

    label("Function_20_60C5")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-3330, 0, 43680, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -160, 0, 39670, 315)
    SetChrPos(0x102, -100, 0, 40880, 315)
    SetChrPos(0x136, -1250, 0, 39900, 315)
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 135, 0)

    ChrTalk(
        0x8,
        (
            "#650F欢迎光临。\x01",
            "欢迎来到游击士协会！\x02\x03",
            "#653F啊，这不是科洛丝吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#040F您好，嘉恩先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F今天又是受校长之托，\x01",
            "来委托我们去消灭魔兽吗？\x02\x03",
            "#651F啊啊，我知道了！\x01",
            "是来委托我们做学园祭的警备吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#045F不是呢，\x01",
            "不过这件事迟早也要来麻烦你们。\x02\x03",
            "#040F今天我是为了\x01",
            "给艾丝蒂尔他们做向导而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#653F咦？说起来……\x01",
            "这两位好像不是学院的学生。\x02\x03",
            "等等，这徽章是……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6361():
        OP_8E(0xFE, 0xFFFFF222, 0x0, 0xB0FE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6361)

    def lambda_637C():

        label("loc_637C")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_637C")

    QueueWorkItem2(0x102, 1, lambda_637C)
    Sleep(200)

    def lambda_6392():
        OP_8E(0xFE, 0xFFFFF222, 0x0, 0xACBC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6392)

    def lambda_63AD():

        label("loc_63AD")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_63AD")

    QueueWorkItem2(0x101, 1, lambda_63AD)
    Sleep(800)

    def lambda_63C3():
        OP_6D(-4540, 0, 45010, 2000)
        ExitThread()

    QueueWorkItem(0x136, 3, lambda_63C3)

    def lambda_63DB():
        OP_8E(0xFE, 0xFFFFF1AA, 0x0, 0xA8C0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_63DB)
    Sleep(500)
    OP_8C(0x8, 90, 0)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x136, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x101,
        (
            "#000F#4P初次见面。\x01",
            "我是准游击士艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我是准游击士约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F啊啊……\x01",
            "你们就是艾丝蒂尔和约修亚啊！\x02\x03",
            "#651F哎呀～你们来了真是太好了！\x02\x03",
            "之前柏斯支部发来了联络，\x01",
            "说你们很快就会来到卢安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#4P是吗，原来卢格兰爷爷\x01",
            "已经帮我们打过招呼了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F下次见面得谢谢他呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F我叫嘉恩，\x01",
            "负责卢安支部的接待工作。\x02\x03",
            "今后我会全力支持你们的工作，\x01",
            "当然也包括对你们进行监督。\x02\x03",
            "还请你们多多关照哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4P嗯！\x01",
            "请多指教，嘉恩哥哥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请多指教。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651F呵呵，\x01",
            "我对你们抱有很大的期待哦。\x02\x03",
            "怎么说，你们可是漂亮地\x01",
            "解决那次空贼事件的最大功臣。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x136, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(
        0x136,
        (
            "#044F空贼事件……\x01",
            "是指柏斯地区发生的那件吗？\x02\x03",
            "#041F我在《利贝尔通讯》的\x01",
            "最新一期上看到这条新闻呢。\x02\x03",
            "原来，那个事件\x01",
            "是艾丝蒂尔你们解决的啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)
    TurnDirection(0x102, 0x136, 400)

    ChrTalk(
        0x101,
        (
            "#008F#4P啊哈哈，也不是……\x01",
            "我们只是帮了点忙而已啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F真正逮捕了空贼的\x01",
            "是王国军的部队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F呵呵，就别谦虚了。\x01",
            "卢格兰老爷子也对你们赞誉有佳。\x02\x03",
            "我马上就给你们办转属手续，\x01",
            "你们两个在这份文件上签个名吧。\x02\x03",
            "快快，就现在。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    OP_8C(0x102, 270, 400)
    OP_8C(0x136, 315, 400)

    ChrTalk(
        0x101,
        "#004F#4P嗯、嗯……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我们这就……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚\x01",
            "在转属手续的文书上签了字。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#651F嗯嗯，这样一来，\x01",
            "你们就隶属于卢安支部的了。\x02\x03",
            "哎呀，现在正是繁忙时期，\x01",
            "你们来卢安真是帮了我们大忙啊。\x02\x03",
            "呵呵……你们两个别想逃哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F#4P好、好像有点不好的预感。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们刚才已经听说了，\x01",
            "这里好像正处于人手不足的状况。\x02\x03",
            "是不是发生了什么事件呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#654F倒没有那么严重。\x02\x03",
            "其实，现在有位王家的大人物\x01",
            "正要来我们卢安市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#4P王家的大人物……\x02\x03",
            "#001F难、难道是女王陛下！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F哈哈，怎么可能。\x02\x03",
            "不过，来的人是王族成员，\x01",
            "这一点是肯定没错的。\x02\x03",
            "据说这位大人物\x01",
            "是来卢安市视察的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#4P哦～有这种人物在啊。\x02\x03",
            "可是可是，\x01",
            "这和人手不足又有什么关系呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F毕竟是王族成员啊。\x02\x03",
            "万一出什么意外可不得了啊，\x01",
            "而且戴尔蒙市长对这件事非常重视。\x02\x03",
            "所以他委托我们\x01",
            "强化卢安市街区的警备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此，\x01",
            "刚才在二楼谈的就是这件事吧。\x02\x03",
            "话说回来，有必要警戒街区吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#654F是啊……\x01",
            "还不是因为港口那边有些不安分的人。\x02\x03",
            "应该是想要我们\x01",
            "在这段时间里盯紧他们一点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#4P不安分的人……\x01",
            "就是刚才来闹事的那帮家伙吧。\x02\x03",
            "嗯～要是他们的话，\x01",
            "没准真会惹出什么事情来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#653F怎么，你们认识他们吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F其实是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚向嘉恩讲述了刚才发生的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#652F是吗……\x01",
            "原来你们去了仓库那里啊。\x02\x03",
            "那里是一个叫做\x01",
            "『渡鸦帮』的不良集团的据点。\x02\x03",
            "来找你们麻烦的大概是\x01",
            "充当集团首领的那群青年吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#4P『渡鸦帮』……\x01",
            "还真是适合那些坏蛋的名字呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#654F前一阵还挺老实的。\x01",
            "不过最近，他们的老毛病好像又发作了。\x02\x03",
            "市长的担心固然没错，\x01",
            "不过我们还必须把卢安\x01",
            "其他地区的工作都做好才行啊。\x02\x03",
            "#650F总之，就因为这样，\x01",
            "我们正为人手不足而发愁呢。\x02\x03",
            "你们来得正好，\x01",
            "多谢多谢，真是及时雨啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#4P啊哈哈……\x01",
            "我们不会辜负你的期待的。\x02\x03",
            "那么，从明天开始，\x01",
            "我们就参与这里的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F有什么事的话，\x01",
            "请不必客气尽管吩咐我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#651F好啊，拜托了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_20_60C5 end

    def Function_21_732D(): pass

    label("Function_21_732D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-1640, 0, 43790, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x102, -690, 0, 39780, 315)
    SetChrPos(0x101, 790, 0, 39400, 315)

    def lambda_7372():

        label("loc_7372")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_7372")

    QueueWorkItem2(0x101, 1, lambda_7372)

    def lambda_7383():

        label("loc_7383")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_7383")

    QueueWorkItem2(0x102, 1, lambda_7383)

    def lambda_7394():
        OP_6D(-5410, 0, 45570, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7394)

    def lambda_73AC():
        OP_8E(0xFE, 0xFFFFF380, 0x0, 0xB036, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_73AC)
    Sleep(500)

    def lambda_73CC():
        OP_8E(0xFE, 0xFFFFF380, 0x0, 0xABB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_73CC)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x101,
        "#000F#2P嘉恩哥哥，早啊～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F哟，早上好。\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F那当然啦☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F抱歉有点心急了，\x01",
            "能安排一些工作给我们做吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F嗯，没问题！\x02\x03",
            "有很多事想请你们帮忙来着，\x01",
            "嗯，选哪一件好呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F请、请手下留情……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F哎……？\x01",
            "你们稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFE8A4, 0x0, 0xB6B2, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)

    ChrTalk(
        0x8,
        (
            "#650F您好，这里是游击士协会。\x02\x03",
            "哟，是白之木莲亭……\x01",
            "说来你们也很久没发联络过来了。\x02\x03",
            "你那里的古董通信器\x01",
            "竟然还能用啊……\x02\x03",
            "………………………………\x02\x03",
            "………………什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F是吗……\x01",
            "这事可严重了。\x02\x03",
            "好，知道了。\x01",
            "我马上派人过去了解情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F怎么了？\x01",
            "出什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#650F现在还不知道是\x01",
            "事故还是人为的案件……\x02\x03",
            "昨天晚上， \x01",
            "海道边的孤儿院发生了火灾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F不、不会吧……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F已经确定了吗？\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFE9BC, 0x0, 0xB02C, 0xBB8, 0x0)
    OP_8C(0x8, 90, 800)

    ChrTalk(
        0x8,
        (
            "#650F是玛诺利亚旅店的主人\x01",
            "特地发了联络通知我们的。\x02\x03",
            "是座名叫玛西亚的孤儿院，\x01",
            "你们知道那里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F何、何止知道……\x01",
            "昨天下午我们还去过呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，\x01",
            "特蕾莎院长和那些孩子都还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F这个还没确认。\x02\x03",
            "总之，要先去调查一下，\x01",
            "还要确认一下他们是否平安。\x02\x03",
            "……可以拜托你们去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F那还用说！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那我们马上\x01",
            "赶去孤儿院了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#650F好，拜托了！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    EventEnd(0x0)
    Return()

    # Function_21_732D end

    def Function_22_79A7(): pass

    label("Function_22_79A7")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-4700, 0, 45110, 0)
    OP_6B(2800, 0)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x8, 255)
    SetChrPos(0x101, -170, 0, 40420, 0)
    SetChrPos(0x102, -610, 0, 39400, 0)
    SetChrPos(0x105, 790, 0, 39400, 0)

    def lambda_7A0A():

        label("loc_7A0A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_7A0A")

    QueueWorkItem2(0x8, 1, lambda_7A0A)

    def lambda_7A1B():

        label("loc_7A1B")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_7A1B")

    QueueWorkItem2(0x101, 1, lambda_7A1B)

    def lambda_7A2C():

        label("loc_7A2C")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_7A2C")

    QueueWorkItem2(0x102, 1, lambda_7A2C)

    def lambda_7A3D():

        label("loc_7A3D")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_7A3D")

    QueueWorkItem2(0x105, 1, lambda_7A3D)
    FadeToBright(1000, 0)

    def lambda_7A57():
        OP_8E(0xFE, 0xFFFFF2E0, 0x0, 0xB036, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A57)
    Sleep(400)

    def lambda_7A77():
        OP_8E(0xFE, 0xFFFFF236, 0x0, 0xAAFA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7A77)
    Sleep(100)

    def lambda_7A97():
        OP_8E(0xFE, 0xFFFFF588, 0x0, 0xACB2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7A97)
    WaitChrThread(0x105, 0x2)

    ChrTalk(
        0x8,
        (
            "#651F哟，辛苦了。\x02\x03",
            "看来那男孩\x01",
            "已经平安获救了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，总算还好。\x02\x03",
            "不过说起来真是吃了一惊。\x01",
            "想不到那个红头发的家伙也来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F哈哈，是说阿加特吗。\x02\x03",
            "他是为别的事情来卢安的，\x01",
            "刚才被我硬逼着去了你们那里。\x02\x03",
            "毕竟他曾经是\x01",
            "『渡鸦帮』的首领啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F果然是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F难怪那家伙看起来\x01",
            "一副粗鲁凶狠的样子啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#655F不过这也是过去的事了。\x02\x03",
            "他在和你们差不多大的时候\x01",
            "流浪到卢安来了……\x02\x03",
            "纠集了一帮天不怕地不怕的流氓，\x01",
            "在这个城市大闹了一阵子。\x02\x03",
            "#650F不过，和那时候相比的话，\x01",
            "现在的成员已经算很可爱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F这、这样的家伙\x01",
            "居然会当上了游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651F嗯，因为他和某个人的相遇，\x01",
            "让他完全地改变了自己。\x02\x03",
            "从那之后他就立志要做游击士，\x01",
            "而且，最后还靠自己的努力达成了。\x02\x03",
            "人啊，想变的话还是可以变的。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    SetChrPos(0xA, 0, 0, 39060, 0)
    ClearChrFlags(0xA, 0x80)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "……要说废话的话，\x01",
            "还是等回到家自己对着墙说个够吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)

    def lambda_7E94():

        label("loc_7E94")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_7E94")

    QueueWorkItem2(0x8, 1, lambda_7E94)

    def lambda_7EA5():

        label("loc_7EA5")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_7EA5")

    QueueWorkItem2(0x101, 2, lambda_7EA5)

    def lambda_7EB6():

        label("loc_7EB6")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_7EB6")

    QueueWorkItem2(0x102, 2, lambda_7EB6)

    def lambda_7EC7():

        label("loc_7EC7")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_7EC7")

    QueueWorkItem2(0x105, 2, lambda_7EC7)

    def lambda_7ED8():
        OP_6D(-4100, 0, 44500, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7ED8)
    OP_8E(0xA, 0xFFFFF57E, 0x0, 0xA62C, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        "#004F啊，回来了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#057F这个家伙， \x01",
            "老是在别人背后说三道四的……\x02\x03",
            "还是和以前一样八卦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651F哈哈，\x01",
            "这话我就当作是表扬好了。\x02\x03",
            "#650F话说回来，\x01",
            "你的调查进行得怎样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#053F嗯，大致有数了。\x02\x03",
            "虽然还不能下结论，\x01",
            "不过那帮家伙应该是清白的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F真的吗～？\x02\x03",
            "虽说那帮家伙是你以前的同伴，\x01",
            "不过你应该不会包庇他们吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "#050F蠢材，别用这样的眼色看人。\x02\x03",
            "有证人看见他们\x01",
            "昨晚在船员酒吧喝酒。\x02\x03",
            "我问你，在醉酒的状态下， \x01",
            "他们怎能做出那么周到的纵火……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P既然这样的话，\x01",
            "他们的嫌疑暂时先搁在一边吧。\x02\x03",
            "#015F而且，我也并不认为\x01",
            "他们有那么大的胆量去纵火。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯，的确……\x01",
            "感觉他们只会虚张声势而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#053F总之， \x01",
            "这段时间我会盯着那帮家伙的。\x02\x03",
            "顺便也一并搜捕犯人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#050F事件的调查由我来接手。\x02\x03",
            "你们两个就不必再跟进了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F你、你说什么～！？\x02\x03",
            "明明是我们先来的，\x01",
            "你凭什么不让我们跟进这个案件！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#1P可以给我们\x01",
            "一个合理的理由吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#057F你们夹带太多的个人感情了。\x02\x03",
            "不止游击士，\x01",
            "任何人都一样，关心则乱。\x02\x03",
            "而且，居然也把\x01",
            "普通的平民卷到战斗中去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F啊……\x02\x03",
            "#049F对不起，我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#051F你没有道歉的必要。\x01",
            "只是这两个家伙觉悟不足。\x02\x03",
            "关键是还欠缺职业意识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F你、你凭什么\x01",
            "这样批评我们啊！？\x02\x03",
            "不管你说什么都好，\x01",
            "反正我们已经跟特蕾莎院长约定了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(
        0xA,
        (
            "#051F喂，嘉恩。\x02\x03",
            "当正游击士和准游击士\x01",
            "要求接手同一桩任务的时候，\x01",
            "按照规章，应该是哪方享有优先权？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#654F哎呀哎呀……\x01",
            "你不是明知故问吗？\x02\x03",
            "当然是正游击士了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#1P我认为我们两个\x01",
            "也有足够的战斗能力。\x02\x03",
            "无论如何请让我们协助……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "#050F普通的调查用不着这么多人。\x02\x03",
            "我就不多说了。\x01",
            "你们还是想开点吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 135, 400)
    OP_8E(0xA, 0x0, 0x0, 0x9894, 0xBB8, 0x0)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0xA, 0x80)

    def lambda_8797():
        OP_6D(-4700, 0, 45110, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8797)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#009F#2P他、他、他……\x02\x03",
            "#005F他以为自己是谁啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#1P虽然很不甘心，\x01",
            "但他说的确实是事实……\x02\x03",
            "我们也无从反驳。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x105, 0xFF)
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(
        0x105,
        (
            "#043F真对不起……\x01",
            "要是我不出剑的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#2P跟这没有关系啦。\x02\x03",
            "真是的，每次一有事，\x01",
            "就总把我们看成是绊脚石……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0x1)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#655F算了，他没有恶意的，\x01",
            "你们也不要太过介意了。\x02\x03",
            "#655F那家伙是个不善言辞的人，\x01",
            "向来就只会用那种语气说话。\x02\x03",
            "#652F而且这次的事件……\x02\x03",
            "#652F说不定还跟\x01",
            "他正在追查的事件有关联。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A56():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8A56)

    def lambda_8A64():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8A64)

    def lambda_8A72():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8A72)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F阿加特正在追查的事件？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652F详情我不便透露……\x01",
            "总之，搜捕犯人的工作就交给他吧。\x02\x03",
            "我也拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F怎、怎能这样呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F是吗……………\x02\x03",
            "#015F那么，就先把我们至今为止\x01",
            "调查所得的情况报告一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#655F嗯，有劳你们了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x3B, 0x4, 0x10)
    OP_28(0x3C, 0x4, 0x10)
    OP_28(0x3C, 0x4, 0x20)
    Sleep(100)
    OP_AF(0x22, 0x3B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#655F看来你们的调查做得很认真啊。\x02\x03",
            "#652F不过就像我刚才所说的，\x01",
            "这次的事件牵涉的东西很多。\x02\x03",
            "虽然非常抱歉，不过事件的调查\x01",
            "还是以这次报告为终结吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F可、可是……\x02\x03",
            "我本来想为特蕾莎院长\x01",
            "还有那些孩子做点什么的……\x02\x03",
            "……现在竟然………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#013F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 0)

    ChrTalk(
        0x105,
        (
            "#043F艾丝蒂尔……\x02\x03",
            "#047F……………………………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 0)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#042F那个，嘉恩先生。\x02\x03",
            "如果我没记错的话， \x01",
            "游击士的成员也可以参与\x01",
            "协助由民间举办的活动对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F是啊，不过也要看内容。\x02\x03",
            "像王立学院的学园祭，\x01",
            "因为会有很多客人来参观，\x01",
            "所以我们通常都会负责警卫的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F这样的话……\x01",
            "艾丝蒂尔、约修亚。\x02\x03",
            "其实工作的意义还可以延伸一下，\x01",
            "我想请你们协助学院舞台剧的举办。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8F1F():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F1F)

    def lambda_8F2D():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8F2D)

    ChrTalk(
        0x101,
        "#004F#2P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#1P这话怎么说？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F每年学园祭的最后，\x01",
            "我们都会在礼堂表演舞台剧。\x02\x03",
            "更重要的是，\x01",
            "那些孩子也一直在期待着演出呢……\x02\x03",
            "#045F不过，有两个很重要的角色\x01",
            "到现在都还没找到合适的人选……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2P难、难道说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#1P要我们来演这两个角色吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F是的，如果再找不到演员，\x01",
            "今年的舞台剧可能就要停演了。\x02\x03",
            "那样就太对不住那些\x01",
            "期待着看表演的孩子们了……\x02\x03",
            "#040F于是昨晚，我和学院的学生会长\x01",
            "说起了你们两人的事。\x02\x03",
            "结果她很感兴趣，\x01",
            "叫我无论如何要把你们请过来……\x02\x03",
            "#041F我们会从预算经费中拨出酬金的，\x01",
            "虽然数目不是很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2P为、为什么选中我们两个？\x02\x03",
            "不是我要推脱，\x01",
            "舞台剧什么的我可是从来没演过啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F因为女生所扮演的角色\x01",
            "一定要精通武术才能胜任……\x02\x03",
            "如果由艾丝蒂尔扮演的话，\x01",
            "我想这角色一定会演得非常好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#2P原、原来是这样啊……\x02\x03",
            "嗯，谈到武术的话，\x01",
            "我倒还满有一点自信的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#1P的确正适合你呢。\x02\x03",
            "#010F那么，另一个角色呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#044F这、这个……\x02\x03",
            "#049F这个……要我说的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#1P要你说的话怎样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#045F……有点……不好意思呢。\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#018F#1P这、这是什么意思……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P真是的，约修亚你呀，\x01",
            "刨根问底的话可会让人为难哦。\x02\x03",
            "既可以参加学园祭，\x01",
            "又可以让那些孩子高兴……\x02\x03",
            "再说这又算是工作，\x01",
            "简直就是一石三鸟啊！\x02\x03",
            "#001F当然是非做不可的啦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#1P等、等一下。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x102,
        (
            "#014F#1P嘉恩先生。 \x01",
            "这样的工作也可以做吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_95B1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_95B1)

    ChrTalk(
        0x8,
        (
            "#651F当然了，没问题。\x02\x03",
            "对平民的协助、对地区的贡献，\x01",
            "这是一份非常有意义的好工作呢。\x02\x03",
            "#650F而且刚好阿加特来了，\x01",
            "你们也可以挪出空闲来……\x02\x03",
            "可以的话就尽管去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#2P太好啦㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#017F#1P呼……\x01",
            "总有种不祥的预感。\x02\x03",
            "#017F不过为了那些孩子，\x01",
            "我们也只好尽力而为了。\x02\x03",
            "#010F不过，如果有什么未完的工作，\x01",
            "最好还是在去王立学院之前\x01",
            "处理完比较好吧。\x02\x03",
            "一旦开始帮忙排演舞台剧，\x01",
            "大概就没空做其他的事了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006F#2P是啊，的确呢。\x02",
    )

    CloseMessageWindow()

    def lambda_9803():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9803)

    def lambda_9811():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9811)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#501F#2P那个，科洛丝。\x02\x03",
            "可能会稍微耽误些时间，\x01",
            "先等我们完成工作再去可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F啊，好呢。\x01",
            "你们就不用顾虑我了。\x02\x03",
            "#040F顺便说一下怎么去王立学院吧……\x02\x03",
            "出了梅威海道，在第一个三叉路口处\x01",
            "向东拐，然后沿着林道走就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P嗯，知道了。\x02\x03",
            "#001F那么，我们走吧～！\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3C, 0x1, 0x40)
    OP_28(0x3C, 0x1, 0x80)
    OP_28(0x3D, 0x4, 0x2)
    OP_28(0x3D, 0x4, 0x4)
    OP_28(0x3D, 0x1, 0x1)
    OP_28(0x3D, 0x1, 0x2)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_22_79A7 end

    def Function_23_998D(): pass

    label("Function_23_998D")

    EventBegin(0x0)
    OP_6D(-4840, 0, 45450, 0)
    SetChrPos(0x101, -3350, 0, 45440, 270)
    SetChrPos(0x102, -3440, 0, 44470, 270)
    SetChrPos(0x105, 0, 0, 39060, 0)
    SetChrFlags(0x105, 0x80)
    OP_4A(0x8, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#652F……我明白了。\x02\x03",
            "真想不到戴尔蒙市长\x01",
            "会是一连串事件的幕后主使。\x02\x03",
            "嗯，这可是件大事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F对了，嘉恩哥哥。\x01",
            "我们可以去逮捕市长吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#654F这个嘛……\x01",
            "很遗憾，恐怕很难。\x02\x03",
            "但如果是现行犯的话，\x01",
            "即使是市长也可以不容置辩地将其逮捕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F果然是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F怎、怎么会……\x02\x03",
            "难道还要让那个恶毒的市长\x01",
            "继续胡作非为下去吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F哎呀，不用那么紧张啦。\x02\x03",
            "就算协会没权这么做……\x01",
            "不过，王国军却可以逮捕市长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652F艾丝蒂尔、约修亚。\x02\x03",
            "你们现在就前往市长官邸，\x01",
            "将事情问个清楚彻底。\x02\x03",
            "就算或多或少把他惹火了也没关系，\x01",
            "总之尽量拖延时间就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此，\x01",
            "这期间你就和王国军联络是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F呵呵呵，就是这样。\x02\x03",
            "我会利用导力通信，\x01",
            "向雷斯顿要塞的司令部申请援助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯，虽然求助于军队有点不爽，\x01",
            "但也没办法了……\x02\x03",
            "#006F好吧，等科洛丝也来到之后，\x01",
            "我们就去市长家……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_9E7E():
        OP_6D(-4770, 0, 44400, 1000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9E7E)

    def lambda_9E96():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9E96)

    def lambda_9EA4():

        label("loc_9EA4")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_9EA4")

    QueueWorkItem2(0x101, 1, lambda_9EA4)

    def lambda_9EB5():

        label("loc_9EB5")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_9EB5")

    QueueWorkItem2(0x102, 1, lambda_9EB5)
    ClearChrFlags(0x105, 0x80)
    OP_8E(0x105, 0xFFFFF434, 0x0, 0xA866, 0xBB8, 0x0)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#049F#3P呼～呼～……\x02\x03",
            "让、让你们久等了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#2P你来得正是时候⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P回去学院一趟之后，\x01",
            "竟还能这么快赶过来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F#3P这、这个……\x01",
            "我对自己的脚力还是有点自信的。\x02\x03",
            "#042F对了……\x01",
            "事情进展得怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P我们正在讨论\x01",
            "前往市长家的事呢。\x02\x03",
            "要在王国军的人到达之前，\x01",
            "一边探听情况一边尽量拖延时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#044F#3P啊……这样吗……\x02\x03",
            "#049F……我可能多此一举了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#2P？？？\x02\x03",
            "那个，科洛丝也一起来吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F#3P啊，是。\x01",
            "请一定让我同行。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#012F嘉恩先生，\x01",
            "联络王国军的事就拜托您了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "#652F嗯，交给我吧！\x02",
    )

    CloseMessageWindow()
    OP_28(0x3E, 0x1, 0x400)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_23_998D end

    def Function_24_A1AC(): pass

    label("Function_24_A1AC")

    EventBegin(0x0)
    OP_6D(-4700, 0, 45110, 0)
    OP_6B(2800, 0)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x8, 255)
    SetChrPos(0x101, -3360, 0, 45110, 270)
    SetChrPos(0x102, -3530, 0, 43770, 315)
    SetChrPos(0x105, -2350, 0, 44220, 270)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#650F哦～这样啊。\x01",
            "没想到王都的亲卫队竟然来了。\x02\x03",
            "而且连传说中的最新型舰艇\x01",
            "『埃尔赛尤号』也出动了。\x02\x03",
            "#654F要不是有接待工作的话，\x01",
            "我也好想跑去亲眼看看啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F想不到嘉恩哥哥\x01",
            "还挺喜欢看热闹的嘛。\x02\x03",
            "#000F话说回来，\x01",
            "嘉恩哥哥联络的是理查德上校对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F是啊，\x01",
            "因为他正好在雷斯顿要塞的司令部。\x02\x03",
            "不过亲卫队为什么会来，\x01",
            "这点我就不知道了……\x02\x03",
            "大概是因为\x01",
            "军队的联络系统也有好多种吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F除了普通的正规军，\x01",
            "国境师团、情报部、王室亲卫队……\x02\x03",
            "的确是非常复杂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F话说回来，\x01",
            "这次事件的善后处理会很麻烦吧……\x02\x03",
            "今后卢安地区的行政工作\x01",
            "将会如何进行下去呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊，对啊……\x01",
            "毕竟是市长已经被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652F我想应该会从王都\x01",
            "派一位代理市长过来暂代政务吧。\x02\x03",
            "市长被定罪之后，\x01",
            "接着很快就会举行市长选举吧。\x02\x03",
            "#651F对了对了，\x01",
            "我想孤儿院也会受到正式补偿的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F是吗……太好了。\x02\x03",
            "#048F这些都是多亏了\x01",
            "艾丝蒂尔你们的全力帮助啊。\x02\x03",
            "真的……太感谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_A6E2():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A6E2)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#008F#2P没、没什么啦。\x01",
            "你就别说得这么见外嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P是啊，\x01",
            "这些都是我们应该做的。\x02\x03",
            "更何况不止我们，\x01",
            "阿加特兄他也帮了大忙啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#2P说、说起来！\x02",
    )

    CloseMessageWindow()

    def lambda_A7C3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A7C3)
    TurnDirection(0x102, 0x8, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#005F喂、喂，嘉恩哥哥！\x01",
            "那个阿加特有联络吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652F啊啊，这个嘛……\x02\x03",
            "非常遗憾，\x01",
            "似乎让那帮黑衣人跑掉了。\x02\x03",
            "他们好像还有其他同伙，\x01",
            "一起对阿加特进行了伏击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F他没事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#655F嗯，总算是突围成功了。\x02\x03",
            "现在应该正追着那帮家伙，\x01",
            "往蔡斯方向去了。\x02\x03",
            "这会儿大概已经\x01",
            "离开卢安地区了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F是、是吗……\x01",
            "还真是高难度的任务啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F哈哈，反正他也习惯了。\x02\x03",
            "阿加特这一段时间\x01",
            "就一直在追捕那帮黑衣人。\x02\x03",
            "而且……\x01",
            "这好像还是你们父亲拜托他做的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F老、老爸！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F阿加特竟然会接受……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651F呵呵，把曾经是『渡鸦帮』一员的\x01",
            "阿加特引回正途的不是别人，\x01",
            "正是卡西乌斯先生哦。\x02\x03",
            "别看他嘴上不饶人，\x01",
            "但一在你们父亲面前，他还是很乖的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎哎？原来是这样吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F不过因为阿加特是那种性格，\x01",
            "所以他经常会和别人一个劲地顶撞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x02\x03",
            "他之所以对我们那么严厉，\x01",
            "也恐怕是这个原因吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F的确很有可能～\x02\x03",
            "#005F也就是说，搞了半天，\x01",
            "我们又是受了老爸的连累啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F呵呵……\x02\x03",
            "#044F啊，\x01",
            "提起艾丝蒂尔你们的父亲……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ACEF():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ACEF)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#004F#2P哎？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F那个……\x01",
            "在市长官邸出现黑光的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#2P对了，还有这件事！\x02",
    )

    CloseMessageWindow()

    def lambda_ADAD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ADAD)
    OP_8C(0x101, 180, 200)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x101, 13)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -3600, 550, 44750, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#009F#2P发生了太多事情，\x01",
            "不知不觉把这个忘掉了……\x02\x03",
            "这个，到底是什么东西呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F虽然这东西救了我们一命，\x01",
            "但不知为什么，总觉得它有点诡异……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#653F很少见到这种颜色的导力器啊。\x02\x03",
            "这东西是哪里来的？\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x101, 65535)

    def lambda_AEF7():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AEF7)
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#003F这是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔向嘉恩说明了\x01",
            "在寄给卡西乌斯的包裹里装有导力器和便条一事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x105,
        "#044F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#655F嗯，Ｒ博士还有Ｋ吗……\x02\x03",
            "难道是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？你知道吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652F不，应该还\x01",
            "称不上是什么线索……\x02\x03",
            "但如果想调查这东西的来历，\x01",
            "我想你们应该到蔡斯地区去一趟。\x01",
            "也许会找到什么答案也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F蔡斯地区？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652F正是如此，\x01",
            "蔡斯市是以制造导力器而闻名的城市。\x02\x03",
            "那里又被称作『工房都市』。\x01",
            "拥有博士头衔的人也有很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x02\x03",
            "就算找不到那位博士，\x01",
            "但是至少也能弄清\x01",
            "这个黑色导力器的真面目也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唔……\x01",
            "但我们还要留在这里修行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651F呵呵，就是为了应付这种情况，\x01",
            "我早已经全都准备好了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "正游击士资格的推荐信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x339, 1)

    ChrTalk(
        0x101,
        "#004F哎哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F这样可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650F哈哈，就和空贼事件时一样啊。\x02\x03",
            "解决了那么大的事件，\x01",
            "还有什么理由不发给你们呢。\x02\x03",
            "评定和报酬也准备好了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3D, 0x4, 0x10)
    OP_28(0x3E, 0x4, 0x10)
    Sleep(100)
    OP_AF(0x22, 0x3D)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(100)
    OP_AF(0x22, 0x3E)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#008F哇～……\x01",
            "连学园祭的演出费都有……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F总之多谢您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651F别这么说，这是你们应得的报酬。\x02\x03",
            "我也希望你们两个\x01",
            "能尽早成为正游击士呢。\x02\x03",
            "到那时候，\x01",
            "你们就能更自由地展现自己的力量了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嘿嘿……\x01",
            "谢谢，嘉恩哥哥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们一定会努力，不辜负您的期望。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F太好了。\x01",
            "艾丝蒂尔、约修亚。\x02\x03",
            "#045F……只是以后，\x01",
            "稍微有点寂寞呢……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B628():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B628)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#003F#2P科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#1P……是啊。\x01",
            "我们也很舍不得呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F啊……\x01",
            "对不起，说了些任性的话。\x02\x03",
            "#542F决定了出发的日子的话，\x01",
            "可以告诉我一声吗？\x02\x03",
            "我想，至少也让我\x01",
            "送你们到艾尔·雷登关所……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x9C4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_AD(0x40043, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_83(0x13, 0x0)
    OP_A2(0x44B)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xF2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存进度】\x01",        # 0
            "【进入下一章】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7F1")
    ShowSaveMenu()

    label("loc_B7F1")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x44C)
    OP_A2(0x442)
    OP_28(0x3E, 0x1, 0x800)
    OP_28(0x53, 0x4, 0x2)
    OP_28(0x53, 0x4, 0x4)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/R2412   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_A1AC end

    def Function_25_B831(): pass

    label("Function_25_B831")

    EventBegin(0x1)
    TurnDirection(0x9, 0x0, 0)
    OP_4A(0x9, 0)
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x14, 0x3E8)

    ChrTalk(
        0x9,
        (
            "#830F抱歉，\x01",
            "现在二楼正在进行商谈。\x02\x03",
            "你们不妨到街上逛逛，\x01",
            "消磨一些时间怎么样？\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_4B(0x9, 0)
    OP_8C(0x9, 90, 0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_25_B831 end

    SaveToFile()

Try(main)
