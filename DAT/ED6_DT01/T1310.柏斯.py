from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1310   ._SN',
        MapName             = 'Bose',
        Location            = 'T1310.x',
        MapIndex            = 1,
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
        '赛罗斯副长',                           # 9
        '士兵阿萨',                             # 10
        '赛尔斯特队长',                         # 11
        '亚妮拉丝',                             # 12
        '士兵艾格尔',                           # 13
        '士兵迈奇',                             # 14
        '士兵卡多尔斯',                         # 15
        '器皿',                                 # 16
        '器皿',                                 # 17
        '咖啡',                                 # 18
        '咖啡',                                 # 19
    )

    DeclEntryPoint(
        Unknown_00              = 48000,
        Unknown_04              = -3000,
        Unknown_08              = 27000,
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH01630 ._CH',             # 02
        'ED6_DT07/CH00003 ._CH',             # 03
        'ED6_DT07/CH00013 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
        'ED6_DT06/CH20008 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH01630P._CP',             # 02
        'ED6_DT07/CH00003P._CP',             # 03
        'ED6_DT07/CH00013P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
        'ED6_DT06/CH20008P._CP',             # 07
    )

    DeclNpc(
        X                   = 19990,
        Z                   = 0,
        Y                   = 22490,
        Direction           = 90,
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
        X                   = 22000,
        Z                   = 0,
        Y                   = 9500,
        Direction           = 90,
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
        X                   = 79860,
        Z                   = 0,
        Y                   = 13400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 21900,
        Z                   = 0,
        Y                   = 22100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 19990,
        Z                   = 0,
        Y                   = 7950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 76700,
        Z                   = 0,
        Y                   = 7590,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 25000,
        Z                   = 0,
        Y                   = 10500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65541,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65541,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572869,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572869,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 21950,
        TriggerZ            = 0,
        TriggerY            = 22540,
        TriggerRange        = 400,
        ActorX              = 19990,
        ActorZ              = 1500,
        ActorY              = 22490,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22050,
        TriggerZ            = 0,
        TriggerY            = 7990,
        TriggerRange        = 400,
        ActorX              = 19990,
        ActorZ              = 1500,
        ActorY              = 7950,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18440,
        TriggerZ            = 0,
        TriggerY            = 12120,
        TriggerRange        = 1000,
        ActorX              = 18440,
        ActorZ              = 1000,
        ActorY              = 12120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B6",          # 00, 0
        "Function_1_416",          # 01, 1
        "Function_2_4CD",          # 02, 2
        "Function_3_4E3",          # 03, 3
        "Function_4_4E8",          # 04, 4
        "Function_5_185B",         # 05, 5
        "Function_6_2087",         # 06, 6
        "Function_7_2C81",         # 07, 7
        "Function_8_30C3",         # 08, 8
        "Function_9_30C8",         # 09, 9
        "Function_10_31C5",        # 0A, 10
        "Function_11_34A4",        # 0B, 11
        "Function_12_3D55",        # 0C, 12
        "Function_13_5E8E",        # 0D, 13
        "Function_14_6139",        # 0E, 14
        "Function_15_65F4",        # 0F, 15
        "Function_16_66E1",        # 10, 16
    )


    def Function_0_2B6(): pass

    label("Function_0_2B6")

    OP_82(0x80, 0x0)
    OP_A2(0x36B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_2F7")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xA, 20390, 0, 10700, 180)
    SetChrPos(0xE, 79990, 0, 13380, 0)
    Jump("loc_3C8")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_321")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xA, 20390, 0, 10700, 180)
    Jump("loc_3C8")

    label("loc_321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_34B")
    SetChrPos(0xA, 20390, 0, 10700, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3C8")

    label("loc_34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_364")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_3C8")

    label("loc_364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_378")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3C8")

    label("loc_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_391")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_3C8")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3AA")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    Jump("loc_3C8")

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3BE")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    Jump("loc_3C8")

    label("loc_3BE")

    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3D6")
    OP_A3(0x3FA)
    Event(0, 13)

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_3F6")
    OP_A3(0x3FB)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B1("t1310_n")
    Event(0, 14)

    label("loc_3F6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_402"),
        (SWITCH_DEFAULT, "loc_415"),
    )


    label("loc_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_412")
    Event(0, 12)

    label("loc_412")

    Jump("loc_415")

    label("loc_415")

    Return()

    # Function_0_2B6 end

    def Function_1_416(): pass

    label("Function_1_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42E")
    OP_B1("t1310_y")
    Jump("loc_437")

    label("loc_42E")

    OP_B1("t1310_n")

    label("loc_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_44F")
    OP_1B(0x0, 0x0, 0xF)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 99)

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_45D")
    OP_64(0x1, 0x1)
    Jump("loc_483")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_467")
    Jump("loc_483")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_475")
    OP_64(0x1, 0x1)
    Jump("loc_483")

    label("loc_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_47F")
    Jump("loc_483")

    label("loc_47F")

    OP_64(0x1, 0x1)

    label("loc_483")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_416 end

    def Function_2_4CD(): pass

    label("Function_2_4CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4CD")

    label("loc_4E2")

    Return()

    # Function_2_4CD end

    def Function_3_4E3(): pass

    label("Function_3_4E3")

    Call(0, 4)
    Return()

    # Function_3_4E3 end

    def Function_4_4E8(): pass

    label("Function_4_4E8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_53D")

    ChrTalk(
        0x8,
        (
            "嗯，今天用野菜作为原料，\x01",
            "来挑战新的菜式吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_53D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_5E6")

    ChrTalk(
        0x8,
        (
            "哦……\x01",
            "从卢安订购的鱼好像运过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "今晚就稍微奢侈一下，\x01",
            "给大家振奋一下士气吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_5E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_690")

    ChrTalk(
        0x8,
        (
            "自那以后，\x01",
            "袭击这里的魔兽再也没有出现过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "果然，\x01",
            "不是住在这一带的魔兽呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_71A")

    ChrTalk(
        0x8,
        "哦，你们不就是游击士的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "怎么了，\x01",
            "来这里有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_12FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B5")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_69(0x8, 0x3E8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 6)), scpexpr(EXPR_END)), "loc_78B")

    ChrTalk(
        0x8,
        (
            "啊呀，怎么了。\x01",
            "现在办理通行手续吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCD")

    label("loc_78B")


    ChrTalk(
        0x101,
        "#001F士兵先生，早上好～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦，早啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "昨天真的是\x01",
            "辛苦你们啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嘿嘿，没什么啦。\x02\x03",
            "士兵先生你们呢？\x01",
            "后来巡逻的时候\x01",
            "没有发生什么事情吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "啊啊。\x01",
            "之后一切正常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不过……有一点比较奇怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F奇怪……怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "街道和关所附近的照明设施\x01",
            "有驱赶魔兽的防御效果，\x01",
            "这点你们应该很清楚的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "就算魔兽真的靠近了关所，\x01",
            "充其量也只有两三只。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是昨天却来了一大群，\x01",
            "这种情况我们还是第一次遇到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F这样说来的确是有点奇怪……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呵呵，不过比起那些帝国军，\x01",
            "这些魔兽还算挺可爱的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "就把这次骚动\x01",
            "当成防卫关所的演习好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F这、这样没问题吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "对于我们来说，\x01",
            "帝国那边的动静才是最令人担心的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "至于魔兽之类的，\x01",
            "还是交给你们游击士处理吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么……\x01",
            "你们也该出发了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "现在办理通行手续吗？\x02",
    )

    CloseMessageWindow()

    label("loc_CCD")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【办理通行手续】\x01",      # 0
            "【还是算了】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_D4B"),
        (0, "loc_D8A"),
        (SWITCH_DEFAULT, "loc_11B2"),
    )


    label("loc_D4B")


    ChrTalk(
        0x8,
        (
            "准备好了的话\x01",
            "随时都可以来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x446)
    EventEnd(0x1)
    Jump("loc_11B2")

    label("loc_D8A")


    ChrTalk(
        0x102,
        "#010F是的，麻烦您了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "通往卢安地区的通行手续已经办理完毕。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        "……这样就行了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "然后……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    Sleep(300)

    def lambda_E7A():
        OP_6D(23120, 0, 24400, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E7A)
    WaitChrThread(0x101, 0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "副长操作开关装置。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_70(0x2, 0x64)
    OP_8B(0x0, 0x5A50, 0x5F50, 0x190)
    OP_8B(0x1, 0x5A50, 0x5F50, 0x190)
    OP_73(0x2)

    def lambda_F07():
        TurnDirection(0x8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F07)
    OP_69(0x8, 0x5DC)

    ChrTalk(
        0x8,
        (
            "碧海白花环抱的卢安\x01",
            "欢迎你们的到来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "对了对了，\x01",
            "小姑娘你们是不是打算去卢安市？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FA5():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_FA5)
    TurnDirection(0x1, 0x8, 400)

    ChrTalk(
        0x101,
        "#000F嗯，我们正想去那里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那就麻烦你们把昨天的情况\x01",
            "向卢安的支部报告一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "军队也会支付相应的酬金的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，这样可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呵呵，\x01",
            "这些酬金你们就和阿加特平分吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么后会有期，\x01",
            "期待你们早日成为正游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F承蒙你们多方关照了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x407)
    OP_28(0x3A, 0x4, 0x10)
    OP_28(0x3A, 0x1, 0x4)
    OP_28(0x11, 0x4, 0x40)
    OP_28(0x13, 0x4, 0x40)
    OP_1B(0x0, 0x0, 0xF)
    NewScene("ED6_DT01/T1300   ._SN", 101, 0, 0)
    IdleLoop()

    label("loc_11B2")

    Jump("loc_12F7")

    label("loc_11B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126A")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "啊，是你们啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那就麻烦你们把昨天的情况\x01",
            "向卢安的支部报告一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "去卢安的路上要小心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12F7")

    label("loc_126A")


    ChrTalk(
        0x8,
        (
            "那就麻烦你们把昨天的情况\x01",
            "向卢安的支部报告一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "去卢安的路上要小心。\x02",
    )

    CloseMessageWindow()

    label("loc_12F7")

    Jump("loc_1857")

    label("loc_12FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1368")

    ChrTalk(
        0x8,
        (
            "啊，\x01",
            "这种时间还到这里来啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "外面已经很冷了吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_1368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_156B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CE")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "不管多么习惯旅行在外，\x01",
            "晚上在这一带行走还是非常危险的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "山路崎岖，而且魔兽也多。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "说起来很奇怪的是，\x01",
            "最近经常会看到有首领带领的魔兽群体。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那可是至今为止都没有见过的哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1568")

    label("loc_14CE")


    ChrTalk(
        0x8,
        (
            "最近很奇怪的是，\x01",
            "经常会看到有首领带领的魔兽群体。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那可是至今为止都没有见过的哦。\x02",
    )

    CloseMessageWindow()

    label("loc_1568")

    Jump("loc_1857")

    label("loc_156B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_160C")

    ChrTalk(
        0x8,
        (
            "我有义务\x01",
            "让士兵们平时保持\x01",
            "六个小时以上的睡眠。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "睡眠不足的话，\x01",
            "就无法将自己的实力好好发挥出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_160C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_17C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1724")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "别看我这个样子，\x01",
            "我可以非常喜欢烹饪的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我会经常请求队长，\x01",
            "让我在这里烧菜做饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "顺带一提，\x01",
            "那边有供旅行者专用的房间，\x01",
            "你们可以随时使用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BD")

    label("loc_1724")


    ChrTalk(
        0x8,
        (
            "别看我这个样子，\x01",
            "我可以非常喜欢烹饪的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我会经常请求队长，\x01",
            "让我在这里炒菜做饭。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BD")

    Jump("loc_1857")

    label("loc_17C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1836")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "啊，\x01",
            "小姑娘你们要去卢安吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "要去卢安的话，\x01",
            "必须要有通行许可证……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_1836")


    ChrTalk(
        0x8,
        "啊，你们要去卢安吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1857")

    TalkEnd(0x8)
    Return()

    # Function_4_4E8 end

    def Function_5_185B(): pass

    label("Function_5_185B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_18B6")

    ChrTalk(
        0xFE,
        (
            "堡垒的人最近\x01",
            "总是谈论市长被捕这个话题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_18B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_19F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1970")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "今天本该轮到\x01",
            "我来炒菜做饭了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过刚才副长来，\x01",
            "说要代替我做饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个人，\x01",
            "真的非常喜欢烹饪啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F1")

    label("loc_1970")


    ChrTalk(
        0xFE,
        (
            "刚才副长来了，\x01",
            "说要代替我做饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个人，\x01",
            "真的非常喜欢烹饪啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F1")

    Jump("loc_2083")

    label("loc_19F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1AF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9D")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "自从空贼被逮捕以来，\x01",
            "柏斯地区就非常和平。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，要是接连不断发生事件\x01",
            "那真是很难办啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF0")

    label("loc_1A9D")


    ChrTalk(
        0xFE,
        (
            "自从空贼被逮捕以来，\x01",
            "柏斯地区就非常和平。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF0")

    Jump("loc_2083")

    label("loc_1AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1B87")

    ChrTalk(
        0xFE,
        (
            "之前来的魔兽\x01",
            "比想象中的要厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们也必须\x01",
            "加紧训练才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_1B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_1C24")

    ChrTalk(
        0xFE,
        (
            "昨天的袭击\x01",
            "真是个很好的教训。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来平时\x01",
            "就要做好充分准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_1C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1CBB")

    ChrTalk(
        0xFE,
        (
            "搜索这样持续下去，\x01",
            "国境师团的家伙们也相当累吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "如果有什么新的进展就好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_1CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1D8A")

    ChrTalk(
        0xFE,
        (
            "这一带\x01",
            "越往山中走魔兽越多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且被通缉的魔兽\x01",
            "也越来越多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "每天的训练是必不可少的啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_1D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1F1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E83")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "这座古罗尼连峰的地形\x01",
            "也是起伏频繁的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说不定\x01",
            "空贼团那些家伙们\x01",
            "就藏在这附近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "国境守备队的搜索队\x01",
            "已经来这里调查了很多次了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F17")

    label("loc_1E83")


    ChrTalk(
        0xFE,
        (
            "这座古罗尼连峰\x01",
            "地形也是起伏频繁的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说不定\x01",
            "空贼团那些家伙们\x01",
            "就藏在这附近。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F17")

    Jump("loc_2083")

    label("loc_1F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF7")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "这么险峻的山道，\x01",
            "一般来说旅行的人\x01",
            "是根本不会走的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为现在飞艇还在停航，\x01",
            "急着去卢安和柏斯的人们\x01",
            "不得不从这里通过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_1FF7")


    ChrTalk(
        0xFE,
        (
            "但是不管怎么说，\x01",
            "还是应该尽量避免\x01",
            "在晚上翻越这座山峰啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对一般人来说太危险了。\x02",
    )

    CloseMessageWindow()

    label("loc_2083")

    TalkEnd(0x9)
    Return()

    # Function_5_185B end

    def Function_6_2087(): pass

    label("Function_6_2087")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2120")

    ChrTalk(
        0xFE,
        (
            "市长的所作所为\x01",
            "真的非常令人感到遗憾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么想，\x01",
            "也觉得这件事不可原谅。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_2120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_2354")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2269")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "利贝尔各地的关所\x01",
            "在十年前分裂帝国军时\x01",
            "起到了很大的作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且如今也\x01",
            "作为军事要地被广泛利用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这些地方的守备\x01",
            "绝对不能放松。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2351")

    label("loc_2269")


    ChrTalk(
        0xFE,
        (
            "利贝尔各地的关所\x01",
            "在十年前分裂帝国军时\x01",
            "起到了很大的作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以说，这些地方的守备\x01",
            "绝对不可以放松。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2351")

    Jump("loc_2C7D")

    label("loc_2354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_24EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245E")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "虽然我们士兵是为了\x01",
            "镇守关所才驻守在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过偶尔也会向\x01",
            "一些登山者实行救助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为来古罗尼连峰登山\x01",
            "而遇难的人也有不少呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24EC")

    label("loc_245E")


    ChrTalk(
        0xFE,
        (
            "虽然我们士兵是为了\x01",
            "镇守关所才驻守在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过偶尔也会向\x01",
            "一些登山者实行救助。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24EC")

    Jump("loc_2C7D")

    label("loc_24EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2575")

    ChrTalk(
        0xFE,
        (
            "如果敌人从两个方向发动进攻，\x01",
            "该如何防守呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天训练的议题就是这个了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_2575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_25D5")

    ChrTalk(
        0xFE,
        "哦，要出发了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "路上小心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_25D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_264A")

    ChrTalk(
        0xFE,
        "哦，睡得还好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天你们出手\x01",
            "真是帮了我们大忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_264A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_28C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2864")
    EventBegin(0x0)
    OP_A2(0x404)
    OP_69(0xFE, 0x3E8)

    ChrTalk(
        0xFE,
        "啊，你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F您好，不好意思打扰一下。\x02\x03",
            "其实我们……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人向队长说明情况，\x01",
            "并且请求在关所留宿一晚。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        (
            "哦，没问题。\x01",
            "游击士的身份就是一种保证。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "隔壁的休息室就请随便使用吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F谢谢，队长先生！\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_28BD")

    label("loc_2864")


    ChrTalk(
        0xFE,
        (
            "这里隔壁的休息室\x01",
            "就请随便使用吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "先取个暖如何？\x02",
    )

    CloseMessageWindow()

    label("loc_28BD")

    Jump("loc_2C7D")

    label("loc_28C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_297F")

    ChrTalk(
        0xFE,
        (
            "国境守备队好像\x01",
            "向本部要求增员了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来将军\x01",
            "准备在这几天动手了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_297F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2A35")

    ChrTalk(
        0xFE,
        (
            "嗯，摩尔根将军已经将搜索范围\x01",
            "缩小到北部山区了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "空贼们果然藏在\x01",
            "国境附近的某个地方啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_2A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B75")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "摩尔根将军\x01",
            "发布命令要求强化这一带的警备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "空贼们藏在哪里，\x01",
            "还不是很清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尤其是山林，\x01",
            "那里是他们最好的藏身之处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要赶快通知队里的人，\x01",
            "让他们提高警惕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C14")

    label("loc_2B75")


    ChrTalk(
        0xFE,
        (
            "摩尔根将军\x01",
            "发布命令要求强化这一带的警备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "空贼们藏在哪里，\x01",
            "还不是很清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C14")

    Jump("loc_2C7D")

    label("loc_2C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2C7D")

    ChrTalk(
        0xFE,
        "需要通行许可证的话，我就发给你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "随时来找我好了。\x02",
    )

    CloseMessageWindow()

    label("loc_2C7D")

    TalkEnd(0xA)
    Return()

    # Function_6_2087 end

    def Function_7_2C81(): pass

    label("Function_7_2C81")

    TalkBegin(0xB)
    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F99")
    OP_A2(0x360)
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "#814F啊，难道……\x01",
            "这不是雪拉扎德前辈吗？\x02\x03",
            "#850F很久不见了啊。\x01",
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
            "说起来，\x01",
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
            "#810F是这样啊……\x02\x03",
            "这个地方\x01",
            "最近发生很多事呢。\x02\x03",
            "您路上一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BF")

    label("loc_2F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_304E")
    OP_A2(0x3)

    ChrTalk(
        0x103,
        "#020F啊，这不是亚妮拉丝吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#850F雪拉扎德前辈！\x02\x03",
            "#810F怎么样？\x01",
            "调查进行得顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F嗯，有一点进展了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30BF")

    label("loc_304E")


    ChrTalk(
        0xFE,
        (
            "#810F雪拉扎德前辈，\x01",
            "这个地方最近处于多事之秋。\x02\x03",
            "您路上一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30BF")

    TalkEnd(0xB)
    Return()

    # Function_7_2C81 end

    def Function_8_30C3(): pass

    label("Function_8_30C3")

    Call(0, 9)
    Return()

    # Function_8_30C3 end

    def Function_9_30C8(): pass

    label("Function_9_30C8")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3168")

    ChrTalk(
        0xC,
        "啊呀，你们要去卢安吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "这里可是去柏斯的出口。\x01",
            "要去卢安的话，请从对面出去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C1")

    label("loc_3168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_31C1")

    ChrTalk(
        0xC,
        (
            "这里的海拔比较高，\x01",
            "太阳一落山果然就会很冷啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C1")

    TalkEnd(0xC)
    Return()

    # Function_9_30C8 end

    def Function_10_31C5(): pass

    label("Function_10_31C5")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3241")

    ChrTalk(
        0xFE,
        (
            "听说卢安的市长\x01",
            "被逮捕了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "竟然有这种事情。\x02",
    )

    CloseMessageWindow()
    Jump("loc_34A0")

    label("loc_3241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_32DC")

    ChrTalk(
        0xFE,
        (
            "被魔兽打伤的地方\x01",
            "终于痊愈了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要尽量避免以后再发生这类事情，\x01",
            "所以要加紧训练。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A0")

    label("loc_32DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_336E")

    ChrTalk(
        0xFE,
        "副长还真是喜欢烹饪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有时候明明不是他当班，\x01",
            "但是他却在厨房做饭呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A0")

    label("loc_336E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_340E")

    ChrTalk(
        0xFE,
        "柴火差不多要用完了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "训练结束后去报告一下，\x01",
            "然后就去砍些柴吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A0")

    label("loc_340E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_3446")

    ChrTalk(
        0xFE,
        "痛痛痛痛痛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是失策。\x01",
            "被魔兽打伤的地方好痛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A0")

    label("loc_3446")


    ChrTalk(
        0xFE,
        "一会儿就轮到我值班了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "趁现在赶快吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A0")

    TalkEnd(0xD)
    Return()

    # Function_10_31C5 end

    def Function_11_34A4(): pass

    label("Function_11_34A4")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_350B")

    ChrTalk(
        0xFE,
        (
            "呜呜～虽说已经是这个季节，\x01",
            "山上却还是这么冷啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D51")

    label("loc_350B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_356B")

    ChrTalk(
        0xFE,
        "离值勤还有段时间……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是先\x01",
            "稍微小睡一会儿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D51")

    label("loc_356B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_36F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3690")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "这里是深山老林，\x01",
            "食物的供应非常不方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然也有很多东西\x01",
            "从柏斯和卢安那里运送过来，\x01",
            "不过毕竟是山路啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "经常需要去迎接送货的人，\x01",
            "并且给他们顺便但当护卫。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_3690")


    ChrTalk(
        0xFE,
        (
            "这里一到冬天，\x01",
            "大雪就会堆积起来，特别不方便。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F0")

    Jump("loc_3D51")

    label("loc_36F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3787")

    ChrTalk(
        0xFE,
        "差不多到训练的时间了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为发生过魔兽袭击事件，\x01",
            "大家要提高警惕了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D51")

    label("loc_3787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_38DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3855")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "早上好，昨天谢谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然看上去挺年轻，\x01",
            "但真不愧是游击士呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "干得真棒。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38D9")

    label("loc_3855")


    ChrTalk(
        0xFE,
        (
            "虽然看上去挺年轻，\x01",
            "但真不愧是游击士呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "昨天干得真棒。\x02",
    )

    CloseMessageWindow()

    label("loc_38D9")

    Jump("loc_3D51")

    label("loc_38DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_39A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_395D")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "有什么事吗？\x01",
            "你们可以随便进去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要使用休息室的话，\x01",
            "和我们队长打声招呼就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399D")

    label("loc_395D")


    ChrTalk(
        0xFE,
        (
            "想使用里面的屋子时，\x01",
            "和我们队长打声招呼就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399D")

    Jump("loc_3D51")

    label("loc_39A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC7")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "好像还是找不到\x01",
            "空贼团的所在之处啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "国境守备队的那伙人\x01",
            "最近也经常到这里\x01",
            "来进行调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "柏斯这个地方\x01",
            "就是山岳比较多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "犯人要是隐藏在这里，\x01",
            "可是最难发现的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B41")

    label("loc_3AC7")


    ChrTalk(
        0xFE,
        (
            "柏斯这个地方\x01",
            "就是山岳比较多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "犯人要是隐藏在这里，\x01",
            "可是最难发现的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B41")

    Jump("loc_3D51")

    label("loc_3B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3BF6")

    ChrTalk(
        0xFE,
        (
            "消失的定期船\x01",
            "好像被找到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为犯人还没有被抓住，\x01",
            "所以关所还要继续\x01",
            "维持盘查的制度。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D51")

    label("loc_3BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3CD3")

    ChrTalk(
        0xFE,
        (
            "是空贼团吗……\x01",
            "真是一群不容易对付的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，这次是由那位\x01",
            "摩尔根将军亲临指挥呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "肯定马上就会抓到他们的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D51")

    label("loc_3CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3D51")

    ChrTalk(
        0xFE,
        "现在正处在戒严状态中。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果你们想通行的话，\x01",
            "必须先在里面办手续。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D51")

    TalkEnd(0xE)
    Return()

    # Function_11_34A4 end

    def Function_12_3D55(): pass

    label("Function_12_3D55")

    EventBegin(0x0)
    AddParty(0x5, 0xFF)
    EventBegin(0x0)
    OP_6D(80631, 0, 54990, 0)
    SetChrPos(0x101, 75900, 0, 53900, 90)
    SetChrPos(0x102, 74500, 0, 53000, 90)
    SetChrPos(0x106, 73600, 0, 52570, 90)
    SetChrPos(0x8, 73600, 0, 52570, 90)
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x106, 0x4)
    FadeToBright(1000, 0)

    def lambda_3DD9():
        OP_8E(0xFE, 0x138E4, 0x0, 0xD28C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DD9)

    def lambda_3DF4():
        OP_8E(0xFE, 0x13560, 0x0, 0xCF08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DF4)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#000F这里就是旅行者专用的休息室啊。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F嗯。\x01",
            "我先把暖炉点着吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E82():
        OP_6D(82761, 0, 52570, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3E82)
    OP_8E(0x102, 0x13BA0, 0x0, 0xCF08, 0x7D0, 0x0)

    def lambda_3EAE():
        OP_8E(0xFE, 0x144BF, 0x0, 0xCA1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EAE)
    Sleep(500)

    def lambda_3ECE():
        OP_8E(0xFE, 0x14344, 0x0, 0xCD5E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3ECE)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 90, 400)
    Sleep(1000)
    OP_22(0x86, 0x0, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8E(0x102, 0x14344, 0x0, 0xC83C, 0x7D0, 0x0)
    OP_8C(0x102, 52, 400)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#001F#1P呼～好暖和……\x02\x03",
            "还是烧柴火的暖炉\x01",
            "更让人感到自然和舒服啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x02\x03",
            "虽然导力炉已经广泛使用了，\x01",
            "不过温暖程度始终比不上暖炉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#1P嗯，各有各的优点吧。\x01",
            "导力炉用起来比较方便嘛～\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#2P两位～打扰了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_412F():
        OP_6D(81370, 0, 53270, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_412F)

    def lambda_4147():

        label("loc_4147")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4147")

    QueueWorkItem2(0x102, 1, lambda_4147)
    Sleep(100)

    def lambda_415D():

        label("loc_415D")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_415D")

    QueueWorkItem2(0x101, 1, lambda_415D)
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x80)
    OP_8E(0x8, 0x130B0, 0x0, 0xD048, 0xBB8, 0x0)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "我从队长那里听说了，\x01",
            "你们今晚要住在这里吧。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "晚饭就和我们\x01",
            "吃一样的饭菜如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P哎，这样好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F不好意思，还让你们这样款待我们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哪里，自从定期船通航之后，\x01",
            "从这里通行的人寥寥无几。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这里大部分时间都很冷清，\x01",
            "所以我们是十分欢迎有客人来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#1P嘿嘿，既然您这样说，\x01",
            "那我们就不客气啦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "好的。\x01",
            "那就请你们稍微等会儿吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "对了，因为是军队的伙食，\x01",
            "你们可别对味道过于期待哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    OP_8E(0x8, 0x1234A, 0x0, 0xCEAE, 0xBB8, 0x0)

    def lambda_4467():
        OP_8E(0xFE, 0x11A80, 0x0, 0xCEFE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4467)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x101,
        (
            "#000F#1P虽然在空贼团作乱的时候\x01",
            "和王国军有过争执……\x02\x03",
            "不过在王国军里\x01",
            "还是有很多亲切的军人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F确实如此。\x02\x03",
            "#015F不过，亲切的军人，\x01",
            "我想也只有利贝尔才会有吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_45D3():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45D3)

    ChrTalk(
        0x101,
        "#501F#1P啊？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F没什么……\x01",
            "总之先把行李放好吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_A2(0x3FC)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T1311   ._SN", 2, 0, 0)
    IdleLoop()
    OP_6D(80990, 200, 53320, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x101, 81090, 200, 51050, 270)
    SetChrPos(0x102, 78250, 200, 51000, 90)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrPos(0xF, 79980, 750, 50430, 0)
    SetChrPos(0x10, 79200, 750, 51110, 0)
    SetChrPos(0x11, 80060, 700, 51150, 0)
    SetChrPos(0x12, 79240, 700, 50480, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Sleep(1000)
    OP_1D(0x54)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#001F#2P哈～～吃饱啦。\x02\x03",
            "还说不要太期待什么的，\x01",
            "没想到原来是这么好吃呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x01",
            "想不到军队里也有如此好吃的饭菜。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x10, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 72320, 0, 52990, 90)

    ChrTalk(
        0x8,
        "#2P打扰了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_22(0xF, 0x0, 0x64)
    Sleep(500)
    SetChrFlags(0x8, 0x4)

    def lambda_48C9():
        OP_6D(79690, 0, 53470, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48C9)
    SetChrSubChip(0x102, 1)
    OP_8C(0x8, 90, 0)
    ClearChrFlags(0x8, 0x80)

    def lambda_48F2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_48F2)
    OP_8E(0x8, 0x1372C, 0x0, 0xCE86, 0xBB8, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x101,
        (
            "#001F#2P啊，副长先生。\x01",
            "饭菜真的很好吃哦⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F谢谢你们的款待。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P只是些粗茶淡饭，\x01",
            "能合你们的口味就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P啊，对了……\x01",
            "又有一位客人来了，\x01",
            "你们不介意和他住一个房间吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F客人……\x01",
            "这么晚了还有人来这里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#2P这位客人胆子还挺大的呢。\x02\x03",
            "我们倒无所谓，\x01",
            "说到底自己也同样是客人罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1P你们能这么说真是太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P说起来，他和小姑娘你们是同行，\x01",
            "因此也没必要太过顾虑哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F同行？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x106, 72320, 0, 52990, 90)

    NpcTalk(
        0x106,
        "青年的声音",
        (
            "#2P哼……\x01",
            "没想到你们也来了这里。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x106, 7)
    ClearChrFlags(0x106, 0x80)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4C6F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_4C6F)

    def lambda_4C81():
        OP_8E(0xFE, 0x13330, 0x0, 0xD160, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4C81)
    Sleep(500)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x106, 0x1)
    OP_8C(0x106, 180, 400)

    ChrTalk(
        0x101,
        "#004F#2P啊，是你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F『重剑阿加特』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1P什么，原来你们认识啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    ChrTalk(
        0x8,
        (
            "#2P对了阿加特，\x01",
            "你吃过晚饭没有？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F谢了，不用了。\x01",
            "刚刚已经吃过了。\x02\x03",
            "让我在这里睡一晚就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2P没问题。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x8,
        (
            "#1P好了。\x01",
            "你们就自己分配床位吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1P晚安了，各位。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    OP_44(0x106, 0xFF)
    OP_8E(0x8, 0x13240, 0x0, 0xCC06, 0xBB8, 0x0)

    def lambda_4EB1():

        label("loc_4EB1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4EB1")

    QueueWorkItem2(0x106, 3, lambda_4EB1)
    OP_8E(0x8, 0x1234A, 0x0, 0xCEAE, 0xBB8, 0x0)

    def lambda_4ED6():
        OP_8E(0xFE, 0x11A80, 0x0, 0xCEFE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4ED6)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_4F0B():
        OP_6D(80990, 200, 53320, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4F0B)
    OP_44(0x106, 0xFF)
    OP_8C(0x106, 135, 400)
    OP_8E(0x106, 0x1372C, 0x0, 0xCE86, 0x7D0, 0x0)
    OP_8C(0x106, 180, 400)

    ChrTalk(
        0x106,
        (
            "#050F#1P对了……\x01",
            "你们两个是大叔的孩子吧。\x02\x03",
            "为什么你们\x01",
            "会在这种地方过夜？\x02\x03",
            "雪拉扎德没和你们在一起吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F雪拉姐姐她\x01",
            "已经回洛连特去了。\x02\x03",
            "现在只有我们两个一起旅行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P嗯，我们以成为正游击士为目标，\x01",
            "打算环游整个王国一周。\x02\x03",
            "同时为了修行，选择了徒步旅行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#052F#1P正游击士？\x01",
            "徒步环游整个王国一周？\x02\x03",
            "真是两个无忧无虑的小鬼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F#2P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F#1P像你们这种小鬼可以\x01",
            "那么简单就成为正游击士吗？\x02\x03",
            "用常识想想，常识啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#2P别、别小看我们！\x01",
            "之前我们还抓住了那些空贼呢！\x02\x03",
            "而且我们也获得了推荐信，\x01",
            "你别把我们当作三岁小孩子！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F#1P捉空贼那件事吗？\x01",
            "我从卢格兰老爷子那听说过了。\x02\x03",
            "#050F我倒要问问你们……\x01",
            "假如只有你们两个的话，\x01",
            "事件真的会那么容易就解决吗？\x02\x03",
            "假如没有雪拉扎德在身边，\x01",
            "你们自己可以对付得了空贼吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#2P这、这个嘛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F……我想会很难。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F#1P那是当然的啦。\x02\x03",
            "你们只是初出茅庐的新人，还是小鬼而已。\x02\x03",
            "能力不够、经验不足，\x01",
            "遇到突发事件又不能做出敏锐的判断。\x02\x03",
            "而且还这么不知天高地厚，\x01",
            "你们迟早有一天会摔跟头的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#2P什、什么不知天高地厚啊！？\x02\x03",
            "你才是呢！\x01",
            "这个时候还上山来，\x01",
            "你究竟知不知道有多危险啊？\x02\x03",
            "还有资格说别人吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F#1P蠢材！我和你们可不一样！\x02\x03",
            "而且我有任务在身，\x01",
            "不像你们那样在到处游山玩水。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F任务？\x01",
            "是游击士协会的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F#1P啊啊，就是你们那个老爸，\x01",
            "出差前把自己的任务强推给我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2P啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F父亲强推给你的任务？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#050F#1P………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 315, 400)

    ChrTalk(
        0x106,
        (
            "#053F不说了，明天还要早起。\x01",
            "赶快睡觉要紧。\x02\x03",
            "你们也别再罗嗦了，上床睡觉吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_586C():
        OP_6D(79640, 0, 54740, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_586C)
    OP_8E(0x106, 0x12F52, 0x0, 0xDCA0, 0x9C4, 0x0)
    OP_8C(0x106, 180, 400)
    SetChrFlags(0x106, 0x4)
    OP_96(0x106, 0x1287C, 0x0, 0xDDCC, 0x3E8, 0x1388)

    ChrTalk(
        0x101,
        "#005F#2P啊～这样就想糊弄过去吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F说得那么明显，\x01",
            "分明就是要让我们在意嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#054F够啦！别再烦我啦。\x02\x03",
            "我是为了你们两个小鬼好，\x01",
            "多管闲事只会惹来一身麻烦。\x02\x03",
            "#053F明天一早就给我快点去卢安，\x01",
            "看看协会的公告板上有什么活干！\x02\x03",
            "那种才是……呼啊……\x01",
            "你们应该去过的生活……\x02\x03",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(2000)
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#2P等、等一下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F好像已经睡着了。\x01",
            "和艾丝蒂尔你一样能睡呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#2P别把我和他混为一谈！\x02\x03",
            "#007F真是的～这家伙究竟怎么想的！？\x02\x03",
            "难道除了吵架，\x01",
            "他就不会做点别的事情吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F算了算了。\x01",
            "毕竟我们还是新人啊。\x02\x03",
            "也许他只是担心我们，\x01",
            "才会特意说那么严厉的话吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#2P………………………\x02\x03",
            "我说约修亚，\x01",
            "难道你真的这样想吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#005F这个嘛，我也不太肯定。\x02\x03",
            "#010F不过，正如他所说的，\x01",
            "我们最好也早点休息吧。\x02\x03",
            "明天还要下山呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2P唔～虽然感到很不爽，\x01",
            "不过没办法啦……\x02\x03",
            "#006F嘿嘿，我们干脆在他脸上涂鸦，\x01",
            "给他一点教训吧？\x02\x03",
            "我看他睡得挺熟的，应该没问题☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F还是不要这么做吧……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T1301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_3D55 end

    def Function_13_5E8E(): pass

    label("Function_13_5E8E")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(80978, 0, 152763, 0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x106, 0x4)
    SetChrPos(0x101, 84150, 0, 151987, 45)
    SetChrPos(0x102, 80770, 0, 151987, 45)
    SetChrPos(0x106, 76070, 0, 151787, 315)
    OP_62(0x101, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    OP_8C(0x101, 225, 400)
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x102, 225, 400)
    OP_62(0x102, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    OP_63(0x102)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x106, 135, 400)
    OP_62(0x106, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    OP_63(0x106)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(
        0x101,
        "#000F刚、刚才你有没有听到什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好像发生了什么事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F……………………\x02\x03",
            "我到外面看看情况，\x01",
            "你们两个乖乖留在这里睡觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_96(0x106, 0x1302D, 0x0, 0x25051, 0x3E8, 0x1770)
    OP_8E(0x106, 0x12E29, 0x0, 0x242F5, 0x1388, 0x0)
    OP_8E(0x106, 0x11E79, 0x0, 0x240ED, 0x1388, 0x0)
    SetChrFlags(0x106, 0x80)

    ChrTalk(
        0x101,
        (
            "#000F啊……\x01",
            "等、等一下嘛！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F为了谨慎起见，\x01",
            "我们也出去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，那当然啦！\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x101, 82130, 0, 148000, 270)
    RemoveParty(0x5, 0xFF)
    EventEnd(0x0)
    Return()

    # Function_13_5E8E end

    def Function_14_6139(): pass

    label("Function_14_6139")

    OP_72(0x3, 0x20)
    OP_6F(0x3, 10)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    RemoveParty(0x5, 0xFF)
    EventBegin(0x0)
    OP_6D(84500, 0, 57320, 0)
    SetChrPos(0x102, 82610, 0, 56640, 90)
    SetChrPos(0x101, 84250, 650, 56940, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 7)
    FadeToDark(0, 0, -1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔。\x01",
            "……天亮了，该起床了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#455F#2P呼啊～～……\x01",
            "讨厌……做什么嘛～……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 16)
    OP_1D(0x10)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#457F#2P咦，约修亚……\x02\x03",
            "这么早就要去协会吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F你在说什么呀？\x01",
            "我们还在古罗尼关所呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_62F0():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62F0)
    Sleep(50)
    OP_6F(0x3, 10)
    OP_70(0x3, 0x14)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#456F#2P啊，对了……\x01",
            "昨天晚上发生了魔兽骚动……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x11, 0x15, 0x5DC)

    ChrTalk(
        0x101,
        "#453F咦……\x02",
    )

    CloseMessageWindow()
    OP_6D(82170, 0, 55040, 1500)

    ChrTalk(
        0x101,
        "#451F#4P那个红头发的刀子嘴呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3P他好像一大早就出发了，\x01",
            "应该是有紧要任务要去执行吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#452F#4P是这样吗……\x02\x03",
            "#455F#4P难得昨天晚上\x01",
            "还同心协力把魔兽击退了……\x02\x03",
            "连个招呼也不打就走了，\x01",
            "真是个没礼貌的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3P算了算了。\x02\x03",
            "我们也该准备动身出发了，\x01",
            "最好在中午之前翻过这座山峰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#454F#4P嗯，我知道了。\x02\x03",
            "终于要到卢安了呢！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_72(0x3, 0x8)
    OP_72(0x3, 0x20)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x2)
    SetChrPos(0x101, 77640, 0, 53190, 270)
    SetChrPos(0x102, 77640, 0, 53190, 270)
    OP_6D(77640, 0, 53190, 0)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x406)
    OP_28(0x3A, 0x4, 0x2)
    OP_28(0x3A, 0x4, 0x4)
    OP_28(0x3A, 0x1, 0x1)
    OP_28(0x3A, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_14_6139 end

    def Function_15_65F4(): pass

    label("Function_15_65F4")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6665")
    TurnDirection(0x102, 0x1, 400)

    ChrTalk(
        0x102,
        (
            "#010F这边是柏斯地区。\x02\x03",
            "没有拿到许可证\x01",
            "是不能从这边出去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C5")

    label("loc_6665")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010F这边是柏斯地区。\x02\x03",
            "没有拿到许可证\x01",
            "是不能从这边出去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66C5")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_15_65F4 end

    def Function_16_66E1(): pass

    label("Function_16_66E1")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在此休息\x01",      # 0
            "离开\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68FC")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 18440, 1000, 12120, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x32)
    OP_73(0x33)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, 19740, 0, 13090, 217)
    SetChrPos(0x1, 19740, 0, 13090, 217)
    SetChrPos(0x2, 19740, 0, 13090, 217)
    SetChrPos(0x3, 19740, 0, 13090, 217)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x5, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_68FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6916")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_6916")

    Return()

    # Function_16_66E1 end

    SaveToFile()

Try(main)
