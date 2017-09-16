from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2320   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2320.x',
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
        "Function_2_170",          # 02, 2
        "Function_3_186",          # 03, 3
        "Function_4_18B",          # 04, 4
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_166")
    OP_B1("t2320_y")
    Jump("loc_16F")

    label("loc_166")

    OP_B1("t2320_n")

    label("loc_16F")

    Return()

    # Function_1_14E end

    def Function_2_170(): pass

    label("Function_2_170")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_185")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_170")

    label("loc_185")

    Return()

    # Function_2_170 end

    def Function_3_186(): pass

    label("Function_3_186")

    Call(0, 4)
    Return()

    # Function_3_186 end

    def Function_4_18B(): pass

    label("Function_4_18B")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB")
    OP_0D()
    OP_A9(0x28)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_1EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FC")
    TalkEnd(0x8)
    Return()

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_27E")

    ChrTalk(
        0x8,
        (
            "只要孩子们一来，\x01",
            "我的腰痛就不犯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "说不定是孩子们\x01",
            "把他们的精神劲头分给我了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2A")

    label("loc_27E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_3CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "听说这次事件的\x01",
            "犯人被关在风车小屋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他们在被交给游击士协会之前，\x01",
            "应该先向孩子们道歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你们也是这么想的吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C9")

    label("loc_339")


    ChrTalk(
        0x8,
        (
            "听说这次事件的\x01",
            "犯人被关在风车小屋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他们在被交给游击士协会之前，\x01",
            "应该先向孩子们道歉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C9")

    Jump("loc_B2A")

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_4C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46A")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "那些孩子们\x01",
            "本来就已经沦落天涯，\x01",
            "竟然还遇到这样的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "空之女神大人\x01",
            "到底在做什么啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF")

    label("loc_46A")


    ChrTalk(
        0x8,
        (
            "那些孩子们\x01",
            "本来就已经沦落天涯，\x01",
            "竟然还遇到这样的事情……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF")

    Jump("loc_B2A")

    label("loc_4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_622")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_597")
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
    Jump("loc_61F")

    label("loc_597")


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

    label("loc_61F")

    Jump("loc_B2A")

    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_6F3")

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

    ChrTalk(
        0x8,
        "我无法原谅做了这种事的犯人……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B2A")

    label("loc_6F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_741")

    ChrTalk(
        0x8,
        (
            "总觉得村里气氛\x01",
            "好像有一些慌乱……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "发生什么事情了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B2A")

    label("loc_741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_84A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EC")
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
    Jump("loc_847")

    label("loc_7EC")


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

    label("loc_847")

    Jump("loc_B2A")

    label("loc_84A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_9AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_941")
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
    Jump("loc_9AB")

    label("loc_941")


    ChrTalk(
        0x8,
        (
            "虽然定期船的开航\x01",
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

    label("loc_9AB")

    Jump("loc_B2A")

    label("loc_9AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_A1E")

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
    Jump("loc_B2A")

    label("loc_A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_B2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD6")
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

    ChrTalk(
        0x8,
        "真是难能可贵啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B2A")

    label("loc_AD6")


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

    label("loc_B2A")

    TalkEnd(0x8)
    Return()

    # Function_4_18B end

    SaveToFile()

Try(main)
