from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4303   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4303.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '军用犬',                               # 12
        '军用犬',                               # 13
        '军用犬',                               # 14
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
        'ED6_DT07/CH00100 ._CH',             # 00
        'ED6_DT07/CH00101 ._CH',             # 01
        'ED6_DT07/CH00110 ._CH',             # 02
        'ED6_DT07/CH00111 ._CH',             # 03
        'ED6_DT07/CH00170 ._CH',             # 04
        'ED6_DT07/CH00171 ._CH',             # 05
        'ED6_DT07/CH00340 ._CH',             # 06
        'ED6_DT07/CH00341 ._CH',             # 07
        'ED6_DT09/CH10060 ._CH',             # 08
        'ED6_DT09/CH10061 ._CH',             # 09
        'ED6_DT06/CH20042 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH00100P._CP',             # 00
        'ED6_DT07/CH00101P._CP',             # 01
        'ED6_DT07/CH00110P._CP',             # 02
        'ED6_DT07/CH00111P._CP',             # 03
        'ED6_DT07/CH00170P._CP',             # 04
        'ED6_DT07/CH00171P._CP',             # 05
        'ED6_DT07/CH00340P._CP',             # 06
        'ED6_DT07/CH00341P._CP',             # 07
        'ED6_DT09/CH10060P._CP',             # 08
        'ED6_DT09/CH10061P._CP',             # 09
        'ED6_DT06/CH20042P._CP',             # 0A
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1C2",          # 00, 0
        "Function_1_262",          # 01, 1
        "Function_2_275",          # 02, 2
        "Function_3_6B3",          # 03, 3
        "Function_4_B03",          # 04, 4
        "Function_5_CA5",          # 05, 5
        "Function_6_E47",          # 06, 6
        "Function_7_FE9",          # 07, 7
        "Function_8_118B",         # 08, 8
        "Function_9_132D",         # 09, 9
        "Function_10_14CF",        # 0A, 10
        "Function_11_1671",        # 0B, 11
        "Function_12_1813",        # 0C, 12
    )


    def Function_0_1C2(): pass

    label("Function_0_1C2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_1F6"),
        (100, "loc_20C"),
        (102, "loc_222"),
        (103, "loc_229"),
        (104, "loc_230"),
        (105, "loc_237"),
        (106, "loc_23E"),
        (107, "loc_245"),
        (108, "loc_24C"),
        (109, "loc_253"),
        (110, "loc_25A"),
        (SWITCH_DEFAULT, "loc_261"),
    )


    label("loc_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_209")
    OP_A2(0x653)
    Event(0, 2)

    label("loc_209")

    Jump("loc_261")

    label("loc_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21F")
    OP_A2(0x653)
    Event(0, 3)

    label("loc_21F")

    Jump("loc_261")

    label("loc_222")

    Event(0, 12)
    Jump("loc_261")

    label("loc_229")

    Event(0, 11)
    Jump("loc_261")

    label("loc_230")

    Event(0, 10)
    Jump("loc_261")

    label("loc_237")

    Event(0, 9)
    Jump("loc_261")

    label("loc_23E")

    Event(0, 8)
    Jump("loc_261")

    label("loc_245")

    Event(0, 7)
    Jump("loc_261")

    label("loc_24C")

    Event(0, 6)
    Jump("loc_261")

    label("loc_253")

    Event(0, 5)
    Jump("loc_261")

    label("loc_25A")

    Event(0, 4)
    Jump("loc_261")

    label("loc_261")

    Return()

    # Function_0_1C2 end

    def Function_1_262(): pass

    label("Function_1_262")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x30062)
    Return()

    # Function_1_262 end

    def Function_2_275(): pass

    label("Function_2_275")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, 16560, 1000, -8020, 87)
    SetChrPos(0x102, 15530, 1000, -8910, 135)
    SetChrPos(0x108, 15490, 1000, -6910, 45)
    OP_6D(15530, 1000, -7950, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, 18910, 1000, 720, 180)
    SetChrPos(0x9, 18910, 1000, 3690, 180)
    SetChrPos(0xB, 18130, 1000, 2540, 180)
    SetChrPos(0xC, 19750, 1000, 2310, 180)

    ChrTalk(
        0x8,
        "你……你们是什么人！？\x02",
    )

    CloseMessageWindow()

    def lambda_349():
        OP_6D(18540, 1000, -4090, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_349)

    def lambda_361():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_361)

    def lambda_371():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_371)

    def lambda_38C():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_38C)

    def lambda_3A7():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3A7)

    def lambda_3C2():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3C2)

    def lambda_3DD():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DD)

    def lambda_3EB():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EB)

    def lambda_3F9():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3F9)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x9, 0x1)

    ChrTalk(
        0x9,
        "可疑的人，在那儿不许动！\x02",
    )

    CloseMessageWindow()

    def lambda_471():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_471)

    def lambda_486():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_486)

    def lambda_49B():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_49B)

    def lambda_4B0():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4B0)
    Sleep(500)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x3AB, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_4ED"),
        (SWITCH_DEFAULT, "loc_4F0"),
    )


    label("loc_4ED")

    OP_B4(0x0)
    Return()

    label("loc_4F0")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, 17040, 1000, -5470, 19)
    SetChrPos(0x102, 16580, 1000, -3860, 45)
    SetChrPos(0x108, 18690, 1000, -6040, 11)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrPos(0x8, 19930, 1000, -3920, 190)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_6D(17470, 1000, -4720, 0)
    OP_6C(315000, 1000)

    ChrTalk(
        0x101,
        (
            "#000F呼～解决了。\x01",
            "冷不妨就跳出几个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F还有相当数量的特务兵\x01",
            "残留在离宫里面。\x02\x03",
            "好像定期在中庭\x01",
            "的走廊巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F没办法，若是被发现了\x01",
            "就只有让他们保持沉默了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_2_275 end

    def Function_3_6B3(): pass

    label("Function_3_6B3")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -16350, 1000, -7540, 301)
    SetChrPos(0x102, -16410, 1000, -8720, 243)
    SetChrPos(0x108, -15040, 1000, -8100, 302)
    OP_6D(-15730, 1000, -8020, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, -19240, 1000, -50, 188)
    SetChrPos(0x9, -19280, 1000, 2470, 180)
    SetChrPos(0xB, -20160, 1000, 960, 180)
    SetChrPos(0xC, -18110, 1000, 970, 180)

    ChrTalk(
        0x8,
        "你……你们是什么人！？\x02",
    )

    CloseMessageWindow()

    def lambda_787():
        OP_6D(-19130, 1000, -4630, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_787)

    def lambda_79F():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_79F)

    def lambda_7AF():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7AF)

    def lambda_7CA():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7CA)

    def lambda_7E5():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7E5)

    def lambda_800():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_800)

    def lambda_81B():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81B)

    def lambda_829():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_829)

    def lambda_837():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_837)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x9, 0x1)

    ChrTalk(
        0x9,
        "可疑的人，在那儿不许动！\x02",
    )

    CloseMessageWindow()

    def lambda_8AF():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8AF)

    def lambda_8C4():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8C4)

    def lambda_8D9():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8D9)

    def lambda_8EE():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8EE)
    Sleep(500)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x3AC, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_92B"),
        (SWITCH_DEFAULT, "loc_92E"),
    )


    label("loc_92B")

    OP_B4(0x0)
    Return()

    label("loc_92E")

    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, -18900, 1000, -6950, 14)
    SetChrPos(0x102, -17970, 1000, -6160, 345)
    SetChrPos(0x108, -20110, 1000, -5730, 45)
    SetChrPos(0x8, -17200, 1000, -3390, 270)
    SetChrPos(0x9, -18660, 1000, -3640, 270)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_6D(-18490, 1000, -4850, 0)
    OP_6C(45000, 0)

    ChrTalk(
        0x101,
        (
            "#000F呼～解决了。\x01",
            "冷不妨就跳出几个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F还有相当数量的特务兵\x01",
            "残留在离宫里面。\x02\x03",
            "好像定期在中庭\x01",
            "的走廊巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F没办法，若是被发现了\x01",
            "就只有让他们保持沉默了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_3_6B3 end

    def Function_4_B03(): pass

    label("Function_4_B03")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B15")
    Return()

    label("loc_B15")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, 19940, 1000, 6790, 294)
    SetChrPos(0x102, 21170, 1000, 6410, 326)
    SetChrPos(0x108, 21290, 1000, 7450, 303)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 19310, 1000, 13490, 173)
    SetChrPos(0x9, 20360, 1000, 15020, 170)
    SetChrPos(0xA, 18980, 1000, 14690, 186)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(19290, 1000, 10760, 1000)

    def lambda_BF7():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BF7)

    def lambda_C0C():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C0C)

    def lambda_C21():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C21)

    def lambda_C36():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C36)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_4_B03 end

    def Function_5_CA5(): pass

    label("Function_5_CA5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB7")
    Return()

    label("loc_CB7")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, 20250, 1000, 21120, 295)
    SetChrPos(0x102, 20800, 1000, 20430, 2)
    SetChrPos(0x108, 20970, 1000, 21870, 149)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 19240, 1000, 31840, 174)
    SetChrPos(0x9, 20580, 1000, 32970, 194)
    SetChrPos(0xA, 18940, 1000, 32770, 160)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(19670, 1000, 32770, 1000)

    def lambda_D99():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D99)

    def lambda_DAE():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_DAE)

    def lambda_DC3():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_DC3)

    def lambda_DD8():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_DD8)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_5_CA5 end

    def Function_6_E47(): pass

    label("Function_6_E47")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E59")
    Return()

    label("loc_E59")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, 20270, 1000, 32830, 270)
    SetChrPos(0x102, 21030, 1000, 32090, 267)
    SetChrPos(0x108, 21160, 1000, 33550, 274)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 12630, 1000, 35570, 101)
    SetChrPos(0x9, 11450, 1000, 36350, 97)
    SetChrPos(0xA, 11530, 1000, 34890, 88)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(12350, 1000, 35970, 1000)

    def lambda_F3B():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F3B)

    def lambda_F50():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F50)

    def lambda_F65():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F65)

    def lambda_F7A():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F7A)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_6_E47 end

    def Function_7_FE9(): pass

    label("Function_7_FE9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFB")
    Return()

    label("loc_FFB")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, 9090, 1000, 36810, 270)
    SetChrPos(0x102, 9630, 1000, 37440, 270)
    SetChrPos(0x108, 8380, 1000, 36730, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 400, 1000, 35050, 88)
    SetChrPos(0x9, -330, 1000, 36110, 103)
    SetChrPos(0xA, -640, 1000, 34500, 78)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(490, 1000, 35070, 1000)

    def lambda_10DD():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10DD)

    def lambda_10F2():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10F2)

    def lambda_1107():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1107)

    def lambda_111C():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_111C)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_7_FE9 end

    def Function_8_118B(): pass

    label("Function_8_118B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119D")
    Return()

    label("loc_119D")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -180, 1000, 40300, 186)
    SetChrPos(0x102, 840, 1000, 40700, 166)
    SetChrPos(0x108, -890, 1000, 40810, 198)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 150, 250, 29590, 351)
    SetChrPos(0x9, -440, 500, 30500, 356)
    SetChrPos(0xA, 940, 500, 30620, 341)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(150, 250, 29590, 1000)

    def lambda_127F():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_127F)

    def lambda_1294():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1294)

    def lambda_12A9():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12A9)

    def lambda_12BE():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_12BE)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_8_118B end

    def Function_9_132D(): pass

    label("Function_9_132D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133F")
    Return()

    label("loc_133F")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -8960, 1000, 36360, 83)
    SetChrPos(0x102, -9650, 1000, 36960, 83)
    SetChrPos(0x108, -7870, 1000, 36840, 87)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 1650, 1000, 34820, 248)
    SetChrPos(0x9, 2640, 1000, 35540, 277)
    SetChrPos(0xA, 2540, 1000, 34230, 260)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(1650, 1000, 34820, 1000)

    def lambda_1421():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1421)

    def lambda_1436():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1436)

    def lambda_144B():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_144B)

    def lambda_1460():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1460)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_9_132D end

    def Function_10_14CF(): pass

    label("Function_10_14CF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E1")
    Return()

    label("loc_14E1")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -20560, 1000, 29250, 23)
    SetChrPos(0x102, -21000, 1000, 28080, 60)
    SetChrPos(0x108, -21470, 1000, 29440, 52)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -16129, 1000, 34890, 224)
    SetChrPos(0x9, -16560, 1000, 36340, 211)
    SetChrPos(0xA, -17730, 1000, 36360, 209)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(-16560, 1000, 36340, 1000)

    def lambda_15C3():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_15C3)

    def lambda_15D8():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_15D8)

    def lambda_15ED():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15ED)

    def lambda_1602():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1602)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_10_14CF end

    def Function_11_1671(): pass

    label("Function_11_1671")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1683")
    Return()

    label("loc_1683")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -20250, 1000, 20460, 144)
    SetChrPos(0x102, -21290, 1000, 20210, 133)
    SetChrPos(0x108, -20770, 1000, 21590, 119)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -16300, 1000, 16040, 316)
    SetChrPos(0x9, -15870, 750, 15030, 297)
    SetChrPos(0xA, -15260, 750, 16170, 306)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(-16300, 1000, 16040, 1000)

    def lambda_1765():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1765)

    def lambda_177A():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_177A)

    def lambda_178F():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_178F)

    def lambda_17A4():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_17A4)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_11_1671 end

    def Function_12_1813(): pass

    label("Function_12_1813")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1825")
    Return()

    label("loc_1825")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -20590, 1000, 3380, 29)
    SetChrPos(0x102, -21500, 1000, 3480, 55)
    SetChrPos(0x108, -21000, 1000, 2080, 29)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -19300, 1000, 10370, 167)
    SetChrPos(0x9, -20480, 1000, 11180, 175)
    SetChrPos(0xA, -18330, 1000, 10260, 167)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(-19300, 1000, 10370, 1000)

    def lambda_1907():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1907)

    def lambda_191C():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_191C)

    def lambda_1931():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1931)

    def lambda_1946():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1946)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_12_1813 end

    SaveToFile()

Try(main)
