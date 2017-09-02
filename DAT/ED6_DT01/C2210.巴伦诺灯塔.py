from ED6ScenarioHelper import *

def main():
    # 巴伦诺灯塔

    CreateScenaFile(
        FileName            = 'C2210   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2210.x',
        MapIndex            = 84,
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
        '迪恩',                                 # 9
        '雷斯',                                 # 10
        '洛克',                                 # 11
        '青年',                                 # 12
        '青年',                                 # 13
        '青年',                                 # 14
        '青年',                                 # 15
        '青年',                                 # 16
        '青年',                                 # 17
        '黑衣男子',                             # 18
        '黑衣男子',                             # 19
        '秘书基尔巴特',                         # 20
        '弗科特老人',                           # 21
        '照相机',                               # 22
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
        Unknown_3A              = 84,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01390 ._CH',             # 00
        'ED6_DT07/CH00370 ._CH',             # 01
        'ED6_DT07/CH00371 ._CH',             # 02
        'ED6_DT07/CH00374 ._CH',             # 03
        'ED6_DT07/CH00372 ._CH',             # 04
        'ED6_DT07/CH00100 ._CH',             # 05
        'ED6_DT07/CH00110 ._CH',             # 06
        'ED6_DT07/CH00140 ._CH',             # 07
        'ED6_DT07/CH00101 ._CH',             # 08
        'ED6_DT07/CH00111 ._CH',             # 09
        'ED6_DT07/CH02420 ._CH',             # 0A
        'ED6_DT07/CH00150 ._CH',             # 0B
        'ED6_DT07/CH00151 ._CH',             # 0C
        'ED6_DT07/CH00152 ._CH',             # 0D
        'ED6_DT06/CH20102 ._CH',             # 0E
        'ED6_DT09/CH10020 ._CH',             # 0F
        'ED6_DT09/CH10021 ._CH',             # 10
        'ED6_DT07/CH01330 ._CH',             # 11
        'ED6_DT07/CH02510 ._CH',             # 12
        'ED6_DT07/CH02520 ._CH',             # 13
        'ED6_DT07/CH02530 ._CH',             # 14
        'ED6_DT07/CH00450 ._CH',             # 15
        'ED6_DT07/CH00451 ._CH',             # 16
        'ED6_DT07/CH00454 ._CH',             # 17
        'ED6_DT07/CH00452 ._CH',             # 18
        'ED6_DT07/CH00460 ._CH',             # 19
        'ED6_DT07/CH00461 ._CH',             # 1A
        'ED6_DT07/CH00464 ._CH',             # 1B
        'ED6_DT07/CH00462 ._CH',             # 1C
        'ED6_DT07/CH00470 ._CH',             # 1D
        'ED6_DT07/CH00471 ._CH',             # 1E
        'ED6_DT07/CH00474 ._CH',             # 1F
        'ED6_DT07/CH00472 ._CH',             # 20
        'ED6_DT06/CH20053 ._CH',             # 21
        'ED6_DT06/CH20085 ._CH',             # 22
        'ED6_DT07/CH00015 ._CH',             # 23
        'ED6_DT06/CH20079 ._CH',             # 24
        'ED6_DT07/CH00141 ._CH',             # 25
        'ED6_DT07/CH00340 ._CH',             # 26
        'ED6_DT07/CH00341 ._CH',             # 27
        'ED6_DT07/CH00342 ._CH',             # 28
        'ED6_DT07/CH00440 ._CH',             # 29
        'ED6_DT07/CH00441 ._CH',             # 2A
        'ED6_DT07/CH00442 ._CH',             # 2B
        'ED6_DT06/CH20080 ._CH',             # 2C
    )

    AddCharChipPat(
        'ED6_DT07/CH01390P._CP',             # 00
        'ED6_DT07/CH00370P._CP',             # 01
        'ED6_DT07/CH00371P._CP',             # 02
        'ED6_DT07/CH00374P._CP',             # 03
        'ED6_DT07/CH00372P._CP',             # 04
        'ED6_DT07/CH00100P._CP',             # 05
        'ED6_DT07/CH00110P._CP',             # 06
        'ED6_DT07/CH00140P._CP',             # 07
        'ED6_DT07/CH00101P._CP',             # 08
        'ED6_DT07/CH00111P._CP',             # 09
        'ED6_DT07/CH02420P._CP',             # 0A
        'ED6_DT07/CH00150P._CP',             # 0B
        'ED6_DT07/CH00151P._CP',             # 0C
        'ED6_DT07/CH00152P._CP',             # 0D
        'ED6_DT06/CH20102P._CP',             # 0E
        'ED6_DT09/CH10020P._CP',             # 0F
        'ED6_DT09/CH10021P._CP',             # 10
        'ED6_DT07/CH01330P._CP',             # 11
        'ED6_DT07/CH02510P._CP',             # 12
        'ED6_DT07/CH02520P._CP',             # 13
        'ED6_DT07/CH02530P._CP',             # 14
        'ED6_DT07/CH00450P._CP',             # 15
        'ED6_DT07/CH00451P._CP',             # 16
        'ED6_DT07/CH00454P._CP',             # 17
        'ED6_DT07/CH00452P._CP',             # 18
        'ED6_DT07/CH00460P._CP',             # 19
        'ED6_DT07/CH00461P._CP',             # 1A
        'ED6_DT07/CH00464P._CP',             # 1B
        'ED6_DT07/CH00462P._CP',             # 1C
        'ED6_DT07/CH00470P._CP',             # 1D
        'ED6_DT07/CH00471P._CP',             # 1E
        'ED6_DT07/CH00474P._CP',             # 1F
        'ED6_DT07/CH00472P._CP',             # 20
        'ED6_DT06/CH20053P._CP',             # 21
        'ED6_DT06/CH20085P._CP',             # 22
        'ED6_DT07/CH00015P._CP',             # 23
        'ED6_DT06/CH20079P._CP',             # 24
        'ED6_DT07/CH00141P._CP',             # 25
        'ED6_DT07/CH00340P._CP',             # 26
        'ED6_DT07/CH00341P._CP',             # 27
        'ED6_DT07/CH00342P._CP',             # 28
        'ED6_DT07/CH00440P._CP',             # 29
        'ED6_DT07/CH00441P._CP',             # 2A
        'ED6_DT07/CH00442P._CP',             # 2B
        'ED6_DT06/CH20080P._CP',             # 2C
    )

    DeclNpc(
        X                   = -11200,
        Z                   = 0,
        Y                   = 7490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -9460,
        Z                   = 0,
        Y                   = 7150,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -10770,
        Z                   = 0,
        Y                   = 5350,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -11930,
        Z                   = 0,
        Y                   = 4280,
        Direction           = 90,
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
        X                   = -11460,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 90,
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
        X                   = -10100,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 90,
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
        X                   = -11930,
        Z                   = 0,
        Y                   = 4280,
        Direction           = 90,
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
        X                   = -11460,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 90,
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
        X                   = -10100,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 90,
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
        X                   = -11460,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -10100,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3670,
        Z                   = 90,
        Y                   = 200850,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x104,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -3810,
        Y                   = 2250,
        Z                   = 106920,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 6,
    )


    ScpFunction(
        "Function_0_3F2",          # 00, 0
        "Function_1_5EF",          # 01, 1
        "Function_2_614",          # 02, 2
        "Function_3_62A",          # 03, 3
        "Function_4_11FA",         # 04, 4
        "Function_5_15C0",         # 05, 5
        "Function_6_19B6",         # 06, 6
        "Function_7_3B3C",         # 07, 7
        "Function_8_3B90",         # 08, 8
        "Function_9_3C07",         # 09, 9
        "Function_10_3C6D",        # 0A, 10
        "Function_11_3CF8",        # 0B, 11
    )


    def Function_0_3F2(): pass

    label("Function_0_3F2")

    SetMapFlags(0x40000000)
    AddParty(0xFF, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_40E"),
        (102, "loc_421"),
        (104, "loc_434"),
        (SWITCH_DEFAULT, "loc_447"),
    )


    label("loc_40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41E")
    Event(0, 3)

    label("loc_41E")

    Jump("loc_447")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_431")
    Event(0, 4)

    label("loc_431")

    Jump("loc_447")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_444")
    Event(0, 5)

    label("loc_444")

    Jump("loc_447")

    label("loc_447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 3)), scpexpr(EXPR_END)), "loc_4D4")
    SetChrFlags(0xF, 0x800)
    SetChrFlags(0x10, 0x800)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    SetChrChipByIndex(0xA, 31)
    SetChrChipByIndex(0xF, 36)
    SetChrChipByIndex(0x10, 36)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, 102990, 0, 98020, 270)
    SetChrPos(0xF, 104030, 0, 99080, 0)
    SetChrPos(0x10, 102870, 0, 100160, 135)

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 2)), scpexpr(EXPR_END)), "loc_561")
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xE, 0x800)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    SetChrChipByIndex(0x9, 27)
    SetChrChipByIndex(0xD, 36)
    SetChrChipByIndex(0xE, 36)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 102640, 0, 1840, 270)
    SetChrPos(0xD, 101950, 0, 3240, 0)
    SetChrPos(0xE, 101850, 0, 770, 135)

    label("loc_561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 1)), scpexpr(EXPR_END)), "loc_5EE")
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0x8, -240, 0, 6100, 225)
    SetChrPos(0xB, 1680, 0, 4920, 180)
    SetChrPos(0xC, -1990, 0, 5180, 315)
    SetChrChipByIndex(0x8, 23)
    SetChrChipByIndex(0xB, 36)
    SetChrChipByIndex(0xC, 36)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5EE")

    Return()

    # Function_0_3F2 end

    def Function_1_5EF(): pass

    label("Function_1_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FE")
    Jump("loc_5FE")

    label("loc_5FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x392), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_613")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_613")

    Return()

    # Function_1_5EF end

    def Function_2_614(): pass

    label("Function_2_614")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_629")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_614")

    label("loc_629")

    Return()

    # Function_2_614 end

    def Function_3_62A(): pass

    label("Function_3_62A")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(400, 0, -2430, 0)
    SetChrPos(0x101, 1330, 0, -5430, 0)
    SetChrPos(0x102, -680, 0, -5890, 0)
    SetChrPos(0x106, 380, 0, -4780, 0)
    SetChrPos(0x105, 190, 0, -6650, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, 0, 0, 0, 0)
    SetChrPos(0xB, 500, 0, 2140, 225)
    SetChrPos(0xC, -1740, 0, 1110, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#005F是、是他们！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F前、前几天在仓库碰到的那些人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#057F真没想到……\x02",
    )

    CloseMessageWindow()
    OP_8E(0x106, 0x78, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(
        0x106,
        (
            "#054F喂，你们几个蠢货……\x01",
            "在这种地方干什么！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D8():
        TurnDirection(0xFE, 0x101, 230)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7D8)

    def lambda_7E6():
        TurnDirection(0xFE, 0x101, 230)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7E6)

    def lambda_7F4():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7F4)
    Sleep(400)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "三个不良青年露出双目呆滞的神态，\x01",
            "似乎什么也意识不到。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x106,
        "#055F喂、喂……\x02",
    )

    CloseMessageWindow()

    def lambda_8B2():
        OP_8E(0xFE, 0xFFFFFF56, 0x0, 0xFFFFFA38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_8B2)
    Sleep(300)
    OP_63(0x8)
    OP_63(0xB)
    OP_63(0xC)
    SetChrChipByIndex(0x8, 24)
    OP_51(0x0, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1FC, 0x0, 0x64)

    def lambda_8F0():
        OP_99(0xFE, 0x0, 0x2, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8F0)

    def lambda_900():
        OP_6D(-170, 0, -1480, 700)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_900)

    ChrTalk(
        0x102,
        "#016F阿加特兄，危险！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x20)

    def lambda_93D():
        OP_93(0xFE, 0x106, 0x384, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_93D)
    OP_51(0x0, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_99(0x8, 0x2, 0x4, 0xFA0)
    OP_22(0xD6, 0x0, 0x64)
    OP_44(0x106, 0xFF)
    SetChrChipByIndex(0x106, 12)
    OP_94(0x1, 0x106, 0xB4, 0x64, 0x1388, 0x0)

    def lambda_983():
        OP_9E(0xFE, 0x14, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_983)

    def lambda_99D():
        OP_9E(0xFE, 0x14, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_99D)
    OP_6B(2800, 700)
    Sleep(500)

    ChrTalk(
        0x106,
        "#052F#4P这、这力量……！？\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_A06():
        OP_6B(3000, 150)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A06)

    def lambda_A16():
        OP_99(0x8, 0x4, 0x7, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A16)
    SetChrFlags(0x8, 0x20)
    OP_95(0x106, 0x0, 0x0, 0xFFFFFA24, 0x12C, 0x1388)
    OP_95(0x106, 0x0, 0x0, 0xFFFFFE0C, 0x64, 0x1388)
    SetChrChipByIndex(0x106, 11)
    ClearChrFlags(0x8, 0x20)
    Sleep(100)
    SetChrChipByIndex(0x8, 21)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x105, 7)
    Sleep(500)

    ChrTalk(
        0x106,
        "#057F迪恩，你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_AAA():
        OP_8E(0xFE, 0x4B0, 0x0, 0xB0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AAA)

    def lambda_AC5():
        OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x100, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_AC5)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 1)
    OP_22(0x1FC, 0x0, 0x64)
    OP_8C(0xC, 180, 0)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 1)
    OP_22(0x1FC, 0x0, 0x64)
    OP_8C(0xB, 180, 0)

    ChrTalk(
        0x106,
        (
            "#057F哈，很好……\x02\x03",
            "虽然不知道\x01",
            "你们在做什么梦……\x02\x03",
            "#054F就让我好好教训教训你们，\x01",
            "给我乖乖清醒过来吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x105, 0x1000)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x101, 8)

    def lambda_BBB():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BBB)
    Sleep(50)
    SetChrChipByIndex(0x102, 9)

    def lambda_BE0():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE0)
    SetChrChipByIndex(0x105, 37)

    def lambda_C00():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C00)
    SetChrChipByIndex(0xB, 2)

    def lambda_C20():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C20)
    Sleep(100)
    SetChrChipByIndex(0xC, 2)

    def lambda_C45():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C45)
    Sleep(50)
    SetChrChipByIndex(0x8, 22)

    def lambda_C6A():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C6A)
    OP_44(0x106, 0xFF)
    SetChrChipByIndex(0x106, 13)

    def lambda_C8E():
        OP_99(0x106, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C8E)

    def lambda_C9E():
        OP_95(0x106, 0x0, 0x0, 0x5DC, 0x5DC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_C9E)
    Sleep(300)
    Battle(0x38F, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_CD4"),
        (SWITCH_DEFAULT, "loc_CD7"),
    )


    label("loc_CD4")

    OP_B4(0x0)
    Return()

    label("loc_CD7")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x105, 0xFF)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    ClearChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrChipByIndex(0x102, 35)
    OP_6D(340, 0, 4960, 0)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    SetChrPos(0x102, 860, 0, 4710, 90)
    SetChrPos(0x106, -830, 0, 4400, 0)
    SetChrPos(0x101, 420, 0, 3000, 0)
    SetChrPos(0x105, -880, 0, 2850, 0)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0x8, -240, 0, 6100, 225)
    SetChrPos(0xB, 1680, 0, 4920, 180)
    SetChrPos(0xC, -1990, 0, 5180, 315)
    SetChrChipByIndex(0x8, 23)
    SetChrChipByIndex(0xB, 36)
    SetChrChipByIndex(0xC, 36)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#009F真、真不敢相信……\x02\x03",
            "他们比在仓库战斗的时候\x01",
            "强了好几个档次啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F而且样子怪怪的……\x01",
            "到底是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F哼……\x02\x03",
            "看来这些蠢货\x01",
            "是被什么人操纵了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F操、操纵是指……\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(
        0x102,
        "#015F嗯，没错……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x102, 400)
    TurnDirection(0x105, 0x102, 400)
    Fade(250)
    SetChrChipByIndex(0x102, 65535)
    OP_0D()
    Sleep(500)
    OP_8C(0x102, 225, 400)

    ChrTalk(
        0x102,
        (
            "#012F似乎是同时利用了药品\x01",
            "和心理暗示的特殊催眠术。\x02\x03",
            "而且身体的潜能也被激发出来。\x01",
            "换言之，力量也达到了更高的水平。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F这、这种事也能做得到吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F当然，\x01",
            "不过这无疑需要相当高明的技术。\x02\x03",
            "这帮家伙难道是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x106, 400)

    ChrTalk(
        0x105,
        "#044F您想到会是谁了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x105, 400)

    ChrTalk(
        0x106,
        (
            "#053F啊啊……有点数了。\x02\x03",
            "#050F总之，往塔顶走吧。\x02\x03",
            "操纵这些蠢货的幕后真凶\x01",
            "一定就在那里！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，知道了！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x439)
    OP_28(0x3E, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_3_62A end

    def Function_4_11FA(): pass

    label("Function_4_11FA")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(96710, 0, 2960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x105, 7)
    SetChrChipByIndex(0x106, 11)
    SetChrPos(0x101, 96610, 0, 4430, 180)
    SetChrPos(0x102, 95640, 0, 5100, 180)
    SetChrPos(0x106, 97840, 0, 5070, 180)
    SetChrPos(0x105, 96810, 0, 5780, 180)
    SetChrChipByIndex(0x9, 25)
    SetChrChipByIndex(0xD, 1)
    SetChrChipByIndex(0xE, 1)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 96530, 0, -1510, 0)
    SetChrPos(0xD, 94530, 0, -1770, 0)
    SetChrPos(0xE, 98360, 0, -790, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F又、又来了～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F虽然不想与你们战斗，\x01",
            "但为了找出真正的犯人……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 26)

    def lambda_137E():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_137E)
    Sleep(50)
    SetChrChipByIndex(0xD, 2)

    def lambda_13A3():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_13A3)
    Sleep(50)
    SetChrChipByIndex(0xE, 2)

    def lambda_13C8():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_13C8)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x105, 0x1000)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x101, 8)

    def lambda_13FC():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13FC)
    Sleep(50)
    SetChrChipByIndex(0x102, 9)

    def lambda_1421():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1421)
    Sleep(50)
    SetChrChipByIndex(0x106, 12)

    def lambda_1446():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1446)
    Sleep(50)
    SetChrChipByIndex(0x105, 37)

    def lambda_146B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_146B)
    Sleep(200)
    Battle(0x390, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_149E"),
        (SWITCH_DEFAULT, "loc_14A1"),
    )


    label("loc_149E")

    OP_B4(0x0)
    Return()

    label("loc_14A1")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x105, 0xFF)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    ClearChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrChipByIndex(0x105, 65535)
    OP_44(0x9, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xE, 0x800)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    SetChrChipByIndex(0x9, 27)
    SetChrChipByIndex(0xD, 36)
    SetChrChipByIndex(0xE, 36)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 102640, 0, 1840, 270)
    SetChrPos(0xD, 101950, 0, 3240, 0)
    SetChrPos(0xE, 101850, 0, 770, 135)
    OP_6D(100640, 0, 1850, 0)
    SetChrPos(0x101, 100640, 0, 1850, 95)
    SetChrPos(0x102, 100640, 0, 1850, 95)
    SetChrPos(0x106, 100640, 0, 1850, 95)
    SetChrPos(0x105, 100640, 0, 1850, 95)
    FadeToBright(1000, 0)
    OP_A2(0x43A)
    EventEnd(0x0)
    Return()

    # Function_4_11FA end

    def Function_5_15C0(): pass

    label("Function_5_15C0")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(102090, 0, 102370, 0)
    SetChrChipByIndex(0xA, 29)
    SetChrChipByIndex(0xF, 1)
    SetChrChipByIndex(0x10, 1)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x105, 7)
    SetChrChipByIndex(0x106, 11)
    SetChrPos(0x101, 104660, 0, 103320, 225)
    SetChrPos(0x102, 104440, 0, 104470, 225)
    SetChrPos(0x106, 103330, 0, 103120, 225)
    SetChrPos(0x105, 103150, 0, 104290, 225)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, 98520, 0, 98750, 45)
    SetChrPos(0xF, 97520, 0, 99170, 45)
    SetChrPos(0x10, 99010, 0, 97700, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F对不起……\x02\x03",
            "其实我真的不想对\x01",
            "只是受控于人的对手出剑……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F哼，不必客气。\x02\x03",
            "#054F留他们一口气就够了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x105, 0x1000)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0xA, 30)

    def lambda_1788():
        OP_90(0xFE, 0xBB8, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1788)
    Sleep(50)
    SetChrChipByIndex(0xF, 2)

    def lambda_17AD():
        OP_90(0xFE, 0xBB8, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_17AD)
    Sleep(50)
    SetChrChipByIndex(0x10, 2)

    def lambda_17D2():
        OP_90(0xFE, 0xBB8, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_17D2)
    SetChrChipByIndex(0x106, 12)

    def lambda_17F2():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_17F2)
    Sleep(50)
    SetChrChipByIndex(0x105, 37)

    def lambda_1817():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1817)
    Sleep(50)
    SetChrChipByIndex(0x101, 8)

    def lambda_183C():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_183C)
    Sleep(50)
    SetChrChipByIndex(0x102, 9)

    def lambda_1861():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1861)
    Sleep(300)
    Battle(0x391, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1894"),
        (SWITCH_DEFAULT, "loc_1897"),
    )


    label("loc_1894")

    OP_B4(0x0)
    Return()

    label("loc_1897")

    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    ClearChrFlags(0x106, 0x1000)
    OP_6D(100440, 0, 98970, 0)
    SetChrPos(0x101, 100440, 0, 98970, 90)
    SetChrPos(0x102, 100440, 0, 98970, 90)
    SetChrPos(0x106, 100440, 0, 98970, 90)
    SetChrPos(0x105, 100440, 0, 98970, 90)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x105, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrChipByIndex(0x105, 65535)
    OP_44(0xA, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrFlags(0xF, 0x800)
    SetChrFlags(0x10, 0x800)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    SetChrChipByIndex(0xA, 31)
    SetChrChipByIndex(0xF, 36)
    SetChrChipByIndex(0x10, 36)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, 102990, 0, 98020, 270)
    SetChrPos(0xF, 104030, 0, 99080, 0)
    SetChrPos(0x10, 102870, 0, 100160, 135)
    FadeToBright(1000, 0)
    OP_A2(0x43B)
    EventEnd(0x0)
    Return()

    # Function_5_15C0 end

    def Function_6_19B6(): pass

    label("Function_6_19B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19C3")
    Return()

    label("loc_19C3")

    OP_A2(0x43C)
    ClearMapFlags(0x1)
    EventBegin(0x0)

    def lambda_19D3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_19D3)

    def lambda_19E1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_19E1)

    def lambda_19EF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_19EF)

    def lambda_19FD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_19FD)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A64")

    ChrTalk(
        0x101,
        "#004F咦……这声音……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B62")

    label("loc_1A64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB7")

    ChrTalk(
        0x102,
        (
            "#012F等一下。\x01",
            "好像听见有人在说话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B62")

    label("loc_1AB7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B17")

    ChrTalk(
        0x105,
        (
            "#044F啊……\x01",
            "好像在哪里听过的声音……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B62")

    label("loc_1B17")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B62")

    ChrTalk(
        0x106,
        (
            "#057F等等。\x01",
            "我听见有人在说话……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B62")

    OP_20(0x5DC)
    Sleep(100)
    Fade(1000)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x13, -1490, 0, 198560, 270)
    SetChrPos(0x11, -2330, 0, 199540, 180)
    SetChrPos(0x12, -2780, 0, 198270, 90)
    OP_6D(-2200, 0, 198720, 0)
    OP_67(0, 7710, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_21()
    OP_1D(0x51)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x13,
        (
            "#675F呵呵呵……\x01",
            "你们做得非常好。\x02\x03",
            "接着只要把罪名全推到那帮败类头上，\x01",
            "我们以后就万事大吉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "我们的办事能力\x01",
            "你应该满意吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#675F嗯，真是高明的手段。\x02\x03",
            "不过还是确认一下比较稳妥……\x01",
            "没留下什么证据吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "嘿嘿，放心吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "就算他们恢复了意识，\x01",
            "也完全不会记得我们的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "看守这灯塔的老头\x01",
            "不到天亮也不会醒的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#675F听你这么说我就放心了。\x02\x03",
            "这样一来，\x01",
            "那个院长也该放弃孤儿院的重建了……\x02\x03",
            "纵火等一连串案件\x01",
            "也名正言顺推到了那帮败类头上。\x02\x03",
            "这就叫做一箭双雕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "你能达成计划就好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不过我说，\x01",
            "毁掉那间孤儿院到底有什么好处……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "真是百思不得其解啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#675F呵呵，看在你们劳苦功高的份上，\x01",
            "我就破例告诉你们吧。\x02\x03",
            "市长打算将那一带的土地\x01",
            "开发成高级别墅区。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "哦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#675F那里紧靠着风光明媚的海道，\x01",
            "而且离卢安市区又不远。\x02\x03",
            "在那种地头建高级别墅区\x01",
            "是最合适不过了。\x02\x03",
            "等到豪宅建成之后，\x01",
            "再卖给国内外的大富豪……\x02\x03",
            "这就是市长的计划了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "哦，真是庞大的计划啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "但为什么\x01",
            "要毁了那孤儿院呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#675F哈哈，你们想想看。\x02\x03",
            "要是在豪华的别墅区当中，\x01",
            "留着那样一座破旧的房子会怎样？\x02\x03",
            "更何况每天还要\x01",
            "忍受着那群小鬼的喧哗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "原来如此……\x01",
            "作为别墅区的价值恐怕会减半吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不过，与其铤而走险，\x01",
            "还不如买下那孤儿院比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#675F哈，那个顽固的女人，\x01",
            "哪里肯卖掉丈夫留下的土地。\x02\x03",
            "但是，只要趁他们不在的时候，\x01",
            "把烧毁的房子清理掉，然后再造上别墅，\x01",
            "那就是我们的东西了。\x02\x03",
            "嘿嘿，连重建费用都被抢走的话，\x01",
            "她不认命也不行了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x105, 0x1000)
    SetChrFlags(0x106, 0x1000)
    SetChrPos(0x101, 3950, 0, 204590, 225)
    SetChrPos(0x102, 3860, 0, 205710, 225)
    SetChrPos(0x106, 2790, 0, 204560, 225)
    SetChrPos(0x105, 2640, 0, 205560, 225)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x105, 7)
    SetChrChipByIndex(0x106, 11)

    ChrTalk(
        0x105,
        "#6P这就是理由吗……\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    def lambda_2648():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2648)

    def lambda_2656():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2656)

    def lambda_2664():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2664)

    def lambda_2672():
        OP_6D(1330, 0, 201850, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2672)

    def lambda_268A():
        OP_67(0, 6000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_268A)

    def lambda_26A2():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_26A2)
    WaitChrThread(0x14, 0x1)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x13, 0xFFFFF952, 0x0, 0x304F8, 0x1388, 0x0)

    ChrTalk(
        0x13,
        "#676F是、是你们……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#049F怎能这样呢……\x01",
            "为了这种毫无意义的事……\x02\x03",
            "不但伤害了老师他们……\x01",
            "让充满回忆的地方化作灰烬……\x02\x03",
            "还让孩子们的心灵受到创伤……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#674F你、你们怎么会找到这里来的！？\x02\x03",
            "还有……\x01",
            "那帮败类不是都在看守的吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4P真可惜～\x01",
            "大家都睡得正香呢。\x02\x03",
            "不过，真没想到市长就是\x01",
            "这一系列事件的幕后黑手啊。\x02\x03",
            "而且，似乎还有些\x01",
            "相当面善的家伙牵涉其中……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "哦……？\x01",
            "小姑娘你认识我们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "我们跟那个红发的游击士\x01",
            "倒是有过数面之缘……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F哈，什么叫数面之缘。\x02\x03",
            "东躲西藏、四处逃窜，\x01",
            "最后还引魔兽来对付我。\x02\x03",
            "不过，这下终于让我\x01",
            "抓到你们这些家伙的尾巴了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#674F你、你们两个！\x01",
            "快把他们全部杀掉！\x02\x03",
            "既、既然被他们看见了，\x01",
            "就绝不能让他们活着出去！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#042F前辈……你太让人失望了……\x02",
    )

    CloseMessageWindow()
    OP_8E(0x12, 0xFFFFFA06, 0x0, 0x3099E, 0xBB8, 0x0)
    TurnDirection(0x12, 0x106, 0)
    SetChrChipByIndex(0x12, 38)

    ChrTalk(
        0x11,
        (
            "#4P好吧，既然客户提出要求的话，\x01",
            "那我们不做也不行了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 41)

    ChrTalk(
        0x12,
        "#3P就让我们陪你们玩玩吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#4P哼，正合我意！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F就算是受人指使，\x01",
            "你们的罪行也无可抵赖……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#054F让你们好好尝尝……\x01",
            "我这把重剑的厉害吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 39)

    def lambda_2C35():
        OP_91(0xFE, 0xBB8, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C35)
    Sleep(100)
    SetChrChipByIndex(0x12, 42)

    def lambda_2C5A():
        OP_91(0xFE, 0xBB8, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2C5A)
    SetChrChipByIndex(0x106, 12)

    def lambda_2C7A():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2C7A)
    Sleep(50)
    SetChrChipByIndex(0x105, 37)

    def lambda_2C9F():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2C9F)
    Sleep(50)
    SetChrChipByIndex(0x101, 8)

    def lambda_2CC4():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CC4)
    Sleep(50)
    SetChrChipByIndex(0x102, 9)

    def lambda_2CE9():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CE9)
    Sleep(300)
    Battle(0x392, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2D1C"),
        (SWITCH_DEFAULT, "loc_2D1F"),
    )


    label("loc_2D1C")

    OP_B4(0x0)
    Return()

    label("loc_2D1F")

    EventBegin(0x0)
    OP_6D(-390, 0, 200780, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x105, 7)
    SetChrChipByIndex(0x106, 11)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x106, 0)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x11, 38)
    SetChrChipByIndex(0x12, 41)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x13, -600, 0, 197930, 0)
    SetChrPos(0x11, -2220, 0, 197930, 45)
    SetChrPos(0x12, -3180, 0, 199000, 45)
    SetChrPos(0x101, 1470, 0, 201530, 225)
    SetChrPos(0x106, 400, 0, 201760, 225)
    SetChrPos(0x102, 120, 0, 202880, 225)
    SetChrPos(0x105, 1590, 0, 202760, 225)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x13,
        "#676F这、这怎么可能……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F#1P市长秘书基尔巴特，\x01",
            "还有旁边的两个黑衣男子。\x02\x03",
            "现基于游击士协会规定，\x01",
            "我要将你们逮捕并拘留归案。\x02\x03",
            "放弃抵抗，乖乖投降吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#676F呜呜呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "还真有两下子嘛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "正面交手的话\x01",
            "果然还是游击士比较强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "嗯，就像队长之前说的，\x01",
            "我们不该这么大意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F队长……\x02\x03",
            "难道就是当初和空贼交涉时，\x01",
            "那个戴着红色面具的男人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "这事你们居然也知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "不愧是游击士协会养的狗。\x01",
            "鼻子还挺灵的嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F明明是手下败将，\x01",
            "竟然还有心情耍嘴皮子！\x02\x03",
            "快点放下武器，\x01",
            "老老实实投降吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "哈哈，这可不行啊。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 17)
    OP_8E(0x11, 0xFFFFF970, 0x0, 0x30494, 0x5DC, 0x0)
    TurnDirection(0x11, 0x13, 400)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x11, 43)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(500)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x13, 0x11, 400)

    ChrTalk(
        0x13,
        "#676F#2P什……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F你、你们想做什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "别动。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "你们要是再靠近的话，\x01",
            "这家伙的脑袋可就不保哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#674F#2P你、你们！？\x02\x03",
            "你、你们竟然对\x01",
            "自己的雇主做出这种事情！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "别误会了，小子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "我们的雇主是市长，\x01",
            "不是你这家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "不过就算是市长也一样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "我们只不过利害关系一致，\x01",
            "所以才帮他一把罢了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "就算你在这里死掉，\x01",
            "我们也是完全不痛不痒。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0x13, 0x32, 0x0, 0x258, 0x1770)

    ChrTalk(
        0x13,
        (
            "#676F#2P啊、啊啊啊……\x02\x03",
            "别过来、你们别过来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F#1P喂，你们玩够没有。\x02\x03",
            "以为演演这种下三滥的猴戏\x01",
            "就能跑得了吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x11, 0x0, 0x2, 0x7D0)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_350D():
        OP_99(0xFE, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_350D)

    def lambda_351D():
        OP_6D(1400, 0, 201500, 1000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_351D)
    OP_96(0x13, 0x2EE, 0x0, 0x30782, 0x64, 0x1388)
    SetChrChipByIndex(0x13, 44)
    LoadEffect(0x0, "map\\\\mp020_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 700, 0, 198510, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9E(0x13, 0x32, 0x0, 0x258, 0x1770)

    ChrTalk(
        0x13,
        (
            "#677F#2P啊啊啊啊……\x02\x03",
            "#677F啊，腿……我的腿！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#046F前、前辈！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#057F#1P嘁……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F看来他们是认真的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "要是这样你们还不相信的话……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x14, 400)
    SetChrFlags(0x12, 0x20)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 43)
    ClearChrFlags(0x12, 0x20)

    ChrTalk(
        0x12,
        (
            "把这看守的老头脑袋打穿\x01",
            "我也倒是无所谓。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#2P住、住手！\x01",
            "不要把无辜的人扯进来！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x106, 400)

    ChrTalk(
        0x11,
        (
            "要我不伤害他也行，\x01",
            "不过你们要向后退一段距离……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "对了……\x01",
            "就退到楼梯边上吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#050F#1P哼，没办法……\x02",
    )

    CloseMessageWindow()

    def lambda_37B8():
        OP_6D(530, 0, 202030, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_37B8)
    SetChrChipByIndex(0x105, 65535)

    def lambda_37D5():
        OP_8F(0xFE, 0xE06, 0x0, 0x321D6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_37D5)
    Sleep(100)
    SetChrChipByIndex(0x102, 65535)

    def lambda_37FA():
        OP_8F(0xFE, 0x9EC, 0x0, 0x32208, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37FA)
    Sleep(100)
    SetChrChipByIndex(0x101, 65535)

    def lambda_381F():
        OP_8F(0xFE, 0xE9C, 0x0, 0x31D4E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_381F)
    Sleep(100)
    SetChrChipByIndex(0x106, 33)

    def lambda_3844():
        OP_8F(0xFE, 0xA0A, 0x0, 0x31CE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3844)
    Sleep(200)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x1)

    ChrTalk(
        0x12,
        "呵呵，很好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "那么，再见了。\x02",
    )

    CloseMessageWindow()

    def lambda_38FF():

        label("loc_38FF")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_38FF")

    QueueWorkItem2(0x101, 2, lambda_38FF)

    def lambda_3910():

        label("loc_3910")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3910")

    QueueWorkItem2(0x102, 2, lambda_3910)

    def lambda_3921():

        label("loc_3921")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3921")

    QueueWorkItem2(0x105, 2, lambda_3921)

    def lambda_3932():

        label("loc_3932")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3932")

    QueueWorkItem2(0x106, 2, lambda_3932)
    SetChrChipByIndex(0x11, 42)

    def lambda_3948():
        OP_6D(3130, 0, 201480, 2000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_3948)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x11, 0x4)
    OP_8E(0x11, 0xFFFFF02E, 0x0, 0x2FAA8, 0x1770, 0x0)
    ClearChrFlags(0x11, 0x4)
    OP_8E(0x11, 0xFFFFF592, 0x0, 0x2FB5C, 0x1770, 0x0)

    def lambda_3997():

        label("loc_3997")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3997")

    QueueWorkItem2(0x106, 2, lambda_3997)
    OP_8E(0x11, 0x7D9, 0x3E8, 0x2FA80, 0x1770, 0x0)

    def lambda_39BC():
        OP_8E(0x11, 0x1DEC, 0x3E8, 0x31100, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_39BC)
    Sleep(100)
    SetChrChipByIndex(0x12, 42)
    OP_8F(0x12, 0x3DE, 0x0, 0x30B88, 0xFA0, 0x0)
    OP_8F(0x12, 0xDFC, 0x0, 0x30778, 0xFA0, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x12, 0x12C0, 0x3E8, 0x3055C, 0x7D0, 0x1770)

    def lambda_3A25():
        OP_8E(0x12, 0x1DEC, 0x3E8, 0x31100, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3A25)
    WaitChrThread(0x11, 0x1)
    OP_4A(0x11, 1)
    OP_4A(0x12, 1)
    OP_6F(0x0, 20)
    OP_48()
    OP_6F(0x0, 40)
    OP_48()
    OP_70(0x0, 0x50)
    OP_4B(0x11, 1)
    OP_4B(0x12, 1)

    def lambda_3A6C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3A6C)

    def lambda_3A7E():
        OP_8E(0xFE, 0x22F6, 0x3E8, 0x3124A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_3A7E)
    WaitChrThread(0x12, 0x1)

    def lambda_3A9E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3A9E)

    def lambda_3AB0():
        OP_8E(0xFE, 0x22F6, 0x3E8, 0x3124A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_3AB0)

    ChrTalk(
        0x101,
        "#005F给我站住！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#054F你们逃不掉的，混帐！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    ClearChrFlags(0x106, 0x1000)
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C2200   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_6_19B6 end

    def Function_7_3B3C(): pass

    label("Function_7_3B3C")

    OP_93(0x13, 0x106, 0x258, 0x2EE0, 0x0)

    ChrTalk(
        0x13,
        "#670F哇啊……\x05\x02",
    )

    TurnDirection(0x106, 0x13, 0)
    TurnDirection(0x13, 0x106, 0)

    def lambda_3B70():
        OP_94(0x1, 0x13, 0x0, 0x258, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3B70)
    OP_94(0x1, 0x106, 0xB4, 0x258, 0x1770, 0x0)
    Return()

    # Function_7_3B3C end

    def Function_8_3B90(): pass

    label("Function_8_3B90")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3BA6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3BA6)
    SetChrChipByIndex(0x101, 8)
    OP_8E(0xFE, 0xB5E, 0x0, 0x327DA, 0x1388, 0x0)
    OP_8E(0xFE, 0xC6C, 0x0, 0x32546, 0x1388, 0x0)
    OP_8E(0x101, 0x6D6, 0x0, 0x31A10, 0x1388, 0x0)
    OP_8C(0xFE, 225, 0)
    SetChrChipByIndex(0x101, 5)
    OP_43(0x101, 0x2, 0x0, 0x2)
    Return()

    # Function_8_3B90 end

    def Function_9_3C07(): pass

    label("Function_9_3C07")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3C1D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C1D)
    OP_8E(0xFE, 0xB5E, 0x0, 0x327DA, 0x1388, 0x0)
    OP_8E(0xFE, 0xC6C, 0x0, 0x32546, 0x1388, 0x0)
    OP_8E(0x105, 0x456, 0x0, 0x31CB8, 0x1388, 0x0)
    OP_8C(0xFE, 225, 0)
    Return()

    # Function_9_3C07 end

    def Function_10_3C6D(): pass

    label("Function_10_3C6D")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3C83():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C83)
    SetChrChipByIndex(0x102, 9)
    OP_8E(0xFE, 0xB5E, 0x0, 0x327DA, 0x1388, 0x0)
    OP_8E(0xFE, 0xC6C, 0x0, 0x32546, 0x1388, 0x0)
    OP_8E(0x102, 0x852, 0x0, 0x32096, 0x1388, 0x0)
    OP_8E(0x102, 0x30C, 0x0, 0x320DC, 0x1388, 0x0)
    OP_8C(0xFE, 225, 0)
    SetChrChipByIndex(0x102, 6)
    OP_43(0x102, 0x2, 0x0, 0x2)
    Return()

    # Function_10_3C6D end

    def Function_11_3CF8(): pass

    label("Function_11_3CF8")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3D0E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D0E)
    SetChrChipByIndex(0x106, 12)
    OP_8E(0xFE, 0xB5E, 0x0, 0x327DA, 0x1388, 0x0)
    OP_8E(0xFE, 0xC6C, 0x0, 0x32546, 0x1388, 0x0)
    OP_8E(0x106, 0xD2A, 0x0, 0x31AF6, 0x1388, 0x0)
    OP_8C(0xFE, 225, 0)
    SetChrChipByIndex(0x106, 11)
    OP_43(0x106, 0x2, 0x0, 0x2)
    Return()

    # Function_11_3CF8 end

    SaveToFile()

Try(main)
