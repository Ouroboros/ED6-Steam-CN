from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2321   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2321.x',
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
        '珂蕾妲婆婆',                           # 9
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
        'ED6_DT07/CH01010 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01010P._CP',             # 00
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 500,
        Y                   = 8800,
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


    DeclActor(
        TriggerX            = -4040,
        TriggerZ            = 500,
        TriggerY            = 7530,
        TriggerRange        = 400,
        ActorX              = -4000,
        ActorZ              = 2000,
        ActorY              = 8800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F6",           # 00, 0
        "Function_1_14E",          # 01, 1
        "Function_2_14F",          # 02, 2
        "Function_3_165",          # 03, 3
        "Function_4_16A",          # 04, 4
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_100")
    Jump("loc_14D")

    label("loc_100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_10A")
    Jump("loc_14D")

    label("loc_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_114")
    Jump("loc_14D")

    label("loc_114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_11E")
    Jump("loc_14D")

    label("loc_11E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_128")
    Jump("loc_14D")

    label("loc_128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_132")
    Jump("loc_14D")

    label("loc_132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_13C")
    Jump("loc_14D")

    label("loc_13C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_146")
    Jump("loc_14D")

    label("loc_146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_14D")

    label("loc_14D")

    Return()

    # Function_0_F6 end

    def Function_1_14E(): pass

    label("Function_1_14E")

    Return()

    # Function_1_14E end

    def Function_2_14F(): pass

    label("Function_2_14F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_164")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_14F")

    label("loc_164")

    Return()

    # Function_2_14F end

    def Function_3_165(): pass

    label("Function_3_165")

    Call(0, 4)
    Return()

    # Function_3_165 end

    def Function_4_16A(): pass

    label("Function_4_16A")

    TalkBegin(0x8)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA")
    OP_0D()
    OP_A9(0x28)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_1CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DB")
    TalkEnd(0x8)
    Return()

    label("loc_1DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_26B")

    ChrTalk(
        0x8,
        (
            "听说这次事件的犯人\x01",
            "被关在风车小屋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他们在被交给游击士协会之前，\x01",
            "真想用石头狠狠砸那些纵火犯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_927")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_304")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CE")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "商店也要关门了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我想，\x01",
            "至少要给孩子送点慰问品……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301")

    label("loc_2CE")


    ChrTalk(
        0x8,
        (
            "我想，\x01",
            "至少要给孩子送点慰问品……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_301")

    Jump("loc_927")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_476")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "孤儿院的孩子们\x01",
            "经常到这里来玩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "就好像一下子\x01",
            "多了许多孙子一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然我喜欢安静，\x01",
            "但是这样也不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_473")

    label("loc_3EB")


    ChrTalk(
        0x8,
        (
            "孤儿院的孩子们\x01",
            "经常到这里来玩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "就好像一下子\x01",
            "多了许多孙子一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_473")

    Jump("loc_927")

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_517")

    ChrTalk(
        0x8,
        (
            "竟然放火烧孤儿院，\x01",
            "那些家伙真是不像话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "人，\x01",
            "也有绝对不能做的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_927")

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_574")

    ChrTalk(
        0x8,
        "是不是我心理作用呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "总觉得村里\x01",
            "好像吵吵闹闹的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_927")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_67D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61F")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "这个村子\x01",
            "景色和花都很漂亮吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然在像卢安那样的城市里\x01",
            "生活很便利……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不过还是这里更合我心意啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_67A")

    label("loc_61F")


    ChrTalk(
        0x8,
        (
            "虽然在像卢安那样的城市里\x01",
            "生活很便利……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不过还是这里更合我心意啊。\x02",
    )

    CloseMessageWindow()

    label("loc_67A")

    Jump("loc_927")

    label("loc_67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_774")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "很多人都在感叹\x01",
            "定期船的开航\x01",
            "让这里变得很冷清……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我倒是觉得，\x01",
            "这样也挺不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "上了年纪之后，\x01",
            "就希望自己能够过上安静的生活。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C1")

    label("loc_774")


    ChrTalk(
        0x8,
        (
            "玛诺利亚村很萧条，\x01",
            "为此遗憾的人也很多，\x01",
            "不过我认为能安静地生活才是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C1")

    Jump("loc_927")

    label("loc_7C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_834")

    ChrTalk(
        0x8,
        "一个戴着帽子的男孩？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他没有到这家店来哦。\x01",
            "你们问问门外的萨蒂吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_927")

    label("loc_834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_927")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D3")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "我的孙女萨蒂\x01",
            "是个非常温柔的孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那孩子的父母\x01",
            "因为工作而到外地去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "为了照顾我，\x01",
            "萨蒂留在了这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_927")

    label("loc_8D3")


    ChrTalk(
        0x8,
        (
            "我的孙女萨蒂\x01",
            "是个非常温柔的孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "真是难能可贵啊。\x02",
    )

    CloseMessageWindow()

    label("loc_927")

    TalkEnd(0x8)
    Return()

    # Function_4_16A end

    SaveToFile()

Try(main)
