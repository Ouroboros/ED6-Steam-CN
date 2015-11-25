from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4300   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60089",
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
        '中队长',                               # 9
        '特务兵',                               # 10
        '特务兵',                               # 11
        '特务兵',                               # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '特务兵',                               # 15
        '特务兵',                               # 16
        '特务兵',                               # 17
        '特务兵',                               # 18
        '特务兵',                               # 19
        '军用犬',                               # 20
        '军用犬',                               # 21
        '军用犬',                               # 22
        '军用犬',                               # 23
        '军用犬',                               # 24
        '亲卫队员',                             # 25
        '亲卫队员',                             # 26
        '亲卫队员',                             # 27
        '亲卫队员',                             # 28
        '科洛丝',                               # 29
        '雪拉',                                 # 30
        '奥利维尔',                             # 31
        '奈尔',                                 # 32
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
        'ED6_DT07/CH01800 ._CH',             # 01
        'ED6_DT09/CH10060 ._CH',             # 02
        'ED6_DT07/CH01320 ._CH',             # 03
        'ED6_DT07/CH00100 ._CH',             # 04
        'ED6_DT07/CH00101 ._CH',             # 05
        'ED6_DT07/CH00110 ._CH',             # 06
        'ED6_DT07/CH00111 ._CH',             # 07
        'ED6_DT07/CH00170 ._CH',             # 08
        'ED6_DT07/CH00171 ._CH',             # 09
        'ED6_DT07/CH00340 ._CH',             # 0A
        'ED6_DT07/CH00341 ._CH',             # 0B
        'ED6_DT07/CH00342 ._CH',             # 0C
        'ED6_DT07/CH00040 ._CH',             # 0D
        'ED6_DT07/CH00020 ._CH',             # 0E
        'ED6_DT07/CH00030 ._CH',             # 0F
        'ED6_DT07/CH02060 ._CH',             # 10
        'ED6_DT06/CH20116 ._CH',             # 11
        'ED6_DT06/CH20117 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01610P._CP',             # 00
        'ED6_DT07/CH01800P._CP',             # 01
        'ED6_DT09/CH10060P._CP',             # 02
        'ED6_DT07/CH01320P._CP',             # 03
        'ED6_DT07/CH00100P._CP',             # 04
        'ED6_DT07/CH00101P._CP',             # 05
        'ED6_DT07/CH00110P._CP',             # 06
        'ED6_DT07/CH00111P._CP',             # 07
        'ED6_DT07/CH00170P._CP',             # 08
        'ED6_DT07/CH00171P._CP',             # 09
        'ED6_DT07/CH00340P._CP',             # 0A
        'ED6_DT07/CH00341P._CP',             # 0B
        'ED6_DT07/CH00342P._CP',             # 0C
        'ED6_DT07/CH00040P._CP',             # 0D
        'ED6_DT07/CH00020P._CP',             # 0E
        'ED6_DT07/CH00030P._CP',             # 0F
        'ED6_DT07/CH02060P._CP',             # 10
        'ED6_DT06/CH20116P._CP',             # 11
        'ED6_DT06/CH20117P._CP',             # 12
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_442",          # 00, 0
        "Function_1_4B7",          # 01, 1
        "Function_2_4CA",          # 02, 2
        "Function_3_808",          # 03, 3
        "Function_4_12D0",         # 04, 4
        "Function_5_130B",         # 05, 5
        "Function_6_13F6",         # 06, 6
        "Function_7_14DC",         # 07, 7
    )


    def Function_0_442(): pass

    label("Function_0_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_453")
    OP_A3(0x3FA)
    Event(0, 2)
    Jump("loc_4B6")

    label("loc_453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_472")
    OP_A3(0x3FB)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)
    Jump("loc_4B6")

    label("loc_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_483")
    OP_A3(0x3FC)
    Event(0, 6)
    Jump("loc_4B6")

    label("loc_483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_494")
    OP_A3(0x3FD)
    Event(0, 7)
    Jump("loc_4B6")

    label("loc_494")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_4A0"),
        (SWITCH_DEFAULT, "loc_4B6"),
    )


    label("loc_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B3")
    OP_A2(0x652)
    Event(0, 3)

    label("loc_4B3")

    Jump("loc_4B6")

    label("loc_4B6")

    Return()

    # Function_0_442 end

    def Function_1_4B7(): pass

    label("Function_1_4B7")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE8900, 0x30061)
    Return()

    # Function_1_4B7 end

    def Function_2_4CA(): pass

    label("Function_2_4CA")

    EventBegin(0x0)
    OP_6D(-70, 0, 20900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(408, 0)

    def lambda_50F():
        OP_6D(-1300, 0, 47880, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50F)

    def lambda_527():
        OP_6C(314000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_527)

    def lambda_537():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_537)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    def lambda_57E():

        label("loc_57E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_57E")

    QueueWorkItem2(0x13, 0, lambda_57E)

    def lambda_591():

        label("loc_591")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_591")

    QueueWorkItem2(0x14, 0, lambda_591)

    def lambda_5A4():

        label("loc_5A4")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_5A4")

    QueueWorkItem2(0x15, 0, lambda_5A4)

    def lambda_5B7():

        label("loc_5B7")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_5B7")

    QueueWorkItem2(0x16, 0, lambda_5B7)

    def lambda_5CA():

        label("loc_5CA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_5CA")

    QueueWorkItem2(0x17, 0, lambda_5CA)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x8, -70, 1000, 50380, 180)
    SetChrPos(0x9, 730, 0, 46530, 0)
    SetChrPos(0xA, 2350, 0, 46770, 315)
    SetChrPos(0xB, 2090, 0, 45430, 332)
    SetChrPos(0xC, 1380, 0, 44350, 351)
    SetChrPos(0xD, 470, 0, 43290, 7)
    SetChrPos(0xE, -920, 0, 43360, 353)
    SetChrPos(0xF, -2230, 0, 44390, 7)
    SetChrPos(0x10, -1210, 0, 45310, 16)
    SetChrPos(0x11, -2029, 0, 46530, 25)
    SetChrPos(0x12, -690, 0, 46650, 7)
    SetChrPos(0x13, -3190, 0, 43920, 33)
    SetChrPos(0x14, -3130, 250, 47070, 62)
    SetChrPos(0x15, 3260, 0, 45110, 307)
    SetChrPos(0x16, 80, 0, 44910, 349)
    SetChrPos(0x17, 1250, 0, 42490, 5)
    Sleep(5000)

    ChrTalk(
        0x8,
        (
            "听着！\x01",
            "从特务飞艇传来消息！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "亲卫队的残党\x01",
            "竟然恬不知耻的出现了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "立刻前往现场，\x01",
            "借此机会将他们全部剿灭！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetMessageWindowPos(70, 80, -1, -1)
    SetChrName("特务兵们")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5S是！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C4113   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_4CA end

    def Function_3_808(): pass

    label("Function_3_808")

    EventBegin(0x0)
    OP_6F(0xD, 120)
    OP_72(0xD, 0x10)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x9, 12)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0xB, 10)
    SetChrChipByIndex(0xC, 10)
    SetChrChipByIndex(0xD, 10)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x108, 8)
    SetChrPos(0x108, 70, 0, 26850, 356)
    SetChrPos(0x101, -640, 0, 26250, 315)
    SetChrPos(0x102, 1000, 0, 26220, 45)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x18, 9480, 250, 32070, 180)
    SetChrPos(0x9, 9490, 250, 31050, 0)
    SetChrPos(0x19, 8250, 130, 44870, 46)
    SetChrPos(0xA, 7080, 0, 41450, 14)
    SetChrPos(0xB, 17790, 0, 47220, 260)
    SetChrPos(0x1A, -18980, 0, 51590, 180)
    SetChrPos(0xC, -19080, 0, 48030, 0)
    SetChrPos(0x1B, -9790, 210, 47380, 56)
    SetChrPos(0xD, -19320, 0, 41420, 44)
    SetChrPos(0xE, -17850, 20, 41630, 80)
    FadeToBright(2000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(278000, 0)
    OP_6E(288, 0)
    Fade(1000)
    OP_6D(9140, 250, 31570, 0)

    def lambda_9B2():
        OP_6C(314000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9B2)
    SetChrChipByIndex(0x18, 18)
    SetChrSubChip(0x18, 1)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrFlags(0x9, 0x20)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_9E1():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9E1)

    def lambda_9FB():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9FB)
    Sleep(1000)

    def lambda_A1A():
        OP_99(0x9, 0x2, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A1A)
    Sleep(100)
    SetChrChipByIndex(0x18, 17)
    OP_96(0x18, 0x2512, 0xFA, 0x80DE, 0x3E8, 0x1F40)
    OP_22(0xA4, 0x0, 0x64)
    SetChrFlags(0x18, 0x20)

    def lambda_A55():
        OP_8E(0x18, 0x24FE, 0xFA, 0x7CC4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A55)
    Sleep(50)
    SetChrChipByIndex(0x18, 18)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrSubChip(0x18, 0)
    Sleep(50)
    SetChrSubChip(0x18, 1)
    Sleep(50)
    SetChrSubChip(0x18, 2)
    OP_96(0x9, 0x24F4, 0xFA, 0x74EA, 0x3E8, 0x1F40)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_AB4():
        OP_99(0x9, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AB4)
    OP_8E(0x9, 0x24FE, 0xFA, 0x799A, 0x1B58, 0x0)
    SetChrSubChip(0x18, 1)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_AE2():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AE2)

    def lambda_AFC():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_AFC)
    Sleep(500)
    Fade(1000)
    OP_6D(7760, 0, 43410, 0)
    OP_6E(330, 0)

    def lambda_B3A():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_B3A)

    def lambda_B4A():
        OP_6D(11360, 0, 49140, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B4A)

    def lambda_B62():

        label("loc_B62")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_B62")

    QueueWorkItem2(0xA, 2, lambda_B62)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xA, 11)
    SetChrChipByIndex(0xB, 11)

    def lambda_B8C():
        OP_8E(0xFE, 0x3BE2, 0xFA, 0xB8BA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B8C)

    def lambda_BA7():
        OP_8E(0xFE, 0x22BA, 0xE6, 0xB50E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_BA7)

    def lambda_BC2():
        OP_8E(0xFE, 0x2724, 0xFA, 0xB8F6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_BC2)
    WaitChrThread(0x19, 0x1)

    def lambda_BE2():
        OP_8E(0xFE, 0x2C60, 0x0, 0xC116, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_BE2)
    WaitChrThread(0x19, 0x1)
    SetChrChipByIndex(0x19, 18)
    SetChrSubChip(0x19, 2)
    SetChrFlags(0x19, 0x20)
    TurnDirection(0x19, 0xA, 800)
    Sleep(200)

    def lambda_C1D():
        OP_92(0xFE, 0x19, 0x3E8, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C1D)

    def lambda_C32():
        OP_92(0xFE, 0x19, 0x3E8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C32)
    Sleep(300)
    TurnDirection(0x19, 0xB, 800)
    SetChrFlags(0xB, 0x20)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_99(0xB, 0x0, 0x2, 0x7D0)

    def lambda_C6C():
        OP_99(0xFE, 0x3, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_C6C)

    def lambda_C7C():
        OP_8E(0xFE, 0x2FD0, 0x0, 0xBD6A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C7C)
    Sleep(100)

    def lambda_C9C():
        OP_8E(0xFE, 0x2832, 0x28, 0xBB3A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C9C)
    Sleep(200)
    SetChrFlags(0x19, 0x4)
    SetChrSubChip(0x19, 1)

    def lambda_CC6():
        OP_97(0xFE, 0x2ED6, 0xC06C, 0x38270, 0x24B8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_CC6)
    Sleep(250)
    OP_22(0x229, 0x0, 0x64)

    def lambda_CEC():
        OP_8F(0xFE, 0x2B0C, 0xFA, 0xB752, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_CEC)
    Sleep(100)

    def lambda_D0C():
        OP_96(0xFE, 0x23F0, 0x0, 0xBA86, 0x258, 0x1B58)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D0C)
    ClearChrFlags(0x19, 0x20)
    ClearChrFlags(0x19, 0x4)
    SetChrChipByIndex(0x19, 17)

    def lambda_D39():
        OP_8E(0xFE, 0x5000, 0x0, 0xB464, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_D39)
    Sleep(500)

    def lambda_D59():
        OP_92(0xFE, 0x19, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D59)
    Sleep(500)

    def lambda_D73():
        OP_92(0xFE, 0x19, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D73)
    Sleep(100)
    ClearChrFlags(0xB, 0x20)
    OP_8E(0xB, 0x2B7A, 0x0, 0xBC7A, 0x1388, 0x0)

    def lambda_DA6():
        OP_92(0xFE, 0x19, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_DA6)

    def lambda_DBB():
        OP_92(0xFE, 0x19, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DBB)
    Sleep(500)
    Fade(1000)
    OP_6D(-19190, 0, 50360, 0)
    SetChrChipByIndex(0xC, 11)

    def lambda_DF0():
        OP_6D(-19700, 0, 53190, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DF0)
    OP_92(0xC, 0x1A, 0x258, 0x1770, 0x0)

    def lambda_E16():
        OP_91(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E16)
    OP_91(0x1A, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
    SetChrFlags(0x1A, 0x20)
    SetChrChipByIndex(0x1A, 18)
    SetChrSubChip(0x1A, 1)

    def lambda_E54():
        OP_9E(0xFE, 0x1E, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E54)

    def lambda_E6E():
        OP_9E(0xFE, 0x1E, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_E6E)
    Sleep(700)

    def lambda_E8D():

        label("loc_E8D")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_E8D")

    QueueWorkItem2(0x1A, 1, lambda_E8D)

    def lambda_E9E():
        OP_8F(0xFE, 0xFFFFB3C0, 0x0, 0xD192, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_E9E)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x40)
    OP_91(0xC, 0x0, 0x0, 0x190, 0x1388, 0x0)
    SetChrChipByIndex(0x1A, 17)
    OP_22(0x208, 0x0, 0x64)
    OP_97(0xC, 0xFFFFB3C0, 0xD192, 0xFFFE7960, 0x2328, 0x2)
    SetChrChipByIndex(0x1A, 18)
    SetChrSubChip(0x1A, 2)
    OP_96(0xC, 0xFFFFAE3E, 0xFFFFF060, 0xDCD2, 0xC8, 0x2710)
    OP_22(0xB3, 0x0, 0x64)
    OP_44(0x1A, 0xFF)
    SetChrChipByIndex(0xD, 11)

    def lambda_F25():
        OP_8E(0xFE, 0xFFFFB348, 0x0, 0xBE46, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F25)
    Sleep(500)

    def lambda_F45():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_F45)

    def lambda_F53():
        OP_6D(-19190, 0, 50360, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F53)

    def lambda_F6B():
        OP_6E(305, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F6B)
    SetChrChipByIndex(0xE, 11)

    def lambda_F80():
        OP_8E(0xFE, 0xFFFFB8FC, 0x0, 0xBDF6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_F80)
    Sleep(1500)

    def lambda_FA0():

        label("loc_FA0")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_FA0")

    QueueWorkItem2(0x1A, 1, lambda_FA0)

    def lambda_FB1():
        OP_91(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FB1)
    Sleep(200)

    def lambda_FD1():
        OP_91(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_FD1)
    Sleep(300)

    def lambda_FF1():
        OP_8E(0xFE, 0xFFFFBB9A, 0x0, 0xBE3C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_FF1)
    Sleep(500)

    def lambda_1011():
        TurnDirection(0xFE, 0x1B, 800)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1011)

    def lambda_101F():
        TurnDirection(0xFE, 0x1B, 800)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_101F)
    Sleep(200)

    def lambda_1032():
        OP_96(0xFE, 0xFFFFBB9A, 0x0, 0xBE3C, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1032)
    SetChrFlags(0x1B, 0x20)
    SetChrChipByIndex(0x1B, 18)
    SetChrSubChip(0x1B, 0)
    Sleep(300)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrSubChip(0x1B, 1)
    Sleep(50)
    SetChrSubChip(0x1B, 2)
    OP_96(0xE, 0xFFFFB64A, 0x0, 0xB928, 0x3E8, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)

    def lambda_1099():
        OP_8F(0xFE, 0xFFFFB384, 0x0, 0xB6E4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1099)

    def lambda_10B4():
        OP_8F(0xFE, 0xFFFFB0E6, 0x0, 0xC1D4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10B4)
    SetChrChipByIndex(0x1A, 17)
    ClearChrFlags(0x1A, 0x20)
    SetChrFlags(0x1A, 0x4)
    OP_8F(0x1A, 0xFFFFB7A8, 0x0, 0xC8F0, 0xFA0, 0x0)
    OP_96(0x1A, 0xFFFFBFE6, 0x0, 0xBFE0, 0x3E8, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)
    OP_8F(0x1A, 0xFFFFBD02, 0x0, 0xBA40, 0x7D0, 0x0)
    SetChrChipByIndex(0x1A, 18)
    SetChrSubChip(0x1A, 2)
    Fade(1000)
    ClearChrFlags(0x108, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_6D(110, 0, 26870, 0)
    OP_6C(326000, 0)
    OP_0D()

    ChrTalk(
        0x108,
        (
            "#070F#5P好呀好呀……正在交战呢。\x01",
            "　\x02\x03",
            "我们趁机冲进这座宫殿里去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#3PＯＫ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F明白！\x02",
    )

    CloseMessageWindow()

    def lambda_11DA():
        OP_6D(-60, 1000, 57500, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11DA)

    def lambda_11F2():
        OP_67(0, 5710, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_11F2)

    def lambda_120A():
        OP_6B(1780, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_120A)

    def lambda_121A():
        OP_6C(44000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_121A)

    def lambda_122A():
        OP_6E(545, 3000)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_122A)

    def lambda_123A():
        OP_8E(0xFE, 0xFFFFFFA6, 0x3E8, 0xE06A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_123A)
    Sleep(300)

    def lambda_125A():
        OP_8E(0xFE, 0xFFFFFDBC, 0x3E8, 0xDB60, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_125A)
    Sleep(100)

    def lambda_127A():
        OP_8E(0xFE, 0x320, 0x3E8, 0xDA2A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_127A)
    WaitChrThread(0x108, 0x1)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_43(0x108, 0x1, 0x0, 0x4)
    Sleep(400)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0x4)
    OP_28(0x4C, 0x1, 0x1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_808 end

    def Function_4_12D0(): pass

    label("Function_4_12D0")

    OP_8E(0xFE, 0xFFFFFFA6, 0x3E8, 0xE06A, 0x1194, 0x0)

    def lambda_12EA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_12EA)
    OP_8E(0xFE, 0xFFFFFFCE, 0x3E8, 0xE948, 0x1194, 0x0)
    Return()

    # Function_4_12D0 end

    def Function_5_130B(): pass

    label("Function_5_130B")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x18, -1440, 1000, 57280, 180)
    SetChrPos(0x19, 1590, 1000, 57280, 180)
    SetChrChipByIndex(0x18, 18)
    SetChrChipByIndex(0x19, 18)
    SetChrSubChip(0x18, 2)
    SetChrSubChip(0x19, 2)
    OP_6D(-110, 1000, 51060, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(538, 0)

    def lambda_1395():
        OP_6D(80, 1000, 58940, 8000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1395)

    def lambda_13AD():
        OP_6C(0, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13AD)

    def lambda_13BD():
        OP_6E(346, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13BD)

    def lambda_13CD():
        OP_67(0, 6150, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13CD)
    Sleep(9000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4311   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_5_130B end

    def Function_6_13F6(): pass

    label("Function_6_13F6")

    EventBegin(0x0)
    SetChrChipByIndex(0x18, 18)
    SetChrChipByIndex(0x19, 18)
    SetChrSubChip(0x18, 2)
    SetChrSubChip(0x19, 2)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x18, -1440, 1000, 57280, 180)
    SetChrPos(0x19, 1590, 1000, 57280, 180)
    OP_6D(750, 0, 24130, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(480, 0)

    def lambda_147B():
        OP_6C(333000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_147B)
    Sleep(1000)

    def lambda_1490():
        OP_6D(-440, 0, 54170, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1490)

    def lambda_14A8():
        OP_67(0, 4770, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14A8)

    def lambda_14C0():
        OP_6E(480, 9000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14C0)
    Sleep(9000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_13F6 end

    def Function_7_14DC(): pass

    label("Function_7_14DC")

    EventBegin(0x0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_6D(260, 1000, 50040, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x101, 130, 1000, 50320, 180)
    SetChrPos(0x102, 170, 750, 49180, 337)
    SetChrPos(0x101, 130, 1000, 50320, 180)
    SetChrPos(0x1C, 1300, 1000, 50640, 233)
    SetChrPos(0x1D, -1050, 1000, 51180, 189)
    SetChrPos(0x1F, -2540, 1000, 50100, 137)
    SetChrPos(0x1E, -1560, 500, 48490, 27)
    SetChrPos(0x108, 1400, 250, 47380, 6)

    ChrTalk(
        0x101,
        (
            "#000F……约修亚，你要小心哟。\x02\x03",
            "做不到的事情\x01",
            "可不能勉强哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，我会小心的。\x02\x03",
            "你也要多思考，\x01",
            "然后再行动哦。\x02\x03",
            "不要对自己的能力太自信，\x01",
            "要和雪拉姐姐他们齐心协力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……我知道了。\x02\x03",
            "无论怎样，\x01",
            "还是和往常相同的约定！\x02\x03",
            "平平安安的\x01",
            "在格兰赛尔城相会吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯……一定！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#040F约修亚君。\x02\x03",
            "现在还不知道在隐藏的水路里\x01",
            "会有什么样的魔兽出现。\x02\x03",
            "因此请你们一定要小心行事。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F我知道了。\x01",
            "我们会小心谨慎的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x1D,
        (
            "#020F现在已经不用为艾丝蒂尔担心了。\x02\x03",
            "她在经过了这么久的旅行之后\x01",
            "已经成长了许多了呢。\x02\x03",
            "而且不仅是作为游击士，\x01",
            "作为一个女人，也是如此哦㈱　　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1D, 400)

    ChrTalk(
        0x101,
        "#000F雪、雪拉姐……\x02",
    )

    CloseMessageWindow()

    def lambda_18D1():

        label("loc_18D1")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_18D1")

    QueueWorkItem2(0x1F, 1, lambda_18D1)

    ChrTalk(
        0x102,
        (
            "#010F？？？\x02\x03",
            "怎么啦？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F不、不知道他们在说什么啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F呵呵，那么……\x02\x03",
            "我们这就开始行动吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1979():
        OP_8E(0xFE, 0x8C, 0x0, 0x5618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1979)

    ChrTalk(
        0x1E,
        "#030F再会吧，小猫咪们㈱\x02",
    )

    CloseMessageWindow()

    def lambda_19BE():
        OP_8E(0xFE, 0x8C, 0x0, 0x5618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_19BE)

    ChrTalk(
        0x102,
        "#010F愿女神保佑你们！\x02",
    )

    CloseMessageWindow()

    def lambda_19F7():
        OP_8E(0xFE, 0x8C, 0x0, 0x5618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19F7)
    Sleep(2000)

    ChrTalk(
        0x101,
        "#000F………约修亚……………\x02",
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8F(0x1D, 0x2BC, 0x3E8, 0xC792, 0x3E8, 0x0)
    OP_63(0x1D)

    ChrTalk(
        0x1D,
        (
            "#020F（公主殿下，您瞧您瞧……）\x02\x03",
            "（那两个孩子在旅途中\x01",
            "是不是产生了……呢？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#040F（……也许是这样的吧。）\x02\x03",
            "（他们两人可以每天\x01",
            "这么愉快地在一起……）\x02\x03",
            "（……让我都有那么一点儿羡慕了呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x65A)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_14DC end

    SaveToFile()

Try(main)
