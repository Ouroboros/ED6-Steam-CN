from ED6ScenarioHelper import *

def main():
    # 东柏斯街道

    CreateScenaFile(
        FileName            = 'R1100   ._SN',
        MapName             = 'Bose',
        Location            = 'R1100.x',
        MapIndex            = 55,
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
    )

    DeclEntryPoint(
        Unknown_00              = 195000,
        Unknown_04              = 0,
        Unknown_08              = -32000,
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
        Unknown_30              = 324,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 55,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10290 ._CH',             # 00
        'ED6_DT09/CH10291 ._CH',             # 01
        'ED6_DT09/CH10320 ._CH',             # 02
        'ED6_DT09/CH10321 ._CH',             # 03
        'ED6_DT09/CH10350 ._CH',             # 04
        'ED6_DT09/CH10351 ._CH',             # 05
        'ED6_DT09/CH10870 ._CH',             # 06
        'ED6_DT09/CH10871 ._CH',             # 07
        'ED6_DT09/CH10880 ._CH',             # 08
        'ED6_DT09/CH10881 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10290P._CP',             # 00
        'ED6_DT09/CH10291P._CP',             # 01
        'ED6_DT09/CH10320P._CP',             # 02
        'ED6_DT09/CH10321P._CP',             # 03
        'ED6_DT09/CH10350P._CP',             # 04
        'ED6_DT09/CH10351P._CP',             # 05
        'ED6_DT09/CH10870P._CP',             # 06
        'ED6_DT09/CH10871P._CP',             # 07
        'ED6_DT09/CH10880P._CP',             # 08
        'ED6_DT09/CH10881P._CP',             # 09
    )

    DeclNpc(
        X                   = 117010,
        Z                   = 20,
        Y                   = -1210,
        Direction           = 348,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 212420,
        Z                   = 0,
        Y                   = -31840,
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
        X                   = 46200,
        Z                   = 0,
        Y                   = -11050,
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
        X                   = 104100,
        Z                   = -100,
        Y                   = 66730,
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
        X                   = 154130,
        Z                   = 30,
        Y                   = -20040,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 138560,
        Z                   = 0,
        Y                   = -700,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 127250,
        Z                   = 50,
        Y                   = 16710,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 81200,
        Z                   = 0,
        Y                   = 10930,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 80560,
        Z                   = 0,
        Y                   = -8189,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 117010,
        Y                   = -500,
        Z                   = -1210,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 101320,
        TriggerZ            = 0,
        TriggerY            = 18640,
        TriggerRange        = 1500,
        ActorX              = 101320,
        ActorZ              = 1300,
        ActorY              = 18640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24A",          # 00, 0
        "Function_1_269",          # 01, 1
        "Function_2_2AA",          # 02, 2
        "Function_3_2C0",          # 03, 3
        "Function_4_588",          # 04, 4
    )


    def Function_0_24A(): pass

    label("Function_0_24A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_256"),
        (SWITCH_DEFAULT, "loc_268"),
    )


    label("loc_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_265")
    OP_A2(0x36C)

    label("loc_265")

    Jump("loc_268")

    label("loc_268")

    Return()

    # Function_0_24A end

    def Function_1_269(): pass

    label("Function_1_269")

    OP_16(0x2, 0xFA0, 0x0, 0xFFFE1F88, 0x30015)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A9")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_2A9")

    Return()

    # Function_1_269 end

    def Function_2_2AA(): pass

    label("Function_2_2AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2AA")

    label("loc_2BF")

    Return()

    # Function_2_2AA end

    def Function_3_2C0(): pass

    label("Function_3_2C0")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡中。\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3B8"),
        (SWITCH_DEFAULT, "loc_452"),
    )


    label("loc_3B8")

    Fade(1000)
    SetChrPos(0x0, 116530, 0, 4520, 163)
    SetChrPos(0x1, 116530, 0, 4520, 163)
    SetChrPos(0x2, 116530, 0, 4520, 163)
    SetChrPos(0x3, 116530, 0, 4520, 163)
    SetChrPos(0x4, 116530, 0, 4520, 163)
    SetChrPos(0x5, 116530, 0, 4520, 163)
    SetChrPos(0x6, 116530, 0, 4520, 163)
    SetChrPos(0x7, 116530, 0, 4520, 163)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_452")

    Battle(0x3F7, 0x0, 0x0, 0x0, 0xFF)
    SetChrPos(0x0, 116530, 0, 4520, 163)
    SetChrPos(0x1, 116530, 0, 4520, 163)
    SetChrPos(0x2, 116530, 0, 4520, 163)
    SetChrPos(0x3, 116530, 0, 4520, 163)
    SetChrPos(0x4, 116530, 0, 4520, 163)
    SetChrPos(0x5, 116530, 0, 4520, 163)
    SetChrPos(0x6, 116530, 0, 4520, 163)
    SetChrPos(0x7, 116530, 0, 4520, 163)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_500"),
        (1, "loc_503"),
        (SWITCH_DEFAULT, "loc_506"),
    )


    label("loc_500")

    EventEnd(0x0)
    Return()

    label("loc_503")

    OP_B4(0x0)
    Return()

    label("loc_506")

    EventBegin(0x1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "成功消灭了东柏斯街道中被通缉的魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x15, 0x4, 0x10)
    OP_28(0x15, 0x1, 0x1)
    OP_A2(0x385)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_2C0 end

    def Function_4_588(): pass

    label("Function_4_588")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　迷雾峡谷\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_588 end

    SaveToFile()

Try(main)
