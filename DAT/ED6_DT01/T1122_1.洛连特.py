from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T1122_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T1122.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_7B0",          # 01, 1
        "Function_2_FE9",          # 02, 2
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_4A(0xC, 255)
    OP_A2(0x5)
    OP_A2(0x4)
    OP_28(0x11, 0x4, 0x4)
    OP_28(0x11, 0x4, 0x2)
    OP_28(0x11, 0x4, 0x8)
    OP_28(0x11, 0x1, 0x1)
    OP_28(0x11, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_103")
    Fade(1000)
    SetChrPos(0x101, 6800, 0, 6600, 90)
    SetChrPos(0x102, 6600, 0, 5600, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0")
    SetChrPos(0x103, 5400, 0, 6400, 90)

    label("loc_E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100")
    SetChrPos(0x104, 5200, 0, 5400, 90)

    label("loc_100")

    Jump("loc_16A")

    label("loc_103")

    Fade(1000)
    SetChrPos(0x101, 10200, 0, 5800, 315)
    SetChrPos(0x102, 9500, 0, 4800, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A")
    SetChrPos(0x103, 10400, 0, 4200, 0)

    label("loc_14A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A")
    SetChrPos(0x104, 9500, 0, 3600, 0)

    label("loc_16A")

    OP_69(0x101, 0x0)
    TurnDirection(0xC, 0x101, 0)
    OP_0D()

    ChrTalk(
        0xC,
        "想买点什么东西吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "我店里的药都是很有效的哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是这样的，\x01",
            "我们是看了公告板而来的……\x02\x03",
            "这么说，\x01",
            "您就是思潘斯老爷爷吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "哦，你们是游击士对吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "我一直在等着你们呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F简而言之，\x01",
            "就是寻找『熊刺草』的生长地带对吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    TurnDirection(0xC, 0x102, 400)

    label("loc_328")


    ChrTalk(
        0xC,
        (
            "『熊刺草』这种药草\x01",
            "在这周边的地域\x01",
            "好像是找不到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "之前都是拜托别人\x01",
            "从洛连特帮我带过来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不久前，\x01",
            "豪尔斯教区长拜托我帮他调配一种新药。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "今后会需要\x01",
            "大量的这种药草来制药。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "所以，\x01",
            "我想事先找一些储备起来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_504")

    ChrTalk(
        0x101,
        (
            "#505F嗯～是『熊刺草』啊。\x02\x03",
            "我记得在洛连特的\x01",
            "神秘森林里有很多这种草。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_563")

    label("loc_504")


    ChrTalk(
        0x101,
        (
            "#505F嗯～是『熊刺草』啊。\x02\x03",
            "在这附近\x01",
            "确实没有见过呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_563")

    TurnDirection(0xC, 0x101, 400)

    ChrTalk(
        0xC,
        (
            "『熊刺草』这种药草\x01",
            "喜欢生长在潮湿的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我想在柏斯那些潮湿的地方\x01",
            "一定也有生长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呼～\x01",
            "又要到湿漉漉的地方去找啊……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_708")

    ChrTalk(
        0x103,
        (
            "#020F这种调查任务也是\x01",
            "游击士很重要的工作之一哦。\x02\x03",
            "把它当成一次学习的机会好好加油吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#505F唔，也只有这样了。\x02",
    )

    CloseMessageWindow()

    label("loc_708")


    ChrTalk(
        0x102,
        (
            "#010F那么，\x01",
            "我们一有消息就来通知您。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(
        0xC,
        (
            "好的，好的，拜托你们了。\x01",
            "路上小心哦。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0xC, 255)
    Return()

    # Function_0_66 end

    def Function_1_7B0(): pass

    label("Function_1_7B0")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_4A(0xC, 255)
    OP_A2(0x5)
    OP_28(0x11, 0x4, 0x10)
    OP_28(0x11, 0x4, 0x4)
    OP_28(0x11, 0x4, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_83E")
    Fade(1000)
    SetChrPos(0x101, 6800, 0, 6600, 90)
    SetChrPos(0x102, 6600, 0, 5600, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81B")
    SetChrPos(0x103, 5400, 0, 6400, 90)

    label("loc_81B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83B")
    SetChrPos(0x104, 5200, 0, 5400, 90)

    label("loc_83B")

    Jump("loc_8A5")

    label("loc_83E")

    Fade(1000)
    SetChrPos(0x101, 10200, 0, 5800, 315)
    SetChrPos(0x102, 9500, 0, 4800, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_885")
    SetChrPos(0x103, 10400, 0, 4200, 0)

    label("loc_885")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A5")
    SetChrPos(0x104, 9500, 0, 3600, 0)

    label("loc_8A5")

    OP_69(0x101, 0x0)
    TurnDirection(0xC, 0x101, 0)
    OP_0D()

    ChrTalk(
        0xC,
        "想买点什么东西吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "我店里的药都是很有效的哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是这样的，\x01",
            "我们是看了公告板而来的……\x02\x03",
            "这么说，\x01",
            "您就是思潘斯老爷爷吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "哦，你们是游击士对吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "我一直在等着你们呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F简而言之，\x01",
            "就是寻找『熊刺草』的生长地带对吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A63")
    TurnDirection(0xC, 0x102, 400)

    label("loc_A63")


    ChrTalk(
        0xC,
        (
            "『熊刺草』这种药草\x01",
            "在这周边的地域\x01",
            "好像是找不到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "之前都是拜托别人\x01",
            "从洛连特帮我带过来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不久前，\x01",
            "豪尔斯教区长拜托我帮他调配一种新药。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "今后会需要\x01",
            "大量的这种药草来制药。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE5")
    OP_28(0x11, 0x1, 0x20)
    OP_28(0x11, 0x1, 0x40)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        "#505F咦？对了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F我们最近不是\x01",
            "找到过『熊刺草』的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，是在迷雾峡谷里发现的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "是真的吗？\x02",
    )

    CloseMessageWindow()

    def lambda_C75():
        TurnDirection(0x101, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C75)
    TurnDirection(0x102, 0xC, 400)

    ChrTalk(
        0x102,
        (
            "#010F数量虽然不是很多……\x01",
            "　\x02\x03",
            "不过用来配药也应该足够了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEC")

    label("loc_CE5")

    OP_28(0x11, 0x1, 0x10)

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，\x01",
            "这样的话就没问题啦。\x02\x03",
            "『熊刺草』这种药草\x01",
            "在柏斯地区也有生长哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(
        0xC,
        "是真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F在迷雾峡谷就有。\x01",
            "我们亲眼见到了。\x02\x03",
            "数量虽然不是很多……\x01",
            "　\x02\x03",
            "不过用来配药也应该足够了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEC")

    TurnDirection(0xC, 0x102, 400)

    ChrTalk(
        0xC,
        "那真是太好了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "果然……\x01",
            "『熊刺草』喜爱潮湿的生长环境。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "迷雾峡谷\x01",
            "正是这样的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "真是太感谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "这下我就可以放心地\x01",
            "进行新药的调配了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯⊙\x02\x03",
            "那么请加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查『熊刺草』】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    OP_4B(0xC, 255)
    Return()

    # Function_1_7B0 end

    def Function_2_FE9(): pass

    label("Function_2_FE9")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_4A(0xC, 255)
    OP_A2(0x5)
    OP_28(0x11, 0x4, 0x10)
    OP_28(0x11, 0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1073")
    Fade(1000)
    SetChrPos(0x101, 6800, 0, 6600, 90)
    SetChrPos(0x102, 6600, 0, 5600, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1050")
    SetChrPos(0x103, 5400, 0, 6400, 90)

    label("loc_1050")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1070")
    SetChrPos(0x104, 5200, 0, 5400, 90)

    label("loc_1070")

    Jump("loc_10DA")

    label("loc_1073")

    Fade(1000)
    SetChrPos(0x101, 10200, 0, 5800, 315)
    SetChrPos(0x102, 9500, 0, 4800, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BA")
    SetChrPos(0x103, 10400, 0, 4200, 0)

    label("loc_10BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DA")
    SetChrPos(0x104, 9500, 0, 3600, 0)

    label("loc_10DA")

    OP_69(0x101, 0x0)
    TurnDirection(0xC, 0x101, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#508F思潘斯老爷爷，您好啊⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "哦，\x01",
            "这不是游击士协会的小姑娘吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "调查方面有什么进展吗？\x01",
            "说来给我听听。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯⊙非常顺利哦。\x02\x03",
            "在柏斯周围果然也有\x01",
            "『熊刺草』生长的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F在迷雾峡谷就有生长。\x01",
            "我们亲眼见到了。\x02\x03",
            "数量虽然不是很多……\x01",
            "　\x02\x03",
            "不过用来配药也应该足够了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126F")
    TurnDirection(0xC, 0x102, 400)

    label("loc_126F")


    ChrTalk(
        0xC,
        "那真是太好了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "果然……\x01",
            "『熊刺草』喜爱潮湿的生长环境。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "迷雾峡谷\x01",
            "正是这样的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "真是太感谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "这下我就可以放心地\x01",
            "进行新药的调配了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯⊙\x02\x03",
            "那么请加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查『熊刺草』】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    OP_4B(0xC, 255)
    Return()

    # Function_2_FE9 end

    SaveToFile()

Try(main)
