from ED6ScenarioHelper import *

def main():
    # 拉文努山道

    CreateScenaFile(
        FileName            = 'R1500   ._SN',
        MapName             = 'Bose',
        Location            = 'R1500.x',
        MapIndex            = 59,
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
        '红发的青年',                           # 9
        '拉文努村',                             # 10
        '西柏斯街道方向',                       # 11
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
        Unknown_3A              = 59,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT06/CH20053 ._CH',             # 00
        'ED6_DT09/CH10030 ._CH',             # 01
        'ED6_DT09/CH10031 ._CH',             # 02
        'ED6_DT09/CH10330 ._CH',             # 03
        'ED6_DT09/CH10331 ._CH',             # 04
        'ED6_DT09/CH10310 ._CH',             # 05
        'ED6_DT09/CH10310 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT06/CH20053P._CP',             # 00
        'ED6_DT09/CH10030P._CP',             # 01
        'ED6_DT09/CH10031P._CP',             # 02
        'ED6_DT09/CH10330P._CP',             # 03
        'ED6_DT09/CH10331P._CP',             # 04
        'ED6_DT09/CH10310P._CP',             # 05
        'ED6_DT09/CH10310P._CP',             # 06
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
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
        X                   = -170710,
        Z                   = 12010,
        Y                   = 95390,
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
        X                   = -204960,
        Z                   = -100,
        Y                   = -46530,
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
        X                   = -191470,
        Z                   = 3990,
        Y                   = 18830,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -180300,
        Z                   = 3990,
        Y                   = -3330,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -166330,
        Z                   = 11950,
        Y                   = 8590,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -210250,
        Y                   = -5000,
        Z                   = -8632,
        Range               = -197450,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFFD3FA,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_1B6",          # 00, 0
        "Function_1_1B7",          # 01, 1
        "Function_2_1CA",          # 02, 2
        "Function_3_1E0",          # 03, 3
    )


    def Function_0_1B6(): pass

    label("Function_0_1B6")

    Return()

    # Function_0_1B6 end

    def Function_1_1B7(): pass

    label("Function_1_1B7")

    OP_16(0x2, 0xFA0, 0xFFFB6C20, 0xFFFE6DA8, 0x3001F)
    Return()

    # Function_1_1B7 end

    def Function_2_1CA(): pass

    label("Function_2_1CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1CA")

    label("loc_1DF")

    Return()

    # Function_2_1CA end

    def Function_3_1E0(): pass

    label("Function_3_1E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1282")
    OP_A2(0x319)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x0, 0x8, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -192020, 3600, 10030, 223)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_250")

    ChrTalk(
        0x101,
        "#004F那是……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_28F")

    label("loc_250")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271")

    ChrTalk(
        0x102,
        "#014F哎……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_28F")

    label("loc_271")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28F")

    ChrTalk(
        0x103,
        "#023F哎呀……？\x02",
    )

    CloseMessageWindow()

    label("loc_28F")


    def lambda_295():
        OP_6D(-197690, 1800, 1790, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_295)

    def lambda_2AD():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2AD)
    Sleep(500)

    def lambda_2C2():
        OP_8E(0xFE, 0xFFFCFF9A, 0x802, 0xB40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C2)
    Sleep(2000)
    WaitChrThread(0x8, 0x1)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(
        0x8,
        "红发的青年",
        "#052F哦……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x103, -205000, 1920, -8810, 22)
    SetChrPos(0x101, -205000, 1920, -8810, 22)
    SetChrPos(0x102, -205000, 1920, -8810, 22)

    def lambda_355():
        OP_8E(0xFE, 0xFFFCFB62, 0x802, 0xFFFFFF88, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_355)
    Sleep(500)

    def lambda_375():
        OP_8E(0xFE, 0xFFFCF3EC, 0x79E, 0xFFFFFFD8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_375)
    Sleep(500)

    def lambda_395():
        OP_8E(0xFE, 0xFFFCF3A6, 0x7D9, 0xFFFFF920, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_395)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 0, 0)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 45, 0)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 0, 0)

    NpcTalk(
        0x8,
        "红发的青年",
        (
            "#050F是雪拉扎德啊。\x01",
            "没想到竟然在这里见到你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F那正是我要说的台词。\x02\x03",
            "本来以为你在王都呢。\x01",
            "你也是来调查这个事件的吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "红发的青年",
        (
            "#053F不，只是些琐事而已。\x02\x03",
            "#050F对了，\x01",
            "据说这个事件是空贼干的好事。\x02\x03",
            "既然你也来到这里，\x01",
            "那我就安心交给你了。\x02\x03",
            "要好好努力哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F什么呀，你也太无情了吧。\x02\x03",
            "老师他可能被别人抓住了，\x01",
            "你也应该听说了吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "红发的青年",
        (
            "#052F#051F被抓住了？\x01",
            "那个卡西乌斯·布莱特吗？\x02\x03",
            "哈哈哈，别开玩笑了！\x02\x03",
            "那个战无不胜的大叔\x01",
            "怎么可能给那帮空贼占上风！\x02\x03",
            "肯定是哪里搞错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#025F虽然我也是这么想的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F（这家伙是干什么的……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（我也不知道……\x01",
            "　但肯定是游击士没错。）\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "红发的青年",
        (
            "#050F顺便问一下……\x01",
            "这两个小鬼是干什么的？\x02\x03",
            "看上去像是刚加入的新人嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F呵呵，听了可别吃惊哦。\x02\x03",
            "他们是卡西乌斯老师的孩子呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(
        0x8,
        "红发的青年",
        (
            "#052F这还真是让人惊讶……\x01",
            "是那个大叔的孩子啊。\x02\x03",
            "哼～这两个小鬼……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFCFA54, 0x7ED, 0x58C, 0x7D0, 0x0)

    NpcTalk(
        0x8,
        "红发的青年",
        "#057F#1P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F怎、怎么了？\x01",
            "盯着我们来回看个没完……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "红发的青年",
        (
            "#050F#1P黑发的小子暂且不论……\x01",
            "那边梳辫子的小丫头。\x02\x03",
            "#050F她真是大叔的女儿吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F她的确是如假包换的\x01",
            "卡西乌斯·布莱特的亲生女儿。\x02\x03",
            "我才是养子。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "红发的青年",
        (
            "#052F#1P哦～是吗？\x02\x03",
            "#053F算了，这种事情怎么样都无所谓。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F才、才不是怎么样都无所谓！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    NpcTalk(
        0x8,
        "红发的青年",
        (
            "#051F#1P那就再会了，雪拉扎德。\x02\x03",
            "不要让这两个小鬼拖了后腿，\x01",
            "总之多多保重吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F是是。\x02\x03",
            "你也要注意别冒失行动，\x01",
            "以免遭受沉重的打击。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "红发的青年",
        "#051F#1P哈哈，铭记在心。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E13")

    ChrTalk(
        0x8,
        (
            "#050F#1P对了，雪拉扎德。\x02\x03",
            "废坑那边被通缉的魔兽\x01",
            "是你除掉的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#1P对，没错。\x02\x03",
            "但是严格说来是『我们』才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#053F#1P哈哈，用新人来凑数\x01",
            "也是没有办法的事吧。\x02\x03",
            "#053F……………………\x02\x03",
            "#051F那么，就保持这个水准，\x01",
            "搜索空贼的行动也要加油哦！\x02\x03",
            "再见了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E13")


    def lambda_E19():

        label("loc_E19")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_E19")

    QueueWorkItem2(0x101, 2, lambda_E19)

    def lambda_E2A():

        label("loc_E2A")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_E2A")

    QueueWorkItem2(0x102, 2, lambda_E2A)

    def lambda_E3B():

        label("loc_E3B")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_E3B")

    QueueWorkItem2(0x103, 2, lambda_E3B)

    def lambda_E4C():
        OP_6D(-198470, 2000, 160, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4C)
    OP_8E(0x8, 0xFFFCF342, 0x7B2, 0x500, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFCEF28, 0x73A, 0xC8, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFCE9D8, 0x730, 0xFFFFDB20, 0xBB8, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)

    ChrTalk(
        0x101,
        (
            "#005F#1P那、那家伙是谁呀！？\x02\x03",
            "太过分了，\x01",
            "真是气死我了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x01",
            "刚才那个人是『重剑阿加特』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P『重剑阿加特』？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)

    ChrTalk(
        0x103,
        (
            "#020F阿加特·科洛斯纳。\x01",
            "游击士协会的正游击士。\x02\x03",
            "#020F没有特定的所属支部，\x01",
            "活动范围遍布全国各地。\x02\x03",
            "使用一把能将魔兽\x01",
            "一刀斩成两段的超重大剑……\x02\x03",
            "总而言之，就是相当的厉害呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        (
            "#009F哼，先不说厉不厉害，\x01",
            "是个没礼貌的家伙肯定没错。\x02\x03",
            "从刚才的谈话中看来，\x01",
            "那家伙也是老爸认识的人吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 45, 400)

    ChrTalk(
        0x102,
        (
            "#010F他虽然承认父亲的实力，\x01",
            "但好像感觉不出什么善意的态度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F以前发生了一些事情……\x02\x03",
            "所以和老师产生过冲突。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F哼……\x02\x03",
            "算了，怎样都无所谓啦。\x01",
            "那种没礼貌的家伙，我才不想管呢！\x02\x03",
            "我们赶快去拉文努村吧！\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_1282")

    Return()

    # Function_3_1E0 end

    SaveToFile()

Try(main)
