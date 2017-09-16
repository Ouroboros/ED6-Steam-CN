from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3117   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3117.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3117   ._SN',
            'ED6_DT01/T3117_1 ._SN',
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
        '雷伊',                                 # 9
        '蒂亚利',                               # 10
        '安东尼',                               # 11
        '运动鞋',                               # 12
        '书3',                                  # 13
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01660 ._CH',             # 01
        'ED6_DT07/CH01700 ._CH',             # 02
        'ED6_DT06/CH20021 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01660P._CP',             # 01
        'ED6_DT07/CH01700P._CP',             # 02
        'ED6_DT06/CH20021P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 270,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -3620,
        Z                   = 750,
        Y                   = 9560,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1441795,
        ChipIndex           = 0x3,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -410,
        Z                   = 800,
        Y                   = 6880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835011,
        ChipIndex           = 0x3,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 770,
        TriggerZ            = 0,
        TriggerY            = 14240,
        TriggerRange        = 1200,
        ActorX              = 770,
        ActorZ              = 0,
        ActorY              = 14240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4600,
        TriggerZ            = 1000,
        TriggerY            = 12780,
        TriggerRange        = 1200,
        ActorX              = 5880,
        ActorZ              = 2000,
        ActorY              = 13200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -410,
        TriggerZ            = 0,
        TriggerY            = 6880,
        TriggerRange        = 1200,
        ActorX              = -410,
        ActorZ              = 800,
        ActorY              = 6880,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1D6",          # 00, 0
        "Function_1_40A",          # 01, 1
        "Function_2_532",          # 02, 2
        "Function_3_548",          # 03, 3
        "Function_4_56C",          # 04, 4
        "Function_5_619",          # 05, 5
        "Function_6_63A",          # 06, 6
        "Function_7_14B8",         # 07, 7
        "Function_8_2630",         # 08, 8
        "Function_9_269D",         # 09, 9
    )


    def Function_0_1D6(): pass

    label("Function_0_1D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_20C")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_242")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_278")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_29F")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 500, 0, 2880, 271)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_3DE")

    label("loc_29F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_2D5")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 4600, 1000, 13110, 69)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2DF")
    Jump("loc_3DE")

    label("loc_2DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2FF")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_33A")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_33A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_370")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3AB")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2790, 0, 9200, 270)
    SetChrFlags(0x9, 0x10)
    Jump("loc_3DE")

    label("loc_3AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3DE")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)

    label("loc_3DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3EE")
    SetChrFlags(0xB, 0x80)

    label("loc_3EE")

    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_409")
    ClearChrFlags(0xC, 0x80)

    label("loc_409")

    Return()

    # Function_0_1D6 end

    def Function_1_40A(): pass

    label("Function_1_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_422")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44F")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44F")

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_502")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FB")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    PlayEffect(0x0, 0x0, 0xFF, 770, 0, 14240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_4FF")

    label("loc_4FB")

    OP_64(0x0, 0x1)

    label("loc_4FF")

    Jump("loc_506")

    label("loc_502")

    OP_64(0x0, 0x1)

    label("loc_506")

    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_526")
    OP_65(0x2, 0x1)

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_531")
    OP_64(0x1, 0x1)

    label("loc_531")

    Return()

    # Function_1_40A end

    def Function_2_532(): pass

    label("Function_2_532")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_547")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_532")

    label("loc_547")

    Return()

    # Function_2_532 end

    def Function_3_548(): pass

    label("Function_3_548")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56B")
    OP_8D(0xFE, -2990, 4830, 3120, 870, 3000)
    Jump("Function_3_548")

    label("loc_56B")

    Return()

    # Function_3_548 end

    def Function_4_56C(): pass

    label("Function_4_56C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_611")
    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【对话】\x01",              # 0
            "【报告测试结果】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_5F9"),
        (1, "loc_603"),
        (SWITCH_DEFAULT, "loc_60D"),
    )


    label("loc_5F9")

    Call(0, 6)
    TalkEnd(0xFE)
    Jump("loc_60D")

    label("loc_603")

    Call(1, 3)
    TalkEnd(0xFE)
    Jump("loc_60D")

    label("loc_60D")

    Return()

    label("loc_611")

    Call(0, 6)
    TalkEnd(0xFE)
    Return()

    # Function_4_56C end

    def Function_5_619(): pass

    label("Function_5_619")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_636")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵呀呵。\x02",
    )

    CloseMessageWindow()

    label("loc_636")

    TalkEnd(0xFE)
    Return()

    # Function_5_619 end

    def Function_6_63A(): pass

    label("Function_6_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6D3")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "这次真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "得到了最低限度的资料，\x01",
            "总会对研究有一点帮助的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，你们请多保重。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B4")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_73A")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "辛苦了。\x01",
            "你们做得很好，帮了我大忙啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，你们请多保重。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B4")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_8A3")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_810")

    ChrTalk(
        0xFE,
        (
            "我好不容易积攒了\x01",
            "下一阶段的研究费……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "雷伊前辈打算就靠那个西红柿\x01",
            "混过下个阶段的研究吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "运、运动鞋的研究\x01",
            "我也必须要努力才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A0")

    label("loc_810")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "真、真是难以置信，\x01",
            "那个苦西红柿\x01",
            "竟然也有人要订货。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……这、这个世界\x01",
            "到底是怎么了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A0")

    Jump("loc_14B4")

    label("loc_8A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_AEB")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AB")

    ChrTalk(
        0xFE,
        (
            "为了得到研究的预算，\x01",
            "不得不多少谎报一些事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是我自己\x01",
            "并不擅长说谎啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在进行的运动鞋研究\x01",
            "说什么也要做出实际的成绩来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE8")

    label("loc_9AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A64")

    ChrTalk(
        0xFE,
        (
            "为了得到研究的预算，\x01",
            "果然还是要多少谎报一些事情吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过像雷伊前辈那样\x01",
            "基本上全是谎报的，\x01",
            "我还是觉得有点过分了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE8")

    label("loc_A64")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "为了得到研究的预算，\x01",
            "果然还是要多少谎报一些事情吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……可是说起来\x01",
            "我自己也不擅长说谎啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE8")

    Jump("loc_14B4")

    label("loc_AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_C89")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BBE")

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "雷伊前辈，适可而止吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，就靠那样的研究题材\x01",
            "也能得到不错的评价，\x01",
            "不能不说前辈很厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也要以运动鞋的开发\x01",
            "作为新的起点再加把劲了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C86")

    label("loc_BBE")


    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "雷伊前辈，适可而止吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，就靠那样的研究题材\x01",
            "也能得到不错的评价，\x01",
            "不能不说前辈很厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那种没有节制的随机应变，\x01",
            "我要稍微学习一下才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C86")

    Jump("loc_14B4")

    label("loc_C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_E0F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D1B")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "实验室没有受害真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且测试也顺利完成了，\x01",
            "可以按照日程来进行下面的工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0C")

    label("loc_D1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_D99")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "实验室没有受害真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来，测试结束之后\x01",
            "就可以按照日程来进行下面的工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0C")

    label("loc_D99")


    ChrTalk(
        0xFE,
        (
            "哈～～太好了。\x01",
            "实验室没有什么变化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "制造商送来的样品\x01",
            "也毫发无损。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0C")

    Jump("loc_14B4")

    label("loc_E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_FBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E83")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "测试就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "抱着踏破鞋底的决心\x01",
            "去好好测试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBC")

    label("loc_E83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EF8")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哎呀，真是辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次你们干得不错，\x01",
            "帮了我大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再过不久成品就能上市了，\x01",
            "敬请期待哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBC")

    label("loc_EF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_F74")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "嗨～运动鞋的状况怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到各个地方去转一转，\x01",
            "然后回到我这里来报告就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBC")

    label("loc_F74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_F85")
    Call(1, 2)
    Jump("loc_FBC")

    label("loc_F85")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "嗯？什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是来找雷伊前辈的吗？\x01",
            "他出去吃午饭了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBC")

    Jump("loc_14B4")

    label("loc_FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_11C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1033")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "测试就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "抱着踏破鞋底的决心\x01",
            "去好好测试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C4")

    label("loc_1033")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10A8")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哎呀，真是辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次你们干得不错，\x01",
            "帮了我大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再过不久成品就能上市了，\x01",
            "敬请期待哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C4")

    label("loc_10A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1124")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "嗨～运动鞋的状况怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到各个地方去转一转，\x01",
            "然后回到我这里来报告就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C4")

    label("loc_1124")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1135")
    Call(1, 2)
    Jump("loc_11C4")

    label("loc_1135")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "呼～试制品总算做好了。\x01",
            "之后就是等测试人员过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在那之前，\x01",
            "我还是再调整一下鞋的内垫吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C4")

    Jump("loc_14B4")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1275")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "昨天晚上真是吓了一跳啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们正赶着做试验品，\x01",
            "突然房间一片漆黑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当时的情况\x01",
            "真是乱作一团啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B4")

    label("loc_1275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_136D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 7)), scpexpr(EXPR_END)), "loc_12D8")

    ChrTalk(
        0xFE,
        (
            "怎、怎么觉得背后\x01",
            "有一股视线盯得我如芒在背呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定是错觉啦，错觉。\x01",
            "我还是集中精力工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136A")

    label("loc_12D8")


    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "运动鞋内垫的素材组合\x01",
            "果然是关键呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我可以亲自进行试验，\x01",
            "不过最好还是可以有个体验者……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136A")

    Jump("loc_14B4")

    label("loc_136D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_14B4")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "被雷伊前辈称为\x01",
            "『防止瞌睡食品』的超级蔬果\x01",
            "已经可以吃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然外表看上去\x01",
            "只是个普通的西红柿，\x01",
            "不过味道却是奇苦无比。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为的确是太苦了，\x01",
            "所以睡意一下子就被扫得一干二净……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个和用晾衣服的夹子\x01",
            "制成的『防止瞌睡装置』\x01",
            "是同样的原理哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B4")

    TalkEnd(0xFE)
    Return()

    # Function_6_63A end

    def Function_7_14B8(): pass

    label("Function_7_14B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1570")

    ChrTalk(
        0xFE,
        (
            "呵呵，一会儿就要进行\x01",
            "关于『苦西红柿』的商谈呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果进行顺利的话，\x01",
            "在不远的将来\x01",
            "这种西红柿就会作为食材流通了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼～这样的话，\x01",
            "研究费就又可以大幅增长了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167F")

    label("loc_1570")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "呼呼，该说是天助我也呢，\x01",
            "还是顺理成章呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "推广温室『苦西红柿』的\x01",
            "商谈即将进行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果进行顺利的话，\x01",
            "在不远的将来\x01",
            "这种西红柿就会作为食材流通了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼～这样的话，\x01",
            "研究费就又可以大幅增长了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167F")

    Jump("loc_262C")

    label("loc_1682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_189B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1796")

    ChrTalk(
        0xFE,
        (
            "作为下一阶段的研究主题\x01",
            "来继续进行温室的开发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……当然这只是做个样子，\x01",
            "实际怎么做就凭我自己的喜好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，对于优秀的研究员来说，\x01",
            "必须要具备确保足够资金的手段。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1898")

    label("loc_1796")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "作为下一阶段的研究主题\x01",
            "来继续进行温室的开发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……当然这只是做个样子，\x01",
            "实际怎么做就凭我自己的喜好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～对了。\x01",
            "试试能不能再做出其他的奇怪农作物来\x01",
            "也是很有意思的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1898")

    Jump("loc_262C")

    label("loc_189B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1B08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19B5")

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "终于把这次的论文完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "论文的题目是……\x01",
            "《特殊性能食品『苦西红柿』的\x01",
            "　温室栽培法和营养价值分析》。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵～\x01",
            "好不容易编出了这么多词，\x01",
            "我真是要陶醉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B05")

    label("loc_19B5")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "嘿嘿，这样就……行了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，各位早上好。\x01",
            "这次的论文已经完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "论文的题目是……\x01",
            "《特殊性能食品『苦西红柿』的\x01",
            "　温室栽培法和营养价值分析》。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么样，\x01",
            "看起来挺像回事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵～\x01",
            "好不容易编出了这么多词，\x01",
            "我真是要陶醉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B05")

    Jump("loc_262C")

    label("loc_1B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_1C02")

    ChrTalk(
        0xFE,
        (
            "演算室的导力演算器\x01",
            "『卡佩尔』被抢走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过真是遗憾，\x01",
            "我的西红柿们一点事也没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我本来还在\x01",
            "偷偷地期待着犯人\x01",
            "会对这些西红柿产生兴趣呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……看起来\x01",
            "根本没有被破坏的痕迹呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_262C")

    label("loc_1C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1DC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CA2")

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "最近蒂亚利的态度有些不对头呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明身边就有\x01",
            "我这么一个完美的模范，\x01",
            "他为什么就不会学学呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBE")

    label("loc_1CA2")

    OP_A2(0x0)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "蒂亚利，差不多到该提交\x01",
            "下一阶段研究主题的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……这次我们做什么呢。\x01",
            "你有没有什么好素材？\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x9, 255)
    OP_62(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x9)

    ChrTalk(
        0x9,
        "……不知道。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我正忙着呢。\x01",
            "你自己考虑吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_4B(0x9, 255)

    label("loc_1DBE")

    Jump("loc_262C")

    label("loc_1DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_206A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E6E")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "昨天产生的那种现象很有意思啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家都哀叹这是场灾难，\x01",
            "其实这对研究者来说\x01",
            "不正是个绝好的研究题材吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2067")

    label("loc_1E6E")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "昨天产生的那种现象很有意思啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像是发生了\x01",
            "干涉导力场的作用……\x01",
            "总之那不是普通的现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家都哀叹这是场灾难，\x01",
            "其实这对研究者来说\x01",
            "不正是个绝好的研究题材吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        "提妲小妹妹，你怎么想？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F嗯，是、是啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x107,
        (
            "#562F……其实，\x01",
            "我也觉得挺有趣的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，真不愧是提妲。\x01",
            "这才像是拉赛尔博士孙女嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和蒂亚利\x01",
            "果然不是一个档次的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2067")

    Jump("loc_262C")

    label("loc_206A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_24C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2156")

    ChrTalk(
        0xFE,
        (
            "……真是的，蒂亚利那小子。\x01",
            "就会做一些多余的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "要不要装出一幅困难的样子\x01",
            "好好求一求提妲呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F（……哎～真是个奇怪的人。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_24C2")

    label("loc_2156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 7)), scpexpr(EXPR_END)), "loc_220B")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "如果提妲不想吃的话，\x01",
            "这个苦西红柿就没有用处了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就在温室里面种植着，\x01",
            "你们想要的话就随便拿点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24C2")

    label("loc_220B")

    OP_A2(0x0)
    OP_A2(0x587)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2240")

    ChrTalk(
        0xFE,
        (
            "呵呵，提妲小妹妹。\x01",
            "你来得正好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2296")

    label("loc_2240")

    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "哦，\x01",
            "这不是提妲小妹妹嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵，你来得正好……\x02",
    )

    CloseMessageWindow()

    label("loc_2296")


    ChrTalk(
        0x107,
        "#560F啊，怎么了？雷伊哥哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实在温室的实验中\x01",
            "培育出了很有趣的农作物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我很想让提妲你\x01",
            "尝一尝它的味道，\x01",
            "所以就特别摘了一个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果你愿意的话，\x01",
            "尝尝看怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F啊，雷伊哥哥。\x02\x03",
            "你说的农作物，\x01",
            "是不是西红柿啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，真不愧是提妲。\x01",
            "你知道得还真清楚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F呵呵，是啊。\x01",
            "是蒂亚利哥哥告诉我的。\x02\x03",
            "他说不要上雷伊哥哥的当，\x01",
            "去吃很～苦的西红柿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064F啊，不好了。\x01",
            "我现在正在\x01",
            "给客人们带路呢。\x02\x03",
            "那么我先告辞了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C2")

    Jump("loc_262C")

    label("loc_24C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_262C")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "这次的研究项目是新型的温室………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这真是个无聊的研究。\x01",
            "简直就是浪费我的才能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "在这次实验中种出了一种怪味的西红柿，\x01",
            "倒是唯一令我感到欣慰的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哼哼哼，接下来……\x01",
            "这个西红柿给谁吃好呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_262C")

    TalkEnd(0xFE)
    Return()

    # Function_7_14B8 end

    def Function_8_2630(): pass

    label("Function_8_2630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269C")
    OP_A2(0x5)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "苦西红柿\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x385, 1)
    OP_64(0x1, 0x1)
    TalkEnd(0xFF)

    label("loc_269C")

    Return()

    # Function_8_2630 end

    def Function_9_269D(): pass

    label("Function_9_269D")

    EventBegin(0x0)
    OP_A2(0x54B)
    OP_64(0x0, 0x1)
    OP_2B(0x41, 0x1)
    OP_6D(770, 0, 14240, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B08")
    OP_A2(0x52F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_274E")

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "约修亚，这是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是刚才所说的发烟筒。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C2")

    label("loc_274E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27DE")

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "约修亚，那是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯。\x01",
            "是刚才所说的发烟筒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C2")

    label("loc_27DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2868")

    ChrTalk(
        0x107,
        (
            "#065F啊……\x01",
            "哥哥，这是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是刚才所说的发烟筒。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C2")

    label("loc_2868")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C2")

    ChrTalk(
        0x106,
        (
            "#057F这个……\x01",
            "就是那发烟筒吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F阿加特兄。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28C2")

    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚很熟练地把发烟筒拆散了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x102, -160, 0, 14080, 90)
    SetChrPos(0x101, -420, 0, 15020, 129)
    SetChrPos(0x107, -1610, 0, 13920, 104)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_294D")
    SetChrPos(0x106, -1390, 0, 12660, 34)

    label("loc_294D")

    FadeToBright(600, 0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2E")

    ChrTalk(
        0x101,
        (
            "#501F哇……\x01",
            "烟雾没有了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F约修亚哥哥，\x01",
            "好厉害……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FＯＫ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B05")

    label("loc_2A2E")

    OP_A2(0x53E)

    ChrTalk(
        0x101,
        (
            "#501F哇……\x01",
            "烟雾没有了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F约修亚哥哥，\x01",
            "好厉害……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#052F哦……\x01",
            "还挺有两下子的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B05")

    Jump("loc_2C41")

    label("loc_2B08")

    FadeToDark(600, 0, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚很熟练地把发烟筒拆散了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetChrPos(0x102, -160, 0, 14080, 90)
    SetChrPos(0x101, -420, 0, 15020, 129)
    SetChrPos(0x107, -1610, 0, 13920, 104)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_2B9B")
    SetChrPos(0x106, -1390, 0, 12660, 34)

    label("loc_2B9B")

    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C41")
    OP_A2(0x53E)

    ChrTalk(
        0x106,
        (
            "#052F哦……\x01",
            "还挺有两下子的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C41")

    EventEnd(0x0)
    Return()

    # Function_9_269D end

    SaveToFile()

Try(main)
