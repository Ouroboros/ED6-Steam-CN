from ED6ScenarioHelper import *

def main():
    # 安塞尔新街

    CreateScenaFile(
        FileName            = 'R1401   ._SN',
        MapName             = 'Bose',
        Location            = 'R1401.x',
        MapIndex            = 58,
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
        Unknown_3A              = 58,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10290 ._CH',             # 00
        'ED6_DT09/CH10291 ._CH',             # 01
        'ED6_DT09/CH10330 ._CH',             # 02
        'ED6_DT09/CH10331 ._CH',             # 03
        'ED6_DT09/CH10540 ._CH',             # 04
        'ED6_DT09/CH10541 ._CH',             # 05
        'ED6_DT09/CH10550 ._CH',             # 06
        'ED6_DT09/CH10551 ._CH',             # 07
        'ED6_DT09/CH10870 ._CH',             # 08
        'ED6_DT09/CH10871 ._CH',             # 09
        'ED6_DT09/CH10410 ._CH',             # 0A
        'ED6_DT09/CH10411 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT09/CH10290P._CP',             # 00
        'ED6_DT09/CH10291P._CP',             # 01
        'ED6_DT09/CH10330P._CP',             # 02
        'ED6_DT09/CH10331P._CP',             # 03
        'ED6_DT09/CH10540P._CP',             # 04
        'ED6_DT09/CH10541P._CP',             # 05
        'ED6_DT09/CH10550P._CP',             # 06
        'ED6_DT09/CH10551P._CP',             # 07
        'ED6_DT09/CH10870P._CP',             # 08
        'ED6_DT09/CH10871P._CP',             # 09
        'ED6_DT09/CH10410P._CP',             # 0A
        'ED6_DT09/CH10411P._CP',             # 0B
    )

    DeclNpc(
        X                   = -140120,
        Z                   = -30,
        Y                   = -242150,
        Direction           = 7,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -141010,
        Z                   = -10,
        Y                   = -90880,
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
        X                   = -140930,
        Z                   = 230,
        Y                   = -255020,
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
        X                   = -218590,
        Z                   = -180,
        Y                   = -201180,
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
        X                   = -145850,
        Z                   = -20,
        Y                   = -134350,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x120,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -139690,
        Z                   = 0,
        Y                   = -154320,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -121830,
        Z                   = -20,
        Y                   = -180660,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x125,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -129880,
        Z                   = 0,
        Y                   = -195360,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -162770,
        Z                   = -230,
        Y                   = -194700,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x122,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -189220,
        Z                   = -40,
        Y                   = -199700,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x122,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -128580,
        Z                   = 0,
        Y                   = -225570,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x120,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -145980,
        Y                   = -2000,
        Z                   = -238720,
        Range               = -127290,
        Unknown_10          = 0x802,
        Unknown_14          = 0xFFFC4492,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -145200,
        TriggerZ            = 0,
        TriggerY            = -202770,
        TriggerRange        = 1500,
        ActorX              = -145200,
        ActorZ              = 1400,
        ActorY              = -202770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -141090,
        TriggerZ            = 0,
        TriggerY            = -211150,
        TriggerRange        = 1500,
        ActorX              = -141090,
        ActorZ              = 1500,
        ActorY              = -211150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B6",          # 00, 0
        "Function_1_2B7",          # 01, 1
        "Function_2_2F8",          # 02, 2
        "Function_3_30E",          # 03, 3
        "Function_4_5D3",          # 04, 4
        "Function_5_62E",          # 05, 5
    )


    def Function_0_2B6(): pass

    label("Function_0_2B6")

    Return()

    # Function_0_2B6 end

    def Function_1_2B7(): pass

    label("Function_1_2B7")

    OP_16(0x2, 0xFA0, 0xFFFBA2D0, 0xFFFB50C8, 0x3001D)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EXEC_OP, "OP_29(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x18, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F7")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_2F7")

    Return()

    # Function_1_2B7 end

    def Function_2_2F8(): pass

    label("Function_2_2F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2F8")

    label("loc_30D")

    Return()

    # Function_2_2F8 end

    def Function_3_30E(): pass

    label("Function_3_30E")

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
        (1, "loc_406"),
        (SWITCH_DEFAULT, "loc_4A0"),
    )


    label("loc_406")

    Fade(1000)
    SetChrPos(0x0, -139820, -100, -236600, 183)
    SetChrPos(0x1, -139820, -100, -236600, 183)
    SetChrPos(0x2, -139820, -100, -236600, 183)
    SetChrPos(0x3, -139820, -100, -236600, 183)
    SetChrPos(0x4, -139820, -100, -236600, 183)
    SetChrPos(0x5, -139820, -100, -236600, 183)
    SetChrPos(0x6, -139820, -100, -236600, 183)
    SetChrPos(0x7, -139820, -100, -236600, 183)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_4A0")

    Battle(0x3FA, 0x0, 0x0, 0x0, 0xFF)
    SetChrPos(0x0, -139820, -100, -236600, 183)
    SetChrPos(0x1, -139820, -100, -236600, 183)
    SetChrPos(0x2, -139820, -100, -236600, 183)
    SetChrPos(0x3, -139820, -100, -236600, 183)
    SetChrPos(0x4, -139820, -100, -236600, 183)
    SetChrPos(0x5, -139820, -100, -236600, 183)
    SetChrPos(0x6, -139820, -100, -236600, 183)
    SetChrPos(0x7, -139820, -100, -236600, 183)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_54E"),
        (1, "loc_551"),
        (SWITCH_DEFAULT, "loc_554"),
    )


    label("loc_54E")

    EventEnd(0x0)
    Return()

    label("loc_551")

    OP_B4(0x0)
    Return()

    label("loc_554")

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
            "成功消灭了安塞尔新街中被通缉的魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x18, 0x4, 0x10)
    OP_28(0x18, 0x1, 0x1)
    OP_A2(0x386)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_30E end

    def Function_4_5D3(): pass

    label("Function_4_5D3")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西　琥珀之塔\x01",
            "※魔兽很多，危险！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_5D3 end

    def Function_5_62E(): pass

    label("Function_5_62E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南　瓦雷利亚湖湖畔\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_62E end

    SaveToFile()

Try(main)
