from ED6ScenarioHelper import *

def main():
    # 空贼要塞

    CreateScenaFile(
        FileName            = 'C1303   ._SN',
        MapName             = 'Bose',
        Location            = 'C1303.x',
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
        '乔丝特',                               # 9
        '吉尔',                                 # 10
        '多伦',                                 # 11
        '罐子',                                 # 12
        '\u3000T',                              # 13
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
        'ED6_DT07/CH00310 ._CH',             # 00
        'ED6_DT07/CH00300 ._CH',             # 01
        'ED6_DT07/CH00290 ._CH',             # 02
        'ED6_DT07/CH02130 ._CH',             # 03
        'ED6_DT07/CH02120 ._CH',             # 04
        'ED6_DT07/CH02110 ._CH',             # 05
        'ED6_DT07/CH00292 ._CH',             # 06
        'ED6_DT07/CH00100 ._CH',             # 07
        'ED6_DT07/CH00101 ._CH',             # 08
        'ED6_DT07/CH00110 ._CH',             # 09
        'ED6_DT07/CH00111 ._CH',             # 0A
        'ED6_DT07/CH00130 ._CH',             # 0B
        'ED6_DT07/CH00131 ._CH',             # 0C
        'ED6_DT07/CH00120 ._CH',             # 0D
        'ED6_DT07/CH00121 ._CH',             # 0E
        'ED6_DT07/CH00314 ._CH',             # 0F
        'ED6_DT07/CH00304 ._CH',             # 10
        'ED6_DT07/CH00294 ._CH',             # 11
        'ED6_DT07/CH00311 ._CH',             # 12
        'ED6_DT07/CH00301 ._CH',             # 13
        'ED6_DT07/CH00291 ._CH',             # 14
        'ED6_DT07/CH00305 ._CH',             # 15
        'ED6_DT06/CH20065 ._CH',             # 16
        'ED6_DT06/CH20066 ._CH',             # 17
        'ED6_DT06/CH20067 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH00310P._CP',             # 00
        'ED6_DT07/CH00300P._CP',             # 01
        'ED6_DT07/CH00290P._CP',             # 02
        'ED6_DT07/CH02130P._CP',             # 03
        'ED6_DT07/CH02120P._CP',             # 04
        'ED6_DT07/CH02110P._CP',             # 05
        'ED6_DT07/CH00292P._CP',             # 06
        'ED6_DT07/CH00100P._CP',             # 07
        'ED6_DT07/CH00101P._CP',             # 08
        'ED6_DT07/CH00110P._CP',             # 09
        'ED6_DT07/CH00111P._CP',             # 0A
        'ED6_DT07/CH00130P._CP',             # 0B
        'ED6_DT07/CH00131P._CP',             # 0C
        'ED6_DT07/CH00120P._CP',             # 0D
        'ED6_DT07/CH00121P._CP',             # 0E
        'ED6_DT07/CH00314P._CP',             # 0F
        'ED6_DT07/CH00304P._CP',             # 10
        'ED6_DT07/CH00294P._CP',             # 11
        'ED6_DT07/CH00311P._CP',             # 12
        'ED6_DT07/CH00301P._CP',             # 13
        'ED6_DT07/CH00291P._CP',             # 14
        'ED6_DT07/CH00305P._CP',             # 15
        'ED6_DT06/CH20065P._CP',             # 16
        'ED6_DT06/CH20066P._CP',             # 17
        'ED6_DT06/CH20067P._CP',             # 18
    )

    DeclNpc(
        X                   = -36460,
        Z                   = 0,
        Y                   = -82960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35810,
        Z                   = 0,
        Y                   = -83940,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -34100,
        Z                   = 0,
        Y                   = -82100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -34310,
        Z                   = 1000,
        Y                   = -83180,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 1000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -22008,
        Y                   = -3000,
        Z                   = -168710,
        Range               = -26065,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFD625F,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = -36040,
        TriggerZ            = 0,
        TriggerY            = -121030,
        TriggerRange        = 800,
        ActorX              = -36040,
        ActorZ              = 1000,
        ActorY              = -121030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -75460,
        TriggerZ            = 0,
        TriggerY            = -119560,
        TriggerRange        = 1000,
        ActorX              = -75450,
        ActorZ              = 1500,
        ActorY              = -118890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_27A",          # 00, 0
        "Function_1_27B",          # 01, 1
        "Function_2_2C5",          # 02, 2
        "Function_3_2DB",          # 03, 3
        "Function_4_280D",         # 04, 4
        "Function_5_2866",         # 05, 5
        "Function_6_28AC",         # 06, 6
        "Function_7_28D7",         # 07, 7
        "Function_8_28FD",         # 08, 8
        "Function_9_2A79",         # 09, 9
    )


    def Function_0_27A(): pass

    label("Function_0_27A")

    Return()

    # Function_0_27A end

    def Function_1_27B(): pass

    label("Function_1_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D")
    OP_6F(0x2, 0)
    Jump("loc_294")

    label("loc_28D")

    OP_6F(0x2, 60)

    label("loc_294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB")
    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    Jump("loc_2AF")

    label("loc_2AB")

    OP_64(0x0, 0x1)

    label("loc_2AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x389), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C4")

    Return()

    # Function_1_27B end

    def Function_2_2C5(): pass

    label("Function_2_2C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2C5")

    label("loc_2DA")

    Return()

    # Function_2_2C5 end

    def Function_3_2DB(): pass

    label("Function_3_2DB")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有熟悉的声音传出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#002F这里是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯……\x01",
            "这里应该就是首领的房间了。\x02",
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
            "【看准机会冲进去】\x01",      # 0
            "【还是算了】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3EE"),
        (0, "loc_3F3"),
        (SWITCH_DEFAULT, "loc_280C"),
    )


    label("loc_3EE")

    EventEnd(0x1)
    Jump("loc_280C")

    label("loc_3F3")

    OP_20(0x5DC)
    Fade(1000)
    OP_6D(-34780, 0, -82570, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, -34290, 500, -83750, 45)
    SetMapFlags(0x400000)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x2)
    SetChrSubChip(0xB, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0x9, 0xA, 0)
    OP_8C(0xA, 225, 0)
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_21()
    OP_1D(0x57)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#193F哼哼哼……\x01",
            "女王打算出赎金了吗？\x02\x03",
            "这下总算和贫穷的生活说再见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#200F大哥，现在还不能大意。\x01",
            "拿到赎金之后才能完全放心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#211F嗯嗯，要不我们先\x01",
            "计划一下怎么释放人质吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#193F释放人质？\x02\x03",
            "喂喂，\x01",
            "为啥我们非要干\x01",
            "那么拖泥带水的事不可呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#213F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#193F米拉到手后\x01",
            "把他们杀光不就了事了嘛。\x02\x03",
            "没必要留活口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#216F多、多伦大哥……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#201F你、你在开玩笑吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#193F那些人质肯定\x01",
            "记得我们的样子。\x02\x03",
            "就算我们逃出了利贝尔，\x01",
            "也难保日后没有后顾之忧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#214F但、但人质里面\x01",
            "还有老人和小孩子啊。\x02\x03",
            "你真的打算杀了他们吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#193F哼！混了这么久，\x01",
            "你们的思维还是这么单纯。\x02\x03",
            "我们可不是在玩过家家！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#215F怎、怎么会……我……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#203F大哥……\x01",
            "不好意思，我反对这样做。\x02\x03",
            "要是真的这样做的话，\x01",
            "空之女神也不会原谅我们的。\x02\x03",
            "#200F而且……\x01",
            "我也不想把染血的米拉带回故乡啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#193F……………………………………\x02\x03",
            "吉尔，你小子……\x01",
            "啥时候变得这么伟大了呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#200F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#195F少给我说废话！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)
    SetChrChipByIndex(0xA, 22)
    SetChrSubChip(0xA, 0)
    Sleep(150)
    TurnDirection(0xA, 0x9, 0)
    SetChrChipByIndex(0xB, 23)

    def lambda_9DD():

        label("loc_9DD")

        OP_99(0xFE, 0x0, 0x7, 0x6A4)
        OP_48()
        Jump("loc_9DD")

    QueueWorkItem2(0xB, 1, lambda_9DD)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x80)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0xA, 1)
    Sleep(150)
    SetChrSubChip(0xA, 2)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -34270, 980, -81780, 225)
    OP_96(0xB, 0xFFFF73C4, 0x190, 0xFFFEB902, 0x3E8, 0x1770)

    def lambda_A3B():
        OP_95(0xB, 0x0, 0xFFFFFC18, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_A3B)

    def lambda_A59():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A59)
    OP_22(0x22B, 0x0, 0x64)
    OP_22(0xF8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x32)
    OP_44(0x9, 0xFF)
    OP_96(0x9, 0xFFFF704A, 0x0, 0xFFFEB3F8, 0x1F4, 0x1388)
    SetChrChipByIndex(0x9, 16)
    SetChrSubChip(0x9, 3)
    SetChrChipByIndex(0xA, 5)

    ChrTalk(
        0x9,
        "#205F啊啊！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x80)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        "#216F吉尔哥！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    OP_92(0x8, 0x9, 0x2BC, 0xBB8, 0x0)

    ChrTalk(
        0xA,
        (
            "#194F嘎哈哈，什么故乡呀！\x02\x03",
            "好不容易才得到那么一大笔钱，\x01",
            "难道你还打算浪费掉，\x01",
            "去买回那种不值钱的土地吗！？\x02\x03",
            "哈，我可是决定要去\x01",
            "南方的度假别墅享受一番。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#201F什么……可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#193F要是米拉花完了，\x01",
            "再干一票抢夺定期船的买卖不就搞定了。\x02\x03",
            "这就是今后\x01",
            "『卡普亚空贼团』要干的大事呀。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0xA,
        "#194F#5S嘎哇～哈哈哈！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(
        0x8,
        (
            "#215F多伦大哥……\x01",
            "你真的要那样……？\x02\x03",
            "#214F难道你真的要那样做吗！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 7)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0x101, -35150, 0, -91730, 0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#1P在这种时候突然插话\x01",
            "真不好意思呢……\x02\x03",
            "兄妹吵架可以放到以后吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_E03():
        OP_6D(-34550, 0, -85900, 1500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_E03)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0x104, 11)
    SetChrChipByIndex(0x103, 13)

    def lambda_E2A():
        OP_8C(0xA, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E2A)

    def lambda_E38():
        OP_8C(0x8, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E38)
    ClearChrFlags(0x101, 0x80)

    def lambda_E4B():
        OP_8E(0xFE, 0xFFFF768A, 0x0, 0xFFFEA9B2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4B)
    Sleep(200)
    SetChrPos(0x103, -35150, 0, -91730, 0)

    def lambda_E7C():
        OP_8E(0xFE, 0xFFFF7B4E, 0x0, 0xFFFEA886, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E7C)
    Sleep(200)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -35150, 0, -91730, 0)

    def lambda_EB2():
        OP_8E(0xFE, 0xFFFF7112, 0x0, 0xFFFEA750, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EB2)
    Sleep(200)
    SetChrPos(0x104, -35150, 0, -91730, 0)

    def lambda_EE3():
        OP_8E(0xFE, 0xFFFF7644, 0x0, 0xFFFEA412, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EE3)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x103, 0x1)
    ClearChrFlags(0x102, 0x4)

    ChrTalk(
        0x8,
        "#213F你、你们！？\x02",
    )

    CloseMessageWindow()
    OP_96(0x9, 0xFFFF6D02, 0x0, 0xFFFEB434, 0x12C, 0xBB8)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)

    def lambda_F50():
        OP_8C(0x9, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F50)

    ChrTalk(
        0x9,
        (
            "#201F游击士！\x02\x03",
            "怎、怎么会在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F呵呵……\x01",
            "别说如此薄情的话嘛。\x02\x03",
            "不正是你们用那艘飞艇\x01",
            "将我们送过来的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#201F混、混帐……\x01",
            "你在开什么玩笑……\x02\x03",
            "…………难道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F你们不记得\x01",
            "在琥珀之塔前面停过飞艇吗？\x02\x03",
            "我们趁着空隙\x01",
            "巧妙地藏到了船舱里。\x02\x03",
            "#001F也就是偷渡啦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#214F很、很厉害嘛！\x01",
            "你这个没大脑的女人。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#509F谁、谁没大脑！\x02\x03",
            "你这个傲慢的男人婆！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#214F你、你说什么～！？\x02\x03",
            "单纯女！暴力女！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F你、你竟敢这么说～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F好了好了。\x01",
            "求你们别再吵了。\x02\x03",
            "#012F……人质已经被释放了，\x01",
            "其他的空贼成员也都被打倒了。\x02\x03",
            "现在只剩下你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F基于游击士协会的规定，\x01",
            "现以协会的名义将你们逮捕归案。\x02\x03",
            "劝你们放弃无谓的抵抗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#201F唔唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#212F混蛋……\x02",
    )

    CloseMessageWindow()

    def lambda_13B9():
        OP_6D(-34330, 0, -83800, 1000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13B9)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#193F#5P吉尔，乔丝特……\x02\x03",
            "这到底是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#203F对、对不起，大哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#215F对不起……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#193F#5P哼，算了。\x01",
            "这次就先饶了你们。\x02\x03",
            "只要把这些家伙\x01",
            "通通杀光就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F你、你说什么！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#194F#5P嘎哈哈，愚蠢的家伙！\x02\x03",
            "就凭你们几个人\x01",
            "也想逮捕我多伦·卡普亚吗？\x01",
            "你们也想得太美了吧！！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x4)
    OP_96(0xA, 0xFFFF79C8, 0x3E8, 0xFFFEB9AC, 0x5DC, 0x1388)
    OP_22(0x8E, 0x0, 0x64)
    SetChrChipByIndex(0xA, 6)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)

    def lambda_1598():
        OP_6D(-34220, 0, -85300, 1000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1598)
    Sleep(1000)

    def lambda_15B5():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15B5)
    Sleep(200)
    OP_22(0x1FA, 0x0, 0x64)
    LoadEffect(0x2, "map\\\\mp019_00.eff")
    SetChrPos(0xC, -35030, 0, -87040, 0)
    PlayEffect(0x2, 0xFF, 0xA, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xC, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_162E():
        OP_96(0xFE, 0xFFFF72AC, 0x0, 0xFFFEA818, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_162E)

    def lambda_164C():
        OP_96(0xFE, 0xFFFF7A5E, 0x0, 0xFFFEA7FA, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_164C)

    def lambda_166A():
        OP_96(0xFE, 0xFFFF6E56, 0x0, 0xFFFEA386, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_166A)

    def lambda_1688():
        OP_96(0xFE, 0xFFFF7C5C, 0x0, 0xFFFEA2DC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1688)
    Sleep(500)
    LoadEffect(0x1, "map\\\\mp019_01.eff")
    PlayEffect(0x1, 0xFF, 0xFF, -35030, 0, -87040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6B(3100, 0)
    OP_6B(3000, 80)
    TurnDirection(0x103, 0xA, 0)
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0x102, 0x9, 0)
    TurnDirection(0x104, 0xA, 0)
    Sleep(600)

    ChrTalk(
        0x101,
        "#504F呀啊啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#016F轻型导力炮……！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 225, 0)

    ChrTalk(
        0xA,
        (
            "#195F#6P吉尔，乔丝特！\x01",
            "快点给我上！\x02\x03",
            "把这些家伙炸成炮灰！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 0)
    Sleep(100)
    SetChrChipByIndex(0x8, 18)
    Sleep(100)
    SetChrChipByIndex(0x9, 19)
    Sleep(500)
    SetChrChipByIndex(0xA, 20)
    SetChrSubChip(0xA, 0)

    def lambda_1804():
        OP_96(0xFE, 0xFFFF768A, 0x0, 0xFFFEAC5A, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1804)
    Sleep(100)

    def lambda_1827():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1827)
    Sleep(100)

    def lambda_1841():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1841)
    Sleep(200)
    Battle(0x389, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_186E"),
        (SWITCH_DEFAULT, "loc_1871"),
    )


    label("loc_186E")

    OP_B4(0x0)
    Return()

    label("loc_1871")

    EventBegin(0x0)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrChipByIndex(0x8, 3)
    SetChrChipByIndex(0x9, 4)
    SetChrChipByIndex(0xA, 17)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, -36430, 0, -82700, 225)
    SetChrPos(0x9, -38890, 0, -82380, 135)
    SetChrPos(0xA, -37360, 0, -81500, 180)
    SetChrPos(0x101, -38990, 0, -84930, 0)
    SetChrPos(0x102, -38900, 0, -86070, 0)
    SetChrPos(0x104, -37640, 0, -86250, 0)
    SetChrPos(0x103, -37780, 0, -84870, 0)
    OP_6D(-37600, 0, -82870, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#203F太、太强了……\x02\x03",
            "这就是游击士的实力吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#215F可、可恶～……\x01",
            "竟然输给了这个女人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F哼哼，这是当然的啦㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F好了，胜负已分。\x01",
            "你们老老实实地投降吧。\x02\x03",
            "#021F要是再敢抵抗的话，\x01",
            "……后果你应该很明白的吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "雪拉扎德一边抽着鞭子一边向乔丝特微笑。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#216F呀……\x01",
            "不要，饶了我吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#203F呜呜……\x01",
            "大势已去了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "………唔……………\x02",
    )

    CloseMessageWindow()
    OP_6D(-37530, 0, -82040, 1000)
    OP_99(0xA, 0x3, 0x0, 0x258)

    ChrTalk(
        0xA,
        (
            "#197F痛痛痛……\x01",
            "到底怎么回事。\x02\x03",
            "身体到处都在疼……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0xA, 5)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#192F我怎么……\x01",
            "拿着这个导力炮啊？\x02\x03",
            "…………咦？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 400)

    ChrTalk(
        0x9,
        "#201F大哥？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(
        0x8,
        "#212F多伦大哥？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#191F哦哦，乔丝特！\x01",
            "从洛连特回来了吗？\x02\x03",
            "这么快就回来了，\x01",
            "果然还是失手了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#213F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#191F嘎哈哈，别想骗我了。\x02\x03",
            "算了，只要你能接受教训就行了。\x01",
            "以后这些要蛮力的差事还是交给我们吧。\x02\x03",
            "虽然这样赚得少点，\x01",
            "不过只要慢慢积累就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#216F多、多伦大哥，你在说什么呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#201F大哥，振作点！\x02\x03",
            "乔丝特她老早\x01",
            "就从洛连特回来了。\x02\x03",
            "袭击了定期船后，\x01",
            "我不是还去迎接过你吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#192F啥？\x01",
            "袭击定期船？\x02\x03",
            "老弟你在说什么梦话呀？\x02\x03",
            "那么危险的事，\x01",
            "只有白痴才会去做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#201F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#213F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F（这家伙在说什么呢？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（嗯……\x01",
            "　不像是故意开脱罪行的样子……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#190F刚才就注意到了，\x01",
            "这些奇怪的家伙是谁啊？\x02\x03",
            "难道是新来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F很遗憾不是。\x02\x03",
            "我们是游击士协会的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#192F#5S啥！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#192F为、为啥\x01",
            "游击士会在这里的啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F这么说……\x01",
            "他好像突然失忆了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哈·哈·哈。\x01",
            "看来剧情变得越来越有趣了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F就算你突然失忆了，\x01",
            "我们也还是要将你逮捕归案。\x02\x03",
            "抢夺定期船、监禁人质、\x01",
            "要求赎金等案件都是既定的嫌疑。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2300, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#192F抢夺定期船……\x01",
            "监禁人质……要求赎金！？\x02\x03",
            "吉尔！乔丝特！\x01",
            "这、这开的是啥玩笑呀！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#215F多伦大哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#204F我们也想知道是怎么回事啊……\x02\x03",
            "#201F不过，多亏了大哥，\x01",
            "……这下有机会了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 21)
    OP_8C(0x9, 180, 400)
    Sleep(200)
    OP_99(0x9, 0x4, 0x5, 0x320)
    LoadEffect(0x0, "map\\\\mp004_00.eff")
    SetChrPos(0xC, -38180, -3000, -85370, 0)
    PlayEffect(0x0, 0xFF, 0x9, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0xC, 0, 0, 0, 0)
    SetChrChipByIndex(0x9, 1)
    Sleep(1300)
    OP_22(0x7F, 0x0, 0x64)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    SetChrPos(0x9, -35240, 0, -89190, 0)
    SetChrPos(0x8, -35240, 0, -89190, 0)
    SetChrPos(0xA, -35240, 0, -89190, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)

    ChrTalk(
        0x101,
        "#004F#1P啊啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#024F#1P糟了！\x01",
            "又是这招……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#192F喂、喂……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#213F吉尔哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#201F有话以后再说吧！\x01",
            "现在还是先逃为妙！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#034F#5P咳咳……\x02\x03",
            "呛、呛到烟了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#016F#5P赶快离开这个房间！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_6D(-35986, 0, -121600, 0)
    OP_6F(0x0, 20)
    Sleep(500)
    FadeToBright(1000, 16777215)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x4)
    OP_43(0x102, 0x1, 0x0, 0x5)
    OP_43(0x103, 0x1, 0x0, 0x6)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#005F那些家伙～\x01",
            "跑到哪里去了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#016F在上面……\x01",
            "他们打算坐空贼飞艇逃走。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        "#580F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#024F#5P现在追还来得及，\x01",
            "绝对不能再让他们逃掉！\x02\x03",
            "全力追击！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#002F嗯！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        "#012F明白了！\x02",
    )

    CloseMessageWindow()
    OP_43(0x104, 0x1, 0x0, 0x7)
    WaitChrThread(0x104, 0x1)

    ChrTalk(
        0x104,
        (
            "#034F咳咳……救、救命……\x02\x03",
            "啊，真是悲剧！\x01",
            "我精致完美的鼻腔啊……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2713():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2713)

    def lambda_2721():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2721)
    TurnDirection(0x101, 0x104, 400)
    WaitChrThread(0x103, 0x1)

    ChrTalk(
        0x101,
        (
            "#005F喂，奥利维尔！\x01",
            "再不快点就丢下你了！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x104,
        (
            "#036F哇哇……\x01",
            "等、等一下嘛！\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x5DC)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27E1")
    OP_8E(0x104, 0xFFFF7360, 0x0, 0xFFFE22BC, 0xBB8, 0x0)

    label("loc_27E1")

    OP_A2(0x358)
    OP_28(0x39, 0x1, 0x40)
    OP_28(0x39, 0x1, 0x80)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    OP_70(0x0, 0x0)
    OP_71(0x0, 0x10)
    OP_64(0x0, 0x1)
    OP_21()
    OP_1E()
    Jump("loc_280C")

    label("loc_280C")

    Return()

    # Function_3_2DB end

    def Function_4_280D(): pass

    label("Function_4_280D")

    SetChrPos(0xFE, -36050, 0, -119700, 0)
    OP_8E(0xFE, 0xFFFF7266, 0x0, 0xFFFE21F4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF6EB0, 0x0, 0xFFFE1C72, 0x1388, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(200)
    OP_8C(0xFE, 265, 400)
    Sleep(200)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_280D end

    def Function_5_2866(): pass

    label("Function_5_2866")

    Sleep(800)
    SetChrPos(0xFE, -36050, 0, -119700, 0)
    OP_8E(0xFE, 0xFFFF7266, 0x0, 0xFFFE21F4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF7586, 0x0, 0xFFFE1DBC, 0x1388, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_2866 end

    def Function_6_28AC(): pass

    label("Function_6_28AC")

    Sleep(1600)
    SetChrPos(0xFE, -36050, 0, -119700, 0)
    OP_8E(0xFE, 0xFFFF7266, 0x0, 0xFFFE21F4, 0x1388, 0x0)
    Return()

    # Function_6_28AC end

    def Function_7_28D7(): pass

    label("Function_7_28D7")

    SetChrPos(0xFE, -36050, 0, -119700, 0)
    OP_8E(0xFE, 0xFFFF7388, 0x0, 0xFFFE27A8, 0x7D0, 0x0)
    Return()

    # Function_7_28D7 end

    def Function_8_28FD(): pass

    label("Function_8_28FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A78")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "道路的尽头是一面岩壁。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#505F这里不能走了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F不……\x01",
            "前面好像有什么。\x02\x03",
            "试着推推看吧？\x02",
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
            "【推岩壁】\x01",      # 0
            "【不推】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A4B"),
        (1, "loc_2A5A"),
        (SWITCH_DEFAULT, "loc_2A78"),
    )


    label("loc_2A4B")

    OP_A2(0x3FB)
    NewScene("ED6_DT01/C1401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2A78")

    label("loc_2A5A")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_2A78")

    label("loc_2A78")

    Return()

    # Function_8_28FD end

    def Function_9_2A79(): pass

    label("Function_9_2A79")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B74")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_2AF3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "复苏药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x384)
    Jump("loc_2B71")

    label("loc_2AF3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "复苏药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "复苏药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_2B71")

    Jump("loc_2BF6")

    label("loc_2B74")

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
    OP_83(0xF, 0xF)

    label("loc_2BF6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_2A79 end

    SaveToFile()

Try(main)
