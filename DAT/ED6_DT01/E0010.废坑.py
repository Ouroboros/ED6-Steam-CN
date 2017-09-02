from ED6ScenarioHelper import *

def main():
    # 废坑

    CreateScenaFile(
        FileName            = 'E0010   ._SN',
        MapName             = 'event',
        Location            = 'E0010.x',
        MapIndex            = 49,
        MapDefaultBGM       = "ed60030",
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
        Unknown_3A              = 49,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclActor(
        TriggerX            = 58996,
        TriggerZ            = -448,
        TriggerY            = 48932,
        TriggerRange        = 1700,
        ActorX              = 58920,
        ActorZ              = -200,
        ActorY              = 49040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59075,
        TriggerZ            = -2000,
        TriggerY            = 54692,
        TriggerRange        = 1700,
        ActorX              = 59075,
        ActorZ              = -1600,
        ActorY              = 54692,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25983,
        TriggerZ            = 200,
        TriggerY            = -8664,
        TriggerRange        = 1700,
        ActorX              = 25510,
        ActorZ              = 1200,
        ActorY              = -8070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 84719,
        TriggerZ            = 0,
        TriggerY            = 44588,
        TriggerRange        = 1700,
        ActorX              = 84719,
        ActorZ              = 2000,
        ActorY              = 44588,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 89364,
        TriggerZ            = -1000,
        TriggerY            = 53636,
        TriggerRange        = 1700,
        ActorX              = 89364,
        ActorZ              = -600,
        ActorY              = 53636,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33110,
        TriggerZ            = 0,
        TriggerY            = 5650,
        TriggerRange        = 1700,
        ActorX              = 33110,
        ActorZ              = 1500,
        ActorY              = 5650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_182",          # 00, 0
        "Function_1_1BC",          # 01, 1
        "Function_2_1E1",          # 02, 2
        "Function_3_3A2",          # 03, 3
        "Function_4_4D6",          # 04, 4
        "Function_5_5BD",          # 05, 5
        "Function_6_6F6",          # 06, 6
        "Function_7_7F5",          # 07, 7
        "Function_8_8F6",          # 08, 8
    )


    def Function_0_182(): pass

    label("Function_0_182")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_19A"),
        (109, "loc_1A9"),
        (115, "loc_1AF"),
        (105, "loc_1B5"),
        (SWITCH_DEFAULT, "loc_1BB"),
    )


    label("loc_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6")
    Event(0, 2)

    label("loc_1A6")

    Jump("loc_1BB")

    label("loc_1A9")

    OP_A2(0x323)
    Jump("loc_1BB")

    label("loc_1AF")

    OP_A2(0x324)
    Jump("loc_1BB")

    label("loc_1B5")

    OP_A2(0x325)
    Jump("loc_1BB")

    label("loc_1BB")

    Return()

    # Function_0_182 end

    def Function_1_1BC(): pass

    label("Function_1_1BC")

    OP_72(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_END)), "loc_1E0")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)

    label("loc_1E0")

    Return()

    # Function_1_1BC end

    def Function_2_1E1(): pass

    label("Function_2_1E1")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(30980, 0, -4620, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 27350, 0, 5680, 103)
    SetChrPos(0x102, 26450, 0, 5010, 114)
    SetChrPos(0x103, 27280, 0, 4760, 101)

    def lambda_25E():
        OP_6C(65000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25E)
    OP_6D(29950, 0, 4840, 4000)

    ChrTalk(
        0x101,
        (
            "#505F哇～……\x01",
            "空荡荡了。\x02\x03",
            "一点货物也不剩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F好像都被那些空贼给搬运走了。\x01",
            "　\x02\x03",
            "这样的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F……不管怎么样，\x01",
            "先到处调查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38B():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38B)
    OP_69(0x0, 0x5DC)
    OP_A2(0x321)
    EventEnd(0x0)
    Return()

    # Function_2_1E1 end

    def Function_3_3A2(): pass

    label("Function_3_3A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464")
    EventBegin(0x0)
    OP_6D(58996, -448, 48932, 1000)

    ChrTalk(
        0x101,
        (
            "#501F这好像是机长的座位吧。\x02\x03",
            "#007F如果是平常的话，\x01",
            "真想高兴地坐坐看呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F还是不要坐了吧。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_4D2")

    label("loc_464")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机长席上没有人坐着。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_4D2")

    OP_A2(0x0)
    Return()

    # Function_3_3A2 end

    def Function_4_4D6(): pass

    label("Function_4_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_560")
    EventBegin(0x0)
    OP_6D(59075, -2000, 54692, 1000)

    ChrTalk(
        0x101,
        (
            "#505F这个是操纵用的舵轮吧。\x02\x03",
            "操作的人……\x01",
            "现在在哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_5B9")

    label("loc_560")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是操纵用的舵轮。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_5B9")

    OP_A2(0x1)
    Return()

    # Function_4_4D6 end

    def Function_5_5BD(): pass

    label("Function_5_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66D")
    EventBegin(0x0)
    OP_6D(25983, 200, -8664, 1000)

    ChrTalk(
        0x101,
        "#004F这是什么东西呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F嗯……\x01",
            "是导力引擎的控制面板。\x02\x03",
            "看起来，\x01",
            "导力已经完全切断了……\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_6F2")

    label("loc_66D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是导力引擎的控制面板。\x01",
            "   \x02\x03",
            "导力完全停止了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_6F2")

    OP_A2(0x2)
    Return()

    # Function_5_5BD end

    def Function_6_6F6(): pass

    label("Function_6_6F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AE")
    EventBegin(0x0)
    OP_6D(33110, 0, 5650, 1000)

    ChrTalk(
        0x101,
        "#004F这个是起重车吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F和在洛连特飞艇坪\x01",
            "见过的是同一种型号呢。\x02\x03",
            "大概就是用这种东西\x01",
            "把货物运出去的吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_7F1")

    label("loc_7AE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是运输货物的起重车。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_7F1")

    OP_A2(0x5)
    Return()

    # Function_6_6F6 end

    def Function_7_7F5(): pass

    label("Function_7_7F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AC")
    EventBegin(0x0)
    OP_6D(84719, 1000, 44588, 1000)

    ChrTalk(
        0x101,
        (
            "#505F这个盆栽……\x01",
            "好像没什么生气呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F应该已经好几天\x01",
            "没有浇水了吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_8F2")

    label("loc_8AC")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "盆栽已经有些枯萎了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_8F2")

    OP_A2(0x3)
    Return()

    # Function_7_7F5 end

    def Function_8_8F6(): pass

    label("Function_8_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_969")
    EventBegin(0x0)
    OP_6D(89364, -600, 53636, 1000)

    ChrTalk(
        0x101,
        (
            "#003F好刺眼……\x01",
            "有光线射进来……\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_9B3")

    label("loc_969")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从外面有光线射进来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_9B3")

    OP_A2(0x4)
    Return()

    # Function_8_8F6 end

    SaveToFile()

Try(main)
