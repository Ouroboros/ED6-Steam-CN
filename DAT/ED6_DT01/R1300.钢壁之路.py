from ED6ScenarioHelper import *

def main():
    # 钢壁之路

    CreateScenaFile(
        FileName            = 'R1300   ._SN',
        MapName             = 'Bose',
        Location            = 'R1300.x',
        MapIndex            = 57,
        MapDefaultBGM       = "ed60022",
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
        '王国军士兵',                           # 9
        '王国军士兵',                           # 10
        '东柏斯街道方向',                       # 11
        '哈肯大门方向',                         # 12
    )

    DeclEntryPoint(
        Unknown_00              = -207000,
        Unknown_04              = 0,
        Unknown_08              = -154000,
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
        Unknown_30              = 312,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 57,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT09/CH10370 ._CH',             # 01
        'ED6_DT09/CH10371 ._CH',             # 02
        'ED6_DT09/CH10360 ._CH',             # 03
        'ED6_DT09/CH10361 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT09/CH10370P._CP',             # 01
        'ED6_DT09/CH10371P._CP',             # 02
        'ED6_DT09/CH10360P._CP',             # 03
        'ED6_DT09/CH10361P._CP',             # 04
    )

    DeclNpc(
        X                   = -209600,
        Z                   = 20,
        Y                   = -150000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -206360,
        Z                   = 10,
        Y                   = -150000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -207930,
        Z                   = -20,
        Y                   = -167750,
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
        X                   = -204120,
        Z                   = -200,
        Y                   = 1430,
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
        X                   = -218580,
        Z                   = -40,
        Y                   = -112680,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x107,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -226560,
        Z                   = -30,
        Y                   = -88140,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x108,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -200780,
        Z                   = -20,
        Y                   = -50350,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x108,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -194620,
        Z                   = -30,
        Y                   = -34740,
        Unknown_0C          = 0,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x10B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -211700,
        Y                   = -2000,
        Z                   = -151630,
        Range               = -202854,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFDAA58,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_1F4",          # 01, 1
        "Function_2_218",          # 02, 2
        "Function_3_22E",          # 03, 3
        "Function_4_2A1",          # 04, 4
        "Function_5_321",          # 05, 5
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1F3")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_1F3")

    Return()

    # Function_0_1E2 end

    def Function_1_1F4(): pass

    label("Function_1_1F4")

    OP_16(0x2, 0xFA0, 0xFFFADF80, 0xFFFCCBB0, 0x30013)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_217")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)

    label("loc_217")

    Return()

    # Function_1_1F4 end

    def Function_2_218(): pass

    label("Function_2_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_218")

    label("loc_22D")

    Return()

    # Function_2_218 end

    def Function_3_22E(): pass

    label("Function_3_22E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "既然是市长的委托，那就没办法了。\x01",
            "办事要快一点。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_3_22E end

    def Function_4_2A1(): pass

    label("Function_4_2A1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哈肯门是与帝国接壤的国境。\x01",
            "千万不要引起麻烦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_2A1 end

    def Function_5_321(): pass

    label("Function_5_321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_32B")
    Jump("loc_E55")

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_8C9")
    EventBegin(0x0)
    OP_4A(0x8, 0)
    OP_4A(0x9, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0x9, 0x101, 400)
    OP_A2(0x30C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C")

    ChrTalk(
        0x8,
        "站住。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "前面是哈肯大门方向，\x01",
            "现在禁止通行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "任何无关人员一律禁止通行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F非常遗憾，我们就是相关人员。\x02",
    )

    CloseMessageWindow()
    Jump("loc_521")

    label("loc_48C")


    ChrTalk(
        0x8,
        "哦，你们是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "我记得是游击士协会的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嘿嘿，真遗憾。\x02\x03",
            "现在的我们是作为\x01",
            "柏斯市长的使者来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_521")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出示了梅贝尔市长的信件。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        "这个是，梅贝尔市长的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们受市长的委托，\x01",
            "来向摩尔根将军了解搜索情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F顺便说一下，这是正式的委托书。\x02\x03",
            "如果不让我们通过的话，\x01",
            "将来有什么后果恐怕你们担当不起哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哎呀，这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "没办法，让他们通过吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        "喂，这样好吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        (
            "说起梅贝尔市长，\x01",
            "不就是柏斯地区的总负责人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那可是不能小觑的人物啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "确实如此……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 400)

    ChrTalk(
        0x9,
        "……喂，你们几个。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x9,
        (
            "可以让你们通过，\x01",
            "不过千万不要引起麻烦哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "现在可是非常时期，而且不管怎么说，\x01",
            "那里毕竟是和帝国接壤的边境。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F好的好的，我们知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F那么，我们过去吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_4B(0x8, 0)
    OP_8C(0x9, 180, 400)
    OP_4B(0x9, 0)
    EventEnd(0x1)
    Jump("loc_E55")

    label("loc_8C9")

    EventBegin(0x0)

    def lambda_8D1():
        OP_6D(-207880, 40, -151960, 1000)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8D1)
    OP_4A(0x8, 0)
    OP_4A(0x9, 0)
    OP_8B(0x0, 0xFFFCD3F8, 0xFFFDAE68, 0x0)
    OP_8B(0x1, 0xFFFCD3F8, 0xFFFDAE68, 0x0)
    OP_8B(0x2, 0xFFFCD3F8, 0xFFFDAE68, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D92")
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 400)
    TurnDirection(0x9, 0x0, 400)
    OP_A2(0x306)

    ChrTalk(
        0x8,
        "站住。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "前面是哈肯大门方向，\x01",
            "现在禁止通行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "任何无关人员一律禁止通行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F什么呀，真小气～\x01",
            "稍微看看又没什么关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "我说，这可不是闹着玩的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "现在，国境师团正在集结军力\x01",
            "搜索行踪不明的定期船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "麻烦你们不要妨碍我们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F我们根本没有妨碍你们的意思。\x02\x03",
            "我们是游击士，\x01",
            "即使这样也不能让我们通过？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "游击士？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "姑且不说你是不是……\x01",
            "难道这两个少年也是游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F嘿嘿，我们就是啊☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F这是我们的游击士徽章。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这、这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是，就算是游击士也毫不例外，\x01",
            "一律禁止通行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "对对。\x01",
            "你们马上离开吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哼～\x01",
            "真是不可理喻呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没办法了，艾丝蒂尔。\x02\x03",
            "我们还是先去柏斯吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E24")

    label("loc_D92")

    TurnDirection(0x8, 0x0, 400)
    TurnDirection(0x9, 0x0, 400)

    ChrTalk(
        0x9,
        "我说了不行就是不行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "想来的话过一阵子再来吧。\x02",
    )

    CloseMessageWindow()

    label("loc_E24")

    OP_90(0x0, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    OP_8C(0x8, 180, 0)
    OP_4B(0x8, 0)
    OP_8C(0x9, 180, 0)
    OP_4B(0x9, 0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_E55")

    Return()

    # Function_5_321 end

    SaveToFile()

Try(main)
