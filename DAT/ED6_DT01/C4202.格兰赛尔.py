from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4202   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4202.x',
        MapIndex            = 1,
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
        'ED6_DT09/CH10490 ._CH',             # 00
        'ED6_DT09/CH10491 ._CH',             # 01
        'ED6_DT09/CH10500 ._CH',             # 02
        'ED6_DT09/CH10501 ._CH',             # 03
        'ED6_DT09/CH10510 ._CH',             # 04
        'ED6_DT09/CH10511 ._CH',             # 05
        'ED6_DT09/CH11110 ._CH',             # 06
        'ED6_DT09/CH11111 ._CH',             # 07
        'ED6_DT09/CH11120 ._CH',             # 08
        'ED6_DT09/CH11121 ._CH',             # 09
        'ED6_DT09/CH11130 ._CH',             # 0A
        'ED6_DT09/CH11131 ._CH',             # 0B
        'ED6_DT09/CH11140 ._CH',             # 0C
        'ED6_DT09/CH11141 ._CH',             # 0D
        'ED6_DT09/CH11150 ._CH',             # 0E
        'ED6_DT09/CH11151 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10490P._CP',             # 00
        'ED6_DT09/CH10491P._CP',             # 01
        'ED6_DT09/CH10500P._CP',             # 02
        'ED6_DT09/CH10501P._CP',             # 03
        'ED6_DT09/CH10510P._CP',             # 04
        'ED6_DT09/CH10511P._CP',             # 05
        'ED6_DT09/CH11110P._CP',             # 06
        'ED6_DT09/CH11111P._CP',             # 07
        'ED6_DT09/CH11120P._CP',             # 08
        'ED6_DT09/CH11121P._CP',             # 09
        'ED6_DT09/CH11130P._CP',             # 0A
        'ED6_DT09/CH11131P._CP',             # 0B
        'ED6_DT09/CH11140P._CP',             # 0C
        'ED6_DT09/CH11141P._CP',             # 0D
        'ED6_DT09/CH11150P._CP',             # 0E
        'ED6_DT09/CH11151P._CP',             # 0F
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 13590,
        Z                   = 0,
        Y                   = 67390,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x272,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13650,
        Z                   = 0,
        Y                   = 73480,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x272,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13600,
        Z                   = 0,
        Y                   = 79600,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x272,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13660,
        Z                   = 0,
        Y                   = 83670,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x272,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13620,
        Z                   = 0,
        Y                   = 90730,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x272,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 60960,
        Z                   = 0,
        Y                   = 94820,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x272,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 100830,
        Z                   = 0,
        Y                   = 20580,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x272,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 38210,
        Z                   = 0,
        Y                   = -520,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x27F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15760,
        Z                   = 0,
        Y                   = -10320,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x27F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34200,
        Z                   = 0,
        Y                   = 7700,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x27F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 30560,
        Z                   = 0,
        Y                   = -65610,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x27F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 43930,
        TriggerZ            = 0,
        TriggerY            = -6210,
        TriggerRange        = 1000,
        ActorX              = 43860,
        ActorZ              = 1500,
        ActorY              = -5600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41920,
        TriggerZ            = 450,
        TriggerY            = 124030,
        TriggerRange        = 1000,
        ActorX              = 41950,
        ActorZ              = 1950,
        ActorY              = 123110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29340,
        TriggerZ            = 0,
        TriggerY            = 130710,
        TriggerRange        = 1000,
        ActorX              = 28570,
        ActorZ              = 1500,
        ActorY              = 130759,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_30A",          # 00, 0
        "Function_1_32D",          # 01, 1
        "Function_2_37E",          # 02, 2
        "Function_3_44C",          # 03, 3
        "Function_4_754",          # 04, 4
        "Function_5_96B",          # 05, 5
        "Function_6_B71",          # 06, 6
    )


    def Function_0_30A(): pass

    label("Function_0_30A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_316"),
        (SWITCH_DEFAULT, "loc_32C"),
    )


    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_329")
    OP_A2(0x65C)
    Event(0, 3)

    label("loc_329")

    Jump("loc_32C")

    label("loc_32C")

    Return()

    # Function_0_30A end

    def Function_1_32D(): pass

    label("Function_1_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F")
    OP_6F(0x0, 0)
    Jump("loc_346")

    label("loc_33F")

    OP_6F(0x0, 60)

    label("loc_346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358")
    OP_6F(0x1, 0)
    Jump("loc_35F")

    label("loc_358")

    OP_6F(0x1, 60)

    label("loc_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_371")
    OP_6F(0x2, 0)
    Jump("loc_378")

    label("loc_371")

    OP_6F(0x2, 60)

    label("loc_378")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_32D end

    def Function_2_37E(): pass

    label("Function_2_37E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A3")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_436")

    label("loc_3A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BC")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_436")

    label("loc_3BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D5")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_436")

    label("loc_3D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EE")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_436")

    label("loc_3EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_407")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_436")

    label("loc_407")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_420")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_436")

    label("loc_420")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_436")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_436")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_436")

    label("loc_44B")

    Return()

    # Function_2_37E end

    def Function_3_44C(): pass

    label("Function_3_44C")

    EventBegin(0x0)
    OP_6D(100690, 250, 128360, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x104, 100890, 2000, 130110, 180)
    SetChrPos(0x108, 101450, 2000, 131240, 180)
    SetChrPos(0x102, 100530, 2000, 131390, 180)

    def lambda_4C4():

        label("loc_4C4")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_4C4")

    QueueWorkItem2(0x108, 1, lambda_4C4)

    def lambda_4D5():

        label("loc_4D5")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_4D5")

    QueueWorkItem2(0x102, 1, lambda_4D5)

    def lambda_4E6():
        OP_8E(0xFE, 0x189FC, 0x0, 0x1F2C0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4E6)

    def lambda_501():
        OP_8E(0xFE, 0x188F8, 0x0, 0x1F2E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_501)

    def lambda_51C():
        OP_8E(0xFE, 0x18BAA, 0x0, 0x1EE38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_51C)
    WaitChrThread(0x104, 0x1)

    def lambda_53C():
        OP_8E(0xFE, 0x18218, 0x0, 0x1F05E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_53C)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 90, 400)
    WaitChrThread(0x108, 0x2)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x104,
        (
            "#030F那么……\x02\x03",
            "呵呵，我们这就确认一下\x01",
            "之前提到的隐藏水路的路线图吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#5P没错……\x01",
            "不过先等一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x40026, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(50, 0, -1, -1)
    SetChrName("金")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#070F现在我们所处的位置\x01",
            "在右下角楼梯标志的地方……\x02\x03",
            "图中央标有『＝』的地方\x01",
            "就是隐藏水路的入口。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 0, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#012F对……\x02\x03",
            "首先就到那里去，\x01",
            "然后调查一下附近的墙壁吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)
    OP_28(0x4D, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_3_44C end

    def Function_4_754(): pass

    label("Function_4_754")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_836")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 43860, 3000, -5600, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_7A3():
        OP_8F(0xFE, 0xAB54, 0x5DC, 0xFFFFEA20, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7A3)

    def lambda_7BE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7BE)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x279, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_811"),
        (2, "loc_823"),
        (1, "loc_833"),
        (SWITCH_DEFAULT, "loc_836"),
    )


    label("loc_811")

    OP_A2(0x6D9)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_836")

    label("loc_823")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_833")

    OP_B4(0x0)
    Return()

    label("loc_836")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x5D, 1)"), scpexpr(EXPR_END)), "loc_88A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "鹰眼枪\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6D8)
    Jump("loc_8FA")

    label("loc_88A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "鹰眼枪\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "鹰眼枪\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_8FA")

    Jump("loc_95D")

    label("loc_8FD")

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
    OP_83(0xF, 0x47)

    label("loc_95D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_754 end

    def Function_5_96B(): pass

    label("Function_5_96B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B35")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4D")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 41950, 3450, 123110, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_9BA():
        OP_8F(0xFE, 0xA3DE, 0x79E, 0x1E0E6, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9BA)

    def lambda_9D5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9D5)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x279, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_A28"),
        (2, "loc_A3A"),
        (1, "loc_A4A"),
        (SWITCH_DEFAULT, "loc_A4D"),
    )


    label("loc_A28")

    OP_A2(0x6DB)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_A4D")

    label("loc_A3A")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_A4A")

    OP_B4(0x0)
    Return()

    label("loc_A4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x146, 1)"), scpexpr(EXPR_END)), "loc_AAC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "斗魂扎头巾\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6DA)
    Jump("loc_B32")

    label("loc_AAC")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "斗魂扎头巾\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "斗魂扎头巾\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_B32")

    Jump("loc_B63")

    label("loc_B35")

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
    OP_83(0xF, 0x48)

    label("loc_B63")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_96B end

    def Function_6_B71(): pass

    label("Function_6_B71")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C63")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_BE8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "大回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6DC)
    Jump("loc_C60")

    label("loc_BE8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "大回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "大回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_C60")

    Jump("loc_CA6")

    label("loc_C63")

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
    OP_83(0xF, 0x49)

    label("loc_CA6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_B71 end

    SaveToFile()

Try(main)
