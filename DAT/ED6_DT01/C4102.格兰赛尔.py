from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4102   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        '艾尔贝离宫方向',                       # 9
        '庭园大道方向',                         # 10
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
        'ED6_DT09/CH10780 ._CH',             # 00
        'ED6_DT09/CH10781 ._CH',             # 01
        'ED6_DT09/CH10790 ._CH',             # 02
        'ED6_DT09/CH10791 ._CH',             # 03
        'ED6_DT09/CH10050 ._CH',             # 04
        'ED6_DT09/CH10051 ._CH',             # 05
        'ED6_DT09/CH10800 ._CH',             # 06
        'ED6_DT09/CH10801 ._CH',             # 07
        'ED6_DT09/CH10810 ._CH',             # 08
        'ED6_DT09/CH10811 ._CH',             # 09
        'ED6_DT09/CH10820 ._CH',             # 0A
        'ED6_DT09/CH10821 ._CH',             # 0B
        'ED6_DT09/CH11220 ._CH',             # 0C
        'ED6_DT09/CH11221 ._CH',             # 0D
        'ED6_DT09/CH11230 ._CH',             # 0E
        'ED6_DT09/CH11231 ._CH',             # 0F
        'ED6_DT09/CH11240 ._CH',             # 10
        'ED6_DT09/CH11241 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT09/CH10780P._CP',             # 00
        'ED6_DT09/CH10781P._CP',             # 01
        'ED6_DT09/CH10790P._CP',             # 02
        'ED6_DT09/CH10791P._CP',             # 03
        'ED6_DT09/CH10050P._CP',             # 04
        'ED6_DT09/CH10051P._CP',             # 05
        'ED6_DT09/CH10800P._CP',             # 06
        'ED6_DT09/CH10801P._CP',             # 07
        'ED6_DT09/CH10810P._CP',             # 08
        'ED6_DT09/CH10811P._CP',             # 09
        'ED6_DT09/CH10820P._CP',             # 0A
        'ED6_DT09/CH10821P._CP',             # 0B
        'ED6_DT09/CH11220P._CP',             # 0C
        'ED6_DT09/CH11221P._CP',             # 0D
        'ED6_DT09/CH11230P._CP',             # 0E
        'ED6_DT09/CH11231P._CP',             # 0F
        'ED6_DT09/CH11240P._CP',             # 10
        'ED6_DT09/CH11241P._CP',             # 11
    )

    DeclNpc(
        X                   = 77370,
        Z                   = 0,
        Y                   = -15080,
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
        X                   = -79490,
        Z                   = 0,
        Y                   = 4930,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 29090,
        Z                   = 110,
        Y                   = -28620,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x261,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 35270,
        Z                   = 0,
        Y                   = -43590,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34970,
        Z                   = 100,
        Y                   = -63310,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x265,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4820,
        Z                   = 100,
        Y                   = -79050,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5370,
        Z                   = 120,
        Y                   = -58670,
        Unknown_0C          = 0,
        Unknown_0E          = 14,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x268,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12310,
        Z                   = 10,
        Y                   = 7720,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x259,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34490,
        Z                   = 40,
        Y                   = 31600,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21340,
        Z                   = 10,
        Y                   = 64120,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x267,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32640,
        Z                   = 90,
        Y                   = 49450,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -6330,
        Z                   = 140,
        Y                   = 2330,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 14510,
        Z                   = 0,
        Y                   = -15050,
        Unknown_0C          = 0,
        Unknown_0E          = 16,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x5E2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 480,
        TriggerZ            = 0,
        TriggerY            = -67940,
        TriggerRange        = 1000,
        ActorX              = 1140,
        ActorZ              = 0,
        ActorY              = -67940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13310,
        TriggerZ            = -30,
        TriggerY            = 61150,
        TriggerRange        = 1000,
        ActorX              = 12570,
        ActorZ              = -30,
        ActorY              = 61290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7430,
        TriggerZ            = 30,
        TriggerY            = -17940,
        TriggerRange        = 1000,
        ActorX              = 7020,
        ActorZ              = 30,
        ActorY              = -18340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 24020,
        TriggerZ            = 500,
        TriggerY            = 54480,
        TriggerRange        = 1500,
        ActorX              = 24020,
        ActorZ              = 4000,
        ActorY              = 54480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3540,
        TriggerZ            = 500,
        TriggerY            = -67980,
        TriggerRange        = 1500,
        ActorX              = 3540,
        ActorZ              = 4000,
        ActorY              = -67980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_382",          # 00, 0
        "Function_1_3B1",          # 01, 1
        "Function_2_421",          # 02, 2
        "Function_3_437",          # 03, 3
        "Function_4_741",          # 04, 4
        "Function_5_955",          # 05, 5
        "Function_6_B5A",          # 06, 6
        "Function_7_C9A",          # 07, 7
        "Function_8_CEC",          # 08, 8
    )


    def Function_0_382(): pass

    label("Function_0_382")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_38E"),
        (SWITCH_DEFAULT, "loc_3A4"),
    )


    label("loc_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A1")
    OP_A2(0x615)
    Event(0, 3)

    label("loc_3A1")

    Jump("loc_3A4")

    label("loc_3A4")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_382 end

    def Function_1_3B1(): pass

    label("Function_1_3B1")

    OP_16(0x2, 0xFA0, 0xFFFE17B8, 0xFFFDE8D8, 0x30065)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D5")
    OP_6F(0x0, 0)
    Jump("loc_3DC")

    label("loc_3D5")

    OP_6F(0x0, 60)

    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE")
    OP_6F(0x1, 0)
    Jump("loc_3F5")

    label("loc_3EE")

    OP_6F(0x1, 60)

    label("loc_3F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407")
    OP_6F(0x2, 0)
    Jump("loc_40E")

    label("loc_407")

    OP_6F(0x2, 60)

    label("loc_40E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_420")
    SetChrFlags(0x15, 0x80)

    label("loc_420")

    Return()

    # Function_1_3B1 end

    def Function_2_421(): pass

    label("Function_2_421")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_436")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_421")

    label("loc_436")

    Return()

    # Function_2_421 end

    def Function_3_437(): pass

    label("Function_3_437")

    EventBegin(0x0)
    OP_6D(-62530, 0, 5200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -66840, 0, 6300, 270)
    SetChrPos(0x102, -66930, 0, 4930, 270)

    def lambda_49E():
        OP_6D(-60360, 0, 5200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_49E)

    def lambda_4B6():
        OP_8E(0xFE, 0xFFFF1438, 0x0, 0x173E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B6)

    def lambda_4D1():
        OP_8E(0xFE, 0xFFFF13AC, 0x0, 0x1176, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4D1)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#501F这就是艾尔贝周游道啊……\x02\x03",
            "在森林中有用石头铺成的大路，\x01",
            "真是有趣啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F作为王都市民休憩的场所，\x01",
            "好像是很久之前就建造的了。\x02\x03",
            "大概，已经有数百年的历史了吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "不愧是女王的脚下啊。\x02\x03",
            "#505F不过，怎么感觉有魔兽的气息呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F真是敏锐啊。\x02\x03",
            "#012F我也感觉到这里\x01",
            "有比刚才路上更厉害的魔兽呢。\x02\x03",
            "一边保持警惕一边找金先生吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_3_437 end

    def Function_4_741(): pass

    label("Function_4_741")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_823")
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, 1700, 2500, -68060, 320)
    TurnDirection(0xA, 0x0, 0)

    def lambda_790():
        OP_8F(0xFE, 0x6A4, 0x3E8, 0xFFFEF624, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_790)

    def lambda_7AB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7AB)
    ClearChrFlags(0xA, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x26C, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_7FE"),
        (2, "loc_810"),
        (1, "loc_820"),
        (SWITCH_DEFAULT, "loc_823"),
    )


    label("loc_7FE")

    OP_A2(0x685)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_823")

    label("loc_810")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_820")

    OP_B4(0x0)
    Return()

    label("loc_823")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x263, 1)"), scpexpr(EXPR_END)), "loc_879")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "防御３\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x684)
    Jump("loc_8ED")

    label("loc_879")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "防御３\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "防御３\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_8ED")

    Jump("loc_947")

    label("loc_8F0")

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
    OP_83(0xF, 0x3D)

    label("loc_947")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_741 end

    def Function_5_955(): pass

    label("Function_5_955")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B01")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A37")
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, 12570, 2500, 61290, 320)
    TurnDirection(0xA, 0x0, 0)

    def lambda_9A4():
        OP_8F(0xFE, 0x311A, 0x3E8, 0xEF6A, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9A4)

    def lambda_9BF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_9BF)
    ClearChrFlags(0xA, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x26C, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_A12"),
        (2, "loc_A24"),
        (1, "loc_A34"),
        (SWITCH_DEFAULT, "loc_A37"),
    )


    label("loc_A12")

    OP_A2(0x687)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_A37")

    label("loc_A24")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_A34")

    OP_B4(0x0)
    Return()

    label("loc_A37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x269, 1)"), scpexpr(EXPR_END)), "loc_A8C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "魔防３\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x686)
    Jump("loc_AFE")

    label("loc_A8C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "魔防３\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "魔防３\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_AFE")

    Jump("loc_B4C")

    label("loc_B01")

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
    OP_83(0xF, 0x3E)

    label("loc_B4C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_955 end

    def Function_6_B5A(): pass

    label("Function_6_B5A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_BD1")
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
    OP_A2(0x688)
    Jump("loc_C49")

    label("loc_BD1")

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

    label("loc_C49")

    Jump("loc_C8C")

    label("loc_C4C")

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
    OP_83(0xF, 0x3F)

    label("loc_C8C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_B5A end

    def Function_7_C9A(): pass

    label("Function_7_C9A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "竖立着古老的苍耀石石碑。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_C9A end

    def Function_8_CEC(): pass

    label("Function_8_CEC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "竖立着古老的红耀石石碑。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_CEC end

    SaveToFile()

Try(main)
