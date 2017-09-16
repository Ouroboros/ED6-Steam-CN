from ED6ScenarioHelper import *

def main():
    # 洛连特市 钟楼

    CreateScenaFile(
        FileName            = 'T0133   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0133.x',
        MapIndex            = 10,
        MapDefaultBGM       = "ed60010",
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
        '潘杜爷爷',                             # 9
        '艾娅莉',                               # 10
        '阿鲁姆',                               # 11
    )

    DeclEntryPoint(
        Unknown_00              = 6000,
        Unknown_04              = 0,
        Unknown_08              = 184000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 10,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01250 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01140 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01250P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01140P._CP',             # 02
    )

    DeclNpc(
        X                   = 3275,
        Z                   = 0,
        Y                   = 2522,
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

    DeclNpc(
        X                   = 54174,
        Z                   = 10300,
        Y                   = 44126,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 54904,
        Z                   = 10300,
        Y                   = 44125,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -300,
        TriggerZ            = 0,
        TriggerY            = 4140,
        TriggerRange        = 800,
        ActorX              = -300,
        ActorZ              = 1000,
        ActorY              = 4140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53450,
        TriggerZ            = 10300,
        TriggerY            = 47970,
        TriggerRange        = 800,
        ActorX              = 53450,
        ActorZ              = 10000,
        ActorY              = 47970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_1E2",          # 01, 1
        "Function_2_204",          # 02, 2
        "Function_3_205",          # 03, 3
        "Function_4_21B",          # 04, 4
        "Function_5_B46",          # 05, 5
        "Function_6_D79",          # 06, 6
        "Function_7_F29",          # 07, 7
        "Function_8_10C7",         # 08, 8
        "Function_9_10D1",         # 09, 9
        "Function_10_2161",        # 0A, 10
        "Function_11_21E4",        # 0B, 11
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_17E")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_1D3")

    label("loc_17E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_188")
    Jump("loc_1D3")

    label("loc_188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_19C")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_1D3")

    label("loc_19C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1A6")
    Jump("loc_1D3")

    label("loc_1A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1C4")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_1D3")

    label("loc_1C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1CE")
    Jump("loc_1D3")

    label("loc_1CE")

    SetChrFlags(0x8, 0x10)

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1E1")
    OP_A3(0x3FA)
    Event(0, 9)

    label("loc_1E1")

    Return()

    # Function_0_16A end

    def Function_1_1E2(): pass

    label("Function_1_1E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA")
    OP_B1("t0133_y")
    Jump("loc_203")

    label("loc_1FA")

    OP_B1("t0133_n")

    label("loc_203")

    Return()

    # Function_1_1E2 end

    def Function_2_204(): pass

    label("Function_2_204")

    Return()

    # Function_2_204 end

    def Function_3_205(): pass

    label("Function_3_205")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_3_205")

    label("loc_21A")

    Return()

    # Function_3_205 end

    def Function_4_21B(): pass

    label("Function_4_21B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_3FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "每天从塔顶向外眺望，\x01",
            "真是让人很开心呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "季节的变化，\x01",
            "城镇里人们的生活……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每天都会发生\x01",
            "各种各样的变化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近经常在街上看到\x01",
            "布露姆老太太。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "她要去干什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F9")

    label("loc_36F")


    ChrTalk(
        0xFE,
        (
            "每天从塔顶向外眺望，\x01",
            "真是让人很开心呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每天都会发生\x01",
            "各种各样的变化。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F9")

    Jump("loc_B42")

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_541")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F1")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "战争结束，修复钟楼的时候，\x01",
            "梅尔达斯的儿子\x01",
            "把大钟改成了导力驱动式。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我能摆弄的部分越来越少了，\x01",
            "真是感到有些寂寞啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "这也是时代的变迁呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53E")

    label("loc_4F1")


    ChrTalk(
        0xFE,
        (
            "战争结束，修复钟楼的时候，\x01",
            "梅尔达斯的儿子\x01",
            "把大钟改成了导力驱动式。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53E")

    Jump("loc_B42")

    label("loc_541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F3")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "开始今天的检查吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个塔是洛连特的象征，\x01",
            "代表了洛连特的历史，\x01",
            "而且也是我的骄傲呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_645")

    label("loc_5F3")


    ChrTalk(
        0xFE,
        (
            "这个塔是洛连特的象征，\x01",
            "代表了洛连特的历史，\x01",
            "而且也是我的骄傲呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_645")

    Jump("loc_B42")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_7AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_725")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "一天又过去了， \x01",
            "和平的日子实在是比什么都好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "一想起十年前的那次战争我就忍不住颤抖。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "战争什么的……不要再发生了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AC")

    label("loc_725")


    ChrTalk(
        0x8,
        "一想起十年前的那次战争我就忍不住颤抖。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "战争什么的……不要再发生了。\x02",
    )

    CloseMessageWindow()

    label("loc_7AC")

    Jump("loc_B42")

    label("loc_7AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_8BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_865")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "还是老样子，\x01",
            "钟声依旧那么动听。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我呀，\x01",
            "最喜欢听这个塔的钟声呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这个钟不仅仅\x01",
            "只有报时的作用哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "它还铭刻着\x01",
            "洛连特的历史呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BB")

    label("loc_865")


    ChrTalk(
        0x8,
        (
            "这个钟不仅仅\x01",
            "只有报时的作用哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "它还铭刻着\x01",
            "洛连特的历史呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BB")

    Jump("loc_B42")

    label("loc_8BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABC")
    OP_A2(0x0)

    ChrTalk(
        0x101,
        "#001F潘杜爷爷！\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0x8,
        "嗯？这个声音是……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(
        0x8,
        "……呵呵呵呵！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我还以为是谁呢，\x01",
            "这不是卡西乌斯家的\x01",
            "调皮姑娘和听话小子吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "最近你们好久都\x01",
            "没有到这里来玩了呢，\x01",
            "这段时间很忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F潘杜爷爷还是一直都在这里守着的吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "这里就像\x01",
            "我的家一样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我会一直守着这个钟楼，\x01",
            "至死方休。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B42")

    label("loc_ABC")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "这里就像\x01",
            "我的家一样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我会一直守着这个钟楼，\x01",
            "至死方休。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B42")

    TalkEnd(0x8)
    Return()

    # Function_4_21B end

    def Function_5_B46(): pass

    label("Function_5_B46")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D31")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "星星开始闪烁的时候，\x01",
            "他在塔上这么和我说的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "可以和我交往吗……\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        "哎呀㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这就是我\x01",
            "梦寐以求的场景啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 500)

    ChrTalk(
        0x101,
        (
            "#501F（唔，\x01",
            "　的确是一个相当不错的地方……）\x02\x03",
            "#501F（为了听这句话\x01",
            "　两个人特意跑上这里来？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（呵呵……\x01",
            "　这要看当事人是怎么想的了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D75")

    label("loc_D31")


    ChrTalk(
        0x9,
        "呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "好·幸·福·呢㈱\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    label("loc_D75")

    TalkEnd(0x9)
    Return()

    # Function_5_B46 end

    def Function_6_D79(): pass

    label("Function_6_D79")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED1")
    OP_A2(0x2)

    ChrTalk(
        0xA,
        "#4S成功了！#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "听我说！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "她终于答应\x01",
            "和我交往了啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 500)
    OP_62(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "啊啊，女神大人……\x01",
            "一整天所做的努力终于没有白费啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#501F（一、一整天……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（真是坚持不懈换来的胜利呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_F25")

    label("loc_ED1")


    ChrTalk(
        0xA,
        (
            "啊啊，女神大人……\x01",
            "一整天所做的努力终于没有白费啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F25")

    TalkEnd(0xA)
    Return()

    # Function_6_D79 end

    def Function_7_F29(): pass

    label("Function_7_F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10BD")
    EventBegin(0x0)
    OP_A2(0x26A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里有架梯子可以通到上面的瞭望台去。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#003F…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F哟，怎么了？\x01",
            "突然愣着不动。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#506F啊……唔唔，没什么！\x02\x03",
            "#006F对了，我们也上瞭望台看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F唔……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AC")

    ChrTalk(
        0x103,
        "#522F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_10AC")

    Sleep(100)
    NewScene("ED6_DT01/T0133   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_10C6")

    label("loc_10BD")

    NewScene("ED6_DT01/T0133   ._SN", 103, 0, 0)
    IdleLoop()

    label("loc_10C6")

    Return()

    # Function_7_F29 end

    def Function_8_10C7(): pass

    label("Function_8_10C7")

    NewScene("ED6_DT01/T0133   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_8_10C7 end

    def Function_9_10D1(): pass

    label("Function_9_10D1")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 54192, 10300, 44126, 180)
    SetChrPos(0x102, 55561, 10300, 44126, 180)
    SetMapFlags(0x10)
    FadeToBright(4000, 0)
    OP_6D(54670, 10300, 44190, 0)
    OP_6C(330000, 0)
    OP_67(0, 8300, -10000, 0)
    OP_6B(1560, 0)
    OP_6E(457, 0)

    def lambda_114B():
        OP_6D(54190, 10300, 41950, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_114B)

    def lambda_1163():
        OP_6C(302000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1163)

    def lambda_1173():
        OP_6E(539, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1173)

    def lambda_1183():
        OP_67(0, 7060, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1183)
    Sleep(6500)
    Fade(1500)
    OP_6D(54620, 10300, 44190, 0)
    OP_67(0, 6690, -10000, 0)
    OP_6B(1660, 0)
    OP_6C(225000, 0)
    OP_6E(476, 0)
    SetChrPos(0x101, 53950, 10300, 44150, 180)
    SetChrPos(0x102, 55250, 10300, 44150, 180)
    Sleep(2000)

    ChrTalk(
        0x101,
        (
            "#501F#2P哈啊～\x01",
            "早上的空气真是清新……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#001F#2P看啊，约修亚。\x01",
            "从这里能看到咱们家呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F#6P真的，能看到屋顶呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#6P不过，\x01",
            "平常你都不想来这里的，\x01",
            "今天这是吹的什么风啊？\x02\x03",
            "我本来以为\x01",
            "你不喜欢这个地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#2P……………………………\x02",
    )

    CloseMessageWindow()

    def lambda_1368():
        OP_6E(450, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1368)
    OP_20(0x7D0)
    Sleep(1000)
    OP_8C(0x101, 180, 300)
    OP_21()
    OP_1D(0x53)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#000F#2P我喜欢这个地方啊。\x01",
            "不过，我不会随便来这里的。\x02\x03",
            "#500F这是我妈妈……\x01",
            "去世的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#6P……哎………\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_AD(0x40019, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "１０年前战争的时候……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "包围洛连特的帝国军队\x01",
            "为了迫使这里的市民投降，\x01",
            "而向作为城市象征的钟楼开炮。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "那个时候，\x01",
            "爸爸作为王国军的军人参加了战斗……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "我……为了要看看\x01",
            "和爸爸战斗的对手是什么样的人，\x01",
            "自己一个人登上了这座钟楼……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "但是……就连逃跑的机会都没有，钟楼突然倒塌了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_AD(0x4001A, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            "不过，当我回过神来的时候，\x01",
            "却发现自己毫发无伤……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "是妈妈……保护了我……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "她用双臂紧紧地抱着我，\x01",
            "为我挡住了大量瓦砾的撞击。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "而且，还为哭个不停的我\x01",
            "唱起了我最喜欢的摇篮曲……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "然后……然后……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "当瓦砾被清除之后……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x64)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0x101,
        (
            "#003F#2P………………………\x02\x03",
            "……战争结束了，\x01",
            "这里也被修复成原来的样子。\x01",
            "不过自那以后，我就很少来过……\x02\x03",
            "因为那是一段非常痛苦的回忆……\x02\x03",
            "#500F一来到这里，\x01",
            "心里就不由得有种想要依赖妈妈的感觉……\x02\x03",
            "可是，要是依赖了妈妈，\x01",
            "就不能像妈妈那样坚强起来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F#6P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#501F#2P不过，没关系吧？\x01",
            "至少今天让我依赖一下……\x02\x03",
            "让我向妈妈祈求，\x01",
            "保佑爸爸平安归来也好……\x02\x03",
            "让我向妈妈祈求，\x01",
            "在天国一直守护着爸爸也好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F#6P……当然可以了。\x02",
    )

    CloseMessageWindow()

    def lambda_192E():
        OP_6D(53840, 10300, 44180, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_192E)
    OP_92(0x102, 0x101, 0x1F4, 0x3E8, 0x0)
    WaitChrThread(0x0, 0x1)

    ChrTalk(
        0x102,
        (
            "#012F#6P放心吧……\x01",
            "父亲一定会平安无事的。\x02\x03",
            "有你母亲守护着他，\x01",
            "一定会没事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#2P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6P就算万一真的出了问题，\x01",
            "还有艾丝蒂尔你可以帮助他啊。\x02\x03",
            "以前母亲救了你，\x01",
            "这次该由你去救父亲了。\x02\x03",
            "我也会帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#2P……约修亚…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#6P你的心情，\x01",
            "我虽然不能完全体会……\x02\x03",
            "不过像这样呆在你身边……\x01",
            "我还是能做到的。\x02\x03",
            "#010F如果不介意的话，\x01",
            "我的胸膛随时可以借你一用。\x02\x03",
            "所以……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#500F#2P…………………………\x02\x03",
            "#008F……………噗～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#6P哎？\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x1)

    ChrTalk(
        0x101,
        (
            "#001F#2P啊哈哈哈哈～！\x01",
            "约修亚你在耍什么帅啊～\x02\x03",
            "真是的……\x01",
            "这种话你也能这么随便说出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_1C5E():
        OP_6D(54620, 10300, 44190, 700)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1C5E)
    OP_8F(0x102, 0xD7D2, 0x283C, 0xAC76, 0xBB8, 0x0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#014F#6P哎、哎哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#507F#2P如果是其它女孩的话，\x01",
            "肯定会完全误解啦。\x02\x03",
            "约修亚你啊，\x01",
            "将来准是个整日被绯闻缠身的男人。\x02\x03",
            "#007F呼～\x01",
            "做姐姐的还真是担心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#6P真、真是抱歉，我这么随便。\x02\x03",
            "#013F真是的……\x01",
            "人家特意这么关心你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#2P嘿嘿……\x01",
            "谢谢你的鼓励啦。\x02\x03",
            "不管怎么说，有点干劲了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F#6P哼，你能这样说，\x01",
            "我刚才装帅也是值得了。\x02\x03",
            "#017F真是……唉唉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#2P别在意，别在意。\x01",
            "我刚才不是说了谢谢嘛。\x02\x03",
            "#006F那么……\x01",
            "我们该下去了吧？\x02\x03",
            "雪拉姐肯定在等着了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#6P是啊，我们下去吧。\x02",
    )

    CloseMessageWindow()

    def lambda_1FCF():
        OP_6D(54240, 10300, 47980, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1FCF)

    def lambda_1FE7():
        OP_67(0, 6220, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1FE7)

    def lambda_1FFF():
        OP_6C(324000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1FFF)

    def lambda_200F():
        OP_6E(470, 4000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_200F)
    OP_43(0x102, 0x0, 0x0, 0xA)
    Sleep(3000)
    SetChrFlags(0x102, 0x4)
    OP_8E(0x101, 0xCD12, 0x283C, 0xB5C7, 0xBB8, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#500F……………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#006F（妈妈，\x01",
            "　我终于明白了……）\x02\x03",
            "（我以游击士作为自己的目标，\x01",
            "　是因为想像妈妈那样\x01",
            "　为了保护别人而变得坚强起来……）\x02\x03",
            "（所以，请等着我……）\x02\x03",
            "（我一定……\x01",
            "　我一定会把爸爸平安带回来的！）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_43(0x101, 0x0, 0x0, 0xB)
    OP_0D()
    SetChrFlags(0x102, 0x80)
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T0100   ._SN", 113, 0, 0)
    IdleLoop()
    Return()

    # Function_9_10D1 end

    def Function_10_2161(): pass

    label("Function_10_2161")

    SetChrFlags(0x102, 0x4)
    OP_8E(0x102, 0xCC9C, 0x283C, 0xB536, 0x7D0, 0x0)
    OP_8E(0x102, 0xCC88, 0x283C, 0xBB08, 0x7D0, 0x0)
    OP_8E(0x102, 0xCE72, 0x283C, 0xBB94, 0x7D0, 0x0)
    SetChrFlags(0x102, 0x4)
    OP_8C(0x102, 270, 400)
    OP_96(0x102, 0xD1C4, 0x251C, 0xBCA4, 0x258, 0x1388)
    Sleep(500)
    OP_8F(0x102, 0xD1C4, 0x206C, 0xBCA4, 0xBB8, 0x0)
    SetChrFlags(0x102, 0x80)
    Return()

    # Function_10_2161 end

    def Function_11_21E4(): pass

    label("Function_11_21E4")

    SetChrFlags(0x101, 0x4)
    OP_8E(0x101, 0xCC88, 0x283C, 0xBB08, 0x7D0, 0x0)
    OP_8E(0x101, 0xCE72, 0x283C, 0xBB94, 0x7D0, 0x0)
    OP_8C(0x101, 270, 400)
    OP_96(0x101, 0xD1C4, 0x251C, 0xBCA4, 0x258, 0x1388)
    Sleep(500)
    OP_8F(0x101, 0xD1C4, 0x206C, 0xBCA4, 0xBB8, 0x0)
    SetChrFlags(0x101, 0x80)
    Return()

    # Function_11_21E4 end

    SaveToFile()

Try(main)
