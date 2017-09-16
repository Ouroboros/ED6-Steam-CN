from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3230   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3230.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '提妲',                                 # 9
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


    AddCharChip(
        'ED6_DT07/CH00060 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH00060P._CP',             # 00
    )

    DeclNpc(
        X                   = 160,
        Z                   = 250,
        Y                   = 8840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_130",          # 01, 1
        "Function_2_157",          # 02, 2
        "Function_3_16D",          # 03, 3
        "Function_4_260",          # 04, 4
        "Function_5_2B8",          # 05, 5
        "Function_6_97D",          # 06, 6
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_DE"),
        (SWITCH_DEFAULT, "loc_106"),
    )


    label("loc_DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE")
    Event(0, 5)

    label("loc_EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_103")

    Jump("loc_106")

    label("loc_106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F")
    SetChrPos(0x8, 160, 250, 8840, 0)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x3)

    label("loc_12F")

    Return()

    # Function_0_D2 end

    def Function_1_130(): pass

    label("Function_1_130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_148")
    OP_B1("t3230_y")
    Jump("loc_151")

    label("loc_148")

    OP_B1("t3230_n")

    label("loc_151")

    OP_22(0xA1, 0x1, 0x64)
    Return()

    # Function_1_130 end

    def Function_2_157(): pass

    label("Function_2_157")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_157")

    label("loc_16C")

    Return()

    # Function_2_157 end

    def Function_3_16D(): pass

    label("Function_3_16D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25F")
    OP_8E(0xFE, 0xFFFFFABA, 0xFA, 0x1ED2, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 300)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFFA9C, 0xFA, 0x1A0E, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 300)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)
    OP_8E(0xFE, 0x9C4, 0x0, 0x1612, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 300)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    OP_8E(0xFE, 0x226, 0xFA, 0x1946, 0xDAC, 0x0)
    OP_8E(0xFE, 0xA0, 0xFA, 0x2288, 0xDAC, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_62(0x8, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)
    Jump("Function_3_16D")

    label("loc_25F")

    Return()

    # Function_3_16D end

    def Function_4_260(): pass

    label("Function_4_260")

    TalkBegin(0xFE)

    ChrTalk(
        0x8,
        "#560F嘿咻嘿咻……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_260 end

    def Function_5_2B8(): pass

    label("Function_5_2B8")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(-1060, 250, 8880, 0)
    RemoveParty(0x6, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -150, 0, 2440, 0)
    SetChrPos(0x101, -740, 0, 1150, 0)
    SetChrPos(0x102, 500, 0, 690, 0)
    OP_4A(0x8, 255)
    FadeToBright(1000, 0)
    OP_6D(-1090, 0, 2630, 3000)

    ChrTalk(
        0x101,
        "#501F哎～这个就是导力泵装置啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F完全看不出是很旧的东西，\x01",
            "保养得很干净啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x8,
        (
            "#067F#2P嘿嘿……\x01",
            "那是因为爷爷每年\x01",
            "都来这里对水泵进行维修啊。\x02\x03",
            "#060F４０年前，\x01",
            "导力器还没完全普及……\x02\x03",
            "为了让大家知道导力器的便利性，\x01",
            "就制造了这个东西出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F原来是这样啊……\x01",
            "所以也就非常有纪念意义对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F这些事情，\x01",
            "等修理好了再慢慢聊吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#061F#2P好的～！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    def lambda_58F():
        OP_6D(-320, 250, 8880, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_58F)

    def lambda_5A7():

        label("loc_5A7")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5A7")

    QueueWorkItem2(0x101, 2, lambda_5A7)

    def lambda_5B8():

        label("loc_5B8")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5B8")

    QueueWorkItem2(0x102, 2, lambda_5B8)

    def lambda_5C9():
        OP_8E(0xFE, 0x4B0, 0xFA, 0x1E64, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C9)
    Sleep(1000)

    def lambda_5E9():
        OP_8E(0xFE, 0xFFFFFF56, 0x0, 0x1342, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E9)
    Sleep(500)

    def lambda_609():
        OP_8E(0xFE, 0x4EC, 0x0, 0x1144, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_609)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 90, 400)

    ChrTalk(
        0x8,
        (
            "#064F唔……\x01",
            "首先要检查一下引擎部件……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x262, 0xFA, 0x2274, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)

    ChrTalk(
        0x8,
        (
            "#062F如果没问题的话，\x01",
            "就开始检查推进器和配管……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFFAD8, 0xFA, 0x1F18, 0xBB8, 0x0)
    OP_8C(0x8, 270, 400)

    ChrTalk(
        0x101,
        (
            "#501F啊，提妲。\x01",
            "有需要的话我们也可以帮忙……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "#560F啊，没关系呢。\x01",
            "我自己一个人就可以了。\x02\x03",
            "艾丝蒂尔姐姐，\x01",
            "你们先去旅馆休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    ChrTalk(
        0x8,
        (
            "#064F考虑到气穴现象和\x01",
            "水击作用的可能性……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFF9F2, 0xFA, 0x18EC, 0xBB8, 0x0)
    OP_8C(0x8, 270, 400)

    ChrTalk(
        0x8,
        (
            "#063F#1P嗯，还有还有……\x02\x03",
            "#065F#1P啊，脉冲器也有问题！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    def lambda_87E():
        OP_6D(-490, 0, 6860, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_87E)
    OP_8E(0x8, 0xA0, 0xFA, 0x2288, 0xFA0, 0x0)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(
        0x101,
        (
            "#506F看来就算我们呆在这里，\x01",
            "也完全帮不上什么忙啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，是啊。\x02\x03",
            "还是先听提妲的，\x01",
            "我们回旅馆等一会吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_4B(0x8, 255)
    OP_A2(0x51F)
    OP_28(0x40, 0x1, 0x10)
    OP_28(0x28, 0x4, 0x40)
    OP_28(0x29, 0x4, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_960")
    OP_28(0x2A, 0x4, 0x40)

    label("loc_960")

    OP_28(0x2C, 0x4, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_975")
    OP_28(0x31, 0x4, 0x40)

    label("loc_975")

    OP_28(0x32, 0x4, 0x40)
    EventEnd(0x0)
    Return()

    # Function_5_2B8 end

    def Function_6_97D(): pass

    label("Function_6_97D")

    EventBegin(0x0)
    OP_44(0x8, 0xFF)
    ClearMapFlags(0x1)
    OP_6D(-10, 250, 8880, 0)
    SetChrFlags(0x8, 0x80)
    AddParty(0x6, 0xFF)
    SetChrPos(0x107, 160, 250, 8840, 0)
    SetChrPos(0x101, -490, 0, 870, 0)
    SetChrPos(0x102, 670, 0, 620, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x107,
        "#063F…………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_9F7():
        OP_8E(0xFE, 0xFFFFFE02, 0x0, 0x13CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F7)
    Sleep(500)

    def lambda_A17():
        OP_8E(0xFE, 0x276, 0x0, 0x1298, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A17)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x107, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x107, 400)

    ChrTalk(
        0x101,
        (
            "#501F提妲，\x01",
            "修理已经完成了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x107, 180, 800)

    ChrTalk(
        0x107,
        (
            "#064F#2P啊……\x01",
            "艾丝蒂尔姐姐、约修亚哥哥。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AC5():
        OP_6D(-80, 250, 7500, 1500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AC5)
    OP_8E(0x107, 0x96, 0xFA, 0x190A, 0x7D0, 0x0)
    WaitChrThread(0x107, 0x1)

    ChrTalk(
        0x107,
        (
            "#067F#2P嘿嘿……\x01",
            "刚刚才完成了呢。\x02\x03",
            "不过还没有确认\x01",
            "热水是不是运送过去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F没问题了，\x01",
            "广场井里的热水都满满的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F故障是什么原因造成的呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F#2P那个啊……\x01",
            "其实水泵的装置本身\x01",
            "并没有什么太大的问题……\x02\x03",
            "不过回旋螺丝上的曲柄轴\x01",
            "锈蚀折断了。\x02\x03",
            "我换了个防锈的零件，\x01",
            "已经没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F是吗，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F那我们就回旅馆，\x01",
            "把小屋的钥匙还给老板娘吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F#2P好的。\x02",
    )

    CloseMessageWindow()
    ClearMapFlags(0x10000000)
    OP_A2(0x524)
    OP_28(0x40, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_6_97D end

    SaveToFile()

Try(main)
