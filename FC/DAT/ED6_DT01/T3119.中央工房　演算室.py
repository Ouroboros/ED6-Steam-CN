from ED6ScenarioHelper import *

def main():
    # 中央工房　演算室

    CreateScenaFile(
        FileName            = 'T3119   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3119.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3119   ._SN',
            'ED6_DT01/T3119_1 ._SN',
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
        '特莱斯主任',                           # 9
        '黑衣男子',                             # 10
        '黑衣男子',                             # 11
        '黑衣男子',                             # 12
        '提妲',                                 # 13
        '威尔姆',                               # 14
        '拉赛尔博士',                           # 15
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
        'ED6_DT07/CH01190 ._CH',             # 00
        'ED6_DT07/CH01330 ._CH',             # 01
        'ED6_DT07/CH00100 ._CH',             # 02
        'ED6_DT07/CH00101 ._CH',             # 03
        'ED6_DT07/CH00110 ._CH',             # 04
        'ED6_DT07/CH00111 ._CH',             # 05
        'ED6_DT07/CH00150 ._CH',             # 06
        'ED6_DT07/CH00151 ._CH',             # 07
        'ED6_DT07/CH00060 ._CH',             # 08
        'ED6_DT07/CH01450 ._CH',             # 09
        'ED6_DT06/CH20104 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01190P._CP',             # 00
        'ED6_DT07/CH01330P._CP',             # 01
        'ED6_DT07/CH00100P._CP',             # 02
        'ED6_DT07/CH00101P._CP',             # 03
        'ED6_DT07/CH00110P._CP',             # 04
        'ED6_DT07/CH00111P._CP',             # 05
        'ED6_DT07/CH00150P._CP',             # 06
        'ED6_DT07/CH00151P._CP',             # 07
        'ED6_DT07/CH00060P._CP',             # 08
        'ED6_DT07/CH01450P._CP',             # 09
        'ED6_DT06/CH20104P._CP',             # 0A
    )

    DeclNpc(
        X                   = 600,
        Z                   = 0,
        Y                   = 10300,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 111,
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
        Direction           = 336,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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


    DeclEvent(
        X                   = -118000,
        Y                   = -1000,
        Z                   = 23400,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -106990,
        Y                   = 0,
        Z                   = -550,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = -540,
        TriggerZ            = 0,
        TriggerY            = 6300,
        TriggerRange        = 800,
        ActorX              = -540,
        ActorZ              = 900,
        ActorY              = 6300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -117890,
        TriggerZ            = 0,
        TriggerY            = 24080,
        TriggerRange        = 800,
        ActorX              = -117890,
        ActorZ              = 1000,
        ActorY              = 24080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26A",          # 00, 0
        "Function_1_489",          # 01, 1
        "Function_2_5A2",          # 02, 2
        "Function_3_5B8",          # 03, 3
        "Function_4_D4D",          # 04, 4
        "Function_5_1982",         # 05, 5
        "Function_6_1A3B",         # 06, 6
        "Function_7_1A51",         # 07, 7
        "Function_8_2510",         # 08, 8
        "Function_9_4490",         # 09, 9
        "Function_10_4D55",        # 0A, 10
        "Function_11_4DDD",        # 0B, 11
    )


    def Function_0_26A(): pass

    label("Function_0_26A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_27E"),
        (104, "loc_291"),
        (100, "loc_2A4"),
        (SWITCH_DEFAULT, "loc_2AC"),
    )


    label("loc_27E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28E")
    Event(0, 7)

    label("loc_28E")

    Jump("loc_2AC")

    label("loc_291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A1")
    Event(0, 9)

    label("loc_2A1")

    Jump("loc_2AC")

    label("loc_2A4")

    OP_22(0xE, 0x0, 0x64)
    Jump("loc_2AC")

    label("loc_2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2CC")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)
    Jump("loc_488")

    label("loc_2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2E7")
    SetChrPos(0x8, -670, 0, 5580, 351)
    Jump("loc_488")

    label("loc_2E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_318")
    SetChrPos(0x8, -670, 0, 5580, 351)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 680, 0, 6900, 268)
    Jump("loc_488")

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_349")
    SetChrPos(0x8, -670, 0, 5580, 351)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 680, 0, 6900, 268)
    Jump("loc_488")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_37A")
    SetChrPos(0x8, -670, 0, 5580, 351)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 680, 0, 6900, 268)
    Jump("loc_488")

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_389")
    SetChrFlags(0x8, 0x80)
    Jump("loc_488")

    label("loc_389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_393")
    Jump("loc_488")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_END)), "loc_3B3")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)
    Jump("loc_488")

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_3E4")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)
    SetChrPos(0x8, 470, 0, 6630, 225)
    Jump("loc_488")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_404")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)
    Jump("loc_488")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_424")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)
    Jump("loc_488")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_444")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)
    Jump("loc_488")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_488")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 700, 0, 9380, 353)
    SetChrFlags(0xC, 0x10)
    TurnDirection(0x8, 0xC, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)

    label("loc_488")

    Return()

    # Function_0_26A end

    def Function_1_489(): pass

    label("Function_1_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CE")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CE")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4EE")
    OP_71(0x4, 0x4)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_50D")
    OP_72(0x7, 0x10)
    OP_6F(0x7, 30)

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_577")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_577")

    OP_72(0x8, 0x10)
    Jump("loc_583")

    label("loc_57F")

    OP_64(0x1, 0x1)

    label("loc_583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_595")
    OP_10(0x7, 0x1)
    OP_10(0x1, 0x0)

    label("loc_595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A1")
    OP_64(0x0, 0x1)

    label("loc_5A1")

    Return()

    # Function_1_489 end

    def Function_2_5A2(): pass

    label("Function_2_5A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5A2")

    label("loc_5B7")

    Return()

    # Function_2_5A2 end

    def Function_3_5B8(): pass

    label("Function_3_5B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_7CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_67E")

    ChrTalk(
        0xFE,
        (
            "说真的，我很想开一个晚会\x01",
            "庆祝博士能够平安无事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过说不定军队的耳目还在附近。\x01",
            "现在还是暂且忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C9")

    label("loc_67E")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "哦，\x01",
            "这不是我们的正义使者吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～我从工房船里面\x01",
            "偷偷看了那么一眼，\x01",
            "真的是紧张坏了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当士兵们聚在\x01",
            "集装箱周围的时候，\x01",
            "我以为你们死定了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不由自主就和\x01",
            "在我身边的雷曼抱成一团。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C9")

    Jump("loc_D49")

    label("loc_7CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_91B")

    ChrTalk(
        0xFE,
        (
            "从导力停止现象\x01",
            "联想到了一种新的维护方法……\x01",
            "有试一试的价值呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……就算这么说，\x01",
            "当然也得等到『卡佩尔』\x01",
            "拿回来之后才能进行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士协会也很努力，\x01",
            "我要对他们充满信心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_A10")

    ChrTalk(
        0xFE,
        (
            "就算没有演算导力器，\x01",
            "还可以做一些其他的工作嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正好趁这个机会，\x01",
            "将库存整理一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果『卡佩尔』在的话，\x01",
            "工作效率就比现在要高多了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_AD8")

    ChrTalk(
        0xFE,
        "没想到『卡佩尔』会被抢走……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，抢走它\x01",
            "到底要做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算在中央工房里，\x01",
            "能完全理解『卡佩尔』的人\x01",
            "也只有开发它的拉赛尔博士啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_B53")

    ChrTalk(
        0xFE,
        (
            "哦……\x01",
            "演算导力器的情况\x01",
            "怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从仪表来看\x01",
            "工作应该是正常的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_C0E")

    ChrTalk(
        0xFE,
        (
            "今天早上回来一看，\x01",
            "演算导力器的状况\x01",
            "竟然神奇地恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这到底是怎么回事？\x01",
            "难道是导力停止的原因？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBE")

    label("loc_C0E")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "今天早上回来一看，\x01",
            "演算导力器的状况\x01",
            "竟然神奇地恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明不管怎么修\x01",
            "都没办法弄好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这到底是怎么回事？\x02",
    )

    CloseMessageWindow()

    label("loc_CBE")

    Jump("loc_D49")

    label("loc_CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D49")

    ChrTalk(
        0xFE,
        "啊，真是麻烦呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里刚刚修好，\x01",
            "那里又出了不同的毛病。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样下去\x01",
            "简直就是没完没了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D49")

    TalkEnd(0xFE)
    Return()

    # Function_3_5B8 end

    def Function_4_D4D(): pass

    label("Function_4_D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_ECC")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DCA")

    ChrTalk(
        0xFE,
        (
            "按照工房长的指示，\x01",
            "我们把『卡佩尔』藏了起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为不知道军队的家伙们\x01",
            "什么时候会过来检查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC9")

    label("loc_DCA")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "啊，是你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "谢谢啊。\x01",
            "把『卡佩尔』夺了回来，\x01",
            "干得真是漂亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "博士也平安无事，\x01",
            "心情很久没有这么愉快过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，不过按照工房长的指示，\x01",
            "我们把『卡佩尔』藏了起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为不知道军队的家伙们\x01",
            "什么时候会过来检查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC9")

    Jump("loc_197E")

    label("loc_ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_FD0")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "啊，各位游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我听工房长说了。\x01",
            "虽然我不知道详细的情况，\x01",
            "不过终于要进行营救作战了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我翘首企盼着你们\x01",
            "能够将博士和『卡佩尔』带回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请加油。\x01",
            "愿女神爱德丝保佑你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1012")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "博士能够平安无事就好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_1012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1110")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "总之就算没有『卡佩尔』，\x01",
            "我们也能先尽量\x01",
            "做一些其他工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为成熟的男人，\x01",
            "任何时候都不能消沉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士协会也在努力，\x01",
            "我们能做的只有相信他们，默默等待了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_1110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_1192")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "怎么会这样……\x01",
            "『卡佩尔』竟然被盗走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是对不起拉赛尔博士啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_1192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_12A9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1260")
    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "对话\x01",                # 0
            "询问烟草的事情\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1217")
    Call(1, 2)
    Return()

    label("loc_1217")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哟，各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们要找的东西找到了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A6")

    label("loc_1260")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哟，各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们要找的东西找到了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_12A6")

    Jump("loc_197E")

    label("loc_12A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_142A")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1314")

    ChrTalk(
        0xFE,
        "你们可以亲自去触摸面板试试。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "很快就能够掌握操作的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1427")

    label("loc_1314")


    ChrTalk(
        0xFE,
        (
            "维修长是飞艇坪的负责人，\x01",
            "我想你们一到那里就会找到他的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "汽油的储存地点\x01",
            "导力器生产工场\x01",
            "就在中央工房的地下区域。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们找那里的员工\x01",
            "就可以要到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "如果还有什么问题的话就再来询问吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1427")

    Jump("loc_197E")

    label("loc_142A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1660")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_152F")

    ChrTalk(
        0xFE,
        (
            "今天早上回来一看，\x01",
            "演算导力器\x01",
            "已经没有什么问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果进行顺利的话，\x01",
            "这个机器今天\x01",
            "应该能照常使用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，虽然不清楚原因，\x01",
            "不过现在感觉十分开心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_165D")

    label("loc_152F")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "哦～早上好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "我还真是吓了一跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天早上回来一看，\x01",
            "演算导力器\x01",
            "已经没有什么问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果进行顺利的话，\x01",
            "这个机器今天\x01",
            "应该能照常使用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，虽然不清楚原因，\x01",
            "不过现在感觉十分开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165D")

    Jump("loc_197E")

    label("loc_1660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_18AD")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16CF")

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "再检查一遍\x01",
            "库存的东西吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "这个工作真是花费时间啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AA")

    label("loc_16CF")

    OP_A2(0x0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        "啊，提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才被叫走\x01",
            "真的不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊，特莱斯主任。\x02\x03",
            "演算导力器的情况\x01",
            "现在如何了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还需要更多时间\x01",
            "来找出故障所在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我估计暂时\x01",
            "是没有办法弄好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064F唔～是这样吗……\x02\x03",
            "#561F对不起，\x01",
            "我也帮不上忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没关系，别放在心上。\x01",
            "反正最近也用不到它。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有别的事，\x01",
            "还要再拜托你啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F啊，好的，再见。\x02",
    )

    CloseMessageWindow()

    label("loc_18AA")

    Jump("loc_197E")

    label("loc_18AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_197E")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "这里的演算导力器\x01",
            "出了点问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们试着做了许多调整，\x01",
            "可是导力器好像还是\x01",
            "没有丝毫的改善迹象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "问题发生在模式切换的时候，\x01",
            "你觉得会是\x01",
            "哪里出了毛病呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197E")

    TalkEnd(0xFE)
    Return()

    # Function_4_D4D end

    def Function_5_1982(): pass

    label("Function_5_1982")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A37")

    ChrTalk(
        0xFE,
        (
            "#560F嗯…是吗……\x02\x03",
            "既然模式切换会发生问题，\x01",
            "那可能是储存器方面出了毛病。\x02\x03",
            "那些地方\x01",
            "都已经检查过了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A37")

    TalkEnd(0xFE)
    Return()

    # Function_5_1982 end

    def Function_6_1A3B(): pass

    label("Function_6_1A3B")

    OP_A3(0x540)
    OP_A3(0x541)
    OP_A3(0x542)
    OP_A3(0x543)
    OP_A3(0x544)
    OP_A2(0x545)
    OP_A3(0x546)
    Return()

    # Function_6_1A3B end

    def Function_7_1A51(): pass

    label("Function_7_1A51")

    EventBegin(0x0)
    OP_6D(1330, 0, 10350, 0)
    SetChrPos(0x101, -480, 0, 1250, 0)
    SetChrPos(0x102, -1790, 0, 1330, 0)
    FadeToBright(1000, 0)
    OP_6D(150, 0, 4860, 3000)

    ChrTalk(
        0x101,
        "#509F呜哇～这个房间好像很厉害啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F看来这里\x01",
            "应该就是演算室了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "#4P啊，你们…………\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3B6, 0x0, 0x1AFE, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFFCEA, 0x0, 0xFC8, 0xBB8, 0x0)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#5P没见过你们啊，\x01",
            "到演算室来有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P我是这里的\x01",
            "技术主任特莱斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F初次见面，我们是游击士协会的人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F其实我们是受拉赛尔博士委托\x01",
            "来调查东西的……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0xB4, 0x1F4, 0xBB8, 0x0)

    ChrTalk(
        0x8,
        "#5P拉、拉赛尔博士！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P不、不、不会\x01",
            "又是什么麻烦事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F又、又是……\x01",
            "博士真的一点信用都没有啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P不不，这个嘛……\x01",
            "我当然知道博士是个天才。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P这台导力演算器『卡佩尔』\x01",
            "也是博士开发的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P但是呢，只要和他扯上关系，\x01",
            "麻烦总是络绎不绝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P不过还好有提妲在他身边，\x01",
            "不然惹出的麻烦会更多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F啊哈哈……\x01",
            "我能理解你的心情。\x02\x03",
            "#006F不过这次\x01",
            "应该不会给你们添麻烦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们只是想查一下\x01",
            "中央工房保管备用品的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P哦，是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P保管备用品的地方……\x01",
            "这个应该很容易就能查到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P机会难得，\x01",
            "我就教你们搜索的方法吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)

    def lambda_1F9B():
        OP_6D(340, 0, 6200, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1F9B)

    def lambda_1FB3():
        OP_8E(0xFE, 0x1D6, 0x0, 0x19E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FB3)
    Sleep(500)

    def lambda_1FD3():
        OP_8E(0xFE, 0xFFFFFFCE, 0x0, 0x137E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FD3)
    Sleep(200)

    def lambda_1FF3():
        OP_8E(0xFE, 0xFFFFFB00, 0x0, 0x1342, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FF3)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 270, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 45, 400)

    ChrTalk(
        0x8,
        (
            "这个圆筒型的装置\x01",
            "就是导力演算器『卡佩尔』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在如今的时代里，\x01",
            "飞艇的航空管理控制中\x01",
            "会用到各种各样的导力演算器……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但这个卡佩尔\x01",
            "具备了当今世界上\x01",
            "最快的信息处理速度和高度泛用性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从构造物质的强度计算到信息的搜索，\x01",
            "没有什么能难倒它的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那么，信息搜索的方法是……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 225, 200)

    ChrTalk(
        0x8,
        (
            "首先使用正面的这个控制板，\x01",
            "转换到信息搜索模式。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这样一来，\x01",
            "导力信号会通过配线访问记忆导力器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "记忆导力器里装载有\x01",
            "大量管理和记载信息的\x01",
            "被称为光感应的特殊结晶回路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果有需要的信息，\x01",
            "就能简单地将其引导出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "——刚才说的这些都明白了吧？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "『完全明白！』\x01",      # 0
            "『莫名其妙！』\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_234A"),
        (1, "loc_2427"),
        (SWITCH_DEFAULT, "loc_248C"),
    )


    label("loc_234A")


    ChrTalk(
        0x101,
        "#502F嗯，完全明白了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F好厉害啊，艾丝蒂尔。\x02\x03",
            "这么新的技术，\x01",
            "连我都有点不太不明白。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F骗你的啦，真不好意思。\x02\x03",
            "#509F说实话，\x01",
            "我完全不知道刚才在说什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_248C")

    label("loc_2427")

    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#509F简直是莫名其妙！\x02\x03",
            "从头到尾，\x01",
            "完全不明白是什么意思。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_248C")

    label("loc_248C")


    ChrTalk(
        0x8,
        "算了，详细原理还是跳过吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "模式已经转换好了，\x01",
            "接下来就实际操作一下控制板吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你们很快就会知道怎么用了。\x02",
    )

    CloseMessageWindow()
    OP_65(0x0, 0x1)
    OP_A2(0x514)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_7_1A51 end

    def Function_8_2510(): pass

    label("Function_8_2510")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-200, 0, 7100, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_26BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2677")
    OP_A2(0x533)
    OP_28(0x41, 0x1, 0x8)

    ChrTalk(
        0x107,
        (
            "#065F啊啊！？\x01",
            "『卡佩尔』被……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F『卡佩尔』？\x01",
            "那是什么东西啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是拉赛尔博士开发的\x01",
            "导力演算器。\x02\x03",
            "看来中枢部分\x01",
            "被别人强行拔走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F就是那些家伙拿走的吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F嗯，可能性很高。\x02",
    )

    CloseMessageWindow()
    Jump("loc_26B9")

    label("loc_2677")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力演算器\x01",
            "『卡佩尔』的中枢被拿走了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_26B9")

    EventEnd(0x1)
    Return()

    label("loc_26BC")

    FadeToDark(300, 0, 100)
    OP_22(0x9D, 0x0, 0x64)
    SetChrName("CAPEL")
    SetMessageWindowPos(250, 78, 36, 12)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1SThe Orbal Calculater\x01",
            "CAPEL SYSTEM Ver.7.0\x01",
            "Copyright(C) Z.C.F. 1197-1202\x01",
            "MODE:Information Retrieval\x01",
            "#200W　#20W\x01",
            "MEMORY_CHECK#100W..........#20WOK!\x01",
            "#200W　#20W\x01",
            "正在访问数据库。\x01",
            "请选择搜索项目。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F99")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        55,
        80,
        1,
        "【中央工房关联】　　\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2804"),
        (SWITCH_DEFAULT, "loc_3F89"),
    )


    label("loc_2804")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F79")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        55,
        153,
        1,
        (
            "【设立·沿革】\x01",            # 0
            "【技术一览】\x01",              # 1
            "【关联信息搜索】　　\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_286E"),
        (1, "loc_3144"),
        (2, "loc_3B55"),
        (SWITCH_DEFAULT, "loc_3F69"),
    )


    label("loc_286E")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S【Ｓ１１５４】（Ｓ…七耀历）\x01",
            "Ｃ·爱普斯泰恩博士于列曼自治州去世。\x01",
            "【Ｓ１１５５】\x01",
            "Ａ·拉赛尔博士回到利贝尔王国。\x01",
            "回国后提倡普及导力器技术，\x01",
            "但是没得到世人的认可和支持。\x01",
            "【Ｓ１１５７】\x01",
            "拉赛尔博士带领蔡斯的钟表工匠普及导力器。\x01",
            "同年，『蔡斯技术工房』（即之后的中央工房）设立。\x01",
            "【Ｓ１１６０】\x01",
            "埃德佳Ⅲ世在视察蔡斯技术工房后提供巨额资金建设工\x01",
            "房。拉赛尔博士出任首任工房长。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S【Ｓ１１６２】\x01",
            "埃德佳Ⅲ世去世。艾莉茜雅Ⅱ世即位。\x01",
            "【Ｓ１１６４】\x01",
            "『伦格兰德大桥』落成。\x01",
            "【Ｓ１１６８】\x01",
            "首部导力飞艇『加拉托拉巴号』诞生。\x01",
            "（经过３９次飞行实验失败后的产物）\x01",
            "【Ｓ１１７３】\x01",
            "蔡斯技术工房开始对共和国乌尔努社和帝国莱恩福尔特\x01",
            "社输出导力器技术。工房改名为『中央工房』。\x01",
            "【Ｓ１１７５】\x01",
            "飞艇公社设立。定期船『林德号』开始服役。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S【Ｓ１１７７】\x01",
            "定期船『赛希莉亚号』开始服役。\x01",
            "【Ｓ１１７８】\x01",
            "移动工房船『莱普尼兹号』开始服役。\x01",
            "【Ｓ１１８０】\x01",
            "中央工房搬迁（即现在的建筑物）。\x01",
            "开掘卡鲁迪亚平原丘陵的一角，地下工房建成。\x01",
            "【Ｓ１１８２】\x01",
            "拉赛尔工房长退休。\x01",
            "玛多克技术主任出任第二任工房长。\x01",
            "【Ｓ１１８５】\x01",
            "自然科学和医学研究部门设立。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S【Ｓ１１８７】\x01",
            "客船『埃迪鲁那号』在卡尔瓦德领海沉没。\x01",
            "尤迪斯王太子夫妇去世。\x01",
            "【Ｓ１１９０】\x01",
            "与爱普斯泰恩财团合作，\x01",
            "发表了『导力网络』的构想。\x01",
            "【Ｓ１１９２】\x01",
            "『百日战役』爆发。\x01",
            "中央工房被埃雷波尼亚帝国接管。\x01",
            "拉赛尔博士在雷斯顿要塞开发出警备飞艇，\x01",
            "并将其用于反攻作战中，取得了显赫的战功，\x01",
            "从此警备飞艇作为王国军的主力兵器而被使用。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S【Ｓ１１９３】\x01",
            "利贝尔王国和埃雷波尼亚帝国缔结和平条约。\x01",
            "战后，王国再次向帝国输出导力器。\x01",
            "【Ｓ１１９７】\x01",
            "导力演算器『卡佩尔』Ver.1完成。\x01",
            "【Ｓ１１９９】\x01",
            "高速巡洋舰『埃尔赛尤号』开发工程开始。\x01",
            "【Ｓ１２０２】\x01",
            "高速巡洋舰『埃尔赛尤号』竣工，进入试飞阶段。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F76")

    label("loc_3144")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B45")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        55,
        259,
        1,
        (
            "【导力器】\x01",          # 0
            "【结晶回路】\x01",        # 1
            "【七耀石】\x01",          # 2
            "【飞行船】\x01",          # 3
            "【导力兵器】\x01",        # 4
            "【战术导力器】\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31E0"),
        (1, "loc_3384"),
        (2, "loc_34A2"),
        (3, "loc_35F1"),
        (4, "loc_3788"),
        (5, "loc_3934"),
        (SWITCH_DEFAULT, "loc_3B35"),
    )


    label("loc_31E0")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S项目：导力器（Orbment）\x01",
            "在半世纪前由Ｃ·爱普斯泰恩博士所发明，是能从七耀\x01",
            "石中提取导力，从而引发各种各样现象的机械装置的总\x01",
            "称。导力器内部的构造和齿轮的运动，使加工七耀石而\x01",
            "成的结晶回路相互干涉，可以引发丰富多彩的现象。导\x01",
            "力器的实用性，除了能产生丰富现象以外，还在于拥有\x01",
            "『经过一段时间内部的导力可以自然恢复』这种特异的\x01",
            "便利性。另外，经济效率也要远远地领先于各种外燃、\x01",
            "内燃引擎设备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B42")

    label("loc_3384")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S项目：结晶回路（Quartz）\x01",
            "将七耀石的碎片（耀晶片，Sepith）精制、加工而成的\x01",
            "具有结晶构造的回路。作为能量源的同时，本身还是引\x01",
            "起各种各样现象的装置。但结晶回路必须安装在导力器\x01",
            "内才可以发挥作用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B42")

    label("loc_34A2")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S项目：七耀石（Septium）\x01",
            "是在大陆全土分布的７种贵重矿石的总称。因被人们称\x01",
            "为『古代的宝石』、『神秘的象征』而变得珍重。近代\x01",
            "一种将体积过小不能成为宝石的碎片（耀晶片）精制加\x01",
            "工制作出结晶回路的技术被发明出来，因此导致七耀石\x01",
            "资源的重要性在大陆诸国之间一夜之间变得十分重要。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B42")

    label("loc_35F1")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S项目：导力飞艇\x01",
            "导力飞艇可以称得上是导力技术精华凝聚而成的结晶。\x01",
            "集合了用于重力制御的大型飞翔装置和供给大量能量的\x01",
            "导力机关两大技术，使得如此大的飞艇在空中飞行成为\x01",
            "可能。\x01",
            "为了实现高效率的导力传送和十分复杂的船体控制，最\x01",
            "新的飞艇大多搭载了高性能的导力演算器。２０亚矩以\x01",
            "上的大型飞艇又被称为『飞船』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B42")

    label("loc_3788")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S项目：导力兵器\x01",
            "即以导力枪、导力炮作为代表，使用导力技术的兵器体\x01",
            "系。现在已成为大多数国家军队的主力装备。\x01",
            "导力枪枪管内具有能将能量按照螺旋线聚集并高速射出\x01",
            "豆粒大小的金属子弹的构造，与发射火药的枪相比，填\x01",
            "弹量大幅增加，而且还能够调节枪的威力。\x01",
            "导力炮则可以发射封装了能量的炮弹（导力弹）并产生\x01",
            "爆炸，与发射火药的炮相比，其后坐力小，而且也可以\x01",
            "自由调节威力大小。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B42")

    label("loc_3934")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S项目：战术导力器\x01",
            "可以发动导力魔法的导力器。大小和怀表差不多，内部\x01",
            "构造则相当精致优雅。\x01",
            "战术导力器具有安装结晶回路后能够提高持有者能力的\x01",
            "设计，使内部结晶回路与持有者达到同步，引发出『共\x01",
            "鸣现象』，以代替传统释放魔法所需的复杂的齿轮和驱\x01",
            "动装置，使持有者能够发动各种导力魔法。\x01",
            "而且，根据复数结晶回路属性和势能的组合不同，持有\x01",
            "者能够使用的导力魔法也会发生变化，具有相当的灵活\x01",
            "性。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B42")

    label("loc_3B35")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B42")

    label("loc_3B42")

    Jump("loc_3144")

    label("loc_3B45")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_3F76")

    label("loc_3B55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F59")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        55,
        255,
        1,
        (
            "【内燃引擎设备】\x01",      # 0
            "【汽油】\x01",              # 1
            "【运输车】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3BBE"),
        (1, "loc_3CD4"),
        (2, "loc_3E20"),
        (SWITCH_DEFAULT, "loc_3F49"),
    )


    label("loc_3BBE")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S项目：内燃引擎设备\x01",
            "在机关装置内燃烧燃料以获得能量的动力源。与导力机\x01",
            "关相比经济效率低下，而且还会产生噪音、废气等各种\x01",
            "问题，因此已经停止开发和生产。\x01\x01",
            "『内燃引擎设备』\x01",
            "库存量：１台\x01",
            "管理责任人：格斯塔夫维修长\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3F, 0x1, 0x200)
    OP_A2(0x1)
    Jump("loc_3F56")

    label("loc_3CD4")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S项目：汽油\x01",
            "将天然产生的液态碳氢化合物（石油）分馏、精制而成\x01",
            "的液体。常作为内燃引擎设备的燃料以及工业生产的溶\x01",
            "剂使用。\x01\x01",
            "『共和国产汽油』\x01",
            "库存：中型桶×２０\x01",
            "保管地点：导力器生产工场\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3F, 0x1, 0x400)
    OP_A2(0x2)
    Jump("loc_3F56")

    label("loc_3E20")

    OP_28(0x29, 0x1, 0x8000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S项目：运输车\x01",
            "使用导力机关驱动的各种车辆的总称。因为乘坐的舒适\x01",
            "度较差，速度也很慢，所以基本不用于客运方面，而主\x01",
            "要用来进行中短距离的货物运输。\x01\x01",
            "『运输车用驱动导力器』\x01",
            "库存量：不明\x01",
            "保管地点：地下工场搬入口\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3F46")
    OP_28(0x29, 0x1, 0x8)

    label("loc_3F46")

    Jump("loc_3F56")

    label("loc_3F49")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F56")

    label("loc_3F56")

    Jump("loc_3B55")

    label("loc_3F59")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_3F76")

    label("loc_3F69")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F76")

    label("loc_3F76")

    Jump("loc_2804")

    label("loc_3F79")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    Jump("loc_3F96")

    label("loc_3F89")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F96")

    label("loc_3F96")

    Jump("loc_27B9")

    label("loc_3F99")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_448D")
    OP_A2(0x516)
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        (
            "看起来，\x01",
            "你们找到要找的东西了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#004F哇～\x01",
            "好像魔法箱一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F导力演算器……\x01",
            "真是超出想象的惊人技术啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P提出这个基本概念的人\x01",
            "好像是拉赛尔博士的师傅，\x01",
            "也就是导力器的发明者爱普斯泰恩博士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P不过，能把它发展到这种地步，\x01",
            "拉赛尔博士也确实是天才啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P唉，话虽如此，\x01",
            "要是为人能再沉稳点就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈……\x01",
            "人无完人嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F对了，说到管理内燃引擎的\x01",
            "格斯塔夫维修长这个人……\x02\x03",
            "他在哪里啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P维修长是飞艇坪的责任人，\x01",
            "你们去那里应该能找到他的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P还有，关于汽油方面，\x01",
            "就要到中央工房地下区域的\x01",
            "导力器生产工场去找找。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P你们找那里的员工问问\x01",
            "应该就能要到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F内燃引擎设备是找\x01",
            "飞艇坪的格斯塔夫维修长……\x02\x03",
            "而汽油就是找\x01",
            "导力器生产工场的员工对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F谢谢您！真是帮大忙了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P哪里哪里。\x01",
            "还有什么需要的话再来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 225, 0)
    OP_4B(0x8, 255)

    label("loc_448D")

    EventEnd(0x1)
    Return()

    # Function_8_2510 end

    def Function_9_4490(): pass

    label("Function_9_4490")

    EventBegin(0x0)
    OP_6D(-101380, 0, -1870, 0)
    SetChrPos(0x101, -101860, 0, -2090, 270)
    SetChrPos(0x102, -101400, 0, -890, 270)
    SetChrPos(0x106, -101230, 0, -3040, 270)
    SetChrPos(0x107, -100640, 0, -1840, 270)
    SetChrPos(0x9, -117950, 0, -1340, 280)
    SetChrPos(0xA, -116160, 0, 710, 41)
    SetChrPos(0xB, -116560, 0, -600, 204)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x4)
    SetChrPos(0xE, -117490, 0, 22060, 328)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6D(-103580, 0, -540, 1000)

    ChrTalk(
        0x101,
        "#004F咦，为什么门会……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "男人的声音",
        (
            "#2P……久等了。\x01",
            "最后的目标已经到手了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "男人的声音",
        (
            "#2P好……\x01",
            "那就马上撤离吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "男人的声音",
        "#2P已经准备好了吧？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x9, -118930, 0, 21810, 0)
    SetChrPos(0xA, -117340, 0, 21040, 328)
    SetChrPos(0xB, -117550, 0, 22790, 0)

    ChrTalk(
        0x102,
        "#016F刚才的声音是……！\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x52)

    ChrTalk(
        0x106,
        (
            "#054F快！\x01",
            "导力梯那边！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x106, 6)
    OP_72(0x8, 0x10)
    OP_6F(0x8, 30)

    def lambda_4753():
        OP_6D(-117150, 0, -90, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4753)

    def lambda_476B():
        OP_8E(0xFE, 0xFFFE3EB4, 0x0, 0xFFFFFB50, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_476B)
    Sleep(400)

    def lambda_478B():
        OP_8E(0xFE, 0xFFFE3270, 0x0, 0xFFFFFBA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_478B)
    Sleep(200)

    def lambda_47AB():
        OP_8E(0xFE, 0xFFFE38A6, 0x0, 0xFFFFFCCC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47AB)
    Sleep(100)

    def lambda_47CB():
        OP_8E(0xFE, 0xFFFE366C, 0x0, 0xFFFFF90C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_47CB)
    Sleep(800)

    def lambda_47EB():
        OP_6D(-117430, 0, 16500, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_47EB)

    def lambda_4803():
        OP_67(0, 3630, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4803)

    def lambda_481B():
        OP_6B(3490, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_481B)

    def lambda_482B():
        OP_6C(21000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_482B)
    WaitChrThread(0x106, 0x1)

    def lambda_4840():
        OP_8E(0xFE, 0xFFFE35B8, 0x0, 0x35C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4840)
    WaitChrThread(0x106, 0x1)

    def lambda_4860():
        OP_8E(0xFE, 0xFFFE328E, 0x0, 0x24B8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4860)
    WaitChrThread(0x101, 0x1)

    def lambda_4880():
        OP_8E(0xFE, 0xFFFE2D52, 0x0, 0x22C4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4880)
    WaitChrThread(0x102, 0x1)

    def lambda_48A0():
        OP_8E(0xFE, 0xFFFE35B8, 0x0, 0x21CA, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_48A0)
    WaitChrThread(0x107, 0x1)

    def lambda_48C0():
        OP_8E(0xFE, 0xFFFE3180, 0x0, 0x1EF0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_48C0)
    WaitChrThread(0x107, 0x1)

    ChrTalk(
        0x101,
        "#005F找到了……！\x02",
    )

    CloseMessageWindow()

    def lambda_48F1():
        OP_8C(0xFE, 303, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_48F1)

    def lambda_48FF():
        TurnDirection(0x9, 0x106, 800)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_48FF)

    def lambda_490D():
        TurnDirection(0xA, 0x106, 800)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_490D)
    TurnDirection(0xB, 0x106, 800)
    WaitChrThread(0x106, 0x1)

    ChrTalk(
        0x106,
        "#052F是你们……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x1)

    ChrTalk(
        0x107,
        "#065F爷、爷爷！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔……\x01",
            "阿加特·科洛斯纳！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "麻烦的家伙又来了……\x01",
            "现在我们可没功夫跟你耗！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)

    def lambda_49B1():
        OP_8E(0xFE, 0xFFFE3284, 0x0, 0x645A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_49B1)
    Sleep(500)

    def lambda_49D1():
        OP_8E(0xFE, 0xFFFE3450, 0x0, 0x6284, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_49D1)

    def lambda_49EC():
        OP_8F(0xFE, 0xFFFE32FC, 0x0, 0x576C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_49EC)
    Sleep(50)

    def lambda_4A0C():
        OP_8E(0xFE, 0xFFFE3450, 0x0, 0x666C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4A0C)

    def lambda_4A27():

        label("loc_4A27")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_4A27")

    QueueWorkItem2(0xA, 1, lambda_4A27)

    def lambda_4A38():

        label("loc_4A38")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_4A38")

    QueueWorkItem2(0xB, 1, lambda_4A38)

    def lambda_4A49():

        label("loc_4A49")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_4A49")

    QueueWorkItem2(0x9, 1, lambda_4A49)

    ChrTalk(
        0x101,
        "#005F站、站住！\x02",
    )

    CloseMessageWindow()

    def lambda_4A7B():
        OP_8F(0xFE, 0xFFFE3220, 0x0, 0x6220, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4A7B)

    def lambda_4A96():
        OP_6D(-118050, 0, 23420, 1000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A96)

    def lambda_4AAE():
        OP_8E(0xFE, 0xFFFE3284, 0x0, 0x5A1E, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4AAE)

    ChrTalk(
        0x106,
        "#10A #054F休想逃走，混帐！\x05\x02",
    )

    Sleep(200)

    def lambda_4AEC():
        OP_8E(0xFE, 0xFFFE3040, 0x0, 0x55AA, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4AEC)
    Sleep(200)

    def lambda_4B0C():
        OP_8E(0xFE, 0xFFFE3450, 0x0, 0x546A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4B0C)
    Sleep(500)

    def lambda_4B2C():
        OP_8E(0xFE, 0xFFFE3270, 0x0, 0x4F10, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4B2C)
    Sleep(100)
    OP_70(0x8, 0x0)
    WaitChrThread(0x106, 0x1)
    Fade(500)
    SetChrChipByIndex(0x106, 6)
    OP_6D(-118180, 0, 22740, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x106,
        (
            "#550F可恶……\x01",
            "又被他们逃跑了！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#003F就、就差那么一步……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x1)

    ChrTalk(
        0x107,
        (
            "#065F怎、怎么会……\x02\x03",
            "为什么他们要把爷爷……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F不管怎样，\x01",
            "快从紧急通道追下去吧。\x02\x03",
            "那些黑衣人好像打算\x01",
            "就这样从中央工房逃走。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x106, 65535)
    TurnDirection(0x106, 0x107, 800)

    ChrTalk(
        0x106,
        (
            "#057F哼，要逃的话，\x01",
            "除了从正门之外就是隧道了。\x02\x03",
            "#054F小鬼们，给我快点！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F不用你说我也知道啦！\x02",
    )

    CloseMessageWindow()
    Fade(2000)
    OP_82(0x1, 0x2)
    OP_A2(0x532)
    OP_28(0x41, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_9_4490 end

    def Function_10_4D55(): pass

    label("Function_10_4D55")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "按了按钮，没有任何反应。\x01",
            "导力梯好像不能用了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_4D55 end

    def Function_11_4DDD(): pass

    label("Function_11_4DDD")

    SetPlaceName(0x9A) # 中央工房　演算室
    Return()

    # Function_11_4DDD end

    SaveToFile()

Try(main)
