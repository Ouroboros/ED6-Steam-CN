from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2411   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2411.x',
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
        '特蕾莎院长',                           # 9
        '达尼艾尔',                             # 10
        '玛丽',                                 # 11
        '波利',                                 # 12
        '克拉姆',                               # 13
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
        'ED6_DT07/CH02590 ._CH',             # 00
        'ED6_DT07/CH02640 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02570 ._CH',             # 03
        'ED6_DT07/CH02500 ._CH',             # 04
        'ED6_DT06/CH20094 ._CH',             # 05
        'ED6_DT06/CH20095 ._CH',             # 06
        'ED6_DT06/CH20096 ._CH',             # 07
        'ED6_DT06/CH20097 ._CH',             # 08
        'ED6_DT07/CH02573 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH02590P._CP',             # 00
        'ED6_DT07/CH02640P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02570P._CP',             # 03
        'ED6_DT07/CH02500P._CP',             # 04
        'ED6_DT06/CH20094P._CP',             # 05
        'ED6_DT06/CH20095P._CP',             # 06
        'ED6_DT06/CH20096P._CP',             # 07
        'ED6_DT06/CH20097P._CP',             # 08
        'ED6_DT07/CH02573P._CP',             # 09
    )

    DeclNpc(
        X                   = 34340,
        Z                   = 0,
        Y                   = -31330,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 37220,
        Z                   = 0,
        Y                   = -33090,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x104,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 37310,
        Z                   = 1500,
        Y                   = -33090,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x104,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 37220,
        Z                   = 0,
        Y                   = -36830,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x104,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 37220,
        Z                   = 1500,
        Y                   = -36830,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x104,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_1C9",          # 01, 1
        "Function_2_252",          # 02, 2
        "Function_3_575",          # 03, 3
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1B1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_1B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_1C8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 2)

    label("loc_1C8")

    Return()

    # Function_0_19A end

    def Function_1_1C9(): pass

    label("Function_1_1C9")

    OP_6F(0x3, 10)
    OP_6F(0x4, 15)
    OP_6F(0x5, 20)
    OP_6F(0x6, 15)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xC, 37940, 1500, -36940, 225)
    SetChrPos(0x9, 37940, 200, -36940, 225)
    SetChrPos(0xA, 37960, 1500, -32830, 225)
    SetChrPos(0xB, 37960, 200, -32830, 225)
    Return()

    # Function_1_1C9 end

    def Function_2_252(): pass

    label("Function_2_252")

    EventBegin(0x0)
    OP_A2(0x41C)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 36300, 200, 42360, 270)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0x8, 255)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 0)
    OP_6F(0x3, 50)
    OP_6D(35210, 3800, -34580, 0)
    OP_67(0, 3030, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(37000, 0)
    OP_6E(280, 0)
    FadeToBright(500, 0)
    OP_6D(35210, 2500, -34580, 3000)
    Sleep(1000)
    Fade(1000)
    OP_6D(36570, 0, 42820, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#750F呵呵，要修补的东西还真多，\x01",
            "这也说明孩子们的精力都很旺盛吧……\x02\x03",
            "好了，差不多该休息了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x8, 3)
    SetChrPos(0x8, 35780, 0, 42330, 270)
    OP_0D()
    Sleep(500)

    def lambda_41A():
        OP_6D(35930, 0, 43280, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_41A)
    OP_8E(0x8, 0x87DC, 0x0, 0xA546, 0x3E8, 0x0)
    OP_8E(0x8, 0x864C, 0x0, 0xAA50, 0x3E8, 0x0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#754F女神啊， \x01",
            "请赐予这些孩子健康的明天吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x86, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#753F这是什么声音？\x01",
            "好像是柴火的声音……\x02\x03",
            "#753F……还有这气味是……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 180, 500)

    ChrTalk(
        0x8,
        "#755F………………难道！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T2403   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_252 end

    def Function_3_575(): pass

    label("Function_3_575")

    EventBegin(0x0)
    OP_22(0x87, 0x1, 0x46)
    SetChrPos(0x101, 40390, 0, -29880, 0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x9, 0x40)
    ClearMapFlags(0x1)
    OP_6D(35210, 2050, -34580, 0)
    OP_67(0, 3210, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(37000, 0)
    OP_6E(280, 0)
    OP_0D()
    OP_72(0x1, 0x10)
    OP_70(0x1, 0x14)
    OP_73(0x1)
    OP_8E(0x8, 0x8520, 0x0, 0xFFFF7BEE, 0xFA0, 0x0)

    ChrTalk(
        0x8,
        "#755F孩子们，快起来！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 1)
    SetChrSubChip(0xA, 1)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(1000)
    ClearChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0)

    def lambda_66B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_66B)
    OP_95(0xC, 0x0, 0x12C, 0x0, 0x258, 0xFA0)

    ChrTalk(
        0xC,
        (
            "#774F#2P哇哇哇……\x01",
            "对不起，我不会再这样了！\x02\x03",
            "#772F…………………哎？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 2)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#1P克拉姆……\x01",
            "你又睡昏头了吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F4():
        OP_6D(36380, 1500, -34730, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6F4)
    OP_8E(0x8, 0x8AD4, 0x0, 0xFFFF77CA, 0xBB8, 0x0)
    OP_8C(0x8, 90, 400)

    ChrTalk(
        0x8,
        (
            "#755F波利，达尼艾尔！\x01",
            "快起来！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 1)
    SetChrSubChip(0x9, 1)

    ChrTalk(
        0xB,
        "#4P呜唔～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3P怎么了啊……\x01",
            "老师你的样子好吓人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#752F……着火了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#774F#2P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1P真、真的！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#755F快下一楼去！\x02\x03",
            "都别慌！\x01",
            "快点跟老师走就是了！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-1280, 0, -1260, 0)
    OP_67(0, 7800, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_22(0x87, 0x1, 0x64)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0xB, 0x2)
    SetChrFlags(0xA, 0x1)
    SetChrFlags(0xC, 0x1)
    SetChrFlags(0x9, 0x1)
    SetChrFlags(0xB, 0x1)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0x8, 870, 1250, 12330, 0)
    SetChrPos(0xA, 560, 1750, 12770, 0)
    SetChrPos(0xC, 1240, 1750, 12770, 0)
    SetChrPos(0x9, 1220, 2000, 13840, 0)
    SetChrPos(0xB, 520, 2000, 13840, 0)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 2)
    SetChrChipByIndex(0x9, 1)
    SetChrChipByIndex(0xB, 4)
    Sleep(500)
    FadeToBright(1000, 0)

    def lambda_93A():
        OP_6D(530, 0, 10090, 2700)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_93A)
    Sleep(1000)

    def lambda_957():
        OP_8E(0xFE, 0x122, 0x0, 0x203A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_957)
    Sleep(100)

    def lambda_977():
        OP_8E(0xFE, 0x532, 0x0, 0x2170, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_977)

    def lambda_992():
        OP_8E(0xFE, 0x1F4, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_992)
    Sleep(100)

    def lambda_9B2():
        OP_8E(0xFE, 0x51E, 0x0, 0x26FC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9B2)

    def lambda_9CD():
        OP_8E(0xFE, 0x1F4, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9CD)
    WaitChrThread(0xA, 0x1)

    def lambda_9ED():
        OP_8E(0xFE, 0xFFFFFE70, 0x0, 0x229C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9ED)
    WaitChrThread(0x8, 0x2)

    ChrTalk(
        0xC,
        "#774F#2P哇哇，怎么会这样！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "咳咳，好呛～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "我、我怕～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "呜唔～……\x01",
            "我还想睡～……\x02",
        )
    )

    CloseMessageWindow()
    OP_70(0x0, 0x64)
    OP_8E(0x8, 0xFFFFFAD8, 0x0, 0x2058, 0xBB8, 0x0)

    def lambda_A9E():

        label("loc_A9E")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_A9E")

    QueueWorkItem2(0x8, 1, lambda_A9E)
    Sleep(400)

    ChrTalk(
        0x8,
        "#755F快，大家快从门口出去！\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_6F(0x0, 100)
    OP_70(0x0, 0x118)

    def lambda_AEC():
        OP_6D(-580, 0, 4990, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AEC)

    def lambda_B04():
        OP_8E(0xFE, 0xFFFFFB50, 0x0, 0x5D2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B04)
    Sleep(100)

    def lambda_B24():
        OP_8E(0xFE, 0xFFFFFB50, 0x0, 0x5D2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B24)
    Sleep(100)

    def lambda_B44():
        OP_8E(0xFE, 0xFFFFFB50, 0x0, 0x5D2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B44)
    Sleep(100)

    def lambda_B64():
        OP_8E(0xFE, 0xFFFFFB50, 0x0, 0x5D2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B64)
    Sleep(500)

    def lambda_B84():
        OP_8E(0xFE, 0xFFFFFB50, 0x0, 0x5D2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B84)
    OP_22(0x88, 0x0, 0x64)
    Sleep(200)
    OP_62(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_BF1():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_BF1)

    def lambda_C07():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C07)
    Sleep(200)

    def lambda_C22():
        OP_94(0x1, 0xFE, 0x0, 0x64, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C22)

    def lambda_C38():
        OP_94(0x1, 0xFE, 0xB4, 0x12C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C38)

    def lambda_C4E():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C4E)

    ChrTalk(
        0xC,
        "#775F哇啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "啊啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#756F怎，怎么会这样……\x02\x03",
            "啊啊，女神啊！\x01",
            "无论如何，请救救这些孩子吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CD8():
        OP_6B(3000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_CD8)
    OP_77(0xFF, 0x0, 0x0, 0x1F400, 0x0)
    Sleep(500)
    OP_20(0x5DC)
    FadeToDark(1000, 16777215, -1)
    OP_24(0x87, 0x5A)
    Sleep(300)
    OP_24(0x87, 0x50)
    Sleep(300)
    OP_24(0x87, 0x46)
    Sleep(300)
    OP_24(0x87, 0x3C)
    Sleep(300)
    OP_24(0x87, 0x32)
    Sleep(300)
    OP_24(0x87, 0x28)
    Sleep(300)
    OP_24(0x87, 0x1E)
    Sleep(300)
    OP_23(0x87)
    OP_0D()
    OP_6D(16750, 0, -54030, 0)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(1000, 16777215)
    OP_21()
    OP_0D()
    SetMapFlags(0x10000000)
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_575 end

    SaveToFile()

Try(main)
