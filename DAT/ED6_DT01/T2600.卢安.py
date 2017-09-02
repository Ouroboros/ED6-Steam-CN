from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2600   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2600   ._SN',
            'ED6_DT01/T2600_1 ._SN',
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
        '基库',                                 # 9
        '米克',                                 # 10
        '艾福托老师',                           # 11
        '王立学院·小道',                       # 12
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
        'ED6_DT07/CH02320 ._CH',             # 00
        'ED6_DT07/CH01080 ._CH',             # 01
        'ED6_DT07/CH01460 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02320P._CP',             # 00
        'ED6_DT07/CH01080P._CP',             # 01
        'ED6_DT07/CH01460P._CP',             # 02
    )

    DeclNpc(
        X                   = 800,
        Z                   = 6000,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = -6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 300,
        Z                   = 0,
        Y                   = -3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 170,
        Z                   = 0,
        Y                   = -16239,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -2090,
        Y                   = -1000,
        Z                   = 4090,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x8C0,
        Unknown_18          = 0x10000,
        Unknown_1C          = 0,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 1000,
        TriggerY            = 9720,
        TriggerRange        = 800,
        ActorX              = 0,
        ActorZ              = 2000,
        ActorY              = 9720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33200,
        TriggerZ            = 0,
        TriggerY            = 14410,
        TriggerRange        = 1000,
        ActorX              = 32509,
        ActorZ              = 0,
        ActorY              = 14410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1AA",          # 00, 0
        "Function_1_1F2",          # 01, 1
        "Function_2_27D",          # 02, 2
        "Function_3_BC1",          # 03, 3
        "Function_4_C10",          # 04, 4
    )


    def Function_0_1AA(): pass

    label("Function_0_1AA")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_1BA"),
        (103, "loc_1DB"),
        (SWITCH_DEFAULT, "loc_1F1"),
    )


    label("loc_1BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D8")
    OP_28(0x27, 0x1, 0x8000)
    Event(1, 2)

    label("loc_1D8")

    Jump("loc_1F1")

    label("loc_1DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EE")
    OP_A2(0x433)
    Event(0, 2)

    label("loc_1EE")

    Jump("loc_1F1")

    label("loc_1F1")

    Return()

    # Function_0_1AA end

    def Function_1_1F2(): pass

    label("Function_1_1F2")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE61F0, 0x3004E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_225")
    OP_B1("t2600_y")
    Jump("loc_22E")

    label("loc_225")

    OP_B1("t2600_n")

    label("loc_22E")

    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_246")
    OP_64(0x0, 0x1)
    OP_71(0x0, 0x10)
    Jump("loc_263")

    label("loc_246")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_263")
    OP_64(0x0, 0x1)
    OP_71(0x0, 0x10)

    label("loc_263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275")
    OP_6F(0x2, 0)
    Jump("loc_27C")

    label("loc_275")

    OP_6F(0x2, 60)

    label("loc_27C")

    Return()

    # Function_1_1F2 end

    def Function_2_27D(): pass

    label("Function_2_27D")

    SetMapFlags(0x10000000)
    AddParty(0x1, 0xFF)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(29000, 5000, 27750, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 28100, 5000, 28150, 90)
    SetChrPos(0x101, 15980, 5000, 27660, 0)
    SetChrPos(0x105, 15980, 5000, 28860, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#013F#5P奇怪了……\x01",
            "刚才还看到这里有动静的……\x02\x03",
            "#013F……但是，难道说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4P约修亚～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_382():
        OP_6D(27000, 5000, 28210, 2000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_382)

    def lambda_39A():
        OP_8E(0xFE, 0x68E2, 0x1388, 0x6C0C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39A)
    TurnDirection(0x102, 0x101, 400)
    Sleep(200)
    OP_8E(0x105, 0x672A, 0x1388, 0x70BC, 0x1388, 0x0)
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x102,
        "#014F艾丝蒂尔、科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#1P真是的，\x01",
            "别惹人担心嘛！\x02\x03",
            "听说你去追那个银发男子，\x01",
            "吓了我们一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F咦？……你们怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F是波利告诉我们的。\x01",
            "说你看到了那个银发男子。\x02\x03",
            "因为那孩子好像也看见了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是吗，好敏锐的孩子……\x02\x03",
            "#013F我隐约看见一个背影，\x01",
            "然后一直追到了这里来了……\x02\x03",
            "可惜被他甩掉了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#1P居然能把约修亚甩掉，\x01",
            "看来那家伙不会是普通人。\x02\x03",
            "他到底是什么人呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F……不知道。\x02\x03",
            "#010F不过，我想他应该不是\x01",
            "纵火烧孤儿院的犯人。\x02\x03",
            "但这也只是我的直觉而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#1P是吗……\x02\x03",
            "#007F不过话说回来……\x01",
            "为什么要一个人行动啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F的确是啊。\x02\x03",
            "至少也应该\x01",
            "给我们捎个口信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F对不起。\x01",
            "让你们为我担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F#1P也、也没有特别担心啦。\x02\x03",
            "只是想告诉你\x01",
            "团队合作的重要性啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F呵呵呵，真不坦率。\x02\x03",
            "我看见你刚才\x01",
            "明明就是一副很慌乱的样子。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#008F哪、哪有这回事。\x02\x03",
            "科洛丝你才是呢，\x01",
            "刚才一副那～么严肃的表情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#542F那、那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈……\x01",
            "总之谢谢你们两个了。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xC4, 0x0, 0x50)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x102, 180, 400)
    OP_8C(0x101, 180, 400)
    OP_8C(0x105, 180, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……现在播送通知。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请舞台剧的演出人员和工作人员\x01",
            "马上前往礼堂开始准备。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "重复一遍。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请舞台剧的演出人员和工作人员\x01",
            "马上前往礼堂开始准备。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#006F是啊……\x01",
            "已经这个时候了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F是啊，我想换完服装之后，\x01",
            "舞台剧就会马上开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F好～啦，\x01",
            "终于轮到我们上阵了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F#1P啊……\x01",
            "那个银发男子怎么办？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 135, 0)
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x102,
        (
            "#013F是啊……\x02\x03",
            "看来只能通知卡露娜小姐，\x01",
            "让她帮我们留意一下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们将银发男子的事情告诉卡露娜之后，\x01",
            "就接着赶去了礼堂。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "３０分钟之后……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    ClearMapFlags(0x800)
    OP_28(0x3D, 0x1, 0x2000)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T2523   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_27D end

    def Function_3_BC1(): pass

    label("Function_3_BC1")

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

    # Function_3_BC1 end

    def Function_4_C10(): pass

    label("Function_4_C10")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_C86")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4C9)
    Jump("loc_CFC")

    label("loc_C86")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_CFC")

    Jump("loc_D30")

    label("loc_CFF")

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
    OP_83(0xF, 0xA2)

    label("loc_D30")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C10 end

    SaveToFile()

Try(main)
