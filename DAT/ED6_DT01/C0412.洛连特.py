from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'C0412   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0412.x',
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
        '鲁克',                                 # 9
        '帕特',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '魔兽',                                 # 13
        '魔兽',                                 # 14
        '魔兽',                                 # 15
        '魔兽',                                 # 16
        '卡西乌斯',                             # 17
        '卡西乌斯',                             # 18
        '卡西乌斯',                             # 19
        '卡西乌斯',                             # 20
        '卡西乌斯',                             # 21
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
        'ED6_DT07/CH01160 ._CH',             # 00
        'ED6_DT07/CH01060 ._CH',             # 01
        'ED6_DT09/CH10020 ._CH',             # 02
        'ED6_DT09/CH10021 ._CH',             # 03
        'ED6_DT07/CH02000 ._CH',             # 04
        'ED6_DT07/CH00100 ._CH',             # 05
        'ED6_DT07/CH00101 ._CH',             # 06
        'ED6_DT07/CH00110 ._CH',             # 07
        'ED6_DT07/CH00111 ._CH',             # 08
        'ED6_DT07/CH00112 ._CH',             # 09
        'ED6_DT07/CH00102 ._CH',             # 0A
        'ED6_DT09/CH10160 ._CH',             # 0B
        'ED6_DT09/CH10161 ._CH',             # 0C
        'ED6_DT06/CH20031 ._CH',             # 0D
        'ED6_DT09/CH10070 ._CH',             # 0E
        'ED6_DT09/CH10071 ._CH',             # 0F
        'ED6_DT09/CH10040 ._CH',             # 10
        'ED6_DT09/CH10041 ._CH',             # 11
        'ED6_DT09/CH10150 ._CH',             # 12
        'ED6_DT09/CH10151 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01160P._CP',             # 00
        'ED6_DT07/CH01060P._CP',             # 01
        'ED6_DT09/CH10020P._CP',             # 02
        'ED6_DT09/CH10021P._CP',             # 03
        'ED6_DT07/CH02000P._CP',             # 04
        'ED6_DT07/CH00100P._CP',             # 05
        'ED6_DT07/CH00101P._CP',             # 06
        'ED6_DT07/CH00110P._CP',             # 07
        'ED6_DT07/CH00111P._CP',             # 08
        'ED6_DT07/CH00112P._CP',             # 09
        'ED6_DT07/CH00102P._CP',             # 0A
        'ED6_DT09/CH10160P._CP',             # 0B
        'ED6_DT09/CH10161P._CP',             # 0C
        'ED6_DT06/CH20031P._CP',             # 0D
        'ED6_DT09/CH10070P._CP',             # 0E
        'ED6_DT09/CH10071P._CP',             # 0F
        'ED6_DT09/CH10040P._CP',             # 10
        'ED6_DT09/CH10041P._CP',             # 11
        'ED6_DT09/CH10150P._CP',             # 12
        'ED6_DT09/CH10151P._CP',             # 13
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 19000,
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
        X                   = 3000,
        Z                   = 0,
        Y                   = 19000,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -18100,
        Z                   = 0,
        Y                   = 110,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x31,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18020,
        Z                   = 0,
        Y                   = 10,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x32,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_322",          # 00, 0
        "Function_1_341",          # 01, 1
        "Function_2_342",          # 02, 2
        "Function_3_358",          # 03, 3
        "Function_4_2D3F",         # 04, 4
        "Function_5_2D75",         # 05, 5
        "Function_6_2DBD",         # 06, 6
        "Function_7_2E1C",         # 07, 7
        "Function_8_2E7B",         # 08, 8
        "Function_9_2EDA",         # 09, 9
    )


    def Function_0_322(): pass

    label("Function_0_322")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_32E"),
        (SWITCH_DEFAULT, "loc_340"),
    )


    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D")
    OP_A2(0x217)
    Event(0, 3)

    label("loc_33D")

    Jump("loc_340")

    label("loc_340")

    Return()

    # Function_0_322 end

    def Function_1_341(): pass

    label("Function_1_341")

    Return()

    # Function_1_341 end

    def Function_2_342(): pass

    label("Function_2_342")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_357")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_342")

    label("loc_357")

    Return()

    # Function_2_342 end

    def Function_3_358(): pass

    label("Function_3_358")

    EventBegin(0x0)
    AddParty(0x3F, 0xFF)
    AddParty(0x40, 0xFF)
    SetChrFlags(0x140, 0x80)
    SetChrFlags(0x141, 0x80)
    FadeToBright(2000, 0)
    OP_6D(20, 500, 21100, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(335000, 0)
    OP_6E(275, 0)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrPos(0x101, -680, 250, 20560, 180)
    SetChrPos(0x102, 630, 250, 20650, 180)
    SetChrPos(0x8, -3860, 0, -3700, 45)
    SetChrPos(0x9, -2850, 0, -4300, 45)
    SetChrPos(0xA, -2830, 0, 1630, 180)
    SetChrPos(0xB, -2120, 0, 2880, 209)
    SetChrPos(0xC, -1510, 0, -250, 192)
    SetChrPos(0xD, 840, 0, 1810, 201)
    SetChrPos(0xE, 1750, 0, -1350, 180)
    TurnDirection(0xA, 0x8, 0)
    TurnDirection(0xB, 0x8, 0)
    TurnDirection(0xC, 0x8, 0)
    TurnDirection(0xD, 0x8, 0)
    TurnDirection(0xE, 0x8, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_6E(262, 2500)
    OP_0D()

    NpcTalk(
        0x8,
        "鲁克的声音",
        "#1S呜哇哇哇～！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "帕特的声音",
        "#1S救、救命啊——！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【自己一口气冲进去】\x01",      # 0
            "【和约修亚一起出击】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5CC"),
        (1, "loc_105E"),
        (SWITCH_DEFAULT, "loc_1A0A"),
    )


    label("loc_5CC")

    OP_28(0x1, 0x1, 0x10)

    ChrTalk(
        0x101,
        "#005F我要进去救他们！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 5)
    Sleep(500)

    def lambda_5F3():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0xC12, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F3)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#012F艾丝蒂尔！\x02\x03",
            "#012F老是这么冲动，真拿你没办法……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 7)
    Sleep(500)

    def lambda_65A():
        OP_8E(0xFE, 0x442, 0x0, 0x2706, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_65A)
    OP_43(0xA, 0x3, 0x0, 0x2)
    Sleep(100)
    OP_43(0xB, 0x3, 0x0, 0x2)
    Sleep(200)

    def lambda_68D():
        OP_8E(0xFE, 0x442, 0x0, 0x2706, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_68D)
    OP_43(0xC, 0x3, 0x0, 0x2)
    Sleep(100)
    OP_43(0xD, 0x3, 0x0, 0x2)
    Sleep(200)
    OP_43(0xE, 0x3, 0x0, 0x2)
    Sleep(500)

    def lambda_6CC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6CC)

    def lambda_6DA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6DA)
    SetChrFlags(0x102, 0x80)
    OP_44(0x101, 0xFF)
    Fade(1000)
    OP_6D(-1550, 0, -920, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(336000, 0)
    OP_6E(306, 0)
    SetChrPos(0x101, 1090, 0, 9990, 66)

    def lambda_744():
        OP_6D(-3060, 0, -2370, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_744)

    def lambda_75C():
        OP_94(0x0, 0xFE, 0x0, 0x834, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_75C)
    Sleep(100)

    def lambda_777():
        OP_94(0x0, 0xFE, 0x0, 0x7D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_777)
    Sleep(100)

    def lambda_792():
        OP_94(0x0, 0xFE, 0x0, 0x7D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_792)

    def lambda_7A8():
        OP_94(0x0, 0xFE, 0x0, 0x834, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7A8)
    Sleep(100)

    def lambda_7C3():
        OP_94(0x0, 0xFE, 0x0, 0x578, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7C3)
    Sleep(1000)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7F0():
        OP_8F(0xFE, 0xFFFFEE8A, 0x0, 0xFFFFEE80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7F0)
    Sleep(500)
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_822():
        OP_8F(0xFE, 0xFFFFF29A, 0x0, 0xFFFFEAFC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_822)
    Sleep(1500)

    ChrTalk(
        0x8,
        "滚、滚开呀，你们这些怪物～！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呜哇哇哇～\x01",
            "不要过来啊，笨蛋——！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#10A喝啊～～！！\x05\x02",
    )

    Sleep(300)

    def lambda_8B0():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_8B0)

    def lambda_8BE():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_8BE)

    def lambda_8CC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_8CC)

    def lambda_8DA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_8DA)

    def lambda_8E8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_8E8)

    def lambda_8F6():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8F6)

    def lambda_904():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_904)
    Sleep(300)

    def lambda_917():
        OP_8E(0xFE, 0xFFFFFB6E, 0x0, 0x8F2, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_917)

    def lambda_932():
        OP_6D(-2220, 0, -1110, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_932)
    WaitChrThread(0x101, 0x1)

    def lambda_94F():

        label("loc_94F")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_94F")

    QueueWorkItem2(0xA, 2, lambda_94F)

    def lambda_960():

        label("loc_960")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_960")

    QueueWorkItem2(0xB, 2, lambda_960)

    def lambda_971():

        label("loc_971")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_971")

    QueueWorkItem2(0xC, 2, lambda_971)

    def lambda_982():

        label("loc_982")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_982")

    QueueWorkItem2(0xD, 2, lambda_982)

    def lambda_993():

        label("loc_993")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_993")

    QueueWorkItem2(0xE, 2, lambda_993)

    def lambda_9A4():

        label("loc_9A4")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_9A4")

    QueueWorkItem2(0x9, 2, lambda_9A4)

    def lambda_9B5():

        label("loc_9B5")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_9B5")

    QueueWorkItem2(0x8, 2, lambda_9B5)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 10)
    SetChrFlags(0x101, 0x1000)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_9E0():
        OP_99(0xFE, 0x0, 0xC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E0)
    OP_8C(0x101, 270, 0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x101, 0xFFFFF827, 0x0, 0xFFFFF8A8, 0x7D0, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, -2630, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_A4D():
        OP_8F(0xFE, 0xFFFFF006, 0x0, 0xFFFFF9DE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A4D)

    def lambda_A68():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A68)

    def lambda_A7E():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A7E)
    Sleep(150)

    def lambda_A99():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A99)
    Sleep(100)

    def lambda_AB4():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AB4)
    Sleep(200)

    def lambda_ACF():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_ACF)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 5)

    def lambda_AF5():
        OP_8C(0xFE, 19, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF5)

    def lambda_B03():
        OP_8F(0xFE, 0xFFFFF524, 0x0, 0xFFFFF420, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B03)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x8,
        "艾丝蒂尔姐姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F你们两个！\x01",
            "这里太危险了，快躲到旁边去！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B92():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B92)

    def lambda_BA0():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BA0)

    def lambda_BAE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_BAE)

    def lambda_BBC():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_BBC)

    def lambda_BCA():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_BCA)

    def lambda_BD8():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_BD8)

    def lambda_BE6():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BE6)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x1000)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)
    TurnDirection(0x102, 0x101, 0)
    OP_96(0x102, 0xFFFFFE8E, 0x0, 0x898, 0x3E8, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 9)
    OP_99(0x102, 0x0, 0x5, 0x9C4)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_C4F():

        label("loc_C4F")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C4F")

    QueueWorkItem2(0xA, 2, lambda_C4F)

    def lambda_C60():

        label("loc_C60")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C60")

    QueueWorkItem2(0xB, 2, lambda_C60)

    def lambda_C71():

        label("loc_C71")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C71")

    QueueWorkItem2(0xC, 2, lambda_C71)

    def lambda_C82():

        label("loc_C82")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C82")

    QueueWorkItem2(0xD, 2, lambda_C82)

    def lambda_C93():

        label("loc_C93")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C93")

    QueueWorkItem2(0xE, 2, lambda_C93)

    def lambda_CA4():

        label("loc_CA4")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_CA4")

    QueueWorkItem2(0x9, 2, lambda_CA4)

    def lambda_CB5():

        label("loc_CB5")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_CB5")

    QueueWorkItem2(0x8, 2, lambda_CB5)

    def lambda_CC6():
        OP_99(0xFE, 0x5, 0xC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CC6)

    def lambda_CD6():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0xFFFFFC72, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CD6)
    Sleep(100)

    def lambda_CF6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_CF6)
    SetChrFlags(0x102, 0x40)
    PlayEffect(0x8, 0xFF, 0xFF, -10, 500, 690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x102, 0x2)
    OP_44(0x102, 0xFF)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)

    def lambda_D5B():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D5B)
    OP_96(0x102, 0xFFFFF876, 0x0, 0xFFFFF39E, 0x1F4, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)

    ChrTalk(
        0x9,
        "是约修亚哥哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4P艾丝蒂尔……\x01",
            "知不知道自己一个人冲进来很危险的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F要训我的话等战斗结束后再说！\x02\x03",
            "来吧，一口气把这些魔兽通通收拾掉！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0x386, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_E66"),
        (SWITCH_DEFAULT, "loc_E6B"),
    )


    label("loc_E66")

    OP_B4(0x0)
    Jump("loc_E6B")

    label("loc_E6B")

    SetChrFlags(0x140, 0x80)
    SetChrFlags(0x141, 0x80)
    EventBegin(0x0)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_6D(-3150, 0, -3290, 0)
    OP_67(0, 7450, -10000, 0)
    OP_6B(1710, 0)
    OP_6E(554, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_8C(0x8, 28, 0)
    OP_8C(0x9, 28, 0)
    SetChrPos(0x101, -3210, 0, -460, 291)
    SetChrPos(0x102, -50, 0, -1270, 72)

    def lambda_F04():
        OP_6E(504, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F04)
    OP_6C(225000, 3000)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#502F大获全胜、大获全胜☆\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F真的大获全胜吗？\x02\x03",
            "还没看清情况\x01",
            "就那么莽撞地冲进来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F算了～算了。\x01",
            "我们不是打了一场漂亮的战斗嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0A")

    label("loc_105E")

    OP_28(0x1, 0x1, 0x8)
    OP_2B(0x1, 0x1)

    ChrTalk(
        0x101,
        "#005F约修亚！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F明白！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 5)
    Sleep(250)
    SetChrChipByIndex(0x102, 7)
    Sleep(250)

    def lambda_10C4():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0xC12, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10C4)
    Sleep(250)

    def lambda_10E4():
        OP_8E(0xFE, 0x442, 0x0, 0x2706, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10E4)
    OP_43(0xA, 0x3, 0x0, 0x2)
    Sleep(100)
    OP_43(0xB, 0x3, 0x0, 0x2)
    Sleep(200)

    def lambda_1117():
        OP_8E(0xFE, 0x442, 0x0, 0x2706, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1117)
    OP_43(0xC, 0x3, 0x0, 0x2)
    Sleep(100)
    OP_43(0xD, 0x3, 0x0, 0x2)
    Sleep(200)
    OP_43(0xE, 0x3, 0x0, 0x2)
    Sleep(500)

    def lambda_1156():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1156)

    def lambda_1164():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1164)
    SetChrFlags(0x102, 0x80)
    OP_44(0x101, 0xFF)
    Fade(1000)
    OP_6D(-1550, 0, -920, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(336000, 0)
    OP_6E(306, 0)
    SetChrPos(0x101, 1090, 0, 9990, 66)

    def lambda_11CE():
        OP_6D(-3060, 0, -2370, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_11CE)

    def lambda_11E6():
        OP_94(0x0, 0xFE, 0x0, 0x834, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11E6)
    Sleep(100)

    def lambda_1201():
        OP_94(0x0, 0xFE, 0x0, 0x7D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1201)
    Sleep(100)

    def lambda_121C():
        OP_94(0x0, 0xFE, 0x0, 0x7D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_121C)

    def lambda_1232():
        OP_94(0x0, 0xFE, 0x0, 0x834, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1232)
    Sleep(100)

    def lambda_124D():
        OP_94(0x0, 0xFE, 0x0, 0x578, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_124D)
    Sleep(1000)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_127A():
        OP_8F(0xFE, 0xFFFFEE8A, 0x0, 0xFFFFEE80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_127A)
    Sleep(500)
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_12AC():
        OP_8F(0xFE, 0xFFFFF29A, 0x0, 0xFFFFEAFC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12AC)
    Sleep(1500)

    ChrTalk(
        0x8,
        "滚、滚开呀，你们这些怪物～！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呜哇哇哇～\x01",
            "不要过来啊，笨蛋——！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#10A喝啊～～！！\x05\x02",
    )

    Sleep(300)

    def lambda_133A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_133A)

    def lambda_1348():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1348)

    def lambda_1356():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1356)

    def lambda_1364():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1364)

    def lambda_1372():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1372)

    def lambda_1380():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1380)

    def lambda_138E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_138E)
    Sleep(300)

    def lambda_13A1():
        OP_8E(0xFE, 0xFFFFFB6E, 0x0, 0x8F2, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13A1)

    def lambda_13BC():
        OP_6D(-2220, 0, -1110, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13BC)
    WaitChrThread(0x101, 0x1)

    def lambda_13D9():

        label("loc_13D9")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_13D9")

    QueueWorkItem2(0xA, 2, lambda_13D9)

    def lambda_13EA():

        label("loc_13EA")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_13EA")

    QueueWorkItem2(0xB, 2, lambda_13EA)

    def lambda_13FB():

        label("loc_13FB")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_13FB")

    QueueWorkItem2(0xC, 2, lambda_13FB)

    def lambda_140C():

        label("loc_140C")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_140C")

    QueueWorkItem2(0xD, 2, lambda_140C)

    def lambda_141D():

        label("loc_141D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_141D")

    QueueWorkItem2(0xE, 2, lambda_141D)

    def lambda_142E():

        label("loc_142E")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_142E")

    QueueWorkItem2(0x9, 2, lambda_142E)

    def lambda_143F():

        label("loc_143F")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_143F")

    QueueWorkItem2(0x8, 2, lambda_143F)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 10)
    SetChrFlags(0x101, 0x1000)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_146A():
        OP_99(0xFE, 0x0, 0xC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_146A)
    OP_8C(0x101, 270, 0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x101, 0xFFFFF827, 0x0, 0xFFFFF8A8, 0x7D0, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, -2630, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_14D7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_14D7)

    def lambda_14E9():
        OP_8F(0xFE, 0xFFFFF006, 0x0, 0xFFFFF9DE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_14E9)

    def lambda_1504():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1504)

    def lambda_151A():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_151A)
    Sleep(150)

    def lambda_1535():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1535)
    Sleep(100)

    def lambda_1550():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1550)
    Sleep(200)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 5)

    def lambda_157B():
        OP_8C(0xFE, 19, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_157B)

    def lambda_1589():
        OP_8F(0xFE, 0xFFFFF524, 0x0, 0xFFFFF420, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1589)

    def lambda_15A4():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15A4)

    def lambda_15B2():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_15B2)

    def lambda_15C0():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_15C0)

    def lambda_15CE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_15CE)

    def lambda_15DC():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_15DC)

    def lambda_15EA():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_15EA)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x1000)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)
    TurnDirection(0x102, 0x101, 0)
    OP_96(0x102, 0xFFFFFE8E, 0x0, 0x898, 0x3E8, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 9)
    OP_99(0x102, 0x0, 0x5, 0x9C4)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_1653():

        label("loc_1653")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1653")

    QueueWorkItem2(0xA, 2, lambda_1653)

    def lambda_1664():

        label("loc_1664")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1664")

    QueueWorkItem2(0xB, 2, lambda_1664)

    def lambda_1675():

        label("loc_1675")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1675")

    QueueWorkItem2(0xC, 2, lambda_1675)

    def lambda_1686():

        label("loc_1686")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1686")

    QueueWorkItem2(0xD, 2, lambda_1686)

    def lambda_1697():

        label("loc_1697")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1697")

    QueueWorkItem2(0xE, 2, lambda_1697)

    def lambda_16A8():

        label("loc_16A8")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_16A8")

    QueueWorkItem2(0x9, 2, lambda_16A8)

    def lambda_16B9():

        label("loc_16B9")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_16B9")

    QueueWorkItem2(0x8, 2, lambda_16B9)

    def lambda_16CA():
        OP_99(0xFE, 0x5, 0xC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_16CA)

    def lambda_16DA():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0xFFFFFC72, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16DA)
    Sleep(100)

    def lambda_16FA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_16FA)
    SetChrFlags(0x102, 0x40)
    PlayEffect(0x8, 0xFF, 0xFF, -10, 500, 690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x102, 0x2)
    OP_44(0x102, 0xFF)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)

    def lambda_175F():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_175F)
    OP_96(0x102, 0xFFFFF876, 0x0, 0xFFFFF39E, 0x1F4, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)

    ChrTalk(
        0x8,
        "艾丝蒂尔姐姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "是约修亚哥哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F你们两个！\x01",
            "这里太危险了，快躲到旁边去！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#4P我们会马上收拾它们的！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0x3B0, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1860"),
        (SWITCH_DEFAULT, "loc_1865"),
    )


    label("loc_1860")

    OP_B4(0x0)
    Jump("loc_1865")

    label("loc_1865")

    EventBegin(0x0)
    SetChrFlags(0x140, 0x80)
    SetChrFlags(0x141, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_6D(-3150, 0, -3290, 0)
    OP_67(0, 7450, -10000, 0)
    OP_6B(1710, 0)
    OP_6E(554, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_8C(0x8, 28, 0)
    OP_8C(0x9, 28, 0)
    SetChrPos(0x101, -3210, 0, -460, 291)
    SetChrPos(0x102, -50, 0, -1270, 72)

    def lambda_18FE():
        OP_6E(504, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18FE)
    OP_6C(225000, 3000)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#001F好啦，都收拾掉了。\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F嗯，大家都没事，太好了。\x02\x03",
            "#010F而且我们联合出击的时机\x01",
            "也掌握得很不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F嘿嘿，是吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A0A")

    label("loc_1A0A")


    ChrTalk(
        0x9,
        "结、结束了吗……？\x02",
    )

    CloseMessageWindow()

    def lambda_1A28():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A28)

    def lambda_1A36():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A36)

    ChrTalk(
        0x8,
        "厉害～～！\x02",
    )

    CloseMessageWindow()

    def lambda_1A63():

        label("loc_1A63")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1A63")

    QueueWorkItem2(0x8, 1, lambda_1A63)

    def lambda_1A74():

        label("loc_1A74")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1A74")

    QueueWorkItem2(0x101, 1, lambda_1A74)

    def lambda_1A85():

        label("loc_1A85")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1A85")

    QueueWorkItem2(0x102, 1, lambda_1A85)
    OP_62(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x2BC, 0x1770)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x2BC, 0x1770)
    Sleep(300)

    def lambda_1ADB():
        OP_8E(0xFE, 0xFFFFF196, 0x0, 0xFFFFF9E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1ADB)
    Sleep(300)

    def lambda_1AFB():
        OP_6D(-3440, 0, -2740, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1AFB)
    Sleep(100)

    def lambda_1B18():

        label("loc_1B18")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1B18")

    QueueWorkItem2(0x9, 1, lambda_1B18)

    def lambda_1B29():
        OP_8E(0xFE, 0xFFFFFC04, 0x0, 0xFFFFF39E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1B29)
    WaitChrThread(0x8, 0x2)
    OP_96(0x8, 0xFFFFEE6C, 0x0, 0xFFFFFBFA, 0x320, 0x1770)
    OP_96(0x8, 0xFFFFEF66, 0x0, 0xFFFFFF42, 0x4B0, 0x1770)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x8,
        "艾丝蒂尔，你还蛮厉害的嘛！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "虽然只是个小女孩，不过还真有一手啊！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F你这个笨蛋！\x02",
    )

    CloseMessageWindow()

    def lambda_1BF6():
        OP_6D(-4540, 0, -1610, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1BF6)
    SetChrFlags(0x101, 0x40)
    OP_92(0x101, 0x8, 0x190, 0x1770, 0x0)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0x8, 0xB4, 0x1F4, 0x1770, 0x0)
    Sleep(500)
    OP_8F(0x8, 0xFFFFE98A, 0x0, 0x14, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        "好疼，你干什么呀！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F真是的，你呀！\x02\x03",
            "居然把这么乖的帕特\x01",
            "都带到这种地方来……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1300)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_44(0x8, 0xFF)

    def lambda_1D1D():
        OP_8C(0xFE, 270, 800)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1D1D)

    def lambda_1D2B():
        OP_94(0x1, 0xFE, 0xB4, 0x5DC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1D2B)
    ClearChrFlags(0x101, 0x1000)
    OP_8F(0x101, 0xFFFFE5B6, 0x0, 0x10E, 0x1388, 0x0)
    SetChrFlags(0x8, 0x4)
    OP_91(0x8, 0x0, 0x64, 0x0, 0x320, 0x0)

    def lambda_1D73():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D73)
    OP_97(0x8, 0xFFFFE5B6, 0x10E, 0xFFFD40E0, 0xFA0, 0x3)

    ChrTalk(
        0x101,
        "#005F给·我·好·好·反·省！\x02",
    )

    CloseMessageWindow()

    def lambda_1DCD():
        OP_91(0xFE, 0x4B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DCD)
    OP_91(0x8, 0x4B0, 0x0, 0x0, 0x7D0, 0x0)
    OP_9E(0x8, 0x3C, 0x0, 0x12C, 0x1F40)
    OP_9E(0x8, 0x3C, 0x0, 0x12C, 0x1F40)

    ChrTalk(
        0x8,
        "疼疼疼，快住手！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "粗暴女！白痴艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F而且还用这种口气\x01",
            "对你的救命恩人说话……\x02\x03",
            "#009F看来不给你点严厉的惩罚是不行的～\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0x3C, 0x0, 0x1F4, 0x1F40)

    ChrTalk(
        0x8,
        "疼疼疼疼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔姐姐！\x01",
            "饶了我吧，都是我不好！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F5F():

        label("loc_1F5F")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_1F5F")

    QueueWorkItem2(0x8, 3, lambda_1F5F)

    ChrTalk(
        0x9,
        "#1P那、那个……姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P这样就够了吧，饶了他吧。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -16000, 0, 0, 282)

    def lambda_1FE8():
        OP_8E(0xFE, 0xFFFFD508, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1FE8)

    ChrTalk(
        0x101,
        (
            "#006F没关系的，对这样的调皮蛋来说\x01",
            "小小的惩罚反而有好处……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x1)
    TurnDirection(0xA, 0x101, 400)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x101, 0x1000)

    ChrTalk(
        0x102,
        "#016F艾丝蒂尔，后面！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0x101, 0xFF)
    ClearChrFlags(0x8, 0x4)
    TurnDirection(0x101, 0xA, 400)
    TurnDirection(0x8, 0x101, 400)

    def lambda_20F7():
        OP_6D(-6670, 0, -1080, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_20F7)

    def lambda_210F():
        OP_8E(0xFE, 0xFFFFDAE4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_210F)
    Sleep(1500)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#002F糟了……\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "battle\\\\mgblood.eff")

    ChrTalk(
        0x102,
        "#510F#4P……该死！\x02",
    )

    CloseMessageWindow()
    OP_43(0x102, 0x0, 0x0, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x11, -21000, 0, 0, 0)
    SetChrPos(0x12, -21040, 0, 0, 0)
    SetChrPos(0x13, -21040, 0, 0, 0)
    SetChrPos(0x14, -21040, 0, 0, 0)
    SetChrPos(0x10, -21040, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x10, 0x40)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x32, 0x0)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 12)

    def lambda_228E():
        OP_8E(0xA, 0xFFFFEA84, 0x0, 0x0, 0xA8C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_228E)

    def lambda_22A9():
        OP_6D(-5130, 0, -1080, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22A9)

    def lambda_22C1():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22C1)

    def lambda_22D7():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22D7)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x13, 0x2)
    SetChrFlags(0x14, 0x2)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x10, 13)
    SetChrChipByIndex(0x11, 13)
    SetChrChipByIndex(0x12, 13)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x14, 13)

    def lambda_2351():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2351)
    Sleep(100)

    def lambda_2371():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2371)
    Sleep(100)

    def lambda_2391():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2391)
    Sleep(100)

    def lambda_23B1():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_23B1)
    Sleep(100)

    def lambda_23D1():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_23D1)
    OP_20(0x3E8)
    WaitChrThread(0x10, 0x1)
    OP_43(0x11, 0x1, 0x0, 0x6)
    OP_43(0x12, 0x1, 0x0, 0x7)
    OP_43(0x13, 0x1, 0x0, 0x8)
    OP_43(0x14, 0x1, 0x0, 0x9)
    SetChrSubChip(0x10, 1)
    OP_96(0x10, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_22(0xA4, 0x0, 0x64)
    OP_43(0x10, 0x1, 0x0, 0x5)
    WaitChrThread(0xA, 0x1)
    OP_22(0x9B, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x9, 0xFF, 0xFF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xA, 0x40)

    def lambda_24F2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_24F2)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F……啊？\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x10, 400)
    Sleep(500)

    ChrTalk(
        0x102,
        "#010F太好了，终于来了。\x02",
    )

    CloseMessageWindow()

    def lambda_2553():
        OP_6C(270000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2553)

    def lambda_2563():
        OP_6D(-5500, 0, 0, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2563)
    Sleep(1300)
    SetChrSubChip(0x10, 4)
    Sleep(1200)

    def lambda_258A():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_258A)

    def lambda_2598():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2598)

    def lambda_25A6():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25A6)
    OP_1D(0x58)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#085F还是太嫩了，艾丝蒂尔。\x02\x03",
            "为了防备难以预见的威胁，\x01",
            "必须时常保持敏锐的感觉才行哦。\x02\x03",
            "#080F这也是游击士的心得。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_266F():

        label("loc_266F")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_266F")

    QueueWorkItem2(0x101, 1, lambda_266F)

    ChrTalk(
        0x101,
        (
            "#004F#4P老、老爸！？\x02\x03",
            "为、什么你会在这儿呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#080F没什么，爱娜把事情都告诉我了。\x02\x03",
            "虽然前往目的地的速度\x01",
            "和处事的判断力都相当不错……\x02\x03",
            "不过最后还是松懈了啊，知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#4P哎呀，真没面子……\x02",
    )

    CloseMessageWindow()

    def lambda_27B7():
        OP_6D(-6270, 0, 130, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_27B7)

    def lambda_27CF():

        label("loc_27CF")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_27CF")

    QueueWorkItem2(0x8, 1, lambda_27CF)

    def lambda_27E0():
        OP_8F(0xFE, 0xFFFFEED0, 0x0, 0x5FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_27E0)

    def lambda_27FB():

        label("loc_27FB")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_27FB")

    QueueWorkItem2(0x9, 1, lambda_27FB)

    def lambda_280C():
        OP_8F(0xFE, 0xFFFFF5E2, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_280C)
    OP_8E(0x102, 0xFFFFED90, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
    OP_44(0x102, 0xFF)
    OP_8C(0x102, 315, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(
        0x102,
        (
            "#013F多亏您来了，爸爸。\x02\x03",
            "对不起，有我在还发生这种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#081F啊，要做到真正保护好别人，\x01",
            "其实你也还差得远呢。\x02\x03",
            "不过再努力一下就会好很多的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#011F……嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#080F那我们回去吧。\x02\x03",
            "孩子们，还走得动吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "嗯、嗯……！\x02",
    )

    CloseMessageWindow()

    def lambda_299F():
        OP_8E(0xFE, 0xFFFFE9BC, 0x0, 0xFFFFF948, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_299F)
    Sleep(200)

    def lambda_29BF():
        OP_8E(0xFE, 0xFFFFE476, 0x0, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_29BF)

    def lambda_29DA():

        label("loc_29DA")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_29DA")

    QueueWorkItem2(0x8, 1, lambda_29DA)
    WaitChrThread(0x9, 0x1)

    def lambda_29F0():
        OP_8E(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFFBE6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_29F0)

    def lambda_2A0B():

        label("loc_2A0B")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_2A0B")

    QueueWorkItem2(0x9, 1, lambda_2A0B)
    WaitChrThread(0x9, 0x2)
    WaitChrThread(0x8, 0x2)

    ChrTalk(
        0x8,
        "太、太有型了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "卡西乌斯叔叔，\x01",
            "你比艾丝蒂尔要酷上一百倍呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#081F哈哈哈，那是当然的啦。\x02\x03",
            "好了，那我们回城镇去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嗯！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 4)
    OP_8C(0x10, 90, 0)
    OP_8C(0x10, 270, 400)

    def lambda_2B34():
        OP_8E(0xFE, 0xFFFF6D2A, 0x0, 0xFFFFFF88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2B34)
    Sleep(300)

    def lambda_2B54():
        OP_8E(0xFE, 0xFFFF6D2A, 0x0, 0xFFFFFF88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B54)
    Sleep(100)

    def lambda_2B74():
        OP_8E(0xFE, 0xFFFF6D2A, 0x0, 0xFFFFFF88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B74)

    def lambda_2B8F():
        OP_6E(471, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B8F)

    def lambda_2B9F():
        OP_6C(224000, 3000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2B9F)
    OP_6D(-6000, 0, 290, 2500)
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F#4P……唔～…………\x02\x03",
            "虽然很感谢老爸救了我们……\x02\x03",
            "可是为什么他会把\x01",
            "我的风头全都抢光了啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_8C(0x101, 45, 400)
    Sleep(500)

    ChrTalk(
        0x101,
        "#009F#5S#4P我不要啊——！\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F哈哈，这也没办法啊。\x02\x03",
            "#010F不管怎么说……\x01",
            "他可是卡西乌斯·布莱特啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_28(0x1, 0x1, 0x20)
    RemoveParty(0x3F, 0xFF)
    RemoveParty(0x40, 0xFF)
    OP_A2(0x217)
    NewScene("ED6_DT01/T0121   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_3_358 end

    def Function_4_2D3F(): pass

    label("Function_4_2D3F")

    ClearChrFlags(0x102, 0x1000)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)
    Sleep(500)

    def lambda_2D5F():
        OP_8E(0xFE, 0xFFFFF600, 0x0, 0xFFFFFC54, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D5F)
    Return()

    # Function_4_2D3F end

    def Function_5_2D75(): pass

    label("Function_5_2D75")

    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_5_2D75 end

    def Function_6_2DBD(): pass

    label("Function_6_2DBD")

    Sleep(100)
    SetChrSubChip(0xFE, 1)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    SetChrFlags(0x11, 0x80)
    Return()

    # Function_6_2DBD end

    def Function_7_2E1C(): pass

    label("Function_7_2E1C")

    Sleep(200)
    SetChrSubChip(0xFE, 1)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    SetChrFlags(0x12, 0x80)
    Return()

    # Function_7_2E1C end

    def Function_8_2E7B(): pass

    label("Function_8_2E7B")

    Sleep(300)
    SetChrSubChip(0xFE, 1)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    SetChrFlags(0x13, 0x80)
    Return()

    # Function_8_2E7B end

    def Function_9_2EDA(): pass

    label("Function_9_2EDA")

    Sleep(400)
    SetChrSubChip(0xFE, 1)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    SetChrFlags(0x14, 0x80)
    Return()

    # Function_9_2EDA end

    SaveToFile()

Try(main)
