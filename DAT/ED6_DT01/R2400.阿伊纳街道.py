from ED6ScenarioHelper import *

def main():
    # 阿伊纳街道

    CreateScenaFile(
        FileName            = 'R2400   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2400.x',
        MapIndex            = 103,
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
        '卢安方向',                             # 9
        '艾尔·雷登关所方向',                   # 10
        '绀碧之塔方向',                         # 11
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
        Unknown_3A              = 103,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10520 ._CH',             # 00
        'ED6_DT09/CH10521 ._CH',             # 01
        'ED6_DT09/CH10340 ._CH',             # 02
        'ED6_DT09/CH10341 ._CH',             # 03
        'ED6_DT09/CH11040 ._CH',             # 04
        'ED6_DT09/CH11041 ._CH',             # 05
        'ED6_DT09/CH11070 ._CH',             # 06
        'ED6_DT09/CH11071 ._CH',             # 07
        'ED6_DT09/CH11080 ._CH',             # 08
        'ED6_DT09/CH11081 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10520P._CP',             # 00
        'ED6_DT09/CH10521P._CP',             # 01
        'ED6_DT09/CH10340P._CP',             # 02
        'ED6_DT09/CH10341P._CP',             # 03
        'ED6_DT09/CH11040P._CP',             # 04
        'ED6_DT09/CH11041P._CP',             # 05
        'ED6_DT09/CH11070P._CP',             # 06
        'ED6_DT09/CH11071P._CP',             # 07
        'ED6_DT09/CH11080P._CP',             # 08
        'ED6_DT09/CH11081P._CP',             # 09
    )

    DeclNpc(
        X                   = -23690,
        Z                   = 0,
        Y                   = 116780,
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
        X                   = 15400,
        Z                   = 0,
        Y                   = 4440,
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
        X                   = -104100,
        Z                   = 10,
        Y                   = 74970,
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
        X                   = -14830,
        Z                   = -70,
        Y                   = 77800,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1AA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28100,
        Z                   = 190,
        Y                   = 43720,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1B0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -15760,
        Z                   = -60,
        Y                   = 37690,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1AB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28480,
        Z                   = 130,
        Y                   = 9940,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1B2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14420,
        Z                   = 200,
        Y                   = 18840,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1B3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40650,
        Z                   = 450,
        Y                   = 58610,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1AF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -66830,
        Z                   = 20,
        Y                   = 39070,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1B3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -31880,
        TriggerZ            = 0,
        TriggerY            = 74800,
        TriggerRange        = 1500,
        ActorX              = -31880,
        ActorZ              = 1400,
        ActorY              = 74800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28300,
        TriggerZ            = 0,
        TriggerY            = 68920,
        TriggerRange        = 1500,
        ActorX              = -28300,
        ActorZ              = 1500,
        ActorY              = 68920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_266",          # 00, 0
        "Function_1_267",          # 01, 1
        "Function_2_27A",          # 02, 2
        "Function_3_2D7",          # 03, 3
    )


    def Function_0_266(): pass

    label("Function_0_266")

    Return()

    # Function_0_266 end

    def Function_1_267(): pass

    label("Function_1_267")

    OP_16(0x2, 0xFA0, 0xFFFD73A8, 0xFFFECF50, 0x30023)
    Return()

    # Function_1_267 end

    def Function_2_27A(): pass

    label("Function_2_27A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西　绀碧之塔\x01",
            "※魔兽很多，危险！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_2_27A end

    def Function_3_2D7(): pass

    label("Function_3_2D7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　卢安市　　　　１０５塞尔矩\x01",
            "南　艾尔·雷登　　　７０塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_2D7 end

    SaveToFile()

Try(main)
