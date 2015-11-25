from ED6ScenarioHelper import *

def main():
    # 格鲁纳门

    CreateScenaFile(
        FileName            = 'T0601   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0601.x',
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
        '士兵塞维安',                           # 9
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
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
    )

    DeclNpc(
        X                   = -940,
        Z                   = 7250,
        Y                   = -94770,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_D3",           # 01, 1
        "Function_2_E6",           # 02, 2
        "Function_3_FC",           # 03, 3
        "Function_4_120",          # 04, 4
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Return()

    # Function_0_D2 end

    def Function_1_D3(): pass

    label("Function_1_D3")

    OP_16(0x2, 0xFA0, 0xFFFE0818, 0xFFFD7790, 0x30012)
    Return()

    # Function_1_D3 end

    def Function_2_E6(): pass

    label("Function_2_E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_E6")

    label("loc_FB")

    Return()

    # Function_2_E6 end

    def Function_3_FC(): pass

    label("Function_3_FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11F")
    OP_8D(0xFE, -3140, -97580, 1480, -73120, 3000)
    Jump("Function_3_FC")

    label("loc_11F")

    Return()

    # Function_3_FC end

    def Function_4_120(): pass

    label("Function_4_120")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D6")

    ChrTalk(
        0xFE,
        (
            "唔～……\x01",
            "之前在这里执勤的时候，\x01",
            "我好像看到了一个女孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我正觉得奇怪，\x01",
            "想擦一下眼睛看清楚的时候，\x01",
            "她却又不见了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF")

    label("loc_1D6")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "唔～……\x01",
            "之前在这里执勤的时候，\x01",
            "我好像看到了一个女孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我正觉得奇怪，\x01",
            "想擦一下眼睛看清楚的时候，\x01",
            "她却又不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔～是不是我累了呢……\x02",
    )

    CloseMessageWindow()

    label("loc_2AF")

    Jump("loc_14D5")

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_38D")

    ChrTalk(
        0xFE,
        (
            "武术大会\x01",
            "今天要进行决战了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然是特务部队的家伙\x01",
            "进入了决赛啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我不想承认，\x01",
            "不过他们的确有两手。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_46A")

    ChrTalk(
        0xFE,
        (
            "从今天开始，\x01",
            "巡视的次数要增加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不能及时传递情报的话，\x01",
            "就无法抓住恐怖分子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_54C")

    ChrTalk(
        0xFE,
        (
            "艾尔贝周游道绿意昂然，\x01",
            "平时去那里散步是最合适不过的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "现在恐怖分子可能就潜藏在\x01",
            "那花草树木中的某处啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_664")

    label("loc_54C")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "艾尔贝周游道绿意昂然，\x01",
            "平时去那里散步是最合适不过的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于格兰赛尔的市民来说，\x01",
            "这一带就好像是个公园。\x01",
            "实在是相当的漂亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "现在恐怖分子可能就潜藏在\x01",
            "那花草树木中的某处啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_664")

    Jump("loc_14D5")

    label("loc_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_74A")

    ChrTalk(
        0xFE,
        (
            "我从来没有在这里\x01",
            "看到过亲卫队的身影。\x01",
            "今天一天还算平静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是现在守卫王都的同志们\x01",
            "一定很辛苦吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_ABC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 1)), scpexpr(EXPR_END)), "loc_89B")

    ChrTalk(
        0xFE,
        (
            "城墙上太宽阔了，\x01",
            "要巡视一遍非常辛苦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在观光客\x01",
            "都集中到王都去了，\x01",
            "所以还算比较轻松。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果恐怖分子\x01",
            "混在观光客里进入王都，\x01",
            "那就难以区分了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB9")

    label("loc_89B")

    OP_A2(0x6E9)

    ChrTalk(
        0xFE,
        "你们能来到这里也很辛苦啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "把这个送给你们做纪念吧。\x01",
            "哈哈，我还真是老土啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x21A, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "红耀石　第９卷\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        (
            "城墙上太宽阔了，\x01",
            "要巡视一遍非常辛苦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在观光客\x01",
            "都集中到王都去了，\x01",
            "所以还算比较轻松。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果恐怖分子\x01",
            "混在观光客里进入王都，\x01",
            "那就难以区分了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB9")

    Jump("loc_14D5")

    label("loc_ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_B48")

    ChrTalk(
        0xFE,
        (
            "平时这个时候定期船总会从我头上经过，\x01",
            "今天却没来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "航运全部停止的传言\x01",
            "看来是真的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_C3B")

    ChrTalk(
        0xFE,
        "呼，差不多到交班的时间了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "结束这里的执勤后，\x01",
            "进入里面享受清爽的空气，\x01",
            "心情真好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好就没有去食堂喝一杯了，\x01",
            "今天就去怀念一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_E96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAC")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "这里偶尔也会有\x01",
            "学者之类的人前来调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来这里果然是\x01",
            "非常古老的遗迹呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对有兴趣的人来说，\x01",
            "也许是一个不可思议的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对我这个没有学问的人来说，\x01",
            "这里除了是工作场所以外，一无是处。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E93")

    label("loc_DAC")


    ChrTalk(
        0xFE,
        (
            "这里偶尔也会有\x01",
            "学者之类的人前来调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来这里果然是\x01",
            "非常古老的遗迹呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对有兴趣的人来说，\x01",
            "也许是一个不可思议的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E93")

    Jump("loc_14D5")

    label("loc_E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1172")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CB")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "就在不久之前， \x01",
            "我的女儿还来这里玩过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听到我说在这里工作的时候，\x01",
            "她可是非常羡慕啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "小孩子这么率直，真好啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然现在白天很温暖，\x01",
            "但是冬天的晚上在这里执勤的话，\x01",
            "可真的是非常痛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "又暗，又冷，风又强，\x01",
            "皮肤冻裂，鼻涕也停不下来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还有，夏天的白天热得不行，\x01",
            "连意识都会模糊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，可以眺望到好风景，\x01",
            "的确是让人欣喜的一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116F")

    label("loc_10CB")


    ChrTalk(
        0xFE,
        (
            "就在不久之前， \x01",
            "我的女儿还来这里玩过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听到我说在这里工作的时候，\x01",
            "她可是非常羡慕啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "小孩子这么率直，真好啊……\x02",
    )

    CloseMessageWindow()

    label("loc_116F")

    Jump("loc_14D5")

    label("loc_1172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1265")

    ChrTalk(
        0xFE,
        "今天没有什么特别异常的情况。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王都这边和洛连特那边\x01",
            "不管什么时候都很平静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "１０年前这座城墙外\x01",
            "帝国大军的铁蹄到处肆虐，\x01",
            "如今实在无法想象当年的情景啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_1265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1429")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "啊，欢迎来到亚宁堡。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们到这里来，\x01",
            "是观光还是来调查遗迹？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这座城墙将格兰赛尔地区\x01",
            "整个围绕起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前的诗中曾说过，王都是颗珍珠，\x01",
            "亚宁堡是将珍珠包起来的贝壳，\x01",
            "好像就是这么比喻的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "它已经十分古旧了，\x01",
            "但至今人们仍没有弄明白\x01",
            "建造这座长城的用意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了防止敌人侵入的说法，\x01",
            "现在来看是最有力的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_1429")


    ChrTalk(
        0xFE,
        (
            "这座城墙将格兰赛尔地区\x01",
            "整个围绕起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前的诗中曾说过，王都是颗珍珠，\x01",
            "亚宁堡是将珍珠包起来的贝壳，\x01",
            "好像就是这么比喻的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D5")

    TalkEnd(0xFE)
    Return()

    # Function_4_120 end

    SaveToFile()

Try(main)
