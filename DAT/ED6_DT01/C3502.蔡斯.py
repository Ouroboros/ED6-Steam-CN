from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3502   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3502.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        '黑衣男子',                             # 9
        '黑衣男子',                             # 10
        '黑衣男子',                             # 11
        '拉赛尔博士',                           # 12
        '特务艇',                               # 13
        ' ',                                    # 14
        '黑衣男子',                             # 15
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
        'ED6_DT07/CH01610 ._CH',             # 00
        'ED6_DT07/CH00440 ._CH',             # 01
        'ED6_DT07/CH00441 ._CH',             # 02
        'ED6_DT07/CH00444 ._CH',             # 03
        'ED6_DT07/CH00100 ._CH',             # 04
        'ED6_DT07/CH00101 ._CH',             # 05
        'ED6_DT07/CH00112 ._CH',             # 06
        'ED6_DT07/CH00111 ._CH',             # 07
        'ED6_DT07/CH00150 ._CH',             # 08
        'ED6_DT07/CH00151 ._CH',             # 09
        'ED6_DT07/CH00160 ._CH',             # 0A
        'ED6_DT07/CH00161 ._CH',             # 0B
        'ED6_DT06/CH20110 ._CH',             # 0C
        'ED6_DT06/CH20111 ._CH',             # 0D
        'ED6_DT06/CH20104 ._CH',             # 0E
        'ED6_DT07/CH01330 ._CH',             # 0F
        'ED6_DT07/CH00442 ._CH',             # 10
        'ED6_DT07/CH00162 ._CH',             # 11
        'ED6_DT07/CH00050 ._CH',             # 12
        'ED6_DT07/CH00051 ._CH',             # 13
        'ED6_DT07/CH00055 ._CH',             # 14
        'ED6_DT07/CH00164 ._CH',             # 15
        'ED6_DT07/CH00340 ._CH',             # 16
        'ED6_DT07/CH00341 ._CH',             # 17
        'ED6_DT07/CH00344 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH01610P._CP',             # 00
        'ED6_DT07/CH00440P._CP',             # 01
        'ED6_DT07/CH00441P._CP',             # 02
        'ED6_DT07/CH00444P._CP',             # 03
        'ED6_DT07/CH00100P._CP',             # 04
        'ED6_DT07/CH00101P._CP',             # 05
        'ED6_DT07/CH00112P._CP',             # 06
        'ED6_DT07/CH00111P._CP',             # 07
        'ED6_DT07/CH00150P._CP',             # 08
        'ED6_DT07/CH00151P._CP',             # 09
        'ED6_DT07/CH00160P._CP',             # 0A
        'ED6_DT07/CH00161P._CP',             # 0B
        'ED6_DT06/CH20110P._CP',             # 0C
        'ED6_DT06/CH20111P._CP',             # 0D
        'ED6_DT06/CH20104P._CP',             # 0E
        'ED6_DT07/CH01330P._CP',             # 0F
        'ED6_DT07/CH00442P._CP',             # 10
        'ED6_DT07/CH00162P._CP',             # 11
        'ED6_DT07/CH00050P._CP',             # 12
        'ED6_DT07/CH00051P._CP',             # 13
        'ED6_DT07/CH00055P._CP',             # 14
        'ED6_DT07/CH00164P._CP',             # 15
        'ED6_DT07/CH00340P._CP',             # 16
        'ED6_DT07/CH00341P._CP',             # 17
        'ED6_DT07/CH00344P._CP',             # 18
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_252",          # 00, 0
        "Function_1_275",          # 01, 1
        "Function_2_2BA",          # 02, 2
        "Function_3_2FF8",         # 03, 3
        "Function_4_3362",         # 04, 4
    )


    def Function_0_252(): pass

    label("Function_0_252")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_25E"),
        (SWITCH_DEFAULT, "loc_274"),
    )


    label("loc_25E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_271")
    OP_A2(0x53A)
    Event(0, 2)

    label("loc_271")

    Jump("loc_274")

    label("loc_274")

    Return()

    # Function_0_252 end

    def Function_1_275(): pass

    label("Function_1_275")

    OP_71(0x4, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29F")
    OP_71(0x5, 0x4)
    OP_7A(0x0, 0x2)
    OP_7A(0x1, 0x2)
    OP_7A(0x2, 0x2)
    OP_7A(0x3, 0x2)
    OP_7B()
    Jump("loc_2B4")

    label("loc_29F")

    OP_78(0xFF, 0xFF, 0xFF)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_7B()

    label("loc_2B4")

    OP_22(0x1C3, 0x1, 0x64)
    Return()

    # Function_1_275 end

    def Function_2_2BA(): pass

    label("Function_2_2BA")

    EventBegin(0x0)
    OP_6D(940, 250, 31840, 0)
    OP_6B(5000, 0)
    SetChrPos(0x106, 300, 0, -2410, 50)
    SetChrPos(0x101, 1330, 0, -2710, 50)
    SetChrPos(0x102, 60, 0, -3500, 50)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 11190, 250, 4260, 96)
    SetChrPos(0x9, 11310, 250, 5950, 96)
    SetChrPos(0xA, 12710, 250, 4560, 96)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 13330, 250, 4520, 180)
    FadeToBright(2000, 0)

    def lambda_370():
        OP_6D(7980, 250, 1980, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_370)
    WaitChrThread(0x101, 0x2)
    OP_0D()
    Fade(500)
    OP_6B(3000, 0)
    OP_6D(3350, 250, -480, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#005F找到了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F哼……\x01",
            "总算被我们追到了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E5():
        OP_67(0, 4700, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E5)

    def lambda_3FD():
        OP_6D(9830, 250, 2770, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FD)

    def lambda_415():
        OP_6B(3700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_415)
    SetChrChipByIndex(0x101, 4)

    def lambda_42A():
        OP_8E(0xFE, 0x1C3E, 0xFA, 0xFFFFFE7A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42A)
    Sleep(200)
    SetChrChipByIndex(0x106, 8)

    def lambda_44F():
        OP_8E(0xFE, 0x182E, 0xFA, 0x24E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_44F)
    Sleep(200)
    SetChrChipByIndex(0x102, 6)

    def lambda_474():
        OP_8E(0xFE, 0x1720, 0xFA, 0xFFFFFD6C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_474)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_4DE():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4DE)

    def lambda_4EC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4EC)

    def lambda_4FA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4FA)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 400)
    WaitChrThread(0x106, 0x1)
    TurnDirection(0x106, 0x8, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x8, 400)
    SetChrSubChip(0x102, 11)
    WaitChrThread(0x101, 0x3)
    OP_8F(0x8, 0x2D96, 0xFA, 0x1266, 0x7D0, 0x0)
    SetChrChipByIndex(0x8, 22)
    Sleep(300)
    SetChrChipByIndex(0x9, 22)
    SetChrChipByIndex(0xA, 1)

    ChrTalk(
        0x8,
        (
            "啊……！\x01",
            "那帮游击士！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真是缠人的家伙。\x01",
            "竟追到这里来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F你们竟然想到换装逃出城镇，\x01",
            "的确也很有一套嘛。\x02\x03",
            "但是你们最终还是难逃法网。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F你们以为谁都不会来这个遗迹，\x01",
            "看来好运再好也会到头的。\x02\x03",
            "请你们还是赶快放下武器投降，\x01",
            "然后马上放了拉赛尔博士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F现基于游击士协会规定，\x01",
            "我要将你们逮捕并拘留归案。\x02\x03",
            "虽然不能马上抓到\x01",
            "那个装模作样的蒙面混蛋……\x02\x03",
            "算了，就先拿你们充数好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "口、口出狂言！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "碍事的家伙就要消灭！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 23)

    def lambda_733():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_733)
    Sleep(50)
    SetChrChipByIndex(0xA, 2)

    def lambda_758():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_758)
    Sleep(50)
    SetChrChipByIndex(0x9, 23)

    def lambda_77D():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_77D)

    def lambda_798():
        OP_90(0xFE, 0xBB8, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_798)
    Sleep(50)

    def lambda_7B8():
        OP_90(0xFE, 0xBB8, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_7B8)
    Sleep(50)

    def lambda_7D8():
        OP_90(0xFE, 0xBB8, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7D8)
    Sleep(200)
    Battle(0x3A0, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_80B"),
        (SWITCH_DEFAULT, "loc_80E"),
    )


    label("loc_80B")

    OP_B4(0x0)
    Return()

    label("loc_80E")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_6D(11880, 250, 6260, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    AddParty(0x6, 0xFF)
    SetChrPos(0x101, 8730, 250, 6030, 108)
    SetChrPos(0x106, 8240, 250, 3640, 87)
    SetChrPos(0x102, 7230, 250, 4750, 101)
    SetChrPos(0x107, 2860, 250, -2970, 58)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)
    SetChrSubChip(0x102, 11)
    SetChrChipByIndex(0x106, 8)
    SetChrChipByIndex(0x107, 10)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 24)
    SetChrChipByIndex(0x9, 3)
    SetChrChipByIndex(0xA, 24)
    SetChrPos(0x8, 12260, 250, 4130, 268)
    SetChrPos(0x9, 12650, 250, 2620, 288)
    SetChrPos(0xA, 13120, 250, 5220, 280)
    SetChrPos(0xB, 14750, 250, 2210, 280)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#2P呜……\x01",
            "不愧是游击士……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P不过……\x01",
            "别忘了我们手上有人质！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_991():
        OP_99(0xFE, 0x3, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_991)

    def lambda_9A1():
        OP_99(0xFE, 0x3, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9A1)

    def lambda_9B1():
        OP_99(0xFE, 0x3, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9B1)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 1)
    OP_96(0x9, 0x3840, 0xFA, 0xAD2, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_9E7():
        OP_6D(12670, 250, 5070, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E7)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 22)

    def lambda_A09():
        OP_8F(0xFE, 0x38FE, 0xFA, 0x127A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A09)
    Sleep(200)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 22)

    def lambda_A33():
        OP_8F(0xFE, 0x34D0, 0xFA, 0xE42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A33)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#005F你们这些家伙！\x01",
            "还要做垂死挣扎吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F你们的目的是\x01",
            "拉赛尔博士的智慧吧。\x02\x03",
            "你们真的敢加害于他吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2P少、少啰嗦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P以为我们不敢伤害他的话，\x01",
            "你们大可以试试啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#054F烦死了……\x01",
            "你们闹够没有，投降吧！\x02\x03",
            "王国军也要出动了，\x01",
            "你们这些家伙已经无处可逃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2P……呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P哈哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#057F……有什么好笑的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P不，没什么。\x01",
            "只是觉得你们还真是单纯得可爱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2P那么……时间差不多了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x79, 0x1, 0x64)
    OP_24(0x79, 0x46)

    ChrTalk(
        0x106,
        (
            "#057F什……\x02\x03",
            "#052F……………什么！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xC, 22050, -10000, -11170, 305)
    OP_24(0x79, 0x50)

    def lambda_C4D():

        label("loc_C4D")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_C4D")

    QueueWorkItem2(0x101, 0, lambda_C4D)

    def lambda_C5E():

        label("loc_C5E")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_C5E")

    QueueWorkItem2(0x102, 0, lambda_C5E)

    def lambda_C6F():

        label("loc_C6F")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_C6F")

    QueueWorkItem2(0x106, 0, lambda_C6F)

    ChrTalk(
        0x102,
        "#016F艾丝蒂尔，危险！\x02",
    )

    CloseMessageWindow()
    OP_72(0x4, 0x4)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x4)
    OP_A1(0xC, 0x4)
    OP_B0(0x4, 0x1E)
    OP_6F(0x4, 975)

    def lambda_CBA():
        OP_6D(15860, 250, 4980, 5300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CBA)

    ChrTalk(
        0x101,
        "#005F#10A我知道！\x05\x02",
    )

    LoadEffect(0x0, "map\\\\mp003_00.eff")
    OP_24(0x79, 0x64)
    OP_48()
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x4)
    SetChrBattleFlags(0xE, 0x20)
    OP_89(0xE, 19530, 1810, -9400, 270)

    def lambda_D22():
        OP_8F(0xFE, 0x5A46, 0xFA, 0x726, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D22)
    Sleep(200)

    def lambda_D42():
        OP_8C(0xFE, 0, 20)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_D42)

    def lambda_D50():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x12C0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D50)
    Sleep(200)

    def lambda_D70():
        OP_8C(0xFE, 0, 19)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_D70)

    def lambda_D7E():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x12C0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D7E)
    Sleep(200)

    def lambda_D9E():
        OP_8C(0xFE, 0, 18)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_D9E)

    def lambda_DAC():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DAC)
    Sleep(500)

    def lambda_DCC():
        OP_6E(350, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DCC)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 12230, 1000, 1240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 10470, 1000, 1770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 10180, 1000, 3370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_E94():
        OP_96(0xFE, 0x1B58, 0xFA, 0x18BA, 0x320, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E94)
    Sleep(100)

    def lambda_EB7():
        OP_96(0xFE, 0x1414, 0xFA, 0x132E, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_EB7)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 8600, 1000, 3960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_F14():
        OP_96(0xFE, 0x1810, 0xFA, 0xAF0, 0x2BC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_F14)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 7510, 1000, 4890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 8610, 1000, 4900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 8850, 1000, 4220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 7510, 1000, 4890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sleep(100)

    def lambda_1033():
        OP_8C(0xFE, 0, 12)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1033)

    def lambda_1041():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x1068, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1041)
    Sleep(100)
    OP_70(0x4, 0x3E8)
    Sleep(100)

    def lambda_106D():
        OP_8C(0xFE, 0, 11)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_106D)

    def lambda_107B():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_107B)
    Sleep(100)

    def lambda_109B():
        OP_8C(0xFE, 0, 10)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_109B)

    def lambda_10A9():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10A9)
    Sleep(200)

    def lambda_10C9():
        OP_8C(0xFE, 355, 9)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_10C9)

    def lambda_10D7():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10D7)
    Sleep(200)

    def lambda_10F7():
        OP_8C(0xFE, 355, 8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_10F7)

    def lambda_1105():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1105)
    Sleep(200)

    def lambda_1125():
        OP_8C(0xFE, 355, 6)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1125)

    def lambda_1133():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1133)
    Sleep(200)

    def lambda_1153():
        OP_8C(0xFE, 355, 4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1153)

    def lambda_1161():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1161)
    Sleep(200)

    def lambda_1181():
        OP_8C(0xFE, 355, 3)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1181)

    def lambda_118F():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_118F)
    Sleep(200)

    def lambda_11AF():
        OP_8C(0xFE, 355, 2)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_11AF)

    def lambda_11BD():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_11BD)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 830)
    OP_70(0x4, 0x352)

    ChrTalk(
        0x101,
        "#005F#5P果然，是飞艇吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#054F#5P可恶，\x01",
            "居然有如此先进的飞行工具！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_123A():
        OP_8F(0xFE, 0x4D76, 0xFFFFF254, 0x1C84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_123A)

    def lambda_1255():
        OP_8C(0xFE, 5, 2)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1255)
    Sleep(300)

    def lambda_1268():
        OP_6D(10930, 650, 4120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1268)

    def lambda_1280():
        OP_6E(292, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1280)

    def lambda_1290():
        OP_8C(0xFE, 5, 3)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1290)

    def lambda_129E():
        OP_8F(0xFE, 0x4D76, 0xFFFFF254, 0x1C84, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_129E)
    Sleep(300)

    def lambda_12BE():
        OP_8C(0xFE, 5, 5)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_12BE)

    def lambda_12CC():
        OP_8F(0xFE, 0x4D76, 0xFFFFF254, 0x1C84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12CC)
    Sleep(1000)

    def lambda_12EC():
        OP_8C(0xFE, 5, 4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_12EC)

    def lambda_12FA():
        OP_8F(0xFE, 0x4D76, 0xFFFFF254, 0x1C84, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12FA)
    Sleep(400)

    def lambda_131A():
        OP_8C(0xFE, 5, 3)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_131A)

    def lambda_1328():
        OP_8F(0xFE, 0x4D76, 0xFFFFF254, 0x1C84, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1328)
    Sleep(400)

    def lambda_1348():
        OP_8C(0xFE, 5, 2)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1348)

    def lambda_1356():
        OP_8F(0xFE, 0x4D76, 0xFFFFF254, 0x1C84, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1356)
    Sleep(300)

    def lambda_1376():
        OP_8C(0xFE, 5, 1)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1376)

    def lambda_1384():
        OP_8F(0xFE, 0x4D76, 0xFFFFF254, 0x1C84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1384)
    Sleep(200)

    def lambda_13A4():
        OP_8F(0xFE, 0x4D76, 0xFFFFF254, 0x1C84, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_13A4)
    WaitChrThread(0xC, 0x1)

    ChrTalk(
        0x8,
        "呵呵……形势逆转了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "虽然可以在这里把你们杀光……\x01",
            "但我们还不打算和游击士协会作对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "劝你们呆在一边乖乖看着，\x01",
            "也许还能保住自己的小命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F可、可恶～！\x01",
            "明明是手下败将还敢说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（艾丝蒂尔……\x01",
            "我们就按他们说的做。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F（哎……！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F（先假装顺从，然后伺机……）\x02\x03",
            "（趁他们把老爷子运进去的瞬间，\x01",
            "我们抓住时机一口气冲过去。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F（明、明白……！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "……看来你们放弃了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呵呵……\x01",
            "这才是明智的选择嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那么，我们就告辞了。\x02",
    )

    CloseMessageWindow()

    def lambda_15AB():
        OP_6D(13430, 650, 4770, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15AB)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 15)
    Sleep(250)
    OP_96(0xA, 0x3D36, 0x44C, 0x1310, 0x514, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    OP_96(0xA, 0x431C, 0xFFFFFF88, 0x1266, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xA, 0x4)
    SetChrBattleFlags(0xA, 0x20)
    OP_89(0xA, 17180, 1000, 4710, 270)
    OP_8F(0xA, 0x48DA, 0xFFFFFF6A, 0x141E, 0x7D0, 0x0)
    SetChrChipByIndex(0x8, 15)
    Sleep(250)
    OP_8F(0x8, 0x3980, 0xFA, 0xED8, 0x7D0, 0x0)
    Sleep(100)
    OP_96(0x8, 0x3D2C, 0x44C, 0xFE6, 0x514, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    OP_96(0x8, 0x41BE, 0xFFFFFF6A, 0xE7E, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x8, 0x4)
    SetChrBattleFlags(0x8, 0x20)
    OP_89(0x8, 16830, 1000, 3710, 270)
    OP_8F(0x8, 0x4B00, 0xFFFFFF7E, 0xE9C, 0x5DC, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x9, 15)
    Sleep(500)
    TurnDirection(0x9, 0xB, 400)
    OP_44(0x106, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    LoadEffect(0x2, "map\\\\mp019_00.eff")

    ChrTalk(
        0x106,
        "#057F（就是现在……！）\x02",
    )

    CloseMessageWindow()

    def lambda_1720():
        OP_6D(15200, 250, 4740, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1720)
    SetChrPos(0x107, 4970, 250, -4350, 45)

    NpcTalk(
        0x107,
        "小女孩的声音",
        "#12A#2P#3S住、住手～！\x05\x02",
    )


    def lambda_1772():
        OP_8E(0xFE, 0x6A04, 0xFA, 0xFFFFFCB8, 0x1004, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1772)
    Sleep(50)

    def lambda_1792():
        OP_8E(0xFE, 0x6A04, 0xFA, 0xFFFFFCB8, 0x1004, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1792)
    Sleep(50)

    def lambda_17B2():
        OP_8E(0xFE, 0x6A04, 0xFA, 0xFFFFFCB8, 0x1004, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17B2)
    SetChrPos(0xD, 17450, 1200, 7800, 0)
    OP_22(0x1FA, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x107, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)
    Sleep(620)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrChipByIndex(0x9, 0)

    def lambda_1867():
        TurnDirection(0xFE, 0x107, 600)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1867)

    def lambda_1875():
        TurnDirection(0xFE, 0x107, 600)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1875)

    def lambda_1883():
        TurnDirection(0xFE, 0x107, 600)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1883)

    def lambda_1891():
        OP_94(0x0, 0xFE, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1891)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)

    def lambda_18C3():
        OP_94(0x0, 0xFE, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18C3)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)

    def lambda_18F5():
        OP_94(0x0, 0xFE, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18F5)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#052F什么！？\x02",
    )

    CloseMessageWindow()

    def lambda_193A():
        OP_6D(12830, 250, 2990, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_193A)

    def lambda_1952():
        OP_6E(270, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1952)

    def lambda_1962():
        TurnDirection(0xFE, 0x107, 600)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1962)
    Sleep(50)

    def lambda_1975():
        TurnDirection(0xFE, 0x107, 600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1975)
    Sleep(50)

    def lambda_1988():
        TurnDirection(0xFE, 0x107, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1988)
    Sleep(500)

    def lambda_199B():

        label("loc_199B")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_199B")

    QueueWorkItem2(0x101, 0, lambda_199B)

    def lambda_19AC():

        label("loc_19AC")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_19AC")

    QueueWorkItem2(0x102, 0, lambda_19AC)

    def lambda_19BD():

        label("loc_19BD")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_19BD")

    QueueWorkItem2(0x106, 0, lambda_19BD)

    def lambda_19CE():
        OP_8E(0xFE, 0x2184, 0xFA, 0xFFFFF7AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_19CE)
    Sleep(1000)

    ChrTalk(
        0x8,
        "小、小女孩！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P提妲！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#016F#1P糟了！\x01",
            "她竟然跟了过来！！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x107, 17)

    ChrTalk(
        0x107,
        (
            "#068F还、还我爷爷！\x02\x03",
            "不还的话……\x01",
            "我、我、我就要开炮了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xD, 17450, 1200, 7800, 0)
    OP_22(0x1FA, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x107, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)
    OP_99(0x107, 0x0, 0xB, 0x7D0)

    ChrTalk(
        0x8,
        "呜哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "臭、臭小鬼！\x01",
            "不要太得意忘形了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B09():
        OP_6D(11750, 250, 1440, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B09)

    def lambda_1B21():
        OP_6E(242, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1B21)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 16)
    OP_44(0x106, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0x101, 0x0)

    def lambda_1B47():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B47)

    def lambda_1B55():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B55)

    def lambda_1B63():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1B63)
    WaitChrThread(0x101, 0x2)
    LoadEffect(0x0, "map\\\\mp008_00.eff")
    Sleep(500)

    ChrTalk(
        0x107,
        "#065F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#016F#1P糟了……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F提妲！\x02",
    )

    CloseMessageWindow()

    def lambda_1BC9():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1BC9)

    ChrTalk(
        0x106,
        "#550F……嘁！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x106, 18)

    def lambda_1BEF():
        OP_6D(9360, 250, -2160, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BEF)

    def lambda_1C07():
        OP_6C(40000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1C07)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x106, 19)

    def lambda_1C21():
        OP_8E(0xFE, 0x1F7C, 0xFA, 0xFFFFFD80, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1C21)
    Sleep(200)

    def lambda_1C41():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C41)

    def lambda_1C4F():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C4F)
    WaitChrThread(0x106, 0x1)

    def lambda_1C62():
        OP_92(0xFE, 0x107, 0x1F4, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1C62)
    SetChrPos(0xD, 8580, 1000, -2130, 0)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)

    def lambda_1CBD():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1CBD)
    WaitChrThread(0x106, 0x1)
    SetChrFlags(0x107, 0x1000)
    SetChrFlags(0x107, 0x20)
    OP_51(0x107, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x107, 21)
    TurnDirection(0x107, 0x106, 0)

    def lambda_1CF3():
        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1CF3)

    def lambda_1D03():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1D03)
    WaitChrThread(0x106, 0x1)
    OP_8C(0x106, 180, 0)
    SetChrFlags(0x106, 0x20)
    OP_51(0x106, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x106, 20)

    def lambda_1D3A():
        OP_96(0xFE, 0x1F22, 0xFA, 0xFFFFF556, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1D3A)
    OP_94(0x1, 0x107, 0xB4, 0x320, 0x1F40, 0x0)
    OP_94(0x1, 0x107, 0xB4, 0x258, 0x1770, 0x0)
    OP_22(0x22B, 0x0, 0x64)
    OP_94(0x1, 0x107, 0xB4, 0x190, 0x1194, 0x0)
    OP_94(0x1, 0x107, 0xB4, 0xC8, 0xBB8, 0x0)
    OP_94(0x1, 0x107, 0xB4, 0x64, 0x5DC, 0x0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x106,
        "#056F呜……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F#4P阿加特！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F阿加特兄！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x106, 0x1000)

    def lambda_1DF2():
        OP_6B(3500, 1200)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1DF2)

    def lambda_1E02():
        OP_6D(12340, 250, 2410, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E02)

    def lambda_1E1A():
        OP_6E(312, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1E1A)
    TurnDirection(0x8, 0x9, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x8,
        (
            "喂、喂！\x01",
            "你怎能对着小孩射击！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "而且那是测试用的……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P抱、抱歉……\x01",
            "我怕飞艇会被她射下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "算了，还是赶快撤退吧！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xB, 0x4)
    TurnDirection(0x9, 0xB, 800)
    TurnDirection(0xB, 0x9, 800)

    def lambda_1EDA():
        OP_96(0xFE, 0x4376, 0xFFFFFF88, 0xC44, 0x514, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1EDA)

    def lambda_1EF8():
        OP_96(0xFE, 0x43D0, 0xFFFFFF74, 0x9F6, 0x514, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1EF8)

    def lambda_1F16():
        OP_6D(12820, 250, 1370, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1F16)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xB, 0x1)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    OP_89(0x9, 17270, 1000, 3140, 270)
    OP_89(0xB, 17360, 1000, 2550, 270)
    TurnDirection(0x9, 0xB, 0)
    TurnDirection(0xB, 0x9, 0)

    ChrTalk(
        0x101,
        "#004F啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_1F8F():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F8F)

    def lambda_1F9D():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F9D)

    def lambda_1FAB():
        OP_99(0xFE, 0x3, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1FAB)

    def lambda_1FBB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1FBB)

    ChrTalk(
        0x101,
        "#005F喂，等一下！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#068F爷、爷爷————————！\x02",
    )

    CloseMessageWindow()

    def lambda_2005():
        OP_6D(17230, 300, 5990, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2005)

    def lambda_201D():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_201D)
    Sleep(100)

    def lambda_203D():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_203D)
    Sleep(100)

    def lambda_205D():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_205D)
    Sleep(100)

    def lambda_207D():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_207D)
    Sleep(1300)

    def lambda_209D():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_209D)
    Sleep(100)

    def lambda_20BD():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_20BD)
    Sleep(100)

    def lambda_20DD():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_20DD)
    Sleep(100)

    def lambda_20FD():
        OP_8F(0xFE, 0x5A46, 0xFFFFF448, 0x726, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_20FD)
    Sleep(100)
    OP_44(0xC, 0xFF)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_71(0x4, 0x2)
    OP_66(0x0)
    SetChrPos(0xD, 31230, 250, -250, 355)
    SetChrPos(0xC, 31230, 250, -250, 355)
    OP_69(0xD, 0x0)
    OP_6A(0xD)
    OP_67(9050, 60020, -29580, 0)
    OP_6B(1560, 0)
    OP_6C(37000, 0)
    OP_6E(171, 0)
    OP_43(0xC, 0x1, 0x0, 0x3)
    OP_43(0xD, 0x1, 0x0, 0x4)
    Sleep(3500)
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)
    OP_24(0x79, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x50)
    Sleep(100)
    OP_24(0x79, 0x46)
    Sleep(100)
    OP_24(0x79, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x32)
    Sleep(100)
    OP_24(0x79, 0x28)
    Sleep(100)
    OP_24(0x79, 0x1E)
    Sleep(100)
    OP_24(0x79, 0x14)
    Sleep(100)
    OP_24(0x79, 0xA)
    Sleep(100)
    OP_23(0x79)
    OP_0D()
    OP_6A(0x0)
    ClearMapFlags(0x1)
    OP_66(0x1)
    OP_6D(13840, 500, 5330, 0)
    OP_67(0, 4990, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x101, 12850, 250, 6370, 130)
    SetChrPos(0x102, 14370, 250, 6810, 192)
    ClearChrFlags(0x106, 0x20)
    SetChrChipByIndex(0x106, 18)
    SetChrSubChip(0x106, 0)
    SetChrPos(0x106, 11040, 250, 3390, 45)
    SetChrPos(0x107, 14260, 250, 5330, 250)
    SetChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 12)
    SetChrSubChip(0x107, 0)

    def lambda_22CF():

        label("loc_22CF")

        OP_99(0xFE, 0x0, 0x4, 0x5DC)
        OP_48()
        Jump("loc_22CF")

    QueueWorkItem2(0x107, 1, lambda_22CF)
    Sleep(2000)
    OP_1D(0x53)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x107,
        "#069F#2P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F总之……\x01",
            "我们先回蔡斯吧。\x02\x03",
            "要先回协会向雾香小姐\x01",
            "报告那艘飞艇的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F嗯、嗯……\x02\x03",
            "提妲……\x01",
            "我知道你很难过……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x107, 0x1)
    OP_99(0x107, 0x0, 0x6, 0x5DC)

    def lambda_23B6():

        label("loc_23B6")

        OP_99(0xFE, 0x7, 0xA, 0x5DC)
        OP_48()
        Jump("loc_23B6")

    QueueWorkItem2(0x107, 1, lambda_23B6)
    Sleep(1000)

    ChrTalk(
        0x107,
        (
            "#069F#2P…………………………………\x02\x03",
            "……为什么……\x01",
            "为什么要把爷爷……\x02\x03",
            "太过分了……为什么……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x106)

    ChrTalk(
        0x106,
        "#053F喂，小不点。\x02",
    )

    CloseMessageWindow()

    def lambda_2462():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2462)

    def lambda_2470():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2470)
    OP_6D(13200, 250, 5060, 1000)
    OP_44(0x107, 0x1)

    ChrTalk(
        0x107,
        "#069F#2P…………？\x02",
    )

    CloseMessageWindow()

    def lambda_24AB():

        label("loc_24AB")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_24AB")

    QueueWorkItem2(0x102, 2, lambda_24AB)

    def lambda_24BC():

        label("loc_24BC")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_24BC")

    QueueWorkItem2(0x101, 2, lambda_24BC)

    def lambda_24CD():
        OP_6D(13840, 500, 5330, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24CD)

    def lambda_24E5():
        OP_6B(2780, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_24E5)
    OP_8E(0x106, 0x3462, 0xFA, 0x14AA, 0xBB8, 0x0)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 13)
    SetChrSubChip(0x106, 0)
    WaitChrThread(0x101, 0x1)
    SetChrSubChip(0x106, 0)
    Sleep(60)
    SetChrSubChip(0x106, 1)
    Sleep(60)
    SetChrSubChip(0x106, 2)
    Sleep(60)
    SetChrSubChip(0x106, 3)
    Sleep(100)
    SetChrSubChip(0x106, 4)
    Sleep(40)
    SetChrSubChip(0x106, 5)
    Sleep(40)
    SetChrSubChip(0x106, 6)
    OP_22(0xA5, 0x0, 0x64)
    SetChrSubChip(0x107, 11)
    Sleep(60)
    SetChrSubChip(0x106, 7)
    Sleep(80)
    SetChrSubChip(0x106, 8)
    Sleep(80)
    SetChrSubChip(0x106, 9)
    Sleep(80)
    SetChrSubChip(0x106, 10)
    Sleep(200)
    OP_51(0x106, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x106, 18)
    ClearChrFlags(0x106, 0x1000)
    ClearChrFlags(0x106, 0x20)
    ClearChrFlags(0x106, 0x2)
    TurnDirection(0x106, 0x107, 0)
    OP_99(0x107, 0xC, 0x12, 0x3E8)

    ChrTalk(
        0x107,
        "#065F……啊……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_99(0x107, 0x13, 0x15, 0x7D0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#004F#1P等、等一下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F我不是说过了……\x01",
            "叫你不要跟来扯我们的后腿。\x02\x03",
            "就因为你的出现，\x01",
            "我们才错过了救你爷爷的时机。\x02\x03",
            "这个责任……你打算怎么负？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F我……我……\x02\x03",
            "我……\x01",
            "没、没想到会那样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F而且还要用那么差劲的威胁方式，\x01",
            "知不知道你刚才差点没命……\x02\x03",
            "为什么就是不听大人的话？\x01",
            "我啊，在这个世界上最讨厌\x01",
            "你这种没本事却又要瞎起劲的小鬼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F……对……对……不……\x02\x03",
            "#069F……对不……起……\x02\x03",
            "呜…………\x01",
            "……呜呜呜呜…………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_27B2():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_27B2)
    OP_8E(0x101, 0x3368, 0xFA, 0x166C, 0xFA0, 0x0)
    OP_8F(0x106, 0x330E, 0xFA, 0x1342, 0xFA0, 0x0)

    ChrTalk(
        0x101,
        (
            "#005F#1P够、够了吧！\x01",
            "你怎么能说这么过分的话！？\x02\x03",
            "刚刚被掳走的\x01",
            "可是她的亲生爷爷啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F所以我才更要说。\x02\x03",
            "喂……小鬼。\x01",
            "就算哭也要给我听好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#069F……呜……呜……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F你想这样就算了吗？\x02\x03",
            "还没救出爷爷，\x01",
            "就这样打算放弃了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28DF():

        label("loc_28DF")

        OP_99(0xFE, 0x15, 0x1A, 0x708)
        OP_48()
        Jump("loc_28DF")

    QueueWorkItem2(0x107, 1, lambda_28DF)
    Sleep(200)

    def lambda_28F7():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28F7)

    ChrTalk(
        0x107,
        "#069F呜呜呜呜……（摇头摇头）\x02",
    )

    CloseMessageWindow()
    OP_44(0x107, 0x1)
    OP_99(0x107, 0x15, 0x1B, 0x5DC)

    ChrTalk(
        0x106,
        (
            "#057F就是啊……\x01",
            "别那么窝囊的，振作点！\x02\x03",
            "哭也好叫也好，\x01",
            "靠自己的双脚站起来！\x02\x03",
            "连自己都照顾不了，\x01",
            "还有什么资格去救别人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F……啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F要是做不到的话，\x01",
            "就不要来给我们添无谓的麻烦。\x02\x03",
            "像个小孩子该做的，\x01",
            "躲在被窝里哼哼唧唧地哭个够吧。\x02\x03",
            "#552F……哼，\x01",
            "那样的话我才要谢天谢地啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#561F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#561F…………………………\x01",
            "不要紧了……姐姐……\x02\x03",
            "我……\x01",
            "……自己站得起来……\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x101, 0x3322, 0xFA, 0x1824, 0x3E8, 0x0)
    Sleep(100)
    OP_8F(0x106, 0x320A, 0xFA, 0x13F6, 0x3E8, 0x0)
    Sleep(400)
    OP_99(0x107, 0x1C, 0x1F, 0x320)
    Sleep(500)

    ChrTalk(
        0x106,
        (
            "#051F哼……\x01",
            "只要有心还是做得到嘛。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x107, 32)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x107,
        (
            "#561F真的……很对不起……\x02\x03",
            "都、都是因为我，\x01",
            "才让那些坏人逃走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F傻瓜……\x01",
            "用不着道歉啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F是啊。\x01",
            "提妲你没事就好。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x107, 31)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x107,
        (
            "#067F谢谢你们……\x01",
            "艾丝蒂尔姐姐、约修亚哥哥……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x107,
        "#065F那、那个……阿加特大哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F怎么了？\x01",
            "有什么怨言直说好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#562F嗯……\x02\x03",
            "真、真的非常谢谢你。\x01",
            "在那么危险的时候救了我……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x107, 0x1F, 0x22, 0x514)
    Sleep(500)
    OP_99(0x107, 0x22, 0x1F, 0x514)
    Sleep(500)

    ChrTalk(
        0x107,
        (
            "#560F还有的是……\x01",
            "谢谢你鼓励我……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x106,
        (
            "#054F谁、谁鼓励你了！\x02\x03",
            "我只是想让\x01",
            "你这哭哭啼啼的小鬼振作一点！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x107, 35)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x107,
        "#067F呵呵……是呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#055F我说你刚刚还在哭个不停，\x01",
            "现在怎么突然笑起来了啊……！？\x02\x03",
            "真、真是喜怒无常的小鬼……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#007F你啊，真是的……\x01",
            "坦率接受人家的道谢不好吗？\x02\x03",
            "真是个爱闹别扭的家伙。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x106, 400)

    ChrTalk(
        0x102,
        (
            "#019F呵呵……\x01",
            "其实阿加特兄只是不好意思罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎呀，原～来是这样啊。\x02\x03",
            "#001F你也有可爱的一面嘛㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#053F那边黑头发的小鬼，给我闭嘴！\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Fade(500)
    OP_51(0x107, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x107, 65535)
    ClearChrFlags(0x107, 0x1000)
    ClearChrFlags(0x107, 0x20)
    ClearChrFlags(0x107, 0x2)
    OP_0D()
    OP_21()
    OP_1D(0x21)
    Sleep(500)
    TurnDirection(0x106, 0x102, 400)

    ChrTalk(
        0x106,
        (
            "#552F好了……\x01",
            "总之马上回城里吧。\x02\x03",
            "看来，那些黑衣人并不简单，\x01",
            "一定有相当强大的后台撑着。\x02\x03",
            "这样下去调查很难有所进展……\x01",
            "看来有必要和军队合作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯……知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F那我们赶快回去吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x41, 0x1, 0x400)
    OP_28(0x41, 0x1, 0x800)
    Fade(1000)
    SetChrChipByIndex(0x106, 65535)
    EventEnd(0x0)
    Return()

    # Function_2_2BA end

    def Function_3_2FF8(): pass

    label("Function_3_2FF8")

    LoadEffect(0x0, "map\\\\mp021_04.eff")

    def lambda_3012():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x1F4, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3012)
    Sleep(250)

    def lambda_3033():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3033)
    Sleep(250)

    def lambda_3054():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x5DC, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3054)
    Sleep(250)

    def lambda_3075():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3075)
    Sleep(300)

    def lambda_3096():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3096)
    Sleep(300)

    def lambda_30B7():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_30B7)
    Sleep(300)

    def lambda_30D8():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0xDAC, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_30D8)
    Sleep(250)

    def lambda_30F9():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_30F9)
    Sleep(250)

    def lambda_311A():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_311A)
    Sleep(200)

    def lambda_313B():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_313B)
    Sleep(30)

    def lambda_315C():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x2328, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_315C)
    Sleep(30)

    def lambda_317D():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x2AF8, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_317D)
    Sleep(30)

    def lambda_319E():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x32C8, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_319E)
    Sleep(30)

    def lambda_31BF():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x3A98, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_31BF)
    Sleep(30)

    def lambda_31E0():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x3E80, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_31E0)
    Sleep(30)

    def lambda_3201():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x4268, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3201)
    Sleep(40)

    def lambda_3222():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x4650, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3222)
    Sleep(50)

    def lambda_3243():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x4A38, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3243)
    Sleep(60)

    def lambda_3264():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x4E20, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3264)
    Sleep(70)

    def lambda_3285():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x5208, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3285)
    Sleep(80)

    def lambda_32A6():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x55F0, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_32A6)
    Sleep(90)

    def lambda_32C7():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x59D8, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_32C7)
    Sleep(100)

    def lambda_32E8():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x5DC0, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_32E8)
    Sleep(110)

    def lambda_3309():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x61A8, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3309)
    Sleep(120)

    def lambda_332A():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFF8AD0, 0x6590, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_332A)
    Sleep(130)

    def lambda_334B():
        OP_97(0xC, 0x1EA, 0x1C16, 0xFFFE7960, 0x6978, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_334B)
    Return()

    # Function_3_2FF8 end

    def Function_4_3362(): pass

    label("Function_4_3362")


    def lambda_3368():
        OP_6E(180, 4500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3368)

    def lambda_3378():
        OP_6B(730, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3378)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFFC18, 0x7D0, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFFC18, 0x7D0, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFFA24, 0xBB8, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFFA24, 0xFA0, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF830, 0x1388, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF830, 0x1770, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF63C, 0x1B58, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF63C, 0x1F40, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF63C, 0x2328, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF63C, 0x2710, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF63C, 0x2AF8, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF3E4, 0x2EE0, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF380, 0x32C8, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF31C, 0x36B0, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF2B8, 0x3A98, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF254, 0x3E80, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF1F0, 0x4268, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF18C, 0x4650, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF510, 0x4268, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF5D8, 0x3E80, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF6A0, 0x3A98, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF768, 0x36B0, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF830, 0x32C8, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF8F8, 0x2EE0, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFF9C0, 0x2AF8, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFFA88, 0x2710, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFFB50, 0x2328, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFFC18, 0x1F40, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFFCE0, 0x1B58, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFFDA8, 0x1770, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFFE70, 0x1388, 0x1)
    OP_97(0xD, 0x1EA, 0x1C16, 0xFFFFFF38, 0xFA0, 0x1)
    Return()

    # Function_4_3362 end

    SaveToFile()

Try(main)
