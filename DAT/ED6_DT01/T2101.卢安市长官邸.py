from ED6ScenarioHelper import *

def main():
    # 卢安市长官邸

    CreateScenaFile(
        FileName            = 'T2101   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2101   ._SN',
            'ED6_DT01/T2101_1 ._SN',
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
        '迪恩',                                 # 9
        '雷斯',                                 # 10
        '洛克',                                 # 11
        '皮卡罗',                               # 12
        '戴尔蒙市长',                           # 13
        '秘书基尔巴特',                         # 14
        '基库',                                 # 15
        '哈古',                                 # 16
        '照相机',                               # 17
        '布诺安',                               # 18
        '奈尔',                                 # 19
        '西蒙',                                 # 20
        '波尔多斯',                             # 21
        '昆茨',                                 # 22
        '布兰塔婆婆',                           # 23
        '船',                                   # 24
        '波尔多斯',                             # 25
        '阿伊纳街道方向',                       # 26
        '卢安市·北街区',                       # 27
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
        'ED6_DT07/CH01390 ._CH',             # 00
        'ED6_DT07/CH02410 ._CH',             # 01
        'ED6_DT07/CH02420 ._CH',             # 02
        'ED6_DT07/CH02320 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH02063 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH01680 ._CH',             # 07
        'ED6_DT07/CH01500 ._CH',             # 08
        'ED6_DT07/CH01460 ._CH',             # 09
        'ED6_DT07/CH01110 ._CH',             # 0A
        'ED6_DT07/CH02510 ._CH',             # 0B
        'ED6_DT07/CH02520 ._CH',             # 0C
        'ED6_DT07/CH02530 ._CH',             # 0D
        'ED6_DT06/CH20051 ._CH',             # 0E
        'ED6_DT06/CH20161 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH01390P._CP',             # 00
        'ED6_DT07/CH02410P._CP',             # 01
        'ED6_DT07/CH02420P._CP',             # 02
        'ED6_DT07/CH02320P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH02063P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH01680P._CP',             # 07
        'ED6_DT07/CH01500P._CP',             # 08
        'ED6_DT07/CH01460P._CP',             # 09
        'ED6_DT07/CH01110P._CP',             # 0A
        'ED6_DT07/CH02510P._CP',             # 0B
        'ED6_DT07/CH02520P._CP',             # 0C
        'ED6_DT07/CH02530P._CP',             # 0D
        'ED6_DT06/CH20051P._CP',             # 0E
        'ED6_DT06/CH20161P._CP',             # 0F
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
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
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 49950,
        Z                   = 1000,
        Y                   = 2460,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
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
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
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
        X                   = 800,
        Z                   = 6000,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4620,
        Z                   = -1800,
        Y                   = 22750,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 6000,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15900,
        Z                   = -1800,
        Y                   = 25200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 65090,
        Z                   = -1700,
        Y                   = 32900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 24700,
        Z                   = 0,
        Y                   = 24500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 20070,
        Z                   = 0,
        Y                   = 26530,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 7100,
        Z                   = 0,
        Y                   = 28900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 58900,
        Z                   = 0,
        Y                   = 29500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 23560,
        Z                   = 1000,
        Y                   = 1760,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 73210,
        Z                   = 0,
        Y                   = -16650,
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
        X                   = 50980,
        Z                   = 400,
        Y                   = 77990,
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
        X                   = 32790,
        Y                   = 2000,
        Z                   = 13300,
        Range               = 26260,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x2ADA,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 49000,
        Y                   = 2000,
        Z                   = 26550,
        Range               = 46940,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x4B82,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 76190,
        Y                   = 0,
        Z                   = 0,
        Range               = 70000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFF830,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = 31200,
        Y                   = 0,
        Z                   = 25340,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 77280,
        Y                   = 0,
        Z                   = 22060,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 18,
    )


    DeclActor(
        TriggerX            = 41040,
        TriggerZ            = -1650,
        TriggerY            = 32140,
        TriggerRange        = 1400,
        ActorX              = 41040,
        ActorZ              = -6350,
        ActorY              = 32140,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17000,
        TriggerZ            = 0,
        TriggerY            = 29200,
        TriggerRange        = 3500,
        ActorX              = 17050,
        ActorZ              = 3500,
        ActorY              = 29200,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 50320,
        TriggerZ            = 1000,
        TriggerY            = 2450,
        TriggerRange        = 800,
        ActorX              = 50320,
        ActorZ              = 2000,
        ActorY              = 2450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 50320,
        TriggerZ            = 1000,
        TriggerY            = 9400,
        TriggerRange        = 800,
        ActorX              = 50320,
        ActorZ              = 2000,
        ActorY              = 9400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31960,
        TriggerZ            = 1000,
        TriggerY            = 3430,
        TriggerRange        = 800,
        ActorX              = 31960,
        ActorZ              = 2000,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23540,
        TriggerZ            = 1000,
        TriggerY            = 3430,
        TriggerRange        = 800,
        ActorX              = 23540,
        ActorZ              = 2000,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_502",          # 00, 0
        "Function_1_5A6",          # 01, 1
        "Function_2_74D",          # 02, 2
        "Function_3_8CA",          # 03, 3
        "Function_4_B0A",          # 04, 4
        "Function_5_107C",         # 05, 5
        "Function_6_142E",         # 06, 6
        "Function_7_1D96",         # 07, 7
        "Function_8_25E0",         # 08, 8
        "Function_9_2666",         # 09, 9
        "Function_10_29F2",        # 0A, 10
        "Function_11_33FE",        # 0B, 11
        "Function_12_36C7",        # 0C, 12
        "Function_13_5C18",        # 0D, 13
        "Function_14_63FD",        # 0E, 14
        "Function_15_682C",        # 0F, 15
        "Function_16_687B",        # 10, 16
        "Function_17_6882",        # 11, 17
        "Function_18_6886",        # 12, 18
    )


    def Function_0_502(): pass

    label("Function_0_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_516")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8)
    Jump("loc_579")

    label("loc_516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_53B")
    SetChrPos(0x15, 19270, 0, 30790, 225)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8)
    Jump("loc_579")

    label("loc_53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_559")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    Jump("loc_579")

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_568")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_579")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_579")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)

    label("loc_579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_587")
    OP_A3(0x3FA)
    Event(0, 13)

    label("loc_587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_594")
    ClearChrFlags(0xB, 0x80)

    label("loc_594")

    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_502 end

    def Function_1_5A6(): pass

    label("Function_1_5A6")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFE7960, 0x30048)
    OP_72(0x16, 0x10)
    OP_6F(0x16, 60)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    OP_72(0x14, 0x10)
    OP_72(0x15, 0x10)
    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E")
    OP_72(0x13, 0x10)
    OP_65(0x2, 0x1)
    Jump("loc_613")

    label("loc_60E")

    OP_1C(0x13, 0x0, 0x10)

    label("loc_613")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_631")
    OP_64(0x0, 0x1)

    label("loc_631")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_650")
    OP_64(0x1, 0x1)

    label("loc_650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_65A")
    Jump("loc_6E3")

    label("loc_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_670")
    OP_6F(0x11, 1020)
    OP_72(0x21, 0x2)
    Jump("loc_6E3")

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_67A")
    Jump("loc_6E3")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_690")
    OP_6F(0x11, 1020)
    OP_72(0x21, 0x2)
    Jump("loc_6E3")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_END)), "loc_6A6")
    OP_6F(0x11, 1020)
    OP_72(0x21, 0x2)
    Jump("loc_6E3")

    label("loc_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_6B0")
    Jump("loc_6E3")

    label("loc_6B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_6BA")
    Jump("loc_6E3")

    label("loc_6BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_END)), "loc_6D0")
    OP_6F(0x11, 1020)
    OP_72(0x21, 0x2)
    Jump("loc_6E3")

    label("loc_6D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_6E3")
    OP_6F(0x11, 1020)
    OP_72(0x21, 0x2)

    label("loc_6E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_747")
    LoadEffect(0x0, "map\\\\mp022_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 41040, -6550, 32140, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)

    label("loc_747")

    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_5A6 end

    def Function_2_74D(): pass

    label("Function_2_74D")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_772")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_8B4")

    label("loc_772")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_8B4")

    label("loc_78B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A4")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_8B4")

    label("loc_7A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BD")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_8B4")

    label("loc_7BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D6")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_8B4")

    label("loc_7D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_8B4")

    label("loc_7EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_808")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_8B4")

    label("loc_808")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_821")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_8B4")

    label("loc_821")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_8B4")

    label("loc_83A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_853")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_8B4")

    label("loc_853")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_8B4")

    label("loc_86C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_885")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_8B4")

    label("loc_885")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_8B4")

    label("loc_89E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B4")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_8B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8C9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_8B4")

    label("loc_8C9")

    Return()

    # Function_2_74D end

    def Function_3_8CA(): pass

    label("Function_3_8CA")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC8")
    EventBegin(0x0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "……为、为什么在这种地方\x01",
            "会有年轻的女孩子……\x02\x03",
            "不行不行，你们不许进入！\x02\x03",
            "这、这可不是你们\x01",
            "这些小鬼可以来的地方！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F你误会了吧，\x01",
            "我们可没说要进去啊……\x02\x03",
            "#000F这位大哥，\x01",
            "你为什么这么紧张呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果、果然\x01",
            "能看得出我很紧张吗……？\x02\x03",
            "……不对，\x01",
            "总之这里不许进入！\x02\x03",
            "赶快去别的地方吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F（呼……\x01",
            "　我觉得还是不要去管他比较好……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F（嗯，这人穿得这么奇怪，\x01",
            "　到底是什么人呢？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043F（…………………………）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x447)
    OP_A2(0x9)
    EventEnd(0x1)
    Jump("loc_B06")

    label("loc_AC8")


    ChrTalk(
        0xFE,
        (
            "总、总之这里不许进入！\x02\x03",
            "这、这可不是\x01",
            "你们这些小鬼可以来的地方！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B06")

    TalkEnd(0xB)
    Return()

    # Function_3_8CA end

    def Function_4_B0A(): pass

    label("Function_4_B0A")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_CF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C44")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "戴尔蒙市长\x01",
            "只重视观光业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他从来不会考虑\x01",
            "为港口更换新的设备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "主任也应该明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "干脆让波尔多斯主任\x01",
            "来当市长更好啦，\x01",
            "那样我们也能够安心地工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CED")

    label("loc_C44")


    ChrTalk(
        0xFE,
        (
            "戴尔蒙市长\x01",
            "从来都不会考虑\x01",
            "为港口更换新的设备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "干脆让波尔多斯主任\x01",
            "来当市长更好啦，\x01",
            "那样我们也能够安心地工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CED")

    Jump("loc_1078")

    label("loc_CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_D63")

    ChrTalk(
        0xFE,
        (
            "最近这几天，\x01",
            "完全看不到那些不良青年的身影。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道说他们已经\x01",
            "被市长赶出去了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_E19")

    ChrTalk(
        0xFE,
        (
            "仓库那帮人正当年青，\x01",
            "却不好好干活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最终还是要靠别人养活，\x01",
            "那副狼狈相，\x01",
            "父母哭都哭不出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_E82")

    ChrTalk(
        0xFE,
        (
            "刚才，渡鸦帮那些家伙\x01",
            "不知为什么在吵吵闹闹的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正又干了些\x01",
            "不入流的事情吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_F2A")

    ChrTalk(
        0xFE,
        (
            "市长为什么放任\x01",
            "渡鸦帮那些家伙们不管啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样让他们任意妄为，\x01",
            "只会让他们更加得意忘形。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1078")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FFD")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "你们是旅游者吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我话说在前面，\x01",
            "你们可千万别靠近仓库那里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那一带集中了\x01",
            "不少不良青年哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_FFD")


    ChrTalk(
        0xFE,
        (
            "我话说在前面，\x01",
            "你们可千万别靠近仓库那里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那一带集中了\x01",
            "不少不良青年哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1078")

    TalkEnd(0x11)
    Return()

    # Function_4_B0A end

    def Function_5_107C(): pass

    label("Function_5_107C")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_11AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1140")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "渡鸦帮的那些家伙\x01",
            "好像都回到城里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也许是心理作用，\x01",
            "看起来他们好像无精打采的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这种时候只要活动一下身体，\x01",
            "就会感觉心情舒畅了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A8")

    label("loc_1140")


    ChrTalk(
        0xFE,
        (
            "渡鸦帮的那些家伙\x01",
            "好像都回到城里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也许是心理作用，\x01",
            "看起来他们好像无精打采的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A8")

    Jump("loc_142A")

    label("loc_11AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_125F")

    ChrTalk(
        0xFE,
        (
            "波尔多斯主任\x01",
            "又在为什么事情烦恼了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有时不要有太多烦恼，\x01",
            "偶尔也运动一下，\x01",
            "说不定会想出什么好点子来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142A")

    label("loc_125F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_12F1")

    ChrTalk(
        0xFE,
        "最近机器的情况不太好啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还是请蔡斯的技术人员\x01",
            "过来检查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142A")

    label("loc_12F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1333")

    ChrTalk(
        0xFE,
        "哦，开合桥吊起来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "差不多到吃饭时间了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_142A")

    label("loc_1333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_13A3")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "今天过得真是很充实啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我果然适合\x01",
            "做这些体力活呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142A")

    label("loc_13A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_142A")

    ChrTalk(
        0xFE,
        (
            "这里是将从国外运来的物资\x01",
            "卸下船的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "进口的货物\x01",
            "在这里办理好通关手续之后，\x01",
            "就可以运往利贝尔各地了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142A")

    TalkEnd(0x15)
    Return()

    # Function_5_107C end

    def Function_6_142E(): pass

    label("Function_6_142E")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_165A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BF")
    OP_28(0x21, 0x1, 0x8000)

    ChrTalk(
        0xFE,
        "哦，之前真是谢谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再遇到什么困难，\x01",
            "还是要拜托你们哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1657")

    label("loc_14BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15A0")
    OP_28(0x21, 0x1, 0x4000)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "我还是觉得那个假扮的主任\x01",
            "和真的波尔多斯主任一模一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不只是外形，\x01",
            "连说话的方式和态度也都完全一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个世上还有\x01",
            "这么厉害的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1657")

    label("loc_15A0")


    ChrTalk(
        0xFE,
        (
            "看到波尔多斯主任那么辛苦，\x01",
            "真是十分过意不去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但要是发生什么问题的话，\x01",
            "能解决问题的人也还是\x01",
            "只有波尔多斯主任一个啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1657")

    Jump("loc_1D92")

    label("loc_165A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_18E2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16E8")
    OP_28(0x21, 0x1, 0x8000)

    ChrTalk(
        0xFE,
        "哦，之前真是谢谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再遇到什么困难，\x01",
            "还是要拜托你们哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18DF")

    label("loc_16E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17C9")
    OP_28(0x21, 0x1, 0x4000)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "我还是觉得那个假扮的主任\x01",
            "和真的波尔多斯主任一模一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不只是外形，\x01",
            "连说话的方式和态度也都完全一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个世上还有\x01",
            "这么厉害的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18DF")

    label("loc_17C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1896")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "波尔多斯主任\x01",
            "虽然外表看上去有点呆呆的，\x01",
            "但实际上他头脑很灵活，而且很负责任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论哪个方面\x01",
            "他都非常为我们着想。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "我们对主任都十分敬仰。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18DF")

    label("loc_1896")


    ChrTalk(
        0xFE,
        (
            "波尔多斯主任\x01",
            "虽然外表看上去有点呆呆的，\x01",
            "但实际上他头脑很灵活，而且很负责任。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18DF")

    Jump("loc_1D92")

    label("loc_18E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1BA2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1970")
    OP_28(0x21, 0x1, 0x8000)

    ChrTalk(
        0xFE,
        "哦，之前真是谢谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再遇到什么困难，\x01",
            "还是要拜托你们哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9F")

    label("loc_1970")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A51")
    OP_28(0x21, 0x1, 0x4000)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "我还是觉得那个假扮的主任\x01",
            "和真的波尔多斯主任一模一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不只是外形，\x01",
            "连说话的方式和态度也都完全一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个世上还有\x01",
            "这么厉害的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9F")

    label("loc_1A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B17")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "下一艘要到达的是共和国的船只吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果被近海的渔船干扰了进港，\x01",
            "就是波尔多斯主任的责任了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果海港能\x01",
            "再扩大一些就好了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9F")

    label("loc_1B17")


    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "下一艘要到达的是共和国的船只。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果被近海的渔船干扰了进港，\x01",
            "就是波尔多斯主任的责任了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B9F")

    Jump("loc_1D92")

    label("loc_1BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1BE7")

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "先赶快把这边的货物处理好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1CAB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C4D")

    ChrTalk(
        0xFE,
        "谢谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再遇到什么困难，\x01",
            "还是要拜托你们哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA8")

    label("loc_1C4D")


    ChrTalk(
        0xFE,
        (
            "伤脑筋了。\x01",
            "掉在哪里了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在被他发现之前，\x01",
            "要赶快找到才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA8")

    Jump("loc_1D92")

    label("loc_1CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1D14")

    ChrTalk(
        0xFE,
        (
            "今天该轮到\x01",
            "我来保管仓库的钥匙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "必须去波尔多斯主任那里\x01",
            "把钥匙拿过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1D92")

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "这些是从帝国运来的集装箱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要把它们装载到\x01",
            "去蔡斯的定期船上。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D92")

    TalkEnd(0xF)
    Return()

    # Function_6_142E end

    def Function_7_1D96(): pass

    label("Function_7_1D96")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED8")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "市长竟然会\x01",
            "犯下这么多的罪行，\x01",
            "看来戴尔蒙家族也没落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样的话，\x01",
            "选举下任市长就要注意点了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "相比之下，\x01",
            "我更加担心那些孩子们啊。\x01",
            "孤儿院被烧掉之后该怎么办呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "像我这样的老太婆\x01",
            "什么忙也帮不上啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7F")

    label("loc_1ED8")


    ChrTalk(
        0xFE,
        (
            "市长竟然会\x01",
            "犯下这么多的罪行，\x01",
            "看来戴尔蒙家族也没落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来我更加\x01",
            "担心那些孩子们啊。\x01",
            "孤儿院被烧掉之后该怎么办呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7F")

    Jump("loc_25DC")

    label("loc_1F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_20E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_204D")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "有一个穿着气派却带有低级趣味的男人\x01",
            "进入了市长官邸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……说起来，\x01",
            "听说有位某地的达官贵人会在卢安停留。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E6")

    label("loc_204D")


    ChrTalk(
        0xFE,
        (
            "就在刚才，\x01",
            "有个虽看上去很有气派但穿着却\x01",
            "带有低级趣味的男人进入了市长官邸。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E6")

    Jump("loc_25DC")

    label("loc_20E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_221C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D2")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "今天的天气也很好啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我小时候总是在这里\x01",
            "看着外国的船进进出出，\x01",
            "从来都不会觉得看腻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "港口的周围\x01",
            "有很多市场和摊贩，\x01",
            "那才叫充满活力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2219")

    label("loc_21D2")


    ChrTalk(
        0xFE,
        (
            "我小时候总是在这里\x01",
            "看着外国的船进进出出，\x01",
            "从来都不会觉得看腻了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2219")

    Jump("loc_25DC")

    label("loc_221C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_23A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2314")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "戴尔蒙市长非常积极地\x01",
            "发展卢安的观光业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他好像准备以此带动\x01",
            "全市各项事业的发展呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里原本是\x01",
            "以港口城市而繁荣起来的，\x01",
            "这就是时代的变迁吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23A4")

    label("loc_2314")


    ChrTalk(
        0xFE,
        (
            "戴尔蒙市长非常积极地\x01",
            "发展卢安的观光业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里原本是\x01",
            "以港口城市而繁荣起来的，\x01",
            "这就是时代的变迁吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A4")

    Jump("loc_25DC")

    label("loc_23A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_250A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2492")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "河川的这边\x01",
            "不是有座非常漂亮的住宅吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那是卢安市长\x01",
            "戴尔蒙先生的官邸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "卢安的市长一职\x01",
            "是由曾为贵族的\x01",
            "戴尔蒙家的主人代代相传的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2507")

    label("loc_2492")


    ChrTalk(
        0xFE,
        (
            "河川的这边\x01",
            "不是有座非常漂亮的住宅吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那是卢安市长\x01",
            "戴尔蒙先生的官邸。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2507")

    Jump("loc_25DC")

    label("loc_250A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_25DC")

    ChrTalk(
        0xFE,
        (
            "在河的对岸那边\x01",
            "集中了本市的商业和观光设施，\x01",
            "那些都是最近才发展起来的产业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "河岸这边则在很早以前\x01",
            "就是港湾设施和住宅区了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25DC")

    TalkEnd(0x16)
    Return()

    # Function_7_1D96 end

    def Function_8_25E0(): pass

    label("Function_8_25E0")

    TalkBegin(0x12)

    ChrTalk(
        0xFE,
        (
            "#140F……接下来，\x01",
            "该怎样继续调查比较好呢。\x02\x03",
            "还是要靠这双脚\x01",
            "去现场调查才行吗。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_8_25E0 end

    def Function_9_2666(): pass

    label("Function_9_2666")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2797")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "以前一提起卢安，\x01",
            "就是贸易与渔业发达的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最繁荣的是这个港口，\x01",
            "可不是如今那么兴盛的观光业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从戴尔蒙市长就任以来，\x01",
            "这里给人的印象就完全成了旅游城市了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2856")

    label("loc_2797")


    ChrTalk(
        0xFE,
        (
            "以前一提起卢安，\x01",
            "就是贸易与渔业发达的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从戴尔蒙市长就任以来，\x01",
            "这里给人的印象就完全成了旅游城市了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2856")

    Jump("loc_29EE")

    label("loc_2859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_2954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F7")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "货物没有问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "必须要赶快\x01",
            "办好通关手续，\x01",
            "把集装箱送到柏斯去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2951")

    label("loc_28F7")


    ChrTalk(
        0xFE,
        (
            "必须要赶快\x01",
            "办好通关手续，\x01",
            "把集装箱送到柏斯去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2951")

    Jump("loc_29EE")

    label("loc_2954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_29EE")

    ChrTalk(
        0xFE,
        (
            "虽说飞艇可以运送大量的商品，\x01",
            "但是所需经费也是大量的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不是什么急需的商品，\x01",
            "我还是会采用海运的方式。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29EE")

    TalkEnd(0x13)
    Return()

    # Function_9_2666 end

    def Function_10_29F2(): pass

    label("Function_10_29F2")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2CC7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B65")
    OP_28(0x20, 0x1, 0x4000)

    ChrTalk(
        0xFE,
        (
            "哟，是你们啊，\x01",
            "我不知道仓库的事，\x01",
            "随便向你们发火实在对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来那个冒牌货\x01",
            "就像扎古所说的那样，\x01",
            "无论哪个方面都和我一模一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，真可惜。\x01",
            "要是你们能把他捉起来的话，\x01",
            "一定能得到许多赏金……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哈哈哈，我是开玩笑的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CC4")

    label("loc_2B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2D")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "真没想到市长\x01",
            "会落得那样的下场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来还想和他商量一下，\x01",
            "重新评估港口设备呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "现在要怎么办才好呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC4")

    label("loc_2C2D")


    ChrTalk(
        0xFE,
        (
            "真没想到市长\x01",
            "会落得那样的下场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来还想和他商量一下，\x01",
            "重新评估港口设备呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC4")

    Jump("loc_33FA")

    label("loc_2CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2F88")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E37")
    OP_28(0x20, 0x1, 0x4000)

    ChrTalk(
        0xFE,
        (
            "哟，是你们啊，\x01",
            "我不知道仓库的事，\x01",
            "随便向你们发火实在对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来那个冒牌货\x01",
            "就像扎古所说的那样，\x01",
            "无论哪个方面都和我一模一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，真可惜。\x01",
            "要是你们能把他捉起来的话，\x01",
            "一定能得到许多赏金……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哈哈哈，我是开玩笑的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F85")

    label("loc_2E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EFB")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "这台起重机也很旧了，\x01",
            "也该是换一台新机器的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然，还是要和市长谈谈\x01",
            "港湾设施的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "事情变得越来越麻烦了呀……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F85")

    label("loc_2EFB")


    ChrTalk(
        0xFE,
        (
            "这台起重机也很旧了，\x01",
            "也该是换一台新机器的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然，还是要和市长谈谈\x01",
            "港湾设施的问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F85")

    Jump("loc_33FA")

    label("loc_2F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_3170")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30F8")
    OP_28(0x20, 0x1, 0x4000)

    ChrTalk(
        0xFE,
        (
            "哟，是你们啊，\x01",
            "我不知道仓库的事，\x01",
            "随便向你们发火实在对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来那个冒牌货\x01",
            "就像扎古所说的那样，\x01",
            "无论哪个方面都和我一模一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，真可惜。\x01",
            "要是你们能把他捉起来的话，\x01",
            "一定能得到许多赏金……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哈哈哈，我是开玩笑的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_316D")

    label("loc_30F8")


    ChrTalk(
        0xFE,
        (
            "这里的设施也开始\x01",
            "慢慢变得老化了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀哎呀，有太多事情让我烦恼了。\x02",
    )

    CloseMessageWindow()

    label("loc_316D")

    Jump("loc_33FA")

    label("loc_3170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3285")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3224")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "我以前拜托过市长，\x01",
            "恳请他处理一下\x01",
            "盘踞在仓库的那些人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在一点音讯都没有。\x01",
            "哎呀哎呀，真是麻烦……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3282")

    label("loc_3224")


    ChrTalk(
        0xFE,
        (
            "我以前拜托过市长，\x01",
            "恳请他处理一下\x01",
            "盘踞在仓库的那些人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3282")

    Jump("loc_33FA")

    label("loc_3285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_33FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3368")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "这里有许多即将\x01",
            "装运上外国船只的货物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如今这个年代，\x01",
            "出口最多的果然是导力制品啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起利贝尔制的导力器，\x01",
            "可是世界闻名的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FA")

    label("loc_3368")


    ChrTalk(
        0xFE,
        (
            "外国船只运走的货物\x01",
            "果然要数导力制品最多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起利贝尔制的导力器，\x01",
            "可是世界闻名的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FA")

    TalkEnd(0x14)
    Return()

    # Function_10_29F2 end

    def Function_11_33FE(): pass

    label("Function_11_33FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C6")
    OP_A2(0x416)
    EventBegin(0x0)
    OP_51(0x136, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x136, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3427():
        OP_6C(156000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3427)

    def lambda_3437():
        OP_6B(4100, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3437)

    def lambda_3447():
        OP_6D(28940, 0, 430, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3447)
    Sleep(5000)
    Fade(1000)
    OP_6C(135000, 0)
    OP_6B(2800, 0)
    OP_6D(29580, 0, 8940, 0)
    SetChrPos(0x101, 29440, 0, 8189, 180)
    SetChrPos(0x102, 30100, 0, 9570, 180)
    SetChrPos(0x136, 28520, 0, 9990, 180)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#004F这里好像\x01",
            "尽是些大型的建筑物啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F这里是仓库区域哦。\x02\x03",
            "从外国运来的货物\x01",
            "和其他物品都是保管在这里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "不过，这里有点冷清呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F因为自从飞艇普及之后，\x01",
            "只能在水面上行走的轮船\x01",
            "就用得越来越少了……\x02\x03",
            "听说和过去相比，\x01",
            "这里的卸货量减少了很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F果然， \x01",
            "好像还有很多仓库闲置着呢。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_36C6")

    Return()

    # Function_11_33FE end

    def Function_12_36C7(): pass

    label("Function_12_36C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C17")
    OP_A2(0x417)
    EventBegin(0x0)
    OP_51(0x136, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x136, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xC, 50970, 0, 35000, 0)
    SetChrPos(0xD, 50970, 0, 34260, 0)
    SetChrPos(0x8, 37400, 0, 23790, 0)
    SetChrPos(0x9, 37400, 0, 21720, 0)
    SetChrPos(0xA, 37400, 0, 22740, 0)

    NpcTalk(
        0x8,
        "年轻人的声音",
        "慢着，小姑娘。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(48730, 0, 23120, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(261, 0)
    SetChrPos(0x101, 50170, 0, 23370, 270)
    SetChrPos(0x102, 50380, 0, 22120, 270)
    SetChrPos(0x136, 51330, 0, 22810, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_3814():
        OP_8E(0xFE, 0xBC98, 0x0, 0x5CE4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3814)
    Sleep(200)

    def lambda_3834():
        OP_8E(0xFE, 0xBBA8, 0x0, 0x54D8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3834)
    Sleep(200)

    def lambda_3854():
        OP_8E(0xFE, 0xBA86, 0x0, 0x58D4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3854)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)

    ChrTalk(
        0x101,
        "#004F哎？是叫我们吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P呦～瞧瞧，\x01",
            "看来真的猜对了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "嘿嘿，难得听到女人的声音，\x01",
            "就走过来看看，果然……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#040F请问，有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P嘿嘿，\x01",
            "我看你们从刚才起就在这里闲逛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P既然那么有空，\x01",
            "不如陪我们来玩～玩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043F哎？这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F什么呀，原来是几个流氓啊～\x02\x03",
            "#006F不好意思，\x01",
            "我们正在游览这城市呢。\x02\x03",
            "要玩的话，你们还是去找别人陪吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呦，态度好强硬。\x01",
            "我就喜欢这种类型～㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "想游览的话，\x01",
            "我们来做导游不就搞定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "别理这个毛头小子了， \x01",
            "跟我们去开心开心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#009F等、等等！\x01",
            "什么叫毛头小子！？\x02\x03",
            "像你们这种门外汉，\x01",
            "就算一起上也不是约修亚的……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)

    ChrTalk(
        0x102,
        (
            "#010F算了，艾丝蒂尔。\x01",
            "我根本就没有介意。\x02\x03",
            "所以你也不用替我生气。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        "#003F但、但是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "#2P什么，这小子……\x01",
            "竟然在我们面前耍酷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "真是气人的小鬼……\x01",
            "居然跟两个美人卿卿我我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嘿嘿……\x01",
            "看来要教教你什么叫做社会的严酷了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E19():
        OP_92(0xFE, 0x102, 0x640, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3E19)
    Sleep(100)

    def lambda_3E33():
        OP_92(0xFE, 0x102, 0x640, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3E33)
    Sleep(100)

    def lambda_3E4D():
        OP_92(0xFE, 0x102, 0x6A4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3E4D)
    Sleep(400)
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        "#005F等、等等……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043F请、请不要这样……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(
        0x102,
        (
            "#015F……如果我的态度令你们不舒服，\x01",
            "我可以道歉。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)
    OP_92(0x102, 0xA, 0x3E8, 0x7D0, 0x0)

    ChrTalk(
        0x102,
        (
            "#012F#4P但如果你们要打她们的主意，\x01",
            "……我可是不会手下留情的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3FB0():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3FB0)
    Sleep(100)

    def lambda_3FCB():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3FCB)
    Sleep(100)

    def lambda_3FE6():
        OP_94(0x1, 0xFE, 0xB4, 0x2BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3FE6)
    WaitChrThread(0xA, 0x1)

    ChrTalk(
        0x9,
        "什……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这、这小子搞什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2P装、装什么腔作什么势！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P嘿嘿，想在小姑娘面前\x01",
            "耍帅的心情我是可以理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P不过太逞强的话，\x01",
            "可是会很受伤的哦……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "青年的声音",
        "#3P你们几个，在干什么！\x02",
    )

    CloseMessageWindow()

    def lambda_410F():
        OP_6D(50290, 0, 24500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_410F)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    def lambda_4131():

        label("loc_4131")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4131")

    QueueWorkItem2(0x101, 1, lambda_4131)

    def lambda_4142():

        label("loc_4142")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4142")

    QueueWorkItem2(0x102, 1, lambda_4142)

    def lambda_4153():

        label("loc_4153")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4153")

    QueueWorkItem2(0x136, 1, lambda_4153)

    def lambda_4164():

        label("loc_4164")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4164")

    QueueWorkItem2(0x8, 1, lambda_4164)

    def lambda_4175():

        label("loc_4175")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4175")

    QueueWorkItem2(0x9, 1, lambda_4175)

    def lambda_4186():

        label("loc_4186")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4186")

    QueueWorkItem2(0xA, 1, lambda_4186)
    OP_8E(0xD, 0xC60C, 0x0, 0x6770, 0xBB8, 0x0)

    ChrTalk(
        0x9,
        "嘁……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "来了个烦人的家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#674F你们几个不知悔改的家伙，\x01",
            "又在惹是生非……\x02\x03",
            "年纪也不小了，\x01",
            "一点都不觉得羞耻吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P啰、啰嗦！\x01",
            "你这家伙懂什么！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2P不过是市长的跟班罢了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#671F你说什么……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "男性的声音",
        "#3P……哦？有人叫我吗？\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)

    def lambda_4365():

        label("loc_4365")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_4365")

    QueueWorkItem2(0x101, 1, lambda_4365)

    def lambda_4376():

        label("loc_4376")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_4376")

    QueueWorkItem2(0x102, 1, lambda_4376)

    def lambda_4387():

        label("loc_4387")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_4387")

    QueueWorkItem2(0x136, 1, lambda_4387)

    def lambda_4398():

        label("loc_4398")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_4398")

    QueueWorkItem2(0x8, 1, lambda_4398)

    def lambda_43A9():

        label("loc_43A9")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_43A9")

    QueueWorkItem2(0x9, 1, lambda_43A9)

    def lambda_43BA():

        label("loc_43BA")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_43BA")

    QueueWorkItem2(0xA, 1, lambda_43BA)

    def lambda_43CB():
        OP_8E(0xFE, 0xC60C, 0x0, 0x6770, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_43CB)
    TurnDirection(0xD, 0xC, 400)
    Sleep(500)
    OP_8E(0xD, 0xCBE8, 0x0, 0x6266, 0x7D0, 0x0)
    OP_8C(0xD, 270, 400)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0xC, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)

    ChrTalk(
        0x9,
        "戴、戴尔蒙！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "嘁……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F（这、这是谁啊……\x01",
            "　看起来好有威严的样子。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F（是卢安的市长戴尔蒙先生。）\x02\x03",
            "（年轻的那个，应该是\x01",
            "　担任秘书的基尔巴特先生……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#664F卢安是座自由而传统的城市。\x02\x03",
            "对于你们的衣着和言行，\x01",
            "我承认的确没有权力干涉。\x02\x03",
            "#662F但如果你们敢给他人带来麻烦， \x01",
            "尤其是旅客，就要另当别论了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P哼，啰嗦什么呀。\x01",
            "这个没落贵族的大款市长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2P我可不记得我有义务听你说教。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(
        0xD,
        (
            "#674F你、你们太放肆了！\x02\x03",
            "再不适可而止的话，\x01",
            "是不是又想让我去协会通报！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哼……\x01",
            "说来说去又是游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "难道你就不会\x01",
            "靠自己的本事干点什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就算你去向协会求救，\x01",
            "他们赶过来也要花时间的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "教训了你们之后我们就溜之大吉，\x01",
            "我看你们还拿我们有什么办法。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4856():
        OP_6D(49220, 0, 23720, 1000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4856)
    Sleep(500)

    def lambda_4873():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4873)
    Sleep(200)

    def lambda_4886():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4886)
    Sleep(200)

    def lambda_4899():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_4899)
    WaitChrThread(0xC, 0x1)

    ChrTalk(
        0x101,
        (
            "#007F真不好意思……\x02\x03",
            "根本就用不着去通知，\x01",
            "因为游击士已经在这里了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_490A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_490A)

    def lambda_4918():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4918)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "#2P什、什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F哈～居然到现在\x01",
            "还没注意到这徽章啊。\x02\x03",
            "你们几个，眼神也太不好使了吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔指了指\x01",
            "自己左边胸前的准游击士徽章。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        "这、这是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "游击士的徽章！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "那么，那个小子也……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F没错，正是如此。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8C(0x9, 0, 400)

    ChrTalk(
        0x9,
        "（怎、怎么办？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "（想不到这样的小鬼\x01",
            "　居然会是游击士……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "（什么呀？管他的！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "（就算是游击士，也只不过是\x01",
            "　两个女人和一个毛头小子罢了！）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x8,
        (
            "#2P（蠢、蠢货！\x01",
            "　别光凭外表判断！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P（你忘了吗！？\x01",
            "　前不久我们跟一个女游击士动手，\x01",
            "　结果三人联手还是被她修理了一顿。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P（而、而且不管怎么说……\x01",
            "　他们和『那个人』是一样的！）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_8C(0x8, 90, 400)

    ChrTalk(
        0x8,
        "#2P今、今天就放你们一马！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)

    ChrTalk(
        0x9,
        "咱们就走着瞧吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "哼，算你们好样的！\x02",
    )

    CloseMessageWindow()

    def lambda_4E73():

        label("loc_4E73")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4E73")

    QueueWorkItem2(0x101, 1, lambda_4E73)

    def lambda_4E84():

        label("loc_4E84")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4E84")

    QueueWorkItem2(0x102, 1, lambda_4E84)

    def lambda_4E95():

        label("loc_4E95")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4E95")

    QueueWorkItem2(0x136, 1, lambda_4E95)

    def lambda_4EA6():

        label("loc_4EA6")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4EA6")

    QueueWorkItem2(0xC, 1, lambda_4EA6)

    def lambda_4EB7():

        label("loc_4EB7")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4EB7")

    QueueWorkItem2(0xD, 1, lambda_4EB7)
    OP_8C(0xA, 270, 400)

    def lambda_4ECF():
        OP_6D(48000, 0, 24000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4ECF)

    def lambda_4EE7():
        OP_8E(0xFE, 0x9088, 0x0, 0x58D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4EE7)
    OP_8C(0x8, 270, 400)

    def lambda_4F09():
        OP_8E(0xFE, 0x9088, 0x0, 0x5CEE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4F09)
    OP_8C(0x9, 270, 400)

    def lambda_4F2B():
        OP_8E(0xFE, 0x9088, 0x0, 0x54D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4F2B)
    WaitChrThread(0x9, 0x1)

    ChrTalk(
        0x101,
        (
            "#007F该说什么好呢……\x01",
            "还真是老套的退场词啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过算了，\x01",
            "我想他们应该不会再过来惹事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xC, 0xFF)
    OP_8C(0xC, 180, 400)

    ChrTalk(
        0xC,
        (
            "#660F#2P真是十分抱歉，各位。\x01",
            "那些人刚才给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5052():
        OP_6D(50450, 0, 24070, 1500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_5052)

    def lambda_506A():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_506A)
    OP_8E(0xC, 0xC60C, 0x0, 0x63D8, 0x7D0, 0x0)

    def lambda_508C():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_508C)

    def lambda_509A():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_509A)
    TurnDirection(0x101, 0xC, 400)
    WaitChrThread(0xC, 0x2)

    ChrTalk(
        0xC,
        (
            "#660F还没做自我介绍，\x01",
            "我是卢安的市长戴尔蒙。\x02\x03",
            "#660F而这位就是\x01",
            "我的秘书基尔巴特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#670F请多指教。\x01",
            "你们是游击士吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，我们是从洛连特来的。\x01",
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
        0xC,
        (
            "#660F说起来，\x01",
            "卢安支部的嘉恩说过\x01",
            "会有两个很有前途的新人过来……\x02\x03",
            "莫非就是指二位吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嘿嘿……\x01",
            "是不是有前途还不敢说呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F接下来的一段时间，\x01",
            "我们会在卢安地区工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#661F呀，那可是帮了我们大忙啊。\x02\x03",
            "现在正处于非常时期。\x02\x03",
            "说不定我也会有\x01",
            "需要你们协助的地方，\x01",
            "到时候就请二位多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F非常时期……吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#660F嗯，详细的情况\x01",
            "二位可以向嘉恩询问。\x02\x03",
            "对了，这位小姐\x01",
            "好像是王立学院的学生啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F是的，我是王立学院二年级的\x01",
            "科洛丝·琳希。\x02\x03",
            "初次见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#660F原来如此， \x01",
            "科林兹校长和我可是老交情了。\x02\x03",
            "说起来，\x01",
            "基尔巴特也是王立学院毕业的对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#670F嗯，是的。\x02\x03",
            "你叫科洛丝是吧？\x01",
            "我可是久仰你的大名了哦。\x02\x03",
            "听说你正和学生会长乔儿\x01",
            "一起争夺学生会主席的位置。\x02\x03",
            "有你们这样优秀的后辈，\x01",
            "我这个前辈也是脸上沾光啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#045F这……太过奖了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#661F哈哈哈， \x01",
            "这次的学园祭我也是非常期待啊。\x02\x03",
            "还请多多加油了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#040F是，我一定会尽力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#661F嗯，那么各位。\x01",
            "我们这就告辞了。\x02\x03",
            "要是刚才那些人再来找麻烦，\x01",
            "尽管来通知我就行了。\x02\x03",
            "就让我这个卢安市长\x01",
            "好好地履行管教他们的职责吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_57AC():
        OP_6D(52270, 0, 23490, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_57AC)

    def lambda_57C4():

        label("loc_57C4")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_57C4")

    QueueWorkItem2(0x101, 1, lambda_57C4)

    def lambda_57D5():

        label("loc_57D5")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_57D5")

    QueueWorkItem2(0x102, 1, lambda_57D5)

    def lambda_57E6():

        label("loc_57E6")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_57E6")

    QueueWorkItem2(0x136, 1, lambda_57E6)
    OP_8E(0xC, 0xCD6E, 0x0, 0x5ADC, 0xBB8, 0x0)

    def lambda_580B():
        OP_8E(0xFE, 0xFB54, 0x0, 0x5334, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_580B)
    Sleep(500)
    OP_8E(0xD, 0xD156, 0x0, 0x594C, 0xBB8, 0x0)

    def lambda_583F():
        OP_8E(0xFE, 0xFB54, 0x0, 0x5334, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_583F)
    WaitChrThread(0xD, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)

    ChrTalk(
        0x101,
        (
            "#000F嗯，这个戴尔蒙先生\x01",
            "真是个好有气量和威严的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊，他的言行举止\x01",
            "的确很有作为市长的风范。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_58F9():
        OP_6D(50520, 0, 23090, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_58F9)
    Sleep(500)
    OP_8C(0x136, 270, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x136,
        (
            "#040F因为戴尔蒙家\x01",
            "以前是一个豪门贵族。\x02\x03",
            "虽说贵族制已经被废除了，\x01",
            "但是这家族的人至今仍被视为\x01",
            "上流阶级的代表者。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(
        0x101,
        (
            "#501F哦～……\x01",
            "好像跟我们不是一个世界的呢。\x02\x03",
            "#007F不过呢，话说回来，\x01",
            "这城市怎么会有流氓存在啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#043F是啊。\x01",
            "吓了我一跳呢。\x02\x03",
            "真对不起，\x01",
            "把你们带到不安全的地方来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F你用不着道歉。\x02\x03",
            "而且，\x01",
            "我们也没必要特意去招惹他们。\x02\x03",
            "看来他们经常聚集在\x01",
            "仓库区域最里面那一带，\x01",
            "所以我们就尽量不要靠近那里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F嗯……\x01",
            "虽然有点气愤，但也没办法啦……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_64(0x2, 0x1)
    OP_71(0x13, 0x10)
    EventEnd(0x0)

    label("loc_5C17")

    Return()

    # Function_12_36C7 end

    def Function_13_5C18(): pass

    label("Function_13_5C18")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_22(0xD4, 0x0, 0x64)
    LoadEffect(0x4, "map\\\\mp013_00.eff")
    LoadEffect(0x5, "map\\\\mp013_01.eff")
    PlayEffect(0x4, 0x0, 0x17, 0, 0, 2200, 180, 0, 0, 1000, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x17, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x17, -1310, -2900, 14370, 270)
    SetChrFlags(0x17, 0x40)
    OP_A1(0x17, 0x20)
    OP_72(0x20, 0x4)
    OP_72(0x20, 0x2)
    OP_71(0x20, 0x400)
    OP_71(0x20, 0x40)
    OP_48()
    ClearChrFlags(0x0, 0x4)
    ClearChrFlags(0x1, 0x4)
    ClearChrFlags(0x2, 0x4)
    SetChrPos(0x102, -2350, -2870, 14350, 270)
    SetChrPos(0x101, -1030, -2800, 14700, 90)
    SetChrPos(0x136, -910, -2840, 13890, 90)
    SetChrFlags(0x0, 0x20)
    SetChrFlags(0x1, 0x20)
    SetChrFlags(0x2, 0x20)
    OP_6D(8670, -1800, 15130, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(158000, 0)
    OP_6E(262, 0)
    Sleep(1000)

    def lambda_5D83():
        OP_6D(18890, -1800, 11040, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D83)

    def lambda_5D9B():
        OP_6C(134000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D9B)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x17, 0x4)
    WaitChrThread(0x17, 0x1)

    def lambda_5DBA():
        OP_8F(0xFE, 0x46FA, 0xFFFFF4AC, 0x343A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5DBA)
    Sleep(500)
    OP_82(0x0, 0x2)
    PlayEffect(0x4, 0x2, 0x17, 0, 0, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1, 0x2)

    def lambda_5E15():
        OP_8F(0xFE, 0x46FA, 0xFFFFF4AC, 0x343A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5E15)
    Sleep(500)

    def lambda_5E35():
        OP_8F(0xFE, 0x46FA, 0xFFFFF4AC, 0x343A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5E35)
    WaitChrThread(0x17, 0x1)
    OP_82(0x2, 0x2)
    ClearChrFlags(0x0, 0x20)
    ClearChrFlags(0x1, 0x20)
    ClearChrFlags(0x2, 0x20)

    def lambda_5E67():

        label("loc_5E67")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_5E67")

    QueueWorkItem2(0x101, 1, lambda_5E67)

    def lambda_5E78():

        label("loc_5E78")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_5E78")

    QueueWorkItem2(0x102, 1, lambda_5E78)
    OP_8C(0x136, 180, 400)
    OP_51(0x136, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x136, 0x1000)
    SetChrSubChip(0x136, 4)

    def lambda_5EA5():
        OP_99(0xFE, 0x4, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x136, 3, lambda_5EA5)
    SetChrFlags(0x136, 0x4)
    OP_96(0x136, 0x47AE, 0xFFFFF8F8, 0x2EC2, 0x5DC, 0x1F40)
    OP_51(0x136, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x136, 0x1000)
    ClearChrFlags(0x136, 0x4)
    OP_8E(0x136, 0x4B64, 0xFFFFF8F8, 0x2C56, 0xBB8, 0x0)
    TurnDirection(0x136, 0x101, 400)

    def lambda_5F01():

        label("loc_5F01")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5F01")

    QueueWorkItem2(0x136, 1, lambda_5F01)
    OP_44(0x101, 0xFF)
    SetChrFlags(0x101, 0x4)
    OP_8E(0x101, 0x4768, 0xFFFFF510, 0x3296, 0xBB8, 0x0)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x101, 0x1000)
    SetChrSubChip(0x101, 0)

    def lambda_5F44():
        OP_99(0xFE, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5F44)
    SetChrFlags(0x101, 0x4)
    OP_96(0x101, 0x47AE, 0xFFFFF8F8, 0x2EC2, 0x5DC, 0x1F40)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x101, 0x4)
    OP_8E(0x101, 0x472C, 0xFFFFF8F8, 0x2A58, 0xBB8, 0x0)
    TurnDirection(0x101, 0x102, 400)

    def lambda_5FA0():

        label("loc_5FA0")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_5FA0")

    QueueWorkItem2(0x136, 1, lambda_5FA0)

    def lambda_5FB1():

        label("loc_5FB1")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_5FB1")

    QueueWorkItem2(0x101, 1, lambda_5FB1)
    OP_44(0x102, 0xFF)
    OP_8E(0x102, 0x42AE, 0xFFFFF542, 0x3296, 0xBB8, 0x0)
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x102, 0x1000)
    SetChrSubChip(0x102, 0)
    SetChrFlags(0x102, 0x4)

    def lambda_5FF4():
        OP_99(0xFE, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_5FF4)
    OP_96(0x102, 0x434E, 0xFFFFF8F8, 0x2D46, 0x5DC, 0x1F40)
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x102, 0x1000)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x4)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#002F这里就是……\x01",
            "仓库区域的最南面吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x197, 0x0, 0x64)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x40)
    SetChrPos(0xE, 31110, 6000, 15480, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x136, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)

    def lambda_60FA():

        label("loc_60FA")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_60FA")

    QueueWorkItem2(0x101, 2, lambda_60FA)

    def lambda_610B():

        label("loc_610B")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_610B")

    QueueWorkItem2(0x102, 2, lambda_610B)

    def lambda_611C():

        label("loc_611C")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_611C")

    QueueWorkItem2(0x136, 2, lambda_611C)

    def lambda_612D():
        OP_6D(20890, -1800, 11040, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_612D)
    OP_22(0x8C, 0x0, 0x64)
    OP_92(0xE, 0x136, 0x1388, 0x1F40, 0x0)
    OP_92(0xE, 0x136, 0xFA0, 0x1770, 0x0)
    OP_92(0xE, 0x136, 0xBB8, 0xFA0, 0x0)
    OP_92(0xE, 0x136, 0x7D0, 0x7D0, 0x0)
    OP_8E(0xE, 0x4D58, 0xFFFFFCE0, 0x2CEC, 0x5DC, 0x0)
    OP_44(0x136, 0xFF)
    SetChrFlags(0x136, 0x20)

    def lambda_619F():
        OP_8C(0xFE, 315, 200)
        ExitThread()

    QueueWorkItem(0x136, 3, lambda_619F)
    SetChrChipByIndex(0x136, 14)
    SetChrSubChip(0x136, 2)
    OP_8F(0xE, 0x4C2C, 0xFFFFF9C0, 0x2CBA, 0x3E8, 0x0)
    WaitChrThread(0xE, 0x3)
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Fade(250)
    SetChrFlags(0xE, 0x80)
    SetChrSubChip(0x136, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#004F啊，基库！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#310F啾。\x02\x03",
            "#310F叽啾，啾～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#049F#2P是吗……我知道了。\x02\x03",
            "#042F#2P……那孩子果然\x01",
            "跑到仓库最里面去了。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0xE, 0x80)
    SetChrSubChip(0x136, 2)
    OP_0D()

    def lambda_6293():

        label("loc_6293")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_6293")

    QueueWorkItem2(0x101, 2, lambda_6293)

    def lambda_62A4():

        label("loc_62A4")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_62A4")

    QueueWorkItem2(0x102, 2, lambda_62A4)

    def lambda_62B5():

        label("loc_62B5")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_62B5")

    QueueWorkItem2(0x136, 2, lambda_62B5)

    def lambda_62C6():
        OP_6D(18890, -1800, 11040, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62C6)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_62E3():
        OP_8E(0xFE, 0xC7A6, 0x1770, 0x3C78, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_62E3)
    Sleep(400)

    def lambda_6303():
        OP_8E(0xFE, 0xC7A6, 0x1770, 0x3C78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6303)
    Sleep(400)
    SetChrChipByIndex(0x136, 65535)
    ClearChrFlags(0x136, 0x20)
    SetChrSubChip(0x136, 0)

    def lambda_6332():
        OP_8E(0xFE, 0xC7A6, 0x1770, 0x3C78, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6332)
    WaitChrThread(0xE, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)
    TurnDirection(0x102, 0x136, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x102,
        (
            "#012F我们赶快过去吧。\x01",
            "那帮家伙的地盘就在最里面。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_63BD():
        TurnDirection(0x136, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_63BD)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#005F#2P明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#042F是……！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x80)
    EventEnd(0x0)
    Return()

    # Function_13_5C18 end

    def Function_14_63FD(): pass

    label("Function_14_63FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EXEC_OP, "OP_40(0x334)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6415")
    Call(1, 10)
    Jump("loc_682B")

    label("loc_6415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_653E")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64A9")
    TurnDirection(0x102, 0x1, 400)

    ChrTalk(
        0x102,
        (
            "#012F往这边走就出城了。\x02\x03",
            "现在我们要去市长家，\x01",
            "在王国军到来之前尽量拖延时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6520")

    label("loc_64A9")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#012F往这边走就出城了。\x02\x03",
            "现在我们要去市长家，\x01",
            "在王国军到来之前尽量拖延时间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6520")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_682B")

    label("loc_653E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65D3")
    EventBegin(0x2)
    TurnDirection(0x136, 0x0, 400)

    ChrTalk(
        0x105,
        (
            "#042F往这边走就出城了。\x02\x03",
            "赶快去仓库区找找克拉姆吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_682B")

    label("loc_65D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67AE")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6731")
    OP_A2(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_667D")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F在去城外之前先到协会报到吧。\x01",
            "　\x02\x03",
            "嘉恩先生不是说\x01",
            "要给我们分配工作吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F啊，是这样。\x02",
    )

    CloseMessageWindow()
    Jump("loc_672E")

    label("loc_667D")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F哎……\x01",
            "要到城外去吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F不了，\x01",
            "还是先去协会吧。\x02\x03",
            "嘉恩先生不是说\x01",
            "要给我们分配工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，好的。\x02",
    )

    CloseMessageWindow()

    label("loc_672E")

    Jump("loc_6790")

    label("loc_6731")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F在去城外之前先到协会报到吧。\x01",
            "　\x02\x03",
            "嘉恩先生不是说\x01",
            "要给我们分配工作吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6790")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_682B")

    label("loc_67AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_682B")
    EventBegin(0x2)
    TurnDirection(0x136, 0x0, 400)

    ChrTalk(
        0x136,
        (
            "#040F再往前走就到阿伊纳街道了。\x01",
            "　\x02\x03",
            "我们还是回城里去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_682B")

    Return()

    # Function_14_63FD end

    def Function_15_682C(): pass

    label("Function_15_682C")

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

    # Function_15_682C end

    def Function_16_687B(): pass

    label("Function_16_687B")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_16_687B end

    def Function_17_6882(): pass

    label("Function_17_6882")

    SetPlaceName(0x69) # 卢安市长官邸
    Return()

    # Function_17_6882 end

    def Function_18_6886(): pass

    label("Function_18_6886")

    SetPlaceName(0x52) # 卢安市长官邸
    Return()

    # Function_18_6886 end

    SaveToFile()

Try(main)
