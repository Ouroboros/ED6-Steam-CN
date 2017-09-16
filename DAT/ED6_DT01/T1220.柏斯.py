from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1220   ._SN',
        MapName             = 'Bose',
        Location            = 'T1220.x',
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
        '埃米尔',                               # 9
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
        'ED6_DT07/CH01040 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
    )

    DeclNpc(
        X                   = -1600,
        Z                   = -1000,
        Y                   = 7600,
        Direction           = 135,
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
        TriggerX            = -670,
        TriggerZ            = -1000,
        TriggerY            = 6680,
        TriggerRange        = 400,
        ActorX              = -1600,
        ActorZ              = 500,
        ActorY              = 7600,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F6",           # 00, 0
        "Function_1_F7",           # 01, 1
        "Function_2_F8",           # 02, 2
        "Function_3_10E",          # 03, 3
        "Function_4_18B",          # 04, 4
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Return()

    # Function_0_F6 end

    def Function_1_F7(): pass

    label("Function_1_F7")

    Return()

    # Function_1_F7 end

    def Function_2_F8(): pass

    label("Function_2_F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_F8")

    label("loc_10D")

    Return()

    # Function_2_F8 end

    def Function_3_10E(): pass

    label("Function_3_10E")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E")
    OP_0D()
    OP_A9(0xE)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_16E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F")
    TalkEnd(0x8)
    Return()

    label("loc_17F")

    Call(0, 4)
    OP_8C(0x8, 135, 0)
    Return()

    # Function_3_10E end

    def Function_4_18B(): pass

    label("Function_4_18B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1FC")

    ChrTalk(
        0x8,
        (
            "现在，在果树园工作的人\x01",
            "都聚集在村长的家里，\x01",
            "好像在一起商量什么事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_815")

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "这个村子里，\x01",
            "除了库赖爷爷和贝斯卡经常吵架，\x01",
            "其他时间都十分安静和平。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "帝国军到来之前，\x01",
            "这个村子就和现在一样\x01",
            "又平静又祥和…… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "所以，\x01",
            "我有时候会觉得现在的这种和平\x01",
            "总有一天会被打破。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E6")

    label("loc_330")


    ChrTalk(
        0x8,
        (
            "就在帝国军来之前不多久，\x01",
            "村子曾经非常和平安稳……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "所以，\x01",
            "我有时候会觉得现在的这种和平\x01",
            "总有一天会被打破。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E6")

    Jump("loc_815")

    label("loc_3E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_504")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_492")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "王国军的人到这里来过，\x01",
            "是不是发生什么事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我听说之前来调查的时候，\x01",
            "也没有找到什么东西……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_501")

    label("loc_492")


    ChrTalk(
        0x8,
        (
            "穿军服的人进进出出，\x01",
            "我总觉得有些莫名的不安。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_501")

    Jump("loc_815")

    label("loc_504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_64F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F0")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "我也想在柏斯超市里\x01",
            "开一家小店啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不过还是故乡最适合定居。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这里商品的进货不太方便，\x01",
            "非常辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64C")

    label("loc_5F0")


    ChrTalk(
        0x8,
        (
            "在青空市场时代我学到了很多东西，\x01",
            "现在想想真是非常有用啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64C")

    Jump("loc_815")

    label("loc_64F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_6CC")

    ChrTalk(
        0x8,
        (
            "百日战争的时候，\x01",
            "连幼小的孩童都难以生还。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "现在想起来心里还是很难过。\x02",
    )

    CloseMessageWindow()
    Jump("loc_815")

    label("loc_6CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_7AD")

    ChrTalk(
        0x8,
        (
            "这个村子和帝国邻近，\x01",
            "所以战争的时候最先被占领。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "有很多人在战争中牺牲了，\x01",
            "直到如今，村子的伤疤仍然没有痊愈。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_815")

    label("loc_7AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_815")

    ChrTalk(
        0x8,
        "哟，我没见过你们呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "欢迎来到拉文努村！\x02",
    )

    CloseMessageWindow()

    label("loc_815")

    OP_56(0x0)
    TalkEnd(0x8)
    Sleep(300)
    Return()

    # Function_4_18B end

    SaveToFile()

Try(main)
