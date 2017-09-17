from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4121   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T4121   ._SN',
            'ED6_DT01/T4121_1 ._SN',
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
        '艾南',                                 # 9
        '卡露娜',                               # 10
        '亚妮拉丝',                             # 11
        '库拉茨',                               # 12
        '克鲁茨',                               # 13
        '尤莉亚中尉',                           # 14
        '阿加特',                               # 15
        '雪拉扎德',                             # 16
        '金',                                   # 17
        '卡西乌斯',                             # 18
        '费瑟尔',                               # 19
        '罗伊德',                               # 20
        '拜舍尔',                               # 21
        '赫穆特',                               # 22
        '玛多克工房长',                         # 23
        '克劳斯市长',                           # 24
        '奥利维尔',                             # 25
        '穆拉',                                 # 26
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
        'ED6_DT07/CH02580 ._CH',             # 00
        'ED6_DT07/CH01240 ._CH',             # 01
        'ED6_DT07/CH01630 ._CH',             # 02
        'ED6_DT07/CH01260 ._CH',             # 03
        'ED6_DT07/CH01620 ._CH',             # 04
        'ED6_DT06/CH20112 ._CH',             # 05
        'ED6_DT07/CH01410 ._CH',             # 06
        'ED6_DT07/CH00050 ._CH',             # 07
        'ED6_DT07/CH00020 ._CH',             # 08
        'ED6_DT07/CH00070 ._CH',             # 09
        'ED6_DT07/CH02000 ._CH',             # 0A
        'ED6_DT07/CH01200 ._CH',             # 0B
        'ED6_DT07/CH01020 ._CH',             # 0C
        'ED6_DT07/CH01460 ._CH',             # 0D
        'ED6_DT07/CH01220 ._CH',             # 0E
        'ED6_DT07/CH01633 ._CH',             # 0F
        'ED6_DT07/CH02620 ._CH',             # 10
        'ED6_DT07/CH02350 ._CH',             # 11
        'ED6_DT07/CH00030 ._CH',             # 12
        'ED6_DT07/CH02190 ._CH',             # 13
        'ED6_DT06/CH20038 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH02580P._CP',             # 00
        'ED6_DT07/CH01240P._CP',             # 01
        'ED6_DT07/CH01630P._CP',             # 02
        'ED6_DT07/CH01260P._CP',             # 03
        'ED6_DT07/CH01620P._CP',             # 04
        'ED6_DT06/CH20112P._CP',             # 05
        'ED6_DT07/CH01410P._CP',             # 06
        'ED6_DT07/CH00050P._CP',             # 07
        'ED6_DT07/CH00020P._CP',             # 08
        'ED6_DT07/CH00070P._CP',             # 09
        'ED6_DT07/CH02000P._CP',             # 0A
        'ED6_DT07/CH01200P._CP',             # 0B
        'ED6_DT07/CH01020P._CP',             # 0C
        'ED6_DT07/CH01460P._CP',             # 0D
        'ED6_DT07/CH01220P._CP',             # 0E
        'ED6_DT07/CH01633P._CP',             # 0F
        'ED6_DT07/CH02620P._CP',             # 10
        'ED6_DT07/CH02350P._CP',             # 11
        'ED6_DT07/CH00030P._CP',             # 12
        'ED6_DT07/CH02190P._CP',             # 13
        'ED6_DT06/CH20038P._CP',             # 14
    )

    DeclNpc(
        X                   = -4460,
        Z                   = 0,
        Y                   = 960,
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
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 27820,
        Z                   = 0,
        Y                   = 62520,
        Direction           = 191,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 84510,
        Z                   = 0,
        Y                   = 56870,
        Direction           = 274,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 90050,
        Z                   = 0,
        Y                   = 63770,
        Direction           = 15,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 25740,
        Z                   = 0,
        Y                   = 58130,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 25470,
        Z                   = 0,
        Y                   = 58140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 31740,
        Z                   = 0,
        Y                   = 63030,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -2600,
        TriggerZ            = 0,
        TriggerY            = 820,
        TriggerRange        = 800,
        ActorX              = -4460,
        ActorZ              = 1500,
        ActorY              = 960,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 27820,
        TriggerZ            = 0,
        TriggerY            = 60600,
        TriggerRange        = 800,
        ActorX              = 27820,
        ActorZ              = 1500,
        ActorY              = 62520,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4970,
        TriggerZ            = 0,
        TriggerY            = -1040,
        TriggerRange        = 1400,
        ActorX              = 4970,
        ActorZ              = 2000,
        ActorY              = -1040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3FE",          # 00, 0
        "Function_1_665",          # 01, 1
        "Function_2_6F5",          # 02, 2
        "Function_3_70B",          # 03, 3
        "Function_4_72F",          # 04, 4
        "Function_5_7BB",          # 05, 5
        "Function_6_1015",         # 06, 6
        "Function_7_1ADA",         # 07, 7
        "Function_8_1BA3",         # 08, 8
        "Function_9_1C21",         # 09, 9
        "Function_10_1C26",        # 0A, 10
        "Function_11_2E04",        # 0B, 11
        "Function_12_2E09",        # 0C, 12
        "Function_13_941A",        # 0D, 13
        "Function_14_B2F8",        # 0E, 14
        "Function_15_B351",        # 0F, 15
        "Function_16_BB74",        # 10, 16
        "Function_17_D66F",        # 11, 17
        "Function_18_EA57",        # 12, 18
        "Function_19_F8AF",        # 13, 19
        "Function_20_F8F9",        # 14, 20
        "Function_21_F943",        # 15, 21
    )


    def Function_0_3FE(): pass

    label("Function_0_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_40C")
    OP_A3(0x3FA)
    Event(0, 15)

    label("loc_40C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_41A")
    OP_A3(0x3FB)
    Event(0, 16)

    label("loc_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_428")
    OP_A3(0x3FC)
    Event(0, 17)

    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_436")
    OP_A3(0x3FD)
    Event(0, 18)

    label("loc_436")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_442"),
        (SWITCH_DEFAULT, "loc_458"),
    )


    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_455")
    OP_A2(0x609)
    Event(0, 13)

    label("loc_455")

    Jump("loc_458")

    label("loc_458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_46C")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_664")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_476")
    Jump("loc_664")

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_END)), "loc_49A")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 120230, 0, -2360, 90)

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_END)), "loc_4B7")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 122900, 0, -2350, 270)

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_END)), "loc_4D4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 121650, 0, -3900, 0)

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_END)), "loc_4F1")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 121680, 0, -830, 180)

    label("loc_4F1")

    Jump("loc_664")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_538")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 62290, 0, -3770, 108)
    OP_43(0xC, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 58990, 0, 2730, 7)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_664")

    label("loc_538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_547")
    SetChrFlags(0x14, 0x80)
    Jump("loc_664")

    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_584")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 54920, 0, -3370, 95)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 58990, 0, 2730, 7)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_664")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5DE")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 58990, 0, 2730, 7)
    OP_43(0x9, 0x0, 0x0, 0x2)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 15)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x4)
    OP_44(0xA, 0xFF)
    SetChrPos(0xA, 58500, 200, -3440, 90)
    Jump("loc_664")

    label("loc_5DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_61B")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 54920, 0, -3370, 95)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 58990, 0, 2730, 7)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_664")

    label("loc_61B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_62A")
    ClearChrFlags(0x15, 0x80)
    Jump("loc_664")

    label("loc_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_65D")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 15)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x4)
    OP_44(0xA, 0xFF)
    SetChrPos(0xA, 58500, 200, -3440, 90)
    Jump("loc_664")

    label("loc_65D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_664")

    label("loc_664")

    Return()

    # Function_0_3FE end

    def Function_1_665(): pass

    label("Function_1_665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_695")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6A8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B8")

    label("loc_6A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_6B8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6EB")
    OP_B1("t4121_y")
    Jump("loc_6F4")

    label("loc_6EB")

    OP_B1("t4121_n")

    label("loc_6F4")

    Return()

    # Function_1_665 end

    def Function_2_6F5(): pass

    label("Function_2_6F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6F5")

    label("loc_70A")

    Return()

    # Function_2_6F5 end

    def Function_3_70B(): pass

    label("Function_3_70B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72E")
    OP_8D(0xFE, 84890, 62930, 95170, 65019, 2000)
    Jump("Function_3_70B")

    label("loc_72E")

    Return()

    # Function_3_70B end

    def Function_4_72F(): pass

    label("Function_4_72F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Oh ho ho...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说实话，我的确没有想到\x01",
            "这里会是一个正式的俱乐部呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_72F end

    def Function_5_7BB(): pass

    label("Function_5_7BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_86D")

    ChrTalk(
        0xFE,
        (
            "武术大会和诞辰庆典，\x01",
            "都是全体市民\x01",
            "参加的活动吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可就算是在这种活动当日，\x01",
            "我们的社团里仍然有\x01",
            "很多人继续去钓鱼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_9AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_90B")

    ChrTalk(
        0xFE,
        (
            "对于喜好外出的我而言，\x01",
            "像这样进退不能\x01",
            "真是一种折磨啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好想快点乘坐飞艇\x01",
            "到别的地方去钓鱼啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A7")

    label("loc_90B")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于喜好外出的我而言，\x01",
            "像这样进退不能\x01",
            "真是一种折磨啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好想快点乘坐飞艇\x01",
            "到别的地方去钓鱼啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A7")

    Jump("loc_1011")

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_A73")

    ChrTalk(
        0xFE,
        (
            "我本打算要去卢安，\x01",
            "刚到达空港准备乘定期船，\x01",
            "士兵们就突然来将空港封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "许久没有去海边垂钓了，\x01",
            "本来还以为这次可以好好享受一番呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B37")

    ChrTalk(
        0xFE,
        (
            "在今天举办的讲座上，\x01",
            "有一位热心的女士\x01",
            "迫切地希望加入我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "讲座结束后，\x01",
            "她还留在湖边继续钓鱼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B41")
    Jump("loc_1011")

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BE6")

    ChrTalk(
        0xFE,
        (
            "明天要举办一场\x01",
            "面向新手的讲座。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于我们来说，\x01",
            "如果能让参加者明白\x01",
            "钓鱼的乐趣就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C80")

    label("loc_BE6")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "明天要举办一场\x01",
            "面向新手的讲座。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "会有什么样的人来，\x01",
            "我真是很期待啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能让他们明白\x01",
            "钓鱼的乐趣就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C80")

    Jump("loc_1011")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C8D")
    Jump("loc_1011")

    label("loc_C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D3A")

    ChrTalk(
        0xFE,
        (
            "为了钓鱼而事先做准备\x01",
            "也很有乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "根据自己想要\x01",
            "钓上多大的鱼\x01",
            "来决定带些什么渔具。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_DDF")

    ChrTalk(
        0xFE,
        (
            "本来觉得用自己做的鱼饵\x01",
            "钓不到什么鱼，\x01",
            "但实际钓起来却意外地管用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "用自己做的鱼饵\x01",
            "来钓鱼很令人开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_E64")

    ChrTalk(
        0xFE,
        (
            "在卢安还是\x01",
            "没能见到努西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在蔡斯也没有\x01",
            "什么大的收获。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我还要加把劲啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1011")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F17")

    ChrTalk(
        0xFE,
        (
            "团长费瑟尔先生\x01",
            "原来是贵族出身。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此我们都称他为\x01",
            "『钓鱼男爵』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_F17")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "团长费瑟尔先生\x01",
            "原来是贵族出身。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为非常喜欢钓鱼，\x01",
            "所以倾尽财产\x01",
            "成立了钓公师团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此我们都称他为\x01",
            "『钓鱼男爵』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1011")

    TalkEnd(0xFE)
    Return()

    # Function_5_7BB end

    def Function_6_1015(): pass

    label("Function_6_1015")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_10B4")

    ChrTalk(
        0xFE,
        (
            "为了发动政变而进行封锁，\x01",
            "剥夺了我们钓鱼的权利，\x01",
            "理查德上校真是不可饶恕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1150")

    ChrTalk(
        0xFE,
        (
            "雷那特川……\x01",
            "瓦雷利亚湖……\x01",
            "亚瑟利亚湾都在呼唤我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，拜托了，\x01",
            "让我拿起钓鱼竿吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_1150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_12A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_11E1")

    ChrTalk(
        0xFE,
        (
            "不能去钓鱼，\x01",
            "对于我来说\x01",
            "可是痛苦万分的事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我都快发疯了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_129E")

    label("loc_11E1")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "什么时候\x01",
            "才能到外地去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不能去钓鱼，\x01",
            "对于我来说\x01",
            "可是痛苦万分的事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我都快发疯了。\x02",
    )

    CloseMessageWindow()

    label("loc_129E")

    Jump("loc_1AD6")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1344")

    ChrTalk(
        0xFE,
        (
            "不快点逮捕\x01",
            "恐怖分子的话，\x01",
            "就不能安心去钓鱼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "快点采取行动吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_1344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_13EB")

    ChrTalk(
        0xFE,
        "拜舍尔今天要出席一个讲座。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "努力推广钓鱼运动\x01",
            "也是我们的职责之一啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_13EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_147D")

    ChrTalk(
        0xFE,
        (
            "昨天入团考试时\x01",
            "钓场的条件真不错啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我是考官，\x01",
            "不过不由自主就想垂下鱼竿钓鱼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_147D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1487")
    Jump("loc_1AD6")

    label("loc_1487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1502")

    ChrTalk(
        0xFE,
        (
            "因为我是\x01",
            "明天入团测试的考官，\x01",
            "所以必须得到湖畔去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要趁现在\x01",
            "赶快准备好才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_1502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_16B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_15C6")

    ChrTalk(
        0xFE,
        (
            "利贝尔虽说是个小国，\x01",
            "但海、河、湖这些\x01",
            "适合钓鱼的场所非常多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以，\x01",
            "开拓新的钓场\x01",
            "也是我们的任务哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B2")

    label("loc_15C6")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "利贝尔虽说是个小国，\x01",
            "但对钓鱼爱好者而言是个很不错的国家哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "海、河、湖这些\x01",
            "适合钓鱼的场所所非常多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以，\x01",
            "开拓新的钓场\x01",
            "也是我们的任务哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B2")

    Jump("loc_1AD6")

    label("loc_16B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_178D")

    ChrTalk(
        0xFE,
        (
            "瓦雷利亚湖的努西\x01",
            "因为气温下降\x01",
            "而潜入较深的水域了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算是这样，\x01",
            "我也要知难而进，\x01",
            "再一次把它找出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_178D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1AD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_187E")

    ChrTalk(
        0xFE,
        (
            "我追寻瓦雷利亚湖的努西\x01",
            "已经接近五年了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次是第２３回的挑战，\x01",
            "一定要把它给钓上来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_187E")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "呀，欢迎来到钓公师团。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F……咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们不就是到柏斯的湖畔\x01",
            "调查事件的游击士吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F啊，\x01",
            "您是把空贼的情报告诉我们的那位……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈～哈～想起来了啊。\x01",
            "再次欢迎来到钓公师团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F钓公师团……\x01",
            "我是觉得有些耳熟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正如你所知，\x01",
            "这里是我们活动的根据地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请在这里好好放松一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1AD6")

    TalkEnd(0xFE)
    Return()

    # Function_6_1015 end

    def Function_7_1ADA(): pass

    label("Function_7_1ADA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#800F钓鱼用具是一种功能性\x01",
            "和艺术性兼备的道具。\x02\x03",
            "#801F就算不钓鱼，\x01",
            "也还是想要啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1ADA end

    def Function_8_1BA3(): pass

    label("Function_8_1BA3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#600F短短的时间内就发生了那么多事，\x01",
            "让人的心情难以平静啊。\x02\x03",
            "到瓦雷利亚湖去垂钓，\x01",
            "放松一下心情吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1BA3 end

    def Function_9_1C21(): pass

    label("Function_9_1C21")

    Call(0, 10)
    Return()

    # Function_9_1C21 end

    def Function_10_1C26(): pass

    label("Function_10_1C26")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_224C")
    OP_A2(0x67C)

    ChrTalk(
        0x12,
        (
            "哈哈！\x01",
            "欢迎来到钓公师团！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F钓公师团？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "对！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "利贝尔各地的钓鱼场\x01",
            "潜藏着一种\x01",
            "名为『努西』的巨大鱼类……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "找到它们，\x01",
            "并顺利钓到手\x01",
            "就是我们的最终目标！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F哈～\x01",
            "原来是钓鱼爱好者的集团嘛。\x02\x03",
            "我也喜欢钓鱼，\x01",
            "对这里也比较感兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F不过我看了看，\x01",
            "似乎举办的活动都是非常正式的吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "嗯，我们这些志同道合的人\x01",
            "为了达成宏伟的宿愿，\x01",
            "在利贝尔各地日复一日地开展活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "为了尽量推广钓鱼这项运动，\x01",
            "我们还开办了面向初学者的课程，\x01",
            "并且出售自制的钓鱼用具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "从中获得的利益\x01",
            "会作为保护钓场环境的委托金\x01",
            "交纳给女王陛下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哇，\x01",
            "的确是非常专业嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F不愧是真正的爱好者集团啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "那么你们愿意加入我们的团队吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "如果想加入的话，\x01",
            "是需要进行考试的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F这、这个，虽然很有趣，\x01",
            "但我们现在还有事情要办。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "这样啊，\x01",
            "你们两个看起来很有潜力呢，\x01",
            "不加入实在是有些可惜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "如果改变主意了，\x01",
            "随时都可以来这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "我们真诚期待着\x01",
            "希望入团的志愿者。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_224C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_239C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_22D0")

    ChrTalk(
        0x12,
        (
            "前些日子新加入了\x01",
            "一位很有前途的女士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "成为本团的一员\x01",
            "是十分值得庆贺的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2399")

    label("loc_22D0")

    OP_A2(0x2)

    ChrTalk(
        0x12,
        (
            "前些日子新加入了\x01",
            "一位很有前途的女士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "成为本团的一员\x01",
            "是十分值得庆贺的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "嗯嗯，虽说她是个新手，\x01",
            "但使用钓鱼竿的技术不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2399")

    Jump("loc_2E00")

    label("loc_239C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2425")

    ChrTalk(
        0x12,
        (
            "直到刚才，\x01",
            "外面还在吵吵嚷嚷的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "如果在钓场\x01",
            "也那么吵闹的话，\x01",
            "就没办法钓到鱼了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_2425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_257B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2495")

    ChrTalk(
        0x12,
        (
            "现在既不能夜间外出，\x01",
            "也不能到外地去，\x01",
            "真是难办啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "这真是我团创立以来\x01",
            "遇到的最糟糕的情况了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2578")

    label("loc_2495")

    OP_A2(0x2)

    ChrTalk(
        0x12,
        (
            "因为禁止夜间外出，\x01",
            "所以现在不能去夜钓了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "不但如此，\x01",
            "现在就连去外地\x01",
            "钓鱼也不行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "这真是我团创立以来\x01",
            "遇到的最糟糕的情况了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2578")

    Jump("loc_2E00")

    label("loc_257B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_263F")

    ChrTalk(
        0x12,
        (
            "今天的天气很好，\x01",
            "非常适合\x01",
            "去钓场钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "工作结束后，\x01",
            "和团员们一起去湖边看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_263F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_26EC")

    ChrTalk(
        0x12,
        (
            "昨天，来了一位客人，\x01",
            "虽然是一位初学者，\x01",
            "不过却对钓鱼抱有非常浓厚的兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "我们的组织能够打动人心，\x01",
            "归功于拜舍尔不懈的宣传啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_26EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_28F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27C8")

    ChrTalk(
        0x12,
        (
            "只要您打心眼里喜欢钓鱼，\x01",
            "并且有一定的基本技术，\x01",
            "就欢迎您加入我们的行列。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "今天的考生技术还可以，\x01",
            "但是感受不到\x01",
            "他们的干劲及热情……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F1")

    label("loc_27C8")

    OP_A2(0x2)

    ChrTalk(
        0x12,
        (
            "只要您打心眼里喜欢钓鱼，\x01",
            "并且有一定的基本技术，\x01",
            "就欢迎您加入我们的行列。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "今天的考生技术还可以，\x01",
            "但是感受不到\x01",
            "他们的干劲及热情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "唉，真是可惜。\x02",
    )

    CloseMessageWindow()

    label("loc_28F1")

    Jump("loc_2E00")

    label("loc_28F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_299D")

    ChrTalk(
        0x12,
        (
            "今天要在瓦雷利亚湖\x01",
            "举行入团考试呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "团员们作为监考官，\x01",
            "全都倾巢而出了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_299D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A48")

    ChrTalk(
        0x12,
        (
            "如果真的喜欢钓鱼，\x01",
            "那么遵守钓鱼场的规则\x01",
            "是理所应当要做到的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "团员一旦在钓鱼场\x01",
            "乱丢垃圾的话，\x01",
            "我们就会立刻责令其退团。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B53")

    label("loc_2A48")

    OP_A2(0x2)

    ChrTalk(
        0x12,
        (
            "如果真的喜欢钓鱼，\x01",
            "那么遵守钓鱼场的规则\x01",
            "是理所应当要做到的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "团员一旦在钓鱼场\x01",
            "乱丢垃圾的话，\x01",
            "我们就会立刻责令其退团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "但我相信\x01",
            "不会有那样无知的人的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B53")

    Jump("loc_2E00")

    label("loc_2B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2CAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2BF7")

    ChrTalk(
        0x12,
        (
            "我们这里销售的\x01",
            "钓鱼用具广受好评。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "甚至还有顾客\x01",
            "从很远的地方乘坐飞艇来买。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CAA")

    label("loc_2BF7")

    OP_A2(0x2)

    ChrTalk(
        0x12,
        (
            "我们这里销售的\x01",
            "钓鱼用具广受好评。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "甚至还有顾客\x01",
            "从很远的地方乘坐飞艇来买。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "以上所说决无虚言。\x02",
    )

    CloseMessageWindow()

    label("loc_2CAA")

    Jump("loc_2E00")

    label("loc_2CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2D86")

    ChrTalk(
        0x12,
        (
            "就像武术大会一样，\x01",
            "我们也要招募参加者\x01",
            "来举行一次钓鱼大会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "当然，我也会参加。\x01",
            "我可是不会认输的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_2D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2E00")

    ChrTalk(
        0x12,
        (
            "如果你们改变主意了，\x01",
            "随时都可以来这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "我们真诚期待着\x01",
            "希望入团的志愿者。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E00")

    TalkEnd(0x12)
    Return()

    # Function_10_1C26 end

    def Function_11_2E04(): pass

    label("Function_11_2E04")

    Call(0, 12)
    Return()

    # Function_11_2E04 end

    def Function_12_2E09(): pass

    label("Function_12_2E09")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_314D")
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3011")

    ChrTalk(
        0x8,
        (
            "#760F各位，你们辛苦了。\x02\x03",
            "#760F艾尔贝离宫解放作战\x01",
            "干得相当漂亮。\x02\x03",
            "好不容易有这个机会，\x01",
            "就把报酬给你们吧。\x02\x03",
            "可以作为今后作战必要的资金。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_AF(0x63, 0x4B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x4C, 0x4, 0x10)
    OP_28(0x4C, 0x4, 0x20)

    ChrTalk(
        0x8,
        (
            "#760F继续保持警惕前进吧，\x01",
            "祝你们好运。\x02\x03",
            "我们也会尽全力给你们以支援的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3144")

    label("loc_3011")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x63)"), scpexpr(EXPR_END)), "loc_30AA")
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#760F辛苦了。\x01",
            "看来顺利地完成了任务呢。\x02\x03",
            "如果完成其他任务的话，\x01",
            "请再来我这里报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3144")

    label("loc_30AA")

    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#760F现在好像没有需要报告的任务。\x01",
            "　\x02\x03",
            "如果完成其他任务的话，\x01",
            "请再来我这里报告。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3144")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_314D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_315E")
    TalkEnd(0x8)
    Return()

    label("loc_315E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3397")
    EventBegin(0x0)

    ChrTalk(
        0x8,
        (
            "#760F哦，是你们。\x02\x03",
            "一旦开始作战，\x01",
            "就没有机会回到市区了。\x02\x03",
            "已经准备完毕了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【准备好了】\x01",          # 0
            "【还没有准备好】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_32B3"),
        (1, "loc_333E"),
        (SWITCH_DEFAULT, "loc_3394"),
    )


    label("loc_32B3")

    OP_A2(0x650)
    OP_28(0x4C, 0x4, 0x2)
    OP_28(0x4C, 0x4, 0x4)
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
        (
            "#764F好的。\x02\x03",
            "#762F那么就请在此等候，\x01",
            "时间一到就开始作战。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_333E")


    ChrTalk(
        0x8,
        (
            "#760F我知道了。\x02\x03",
            "你们准备好的话请和我说一声。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 0)
    OP_4B(0x8, 255)
    EventEnd(0x1)
    Return()

    label("loc_3394")

    Jump("loc_9416")

    label("loc_3397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5925")
    EventBegin(0x0)
    OP_A2(0x650)
    OP_28(0x4B, 0x1, 0x800)
    OP_28(0x4B, 0x1, 0x1000)
    Fade(1000)
    OP_4A(0x8, 255)
    OP_6D(-3330, 0, 750, 0)
    SetChrPos(0x101, -2590, 0, 280, 270)
    SetChrPos(0x102, -2590, 0, 1220, 270)
    SetChrPos(0x108, -1500, 0, 750, 270)
    OP_8C(0x8, 90, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#760F其他的几位游击士已经全部集中起来了。\x01",
            "　\x02\x03",
            "和记者还有亲卫队的人员取得了联络吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F很遗憾……\x01",
            "和他们两方都没能取得联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F但必要的情报基本上都收集好了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们向众人说明了\x01",
            "在杂志社和大圣堂打听到的情报。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#764F原来如此……\x01",
            "科洛蒂娅公主被囚禁在艾尔贝离宫\x01",
            "这一点已经确信无疑了。\x02\x03",
            "#762F亲卫队没来虽然很遗憾，\x01",
            "但已经知道他们没有被捕，\x01",
            "这样已经足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F那么我们这就开始好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F嗯……\x02\x03",
            "全体人员。\x01",
            "现在开始制定作战计划。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_6D(122020, 0, -2070, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(1200, 0)
    OP_6C(315000, 0)
    OP_6E(678, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xC, 123360, 0, -2490, 1)
    SetChrPos(0x9, 123640, 0, -1210, 350)
    SetChrPos(0xB, 125100, 0, -1960, 320)
    SetChrPos(0xA, 124920, 0, -560, 315)
    SetChrPos(0x101, 120480, 0, 820, 90)
    SetChrPos(0x102, 120560, 0, -380, 45)
    SetChrPos(0x108, 121320, 0, -1960, 0)
    SetChrPos(0x8, 122790, 0, 1800, 180)
    OP_4A(0xC, 255)
    OP_4A(0x9, 255)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    OP_1D(0x65)
    FadeToBright(2000, 0)
    OP_6D(122020, 0, 1070, 2500)

    ChrTalk(
        0x8,
        (
            "#764F……以上所说的就是\x01",
            "情报部正在发动的政变的详细情况。\x02\x03",
            "#762F根据这些事实，\x01",
            "王都支部决定接受女王陛下的委托。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#844F没想到竟然有如此大的阴谋\x01",
            "正在进行着……\x02\x03",
            "连这种事情都看不穿，\x01",
            "真恨自己这样没用啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#813F虽然之前就觉得\x01",
            "那一伙特务兵比较可疑……\x02\x03",
            "但我一直认为理查德上校\x01",
            "看起来是个好人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#833F非但不是，\x01",
            "而且他居然还是空贼事件和\x01",
            "戴尔蒙市长事件的幕后操纵者……\x02\x03",
            "#832F这不就是在小瞧\x01",
            "我们这些游击士吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#822F如果不给个说法，\x01",
            "我们是无论如何也不会接受的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F那么各位，请你们协助我们好吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#820F那是当然！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#830F我会听从吩咐的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#840F我要让他们……加倍偿还。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#816F请让我也加入你们！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        (
            "#008F哇啊～……这可太好了！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x01",
            "的确大家都是很值得信赖的伙伴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764F接下来就开始制定救出作战计划。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BF8():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BF8)

    def lambda_3C06():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C06)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#762F人质的性命最为要紧，\x01",
            "所以不能进行持久战。\x02\x03",
            "我们只有采取强行攻入，\x01",
            "然后各个击破这种作战方法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#824F没有时间去探明进攻线路了，\x01",
            "看来也只有采取这个办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#832F可是要进攻离宫的话，\x01",
            "不如分别行动怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#840F……佯攻组和突入组，\x01",
            "兵分两路行事比较可靠。\x02\x03",
            "如果给敌人制造了骚乱的话，\x01",
            "就可以吸引敌人的大部分战斗力，\x01",
            "然后突入队员就可以乘机冲进去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#5P但大家不要忘记了，对手可是\x01",
            "王国军中精英级别的情报部特别部队。\x02\x03",
            "我想说的是，作战中最好还要有\x01",
            "佯攻时的伏击组以及突入时的扰乱组。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(
        0x101,
        (
            "#004F#5P咦……\x01",
            "这是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F首先佯攻组佯攻，\x01",
            "然后伏击组以逸待劳地痛击追来的敌人……\x02\x03",
            "扰乱组给敌人制造混乱，\x01",
            "让突入组的行动变得轻而易举。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#5P原来是这样啊……\x02\x03",
            "#505F可是就我们这几个人，\x01",
            "要想那样分配有些勉强啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#765F嗯……没办法啊。\x02\x03",
            "虽然联络了其他支部，\x01",
            "但是由于关所和飞艇坪都被封锁了，\x01",
            "那些游击士就来不了这里了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4181():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4181)
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        (
            "#007F这样啊……\x02\x03",
            "#003F如果这个时候雪拉姐和\x01",
            "阿加特他们在就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764F……金先生说得很对，\x01",
            "只分为佯攻和突入两个组危险性较大。\x01",
            "　\x02\x03",
            "或许只有重新制定其他的方案了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xD, 123420, -2000, 4570, 270)

    NpcTalk(
        0xD,
        "女性的声音",
        (
            "#1P不必了。\x01",
            "不足的战斗力由我们来补充。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 6)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4396():

        label("loc_4396")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4396")

    QueueWorkItem2(0x101, 1, lambda_4396)

    def lambda_43A7():

        label("loc_43A7")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43A7")

    QueueWorkItem2(0x102, 1, lambda_43A7)

    def lambda_43B8():

        label("loc_43B8")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43B8")

    QueueWorkItem2(0x108, 1, lambda_43B8)

    def lambda_43C9():

        label("loc_43C9")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43C9")

    QueueWorkItem2(0xB, 1, lambda_43C9)

    def lambda_43DA():

        label("loc_43DA")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43DA")

    QueueWorkItem2(0x9, 1, lambda_43DA)

    def lambda_43EB():

        label("loc_43EB")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43EB")

    QueueWorkItem2(0xC, 1, lambda_43EB)

    def lambda_43FC():

        label("loc_43FC")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43FC")

    QueueWorkItem2(0xA, 1, lambda_43FC)

    def lambda_440D():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_440D)
    SetChrFlags(0x8, 0x4)

    def lambda_4420():
        OP_8F(0xFE, 0x1DCE0, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4420)

    def lambda_443B():
        OP_8E(0xFE, 0x1D57E, 0x0, 0x132E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_443B)
    OP_6D(120550, 0, 3300, 2000)
    WaitChrThread(0xD, 0x1)
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(
        0x101,
        "#004F#5P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#5P尤莉亚中尉……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F#5P哦，这位不就是\x01",
            "我们在周游道遇见的修女吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_44DB():

        label("loc_44DB")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_44DB")

    QueueWorkItem2(0x8, 1, lambda_44DB)

    def lambda_44EC():
        OP_8E(0xFE, 0x1D47A, 0x0, 0xBF4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_44EC)
    OP_6D(121320, 0, 1770, 2000)
    WaitChrThread(0xD, 0x1)
    Fade(1000)
    SetChrChipByIndex(0xD, 5)
    TurnDirection(0xD, 0x8, 400)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#465F初次见面，你们好。\x02\x03",
            "#460F我是王室亲卫队的中队长，\x01",
            "尤莉亚·舒华兹中尉。\x02\x03",
            "请让我们亲卫队来协助你们的作战。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(122540, 0, 820, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(1200, 0)
    OP_6C(315000, 0)
    OP_6E(678, 0)
    OP_44(0xB, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xD, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xC, 124600, 0, -2300, 340)
    SetChrPos(0x9, 124530, 0, -1010, 319)
    SetChrPos(0xB, 125530, 0, -570, 294)
    SetChrPos(0xA, 125290, 0, 750, 284)
    SetChrPos(0x101, 120540, 0, 1210, 75)
    SetChrPos(0x102, 120520, 0, 190, 45)
    SetChrPos(0x108, 120880, 0, -1300, 64)
    SetChrPos(0x8, 122790, 0, 1800, 180)
    SetChrPos(0xD, 122810, 0, -1980, 7)
    TurnDirection(0xC, 0xD, 0)
    TurnDirection(0x9, 0xD, 0)
    TurnDirection(0xB, 0xD, 0)
    TurnDirection(0xA, 0xD, 0)
    TurnDirection(0x101, 0xD, 0)
    TurnDirection(0x102, 0xD, 0)
    TurnDirection(0x108, 0xD, 0)
    TurnDirection(0x8, 0xD, 0)
    TurnDirection(0xD, 0x8, 0)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#760F原来如此……\x01",
            "您的意思我明白了。\x02\x03",
            "包括您在内的八名队员将协助\x01",
            "我们的营救作战计划对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#460F我的队员虽然分散潜伏在王都里面。\x01",
            "　\x02\x03",
            "但是他们在一小时之内就能集合到一起。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#5P这、这样就好了，可是……\x02\x03",
            "尤莉亚小姐，\x01",
            "您是怎么得知我们要去营救人质的呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们为了转达这个消息到了大圣堂一趟，\x01",
            "但是没能见到尤莉亚中尉您的身影。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#465F这样啊……真是对不起。\x02\x03",
            "#460F不过我知道你们接受了陛下的委托。\x01",
            "　\x02\x03",
            "而且就在昨天晚上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#5P昨天晚上！？\x02\x03",
            "就是说在我们与女王陛下见面之后？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#461F呵呵……是的。\x02\x03",
            "总之，我们拥有连情报部\x01",
            "都不知道的特殊联络方法。\x02\x03",
            "前来协助你们也是陛下的指示。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#5P特殊的联络方法？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#464F嗯，该怎么说好呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#5P嗯，这样就行了。\x02\x03",
            "总算确保可以分为伏击组和扰乱组了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761F是啊，这样一来，\x01",
            "作战的成功率就大幅上升了。\x02\x03",
            "我们立刻决定人员的分配吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#465F明白了。\x02\x03",
            "#462F首先是佯攻组……\x01",
            "就由我们亲卫队中的四名成员来担任吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#820F的确，\x01",
            "正在被通缉的你们如果现身的话，\x01",
            "可以很有效地吸引敌人注意力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#460F啊，确实如此。\x02\x03",
            "具体来说，就是以在周游道外停放的\x01",
            "情报部的特务飞艇为目标。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F#5P特务飞艇……\x01",
            "就是特务兵乘坐的那个！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F周游道外围停放有飞艇……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F#5P对了，就是那个封锁住不让人进去的\x01",
            "所谓军事禁区……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#460F据我调查，\x01",
            "有数名特务兵是经常在那里看守的。\x02\x03",
            "对那里展开进攻后，与离宫保持联络的\x01",
            "支援部队就会朝着那里赶去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#814F啊，原来如此……\x02\x03",
            "#850F那个支援部队就是伏击组\x01",
            "要攻击的目标对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#840F#6P这样的话，\x01",
            "伏击组就由我们四人来担当吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#821F没错，在执行剿灭魔兽的任务时\x01",
            "就已经习惯了森林里的战斗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#830F我们之中也有用枪作为兵器的……\x01",
            "真是再合适不过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764F确实是人尽其材啊。\x02\x03",
            "#760F接下来是扰乱组和突入组……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#460F和佯攻组一样，\x01",
            "扰乱组就由亲卫队成员担当吧。\x02\x03",
            "由他们将特务兵的注意力吸引过来。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#5P……这么说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们就是突入组了，\x01",
            "负责解救人质对吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#070F#5P大家各自的行动都是为\x01",
            "我们这最重要的角色所做的准备工作。\x02\x03",
            "一定要鼓足干劲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#5P话、话是这么说，\x01",
            "可多少还是感觉有压力呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    def lambda_5384():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5384)
    TurnDirection(0x9, 0x101, 400)

    def lambda_5399():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5399)
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(
        0xD,
        (
            "#461F呵呵……\x01",
            "不用担心那么多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#831F不管怎么说，\x01",
            "你们都是武术大会的优胜组对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#841F#6P大部分敌人\x01",
            "都是奈何不了我们的。\x02",
            "#6P你们只需要考虑\x01",
            "救出人质这一点就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#5P尤莉亚中尉……各位前辈……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F并不是只有我们参与营救人质哦。\x01",
            "　\x02\x03",
            "集合大家的力量一定没问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5P嗯……！\x02\x03",
            "好的！\x01",
            "大干一场吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#071F#5P哦哦，很有干劲嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#764F作战会议到此结束。\x02",
    )

    CloseMessageWindow()

    def lambda_561B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_561B)

    def lambda_5629():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5629)

    def lambda_5637():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5637)

    def lambda_5645():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5645)

    def lambda_5653():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_5653)

    def lambda_5661():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5661)

    def lambda_566F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_566F)
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#760F作战计划今夜执行……\x01",
            "希望各位能巧妙借助这个黑夜取得成功。\x02\x03",
            "一旦开始作战，\x01",
            "就没有机会回到市区了。\x02\x03",
            "趁这段时间，\x01",
            "把缺少的东西补充齐备如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F啊，说的也是呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#465F我这就去和潜伏在王都的部下联络。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么我们就暂时先分头行事吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 119650, 0, 1610, 0)
    SetChrPos(0x102, 119650, 0, 1610, 0)
    SetChrPos(0x108, 119650, 0, 1610, 0)
    SetChrPos(0x8, -4460, 0, 960, 90)
    SetChrPos(0x9, 120230, 0, -2360, 90)
    SetChrPos(0xC, 122900, 0, -2350, 270)
    SetChrPos(0xB, 121650, 0, -3900, 0)
    SetChrPos(0xA, 121680, 0, -830, 180)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrFlags(0xD, 0x80)
    OP_6D(119650, 0, 1610, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_9416")

    label("loc_5925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A75")
    EventBegin(0x0)
    OP_A2(0x628)
    OP_28(0x48, 0x1, 0x80)
    Fade(1000)
    OP_6D(-4030, 0, 1100, 0)
    SetChrPos(0x101, -2590, 0, 280, 270)
    SetChrPos(0x102, -2590, 0, 1220, 270)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 90, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE8")

    ChrTalk(
        0x8,
        (
            "#761F艾丝蒂尔、约修亚。\x01",
            "听说你们顺利地进入决赛了呢。\x02\x03",
            "虽然对克鲁茨他们来说有点遗憾，\x01",
            "不过听说比赛打得很精彩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，真是白热化的战斗啊。\x02\x03",
            "#007F不过，和各位前辈比起来，\x01",
            "我们的实力还需要有待提高呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F说得没错。\x02\x03",
            "金先生就不用说了，\x01",
            "奥利维尔的枪法和魔法也帮了很大的忙。\x01",
            "　\x02\x03",
            "我们以后还要加倍努力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761F呵呵，有这种上进的意识，\x01",
            "我想你们一定会不断地进步的。\x02\x03",
            "#760F对了，\x01",
            "今天有没有打听到什么事情呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C73")

    label("loc_5BE8")


    ChrTalk(
        0x8,
        (
            "#760F艾丝蒂尔、约修亚。\x01",
            "《利贝尔通讯》那边怎么样了？\x02\x03",
            "有没有从那里得到什么情报？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C73")


    ChrTalk(
        0x102,
        "#012F嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚把奈尔调查到的情报报告给了艾南。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#763F原来如此……\x01",
            "洛伦斯少尉是『猎兵团』出身啊。\x01",
            "　\x02\x03",
            "#764F『杰斯塔猎兵团』……\x02\x03",
            "没有听说过的名字呢。\x01",
            "看来我要好好去调查一下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F游击士协会和猎兵团也有交往吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762F不，双方可以说是商业上的竞争对手。\x01",
            "　\x02\x03",
            "我们的规约是不能参与国家之间的战争，\x01",
            "而对他们来说这却是买卖的所在。\x01",
            "　\x02\x03",
            "在纷争不断的边境等地，\x01",
            "我们协会为了普通居民的安全，\x01",
            "曾经多次与他们处于对立的境地呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F……真是让人没有好感的组织啊。\x02\x03",
            "#505F但是……\x01",
            "这样不就没办法取得他们的情报了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F这点不用担心。\x01",
            "俗语有说『蛇行蛇道』……\x02\x03",
            "不过收集情报可能要花两三天时间。\x01",
            "会赶不上决赛的……\x01",
            "　\x02\x03",
            "这样也没关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F啊，没什么。\x01",
            "这不只是和大会有关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F拜托您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764F还有一条情报就是……\x01",
            "关于理查德上校在寻找\x01",
            "科洛蒂娅公主结婚对象的事情。\x02\x03",
            "其实……\x01",
            "和这个有关的情报也不是没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F……怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F好像在女王诞辰庆典那天\x01",
            "有一位埃雷波尼亚的皇族成员要来。\x02\x03",
            "虽然现在还不知道他的名字……\x01",
            "不过帝国的皇族自从十年前的\x01",
            "侵略战争以来还没有访问过利贝尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此，\x01",
            "感觉与之前的谈话很有关系呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F埃雷波尼亚的皇族吗。\x01",
            "是什么样的人，我们完全不知道呢。\x02\x03",
            "说起来，我们认识的帝国人\x01",
            "就只有奥利维尔一个呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#765F而且，科洛蒂娅公主才刚刚１６岁。\x01",
            "　\x02\x03",
            "这么着急结婚确实有点不自然啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎，是吗！？\x01",
            "不就是和我们一样大嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F对于上流阶级，\x01",
            "这正好是在社交界出道的年龄。\x02\x03",
            "#013F不过，以前从来没有听说过，\x01",
            "这个年龄结婚也太早了点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762F但是……\x01",
            "说不定这其中会有什么特别的理由。\x02\x03",
            "我觉得有调查的价值。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，我知道了。\x02\x03",
            "如果顺利地被招待入城的话，\x01",
            "也打听一下这方面的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F为了这个，\x01",
            "明天的比赛说什么也要取胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764F嗯……\x01",
            "虽然可能会有点危险。\x02\x03",
            "把这个给你们吧。\x02",
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
            "地下水路的钥匙Ｂ\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x36E, 1)

    ChrTalk(
        0x101,
        "#004F哎，这个是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F是王都支部管理的\x01",
            "地下水路钥匙的其中一把。\x02\x03",
            "用这把钥匙可以打开\x01",
            "王立竞技场旁边的地下水路入口。\x02\x03",
            "不过，进入那边的区域之后，\x01",
            "可能会遇到相当强大的魔兽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F这正是我想要的！\x02\x03",
            "和那些家伙战斗之前，\x01",
            "能再锻炼一下实在是很必要呢！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F艾南先生，\x01",
            "实在是太感谢您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F没什么，这也是身为负责人的工作。\x02\x03",
            "不过，如果只有你们两人，\x01",
            "记住一定不要贸然进去哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F知道啦。\x02\x03",
            "明天早上和金先生他们会合之后\x01",
            "再进去里面看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    NewScene("ED6_DT01/T4150   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_9416")

    label("loc_6A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_743F")
    EventBegin(0x0)
    OP_A2(0x61F)
    OP_28(0x47, 0x1, 0x200)
    Fade(1000)
    OP_6D(-4030, 0, 1100, 0)
    SetChrPos(0x101, -2590, 0, 280, 270)
    SetChrPos(0x102, -2590, 0, 1220, 270)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 90, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#761F啊，你们回来了。\x01",
            "艾丝蒂尔、约修亚。\x02\x03",
            "恭喜你们通过第一场比赛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嘿嘿，过奖过奖。\x02\x03",
            "#501F对了，艾南哥哥。\x01",
            "你都知道比赛结果了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F刚才克鲁茨他们回来的时候，\x01",
            "已经告诉我了。\x02\x03",
            "那么……\x01",
            "怎么样，感觉不错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这个嘛……\x02\x03",
            "不只是前辈他们，\x01",
            "晋级的队伍也都是强敌呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们说明了关于空贼和特务兵小组的事情。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#762F原来如此……\x01",
            "我倒是听说过那些空贼被允许参赛。\x01",
            "　\x02\x03",
            "可是没想到特务部队的队长那么厉害啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F普通的队员就很厉害了，\x01",
            "不过和那个队长完全不能相提并论。\x02\x03",
            "#002F拥有单手举起巨剑的臂力，\x01",
            "还有像豹子一样敏捷的身手……\x02\x03",
            "虽然早就知道他不是一般人，\x01",
            "不过真没想到会强到那种程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F是啊……\x02\x03",
            "#012F那个，艾南先生。\x02\x03",
            "关于那个洛伦斯少尉的经历，\x01",
            "你知不知道些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#765F嗯，真是遗憾，\x01",
            "他的事情我也不知道。\x02\x03",
            "情报部是新设立的部队，\x01",
            "成员都是在理查德上校升职时候\x01",
            "从各个部队选拔出来的精英。\x02\x03",
            "他也应该是其中一人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F是、是吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F#6P喂喂，约修亚……\x02\x03",
            "你好像很关心那个红头怪嘛。\x01",
            "　\x02\x03",
            "有什么……你很在意的事情吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#2P不，很显然他不是个简单的人物。\x01",
            "　\x02\x03",
            "因为很可能和他交手，\x01",
            "所以要知道对方详细的战斗力才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#6P哦……是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F说起来，还有件事要告诉你们，\x01",
            "虽然和那个洛伦斯少尉无关……\x02\x03",
            "就在今天中午，\x01",
            "一艘军用警备飞艇到达了王都的空港。\x02\x03",
            "从警备飞艇上面走下来的是\x01",
            "上校的副官凯诺娜上尉。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x102,
        "#014F这个是值得注意的情报哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F凯诺娜上尉……\x01",
            "就是那个阴险的母狐狸嘛。\x02\x03",
            "利用提妲、威胁博士的讨厌婆娘。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F那个警备飞艇，\x01",
            "好像在五大都市都去过一遍呢。\x02\x03",
            "强行在空港着陆，\x01",
            "让定期船的出发时间都不得不推迟。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F真是没有好事啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F五大都市都到过吗。\x02\x03",
            "就算要搜捕博士他们，\x01",
            "这样的范围也似乎太大了点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F现在，各地的支部正在调查这件事。\x01",
            "　\x02\x03",
            "如果知道什么消息的话会立刻联系我们的。\x02\x03",
            "你们就不用担心太多了，\x01",
            "安心地继续参加武术大会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，说的也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么，我们告辞了。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_9416")

    label("loc_743F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7778")
    OP_A2(0x60A)

    ChrTalk(
        0x101,
        "#004F啊，对了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#501F我说约修亚，\x01",
            "科洛丝不是也会来王都这里吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F她确实说过在诞辰庆典之前\x01",
            "要回王都这里的。\x02\x03",
            "也许已经来了也说不定。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_754F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_754F)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#006F艾南哥哥，我想问一下。\x02\x03",
            "有一个叫做科洛丝的女孩子来过这里吗？\x01",
            "她和我们年纪差不多。\x01",
            "  \x02\x03",
            "我们约好在王都见面的……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#763F是叫科洛丝吗？\x02\x03",
            "没有，\x01",
            "并没有你所说的女孩子来过这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F是吗……\x02\x03",
            "#505F对了，\x01",
            "当时没有详细地问她会在哪里落脚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F她好像说过\x01",
            "会在富裕的亲戚家住下来……\x02\x03",
            "不过单凭这一点来寻找，\x01",
            "似乎有点太过勉强了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F既然约好了，\x01",
            "就肯定会取得联络的。\x02\x03",
            "一旦有了消息，\x01",
            "我会立刻告知你们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9416")

    label("loc_7778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E0A")
    OP_A2(0x6FD)

    ChrTalk(
        0x8,
        (
            "#762F对了，虽然在诞辰庆典\x01",
            "说这些不合时宜的话有些煞风景……\x02\x03",
            "不过与『杰斯塔猎兵团』\x01",
            "相关的情报终于收集到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F『杰斯塔猎兵团』？\x01",
            "那个好像是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是洛伦斯少尉在加入情报部之前\x01",
            "所属的佣兵部队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762F嗯……\x02\x03",
            "那是一个以埃雷波尼亚周边的自治州\x01",
            "为主要活动范围的部队。\x02\x03",
            "『猎兵团』这个名字与他们非常相称，\x01",
            "既拥有实力又有显赫的战绩……\x02\x03",
            "大约半年前，在毫无先兆的情况下，\x01",
            "整个部队突然间行踪不明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F整个部队行踪不明！？\x02\x03",
            "这么说……\x01",
            "是因为在战场上打了败仗吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#765F不，那个时候，\x01",
            "他们完全没有到任何地方\x01",
            "展开任何战斗的迹象。\x02\x03",
            "像这种情况，\x01",
            "超过百人的集团忽然之间消失得无影无踪，\x01",
            "就连他们的同行也百思不得其解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F总、总感觉好可怕呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F………………………………\x02\x03",
            "#015F就在那时，\x01",
            "洛伦斯少尉正好加入了情报部。\x02\x03",
            "#012F这两者之间有什么关联吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764F与之相关的情况正在调查当中。\x02\x03",
            "说不定王国军方面会获得什么情报。\x01",
            "　\x02\x03",
            "#760F对了，还有一个不合时宜的事情。\x02\x03",
            "埃雷波尼亚皇族答应过\x01",
            "要来参加诞辰庆典的约定，\x01",
            "最终还是没有兑现。\x02\x03",
            "和往年一样，\x01",
            "只有帝国的大使出席了庆典仪式。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F唔～是这样啊。\x02\x03",
            "对了，那个皇族\x01",
            "就是科洛丝的婚约对象吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，那是杜南公爵\x01",
            "打算在继承王位之后安排的婚约。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F结果那个婚约在询问了\x01",
            "女王陛下的意见之后决定取消了。\x02\x03",
            "皇族取消访问大概也是因为这个缘故吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EBC")

    label("loc_7E0A")


    ChrTalk(
        0x8,
        (
            "#760F诞辰庆典的警备工作\x01",
            "都交给王国军来负责了，\x01",
            "大家应该都在街上自由自在地游玩。\x02\x03",
            "我想在酒廊、小店还有酒店这些地方\x01",
            "就能找到他们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EBC")

    Jump("loc_808F")

    label("loc_7EBF")

    OP_A2(0x6FC)

    ChrTalk(
        0x8,
        (
            "#760F哎呀呀，\x01",
            "艾丝蒂尔和约修亚……\x02\x03",
            "今天基本上没有什么任务呢。\x01",
            "　\x02\x03",
            "#761F不用顾虑，\x01",
            "好好地享受约会的快乐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F约、约、约会，\x01",
            "不是那样的啦！\x02\x03",
            "不过再过一段时间大概就能这么说了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F啊哈，哈哈哈……\x01",
            "没、没什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F诞辰庆典的警备工作\x01",
            "都交给王国军来负责了，\x01",
            "大家应该都在街上自由自在地游玩。\x02\x03",
            "我想在酒廊、小店还有酒店这些地方\x01",
            "就能找到他们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_808F")

    Jump("loc_9416")

    label("loc_8092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_827F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8172")

    ChrTalk(
        0x8,
        (
            "#762F科洛蒂娅公主的委托情况\x01",
            "我已经从亲卫队那里了解到了。\x02\x03",
            "#760F这边不会有问题的。\x01",
            "就算王国军跑来询问，\x01",
            "我们也会装作不知情的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_827C")

    label("loc_8172")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#762F约修亚，还有金先生，\x01",
            "你们平安无事可真是太好了。\x02\x03",
            "科洛蒂娅公主的委托情况\x01",
            "我已经从亲卫队那里了解到了。\x02\x03",
            "#760F这边不会有问题的。\x01",
            "就算王国军跑来询问，\x01",
            "我们也会装作不知情的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_827C")

    Jump("loc_9416")

    label("loc_827F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_8481")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8345")

    ChrTalk(
        0x8,
        (
            "#760F游击士已经全部到齐了。\x02\x03",
            "接下来要是还能联系到\x01",
            "亲卫队以及熟识的记者就好了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_847E")

    label("loc_8345")


    ChrTalk(
        0x8,
        (
            "#760F在王都的其余游击士有克鲁茨、\x01",
            "库拉茨、卡露娜和亚妮拉丝这四位。\x01",
            "　\x02\x03",
            "在酒廊、一般的商店，\x01",
            "或者酒店里都可以见到他们。\x02\x03",
            "找到的话，就叫他们到这里来集合吧。\x01",
            "　\x02\x03",
            "如果要是还能联系到\x01",
            "亲卫队以及熟识的记者就好了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_847E")

    Jump("loc_9416")

    label("loc_8481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_87CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_84EA")

    ChrTalk(
        0x8,
        (
            "#760F今天很累了吧。\x01",
            "晚宴的事，就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87CC")

    label("loc_84EA")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#761F我听大家说了，\x01",
            "恭喜你们取得优胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F谢谢你，艾南哥哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F我听克鲁茨他们说，\x01",
            "决赛好像非常激烈哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F是呢……\x02\x03",
            "下次再和他们战斗的话，\x01",
            "就不知能不能赢了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F嗯，\x01",
            "肯定不再是那么简单的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761F哈哈，胜负有时要靠运气，\x01",
            "但引导你们取得胜利的是\x01",
            "你们自身的实力啊。\x02\x03",
            "而且，\x01",
            "你们以后还会继续成长的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，谢谢你的鼓励，\x01",
            "我们会更加努力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F今天很累了吧。\x01",
            "晚宴的事，就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯！交给我们吧！\x02",
    )

    CloseMessageWindow()

    label("loc_87CC")

    Jump("loc_9416")

    label("loc_87CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_889C")

    ChrTalk(
        0x8,
        (
            "#760F昨天你们有没有\x01",
            "到我所说的地下水路看一下呢？\x02\x03",
            "我觉得对现在的你们来说，\x01",
            "那里会是一个非常理想的锻炼场所。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8980")

    label("loc_889C")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#760F早上好啊，各位。\x01",
            "今天终于到总决赛了。\x02\x03",
            "昨天你们有没有\x01",
            "到我所说的地下水路看一下呢？\x02\x03",
            "我觉得对现在的你们来说，\x01",
            "那里会是一个非常理想的锻炼场所。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8980")

    Jump("loc_9416")

    label("loc_8983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_END)), "loc_8ABE")

    ChrTalk(
        0x8,
        (
            "#760F给你们的那把钥匙可以打开\x01",
            "竞技场旁边的地下水路入口。\x01",
            "　\x02\x03",
            "不过，进入那边的区域\x01",
            "可能会遇到相当强大的魔兽。\x02\x03",
            "如果只有你们两人，\x01",
            "记住一定不要贸然进去哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9416")

    label("loc_8ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_8F0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E8B")
    OP_A2(0x6FA)

    ChrTalk(
        0x8,
        (
            "#761F艾丝蒂尔、约修亚。\x01",
            "听说你们顺利地进入决赛了呢。\x02\x03",
            "虽然对克鲁茨他们来说有点遗憾，\x01",
            "不过听说比赛打得很精彩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，真是白热化的战斗呢。\x02\x03",
            "#007F不过，和各位前辈比起来，\x01",
            "我们的实力还需要有待提高呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F说得没错。\x02\x03",
            "金先生就不用说了，\x01",
            "奥利维尔的枪法和魔法也帮了很大的忙。\x01",
            "　\x02\x03",
            "我们以后还要加倍努力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761F呵呵，有这种上进的意识，\x01",
            "我想你们一定会不断地进步的。\x02\x03",
            "#760F对了，\x01",
            "今天有没有打听到什么事情呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F其实，我们拜托了\x01",
            "《利贝尔通讯》的记者帮忙收集情报。\x02\x03",
            "现在准备去看看情况……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#763F《利贝尔通讯》吗……\x01",
            "那真是太好了。\x02\x03",
            "#761F我知道了。\x01",
            "期待你们的好消息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F08")

    label("loc_8E8B")


    ChrTalk(
        0x8,
        (
            "#763F《利贝尔通讯》吗……\x01",
            "那真是太好了。\x02\x03",
            "#761F我知道了。\x01",
            "期待你们的好消息。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F08")

    Jump("loc_9416")

    label("loc_8F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8F8B")

    ChrTalk(
        0x8,
        (
            "#760F从今天开始，不管对手是谁，\x01",
            "应该都不是那么好对付的吧。\x02\x03",
            "要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9044")

    label("loc_8F8B")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#760F早上好啊，各位。\x02\x03",
            "怎么样，\x01",
            "行装都整理好了吗？\x02\x03",
            "从今天开始，不管对手是谁，\x01",
            "应该都不是那么好对付的吧。\x02\x03",
            "要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9044")

    Jump("loc_9416")

    label("loc_9047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_90E1")

    ChrTalk(
        0x8,
        (
            "#760F凯诺娜上尉的活动情况\x01",
            "现在正由各支部在进行追踪。\x02\x03",
            "你们就不用管了，\x01",
            "专心地参加武术大会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9416")

    label("loc_90E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_92B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9179")

    ChrTalk(
        0x8,
        (
            "#760F比赛应该是在下午开始，\x01",
            "所以不用这么着急。\x02\x03",
            "在大街上稍微放松一下\x01",
            "也许是个不错的选择。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92B3")

    label("loc_9179")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#760F早上好啊，各位。\x01",
            "今天是第一回合的比赛。\x02\x03",
            "现在王都的周边是由\x01",
            "军队负责警备的工作，\x01",
            "所以给协会的委托就少了。\x02\x03",
            "各位只要专心为大会\x01",
            "做好准备就可以了。\x02\x03",
            "比赛要下午才开始，\x01",
            "所以各位现在不用着急。\x02\x03",
            "在大街上稍微放松一下\x01",
            "也许是个不错的选择。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92B3")

    Jump("loc_9416")

    label("loc_92B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_93B6")

    ChrTalk(
        0x8,
        (
            "#760F金先生在王都的住所\x01",
            "是东街区的卡尔瓦德共和国大使馆。\x02\x03",
            "他平常会呆在酒廊里面，\x01",
            "你们最好也去那里看看。\x01",
            "　\x02\x03",
            "从北边的小路过去就能找到酒廊了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9416")

    label("loc_93B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_9416")

    ChrTalk(
        0x8,
        (
            "#760F想要去王城的话，\x01",
            "沿着大街一直往北走就到了。\x02\x03",
            "总之，\x01",
            "收集情报的时候请一定要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9416")

    TalkEnd(0x8)
    Return()

    # Function_12_2E09 end

    def Function_13_941A(): pass

    label("Function_13_941A")

    EventBegin(0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xC, -2590, 0, 1600, 270)
    SetChrPos(0x9, -1500, 0, 770, 270)
    SetChrPos(0xB, -1770, 0, -310, 270)
    SetChrPos(0xA, -2590, 0, -610, 270)
    OP_4A(0xC, 255)
    OP_4A(0x9, 255)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    OP_4A(0x8, 255)
    OP_6D(-4030, 0, 1100, 0)
    OP_6B(2800, 0)
    SetChrPos(0x101, 30, -250, -4920, 315)
    SetChrPos(0x102, 1120, -250, -4920, 315)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#760F那么，祝你们胜利。\x02\x03",
            "实际上，如果是你们的话，\x01",
            "比赛肯定可以轻松通过的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#821F嘿嘿，你很清楚嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#830F一旦出场，\x01",
            "就要全力以赴哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#850F没错！\x01",
            "绝对不能输给军队那些人！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#840F那么……\x01",
            "差不多该出发了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#840F……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    def lambda_964A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_964A)

    def lambda_9658():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9658)

    def lambda_9666():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9666)

    def lambda_9674():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9674)

    def lambda_9682():

        label("loc_9682")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_9682")

    QueueWorkItem2(0x101, 1, lambda_9682)

    def lambda_9693():

        label("loc_9693")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_9693")

    QueueWorkItem2(0x102, 1, lambda_9693)

    def lambda_96A4():
        OP_8E(0xFE, 0xFFFFF97A, 0x0, 0xFFFFF7FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_96A4)

    def lambda_96BF():
        OP_8E(0xFE, 0xFFFFFDC6, 0x0, 0xFFFFF8E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_96BF)
    OP_6D(-2770, 0, 100, 2000)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        "#008F啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x102,
        "#010F抱歉，打扰了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0x9, 0xFFFFFEE8, 0x0, 0xFFFFFE3E, 0xBB8, 0x0)
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "#831F#2P你们……\x01",
            "不是艾丝蒂尔和约修亚嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_979A():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_979A)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        (
            "#501F啊……\x01",
            "你是卢安支部的卡露娜姐姐！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_END)), "loc_9868")

    ChrTalk(
        0xB,
        (
            "#820F#2P说起来，在空贼作乱的时候，\x01",
            "我们在柏斯曾经见过一面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#850F#1P我记得……\x01",
            "你们是和雪拉前辈在一起的新人吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E5")

    label("loc_9868")


    ChrTalk(
        0xB,
        (
            "#820F#2P说起来，在空贼作乱的时候，\x01",
            "我们在柏斯曾经见过一面呢。\x02\x03",
            "#2P我记得……\x01",
            "你们是和雪拉扎德在一起的新人吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98E5")


    ChrTalk(
        0x102,
        (
            "#010F嗯，很久不见了。\x02\x03",
            "不过请问一下，\x01",
            "为什么大家都集中在王都呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F关于这个问题，\x01",
            "就让我来说明一下吧。\x02\x03",
            "各位如果不快点去的话，\x01",
            "可能会赶不上准备哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#830F#2P哦，说的也是……\x02\x03",
            "#2P不好意思，你们两个，\x01",
            "要说的话过后再谈吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0xE)

    ChrTalk(
        0xB,
        (
            "#820F#2P那么，\x01",
            "我们也告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x0, 0xE)

    ChrTalk(
        0xA,
        "#811F#1P待会儿见，两位新人！\x02",
    )

    CloseMessageWindow()
    OP_43(0xA, 0x1, 0x0, 0xE)

    ChrTalk(
        0xC,
        "#840F……告辞了。\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x1, 0x0, 0xE)

    def lambda_9A37():

        label("loc_9A37")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_9A37")

    QueueWorkItem2(0x101, 1, lambda_9A37)

    def lambda_9A48():

        label("loc_9A48")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_9A48")

    QueueWorkItem2(0x102, 1, lambda_9A48)

    def lambda_9A59():

        label("loc_9A59")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_9A59")

    QueueWorkItem2(0x8, 1, lambda_9A59)
    WaitChrThread(0xC, 0x1)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    Sleep(700)

    ChrTalk(
        0x101,
        (
            "#004F啊～单单有这几位游击士聚在一起，\x01",
            "就感觉很壮观很气派呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊……\x01",
            "每个人都很身手不凡呢。\x02\x03",
            "刚才你们说到出场，\x01",
            "难道是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761F嗯，你想得没错。\x02\x03",
            "他们现在正要出席武术大会的预选赛。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F哎～～～\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x8, 400)

    def lambda_9BF6():
        OP_6D(-4030, 0, 1100, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9BF6)

    def lambda_9C0E():
        OP_8E(0xFE, 0xFFFFF5E2, 0x0, 0x118, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9C0E)

    def lambda_9C29():

        label("loc_9C29")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_9C29")

    QueueWorkItem2(0x101, 1, lambda_9C29)
    TurnDirection(0x102, 0x8, 400)
    OP_8E(0x102, 0xFFFFF95C, 0x0, 0x474, 0xBB8, 0x0)

    def lambda_9C55():
        OP_8E(0xFE, 0xFFFFF5E2, 0x0, 0x4C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9C55)

    def lambda_9C70():

        label("loc_9C70")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_9C70")

    QueueWorkItem2(0x102, 1, lambda_9C70)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#008F对、对不起！\x02\x03",
            "我是从蔡斯支部来的准游击士\x01",
            "艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F和她一样，我是约修亚·布莱特。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F我是艾南，\x01",
            "是格兰赛尔支部的负责人。\x02\x03",
            "之前我收到了雾香的联络，\x01",
            "所以知道你们今天会来的。\x02\x03",
            "趁现在赶快把转属手续办了吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#761F好，可以了。\x02\x03",
            "欢迎来到游击士协会格兰赛尔支部。\x01",
            "　\x02\x03",
            "#760F就我个人来说，\x01",
            "可是很期待你们的到来呢。\x02\x03",
            "我记得，\x01",
            "你们是卡西乌斯先生的孩子吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊～嗯，是的……\x02\x03",
            "艾南哥哥，你也和老爸认识吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F是啊，我以前研修的时候\x01",
            "也经常受到卡西乌斯先生的照顾呢。\x02\x03",
            "我听说，\x01",
            "他出去旅行一直没有回来是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯……\x02\x03",
            "虽然曾经写信说他暂时不会回来……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F但是……\x01",
            "完全没有提到具体去了哪里。\x02\x03",
            "我们从洛连特到蔡斯各个城市走了一遍，\x01",
            "也没有打听到父亲的消息。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762F嗯，听你们这样说的话，\x01",
            "他不在国内的可能性就很高了。\x02\x03",
            "#764F不过还真是麻烦啊……\x02\x03",
            "现在由于军队对恐怖事件实行的对策，\x01",
            "王都的游击士的活动受到了很大的限制。\x01",
            "　\x02\x03",
            "如果作为原军人的卡西乌斯先生在的话，\x01",
            "说不定他会知道现在的王国军里\x01",
            "到底发生了什么事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#763F哎……你们怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯，实际上……\x02\x03",
            "其中的内幕我们两个就知道呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#763F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F连同蔡斯地区发生的事情，\x01",
            "这就一并向您报告吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚向艾南说明了\x01",
            "在雷斯顿要塞得知的事情\x01",
            "以及拉赛尔博士的委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#763F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎……\x01",
            "艾南哥哥，你没事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762F没、没什么……\x01",
            "突然听到这么重大的事情，脑子一片空白。\x02\x03",
            "理查德上校控制了王国军队……\x01",
            "　\x02\x03",
            "情报部特殊部队导演的恐怖事件……\x01",
            "　\x02\x03",
            "真是一时让人无法相信啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F可、可是这是真的啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F问问蔡斯支部的雾香小姐，\x01",
            "我想您就可以知道得更清楚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764F没关系，\x01",
            "我并不是在怀疑你们说的话……\x02\x03",
            "正相反，听了这些话，\x01",
            "我心中的谜团终于找到答案了。\x02\x03",
            "#762F不过话说回来，\x01",
            "理查德上校在王都拥有极高的人望……\x02\x03",
            "不怕被你们笑话，在听你们说这件事之前，\x01",
            "我也对他很有好感呢。\x02\x03",
            "而且，普通的市民对上校的阴谋，\x01",
            "是做梦也都想不到的吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F果然是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F不愧是情报部，\x01",
            "操纵情报的手法真是滴水不漏啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762F游击士协会从原则上来说，\x01",
            "是不能干涉军队内政的……\x01",
            "但是，这也不代表我们就此袖手旁观。\x02\x03",
            "总而言之，\x01",
            "请你们先按照预定的计划，\x01",
            "完成拉赛尔博士的委托吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F当然，我们正打算这么做呢。\x02\x03",
            "不过问题是，\x01",
            "怎么样才能见到女王呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764F是啊……\x02\x03",
            "普通情况下，有游击士协会的介绍信，\x01",
            "就可以直接晋见女王了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎，是吗！？\x02\x03",
            "#001F什么呀～⊙\x01",
            "刚才真是白让我担心了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F#2P艾丝蒂尔……\x01",
            "我觉得事情没这么简单。\x02\x03",
            "不管怎么说，\x01",
            "守城的亲卫队都被当成恐怖分子了。\x02\x03",
            "#012F你知道这意味着什么吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#505F#6P哎，你是说……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "「王城的警卫会变少？」\x01",      # 0
            "「女王本人会有危险？」\x01",      # 1
            "「会把介绍信拦下来？」\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AA8A"),
        (1, "loc_AC4C"),
        (2, "loc_AE16"),
        (SWITCH_DEFAULT, "loc_AFBE"),
    )


    label("loc_AA8A")


    ChrTalk(
        0x102,
        (
            "#015F#2P不，正好相反。\x01",
            "警备会变得更加森严呢。\x02\x03",
            "#012F也就是说，和雷斯顿要塞一样，\x01",
            "王城在理查德上校控制下的可能性很高。\x01",
            "　\x02\x03",
            "就算有游击士协会的介绍信，\x01",
            "我想也会被他们拦下来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#6P什、什么！？\x02\x03",
            "那样的话，\x01",
            "到底该怎么才能和女王会面呢！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P像在雷斯顿要塞那样，\x01",
            "潜入王城的做法虽然可行……\x02\x03",
            "但再次用同样的手法，\x01",
            "应该不会那么简单就成功吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFBE")

    label("loc_AC4C")


    ChrTalk(
        0x102,
        (
            "#012F#2P这种可能性也有……\x02\x03",
            "比起这个，和雷斯顿要塞一样，\x01",
            "王城在理查德上校控制下的可能性很高。\x01",
            "　\x02\x03",
            "就算有游击士协会的介绍信，\x01",
            "我想也会被他们拦下来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#6P什、什么！？\x02\x03",
            "那样的话，\x01",
            "到底该怎么才能和女王会面呢！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P像在雷斯顿要塞那样，\x01",
            "潜入王城的做法虽然可行……\x02\x03",
            "但再次用同样的手法，\x01",
            "应该不会那么简单就成功吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFBE")

    label("loc_AE16")


    ChrTalk(
        0x102,
        (
            "#012F#2P嗯，很有可能。\x02\x03",
            "和雷斯顿要塞一样，\x01",
            "王城在理查德上校控制下的可能性很高。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6P呜呜，果然是这样吗……\x02\x03",
            "还是不能这么简单就见到女王啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P像在雷斯顿要塞那样，\x01",
            "潜入王城的做法虽然可行……\x02\x03",
            "但再次用同样的手法，\x01",
            "应该不会那么简单就成功吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x45, 0x1)
    Jump("loc_AFBE")

    label("loc_AFBE")


    ChrTalk(
        0x101,
        (
            "#007F#6P嗯……\x02\x03",
            "#006F在这里想也没用，\x01",
            "总之先去城那边看看吧？\x02\x03",
            "运气好的话，\x01",
            "说不定能从门卫那里得到什么情报呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#2P这样倒是没什么问题……\x01",
            "不过行动的时候还是要注意一点。\x02\x03",
            "我们想要和女王陛下会面的事情，\x01",
            "最好还是不要说出来。\x01",
            "　\x02\x03",
            "万一被理查德上校知道了，\x01",
            "我们的计划很有可能会暴露出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6P啊，原来是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F确实如此，\x01",
            "最好连其他的游击士也瞒着。\x02\x03",
            "顺便告诉你们，\x01",
            "沿着大街一直往北走就到王城了。\x02\x03",
            "总之，\x01",
            "收集情报的时候请一定要小心。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B282():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B282)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#006F我知道了，艾南哥哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F打听到什么会立刻回来报告的。\x02",
    )

    CloseMessageWindow()
    OP_28(0x45, 0x1, 0x80)
    OP_28(0x45, 0x1, 0x100)
    OP_44(0x8, 0x1)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_13_941A end

    def Function_14_B2F8(): pass

    label("Function_14_B2F8")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x42E, 0x0, 0xFFFFFAE2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFFF4C, 0xFFFFFF06, 0xFFFFE8C2, 0xBB8, 0x0)

    def lambda_B32B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_B32B)
    OP_8E(0xFE, 0xFFFFFF92, 0xFFFFFF06, 0xFFFFE43A, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_B2F8 end

    def Function_15_B351(): pass

    label("Function_15_B351")

    EventBegin(0x0)
    OP_6D(-4030, 0, 1100, 0)
    SetChrPos(0x101, -2590, 0, 280, 270)
    SetChrPos(0x102, -2590, 0, 1220, 270)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#760F没错，金先生曾经拜托过我\x01",
            "寻找能够协助他战斗的游击士。\x02\x03",
            "不过你们有博士的委托在身，\x01",
            "所以没有特地介绍给他……\x02\x03",
            "#761F没想到因为杜南公爵的一时兴起，\x01",
            "委托和大会重合在一起了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嘿嘿，从结果上来看，\x01",
            "公爵的任性反而帮了我们大忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F参加武术大会……\x01",
            "艾南先生您觉得怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F是啊……\x01",
            "要把所有可能的方法都试一遍，\x01",
            "我觉得这也很有尝试的价值。\x02\x03",
            "如果克鲁茨他们赢了，\x01",
            "到时候再拜托他们也可以。\x02\x03",
            "不管怎样，\x01",
            "你们就尽全力试着挑战一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F太好了，就这样吧！\x02\x03",
            "#006F艾南哥哥，\x01",
            "赶快告诉我们金先生现在在哪里吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F平常的话，\x01",
            "应该都呆在这座建筑旁边的酒廊里。\x02\x03",
            "顺带说一下，\x01",
            "他在王都的住所是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F原来是这样啊，\x01",
            "是金先生祖国的大使馆啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#2P共和国大使馆和竞技场一样在东街区。\x01",
            "　\x02\x03",
            "另外，\x01",
            "我们最好也去酒廊看看吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006F#3P嗯，ＯＫ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#763F啊，对了……\x02\x03",
            "你们两个在王都的这段时间里\x01",
            "打算住在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B890():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B890)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#505F嗯～\x01",
            "我想应该会在酒店吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我记得王国最大的酒店是在北街区吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F对。\x01",
            "叫做罗恩鲍姆酒店。\x02\x03",
            "如果没有问题的话，\x01",
            "我就帮你们向酒店预约房间吧？\x02\x03",
            "费用由王都支部承担。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎，这样好吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F为了我们准备得这么周到……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F就当作和博士的委托有关的必要经费吧。\x01",
            "　\x02\x03",
            "这也是我力所能及的事情……\x01",
            "没帮上忙，真是对不住你们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F没有的事，已经帮了很大忙了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这样的话……\x01",
            "我们就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761F就这样定了，\x01",
            "那么我这就去预约房间哦。\x02\x03",
            "傍晚之后去酒店的前台说出自己的名字，\x01",
            "他们就会给你们安排房间了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x611)
    OP_28(0x46, 0x4, 0x2)
    OP_28(0x46, 0x4, 0x4)
    OP_28(0x46, 0x1, 0x1)
    OP_28(0x46, 0x1, 0x2)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_15_B351 end

    def Function_16_BB74(): pass

    label("Function_16_BB74")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_6D(-1330, 0, 750, 0)
    SetChrPos(0x101, -2590, 0, 280, 270)
    SetChrPos(0x102, -2590, 0, 1220, 270)
    SetChrPos(0x108, -1500, 0, 750, 270)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 90, 0)
    OP_A2(0x649)
    OP_28(0x4B, 0x4, 0x2)
    OP_28(0x4B, 0x4, 0x4)
    OP_28(0x4B, 0x1, 0x1)
    OP_28(0x4B, 0x1, 0x2)
    OP_28(0x4B, 0x1, 0x4)
    OP_28(0x4B, 0x1, 0x8)
    FadeToBright(2000, 0)
    OP_6D(-3330, 0, 750, 2000)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#764F我明白当前的状况了……\x02\x03",
            "#760F艾丝蒂尔、约修亚。\x01",
            "你们两个做得非常出色。\x02\x03",
            "竟然可以接受女王陛下的直接委托……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊哈哈，只是运气好啦。\x02\x03",
            "#007F但是，从现在开始\x01",
            "可能就没有那么好的运气了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F嗯……\x01",
            "但绝对不能放弃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761F既然你们都下了决心，\x01",
            "我也就没有什么要说的了。\x02\x03",
            "总之，拉赛尔博士的委托已经达成了。\x01",
            "　\x02\x03",
            "这些钱你们今后可能用得上，\x01",
            "我这就把报酬交给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x45, 0x4, 0x10)
    Sleep(100)
    OP_AF(0x63, 0x45)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x46, 0x4, 0x10)
    OP_28(0x47, 0x4, 0x10)
    OP_28(0x48, 0x4, 0x10)
    OP_28(0x49, 0x4, 0x10)
    OP_28(0x4A, 0x4, 0x10)
    OP_28(0x46, 0x4, 0x20)
    OP_28(0x47, 0x4, 0x20)
    OP_28(0x48, 0x4, 0x20)
    OP_28(0x49, 0x4, 0x20)
    OP_28(0x4A, 0x4, 0x20)

    ChrTalk(
        0x8,
        (
            "#760F那么，接下来……金先生。\x02\x03",
            "卡西乌斯先生能够把你找来，\x01",
            "对于我们而言真是幸运啊。\x02\x03",
            "用你那身为Ａ级游击士的实力\x01",
            "来全力帮助我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F啊，当然。\x02\x03",
            "这可是报答大人恩德的良机，\x01",
            "这样的大事我怎能放任不管呢。\x02\x03",
            "我会一直帮忙到底的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BFE4():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BFE4)
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        (
            "#001F#5P不愧是金大哥，够爽快！\x02\x03",
            "#501F对了……什么叫做Ａ级呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#2P衡量正游击士实力的级别标准。\x01",
            "　\x02\x03",
            "从最低的Ｇ级开始到Ａ级为止，\x01",
            "共分为七个级别。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#5P那、那么说Ａ级不就是最高的级别了吗？\x01",
            "　\x02\x03",
            "金大哥……\x01",
            "竟然是这么厉害的游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈，我啊，\x01",
            "只是处于Ａ级中下游的水平罢了。\x02\x03",
            "#074F而且从整个大陆来说，\x01",
            "Ａ级游击士一共２０人左右……\x02\x03",
            "在其之上，\x01",
            "其实还有不公开的Ｓ级那样的级别。\x02\x03",
            "是解决了国家的重大事件的游击士\x01",
            "才能获得的特级游击士称号。\x02\x03",
            "#070F整个大陆一共只有四人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#5P那、那样的人究竟厉害到什么程度，\x01",
            "简直完全无法想象啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#075F呼，不管怎么说，\x01",
            "你们也不该不知道啊……\x02\x03",
            "#070F因为其中之一就是卡西乌斯大人啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F#5P#3S什么～～～～！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#009F难、难道说……\x01",
            "约修亚你又是已经知道了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P对不起，其实我是知道的。\x02\x03",
            "#010F因为父亲成功解决了\x01",
            "五年前发生在共和国的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F哈啊，又来一个……\x01",
            "我算是彻底地服这个老爸了。\x02\x03",
            "王国军的上校啦、幕后英雄啦、\x01",
            "剑圣啦、Ｓ级游击士啦……\x02\x03",
            "#509F既然老爸这么厉害无比，\x01",
            "怎么还不快点回利贝尔，\x01",
            "把这次的事件通通给解决掉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈，你说得也许没错。\x02\x03",
            "如果大人一开始就在这里的话，\x01",
            "肯定会在这个事件发展成为\x01",
            "政变之前将其阻止的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F约修亚，你怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P……事情有一些奇怪。\x02\x03",
            "这一连串的事件\x01",
            "都是在父亲外出旅行时发生的。\x02\x03",
            "#012F难道他们早就瞄准了父亲外出的机会\x01",
            "来制造这起政变吗……\x02\x03",
            "我有这样的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F唔，大人前往帝国也是\x01",
            "这次政变的其中一个环节……\x02\x03",
            "就是这个意思对吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x108, 400)

    ChrTalk(
        0x102,
        (
            "#010F#2P……不。\x01",
            "是我有些多虑了吧。\x02\x03",
            "那么强的父亲，被人不知不觉\x01",
            "就下套的可能性几乎是没有的……\x02\x03",
            "#013F除非存在那种可以掌握父亲的行动、\x01",
            "并且可以将计就计的人物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F唔～的确有可能。\x02\x03",
            "好比说我吧，如果有人潜伏在我的附近，\x01",
            "我是不会那么容易察觉的哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F不过，要想钻大人的空子，\x01",
            "那个理查德上校是不可能做到的。\x02\x03",
            "多半这两个重大的事件偶然产生了重叠吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764F不管怎么说，要想借助作为顶梁柱的\x01",
            "卡西乌斯先生的力量看来是不行了。\x02\x03",
            "#762F因此，我决定了。\x02\x03",
            "游击士协会·王都支部\x01",
            "现在开始采取紧急应对制度。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CB16():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CB16)

    def lambda_CB24():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CB24)
    TurnDirection(0x108, 0x8, 400)

    ChrTalk(
        0x101,
        "#004F紧、紧急应对制度……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F怎么说这也是女王陛下的直接委托。\x01",
            "　\x02\x03",
            "协会规约第三项——\x01",
            "『不对国家主权进行干涉』的桎梏\x01",
            "在这个紧要关头就解除掉了……\x02\x03",
            "尽管如此，协会和王国军的战斗力\x01",
            "在根本上还是有很大的差距的。\x02\x03",
            "不止是金先生，\x01",
            "在王都的其余所有游击士\x01",
            "也都要来助一臂之力才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F原来是这样啊……\x02\x03",
            "的确，要和情报部对峙的话，\x01",
            "还需要集结更多的战斗力才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#765F可以的话，\x01",
            "最好能取得国内其他支部的协助……\x02\x03",
            "可是现在所有地区的关所和飞艇坪\x01",
            "都已经被王国军完全封锁了。\x02\x03",
            "以针对恐怖分子的名义。\x02",
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
        "#012F实质上是一道戒严令……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F敌人的行动也终于开始正式化了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762F我想，恐怕是打算封锁\x01",
            "潜伏中的亲卫队和我们的行动吧。\x02\x03",
            "要想救出人质，\x01",
            "手中没有充足的战斗力是不行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F说白了就是只要有实力，\x01",
            "然后就是勇往直前不怕挑战对吧！\x02\x03",
            "对了，人质被囚禁的地方，\x01",
            "有没有什么大致的线索呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764F是啊，我刚才已经想了许多……\x01",
            "　\x02\x03",
            "#762F最有可能的还是『艾尔贝离宫』了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F『艾尔贝离宫』……\x01",
            "不就是那座森林中的王家建筑吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F可能性比较高。\x02\x03",
            "以针对恐怖组织的名义接管那里，\x01",
            "其实就是调用了特务兵来监守人质……\x02\x03",
            "而且，我认为王族的女性\x01",
            "不可能会被监禁在雷斯顿要塞那种地方。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F可对手是军队，\x01",
            "我们要有确凿的情报才行。\x02\x03",
            "稍有差池的话是不能击败对手的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764F嗯……说的也是。\x02\x03",
            "#760F不管推测是否属实，\x01",
            "先把在王都的其他游击士聚集起来再说吧。\x01",
            "　\x02\x03",
            "等把他们聚集到一起之后，\x01",
            "我们再去收集情报如何？\x02\x03",
            "据我所知，艾丝蒂尔你们\x01",
            "和杂志社的记者比较熟悉对吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，你是说奈尔吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F的确，在没有什么线索的情况下，\x01",
            "还是先问问他们会比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762F还有，如果可能的话，\x01",
            "也请尽量得到潜伏中的亲卫队的协助。\x02\x03",
            "我们营救人质的计划，\x01",
            "他们肯定会予以全力支持的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F这么说……\x02\x03",
            "要和乔装成修女的尤莉亚中尉\x01",
            "取得联络才行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F上次多亏得到她的帮助才能见到女王，\x01",
            "所以这次最好向她报告一下这件事。\x02\x03",
            "那我们这就前往大圣堂吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760F在王都的其余游击士有克鲁茨、\x01",
            "库拉茨、卡露娜和亚妮拉丝这四位。\x01",
            "　\x02\x03",
            "在酒廊、一般的商店，\x01",
            "或者酒店里都可以见到他们。\x02\x03",
            "找到的话，就叫他们到这里来集合吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        "#006F嗯，ＯＫ！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x102,
        "#010F那么我们就立刻出发吧。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_16_BB74 end

    def Function_17_D66F(): pass

    label("Function_17_D66F")

    OP_28(0x4F, 0x1, 0x20)
    OP_28(0x4F, 0x1, 0x40)
    OP_28(0x4F, 0x1, 0x80)
    OP_28(0x4F, 0x1, 0x100)
    OP_28(0x4F, 0x1, 0x200)
    OP_28(0x4F, 0x1, 0x400)
    OP_28(0x4F, 0x1, 0x800)
    OP_28(0x4F, 0x4, 0x10)
    EventBegin(0x0)
    OP_6D(115240, 250, 4410, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(1550, 0)
    OP_6C(315000, 0)
    OP_6E(519, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x8, 122730, 0, -1280, 180)
    SetChrPos(0xA, 120000, 0, -2600, 90)
    SetChrPos(0x9, 118530, 0, -3290, 90)
    SetChrPos(0xB, 119790, 0, -3880, 90)
    SetChrPos(0xC, 118310, 0, -1930, 90)
    SetChrPos(0xE, 120540, 0, 450, 135)
    SetChrPos(0xF, 120230, 0, -800, 135)
    SetChrPos(0x10, 118670, 0, -680, 135)
    SetChrPos(0x11, 123780, 0, -740, 180)
    SetChrPos(0x101, 122440, 0, -3200, 0)
    SetChrPos(0x102, 123620, 0, -3200, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    FadeToBright(2000, 0)
    OP_6D(121410, 0, -1310, 4000)

    ChrTalk(
        0x8,
        (
            "#760F#2P——艾丝蒂尔·布莱特，\x01",
            "还有约修亚·布莱特。\x02\x03",
            "根据这次行动的表现，格兰赛尔支部\x01",
            "决定授予你们正游击士资格的推荐信。\x02\x03",
            "请接受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F是！\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x1DFD8, 0x0, 0xFFFFF6AA, 0x7D0, 0x0)
    Sleep(100)
    OP_AF(0x63, 0x4F)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
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
    OP_3E(0x33B, 1)
    OP_8F(0x8, 0x1DF6A, 0x0, 0xFFFFFB00, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "#761F#2P这样，你们二人也已经\x01",
            "获得了五个地区支部的推荐信。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    ChrTalk(
        0x8,
        (
            "#760F#5P那么，卡西乌斯先生，\x01",
            "接下来的工作就交给您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#085F#2P嗯。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_8F(0x8, 0x1DE8E, 0x0, 0xFFFFFE66, 0x7D0, 0x0)
    OP_8F(0x11, 0x1E01E, 0x0, 0xFFFFF916, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#082F#2P艾丝蒂尔·布莱特，\x01",
            "还有约修亚·布莱特。\x02\x03",
            "现基于游击士协会的规定，\x01",
            "正式授予你们二人正游击士的资格。\x02\x03",
            "请交出各地方支部的推荐信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F好、好的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F请您确认一下。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了所有的\x07\x02",
            "正游击士资格的推荐信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x330, 1)
    OP_3F(0x333, 1)
    OP_3F(0x339, 1)
    OP_3F(0x33A, 1)
    OP_3F(0x33B, 1)
    OP_3F(0x36D, 1)
    OP_3F(0x36E, 1)

    ChrTalk(
        0x11,
        (
            "#085F#2P洛连特支部、柏斯支部、\x01",
            "卢安支部、蔡斯支部，\x01",
            "还有格兰赛尔支部……\x02\x03",
            "五个支部的签名都确认完毕了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCEE")

    ChrTalk(
        0x11,
        (
            "#080F#2P最终等级是准游击士１级。\x02\x03",
            "#081F没想到能达到如此程度，\x01",
            "你们俩的成绩真是让我吃惊呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF94")

    label("loc_DCEE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD69")

    ChrTalk(
        0x11,
        (
            "#080F#2P最终等级是准游击士２级。\x02\x03",
            "作为见习的新人已经做得很不错了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF94")

    label("loc_DD69")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDE4")

    ChrTalk(
        0x11,
        (
            "#080F#2P最终等级是准游击士３级。\x02\x03",
            "作为见习的新人已经做得很不错了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF94")

    label("loc_DDE4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE7B")

    ChrTalk(
        0x11,
        (
            "#080F#2P最终等级是准游击士４级。\x02\x03",
            "#083F说真的，成绩差强人意，\x01",
            "你们俩以后还要继续努力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF94")

    label("loc_DE7B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF12")

    ChrTalk(
        0x11,
        (
            "#080F#2P最终等级是准游击士５级。\x02\x03",
            "#083F说真的，成绩差强人意，\x01",
            "你们俩以后还要继续努力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF94")

    label("loc_DF12")


    ChrTalk(
        0x11,
        (
            "#080F#2P最终等级是准游击士……\x02\x03",
            "#083F……该怎么评价好呢，\x01",
            "以这种成绩也能成为正游击士也算是奇迹。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF94")

    Sleep(400)

    ChrTalk(
        0x11,
        (
            "#080F#2P现以女神与游击士徽章之名义，\x01",
            "在此任命你们二人为正游击士。\x02\x03",
            "你们二人，请接受徽章。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F是！\x02",
    )

    CloseMessageWindow()
    OP_8F(0x11, 0x1DFD8, 0x0, 0xFFFFF6AA, 0x7D0, 0x0)
    OP_AD(0x40023, 0xBE, 0x64, 0x1F4)
    Sleep(1500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "正游击士的徽章\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x35D, 1)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_8F(0x11, 0x1E01E, 0x0, 0xFFFFF916, 0x7D0, 0x0)
    OP_22(0xE9, 0x0, 0x64)
    Sleep(500)

    def lambda_E0E9():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E0E9)

    def lambda_E0F7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E0F7)
    OP_6D(119780, 0, -1210, 1500)
    Sleep(500)

    ChrTalk(
        0xF,
        "#021F恭喜！艾丝蒂尔、约修亚！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#071F哈哈，新的徽章，\x01",
            "看起来非常适合你们嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#051F哼……\x01",
            "这次我就破例称赞你们『干得好』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#6P嘿嘿……\x01",
            "真是太谢谢大家了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F我们能取得今天的成绩……\x01",
            "也是多亏了大家的帮助和支持。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#080F#2P游击士的生涯从这里才正式开始。\x01",
            "　\x02\x03",
            "你们俩，不要忘记这一点哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E26C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E26C)
    Sleep(100)
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        "#006F#6P嗯……我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们会努力更上一层楼的。\x02",
    )

    CloseMessageWindow()
    OP_6D(119780, 0, -210, 1000)
    OP_8C(0x8, 225, 400)

    ChrTalk(
        0x8,
        (
            "#760F#2P各位，虽然很抱歉打断你们的谈话，\x01",
            "不过庆贺的话还请留待之后再说吧……\x02\x03",
            "趁今天大家齐聚一起的机会，\x01",
            "必须向大家宣布一件很遗憾的事情。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E374():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E374)

    def lambda_E382():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E382)

    def lambda_E390():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E390)

    def lambda_E39E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E39E)

    def lambda_E3AC():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E3AC)

    def lambda_E3BA():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E3BA)

    def lambda_E3C8():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E3C8)

    def lambda_E3D6():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E3D6)

    def lambda_E3E4():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E3E4)

    def lambda_E3F2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E3F2)

    ChrTalk(
        0xC,
        "#842F遗憾的事情……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762F#2P从今天开始，\x01",
            "卡西乌斯·布莱特先生正式决定\x01",
            "退出我们游击士协会。\x02\x03",
            "在往后的日子里，\x01",
            "卡西乌斯先生将重返王国军。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_E516():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E516)

    def lambda_E524():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E524)

    def lambda_E532():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E532)

    def lambda_E540():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E540)

    def lambda_E54E():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E54E)
    Sleep(1000)

    def lambda_E561():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E561)

    def lambda_E56F():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E56F)

    def lambda_E57D():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E57D)

    def lambda_E58B():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E58B)

    ChrTalk(
        0x9,
        "#832F#5P什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#822F#5P是、是真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#085F#2P长时间外出之后，\x01",
            "还向协会提出这样突然的请求，\x01",
            "各位，我真是深感抱歉。\x02\x03",
            "#080F但是，王国的当务之急，\x01",
            "是必须解决政变所带来的混乱状况。\x02\x03",
            "被情报部弄得乌烟瘴气的\x01",
            "军队的指挥系统也有必要重建。\x02\x03",
            "所以，我打算协助做这些工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#818F#5P啊，是啊……\x01",
            "军人不能同时担任游击士……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xF, 400)

    ChrTalk(
        0xA,
        (
            "#814F#5P对了，\x01",
            "前辈你们好像知道这件事吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xA, 400)

    ChrTalk(
        0xF,
        (
            "#020F#2P嗯，老师和我们谈过这件事。\x02\x03",
            "老实说，虽然感到非常惋惜……\x01",
            "但如果总是依赖老师的话，\x01",
            "我们是无法成为独当一面的游击士的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xA, 400)

    ChrTalk(
        0xE,
        (
            "#051F哼，以后我们要证明给他看看，\x01",
            "不管什么事情年轻人也都能办到。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#841F#5P是吗……是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#835F#5P不管什么时候\x01",
            "都无法从忙碌中解脱出来啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E90B():
        OP_6D(119780, 0, -1210, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E90B)
    OP_8C(0x11, 180, 400)

    def lambda_E92A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E92A)

    def lambda_E938():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E938)

    def lambda_E946():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E946)

    def lambda_E954():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E954)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x11,
        (
            "#080F#2P不过今天有两位新的正游击士诞生了。\x01",
            "　\x02\x03",
            "他们俩作为我今后的代理人，\x01",
            "可以任由你们这些前辈随意差遣哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#6P喂～我说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#4P哈哈，看来以后会变得更忙呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x66B)
    ClearMapFlags(0x2000000)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_D66F end

    def Function_18_EA57(): pass

    label("Function_18_EA57")

    EventBegin(0x0)
    OP_6D(-3270, 0, 730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -2600, 0, 100, 90)
    SetChrPos(0x101, -860, 0, -670, 270)
    SetChrPos(0x102, -950, 0, 482, 270)
    OP_4A(0x8, 255)
    SetChrPos(0x8, -5700, 0, -130, 270)
    LoadEffect(0x0, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x18,
        (
            "#033F#5P？？？\x02\x03",
            "为什么要到游击士协会来呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#507F哎呀呀，不要着急嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们马上让艾南先生\x01",
            "把那个人叫过来。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EBDA():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_EBDA)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#760F#4P嗯，好的，\x01",
            "那么，就请到游击士协会来……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(300)
    OP_8C(0x8, 90, 400)
    OP_8E(0x8, 0xFFFFEE80, 0x0, 0x3C0, 0x7D0, 0x0)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "#761F各位，联络完毕了。\x02\x03",
            "那个人很快就会到这里了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#035F呵，这么急不可耐\x01",
            "想和我这个天才演奏家见面啊。\x02\x03",
            "#030F对了，\x01",
            "那个小猫咪是我以前认识的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F当然啦，\x01",
            "而且是你再熟悉不过的朋友哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 90, 400)

    ChrTalk(
        0x18,
        (
            "#037F#5P唔呵呵……\x01",
            "现在在王都这里的小猫咪……\x02\x03",
            "这么说是雪拉君……\x01",
            "还是卡露娜女士或亚妮拉丝小姐……\x02\x03",
            "#035F不对不对，\x01",
            "梅贝尔市长和莉拉小姐也是有可能的……\x02\x03",
            "#033F啊，难道说是科洛蒂娅公主\x01",
            "或是提妲小姑娘吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#019F该怎么说呢……\x01",
            "这还真是惊人的想象力啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(700)
    SetChrPos(0x19, -200, -250, -7270, 152)

    def lambda_EF66():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EF66)

    def lambda_EF74():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EF74)

    def lambda_EF82():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_EF82)

    def lambda_EF90():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EF90)
    OP_9F(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-1570, 0, -2670, 2000)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#760F#6P啊，\x01",
            "请直接进来就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#031F哦哦，终于来了！\x02\x03",
            "我心爱的人儿啊！\x01",
            "快，进来吧！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x19,
        "男人的声音",
        (
            "#2P……那么，我就不客气了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    ClearChrFlags(0x19, 0x80)

    def lambda_F07E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_F07E)

    def lambda_F090():
        OP_8E(0x19, 0xFFFFF8F8, 0x0, 0xFFFFF7F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_F090)

    def lambda_F0AB():

        label("loc_F0AB")

        TurnDirection(0x19, 0x18, 0)
        OP_48()
        Jump("loc_F0AB")

    QueueWorkItem2(0x19, 0, lambda_F0AB)

    def lambda_F0BC():
        OP_6D(-2220, 0, -370, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F0BC)

    def lambda_F0D4():

        label("loc_F0D4")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_F0D4")

    QueueWorkItem2(0x101, 1, lambda_F0D4)

    def lambda_F0E5():

        label("loc_F0E5")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_F0E5")

    QueueWorkItem2(0x102, 1, lambda_F0E5)

    def lambda_F0F6():

        label("loc_F0F6")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_F0F6")

    QueueWorkItem2(0x18, 1, lambda_F0F6)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x18,
        "#033F啊……\x02",
    )

    CloseMessageWindow()
    OP_44(0x19, 0xFF)
    TurnDirection(0x19, 0x101, 400)

    ChrTalk(
        0x19,
        (
            "#270F看来只有靠你们俩\x01",
            "才能这么顺利地完成这个委托。\x02\x03",
            "#272F非常感谢，\x01",
            "我代表帝国大使馆向你们致意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F哪里哪里，不用客气啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F奥利维尔他本人也非常愿意呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#033F……和你们说的不一样啊。\x02\x03",
            "想见我的小猫咪到底在哪儿啊……？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 400)

    ChrTalk(
        0x19,
        (
            "#270F你在说什么胡话。\x02\x03",
            "由于接受了女王陛下的直接邀请，\x01",
            "现在正要对出席今夜晚宴的相关事项进行确认。\x01",
            "　\x02\x03",
            "正因为如此，\x01",
            "不能再对你放任不管了。\x02\x03",
            "这已经不是第一次了，\x01",
            "我反复对你强调过吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x18, 0xFF)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x18, 90, 400)

    ChrTalk(
        0x18,
        (
            "#036F艾、艾丝蒂尔君！约修亚君！\x02\x03",
            "你们太残忍了吧！\x01",
            "怎么能够这样欺骗我的感情呢！？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        "#509F这种话让别人听到会想歪的……\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x102,
        (
            "#019F我们完全没有说过\x01",
            "是一位女性在等着你啊……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x19, 0x40)
    OP_8E(0x19, 0xFFFFF5D8, 0x0, 0xFFFFFCE0, 0xBB8, 0x0)
    TurnDirection(0x19, 0x18, 400)
    TurnDirection(0x18, 0x19, 0)

    ChrTalk(
        0x19,
        (
            "#272F#3P好了……时间不多了，\x01",
            "很快就要到傍晚了。\x02\x03",
            "还有许多事情要商定，\x01",
            "赶快回大使馆去吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F58B():

        label("loc_F58B")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_F58B")

    QueueWorkItem2(0x101, 1, lambda_F58B)

    def lambda_F59C():

        label("loc_F59C")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_F59C")

    QueueWorkItem2(0x102, 1, lambda_F59C)
    OP_8E(0x19, 0xFFFFF5D8, 0x0, 0xFFFFFD44, 0xBB8, 0x0)
    OP_8C(0x19, 90, 400)
    SetChrFlags(0x18, 0x4)
    SetChrPos(0x18, -2600, 400, 100, 0)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_F5F0():
        OP_97(0x18, 0xFFFFF5D8, 0xFFFFFD44, 0x16760, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_F5F0)
    SetChrChipByIndex(0x18, 20)
    SetChrSubChip(0x18, 0)
    SetChrFlags(0x18, 0x20)
    OP_8C(0x19, 180, 400)

    ChrTalk(
        0x18,
        "#20A#036F哎～呀～！\x05\x02",
    )

    OP_43(0x18, 0x1, 0x0, 0x13)
    OP_43(0x19, 0x1, 0x0, 0x14)
    WaitChrThread(0x18, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x8, 0x1)
    OP_6D(-2240, 0, 670, 1000)
    TurnDirection(0x8, 0x102, 400)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "#760F呼，总算是告一段落了。\x02\x03",
            "审核也一起完成了，请收下报酬。\x01",
            "　\x02\x03",
            "因为正游击士的手册还没有准备好，\x01",
            "所以暂且先用准游击士手册来记录。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x55, 0x4, 0x10)
    OP_28(0x55, 0x1, 0x1)
    OP_28(0x55, 0x1, 0x2)
    Sleep(100)
    OP_AF(0x63, 0x55)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#506F#6P嗯，感觉有点内疚呢，\x01",
            "还好事先得到了他本人的同意。\x02\x03",
            "#006F那么，\x01",
            "诞辰庆典游览再次开始。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#2P嗯，好的。\x02\x03",
            "我们逛一圈之后，\x01",
            "就到东街区的休息处去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x800)
    OP_4B(0x8, 255)
    OP_A2(0x6FB)
    EventEnd(0x0)
    Return()

    # Function_18_EA57 end

    def Function_19_F8AF(): pass

    label("Function_19_F8AF")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0x21C, 0xFA, 0xFFFFEA02, 0x7D0, 0x0)

    def lambda_F8D3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_F8D3)
    OP_8F(0xFE, 0x21C, 0xFA, 0xFFFFE192, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_F8AF end

    def Function_20_F8F9(): pass

    label("Function_20_F8F9")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0xFFFFFEAC, 0xFFFFFF06, 0xFFFFEA02, 0x834, 0x0)

    def lambda_F91D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_F91D)
    OP_8F(0xFE, 0xFFFFFEAC, 0xFFFFFF06, 0xFFFFE192, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_F8F9 end

    def Function_21_F943(): pass

    label("Function_21_F943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 5)), scpexpr(EXPR_END)), "loc_F956")
    OP_2A(0x50, 0x51, 0x55, 0xFFFF)
    Jump("loc_F9F8")

    label("loc_F956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_F99C")
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在没有什么特别的委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_F9F8")

    label("loc_F99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_F9AD")
    OP_2A(0x50, 0x51, 0xFFFF)
    Jump("loc_F9F8")

    label("loc_F9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_F9BC")
    OP_2A(0x50, 0xFFFF)
    Jump("loc_F9F8")

    label("loc_F9BC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在没有什么特别的委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F9F8")

    TalkEnd(0xFF)
    Return()

    # Function_21_F943 end

    SaveToFile()

Try(main)
