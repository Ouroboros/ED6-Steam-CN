from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3402   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3402.x',
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
        '小女孩',                               # 9
        '艾尔·雷登关所方向',                   # 10
        '蔡斯方向',                             # 11
        '卡鲁迪亚钟乳洞方向',                   # 12
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
        'ED6_DT07/CH00060 ._CH',             # 00
        'ED6_DT07/CH00061 ._CH',             # 01
        'ED6_DT09/CH10130 ._CH',             # 02
        'ED6_DT09/CH10131 ._CH',             # 03
        'ED6_DT09/CH10750 ._CH',             # 04
        'ED6_DT09/CH10751 ._CH',             # 05
        'ED6_DT09/CH10760 ._CH',             # 06
        'ED6_DT09/CH10761 ._CH',             # 07
        'ED6_DT09/CH10770 ._CH',             # 08
        'ED6_DT09/CH10771 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH00060P._CP',             # 00
        'ED6_DT07/CH00061P._CP',             # 01
        'ED6_DT09/CH10130P._CP',             # 02
        'ED6_DT09/CH10131P._CP',             # 03
        'ED6_DT09/CH10750P._CP',             # 04
        'ED6_DT09/CH10751P._CP',             # 05
        'ED6_DT09/CH10760P._CP',             # 06
        'ED6_DT09/CH10761P._CP',             # 07
        'ED6_DT09/CH10770P._CP',             # 08
        'ED6_DT09/CH10771P._CP',             # 09
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

    DeclNpc(
        X                   = 320150,
        Z                   = 0,
        Y                   = -37050,
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
        X                   = 574100,
        Z                   = 0,
        Y                   = -54930,
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
        X                   = 400800,
        Z                   = -30,
        Y                   = 22800,
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
        X                   = 367410,
        Z                   = 10,
        Y                   = -42400,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 389970,
        Z                   = 10,
        Y                   = -68740,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 425100,
        Z                   = 0,
        Y                   = -71190,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 467260,
        Z                   = 0,
        Y                   = -70580,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 497850,
        Z                   = -20,
        Y                   = -51510,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 506530,
        Z                   = 0,
        Y                   = -62560,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 526430,
        Z                   = 30,
        Y                   = -100000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 402970,
        Z                   = -20,
        Y                   = -38570,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 422790,
        Z                   = -10,
        Y                   = -33010,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 407380,
        Z                   = -20,
        Y                   = -4320,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 537500,
        Y                   = -1000,
        Z                   = -53500,
        Range               = 532500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF09E8,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = 558400,
        Y                   = -1000,
        Z                   = -50000,
        Range               = 561500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF19EC,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 411920,
        TriggerZ            = 0,
        TriggerY            = -58300,
        TriggerRange        = 1500,
        ActorX              = 411920,
        ActorZ              = 1500,
        ActorY              = -58300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 423050,
        TriggerZ            = -40,
        TriggerY            = -33400,
        TriggerRange        = 1000,
        ActorX              = 423660,
        ActorZ              = -40,
        ActorY              = -33400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 499670,
        TriggerZ            = -60,
        TriggerY            = -114340,
        TriggerRange        = 1000,
        ActorX              = 499140,
        ActorZ              = -60,
        ActorY              = -114740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 514840,
        TriggerZ            = -20,
        TriggerY            = -121220,
        TriggerRange        = 1000,
        ActorX              = 514850,
        ActorZ              = -20,
        ActorY              = -121830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 551940,
        TriggerZ            = 0,
        TriggerY            = -50340,
        TriggerRange        = 1500,
        ActorX              = 551940,
        ActorZ              = 1500,
        ActorY              = -50340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_386",          # 00, 0
        "Function_1_387",          # 01, 1
        "Function_2_3F6",          # 02, 2
        "Function_3_AD9",          # 03, 3
        "Function_4_B79",          # 04, 4
        "Function_5_E3C",          # 05, 5
        "Function_6_EA8",          # 06, 6
        "Function_7_F07",          # 07, 7
        "Function_8_105D",         # 08, 8
        "Function_9_119A",         # 09, 9
    )


    def Function_0_386(): pass

    label("Function_0_386")

    Return()

    # Function_0_386 end

    def Function_1_387(): pass

    label("Function_1_387")

    OP_16(0x2, 0xFA0, 0x4E200, 0xFFFD44C8, 0x30039)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AA")
    OP_1B(0x0, 0x0, 0x4)

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC")
    OP_6F(0x11, 0)
    Jump("loc_3C3")

    label("loc_3BC")

    OP_6F(0x11, 60)

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D5")
    OP_6F(0xF, 0)
    Jump("loc_3DC")

    label("loc_3D5")

    OP_6F(0xF, 60)

    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE")
    OP_6F(0x10, 0)
    Jump("loc_3F5")

    label("loc_3EE")

    OP_6F(0x10, 60)

    label("loc_3F5")

    Return()

    # Function_1_387 end

    def Function_2_3F6(): pass

    label("Function_2_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD8")
    OP_A2(0x505)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(541390, 0, -59060, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 533830, 0, -55500, 135)
    SetChrPos(0x102, 534050, -20, -54120, 135)
    SetChrPos(0x8, 550900, 0, -55310, 270)
    OP_0D()

    def lambda_47F():
        OP_8E(0xFE, 0x83D24, 0x0, 0xFFFF162C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47F)
    Sleep(500)

    def lambda_49F():
        OP_8E(0xFE, 0x83CD4, 0x0, 0xFFFF1B5E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_49F)
    Sleep(2000)

    NpcTalk(
        0x8,
        "声音",
        (
            "#1S#3P呼……呼……\x01",
            "必、必须要赶快完成……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 90, 400)
    OP_8C(0x102, 90, 400)

    ChrTalk(
        0x101,
        "#004F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F……好像有人过来了。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 1)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x8, 0x843DC, 0x0, 0xFFFF199C, 0x1770, 0x0)
    SetChrChipByIndex(0x8, 0)
    OP_8C(0x8, 270, 400)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#064F#2P啊……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F哟，你好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F怎么了，急成这个样子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#061F#2P啊，你们好。\x02\x03",
            "#060F请问……\x01",
            "姐姐你们是沿着这条隧道走来的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F嗯，是呢。怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#063F#2P那个那个……\x01",
            "你们在途中有没有看到熄灭的照明灯？\x02\x03",
            "就是安装在\x01",
            "隧道岩壁上的灯……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 4)), scpexpr(EXPR_END)), "loc_79C")

    ChrTalk(
        0x101,
        (
            "#006F熄灭的照明灯……\x01",
            "没看到哦。\x02\x03",
            "不过，倒是看到过\x01",
            "亮度非常强的灯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F大概是跨过两条河的地方吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_861")

    label("loc_79C")


    ChrTalk(
        0x101,
        (
            "#007F唔……不好意思。\x01",
            "我一点也没注意到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F虽说没见到过熄灭了的照明灯，\x01",
            "不过跨过两条河的地方\x01",
            "有一盏照明灯好像不太亮。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_861")


    ChrTalk(
        0x8,
        (
            "#065F#2P就是那个！\x02\x03",
            "果、果然\x01",
            "和我想的一样～……\x02\x03",
            "对不起。\x01",
            "我得马上走了！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x8, 1)

    def lambda_8D0():

        label("loc_8D0")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_8D0")

    QueueWorkItem2(0x101, 1, lambda_8D0)

    def lambda_8E1():

        label("loc_8E1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_8E1")

    QueueWorkItem2(0x102, 1, lambda_8E1)

    def lambda_8F2():
        OP_6D(539960, 0, -59290, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F2)
    OP_8E(0x8, 0x83B1C, 0x0, 0xFFFF1FDC, 0x1770, 0x0)
    OP_8E(0x8, 0x83234, 0xFFFFFFEC, 0xFFFF20FE, 0x1770, 0x0)
    OP_8E(0x8, 0x821E0, 0x14, 0xFFFF30B2, 0x1770, 0x0)
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x102,
        (
            "#010F是蔡斯市的孩子吧，\x01",
            "感觉那一身打扮好奇特。\x02\x03",
            "为什么那么慌张呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯～\x01",
            "我有点担心啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F约修亚，\x01",
            "我们追过去看看吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F就知道你会这么说。\x02\x03",
            "让一个小女孩独自走到这种地方，\x01",
            "的确也是太危险了。\x02\x03",
            "还是追上去比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯！\x01",
            "我们快追吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    EventEnd(0x0)

    label("loc_AD8")

    Return()

    # Function_2_3F6 end

    def Function_3_AD9(): pass

    label("Function_3_AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B78")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B28")

    ChrTalk(
        0x101,
        (
            "#000F真是在意那个孩子啊………\x01",
            "快点追上去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5D")

    label("loc_B28")


    ChrTalk(
        0x102,
        (
            "#010F如果要追那个孩子的话，\x01",
            "最好快一点……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5D")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_B78")

    Return()

    # Function_3_AD9 end

    def Function_4_B79(): pass

    label("Function_4_B79")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 5)), scpexpr(EXPR_END)), "loc_CD7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDE")

    ChrTalk(
        0x108,
        (
            "#073F哦，这边是相反方向。\x02\x03",
            "现在要尽快赶回蔡斯。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD4")

    label("loc_BDE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3D")

    ChrTalk(
        0x102,
        (
            "#012F走错路了……\x02\x03",
            "现在要赶快回蔡斯去才行。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD4")

    label("loc_C3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8E")

    ChrTalk(
        0x107,
        (
            "#064F啊，这边的路不对。\x02\x03",
            "不赶快回城的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD4")

    label("loc_C8E")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#012F应该不是走这边哦。\x02\x03",
            "现在要赶快回蔡斯去。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD4")

    Jump("loc_E20")

    label("loc_CD7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4C")
    TurnDirection(0x107, 0x0, 400)

    ChrTalk(
        0x107,
        (
            "#064F那个～\x01",
            "我们好像走过头了。\x02\x03",
            "钟乳洞应该在刚才来这里的途中。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_D4C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBA")

    ChrTalk(
        0x107,
        (
            "#064F啊，\x01",
            "我们好像走过头了。\x02\x03",
            "钟乳洞应该在刚才来这里的途中。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_DBA")

    TurnDirection(0x107, 0x0, 400)

    ChrTalk(
        0x107,
        (
            "#064F啊，\x01",
            "我们好像走过头了。\x02\x03",
            "钟乳洞应该在刚才来这里的途中。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E20")

    OP_90(0x0, 0x3E8, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_4_B79 end

    def Function_5_E3C(): pass

    label("Function_5_E3C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　钟乳洞\x01",
            "※魔兽很多，危险！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_E3C end

    def Function_6_EA8(): pass

    label("Function_6_EA8")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东　蔡斯市\x01",
            "西　艾尔·雷登　４４８塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_EA8 end

    def Function_7_F07(): pass

    label("Function_7_F07")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_F7E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "大回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x596)
    Jump("loc_FF6")

    label("loc_F7E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "大回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "大回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_FF6")

    Jump("loc_104F")

    label("loc_FF9")

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
    OP_83(0xF, 0x9F)

    label("loc_104F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_F07 end

    def Function_8_105D(): pass

    label("Function_8_105D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_10D8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "圣灵药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x597)
    Jump("loc_1158")

    label("loc_10D8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "圣灵药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "圣灵药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_1158")

    Jump("loc_118C")

    label("loc_115B")

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
    OP_83(0xF, 0xA0)

    label("loc_118C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_105D end

    def Function_9_119A(): pass

    label("Function_9_119A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_1211")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "大回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x598)
    Jump("loc_1289")

    label("loc_1211")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "大回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "大回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_1289")

    Jump("loc_12E8")

    label("loc_128C")

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
    OP_83(0xF, 0xA1)

    label("loc_12E8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_119A end

    SaveToFile()

Try(main)
