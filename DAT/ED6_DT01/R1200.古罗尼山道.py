from ED6ScenarioHelper import *

def main():
    # 古罗尼山道

    CreateScenaFile(
        FileName            = 'R1200   ._SN',
        MapName             = 'Bose',
        Location            = 'R1200.x',
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
        '柏斯方向',                             # 10
    )

    DeclEntryPoint(
        Unknown_00              = -116000,
        Unknown_04              = 0,
        Unknown_08              = -69000,
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
        Unknown_30              = 315,
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
        X                   = -205290,
        Z                   = -150,
        Y                   = -15350,
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
        X                   = -91180,
        Z                   = 0,
        Y                   = -70080,
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
        X                   = -143880,
        Z                   = -10,
        Y                   = -61790,
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
        X                   = -158850,
        Z                   = -20,
        Y                   = -50270,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -173400,
        Z                   = 20,
        Y                   = -48970,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -167290,
        Z                   = 0,
        Y                   = -1300,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -128190,
        TriggerZ            = 0,
        TriggerY            = -64590,
        TriggerRange        = 1500,
        ActorX              = -128190,
        ActorZ              = 1500,
        ActorY              = -64590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -192620,
        TriggerZ            = 0,
        TriggerY            = -46900,
        TriggerRange        = 1000,
        ActorX              = -192620,
        ActorZ              = 1000,
        ActorY              = -46900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F2",          # 00, 0
        "Function_1_1F3",          # 01, 1
        "Function_2_21F",          # 02, 2
        "Function_3_29D",          # 03, 3
    )


    def Function_0_1F2(): pass

    label("Function_0_1F2")

    Return()

    # Function_0_1F2 end

    def Function_1_1F3(): pass

    label("Function_1_1F3")

    OP_16(0x2, 0xFA0, 0xFFFBC210, 0xFFFD5080, 0x30019)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217")
    OP_6F(0x0, 0)
    Jump("loc_21E")

    label("loc_217")

    OP_6F(0x0, 60)

    label("loc_21E")

    Return()

    # Function_1_1F3 end

    def Function_2_21F(): pass

    label("Function_2_21F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东　柏斯市\x01",
            "西　拉文努村　　２８７塞尔矩\x01",
            "　　古罗尼山顶　４４１塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_2_21F end

    def Function_3_29D(): pass

    label("Function_3_29D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_398")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_317")
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
    OP_A2(0x38A)
    Jump("loc_395")

    label("loc_317")

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
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_395")

    Jump("loc_3DC")

    label("loc_398")

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
    OP_83(0xF, 0x7D)

    label("loc_3DC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_29D end

    SaveToFile()

Try(main)
