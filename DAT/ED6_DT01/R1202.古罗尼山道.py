from ED6ScenarioHelper import *

def main():
    # 古罗尼山道

    CreateScenaFile(
        FileName            = 'R1202   ._SN',
        MapName             = 'Bose',
        Location            = 'R1202.x',
        MapIndex            = 61,
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
        Unknown_3A              = 61,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10320 ._CH',             # 00
        'ED6_DT09/CH10321 ._CH',             # 01
        'ED6_DT09/CH10350 ._CH',             # 02
        'ED6_DT09/CH10351 ._CH',             # 03
        'ED6_DT09/CH10310 ._CH',             # 04
        'ED6_DT09/CH10310 ._CH',             # 05
        'ED6_DT09/CH10550 ._CH',             # 06
        'ED6_DT09/CH10550 ._CH',             # 07
        'ED6_DT09/CH10900 ._CH',             # 08
        'ED6_DT09/CH10901 ._CH',             # 09
        'ED6_DT09/CH11240 ._CH',             # 0A
        'ED6_DT09/CH11241 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT09/CH10320P._CP',             # 00
        'ED6_DT09/CH10321P._CP',             # 01
        'ED6_DT09/CH10350P._CP',             # 02
        'ED6_DT09/CH10351P._CP',             # 03
        'ED6_DT09/CH10310P._CP',             # 04
        'ED6_DT09/CH10310P._CP',             # 05
        'ED6_DT09/CH10550P._CP',             # 06
        'ED6_DT09/CH10550P._CP',             # 07
        'ED6_DT09/CH10900P._CP',             # 08
        'ED6_DT09/CH10901P._CP',             # 09
        'ED6_DT09/CH11240P._CP',             # 0A
        'ED6_DT09/CH11241P._CP',             # 0B
    )

    DeclNpc(
        X                   = -448750,
        Z                   = -60,
        Y                   = 50710,
        Direction           = 0,
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
        X                   = -505000,
        Z                   = 10,
        Y                   = 56760,
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
        X                   = -352510,
        Z                   = 0,
        Y                   = 15930,
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
        X                   = -391300,
        Z                   = -10,
        Y                   = 18680,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -416900,
        Z                   = 560,
        Y                   = 32439,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -422220,
        Z                   = 40,
        Y                   = 48020,
        Unknown_0C          = 0,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x5DD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -448750,
        Y                   = -1060,
        Z                   = 50710,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_1EB",          # 01, 1
        "Function_2_23E",          # 02, 2
        "Function_3_254",          # 03, 3
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_1DE end

    def Function_1_1EB(): pass

    label("Function_1_1EB")

    OP_16(0x2, 0xFA0, 0xFFF77480, 0xFFFEA070, 0x3001B)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_22B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23D")
    SetChrFlags(0xD, 0x80)

    label("loc_23D")

    Return()

    # Function_1_1EB end

    def Function_2_23E(): pass

    label("Function_2_23E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_253")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_23E")

    label("loc_253")

    Return()

    # Function_2_23E end

    def Function_3_254(): pass

    label("Function_3_254")

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
        (1, "loc_34C"),
        (SWITCH_DEFAULT, "loc_3E6"),
    )


    label("loc_34C")

    Fade(1000)
    SetChrPos(0x0, -448540, 0, 56140, 188)
    SetChrPos(0x1, -448540, 0, 56140, 188)
    SetChrPos(0x2, -448540, 0, 56140, 188)
    SetChrPos(0x3, -448540, 0, 56140, 188)
    SetChrPos(0x4, -448540, 0, 56140, 188)
    SetChrPos(0x5, -448540, 0, 56140, 188)
    SetChrPos(0x6, -448540, 0, 56140, 188)
    SetChrPos(0x7, -448540, 0, 56140, 188)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_3E6")

    Battle(0x3F9, 0x0, 0x0, 0x0, 0xFF)
    SetChrPos(0x0, -448540, 0, 56140, 188)
    SetChrPos(0x1, -448540, 0, 56140, 188)
    SetChrPos(0x2, -448540, 0, 56140, 188)
    SetChrPos(0x3, -448540, 0, 56140, 188)
    SetChrPos(0x4, -448540, 0, 56140, 188)
    SetChrPos(0x5, -448540, 0, 56140, 188)
    SetChrPos(0x6, -448540, 0, 56140, 188)
    SetChrPos(0x7, -448540, 0, 56140, 188)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_494"),
        (1, "loc_497"),
        (SWITCH_DEFAULT, "loc_49A"),
    )


    label("loc_494")

    EventEnd(0x0)
    Return()

    label("loc_497")

    OP_B4(0x0)
    Return()

    label("loc_49A")

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
            "成功消灭了西柏斯街道中被通缉的魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x17, 0x4, 0x10)
    OP_28(0x17, 0x1, 0x1)
    OP_A2(0x388)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_254 end

    SaveToFile()

Try(main)
