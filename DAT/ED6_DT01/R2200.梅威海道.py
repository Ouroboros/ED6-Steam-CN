from ED6ScenarioHelper import *

def main():
    # 梅威海道

    CreateScenaFile(
        FileName            = 'R2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2200.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60020",
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
        '克拉姆',                               # 9
        '玛诺利亚村方向',                       # 10
        '玛西亚孤儿院方向',                     # 11
        '卢安方向',                             # 12
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
        Unknown_3A              = 101,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02590 ._CH',             # 00
        'ED6_DT07/CH00040 ._CH',             # 01
        'ED6_DT07/CH00041 ._CH',             # 02
        'ED6_DT09/CH10160 ._CH',             # 03
        'ED6_DT09/CH10161 ._CH',             # 04
        'ED6_DT09/CH10450 ._CH',             # 05
        'ED6_DT09/CH10451 ._CH',             # 06
        'ED6_DT09/CH10220 ._CH',             # 07
        'ED6_DT09/CH10221 ._CH',             # 08
        'ED6_DT09/CH10460 ._CH',             # 09
        'ED6_DT09/CH10461 ._CH',             # 0A
        'ED6_DT09/CH10480 ._CH',             # 0B
        'ED6_DT09/CH10481 ._CH',             # 0C
        'ED6_DT09/CH10470 ._CH',             # 0D
        'ED6_DT09/CH10471 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02590P._CP',             # 00
        'ED6_DT07/CH00040P._CP',             # 01
        'ED6_DT07/CH00041P._CP',             # 02
        'ED6_DT09/CH10160P._CP',             # 03
        'ED6_DT09/CH10161P._CP',             # 04
        'ED6_DT09/CH10450P._CP',             # 05
        'ED6_DT09/CH10451P._CP',             # 06
        'ED6_DT09/CH10220P._CP',             # 07
        'ED6_DT09/CH10221P._CP',             # 08
        'ED6_DT09/CH10460P._CP',             # 09
        'ED6_DT09/CH10461P._CP',             # 0A
        'ED6_DT09/CH10480P._CP',             # 0B
        'ED6_DT09/CH10481P._CP',             # 0C
        'ED6_DT09/CH10470P._CP',             # 0D
        'ED6_DT09/CH10471P._CP',             # 0E
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
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
        X                   = -139370,
        Z                   = -2020,
        Y                   = 15120,
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
        X                   = -28630,
        Z                   = -1990,
        Y                   = 79340,
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
        X                   = 7410,
        Z                   = -2000,
        Y                   = 29980,
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


    DeclMonster(
        X                   = -96260,
        Z                   = -1950,
        Y                   = 27960,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x181,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -104740,
        Z                   = -5970,
        Y                   = 11000,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -81100,
        Z                   = -5870,
        Y                   = 13330,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88220,
        Z                   = -5960,
        Y                   = 9810,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -96260,
        Z                   = -1950,
        Y                   = 27960,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x325,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -104740,
        Z                   = -5970,
        Y                   = 11000,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x330,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -81100,
        Z                   = -5870,
        Y                   = 13330,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x330,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88220,
        Z                   = -5960,
        Y                   = 9810,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x331,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -30500,
        Y                   = 2000,
        Z                   = 36300,
        Range               = -27500,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0x6464,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -14300,
        Y                   = 2000,
        Z                   = 34900,
        Range               = -11500,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0x58AC,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -23460,
        Y                   = 2000,
        Z                   = 55770,
        Range               = -34700,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0xC760,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -38000,
        Y                   = 2000,
        Z                   = 33000,
        Range               = -40000,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0x55F0,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = -21830,
        TriggerZ            = -2000,
        TriggerY            = 37790,
        TriggerRange        = 1500,
        ActorX              = -21830,
        ActorZ              = -800,
        ActorY              = 37790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18840,
        TriggerZ            = -2000,
        TriggerY            = 33860,
        TriggerRange        = 1500,
        ActorX              = -18840,
        ActorZ              = -500,
        ActorY              = 33860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -114230,
        TriggerZ            = -6050,
        TriggerY            = 11770,
        TriggerRange        = 1000,
        ActorX              = -114730,
        ActorZ              = -6040,
        ActorY              = 12270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -77980,
        TriggerZ            = -6870,
        TriggerY            = -11780,
        TriggerRange        = 1000,
        ActorX              = -77540,
        ActorZ              = -6730,
        ActorY              = -11140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_392",          # 00, 0
        "Function_1_3B5",          # 01, 1
        "Function_2_477",          # 02, 2
        "Function_3_7C8",          # 03, 3
        "Function_4_1172",         # 04, 4
        "Function_5_128A",         # 05, 5
        "Function_6_13B4",         # 06, 6
        "Function_7_182B",         # 07, 7
        "Function_8_1875",         # 08, 8
        "Function_9_18DF",         # 09, 9
        "Function_10_1A30",        # 0A, 10
    )


    def Function_0_392(): pass

    label("Function_0_392")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_39E"),
        (SWITCH_DEFAULT, "loc_3B4"),
    )


    label("loc_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B1")
    OP_A2(0x43D)
    Event(0, 6)

    label("loc_3B1")

    Jump("loc_3B4")

    label("loc_3B4")

    Return()

    # Function_0_392 end

    def Function_1_3B5(): pass

    label("Function_1_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CD")
    OP_B1("R2200_y")
    Jump("loc_3D6")

    label("loc_3CD")

    OP_B1("R2200_n")

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F9")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_40D")

    label("loc_3F9")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_41D")
    OP_10(0x1, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_423")

    label("loc_41D")

    OP_10(0x1, 0x1)
    OP_10(0x3, 0x0)

    label("loc_423")

    OP_16(0x2, 0xFA0, 0xFFFD21A0, 0xFFFE5638, 0x30026)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_447")
    OP_6F(0x0, 0)
    Jump("loc_44E")

    label("loc_447")

    OP_6F(0x0, 60)

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_460")
    OP_6F(0x1, 0)
    Jump("loc_467")

    label("loc_460")

    OP_6F(0x1, 60)

    label("loc_467")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x186A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C8, 0x1, 0x64)
    Return()

    # Function_1_3B5 end

    def Function_2_477(): pass

    label("Function_2_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C7")
    OP_A2(0x40E)
    EventBegin(0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4A6():
        OP_6D(-22740, -1990, 38220, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4A6)

    def lambda_4BE():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4BE)

    def lambda_4CE():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4CE)
    WaitChrThread(0x0, 0x2)
    SetChrPos(0x101, -28320, -2000, 32860, 90)
    SetChrPos(0x102, -28920, -2000, 32460, 90)

    def lambda_505():
        OP_8E(0xFE, 0xFFFFA646, 0xFFFFF83A, 0x9448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_505)
    Sleep(800)

    def lambda_525():
        OP_8E(0xFE, 0xFFFFA4F2, 0xFFFFF830, 0x8EC6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_525)
    WaitChrThread(0x101, 0x1)

    def lambda_545():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_545)
    WaitChrThread(0x102, 0x1)

    def lambda_558():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_558)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　玛西亚孤儿院\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#002F#1P…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_5B4():
        OP_6D(-23610, -2000, 39450, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5B4)
    OP_8C(0x102, 315, 400)
    WaitChrThread(0x0, 0x2)

    ChrTalk(
        0x102,
        (
            "#010F看起来，\x01",
            "孤儿院就在这里面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#1P嗯……\x02\x03",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_632():
        OP_6D(-22740, -1990, 38220, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_632)
    TurnDirection(0x102, 0x101, 400)
    WaitChrThread(0x0, 0x2)

    ChrTalk(
        0x102,
        "#014F怎么了，艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#1P……好的，我决定了！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#005F#1P就算自己的身世再怎么可怜，\x01",
            "偷别人的东西就是不对！\x02\x03",
            "等我抓到那个调皮蛋之后，\x01",
            "一定要好好教训教训他！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#019F哈哈，在烦恼中得出结论，\x01",
            "还真是艾丝蒂尔的风格……\x02\x03",
            "#010F不管怎么说，对小孩子还是温柔点好。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_7C7")

    Return()

    # Function_2_477 end

    def Function_3_7C8(): pass

    label("Function_3_7C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1171")
    OP_A2(0x411)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_51(0x136, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x136, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -22174, -700, 54574, 0)

    NpcTalk(
        0x8,
        "少年的声音",
        "……科洛丝姐姐。\x02",
    )

    CloseMessageWindow()
    OP_62(0x136, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6D(-25380, -2050, 57450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -25380, -2000, 57447, 225)
    SetChrPos(0x136, -26370, -2000, 58130, 180)
    SetChrPos(0x102, -27810, -2000, 57580, 135)
    OP_0D()
    OP_8E(0x8, 0xFFFF9F2A, 0xFFFFFD44, 0xCC6A, 0x1B58, 0x0)
    OP_8C(0x8, 270, 0)
    OP_96(0x8, 0xFFFF9BCE, 0xFFFFF7F4, 0xD340, 0x3E8, 0x1B58)
    OP_8E(0x8, 0xFFFF96EC, 0xFFFFF830, 0xD49E, 0x1B58, 0x0)
    OP_8C(0x8, 0, 600)
    ClearChrFlags(0x8, 0x4)

    ChrTalk(
        0x136,
        "#044F克拉姆？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，是调皮蛋！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x136, 0x2)

    ChrTalk(
        0x136,
        (
            "#042F你呀……\x01",
            "怎么到这种地方来玩呢？\x02\x03",
            "要是碰到魔兽怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#775F我、我只是想和科洛丝姐姐\x01",
            "说声对不起而已……\x02\x03",
            "我骗你说没有恶作剧，\x01",
            "实在对不起呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F呵呵……\x01",
            "我并没有生你的气啊。\x02\x03",
            "#041F不过，\x01",
            "你是不是还要向谁道个歉呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        (
            "#774F啊……\x02\x03",
            "才、才不会呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#048F你是个心地很好的孩子，\x01",
            "这点我是很清楚的。\x02\x03",
            "乖孩子……说声对不起好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#773F…………………………\x02\x03",
            "既然科洛丝姐姐这样说，\x01",
            "那我只有照办了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B81():

        label("loc_B81")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_B81")

    QueueWorkItem2(0x101, 1, lambda_B81)

    def lambda_B92():

        label("loc_B92")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_B92")

    QueueWorkItem2(0x136, 1, lambda_B92)

    def lambda_BA3():

        label("loc_BA3")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_BA3")

    QueueWorkItem2(0x102, 1, lambda_BA3)
    OP_8E(0x8, 0xFFFF9CA5, 0xFFFFF830, 0xDC3C, 0xBB8, 0x0)
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#773F是我不好。\x01",
            "游击士姐姐。\x02\x03",
            "对……不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊、啊哈哈……\x01",
            "原来你是特意过来向我道歉的啊。\x02\x03",
            "#001F看样子你也有诚实的一面嘛㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x8, 0xFFFF9D54, 0xFFFFF7CC, 0xD9F8, 0xBB8, 0x0)

    ChrTalk(
        0x8,
        (
            "#774F你、你别误会哦！\x02\x03",
            "是科洛丝姐姐叫我说，\x01",
            "我才这样说的！\x02\x03",
            "#772F其实你自己也要检讨一下，\x01",
            "做游击士怎么能这么粗心大意呢！\x02\x03",
            "连像我这样的小孩\x01",
            "也能这么容易骗到你，这怎么行？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F呜……\x02",
    )

    CloseMessageWindow()
    OP_95(0x8, 0x0, 0x0, 0x0, 0x320, 0x1770)

    ChrTalk(
        0x8,
        (
            "#770F拜拜！\x01",
            "要努力锻炼才行哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFA1D0, 0xFFFFF830, 0xE006, 0x1770, 0x0)
    OP_8E(0x8, 0xFFFFA010, 0xFFFFF830, 0x12494, 0x1B58, 0x0)
    SetChrFlags(0x8, 0x80)

    ChrTalk(
        0x101,
        "#009F#2P还、还真的是一点都不可爱！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x136, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F算啦算啦。\x01",
            "他只是害羞而已吧。\x02\x03",
            "不过那孩子说的倒是很有道理，\x01",
            "粗心大意的确是你的缺点。\x02\x03",
            "你不觉得自己还要多锻炼一下才行吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F#2P哎呀呀……\x01",
            "约修亚也越来越不可爱了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x136, 180, 400)

    ChrTalk(
        0x136,
        (
            "#041F呵呵……\x02\x03",
            "艾丝蒂尔、约修亚，\x01",
            "你们两个感情真好。\x02\x03",
            "感觉就像真正的姐弟俩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#2P真、真的吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F要是从互相照顾的角度来看，\x01",
            "倒不如说是兄妹更加贴切吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F#2P哼～你不觉得这样说很没礼貌吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F呵呵，真是羡慕你们啊。\x01",
            "因为我是独生女。\x02\x03",
            "#049F所以呢，\x01",
            "我一直很向往这样的家庭气氛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#2P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#045F啊，没什么……\x02\x03",
            "#040F话就说到这里吧，\x01",
            "我们也该继续赶路了。\x02\x03",
            "沿着海岸街道一直走\x01",
            "就可以到卢安了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2PＯＫ。\x01",
            "那我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_1171")

    Return()

    # Function_3_7C8 end

    def Function_4_1172(): pass

    label("Function_4_1172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1289")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EB")

    ChrTalk(
        0x102,
        (
            "#010F往这边走是卢安市啦。\x02\x03",
            "要去孤儿院的话，\x01",
            "得回到刚才的三岔路口才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126E")

    ChrTalk(
        0x101,
        (
            "#000F哎……\x01",
            "这边是孤儿院吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不……\x01",
            "这边是卢安市啦。\x02\x03",
            "我们回到刚才的三岔路口去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126E")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_1289")

    Return()

    # Function_4_1172 end

    def Function_5_128A(): pass

    label("Function_5_128A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131E")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F往这边走是玛诺利亚啊。\x02\x03",
            "要去孤儿院的话，\x01",
            "得回到刚才的三岔路口才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1398")

    ChrTalk(
        0x102,
        (
            "#012F（往这边是玛诺利亚……）\x02\x03",
            "（要去孤儿院的话，\x01",
            "　得回到刚才的三岔路口才行。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1398")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_13B3")

    Return()

    # Function_5_128A end

    def Function_6_13B4(): pass

    label("Function_6_13B4")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-114260, -2000, 16980, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    SetChrPos(0x101, -113570, -2029, 17310, 270)
    SetChrPos(0x105, -114690, -1960, 16400, 0)
    SetChrPos(0x102, -115110, -2020, 17800, 135)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#582F不过，真想不到戴尔蒙市长\x01",
            "会是一系列事件的幕后主使……\x02\x03",
            "#005F那些亲切的态度和表现，\x01",
            "原来全都只是在做戏啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F那个……\x01",
            "有一点我不大清楚……\x02\x03",
            "这次的事件，\x01",
            "我们可以逮捕戴尔蒙市长吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F……哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F是啊……\x01",
            "恐怕会很难啊。\x02\x03",
            "因为不干涉国家内政\x01",
            "是游击士协会一贯以来的原则。\x02\x03",
            "要逮捕身为卢安地区负责人的现任市长，\x01",
            "我想，恐怕会很难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F等一下！\x01",
            "这太不合理了吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F的确不合理，\x01",
            "但这是明文的规定啊。\x02\x03",
            "就是因为有这条规定，\x01",
            "所以连埃雷波尼亚帝国\x01",
            "也可以设立游击士协会的支部。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F话、话是这么说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F总之先回协会\x01",
            "和嘉恩先生商量一下吧。\x02\x03",
            "我想他会帮我们出个好主意的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#049F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F没事的，不用担心！\x02\x03",
            "无论这次的犯人是怎样的人，\x01",
            "我们一定会将他们绳之以法的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#542F嗯……是啊。\x02",
    )

    CloseMessageWindow()
    OP_28(0x3E, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_6_13B4 end

    def Function_7_182B(): pass

    label("Function_7_182B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　玛西亚孤儿院\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_182B end

    def Function_8_1875(): pass

    label("Function_8_1875")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东　卢安市　　２３８塞尔矩\x01",
            "西　玛诺利亚村　７４塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1875 end

    def Function_9_18DF(): pass

    label("Function_9_18DF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1955")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4B9)
    Jump("loc_19CB")

    label("loc_1955")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_19CB")

    Jump("loc_1A22")

    label("loc_19CE")

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
    OP_83(0xF, 0x83)

    label("loc_1A22")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_18DF end

    def Function_10_1A30(): pass

    label("Function_10_1A30")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1AA6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4BA)
    Jump("loc_1B1C")

    label("loc_1AA6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_1B1C")

    Jump("loc_1B73")

    label("loc_1B1F")

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
    OP_83(0xF, 0x84)

    label("loc_1B73")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1A30 end

    SaveToFile()

Try(main)
