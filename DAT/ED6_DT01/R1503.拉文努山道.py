from ED6ScenarioHelper import *

def main():
    # 拉文努山道

    CreateScenaFile(
        FileName            = 'R1503   ._SN',
        MapName             = 'Bose',
        Location            = 'R1503.x',
        MapIndex            = 59,
        MapDefaultBGM       = "ed60022",
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
        '王国军士兵',                           # 9
        '拉文努山道方向',                       # 10
        '拉文努山道方向',                       # 11
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
        Unknown_3A              = 59,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
    )

    DeclNpc(
        X                   = -112680,
        Z                   = -50,
        Y                   = 21490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -111060,
        Z                   = -20,
        Y                   = -19200,
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

    DeclNpc(
        X                   = 1140,
        Z                   = 10,
        Y                   = -19200,
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
        X                   = -112190,
        Y                   = -1000,
        Z                   = 23280,
        Range               = -106880,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x619E,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = 2000,
        TriggerZ            = 0,
        TriggerY            = 22680,
        TriggerRange        = 1700,
        ActorX              = 2100,
        ActorZ              = 1000,
        ActorY              = 23270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -114320,
        TriggerZ            = 0,
        TriggerY            = 6860,
        TriggerRange        = 1500,
        ActorX              = -114320,
        ActorZ              = 50,
        ActorY              = 6860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2180,
        TriggerZ            = 0,
        TriggerY            = 6860,
        TriggerRange        = 1500,
        ActorX              = -2180,
        ActorZ              = 50,
        ActorY              = 6860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19E",          # 00, 0
        "Function_1_1AB",          # 01, 1
        "Function_2_1F4",          # 02, 2
        "Function_3_20A",          # 03, 3
        "Function_4_272",          # 04, 4
        "Function_5_DCD",          # 05, 5
        "Function_6_F40",          # 06, 6
    )


    def Function_0_19E(): pass

    label("Function_0_19E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1AA")
    ClearChrFlags(0x8, 0x80)

    label("loc_1AA")

    Return()

    # Function_0_19E end

    def Function_1_1AB(): pass

    label("Function_1_1AB")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1BF"),
        (101, "loc_1D9"),
        (102, "loc_1D9"),
        (SWITCH_DEFAULT, "loc_1F3"),
    )


    label("loc_1BF")

    OP_16(0x2, 0xFA0, 0xFFFE0FE8, 0xFFFE2758, 0x3006B)
    ClearChrFlags(0x9, 0x4)
    Jump("loc_1F3")

    label("loc_1D9")

    OP_16(0x2, 0xFA0, 0xFFFC5A68, 0xFFFE2758, 0x30022)
    ClearChrFlags(0xA, 0x4)
    Jump("loc_1F3")

    label("loc_1F3")

    Return()

    # Function_1_1AB end

    def Function_2_1F4(): pass

    label("Function_2_1F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_209")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1F4")

    label("loc_209")

    Return()

    # Function_2_1F4 end

    def Function_3_20A(): pass

    label("Function_3_20A")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "现在王国军队\x01",
            "正在里面进行现场勘查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不允许平民进入。\x01",
            "当然游击士也包含在内。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_3_20A end

    def Function_4_272(): pass

    label("Function_4_272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_27C")
    Jump("loc_DCC")

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_END)), "loc_53D")
    EventBegin(0x0)
    OP_A2(0x31F)
    OP_28(0x36, 0x1, 0x100)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上套着一把结实的挂锁，\x01",
            "入口被紧紧地封住了。 \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_339")

    ChrTalk(
        0x101,
        (
            "#000F好了，赶快用从村长\x01",
            "那里借来的钥匙开门吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2")

    label("loc_339")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_374")

    ChrTalk(
        0x102,
        "#010F用借来的钥匙吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B2")

    label("loc_374")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2")

    ChrTalk(
        0x103,
        "#020F那么，用钥匙试试看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3B2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x73, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "使用了\x07\x02",
            "废坑的钥匙\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x6E, 0x0, 0x64)
    OP_6D(-110000, 0, 21330, 0)
    SetChrPos(0x101, -110000, 0, 21330, 0)
    SetChrPos(0x102, -110700, 0, 20190, 0)
    SetChrPos(0x103, -109100, 0, 20200, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F呼，好结实的门啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F那么……\x01",
            "我们赶快进去调查吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F空贼就不用说了，\x01",
            "这里好像还有魔兽出没的迹象。\x02\x03",
            "要集中注意力才行哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x4)
    OP_16(0x2, 0xFA0, 0xFFFC5A68, 0xFFFE2758, 0x30022)
    ClearChrFlags(0xA, 0x4)
    EventEnd(0x0)
    Jump("loc_DCC")

    label("loc_53D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_5A3")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上套着一把结实的挂锁，\x01",
            "入口被紧紧地封住了。 \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_DCC")

    label("loc_5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_D70")
    OP_A2(0x31D)
    OP_28(0x36, 0x1, 0x20)
    OP_28(0x36, 0x1, 0x40)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6D(2610, 0, 22670, 0)
    SetChrPos(0x101, 2298, 0, 22143, 0)
    SetChrPos(0x102, 1217, 0, 21146, 0)
    SetChrPos(0x103, 2841, 0, 20998, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上套着一把结实的挂锁，\x01",
            "入口被紧紧地封住了。 \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x102,
        "#010F这里似乎就是废坑的入口了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#1P确实，这里有着和\x01",
            "玛鲁加矿山一样的气氛……\x02\x03",
            "相当的荒凉啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F这里好像很早以前就被封闭了。\x02\x03",
            "锁销和锁头都生锈了。\x01",
            "没有近期内被打开过的痕迹呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F也就是说，\x01",
            "那些空贼不会从这门进入……\x02\x03",
            "所以军队也就没有调查这里面是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#1P嗯，就算调查矿山里面\x01",
            "也应该找不到什么线索…… \x02\x03",
            "#002F…………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F怎么了，艾丝蒂尔？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 181, 400)

    ChrTalk(
        0x101,
        (
            "#002F#1P是不是我神经过敏呢……\x02\x03",
            "从里面，好像有风吹过来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F里面？是从废坑的里面？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#1P嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F等一下……\x02",
    )

    CloseMessageWindow()

    def lambda_9A3():

        label("loc_9A3")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_9A3")

    QueueWorkItem2(0x101, 1, lambda_9A3)
    OP_8E(0x102, 0x4B0, 0x0, 0x588E, 0x7D0, 0x0)
    OP_44(0x101, 0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚把食指放在口中吮了一下，\x01",
            "然后竖在门边。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x102,
        "#015F………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x102,
        (
            "#014F真的……\x01",
            "虽然很微弱，但确实有风过吹来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#1P啊，没错吧？\x02",
    )

    CloseMessageWindow()

    def lambda_AE4():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE4)

    ChrTalk(
        0x103,
        (
            "#023F你呀，时不时地让人吃一惊，\x01",
            "感觉还真是敏锐呢。\x02\x03",
            "#021F真不愧是老师的女儿。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        (
            "#007F#1P这和老爸才没有关系呢。\x02\x03",
            "#006F不过这里面……\x01",
            "你们不觉得有点可疑吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊，\x01",
            "也许这里能通向哪里也说不定。\x02\x03",
            "看起来有调查一下的价值。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        (
            "#001F#1P好了，就这么决定，\x01",
            "我们赶快把锁给砸开……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F喂喂，先别急。\x02\x03",
            "#020F总之还是先回村子\x01",
            "和村长商量一下再说吧。\x02\x03",
            "说不定他有钥匙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#1P唉～真是遗憾。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_DCC")

    label("loc_D70")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上套着一把结实的挂锁，\x01",
            "入口被紧紧地封住了。 \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_DCC")

    Return()

    # Function_4_272 end

    def Function_5_DCD(): pass

    label("Function_5_DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_F3F")
    EventBegin(0x1)
    TurnDirection(0x8, 0x0, 400)
    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E77")

    ChrTalk(
        0x8,
        "我不是说了禁止入内吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们想被关进\x01",
            "哈肯门的地下牢吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F12")

    label("loc_E77")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        "喂，那边禁止入内。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果不遵从命令的话\x01",
            "可是会遭到逮捕的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F12")


    def lambda_F18():
        OP_8C(0x8, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F18)
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0x8, 255)

    label("loc_F3F")

    Return()

    # Function_5_DCD end

    def Function_6_F40(): pass

    label("Function_6_F40")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拉文努矿山\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_F40 end

    SaveToFile()

Try(main)
