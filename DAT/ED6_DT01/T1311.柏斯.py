from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1311   ._SN',
        MapName             = 'Bose',
        Location            = 'T1311.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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

    DeclEntryPoint(
        Unknown_00              = 48000,
        Unknown_04              = -3000,
        Unknown_08              = 27000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 6000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 280,
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
        'ED6_DT07/CH01240 ._CH',             # 02
        'ED6_DT07/CH00003 ._CH',             # 03
        'ED6_DT07/CH00013 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
        'ED6_DT06/CH20053 ._CH',             # 07
        'ED6_DT06/CH20053 ._CH',             # 08
        'ED6_DT06/CH20062 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH01240P._CP',             # 02
        'ED6_DT07/CH00003P._CP',             # 03
        'ED6_DT07/CH00013P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
        'ED6_DT06/CH20053P._CP',             # 07
        'ED6_DT06/CH20053P._CP',             # 08
        'ED6_DT06/CH20062P._CP',             # 09
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
        Direction           = 27,
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
        X                   = 81840,
        Z                   = 0,
        Y                   = 13080,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 10,
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
        TriggerX            = 18440,
        TriggerZ            = 0,
        TriggerY            = 12120,
        TriggerRange        = 1000,
        ActorX              = 18440,
        ActorZ              = 1000,
        ActorY              = 12120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_442",          # 01, 1
        "Function_2_4B9",          # 02, 2
        "Function_3_4CF",          # 03, 3
        "Function_4_4D4",          # 04, 4
        "Function_5_15A1",         # 05, 5
        "Function_6_1CD3",         # 06, 6
        "Function_7_27A5",         # 07, 7
        "Function_8_2BD2",         # 08, 8
        "Function_9_2C32",         # 09, 9
        "Function_10_2E98",        # 0A, 10
        "Function_11_36C8",        # 0B, 11
        "Function_12_4F97",        # 0C, 12
        "Function_13_52F9",        # 0D, 13
        "Function_14_56CF",        # 0E, 14
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_352")
    OP_71(0x2, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3EF")

    label("loc_352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_37A")
    OP_71(0x2, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3EF")

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_393")
    OP_71(0x2, 0x10)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3EF")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3AC")
    OP_71(0x2, 0x10)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3EF")

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_3C0")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3EF")

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3D9")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_3EF")

    label("loc_3D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3EF")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_3FD")
    OP_A3(0x3FC)
    Event(0, 11)

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_414")
    OP_A3(0x3FA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_422")
    OP_A3(0x3FB)
    Event(0, 13)

    label("loc_422")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_42E"),
        (SWITCH_DEFAULT, "loc_441"),
    )


    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43E")
    Event(0, 11)

    label("loc_43E")

    Jump("loc_441")

    label("loc_441")

    Return()

    # Function_0_32A end

    def Function_1_442(): pass

    label("Function_1_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_END)), "loc_46F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_64(0x0, 0x1)

    label("loc_46F")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_442 end

    def Function_2_4B9(): pass

    label("Function_2_4B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4B9")

    label("loc_4CE")

    Return()

    # Function_2_4B9 end

    def Function_3_4CF(): pass

    label("Function_3_4CF")

    Call(0, 4)
    Return()

    # Function_3_4CF end

    def Function_4_4D4(): pass

    label("Function_4_4D4")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_580")

    ChrTalk(
        0x8,
        (
            "从卢安订购的鱼\x01",
            "终于送过来了。\x02",
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
    Jump("loc_159D")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_62A")

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
    Jump("loc_159D")

    label("loc_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_6B4")

    ChrTalk(
        0x8,
        "啊，你们不就是游击士的……\x02",
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
    Jump("loc_159D")

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_10A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5C")
    ClearMapFlags(0x1)
    OP_69(0x8, 0x3E8)

    ChrTalk(
        0x101,
        "#000F士兵先生，早上好～！\x02",
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
            "#000F嘿嘿，没什么啦。\x02\x03",
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
        "#000F奇怪……怎么了？\x02",
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
        "#010F这样说来的确是有点奇怪……\x02",
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
        "#000F这、这样没问题吗？\x02",
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
        "那么……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)
    OP_70(0x2, 0x64)
    OP_6D(23765, 0, 25450, 2000)

    ChrTalk(
        0x8,
        (
            "碧海白花环抱的卢安\x01",
            "欢迎你们的到来！\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x8, 0x3E8)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        (
            "对了对了，\x01",
            "小姑娘你们是不是打算去卢安市？\x02",
        )
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
        "#000F啊，这样可以吗？\x02",
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
        "#000F嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F承蒙你们多方关照了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x407)
    OP_28(0x11, 0x4, 0x40)
    OP_28(0x13, 0x4, 0x40)
    NewScene("ED6_DT01/T1300   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_109E")

    label("loc_F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1011")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "啊呀，是你们啊……\x02",
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
    Jump("loc_109E")

    label("loc_1011")


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

    label("loc_109E")

    Jump("loc_159D")

    label("loc_10A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_110F")

    ChrTalk(
        0x8,
        (
            "啊呀，这种时间\x01",
            "还到这里来啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "外面已经很冷了吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_159D")

    label("loc_110F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1312")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1275")
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
            "说起来\x01",
            "最近很奇怪的是，\x01",
            "我看到了有首领带领的魔兽群体。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "可是至今为止都没有见过的哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_130F")

    label("loc_1275")


    ChrTalk(
        0x8,
        (
            "最近很奇怪的是，\x01",
            "会看到有首领带领的魔兽群体。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "可是至今为止都没有见过的哦。\x02",
    )

    CloseMessageWindow()

    label("loc_130F")

    Jump("loc_159D")

    label("loc_1312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_13B3")

    ChrTalk(
        0x8,
        (
            "我有义务\x01",
            "让士兵们平时保持\x01",
            "６个小时以上的睡眠。\x02",
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
    Jump("loc_159D")

    label("loc_13B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_14CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1461")
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
            "让我到这里来\x01",
            "给士兵们做饭。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14CB")

    label("loc_1461")


    ChrTalk(
        0x8,
        (
            "顺带一提，那里有\x01",
            "供旅行者专用的房间，\x01",
            "你们可以随时使用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14CB")

    Jump("loc_159D")

    label("loc_14CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_159D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157C")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "啊呀，小姑娘\x01",
            "你们要去卢安吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "要去卢安的话，\x01",
            "必须要有许可证……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159D")

    label("loc_157C")


    ChrTalk(
        0x8,
        "啊呀，你们要去卢安吗？\x02",
    )

    CloseMessageWindow()

    label("loc_159D")

    TalkEnd(0x8)
    Return()

    # Function_4_4D4 end

    def Function_5_15A1(): pass

    label("Function_5_15A1")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_16E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165E")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "今天该轮到\x01",
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
            "那个人，真的\x01",
            "非常喜欢烹饪啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DF")

    label("loc_165E")


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
            "那个人，真的\x01",
            "非常喜欢烹饪啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DF")

    Jump("loc_1CCF")

    label("loc_16E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_17E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178B")
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
            "哎呀，这样接连不断\x01",
            "发生事件真是很难办啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DE")

    label("loc_178B")


    ChrTalk(
        0xFE,
        (
            "自从空贼被逮捕以来，\x01",
            "柏斯地区就非常和平。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17DE")

    Jump("loc_1CCF")

    label("loc_17E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1875")

    ChrTalk(
        0xFE,
        (
            "这之前的魔兽们\x01",
            "比想象中的要厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们也要\x01",
            "加紧训练才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_1875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_1912")

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
    Jump("loc_1CCF")

    label("loc_1912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_19A9")

    ChrTalk(
        0xFE,
        (
            "这样持续拖延搜索，\x01",
            "国境师团的家伙也相当疲劳吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "如果有什么新的进展就好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_19A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1A6A")

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
    Jump("loc_1CCF")

    label("loc_1A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1B66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B03")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "这座古罗尼连峰的\x01",
            "地形也是起伏频繁的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难不成\x01",
            "空贼团那些家伙们\x01",
            "都藏在这一带？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B63")

    label("loc_1B03")


    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "国境师团的搜查队\x01",
            "已经在这里调查好几次了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B63")

    Jump("loc_1CCF")

    label("loc_1B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C43")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "这么险峻的山道，\x01",
            "一般的登山者\x01",
            "是根本不会走的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在飞艇还在停航，\x01",
            "急着去卢安和柏斯的人们\x01",
            "不得不从这里通过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_1C43")


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

    label("loc_1CCF")

    TalkEnd(0x9)
    Return()

    # Function_5_15A1 end

    def Function_6_1CD3(): pass

    label("Function_6_1CD3")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1F0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1F")
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
    Jump("loc_1F07")

    label("loc_1E1F")


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

    label("loc_1F07")

    Jump("loc_27A1")

    label("loc_1F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_20A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2014")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "为了镇守关所，\x01",
            "才让士兵们驻守在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "偶尔也会向\x01",
            "一些登山者实行救助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为来古罗尼连峰登山\x01",
            " \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A2")

    label("loc_2014")


    ChrTalk(
        0xFE,
        (
            "为了镇守关所，\x01",
            "才让士兵们驻守在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "偶尔也会向\x01",
            "一些登山者实行救助。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A2")

    Jump("loc_27A1")

    label("loc_20A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_212B")

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
    Jump("loc_27A1")

    label("loc_212B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_218B")

    ChrTalk(
        0xFE,
        "喂，要出发了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "小心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27A1")

    label("loc_218B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_2200")

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
    Jump("loc_27A1")

    label("loc_2200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2427")
    OP_A2(0x404)
    ClearMapFlags(0x1)
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
        "隔壁的房间请自由使用。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F谢谢，队长先生！\x02",
    )

    CloseMessageWindow()
    OP_69(0x0, 0x3E8)
    SetMapFlags(0x1)
    Jump("loc_2480")

    label("loc_2427")


    ChrTalk(
        0xFE,
        (
            "这里隔壁的休息室\x01",
            "房间请自由使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "先取个暖如何？\x02",
    )

    CloseMessageWindow()

    label("loc_2480")

    Jump("loc_27A1")

    label("loc_2483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2542")

    ChrTalk(
        0xFE,
        "国境师团好像要求增员了。\x02",
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
    Jump("loc_27A1")

    label("loc_2542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_25F8")

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
    Jump("loc_27A1")

    label("loc_25F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_273B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26AC")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "摩尔根将军\x01",
            "要求强化这一带的警备，\x01",
            "下达了这样的命令。\x02",
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
    Jump("loc_2738")

    label("loc_26AC")


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
            "我要赶快通知\x01",
            "队里的人，\x01",
            "让他们提高警惕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2738")

    Jump("loc_27A1")

    label("loc_273B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_27A1")

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

    label("loc_27A1")

    TalkEnd(0xA)
    Return()

    # Function_6_1CD3 end

    def Function_7_27A5(): pass

    label("Function_7_27A5")

    TalkBegin(0xB)
    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAF")
    OP_A2(0x360)
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "啊，难不成……\x01",
            "这不是雪拉扎德前辈吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
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
            "呵呵，协会委派我来这里\x01",
            "就在这个方向。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是这样……\x02\x03",
            "对了，你已经找到\x01",
            "所谓的剑之道了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，请别问了。\x01",
            "我还是处在修行阶段呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，前辈您也是在\x01",
            "执行协会的任务吗？\x02",
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
        "是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个地方\x01",
            "最近事情很多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "您路上一定要小心哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BCE")

    label("loc_2AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B5E")
    OP_A2(0x3)

    ChrTalk(
        0x103,
        "#020F啊，这不是亚妮拉丝吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "雪拉扎德前辈！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么样？\x01",
            "调查进行得顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F嗯，有一点进展了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BCE")

    label("loc_2B5E")


    ChrTalk(
        0xFE,
        (
            "雪拉扎德前辈，\x01",
            "这个地方最近处于多事之秋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "您路上一定要小心哦。\x02",
    )

    CloseMessageWindow()

    label("loc_2BCE")

    TalkEnd(0xB)
    Return()

    # Function_7_27A5 end

    def Function_8_2BD2(): pass

    label("Function_8_2BD2")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2C2E")

    ChrTalk(
        0xC,
        (
            "这里的海拔比较高，\x01",
            "太阳一落山果然就会很冷啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2E")

    TalkEnd(0xC)
    Return()

    # Function_8_2BD2 end

    def Function_9_2C32(): pass

    label("Function_9_2C32")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2CD0")

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
            "要尽量避免这类事情的发生，\x01",
            "所以要加紧训练。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E94")

    label("loc_2CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2D62")

    ChrTalk(
        0xFE,
        "副长还真是喜欢烹饪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有时候明明不是他当班，\x01",
            "但是却在厨房烧饭呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E94")

    label("loc_2D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2E02")

    ChrTalk(
        0xFE,
        "柴火差不多要用完了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "训练结束后去报告一下，\x01",
            "然后去砍些柴吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E94")

    label("loc_2E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_2E3A")

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
    Jump("loc_2E94")

    label("loc_2E3A")


    ChrTalk(
        0xFE,
        "我还要再值会儿班。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "趁现在\x01",
            "赶快吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E94")

    TalkEnd(0xD)
    Return()

    # Function_9_2C32 end

    def Function_10_2E98(): pass

    label("Function_10_2E98")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2EFB")

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
    Jump("loc_36C4")

    label("loc_2EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_3083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3020")
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
            "虽然有很多东西都是\x01",
            "从柏斯和卢安那里运送过来的，\x01",
            "这些都是靠这条山路呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "兼任保卫的途中\x01",
            "过来迎接你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3080")

    label("loc_3020")


    ChrTalk(
        0xFE,
        (
            "这里一到冬天，\x01",
            "大雪堆积，特别不方便。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3080")

    Jump("loc_36C4")

    label("loc_3083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3117")

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
    Jump("loc_36C4")

    label("loc_3117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_326C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E5")
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
            "但不愧是游击士呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "干得真棒。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3269")

    label("loc_31E5")


    ChrTalk(
        0xFE,
        (
            "虽然看上去挺年轻，\x01",
            "不愧是游击士呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "昨天干得真棒。\x02",
    )

    CloseMessageWindow()

    label("loc_3269")

    Jump("loc_36C4")

    label("loc_326C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_333A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F2")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "有什么事？\x01",
            "没关系，你们可以进去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想使用里面的屋子时，\x01",
            "和我们队长打声招呼就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3337")

    label("loc_32F2")


    ChrTalk(
        0xFE,
        (
            "想使用里面的屋子时，\x01",
            "和我们队长打声招呼就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3337")

    Jump("loc_36C4")

    label("loc_333A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_34DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3461")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "好像找不到\x01",
            "空贼团的所在之处啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "国境师团的家伙们\x01",
            "也经常到这里\x01",
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
            " \x01",
            "可是最理想的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DB")

    label("loc_3461")


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
            " \x01",
            "可是最理想的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34DB")

    Jump("loc_36C4")

    label("loc_34DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3590")

    ChrTalk(
        0xFE,
        (
            "消失的飞艇\x01",
            "好像被找到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为犯人还没有被抓住，\x01",
            "所以还要在关所\x01",
            "就得继续进行检查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C4")

    label("loc_3590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3646")

    ChrTalk(
        0xFE,
        "空贼团啊……\x02",
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
    Jump("loc_36C4")

    label("loc_3646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_36C4")

    ChrTalk(
        0xFE,
        "现在正处在戒严状态中。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果是这样的话，\x01",
            "必须先在里面办手续。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C4")

    TalkEnd(0xE)
    Return()

    # Function_10_2E98 end

    def Function_11_36C8(): pass

    label("Function_11_36C8")

    EventBegin(0x0)
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
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)

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
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x8, 0x40)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 72320, 0, 52990, 90)

    ChrTalk(
        0x8,
        "#2P打扰了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_4A(0x8, 255)
    SetChrFlags(0x8, 0x4)

    def lambda_390F():
        OP_6D(79690, 0, 53470, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_390F)
    SetChrSubChip(0x102, 1)
    OP_8C(0x8, 90, 0)
    ClearChrFlags(0x8, 0x80)

    def lambda_3938():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3938)
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
    ClearChrFlags(0x106, 0x80)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x106, 7)
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
    SetChrFlags(0x106, 0x4)

    def lambda_3CC0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_3CC0)

    def lambda_3CD2():
        OP_8E(0xFE, 0x13330, 0x0, 0xD160, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3CD2)
    Sleep(500)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x106, 0x1)
    OP_8C(0x106, 180, 400)
    ClearChrFlags(0x106, 0x4)

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

    ChrTalk(
        0x8,
        (
            "#2P好了。\x01",
            "你们就自己分配床位吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(300)

    ChrTalk(
        0x8,
        "#1P晚安了，各位。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    OP_44(0x106, 0xFF)
    OP_8E(0x8, 0x13240, 0x0, 0xCDDC, 0xBB8, 0x0)

    def lambda_3F0C():

        label("loc_3F0C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3F0C")

    QueueWorkItem2(0x106, 3, lambda_3F0C)
    OP_8E(0x8, 0x1234A, 0x0, 0xCEAE, 0xBB8, 0x0)

    def lambda_3F31():
        OP_8E(0xFE, 0x11A80, 0x0, 0xCEFE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3F31)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_3F6B():
        OP_6D(80990, 200, 53320, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F6B)
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
    OP_62(0x101, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#009F#2P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F#1P像你们这种小鬼可以\x01",
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
            "#050F#1P捉空贼那件事吗？\x01",
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
            "#054F#1P蠢材！我和你们可不一样！\x02\x03",
            "而且我有任务在身，\x01",
            "不像你们那样在到处游山玩水。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F任务？\x01",
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
    OP_8C(0x106, 0, 400)

    ChrTalk(
        0x106,
        (
            "#053F不说了，明天还要早起。\x01",
            "赶快睡觉要紧。\x02\x03",
            "你们也别再啰嗦了，上床睡觉吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4908():
        OP_6D(79640, 0, 54740, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4908)
    OP_8E(0x106, 0x12F52, 0x0, 0xDCA0, 0x9C4, 0x0)
    OP_8C(0x106, 180, 400)
    SetChrFlags(0x106, 0x4)
    OP_96(0x106, 0x12818, 0x3E8, 0xD994, 0x4B0, 0x1388)
    OP_22(0xD1, 0x0, 0x64)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 9)
    OP_7C(0x0, 0x64, 0x7D0, 0x64)

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
    OP_62(0x106, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)
    OP_99(0x106, 0x0, 0x2, 0x3E8)
    Sleep(300)
    SetChrSubChip(0x106, 3)

    ChrTalk(
        0x106,
        (
            "#054F#1P够啦！别再烦我啦。\x02\x03",
            "我是为了你们两个小鬼好，\x01",
            "多管闲事只会惹来一身麻烦。\x02\x03",
            "明天一早就给我快点去卢安，\x01",
            "看看协会的公告板上有什么活干！\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x106, 0x3, 0x5, 0x3E8)
    Sleep(400)

    ChrTalk(
        0x106,
        (
            "#053F#1P那种才是……呼啊……\x01",
            "你们应该去过的生活……\x02\x03",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)
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
            "#014F好像已经睡着了。\x01",
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
    SetChrSubChip(0x102, 0)
    Sleep(300)

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
            "#015F这个嘛，我也不太肯定。\x02\x03",
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

    # Function_11_36C8 end

    def Function_12_4F97(): pass

    label("Function_12_4F97")

    EventBegin(0x0)
    OP_6D(79640, 0, 54740, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x101, 81090, 200, 51050, 270)
    SetChrPos(0x102, 78250, 200, 51000, 90)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrSubChip(0x102, 1)
    SetChrPos(0xF, 79980, 750, 50430, 0)
    SetChrPos(0x10, 79200, 750, 51110, 0)
    SetChrPos(0x11, 80060, 700, 51150, 0)
    SetChrPos(0x12, 79240, 700, 50480, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x106, 0x4)
    SetChrFlags(0x106, 0x2)
    SetChrPos(0x106, 75800, 1000, 55700, 0)
    SetChrChipByIndex(0x106, 9)
    SetChrSubChip(0x106, 2)
    OP_0D()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#2P刚、刚才你有没有听到什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F好像发生了什么事。\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x106)
    Sleep(300)
    SetChrChipByIndex(0x106, 7)
    ClearChrFlags(0x106, 0x2)
    OP_8C(0x106, 90, 0)
    SetChrSubChip(0x106, 0)
    OP_96(0x106, 0x12FA2, 0x0, 0xDB06, 0x258, 0x1770)
    OP_8E(0x106, 0x12ED0, 0x0, 0xD052, 0xFA0, 0x0)

    ChrTalk(
        0x106,
        (
            "#050F#1P我到外面看看情况，\x01",
            "你们两个乖乖留在这里睡觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x106, 0x12412, 0x0, 0xCEA4, 0x1770, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_51B9():
        OP_8E(0xFE, 0x11A80, 0x0, 0xCEFE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_51B9)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0x106, 0x80)

    ChrTalk(
        0x101,
        (
            "#004F#2P啊……\x01",
            "等、等一下嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F为了谨慎起见，\x01",
            "我们也出去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#2P嗯，那当然啦！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    RemoveParty(0x5, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x102, 77820, 0, 53250, 270)
    SetChrPos(0x101, 77820, 0, 53250, 270)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_6D(77820, 0, 53250, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x405)
    Return()

    # Function_12_4F97 end

    def Function_13_52F9(): pass

    label("Function_13_52F9")

    RemoveParty(0x5, 0xFF)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(83887, 0, 57065, 0)
    SetChrPos(0x101, 84150, 0, 57128, 270)
    SetChrPos(0x102, 82890, 0, 56215, 90)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)

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
            "#000F呼啊～～……\x01",
            "讨厌……做什么嘛～……\x02",
        )
    )

    CloseMessageWindow()
    OP_77(0xFF, 0xFF, 0xFF, 0x3E800, 0x0)
    Sleep(1300)

    ChrTalk(
        0x101,
        (
            "#000F咦，约修亚……\x02\x03",
            "这么早就要去协会吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F你在说什么呀？\x01",
            "我们还在古罗尼关所呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#000F啊，对了……\x01",
            "昨天晚上发生了魔兽骚动……\x02\x03",
            "咦……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 315, 400)
    Sleep(300)
    OP_8C(0x101, 315, 400)
    Sleep(300)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F那个红头发的刀子嘴呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F他好像一大早就出发了，\x01",
            "应该是有紧要任务要去执行吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是这样吗……\x02\x03",
            "难得昨天晚上\x01",
            "还同心协力把魔兽击退了……\x02\x03",
            "连个招呼也不打就走了，\x01",
            "真是个没礼貌的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F算了算了。\x02\x03",
            "我们也该准备动身出发了，\x01",
            "最好在中午之前翻过这座山峰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，我知道了。\x02\x03",
            "终于要到卢安了呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x406)
    OP_28(0x3A, 0x4, 0x2)
    OP_28(0x3A, 0x4, 0x4)
    OP_28(0x3A, 0x1, 0x1)
    OP_28(0x3A, 0x1, 0x2)
    Fade(1000)
    SetChrPos(0x101, 82076, 0, 53560, 270)
    SetChrPos(0x102, 82076, 0, 53560, 270)
    EventEnd(0x0)
    Return()

    # Function_13_52F9 end

    def Function_14_56CF(): pass

    label("Function_14_56CF")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58EA")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 18440, 1000, 12120, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x32)
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
    OP_6F(0xA, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_58EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5904")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_5904")

    Return()

    # Function_14_56CF end

    SaveToFile()

Try(main)
