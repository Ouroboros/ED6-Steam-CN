from ED6ScenarioHelper import *

def main():
    # 洛连特市长官邸

    CreateScenaFile(
        FileName            = 'T0210   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0210.x',
        MapIndex            = 12,
        MapDefaultBGM       = "ed60010",
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
        '克劳斯市长',                           # 9
        '米蕾奴夫人',                           # 10
        '玲达',                                 # 11
        '乔丝特',                               # 12
        '雪拉扎德',                             # 13
        '目标用摄像机',                         # 14
        '树叶',                                 # 15
    )

    DeclEntryPoint(
        Unknown_00              = 6000,
        Unknown_04              = 0,
        Unknown_08              = 184000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
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
        Unknown_3A              = 12,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 6000,
        Unknown_04              = 0,
        Unknown_08              = 184000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 12,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02350 ._CH',             # 00
        'ED6_DT07/CH01180 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
        'ED6_DT07/CH02330 ._CH',             # 03
        'ED6_DT07/CH00020 ._CH',             # 04
        'ED6_DT07/CH02353 ._CH',             # 05
        'ED6_DT06/CH20034 ._CH',             # 06
        'ED6_DT06/CH20021 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02350P._CP',             # 00
        'ED6_DT07/CH01180P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
        'ED6_DT07/CH02330P._CP',             # 03
        'ED6_DT07/CH00020P._CP',             # 04
        'ED6_DT07/CH02353P._CP',             # 05
        'ED6_DT06/CH20034P._CP',             # 06
        'ED6_DT06/CH20021P._CP',             # 07
    )

    DeclNpc(
        X                   = 82247,
        Z                   = 0,
        Y                   = 2548,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 7138,
        Z                   = 0,
        Y                   = 64539,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 506,
        Z                   = 0,
        Y                   = -1811,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 81266,
        Z                   = 0,
        Y                   = 53214,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        X                   = 138350,
        Z                   = 50,
        Y                   = -52070,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 851975,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -6321,
        Y                   = 0,
        Z                   = -3741,
        Range               = -3987,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE60E,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = 75880,
        TriggerZ            = 0,
        TriggerY            = 56920,
        TriggerRange        = 500,
        ActorX              = 75880,
        ActorZ              = 700,
        ActorY              = 56920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 138350,
        TriggerZ            = 0,
        TriggerY            = -52070,
        TriggerRange        = 500,
        ActorX              = 138350,
        ActorZ              = 0,
        ActorY              = -52070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 78710,
        TriggerZ            = 0,
        TriggerY            = 52510,
        TriggerRange        = 1800,
        ActorX              = 78710,
        ActorZ              = 1000,
        ActorY              = 52510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 77520,
        TriggerZ            = 0,
        TriggerY            = 50360,
        TriggerRange        = 500,
        ActorX              = 77520,
        ActorZ              = 900,
        ActorY              = 50360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 82150,
        TriggerZ            = 0,
        TriggerY            = 50830,
        TriggerRange        = 500,
        ActorX              = 82150,
        ActorZ              = 1200,
        ActorY              = 50830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 82490,
        TriggerZ            = 310,
        TriggerY            = 57230,
        TriggerRange        = 500,
        ActorX              = 82490,
        ActorZ              = 1200,
        ActorY              = 57230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 78330,
        TriggerZ            = 0,
        TriggerY            = 57050,
        TriggerRange        = 500,
        ActorX              = 78330,
        ActorZ              = 500,
        ActorY              = 57050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 84700,
        TriggerZ            = 0,
        TriggerY            = 55320,
        TriggerRange        = 500,
        ActorX              = 84700,
        ActorZ              = 500,
        ActorY              = 55320,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_34E",          # 00, 0
        "Function_1_5DC",          # 01, 1
        "Function_2_64B",          # 02, 2
        "Function_3_661",          # 03, 3
        "Function_4_15CA",         # 04, 4
        "Function_5_21D8",         # 05, 5
        "Function_6_2B19",         # 06, 6
        "Function_7_3D70",         # 07, 7
        "Function_8_4774",         # 08, 8
        "Function_9_49C7",         # 09, 9
        "Function_10_4C15",        # 0A, 10
        "Function_11_4D0B",        # 0B, 11
        "Function_12_4E27",        # 0C, 12
        "Function_13_4F1C",        # 0D, 13
        "Function_14_5012",        # 0E, 14
        "Function_15_50C0",        # 0F, 15
        "Function_16_517B",        # 10, 16
        "Function_17_5919",        # 11, 17
        "Function_18_5962",        # 12, 18
        "Function_19_6F37",        # 13, 19
        "Function_20_6F5A",        # 14, 20
        "Function_21_6F7B",        # 15, 21
        "Function_22_6F9E",        # 16, 22
        "Function_23_7B28",        # 17, 23
        "Function_24_7B44",        # 18, 24
        "Function_25_7B65",        # 19, 25
    )


    def Function_0_34E(): pass

    label("Function_0_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_37F")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 200010, 0, 44420, 270)
    SetChrPos(0xA, 201860, 0, 1360, 90)
    Jump("loc_42E")

    label("loc_37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_3B0")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 200010, 0, 44420, 270)
    SetChrPos(0xA, 201860, 0, 1360, 90)
    Jump("loc_42E")

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_3C9")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_42E")

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_3D8")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_42E")

    label("loc_3D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_409")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 201700, 0, 43930, 90)
    SetChrPos(0xA, 7130, 0, 64540, 0)
    Jump("loc_42E")

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_422")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_42E")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_42E")
    ClearChrFlags(0x9, 0x80)

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_486")
    OP_44(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, 7150, 200, -3320, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_486")
    SetChrPos(0xC, 5410, 0, -3320, 90)
    ClearChrFlags(0xC, 0x80)

    label("loc_486")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (112, "loc_49E"),
        (115, "loc_4F0"),
        (100, "loc_517"),
        (1, "loc_55F"),
        (SWITCH_DEFAULT, "loc_5DB"),
    )


    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C9")
    OP_A2(0x24F)
    OP_28(0x3, 0x1, 0x200)
    OP_28(0x3, 0x4, 0x10)
    OP_28(0x4, 0x4, 0x40)
    OP_28(0x6, 0x4, 0x40)
    Event(0, 18)
    Jump("loc_4ED")

    label("loc_4C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ED")
    SetChrPos(0x0, 84098, 0, 52559, 270)
    OP_69(0x0, 0x0)

    label("loc_4ED")

    Jump("loc_5DB")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_514")
    SetChrPos(0x0, 75765, 0, 54963, 90)
    OP_69(0x0, 0x0)

    label("loc_514")

    Jump("loc_5DB")

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55C")
    EventBegin(0x0)
    SetChrPos(0x101, -5800, 0, -3300, 0)
    SetChrPos(0x102, -4800, 0, -3300, 0)
    SetChrPos(0x8, -1180, 1750, 3000, 0)
    Event(0, 22)

    label("loc_55C")

    Jump("loc_5DB")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D8")
    SetChrPos(0x101, 81771, 0, 55487, 0)
    SetChrPos(0x102, 81444, 0, 54476, 0)
    SetChrPos(0x8, 83000, 0, 53344, 0)
    SetChrPos(0xC, 81266, 0, 53214, 0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x25A)
    OP_28(0x1A, 0x4, 0x4)
    OP_28(0x1A, 0x1, 0x1)
    OP_28(0x1A, 0x1, 0x2)
    ClearChrFlags(0xC, 0x80)
    OP_69(0x101, 0x0)
    Event(0, 16)

    label("loc_5D8")

    Jump("loc_5DB")

    label("loc_5DB")

    Return()

    # Function_0_34E end

    def Function_1_5DC(): pass

    label("Function_1_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F4")
    OP_B1("t0210_y")
    Jump("loc_5FD")

    label("loc_5F4")

    OP_B1("t0210_n")

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_614")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    Jump("loc_62C")

    label("loc_614")

    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 6)), scpexpr(EXPR_END)), "loc_627")
    OP_64(0x1, 0x1)
    Jump("loc_62C")

    label("loc_627")

    ClearChrFlags(0xE, 0x80)

    label("loc_62C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_64A")

    Return()

    # Function_1_5DC end

    def Function_2_64B(): pass

    label("Function_2_64B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_660")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_64B")

    label("loc_660")

    Return()

    # Function_2_64B end

    def Function_3_661(): pass

    label("Function_3_661")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_AE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A32")
    OP_A2(0x0)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "#600F喔，是艾丝蒂尔和约修亚啊。\x02\x03",
            "#600F这次真的是给你们添了很多麻烦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F不，请别这么说……\x02\x03",
            "#015F而且我们最后还是让犯人逃走了，\x01",
            "真是感到抱歉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#601F没事没事，\x01",
            "你们能够平安无事，结晶又能拿回来，\x01",
            "对我来说这样已经足够了。\x02\x03",
            "#600F我听说柏斯地区\x01",
            "最近好像有一群空贼在四处作案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F嗯嗯，好像是呢。\x02\x03",
            "而且那些犯人居然会开飞艇，\x01",
            "让他们逃走了我真是不甘心啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "#601F哈哈，竟然还有飞艇，\x01",
            "这样你们行动的时候要更加小心才行。\x02\x03",
            "#602F不过，说起来柏斯\x01",
            "最近发生了一宗定期船失踪事件。\x02\x03",
            "详细的情况我也不是很清楚，\x01",
            "不过，现在王国军应该在调查吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#603F继续任由空贼作乱下去也不是办法啊。\x01",
            "是不是该和柏斯的市长联系一下呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE0")

    label("loc_A32")


    ChrTalk(
        0xFE,
        (
            "#602F我也在担心定期船失踪这件事。\x01",
            "这样继续任由空贼作乱也不行啊。\x02\x03",
            "试试和柏斯的市长联系一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE0")

    Jump("loc_15C6")

    label("loc_AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEE")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#600F想不到我不在期间居然发生了这种事……\x01",
            "　\x02\x03",
            "调查事宜我已经委托给协会了。\x01",
            "　\x02\x03",
            "麻烦你们了，\x01",
            "这件事都靠你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA2")

    label("loc_BEE")


    ChrTalk(
        0xFE,
        (
            "#600F调查事宜我已经委托给协会了。\x01",
            "　\x02\x03",
            "麻烦你们了，\x01",
            "这件事都靠你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA2")

    Jump("loc_15C6")

    label("loc_CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_END)), "loc_D1E")

    ChrTalk(
        0xFE,
        (
            "#600F我回来的时候\x01",
            "就看到家里已经变成这个样子了……\x02\x03",
            "连犯人的影子我也没有看见。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C6")

    label("loc_D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDF")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#600F你们俩都做得很好，\x01",
            "把结晶平安送来了。\x02\x03",
            "听说你们最近也相当活跃啊。\x01",
            "　\x02\x03",
            "希望你们今后也在协会的工作中大展身手。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_DDF")


    ChrTalk(
        0xFE,
        (
            "#600F希望你们今后也在协会的工作中大展身手。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E20")

    Jump("loc_15C6")

    label("loc_E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_END)), "loc_F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA8")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#600F矿山就在洛连特北部，\x01",
            "玛鲁加山道的尽头。\x02\x03",
            "离这儿也不是太远。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0B")

    label("loc_EA8")


    ChrTalk(
        0xFE,
        (
            "#600F只要你们出示介绍信，\x01",
            "应该就能够进入矿山了。\x02\x03",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0B")

    Jump("loc_15C6")

    label("loc_F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_FAF")

    ChrTalk(
        0x8,
        (
            "#600F玛鲁加的新矿脉中\x01",
            "似乎发现了了不起的东西呢。\x02\x03",
            "我已经委托游击士协会负责运送了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C6")

    label("loc_FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1079")

    ChrTalk(
        0xFE,
        (
            "#600F听说北边的玛鲁加矿山\x01",
            "发现了新矿脉。\x02\x03",
            "听说是条很有潜力的矿脉，\x01",
            "真是令人振奋的消息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C6")

    label("loc_1079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1212")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C4")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#600F百日战役之后，\x01",
            "利贝尔王国复兴的速度非常之惊人。\x01",
            "　\x02\x03",
            "和帝国的邦交正常化\x01",
            "促进了导力技术和贸易的发展……\x02\x03",
            "艾莉茜雅女王执政方针非常正确。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120F")

    label("loc_11C4")


    ChrTalk(
        0x8,
        (
            "#600F呵呵……\x01",
            "艾莉茜雅女王执政方针非常正确啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120F")

    Jump("loc_15C6")

    label("loc_1212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_139C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1316")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#600F洛连特和其他的都市相比较而言\x01",
            "的确是个相当平凡的乡间小镇。\x01",
            "　\x02\x03",
            "但是我个人却很喜欢这里。\x01",
            "　\x02\x03",
            "洛连特的人们非常纯朴善良。\x01",
            "　\x02\x03",
            "我认为这种朴实的民风非常的珍贵呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1399")

    label("loc_1316")


    ChrTalk(
        0x8,
        (
            "#600F洛连特的人们非常纯朴善良。\x01",
            "　\x02\x03",
            "我认为这种朴实的民风非常的珍贵呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1399")

    Jump("loc_15C6")

    label("loc_139C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1533")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#600F哦，早上好啊。\x01",
            "是艾丝蒂尔和约修亚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F早上好啊，市长爷爷。\x02",
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
            "#600F我听到了关于你们俩的传闻了哦。\x02\x03",
            "马上就要接受游击士研修训练了吧。\x01",
            "　\x02\x03",
            "#601F你们这样的年轻人能够以成为游击士为志向，\x01",
            "保护大家的安全，真是非常好啊。\x01",
            "　\x02\x03",
            "我很期待你们的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，我们会加油的！\x02",
    )

    CloseMessageWindow()
    Jump("loc_15C6")

    label("loc_1533")


    ChrTalk(
        0x8,
        (
            "#601F你们这样的年轻人能够以成为游击士为志向，\x01",
            "保护大家的安全，真是非常好啊。\x01",
            "　\x02\x03",
            "我很期待你们的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C6")

    TalkEnd(0x8)
    Return()

    # Function_3_661 end

    def Function_4_15CA(): pass

    label("Function_4_15CA")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_16AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1679")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "家里遭到了打劫，\x01",
            "但幸好谁也没有受伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当时一想到那些人\x01",
            "会不会对老伴和玲达做些什么，\x01",
            "我就非常担心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AB")

    label("loc_1679")


    ChrTalk(
        0xFE,
        (
            "艾丝蒂尔、约修亚，\x01",
            "真的十分感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AB")

    Jump("loc_21D4")

    label("loc_16AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1725")

    ChrTalk(
        0xFE,
        (
            "那些人走的时候\x01",
            "好像还拿了好几包吃的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "难道他们当时也很饿了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D4")

    label("loc_1725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_END)), "loc_19A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1938")
    EventBegin(0x0)
    OP_69(0x9, 0x3E8)
    OP_A2(0x25C)
    OP_28(0x1A, 0x1, 0x20)

    ChrTalk(
        0x101,
        "#002F米蕾奴婶婶，您没事吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯，不用担心。\x01",
            "我没有受到粗暴对待呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F请问市长夫人，关于那些犯人，\x01",
            "您有没有注意到什么特别的事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因为那些人都蒙着面，\x01",
            "所以没办法分辨他们的面部特征……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "而且我记得很清楚，\x01",
            "家里大门明明锁得好好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "老伴去了教会，家里只留下两个女人，\x01",
            "锁上大门也是为了保险起见嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那些人到底是从\x01",
            "什么地方进来的呢……？\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_19A5")

    label("loc_1938")


    ChrTalk(
        0x9,
        (
            "那些人走的时候\x01",
            "好像还拿了好几包吃的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "难道他们当时也很饿了？\x02",
    )

    CloseMessageWindow()

    label("loc_19A5")

    Jump("loc_21D4")

    label("loc_19A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB1")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "听说你们受我丈夫之托，\x01",
            "要去办一件事情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们俩这么年轻就这么能干。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说卡西乌斯出差了，\x01",
            "不过有你们俩在这里的话，\x01",
            "洛连特的市民也安心很多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B16")

    label("loc_1AB1")


    ChrTalk(
        0xFE,
        (
            "虽说卡西乌斯出差了，\x01",
            "不过有你们俩在这里的话，\x01",
            "洛连特的市民也安心很多呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B16")

    Jump("loc_21D4")

    label("loc_1B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1C59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE4")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "玲达说，\x01",
            "帕赛尔农场\x01",
            "最近不能运送蔬菜过来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到底怎么回事呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那里的蔬菜真的很新鲜，\x01",
            "好吃极了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_1BE4")


    ChrTalk(
        0xFE,
        (
            "玲达说，\x01",
            "帕赛尔农场\x01",
            "最近不能运送蔬菜过来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到底怎么回事呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1C56")

    Jump("loc_21D4")

    label("loc_1C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1D9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D24")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "我们儿子\x01",
            "在卢安附近的\x01",
            "杰尼丝王立学院那里教书呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从儿子走了以后\x01",
            "总觉得家里空荡荡的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "真是有些寂寞呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D9B")

    label("loc_1D24")


    ChrTalk(
        0xFE,
        (
            "我们儿子\x01",
            "在卢安附近的\x01",
            "杰尼丝王立学院那里教书呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从儿子走了以后\x01",
            "总觉得家里空荡荡的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9B")

    Jump("loc_21D4")

    label("loc_1D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1F07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E83")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "对了，是不是该叫玲达过来\x01",
            "和我一起准备晚餐了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我想，\x01",
            "今天就给老伴儿做\x01",
            "他喜欢的罗宋汤吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "我先去和玲达商量一下。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_1E83")


    ChrTalk(
        0x9,
        (
            "我想，\x01",
            "今天就给老伴儿做\x01",
            "他喜欢的罗宋汤吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "我先去和玲达商量一下。\x02",
    )

    CloseMessageWindow()

    label("loc_1F04")

    Jump("loc_21D4")

    label("loc_1F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_20DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2056")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "玲达把所有的家务活\x01",
            "都包揽了下来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好像不干点什么\x01",
            "就镇静不下来一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "肯定是因为她来我们家之前\x01",
            "就天天习惯于干家务了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果让她休息一会儿的话，\x01",
            "她反而会不知所措吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D8")

    label("loc_2056")


    ChrTalk(
        0x9,
        (
            "玲达把所有的家务活\x01",
            "都包揽了下来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好像不干点什么\x01",
            "就镇静不下来一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D8")

    Jump("loc_21D4")

    label("loc_20DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2192")
    OP_A2(0x1)

    ChrTalk(
        0x101,
        (
            "#000F米蕾奴婶婶，\x01",
            "早上好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哎呀，早上好。\x01",
            "艾丝蒂尔和约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "你们一大早就出门了？\x01",
            "真是辛苦了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D4")

    label("loc_2192")


    ChrTalk(
        0x9,
        (
            "你们一大早就出门了？\x01",
            "真是辛苦了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D4")

    TalkEnd(0x9)
    Return()

    # Function_4_15CA end

    def Function_5_21D8(): pass

    label("Function_5_21D8")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_22F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2273")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "终于把乱糟糟的书房\x01",
            "给打扫干净了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可是每天都把这里弄得干干净净的，\x01",
            "不能饶恕那些家伙，哼哼哼！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F5")

    label("loc_2273")


    ChrTalk(
        0xFE,
        (
            "要是我看到那些犯人，\x01",
            "一定要用抹布抽他们的脸，\x01",
            "用扫帚打他们一顿～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F5")

    Jump("loc_2B15")

    label("loc_22F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_END)), "loc_2553")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247F")
    EventBegin(0x0)
    OP_69(0xA, 0x3E8)
    OP_A2(0x25B)
    OP_28(0x1A, 0x1, 0x10)

    ChrTalk(
        0xA,
        "真是的！吓死我了～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "当时我在阁楼打扫卫生，\x01",
            "突然有一群蒙面的男人\x01",
            "闯了进来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F一群蒙面的男人……\x01",
            "也就是说，犯人不止一个了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F是几个人的团伙？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "让我想想……\x01",
            "大概有三、四个人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "啊，说起来，\x01",
            "其中有一个人的个子比较矮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "说不定是女的呢。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_2550")

    label("loc_247F")


    ChrTalk(
        0xA,
        (
            "前几天好不容易把书房打扫干净，\x01",
            "现在又搞得乱糟糟的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "要是你们抓到那些犯人，\x01",
            "一定要给我好好教训他们才行！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2550")

    Jump("loc_2B15")

    label("loc_2553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_26DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2648")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "接下来得打扫阁楼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那里的房间暗暗的，\x01",
            "还时不时有老鼠蹿出来，\x01",
            "有点紧张呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呜～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "鬼我倒是不怕，\x01",
            "但老鼠实在是很讨厌。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DA")

    label("loc_2648")


    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "接下来得打扫阁楼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那里的房间暗暗的，\x01",
            "还时不时有老鼠蹿出来，\x01",
            "有点紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26DA")

    Jump("loc_2B15")

    label("loc_26DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_2771")

    ChrTalk(
        0xFE,
        (
            "现在书房里\x01",
            "有一位客人来访。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果找市长有事的话，\x01",
            "就请轻轻地进去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B15")

    label("loc_2771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_283B")

    ChrTalk(
        0xFE,
        (
            "帕赛尔农场\x01",
            "终于又开始供应蔬菜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过今年的\x01",
            "气候也并不坏啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是发生什么事了吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B15")

    label("loc_283B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2845")
    Jump("loc_2B15")

    label("loc_2845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_28C1")

    ChrTalk(
        0xA,
        (
            "啊……\x01",
            "今天要准备哪些菜式呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "我得去和夫人商量一下。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B15")

    label("loc_28C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_29FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A6")
    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "夫人还来帮助我，\x01",
            "和我一起工作哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就像对待自己\x01",
            "家里的亲人一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "之前还无论如何\x01",
            "也要我和他们一起用餐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "我真是太感动了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FB")

    label("loc_29A6")


    ChrTalk(
        0xA,
        (
            "夫人对我就像对待\x01",
            "自己家里的亲人一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "我真是太感动了！\x02",
    )

    CloseMessageWindow()

    label("loc_29FB")

    Jump("loc_2B15")

    label("loc_29FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB6")
    OP_A2(0x2)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "呼呼，忙死了忙死了。\x01",
            "这个屋子实在是太大了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "要做的杂务有扫除和洗涤，\x01",
            "早晨真是女佣最忙的时间啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B15")

    label("loc_2AB6")


    ChrTalk(
        0xA,
        "目标～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "在夫人从教会\x01",
            "回来之前完成扫除！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B15")

    TalkEnd(0xA)
    Return()

    # Function_5_21D8 end

    def Function_6_2B19(): pass

    label("Function_6_2B19")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CBA")
    EventBegin(0x0)

    ChrTalk(
        0xC,
        (
            "#020F刚才我已经向市长\x01",
            "了解整件案件的详细经过了。\x02\x03",
            "#020F你们那边有什么收获吗？\x02",
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
            "『还要再仔细调查一下才行』\x01",      # 0
            "『嗯，已经找到很多的线索』\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2C46"),
        (0, "loc_3C57"),
        (SWITCH_DEFAULT, "loc_3CB7"),
    )


    label("loc_2C46")

    ClearMapFlags(0x1)
    Fade(1000)
    SetChrPos(0x101, 4720, 0, -2800, 90)
    SetChrPos(0x102, 5720, 0, -3920, 0)
    SetChrPos(0xC, 6370, 0, -2250, 225)
    OP_6D(6020, 0, -2610, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#020F那么……\x01",
            "我们就一项一项来确认吧。\x02\x03",
            "#020F首先，犯人的目的是？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【可以换成米拉的东西】\x01",      # 0
            "【保险箱里的七耀石】\x01",        # 1
            "【厨房里的食物】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2DEF"),
        (1, "loc_2E00"),
        (2, "loc_2E11"),
        (SWITCH_DEFAULT, "loc_2E22"),
    )


    label("loc_2DEF")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E22")

    label("loc_2E00")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E22")

    label("loc_2E11")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E22")

    label("loc_2E22")


    ChrTalk(
        0xC,
        "#020F犯人的规模是？\x02",
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
            "【男女二人组】\x01",          # 0
            "【３～４人的团伙】\x01",      # 1
            "【女性的独犯】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F16"),
        (1, "loc_2F27"),
        (2, "loc_2F38"),
        (SWITCH_DEFAULT, "loc_2F49"),
    )


    label("loc_2F16")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F49")

    label("loc_2F27")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F49")

    label("loc_2F38")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F49")

    label("loc_2F49")


    ChrTalk(
        0xC,
        "#020F犯人是怎么进来的？\x02",
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
            "【从一楼的窗户跳进来】\x01",      # 0
            "【撬开大门的锁冲进来】\x01",      # 1
            "【从二楼的阳台爬进来】\x01",      # 2
            "【从屋顶的阁楼闯进来】\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_305C"),
        (1, "loc_306D"),
        (2, "loc_3070"),
        (3, "loc_3081"),
        (SWITCH_DEFAULT, "loc_3084"),
    )


    label("loc_305C")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3084")

    label("loc_306D")

    Jump("loc_3084")

    label("loc_3070")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3084")

    label("loc_3081")

    Jump("loc_3084")

    label("loc_3084")


    ChrTalk(
        0xC,
        (
            "#020F那么，你觉得和这次案件\x01",
            "有嫌疑的应该是什么人？\x02",
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
            "【平时进出的市民】\x01",            # 0
            "【克劳斯市长的家人】\x01",          # 1
            "【玛鲁加矿山的见习矿工】\x01",      # 2
            "【最近来访的旅行者】\x01",          # 3
            "【以上所列的人都不是】\x01",        # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31E3"),
        (1, "loc_31F4"),
        (2, "loc_3205"),
        (3, "loc_3216"),
        (4, "loc_3227"),
        (SWITCH_DEFAULT, "loc_322A"),
    )


    label("loc_31E3")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322A")

    label("loc_31F4")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322A")

    label("loc_3205")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322A")

    label("loc_3216")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322A")

    label("loc_3227")

    Jump("loc_322A")

    label("loc_322A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CA")
    OP_2B(0x1A, 0x4)
    OP_28(0x1A, 0x1, 0x8000)

    ChrTalk(
        0xC,
        (
            "#021F呵呵～调查得相当不错。\x01",
            "这样就可以确定犯人的身份了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FD")

    label("loc_32CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3378")
    OP_2B(0x1A, 0x2)
    OP_28(0x1A, 0x1, 0x4000)

    ChrTalk(
        0xC,
        (
            "#020F嗯，这些线索也有参考价值。\x01",
            "这样就可以确定犯人的身份了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FD")

    label("loc_3378")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_33FD")
    OP_28(0x1A, 0x1, 0x2000)

    ChrTalk(
        0xC,
        (
            "#025F这些线索都互不相关，\x01",
            "不太好确定犯人的身份呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FD")

    TurnDirection(0xC, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0xC,
        (
            "#022F……市长。\x02\x03",
            "#022F请您回忆一下最近几天，\x01",
            "有没有刚认识的人到过书房？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#604F让我想想。\x01",
            "有好几个人呢……\x02\x03",
            "杂志社的两位记者也来过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F怎么，\x01",
            "他们两个也来拜访过市长先生啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F案发当时，\x01",
            "那两位记者和我们一起去了『翡翠之塔』。\x02\x03",
            "#012F我想应该可以排除在嫌疑犯之外。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F原来如此……\x01",
            "市长，除此之外还有其他人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600F除此之外……\x01",
            "就只有乔丝特了。\x02\x03",
            "#601F哈哈哈，不过不可能吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈，那也是。\x01",
            "那孩子不可能是犯人呢。\x02\x03",
            "#001F怎么说也是王立学院的学生啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 225, 400)

    ChrTalk(
        0xC,
        (
            "#022F并不是所有犯人都会\x01",
            "让人一眼就看出来的啊。\x02\x03",
            "#022F校服什么的，\x01",
            "这种东西要做出复制品来也不是什么难事。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(
        0x101,
        (
            "#000F可是，她真的是很乖的孩子呢，\x01",
            "又讲礼貌又像大小姐的样子……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#001F对吧，约修亚？\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#015F很不巧，我的看法正好相反。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F那时——\x01",
            "市长正在把七耀石放进保险箱的时候……\x02\x03",
            "#012F那孩子的眼神就像\x01",
            "猎人盯着猎物一样锐利。\x02\x03",
            "#012F当时没有确实的证据，\x01",
            "而且也没办法当面去问她……\x02\x03",
            "#012F不过，至少在我看来，\x01",
            "她并不是什么单纯的女学生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F不、不会吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#602F真是难以置信……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#022F无论如何，\x01",
            "看来有必要找那女孩问话才行了。\x02\x03",
            "#022F你们知道那女孩现在在哪吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 0)
    Sleep(300)
    TurnDirection(0x102, 0xC, 0)

    ChrTalk(
        0x101,
        (
            "#002F这个嘛～\x01",
            "应该是住在旅馆的吧……\x02\x03",
            "#002F不过她说过\x01",
            "今天就要离开洛连特了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#026F嗯，看来要赶快才行了。\x02\x03",
            "#024F艾丝蒂尔、约修亚。\x01",
            "我们马上去旅馆看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F知道了。\x02",
    )

    CloseMessageWindow()

    def lambda_3BB7():
        OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_3BB7)
    SetChrFlags(0xC, 0x40)
    OP_92(0xC, 0x0, 0x0, 0xBB8, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    OP_A2(0x261)
    OP_28(0x1A, 0x1, 0x200)
    OP_28(0x1B, 0x4, 0x4)
    OP_28(0x1B, 0x1, 0x1)
    OP_28(0x1B, 0x1, 0x2)
    OP_20(0x5DC)
    EventEnd(0x0)
    OP_31(0x2, 0x0, 0xC)
    OP_B5(0x2, 0x0)
    OP_B5(0x2, 0x1)
    OP_B5(0x2, 0x5)
    OP_B5(0x2, 0x4)
    OP_41(0x2, 0x3D)
    OP_41(0x2, 0xF2)
    OP_41(0x2, 0x110)
    OP_41(0x2, 0x26D, 0x0)
    OP_41(0x2, 0x26A, 0x1)
    OP_41(0x2, 0x25E, 0x5)
    OP_41(0x2, 0x267, 0x4)
    OP_35(0x2, 0xAA)
    OP_36(0x2, 0xF0)
    AddParty(0x2, 0xFF)
    ClearMapFlags(0x800)
    OP_21()
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1E()
    Jump("loc_3CB7")

    label("loc_3C57")


    ChrTalk(
        0xC,
        (
            "#020F我就说要你们去调查嘛。\x01",
            "不过，你们动作要快点才行哦。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_3CB7")

    label("loc_3CB7")

    Jump("loc_3D6C")

    label("loc_3CBA")


    ChrTalk(
        0xC,
        (
            "#020F哎呀，这么快就调查完了？\x01",
            "好像太早了吧。\x02\x03",
            "#020F再认真调查一下吧。\x01",
            "说不定有些地方你们还没有调查哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D6C")

    TalkEnd(0xC)
    Return()

    # Function_6_2B19 end

    def Function_7_3D70(): pass

    label("Function_7_3D70")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_470F")
    Fade(1000)
    SetChrPos(0x101, 75500, 0, 55990, 0)
    SetChrPos(0x102, 76250, 0, 55794, 315)
    OP_6D(76000, 0, 56380, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#007F#3P啊～给女王的礼物就这样……\x01",
            "那可是我们辛苦送回来的东西啊。\x02\x03",
            "#005F那些可恶的犯人～绝对不能饶恕！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4P这里看起来……\x01",
            "箱门并没有被破坏的痕迹。\x02\x03",
            "#012F难道是解开密码后打开的，\x01",
            "还是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F#3P解开密码？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F#4P嗯，这并不是不可能。\x01",
            "但是没有专业技术的话很难办到。\x02\x03",
            "#012F我想犯人应该是\x01",
            "通过更简单的方法得知密码的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#3P更简单的方法……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#4P这个嘛……\x02\x03",
            "#012F比如说，\x01",
            "将一种特殊的粉末洒在保险箱的每个按钮上。\x02\x03",
            "#012F那种粉末有极强的吸附性，\x01",
            "而且颗粒很小肉眼看不见。\x02\x03",
            "#012F不过，用蓝色的光照射就会发光。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#3P嗯嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P犯人先洒上那种粉末，\x01",
            "然后趁机让市长去输入密码。\x02\x03",
            "#015F被按到的按钮上的粉末\x01",
            "就自然会被手指沾掉。\x02\x03",
            "#015F这样就不难得知\x01",
            "市长按了哪几个按钮了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#3P等一下。\x01",
            "这样不就不能知道顺序吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4P不，这也不一定。\x02\x03",
            "#012F手指上沾到的粉末越多，\x01",
            "从按钮上沾掉的粉末就会变少。\x02\x03",
            "#012F也就是说，\x01",
            "从发光量少的按钮开始按就对了。\x02\x03",
            "#012F如果数字有重复的话会比较麻烦，\x01",
            "不过还是可以推断出大致的数字来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#3P哦……我明白了。\x01",
            "约修亚，你真是个天才啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P这些都只是基础常识啊。\x01",
            "总之，先调查一下按钮吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_44CF():
        OP_6D(77550, 0, 56660, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44CF)
    OP_8E(0x102, 0x12E8A, 0x0, 0xDAE8, 0x7D0, 0x0)
    OP_8E(0x102, 0x12DCC, 0x0, 0xDE8D, 0x7D0, 0x0)
    OP_8C(0x102, 225, 400)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8E(0x101, 0x12CE6, 0x0, 0xD9EE, 0x7D0, 0x0)
    OP_8E(0x101, 0x12F98, 0x0, 0xDC5A, 0x7D0, 0x0)
    OP_8C(0x101, 270, 400)
    Sleep(2000)
    OP_63(0x102)

    ChrTalk(
        0x102,
        (
            "#012F#3P……果然是那种粉末。\x02\x03",
            "#012F犯人肯定是用我刚才说的方法\x01",
            "打开保险箱的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4P是、是吗……\x02\x03",
            "#006F那现在的问题是，\x01",
            "究竟是谁把粉末洒上去的……\x02\x03",
            "#006F我想至少应该是\x01",
            "进过这间屋子的人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#3P是啊……那才是破案的关键。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x25D)
    OP_28(0x1A, 0x1, 0x4)
    OP_28(0x1A, 0x1, 0x8)
    EventEnd(0x0)
    Jump("loc_4773")

    label("loc_470F")


    ChrTalk(
        0x102,
        (
            "#010F既然知道犯人是如何打开保险箱的了，\x01",
            "那我们再到其他地方调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)

    label("loc_4773")

    Return()

    # Function_7_3D70 end

    def Function_8_4774(): pass

    label("Function_8_4774")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4788")
    Jump("loc_49C1")

    label("loc_4788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47F9")
    EventBegin(0x1)

    ChrTalk(
        0x102,
        (
            "#012F艾丝蒂尔。\x01",
            "我们还是先在屋里调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_49C1")

    label("loc_47F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4938")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -5150, 0, -3680, 180)
    SetChrPos(0x102, -5810, 0, -2850, 180)
    OP_6D(-5150, 0, -2820, 1000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002F案发当时，\x01",
            "大门的确是锁着的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)

    ChrTalk(
        0x101,
        "#002F可是门锁并没有被弄坏啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F也就是说……\x01",
            "犯人是从别的地方进来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x25F)
    OP_28(0x1A, 0x1, 0x40)
    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_49C1")

    label("loc_4938")

    EventBegin(0x1)

    ChrTalk(
        0x102,
        (
            "#012F看起来犯人当时\x01",
            "并不是从大门进来的。\x02\x03",
            "#012F我们到其他地方调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_49C1")

    ClearMapFlags(0x80)
    Return()

    # Function_8_4774 end

    def Function_9_49C7(): pass

    label("Function_9_49C7")

    EventBegin(0x0)
    OP_A2(0x25E)
    OP_28(0x1A, 0x1, 0x100)

    ChrTalk(
        0x101,
        "#004F啊，这个是……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrFlags(0xE, 0x80)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "塞尔贝树叶\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x32A, 1)
    ClearMapFlags(0x1)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x320)

    ChrTalk(
        0x101,
        (
            "#505F这种地方竟然会有树叶，\x01",
            "是不是有些奇怪呢……\x02\x03",
            "而且，\x01",
            "这好像不是附近的树上长的叶子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F真细心啊，艾丝蒂尔。\x02\x03",
            "#010F这个阁楼是当时\x01",
            "市长夫人她们被囚禁的地方。\x02\x03",
            "#010F这树叶有可能是\x01",
            "从犯人身上掉下来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F这么说，是重要的物证呢。\x02",
    )

    CloseMessageWindow()
    OP_64(0x1, 0x1)
    EventEnd(0x1)
    Return()

    # Function_9_49C7 end

    def Function_10_4C15(): pass

    label("Function_10_4C15")

    EventBegin(0x0)
    OP_6D(78710, 0, 52510, 1000)

    ChrTalk(
        0x101,
        (
            "#002F哎呀呀～\x01",
            "桌子被翻得乱七八糟的。\x02\x03",
            "要是被玲达姐姐看见了\x01",
            "她肯定会晕倒的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F而且书架上的书\x01",
            "好像也被犯人弄散了。\x02\x03",
            "犯人这样做究竟是为什么呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_10_4C15 end

    def Function_11_4D0B(): pass

    label("Function_11_4D0B")

    EventBegin(0x0)
    OP_6D(77520, 0, 50360, 1000)

    ChrTalk(
        0x101,
        (
            "#000F啊～\x01",
            "抽屉里面有好几本书呢。\x02\x03",
            "不过并没有被翻过的痕迹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯，好像都是些\x01",
            "和洛连特的行政有关的文件。\x02\x03",
            "这些东西没事，\x01",
            "就说明犯人行事不是出于政治上的目的。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_11_4D0B end

    def Function_12_4E27(): pass

    label("Function_12_4E27")

    EventBegin(0x0)
    OP_6D(82150, 0, 50830, 1000)

    ChrTalk(
        0x101,
        (
            "#008F不愧是市长爷爷啊。\x01",
            "竟然有这么多这么难懂的书～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F好像也有好几本\x01",
            "价值不菲的珍藏版呢。\x02\x03",
            "是犯人不知道它的价值呢，\x01",
            "还是……\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_12_4E27 end

    def Function_13_4F1C(): pass

    label("Function_13_4F1C")

    EventBegin(0x0)
    OP_6D(82490, 310, 57230, 1000)

    ChrTalk(
        0x101,
        (
            "#008F不愧是市长爷爷啊。\x01",
            "竟然有这么多这么难懂的书～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F好像也有好几本\x01",
            "价值不菲的珍藏版呢。\x02\x03",
            "是犯人不知道它的价值呢，\x01",
            "还是……\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_13_4F1C end

    def Function_14_5012(): pass

    label("Function_14_5012")

    EventBegin(0x0)
    OP_6D(78330, 0, 57050, 1000)

    ChrTalk(
        0x101,
        (
            "#000F这个罐子倒了……\x01",
            "里面什么东西也没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x01",
            "看起来只是被撞倒了而已。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_14_5012 end

    def Function_15_50C0(): pass

    label("Function_15_50C0")

    EventBegin(0x0)
    OP_6D(84700, 0, 55320, 1000)

    ChrTalk(
        0x101,
        (
            "#002F这个是杂物箱吧……\x01",
            "不过里面是空的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F箱子盖上的锁像是\x01",
            "被熔化了一样断开了……\x02\x03",
            "说不定……\x01",
            "是用导力枪打断的。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_15_50C0 end

    def Function_16_517B(): pass

    label("Function_16_517B")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_44(0x8, 0xFF)
    OP_44(0xC, 0xFF)
    FadeToBright(2000, 0)
    OP_6B(2600, 0)
    OP_6D(82702, 0, 54610, 0)
    OP_8C(0x101, 315, 0)
    OP_8C(0x102, 270, 0)
    OP_8C(0x8, 270, 0)
    OP_8C(0xC, 225, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F哇～乱七八糟的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#023F搞成这个样子……\x01",
            "犯人还真不是一般的粗暴啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    OP_8C(0xC, 270, 0)
    OP_6D(79224, 0, 54590, 1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0x101, 0x13986, 0x0, 0xD8E0, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        "#004F啊啊，保险箱……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#603F……那块要送给女王的七耀石也被偷走了。\x01",
            "　\x02\x03",
            "之前还特地让你们送过来，\x01",
            "我真是太对不起大家了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 0)
    OP_69(0x102, 0x320)

    ChrTalk(
        0x102,
        (
            "#012F市长您没必要道歉啊。\x01",
            "而且这根本不是您的错。\x02\x03",
            "#012F对了……\x01",
            "其他的房间情况怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#602F其他的房间几乎没有被翻乱的痕迹。\x01",
            "　\x02\x03",
            "最多就是囚禁内人她们的\x01",
            "阁楼房间稍稍有点乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#026F嗯……\x02\x03",
            "#026F…………………………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(
        0xC,
        (
            "#022F艾丝蒂尔、约修亚。\x01",
            "我想让你们两人办点事。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    TurnDirection(0x102, 0xC, 400)

    ChrTalk(
        0x101,
        "#002F什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#022F我要向市长\x01",
            "了解一下这案件的详细情况。\x02\x03",
            "#022F在这段时间里，\x01",
            "你们就在屋里调查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊，那就是……\x01",
            "所谓的现场勘查吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F交给我们可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F正好人手足够，\x01",
            "分头行动的话效率不是更高吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F明白了。\x01",
            "我们会努力去做的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#020F要慎重细致地调查才行啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 400)

    ChrTalk(
        0xC,
        (
            "#020F那么市长，\x01",
            "我们去客厅谈吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 400)

    ChrTalk(
        0x8,
        "#602F嗯，该从何说起呢……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_43(0x8, 0x1, 0x0, 0x11)
    Sleep(500)
    OP_8E(0xC, 0x14A14, 0x0, 0xCF26, 0x7D0, 0x0)
    SetChrFlags(0xC, 0x4)
    OP_8E(0xC, 0x154BE, 0x0, 0xCF26, 0x7D0, 0x0)
    OP_72(0x3, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x3, 9)
    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_71(0x3, 0x800)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x8, 4994, 0, -8380, 315)
    SetChrPos(0xC, 3173, 0, -5730, 135)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x320)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F现场勘查啊……\x01",
            "不禁感到有点紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F我们就从这个房间开始调查吧。\x02\x03",
            "#012F而且还要向屋里的人\x01",
            "听取案件发生时的证言。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，ＯＫ！\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    EventEnd(0x0)
    OP_21()
    SetMapFlags(0x800)
    OP_1D(0x57)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_517B end

    def Function_17_5919(): pass

    label("Function_17_5919")

    Sleep(100)
    OP_8E(0x8, 0x14A14, 0x0, 0xCF26, 0x7D0, 0x0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x9)
    OP_73(0x3)
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0x154BE, 0x0, 0xCF26, 0x7D0, 0x0)
    SetChrFlags(0x8, 0x80)
    Return()

    # Function_17_5919 end

    def Function_18_5962(): pass

    label("Function_18_5962")

    ClearChrFlags(0xB, 0x80)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetMapFlags(0x400000)
    OP_6D(80120, 0, 270, 0)
    OP_6B(3000, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, 78100, 200, -950, 90)
    SetChrPos(0xB, 80250, 0, -950, 270)
    SetChrPos(0x101, 84060, 0, -150, 270)
    SetChrPos(0x102, 84240, 0, -950, 270)
    FadeToBright(2000, 0)
    OP_0D()

    NpcTalk(
        0xB,
        "穿制服的少女",
        (
            "#217F原来如此……\x01",
            "那个钟楼有这样一段逸事啊。\x02\x03",
            "真是太让人感动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#603F用语言来描述战争的悲惨会另有一番意义……\x02\x03",
            "更重要的是可以让人体会到\x01",
            "化悲痛为力量、重建和平的那种坚强。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#604F…………哦？\x02",
    )

    CloseMessageWindow()
    OP_43(0x102, 0x1, 0x0, 0x14)
    OP_8E(0x101, 0x13F9C, 0x0, 0x362, 0xBB8, 0x0)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#000F#1P我们把那东西送回来了……\x02\x03",
            "#000F嗯，打扰你们了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#601F哦，是艾丝蒂尔你们啊。\x01",
            "怎么会打扰呢。\x02\x03",
            "#601F来得正好，我来介绍一下吧。\x02\x03",
            "#601F这位是乔丝特，\x01",
            "杰尼丝王立学院的学生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#1P杰尼丝王立学院……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xB, 400)

    ChrTalk(
        0x102,
        (
            "#010F我听说过。\x02\x03",
            "#010F是卢安地区的那所寄宿制高等院校吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#218F嗯，你说得没错。\x02\x03",
            "初次见面，\x01",
            "我叫乔丝特·哈尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#1P我叫艾丝蒂尔。\x01",
            "请多指教哦，乔丝特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我叫约修亚，请多指教。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600F其实他们俩是游击士。\x02\x03",
            "因为我有点私人的事情，\x01",
            "刚才拜托他们帮我处理。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#217F游击士！？\x02\x03",
            "就是传说中不屈服于任何权势，\x01",
            "以爱好和平为荣耀的自由骑士吗！？\x02\x03",
            "#218F啊啊，我太感动了！\x01",
            "没想到能见到真正的游击士！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#1P你、你这么感动，\x01",
            "连我们都不好意思了……\x02\x03",
            "#008F对了……\x01",
            "啊，能叫你小乔吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#218F嗯，没问题呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#1P小乔你为什么会来这里呢？\x01",
            "和市长爷爷认识吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#217F不是的，\x01",
            "其实今天是第一次见面。\x02\x03",
            "作为自主学习的一部分，\x01",
            "我正在调查各地的重要文化遗产。\x02\x03",
            "明知市长身处百忙之中，\x01",
            "还麻烦他抽出时间和我谈话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#1P嗯～真是刻苦学习啊。\x02\x03",
            "#000F那……我们有没有打扰你？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#217F没有呢，\x01",
            "反正我要调查的东西都已经请教过了。\x02\x03",
            "#217F话说回来……\x01",
            "我还呆在这里是不是不方便呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 400)

    ChrTalk(
        0x8,
        (
            "#600F不不，没这回事啦。\x02\x03",
            "#600F艾丝蒂尔，机会难得，\x01",
            "让她也见识一下那东西吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#1P啊，好。\x01",
            "不过先等一下……\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x15)
    Sleep(500)
    OP_8E(0x102, 0x13826, 0x0, 0x17C, 0xBB8, 0x0)
    SetChrSubChip(0x8, 1)
    OP_8C(0x102, 225, 400)
    Sleep(1000)
    OP_22(0x80, 0x0, 0x64)
    SetChrChipByIndex(0x101, 6)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0x101, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#217F啊……！\x01",
            "那个就是七耀石吧。\x02\x03",
            "#217F真是美丽的光芒啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#601F嗯，大小正合适。\x02\x03",
            "很适合作为表达\x01",
            "洛连特市民感激之情的礼物呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#1P礼物？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P表达感激之情……\x02\x03",
            "#019F原来如此，是女王诞辰庆典的礼物吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#601F真聪明啊，约修亚。\x02\x03",
            "我打算用这个做成导力器工艺品，\x01",
            "赠送给艾莉茜雅女王陛下。\x02\x03",
            "向六十大寿的陛下\x01",
            "表达我们洛连特市民的谢意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P啊啊，是送给女王的礼物！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#218F啊，真是太美妙了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600F我们利贝尔的国民，\x01",
            "一直以来受到女王陛下许多恩惠。\x02\x03",
            "今天能够如此方便地乘坐\x01",
            "定期飞船也是由于王家的资助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P听说利贝尔国内的游击士协会\x01",
            "也同样得到了王家许多方面的援助。\x02\x03",
            "#010F确实……\x01",
            "在各个方面都受到了恩惠啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#1P哇～！\x01",
            "真是太厉害了！\x02",
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
            "#001F#1P喂喂，约修亚，怎么办呢？\x02\x03",
            "#001F我们可是亲手\x01",
            "运送过给女王的礼物呢！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#011F#2P而且你还，\x01",
            "拿着它晃来晃去呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#008F#1P讨厌，不要说出来嘛！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#218F嘻嘻……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#601F哈哈，艾丝蒂尔你啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F#1P真、真是的……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0xB, 0x8, 400)
    OP_43(0x8, 0x1, 0x0, 0x13)

    ChrTalk(
        0x101,
        (
            "#000F#1P市长爷爷。\x01",
            "那我把这个完好无损地交给您了。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "把\x07\x02",
            "七耀石的结晶\x07\x00",
            "交给了市长。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x323, 1)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0x8, 0, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x101, 65535)

    ChrTalk(
        0x8,
        (
            "#602F嗯，确实就是这东西。\x02\x03",
            "那么为了保险起见……\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x10)
    SetChrPos(0x8, 77740, 0, -250, 0)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_8E(0x8, 0x12732, 0x0, 0x762, 0x7D0, 0x0)
    OP_8C(0x8, 0, 400)
    OP_44(0x8, 0xFF)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x68)
    OP_73(0x4)
    Sleep(500)
    SetChrFlags(0x8, 0x4)
    OP_8F(0x8, 0x128C2, 0x0, 0x9CE, 0x7D0, 0x0)
    OP_82(0x0, 0x2)
    Sleep(200)
    PlayEffect(0x0, 0x1, 0xFF, 75970, 500, 3330, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_8F(0x8, 0x12732, 0x0, 0x762, 0x7D0, 0x0)
    OP_22(0xE6, 0x0, 0x64)
    OP_6F(0x4, 104)
    OP_70(0x4, 0x0)
    Sleep(500)
    OP_82(0x1, 0x2)
    OP_73(0x4)
    Sleep(300)

    ChrTalk(
        0x8,
        "#603F……这就可以了。\x02",
    )

    CloseMessageWindow()
    OP_43(0x8, 0x1, 0x0, 0x13)
    OP_8E(0x8, 0x12FAC, 0x0, 0xFFFFFF06, 0x7D0, 0x0)
    Fade(1000)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, 78100, 200, -950, 90)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#601F之后只要请梅尔达斯工房\x01",
            "把它做成导力器工艺品就行了。\x01",
            " \x02\x03",
            "真是期待早日见到成品啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#1P啊，市长爷爷你真狡猾！\x02\x03",
            "#000F做好的话，能让我们看看吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#217F哎呀，真是遗憾……\x01",
            "我可是没办法亲眼看到了。\x02\x03",
            "#218F不过今天不仅增长了很多见闻，\x01",
            "还见到了那么美丽的东西。\x02\x03",
            "我都不知道该说些什么感激的话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600F没事没事，\x01",
            "这也算是市长的义务嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#217F真是太感谢您了。\x02\x03",
            "那么……\x01",
            "我就先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        (
            "#000F#1P等一下，\x01",
            "我们也一起回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)

    ChrTalk(
        0x102,
        (
            "#010F#2P是啊。\x02\x03",
            "#010F市长，我们这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#601F嗯，辛苦你们了。\x02",
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/T0200   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_18_5962 end

    def Function_19_6F37(): pass

    label("Function_19_6F37")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F59")
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    TurnDirection(0xB, 0xFE, 0)
    OP_48()
    Jump("Function_19_6F37")

    label("loc_6F59")

    Return()

    # Function_19_6F37 end

    def Function_20_6F5A(): pass

    label("Function_20_6F5A")

    Sleep(500)
    OP_8E(0x102, 0x14190, 0x0, 0xFFFFFFEC, 0xBB8, 0x0)
    TurnDirection(0x102, 0x8, 0)
    Return()

    # Function_20_6F5A end

    def Function_21_6F7B(): pass

    label("Function_21_6F7B")

    OP_8E(0x101, 0x133F8, 0x0, 0x190, 0xBB8, 0x0)
    OP_8C(0x101, 180, 400)
    TurnDirection(0xB, 0x101, 400)
    Return()

    # Function_21_6F7B end

    def Function_22_6F9E(): pass

    label("Function_22_6F9E")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x8, 0xFF)
    ClearMapFlags(0x1)
    OP_6D(-5266, 0, -1110, 0)
    OP_0D()
    OP_A2(0x23B)
    OP_28(0x3, 0x1, 0x2)
    OP_28(0x3, 0x1, 0x4)

    ChrTalk(
        0x101,
        (
            "#006F那么……\x01",
            "不知道市长爷爷在不在呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F像市长这么忙的人，\x01",
            "这种时间外出了也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P哦哦……\x01",
            "是艾丝蒂尔和约修亚啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 0)
    OP_6D(-2250, 1750, 3170, 2000)

    ChrTalk(
        0x101,
        "#001F#5P啊，市长爷爷。\x02",
    )

    CloseMessageWindow()
    OP_43(0x8, 0x1, 0x0, 0x19)
    OP_43(0x101, 0x1, 0x0, 0x17)
    OP_43(0x102, 0x1, 0x0, 0x18)
    OP_6D(-4620, 0, 1950, 1500)
    Sleep(1500)

    ChrTalk(
        0x102,
        (
            "#010F打扰了。\x01",
            "我们是游击士协会派来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600F嗯，我已经听说了。\x02\x03",
            "你们是代替卡西乌斯\x01",
            "来我这里接受委托的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯，的确是这样没错……\x02\x03",
            "#505F对不起，市长爷爷。\x01",
            "本来应该由老爸来接这个任务的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#603F没事没事，\x01",
            "我知道他有重要的任务去做，\x01",
            "忙得抽不开身也是理所当然的事情。\x02\x03",
            "#600F对了……\x01",
            "站在这里说话不太方便。\x02\x03",
            "详细情况就到书房去谈吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(2000)
    OP_6D(79750, 0, 190, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, 78100, 200, -950, 90)
    SetChrPos(0x101, 80520, 0, -840, 270)
    SetChrPos(0x102, 80370, 0, 180, 225)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#600F……虽说是委托，\x01",
            "其实也不是什么难事。\x02\x03",
            "要协会帮忙做这件事，\x01",
            "我还觉得有点不好意思呢。\x02\x03",
            "只是我手头的工作一直放不开，\x01",
            "所以才想到向协会提出请求。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F听说是运送物品的工作，\x01",
            "到底是些什么东西呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600F嗯，我希望你们能代我\x01",
            "去一趟北边的玛鲁加矿山，\x01",
            "然后把七耀石的结晶送回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F说起七耀石……\x02\x03",
            "和我们平时得到的\x01",
            "『耀晶片』都是同一种东西吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F严格来说，\x01",
            "比宝石小的七耀石碎片才称作耀晶片。\x02\x03",
            "耀晶片经过精制和加工之后，\x01",
            "就可以做成安装在导力器里的结晶回路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F原来是这样啊……\x01",
            "我大概明白是什么意思了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#603F在玛鲁加矿山，\x01",
            "一直都可以开采到\x01",
            "七耀石之一的翠耀石……\x02\x03",
            "最近矿山采集到一块较大的结晶，\x01",
            "目前交由矿长暂时保管。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F从矿长那里取得那块结晶，\x01",
            "然后送回来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600F没错。\x01",
            "怎么样，愿意帮我这个忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F运送宝石啊……\x02\x03",
            "#505F虽然和打倒魔兽不一样\x01",
            "不过还是有一种特别的紧张感……\x02\x03",
            "#001F好吧，这件事就交给我们吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#601F谢谢你们俩。\x02\x03",
            "啊，对了，\x01",
            "你们把这个带上吧。\x02",
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
            "市长的介绍信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x321, 1)

    ChrTalk(
        0x8,
        (
            "#600F把这封信交给门卫，\x01",
            "就可以进入矿山了。\x02\x03",
            "#600F那就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    Return()

    # Function_22_6F9E end

    def Function_23_7B28(): pass

    label("Function_23_7B28")

    OP_8E(0x101, 0xFFFFE69C, 0x0, 0x4EC, 0x7D0, 0x0)
    TurnDirection(0x101, 0x8, 0)
    Return()

    # Function_23_7B28 end

    def Function_24_7B44(): pass

    label("Function_24_7B44")

    Sleep(500)
    OP_8E(0x102, 0xFFFFEBF6, 0x0, 0x3E8, 0x7D0, 0x0)
    TurnDirection(0x102, 0x8, 0)
    Return()

    # Function_24_7B44 end

    def Function_25_7B65(): pass

    label("Function_25_7B65")

    OP_8E(0x8, 0xFFFFEDFE, 0x0, 0xB7C, 0x7D0, 0x0)
    TurnDirection(0x8, 0x101, 0)
    Return()

    # Function_25_7B65 end

    SaveToFile()

Try(main)
