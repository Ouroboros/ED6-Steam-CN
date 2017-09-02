from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4270   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4270.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '艾莉茜雅女王',                         # 9
        '杜南公爵',                             # 10
        '管家菲利普',                           # 11
        '特务兵',                               # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '特务兵',                               # 15
        '茜亚',                                 # 16
        '\u3000',                               # 17
        '\u3000',                               # 18
        '\u3000',                               # 19
        '\u3000',                               # 20
        '\u3000',                               # 21
        '科洛丝',                               # 22
        '尤莉亚中尉',                           # 23
        '希尔丹夫人',                           # 24
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02230 ._CH',             # 01
        'ED6_DT07/CH02240 ._CH',             # 02
        'ED6_DT07/CH00000 ._CH',             # 03
        'ED6_DT07/CH00010 ._CH',             # 04
        'ED6_DT07/CH02010 ._CH',             # 05
        'ED6_DT07/CH02140 ._CH',             # 06
        'ED6_DT07/CH02470 ._CH',             # 07
        'ED6_DT07/CH01330 ._CH',             # 08
        'ED6_DT07/CH00100 ._CH',             # 09
        'ED6_DT07/CH00101 ._CH',             # 0A
        'ED6_DT07/CH00120 ._CH',             # 0B
        'ED6_DT07/CH00121 ._CH',             # 0C
        'ED6_DT07/CH00140 ._CH',             # 0D
        'ED6_DT07/CH00141 ._CH',             # 0E
        'ED6_DT07/CH02540 ._CH',             # 0F
        'ED6_DT07/CH00003 ._CH',             # 10
        'ED6_DT07/CH00013 ._CH',             # 11
        'ED6_DT07/CH02013 ._CH',             # 12
        'ED6_DT06/CH20020 ._CH',             # 13
        'ED6_DT07/CH00043 ._CH',             # 14
        'ED6_DT07/CH02093 ._CH',             # 15
        'ED6_DT07/CH02463 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH00000P._CP',             # 03
        'ED6_DT07/CH00010P._CP',             # 04
        'ED6_DT07/CH02010P._CP',             # 05
        'ED6_DT07/CH02140P._CP',             # 06
        'ED6_DT07/CH02470P._CP',             # 07
        'ED6_DT07/CH01330P._CP',             # 08
        'ED6_DT07/CH00100P._CP',             # 09
        'ED6_DT07/CH00101P._CP',             # 0A
        'ED6_DT07/CH00120P._CP',             # 0B
        'ED6_DT07/CH00121P._CP',             # 0C
        'ED6_DT07/CH00140P._CP',             # 0D
        'ED6_DT07/CH00141P._CP',             # 0E
        'ED6_DT07/CH02540P._CP',             # 0F
        'ED6_DT07/CH00003P._CP',             # 10
        'ED6_DT07/CH00013P._CP',             # 11
        'ED6_DT07/CH02013P._CP',             # 12
        'ED6_DT06/CH20020P._CP',             # 13
        'ED6_DT07/CH00043P._CP',             # 14
        'ED6_DT07/CH02093P._CP',             # 15
        'ED6_DT07/CH02463P._CP',             # 16
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638419,
        ChipIndex           = 0x13,
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
        Unknown3            = 1638419,
        ChipIndex           = 0x13,
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
        Unknown3            = 1638419,
        ChipIndex           = 0x13,
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
        Unknown3            = 1638419,
        ChipIndex           = 0x13,
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
        Unknown3            = 1703955,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -103870,
        Z                   = 200,
        Y                   = 8990,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -105240,
        Z                   = 200,
        Y                   = 7690,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -106560,
        Z                   = 200,
        Y                   = 8960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclEvent(
        X                   = 1980,
        Y                   = -1000,
        Z                   = -1550,
        Range               = -2230,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFF056,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = -1040,
        TriggerZ            = 8000,
        TriggerY            = 35960,
        TriggerRange        = 800,
        ActorX              = -1040,
        ActorZ              = 9000,
        ActorY              = 35960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3A6",          # 00, 0
        "Function_1_5BA",          # 01, 1
        "Function_2_624",          # 02, 2
        "Function_3_63A",          # 03, 3
        "Function_4_661",          # 04, 4
        "Function_5_700",          # 05, 5
        "Function_6_9AD",          # 06, 6
        "Function_7_AA6",          # 07, 7
        "Function_8_D0B",          # 08, 8
        "Function_9_F22",          # 09, 9
        "Function_10_1120",        # 0A, 10
        "Function_11_1717",        # 0B, 11
        "Function_12_5279",        # 0C, 12
        "Function_13_6965",        # 0D, 13
        "Function_14_69ED",        # 0E, 14
    )


    def Function_0_3A6(): pass

    label("Function_0_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3B4")
    OP_A3(0x3FA)
    Event(0, 10)

    label("loc_3B4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3C0"),
        (SWITCH_DEFAULT, "loc_3D6"),
    )


    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D3")
    OP_A2(0x665)
    Event(0, 12)

    label("loc_3D3")

    Jump("loc_3D6")

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_3FB")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    Jump("loc_40A")

    label("loc_3FB")

    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 3)
    SetChrChipByIndex(0x138, 4)

    label("loc_40A")

    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_4D6")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 18)
    SetChrPos(0x8, -105250, 200, 10500, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x11, -104620, 640, 8950, 0)
    SetChrPos(0x12, -105280, 640, 8300, 0)
    SetChrPos(0x10, -105350, 640, 9620, 0)
    SetChrPos(0x13, -105990, 640, 8950, 0)
    SetChrPos(0x14, -105280, 700, 9050, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -107640, 0, 7110, 90)
    Jump("loc_522")

    label("loc_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4FD")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -53080, 0, 12340, 3)
    OP_43(0xF, 0x0, 0x0, 0x2)
    Jump("loc_522")

    label("loc_4FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_507")
    Jump("loc_522")

    label("loc_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_511")
    Jump("loc_522")

    label("loc_511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_51B")
    Jump("loc_522")

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_522")

    label("loc_522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_52C")
    Jump("loc_5B9")

    label("loc_52C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_562")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, -52830, 0, 7650, 179)
    SetChrPos(0xA, -53810, 0, 7520, 79)
    Jump("loc_5B9")

    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_56C")
    Jump("loc_5B9")

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_576")
    Jump("loc_5B9")

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_580")
    Jump("loc_5B9")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_58A")
    Jump("loc_5B9")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_594")
    Jump("loc_5B9")

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_59E")
    Jump("loc_5B9")

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5A8")
    Jump("loc_5B9")

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5B2")
    Jump("loc_5B9")

    label("loc_5B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5B9")

    label("loc_5B9")

    Return()

    # Function_0_3A6 end

    def Function_1_5BA(): pass

    label("Function_1_5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DE")
    OP_72(0x22, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_5DB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DB")

    Jump("loc_5EE")

    label("loc_5DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_5EE")
    OP_71(0x22, 0x10)
    OP_64(0x0, 0x1)

    label("loc_5EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_60A")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_61A")

    label("loc_60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_61A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61A")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_5BA end

    def Function_2_624(): pass

    label("Function_2_624")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_639")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_624")

    label("loc_639")

    Return()

    # Function_2_624 end

    def Function_3_63A(): pass

    label("Function_3_63A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "杜南公爵晕过去了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_63A end

    def Function_4_661(): pass

    label("Function_4_661")

    TalkBegin(0xFE)

    ChrTalk(
        0xA,
        (
            "#720F公主殿下，还有各位，\x01",
            "十分感谢你们的宽宏大量。\x02\x03",
            "我代表殿下向你们谢罪，\x01",
            "对于此恩此德，没齿难忘。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_661 end

    def Function_5_700(): pass

    label("Function_5_700")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_7FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_789")
    OP_A2(0x0)

    ChrTalk(
        0xF,
        (
            "刚才我给公主殿下帮忙，\x01",
            "制做了一些点心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "公主做的点心真是非常美味，\x01",
            "如果有兴趣请一定要来品尝。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FA")

    label("loc_789")


    ChrTalk(
        0xF,
        (
            "刚才我给公主殿下帮忙，\x01",
            "制做了一些点心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "公主做的点心真是非常美味，\x01",
            "如果有兴趣请一定要来品尝。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FA")

    Jump("loc_9A9")

    label("loc_7FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_984")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_88A")

    ChrTalk(
        0xFE,
        (
            "公主殿下她\x01",
            "刚才悄悄地到街上去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说是因为\x01",
            "她的同学也到王都来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_981")

    label("loc_88A")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "因为公主殿下回来了，\x01",
            "我要把这个房间打扫一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公主殿下她\x01",
            "刚才悄悄地到街上去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说是因为\x01",
            "她的同学也到王都来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_981")

    Jump("loc_9A9")

    label("loc_984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_98E")
    Jump("loc_9A9")

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_998")
    Jump("loc_9A9")

    label("loc_998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_9A2")
    Jump("loc_9A9")

    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_9A9")

    label("loc_9A9")

    TalkEnd(0xFE)
    Return()

    # Function_5_700 end

    def Function_6_9AD(): pass

    label("Function_6_9AD")

    TalkBegin(0x8)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9D2")
    SetChrSubChip(0xFE, 1)
    Jump("loc_9ED")

    label("loc_9D2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9E8")
    SetChrSubChip(0xFE, 0)
    Jump("loc_9ED")

    label("loc_9E8")

    SetChrSubChip(0xFE, 2)

    label("loc_9ED")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0x8,
        (
            "#090F嗯，\x01",
            "已经休养了很长的一段时间。\x02\x03",
            "从明天开始要抓紧时间，\x01",
            "还有很多的事情要处理呢。\x02\x03",
            "#094F又要和科洛蒂娅\x01",
            "暂时分别一些日子了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_9AD end

    def Function_7_AA6(): pass

    label("Function_7_AA6")

    TalkBegin(0x15)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ACB")
    SetChrSubChip(0xFE, 2)
    Jump("loc_AFC")

    label("loc_ACB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AE1")
    SetChrSubChip(0xFE, 1)
    Jump("loc_AFC")

    label("loc_AE1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AF7")
    SetChrSubChip(0xFE, 0)
    Jump("loc_AFC")

    label("loc_AF7")

    SetChrSubChip(0xFE, 2)

    label("loc_AFC")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B81")

    ChrTalk(
        0x15,
        (
            "#040F等没事了，\x01",
            "就和约修亚一起过来坐坐吧。\x02\x03",
            "大家一起喝茶聊聊天。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D02")

    label("loc_B81")

    OP_A2(0x2)

    ChrTalk(
        0x15,
        (
            "#040F艾丝蒂尔，\x01",
            "一起来喝杯茶吧？\x02\x03",
            "还想让你尝尝我新学来的点心呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F不好意思，科洛丝。\x01",
            "我正在找约修亚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#044F……约修亚？\x02\x03",
            "#041F那好，\x01",
            "等你们没事了就一起过来吧。\x02\x03",
            "我们会在这等着的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊，嗯……谢谢。\x01",
            "让你们费心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D02")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0x15)
    Return()

    # Function_7_AA6 end

    def Function_8_D0B(): pass

    label("Function_8_D0B")

    TalkBegin(0x16)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D30")
    SetChrSubChip(0xFE, 2)
    Jump("loc_D4B")

    label("loc_D30")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D46")
    SetChrSubChip(0xFE, 0)
    Jump("loc_D4B")

    label("loc_D46")

    SetChrSubChip(0xFE, 1)

    label("loc_D4B")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E16")

    ChrTalk(
        0x16,
        (
            "#170F以后决不能让理查德上校叛变\x01",
            "这种事件再次发生了。\x02\x03",
            "#176F亲卫队会和摩尔根将军\x01",
            "以及卡西乌斯上校齐心协力，\x01",
            "为王国军的再建拼尽全力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F19")

    label("loc_E16")

    OP_A2(0x3)

    ChrTalk(
        0x16,
        (
            "#170F诞辰庆典平安无事地结束，\x01",
            "实在太好了……\x02\x03",
            "以后决不能让理查德上校叛变\x01",
            "这种事件再次发生了。\x02\x03",
            "#176F亲卫队会和摩尔根将军\x01",
            "以及卡西乌斯上校齐心协力，\x01",
            "为王国军的再建拼尽全力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F19")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0x16)
    Return()

    # Function_8_D0B end

    def Function_9_F22(): pass

    label("Function_9_F22")

    TalkBegin(0x17)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F47")
    SetChrSubChip(0xFE, 1)
    Jump("loc_F78")

    label("loc_F47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F5D")
    SetChrSubChip(0xFE, 2)
    Jump("loc_F78")

    label("loc_F5D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F73")
    SetChrSubChip(0xFE, 0)
    Jump("loc_F78")

    label("loc_F73")

    SetChrSubChip(0xFE, 1)

    label("loc_F78")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1051")

    ChrTalk(
        0x17,
        (
            "#711F这样看着陛下和公主殿下\x01",
            "开心快乐地在一起，\x01",
            "我深切体会到和平的日子又回来了。\x02\x03",
            "这全靠艾丝蒂尔和各位的努力换来的啊。\x01",
            "　\x02\x03",
            "真是千恩万谢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1117")

    label("loc_1051")

    OP_A2(0x4)

    ChrTalk(
        0x17,
        (
            "#711F这样看着陛下和公主殿下\x01",
            "开心快乐地在一起，\x01",
            "我深切体会到和平的日子又回来了。\x02\x03",
            "这全靠艾丝蒂尔和各位的努力换来的啊。\x01",
            "　\x02\x03",
            "真是千恩万谢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1117")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0x17)
    Return()

    # Function_9_F22 end

    def Function_10_1120(): pass

    label("Function_10_1120")

    EventBegin(0x0)
    OP_6D(-460, 0, 2620, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x138, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 10, 0, -5370, 225)
    SetChrPos(0x102, 10, 0, -5370, 225)
    SetChrPos(0x138, 10, 0, -5370, 225)

    def lambda_119C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_119C)

    def lambda_11AE():
        OP_8E(0xFE, 0xFFFFFFA6, 0x0, 0x564, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_11AE)
    Sleep(500)

    def lambda_11CE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11CE)

    def lambda_11E0():
        OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0xFFFFFE5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11E0)
    Sleep(500)

    def lambda_1200():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1200)

    def lambda_1212():
        OP_8E(0xFE, 0x2EE, 0x0, 0xFFFFFE5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1212)
    WaitChrThread(0x138, 0x1)
    OP_8C(0x138, 180, 400)

    ChrTalk(
        0x101,
        (
            "#327F呼～刚才好紧张。\x02\x03",
            "#328F谢谢您，希尔丹夫人，\x01",
            "多亏您的及时相助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#331F很高明的手腕呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#713F#5P多谢你们的夸奖。\x02\x03",
            "#711F那么……怎么样，\x01",
            "在和陛下见面之前先换衣服吧？\x02\x03",
            "不用特别在意的，\x01",
            "我先带你们去换吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#471F没关系，就这个样子可以了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#333F#3S请务必要带我去换衣服。\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)

    def lambda_13C9():
        OP_6D(7620, 0, 14990, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13C9)
    OP_0D()
    OP_44(0x101, 0x1)
    SetMapFlags(0x800)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0x54)
    OP_6D(-52690, 0, 7170, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x101, -51850, 0, 7470, 270)
    SetChrPos(0x102, -53280, 0, 7850, 180)
    SetChrPos(0x138, -52990, 0, 5970, 0)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#507F你还真是的，那么害羞干嘛。\x01",
            "　\x02\x03",
            "刚才那样不就很好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F这可关系到我的名誉啊，\x01",
            "刚才那个样子是绝对不行的。\x02\x03",
            "#010F对了，希尔丹夫人，\x01",
            "这个房间莫非是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#713F嗯……\x01",
            "就是科洛蒂亚公主的房间。\x02\x03",
            "不过她一般不在王城里面居住，\x01",
            "所以就没有怎么用过……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(
        0x101,
        (
            "#501F咦～是这样的啊。\x02\x03",
            "#505F可是……\x01",
            "不是说公主殿下在照顾着陛下的吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#715F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F那果然也是假消息。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#713F详细情况你们就直接询问陛下吧。\x01",
            "　\x02\x03",
            "#710F女王宫的二楼就是\x01",
            "艾莉茜雅女王的房间。\x02\x03",
            "我们这就去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x643)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x0)
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 3)
    SetChrChipByIndex(0x138, 4)
    Return()

    # Function_10_1120 end

    def Function_11_1717(): pass

    label("Function_11_1717")

    EventBegin(0x0)
    Fade(1000)
    OP_A2(0x644)
    OP_28(0x4A, 0x1, 0x100)
    OP_28(0x4A, 0x1, 0x200)
    SetChrChipByIndex(0x138, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x138, -1000, 8000, 35250, 0)
    SetChrPos(0x101, -1500, 8000, 34000, 0)
    SetChrPos(0x102, -500, 8000, 34000, 0)
    SetChrPos(0x8, -980, 8000, 38840, 0)
    OP_6D(-1080, 8000, 35400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(27000, 0)
    OP_6E(280, 0)
    OP_0D()
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x138,
        (
            "#713F陛下，打扰了。\x02\x03",
            "我照之前所说，\x01",
            "把艾丝蒂尔和约修亚带来了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "老妇人的声音",
        "#4P……辛苦你了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "老妇人的声音",
        "#4P请进来吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#711F我明白了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x138, 270, 400)
    OP_8E(0x138, 0xFFFFF786, 0x1F40, 0x89B2, 0x7D0, 0x0)
    OP_8C(0x138, 180, 400)

    ChrTalk(
        0x138,
        (
            "#711F#1P我就在这里等着。\x02\x03",
            "那么你们俩就进去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F好、好的……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F打扰了……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-100970, 0, 4310, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -96900, 0, 15200, 0)
    SetChrPos(0x101, -101650, 0, 3300, 0)
    SetChrPos(0x102, -100450, 0, 3300, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()

    def lambda_19AD():
        OP_6D(-97420, 0, 14400, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19AD)

    def lambda_19C5():
        OP_6C(18000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19C5)

    def lambda_19D5():
        OP_67(0, 4200, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_19D5)

    def lambda_19ED():
        OP_6E(317, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_19ED)
    Sleep(4000)
    OP_8C(0x8, 180, 300)

    ChrTalk(
        0x8,
        (
            "#091F#5P呵呵……\x01",
            "欢迎你们两位的到来。\x02\x03",
            "#090F我的名字叫做\x01",
            "艾莉茜雅·冯·奥赛雷丝。\x02\x03",
            "利贝尔王国第２６代国王。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A91():
        OP_6D(-97420, 0, 14400, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A91)

    def lambda_1AA9():
        OP_8E(0xFE, 0xFFFE7F32, 0x0, 0x3160, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AA9)
    Sleep(300)

    def lambda_1AC9():
        OP_8E(0xFE, 0xFFFE8414, 0x0, 0x2F4E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1AC9)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#008F我、我是……\x01",
            "艾丝蒂尔·布莱特。\x02\x03",
            "游击士协会的准游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F同为游击士协会的准游击士，\x01",
            "我的名字是约修亚·布莱特。\x02\x03",
            "初次见面，陛下您好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F#5P艾丝蒂尔和约修亚。\x02\x03",
            "我真的很高兴能和你们两位见面。\x01",
            "　\x02\x03",
            "没有什么好东西可以款待你们，\x01",
            "就以一些茶水微表谢意吧。\x02\x03",
            "#091F请吧，我们到那边去慢慢谈。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-105030, 0, 9180, 0)
    OP_67(0, 6300, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(44000, 0)
    OP_6E(368, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 16)
    SetChrChipByIndex(0x102, 17)
    SetChrChipByIndex(0x8, 18)
    SetChrPos(0x8, -105250, 200, 10500, 180)
    SetChrPos(0x101, -103870, 200, 8990, 270)
    SetChrPos(0x102, -105250, 200, 7600, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x11, -104620, 640, 8950, 0)
    SetChrPos(0x12, -105280, 640, 8300, 0)
    SetChrPos(0x10, -105350, 640, 9620, 0)
    SetChrPos(0x14, -105280, 700, 9050, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#093F这样啊……\x01",
            "拉赛尔博士竟会卷入这样的事。\x02\x03",
            "#094F将一切导力停止的黑色导力器……\x01",
            "　\x02\x03",
            "那样的物品竟然落入了上校手中……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F博士说女王陛下也许会知道\x01",
            "理查德上校使用这个黑色导力器的目的。\x01",
            "　\x02\x03",
            "请问……有什么线索吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#094F……………………\x02\x03",
            "#093F只有一个线索。\x02\x03",
            "不过……\x01",
            "我想上校应该不会知道那一点。\x02\x03",
            "希望那只是我多余的担心就好了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F请问……\x01",
            "那个线索是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#094F……把这些事情告诉你们也没什么关系。\x01",
            "　\x02\x03",
            "#092F——数十年前，在这个王都的地下\x01",
            "检测出了巨大的导力反应。\x02\x03",
            "当时做这项导力调查研究的就是\x01",
            "中央工房的拉赛尔博士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F巨大的导力反应……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F所谓王都的地下……\x01",
            "就是指地下水路的周边吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#092F不是，是从比地下水路\x01",
            "还要深很多的地方检测出来的。\x02\x03",
            "博士认为那是古文明宝藏之地，\x01",
            "埋藏着至今仍未失去机能的古代文明遗物。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F古代文明的遗物……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#012F就是被称为『古代遗物』的古代导力器。\x01",
            "　\x02\x03",
            "其中大部分都像四轮之塔塔顶的装置\x01",
            "那样失去了机能……\x02\x03",
            "而小部分就像戴尔蒙市长的传家宝那样，\x01",
            "还继续保持着机能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F那样的东西在王都地下……\x02\x03",
            "#580F啊，这么说那个『福音』就是……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#012F是用作将古代遗物的机能\x01",
            "停止下来的特殊导力器……\x02\x03",
            "这种可能性是有的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#093F是啊……\x02\x03",
            "可是，那个遗物究竟是什么\x01",
            "以及为何会埋藏在那里这些问题至今仍未查明。\x01",
            "　\x02\x03",
            "拉赛尔博士的调查\x01",
            "本身也是在非正式的进行当中……\x02\x03",
            "如果说上校从某个地方得知了其存在，\x01",
            "我认为这也并不是不可能的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F是这样啊……\x02\x03",
            "不管怎样说，\x01",
            "所有的事件有可能是因此而引起的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F真是的，稍微想开一点，\x01",
            "不要把事情想的那么严峻嘛……\x02\x03",
            "#002F总之，只要人们陷入了困境，\x01",
            "代表爱与正义的游击士就会立刻出现！\x02\x03",
            "无论如何也会阻止上校的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F呵呵……\x02\x03",
            "真不愧是……\x01",
            "卡西乌斯上校的孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F陛下和父亲以前曾经认识吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F他是我去世的孩子的朋友，\x01",
            "也是拯救王国的英雄呢。\x02\x03",
            "他退役之后，当了游击士还常帮我办事，\x01",
            "真是……无论何时都承蒙他的关照啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F还、还有这回事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F这我们以前并不知道呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F呵呵，以他的性格来看，\x01",
            "你们两个不知道也是比较正常的。\x02\x03",
            "假如十年前的战争中，\x01",
            "没有他在战场上的奋力拼搏……\x02\x03",
            "这个地方还会存在吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F其实呢，女王陛下……\x01",
            "这件事的详细情况我确实不太清楚呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#094F那么，告诉你们真相的角色，\x01",
            "说不定是留给了身为女王的本人……\x02\x03",
            "#090F艾丝蒂尔、约修亚。\x02\x03",
            "你们两个愿意稍微听一听\x01",
            "我这个上了年纪的人讲的故事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F啊……好的，那当然啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F洗耳恭听。\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_1D(0x53)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("艾莉茜雅女王")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "这是在十年前的春天发生的事情……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "埃雷波尼亚帝国的南部\x01",
            "发生了一起十分沉痛的事件。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "因为至今整个事件的起因仍未查明，\x01",
            "所以与事件有关的说明就省略了……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "以这起事件为开端，\x01",
            "埃雷波尼亚帝国向利贝尔王国宣战。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "之后，『百日战役』的苦难岁月\x01",
            "就是从那个时候开始的了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x4001B, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetChrName("艾莉茜雅女王")

    AnonymousTalk(
        (
            "就在帝国向王国宣战的同时，\x01",
            "帝国军集中大量兵力攻陷了哈肯大门……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "除了有长城守护的王都格兰赛尔以外，\x01",
            "利贝尔整片土地转瞬之间被全部占领了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "而且入侵的帝国军的兵力是\x01",
            "我们王国军的三倍以上……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "即使卡尔瓦德要派来援军也来不及……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "王都被占领也只是时间上的问题。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x4001C, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetChrName("艾莉茜雅女王")

    AnonymousTalk(
        "可是开战的两个月之后……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "处于被动的战局发生了巨大的逆转。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "利用当时才开发完毕的警备飞艇，\x01",
            "王国军将连接各地的关所一一夺回，\x01",
            "并且切断了帝国军的联络。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "接着，以雷斯顿要塞为先发部队，\x01",
            "王国军总兵力乘坐水上飞艇出击，\x01",
            "将各个地区顺利夺了回来。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "蔡斯、卢安、柏斯、洛连特……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "帝国军的补给线被切断了之后，\x01",
            "王国军将占领各地的帝国军师团逐个击破。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x4001D, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetChrName("艾莉茜雅女王")

    AnonymousTalk(
        (
            "制定这次反攻作战计划的就是\x01",
            "卡西乌斯·布莱特上校——\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "摩尔根将军的得力助手、\x01",
            "理查德上校的顶头上司、\x01",
            "同时也是你们两个孩子的父亲。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "此后不久，\x01",
            "在游击士协会以及七耀教会的仲裁之下，\x01",
            "长达百日的战争也就此宣告结束。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "可是就在那个时候……\x01",
            "卡西乌斯上校失去了他的最爱最重要的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x4001E, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetChrName("艾莉茜雅女王")

    AnonymousTalk(
        (
            "她就是莱娜·布莱特女士……\x01",
            "也是艾丝蒂尔你的母亲。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "在反攻作战即将胜利的时刻，\x01",
            "走投无路的帝国军师团为了报复王国军，\x01",
            "炮击破坏了作为洛连特象征的钟楼。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "于是……\x01",
            "后面的事情你们都知道了……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "卡西乌斯上校，\x01",
            "甚至连夫人最后一面都没有见到……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x64)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#003F……怎么会……………\x02\x03",
            "怎么会这样……………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#094F……无奈自己制定的作战计划\x01",
            "却是导致了夫人死去的原因。\x02\x03",
            "因此而深深自责的卡西乌斯上校决定退役，\x01",
            "走上了游击士的道路……\x02\x03",
            "守护在战争中幸存下来的你的身边……\x02\x03",
            "他这样做，外人虽然非常不解，\x01",
            "但也是为了用自己双手来保护最亲的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F笨蛋……爸爸……\x02\x03",
            "因为爸爸的过失而导致妈妈的离去什么的……\x01",
            "　\x02\x03",
            "明明不是这样的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#093F嗯，是啊……\x02\x03",
            "这一切一切的悲剧……都是我这个\x01",
            "没有好好保护自己子民的女王的过错。\x02\x03",
            "#094F对不起，艾丝蒂尔。\x01",
            "我没能保护好你的妈妈……\x02\x03",
            "对于此事……\x01",
            "请接受我深深的歉意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F没、没有必要道歉呢！\x02\x03",
            "#500F女王陛下一直守护着这来之不易的和平……\x01",
            "　\x02\x03",
            "而爸爸他们也在拼死守护着这个国家……\x01",
            "　\x02\x03",
            "妈妈以生命为代价守护了我……\x01",
            "　\x02\x03",
            "#008F这样，我就已经满足了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F艾丝蒂尔……\x01",
            "谢谢，你的确是个优秀的孩子……\x02\x03",
            "#094F能够见到你真是太好了……\x01",
            "　\x02\x03",
            "这是我发自心底的感慨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F女王陛下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#094F不过，正因为如此……\x02\x03",
            "#090F正因为如此，\x01",
            "我不希望你们遇到任何危险。\x02\x03",
            "无论结局是怎样都好，\x01",
            "我都不想让你们再卷入这次的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F啊……！\x02\x03",
            "可、可是我们俩是受尤莉亚中尉委托\x01",
            "来协助女王陛下您的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F谢谢。\x01",
            "你们的好意我心领了。\x02\x03",
            "在卡西乌斯上校外出的时候，\x01",
            "你们两个孩子万一出了什么事情，\x01",
            "身为女王的我只会无法向他交待……\x02\x03",
            "因此，请你们回到洛连特的家中，\x01",
            "等待你们的父亲回来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F可、可是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F可是，女王陛下……\x02\x03",
            "由父亲取回的、陛下您一直守护着的和平，\x01",
            "现在正在经受着严峻的考验。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#093F约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F因为『福音』引起的所有事件……\x02\x03",
            "就这样下去的话……\x01",
            "上校一旦达成让公爵成为国王的目的，\x01",
            "现在的和平会变成如何的样子呢？\x02\x03",
            "请陛下您务必要考虑一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#093F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F对、对不起，女王陛下……\x02\x03",
            "我们两个自从成为游击士以来，\x01",
            "就作为爸爸的代理人来完成任务。\x02\x03",
            "从那个时候的空贼事件开始，\x01",
            "收到了老爸的信、来历不明的包裹，\x01",
            "然后就沿着这样的轨迹在各地修行……\x02\x03",
            "感觉就好像是老爸在\x01",
            "引导着我们来这里和女王陛下见面。\x02\x03",
            "#500F所以……我也有必须守护的东西。\x02\x03",
            "这和平的、幸福的每一天……\x02\x03",
            "以及这一路上所认识的、\x01",
            "关心我、喜欢我的各位朋友……\x02\x03",
            "#002F我会用自己的方法来守护着的！\x01",
            "就像女王陛下您和妈妈那样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#093F艾丝蒂尔……\x02\x03",
            "#094F……………………\x02\x03",
            "的确……\x01",
            "和那个孩子所说的一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F我也终于明白了。\x02\x03",
            "我想通过艾丝蒂尔你们\x01",
            "向游击士协会委托一些需要解决的事情。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F女王陛下……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F陛下……\x01",
            "请您尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#092F委托的内容就是——\x01",
            "救出被情报部囚禁的人质。\x02\x03",
            "其中还包括我的孙女科洛蒂娅。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F啊，公主殿下果然\x01",
            "被那些家伙抓到某个地方去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#094F嗯……\x02\x03",
            "现在回想起来……\x01",
            "这次的政变是因为我要推选那个孩子\x01",
            "为下一任国王而开始的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F果然不是杜南公爵呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#093F嗯，虽说杜南是我的外甥，\x01",
            "但这个人是个问题诸多的败家子。\x01",
            "　\x02\x03",
            "相比之下，我的孙女虽说不算很成熟，\x01",
            "但在很多方面都要出色很多。\x02\x03",
            "在考虑了王国的未来之后……\x01",
            "我做出的决定就是选择科洛蒂娅公主。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯……\x01",
            "公主的事情我不是很了解……\x02\x03",
            "不过不管怎么说，\x01",
            "做出这样的决定肯定是正确的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#094F可是无论何时……\x01",
            "这个世界总是倾向于对女性当权\x01",
            "持反对甚至是敌对的态度。\x02\x03",
            "而且，当年被侵略的历史依旧历历在目，\x01",
            "所以这种态度也越来越强硬……\x02\x03",
            "#092F国家连续两代都由女性来统治，\x01",
            "结果只会导致国力的衰弱……\x02\x03",
            "会出现持有这种观点的人物，\x01",
            "也不是什么不可思议的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F原来如此……\x01",
            "那样的人物就是理查德上校吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#092F是的。\x02\x03",
            "我打算推选科洛蒂娅为下一任国王的想法\x01",
            "不知何时被他得知了。\x01",
            "　\x02\x03",
            "于是他就把这件事告诉了杜南公爵，\x01",
            "然后发动了这次政变。\x02\x03",
            "实际上，他暗中操纵杜南公爵，\x01",
            "是为了要把利贝尔打造成一个\x01",
            "能与周边大国抗衡的强大军事国家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F原来如此……\x02\x03",
            "终于明白整件事情的全貌了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#505F打造成强大的军事国家……\x01",
            "具体来说他要怎么做呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#012F会有各种各样的做法。\x02\x03",
            "例如提高税率、增加军费开支……\x01",
            "　\x02\x03",
            "开发大量具有破坏性的导力兵器……\x01",
            "　\x02\x03",
            "采取大规模的征兵制……\x02\x03",
            "甚至能和利贝尔不承认的组织『猎兵团』\x01",
            "签订所谓的合法契约……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F怎、怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#094F的确，与之类似的要求，\x01",
            "理查德上校也曾向我提出过。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#093F虽说我知道这也是\x01",
            "出自纯粹的爱国心而说的一番话……\x02\x03",
            "但是无论怎样，\x01",
            "我也不认为这种作法是正确的。\x02\x03",
            "要守护一个国家，\x01",
            "仅靠强大的军事力量是不行的。\x02\x03",
            "只要和周边诸国协调好关系，\x01",
            "多做一些善意的互利的外交政策……\x02\x03",
            "加强国家之间的技术和经济交流，\x01",
            "这样就可以让全国各地更加繁荣，\x01",
            "也就可以牢固地守护着国家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F……陛下所言的确才是真正的道理。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯嗯！我也觉得是！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#092F但是，上校一口断定这是\x01",
            "我自己带有妇人之见的理想论。\x02\x03",
            "而且没想到的是……\x01",
            "他以科洛蒂娅的安全来要挟我退位。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#094F大部分掌权者的亲属都被扣押为人质，\x01",
            "所以他们都不敢违抗上校的意思。\x02\x03",
            "可我是利贝尔的女王。\x01",
            "不能因为骨肉之情而出卖国家的未来。\x01",
            "　\x02\x03",
            "#093F话虽然这么说……\x01",
            "但那孩子毕竟是我唯一的孙女……\x02\x03",
            "我不能见死不救啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F女王陛下……\x01",
            "这件事就请您放心吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F您委托的旨意，我们已经清楚地了解了。\x02\x03",
            "我们一定会将包括公主殿下在内的\x01",
            "所有人质解救出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F非常感谢……\x01",
            "艾丝蒂尔、约修亚。\x02\x03",
            "这样一来，\x01",
            "我就有和上校相抗衡的保证。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F请、请问，\x01",
            "就没有其他的委托了吗？\x02\x03",
            "还有『福音』那件事……\x02\x03",
            "如果现在要帮助女王陛下您逃离这里，\x01",
            "我认为也不是不可能的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F谢谢你，艾丝蒂尔。\x02\x03",
            "不过，即使我离开这里，\x01",
            "也不能改变国家如今的局势。\x02\x03",
            "#094F这件事究竟与『福音』有着怎样的关联，\x01",
            "对此我真的非常在意。\x02\x03",
            "所以，我要向上校问清楚\x01",
            "他做这些事情的真实意图所在。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_6D(-52350, 0, 6280, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x138, 0)
    SetChrPos(0x101, -53000, 0, 6160, 90)
    SetChrPos(0x102, -51450, 0, 6000, 270)
    OP_1D(0x54)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#328F哈……女王陛下真是一位\x01",
            "充满魅力和优雅感的女性啊～\x02\x03",
            "不但待人和蔼可亲，\x01",
            "而且内心又坚强、性格又坚毅……\x02\x03",
            "#321F等我到了那个年纪时，\x01",
            "也要成为那样有魅力的老奶奶呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#337F有魅力……\x02\x03",
            "#338F不过的确是一位很有\x01",
            "一国之主风范的女性呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#323F唔……\x02\x03",
            "真想这就阻止政变，\x01",
            "把女王陛下和公主他们救出来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#330F唔……其实这并不属于\x01",
            "游击士协会所管辖的范围……\x02\x03",
            "不过无论如何，\x01",
            "我们也要尽力去完成委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#326F嗯……没错。\x02\x03",
            "#327F而且，能从女王那里听说到老爸的事迹，\x01",
            "简直就像是在做梦一样……\x01",
            "　\x02\x03",
            "还会不会有我不知道的事情冒出来呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    OP_9F(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x138, -51030, 0, 420, 225)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4FEB():

        label("loc_4FEB")

        TurnDirection(0xFE, 0x138, 400)
        OP_48()
        Jump("loc_4FEB")

    QueueWorkItem2(0x101, 1, lambda_4FEB)

    def lambda_4FFC():

        label("loc_4FFC")

        TurnDirection(0xFE, 0x138, 400)
        OP_48()
        Jump("loc_4FFC")

    QueueWorkItem2(0x102, 1, lambda_4FFC)

    ChrTalk(
        0x138,
        (
            "#1P艾丝蒂尔、约修亚。\x02\x03",
            "你们准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5048():
        TurnDirection(0xFE, 0x138, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5048)
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(
        0x101,
        "#471F啊，好了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_507B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_507B)

    def lambda_508D():
        OP_8E(0xFE, 0xFFFF34A4, 0x0, 0xF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_508D)
    OP_6D(-52330, 0, 5310, 2000)
    WaitChrThread(0x138, 0x1)

    ChrTalk(
        0x138,
        (
            "#710F那我们就立刻回休息室去吧。\x01",
            "　\x02\x03",
            "已经过１１点了……\x01",
            "再过一会儿就是新的一天了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#324F哇啊，已经这么晚了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#330F我们和陛下聊天用了很长时间呢。\x01",
            "　\x02\x03",
            "如果再这么呆下去的话，\x01",
            "看守的那些士兵就会怀疑了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    SetChrPos(0x101, -52650, 0, 5460, 180)
    SetChrPos(0x102, -52650, 0, 5460, 180)
    SetChrPos(0x138, -52650, 0, 5460, 180)
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    OP_1B(0x2, 0x0, 0xFFFF)
    OP_6D(-52650, 0, 5460, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_11_1717 end

    def Function_12_5279(): pass

    label("Function_12_5279")

    OP_28(0x4E, 0x1, 0x4)
    EventBegin(0x0)
    OP_6D(170, 0, 5170, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 0, 0, 9760, 180)
    SetChrPos(0xB, -1480, 0, 9280, 180)
    SetChrPos(0xC, -660, 0, 8290, 180)
    SetChrPos(0xD, 700, 0, 8420, 180)
    SetChrPos(0xE, 1400, 0, 9310, 180)
    SetChrPos(0x101, -90, 0, 920, 0)
    SetChrPos(0x105, -1330, 0, 430, 0)
    SetChrPos(0x103, 930, 0, 430, 0)
    SetChrChipByIndex(0x101, 9)
    SetChrChipByIndex(0x103, 11)
    SetChrChipByIndex(0x105, 13)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#220F叛、叛逆者！\x01",
            "居然恬不知耻的跑到这儿来了！？\x02\x03",
            "明知我是将要继承王位的人，\x01",
            "你们还要动粗吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F别说笑了，你那发型已经够搞笑了。\x02\x03",
            "你现在已经\x01",
            "再也不可能成为国王了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#220F什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F您是杜南公爵阁下吧。\x01",
            "我们是游击士协会派来的人。\x02\x03",
            "科洛蒂娅殿下委托我们\x01",
            "来救出女王陛下。\x02\x03",
            "如果您能通融一下，\x01",
            "我们也会给您好处的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#220F科、科洛蒂娅！？\x02\x03",
            "那个小姑娘……\x01",
            "简直是多此一举！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F杜南王叔……\x01",
            "请您不要再执迷不悟了好吗？\x02\x03",
            "王叔，您是被理查德\x01",
            "上校给利用了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#220F你、你在胡说什么啊……\x02\x03",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#220F你、你、你、\x01",
            "你不是科洛蒂娅吗！\x02\x03",
            "那样的发型和装扮，像个什么样子！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F终于发觉了啊……\x02\x03",
            "原来这就是你在卢安\x01",
            "没能注意到的原因啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F虽然之前不是很了解，\x01",
            "不过的确是个很迟钝的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F对不起，一直瞒着您\x01",
            "这件事，是我不好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#220F根、根本就是把我\x01",
            "当傻瓜来耍！\x02\x03",
            "这就是为何女人这种生物\x01",
            "不可信任的原因啊！\x02\x03",
            "狡猾、小气、为一些不值得\x01",
            "的小事情故意找碴儿……\x02\x03",
            "怎么能把王冠交给\x01",
            "这样无聊的家伙呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F……………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#220F……嗯……不过………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "大、大人……\x01",
            "情况不妙啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "还、还是投降吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哈哈……无聊的手下啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F哎呀呀，看来我得对你另眼相看了。\x02\x03",
            "在这样的时代中，\x01",
            "还敢做出这么有胆识的发言。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F对、对不起了王叔。\x02\x03",
            "这回有点儿……\x01",
            "我也不好帮您求情了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5A7A():
        OP_8E(0xFE, 0x122, 0x0, 0x59A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A7A)

    def lambda_5A95():
        OP_8E(0xFE, 0x122, 0x0, 0x59A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A95)

    def lambda_5AB0():
        OP_8E(0xFE, 0x122, 0x0, 0x59A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5AB0)
    OP_6D(420, 0, 10250, 500)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    Battle(0x3AA, 0x0, 0x0, 0x2, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_5AFB"),
        (SWITCH_DEFAULT, "loc_5AFE"),
    )


    label("loc_5AFB")

    OP_B4(0x0)
    Return()

    label("loc_5AFE")

    EventBegin(0x0)
    SetChrPos(0xB, -1890, 0, 12000, 315)
    SetChrPos(0xC, 280, 0, 13640, 135)
    SetChrPos(0xD, 3410, 0, 11230, 315)
    SetChrPos(0xE, 1760, 0, 8900, 177)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (3, "loc_5B50"),
        (SWITCH_DEFAULT, "loc_6359"),
    )


    label("loc_5B50")

    OP_6D(-2350, 0, 8189, 0)
    SetChrPos(0x9, -4620, 0, 7950, 90)
    SetChrPos(0x101, -1690, 0, 9010, 22)
    SetChrPos(0x105, -390, 0, 8010, 90)
    SetChrPos(0x103, -1510, 0, 6870, 90)
    OP_2B(0x4D, 0x2)

    ChrTalk(
        0x101,
        (
            "#000F好的，解决了！\x02\x03",
            "接下来，应该\x01",
            "轮到公爵您了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C10():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C10)

    def lambda_5C1E():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C1E)

    def lambda_5C2C():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5C2C)
    OP_8F(0x9, 0xFFFFEAC0, 0x0, 0x1EB4, 0x7D0, 0x0)

    ChrTalk(
        0x103,
        (
            "#020F由女人手中挥出的鞭子，\x01",
            "想不想品尝一下是什么滋味呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x9, 0xFFFFE6E2, 0x0, 0x1EB4, 0x7D0, 0x0)

    ChrTalk(
        0x9,
        (
            "#220F哇、哇呀呀呀呀呀……\x02\x03",
            "不要过来、不要靠近我呀啊啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F对、对不起……\x01",
            "请您原谅我们吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D18():
        OP_6D(-4750, 0, 8080, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5D18)

    ChrTalk(
        0x9,
        (
            "#220F可恶，这样的话，\x01",
            "我就只好拿陛下当盾牌……\x02\x03",
            "……嘿～哈～喝！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D8E():
        OP_8C(0xFE, 275, 800)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5D8E)
    OP_8F(0x9, 0xFFFFDFD0, 0x0, 0x1E82, 0x1B58, 0x0)
    OP_62(0x9, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    OP_22(0x30, 0x0, 0x64)

    def lambda_5DC7():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5DC7)
    OP_8F(0x9, 0xFFFFE124, 0x0, 0x1E82, 0xBB8, 0x0)
    WaitChrThread(0x9, 0x1)

    def lambda_5DEE():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5DEE)

    ChrTalk(
        0x9,
        "#220F呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎呀……\x01",
            "好像惊吓过度了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F不过他确实阻碍我们了呢，\x01",
            "这不是个很好的教训吗?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F是……\x01",
            "真是不幸的事件啊。\x02\x03",
            "可是，难道就让\x01",
            "王叔这么昏迷在这儿吗……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -50, 0, 340, 315)

    ChrTalk(
        0xA,
        "……公、公爵大人！？　　　\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)

    def lambda_5F80():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F80)

    def lambda_5F8E():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5F8E)

    def lambda_5F9C():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5F9C)
    OP_6D(-2009, 0, 6520, 1000)

    def lambda_5FBB():

        label("loc_5FBB")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5FBB")

    QueueWorkItem2(0x101, 1, lambda_5FBB)

    def lambda_5FCC():

        label("loc_5FCC")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5FCC")

    QueueWorkItem2(0x103, 1, lambda_5FCC)

    def lambda_5FDD():

        label("loc_5FDD")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5FDD")

    QueueWorkItem2(0x105, 1, lambda_5FDD)

    def lambda_5FEE():
        OP_6D(-4750, 0, 8080, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5FEE)
    OP_92(0xA, 0x9, 0x258, 0x1388, 0x0)

    ChrTalk(
        0x101,
        "#000F啊，是菲利普先生！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "#720F艾丝蒂尔小姐……\x01",
            "还有科洛蒂娅公主！\x02\x03",
            "对于这次我家主人\x01",
            "的执迷不悟，我感到非常的抱歉！\x02\x03",
            "这一切都是因为我没有\x01",
            "好好教导大人而导致的……\x02\x03",
            "因此，如果你们要惩罚的话，\x01",
            "就请惩罚在下吧！　　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "菲利普深深的低下了头。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#000F惩、惩罚……\x01",
            "只是晕过去了而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F菲利普先生……\x01",
            "请您先抬起头来吧。\x02\x03",
            "我们一行人，是为了救祖母……\x01",
            "营救陛下而赶来的。\x02\x03",
            "原本就和王叔\x01",
            "是没有任何牵连的。\x02\x03",
            "因此，请把王叔送到\x01",
            "我的房间养伤吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#720F公、公主殿下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F事实上他没有受到什么伤害哦。\x02\x03",
            "就只是因为突然受惊\x01",
            "而昏厥，没事儿的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#720F大、大家……\x01",
            "真是太感谢了。\x02\x03",
            "你们的大恩大德，我决对不会忘记的！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_63(0x9)
    FadeToBright(2000, 0)
    OP_0D()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    EventEnd(0x0)
    Return()

    label("loc_6359")

    OP_6D(370, 0, 8590, 0)
    SetChrPos(0x9, 1620, 0, 8100, 112)
    SetChrPos(0x101, -1690, 0, 9010, 22)
    SetChrPos(0x105, -390, 0, 8010, 90)
    SetChrPos(0x103, -1510, 0, 6870, 90)
    TurnDirection(0x101, 0x9, 0)
    TurnDirection(0x105, 0x9, 0)
    TurnDirection(0x103, 0x9, 0)

    ChrTalk(
        0x101,
        (
            "#000F呼，想不到连公爵\x01",
            "也一起打晕了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F如果可以办到的话，\x01",
            "倒是只需要打倒特务兵就行了……\x02\x03",
            "不过他确实阻碍我们了呢，\x01",
            "这不是个很好的教训吗?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F是……\x01",
            "真是不幸的事件啊。\x02\x03",
            "可是，难道就让\x01",
            "王叔这么昏迷在这儿吗……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -120, 0, -820, 315)

    ChrTalk(
        0xA,
        "……公、公爵大人！？　　　\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)

    def lambda_6586():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6586)

    def lambda_6594():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6594)

    def lambda_65A2():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_65A2)
    OP_6D(510, 0, 4400, 1000)

    def lambda_65C1():

        label("loc_65C1")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_65C1")

    QueueWorkItem2(0x101, 1, lambda_65C1)

    def lambda_65D2():

        label("loc_65D2")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_65D2")

    QueueWorkItem2(0x103, 1, lambda_65D2)

    def lambda_65E3():

        label("loc_65E3")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_65E3")

    QueueWorkItem2(0x105, 1, lambda_65E3)

    def lambda_65F4():
        OP_6D(370, 0, 8590, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_65F4)
    OP_92(0xA, 0x9, 0x258, 0x1388, 0x0)

    ChrTalk(
        0x101,
        "#000F啊，是菲利普先生！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "#720F艾丝蒂尔小姐……\x01",
            "还有科洛蒂娅公主！\x02\x03",
            "对于这次我家主人\x01",
            "的执迷不悟，我感到非常的抱歉！\x02\x03",
            "这一切都是因为我没有\x01",
            "好好教导大人而导致的……\x02\x03",
            "因此，如果你们要惩罚的话，\x01",
            "就请惩罚在下吧！　　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "菲利普深深的低下了头。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#000F等、等一下！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F菲利普先生……\x01",
            "请您先抬起头来吧。\x02\x03",
            "我们一行人，是为了救祖母……\x01",
            "营救陛下而赶来的。\x02\x03",
            "原本就和王叔\x01",
            "是没有任何牵连的。\x02\x03",
            "因此，请把王叔送到\x01",
            "我的房间养伤吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#720F公、公主殿下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F事实上他没有受到什么伤害哦。\x02\x03",
            "就只是因为受了点打击\x01",
            "而昏厥，没事儿的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#720F大、大家……\x01",
            "真是太感谢了。\x02\x03",
            "你们的大恩大德，我决对不会忘记的！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_63(0x9)
    FadeToBright(2000, 0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_12_5279 end

    def Function_13_6965(): pass

    label("Function_13_6965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69EC")
    EventBegin(0x1)
    TurnDirection(0x0, 0x1, 400)

    NpcTalk(
        0x0,
        "希尔丹夫人",
        (
            "#710F女王陛下的房间就在\x01",
            "这个女王宫的二楼。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_69EC")

    Return()

    # Function_13_6965 end

    def Function_14_69ED(): pass

    label("Function_14_69ED")

    OP_1F(0x50, 0xC8)
    Return()

    # Function_14_69ED end

    SaveToFile()

Try(main)
