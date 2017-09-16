from ED6ScenarioHelper import *

def main():
    # 布莱特家

    CreateScenaFile(
        FileName            = 'T0301   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0301.x',
        MapIndex            = 15,
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
        '约修亚',                               # 9
        '卡西乌斯',                             # 10
        '器皿',                                 # 11
    )

    DeclEntryPoint(
        Unknown_00              = 2000,
        Unknown_04              = 0,
        Unknown_08              = -6000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00010 ._CH',             # 00
        'ED6_DT07/CH02000 ._CH',             # 01
        'ED6_DT06/CH20030 ._CH',             # 02
        'ED6_DT06/CH20011 ._CH',             # 03
        'ED6_DT06/CH20021 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH00010P._CP',             # 00
        'ED6_DT07/CH02000P._CP',             # 01
        'ED6_DT06/CH20030P._CP',             # 02
        'ED6_DT06/CH20011P._CP',             # 03
        'ED6_DT06/CH20021P._CP',             # 04
    )

    DeclNpc(
        X                   = 11500,
        Z                   = 0,
        Y                   = -3400,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 450,
        Y                   = -1200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262148,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1FE",          # 00, 0
        "Function_1_32E",          # 01, 1
        "Function_2_352",          # 02, 2
        "Function_3_46A",          # 03, 3
        "Function_4_DC4",          # 04, 4
        "Function_5_E0D",          # 05, 5
        "Function_6_E26",          # 06, 6
        "Function_7_E27",          # 07, 7
        "Function_8_1952",         # 08, 8
        "Function_9_1995",         # 09, 9
    )


    def Function_0_1FE(): pass

    label("Function_0_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_208")
    Jump("loc_20F")

    label("loc_208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_20F")

    label("loc_20F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_223"),
        (2, "loc_28E"),
        (3, "loc_326"),
        (SWITCH_DEFAULT, "loc_32D"),
    )


    label("loc_223")

    ClearMapFlags(0x1)
    SetChrChipByIndex(0x8, 2)
    SetChrPos(0x8, -6220, 3450, 4390, 180)
    SetChrFlags(0x8, 0x4)

    def lambda_249():

        label("loc_249")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_249")

    QueueWorkItem2(0x8, 1, lambda_249)
    ClearChrFlags(0x8, 0x80)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(7170, 3450, -16520, 0)
    OP_6C(308000, 0)
    FadeToBright(2000, 0)
    Event(0, 3)
    Jump("loc_32D")

    label("loc_28E")

    ClearMapFlags(0x1)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x9, 0x8)
    SetChrPos(0x102, 6021, 450, 3014, 90)
    SetChrPos(0x9, 9600, 500, -2310, 90)
    SetChrChipByIndex(0x9, 10)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0xA, 10000, 1100, -3300, 0)
    ClearChrFlags(0xA, 0x80)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-2924, 0, -6598, 0)
    OP_6C(48000, 0)
    FadeToBright(500, 0)
    Event(0, 7)
    Jump("loc_32D")

    label("loc_326")

    Event(0, 2)
    Jump("loc_32D")

    label("loc_32D")

    Return()

    # Function_0_1FE end

    def Function_1_32E(): pass

    label("Function_1_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_338")
    Jump("loc_33F")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_33F")

    label("loc_33F")

    OP_16(0x2, 0xFA0, 0xFFFE17B8, 0xFFFDF878, 0x30003)
    Return()

    # Function_1_32E end

    def Function_2_352(): pass

    label("Function_2_352")

    EventBegin(0x0)
    OP_22(0x1CF, 0x0, 0x64)
    OP_A2(0x390)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_6D(800, -1000, -24180, 0)
    OP_67(0, 5600, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(350000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_3B7():
        OP_6D(4000, 0, -1000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B7)

    def lambda_3CF():
        OP_67(0, 8000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3CF)

    def lambda_3E7():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E7)
    Sleep(8000)

    def lambda_3FC():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FC)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_24(0x1CF, 0x5F)
    Sleep(100)
    OP_24(0x1CF, 0x5A)
    Sleep(100)
    OP_24(0x1CF, 0x55)
    Sleep(100)
    OP_24(0x1CF, 0x50)
    Sleep(100)
    OP_24(0x1CF, 0x4B)
    Sleep(100)
    OP_24(0x1CF, 0x46)
    Sleep(100)
    OP_24(0x1CF, 0x3C)
    Sleep(100)
    OP_23(0x1CF)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T0311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_352 end

    def Function_3_46A(): pass

    label("Function_3_46A")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_1F(0x64, 0x12C)
    SetChrPos(0x101, -1860, 3450, 930, 270)
    SetChrFlags(0x101, 0x40)
    OP_43(0x101, 0x0, 0x0, 0x4)
    OP_43(0x8, 0x0, 0x0, 0x5)
    OP_43(0x9, 0x0, 0x0, 0x6)
    OP_6D(-5250, 3450, 3230, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4380, 0)
    OP_6C(226000, 0)
    OP_6E(262, 0)

    def lambda_4E5():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4E5)

    def lambda_4F5():
        OP_67(0, 5000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4F5)
    OP_6B(2940, 10000)

    def lambda_516():
        OP_67(0, 8000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_516)
    OP_6B(2800, 5000)
    Sleep(4000)
    OP_70(0x2, 0x3C)
    Sleep(500)
    OP_A2(0x0)
    OP_A5(0x0)
    OP_21()
    OP_44(0x8, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#001F咻——咻——！\x02\x03",
            "不错嘛，约修亚。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_1D(0xF)
    Fade(250)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    Sleep(400)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#010F早上好，艾丝蒂尔。\x02\x03",
            "是不是把你吵醒了？\x01",
            "那我要向你说抱歉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没有啊，\x01",
            "我已经睡饱了，自然要起床嘛。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_612():
        OP_6D(-6350, 3450, 3460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_612)
    OP_8E(0x101, 0xFFFFE7B4, 0xD7A, 0xB2C, 0x7D0, 0x0)
    TurnDirection(0x101, 0x8, 400)
    Sleep(100)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#001F不过，约修亚也真是的。\x01",
            "一大早就这么认真地吹口琴～\x02\x03",
            "呵呵～姐姐我啊，\x01",
            "都听得入神了呢㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#017F什么姐姐啊……\x01",
            "明明和我一样大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F啧啧啧，你太天真了。\x02\x03",
            "虽然我和你同龄，\x01",
            "不过在这个家里我可算是前辈哦。\x02\x03",
            "也可以说是你的师姐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#010F是是，我完全明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F呀～你这态度也太敷衍了吧……\x02\x03",
            "#001F话说回来，这首曲子真的很好听呢。\x02\x03",
            "#001F旋律明快，却又有点悲伤的意境……\x02\x03",
            "#001F虽然其它的曲子也都不错，\x01",
            "不过我最喜欢的还要数这首了。\x02\x03",
            "#000F对了……曲名叫什么来着？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#010F『星之所在』。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊对对，叫『星之所在』。\x02\x03",
            "#007F啊～要是我也能\x01",
            "把口琴吹得这么棒就好了。\x02\x03",
            "看起来挺简单的，\x01",
            "不过真的做起来却很难啊～\x02\x03",
            "比如手的动作啊，控制气息啊，\x01",
            "我根本配合不起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#019F比起你擅长的棒术，\x01",
            "我倒觉得这个简单多了……\x02\x03",
            "#019F关键还是集中力的问题哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F那也是，要是让我一动不动地做事情，\x01",
            "肯定一会儿就睡着了～\x02\x03",
            "#009F这就是所谓的『春眠不觉晓』吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#018F不，我想你搞错意思了……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x9, -6050, 0, -2610, 0)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(
        0x9,
        "男人的声音",
        (
            "喂～\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x1)
    OP_6D(-6400, 3450, -400, 2000)

    ChrTalk(
        0x101,
        "#001F啊～老爸，早啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#019F早上好，爸爸。\x01",
            "早饭已经准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#080F啊啊，大功告成了。\x02\x03",
            "#080F你们俩，趁饭菜还没凉，\x01",
            "赶快下来吃吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F明白～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#010F马上就去。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    NewScene("ED6_DT01/T0310   ._SN", 2, 0, 0)
    IdleLoop()
    Return()

    # Function_3_46A end

    def Function_4_DC4(): pass

    label("Function_4_DC4")

    OP_A6(0x0)
    SetChrPos(0x101, -1860, 3450, 930, 270)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFF3D0, 0xD7A, 0x3DE, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x40)
    OP_A3(0x0)
    OP_A6(0x0)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_A3(0x0)
    Return()

    # Function_4_DC4 end

    def Function_5_E0D(): pass

    label("Function_5_E0D")

    OP_A6(0x1)
    Sleep(400)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_A3(0x1)
    Return()

    # Function_5_E0D end

    def Function_6_E26(): pass

    label("Function_6_E26")

    Return()

    # Function_6_E26 end

    def Function_7_E27(): pass

    label("Function_7_E27")

    EventBegin(0x0)
    OP_6B(3000, 0)
    OP_43(0x102, 0x0, 0x0, 0x8)
    OP_43(0x9, 0x0, 0x0, 0x9)
    OP_22(0x1CF, 0x0, 0x64)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 0, 0, 0, 0)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x9, 9600, 620, -2310, 90)
    OP_A2(0x2)
    OP_6D(7500, 450, 1022, 8000)
    OP_A5(0x2)
    OP_67(0, 6710, -10000, 4000)
    OP_0D()
    OP_70(0x1, 0x3C)
    OP_73(0x1)
    OP_A2(0x1)
    Sleep(1000)
    OP_72(0x1, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x1, 0x0)
    OP_A5(0x1)
    OP_71(0x1, 0x800)

    ChrTalk(
        0x102,
        "#015F……爸爸。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 1)
    Sleep(300)

    ChrTalk(
        0x9,
        "#080F是约修亚啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_6D(10020, 450, -790, 2000)
    OP_A5(0x1)

    ChrTalk(
        0x102,
        (
            "#010F喝这么多酒，\x01",
            "又会被艾丝蒂尔骂的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#080F出发前提提神嘛。\x01",
            "要不，你也来一杯吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F还是免了。\x01",
            "还有，请不要劝未成年人喝酒。\x02\x03",
            "#018F况且我又不是雪拉姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#081F哈哈……\x01",
            "那个大酒鬼，比我能喝多了。\x02\x03",
            "#080F…………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F…………………………\x02\x03",
            "#012F……看来任务很棘手吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#085F现在还没有确实的证据……\x01",
            "不过帝国那边似乎已经有动静了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F埃雷波尼亚帝国……\x02\x03",
            "#012F就是说很可疑吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#082F虽然还没有明显的行动……\x01",
            "不过这却反而让人更加怀疑。\x02\x03",
            "所以我打算先\x01",
            "到帝国大使馆那里打听一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我知道了。\x01",
            "艾丝蒂尔就交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#080F可别太娇惯她哦。\x02\x03",
            "她已经是游击士了，\x01",
            "不好好学会照顾自己怎么行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔能行的。\x02\x03",
            "#010F她有天生的直觉。虽然平常有点粗枝大叶，\x01",
            "但在武术方面也算是个天才。\x02\x03",
            "#019F所以一定能成为一流的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#085F现在还是不谙世事的小孩子呢。\x02\x03",
            "#085F总有一天她也要\x01",
            "依自身的意志来选择前进的道路。\x02\x03",
            "#082F……约修亚。\x01",
            "这话也同样是对你说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#080F已经过了五年了啊……\x02\x03",
            "时间真是转瞬即逝啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F嗯……\x02\x03",
            "#010F真的是转瞬即逝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#082F那时候的话……\x01",
            "你还不打算收回吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F…………………………\x02\x03",
            "#013F对我来说，那已经是最后的底线了。\x02\x03",
            "#013F如果连那都不能守护，\x01",
            "我……绝对不会原谅自己的。\x02\x03",
            "#015F所以我……再一次说抱歉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#085F……你没必要道歉啊。\x02\x03",
            "#080F但是，你要记住一件事。\x02\x03",
            "#080F不管你选择什么样的道路，\x01",
            "都无法抹消这五年的时光。\x02\x03",
            "#080F我和艾丝蒂尔，都是你的家人。\x02\x03",
            "#080F无论发生什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F……嗯……\x02\x03",
            "#015F…………………………\x02\x03",
            "#010F#50W谢谢您……爸爸……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_20(0x9C4)
    FadeToDark(2000, 0, -1)
    OP_24(0x1CF, 0x5F)
    Sleep(100)
    OP_24(0x1CF, 0x5A)
    Sleep(100)
    OP_24(0x1CF, 0x55)
    Sleep(100)
    OP_24(0x1CF, 0x50)
    Sleep(100)
    OP_24(0x1CF, 0x4B)
    Sleep(100)
    OP_24(0x1CF, 0x46)
    Sleep(100)
    OP_24(0x1CF, 0x3C)
    Sleep(100)
    OP_23(0x1CF)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_AD(0x4003C, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT01/T0700   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_7_E27 end

    def Function_8_1952(): pass

    label("Function_8_1952")

    OP_A6(0x1)
    OP_8E(0xFE, 0x212C, 0x1C2, 0xAB5, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_8E(0xFE, 0x2710, 0x1C2, 0xFFFFFF56, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x1)
    Return()

    # Function_8_1952 end

    def Function_9_1995(): pass

    label("Function_9_1995")

    OP_A6(0x2)
    OP_6C(315000, 8000)
    OP_A3(0x2)
    OP_A6(0x2)
    OP_A3(0x2)
    Return()

    # Function_9_1995 end

    SaveToFile()

Try(main)
