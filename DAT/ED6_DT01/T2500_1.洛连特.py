from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2500_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2500.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        "Function_1_3C6",          # 01, 1
        "Function_2_D64",          # 02, 2
        "Function_3_179C",         # 03, 3
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    Fade(1000)
    OP_6C(135000, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        "呼，难办啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样下去校园的装饰\x01",
            "就完成不了了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要找人帮忙，\x01",
            "但是学生们现在都很忙啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 135, 400)

    ChrTalk(
        0xFE,
        (
            "你们看吧，\x01",
            "还有一些没能装饰到的地方。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17E():
        OP_6D(49960, 1500, 53870, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17E)
    Sleep(100)
    OP_8B(0x101, 0xC328, 0xD26E, 0x190)
    Sleep(150)
    OP_8B(0x105, 0xC328, 0xD26E, 0x190)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CF")
    OP_8B(0x13B, 0xC328, 0xD26E, 0x190)

    label("loc_1CF")

    WaitChrThread(0xFE, 0x1)

    ChrTalk(
        0x101,
        (
            "#004F哎呀……\x01",
            "正中间没有垂幕啊。\x02\x03",
            "#003F唔～\x01",
            "的确有些不好看。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "对吧？\x02",
    )

    CloseMessageWindow()

    def lambda_248():
        OP_69(0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_248)
    Sleep(100)
    TurnDirection(0x101, 0xFE, 400)
    Sleep(100)
    TurnDirection(0x105, 0xFE, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27D")
    TurnDirection(0x13B, 0xFE, 400)

    label("loc_27D")

    WaitChrThread(0xFE, 0x1)

    ChrTalk(
        0xFE,
        (
            "如果看到没有装饰的地方，\x01",
            "还请告诉我一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我会很快过去，\x01",
            "把它给弄好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要稍微注意一下\x01",
            "应该就可以发现的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这么说，\x01",
            "只要找到像这样\x01",
            "还没装饰的地方就可以了吧。\x02\x03",
            "嗯，明白了。\x01",
            "如果看到了就回来告诉您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，那就拜托了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x27, 0x1, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    EventEnd(0x1)
    Return()

    # Function_0_66 end

    def Function_1_3C6(): pass

    label("Function_1_3C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D60")
    EventBegin(0x0)
    Fade(1000)
    OP_6C(225000, 0)
    SetChrPos(0x101, 21320, 250, 26540, 180)
    SetChrPos(0x105, 21880, 0, 27550, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_423")
    SetChrPos(0x13B, 20790, 0, 27100, 180)

    label("loc_423")

    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F哎……？\x02\x03",
            "这里没有彩旗吗……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47E")
    TurnDirection(0x101, 0x13B, 400)
    Jump("loc_485")

    label("loc_47E")

    TurnDirection(0x101, 0x105, 400)

    label("loc_485")


    ChrTalk(
        0x101,
        (
            "#002F你看，其他建筑物的门口\x01",
            "不都有挂上彩旗的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_556")

    ChrTalk(
        0x13B,
        (
            "#643F啊，\x01",
            "这样说的话好像真的是这样。\x02\x03",
            "这个地方应该是还没有装饰好。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F我们去告诉\x01",
            "勤务员巴克斯师傅吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    Jump("loc_5D4")

    label("loc_556")


    ChrTalk(
        0x105,
        (
            "#044F啊，真的呢。\x01",
            "好像还没有装饰到呢。\x02\x03",
            "#040F我们去告诉\x01",
            "勤务员巴克斯师傅吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D4")


    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x15, 30130, 0, 28910, 270)
    SetChrPos(0x101, 22450, 0, 27570, 180)
    SetChrPos(0x105, 21590, 0, 28160, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_641")
    SetChrPos(0x13B, 20300, 0, 27960, 90)

    label("loc_641")

    OP_8C(0x101, 90, 0)
    OP_8C(0x105, 90, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_664")
    OP_8C(0x13B, 90, 0)

    label("loc_664")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0x5F3C, 0x0, 0x6CC0, 0xBB8, 0x0)
    OP_8E(0x15, 0x5BEA, 0x0, 0x6A5E, 0xBB8, 0x0)
    OP_4A(0x15, 255)
    Sleep(400)
    OP_8C(0x15, 225, 400)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x15,
        (
            "啊，果然。\x01",
            "很会观察嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(
        0x15,
        (
            "好，\x01",
            "我这就开始装饰。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_768")
    TurnDirection(0x13B, 0x101, 400)

    ChrTalk(
        0x13B,
        "#644F我们也来帮忙吧。\x02",
    )

    CloseMessageWindow()

    def lambda_756():
        TurnDirection(0x105, 0x13B, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_756)
    TurnDirection(0x101, 0x13B, 400)
    Jump("loc_795")

    label("loc_768")


    ChrTalk(
        0x105,
        (
            "#040F我们也来帮忙吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    label("loc_795")


    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "啊，谢谢了。\x02",
    )

    CloseMessageWindow()

    def lambda_7CA():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7CA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7EE")

    def lambda_7E6():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_7E6)

    label("loc_7EE")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(
        0x15,
        (
            "那么就\x01",
            "有劳你们了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_81A():
        OP_8E(0x101, 0x57B2, 0x0, 0x6658, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81A)

    def lambda_835():
        OP_8E(0x105, 0x5456, 0x0, 0x6720, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_835)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_873")

    def lambda_85E():
        OP_8E(0x13B, 0x5154, 0xFA, 0x65A4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_85E)

    label("loc_873")


    def lambda_879():
        OP_8E(0x15, 0x5AB4, 0xFA, 0x65B8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_879)

    def lambda_894():
        OP_6C(135000, 2500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_894)
    OP_6D(22030, 3500, 24930, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D7")
    WaitChrThread(0x13B, 0x1)

    label("loc_8D7")

    WaitChrThread(0x15, 0x1)
    Sleep(400)
    OP_72(0x1E, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Sleep(400)
    OP_28(0x27, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C08")

    ChrTalk(
        0x15,
        (
            "……好。\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(
        0x15,
        (
            "呼……\x01",
            "总算是全部解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "哎呀～\x01",
            "让你们费心了啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A8():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9CC")

    def lambda_9C4():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_9C4)

    label("loc_9CC")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(
        0x101,
        (
            "#000F没什么，不用介意。\x02\x03",
            "好不容易才有一次学园祭，\x01",
            "不好好准备一下怎么能行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯，是啊。\x02\x03",
            "既然是我们大家的节日，\x01",
            "帮帮忙那是应该的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9C")
    TurnDirection(0x13B, 0x105, 400)

    ChrTalk(
        0x13B,
        (
            "#644F不愧是科洛丝。\x01",
            "真是说出了我们的心声啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9C")


    ChrTalk(
        0x15,
        (
            "哈哈～\x01",
            "的确如此啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x15, 400)

    ChrTalk(
        0x15,
        (
            "我们也很期待\x01",
            "明天的学园祭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯！交给我们吧！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B41")

    ChrTalk(
        0x13B,
        (
            "#649F呵呵，\x01",
            "那就请拭目以待了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5E")

    label("loc_B41")


    ChrTalk(
        0x105,
        "#040F我们会竭尽全力的。\x02",
    )

    CloseMessageWindow()

    label("loc_B5E")


    ChrTalk(
        0x15,
        (
            "那么，\x01",
            "你们要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x27, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x200)
    OP_2C(0x3D, 0x1F4)
    OP_2B(0x3D, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "学园祭的校园任务\x01",
            "【装饰校园】\x07\x00",
            "完成！\x02",
        )
    )

    OP_83(0x2, 0x2)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_CBD")

    label("loc_C08")


    ChrTalk(
        0x15,
        (
            "……好。\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(
        0x15,
        (
            "那，如果再看到的话，\x01",
            "也麻烦告诉我。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C68():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C68)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C8C")

    def lambda_C84():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_C84)

    label("loc_C8C")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(
        0x101,
        "#006F嗯，放心吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_CBD")


    def lambda_CC3():

        label("loc_CC3")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_CC3")

    QueueWorkItem2(0x0, 1, lambda_CC3)

    def lambda_CD4():

        label("loc_CD4")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_CD4")

    QueueWorkItem2(0x1, 1, lambda_CD4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFE")

    def lambda_CF3():

        label("loc_CF3")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_CF3")

    QueueWorkItem2(0x2, 1, lambda_CF3)

    label("loc_CFE")

    OP_8E(0x15, 0x6086, 0x0, 0x6E6E, 0xBB8, 0x0)
    OP_8E(0x15, 0x7A30, 0x0, 0x6D60, 0xBB8, 0x0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D40")
    OP_44(0x2, 0xFF)

    label("loc_D40")

    SetChrPos(0x15, 47880, 0, 56070, 135)
    ClearChrFlags(0x15, 0x40)
    OP_4B(0x15, 255)
    OP_64(0x3, 0x1)
    EventEnd(0x0)

    label("loc_D60")

    TalkEnd(0xFF)
    Return()

    # Function_1_3C6 end

    def Function_2_D64(): pass

    label("Function_2_D64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1798")
    EventBegin(0x0)
    Fade(1000)
    OP_6C(45000, 0)
    SetChrPos(0x101, 38970, 0, 68950, 90)
    SetChrPos(0x105, 40770, 0, 68550, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC1")
    SetChrPos(0x13B, 38560, 0, 70140, 90)

    label("loc_DC1")

    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x105,
        "#044F咦……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E07")

    def lambda_DFF():
        TurnDirection(0x13B, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_DFF)

    label("loc_E07")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#000F怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#044F这里……\x01",
            "按理说这也应该是挂垂幕的地方啊。\x01",
            "　\x02\x03",
            "门的另外一边是挂好了的……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 0, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB2")

    def lambda_EAA():
        OP_8C(0x13B, 0, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_EAA)

    label("loc_EB2")

    OP_8C(0x101, 0, 400)
    OP_6D(41580, 2000, 73990, 1500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F07")

    ChrTalk(
        0x13B,
        "#643F啊，没错……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F1B")

    label("loc_F07")


    ChrTalk(
        0x101,
        "#004F啊，真的呢。\x02",
    )

    CloseMessageWindow()

    label("loc_F1B")

    OP_69(0x105, 0x5DC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F43")
    Sleep(100)

    def lambda_F3B():
        TurnDirection(0x13B, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_F3B)

    label("loc_F43")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#000F那好，\x01",
            "我们去告诉巴克斯师傅吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#040F嗯，好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x15, 45200, 0, 65300, 270)
    SetChrPos(0x101, 39140, 0, 69780, 135)
    SetChrPos(0x105, 38830, 0, 68410, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF5")
    Sleep(100)
    SetChrPos(0x13B, 37730, 0, 69120, 135)

    label("loc_FF5")

    OP_69(0x101, 0x0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_1011():

        label("loc_1011")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1011")

    QueueWorkItem2(0x0, 1, lambda_1011)

    def lambda_1022():

        label("loc_1022")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1022")

    QueueWorkItem2(0x1, 1, lambda_1022)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104C")

    def lambda_1041():

        label("loc_1041")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1041")

    QueueWorkItem2(0x2, 1, lambda_1041)

    label("loc_104C")

    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0x9FE2, 0x0, 0x1046E, 0xBB8, 0x0)
    OP_8E(0x15, 0x9F42, 0x0, 0x10BC6, 0xBB8, 0x0)
    OP_4A(0x15, 255)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1097")
    OP_44(0x2, 0xFF)

    label("loc_1097")

    Sleep(400)
    OP_8C(0x15, 45, 400)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x15,
        (
            "啊，\x01",
            "这里很明显呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(
        0x15,
        (
            "那么我这就\x01",
            "开始装饰吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1132")

    ChrTalk(
        0x13B,
        "#644F好，我们也来帮忙。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x13B, 400)
    Jump("loc_1160")

    label("loc_1132")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(
        0x101,
        "#000F我们也来帮忙吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    label("loc_1160")


    ChrTalk(
        0x15,
        "哦，有劳了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "那就拜托了。\x02",
    )

    CloseMessageWindow()

    def lambda_118B():
        OP_6C(135000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_118B)

    def lambda_119B():
        OP_8E(0x101, 0xA028, 0x0, 0x111FC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_119B)

    def lambda_11B6():
        OP_8E(0x105, 0x9F42, 0x0, 0x10BC6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11B6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F4")

    def lambda_11DF():
        OP_8E(0x13B, 0x9CC2, 0x0, 0x10F04, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_11DF)

    label("loc_11F4")


    def lambda_11FA():
        OP_6D(41770, 3500, 69260, 4000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_11FA)
    OP_8E(0x15, 0x9FE2, 0x0, 0x107AC, 0x7D0, 0x0)
    OP_8E(0x15, 0x9506, 0x0, 0x109A0, 0x7D0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_8E(0x15, 0x959C, 0x0, 0x11A9E, 0xBB8, 0x0)
    OP_72(0x5, 0x2)
    OP_6F(0x5, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_127C")
    WaitChrThread(0x13B, 0x1)

    label("loc_127C")

    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x15, 0x2)
    OP_72(0x12, 0x4)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x15, 43990, 0, 73850, 270)
    OP_6F(0x5, 60)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C7")
    SetChrPos(0x13B, 41160, 0, 69290, 90)

    label("loc_12C7")

    FadeToBright(1000, 0)
    OP_8E(0x15, 0xA258, 0x1F4, 0x121EC, 0xBB8, 0x0)
    OP_72(0x5, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)
    OP_8E(0x15, 0x959C, 0x0, 0x11A9E, 0xBB8, 0x0)
    OP_8E(0x15, 0x9470, 0x0, 0x10BC6, 0xBB8, 0x0)
    OP_8C(0x15, 90, 400)
    OP_71(0x5, 0x800)
    Sleep(400)
    OP_28(0x27, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_163B")

    ChrTalk(
        0x15,
        (
            "……好。\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    def lambda_1381():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1381)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A5")

    def lambda_139D():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_139D)

    label("loc_13A5")

    TurnDirection(0x101, 0x15, 400)
    OP_69(0x101, 0x5DC)

    ChrTalk(
        0x15,
        (
            "呼……\x01",
            "总算是全部解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "哎呀～\x01",
            "让你们费心了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没什么，不用介意。\x02\x03",
            "好不容易才有一次学园祭，\x01",
            "不好好准备一下怎么能行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯，是啊。\x02\x03",
            "既然是我们大家的节日，\x01",
            "帮帮忙那是应该的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14CF")
    TurnDirection(0x13B, 0x105, 400)

    ChrTalk(
        0x13B,
        (
            "#644F不愧是科洛丝。\x01",
            "真是说出了我们的心声啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14CF")


    ChrTalk(
        0x15,
        (
            "哈哈～\x01",
            "的确如此啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x15, 400)

    ChrTalk(
        0x15,
        (
            "我们也很期待\x01",
            "明天的学园祭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯！交给我们吧！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1574")

    ChrTalk(
        0x13B,
        (
            "#649F呵呵，\x01",
            "那就请拭目以待了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1591")

    label("loc_1574")


    ChrTalk(
        0x105,
        "#040F我们会竭尽全力的。\x02",
    )

    CloseMessageWindow()

    label("loc_1591")


    ChrTalk(
        0x15,
        (
            "那么，\x01",
            "你们要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x27, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x200)
    OP_2C(0x3D, 0x1F4)
    OP_2B(0x3D, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "学园祭的校园任务\x01",
            "【装饰校园】\x07\x00",
            "完成！\x02",
        )
    )

    OP_83(0x2, 0x2)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_16F0")

    label("loc_163B")


    ChrTalk(
        0x15,
        (
            "……好。\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1667():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1667)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_168B")

    def lambda_1683():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1683)

    label("loc_168B")

    TurnDirection(0x101, 0x15, 400)
    OP_69(0x101, 0x5DC)
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(
        0x15,
        (
            "那，如果再看到的话，\x01",
            "也麻烦告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，放心吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_16F0")


    def lambda_16F6():

        label("loc_16F6")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_16F6")

    QueueWorkItem2(0x0, 1, lambda_16F6)

    def lambda_1707():

        label("loc_1707")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1707")

    QueueWorkItem2(0x1, 1, lambda_1707)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1731")

    def lambda_1726():

        label("loc_1726")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1726")

    QueueWorkItem2(0x2, 1, lambda_1726)

    label("loc_1731")

    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0x9B6E, 0x0, 0xFF32, 0xBB8, 0x0)
    OP_8E(0x15, 0xB4C8, 0x0, 0xFF3C, 0xBB8, 0x0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1778")
    OP_44(0x2, 0xFF)

    label("loc_1778")

    SetChrPos(0x15, 47880, 0, 56070, 135)
    ClearChrFlags(0x15, 0x40)
    OP_4B(0x15, 255)
    OP_64(0x4, 0x1)
    EventEnd(0x0)

    label("loc_1798")

    TalkEnd(0xFF)
    Return()

    # Function_2_D64 end

    def Function_3_179C(): pass

    label("Function_3_179C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B9")
    OP_28(0x27, 0x1, 0x8)
    EventBegin(0x0)
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x101, 53860, 0, 28500, 90)
    SetChrPos(0x105, 53290, 0, 29520, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17FF")
    SetChrPos(0x13B, 52540, 0, 30290, 90)

    label("loc_17FF")

    OP_69(0x101, 0x0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F哎……？\x02\x03",
            "啊，难道……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    OP_94(0x1, 0x101, 0xB4, 0x3E8, 0x7D0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1871")

    def lambda_1864():
        TurnDirection(0x13B, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1864)
    Sleep(150)

    label("loc_1871")

    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#040F怎么了呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F这里没有彩旗。\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_18C1():

        label("loc_18C1")

        TurnDirection(0x105, 0x101, 0)
        OP_48()
        Jump("loc_18C1")

    QueueWorkItem2(0x105, 1, lambda_18C1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18EB")

    def lambda_18E0():

        label("loc_18E0")

        TurnDirection(0x13B, 0x101, 0)
        OP_48()
        Jump("loc_18E0")

    QueueWorkItem2(0x13B, 1, lambda_18E0)

    label("loc_18EB")

    OP_8E(0x101, 0xC80A, 0x0, 0x6C3E, 0x1770, 0x0)
    Sleep(100)
    Fade(1000)
    OP_6C(135000, 0)
    OP_6D(51210, 0, 27710, 0)
    Sleep(100)
    OP_8C(0x101, 90, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#000F你看，反面却是有的。\x02",
    )

    CloseMessageWindow()
    OP_44(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1992")
    OP_44(0x13B, 0x1)

    def lambda_197D():
        OP_8E(0x13B, 0xCD96, 0x0, 0x73A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_197D)

    label("loc_1992")

    OP_8E(0x105, 0xCCCE, 0x0, 0x6C66, 0xBB8, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C2")

    def lambda_19BA():
        OP_8C(0x13B, 315, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_19BA)

    label("loc_19C2")

    OP_8C(0x105, 315, 400)
    Sleep(200)
    OP_8C(0x105, 180, 400)
    Sleep(200)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x105, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A52")

    ChrTalk(
        0x105,
        "#044F啊，真的呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x101, 400)

    ChrTalk(
        0x13B,
        (
            "#643F不愧是游击士，\x01",
            "观察得这么仔细。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13B, 400)
    Jump("loc_1A8E")

    label("loc_1A52")


    ChrTalk(
        0x105,
        (
            "#044F啊，真的呢。\x02\x03",
            "艾丝蒂尔，\x01",
            "你很会观察啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    label("loc_1A8E")


    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，还好啦。\x02\x03",
            "那好，\x01",
            "我们去告诉巴克斯师傅吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#041F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x15, 49850, 0, 28600, 90)
    SetChrPos(0x101, 55720, 0, 29180, 270)
    SetChrPos(0x105, 55170, 0, 30090, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B4F")
    SetChrPos(0x13B, 56220, 0, 30860, 270)

    label("loc_1B4F")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_6C(270000, 0)
    OP_6D(54350, 0, 28820, 0)
    OP_0D()

    def lambda_1B7E():

        label("loc_1B7E")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1B7E")

    QueueWorkItem2(0x0, 1, lambda_1B7E)

    def lambda_1B8F():

        label("loc_1B8F")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1B8F")

    QueueWorkItem2(0x1, 1, lambda_1B8F)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB9")

    def lambda_1BAE():

        label("loc_1BAE")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1BAE")

    QueueWorkItem2(0x2, 1, lambda_1BAE)

    label("loc_1BB9")

    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0xD598, 0x0, 0x6F04, 0xBB8, 0x0)
    OP_4A(0x15, 255)
    Sleep(400)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BF5")
    OP_44(0x2, 0xFF)

    label("loc_1BF5")

    OP_8C(0x15, 270, 400)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x15,
        (
            "哦，\x01",
            "这样的细节也能发现啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(
        0x15,
        (
            "真是很不起眼的地方呢。\x01",
            "我这就开始装饰吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC7")

    ChrTalk(
        0x13B,
        "#644F那我们也来帮忙吧。\x02",
    )

    CloseMessageWindow()

    def lambda_1C96():
        TurnDirection(0x105, 0x13B, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C96)
    TurnDirection(0x101, 0x13B, 400)

    ChrTalk(
        0x105,
        "#040F嗯，当然。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x13B, 400)
    Jump("loc_1D14")

    label("loc_1CC7")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#000F好的，我们也来帮忙吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#040F嗯，好的。\x02",
    )

    CloseMessageWindow()

    label("loc_1D14")


    ChrTalk(
        0x15,
        "抱歉，又麻烦你们了。\x02",
    )

    CloseMessageWindow()

    def lambda_1D30():
        OP_8E(0x15, 0xD764, 0x0, 0x6054, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1D30)

    def lambda_1D4B():
        OP_8E(0x101, 0xDAFC, 0x0, 0x7CD8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D4B)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA7")

    def lambda_1D74():
        OP_8E(0x13B, 0xD7AA, 0x0, 0x7D77, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1D74)

    def lambda_1D8F():
        OP_8E(0x105, 0xDAD4, 0x0, 0x646E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D8F)
    Jump("loc_1DC2")

    label("loc_1DA7")


    def lambda_1DAD():
        OP_8E(0x105, 0xD7AA, 0x0, 0x7D77, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1DAD)

    label("loc_1DC2")

    OP_6D(54350, 1500, 28820, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x15, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DFC")
    OP_44(0x13B, 0x1)

    label("loc_1DFC")

    OP_72(0x1A, 0x4)
    SetChrPos(0x101, 55720, 0, 29180, 270)
    SetChrPos(0x105, 55170, 0, 30090, 270)
    SetChrPos(0x15, 56700, 0, 27700, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E53")
    SetChrPos(0x13B, 57090, 0, 30560, 270)

    label("loc_1E53")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_28(0x27, 0x1, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2170")

    ChrTalk(
        0x15,
        (
            "……好。\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    def lambda_1EB6():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1EB6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EDA")

    def lambda_1ED2():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1ED2)

    label("loc_1EDA")

    TurnDirection(0x101, 0x15, 400)
    OP_69(0x101, 0x5DC)

    ChrTalk(
        0x15,
        (
            "呼……\x01",
            "总算是全部解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "哎呀～\x01",
            "让你们费心了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没什么，不用介意。\x02\x03",
            "好不容易才有一次学园祭，\x01",
            "不好好准备一下怎么能行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯，是啊。\x02\x03",
            "既然是我们大家的节日，\x01",
            "帮帮忙那是应该的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2004")
    TurnDirection(0x13B, 0x105, 400)

    ChrTalk(
        0x13B,
        (
            "#644F不愧是科洛丝。\x01",
            "真是说出了我们的心声啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2004")


    ChrTalk(
        0x15,
        (
            "哈哈～\x01",
            "的确如此啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x15, 400)

    ChrTalk(
        0x15,
        (
            "我们也很期待\x01",
            "明天的学园祭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯！交给我们吧！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20A9")

    ChrTalk(
        0x13B,
        (
            "#649F呵呵，\x01",
            "那就请拭目以待了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C6")

    label("loc_20A9")


    ChrTalk(
        0x105,
        "#040F我们会竭尽全力的。\x02",
    )

    CloseMessageWindow()

    label("loc_20C6")


    ChrTalk(
        0x15,
        (
            "那么，\x01",
            "你们要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x27, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x200)
    OP_2C(0x3D, 0x1F4)
    OP_2B(0x3D, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "学园祭的校园任务\x01",
            "【装饰校园】\x07\x00",
            "完成！\x02",
        )
    )

    OP_83(0x2, 0x2)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_2225")

    label("loc_2170")


    ChrTalk(
        0x15,
        (
            "……好。\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)
    TurnDirection(0x15, 0x101, 400)

    def lambda_21AA():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_21AA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21CE")

    def lambda_21C6():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_21C6)

    label("loc_21CE")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(
        0x15,
        (
            "那，如果再看到的话，\x01",
            "也麻烦告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，放心吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_2225")


    def lambda_222B():

        label("loc_222B")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_222B")

    QueueWorkItem2(0x0, 1, lambda_222B)

    def lambda_223C():

        label("loc_223C")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_223C")

    QueueWorkItem2(0x1, 1, lambda_223C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2266")

    def lambda_225B():

        label("loc_225B")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_225B")

    QueueWorkItem2(0x2, 1, lambda_225B)

    label("loc_2266")

    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0xB0C2, 0x0, 0x6DCE, 0xBB8, 0x0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2299")
    OP_44(0x2, 0xFF)

    label("loc_2299")

    SetChrPos(0x15, 47880, 0, 56070, 135)
    ClearChrFlags(0x15, 0x40)
    OP_4B(0x15, 255)
    OP_64(0x5, 0x1)
    EventEnd(0x0)

    label("loc_22B9")

    TalkEnd(0xFF)
    Return()

    # Function_3_179C end

    SaveToFile()

Try(main)
