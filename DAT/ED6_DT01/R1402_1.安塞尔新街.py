from ED6ScenarioHelper import *

def main():
    # 安塞尔新街

    CreateScenaFile(
        FileName            = 'R1402_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'R1402.x',
        MapIndex            = 58,
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

    ClearMapFlags(0x1)
    EventBegin(0x0)
    RemoveParty(0xD, 0xFF)
    ClearChrFlags(0x8, 0x80)
    OP_28(0xF, 0x4, 0x10)
    SetChrPos(0x101, 2200, 4000, 17880, 270)
    SetChrPos(0x102, 3120, 4000, 16810, 270)
    SetChrPos(0x103, 3250, 4000, 17800, 285)
    SetChrPos(0x8, -200, 4000, 17880, 90)
    OP_6D(20070, 0, 19800, 0)
    OP_6C(315000, 0)
    OP_6B(4000, 0)
    FadeToBright(2000, 0)

    def lambda_F0():
        OP_69(0x101, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F0)

    def lambda_FE():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_FE)

    def lambda_10E():
        OP_6B(3000, 6000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_10E)
    Sleep(7000)
    OP_44(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "#130F……呀，你们又帮了我一次啊。\x02\x03",
            "如果没有你们，\x01",
            "我可能早就没命了。\x02\x03",
            "虽然我的研究经费很少，\x01",
            "不过还是要拿出一些给协会作报答。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F你现在才这么说，\x01",
            "一开始就委托游击士不就没事了吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#130F是啊……\x01",
            "下次我一定会好好反省这点的……\x02\x03",
            "那么我就告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3E8, 0xFA0, 0x3EE4, 0x7D0, 0x0)

    def lambda_2F8():

        label("loc_2F8")

        TurnDirection(0x101, 0x8, 0)
        OP_48()
        Jump("loc_2F8")

    QueueWorkItem2(0x101, 1, lambda_2F8)

    def lambda_309():

        label("loc_309")

        TurnDirection(0x102, 0x8, 0)
        OP_48()
        Jump("loc_309")

    QueueWorkItem2(0x102, 1, lambda_309)

    def lambda_31A():

        label("loc_31A")

        TurnDirection(0x103, 0x8, 0)
        OP_48()
        Jump("loc_31A")

    QueueWorkItem2(0x103, 1, lambda_31A)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(
        0x103,
        (
            "#023F等一下，\x01",
            "不把你送回城里真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(
        0x8,
        (
            "#130F哈哈哈，\x01",
            "送到这里就可以了，\x01",
            "而且我的荷包已经空空如也了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#132F那就这样吧……\x01",
            "希望我们有缘再会。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_423():
        OP_6D(2910, 4000, 17460, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_423)
    OP_8E(0x8, 0x424, 0x4B0, 0x253A, 0x7D0, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x8, 0x2)

    ChrTalk(
        0x102,
        "#014F……真是个不可思议的人。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#501F咦，是这样吗？\x02\x03",
            "我觉得他就是那种典型的学者嘛。\x01",
            "　\x02\x03",
            "一旦集中注意力做某件事情，\x01",
            "就会无视周围情况的那种类型。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#018F…………这说的不是你自己吗。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#009F哼。\x02\x03",
            "我才不是这样呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F不过，虽然外表看起来只是个学者，\x01",
            "但说不定是个很厉害的人物哦。\x02\x03",
            "不管怎么说，\x01",
            "他敢孤身一人来这种地方也算不简单了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#007F就算是吧……\x02\x03",
            "到头来还不是要靠我们帮忙，\x01",
            "不然就陷入绝境了吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#020F这也就是我们游击士的职责所在了。\x01",
            "　\x02\x03",
            "那么，\x01",
            "我们这就回去吧。\x02",
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
            "任务【琥珀之塔的可疑人物】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
