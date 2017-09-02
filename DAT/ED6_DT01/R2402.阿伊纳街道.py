from ED6ScenarioHelper import *

def main():
    # 阿伊纳街道

    CreateScenaFile(
        FileName            = 'R2402   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2402.x',
        MapIndex            = 103,
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
        '黑衣男子',                             # 9
        '黑衣男子',                             # 10
        '阿加特',                               # 11
        '蒙面队长',                             # 12
        '目标用摄像机',                         # 13
        '卢安方向',                             # 14
        '艾尔·雷登关所方向',                   # 15
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
        Unknown_3A              = 103,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00341 ._CH',             # 00
        'ED6_DT07/CH00151 ._CH',             # 01
        'ED6_DT07/CH00152 ._CH',             # 02
        'ED6_DT07/CH00260 ._CH',             # 03
        'ED6_DT07/CH00340 ._CH',             # 04
        'ED6_DT07/CH00341 ._CH',             # 05
        'ED6_DT07/CH00342 ._CH',             # 06
        'ED6_DT07/CH00344 ._CH',             # 07
        'ED6_DT07/CH00260 ._CH',             # 08
        'ED6_DT07/CH00261 ._CH',             # 09
        'ED6_DT07/CH00262 ._CH',             # 0A
        'ED6_DT07/CH00264 ._CH',             # 0B
        'ED6_DT07/CH00265 ._CH',             # 0C
        'ED6_DT09/CH10520 ._CH',             # 0D
        'ED6_DT09/CH10521 ._CH',             # 0E
        'ED6_DT09/CH10340 ._CH',             # 0F
        'ED6_DT09/CH10341 ._CH',             # 10
        'ED6_DT09/CH11040 ._CH',             # 11
        'ED6_DT09/CH11041 ._CH',             # 12
        'ED6_DT09/CH11070 ._CH',             # 13
        'ED6_DT09/CH11071 ._CH',             # 14
        'ED6_DT09/CH11080 ._CH',             # 15
        'ED6_DT09/CH11081 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT07/CH00341P._CP',             # 00
        'ED6_DT07/CH00151P._CP',             # 01
        'ED6_DT07/CH00152P._CP',             # 02
        'ED6_DT07/CH00260P._CP',             # 03
        'ED6_DT07/CH00340P._CP',             # 04
        'ED6_DT07/CH00341P._CP',             # 05
        'ED6_DT07/CH00342P._CP',             # 06
        'ED6_DT07/CH00344P._CP',             # 07
        'ED6_DT07/CH00260P._CP',             # 08
        'ED6_DT07/CH00261P._CP',             # 09
        'ED6_DT07/CH00262P._CP',             # 0A
        'ED6_DT07/CH00264P._CP',             # 0B
        'ED6_DT07/CH00265P._CP',             # 0C
        'ED6_DT09/CH10520P._CP',             # 0D
        'ED6_DT09/CH10521P._CP',             # 0E
        'ED6_DT09/CH10340P._CP',             # 0F
        'ED6_DT09/CH10341P._CP',             # 10
        'ED6_DT09/CH11040P._CP',             # 11
        'ED6_DT09/CH11041P._CP',             # 12
        'ED6_DT09/CH11070P._CP',             # 13
        'ED6_DT09/CH11071P._CP',             # 14
        'ED6_DT09/CH11080P._CP',             # 15
        'ED6_DT09/CH11081P._CP',             # 16
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

    DeclNpc(
        X                   = -4970,
        Z                   = 0,
        Y                   = 153310,
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
        X                   = -930,
        Z                   = 0,
        Y                   = -3800,
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
        X                   = 4300,
        Z                   = -30,
        Y                   = 113330,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1AB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19510,
        Z                   = 210,
        Y                   = 102750,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1AE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2490,
        Z                   = 110,
        Y                   = 49730,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1AD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1490,
        Z                   = 740,
        Y                   = 62250,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1B3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -2060,
        TriggerZ            = 0,
        TriggerY            = 120820,
        TriggerRange        = 1500,
        ActorX              = -2060,
        ActorZ              = 1500,
        ActorY              = 120820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30,
        TriggerZ            = 240,
        TriggerY            = 75790,
        TriggerRange        = 1000,
        ActorX              = 360,
        ActorZ              = 240,
        ActorY              = 76370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2FA",          # 00, 0
        "Function_1_320",          # 01, 1
        "Function_2_368",          # 02, 2
        "Function_3_1BEF",         # 03, 3
        "Function_4_1CD5",         # 04, 4
        "Function_5_1D76",         # 05, 5
        "Function_6_1F19",         # 06, 6
        "Function_7_1F6D",         # 07, 7
        "Function_8_1FCA",         # 08, 8
    )


    def Function_0_2FA(): pass

    label("Function_0_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_31F")
    OP_A3(0x3FA)
    Event(0, 2)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x4)

    label("loc_31F")

    Return()

    # Function_0_2FA end

    def Function_1_320(): pass

    label("Function_1_320")

    OP_16(0x2, 0xFA0, 0xFFFDECC0, 0xFFFF34E0, 0x30025)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344")
    OP_6F(0x0, 0)
    Jump("loc_34B")

    label("loc_344")

    OP_6F(0x0, 60)

    label("loc_34B")

    SoundDistance(0x1C5, 0xFFFFF092, 0x3E8, 0x20FC6, 0x2710, 0x9C40, 0x64, 0x0)
    Return()

    # Function_1_320 end

    def Function_2_368(): pass

    label("Function_2_368")

    FadeToBright(2000, 0)
    OP_77(0x41, 0x64, 0x82, 0x0, 0x0)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-4600, 3000, 117500, 0)
    OP_6B(3400, 0)
    OP_67(0, 3300, -10000, 0)
    OP_6C(52000, 0)
    SetChrPos(0x8, -4900, 0, 125700, 0)
    SetChrPos(0x9, -3900, 0, 125000, 0)
    SetChrPos(0xA, 5300, 0, 139100, 0)

    def lambda_3EE():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3EE)
    OP_6D(-4600, 0, 117500, 5000)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_41E():
        OP_8E(0xFE, 0xFFFFE9BC, 0x0, 0x1C4BC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_41E)

    def lambda_439():
        OP_8E(0xFE, 0xFFFFEE08, 0x0, 0x1CAFC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_439)
    WaitChrThread(0x9, 0x1)

    def lambda_459():
        OP_8C(0x9, 0, 800)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_459)
    WaitChrThread(0x8, 0x1)

    def lambda_46C():
        OP_8C(0x8, 0, 800)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_46C)

    ChrTalk(
        0x8,
        "呼呼～～～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这家伙怎么这么缠人呀！\x02",
    )

    CloseMessageWindow()

    def lambda_4AA():
        OP_6C(21000, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4AA)
    OP_43(0xA, 0x1, 0x0, 0x5)

    ChrTalk(
        0xA,
        "#10A别逃！！（※假定）\x05\x02",
    )

    Sleep(200)
    OP_43(0x8, 0x1, 0x0, 0x3)
    Sleep(200)
    OP_43(0x9, 0x1, 0x0, 0x4)
    OP_6A(0x9)
    Sleep(600)

    ChrTalk(
        0x9,
        (
            "#20A带着这么大把剑\x01",
            "怎么还能追的上来呀！？\x05\x02",
        )
    )

    Sleep(2400)

    ChrTalk(
        0xA,
        "#5P#10A呵，我和你们锻炼的方法可不一样啊。\x05\x02",
    )

    Sleep(1400)

    ChrTalk(
        0xA,
        "#5P呀啊～～～～～！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x1)

    def lambda_593():
        OP_6C(348000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_593)

    ChrTalk(
        0x8,
        (
            "唔……\x01",
            "怎么都甩不掉吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CC():
        OP_97(0x8, 0xFFFFE37C, 0xDC50, 0x9C40, 0x5DC, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5CC)

    ChrTalk(
        0x9,
        "没办法了，迎击吧！\x02",
    )

    CloseMessageWindow()

    def lambda_604():
        OP_97(0x9, 0xFFFFE37C, 0xDC50, 0xFFFF63C0, 0x5DC, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_604)
    OP_96(0xA, 0xFFFFE0C0, 0x0, 0xE358, 0x1F4, 0x3A98)
    OP_99(0xA, 0x7, 0x0, 0x7D0)

    ChrTalk(
        0xA,
        (
            "#050F你们好像勉勉强强\x01",
            "才撑到现在嘛。\x02\x03",
            "和你们捉迷藏追到你们厌烦，\x01",
            "是件很开心的事哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "被你穷追不舍的怨恨\x01",
            "一定要你的死来补偿！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "愚蠢的家伙！\x01",
            "2对1你还想赢吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#050F哈哈，\x01",
            "当然是想赢的啰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#050F打架要全神贯注。\x01",
            "在气魄上输了就完了。\x02\x03",
            "在你们夹着尾巴逃跑的时候\x01",
            "就注定你们是丧家之犬。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "胡说！\x01",
            "你这个游击会的狗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "看我们两个\x01",
            "怎么折磨死你！（※假定发生自动战斗）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0x9, 0xA, 0)

    def lambda_838():
        OP_94(0x1, 0xFE, 0x0, 0x7D0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_838)

    def lambda_84E():
        OP_94(0x1, 0xFE, 0x0, 0x7D0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_84E)
    Sleep(500)
    Fade(1000)
    OP_44(0xA, 0xFF)
    OP_6B(3000, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6C(45000, 0)
    SetChrPos(0x8, -8400, 0, 54200, 0)
    SetChrPos(0x9, -9800, 0, 54800, 0)
    SetChrPos(0xB, -6700, 0, 58700, 180)
    SetChrPos(0xA, -7300, 0, 56400, 0)
    TurnDirection(0xA, 0x8, 0)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0x9, 0xA, 0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 7)
    SetChrChipByIndex(0x9, 7)

    ChrTalk(
        0x8,
        "唔～～～～～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔……\x01",
            "怎么能在这里被抓住………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#050F哼，快点投降\x01",
            "给我老实坦白吧！\x02\x03",
            "你们是什么人\x01",
            "有什么企图……\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)

    ChrTalk(
        0xB,
        "青年的声音──那样的话会让我十分困扰呀。\x02",
    )

    CloseMessageWindow()

    def lambda_9FD():
        OP_8C(0xA, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_9FD)

    ChrTalk(
        0xA,
        "#050F#10A啊！？\x05\x02",
    )

    Sleep(300)
    SetChrChipByIndex(0xA, 1)
    OP_96(0xA, 0xFFFFE890, 0x0, 0xD6D8, 0x3E8, 0x2710)

    def lambda_A43():

        label("loc_A43")

        TurnDirection(0xA, 0xB, 0)
        OP_48()
        Jump("loc_A43")

    QueueWorkItem2(0xA, 1, lambda_A43)

    ChrTalk(
        0xA,
        "#050F你什么时候………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊，队长！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "您来救我们了吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "真拿你们没办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我正想怎么联络比约定的时候晚，\x01",
            "原来你们在这里玩耍呀。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AEC():
        OP_99(0x8, 0x3, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AEC)

    ChrTalk(
        0x8,
        "实，实在是抱歉！\x02",
    )

    CloseMessageWindow()

    def lambda_B1A():
        OP_99(0x9, 0x3, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B1A)

    ChrTalk(
        0x9,
        "有很多人在妨碍我们………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#050F原来如此……\x01",
            "你就是首领啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "呵呵，\x01",
            "我只不过是现场责任人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "对于部下的失礼我道歉。\x01",
            "能不能在这放过我们一把呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#050F啊？\x02\x03",
            "你刚才说什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "我说能不能放过我们一把。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我们这里也不打算\x01",
            "和游击士协会扯上什么关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#050F你是傻瓜啊！\x01",
            "我怎么可能会放过啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "哎呀哎呀～～～\x01",
            "我本来不打算说难听的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……你们两个。\x01",
            "这里有我来挡住他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "你们快点去汇合地点。\x02",
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)

    ChrTalk(
        0x8,
        "是！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 5)

    def lambda_D3D():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0xAB7C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D3D)

    ChrTalk(
        0x9,
        "太感谢了，队长！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 5)

    def lambda_D75():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0xAB7C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D75)
    OP_8C(0xA, 225, 800)

    ChrTalk(
        0xA,
        "#050F想逃吗？喂！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xB, 9)
    OP_8E(0xB, 0xFFFFE318, 0x0, 0xDEA8, 0x1F40, 0x0)

    def lambda_DCF():
        OP_6D(-8700, 0, 52500, 1000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_DCF)

    def lambda_DE7():
        OP_97(0xFE, 0xFFFFEC14, 0xD034, 0xFFFEDB08, 0x36B0, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DE7)
    SetChrChipByIndex(0xA, 1)
    OP_8E(0xA, 0xFFFFDF94, 0x0, 0xCF08, 0x1F40, 0x0)
    TurnDirection(0xA, 0xB, 0)

    def lambda_E23():

        label("loc_E23")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_E23")

    QueueWorkItem2(0xB, 0, lambda_E23)
    SetChrChipByIndex(0xA, 2)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 8)
    OP_94(0x1, 0xA, 0xB4, 0x3E8, 0xBB8, 0x0)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(
        0xA,
        (
            "#050F你……\x02\x03",
            "哼，算了。\x01",
            "那样我最多换个猎物抓。\x02\x03",
            "你身上应该带着\x01",
            "很重要的情报吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "呵呵……\x01",
            "那么简单就想抓住我吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_96(0xB, 0xFFFFD760, 0x0, 0xC738, 0x3E8, 0x1F40)

    def lambda_F2A():

        label("loc_F2A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_F2A")

    QueueWorkItem2(0xA, 0, lambda_F2A)

    ChrTalk(
        0xA,
        "#050F上等货色！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xA, 1)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    def lambda_F67():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_F67)
    OP_94(0x1, 0xA, 0xB4, 0x12C, 0x3E8, 0x0)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xC, 0x3E8)
    OP_43(0x8, 0x1, 0x0, 0x6)
    OP_93(0xA, 0xB, 0x44C, 0x3A98, 0x0)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xA, 2)

    def lambda_FF6():
        OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FF6)

    def lambda_100C():
        OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_100C)
    OP_9E(0xB, 0x1E, 0x0, 0x12C, 0x1388)
    WaitChrThread(0xB, 0x1)

    def lambda_103A():
        OP_94(0x1, 0xFE, 0x0, 0x5DC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_103A)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 8)
    OP_96(0xB, 0xFFFFCFF4, 0x514, 0xC47C, 0x514, 0x3A98)
    Sleep(100)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 10)

    def lambda_108C():
        OP_96(0xFE, 0xFFFFD828, 0x514, 0xC670, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_108C)

    def lambda_10AA():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_10AA)
    Sleep(200)

    def lambda_10BF():
        OP_96(0xFE, 0xFFFFDC10, 0x0, 0xCF08, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10BF)
    SetChrChipByIndex(0xA, 1)
    WaitChrThread(0xB, 0x1)
    OP_96(0xB, 0xFFFFDAE4, 0x0, 0xBAB8, 0x3E8, 0x2710)

    def lambda_10FE():
        OP_99(0xB, 0x7, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_10FE)
    OP_6B(2900, 1000)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 9)
    OP_96(0xB, 0xFFFFDF94, 0x0, 0xC030, 0x1F4, 0xBB8)

    def lambda_113E():
        OP_6B(2500, 1000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_113E)
    OP_96(0xB, 0xFFFFD954, 0x0, 0xC3B4, 0x1F4, 0x1B58)

    def lambda_1165():
        OP_8C(0xA, 30, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1165)
    OP_96(0xB, 0xFFFFE188, 0x0, 0xCA58, 0x1F4, 0x2710)

    def lambda_118A():
        OP_96(0xB, 0xFFFFDCD8, 0x0, 0xCB20, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_118A)
    OP_44(0xA, 0xFF)
    OP_8C(0xA, 315, 1300)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 8)

    def lambda_11C3():
        OP_96(0xFE, 0xFFFFDAE4, 0x1F4, 0xCABC, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_11C3)
    OP_8C(0xA, 135, 1600)
    Sleep(350)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 10)

    def lambda_11FD():
        OP_99(0xFE, 0x0, 0x2, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_11FD)
    TurnDirection(0xA, 0xB, 0)
    SetChrChipByIndex(0xA, 2)
    OP_99(0xA, 0x6, 0x7, 0x5DC)

    def lambda_1222():
        OP_99(0xA, 0x5, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1222)

    def lambda_1232():
        OP_99(0xFE, 0x2, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1232)

    def lambda_1242():
        OP_96(0xB, 0xFFFFDD3C, 0x0, 0xDDE0, 0xFA0, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1242)
    Sleep(200)

    def lambda_1265():
        OP_8C(0xA, 0, 500)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1265)
    Sleep(300)

    def lambda_1278():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1278)

    def lambda_1288():
        OP_96(0xA, 0xFFFFDD3C, 0x0, 0xDA5C, 0x7D0, 0x2710)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1288)

    def lambda_12A6():
        OP_99(0xA, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_12A6)
    Sleep(450)

    def lambda_12BB():
        OP_99(0xFE, 0x7, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_12BB)
    OP_8F(0xB, 0xFFFFE34A, 0x0, 0xDDE0, 0x3A98, 0x0)
    WaitChrThread(0xA, 0x1)
    PlayEffect(0x12, 0xFF, 0xFF, -8900, -1000, 56800, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_96(0xB, 0xFFFFEC78, 0x0, 0xDD7C, 0x514, 0x1388)
    Sleep(1000)

    def lambda_1346():
        OP_99(0xA, 0x7, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1346)

    def lambda_1356():
        TurnDirection(0xA, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1356)
    Sleep(500)

    ChrTalk(
        0xA,
        "#050F呼，很不错嘛！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "用厚重的铁块\x01",
            "把激情全都释放出来吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你……\x01",
            "和我有点相似啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#050F………………………\x02\x03",
            "……你说什么……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你曾经因为\x01",
            "自己的无用而被打败过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "你有那样的眼神。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#050F………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#050F呵呵呵，不错嘛。\x02\x03",
            "虽然我和你不相识，\x01",
            "但却相当中意你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我也和你一样，\x01",
            "对不中用的男人感到讨厌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我们就在这里\x01",
            "互相和解怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#050F不要开玩笑！！\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "battle\\\\mgaria0.eff")

    def lambda_157C():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_157C)
    PlayEffect(0x0, 0x0, 0xA, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0xA,
        (
            "#050F我没发话听你说，\x01",
            "你就给我见风使舵的瞎扯。\x02\x03",
            "你真是个完完全全混淆视听的家伙！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)

    ChrTalk(
        0xB,
        "唔……\x02",
    )

    CloseMessageWindow()

    def lambda_1637():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1637)

    ChrTalk(
        0xA,
        "#050F噢喔喔喔喔喔！\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x0, 0x1, 0xB, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_16A7():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_16A7)

    ChrTalk(
        0xB,
        "呀啊啊啊啊啊！\x02",
    )

    CloseMessageWindow()
    OP_44(0xB, 0xFF)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xA, 0x40)
    OP_99(0xA, 0x0, 0x3, 0x7D0)

    def lambda_16F4():
        OP_99(0xA, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_16F4)

    def lambda_1704():
        TurnDirection(0xA, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1704)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 10)

    def lambda_1722():
        OP_99(0xFE, 0x0, 0x3, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1722)

    def lambda_1732():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0xDA5C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1732)

    def lambda_174D():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0xDD7C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_174D)
    Sleep(200)
    FadeToDark(1, 16777215, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    FadeToBright(200, 16777215)

    def lambda_1787():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1787)
    Sleep(3000)
    OP_99(0xB, 0x3, 0x7, 0x5DC)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 11)
    OP_99(0xB, 0x0, 0x3, 0x514)

    ChrTalk(
        0xB,
        "哼……\x02",
    )

    CloseMessageWindow()

    def lambda_17CC():
        OP_99(0xA, 0x7, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_17CC)

    def lambda_17DC():
        TurnDirection(0xA, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_17DC)

    ChrTalk(
        0xA,
        (
            "#050F呼～～\x01",
            "你不止是个嘴上说说的家伙嘛。\x02\x03",
            "你们注定要\x01",
            "被游击会完全盯上的……\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x64, 0x3E8)

    ChrTalk(
        0xA,
        "#050F啊，什么！\x02",
    )

    CloseMessageWindow()
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)

    ChrTalk(
        0xA,
        (
            "#050F这，这是……\x01",
            "分身的战技！？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在昏暗树丛的空隙中\x01",
            "有隐隐约约的人影漂浮着。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男人的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "《呵呵呵……》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("男人的声音")

    AnonymousTalk(
        (
            "《那一击不错呀，\x01",
            "不过现在好像很迷茫的样子啊。》\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("男人的声音")

    AnonymousTalk(
        "《那种迷茫会把刀法弄乱的。》\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0xA,
        "#050F什么！？\x02",
    )

    CloseMessageWindow()
    SetChrName("男人的声音")

    AnonymousTalk(
        (
            "《要成为修罗的话\x01",
            "就必须要有舍弃一切的觉悟。》\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "《对于想活下去的人来说……\x01",
            "愤怒和悲伤的事还是忘了比较好。》\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "《就这样吧，再见啰……》\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "《………………………》\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "树丛间漂浮的人影\x01",
            "隐入黑暗消失了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    def lambda_1AC4():
        OP_6D(-5100, 1400, 56900, 1100)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1AC4)
    Sleep(1100)

    ChrTalk(
        0xA,
        (
            "#050F…………………………\x02\x03",
            "……竟然叫我忘了它……\x02\x03",
            "这种事……\x01",
            "……怎么可能办得到嘛……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B41():
        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1B41)

    def lambda_1B5B():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1B5B)

    def lambda_1B6B():
        OP_67(0, 6000, -10000, 2300)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1B6B)

    def lambda_1B83():
        OP_6C(54000, 2000)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1B83)
    OP_99(0xA, 0x0, 0x3, 0x7D0)
    Fade(1000)

    def lambda_1BA1():
        OP_99(0xA, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1BA1)

    ChrTalk(
        0xA,
        "#6P#20A呜喔喔喔喔喔！\x05\x02",
    )

    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FF)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_368 end

    def Function_3_1BEF(): pass

    label("Function_3_1BEF")

    SetChrFlags(0xFE, 0x40)
    OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDF30, 0x0, 0x186A0, 0x2710, 0x0)
    OP_8E(0xFE, 0xFFFFD634, 0x0, 0x15180, 0x2710, 0x0)

    def lambda_1C31():
        OP_6C(324000, 3000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C31)

    def lambda_1C41():
        OP_67(0, 5200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1C41)

    def lambda_1C59():
        OP_6D(-8000, 1300, 66400, 2700)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_1C59)
    ClearMapFlags(0x1)
    OP_8E(0xFE, 0xFFFFE0C0, 0x0, 0x11A08, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFE7C8, 0x0, 0x10CC0, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFEC14, 0x0, 0xFBF4, 0x32C8, 0x0)
    OP_8E(0xFE, 0xFFFFE7C8, 0x0, 0xE54C, 0x32C8, 0x0)
    OP_8E(0xFE, 0xFFFFDA80, 0x0, 0xBD74, 0x32C8, 0x0)
    Return()

    # Function_3_1BEF end

    def Function_4_1CD5(): pass

    label("Function_4_1CD5")

    SetChrFlags(0xFE, 0x40)
    OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDF30, 0x0, 0x186A0, 0x2710, 0x0)
    OP_8E(0xFE, 0xFFFFD634, 0x0, 0x15180, 0x2AF8, 0x0)
    OP_8E(0xFE, 0xFFFFE0C0, 0x0, 0x11A08, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFE7C8, 0x0, 0x10CC0, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFEC14, 0x0, 0xFBF4, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFE7C8, 0x0, 0xE54C, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFDF30, 0x0, 0xC670, 0x2EE0, 0x0)
    Return()

    # Function_4_1CD5 end

    def Function_5_1D76(): pass

    label("Function_5_1D76")

    OP_8E(0xFE, 0x0, 0x0, 0x20850, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFDF30, 0x0, 0x186A0, 0x32C8, 0x0)
    OP_8E(0xFE, 0xFFFFD634, 0x0, 0x15180, 0x36B0, 0x0)
    OP_8E(0xFE, 0xFFFFE0C0, 0x0, 0x11A08, 0x3A98, 0x0)
    OP_44(0x8, 0x2)
    OP_44(0x8, 0x3)
    SetChrFlags(0xFE, 0x4)
    OP_96(0xFE, 0xFFFFE0C0, 0x5DC, 0x10360, 0x7D0, 0x1F40)

    def lambda_1DF0():
        OP_6D(-7300, 0, 56400, 600)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1DF0)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 2)

    def lambda_1E12():
        OP_99(0xA, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1E12)

    def lambda_1E22():
        OP_6C(24000, 800)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1E22)
    OP_96(0xFE, 0xFFFFE37C, 0x0, 0xDC50, 0x7D0, 0x1F40)
    PlayEffect(0x12, 0xFF, 0xFF, -6800, -1000, 55400, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0x9, 0xA, 0)

    def lambda_1EA5():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1EA5)

    def lambda_1EBB():
        OP_96(0xFE, 0xFFFFEA84, 0x0, 0xD5AC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1EBB)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0xA, 400)

    def lambda_1EE5():
        OP_94(0x1, 0xFE, 0xB4, 0x12C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1EE5)
    WaitChrThread(0x8, 0x1)

    def lambda_1F00():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F00)
    OP_6A(0x0)
    ClearMapFlags(0x1)
    Return()

    # Function_5_1D76 end

    def Function_6_1F19(): pass

    label("Function_6_1F19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F6C")
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xC, 0x0)
    OP_48()
    Jump("Function_6_1F19")

    label("loc_1F6C")

    Return()

    # Function_6_1F19 end

    def Function_7_1F6D(): pass

    label("Function_7_1F6D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　卢安市\x01",
            "南　艾尔·雷登　１７５塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_1F6D end

    def Function_8_1FCA(): pass

    label("Function_8_1FCA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x287, 1)"), scpexpr(EXPR_END)), "loc_2042")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "死之刃２\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4C3)
    Jump("loc_20BC")

    label("loc_2042")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "死之刃２\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "死之刃２\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_20BC")

    Jump("loc_2114")

    label("loc_20BF")

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
    OP_83(0xF, 0x8C)

    label("loc_2114")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1FCA end

    SaveToFile()

Try(main)
