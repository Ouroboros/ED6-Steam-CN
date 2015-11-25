from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T1300_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
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
        "Function_1_A0B",          # 01, 1
        "Function_2_A26",          # 02, 2
        "Function_3_A55",          # 03, 3
        "Function_4_A84",          # 04, 4
        "Function_5_AB3",          # 05, 5
        "Function_6_B0F",          # 06, 6
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x0, -39200, 0, 31000, 0)
    SetChrPos(0x1, -39200, 0, 32200, 0)
    SetChrPos(0x2, -39200, 0, 33400, 0)
    SetChrPos(0xA, -39200, 0, 34600, 0)
    OP_43(0x0, 0x1, 0x1, 0x1)
    OP_43(0x1, 0x1, 0x1, 0x2)
    OP_43(0x2, 0x1, 0x1, 0x3)
    OP_43(0xA, 0x1, 0x1, 0x4)
    OP_A2(0x1)
    OP_A2(0x2)
    OP_A2(0x3)
    OP_A2(0x4)

    def lambda_DF():
        OP_6C(225000, 8000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DF)

    def lambda_EF():
        OP_6B(2800, 8000)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_EF)
    OP_6D(-50000, 0, 6500, 8000)
    OP_A5(0x1)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0xA, 0xFF)
    Fade(1000)
    SetChrPos(0x101, -51000, 0, 18400, 180)
    SetChrPos(0x102, -50000, 0, 20000, 180)
    SetChrPos(0x103, -50000, 0, 17200, 180)
    SetChrPos(0xA, -48500, 0, 21500, 180)
    OP_69(0x101, 0x0)

    def lambda_16F():
        OP_8E(0x101, 0xFFFF38C8, 0x0, 0x43F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16F)

    def lambda_18A():
        OP_8E(0x102, 0xFFFF3CB0, 0x0, 0x4A38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18A)

    def lambda_1A5():
        OP_8E(0x103, 0xFFFF3CB0, 0x0, 0x3DB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A5)

    def lambda_1C0():
        OP_8E(0xA, 0xFFFF428C, 0x0, 0x43F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1C0)

    def lambda_1DB():
        OP_6D(-50000, 0, 17400, 2000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1DB)
    Sleep(1000)
    Sleep(2000)

    ChrTalk(
        0xA,
        "哈，总算到了……\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        (
            "#007F呼，\x01",
            "真是不容易啊～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F现在终于可以放松一下了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xA, 400)

    ChrTalk(
        0x103,
        (
            "#020F从卢安来接你的游击士\x01",
            "应该很快就会到的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0x103, 180, 400)
    Sleep(800)

    ChrTalk(
        0x103,
        (
            "#020F……看吧，\x01",
            "刚说着他就来了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, -50000, 500, 8700, 0)
    ClearChrFlags(0xB, 0x80)

    def lambda_35C():

        label("loc_35C")

        TurnDirection(0x101, 0xB, 400)
        OP_48()
        Jump("loc_35C")

    QueueWorkItem2(0x101, 1, lambda_35C)

    def lambda_36D():

        label("loc_36D")

        TurnDirection(0x102, 0xB, 400)
        OP_48()
        Jump("loc_36D")

    QueueWorkItem2(0x102, 1, lambda_36D)

    def lambda_37E():

        label("loc_37E")

        TurnDirection(0x103, 0xB, 400)
        OP_48()
        Jump("loc_37E")

    QueueWorkItem2(0x103, 1, lambda_37E)

    def lambda_38F():

        label("loc_38F")

        TurnDirection(0xA, 0xB, 400)
        OP_48()
        Jump("loc_38F")

    QueueWorkItem2(0xA, 1, lambda_38F)
    OP_70(0x1, 0x64)
    OP_73(0x1)
    OP_6F(0x1, 100)
    OP_70(0x1, 0x0)
    OP_8E(0xB, 0xFFFF3CB0, 0x1F4, 0x3390, 0xBB8, 0x0)
    OP_8E(0xB, 0xFFFF42F0, 0x1F4, 0x3DB8, 0xBB8, 0x0)
    TurnDirection(0xB, 0x103, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0xA, 0xFF)
    Sleep(800)

    ChrTalk(
        0xB,
        "辛苦你们了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我是卢安支部所属的\x01",
            "准游击士梅尔茨！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F你也辛苦了。\x01",
            "这边这位就是委托人哈尔德先生。\x02\x03",
            "待会儿就拜托你\x01",
            "把他护送到卢安了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "明白！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(
        0xB,
        "请您多多指教！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你、你还真是\x01",
            "精神抖擞啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "总之就拜托你了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "刚才多谢\x01",
            "你们三位的帮忙。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        "#001F保重哦⊙\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 400)

    ChrTalk(
        0x102,
        "#010F工作方面也请加油。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0xA,
        "哈哈，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "虽然可能已经迟到了，\x01",
            "不过我会努力的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 400)

    ChrTalk(
        0xB,
        "那么我们就失陪了！\x02",
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x1, 0x5)
    OP_43(0xA, 0x1, 0x1, 0x6)
    OP_A2(0x5)
    OP_A2(0x6)

    def lambda_6E1():

        label("loc_6E1")

        TurnDirection(0x101, 0xA, 400)
        OP_48()
        Jump("loc_6E1")

    QueueWorkItem2(0x101, 1, lambda_6E1)

    def lambda_6F2():

        label("loc_6F2")

        TurnDirection(0x102, 0xA, 400)
        OP_48()
        Jump("loc_6F2")

    QueueWorkItem2(0x102, 1, lambda_6F2)

    def lambda_703():

        label("loc_703")

        TurnDirection(0x103, 0xA, 400)
        OP_48()
        Jump("loc_703")

    QueueWorkItem2(0x103, 1, lambda_703)
    OP_A5(0x5)
    OP_A5(0x7)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_6F(0x1, 100)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F竟然会有这么精神抖擞的人啊～\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是个准游击士呢。\x02\x03",
            "和我们一样，\x01",
            "好像也正在支部进行实习……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(
        0x103,
        (
            "#020F嗯，不止是你们，\x01",
            "很多人都想成为优秀的游击士哦。\x02\x03",
            "所以说，为了成为正游击士，\x01",
            "你们更要拼命努力才行哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#002F嗯～\x01",
            "我也要加倍努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x02\x03",
            "我们总是要依靠雪拉姐姐，\x01",
            "还真是有点过意不去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F呵呵，看来受到了鞭策呢。\x01",
            "　\x02\x03",
            "那么，\x01",
            "我们回协会汇报工作吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x10, 0x4, 0x10)
    OP_28(0x10, 0x3, 0x8)
    OP_28(0x10, 0x1, 0x20)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【护卫委托】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    def Function_1_A0B(): pass

    label("Function_1_A0B")

    OP_A6(0x1)
    OP_8E(0x0, 0xFFFF3CB0, 0x0, 0x4650, 0x7D0, 0x0)
    OP_A3(0x1)
    Return()

    # Function_1_A0B end

    def Function_2_A26(): pass

    label("Function_2_A26")

    OP_A6(0x2)
    OP_8E(0x1, 0xFFFF66E0, 0x0, 0x7918, 0x7D0, 0x0)
    OP_8E(0x1, 0xFFFF3CB0, 0x0, 0x4650, 0x7D0, 0x0)
    OP_A3(0x2)
    Return()

    # Function_2_A26 end

    def Function_3_A55(): pass

    label("Function_3_A55")

    OP_A6(0x3)
    OP_8E(0x2, 0xFFFF66E0, 0x0, 0x7918, 0x7D0, 0x0)
    OP_8E(0x2, 0xFFFF3CB0, 0x0, 0x4650, 0x7D0, 0x0)
    OP_A3(0x3)
    Return()

    # Function_3_A55 end

    def Function_4_A84(): pass

    label("Function_4_A84")

    OP_A6(0x4)
    OP_8E(0xA, 0xFFFF66E0, 0x0, 0x7918, 0x7D0, 0x0)
    OP_8E(0xA, 0xFFFF3CB0, 0x0, 0x4650, 0x7D0, 0x0)
    OP_A3(0x4)
    Return()

    # Function_4_A84 end

    def Function_5_AB3(): pass

    label("Function_5_AB3")

    OP_A6(0x5)
    OP_8E(0xB, 0xFFFF3CB0, 0x1F4, 0x3390, 0x7D0, 0x0)
    OP_8E(0xB, 0xFFFF3CB0, 0x1F4, 0x28DA, 0x7D0, 0x0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x64)
    OP_73(0x1)
    OP_A2(0x7)
    OP_8E(0xB, 0xFFFF3CB0, 0x1F4, 0x1A2C, 0x7D0, 0x0)
    SetChrFlags(0xB, 0x80)
    OP_A3(0x5)
    Return()

    # Function_5_AB3 end

    def Function_6_B0F(): pass

    label("Function_6_B0F")

    OP_A6(0x6)
    OP_8E(0xA, 0xFFFF42F0, 0x1F4, 0x3DB8, 0x7D0, 0x0)
    OP_8E(0xA, 0xFFFF3CB0, 0x1F4, 0x3390, 0x7D0, 0x0)
    OP_8E(0xA, 0xFFFF3CB0, 0x1F4, 0x2C88, 0x3E8, 0x0)
    OP_A3(0x6)
    OP_A6(0x7)
    OP_8E(0xA, 0xFFFF3CB0, 0x1F4, 0x21FC, 0x7D0, 0x0)
    SetChrFlags(0xA, 0x80)
    OP_A3(0x7)
    Return()

    # Function_6_B0F end

    SaveToFile()

Try(main)
