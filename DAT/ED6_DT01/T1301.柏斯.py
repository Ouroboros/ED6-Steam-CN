from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1301   ._SN',
        MapName             = 'Bose',
        Location            = 'T1301.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '士兵卡多尔斯',                         # 9
        '士兵阿萨',                             # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '魔兽',                                 # 13
        '魔兽',                                 # 14
        '魔兽',                                 # 15
        '魔兽',                                 # 16
        '魔兽',                                 # 17
        '赛尔斯特队长',                         # 18
        '赛罗斯副长',                           # 19
        '士兵迈奇',                             # 20
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT09/CH10060 ._CH',             # 01
        'ED6_DT09/CH10061 ._CH',             # 02
        'ED6_DT09/CH10062 ._CH',             # 03
        'ED6_DT09/CH10064 ._CH',             # 04
        'ED6_DT09/CH10063 ._CH',             # 05
        'ED6_DT07/CH01310 ._CH',             # 06
        'ED6_DT07/CH00150 ._CH',             # 07
        'ED6_DT07/CH00151 ._CH',             # 08
        'ED6_DT07/CH00152 ._CH',             # 09
        'ED6_DT07/CH00100 ._CH',             # 0A
        'ED6_DT07/CH00101 ._CH',             # 0B
        'ED6_DT07/CH00110 ._CH',             # 0C
        'ED6_DT07/CH00111 ._CH',             # 0D
        'ED6_DT07/CH01650 ._CH',             # 0E
        'ED6_DT06/CH20053 ._CH',             # 0F
        'ED6_DT06/CH20053 ._CH',             # 10
        'ED6_DT07/CH00330 ._CH',             # 11
        'ED6_DT07/CH00331 ._CH',             # 12
        'ED6_DT07/CH00332 ._CH',             # 13
        'ED6_DT07/CH00320 ._CH',             # 14
        'ED6_DT07/CH00321 ._CH',             # 15
        'ED6_DT07/CH00322 ._CH',             # 16
        'ED6_DT07/CH00324 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT09/CH10060P._CP',             # 01
        'ED6_DT09/CH10061P._CP',             # 02
        'ED6_DT09/CH10062P._CP',             # 03
        'ED6_DT09/CH10064P._CP',             # 04
        'ED6_DT09/CH10063P._CP',             # 05
        'ED6_DT07/CH01310P._CP',             # 06
        'ED6_DT07/CH00150P._CP',             # 07
        'ED6_DT07/CH00151P._CP',             # 08
        'ED6_DT07/CH00152P._CP',             # 09
        'ED6_DT07/CH00100P._CP',             # 0A
        'ED6_DT07/CH00101P._CP',             # 0B
        'ED6_DT07/CH00110P._CP',             # 0C
        'ED6_DT07/CH00111P._CP',             # 0D
        'ED6_DT07/CH01650P._CP',             # 0E
        'ED6_DT06/CH20053P._CP',             # 0F
        'ED6_DT06/CH20053P._CP',             # 10
        'ED6_DT07/CH00330P._CP',             # 11
        'ED6_DT07/CH00331P._CP',             # 12
        'ED6_DT07/CH00332P._CP',             # 13
        'ED6_DT07/CH00320P._CP',             # 14
        'ED6_DT07/CH00321P._CP',             # 15
        'ED6_DT07/CH00322P._CP',             # 16
        'ED6_DT07/CH00324P._CP',             # 17
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
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
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
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
        X                   = -46890,
        Z                   = -50,
        Y                   = -15230,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 196631,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2EA",          # 00, 0
        "Function_1_31F",          # 01, 1
        "Function_2_332",          # 02, 2
        "Function_3_348",          # 03, 3
        "Function_4_C04",          # 04, 4
        "Function_5_28F1",         # 05, 5
        "Function_6_2B3B",         # 06, 6
        "Function_7_2E50",         # 07, 7
    )


    def Function_0_2EA(): pass

    label("Function_0_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2FD")
    OP_A3(0x3FA)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_2FD")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_309"),
        (SWITCH_DEFAULT, "loc_31E"),
    )


    label("loc_309")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_31E")

    label("loc_31E")

    Return()

    # Function_0_2EA end

    def Function_1_31F(): pass

    label("Function_1_31F")

    OP_16(0x2, 0xFA0, 0xFFFD48B0, 0xFFFE17B8, 0x30044)
    Return()

    # Function_1_31F end

    def Function_2_332(): pass

    label("Function_2_332")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_347")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_332")

    label("loc_347")

    Return()

    # Function_2_332 end

    def Function_3_348(): pass

    label("Function_3_348")

    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    SetChrPos(0x8, -50060, 0, 12640, 0)
    SetChrPos(0x9, -50070, 450, 8800, 0)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-50200, 0, 9940, 0)
    OP_6B(3000, 0)
    OP_6C(225000, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_70(0x6, 0x64)
    OP_73(0x6)
    SetChrFlags(0x9, 0x4)
    OP_8E(0x9, 0xFFFF3CB9, 0x1C2, 0x2BE3, 0x7D0, 0x0)
    ClearChrFlags(0x9, 0x4)
    OP_4A(0x8, 255)

    ChrTalk(
        0x9,
        (
            "#1P久等了。\x01",
            "已经到交班时间了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        "啊，已经这么晚了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过我说，既然没有人通行，\x01",
            "那就没必要一直在这里站岗吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "其实我们可以整夜关着门，\x01",
            "这样不就更省事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P这是上头的决定，我们只能照办。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P之前的空贼事件就不说了，\x01",
            "最近还经常感觉到附近有骚动……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x9, 270, 400)
    Sleep(200)
    OP_8C(0x9, 0, 400)
    OP_8C(0x9, 90, 400)
    Sleep(500)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P你没听到有声音吗？\x01",
            "听！沙沙沙的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "是风吹的声音吧？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, -46050, -600, 23150, 225)
    SetChrPos(0xB, -43720, -300, 22970, 225)
    SetChrPos(0xC, -45010, -400, 25300, 225)
    SetChrPos(0xD, -44180, -500, 24380, 225)
    SetChrPos(0xE, -43420, -500, 25190, 225)
    SetChrPos(0xF, -42140, -600, 25680, 225)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    OP_20(0x5DC)
    OP_21()
    OP_22(0x193, 0x0, 0x64)

    NpcTalk(
        0xF,
        "低吟声",
        "#1P咕噜噜噜……\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x9, 45, 400)
    OP_8C(0x8, 45, 400)
    OP_1D(0x52)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)

    def lambda_795():
        OP_6B(3000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_795)

    def lambda_7A5():
        OP_6D(-47350, 0, 17130, 1700)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A5)
    Sleep(500)

    def lambda_7C2():
        OP_8E(0xFE, 0xFFFF275C, 0x0, 0x3EEE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7C2)

    def lambda_7DD():
        OP_8E(0xFE, 0xFFFF1708, 0x0, 0x401A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7DD)

    def lambda_7F8():
        OP_8E(0xFE, 0xFFFF236A, 0x0, 0x41F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7F8)

    def lambda_813():
        OP_8E(0xFE, 0xFFFF1D2A, 0x0, 0x4344, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_813)
    Sleep(100)

    def lambda_833():
        OP_8E(0xFE, 0xFFFF1884, 0x0, 0x4754, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_833)
    Sleep(100)

    def lambda_853():
        OP_8E(0xFE, 0xFFFF2374, 0x0, 0x4830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_853)
    Sleep(1000)

    def lambda_873():
        OP_6D(-49494, 0, 13760, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_873)

    def lambda_88B():
        OP_8E(0xFE, 0xFFFF4A84, 0x0, 0x3EEE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_88B)
    Sleep(150)

    def lambda_8AB():
        OP_8E(0xFE, 0xFFFF3A30, 0x0, 0x401A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8AB)
    Sleep(150)

    def lambda_8CB():
        OP_8E(0xFE, 0xFFFF444E, 0x0, 0x4330, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8CB)
    Sleep(150)

    def lambda_8EB():
        OP_8E(0xFE, 0xFFFF4052, 0x0, 0x4344, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8EB)
    Sleep(150)

    def lambda_90B():
        OP_8E(0xFE, 0xFFFF3C24, 0x0, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_90B)
    Sleep(150)

    def lambda_92B():
        OP_8E(0xFE, 0xFFFF4890, 0x0, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_92B)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 1)
    OP_43(0xB, 0x1, 0x0, 0x2)
    PlayEffect(0x12, 0xFF, 0xB, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_98C():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_98C)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 1)
    OP_43(0xA, 0x1, 0x0, 0x2)
    PlayEffect(0x12, 0xFF, 0xA, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_9E8():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_9E8)
    WaitChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 1)
    OP_43(0xD, 0x1, 0x0, 0x2)
    PlayEffect(0x12, 0xFF, 0xD, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_A44():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_A44)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 1)
    OP_43(0xC, 0x1, 0x0, 0x2)
    PlayEffect(0x12, 0xFF, 0xC, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_AA0():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_AA0)
    WaitChrThread(0xE, 0x1)
    SetChrChipByIndex(0xE, 1)
    OP_43(0xE, 0x1, 0x0, 0x2)
    PlayEffect(0x12, 0xFF, 0xE, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_AFC():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_AFC)
    WaitChrThread(0xF, 0x1)
    SetChrChipByIndex(0xF, 1)
    OP_43(0xF, 0x1, 0x0, 0x2)
    PlayEffect(0x12, 0xFF, 0xF, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_B58():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_B58)
    WaitChrThread(0xE, 0x2)
    TurnDirection(0xE, 0x8, 0)
    WaitChrThread(0x101, 0x1)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0xB4, 0x1F4, 0x3E8, 0x0)

    ChrTalk(
        0x8,
        "狼、狼群！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "喂喂，不是做梦吧！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T1311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_348 end

    def Function_4_C04(): pass

    label("Function_4_C04")

    AddParty(0x5, 0xFF)
    ClearMapFlags(0x10)
    OP_31(0x5, 0x0, 0x16)
    OP_B5(0x5, 0x0)
    OP_B5(0x5, 0x1)
    OP_B5(0x5, 0x2)
    OP_41(0x5, 0x97)
    OP_41(0x5, 0xF2)
    OP_41(0x5, 0x110)
    OP_41(0x5, 0x25E, 0x0)
    OP_41(0x5, 0x258, 0x1)
    OP_41(0x5, 0x261, 0x2)
    OP_35(0x5, 0xC8)
    OP_35(0x5, 0xC9)
    OP_36(0x5, 0xFF)
    OP_31(0x5, 0x5, 0x64)
    EventBegin(0x0)
    OP_6F(0x6, 120)
    OP_72(0x6, 0x10)
    OP_6F(0x7, 120)
    OP_72(0x7, 0x10)
    OP_6D(-49790, 450, 10030, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(4080, 0)
    OP_6C(201000, 0)
    OP_6E(262, 0)
    SetChrPos(0x106, -49160, 450, 11070, 20)
    SetChrPos(0x101, -50770, 450, 11200, 20)
    SetChrPos(0x102, -50340, 450, 10410, 20)
    SetChrPos(0x8, -52080, 0, 15480, 315)
    SetChrPos(0x9, -47500, 0, 13630, 90)
    SetChrPos(0x12, -49730, 0, 15340, 0)
    SetChrPos(0x11, -48130, 0, 14880, 45)
    SetChrChipByIndex(0x8, 20)
    SetChrChipByIndex(0x9, 20)
    SetChrChipByIndex(0x12, 20)
    SetChrChipByIndex(0x11, 17)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xA, -45600, 0, 14320, 270)
    SetChrPos(0xB, -47500, 0, 15620, 225)
    SetChrPos(0xF, -44730, 0, 19520, 225)
    SetChrPos(0xD, -47980, 0, 18190, 180)
    SetChrPos(0xC, -50380, 0, 18680, 135)
    SetChrPos(0xE, -51820, 0, 17000, 135)
    TurnDirection(0xA, 0x9, 0)
    TurnDirection(0xB, 0x11, 0)
    TurnDirection(0xF, 0x11, 0)
    TurnDirection(0xD, 0x12, 0)
    TurnDirection(0xC, 0x12, 0)
    TurnDirection(0xE, 0x8, 0)
    TurnDirection(0x12, 0xD, 0)
    SetChrChipByIndex(0xA, 1)
    SetChrChipByIndex(0xB, 1)
    SetChrChipByIndex(0xC, 1)
    SetChrChipByIndex(0xD, 1)
    SetChrChipByIndex(0xE, 1)
    SetChrChipByIndex(0xF, 1)
    OP_43(0xA, 0x1, 0x0, 0x2)
    OP_43(0xC, 0x1, 0x0, 0x2)
    OP_43(0xD, 0x1, 0x0, 0x2)
    OP_43(0xE, 0x1, 0x0, 0x2)
    OP_43(0xF, 0x1, 0x0, 0x2)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x106, 15)
    OP_43(0x11, 0x1, 0x0, 0x6)
    OP_43(0x9, 0x1, 0x0, 0x5)
    OP_43(0x12, 0x1, 0x0, 0x7)
    OP_6D(-49360, 450, 13230, 2000)

    ChrTalk(
        0x102,
        "#012F#2P狼群……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2P不、不好了！\x01",
            "我们快点去帮忙吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#053F#1P……给我回去，这里不用你们管。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(
        0x101,
        (
            "#005F#2P什、什么不用我们管！？\x02\x03",
            "你说这种话还算是个游击士吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F#1P你们别理解错了。\x01",
            "守护关所是军队的使命。\x02\x03",
            "而且这些士兵都受过严格训练，\x01",
            "他们很快就会把这群狼消灭掉的。\x02\x03",
            "你们过去帮忙也只是多余罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#2P虽、虽然这样说……\x02",
    )

    CloseMessageWindow()
    OP_A6(0x0)
    OP_44(0xF, 0x2)
    OP_44(0xB, 0x2)
    OP_4A(0x11, 1)
    OP_44(0x11, 0xFF)
    SetChrFlags(0x11, 0x20)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 19)
    OP_22(0x84, 0x0, 0x64)

    def lambda_10AC():
        OP_99(0x11, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_10AC)
    OP_93(0x11, 0xB, 0x258, 0x1B58, 0x0)

    def lambda_10CA():
        OP_99(0x11, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_10CA)
    SetChrChipByIndex(0xB, 5)
    OP_44(0xB, 0xFF)
    TurnDirection(0xB, 0x11, 0)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x20)
    PlayEffect(0x9, 0xFF, 0xFF, -47540, 1000, 15460, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_112F():
        OP_94(0x1, 0xB, 0xB4, 0x7D0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_112F)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 17)
    OP_96(0x11, 0xFFFF43FE, 0x0, 0x3A20, 0x3E8, 0x1388)
    SetChrFlags(0xB, 0x40)

    ChrTalk(
        0x11,
        (
            "他说得没错！\x01",
            "守护关所是我们军人的本分！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "小姑娘，这里不用你们操心！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 400)

    ChrTalk(
        0x101,
        "#003F#2P但、但是……\x02",
    )

    CloseMessageWindow()

    def lambda_11EC():
        OP_8E(0xFE, 0xFFFF458E, 0x0, 0x3C96, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_11EC)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 19)
    OP_22(0xC2, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(70)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(70)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1270():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1270)
    Sleep(300)

    def lambda_1283():
        OP_8C(0xFE, 160, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1283)

    def lambda_1291():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1291)
    OP_6D(-49790, 450, 10030, 1000)

    ChrTalk(
        0x106,
        "#057F#1P……嘁！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x106, 0x4)
    OP_8E(0x106, 0xFFFF3C6A, 0x122, 0x2328, 0x1B58, 0x0)
    OP_8E(0x106, 0xFFFF3B7A, 0x1C2, 0x1A9A, 0x1B58, 0x0)
    ClearChrFlags(0x106, 0x4)
    SetChrFlags(0x106, 0x80)

    ChrTalk(
        0x101,
        "#004F#1P又怎么了！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#016F#1P艾丝蒂尔，是对面！\x02\x03",
            "通往卢安那面的出口\x01",
            "好像也受到了魔兽袭击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F#1P你说什么～！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-49110, -500, -18460, 0)
    OP_6C(315000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_44(0x11, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xC, 0x20)
    ClearChrFlags(0xD, 0x20)
    ClearChrFlags(0xE, 0x20)
    ClearChrFlags(0xF, 0x20)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0xA, 1)
    SetChrChipByIndex(0xB, 1)
    SetChrChipByIndex(0xC, 1)
    SetChrChipByIndex(0xD, 1)
    SetChrChipByIndex(0xE, 1)
    SetChrChipByIndex(0xF, 2)
    SetChrChipByIndex(0x10, 1)
    SetChrPos(0xA, -45460, -500, -20310, 315)
    SetChrPos(0xB, -51540, -300, -17880, 90)
    SetChrPos(0xD, -51890, -500, -20520, 45)
    SetChrPos(0xC, -50260, -500, -20200, 45)
    SetChrPos(0xE, -48980, -500, -20950, 0)
    SetChrPos(0xF, -44270, -300, -18680, 270)
    SetChrPos(0x10, -44460, 0, -17870, 225)
    OP_43(0xA, 0x1, 0x0, 0x2)
    OP_43(0xB, 0x1, 0x0, 0x2)
    OP_43(0xC, 0x1, 0x0, 0x2)
    OP_43(0xD, 0x1, 0x0, 0x2)
    OP_43(0xE, 0x1, 0x0, 0x2)
    OP_43(0xF, 0x1, 0x0, 0x2)
    OP_43(0x10, 0x1, 0x0, 0x2)
    SetChrPos(0x13, -49160, -600, -17710, 180)
    SetChrFlags(0xF, 0x40)
    ClearChrFlags(0x106, 0x80)
    SetChrPos(0x106, -50596, 300, -9470, 0)
    SetChrPos(0x101, -50644, 0, -9440, 180)
    SetChrPos(0x102, -49430, 0, -9440, 180)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x106, 8)

    def lambda_1570():
        OP_92(0xF, 0x13, 0x8FC, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1570)
    OP_0D()
    OP_8E(0x106, 0xFFFF3F84, 0xFFFFFE0C, 0xFFFFBF6E, 0x1770, 0x0)
    SetChrChipByIndex(0x106, 9)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x106, 0x20)

    def lambda_15A9():
        OP_99(0x106, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_15A9)

    def lambda_15B9():
        OP_96(0x106, 0xFFFF459E, 0xFFFFFE0C, 0xFFFFB442, 0x708, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_15B9)

    def lambda_15D7():
        OP_96(0xF, 0xFFFF402A, 0xFFFFFE0C, 0xFFFFB7E4, 0x7D0, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_15D7)

    def lambda_15F5():
        OP_6B(2600, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15F5)
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x20)
    Sleep(350)
    SetChrFlags(0xF, 0x4)
    OP_44(0xF, 0xFF)
    OP_4A(0x106, 1)
    Sleep(100)
    OP_4B(0x106, 1)
    PlayEffect(0x9, 0xFF, 0xFF, -47725, 3000, -19196, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_166A():
        OP_99(0x106, 0x4, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_166A)
    SetChrChipByIndex(0xF, 5)
    OP_44(0xF, 0xFF)
    TurnDirection(0xF, 0x106, 0)
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x20)
    OP_8F(0xF, 0xFFFF49DA, 0xFFFFFE0C, 0xFFFFADB2, 0x4E20, 0x0)
    SetChrChipByIndex(0xE, 2)
    SetChrChipByIndex(0x10, 2)
    SetChrChipByIndex(0xA, 2)

    def lambda_16BD():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_16BD)

    def lambda_16D3():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_16D3)

    def lambda_16E9():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16E9)
    PlayEffect(0x12, 0xFF, 0xFF, -46630, -500, -21070, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xF, 0x4)

    def lambda_1739():
        OP_96(0xF, 0xFFFF4C28, 0xFFFFFE0C, 0xFFFFA966, 0x7D0, 0x2710)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1739)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
    Sleep(50)
    SetChrChipByIndex(0xB, 2)

    def lambda_176C():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_176C)
    Sleep(100)
    SetChrChipByIndex(0xD, 2)

    def lambda_178C():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_178C)
    Sleep(100)
    SetChrChipByIndex(0xC, 2)

    def lambda_17AC():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_17AC)
    OP_99(0x106, 0x0, 0x3, 0x7D0)
    OP_96(0x106, 0xFFFF3F58, 0xFFFFFE0C, 0xFFFFB5FA, 0x3E8, 0xFA0)
    SetChrChipByIndex(0x106, 7)
    ClearChrFlags(0x106, 0x20)

    def lambda_17EC():
        OP_6C(340000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17EC)
    OP_6D(-50734, 0, -10950, 2000)

    ChrTalk(
        0x101,
        "#004F#1P好、好厉害……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F看来他比传说中还要厉害呢。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(-49960, -600, -18520, 0)

    def lambda_1879():
        OP_6D(-49070, -600, -19300, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1879)
    SetChrPos(0x13, -46890, -50, -15230, 180)
    OP_0D()

    def lambda_18A3():

        label("loc_18A3")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_18A3")

    QueueWorkItem2(0xA, 2, lambda_18A3)

    def lambda_18B4():

        label("loc_18B4")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_18B4")

    QueueWorkItem2(0xB, 2, lambda_18B4)

    def lambda_18C5():

        label("loc_18C5")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_18C5")

    QueueWorkItem2(0xC, 2, lambda_18C5)

    def lambda_18D6():

        label("loc_18D6")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_18D6")

    QueueWorkItem2(0xD, 2, lambda_18D6)

    def lambda_18E7():

        label("loc_18E7")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_18E7")

    QueueWorkItem2(0xE, 2, lambda_18E7)

    def lambda_18F8():

        label("loc_18F8")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_18F8")

    QueueWorkItem2(0x10, 2, lambda_18F8)
    SetChrFlags(0x106, 0x40)
    SetChrChipByIndex(0x106, 8)

    def lambda_1913():
        OP_8E(0xFE, 0xFFFF3B84, 0xFFFFFE0C, 0xFFFFB0E6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1913)

    def lambda_192E():
        OP_96(0xFE, 0xFFFF31E8, 0xFFFFFE0C, 0xFFFFB262, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_192E)
    Sleep(100)

    def lambda_1951():
        OP_8F(0xFE, 0xFFFF3576, 0xFFFFFE0C, 0xFFFFAA2E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1951)

    def lambda_196C():
        OP_96(0xFE, 0xFFFF36D4, 0x0, 0xFFFFC248, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_196C)
    Sleep(100)

    def lambda_198F():
        OP_96(0xFE, 0xFFFF4124, 0xFFFFFE0C, 0xFFFFA81C, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_198F)

    def lambda_19AD():
        OP_96(0xFE, 0xFFFF46B0, 0xFFFFFE0C, 0xFFFFB3AC, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_19AD)

    def lambda_19CB():
        OP_8F(0xFE, 0xFFFF4606, 0xFFFFFE0C, 0xFFFFAEE8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_19CB)
    WaitChrThread(0x106, 0x1)
    SetChrChipByIndex(0x106, 7)
    OP_43(0x106, 0x1, 0x0, 0x2)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x106, 0x10, 600)
    SetChrFlags(0x106, 0x40)
    SetChrChipByIndex(0x106, 8)

    def lambda_1A1C():
        OP_96(0xFE, 0xFFFF4304, 0xFFFFFDA8, 0xFFFFB1AE, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1A1C)

    def lambda_1A3A():
        OP_96(0xFE, 0xFFFF4B4C, 0xFFFFFE0C, 0xFFFFB442, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A3A)
    Sleep(100)

    def lambda_1A5D():
        OP_8F(0xFE, 0xFFFF4E6C, 0xFFFFFE0C, 0xFFFFAD30, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A5D)

    def lambda_1A78():
        OP_96(0xFE, 0xFFFF367A, 0xFFFFFED4, 0xFFFFB85C, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A78)

    def lambda_1A96():
        OP_8F(0xFE, 0xFFFF3A58, 0xFFFFFE0C, 0xFFFFAECA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1A96)
    WaitChrThread(0x106, 0x1)
    SetChrChipByIndex(0x106, 7)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x10, 0x1)

    def lambda_1ACF():
        OP_92(0xFE, 0x106, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1ACF)

    def lambda_1AE4():
        OP_92(0xFE, 0x106, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1AE4)

    def lambda_1AF9():
        OP_96(0xFE, 0xFFFF4084, 0xFFFFFED4, 0xFFFFC112, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1AF9)
    Sleep(150)

    def lambda_1B1C():
        OP_92(0xFE, 0x106, 0xDAC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B1C)
    Sleep(150)

    def lambda_1B36():
        OP_92(0xFE, 0x106, 0xDAC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B36)
    Sleep(150)

    def lambda_1B50():
        OP_92(0xFE, 0x106, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1B50)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x10, 0x1)

    def lambda_1B83():
        OP_94(0x1, 0xFE, 0x64, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1B83)
    Sleep(200)

    def lambda_1B9E():
        OP_94(0x1, 0xFE, 0x64, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1B9E)
    Sleep(100)

    def lambda_1BB9():
        OP_94(0x1, 0xFE, 0x64, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1BB9)

    def lambda_1BCF():
        OP_94(0x1, 0xFE, 0x64, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1BCF)
    Sleep(100)

    def lambda_1BEA():
        OP_94(0x1, 0xFE, 0x64, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1BEA)
    Sleep(200)

    def lambda_1C05():
        OP_94(0x1, 0xFE, 0x64, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1C05)
    Sleep(100)

    def lambda_1C20():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1C20)

    def lambda_1C36():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C36)
    Sleep(100)

    def lambda_1C51():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1C51)
    Sleep(200)

    def lambda_1C6C():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1C6C)
    Sleep(100)

    def lambda_1C87():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C87)
    Sleep(200)

    def lambda_1CA2():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1CA2)
    OP_8C(0x106, 135, 400)

    ChrTalk(
        0x106,
        (
            "#051F哈～想夹击我吗？\x02\x03",
            "一群光使蛮劲的野狗，\x01",
            "偶尔也会动动脑筋嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "……我们来帮忙了！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)

    def lambda_1D4C():
        OP_8E(0x101, 0xFFFF4426, 0xFFFFFED4, 0xFFFFBF32, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D4C)
    Sleep(300)

    def lambda_1D6C():
        OP_8E(0x102, 0xFFFF4426, 0xFFFFFED4, 0xFFFFBF32, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D6C)
    WaitChrThread(0x101, 0x1)

    def lambda_1D8C():
        OP_96(0x101, 0xFFFF3F9E, 0xFFFFFD80, 0xFFFFB3D4, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D8C)
    WaitChrThread(0x102, 0x1)

    def lambda_1DAF():
        OP_96(0x102, 0xFFFF4372, 0xFFFFFE0C, 0xFFFFB5FA, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DAF)

    def lambda_1DCD():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1DCD)
    Sleep(100)

    def lambda_1DE8():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1DE8)

    def lambda_1DFE():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1DFE)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1E1E():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E1E)
    Sleep(50)

    def lambda_1E31():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1E31)

    def lambda_1E47():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E47)
    Sleep(100)

    def lambda_1E62():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1E62)
    WaitChrThread(0x102, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1E82():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1E82)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#054F喂！谁叫你们过来的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嘿嘿～～\x01",
            "我们想过来就过来的啦☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F我们不会给你添麻烦的，\x01",
            "让我们和你一起并肩作战吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F哼，随你们吧……\x02\x03",
            "#054F不过你们要注意了，\x01",
            "我的『重剑』可是不长眼的！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F9F():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1F9F)

    def lambda_1FB5():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1FB5)
    Sleep(100)

    def lambda_1FD0():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1FD0)
    Sleep(50)

    def lambda_1FEB():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1FEB)

    def lambda_2001():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2001)
    Sleep(100)

    def lambda_201C():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_201C)
    Sleep(200)
    Battle(0x396, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_204A"),
        (SWITCH_DEFAULT, "loc_204D"),
    )


    label("loc_204A")

    OP_B4(0x0)
    Return()

    label("loc_204D")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_31(0x5, 0x0, 0x18)
    OP_41(0x5, 0xF3)
    OP_41(0x5, 0x111)
    OP_6B(3000, 0)
    SetChrPos(0x101, -49970, -650, -18800, 315)
    SetChrPos(0x102, -47880, -430, -19000, 45)
    SetChrPos(0x106, -48850, -540, -20000, 180)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x106, 15)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)

    ChrTalk(
        0x101,
        (
            "#501F呼……\x01",
            "终于击败它们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯，它们数目众多，\x01",
            "而且都是很难缠的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F……………………………\x02\x03",
            "#053F哼……\x01",
            "看来你们也没有想象中那么没用。\x02\x03",
            "毕竟是继承了大叔的真传，\x01",
            "这点水平还是应该有的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2234():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2234)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(
        0x101,
        "#004F啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 0, 400)

    ChrTalk(
        0x106,
        (
            "#050F别搞错了。\x01",
            "你们始终还是新人。\x02\x03",
            "离正游击士还差得远啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 6)
    SetChrChipByIndex(0x12, 14)
    SetChrPos(0x11, -50620, 450, -7940, 0)
    SetChrPos(0x12, -49390, 450, -8010, 0)
    ClearChrFlags(0x11, 0x20)
    ClearChrFlags(0x12, 0x20)

    ChrTalk(
        0x11,
        (
            "喂——！\x01",
            "你们那边没事吧！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_234D():
        OP_6D(-49756, -300, -16490, 2000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_234D)

    def lambda_2365():
        OP_8E(0xFE, 0xFFFF3B7A, 0x0, 0xFFFFC630, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2365)
    Sleep(500)

    def lambda_2385():
        OP_8E(0xFE, 0xFFFF3F9E, 0x0, 0xFFFFC824, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2385)

    def lambda_23A0():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23A0)

    def lambda_23AE():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23AE)

    def lambda_23BC():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_23BC)
    WaitChrThread(0x11, 0x1)

    ChrTalk(
        0x106,
        (
            "#050F#3P啊，没问题。\x01",
            "把它们杀个片甲不留了。\x02\x03",
            "刚才那个晕倒的士兵怎样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "还好没什么大碍。\x01",
            "这次幸好有你在这里帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "真不愧是『重剑阿加特』啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F#3P也没什么大不了的。\x02\x03",
            "#053F而且……\x01",
            "这两个小鬼也帮了我不少忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "是这样啊……\x01",
            "小姑娘，太谢谢你们啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "为了安全起见，\x01",
            "我们还要继续在这周围巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "你们大概都有点累了，\x01",
            "回到休息室好好睡一觉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#051F啊啊，你们也小心点。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 45, 400)

    def lambda_261E():
        OP_8E(0xFE, 0xFFFF3C60, 0x1C2, 0xFFFFE2B4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_261E)
    Sleep(500)
    OP_8C(0x12, 45, 400)

    def lambda_2645():
        OP_8E(0xFE, 0xFFFF3C60, 0x1C2, 0xFFFFE2B4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2645)
    WaitChrThread(0x11, 0x1)
    SetChrFlags(0x11, 0x80)
    WaitChrThread(0x12, 0x1)
    SetChrFlags(0x12, 0x80)

    def lambda_2674():

        label("loc_2674")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_2674")

    QueueWorkItem2(0x101, 1, lambda_2674)

    def lambda_2685():

        label("loc_2685")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_2685")

    QueueWorkItem2(0x102, 1, lambda_2685)
    OP_6D(-49340, -600, -17500, 1000)

    ChrTalk(
        0x106,
        (
            "#050F我要回去接着睡了。\x02\x03",
            "危险已经排除了，\x01",
            "你们也快点回去睡觉吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8E(0x106, 0xFFFF3C60, 0x1C2, 0xFFFFE2B4, 0xBB8, 0x0)
    SetChrFlags(0x106, 0x80)
    OP_63(0x101)
    OP_63(0x102)
    OP_44(0x101, 0x1)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F怎、怎么回事？\x02\x03",
            "那个刀子嘴\x01",
            "这次竟然表扬我们呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0x1)
    TurnDirection(0x102, 0x101, 300)

    ChrTalk(
        0x102,
        (
            "#010F也许，他或多或少\x01",
            "开始承认我们两个的能力了吧。\x02\x03",
            "其实他也不是那种不近人情的人，\x01",
            "只不过是性格比较直率而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呼……\x01",
            "其实是率直过头了吧。\x02\x03",
            "#006F……不过话说回来，\x01",
            "那家伙也有相当可爱的一面。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_22(0xD, 0x0, 0x64)
    SetMapFlags(0x100000)
    Sleep(3000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T1310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_C04 end

    def Function_5_28F1(): pass

    label("Function_5_28F1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3A")
    OP_93(0x9, 0xA, 0x258, 0x1388, 0x0)
    OP_94(0x1, 0xA, 0xB4, 0x3E8, 0x1388, 0x0)

    def lambda_291D():
        OP_8F(0xFE, 0xFFFF4DE0, 0x0, 0x37F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_291D)

    def lambda_2938():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2938)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xA, 0xFFFF4674, 0x0, 0x353E, 0x7D0, 0x1770)
    TurnDirection(0xA, 0x9, 0)
    TurnDirection(0x9, 0xA, 800)
    Sleep(1000)

    def lambda_2975():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2975)

    def lambda_298B():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_298B)
    WaitChrThread(0x9, 0x2)
    WaitChrThread(0xA, 0x2)
    Sleep(700)
    SetChrChipByIndex(0xA, 2)

    def lambda_29B5():
        OP_94(0x1, 0xFE, 0x0, 0x640, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_29B5)

    def lambda_29CB():
        OP_94(0x1, 0xFE, 0x0, 0x640, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_29CB)
    WaitChrThread(0x9, 0x2)
    WaitChrThread(0xA, 0x2)
    OP_22(0x22B, 0x0, 0x64)
    SetChrChipByIndex(0xA, 1)

    def lambda_29F5():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_29F5)

    def lambda_2A0B():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2A0B)
    Sleep(600)

    def lambda_2A26():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2A26)

    def lambda_2A3C():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2A3C)
    Sleep(200)

    def lambda_2A57():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2A57)

    def lambda_2A6D():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2A6D)
    Sleep(200)

    def lambda_2A88():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2A88)

    def lambda_2A9E():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2A9E)
    Sleep(200)

    def lambda_2AB9():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2AB9)

    def lambda_2ACF():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2ACF)
    Sleep(200)

    def lambda_2AEA():
        OP_8F(0xFE, 0xFFFF4674, 0x0, 0x353E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2AEA)

    def lambda_2B05():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2B05)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xA, 0xFFFF4DE0, 0x0, 0x37F0, 0x7D0, 0x1770)
    TurnDirection(0xA, 0x9, 0)
    TurnDirection(0x9, 0xA, 800)
    Jump("Function_5_28F1")

    label("loc_2B3A")

    Return()

    # Function_5_28F1 end

    def Function_6_2B3B(): pass

    label("Function_6_2B3B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E4F")
    SetChrFlags(0x11, 0x20)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 19)

    def lambda_2B5F():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2B5F)

    def lambda_2B75():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2B75)
    Sleep(200)

    def lambda_2B90():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2B90)

    def lambda_2BA6():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2BA6)
    Sleep(200)

    def lambda_2BC1():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2BC1)

    def lambda_2BD7():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2BD7)
    Sleep(200)

    def lambda_2BF2():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2BF2)

    def lambda_2C08():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2C08)
    Sleep(200)

    def lambda_2C23():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2C23)

    def lambda_2C39():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2C39)
    Sleep(200)

    def lambda_2C54():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2C54)

    def lambda_2C6A():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2C6A)
    Sleep(200)

    def lambda_2C85():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2C85)

    def lambda_2C9B():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2C9B)
    Sleep(500)
    OP_A3(0x0)
    SetChrChipByIndex(0xF, 2)

    def lambda_2CBE():
        OP_94(0x1, 0xFE, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2CBE)
    Sleep(500)
    WaitChrThread(0xF, 0x2)

    def lambda_2CDE():
        OP_96(0xFE, 0xFFFF4F84, 0x0, 0x4326, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2CDE)
    OP_44(0xF, 0x1)
    OP_44(0xB, 0x1)
    OP_99(0x11, 0x1, 0x3, 0xBB8)
    SetChrChipByIndex(0xB, 5)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x20)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_2D27():
        OP_99(0x11, 0x3, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2D27)

    def lambda_2D37():
        OP_8F(0xFE, 0xFFFF43FE, 0x0, 0x3A20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2D37)

    def lambda_2D52():
        OP_8F(0xFE, 0xFFFF5146, 0x0, 0x4C40, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2D52)
    WaitChrThread(0xF, 0x2)

    def lambda_2D72():
        OP_96(0xFE, 0xFFFF4674, 0x0, 0x3D04, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2D72)
    WaitChrThread(0xB, 0x2)
    SetChrChipByIndex(0xB, 1)
    WaitChrThread(0xF, 0x2)
    SetChrChipByIndex(0xF, 1)
    SetChrPos(0xB, -47500, 0, 15620, 225)
    SetChrPos(0xF, -44730, 0, 19520, 225)

    def lambda_2DC6():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2DC6)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 19)
    OP_94(0x1, 0x11, 0xB4, 0x1F4, 0x1770, 0x0)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 17)
    OP_43(0xB, 0x1, 0x0, 0x2)
    OP_43(0xF, 0x1, 0x0, 0x2)
    OP_A2(0x0)
    OP_43(0x11, 0x2, 0x0, 0x2)
    Sleep(500)
    Sleep(1000)

    def lambda_2E2D():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2E2D)
    OP_94(0x1, 0x11, 0x0, 0x1F4, 0xFA0, 0x0)
    Jump("Function_6_2B3B")

    label("loc_2E4F")

    Return()

    # Function_6_2B3B end

    def Function_7_2E50(): pass

    label("Function_7_2E50")

    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0x12, 0x40)

    def lambda_2E6A():

        label("loc_2E6A")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2E6A")

    QueueWorkItem2(0x8, 0, lambda_2E6A)

    def lambda_2E7B():

        label("loc_2E7B")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2E7B")

    QueueWorkItem2(0xE, 0, lambda_2E7B)

    label("loc_2E86")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31FD")
    OP_22(0x227, 0x0, 0x64)

    def lambda_2E9A():
        OP_93(0xFE, 0x8, 0x258, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2E9A)

    def lambda_2EAF():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2EAF)
    SetChrChipByIndex(0xD, 2)
    OP_93(0xD, 0x12, 0x258, 0x1770, 0x0)
    SetChrChipByIndex(0xD, 1)
    OP_94(0x1, 0x12, 0xB4, 0x1F4, 0x1388, 0x0)
    Sleep(200)
    OP_94(0x1, 0x12, 0x0, 0x1F4, 0x1388, 0x0)

    def lambda_2F00():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2F00)

    def lambda_2F16():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2F16)

    def lambda_2F2C():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2F2C)

    def lambda_2F42():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2F42)
    Sleep(500)

    def lambda_2F5D():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2F5D)

    def lambda_2F73():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2F73)
    Sleep(500)

    def lambda_2F8E():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2F8E)

    def lambda_2FA4():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2FA4)
    Sleep(500)
    OP_44(0x8, 0x2)

    def lambda_2FC3():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2FC3)
    OP_22(0xCB, 0x0, 0x64)
    OP_96(0x8, 0xFFFF3B20, 0x0, 0x40D8, 0x258, 0x1770)
    WaitChrThread(0xC, 0x2)

    def lambda_2FFA():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2FFA)

    def lambda_3010():
        OP_92(0xFE, 0x8, 0x12C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3010)
    Sleep(150)
    OP_96(0x8, 0xFFFF347C, 0x0, 0x4236, 0x3E8, 0x1770)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_3046():
        TurnDirection(0xFE, 0xE, 800)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3046)
    TurnDirection(0xE, 0x8, 800)
    OP_92(0x8, 0xE, 0x258, 0x1388, 0x0)
    OP_22(0x227, 0x0, 0x64)
    OP_94(0x1, 0xE, 0xB4, 0x3E8, 0x1388, 0x0)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0xE, 0x2)

    def lambda_3087():
        OP_8F(0xFE, 0xFFFF3490, 0x0, 0x3C78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3087)

    def lambda_30A2():
        OP_8E(0xFE, 0xFFFF3706, 0x0, 0x4268, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_30A2)

    def lambda_30BD():
        OP_93(0xFE, 0x12, 0x9C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_30BD)
    SetChrChipByIndex(0xC, 2)
    Sleep(1700)

    def lambda_30DC():
        OP_93(0xFE, 0x12, 0x258, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_30DC)
    OP_22(0x22A, 0x0, 0x64)
    OP_44(0xD, 0x1)
    SetChrChipByIndex(0xD, 5)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x20)

    def lambda_310F():
        OP_8F(0xFE, 0xFFFF4494, 0x0, 0x470E, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_310F)

    def lambda_312A():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_312A)

    def lambda_3140():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3140)

    def lambda_3156():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3156)
    WaitChrThread(0xD, 0x2)
    SetChrChipByIndex(0xD, 1)
    ClearChrFlags(0xD, 0x20)
    OP_43(0xD, 0x1, 0x0, 0x2)
    WaitChrThread(0xC, 0x2)
    OP_22(0x22B, 0x0, 0x64)
    OP_44(0xC, 0x1)
    SetChrChipByIndex(0xC, 5)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x20)

    def lambda_31A5():
        OP_8F(0xFE, 0xFFFF3B34, 0x0, 0x48F8, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_31A5)

    def lambda_31C0():
        OP_8F(0xFE, 0xFFFF3DBE, 0x0, 0x3BEC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_31C0)
    WaitChrThread(0xC, 0x2)
    SetChrChipByIndex(0xC, 1)
    ClearChrFlags(0xC, 0x20)
    OP_43(0xC, 0x1, 0x0, 0x2)
    WaitChrThread(0x12, 0x2)
    WaitChrThread(0xC, 0x2)
    WaitChrThread(0xD, 0x2)
    Jump("loc_2E86")

    label("loc_31FD")

    Return()

    # Function_7_2E50 end

    SaveToFile()

Try(main)
