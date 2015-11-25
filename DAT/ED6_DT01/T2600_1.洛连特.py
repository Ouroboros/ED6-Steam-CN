from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2600_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        "Function_1_B0F",          # 01, 1
        "Function_2_B34",          # 02, 2
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2000)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_83")
    Return()

    label("loc_83")

    EventBegin(0x0)
    Fade(1000)
    OP_6C(45000, 0)
    OP_6D(200, 0, 3500, 0)
    SetChrPos(0x101, 200, 0, 3500, 0)
    SetChrPos(0x105, -600, 0, 2500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5")
    SetChrPos(0x13B, 1000, 0, 1500, 0)

    label("loc_E5")

    OP_0D()
    WaitChrThread(0x9, 0x1)

    def lambda_F1():
        OP_6D(-180, 1000, 7200, 1500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_160")
    Sleep(150)
    OP_62(0x13B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_160")

    WaitChrThread(0x9, 0x1)
    SetChrPos(0x9, 20, 1000, 12000, 180)
    ClearChrFlags(0x9, 0x80)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x2D)
    OP_73(0x0)

    def lambda_192():
        OP_8F(0x9, 0x50, 0x3E8, 0x2A30, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_192)
    OP_8C(0x9, 0, 800)
    OP_72(0x0, 0x800)
    OP_22(0xD3, 0x0, 0x64)
    OP_6F(0x0, 45)
    OP_70(0x0, 0x0)
    WaitChrThread(0x9, 0x2)
    OP_94(0x1, 0x9, 0xB4, 0x578, 0x1770, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_43(0x9, 0x1, 0x1, 0x1)
    OP_97(0x9, 0xFFFFFD12, 0x2508, 0x2BF20, 0x1388, 0x1)
    OP_8C(0x9, 45, 400)
    OP_44(0x9, 0x1)
    Sleep(400)

    ChrTalk(
        0x9,
        "哈～呼～哈～呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "可恶……\x01",
            "到底是怎么回事……\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#002F……怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F是啊，怎么了呢……？\x02\x03",
            "好像不太寻常的样子……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_6A(0x101)

    def lambda_2E1():
        OP_91(0x101, 0x0, 0x0, 0xA8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E1)
    Sleep(150)

    def lambda_301():
        OP_91(0x105, 0x0, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_301)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33B")
    OP_91(0x13B, 0x0, 0x0, 0xA28, 0x7D0, 0x0)
    Jump("loc_340")

    label("loc_33B")

    WaitChrThread(0x105, 0x1)

    label("loc_340")

    TurnDirection(0x101, 0x9, 400)
    ClearMapFlags(0x1)

    ChrTalk(
        0x101,
        "#002F请问发生什么事了？\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x9, 0x101, 400)
    Sleep(400)

    ChrTalk(
        0x9,
        (
            "喂、喂，\x01",
            "你们最好别站在门口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "说不定什么时候\x01",
            "怪物就会跳出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F怪、怪物？\x02\x03",
            "这座建筑物里面有魔兽吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "啊，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "体型相当巨大，\x01",
            "而且有很多只聚集在一起。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#042F这座古老的建筑物\x01",
            "是学院以前的校舍。\x02\x03",
            "不过一般情况下，\x01",
            "入口应该是用钥匙锁住了的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x105, 400)

    ChrTalk(
        0x9,
        (
            "是我从艾福托老师那里\x01",
            "把钥匙借来的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55C")

    def lambda_54F():
        TurnDirection(0x13B, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_54F)
    Sleep(100)

    label("loc_55C")

    TurnDirection(0x105, 0x9, 400)

    ChrTalk(
        0x9,
        (
            "校舍里因为准备学园祭太吵了，\x01",
            "所以我想到安静的地方休息。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72E")

    ChrTalk(
        0x101,
        "#004F到安静的地方休息……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13B,
        (
            "#647F这是有意在逃避工作啊。\x01",
            "也就是说你是在偷懒了。\x02\x03",
            "#659F哼哼～米克。\x01",
            "你还真是有胆量啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x13B, 400)

    ChrTalk(
        0x9,
        (
            "哼，\x01",
            "我本来就不想参加啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "为什么非要\x01",
            "让我出演那样的舞台剧啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我都烦死了，\x01",
            "不想再参与了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A4")

    label("loc_72E")


    ChrTalk(
        0x101,
        (
            "#004F到安静的地方休息……\x02\x03",
            "这么说来，\x01",
            "你不就是来这里偷懒的吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "准备工作实在太烦人了，\x01",
            "让愿意做的人去做吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A4")

    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#009F这、这是什么态度。\x02\x03",
            "在大家拼命努力的时候，\x01",
            "你却说出这种事不关己的话。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#045F算了，算了，艾丝蒂尔。\x02\x03",
            "现在更为重要的是\x01",
            "确定魔兽的情况……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#004F啊……哦，\x01",
            "说得没错。\x02\x03",
            "#002F的确，\x01",
            "魔兽可不能就这么放任不管。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F嗯，\x01",
            "明天就是学园祭了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x105, 400)

    ChrTalk(
        0x9,
        (
            "不过，\x01",
            "这些应该和我没有什么关系了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "总之，我现在去还钥匙，\x01",
            "然后把事情告诉艾福托老师。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)
    TurnDirection(0x9, 0x101, 400)

    def lambda_A00():

        label("loc_A00")

        TurnDirection(0x101, 0x9, 0)
        OP_48()
        Jump("loc_A00")

    QueueWorkItem2(0x101, 1, lambda_A00)

    def lambda_A11():

        label("loc_A11")

        TurnDirection(0x105, 0x9, 0)
        OP_48()
        Jump("loc_A11")

    QueueWorkItem2(0x105, 1, lambda_A11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3B")

    def lambda_A30():

        label("loc_A30")

        TurnDirection(0x13B, 0x9, 0)
        OP_48()
        Jump("loc_A30")

    QueueWorkItem2(0x13B, 1, lambda_A30)

    label("loc_A3B")


    ChrTalk(
        0x9,
        (
            "真的很危险，\x01",
            "不要接近门口哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFFFB6E, 0x3E8, 0x1A54, 0x1388, 0x0)

    def lambda_AB0():
        OP_91(0x105, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AB0)
    OP_8E(0x9, 0x82, 0x3E8, 0xFFFFEF8E, 0x1388, 0x0)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x40)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFD")
    OP_44(0x13B, 0x1)

    label("loc_AFD")

    OP_28(0x27, 0x1, 0x2000)
    OP_64(0x0, 0x1)
    OP_71(0x0, 0x10)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    def Function_1_B0F(): pass

    label("Function_1_B0F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B33")
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_48()
    Jump("Function_1_B0F")

    label("loc_B33")

    Return()

    # Function_1_B0F end

    def Function_2_B34(): pass

    label("Function_2_B34")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B53")
    SetChrFlags(0x13B, 0x80)

    label("loc_B53")

    SetMapFlags(0x400000)
    SetChrPos(0x101, -500, 1000, 11470, 96)
    SetChrPos(0x105, 500, 1000, 11470, 96)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B99")
    SetChrPos(0x13B, 0, 1000, 11470, 96)

    label("loc_B99")

    OP_6C(45000, 0)
    OP_6D(0, 1000, 6110, 0)
    OP_6F(0x0, 60)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x105, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD7")
    ClearChrFlags(0x13B, 0x80)

    label("loc_BD7")


    def lambda_BDD():
        OP_8E(0x101, 0xFFFFFE0C, 0x3E8, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDD)
    Sleep(200)

    def lambda_BFD():
        OP_8E(0x105, 0x226, 0x3E8, 0x1838, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BFD)

    def lambda_C18():
        OP_8E(0xA, 0x12C, 0x1F4, 0x100E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C18)
    Sleep(400)
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C68")

    def lambda_C4B():
        OP_8E(0x13B, 0x12C, 0x3E8, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_C4B)
    WaitChrThread(0x13B, 0x1)
    Jump("loc_C6D")

    label("loc_C68")

    WaitChrThread(0x105, 0x1)

    label("loc_C6D")

    OP_72(0x0, 0x800)
    OP_22(0xD3, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0xA, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBD")

    def lambda_CB5():
        TurnDirection(0x13B, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_CB5)

    label("loc_CBD")

    TurnDirection(0x105, 0xA, 400)
    OP_71(0x0, 0x800)

    ChrTalk(
        0x105,
        "#040F啊，艾福托老师。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x105, 400)

    ChrTalk(
        0xA,
        "哦，你们没事吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "旧校舍有魔兽出没的情况，\x01",
            "米克都告诉我了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F啊，是有这么一回事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F已经不用担心了哦。\x01",
            "魔兽全都被消灭掉了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        "哦，这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "说起来，艾丝蒂尔，\x01",
            "你是游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哎呀，真是帮了大忙啊。\x01",
            "要是等到学园祭当天\x01",
            "发生了什么事情那可就糟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F嗯，的确。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F0F")

    ChrTalk(
        0x13B,
        (
            "#640F如果这样想的话……\x02\x03",
            "那个懒虫米克\x01",
            "也算帮了一个大忙。\x02\x03",
            "先不说他的动机如何，\x01",
            "总之发现了魔兽这个隐患。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EE3():
        TurnDirection(0x105, 0x13B, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EE3)
    TurnDirection(0x101, 0x13B, 400)

    ChrTalk(
        0x101,
        "#000F嗯，说的也是。\x02",
    )

    CloseMessageWindow()

    label("loc_F0F")


    ChrTalk(
        0xA,
        (
            "好的，为了谨慎起见，\x01",
            "还是把门给锁上吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F59():
        TurnDirection(0x105, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F59)
    Sleep(100)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0xA,
        (
            "我以后会留心的，\x01",
            "不会让这种事情再次发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F嗯，那样就最好不过了。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x40)

    def lambda_FB8():

        label("loc_FB8")

        TurnDirection(0x101, 0xA, 0)
        OP_48()
        Jump("loc_FB8")

    QueueWorkItem2(0x101, 1, lambda_FB8)

    def lambda_FC9():

        label("loc_FC9")

        TurnDirection(0x105, 0xA, 0)
        OP_48()
        Jump("loc_FC9")

    QueueWorkItem2(0x105, 1, lambda_FC9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF3")

    def lambda_FE8():

        label("loc_FE8")

        TurnDirection(0x13B, 0xA, 0)
        OP_48()
        Jump("loc_FE8")

    QueueWorkItem2(0x13B, 1, lambda_FE8)

    label("loc_FF3")


    def lambda_FF9():
        OP_91(0x105, 0x2BC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_FF9)

    def lambda_1014():
        OP_91(0x101, 0xFFFFFD44, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1014)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1052")

    def lambda_103D():
        OP_91(0x13B, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 2, lambda_103D)

    label("loc_1052")


    def lambda_1058():
        OP_6D(-20, 1000, 9150, 1500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1058)
    OP_8E(0xA, 0xFFFFFFEC, 0x3E8, 0x23BE, 0x7D0, 0x0)
    WaitChrThread(0xA, 0x1)
    Sleep(300)
    OP_22(0x73, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0xA,
        "……唔，没问题了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)

    ChrTalk(
        0xA,
        (
            "那么，\x01",
            "我就回值班室去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "平常到了这个时间\x01",
            "也该关门了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "对了，\x01",
            "你们也不要玩到太晚了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116A")

    ChrTalk(
        0x13B,
        "#640F嗯～不用担心啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_119C")

    label("loc_116A")


    ChrTalk(
        0x105,
        "#040F好的，我们会小心的。\x02",
    )

    CloseMessageWindow()

    label("loc_119C")


    ChrTalk(
        0x101,
        "#000F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_11B8():
        OP_6D(0, 1000, 6110, 1500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11B8)
    OP_8E(0xA, 0x12C, 0x0, 0xFFFFEF2A, 0xBB8, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F8")
    OP_44(0x13B, 0x1)

    label("loc_11F8")

    ClearChrFlags(0xA, 0x40)
    SetChrFlags(0xA, 0x80)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "学园祭的校园任务\x01",
            "【剿灭旧校舍的魔兽】\x07\x00",
            "完成！\x02",
        )
    )

    OP_83(0x2, 0x1)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    ClearMapFlags(0x400000)
    OP_65(0x0, 0x1)
    OP_72(0x0, 0x10)
    EventEnd(0x0)
    Return()

    # Function_2_B34 end

    SaveToFile()

Try(main)
