from ED6ScenarioHelper import *

def main():
    # 迷雾峡谷

    CreateScenaFile(
        FileName            = 'C1400   ._SN',
        MapName             = 'Bose',
        Location            = 'C1400.x',
        MapIndex            = 60,
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
    )

    DeclEntryPoint(
        Unknown_00              = -43600,
        Unknown_04              = -140,
        Unknown_08              = 24500,
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
        Unknown_3A              = 60,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10170 ._CH',             # 00
        'ED6_DT09/CH10171 ._CH',             # 01
        'ED6_DT09/CH11170 ._CH',             # 02
        'ED6_DT09/CH11171 ._CH',             # 03
        'ED6_DT09/CH11180 ._CH',             # 04
        'ED6_DT09/CH11181 ._CH',             # 05
        'ED6_DT09/CH11190 ._CH',             # 06
        'ED6_DT09/CH11191 ._CH',             # 07
        'ED6_DT09/CH10840 ._CH',             # 08
        'ED6_DT09/CH10841 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10170P._CP',             # 00
        'ED6_DT09/CH10171P._CP',             # 01
        'ED6_DT09/CH11170P._CP',             # 02
        'ED6_DT09/CH11171P._CP',             # 03
        'ED6_DT09/CH11180P._CP',             # 04
        'ED6_DT09/CH11181P._CP',             # 05
        'ED6_DT09/CH11190P._CP',             # 06
        'ED6_DT09/CH11191P._CP',             # 07
        'ED6_DT09/CH10840P._CP',             # 08
        'ED6_DT09/CH10841P._CP',             # 09
    )

    DeclNpc(
        X                   = -67060,
        Z                   = -50,
        Y                   = 102230,
        Direction           = 143,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -68750,
        Z                   = 50,
        Y                   = 92910,
        Unknown_0C          = 127,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -84390,
        Z                   = -40,
        Y                   = 90590,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -112800,
        Z                   = -50,
        Y                   = 104070,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xBE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -86000,
        Z                   = 2020,
        Y                   = 104050,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -91980,
        Z                   = 2080,
        Y                   = 122080,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -78470,
        Z                   = 4059,
        Y                   = 133110,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -61710,
        Z                   = 4050,
        Y                   = 112490,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -46460,
        Z                   = 4080,
        Y                   = 83320,
        Unknown_0C          = 198,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xC6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -65700,
        Y                   = 200,
        Z                   = 101220,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = -86770,
        TriggerZ            = 100,
        TriggerY            = 113690,
        TriggerRange        = 1500,
        ActorX              = -86770,
        ActorZ              = 1600,
        ActorY              = 113690,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -78820,
        TriggerZ            = 90,
        TriggerY            = 98230,
        TriggerRange        = 1000,
        ActorX              = -78790,
        ActorZ              = 1590,
        ActorY              = 97650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_262",          # 00, 0
        "Function_1_278",          # 01, 1
        "Function_2_2D0",          # 02, 2
        "Function_3_2E6",          # 03, 3
        "Function_4_BF8",          # 04, 4
        "Function_5_EBB",          # 05, 5
    )


    def Function_0_262(): pass

    label("Function_0_262")

    SetMapFlags(0x10)
    OP_11(0xFF, 0xFF, 0xFF, 0x80E8, 0xD2F0, 0x0)
    Return()

    # Function_0_262 end

    def Function_1_278(): pass

    label("Function_1_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_288")
    OP_71(0x0, 0x4)
    OP_64(0x0, 0x1)

    label("loc_288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A")
    OP_6F(0x2, 0)
    Jump("loc_2A1")

    label("loc_29A")

    OP_6F(0x2, 60)

    label("loc_2A1")

    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x16, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_2CF")

    Return()

    # Function_1_278 end

    def Function_2_2D0(): pass

    label("Function_2_2D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2D0")

    label("loc_2E5")

    Return()

    # Function_2_2D0 end

    def Function_3_2E6(): pass

    label("Function_3_2E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D4")
    SetMapFlags(0x8000000)
    OP_28(0x11, 0x1, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x386, 1)"), scpexpr(EXPR_END)), "loc_379")
    OP_71(0x0, 0x4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "熊刺草\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x0, 0x1)
    OP_A2(0x362)
    Jump("loc_3C9")

    label("loc_379")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "熊刺草\x07\x00",
            "发现了，\x01\x07\x00",
            "不过现有的数量太多，不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3C9")

    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_BF7")

    label("loc_3D4")

    OP_28(0x11, 0x1, 0x4)
    SetMapFlags(0x8000000)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -86760, 110, 114850, 180)
    SetChrPos(0x102, -87680, 70, 115430, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_427")
    SetChrPos(0x103, -85440, 180, 115460, 180)

    label("loc_427")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_446")
    SetChrPos(0x104, -86320, 140, 116900, 180)

    label("loc_446")

    OP_69(0x101, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_509")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x386, 1)"), scpexpr(EXPR_END)), "loc_4B9")
    OP_71(0x0, 0x4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "熊刺草\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x0, 0x1)
    OP_A2(0x362)
    Jump("loc_509")

    label("loc_4B9")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "熊刺草\x07\x00",
            "发现了，\x01\x07\x00",
            "不过现有的数量太多，不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_509")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_A4F")

    ChrTalk(
        0x101,
        (
            "#000F呼，终～于找到了。\x02\x03",
            "接下来要做的就是\x01",
            "把这个地方告诉超市的老爷爷。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68C")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#020F那么，艾丝蒂尔，\x01",
            "我问你一下……\x02\x03",
            "你知道这里是什么地方吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿，\x01",
            "雪拉姐的问题真无聊。\x02\x03",
            "『蜜猪峡谷』，对吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73A")

    label("loc_68C")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔，\x01",
            "你知道这个地方叫什么吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#502F真是的，别把我当傻瓜啊。\x02\x03",
            "『蜜猪峡谷』，对吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E1")

    ChrTalk(
        0x102,
        "#015F……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F哦……\x02\x03",
            "不管怎么说\x01",
            "真是个能引起食欲的名字啊。　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔……\x02\x03",
            "这里叫『迷雾峡谷』啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B1")

    label("loc_7E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86C")

    ChrTalk(
        0x102,
        "#015F……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#027F……真是个非常美味的名字啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔……\x02\x03",
            "这里叫『迷雾峡谷』啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B1")

    label("loc_86C")


    ChrTalk(
        0x102,
        (
            "#018F……………………\x02\x03",
            "#018F艾丝蒂尔……\x01",
            "这里叫『迷雾峡谷』啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B1")


    ChrTalk(
        0x101,
        "#008F啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F7")

    ChrTalk(
        0x103,
        "#025F……还好事先问了你一下。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_927")

    label("loc_8F7")


    ChrTalk(
        0x102,
        "#015F……还好事先问了你一下。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    label("loc_927")


    ChrTalk(
        0x101,
        (
            "#009F这、这也是没办法的事情啊，\x01",
            "人家正处于生长发育旺盛的时期嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F这算什么理由啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#008F好、好啦好啦，\x01",
            "我们这是在工作中啊，工作中。\x02\x03",
            "快点出发吧，好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)

    ChrTalk(
        0x102,
        "#017F真拿你没办法……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF0")

    label("loc_A4F")


    ChrTalk(
        0x101,
        (
            "#000F嗯～这是『熊刺草』呢。\x02\x03",
            "说起来……\x01",
            "好像有谁正在找这个东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B40")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#020F不是在公告板上写着的吗？\x02\x03",
            "看看手册里的记载吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_BCD")

    label("loc_B40")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F是在公告板上写着的吧。\x02\x03",
            "看看手册里的记载吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    label("loc_BCD")


    ChrTalk(
        0x101,
        "#006F嗯，好吧。\x02",
    )

    CloseMessageWindow()

    label("loc_BF0")

    EventEnd(0x0)
    ClearMapFlags(0x8000000)

    label("loc_BF7")

    Return()

    # Function_3_2E6 end

    def Function_4_BF8(): pass

    label("Function_4_BF8")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡中。\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_CF0"),
        (SWITCH_DEFAULT, "loc_D8A"),
    )


    label("loc_CF0")

    Fade(1000)
    SetChrPos(0x0, -62850, 1270, 98430, 319)
    SetChrPos(0x1, -62850, 1270, 98430, 319)
    SetChrPos(0x2, -62850, 1270, 98430, 319)
    SetChrPos(0x3, -62850, 1270, 98430, 319)
    SetChrPos(0x4, -62850, 1270, 98430, 319)
    SetChrPos(0x5, -62850, 1270, 98430, 319)
    SetChrPos(0x6, -62850, 1270, 98430, 319)
    SetChrPos(0x7, -62850, 1270, 98430, 319)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_D8A")

    Battle(0x3F8, 0x0, 0x0, 0x0, 0xFF)
    SetChrPos(0x0, -62850, 1270, 98430, 319)
    SetChrPos(0x1, -62850, 1270, 98430, 319)
    SetChrPos(0x2, -62850, 1270, 98430, 319)
    SetChrPos(0x3, -62850, 1270, 98430, 319)
    SetChrPos(0x4, -62850, 1270, 98430, 319)
    SetChrPos(0x5, -62850, 1270, 98430, 319)
    SetChrPos(0x6, -62850, 1270, 98430, 319)
    SetChrPos(0x7, -62850, 1270, 98430, 319)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_E38"),
        (1, "loc_E3B"),
        (SWITCH_DEFAULT, "loc_E3E"),
    )


    label("loc_E38")

    EventEnd(0x0)
    Return()

    label("loc_E3B")

    OP_B4(0x0)
    Return()

    label("loc_E3E")

    EventBegin(0x1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "成功消灭了迷雾峡谷中被通缉的魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x16, 0x4, 0x10)
    OP_28(0x16, 0x1, 0x1)
    OP_A2(0x387)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_4_BF8 end

    def Function_5_EBB(): pass

    label("Function_5_EBB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x22, 1)"), scpexpr(EXPR_END)), "loc_F2E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "拳剑\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x376)
    Jump("loc_F9E")

    label("loc_F2E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "拳剑\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "拳剑\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_F9E")

    Jump("loc_FD3")

    label("loc_FA1")

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
    OP_83(0xF, 0x15)

    label("loc_FD3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_EBB end

    SaveToFile()

Try(main)
