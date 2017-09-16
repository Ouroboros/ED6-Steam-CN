from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3403_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(610490, -10, -60800, 0)
    OP_6C(225000, 0)
    OP_4A(0x8, 255)
    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    SetChrPos(0x101, 610110, -10, -60540, 180)
    SetChrPos(0x102, 609200, 0, -59580, 180)
    SetChrPos(0x107, 610360, 0, -59200, 180)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0xFE,
        "哈啊～………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……我真没用啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#506F？？？\x02\x03",
            "总、总觉得\x01",
            "这里的气氛好像很沉重呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "嗯？啊啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，没什么事啦。\x01",
            "只是刚才被前辈痛骂了一顿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……你们找我有什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F啊，嗯。\x01",
            "我们想麻烦您一点小事情。\x02\x03",
            "其实我们在寻找\x01",
            "运输车用的小型导力引擎。\x02\x03",
            "而它的保管场所\x01",
            "似乎就在这附近……\x02\x03",
            "您知道是放在哪儿的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是运输车用的\x01",
            "驱动导力器吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们找那种东西\x01",
            "要用来做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F因为运输车在平原那里抛锚了……\x01",
            "　\x02\x03",
            "是由于导力引擎的故障所引起的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "啊，原来如此，我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就是说需要\x01",
            "更换用的零件对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样我就可以放心交给你们了，\x01",
            "请稍微等一会儿。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xFE, 0x94A16, 0xFFFFFFE2, 0xFFFF0C04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x94B7E, 0xA, 0xFFFF0074, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x94A16, 0xFFFFFFE2, 0xFFFF0C04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x94F98, 0xFFFFFFD8, 0xFFFF0D94, 0xBB8, 0x0)
    OP_8C(0xFE, 360, 400)

    ChrTalk(
        0xFE,
        "久等了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为库存已经所剩不多了，\x01",
            "所以你们一定要送到啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_94(0x1, 0xFE, 0x0, 0x258, 0x7D0, 0x0)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "驱动用导力器\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_94(0x1, 0xFE, 0xB4, 0x258, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        "#000F嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F好，\x01",
            "那么我们立刻回王先生那里吧。\x02\x03",
            "他们肯定还在托兰特平原那里。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们也要注意安全哦。\x02",
    )

    CloseMessageWindow()

    def lambda_66D():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66D)
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x107,
        (
            "#060F啊，好的。\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我们就告辞了。\x02",
    )

    CloseMessageWindow()
    OP_3E(0x346, 1)
    OP_28(0x29, 0x4, 0x8)
    OP_28(0x29, 0x1, 0x10)
    OP_28(0x29, 0x1, 0x20)
    OP_A2(0x2)
    EventEnd(0x0)
    Return()

    # Function_2_AC end

    SaveToFile()

Try(main)
