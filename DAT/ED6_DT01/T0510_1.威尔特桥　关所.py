from ED6ScenarioHelper import *

def main():
    # 威尔特桥　关所

    CreateScenaFile(
        FileName            = 'T0510_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0510.x',
        MapIndex            = 18,
        MapDefaultBGM       = "ed60016",
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
        "Function_1_9E9",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_426")
    OP_A2(0x281)

    ChrTalk(
        0x8,
        (
            "哦哦，\x01",
            "这不是艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 0)

    ChrTalk(
        0x101,
        "#000F阿斯顿队长，你好。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 0)

    ChrTalk(
        0x102,
        "#010F很久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊啊，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我都听说了，\x01",
            "我家的鲁克给你们添了不少麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "作为父亲，真是感到惭愧啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F没事，像他这种年纪的男孩子\x01",
            "喜欢恶作剧也是没有办法的事。\x02\x03",
            "#001F就算是我，\x01",
            "小的时候也经常到城镇外面乱跑呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#017F你不是女孩子吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哈哈，还是这么精神啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你这种精神劲头\x01",
            "要是也能分一部分\x01",
            "给这里的新兵就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我想通过模拟战斗来锻炼那些新兵，\x01",
            "并端正他们的态度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "于是我就通过\x01",
            "游击士协会募集\x01",
            "愿意扮演敌兵角色的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果能由你们来扮演就再合适不过了，\x01",
            "怎么样？可以吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8, 0x4, 0x4)
    OP_28(0x8, 0x1, 0x1)
    OP_28(0x8, 0x4, 0x2)
    TurnDirection(0x102, 0x8, 400)
    Jump("loc_66B")

    label("loc_426")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F5")

    ChrTalk(
        0x8,
        "哦，是艾丝蒂尔和约修亚啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们是因为看到了\x01",
            "协会的公告板而赶来的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "实际上是这样的，\x01",
            "我想通过模拟战斗来锻炼那些新兵，\x01",
            "并端正他们的态度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "于是我就通过\x01",
            "游击士协会募集\x01",
            "愿意扮演敌兵角色的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果能由你们来扮演就再合适不过了，\x01",
            "怎么样？可以吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8, 0x4, 0x4)
    OP_28(0x8, 0x1, 0x1)
    OP_28(0x8, 0x4, 0x2)
    Jump("loc_66B")

    label("loc_5F5")


    ChrTalk(
        0x8,
        "事情办完了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "可以来扮演\x01",
            "模拟战斗的敌兵角色了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DE")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_6D0"),
        (0, "loc_7F9"),
        (SWITCH_DEFAULT, "loc_6D0"),
    )


    label("loc_6D0")

    OP_28(0x8, 0x1, 0x8000)

    ChrTalk(
        0x101,
        (
            "#505F对不起啊，阿斯顿队长。\x01",
            "我们还有事情要办……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这样啊，真是遗憾啊，\x01",
            "不过我是不会勉强你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果愿意帮忙的话，\x01",
            "就请尽快到这里来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_9DB")

    label("loc_7F9")

    OP_28(0x8, 0x4, 0x8)

    ChrTalk(
        0x101,
        "#006F嗯，可以。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们接受。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "谢谢，真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在训练的准备完成之前\x01",
            "你们就先休息一会儿吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果不保持最好的状态去训练，\x01",
            "就没有什么效果了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#001F好的～～\x01",
            "那我就先小睡一觉啦～～⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我们就去准备了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嗯，有劳你们了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    NewScene("ED6_DT01/T0500   ._SN", 1, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_9DB")

    label("loc_9DB")

    Jump("loc_66B")

    label("loc_9DE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_66 end

    def Function_1_9E9(): pass

    label("Function_1_9E9")

    TalkBegin(0x8)
    EventBegin(0x0)
    OP_6D(28890, 0, -73240, 0)
    OP_8C(0x8, 270, 0)
    SetChrPos(0x101, 27710, 0, -72870, 90)
    SetChrPos(0x102, 27790, 0, -73700, 90)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    Sleep(2000)

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚，\x01",
            "今天真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "通过你们的协助，\x01",
            "士兵们或多或少明白了一些道理。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 0)

    ChrTalk(
        0x101,
        (
            "#000F您太客气了，\x01",
            "说谢谢的应该是我们才对。\x02\x03",
            "这是一次很好的锻炼呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 0)

    ChrTalk(
        0x102,
        "#010F是啊，我们也学到了很多。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呵呵，你们能够有这种想法，\x01",
            "今后肯定会成为杰出的游击士的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "能站在对方的角度去思考，\x01",
            "就可以非常的客观公正了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "希望你们能够在今后的舞台中大展身手。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯。\x01",
            "谢谢你，阿斯顿队长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F阿斯顿队长也要好好保重。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯。\x01",
            "那么，再会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【训练士兵】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1)
    OP_28(0x8, 0x4, 0x10)
    OP_28(0x8, 0x1, 0x8)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    TalkEnd(0x8)
    Return()

    # Function_1_9E9 end

    SaveToFile()

Try(main)
