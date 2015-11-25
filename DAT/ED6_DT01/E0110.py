from ED6ScenarioHelper import *

def main():
    CreateScenaFile(
        FileName            = 'E0110   ._SN',
        MapName             = 'event',
        Location            = 'E0110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60087",
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
        '吉尔',                                 # 9
        '乔丝特',                               # 10
        '空贼雷古',                             # 11
        '空贼蒂诺',                             # 12
        '空贼莱尔',                             # 13
        '空贼洛西',                             # 14
        '空贼罗尔',                             # 15
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
        'ED6_DT07/CH02120 ._CH',             # 00
        'ED6_DT07/CH02130 ._CH',             # 01
        'ED6_DT07/CH01380 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02120P._CP',             # 00
        'ED6_DT07/CH02130P._CP',             # 01
        'ED6_DT07/CH01380P._CP',             # 02
    )

    DeclNpc(
        X                   = -24246,
        Z                   = -1000,
        Y                   = 4880,
        Direction           = 270,
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
        X                   = -18320,
        Z                   = 3000,
        Y                   = 4790,
        Direction           = 270,
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
        X                   = -21660,
        Z                   = 650,
        Y                   = 5320,
        Direction           = 290,
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
        X                   = 45400,
        Z                   = 0,
        Y                   = 6950,
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
        X                   = 51600,
        Z                   = 0,
        Y                   = 3170,
        Direction           = 135,
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
        X                   = 47800,
        Z                   = 0,
        Y                   = 6490,
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
        X                   = 52600,
        Z                   = 0,
        Y                   = 3890,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_205",          # 01, 1
        "Function_2_20B",          # 02, 2
        "Function_3_388",          # 03, 3
        "Function_4_74A",          # 04, 4
        "Function_5_7C7",          # 05, 5
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1D3")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_204")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_A3(0x3FB)
    Event(0, 5)

    label("loc_204")

    Return()

    # Function_0_1A2 end

    def Function_1_205(): pass

    label("Function_1_205")

    OP_22(0x7A, 0x0, 0x64)
    Return()

    # Function_1_205 end

    def Function_2_20B(): pass

    label("Function_2_20B")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_372")

    label("loc_230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_372")

    label("loc_249")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_372")

    label("loc_262")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_372")

    label("loc_27B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_372")

    label("loc_294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_372")

    label("loc_2AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C6")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_372")

    label("loc_2C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_372")

    label("loc_2DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_372")

    label("loc_2F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_372")

    label("loc_311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_372")

    label("loc_32A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_372")

    label("loc_343")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_372")

    label("loc_35C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_372")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_387")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_372")

    label("loc_387")

    Return()

    # Function_2_20B end

    def Function_3_388(): pass

    label("Function_3_388")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 51687, 0, 77948, 225)
    SetChrPos(0x102, 51687, 0, 77948, 225)
    SetChrPos(0x103, 51687, 0, 77948, 225)
    SetChrPos(0x104, 51687, 0, 77948, 225)
    OP_6D(-28590, -250, 8210, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_75(0x4, 0x5, 0x5)
    OP_74(0x4, 0x5, 0x0)
    FadeToBright(2000, 0)
    OP_6D(-23750, -500, 7540, 3000)

    ChrTalk(
        0x9,
        (
            "#210F气温２１度，湿度１５％。\x02\x03",
            "南南西，风速１２亚矩。\x02\x03",
            "周围没有导力反应。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#200F好像也没有军队巡逻……\x02\x03",
            "开动导力引擎。\x01",
            "开始向船体各部分传送导力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "收到。\x01",
            "开动导力引擎。\x02",
        )
    )

    CloseMessageWindow()
    OP_74(0x4, 0x5, 0x0)
    Sleep(100)
    OP_74(0x4, 0x5, 0x1)
    Sleep(100)
    OP_74(0x4, 0x5, 0x2)
    Sleep(100)
    OP_74(0x4, 0x5, 0x3)
    Sleep(100)
    OP_74(0x4, 0x5, 0x4)
    Sleep(100)
    OP_74(0x4, 0x5, 0x5)
    Sleep(100)
    OP_74(0x4, 0x5, 0x6)
    Sleep(100)
    OP_74(0x4, 0x5, 0x7)
    Sleep(100)
    OP_43(0xA, 0x3, 0x0, 0x4)
    Sleep(500)

    ChrTalk(
        0xA,
        "开始向各部分传送导力。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(48020, 0, 5490, 0)
    OP_0D()

    ChrTalk(
        0xC,
        "#3P导力浮板开始运作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "导力驱动开始运作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "水平尾翼也ＯＫ了！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-22333, 650, 4849, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#200F好了……\x02\x03",
            "#201F卡普亚空贼团所属的『山猫号』\x01",
            "——起航！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "收到。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/R1403   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_388 end

    def Function_4_74A(): pass

    label("Function_4_74A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C6")
    OP_74(0x4, 0x5, 0x8)
    Sleep(100)
    OP_74(0x4, 0x5, 0x9)
    Sleep(100)
    OP_74(0x4, 0x5, 0xA)
    Sleep(100)
    OP_74(0x4, 0x5, 0xB)
    Sleep(100)
    OP_74(0x4, 0x5, 0xC)
    Sleep(100)
    OP_74(0x4, 0x5, 0xD)
    Sleep(100)
    OP_74(0x4, 0x5, 0xE)
    Sleep(100)
    OP_74(0x4, 0x5, 0xF)
    Sleep(100)
    Jump("Function_4_74A")

    label("loc_7C6")

    Return()

    # Function_4_74A end

    def Function_5_7C7(): pass

    label("Function_5_7C7")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_71(0x2, 0x4)
    OP_72(0x1, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0x9, 0x4)
    OP_7A(0x9, 0x2)
    OP_7B()
    OP_6D(-23750, -500, 7540, 0)
    SetChrPos(0x101, 51687, 0, 77948, 100)
    SetChrPos(0x102, 51187, 0, 77448, 100)
    SetChrPos(0x103, 51187, 0, 77448, 100)
    SetChrPos(0x104, 51187, 0, 77448, 100)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#200F驱动率固定在４０％。\x01",
            "就这样维持航行速度。\x02\x03",
            "不过，\x01",
            "要随时准备将其切换成战斗速度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "收到。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#211F哈哈，\x01",
            "天亮前应该就能到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#200F是啊。\x02\x03",
            "虽然很想早点休息，\x01",
            "不过必须先向多伦大哥报告一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x0, 0x2)
    OP_43(0xD, 0x1, 0x0, 0x2)
    Sleep(300)
    Fade(1000)
    OP_6D(48020, 0, 5490, 0)
    Sleep(1500)
    OP_22(0x82, 0x0, 0x64)
    Sleep(500)
    OP_62(0xE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)
    OP_8C(0xE, 0, 400)
    Sleep(200)

    ChrTalk(
        0xE,
        "……咦…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "好像有什么声音。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 400)
    Sleep(200)

    ChrTalk(
        0xC,
        (
            "#3P唔？\x01",
            "我什么也没听见啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "好奇怪。\x01",
            "应该是从船舱的方向……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xE, 0xCAA3, 0x0, 0x1B04, 0xBB8, 0x0)
    OP_8E(0xE, 0xC070, 0xFFFFF830, 0x1B04, 0xBB8, 0x0)
    Fade(1000)
    OP_6D(47960, 0, 77660, 0)
    SetChrPos(0xE, 50750, 1500, 77980, 0)
    OP_8E(0xE, 0xBC00, 0x0, 0x12F00, 0xBB8, 0x0)
    OP_8C(0xE, 180, 400)

    ChrTalk(
        0xE,
        (
            "啊……\x01",
            "也许是老鼠吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "有空再打扫一下好了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 90, 400)
    OP_8E(0xE, 0xC684, 0x5DC, 0x1304C, 0xBB8, 0x0)

    def lambda_B83():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B83)

    def lambda_B95():
        OP_8E(0xFE, 0xCF9E, 0xBB8, 0x12FDE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_B95)
    Sleep(1000)

    def lambda_BB5():
        OP_6B(2400, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BB5)
    OP_6D(52782, 0, 77100, 5000)
    SetChrFlags(0xE, 0x80)
    OP_20(0x7D0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C1401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_7C7 end

    SaveToFile()

Try(main)
