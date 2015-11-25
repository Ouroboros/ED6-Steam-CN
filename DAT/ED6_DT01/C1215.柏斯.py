from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'C1215   ._SN',
        MapName             = 'Bose',
        Location            = 'C1215.x',
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
        '亚鲁瓦教授',                           # 9
        '魔兽',                                 # 10
        '魔兽',                                 # 11
        '宝箱魔兽',                             # 12
        '宝箱魔兽',                             # 13
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
        'ED6_DT07/CH02050 ._CH',             # 00
        'ED6_DT09/CH10410 ._CH',             # 01
        'ED6_DT07/CH00101 ._CH',             # 02
        'ED6_DT07/CH00111 ._CH',             # 03
        'ED6_DT07/CH00121 ._CH',             # 04
        'ED6_DT09/CH10411 ._CH',             # 05
        'ED6_DT09/CH10440 ._CH',             # 06
        'ED6_DT09/CH10441 ._CH',             # 07
        'ED6_DT09/CH10410 ._CH',             # 08
        'ED6_DT09/CH10411 ._CH',             # 09
        'ED6_DT09/CH10420 ._CH',             # 0A
        'ED6_DT09/CH10421 ._CH',             # 0B
        'ED6_DT09/CH10430 ._CH',             # 0C
        'ED6_DT09/CH10431 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02050P._CP',             # 00
        'ED6_DT09/CH10410P._CP',             # 01
        'ED6_DT07/CH00101P._CP',             # 02
        'ED6_DT07/CH00111P._CP',             # 03
        'ED6_DT07/CH00121P._CP',             # 04
        'ED6_DT09/CH10411P._CP',             # 05
        'ED6_DT09/CH10440P._CP',             # 06
        'ED6_DT09/CH10441P._CP',             # 07
        'ED6_DT09/CH10410P._CP',             # 08
        'ED6_DT09/CH10411P._CP',             # 09
        'ED6_DT09/CH10420P._CP',             # 0A
        'ED6_DT09/CH10421P._CP',             # 0B
        'ED6_DT09/CH10430P._CP',             # 0C
        'ED6_DT09/CH10431P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 380,
        Y                   = 3530,
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
        X                   = -4280,
        Z                   = 10000,
        Y                   = 4280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4190,
        Z                   = 10000,
        Y                   = 3730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 20670,
        Z                   = 0,
        Y                   = -5460,
        Unknown_0C          = 151,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x94,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19250,
        Z                   = 0,
        Y                   = 8320,
        Unknown_0C          = 329,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x97,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8520,
        Z                   = 0,
        Y                   = 19510,
        Unknown_0C          = 271,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x91,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17540,
        Z                   = 0,
        Y                   = 12440,
        Unknown_0C          = 223,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x96,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -3030,
        Y                   = -1000,
        Z                   = 14100,
        Range               = 2970,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x3DAE,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 11840,
        TriggerZ            = 0,
        TriggerY            = 40,
        TriggerRange        = 1000,
        ActorX              = 12620,
        ActorZ              = 1500,
        ActorY              = 60,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -11810,
        TriggerZ            = 0,
        TriggerY            = -40,
        TriggerRange        = 1000,
        ActorX              = -12660,
        ActorZ              = 1500,
        ActorY              = 90,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_293",          # 01, 1
        "Function_2_2C6",          # 02, 2
        "Function_3_2DC",          # 03, 3
        "Function_4_DAC",          # 04, 4
        "Function_5_E16",          # 05, 5
        "Function_6_E80",          # 06, 6
        "Function_7_10CE",         # 07, 7
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Return()

    # Function_0_292 end

    def Function_1_293(): pass

    label("Function_1_293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A5")
    OP_6F(0x0, 0)
    Jump("loc_2AC")

    label("loc_2A5")

    OP_6F(0x0, 60)

    label("loc_2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE")
    OP_6F(0x1, 0)
    Jump("loc_2C5")

    label("loc_2BE")

    OP_6F(0x1, 60)

    label("loc_2C5")

    Return()

    # Function_1_293 end

    def Function_2_2C6(): pass

    label("Function_2_2C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2C6")

    label("loc_2DB")

    Return()

    # Function_2_2C6 end

    def Function_3_2DC(): pass

    label("Function_3_2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAB")
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F啊！那个人是……\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    Fade(1000)
    OP_6C(225000, 0)

    def lambda_35C():
        OP_6D(40, 380, 3090, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_35C)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_91(0x8, 0x3E8, 0x0, 0xFFFFFDA8, 0x3E8, 0x0)
    Sleep(200)
    OP_63(0x8)
    OP_91(0x8, 0xFFFFFC18, 0x0, 0x258, 0x3E8, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_91(0x8, 0xFFFFFE0C, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
    Sleep(200)
    WaitChrThread(0x8, 0x1)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_43(0x9, 0x1, 0x0, 0x4)
    OP_43(0xA, 0x1, 0x0, 0x5)
    OP_63(0x8)
    OP_91(0x8, 0x1F4, 0x0, 0x12C, 0x3E8, 0x0)
    Sleep(400)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x8, 0x101, 400)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_8C(0x8, 315, 200)
    OP_8C(0x8, 45, 200)
    OP_8C(0x8, 0, 100)
    Sleep(400)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#131F哎呀，哎呀呀！\x02\x03",
            "救、救命啊～！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4C3():
        OP_8E(0x9, 0xFFFFFC68, 0x0, 0x1234, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4C3)

    def lambda_4DE():
        OP_8E(0xA, 0x4F6, 0x0, 0x1266, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4DE)
    OP_91(0x8, 0x0, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x103, 4)
    SetChrPos(0x101, -60, 0, 11030, 182)
    SetChrPos(0x102, 670, 0, 11700, 180)
    SetChrPos(0x103, -810, 0, 12320, 180)

    def lambda_55E():
        OP_90(0x101, 0x0, 0x0, 0xFFFFEC78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55E)

    def lambda_579():
        OP_90(0x102, 0x0, 0x0, 0xFFFFEC78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_579)

    def lambda_594():
        OP_90(0x103, 0x0, 0x0, 0xFFFFEC78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_594)
    WaitChrThread(0x101, 0x1)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x3EF, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_5D7"),
        (SWITCH_DEFAULT, "loc_5DC"),
    )


    label("loc_5D7")

    OP_B4(0x0)
    Jump("loc_5DC")

    label("loc_5DC")

    EventBegin(0x0)
    AddParty(0xD, 0x3)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrPos(0x101, 0, 0, 5400, 180)
    SetChrPos(0x102, -910, 0, 6810, 180)
    SetChrPos(0x103, 800, 0, 6800, 180)
    SetChrPos(0x10E, 0, 380, 3420, 0)
    OP_6D(0, 0, 4440, 0)

    def lambda_669():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_669)

    def lambda_679():
        OP_6D(-720, 0, 5910, 3000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_679)

    def lambda_691():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_691)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    Sleep(400)

    ChrTalk(
        0x10E,
        (
            "#131F呼呼……\x01",
            "得、得救了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#1P我以为是谁呢，\x01",
            "这不是亚鲁瓦教授吗。\x02\x03",
            "真是的～我以为是空贼团，\x01",
            "白紧张了一番呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F哈、哈哈哈，\x01",
            "很久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F你们认识吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#000F#1P嗯，这位先生是\x01",
            "是喜欢调查塔什么的考古学者。\x02\x03",
            "我们在洛连特为记者做护卫的时候，\x01",
            "曾经在翡翠之塔见过他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F哈哈哈，\x01",
            "你们又救了我一次啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x103,
        (
            "#022F我们刚才听到了说话的声音，\x01",
            "还有其他人在吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F哎呀，你们听到了啊。\x02\x03",
            "让你们见笑了，\x01",
            "那是我在进行研究时的坏习惯……\x02\x03",
            "如果嘴里不说些什么，\x01",
            "就无论如何也没办法进行思考。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F#1P什么嘛，原来是自言自语。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是这样啊，我明白了。\x01",
            "这个问题我们待会儿再讨论吧。\x02\x03",
            "在魔兽再次袭击我们之前，\x01",
            "先从塔里出去比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#131F……啊？\x02\x03",
            "现在就出去？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F有什么问题吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#131F可、可是我的调查还没有完呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F哦，这样啊。\x01",
            "那就随你高兴，继续调查吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)

    ChrTalk(
        0x103,
        (
            "#026F艾丝蒂尔、约修亚，\x01",
            "我们回去了。\x02\x03",
            "学者先生看来是想自己一个人回去。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        "#131F啊？\x02",
    )

    CloseMessageWindow()

    def lambda_BDC():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDC)

    def lambda_BEA():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BEA)
    Sleep(400)

    ChrTalk(
        0x101,
        "#509F#1P（哇啊，好可怕～～～）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F（……这根本就是胁迫嘛。）\x02",
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x10E,
        (
            "#131F对、对不起！\x01",
            "我决定现在就从塔里出去！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)

    ChrTalk(
        0x103,
        (
            "#027F哼哼，乖乖听话的男人才是最棒的哦㈱\x02\x03",
            "好了，艾丝蒂尔、约修亚，\x01",
            "快走吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#1P知道～了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F……哎呀哎呀。\x02",
    )

    CloseMessageWindow()

    def lambda_D53():
        OP_92(0x101, 0x103, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D53)

    def lambda_D68():
        OP_92(0x102, 0x103, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D68)

    def lambda_D7D():
        OP_92(0x10E, 0x103, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_D7D)
    OP_69(0x103, 0x578)
    WaitChrThread(0x10E, 0x1)
    OP_28(0xF, 0x4, 0x8)
    OP_28(0xF, 0x1, 0x4)
    OP_28(0xF, 0x1, 0x8)
    EventEnd(0x0)

    label("loc_DAB")

    Return()

    # Function_3_2DC end

    def Function_4_DAC(): pass

    label("Function_4_DAC")

    OP_22(0xBD, 0x0, 0x64)
    OP_8E(0x9, 0xFFFFEF48, 0x0, 0x10B8, 0x4650, 0x0)
    OP_22(0x212, 0x0, 0x64)
    OP_96(0x9, 0xFFFFEEB2, 0x0, 0x12A2, 0x7D0, 0x7D0)
    OP_22(0x212, 0x0, 0x64)
    OP_96(0x9, 0xFFFFF77C, 0x0, 0x196E, 0x578, 0xBB8)
    SetChrChipByIndex(0x9, 1)
    SetChrFlags(0x9, 0x1)
    TurnDirection(0xFE, 0x8, 400)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Return()

    # Function_4_DAC end

    def Function_5_E16(): pass

    label("Function_5_E16")

    Sleep(600)
    OP_8E(0xA, 0x105E, 0x0, 0xE92, 0x4650, 0x0)
    OP_22(0x212, 0x0, 0x64)
    OP_96(0xA, 0xE1A, 0x0, 0x12AC, 0x9C4, 0x9C4)
    OP_22(0x212, 0x0, 0x64)
    OP_96(0xA, 0x938, 0x0, 0x196E, 0x578, 0xBB8)
    SetChrChipByIndex(0xA, 1)
    SetChrFlags(0xA, 0x1)
    TurnDirection(0xFE, 0x8, 400)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    # Function_5_E16 end

    def Function_6_E80(): pass

    label("Function_6_E80")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1032")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F62")
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 12620, 3000, 60, 320)
    TurnDirection(0xB, 0x0, 0)

    def lambda_ECF():
        OP_8F(0xFE, 0x314C, 0x5DC, 0x3C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_ECF)

    def lambda_EEA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_EEA)
    ClearChrFlags(0xB, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0xA0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_F3D"),
        (2, "loc_F4F"),
        (1, "loc_F5F"),
        (SWITCH_DEFAULT, "loc_F62"),
    )


    label("loc_F3D")

    OP_A2(0x382)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_F62")

    label("loc_F4F")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_F5F")

    OP_B4(0x0)
    Return()

    label("loc_F62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xF8, 1)"), scpexpr(EXPR_END)), "loc_FB9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "锁片薄衣\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x380)
    Jump("loc_102F")

    label("loc_FB9")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "锁片薄衣\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "锁片薄衣\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_102F")

    Jump("loc_10C0")

    label("loc_1032")

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
    OP_83(0xF, 0xD)

    label("loc_10C0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_E80 end

    def Function_7_10CE(): pass

    label("Function_7_10CE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1292")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B0")
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xC, -12660, 3000, 90, 320)
    TurnDirection(0xC, 0x0, 0)

    def lambda_111D():
        OP_8F(0xFE, 0xFFFFCE8C, 0x5DC, 0x5A, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_111D)

    def lambda_1138():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1138)
    ClearChrFlags(0xC, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x9F, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_118B"),
        (2, "loc_119D"),
        (1, "loc_11AD"),
        (SWITCH_DEFAULT, "loc_11B0"),
    )


    label("loc_118B")

    OP_A2(0x383)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_11B0")

    label("loc_119D")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_11AD")

    OP_B4(0x0)
    Return()

    label("loc_11B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x144, 1)"), scpexpr(EXPR_END)), "loc_120D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "翠耀石护符\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x381)
    Jump("loc_128F")

    label("loc_120D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "翠耀石护符\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "翠耀石护符\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_128F")

    Jump("loc_12D9")

    label("loc_1292")

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
    OP_83(0xF, 0xE)

    label("loc_12D9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_10CE end

    SaveToFile()

Try(main)
