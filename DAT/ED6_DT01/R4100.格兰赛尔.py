from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'R4100   ._SN',
        MapName             = 'Grancel',
        Location            = 'R4100.x',
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
        '科洛丝',                               # 9
        '尤莉亚中尉',                           # 10
        '基库',                                 # 11
        '特务兵',                               # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '军用犬',                               # 15
        '军用犬',                               # 16
        '军用犬',                               # 17
        '军用犬',                               # 18
        '军用犬',                               # 19
        '士兵',                                 # 20
        '士兵',                                 # 21
        '士兵',                                 # 22
        '士兵',                                 # 23
        '士兵',                                 # 24
        '圣海姆门方向',                         # 25
        '艾尔贝周游道方向',                     # 26
        '王都格兰赛尔方向',                     # 27
        '炽炎草',                               # 28
        '炽炎草',                               # 29
        '地狱火爆麻雀',                         # 30
        '地狱火爆麻雀',                         # 31
        '沼泽剑齿吸血魔',                       # 32
        '沼泽剑齿吸血魔',                       # 33
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
        'ED6_DT07/CH00040 ._CH',             # 00
        'ED6_DT06/CH20114 ._CH',             # 01
        'ED6_DT07/CH02320 ._CH',             # 02
        'ED6_DT07/CH00341 ._CH',             # 03
        'ED6_DT09/CH10061 ._CH',             # 04
        'ED6_DT07/CH01640 ._CH',             # 05
        'ED6_DT06/CH20115 ._CH',             # 06
        'ED6_DT07/CH00041 ._CH',             # 07
        'ED6_DT09/CH10060 ._CH',             # 08
        'ED6_DT09/CH10780 ._CH',             # 09
        'ED6_DT09/CH10781 ._CH',             # 0A
        'ED6_DT09/CH10790 ._CH',             # 0B
        'ED6_DT09/CH10791 ._CH',             # 0C
        'ED6_DT09/CH10050 ._CH',             # 0D
        'ED6_DT09/CH10051 ._CH',             # 0E
        'ED6_DT09/CH10800 ._CH',             # 0F
        'ED6_DT09/CH10801 ._CH',             # 10
        'ED6_DT09/CH10810 ._CH',             # 11
        'ED6_DT09/CH10811 ._CH',             # 12
        'ED6_DT09/CH10820 ._CH',             # 13
        'ED6_DT09/CH10821 ._CH',             # 14
        'ED6_DT09/CH11220 ._CH',             # 15
        'ED6_DT09/CH11221 ._CH',             # 16
        'ED6_DT09/CH11230 ._CH',             # 17
        'ED6_DT09/CH11231 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH00040P._CP',             # 00
        'ED6_DT06/CH20114P._CP',             # 01
        'ED6_DT07/CH02320P._CP',             # 02
        'ED6_DT07/CH00341P._CP',             # 03
        'ED6_DT09/CH10061P._CP',             # 04
        'ED6_DT07/CH01640P._CP',             # 05
        'ED6_DT06/CH20115P._CP',             # 06
        'ED6_DT07/CH00041P._CP',             # 07
        'ED6_DT09/CH10060P._CP',             # 08
        'ED6_DT09/CH10780P._CP',             # 09
        'ED6_DT09/CH10781P._CP',             # 0A
        'ED6_DT09/CH10790P._CP',             # 0B
        'ED6_DT09/CH10791P._CP',             # 0C
        'ED6_DT09/CH10050P._CP',             # 0D
        'ED6_DT09/CH10051P._CP',             # 0E
        'ED6_DT09/CH10800P._CP',             # 0F
        'ED6_DT09/CH10801P._CP',             # 10
        'ED6_DT09/CH10810P._CP',             # 11
        'ED6_DT09/CH10811P._CP',             # 12
        'ED6_DT09/CH10820P._CP',             # 13
        'ED6_DT09/CH10821P._CP',             # 14
        'ED6_DT09/CH11220P._CP',             # 15
        'ED6_DT09/CH11221P._CP',             # 16
        'ED6_DT09/CH11230P._CP',             # 17
        'ED6_DT09/CH11231P._CP',             # 18
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -41770,
        Z                   = 0,
        Y                   = -5530,
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
        X                   = 137370,
        Z                   = -2050,
        Y                   = 5100,
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
        X                   = -16930,
        Z                   = 0,
        Y                   = 111160,
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


    DeclMonster(
        X                   = 13640,
        Z                   = -40,
        Y                   = -2250,
        Unknown_0C          = 0,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16650,
        Z                   = 300,
        Y                   = 2360,
        Unknown_0C          = 0,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15450,
        Z                   = -30,
        Y                   = 56010,
        Unknown_0C          = 0,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13350,
        Z                   = 110,
        Y                   = 68880,
        Unknown_0C          = 0,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 60840,
        Z                   = 10,
        Y                   = 16239,
        Unknown_0C          = 0,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 105890,
        Z                   = -1980,
        Y                   = 18620,
        Unknown_0C          = 0,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 16690,
        Y                   = -1000,
        Z                   = 31700,
        Range               = 36480,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x5546,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 31170,
        TriggerZ            = 0,
        TriggerY            = 32450,
        TriggerRange        = 1500,
        ActorX              = 31170,
        ActorZ              = 1700,
        ActorY              = 32450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29270,
        TriggerZ            = 0,
        TriggerY            = 21060,
        TriggerRange        = 1500,
        ActorX              = 29270,
        ActorZ              = 1800,
        ActorY              = 21060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34440,
        TriggerZ            = 0,
        TriggerY            = 31310,
        TriggerRange        = 1500,
        ActorX              = 34440,
        ActorZ              = 1700,
        ActorY              = 31310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_506",          # 00, 0
        "Function_1_534",          # 01, 1
        "Function_2_547",          # 02, 2
        "Function_3_1317",         # 03, 3
        "Function_4_1E2F",         # 04, 4
        "Function_5_1E5D",         # 05, 5
        "Function_6_1E8B",         # 06, 6
        "Function_7_1EB9",         # 07, 7
        "Function_8_1F10",         # 08, 8
        "Function_9_1F58",         # 09, 9
    )


    def Function_0_506(): pass

    label("Function_0_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_522")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_522")

    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_506 end

    def Function_1_534(): pass

    label("Function_1_534")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFE90D0, 0x3003B)
    Return()

    # Function_1_534 end

    def Function_2_547(): pass

    label("Function_2_547")

    ClearMapFlags(0x10000000)
    OP_B6(0x0)
    EventBegin(0x0)
    OP_6D(94030, -2000, 13780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0x9, 103460, -2000, 12700, 270)
    SetChrPos(0x8, 104570, -2000, 10950, 270)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 96990, 7000, 16000, 90)
    OP_8E(0x9, 0x172B4, 0xFFFFF830, 0x3598, 0x1388, 0x0)
    SetChrChipByIndex(0x9, 6)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x20)
    OP_8C(0x9, 135, 800)

    ChrTalk(
        0x9,
        "#172F这边，科洛丝！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 7)

    def lambda_63B():
        OP_8E(0xFE, 0x14C44, 0x28, 0x337C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_63B)
    Sleep(1000)
    OP_8C(0x9, 270, 800)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 1)

    def lambda_66C():
        OP_8E(0xFE, 0x1482A, 0x50, 0x35FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_66C)

    def lambda_687():
        OP_6C(57000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_687)

    def lambda_697():
        OP_6D(84370, 60, 13300, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_697)
    WaitChrThread(0x9, 0x1)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 6)
    SetChrFlags(0x9, 0x20)
    TurnDirection(0x9, 0x8, 800)

    def lambda_6D0():

        label("loc_6D0")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_6D0")

    QueueWorkItem2(0x9, 1, lambda_6D0)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 0)

    ChrTalk(
        0x8,
        (
            "#043F呼呼……\x01",
            "总算离开周游道了。\x02\x03",
            "接下来我们该怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#170F就这样顺着庭园大道去王都吧。\x01",
            "　\x02\x03",
            "我的部下事先做了些伪装的行动，\x01",
            "对方的警戒已经变得比较薄弱。\x02\x03",
            "再说你打扮成这个样子，\x01",
            "在到达协会之前应该不会被发现的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#042F我知道了……\x02\x03",
            "啊，那么尤莉亚你呢……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#170F我在这里挡住敌人。\x02\x03",
            "虽然没办法拖住太长时间，\x01",
            "但也应该足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#043F什么……那怎么可以！\x02\x03",
            "只有我一个人逃走……\x02\x03",
            "我也要和尤莉亚一起战斗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#176F……人都有各自必须要守护的东西。\x01",
            "　\x02\x03",
            "我留下来，\x01",
            "是为了自己的信念和责任。\x02\x03",
            "#170F虽然这样说有点失礼……\x01",
            "不过我认为，您只是在感情用事罢了。\x02\x03",
            "请不要忘记，\x01",
            "您不只是属于您自己一个人的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#049F…………………………\x02\x03",
            "#047F我明白了，尤莉亚。\x02\x03",
            "#040F但是，请答应我，\x01",
            "绝对不要做出危险的事……\x02\x03",
            "而且，等所有事件平息之后，\x01",
            "我们还要好好坐在空中庭园，\x01",
            "一起品尝祖母大人沏的红茶哦。\x02\x03",
            "#041F我学会做新的点心了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#171F我非常期待。\x02\x03",
            "那么，请赶快走吧。\x02\x03",
            "#172F……基库！\x01",
            "好好地保护她！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BEE():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BEE)
    OP_22(0x197, 0x0, 0x64)

    def lambda_C01():

        label("loc_C01")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_C01")

    QueueWorkItem2(0x8, 1, lambda_C01)
    SetChrFlags(0xA, 0x1)

    def lambda_C17():
        OP_8E(0xFE, 0x14492, 0xFA0, 0x3F8E, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C17)
    Sleep(200)
    OP_8C(0x8, 270, 300)
    SetChrChipByIndex(0x8, 7)

    def lambda_C43():
        OP_8E(0xFE, 0x10A18, 0x0, 0x337C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C43)

    def lambda_C5E():

        label("loc_C5E")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_C5E")

    QueueWorkItem2(0x9, 1, lambda_C5E)
    Sleep(100)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_C79():
        OP_6D(82000, 0, 13970, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C79)
    WaitChrThread(0xA, 0x1)
    OP_8E(0xA, 0xFB72, 0x7D0, 0x3F8E, 0x2328, 0x0)
    OP_44(0x9, 0xFF)
    SetChrPos(0xE, 108880, -2000, 5290, 0)
    SetChrPos(0xF, 110190, -2000, 6430, 0)
    SetChrPos(0x10, 111910, -2000, 6760, 0)
    SetChrPos(0x11, 109570, -2000, 3930, 0)
    SetChrPos(0x12, 110140, -2000, 2710, 0)
    SetChrPos(0xB, 111470, -2000, 4930, 0)
    SetChrPos(0xC, 112960, -2000, 5790, 0)
    SetChrPos(0xD, 112000, -2000, 3870, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    WaitChrThread(0x0, 0x1)

    ChrTalk(
        0x9,
        (
            "#176F那些人……\x01",
            "也差不多该追上了吧……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 400)

    def lambda_D9C():
        OP_6C(314000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D9C)

    def lambda_DAC():
        OP_6D(100950, -2000, 14190, 2900)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DAC)
    Sleep(2000)

    def lambda_DC9():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DC9)

    def lambda_DE4():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DE4)

    def lambda_DFF():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_DFF)

    def lambda_E1A():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E1A)

    def lambda_E35():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E35)

    def lambda_E50():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E50)

    def lambda_E6B():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E6B)

    def lambda_E86():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E86)
    Sleep(900)
    SetChrPos(0x9, 80010, 80, 13820, 0)
    TurnDirection(0x9, 0xB, 0)

    def lambda_EBE():
        OP_67(0, 6770, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_EBE)

    def lambda_ED6():
        OP_6B(3920, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_ED6)

    def lambda_EE6():
        OP_6D(88700, 0, 13370, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_EE6)
    Sleep(1000)

    def lambda_F03():
        OP_90(0xFE, 0xFFFFD508, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_F03)

    def lambda_F1E():
        OP_90(0xFE, 0xFFFFD508, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_F1E)
    Sleep(100)

    def lambda_F3E():
        OP_90(0xFE, 0xFFFFD508, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F3E)

    def lambda_F59():
        OP_90(0xFE, 0xFFFFD508, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F59)
    Sleep(100)

    def lambda_F79():
        OP_90(0xFE, 0xFFFFD6FC, 0x0, 0x2BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_F79)
    Sleep(200)

    def lambda_F99():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F99)
    Sleep(100)

    def lambda_FB9():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_FB9)
    Sleep(100)

    def lambda_FD9():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFFD44, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FD9)
    WaitChrThread(0xE, 0x1)
    SetChrChipByIndex(0xE, 8)
    SetChrChipByIndex(0xF, 8)

    def lambda_1003():

        label("loc_1003")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1003")

    QueueWorkItem2(0xE, 0, lambda_1003)

    def lambda_1016():

        label("loc_1016")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1016")

    QueueWorkItem2(0xF, 0, lambda_1016)
    WaitChrThread(0x10, 0x1)
    SetChrChipByIndex(0x10, 8)
    SetChrChipByIndex(0x11, 8)

    def lambda_1038():

        label("loc_1038")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1038")

    QueueWorkItem2(0x10, 0, lambda_1038)

    def lambda_104B():

        label("loc_104B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_104B")

    QueueWorkItem2(0x11, 0, lambda_104B)
    WaitChrThread(0x12, 0x1)
    SetChrChipByIndex(0x12, 8)

    def lambda_1068():

        label("loc_1068")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1068")

    QueueWorkItem2(0x12, 0, lambda_1068)
    WaitChrThread(0xD, 0x1)

    ChrTalk(
        0x9,
        (
            "#170F三个人……\x01",
            "再加上五只狗。\x02\x03",
            "#176F哼，被小看了吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10D0():
        OP_6D(80740, 0, 14730, 1200)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10D0)
    OP_6B(3200, 1200)

    ChrTalk(
        0x9,
        (
            "#176F那个人教我的剑法……\x01",
            "是该派上用场的时候了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x1F8, 0x0, 0x64)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "#172F王室亲卫队中队长……\x02\x03",
            "#177F尤莉亚·舒华兹——候教了！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 1)

    def lambda_11CD():
        OP_6D(88700, 0, 13370, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11CD)

    def lambda_11E5():
        OP_8E(0xFE, 0x15E3C, 0xFFFFFC18, 0x3732, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11E5)
    Sleep(200)
    SetChrChipByIndex(0xE, 4)

    def lambda_120A():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_120A)
    Sleep(50)
    SetChrChipByIndex(0xF, 4)
    SetChrChipByIndex(0x10, 4)

    def lambda_1234():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1234)

    def lambda_124F():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_124F)
    Sleep(100)
    SetChrChipByIndex(0x11, 4)

    def lambda_1274():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1274)
    Sleep(50)
    SetChrChipByIndex(0x12, 4)

    def lambda_1299():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1299)

    def lambda_12B4():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12B4)
    Sleep(100)

    def lambda_12D4():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12D4)

    def lambda_12EF():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_12EF)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/R4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_547 end

    def Function_3_1317(): pass

    label("Function_3_1317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E2E")
    OP_A2(0x607)
    EventBegin(0x0)
    SetChrPos(0x13, 23950, 0, 33710, 180)
    SetChrPos(0x14, 22810, 0, 34790, 180)
    SetChrPos(0x15, 25010, 0, 34710, 180)
    SetChrPos(0x16, 23120, 0, 36550, 180)
    SetChrPos(0x17, 24610, 0, 36760, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    ChrTalk(
        0x13,
        "喂，你们等一下！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 0)
    TurnDirection(0x102, 0x13, 0)
    TurnDirection(0x10E, 0x13, 0)

    def lambda_13C6():
        OP_8E(0xFE, 0x63A6, 0x0, 0x78C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_13C6)

    def lambda_13E1():
        OP_8E(0xFE, 0x5EBA, 0x0, 0x7BAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_13E1)

    def lambda_13FC():
        OP_8E(0xFE, 0x5E06, 0x0, 0x82BE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_13FC)

    def lambda_1417():
        OP_8E(0xFE, 0x669E, 0x0, 0x7EFD, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1417)

    def lambda_1432():
        OP_8E(0xFE, 0x64C8, 0x0, 0x8426, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1432)

    def lambda_144D():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_144D)
    OP_6D(23860, 0, 33760, 2000)
    SetChrPos(0x101, 25010, 0, 20590, 0)
    SetChrPos(0x102, 23710, 0, 20590, 0)
    SetChrPos(0x10E, 23720, 0, 19280, 0)

    def lambda_14A1():

        label("loc_14A1")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_14A1")

    QueueWorkItem2(0x13, 1, lambda_14A1)

    def lambda_14B2():

        label("loc_14B2")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_14B2")

    QueueWorkItem2(0x14, 1, lambda_14B2)

    def lambda_14C3():

        label("loc_14C3")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_14C3")

    QueueWorkItem2(0x15, 1, lambda_14C3)

    def lambda_14D4():

        label("loc_14D4")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_14D4")

    QueueWorkItem2(0x16, 1, lambda_14D4)

    def lambda_14E5():

        label("loc_14E5")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_14E5")

    QueueWorkItem2(0x17, 1, lambda_14E5)

    def lambda_14F6():
        OP_6D(25030, 0, 29550, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14F6)

    def lambda_150E():
        OP_8E(0xFE, 0x6626, 0x0, 0x6D88, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_150E)

    def lambda_1529():
        OP_8E(0xFE, 0x613A, 0x0, 0x6CFC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1529)

    def lambda_1544():
        OP_8E(0xFE, 0x631A, 0x0, 0x6838, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1544)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#004F（哎……？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F（好像是军队呢……）\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x2)

    ChrTalk(
        0x13,
        (
            "你们注意了。\x01",
            "艾尔贝离宫禁止参观。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 0x2)

    ChrTalk(
        0x13,
        (
            "就在昨天，\x01",
            "格兰赛尔的街上不是贴有公告吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那个……\x01",
            "我们并不是王都的市民。\x02\x03",
            "我们刚刚通过圣海姆门，\x01",
            "正在赶往王都格兰赛尔的途中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "什么，是旅行者啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "在恐怖分子活动的期间\x01",
            "沿着有这么多魔兽的街道徒步旅行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "你们还真是大胆啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎……\x01",
            "先不说什么恐怖分子。\x02\x03",
            "『艾尔贝离宫』是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F应该是指坐落在王都东边的\x01",
            "那座利贝尔王家的小型宫殿吧。\x02\x03",
            "我听说那里作为市民的休憩场所，\x01",
            "平常应该是自由开放的啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "不好意思，现在那里禁止进入。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "因为那里作为恐怖事件的搜查本部，\x01",
            "现在暂由军队接管使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F搜查本部吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "艾尔贝离宫周边的街道\x01",
            "虽然没有禁止进入……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "不过，为了避免被认为是恐怖分子，\x01",
            "我先在此劝诫你们别靠近那里。\x01",
            "这也是为了你们自身的安全着想。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x13, 0x63EC, 0x0, 0x75E4, 0xBB8, 0x0)

    def lambda_198A():
        OP_8F(0xFE, 0x5BAE, 0xFFFFFFF6, 0x7080, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_198A)

    def lambda_19A5():
        OP_8F(0xFE, 0x5C1C, 0xFFFFFFF6, 0x6CAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19A5)

    def lambda_19C0():
        OP_8F(0xFE, 0x5BD6, 0xFFFFFFF6, 0x6702, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 2, lambda_19C0)

    def lambda_19DB():

        label("loc_19DB")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_19DB")

    QueueWorkItem2(0x101, 1, lambda_19DB)

    def lambda_19EC():

        label("loc_19EC")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_19EC")

    QueueWorkItem2(0x102, 1, lambda_19EC)

    def lambda_19FD():

        label("loc_19FD")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_19FD")

    QueueWorkItem2(0x10E, 1, lambda_19FD)
    OP_43(0x13, 0x1, 0x0, 0x4)
    OP_43(0x16, 0x1, 0x0, 0x5)
    Sleep(100)
    OP_43(0x15, 0x1, 0x0, 0x6)
    OP_43(0x14, 0x1, 0x0, 0x5)
    Sleep(150)
    OP_43(0x17, 0x1, 0x0, 0x6)
    Sleep(1000)
    OP_6D(23230, -10, 27690, 3000)
    WaitChrThread(0x17, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10E, 0xFF)

    ChrTalk(
        0x10E,
        (
            "#130F真是严肃的气氛啊。\x02\x03",
            "越是说不要靠近，\x01",
            "我就越想靠近去看个究竟。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x101, 400)

    ChrTalk(
        0x10E,
        (
            "#130F怎么样，我们稍微绕个路，\x01",
            "去那个离宫附近看看吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯、嗯……\x01",
            "虽然我的好奇心也被勾起来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F刚刚才被警告过，\x01",
            "我们最好还是别去了吧。\x02\x03",
            "正如那些士兵所说，\x01",
            "那里很可能有恐怖分子埋伏着。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F哎，但那个不是……\x02\x03",
            "情报部把自己做的事\x01",
            "嫁祸给亲卫队和游击士的吗……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#012F艾丝蒂尔！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#013F（尽量不要把这件事泄露出去比较好。）\x01",
            "　\x02\x03",
            "（要是让一般人知道了，\x01",
            "　说不定会被卷进这件事来的。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F（说、说的也是……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x102, 400)

    ChrTalk(
        0x10E,
        (
            "#131F？？？\x02\x03",
            "情报……什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x10E, 400)

    ChrTalk(
        0x101,
        (
            "#506F哎，啊，嗯。\x02\x03",
            "不好意思，我什么也没说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F就是这样，\x01",
            "所以我们还是赶快去王都吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F啊……\x01",
            "真是遗憾啊，不过也没有办法。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_1E2E")

    Return()

    # Function_3_1317 end

    def Function_4_1E2F(): pass

    label("Function_4_1E2F")

    OP_8E(0xFE, 0x6586, 0x0, 0x611C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x55F0, 0x0, 0x41AA, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_4_1E2F end

    def Function_5_1E5D(): pass

    label("Function_5_1E5D")

    OP_8E(0xFE, 0x60E0, 0x0, 0x6554, 0xBB8, 0x0)
    OP_8E(0xFE, 0x52BC, 0x0, 0x461E, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_5_1E5D end

    def Function_6_1E8B(): pass

    label("Function_6_1E8B")

    OP_8E(0xFE, 0x67D4, 0x0, 0x5EA6, 0xBB8, 0x0)
    OP_8E(0xFE, 0x5C08, 0x0, 0x4646, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_1E8B end

    def Function_7_1EB9(): pass

    label("Function_7_1EB9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　王都格兰赛尔　１７９塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_1EB9 end

    def Function_8_1F10(): pass

    label("Function_8_1F10")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南　圣海姆门\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1F10 end

    def Function_9_1F58(): pass

    label("Function_9_1F58")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东　艾尔贝离宫　　２２４塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_1F58 end

    SaveToFile()

Try(main)
