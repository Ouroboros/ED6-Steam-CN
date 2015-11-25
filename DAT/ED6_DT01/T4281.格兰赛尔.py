from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4281   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4281.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60035",
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
        'ED6_DT07/CH00050 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT07/CH02020 ._CH',             # 07
        'ED6_DT07/CH01320 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02010P._CP',             # 00
        'ED6_DT07/CH02090P._CP',             # 01
        'ED6_DT07/CH00010P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00070P._CP',             # 04
        'ED6_DT07/CH00050P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT07/CH02020P._CP',             # 07
        'ED6_DT07/CH01320P._CP',             # 08
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
        "Function_0_232",          # 00, 0
        "Function_1_241",          # 01, 1
        "Function_2_276",          # 02, 2
    )


    def Function_0_232(): pass

    label("Function_0_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_240")
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_240")

    Return()

    # Function_0_232 end

    def Function_1_241(): pass

    label("Function_1_241")

    OP_A1(0x11, 0x2)
    SetChrPos(0x11, 0, 0, 0, 0)
    SetChrFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_26C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26C")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_241 end

    def Function_2_276(): pass

    label("Function_2_276")

    EventBegin(0x0)
    OP_6D(-40, 100, -60120, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
    SetChrPos(0xB, 640, 0, -72930, 0)
    SetChrPos(0xC, 2070, 0, -73010, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    def lambda_384():
        OP_8E(0xFE, 0xFFFFFA24, 0x0, 0xFFFEF502, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_384)

    def lambda_39F():
        OP_8E(0xFE, 0xFFFFFBD2, 0x0, 0xFFFEEF94, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_39F)

    def lambda_3BA():
        OP_8E(0xFE, 0x1A4, 0x0, 0xFFFEF390, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3BA)

    def lambda_3D5():
        OP_8E(0xFE, 0x50, 0x0, 0xFFFEF8CC, 0x578, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D5)

    def lambda_3F0():
        OP_8E(0xFE, 0x488, 0x0, 0xFFFEF7A0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3F0)

    def lambda_40B():
        OP_8E(0xFE, 0xFFFFF74A, 0x0, 0xFFFEF7FA, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_40B)

    def lambda_426():
        OP_8E(0xFE, 0x280, 0x0, 0xFFFEEEFE, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_426)

    def lambda_441():
        OP_8E(0xFE, 0x816, 0x0, 0xFFFEF1D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_441)

    def lambda_45C():
        OP_6D(-80, 0, -64650, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_45C)
    FadeToBright(1000, 0)
    WaitChrThread(0x0, 0x2)

    ChrTalk(
        0x9,
        (
            "#170F在这种地方\x01",
            "居然还有导力梯……\x02\x03",
            "这以前是绝对没有过的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#070F这东西是上校\x01",
            "特意建造的吧……\x02\x03",
            "如此说来，这个导力梯\x01",
            "应该就可以下降到\x01",
            "封印『辉之环』的地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F是啊……\x02\x03",
            "或许，这正是他们\x01",
            "发动这次政变的背后\x01",
            "所隐藏的真实目的。\x02\x03",
            "只要不占领王城，\x01",
            "就不能建造出这样的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F竟然、竟然会是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#030F呵呵，可能就是如此。\x02\x03",
            "想要打开由王权守护的圣域\x01",
            "就必须采取一些强硬的手段……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#010F不管怎么样，想要下降到地下\x01",
            "就必须要使用这个东西。\x02\x03",
            "先把它启动了再说。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xA, 0xFFFFFC68, 0x0, 0xFFFEFCAA, 0xBB8, 0x0)
    OP_8E(0xA, 0xFFFFFDDA, 0x3C, 0xFFFEFE4E, 0xBB8, 0x0)
    OP_8E(0xA, 0xA, 0x64, 0xFFFF10B4, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚开始调查\x01",
            "导力梯的控电盘。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "表情渐渐地焦急起来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(
        0x101,
        "#000F怎么了，约修亚？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "#010F这是……\x01",
            "用导力的方式锁住了。\x02\x03",
            "没有特殊结晶回路组成的钥匙\x01",
            "是不能将其启动的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_895():
        OP_8E(0xFE, 0xFFFFFF60, 0x0, 0xFFFF01E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_895)

    ChrTalk(
        0x101,
        "#000F什、什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F怎么会这样，都到了这里了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "#170F把拘捕到的特务兵\x01",
            "绑过来问话！\x02\x03",
            "钥匙一定存在于某个地方的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯……\x01",
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

    def lambda_9ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9ED)

    ChrTalk(
        0xF,
        "不，还没有到那种地步。\x02",
    )

    CloseMessageWindow()

    def lambda_A21():
        OP_6D(-550, 0, -69950, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A21)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_A67():

        label("loc_A67")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_A67")

    QueueWorkItem2(0x101, 1, lambda_A67)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_AAB():

        label("loc_AAB")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_AAB")

    QueueWorkItem2(0x105, 1, lambda_AAB)

    def lambda_ABC():

        label("loc_ABC")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_ABC")

    QueueWorkItem2(0x103, 1, lambda_ABC)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_B00():

        label("loc_B00")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_B00")

    QueueWorkItem2(0x8, 1, lambda_B00)

    def lambda_B11():

        label("loc_B11")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_B11")

    QueueWorkItem2(0x9, 1, lambda_B11)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_B55():

        label("loc_B55")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_B55")

    QueueWorkItem2(0xB, 1, lambda_B55)

    def lambda_B66():

        label("loc_B66")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_B66")

    QueueWorkItem2(0xC, 1, lambda_B66)
    WaitChrThread(0x0, 0x2)

    ChrTalk(
        0x101,
        "#000F哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#010F难道是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#090F哦……是拉赛尔博士！？\x02",
    )

    CloseMessageWindow()

    def lambda_BC8():
        OP_6D(-400, 0, -68560, 2500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BC8)

    def lambda_BE0():
        OP_8E(0xFE, 0xFFFFFD4E, 0x0, 0xFFFEE9EA, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_BE0)
    Sleep(200)
    SetChrFlags(0xA, 0x4)

    def lambda_C05():
        OP_8E(0xFE, 0xFFFFF484, 0x0, 0xFFFEF502, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C05)

    def lambda_C20():

        label("loc_C20")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_C20")

    QueueWorkItem2(0xA, 1, lambda_C20)
    WaitChrThread(0x0, 0x2)

    ChrTalk(
        0xF,
        (
            "#100F艾莉茜雅。\x01",
            "久疏问候了啊。\x02\x03",
            "#100F艾丝蒂尔、约修亚，\x01",
            "看来也很精神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F等、等一下……\x01",
            "为什么博士会在这里！\x02\x03",
            "不是在蔡斯被情报部\x01",
            "追击而逃离了吗……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D1E():

        label("loc_D1E")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_D1E")

    QueueWorkItem2(0xA, 1, lambda_D1E)

    ChrTalk(
        0xA,
        (
            "#010F而且，既然博士\x01",
            "都到这里来了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D66():
        OP_6D(-20, 0, -71810, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D66)
    Sleep(100)

    def lambda_D83():

        label("loc_D83")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_D83")

    QueueWorkItem2(0x101, 1, lambda_D83)
    Sleep(50)

    def lambda_D99():

        label("loc_D99")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_D99")

    QueueWorkItem2(0x105, 1, lambda_D99)

    def lambda_DAA():

        label("loc_DAA")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_DAA")

    QueueWorkItem2(0x103, 1, lambda_DAA)
    Sleep(50)

    def lambda_DC0():

        label("loc_DC0")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_DC0")

    QueueWorkItem2(0x8, 1, lambda_DC0)

    def lambda_DD1():

        label("loc_DD1")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_DD1")

    QueueWorkItem2(0x9, 1, lambda_DD1)
    Sleep(50)

    def lambda_DE7():

        label("loc_DE7")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_DE7")

    QueueWorkItem2(0xB, 1, lambda_DE7)

    def lambda_DF8():

        label("loc_DF8")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_DF8")

    QueueWorkItem2(0xC, 1, lambda_DF8)

    def lambda_E09():

        label("loc_E09")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_E09")

    QueueWorkItem2(0xF, 1, lambda_E09)

    ChrTalk(
        0xE,
        (
            "爷爷、爷爷啊。\x01",
            "你跑到哪里去了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "喂，你不要在我\x01",
            "面前窜来窜去好不好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "和老爷子果然是一家人，\x01",
            "都属于静不下来的类型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "可、可是阿加特大哥哥……\x02",
    )

    CloseMessageWindow()

    def lambda_EC4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_EC4)

    def lambda_ED6():
        OP_8E(0xFE, 0xFFFFFBA0, 0x0, 0xFFFEDB30, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_ED6)
    Sleep(600)

    def lambda_EF6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EF6)

    def lambda_F08():
        OP_8E(0xFE, 0xE6, 0x0, 0xFFFEDC16, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_F08)

    ChrTalk(
        0xE,
        "#060F啊……！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)

    ChrTalk(
        0x101,
        "#000F提妲！？\x02",
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
            "#060F艾丝蒂尔姐姐！\x01",
            "还有约修亚哥哥！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F7B():
        OP_8E(0xFE, 0xFFFFF696, 0x0, 0xFFFEEF9E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_F7B)

    def lambda_F96():

        label("loc_F96")

        OP_8C(0xFE, 0, 0)
        OP_48()
        Jump("loc_F96")

    QueueWorkItem2(0xE, 1, lambda_F96)

    def lambda_FA7():
        OP_8E(0xFE, 0xFFFFF880, 0x0, 0xFFFEE922, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_FA7)

    def lambda_FC2():

        label("loc_FC2")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_FC2")

    QueueWorkItem2(0xD, 1, lambda_FC2)
    OP_6D(-460, 0, -68660, 2000)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(
        0x101,
        "#000F哇哇，提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#060F实、实在太好啦。\x01",
            "又见到你们了～\x02\x03",
            "从游击士协会听说了\x01",
            "姐姐你们在城里\x01",
            "战斗的事情……\x02\x03",
            "呜呜，你们平安真是太好了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F提妲……\x02",
    )

    CloseMessageWindow()

    def lambda_10CF():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10CF)

    ChrTalk(
        0xA,
        (
            "#010F谢谢……\x01",
            "让你为我们担心了。\x02\x03",
            "阿加特兄……\x01",
            "也平安无事呢。\x02\x03",
            "为什么会到王都来呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1159():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1159)

    def lambda_1167():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1167)

    def lambda_1175():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1175)

    def lambda_1183():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1183)

    def lambda_1191():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1191)

    def lambda_119F():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_119F)

    def lambda_11AD():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_11AD)

    def lambda_11BB():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_11BB)

    ChrTalk(
        0xD,
        (
            "#050F其实是偶然的找到了\x01",
            "一艘开往王都的货船。\x02\x03",
            "乘着它暗中潜入这里，\x01",
            " \x02\x03",
            "就特地赶来王城这边看一看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F是、是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#050F可是这么多人聚\x01",
            "在这里是在做什么呢？\x02\x03",
            "准是在商量怎么把\x01",
            "残余的特务兵彻底打垮吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xD, 0xFF)
    TurnDirection(0xD, 0x105, 400)

    ChrTalk(
        0xD,
        "#050F……嗯，你是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xD, 400)

    def lambda_1367():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1367)

    def lambda_1375():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1375)

    def lambda_1383():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1383)

    def lambda_1391():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1391)

    ChrTalk(
        0x105,
        (
            "#040F好久不见了，阿加特大哥。\x02\x03",
            "灯塔的事情多谢您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#050F我记得你是叫科洛丝对吧？\x02\x03",
            "可是为何你一个学生\x01",
            "会跑到这里来呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F看来我孙女承蒙过\x01",
            "你的照顾啊。\x02\x03",
            "我在这儿也向你\x01",
            "表示谢意。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(
        0xD,
        (
            "#050F哈哈，不用放在心上。\x01",
            "对我来说只是单纯的任务罢了。\x02\x03",
            "对了，老太太，\x01",
            "你是这个城的什么人呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#170F无、无礼之徒！\x01",
            "你可知道这位夫人是谁！\x02\x03",
            "她是利贝尔的一国之主，\x01",
            "艾莉茜雅女王陛下！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15B1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_15B1)

    ChrTalk(
        0xD,
        (
            "#050F呼～～\x02\x03",
            "我是说好像感觉\x01",
            "好像在哪里见过的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#100F哎呀呀。\x01",
            " \x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xF, 400)

    ChrTalk(
        0xD,
        "#050F你说什么！\x02",
    )

    CloseMessageWindow()

    def lambda_169E():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_169E)
    TurnDirection(0xE, 0x105, 400)

    ChrTalk(
        0xE,
        (
            "#060F女、女王陛下！？\x02\x03",
            "这、这么说……\x01",
            "那位姐姐不就是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xE, 400)

    ChrTalk(
        0xA,
        (
            "#010F女王陛下的孙女，\x01",
            "科洛蒂娅公主。\x02\x03",
            "我们都\x01",
            "叫她科洛丝哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F科洛丝。\x01",
            "这个小姑娘是博士的孙女提妲。\x02\x03",
            "她就像我们的妹妹一样哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F是这样啊……\x01",
            "初次见面，提妲小妹妹。\x02\x03",
            "叫我科洛丝\x01",
            "就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#060F好、好的呢……\x02\x03",
            "科、科洛丝姐姐……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x103, 0xFFFFFE48, 0x0, 0xFFFEF494, 0x7D0, 0x0)
    TurnDirection(0x103, 0xE, 400)

    ChrTalk(
        0x103,
        (
            "#020F哎哟哟。\x01",
            "这个孩子好可爱呀。\x02\x03",
            "我叫雪拉扎德，\x01",
            "是艾丝蒂尔和约修亚的前辈哦。\x02\x03",
            "叫我雪拉就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#060F好、好的，雪拉姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#030F那么我就是\x01",
            "『奥利维尔小哥哥』了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F别管那家伙，不要理他。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xA, 400)

    ChrTalk(
        0xF,
        (
            "#100F其他的姑且不论……\x01",
            "不过应该不只是因为\x01",
            "这个导力梯不能启动而烦恼吧。\x02\x03",
            "到底是发生了什么事情？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_19D0():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_19D0)

    def lambda_19DE():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_19DE)

    ChrTalk(
        0xA,
        "#010F那是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚说明了上校的企图\x01",
            "和与『辉之环』有关的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xD,
        (
            "#050F喂喂，没有搞错吧……\x01",
            "可别开这样的玩笑啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#060F那样的东西\x01",
            "竟然埋在这儿地下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#100F呼……果然和我所\x01",
            "担忧的一样啊。\x02\x03",
            "如果能够使用这个导力梯的话，\x01",
            "就可以下降到那里去了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#010F嗯，可是它被\x01",
            "特殊的钥匙给锁住了。\x02\x03",
            "似乎是使用了结晶回路……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 0, 400)

    ChrTalk(
        0xF,
        (
            "#100F呵呵，是这样。\x02\x03",
            "让我来看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-470, 100, -63150, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF, -230, 100, -61280, 0)
    SetChrPos(0xE, 630, 100, -61490, 327)
    SetChrPos(0x101, -20, 100, -62860, 0)
    SetChrPos(0xA, -1040, 100, -62820, 33)
    SetChrPos(0x8, -80, 0, -65250, 9)
    SetChrPos(0x9, 760, 0, -66280, 346)
    SetChrPos(0xD, 1100, 100, -63990, 334)
    SetChrPos(0x105, -840, 0, -67210, 339)
    SetChrPos(0xC, -2050, 0, -66600, 39)
    SetChrPos(0x103, -3290, 0, -67250, 44)
    SetChrPos(0xB, -1860, 0, -67840, 10)
    OP_0D()

    ChrTalk(
        0xF,
        (
            "#100F这东西是用到了我\x01",
            "开发的磁卡钥匙。\x02\x03",
            "将拥有相同的结晶回路的\x01",
            "磁卡插入进去就可以解锁了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "博士取出了一个小型装置，\x01",
            "然后将伸出来的线缆\x01",
            "插入导力梯的卡槽之中。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xF,
        (
            "#100F哦，这个是早期的型号，\x01",
            "所以没有采用保护技术。\x02\x03",
            "这样，调整导力压，\x01",
            "让特定的负荷进入回路……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F太棒了，不愧是博士啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#010F……名不虚传。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F呵呵……好厉害。\x02\x03",
            "那么我们就立刻\x01",
            "降到地下去吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 20, 0, -77690, 315)

    ChrTalk(
        0x10,
        "不、不得了了！\x02",
    )

    CloseMessageWindow()

    def lambda_1F5E():

        label("loc_1F5E")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1F5E")

    QueueWorkItem2(0x101, 1, lambda_1F5E)

    def lambda_1F6F():

        label("loc_1F6F")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1F6F")

    QueueWorkItem2(0x105, 1, lambda_1F6F)

    def lambda_1F80():

        label("loc_1F80")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1F80")

    QueueWorkItem2(0x103, 1, lambda_1F80)

    def lambda_1F91():

        label("loc_1F91")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1F91")

    QueueWorkItem2(0x8, 1, lambda_1F91)

    def lambda_1FA2():

        label("loc_1FA2")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FA2")

    QueueWorkItem2(0x9, 1, lambda_1FA2)

    def lambda_1FB3():

        label("loc_1FB3")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FB3")

    QueueWorkItem2(0xB, 1, lambda_1FB3)

    def lambda_1FC4():

        label("loc_1FC4")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FC4")

    QueueWorkItem2(0xC, 1, lambda_1FC4)

    def lambda_1FD5():

        label("loc_1FD5")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FD5")

    QueueWorkItem2(0xF, 1, lambda_1FD5)

    def lambda_1FE6():

        label("loc_1FE6")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FE6")

    QueueWorkItem2(0xE, 1, lambda_1FE6)

    def lambda_1FF7():

        label("loc_1FF7")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FF7")

    QueueWorkItem2(0xD, 1, lambda_1FF7)

    def lambda_2008():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2008)

    def lambda_201A():
        OP_8E(0xFE, 0x1D6, 0x0, 0xFFFEF688, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_201A)
    OP_6D(-170, 0, -65530, 3000)

    ChrTalk(
        0x9,
        "#170F怎么，怎么了！？\x02",
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
        "#170F什么！？\x02",
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
        "#170F唉，在这紧要关头！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F……还是由我出面\x01",
            "去劝说他们吧。\x02",
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

    def lambda_2208():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2208)

    def lambda_2216():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2216)

    def lambda_2224():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2224)

    def lambda_2232():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2232)

    def lambda_2240():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2240)

    def lambda_224E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_224E)

    def lambda_225C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_225C)

    ChrTalk(
        0x105,
        "#040F祖、祖母大人……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F我到屋顶的阳台上去\x01",
            "让前来的部队听到我的声音。\x02\x03",
            "尤莉亚中尉，帮我准备一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#170F可、可是……\x01",
            "万一他们展开攻击可就糟了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F我相信他们。\x02\x03",
            "虽然有一些误解，\x01",
            "但他们还是利贝尔的子民……\x02\x03",
            "如果看到了我，听到我的声音，\x01",
            "还有什么理由会展开攻击呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#170F……陛下……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#090F艾丝蒂尔，还有大家……\x02\x03",
            "把这件事情委托给你们，\x01",
            "我心理很是过意不去啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F女王陛下……\x01",
            "请您不要这么说。\x02\x03",
            "理查德上校的野心，\x01",
            "我们一定会阻止的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x11, 0x2)
    SetChrPos(0x11, 0, 170000, 0, 0)
    SetChrFlags(0x11, 0x4)

    ChrTalk(
        0xA,
        "请放心的交给我们去办吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_11(0x0, 0x0, 0x0, 0x7530, 0x9C40, 0x0)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x11, 0x0)
    OP_6A(0x11)
    OP_67(0, 4000, -10000, 0)
    OP_6B(2070, 0)
    OP_6C(65000, 0)
    OP_6E(554, 0)

    def lambda_2571():
        OP_67(0, 15000, -10000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2571)

    def lambda_2589():
        OP_6B(1280, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2589)

    def lambda_2599():
        OP_6C(600000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2599)

    def lambda_25A9():
        OP_6E(900, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_25A9)
    SetChrPos(0x101, 0, 0, 0, 0)
    ClearChrFlags(0xA, 0x4)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0xA, 0x20)
    SetChrBattleFlags(0x105, 0x20)
    SetChrBattleFlags(0x103, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0xE, 0x20)
    SetChrBattleFlags(0xD, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0xF, 0x20)
    OP_89(0x101, -1370, 190100, 270, 258)
    OP_89(0xA, -1470, 190100, 1080, 286)
    OP_89(0x105, -390, 190100, -450, 9)
    OP_89(0x103, -1660, 190100, -1180, 246)
    OP_89(0xB, -850, 190100, -2020, 246)
    OP_89(0xE, 950, 190100, 440, 319)
    OP_89(0xD, 1300, 190100, -1220, 265)
    OP_89(0xC, 420, 190100, -2009, 155)
    OP_89(0xF, -70, 190100, 750, 9)
    FadeToBright(2000, 0)
    OP_8F(0x11, 0x0, 0x9C40, 0x0, 0x2710, 0x0)
    FadeToDark(2000, 0, -1)
    OP_8F(0x11, 0x0, 0x0, 0x0, 0x2710, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_276 end

    SaveToFile()

Try(main)
