from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1130   ._SN',
        MapName             = 'Bose',
        Location            = 'T1130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0130   ._SN',
            'ED6_DT01/T1130_1 ._SN',
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
        '豪尔斯教区长',                         # 9
        '修女萝萨',                             # 10
        '西加罗',                               # 11
        '艾德尔',                               # 12
        '莉拉',                                 # 13
        '萨拉',                                 # 14
        '目标用摄像机',                         # 15
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01410 ._CH',             # 01
        'ED6_DT07/CH01043 ._CH',             # 02
        'ED6_DT07/CH01213 ._CH',             # 03
        'ED6_DT07/CH01350 ._CH',             # 04
        'ED6_DT07/CH02370 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01410P._CP',             # 01
        'ED6_DT07/CH01043P._CP',             # 02
        'ED6_DT07/CH01213P._CP',             # 03
        'ED6_DT07/CH01350P._CP',             # 04
        'ED6_DT07/CH02370P._CP',             # 05
    )

    DeclNpc(
        X                   = 59100,
        Z                   = 1000,
        Y                   = 52100,
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
        X                   = 15690,
        Z                   = 4000,
        Y                   = 43180,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 63600,
        Z                   = 90,
        Y                   = 46000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 62600,
        Z                   = 90,
        Y                   = 46000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 58950,
        Z                   = 0,
        Y                   = 48260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58920,
        Z                   = 0,
        Y                   = 48170,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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


    DeclActor(
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50250,
        TriggerRange        = 400,
        ActorX              = 59100,
        ActorZ              = 2500,
        ActorY              = 52100,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_247",          # 01, 1
        "Function_2_248",          # 02, 2
        "Function_3_25E",          # 03, 3
        "Function_4_27C",          # 04, 4
        "Function_5_CEC",          # 05, 5
        "Function_6_160A",         # 06, 6
        "Function_7_168C",         # 07, 7
        "Function_8_173A",         # 08, 8
        "Function_9_17F1",         # 09, 9
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1E8")
    Jump("loc_235")

    label("loc_1E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1F7")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_235")

    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_206")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_235")

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_210")
    Jump("loc_235")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_21A")
    Jump("loc_235")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_224")
    Jump("loc_235")

    label("loc_224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_235")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_246")
    ClearChrFlags(0xC, 0x80)

    label("loc_246")

    Return()

    # Function_0_1DE end

    def Function_1_247(): pass

    label("Function_1_247")

    Return()

    # Function_1_247 end

    def Function_2_248(): pass

    label("Function_2_248")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_248")

    label("loc_25D")

    Return()

    # Function_2_248 end

    def Function_3_25E(): pass

    label("Function_3_25E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_277")
    Call(1, 0)
    Jump("loc_27B")

    label("loc_277")

    Call(0, 4)

    label("loc_27B")

    Return()

    # Function_3_25E end

    def Function_4_27C(): pass

    label("Function_4_27C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_345")

    ChrTalk(
        0x8,
        (
            "你们从洛连特一路赶来，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "空之女神爱德丝啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请赐予他们护佑……\x01",
            "并且给予他们指引……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE8")

    label("loc_345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_443")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "虽然发生了很多事情，\x01",
            "不过现在城市似乎已经\x01",
            "恢复了往常的平静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呵呵，\x01",
            "就算发生了意外也不会失去活力，\x01",
            "这就是柏斯市民的优点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "呵·呵·呵。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D1")

    label("loc_443")


    ChrTalk(
        0x8,
        (
            "就算发生了什么意外\x01",
            "也不会失去活力，\x01",
            "这就是柏斯市民的优点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D1")

    Jump("loc_CE8")

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_683")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EA")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "不知为何，\x01",
            "最近总是接连发生许多案件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "为了这里的市民，\x01",
            "我们来对天祈祷吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "空之女神爱德丝啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请保佑这里的每个人……\x01",
            "并且给予他们指引……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_680")

    label("loc_5EA")


    ChrTalk(
        0x8,
        (
            "不知为何，\x01",
            "最近总是接连发生许多案件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "为了这里的市民，\x01",
            "我们来对天祈祷吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_680")

    Jump("loc_CE8")

    label("loc_683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_6DC")

    ChrTalk(
        0x8,
        "不知为何外面这么吵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "发生什么事情了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE8")

    label("loc_6DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_89B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E0")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "出城往西走，有一个叫拉文努的小村。\x01",
            "那里是王国富有盛名的果树栽培园地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那个小村没有教会。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "其实，\x01",
            "我很想让那里的孩子们\x01",
            "也到这个教会的主日学校来上课啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_898")

    label("loc_7E0")


    ChrTalk(
        0x8,
        (
            "出城往西走，有一个叫拉文努的小村。\x01",
            "那里是王国富有盛名的果树栽培园地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "其实，\x01",
            "我很想让那里的孩子们\x01",
            "也到这个教会的主日学校来上课啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_898")

    Jump("loc_CE8")

    label("loc_89B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_A2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F5")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "修女萝萨\x01",
            "非常认真而且优秀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呵呵，\x01",
            "如果她能少付出一点多余的关心就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "柏斯的人民\x01",
            "非常崇尚自由的风气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然教义和戒律也很重要，\x01",
            "但是教会也要根据\x01",
            "当地的实际情况而进行活动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A27")

    label("loc_9F5")


    ChrTalk(
        0x8,
        (
            "呵呵，每个人的身高不同，\x01",
            "思考的角度也不同，\x01",
            "不能强求……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A27")

    Jump("loc_CE8")

    label("loc_A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_AFB")

    ChrTalk(
        0x8,
        (
            "现在的市长梅贝尔小姐\x01",
            "是前任市长的女儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然她还年轻，\x01",
            "有时候做事有点欠考虑……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过也能看到她有很多\x01",
            "不逊色于父亲的优点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE8")

    label("loc_AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_CE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C24")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "柏斯的大部分街道\x01",
            "在１０年前的战争中一度成为瓦砾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "战后，商人们都把自己的财产\x01",
            "捐出来作为复兴城市的资金。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "原本各自为政的商人们\x01",
            "也因为这样而团结起来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE8")

    label("loc_C24")


    ChrTalk(
        0x8,
        (
            "柏斯的大部分街道\x01",
            "在１０年前的战争中一度成为瓦砾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "战后，商人们都把自己的财产\x01",
            "捐出来作为复兴城市的资金。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE8")

    TalkEnd(0x8)
    Return()

    # Function_4_27C end

    def Function_5_CEC(): pass

    label("Function_5_CEC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E43")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "扫除做完了，\x01",
            "衣物也都洗完了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "讲话稿也写好了，\x01",
            "弥撒也准备好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了对了，\x01",
            "主日学校下一次的课程该怎么办呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不把以后要做的事情决定下来，\x01",
            "我是不会放心的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E9A")

    label("loc_E43")


    ChrTalk(
        0xFE,
        (
            "不把以后要做的事情决定下来，\x01",
            "我是不会放心的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9A")

    Jump("loc_1606")

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_FE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4D")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "没想到竟然连普通的民居\x01",
            "也受到了强盗的洗劫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……等会儿我要去\x01",
            "探访一下受害的居民。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE4")

    label("loc_F4D")


    ChrTalk(
        0xFE,
        "商业街也受到了强盗的洗劫……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "等会儿我要去\x01",
            "探访一下受害的居民。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE4")

    Jump("loc_1606")

    label("loc_FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1085")

    ChrTalk(
        0xFE,
        (
            "现在正在做礼拜，\x01",
            "外面还真是吵得很啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个城市也真是的，\x01",
            "总是那么吵吵嚷嚷的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1606")

    label("loc_1085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_125F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B3")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "经常来教会做礼拜的人\x01",
            "都是来祈求生意兴隆的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "爱德丝是创造女神，\x01",
            "而不是发财女神！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "是不是该在入口处贴一张告示呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125C")

    label("loc_11B3")


    ChrTalk(
        0xFE,
        (
            "经常来教会做礼拜的人\x01",
            "都是来祈求生意兴隆的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "爱德丝是创造女神，\x01",
            "而不是发财女神！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125C")

    Jump("loc_1606")

    label("loc_125F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1305")

    ChrTalk(
        0xFE,
        (
            "教区长非常通情达理，\x01",
            "也获得了很多人的支持……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过有时候有点自作主张\x01",
            "也算是个缺点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1606")

    label("loc_1305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1568")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146C")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "市长把礼拜交给女佣来做\x01",
            "真是前所未闻的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "教区长也不怎么介意，\x01",
            "真是可叹啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为市长，\x01",
            "应该为大家树立榜样才对啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1565")

    label("loc_146C")


    ChrTalk(
        0xFE,
        (
            "市长把礼拜交给女佣来做\x01",
            "真是前所未闻的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为市长，\x01",
            "应该为大家树立榜样才对啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1565")

    Jump("loc_1606")

    label("loc_1568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1606")

    ChrTalk(
        0xFE,
        "哎呀，欢迎来到七耀教会。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要做礼拜吗？\x01",
            "这么年轻值得表扬啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1606")

    TalkEnd(0x9)
    Return()

    # Function_5_CEC end

    def Function_6_160A(): pass

    label("Function_6_160A")

    TalkBegin(0xA)

    ChrTalk(
        0xFE,
        (
            "我一到达柏斯，\x01",
            "定期船就开始停航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还在巡礼的途中啊，\x01",
            "这下伤脑筋了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_6_160A end

    def Function_7_168C(): pass

    label("Function_7_168C")

    TalkBegin(0xB)

    ChrTalk(
        0xFE,
        "嘿嘿嘿，终于来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这一天终于到来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "等礼拜结束之后，\x01",
            "就向柏斯超市进发！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_7_168C end

    def Function_8_173A(): pass

    label("Function_8_173A")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BB")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "为什么士兵\x01",
            "都是那么傲慢呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还是游击士比较友善，\x01",
            "我喜欢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17ED")

    label("loc_17BB")


    ChrTalk(
        0xFE,
        (
            "今天我会连大小姐的那份\x01",
            "也一起祈祷呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17ED")

    TalkEnd(0xD)
    Return()

    # Function_8_173A end

    def Function_9_17F1(): pass

    label("Function_9_17F1")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1897")

    ChrTalk(
        0xFE,
        (
            "#620F小姐连续好几天\x01",
            "彻夜不眠地加班加点，\x01",
            "来想办法如何处理强盗事件。\x02\x03",
            "如果我无法好好照顾\x01",
            "小姐的身体状况的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F73")

    label("loc_1897")

    EventBegin(0x0)
    OP_A2(0x30A)
    Fade(1000)
    SetChrPos(0x101, 58910, 0, 46930, 0)
    SetChrPos(0x102, 58250, 0, 46000, 0)
    SetChrPos(0x103, 59540, 0, 46030, 0)
    TurnDirection(0xFE, 0x101, 0)
    OP_69(0xC, 0x3E8)

    ChrTalk(
        0x101,
        "#001F是女佣小姐，找到了！\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#620F诸位是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔，这么冒失太失礼了。\x02\x03",
            "#010F非常抱歉，我们是游击士协会的人。\x02\x03",
            "为了确认委托的内容，\x01",
            "特地前来拜访你们的市长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#621F啊，是这样啊……\x02\x03",
            "请允许我先自我介绍一下。\x01",
            "我是女佣莉拉。\x02\x03",
            "打理市长的日常生活\x01",
            "是我的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F打理日常生活……\x01",
            "真是活在不同的世界啊～\x02\x03",
            "那么市长在哪里呢？\x01",
            "不是说来这里做礼拜吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#623F……逃掉了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#620F我想现在大概\x01",
            "正在超市里面视察吧。\x02\x03",
            "刚才市长吩咐我，\x01",
            "让我代替做礼拜，\x01",
            "然后自己就出去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#019F该怎么说呢……\x01",
            "真是一位独特的人物啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F呵呵，市长还真有趣。\x01",
            "暂且不说是不是专注于职务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#620F市长确实是位十分有能力的人。\x01",
            "只是有时候的行动让人无法捉摸。\x02\x03",
            "……我差不多\x01",
            "该去接市长回官邸了。\x02\x03",
            "十分抱歉，能不能先请\x01",
            "诸位到市长官邸稍稍等候一下？\x02\x03",
            "我陪同市长随后就到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯～都到这里来了，\x01",
            "要是空着手回去也不太好嘛……\x02\x03",
            "可以的话，我们和你一起去好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#622F一起去迎接市长吗？\x01",
            "我倒是没什么意见……\x02\x03",
            "#621F那么我们立刻前往\x01",
            "坐落在市中央的柏斯超市吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x10)
    SetChrFlags(0xC, 0x40)
    OP_92(0xC, 0x0, 0x0, 0xBB8, 0x0)
    SetChrFlags(0xC, 0x80)
    EventEnd(0x0)
    AddParty(0x33, 0xFF)
    SetMapFlags(0x1)

    label("loc_1F73")

    TalkEnd(0xC)
    Return()

    # Function_9_17F1 end

    SaveToFile()

Try(main)
