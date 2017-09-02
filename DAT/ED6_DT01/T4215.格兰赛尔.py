from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4215   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4215.x',
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
        '茜亚',                                 # 9
        '吉尔维厨师长',                         # 10
        '福卢克',                               # 11
        '里吉斯',                               # 12
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
        'ED6_DT07/CH02540 ._CH',             # 03
        'ED6_DT07/CH01280 ._CH',             # 04
        'ED6_DT07/CH01520 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH02540P._CP',             # 03
        'ED6_DT07/CH01280P._CP',             # 04
        'ED6_DT07/CH01520P._CP',             # 05
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -68800,
        Z                   = 0,
        Y                   = 73190,
        Direction           = 270,
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
        X                   = -62700,
        Z                   = 0,
        Y                   = 67500,
        Direction           = 258,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -71490,
        Z                   = 0,
        Y                   = 65550,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_15A",          # 00, 0
        "Function_1_21B",          # 01, 1
        "Function_2_225",          # 02, 2
        "Function_3_3A2",          # 03, 3
        "Function_4_645",          # 04, 4
        "Function_5_7BB",          # 05, 5
        "Function_6_BB2",          # 06, 6
    )


    def Function_0_15A(): pass

    label("Function_0_15A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_184")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_1C6")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -68800, 0, 72170, 273)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x9, -61660, 0, 68120, 76)
    Jump("loc_21A")

    label("loc_1C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1E1")
    SetChrPos(0xB, -68420, 0, 78980, 0)
    Jump("loc_21A")

    label("loc_1E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_1F5")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_21A")

    label("loc_1F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_209")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_21A")

    label("loc_209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_213")
    Jump("loc_21A")

    label("loc_213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_21A")

    label("loc_21A")

    Return()

    # Function_0_15A end

    def Function_1_21B(): pass

    label("Function_1_21B")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_21B end

    def Function_2_225(): pass

    label("Function_2_225")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_38C")

    label("loc_24A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_263")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_38C")

    label("loc_263")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_38C")

    label("loc_27C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_295")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_38C")

    label("loc_295")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_38C")

    label("loc_2AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C7")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_38C")

    label("loc_2C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E0")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_38C")

    label("loc_2E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F9")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_38C")

    label("loc_2F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_312")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_38C")

    label("loc_312")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_38C")

    label("loc_32B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_38C")

    label("loc_344")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35D")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_38C")

    label("loc_35D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_376")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_38C")

    label("loc_376")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_38C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_38C")

    label("loc_3A1")

    Return()

    # Function_2_225 end

    def Function_3_3A2(): pass

    label("Function_3_3A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_3AF")
    Jump("loc_641")

    label("loc_3AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_404")

    ChrTalk(
        0xFE,
        (
            "不单是发动了政变，\x01",
            "居然还把老鼠带来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "情报部的家伙，太可耻了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BA")

    label("loc_404")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "我知道老鼠是从哪儿来的了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟然是从宝物库的\x01",
            "深处跑出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不单是发动了政变，\x01",
            "居然还把老鼠带来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "情报部的家伙，太可耻了！\x02",
    )

    CloseMessageWindow()

    label("loc_4BA")

    Jump("loc_641")

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_4C7")
    Jump("loc_641")

    label("loc_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_4D1")
    Jump("loc_641")

    label("loc_4D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_580")

    ChrTalk(
        0xFE,
        (
            "为了不让老鼠糟蹋粮食，\x01",
            "必须把食物小心保管起来才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过话说回来，\x01",
            "老鼠为何那么喜欢奶酪呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_641")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5BC")

    ChrTalk(
        0xFE,
        (
            "这些可恶的老鼠，\x01",
            "到底是从哪里钻进来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_641")

    label("loc_5BC")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "感觉最近老鼠\x01",
            "好像多了起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于讨厌老鼠的我来说，\x01",
            "这可是超紧急事态啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_641")

    TalkEnd(0xFE)
    Return()

    # Function_3_3A2 end

    def Function_4_645(): pass

    label("Function_4_645")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_652")
    Jump("loc_7B7")

    label("loc_652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6D3")

    ChrTalk(
        0xFE,
        (
            "做蔬菜料理\x01",
            "可是我的拿手戏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为我是在洛连特长大的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B7")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_6DD")
    Jump("loc_7B7")

    label("loc_6DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_6E7")
    Jump("loc_7B7")

    label("loc_6E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_72D")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "早点收拾好就可以回家了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B7")

    label("loc_72D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_7B7")

    ChrTalk(
        0xFE,
        (
            "厨师长不仅精于宫廷料理，\x01",
            "而且据说他可以烹制出\x01",
            "上千种各式风味的料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B7")

    TalkEnd(0xFE)
    Return()

    # Function_4_645 end

    def Function_5_7BB(): pass

    label("Function_5_7BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_832")

    ChrTalk(
        0xFE,
        (
            "鸡骨头、洋葱、芹菜、\x01",
            "胡萝卜、月桂叶还有香菜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我正在调制\x01",
            "明天做饭用的底汤。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAE")

    label("loc_832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_894")

    ChrTalk(
        0xFE,
        (
            "陛下和公主好久没有\x01",
            "像现在这样聚在一起了，\x01",
            "我得大显身手才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAE")

    label("loc_894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_89E")
    Jump("loc_BAE")

    label("loc_89E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_9DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8FF")

    ChrTalk(
        0xFE,
        (
            "最重要的是\x01",
            "要给卧病在床的陛下\x01",
            "多多补充营养啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D9")

    label("loc_8FF")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "希尔丹夫人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "稍后我想和您谈一下\x01",
            "陛下的饮食方面的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F待会儿我会来找您谈的。\x01",
            "　\x02\x03",
            "等事情办完之后我就来，\x01",
            "所以请您再等一会儿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D9")

    Jump("loc_BAE")

    label("loc_9DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_A1C")

    ChrTalk(
        0xFE,
        "啊，客人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "料理的味道\x01",
            "你们还满意吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAE")

    label("loc_A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_BAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_AC7")

    ChrTalk(
        0xFE,
        (
            "现在料理\x01",
            "还没有准备完毕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "准备好了之后，\x01",
            "会有侍者去叫你们的，\x01",
            "请在房间稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAE")

    label("loc_AC7")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "十分抱歉，客人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在料理\x01",
            "还没有准备完毕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "准备好了之后，\x01",
            "会有侍者去叫你们的，\x01",
            "请在房间稍等片刻。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAE")

    TalkEnd(0xFE)
    Return()

    # Function_5_7BB end

    def Function_6_BB2(): pass

    label("Function_6_BB2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "你在找约修亚先生吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他好像没有\x01",
            "来过这边呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_BB2 end

    SaveToFile()

Try(main)
