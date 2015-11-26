from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2102_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2102.x',
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

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_28(0x20, 0x1, 0x10)
    Fade(1000)
    SetChrPos(0x102, 113500, 0, 102600, 90)
    SetChrPos(0x101, 112500, 0, 102300, 90)
    SetChrPos(0x105, 111200, 0, 103100, 90)
    OP_51(0xE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6C(135000, 0)

    def lambda_F9():
        OP_6C(155000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_F9)

    def lambda_109():
        OP_69(0xE, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_109)
    OP_6B(2800, 3000)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xE, 0x2)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#011F#1P原来如此，\x01",
            "『独眼狮子』啊…………\x02\x03",
            "照谜语上所写的，\x01",
            "这看起来不就是一只狮子吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P这里也正是『陆地之港』吧。\x02\x03",
            "绝对没错。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#1P是啊，那就调查一下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xE, 0x1, (scpexpr(EXPR_PUSH_LONG, 0x1C32C), scpexpr(EXPR_PUSH_LONG, 0x1BB5C), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x19000), scpexpr(EXPR_PUSH_LONG, 0x190C8), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_24A():
        OP_6C(180000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_24A)

    def lambda_25A():
        OP_69(0xE, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_25A)
    SetChrFlags(0x102, 0x40)
    OP_8C(0x102, 0, 400)

    def lambda_274():
        OP_8E(0x101, 0x1BB5C, 0x0, 0x190C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_274)

    def lambda_28F():
        OP_8E(0x105, 0x1B7D8, 0x0, 0x19320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_28F)
    OP_8E(0x102, 0x1BB5C, 0x0, 0x196A4, 0x7D0, 0x0)
    OP_8E(0x102, 0x1C1A6, 0x0, 0x196A4, 0x7D0, 0x0)
    OP_8E(0x102, 0x1C32C, 0x0, 0x19000, 0x7D0, 0x0)
    OP_8C(0x102, 225, 400)
    ClearChrFlags(0x102, 0x40)
    Sleep(600)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#012F#1P嗯，有一张卡片。\x02\x03",
            "立刻确认内容。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "『啊，探寻者们。\x01",
            "　如女神一般直视真实，\x01",
            "　抛弃虚伪的人啊。\x01",
            "　\x01",
            "　前往开合桥的对面、\x01",
            "　安身于钢铁之鹤旁的\x01",
            "　木桶所在之处吧。\x01",
            "　如是，探寻者们，\x01",
            "　汝等将至苍之光所在。\x01",
            "　　　　　　　　　　　　　　　怪盗Ｂ』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#509F#2P哼，怎么还是这种东西。\x01",
            "这回又是『钢铁之鹤』了。\x02\x03",
            "#505F所谓『开合桥的对面』\x01",
            "就是港湾的方向吧……\x02\x03",
            "呼，我们究竟要被这种东西\x01",
            "捉弄到什么时候啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#041F#4P呵呵，\x01",
            "只要再坚持一下就好了。\x02\x03",
            "再加把劲吧，\x01",
            "艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018F#1P艾丝蒂尔…………\x01",
            "你不是一向都很干劲十足的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#008F#2P啊…………\x02\x03",
            "人、人家只是\x01",
            "觉得找了这么久有点累嘛。\x02\x03",
            "好、好了，\x01",
            "我们鼓足干劲出发吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F#1P真拿你没办法……\x02",
    )

    CloseMessageWindow()
    OP_64(0x0, 0x1)

    def lambda_6AB():
        OP_6B(3500, 2000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6AB)
    OP_8E(0x102, 0x1C1A6, 0x0, 0x196A4, 0x7D0, 0x0)
    OP_8E(0x102, 0x1BB5C, 0x0, 0x196A4, 0x7D0, 0x0)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
