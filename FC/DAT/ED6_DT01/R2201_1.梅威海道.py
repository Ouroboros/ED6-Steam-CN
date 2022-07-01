from ED6ScenarioHelper import *

def main():
    # 梅威海道

    CreateScenaFile(
        FileName            = 'R2201_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'R2201.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60020",
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

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE0")
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(
        0x8,
        "男性的声音",
        "呜哦哦～～来人啊～！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x8, 0)
    ClearChrFlags(0xA, 0x80)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    ClearChrFlags(0xB, 0x80)
    Fade(1000)
    OP_6C(315000, 0)
    OP_4A(0x9, 0)
    OP_4A(0xA, 0)
    OP_4A(0xB, 0)
    SetChrChipByIndex(0x9, 7)
    SetChrChipByIndex(0xA, 7)
    SetChrChipByIndex(0xB, 7)

    def lambda_101():
        OP_69(0x8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_101)

    def lambda_10F():
        OP_92(0x9, 0x8, 0x3E8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10F)

    def lambda_124():
        OP_92(0xA, 0x8, 0x3E8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_124)

    def lambda_139():
        OP_92(0xB, 0x8, 0x3E8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_139)
    OP_6C(45000, 4000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0xB4, 0x1F4, 0x3E8, 0x0)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x8, 0xB, 400)
    OP_4A(0xA, 1)
    SetChrChipByIndex(0xA, 6)
    OP_4B(0xA, 0)
    Sleep(400)
    TurnDirection(0x8, 0x9, 400)
    OP_4A(0xA, 0)
    SetChrChipByIndex(0xA, 7)
    OP_4B(0xA, 1)
    OP_4A(0x9, 1)
    SetChrChipByIndex(0x9, 6)
    OP_4B(0x9, 0)
    Sleep(400)
    TurnDirection(0x8, 0xA, 400)
    OP_4A(0x9, 0)
    SetChrChipByIndex(0x9, 7)
    OP_4B(0x9, 1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)

    def lambda_1E9():
        OP_92(0x9, 0x8, 0x3E8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E9)

    def lambda_1FE():
        OP_92(0xA, 0x8, 0x3E8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1FE)

    def lambda_213():
        OP_92(0xB, 0x8, 0x3E8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_213)
    OP_4A(0xA, 1)
    OP_4A(0xB, 1)
    Sleep(200)
    OP_4B(0xB, 1)
    Sleep(200)
    OP_4B(0xA, 1)
    SetChrPos(0x101, 69700, -6000, -9500, 0)
    SetChrPos(0x102, 69700, -6000, -10500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27C")
    SetChrPos(0x136, 69700, -6000, -11500, 0)

    label("loc_27C")

    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_298")
    SetChrFlags(0x136, 0x40)

    label("loc_298")

    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)

    def lambda_2B2():
        OP_8E(0x101, 0x11D28, 0xFFFFE890, 0xFFFFF95C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B2)

    def lambda_2CD():
        OP_8E(0x102, 0x1174C, 0xFFFFE890, 0xFFFFF830, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CD)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_30A")

    def lambda_2F5():
        OP_8E(0x136, 0x11170, 0xFFFFE890, 0xFFFFF0F6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_2F5)

    label("loc_30A")

    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0x87, 0x1F4, 0x3E8, 0x0)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    SetChrChipByIndex(0x9, 6)
    SetChrChipByIndex(0xA, 6)
    SetChrChipByIndex(0xB, 6)
    OP_4B(0x9, 0)
    OP_4B(0xA, 0)
    OP_4B(0xB, 0)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 2)
    OP_43(0x101, 0x1, 0x0, 0x2)
    OP_8C(0x101, 0, 0)
    WaitChrThread(0x102, 0x1)
    SetChrChipByIndex(0x102, 4)
    OP_43(0x102, 0x1, 0x0, 0x2)
    OP_8C(0x102, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_39B")
    WaitChrThread(0x136, 0x1)
    OP_8C(0x136, 0, 0)

    label("loc_39B")

    TurnDirection(0x8, 0x101, 0)
    OP_69(0x101, 0x320)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    ChrTalk(
        0x8,
        "救、救命啊～～！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3EF")

    ChrTalk(
        0x136,
        "#044F啊，不好！\x02",
    )

    CloseMessageWindow()

    label("loc_3EF")


    ChrTalk(
        0x102,
        "#012F艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F好！\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_442")
    OP_44(0x136, 0xFF)

    label("loc_442")

    Battle(0x3F3, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_45B"),
        (SWITCH_DEFAULT, "loc_45E"),
    )


    label("loc_45B")

    OP_B4(0x0)
    Return()

    label("loc_45E")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x101, 73500, -6000, 0, 0)
    SetChrPos(0x102, 72120, -6080, -170, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4B3")
    SetChrPos(0x136, 71000, -6000, -1000, 0)

    label("loc_4B3")

    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xC, 0x0)
    OP_0D()
    Sleep(1000)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F呼……\x01",
            "还好及时解决掉了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_53F")
    TurnDirection(0x136, 0x101, 400)

    label("loc_53F")

    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，\x01",
            "已经没事了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5D6")
    TurnDirection(0x136, 0x8, 400)

    ChrTalk(
        0x136,
        "#040F请问您有没有受伤呢？\x02",
    )

    CloseMessageWindow()

    def lambda_5BD():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BD)

    def lambda_5CB():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5CB)
    Jump("loc_5F8")

    label("loc_5D6")

    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        "#010F您没有受伤吧？\x02",
    )

    CloseMessageWindow()

    label("loc_5F8")


    ChrTalk(
        0x8,
        (
            "哦哦～\x01",
            "刚才真是太危险了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我还以为肯定会\x01",
            "成为鱼饵了呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_660():
        OP_94(0x1, 0x8, 0x0, 0x834, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_660)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#002F真是的，\x01",
            "竟敢自己一个人跑到这种地方来。\x02\x03",
            "到底是怎么回事？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "唔～\x01",
            "实际上是有原因的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…………不过嘛，\x01",
            "我不太方便告诉你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F哎呀。\x01",
            "不过算了吧。\x02\x03",
            "#002F总之，别在这种危险的地方\x01",
            "随意逛来逛去就行了。\x02\x03",
            "等真的成了鱼饵就太迟了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "说的是啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    ChrTalk(
        0x8,
        (
            "今天的确是很危险啊，\x01",
            "可是打工赚的钱\x01",
            "就只有那么一点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "好吧…………\x01",
            "我还要拼命发奋才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F？？？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D8")

    ChrTalk(
        0x102,
        (
            "#010F……对了，\x01",
            "接下来您打算怎么办呢？\x02\x03",
            "我们本来应该\x01",
            "把您送回城里的，\x01",
            "可是现在我们也有要紧事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92B")

    label("loc_8D8")


    ChrTalk(
        0x102,
        (
            "#010F……对了，\x01",
            "接下来您打算怎么办呢？\x02\x03",
            "如果您不介意的话，\x01",
            "我们就护送您到城里吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92B")

    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "不用不用，没关系的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "对于逃跑的本领我还是有自信的，\x01",
            "只要在海道上就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "再见了，\x01",
            "谢谢你们！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)

    def lambda_9A3():

        label("loc_9A3")

        TurnDirection(0x101, 0x8, 0)
        OP_48()
        Jump("loc_9A3")

    QueueWorkItem2(0x101, 1, lambda_9A3)

    def lambda_9B4():

        label("loc_9B4")

        TurnDirection(0x102, 0x8, 0)
        OP_48()
        Jump("loc_9B4")

    QueueWorkItem2(0x102, 1, lambda_9B4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A1F")

    def lambda_9D2():

        label("loc_9D2")

        TurnDirection(0x136, 0x8, 0)
        OP_48()
        Jump("loc_9D2")

    QueueWorkItem2(0x136, 1, lambda_9D2)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x136, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x136, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x136, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A5E")

    label("loc_A1F")

    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A5E")


    def lambda_A64():
        OP_69(0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A64)
    OP_8E(0x8, 0x11170, 0x0, 0x1F4, 0x1770, 0x0)
    OP_8E(0x8, 0x11170, 0x0, 0xFFFFD8F0, 0x1770, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AB2")
    OP_44(0x136, 0x1)

    label("loc_AB2")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F毫无紧张感的人呢～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F应该是有什么原因\x01",
            "才跑到这里附近来的吧。\x02\x03",
            "希望他不要再遇到危险就好了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B62")
    ClearChrFlags(0x136, 0x40)

    label("loc_B62")

    Fade(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BB3")
    OP_51(0x1, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BD1")

    label("loc_BB3")

    OP_51(0x1, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BD1")

    OP_69(0x0, 0x3E8)
    OP_28(0x1E, 0x1, 0x8000)
    EventEnd(0x0)

    label("loc_BE0")

    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
