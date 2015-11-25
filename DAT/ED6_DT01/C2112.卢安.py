from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'C2112   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2112.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'ED6_DT09/CH10560 ._CH',             # 00
        'ED6_DT09/CH10561 ._CH',             # 01
        'ED6_DT09/CH10570 ._CH',             # 02
        'ED6_DT09/CH10571 ._CH',             # 03
        'ED6_DT09/CH10580 ._CH',             # 04
        'ED6_DT09/CH10581 ._CH',             # 05
        'ED6_DT09/CH10590 ._CH',             # 06
        'ED6_DT09/CH10591 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10560P._CP',             # 00
        'ED6_DT09/CH10561P._CP',             # 01
        'ED6_DT09/CH10570P._CP',             # 02
        'ED6_DT09/CH10571P._CP',             # 03
        'ED6_DT09/CH10580P._CP',             # 04
        'ED6_DT09/CH10581P._CP',             # 05
        'ED6_DT09/CH10590P._CP',             # 06
        'ED6_DT09/CH10591P._CP',             # 07
    )

    DeclMonster(
        X                   = -150,
        Z                   = 0,
        Y                   = -10,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1B9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21120,
        Z                   = 0,
        Y                   = 3940,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1BB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21420,
        Z                   = 0,
        Y                   = 3700,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1BB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -21770,
        TriggerZ            = 0,
        TriggerY            = -2940,
        TriggerRange        = 1000,
        ActorX              = -21820,
        ActorZ              = 0,
        ActorY              = -3560,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22320,
        TriggerZ            = 0,
        TriggerY            = -80,
        TriggerRange        = 1000,
        ActorX              = 22880,
        ActorZ              = 0,
        ActorY              = -170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_186",          # 00, 0
        "Function_1_187",          # 01, 1
        "Function_2_1BA",          # 02, 2
        "Function_3_2ED",          # 03, 3
    )


    def Function_0_186(): pass

    label("Function_0_186")

    Return()

    # Function_0_186 end

    def Function_1_187(): pass

    label("Function_1_187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199")
    OP_6F(0x0, 0)
    Jump("loc_1A0")

    label("loc_199")

    OP_6F(0x0, 60)

    label("loc_1A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2")
    OP_6F(0x1, 0)
    Jump("loc_1B9")

    label("loc_1B2")

    OP_6F(0x1, 60)

    label("loc_1B9")

    Return()

    # Function_1_187 end

    def Function_2_1BA(): pass

    label("Function_2_1BA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_230")
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
    OP_A2(0x4A9)
    Jump("loc_2A6")

    label("loc_230")

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

    label("loc_2A6")

    Jump("loc_2DF")

    label("loc_2A9")

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
    OP_83(0xF, 0x1B)

    label("loc_2DF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1BA end

    def Function_3_2ED(): pass

    label("Function_3_2ED")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_363")
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
    OP_A2(0x4AA)
    Jump("loc_3D9")

    label("loc_363")

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

    label("loc_3D9")

    Jump("loc_412")

    label("loc_3DC")

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
    OP_83(0xF, 0x1C)

    label("loc_412")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2ED end

    SaveToFile()

Try(main)
