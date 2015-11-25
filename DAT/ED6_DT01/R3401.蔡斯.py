from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3401   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
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
        '艾尔·雷登关所方向',                   # 13
        '蔡斯方向',                             # 14
        ' ',                                    # 15
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
        'ED6_DT09/CH10750 ._CH',             # 00
        'ED6_DT07/CH00160 ._CH',             # 01
        'ED6_DT07/CH00162 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00101 ._CH',             # 04
        'ED6_DT07/CH00110 ._CH',             # 05
        'ED6_DT07/CH00111 ._CH',             # 06
        'ED6_DT07/CH00102 ._CH',             # 07
        'ED6_DT07/CH00161 ._CH',             # 08
        'ED6_DT09/CH10130 ._CH',             # 09
        'ED6_DT09/CH10131 ._CH',             # 0A
        'ED6_DT09/CH10750 ._CH',             # 0B
        'ED6_DT09/CH10751 ._CH',             # 0C
        'ED6_DT09/CH10760 ._CH',             # 0D
        'ED6_DT09/CH10761 ._CH',             # 0E
        'ED6_DT09/CH10770 ._CH',             # 0F
        'ED6_DT09/CH10771 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT09/CH10750P._CP',             # 00
        'ED6_DT07/CH00160P._CP',             # 01
        'ED6_DT07/CH00162P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00101P._CP',             # 04
        'ED6_DT07/CH00110P._CP',             # 05
        'ED6_DT07/CH00111P._CP',             # 06
        'ED6_DT07/CH00102P._CP',             # 07
        'ED6_DT07/CH00161P._CP',             # 08
        'ED6_DT09/CH10130P._CP',             # 09
        'ED6_DT09/CH10131P._CP',             # 0A
        'ED6_DT09/CH10750P._CP',             # 0B
        'ED6_DT09/CH10751P._CP',             # 0C
        'ED6_DT09/CH10760P._CP',             # 0D
        'ED6_DT09/CH10761P._CP',             # 0E
        'ED6_DT09/CH10770P._CP',             # 0F
        'ED6_DT09/CH10771P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x0,
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
        ChipIndex           = 0x0,
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
        ChipIndex           = 0x0,
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
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 169300,
        Z                   = 0,
        Y                   = -27030,
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

    DeclNpc(
        X                   = 330710,
        Z                   = 0,
        Y                   = -37560,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 257600,
        Z                   = 70,
        Y                   = -24310,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 286240,
        Z                   = 20,
        Y                   = -35830,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 222300,
        Y                   = -1000,
        Z                   = -28000,
        Range               = 217700,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF6CBC,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 199000,
        TriggerZ            = 500,
        TriggerY            = -22200,
        TriggerRange        = 800,
        ActorX              = 199000,
        ActorZ              = 1500,
        ActorY              = -22200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 285640,
        TriggerZ            = 0,
        TriggerY            = -26290,
        TriggerRange        = 1000,
        ActorX              = 285640,
        ActorZ              = 1000,
        ActorY              = -26290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_2B3",          # 01, 1
        "Function_2_324",          # 02, 2
        "Function_3_4AC",          # 03, 3
        "Function_4_637",          # 04, 4
        "Function_5_1E52",         # 05, 5
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Return()

    # Function_0_2B2 end

    def Function_1_2B3(): pass

    label("Function_1_2B3")

    OP_16(0x2, 0xFA0, 0x1F018, 0xFFFD9AB8, 0x30038)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2DA")
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_64(0x0, 0x1)

    label("loc_2DA")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 285640, 1000, -26290, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_2B3 end

    def Function_2_324(): pass

    label("Function_2_324")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_496")

    label("loc_354")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_496")

    label("loc_36D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_496")

    label("loc_386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_496")

    label("loc_39F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B8")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_496")

    label("loc_3B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_496")

    label("loc_3D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EA")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_496")

    label("loc_3EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_403")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_496")

    label("loc_403")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_496")

    label("loc_41C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_435")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_496")

    label("loc_435")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_496")

    label("loc_44E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_467")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_496")

    label("loc_467")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_480")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_496")

    label("loc_480")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_496")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_496")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_496")

    label("loc_4AB")

    Return()

    # Function_2_324 end

    def Function_3_4AC(): pass

    label("Function_3_4AC")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C9")
    OP_A2(0x504)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FE")

    ChrTalk(
        0x101,
        (
            "#004F咦……\x01",
            "这个照明灯，是不是有点怪呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_534")

    label("loc_4FE")


    ChrTalk(
        0x101,
        (
            "#004F咦……\x01",
            "那个照明灯，是不是有点怪呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_534")


    ChrTalk(
        0x102,
        (
            "#012F确实是。\x01",
            "应该是有点故障了。\x02\x03",
            "导力器的导力\x01",
            "是可以自动积蓄的，\x01",
            "所以，我想应该不用担心……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_634")

    label("loc_5C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_600")

    ChrTalk(
        0x101,
        "#000F照明灯好像有点怪怪的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_634")

    label("loc_600")


    ChrTalk(
        0x102,
        (
            "#015F照明灯有点闪烁。\x01",
            "看来有点故障了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_634")

    EventEnd(0x1)
    Return()

    # Function_3_4AC end

    def Function_4_637(): pass

    label("Function_4_637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E51")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_A2(0x506)
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 197700, 0, -23200, 45)
    SetChrPos(0x9, 199000, 0, -24200, 0)
    SetChrPos(0xA, 200900, 0, -24200, 315)
    SetChrPos(0xB, 200600, 0, -23100, 315)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)

    NpcTalk(
        0x8,
        "女孩子的声音",
        "啊——！\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6C(45000, 0)
    OP_6D(200700, 2000, -24400, 0)
    OP_31(0x6, 0x0, 0x12)
    OP_B5(0x6, 0x0)
    OP_B5(0x6, 0x1)
    OP_B5(0x6, 0x5)
    OP_B5(0x6, 0x4)
    OP_41(0x6, 0xB5)
    OP_41(0x6, 0xF4)
    OP_41(0x6, 0x112)
    OP_41(0x6, 0x2C9, 0x0)
    OP_41(0x6, 0x271, 0x1)
    OP_41(0x6, 0x262, 0x5)
    OP_41(0x6, 0x26B, 0x4)
    OP_35(0x6, 0xD2)
    OP_36(0x6, 0x104)
    AddParty(0x6, 0xFF)
    SetChrPos(0x107, 204300, 0, -26400, 270)
    OP_0D()
    OP_21()
    OP_1D(0x56)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    Sleep(500)
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(
        0x107,
        "小女孩",
        (
            "#065F#2P已、已经聚集了\x01",
            "这么多只魔兽啊～……\x02\x03",
            "这样下去会坏掉的……\x02\x03",
            "既、既然这样的话……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_81F():
        OP_6B(2600, 2500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_81F)
    Sleep(1000)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 2)
    OP_51(0x107, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    Sleep(500)
    TurnDirection(0x107, 0xA, 0)

    NpcTalk(
        0x107,
        "小女孩",
        "#062F#2P方向ＯＫ，仰角２０度……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    NpcTalk(
        0x107,
        "小女孩",
        (
            "#062F导力填充率３０％……\x02\x03",
            "#068F……发射！！\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x2, "map\\\\mp019_00.eff")

    def lambda_901():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_901)
    SetChrChipByIndex(0x107, 2)
    SetChrPos(0xE, 196500, 1500, -22500, 0)
    OP_22(0x1FA, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x107, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_99(0x107, 0x0, 0x3, 0x7D0)
    OP_99(0x107, 0x3, 0x7, 0x7D0)

    def lambda_979():
        OP_94(0x1, 0xFE, 0x78, 0x384, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_979)

    def lambda_98F():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_98F)

    def lambda_9A5():
        OP_94(0x1, 0xFE, 0xE6, 0x2BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9A5)

    def lambda_9BB():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9BB)
    Sleep(1000)
    WaitChrThread(0x8, 0x1)

    def lambda_9DB():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9DB)
    WaitChrThread(0x9, 0x1)

    def lambda_9EE():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9EE)
    WaitChrThread(0xA, 0x1)

    def lambda_A01():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A01)
    WaitChrThread(0xB, 0x1)

    def lambda_A14():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A14)
    OP_8C(0x107, 270, 0)
    Sleep(400)

    NpcTalk(
        0x107,
        "小女孩",
        (
            "#062F#2P再、再靠近的话，\x01",
            "这次真的会打中你们哦！\x02\x03",
            "真、真的哦，我是认真的！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(300)
    OP_62(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(100)
    OP_62(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(100)
    OP_62(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(200)
    Sleep(1000)

    def lambda_AE6():
        OP_6D(201700, 2000, -25100, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE6)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)

    def lambda_B12():
        OP_94(0x0, 0xFE, 0x0, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B12)
    OP_63(0xA)
    Sleep(300)

    def lambda_B30():
        OP_94(0x0, 0xFE, 0x0, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B30)
    OP_63(0xB)

    def lambda_B49():
        OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B49)
    OP_63(0x9)
    Sleep(600)

    def lambda_B67():
        OP_94(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B67)
    OP_63(0x8)
    SetChrChipByIndex(0x107, 1)
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1700)

    NpcTalk(
        0x107,
        "小女孩",
        (
            "#065F#2P啊……\x01",
            "起、起到反效果了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 210200, 0, -30000, 0)
    SetChrPos(0x102, 209330, 0, -30000, 0)
    SetChrFlags(0x102, 0x4)

    def lambda_C0F():
        OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C0F)
    Sleep(150)

    def lambda_C2A():
        OP_94(0x0, 0xFE, 0x0, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C2A)

    def lambda_C40():
        OP_94(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C40)
    Sleep(300)

    def lambda_C5B():
        OP_94(0x0, 0xFE, 0x0, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C5B)
    Sleep(400)

    NpcTalk(
        0x107,
        "小女孩",
        "#069F#2P呀……！\x02",
    )

    OP_9E(0x107, 0x14, 0x0, 0x190, 0xFA0)
    CloseMessageWindow()

    def lambda_CA6():
        OP_94(0x0, 0xA, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CA6)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)

    def lambda_CD0():
        OP_6B(3160, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CD0)

    def lambda_CE0():
        OP_6D(203200, 0, -24900, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CE0)

    def lambda_CF8():
        OP_6C(78000, 1200)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CF8)

    ChrTalk(
        0x101,
        "#10A#1P喔喔喔喔喔！\x05\x02",
    )

    OP_8E(0x101, 0x326F4, 0x0, 0xFFFF9886, 0x2710, 0x0)

    def lambda_D32():
        OP_8E(0xFE, 0x317B8, 0x0, 0xFFFF952A, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D32)

    def lambda_D4D():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_D4D)
    SetChrFlags(0x107, 0x1000)
    SetChrChipByIndex(0x107, 8)

    def lambda_D65():
        OP_8F(0xFE, 0x3214A, 0x0, 0xFFFF9566, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_D65)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 7)

    def lambda_D90():
        OP_99(0xFE, 0x0, 0xC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D90)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0x1F4, 0x0, 0x64)
    OP_96(0x101, 0x31830, 0x0, 0xFFFF9C00, 0x5DC, 0x1770)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, 202800, 0, -25600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_E07():
        OP_94(0x1, 0xA, 0xB4, 0x7D0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E07)
    OP_96(0x101, 0x31A92, 0x0, 0xFFFF9A52, 0x1F4, 0x1388)

    def lambda_E34():
        OP_94(0x1, 0xFE, 0xB4, 0x384, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E34)

    def lambda_E4A():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E4A)

    def lambda_E60():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E60)
    WaitChrThread(0x102, 0x1)
    SetChrChipByIndex(0x102, 5)
    ClearChrFlags(0x102, 0x4)
    Sleep(1000)

    NpcTalk(
        0x107,
        "小女孩",
        "#065F咦……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x107, 1)
    ClearChrFlags(0x107, 0x1000)
    TurnDirection(0x107, 0x101, 400)

    NpcTalk(
        0x107,
        "小女孩",
        "#560F啊，刚才的……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F待会再慢慢聊吧！\x01",
            "你先退到我们后面去！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F总之\x01",
            "先把这些家伙赶走吧！\x02",
        )
    )

    CloseMessageWindow()
    Battle(0x3A7, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_F49"),
        (SWITCH_DEFAULT, "loc_F4C"),
    )


    label("loc_F49")

    OP_B4(0x0)
    Return()

    label("loc_F4C")

    EventBegin(0x0)
    OP_4F(0x23, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x101, 202800, 0, -25600, 315)
    SetChrPos(0x102, 202500, 0, -27300, 315)
    SetChrPos(0x107, 204200, 0, -26900, 315)
    OP_6D(203400, 0, -26050, 0)
    SetChrChipByIndex(0x107, 65535)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x107,
        "小女孩",
        (
            "#065F真、真是吓死人了～……\x02\x03",
            "#067F那个那个……\x01",
            "真是非常感谢呢。\x02\x03",
            "救了我一命呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)

    def lambda_1040():
        OP_6B(2790, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1040)
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x107, 400)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x107, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈。\x01",
            "你没事就好了。\x02\x03",
            "#006F不过……\x01",
            "以后可要吸取教训哦。\x02\x03",
            "一个人和魔兽战斗\x01",
            "这种危险的事可不能做哦。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x107,
        "小女孩",
        (
            "#065F啊，但是但是……\x02\x03",
            "如果放着不管的话，\x01",
            "隧道的照明灯会坏掉呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F这么说来……\x02\x03",
            "为什么魔兽会聚集在\x01",
            "熄灭了的照明灯周围呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_12D6")

    ChrTalk(
        0x102,
        (
            "#010F以前在更换路灯的时候\x01",
            "不是也发生过同样的事吗？\x02\x03",
            "因为导力器里的七耀石\x01",
            "是魔兽喜欢的东西。\x02\x03",
            "因此路灯里\x01",
            "都带有驱赶魔兽的机能……\x02\x03",
            "如果这种机能坏了的话，\x01",
            "自然就会容易吸引魔兽过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1392")

    label("loc_12D6")


    ChrTalk(
        0x102,
        (
            "#010F因为导力器里的七耀石\x01",
            "是魔兽喜欢的东西。\x02\x03",
            "因此路灯里\x01",
            "都带有驱赶魔兽的机能……\x02\x03",
            "如果这种机能坏了的话，\x01",
            "自然就会容易吸引魔兽过来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1392")


    ChrTalk(
        0x101,
        (
            "#501F啊，原来是这样啊。\x02\x03",
            "#007F不过就算这样，\x01",
            "也不能这么胡来啊。\x02\x03",
            "万一受伤的话可就不好了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x107,
        "小女孩",
        (
            "#063F啊……\x01",
            "对、对不起……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F好了好了，到此为止吧。\x02\x03",
            "更何况，『不能胡来』从你嘴里说出来，\x01",
            "可是完全没有说服力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F讨厌，少泼冷水啦。\x02\x03",
            "#006F算了……\x01",
            "我叫艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我是约修亚。\x02\x03",
            "我们俩都是\x01",
            "游击士协会的见习游击士。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x107,
        "小女孩",
        (
            "#061F哇～～\x01",
            "难怪那么厉害呢……\x02\x03",
            "#060F我叫提妲。\x02\x03",
            "现在正在\x01",
            "蔡斯的中央工房实习。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嘿嘿～\x01",
            "所以才会打扮成这样吧。\x02\x03",
            "那么，提妲。\x02\x03",
            "你要回蔡斯的话，\x01",
            "就和我们一起走吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x01",
            "如果再遇到魔兽就糟糕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F真、真的吗？\x01",
            "真是非常感谢呢。\x02\x03",
            "#560F啊，不过请稍等一下。\x01",
            "　\x02\x03",
            "我得先修理好那个照明灯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊，那也是。\x01",
            "这样放着不管的确非常危险。\x02\x03",
            "不过……\x01",
            "你是怎么知道这里的照明灯坏了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，我在调查电脑的\x01",
            "数据库的时候偶然发现的。\x02\x03",
            "好像当初安装时候用的是次品，\x01",
            "而且设置元件也不齐全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此，\x01",
            "那你还是快看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F（电脑？数据库？）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(198940, 30, -23590, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, 199360, 10, -24480, 0)
    SetChrPos(0x102, 198190, 20, -24530, 0)
    SetChrPos(0x107, 199160, 20, -22710, 0)
    SetChrFlags(0x107, 0x4)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x107,
        "#062F#4P……嘿咻。\x02",
    )

    CloseMessageWindow()
    OP_72(0x1, 0x4)
    Sleep(100)
    OP_71(0x1, 0x4)
    Sleep(100)
    OP_72(0x1, 0x4)
    Sleep(100)
    OP_71(0x1, 0x4)
    Sleep(90)
    OP_72(0x1, 0x4)
    Sleep(80)
    OP_71(0x1, 0x4)
    Sleep(70)
    OP_72(0x1, 0x4)
    Sleep(60)
    OP_71(0x1, 0x4)
    Sleep(50)
    OP_72(0x1, 0x4)
    Sleep(1000)

    ChrTalk(
        0x107,
        "#560F#4P好～这样就可以了。\x02",
    )

    CloseMessageWindow()
    OP_8F(0x107, 0x309BC, 0x1E, 0xFFFFA4DE, 0x7D0, 0x0)
    OP_8C(0x107, 180, 400)
    ClearChrFlags(0x107, 0x4)

    ChrTalk(
        0x107,
        "#061F#1P让你们久等了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F哎～好厉害。\x01",
            "原来你这么熟练的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F真不愧是\x01",
            "在中央工房的见习生啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F#1P嘿嘿……\x01",
            "这不算什么啦。\x02\x03",
            "只不过是修正接触不良的结晶回路\x01",
            "和调整错乱的导力压而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F？？？\x02\x03",
            "唔……\x01",
            "听起来好像相当复杂的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F其实一点也不复杂。\x02\x03",
            "这个呢，\x01",
            "简单解释起来的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#1K#1P在导力器的内部镶嵌着\x01",
            "可以发挥各种功能的结晶回路。\x01",
            "结晶回路与元件必须准确地\x01",
            "进行连接才能使导力器正常运作，\x01",
            "而当两者出现连接错误时，\x01",
            "导力器生成的导力就会无处可去，\x01",
            "其结果自然就导致\x01",
            "设计时预想的机能无法正常发挥。\x01",
            "以照明灯的情况来说就是发光和驱除魔兽的……\x02",
        )
    )

    Sleep(2000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        "#1K#004F停、停一下！\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(
        0x101,
        (
            "#506F还、还是以后再慢慢解释吧。\x01",
            "我们差不多该出发了呢～\x02\x03",
            "嗯嗯～\x01",
            "站在这里说话也不方便嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F#1P啊，说得也是。\x01",
            "虽然没解释完有点可惜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F（呼……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，\x01",
            "那我们继续前往蔡斯吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FＯＫ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F#1P好的。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    OP_64(0x0, 0x1)
    EventEnd(0x0)

    label("loc_1E51")

    Return()

    # Function_4_637 end

    def Function_5_1E52(): pass

    label("Function_5_1E52")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在此休息\x01",      # 0
            "离开\x01",          # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2071")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 285640, 1000, -26290, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x32)
    OP_73(0x11)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 285640, 1000, -26290, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, 285600, 30, -28390, 13)
    SetChrPos(0x1, 285600, 30, -28390, 13)
    SetChrPos(0x2, 285600, 30, -28390, 13)
    SetChrPos(0x3, 285600, 30, -28390, 13)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 285640, 1000, -26290, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2071")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_208B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_208B")

    Return()

    # Function_5_1E52 end

    SaveToFile()

Try(main)
