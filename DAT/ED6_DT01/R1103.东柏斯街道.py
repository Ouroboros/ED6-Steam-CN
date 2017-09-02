from ED6ScenarioHelper import *

def main():
    # 东柏斯街道

    CreateScenaFile(
        FileName            = 'R1103   ._SN',
        MapName             = 'Bose',
        Location            = 'R1103.x',
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
        '威尔特桥·关所方向',                   # 9
        '柏斯方向',                             # 10
        '钢壁之路方向',                         # 11
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
    )

    DeclNpc(
        X                   = -209870,
        Z                   = 0,
        Y                   = -15970,
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
        X                   = -344620,
        Z                   = 0,
        Y                   = 11780,
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
        X                   = -250290,
        Z                   = 0,
        Y                   = 30060,
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
        X                   = -112490,
        Z                   = 20,
        Y                   = -60920,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -254420,
        TriggerZ            = 0,
        TriggerY            = 230,
        TriggerRange        = 1500,
        ActorX              = -254420,
        ActorZ              = 1500,
        ActorY              = 230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -258970,
        TriggerZ            = 0,
        TriggerY            = -2500,
        TriggerRange        = 1500,
        ActorX              = -258970,
        ActorZ              = 1500,
        ActorY              = -2500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1AE",          # 00, 0
        "Function_1_1AF",          # 01, 1
        "Function_2_1C2",          # 02, 2
        "Function_3_212",          # 03, 3
    )


    def Function_0_1AE(): pass

    label("Function_0_1AE")

    Return()

    # Function_0_1AE end

    def Function_1_1AF(): pass

    label("Function_1_1AF")

    OP_16(0x2, 0xFA0, 0xFFF9BE70, 0xFFFE17B8, 0x30018)
    Return()

    # Function_1_1AF end

    def Function_2_1C2(): pass

    label("Function_2_1C2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　哈肯大门　２１０塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_2_1C2 end

    def Function_3_212(): pass

    label("Function_3_212")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西　柏斯市\x01",
            "东　威尔特桥　４２０塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_212 end

    SaveToFile()

Try(main)
