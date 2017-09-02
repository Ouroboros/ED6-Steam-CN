from ED6ScenarioHelper import *

def main():
    # 洛连特市长官邸

    CreateScenaFile(
        FileName            = 'T0200   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0200.x',
        MapIndex            = 12,
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
        '乔丝特',                               # 9
        '洛连特市街道',                         # 10
    )

    DeclEntryPoint(
        Unknown_00              = -6100,
        Unknown_04              = 0,
        Unknown_08              = 50,
        Unknown_0C              = 4,
        Unknown_0E              = 90,
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
        Unknown_3A              = 12,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -6100,
        Unknown_04              = 0,
        Unknown_08              = 50,
        Unknown_0C              = 4,
        Unknown_0E              = 90,
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
        Unknown_3A              = 12,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02330 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02330P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -20690,
        Z                   = 0,
        Y                   = -180,
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


    DeclActor(
        TriggerX            = 13870,
        TriggerZ            = 3700,
        TriggerY            = -4460,
        TriggerRange        = 500,
        ActorX              = 13870,
        ActorZ              = 4200,
        ActorY              = -4460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8189,
        TriggerZ            = 450,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = 8189,
        ActorZ              = 1450,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_17E",          # 00, 0
        "Function_1_1B5",          # 01, 1
        "Function_2_216",          # 02, 2
        "Function_3_379",          # 03, 3
        "Function_4_98B",          # 04, 4
    )


    def Function_0_17E(): pass

    label("Function_0_17E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_191")
    OP_64(0x0, 0x1)
    Jump("loc_191")

    label("loc_191")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1A1"),
        (103, "loc_1A8"),
        (SWITCH_DEFAULT, "loc_1B4"),
    )


    label("loc_1A1")

    Event(0, 3)
    Jump("loc_1B4")

    label("loc_1A8")

    OP_6C(225000, 0)
    Jump("loc_1B4")

    label("loc_1B4")

    Return()

    # Function_0_17E end

    def Function_1_1B5(): pass

    label("Function_1_1B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CD")
    OP_B1("t0200_y")
    Jump("loc_1D6")

    label("loc_1CD")

    OP_B1("t0200_n")

    label("loc_1D6")

    OP_16(0x2, 0xFA0, 0xFFFE36F8, 0xFFFE0C00, 0x30002)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FC")
    OP_72(0x0, 0x10)
    Jump("loc_200")

    label("loc_1FC")

    OP_64(0x1, 0x1)

    label("loc_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_215")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_215")

    Return()

    # Function_1_1B5 end

    def Function_2_216(): pass

    label("Function_2_216")

    EventBegin(0x0)
    OP_6D(13870, 3700, -4460, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA")

    ChrTalk(
        0x101,
        "#004F啊，这里的栏杆有划痕。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F真的啊……\x01",
            "而且还是刚划上去的。\x02\x03",
            "#012F看起来是用金属之类的东西挂过的痕迹。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x260)
    OP_28(0x1A, 0x1, 0x80)
    Jump("loc_376")

    label("loc_2DA")


    ChrTalk(
        0x101,
        (
            "#002F栏杆有划痕……\x01",
            "看起来是用金属之类的东西弄成的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯，\x01",
            "先把这些线索详细记录在手册上再说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376")

    EventEnd(0x1)
    Return()

    # Function_2_216 end

    def Function_3_379(): pass

    label("Function_3_379")

    EventBegin(0x0)
    OP_A2(0x24F)
    OP_28(0x3, 0x4, 0x10)
    OP_28(0x3, 0x1, 0x200)
    OP_28(0x3, 0x1, 0x400)
    OP_28(0x4, 0x4, 0x40)
    OP_28(0x6, 0x4, 0x40)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    ClearChrFlags(0x8, 0x80)
    OP_6D(2040, 0, 650, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 1770, 0, 690, 270)
    SetChrPos(0x102, 1640, 0, -790, 270)
    SetChrPos(0x8, -450, 0, -60, 90)
    OP_6D(750, 0, -40, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#000F原来你明天\x01",
            "就要坐定期船回去了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#217F嗯，是的。\x01",
            "因为学院快要开学了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P原来如此，\x01",
            "是趁着学校放假的机会出来调查的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F啊～～真遗憾。\x01",
            "好不容易认识了一个朋友……\x02\x03",
            "#000F以后还有机会见面吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#217F嗯……\x01",
            "我也希望能再见到你们。\x02\x03",
            "#218F那么后会有期哦。\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    OP_8E(0x8, 0xFFFFDC4C, 0x0, 0x118, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        (
            "#001F啊～真是个好女孩呢。\x02\x03",
            "#001F虽然看起来像个大小姐，\x01",
            "不过却完全没有架子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F#2P………嗯…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F约修亚？\x02\x03",
            "#006F哎呀，难道说～……\x02\x03",
            "#006F你喜欢的类型是那样的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#2P啊……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#012F#2P你、你在乱说些什么呀！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F脸红了、脸红了⊙\x02\x03",
            "#001F呀～姐姐我真是吃了一惊呢。\x02\x03",
            "#001F原来约修亚喜欢的是\x01",
            "大小姐类型的呢。\x02\x03",
            "#001F下次见面之前，\x01",
            "记得一定要准备好能打动人家芳心的告白哦㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#018F#2P哼，你不要再自编自演了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(
        0x102,
        "#013F#2P真是的，完全不了解别人的心情……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F#2P……没什么。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#2P好了，我们快点去协会报告吧。\x02\x03",
            "父亲交待的工作还有一件就完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊，对呀……\x02\x03",
            "#001F嗯，鼓足干劲去做吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    Return()

    # Function_3_379 end

    def Function_4_98B(): pass

    label("Function_4_98B")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

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

    # Function_4_98B end

    SaveToFile()

Try(main)
