from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4311   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4311.x',
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
        '管家雷蒙德',                           # 9
        '特务兵',                               # 10
        '特务兵',                               # 11
        '特务兵',                               # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '科洛丝',                               # 15
        '奥利维尔',                             # 16
        '雪拉',                                 # 17
        '尤莉亚中尉',                           # 18
        '基库',                                 # 19
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
        'ED6_DT07/CH01570 ._CH',             # 06
        'ED6_DT07/CH01330 ._CH',             # 07
        'ED6_DT06/CH20143 ._CH',             # 08
        'ED6_DT07/CH00030 ._CH',             # 09
        'ED6_DT07/CH00020 ._CH',             # 0A
        'ED6_DT07/CH02090 ._CH',             # 0B
        'ED6_DT07/CH02320 ._CH',             # 0C
        'ED6_DT06/CH20042 ._CH',             # 0D
        'ED6_DT06/CH20113 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH00100P._CP',             # 00
        'ED6_DT07/CH00101P._CP',             # 01
        'ED6_DT07/CH00110P._CP',             # 02
        'ED6_DT07/CH00111P._CP',             # 03
        'ED6_DT07/CH00170P._CP',             # 04
        'ED6_DT07/CH00171P._CP',             # 05
        'ED6_DT07/CH01570P._CP',             # 06
        'ED6_DT07/CH01330P._CP',             # 07
        'ED6_DT06/CH20143P._CP',             # 08
        'ED6_DT07/CH00030P._CP',             # 09
        'ED6_DT07/CH00020P._CP',             # 0A
        'ED6_DT07/CH02090P._CP',             # 0B
        'ED6_DT07/CH02320P._CP',             # 0C
        'ED6_DT06/CH20042P._CP',             # 0D
        'ED6_DT06/CH20113P._CP',             # 0E
    )

    DeclNpc(
        X                   = -11850,
        Z                   = 0,
        Y                   = 20220,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 25980,
        TriggerZ            = 0,
        TriggerY            = 50580,
        TriggerRange        = 800,
        ActorX              = 25690,
        ActorZ              = 1500,
        ActorY              = 51500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22140,
        TriggerZ            = 0,
        TriggerY            = 50600,
        TriggerRange        = 800,
        ActorX              = 21830,
        ActorZ              = 890,
        ActorY              = 51760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18200,
        TriggerZ            = 0,
        TriggerY            = 51350,
        TriggerRange        = 800,
        ActorX              = 18200,
        ActorZ              = 1800,
        ActorY              = 51350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14200,
        TriggerZ            = 0,
        TriggerY            = 51310,
        TriggerRange        = 800,
        ActorX              = 14200,
        ActorZ              = 2000,
        ActorY              = 51310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10220,
        TriggerZ            = 0,
        TriggerY            = 51150,
        TriggerRange        = 800,
        ActorX              = 10220,
        ActorZ              = 1200,
        ActorY              = 51150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 24340,
        TriggerZ            = 0,
        TriggerY            = 45480,
        TriggerRange        = 800,
        ActorX              = 24340,
        ActorZ              = 500,
        ActorY              = 45480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13210,
        TriggerZ            = 0,
        TriggerY            = 18820,
        TriggerRange        = 800,
        ActorX              = -11850,
        ActorZ              = 1500,
        ActorY              = 20220,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_37E",          # 00, 0
        "Function_1_450",          # 01, 1
        "Function_2_451",          # 02, 2
        "Function_3_467",          # 03, 3
        "Function_4_46C",          # 04, 4
        "Function_5_958",          # 05, 5
        "Function_6_1996",         # 06, 6
        "Function_7_1B1A",         # 07, 7
        "Function_8_1BF0",         # 08, 8
        "Function_9_1CDC",         # 09, 9
        "Function_10_1DCA",        # 0A, 10
        "Function_11_1ECC",        # 0B, 11
        "Function_12_3057",        # 0C, 12
    )


    def Function_0_37E(): pass

    label("Function_0_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_395")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 11)

    label("loc_395")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_3A1"),
        (SWITCH_DEFAULT, "loc_3B4"),
    )


    label("loc_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B1")
    Event(0, 5)

    label("loc_3B1")

    Jump("loc_3B4")

    label("loc_3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_END)), "loc_44F")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrPos(0x9, -11150, 0, 15510, 315)
    SetChrPos(0xA, -11000, 0, 17300, 0)
    SetChrPos(0xB, -12500, 0, 17280, 270)
    SetChrPos(0xC, -13000, 0, 16040, 225)
    SetChrChipByIndex(0x9, 13)
    SetChrChipByIndex(0xA, 13)
    SetChrChipByIndex(0xB, 13)
    SetChrChipByIndex(0xC, 13)

    label("loc_44F")

    Return()

    # Function_0_37E end

    def Function_1_450(): pass

    label("Function_1_450")

    Return()

    # Function_1_450 end

    def Function_2_451(): pass

    label("Function_2_451")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_466")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_451")

    label("loc_466")

    Return()

    # Function_2_451 end

    def Function_3_467(): pass

    label("Function_3_467")

    Call(0, 4)
    Return()

    # Function_3_467 end

    def Function_4_46C(): pass

    label("Function_4_46C")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_511")
    OP_20(0xBB8)
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
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_511")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52B")
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    label("loc_52B")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_END)), "loc_596")

    ChrTalk(
        0x8,
        "对对，就是那个钥匙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果有了那个，\x01",
            "就可以进入『纹章之间』了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_954")

    label("loc_596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_END)), "loc_627")

    ChrTalk(
        0x8,
        (
            "还有一把备用钥匙\x01",
            "是保管在某个地方的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我记得……\x01",
            "应该是藏匿在展示室里面的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_954")

    label("loc_627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CD")
    OP_A2(0x679)
    OP_28(0x4C, 0x1, 0x10)
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "众人向管家说明了深处的门被锁上了的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "是啊，\x01",
            "那里是被锁上了的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "开那扇门的钥匙\x01",
            "是由情报部的中队长保管的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "因为出现了恐怖分子，\x01",
            "中队长好像出动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F也就是说，\x01",
            "是到尤莉亚中尉他们埋伏的地方去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F嗯，这可就麻烦了，\x01",
            "没时间回去了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "等等……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "还有一把备用钥匙\x01",
            "是保管在某个地方的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我想应该是\x01",
            "藏匿在展示室里面……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F展示室！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F立刻去调查。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_954")

    label("loc_8CD")


    ChrTalk(
        0x8,
        "谢谢你们救了我。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P对了，如果感到疲劳，\x01",
            "就回到这里休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P我给你们准备饮料。\x02",
    )

    CloseMessageWindow()

    label("loc_954")

    TalkEnd(0x8)
    Return()

    # Function_4_46C end

    def Function_5_958(): pass

    label("Function_5_958")

    EventBegin(0x0)
    OP_6D(-11300, 0, 20870, 0)
    OP_67(0, 6220, -10000, 0)
    OP_6B(1820, 0)
    OP_6C(45000, 0)
    OP_6E(487, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0x8, -11780, 0, 20150, 225)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -16850, 0, 13660, 45)
    SetChrPos(0x108, -18160, 0, 13760, 45)
    SetChrPos(0x102, -16690, 0, 12820, 45)
    SetChrPos(0x9, -10960, 0, 18200, 0)
    SetChrPos(0xA, -12000, 0, 18190, 0)
    SetChrPos(0xB, -14950, 0, 18980, 90)
    SetChrPos(0xC, -13770, 0, 18980, 270)
    FadeToBright(1000, 0)
    OP_6D(-14900, 0, 16920, 2000)
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "你、你们几个是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哇……\x01",
            "聚集了不少人啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    def lambda_B09():
        TurnDirection(0xFE, 0x101, 250)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B09)

    def lambda_B17():
        TurnDirection(0xFE, 0x101, 200)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B17)

    def lambda_B25():
        TurnDirection(0xFE, 0x101, 150)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B25)
    TurnDirection(0xB, 0x101, 200)

    ChrTalk(
        0xB,
        (
            "#5P嗯～……\x01",
            "什么，你们是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P唔～……\x01",
            "怎么我们不认识你们啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F晚上好，\x01",
            "我们是游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F你们就在这里好好睡一觉吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C13():
        OP_92(0xFE, 0x8, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C13)
    Sleep(50)

    def lambda_C2D():
        OP_92(0xFE, 0xA, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C2D)
    Sleep(50)

    def lambda_C47():
        OP_92(0xFE, 0xC, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_C47)
    OP_6D(-13120, 0, 18720, 500)
    OP_44(0x101, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)
    Battle(0x3AF, 0x0, 0x2, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_C8C"),
        (SWITCH_DEFAULT, "loc_C8F"),
    )


    label("loc_C8C")

    OP_B4(0x0)
    Return()

    label("loc_C8F")

    EventBegin(0x0)
    OP_6D(-13760, 0, 18120, 0)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0x9, -11150, 0, 15510, 315)
    SetChrPos(0xA, -11000, 0, 17300, 0)
    SetChrPos(0xB, -12500, 0, 17280, 270)
    SetChrPos(0xC, -13000, 0, 16040, 225)
    SetChrChipByIndex(0x9, 13)
    SetChrChipByIndex(0xA, 13)
    SetChrChipByIndex(0xB, 13)
    SetChrChipByIndex(0xC, 13)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, -15250, 0, 17530, 90)
    SetChrPos(0x108, -15870, 0, 15890, 90)
    SetChrPos(0x102, -14310, 0, 16540, 90)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -12050, -600, 20370, 225)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#006F呵呵，一个不留。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F几下就打晕了，\x01",
            "真是没有挑战性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这里和王城里面一样，\x01",
            "也是个类似小酒吧的谈话室呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "留、留我一条小命……\x02",
    )

    CloseMessageWindow()

    def lambda_E5D():
        OP_6D(-12770, 0, 19310, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E5D)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)

    def lambda_E84():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E84)
    Sleep(200)

    def lambda_E97():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E97)
    Sleep(200)

    def lambda_EAA():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_EAA)
    WaitChrThread(0x101, 0x2)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_ECF():
        OP_8F(0xFE, 0xFFFFD0EE, 0x0, 0x4F92, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_ECF)

    def lambda_EEA():

        label("loc_EEA")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EEA")

    QueueWorkItem2(0x108, 1, lambda_EEA)

    def lambda_EFB():

        label("loc_EFB")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EFB")

    QueueWorkItem2(0x101, 1, lambda_EFB)

    def lambda_F0C():

        label("loc_F0C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_F0C")

    QueueWorkItem2(0x102, 1, lambda_F0C)
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "我、我、我\x01",
            "不是他们的同伙！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F我们知道了，\x01",
            "你是离宫的工作人员对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是接受女王陛下的委托\x01",
            "前来解救被囚禁的人质的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "真、真的吗？\x01",
            "真的是来救我们的吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，因此你可以放心了。\x02",
    )

    CloseMessageWindow()

    def lambda_1028():
        OP_6D(-15830, 0, 17600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1028)
    OP_8E(0x8, 0xFFFFCD7E, 0x0, 0x538E, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFC22A, 0x0, 0x51EA, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFC054, 0x0, 0x46BE, 0xBB8, 0x0)
    OP_44(0x101, 0x1)
    OP_8C(0x101, 270, 0)

    ChrTalk(
        0x8,
        "#5P哈……太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P我那个记者朋友抓了之后，\x01",
            "我以为我已经活不成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P他应该没事吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F记者朋友……\x02\x03",
            "#004F啊，奈尔的朋友难道就是你？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P啊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "众人告诉管家雷蒙德奈尔失踪事件的经过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#5P是啊，\x01",
            "那时联络奈尔的确实是我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P他想对保护在这里的公主\x01",
            "进行一次采访……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P看到他那么热心，我不忍心拒绝，\x01",
            "于是我就把他悄悄带了进来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F结果事情暴露而被捕了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P是啊，说来惭愧，\x01",
            "那时我还没有觉察到真相。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P只是听说公主被恐怖分子列为目标，\x01",
            "然后就被送到这里保护起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P没想到公主原来是被\x01",
            "情报部的那伙人给软禁了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P公主要来的事情让我们很高兴，\x01",
            "所以根本就没有注意到实情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P我真是个不称职的管家……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F算了算了，\x01",
            "不要灰心丧气嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F您知道那些人质被关在哪里吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P啊，他们集中在这个建筑最深处的\x01",
            "『纹章之间』里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P那房间是用来签署条约的，\x01",
            "是离宫里一个具有光辉历史的大厅。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_163D")

    ChrTalk(
        0x101,
        "#006F最深处的『纹章之间』吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F好，赶快去看看吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x4)
    Jump("loc_18E8")

    label("loc_163D")

    OP_A2(0x679)
    OP_28(0x4C, 0x1, 0x10)

    ChrTalk(
        0x101,
        (
            "#004F最深处的大厅……\x01",
            "不就是在刚才那边吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F啊，不过里面有一扇上了锁的门。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P是啊，\x01",
            "那里是被锁上了的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P开那扇门的钥匙\x01",
            "是由情报部的中队长保管的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P因为出现了恐怖分子，\x01",
            "中队长好像出动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F也就是说，\x01",
            "是到尤莉亚中尉他们埋伏的地方去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F嗯，这可就麻烦了，\x01",
            "没时间回去了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P等等……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P还有一把备用钥匙\x01",
            "是保管在某个地方的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P我想应该是\x01",
            "藏匿在展示室里面……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F展示室！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F立刻去调查。\x02",
    )

    CloseMessageWindow()

    label("loc_18E8")

    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, -11850, 0, 20220, 225)
    SetChrPos(0x101, -16149, 0, 17150, 180)
    SetChrPos(0x102, -16149, 0, 17150, 180)
    SetChrPos(0x108, -16149, 0, 17150, 180)
    OP_6D(-16149, 0, 17150, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_A2(0x656)
    EventEnd(0x0)
    Return()

    # Function_5_958 end

    def Function_6_1996(): pass

    label("Function_6_1996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AC4")
    EventBegin(0x0)
    OP_A2(0x657)
    OP_28(0x4C, 0x1, 0x20)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有个巨大的深红色花瓶。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们调查了一下，\x01",
            "看到在其底部粘有什么东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(400)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "备用钥匙\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x36F, 1)

    ChrTalk(
        0x101,
        "#006F啊，就是它！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这样就可以打开里面那扇门了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_1B19")

    label("loc_1AC4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有个巨大的深红色花瓶。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_1B19")

    Return()

    # Function_6_1996 end

    def Function_7_1B1A(): pass

    label("Function_7_1B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BA4")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "漂亮的器皿作为装饰。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们调查了一下，\x01",
            "没有找到什么特别的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1BEC")

    label("loc_1BA4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "漂亮的器皿作为装饰。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1BEC")

    TalkEnd(0xFF)
    Return()

    # Function_7_1B1A end

    def Function_8_1BF0(): pass

    label("Function_8_1BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C85")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "放置着东方风格的瓶子。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们调查了一下，\x01",
            "没有找到什么特别的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1CD8")

    label("loc_1C85")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "放置着东方风格的瓶子。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1CD8")

    TalkEnd(0xFF)
    Return()

    # Function_8_1BF0 end

    def Function_9_1CDC(): pass

    label("Function_9_1CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D72")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "放置着帝国风格的瓶子。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们调查了一下，\x01",
            "没有找到什么特别的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1DC6")

    label("loc_1D72")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "放置着帝国风格的瓶子。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1DC6")

    TalkEnd(0xFF)
    Return()

    # Function_9_1CDC end

    def Function_10_1DCA(): pass

    label("Function_10_1DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E6B")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "美术目录并排着。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们调查了一下，\x01",
            "没有找到什么特别的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1EC8")

    label("loc_1E6B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "美术目录并排着。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1EC8")

    TalkEnd(0xFF)
    Return()

    # Function_10_1DCA end

    def Function_11_1ECC(): pass

    label("Function_11_1ECC")

    SetMapFlags(0x2000000)
    EventBegin(0x0)
    OP_6D(17870, 0, -11650, 0)
    OP_67(0, 4740, -10000, 0)
    OP_6B(3019, 0)
    OP_6C(315000, 0)
    OP_6E(261, 0)
    SetChrPos(0xE, 11330, 0, -10500, 135)
    SetChrPos(0x12, 12980, 0, -9840, 225)
    SetChrPos(0x11, 12980, 0, -9840, 270)
    SetChrPos(0x10, 12140, 0, -12950, 0)
    SetChrPos(0xF, 10420, 0, -12050, 90)
    SetChrPos(0x108, 11130, 0, -13550, 0)
    SetChrPos(0x101, 13440, 0, -12780, 315)
    SetChrPos(0x102, 14010, 0, -11910, 315)
    TurnDirection(0xE, 0x11, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x108, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 14)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x12, 0x80)
    OP_6D(11600, 0, -10880, 3000)

    ChrTalk(
        0x11,
        (
            "#175F我真的……\x01",
            "感到非常抱歉。\x02\x03",
            "由于不成器的我，\x01",
            "而让大家受了这么多苦……\x02\x03",
            "如果不能救出大家，办事不周的我\x01",
            "必定用自己双手将身体撕裂来以谢此罪……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "科洛蒂娅公主",
        (
            "#401F我不允许你这样说。\x02\x03",
            "能够这样和大家再次相会，\x01",
            "我已经觉得非常心满意足了。\x02\x03",
            "你们能够来救我……\x01",
            "我感激都还来不及呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#171F殿下……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12, 400)

    ChrTalk(
        0x101,
        (
            "#506F哎……不好意思，\x01",
            "在你们感动的时候打断一下……\x02\x03",
            "#505F为什么基库也在这里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#310F啾？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(
        0x11,
        (
            "#170F呵呵，基库在作为殿下的护卫的同时，\x01",
            "也是亲卫队的传令员哦。\x01",
            "　\x02\x03",
            "你们忘了在旅馆收到的那封信吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……是那天晚上！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F果然是这样。\x02\x03",
            "这么说来，让尤莉亚中尉\x01",
            "得知女王陛下委托的也是它了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#176F嗯，没错。\x01",
            "是女王陛下直接通过基库告知我的。\x02\x03",
            "#175F不过殿下所在的这个大房间\x01",
            "没有基库可以进入的窗户。\x02\x03",
            "不能及时取得联系真让我很担心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F真是的……\x01",
            "我完全没有想到呢。\x02\x03",
            "#509F喂，基库。\x01",
            "悄悄的把信放下后就离开了，\x01",
            "是不是有些不太礼貌呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#310F啾～……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    NpcTalk(
        0xE,
        "科洛蒂娅公主",
        (
            "#408F嘻嘻……\x01",
            "它说『对不起』呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F哎呀，没关系的啦。\x02\x03",
            "#006F对了，\x01",
            "那些特务兵已经全部解决了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_255F():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_255F)

    ChrTalk(
        0x11,
        (
            "#178F在离宫这里值勤的特务部队\x01",
            "基本上都被我们控制了。\x02\x03",
            "但是在格兰赛尔城内\x01",
            "应该还有相当一部分的残党。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#026F各地的王国军，\x01",
            "至今还处于情报部的掌控之下。\x02\x03",
            "#022F最糟糕的是，他们很有可能会\x01",
            "以镇压叛军的名义对这里展开进攻。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        (
            "#580F啊……\x01",
            "我还没有想到这一点。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x102,
        (
            "#012F是呀……\x02\x03",
            "我想，至少也要让科洛丝\x01",
            "先去安全的地方躲避一下吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "科洛蒂娅公主",
        "#404F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#030F如果可以的话，\x01",
            "去寻求帝国或共和国大使馆的保护如何？\x02\x03",
            "#035F在大使馆里有治外法权保护……\x01",
            "我想敌人是不会随便轻举妄动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F可以用刚才作战所缴获的\x01",
            "特务飞艇作为逃跑的工具。\x02\x03",
            "虽然不能从根本上解决问题，\x01",
            "但可以拖延一些时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#176F说的是啊……\x01",
            "也只有选择逃亡了……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "科洛蒂娅公主",
        (
            "#406F…………………………\x02\x03",
            "#402F大家……听我说。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x108, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2A5B():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A5B)

    def lambda_2A69():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A69)

    def lambda_2A77():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2A77)

    def lambda_2A85():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2A85)

    def lambda_2A93():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2A93)

    def lambda_2AA1():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2AA1)

    NpcTalk(
        0xE,
        "科洛蒂娅公主",
        (
            "#402F在这种状况下，\x01",
            "我可以通过你们向游击士协会委托任务吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F人质营救任务已经完成了，\x01",
            "所以应该可以接受其他的委托。\x02\x03",
            "当然，要视委托的内容而定。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "科洛蒂娅公主",
        (
            "#406F如果可以……\x01",
            "请接受我无理的请求。\x02\x03",
            "#403F可以帮助我解放王城并救出陛下吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#173F殿、殿下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F对啊……还有女王陛下呢。\x02\x03",
            "我们一定要把她也救出来啊！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F说实话，\x01",
            "我就知道有可能会变成这样。\x02\x03",
            "#072F不过，公主殿下……\x01",
            "这个委托相当棘手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#025F是啊……\x02\x03",
            "以我们现在的战斗力，就算全员齐聚，\x01",
            "也不可能从正面攻入王城的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F如果利用那艘特务飞艇的话，\x01",
            "也不是没有可能……\x02\x03",
            "然而……\x01",
            "充足的准备是行动的必要条件。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "科洛蒂娅公主",
        (
            "#406F……这些我已经考虑过了。\x02\x03",
            "#402F各位，你们看这个可以吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "科洛蒂娅公主取出了一幅古老的地图。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x357, 1)
    OP_AD(0x40026, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        "#004F这张是……哪里的地图？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("科洛蒂娅公主")

    AnonymousTalk(
        (
            "#402F这张古地图是记载着王都地下水路\x01",
            "内部结构的古代文献。\x02\x03",
            "这上面标记有通往王城地下的隐藏水路。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(0, 0, -1)
    OP_AE(0x1F4)
    OP_20(0x5DC)
    OP_21()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4260   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1ECC end

    def Function_12_3057(): pass

    label("Function_12_3057")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『先王的御座』\x01",
            "　先王埃德佳Ⅲ世\x01",
            "　下榻艾尔贝离宫时\x01",
            "　爱用的椅子。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_3057 end

    SaveToFile()

Try(main)
