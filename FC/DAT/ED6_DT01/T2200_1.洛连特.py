from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2200_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2200.x',
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
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    OP_69(0x101, 0x0)
    SetMapFlags(0x400000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrPos(0x101, 113000, 2000, 22300, 270)
    SetChrPos(0x102, 114500, 2000, 21500, 270)
    SetChrPos(0x105, 115000, 2000, 22600, 270)
    OP_51(0xA, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x0, 30)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    FadeToBright(2000, 0)

    def lambda_12F():
        OP_94(0x1, 0x101, 0x0, 0x15E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12F)
    Sleep(200)

    def lambda_14A():
        OP_94(0x1, 0x102, 0x0, 0x1770, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14A)
    Sleep(200)

    def lambda_165():
        OP_94(0x1, 0x105, 0x0, 0x1900, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_165)

    def lambda_17B():
        OP_69(0xA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_17B)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    def lambda_18F():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18F)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F呼～～\x02\x03",
            "总算是勉强完成了任务，\x01",
            "不过总感觉不够彻底啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F嗯，是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F……………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#002F啊，约修亚你怎么了……\x02\x03",
            "一个人在那里想些什么呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F啊…………？\x01",
            "……嗯，没什么。\x02\x03",
            "只是在想……\x01",
            "犯人偷烛台的动机究竟是什么呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊，对啊。\x02\x03",
            "最后我们还是不明白这一点呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        (
            "#042F最后一张卡片的内容\x01",
            "应该隐含着更深层的含义。\x02\x03",
            "从那种行文的语气来看，\x01",
            "好像对于艾丝蒂尔你们\x01",
            "抱有什么期待一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F唔……\x01",
            "我还是非常在意呢。\x02\x03",
            "#002F不如……\x01",
            "我们继续进行调查吧。\x02\x03",
            "先判断一下犯人\x01",
            "大概会隐藏在什么地方。\x02\x03",
            "等今晚时机一到，\x01",
            "我们就去对应的房屋里面调查。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x102,
        (
            "#018F那我们不就和小偷\x01",
            "没什么两样了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F可是，我不甘心啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F这也是没有办法的事，\x01",
            "委托人并不希望这样。\x02\x03",
            "#010F我们就忍住吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#505F唔…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F好了，我们走吧。\x02\x03",
            "市长说的话很对，\x01",
            "还要许多需要我们去做的事情呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F……嗯，明白了。\x01",
            "只有忍住了。\x02\x03",
            "#006F那好，\x01",
            "我们就调整心情继续努力吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#041F嗯，就应该这样呢。\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【烛台失窃事件】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
