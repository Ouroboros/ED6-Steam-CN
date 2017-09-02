from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T0121   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0121   ._SN',
            'ED6_DT01/T0121_1 ._SN',
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
        '爱娜',                                 # 9
        '雪拉扎德',                             # 10
        '利吉',                                 # 11
        '里农',                                 # 12
        '布露姆老奶奶',                         # 13
        '尤妮',                                 # 14
        '奥维德',                               # 15
        '克劳斯市长',                           # 16
        '目标用摄像机',                         # 17
        '塔罗牌',                               # 18
        '塔罗牌',                               # 19
        '塔罗牌',                               # 20
        '塔罗牌',                               # 21
        '塔罗牌',                               # 22
        '塔罗牌',                               # 23
    )

    DeclEntryPoint(
        Unknown_00              = 4250,
        Unknown_04              = 0,
        Unknown_08              = -2000,
        Unknown_0C              = 4,
        Unknown_0E              = 90,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 2,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 4250,
        Unknown_04              = 0,
        Unknown_08              = -2000,
        Unknown_0C              = 4,
        Unknown_0E              = 90,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 315,
        Unknown_34              = 315,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 2,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02560 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01010 ._CH',             # 03
        'ED6_DT07/CH01760 ._CH',             # 04
        'ED6_DT07/CH01170 ._CH',             # 05
        'ED6_DT07/CH01120 ._CH',             # 06
        'ED6_DT07/CH02350 ._CH',             # 07
        'ED6_DT07/CH00023 ._CH',             # 08
        'ED6_DT06/CH20021 ._CH',             # 09
        'ED6_DT06/CH20133 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02560P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01010P._CP',             # 03
        'ED6_DT07/CH01760P._CP',             # 04
        'ED6_DT07/CH01170P._CP',             # 05
        'ED6_DT07/CH01120P._CP',             # 06
        'ED6_DT07/CH02350P._CP',             # 07
        'ED6_DT07/CH00023P._CP',             # 08
        'ED6_DT06/CH20021P._CP',             # 09
        'ED6_DT06/CH20133P._CP',             # 0A
    )

    DeclNpc(
        X                   = 750,
        Z                   = 0,
        Y                   = 118600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 200,
        Z                   = 0,
        Y                   = 74200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -355,
        Z                   = 0,
        Y                   = 71450,
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
        X                   = 3800,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 47500,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -295,
        Z                   = 0,
        Y                   = 116400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = -3100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 82247,
        Z                   = 0,
        Y                   = 2548,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458761,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 524297,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589833,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 655369,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 720905,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 786441,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -2700,
        Y                   = -500,
        Z                   = 109000,
        Range               = -1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x1B580,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 2900,
        Y                   = -500,
        Z                   = 110700,
        Range               = 5300,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x1ABBC,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = 3810,
        TriggerZ            = 0,
        TriggerY            = 1080,
        TriggerRange        = 800,
        ActorX              = 3800,
        ActorZ              = 1500,
        ActorY              = 2000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1271,
        TriggerZ            = 0,
        TriggerY            = 116402,
        TriggerRange        = 800,
        ActorX              = 750,
        ActorZ              = 1500,
        ActorY              = 118600,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4900,
        TriggerZ            = 0,
        TriggerY            = 112600,
        TriggerRange        = 1400,
        ActorX              = 4900,
        ActorZ              = 2000,
        ActorY              = 112600,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4900,
        TriggerZ            = 0,
        TriggerY            = 112600,
        TriggerRange        = 1400,
        ActorX              = 4900,
        ActorZ              = 2000,
        ActorY              = 112600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3F6",          # 00, 0
        "Function_1_606",          # 01, 1
        "Function_2_660",          # 02, 2
        "Function_3_676",          # 03, 3
        "Function_4_69A",          # 04, 4
        "Function_5_69F",          # 05, 5
        "Function_6_777",          # 06, 6
        "Function_7_4B1C",         # 07, 7
        "Function_8_5A1D",         # 08, 8
        "Function_9_5A22",         # 09, 9
        "Function_10_7F87",        # 0A, 10
        "Function_11_8C9A",        # 0B, 11
        "Function_12_8D4D",        # 0C, 12
        "Function_13_8DF9",        # 0D, 13
        "Function_14_8EA5",        # 0E, 14
        "Function_15_925E",        # 0F, 15
        "Function_16_98ED",        # 10, 16
        "Function_17_9E26",        # 11, 17
        "Function_18_B236",        # 12, 18
        "Function_19_B415",        # 13, 19
        "Function_20_B444",        # 14, 20
        "Function_21_B478",        # 15, 21
        "Function_22_B4A7",        # 16, 22
        "Function_23_D3EF",        # 17, 23
        "Function_24_E399",        # 18, 24
        "Function_25_E3E4",        # 19, 25
        "Function_26_E405",        # 1A, 26
        "Function_27_E421",        # 1B, 27
        "Function_28_E442",        # 1C, 28
        "Function_29_E4A8",        # 1D, 29
        "Function_30_E4FB",        # 1E, 30
        "Function_31_EC90",        # 1F, 31
    )


    def Function_0_3F6(): pass

    label("Function_0_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41F")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 41, 0, 116398, 0)
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_41F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_43C")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 5649, 0, 114874, 0)

    label("loc_43C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_44D")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    label("loc_44D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_459")
    ClearChrFlags(0xD, 0x80)

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_485")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)
    SetChrPos(0xA, -355, 0, 71450, 180)

    label("loc_485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_496")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    label("loc_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_4A7")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_4B8")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_4C9")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)

    label("loc_4C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_4DC")
    SetChrFlags(0x9, 0x80)
    OP_A3(0x3FA)
    Event(0, 16)

    label("loc_4DC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_4F0"),
        (103, "loc_54A"),
        (106, "loc_5D8"),
        (SWITCH_DEFAULT, "loc_5EC"),
    )


    label("loc_4F0")

    ClearMapFlags(0x1)
    SetChrPos(0x101, 1500, 0, 116000, 0)
    SetChrPos(0x102, 700, 0, 115200, 0)
    OP_6D(611, 0, 116942, 0)
    OP_6C(315000, 0)
    FadeToBright(1000, 0)
    OP_B1("t0121_y")
    Event(0, 30)
    Jump("loc_5EC")

    label("loc_54A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 4)), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58B")
    ClearMapFlags(0x1)
    SetChrPos(0x101, 2400, 0, 111120, 0)
    SetChrPos(0x102, 3790, 0, 110540, 0)
    FadeToBright(500, 0)
    Event(0, 18)

    label("loc_58B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    OP_A2(0x268)
    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    Event(0, 17)

    label("loc_5AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D5")

    def lambda_5BC():

        label("loc_5BC")

        TurnDirection(0x9, 0x0, 0)
        OP_48()
        Jump("loc_5BC")

    QueueWorkItem2(0x9, 1, lambda_5BC)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    Event(0, 14)

    label("loc_5D5")

    Jump("loc_5EC")

    label("loc_5D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E9")
    Event(0, 22)

    label("loc_5E9")

    Jump("loc_5EC")

    label("loc_5EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_605")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    Jump("loc_605")

    label("loc_605")

    Return()

    # Function_0_3F6 end

    def Function_1_606(): pass

    label("Function_1_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_633")
    OP_B1("t0121_y")
    Jump("loc_63C")

    label("loc_633")

    OP_B1("t0121_n")

    label("loc_63C")

    OP_64(0x0, 0x2)
    OP_64(0x1, 0x2)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65F")
    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_65F")
    OP_65(0x3, 0x1)

    label("loc_65F")

    Return()

    # Function_1_606 end

    def Function_2_660(): pass

    label("Function_2_660")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_675")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_660")

    label("loc_675")

    Return()

    # Function_2_660 end

    def Function_3_676(): pass

    label("Function_3_676")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_699")
    OP_8D(0xFE, 960, -4400, 2700, -2500, 3000)
    Jump("Function_3_676")

    label("loc_699")

    Return()

    # Function_3_676 end

    def Function_4_69A(): pass

    label("Function_4_69A")

    Call(0, 6)
    Return()

    # Function_4_69A end

    def Function_5_69F(): pass

    label("Function_5_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_6B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B2")
    Call(0, 6)

    label("loc_6B2")

    Jump("loc_776")

    label("loc_6B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_776")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_6F7")

    ChrTalk(
        0x9,
        (
            "#020F你们两个，\x01",
            "快点到爱娜那儿报告去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_773")

    label("loc_6F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_73F")

    ChrTalk(
        0x9,
        (
            "#020F你们两个不要随处乱跑了，\x01",
            "快点到公告板那里确认工作内容吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_773")

    label("loc_73F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_773")

    ChrTalk(
        0x9,
        (
            "#020F你们两个不要随处乱跑了，\x01",
            "赶快把东西接下来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_773")

    TalkEnd(0x9)

    label("loc_776")

    Return()

    # Function_5_69F end

    def Function_6_777(): pass

    label("Function_6_777")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81B")
    FadeToDark(300, 0, 70)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A")
    OP_0D()
    Call(1, 2)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_80A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81B")
    TalkEnd(0x8)
    Return()

    label("loc_81B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_99F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_917")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#740F啊，你们还没出发吗？\x02\x03",
            "要去柏斯的话，\x01",
            "沿米尔西街道往西走就行了。\x02\x03",
            "我已经和那边的\x01",
            "协会支部取得联系了。\x02\x03",
            "你们一路小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99C")

    label("loc_917")


    ChrTalk(
        0x8,
        (
            "#740F要去柏斯的话，\x01",
            "沿米尔西街道往西走就行了。\x02\x03",
            "你们一路小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99C")

    Jump("loc_4B16")

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_2155")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_201F")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 1078, 0, 116398, 0)
    TurnDirection(0x101, 0x9, 0)
    SetChrPos(0x102, 1078, 0, 115280, 0)
    TurnDirection(0x102, 0x9, 0)
    OP_44(0x9, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    TurnDirection(0x9, 0x101, 0)
    OP_6D(270, 0, 117230, 0)
    OP_6B(2800, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x9,
        "#020F#1P哎呀，艾丝蒂尔、约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4P啊，雪拉姐？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F真少见啊，\x01",
            "平时总是看到你在外面奔波的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#020F#1P老师交待给我的工作\x01",
            "终于都做完了。\x02\x03",
            "#020F刚刚回来进行报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#4P啊，雪拉姐也完成了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#027F#1P嗯，总算完成了。\x02\x03",
            "#027F爱娜已经告诉我了。\x01",
            "看来你们也很努力是吗？\x02\x03",
            "#027F不过话说回来，能学到东西，\x01",
            "即使辛苦点也是值得的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#4P嘿嘿，知道啦雪拉姐。\x02\x03",
            "#008F那么……\x01",
            "我们也赶快报告吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x8,
        "#740F好的，你们说吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人报告了当记者护卫的经过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_28(0x19, 0x4, 0x10)
    OP_28(0x19, 0x1, 0x100)
    Sleep(100)
    OP_AF(0x4, 0x19)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#741F好的，真是辛苦了。\x02\x03",
            "怎么样，雪拉扎德。\x01",
            "不觉得他们成长了很多吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)
    TurnDirection(0x101, 0x9, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_EE5")

    ChrTalk(
        0x9,
        (
            "#022F#1P还太嫩了点呢。\x01",
            "在塔里的多余行动还是比较多。\x02\x03",
            "#022F你们的任务不单是战斗，\x01",
            "还要确保保护对象不受伤害才行。\x02\x03",
            "#022F记住以后工作需要更加谨慎，\x01",
            "做好每一个细节是游击士应有的职责。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F#4P唔唔……雪拉姐好严呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_EE5")


    ChrTalk(
        0x9,
        (
            "#027F#1P作为新人来说干得还不错。\x02\x03",
            "#027F不过，可不能这样就满足哦。\x02\x03",
            "#027F特别是艾丝蒂尔，\x01",
            "你啊，总是容易得意忘形。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F#4P嗯……好啦。\x01",
            "我知道啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE6")


    ChrTalk(
        0x8,
        (
            "#741F呵呵，艾丝蒂尔、约修亚，\x01",
            "还有雪拉扎德，你们都辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "#740F卡西乌斯先生留下的空缺，\x01",
            "没想到能这么快就填补上了。\x02\x03",
            "这么一来，\x01",
            "可以暂时放松一段时间了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#4P那样的话，\x01",
            "反倒觉得有点无聊呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F还有巡视街道和消灭魔兽这样的琐碎工作嘛，\x01",
            "没有关系啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#027F#1P呵呵……\x01",
            "好久没有这么悠闲了呢。\x02\x03",
            "#021F好，今晚一定要喝个痛快～！\x02\x03",
            "#021F艾丝蒂尔、约修亚，\x01",
            "你们两人一定要来陪我哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x9, 400)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        (
            "#004F#4P啊～……\x01",
            "要去陪喝醉的雪拉姐吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#022F#1P哎呀，艾丝蒂尔，\x01",
            "你想拒绝我的邀请吗？\x02\x03",
            "#022F哼哼，真是够胆量呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#4P因、因为雪拉姐的酒品\x01",
            "实在差得一塌糊涂啊！\x02\x03",
            "#007F又大吵大闹，又跳舞，还脱衣服……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F的确是……\x01",
            "连我们都觉得不好意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#745F我说雪拉扎德，\x01",
            "你对未成年人都做了些什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#024F#1P什么呀，只是喝酒的助兴节目啦。\x02\x03",
            "#025F哼，既然这么不情愿的话，\x01",
            "这次就先饶过艾丝蒂尔你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#4P啊，真的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#020F#1P嗯～～\x02",
    )

    CloseMessageWindow()
    OP_92(0x9, 0x102, 0x2BC, 0xBB8, 0x0)
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x9, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#021F#1P不过作为补偿，\x01",
            "就把你那份算到约修亚的头上吧㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#018F啊……\x02\x03",
            "#018F那、那个，雪拉姐姐……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F#4P慢、慢着！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#027F#1P唔呼呼～\x01",
            "谁叫你约修亚又正经又晚熟啊㈱\x02\x03",
            "#027F不管是喝酒，还是其他什么的，\x01",
            "各种各样的事姐姐都会教你哦⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F各、各种各样……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#009F#4P喂，约修亚……\x01",
            "你干嘛一脸色色的样子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F你、你误会啦！\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0xF, 4147, 0, 110113, 315)

    NpcTalk(
        0xF,
        "老人的声音",
        "不、不好啦！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0xF, 0)
    TurnDirection(0x102, 0xF, 0)
    TurnDirection(0x101, 0xF, 0)
    OP_8E(0xF, 0x6AC, 0x0, 0x1B280, 0xFA0, 0x0)
    TurnDirection(0x9, 0xF, 0)
    TurnDirection(0x102, 0xF, 0)
    TurnDirection(0x101, 0xF, 0)
    OP_8E(0xF, 0x4A6, 0x0, 0x1BB8E, 0xFA0, 0x0)
    OP_43(0x101, 0x1, 0x0, 0x19)
    OP_43(0x102, 0x1, 0x0, 0x1A)
    OP_43(0x9, 0x1, 0x0, 0x1B)
    OP_6D(810, 0, 115660, 1000)

    ChrTalk(
        0x101,
        "#004F#2P咦，市长爷爷？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#603F呼呼……哈哈……\x02\x03",
            "#604F艾丝蒂尔、约修亚……\x01",
            "哦哦，雪拉扎德也在啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F（还好救兵来了……）\x01",
            "发生什么事了，这么慌张？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#604F不、不得了的大事啊！\x02\x03",
            "强盗不在家的时候，\x01",
            "刚好有我闯进来啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#2P啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#025F我说市长，\x01",
            "您先镇静一下。\x02\x03",
            "#020F深吸一口气，然后慢慢吐出来。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x9, 400)

    ChrTalk(
        0xF,
        (
            "#604F嗯、嗯……\x02\x03",
            "#603F吸～～……呼～～……\x02\x03",
            "#603F…………………………\x02\x03",
            "#602F……其实是这样的，\x01",
            "我不在家的时候，刚好有强盗闯进来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#2P啊～～～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#022F那就不该镇静了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#602F因为我有些话要和教区长谈，\x01",
            "所以刚才一直呆在教堂里……\x02\x03",
            "回家的时候没有人出来迎接，\x01",
            "觉得奇怪就在屋里到处查看了一下，\x01",
            "才发现原来有强盗闯进来过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#2P等、等一下……\x01",
            "米蕾奴婶婶她们呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#600F还好，她们都平安无事。\x01",
            "只是被关在阁楼里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#2P太、太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#022F没有人受伤，\x01",
            "总算是不幸中的万幸啊……\x02\x03",
            "#022F反正呆在这里也无济于事，\x01",
            "市长，能让我们调查一下现场吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#602F嗯，拜托你们了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#2P等一下，我们也要去！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是啊。\x01",
            "说不定能帮上什么忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#025F呼，真拿你们没办法……\x02",
    )

    CloseMessageWindow()

    def lambda_1EDD():
        OP_6D(270, 0, 117230, 1000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1EDD)
    TurnDirection(0x9, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "#022F爱娜。\x01",
            "我们去调查案件了。\x02\x03",
            "#022F如果有什么事情，\x01",
            "就全部交给利吉去办吧。\x02\x03",
            "#022F反正他肯定在酒馆闲着的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#742F嗯，我知道了，\x01",
            "大家也要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    NewScene("ED6_DT01/T0210   ._SN", 1, 0, 0)
    IdleLoop()
    Jump("loc_2152")

    label("loc_201F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BE")

    ChrTalk(
        0x8,
        (
            "#740F竟敢闯入市长官邸，\x01",
            "这伙强盗胆子真不小啊。\x02\x03",
            "事件的调查就拜托你们了。\x01",
            "你们三个都要小心行事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2152")

    label("loc_20BE")


    ChrTalk(
        0x8,
        (
            "#740F调查方面怎么样了？\x02\x03",
            "这里的工作就都交给利吉了。\x01",
            "　\x02\x03",
            "你们就集中精力\x01",
            "去调查这件失窃案件吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2152")

    Jump("loc_4B16")

    label("loc_2155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_2340")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22C1")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#740F……对了， \x01",
            "要是碰到里农的妈妈，\x01",
            "麻烦帮我带下话。\x02\x03",
            "#741F就说请她找城镇里的其他女性吧。\x01",
            "　\x02\x03",
            "不好意思， \x01",
            "我还不打算结婚呢。\x02\x03",
            "#740F呵呵，要是真的出现很棒的人，\x01",
            "也许我会改变想法的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233D")

    label("loc_22C1")


    ChrTalk(
        0x8,
        (
            "#740F哦，是去『翡翠之塔』啊，\x01",
            "那要小心点了。\x02\x03",
            "虽然你们去过那里，\x01",
            "不过行动时也务必不要大意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_233D")

    Jump("loc_4B16")

    label("loc_2340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_2DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C05")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 1390, 0, 115970, 0)
    SetChrPos(0x102, 410, 0, 115820, 0)
    OP_8C(0x8, 180, 0)
    ClearMapFlags(0x1)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x3E8)
    OP_A2(0x250)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#740F辛苦了。\x01",
            "矿山似乎发生了不得了的事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4P啊，爱娜姐姐你也知道了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F矿山那边已经送来消息了。\x01",
            "还对你们的帮忙感激不尽呢。\x02\x03",
            "好了，把那里发生的事情经过\x01",
            "详细地报告给我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好的，那么——\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_AF(0x4, 0x3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#740F呵呵……\x01",
            "比预想的做得更好呢。\x02\x03",
            "应对突发事件，\x01",
            "也是游击士的使命之一哦。\x02\x03",
            "以后也拜托了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#001F#4P嗯，尽管交给我们吧☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F嗯，艾丝蒂尔她啊，\x01",
            "就算没有人委托，也会自动去做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F#4P对，对………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#005F#4P喂！\x01",
            "不要把人说得跟管家婆一样嘛！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015F不管怎么说，事实就是如此啊。\x02\x03",
            "老好人心肠，好奇心旺盛，\x01",
            "还有直率的性格就是你的特点嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#009F#4P唔……约修亚，\x01",
            "你这样打击人也太过分了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F是你太敏感了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#740F哎呀，怎么又吵起来了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "#740F好了，我来介绍一下\x01",
            "你们要做的最后一项任务吧。\x02\x03",
            "你们知道《利贝尔通讯》吗？\x01",
            "这次要协助他们进行取材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#4P啊，那不是……\x01",
            "之前帮老爸买的杂志吗。\x02\x03",
            "#004F嘿～还真是有趣的巧合啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F协助取材……\x01",
            "具体要做些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F因为要去危险的场所取材，\x01",
            "所以需要身手不凡的向导。\x02\x03",
            "详细的情况，直接向委托人询问吧。\x02\x03",
            "杂志社的记者和摄影师\x01",
            "正暂住在『洛连特旅馆』。\x02\x03",
            "啊，这个是协会的介绍信。\x02",
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
            "得到了\x07\x02",
            "游击士协会的介绍信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x19, 0x4, 0x4)
    OP_28(0x19, 0x1, 0x1)
    OP_28(0x19, 0x1, 0x2)
    OP_3E(0x324, 1)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F#4P那好，\x01",
            "我们现在就去旅馆看看吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F是啊，走吧。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_2DEE")

    label("loc_2C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D6B")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#740F……对了， \x01",
            "要是碰到里农的妈妈，\x01",
            "麻烦帮我带下话。\x02\x03",
            "#741F就说请她找城镇里的其他女性吧。\x01",
            "　\x02\x03",
            "不好意思， \x01",
            "我还不打算结婚呢。\x02\x03",
            "#740F呵呵，要是真的出现很棒的人，\x01",
            "也许我会改变想法的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEE")

    label("loc_2D6B")


    ChrTalk(
        0x8,
        (
            "#740F这次任务的委托人\x01",
            "正暂住在『洛连特旅馆』。\x02\x03",
            "给他看推荐信，\x01",
            "并向他咨询详细的工作内容就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DEE")

    Jump("loc_4B16")

    label("loc_2DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_38B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F0")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 1390, 0, 115970, 0)
    SetChrPos(0x102, 410, 0, 115820, 0)
    OP_8C(0x8, 180, 0)
    ClearMapFlags(0x1)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x3E8)
    OP_A2(0x23A)

    ChrTalk(
        0x8,
        (
            "#740F辛苦了。\x01",
            "农场的工作还顺利吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#4P嗯，虽然有点小波折……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F总之先报告吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人报告了在农场执行任务的经过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(100)
    OP_AF(0x4, 0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#740F原来如此。\x01",
            "最后还是把魔兽放走了啊。\x02\x03",
            "虽然觉得这种做法有欠考虑……\x01",
            "不过这次就不追究了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4P啊？这可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F游击士的使命是保卫百姓、维护正义……\x01",
            "　\x02\x03",
            "然而保护的方式有很多种，\x01",
            "正义的存在形式也多如繁星。\x02\x03",
            "所以，把握好做事的尺度\x01",
            "也是你们的工作之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F原来如此……\x01",
            "还真是很深奥啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#744F因为我们不仅要打倒魔兽，\x01",
            "有时还要调停国家间的争端。\x02\x03",
            "高级的游击士除了具备优秀战斗力，\x01",
            "还要有纵观全局的判断力以及\x01",
            "灵活处理问题的能力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F判断力和处理问题的能力吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#4P唔唔～……\x01",
            "成为一流游击士的道路还真艰辛啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#741F呵呵，每天都要有进步才行哦。\x02\x03",
            "#740F接下来……\x01",
            "该交给你们下一个任务了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4P我们正等着呢！\x01",
            "快点告诉我们内容吧。\x02\x03",
            "#006F这次还是打倒魔兽之类的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F不，是运送物品的工作。\x02\x03",
            "委托人是克劳斯市长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4P啊，是市长委托的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F这样好吗？\x01",
            "把这么重要的任务交给我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F据说是很简单的工作。\x02\x03",
            "总之，\x01",
            "详细情况可以先向市长询问一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3, 0x1, 0x1)
    OP_28(0x3, 0x4, 0x4)
    EventEnd(0x0)
    Jump("loc_38AE")

    label("loc_36F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_3794")

    ChrTalk(
        0x8,
        (
            "#744F呼呼，之前那次\x01",
            "还没有和雪拉分胜负呢。\x02\x03",
            "#740F她回来之后，\x01",
            "要再约她到酒馆去喝一回。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38AE")

    label("loc_3794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_END)), "loc_37F6")

    ChrTalk(
        0x8,
        (
            "#740F嗯，原来是去玛鲁加矿山啊。\x02\x03",
            "那你们路上要小心点哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38AE")

    label("loc_37F6")


    ChrTalk(
        0x8,
        (
            "#740F这次任务的详细情况\x01",
            "要直接向克劳斯市长咨询。\x02\x03",
            "克劳斯市长的官邸就在城镇的东面。\x01",
            "　\x02\x03",
            "……你们应该知道的吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38AE")

    Jump("loc_4B16")

    label("loc_38B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3FC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F07")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 1390, 0, 115970, 0)
    SetChrPos(0x102, 410, 0, 115820, 0)
    OP_8C(0x8, 180, 0)
    ClearMapFlags(0x1)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x3E8)
    OP_A2(0x22C)
    OP_28(0x2, 0x4, 0x4)
    OP_28(0x2, 0x1, 0x1)
    OP_28(0x2, 0x1, 0x2)

    ChrTalk(
        0x8,
        (
            "#740F哎呀，艾丝蒂尔、约修亚。\x02\x03",
            "卡西乌斯先生已经出发了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#4P嗯，刚刚才走。\x02\x03",
            "#000F爱娜姐姐，\x01",
            "还是快点把老爸\x01",
            "留下来的工作介绍给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F我知道了。\x02\x03",
            "要拜托你们去做的任务一共有三个……\x01",
            "　\x02\x03",
            "首先，\x01",
            "需要你们去西边的农场一趟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4P西边的农场，不就是缇欧的家吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#743F缇欧？\x01",
            "这名字我好像在哪听到过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F她是和我们同级的同学，\x01",
            "叫缇欧·帕赛尔。\x02\x03",
            "#010F帕赛尔农场家的女儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F哦，是这样啊。\x02\x03",
            "你们的任务就是\x01",
            "打倒帕赛尔农场里的魔兽。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#4P啊……有魔兽出没吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F嗯，所幸的是没有人受伤，\x01",
            "不过农田被破坏了也很伤脑筋呢。\x02\x03",
            "所以农场才向协会提出了请求。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#4P有这种事啊……\x02\x03",
            "#002F嗯，我知道了！\x01",
            "我们马上就赶过去！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#740F那么，把这个带上吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "游击士协会的介绍信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x320, 1)

    ChrTalk(
        0x8,
        (
            "#740F这封是介绍信。\x01",
            "可以证明你们是协会派遣的。\x02\x03",
            "把信交给农场的主人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#4P缇欧的爸爸认识我们，\x01",
            "所以我觉得没这个必要……\x02\x03",
            "#501F不过还是拿着吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_3FC5")

    label("loc_3F07")


    ChrTalk(
        0x8,
        (
            "#740F你们第一个任务就是\x01",
            "消灭帕赛尔农场里的魔兽。\x02\x03",
            "要去农场，沿着西面那条\x01",
            "米尔西街道走到一半再向南拐就行了。\x02\x03",
            "这件事拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FC5")

    Jump("loc_4B16")

    label("loc_3FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_4126")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40BB")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#741F才刚当上游击士就已经那么忙。\x02\x03",
            "真是辛苦你们了。\x01",
            "明天也要继续加油哦。\x02\x03",
            "#740F那可是寄给卡西乌斯的信件，\x01",
            "我想应该是很重要的联络信吧。\x01",
            "一定要记得交给他哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4123")

    label("loc_40BB")


    ChrTalk(
        0x8,
        (
            "#740F那可是寄给卡西乌斯的信件，\x01",
            "我想应该是很重要的联络信吧。\x01",
            "一定要记得交给他哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4123")

    Jump("loc_4B16")

    label("loc_4126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_41D7")

    ChrTalk(
        0x8,
        (
            "#740F那两个孩子就拜托你们了。\x02\x03",
            "翡翠之塔就在通往玛鲁加山道途中\x01",
            "往西拐的那个方向。\x02\x03",
            "玛鲁加山道从城镇的北边出去就是了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B16")

    label("loc_41D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_4356")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E1")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#740F恭喜！\x01",
            "你们俩终于正式成为游击士了。\x02\x03",
            "最近协会的工作比较多，\x01",
            "你们也会开始忙起来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F嘿嘿，这正是我期待的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请多指教。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4353")

    label("loc_42E1")


    ChrTalk(
        0x8,
        (
            "#740F最近协会的工作比较多，\x01",
            "你们也会开始忙起来哦。\x02\x03",
            "请多多指教哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4353")

    Jump("loc_4B16")

    label("loc_4356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_440E")

    ChrTalk(
        0x8,
        (
            "#740F实地考试合格的话，\x01",
            "你们就能正式成为游击士了。 \x02\x03",
            "如果要报告已经完成的工作任务，\x01",
            "在菜单上选择『报告』就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B16")

    label("loc_440E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4444")

    ChrTalk(
        0x8,
        "#740F哎呀，公告板就在那边呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B16")

    label("loc_4444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4A66")
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    OP_A2(0xD)

    ChrTalk(
        0x8,
        (
            "#740F这是很重要的东西，\x01",
            "所以千万别弄丢哦。\x02",
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
            "得到了\x07\x02",
            "游击士手册\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x208, 1)
    SetMessageWindowPos(72, 320, 56, 3)
    TurnDirection(0x101, 0x9, 400)
    TurnDirection(0x102, 0x9, 400)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x320)

    ChrTalk(
        0x9,
        (
            "#020F那是游击士手册，\x01",
            "就是用来记录工作细节的正规手册。\x02\x03",
            "#020F无论从谁那里听到了什么情报，\x01",
            "还是在哪里发现了什么东西……\x02\x03",
            "#020F这些细微的事件\x01",
            "经常都会成为调查的线索。\x02\x03",
            "#020F工作中就算是再小的事，\x01",
            "也一定要做记录。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#2P#1K明白了。\x02",
    )


    ChrTalk(
        0x101,
        "#509F#4P#1K嘁，真是麻烦……\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    ChrTalk(
        0x9,
        (
            "#026F哎呀？\x02\x03",
            "不知道是不是我多心。\x01",
            "怎么只听到一个回答的声音？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F啊、啊哈哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#020F记录工作过程中的详细内容是\x01",
            "游击士重要的职责哦。\x02\x03",
            "开始的时候也许会觉得麻烦，\x01",
            "不过你们无论如何都要好好去习惯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F好～的，我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#020F呼，知道就好。\x02\x03",
            "#020F……那么，\x01",
            "就用实际行动证明给我看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_8C(0x9, 135, 400)

    ChrTalk(
        0x9,
        (
            "#020F看门口那边。\x01",
            "看到竖在那里的公告板吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    OP_8C(0x102, 135, 400)
    OP_6D(3915, 0, 113532, 1000)

    ChrTalk(
        0x9,
        (
            "#020F你们去公告板那里，\x01",
            "试试确认一下工作的内容吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※靠近公告板会出现『！』的标记，\x01",
            "　点击右键可以浏览公告板的内容。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※点击列出的各任务的名称，\x01",
            "　就可以看见该任务的详细内容和信息。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x1)

    def lambda_4A54():

        label("loc_4A54")

        TurnDirection(0x9, 0x0, 0)
        OP_48()
        Jump("loc_4A54")

    QueueWorkItem2(0x9, 1, lambda_4A54)
    OP_65(0x3, 0x1)
    Jump("loc_4B16")

    label("loc_4A66")


    ChrTalk(
        0x8,
        (
            "#740F今天的研修结束之后，\x01",
            "你们就会正式成为游击士的一员了。\x02\x03",
            "雪拉扎德正在二楼等着你们呢。\x01",
            "　\x02\x03",
            "要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B16")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    # Function_6_777 end

    def Function_7_4B1C(): pass

    label("Function_7_4B1C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4D26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CC0")
    OP_A2(0x6)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "雪、雪拉前辈。\x01",
            "我听说您要带他们两个\x01",
            "到柏斯那里去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "卡西乌斯先生也不在，\x01",
            "这里只有我一个人不要紧吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#024F你说什么呀。\x01",
            "你要知道自己是个男人。\x02\x03",
            "#020F虽说工作可能比较多，\x01",
            "而且有些也比较难做，\x01",
            "不过大家就看你的啦。\x02\x03",
            "#020F这里就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "知、知道了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D23")

    label("loc_4CC0")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "雪拉前辈，\x01",
            "我会好好努力工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "也请你们路上要小心。\x02",
    )

    CloseMessageWindow()

    label("loc_4D23")

    Jump("loc_5A19")

    label("loc_4D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_4E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E2A")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "啊，艾丝蒂尔和约修亚啊。\x01",
            "市长官邸的事情我听说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "空贼逃到天上，\x01",
            "这样也拿他们没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不管怎样，大家都辛苦了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E69")

    label("loc_4E2A")


    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们背着旅行包，\x01",
            "打算要去做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E69")

    Jump("loc_5A19")

    label("loc_4E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_4FB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F59")
    OP_A2(0x6)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "啊，雪拉前辈……\x01",
            "难道你们三人在一起工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是啊。\x02\x03",
            "也许我的那部分工作会交给你，\x01",
            "到时候就麻烦你了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是！\x01",
            "我会尽力加油的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB2")

    label("loc_4F59")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "烦琐的工作都交给我吧，\x01",
            "你们就专心去做这件工作好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FB2")

    Jump("loc_5A19")

    label("loc_4FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_512D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50E8")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "说起来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有个和雪拉前辈同辈的人，\x01",
            "是柏斯出身的很厉害的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且听说\x01",
            "他最近也很活跃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "大家都很厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我进协会也有三年了……\x01",
            "必须要继续努力才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_512A")

    label("loc_50E8")


    ChrTalk(
        0xFE,
        (
            "我进协会也有三年了……\x01",
            "必须要继续努力才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_512A")

    Jump("loc_5A19")

    label("loc_512D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_5433")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53BC")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "艾丝蒂尔，\x01",
            "你们也是由雪拉前辈带着训练的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那和我一样了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实被雪拉前辈训练\x01",
            "可是我的骄傲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为她也是王国里\x01",
            "首屈一指的游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一起工作的话，你就会知道\x01",
            "『银闪』的称号可不是浪得虚名的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "卡西乌斯先生也是，\x01",
            "洛连特支部多亏了前辈们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F雪拉姐果然是很厉害的人啊……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F一听别人说，\x01",
            "感觉马上就不一样了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5430")

    label("loc_53BC")


    ChrTalk(
        0xFE,
        (
            "雪拉前辈也是，\x01",
            "卡西乌斯先生也是，\x01",
            "洛连特支部多亏了前辈们啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5430")

    Jump("loc_5A19")

    label("loc_5433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_57EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_577A")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "啊，卡西乌斯先生\x01",
            "要出差一段时间了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F我的老爸真是一点也不考虑到家里，\x01",
            "老是随随便便就出差了。\x01",
            "　\x02\x03",
            "这样也能好好工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "卡西乌斯先生可是\x01",
            "我们洛连特支部的脸面人物啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前所有重要的\x01",
            "委托全部都是拜托\x01",
            "卡西乌斯先生去完成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F是这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，最近开始\x01",
            "也有些拜托雪拉前辈的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过好像大多是从\x01",
            "其他支部过来的直接委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此他们才会\x01",
            "经常到外地出差呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F是这样啊，我都不知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……嗯，\x01",
            "因为我们都还是新人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯，在家里的时候\x01",
            "他只是个不良中年。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57E7")

    label("loc_577A")


    ChrTalk(
        0xFE,
        (
            "敬仰卡西乌斯先生的\x01",
            "游击士可是很多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我也是其中之一。\x02",
    )

    CloseMessageWindow()

    label("loc_57E7")

    Jump("loc_5A19")

    label("loc_57EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_59EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5985")
    OP_A2(0x6)

    ChrTalk(
        0xA,
        "呀，是艾丝蒂尔和约修亚啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，利吉哥哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "研修好像结束了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你们两个可是游击士行列里年纪最小的，\x01",
            "真是后生可畏啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "同为游击士的我\x01",
            "以后要请你们多多关照哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F彼此彼此，\x01",
            "请您多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我马上就要去工作了。\x01",
            "如果有什么事情不明白，\x01",
            "不用客气尽管来问我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59EB")

    label("loc_5985")


    ChrTalk(
        0xA,
        (
            "我马上就要去工作了。\x01",
            "如果有什么事情不明白，\x01",
            "不用客气尽管来问我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59EB")

    Jump("loc_5A19")

    label("loc_59EE")


    ChrTalk(
        0xA,
        (
            "这个时候\x01",
            "我没有出现在这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A19")

    TalkEnd(0xA)
    Return()

    # Function_7_4B1C end

    def Function_8_5A1D(): pass

    label("Function_8_5A1D")

    Call(0, 9)
    Return()

    # Function_8_5A1D end

    def Function_9_5A22(): pass

    label("Function_9_5A22")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_5AB2")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AA1")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_5A8A")
    OP_A9(0x8)
    Jump("loc_5A98")

    label("loc_5A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_5A96")
    OP_A9(0x7)
    Jump("loc_5A98")

    label("loc_5A96")

    OP_A9(0x2)

    label("loc_5A98")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_5AA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AB2")
    TalkEnd(0xB)
    Return()

    label("loc_5AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_5DC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CF4")
    OP_A2(0x4)

    ChrTalk(
        0xB,
        (
            "哟，你们都拿着行李，\x01",
            "难道说你们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "要到哪里去工作？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，\x01",
            "我们要到柏斯那里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "柏、柏斯？\x01",
            "可是，现在定期船停航了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……难道你们\x01",
            "打算走路过去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没错，其实我听说\x01",
            "这段路程也不算非常远。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "虽说不是很远，\x01",
            "不过我想也不会很近吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "就算是游击士也应该很辛苦吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你们带的东西准备充足了吗？\x01",
            "路上一定要小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DBE")

    label("loc_5CF4")


    ChrTalk(
        0xB,
        (
            "说起柏斯，那是个商人的城市吧。\x01",
            "我最近也没去过那里呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "以前为了学习店铺的经营方法，\x01",
            "曾去过那里好几次。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DBE")

    Jump("loc_7F83")

    label("loc_5DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_608A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6029")
    OP_A2(0x4)

    ChrTalk(
        0xB,
        (
            "哎呀，三个游击士聚在一块儿，\x01",
            "是发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，有点工作要做。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "你们要加油哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "说起来，\x01",
            "雪拉扎德小姐\x01",
            "你订的附件终于到了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "因为是通过共和国那边弄来的，\x01",
            "所以花了点时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F啊，真的？\x01",
            "多谢了。\x02\x03",
            "不过现在正忙着，\x01",
            "等下次有空了再来拿吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "那好，我等着。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6087")

    label("loc_6029")


    ChrTalk(
        0xB,
        (
            "三位工作结束之后，\x01",
            "还请常来小店逛逛啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6087")

    Jump("loc_7F83")

    label("loc_608A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_62B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_620D")
    OP_A2(0x4)

    ChrTalk(
        0xB,
        (
            "最近街上的人\x01",
            "总是朝我看上看下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "大概是\x01",
            "老妈到处去\x01",
            "替我说亲的缘故。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "知道这事的时候\x01",
            "真是羞得我脸上火辣辣的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我劝她别这么做了，\x01",
            "但怎么说她也听不进，真头疼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B5")

    label("loc_620D")


    ChrTalk(
        0xB,
        (
            "大概是\x01",
            "老妈到处去\x01",
            "替我说亲的缘故。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "知道这事的时候\x01",
            "真是羞得我脸上火辣辣的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62B5")

    Jump("loc_7F83")

    label("loc_62B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_63F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A4")
    OP_A2(0x4)

    ChrTalk(
        0xB,
        (
            "老妈真是的，\x01",
            "忽然要我去相亲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我都跟她说了\x01",
            "暂时不想结婚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "可她完全当作耳旁风。\x01",
            "真是怕了她……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F0")

    label("loc_63A4")


    ChrTalk(
        0xB,
        (
            "我还没打算\x01",
            "要这么早成家啦……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63F0")

    Jump("loc_7F83")

    label("loc_63F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_6649")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65DC")
    OP_A2(0x4)

    ChrTalk(
        0xB,
        (
            "哟，是艾丝蒂尔啊。\x01",
            "最近很忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "都没见你来买零食吃，\x01",
            "真有点寂寞呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F哦……\x01",
            "说起来以前研修回来的路上，\x01",
            "经常走着走着你就不见了，原来……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#009F什、什么嘛……\x01",
            "这有什么关系啊。\x02\x03",
            "买零食吃\x01",
            "是花季女孩的特权嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    ChrTalk(
        0xB,
        (
            "哈哈，你们休息日有空的话，\x01",
            "还请多多光顾小店啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "艾丝蒂尔喜欢的运动鞋\x01",
            "我也会多多留意的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6646")

    label("loc_65DC")


    ChrTalk(
        0xB,
        (
            "哈哈，你们休息日有空的话，\x01",
            "还请多多光顾小店啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "艾丝蒂尔喜欢的运动鞋\x01",
            "我也会多多留意的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6646")

    Jump("loc_7F83")

    label("loc_6649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_66EC")

    ChrTalk(
        0xB,
        (
            "刚才飞行船『林德号』\x01",
            "好像已经到达停机坪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "从柏斯采购来的商品\x01",
            "应该也已经到了，\x01",
            "得过去取回来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F83")

    label("loc_66EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_67B2")

    ChrTalk(
        0xB,
        (
            "呀，是二位游击士新人啊。\x01",
            "我为你们的活跃表现感到很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不过小店马上就要打佯了，\x01",
            "要买东西就请快点挑选好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F83")

    label("loc_67B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B65")
    OP_A2(0x208)
    OP_A2(0x4)

    ChrTalk(
        0x101,
        "#001F早上好，里农叔叔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "哟，这不是艾丝蒂尔和约修亚嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "这么大清早就来这儿还真是少见哦。\x01",
            "是来买新鞋子吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊～进了新货吗？\x02\x03",
            "#001F难道是『斯托雷加』的新产品？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#018F一转眼就把来这里的目的忘掉了。\x02\x03",
            "父亲的吩咐已经忘了吗？ \x01",
            "我们是来买《利贝尔通讯》啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F啊，对对对☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "呵呵，艾丝蒂尔\x01",
            "还是那么热衷于收集运动鞋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不过真是很遗憾啊，\x01",
            "『斯托雷加』的新产品还没有出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "《利贝尔通讯》最新号的话，\x01",
            "我想今天中午才可以到货哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_61(0x101)

    ChrTalk(
        0x101,
        (
            "#505F中午啊……\x01",
            "那时我们正在进行研修呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xB, 500)

    ChrTalk(
        0x102,
        "#010F那研修结束后我们再过来买吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "那好，我给你们留着哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F29")

    label("loc_6B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E2D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE2")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_6BCB")
    OP_A9(0x8)
    Jump("loc_6BD9")

    label("loc_6BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_6BD7")
    OP_A9(0x7)
    Jump("loc_6BD9")

    label("loc_6BD7")

    OP_A9(0x2)

    label("loc_6BD9")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_6BE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BF3")
    TalkEnd(0xB)
    Return()

    label("loc_6BF3")

    OP_A2(0x209)

    ChrTalk(
        0xB,
        (
            "这样啊……\x01",
            "你们也要成为游击士了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "真令人羡慕啊，\x01",
            "我小时候也好想成为一名游击士呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_61(0x102)

    ChrTalk(
        0x102,
        (
            "#011F可以说利贝尔的男孩子\x01",
            "都拥有这一美好的憧憬呢。\x02\x03",
            "……不过这里有一位女孩也是这样。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#009F真是的～这算什么话啊。\x02\x03",
            "雪拉姐不也是\x01",
            "一名女游击士吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#010F我没有说当女游击士有什么不好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "好啦，你们两个可要好好加油哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "待会儿新的《利贝尔通讯》到货的时候\x01",
            "你们可要记得来买哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F29")

    label("loc_6E2D")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EA2")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_6E8B")
    OP_A9(0x8)
    Jump("loc_6E99")

    label("loc_6E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_6E97")
    OP_A9(0x7)
    Jump("loc_6E99")

    label("loc_6E97")

    OP_A9(0x2)

    label("loc_6E99")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_6EA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EB3")
    TalkEnd(0xB)
    Return()

    label("loc_6EB3")


    ChrTalk(
        0xB,
        "好啦，你们两个可要好好加油哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "待会儿新的《利贝尔通讯》到货的时候\x01",
            "你们可要记得来买哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F29")

    Jump("loc_7F83")

    label("loc_6F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_781E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_776C")
    EventBegin(0x0)
    OP_A2(0x20A)
    Fade(1000)
    OP_6D(3870, 0, 1030, 0)
    SetChrPos(0x101, 3420, 0, 50, 0)
    SetChrPos(0x102, 4360, 0, 40, 0)
    OP_8C(0xB, 180, 0)
    OP_0D()

    ChrTalk(
        0xB,
        "哟，这不是艾丝蒂尔和约修亚嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "欢迎。\x01",
            "是来买新鞋子吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊～进了新货吗？\x02\x03",
            "#001F难道是『斯托雷加』的新产品？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F一转眼就把来这里的目的忘掉了。\x02\x03",
            "父亲的吩咐已经忘了吗？ \x01",
            "我们是来买《利贝尔通讯》啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F啊，对对对☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "呵呵，艾丝蒂尔\x01",
            "还是那么热衷于收集运动鞋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不过真是很遗憾啊，\x01",
            "『斯托雷加』的新产品还没有出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "《利贝尔通讯》已经到了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F那么，我们就要一本吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "多谢，盛惠１００米拉。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_727F")
    SubMira(100)
    Jump("loc_7347")

    label("loc_727F")


    ChrTalk(
        0x101,
        (
            "#004F糟糕！\x01",
            "钱不够了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F真是的，刚才又乱花钱了。\x01",
            "你又想被父亲说一顿吗……\x02\x03",
            "#018F真拿你没办法。\x01",
            "算了，我先垫付着这点钱吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F哎呀，真没面子啊……\x02",
    )

    CloseMessageWindow()

    label("loc_7347")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "购入\x07\x02",
            "利贝尔通讯 第１号\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x207)
    OP_3E(0x347, 1)

    ChrTalk(
        0x101,
        (
            "#000F我家的老爸，\x01",
            "很喜欢看这本杂志……\x02\x03",
            "#000F对了，这本杂志卖得很好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "对啊，还经常报道独家新闻呢。\x01",
            "这杂志社有很精干的记者和摄影师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "杂志最近还在连载\x01",
            "女王诞辰庆典等相关的报道呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20B)

    ChrTalk(
        0xB,
        (
            "对了，\x01",
            "你们顺利成为游击士了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "最后的研修怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿，当然了⊙\x02\x03",
            "#004F对了，里农叔叔。\x01",
            "你是怎么知道的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "哈哈，你们现在已经成为\x01",
            "洛连特的风云人物了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "我从顾客那里听到了许多关于你们的事情哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F小城镇就是小城镇……\x01",
            "消息传的比广播还快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F这也是没办法的事啊……\x02",
    )

    CloseMessageWindow()
    Call(0, 31)
    EventEnd(0x0)
    Jump("loc_781B")

    label("loc_776C")

    SetChrName("里农")

    ChrTalk(
        0xB,
        "恭喜你们游击士考试合格。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "为了这值得庆祝的一刻，\x01",
            "买点东西作为纪念如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "我会给你们打折的哦。\x02",
    )

    CloseMessageWindow()

    label("loc_781B")

    Jump("loc_7F83")

    label("loc_781E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D05")
    EventBegin(0x0)
    OP_A2(0x20A)
    Fade(1000)
    OP_6D(3870, 0, 1030, 0)
    SetChrPos(0x101, 3420, 0, 50, 0)
    SetChrPos(0x102, 4360, 0, 40, 0)
    OP_8C(0xB, 180, 0)
    OP_0D()
    SetChrName("里农")

    ChrTalk(
        0xB,
        "哟，这不是艾丝蒂尔和约修亚嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "欢迎。\x01",
            "顺利成为游击士了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_61(0x101)

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿，当然了⊙\x02\x03",
            "#502F现在的我可是正牌游击士哦。\x01",
            "里农叔叔，从今天起叫我\x01",
            "『超级游击士·艾丝蒂尔』就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，里农先生。\x01",
            "《利贝尔通讯》到货了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "嗯，刚过中午就到了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#009F喂，没看到我正在高兴吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(
        0x101,
        "#007F……算了，就买一本吧。\x02",
    )

    CloseMessageWindow()
    SetChrName("里农")

    ChrTalk(
        0xB,
        "多谢，盛惠１００米拉。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7A75")
    SubMira(100)
    Jump("loc_7B3D")

    label("loc_7A75")


    ChrTalk(
        0x101,
        (
            "#004F糟糕！\x01",
            "钱不够了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F真是的，刚才又乱花钱了。\x01",
            "你又想被父亲说一顿吗……\x02\x03",
            "#018F真拿你没办法。\x01",
            "算了，我先垫付着这点钱吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F哎呀，真没面子啊……\x02",
    )

    CloseMessageWindow()

    label("loc_7B3D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "购入\x07\x02",
            "利贝尔通讯 第１号\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x207)
    OP_3E(0x347, 1)

    ChrTalk(
        0x101,
        (
            "#000F我家的老爸，\x01",
            "很喜欢看这本杂志……\x02\x03",
            "#000F对了，这本杂志卖得很好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "对啊，还经常报道独家新闻呢。\x01",
            "这杂志社有很精干的记者和摄影师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "杂志最近还在连载\x01",
            "女王诞辰庆典等相关的报道呢。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    EventEnd(0x0)
    Jump("loc_7F83")

    label("loc_7D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7ED4")
    OP_A2(0x20B)

    ChrTalk(
        0x101,
        (
            "#505F对了，里农老板。\x02\x03",
            "#505F你怎么知道我们的研修\x01",
            "是今天结业的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "哈哈，你们现在已经成为\x01",
            "洛连特的风云人物了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "我从顾客那里听到了许多关于你们的事情哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F小城镇就是小城镇……\x01",
            "消息传的比广播还快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F这也是没办法的事啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F83")

    label("loc_7ED4")

    SetChrName("里农")

    ChrTalk(
        0xB,
        "恭喜你们游击士考试合格。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "为了这值得庆祝的一刻，\x01",
            "买点东西作为纪念如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "我会给你们打折的哦。\x02",
    )

    CloseMessageWindow()

    label("loc_7F83")

    TalkEnd(0xB)
    Return()

    # Function_9_5A22 end

    def Function_10_7F87(): pass

    label("Function_10_7F87")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_80DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8055")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "拿着这么多的行李，\x01",
            "难道说你们要去旅行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "旅行时要是遇到适合做我家媳妇的人选，\x01",
            "记得回来和我说说哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我会立刻飞奔而去的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_80DB")

    label("loc_8055")


    ChrTalk(
        0xFE,
        (
            "拿着这么多的行李，\x01",
            "难道说你们要去旅行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "旅行时要是遇到适合做我家媳妇的人选，\x01",
            "记得回来和我说说哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80DB")

    Jump("loc_8C96")

    label("loc_80DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_8345")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8316")
    OP_A2(0x7)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(
        0xFE,
        (
            "……哎呀，你的头发是银色的呢，\x01",
            "难道你是外国人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F您说我吗？\x01",
            "嗯，也可以这样说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，年龄倒是正合适，\x01",
            "不过作为新娘好像太惹眼了些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F啊？新娘？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F（雪拉姐作新娘啊……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F（首先对方酒量不过关\x01",
            "　就没办法当她老公啊。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F（哇，这可不是闹着玩的……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F喂，你们两个，\x01",
            "在那儿嘀嘀咕咕说些什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8342")

    label("loc_8316")


    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "找媳妇可真不容易啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8342")

    Jump("loc_8C96")

    label("loc_8345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_8689")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_862F")
    OP_A2(0x7)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "你是卡西乌斯家的那个……\x01",
            "叫艾丝蒂尔的孩子是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，看起来\x01",
            "又健康又开朗呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么样，\x01",
            "愿意嫁到我们家来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊？\x02\x03",
            "#501F我、我吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然太年轻了点，不过反正最近\x01",
            "大家都不大在意年龄差距的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F等、等一下。\x01",
            "我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔，果然不行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家的儿子倒\x01",
            "的确是没有你身边\x01",
            "那位黑发小哥长得帅……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "你可要让\x01",
            "艾丝蒂尔幸福哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F哦、哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F（好像被老婆婆误会了呢……）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（哈哈……\x01",
            "　就先顺着她说吧，\x01",
            "　否则恐怕脱不了身了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8686")

    label("loc_862F")


    ChrTalk(
        0xFE,
        (
            "最近女孩子\x01",
            "也都出去工作了，\x01",
            "要找媳妇还真不是那么容易呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8686")

    Jump("loc_8C96")

    label("loc_8689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_8722")

    ChrTalk(
        0xFE,
        (
            "我决定要悄悄地替儿子\x01",
            "物色媳妇的人选。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我去了城里所有年龄合适\x01",
            "又贤淑端庄的姑娘家帮他说媒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C96")

    label("loc_8722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_88D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8830")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "儿子好像满脑子\x01",
            "都是店里的事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但人要成家立业、\x01",
            "生儿育女后才算是真正的成熟啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我这当老妈的\x01",
            "是不是该推他一把呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88CF")

    label("loc_8830")


    ChrTalk(
        0xFE,
        (
            "人要成家立业、\x01",
            "生儿育女后才算是真正的成熟啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我这当老妈的\x01",
            "是不是该推他一把呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88CF")

    Jump("loc_8C96")

    label("loc_88D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_8954")

    ChrTalk(
        0xFE,
        (
            "里农很勤快，\x01",
            "是个好孩子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但作父母的还是\x01",
            "希望他快点讨个老婆，\x01",
            "好让我们放心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C96")

    label("loc_8954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_8A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89FE")
    OP_A2(0x7)

    ChrTalk(
        0xC,
        (
            "已经到傍晚时分了啊，\x01",
            "我也该准备去吃饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "……里农那孩子\x01",
            "能够早点讨个\x01",
            "会做饭的老婆就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A46")

    label("loc_89FE")


    ChrTalk(
        0xC,
        (
            "里农那孩子\x01",
            "能够早点讨个\x01",
            "会做饭的老婆就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A46")

    Jump("loc_8C96")

    label("loc_8A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_8BE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B7B")
    OP_A2(0x7)

    ChrTalk(
        0xC,
        (
            "里农开的店已经走上正轨了，\x01",
            "这可比什么都好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "看着各种新商品\x01",
            "从飞艇上运送下来，\x01",
            "人们购物也增添几分乐趣呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "自从导力器发明以来，\x01",
            "人们的生活就变得方便了许多啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BE3")

    label("loc_8B7B")


    ChrTalk(
        0xC,
        (
            "自从导力器发明以来，\x01",
            "人们的生活就变得方便了许多啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BE3")

    Jump("loc_8C96")

    label("loc_8BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C5B")
    OP_A2(0x7)

    ChrTalk(
        0xC,
        (
            "呼～～果然还是\x01",
            "清晨的空气最新鲜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "接下来要给可爱的\x01",
            "花朵们浇水了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C96")

    label("loc_8C5B")


    ChrTalk(
        0xC,
        (
            "接下来要给可爱的\x01",
            "花朵们浇水了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C96")

    TalkEnd(0xC)
    Return()

    # Function_10_7F87 end

    def Function_11_8C9A(): pass

    label("Function_11_8C9A")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D0C")
    OP_A2(0x8)

    ChrTalk(
        0xD,
        (
            "鲁克和帕特他们\x01",
            "不会有事吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我都已经\x01",
            "那样拼命阻止了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "呜呜。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D49")

    label("loc_8D0C")


    ChrTalk(
        0xD,
        (
            "艾丝蒂尔姐姐，\x01",
            "约修亚哥哥，\x01",
            "那两个人就拜托你们了，呜呜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D49")

    TalkEnd(0xD)
    Return()

    # Function_11_8C9A end

    def Function_12_8D4D(): pass

    label("Function_12_8D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DF8")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_69(0x9, 0x320)

    def lambda_8D71():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8D71)

    def lambda_8D7F():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8D7F)

    ChrTalk(
        0x9,
        (
            "#024F怎么了，想出去吗？\x01",
            "研修还没结束呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x3E8, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_8DF8")

    Return()

    # Function_12_8D4D end

    def Function_13_8DF9(): pass

    label("Function_13_8DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EA4")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_69(0x9, 0x320)

    def lambda_8E1D():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8E1D)

    def lambda_8E2B():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8E2B)

    ChrTalk(
        0x9,
        (
            "#024F怎么了，想出去吗？\x01",
            "研修还没结束呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_8EA4")

    Return()

    # Function_13_8DF9 end

    def Function_14_8EA5(): pass

    label("Function_14_8EA5")

    EventBegin(0x0)
    OP_4A(0x8, 0)
    ClearChrFlags(0x9, 0x80)
    ClearMapFlags(0x1)
    SetChrPos(0x9, -764, 0, 114882, 90)
    SetChrPos(0x101, 811, 0, 115528, 270)
    SetChrPos(0x102, 811, 0, 114132, 270)
    OP_6D(342, 0, 115532, 0)
    OP_6B(3000, 0)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0x9,
        (
            "#020F最后的研修就是\x01",
            "完成工作之后的报告方法了。\x02\x03",
            "#020F不管是什么工作，\x01",
            "完成之后一定要到协会报告。\x02\x03",
            "#020F解决了什么样的事情、解决事情的经过，\x01",
            "这些都需要一一汇报，\x01",
            "因为工作报告也是游击士应履行的职责。\x02\x03",
            "#020F受理报告的地点是各个协会的接待处。\x01",
            "洛连特这里的负责人\x01",
            "就是你们两人都很熟悉的爱娜。\x02\x03",
            "#020F啊，还要记得的是\x01",
            "工作报酬也是在协会里获得的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#740F今后就请多多关照哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#020F好了，你们两人\x01",
            "就试试向爱娜报告一下工作吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※站在柜台附近时会出现『TALK』的标记，\x01",
            "　用右键点击会出现选择菜单。\x01",
            "　在前台报告工作的时候在菜单上选择『报告』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_4B(0x8, 0)
    EventEnd(0x0)
    Return()

    # Function_14_8EA5 end

    def Function_15_925E(): pass

    label("Function_15_925E")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    Sleep(500)
    OP_2A(0xA, 0xFFFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_927D")
    EventEnd(0x1)
    Return()

    label("loc_927D")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※已在公告板上确认的\x01",
            "　工作详情和工作中的要点\x01",
            "　都会自动记录在游击士手册上。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※手册在Camp内［Item］栏的［书籍］中。\x01",
            " 或者点击画面右下角显示的手册图标\x01",
            " 也可以查看到所有工作任务及其相关的内容。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0xE)
    Fade(1000)
    OP_6D(-91, 0, 115143, 0)
    OP_44(0x9, 0xFF)
    SetChrPos(0x9, -764, 0, 114882, 90)
    SetChrPos(0x101, 811, 0, 115528, 270)
    SetChrPos(0x102, 811, 0, 114132, 270)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#020F嗯，可以了。\x02\x03",
            "#020F你们两人都仔细确认过\x01",
            "公告板上的内容了吧。\x02\x03",
            "#020F对游击士来说，\x01",
            "时常留意公告板是基本中的基本。\x02\x03",
            "#020F经常确认是不是有紧急的工作，\x01",
            "对游击士来说，也是一个重要的职责哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呼……这么多的职责，\x01",
            "光是听就已经觉得快窒息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F的确有很多规则，\x01",
            "因为游击士要做的都是需要负责任的工作。\x02\x03",
            "#010F如果抱着敷衍了事的态度，\x01",
            "是无法胜任游击士这种职业的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F……嗯，也对。\x02\x03",
            "得更加努力去适应才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#020F呵呵，\x01",
            "是不是已经有所觉悟了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F是的。\x01",
            "完全没问题了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#020F那么……\x01",
            "趁热情还没有消退，\x01",
            "马上进行下一项研修吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F这次是什么内容呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#020F要去对面梅尔达斯先生的工房。\x01",
            "我希望你们学习一下\x01",
            "工房的主要用途和具体操作。\x02\x03",
            "#020F因为我们占用了\x01",
            "工房的营业时间去请教人家，\x01",
            "所以你们不要做出失礼的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F好～\x02",
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/T0120   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_15_925E end

    def Function_16_98ED(): pass

    label("Function_16_98ED")

    EventBegin(0x0)
    OP_6D(740, 0, 117300, 0)
    OP_6B(3000, 0)
    SetChrPos(0x101, 780, 0, 115570, 0)
    SetChrPos(0x103, -440, 0, 116340, 45)
    SetChrPos(0x102, 1860, 0, 116020, 0)
    OP_44(0x8, 0xFF)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#740F——事情我已经了解了。\x02\x03",
            "说实话，继卡西乌斯先生之后，\x01",
            "雪拉扎德也离开的话，\x01",
            "这里的人手会相当紧张……\x02\x03",
            "不过，毕竟事关卡西乌斯先生的安危。\x01",
            "请不要挂念太多，放心地出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F多谢你，爱娜。\x02\x03",
            "#021F呵呵，利吉那小子，\x01",
            "你就使劲地使唤他吧。\x02\x03",
            "以平常的工作量来算，\x01",
            "就算再加三倍我想也没问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F真、真是可怜呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#741F呵呵，万一不行的话，\x01",
            "还可以向王都支部请求支援，\x01",
            "所以你们不用担心。\x02\x03",
            "#740F对了，雪拉扎德。\x01",
            "能耽误你一些时间吗？\x02\x03",
            "关于你刚接手的那个工作\x01",
            "有点事情要说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#020F艾丝蒂尔、约修亚。\x01",
            "你们在二楼等我一会儿好吗？\x02\x03",
            "马上就会说完的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        "#010F#4P好的，我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F…………………………\x02\x03",
            "#501F那个，雪拉姐。\x02\x03",
            "如果要等的话，\x01",
            "我想去钟楼那里可以吗？\x02\x03",
            "有点……\x01",
            "有点话想和一个人说。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F#4P……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F是吗……\x01",
            "嗯，那好吧。\x02\x03",
            "#020F那么，\x01",
            "一会儿就在钟楼的前面会合吧。\x02\x03",
            "等办完事情，\x01",
            "我马上就过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F知道了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#501F约修亚，走吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#4P啊，好……\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    RemoveParty(0x2, 0xFF)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_98ED end

    def Function_17_9E26(): pass

    label("Function_17_9E26")

    EventBegin(0x0)
    OP_6D(590, 0, 117600, 0)
    OP_67(0, 8010, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 780, 0, 115570, 0)
    SetChrPos(0x103, -440, 0, 116340, 45)
    SetChrPos(0x102, 1860, 0, 116020, 0)
    OP_44(0x8, 0xFF)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#742F真是不得了呢。\x01",
            "没想到犯人竟然是空贼……\x02\x03",
            "#742F被他们逃掉也是没办法的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F不，这次是我的失误。\x01",
            "都是因为我一时大意才会这样的。\x02\x03",
            "果然，离老师的境界还远着呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F哎呀，不是雪拉姐的责任啦。\x02\x03",
            "#003F要怪就怪我一时冲动，\x01",
            "才会让他们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F#4P……我也疏忽大意了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1A, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_A0C4")

    ChrTalk(
        0x103,
        (
            "#020F不，你们已经做得很好了。\x01",
            "在市长家的现场调查十分完美。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1D1")

    label("loc_A0C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_A155")

    ChrTalk(
        0x103,
        (
            "#020F不，你们已经做得很好了。\x01",
            "在市长家的现场调查也算可以。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1D1")

    label("loc_A155")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1A, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_A1D1")

    ChrTalk(
        0x103,
        (
            "#020F不，你们已经做得很好了。\x01",
            "虽然在市长家的现场调查不怎么样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1D1")

    TurnDirection(0x103, 0x8, 400)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#027F爱娜……\x01",
            "他们可以获得推荐的资格吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#741F嗯，当然可以了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#004F推荐？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#4P这是什么意思呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F在这之前，\x01",
            "先把这次调查的报酬支付给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_28(0x1A, 0x4, 0x10)
    OP_AF(0x4, 0x1A)
    OP_28(0x1B, 0x4, 0x10)
    OP_28(0x1B, 0x4, 0x20)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#740F然后……\x01",
            "你们收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x330, 1)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
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
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x101,
        "#004F这、这个是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F现在你们是准游击士。\x01",
            "也就是说还是在见习阶段。\x02\x03",
            "要成为正游击士的话，\x01",
            "还必须取得王国所有地区支部的\x01",
            "推荐信才可以哦。\x02\x03",
            "而这就是洛连特支部的推荐信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F可、可以吗？\x01",
            "给我们这个……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#4P而且我听说，\x01",
            "要成为正游击士，\x01",
            "必须要做出很优秀的成绩才……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#741F你们完成的三个任务和这次的活跃表现，\x01",
            "作为成绩来说已经完全足够了。\x02\x03",
            "#740F……不过，\x01",
            "这也只是洛连特地区的成绩而已。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(
        0x103,
        (
            "#027F你们还要在其他地区作出像样的成绩，\x01",
            "这样才能取得所有支部的推荐资格。\x02\x03",
            "#027F柏斯、卢安、蔡斯，\x01",
            "还有王都格兰赛尔……\x02\x03",
            "#021F要走的路还很长呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#001F可是可是，我真的很开心！\x01",
            "努力工作得到回报了呢！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F约修亚，这样的话，\x01",
            "我们不去其他地方不行呢！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F#4P哈哈，就知道你会这么说。\x02\x03",
            "#010F虽然我也赞成这样……\x01",
            "不过我们也不能擅自决定啊。\x02\x03",
            "#010F等父亲回来之后再商量一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯！\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x0, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_A8FB():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8FB)

    def lambda_A909():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A909)

    def lambda_A917():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A917)
    Sleep(1000)
    OP_8C(0x8, 315, 400)

    ChrTalk(
        0x8,
        "#743F哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，那个是通信器吗？\x02",
    )

    CloseMessageWindow()

    def lambda_A968():
        OP_6D(-660, 0, 118480, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A968)
    OP_8E(0x8, 0xFFFFFE52, 0x0, 0x1D0CE, 0x7D0, 0x0)
    OP_8C(0x8, 0, 400)
    Sleep(500)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x0, 0xFF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#740F#5P你好，这里是游击士协会，\x01",
            "利贝尔王国·洛连特支部。\x02\x03",
            "#743F啊，很久没有联系了呢……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#742F#5P…………………………\x02\x03",
            "#742F……………是真的吗？\x02\x03",
            "#744F那、那真是……\x01",
            "不得了的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#505F发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#4P嗯……看来好像是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#743F#5P嗯，没错。\x01",
            "确实是前几天出发的……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_21()
    OP_63(0x8)

    ChrTalk(
        0x8,
        "#742F#3S#5P什么！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)
    OP_1D(0x51)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#745F#5P不、不好意思。\x01",
            "事出突然，实在不敢相信……\x02\x03",
            "好，我明白了。\x01",
            "家属方面我会通知的。\x02\x03",
            "#742F……没关系。\x01",
            "他们本身也是游击士。\x02\x03",
            "好……\x01",
            "如果有什么消息请赶快联络。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#505F爱娜姐姐，发生什么事情了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F真是少见啊。\x01",
            "让你吃惊到那种程度。\x02\x03",
            "对了，是哪里来的联络？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8)

    def lambda_AD7B():
        OP_6D(590, 0, 117600, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD7B)
    OP_8C(0x8, 90, 400)
    OP_8E(0x8, 0x2EE, 0x0, 0x1CF48, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x8,
        (
            "#742F是柏斯支部的。\x01",
            "……发生了很严重的事情啊。\x02\x03",
            "定期船『林德号』\x01",
            "在柏斯地区失去了音讯。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#4P到底是怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#744F详细情况还不清楚……\x02\x03",
            "据说王国军已经出动了，\x01",
            "在附近进行着大规模的搜索行动。\x02\x03",
            "也因为这件事，\x01",
            "其他航线的定期船也要暂时停航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F原来如此……\x01",
            "难怪飞艇坪会聚集那么多人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#745F而、而且……\x02\x03",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F爱娜姐姐？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#742F艾丝蒂尔、约修亚。\x01",
            "你们一定要保持镇定。\x02\x03",
            "#742F失踪的定期船似乎正是……\x01",
            "卡西乌斯先生所乘坐的那一艘。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)

    ChrTalk(
        0x101,
        "#580F#3S…………啊。\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#016F#4P怎么会……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F开、开玩笑吧！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#742F乘客名单上似乎有他的名字。\x02\x03",
            "利贝尔游击士协会，\x01",
            "洛连特支部所属，正游击士……\x02\x03",
            "卡西乌斯·布莱特，４５岁……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x9C4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_AD(0x40041, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_83(0x11, 0x0)
    OP_A2(0x269)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-87490, 0, 61990, 0)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1E7")
    ShowSaveMenu()

    label("loc_B1E7")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    NewScene("ED6_DT01/T0301   ._SN", 3, 0, 0)
    IdleLoop()
    Return()

    # Function_17_9E26 end

    def Function_18_B236(): pass

    label("Function_18_B236")

    EventBegin(0x0)
    OP_0D()
    OP_43(0x101, 0x0, 0x0, 0x13)
    OP_43(0x102, 0x0, 0x0, 0x14)
    OP_43(0x101, 0x1, 0x0, 0x15)
    OP_4A(0x8, 0)
    OP_A2(0x3)
    OP_A5(0x3)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#740F哎呀，早啊。\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F爱娜姐姐，早上好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x3)
    OP_A5(0x0)
    OP_A5(0x1)
    OP_A5(0x3)

    ChrTalk(
        0x101,
        "#000F#4P雪拉姐已经来了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F嗯，在二楼等着呢。\x02\x03",
            "今天的研修结束之后，\x01",
            "就可以正式成为游击士的一员了。\x02\x03",
            "你们俩要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#4P嗯，谢谢！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们会努力的。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_4B(0x8, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_A2(0x204)
    EventEnd(0x0)
    Return()

    # Function_18_B236 end

    def Function_19_B415(): pass

    label("Function_19_B415")

    OP_A6(0x0)
    OP_8E(0xFE, 0x898, 0x0, 0x1B968, 0xBB8, 0x0)
    OP_8E(0xFE, 0x5DC, 0x0, 0x1C520, 0xBB8, 0x0)
    OP_A3(0x0)
    Return()

    # Function_19_B415 end

    def Function_20_B444(): pass

    label("Function_20_B444")

    OP_A6(0x1)
    Sleep(200)
    OP_8E(0xFE, 0x7D0, 0x0, 0x1B580, 0xBB8, 0x0)
    OP_8E(0xFE, 0x2BC, 0x0, 0x1C200, 0xBB8, 0x0)
    OP_A3(0x1)
    Return()

    # Function_20_B444 end

    def Function_21_B478(): pass

    label("Function_21_B478")

    OP_A6(0x3)
    OP_6D(1500, 0, 116000, 1200)
    OP_A3(0x3)
    OP_A6(0x3)
    OP_6D(740, 0, 117400, 1500)
    OP_A3(0x3)
    Return()

    # Function_21_B478 end

    def Function_22_B4A7(): pass

    label("Function_22_B4A7")

    FadeToBright(1000, 0)
    OP_6D(-90, 0, 72340, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x12, -400, 700, 73300, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x13, -100, 700, 73300, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, 200, 700, 73300, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x15, 500, 700, 73300, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x16, 800, 700, 73300, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x9, 200, 200, 74100, 180)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_43(0x101, 0x0, 0x0, 0x18)
    OP_43(0x102, 0x0, 0x0, 0x1C)
    OP_43(0x9, 0x0, 0x0, 0x1D)
    SetChrSubChip(0x12, 8)
    SetChrSubChip(0x13, 9)
    SetChrSubChip(0x14, 10)
    SetChrSubChip(0x15, 11)
    SetChrSubChip(0x16, 7)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 1)
    SetChrFlags(0x9, 0x2)
    OP_0D()
    Sleep(1000)
    SetChrSubChip(0x9, 0)
    Sleep(200)
    Fade(1000)
    SetChrFlags(0x16, 0x80)
    SetChrSubChip(0x9, 1)
    SetChrSubChip(0x16, 12)
    Sleep(1000)
    OP_99(0x9, 0x1, 0x3, 0x3E8)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#026F#2P………………\x02\x03",
            "『星星』和『倒吊男』……\x02\x03",
            "『隐者』和『魔术师』……\x02\x03",
            "最后是逆位置的『命运之轮』……\x02\x03",
            "#025F这可难办了。\x01",
            "该怎么解读好呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -4850, -2000, 66000, 0)
    ClearChrFlags(0x101, 0x8)

    ChrTalk(
        0x101,
        "#2P雪拉姐，早啊～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_99(0x9, 0x3, 0x1, 0x4B0)
    Sleep(100)
    Fade(1000)
    SetChrSubChip(0x16, 12)
    ClearChrFlags(0x16, 0x80)
    Sleep(400)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 8)
    SetChrSubChip(0x9, 0)
    Sleep(1000)

    def lambda_B76B():
        OP_6D(-2250, 0, 73500, 2000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B76B)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A5(0x0)
    OP_A5(0x1)
    WaitChrThread(0x9, 0x1)

    ChrTalk(
        0x9,
        (
            "#023F#2P噢，艾丝蒂尔、约修亚。\x02\x03",
            "#023F真是少见啊。\x01",
            "你们这么早就来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嘿嘿，因为是最后的研修嘛。\x02\x03",
            "而且通过考试之后\x01",
            "我们就可以成为游击士啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#025F#2P唉……\x01",
            "难得你这么有干劲。\x02\x03",
            "#020F好吧！为了回应你的气势，\x01",
            "今天的训练也会格外严格。\x02\x03",
            "你们做好心理准备吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F啊～怎么会呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#022F#2P多·说·无·用。\x02\x03",
            "每次教你的东西\x01",
            "总是左耳进右耳出的……\x02\x03",
            "这样做也是为了\x01",
            "让你这个漏勺一样的脑子牢牢记住啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        (
            "#504F哎～约修亚！\x01",
            "雪拉姐欺负我啦～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没问题的，雪拉姐姐。\x02\x03",
            "艾丝蒂尔虽然讨厌学习，\x01",
            "平时也不怎么预习和复习……\x02\x03",
            "而且做事不假思索，\x01",
            "经常做老好人又喜欢多管闲事……\x02\x03",
            "不过敏锐的第六感却是首屈一指的，\x01",
            "导力器的运用也在实战中得到过锻炼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#025F#2P呵呵，既然如此，\x01",
            "也只好期待她的表现了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#509F我说约修亚……\x02\x03",
            "怎么听起来你说的\x01",
            "全是些胳膊肘向外拐的话啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F你想太多了。\x01",
            "我只是坦白说出你的优点而已嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F真是的……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        (
            "#501F啊，对了雪拉姐。\x01",
            "你用塔罗牌在占卜什么啊？\x02\x03",
            "看你一脸心事重重的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#522F#2P啊，这个啊。\x02\x03",
            "我本来想试试占卜一下\x01",
            "最近身边可能会发生的事情。\x02\x03",
            "可似乎状态不太好，\x01",
            "怎么也解读不出来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F解读不出来？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F咦……\x01",
            "会有这样的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#020F#2P隐藏于形态的涵义越深，\x01",
            "相应地也就越难让人解读呢。\x02\x03",
            "#020F算了，先不管这个了。\x01",
            "开始最后的研修吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(500, 0, -1)
    Sleep(1000)
    SetChrPos(0x101, 500, 0, 72250, 0)
    SetChrPos(0x102, -500, 0, 72250, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrSubChip(0x9, 0)
    OP_6D(-440, 0, 73390, 0)
    FadeToBright(500, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#020F#2P先把至今为止所学习的内容\x01",
            "从头到尾复习一遍吧。\x02\x03",
            "#020F因为这些都是作为游击士\x01",
            "所必须具备的最低限度的常识。\x02\x03",
            "#020F特别是艾丝蒂尔，\x01",
            "好好听着哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F是～\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -56)
    OP_0D()
    Sleep(500)

    label("loc_C182")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD02")
    SetChrName("雪拉扎德")

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F想知道关于哪方面的内容？\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_C299")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_C240")

    Menu(
        0,
        200,
        100,
        0,
        (
            "【导力器是什么？】\x01",          # 0
            "【游击士协会是什么？】\x01",      # 1
            "【关于利贝尔王国】\x01",          # 2
            "【放弃】\x01",                    # 3
        )
    )

    Jump("loc_C296")

    label("loc_C240")


    Menu(
        0,
        200,
        100,
        0,
        (
            "【导力器是什么？】\x01",      # 0
            "【游击士是什么？】\x01",      # 1
            "【关于利贝尔王国】\x01",      # 2
            "【放弃】\x01",                # 3
        )
    )


    label("loc_C296")

    Jump("loc_C2E1")

    label("loc_C299")


    Menu(
        0,
        200,
        100,
        0,
        (
            "【导力器是什么？】\x01",      # 0
            "【游击士是什么？】\x01",      # 1
            "【关于利贝尔王国】\x01",      # 2
        )
    )


    label("loc_C2E1")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C30B"),
        (1, "loc_C30E"),
        (2, "loc_C322"),
        (3, "loc_C336"),
        (SWITCH_DEFAULT, "loc_C343"),
    )


    label("loc_C30B")

    Jump("loc_C343")

    label("loc_C30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_C31F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C31F")

    Jump("loc_C343")

    label("loc_C322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_C333")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C333")

    Jump("loc_C343")

    label("loc_C336")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C343")

    label("loc_C343")

    OP_A2(0xA)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C363"),
        (1, "loc_C5B3"),
        (2, "loc_C78A"),
        (4, "loc_CAB6"),
        (3, "loc_CCED"),
        (SWITCH_DEFAULT, "loc_CCFD"),
    )


    label("loc_C363")

    OP_AD(0x40013, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("雪拉扎德")

    AnonymousTalk(
        (
            "#020F使用一种被称为『导力』的能源来驱动的\x01",
            "机械装置单元就叫做导力器。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#020F导力器内部装有用\x01",
            "七耀石加工而成的结晶回路，\x01",
            "根据其不同结构能够引起各种各样的现象。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#020F从发明至今\x01",
            "虽只经历了５０年左右的时间……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#020F但现今无论是照明、取暖等日用品，\x01",
            "还是兵器、魔法、飞艇等高科技工具，\x01",
            "各个领域内，导力器的力量都已得到广泛应用。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#020F顺带一提，\x01",
            "实用导力器的技术革新一般通称为『导力革命』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_CCFD")

    label("loc_C5B3")

    OP_A2(0xB)
    OP_AD(0x40015, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("雪拉扎德")

    AnonymousTalk(
        (
            "#020F游击士是一种\x01",
            "为保护地区和平及百姓安全，\x01",
            "而进行调查与战斗活动的专家。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#020F不只是消灭魔兽、制止犯罪，\x01",
            "还有像护送货物、寻找失物等\x01",
            "对地区有贡献的工作都是游击士所理应承担的。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#020F管理各地游击士的机构，\x01",
            "就是分布在大陆各地的游击士协会。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_CCFD")

    label("loc_C78A")

    OP_AD(0x40014, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("雪拉扎德")

    AnonymousTalk(
        (
            "#020F我们所居住的这个利贝尔王国，\x01",
            "位于塞姆里亚大陆西部，\x01",
            "是一个拥有悠久历史传统和丰富自然资源的国家。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#020F身为整个大陆内为数不多的七耀石产地之一，\x01",
            "利贝尔利用这个优势进行各种高端的导力器开发，\x01",
            "因此王国也以拥有最尖端的导力技术而闻名整个大陆。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#020F对于利贝尔王国来说，\x01",
            "导力技术是其能与周边的大国进行抗衡、\x01",
            "保持国家独立性的重要支柱。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#020F１０年前遭到埃雷波尼亚帝国侵略之时，\x01",
            "在最后关头拯救了王国的，\x01",
            "正是使用以导力引擎驱动的飞艇所进行的反攻作战。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#020F嗯，虽说现在王国和帝国的关系仍很微妙，\x01",
            "不过依靠艾莉茜雅女王陛下英明的政治手腕，\x01",
            "现在的利贝尔，大致上可说是和平安定的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_CCFD")

    label("loc_CAB6")

    OP_AD(0x40015, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("雪拉扎德")

    AnonymousTalk(
        (
            "#020F游击士协会，\x01",
            "是５０年前设立的一个世界范围的游击士联合组织。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#020F在利贝尔王国以外的\x01",
            "国家和地区都设有其支部，\x01",
            "协会对各地的和平作出了很大贡献。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#020F而且因为协会具有国际性和中立性，\x01",
            "所以也曾经承担过仲裁国家间纠纷的工作。\x01",
            "在终止１０年前的战争一事中也发挥了重要作用。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#025F不过，经常被委托做各种各样的工作，\x01",
            "协会也一直为人手不足的问题所困扰。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_CCFD")

    label("loc_CCED")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_CCFD")

    label("loc_CCFD")

    OP_56(0x0)
    Jump("loc_C182")

    label("loc_CD02")

    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#020F#2P那么……\x01",
            "复习就到此为止吧。\x02\x03",
            "#020F今天要做的事情堆积如山，\x01",
            "我们还是赶快进行实地研修吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F我说雪拉姐……\x02\x03",
            "那个实地研修，\x01",
            "和我们之前做的研修有什么不一样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#020F#2P所谓实地，\x01",
            "就是要亲自去现场体验啊。\x02\x03",
            "#020F从现在开始，\x01",
            "我要你们两个亲身去体会一下\x01",
            "身为游击士必须要做的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F也就是说……\x02\x03",
            "不是坐在桌子前面\x01",
            "傻乎乎地埋头学习啦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#027F#2P嗯，当然不是啦。\x02\x03",
            "#027F其实我希望你们到各种地方去，\x01",
            "让自己的身体真正活动起来。\x02\x03",
            "#027F尽情挥洒汗水，\x01",
            "好好体会当中的乐趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿嘿，得救了～\x02\x03",
            "#001F如果是运动之类的话，\x01",
            "那可比之前的研修要轻松多了。\x02\x03",
            "#001F真是……之前还害我担心得要死。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#3P怎么好像突然精神起来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#026F#2P看你这么开心，\x01",
            "我希望你能笑到最后……\x02\x03",
            "#020F……那么，\x01",
            "我们去第一个实地研修地点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F好！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-91, 0, 115143, 0)
    OP_4A(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 1)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x10)
    SetChrPos(0x9, -764, 0, 114882, 90)
    SetChrPos(0x101, 811, 0, 115528, 270)
    SetChrPos(0x102, 811, 0, 114132, 270)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#020F第一项研修，\x01",
            "是确认工作内容。\x02\x03",
            "#020F……在此之前，\x01",
            "我有样东西要交给你们。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "#020F爱娜。\x01",
            "准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#740F嗯，准备好了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)

    ChrTalk(
        0x9,
        (
            "#020F可以了，\x01",
            "你们两个到爱娜那里去拿吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_4B(0x8, 0)
    EventEnd(0x0)

    def lambda_D3E3():

        label("loc_D3E3")

        TurnDirection(0x9, 0x1, 0)
        OP_48()
        Jump("loc_D3E3")

    QueueWorkItem2(0x9, 1, lambda_D3E3)
    Return()

    # Function_22_B4A7 end

    def Function_23_D3EF(): pass

    label("Function_23_D3EF")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x101, 500, 0, 72250, 0)
    SetChrPos(0x102, -500, 0, 72250, 0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 8)
    SetChrPos(0x9, 200, 200, 74100, 180)
    OP_6D(-440, 0, 73390, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#020F#2P你们两人都辛苦了。\x01",
            "这样所有的研修课程都结束了。\x02\x03",
            "#020F之后要做的就是\x01",
            "亲自在实践中总结经验。\x02\x03",
            "#026F那么……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "雪拉扎德取出两个小箱子。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#004F#6P啊，那个箱子是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#027F#2P对啊，\x01",
            "就是刚才考试收回的小箱子。\x02\x03",
            "#027F看来你们也很在意\x01",
            "里面究竟装了些什么吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#6P难道说……\x01",
            "现在可以让我们打开了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#020F#2P嗯，可以了。\x02\x03",
            "#020F你们两人\x01",
            "都打开看看里面的东西吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#6P嘿嘿，太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#3P那我就……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人把小箱子打开了。\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x40022, 0xBE, 0x64, 0x1F4)
    Sleep(1500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "准游击士的徽章\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_3E(0x35C, 1)

    ChrTalk(
        0x101,
        "#004F#6P这个徽章是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#3P这么说，现在我们就是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#026F#2P……咳咳。\x02\x03",
            "#022F艾丝蒂尔·布莱特。\x01",
            "约修亚·布莱特。\x02\x03",
            "#022F以上两人于本日１５：００\x01",
            "正式被任命为『准游击士』。\x02\x03",
            "#022F今后，作为游击士协会的一员，\x01",
            "你们要谨记为守护人民的和平生活\x01",
            "以及维护正义而贡献力量。\x02\x03",
            "#021F……恭喜你们两人，\x01",
            "从现在开始我们就是同事了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#001F#4P成功啦，约修亚！\x02\x03",
            "#001F这么一来我们也\x01",
            "堂堂正正地成为协会的一员啦☆\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 300)

    ChrTalk(
        0x102,
        (
            "#015F#3P是吗，我也成为游击士了……\x02\x03",
            "#015F……………………\x02\x03",
            "#011F哈哈，感觉有点不可思议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4P真是的，约修亚～\x02\x03",
            "#006F你别这么心平气和嘛，\x01",
            "应该表现得更加兴高采烈才对啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#001F#2P#5S呀嗬～太棒啦～⊙\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#018F#3P兴高采烈过头了吧，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#021F#2P呵呵，那么……\x01",
            "我差不多该告辞了。\x02\x03",
            "#021F外面还有一大堆的工作\x01",
            "在等着我去处理呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 0)
    TurnDirection(0x102, 0x9, 0)

    ChrTalk(
        0x101,
        (
            "#501F#6P是吗，工作那么忙，\x01",
            "每天还要抽空陪我们啊。\x02\x03",
            "#501F雪拉姐，真是太感谢你啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#3P真是给你添麻烦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#027F#2P呵呵，别这么说。\x01",
            "培养新人也是游击士的义务啊。\x02\x03",
            "#027F我以前研修的时候，\x01",
            "也曾受到卡西乌斯老师很多照顾呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#6P啊，因为这样\x01",
            "你就称呼老爸为『老师』是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#020F#2P不仅仅是因为这个理由。\x02\x03",
            "#020F我希望你们也能早日独当一面，\x01",
            "这样就拥有指导后辈的能力。\x02\x03",
            "#020F然后，\x01",
            "逐渐成为像老师那样伟大的游击士。\x02\x03",
            "#021F好了，以后再聊吧，再见哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrPos(0x9, 200, 0, 74100, 180)
    ClearChrFlags(0x9, 0x10)
    Sleep(500)

    def lambda_E051():

        label("loc_E051")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_E051")

    QueueWorkItem2(0x101, 3, lambda_E051)

    def lambda_E062():

        label("loc_E062")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_E062")

    QueueWorkItem2(0x102, 3, lambda_E062)
    OP_43(0x9, 0x0, 0x0, 0x1D)
    Sleep(200)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x2)
    Sleep(500)
    ClearChrFlags(0x9, 0x4)
    OP_A5(0x2)
    OP_A3(0x1)
    OP_A3(0x0)
    Sleep(200)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x3)

    ChrTalk(
        0x101,
        "#505F#4P嗯……真是想不明白。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#014F#3P什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#505F#4P说起『银闪雪拉扎德』，\x01",
            "大家都知道她是游击士当中\x01",
            "数一数二的厉害人物。\x02\x03",
            "#505F可是为什么\x01",
            "她会给老爸那么高的评价呢？\x02\x03",
            "#007F要是让作为女儿的我来评价的话，\x01",
            "他只不过是个经常外出不归的不良中年罢了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#3P不良中年……\x02\x03",
            "#015F不过，站在艾丝蒂尔的角度，\x01",
            "做这种评价也不是没有道理的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4P啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3P……啊，没什么。\x02\x03",
            "#010F那么，今天早点回家吧。\x02\x03",
            "#010F我们还要把成为游击士的事告诉父亲呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#4P嗯，好啊！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_A2(0x205)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_23_D3EF end

    def Function_24_E399(): pass

    label("Function_24_E399")

    OP_A6(0x0)
    OP_8E(0xFE, 0xFFFFED0E, 0x0, 0x11558, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF6FA, 0x0, 0x118DC, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    OP_A3(0x0)
    OP_A6(0x0)

    label("loc_E3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E3E3")
    TurnDirection(0xFE, 0x9, 0)
    OP_48()
    Jump("loc_E3D1")

    label("loc_E3E3")

    Return()

    # Function_24_E399 end

    def Function_25_E3E4(): pass

    label("Function_25_E3E4")

    Sleep(600)
    OP_8E(0x101, 0x32A, 0x0, 0x1C4B2, 0x7D0, 0x0)
    TurnDirection(0x101, 0xF, 400)
    Return()

    # Function_25_E3E4 end

    def Function_26_E405(): pass

    label("Function_26_E405")

    OP_8E(0x102, 0x762, 0x0, 0x1C3CC, 0x7D0, 0x0)
    TurnDirection(0x102, 0xF, 400)
    Return()

    # Function_26_E405 end

    def Function_27_E421(): pass

    label("Function_27_E421")

    Sleep(300)
    OP_8E(0x9, 0xFFFFFFA6, 0x0, 0x1C246, 0x7D0, 0x0)
    TurnDirection(0x9, 0xF, 400)
    Return()

    # Function_27_E421 end

    def Function_28_E442(): pass

    label("Function_28_E442")

    OP_A6(0x1)
    SetChrPos(0xFE, -4850, -2000, 66000, 0)
    ClearChrFlags(0xFE, 0x8)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFED0E, 0x0, 0x11558, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF24A, 0x0, 0x11A08, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    OP_A3(0x1)
    OP_A6(0x1)

    label("loc_E495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E4A7")
    TurnDirection(0xFE, 0x9, 0)
    OP_48()
    Jump("loc_E495")

    label("loc_E4A7")

    Return()

    # Function_28_E442 end

    def Function_29_E4A8(): pass

    label("Function_29_E4A8")

    OP_A6(0x2)
    OP_8E(0xFE, 0xFFFFF45C, 0x0, 0x12174, 0xBB8, 0x0)
    ClearChrFlags(0x9, 0x4)
    OP_8E(0xFE, 0xFFFFEC46, 0x0, 0x11422, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFEC46, 0xFFFFF830, 0x1027A, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    Return()

    # Function_29_E4A8 end

    def Function_30_E4FB(): pass

    label("Function_30_E4FB")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_4A(0x8, 0)
    OP_6B(2800, 0)
    SetChrPos(0x101, 1500, 0, 116000, 0)
    SetChrPos(0x102, 700, 0, 115200, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)

    ChrTalk(
        0x8,
        "#740F呵呵，真是辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F老爸真是的……\x02\x03",
            "#007F刚到镇上就扔下一句\x01",
            "『报告的事就拜托了』，\x01",
            "然后就一溜烟地跑回家了……\x02\x03",
            "#007F真不知道该怎么形容他这种性格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F算了，也无所谓吧。\x01",
            "反正孩子们平安无事就行了。\x02\x03",
            "#010F……以上就是这次任务的报告。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x1, 0x4, 0x10)
    Sleep(100)
    OP_AF(0x4, 0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#740F初次任务，你们辛苦了。\x02\x03",
            "从工作报告看来，\x01",
            "你们都已经很努力了。\x02\x03",
            "我觉得足够引以为荣哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F是、是吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#741F没问题，下次会做得更好的。\x02\x03",
            "再有什么事的话，还要靠你们哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F……嗯……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F…………………………\x02\x03",
            "#010F那么艾丝蒂尔，我们回去吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F好吧～……\x02\x03",
            "#000F得回去做晚饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#743F啊，稍等一下。\x01",
            "刚好有一封信是寄给卡西乌斯先生的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "#740F刚才没有机会交给他，\x01",
            "帮我转交一下好吗？\x02",
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
            "得到了\x07\x02",
            "致卡西乌斯的信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x336, 1)

    ChrTalk(
        0x101,
        "#000F……是和工作有关的联络吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F我想应该是。\x01",
            "好像是从国外的支部寄来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F国外的支部……吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#740F拥有游击士协会的国家\x01",
            "并不只局限于利贝尔王国。\x02\x03",
            "卡西乌斯先生的交际很广，\x01",
            "所以经常会收到这样的信件。\x02\x03",
            "那么，就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x212)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_4B(0x8, 0)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_30_E4FB end

    def Function_31_EC90(): pass

    label("Function_31_EC90")


    ChrTalk(
        0xB,
        (
            "啊，对了对了。\x01",
            "这是我给你们的贺礼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不过说起来，\x01",
            "这其实是刚进货的试销品而已。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "料理手册\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x20D, 1)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(100)

    ChrTalk(
        0x101,
        "#004F啊，这是什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F手册里面的食谱，是做料理用的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "和魔兽战斗受伤的时候，\x01",
            "总是使用药的话不是太花钱了吗？\x02\x03",
            "用料理代替的话可以节省很多钱呢，\x01",
            "有材料就可以做出多种有回复效果的料理。\x02\x03",
            "只要尝过新的料理，\x01",
            "就可以把食谱写到那个手册里面，\x01",
            "慢慢地就会掌握越来越多的料理做法了。\x02\x03",
            "那么，你们来试试看吧。\x01",
            "艾丝蒂尔，尝尝这块曲奇。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "枫糖曲奇\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿嘿⊙\x01",
            "那我就不客气了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "尝了尝\x07\x02",
            "枫糖曲奇\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_31(0x0, 0xFD, 0x50)
    OP_AC(0x14)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "枫糖曲奇\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0xB,
        (
            "……就是这样子了。\x02\x03\x07\x04",
            "尝过料理并且记住它的做法\x07\x00",
            "是基本的要领。\x01",
            "没见过的料理更要去尝尝看，\x01",
            "反正看到什么吃什么就是了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F原来如此，真是方便啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯～虽然我不讨厌做饭，\x01",
            "但是做出来的东西都不太好吃……\x02\x03",
            "#006F不过我也想多学些菜式，\x01",
            "让老爸对我另眼相看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "对对，有这种志气已经很不错了。\x02\x03",
            "你们要买食物材料时，\x01",
            "记得到我的店子里挑挑看哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#4P啊哈哈。\x01",
            "不愧是里农叔叔，真会做生意啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F真是谢谢你了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※在酒吧食用『推荐料理』，\x01",
            "　或使用『便携食物』时，\x01",
            "　其烹饪方法便会自动记录到料理手册上。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※使用料理手册会显示已记录的料理，\x01",
            "　如果具备必要的材料便可以将其烹调出来。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※料理分为当场食用的『大盘料理』和\x01",
            "　可作为道具而随身携带的『便携料理』。\x01",
            "　即使做出『大盘料理』，也没办法变成道具带走。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※料理所使用的『食物材料』\x01",
            "　可以在杂货铺等店铺购买。\x01",
            "　此外，部分材料也可以通过击败魔兽获得。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Return()

    # Function_31_EC90 end

    SaveToFile()

Try(main)
