from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4241   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4241.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '艾莉茜雅女王',                         # 9
        '尤莉亚中尉',                           # 10
        '约修亚',                               # 11
        '奥利维尔',                             # 12
        '金',                                   # 13
        '阿加特',                               # 14
        '提妲',                                 # 15
        '拉赛尔博士',                           # 16
        '亲卫队员',                             # 17
        '导力梯',                               # 18
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
        'ED6_DT07/CH02010 ._CH',             # 00
        'ED6_DT07/CH02090 ._CH',             # 01
        'ED6_DT07/CH00010 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00070 ._CH',             # 04
        'ED6_DT06/CH20053 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT07/CH02020 ._CH',             # 07
        'ED6_DT07/CH01320 ._CH',             # 08
        'ED6_DT06/CH20141 ._CH',             # 09
        'ED6_DT07/CH00061 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02010P._CP',             # 00
        'ED6_DT07/CH02090P._CP',             # 01
        'ED6_DT07/CH00010P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00070P._CP',             # 04
        'ED6_DT06/CH20053P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT07/CH02020P._CP',             # 07
        'ED6_DT07/CH01320P._CP',             # 08
        'ED6_DT06/CH20141P._CP',             # 09
        'ED6_DT07/CH00061P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_253",          # 01, 1
        "Function_2_278",          # 02, 2
    )


    def Function_0_242(): pass

    label("Function_0_242")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 2)
    Return()

    # Function_0_242 end

    def Function_1_253(): pass

    label("Function_1_253")

    OP_A1(0x11, 0x2)
    SetChrPos(0x11, 0, 0, 0, 0)
    SetChrFlags(0x11, 0x4)
    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_253 end

    def Function_2_278(): pass

    label("Function_2_278")

    EventBegin(0x0)
    OP_6D(-10, 0, -72410, 0)
    OP_67(0, 7490, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(45000, 0)
    OP_6E(536, 0)
    SetChrPos(0x101, -1190, 0, -72040, 0)
    SetChrPos(0x105, -1330, 0, -73970, 0)
    SetChrPos(0x103, -30, 0, -72830, 0)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x105, 0x40)
    SetChrFlags(0x103, 0x40)
    SetChrPos(0x8, 80, 0, -70380, 0)
    SetChrPos(0x9, 890, 0, -71230, 0)
    SetChrPos(0xA, -2230, 0, -70590, 0)
    SetChrPos(0xB, 640, 0, -73900, 0)
    SetChrPos(0xC, 2070, 0, -73010, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    def lambda_386():
        OP_8E(0xFE, 0xFFFFFA24, 0x0, 0xFFFEF502, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_386)

    def lambda_3A1():
        OP_8E(0xFE, 0xFFFFFBD2, 0x0, 0xFFFEEF94, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A1)

    def lambda_3BC():
        OP_8E(0xFE, 0x1A4, 0x0, 0xFFFEF390, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3BC)

    def lambda_3D7():
        OP_8E(0xFE, 0x50, 0x0, 0xFFFEF8CC, 0x578, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D7)

    def lambda_3F2():
        OP_8E(0xFE, 0x488, 0x0, 0xFFFEF7A0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3F2)

    def lambda_40D():
        OP_8E(0xFE, 0xFFFFF74A, 0x0, 0xFFFEF7FA, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_40D)

    def lambda_428():
        OP_8E(0xFE, 0x280, 0x0, 0xFFFEEEFE, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_428)

    def lambda_443():
        OP_8E(0xFE, 0x816, 0x0, 0xFFFEF1D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_443)

    def lambda_45E():
        OP_6D(110, 0, -66230, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_45E)
    FadeToBright(1000, 0)
    WaitChrThread(0x0, 0x2)
    Fade(500)
    OP_6D(110, 0, -66230, 0)
    OP_67(0, 7490, -10000, 0)
    OP_6B(1470, 0)
    OP_6C(45000, 0)
    OP_6E(536, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#173F#2P这种地方居然有一部导力梯……\x01",
            "　\x02\x03",
            "#177F以前是绝对没有的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#072F这东西是上校特意建造的吧……\x01",
            "　\x02\x03",
            "如此说来，乘坐这个导力梯应该就可以\x01",
            "降落到封印『辉之环』的地方吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#093F嗯……\x02\x03",
            "#094F也许，这正是理查德上校\x01",
            "发动这次政变背后所隐藏的真正原因。\x01",
            "　\x02\x03",
            "也只有控制了王城之后，\x01",
            "才能达到他们建造出这东西的目的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F竟然、竟然会是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#035F呵呵，可能就是如此。\x02\x03",
            "#030F无论是什么国家，\x01",
            "由王权守护的圣域都是不可侵犯的。\x02\x03",
            "如果想要打破这一点，\x01",
            "就必须下决心使出强硬的手段才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#012F不管怎样，想要降落到地下，\x01",
            "就必须要使用这个导力梯。\x02\x03",
            "先把它启动了再说。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A5():
        OP_6D(-40, 0, -62650, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_7A5)
    OP_8E(0xA, 0xFFFFFC68, 0x0, 0xFFFEFCAA, 0xBB8, 0x0)
    OP_8E(0xA, 0xFFFFFDDA, 0x3C, 0xFFFEFE4E, 0xBB8, 0x0)
    OP_8E(0xA, 0xA, 0x64, 0xFFFF10B4, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚开始调查导力梯的控电盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xA)

    ChrTalk(
        0xA,
        "#014F#5P#4S！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F怎么了啊，约修亚？\x02",
    )

    CloseMessageWindow()

    def lambda_8C2():
        OP_6D(110, 0, -66230, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8C2)
    TurnDirection(0xA, 0x101, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0xA,
        (
            "#012F这个东西……\x01",
            "用导力的加密方式锁住了。\x02\x03",
            "没有由特殊结晶回路组成的钥匙，\x01",
            "是不能将导力梯启动的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_976():
        OP_8E(0xFE, 0xFFFFFF60, 0x0, 0xFFFF01E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_976)

    ChrTalk(
        0x101,
        "#005F岂、岂有此理～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F怎么会这样，都到了这里了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "#177F#2P把拘捕到的特务兵绑过来问话！\x01",
            "　\x02\x03",
            "钥匙一定是藏在某个地方了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#093F嗯……\x01",
            "看来只有这个办法了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 20, 0, -77690, 0)
    SetChrPos(0xE, 20, 0, -77690, 0)
    SetChrPos(0xF, -1020, 0, -74230, 0)

    def lambda_AD9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_AD9)

    NpcTalk(
        0xF,
        "老人的声音",
        "#1P不，还没有到那种地步。\x02",
    )

    CloseMessageWindow()

    def lambda_B20():
        OP_6D(-550, 0, -69950, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B20)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_B66():

        label("loc_B66")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_B66")

    QueueWorkItem2(0x101, 1, lambda_B66)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_BAA():

        label("loc_BAA")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_BAA")

    QueueWorkItem2(0x105, 1, lambda_BAA)

    def lambda_BBB():

        label("loc_BBB")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_BBB")

    QueueWorkItem2(0x103, 1, lambda_BBB)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_BFF():

        label("loc_BFF")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_BFF")

    QueueWorkItem2(0x8, 1, lambda_BFF)

    def lambda_C10():

        label("loc_C10")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_C10")

    QueueWorkItem2(0x9, 1, lambda_C10)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_C54():

        label("loc_C54")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_C54")

    QueueWorkItem2(0xB, 1, lambda_C54)

    def lambda_C65():

        label("loc_C65")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_C65")

    QueueWorkItem2(0xC, 1, lambda_C65)
    WaitChrThread(0x0, 0x2)

    ChrTalk(
        0x101,
        "#004F咦……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#014F难道是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#097F哦……是拉赛尔博士！？\x02",
    )

    CloseMessageWindow()

    def lambda_CC7():
        OP_6D(-400, 0, -68560, 2500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_CC7)

    def lambda_CDF():
        OP_8E(0xFE, 0xFFFFFD4E, 0x0, 0xFFFEE9EA, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_CDF)
    Sleep(200)
    SetChrFlags(0xA, 0x4)

    def lambda_D04():
        OP_8E(0xFE, 0xFFFFF484, 0x0, 0xFFFEF502, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D04)

    def lambda_D1F():

        label("loc_D1F")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_D1F")

    QueueWorkItem2(0xA, 1, lambda_D1F)
    WaitChrThread(0x0, 0x2)

    ChrTalk(
        0xF,
        (
            "#101F艾莉茜雅。久疏问候了啊。\x01",
            "　\x02\x03",
            "哈哈……一阵子没见，\x01",
            "艾丝蒂尔和约修亚看来也很精神嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#5P等、等一下……\x01",
            "为什么博士会在这里？\x02\x03",
            "不是在被情报部追捕中吗。\x01",
            "应该还没有逃出蔡斯地区才对啊……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E1B():

        label("loc_E1B")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_E1B")

    QueueWorkItem2(0xA, 1, lambda_E1B)

    ChrTalk(
        0xA,
        (
            "#014F#5P能平安无事已经是最好了，\x01",
            "不过，既然博士都到这里来的话……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xE, -900, 0, -77820, 0)

    NpcTalk(
        0xE,
        "小姑娘的声音",
        (
            "#1P爷爷、爷爷啊。\x01",
            "您跑到哪里去了呢！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EA9():
        OP_6D(-20, 0, -71810, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EA9)
    OP_44(0xA, 0xFF)
    OP_8C(0xA, 180, 400)
    Sleep(100)

    def lambda_ED1():

        label("loc_ED1")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_ED1")

    QueueWorkItem2(0x101, 1, lambda_ED1)
    Sleep(50)

    def lambda_EE7():

        label("loc_EE7")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_EE7")

    QueueWorkItem2(0x105, 1, lambda_EE7)

    def lambda_EF8():

        label("loc_EF8")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_EF8")

    QueueWorkItem2(0x103, 1, lambda_EF8)
    Sleep(50)

    def lambda_F0E():

        label("loc_F0E")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_F0E")

    QueueWorkItem2(0x8, 1, lambda_F0E)

    def lambda_F1F():

        label("loc_F1F")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_F1F")

    QueueWorkItem2(0x9, 1, lambda_F1F)
    Sleep(50)

    def lambda_F35():

        label("loc_F35")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_F35")

    QueueWorkItem2(0xB, 1, lambda_F35)

    def lambda_F46():

        label("loc_F46")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_F46")

    QueueWorkItem2(0xC, 1, lambda_F46)

    def lambda_F57():

        label("loc_F57")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_F57")

    QueueWorkItem2(0xF, 1, lambda_F57)
    WaitChrThread(0x101, 0x2)
    SetChrPos(0xD, 360, 0, -77890, 0)

    NpcTalk(
        0xD,
        "青年的声音",
        (
            "#1P喂，我说你这个小不点，\x01",
            "别老在我面前窜来窜去好不好。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "青年的声音",
        (
            "#1P真是的，和老爷子是同种性格，\x01",
            "都属于静不下来的类型。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "小姑娘的声音",
        "#1P可、可是阿加特大哥哥……\x02",
    )

    CloseMessageWindow()

    def lambda_1040():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1040)

    def lambda_1052():
        OP_8E(0xFE, 0xFFFFFBA0, 0x0, 0xFFFEDC16, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1052)
    Sleep(600)

    def lambda_1072():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1072)

    def lambda_1084():
        OP_8E(0xFE, 0xE6, 0x0, 0xFFFEDB30, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1084)
    OP_31(0x5, 0x0, 0x22)
    OP_B5(0x5, 0x0)
    OP_B5(0x5, 0x1)
    OP_B5(0x5, 0x2)
    OP_B5(0x5, 0x3)
    OP_B5(0x5, 0x5)
    OP_B5(0x5, 0x4)
    OP_41(0x5, 0x9A)
    OP_41(0x5, 0xF6)
    OP_41(0x5, 0x114)
    OP_41(0x5, 0x260, 0x0)
    OP_41(0x5, 0x259, 0x1)
    OP_41(0x5, 0x262, 0x2)
    OP_41(0x5, 0x26E, 0x3)
    OP_41(0x5, 0x283, 0x5)
    OP_35(0x5, 0xC8)
    OP_35(0x5, 0xC9)
    OP_35(0x5, 0xCA)
    OP_35(0x5, 0xCB)
    OP_36(0x5, 0xFF)
    OP_36(0x5, 0x100)
    OP_31(0x6, 0x0, 0x20)
    OP_B5(0x6, 0x0)
    OP_B5(0x6, 0x1)
    OP_B5(0x6, 0x5)
    OP_B5(0x6, 0x4)
    OP_B5(0x6, 0x3)
    OP_B5(0x6, 0x2)
    OP_41(0x6, 0xB8)
    OP_41(0x6, 0xF6)
    OP_41(0x6, 0x114)
    OP_41(0x6, 0x2C9, 0x0)
    OP_41(0x6, 0x281, 0x1)
    OP_41(0x6, 0x25F, 0x5)
    OP_41(0x6, 0x26C, 0x4)
    OP_41(0x6, 0x271, 0x3)
    OP_41(0x6, 0x259, 0x2)
    OP_35(0x6, 0xD2)
    OP_35(0x6, 0xD3)
    OP_36(0x6, 0x104)
    WaitChrThread(0xE, 0x2)

    ChrTalk(
        0xE,
        "#064F啊……！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)

    ChrTalk(
        0x101,
        "#004F提妲！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#010F果然……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#067F艾丝蒂尔姐姐！\x01",
            "还有约修亚哥哥！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 10)

    def lambda_11AE():
        OP_8E(0xFE, 0xFFFFF79A, 0x0, 0xFFFEED32, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_11AE)

    def lambda_11C9():

        label("loc_11C9")

        OP_8C(0xFE, 0, 0)
        OP_48()
        Jump("loc_11C9")

    QueueWorkItem2(0xE, 1, lambda_11C9)

    def lambda_11DA():
        OP_8E(0xFE, 0xFFFFF880, 0x0, 0xFFFEE9AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_11DA)

    def lambda_11F5():

        label("loc_11F5")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_11F5")

    QueueWorkItem2(0xD, 1, lambda_11F5)

    def lambda_1206():
        OP_6D(-460, 0, -68660, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1206)

    def lambda_121E():
        OP_8E(0xFE, 0xFFFFF6FA, 0x0, 0xFFFEEEF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_121E)

    def lambda_1239():

        label("loc_1239")

        OP_8C(0xFE, 180, 0)
        OP_48()
        Jump("loc_1239")

    QueueWorkItem2(0x101, 1, lambda_1239)
    WaitChrThread(0xE, 0x2)
    SetChrChipByIndex(0xE, 9)
    SetChrSubChip(0xE, 0)
    SetChrFlags(0xE, 0x20)

    def lambda_125E():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_125E)
    OP_94(0x1, 0x101, 0xB4, 0x1F4, 0x7D0, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(
        0x101,
        "#506F#5P哇哇，提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#562F#6P实、实在太好啦。\x01",
            "又见到你们了～\x02\x03",
            "又见到姐姐你们了～\x01",
            "我们从游击士协会听说了\x01",
            "姐姐你们在城里战斗的事情……\x02\x03",
            "#069F呜呜，你们平安真是太好了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#5P提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#019F#5P谢谢你……\x01",
            "让你为我们担心了。\x02\x03",
            "#010F阿加特兄……也平安无事呢。\x01",
            "　\x02\x03",
            "您为什么也到王都来呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1400():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1400)

    def lambda_140E():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_140E)

    def lambda_141C():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_141C)

    def lambda_142A():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_142A)

    def lambda_1438():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1438)

    def lambda_1446():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1446)

    def lambda_1454():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1454)

    ChrTalk(
        0xD,
        (
            "#051F其实是在逃亡的途中，\x01",
            "偶然找到了一艘开往王都的货船。\x02\x03",
            "我们暗中乘着货船潜入这里，\x01",
            "不过，来到之后却发现到处都是一团糟。\x02\x03",
            "在向艾南打听了事情的经过之后，\x01",
            "就特地赶来王城看一看情况。\x02\x03",
            "对了，他叫我带了些东西给你们。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B8")
    Sleep(100)
    OP_AF(0x63, 0x4B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x4C, 0x4, 0x10)
    OP_28(0x4C, 0x4, 0x20)

    label("loc_15B8")

    OP_28(0x4D, 0x4, 0x10)
    OP_28(0x4D, 0x1, 0x100)
    Sleep(100)
    OP_AF(0x63, 0x4D)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x4E, 0x4, 0x10)
    OP_28(0x4E, 0x4, 0x20)

    ChrTalk(
        0x101,
        (
            "#004F#5P这样可以吗……\x01",
            "还没有去协会做详细的报告呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#053F我已经从亲卫队的队员那里\x01",
            "了解到大概的情况了。\x02\x03",
            "#050F可是……\x01",
            "这么多人聚在这里做什么呢？\x02\x03",
            "是在商量怎么把\x01",
            "残余的特务兵彻底打垮吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_44(0xD, 0xFF)
    TurnDirection(0xD, 0x105, 400)

    ChrTalk(
        0xD,
        "#052F嗯，你是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xD, 400)

    def lambda_174C():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_174C)

    def lambda_175A():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_175A)

    def lambda_1768():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1768)
    SetChrChipByIndex(0xE, 6)
    SetChrSubChip(0xE, 0)
    ClearChrFlags(0xE, 0x20)
    OP_94(0x1, 0xE, 0xB4, 0xC8, 0x3E8, 0x0)

    def lambda_1794():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1794)

    ChrTalk(
        0x105,
        (
            "#041F#5P好久不见了，阿加特先生。\x02\x03",
            "灯塔的事情多谢您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#052F我记得你是叫科洛丝对吧？\x02\x03",
            "可是，为什么你一个学生\x01",
            "会跑到这种地方来啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F#5P看来我孙女承蒙过你的关照啊。\x01",
            "　\x02\x03",
            "我也在此向你表示谢意。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(
        0xD,
        (
            "#051F哈哈，不用放在心上。\x01",
            "对我来说只是单纯的任务罢了。\x02\x03",
            "对了，老太太。\x01",
            "你是这个王城的什么人啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#177F#2P无、无礼之徒！\x02\x03",
            "#177F你可知道这位夫人是谁！？\x02\x03",
            "她是利贝尔王国的一国之主\x01",
            "艾莉茜雅女王陛下！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_19F0():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_19F0)

    ChrTalk(
        0xD,
        (
            "#055F哎呀……\x02\x03",
            "我就说好像感觉在哪见过……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#104F#2P哎呀呀，你这个小子，\x01",
            "很多方面还是不成熟啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xF, 400)

    ChrTalk(
        0xD,
        "#054F#6P你说什么！\x02",
    )

    CloseMessageWindow()

    def lambda_1AE3():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1AE3)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xE, 0x105, 400)

    ChrTalk(
        0xE,
        (
            "#065F#6P女、女王陛下！？\x02\x03",
            "这、这么说……\x01",
            "那位姐姐不就是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xE, 400)

    ChrTalk(
        0xA,
        (
            "#010F#6P女王陛下的孙女科洛蒂娅公主。\x01",
            "　\x02\x03",
            "我们都叫她科洛丝哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#6P科洛丝。\x01",
            "这个小姑娘是博士的孙女提妲。\x02\x03",
            "就像我们的妹妹一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F#2P是这样啊……\x01",
            "初次见面，提妲小妹妹。\x02\x03",
            "#041F叫我科洛丝就可以了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#067F#6P好、好的……\x02\x03",
            "科、科洛丝姐姐……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x103, 0xFFFFFE48, 0x0, 0xFFFEF494, 0x7D0, 0x0)
    TurnDirection(0x103, 0xE, 400)

    ChrTalk(
        0x103,
        (
            "#023F哎哟哟。\x01",
            "这个孩子好～可爱呢。\x02\x03",
            "#021F我叫雪拉扎德，\x01",
            "是艾丝蒂尔和约修亚的前辈哦。\x02\x03",
            "叫我雪拉就行了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x103, 400)

    ChrTalk(
        0xE,
        "#066F#6P好、好的，雪拉姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#031F嘻嘻……那么我就是\x01",
            "『奥利维尔小哥哥』了哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#6P别、别管那家伙，不要理他。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xA, 400)

    ChrTalk(
        0xF,
        (
            "#102F其他的姑且不论……\x01",
            "你们应该不只是因为这个\x01",
            "导力梯不能启动而烦恼吧。\x02\x03",
            "到底是发生了什么事情？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E4D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1E4D)

    def lambda_1E5B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E5B)

    def lambda_1E69():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E69)
    OP_8C(0xA, 180, 400)

    ChrTalk(
        0xA,
        "#013F#5P事实上……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚向拉赛尔博士等人说明了\x01",
            "上校的企图和与『辉之环』有关的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0xD,
        (
            "#057F喂喂，没有搞错吧……\x01",
            "可别开这样的玩笑啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#065F#6P那样的东西竟然埋在这地下……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#104F呼……\x01",
            "果然和我所担心的一样啊。\x02\x03",
            "#102F如果能够使用这个导力梯的话，\x01",
            "就可以降落到那里去了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#012F#5P嗯……\x01",
            "可是它被特殊的钥匙给锁住了。\x02\x03",
            "似乎是使用了结晶回路……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 0, 400)

    ChrTalk(
        0xF,
        (
            "#103F呵呵，是这样。\x02\x03",
            "让我来看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-470, 100, -63150, 0)
    OP_67(0, 6860, -10000, 0)
    OP_6B(1470, 0)
    OP_6C(32000, 0)
    OP_6E(536, 0)
    SetChrPos(0xF, -230, 100, -61280, 0)
    SetChrPos(0xE, 630, 100, -61490, 327)
    SetChrPos(0x101, -20, 100, -62860, 0)
    SetChrPos(0xA, -1040, 100, -62820, 33)
    SetChrPos(0x8, -80, 0, -65250, 0)
    SetChrPos(0x9, 760, 0, -66280, 346)
    SetChrPos(0xD, 1100, 100, -63990, 334)
    SetChrPos(0x105, -840, 0, -67210, 339)
    SetChrPos(0xC, -2050, 0, -66600, 39)
    SetChrPos(0x103, -3290, 0, -67250, 44)
    SetChrPos(0xB, -1860, 0, -67840, 10)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xF,
        (
            "#100F#6P这东西是用到了我开发的磁卡钥匙。\x01",
            "　\x02\x03",
            "将拥有相同的结晶回路的磁卡\x01",
            "插进去就可以解锁了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拉赛尔博士取出了一个小型装置，\x01",
            "然后将导力缆插入卡槽之中。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0xF,
        (
            "#102F#6P哦，这个是早期的型号，\x01",
            "所以没有采用保护技术。\x02\x03",
            "这样，调整导力压，\x01",
            "让特定的负荷进入回路……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xB7, 0x0, 0x64)
    OP_71(0x1, 0x4)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#001F#6P太棒了，不愧是博士啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#010F#6P……名不虚传。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#091F呵呵……好厉害。\x02\x03",
            "#090F那么我们就立刻前往地下去吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 20, 0, -77690, 315)

    NpcTalk(
        0x10,
        "青年的声音",
        "不、不得了了！\x02",
    )

    CloseMessageWindow()

    def lambda_2462():

        label("loc_2462")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2462")

    QueueWorkItem2(0xA, 1, lambda_2462)

    def lambda_2473():

        label("loc_2473")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2473")

    QueueWorkItem2(0x101, 1, lambda_2473)

    def lambda_2484():

        label("loc_2484")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2484")

    QueueWorkItem2(0x105, 1, lambda_2484)

    def lambda_2495():

        label("loc_2495")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2495")

    QueueWorkItem2(0x103, 1, lambda_2495)

    def lambda_24A6():

        label("loc_24A6")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24A6")

    QueueWorkItem2(0x8, 1, lambda_24A6)

    def lambda_24B7():

        label("loc_24B7")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24B7")

    QueueWorkItem2(0x9, 1, lambda_24B7)

    def lambda_24C8():

        label("loc_24C8")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24C8")

    QueueWorkItem2(0xB, 1, lambda_24C8)

    def lambda_24D9():

        label("loc_24D9")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24D9")

    QueueWorkItem2(0xC, 1, lambda_24D9)

    def lambda_24EA():

        label("loc_24EA")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24EA")

    QueueWorkItem2(0xF, 1, lambda_24EA)

    def lambda_24FB():

        label("loc_24FB")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24FB")

    QueueWorkItem2(0xE, 1, lambda_24FB)

    def lambda_250C():

        label("loc_250C")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_250C")

    QueueWorkItem2(0xD, 1, lambda_250C)

    def lambda_251D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_251D)

    def lambda_252F():
        OP_8E(0xFE, 0x1D6, 0x0, 0xFFFEF688, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_252F)
    OP_6D(-170, 0, -65530, 1500)

    ChrTalk(
        0x9,
        "#173F怎么，怎么了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "一个师的正规军\x01",
            "到达了王都的正门！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "是由一个看起来是\x01",
            "情报部的军官模样的人率领的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#178F什么，竟然这么快就到了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "更严重的是还有三艘\x01",
            "军用警备飞艇正从湖面上接近！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "究、究竟应该怎么办！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#177F唉，在这紧要关头！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#094F……还是由我出面去劝说他们吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xC, 0xFF)

    def lambda_2729():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2729)

    def lambda_2737():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2737)

    def lambda_2745():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2745)

    def lambda_2753():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2753)

    def lambda_2761():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2761)

    def lambda_276F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_276F)

    def lambda_277D():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_277D)

    def lambda_278B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_278B)

    ChrTalk(
        0x105,
        "#043F祖、祖母大人……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#092F我要到屋顶的露台上去，\x01",
            "让前来的部队听到我的解释。\x02\x03",
            "尤莉亚中尉，帮我准备一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#173F可、可是……\x01",
            "万一他们展开攻击可就糟了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#094F我相信他们。\x02\x03",
            "虽然他们对事情有一些误解，\x01",
            "但他们还是利贝尔的子民……\x02\x03",
            "#090F如果看到了我、听到我的声音，\x01",
            "还有什么理由会展开攻击呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#175F……陛下……\x02",
    )

    CloseMessageWindow()

    def lambda_292F():
        OP_6D(-470, 100, -63150, 1200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_292F)
    TurnDirection(0x8, 0x101, 400)
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "#093F艾丝蒂尔，还有大家……\x02\x03",
            "把这件事情委托给你们，\x01",
            "我真是非常地过意不去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5P女王陛下……\x01",
            "请您不要这么说。\x02\x03",
            "我们一定不会让理查德上校得逞的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#010F#5P请放心地交给我们去办吧。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(140, 100, -61920, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    OP_A1(0x11, 0x0)
    SetChrPos(0x11, 0, 0, -62000, 0)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x40)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0xA, 0x20)
    SetChrBattleFlags(0x105, 0x20)
    SetChrBattleFlags(0x103, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0xE, 0x20)
    SetChrBattleFlags(0xD, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0xF, 0x20)
    OP_89(0x101, -1370, 10000, -61730, 180)
    OP_89(0xA, -1470, 10000, -60920, 180)
    OP_89(0x105, -390, 10000, -62450, 180)
    OP_89(0x103, -1660, 10000, -63180, 180)
    OP_89(0xB, -850, 10000, -64019, 180)
    OP_89(0xE, 950, 10000, -61560, 180)
    OP_89(0xC, 1300, 10000, -63220, 180)
    OP_89(0xD, 420, 10000, -64010, 180)
    OP_89(0xF, -70, 10000, -61150, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xF7, 0x0, 0x64)
    OP_22(0x68, 0x1, 0x64)

    def lambda_2B91():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2B91)
    Sleep(300)

    def lambda_2BB1():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BB1)
    Sleep(500)

    def lambda_2BD1():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BD1)
    Sleep(800)

    def lambda_2BF1():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BF1)
    Sleep(1000)

    def lambda_2C11():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C11)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x11, 0xFF)
    OP_A1(0x11, 0x2)
    SetChrPos(0x11, 0, 170000, 0, 0)
    SetChrFlags(0x11, 0x4)
    OP_11(0x0, 0x0, 0x0, 0x7530, 0x9C40, 0x0)
    SetMapFlags(0x10)
    OP_48()
    OP_69(0x11, 0x0)
    OP_6A(0x11)
    OP_67(0, 4000, -10000, 0)
    OP_6B(2070, 0)
    OP_6C(65000, 0)
    OP_6E(554, 0)
    OP_67(0, 3080, -10000, 0)
    OP_6B(2180, 0)
    OP_6C(35000, 0)
    OP_6E(450, 0)

    def lambda_2CCE():
        OP_67(0, 11400, -10000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CCE)

    def lambda_2CE6():
        OP_6B(1310, 20000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CE6)

    def lambda_2CF6():
        OP_6C(55000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2CF6)

    def lambda_2D06():
        OP_6E(776, 20000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D06)
    SetChrPos(0x101, 0, 0, 0, 0)
    ClearChrFlags(0xA, 0x4)
    OP_89(0x101, -1370, 190100, 270, 270)
    OP_89(0xA, -1470, 190100, 1080, 270)
    OP_89(0x105, -390, 190100, -450, 270)
    OP_89(0x103, -1660, 190100, -1180, 270)
    OP_89(0xB, -850, 190100, -2020, 270)
    OP_89(0xE, 950, 190100, 440, 270)
    OP_89(0xC, 1300, 190100, -1220, 270)
    OP_89(0xD, 420, 190100, -2009, 270)
    OP_89(0xF, -70, 190100, 750, 270)
    FadeToBright(2000, 0)
    OP_8F(0x11, 0x0, 0xEA60, 0x0, 0x1F40, 0x0)
    FadeToDark(2000, 0, -1)

    def lambda_2DEC():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2DEC)
    OP_24(0x68, 0x5A)
    Sleep(400)
    OP_24(0x68, 0x55)
    Sleep(400)
    OP_24(0x68, 0x50)
    Sleep(400)
    OP_24(0x68, 0x4B)
    Sleep(400)
    OP_24(0x68, 0x46)
    Sleep(400)
    OP_24(0x68, 0x41)
    Sleep(400)
    OP_24(0x68, 0x3C)
    Sleep(400)
    OP_23(0x68)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_278 end

    SaveToFile()

Try(main)
