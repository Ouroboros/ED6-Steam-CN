from ED6ScenarioHelper import *

def main():
    CreateScenaFile(
        FileName            = 'C0302   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0302.x',
        MapIndex            = 19,
        MapDefaultBGM       = "ed60021",
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
        '乔丝特',                               # 9
        '雷古',                                 # 10
        '蒂诺',                                 # 11
        '莱尔',                                 # 12
        '吉尔',                                 # 13
        '空贼艇',                               # 14
        '空贼艇（影）',                         # 15
        '目标用摄像机',                         # 16
    )

    DeclEntryPoint(
        Unknown_00              = 35000,
        Unknown_04              = 0,
        Unknown_08              = 16000,
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
        Unknown_3A              = 19,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00310 ._CH',             # 00
        'ED6_DT07/CH00311 ._CH',             # 01
        'ED6_DT07/CH00314 ._CH',             # 02
        'ED6_DT07/CH00360 ._CH',             # 03
        'ED6_DT07/CH00361 ._CH',             # 04
        'ED6_DT07/CH00364 ._CH',             # 05
        'ED6_DT07/CH00100 ._CH',             # 06
        'ED6_DT07/CH00101 ._CH',             # 07
        'ED6_DT07/CH00110 ._CH',             # 08
        'ED6_DT07/CH00111 ._CH',             # 09
        'ED6_DT07/CH00120 ._CH',             # 0A
        'ED6_DT07/CH00121 ._CH',             # 0B
        'ED6_DT07/CH00122 ._CH',             # 0C
        'ED6_DT07/CH02130 ._CH',             # 0D
        'ED6_DT07/CH02330 ._CH',             # 0E
        'ED6_DT07/CH02120 ._CH',             # 0F
        'ED6_DT07/CH01380 ._CH',             # 10
        'ED6_DT09/CH10010 ._CH',             # 11
        'ED6_DT09/CH10011 ._CH',             # 12
        'ED6_DT09/CH10280 ._CH',             # 13
        'ED6_DT09/CH10281 ._CH',             # 14
        'ED6_DT09/CH10230 ._CH',             # 15
        'ED6_DT09/CH10231 ._CH',             # 16
        'ED6_DT09/CH10240 ._CH',             # 17
        'ED6_DT09/CH10241 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH00310P._CP',             # 00
        'ED6_DT07/CH00311P._CP',             # 01
        'ED6_DT07/CH00314P._CP',             # 02
        'ED6_DT07/CH00360P._CP',             # 03
        'ED6_DT07/CH00361P._CP',             # 04
        'ED6_DT07/CH00364P._CP',             # 05
        'ED6_DT07/CH00100P._CP',             # 06
        'ED6_DT07/CH00101P._CP',             # 07
        'ED6_DT07/CH00110P._CP',             # 08
        'ED6_DT07/CH00111P._CP',             # 09
        'ED6_DT07/CH00120P._CP',             # 0A
        'ED6_DT07/CH00121P._CP',             # 0B
        'ED6_DT07/CH00122P._CP',             # 0C
        'ED6_DT07/CH02130P._CP',             # 0D
        'ED6_DT07/CH02330P._CP',             # 0E
        'ED6_DT07/CH02120P._CP',             # 0F
        'ED6_DT07/CH01380P._CP',             # 10
        'ED6_DT09/CH10010P._CP',             # 11
        'ED6_DT09/CH10011P._CP',             # 12
        'ED6_DT09/CH10280P._CP',             # 13
        'ED6_DT09/CH10281P._CP',             # 14
        'ED6_DT09/CH10230P._CP',             # 15
        'ED6_DT09/CH10231P._CP',             # 16
        'ED6_DT09/CH10240P._CP',             # 17
        'ED6_DT09/CH10241P._CP',             # 18
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 52120,
        Z                   = 240,
        Y                   = -16250,
        Unknown_0C          = 93,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x4D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 61090,
        Z                   = -350,
        Y                   = 5020,
        Unknown_0C          = 237,
        Unknown_0E          = 23,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x47,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 73730,
        Z                   = -80,
        Y                   = -3560,
        Unknown_0C          = 208,
        Unknown_0E          = 23,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x47,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 53060,
        Z                   = -210,
        Y                   = 8160,
        Unknown_0C          = 61,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -74120,
        Y                   = -1000,
        Z                   = -14700,
        Range               = -71420,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFA92A,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    DeclActor(
        TriggerX            = 72710,
        TriggerZ            = 0,
        TriggerY            = 10290,
        TriggerRange        = 1500,
        ActorX              = 72710,
        ActorZ              = 1500,
        ActorY              = 10290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45900,
        TriggerZ            = -60,
        TriggerY            = 4140,
        TriggerRange        = 1000,
        ActorX              = 45300,
        ActorZ              = 1440,
        ActorY              = 3640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_34A",          # 00, 0
        "Function_1_360",          # 01, 1
        "Function_2_3B0",          # 02, 2
        "Function_3_26C3",         # 03, 3
        "Function_4_26E3",         # 04, 4
        "Function_5_2749",         # 05, 5
        "Function_6_2A84",         # 06, 6
        "Function_7_2D4E",         # 07, 7
        "Function_8_2D75",         # 08, 8
        "Function_9_2F76",         # 09, 9
        "Function_10_3116",        # 0A, 10
        "Function_11_31E0",        # 0B, 11
    )


    def Function_0_34A(): pass

    label("Function_0_34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_END)), "loc_35F")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_64(0x0, 0x1)

    label("loc_35F")

    Return()

    # Function_0_34A end

    def Function_1_360(): pass

    label("Function_1_360")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x385), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SoundLoad(119)
    SoundLoad(121)
    SoundLoad(502)

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_390")
    OP_6F(0x4, 0)
    Jump("loc_397")

    label("loc_390")

    OP_6F(0x4, 60)

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_END)), "loc_3AC")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_64(0x0, 0x1)

    label("loc_3AC")

    OP_10(0x1, 0x1)
    Return()

    # Function_1_360 end

    def Function_2_3B0(): pass

    label("Function_2_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26C2")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x103, 0x8, 0)
    SetChrPos(0x8, -60860, -320, 5360, 135)
    SetChrPos(0x9, -60550, -150, 2920, 341)
    SetChrPos(0xA, -59230, -300, 3520, 317)
    SetChrPos(0xB, -58760, -350, 5070, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8)
    OP_20(0xFA0)

    def lambda_499():
        OP_67(0, 6280, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_499)

    def lambda_4B1():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B1)
    OP_6D(-59790, -340, 4800, 4000)
    SetChrPos(0x101, -57980, 130, -9190, 356)
    SetChrPos(0x102, -56650, 110, -9280, 356)
    SetChrPos(0x103, -57400, -130, -10020, 356)
    OP_22(0x80, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0x8, 0, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_1D(0x57)

    ChrTalk(
        0x8,
        (
            "#219F哼哼哼……\x01",
            "真是简单透顶了。\x02\x03",
            "#219F本小姐只不过略施小计，\x01",
            "就能拿到这么棒的东西。\x02\x03",
            "#219F这下可以向大哥他们炫耀一下啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#6P是啊是啊，大小姐真是厉害呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P普通人就算穿上校服，\x01",
            "也不见得有那么一流的演技啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "真不愧是原贵族大小姐。\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#219F哼……\x01",
            "过去的事就别提了。\x02\x03",
            "#219F不过，这种装扮也能被骗倒，\x01",
            "那些家伙还真是有眼光啊。\x02\x03",
            "#219F不管是那个喜欢做老好人的市长，\x01",
            "还是那个没大脑的女游击士……\x02\x03",
            "#410F啊哈哈，他们真是太好骗了！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    def lambda_795():
        OP_6D(-58480, 30, -5380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_795)

    def lambda_7AD():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7AD)
    Sleep(1500)
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F（说、说什么～！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（冷静点……\x01",
            " 再听听他们还会说些什么。）\x02",
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
            "（这叫我怎么冷～静！）\x01",      # 0
            "（唔……只好忍一下。）\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0C")
    SetChrChipByIndex(0x101, 6)

    ChrTalk(
        0x101,
        "#005F（这叫我怎么冷～静！）\x02",
    )

    CloseMessageWindow()

    def lambda_8D1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D1)

    def lambda_8DF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8DF)
    OP_8E(0x101, 0xFFFF1974, 0x14, 0xFFFFDBF2, 0x1770, 0x0)

    def lambda_901():

        label("loc_901")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_901")

    QueueWorkItem2(0x102, 1, lambda_901)

    def lambda_912():

        label("loc_912")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_912")

    QueueWorkItem2(0x103, 1, lambda_912)
    OP_8E(0x101, 0xFFFF1406, 0x0, 0xFFFFE034, 0x1770, 0x0)

    def lambda_937():
        OP_8E(0xFE, 0xFFFF1334, 0x1E, 0xFFFFF646, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_937)

    ChrTalk(
        0x102,
        "#014F（啊啊！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#025F（又冲动了啊……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#6P哼～！\x01",
            "你们这些坏蛋，一个都别想逃！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 8)
    SetChrChipByIndex(0x103, 10)

    def lambda_9BF():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9BF)

    def lambda_9CF():
        OP_6D(-60120, -80, 1150, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9CF)

    def lambda_9E7():
        OP_8E(0xFE, 0xFFFF1302, 0x14, 0xFFFFDD64, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E7)
    Sleep(600)

    def lambda_A07():
        OP_8E(0xFE, 0xFFFF1302, 0x14, 0xFFFFDD64, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A07)
    WaitChrThread(0x102, 0x1)

    def lambda_A27():
        OP_8E(0xFE, 0xFFFF0FB0, 0xFFFFFF74, 0xFFFFF114, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A27)
    WaitChrThread(0x103, 0x1)

    def lambda_A47():
        OP_8E(0xFE, 0xFFFF16CC, 0xA, 0xFFFFF114, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A47)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_ACD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ACD)

    def lambda_ADB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_ADB)

    def lambda_AE9():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_AE9)

    def lambda_AF7():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AF7)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Jump("loc_ED7")

    label("loc_B0C")

    OP_2B(0x1A, 0x1)

    ChrTalk(
        0x101,
        "#509F（唔……只好忍一下。）\x02",
    )

    CloseMessageWindow()
    OP_6D(-59850, -340, 4500, 1500)

    ChrTalk(
        0xB,
        (
            "可是我听说，\x01",
            "那些小鬼好像还蛮强的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "矿山里出现的魔兽\x01",
            "一下子就被他们收拾掉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#219F矿山？\x01",
            "啊啊，是说你行动失败的那件事吧。\x02\x03",
            "#219F要是成功了，\x01",
            "我就不必特意去演那出猴戏啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "对、对不起，大小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#219F结局好就万事ＯＫ啦。\x01",
            "话说回来……\x02\x03",
            "#219F那个……\x01",
            "那种水平也能当上游击士，\x01",
            "真是笑死本小姐了。\x02\x03",
            "#219F特别是那个没大脑的笨女人！\x01",
            "对本小姐毫无戒心，\x01",
            "还说什么『好不容易认识到一个朋友』！\x02\x03",
            "#410F啊哈哈哈哈！\x01",
            "我都忍不住要笑死了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3P#1K哇哈哈哈哈！\x02",
    )


    ChrTalk(
        0xB,
        "#2P#1K嘎哈哈哈哈！\x02",
    )


    ChrTalk(
        0xA,
        "#4P#1K呀哈哈哈哈！\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()
    SetChrChipByIndex(0x101, 6)
    SetChrChipByIndex(0x102, 8)
    SetChrChipByIndex(0x103, 10)
    SetChrPos(0x101, -60670, 20, -8860, 270)
    SetChrPos(0x102, -60670, 20, -8860, 270)
    SetChrPos(0x103, -60670, 20, -8860, 270)

    ChrTalk(
        0x101,
        "#5P……真的那么好笑吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_E29():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E29)

    def lambda_E37():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E37)

    def lambda_E45():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E45)

    def lambda_E53():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E53)

    def lambda_E61():
        OP_8E(0xFE, 0xFFFF133E, 0x1E, 0xFFFFF650, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E61)
    Sleep(300)

    def lambda_E81():
        OP_8E(0xFE, 0xFFFF0FB0, 0xFFFFFF74, 0xFFFFF114, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E81)
    Sleep(300)

    def lambda_EA1():
        OP_8E(0xFE, 0xFFFF16CC, 0xA, 0xFFFFF114, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EA1)

    def lambda_EBC():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_EBC)
    OP_6D(-60120, -80, 1150, 1500)

    label("loc_ED7")

    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        "#411F你、你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#582F一直忍着不出声，\x01",
            "结果就没大脑啦笨女人啦之类的，\x01",
            "越说越来劲、越说越放肆……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x101,
        "#005F#3S准备好受死了吧！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x9, 3)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0xA, 3)

    ChrTalk(
        0xB,
        "是游击士！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "为什么会发现这儿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F从市长家偷走七耀石的手段\x01",
            "的确相当高明……\x02\x03",
            "#027F呵呵，不过最后还是被我们逮个正着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F现根据游击士协会的规定，\x01",
            "你们涉嫌私闯民宅，破坏财物和盗窃，\x01",
            "我们要代表游击士协会将你们逮捕。\x02\x03",
            "请你们马上放下武器，不要做多余的抵抗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "哇哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "大、大小姐，该怎么办！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#412F有什么好怕的！\x02\x03",
            "就算是游击士，也只不过是\x01",
            "女人和小孩罢了！\x02\x03",
            "要让他们尝尝我们『卡普亚\x01",
            "一家』的厉害！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F什么女人和小孩啊！\x01",
            "不要说得自己有多伟大！\x02\x03",
            "#005F啊～真是快要气炸啦！\x01",
            "我一定要让你们输得心服口服！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#219F那正是我要说的！\x02",
    )

    CloseMessageWindow()

    def lambda_1205():
        OP_6B(3000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1205)

    def lambda_1215():
        OP_6D(-60120, -80, 3200, 1000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1215)
    Sleep(500)
    OP_82(0x0, 0x0)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0x8, 32, 800)
    SetChrChipByIndex(0x8, 0)
    OP_8C(0x8, 330, 800)
    OP_8C(0x8, 180, 800)
    Sleep(500)
    WaitChrThread(0x8, 0x2)

    ChrTalk(
        0x8,
        "#210F你们，给我上！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1P#1K收到！\x02",
    )


    ChrTalk(
        0xA,
        "#2P#1K收到！\x02",
    )


    ChrTalk(
        0x9,
        "#4P#1K收到！\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    def lambda_12B2():
        OP_6D(-60120, -80, 1150, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_12B2)
    SetChrChipByIndex(0xA, 4)

    def lambda_12CF():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12CF)
    SetChrChipByIndex(0x9, 4)

    def lambda_12E9():
        OP_92(0xFE, 0x102, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12E9)
    SetChrChipByIndex(0xB, 4)

    def lambda_1303():
        OP_92(0xFE, 0x103, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1303)
    SetChrChipByIndex(0x8, 1)

    def lambda_131D():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_131D)
    Sleep(400)
    Battle(0x385, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_134A"),
        (SWITCH_DEFAULT, "loc_134F"),
    )


    label("loc_134A")

    OP_B4(0x0)
    Jump("loc_134F")

    label("loc_134F")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    OP_6D(-56340, -330, 2350, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(68000, 0)
    OP_6E(291, 0)
    SetChrPos(0x103, -59720, -110, 320, 26)
    SetChrPos(0x102, -57190, -230, -570, 20)
    SetChrPos(0x101, -57720, -260, 480, 4)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 2)
    SetChrChipByIndex(0x9, 5)
    SetChrChipByIndex(0xB, 5)
    SetChrChipByIndex(0xA, 5)
    SetChrPos(0x8, -55850, -280, 3840, 206)
    SetChrPos(0x9, -56410, -160, 5250, 213)
    SetChrPos(0xA, -54320, -160, 4210, 216)
    SetChrPos(0xB, -54160, -50, 5560, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#216F怎、怎么可能……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿，小菜一碟⊙\x01",
            "这就是小看游击士的后果哦。\x02\x03",
            "#507F我说你，快点把那东西还给我们！\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x8, 0x320, 0xBB8, 0x0)
    Sleep(300)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0x101, 0, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x80, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取回了\x07\x02",
            "七耀石的结晶\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        "#216F啊啊……本小姐的七耀石……\x02",
    )

    CloseMessageWindow()
    OP_8F(0x101, 0xFFFF2248, 0xFFFFFEC0, 0x848, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        (
            "#582F不是你的，\x01",
            "是洛连特全体市民的！\x02\x03",
            "#009F真是的，脸皮这么厚……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x0)

    def lambda_1644():
        OP_8F(0xFE, 0xFFFF20C2, 0xFFFFFEE8, 0x2DA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1644)
    OP_8E(0x103, 0xFFFF1AC8, 0xFFFFFF06, 0x44C, 0xBB8, 0x0)
    OP_8E(0x103, 0xFFFF1F0A, 0xFFFFFED4, 0x6A4, 0xBB8, 0x0)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(
        0x103,
        (
            "#021F是啊，既然结晶已经取回来了，\x01",
            "是不是到了该坦白交待的时间了？\x02\x03",
            "#020F之前你说了很有趣的名字呢。\x01",
            "好像是『卡普亚一家』什么的……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#216F唔……\x02\x03",
            "#211F不、不知道啊，你在说什么呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x103, 10)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x103,
        (
            "#027F呵呵，真是嘴硬啊。\x01",
            "不过我就是喜欢这样的孩子呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x103, 12)
    OP_22(0x1F6, 0x0, 0x64)
    OP_99(0x103, 0x0, 0x4, 0x7D0)

    def lambda_17C1():
        OP_99(0x103, 0x7, 0x9, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_17C1)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_96(0x8, 0xFFFF268A, 0xFFFFFF24, 0x109A, 0x1F4, 0x1388)
    SetChrChipByIndex(0x8, 13)

    ChrTalk(
        0x8,
        (
            "#213F呀！\x02\x03",
            "#214F这、这样多危险啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F如果你不肯开口，\x01",
            "就只好问问你的身体了，不是吗？\x02\x03",
            "#021F没关系的，姐姐我会很温柔的哦㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 65535)
    OP_8E(0x103, 0xFFFF2248, 0xFFFFFEC0, 0x848, 0x7D0, 0x0)
    TurnDirection(0x103, 0x8, 400)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 10)

    def lambda_18C1():

        label("loc_18C1")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_18C1")

    QueueWorkItem2(0x103, 1, lambda_18C1)
    OP_62(0x8, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        (
            "#216F唔……\x02\x03",
            "#216F不、不要过来，离远点！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x102)

    ChrTalk(
        0x101,
        "#509F（雪拉姐绝对是在享受呢。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F（不招惹瘟神也就不会有报应了吧……）\x02",
    )

    CloseMessageWindow()
    OP_22(0x79, 0x1, 0x5A)
    Sleep(200)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x103, 0)
    SetChrPos(0xD, -37060, 300, -13200, 291)
    TurnDirection(0x102, 0xD, 800)
    SetChrChipByIndex(0x102, 8)

    def lambda_1A10():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A10)

    ChrTalk(
        0x102,
        "#016F雪拉姐姐，危险！\x02",
    )

    CloseMessageWindow()

    def lambda_1A39():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A39)
    OP_44(0x103, 0xFF)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x103, 0xD, 800)
    OP_96(0x103, 0xFFFF1A0A, 0xFFFFFF38, 0x104, 0x3E8, 0x1770)
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -53890, -320, 1090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -54980, -320, 1650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -56310, -330, 2190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -57630, -300, 2760, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -58980, -300, 3360, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)

    ChrTalk(
        0x103,
        "#023F导力炮！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#004F雪拉姐，没事吧！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#024F没事！\x01",
            "注意头顶！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 6)

    def lambda_1C7E():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C7E)

    def lambda_1C8C():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C8C)

    def lambda_1C9A():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C9A)

    def lambda_1CA8():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CA8)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x40)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x3)
    OP_43(0xD, 0x1, 0x0, 0x5)
    OP_43(0xE, 0x1, 0x0, 0x6)
    OP_B0(0x2, 0x1E)

    def lambda_1CF0():
        OP_6E(511, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1CF0)
    OP_24(0x79, 0x5A)
    Sleep(500)
    OP_24(0x79, 0x64)
    Sleep(2500)

    def lambda_1D12():

        label("loc_1D12")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_1D12")

    QueueWorkItem2(0x8, 1, lambda_1D12)

    def lambda_1D23():

        label("loc_1D23")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_1D23")

    QueueWorkItem2(0x101, 1, lambda_1D23)

    def lambda_1D34():

        label("loc_1D34")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_1D34")

    QueueWorkItem2(0x103, 1, lambda_1D34)

    def lambda_1D45():

        label("loc_1D45")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_1D45")

    QueueWorkItem2(0x102, 1, lambda_1D45)

    def lambda_1D56():
        OP_6D(-61600, 3050, 5140, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D56)

    def lambda_1D6E():
        OP_6C(33000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1D6E)
    Sleep(5000)
    OP_43(0x9, 0x1, 0x0, 0x7)
    OP_43(0xB, 0x1, 0x0, 0x7)
    OP_43(0xA, 0x1, 0x0, 0x7)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580F飞、飞艇？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#211F啊哈哈，形势逆转了！\x02",
    )

    CloseMessageWindow()

    def lambda_1DD1():
        OP_8E(0xFE, 0xFFFF121C, 0xFFFFFEC0, 0x11D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1DD1)
    Sleep(200)
    SetChrChipByIndex(0x9, 4)

    def lambda_1DF6():
        OP_8E(0xFE, 0xFFFF17B2, 0xFFFFFE8E, 0x159A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1DF6)
    Sleep(200)
    SetChrChipByIndex(0xB, 4)

    def lambda_1E1B():
        OP_8E(0xFE, 0xFFFF1668, 0xFFFFFEC0, 0x1040, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E1B)
    Sleep(100)
    SetChrChipByIndex(0xA, 4)

    def lambda_1E40():
        OP_8E(0xFE, 0xFFFF11A4, 0xFFFFFF4C, 0xC3A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1E40)
    WaitChrThread(0x8, 0x1)
    SetChrPos(0xC, -67370, 8500, 6060, 123)
    TurnDirection(0x8, 0xC, 0)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 3)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 3)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 3)
    WaitChrThread(0x101, 0x2)

    def lambda_1E9B():
        OP_6D(-62640, 4570, 5610, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E9B)

    def lambda_1EB3():
        OP_6E(363, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EB3)

    def lambda_1EC3():
        OP_67(0, 10510, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1EC3)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x5F)
    OP_73(0x2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x4)
    OP_8F(0xC, 0xFFFEF8D6, 0x24B8, 0x17AC, 0xBB8, 0x0)
    Sleep(500)

    ChrTalk(
        0xC,
        "#201F乔丝特，没事吧！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#214F吉尔哥！\x01",
            "你来得太慢啦！\x02\x03",
            "#210F算了，赶快来帮我教训他们吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#201F不，我们要马上离开洛连特。\x02\x03",
            "你不在的时候，\x01",
            "柏斯发生了点麻烦事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#213F麻、麻烦事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#201F好了，赶快上来！\x01",
            "再磨蹭的话就不管你了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0xC, 0xFFFEF8D6, 0x1F40, 0x17AC, 0xBB8, 0x0)
    SetChrFlags(0xC, 0x80)
    OP_22(0xCE, 0x0, 0x64)
    OP_6F(0x2, 95)
    OP_70(0x2, 0xA0)

    ChrTalk(
        0x8,
        "#215F唔……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xA, 0x4)

    def lambda_205F():
        OP_8E(0xFE, 0xFFFF010B, 0xFFFFFF38, 0x13BA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_205F)
    Sleep(200)

    def lambda_207F():
        OP_6D(-61640, -300, 5890, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_207F)

    def lambda_2097():
        OP_67(0, 9430, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2097)

    def lambda_20AF():
        OP_6C(9000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20AF)
    SetChrChipByIndex(0x9, 4)

    def lambda_20C4():
        OP_8E(0xFE, 0xFFFEBBB4, 0xFFFFFEB6, 0x6810, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20C4)
    Sleep(200)
    SetChrChipByIndex(0xB, 4)

    def lambda_20E9():
        OP_8E(0xFE, 0xFFFEBBB4, 0xFFFFFEB6, 0x6810, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_20E9)
    Sleep(100)
    SetChrChipByIndex(0xA, 4)

    def lambda_210E():
        OP_8E(0xFE, 0xFFFEBBB4, 0xFFFFFEB6, 0x6810, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_210E)

    def lambda_2129():
        OP_8E(0xFE, 0xFFFF19F6, 0xFFFFFEE8, 0x7D9, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2129)

    def lambda_2144():
        OP_8E(0xFE, 0xFFFF1410, 0x14, 0xFFFFFB46, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2144)
    WaitChrThread(0x8, 0x1)
    ClearChrFlags(0x8, 0x4)
    SetChrBattleFlags(0x8, 0x20)
    OP_96(0x8, 0xFFFEFDB8, 0x226, 0x125C, 0x3E8, 0x1F40)
    OP_8C(0x8, 160, 400)
    Sleep(500)

    ChrTalk(
        0x101,
        "#005F给、给我慢着！喂！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#214F#5P你们给我记住！\x01",
            "别以为这样就算赢了！\x02\x03",
            "#214F总有一天要一决胜负！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21FA():

        label("loc_21FA")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_21FA")

    QueueWorkItem2(0x101, 0, lambda_21FA)

    def lambda_220B():

        label("loc_220B")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_220B")

    QueueWorkItem2(0x103, 0, lambda_220B)

    def lambda_221C():

        label("loc_221C")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_221C")

    QueueWorkItem2(0x102, 0, lambda_221C)
    OP_22(0xCD, 0x0, 0x64)
    OP_43(0xD, 0x1, 0x0, 0x8)
    OP_43(0xE, 0x1, 0x0, 0x9)
    OP_43(0x8, 0x3, 0x0, 0x4)

    def lambda_2247():
        OP_6D(-68070, 1230, 7050, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2247)

    def lambda_225F():
        OP_6C(69000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_225F)

    def lambda_226F():
        OP_6B(4000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_226F)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    Sleep(3000)

    def lambda_2293():
        OP_6D(-60410, -60, 750, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2293)

    def lambda_22AB():
        OP_67(0, 9000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_22AB)
    Sleep(3000)
    OP_82(0x2, 0x0)
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_6D(-60200, -110, 1680, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(2009, 0)
    OP_6C(90000, 0)
    OP_6E(363, 0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x101, -60700, -40, 950, 225)
    SetChrPos(0x102, -60790, -80, 2280, 225)
    SetChrPos(0x103, -59390, -210, 1740, 225)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_24(0x79, 0x5F)
    OP_24(0xCD, 0x5F)
    Sleep(100)
    OP_24(0x79, 0x5A)
    OP_24(0xCD, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x55)
    OP_24(0xCD, 0x55)
    Sleep(100)
    OP_24(0x79, 0x50)
    OP_24(0xCD, 0x50)
    Sleep(50)
    OP_24(0x79, 0x46)
    OP_24(0xCD, 0x46)
    Sleep(50)
    OP_24(0x79, 0x3C)
    OP_24(0xCD, 0x3C)
    Sleep(50)
    OP_24(0x79, 0x32)
    OP_24(0xCD, 0x32)
    Sleep(50)
    OP_23(0x79)
    OP_23(0xCD)
    Sleep(500)
    OP_1D(0x15)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#002F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#522F伤脑筋了。\x01",
            "没想到连那种东西都出来了。\x02\x03",
            "#021F啊哈哈，被她略占上风了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#007F现在不是笑的时候吧……\x02\x03",
            "#003F唔～真不甘心啊～！！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 135, 400)

    ChrTalk(
        0x102,
        (
            "#019F算了吧。\x01",
            "反正七耀石也已经取回来了。\x02\x03",
            "#012F那个……\x01",
            "那些人应该就是空贼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)

    ChrTalk(
        0x103,
        (
            "#026F嗯，应该没错。\x02\x03",
            "看起来，他们就是那群\x01",
            "盘踞在柏斯地区的犯罪团伙……\x02\x03",
            "#022F没想到会到洛连特\x01",
            "这种乡下地方来作案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F管他是空贼还是山贼，\x01",
            "反正通通都不是好家伙啦！\x02\x03",
            "下次再让我遇到那个嚣张的男人婆，\x01",
            "一定要打她个稀里哗啦噼里啪啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F稀里哗啦噼里啪啦……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "经过众人的调查和森林一战后，\x01",
            "市长家被抢走的七耀石结晶终于顺利地取回来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把七耀石还给市长之后，\x01",
            "艾丝蒂尔等人为了报告事情的经过而回到协会。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x266)
    OP_28(0x1B, 0x1, 0x80)
    OP_28(0x1B, 0x1, 0x100)
    Sleep(1000)
    NewScene("ED6_DT01/T0121   ._SN", 103, 0, 0)
    IdleLoop()

    label("loc_26C2")

    Return()

    # Function_2_3B0 end

    def Function_3_26C3(): pass

    label("Function_3_26C3")

    OP_24(0x79, 0x46)
    Sleep(500)
    OP_24(0x79, 0x50)
    Sleep(500)
    OP_24(0x79, 0x5A)
    Sleep(500)
    OP_24(0x79, 0x64)
    Return()

    # Function_3_26C3 end

    def Function_4_26E3(): pass

    label("Function_4_26E3")

    Sleep(6000)
    OP_24(0x79, 0x64)
    Sleep(200)
    OP_24(0x79, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    Sleep(200)
    OP_24(0x79, 0x28)
    Sleep(200)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_24(0x79, 0x14)
    Sleep(200)
    OP_24(0x79, 0xA)
    Sleep(200)
    OP_23(0x77)
    OP_23(0x79)
    Return()

    # Function_4_26E3 end

    def Function_5_2749(): pass

    label("Function_5_2749")

    SetChrPos(0xFE, -37060, 17100, -13200, 291)
    LoadEffect(0x1, "map\\\\mp021_00.eff")

    def lambda_2774():
        OP_8E(0xFE, 0xFFFEF318, 0x283C, 0x24B8, 0x1838, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2774)
    Sleep(3000)

    def lambda_2794():
        OP_8F(0xFE, 0xFFFEF318, 0x2454, 0x24B8, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2794)
    Sleep(500)

    def lambda_27B4():
        OP_8F(0xFE, 0xFFFEF318, 0x2454, 0x24B8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27B4)

    def lambda_27CF():
        OP_8C(0xFE, 155, 6)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_27CF)
    Sleep(100)

    def lambda_27E2():
        OP_8C(0xFE, 155, 8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_27E2)
    Sleep(100)

    def lambda_27F5():
        OP_8C(0xFE, 155, 10)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_27F5)
    Sleep(100)

    def lambda_2808():
        OP_8C(0xFE, 155, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2808)
    Sleep(100)

    def lambda_281B():
        OP_8C(0xFE, 155, 14)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_281B)
    Sleep(100)

    def lambda_282E():
        OP_8C(0xFE, 155, 16)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_282E)
    Sleep(100)

    def lambda_2841():
        OP_8C(0xFE, 155, 18)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2841)
    Sleep(100)

    def lambda_2854():
        OP_8C(0xFE, 155, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2854)
    Sleep(100)

    def lambda_2867():
        OP_8C(0xFE, 155, 22)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2867)
    Sleep(100)

    def lambda_287A():
        OP_8C(0xFE, 155, 25)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_287A)

    def lambda_2888():
        OP_8F(0xFE, 0xFFFEF318, 0x1C84, 0x24B8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2888)
    Sleep(500)

    def lambda_28A8():
        OP_8F(0xFE, 0xFFFEF318, 0x1C84, 0x24B8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28A8)
    Sleep(100)

    def lambda_28C8():
        OP_8C(0xFE, 155, 28)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_28C8)
    Sleep(100)

    def lambda_28DB():
        OP_8C(0xFE, 155, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_28DB)
    Sleep(100)

    def lambda_28EE():
        OP_8C(0xFE, 155, 32)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_28EE)
    Sleep(100)
    PlayEffect(0x1, 0x2, 0xE, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)

    def lambda_293B():
        OP_8F(0xFE, 0xFFFEF318, 0x1C84, 0x24B8, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_293B)
    Sleep(100)

    def lambda_295B():
        OP_8C(0xFE, 155, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_295B)
    Sleep(100)

    def lambda_296E():
        OP_8C(0xFE, 155, 28)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_296E)
    Sleep(100)
    Sleep(100)

    def lambda_2986():
        OP_8F(0xFE, 0xFFFEF318, 0xCE4, 0x24B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2986)
    Sleep(300)

    def lambda_29A6():
        OP_8C(0xFE, 155, 25)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_29A6)
    Sleep(100)

    def lambda_29B9():
        OP_8C(0xFE, 155, 22)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_29B9)
    Sleep(100)

    def lambda_29CC():
        OP_8C(0xFE, 155, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_29CC)

    def lambda_29DA():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_29DA)
    Sleep(500)
    Sleep(300)

    def lambda_29FF():
        OP_8C(0xFE, 155, 18)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_29FF)
    Sleep(100)

    def lambda_2A12():
        OP_8C(0xFE, 155, 16)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2A12)
    Sleep(100)

    def lambda_2A25():
        OP_8C(0xFE, 155, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2A25)
    Sleep(100)

    def lambda_2A38():
        OP_8C(0xFE, 155, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2A38)
    Sleep(1000)

    def lambda_2A4B():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A4B)
    Sleep(2000)
    OP_82(0x2, 0x2)
    WaitChrThread(0xFE, 0x2)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Return()

    # Function_5_2749 end

    def Function_6_2A84(): pass

    label("Function_6_2A84")

    SetChrPos(0xFE, -37060, 300, -13200, 291)

    def lambda_2A9B():
        OP_8E(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x1838, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A9B)
    Sleep(3000)

    def lambda_2ABB():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2ABB)
    Sleep(500)

    def lambda_2ADB():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2ADB)

    def lambda_2AF6():
        OP_8C(0xFE, 155, 6)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2AF6)
    Sleep(100)

    def lambda_2B09():
        OP_8C(0xFE, 155, 8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2B09)
    Sleep(100)

    def lambda_2B1C():
        OP_8C(0xFE, 155, 10)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2B1C)
    Sleep(100)

    def lambda_2B2F():
        OP_8C(0xFE, 155, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2B2F)
    Sleep(100)

    def lambda_2B42():
        OP_8C(0xFE, 155, 14)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2B42)
    Sleep(100)

    def lambda_2B55():
        OP_8C(0xFE, 155, 16)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2B55)
    Sleep(100)

    def lambda_2B68():
        OP_8C(0xFE, 155, 18)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2B68)
    Sleep(100)

    def lambda_2B7B():
        OP_8C(0xFE, 155, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2B7B)
    Sleep(100)

    def lambda_2B8E():
        OP_8C(0xFE, 155, 22)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2B8E)
    Sleep(100)

    def lambda_2BA1():
        OP_8C(0xFE, 155, 25)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2BA1)

    def lambda_2BAF():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BAF)
    Sleep(500)

    def lambda_2BCF():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BCF)
    Sleep(100)

    def lambda_2BEF():
        OP_8C(0xFE, 155, 28)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2BEF)
    Sleep(100)

    def lambda_2C02():
        OP_8C(0xFE, 155, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2C02)
    Sleep(100)

    def lambda_2C15():
        OP_8C(0xFE, 155, 32)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2C15)
    Sleep(100)

    def lambda_2C28():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C28)
    Sleep(100)

    def lambda_2C48():
        OP_8C(0xFE, 155, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2C48)
    Sleep(100)

    def lambda_2C5B():
        OP_8C(0xFE, 155, 28)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2C5B)
    Sleep(100)
    Sleep(100)

    def lambda_2C73():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C73)
    Sleep(300)

    def lambda_2C93():
        OP_8C(0xFE, 155, 25)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2C93)
    Sleep(100)

    def lambda_2CA6():
        OP_8C(0xFE, 155, 22)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2CA6)
    Sleep(100)

    def lambda_2CB9():
        OP_8C(0xFE, 155, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2CB9)

    def lambda_2CC7():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CC7)
    Sleep(500)
    Sleep(300)

    def lambda_2CEC():
        OP_8C(0xFE, 155, 18)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2CEC)
    Sleep(100)

    def lambda_2CFF():
        OP_8C(0xFE, 155, 16)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2CFF)
    Sleep(100)

    def lambda_2D12():
        OP_8C(0xFE, 155, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2D12)
    Sleep(100)

    def lambda_2D25():
        OP_8C(0xFE, 155, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2D25)
    Sleep(1000)

    def lambda_2D38():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D38)
    Return()

    # Function_6_2A84 end

    def Function_7_2D4E(): pass

    label("Function_7_2D4E")

    OP_99(0xFE, 0x3, 0x0, 0x3E8)
    SetChrChipByIndex(0xFE, 3)
    TurnDirection(0xFE, 0xD, 200)

    def lambda_2D69():

        label("loc_2D69")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_2D69")

    QueueWorkItem2(0xFE, 2, lambda_2D69)
    Return()

    # Function_7_2D4E end

    def Function_8_2D75(): pass

    label("Function_8_2D75")

    LoadEffect(0x1, "map\\\\mp021_00.eff")
    PlayEffect(0x1, 0x2, 0xE, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    OP_6F(0x2, 160)
    OP_70(0x2, 0xF0)

    def lambda_2DD7():
        OP_8F(0xFE, 0xFFFEF318, 0x2710, 0x24B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DD7)

    def lambda_2DF2():
        OP_8C(0xFE, 243, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2DF2)
    Sleep(100)

    def lambda_2E05():
        OP_8C(0xFE, 243, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2E05)
    Sleep(100)

    def lambda_2E18():
        OP_8C(0xFE, 243, 17)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2E18)
    Sleep(500)
    Sleep(300)

    def lambda_2E30():
        OP_8C(0xFE, 243, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2E30)
    Sleep(100)

    def lambda_2E43():
        OP_8C(0xFE, 243, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2E43)
    Sleep(100)
    Sleep(1000)

    def lambda_2E5B():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E5B)
    Sleep(500)

    def lambda_2E7B():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E7B)
    Sleep(500)

    def lambda_2E9B():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E9B)
    Sleep(500)

    def lambda_2EBB():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EBB)
    Sleep(500)

    def lambda_2EDB():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EDB)
    Sleep(500)

    def lambda_2EFB():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EFB)
    Sleep(500)

    def lambda_2F1B():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F1B)
    Sleep(500)

    def lambda_2F3B():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F3B)
    Sleep(500)

    def lambda_2F5B():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F5B)
    Sleep(500)
    Return()

    # Function_8_2D75 end

    def Function_9_2F76(): pass

    label("Function_9_2F76")


    def lambda_2F7C():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F7C)

    def lambda_2F97():
        OP_8C(0xFE, 243, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2F97)
    Sleep(100)

    def lambda_2FAA():
        OP_8C(0xFE, 243, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2FAA)
    Sleep(100)

    def lambda_2FBD():
        OP_8C(0xFE, 243, 17)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2FBD)
    Sleep(500)
    Sleep(300)

    def lambda_2FD5():
        OP_8C(0xFE, 243, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2FD5)
    Sleep(100)

    def lambda_2FE8():
        OP_8C(0xFE, 243, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2FE8)
    Sleep(100)
    Sleep(2000)

    def lambda_3000():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3000)
    Sleep(500)

    def lambda_3020():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3020)
    Sleep(500)

    def lambda_3040():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3040)
    Sleep(500)

    def lambda_3060():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3060)
    Sleep(500)

    def lambda_3080():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3080)
    Sleep(500)

    def lambda_30A0():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30A0)
    Sleep(500)

    def lambda_30C0():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30C0)
    Sleep(500)

    def lambda_30E0():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30E0)
    Sleep(500)

    def lambda_3100():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3100)
    Return()

    # Function_9_2F76 end

    def Function_10_3116(): pass

    label("Function_10_3116")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x386, 1)"), scpexpr(EXPR_END)), "loc_3185")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "熊刺草\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x0, 0x1)
    OP_A2(0x286)
    Jump("loc_31D7")

    label("loc_3185")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "熊刺草\x07\x00",
            "发现了，\x01\x07\x00",
            "不过现有的数量太多，不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_31D7")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_3116 end

    def Function_11_31E0(): pass

    label("Function_11_31E0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xF7, 1)"), scpexpr(EXPR_END)), "loc_3256")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "兽皮制服\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x293)
    Jump("loc_32CD")

    label("loc_3256")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "兽皮制服\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "兽皮制服\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_32CD")

    Jump("loc_3308")

    label("loc_32D0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x2)

    label("loc_3308")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_31E0 end

    SaveToFile()

Try(main)
