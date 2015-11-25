from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4253   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4253.x',
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
        '特务兵',                               # 9
        '特务兵',                               # 10
        '特务兵',                               # 11
        '特务兵',                               # 12
        '特务兵',                               # 13
        '尤莉亚中尉',                           # 14
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02230 ._CH',             # 01
        'ED6_DT07/CH02240 ._CH',             # 02
        'ED6_DT07/CH01330 ._CH',             # 03
        'ED6_DT07/CH00340 ._CH',             # 04
        'ED6_DT07/CH00344 ._CH',             # 05
        'ED6_DT07/CH00110 ._CH',             # 06
        'ED6_DT07/CH00111 ._CH',             # 07
        'ED6_DT07/CH00170 ._CH',             # 08
        'ED6_DT07/CH00171 ._CH',             # 09
        'ED6_DT07/CH00130 ._CH',             # 0A
        'ED6_DT07/CH00131 ._CH',             # 0B
        'ED6_DT07/CH02090 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH01330P._CP',             # 03
        'ED6_DT07/CH00340P._CP',             # 04
        'ED6_DT07/CH00344P._CP',             # 05
        'ED6_DT07/CH00110P._CP',             # 06
        'ED6_DT07/CH00111P._CP',             # 07
        'ED6_DT07/CH00170P._CP',             # 08
        'ED6_DT07/CH00171P._CP',             # 09
        'ED6_DT07/CH00130P._CP',             # 0A
        'ED6_DT07/CH00131P._CP',             # 0B
        'ED6_DT07/CH02090P._CP',             # 0C
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_1D2",          # 00, 0
        "Function_1_275",          # 01, 1
        "Function_2_28F",          # 02, 2
        "Function_3_2A5",          # 03, 3
        "Function_4_3FE",          # 04, 4
    )


    def Function_0_1D2(): pass

    label("Function_0_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FC")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_1FC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_208"),
        (SWITCH_DEFAULT, "loc_21E"),
    )


    label("loc_208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21B")
    OP_A2(0x661)
    Event(0, 4)

    label("loc_21B")

    Jump("loc_21E")

    label("loc_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_245")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 74910, 0, -38410, 99)
    OP_43(0xD, 0x0, 0x0, 0x2)
    Jump("loc_274")

    label("loc_245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_24F")
    Jump("loc_274")

    label("loc_24F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_259")
    Jump("loc_274")

    label("loc_259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_263")
    Jump("loc_274")

    label("loc_263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_26D")
    Jump("loc_274")

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_274")

    label("loc_274")

    Return()

    # Function_0_1D2 end

    def Function_1_275(): pass

    label("Function_1_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_285")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_285")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_275 end

    def Function_2_28F(): pass

    label("Function_2_28F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_28F")

    label("loc_2A4")

    Return()

    # Function_2_28F end

    def Function_3_2A5(): pass

    label("Function_3_2A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_33F")

    ChrTalk(
        0xD,
        (
            "#178F这次的事情让我深刻体会到\x01",
            "自己还远远没有成熟。\x02\x03",
            "卡西乌斯上校也回来了。\x01",
            "为了不再辱没亲卫队的名声，\x01",
            "我更要借此机会身心兼顾地认真修炼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FA")

    label("loc_33F")

    OP_A2(0x0)

    ChrTalk(
        0xD,
        (
            "#176F呼～\x01",
            "终于又回到这里来了……\x02\x03",
            "这次的事情让我深刻体会到\x01",
            "自己还远远没有成熟。\x02\x03",
            "#178F卡西乌斯上校也回来了。\x01",
            "为了不再辱没亲卫队的名声，\x01",
            "我更要借此机会身心兼顾地认真修炼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FA")

    TalkEnd(0xFE)
    Return()

    # Function_3_2A5 end

    def Function_4_3FE(): pass

    label("Function_4_3FE")

    EventBegin(0x0)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x108, 8)
    SetChrChipByIndex(0x104, 10)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x102, 66560, 0, -30890, 186)
    SetChrPos(0x108, 65640, 0, -29760, 182)
    SetChrPos(0x104, 67130, 0, -29550, 172)
    SetChrPos(0x8, 68760, 0, -39520, 135)
    SetChrPos(0x9, 69890, 0, -40660, 315)
    SetChrPos(0xA, 65810, 0, -43750, 270)
    SetChrPos(0xB, 65730, 0, -41730, 214)
    SetChrPos(0xC, 63940, 0, -43580, 111)
    OP_6D(68190, 0, -42370, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_6D(67700, 0, -42570, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)

    def lambda_539():
        OP_6D(66270, 0, -37030, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_539)

    def lambda_551():
        OP_6E(300, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_551)

    def lambda_561():
        OP_67(0, 5550, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_561)

    def lambda_579():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_579)
    Sleep(100)

    def lambda_58C():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_58C)
    Sleep(100)

    def lambda_59F():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_59F)
    Sleep(100)

    def lambda_5B2():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5B2)
    Sleep(100)

    def lambda_5C5():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5C5)
    WaitChrThread(0x0, 0x1)

    ChrTalk(
        0x8,
        "啊……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 4)
    Sleep(100)
    SetChrChipByIndex(0xA, 4)
    SetChrChipByIndex(0xB, 4)
    Sleep(100)
    SetChrChipByIndex(0x9, 4)
    SetChrChipByIndex(0xC, 4)

    ChrTalk(
        0x9,
        "岂有此理，是侵入者！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F被侵入的一方\x01",
            "肯定是会这么说的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F用不着和他们解释什么的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……我们上！\x02",
    )

    CloseMessageWindow()

    def lambda_694():
        OP_8E(0xFE, 0x10252, 0x0, 0xFFFF33AA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_694)

    def lambda_6AF():
        OP_8E(0xFE, 0x10252, 0x0, 0xFFFF33AA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_6AF)

    def lambda_6CA():
        OP_8E(0xFE, 0x10252, 0x0, 0xFFFF33AA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6CA)

    def lambda_6E5():
        OP_6D(65930, 0, -40190, 800)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6E5)

    def lambda_6FD():
        OP_6E(225, 800)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6FD)
    Sleep(500)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x104, 0xFF)
    Battle(0x3A9, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_731"),
        (SWITCH_DEFAULT, "loc_734"),
    )


    label("loc_731")

    OP_B4(0x0)
    Return()

    label("loc_734")

    EventBegin(0x0)
    OP_6D(68410, 0, -39770, 0)
    OP_6E(309, 0)
    SetChrPos(0x102, 69140, 0, -41420, 217)
    SetChrPos(0x108, 66620, 0, -39440, 188)
    SetChrPos(0x104, 69070, 0, -39370, 233)
    SetChrPos(0x8, 64750, 0, -43440, 203)
    SetChrPos(0x9, 66130, 0, -44420, 111)
    SetChrPos(0xA, 65480, 0, -42510, 0)
    SetChrPos(0xB, 67860, 0, -42520, 0)
    SetChrPos(0xC, 66830, 0, -45880, 180)
    Sleep(500)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    OP_51(0x104, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x104, 65535)
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x108, 65535)

    def lambda_813():

        label("loc_813")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_813")

    QueueWorkItem2(0x108, 1, lambda_813)

    ChrTalk(
        0x108,
        "#070F好的，先胜一局。\x02",
    )

    CloseMessageWindow()

    def lambda_847():

        label("loc_847")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_847")

    QueueWorkItem2(0x104, 1, lambda_847)

    ChrTalk(
        0x104,
        "#030F哎呀，真不过瘾啊。\x02",
    )

    CloseMessageWindow()

    def lambda_87E():
        OP_8E(0xFE, 0x120CA, 0x0, 0xFFFF5BDC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_87E)
    OP_6D(70990, 0, -40680, 2000)
    OP_44(0x108, 0xFF)
    OP_44(0x104, 0xFF)

    ChrTalk(
        0x102,
        (
            "#010F现在我就开始操作\x01",
            "城门的开关装置！\x02\x03",
            "如果敌人来了请将其击退！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F噢，没问题！\x02\x03",
            "我以『不动』之名保证，\x01",
            "不让任何人攻入！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x108, 8)
    OP_8C(0x108, 270, 400)
    SetChrChipByIndex(0x104, 10)

    ChrTalk(
        0x104,
        (
            "#030F呵呵，此刻就是\x01",
            "天上之门打开之时了……\x02\x03",
            "……最终的乐章奏响了！\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4E, 0x4, 0x2)
    OP_28(0x4E, 0x4, 0x4)
    OP_28(0x4E, 0x1, 0x1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_3FE end

    SaveToFile()

Try(main)
