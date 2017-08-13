from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2330   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2330.x',
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
        '雷克斯',                               # 9
        '卡拉',                                 # 10
        '特蕾莎院长',                           # 11
        '达尼艾尔',                             # 12
        '玛丽',                                 # 13
        '波利',                                 # 14
        '克拉姆',                               # 15
        '戴尔蒙市长',                           # 16
        '秘书基尔巴特',                         # 17
        '卡露娜',                               # 18
        '阿尔宾',                               # 19
        '蔡尔德',                               # 20
        '卢希娅',                               # 21
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02640 ._CH',             # 02
        'ED6_DT07/CH02630 ._CH',             # 03
        'ED6_DT07/CH02570 ._CH',             # 04
        'ED6_DT07/CH02410 ._CH',             # 05
        'ED6_DT07/CH02420 ._CH',             # 06
        'ED6_DT07/CH01030 ._CH',             # 07
        'ED6_DT07/CH01240 ._CH',             # 08
        'ED6_DT07/CH02500 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01070 ._CH',             # 0C
        'ED6_DT06/CH20093 ._CH',             # 0D
        'ED6_DT06/CH20101 ._CH',             # 0E
        'ED6_DT06/CH20053 ._CH',             # 0F
        'ED6_DT07/CH01023 ._CH',             # 10
        'ED6_DT07/CH01143 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02640P._CP',             # 02
        'ED6_DT07/CH02630P._CP',             # 03
        'ED6_DT07/CH02570P._CP',             # 04
        'ED6_DT07/CH02410P._CP',             # 05
        'ED6_DT07/CH02420P._CP',             # 06
        'ED6_DT07/CH01030P._CP',             # 07
        'ED6_DT07/CH01240P._CP',             # 08
        'ED6_DT07/CH02500P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01070P._CP',             # 0C
        'ED6_DT06/CH20093P._CP',             # 0D
        'ED6_DT06/CH20101P._CP',             # 0E
        'ED6_DT06/CH20053P._CP',             # 0F
        'ED6_DT07/CH01023P._CP',             # 10
        'ED6_DT07/CH01143P._CP',             # 11
    )

    DeclNpc(
        X                   = -25500,
        Z                   = 0,
        Y                   = 43210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -37500,
        Z                   = 0,
        Y                   = 44500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -50190,
        Z                   = 0,
        Y                   = -1000,
        Direction           = 90,
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
        X                   = -50850,
        Z                   = 0,
        Y                   = 180,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -50850,
        Z                   = 0,
        Y                   = 1400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -50570,
        Z                   = 0,
        Y                   = -2840,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -49420,
        Z                   = 0,
        Y                   = -2280,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
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
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -400,
        Z                   = 0,
        Y                   = 45400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -33200,
        Z                   = 150,
        Y                   = 41740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -32060,
        Z                   = 150,
        Y                   = 42960,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -23900,
        Z                   = 0,
        Y                   = -1170,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )


    DeclActor(
        TriggerX            = -37020,
        TriggerZ            = 0,
        TriggerY            = 42970,
        TriggerRange        = 400,
        ActorX              = -37500,
        ActorZ              = 1500,
        ActorY              = 44500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26870,
        TriggerZ            = 0,
        TriggerY            = 42820,
        TriggerRange        = 400,
        ActorX              = -25500,
        ActorZ              = 1500,
        ActorY              = 43210,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_322",          # 00, 0
        "Function_1_5C7",          # 01, 1
        "Function_2_611",          # 02, 2
        "Function_3_627",          # 03, 3
        "Function_4_62C",          # 04, 4
        "Function_5_151E",         # 05, 5
        "Function_6_1523",         # 06, 6
        "Function_7_1B02",         # 07, 7
        "Function_8_20DD",         # 08, 8
        "Function_9_26CC",         # 09, 9
        "Function_10_2AB9",        # 0A, 10
        "Function_11_2B61",        # 0B, 11
        "Function_12_2C38",        # 0C, 12
        "Function_13_2CBC",        # 0D, 13
        "Function_14_2D59",        # 0E, 14
        "Function_15_2E04",        # 0F, 15
        "Function_16_2E80",        # 10, 16
        "Function_17_54C4",        # 11, 17
        "Function_18_54DF",        # 12, 18
        "Function_19_54F0",        # 13, 19
        "Function_20_5501",        # 14, 20
        "Function_21_5512",        # 15, 21
        "Function_22_5528",        # 16, 22
        "Function_23_6758",        # 17, 23
        "Function_24_6779",        # 18, 24
        "Function_25_679A",        # 19, 25
        "Function_26_67BB",        # 1A, 26
        "Function_27_67E9",        # 1B, 27
        "Function_28_681C",        # 1C, 28
        "Function_29_684F",        # 1D, 29
        "Function_30_6882",        # 1E, 30
    )


    def Function_0_322(): pass

    label("Function_0_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_32C")
    Jump("loc_591")

    label("loc_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_393")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -48350, 0, 150, 215)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -50850, 0, 180, 135)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -50570, 0, -2840, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -49420, 0, -2280, 315)
    Jump("loc_591")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_42B")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, -53290, 0, 2040, 180)
    SetChrPos(0xA, -53080, 0, -870, 180)
    SetChrPos(0xB, -50850, 0, -230, 270)
    SetChrPos(0xD, -50850, 0, -1430, 270)
    SetChrPos(0xC, -52530, 0, -2420, 0)
    SetChrPos(0xE, -50800, 0, 1470, 270)
    Jump("loc_591")

    label("loc_42B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_502")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, -53000, 0, 2040, 90)
    SetChrPos(0xA, -53000, 0, -870, 90)
    SetChrChipByIndex(0xA, 13)
    SetChrChipByIndex(0x11, 14)
    OP_44(0x11, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrPos(0xB, -50850, 0, -230, 270)
    SetChrPos(0xD, -50850, 0, -1430, 270)
    SetChrPos(0xC, -52530, 0, -2420, 0)
    SetChrPos(0xE, -50800, 0, 1470, 270)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_591")

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_511")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_591")

    label("loc_511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_562")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -48450, 0, -990, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -49210, 0, -2360, 315)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -47720, 0, 2100, 0)
    Jump("loc_591")

    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_56C")
    Jump("loc_591")

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_576")
    Jump("loc_591")

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_580")
    Jump("loc_591")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_58A")
    Jump("loc_591")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_591")

    label("loc_591")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (107, "loc_59D"),
        (SWITCH_DEFAULT, "loc_5C6"),
    )


    label("loc_59D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B0")
    OP_A2(0x428)
    Event(0, 16)

    label("loc_5B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C3")
    OP_A2(0x436)
    Event(0, 22)

    label("loc_5C3")

    Jump("loc_5C6")

    label("loc_5C6")

    Return()

    # Function_0_322 end

    def Function_1_5C7(): pass

    label("Function_1_5C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F7")
    OP_B1("t2330_y")
    OP_72(0x2, 0x20)
    OP_6F(0x2, 15)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 15)
    Jump("loc_600")

    label("loc_5F7")

    OP_B1("t2330_n")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_610")
    OP_64(0x0, 0x1)

    label("loc_610")

    Return()

    # Function_1_5C7 end

    def Function_2_611(): pass

    label("Function_2_611")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_626")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_611")

    label("loc_626")

    Return()

    # Function_2_611 end

    def Function_3_627(): pass

    label("Function_3_627")

    Call(0, 4)
    Return()

    # Function_3_627 end

    def Function_4_62C(): pass

    label("Function_4_62C")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                 # 0
            "买东西\x01",                               # 1
            "欢迎品尝「硬壳杂菜烩饭」500米拉\x01",      # 2
            "离开\x01",                                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AA")
    OP_0D()
    OP_A9(0x2A)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_6AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AC")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_777")
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
            "硬壳杂菜烩饭\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x1C2)
    OP_31(0x1, 0xFD, 0x1C2)
    OP_31(0x2, 0xFD, 0x1C2)
    OP_31(0x3, 0xFD, 0x1C2)
    OP_31(0x4, 0xFD, 0x1C2)
    OP_31(0x5, 0xFD, 0x1C2)
    OP_31(0x6, 0xFD, 0x1C2)
    OP_31(0x7, 0xFD, 0x1C2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_769")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x1)"), scpexpr(EXPR_END)), "loc_73F")
    Jump("loc_769")

    label("loc_73F")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "硬壳杂菜烩饭\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_769")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_79D")

    label("loc_777")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_79D")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x8)
    Return()

    label("loc_7AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BD")
    TalkEnd(0x8)
    Return()

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1A")
    EventBegin(0x0)
    OP_69(0x8, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B67")

    ChrTalk(
        0x8,
        "欢迎来到『白之木莲亭』。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "啊，以前没见过你们。\x01",
            "是来玛诺利亚村观光的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F不是呢。\x01",
            "其实我们正在去卢安市的途中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是从柏斯那边\x01",
            "越过古罗尼山峰来到这里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "越过古罗尼山峰！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哈～没想到现在这个年代\x01",
            "还会有人爬那座山峰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你们平时有爬山的爱好吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊……\x01",
            "也不算是啦。\x02\x03",
            "#501F总之，我们走了好久的山路，\x01",
            "现在肚子饿得咕咕直叫呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F这里有什么特别推荐的料理吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "料理的话……\x01",
            "中午特别推荐的就肯定是便当了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F便当？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们村里的风车屋前\x01",
            "有个可以看到漂亮海景的了望台。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "每到中午的时候，\x01",
            "就有很多客人来这里买便当拿去那里吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊～好像蛮有趣的嘛⊙\x02\x03",
            "光是听你这么介绍，\x01",
            "我就已经觉得很好吃呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F那么我们就买便当吧。\x02\x03",
            "#010F请问这里的便当有几种呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "今天有海鲜焗饭\x01",
            "和熏火腿三明治两种。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不管哪一个都非常值得品尝的哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯～\x01",
            "我要熏火腿三明治。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我要海鲜焗饭吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "多谢惠顾。\x01",
            "两款便当合计１２０米拉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBF")

    label("loc_B67")


    ChrTalk(
        0x8,
        (
            "我们这里今天出售\x01",
            "海鲜焗饭和熏火腿三明治\x01",
            "两种便当。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "一共是１２０米拉，可以吗？\x02",
    )

    CloseMessageWindow()

    label("loc_BBF")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【购买】\x01",          # 0
            "【还是算了】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C26"),
        (1, "loc_D85"),
        (SWITCH_DEFAULT, "loc_E15"),
    )


    label("loc_C26")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D46")
    OP_4F(0x12, (scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_22(0x14, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "特制午餐盒饭\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x33C, 1)

    ChrTalk(
        0x8,
        (
            "另外，作为今天的特别服务，\x01",
            "随便当附送香草茶哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这种茶也是本店的推荐饮品。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊～谢谢㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F那我们现在就去了望台吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x101,
        "#006F嗯！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x413)
    Jump("loc_D82")

    label("loc_D46")


    ChrTalk(
        0x8,
        (
            "咦……\x01",
            "好像没有足够的米拉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "攒够了钱再来吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x401)

    label("loc_D82")

    Jump("loc_E15")

    label("loc_D85")


    ChrTalk(
        0x8,
        (
            "那么，\x01",
            "就在这里用餐怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "我们还供应很多别的料理。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯～\x01",
            "我还是想在室外吃便当呢。\x02\x03",
            "#008F不好意思，我们再考虑一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x401)
    Jump("loc_E15")

    label("loc_E15")

    EventEnd(0x1)
    Jump("loc_151A")

    label("loc_E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_F03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAE")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "当时我看到的犯人\x01",
            "果然是市长的秘书啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "说起来，\x01",
            "市长他们竟然犯下那样的罪行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哼，\x01",
            "他们要用往后的人生来赎罪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F00")

    label("loc_EAE")


    ChrTalk(
        0x8,
        (
            "说起来，\x01",
            "市长他们竟然犯下那样的罪行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哼，\x01",
            "他们要用往后的人生来赎罪了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F00")

    Jump("loc_151A")

    label("loc_F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_FE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F99")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "我好像在哪里\x01",
            "看到过其中的一个犯人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "难道说，就是之前\x01",
            "到这里来过的戴尔蒙市长的秘书？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……不会的。\x01",
            "应该不可能的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE5")

    label("loc_F99")


    ChrTalk(
        0x8,
        (
            "其中一个犯人\x01",
            "感觉有点像市长的秘书……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……不会的。\x01",
            "应该不可能的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE5")

    Jump("loc_151A")

    label("loc_FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_1097")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1059")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "老师她们\x01",
            "在这里的二楼休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "纵火事件也好，这回的事情也罢，\x01",
            "孩子们真是太可怜了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1094")

    label("loc_1059")


    ChrTalk(
        0x8,
        (
            "纵火事件也好，这回的事情也罢，\x01",
            "孩子们真是太可怜了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1094")

    Jump("loc_151A")

    label("loc_1097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_117D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1120")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "马上就要到学园祭了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "孤儿院的孩子们\x01",
            "好像也要到学院里去玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "能忘记以前的不快，\x01",
            "玩得开心就最好不过了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117A")

    label("loc_1120")


    ChrTalk(
        0x8,
        (
            "孤儿院的孩子们\x01",
            "好像也要到学院里去玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "能忘记以前的不快，\x01",
            "玩得开心就最好不过了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117A")

    Jump("loc_151A")

    label("loc_117D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_11D0")

    ChrTalk(
        0x8,
        (
            "就在刚才，\x01",
            "有个孤儿院的男孩子飞奔出去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "发生什么事情了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_151A")

    label("loc_11D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_129A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1260")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "听说，\x01",
            "孤儿院被烧得精光？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我马上就去\x01",
            "腾出房间给孩子们住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "小姑娘，如果可以的话，\x01",
            "请你们鼓励一下那些孩子哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1297")

    label("loc_1260")


    ChrTalk(
        0x8,
        (
            "小姑娘，如果可以的话，\x01",
            "请你们鼓励一下那些孩子哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1297")

    Jump("loc_151A")

    label("loc_129A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_12DD")

    ChrTalk(
        0x8,
        "今天的风很宜人啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "沿着海岸散步\x01",
            "感觉很舒服哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_151A")

    label("loc_12DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_13FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A1")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "这里的游客大多都是\x01",
            "来观赏木莲之花和海岸美景的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "偶尔也会有一些\x01",
            "像那两个人一样的登山客来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以前的人都是通过这里往来于柏斯和卢安的，\x01",
            "所以说村里曾经非常热闹呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F9")

    label("loc_13A1")


    ChrTalk(
        0x8,
        (
            "从风车小屋望出去，\x01",
            "景色很美丽吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那个风车小屋和湛蓝的大海\x01",
            "搭配起来很漂亮呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F9")

    Jump("loc_151A")

    label("loc_13FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_149F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1473")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "哦，\x01",
            "这不是刚才来过的小姑娘吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "有什么事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "啊？男孩子吗？\x01",
            "他没有到这家店来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149C")

    label("loc_1473")


    ChrTalk(
        0x8,
        (
            "啊？男孩子吗？\x01",
            "他没有到这家店来哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149C")

    Jump("loc_151A")

    label("loc_149F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_151A")

    ChrTalk(
        0x8,
        (
            "我们村里的风车小屋前\x01",
            "有个可以看到漂亮海景的了望台。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "每到中午的时候，\x01",
            "就有很多客人来这里买便当拿去那里吃。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151A")

    TalkEnd(0x8)
    Return()

    # Function_4_62C end

    def Function_5_151E(): pass

    label("Function_5_151E")

    Call(0, 6)
    Return()

    # Function_5_151E end

    def Function_6_1523(): pass

    label("Function_6_1523")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157F")
    OP_0D()
    OP_A9(0x29)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_157F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1590")
    TalkEnd(0x9)
    Return()

    label("loc_1590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_15EB")

    ChrTalk(
        0x9,
        (
            "在孤儿院重建之前，\x01",
            "各位就先住在这里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "这里变得热闹起来，我也很高兴。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_15EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_165C")

    ChrTalk(
        0x9,
        "听说犯人被抓住了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "与其交给游击士协会，\x01",
            "我们更想亲自来惩罚他们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "可能会用石头砸他们吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_165C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_16A7")

    ChrTalk(
        0x9,
        "怎么会变成这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不可原谅……\x01",
            "做坏事也要有个限度啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_16A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1757")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1714")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "孤儿院的孩子们和老师\x01",
            "就由我们『白之木莲亭』\x01",
            "来好好照顾吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "一人有难大家帮嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1754")

    label("loc_1714")


    ChrTalk(
        0x9,
        (
            "孤儿院的老师和孩子们\x01",
            "就由我们『白之木莲亭』\x01",
            "来好好照顾吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1754")

    Jump("loc_1AFE")

    label("loc_1757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1798")

    ChrTalk(
        0x9,
        (
            "刚才克拉姆\x01",
            "急急忙忙跑出去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "到底怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_1798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_18E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1899")
    OP_A2(0x1)
    TurnDirection(0x9, 0x136, 0)

    ChrTalk(
        0x9,
        "啊，王立学院的校服……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "难道，\x01",
            "你就是科洛丝吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#044F嗯，是的。\x01",
            "我就是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "孤儿院的孩子们\x01",
            "都急着想见你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "他们应该都\x01",
            "还在二楼的大房间里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "你快点去见见他们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#043F嗯，好、好的。\x01",
            "真是麻烦您了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18DF")

    label("loc_1899")

    TurnDirection(0x9, 0x136, 0)

    ChrTalk(
        0x9,
        (
            "孤儿院的孩子们\x01",
            "都急着想见你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "你快点去见见他们吧。\x02",
    )

    CloseMessageWindow()

    label("loc_18DF")

    Jump("loc_1AFE")

    label("loc_18E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1980")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1948")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "好，接下来该洗衣服了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "今天的天气很不错，\x01",
            "晒床单的话应该很快就能干吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197D")

    label("loc_1948")


    ChrTalk(
        0x9,
        (
            "今天的天气很不错，\x01",
            "晒床单的话应该很快就能干吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197D")

    Jump("loc_1AFE")

    label("loc_1980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_19F2")

    ChrTalk(
        0x9,
        (
            "今年的木莲之花\x01",
            "也开始陆陆续续地盛开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这里虽然不是什么起眼的村子，\x01",
            "但是来赏花的人却不少呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_19F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_1A4A")

    ChrTalk(
        0x9,
        (
            "男孩子？\x01",
            "我没见过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果是王立学院的女生，\x01",
            "那刚才还见到过一个……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_1A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1AFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD1")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "哟，两位客人你好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果可以的话，\x01",
            "请在我们这里享用午餐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "和丈夫一起经营旅馆，\x01",
            "我也渐渐有了信心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_1AD1")


    ChrTalk(
        0x9,
        (
            "如果可以的话，\x01",
            "请在我们这里享用午餐吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AFE")

    TalkEnd(0x9)
    Return()

    # Function_6_1523 end

    def Function_7_1B02(): pass

    label("Function_7_1B02")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B46")

    ChrTalk(
        0xFE,
        "好，再去登山吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "古罗尼的山峰\x01",
            "在呼唤着我啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D9")

    label("loc_1B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_1BAF")

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "听说犯人被抓住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真想把他们带到山里，\x01",
            "把他们那些扭曲丑陋的性格\x01",
            "给纠正回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D9")

    label("loc_1BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_1CA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C40")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "那些孩子们\x01",
            "这次又被强盗袭击了！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "可恶，这是怎么回事啊！\x01",
            "怎么会发生这种残酷的事情！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA0")

    label("loc_1C40")


    ChrTalk(
        0xFE,
        (
            "那些孩子们\x01",
            "这次又被强盗袭击了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可恶，这是怎么回事啊！\x01",
            "怎么会发生这种残酷的事情！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA0")

    Jump("loc_20D9")

    label("loc_1CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1DBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D64")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "今天天气不错，\x01",
            "应该能够登上山顶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "我还是有点担心孤儿院的孩子们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还想再照顾一下\x01",
            "那些孩子们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我可能帮不上什么忙，\x01",
            "但是我也不能坐视不管。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB8")

    label("loc_1D64")


    ChrTalk(
        0xFE,
        (
            "今天天气不错，\x01",
            "应该能够登上山顶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "我还是有点担心孤儿院的孩子们啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB8")

    Jump("loc_20D9")

    label("loc_1DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1E1B")

    ChrTalk(
        0xFE,
        (
            "附近的孤儿院被纵火烧毁了，\x01",
            "是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "居然有人能\x01",
            "做出这么伤天害理的事情……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D9")

    label("loc_1E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_1E5E")

    ChrTalk(
        0xFE,
        (
            "我听到二楼\x01",
            "传出孩子们的哭声……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生什么事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D9")

    label("loc_1E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1F5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFD")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "山真好呀！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一大早起来呼吸到清爽的空气，\x01",
            "感觉真的很舒服……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "简直就像切身感受到\x01",
            "山间气氛的瞬间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊～好想快点去登山啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F5B")

    label("loc_1EFD")


    ChrTalk(
        0xFE,
        (
            "一大早起来呼吸到清爽的空气，\x01",
            "感觉真的很舒服……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "简直就像切身感受到\x01",
            "山间气氛的瞬间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5B")

    Jump("loc_20D9")

    label("loc_1F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2034")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2004")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "啊～我好想快点去登山啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你问我为什么要去登山？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，真是个愚蠢的问题……\x01",
            "因为那里有山啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F那个……\x01",
            "我什么也没有问啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2031")

    label("loc_2004")


    ChrTalk(
        0xFE,
        (
            "你问我为什么要去登山？\x01",
            "因为那里有山啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2031")

    Jump("loc_20D9")

    label("loc_2034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_2087")

    ChrTalk(
        0xFE,
        (
            "嗯？\x01",
            "你们在找一个戴帽子的男孩子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我好像没有看见过这样的孩子。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D9")

    label("loc_2087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_20D9")

    ChrTalk(
        0xFE,
        "我们是登山爱好者。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了登上古罗尼连峰，\x01",
            "我们才留在了玛诺利亚村。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D9")

    TalkEnd(0x12)
    Return()

    # Function_7_1B02 end

    def Function_8_20DD(): pass

    label("Function_8_20DD")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2140")

    ChrTalk(
        0xFE,
        (
            "唔，南坡面的雪有点融化，\x01",
            "可能会很危险……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还是重新考虑一下\x01",
            "登山路线比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C8")

    label("loc_2140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_21BA")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "听说那些犯人终于被抓住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样我的同伴\x01",
            "也可以稍微放心些了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我的心情也一下子爽快了许多。\x02",
    )

    CloseMessageWindow()
    Jump("loc_26C8")

    label("loc_21BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_221C")

    ChrTalk(
        0xFE,
        (
            "难不成，\x01",
            "抢劫犯和纵火犯是同一个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这种行为太没有人性了。\x01",
            "真让人怒火中烧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C8")

    label("loc_221C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2278")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "登山的机会以后还是会有的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于阿尔宾说的那番话，\x01",
            "我也没有异议。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C8")

    label("loc_2278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_22E3")

    ChrTalk(
        0xFE,
        (
            "嗯，天气很不错，\x01",
            "不久之后就可以\x01",
            "向古罗尼连峰挑战了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来我们这么等着\x01",
            "还是有价值的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C8")

    label("loc_22E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_2310")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "看来发生了什么大事呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C8")

    label("loc_2310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2490")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_242B")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "古罗尼连峰就像半岛一样，\x01",
            "向瓦雷利亚湖中突起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为标高相当高，\x01",
            "要登山必须装备得非常完善才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "根据天气和季节不同，\x01",
            "必须要慎重考虑，\x01",
            "选择路线也是非常重要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在我们应该等到\x01",
            "山里的天气恢复了再行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然这里很晴朗，\x01",
            "但山里天气好像很糟糕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_248D")

    label("loc_242B")


    ChrTalk(
        0xFE,
        (
            "要登古罗尼连蜂\x01",
            "必须要有完善的装备和心理准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在我们只能等到\x01",
            "山里的天气恢复了再行动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_248D")

    Jump("loc_26C8")

    label("loc_2490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2570")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2517")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "已经购买了充足的干粮，\x01",
            "装备也准备齐全了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "上一次由于气候恶劣只能作罢，\x01",
            "这次我一定要踏遍这连绵的山峦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_256D")

    label("loc_2517")


    ChrTalk(
        0xFE,
        "众所周知，山里面是很危险的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的伙伴阿尔宾\x01",
            "如果能学得\x01",
            "更加慎重点就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_256D")

    Jump("loc_26C8")

    label("loc_2570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_2642")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2614")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "男孩子啊……\x01",
            "长什么样子的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F唔，戴着帽子的，\x01",
            "样子很淘气任性的孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "非常抱歉，我没有看到过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F这样啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_263F")

    label("loc_2614")


    ChrTalk(
        0xFE,
        (
            "男孩子啊……\x01",
            "非常抱歉，我没有看到过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_263F")

    Jump("loc_26C8")

    label("loc_2642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_26C8")

    ChrTalk(
        0xFE,
        "我们就是所谓的登山家。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "玛诺利亚村一直被认为是\x01",
            "古罗尼连峰的登山入口……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我们要在这里做好准备，向这座山发起挑战。\x02",
    )

    CloseMessageWindow()

    label("loc_26C8")

    TalkEnd(0x13)
    Return()

    # Function_8_20DD end

    def Function_9_26CC(): pass

    label("Function_9_26CC")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_26D9")
    Jump("loc_2AB5")

    label("loc_26D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_28B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2875")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#750F啊，是你们几个……\x02\x03",
            "我从旅馆的人那里听说了。\x01",
            "你们已经把那些犯人抓住了吧。\x02\x03",
            "总是给你们添麻烦，\x01",
            "我该怎么感谢你们才好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F您、您这么说，\x01",
            "我们会不好意思的。\x02\x03",
            "#008F而且……\x02\x03",
            "#503F（嗯……现在还是不要\x01",
            "　把实情说出来比较好啊……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……我们还要报告工作情况，\x01",
            "所以现在要先回卢安。\x02\x03",
            "犯人们如今在\x01",
            "卡露娜小姐的严密监视之下，\x01",
            "请你们放心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#750F嗯，真的非常感谢你们……\x02",
    )

    CloseMessageWindow()
    Jump("loc_28B4")

    label("loc_2875")


    ChrTalk(
        0xFE,
        (
            "#750F最近我总是给你们添麻烦，\x01",
            "我该怎么感谢你们才好呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28B4")

    Jump("loc_2AB5")

    label("loc_28B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_28DF")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特蕾莎院长安静地睡着。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_2AB5")

    label("loc_28DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_29C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2979")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#750F哎呀，是你们几个啊……\x02\x03",
            "这段时间真的帮了我们大忙啊。\x01",
            "　\x02\x03",
            "玛诺利亚村的村民\x01",
            "也对我们非常好……\x02\x03",
            "#751F真的要感谢大家才行。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C1")

    label("loc_2979")


    ChrTalk(
        0xFE,
        (
            "#750F这段时间真的帮了我们大忙啊。\x01",
            "　\x02\x03",
            "#751F真的要感谢大家才行。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C1")

    Jump("loc_2AB5")

    label("loc_29C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A53")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#756F……我已经听玛丽说了。\x02\x03",
            "怎么会这样呢……\x01",
            "那孩子竟然听到了那件事……\x02\x03",
            "#752F求求你们了。\x01",
            "请一定要把克拉姆带回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB5")

    label("loc_2A53")


    ChrTalk(
        0xFE,
        (
            "#756F怎么会这样呢……\x01",
            "那孩子竟然听到了那件事……\x02\x03",
            "#752F求求你们了。\x01",
            "请一定要把克拉姆带回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB5")

    TalkEnd(0xFE)
    Return()

    # Function_9_26CC end

    def Function_10_2AB9(): pass

    label("Function_10_2AB9")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2AC6")
    Jump("loc_2B5D")

    label("loc_2AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_2B18")

    ChrTalk(
        0xFE,
        (
            "#770F啊，是姐姐你们啊！\x02\x03",
            "你们已经把那些家伙抓住了吧？\x01",
            "　\x02\x03",
            "真厉害！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5D")

    label("loc_2B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_2B5D")

    ChrTalk(
        0xFE,
        (
            "#770F约修亚哥哥……\x02\x03",
            "我，一定要成为\x01",
            "像哥哥一样强的人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B5D")

    TalkEnd(0xE)
    Return()

    # Function_10_2AB9 end

    def Function_11_2B61(): pass

    label("Function_11_2B61")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2B6E")
    Jump("loc_2C34")

    label("loc_2B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_2BB7")

    ChrTalk(
        0xFE,
        (
            "清早的时候\x01",
            "老师终于醒过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嘿嘿嘿，真是太好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C34")

    label("loc_2BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_2C0B")

    ChrTalk(
        0xFE,
        (
            "大家终于都\x01",
            "稍微镇静下来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来只要等\x01",
            "老师醒过来就行了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C34")

    label("loc_2C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2C34")

    ChrTalk(
        0xFE,
        "大姐姐，克拉姆就拜托你们了！\x02",
    )

    CloseMessageWindow()

    label("loc_2C34")

    TalkEnd(0xC)
    Return()

    # Function_11_2B61 end

    def Function_12_2C38(): pass

    label("Function_12_2C38")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2C45")
    Jump("loc_2CB8")

    label("loc_2C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_2C78")

    ChrTalk(
        0xFE,
        (
            "哈～一旦放心下来，\x01",
            "肚子就觉得饿了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB8")

    label("loc_2C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_2C94")

    ChrTalk(
        0xFE,
        "呜……呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CB8")

    label("loc_2C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2CB8")

    ChrTalk(
        0xFE,
        (
            "克拉姆他\x01",
            "突然怎么了啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CB8")

    TalkEnd(0xB)
    Return()

    # Function_12_2C38 end

    def Function_13_2CBC(): pass

    label("Function_13_2CBC")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2CC9")
    Jump("loc_2D55")

    label("loc_2CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_2CEE")

    ChrTalk(
        0xFE,
        (
            "哇～\x01",
            "老师醒过来了～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D55")

    label("loc_2CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_2D14")

    ChrTalk(
        0xFE,
        "老师……不会有事吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D55")

    label("loc_2D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2D55")

    ChrTalk(
        0xFE,
        (
            "克拉姆他啊，\x01",
            "在吃布丁的时候\x01",
            "不知道又在想些什么事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D55")

    TalkEnd(0xD)
    Return()

    # Function_13_2CBC end

    def Function_14_2D59(): pass

    label("Function_14_2D59")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2DDF")

    ChrTalk(
        0xFE,
        (
            "在事情了结之前，\x01",
            "这些属于特蕾莎院长的捐款\x01",
            "就先由我来暂代保管吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次我一定会保护好的，\x01",
            "所以你们就安心出发吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_2DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_2E00")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "卡露娜安静地睡着。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2E00")

    TalkEnd(0x11)
    Return()

    # Function_14_2D59 end

    def Function_15_2E04(): pass

    label("Function_15_2E04")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_2E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E66")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "孤儿院的大家\x01",
            "都一边哭一边跑回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么回事？\x01",
            "是谁欺负他们了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2E66")


    ChrTalk(
        0xFE,
        "是谁欺负他们了？\x02",
    )

    CloseMessageWindow()

    label("loc_2E7C")

    TalkEnd(0x14)
    Return()

    # Function_15_2E04 end

    def Function_16_2E80(): pass

    label("Function_16_2E80")

    EventBegin(0x0)
    OP_6D(-50180, 0, -790, 0)
    OP_6B(2800, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, -52390, 0, 510, 90)
    SetChrPos(0xB, -50850, 0, 180, 315)
    SetChrPos(0xD, -50850, 0, 1400, 225)
    SetChrPos(0xC, -50570, 0, -2840, 45)
    SetChrPos(0xE, -49420, 0, -2280, 225)
    SetChrPos(0x101, -46270, 0, -1540, 270)
    SetChrPos(0x102, -46100, 0, -760, 270)
    SetChrPos(0x136, -47050, 0, -1030, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x136,
        "#043F老师，孩子们……！\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xD, 255)
    OP_4A(0xC, 255)
    OP_4A(0xE, 255)

    def lambda_300A():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_300A)

    def lambda_3018():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3018)

    def lambda_3026():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3026)

    def lambda_3034():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3034)

    def lambda_3042():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3042)
    Sleep(400)

    ChrTalk(
        0xE,
        "#774F啊，科洛丝姐姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "姐姐来了啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_3086():
        OP_6D(-50670, 0, -380, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3086)

    def lambda_309E():
        OP_8F(0xFE, 0xFFFF41A6, 0x0, 0xFFFFFE8E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_309E)
    Sleep(100)

    def lambda_30BE():
        OP_8E(0xFE, 0xFFFF3DD2, 0x0, 0x21C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_30BE)
    Sleep(100)

    def lambda_30DE():
        OP_8E(0xFE, 0xFFFF3D5A, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_30DE)

    def lambda_30F9():
        OP_8E(0xFE, 0xFFFF3FD0, 0x0, 0xFFFFFB50, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_30F9)
    Sleep(100)

    def lambda_3119():
        OP_8E(0xFE, 0xFFFF4322, 0x0, 0xFFFFFBD2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3119)
    WaitChrThread(0xE, 0x2)
    TurnDirection(0xE, 0x136, 400)

    ChrTalk(
        0x136,
        (
            "#042F#2P大家……\x01",
            "都没受伤吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1P嗯，没事！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "嘿嘿。\x01",
            "波利也没事～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#048F#2P太好了……\x01",
            "真是太好了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x4)
    OP_8E(0xA, 0xFFFF394A, 0x0, 0xB4, 0x7D0, 0x0)

    ChrTalk(
        0xA,
        (
            "#750F呵呵……\x01",
            "你能来真是太好了。\x02\x03",
            "#751F艾丝蒂尔和约修亚\x01",
            "也一起来了啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_321B():

        label("loc_321B")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_321B")

    QueueWorkItem2(0xA, 1, lambda_321B)

    def lambda_322C():

        label("loc_322C")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_322C")

    QueueWorkItem2(0xB, 1, lambda_322C)

    def lambda_323D():

        label("loc_323D")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_323D")

    QueueWorkItem2(0xD, 1, lambda_323D)

    def lambda_324E():

        label("loc_324E")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_324E")

    QueueWorkItem2(0xC, 1, lambda_324E)

    def lambda_325F():

        label("loc_325F")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_325F")

    QueueWorkItem2(0xE, 1, lambda_325F)

    def lambda_3270():

        label("loc_3270")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3270")

    QueueWorkItem2(0x136, 1, lambda_3270)

    def lambda_3281():
        OP_8E(0xFE, 0xFFFF4124, 0x0, 0xFFFFF498, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3281)
    Sleep(500)

    def lambda_32A1():
        OP_8E(0xFE, 0xFFFF441C, 0x0, 0xFFFFF5F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_32A1)
    WaitChrThread(0x101, 0x2)

    def lambda_32C1():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_32C1)
    WaitChrThread(0x102, 0x2)

    def lambda_32D4():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32D4)
    Sleep(500)
    OP_44(0xA, 0xFF)

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "有人通知了游击士协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是来调查的，\x01",
            "顺便和科洛丝一起来看望你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F是吗……\x01",
            "谢谢你们的关心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#772F#2P你说来调查……\x01",
            "是来调查昨天的火灾吗？\x02\x03",
            "发现什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F该怎么说好呢……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚\x01",
            "为难地互相交换了一下眼神。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x136, 0x101, 400)
    OP_62(0x136, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x136)
    OP_44(0x136, 0xFF)
    TurnDirection(0x136, 0xB, 400)
    Sleep(200)
    TurnDirection(0x136, 0x102, 400)

    ChrTalk(
        0x136,
        (
            "#040F好了，孩子们。\x01",
            "大家的肚子都饿了吧？\x02\x03",
            "我还没有吃早饭呢，\x01",
            "正准备到下面食堂吃点东西。\x02\x03",
            "#041F所以呢，\x01",
            "今天就请大家吃点好东西好吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34F2():

        label("loc_34F2")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_34F2")

    QueueWorkItem2(0x101, 1, lambda_34F2)

    def lambda_3503():

        label("loc_3503")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_3503")

    QueueWorkItem2(0x102, 1, lambda_3503)
    Sleep(50)

    def lambda_3519():

        label("loc_3519")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_3519")

    QueueWorkItem2(0xA, 1, lambda_3519)
    OP_44(0xB, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    Sleep(50)

    def lambda_353F():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_353F)

    def lambda_354D():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_354D)
    Sleep(50)

    def lambda_3560():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3560)

    def lambda_356E():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_356E)

    ChrTalk(
        0xB,
        "#1P哎？真的！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "波利要吃布丁！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#773F#3P可、可是姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#1P…………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 400)

    ChrTalk(
        0xC,
        "#1P走吧，克拉姆。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xC, 400)

    ChrTalk(
        0xE,
        "#774F#4P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1P别啰嗦了，\x01",
            "快点过来啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1P科洛丝姐姐，\x01",
            "我们快点下去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#048F呵呵，好呢。\x02",
    )

    CloseMessageWindow()
    OP_43(0x136, 0x2, 0x0, 0x11)
    OP_43(0xE, 0x2, 0x0, 0x12)
    OP_43(0xC, 0x2, 0x0, 0x13)
    OP_43(0xB, 0x2, 0x0, 0x14)
    OP_43(0xD, 0x2, 0x0, 0x15)

    def lambda_3691():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_3691)
    Sleep(600)

    def lambda_36B1():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_36B1)
    Sleep(50)

    def lambda_36D1():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_36D1)
    Sleep(200)

    def lambda_36F1():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_36F1)
    Sleep(300)

    def lambda_3711():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3711)
    WaitChrThread(0x136, 0x1)
    SetChrFlags(0x136, 0x80)
    WaitChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    WaitChrThread(0xD, 0x1)
    SetChrFlags(0xD, 0x80)
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xA, 0xFF)

    ChrTalk(
        0x101,
        (
            "#007F呼……还好没事。\x02\x03",
            "调查的事还是不要\x01",
            "让孩子们知道好一些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P是啊。\x02\x03",
            "#010F不过，那个叫玛丽的孩子\x01",
            "似乎已经察觉到我们的意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#751F呵呵，有这样懂事的孩子，\x01",
            "我自己也觉得很欣慰啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#750F对了，\x01",
            "你们刚才说是来调查。\x02\x03",
            "想知道些什么，请随便问吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 0)
    Sleep(100)
    TurnDirection(0x102, 0xA, 0)

    ChrTalk(
        0x102,
        "#012F#4P多谢您的配合。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯，那么……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -49200, 0, -1200, 0)
    SetChrPos(0x102, -50100, 0, -990, 45)
    SetChrPos(0xA, -49670, 0, 200, 180)
    OP_6D(-50810, 0, 340, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "首先，根据我们在火灾现场\x01",
            "调查得到的结果来看……\x02\x03",
            "这次火灾并不是意外， \x01",
            "人为纵火的可能性极高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#754F#2P是吗……果然啊……\x02\x03",
            "我也觉得着火的时候\x01",
            "屋外的情况确实有点古怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F我们想问问您……\x01",
            "您觉得有什么可疑的人物吗？\x02\x03",
            "也就是说， \x01",
            "谁会有做这种事的动机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#757F#2P……我不清楚……\x02\x03",
            "我们几乎没有什么钱财，\x01",
            "印象中也完全没和别人结怨……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F也就是说，\x01",
            "犯人的动机既不是抢劫也不是报复吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F这样的话，虽然很不愿相信，\x01",
            "但有可能是纯粹的恶作剧犯罪。\x02\x03",
            "事件发生前后，\x01",
            "有什么不寻常的事情吗？\x02\x03",
            "比如说有没有\x01",
            "陌生人在孤儿院附近晃荡……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#756F#2P这个嘛……\x02\x03",
            "除了白天见到了你们之外，\x01",
            "就没有什么特别的了……\x02\x03",
            "#757F……也应该跟那个人无关的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F那个人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#754F#2P在我们将要逃出\x01",
            "被大火包围的屋子的时候……\x02\x03",
            "天花板上的梁柱突然掉了下来，\x01",
            "挡住了通往门口的路。\x02\x03",
            "#750F但就在那个时候，\x01",
            "有人打破了门，冲了进来……\x02\x03",
            "那个人挪开了梁柱，\x01",
            "把我和孩子们救了出去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F还、还有这么一回事啊。\x02\x03",
            "那人是玛诺利亚的村民吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#756F#2P那个人把我们救出来之后，\x01",
            "说去村子里叫人过来，\x01",
            "连名字都没有留下就离开了……\x02\x03",
            "我问了玛诺利亚的村民，\x01",
            "不过似乎没人知道那个人是谁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F……这有点可疑。\x02\x03",
            "半夜三更出现在孤儿院附近，\x01",
            "怎么想也有点太过蹊跷了吧。\x02\x03",
            "那是个什么样的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F#2P是个穿着象牙色外套，\x01",
            "不到３０岁的青年男子。\x02\x03",
            "而且，还有一头耀眼的银发。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F银发……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F#2P嗯，虽然看样子还很年轻，\x01",
            "但那深邃的眼神让人感到他饱经沧桑。\x02\x03",
            "看起来不像是坏人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F虽然感觉不是普通人，\x01",
            "但他救了人这点的确是事实……\x02\x03",
            "听起来不像是犯人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 300)

    ChrTalk(
        0x101,
        (
            "#002F#4P约修亚？\x02\x03",
            "怎么了，为什么发起呆来了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 200)

    ChrTalk(
        0x102,
        (
            "#013F#1P没什么……\x02\x03",
            "你们说得也对， \x01",
            "也许是哪里过来的游击士也说不定……\x02\x03",
            "#015F总之这个人的事\x01",
            "还是先别下定论的好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#4P啊，嗯……\x02",
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x136,
        "#1P……打扰了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0x136, 0xA, 0)
    ClearChrFlags(0x136, 0x80)

    def lambda_401F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_401F)

    def lambda_402D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_402D)

    def lambda_403B():
        OP_6D(-49000, 0, -520, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_403B)

    def lambda_4053():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 3, lambda_4053)
    OP_8E(0x136, 0xFFFF4818, 0x0, 0xFFFFFCAE, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#000F啊，科洛丝？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那些孩子怎么样了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F呵呵……\x01",
            "大家都在下面吃蛋糕呢。\x02\x03",
            "#040F对了，老师。\x01",
            "有两位客人来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#753F客人？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xF, -44560, 0, -1000, 0)
    SetChrPos(0x10, -44420, 0, -1440, 0)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xF, 0xA, 0)

    NpcTalk(
        0xF,
        "男性的声音",
        "#1P打扰了。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x136, 0xFFFF44B2, 0x0, 0xFFFFF8D0, 0x7D0, 0x0)

    def lambda_4180():

        label("loc_4180")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_4180")

    QueueWorkItem2(0x136, 1, lambda_4180)

    def lambda_4191():

        label("loc_4191")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_4191")

    QueueWorkItem2(0x101, 1, lambda_4191)

    def lambda_41A2():

        label("loc_41A2")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_41A2")

    QueueWorkItem2(0x102, 1, lambda_41A2)

    def lambda_41B3():

        label("loc_41B3")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_41B3")

    QueueWorkItem2(0xA, 1, lambda_41B3)
    ClearChrFlags(0xF, 0x80)

    def lambda_41C9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_41C9)

    def lambda_41DB():
        OP_8E(0xFE, 0xFFFF4926, 0x0, 0xFFFFFD76, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_41DB)
    Sleep(500)
    ClearChrFlags(0x10, 0x80)

    def lambda_4200():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_4200)

    def lambda_4212():
        OP_8E(0xFE, 0xFFFF4DD6, 0x0, 0xFFFFFA60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4212)
    WaitChrThread(0x10, 0x1)

    ChrTalk(
        0x101,
        "#004F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F戴尔蒙市长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#660F#2P啊，昨天碰到的\x01",
            "两位游击士也在啊。\x02\x03",
            "不愧是嘉恩，\x01",
            "这么快就安排人手过来了。\x02\x03",
            "#664F对了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42C3():
        OP_8E(0xFE, 0xFFFF443A, 0x0, 0xFA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_42C3)
    Sleep(500)

    def lambda_42E3():
        OP_8E(0xFE, 0xFFFF4796, 0x0, 0xFFFFFC68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_42E3)
    WaitChrThread(0xF, 0x1)
    TurnDirection(0xF, 0xA, 400)
    WaitChrThread(0x10, 0x1)

    ChrTalk(
        0xF,
        (
            "#660F#4P好久不见了，特蕾莎院长。\x02\x03",
            "我刚刚接到报告，\x01",
            "所以就急急忙忙赶了过来。\x02\x03",
            "不过，幸好你们都没事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F谢谢您，市长。\x02\x03",
            "要您在百忙之中抽出时间过来，\x01",
            "我真是感到过意不去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#660F#4P没什么，这也是身为\x01",
            "卢安市长所应尽的职责啊。\x02\x03",
            "#664F而且，虽然不知道是何人所为，\x01",
            "总之这种行径绝不能饶恕。\x02\x03",
            "竟然灭绝人性地把\x01",
            "约瑟夫心爱的屋子给……\x02\x03",
            "#662F简直令人惋惜和气愤啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#754F不……\x02\x03",
            "只要孩子们得救了，\x01",
            "我想他也会觉得欣慰吧。\x02\x03",
            "#757F唯一遗憾的是，\x01",
            "他的遗物全都被烧毁了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043F特蕾莎老师……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 225, 300)

    ChrTalk(
        0xF,
        (
            "#662F两位游击士，\x01",
            "案件有眉目了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F调查才刚开始，\x01",
            "所以还不能下明确的结论……\x02\x03",
            "不过，经过初步的判断，\x01",
            "也存在着恶作剧性质的犯罪可能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#664F是吗……\x01",
            "真是令人遗憾啊。\x02\x03",
            "在这美丽的卢安，\x01",
            "竟然也有如此丑恶的人存在。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 315, 400)

    ChrTalk(
        0x10,
        "#673F市长，请恕我失礼……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(
        0xF,
        "#660F嗯，什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671F这次的火灾……\x01",
            "该不会是他们几个做的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#662F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F等、等等！\x01",
            "『他们几个』是指谁？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 300)

    ChrTalk(
        0x10,
        (
            "#671F你们几位昨天不是也被他们缠上了吗。\x02\x03",
            "就是聚集在卢安仓库那一带的\x01",
            "那些地痞流氓啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F是他们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F恕我多言……\x01",
            "为什么您会怀疑他们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671F昨天的事也是这样……\x01",
            "那帮家伙总是跟市长作对，\x01",
            "整天惹是生非，唯恐天下不乱。\x02\x03",
            "甚至以给市长惹麻烦为乐。\x01",
            "　\x02\x03",
            "#673F所以就对和市长\x01",
            "交情很深的特蕾莎院长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#665F基尔巴特！\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 315, 400)

    ChrTalk(
        0x10,
        "#676F是、是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#663F不要光凭猜测就\x01",
            "如此口无遮拦地妄下判断。\x02\x03",
            "这是重大的犯罪。\x01",
            "绝不能冤枉任何人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#676F十、十分抱歉。\x01",
            "请恕我考虑不周……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#664F用不着你多嘴，\x01",
            "这两位游击士也\x01",
            "一定会把犯人缉捕归案的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 225, 400)

    ChrTalk(
        0xF,
        "#660F我这样说没问题吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，包在我们身上！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们一定尽力而为。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#661F嗯，这回答真让人放心。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xA, 400)
    Sleep(500)
    OP_8C(0x10, 270, 0)

    ChrTalk(
        0xF,
        (
            "#660F#4P对了，特蕾莎院长……\x01",
            "我有件事想和你谈谈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#753F什么事呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#660F#4P孤儿院现在毁了，\x01",
            "从今以后你有什么打算？\x02\x03",
            "房子重建需要一段时间，\x01",
            "而且需要花费的金钱也不少吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#757F…………………………\x02\x03",
            "老实说，我也不知该如何是好啊。\x02\x03",
            "我这里虽然有一点积蓄，\x01",
            "但要重建孤儿院的话根本……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F院长老师……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043F……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#664F#4P果然如此吗……\x02\x03",
            "#660F要不这样吧。\x01",
            "你听听我个人的提议如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#750F……是什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#660F#4P其实是这样的，\x01",
            "格兰赛尔有我们戴尔蒙家的别墅。\x02\x03",
            "我平时只是偶尔去住一下，\x01",
            "所以那里一直都是闲置着的……\x02\x03",
            "可以的话，你就和孩子们\x01",
            "搬到我那别墅住一段时间如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#753F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#660F#4P当然，院长你也不必\x01",
            "为房租这类无关痛痒的事情和我客气。\x02\x03",
            "直到重建的事有眉目为止，\x01",
            "随便你们在那里住多久都没问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#757F但、但这也太麻烦您了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#661F#4P反正那屋子也没人住。\x02\x03",
            "你要是觉得过意不去……\x01",
            "嗯，那不妨就帮我看管房子吧。\x02\x03",
            "当然，我会付报酬的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#756F市长……\x02\x03",
            "…………………………\x02\x03",
            "#757F能让我考虑一下吗？\x02\x03",
            "真的很感谢您的提议，\x01",
            "不过实在发生了太多事情，\x01",
            "所以我现在很难一下子给您答复……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#664F#4P这也难怪……\x01",
            "你就先好好休息一下吧。\x02\x03",
            "#660F我们这就告辞了。\x02\x03",
            "如果你考虑好了，\x01",
            "可以随时和我联系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F好的……\x01",
            "真的非常感谢您。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(
        0xF,
        "#660F基尔巴特，走吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)

    ChrTalk(
        0x10,
        "#670F是！\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10, 0xFFFF4818, 0x0, 0xFFFFF9B6, 0x7D0, 0x0)
    OP_8C(0x10, 0, 400)

    def lambda_4EA2():
        OP_8E(0xFE, 0xFFFF4F20, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4EA2)
    WaitChrThread(0xF, 0x1)

    def lambda_4EC2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_4EC2)

    def lambda_4ED4():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4ED4)
    Sleep(300)

    def lambda_4EF4():
        OP_8E(0xFE, 0xFFFF4F20, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4EF4)
    WaitChrThread(0x10, 0x1)

    def lambda_4F14():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_4F14)

    def lambda_4F26():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4F26)
    WaitChrThread(0xF, 0x1)
    SetChrFlags(0xF, 0x80)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)

    def lambda_4F5F():
        OP_6D(-49600, 0, -480, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F5F)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#008F哈～真是吃了一惊。\x02\x03",
            "原来除了梅贝尔市长之外，\x01",
            "这个戴尔蒙市长也是这么大度的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊……\x01",
            "真不愧是昔日的豪门贵族。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x136, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x136)

    def lambda_5018():
        OP_6D(-49200, 0, 70, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5018)
    OP_44(0x136, 0xFF)
    OP_8E(0x136, 0xFFFF4354, 0x0, 0xFFFFFF9C, 0x7D0, 0x0)
    TurnDirection(0x136, 0xA, 400)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_505B():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_505B)

    def lambda_5069():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5069)
    TurnDirection(0xA, 0x136, 400)

    ChrTalk(
        0x136,
        (
            "#049F老师，市长的提议，\x01",
            "您打算怎么回应呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#754F是啊……\x01",
            "你又是怎么想的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#049F…………………………\x02\x03",
            "#049F从常理来说，\x01",
            "我觉得自然是应该接受的。\x02\x03",
            "可是……\x01",
            "你们要是去了王都的话……\x02\x03",
            "#043F不……没什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F呵呵，我知道你向来\x01",
            "都是个很明白事理的孩子。\x02\x03",
            "没事的，科洛丝。\x01",
            "有什么心里话尽管说出来好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#043F…………………………\x02\x03",
            "#049F要是你们去了王都，\x01",
            "那块香草田就会没人打理……\x02\x03",
            "而且……而且……\x02\x03",
            "#047F我总觉得老师和约瑟夫叔叔\x01",
            "疼爱我照顾我的那段回忆\x01",
            "也会随之消失掉似的……\x02\x03",
            "对不起……\x01",
            "我说了一些任性的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F呵呵，其实我也有同样的感受。\x02\x03",
            "在那里，充满了许多\x01",
            "孩子们和我丈夫的珍贵回忆。\x02\x03",
            "但是我觉得，\x01",
            "和这些回忆相比起来，\x01",
            "如何生存下去才是更加重要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#049F是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F嗯……\x01",
            "这段时间我就会做出决定的。\x02\x03",
            "你还是继续\x01",
            "专心准备学园祭的事情吧。\x02\x03",
            "那些孩子也都\x01",
            "很期待那天的到来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#048F……是。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 300)

    ChrTalk(
        0xA,
        (
            "#750F艾丝蒂尔，约修亚。\x02\x03",
            "这么说虽然很不好意思……\x01",
            "不过调查的事情，还是要拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 0)
    Sleep(100)
    TurnDirection(0x102, 0xA, 0)

    ChrTalk(
        0x102,
        "#010F请放心交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F我们一定会捉到犯人，\x01",
            "绝对不会让他们逍遥法外的！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x3B, 0x1, 0x80)
    OP_28(0x3B, 0x1, 0x100)
    OP_28(0x3B, 0x1, 0x200)
    OP_28(0x3B, 0x1, 0x400)
    OP_28(0x3C, 0x4, 0x2)
    OP_28(0x3C, 0x4, 0x4)
    OP_28(0x3C, 0x1, 0x1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2E80 end

    def Function_17_54C4(): pass

    label("Function_17_54C4")

    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_9F(0x136, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_17_54C4 end

    def Function_18_54DF(): pass

    label("Function_18_54DF")

    Sleep(2000)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_18_54DF end

    def Function_19_54F0(): pass

    label("Function_19_54F0")

    Sleep(2500)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_19_54F0 end

    def Function_20_5501(): pass

    label("Function_20_5501")

    Sleep(3000)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_20_5501 end

    def Function_21_5512(): pass

    label("Function_21_5512")

    Sleep(3500)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_21_5512 end

    def Function_22_5528(): pass

    label("Function_22_5528")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-50180, 0, -790, 0)
    AddParty(0x5, 0xFF)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8)
    SetChrPos(0x9, -52430, 0, 480, 0)
    SetChrPos(0xB, -50850, 0, -1230, 270)
    SetChrPos(0xD, -51540, 0, -2430, 0)
    SetChrPos(0xC, -52530, 0, -2420, 0)
    SetChrPos(0xE, -50800, 0, 1470, 270)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrPos(0x101, -44330, 0, -1080, 270)
    SetChrPos(0x102, -44330, 0, -1080, 270)
    SetChrPos(0x105, -44330, 0, -1080, 270)
    SetChrPos(0x106, -44330, 0, -1080, 270)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x9, 255)
    OP_4A(0xB, 255)
    OP_4A(0xD, 255)
    OP_4A(0xC, 255)
    OP_4A(0xE, 255)
    SetChrFlags(0x106, 0x80)
    FadeToBright(1000, 0)
    OP_43(0x105, 0x1, 0x0, 0x19)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_43(0x101, 0x1, 0x0, 0x17)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_43(0x102, 0x1, 0x0, 0x18)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x11, 0x1)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5721():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5721)

    def lambda_572F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_572F)

    def lambda_573D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_573D)

    def lambda_574B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_574B)

    def lambda_5759():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5759)

    ChrTalk(
        0xE,
        "#775F#2P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "哥哥姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F孩子们……\x02",
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x0, 0x1A)
    OP_43(0xC, 0x1, 0x0, 0x1B)
    OP_43(0xE, 0x1, 0x0, 0x1C)
    OP_43(0xD, 0x1, 0x0, 0x1D)
    WaitChrThread(0xB, 0x1)
    OP_43(0x9, 0x1, 0x0, 0x1E)

    ChrTalk(
        0xB,
        "呜哇啊啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5P好可怕啊～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F太好了……\x01",
            "大家都平安无事。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)

    def lambda_581E():

        label("loc_581E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_581E")

    QueueWorkItem2(0x102, 1, lambda_581E)

    ChrTalk(
        0x102,
        (
            "#012F对不起。\x01",
            "老师她们的状况如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "放心吧。\x01",
            "两人都没受什么伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "只是一直昏迷不醒，\x01",
            "着实让人有些担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F……容我失礼一下。\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x102, 0x4)

    def lambda_58D0():

        label("loc_58D0")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_58D0")

    QueueWorkItem2(0x101, 1, lambda_58D0)

    def lambda_58E1():

        label("loc_58E1")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_58E1")

    QueueWorkItem2(0x105, 1, lambda_58E1)

    def lambda_58F2():

        label("loc_58F2")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_58F2")

    QueueWorkItem2(0xE, 1, lambda_58F2)

    def lambda_5903():

        label("loc_5903")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_5903")

    QueueWorkItem2(0xC, 1, lambda_5903)

    def lambda_5914():

        label("loc_5914")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_5914")

    QueueWorkItem2(0x9, 1, lambda_5914)
    OP_8E(0x102, 0xFFFF42DC, 0x0, 0x5A, 0x7D0, 0x0)
    OP_8E(0x102, 0xFFFF3F6C, 0x0, 0x3CA, 0x7D0, 0x0)

    def lambda_594D():
        OP_6D(-52260, 0, -520, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_594D)
    OP_8E(0x102, 0xFFFF3896, 0x0, 0x226, 0x7D0, 0x0)
    OP_8E(0x102, 0xFFFF30EE, 0x0, 0x1F4, 0x7D0, 0x0)
    OP_8C(0x102, 0, 400)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_8C(0x102, 180, 400)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#013F果然没错……\x01",
            "看来是对她们施了催眠药。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580F催、催眠药？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F嗯，还能闻到一点刺激性气味。\x02\x03",
            "这是没有副作用的品种，\x01",
            "所以我想应该可以放心……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(
        0x101,
        "#505F嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)

    def lambda_5AA9():
        OP_6D(-50370, 0, -640, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5AA9)
    OP_8E(0x102, 0xFFFF3A80, 0x0, 0xF0, 0x7D0, 0x0)
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(
        0x101,
        (
            "#002F对了，克拉姆。\x01",
            "可以告诉我们发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#773F…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(
        0xC,
        "我来说吧……\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)

    def lambda_5B4E():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B4E)

    def lambda_5B5C():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5B5C)
    Sleep(50)

    def lambda_5B6F():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B6F)

    def lambda_5B7D():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5B7D)
    Sleep(50)

    def lambda_5B90():
        TurnDirection(0xFE, 0xC, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B90)

    def lambda_5B9E():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5B9E)
    Sleep(50)
    OP_44(0xE, 0xFF)
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#3P我们……\x01",
            "和游击士姐姐一起\x01",
            "在海道上走着走着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3P就在那时，\x01",
            "突然出现了几个蒙面的怪人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3P游击士姐姐\x01",
            "虽然想把他们赶走……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3P但是我们很快就被\x01",
            "那几个蒙面的怪人包围了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3P老师也为了保护我们，\x01",
            "跟那帮怪人纠缠了起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3P……然后就……呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F好了好了，大家都吓坏了吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#773F……那帮家伙……\x01",
            "还把老师身上的信封给抢走了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D38():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D38)
    Sleep(50)

    def lambda_5D4B():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5D4B)
    Sleep(50)

    def lambda_5D5E():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D5E)
    Sleep(50)

    def lambda_5D71():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5D71)
    Sleep(50)
    TurnDirection(0x102, 0xE, 400)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#775F我……\x01",
            "我想把信封抢回来的，\x01",
            "但一下子就被他们踢倒了……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xE, 0xFF)
    TurnDirection(0xE, 0x102, 300)

    ChrTalk(
        0xE,
        (
            "#777F约修亚哥哥……\x01",
            "我……没能保护好老师……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#5P……没这回事。\x02\x03",
            "只要你们没事，\x01",
            "老师就一定已经很高兴了。\x02\x03",
            "#012F所以……不要责备自己了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#777F但是……\x01",
            "我……我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "呜……呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F不可原谅……！\x01",
            "到底是什么人干的好事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#047F#2P………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#042F#2P现在可以确定的是……\x01",
            "那些蒙面人的犯案手段相当老练。\x02\x03",
            "连游击士都不是他们对手，\x01",
            "甚至还被他们用催眠药弄晕了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F77():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F77)

    def lambda_5F85():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5F85)

    def lambda_5F93():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5F93)
    TurnDirection(0xE, 0x105, 400)

    ChrTalk(
        0x101,
        "#004F科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F#2P另外还有一点……\x01",
            "我认为这是有计划的犯罪。\x02\x03",
            "目标当然是\x01",
            "老师身上的那大批捐款……\x02\x03",
            "纵火烧孤儿院\x01",
            "恐怕同样是这些人的所为吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#1P嗯，这种可能性很高。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F科洛丝……\x01",
            "看来你终于镇定下来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F#2P是的……\x01",
            "因为再沮丧也于事无补。\x02\x03",
            "总之现在要尽快\x01",
            "找到犯人的行踪才行……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x106, -44560, 0, -1160, 0)
    TurnDirection(0x106, 0x105, 0)
    ClearChrFlags(0x106, 0x80)

    NpcTalk(
        0x106,
        "青年的声音",
        "#1P……我也有同感。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    SetChrChipByIndex(0x106, 15)

    def lambda_617B():
        OP_6D(-49600, 0, -620, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_617B)
    ClearChrFlags(0x106, 0x80)

    def lambda_6198():
        OP_8E(0xFE, 0xFFFF4598, 0x0, 0xFFFFFD08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_6198)

    def lambda_61B3():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_61B3)

    def lambda_61C1():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_61C1)

    def lambda_61CF():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_61CF)

    def lambda_61DD():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_61DD)

    def lambda_61EB():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_61EB)

    def lambda_61F9():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_61F9)

    def lambda_6207():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6207)

    def lambda_6215():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6215)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x106, 0x1)

    ChrTalk(
        0x101,
        "#004F啊～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F阿加特兄……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F事情我在协会听说了。\x02\x03",
            "看来这次的情况\x01",
            "还满棘手的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F别、别说得好像事不关己一样！\x02\x03",
            "连卡露娜姐姐都\x01",
            "中了他们的暗算啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F我知道……\x01",
            "别大呼小叫的。\x02\x03",
            "#050F卡露娜是一流的游击士。\x01",
            "看来是帮相当危险的家伙啊。\x02\x03",
            "把事情经过给我说一遍吧，\x01",
            "说个大概就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F好的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚向阿加特说明了\x01",
            "包括捐款被抢在内一系列事情的经过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x106,
        (
            "#552F嗯，这样啊……\x01",
            "不过事情有点古怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F古怪？什么古怪？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F啊啊，其实是……\x02\x03",
            "『渡鸦帮』的那帮蠢货\x01",
            "已经离开了港口的仓库。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F这、这就是说……\x02\x03",
            "#005F果然是这帮家伙\x01",
            "袭击特蕾莎院长他们吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F不，这还不好说。\x02\x03",
            "我觉得以他们的力量\x01",
            "根本不足以做卡露娜小姐的对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F这倒也是……\x02\x03",
            "那帮家伙只会耍嘴皮子，\x01",
            "根本就没什么真功夫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F我盯了他们一阵子，\x01",
            "本来还以为他们变老实了……\x02\x03",
            "谁知道那些蠢货\x01",
            "今天突然不见了……\x02\x03",
            "刚好又在这时候发生了这事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F先不说他们是不是犯人，\x01",
            "但肯定跟这件事脱不了关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F是啊……\x01",
            "不过现在还不是研究这个的时候。\x02\x03",
            "你们两个，跟我一起走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F什么呀，忽然冒出这一句……\x02\x03",
            "#002F到底要去哪里啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#551F你还真是迟钝。\x01",
            "当然是去犯罪现场的海道了。\x02\x03",
            "先不管这件事\x01",
            "是不是那帮蠢货干的……\x02\x03",
            "#054F总之要尽量多搜集些线索，\x01",
            "找到犯人的行踪！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F明白了，我们跟你一起去。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_5528 end

    def Function_23_6758(): pass

    label("Function_23_6758")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4070, 0x0, 0xFFFFFA6A, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_23_6758 end

    def Function_24_6779(): pass

    label("Function_24_6779")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF430E, 0x0, 0xFFFFFD44, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_24_6779 end

    def Function_25_679A(): pass

    label("Function_25_679A")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF3EA4, 0x0, 0xFFFFFE52, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_25_679A end

    def Function_26_67BB(): pass

    label("Function_26_67BB")

    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3C42, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_26_67BB end

    def Function_27_67E9(): pass

    label("Function_27_67E9")

    Sleep(150)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3F8A, 0x0, 0xFFFFF7B8, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_27_67E9 end

    def Function_28_681C(): pass

    label("Function_28_681C")

    Sleep(100)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3F12, 0x0, 0x10E, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_28_681C end

    def Function_29_684F(): pass

    label("Function_29_684F")

    Sleep(50)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3D28, 0x0, 0xFFFFFAB0, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_29_684F end

    def Function_30_6882(): pass

    label("Function_30_6882")

    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    OP_8E(0x9, 0xFFFF3922, 0x0, 0x15E, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF3E4A, 0x0, 0x3F2, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF4336, 0x0, 0x35C, 0x7D0, 0x0)
    TurnDirection(0x9, 0x102, 400)
    Return()

    # Function_30_6882 end

    SaveToFile()

Try(main)
