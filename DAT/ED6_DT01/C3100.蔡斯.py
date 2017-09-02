from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3100   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        '希德少校',                             # 9
        '卫兵',                                 # 10
        '卫兵',                                 # 11
        '士兵塞缪尔',                           # 12
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
        'ED6_DT07/CH02450 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH02450P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3340,
        Z                   = 0,
        Y                   = -4720,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclEvent(
        X                   = -6310,
        Y                   = -1000,
        Z                   = -4980,
        Range               = 6020,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFDAC6,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 5480,
        Y                   = -1000,
        Z                   = -41450,
        Range               = -5800,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFF61C2,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -5300,
        Y                   = -1000,
        Z                   = -7680,
        Range               = 5340,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE94E,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = 6000,
        TriggerZ            = 0,
        TriggerY            = -45540,
        TriggerRange        = 1500,
        ActorX              = 6000,
        ActorZ              = 1500,
        ActorY              = -45540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BE",          # 00, 0
        "Function_1_22B",          # 01, 1
        "Function_2_26D",          # 02, 2
        "Function_3_283",          # 03, 3
        "Function_4_830",          # 04, 4
        "Function_5_C22",          # 05, 5
        "Function_6_2940",         # 06, 6
        "Function_7_2B80",         # 07, 7
        "Function_8_2C1B",         # 08, 8
    )


    def Function_0_1BE(): pass

    label("Function_0_1BE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1CA"),
        (SWITCH_DEFAULT, "loc_1E0"),
    )


    label("loc_1CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DD")
    OP_A2(0x55B)
    Event(0, 4)

    label("loc_1DD")

    Jump("loc_1E0")

    label("loc_1E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1EA")
    Jump("loc_22A")

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_205")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    OP_8C(0xB, 90, 0)
    Jump("loc_22A")

    label("loc_205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_20F")
    Jump("loc_22A")

    label("loc_20F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_21E")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_22A")

    label("loc_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_22A")
    ClearChrFlags(0xB, 0x80)

    label("loc_22A")

    Return()

    # Function_0_1BE end

    def Function_1_22B(): pass

    label("Function_1_22B")

    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_243")
    OP_6F(0x0, 310)

    label("loc_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_253")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_253")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    OP_28(0x2A, 0x1, 0x4000)

    label("loc_267")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_22B end

    def Function_2_26D(): pass

    label("Function_2_26D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_282")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_26D")

    label("loc_282")

    Return()

    # Function_2_26D end

    def Function_3_283(): pass

    label("Function_3_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_51E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_343")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了希德少校的名誉，\x01",
            "还是拒绝了好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "少校是个好人，也很聪明。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只不过……\x01",
            "他心太软了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_51B")

    label("loc_343")

    TalkBegin(0xFE)
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "说起来，希德少校也很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "让情报部的那些家伙们\x01",
            "随便使唤来使唤去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为人老实虽然好，\x01",
            "可是也要看对象是谁啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 400)
    Sleep(400)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0xFE,
        (
            "哇、哇～！\x01",
            "什么时候来的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "平、平民\x01",
            "禁止进入这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "赶快回去！\x01",
            "要不然就把你们抓起来！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 180, 0)
    OP_4B(0xFE, 255)
    ClearMapFlags(0x80)

    label("loc_51B")

    Jump("loc_82F")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_747")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_597")

    ChrTalk(
        0xFE,
        (
            "……嗯？\x01",
            "你、你们还在这里吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不赶快离开的话，\x01",
            "这次真的要把你们抓起来哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6B0")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "怎么了，\x01",
            "你们就这么想被逮捕吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我不是在威胁你们。\x01",
            "因为现在有情报部的部队\x01",
            "驻扎在这里……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0xFE,
        "啊…………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "咳咳……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总、总之，\x01",
            "你们赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741")

    label("loc_6B0")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "这里是王国军的据点\x01",
            "雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "普通老百姓\x01",
            "是不能进去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请你们赶快回去吧。\x02",
    )

    CloseMessageWindow()

    label("loc_741")

    TalkEnd(0xFE)
    Jump("loc_82F")

    label("loc_747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_82F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_79B")

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "赖在这里也没有用哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_82C")

    label("loc_79B")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "这里是王国军的据点\x01",
            "雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "普通老百姓\x01",
            "是不能进去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请你们赶快回去吧。\x02",
    )

    CloseMessageWindow()

    label("loc_82C")

    TalkEnd(0xFE)

    label("loc_82F")

    Return()

    # Function_3_283 end

    def Function_4_830(): pass

    label("Function_4_830")

    EventBegin(0x0)
    SetChrPos(0x101, -50, 0, -57100, 0)
    SetChrPos(0x102, -1380, 0, -57730, 0)
    OP_6D(-240, -50, -54460, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    StopSound(0x9470, 0x493E0, 0x1F40)

    def lambda_8A4():
        OP_6D(1220, 250, -12050, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A4)

    def lambda_8BC():
        OP_67(0, 5140, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8BC)

    def lambda_8D4():
        OP_6B(8860, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8D4)

    def lambda_8E4():
        OP_6C(77000, 9000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8E4)
    Sleep(9000)
    Fade(1000)
    StopSound(0x9470, 0x1FBD0, 0x0)
    OP_6D(-240, -50, -54460, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#004F唔哇～……\x01",
            "这么大的军事基地啊。\x02\x03",
            "约修亚，你看！\x01",
            "有那个哈肯大门两倍大吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是啊……\x01",
            "说不定是有好几倍哦。\x02\x03",
            "这里在十年前的战争中不但没有陷落，\x01",
            "反而成为了王国反攻作战的根据地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F原来是这样啊……\x01",
            "不过，现在可不是赞赏的时候吧。\x02\x03",
            "总之赶快去门口，\x01",
            "把这里的负责人叫出来吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F#2P咦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没什么……\x01",
            "只是觉得你越来越勇往直前了。\x02\x03",
            "不愧是父亲的女儿啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2P不怕跟你说，\x01",
            "其实我也有点紧张的呢。\x02\x03",
            "只不过我想这里应该不会有\x01",
            "比那个摩尔根将军更加可怕的人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，大概是吧。\x02\x03",
            "#013F摩尔根将军……\x01",
            "现在还留守在哈肯大门吗？\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_4_830 end

    def Function_5_C22(): pass

    label("Function_5_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_293F")
    OP_A2(0x55C)
    OP_28(0x43, 0x1, 0x2)
    OP_28(0x43, 0x1, 0x4)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -730, 250, -10440, 0)
    SetChrPos(0x102, 580, 250, -10420, 0)
    OP_6D(420, 1480, -5420, 0)
    OP_67(0, 6320, -20350, 0)
    OP_6B(1000, 0)
    OP_6E(611, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F咦，没人呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F奇怪……\x02\x03",
            "按照军队的规定，\x01",
            "这里应该会有门卫站岗的……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男性的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……你们是来做什么的？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F哎，咦……\x01",
            "哪里传出来的声音？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F大概是那边的扩音器。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("男性的声音")

    AnonymousTalk(
        (
            "这里是雷斯顿要塞，\x01",
            "利贝尔王国军的总司令部。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "雷斯顿要塞是军事禁区，\x01",
            "不是你们平民能靠近的地方。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "抱歉，麻烦你们马上离开吧。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x101,
        "#505F（真、真叫人觉得不爽啊。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F（嗯……\x01",
            "　看来这里的戒备相当严密啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("男性的声音")

    AnonymousTalk(
        (
            "喂喂！\x01",
            "你们听到了没有？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x101,
        (
            "#006F不好意思，\x01",
            "我们两个不是普通的平民。\x02\x03",
            "我们是游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F关于中央工房的袭击事件，\x01",
            "我们有些问题想当面请教一下。\x02\x03",
            "能让我们见见你们的负责人吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("男性的声音")

    AnonymousTalk(
        (
            "游击士协会……\x01",
            "你们两个是游击士？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x101,
        (
            "#006F要是不信的话，\x01",
            "麻烦你看一下这个胸章。\x02\x03",
            "这个这个，看到了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("男性的声音")

    AnonymousTalk(
        "…………………………………\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "……确认完毕，\x01",
            "看来你们的确是游击士。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "不过很不凑巧，\x01",
            "这个要塞的负责人刚好外出。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "可以的话麻烦改日再来。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x101,
        (
            "#505F负责人不在……\x01",
            "总觉得这是敷衍别人的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么能让我们见见情报部的人吗？\x01",
            "任何一位都可以。\x02\x03",
            "我们有些事情要向\x01",
            "理查德上校和凯诺娜上尉传达。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("男性的声音")

    AnonymousTalk(
        "…………………………………\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "那好，你们先等一下吧。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#007F呼……\x01",
            "终于把头儿给叫出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯……但这里的戒备\x01",
            "真是比想象中还要森严啊。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 40, 0, 3860, 180)
    SetChrPos(0x9, -760, 160, 4180, 180)
    SetChrPos(0xA, 900, 160, 4180, 180)
    OP_4A(0x9, 0)
    OP_4A(0xA, 0)
    OP_72(0x0, 0x10)
    OP_70(0x0, 0x1C2)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F哇哇……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F好像有人来了……\x02",
    )

    CloseMessageWindow()

    def lambda_1358():
        OP_67(0, 12570, -20350, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1358)
    OP_6C(0, 8000)
    OP_73(0x0)

    def lambda_137C():
        OP_8E(0xFE, 0xFFFFFF92, 0xD2, 0xFFFFE37C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_137C)
    Sleep(500)

    def lambda_139C():
        OP_8E(0xFE, 0xFFFFFC54, 0xAA, 0xFFFFE728, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_139C)

    def lambda_13B7():
        OP_8E(0xFE, 0x316, 0xAA, 0xFFFFE714, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13B7)

    def lambda_13D2():
        OP_6D(-150, 190, -6720, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13D2)

    def lambda_13EA():
        OP_6B(850, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13EA)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#700F#5P非常抱歉，让你们久等了。\x02\x03",
            "我是雷斯顿要塞的守备队长\x01",
            "希德少校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F我是游击士协会的\x01",
            "艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F同属游击士协会的约修亚·布莱特。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#702F#5P……布莱特……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F#5P不，没……\x01",
            "抱歉，没什么。\x02\x03",
            "#701F言归正传……\x01",
            "你们来的目的是要传达有关\x01",
            "中央工房袭击事件的事情对吧。\x02\x03",
            "真是非常抱歉……\x01",
            "情报部的所有人刚刚外出。\x02\x03",
            "有什么事的话，我可以代为传达。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唔，这就麻烦了。\x02\x03",
            "#006F（好，\x01",
            "　这就试探一下他们……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "「抓到了那些袭击中央工房的犯人」\x01",            # 0
            "「查到了被绑架的拉赛尔博士的行踪」\x01",          # 1
            "「找到了犯人掳走博士时乘的飞艇的线索」\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_173A"),
        (1, "loc_18A6"),
        (2, "loc_1A0E"),
        (SWITCH_DEFAULT, "loc_1AD1"),
    )


    label("loc_173A")


    ChrTalk(
        0x101,
        (
            "#007F唉唉，我们好不容易\x01",
            "抓到了那些袭击中央工房的犯人。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#702F#5P说、说什么！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F艾丝蒂尔，这太性急了。\x02\x03",
            "我们只不过找到了一些\x01",
            "犯人掳走博士时乘的飞艇的线索而已。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#001F啊，抱歉抱歉。\x01",
            "刚才不小心说错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#700F#5P……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#006F咦，少校。\x01",
            "为什么突然沉默了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD1")

    label("loc_18A6")


    ChrTalk(
        0x101,
        (
            "#007F唉唉，我们好不容易\x01",
            "查到了被绑架的拉赛尔博士的行踪。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#702F#5P说、说什么！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F艾丝蒂尔，这太性急了。\x02\x03",
            "我们只不过找到了一些\x01",
            "犯人掳走博士时乘的飞艇的线索而已。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#001F啊，抱歉抱歉。\x01",
            "刚才不小心说错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#700F#5P……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#006F咦，少校。\x01",
            "为什么突然沉默了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD1")

    label("loc_1A0E")


    ChrTalk(
        0x101,
        (
            "#007F唉唉，我们好不容易\x01",
            "找到了犯人掳走博士时乘的飞艇的线索。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#702F#5P说、说什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F咦，少校。\x01",
            "您怎么那么吃惊啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD1")

    label("loc_1AD1")


    ChrTalk(
        0x8,
        (
            "#701F#5P不、没什么……\x01",
            "因为接到联络后我们也在不断搜索。\x02\x03",
            "对了……\x01",
            "是什么线索呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F请少校看看这个。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xD2, 0xFA, 0xFFFFDF94, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "朵洛希拍的照片\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x358, 1)
    OP_8F(0x102, 0x1F4, 0xFA, 0xFFFFDD6E, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "#702F#5P这……\x01",
            "不就是雷斯顿要塞吗。\x02\x03",
            "这样的照片你们是怎样……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFFDA8, 0xF0, 0xFFFFE174, 0xBB8, 0x0)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#006F哎呀哎呀。\x01",
            "不要说得那么肯定嘛。\x02\x03",
            "请仔细看看照片的右上角。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#700F#5P右上角……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#704F#5P这、这个是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这艘飞艇的轮廓和\x01",
            "军队使用的警备飞艇明显不同吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#507F但是却和犯人绑架博士时乘的飞艇\x01",
            "一模一样哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#700F#5P……………………………\x02\x03",
            "#703F原来如此……\x01",
            "这的确是相当奇怪的事态。\x02\x03",
            "感谢你们的合作，\x01",
            "我会尽快将此事传达情报部的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎……\x02\x03",
            "等、等一下！\x01",
            "这样说几句就行了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "#702F#5P小姐你的意思是……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x101, 0xFFFFFD30, 0xFA, 0xFFFFDF12, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        (
            "#009F因、因为……\x01",
            "你不觉得这照片很不可思议吗？\x02\x03",
            "为什么犯人乘坐的飞艇\x01",
            "会在戒备森严的要塞上空出现？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F#5P虽然这样说十分惭愧，\x01",
            "但我们对此确实完全不知情。\x02\x03",
            "最近这段时间\x01",
            "我们一直忙于国境附近的搜索，\x01",
            "所以有时候疏忽了根据地周围的警戒。\x02\x03",
            "从飞艇飞向瓦雷利亚湖北面这点来看，\x01",
            "很有可能是帝国那边的飞艇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F是、是这样吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F…………………………\x02\x03",
            "#010F还有个问题想少校回答一下。\x02\x03",
            "请问情报部的人\x01",
            "现在都去了哪里执行任务呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "#700F#5P………………………………\x02\x03",
            "#703F这是军事机密。\x02\x03",
            "抱歉两位，我这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2146():

        label("loc_2146")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2146")

    QueueWorkItem2(0x9, 1, lambda_2146)

    def lambda_2157():

        label("loc_2157")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2157")

    QueueWorkItem2(0xA, 1, lambda_2157)
    OP_8C(0x8, 0, 400)

    def lambda_216F():
        OP_8E(0xFE, 0x28, 0x0, 0xF14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_216F)
    Sleep(1000)

    def lambda_218F():
        OP_8E(0xFE, 0xFFFFFD08, 0xA0, 0x1054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_218F)

    def lambda_21AA():
        OP_8E(0xFE, 0x384, 0xA0, 0x1054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_21AA)
    Sleep(2000)

    def lambda_21CA():
        OP_67(0, 18220, -20350, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21CA)

    def lambda_21E2():
        OP_6E(489, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_21E2)
    Sleep(4000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#009F我、我说约修亚……\x02\x03",
            "这么敷衍的回答，\x01",
            "不就是明摆着很奇怪嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#013F我知道……\x02\x03",
            "但是只要没有决定性的证据，\x01",
            "我们也就没办法继续追问下去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F唔唔～……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(-770, 1700, -3300, 0)
    OP_67(0, 5430, -10000, 0)
    OP_6B(4880, 0)
    OP_6C(339000, 0)
    OP_6E(262, 0)
    OP_72(0x0, 0x800)
    OP_22(0x6C, 0x0, 0x64)
    OP_6F(0x0, 450)
    OP_70(0x0, 0x136)
    OP_73(0x0)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)
    Sleep(500)
    OP_71(0x0, 0x800)

    ChrTalk(
        0x101,
        "#004F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F……怎么回事？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "希德少校",
        (
            "什、什么……\x01",
            "怎么会在中途停下的？\x02\x03",
            "…………………………\x02\x03",
            "……什么……\x02\x03",
            "那个现象又发生了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F（约修亚，这是……！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（啊啊……\x01",
            "　看来我们真的猜对了。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0x8, 1280, 0, 3540, 0)
    SetChrPos(0x9, 1280, 0, 3540, 0)
    SetChrPos(0xA, 1280, 0, 3540, 0)

    def lambda_24EC():

        label("loc_24EC")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_24EC")

    QueueWorkItem2(0x101, 3, lambda_24EC)

    def lambda_24FD():

        label("loc_24FD")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_24FD")

    QueueWorkItem2(0x102, 3, lambda_24FD)

    def lambda_250E():
        OP_6D(-120, 180, -6630, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_250E)

    def lambda_2526():
        OP_6B(4090, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2526)

    def lambda_2536():
        OP_8E(0xFE, 0xFFFFFF38, 0xAA, 0xFFFFE6BA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2536)
    Sleep(500)

    def lambda_2556():
        OP_8E(0xFE, 0xFFFFFC0E, 0x0, 0xFFFFEBD8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2556)
    Sleep(500)

    def lambda_2576():
        OP_8E(0xFE, 0x3DE, 0x0, 0xFFFFECD2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2576)
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "#701F#2P非常抱歉，\x01",
            "让你们看到丢人的事了。\x02\x03",
            "最近要塞大门的开关装置\x01",
            "好像运作得不太好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F原来如此，那还真是不妙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F如果情况很糟的话，\x01",
            "就请中央工房的人来修理一下吧。\x02\x03",
            "像拉赛尔博士那样厉害的人，\x01",
            "肯定能马上为你们修好的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#701F#2P嗯、嗯，我们会考虑的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    ChrTalk(
        0x8,
        (
            "#704F在装置修好之前，\x01",
            "你们在这里警戒。\x02\x03",
            "不许随便让普通平民靠近。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        "是！\x02",
    )

    CloseMessageWindow()

    def lambda_27AB():
        OP_8E(0xFE, 0xFFFFF254, 0x0, 0xFFFFED18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_27AB)

    def lambda_27C6():

        label("loc_27C6")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_27C6")

    QueueWorkItem2(0x9, 1, lambda_27C6)

    ChrTalk(
        0xA,
        "明白！\x02",
    )

    CloseMessageWindow()

    def lambda_27ED():
        OP_8E(0xFE, 0xEA6, 0x0, 0xFFFFEBE2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_27ED)

    def lambda_2808():

        label("loc_2808")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_2808")

    QueueWorkItem2(0xA, 1, lambda_2808)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#701F#2P那就这样了，\x01",
            "你们也尽快回去吧。\x02\x03",
            "关于那张要塞的照片，\x01",
            "我一定会代为转交情报部的。\x02\x03",
            "我这就告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    def lambda_28B5():
        OP_6D(-220, 250, -8550, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_28B5)

    def lambda_28CD():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_28CD)

    def lambda_28E5():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_28E5)

    def lambda_28F5():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_28F5)

    def lambda_2905():
        OP_8E(0xFE, 0x4EC, 0xFA, 0xD48, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2905)
    WaitChrThread(0x0, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    EventEnd(0x0)
    OP_85(0x9)
    OP_85(0xA)
    OP_4B(0x9, 0)
    OP_4B(0xA, 0)

    label("loc_293F")

    Return()

    # Function_5_C22 end

    def Function_6_2940(): pass

    label("Function_6_2940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B7F")
    OP_A2(0x55D)
    OP_28(0x43, 0x1, 0x8)
    OP_28(0x43, 0x1, 0x10)
    EventBegin(0x0)
    TurnDirection(0x102, 0x101, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F真是不敢相信啊……\x02\x03",
            "刚才的果然是那个吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F嗯……\x01",
            "应该就是那个现象了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F这么说来……\x02\x03",
            "#005F难道拉赛尔博士\x01",
            "被捉到这个要塞里来了……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（小声点，艾丝蒂尔……）\x02\x03",
            "（在这种地方\x01",
            "　还是不要把那件事说出来为好。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F（明、明白了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F（总之还是先回蔡斯，\x01",
            "　然后和雾香小姐商量一下吧。）\x02\x03",
            "（可以的话……\x01",
            "　最好把玛多克工房长也请过来。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3120   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2B7F")

    Return()

    # Function_6_2940 end

    def Function_7_2B80(): pass

    label("Function_7_2B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C1A")
    EventBegin(0x1)
    OP_4A(0x9, 0)
    OP_4A(0xA, 0)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0x9,
        (
            "你应该知道吧，\x01",
            "这里禁止闲杂人等进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你们赶快回去吧。\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_8C(0x9, 180, 0)
    OP_8C(0xA, 180, 0)
    OP_4B(0x9, 0)
    OP_4B(0xA, 0)

    label("loc_2C1A")

    Return()

    # Function_7_2B80 end

    def Function_8_2C1B(): pass

    label("Function_8_2C1B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　警告！　　　　\x01",
            "军队重地，严禁拍摄\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_2C1B end

    SaveToFile()

Try(main)
