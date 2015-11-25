from ED6ScenarioHelper import *

def main():
    # 洛连特地下水路

    CreateScenaFile(
        FileName            = 'C0500   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0500.x',
        MapIndex            = 20,
        MapDefaultBGM       = "ed60031",
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
        '目标用摄像机',                         # 9
        '肮脏甲鼠2',                            # 10
        '紫色飞蛾群2',                          # 11
        '肮脏甲鼠3',                            # 12
        '肮脏甲鼠4',                            # 13
        '肮脏甲鼠4',                            # 14
        '肮脏甲鼠',                             # 15
        '肮脏甲鼠',                             # 16
        '紫色飞蛾群',                           # 17
        '紫色飞蛾群',                           # 18
        '紫色飞蛾群',                           # 19
        '肮脏甲鼠',                             # 20
        '肮脏甲鼠',                             # 21
        '紫色飞蛾群',                           # 22
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
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 20,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10110 ._CH',             # 00
        'ED6_DT09/CH10111 ._CH',             # 01
        'ED6_DT09/CH10270 ._CH',             # 02
        'ED6_DT09/CH10271 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT09/CH10110P._CP',             # 00
        'ED6_DT09/CH10111P._CP',             # 01
        'ED6_DT09/CH10270P._CP',             # 02
        'ED6_DT09/CH10271P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x141,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -17000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x141,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -20000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x141,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -24000,
        Z                   = 460,
        Y                   = 37000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x141,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -28000,
        Z                   = 0,
        Y                   = 55800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x141,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 11000,
        Z                   = 0,
        Y                   = 0,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1000,
        Z                   = 0,
        Y                   = 14000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20000,
        Z                   = 0,
        Y                   = 16000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4000,
        Z                   = 0,
        Y                   = 30000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20000,
        Z                   = 0,
        Y                   = 51000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24000,
        Z                   = 460,
        Y                   = 37000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28000,
        Z                   = 0,
        Y                   = 55800,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x30,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19000,
        Z                   = 0,
        Y                   = 29000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 2000,
        Y                   = 0,
        Z                   = 10000,
        Range               = 3000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -17000,
        Y                   = 0,
        Z                   = 14000,
        Range               = 3000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -20000,
        Y                   = 0,
        Z                   = 28000,
        Range               = 3000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -24000,
        Y                   = 0,
        Z                   = 37000,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = -28000,
        Y                   = 0,
        Z                   = 55800,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = 6170,
        Y                   = -1000,
        Z                   = 2310,
        Range               = 8320,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0xFFFFF5B0,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 4180,
        Y                   = -1000,
        Z                   = 1490,
        Range               = -1300,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x127A,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )


    DeclActor(
        TriggerX            = 3200,
        TriggerZ            = 0,
        TriggerY            = -17000,
        TriggerRange        = 800,
        ActorX              = 3200,
        ActorZ              = 1000,
        ActorY              = -17000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28000,
        TriggerZ            = 0,
        TriggerY            = 57000,
        TriggerRange        = 800,
        ActorX              = -28000,
        ActorZ              = 1000,
        ActorY              = 57000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1500,
        TriggerZ            = 0,
        TriggerY            = 30000,
        TriggerRange        = 800,
        ActorX              = -1500,
        ActorZ              = 1000,
        ActorY              = 30000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19960,
        TriggerZ            = 0,
        TriggerY            = 53960,
        TriggerRange        = 800,
        ActorX              = -19960,
        ActorZ              = 1000,
        ActorY              = 53960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19960,
        TriggerZ            = 0,
        TriggerY            = 53960,
        TriggerRange        = 800,
        ActorX              = -19960,
        ActorZ              = 1000,
        ActorY              = 53960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19960,
        TriggerZ            = 0,
        TriggerY            = 51810,
        TriggerRange        = 800,
        ActorX              = -19960,
        ActorZ              = 0,
        ActorY              = 51810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15800,
        TriggerZ            = 0,
        TriggerY            = -160,
        TriggerRange        = 1000,
        ActorX              = 15800,
        ActorZ              = 1000,
        ActorY              = -160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_446",          # 00, 0
        "Function_1_47C",          # 01, 1
        "Function_2_71E",          # 02, 2
        "Function_3_734",          # 03, 3
        "Function_4_793",          # 04, 4
        "Function_5_899",          # 05, 5
        "Function_6_AF6",          # 06, 6
        "Function_7_F7F",          # 07, 7
        "Function_8_1162",         # 08, 8
        "Function_9_1482",         # 09, 9
        "Function_10_17B2",        # 0A, 10
        "Function_11_1DE9",        # 0B, 11
        "Function_12_2060",        # 0C, 12
        "Function_13_2347",        # 0D, 13
        "Function_14_258F",        # 0E, 14
        "Function_15_26EF",        # 0F, 15
        "Function_16_292B",        # 10, 16
    )


    def Function_0_446(): pass

    label("Function_0_446")

    SetChrPos(0x101, 1370, 0, -15162, 0)
    SetChrPos(0x102, 1370, 0, -15162, 0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_END)), "loc_47B")
    SetChrFlags(0x14, 0x80)

    label("loc_47B")

    Return()

    # Function_0_446 end

    def Function_1_47C(): pass

    label("Function_1_47C")

    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_4A4")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_625")

    label("loc_4A4")

    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_505")
    Call(0, 16)
    SetChrPos(0x0, 2000, 0, 7000, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_505")
    OP_A2(0x5)

    label("loc_505")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53E")
    Call(0, 16)
    SetChrPos(0x0, -13680, 0, 14260, 270)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53E")
    OP_A2(0x6)

    label("loc_53E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577")
    Call(0, 16)
    SetChrPos(0x0, -19860, 0, 24930, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_577")
    OP_A2(0x7)

    label("loc_577")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B0")
    Call(0, 16)
    SetChrPos(0x0, -21300, 150, 37200, 270)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B0")
    OP_A2(0x8)

    label("loc_5B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E9")
    Call(0, 16)
    SetChrPos(0x0, -27900, 0, 53010, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E9")
    OP_A2(0x9)

    label("loc_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5F5")
    SetChrFlags(0x9, 0x80)

    label("loc_5F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_601")
    SetChrFlags(0xA, 0x80)

    label("loc_601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_60D")
    SetChrFlags(0xB, 0x80)

    label("loc_60D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_619")
    SetChrFlags(0xC, 0x80)

    label("loc_619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_625")
    SetChrFlags(0xD, 0x80)

    label("loc_625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_637")
    OP_6F(0x1, 0)
    Jump("loc_63E")

    label("loc_637")

    OP_6F(0x1, 60)

    label("loc_63E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_650")
    OP_6F(0x2, 0)
    Jump("loc_657")

    label("loc_650")

    OP_6F(0x2, 60)

    label("loc_657")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x20)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x8000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_67A")
    OP_64(0x5, 0x1)
    Jump("loc_6C3")

    label("loc_67A")

    LoadEffect(0x6, "map\\\\evsepith.eff")
    PlayEffect(0x6, 0x6, 0xFF, -19960, 200, 51810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_6C3")

    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    OP_22(0x1CD, 0x1, 0x64)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 15800, 1000, -160, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_47C end

    def Function_2_71E(): pass

    label("Function_2_71E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_733")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_71E")

    label("loc_733")

    Return()

    # Function_2_71E end

    def Function_3_734(): pass

    label("Function_3_734")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "铁门已经生锈得不能再打开了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_734 end

    def Function_4_793(): pass

    label("Function_4_793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_7A6")
    NewScene("ED6_DT01/T0100   ._SN", 1, 0, 0)
    IdleLoop()
    Jump("loc_898")

    label("loc_7A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_878")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_822")

    ChrTalk(
        0x102,
        (
            "#012F艾丝蒂尔，等等。\x02\x03",
            "#012F我们还没有回收搜索对象啊。\x02",
        )
    )

    Jump("loc_871")

    label("loc_822")


    ChrTalk(
        0x102,
        (
            "#012F在回到地上之前一定要把\x01",
            "搜索对象回收了才算是完成任务。\x02",
        )
    )


    label("loc_871")

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_898")

    label("loc_878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88F")
    OP_A2(0x22F)
    NewScene("ED6_DT01/T0100   ._SN", 2, 0, 0)
    IdleLoop()
    Jump("loc_898")

    label("loc_88F")

    NewScene("ED6_DT01/T0100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_898")

    Return()

    # Function_4_793 end

    def Function_5_899(): pass

    label("Function_5_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_8A1")
    Return()

    label("loc_8A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8A9")
    Return()

    label("loc_8A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8B5")
    EventBegin(0x1)
    Jump("loc_AB2")

    label("loc_8B5")

    EventBegin(0x0)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)

    def lambda_8CB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8CB)

    def lambda_8D9():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D9)
    OP_69(0x9, 0x3E8)
    Sleep(400)

    ChrTalk(
        0x101,
        "#002F……出现了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F艾丝蒂尔，\x01",
            "小心别让它绕到自己背后。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F知道啦！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※魔兽的样子是无法从远处看到的。\x01",
            "  在接近到一定距离后才能看清它们。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※根据接触方式不同，战斗开始时的状况也会不同。\x01",
            "  接触魔兽背后有利战斗，\x01",
            "  被魔兽从背后接触则不利战斗。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x0)

    label("loc_AB2")


    def lambda_AB8():
        OP_92(0x0, 0x9, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_AB8)

    def lambda_ACD():
        OP_92(0x1, 0x9, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_ACD)
    Sleep(200)
    Battle(0x11, 0x10000B, 0x0, 0x0, 0x9)
    EventEnd(0x2)
    SetMapFlags(0x1)
    Return()

    # Function_5_899 end

    def Function_6_AF6(): pass

    label("Function_6_AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_AFE")
    Return()

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_B06")
    Return()

    label("loc_B06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x1E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x1E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x32)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x32)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x41)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x41)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF2")
    EventBegin(0x0)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)

    def lambda_B65():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B65)

    def lambda_B73():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B73)
    OP_69(0xA, 0x3E8)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB6")

    ChrTalk(
        0x101,
        "#002F又出现了。\x02",
    )

    CloseMessageWindow()

    label("loc_BB6")


    ChrTalk(
        0x102,
        (
            "#012F这类敌人比较特殊，\x01",
            "有时候武器对他们也不管用。\x02\x03",
            "#012F如果普通攻击不起作用的话，\x01",
            "就用魔法来攻击他们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯，知道啦！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※结晶回路的安装在[Orbment]界面进行。\x01",
            "  要开启[Orbment]界面\x01",
            "  只需在Camp中点击[Orbment]即可。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    EventEnd(0x0)
    OP_A2(0xA)
    Return()

    label("loc_CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_CFE")
    EventBegin(0x2)
    Jump("loc_F3B")

    label("loc_CFE")

    EventBegin(0x0)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)

    def lambda_D14():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D14)

    def lambda_D22():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D22)
    OP_69(0xA, 0x3E8)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5D")

    ChrTalk(
        0x101,
        "#002F又出现了。\x02",
    )

    CloseMessageWindow()

    label("loc_D5D")


    ChrTalk(
        0x102,
        (
            "#012F这类敌人比较特殊，\x01",
            "有时候武器对他们也不管用。\x02\x03",
            "#012F不光要用普通攻击来对付它们，\x01",
            "还要用魔法才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F好！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※在普通攻击很难对敌人起效的情况下，魔法就很有效。\x01",
            "魔法还可以远距离攻击，\x01",
            "但发动魔法需要耗费一定时间（驱动时间）。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※使用魔法会消耗ＥＰ。\x01",
            "  ＥＰ可以通过在酒店、旅馆等回复点休息，\x01",
            "  或使用ＥＰ填充剂等回复物品来进行回复。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x1)
    OP_A2(0xA)

    label("loc_F3B")


    def lambda_F41():
        OP_92(0x0, 0xA, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F41)

    def lambda_F56():
        OP_92(0x1, 0xA, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_F56)
    Sleep(200)
    Battle(0x12, 0x10000B, 0x0, 0x0, 0xA)
    EventEnd(0x2)
    SetMapFlags(0x1)
    Return()

    # Function_6_AF6 end

    def Function_7_F7F(): pass

    label("Function_7_F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_F87")
    Return()

    label("loc_F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_F8F")
    Return()

    label("loc_F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F9B")
    EventBegin(0x2)
    Jump("loc_111E")

    label("loc_F9B")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)

    def lambda_FB6():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FB6)

    def lambda_FC4():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FC4)
    OP_69(0xB, 0x3E8)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#012F艾丝蒂尔，\x01",
            "这次我们来使用战技吧。\x02\x03",
            "战技除了攻击之外，\x01",
            "还会有其他很多效果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F嗯，明白！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※战技虽有范围限制，但可以即时发动。\x01",
            "  使用战技所必需的ＣＰ会在\x01",
            "  攻击敌人或被敌人攻击的时候自动积蓄起来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2)

    label("loc_111E")


    def lambda_1124():
        OP_92(0x101, 0xB, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1124)

    def lambda_1139():
        OP_92(0x102, 0xB, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1139)
    Sleep(200)
    Battle(0x13, 0x10000B, 0x0, 0x0, 0xB)
    EventEnd(0x2)
    SetMapFlags(0x1)
    Return()

    # Function_7_F7F end

    def Function_8_1162(): pass

    label("Function_8_1162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_116A")
    Return()

    label("loc_116A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1172")
    Return()

    label("loc_1172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_117E")
    EventBegin(0x2)
    Jump("loc_143E")

    label("loc_117E")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)

    def lambda_1199():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1199)

    def lambda_11A7():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11A7)
    OP_69(0xC, 0x3E8)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#509F好讨厌～\x01",
            "怎么还有啊。\x02\x03",
            "#509F真麻烦～\x01",
            "快点把它们解决掉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F如果使用Ｓ战技或Ｓ爆发技，\x01",
            "我想只需一击就能打倒这些魔兽。\x02\x03",
            "#012F不过，要注意的是一定要在\x01",
            "ＣＰ值为１００以上的时候才能使用。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ＣＰ超过１００后，\x01",
            "  就能使用攻击力强劲的战技，\x01",
            "  分别是Ｓ战技以及最强的Ｓ爆发技。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※Ｓ爆发技即无视ＡＴ（行动顺序）而直接发动Ｓ战技。\x01",
            "  作为Ｓ爆发技发动的Ｓ战技，\x01",
            "  可以在Camp的[Tactics]-[Ｓ爆发技登记]中变更。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x3)

    label("loc_143E")


    def lambda_1444():
        OP_92(0x0, 0xC, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1444)

    def lambda_1459():
        OP_92(0x1, 0xC, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1459)
    Sleep(200)
    Battle(0x10, 0x10000B, 0x0, 0x0, 0xC)
    EventEnd(0x2)
    SetMapFlags(0x1)
    Return()

    # Function_8_1162 end

    def Function_9_1482(): pass

    label("Function_9_1482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_148A")
    Return()

    label("loc_148A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1492")
    Return()

    label("loc_1492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_149E")
    EventBegin(0x2)
    Jump("loc_176E")

    label("loc_149E")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)

    def lambda_14B9():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14B9)

    def lambda_14C7():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14C7)
    OP_6D(-28300, 0, 54500, 1000)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#000F那就是目标宝箱啊。\x02\x03",
            "#000F如果研修就到此为止的话，\x01",
            "那也太轻松太简单了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F看来已经开始得心应手了。\x02\x03",
            "#010F那么这次注意一下\x01",
            "战斗行动顺序的应用吧。\x02\x03",
            "#010F掌握好的话\x01",
            "会有各种各样的好处哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※战斗中，随着ＡＴ（行动顺序）的不同，\x01",
            "  角色有机会得到『攻击力上升』、『得到耀晶片』等各种ＡＴ奖励。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※这些ＡＴ奖励对敌我双方都发挥同样的效果。\x01",
            "  熟练错开行动顺序的话，\x01",
            "  更可以强行夺取敌人的ＡＴ奖励为己用。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x4)

    label("loc_176E")


    def lambda_1774():
        OP_92(0x0, 0xD, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1774)

    def lambda_1789():
        OP_92(0x1, 0xD, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1789)
    Sleep(200)
    Battle(0xF, 0x10000B, 0x0, 0x0, 0xD)
    EventEnd(0x2)
    SetMapFlags(0x1)
    Return()

    # Function_9_1482 end

    def Function_10_17B2(): pass

    label("Function_10_17B2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7F")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)
    OP_8B(0x0, 0xFFFF92A0, 0xDEA8, 0x0)
    OP_8B(0x1, 0xFFFF92A0, 0xDEA8, 0x0)
    OP_51(0x8, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x8, 0x5DC)
    OP_28(0xA, 0x1, 0x2)
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了２个\x07\x02",
            "小箱子\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x373, 2)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x101,
        (
            "#505F咦～奇怪了，\x01",
            "怎么宝箱里还是箱子啊。\x02\x03",
            "#501F奇怪的是有两个箱子呢。\x01",
            "嗯～到底里面放了些什么东西呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔，\x01",
            "这次的任务是搜索和回收哦。\x02\x03",
            "#014F我想这其中应该不包括调查吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F哎呀～\x01",
            "约修亚你真是死脑筋。\x02\x03",
            "#502F这又不是工作的问题，\x01",
            "只不过是纯粹的好奇心嘛。\x02\x03",
            "#502F……………………\x02\x03",
            "#006F……我说，既然这里没有人，\x01",
            "稍微打开看一下也不会露馅吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……………………\x02\x03",
            "#015F要是你想考试不合格的话，\x01",
            "那我也不阻止你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F不、不合格？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F有这种可能性啊。\x02\x03",
            "#010F如果这是真正的工作，\x01",
            "那这箱子就是委托人的物品。\x02\x03",
            "#010F如果不是非法物品，\x01",
            "我们就无权调查里面的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F啊，这样说也有道理……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F既然你这么在意，\x01",
            "就等考试结束后去问一下雪拉姐姐吧。\x02\x03",
            "#010F……好了，就这样决定吧。\x01",
            "回去的路上也要小心谨慎一点哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FＯＫ！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x28A)
    Sleep(30)
    EventEnd(0x0)
    Jump("loc_1DE3")

    label("loc_1D7F")

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
    TalkEnd(0xFF)
    Sleep(30)

    label("loc_1DE3")

    ClearMapFlags(0x8000000)
    Return()

    # Function_10_17B2 end

    def Function_11_1DE9(): pass

    label("Function_11_1DE9")

    SetMapFlags(0x8000000)
    EventBegin(0x0)
    OP_82(0x6, 0x0)
    OP_84(0x6)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "结晶回路的碎片\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(400)
    OP_3E(0x325, 1)
    OP_64(0x5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2052")

    ChrTalk(
        0x101,
        (
            "#000F哦～原来是这个啊。\x02\x03",
            "从排水沟那里看到的光\x01",
            "好像就是这东西发出来的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F好像是。\x02\x03",
            "原来是结晶回路的碎片啊……\x01",
            "怪不得会发光呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F真是好美的光啊。\x02\x03",
            "这也是用七耀石制成的东西吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F虽然这种说法比较粗略，\x01",
            "不过也没说错……\x02\x03",
            "详细的说明\x01",
            "回去再慢慢告诉你吧。\x02\x03",
            "一直站在这里说话，\x01",
            "感觉可不太舒服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F嗯，对啊。\x02\x03",
            "这里的确是挺阴森森的，\x01",
            "我们快点回去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4, 0x1, 0x20)
    Jump("loc_2058")

    label("loc_2052")

    OP_28(0x4, 0x1, 0x8000)

    label("loc_2058")

    EventEnd(0x0)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1DE9 end

    def Function_12_2060(): pass

    label("Function_12_2060")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_206F")
    Return()

    label("loc_206F")

    EventBegin(0x0)
    OP_28(0xA, 0x1, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2126")
    TurnDirection(0x102, 0x101, 0)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#010F那边好像有一个\x01",
            "专门用来休息的回复点。\x02\x03",
            "如果ＨＰ和ＥＰ降低了，就到那儿休息吧。\x01",
            "特别是在战斗之前。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21B6")

    label("loc_2126")

    TurnDirection(0x102, 0x101, 0)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，等一下。\x02\x03",
            "那边有一个回复点，\x01",
            "如果ＨＰ和ＥＰ降低了，就到那儿休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B6")

    Sleep(100)

    def lambda_21C1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_21C1)

    def lambda_21CF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_21CF)
    OP_6D(13300, 0, -130, 1500)
    TurnDirection(0x102, 0x101, 0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※回复点是一种\x01",
            "  配置在危险地域中的导力回复装置。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※靠近回复点会出现『！』的标记，\x01",
            "  用右键点击会出现选择菜单。\x01",
            "  选择『休息』即可让全员的ＨＰ、ＥＰ完全回复。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(100)
    OP_69(0x0, 0x5DC)

    ChrTalk(
        0x101,
        "#000F嗯，明白！\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_12_2060 end

    def Function_13_2347(): pass

    label("Function_13_2347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2356")
    Return()

    label("loc_2356")

    EventBegin(0x0)
    OP_28(0xA, 0x1, 0x8000)
    OP_8C(0x102, 90, 0)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#010F那边好像有一个\x01",
            "专门用来休息的回复点。\x02\x03",
            "如果ＨＰ和ＥＰ降低了，就到那儿休息吧。\x01",
            "特别是在战斗之前。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_2409():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2409)

    def lambda_2417():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2417)
    OP_6D(13300, 0, -130, 1500)
    TurnDirection(0x102, 0x101, 0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※回复点是一种\x01",
            "  配置在危险地域中的导力回复装置。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※靠近回复点会出现『！』的标记，\x01",
            "  用右键点击会出现选择菜单。\x01",
            "  选择『休息』即可让全员的ＨＰ、ＥＰ完全回复。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(100)
    OP_69(0x0, 0x5DC)

    ChrTalk(
        0x101,
        "#000F嗯，明白！\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_13_2347 end

    def Function_14_258F(): pass

    label("Function_14_258F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_2609")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "复苏药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28B)
    Jump("loc_2687")

    label("loc_2609")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "复苏药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "复苏药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_2687")

    Jump("loc_26E1")

    label("loc_268A")

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
    OP_83(0xF, 0x8)

    label("loc_26E1")

    TalkEnd(0xFF)
    Sleep(30)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_258F end

    def Function_15_26EF(): pass

    label("Function_15_26EF")

    OP_28(0xA, 0x1, 0x8000)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在此休息\x01",      # 0
            "离开\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2910")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 15800, 1000, -160, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x32)
    OP_73(0x3)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 15800, 1000, -160, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, 14290, 0, -230, 92)
    SetChrPos(0x1, 14290, 0, -230, 92)
    SetChrPos(0x2, 14290, 0, -230, 92)
    SetChrPos(0x3, 14290, 0, -230, 92)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 15800, 1000, -160, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2910")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_292A")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_292A")

    Return()

    # Function_15_26EF end

    def Function_16_292B(): pass

    label("Function_16_292B")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    Return()

    # Function_16_292B end

    SaveToFile()

Try(main)
