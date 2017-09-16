from ED6ScenarioHelper import *

def main():
    # 安塞尔新街

    CreateScenaFile(
        FileName            = 'R1400   ._SN',
        MapName             = 'Bose',
        Location            = 'R1400.x',
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
        '柏斯方向',                             # 9
        '瓦雷利亚湖畔方向',                     # 10
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
    )

    DeclNpc(
        X                   = -153950,
        Z                   = 0,
        Y                   = 68430,
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
        X                   = -140970,
        Z                   = -10,
        Y                   = -85530,
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
        X                   = -159990,
        Z                   = 0,
        Y                   = 15330,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -162450,
        Z                   = -30,
        Y                   = 220,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -181290,
        Z                   = 50,
        Y                   = -41120,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -147870,
        Z                   = 20,
        Y                   = -37440,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -160560,
        TriggerZ            = 0,
        TriggerY            = 35590,
        TriggerRange        = 1500,
        ActorX              = -160560,
        ActorZ              = 1500,
        ActorY              = 35590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1CE",          # 00, 0
        "Function_1_1CF",          # 01, 1
        "Function_2_1E2",          # 02, 2
    )


    def Function_0_1CE(): pass

    label("Function_0_1CE")

    Return()

    # Function_0_1CE end

    def Function_1_1CF(): pass

    label("Function_1_1CF")

    OP_16(0x2, 0xFA0, 0xFFFB9EE8, 0xFFFDF878, 0x3001C)
    Return()

    # Function_1_1CF end

    def Function_2_1E2(): pass

    label("Function_2_1E2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　柏斯市\x01",
            "南　瓦雷利亚湖畔　２００塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_2_1E2 end

    SaveToFile()

Try(main)
