from ED6ScenarioHelper import *

def main():
    # 格鲁纳门

    CreateScenaFile(
        FileName            = 'T0600   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0600.x',
        MapIndex            = 17,
        MapDefaultBGM       = "ed60016",
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
        '士兵舒托尔',                           # 9
        '士兵巴兰克',                           # 10
        '士兵托马斯',                           # 11
        '士兵亚多罗瓦',                         # 12
        '士兵洛克思',                           # 13
        '艾利兹街道方向',                       # 14
        '庭园大道方向',                         # 15
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
        Unknown_3A              = 17,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
    )

    DeclNpc(
        X                   = -35300,
        Z                   = 0,
        Y                   = 3650,
        Direction           = 261,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -35300,
        Z                   = 0,
        Y                   = -3560,
        Direction           = 265,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -21590,
        Z                   = 11750,
        Y                   = 150,
        Direction           = 101,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -10690,
        Z                   = 0,
        Y                   = -3640,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -10660,
        Z                   = 0,
        Y                   = 3600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 37180,
        Z                   = 0,
        Y                   = -1450,
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
        X                   = -83430,
        Z                   = 0,
        Y                   = -1170,
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


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1A3",          # 01, 1
        "Function_2_216",          # 02, 2
        "Function_3_22C",          # 03, 3
        "Function_4_250",          # 04, 4
        "Function_5_DE1",          # 05, 5
        "Function_6_11CE",         # 06, 6
        "Function_7_178A",         # 07, 7
        "Function_8_1D18",         # 08, 8
        "Function_9_20DF",         # 09, 9
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Return()

    # Function_0_1A2 end

    def Function_1_1A3(): pass

    label("Function_1_1A3")

    OP_16(0x2, 0xFA0, 0xFFFDB610, 0xFFFE0430, 0x30006)
    OP_6F(0x0, 160)
    OP_6F(0x1, 160)
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_1C(0x2, 0x0, 0x9)
    OP_1C(0x3, 0x0, 0x9)
    OP_1C(0x4, 0x0, 0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1E6")
    Jump("loc_215")

    label("loc_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1F0")
    Jump("loc_215")

    label("loc_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1FA")
    Jump("loc_215")

    label("loc_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_204")
    Jump("loc_215")

    label("loc_204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_20E")
    Jump("loc_215")

    label("loc_20E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_215")

    label("loc_215")

    Return()

    # Function_1_1A3 end

    def Function_2_216(): pass

    label("Function_2_216")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_216")

    label("loc_22B")

    Return()

    # Function_2_216 end

    def Function_3_22C(): pass

    label("Function_3_22C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24F")
    OP_8D(0xFE, -28070, -8920, -16500, 6400, 3000)
    Jump("Function_3_22C")

    label("loc_24F")

    Return()

    # Function_3_22C end

    def Function_4_250(): pass

    label("Function_4_250")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2FD")

    ChrTalk(
        0xFE,
        (
            "塞维安那家伙，\x01",
            "说什么在执勤的时候\x01",
            "看到了一个女孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过也真是的， \x01",
            "他很久没见到女儿，\x01",
            "是不是产生幻觉了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3AF")

    ChrTalk(
        0xFE,
        "这一带还真是平静啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从这里眺望远景，\x01",
            "真是难以想象\x01",
            "这个国家会发生恐怖事件。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_3AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_47C")

    ChrTalk(
        0xFE,
        (
            "昨天我看见有军用艇\x01",
            "从洛连特那边飞向王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个时间本应该是\x01",
            "定期船通行的时段，\x01",
            "是不是发生什么紧急事件了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_54A")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "之前我在周游道看到了一只白隼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "白隼是\x01",
            "利贝尔王国的国徽，\x01",
            "据说看到的人就会有好运气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67F")

    label("loc_54A")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "之前我在周游道看到了一只白隼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "白隼是\x01",
            "利贝尔王国的国徽，\x01",
            "据说看到的人就会有好运气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望诞辰庆典和武术大会\x01",
            "能够平安无事地结束……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67F")

    Jump("loc_DDD")

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_733")

    ChrTalk(
        0xFE,
        (
            "刚才有一架定期船\x01",
            "从格鲁纳门上空通过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然为了盘查恐怖人员\x01",
            "定期船被迫停航了一段时间，\x01",
            "不过最后还是恢复正常了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_832")

    ChrTalk(
        0xFE,
        (
            "今天的天气也很不错呢。\x01",
            "连湖对岸的古罗尼连峰\x01",
            "也能看得清清楚楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "利贝尔王国的正中央\x01",
            "有一个瓦雷利亚湖对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "湖的四面环山傍海，\x01",
            "不管从哪个角度看，风景都十分迷人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_8E5")

    ChrTalk(
        0xFE,
        (
            "我看到神秘森林那边\x01",
            "有奇怪的飞艇起飞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "向队长报告了以后， \x01",
            "他脸色一变，然后就开始思考着什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_9A9")

    ChrTalk(
        0xFE,
        "好，今天也没有什么异常。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然战争已经结束了１０年了，\x01",
            "只要一想起那时的状况，\x01",
            "就不能放松对这里的警戒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_9A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_AB1")

    ChrTalk(
        0xFE,
        (
            "我觉得我们的队长\x01",
            "是个非常率直的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是他总是\x01",
            "为各种事情操心，\x01",
            "难道他不累吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要调集兵力也很不容易啊。\x01",
            "至少要加紧脚步行动才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_BF6")

    ChrTalk(
        0xFE,
        (
            "每一个关所\x01",
            "都至少要配备\x01",
            "一个守备队的警备力量才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然通过关所的人减少了，\x01",
            "但是自从百日战役结束以来，\x01",
            "也就一直像现在这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然战争结束了，\x01",
            "但并不意味着帝国的威胁就这样消失了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_D41")

    ChrTalk(
        0xFE,
        "嗯，今天也没有什么异常。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我肚子也饿了，\x01",
            "报告一下之后就去食堂吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为食堂的店主喜欢新鲜事物，\x01",
            "所以那里的菜单经常换来换去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，我可不是说\x01",
            "所有的饭菜都非常好吃。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_D41")


    ChrTalk(
        0xFE,
        (
            "啊呀，没想到你们能来到这里。\x01",
            "中途有没有迷路啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这栋建筑物的内部\x01",
            "要比从外面看起来的复杂哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDD")

    TalkEnd(0xFE)
    Return()

    # Function_4_250 end

    def Function_5_DE1(): pass

    label("Function_5_DE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_F5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E85")

    ChrTalk(
        0xFE,
        (
            "昨天开始王国各地的关所\x01",
            "都已经被完全封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在一切通行手续\x01",
            "都无法办理呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5A")

    label("loc_E85")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "欢迎来到格鲁纳门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……虽然我想这么说，\x01",
            "昨天开始王国各地的关所\x01",
            "都已经被完全封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在一切通行手续\x01",
            "都无法办理呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5A")

    Jump("loc_11CA")

    label("loc_F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_FD8")

    ChrTalk(
        0xFE,
        "武术大会今天就结束了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，在恐怖分子被抓到之前，\x01",
            "我们是不会掉以轻心的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CA")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_105D")

    ChrTalk(
        0xFE,
        (
            "上头下达命令\x01",
            "要求我们加强警备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "通行证的发行\x01",
            "从今天起也开始变得严格了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CA")

    label("loc_105D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_10D0")

    ChrTalk(
        0xFE,
        (
            "我记得武术大会的正式赛\x01",
            "就是从今天开始吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今年谁会取胜呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11CA")

    label("loc_10D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1167")

    ChrTalk(
        0xFE,
        (
            "中央工房受到袭击，\x01",
            "这可不是一件小事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "柏斯和卢安的事件\x01",
            "才刚告一个段落……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CA")

    label("loc_1167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_11CA")

    ChrTalk(
        0xFE,
        "这里是格鲁纳门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是连接格兰赛尔地区\x01",
            "和洛连特地区的关所。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CA")

    TalkEnd(0xFE)
    Return()

    # Function_5_DE1 end

    def Function_6_11CE(): pass

    label("Function_6_11CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_12B2")

    ChrTalk(
        0xFE,
        (
            "听说王城里\x01",
            "举办了宫廷晚宴，\x01",
            "女王陛下是不是也出席了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "关于生病和诞辰庆典的事情，\x01",
            "还是应该正式对外\x01",
            "宣告一下比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_12B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1391")

    ChrTalk(
        0xFE,
        (
            "最近这几天，\x01",
            "经常能在这附近\x01",
            "看到情报部的特务部队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在诞辰庆典前还抓不到恐怖分子，\x01",
            "真让人不安啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_1391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1410")

    ChrTalk(
        0xFE,
        "没有异常！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里现在还没有出现\x01",
            "亲卫队或者是可疑人物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_1410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_14B7")

    ChrTalk(
        0xFE,
        (
            "听说亲卫队犯了叛逆罪，\x01",
            "我可是吓了一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是任务就是任务。\x01",
            "如果和他们遇上，\x01",
            "也就不得不出手了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_14B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_159D")

    ChrTalk(
        0xFE,
        (
            "出于恐怖分子的原因，\x01",
            "那位摩尔根将军\x01",
            "终于要开始行动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要理查德上校\x01",
            "和摩尔根将军齐上阵，\x01",
            "解决这个事件只是时间的问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_159D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_1786")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1692")

    ChrTalk(
        0xFE,
        (
            "这条艾尔贝周游道\x01",
            "是围绕王都地区一周的街道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "庭园大道和艾尔贝周游道\x01",
            "是围绕王都地区一周的街道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以经常会有人没看清楚\x01",
            "哪条路去王都更近一点，\x01",
            "而绕了一个大圈子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_1692")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "庭园大道和艾尔贝周游道\x01",
            "是围绕王都地区一周的街道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以经常会有人没有看清楚\x01",
            "哪条路去王都更近一点，\x01",
            "而绕了一个大圈子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前就有一个戴着眼镜的\x01",
            "奇怪的姑娘绕了一整圈呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1786")

    TalkEnd(0xFE)
    Return()

    # Function_6_11CE end

    def Function_7_178A(): pass

    label("Function_7_178A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_187D")

    ChrTalk(
        0xFE,
        (
            "什么，你们要去柏斯？\x01",
            "那么，可不是往这边走哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "应该回到洛连特从城的西门出发，\x01",
            "然后向威尔特桥那边走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是朝着帕赛尔农场的方向哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_187D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1930")

    ChrTalk(
        0xFE,
        (
            "最近，有报告说\x01",
            "在神秘森林附近看见奇怪的人影。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们在通过街道的时候要小心点。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_1930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_19FA")

    ChrTalk(
        0xFE,
        (
            "自从定期船开始运航以来，\x01",
            "从这里通行的人就大大减少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这种时期，来这里的人\x01",
            "大多都是来游览这座长城的旅客。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_19FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1A7B")

    ChrTalk(
        0xFE,
        (
            "如今的王国军有一位\x01",
            "虽然年轻但非常了不起的上校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在普通士兵之间，\x01",
            "他也非常受欢迎呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_1A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1B76")

    ChrTalk(
        0xFE,
        (
            "百日战役的时候，\x01",
            "多亏了这个亚宁堡，\x01",
            "才让王都免于被帝国军侵占。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "占领了四个城市的帝国军\x01",
            "也对这座长城\x01",
            "感到无从下手呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_1B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1C08")

    ChrTalk(
        0xFE,
        (
            "这座巨大的长城\x01",
            "被称为『亚宁堡』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "它是围绕隔壁的格兰赛尔地区\x01",
            "而建造起来的城墙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_1C08")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "这座巨大的长城\x01",
            "被称为『亚宁堡』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "它是围绕隔壁的格兰赛尔地区\x01",
            "而建造起来的城墙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说它在利贝尔王国\x01",
            "建国之前就已经存在了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是什么人为了什么原因建起来的呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1D14")

    TalkEnd(0xFE)
    Return()

    # Function_7_178A end

    def Function_8_1D18(): pass

    label("Function_8_1D18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1DA5")

    ChrTalk(
        0xFE,
        "欢迎来到格鲁纳门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要去格兰赛尔地区的话，\x01",
            "通过这个关所就能到了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_1DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1E1F")

    ChrTalk(
        0xFE,
        (
            "哦？\x01",
            "你们好像都是游击士嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道这一带\x01",
            "发生了什么事情吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_1E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1ECB")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "最近利贝尔通讯社的记者\x01",
            "到过亚宁堡来取材呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说什么要写一篇\x01",
            "关于古老遗迹的特集。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_1ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1FE0")

    ChrTalk(
        0xFE,
        (
            "这前面不止有王都，\x01",
            "还有王家的艾尔贝离宫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "离宫在公用时间之外，\x01",
            "均向格兰赛尔市民开放，\x01",
            "可以自由出入哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "艾莉茜雅女王即位以来，\x01",
            "王家也改变了许多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_1FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_2086")

    ChrTalk(
        0xFE,
        (
            "格兰赛尔城位于瓦雷利亚湖畔上，\x01",
            "是一座非常美丽的城堡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "街上的热闹景象也非常让人惊叹。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_2086")


    ChrTalk(
        0xFE,
        (
            "前面就是格兰赛尔地区了。\x01",
            "去王都有事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DB")

    TalkEnd(0xFE)
    Return()

    # Function_8_1D18 end

    def Function_9_20DF(): pass

    label("Function_9_20DF")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_9_20DF end

    SaveToFile()

Try(main)
