from ED6ScenarioHelper import *

def main():
    # 中央工房　医务室

    CreateScenaFile(
        FileName            = 'T3114   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3114.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3114   ._SN',
            'ED6_DT01/T3114_1 ._SN',
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


    DeclEvent(
        X                   = -118000,
        Y                   = -1000,
        Z                   = 23400,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -118000,
        Y                   = -1000,
        Z                   = 223400,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -118000,
        Y                   = -1000,
        Z                   = 423400,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -106990,
        Y                   = -1000,
        Z                   = -550,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x10040,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -107140,
        Y                   = 0,
        Z                   = -340,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = -119480,
        Y                   = 0,
        Z                   = 6960,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = -107010,
        Y                   = 0,
        Z                   = 199500,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = -119590,
        Y                   = 0,
        Z                   = 206950,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -106990,
        Y                   = 0,
        Z                   = 399440,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -119440,
        Y                   = 0,
        Z                   = 406910,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 14,
    )


    DeclActor(
        TriggerX            = -113730,
        TriggerZ            = 0,
        TriggerY            = 22590,
        TriggerRange        = 1200,
        ActorX              = -113730,
        ActorZ              = 0,
        ActorY              = 22590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -106980,
        TriggerZ            = 0,
        TriggerY            = -20,
        TriggerRange        = 800,
        ActorX              = -106980,
        ActorZ              = 1000,
        ActorY              = -20,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -118040,
        TriggerZ            = 0,
        TriggerY            = 24100,
        TriggerRange        = 800,
        ActorX              = -118040,
        ActorZ              = 1000,
        ActorY              = 24100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -117980,
        TriggerZ            = 0,
        TriggerY            = 224050,
        TriggerRange        = 800,
        ActorX              = -117980,
        ActorZ              = 1000,
        ActorY              = 224050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -117970,
        TriggerZ            = 0,
        TriggerY            = 424010,
        TriggerRange        = 800,
        ActorX              = -117970,
        ActorZ              = 1000,
        ActorY              = 424010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_29E",          # 00, 0
        "Function_1_2C9",          # 01, 1
        "Function_2_4BF",          # 02, 2
        "Function_3_7D3",          # 03, 3
        "Function_4_D7C",          # 04, 4
        "Function_5_E04",          # 05, 5
        "Function_6_E1A",          # 06, 6
        "Function_7_E30",          # 07, 7
        "Function_8_E46",          # 08, 8
        "Function_9_E95",          # 09, 9
        "Function_10_E99",         # 0A, 10
        "Function_11_E9D",         # 0B, 11
        "Function_12_EA1",         # 0C, 12
        "Function_13_EA5",         # 0D, 13
        "Function_14_EA9",         # 0E, 14
    )


    def Function_0_29E(): pass

    label("Function_0_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2AC")
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_2AC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2C0"),
        (106, "loc_2C0"),
        (112, "loc_2C0"),
        (SWITCH_DEFAULT, "loc_2C8"),
    )


    label("loc_2C0")

    OP_22(0xE, 0x0, 0x64)
    Jump("loc_2C8")

    label("loc_2C8")

    Return()

    # Function_0_29E end

    def Function_1_2C9(): pass

    label("Function_1_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30E")

    label("loc_2E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30E")

    label("loc_2F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E")
    OP_72(0x2, 0x10)
    Jump("loc_322")

    label("loc_31E")

    OP_64(0x1, 0x1)

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DA")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    PlayEffect(0x0, 0x0, 0xFF, -113730, 0, 22590, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_3DE")

    label("loc_3DA")

    OP_64(0x0, 0x1)

    label("loc_3DE")

    Jump("loc_48C")

    label("loc_3E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_43E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_43B")

    Jump("loc_48C")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_48C")

    OP_72(0x3, 0x10)
    OP_72(0x7, 0x10)
    OP_72(0xB, 0x10)
    Jump("loc_4AE")

    label("loc_49E")

    OP_64(0x0, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)

    label("loc_4AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_4BE")
    OP_B2(0x0, 0x3, 0x80)

    label("loc_4BE")

    Return()

    # Function_1_2C9 end

    def Function_2_4BF(): pass

    label("Function_2_4BF")

    EventBegin(0x0)
    OP_6D(-107370, 0, -940, 0)
    SetChrPos(0x101, -107570, 0, -2230, 0)
    SetChrPos(0x102, -108910, 0, -1630, 90)
    SetChrPos(0x107, -107270, 0, -860, 225)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#001F哎呀～\x01",
            "真没想到来的会是提妲。\x02\x03",
            "而且还是那么有名的博士的孙女。\x01",
            "刚才真是让我吃了一惊呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F我也是啊。\x01",
            "怪不得操作导力器的技术那么熟练。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F哎～嘿嘿，\x01",
            "其实也没什么啦。\x02\x03",
            "不管爷爷怎么出名也好，\x01",
            "我还只是个实习生而已啦。\x02\x03",
            "#064F啊，对了……\x02\x03",
            "你们要找爷爷谈的事，\x01",
            "和游击士的工作有关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯……\x01",
            "算是一半有关一半无关吧。\x02\x03",
            "#509F总之就是三言两语说不完的、\x01",
            "又复杂又离奇的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F详细的情况\x01",
            "还是等见到你爷爷再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊，好的，我明白了。\x02\x03",
            "#060F那个那个，\x01",
            "我家就在城镇的西南面。\x02\x03",
            "下了导力扶梯之后，\x01",
            "一直向市街区的南面走……\x02\x03",
            "#061F然后到了门口那里再向西拐就到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F明白了。\x01",
            "那么我们赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3F, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_2_4BF end

    def Function_3_7D3(): pass

    label("Function_3_7D3")

    EventBegin(0x0)
    OP_A2(0x549)
    OP_64(0x0, 0x1)
    OP_2B(0x41, 0x1)
    OP_6D(-113730, 0, 22590, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C40")
    OP_A2(0x52F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_884")

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "约修亚，这是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是刚才所说的发烟筒。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F8")

    label("loc_884")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_914")

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "约修亚，那是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯。\x01",
            "是刚才所说的发烟筒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F8")

    label("loc_914")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99E")

    ChrTalk(
        0x107,
        (
            "#065F啊……\x01",
            "哥哥，这是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是刚才所说的发烟筒。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F8")

    label("loc_99E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F8")

    ChrTalk(
        0x106,
        (
            "#057F这个……\x01",
            "就是那发烟筒吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F阿加特兄。\x01",
            "给我看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚很熟练地把发烟筒拆散了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x102, -114480, 0, 21800, 45)
    SetChrPos(0x101, -115670, 0, 21890, 90)
    SetChrPos(0x107, -114840, 0, 20630, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_A85")
    SetChrPos(0x106, -116160, 0, 20300, 0)

    label("loc_A85")

    FadeToBright(600, 0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B66")

    ChrTalk(
        0x101,
        (
            "#501F哇……\x01",
            "烟雾没有了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F约修亚哥哥，\x01",
            "好厉害……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FＯＫ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C3D")

    label("loc_B66")

    OP_A2(0x53E)

    ChrTalk(
        0x101,
        (
            "#501F哇……\x01",
            "烟雾没有了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F约修亚哥哥，\x01",
            "好厉害……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#052F哦……\x01",
            "还挺有两下子的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3D")

    Jump("loc_D79")

    label("loc_C40")

    FadeToDark(600, 0, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚很熟练地把发烟筒拆散了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetChrPos(0x102, -114480, 0, 21800, 45)
    SetChrPos(0x101, -115670, 0, 21890, 90)
    SetChrPos(0x107, -114840, 0, 20630, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_CD3")
    SetChrPos(0x106, -116160, 0, 20300, 0)

    label("loc_CD3")

    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D79")
    OP_A2(0x53E)

    ChrTalk(
        0x106,
        (
            "#052F哦……\x01",
            "还挺有两下子的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F别的地方肯定还有\x01",
            "和这个一样的发烟筒。\x02\x03",
            "找到了就把它们拆散吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D79")

    EventEnd(0x0)
    Return()

    # Function_3_7D3 end

    def Function_4_D7C(): pass

    label("Function_4_D7C")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "按了按钮，没有任何反应。\x01",
            "导力梯好像不能用了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_D7C end

    def Function_5_E04(): pass

    label("Function_5_E04")

    OP_A3(0x540)
    OP_A3(0x541)
    OP_A2(0x542)
    OP_A3(0x543)
    OP_A3(0x544)
    OP_A3(0x545)
    OP_A3(0x546)
    Return()

    # Function_5_E04 end

    def Function_6_E1A(): pass

    label("Function_6_E1A")

    OP_A3(0x540)
    OP_A3(0x541)
    OP_A3(0x542)
    OP_A2(0x543)
    OP_A3(0x544)
    OP_A3(0x545)
    OP_A3(0x546)
    Return()

    # Function_6_E1A end

    def Function_7_E30(): pass

    label("Function_7_E30")

    OP_A3(0x540)
    OP_A3(0x541)
    OP_A3(0x542)
    OP_A3(0x543)
    OP_A2(0x544)
    OP_A3(0x545)
    OP_A3(0x546)
    Return()

    # Function_7_E30 end

    def Function_8_E46(): pass

    label("Function_8_E46")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_E46 end

    def Function_9_E95(): pass

    label("Function_9_E95")

    SetPlaceName(0x94) # 中央工房　医务室
    Return()

    # Function_9_E95 end

    def Function_10_E99(): pass

    label("Function_10_E99")

    SetPlaceName(0x93) # 中央工房　医务室
    Return()

    # Function_10_E99 end

    def Function_11_E9D(): pass

    label("Function_11_E9D")

    SetPlaceName(0x96) # 中央工房　医务室
    Return()

    # Function_11_E9D end

    def Function_12_EA1(): pass

    label("Function_12_EA1")

    SetPlaceName(0x95) # 中央工房　医务室
    Return()

    # Function_12_EA1 end

    def Function_13_EA5(): pass

    label("Function_13_EA5")

    SetPlaceName(0x98) # 中央工房　医务室
    Return()

    # Function_13_EA5 end

    def Function_14_EA9(): pass

    label("Function_14_EA9")

    SetPlaceName(0x97) # 中央工房　医务室
    Return()

    # Function_14_EA9 end

    SaveToFile()

Try(main)
