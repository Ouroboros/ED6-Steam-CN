from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1511   ._SN',
        MapName             = 'Bose',
        Location            = 'T1511.x',
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
        '雷纳德',                               # 9
        '索菲娜',                               # 10
        '罗伊德',                               # 11
        '艾露凯',                               # 12
        '阿妮特',                               # 13
        '奥利维尔',                             # 14
        '奥利维尔',                             # 15
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
        Unknown_30              = 225,
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01690 ._CH',             # 01
        'ED6_DT07/CH01023 ._CH',             # 02
        'ED6_DT07/CH01180 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT06/CH20050 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01690P._CP',             # 01
        'ED6_DT07/CH01023P._CP',             # 02
        'ED6_DT07/CH01180P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT06/CH20050P._CP',             # 05
    )

    DeclNpc(
        X                   = 24400,
        Z                   = 0,
        Y                   = 9200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 14000,
        Z                   = 0,
        Y                   = 3600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 49500,
        Z                   = 200,
        Y                   = 26230,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 54500,
        Z                   = 0,
        Y                   = 3400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 49900,
        Z                   = 0,
        Y                   = 5800,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 109100,
        Z                   = 600,
        Y                   = 5100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x156,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 110010,
        Z                   = -500,
        Y                   = 5150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x156,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 80610,
        TriggerZ            = 0,
        TriggerY            = 9100,
        TriggerRange        = 1400,
        ActorX              = 80610,
        ActorZ              = 1500,
        ActorY              = 9100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_1ED",          # 01, 1
        "Function_2_1EE",          # 02, 2
        "Function_3_204",          # 03, 3
        "Function_4_228",          # 04, 4
        "Function_5_2B1",          # 05, 5
        "Function_6_341",          # 06, 6
        "Function_7_3D9",          # 07, 7
        "Function_8_48E",          # 08, 8
        "Function_9_677",          # 09, 9
        "Function_10_6B4",         # 0A, 10
        "Function_11_EA1",         # 0B, 11
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1EC")
    OP_A3(0x3FA)
    Event(0, 10)

    label("loc_1EC")

    Return()

    # Function_0_1DE end

    def Function_1_1ED(): pass

    label("Function_1_1ED")

    Return()

    # Function_1_1ED end

    def Function_2_1EE(): pass

    label("Function_2_1EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_203")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1EE")

    label("loc_203")

    Return()

    # Function_2_1EE end

    def Function_3_204(): pass

    label("Function_3_204")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_227")
    OP_8D(0xFE, 50200, 5000, 54800, 6300, 2000)
    Jump("Function_3_204")

    label("loc_227")

    Return()

    # Function_3_204 end

    def Function_4_228(): pass

    label("Function_4_228")

    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        "要出去吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "晚上外出钓鱼的话，\x01",
            "不带上导力灯可是看不清周围的哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_4_228 end

    def Function_5_2B1(): pass

    label("Function_5_2B1")

    TalkBegin(0x9)

    ChrTalk(
        0xFE,
        (
            "你们的同伴看起来醉得很厉害，\x01",
            "不要紧吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不介意的话，\x01",
            "我给他送点水吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_5_2B1 end

    def Function_6_341(): pass

    label("Function_6_341")

    TalkBegin(0xB)

    ChrTalk(
        0xFE,
        "啊呀，晚上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也很想认识一下\x01",
            "同在这里住宿的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果您不介意的话，\x01",
            "请多来找我聊聊天吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_6_341 end

    def Function_7_3D9(): pass

    label("Function_7_3D9")

    TalkBegin(0xC)

    ChrTalk(
        0xFE,
        (
            "母亲好像\x01",
            "很喜欢这里的氛围呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说最初\x01",
            "推荐她来这里的是我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在则是母亲主动要求\x01",
            "要到这里来呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_7_3D9 end

    def Function_8_48E(): pass

    label("Function_8_48E")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A")
    OP_A2(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德正在研究展开在桌面上的地图。\x01",
            "好像是瓦雷利亚湖的地图。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        (
            "西侧的方向\x01",
            "结构比较简单，\x01",
            "在那边不会钓到什么鱼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "东侧的港湾处鱼的数量会多点，\x01",
            "不过都是一些小型的鱼类。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这两处的话，\x01",
            "那个家伙可能不会出来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然还是要\x01",
            "坚持陆钓啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_673")

    label("loc_63A")


    ChrTalk(
        0xFE,
        (
            "这次我一定要\x01",
            "把那个努西给钓上来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_673")

    TalkEnd(0xA)
    Return()

    # Function_8_48E end

    def Function_9_677(): pass

    label("Function_9_677")

    TalkBegin(0xD)

    ChrTalk(
        0xFE,
        (
            "嗯嗯……雪拉君……\x01",
            "再这样下去我就……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_9_677 end

    def Function_10_6B4(): pass

    label("Function_10_6B4")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    AddParty(0x2, 0xFF)
    SetChrPos(0x101, 107680, 0, 5310, 90)
    SetChrPos(0x103, 109180, 0, 6400, 180)
    SetChrPos(0x102, 107620, 0, 6630, 135)
    OP_6D(107890, 0, 13120, 0)
    OP_A2(0x34E)
    OP_28(0x38, 0x1, 0x80)
    FadeToBright(2000, 0)
    OP_6D(109120, 0, 5740, 3000)

    ChrTalk(
        0xE,
        (
            "#038F啊……唔……\x02\x03",
            "唔……咕噜咕噜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6P啊～哈，醉得不成样子了。\x02\x03",
            "我就知道这个奥利维尔\x01",
            "是喝不过我们的雪拉姐的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x103,
        (
            "#021F#5P呵呵，也不能这么说。\x02\x03",
            "最近一直忙于工作，\x01",
            "今天我的酒瘾一下子爆发出来了㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 200)

    ChrTalk(
        0x102,
        (
            "#017F喝了这么多还面不改色……\x02\x03",
            "#018F雪拉姐姐，\x01",
            "难道你受过什么特殊的训练吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(
        0x103,
        (
            "#020F#5P唔……可能是因为\x01",
            "我从来都不会挑酒喝吧。\x02\x03",
            "加了蝎子的、毒蛇的，什么酒都喝过。\x02\x03",
            "#021F越古怪的酒喝起来才越有滋味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F不……\x01",
            "我觉得好像不是这样……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#009F#6P对了，这家伙该怎么处理？\x01",
            "他暂时应该醒不过来了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#026F#5P就让他好好睡下去吧。\x02\x03",
            "#022F……毕竟我们今晚\x01",
            "很有可能和那些空贼正面交锋。\x02\x03",
            "还是不要让这种普通市民\x01",
            "卷入这件事比较好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#6P咦，难道雪拉姐你……\x02\x03",
            "为了不让他跟着我们，\x01",
            "所以才会特意把他灌醉的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023F#5P哎……\x02\x03",
            "…………………………\x02\x03",
            "#021F啊、那、那是当然的啦。\x01",
            "这就是我深谋远虑的良苦用心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#6P在这之前的『哎』是什么啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F之前明明那么享受。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F#5P不说了，现在已经夜深了。\x02\x03",
            "我们还是早点\x01",
            "做好监视的准备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#507F#6P啊，岔开话题了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F#5P好啦，多说无用。\x02\x03",
            "我们先到栈桥那里看看吧。\x01",
            "说不定那些空贼很快会来到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#6P那好，我们出发吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 107480, 0, 9560, 0)
    SetChrPos(0x103, 107480, 0, 9560, 0)
    SetChrPos(0x102, 107480, 0, 9560, 0)
    OP_6D(107480, 0, 9560, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    ClearMapFlags(0x10000000)
    Return()

    # Function_10_6B4 end

    def Function_11_EA1(): pass

    label("Function_11_EA1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "钓鱼工具并排摆在架子上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_11_EA1 end

    SaveToFile()

Try(main)
