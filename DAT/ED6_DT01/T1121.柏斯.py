from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1121   ._SN',
        MapName             = 'Bose',
        Location            = 'T1121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1121   ._SN',
            'ED6_DT01/T1121_1 ._SN',
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
        '卢格兰老人',                           # 9
        '斯丁克',                               # 10
        '亚妮拉丝',                             # 11
        '梅贝尔',                               # 12
        '莉拉',                                 # 13
        '售票员泰德',                           # 14
        '小包',                                 # 15
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
        'ED6_DT07/CH02380 ._CH',             # 00
        'ED6_DT07/CH01620 ._CH',             # 01
        'ED6_DT07/CH01630 ._CH',             # 02
        'ED6_DT07/CH02360 ._CH',             # 03
        'ED6_DT07/CH02370 ._CH',             # 04
        'ED6_DT07/CH01290 ._CH',             # 05
        'ED6_DT07/CH00003 ._CH',             # 06
        'ED6_DT07/CH00013 ._CH',             # 07
        'ED6_DT07/CH00023 ._CH',             # 08
        'ED6_DT07/CH00033 ._CH',             # 09
        'ED6_DT06/CH20020 ._CH',             # 0A
        'ED6_DT06/CH20021 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH02380P._CP',             # 00
        'ED6_DT07/CH01620P._CP',             # 01
        'ED6_DT07/CH01630P._CP',             # 02
        'ED6_DT07/CH02360P._CP',             # 03
        'ED6_DT07/CH02370P._CP',             # 04
        'ED6_DT07/CH01290P._CP',             # 05
        'ED6_DT07/CH00003P._CP',             # 06
        'ED6_DT07/CH00013P._CP',             # 07
        'ED6_DT07/CH00023P._CP',             # 08
        'ED6_DT07/CH00033P._CP',             # 09
        'ED6_DT06/CH20020P._CP',             # 0A
        'ED6_DT06/CH20021P._CP',             # 0B
    )

    DeclNpc(
        X                   = 186,
        Z                   = 0,
        Y                   = 4400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x114,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 34900,
        Z                   = 0,
        Y                   = -2300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 25010,
        Z                   = 0,
        Y                   = 630,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -60835,
        Z                   = 0,
        Y                   = 38681,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35500,
        Z                   = 0,
        Y                   = -2500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 46050,
        Z                   = 0,
        Y                   = 19400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 25390,
        Z                   = 750,
        Y                   = -3760,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 983051,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E7,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 130,
        TriggerZ            = 0,
        TriggerY            = 3000,
        TriggerRange        = 600,
        ActorX              = 186,
        ActorZ              = 1500,
        ActorY              = 4400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4470,
        TriggerZ            = 0,
        TriggerY            = -2690,
        TriggerRange        = 1400,
        ActorX              = -4470,
        ActorZ              = 2000,
        ActorY              = -2690,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3520,
        TriggerZ            = 0,
        TriggerY            = -780,
        TriggerRange        = 1400,
        ActorX              = 3520,
        ActorZ              = 2000,
        ActorY              = -780,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_256",          # 00, 0
        "Function_1_2CB",          # 01, 1
        "Function_2_2CC",          # 02, 2
        "Function_3_2E2",          # 03, 3
        "Function_4_306",          # 04, 4
        "Function_5_555",          # 05, 5
        "Function_6_1D22",         # 06, 6
        "Function_7_234C",         # 07, 7
        "Function_8_2F90",         # 08, 8
        "Function_9_4452",         # 09, 9
        "Function_10_5E95",        # 0A, 10
    )


    def Function_0_256(): pass

    label("Function_0_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_26F")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_29E")

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_279")
    Jump("loc_29E")

    label("loc_279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_288")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_29E")

    label("loc_288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_292")
    Jump("loc_29E")

    label("loc_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_29E")
    ClearChrFlags(0x9, 0x80)

    label("loc_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2AC")
    OP_A3(0x3FA)
    Event(0, 9)

    label("loc_2AC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2B8"),
        (SWITCH_DEFAULT, "loc_2CA"),
    )


    label("loc_2B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C7")
    OP_A2(0x308)
    Event(0, 8)

    label("loc_2C7")

    Jump("loc_2CA")

    label("loc_2CA")

    Return()

    # Function_0_256 end

    def Function_1_2CB(): pass

    label("Function_1_2CB")

    Return()

    # Function_1_2CB end

    def Function_2_2CC(): pass

    label("Function_2_2CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2CC")

    label("loc_2E1")

    Return()

    # Function_2_2CC end

    def Function_3_2E2(): pass

    label("Function_3_2E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_305")
    OP_8D(0xFE, 24030, 2670, 26360, -1350, 1500)
    Jump("Function_3_2E2")

    label("loc_305")

    Return()

    # Function_3_2E2 end

    def Function_4_306(): pass

    label("Function_4_306")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "报告\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53F")
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x35, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x35, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_423")

    ChrTalk(
        0x8,
        (
            "#630F之前调查的报酬\x01",
            "梅贝尔市长已经支付过了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_AF(0x1C, 0x35)
    Sleep(100)
    OP_28(0x36, 0x4, 0x10)
    OP_28(0x36, 0x4, 0x20)

    ChrTalk(
        0x8,
        (
            "#630F唔，\x01",
            "接下来你们也要认真地进行调查哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_536")

    label("loc_423")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x1C)"), scpexpr(EXPR_END)), "loc_4AD")

    ChrTalk(
        0x8,
        (
            "#630F嗯，辛苦了。\x01",
            "看起来很顺利地完成工作了嘛。\x02\x03",
            "如果完成其他任务的话，\x01",
            "可以随时再来向我报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_536")

    label("loc_4AD")

    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#630F唔，\x01",
            "现在好像没有可以报告的工作。\x02\x03",
            "如果完成其他任务的话，\x01",
            "可以随时再来向我报告。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_536")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_53F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_550")
    TalkEnd(0x8)
    Return()

    label("loc_550")

    Call(0, 5)
    Return()

    # Function_4_306 end

    def Function_5_555(): pass

    label("Function_5_555")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_749")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EA")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "#630F哦，你们要去卢安吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，卢格兰爷爷，\x01",
            "谢谢您最近一段时间的照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F真是麻烦您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630F没什么没什么。\x02\x03",
            "你们走了之后\x01",
            "还真是有点寂寞呢。\x02\x03",
            "如果再来到柏斯的话\x01",
            "一定要来这里看看啊。\x02\x03",
            "#631F无论你们什么时候来，\x01",
            "我都十分欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯，我知道啦。\x01",
            "您也要保重哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_6EA")


    ChrTalk(
        0x8,
        (
            "#630F去卢安的话，\x01",
            "会经过比较难走的山道。\x02\x03",
            "赶路的时候要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_746")

    Jump("loc_1D1E")

    label("loc_749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_864")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#630F是吗，要去湖边的旅馆吗。\x02\x03",
            "从柏斯市的南门出去，\x01",
            "沿着安塞尔新街一直走下去就到了。\x02\x03",
            "就是瓦雷利亚湖边的建筑物，\x01",
            "你们一到就应该看到了。\x02\x03",
            "你们路上要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FD")

    label("loc_864")


    ChrTalk(
        0x8,
        (
            "#630F是吗，要去湖边的旅馆吗。\x02\x03",
            "从柏斯市的南门出去，\x01",
            "沿着安塞尔新街向南走哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FD")

    Jump("loc_1D1E")

    label("loc_900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6B")
    OP_A2(0x36D)

    ChrTalk(
        0x8,
        (
            "#630F哦哦，是雪拉扎德啊。\x01",
            "你们终于回来了。\x02\x03",
            "之前吓了我一跳哦。\x02\x03",
            "游击士在调查中竟被军队逮捕，\x01",
            "这还真是闻所未闻的事情啊。\x02\x03",
            "摩尔根将军也真是干得出来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F真是非常抱歉。\x01",
            "让你们这么担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630F没事没事，\x01",
            "不管怎么说能够平安回来比什么都好。\x02\x03",
            "本来我们打算\x01",
            "以柏斯支部的名义\x01",
            "来向王都提出抗议的。\x02\x03",
            "就在那个时候，\x01",
            "梅贝尔市长亲自出面调停了这件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F原、原来\x01",
            "这件事引起这么多风波啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F这样啊……\x02\x03",
            "不过利贝尔王国既然承认了\x01",
            "游击士拥有特别的搜查权。\x02\x03",
            "那么将军的行动就与\x01",
            "王国所作的规定相违背了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630F嗯，不过这件事已经平息，\x01",
            "也算是解决了问题，\x01",
            "大家就安心继续工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3D")

    label("loc_C6B")


    ChrTalk(
        0x8,
        (
            "#630F不管怎样，\x01",
            "你们现在还是专注于\x01",
            "调查强盗案件比较好一些。\x02\x03",
            "你们还会和军队那些人碰面的，\x01",
            "以后行动就多多小心一点哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3D")

    Jump("loc_1D1E")

    label("loc_D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_F81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC6")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#630F哦哦……\x01",
            "你们要去拉文努村调查吗。\x02\x03",
            "沿着西柏斯街道走，\x01",
            "途中会有一个山道的入口。\x02\x03",
            "你们沿着那条山道走，\x01",
            "就能到那里了。\x02\x03",
            "#632F拉文努村……\x01",
            "如果那家伙在这个支部的话，\x01",
            "也许如今的情况会好转些吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F7E")

    label("loc_EC6")


    ChrTalk(
        0x8,
        (
            "#630F拉文努村的话，\x01",
            "沿着途中会有一个山道的入口。\x02\x03",
            "你们沿着那条山道走，\x01",
            "就能到那里了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F7E")

    Jump("loc_1D1E")

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 5)), scpexpr(EXPR_END)), "loc_1085")

    ChrTalk(
        0x8,
        (
            "#630F空贼团『卡普亚一家』吗……\x02\x03",
            "没想到他们竟然策划\x01",
            "如此大胆无耻的犯罪行为。\x02\x03",
            "要想弄清楚现状\x01",
            "还需要更多的线索啊。\x01",
            "　\x02\x03",
            "总之现在去收集一下情报怎么样？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1110")

    label("loc_1085")


    ChrTalk(
        0x8,
        (
            "#630F空贼团『卡普亚一家』吗……\x02\x03",
            "没想到他们竟然策划\x01",
            "如此大胆无耻的犯罪行为。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1110")

    Jump("loc_1D1E")

    label("loc_1113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_END)), "loc_11F2")

    ChrTalk(
        0x8,
        (
            "#630F空贼团『卡普亚一家』吗……\x02\x03",
            "没想到他们竟然策划\x01",
            "如此大胆无耻的犯罪行为。\x02\x03",
            "要赶紧向梅贝尔市长\x01",
            "报告情况才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D1E")

    label("loc_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19D4")
    EventBegin(0x0)
    OP_A2(0x314)
    ClearMapFlags(0x1)
    Fade(1000)
    SetChrPos(0x101, 940, 0, 2160, 0)
    SetChrPos(0x102, 240, 0, 790, 0)
    SetChrPos(0x103, -540, 0, 1860, 0)
    OP_6D(640, 0, 2790, 1000)

    ChrTalk(
        0x8,
        (
            "#633F哦哦，你们几个回来了啊。\x01",
            "搞清楚到底发生什么事件了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿……\x01",
            "得到了重要的情报哦！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "众人把从将军那里得到的情报\x01",
            "向卢格兰老人进行了详细的说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#631F空贼团『卡普亚一家』……\x01",
            "这确实是重大的情报啊！\x02\x03",
            "这样一来，\x01",
            "协会的行动方针也可以决定了。\x02\x03",
            "#632F可是，摩尔根将军好像\x01",
            "比传说中还要讨厌游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯，吓死我了。\x02\x03",
            "因为在洛连特\x01",
            "游击士是个很受大家欢迎的职业，\x01",
            "这次竟然会被别人批了一番……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630F算了，摩尔根将军是个例外吧。\x02\x03",
            "一般情况下，\x01",
            "王国军和协会都还能维持着合作关系。\x02\x03",
            "#634F话说回来，\x01",
            "这次好像害你们多费了不少功夫，\x01",
            "真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F没什么，我们也希望能\x01",
            "做些自己力所能及的事情。\x02\x03",
            "对了，最近一段时间的盗窃案件\x01",
            "好像也是空贼团的所为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#632F嗯，结合洛连特的案件来分析，\x01",
            "应该错不了的。\x02\x03",
            "说是盗窃案件，\x01",
            "其实大部分都只是些琐碎的案子……\x02\x03",
            "不过，真没想到的是，\x01",
            "他们竟还能做出如此胆大包天的案件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F确实像您所说的那样。\x02\x03",
            "他们在洛连特犯下的\x01",
            "也是十分明目张胆的强盗事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F这次竟然劫持了定期船，\x01",
            "向王家要求赎金……\x02\x03",
            "我总觉得这风险太过高了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F嗯，以这个疑点为基础进行调查，\x01",
            "说不定能找到什么线索。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1D1E")

    label("loc_19D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1C7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC6")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#630F是吗，\x01",
            "你们要去哈肯门会见摩尔根将军啊。\x02\x03",
            "说实话，\x01",
            "你们能接受市长的委托，\x01",
            "真的是帮了大忙。\x02\x03",
            "最近这段时间\x01",
            "接连发生了不少事故\x01",
            "和与魔兽相关的事件。\x02\x03",
            "虽然都不是什么大事，\x01",
            "但是这里所属的游击士\x01",
            "都已经派出去工作了。\x02\x03",
            "本来我还想着\x01",
            "如果实在忙不过来，\x01",
            "就去联络其他支部要求支援呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C77")

    label("loc_1BC6")


    ChrTalk(
        0x8,
        (
            "#630F是吗，\x01",
            "你们要去哈肯门会见摩尔根将军啊。\x02\x03",
            "你们从东柏斯街道出去\x01",
            "沿着钢壁之路走就可以了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C77")

    Jump("loc_1D1E")

    label("loc_1C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1D1E")

    ChrTalk(
        0x8,
        (
            "#630F这样一来，\x01",
            "市长的委托就可以交托给你们了。\x02\x03",
            "市长官邸坐落在城西门附近。\x01",
            "你们就去打听一下消息吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1E")

    TalkEnd(0x8)
    Return()

    # Function_5_555 end

    def Function_6_1D22(): pass

    label("Function_6_1D22")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1DF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_1D9E")

    ChrTalk(
        0xFE,
        "……要走了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我期待着你们能\x01",
            "早日成为正游击士哦……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF3")

    label("loc_1D9E")


    ChrTalk(
        0xFE,
        "你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……和雪拉扎德\x01",
            "一起行动的准游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF3")

    Jump("loc_2348")

    label("loc_1DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_216A")
    OP_A2(0x35F)
    OP_A2(0x1)

    ChrTalk(
        0x101,
        "#006F（啊，这个人……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（嗯，\x01",
            "　好像和我们一样都是游击士呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F喂，打扰一下？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F还是那样冷淡呢，\x01",
            "斯丁克。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(
        0xFE,
        (
            "你是……\x01",
            "以前的那个见习游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F没错呢。\x02\x03",
            "托你的福，\x01",
            "现在我已经是正游击士啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼……看起来的确成熟了不少。\x01",
            "在柏斯支部有工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F嗯，现在就正在工作呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近发生了很多事情，\x01",
            "游击士的人手远远不够呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……那就靠你们了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)

    ChrTalk(
        0x101,
        (
            "#002F（是雪拉姐的熟人吧。\x01",
            "　感觉有点恐怖的人呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（但是那走路的动作……\x01",
            "　看起来应该很厉害吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2348")

    label("loc_216A")

    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B5")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是你们啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难得来到这里，\x01",
            "本来想开个欢迎会的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过现在库拉茨和亚妮拉丝\x01",
            "都因为工作出去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（……其实他人挺好的吧？）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(
        0x103,
        (
            "#020F（呵呵，别看他那个样子，\x01",
            "　其实很会关心人的。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    Jump("loc_2348")

    label("loc_22B5")


    ChrTalk(
        0xFE,
        (
            "最近发生了很多事情，\x01",
            "游击士的人手远远不够呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……那就靠你们了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)

    label("loc_2348")

    TalkEnd(0x9)
    Return()

    # Function_6_1D22 end

    def Function_7_234C(): pass

    label("Function_7_234C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_251B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24C6")
    OP_A2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_END)), "loc_2418")

    ChrTalk(
        0xFE,
        (
            "#814F啊，你们要走了吗？\x02\x03",
            "#818F真是遗憾啊……\x01",
            "本来还想和你们一起工作的。\x02\x03",
            "#810F今后还会有很多事情等着你们，\x01",
            "一定不要泄气，加油干哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24C3")

    label("loc_2418")


    ChrTalk(
        0xFE,
        (
            "#814F啊，难道你们就是\x01",
            "和雪拉前辈一起很活跃的……\x02\x03",
            "#810F嗯～真是年轻啊。\x02\x03",
            "今后还会有很多事情等着你们，\x01",
            "一定不要泄气，加油干哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C3")

    Jump("loc_2518")

    label("loc_24C6")


    ChrTalk(
        0xFE,
        (
            "今后还会有很多事情等着你们，\x01",
            "一定不要泄气，加油干哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2518")

    Jump("loc_2F8C")

    label("loc_251B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0A")
    TurnDirection(0xFE, 0x103, 0)
    OP_A2(0x360)
    OP_A2(0x2)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "#850F很久不见了，雪拉扎德前辈。\x01",
            "自从您去修行之后就再没见面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F这不是亚妮拉丝吗。\x01",
            "真的是很久没见了呢。\x02\x03",
            "对了，\x01",
            "你已经找到所谓的剑之道了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#819F呵呵，请别问了。\x01",
            "我还处在修行阶段呢。\x02\x03",
            "#817F在没有确凿证据的情况下，\x01",
            "王国军居然把游击士抓进监狱……\x02\x03",
            "#818F那个胡子将军也真是的，\x01",
            "他到底在想些什么呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F算了，\x01",
            "反正那也是一场误会罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810F呵呵，\x01",
            "总之大家没事就好了。\x02\x03",
            "有件事我想问问……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "听说前辈您带的两个新人\x01",
            "好像是卡西乌斯先生的孩子，\x01",
            "是不是呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F啊，是的。\x01",
            "我叫艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0x102,
        (
            "#010F我叫约修亚。\x01",
            "我其实是卡西乌斯先生收养的儿子。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "#818F啊，原来如此……\x01",
            "就是你们两个啊～\x02\x03",
            "本来我以为你们年纪太小，\x01",
            "是不会成为什么厉害的游击士的……\x02\x03",
            "#811F这次亲眼看到你们，\x01",
            "才感到你们的未来\x01",
            "真是无可限量呀～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F（……这个人\x01",
            "　果然也知道老爸的事情。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（嗯，应该是这样。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F8C")

    label("loc_2A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EDB")
    OP_A2(0x2)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "#810F雪拉扎德前辈，真是一场灾难啊。\x02\x03",
            "#817F在没有确凿证据的情况下，\x01",
            "王国军居然把游击士抓进监狱……\x02\x03",
            "#818F那个胡子将军也真是的，\x01",
            "他到底在想些什么呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F算了，\x01",
            "反正那也是一场误会罢了。\x02\x03",
            "#020F说起来，\x01",
            "听说是你去通知的市长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810F啊，对，是我。\x02\x03",
            "正好那时我有任务在身，\x01",
            "碰巧就在那村子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F哈哈，给你添麻烦了，\x01",
            "真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810F呵呵，前辈您就别这么客气啦。\x02\x03",
            "有件事我想问问……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "听说前辈您带的两个新人\x01",
            "是卡西乌斯先生的孩子，\x01",
            "有没有这回事呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F啊，是的。\x01",
            "我叫艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0x102,
        (
            "#010F我叫约修亚。\x01",
            "我其实是卡西乌斯先生的养子。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "#818F啊，原来如此……\x01",
            "就是你们两个啊～\x02\x03",
            "本来我以为你们年纪太小，\x01",
            "是不会成为什么厉害的游击士的……\x02\x03",
            "#811F这次亲眼看到你们，\x01",
            "才感到你们的未来\x01",
            "真是无可限量呀～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F（……这个人\x01",
            "　果然也知道老爸的事情。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（嗯，应该是这样。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F8C")

    label("loc_2EDB")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "#810F你们是卡西乌斯先生的孩子吧。\x01",
            "本来我以为你们年纪太小，\x01",
            "是不会成为什么厉害的游击士的……\x02\x03",
            "#811F这次亲眼看到你们，\x01",
            "才感到你们的未来\x01",
            "真是无可限量呀～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8C")

    TalkEnd(0xA)
    Return()

    # Function_7_234C end

    def Function_8_2F90(): pass

    label("Function_8_2F90")

    EventBegin(0x0)
    SetChrPos(0x101, -1120, 0, -4740, 0)
    SetChrPos(0x102, 22, 0, -4880, 0)
    SetChrPos(0x103, -57, 0, -3932, 0)

    def lambda_2FCB():
        OP_6D(0, 0, 2800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2FCB)
    Sleep(2000)
    OP_4A(0x8, 0)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#633F噢，雪拉扎德。\x01",
            "你比我预想中来得要早啊。\x02\x03",
            "特地从洛连特走路过来，\x01",
            "真是辛苦你了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3079():
        OP_8E(0x103, 0xFFFFFE2A, 0x0, 0x776, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3079)
    Sleep(500)

    def lambda_3099():
        OP_8E(0x101, 0xFFFFFBA0, 0x0, 0x2C6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3099)
    Sleep(500)

    def lambda_30B9():
        OP_8E(0x102, 0x16, 0x0, 0x2C6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30B9)
    WaitChrThread(0x103, 0x1)

    ChrTalk(
        0x103,
        (
            "#020F#2P卢格兰爷爷，好久不见了。\x02\x03",
            "难道说您已经\x01",
            "收到我们要来的通知了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630F嗯，早些时候爱娜通知我了。\x02\x03",
            "那么，那边的小姑娘和小兄弟\x01",
            "就是卡西乌斯的孩子吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F#2P是的，正如您所说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#3P嗯，初次见面。\x01",
            "我是艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我是约修亚·布莱特。\x01",
            "请您多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#631F我是柏斯支部的负责人，\x01",
            "叫做卢格兰的老头子。\x02\x03",
            "其实我和你们的父亲\x01",
            "也算是交情颇深哦。\x02\x03",
            "你们就叫我卢格兰爷爷吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#3P嗯，卢格兰爷爷。\x02\x03",
            "#002F那么……\x01",
            "请您赶快告诉我们那个事件\x01",
            "到底是怎么一回事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#632F嗯，事情是这样的……\x02\x03",
            "国王军对失踪定期船的搜索行动\x01",
            "目前还在进行当中。\x02\x03",
            "#634F但是由于军队实行情报控制，\x01",
            "至今没有半点儿消息传出来。\x02\x03",
            "一般的市民也就算了，\x01",
            "连游击士协会也得不到任何消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#3P哎～！？\x02\x03",
            "怎么回事啊，\x01",
            "军队不是和游击士协会有合作关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F#2P唉，那只不过是表面的政策而已。\x02\x03",
            "事实上，在很多情况下，\x01",
            "还是双方对立的局面比较多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F也就是说，在互相争夺势力范围吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#632F虽然很遗憾，但事实如此。\x02\x03",
            "而且更麻烦的是，\x01",
            "这次事件是由摩尔根将军来负责的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#023F#2P啊，摩尔根将军……\x01",
            "这下子事情可不好办了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#3P什么，那个摩尔根将军是谁啊？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F他可是十年前击退帝国军的功臣，\x01",
            "是个赫赫有名的人物。\x02\x03",
            "在历史书里不是也出现过吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F#3P唔……\x01",
            "好像完全没有印象呢。\x02\x03",
            "#002F不过，那位将军究竟有什么问题呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#025F#2P据说那位将军……\x01",
            "非常地讨厌游击士。\x02\x03",
            "而且他一直在主张\x01",
            "游击士协会没有存在的必要。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#009F#3P真、真是个不讲道理的大叔～\x02\x03",
            "那么说，就是那个将军\x01",
            "害我们一点情报都得不到吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#634F……也不能那么说。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "#632F因为军队进行调查的地方\x01",
            "是不能让无关人员进入的。\x02\x03",
            "所以说，\x01",
            "就算是其它工作也没办法顺利进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#3P怎，怎么这样……\x01",
            "好不容易才从洛连特来到这里……\x02\x03",
            "既然这样，我要和那个将军一决胜负，\x01",
            "决定到底由谁来调查这个事件！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F你千万不要乱来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630F好了，不用那么心急。\x02\x03",
            "其实，关于这个事件，\x01",
            "支部收到了来自柏斯市长的委托。\x02\x03",
            "市长希望在军队搜索定期船的同时，\x01",
            "游击士协会也能够参与调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#2P真的？这下我就放心了。\x02\x03",
            "有了柏斯市长的正式委托书，\x01",
            "我们的行动就有正当的理由了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#3P真的吗，这还真是场及时雨啊。\x02\x03",
            "卢格兰爷爷。\x01",
            "我们能接受那个委托吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#634F嗯，当然可以。\x02\x03",
            "#630F不过在那之前……\x01",
            "你们已经是准游击士了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#3P嗯，有什么问题吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630F作为准游击士，\x01",
            "必须在各个支部进行实习。\x02\x03",
            "也就是说，\x01",
            "是受所属支部监督的身份。\x02\x03",
            "你们现在还是\x01",
            "隶属于洛连特支部的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#3P这么说的话……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是不是想接受这个委托，\x01",
            "就必须变更所属的支部才行呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#630F正是如此。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x5A9, 0x0, 0x1072, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x8,
        (
            "#630F来，你们两个。\x01",
            "在这份转属手续的文件上签字吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#3P哦，好的……\x02",
    )

    CloseMessageWindow()

    def lambda_3FE5():
        OP_8E(0xFE, 0x6AE, 0x0, 0x910, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FE5)
    Sleep(500)

    def lambda_4005():
        OP_6D(2210, 0, 3140, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4005)
    OP_8E(0x101, 0xFFFFFE34, 0x0, 0x37A, 0xBB8, 0x0)
    OP_8E(0x101, 0x366, 0x0, 0x8FC, 0xBB8, 0x0)

    def lambda_4045():
        TurnDirection(0x103, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4045)
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)
    Sleep(500)

    ChrTalk(
        0x102,
        "#010F#4P在这里填入名字就可以了吧……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚\x01",
            "在转属手续的文书上签了字。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#630F嗯，这就行了。\x02\x03",
            "游击士艾丝蒂尔，以及约修亚。\x02\x03",
            "以上两人于本日１５：２０\x01",
            "正式成为柏斯支部所属的游击士。\x02\x03",
            "#631F……这样一来，\x01",
            "你们就是柏斯支部的游击士了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F顺便说一下，一旦成为正游击士，\x01",
            "即使没有隶属关系也可以接受工作。\x02\x03",
            "当然相应的责任和义务也就增多了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        "#010F#4P原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#4P我们还是矮人一截啊……\x02",
    )

    CloseMessageWindow()

    def lambda_4300():
        OP_6D(490, 0, 3220, 1000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4300)
    OP_8E(0x8, 0xBA, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x8,
        (
            "#630F这样一来，\x01",
            "市长的委托就可以交托给你们了。\x02\x03",
            "市长官邸坐落在西面入口附近。\x01",
            "你们就去打听一下消息吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(
        0x101,
        "#006F嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F明白了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x52, 0x3, 0x2)
    OP_28(0x52, 0x3, 0x4)
    OP_28(0x35, 0x4, 0x2)
    OP_28(0x35, 0x4, 0x4)
    OP_28(0x35, 0x1, 0x1)
    OP_28(0x35, 0x1, 0x2)
    OP_28(0x35, 0x1, 0x4)
    OP_4B(0x8, 0)
    EventEnd(0x0)
    Return()

    # Function_8_2F90 end

    def Function_9_4452(): pass

    label("Function_9_4452")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, -710, 0, -80, 45)
    SetChrPos(0xC, -1790, 0, -290, 45)
    SetChrPos(0x101, 500, 0, 2000, 225)
    SetChrPos(0x102, -910, 0, 2000, 180)
    SetChrPos(0x103, 1580, 0, 1390, 225)
    SetChrPos(0x104, 1700, 0, 190, 270)
    OP_6D(830, 0, 5070, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_6D(830, 0, 2120, 2000)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#611F#4P——真是辛苦你们了。\x02\x03",
            "我就相信自己不会看错人。\x01",
            "你们真不愧为一流的游击士。\x02\x03",
            "由你们来出马的话，\x01",
            "一定可以把问题妥善解决。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#5P可是可是，\x01",
            "最后好处都被军队给占光了。\x02\x03",
            "根本不算是我们解决的呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#610F#4P才不是那回事呢。\x02\x03",
            "假如没有大家的帮忙，\x01",
            "军队也不会那么顺利地突入。\x02\x03",
            "而且，搞不好会让\x01",
            "那些反抗的空贼伤害人质。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#631F嗯，你们的潜入的确为\x01",
            "压制空贼基地起了很大作用。\x02\x03",
            "你们应该引以为傲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#5P是吗……嘿嘿。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F的确顺利解救了人质，\x01",
            "也逮捕了空贼团一伙人……\x02\x03",
            "遗憾的是，\x01",
            "还有几个遗留下来的谜团没有解开。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#1P是在湖畔出现的男人，\x01",
            "还有空贼首领奇怪的态度吧。\x02\x03",
            "这起事件，\x01",
            "似乎还隐藏着一些不为人知的内幕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#632F也是啊……\x01",
            "不过那些问题也只能交给王国军处理了。\x02\x03",
            "那些空贼已经被关押起来了，\x01",
            "所以我们也无法做深入的调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#610F#4P总之，所有人质平安获救，\x01",
            "这已经是万幸的事情了。\x02\x03",
            "多亏了逮捕空贼的新闻，\x01",
            "现在城市又重新恢复活力了。\x02\x03",
            "我代表柏斯市民由衷感谢你们，\x01",
            "请接受我们小小的谢礼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#5P咦，这样好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#611F#4P呵呵，当然可以了。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0xB, 90, 200)

    ChrTalk(
        0xB,
        (
            "#610F#4P还有奥利维尔先生……\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#2P呵呵……\x01",
            "这就作为我不小心喝掉\x01",
            "『格兰·夏利拿』的补偿好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#611F#4P是啊，还有找零呢。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0xB, 45, 200)

    ChrTalk(
        0xB,
        (
            "#611F#4P那么各位，请保重了。\x01",
            "再有什么事的话还请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#621F#6P……我们告辞了。\x02",
    )

    CloseMessageWindow()

    def lambda_4CF4():

        label("loc_4CF4")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_4CF4")

    QueueWorkItem2(0x101, 1, lambda_4CF4)

    def lambda_4D05():

        label("loc_4D05")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_4D05")

    QueueWorkItem2(0x102, 1, lambda_4D05)

    def lambda_4D16():

        label("loc_4D16")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_4D16")

    QueueWorkItem2(0x103, 1, lambda_4D16)

    def lambda_4D27():

        label("loc_4D27")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_4D27")

    QueueWorkItem2(0x104, 1, lambda_4D27)
    OP_8C(0xB, 180, 400)

    def lambda_4D3F():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFDEE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4D3F)
    Sleep(300)
    OP_8C(0xC, 180, 400)

    def lambda_4D66():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFDEE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4D66)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    OP_22(0x6, 0x0, 0x64)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)

    ChrTalk(
        0x101,
        (
            "#008F#5P啊～感觉就像是\x01",
            "一场隆重的表彰仪式呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)

    ChrTalk(
        0x102,
        (
            "#010F#1P如果事件迟迟得不到解决，\x01",
            "贸易流通必定变得更加混乱。\x02\x03",
            "市长这么高兴也是理所当然的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        (
            "#001F#5P嘿嘿，我也觉得非常开心呢。\x02\x03",
            "靠我们的努力能\x01",
            "帮到大家的忙、让大家开心，\x01",
            "也算是尽到了游击士的职责呢⊙\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F53():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4F53)
    OP_8C(0x103, 270, 400)

    ChrTalk(
        0x103,
        (
            "#027F呵呵，还太嫩了。\x02\x03",
            "不过呢，\x01",
            "你们已经不算是什么新人了。\x02\x03",
            "坦白说，你们这次的表现很惊人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#008F#5P嘿嘿，真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630F总而言之，\x01",
            "先接受这次事件的评定和报酬吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_508F():
        OP_6D(770, 0, 3160, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_508F)

    def lambda_50A7():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50A7)

    def lambda_50B5():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_50B5)

    def lambda_50C3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50C3)
    TurnDirection(0x101, 0x8, 400)
    WaitChrThread(0x101, 0x3)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x35, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50FA")
    OP_AF(0x1C, 0x35)
    Sleep(100)
    OP_28(0x36, 0x4, 0x10)
    OP_28(0x36, 0x4, 0x20)

    label("loc_50FA")

    OP_AF(0x1C, 0x37)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x38, 0x4, 0x10)
    OP_28(0x38, 0x4, 0x20)
    OP_28(0x39, 0x4, 0x10)
    OP_28(0x39, 0x4, 0x20)
    OP_28(0x39, 0x1, 0x400)

    ChrTalk(
        0x8,
        (
            "#630F市长也说过了，\x01",
            "这次要付给你们很多的酬劳。\x02\x03",
            "#630F还有这个……\x01",
            "是我代表支部给你们的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "正游击士资格的推荐信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x333, 1)

    ChrTalk(
        0x101,
        (
            "#004F#4P这个是……\x01",
            "柏斯支部的推荐信！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#6P这样可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#631F那还用说。\x01",
            "光是凭解决这起事件的功劳，\x01",
            "已经足够让我们支部来推荐你们。\x02\x03",
            "总之你们接受吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#4P谢谢，卢格兰爷爷。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6P为了不愧对这封推荐信，\x01",
            "我们以后也会继续努力的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)

    ChrTalk(
        0x103,
        (
            "#021F#2P呵呵，真是太好了。\x02\x03",
            "如果让卡西乌斯老师听到了，\x01",
            "他也一定会很高兴的……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(
        0x101,
        "#003F……唔…………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 135, 400)

    ChrTalk(
        0x102,
        "#013F……是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#634F卡西乌斯……\x01",
            "他现在到底在哪里呢。\x02\x03",
            "协会就先不说了，\x01",
            "没想到连家人也不联系一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#522F#2P是啊……真不像老师的作风。\x02\x03",
            "在柏斯突然下机后，\x01",
            "老师到底去了哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0xD, -800, 0, -8480, 0)

    NpcTalk(
        0xD,
        "青年的声音",
        "#1P打扰了！\x02",
    )

    CloseMessageWindow()

    def lambda_55A4():
        OP_6D(830, 0, 2120, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_55A4)

    def lambda_55BC():

        label("loc_55BC")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_55BC")

    QueueWorkItem2(0x101, 1, lambda_55BC)

    def lambda_55CD():

        label("loc_55CD")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_55CD")

    QueueWorkItem2(0x102, 1, lambda_55CD)

    def lambda_55DE():

        label("loc_55DE")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_55DE")

    QueueWorkItem2(0x103, 1, lambda_55DE)

    def lambda_55EF():

        label("loc_55EF")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_55EF")

    QueueWorkItem2(0x104, 1, lambda_55EF)
    ClearChrFlags(0xD, 0x80)
    OP_8E(0xD, 0xFFFFFDF8, 0x0, 0xFFFFFBDC, 0xBB8, 0x0)

    ChrTalk(
        0x8,
        (
            "#633F空港的接待员……\x02\x03",
            "怎么了，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "是这样的，\x01",
            "被空贼抢走的定期船货物都拿回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "其中有一些是给\x01",
            "游击士协会的邮件和包裹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "请签收一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#631F那真是辛苦你了。\x02\x03",
            "#632F啊，慢着……\x02\x03",
            "从柏斯出发的定期船里\x01",
            "怎么会有给我们支部的东西？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "哎呀，不是呢。\x01",
            "是寄往洛连特支部的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "对了，请问一下\x01",
            "卡西乌斯·布莱特的家属\x01",
            "现在在这里吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#5P哎哎！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F#1P我们就是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "啊，那真是太巧了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "刚才联络洛连特支部的时候，\x01",
            "他们说你们很早就已经来了柏斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "那么，请你们签收吧。\x02",
    )

    CloseMessageWindow()
    OP_92(0xD, 0x101, 0x320, 0xBB8, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "得到了信件和包裹。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0xD, 0x50, 0x0, 0x1AE, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        (
            "#501F#5P这封信……\x01",
            "嗯，是老爸的字呢。\x02\x03",
            "收信人是洛连特支部的\x01",
            "我和约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P看来应该是\x01",
            "在下机之前写好的。\x02\x03",
            "#019F原来如此……\x01",
            "其实父亲也正打算和我们联络的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#5P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F呵呵，真是太好了。\x02\x03",
            "#020F那个包裹也是\x01",
            "老师送来的东西吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#5P唔……\x01",
            "好像是别人送给老爸的东西。\x02\x03",
            "#004F…………………………\x01",
            "……咦，好奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#1P……嗯，\x01",
            "上面没有写寄件人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "你们把邮件收好吧，我告辞了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)

    def lambda_5C0D():

        label("loc_5C0D")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5C0D")

    QueueWorkItem2(0x101, 1, lambda_5C0D)

    def lambda_5C1E():

        label("loc_5C1E")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5C1E")

    QueueWorkItem2(0x102, 1, lambda_5C1E)

    def lambda_5C2F():

        label("loc_5C2F")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5C2F")

    QueueWorkItem2(0x103, 1, lambda_5C2F)

    def lambda_5C40():

        label("loc_5C40")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5C40")

    QueueWorkItem2(0x104, 1, lambda_5C40)
    OP_8E(0xD, 0xFFFFFE5C, 0x0, 0xFFFFFBDC, 0x7D0, 0x0)
    OP_62(0xD, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0xD, 0, 400)

    ChrTalk(
        0xD,
        (
            "啊啊，还有的是，\x01",
            "逮捕空贼那件事真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "真不愧是游击士啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)
    OP_8E(0xD, 0xFFFFFCE0, 0x0, 0xFFFFDEE0, 0xBB8, 0x0)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0xD, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)

    def lambda_5D2D():
        OP_6D(770, 0, 3160, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5D2D)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x8,
        (
            "#630F真没想到定期船的货物里\x01",
            "会有卡西乌斯的线索。\x02\x03",
            "大家如果要看信的话，\x01",
            "就到二楼的休息所吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5DF5():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DF5)

    def lambda_5E03():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E03)

    def lambda_5E11():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E11)
    TurnDirection(0x101, 0x8, 400)
    Sleep(200)

    ChrTalk(
        0x101,
        "#501F谢谢，卢格兰爷爷。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F哈·哈·哈，\x01",
            "那么我们赶快看看这里面的东西吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 10)
    Return()

    # Function_9_4452 end

    def Function_10_5E95(): pass

    label("Function_10_5E95")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 26780, 200, -3520, 270)
    SetChrPos(0x102, 26780, 200, -4800, 270)
    SetChrPos(0x103, 24180, 200, -3500, 90)
    SetChrPos(0x104, 24180, 200, -4700, 90)
    SetChrChipByIndex(0x101, 6)
    SetChrChipByIndex(0x102, 7)
    SetChrChipByIndex(0x103, 8)
    SetChrChipByIndex(0x104, 9)
    SetChrSubChip(0x101, 1)
    OP_6D(26360, 200, -3250, 0)
    OP_67(0, 5820, -10000, 0)
    OP_6B(1730, 0)
    OP_6C(45000, 0)
    OP_6E(459, 0)
    ClearChrFlags(0xE, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#007F#5P……真是的，\x01",
            "为什么你也要跟着过来啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#6P哎呀，纯粹是感兴趣嘛。\x02\x03",
            "比如你们的父亲\x01",
            "为什么会在出发前下机……\x02\x03",
            "又为什么要送这东西过来，\x01",
            "我简直好奇得连觉也睡不着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#5P就、就算你说这种话也……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#034F#6P啊啊，你怎么能对一个曾经\x01",
            "出生入死的同伴如此薄情寡意……\x02\x03",
            "能成功潜入基地\x01",
            "到底是多亏了谁～～呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#5P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#027F真是个爱记旧帐的坏男人啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F真没办法……\x02\x03",
            "#012F不过，看过内容后，\x01",
            "请你谨记不能说出去哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#031F#6P呵呵，这是当然的啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#5P哈啊，先做一下深呼吸……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔先把信封打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_1F(0x50, 0x12C)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "致艾丝蒂尔、约修亚：\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "交给你们的工作\x01",
            "也差不多快完成了吧？\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "起初可能忽略工作上的细节，\x01",
            "但只要一步一步地积累经验，\x01",
            "我想你们一定能够做得更好的。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我这里的工作\x01",
            "稍微遇到了一些麻烦。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "总之短时间内\x01",
            "大概是不能回家了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "对了……\x01",
            "我想起码要到女王的\x01",
            "诞辰庆典结束之后才能回来吧。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在这里先说声抱歉了。\x01",
            "不过你们也要知道自己\x01",
            "已经到了不用爸爸带着的年龄了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "——在我回来之前，\x01",
            "你们要过怎样的生活，\x01",
            "就由自己来决定吧。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可以继续留在洛连特工作。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "也可以为了得到\x01",
            "正游击士的资格环游王国旅行。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "１６岁是收获的季节啊，\x01",
            "希望你们能过得充实有意义。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好了，先写到这吧。\x01",
            "记得帮我向雪拉扎德\x01",
            "还有爱娜问好哦。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "卡西乌斯·布莱特\x07\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_1F(0x64, 0x12C)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#020F……是老师的文笔呢。\x02\x03",
            "虽然看上去轻松随意，\x01",
            "但却充满了对我们的思念啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#5P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#6P哦，女王诞辰庆典啊。\x02\x03",
            "听这番话的口气，\x01",
            "好像还有一段时间吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F大概两三个月吧。\x02\x03",
            "这段时间，\x01",
            "即使出去旅行都够了……\x02\x03",
            "究竟老师他在哪里，\x01",
            "现在又在做些什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#6P先不说这个……\x01",
            "那个包裹装着什么东西呢？\x02\x03",
            "没有写寄件人，\x01",
            "的确是太耐人寻味了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#5P哈哈，的确很让人在意。\x02\x03",
            "不过随便乱动\x01",
            "老爸的东西会不会有点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#6P但是你仔细想想嘛。\x02\x03",
            "在父亲失踪的同时，\x01",
            "收到一个寄件人不明的包裹。\x02\x03",
            "这之间或许有什么关联哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#5P这、这倒是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F喂喂，奥利维尔……\x02\x03",
            "你怎么能为了自己的好奇心\x01",
            "而找诸多的借口怂恿别人呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F不，我觉得奥利维尔说的\x01",
            "确实也有他的道理。\x02\x03",
            "就这样一直放到\x01",
            "父亲回来才打开的话……\x02\x03",
            "我觉得还是先打开看看比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#5P………………………………\x02\x03",
            "#006F明白了，打开看看吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x102, 2)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔打开寄件人不明的包裹。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x5DC)
    Fade(1000)
    SetChrPos(0xE, 25190, 750, -3960, 0)
    SetChrSubChip(0xE, 16)
    OP_0D()
    OP_AD(0x4001F, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "包裹里装着一个\x01",
            "闪着漆黑色光泽的半球体状的装置。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "同时还附有一张纸条。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    OP_1D(0x21)
    Sleep(1000)
    OP_3E(0x35B, 1)

    ChrTalk(
        0x101,
        "#004F#5P这、这个是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是导力器。\x01",
            "虽然用途还不清楚。\x02\x03",
            "有张纸条……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是那个集团运来的物品，\x01",
            "麻烦暂时保管一下。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "找到机会的话，\x01",
            "希望能送给Ｒ博士进行解析。　　Ｋ\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#580F#5P就、就这些？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F嗯……\x01",
            "没写其他的。\x02\x03",
            "#012F雪拉姐姐。\x01",
            "这里所写的Ｋ和Ｒ博士，\x01",
            "你觉得这两个是什么人呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F唔……\x01",
            "很遗憾我并不清楚。\x02\x03",
            "老师的人面非常广，\x01",
            "这两个人有可能是外国人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#5P暗示只有这么一点，\x01",
            "的确让人摸不着头脑。\x02\x03",
            "#505F这个黑色的\x01",
            "导力器到底是什么东西呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F从形状来判断的话，\x01",
            "不像是一般的导力器。\x02\x03",
            "感觉有点像\x01",
            "战术导力器一类的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#032F#6P不，应该不是的。\x02\x03",
            "一般的战术导力器都会有\x01",
            "用来镶嵌结晶回路的结晶孔……\x01",
            "　\x02\x03",
            "但是，这个什么也没有。\x02\x03",
            "这个难道是……\x01",
            "传说中的『古代遗物』？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#5P古代遗物？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#6P就是我们现在\x01",
            "所用的导力器的原型。\x01",
            "换句话说，是古代文明的导力器。\x02\x03",
            "从遗迹发掘出的古代遗物极为珍稀，\x01",
            "而且大多数是由七耀教会保管的。\x02\x03",
            "通俗点说，也就是古董了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F不过这个看上去\x01",
            "并不像十分古老的东西。\x02\x03",
            "反而比较像最近才制造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#6P确实是……\x02\x03",
            "不过……\x01",
            "可以肯定的是这不是什么简单的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#582F#5P#3S啊～真受不了！\x01",
            "那个乱来的老爸！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#582F#5P#3S真是的！\x01",
            "总是让我们操心！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F艾、艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#5P竟然送来这种\x01",
            "寄件人不明的奇怪东西……\x02\x03",
            "老爸到底卷入了\x01",
            "什么样的事件里呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#522F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F…………………………\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()

    ChrTalk(
        0x102,
        (
            "#010F我说，艾丝蒂尔。\x01",
            "我有一个提议……\x02\x03",
            "我们就这样继续旅行下去吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x101, 1)

    ChrTalk(
        0x101,
        "#004F#5P……哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F约修亚？\x02",
    )

    CloseMessageWindow()
    OP_1D(0x58)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#010F父亲的信不是\x01",
            "已经写得很清楚了吗。\x02\x03",
            "『也可以为了得到\x01",
            "正游击士的资格环游王国旅行』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#5P嗯、嗯……\x01",
            "的确是这样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们已经得到了\x01",
            "洛连特和柏斯的推荐信了。\x02\x03",
            "剩下的有卢安、蔡斯和王都格兰赛尔\x01",
            "这三个地方。\x02\x03",
            "一边做协会的工作，\x01",
            "一边在这些地方旅行的话……\x02\x03",
            "说不定……\x01",
            "能找到父亲的行踪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F想到父亲的实力，\x01",
            "就觉得担心都是多余的……\x02\x03",
            "而且他有可能\x01",
            "去了外国执行任务……\x02\x03",
            "#010F与其在这里等待，\x01",
            "我觉得还不如做点实际的事情。\x02\x03",
            "而且……\x01",
            "我们也许还能找到那个叫Ｒ博士的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#5P……………………………\x02\x03",
            "……喂……约修亚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F什么?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0x101, 26826, 0, -3385, 180)
    SetChrSubChip(0x101, 0)
    OP_96(0x101, 0x6856, 0x0, 0xFFFFEFCA, 0x2BC, 0xFA0)
    SetChrSubChip(0x101, 2)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_22(0x7D, 0x0, 0x64)

    ChrTalk(
        0x101,
        "#001F#5P#5S约修亚真是个天才！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x102,
        "#014F艾、艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5P这真是一石二鸟的想法，\x01",
            "不不，简直是十鸟呢～！\x02\x03",
            "啊～我已经不烦恼了，\x01",
            "而且头脑也清醒多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么……\x01",
            "你是赞成的了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#5P赞成，赞成，非常赞成！\x02\x03",
            "#001F一边做游击士的修行，\x01",
            "一边环游利贝尔王国……\x02\x03",
            "顺便还要调查一下\x01",
            "那个不良中年到底在干什么！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F那个……\x01",
            "好像有点偏离目标了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F呵呵……\x01",
            "好像完全恢复精神了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#031F#6P呵呵，总算解决了一件事呢。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_5E95 end

    SaveToFile()

Try(main)
