from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3511   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3511.x',
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
        'ED6_DT09/CH10710 ._CH',             # 00
        'ED6_DT09/CH10711 ._CH',             # 01
        'ED6_DT09/CH10720 ._CH',             # 02
        'ED6_DT09/CH10721 ._CH',             # 03
        'ED6_DT09/CH10730 ._CH',             # 04
        'ED6_DT09/CH10731 ._CH',             # 05
        'ED6_DT09/CH10740 ._CH',             # 06
        'ED6_DT09/CH10741 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10710P._CP',             # 00
        'ED6_DT09/CH10711P._CP',             # 01
        'ED6_DT09/CH10720P._CP',             # 02
        'ED6_DT09/CH10721P._CP',             # 03
        'ED6_DT09/CH10730P._CP',             # 04
        'ED6_DT09/CH10731P._CP',             # 05
        'ED6_DT09/CH10740P._CP',             # 06
        'ED6_DT09/CH10741P._CP',             # 07
    )

    DeclMonster(
        X                   = -140,
        Z                   = 0,
        Y                   = 5770,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -3400,
        TriggerZ            = 0,
        TriggerY            = -22930,
        TriggerRange        = 1000,
        ActorX              = -3400,
        ActorZ              = 0,
        ActorY              = -23590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3430,
        TriggerZ            = 0,
        TriggerY            = -22930,
        TriggerRange        = 1000,
        ActorX              = 3490,
        ActorZ              = 0,
        ActorY              = -23630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4760,
        TriggerZ            = 0,
        TriggerY            = 22800,
        TriggerRange        = 1000,
        ActorX              = 4760,
        ActorZ              = 0,
        ActorY              = 23420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4540,
        TriggerZ            = 0,
        TriggerY            = 22820,
        TriggerRange        = 1000,
        ActorX              = -4630,
        ActorZ              = 0,
        ActorY              = 23480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_196",          # 00, 0
        "Function_1_19F",          # 01, 1
        "Function_2_204",          # 02, 2
        "Function_3_343",          # 03, 3
        "Function_4_499",          # 04, 4
        "Function_5_5DE",          # 05, 5
    )


    def Function_0_196(): pass

    label("Function_0_196")

    SetMapFlags(0x40000000)
    AddParty(0xFF, 0xFF)
    Return()

    # Function_0_196 end

    def Function_1_19F(): pass

    label("Function_1_19F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1")
    OP_6F(0x0, 0)
    Jump("loc_1B8")

    label("loc_1B1")

    OP_6F(0x0, 60)

    label("loc_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA")
    OP_6F(0x1, 0)
    Jump("loc_1D1")

    label("loc_1CA")

    OP_6F(0x1, 60)

    label("loc_1D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3")
    OP_6F(0x2, 0)
    Jump("loc_1EA")

    label("loc_1E3")

    OP_6F(0x2, 60)

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC")
    OP_6F(0x3, 0)
    Jump("loc_203")

    label("loc_1FC")

    OP_6F(0x3, 60)

    label("loc_203")

    Return()

    # Function_1_19F end

    def Function_2_204(): pass

    label("Function_2_204")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_27A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x5A7)
    Jump("loc_2F0")

    label("loc_27A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_2F0")

    Jump("loc_335")

    label("loc_2F3")

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
    OP_83(0xF, 0x2C)

    label("loc_335")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_204 end

    def Function_3_343(): pass

    label("Function_3_343")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_3BA")
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
    OP_A2(0x5A8)
    Jump("loc_432")

    label("loc_3BA")

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
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_432")

    Jump("loc_48B")

    label("loc_435")

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
    OP_83(0xF, 0x2D)

    label("loc_48B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_343 end

    def Function_4_499(): pass

    label("Function_4_499")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_588")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_50F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x5A9)
    Jump("loc_585")

    label("loc_50F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_585")

    Jump("loc_5D0")

    label("loc_588")

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
    OP_83(0xF, 0x2E)

    label("loc_5D0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_499 end

    def Function_5_5DE(): pass

    label("Function_5_5DE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xFA, 1)"), scpexpr(EXPR_END)), "loc_655")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "黑大衣\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x5AA)
    Jump("loc_6CD")

    label("loc_655")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "黑大衣\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "黑大衣\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_6CD")

    Jump("loc_701")

    label("loc_6D0")

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
    OP_83(0xF, 0x2F)

    label("loc_701")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_5DE end

    SaveToFile()

Try(main)
