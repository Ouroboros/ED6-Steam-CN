from ED6ScenarioHelper import *

def main():
    # 洛连特旅馆

    CreateScenaFile(
        FileName            = 'T0132   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0132.x',
        MapIndex            = 8,
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
        '伟诺',                                 # 9
        '穿制服的少女',                         # 10
        '西加罗',                               # 11
        '艾德尔',                               # 12
        '目标用摄像机',                         # 13
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
        Unknown_3A              = 8,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 8000,
        Unknown_04              = 0,
        Unknown_08              = 181000,
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
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01560 ._CH',             # 00
        'ED6_DT07/CH02330 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01560P._CP',             # 00
        'ED6_DT07/CH02330P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 0,
        Y                   = 190662,
        Direction           = 90,
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
        X                   = -88400,
        Z                   = 0,
        Y                   = 155930,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -48500,
        Z                   = 0,
        Y                   = 155890,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -44250,
        Z                   = 0,
        Y                   = 152480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TriggerX            = 6598,
        TriggerZ            = 0,
        TriggerY            = 190158,
        TriggerRange        = 1000,
        ActorX              = 4500,
        ActorZ              = 1500,
        ActorY              = 190662,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3130,
        TriggerZ            = 0,
        TriggerY            = 192000,
        TriggerRange        = 800,
        ActorX              = 3130,
        ActorZ              = 1000,
        ActorY              = 192000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_257",          # 01, 1
        "Function_2_282",          # 02, 2
        "Function_3_298",          # 03, 3
        "Function_4_2BC",          # 04, 4
        "Function_5_2E0",          # 05, 5
        "Function_6_334",          # 06, 6
        "Function_7_388",          # 07, 7
        "Function_8_3DC",          # 08, 8
        "Function_9_3E1",          # 09, 9
        "Function_10_1540",        # 0A, 10
        "Function_11_1886",        # 0B, 11
        "Function_12_19AC",        # 0C, 12
        "Function_13_1D95",        # 0D, 13
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20A")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_21B")

    label("loc_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21B")
    ClearChrFlags(0x9, 0x80)

    label("loc_21B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_225")
    Jump("loc_24A")

    label("loc_225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_239")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_24A")

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_24A")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_256")
    ClearChrFlags(0x9, 0x10)

    label("loc_256")

    Return()

    # Function_0_1F6 end

    def Function_1_257(): pass

    label("Function_1_257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26F")
    OP_B1("t0132_y")
    Jump("loc_278")

    label("loc_26F")

    OP_B1("t0132_n")

    label("loc_278")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    Return()

    # Function_1_257 end

    def Function_2_282(): pass

    label("Function_2_282")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_297")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_282")

    label("loc_297")

    Return()

    # Function_2_282 end

    def Function_3_298(): pass

    label("Function_3_298")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BB")
    OP_8D(0xFE, -86000, 151900, -82840, 154200, 3000)
    Jump("Function_3_298")

    label("loc_2BB")

    Return()

    # Function_3_298 end

    def Function_4_2BC(): pass

    label("Function_4_2BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DF")
    OP_8D(0xFE, -46100, 153900, -42900, 151500, 3000)
    Jump("Function_4_2BC")

    label("loc_2DF")

    Return()

    # Function_4_2BC end

    def Function_5_2E0(): pass

    label("Function_5_2E0")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A2(0x3)
    Jump("loc_32E")

    label("loc_328")

    OP_82(0x80, 0x2)
    OP_A3(0x3)

    label("loc_32E")

    ClearMapFlags(0x80)
    Return()

    # Function_5_2E0 end

    def Function_6_334(): pass

    label("Function_6_334")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C")
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A2(0x4)
    Jump("loc_382")

    label("loc_37C")

    OP_82(0x81, 0x2)
    OP_A3(0x4)

    label("loc_382")

    ClearMapFlags(0x80)
    Return()

    # Function_6_334 end

    def Function_7_388(): pass

    label("Function_7_388")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0")
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A2(0x5)
    Jump("loc_3D6")

    label("loc_3D0")

    OP_82(0x82, 0x2)
    OP_A3(0x5)

    label("loc_3D6")

    ClearMapFlags(0x80)
    Return()

    # Function_7_388 end

    def Function_8_3DC(): pass

    label("Function_8_3DC")

    Call(0, 9)
    Return()

    # Function_8_3DC end

    def Function_9_3E1(): pass

    label("Function_9_3E1")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_END)), "loc_459")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_448")
    OP_0D()
    OP_A9(0x3)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_448")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_459")
    TalkEnd(0x8)
    Return()

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "咦……\x01",
            "这副装束……难道你们要去旅行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "可是，\x01",
            "定期船已经停止航运了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，\x01",
            "其实我们打算走路到柏斯去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们有一些事情要到那里去调查。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哦哦，难道说\x01",
            "你们有什么紧要的工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "啊，不好意思多问了。\x01",
            "不管怎样，请你们路上多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_672")

    label("loc_5CD")


    ChrTalk(
        0x8,
        (
            "今天早上就已经有几位乘客\x01",
            "步行向着柏斯方向走去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "定期船停航之后，\x01",
            "的确引来诸多的不便啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_672")

    Jump("loc_1537")

    label("loc_675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_8DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86A")
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚。\x01",
            "啊，连雪拉扎德也来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "发生什么事了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F伟诺叔叔，你认识乔丝特吗？\x02\x03",
            "#002F就是住在你们这里的\x01",
            "那个王立学院女学生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "当然认识啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过她……\x01",
            "刚才已经结帐离开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#022F啊，来迟一步了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F去飞艇坪看看吧，\x01",
            "说不定还来得及。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唔～\x01",
            "我怎么看不出来她是个坏孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "？？？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x262)
    OP_28(0x1B, 0x1, 0x4)
    OP_28(0x1B, 0x1, 0x8)
    EventEnd(0x1)
    Jump("loc_8DB")

    label("loc_86A")


    ChrTalk(
        0x8,
        (
            "乔丝特小姐在刚才\x01",
            "已经办理退房手续了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "也许是我心里作用，\x01",
            "看她样子好像要急着回去……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DB")

    Jump("loc_1537")

    label("loc_8DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A4")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚。\x01",
            "我听说了你们在农场和矿山有活跃的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "连客人中也有人\x01",
            "想打听你们俩的事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "今后也要努力哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A19")

    label("loc_9A4")


    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚。\x01",
            "我听说了你们在农场和矿山有活跃的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "今后也要努力哦。\x02",
    )

    CloseMessageWindow()

    label("loc_A19")

    Jump("loc_1537")

    label("loc_A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_AED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_A95")

    ChrTalk(
        0x8,
        (
            "看来你们\x01",
            "顺利找到那些记者了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "要努力工作哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AEA")

    label("loc_A95")


    ChrTalk(
        0x8,
        (
            "怎么了？\x01",
            "你们找到\x01",
            "那些记者了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEA")

    Jump("loc_1537")

    label("loc_AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_E17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA5")
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    OP_A2(0x251)
    OP_28(0x19, 0x1, 0x4)

    ChrTalk(
        0x101,
        (
            "#000F伟诺叔叔。\x01",
            "我想问一件事情……\x02\x03",
            "#000F杂志社的那两个记者\x01",
            "是住在这里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦，你竟然知道这个啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "有什么事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F其实是协会委派的工作，\x01",
            "我们是为协助他们取材而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过现在……\x01",
            "那两个人都出去了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F这样啊。\x01",
            "那你知道他们去了哪里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那位记者的话，\x01",
            "好像说过要去酒馆……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你们就去那里看看吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F酒馆是吗，谢谢了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我们先告辞了。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_E14")

    label("loc_DA5")


    ChrTalk(
        0x8,
        (
            "那位记者的话，\x01",
            "好像说过要去酒馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你们就去那里看看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_E14")

    Jump("loc_1537")

    label("loc_E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_E9C")

    ChrTalk(
        0x8,
        (
            "今天有两位王都的记者\x01",
            "在本旅馆预定了房间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "看看时间，\x01",
            "他们差不多该到了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1537")

    label("loc_E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_F59")

    ChrTalk(
        0x8,
        (
            "本旅馆时常\x01",
            "会有各地的游击士\x01",
            "来这里下榻住宿的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "常常会有所属于\x01",
            "其它支部的游击士\x01",
            "被派遣到这里来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1537")

    label("loc_F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1074")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100D")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "前台工作\x01",
            "总算告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "定期船起飞和到达前后\x01",
            "出入的客人果然是最多的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1071")

    label("loc_100D")


    ChrTalk(
        0x8,
        (
            "定期船起飞和到达前后\x01",
            "出入的客人果然是最多的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1071")

    Jump("loc_1537")

    label("loc_1074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112B")
    OP_A2(0x0)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "艾丝蒂尔，我听说了哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你们终于成为游击士了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我从心底祝福你们，\x01",
            "希望你们将来能够大展身手呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F……嗯，非常感谢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_118E")

    label("loc_112B")


    ChrTalk(
        0x8,
        "你们终于成为游击士了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我从心底祝福你们，\x01",
            "希望你们将来能够大展身手呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118E")

    Jump("loc_1537")

    label("loc_1191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_12D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1258")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "刚才有一位\x01",
            "稀罕的客人来住宿哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "怎么看都是\x01",
            "杰尼丝王立学院的学生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "好像是为了学习，\x01",
            "专门来洛连特\x01",
            "做什么调查研究的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D3")

    label("loc_1258")


    ChrTalk(
        0x8,
        (
            "刚才有一位\x01",
            "稀罕的客人来住宿哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "怎么看都是\x01",
            "杰尼丝王立学院的学生。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D3")

    Jump("loc_1537")

    label("loc_12D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1499")

    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "这里是洛连特旅馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "两位是来住宿的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊？那个……！？\x01",
            "伟诺叔叔，是我们啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x8,
        (
            "哈哈，我知道。\x01",
            "开玩笑的，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "刚才那个只是练习问好而已。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(700)

    ChrTalk(
        0x101,
        "#008F是、是这样啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#007F（伟诺叔叔还真是喜欢\x01",
            "　一本正经地开玩笑啊。）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（……喜欢开玩笑也\x01",
            "　不算什么坏习惯嘛。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1537")

    label("loc_1499")


    ChrTalk(
        0x8,
        (
            "艾丝蒂尔游击士测试合格之后，\x01",
            "就会成为继雪拉扎德小姐之后\x01",
            "洛连特的第二位女性游击士了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "约修亚，\x01",
            "你也要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1537")

    OP_A2(0x229)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    # Function_9_3E1 end

    def Function_10_1540(): pass

    label("Function_10_1540")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DE")
    OP_A2(0x1)

    NpcTalk(
        0x9,
        "乔丝特",
        (
            "#217F啊，艾丝蒂尔，\x01",
            "还有约修亚……\x02\x03",
            "你们是来\x01",
            "找我玩的吗？\x02\x03",
            "不介意的话，\x01",
            "我给你们泡杯红茶吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1645")

    label("loc_15DE")


    NpcTalk(
        0x9,
        "乔丝特",
        (
            "#217F啊，艾丝蒂尔，\x01",
            "还有约修亚……\x02\x03",
            "你们是来\x01",
            "找我玩的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1645")

    Jump("loc_1882")

    label("loc_1648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_16AB")

    ChrTalk(
        0x9,
        (
            "#217F我应该在教会。\x01",
            "看到这句台词就表示有BUG。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1882")

    label("loc_16AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_16FE")

    ChrTalk(
        0x9,
        (
            "好了，\x01",
            "得去跟市长做个预约了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1882")

    label("loc_16FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_179C")

    ChrTalk(
        0x9,
        (
            "市长官邸在城镇东面……\x01",
            "游击士协会在钟楼的南面。\x02\x03",
            "城镇的地理位置\x01",
            "我基本上弄清楚了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1882")

    label("loc_179C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1816")

    ChrTalk(
        0x9,
        (
            "呼……\x01",
            "终于抵达洛连特了呢。\x02\x03",
            "那么，\x01",
            "首先要到处逛逛才行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1882")

    label("loc_1816")


    ChrTalk(
        0x9,
        (
            "#217F我在这个时候\x01",
            "应该还没有到达洛连特这里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#217F所以……\x01",
            "请装作没看见我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1882")

    TalkEnd(0x9)
    Return()

    # Function_10_1540 end

    def Function_11_1886(): pass

    label("Function_11_1886")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1938")

    ChrTalk(
        0xFE,
        (
            "我们准备乘坐\x01",
            "下一班的定期船去柏斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近柏斯好像\x01",
            "发生了不少事件，\x01",
            "有些不放心啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A8")

    label("loc_1938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_19A8")

    ChrTalk(
        0xFE,
        (
            "本来只是为了巡礼才来的，\x01",
            "没想到洛连特还真是个\x01",
            "地灵人杰的好地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我很喜欢呢。\x02",
    )

    CloseMessageWindow()

    label("loc_19A8")

    TalkEnd(0xA)
    Return()

    # Function_11_1886 end

    def Function_12_19AC(): pass

    label("Function_12_19AC")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1BD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4E")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "接下来终于要去柏斯地区了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起柏斯的话，\x01",
            "果然还是柏斯超市最吸引我啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说店里摆满了各种\x01",
            "来自帝国的稀奇物品呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "为了这一天我一直在筹私房钱呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "准备充足，干劲充足，\x01",
            "钱包充～足！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "向柏斯超市出击！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BD4")

    label("loc_1B4E")


    ChrTalk(
        0xFE,
        (
            "准备充足，干劲充足，\x01",
            "钱包充～足！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "向柏斯超市出击！\x02",
    )

    CloseMessageWindow()

    label("loc_1BD4")

    Jump("loc_1D91")

    label("loc_1BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1D91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE8")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "这旅馆比想象中的要好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "主管的服务很周到，\x01",
            "而且又安静又整洁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和王都的高级酒店相比\x01",
            "一点都不逊色呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D91")

    label("loc_1CE8")


    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "这旅馆比想象中的要好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和王都的高级酒店相比\x01",
            "一点都不逊色呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D91")

    TalkEnd(0xB)
    Return()

    # Function_12_19AC end

    def Function_13_1D95(): pass

    label("Function_13_1D95")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　　　　洗衣房　　　　　　　\x01",
            "※工作人员以外禁止进入。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_1D95 end

    SaveToFile()

Try(main)
