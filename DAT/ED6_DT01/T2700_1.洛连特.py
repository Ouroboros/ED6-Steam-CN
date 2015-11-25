from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2700_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2700.x',
        MapIndex            = 1,
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
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetMapFlags(0x400000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_44(0x8, 0xFF)
    OP_6D(10100, 15000, 8500, 0)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_E9():
        OP_69(0xC, 0x1770)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E9)
    OP_6B(2800, 6000)
    OP_0D()
    WaitChrThread(0xC, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "那么…………\x01",
            "大人的心情现在怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#720F大人是那种话一旦说出口，\x01",
            "就固执得谁也劝不动的类型……\x02\x03",
            "无论我们如何劝说，\x01",
            "都改变不了他的主意，\x01",
            "就是想要在这里留宿啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "唔，这样啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "没办法，\x01",
            "在游击士来之前，\x01",
            "就只能先稳定他的情绪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#720F是的，真是过意不去。\x02\x03",
            "那我就先告辞了………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…………嗯。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x9, 0x578, 0x1388, 0x7D0, 0x7D0, 0x0)

    def lambda_29A():
        OP_8E(0x9, 0xFFFFEDA4, 0x1388, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_29A)
    OP_8C(0x8, 0, 400)
    SetChrPos(0x101, -3600, 5000, 0, 90)
    SetChrPos(0x102, -4600, 5000, -1000, 90)
    SetChrPos(0x105, -5600, 5000, 400, 90)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)

    def lambda_2FE():
        OP_94(0x1, 0x101, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FE)
    Sleep(200)

    def lambda_319():
        OP_94(0x1, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_319)
    Sleep(200)

    def lambda_334():
        OP_94(0x1, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_334)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    OP_8C(0x101, 315, 400)
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        (
            "#004F…………咦？\x02\x03",
            "刚才那个人……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x80)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 400)
    Sleep(400)

    ChrTalk(
        0x8,
        "哦哦，你们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "是游击士，对吧？\x02",
    )

    CloseMessageWindow()
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_44C():
        OP_69(0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_44C)

    def lambda_45A():
        OP_94(0x1, 0x8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_45A)

    def lambda_470():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_470)

    def lambda_47E():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47E)
    TurnDirection(0x105, 0x8, 400)
    WaitChrThread(0x8, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_598")

    ChrTalk(
        0x8,
        (
            "终于来了啊。\x01",
            "我是守备队队长哈恩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#508F啊，初次见面。\x01",
            "我是准游击士艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我是准游击士约修亚。\x02\x03",
            "我们从公告板上了解到\x01",
            "关所来了一个麻烦的旅行者，\x01",
            "所以来看看能帮上什么忙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D8")

    label("loc_598")


    ChrTalk(
        0x101,
        "#501F嗯，然后呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F有什么问题吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D8")

    OP_28(0x23, 0x4, 0x4)
    OP_28(0x23, 0x4, 0x2)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x8,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "实际上有一个非常麻烦的旅行者……\x01",
            "想要处理妥当十分困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果可以的话，\x01",
            "能请你们帮帮忙吗？\x02",
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
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6F4"),
        (1, "loc_78F"),
        (SWITCH_DEFAULT, "loc_8F8"),
    )


    label("loc_6F4")

    OP_28(0x23, 0x4, 0x8)

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "谢谢了，真是帮大忙了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么就先到楼下去，\x01",
            "我把详细的情况告诉你们。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/T2710   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_8F8")

    label("loc_78F")

    OP_28(0x23, 0x1, 0x4000)

    ChrTalk(
        0x101,
        (
            "#003F抱歉，\x01",
            "现在大概不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是吗，\x01",
            "不过我这边也的确很麻烦啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那我们唯有\x01",
            "先靠自己去说服他吧，\x01",
            "虽然知道自己对这种事不是很擅长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们一旦有空，\x01",
            "就请尽快过来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "唔，拜托了。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6B(3500, 0)
    OP_8C(0x8, 270, 0)
    Jump("loc_8F8")

    label("loc_8F8")

    OP_85(0x8)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
