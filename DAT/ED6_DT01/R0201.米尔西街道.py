from ED6ScenarioHelper import *

def main():
    # 米尔西街道

    CreateScenaFile(
        FileName            = 'R0201   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0201.x',
        MapIndex            = 22,
        MapDefaultBGM       = "ed60020",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/R0201   ._SN',
            'ED6_DT01/R0201_1 ._SN',
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
        '魔兽',                                 # 9
        '魔兽',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '艾丝蒂尔',                             # 13
        '约修亚',                               # 14
        '艾丝蒂尔',                             # 15
        '约修亚',                               # 16
        '洛连特方向',                           # 17
        '威尔特桥·关所方向',                   # 18
        '帕赛尔农场方向',                       # 19
        '跳跳猫',                               # 20
        '爆种铃兰',                             # 21
        '红茶钳虫',                             # 22
        '跳跳猫',                               # 23
        '爆种铃兰',                             # 24
        '红茶钳虫',                             # 25
        '跳跳猫',                               # 26
        '红茶钳虫',                             # 27
        '爆种铃兰',                             # 28
        '红茶钳虫',                             # 29
        '爆种铃兰',                             # 30
        '爆种铃兰',                             # 31
        '跳跳猫',                               # 32
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
        Unknown_28              = 3200,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 22,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10020 ._CH',             # 00
        'ED6_DT09/CH10021 ._CH',             # 01
        'ED6_DT07/CH00000 ._CH',             # 02
        'ED6_DT07/CH00010 ._CH',             # 03
        'ED6_DT07/CH00101 ._CH',             # 04
        'ED6_DT07/CH00111 ._CH',             # 05
        'ED6_DT07/CH00100 ._CH',             # 06
        'ED6_DT07/CH00110 ._CH',             # 07
        'ED6_DT09/CH10020 ._CH',             # 08
        'ED6_DT09/CH10021 ._CH',             # 09
        'ED6_DT09/CH10180 ._CH',             # 0A
        'ED6_DT09/CH10181 ._CH',             # 0B
        'ED6_DT09/CH10260 ._CH',             # 0C
        'ED6_DT09/CH10261 ._CH',             # 0D
        'ED6_DT09/CH10210 ._CH',             # 0E
        'ED6_DT09/CH10211 ._CH',             # 0F
        'ED6_DT07/CH00107 ._CH',             # 10
        'ED6_DT07/CH00001 ._CH',             # 11
        'ED6_DT07/CH00011 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT09/CH10020P._CP',             # 00
        'ED6_DT09/CH10021P._CP',             # 01
        'ED6_DT07/CH00000P._CP',             # 02
        'ED6_DT07/CH00010P._CP',             # 03
        'ED6_DT07/CH00101P._CP',             # 04
        'ED6_DT07/CH00111P._CP',             # 05
        'ED6_DT07/CH00100P._CP',             # 06
        'ED6_DT07/CH00110P._CP',             # 07
        'ED6_DT09/CH10020P._CP',             # 08
        'ED6_DT09/CH10021P._CP',             # 09
        'ED6_DT09/CH10180P._CP',             # 0A
        'ED6_DT09/CH10181P._CP',             # 0B
        'ED6_DT09/CH10260P._CP',             # 0C
        'ED6_DT09/CH10261P._CP',             # 0D
        'ED6_DT09/CH10210P._CP',             # 0E
        'ED6_DT09/CH10211P._CP',             # 0F
        'ED6_DT07/CH00107P._CP',             # 10
        'ED6_DT07/CH00001P._CP',             # 11
        'ED6_DT07/CH00011P._CP',             # 12
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -131580,
        Z                   = 0,
        Y                   = -18130,
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
        X                   = -224350,
        Z                   = 20,
        Y                   = -16180,
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
        X                   = -184980,
        Z                   = 0,
        Y                   = -81290,
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
        X                   = -160000,
        Z                   = 200,
        Y                   = -2000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -161000,
        Z                   = 0,
        Y                   = -21000,
        Unknown_0C          = 0,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -155000,
        Z                   = 0,
        Y                   = -44000,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -178000,
        Z                   = 500,
        Y                   = -29000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -190000,
        Z                   = 0,
        Y                   = -39000,
        Unknown_0C          = 0,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -205000,
        Z                   = 200,
        Y                   = -55000,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -193000,
        Z                   = 200,
        Y                   = -2000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -207000,
        Z                   = 200,
        Y                   = -6000,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -198000,
        Z                   = 300,
        Y                   = -47000,
        Unknown_0C          = 0,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -180000,
        Z                   = -500,
        Y                   = -58000,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x80,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -159000,
        Z                   = 200,
        Y                   = -59000,
        Unknown_0C          = 0,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x85,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -180000,
        Z                   = 0,
        Y                   = -5000,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x85,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -172000,
        Z                   = 200,
        Y                   = -43000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -204160,
        TriggerZ            = 0,
        TriggerY            = -21600,
        TriggerRange        = 1700,
        ActorX              = -204160,
        ActorZ              = 2500,
        ActorY              = -21600,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -179550,
        TriggerZ            = 0,
        TriggerY            = -15360,
        TriggerRange        = 1500,
        ActorX              = -179550,
        ActorZ              = 1500,
        ActorY              = -15360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -176080,
        TriggerZ            = 50,
        TriggerY            = 11940,
        TriggerRange        = 1000,
        ActorX              = -176140,
        ActorZ              = 1050,
        ActorY              = 12680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -211720,
        TriggerZ            = 20,
        TriggerY            = -56010,
        TriggerRange        = 1000,
        ActorX              = -211660,
        ActorZ              = 20,
        ActorY              = -56570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -145080,
        TriggerZ            = 40,
        TriggerY            = -50920,
        TriggerRange        = 1000,
        ActorX              = -144640,
        ActorZ              = 40,
        ActorY              = -51360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4C2",          # 00, 0
        "Function_1_52A",          # 01, 1
        "Function_2_5B8",          # 02, 2
        "Function_3_5CE",          # 03, 3
        "Function_4_6E3",          # 04, 4
        "Function_5_6FF",          # 05, 5
        "Function_6_744",          # 06, 6
        "Function_7_888",          # 07, 7
        "Function_8_9C6",          # 08, 8
    )


    def Function_0_4C2(): pass

    label("Function_0_4C2")

    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4F6"),
        (SWITCH_DEFAULT, "loc_529"),
    )


    label("loc_4F6")

    SetChrPos(0x101, -184970, -500, -80630, 0)
    SetChrPos(0x102, -184970, -500, -80630, 0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    Event(0, 3)
    Jump("loc_529")

    label("loc_529")

    Return()

    # Function_0_4C2 end

    def Function_1_52A(): pass

    label("Function_1_52A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_543")
    OP_64(0x0, 0x1)
    Jump("loc_55A")

    label("loc_543")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_55A")
    OP_64(0x0, 0x1)
    Jump("loc_55A")

    label("loc_55A")

    OP_16(0x2, 0xFA0, 0xFFFB54B0, 0xFFFD8730, 0x3000C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57E")
    OP_6F(0x0, 0)
    Jump("loc_585")

    label("loc_57E")

    OP_6F(0x0, 60)

    label("loc_585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_597")
    OP_6F(0x1, 0)
    Jump("loc_59E")

    label("loc_597")

    OP_6F(0x1, 60)

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B0")
    OP_6F(0x2, 0)
    Jump("loc_5B7")

    label("loc_5B0")

    OP_6F(0x2, 60)

    label("loc_5B7")

    Return()

    # Function_1_52A end

    def Function_2_5B8(): pass

    label("Function_2_5B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5B8")

    label("loc_5CD")

    Return()

    # Function_2_5B8 end

    def Function_3_5CE(): pass

    label("Function_3_5CE")

    EventBegin(0x0)
    OP_6D(-185000, -500, -66930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_43(0x102, 0x0, 0x0, 0x4)
    Sleep(800)
    OP_8E(0x101, 0xFFFD2CD6, 0xFFFFFE0C, 0xFFFEEF4E, 0xBB8, 0x0)

    ChrTalk(
        0x102,
        (
            "#010F我们赶快回协会吧。\x02\x03",
            "#010F把这份工作报告做好之后，\x01",
            "继续去做下一个任务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯，好啊。\x02\x03",
            "#001F就这样接着做下去吧～！\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x400000)
    OP_A2(0x239)
    EventEnd(0x0)
    Return()

    # Function_3_5CE end

    def Function_4_6E3(): pass

    label("Function_4_6E3")

    OP_8E(0xFE, 0xFFFD2C90, 0xFFFFFE0C, 0xFFFEF69C, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_4_6E3 end

    def Function_5_6FF(): pass

    label("Function_5_6FF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南　帕赛尔农场\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_6FF end

    def Function_6_744(): pass

    label("Function_6_744")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_833")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_7BA")
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
    OP_A2(0x297)
    Jump("loc_830")

    label("loc_7BA")

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

    label("loc_830")

    Jump("loc_87A")

    label("loc_833")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x77)

    label("loc_87A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_744 end

    def Function_7_888(): pass

    label("Function_7_888")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_977")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_8FE")
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
    OP_A2(0x298)
    Jump("loc_974")

    label("loc_8FE")

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

    label("loc_974")

    Jump("loc_9B8")

    label("loc_977")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x78)

    label("loc_9B8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_888 end

    def Function_8_9C6(): pass

    label("Function_8_9C6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_A3C")
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
    OP_A2(0x299)
    Jump("loc_AB2")

    label("loc_A3C")

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
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_AB2")

    Jump("loc_AF6")

    label("loc_AB5")

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
    OP_83(0xF, 0x79)

    label("loc_AF6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_9C6 end

    SaveToFile()

Try(main)
