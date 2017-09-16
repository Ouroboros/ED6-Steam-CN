from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2610   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2610.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2610   ._SN',
            'ED6_DT01/T2610_1 ._SN',
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
        'ED6_DT06/CH20021 ._CH',             # 00
        'ED6_DT09/CH10530 ._CH',             # 01
        'ED6_DT09/CH10531 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT06/CH20021P._CP',             # 00
        'ED6_DT09/CH10530P._CP',             # 01
        'ED6_DT09/CH10531P._CP',             # 02
    )

    DeclMonster(
        X                   = 510,
        Z                   = 0,
        Y                   = 10520,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 129,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 1189,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33210,
        Z                   = 250,
        Y                   = 28100,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 129,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 1190,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8140,
        Z                   = 0,
        Y                   = 20000,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 129,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 1191,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -93270,
        Z                   = 0,
        Y                   = 1680,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 129,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 1192,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -80260,
        TriggerZ            = 250,
        TriggerY            = 31430,
        TriggerRange        = 1000,
        ActorX              = -80210,
        ActorZ              = 250,
        ActorY              = 32080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_156",          # 00, 0
        "Function_1_157",          # 01, 1
        "Function_2_242",          # 02, 2
    )


    def Function_0_156(): pass

    label("Function_0_156")

    Return()

    # Function_0_156 end

    def Function_1_157(): pass

    label("Function_1_157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_178")
    OP_B1("t2610_y")
    Jump("loc_181")

    label("loc_178")

    OP_B1("t2610_n")

    label("loc_181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2000)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB")
    ClearChrFlags(0x8, 0x80)

    label("loc_1AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B8")
    ClearChrFlags(0x9, 0x80)

    label("loc_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5")
    ClearChrFlags(0xA, 0x80)

    label("loc_1C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2")
    ClearChrFlags(0xB, 0x80)

    label("loc_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2000)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_228")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 5)), scpexpr(EXPR_END)), "loc_228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 6)), scpexpr(EXPR_END)), "loc_228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 7)), scpexpr(EXPR_END)), "loc_228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 0)), scpexpr(EXPR_END)), "loc_228")
    OP_28(0x27, 0x1, 0x4000)
    OP_28(0x3D, 0x1, 0x100)
    OP_2C(0x3D, 0x3E8)
    OP_2B(0x3D, 0x3)
    Event(1, 0)

    label("loc_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A")
    OP_6F(0xB, 0)
    Jump("loc_241")

    label("loc_23A")

    OP_6F(0xB, 60)

    label("loc_241")

    Return()

    # Function_1_157 end

    def Function_2_242(): pass

    label("Function_2_242")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_2BC")
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
    OP_A2(0x4CA)
    Jump("loc_33A")

    label("loc_2BC")

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
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_33A")

    Jump("loc_394")

    label("loc_33D")

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
    OP_83(0xF, 0xA3)

    label("loc_394")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_242 end

    SaveToFile()

Try(main)
