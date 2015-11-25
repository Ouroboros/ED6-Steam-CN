from ED6ScenarioHelper import *

def main():
    # 空贼要塞

    CreateScenaFile(
        FileName            = 'C1305   ._SN',
        MapName             = 'Bose',
        Location            = 'C1305.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60031",
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
        '空贼莱尔',                             # 9
        '空贼罗尔',                             # 10
        '空贼',                                 # 11
        '空贼',                                 # 12
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
        Unknown_3A              = 52,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00360 ._CH',             # 00
        'ED6_DT07/CH00364 ._CH',             # 01
        'ED6_DT07/CH00361 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00110 ._CH',             # 04
        'ED6_DT07/CH00120 ._CH',             # 05
        'ED6_DT07/CH00130 ._CH',             # 06
        'ED6_DT09/CH10380 ._CH',             # 07
        'ED6_DT09/CH10381 ._CH',             # 08
        'ED6_DT09/CH10390 ._CH',             # 09
        'ED6_DT09/CH10391 ._CH',             # 0A
        'ED6_DT09/CH10250 ._CH',             # 0B
        'ED6_DT09/CH10251 ._CH',             # 0C
        'ED6_DT06/CH20074 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH00360P._CP',             # 00
        'ED6_DT07/CH00364P._CP',             # 01
        'ED6_DT07/CH00361P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00110P._CP',             # 04
        'ED6_DT07/CH00120P._CP',             # 05
        'ED6_DT07/CH00130P._CP',             # 06
        'ED6_DT09/CH10380P._CP',             # 07
        'ED6_DT09/CH10381P._CP',             # 08
        'ED6_DT09/CH10390P._CP',             # 09
        'ED6_DT09/CH10391P._CP',             # 0A
        'ED6_DT09/CH10250P._CP',             # 0B
        'ED6_DT09/CH10251P._CP',             # 0C
        'ED6_DT06/CH20074P._CP',             # 0D
    )

    DeclNpc(
        X                   = -2300,
        Z                   = 500,
        Y                   = -2700,
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
        X                   = 1000,
        Z                   = 500,
        Y                   = -1900,
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
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
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
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
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


    DeclMonster(
        X                   = -5080,
        Z                   = 0,
        Y                   = 890,
        Unknown_0C          = 133,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xA4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1060,
        Z                   = 0,
        Y                   = -138590,
        Unknown_0C          = 267,
        Unknown_0E          = 11,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xAB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 65660,
        Z                   = 0,
        Y                   = -21310,
        Unknown_0C          = 167,
        Unknown_0E          = 11,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xAB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -51050,
        TriggerZ            = 0,
        TriggerY            = -136010,
        TriggerRange        = 800,
        ActorX              = -51050,
        ActorZ              = 1000,
        ActorY              = -136010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -164160,
        TriggerZ            = 0,
        TriggerY            = -193160,
        TriggerRange        = 1000,
        ActorX              = -164160,
        ActorZ              = 1500,
        ActorY              = -193160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -54870,
        TriggerZ            = 0,
        TriggerY            = 46490,
        TriggerRange        = 1000,
        ActorX              = -54740,
        ActorZ              = 1500,
        ActorY              = 47090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -206690,
        TriggerZ            = 0,
        TriggerY            = -155420,
        TriggerRange        = 1000,
        ActorX              = -206660,
        ActorZ              = 1500,
        ActorY              = -154670,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_27E",          # 00, 0
        "Function_1_34D",          # 01, 1
        "Function_2_3DA",          # 02, 2
        "Function_3_3F0",          # 03, 3
        "Function_4_654",          # 04, 4
        "Function_5_76E",          # 05, 5
        "Function_6_BC8",          # 06, 6
        "Function_7_D11",          # 07, 7
        "Function_8_E59",          # 08, 8
    )


    def Function_0_27E(): pass

    label("Function_0_27E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (117, "loc_28A"),
        (SWITCH_DEFAULT, "loc_29D"),
    )


    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29A")
    Event(0, 5)

    label("loc_29A")

    Jump("loc_29D")

    label("loc_29D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 3)), scpexpr(EXPR_END)), "loc_34C")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -116480, 0, 2830, 80)
    SetChrPos(0x9, -117700, 0, 3160, 360)
    SetChrPos(0xA, -119190, 0, 2820, 125)
    SetChrPos(0xB, -119490, 0, 1060, 200)
    SetChrChipByIndex(0xA, 13)
    SetChrChipByIndex(0xB, 13)
    SetChrChipByIndex(0x8, 13)
    SetChrChipByIndex(0x9, 13)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)

    label("loc_34C")

    Return()

    # Function_0_27E end

    def Function_1_34D(): pass

    label("Function_1_34D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F")
    OP_6F(0x1, 0)
    Jump("loc_366")

    label("loc_35F")

    OP_6F(0x1, 60)

    label("loc_366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_378")
    OP_6F(0x2, 0)
    Jump("loc_37F")

    label("loc_378")

    OP_6F(0x2, 60)

    label("loc_37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_391")
    OP_6F(0x3, 0)
    Jump("loc_398")

    label("loc_391")

    OP_6F(0x3, 60)

    label("loc_398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B0")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_3B9")

    label("loc_3B0")

    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)

    label("loc_3B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D5")
    OP_1B(0x22, 0x0, 0x3)
    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    Jump("loc_3D9")

    label("loc_3D5")

    OP_64(0x0, 0x1)

    label("loc_3D9")

    Return()

    # Function_1_34D end

    def Function_2_3DA(): pass

    label("Function_2_3DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3DA")

    label("loc_3EF")

    Return()

    # Function_2_3DA end

    def Function_3_3F0(): pass

    label("Function_3_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_653")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_53A")

    def lambda_41A():
        OP_6D(-46410, 0, -137150, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_41A)
    Sleep(600)
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x102,
        (
            "#012F等一下……\x02\x03",
            "从那道门可以听到说话的声音。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_497():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_497)

    def lambda_4A5():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A5)
    OP_8C(0x103, 270, 400)

    ChrTalk(
        0x103,
        (
            "#022F看起来空贼就在这里呢。\x01",
            "先把他们解决掉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_638")

    label("loc_53A")


    def lambda_540():
        OP_6D(-46410, 0, -137150, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_540)
    Sleep(600)
    OP_8C(0x104, 270, 400)

    ChrTalk(
        0x104,
        (
            "#033F哎呀……\x02\x03",
            "从那道门可以听到说话的声音呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CC():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5CC)

    def lambda_5DA():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DA)
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        (
            "#002F难道是空贼？\x01",
            "那先把这里解决掉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_638")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_653")

    Return()

    # Function_3_3F0 end

    def Function_4_654(): pass

    label("Function_4_654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76D")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有男人说话的声音传出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x102,
        (
            "#012F好像有空贼的成员在里面，\x01",
            "……要闯进去吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【闯进去】\x01",        # 0
            "【还是算了】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_759"),
        (0, "loc_75E"),
        (SWITCH_DEFAULT, "loc_76D"),
    )


    label("loc_759")

    EventEnd(0x1)
    Jump("loc_76D")

    label("loc_75E")

    OP_A2(0x3FA)
    NewScene("ED6_DT01/C1304   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_76D")

    label("loc_76D")

    Return()

    # Function_4_654 end

    def Function_5_76E(): pass

    label("Function_5_76E")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-114820, 0, -1080, 0)
    OP_6B(2800, 0)
    SetChrPos(0x8, -113140, 0, -920, 225)
    SetChrPos(0x9, -113210, 0, 90, 225)
    SetChrPos(0xA, -112860, 0, 1370, 225)
    SetChrPos(0xB, -112680, 0, -2000, 270)
    SetChrPos(0x101, -116790, 0, -2600, 90)
    SetChrPos(0x102, -118090, 0, -3150, 90)
    SetChrPos(0x103, -117660, 0, -1530, 90)
    SetChrPos(0x104, -117180, 0, -4120, 45)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x103, 5)
    SetChrChipByIndex(0x104, 6)

    ChrTalk(
        0x8,
        "#2P嘁，果然来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "我们根本没想过要赢！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "只要争取到能让\x01",
            "大哥他们逃跑的时间就够了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F呵呵，为了保护首领\x01",
            "而情愿将自身当作盾牌吗……\x02\x03",
            "虽说有点愚蠢，\x01",
            "但却是值得敬佩的气概嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F那我们全力作战\x01",
            "也算是对他们的尊重吧……\x02\x03",
            "#024F来吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    SetChrChipByIndex(0xA, 2)
    SetChrChipByIndex(0xB, 2)
    SetChrChipByIndex(0x8, 2)
    SetChrChipByIndex(0x9, 2)

    def lambda_A34():
        OP_92(0xFE, 0x102, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A34)

    def lambda_A49():
        OP_92(0xFE, 0x102, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A49)

    def lambda_A5E():
        OP_92(0xFE, 0x102, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A5E)

    def lambda_A73():
        OP_92(0xFE, 0x102, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A73)
    Sleep(400)
    Battle(0x38C, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_AA0"),
        (SWITCH_DEFAULT, "loc_AA3"),
    )


    label("loc_AA0")

    OP_B4(0x0)
    Return()

    label("loc_AA3")

    SetChrPos(0x8, -116480, 0, 2830, 80)
    SetChrPos(0x9, -117700, 0, 3160, 360)
    SetChrPos(0xA, -119190, 0, 2820, 125)
    SetChrPos(0xB, -119490, 0, 1060, 200)
    SetChrChipByIndex(0xA, 13)
    SetChrChipByIndex(0xB, 13)
    SetChrChipByIndex(0x8, 13)
    SetChrChipByIndex(0x9, 13)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    SetChrPos(0x101, -115860, 0, 30, 270)
    SetChrPos(0x102, -115860, 0, 30, 270)
    SetChrPos(0x103, -115860, 0, 30, 270)
    SetChrPos(0x104, -115860, 0, 30, 270)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x104, 65535)
    OP_6D(-115860, 0, 30, 0)
    OP_6B(2600, 0)
    FadeToBright(1000, 0)
    OP_A2(0x35B)
    EventEnd(0x0)
    Return()

    # Function_5_76E end

    def Function_6_BC8(): pass

    label("Function_6_BC8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x14E, 1)"), scpexpr(EXPR_END)), "loc_C41")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "宝石戒指\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x389)
    Jump("loc_CBD")

    label("loc_C41")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "宝石戒指\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "宝石戒指\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_CBD")

    Jump("loc_D03")

    label("loc_CC0")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x10)

    label("loc_D03")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_BC8 end

    def Function_7_D11(): pass

    label("Function_7_D11")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3F, 1)"), scpexpr(EXPR_END)), "loc_D86")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "毒蝎鞭\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x36E)
    Jump("loc_DFA")

    label("loc_D86")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "毒蝎鞭\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "毒蝎鞭\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_DFA")

    Jump("loc_E4B")

    label("loc_DFD")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x11)

    label("loc_E4B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_D11 end

    def Function_8_E59(): pass

    label("Function_8_E59")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F48")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_ECF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x36F)
    Jump("loc_F45")

    label("loc_ECF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_F45")

    Jump("loc_F9C")

    label("loc_F48")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x12)

    label("loc_F9C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_E59 end

    SaveToFile()

Try(main)
