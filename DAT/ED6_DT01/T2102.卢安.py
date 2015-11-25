from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2102   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2102   ._SN',
            'ED6_DT01/T2102_1 ._SN',
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
        '尤莉亚中尉',                           # 9
        '奈尔',                                 # 10
        '基库',                                 # 11
        '理查德上校',                           # 12
        '凯诺娜上尉',                           # 13
        '西蒙',                                 # 14
        '照相机',                               # 15
        '哈尔德',                               # 16
        '爱德望',                               # 17
        '库莱泽',                               # 18
        '萨马里奥',                             # 19
        '豆豆',                                 # 20
        '亲卫队员',                             # 21
        '亲卫队员',                             # 22
        '亲卫队员',                             # 23
        '亲卫队员',                             # 24
        '亲卫队员',                             # 25
        '亲卫队员',                             # 26
        '亲卫队员',                             # 27
        '亲卫队员',                             # 28
        '亲卫队员',                             # 29
        '亲卫队员',                             # 30
        '亲卫队员',                             # 31
        '亲卫队员',                             # 32
        '亲卫队员',                             # 33
        '亲卫队员',                             # 34
        '亲卫队员',                             # 35
        '亲卫队员',                             # 36
        '\u3000',                               # 37
        '\u3000',                               # 38
        '卢安市·北街区',                       # 39
    )

    DeclEntryPoint(
        Unknown_00              = 94000,
        Unknown_04              = 0,
        Unknown_08              = 80000,
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
        'ED6_DT07/CH02323 ._CH',             # 00
        'ED6_DT07/CH02060 ._CH',             # 01
        'ED6_DT07/CH02090 ._CH',             # 02
        'ED6_DT07/CH02030 ._CH',             # 03
        'ED6_DT07/CH02100 ._CH',             # 04
        'ED6_DT07/CH01140 ._CH',             # 05
        'ED6_DT07/CH01120 ._CH',             # 06
        'ED6_DT07/CH01290 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01470 ._CH',             # 09
        'ED6_DT07/CH01320 ._CH',             # 0A
        'ED6_DT06/CH20127 ._CH',             # 0B
        'ED6_DT06/CH20128 ._CH',             # 0C
        'ED6_DT06/CH20129 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02323P._CP',             # 00
        'ED6_DT07/CH02060P._CP',             # 01
        'ED6_DT07/CH02090P._CP',             # 02
        'ED6_DT07/CH02030P._CP',             # 03
        'ED6_DT07/CH02100P._CP',             # 04
        'ED6_DT07/CH01140P._CP',             # 05
        'ED6_DT07/CH01120P._CP',             # 06
        'ED6_DT07/CH01290P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01470P._CP',             # 09
        'ED6_DT07/CH01320P._CP',             # 0A
        'ED6_DT06/CH20127P._CP',             # 0B
        'ED6_DT06/CH20128P._CP',             # 0C
        'ED6_DT06/CH20129P._CP',             # 0D
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 6130,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 47780,
        Z                   = 0,
        Y                   = 39390,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 47780,
        Z                   = 0,
        Y                   = 39390,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 111490,
        Z                   = 4150,
        Y                   = 81190,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 147300,
        Z                   = 8200,
        Y                   = 95200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 101700,
        Z                   = 0,
        Y                   = 83800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 134200,
        Z                   = 8200,
        Y                   = 93000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 140500,
        Z                   = 6100,
        Y                   = 100500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 126600,
        Z                   = 8200,
        Y                   = 95200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 134940,
        Z                   = 8050,
        Y                   = 85090,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 129360,
        Z                   = 8050,
        Y                   = 85070,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 130139,
        Z                   = 8050,
        Y                   = 85100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 134140,
        Z                   = 8050,
        Y                   = 85130,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 133300,
        Z                   = 8050,
        Y                   = 83500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 133300,
        Z                   = 8050,
        Y                   = 82200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 133300,
        Z                   = 8050,
        Y                   = 80900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 133300,
        Z                   = 8050,
        Y                   = 79600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 132100,
        Z                   = 8050,
        Y                   = 83500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 132100,
        Z                   = 8050,
        Y                   = 82200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 132100,
        Z                   = 8050,
        Y                   = 80900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 132100,
        Z                   = 8050,
        Y                   = 79600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 130900,
        Z                   = 8050,
        Y                   = 83500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 130900,
        Z                   = 8050,
        Y                   = 82200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 130900,
        Z                   = 8050,
        Y                   = 80900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 130900,
        Z                   = 8050,
        Y                   = 79600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 71170,
        Z                   = 0,
        Y                   = 80860,
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


    DeclActor(
        TriggerX            = 114900,
        TriggerZ            = 0,
        TriggerY            = 101600,
        TriggerRange        = 2000,
        ActorX              = 114900,
        ActorZ              = 1500,
        ActorY              = 101600,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 100400,
        TriggerZ            = 0,
        TriggerY            = 83700,
        TriggerRange        = 1000,
        ActorX              = 101700,
        ActorZ              = 1500,
        ActorY              = 83800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 108610,
        TriggerZ            = 6150,
        TriggerY            = 96910,
        TriggerRange        = 800,
        ActorX              = 108610,
        ActorZ              = 8350,
        ActorY              = 96910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 127080,
        TriggerZ            = 6150,
        TriggerY            = 100740,
        TriggerRange        = 800,
        ActorX              = 127080,
        ActorZ              = 8350,
        ActorY              = 100740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 140870,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 140870,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 149330,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 149330,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 103030,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 103030,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 96980,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 96980,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_61A",          # 00, 0
        "Function_1_805",          # 01, 1
        "Function_2_8BF",          # 02, 2
        "Function_3_A3C",          # 03, 3
        "Function_4_AEE",          # 04, 4
        "Function_5_C0A",          # 05, 5
        "Function_6_C8F",          # 06, 6
        "Function_7_1596",         # 07, 7
        "Function_8_1BA8",         # 08, 8
        "Function_9_2210",         # 09, 9
        "Function_10_271A",        # 0A, 10
        "Function_11_472D",        # 0B, 11
        "Function_12_4776",        # 0C, 12
        "Function_13_47AB",        # 0D, 13
        "Function_14_47ED",        # 0E, 14
        "Function_15_4836",        # 0F, 15
        "Function_16_4887",        # 10, 16
        "Function_17_48F0",        # 11, 17
        "Function_18_496F",        # 12, 18
    )


    def Function_0_61A(): pass

    label("Function_0_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_63A")
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x13, 147500, 8150, 95630, 90)
    Jump("loc_7C9")

    label("loc_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_65A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x13, 147500, 8150, 95630, 90)
    Jump("loc_7C9")

    label("loc_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_67F")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x13, 135010, 8150, 94960, 0)
    Jump("loc_7C9")

    label("loc_67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_6C1")
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, 136900, 6100, 101800, 135)
    SetChrPos(0x13, 137600, 6100, 99400, 0)
    SetChrPos(0x12, 139000, 6100, 101400, 270)
    Jump("loc_7C9")

    label("loc_6C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_70D")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 96700, 1000, 90100, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 98600, 0, 81460, 45)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x13, 159290, 0, 107030, 90)
    Jump("loc_7C9")

    label("loc_70D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_73E")
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, 132010, 8360, 93010, 90)
    SetChrPos(0x13, 132950, 8150, 96370, 180)
    Jump("loc_7C9")

    label("loc_73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_76F")
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, 129600, 8200, 94200, 0)
    SetChrPos(0x13, 129600, 8200, 96800, 180)
    Jump("loc_7C9")

    label("loc_76F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_78A")
    SetChrPos(0x13, 159290, 0, 107030, 90)
    Jump("loc_7C9")

    label("loc_78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_7C9")
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, 131500, 8150, 97650, 180)
    SetChrPos(0x13, 130539, 8150, 96030, 45)
    SetChrPos(0x12, 132620, 8150, 95740, 315)

    label("loc_7C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7E8")
    OP_64(0x0, 0x1)

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_804")
    OP_A3(0x3FA)
    Event(0, 10)
    OP_B1("t2102_1")
    OP_71(0xA, 0x4)

    label("loc_804")

    Return()

    # Function_0_61A end

    def Function_1_805(): pass

    label("Function_1_805")

    OP_16(0x2, 0xFA0, 0x4E20, 0xFFFF63C0, 0x30049)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_838")
    OP_B1("t2102_y")
    Jump("loc_89A")

    label("loc_838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_850")
    OP_B1("t2102_0")
    Jump("loc_89A")

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_868")
    OP_B1("t2102_2")
    Jump("loc_89A")

    label("loc_868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_880")
    OP_B1("t2102_0")
    Jump("loc_89A")

    label("loc_880")

    OP_B1("t2102_0")
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_6F(0x7, 100)

    label("loc_89A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B9")
    OP_64(0x0, 0x1)

    label("loc_8B9")

    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_805 end

    def Function_2_8BF(): pass

    label("Function_2_8BF")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E4")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_A26")

    label("loc_8E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FD")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_A26")

    label("loc_8FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_916")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_A26")

    label("loc_916")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_A26")

    label("loc_92F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_948")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_A26")

    label("loc_948")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_961")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_A26")

    label("loc_961")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_A26")

    label("loc_97A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_993")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_A26")

    label("loc_993")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AC")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_A26")

    label("loc_9AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C5")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_A26")

    label("loc_9C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DE")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_A26")

    label("loc_9DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_A26")

    label("loc_9F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A10")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_A26")

    label("loc_A10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A26")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_A26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A3B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_A26")

    label("loc_A3B")

    Return()

    # Function_2_8BF end

    def Function_3_A3C(): pass

    label("Function_3_A3C")

    TalkBegin(0x9)

    ChrTalk(
        0xFE,
        (
            "#140F哟，\x01",
            "我准备回格兰赛尔办点事情。\x02\x03",
            "现在正在等着看看有没有人来退票。\x01",
            "　\x02\x03",
            "等事情办完我会马上回卢安来的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_3_A3C end

    def Function_4_AEE(): pass

    label("Function_4_AEE")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB7")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "哎呀，回到柏斯之后\x01",
            "还有一堆事情要等着我去处理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "愉快的假期总是那么转瞬即逝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定要把心思转回来，\x01",
            "不然又要被米拉诺小姐骂了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C06")

    label("loc_BB7")


    ChrTalk(
        0xFE,
        (
            "哎呀，回到柏斯之后\x01",
            "还有一堆事情要等着我去处理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C06")

    TalkEnd(0xD)
    Return()

    # Function_4_AEE end

    def Function_5_C0A(): pass

    label("Function_5_C0A")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6B")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "好了……\x01",
            "要去办理搭乘手续呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能准时在定期船起飞时上船，\x01",
            "那真是万幸啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_C6B")


    ChrTalk(
        0xFE,
        (
            "好了……\x01",
            "要去办理搭乘手续呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8B")

    TalkEnd(0xF)
    Return()

    # Function_5_C0A end

    def Function_6_C8F(): pass

    label("Function_6_C8F")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_E55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBB")
    OP_A2(0x3)

    ChrTalk(
        0x10,
        (
            "市长干了那么多坏事，\x01",
            "这我万万没有想到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "不过既然已经被逮捕了，\x01",
            "这样也就可以了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "那样的人如果释放了的话，\x01",
            "很可能又会去干坏事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "这都是游击士协会的功劳啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E52")

    label("loc_DBB")


    ChrTalk(
        0x10,
        (
            "市长已经被逮捕了，\x01",
            "这样就可以了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "那样的人如果释放了的话，\x01",
            "很可能又会去干坏事吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E52")

    Jump("loc_1592")

    label("loc_E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_ED8")

    ChrTalk(
        0x10,
        (
            "飞艇公社的总部\x01",
            "设立在王都格兰赛尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "嗯，\x01",
            "记得我只在研修的时候去过那里一次。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1592")

    label("loc_ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_10FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1067")
    OP_A2(0x3)

    ChrTalk(
        0x10,
        (
            "这个空港在建造的时候，\x01",
            "大家为了究竟建在城市的北边还是南边\x01",
            "这个问题争执了很久呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "店铺和观光设施非常多的北街区\x01",
            "从一开始就是最有利的场所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "而且，南街区的仓库\x01",
            "还聚集了一群不良青年，\x01",
            "也不适合在那里兴建吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F7")

    label("loc_1067")


    ChrTalk(
        0x10,
        (
            "这个空港在建造的时候，\x01",
            "大家为了究竟建在城市的北边还是南边\x01",
            "这个问题争执了很久呢。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()

    label("loc_10F7")

    Jump("loc_1592")

    label("loc_10FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_116D")

    ChrTalk(
        0x10,
        (
            "就在刚才，\x01",
            "去柏斯的定期船已经飞走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "今天已经没有其他的航班了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1592")

    label("loc_116D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1223")

    ChrTalk(
        0x10,
        (
            "当天取消的票\x01",
            "会卖给先来的客人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "如果有很紧急的事情，\x01",
            "就算事先没有预约，\x01",
            "也不要放弃，要赶快来询问。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1592")

    label("loc_1223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_133C")

    ChrTalk(
        0x10,
        (
            "在预定乘坐飞艇的那天，\x01",
            "去南街区的时候要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "开合桥拉升了之后，\x01",
            "来不及上飞艇的人可不少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "因为这个时候\x01",
            "拉桥与飞艇出发的时间重合了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1592")

    label("loc_133C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_13B3")

    ChrTalk(
        0x10,
        "今天的天气真好呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "不过，不管天气好还是坏，\x01",
            "我的干劲可永远都是满满的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1592")

    label("loc_13B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_1485")

    ChrTalk(
        0x10,
        (
            "来卢安旅游的客人\x01",
            "近几年来在急剧增加。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "特地来各个观光地\x01",
            "度假休息的人也特别多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1592")

    label("loc_1485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1592")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1569")
    OP_A2(0x3)

    ChrTalk(
        0x10,
        (
            "在定期船停航的时候，\x01",
            "我可是忙个不停应付来问讯的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "通航恢复正常的话，\x01",
            "我还是一样得忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "算了，\x01",
            "反正我越忙就越有干劲！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1592")

    label("loc_1569")


    ChrTalk(
        0x10,
        (
            "算了，\x01",
            "反正我越忙就越有干劲！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1592")

    TalkEnd(0x10)
    Return()

    # Function_6_C8F end

    def Function_7_1596(): pass

    label("Function_7_1596")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_171C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16AF")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "蔡斯的中央工房\x01",
            "邀请我去当客座技师……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但我还是推辞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对我而言，\x01",
            "技术人员的工作的确非常有吸引力，\x01",
            "可我是豆豆的哥哥啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不能只为了自己\x01",
            "而离开卢安啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1719")

    label("loc_16AF")


    ChrTalk(
        0xFE,
        (
            "蔡斯的中央工房\x01",
            "邀请我去当客座技师……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但我还是推辞了。\x02",
    )

    CloseMessageWindow()

    label("loc_1719")

    Jump("loc_1BA4")

    label("loc_171C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1790")

    ChrTalk(
        0xFE,
        (
            "本部让我去\x01",
            "蔡斯的研究所去上班。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这虽然是件非常值得庆祝的事情……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BA4")

    label("loc_1790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_17BA")

    ChrTalk(
        0xFE,
        "好～的，大家休息一会儿吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BA4")

    label("loc_17BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_17CD")

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BA4")

    label("loc_17CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_18A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185A")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "这边的机器\x01",
            "也差不多该换新的零件了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "去和总部的技术人员\x01",
            "联系一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A2")

    label("loc_185A")


    ChrTalk(
        0xFE,
        (
            "这边的机器\x01",
            "也差不多该换新的零件了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A2")

    Jump("loc_1BA4")

    label("loc_18A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_19E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198B")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "听懂了吗？\x01",
            "我再说明一次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "将导力流撞上动翼列，\x01",
            "直线的运动能量\x01",
            "将转变为回转运动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这就是导力引擎的\x01",
            "基本原理和构造。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    Jump("loc_19E6")

    label("loc_198B")


    ChrTalk(
        0xFE,
        "豆豆是我唯一的亲人了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我会竭尽全力\x01",
            "做好我能做的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E6")

    Jump("loc_1BA4")

    label("loc_19E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_1A63")

    ChrTalk(
        0xFE,
        (
            "哦，桥好像被拉上去了。\x01",
            "差不多可以开始整理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "伦格兰德大桥\x01",
            "对我们卢安市民来说\x01",
            "是具有跨时代意义的建筑物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA4")

    label("loc_1A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1BA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B79")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "虽然现在还没什么问题，\x01",
            "以防万一，我还是把\x01",
            "４号和７号的插座交换一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "与此同时，\x01",
            "你也不要忘了检查一下导力压。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "好，我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "豆豆去仓库\x01",
            "把新的零件拿过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "知、知道了！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    Jump("loc_1BA4")

    label("loc_1B79")


    ChrTalk(
        0xFE,
        (
            "抱歉，\x01",
            "现在我们正在讨论工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA4")

    TalkEnd(0x11)
    Return()

    # Function_7_1596 end

    def Function_8_1BA8(): pass

    label("Function_8_1BA8")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C26")

    ChrTalk(
        0xFE,
        (
            "如果能够达成一致意见\x01",
            "就不会变成现在这样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是难办啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_220C")

    label("loc_1C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1CC0")

    ChrTalk(
        0xFE,
        (
            "糟了糟了，\x01",
            "我最不擅长应付这种阴沉的气氛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算库莱泽的技术再强，\x01",
            "遇到这种问题也很难决断……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220C")

    label("loc_1CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_1D6D")

    ChrTalk(
        0xFE,
        (
            "虽然维修长不在，\x01",
            "但是这个世上是不会允许失败的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要比平时更加严格地\x01",
            "进行检查工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220C")

    label("loc_1D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1D9B")

    ChrTalk(
        0xFE,
        (
            "呼～顺利地起飞了，\x01",
            "真是松了一口气啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220C")

    label("loc_1D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1E90")

    ChrTalk(
        0xFE,
        (
            "我以为刚才来的客人\x01",
            "都与往常一样是来\x01",
            "劝说库莱泽回本部工作的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是看库莱泽的样子，\x01",
            "好像是一件更严重的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220C")

    label("loc_1E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1F27")

    ChrTalk(
        0xFE,
        (
            "我在库莱泽那边\x01",
            "碰到了几个从总部来的客人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……到底是什么事情\x01",
            "我差不多也猜到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过，这已是家常便饭了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_220C")

    label("loc_1F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1FC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F98")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "那么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "定期船过来之前，\x01",
            "一定要把设备检查完毕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC0")

    label("loc_1F98")


    ChrTalk(
        0xFE,
        (
            "现在要赶快\x01",
            "把设备检查完毕啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC0")

    Jump("loc_220C")

    label("loc_1FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_21C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2125")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "库莱泽是从蔡斯来的\x01",
            "非常有经验的技师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然他已经好几次收到调令，\x01",
            "让他去总部工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他却以这里离家近的理由\x01",
            "一直留在这里工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说这就是他的性格，\x01",
            "但是我觉得这样有点不值得啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C6")

    label("loc_2125")


    ChrTalk(
        0xFE,
        (
            "库莱泽他\x01",
            "虽然已经好几次收到调令，\x01",
            "让他去总部工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他却以这里离家近的理由\x01",
            "一直留在这里工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C6")

    Jump("loc_220C")

    label("loc_21C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_220C")

    ChrTalk(
        0xFE,
        (
            "现在我们\x01",
            "正在讨论维修的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220C")

    TalkEnd(0x12)
    Return()

    # Function_8_1BA8 end

    def Function_9_2210(): pass

    label("Function_9_2210")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2277")

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不是因为我的话，\x01",
            "哥哥肯定已经成为\x01",
            "新型引擎的研究者了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2716")

    label("loc_2277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_235E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2338")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "虽然哥哥他\x01",
            "什么都不跟我说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过我从爱德望叔叔那里听说了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有人向哥哥发出邀请，\x01",
            "问他是不是愿意去蔡斯\x01",
            "做导力引擎的开发。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的哥哥\x01",
            "果然很厉害呀……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235B")

    label("loc_2338")


    ChrTalk(
        0xFE,
        (
            "我的哥哥\x01",
            "果然很厉害呀……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235B")

    Jump("loc_2716")

    label("loc_235E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_23A8")

    ChrTalk(
        0xFE,
        (
            "今天哥哥\x01",
            "好像没有去出差。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2716")

    label("loc_23A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_23CD")

    ChrTalk(
        0xFE,
        (
            "就在刚才，\x01",
            "去蔡斯的定期船刚刚飞走。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2716")

    label("loc_23CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2442")

    ChrTalk(
        0xFE,
        "是我的错觉吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天哥哥不知为何\x01",
            "有点提不起精神。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么了呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2716")

    label("loc_2442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_251C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24EA")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "库莱泽哥哥\x01",
            "果然是个很厉害的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "能够在哥哥手下实践学习真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总有一天，\x01",
            "我也一定会成为像哥哥这样棒的技师。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_24EA")


    ChrTalk(
        0xFE,
        (
            "总有一天，\x01",
            "我也一定会成为像哥哥这样棒的技师。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2519")

    Jump("loc_2716")

    label("loc_251C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_25E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25C7")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "库莱泽哥哥\x01",
            "开始教我念书了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "多亏了哥哥，\x01",
            "我的功课也进步了很多，\x01",
            "也变得有自信了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "哥哥就像爸爸一样啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E6")

    label("loc_25C7")


    ChrTalk(
        0xFE,
        (
            "库莱泽哥哥\x01",
            "开始教我念书了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E6")

    Jump("loc_2716")

    label("loc_25E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_26EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268D")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "只要你的能力得到了\x01",
            "蔡斯中央工房的认可，\x01",
            "无论年龄大小都能在那里工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也要努力磨练我的技术，\x01",
            "总有一天在蔡斯工作是我的梦想。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26EB")

    label("loc_268D")


    ChrTalk(
        0xFE,
        (
            "我也要努力磨练我的技术，\x01",
            "总有一天在蔡斯工作是我的梦想。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26EB")

    Jump("loc_2716")

    label("loc_26EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2716")

    ChrTalk(
        0xFE,
        (
            "我、我正在这里\x01",
            "做维修师的实习。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2716")

    TalkEnd(0x13)
    Return()

    # Function_9_2210 end

    def Function_10_271A(): pass

    label("Function_10_271A")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(132240, 8150, 95810, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_4A(0x9, 255)
    OP_22(0x75, 0x0, 0x64)
    SetChrPos(0x8, 133220, 8150, 96310, 270)
    SetChrPos(0x101, 131000, 8150, 96980, 90)
    SetChrPos(0x102, 130960, 8150, 95770, 90)
    SetChrPos(0x105, 129930, 8150, 96550, 90)
    SetChrPos(0x9, 131860, 8150, 98100, 135)
    SetChrPos(0xA, 133250, 9200, 93100, 315)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#178F#5P刚才我们审问了\x01",
            "醒过来的戴尔蒙市长……\x02\x03",
            "不过奇怪的是，\x01",
            "他好像突然失去了所有记忆。\x02\x03",
            "就连纵火抢劫等事件，\x01",
            "也似乎只有一点模糊的印象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F这、这样吗……\x02\x03",
            "好像跟空贼的首领一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P突然失去记忆……\x01",
            "这恐怕和那帮黑衣人有关。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#176F#5P不过，就算记忆模糊，\x01",
            "所犯下的罪行还是无可狡辩的……\x02\x03",
            "当然，他的秘书基尔巴特\x01",
            "也会一起受到严厉的审讯。\x02\x03",
            "#171F有了调查结果之后，\x01",
            "我们也会通知游击士协会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#2P那太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#147F对了，中尉大人。\x01",
            "我这里有个不情之请。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2AC4():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2AC4)
    Sleep(300)

    def lambda_2AD7():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AD7)

    def lambda_2AE5():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2AE5)

    def lambda_2AF3():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2AF3)

    ChrTalk(
        0x8,
        "#173F#5P什么事，记者先生？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F如果不麻烦你们的话，\x01",
            "能让我也搭乘一下那艘飞艇吗？\x02\x03",
            "毕竟是蔡斯中央工房研制的\x01",
            "最新型飞艇啊。\x02\x03",
            "所以，恳请您让我上去做个采访。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#176F#5P非常抱歉，\x01",
            "恕我不能答应你的请求。\x02\x03",
            "#170F这艘『埃尔赛尤号』\x01",
            "前几天才刚完成了装配，\x01",
            "现在还是处于非公开的试飞阶段之中。\x02\x03",
            "在正式举行新闻发布会之前，\x01",
            "还请贵社尽量不要做太多的报道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142F就、就通融一下吧！\x02\x03",
            "我还想和被逮捕的市长\x01",
            "和秘书他们说两句……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#171F#5P这点你不用担心。调查完结之后，\x01",
            "我们自然会把真相告之王都的通讯社。\x02\x03",
            "其他方面就恕我不能帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145F唉～没办法了。\x02\x03",
            "#144F好吧，只有一条路了！\x02\x03",
            "只能写完新闻之后，\x01",
            "十万火急赶回王都了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "#147F那么各位，告辞了！\x02",
    )

    CloseMessageWindow()

    def lambda_2EBC():

        label("loc_2EBC")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2EBC")

    QueueWorkItem2(0x8, 1, lambda_2EBC)

    def lambda_2ECD():

        label("loc_2ECD")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2ECD")

    QueueWorkItem2(0x101, 1, lambda_2ECD)

    def lambda_2EDE():

        label("loc_2EDE")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2EDE")

    QueueWorkItem2(0x102, 1, lambda_2EDE)

    def lambda_2EEF():

        label("loc_2EEF")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2EEF")

    QueueWorkItem2(0x105, 1, lambda_2EEF)
    OP_8C(0x9, 90, 400)
    OP_8E(0x9, 0x20EC2, 0x1FD6, 0x184D4, 0x1388, 0x0)
    OP_8E(0x9, 0x20EF4, 0x1FD6, 0x18A74, 0x1388, 0x0)
    OP_8E(0x9, 0x1ED34, 0x1806, 0x18B8C, 0x1388, 0x0)
    SetChrFlags(0x9, 0x80)

    ChrTalk(
        0x101,
        (
            "#506F还是老样子，\x01",
            "该说他干劲强呢，还是执念强呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#2P哈哈……\x01",
            "不过这才是奈尔先生的风格啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#178F#5P听说《利贝尔通讯》的发行量\x01",
            "最近在直线上升。\x02\x03",
            "我只是希望他能写出\x01",
            "不被政治宣传所束缚的新闻……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3043():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3043)

    def lambda_3051():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3051)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        "#014F政治宣传……？\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "#175F#5P没什么……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x40)
    SetChrPos(0xB, 126260, 6150, 101260, 90)
    SetChrPos(0xC, 126260, 6150, 101260, 90)

    NpcTalk(
        0xB,
        "男性的声音",
        (
            "#5P看来你立了一功啊。\x01",
            "舒华兹中尉。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_318A():
        OP_6D(132920, 8150, 97630, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_318A)

    def lambda_31A2():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_31A2)

    def lambda_31B2():

        label("loc_31B2")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_31B2")

    QueueWorkItem2(0x8, 1, lambda_31B2)

    def lambda_31C3():

        label("loc_31C3")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_31C3")

    QueueWorkItem2(0x101, 1, lambda_31C3)

    def lambda_31D4():

        label("loc_31D4")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_31D4")

    QueueWorkItem2(0x102, 1, lambda_31D4)

    def lambda_31E5():

        label("loc_31E5")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_31E5")

    QueueWorkItem2(0x105, 1, lambda_31E5)
    OP_43(0xB, 0x1, 0x0, 0xB)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0xC)
    WaitChrThread(0xB, 0x1)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "#173F这、这不是上校吗……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6P啊啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F理查德上校……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#113F哦，你们是上次的……\x02\x03",
            "#110F原来如此，协会发来的联络中\x01",
            "所提到的游击士新人就是你们两位啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#6P咦……？\x02\x03",
            "嘉恩哥哥联络的\x01",
            "原来就是理查德上校啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#110F嗯，王国军司令部所在的\x01",
            "雷斯顿要塞收到了协会的联络。\x02\x03",
            "我急急忙忙赶来一看，\x01",
            "原来事情已经结束了啊。\x02\x03",
            "做得真漂亮，舒华兹中尉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#176F不，您过奖了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#182F呵呵，不过还真不可思议啊。\x02\x03",
            "想不到身在王都的亲卫队\x01",
            "竟然会跑来这种地方……\x02\x03",
            "看来，你们有着连我们情报部\x01",
            "都还没掌握的独特情报网啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#175F您、您说笑了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#047F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#111F哈哈，凯诺娜上尉。\x01",
            "这点我们也没必要深究了。\x02\x03",
            "#115F不过，负责守护陛下的亲卫队\x01",
            "为其他琐事分神也并不是什么好事啊。\x02\x03",
            "#110F后面的调查由我们接手，\x01",
            "而犯人就移交到雷斯顿要塞吧。\x02\x03",
            "我们会代表王国军\x01",
            "对市长他们进行严厉的审讯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#178F是……明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#111F那我们这就告辞了。\x02\x03",
            "舒华兹中尉、各位游击士，\x01",
            "还有那位穿校服的小姐……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#115F……有机会再见吧。\x01",
            "　\x02\x03",
            "#110F那么，告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#182F呵呵，多保重。\x02",
    )

    CloseMessageWindow()
    OP_44(0x105, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_8C(0xB, 135, 400)
    OP_43(0xB, 0x1, 0x0, 0xD)
    Sleep(600)
    OP_8C(0xC, 135, 400)
    OP_43(0xC, 0x1, 0x0, 0xD)
    WaitChrThread(0xC, 0x1)

    def lambda_37E5():
        OP_6D(131910, 8150, 96570, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37E5)
    OP_8C(0x101, 225, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#505F#1P可能是我多心了，不过……\x02\x03",
            "刚才，理查德上校\x01",
            "似乎一直在往科洛丝那边看。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3882():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3882)

    def lambda_3890():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3890)
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(
        0x105,
        "#542F是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P…………………………\x02\x03",
            "#010F我也觉得是。\x01",
            "像你这样的学生\x01",
            "出现在这种场合并不寻常啊。\x02\x03",
            "他会觉得奇怪也是难免的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F啊、啊哈哈……\x01",
            "那也的确是呢。\x02\x03",
            "我该反省一下了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#1P唔，不过我的感觉\x01",
            "也不完全是你们说的那样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#176F……让我来说的话，\x01",
            "你们的成绩也足够让人吃惊了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A13():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A13)
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#171F就算是游击士，\x01",
            "但这么年轻就能有如此的本领……\x02\x03",
            "可以的话，真想把你们招进亲卫队啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#1P没、没有啦～\x01",
            "您就别这么抬举我们了。\x02\x03",
            "能解决这次的事件，\x01",
            "也是因为多亏了很多人的帮助啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#170F不用这么谦虚。\x02\x03",
            "你们似乎还是准游击士，\x01",
            "打算进级成为正游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#1P嗯，是呢。\x01",
            "现在正为了这目标而修行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们打算在女王的诞辰庆典之前\x01",
            "环游整个利贝尔王国一周。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#170F是吗……\x01",
            "我支持你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#1P尤莉亚队长！\x01",
            "出航准备完成了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x14, 400)

    ChrTalk(
        0x8,
        "#170F好，知道了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#170F艾丝蒂尔、约修亚。\x01",
            "……还有科洛丝。\x02\x03",
            "我们这就要告辞了。\x01",
            "有机会再见吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F到时还请多多关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#048F……真的谢谢您。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_43(0x8, 0x0, 0x0, 0xE)

    def lambda_3E07():
        OP_6C(224000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3E07)

    def lambda_3E17():
        OP_6D(132040, 8960, 87760, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E17)

    def lambda_3E2F():
        OP_6B(3680, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E2F)

    def lambda_3E3F():
        OP_67(0, 5440, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3E3F)
    Sleep(1000)

    def lambda_3E5C():
        OP_8E(0xFE, 0x206C0, 0x1FD6, 0x172A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E5C)

    def lambda_3E77():
        OP_8E(0xFE, 0x201D4, 0x1FD6, 0x171F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E77)

    def lambda_3E92():
        OP_8E(0xFE, 0x20454, 0x1FD6, 0x17610, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3E92)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 180, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 180, 400)
    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 13)
    Sleep(100)
    OP_99(0x8, 0x0, 0x1, 0x4B0)

    ChrTalk(
        0x8,
        "#177F全体队员，敬礼！\x02",
    )

    CloseMessageWindow()
    OP_1F(0x50, 0x1F4)
    OP_22(0x98, 0x0, 0x64)

    def lambda_3F19():

        label("loc_3F19")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_3F19")

    QueueWorkItem2(0x14, 0, lambda_3F19)

    def lambda_3F2C():

        label("loc_3F2C")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_3F2C")

    QueueWorkItem2(0x15, 0, lambda_3F2C)

    def lambda_3F3F():

        label("loc_3F3F")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_3F3F")

    QueueWorkItem2(0x16, 0, lambda_3F3F)

    def lambda_3F52():

        label("loc_3F52")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_3F52")

    QueueWorkItem2(0x17, 0, lambda_3F52)
    SetChrChipByIndex(0x18, 11)
    SetChrChipByIndex(0x1C, 11)
    SetChrChipByIndex(0x20, 11)
    Sleep(100)
    SetChrChipByIndex(0x19, 11)
    SetChrChipByIndex(0x1D, 11)
    SetChrChipByIndex(0x21, 11)
    Sleep(100)
    SetChrChipByIndex(0x1A, 11)
    SetChrChipByIndex(0x1E, 11)
    SetChrChipByIndex(0x22, 11)
    Sleep(100)
    SetChrChipByIndex(0x1B, 11)
    SetChrChipByIndex(0x1F, 11)
    SetChrChipByIndex(0x23, 11)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F哇……\x02",
    )

    CloseMessageWindow()

    def lambda_3FC7():

        label("loc_3FC7")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3FC7")

    QueueWorkItem2(0x102, 1, lambda_3FC7)

    def lambda_3FD8():

        label("loc_3FD8")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3FD8")

    QueueWorkItem2(0x105, 1, lambda_3FD8)

    def lambda_3FE9():

        label("loc_3FE9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3FE9")

    QueueWorkItem2(0x101, 1, lambda_3FE9)

    ChrTalk(
        0x8,
        (
            "#172F王室亲卫队所属舰，\x01",
            "『埃尔赛尤号』——起飞！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(3000)
    OP_6D(159890, 6490, 81650, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(388, 0)
    OP_6F(0x7, 100)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrPos(0x24, 138000, 6550, 81800, 90)
    SetChrPos(0x25, 138000, 1200, 81800, 90)
    OP_A1(0x24, 0x8)
    OP_72(0x8, 0x4)
    OP_72(0x8, 0x20)
    SetChrFlags(0x24, 0x4)
    OP_A1(0x25, 0x9)
    OP_72(0x9, 0x4)
    SetChrFlags(0x25, 0x4)

    def lambda_4126():
        OP_6D(129389, 10000, 81550, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4126)
    Sleep(2000)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0x8, 1)
    OP_70(0x8, 0x96)
    OP_73(0x4)
    OP_6F(0x8, 150)
    OP_70(0x8, 0x14A)
    OP_43(0x24, 0x3, 0x0, 0xF)

    def lambda_416E():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_416E)

    def lambda_417E():
        OP_67(0, 7850, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_417E)
    OP_91(0x24, 0x0, 0x1F4, 0x0, 0x190, 0x0)
    OP_91(0x24, 0x0, 0x3E8, 0x0, 0x320, 0x0)
    OP_91(0x24, 0x0, 0x7D0, 0x0, 0x640, 0x0)
    OP_91(0x24, 0x0, 0x1F4, 0x0, 0x320, 0x0)
    OP_91(0x24, 0x0, 0x190, 0x0, 0x190, 0x0)
    OP_73(0x8)
    OP_71(0x8, 0x20)
    OP_6F(0x8, 330)
    OP_70(0x8, 0x1AE)

    def lambda_4210():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4210)

    def lambda_4226():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4226)
    Sleep(200)

    def lambda_4241():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4241)

    def lambda_4257():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4257)
    Sleep(200)

    def lambda_4272():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4272)

    def lambda_4288():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4288)
    Sleep(200)

    def lambda_42A3():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_42A3)

    def lambda_42B9():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_42B9)
    Sleep(200)

    def lambda_42D4():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_42D4)

    def lambda_42EA():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_42EA)
    Sleep(200)

    def lambda_4305():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4305)

    def lambda_431B():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_431B)
    Sleep(200)

    def lambda_4336():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4336)

    def lambda_434C():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_434C)
    Sleep(200)

    def lambda_4367():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4367)

    def lambda_437D():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_437D)
    Sleep(200)

    def lambda_4398():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4398)

    def lambda_43AE():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_43AE)
    Sleep(200)

    def lambda_43C9():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_43C9)

    def lambda_43DF():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_43DF)
    Sleep(200)

    def lambda_43FA():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_43FA)

    def lambda_4410():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4410)
    Sleep(200)

    def lambda_442B():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_442B)

    def lambda_4441():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4441)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    OP_24(0x75, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    OP_24(0x75, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    OP_24(0x75, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    OP_24(0x75, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    OP_24(0x75, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    OP_24(0x75, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    OP_24(0x75, 0x1E)
    Sleep(100)
    OP_23(0x77)
    OP_23(0x75)
    OP_1F(0x64, 0x1F4)
    Fade(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x24, 0xFF)
    OP_44(0x25, 0xFF)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_6D(132060, 8150, 94520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(
        0x101,
        (
            "#506F哇～一边敬礼，\x01",
            "一边吹起喇叭……\x02\x03",
            "简直是压倒性的震撼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F是啊……\x01",
            "飞艇也是最新型的。\x02\x03",
            "不愧是保护女王陛下安全的\x01",
            "精英部队啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#041F呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#501F不过尤莉亚中尉\x01",
            "不愧是一个巾帼英雄啊。\x02\x03",
            "#001F感觉就像科洛丝扮演的\x01",
            "苍骑士奥斯卡那样帅气呢㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F我也有这种感觉。\x02\x03",
            "#041F呵呵，真是有趣的巧合。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#311F#1P啾～☆\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2120   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_10_271A end

    def Function_11_472D(): pass

    label("Function_11_472D")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x20EF4, 0x1FD6, 0x18A74, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20EAE, 0x1FD6, 0x1856A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x209C2, 0x1FD6, 0x18006, 0xBB8, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_11_472D end

    def Function_12_4776(): pass

    label("Function_12_4776")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x20EF4, 0x1FD6, 0x18A74, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20D64, 0x1FD6, 0x17FCA, 0xBB8, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_12_4776 end

    def Function_13_47AB(): pass

    label("Function_13_47AB")

    OP_8E(0xFE, 0x20EAE, 0x1FD6, 0x1856A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20EF4, 0x1FD6, 0x18A74, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1ED34, 0x1806, 0x18B8C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_13_47AB end

    def Function_14_47ED(): pass

    label("Function_14_47ED")

    OP_8E(0xFE, 0x20468, 0x1FD6, 0x17250, 0xBB8, 0x0)
    OP_8E(0xFE, 0x2042C, 0x1FD6, 0x14FAA, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x203E6, 0x1F72, 0x14C94, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)
    Return()

    # Function_14_47ED end

    def Function_15_4836(): pass

    label("Function_15_4836")

    OP_6F(0x8, 150)
    OP_70(0x8, 0xFA)
    OP_73(0x8)
    OP_22(0xDD, 0x0, 0x64)
    OP_6F(0x8, 251)
    OP_70(0x8, 0x109)
    OP_73(0x8)
    OP_22(0xDD, 0x0, 0x64)
    OP_6F(0x8, 266)
    OP_70(0x8, 0x11F)
    OP_73(0x8)
    OP_22(0xDD, 0x0, 0x64)
    OP_6F(0x8, 288)
    OP_70(0x8, 0x14A)
    Return()

    # Function_15_4836 end

    def Function_16_4887(): pass

    label("Function_16_4887")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "定期船起降坪\x01",
            "≡　开往柏斯市\x01",
            "≡　开往蔡斯市\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_4887 end

    def Function_17_48F0(): pass

    label("Function_17_48F0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※请勿携带易燃物和危险品\x01",
            "　　　　　利贝尔飞艇公社\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_48F0 end

    def Function_18_496F(): pass

    label("Function_18_496F")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_496F end

    SaveToFile()

Try(main)
