from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1230   ._SN',
        MapName             = 'Bose',
        Location            = 'T1230.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '阿波尔',                               # 9
        '莉莫奈',                               # 10
        '罗亚',                                 # 11
        '贝斯卡',                               # 12
        '梅洛涅',                               # 13
        '亚妮拉丝',                             # 14
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
        'ED6_DT07/CH01150 ._CH',             # 00
        'ED6_DT07/CH01050 ._CH',             # 01
        'ED6_DT07/CH01123 ._CH',             # 02
        'ED6_DT07/CH01023 ._CH',             # 03
        'ED6_DT07/CH01143 ._CH',             # 04
        'ED6_DT07/CH01033 ._CH',             # 05
        'ED6_DT07/CH01630 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01150P._CP',             # 00
        'ED6_DT07/CH01050P._CP',             # 01
        'ED6_DT07/CH01123P._CP',             # 02
        'ED6_DT07/CH01023P._CP',             # 03
        'ED6_DT07/CH01143P._CP',             # 04
        'ED6_DT07/CH01033P._CP',             # 05
        'ED6_DT07/CH01630P._CP',             # 06
    )

    DeclNpc(
        X                   = -730,
        Z                   = 0,
        Y                   = 5300,
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
        X                   = 440,
        Z                   = 0,
        Y                   = 32439,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -960,
        Z                   = 270,
        Y                   = 34690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -1680,
        Z                   = 270,
        Y                   = 32310,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -1660,
        Z                   = 300,
        Y                   = 31080,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -700,
        Z                   = 0,
        Y                   = 35300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    DeclActor(
        TriggerX            = -780,
        TriggerZ            = 0,
        TriggerY            = 4190,
        TriggerRange        = 400,
        ActorX              = -700,
        ActorZ              = 1500,
        ActorY              = 5300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1500,
        TriggerZ            = 0,
        TriggerY            = 31600,
        TriggerRange        = 400,
        ActorX              = 440,
        ActorZ              = 1500,
        ActorY              = 32439,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1EA",          # 00, 0
        "Function_1_248",          # 01, 1
        "Function_2_280",          # 02, 2
        "Function_3_296",          # 03, 3
        "Function_4_313",          # 04, 4
        "Function_5_ABD",          # 05, 5
        "Function_6_AC2",          # 06, 6
        "Function_7_137C",         # 07, 7
        "Function_8_147E",         # 08, 8
        "Function_9_164F",         # 09, 9
        "Function_10_16E7",        # 0A, 10
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1F4")
    Jump("loc_247")

    label("loc_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_212")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x10)
    Jump("loc_247")

    label("loc_212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_221")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_247")

    label("loc_221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_22B")
    Jump("loc_247")

    label("loc_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247")
    SetChrPos(0x9, 1360, 0, 38700, 45)
    Jump("loc_247")

    label("loc_247")

    Return()

    # Function_0_1EA end

    def Function_1_248(): pass

    label("Function_1_248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_252")
    Jump("loc_27F")

    label("loc_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_25C")
    Jump("loc_27F")

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_266")
    Jump("loc_27F")

    label("loc_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_270")
    Jump("loc_27F")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F")
    OP_64(0x1, 0x1)
    Jump("loc_27F")

    label("loc_27F")

    Return()

    # Function_1_248 end

    def Function_2_280(): pass

    label("Function_2_280")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_295")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_280")

    label("loc_295")

    Return()

    # Function_2_280 end

    def Function_3_296(): pass

    label("Function_3_296")

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
            "休息\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F6")
    OP_0D()
    OP_A9(0xF)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_2F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_307")
    TalkEnd(0x8)
    Return()

    label("loc_307")

    Call(0, 4)
    OP_8C(0x8, 180, 0)
    Return()

    # Function_3_296 end

    def Function_4_313(): pass

    label("Function_4_313")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_390")

    ChrTalk(
        0x8,
        (
            "我能够与莉莫奈一起\x01",
            "开这家店真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "我要更加更加努力才行……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB9")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_434")

    ChrTalk(
        0x8,
        (
            "上午莉莫奈会来\x01",
            "帮我打扫客房。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "晚上，酒馆很挤的时候，\x01",
            "我也会去帮莉莫奈的忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB9")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4C4")

    ChrTalk(
        0x8,
        (
            "莉莫奈一个人\x01",
            "在酒馆那边没问题吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "要是她忙不过来的话，\x01",
            "我一定要去帮忙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB9")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_627")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EE")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "虽然我是个很内向的人，\x01",
            "但是我非常喜欢这项工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "有各种各样的人来访，\x01",
            "让我增加了许多见识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我觉得这里\x01",
            "真的非常温馨呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在这里住过一次的人\x01",
            "再次来到这里住宿时，\x01",
            "我会觉得更加开心……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_624")

    label("loc_5EE")


    ChrTalk(
        0x8,
        (
            "虽然我是个很内向的人，\x01",
            "但是我非常喜欢这项工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_624")

    Jump("loc_AB9")

    label("loc_627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_9DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_972")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "在这个村里，\x01",
            "特别是水果成熟的季节，\x01",
            "人们都会来果树园体验采摘水果哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(
        0x101,
        (
            "#508F约修亚，可以体验摘水果呢！\x02\x03",
            "#001F我想玩～我想摘～我想吃！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#018F真是的，你啊……\x02\x03",
            "#010F但是，现在离那个季节\x01",
            "好像还早了一点吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 0)

    ChrTalk(
        0x8,
        (
            "是、是啊。\x01",
            "好像还要过好几个月。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F啊～真扫兴……\x02\x03",
            "#001F等到水果成熟的季节，\x01",
            "我们再来吧？\x02\x03",
            "下次等没有工作的时候再来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是是。\x02\x03",
            "你在柏斯也说过这些话吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "呵呵呵……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9DC")

    label("loc_972")


    ChrTalk(
        0x8,
        (
            "在这个村里，\x01",
            "特别是水果成熟的季节，\x01",
            "人们都会来果树园体验采摘水果哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DC")

    Jump("loc_AB9")

    label("loc_9DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_A79")

    ChrTalk(
        0x8,
        "那、那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我、我推荐你们去尝尝\x01",
            "二楼酒场的鲜榨果汁，很不错的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "可以的话，\x01",
            "请客人务必去品尝一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB9")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_AB9")

    ChrTalk(
        0x8,
        "啊，欢、欢迎光临……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那个……你们要投宿吗？\x02",
    )

    CloseMessageWindow()

    label("loc_AB9")

    TalkEnd(0x8)
    Return()

    # Function_4_313 end

    def Function_5_ABD(): pass

    label("Function_5_ABD")

    Call(0, 6)
    Return()

    # Function_5_ABD end

    def Function_6_AC2(): pass

    label("Function_6_AC2")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_B3A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B29")
    OP_0D()
    OP_A9(0x16)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_B29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B3A")
    TalkEnd(0x9)
    Return()

    label("loc_B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_BF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB6")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "现在店里有\x01",
            "用刚摘下来的新鲜水果\x01",
            "榨出来的果汁哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "来一杯吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BED")

    label("loc_BB6")


    ChrTalk(
        0x9,
        (
            "现在店里有\x01",
            "用刚摘下来的新鲜水果\x01",
            "榨出来的果汁哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BED")

    Jump("loc_1378")

    label("loc_BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_CE2")

    ChrTalk(
        0x9,
        (
            "今天好像是\x01",
            "村里集会的日子吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "村长早上来的时候，\x01",
            "一幅非常烦恼的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这么忧虑，\x01",
            "希望不要弄坏身子才好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1378")

    label("loc_CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_D49")

    ChrTalk(
        0x9,
        (
            "今、今天\x01",
            "客人真是多啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "阿波尔～……\x01",
            "来帮帮我吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1378")

    label("loc_D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_E4F")

    ChrTalk(
        0x9,
        (
            "这家店是我和\x01",
            "青梅竹马的阿波尔一起开的哦。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "当然是我邀请她的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那个孩子本来很害羞的，\x01",
            "我原以为她不适合干这个的，\x01",
            "没想到她越做越起劲呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1378")

    label("loc_E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_EE1")

    ChrTalk(
        0x9,
        (
            "唔，菜单里是不是应该再\x01",
            "增加一些用水果制成的小点心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "等会儿和阿波尔商量一下吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1378")

    label("loc_EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1297")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "本店的招牌可是各式的果实酒哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "之所以称得上招牌，\x01",
            "是因为我们所采用的原材料都是最新鲜的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F啊呀，听起来很不错……\x01",
            "以前没有这家店的吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 0)

    ChrTalk(
        0x9,
        (
            "是啊，我们这家店是最近才开的。\x01",
            "以后也请多多关照哦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F现在有什么好吃的菜\x01",
            "可以推荐给我们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "有呢～今天的特色菜点\x01",
            "是石榴酒和杏子水果馅饼套餐。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 0)

    ChrTalk(
        0x101,
        (
            "#509F我说雪拉姐啊，\x01",
            "今天不是以调查为首要任务吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(
        0x103,
        (
            "#020F我知道啊。\x02\x03",
            "像这样和当地人聊天\x01",
            "也可以得到很多信息嘛。\x02\x03",
            "#020F不要着急，不要着急。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F唔～\x01",
            "我们真的是在认真调查吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 0)

    ChrTalk(
        0x102,
        (
            "#019F哈哈，一碰到酒，\x01",
            "雪拉姐姐就控制不住自己了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FE")

    label("loc_1297")


    ChrTalk(
        0x9,
        (
            "多吃点多喝点，\x01",
            "累了的话可以到下面的旅馆放松一下㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FE")

    Jump("loc_1378")

    label("loc_1301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1378")

    ChrTalk(
        0x9,
        "啊呀，是客人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "非常抱歉～\x01",
            "现在我们还在准备之中。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1378")

    TalkEnd(0x9)
    Return()

    # Function_6_AC2 end

    def Function_7_137C(): pass

    label("Function_7_137C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142A")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "这两天，\x01",
            "村长准备召开集会\x01",
            "讨论栽培的方针。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "如果有进展就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_147A")

    label("loc_142A")


    ChrTalk(
        0xFE,
        (
            "老婆和波波\x01",
            "现在都还好吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也不知道他们\x01",
            "在柏斯城里过得顺心吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_147A")

    TalkEnd(0xA)
    Return()

    # Function_7_137C end

    def Function_8_147E(): pass

    label("Function_8_147E")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1615")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "总是使用\x01",
            "古老的方法也不行吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "优先考虑效率，\x01",
            "使供货能够源源不断，\x01",
            "这种独特想法也是很必要的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里已经结果的树\x01",
            "都比大家的身高要高不少吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这也是我在集会上\x01",
            "打算要提出的内容。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要减少高空的作业，\x01",
            "也就不需要这么多人手了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164B")

    label("loc_1615")


    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "为什么我的提议他不愿意接受呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164B")

    TalkEnd(0xB)
    Return()

    # Function_8_147E end

    def Function_9_164F(): pass

    label("Function_9_164F")

    TalkBegin(0xC)

    ChrTalk(
        0xFE,
        (
            "我很希望库赖爷爷\x01",
            "也能够理解我丈夫的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定会为村子\x01",
            "带来好处的……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_9_164F end

    def Function_10_16E7(): pass

    label("Function_10_16E7")

    TalkBegin(0xD)
    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0C")
    OP_A2(0x360)
    OP_A2(0x6)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "#814F啊，难道……\x01",
            "这不是雪拉扎德前辈吗？\x02\x03",
            "很久不见了啊。\x01",
            "自从您去修行之后就再没见面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F这不是亚妮拉丝吗。\x01",
            "你在这里做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810F嗯～\x01",
            "协会委托我来这边消灭通缉魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是这样啊……\x02\x03",
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
            "#810F说起来，\x01",
            "前辈您也是在执行协会的任务吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F是啊，不过我和你的任务性质不同。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810F是这样啊……\x01",
            "这个地方最近发生很多事呢。\x02\x03",
            "您路上一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6F")

    label("loc_1A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF7")
    OP_A2(0x6)

    ChrTalk(
        0x103,
        "#020F啊，这不是亚妮拉丝吗。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "#814F啊，雪拉扎德前辈……\x02\x03",
            "难道前辈也是\x01",
            "因为工作才来这儿的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#810F咱们都挺忙的呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B6F")

    label("loc_1AF7")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "#810F雪拉扎德前辈，\x01",
            "这个地方最近处于多事之秋。\x02\x03",
            "您路上一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6F")

    TalkEnd(0xD)
    Return()

    # Function_10_16E7 end

    SaveToFile()

Try(main)
