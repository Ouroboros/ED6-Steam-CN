from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2710_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2710.x',
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
        "Function_1_441",          # 01, 1
        "Function_2_C96",          # 02, 2
        "Function_3_CB2",          # 03, 3
        "Function_4_CE2",          # 04, 4
        "Function_5_D12",          # 05, 5
        "Function_6_D42",          # 06, 6
        "Function_7_D67",          # 07, 7
        "Function_8_DA0",          # 08, 8
        "Function_9_DE9",          # 09, 9
        "Function_10_E37",         # 0A, 10
        "Function_11_E85",         # 0B, 11
        "Function_12_2E0E",        # 0C, 12
        "Function_13_2E32",        # 0D, 13
        "Function_14_2E5B",        # 0E, 14
        "Function_15_35F3",        # 0F, 15
        "Function_16_3F8D",        # 10, 16
        "Function_17_3FCD",        # 11, 17
        "Function_18_3FF1",        # 12, 18
        "Function_19_400B",        # 13, 19
        "Function_20_404D",        # 14, 20
        "Function_21_4075",        # 15, 21
        "Function_22_4091",        # 16, 22
        "Function_23_420A",        # 17, 23
        "Function_24_48FD",        # 18, 24
        "Function_25_5120",        # 19, 25
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
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    SetChrPos(0xB, 1596, 0, 12441, 90)
    SetChrPos(0xC, 1513, 0, 13617, 90)
    SetChrPos(0xD, 909, 0, 13169, 90)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "唔………\x01",
            "完全不听别人的劝告啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "真是的，\x01",
            "到底想要怎么样嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "王国军原来都是些\x01",
            "畏惧强权的家伙啊……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_4B(0xB, 255)
    Sleep(50)
    OP_4B(0xC, 255)
    Sleep(70)
    OP_4B(0xD, 255)
    SetChrPos(0x101, -550, 0, 3400, 0)
    SetChrPos(0x102, -1460, 0, 2620, 0)
    SetChrPos(0x105, -1000, 0, 1420, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)

    def lambda_200():
        OP_94(0x1, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_200)

    def lambda_216():
        OP_94(0x1, 0x1, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_216)

    def lambda_22C():
        OP_94(0x1, 0x2, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_22C)
    OP_6D(-550, 0, 8300, 3000)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0xB, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#501F…………？\x02\x03",
            "那群人在那里围着看什么呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xB, 400)
    TurnDirection(0x105, 0xB, 400)

    ChrTalk(
        0x102,
        (
            "#010F看起来好像只是一般的旅行者……\x01",
            "　\x02\x03",
            "而且…………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F……而且什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F守备队的人一个都不在啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        "#044F啊，果然…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F发生了什么事件吗…………？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F现在还不清楚呢……\x02\x03",
            "总之还是先找一个\x01",
            "守备队的人来问问比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    def Function_1_441(): pass

    label("Function_1_441")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetMapFlags(0x400000)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0xE, 255)
    OP_69(0x101, 0x0)
    SetChrPos(0x8, -4000, 0, 4000, 90)
    SetChrPos(0x101, -7000, 1000, 3800, 90)
    SetChrPos(0xE, -7000, 1000, 4900, 90)
    SetChrPos(0x105, -8500, 1000, 5200, 180)
    SetChrPos(0xB, 1596, 0, 12441, 90)
    SetChrPos(0xC, 1513, 0, 13617, 90)
    SetChrPos(0xD, 909, 0, 13169, 90)
    OP_43(0x8, 0x1, 0x1, 0x2)
    OP_43(0x101, 0x1, 0x1, 0x3)
    OP_43(0xE, 0x1, 0x1, 0x4)
    OP_43(0x105, 0x1, 0x1, 0x5)
    OP_6D(-1000, 0, 8700, 4000)
    WaitChrThread(0x105, 0x1)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "唔…………\x01",
            "好像没有什么进展啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)

    ChrTalk(
        0x101,
        (
            "#000F那里围着的一群人\x01",
            "和这件事有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5DA():
        TurnDirection(0xE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5DA)

    def lambda_5E8():
        TurnDirection(0x105, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E8)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "他们都是被这次事件\x01",
            "牵连的受害者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "麻烦的旅行者\x01",
            "现在正在食堂里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F食堂…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是啊，\x01",
            "无论如何也要说服他才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我的部下们\x01",
            "正在努力劝说他呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F说服…………\x02\x03",
            "#002F对了，那个麻烦的旅客\x01",
            "究竟是个什么样的人呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "唔，实际上他是……\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xB, 0x8, 400)
    Sleep(400)

    ChrTalk(
        0xB,
        "喂！\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_804():
        TurnDirection(0xD, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_804)
    TurnDirection(0xC, 0x8, 400)

    def lambda_819():

        label("loc_819")

        TurnDirection(0x8, 0xB, 0)
        OP_48()
        Jump("loc_819")

    QueueWorkItem2(0x8, 1, lambda_819)

    def lambda_82A():

        label("loc_82A")

        TurnDirection(0x101, 0xB, 0)
        OP_48()
        Jump("loc_82A")

    QueueWorkItem2(0x101, 1, lambda_82A)

    def lambda_83B():

        label("loc_83B")

        TurnDirection(0xE, 0xB, 0)
        OP_48()
        Jump("loc_83B")

    QueueWorkItem2(0xE, 1, lambda_83B)

    def lambda_84C():

        label("loc_84C")

        TurnDirection(0x105, 0xB, 0)
        OP_48()
        Jump("loc_84C")

    QueueWorkItem2(0x105, 1, lambda_84C)

    def lambda_85D():
        OP_69(0x8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_85D)
    Sleep(400)
    OP_43(0xC, 0x1, 0x1, 0x6)
    OP_43(0xD, 0x1, 0x1, 0x7)
    OP_8E(0xB, 0x0, 0x0, 0x1C3E, 0xBB8, 0x0)
    OP_44(0x8, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0x105, 0x1)
    TurnDirection(0xB, 0x8, 400)
    OP_44(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "你是这里的负责人吧！\x01",
            "快点想想办法啊！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 0x1)

    ChrTalk(
        0xD,
        "就这样任他无理取闹吗！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0x1)

    ChrTalk(
        0xC,
        "王国军不是市民的朋友吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "好歹也要做些什么吧！\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "大家、大家……\x02",
    )

    CloseMessageWindow()
    OP_8E(0xE, 0xFFFFFD58, 0x0, 0x184C, 0xBB8, 0x0)
    OP_8C(0xE, 0, 400)

    ChrTalk(
        0xE,
        "#012F大家先冷静下来……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 0)
    OP_8C(0xC, 180, 0)
    OP_8C(0xD, 180, 0)

    def lambda_A30():
        OP_6D(-840, 0, 3830, 1000)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A30)

    def lambda_A48():
        OP_94(0x1, 0xB, 0x0, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A48)

    def lambda_A5E():
        OP_94(0x1, 0xC, 0x0, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A5E)

    def lambda_A74():
        OP_94(0x1, 0xD, 0x0, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A74)
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_AAE():
        OP_94(0x1, 0xE, 0xB4, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_AAE)

    def lambda_AC4():
        OP_94(0x1, 0x8, 0xB4, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AC4)
    Sleep(200)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_AF1():
        OP_94(0x1, 0x101, 0xB4, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF1)

    ChrTalk(
        0xB,
        "你叫我们怎么冷静！\x02",
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x1, 0x8)
    OP_43(0xC, 0x1, 0x1, 0x9)
    OP_43(0xD, 0x1, 0x1, 0xA)

    ChrTalk(
        0xE,
        (
            "#014F我、我明白你们的心情，\x01",
            "能不能不要这么靠近…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F约、约修亚，没事吧！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(
        0xE,
        (
            "#012F这、这边还行……\x02\x03",
            "总之，艾丝蒂尔你们\x01",
            "快到食堂里看看情况吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 0, 400)

    ChrTalk(
        0x101,
        "#002F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#002F好了，我们走。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#043F……嗯、嗯。\x02",
    )

    CloseMessageWindow()
    OP_4B(0xE, 255)
    OP_4B(0x8, 255)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x1, 0x1, 0x8)
    OP_43(0xC, 0x1, 0x1, 0x9)
    OP_43(0xD, 0x1, 0x1, 0xA)
    SetChrFlags(0x8, 0x10)
    OP_28(0x23, 0x1, 0x1000)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_1_441 end

    def Function_2_C96(): pass

    label("Function_2_C96")

    OP_8E(0xFE, 0x0, 0x0, 0x186A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_2_C96 end

    def Function_3_CB2(): pass

    label("Function_3_CB2")

    OP_8E(0xFE, 0xFFFFF510, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0x12C0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_CB2 end

    def Function_4_CE2(): pass

    label("Function_4_CE2")

    OP_8E(0xFE, 0xFFFFF3B2, 0x0, 0x13EC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF8F8, 0x0, 0x1770, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_CE2 end

    def Function_5_D12(): pass

    label("Function_5_D12")

    OP_8E(0xFE, 0xFFFFE4DA, 0x3E8, 0x10CC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF682, 0x0, 0x10CC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_5_D12 end

    def Function_6_D42(): pass

    label("Function_6_D42")

    Sleep(800)
    OP_8E(0xC, 0x29E, 0x0, 0x1B30, 0xBB8, 0x0)
    TurnDirection(0xC, 0x8, 400)
    OP_44(0xC, 0xFF)
    Return()

    # Function_6_D42 end

    def Function_7_D67(): pass

    label("Function_7_D67")

    Sleep(600)
    OP_8E(0xD, 0xFFFFFCE0, 0x0, 0x2954, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFFCE0, 0x0, 0x1AE0, 0xBB8, 0x0)
    TurnDirection(0xD, 0x8, 400)
    OP_44(0xD, 0xFF)
    Return()

    # Function_7_D67 end

    def Function_8_DA0(): pass

    label("Function_8_DA0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DE8")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1400)
    TurnDirection(0xFE, 0x8, 400)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    TurnDirection(0xFE, 0xE, 400)
    Jump("Function_8_DA0")

    label("loc_DE8")

    Return()

    # Function_8_DA0 end

    def Function_9_DE9(): pass

    label("Function_9_DE9")

    Sleep(400)

    label("loc_DEE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E36")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1400)
    TurnDirection(0xFE, 0x8, 400)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    TurnDirection(0xFE, 0xE, 400)
    Jump("loc_DEE")

    label("loc_E36")

    Return()

    # Function_9_DE9 end

    def Function_10_E37(): pass

    label("Function_10_E37")

    Sleep(200)

    label("loc_E3C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E84")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    TurnDirection(0xFE, 0x8, 400)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1400)
    TurnDirection(0xFE, 0xE, 400)
    Jump("loc_E3C")

    label("loc_E84")

    Return()

    # Function_10_E37 end

    def Function_11_E85(): pass

    label("Function_11_E85")

    SetMapFlags(0x400000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    FadeToBright(2000, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x9, 92630, 0, 12500, 90)
    SetChrPos(0x101, 90630, 0, 10900, 90)
    SetChrPos(0x105, 89630, 0, 10900, 90)
    SetChrPos(0x10, 95380, 0, 12000, 90)
    SetChrPos(0x12, 96610, 0, 12000, 270)
    SetChrPos(0x11, 94280, 0, 11200, 90)
    OP_4A(0x12, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x0)
    OP_0D()
    OP_28(0x23, 0x1, 0x2)
    OP_28(0x23, 0x1, 0x4)

    ChrTalk(
        0x12,
        "…………所以说啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "您把招待所和食堂\x01",
            "全都包下来，\x01",
            "难道就没有为别的客人想想吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "为什么连这种事\x01",
            "您也不能做一下让步呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(
        0x11,
        (
            "#722F殿下，他说的也有道理。\x01",
            "请您稍微考虑一下吧……\x02\x03",
            "就按照预定的安排，\x01",
            "我们现在回去卢安好吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(
        0x10,
        (
            "#222F给我闭嘴，菲利普！\x01",
            "我在这里呆定了。\x02\x03",
            "#220F只有在这种地方才能和\x01",
            "艾尔·雷登的瀑布做最亲密的接触呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x12, 400)
    OP_8C(0x11, 90, 0)
    OP_62(0x12, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x12,
        "我说你啊…………\x02",
    )

    CloseMessageWindow()
    OP_43(0x12, 0x1, 0x1, 0xC)
    OP_43(0x10, 0x1, 0x1, 0xD)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x105, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x105, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x1E)
    OP_73(0x1)

    def lambda_1183():
        OP_6D(92630, 0, 11500, 2000)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1183)

    def lambda_119B():
        OP_94(0x1, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_119B)
    OP_94(0x1, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)

    def lambda_11C0():
        OP_8E(0x101, 0x169D6, 0x0, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11C0)
    WaitChrThread(0x105, 0x1)
    OP_8E(0x105, 0x169D6, 0x0, 0x2904, 0x7D0, 0x0)
    TurnDirection(0x101, 0x10, 400)
    OP_8C(0x105, 90, 400)
    OP_72(0x1, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x1, 30)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_71(0x1, 0x800)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F…………咦！\x02\x03",
            "我说是谁呢，\x01",
            "这不是任性公爵吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "…………嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哦…………\x01",
            "是游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12F9():
        TurnDirection(0x105, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12F9)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x9,
        "等你们很久了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F超级麻烦的旅行者……\x02\x03",
            "难道就是他？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "除了他还有谁。\x02",
    )

    CloseMessageWindow()

    def lambda_139C():
        OP_8C(0x105, 90, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_139C)
    TurnDirection(0x101, 0x10, 400)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F呼，伤脑筋啊…………\x02\x03",
            "其实刚才看到\x01",
            "和队长谈话的那个人，\x01",
            "就应该想到是他……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x10, 400)

    ChrTalk(
        0x9,
        (
            "那个公爵\x01",
            "说他要在这里留宿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "还放出话来说要把\x01",
            "这里的招待所和食堂全部包下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F简直就是肆无忌惮嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F呼，真是的……\x01",
            "好一个麻烦的人啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "难道就因为王族的客人要留宿，\x01",
            "就把一般的旅行者全都赶到外面\x01",
            "去风餐露宿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…………事情就是这样的，\x01",
            "希望你们能够主持公道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "无论怎样也要\x01",
            "说服公爵回卢安去。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1645():
        TurnDirection(0x105, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1645)
    TurnDirection(0x101, 0x9, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F要、要我去说服！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "和别人交涉\x01",
            "不也属于游击士的工作之一吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "而我们这些士兵\x01",
            "只受过剑和枪的训练。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F我、我也没有\x01",
            "受过与交涉相关的训练啊。\x02\x03",
            "#503F如果他之前\x01",
            "稍微教我一些秘诀之类的，\x01",
            "也许我还能胜任这种事……\x02\x03",
            "（这种事情平常\x01",
            "　都是交给约修亚的啊……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F可是艾丝蒂尔。\x01",
            "我们不能这样放任不管啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        "#505F唔………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "那就拜托了哦。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    ChrTalk(
        0x101,
        (
            "#007F唉…………\x01",
            "没得选择了。\x02\x03",
            "呼，只有硬着头皮上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哦，听你这么说\x01",
            "我就有信心了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F管他呢，乱说一气吧，\x01",
            "我可是完全没有自信啊。\x02\x03",
            "…………最好不要对我抱有希望。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F艾丝蒂尔，你一定能行的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#002F嗯、嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#582F好的，不管成功与否，\x01",
            "我尽全力就是了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    def lambda_1A42():

        label("loc_1A42")

        TurnDirection(0x9, 0x101, 0)
        OP_48()
        Jump("loc_1A42")

    QueueWorkItem2(0x9, 1, lambda_1A42)

    def lambda_1A53():

        label("loc_1A53")

        TurnDirection(0x105, 0x101, 0)
        OP_48()
        Jump("loc_1A53")

    QueueWorkItem2(0x105, 1, lambda_1A53)

    def lambda_1A64():

        label("loc_1A64")

        TurnDirection(0xA, 0x101, 0)
        OP_48()
        Jump("loc_1A64")

    QueueWorkItem2(0xA, 1, lambda_1A64)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17494), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_PUSH_LONG, 0x32C8), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1AB7():
        OP_69(0xF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1AB7)
    OP_8E(0x101, 0x16CD8, 0x0, 0x300C, 0x7D0, 0x0)
    OP_8E(0x101, 0x17494, 0x0, 0x32C8, 0x7D0, 0x0)
    TurnDirection(0x101, 0x10, 400)
    OP_44(0x9, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xA, 0xFF)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(
        0x11,
        "#721F哦？你好像之前的那位……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 400)

    ChrTalk(
        0x101,
        (
            "#506F嗯，好久不见了。\x02\x03",
            "不过一见面又有大麻烦了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10, 0xFF)
    OP_44(0x12, 0xFF)
    ClearMapFlags(0x400000)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_1BC3():
        TurnDirection(0x12, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1BC3)
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(
        0x10,
        (
            "#220F嗯？\x02\x03",
            "菲利普，你在和谁说话？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        "#002F（总、总之开始是很关键的。）\x02",
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
            "【嗨嗨～公爵大人！】\x01",                  # 0
            "【公爵大人，我来恭迎您的大驾。】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1CD9"),
        (1, "loc_238C"),
        (SWITCH_DEFAULT, "loc_2E01"),
    )


    label("loc_1CD9")

    OP_28(0x23, 0x1, 0x2000)

    ChrTalk(
        0x101,
        "#508F嗨嗨～公爵大人！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "#222F…………哼。\x02\x03",
            "竟然用那样的口气\x01",
            "来称呼即将成为国王的我……\x01",
            "真是个无知至极的家伙。\x02\x03",
            "#220F哼，算了……\x01",
            "…………有什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，\x01",
            "我是来迎接公爵您的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#223F迎接我？\x02\x03",
            "我不记得\x01",
            "下过这样的命令啊。\x02\x03",
            "究竟是从哪里来迎接的呢？\x01",
            "　\x02",
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
            "【市长官邸啊。】\x01",        # 0
            "【布朗西酒店啊。】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E9C"),
        (1, "loc_1EDC"),
        (SWITCH_DEFAULT, "loc_1F24"),
    )


    label("loc_1E9C")


    ChrTalk(
        0x101,
        (
            "#000F市长官邸啊。\x02\x03",
            "戴尔蒙市长委托我，\x01",
            "让我来迎接您回去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F24")

    label("loc_1EDC")


    ChrTalk(
        0x101,
        (
            "#000F布朗西酒店啊。\x02\x03",
            "酒店老板委托我，\x01",
            "让我来迎接您回去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F24")

    label("loc_1F24")


    ChrTalk(
        0x10,
        (
            "#220F哼，是这样啊。\x01",
            "辛苦你了。\x02\x03",
            "不过，今晚我不准备回卢安。\x02\x03",
            "我决定在艾尔·雷登留宿一晚。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F可是今晚市长官邸\x01",
            "会举办一场豪华晚宴哦。\x02\x03",
            "如果身为未来国王的您能参加，\x01",
            "大家一定会很高兴的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#220F啊啊，\x01",
            "晚宴什么时候举行都可以啊。\x02\x03",
            "我对晚宴之类的活动已经有些厌倦了。\x01",
            "今晚是绝对不会去的。\x02\x03",
            "#225F在这个关所住下来，\x01",
            "然后悠然自得地远眺瀑布，\x01",
            "更是一件有趣开心的事情。\x02\x03",
            "哈哈哈…………\x01",
            "我的情操真是高尚啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F但、但是…………\x02\x03",
            "未来的国王要在这种简陋的地方留宿，\x01",
            "是不是有些太～委屈了呢？\x01",
            "　\x02\x03",
            "而且也没有\x01",
            "豪华的料理来招待您…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#223F哦，这也有道理。\x02\x03",
            "#220F虽然你的好心让我有一些动摇……\x01",
            "　\x02\x03",
            "…………菲利普！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2285():
        TurnDirection(0x12, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2285)
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(
        0x11,
        "#720F是、是。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(
        0x10,
        (
            "#220F马上做好留宿的准备。\x02\x03",
            "和卢安的酒店联系，\x01",
            "叫他们把床给我送来这里。\x02\x03",
            "还有，不要忘记了。\x01",
            "叫他们把一流的厨师和料理也一起送来。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 15)
    Jump("loc_2E01")

    label("loc_238C")


    ChrTalk(
        0x101,
        "#500F公爵大人，我来恭迎您的大驾。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "#223F迎接我？\x02\x03",
            "我不记得\x01",
            "下过这样的命令啊。\x02\x03",
            "究竟是从哪里来迎接的呢？\x01",
            "　\x02",
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
            "【是市长官邸。】\x01",        # 0
            "【是布朗西酒店。】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24B0"),
        (1, "loc_24F0"),
        (SWITCH_DEFAULT, "loc_2538"),
    )


    label("loc_24B0")


    ChrTalk(
        0x101,
        (
            "#000F市长官邸啊。\x02\x03",
            "戴尔蒙市长委托我，\x01",
            "让我来迎接您回去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2538")

    label("loc_24F0")


    ChrTalk(
        0x101,
        (
            "#000F布朗西酒店啊。\x02\x03",
            "酒店老板委托我，\x01",
            "让我来迎接您回去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2538")

    label("loc_2538")


    ChrTalk(
        0x10,
        (
            "#220F哦，是吗。\x01",
            "办事很细心，值得称赞。\x02\x03",
            "不过，今晚我不准备回卢安。\x02\x03",
            "我决定在艾尔·雷登留宿一晚。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F（……关键的时刻到了。）\x02\x03",
            "（趁这个时候\x01",
            "　顺着他的话劝服他……）\x02",
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
            "【啊！在这样简陋的地方……】\x01",          # 0
            "【今晚市长官邸会有豪华晚宴……】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26D1"),
        (1, "loc_29F9"),
        (SWITCH_DEFAULT, "loc_2DFE"),
    )


    label("loc_26D1")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F……啊！\x01",
            "难道公爵您要在这样简陋的地方留宿？\x01",
            "　\x02\x03",
            "这个地方怎么看，\x01",
            "都和贵为未来国王的您极不相称啊……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#225F哼，\x01",
            "这种事不用你说我也很清楚。\x02\x03",
            "我本来就不觉得\x01",
            "这个地方与我相称。\x02\x03",
            "只是觉得偶尔体验一下\x01",
            "庶民生活也是很有趣的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F既然您觉得可以，那就算了……\x02\x03",
            "不过，留在这里就没有\x01",
            "豪华的料理可以款待您了。\x02\x03",
            "而且很明显…………\x01",
            "这里不太卫生啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x12,
        "（……怒。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#223F……是、是吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    ChrTalk(
        0x10,
        (
            "#222F唔、唔，经你这么一说，\x01",
            "好像这里到处都不太干净啊…………\x02\x03",
            "唔…………\x02\x03",
            "果然不能在这种地方留宿。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F（好，就差最后一步了！）\x02",
    )

    CloseMessageWindow()
    Call(1, 14)
    Jump("loc_2DFE")

    label("loc_29F9")


    ChrTalk(
        0x101,
        (
            "#000F今晚市长官邸会举办一场豪华晚宴哦。\x01",
            "　\x02\x03",
            "如果身为未来国王的您能参加，\x01",
            "大家一定会很高兴的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#220F啊啊，\x01",
            "晚宴什么时候举行都可以啊。\x02\x03",
            "我对晚宴之类的活动已经有些厌倦了。\x01",
            "今晚是绝对不会去的。\x02\x03",
            "#225F在这个关所住下来，\x01",
            "然后悠然自得地远眺瀑布，\x01",
            "更是一件有趣开心的事情。\x02\x03",
            "呵呵呵……\x01",
            "我的情操真是高尚啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F哎～可、可是……\x02\x03",
            "这个地方怎么看，\x01",
            "都和贵为未来国王的您极不相称啊……\x01",
            "　\x02\x03",
            "而且庶民吃的饭菜\x01",
            "也肯定不合您的口味啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#223F哦，这也有道理。\x02\x03",
            "#220F虽然你的好心让我有一些动摇……\x01",
            "　\x02\x03",
            "…………菲利普！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2CFC():
        TurnDirection(0x12, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2CFC)
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(
        0x11,
        "#720F是、是。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(
        0x10,
        (
            "#220F马上做好留宿的准备。\x02\x03",
            "和卢安的酒店联系，\x01",
            "叫他们把床给我送来这里。\x02\x03",
            "还有，不要忘记了。\x01",
            "叫他们把一流的厨师和料理也一起送来。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 15)
    Jump("loc_2DFE")

    label("loc_2DFE")

    Jump("loc_2E01")

    label("loc_2E01")

    ClearMapFlags(0x400000)
    EventEnd(0x0)
    SetMapFlags(0x1)
    Return()

    # Function_11_E85 end

    def Function_12_2E0E(): pass

    label("Function_12_2E0E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E31")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(4000)
    Jump("Function_12_2E0E")

    label("loc_2E31")

    Return()

    # Function_12_2E0E end

    def Function_13_2E32(): pass

    label("Function_13_2E32")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E5A")
    Sleep(2000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("Function_13_2E32")

    label("loc_2E5A")

    Return()

    # Function_13_2E32 end

    def Function_14_2E5B(): pass

    label("Function_14_2E5B")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【那我们就回卢安吧。】\x01",        # 0
            "【啊，大人的脚下是……】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EF3"),
        (1, "loc_3156"),
        (SWITCH_DEFAULT, "loc_35F2"),
    )


    label("loc_2EF3")


    ChrTalk(
        0x101,
        (
            "#006F那我们就回卢安吧。\x02\x03",
            "趁现在天色还早，快点回去吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "#223F嗯？你说什么啊？\x02\x03",
            "谁说过要回卢安啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F…………啊？\x02\x03",
            "可、可是刚才\x01",
            "您不是说这种地方不能留宿的吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#220F哼，那只是看你那么费心，\x01",
            "而随便说说罢了。\x02\x03",
            "…………菲利普！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3054():
        TurnDirection(0x12, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3054)
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(
        0x11,
        "#720F是、是。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(
        0x10,
        (
            "#220F马上做好留宿的准备。\x02\x03",
            "和卢安的酒店联系，\x01",
            "叫他们把床给我送来这里。\x02\x03",
            "还有，不要忘记了。\x01",
            "叫他们把一流的厨师和料理也一起送来。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 15)
    Jump("loc_35F2")

    label("loc_3156")

    OP_28(0x23, 0x1, 0x8)

    ChrTalk(
        0x101,
        "#004F啊，大人的脚下是……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        "#223F嗯？我的脚下怎么了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F……有一只蟑螂。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    def lambda_3223():
        TurnDirection(0x9, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3223)

    def lambda_3231():
        TurnDirection(0x105, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3231)
    TurnDirection(0x12, 0x10, 400)

    ChrTalk(
        0x10,
        (
            "#226F啊、啊呀呀呀！\x01",
            "菲、菲利～普！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#723F是、是的！\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 225, 800)
    OP_8C(0x10, 315, 800)
    OP_8C(0x10, 135, 800)

    ChrTalk(
        0x10,
        (
            "#226F呜，虫子在哪里！\x01",
            "究竟在哪里啊！\x02\x03",
            "快、快给我杀死它们～～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#507F哎～呀，\x01",
            "庶民的食堂果然不卫生啊～\x02\x03",
            "说不定哪里还会\x01",
            "冒出一只大魔兽来哦……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    ChrTalk(
        0x10,
        "#228F呀、呀啊啊！！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 0)

    ChrTalk(
        0x10,
        (
            "#226F不、不能这样！\x01",
            "菲利普，我们回去！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x11,
        (
            "#723F是、是的！\x01",
            "这就最好不过了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_342F():

        label("loc_342F")

        TurnDirection(0x12, 0x10, 0)
        OP_48()
        Jump("loc_342F")

    QueueWorkItem2(0x12, 1, lambda_342F)

    def lambda_3440():

        label("loc_3440")

        TurnDirection(0x9, 0x10, 0)
        OP_48()
        Jump("loc_3440")

    QueueWorkItem2(0x9, 1, lambda_3440)

    def lambda_3451():

        label("loc_3451")

        TurnDirection(0x101, 0x10, 0)
        OP_48()
        Jump("loc_3451")

    QueueWorkItem2(0x101, 1, lambda_3451)

    def lambda_3462():

        label("loc_3462")

        TurnDirection(0x11, 0x10, 0)
        OP_48()
        Jump("loc_3462")

    QueueWorkItem2(0x11, 1, lambda_3462)

    def lambda_3473():

        label("loc_3473")

        TurnDirection(0xA, 0x10, 0)
        OP_48()
        Jump("loc_3473")

    QueueWorkItem2(0xA, 1, lambda_3473)
    OP_8E(0x10, 0x16E04, 0x0, 0x2EE0, 0x1388, 0x0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x1E)
    OP_43(0x105, 0x1, 0x1, 0x14)
    OP_43(0x11, 0x1, 0x1, 0x15)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_34C6():
        OP_8E(0xA, 0x169A4, 0x0, 0x21FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_34C6)
    OP_8E(0x10, 0x1624C, 0x0, 0x2904, 0x1388, 0x0)
    SetChrFlags(0x10, 0x80)
    WaitChrThread(0x11, 0x1)
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(
        0x11,
        "#720F……给你们添麻烦了。\x02",
    )

    CloseMessageWindow()
    OP_73(0x1)
    OP_44(0x12, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xA, 0xFF)

    def lambda_353D():

        label("loc_353D")

        TurnDirection(0x12, 0x11, 0)
        OP_48()
        Jump("loc_353D")

    QueueWorkItem2(0x12, 1, lambda_353D)

    def lambda_354E():

        label("loc_354E")

        TurnDirection(0x9, 0x11, 0)
        OP_48()
        Jump("loc_354E")

    QueueWorkItem2(0x9, 1, lambda_354E)

    def lambda_355F():

        label("loc_355F")

        TurnDirection(0x101, 0x11, 0)
        OP_48()
        Jump("loc_355F")

    QueueWorkItem2(0x101, 1, lambda_355F)

    def lambda_3570():

        label("loc_3570")

        TurnDirection(0x105, 0x11, 0)
        OP_48()
        Jump("loc_3570")

    QueueWorkItem2(0x105, 1, lambda_3570)

    def lambda_3581():

        label("loc_3581")

        TurnDirection(0xA, 0x11, 0)
        OP_48()
        Jump("loc_3581")

    QueueWorkItem2(0xA, 1, lambda_3581)

    ChrTalk(
        0x101,
        "#001F嗯，这就可以放心了⊙\x02",
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x1624C, 0x0, 0x2904, 0x1388, 0x0)
    SetChrFlags(0x11, 0x80)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x12, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xA, 0xFF)
    NewScene("ED6_DT01/T2710   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_35F2")

    label("loc_35F2")

    Return()

    # Function_14_2E5B end

    def Function_15_35F3(): pass

    label("Function_15_35F3")

    OP_28(0x23, 0x1, 0x10)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F啊，什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#220F从现在开始，让士兵到这里集中，\x01",
            "做食堂的大扫除。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#722F大人，这是不是有点……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#224F给我闭嘴，菲利普！\x02\x03",
            "作为未来国王的我要在这里留宿！\x01",
            "　\x02\x03",
            "做准备是理所当然的！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#002F请您不要太过分了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        "#222F唔……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F你可不要敬酒不吃吃罚酒……\x01",
            "　\x02\x03",
            "没有菲利普先生在，\x01",
            "你根本就什么也做不了！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_38A7")
    OP_62(0x105, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#045F（哎呀，艾丝蒂尔发怒了……）\x02\x03",
            "（都说出这种话来了……）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D9")

    label("loc_38A7")

    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x105,
        "#044F艾、艾丝蒂尔！？\x02",
    )

    CloseMessageWindow()

    label("loc_38D9")


    ChrTalk(
        0x10,
        (
            "#222F可恶……\x01",
            "你、你不知道就不要乱说。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x9, 400)

    ChrTalk(
        0x10,
        (
            "#224F喂、喂，那边的士兵！\x01",
            "给我行动起来！\x02\x03",
            "快把这个家伙给我赶出去！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#582F要赶出去的……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 1000)
    OP_8C(0x101, 315, 1000)
    OP_8C(0x101, 180, 1000)
    SetChrChipByIndex(0x101, 9)

    ChrTalk(
        0x101,
        "#005F是你啊！\x02",
    )

    CloseMessageWindow()

    def lambda_39D9():
        TurnDirection(0x12, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_39D9)
    TurnDirection(0x10, 0x101, 0)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(400)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3AAB():
        OP_94(0x1, 0x10, 0xB4, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3AAB)
    WaitChrThread(0x10, 0x1)

    ChrTalk(
        0x10,
        "#226F啊啊，好可怕啊！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F啊，艾丝蒂尔！不行！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F喝啊～～～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3B2F():

        label("loc_3B2F")

        TurnDirection(0x9, 0x101, 0)
        OP_48()
        Jump("loc_3B2F")

    QueueWorkItem2(0x9, 1, lambda_3B2F)

    def lambda_3B40():

        label("loc_3B40")

        TurnDirection(0xA, 0x101, 0)
        OP_48()
        Jump("loc_3B40")

    QueueWorkItem2(0xA, 1, lambda_3B40)
    OP_43(0x10, 0x1, 0x1, 0x10)
    OP_43(0x11, 0x2, 0x1, 0x11)
    OP_43(0x101, 0x1, 0x1, 0x12)
    OP_43(0x105, 0x1, 0x1, 0x13)

    def lambda_3B6D():

        label("loc_3B6D")

        TurnDirection(0x12, 0x10, 0)
        OP_48()
        Jump("loc_3B6D")

    QueueWorkItem2(0x12, 1, lambda_3B6D)

    def lambda_3B7E():

        label("loc_3B7E")

        TurnDirection(0x11, 0x10, 0)
        OP_48()
        Jump("loc_3B7E")

    QueueWorkItem2(0x11, 1, lambda_3B7E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x12, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0xE, 0x80)
    Sleep(1000)
    FadeToBright(2000, 0)
    SetChrPos(0x10, 95380, 0, 12000, 90)
    SetChrPos(0x11, 94280, 0, 11200, 90)
    SetChrPos(0x101, 92630, 0, 13400, 135)
    SetChrPos(0xA, 93400, 0, 13300, 315)
    SetChrPos(0x9, 92710, 0, 12520, 0)
    SetChrPos(0x12, 93420, 0, 12620, 315)
    SetChrPos(0xE, 96610, 0, 12500, 270)
    SetChrPos(0x105, 96610, 0, 11500, 270)
    OP_44(0xE, 0xFF)
    OP_43(0x101, 0x1, 0x1, 0x16)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x10,
        (
            "#220F……呼，如果是这样，\x01",
            "那就没办法了。\x02\x03",
            "呵哈哈，\x01",
            "想怎么做就怎么做，怎么做都行。\x02\x03",
            "菲利普，\x01",
            "我们回卢安吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#720F好、好的！\x01",
            "这就最好不过了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D0A():

        label("loc_3D0A")

        TurnDirection(0x101, 0x10, 0)
        OP_48()
        Jump("loc_3D0A")

    QueueWorkItem2(0x101, 3, lambda_3D0A)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    OP_8E(0x10, 0x16E04, 0x0, 0x2EE0, 0xBB8, 0x0)
    OP_8E(0x10, 0x169B8, 0x0, 0x2A94, 0xBB8, 0x0)
    OP_43(0x11, 0x1, 0x1, 0x15)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_8E(0x10, 0x1624C, 0x0, 0x2A94, 0xBB8, 0x0)
    SetChrFlags(0x10, 0x8)
    TurnDirection(0x11, 0xE, 400)

    ChrTalk(
        0x11,
        "#720F……给你们添麻烦了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x11, 400)

    ChrTalk(
        0xE,
        (
            "#015F这话该我们说才是，\x01",
            "刚才非常抱歉。\x02\x03",
            "还好公爵没有受伤。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x105, 400)

    ChrTalk(
        0x11,
        (
            "#720F多亏了这位小姐。\x02\x03",
            "差一点就闹到不可收拾了，\x01",
            "幸好她及时阻止住了大人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "菲利普！\x01",
            "你还在做什么！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#720F那我就告辞了。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x1624C, 0x0, 0x2A94, 0x1388, 0x0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_72(0x1, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x1, 30)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_71(0x1, 0x800)

    ChrTalk(
        0xE,
        (
            "#017F……………………\x02\x03",
            "呼……终于……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F哈…………\x01",
            "已经回去了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x101, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrFlags(0xE, 0x80)
    NewScene("ED6_DT01/T2710   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_15_35F3 end

    def Function_16_3F8D(): pass

    label("Function_16_3F8D")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x172B4, 0x0, 0x1FA4, 0x7D0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_16_3F8D end

    def Function_17_3FCD(): pass

    label("Function_17_3FCD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FF0")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Jump("Function_17_3FCD")

    label("loc_3FF0")

    Return()

    # Function_17_3FCD end

    def Function_18_3FF1(): pass

    label("Function_18_3FF1")

    SetChrChipByIndex(0x101, 10)
    OP_8E(0xFE, 0x172B4, 0x0, 0x251C, 0x7D0, 0x0)
    Return()

    # Function_18_3FF1 end

    def Function_19_400B(): pass

    label("Function_19_400B")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x16F94, 0x0, 0x2828, 0xBB8, 0x0)
    OP_8E(0xFE, 0x17318, 0x0, 0x22B0, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_19_400B end

    def Function_20_404D(): pass

    label("Function_20_404D")

    OP_8C(0xFE, 0, 400)
    OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)

    def lambda_4069():

        label("loc_4069")

        TurnDirection(0x105, 0x10, 0)
        OP_48()
        Jump("loc_4069")

    QueueWorkItem2(0x105, 2, lambda_4069)
    Return()

    # Function_20_404D end

    def Function_21_4075(): pass

    label("Function_21_4075")

    OP_8C(0xFE, 270, 400)
    OP_94(0x1, 0xFE, 0x0, 0x64, 0x7D0, 0x0)
    Sleep(1000)
    Return()

    # Function_21_4075 end

    def Function_22_4091(): pass

    label("Function_22_4091")

    OP_43(0xFE, 0x0, 0x0, 0x2)
    OP_4B(0x9, 255)
    OP_4B(0x12, 255)
    OP_4B(0xA, 255)

    label("loc_40A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4209")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_40FB():
        OP_94(0x1, 0xFE, 0x0, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40FB)
    Sleep(200)

    def lambda_4116():
        OP_94(0x1, 0xFE, 0xB4, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4116)

    def lambda_412C():
        OP_94(0x1, 0xFE, 0xB4, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_412C)
    Sleep(200)

    def lambda_4147():
        OP_94(0x1, 0x12, 0xB4, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4147)
    Sleep(2000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_41AA():
        OP_94(0x1, 0xFE, 0xB4, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_41AA)

    def lambda_41C0():
        OP_94(0x1, 0xFE, 0xB4, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_41C0)

    def lambda_41D6():
        OP_94(0x1, 0x12, 0xB4, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_41D6)
    Sleep(200)

    def lambda_41F1():
        OP_94(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41F1)
    Sleep(2000)
    Jump("loc_40A4")

    label("loc_4209")

    Return()

    # Function_22_4091 end

    def Function_23_420A(): pass

    label("Function_23_420A")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xB, -770, 0, 21500, 0)
    SetChrPos(0xC, -770, 0, 22500, 0)
    SetChrPos(0xD, -770, 0, 23500, 0)
    SetChrPos(0x101, -1000, 0, 9300, 180)
    SetChrPos(0x105, 0, 0, 9300, 180)
    SetChrPos(0x102, -1800, 0, 7800, 90)
    SetChrPos(0x8, 0, 0, 6500, 0)
    SetChrPos(0x9, -1000, 0, 5500, 0)
    SetChrPos(0x12, -2000, 0, 6500, 90)
    SetChrPos(0xA, -4800, 0, 7900, 90)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0x12, 255)
    OP_4A(0xA, 255)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "……就是这样，\x01",
            "这位小姑娘一句话就把他摆平了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "说那家伙的脚下\x01",
            "有一只蟑螂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "一听到这句话，\x01",
            "那家伙的脸色都吓白了……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呀～\x01",
            "好久都没有这么痛快过了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "唔，是这样啊。\x01",
            "听到你们所说的我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我开始还有些担心\x01",
            "你们会用强制性的手段呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从基恩茨的话来看，\x01",
            "你们处理得非常好啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(
        0x12,
        (
            "刚才我听你说了些食堂的坏话，\x01",
            "确实还很生气呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F啊、啊哈哈，真是不好意思呢。\x02\x03",
            "为了让公爵动摇，\x01",
            "只有说些谎话了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#011F不过很让我意外哦。\x02\x03",
            "艾丝蒂尔竟然可以处理得那么恰当。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿，我可是在关键时刻\x01",
            "就能发挥出真正的实力。\x02\x03",
            "嗯，说实话，\x01",
            "刚才我是以约修亚的方式\x01",
            "来劝说公爵的哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#040F呵呵，原来是这样啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#001F嗯，是呀，\x01",
            "我才不会像那样说谎吓人呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(
        0x102,
        "#018F……………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x102)

    ChrTalk(
        0x9,
        (
            "哈哈哈，\x01",
            "谎话也是分很多种的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果是为了帮助大家，\x01",
            "相信女神也是会允许的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嗯，今天多谢你们的帮助。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以后的工作\x01",
            "也多多加油吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47FD():
        TurnDirection(0x105, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_47FD)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#006F嗯，那么就再见了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        "#010F告辞了。\x02",
    )

    CloseMessageWindow()
    OP_2B(0x23, 0x2)
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【说服旅行者】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0x12, 255)
    OP_4B(0xA, 255)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x105, 0x40)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x11, 0x40)
    NewScene("ED6_DT01/T2700   ._SN", 101, 0, 0)
    IdleLoop()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_23_420A end

    def Function_24_48FD(): pass

    label("Function_24_48FD")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xB, -770, 0, 21500, 0)
    SetChrPos(0xC, -770, 0, 22500, 0)
    SetChrPos(0xD, -770, 0, 23500, 0)
    SetChrPos(0x101, -1000, 0, 9300, 180)
    SetChrPos(0x105, 0, 0, 9300, 180)
    SetChrPos(0x102, -1800, 0, 7800, 90)
    SetChrPos(0x8, 0, 0, 6500, 0)
    SetChrPos(0x9, -1000, 0, 5500, 0)
    SetChrPos(0x12, -2000, 0, 6500, 90)
    SetChrPos(0xA, -4800, 0, 7900, 90)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0x12, 255)
    OP_4A(0xA, 255)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "……就是这样，\x01",
            "这位小姑娘的确很干脆啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那家伙不讲道理的时候，\x01",
            "就把棒子向他挥去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "一看到这种情况，\x01",
            "那家伙的脸色都吓白了……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "结果呢，靠小姑娘一个人\x01",
            "就成功地赶走了那家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "唔，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我刚才听到打架的声音\x01",
            "还担心了半天……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "喂，\x01",
            "真的没有把他打伤吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x8, 400)

    ChrTalk(
        0x12,
        "嗯，一点事也没有。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F唉，我真丢脸……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        "#017F真是不好意思。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "哪里，\x01",
            "这件事的起因是\x01",
            "公爵大人的任性胡为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们没有必要\x01",
            "为此道歉或负责。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4CE2():
        TurnDirection(0x12, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4CE2)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "不过，今后不到万不得已，\x01",
            "还是不要动手为好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯……\x01",
            "我会牢记在心的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#003F谢谢队长。\x01",
            "还有科洛丝，你们及时阻止了我。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#040F没事的，不要那么介意嘛。\x02\x03",
            "虽然使用暴力的确不太好……\x01",
            "不过这也和公爵大人的态度有关。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "方法虽然有些问题，\x01",
            "不过最后还是帮助了那些普通的旅行者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我代表他们\x01",
            "向你们表达感谢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#000F……嗯，谢谢您。\x02\x03",
            "#001F嘿嘿，太好了。\x02\x03",
            "听了你们的话，\x01",
            "我觉得又精神起来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018F真是的，\x01",
            "转变得可真快啊……\x02\x03",
            "#017F算了，\x01",
            "这也算是艾丝蒂尔的一个优点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#041F嘻嘻…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不管怎么说，\x01",
            "今天真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以后的工作\x01",
            "也多多加油吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，那么就再见了。\x02",
    )

    CloseMessageWindow()

    def lambda_5045():
        TurnDirection(0x105, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5045)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        "#010F告辞了。\x02",
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
            "任务【说服旅行者】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0x12, 255)
    OP_4B(0xA, 255)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x105, 0x40)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x11, 0x40)
    NewScene("ED6_DT01/T2700   ._SN", 101, 0, 0)
    IdleLoop()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_24_48FD end

    def Function_25_5120(): pass

    label("Function_25_5120")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51A1")
    EventBegin(0x1)
    OP_4A(0xE, 255)
    TurnDirection(0xE, 0x101, 0)

    ChrTalk(
        0xE,
        (
            "#012F艾丝蒂尔，\x01",
            "赶快去食堂看看情况吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    OP_8C(0xE, 0, 0)
    OP_4B(0xE, 255)
    Sleep(50)
    EventEnd(0x4)

    label("loc_51A1")

    Return()

    # Function_25_5120 end

    SaveToFile()

Try(main)
