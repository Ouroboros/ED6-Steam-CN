from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4255   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4255.x',
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
        "Function_1_20F",          # 01, 1
        "Function_2_229",          # 02, 2
        "Function_3_3A6",          # 03, 3
        "Function_4_649",          # 04, 4
        "Function_5_7BF",          # 05, 5
        "Function_6_BC9",          # 06, 6
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
    Jump("loc_20E")

    label("loc_1C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1D0")
    Jump("loc_20E")

    label("loc_1D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_1E9")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_20E")

    label("loc_1E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_1FD")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_20E")

    label("loc_1FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_207")
    Jump("loc_20E")

    label("loc_207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_20E")

    label("loc_20E")

    Return()

    # Function_0_15A end

    def Function_1_20F(): pass

    label("Function_1_20F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_21F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21F")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_20F end

    def Function_2_229(): pass

    label("Function_2_229")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_390")

    label("loc_24E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_390")

    label("loc_267")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_280")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_390")

    label("loc_280")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_299")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_390")

    label("loc_299")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_390")

    label("loc_2B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_390")

    label("loc_2CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E4")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_390")

    label("loc_2E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_390")

    label("loc_2FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_390")

    label("loc_316")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_390")

    label("loc_32F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_348")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_390")

    label("loc_348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_361")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_390")

    label("loc_361")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_390")

    label("loc_37A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_390")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_390")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_390")

    label("loc_3A5")

    Return()

    # Function_2_229 end

    def Function_3_3A6(): pass

    label("Function_3_3A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_3B3")
    Jump("loc_645")

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_408")

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
    Jump("loc_4BE")

    label("loc_408")

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

    label("loc_4BE")

    Jump("loc_645")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_4CB")
    Jump("loc_645")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_4D5")
    Jump("loc_645")

    label("loc_4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_584")

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
    Jump("loc_645")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_645")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5C0")

    ChrTalk(
        0xFE,
        (
            "这些可恶的老鼠，\x01",
            "到底是从哪里钻进来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_645")

    label("loc_5C0")

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

    label("loc_645")

    TalkEnd(0xFE)
    Return()

    # Function_3_3A6 end

    def Function_4_649(): pass

    label("Function_4_649")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_656")
    Jump("loc_7BB")

    label("loc_656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6D7")

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
    Jump("loc_7BB")

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_6E1")
    Jump("loc_7BB")

    label("loc_6E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_6EB")
    Jump("loc_7BB")

    label("loc_6EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_731")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "早点收拾好就可以回家了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB")

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_7BB")

    ChrTalk(
        0xFE,
        (
            "厨师长不仅精于宫廷料理，\x01",
            "而且据说他可以烹制出\x01",
            "上千种各式风味的料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BB")

    TalkEnd(0xFE)
    Return()

    # Function_4_649 end

    def Function_5_7BF(): pass

    label("Function_5_7BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_836")

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
    Jump("loc_BC5")

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_898")

    ChrTalk(
        0xFE,
        (
            "陛下和公主好久没有\x01",
            "像现在这样聚在一起了，\x01",
            "我得大显身手才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC5")

    label("loc_898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_8A2")
    Jump("loc_BC5")

    label("loc_8A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_9F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_903")

    ChrTalk(
        0xFE,
        (
            "最重要的是\x01",
            "要给卧病在床的陛下\x01",
            "多多补充营养啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9ED")

    label("loc_903")

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

    NpcTalk(
        0x0,
        "希尔丹夫人",
        (
            "#710F待会儿我会来找您谈的。\x01",
            "　\x02\x03",
            "等事情办完之后我就来，\x01",
            "所以请您再等一会儿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9ED")

    Jump("loc_BC5")

    label("loc_9F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_A30")

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
    Jump("loc_BC5")

    label("loc_A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B30")

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
    Jump("loc_BC5")

    label("loc_B30")


    ChrTalk(
        0xFE,
        (
            "料理的准备工作\x01",
            "马上就要做完了……\x02",
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

    label("loc_BC5")

    TalkEnd(0xFE)
    Return()

    # Function_5_7BF end

    def Function_6_BC9(): pass

    label("Function_6_BC9")

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

    # Function_6_BC9 end

    SaveToFile()

Try(main)
