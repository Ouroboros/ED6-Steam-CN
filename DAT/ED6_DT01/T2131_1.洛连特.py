from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2131_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2131.x',
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
        "Function_1_6C3",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_28(0x20, 0x1, 0x8)
    Fade(1000)
    SetChrPos(0x102, 25900, 0, 26500, 315)
    SetChrPos(0x101, 27000, 0, 26500, 315)
    SetChrPos(0x105, 27500, 0, 27100, 270)
    OP_51(0x9, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6158), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6DC4), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x9, 0x7D0)

    ChrTalk(
        0x101,
        (
            "#006F红与黑的圆舞曲…………对吧。\x02\x03",
            "嗯，除了这个轮盘，\x01",
            "应该找不到其他更合适的了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F的确如此。\x02\x03",
            "那么我们就调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "哦，是客人啊…………\x01",
            "在找什么东西吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D2():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D2)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#010F非常抱歉，\x01",
            "我们马上就好了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21C():

        label("loc_21C")

        TurnDirection(0x101, 0x102, 0)
        OP_48()
        Jump("loc_21C")

    QueueWorkItem2(0x101, 1, lambda_21C)

    def lambda_22D():

        label("loc_22D")

        TurnDirection(0x105, 0x102, 0)
        OP_48()
        Jump("loc_22D")

    QueueWorkItem2(0x105, 1, lambda_22D)

    def lambda_23E():

        label("loc_23E")

        TurnDirection(0x8, 0x102, 0)
        OP_48()
        Jump("loc_23E")

    QueueWorkItem2(0x8, 1, lambda_23E)
    SetChrFlags(0x102, 0x40)
    OP_8E(0x102, 0x6572, 0x0, 0x6A4A, 0x7D0, 0x0)
    OP_8C(0x102, 315, 400)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x8, 0x1)
    Sleep(600)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#012F……果然这里也有。\x02\x03",
            "横着贴上了一张卡片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F那么…………\x01",
            "下一条提示\x01",
            "写的又是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        "#010F嗯，看看吧。\x02",
    )

    CloseMessageWindow()
    Sleep(400)
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
            "　前往栖身于陆地之港的\x01",
            "　独眼狮子所在之处吧。\x01",
            "　如是，探寻者们，\x01",
            "　汝等将至苍之光所在。\x01",
            "　　　　　　　　　　　怪盗Ｂ』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    def lambda_432():

        label("loc_432")

        TurnDirection(0x105, 0x102, 0)
        OP_48()
        Jump("loc_432")

    QueueWorkItem2(0x105, 1, lambda_432)

    def lambda_443():

        label("loc_443")

        TurnDirection(0x8, 0x102, 0)
        OP_48()
        Jump("loc_443")

    QueueWorkItem2(0x8, 1, lambda_443)
    OP_8E(0x102, 0x652C, 0x0, 0x6784, 0x7D0, 0x0)

    def lambda_468():
        TurnDirection(0x102, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_468)
    TurnDirection(0x101, 0x102, 400)
    OP_44(0x105, 0x1)
    OP_44(0x8, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#006F好的，已经记录下来了。\x02\x03",
            "重要的部分就是『陆地之港』\x01",
            "和『独眼狮子』这两点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F这次变成『独眼』了吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F根据至今为止的经验，\x01",
            "我认为只要找到相应的地方后\x01",
            "再仔细调查一下就可以了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F嗯，\x01",
            "那我们这就展开行动吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "？？？\x02",
    )

    CloseMessageWindow()

    def lambda_627():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_627)

    def lambda_635():
        TurnDirection(0x105, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_635)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x101,
        "#001F打扰您了～\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_8C(0x8, 0, 0)
    OP_4B(0x8, 255)
    OP_64(0x0, 0x1)
    OP_51(0x1, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x102, 0x40)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    def Function_1_6C3(): pass

    label("Function_1_6C3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "钓鱼工具并排摆在架子上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73C")
    OP_28(0x21, 0x1, 0x1000)
    Jump("loc_908")

    label("loc_73C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_7A7")
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#000F钓鱼竿用完之后，\x01",
            "要还给这家店的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_908")

    label("loc_7A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_7F9")
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#007F呼，\x01",
            "本来我还想好好钓一次鱼的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_908")

    label("loc_7F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_806")
    Jump("loc_908")

    label("loc_806")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_8BE")
    Sleep(400)
    OP_28(0x21, 0x1, 0x1000)

    ChrTalk(
        0x101,
        (
            "#501F…………这里的东西\x01",
            "可不可以借走呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F问问店里的人吧。\x02\x03",
            "这家店的老板在一楼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_908")

    label("loc_8BE")

    Sleep(400)
    OP_28(0x21, 0x1, 0x1000)

    ChrTalk(
        0x101,
        (
            "#501F这里果然也可以租借钓鱼竿啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_908")

    TalkEnd(0xFF)
    Return()

    # Function_1_6C3 end

    SaveToFile()

Try(main)
