from ED6ScenarioHelper import *

def main():
    # 玛诺利亚村　村长家

    CreateScenaFile(
        FileName            = 'T2300   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2300.x',
        MapIndex            = 86,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2300   ._SN',
            'ED6_DT01/T2300_1 ._SN',
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
        'Girl in Uniform',                      # 9
        'Sieg',                                 # 10
        'Boy Wearing Cap',                      # 11
        'Clem',                                 # 12
        'Sadie',                                # 13
        'Mary',                                 # 14
        'Amelia',                               # 15
        'Camera',                               # 16
        'Orvid',                                # 17
        'Lucia',                                # 18
        'Daniel',                               # 19
        'Polly',                                # 20
        'Carna',                                # 21
        'Matron Theresa',                       # 22
        'Manoria Byroad',                       # 23
        'Gull Seaside Way',                     # 24
    )

    DeclEntryPoint(
        Unknown_00              = 9000,
        Unknown_04              = 6000,
        Unknown_08              = -3000,
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
        Unknown_3A              = 86,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00040 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH01150 ._CH',             # 02
        'ED6_DT07/CH02320 ._CH',             # 03
        'ED6_DT07/CH02630 ._CH',             # 04
        'ED6_DT07/CH01050 ._CH',             # 05
        'ED6_DT07/CH01120 ._CH',             # 06
        'ED6_DT07/CH01070 ._CH',             # 07
        'ED6_DT07/CH02640 ._CH',             # 08
        'ED6_DT07/CH02500 ._CH',             # 09
        'ED6_DT07/CH00004 ._CH',             # 0A
        'ED6_DT07/CH00044 ._CH',             # 0B
        'ED6_DT07/CH00003 ._CH',             # 0C
        'ED6_DT07/CH00013 ._CH',             # 0D
        'ED6_DT07/CH00005 ._CH',             # 0E
        'ED6_DT06/CH20051 ._CH',             # 0F
        'ED6_DT06/CH20053 ._CH',             # 10
        'ED6_DT06/CH20085 ._CH',             # 11
        'ED6_DT07/CH01240 ._CH',             # 12
        'ED6_DT07/CH02570 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH00040P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH01150P._CP',             # 02
        'ED6_DT07/CH02320P._CP',             # 03
        'ED6_DT07/CH02630P._CP',             # 04
        'ED6_DT07/CH01050P._CP',             # 05
        'ED6_DT07/CH01120P._CP',             # 06
        'ED6_DT07/CH01070P._CP',             # 07
        'ED6_DT07/CH02640P._CP',             # 08
        'ED6_DT07/CH02500P._CP',             # 09
        'ED6_DT07/CH00004P._CP',             # 0A
        'ED6_DT07/CH00044P._CP',             # 0B
        'ED6_DT07/CH00003P._CP',             # 0C
        'ED6_DT07/CH00013P._CP',             # 0D
        'ED6_DT07/CH00005P._CP',             # 0E
        'ED6_DT06/CH20051P._CP',             # 0F
        'ED6_DT06/CH20053P._CP',             # 10
        'ED6_DT06/CH20085P._CP',             # 11
        'ED6_DT07/CH01240P._CP',             # 12
        'ED6_DT07/CH02570P._CP',             # 13
    )

    DeclNpc(
        X                   = 18100,
        Z                   = 0,
        Y                   = 16400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 6130,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 0,
        Y                   = 23500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 37310,
        Z                   = 1700,
        Y                   = -33090,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -4100,
        Z                   = 8000,
        Y                   = 45100,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 53000,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 53000,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2800,
        Z                   = 4000,
        Y                   = 29000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 6000,
        Z                   = 200,
        Y                   = 22200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 32500,
        Z                   = 0,
        Y                   = -34400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 5560,
        Z                   = 6000,
        Y                   = -2680,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 3860,
        Z                   = 4030,
        Y                   = 16990,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -2940,
        Z                   = 7990,
        Y                   = 68620,
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
        X                   = 75410,
        Z                   = -40,
        Y                   = 20810,
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


    DeclEvent(
        X                   = 16870,
        Y                   = 7000,
        Z                   = -7690,
        Range               = -9400,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFFF998,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 8200,
        Y                   = 4000,
        Z                   = 9300,
        Range               = 1460,
        Unknown_10          = 0x178E,
        Unknown_14          = 0x198C,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 65500,
        Y                   = -1000,
        Z                   = 23100,
        Range               = 68250,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x4736,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = -760,
        Y                   = 5000,
        Z                   = 59750,
        Range               = -5380,
        Unknown_10          = 0x2670,
        Unknown_14          = 0xF4D8,
        Unknown_18          = 0x0,
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 27540,
        Y                   = 0,
        Z                   = 18980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = 53410,
        Y                   = 0,
        Z                   = 22710,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 6000,
        Y                   = 4000,
        Z                   = 20210,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )


    ScpFunction(
        "Function_0_42A",          # 00, 0
        "Function_1_6BA",          # 01, 1
        "Function_2_720",          # 02, 2
        "Function_3_736",          # 03, 3
        "Function_4_75A",          # 04, 4
        "Function_5_82F",          # 05, 5
        "Function_6_904",          # 06, 6
        "Function_7_9D9",          # 07, 7
        "Function_8_AAE",          # 08, 8
        "Function_9_B16",          # 09, 9
        "Function_10_1514",        # 0A, 10
        "Function_11_1C0B",        # 0B, 11
        "Function_12_1C8F",        # 0C, 12
        "Function_13_1D9F",        # 0D, 13
        "Function_14_1E5B",        # 0E, 14
        "Function_15_1F08",        # 0F, 15
        "Function_16_218A",        # 10, 16
        "Function_17_25E9",        # 11, 17
        "Function_18_3415",        # 12, 18
        "Function_19_3425",        # 13, 19
        "Function_20_43C1",        # 14, 20
        "Function_21_4EA6",        # 15, 21
        "Function_22_4EB1",        # 16, 22
        "Function_23_5AD7",        # 17, 23
        "Function_24_63F9",        # 18, 24
        "Function_25_69F8",        # 19, 25
        "Function_26_6F19",        # 1A, 26
        "Function_27_6F35",        # 1B, 27
        "Function_28_7309",        # 1C, 28
        "Function_29_7325",        # 1D, 29
        "Function_30_7329",        # 1E, 30
        "Function_31_732D",        # 1F, 31
    )


    def Function_0_42A(): pass

    label("Function_0_42A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4D2")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 5000, 4000, 17180, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 5160, 4000, 15170, 180)
    SetChrFlags(0xB, 0x10)
    OP_43(0xB, 0x0, 0x0, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 7040, 4030, 12860, 270)
    SetChrFlags(0x12, 0x10)
    OP_43(0x12, 0x0, 0x0, 0x5)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 5130, 4030, 10940, 0)
    SetChrFlags(0x13, 0x10)
    OP_43(0x13, 0x0, 0x0, 0x6)
    SetChrPos(0x11, 3030, 4030, 13020, 90)
    SetChrFlags(0x11, 0x10)
    OP_43(0x11, 0x0, 0x0, 0x7)
    Jump("loc_5E9")

    label("loc_4D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_4E1")
    ClearChrFlags(0x14, 0x80)
    Jump("loc_5E9")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_4F5")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_5E9")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_598")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 5000, 4000, 17180, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 5160, 4000, 15170, 180)
    SetChrFlags(0xB, 0x10)
    OP_43(0xB, 0x0, 0x0, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 7040, 4030, 12860, 270)
    SetChrFlags(0x12, 0x10)
    OP_43(0x12, 0x0, 0x0, 0x5)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 5130, 4030, 10940, 0)
    SetChrFlags(0x13, 0x10)
    OP_43(0x13, 0x0, 0x0, 0x6)
    SetChrPos(0x11, 3030, 4030, 13020, 90)
    SetChrFlags(0x11, 0x10)
    OP_43(0x11, 0x0, 0x0, 0x7)
    Jump("loc_5E9")

    label("loc_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5BA")
    SetChrPos(0x11, 63480, -20, 23290, 180)
    OP_43(0x11, 0x0, 0x0, 0x2)
    Jump("loc_5E9")

    label("loc_5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_5C4")
    Jump("loc_5E9")

    label("loc_5C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_5CE")
    Jump("loc_5E9")

    label("loc_5CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5D8")
    Jump("loc_5E9")

    label("loc_5D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_5E2")
    Jump("loc_5E9")

    label("loc_5E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_5E9")

    label("loc_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_611")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_611")
    ClearChrFlags(0xE, 0x80)

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_61F")
    OP_A3(0x3FA)
    Event(0, 22)

    label("loc_61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_63B")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 23)

    label("loc_63B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_649")
    OP_A3(0x3FC)
    Event(0, 24)

    label("loc_649")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_659"),
        (105, "loc_695"),
        (SWITCH_DEFAULT, "loc_6A8"),
    )


    label("loc_659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66B")
    OP_A2(0x409)
    Event(0, 16)
    Jump("loc_692")

    label("loc_66B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x36)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_692")
    OP_28(0x1F, 0x4, 0x10)
    OP_28(0x1F, 0x1, 0x80)
    RemoveParty(0x36, 0xFF)
    Event(1, 1)

    label("loc_692")

    Jump("loc_6A8")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A5")
    Event(0, 17)

    label("loc_6A5")

    Jump("loc_6A8")

    label("loc_6A8")

    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_42A end

    def Function_1_6BA(): pass

    label("Function_1_6BA")

    OP_16(0x2, 0xFA0, 0xFFFE5A20, 0xFFFE13D0, 0x3004B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E4")
    OP_B1("t2300_y")
    Jump("loc_6ED")

    label("loc_6E4")

    OP_B1("t2300_n")

    label("loc_6ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_705")
    OP_6F(0x2, 0)
    OP_72(0x2, 0x10)

    label("loc_705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71A")
    OP_77(0x41, 0x64, 0x82, 0x0, 0x0)

    label("loc_71A")

    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_6BA end

    def Function_2_720(): pass

    label("Function_2_720")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_735")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_720")

    label("loc_735")

    Return()

    # Function_2_720 end

    def Function_3_736(): pass

    label("Function_3_736")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_759")
    OP_8D(0xFE, -6100, 32000, 300, 25200, 3000)
    Jump("Function_3_736")

    label("loc_759")

    Return()

    # Function_3_736 end

    def Function_4_75A(): pass

    label("Function_4_75A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_82E")
    OP_8E(0xFE, 0x1B80, 0xFBE, 0x323C, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0x140A, 0xFBE, 0x2ABC, 0xDAC, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_62(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0xBD6, 0xFBE, 0x32DC, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0x1428, 0xFA0, 0x3B42, 0xDAC, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_62(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    Jump("Function_4_75A")

    label("loc_82E")

    Return()

    # Function_4_75A end

    def Function_5_82F(): pass

    label("Function_5_82F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_903")
    OP_8E(0xFE, 0x140A, 0xFBE, 0x2ABC, 0xDAC, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_62(0x12, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0xBD6, 0xFBE, 0x32DC, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0x12, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0x1428, 0xFA0, 0x3B42, 0xDAC, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_62(0x12, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0x1B80, 0xFBE, 0x323C, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0x12, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    Jump("Function_5_82F")

    label("loc_903")

    Return()

    # Function_5_82F end

    def Function_6_904(): pass

    label("Function_6_904")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D8")
    OP_8E(0xFE, 0xBD6, 0xFBE, 0x32DC, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x1428, 0xFA0, 0x3B42, 0xDAC, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x1B80, 0xFBE, 0x323C, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x140A, 0xFBE, 0x2ABC, 0xDAC, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1000)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jump("Function_6_904")

    label("loc_9D8")

    Return()

    # Function_6_904 end

    def Function_7_9D9(): pass

    label("Function_7_9D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AAD")
    OP_8E(0xFE, 0x1428, 0xFA0, 0x3B42, 0xDAC, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_62(0x11, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0x1B80, 0xFBE, 0x323C, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0x11, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0x140A, 0xFBE, 0x2ABC, 0xDAC, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_62(0x11, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0xBD6, 0xFBE, 0x32DC, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0x11, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    Jump("Function_7_9D9")

    label("loc_AAD")

    Return()

    # Function_7_9D9 end

    def Function_8_AAE(): pass

    label("Function_8_AAE")

    TalkBegin(0x14)

    ChrTalk(
        0x14,
        (
            "#830FI'm keeping an eye on these idiots.\x02\x03",
            "You guys head on to Ruan and\x01",
            "report back to Jean.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_8_AAE end

    def Function_9_B16(): pass

    label("Function_9_B16")

    TalkBegin(0xC)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B76")
    OP_0D()
    OP_A9(0x36)
    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_B76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B87")
    TalkEnd(0xC)
    Return()

    label("loc_B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C65")
    OP_A2(0x0)

    ChrTalk(
        0xC,
        "The kids finally seem happy again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm still having a tough time\x01",
            "dealing with Mayor Dalmore\x01",
            "being a criminal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There's no telling what the kids will\x01",
            "think, once they figure it all out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D06")

    label("loc_C65")


    ChrTalk(
        0xC,
        (
            "I'm still having a tough time\x01",
            "dealing with Mayor Dalmore\x01",
            "being a criminal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There's no telling what the kids will\x01",
            "think, once they figure it all out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D06")

    Jump("loc_1510")

    label("loc_D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_E0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB9")
    OP_A2(0x0)

    ChrTalk(
        0xC,
        "The arsonists were caught?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "That's a relief, but it's still sad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I don't think the kids will ever\x01",
            "completely heal from the\x01",
            "trauma of this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E08")

    label("loc_DB9")


    ChrTalk(
        0xC,
        (
            "I don't think the kids will ever\x01",
            "completely heal from the\x01",
            "trauma of this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E08")

    Jump("loc_1510")

    label("loc_E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_EF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC0")
    OP_A2(0x0)

    ChrTalk(
        0xC,
        (
            "Matron Theresa was injured in\x01",
            "a mugging?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Almighty Aidios...what are they\x01",
            "to do...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please...you're bracers! You have\x01",
            "to catch whoever did this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EEF")

    label("loc_EC0")


    ChrTalk(
        0xC,
        (
            "Almighty Aidios...what are they\x01",
            "to do...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEF")

    Jump("loc_1510")

    label("loc_EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_F8A")

    ChrTalk(
        0xC,
        (
            "The kids from the orphanage \x01",
            "seem to be getting a bit of\x01",
            "their old spirit back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm glad the girls were able to\x01",
            "come over and play.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1510")

    label("loc_F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_101E")

    ChrTalk(
        0xC,
        (
            "That little boy from the orphanage\x01",
            "was running like his life depended\x01",
            "on it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wonder what happened?\x01",
            "It's a little worrisome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1510")

    label("loc_101E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_110A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AB")
    OP_A2(0x0)

    ChrTalk(
        0xC,
        (
            "I heard there was a fire at\x01",
            "the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I saw all of the kids go by,\x01",
            "crying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I feel bad for them...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1107")

    label("loc_10AB")


    ChrTalk(
        0xC,
        (
            "I heard there was a fire at\x01",
            "the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I saw all of the kids go by,\x01",
            "crying...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1107")

    Jump("loc_1510")

    label("loc_110A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_117F")

    ChrTalk(
        0xC,
        (
            "I opened up a florist shop to help\x01",
            "cheer up this town a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Would you bracers like anything?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1510")

    label("loc_117F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1221")

    ChrTalk(
        0xC,
        (
            "The Mercia Orphanage is east\x01",
            "of the Gull Seaside Way, on a\x01",
            "little byroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Here, I'll mark it on your map for\x01",
            "you, so you don't lose your way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1510")

    label("loc_1221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1499")
    EventBegin(0x0)
    OP_69(0xC, 0x3E8)

    ChrTalk(
        0xC,
        "Hey, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FI have a question for you...\x02\x03",
            "You haven't seen a little boy in\x01",
            "a cap around here, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmm...let me think...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Was he a student's guest at\x01",
            "the Royal Academy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002FYes, actually!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FDo you know the boy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "He's not from this town.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I think he's one of the orphans...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "From Mercia Orphanage.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "A woman called Matron Theresa is\x01",
            "the administrator. She takes in kids\x01",
            "who've lost their parents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's just off the Gull Seaside Way,\x01",
            "to the east.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002FSo, the kid lives there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FLet's go check it out.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x40D)
    EventEnd(0x1)
    Jump("loc_1510")

    label("loc_1499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1510")

    ChrTalk(
        0xC,
        (
            "These flowers you see everywhere?\x01",
            "They're a breed called 'magnolia.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Aren't they positively gorgeous?\x02",
    )

    CloseMessageWindow()

    label("loc_1510")

    TalkEnd(0xC)
    Return()

    # Function_9_B16 end

    def Function_10_1514(): pass

    label("Function_10_1514")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1534")
    OP_4A(0x11, 0)

    ChrTalk(
        0xFE,
        "Wait!\x05\x02",
    )

    OP_4B(0x11, 0)
    Jump("loc_1C07")

    label("loc_1534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_1639")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E6")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "Were those guys picking on\x01",
            "Polly and the other kids?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You gotta make 'em pay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You just can't let people who\x01",
            "pick on everyone get away\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1636")

    label("loc_15E6")


    ChrTalk(
        0xFE,
        (
            "Everyone from the orphanage\x01",
            "came home crying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You gotta make 'em pay!\x02",
    )

    CloseMessageWindow()

    label("loc_1636")

    Jump("loc_1C07")

    label("loc_1639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_16D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16AA")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "Everyone from the orphanage\x01",
            "came back crying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How come? Was someone mean\x01",
            "to them?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CF")

    label("loc_16AA")


    ChrTalk(
        0xFE,
        "Who was being mean to everyone?\x02",
    )

    CloseMessageWindow()

    label("loc_16CF")

    Jump("loc_1C07")

    label("loc_16D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_170F")
    OP_4A(0x11, 0)

    ChrTalk(
        0xFE,
        "I'm sure glad I have lots of friends.\x05\x02",
    )

    OP_4B(0x11, 0)
    Jump("loc_1C07")

    label("loc_170F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_17F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A3")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "I think Clem ran outside in a\x01",
            "big hurry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if he did something bad\x01",
            "and got Matron Theresa mad at\x01",
            "him again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F4")

    label("loc_17A3")


    ChrTalk(
        0xFE,
        (
            "I wonder if Clem did something\x01",
            "bad and got Matron Theresa\x01",
            "mad at him again?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F4")

    Jump("loc_1C07")

    label("loc_17F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_1908")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188B")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "Everyone from the orphanage\x01",
            "came over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were all upset about\x01",
            "something, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what happened.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1905")

    label("loc_188B")


    ChrTalk(
        0xFE,
        (
            "Everyone from the orphanage\x01",
            "came over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were all upset about\x01",
            "something, though...\x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1905")

    Jump("loc_1C07")

    label("loc_1908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_19F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BE")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "*sigh* I wanna go play at\x01",
            "the orphanage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It must be nice, being like brothers\x01",
            "and sisters with all those kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wanna go play with everyone...\x02",
    )

    CloseMessageWindow()
    Jump("loc_19EE")

    label("loc_19BE")


    ChrTalk(
        0xFE,
        (
            "*sigh* I wanna go play at\x01",
            "the orphanage...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EE")

    Jump("loc_1C07")

    label("loc_19F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1A85")

    ChrTalk(
        0xFE,
        (
            "The kids at the orphanage come\x01",
            "to Manoria and play sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've met 'em a couple of times.\x01",
            "The matron is a really nice lady.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C07")

    label("loc_1A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_1B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF6")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "A boy in a cap? Oh, I know who\x01",
            "you mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Um, I saw him over by the\x01",
            "flower shop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B4A")

    label("loc_1AF6")


    ChrTalk(
        0xFE,
        (
            "If you're lookin' for a little boy,\x01",
            "I think I saw him over by the\x01",
            "flower shop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B4A")

    Jump("loc_1C07")

    label("loc_1B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1C07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC3")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "Are you guys travelers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I live over at the inn!\x01",
            "You oughtta stop in,\x01",
            "if you have time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C07")

    label("loc_1BC3")


    ChrTalk(
        0xFE,
        (
            "I live over at the inn!\x01",
            "You oughtta stop in,\x01",
            "if you have time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C07")

    TalkEnd(0x11)
    Return()

    # Function_10_1514 end

    def Function_11_1C0B(): pass

    label("Function_11_1C0B")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C51")
    OP_4A(0xB, 0)

    ChrTalk(
        0xFE,
        "#772FIt's no fun playing when Polly's 'IT.'\x05\x02",
    )

    OP_4B(0xB, 0)
    Jump("loc_1C8B")

    label("loc_1C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1C8B")
    OP_4A(0xB, 0)

    ChrTalk(
        0xFE,
        "#770FEveryone's doing better already!\x05\x02",
    )

    OP_4B(0xB, 0)

    label("loc_1C8B")

    TalkEnd(0xB)
    Return()

    # Function_11_1C0B end

    def Function_12_1C8F(): pass

    label("Function_12_1C8F")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D50")

    ChrTalk(
        0xFE,
        (
            "I'm so relieved that the matron\x01",
            "is here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know I have to learn to be\x01",
            "more grown up, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And someday, we can pay the\x01",
            "matron back for all that she's\x01",
            "done for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D9B")

    label("loc_1D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1D9B")

    ChrTalk(
        0xFE,
        "Thanks for helping Clem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He can be a real pain sometimes.\x02",
    )

    CloseMessageWindow()

    label("loc_1D9B")

    TalkEnd(0xD)
    Return()

    # Function_12_1C8F end

    def Function_13_1D9F(): pass

    label("Function_13_1D9F")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1DE5")
    OP_4A(0x12, 0)

    ChrTalk(
        0xFE,
        (
            "What are we gonna have for\x01",
            "snacks today...?\x05\x02",
        )
    )

    OP_4B(0x12, 0)
    Jump("loc_1E57")

    label("loc_1DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1E2A")
    OP_4A(0x12, 0)

    ChrTalk(
        0xFE,
        (
            "I wonder what's gonna go with\x01",
            "dinner tonight.\x05\x02",
        )
    )

    OP_4B(0x12, 0)
    Jump("loc_1E57")

    label("loc_1E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1E57")

    ChrTalk(
        0xFE,
        "What's Clem all worked up about?\x02",
    )

    CloseMessageWindow()

    label("loc_1E57")

    TalkEnd(0x12)
    Return()

    # Function_13_1D9F end

    def Function_14_1E5B(): pass

    label("Function_14_1E5B")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1E88")
    OP_4A(0x13, 0)

    ChrTalk(
        0xFE,
        "An' one an' two...\x05\x02",
    )

    OP_4B(0x13, 0)
    Jump("loc_1F04")

    label("loc_1E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1EB8")
    OP_4A(0x13, 0)

    ChrTalk(
        0xFE,
        "I'm playin' wif evvyone.\x05\x02",
    )

    OP_4B(0x13, 0)
    Jump("loc_1F04")

    label("loc_1EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1F04")

    ChrTalk(
        0xFE,
        (
            "Clem looked all upset when we had\x01",
            "puddin'. Was his puddin' bad?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F04")

    TalkEnd(0x13)
    Return()

    # Function_14_1E5B end

    def Function_15_1F08(): pass

    label("Function_15_1F08")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2127")
    OP_A2(0x6)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "#753FOh, my...Estelle?\x01",
            "Are you leaving...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FYeah...we've gotta go to Zeiss,\x01",
            "actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#753FOh, I see...\x02\x03",
            "#750FWe're all greatly indebted to you\x01",
            "for all that you've done.\x02\x03",
            "It pains me that I can't repay your\x01",
            "kindness like you deserve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FPlease, it's really fine.\x02\x03",
            "I'm really just glad that all those\x01",
            "kids are happy again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#750FEstelle...\x02\x03",
            "Please, be well and safe on your\x01",
            "journey to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThank you, ma'am. We wish you\x01",
            "all the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#751FOn behalf of everyone, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2186")

    label("loc_2127")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "#751FTake care, both of you...\x02\x03",
            "Please, be well and safe on your\x01",
            "journey to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2186")

    TalkEnd(0xFE)
    Return()

    # Function_15_1F08 end

    def Function_16_218A(): pass

    label("Function_16_218A")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    StopSound(0x64, 0x3D090, 0x0)
    SetChrPos(0x101, -2020, 8000, 57380, 180)
    SetChrPos(0x102, -3170, 8039, 57530, 180)
    OP_6D(-2500, 6000, -3290, 0)
    OP_6C(310000, 0)
    OP_6B(5900, 0)

    def lambda_21E9():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_21E9)
    Sleep(2000)

    def lambda_21FE():
        OP_6D(-2100, 7980, 57740, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21FE)
    StopSound(0x9470, 0x14C08, 0x1F40)
    OP_6B(3000, 8000)

    ChrTalk(
        0x101,
        (
            "#501F#6P*sigh*...\x01",
            "Civilization at last.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 90, 400)
    Sleep(200)
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#000F#6PAnd with all these pretty white\x01",
            "flowers blooming everywhere,\x01",
            "too...\x02\x03",
            "What did you say this place\x01",
            "was called?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FManoria. It's a little seaside\x01",
            "village with an inn.\x02\x03",
            "And the white flowers are a\x01",
            "type of hibiscus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#6PThey're so pretty...\x02\x03",
            "The ocean and the flowers together...\x01",
            "It smells great around here!\x02\x03",
            "#001FHmm... It also makes me kind of\x01",
            "hungry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019FHa ha ha. Only you could work\x01",
            "up an appetite from smelling\x01",
            "flowers.\x02\x03",
            "#011FJust make sure you eat the\x01",
            "food and not the flowers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F#4PHey, I'm a growing girl.\x02\x03",
            "It's almost noon, anyway, so\x01",
            "what would you say to lunch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FFine by me... But do we have\x01",
            "any provisions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#4PUmm...\x02\x03",
            "#000FWhy don't we get something local?\x01",
            "It's such a nice, quiet little town...\x02\x03",
            "I mean, we just got to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThat's true. Okay, let's go check\x01",
            "out the inn and tavern.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_16_218A end

    def Function_17_25E9(): pass

    label("Function_17_25E9")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(27790, 0, 18450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 35500, -80, 17000, 270)
    SetChrPos(0x101, 27300, 480, 20630, 0)
    SetChrPos(0x102, 27300, 480, 21630, 180)
    FadeToBright(1000, 0)
    OP_8E(0x8, 0x6B44, 0x3C, 0x41BE, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(
        0x8,
        (
            "#042FI've already checked here...\x02\x03",
            "#042FHe's not in the general store,\x01",
            "either...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_26EF():
        OP_6D(27520, 60, 16390, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_26EF)
    OP_8C(0x8, 270, 400)
    OP_8C(0x8, 180, 400)
    Sleep(200)
    OP_8C(0x8, 270, 400)
    Sleep(200)
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(
        0x8,
        "#043FDamn... Where could he be?\x02",
    )

    CloseMessageWindow()
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_8F(0x101, 0x6A90, 0x1F4, 0x4B8C, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        "#001FGet a move on, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWhoa, Estelle. Watch where\x01",
            "you're going, or...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_27CF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27CF)

    def lambda_27DD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27DD)

    def lambda_27EB():
        OP_8F(0xFE, 0x6AF4, 0x3C, 0x431C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27EB)
    WaitChrThread(0x101, 0x1)
    OP_22(0x7D, 0x0, 0x64)
    SetChrFlags(0x101, 0x4)

    def lambda_2815():
        OP_96(0xFE, 0x6A68, 0x14, 0x4574, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2815)

    def lambda_2833():
        OP_96(0xFE, 0x6B30, 0x46, 0x3D0E, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2833)
    OP_43(0x101, 0x2, 0x0, 0x12)

    ChrTalk(
        0x8,
        "#044F#4P#12AOof...\x05\x02",
    )


    ChrTalk(
        0x101,
        "#004F#3P#12AAck...\x05\x02",
    )

    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x102, 0x4)

    def lambda_2892():
        OP_8E(0xFE, 0x6C52, 0x1F4, 0x4B50, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2892)
    WaitChrThread(0x102, 0x1)
    ClearChrFlags(0x102, 0x4)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007FOwwww...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(400)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    ClearChrFlags(0x101, 0x4)
    OP_92(0x101, 0x8, 0x3E8, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        (
            "#004FI-I'm sorry! Are you okay?!\x02\x03",
            "I wasn't paying attention to where\x01",
            "I was going, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#040FNo, no... It's all right.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(400)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#045FPardon me. I confess, my attention\x01",
            "was elsewhere, as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FOh, okay.\x02\x03",
            "#001FSo I guess we're even.\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x4, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x4, 30)
    OP_70(0x4, 0x0)
    OP_8E(0x102, 0x6E78, 0xFFFFFFD8, 0x425E, 0x7D0, 0x0)
    TurnDirection(0x102, 0x8, 400)
    OP_71(0x4, 0x800)

    ChrTalk(
        0x102,
        (
            "#017FI swear, Estelle.\x01",
            "What are you doing?\x02\x03",
            "#014F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#040F???\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013FN-Nothing...\x02",
    )

    CloseMessageWindow()
    OP_92(0x102, 0x8, 0x4B0, 0x3E8, 0x0)

    def lambda_2AEE():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AEE)
    TurnDirection(0x8, 0x102, 0)

    ChrTalk(
        0x102,
        (
            "#010FI'm sorry if she disturbed you.\x02\x03",
            "You're not hurt, I hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#045FNo, I'm fine.\x02\x03",
            "I was looking for someone, and\x01",
            "I wasn't watching where I was\x01",
            "going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FOh, who are you looking for?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#040FA little boy, about ten years old,\x01",
            "wearing a cap.\x02\x03",
            "I don't suppose you've seen him,\x01",
            "by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FA boy in a cap...\x02\x03",
            "#000FYou see anyone like that,\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FNot that I can recall, no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#043FI see...\x01",
            "Where could he be?\x02\x03",
            "#045FIf you'll excuse me. Sorry to have\x01",
            "caused you any trouble.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    def lambda_2D16():

        label("loc_2D16")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D16")

    QueueWorkItem2(0x101, 1, lambda_2D16)

    def lambda_2D27():

        label("loc_2D27")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D27")

    QueueWorkItem2(0x102, 1, lambda_2D27)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_2D5C():
        OP_8E(0xFE, 0xA0BE, 0xFFFFFFEC, 0x48E4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2D5C)
    OP_6D(30950, -30, 16970, 2000)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    OP_63(0x101)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1200)
    OP_6D(28490, 40, 16850, 1000)
    OP_44(0x101, 0xFF)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002FJoshua?\x02\x03",
            "#002FHello... Calling Joshua, come in,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F#4POh, uhh... What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007FGee, I wonder.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#004FOh, I get it...\x02\x03",
            "#001FI see what's going on. 噴\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F#4PWhat half-baked idea are you\x01",
            "cooking up THIS time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FNow, now. No need to be shy\x01",
            "about it.\x02\x03",
            "I see the way she's set your\x01",
            "heart aflutter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F#4PAb-so-lute-ly NOT.\x02\x03",
            "I just think I've met her before,\x01",
            "a long time ago.\x02\x03",
            "#010FI was just surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FHmmmmm... 'Met her before,'\x01",
            "you say.\x02\x03",
            "#502FAs pick-up lines go, I give it\x01",
            "thirty points.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x102,
        (
            "#015F#4PMoving on...\x01",
            "Don't you recognize her uniform?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FNow that you mention it...\x02\x03",
            "Isn't that the same outfit that\x01",
            "Josette used as a disguise?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PYep. The Jenis Royal Academy\x01",
            "uniform.\x02\x03",
            "Since we're in Ruan, it's not all\x01",
            "that surprising to see someone\x01",
            "wearing one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FAhh... So that's the real thing,\x01",
            "then?\x02\x03",
            "#001FShe seemed polite and smart...\x01",
            "and refined.\x02\x03",
            "Totally different from that scruffy,\x01",
            "crude pretender, in other words!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4PWhat are you talking about?\x02\x03",
            "Josette had you completely\x01",
            "fooled from the get-go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#4POh, that's right. You teased me\x01",
            "about it THEN, too.\x02\x03",
            "Well, if you get taken for a\x01",
            "fool again, don't expect me\x01",
            "to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003FGrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#4PInstead of picking on me, why not\x01",
            "work on becoming a better judge\x01",
            "of character?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FAll right, all right!\x02\x03",
            "Fine, I won't pick on you\x01",
            "anymore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PGood.\x02\x03",
            "Now, why don't we go have lunch\x01",
            "up on the viewing platform?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007FFine...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x40A)
    EventEnd(0x0)
    Return()

    # Function_17_25E9 end

    def Function_18_3415(): pass

    label("Function_18_3415")

    Sleep(200)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x8, 11)
    Return()

    # Function_18_3415 end

    def Function_19_3425(): pass

    label("Function_19_3425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43C0")
    EventBegin(0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004FWow, check out this view!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYep, you can practically see\x01",
            "the entire ocean from here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34D8():
        OP_6D(2428, 6000, -13190, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34D8)

    def lambda_34F0():
        OP_6B(8450, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34F0)

    def lambda_3500():
        OP_6C(60000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3500)

    def lambda_3510():
        OP_67(0, 5095, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3510)
    StopSound(0x186A0, 0x3D090, 0x1B58)
    Sleep(7000)

    ChrTalk(
        0x101,
        (
            "#501FGetting to eat at a nice place like\x01",
            "this really makes it feel like\x01",
            "you're living it up, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt sure does.\x02\x03",
            "So, shall we have ourselves\x01",
            "a little picnic, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FSure!\x02\x03",
            "#001FI'm starving!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(5420, 6000, -13860, 0)
    OP_6B(2800, 0)
    OP_6C(51000, 0)
    OP_67(0, 9500, -10000, 0)
    StopSound(0x0, 0x0, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 12)
    SetChrChipByIndex(0x102, 13)
    SetChrPos(0x101, 5200, 6200, -13860, 180)
    SetChrPos(0x102, 6100, 6200, -13860, 180)
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0x102, 2)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#501F#3PGet a load of this smoked\x01",
            "ham sandwich!\x02\x03",
            "Mmmm, it smells so good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PI'm looking forward to eating my\x01",
            "seafood paella, personally.\x02\x03",
            "I love the smell of saffron.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#3PWell, let's dig in!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F#4PYes, let's.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#501F#3PTime for that first bite...\x02\x03",
            "#502F*chompmunchchew*...*gulp*\x02\x03",
            "#004FWow, it's as good as it smells!\x01",
            "The lettuce is super-fresh and\x01",
            "crunchy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThe paella's really good, too.\x01",
            "Just the right amount of saffron.\x02\x03",
            "My compliments to the chef.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#501F#3PHey, can I have a bite?\x02\x03",
            "I've never tried paella before.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)
    Sleep(300)

    ChrTalk(
        0x102,
        "#010F#4PAll right... How about we share?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#3PHmm...but my hands are full.\x02\x03",
            "I know! You can feed me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#4PFeed...you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#3PYep! Aaaahhhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F#4PThis is...a little embarrassing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#3POh, it's fine. It's not like\x01",
            "anyone's watching.\x02\x03",
            "Unless you can let loose, you'll\x01",
            "never enjoy yourself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F#4PIt's not being seen that makes it\x01",
            "embarrassing...\x02\x03",
            "I don't have much of a choice\x01",
            "here, do I?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Joshua fed Estelle a bite of the paella.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#502F#3P*munchchew*...*gulp*\x02\x03",
            "#501FMmmm, delicious. That's some\x01",
            "pretty fantastic seafood.\x02\x03",
            "I don't know what that sweet-\x01",
            "peppery smell is, but it really\x01",
            "adds something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#4PYeah, it's pretty good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#3POh. I'm being selfish, aren't I?\x02\x03",
            "#001FOkay, give this a try!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle pushed her sandwich into Joshua's mouth...perhaps a little too\x01",
            "enthusiastically.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x102,
        (
            "#014F#4PMmrrph...\x02\x03",
            "#015F*chewchewchew*...*gulp*\x02\x03",
            "#018F...That's pretty tasty, but you\x01",
            "really didn't have to do that,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F#3PHeh heh heh... I know.侓\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(5600, 6150, -15410, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(261, 0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrPos(0x101, 5150, 6150, -14900, 180)
    SetChrPos(0x102, 6010, 6000, -14900, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#001FAhhh, that hit the spot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PThe herbal tea we got with our meals\x01",
            "was pretty good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FYeah, it was nice and warming\x01",
            "without sitting all heavy.\x02\x03",
            "#007FThe breeze is so nice...\x01",
            "makes me kind of sleepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PThey say you shouldn't sleep right\x01",
            "after eating...\x02\x03",
            "...but maybe a little post-meal\x01",
            "nap isn't so bad, in moderation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FYeah...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F...Huh?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_22(0x8C, 0x0, 0x64)
    StopSound(0x9470, 0x20F58, 0x0)
    OP_6C(0, 0)

    def lambda_3FB5():

        label("loc_3FB5")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3FB5")

    QueueWorkItem2(0x102, 1, lambda_3FB5)

    def lambda_3FC6():

        label("loc_3FC6")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3FC6")

    QueueWorkItem2(0x101, 1, lambda_3FC6)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, -15000, 15680, -15710, 0)
    OP_69(0x9, 0x0)
    OP_6A(0x9)

    def lambda_4002():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4002)

    def lambda_4012():
        OP_6C(300000, 5000)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_4012)
    ClearChrFlags(0x9, 0x80)
    OP_8E(0x9, 0x4D58, 0x2CEC, 0xFFFFCFEA, 0x32C8, 0x0)
    OP_8E(0x9, 0x9B14, 0x2CEC, 0xFFFFFF92, 0x32C8, 0x0)
    OP_8E(0x9, 0xD804, 0x396C, 0x17CA, 0x32C8, 0x0)
    Fade(1000)
    SetChrFlags(0x9, 0x80)
    OP_6A(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x101, 9310, 6140, -12420, 90)
    SetChrPos(0x102, 8940, 6140, -13650, 90)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_6D(8900, 6000, -13650, 0)
    OP_6B(3000, 0)
    OP_6C(51000, 0)
    OP_67(0, 9500, -10000, 0)
    StopSound(0x9470, 0x14C08, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#004FHey, did you see that bird? It\x01",
            "looked like a seagull, except\x01",
            "it was huge!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6PYeah. The wings were a different\x01",
            "shape and the beak was sharp.\x02\x03",
            "Maybe it was a falcon or an eagle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FA white falcon...? Didn't know\x01",
            "they made 'em in that color!\x02\x03",
            "#001FHmm... I wonder if it's a sign of\x01",
            "good fortune in our future.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F#4PHa ha. That would be nice.\x02\x03",
            "#010FHey... I thought you were sleepy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#008FOh...\x02\x03",
            "Not anymore, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PMaybe we should get going, then?\x02\x03",
            "I'd like to check in with the Ruanian\x01",
            "guild branch, and get all our paperwork\x01",
            "squared away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FOh, right...\x02\x03",
            "Okay. I hate to leave, but I guess\x01",
            "we have to.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_3F(0x33C, 1)
    OP_A2(0x40B)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)

    label("loc_43C0")

    Return()

    # Function_19_3425 end

    def Function_20_43C1(): pass

    label("Function_20_43C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EA5")
    OP_A2(0x40C)
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(4130, 3990, 10660, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 4590, 5970, 3440, 0)
    SetChrPos(0x102, 5510, 5980, 2610, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, 180, 4050, 18030, 152)
    FadeToBright(500, 0)

    def lambda_4466():

        label("loc_4466")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4466")

    QueueWorkItem2(0x101, 3, lambda_4466)

    def lambda_4477():
        OP_8E(0xFE, 0x10CC, 0xF82, 0x2C9C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4477)
    Sleep(500)

    def lambda_4497():
        OP_8E(0xFE, 0x1464, 0xFAA, 0x25D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4497)
    Sleep(1200)

    def lambda_44B7():
        OP_8E(0xFE, 0x10A4, 0xF8C, 0x2ECC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_44B7)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xA, 0x1)
    OP_22(0x7D, 0x0, 0x64)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xA, 0x4)
    TurnDirection(0xA, 0x101, 0)

    def lambda_44F2():
        OP_96(0xFE, 0x1126, 0xF8C, 0x28B4, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44F2)

    def lambda_4510():
        OP_96(0xFE, 0x1108, 0xF78, 0x335E, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4510)
    OP_43(0x101, 0x2, 0x0, 0x15)
    OP_3F(0x35C, 1)

    ChrTalk(
        0xA,
        "#774F#4P#12AWhoa!\x05\x02",
    )


    ChrTalk(
        0x101,
        "#004F#3P#12AOw...\x05\x02",
    )

    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007FToday...must be my day for just\x01",
            "randomly running into people...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0xA, 0x4)
    OP_8E(0xA, 0x114E, 0xF96, 0x2D3C, 0xBB8, 0x0)

    ChrTalk(
        0xA,
        (
            "#771F#4PSorry 'bout that. I'm just\x01",
            "looking for somebody.\x02\x03",
            "#770FSay, you're not from around\x01",
            "here, are you?\x02",
        )
    )

    CloseMessageWindow()
    Fade(400)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#000FNope. We're from out of town.\x02\x03",
            "#004FHey, aren't you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#772F#4P...Wh-What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FWe ran into a girl who said she\x01",
            "was looking for a boy who was\x01",
            "wearing a cap...\x02\x03",
            "You know anything about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#770F#4POh! I'm looking for her, actually.\x02\x03",
            "Where'd you see her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FOver by the tavern...\x02\x03",
            "It was a while ago, though, so\x01",
            "I'm not sure where she went.\x02\x03",
            "Would you like us to help\x01",
            "you search?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#774F#4PN-No, that's okay. I'm pretty\x01",
            "sure I can find her.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_95(0xA, 0x0, 0x0, 0x0, 0x320, 0x1770)

    ChrTalk(
        0xA,
        "#771F#4POkay, bye!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)

    def lambda_488C():

        label("loc_488C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_488C")

    QueueWorkItem2(0x102, 3, lambda_488C)

    def lambda_489D():
        OP_6D(7160, 4030, 12560, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_489D)
    OP_8E(0xA, 0x41C8, 0x6B8, 0x3958, 0x1770, 0x0)
    SetChrFlags(0xA, 0x80)
    WaitChrThread(0xA, 0x2)

    ChrTalk(
        0x101,
        (
            "#501F#4PThat kid seems pretty energetic.\x02\x03",
            "He reminds me a little of Luke,\x01",
            "back in Rolent.\x02\x03",
            "I wonder what the kids are up\x01",
            "to now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_4970():
        OP_6D(4380, 4019, 9800, 1200)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4970)
    OP_44(0x101, 0x3)
    OP_8C(0x101, 90, 400)
    WaitChrThread(0xA, 0x2)

    ChrTalk(
        0x101,
        "#004F#4PWhat's wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0x102)
    OP_44(0x102, 0x3)
    OP_8C(0x102, 0, 400)

    ChrTalk(
        0x102,
        (
            "#014F#3PIt...might just be my imagination, but...\x02\x03",
            "...have you lost anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4PLost...what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#3PAnything you're wearing.\x02\x03",
            "Like a money pouch or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#4PWhy are you asking all of a\x01",
            "sudden?\x02\x03",
            "#006FLet's see...\x01",
            "Pouch...check.\x02\x03",
            "Hairbands...check.\x02\x03",
            "#501FBracer emblem...\x02\x03",
            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#015F#3PI knew it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#4PWhat the...?! Where is it?!\x02\x03",
            "Did I drop it on the mountain\x01",
            "pass or something?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#3PCalm down.\x02\x03",
            "I remember that you had it\x01",
            "when we were eating lunch.\x02\x03",
            "If you lost it, it has to be\x01",
            "somewhere around here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 180, 400)
    Sleep(200)
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 0, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#002F#4PB-But...where around here?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        "#004F#4POh, no way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3PYeah, I'm thinking the same thing.\x01",
            "It was probably that kid.\x02\x03",
            "I'll bet it happened when he\x01",
            "'accidentally' ran into you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#4P...WHAT?!\x02\x03",
            "Why would he want my\x01",
            "bracer emblem?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#3PWhat reason does a kid have\x01",
            "for wanting anything?\x02\x03",
            "He probably just took it because\x01",
            "he could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#4PGrrrr... Oh, he is in SO much\x01",
            "trouble!\x02\x03",
            "#005FOnce I get my hands on him, he's\x01",
            "gonna get the spanking of his life!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3PNow, calm down...\x02\x03",
            "For now, let's focus on figuring\x01",
            "out where he is.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_4EA5")

    Return()

    # Function_20_43C1 end

    def Function_21_4EA6(): pass

    label("Function_21_4EA6")

    Sleep(200)
    SetChrChipByIndex(0x101, 14)
    Return()

    # Function_21_4EA6 end

    def Function_22_4EB1(): pass

    label("Function_22_4EB1")

    EventBegin(0x0)
    OP_6D(26870, 100, 17110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xD, 39130, -90, 16600, 270)
    SetChrPos(0x101, 26280, 40, 17460, 180)
    SetChrPos(0x102, 26250, 70, 16210, 0)
    SetChrPos(0x136, 27640, 40, 17110, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002FThis sure has turned into a\x01",
            "royal mess.\x02\x03",
            "Where should we start the search?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4PHmm...\x02\x03",
            "Maybe we should go to the guild\x01",
            "and report back to Jean.\x02\x03",
            "We can figure out a plan of\x01",
            "attack then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FSounds good to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#049F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x136, 400)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        (
            "#004FSomething wrong? You look like\x01",
            "something's bugging you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#045FOh, I'm sorry...\x02\x03",
            "My mind is just all over the\x01",
            "place right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003FI know how you feel...\x02\x03",
            "#501FBy the way, Joseph was Matron\x01",
            "Theresa's husband, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#048FYes.\x02\x03",
            "He died several years ago...\x02\x03",
            "But he meant a great deal to\x01",
            "me, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FI see...\x02\x03",
            "#004FWait, does that mean...you're\x01",
            "from the orphanage, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#045FNo, nothing like that...\x02\x03",
            "He just did a huge favor for me\x01",
            "a long time ago.\x02\x03",
            "We grew close again when I came\x01",
            "to Ruan to attend the Academy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FOh, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FSo in other words, every time\x01",
            "you came by to play you ended\x01",
            "up helping out, like part of the family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#048FYes...\x02\x03",
            "#047F...\x02\x03",
            "#049FHe was like a father to me...but the shock\x01",
            "I experienced was nothing compared to that\x01",
            "of the matron and the other children.\x02\x03",
            "But we managed somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3PMiss Kloe!\x02",
    )

    CloseMessageWindow()
    OP_62(0x136, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_4A(0xD, 255)
    ClearChrFlags(0xD, 0x80)

    def lambda_53E7():
        OP_6D(28370, 100, 17960, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_53E7)

    def lambda_53FF():

        label("loc_53FF")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_53FF")

    QueueWorkItem2(0x136, 1, lambda_53FF)

    def lambda_5410():

        label("loc_5410")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5410")

    QueueWorkItem2(0x101, 1, lambda_5410)

    def lambda_5421():

        label("loc_5421")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5421")

    QueueWorkItem2(0x102, 1, lambda_5421)
    OP_62(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xD, 0x7198, 0xFFFFFF88, 0x4380, 0x1388, 0x0)

    ChrTalk(
        0x136,
        (
            "#044FMary! What's gotten you into\x01",
            "such a hurry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2PListen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2PClem's gone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FY-You don't mean he's left\x01",
            "Manoria...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FCan you give us some more\x01",
            "details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2POkay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2PAfter that old man showed up,\x01",
            "Clem went upstairs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2PIn a coupla minutes, he came back\x01",
            "down all red in the face saying,\x01",
            "'They're not gettin' away with this!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2PThen he just ran off!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FI wonder who he meant...?\x02\x03",
            "You don't suppose it's...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[The orphanage's arsonist]\x01",           # 0
            "[Mayor Dalmore and his steward]\x01",      # 1
            "[The gang at the warehouse]\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_56E2"),
        (1, "loc_575D"),
        (2, "loc_57D7"),
        (SWITCH_DEFAULT, "loc_583B"),
    )


    label("loc_56E2")


    ChrTalk(
        0x102,
        (
            "#012FI'll bet you're right...\x02\x03",
            "Everything points at the Ravens.\x02\x03",
            "He probably overheard what\x01",
            "the steward said.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x3B, 0x1)
    Jump("loc_583B")

    label("loc_575D")


    ChrTalk(
        0x102,
        (
            "#017FWhy would you say that?\x02\x03",
            "#012FEverything points at the Ravens.\x02\x03",
            "He probably overheard what\x01",
            "the steward said.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_583B")

    label("loc_57D7")


    ChrTalk(
        0x102,
        (
            "#013FYes... I believe it was the Ravens.\x02\x03",
            "He probably overheard what\x01",
            "the steward said.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x3B, 0x2)
    Jump("loc_583B")

    label("loc_583B")


    ChrTalk(
        0x101,
        (
            "#004FOh, no!\x02\x03",
            "I hope he's not planning to go\x01",
            "and find them himself...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x136, 0xFF)
    OP_8C(0x136, 270, 400)

    ChrTalk(
        0x136,
        (
            "#043F#2PIt... It can't be...\x02\x03",
            "#042FI can't allow this! I have to find\x01",
            "him at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWe'll come with you.\x02\x03",
            "If we hurry, we might be able\x01",
            "to catch him before he gets to\x01",
            "Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2PMiss Kloe...\x02",
    )

    CloseMessageWindow()

    def lambda_5967():

        label("loc_5967")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5967")

    QueueWorkItem2(0x136, 1, lambda_5967)
    Sleep(400)

    ChrTalk(
        0x136,
        (
            "#042FDon't you worry.\x01",
            "I'll bring him back safely.\x02\x03",
            "You just look after the other\x01",
            "children, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2POkay... Good luck!\x02",
    )

    CloseMessageWindow()

    def lambda_5A03():
        OP_6D(26760, 100, 17100, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A03)
    OP_8E(0xD, 0x6B62, 0x1F4, 0x4AA6, 0xBB8, 0x0)
    OP_8C(0xD, 0, 400)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    SetChrFlags(0xD, 0x4)
    OP_8E(0xD, 0x6CFC, 0x1F4, 0x52D0, 0xBB8, 0x0)
    SetChrFlags(0xD, 0x80)
    OP_72(0x4, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x4, 30)
    OP_70(0x4, 0x0)
    OP_71(0x4, 0x800)
    OP_73(0x4)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)
    TurnDirection(0x102, 0x136, 400)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        "#002FLet's head back to Ruan!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x136, 270, 400)

    ChrTalk(
        0x136,
        "#042FAll right...!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_22_4EB1 end

    def Function_23_5AD7(): pass

    label("Function_23_5AD7")

    EventBegin(0x0)
    OP_77(0x41, 0x64, 0x82, 0x0, 0x0)
    OP_6D(27410, 20, 17820, 0)
    OP_6C(315000, 0)
    SetChrChipByIndex(0x106, 16)
    SetChrPos(0x106, 27180, 500, 20940, 0)
    SetChrPos(0x101, 27180, 500, 20940, 0)
    SetChrPos(0x102, 27180, 500, 20940, 0)
    SetChrPos(0x105, 27180, 500, 20940, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_70(0x4, 0x1E)
    OP_73(0x4)

    def lambda_5B5F():
        OP_8E(0xFE, 0x6BF8, 0x0, 0x41A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B5F)
    Sleep(500)

    def lambda_5B7F():
        OP_8E(0xFE, 0x6914, 0x0, 0x44B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B7F)
    Sleep(500)

    def lambda_5B9F():
        OP_8E(0xFE, 0x7058, 0x0, 0x4434, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B9F)
    Sleep(500)

    def lambda_5BBF():
        OP_8E(0xFE, 0x6CF2, 0x0, 0x470E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5BBF)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#004FWow, how'd it get to be so late?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x106, 0x1)
    OP_6F(0x4, 30)
    OP_70(0x4, 0x0)

    ChrTalk(
        0x106,
        (
            "#057FBah... This is no good.\x02\x03",
            "How are we supposed to search\x01",
            "in the dark?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 16500, 6000, 10000, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We should be able to hear Sieg,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x106, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5D21():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D21)

    def lambda_5D2F():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D2F)

    def lambda_5D3D():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D3D)

    def lambda_5D4B():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5D4B)
    Sleep(500)

    ChrTalk(
        0x106,
        "#052FHey, what was that sound?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    ClearChrFlags(0x9, 0x80)

    def lambda_5D8C():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_5D8C)

    def lambda_5D9C():

        label("loc_5D9C")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_5D9C")

    QueueWorkItem2(0x101, 1, lambda_5D9C)

    def lambda_5DAD():

        label("loc_5DAD")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_5DAD")

    QueueWorkItem2(0x102, 1, lambda_5DAD)

    def lambda_5DBE():

        label("loc_5DBE")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_5DBE")

    QueueWorkItem2(0x106, 1, lambda_5DBE)
    OP_92(0x9, 0x136, 0x1388, 0x2710, 0x0)
    OP_92(0x9, 0x136, 0xFA0, 0x1F40, 0x0)
    OP_92(0x9, 0x136, 0xBB8, 0x1770, 0x0)
    OP_92(0x9, 0x136, 0x7D0, 0xBB8, 0x0)
    OP_44(0x106, 0x1)
    OP_8C(0x106, 180, 0)
    OP_8E(0x9, 0x7292, 0x384, 0x41DC, 0x5DC, 0x0)
    OP_44(0x101, 0x1)
    OP_8C(0x101, 45, 0)

    def lambda_5E31():
        OP_8C(0xFE, 270, 200)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_5E31)
    SetChrChipByIndex(0x105, 15)
    SetChrSubChip(0x105, 3)
    SetChrFlags(0x105, 0x20)
    OP_8C(0x105, 225, 200)
    OP_8F(0x9, 0x7224, 0x64, 0x42C2, 0x3E8, 0x0)
    WaitChrThread(0x9, 0x3)
    Sleep(100)
    Fade(250)
    SetChrFlags(0x9, 0x80)
    SetChrSubChip(0x105, 1)
    SetChrFlags(0x105, 0x20)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x105,
        "#044FOh, Sieg. Where have you been?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#055FWh-What the hell...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4PThat's Sieg. He's Kloe's gyrfalcon\x01",
            "companion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#055FWhew... As long as he's friendly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#310FScreeee!\x02\x03",
            "Scree, scree!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047FUnderstood.\x02\x03",
            "#042FThank you, Sieg.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#311FScree! 仚\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053FNow I've seen everything.\x02\x03",
            "#051FSo, missy. What did your friend\x01",
            "there tell you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042FThe whereabouts of the ruffians who\x01",
            "assaulted Matron Theresa, evidently.\x02\x03",
            "It seems that he saw the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#051FHa ha ha! That's a good one...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#4PNice going, Sieg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#3PYes, most impressive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#311FScree! 侓\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x106,
        (
            "#055FNow wait one damn minute!\x02\x03",
            "You mean to tell me you actually\x01",
            "believe that load of bull?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#3PWe've seen him communicate\x01",
            "several times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4PHey, if you don't believe us,\x01",
            "you don't have to come along.\x02\x03",
            "Come on, guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040FAll right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#310FScreee!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x9, 0x80)
    SetChrSubChip(0x105, 3)
    OP_8C(0x105, 270, 0)

    def lambda_6239():
        OP_8E(0xFE, 0x4074, 0x1770, 0x3584, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6239)
    Sleep(100)

    def lambda_6259():
        OP_8E(0xFE, 0x4074, 0x1770, 0x3584, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6259)
    Sleep(100)

    def lambda_6279():

        label("loc_6279")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6279")

    QueueWorkItem2(0x101, 1, lambda_6279)

    def lambda_628A():

        label("loc_628A")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_628A")

    QueueWorkItem2(0x102, 1, lambda_628A)
    SetChrChipByIndex(0x105, 65535)
    ClearChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 0)

    def lambda_62AA():
        OP_8E(0xFE, 0x4074, 0x1770, 0x3584, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_62AA)
    Sleep(100)

    def lambda_62CA():

        label("loc_62CA")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_62CA")

    QueueWorkItem2(0x106, 1, lambda_62CA)

    def lambda_62DB():
        OP_8E(0xFE, 0x4074, 0x1770, 0x3584, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_62DB)
    Sleep(100)

    def lambda_62FB():
        OP_8E(0xFE, 0x4074, 0x1770, 0x3584, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_62FB)
    Sleep(500)
    OP_44(0x101, 0xFF)

    def lambda_631F():
        OP_8E(0xFE, 0x2D64, 0xFBE, 0x3A84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_631F)
    Sleep(500)
    OP_44(0x102, 0xFF)

    def lambda_6343():
        OP_8E(0xFE, 0x2D64, 0xFBE, 0x3A84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6343)
    Sleep(100)

    def lambda_6363():
        OP_8E(0xFE, 0x2D64, 0xFBE, 0x3A84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6363)
    Sleep(1000)

    ChrTalk(
        0x106,
        (
            "#055FUmm...\x02\x03",
            "#054FW-Wait up, you punks!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_62(0x106, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)

    def lambda_63CC():
        OP_8E(0xFE, 0x2D64, 0xFBE, 0x3A84, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_63CC)
    OP_0D()
    OP_A2(0x3FA)
    SetMapFlags(0x2000000)
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT01/R2101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_5AD7 end

    def Function_24_63F9(): pass

    label("Function_24_63F9")

    EventBegin(0x0)
    OP_B8(0x5)
    RemoveParty(0x5, 0xFF)
    SetChrPos(0x101, 6920, 5980, -1940, 225)
    SetChrPos(0x102, 6130, 6000, -1360, 180)
    SetChrPos(0x105, 7280, 5980, -2810, 270)
    OP_8C(0x14, 45, 0)
    OP_4A(0x14, 255)
    OP_6D(5680, 6000, -2120, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x14,
        (
            "#830FNow then... I'll keep an eye on\x01",
            "things here.\x02\x03",
            "Could you return to Ruan and\x01",
            "report back to Jean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#4PThat's fine with me, but are\x01",
            "you sure you'll be okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#831FC'mon, I just got a whiff of\x01",
            "sleeping powder is all.\x02\x03",
            "#835FIt all happened a little too\x01",
            "fast for me to remember who\x01",
            "attacked me, though...\x02\x03",
            "Pretty shameful, I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FDon't beat yourself up over it.\x02\x03",
            "You still managed to fend off\x01",
            "four attackers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040FThe children are safe thanks\x01",
            "to you.\x02\x03",
            "I can't thank you enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#835FHa ha... Well, I guess there's\x01",
            "that, at least.\x02\x03",
            "#833FStill, will Agate be okay facing\x01",
            "them on his own?\x02\x03",
            "#834FI know he's tough and all,\x01",
            "but it still worries me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#4PY-Yeah... If they somehow\x01",
            "manage to get the drop on\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FFor now, we just have to trust\x01",
            "that he knows what he's doing. \x02\x03",
            "He's been after those guys\x01",
            "for a while now.\x02\x03",
            "#010FHe knows how they work, so I think\x01",
            "they'll have a tough time taking\x01",
            "him on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4PYeah, I guess you're right.\x02\x03",
            "We'll just have to focus on\x01",
            "what WE can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#830FYou're right.\x01",
            "You're exactly right.\x02\x03",
            "I'll hang on to the donated money until the\x01",
            "matron wakes up. If those guys want it, they'll\x01",
            "have to pry it from my cold, dead fingers!\x02\x03",
            "You can count on me. I'll be\x01",
            "fine, so you go on ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#041FAll right...be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#4PLet's go, guys!\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_8C(0x14, 90, 400)
    OP_4B(0x14, 255)
    EventEnd(0x0)
    Return()

    # Function_24_63F9 end

    def Function_25_69F8(): pass

    label("Function_25_69F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AF9")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AA7")
    OP_A2(0x7)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000FHey, it's about noon, so why\x01",
            "don't we break for lunch?\x02\x03",
            "It'll just be a minute.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010FOkay. Let's find a place to eat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AF2")

    label("loc_6AA7")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000FIt'll just take a minute, so let's\x01",
            "find somewhere to eat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AF2")

    Call(0, 26)
    Jump("loc_6F18")

    label("loc_6AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B7C")
    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FThe highway is this way.\x02\x03",
            "I think the windmill outside of\x01",
            "town has a viewing platform on\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 26)
    Jump("loc_6F18")

    label("loc_6B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CD1")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C21")
    OP_A2(0x7)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012FWait. We're not even sure where\x01",
            "that kid went.\x02\x03",
            "Let's figure out where he is first before\x01",
            "we start wandering aimlessly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CCA")

    label("loc_6C21")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012FHold on a sec, Estelle. We still don't know\x01",
            "where that kid is.\x02\x03",
            "I think the best course of action now would\x01",
            "be to ask around town if anyone's seen him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CCA")

    Call(0, 26)
    Jump("loc_6F18")

    label("loc_6CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E38")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D5C")

    ChrTalk(
        0x106,
        (
            "#050FWe ain't got time to go back\x01",
            "to Ruan...\x02\x03",
            "Bah, whatever. I guess we'll\x01",
            "just have to bet on the bird.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E31")

    label("loc_6D5C")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(
        0x106,
        (
            "#050FHey, where do you think you're\x01",
            "going?\x02\x03",
            "We ain't got time to go back\x01",
            "to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6DC0():
        TurnDirection(0x105, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6DC0)

    def lambda_6DCE():
        TurnDirection(0x101, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DCE)
    TurnDirection(0x102, 0x106, 400)

    ChrTalk(
        0x102,
        (
            "#012FIndeed.\x02\x03",
            "For now, let's just follow Sieg's\x01",
            "trail, and see where it leads.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E31")

    Call(0, 26)
    Jump("loc_6F18")

    label("loc_6E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F18")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EB9")

    ChrTalk(
        0x106,
        (
            "#050FWe ain't got time to go back\x01",
            "to Ruan.\x02\x03",
            "Let's head back to the lighthouse\x01",
            "and settle this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F14")

    label("loc_6EB9")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(
        0x106,
        (
            "#050FHey, where do you think you're\x01",
            "going?\x02\x03",
            "Let's head back to the lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F14")

    Call(0, 26)

    label("loc_6F18")

    Return()

    # Function_25_69F8 end

    def Function_26_6F19(): pass

    label("Function_26_6F19")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_26_6F19 end

    def Function_27_6F35(): pass

    label("Function_27_6F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FB8")
    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FThe highway is this way.\x02\x03",
            "I think the windmill outside of\x01",
            "town has a viewing platform on\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 28)
    Jump("loc_7308")

    label("loc_6FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70B9")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_703E")
    OP_A2(0x7)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012FLet's figure out where that kid\x01",
            "went first.\x02\x03",
            "We can worry about following him\x01",
            "afterward.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70B2")

    label("loc_703E")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012FLet's figure out where that kid\x01",
            "went first.\x02\x03",
            "From what the villagers said,\x01",
            "he was in a real hurry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70B2")

    Call(0, 28)
    Jump("loc_7308")

    label("loc_70B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7267")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7159")

    ChrTalk(
        0x101,
        (
            "#002FOops... This way leads to the\x01",
            "Krone Pass.\x02\x03",
            "If we want to get back to Ruan,\x01",
            "we should use the east entrance\x01",
            "to the beach.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7260")

    label("loc_7159")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71E1")

    ChrTalk(
        0x102,
        (
            "#012FThe Manoria Byroad is this way.\x02\x03",
            "If we want to get back to Ruan,\x01",
            "we should use the east entrance\x01",
            "to the beach.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7260")

    label("loc_71E1")


    ChrTalk(
        0x105,
        (
            "#042FThis way leads to the Manoria\x01",
            "Byroad.\x02\x03",
            "If we want to get back to Ruan,\x01",
            "we should use the east entrance\x01",
            "to the beach.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7260")

    Call(0, 28)
    Jump("loc_7308")

    label("loc_7267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7308")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_728B")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_7292")

    label("loc_728B")

    TurnDirection(0x102, 0x0, 400)

    label("loc_7292")


    ChrTalk(
        0x102,
        (
            "#012FThe highway is this way.\x02\x03",
            "We have to find Matron Theresa first.\x01",
            "She's got to still be here, in Manoria.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 28)

    label("loc_7308")

    Return()

    # Function_27_6F35 end

    def Function_28_7309(): pass

    label("Function_28_7309")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_28_7309 end

    def Function_29_7325(): pass

    label("Function_29_7325")

    SetPlaceName(0x58) # 玛诺利亚村　村长家
    Return()

    # Function_29_7325 end

    def Function_30_7329(): pass

    label("Function_30_7329")

    SetPlaceName(0x57) # 玛诺利亚村　村长家
    Return()

    # Function_30_7329 end

    def Function_31_732D(): pass

    label("Function_31_732D")

    SetPlaceName(0x59) # 玛诺利亚村　村长家
    Return()

    # Function_31_732D end

    SaveToFile()

Try(main)
