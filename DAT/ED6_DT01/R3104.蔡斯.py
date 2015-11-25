from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3104   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3104.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60020",
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
        '魔兽',                                 # 9
        '魔兽',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '魔兽',                                 # 13
        '托兰特平原道方向',                     # 14
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
        Unknown_3A              = 144,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10060 ._CH',             # 00
        'ED6_DT09/CH10061 ._CH',             # 01
        'ED6_DT07/CH00100 ._CH',             # 02
        'ED6_DT07/CH00101 ._CH',             # 03
        'ED6_DT07/CH00110 ._CH',             # 04
        'ED6_DT07/CH00111 ._CH',             # 05
        'ED6_DT07/CH00150 ._CH',             # 06
        'ED6_DT07/CH00151 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10060P._CP',             # 00
        'ED6_DT09/CH10061P._CP',             # 01
        'ED6_DT07/CH00100P._CP',             # 02
        'ED6_DT07/CH00101P._CP',             # 03
        'ED6_DT07/CH00110P._CP',             # 04
        'ED6_DT07/CH00111P._CP',             # 05
        'ED6_DT07/CH00150P._CP',             # 06
        'ED6_DT07/CH00151P._CP',             # 07
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 50,
        Z                   = -130,
        Y                   = -59690,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1AA",          # 00, 0
        "Function_1_1E9",          # 01, 1
        "Function_2_232",          # 02, 2
        "Function_3_3BA",          # 03, 3
        "Function_4_1264",         # 04, 4
        "Function_5_1297",         # 05, 5
    )


    def Function_0_1AA(): pass

    label("Function_0_1AA")

    ClearMapFlags(0x40000000)
    AddParty(0xFF, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1C2"),
        (101, "loc_1D5"),
        (SWITCH_DEFAULT, "loc_1E8"),
    )


    label("loc_1C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D2")
    Event(0, 3)

    label("loc_1D2")

    Jump("loc_1E8")

    label("loc_1D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E5")
    Event(0, 5)

    label("loc_1E5")

    Jump("loc_1E8")

    label("loc_1E8")

    Return()

    # Function_0_1AA end

    def Function_1_1E9(): pass

    label("Function_1_1E9")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x30031)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_210")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_228")
    OP_B1("R3104_y")
    Jump("loc_231")

    label("loc_228")

    OP_B1("R3104_n")

    label("loc_231")

    Return()

    # Function_1_1E9 end

    def Function_2_232(): pass

    label("Function_2_232")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3A4")

    label("loc_262")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3A4")

    label("loc_27B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3A4")

    label("loc_294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3A4")

    label("loc_2AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C6")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3A4")

    label("loc_2C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3A4")

    label("loc_2DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3A4")

    label("loc_2F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3A4")

    label("loc_311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3A4")

    label("loc_32A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3A4")

    label("loc_343")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3A4")

    label("loc_35C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_375")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3A4")

    label("loc_375")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3A4")

    label("loc_38E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3A4")

    label("loc_3B9")

    Return()

    # Function_2_232 end

    def Function_3_3BA(): pass

    label("Function_3_3BA")

    EventBegin(0x0)
    OP_6D(620, -50, -47670, 0)
    SetChrPos(0x101, 430, -70, -48480, 0)
    SetChrPos(0x106, 950, -90, -49600, 0)
    SetChrPos(0x102, -1020, -40, -49790, 0)
    FadeToBright(1000, 0)
    OP_66(0x0)

    def lambda_412():
        OP_67(-22360, 30130, -70650, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_412)
    OP_6D(270, 5050, -6000, 6000)
    Fade(1000)
    OP_66(0x1)
    OP_6D(380, 650, -19840, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 380, -100, -22070, 0)
    SetChrPos(0x106, 1170, -30, -23100, 0)
    SetChrPos(0x102, -1140, -60, -23590, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002F这里就是『红莲之塔』……\x02\x03",
            "博士真的被那帮家伙\x01",
            "掳到这种地方来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F看来没错……\x01",
            "地上有很多纷乱的脚印。\x02\x03",
            "而且这里作为藏身之处\x01",
            "确实是最合适不过……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 4)
    OP_0D()

    ChrTalk(
        0x102,
        "#016F你们两个小心！\x02",
    )

    CloseMessageWindow()

    def lambda_5D5():
        OP_6C(32000, 2000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5D5)
    OP_6D(-150, 3850, -10760, 2000)
    SetChrPos(0x8, -1210, 5050, -5570, 0)
    SetChrPos(0x9, -670, 4650, -6550, 0)
    SetChrPos(0xA, 260, 5050, -5940, 0)
    SetChrPos(0xB, 990, 5050, -5750, 0)
    SetChrPos(0xC, 1500, 5050, -5570, 0)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)

    def lambda_664():
        OP_6D(400, 650, -19840, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_664)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x106, 6)
    ClearChrFlags(0x8, 0x80)

    def lambda_68B():
        OP_8E(0xFE, 0xFFFFFBE6, 0x41A, 0xFFFFB762, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_68B)
    Sleep(200)
    ClearChrFlags(0xC, 0x80)

    def lambda_6B0():
        OP_8E(0xFE, 0x55A, 0x41A, 0xFFFFB7C6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6B0)
    Sleep(500)
    ClearChrFlags(0xA, 0x80)

    def lambda_6D5():
        OP_8E(0xFE, 0x1E, 0x41A, 0xFFFFB668, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6D5)
    Sleep(500)
    ClearChrFlags(0x9, 0x80)

    def lambda_6FA():
        OP_8E(0xFE, 0xFFFFFE0C, 0x5AA, 0xFFFFBD2A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6FA)
    Sleep(200)
    ClearChrFlags(0xB, 0x80)

    def lambda_71F():
        OP_8E(0xFE, 0x2E4, 0x5AA, 0xFFFFBD3E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_71F)
    OP_43(0x106, 0x0, 0x0, 0x4)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x4)

    def lambda_74B():
        OP_96(0xFE, 0xFFFFF646, 0xBEA, 0xFFFFAC54, 0x9C4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_74B)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x4)
    OP_96(0xC, 0x9CE, 0xBEA, 0xFFFFAC54, 0x9C4, 0x1B58)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F这些家伙！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#054F哼……\x01",
            "果然押对了！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    SetChrChipByIndex(0x9, 1)
    SetChrChipByIndex(0xA, 1)
    SetChrChipByIndex(0xB, 1)

    def lambda_7DE():
        OP_8E(0xFE, 0xA0, 0xFFFFFFCE, 0xFFFF7DF6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7DE)

    def lambda_7F9():
        OP_8E(0xFE, 0xA0, 0xFFFFFFCE, 0xFFFF7DF6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7F9)

    def lambda_814():
        OP_8E(0xFE, 0xA0, 0xFFFFFFCE, 0xFFFF7DF6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_814)
    Sleep(150)
    OP_44(0x8, 0xFF)
    SetChrChipByIndex(0x8, 1)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x8, 0x101, 0)

    def lambda_84F():
        OP_96(0xFE, 0xFFFFFF7E, 0xFFFFFFA6, 0xFFFFA394, 0x384, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_84F)
    Sleep(100)
    OP_44(0xC, 0xFF)
    SetChrChipByIndex(0xC, 1)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xC, 0x101, 0)

    def lambda_88D():
        OP_96(0xFE, 0xFFFFFF7E, 0xFFFFFFA6, 0xFFFFA394, 0x384, 0x1B58)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_88D)
    Sleep(250)
    Battle(0x3A6, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_8C3"),
        (SWITCH_DEFAULT, "loc_8C6"),
    )


    label("loc_8C3")

    OP_B4(0x0)
    Return()

    label("loc_8C6")

    EventBegin(0x0)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, 380, -100, -22070, 0)
    SetChrPos(0x106, 880, -30, -23670, 0)
    SetChrPos(0x102, -1140, -60, -23590, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrChipByIndex(0x102, 65535)
    OP_6D(310, -90, -21210, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002F#5P可是……\x01",
            "为什么那些魔兽会在这里？\x02\x03",
            "#004F啊，难道说……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_9A3)

    def lambda_9B1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B1)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "「只是单纯的巧合？」\x01",            # 0
            "「是在这座塔里栖息的吗？」\x01",      # 1
            "「和那伙黑衣人有关系吗？」\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A77"),
        (1, "loc_BB9"),
        (2, "loc_CFF"),
        (SWITCH_DEFAULT, "loc_DB0"),
    )


    label("loc_A77")


    ChrTalk(
        0x101,
        "#005F#5P只是单纯的巧合？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#053F傻丫头，怎么可能。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 600)

    ChrTalk(
        0x101,
        "#509F#5P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F虽然可能是巧合……\x01",
            "但从以前和它们交战的记录来看，\x01",
            "更可能是那些黑衣人所做的好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F啊啊，不会错的。\x02\x03",
            "恐怕那些魔兽\x01",
            "就是他们训练出来的战斗犬。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB0")

    label("loc_BB9")


    ChrTalk(
        0x101,
        "#005F#5P它们栖息在这塔里？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#053F傻丫头，怎么可能。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 600)

    ChrTalk(
        0x101,
        "#509F#5P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F虽然可能是巧合……\x01",
            "但从以前和它们交战的记录来看，\x01",
            "更可能是那些黑衣人所做的好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F啊啊，不会错的。\x02\x03",
            "恐怕那些魔兽\x01",
            "就是他们训练出来的战斗犬。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x41, 0x1)
    Jump("loc_DB0")

    label("loc_CFF")


    ChrTalk(
        0x101,
        "#005F#5P和黑衣人有关？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F啊啊，不会错的。\x02\x03",
            "恐怕那些魔兽\x01",
            "就是他们训练出来的战斗犬。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x41, 0x3)
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_DB0")

    label("loc_DB0")


    def lambda_DB6():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB6)

    ChrTalk(
        0x101,
        "#580F#5P战、战斗犬……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F我从调查他们开始，\x01",
            "就接连受到那种魔兽的袭击。\x02\x03",
            "那些疯狗应该是那些家伙养的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#5P是、是这样啊……\x02\x03",
            "#005F这么说……\x01",
            "我们上次在山顶关受到袭击，\x01",
            "都是拜你所赐的啦！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F啊，追根究底算是这样吧。\x02\x03",
            "#050F别忘记了，把调查他们的任务强塞给我的\x01",
            "就是你们的好老爸。\x02\x03",
            "不知道谁才是受害者呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#5P唔，被你这样一说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F对了，阿加特兄。\x01",
            "之前嘉恩先生也说起过这件事。\x02\x03",
            "可以告诉我们这件事的来龙去脉吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#551F你们的老爸是在空贼事件发生之前\x01",
            "突然过来要我调查这件事的。\x02\x03",
            "说什么自己有其他要事去做，\x01",
            "丢下几句话就马上溜掉了。\x02\x03",
            "真是的，大叔就爱装傻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#5P是、是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F不过事到如今，\x01",
            "我也下定决心一定要调查到底。\x02\x03",
            "特别是那个混蛋，\x01",
            "我一定要亲手抓到他……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#5P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F那个混蛋……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F……没什么。\x02\x03",
            "总之赶快抓到那帮家伙，\x01",
            "把老爷子救出来！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x539)
    EventEnd(0x0)
    Return()

    # Function_3_3BA end

    def Function_4_1264(): pass

    label("Function_4_1264")

    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 0)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 0)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 0)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 0)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 0)
    Return()

    # Function_4_1264 end

    def Function_5_1297(): pass

    label("Function_5_1297")

    EventBegin(0x0)
    OP_6D(120, 5050, -5370, 0)
    SetChrPos(0x101, 0, 5050, -5210, 0)
    SetChrPos(0x102, -830, 5050, -5210, 0)
    SetChrPos(0x107, 900, 5050, -5210, 0)
    SetChrPos(0x106, 0, 5050, -5210, 0)

    def lambda_12F4():
        OP_6D(250, 3850, -10670, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12F4)

    def lambda_130C():
        OP_8E(0xFE, 0xFFFFFFF6, 0xF0A, 0xFFFFD1B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_130C)
    Sleep(400)

    def lambda_132C():
        OP_8E(0xFE, 0xFFFFFBD2, 0xF0A, 0xFFFFD378, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_132C)
    Sleep(200)

    def lambda_134C():
        OP_8E(0xFE, 0x2C6, 0xF0A, 0xFFFFD83C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_134C)
    Sleep(200)

    def lambda_136C():
        OP_8E(0xFE, 0x50, 0xF0A, 0xFFFFDCD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_136C)
    WaitChrThread(0x106, 0x1)

    ChrTalk(
        0x106,
        "#053F……唔……\x02",
    )

    OP_9E(0x106, 0x1E, 0x0, 0x258, 0xBB8)

    def lambda_13AC():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13AC)

    def lambda_13BA():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13BA)

    def lambda_13C8():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_13C8)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F怎、怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F不……没什么。\x02\x03",
            "只是有点头晕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F#2P啊……！\x02\x03",
            "难、难道是\x01",
            "在保护我的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F这、这么说来……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F难道说……\x01",
            "你被他们导力弹打中了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F只是擦伤一点而已。\x01",
            "没什么大碍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F#2P但、但是……\x01",
            "都怪我不好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#055F不怕告诉你们，\x01",
            "这种小伤对我来说根本是家常便饭。\x02\x03",
            "别再说废话了，\x01",
            "加快脚步回蔡斯吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x53B)
    EventEnd(0x0)
    Return()

    # Function_5_1297 end

    SaveToFile()

Try(main)
