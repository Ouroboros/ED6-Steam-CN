from ED6ScenarioHelper import *

def main():
    # 迷雾峡谷

    CreateScenaFile(
        FileName            = 'C1401   ._SN',
        MapName             = 'Bose',
        Location            = 'C1401.x',
        MapIndex            = 60,
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
        '卫兵',                                 # 9
        '卫兵',                                 # 10
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
        Unknown_3A              = 60,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT09/CH10170 ._CH',             # 01
        'ED6_DT09/CH10171 ._CH',             # 02
        'ED6_DT09/CH11170 ._CH',             # 03
        'ED6_DT09/CH11171 ._CH',             # 04
        'ED6_DT09/CH11180 ._CH',             # 05
        'ED6_DT09/CH11181 ._CH',             # 06
        'ED6_DT09/CH11190 ._CH',             # 07
        'ED6_DT09/CH11191 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT09/CH10170P._CP',             # 01
        'ED6_DT09/CH10171P._CP',             # 02
        'ED6_DT09/CH11170P._CP',             # 03
        'ED6_DT09/CH11171P._CP',             # 04
        'ED6_DT09/CH11180P._CP',             # 05
        'ED6_DT09/CH11181P._CP',             # 06
        'ED6_DT09/CH11190P._CP',             # 07
        'ED6_DT09/CH11191P._CP',             # 08
    )

    DeclNpc(
        X                   = 1220,
        Z                   = -2070,
        Y                   = 185310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = -2070,
        Y                   = 185310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -31230,
        Z                   = -30,
        Y                   = 76720,
        Unknown_0C          = 165,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22600,
        Z                   = 0,
        Y                   = 45730,
        Unknown_0C          = 225,
        Unknown_0E          = 5,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xBA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1980,
        Z                   = 40,
        Y                   = 82660,
        Unknown_0C          = 164,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xBD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8330,
        Z                   = -1840,
        Y                   = 91320,
        Unknown_0C          = 114,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2350,
        Z                   = -1960,
        Y                   = 58080,
        Unknown_0C          = 156,
        Unknown_0E          = 7,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xBB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31080,
        Z                   = -1990,
        Y                   = 103160,
        Unknown_0C          = 43,
        Unknown_0E          = 7,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xBE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5530,
        Z                   = -1920,
        Y                   = 140390,
        Unknown_0C          = 293,
        Unknown_0E          = 7,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xBE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10740,
        Z                   = -2009,
        Y                   = 162000,
        Unknown_0C          = 284,
        Unknown_0E          = 5,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10420,
        Z                   = -1910,
        Y                   = 77510,
        Unknown_0C          = 103,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21780,
        Z                   = -2050,
        Y                   = 78280,
        Unknown_0C          = 162,
        Unknown_0E          = 5,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -330,
        Y                   = -4000,
        Z                   = 184860,
        Range               = 5340,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x2C808,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -26110,
        Y                   = -4000,
        Z                   = 69000,
        Range               = -38850,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x11558,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = -9350,
        TriggerZ            = -1950,
        TriggerY            = 71290,
        TriggerRange        = 1500,
        ActorX              = -9350,
        ActorZ              = -450,
        ActorY              = 71290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 19360,
        TriggerZ            = -1990,
        TriggerY            = 166110,
        TriggerRange        = 1000,
        ActorX              = 19810,
        ActorZ              = -490,
        ActorY              = 166800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2D2",          # 00, 0
        "Function_1_31E",          # 01, 1
        "Function_2_358",          # 02, 2
        "Function_3_36E",          # 03, 3
        "Function_4_3D6",          # 04, 4
        "Function_5_7FD",          # 05, 5
        "Function_6_8E9",          # 06, 6
        "Function_7_A89",          # 07, 7
        "Function_8_13A8",         # 08, 8
    )


    def Function_0_2D2(): pass

    label("Function_0_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2E9")
    OP_A3(0x3FA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_2E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_2F7")
    OP_A3(0x3FB)
    Event(0, 4)

    label("loc_2F7")

    SetMapFlags(0x10)
    OP_11(0xFF, 0xFF, 0xFF, 0x80E8, 0xD2F0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_END)), "loc_31D")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_31D")

    Return()

    # Function_0_2D2 end

    def Function_1_31E(): pass

    label("Function_1_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32E")
    OP_71(0x0, 0x4)

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 3)), scpexpr(EXPR_END)), "loc_33E")
    OP_71(0x1, 0x4)
    OP_64(0x0, 0x1)

    label("loc_33E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350")
    OP_6F(0x2, 0)
    Jump("loc_357")

    label("loc_350")

    OP_6F(0x2, 60)

    label("loc_357")

    Return()

    # Function_1_31E end

    def Function_2_358(): pass

    label("Function_2_358")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_358")

    label("loc_36D")

    Return()

    # Function_2_358 end

    def Function_3_36E(): pass

    label("Function_3_36E")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-6987, -2000, 112486, 0)
    OP_6B(4500, 0)
    OP_6C(288000, 0)

    def lambda_39E():
        OP_6D(630, 3040, 186710, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39E)

    def lambda_3B6():
        OP_6B(2500, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B6)
    OP_6C(48000, 10000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C1301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_36E end

    def Function_4_3D6(): pass

    label("Function_4_3D6")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(2616, -2000, 188840, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)

    def lambda_406():
        OP_67(0, 3600, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_406)

    def lambda_41E():
        OP_6B(3400, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41E)
    OP_6C(24000, 4000)
    Sleep(1000)
    OP_22(0xC1, 0x0, 0x64)
    PlayEffect(0x12, 0xFF, 0xFF, 2616, -2000, 188840, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x101, 2780, -2020, 190580, 209)
    SetChrPos(0x103, 2140, -2029, 191100, 190)
    SetChrPos(0x102, 2780, -2020, 191990, 178)
    SetChrPos(0x104, 2380, -2029, 192390, 184)
    OP_71(0x0, 0x4)
    OP_6B(3470, 0)
    OP_6B(3400, 80)
    Sleep(1000)

    def lambda_4D6():
        OP_6D(2180, -1900, 181510, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4D6)

    def lambda_4EE():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4EE)

    def lambda_4FE():
        OP_6E(318, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4FE)

    def lambda_50E():
        OP_8E(0xFE, 0x97E, 0xFFFFF858, 0x2CFCE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50E)
    Sleep(200)

    def lambda_52E():
        OP_8E(0xFE, 0x6C2, 0xFFFFF830, 0x2D3FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_52E)
    Sleep(200)

    def lambda_54E():
        OP_8E(0xFE, 0xD84, 0xFFFFF858, 0x2D1B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54E)
    Sleep(200)

    def lambda_56E():
        OP_8E(0xFE, 0xB54, 0xFFFFF84E, 0x2D618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_56E)
    Sleep(3000)

    ChrTalk(
        0x101,
        "#004F是、是暗门呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F不愧是古老的隐藏堡垒。\x01",
            "这可真是华丽的欺骗技巧啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        (
            "#012F这里是……\x01",
            "『迷雾峡谷』的一个角落吧。\x02\x03",
            "雪拉姐姐，\x01",
            "先让人质从这里逃走吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_695():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_695)

    def lambda_6A3():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A3)
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(
        0x103,
        (
            "#022F不……\x01",
            "还是先去抓空贼的首领。\x02\x03",
            "要是人质逃走时候遇到袭击的话，\x01",
            "单凭我们几个是无法保护那么多人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F啊，对啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F哈·哈·哈。\x01",
            "那我们赶快回去和空贼首领对决吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x357)
    EventEnd(0x0)
    Return()

    # Function_4_3D6 end

    def Function_5_7FD(): pass

    label("Function_5_7FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_END)), "loc_8E8")
    EventBegin(0x1)
    OP_4A(0x8, 0)
    TurnDirection(0x8, 0x0, 400)

    def lambda_817():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_817)
    TurnDirection(0x1, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "现在里面正在进行调查，\x01",
            "平民不得入内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "对不起，请回去吧。\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8C(0x8, 180, 0)
    OP_4B(0x8, 0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_8E8")

    Return()

    # Function_5_7FD end

    def Function_6_8E9(): pass

    label("Function_6_8E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A88")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C9")
    TurnDirection(0x103, 0x1, 400)

    def lambda_910():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_910)

    def lambda_91E():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_91E)
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(
        0x103,
        (
            "#022F还没有把空贼头目抓住，\x01",
            "现在离开的话太危险了。\x02\x03",
            "……回空贼基地里去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6D")

    label("loc_9C9")

    TurnDirection(0x103, 0x0, 400)

    def lambda_9D6():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9D6)

    def lambda_9E4():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_9E4)
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(
        0x103,
        (
            "#022F等一下，\x01",
            "还没有把空贼头目抓住呢。\x02\x03",
            "赶快回空贼基地里去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6D")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_A88")

    Return()

    # Function_6_8E9 end

    def Function_7_A89(): pass

    label("Function_7_A89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B77")
    SetMapFlags(0x8000000)
    OP_28(0x11, 0x1, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x386, 1)"), scpexpr(EXPR_END)), "loc_B1C")
    OP_71(0x1, 0x4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "熊刺草\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x0, 0x1)
    OP_A2(0x363)
    Jump("loc_B6C")

    label("loc_B1C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "熊刺草\x07\x00",
            "发现了，\x01\x07\x00",
            "不过现有的数量太多，不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B6C")

    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_13A7")

    label("loc_B77")

    OP_28(0x11, 0x1, 0x4)
    SetMapFlags(0x8000000)
    EventBegin(0x0)
    Fade(1000)
    OP_6C(125000, 0)
    SetChrPos(0x101, -7970, -2000, 71470, 270)
    SetChrPos(0x102, -7850, -2070, 72520, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD3")
    SetChrPos(0x103, -6790, -2009, 71120, 270)

    label("loc_BD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF2")
    SetChrPos(0x104, -6370, -2009, 72240, 270)

    label("loc_BF2")

    OP_69(0x101, 0x0)
    OP_6C(135000, 2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x386, 1)"), scpexpr(EXPR_END)), "loc_C69")
    OP_71(0x1, 0x4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "熊刺草\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x0, 0x1)
    OP_A2(0x363)
    Jump("loc_CB9")

    label("loc_C69")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "熊刺草\x07\x00",
            "发现了，\x01\x07\x00",
            "不过现有的数量太多，不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_11FF")

    ChrTalk(
        0x101,
        (
            "#000F呼，终～于找到了。\x02\x03",
            "接下来要做的就是\x01",
            "把这个地方告诉超市的老爷爷。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E3C")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#020F那么，艾丝蒂尔，\x01",
            "我问你一下……\x02\x03",
            "你知道这里是什么地方吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿，\x01",
            "雪拉姐的问题真无聊。\x02\x03",
            "『蜜猪峡谷』，对吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EEA")

    label("loc_E3C")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔，\x01",
            "你知道这个地方叫什么吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#502F真是的，别把我当傻瓜啊。\x02\x03",
            "『蜜猪峡谷』，对吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F91")

    ChrTalk(
        0x102,
        "#015F……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F哦……\x02\x03",
            "不管怎么说\x01",
            "真是个能引起食欲的名字啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔……\x02\x03",
            "这里叫『迷雾峡谷』啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1061")

    label("loc_F91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101C")

    ChrTalk(
        0x102,
        "#015F……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#027F……真是个非常美味的名字啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔……\x02\x03",
            "这里叫『迷雾峡谷』啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1061")

    label("loc_101C")


    ChrTalk(
        0x102,
        (
            "#018F……………………\x02\x03",
            "#018F艾丝蒂尔……\x01",
            "这里叫『迷雾峡谷』啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1061")


    ChrTalk(
        0x101,
        "#008F啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A7")

    ChrTalk(
        0x103,
        "#025F……还好事先问了你一下。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_10D7")

    label("loc_10A7")


    ChrTalk(
        0x102,
        "#015F……还好事先问了你一下。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    label("loc_10D7")


    ChrTalk(
        0x101,
        (
            "#009F这、这也是没办法的事情啊，\x01",
            "人家正处于生长发育旺盛的时期嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F这算什么理由啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#008F好、好啦好啦，\x01",
            "我们这是在工作中啊，工作中。\x02\x03",
            "快点出发吧，好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)

    ChrTalk(
        0x102,
        "#017F真拿你没办法……\x02",
    )

    CloseMessageWindow()
    Jump("loc_13A0")

    label("loc_11FF")


    ChrTalk(
        0x101,
        (
            "#000F嗯～这是『熊刺草』呢。\x02\x03",
            "说起来……\x01",
            "好像有谁正在找这个东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F0")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#020F不是在公告板上写着的吗？\x02\x03",
            "看看手册里的记载吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_137D")

    label("loc_12F0")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F是在公告板上写着的吧。\x02\x03",
            "看看手册里的记载吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    label("loc_137D")


    ChrTalk(
        0x101,
        "#006F嗯，好吧。\x02",
    )

    CloseMessageWindow()

    label("loc_13A0")

    EventEnd(0x0)
    ClearMapFlags(0x8000000)

    label("loc_13A7")

    Return()

    # Function_7_A89 end

    def Function_8_13A8(): pass

    label("Function_8_13A8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1494")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x116, 1)"), scpexpr(EXPR_END)), "loc_141D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "斯托雷加Ｒ\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x377)
    Jump("loc_1491")

    label("loc_141D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "斯托雷加Ｒ\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "斯托雷加Ｒ\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_1491")

    Jump("loc_14E2")

    label("loc_1494")

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
    OP_83(0xF, 0x16)

    label("loc_14E2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_13A8 end

    SaveToFile()

Try(main)
