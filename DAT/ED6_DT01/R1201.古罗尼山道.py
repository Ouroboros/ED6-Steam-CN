from ED6ScenarioHelper import *

def main():
    # 古罗尼山道

    CreateScenaFile(
        FileName            = 'R1201   ._SN',
        MapName             = 'Bose',
        Location            = 'R1201.x',
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
        '古罗尼山道方向',                       # 9
        '拉文努山道方向',                       # 10
        '柏斯方向',                             # 11
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
        'ED6_DT09/CH10311 ._CH',             # 05
        'ED6_DT09/CH10550 ._CH',             # 06
        'ED6_DT09/CH10550 ._CH',             # 07
        'ED6_DT09/CH10870 ._CH',             # 08
        'ED6_DT09/CH10871 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10320P._CP',             # 00
        'ED6_DT09/CH10321P._CP',             # 01
        'ED6_DT09/CH10350P._CP',             # 02
        'ED6_DT09/CH10351P._CP',             # 03
        'ED6_DT09/CH10310P._CP',             # 04
        'ED6_DT09/CH10311P._CP',             # 05
        'ED6_DT09/CH10550P._CP',             # 06
        'ED6_DT09/CH10550P._CP',             # 07
        'ED6_DT09/CH10870P._CP',             # 08
        'ED6_DT09/CH10871P._CP',             # 09
    )

    DeclNpc(
        X                   = -348670,
        Z                   = 150,
        Y                   = 8790,
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
        X                   = -251150,
        Z                   = 0,
        Y                   = 36410,
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
        X                   = -206940,
        Z                   = 0,
        Y                   = -15170,
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
        X                   = -245780,
        Z                   = 10,
        Y                   = -13290,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -283410,
        Z                   = 510,
        Y                   = 3500,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -297320,
        Z                   = -10,
        Y                   = -50,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -321660,
        Z                   = 0,
        Y                   = 7860,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xFA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -244460,
        Y                   = -1000,
        Z                   = 18100,
        Range               = -258140,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x5BEA,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    DeclActor(
        TriggerX            = -254930,
        TriggerZ            = 0,
        TriggerY            = 140,
        TriggerRange        = 1500,
        ActorX              = -254930,
        ActorZ              = 1300,
        ActorY              = 140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -261790,
        TriggerZ            = 0,
        TriggerY            = -2900,
        TriggerRange        = 1500,
        ActorX              = -261790,
        ActorZ              = 1500,
        ActorY              = -2900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_232",          # 00, 0
        "Function_1_233",          # 01, 1
        "Function_2_246",          # 02, 2
        "Function_3_80F",          # 03, 3
        "Function_4_865",          # 04, 4
    )


    def Function_0_232(): pass

    label("Function_0_232")

    Return()

    # Function_0_232 end

    def Function_1_233(): pass

    label("Function_1_233")

    OP_16(0x2, 0xFA0, 0xFFF9E580, 0xFFFE0FE8, 0x3001A)
    Return()

    # Function_1_233 end

    def Function_2_246(): pass

    label("Function_2_246")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80E")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_381")
    OP_A2(0x0)
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(
        0x103,
        (
            "#020F艾丝蒂尔，走错路了。\x01",
            "这边是拉文努山道啊。\x02\x03",
            "古罗尼连峰\x01",
            "要继续往西走才对。\x02\x03",
            "要去拉文努村的话，\x01",
            "等把委托人平安送到目的地后再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#000F好～知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_451")

    label("loc_381")


    ChrTalk(
        0x103,
        (
            "#020F走错路了。\x01",
            "这边是拉文努山道啊。\x02\x03",
            "古罗尼连峰\x01",
            "要继续往西走才对。\x02\x03",
            "要去拉文努村的话，\x01",
            "等把委托人平安送到目的地后再说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_451")

    Jump("loc_7F3")

    label("loc_454")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568")
    OP_A2(0x0)
    TurnDirection(0x103, 0x102, 0)

    ChrTalk(
        0x103,
        (
            "#020F约修亚，走错路了。\x01",
            "这边是拉文努山道啊。\x02\x03",
            "古罗尼连峰\x01",
            "要继续往西走才对。\x02\x03",
            "要去拉文努村的话，\x01",
            "等把委托人平安送到目的地后再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        "#010F好，知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_638")

    label("loc_568")


    ChrTalk(
        0x103,
        (
            "#020F走错路了。\x01",
            "这边是拉文努山道啊。\x02\x03",
            "古罗尼连峰\x01",
            "要继续往西走才对。\x02\x03",
            "要去拉文努村的话，\x01",
            "等把委托人平安送到目的地后再说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_638")

    Jump("loc_7F3")

    label("loc_63B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72B")
    OP_A2(0x0)

    ChrTalk(
        0x103,
        (
            "#023F啊……\x01",
            "这边是拉文努山道啊。\x02\x03",
            "古罗尼连峰\x01",
            "要继续往西走才对。\x02\x03",
            "要去拉文努村的话，\x01",
            "等把委托人平安送到目的地后再说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F3")

    label("loc_72B")


    ChrTalk(
        0x103,
        (
            "#020F这边是拉文努山道啊。\x02\x03",
            "古罗尼连峰\x01",
            "要继续往西走才对。\x02\x03",
            "要去拉文努村的话，\x01",
            "等把委托人平安送到目的地后再说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F3")

    OP_90(0x0, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_80E")

    Return()

    # Function_2_246 end

    def Function_3_80F(): pass

    label("Function_3_80F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　拉文努村　　１４７塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_80F end

    def Function_4_865(): pass

    label("Function_4_865")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东　柏斯市　　　１４０塞尔矩\x01",
            "西　古罗尼山顶　３０１塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_865 end

    SaveToFile()

Try(main)
