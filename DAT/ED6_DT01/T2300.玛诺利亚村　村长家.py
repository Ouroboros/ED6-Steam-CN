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
        '穿制服的少女',                         # 9
        '基库',                                 # 10
        '戴帽子的男孩',                         # 11
        '克拉姆',                               # 12
        '萨蒂',                                 # 13
        '玛丽',                                 # 14
        '阿梅莉娅',                             # 15
        '照相机',                               # 16
        '奥维德',                               # 17
        '卢希娅',                               # 18
        '达尼艾尔',                             # 19
        '波利',                                 # 20
        '卡露娜',                               # 21
        '特蕾莎院长',                           # 22
        '玛诺利亚间道方向',                     # 23
        '梅威海道方向',                         # 24
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
            "那帮家伙由我看着。\x02\x03",
            "你们就赶去卢安，\x01",
            "向嘉恩报告昨天的事情吧。\x02",
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
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
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
        (
            "孩子们的脸上\x01",
            "总算又展露了笑容……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不过犯人竟然是\x01",
            "那个戴尔蒙市长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我想总有一天\x01",
            "孩子们会知道真相的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D06")

    label("loc_C65")


    ChrTalk(
        0xC,
        (
            "不过犯人竟然是\x01",
            "那个戴尔蒙市长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我想总有一天\x01",
            "孩子们会知道真相的……\x02",
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
        (
            "听说那些纵火犯\x01",
            "都被抓住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "虽然松了一口气，\x01",
            "不过我的心情还是很悲伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "事情虽然解决了，\x01",
            "但是孩子们的心灵创伤是不会这么简单痊愈的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E08")

    label("loc_DB9")


    ChrTalk(
        0xC,
        (
            "事情虽然解决了，\x01",
            "但是孩子们的心灵创伤是不会这么简单痊愈的。\x02",
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
            "听说特蕾莎老师被袭击，\x01",
            "还受了伤啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "啊啊，爱德丝啊……\x01",
            "您究竟想对\x01",
            "老师和孩子们做什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "求你们了，游击士。\x01",
            "一定要抓住犯人们！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EEF")

    label("loc_EC0")


    ChrTalk(
        0xC,
        (
            "啊啊，爱德丝啊……\x01",
            "您究竟想对\x01",
            "老师和孩子们做什么啊。\x02",
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
            "孤儿院的孩子们\x01",
            "最近好像有点精神了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "女孩子们\x01",
            "经常到这里来玩呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1510")

    label("loc_F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_101E")

    ChrTalk(
        0xC,
        (
            "一个孤儿院的男孩子\x01",
            "刚才飞快地奔出去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "发生什么事了吗……\x01",
            "我有点担心呢。\x02",
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
        "听说孤儿院着火了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "刚才孩子们\x01",
            "都哭着从这里走过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "好可怜啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1107")

    label("loc_10AB")


    ChrTalk(
        0xC,
        "听说孤儿院着火了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "刚才孩子们\x01",
            "都哭着从这里走过……\x02",
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
            "我想给婆婆多少帮点忙，\x01",
            "于是就开了一间花店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "各位游击士，\x01",
            "来一束花怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1510")

    label("loc_117F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1221")

    ChrTalk(
        0xC,
        (
            "要去玛西亚孤儿院的话，\x01",
            "走东边的梅威海道然后拐入岔道，\x01",
            "这样你们就可以找到那里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "如果没有看漏路标的话，\x01",
            "应该很快就能找到的。\x02",
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
        "哎呀，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F我们有件事想请问您……\x02\x03",
            "您有没有在这附近\x01",
            "见到一个戴帽子的男孩呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "戴帽子的男孩……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "啊啊……\x01",
            "他不就是那个王立学院女学生的朋友吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯，就是那孩子！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请问你知道他是哪家的孩子吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "他不是这村子的孩子呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "我想他应该是孤儿院的孩子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F孤儿院……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "嗯，就是『玛西亚孤儿院』。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "由一位叫特蕾莎的女士\x01",
            "所开设的慈善设施。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "走东面的梅威海道就会经过那里的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F原来那孩子是住在孤儿院的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们也去孤儿院那边看看吧。\x02",
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
            "在村子里绽放的是\x01",
            "一种名为美洲木兰的木莲花。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "嘿嘿，\x01",
            "是不是非常漂亮可爱呢？\x02",
        )
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
        "等一下～！\x05\x02",
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
            "那些大哥哥\x01",
            "是不是欺负波利了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姐姐，\x01",
            "你们去教训他们吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "欺负大家的人，\x01",
            "是绝对不能原谅的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1636")

    label("loc_15E6")


    ChrTalk(
        0xFE,
        (
            "那些大哥哥\x01",
            "是不是欺负波利了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姐姐，\x01",
            "你们去教训他们吧！\x02",
        )
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
            "孤儿院的大家\x01",
            "都一边哭一边回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么回事？\x01",
            "是谁欺负他们了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CF")

    label("loc_16AA")


    ChrTalk(
        0xFE,
        "是谁欺负他们了？\x02",
    )

    CloseMessageWindow()

    label("loc_16CF")

    Jump("loc_1C07")

    label("loc_16D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_170F")
    OP_4A(0x11, 0)

    ChrTalk(
        0xFE,
        (
            "我交了好多朋友，\x01",
            "真开心。\x05\x02",
        )
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
            "克拉姆\x01",
            "刚才飞奔出去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是不是又做了什么坏事，\x01",
            "惹特蕾莎老师生气了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F4")

    label("loc_17A3")


    ChrTalk(
        0xFE,
        (
            "克拉姆是不是又做了什么坏事，\x01",
            "惹特蕾莎老师生气了？\x02",
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
            "孤儿院的大家\x01",
            "都到我家里来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家好像\x01",
            "非常痛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "该怎么办呢，我很担心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1905")

    label("loc_188B")


    ChrTalk(
        0xFE,
        (
            "孤儿院的大家\x01",
            "都到我家里来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家好像非常痛苦啊……\x01",
            "该怎么办呢，我很担心啊。\x02",
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
            "啊，\x01",
            "卢希娅也想去孤儿院玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家都像兄妹一样，\x01",
            "相处得好开心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好想和他们一起玩啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19EE")

    label("loc_19BE")


    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "卢希娅也想去孤儿院玩啊。\x02",
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
            "孤儿院的孩子们\x01",
            "有时候会来玛诺利亚村玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我碰到过他们好几次了。\x01",
            "特蕾莎老师非常温柔。\x02",
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
            "戴帽子的男孩子？\x01",
            "难道你们说的是他吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "我好像在花店那里看到过……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B4A")

    label("loc_1AF6")


    ChrTalk(
        0xFE,
        (
            "那个男孩子，\x01",
            "我好像在花店那里看到过……\x02",
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
        "大姐姐，你们是来旅游的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家是酒馆兼旅馆。\x01",
            "不介意的话就住我家吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C07")

    label("loc_1BC3")


    ChrTalk(
        0xFE,
        (
            "我家是酒馆兼旅馆。\x01",
            "不介意的话就住我家吧。\x02",
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
        (
            "#772F如果让波利当鬼的话，\x01",
            "游戏就没有意思了。\x05\x02",
        )
    )

    OP_4B(0xB, 0)
    Jump("loc_1C8B")

    label("loc_1C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1C8B")
    OP_4A(0xB, 0)

    ChrTalk(
        0xFE,
        (
            "#770F大家都已经很有精神了！\x01",
            "　\x05\x02",
        )
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
            "有老师在旁边，\x01",
            "果然感到很安心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但我们总有一天\x01",
            "必须要自立的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那时侯大家都要\x01",
            "好好报答老师呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D9B")

    label("loc_1D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1D9B")

    ChrTalk(
        0xFE,
        (
            "姐姐，\x01",
            "谢谢你们救了克拉姆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个孩子\x01",
            "真的很乱来。\x02",
        )
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
        "今天的饭会是什么呢～\x05\x02",
    )

    OP_4B(0x12, 0)
    Jump("loc_1E57")

    label("loc_1DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1E2A")
    OP_4A(0x12, 0)

    ChrTalk(
        0xFE,
        "今天的饭会是什么呢～\x05\x02",
    )

    OP_4B(0x12, 0)
    Jump("loc_1E57")

    label("loc_1E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1E57")

    ChrTalk(
        0xFE,
        (
            "克拉姆他\x01",
            "突然怎么了啊～\x02",
        )
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
        "嘿咻嘿咻……\x05\x02",
    )

    OP_4B(0x13, 0)
    Jump("loc_1F04")

    label("loc_1E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1EB8")
    OP_4A(0x13, 0)

    ChrTalk(
        0xFE,
        "大家正在玩呢～\x05\x02",
    )

    OP_4B(0x13, 0)
    Jump("loc_1F04")

    label("loc_1EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1F04")

    ChrTalk(
        0xFE,
        (
            "克拉姆他\x01",
            "在吃布丁的时候，\x01",
            "好像在考虑什么事情……\x02",
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
            "#753F哎呀，艾丝蒂尔你们这副装束，\x01",
            "难道说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯，\x01",
            "我们这就准备去蔡斯呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#753F真是这样啊……\x02\x03",
            "#750F各位实在是帮了我们大忙啊。\x01",
            "　\x02\x03",
            "而且没能给你们什么回报，\x01",
            "我真的是过意不去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F不要紧，您太客气了。\x02\x03",
            "能看到孩子们的笑脸，\x01",
            "我觉得我们的努力就有价值了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#750F艾丝蒂尔……\x02\x03",
            "……你们到了蔡斯之后\x01",
            "也要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F谢谢。\x01",
            "老师你们也请保重。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#751F嗯，\x01",
            "真的是多谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2186")

    label("loc_2127")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "#751F艾丝蒂尔、约修亚，\x01",
            "你们要保重啊……\x02\x03",
            "你们到了蔡斯之后\x01",
            "也要好好加油哦。\x02",
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
            "#501F#2P哈～～\x01",
            "终于来到有人住的地方了。\x02",
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
            "#000F#2P哇啊～真漂亮……\x01",
            "这里到处开满了白花……\x02\x03",
            "这村子叫什么名字呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F玛诺利亚村。\x01",
            "一个位于海道沿岸的小村落。\x02\x03",
            "这种白色的花，应该是木莲的一种吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#2P嗯～真的好漂亮啊～\x02\x03",
            "而且这种花香和海水味混在一起，\x01",
            "感觉有种清新自然的甘甜气息～\x02\x03",
            "#001F嗯……\x01",
            "不知不觉我都有点饿了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F哈哈，\x01",
            "闻到花香食欲就被刺激起来了，\x01",
            "还真像艾丝蒂尔的习性啊……\x02\x03",
            "#011F正所谓『好看不如好吃』呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F#2P因为正是长身体的时候嘛。\x02\x03",
            "已经到中午了吧。\x01",
            "我们找个地方休息一下，吃点东西吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F好啊……\x01",
            "我们身上好像还有些干粮吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2P啊，等一下。\x02\x03",
            "#000F难得来到这么别致的小村落，\x01",
            "不如尝尝当地的料理吧？\x02\x03",
            "我们可是第一次来到卢安地区呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，也是。\x01",
            "那我们到这里的旅馆看看吧。\x02",
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
            "#042F刚刚已经来这里找过了。\x02\x03",
            "#042F在杂货店里也没有见到他……\x02",
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
        (
            "#043F怎么办……\x01",
            "那小家伙到底去了哪里呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_8F(0x101, 0x6A90, 0x1F4, 0x4B8C, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        "#001F约修亚，快点啦快点啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F等一下，艾丝蒂尔。\x01",
            "当心后面的台阶……\x02",
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
        "#044F#4P#12A呀……\x05\x02",
    )


    ChrTalk(
        0x101,
        "#004F#1P#12A啊……\x05\x02",
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
        "#007F好疼啊……\x02",
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
            "#004F不、不好意思，你没事吧！？\x02\x03",
            "刚才我没看到门口有人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#040F啊，我没事，不要在意。\x02",
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
            "#045F其实该说对不起的是我才对。\x01",
            "都怪我在看其他地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，是这样吗。\x02\x03",
            "#001F哈哈，大家没事就好了⊙\x02",
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
            "#017F真是的……\x01",
            "艾丝蒂尔，你在说什么啊。\x02\x03",
            "#014F………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#040F？？？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F怎么了，约修亚？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F没、没什么……\x02",
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
            "#010F不好意思。\x01",
            "我的同伴给你添麻烦了。\x02\x03",
            "你没有受伤吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#045F啊，我没事。\x02\x03",
            "我正急着找人……\x01",
            "所以刚才没有留意周围。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，你找的是什么人呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#040F一个１０岁左右的男孩，\x01",
            "戴着一顶帽子的。\x02\x03",
            "你们有没有看到过他呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F戴帽子的男孩……\x02\x03",
            "#000F约修亚，你有没有印象呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F没有，我印象中并未见过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#043F这样啊……\x01",
            "到底跑到哪里去了呢……\x02\x03",
            "#045F那我先失陪了，\x01",
            "刚才给你们添麻烦了。\x02",
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
            "#002F约修亚？\x02\x03",
            "#002F喂，约修亚。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F#2P哦，啊啊……怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F怎么也没怎么……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#004F啊，难道……\x02\x03",
            "#001F原来是这样，我知道啦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F#2P……你又在乱想什么啦？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F别害羞、别害羞嘛⊙\x02\x03",
            "知道什么叫一见钟情吗？\x01",
            "恋爱之花就是在这个时候绽放的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F#2P你·别·误·会·了。\x02\x03",
            "我只是觉得她和\x01",
            "我以前认识的一个人有点相似而已。\x02\x03",
            "#010F#2P所以，刚才只是有点惊讶罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊……真的吗？哇～\x01",
            "和你小时候认识的人很像啊～\x02\x03",
            "#502F这种理由只能得３０分呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x102,
        (
            "#015F#2P我说，艾丝蒂尔。\x01",
            "你还记得刚才那女孩的校服吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F说起来……\x02\x03",
            "她的衣服好像和乔丝特变装时穿的\x01",
            "什么学院的校服一模一样呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P是杰尼丝王立学院。\x02\x03",
            "因为王立学院就在卢安地区，\x01",
            "所以我们见到这些学生也并不奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯～这次总该是货真价实的吧。\x02\x03",
            "#001F我觉得那女孩很有礼貌，\x01",
            "而且头脑也好像很聪明的呢～\x02\x03",
            "气质和那个傲慢的男人婆完全不同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P你还敢说那件事。\x02\x03",
            "是谁第一次见到乔丝特的时候\x01",
            "被骗得晕头转向的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#2P而且，当时又是谁\x01",
            "像刚才那样拿我开了一顿玩笑。\x02\x03",
            "不过，就算被骗，\x01",
            "也毕竟都是以前的事情啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F唔唔唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#2P与其花时间嘲笑别人，\x01",
            "还不如花点功夫观察身边的人和事，\x01",
            "锻炼一下自己的观察力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F明白了，我完全明白了啦！\x02\x03",
            "我以后再也不会随便嘲笑别人啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P你明白了就好。\x02\x03",
            "料理都快凉了，\x01",
            "我们去了望台那里吃午餐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F好～～吧。\x02",
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
        "#004F呜哇～～真是绝妙的景色！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，海边的风景一览无遗呢。\x02",
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
            "#501F在这里吃午餐……\x01",
            "简直就是一种奢侈的享受啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我也有同感。\x02\x03",
            "我们现在就开始吃吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯⊙\x02\x03",
            "#001F啊～肚子真的好饿呢。\x02",
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
            "#501F#3P我的便当是\x01",
            "熏火腿三明治。\x02\x03",
            "嗯～～还没吃就闻到一阵香味呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F而我的是……海鲜焗饭。\x01",
            "　\x02\x03",
            "漂着淡淡番红花的香味呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#3P那么，我不客气了～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F我也不客气了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#501F#3P先吃一口尝尝味道……\x02\x03",
            "#502F莫咕莫咕莫咕……咕咚。\x02\x03",
            "#004F哇～真的很好吃呢！\x01",
            "而且莴苣又香又脆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我的焗饭也很不错，\x01",
            "番红花的香气恰倒好处。\x02\x03",
            "白之木莲亭老板的厨艺的确一流。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#501F#3P约修亚，可以让我尝一口吗？\x02\x03",
            "我还没吃过海鲜焗饭，\x01",
            "很想尝尝是什么味道呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#010F好啊……\x01",
            "那我和你交换吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#3P嗯……\x01",
            "不过我两只手都拿着东西，不太方便……\x02\x03",
            "约修亚你喂我吃吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F我喂你……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#3P当然啦，啊～㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F这样……\x01",
            "我觉得有点不好意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#3P怕什么呀。\x01",
            "反正这里又没人看着我们。\x02\x03",
            "就像小孩子玩过家家那样，\x01",
            "有什么不好意思的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F……我说的不好意思\x01",
            "并不是你那种不好意思啊。\x02\x03",
            "算了，真拿你没办法……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚舀了一勺饭，\x01",
            "轻轻地喂进艾丝蒂尔的嘴里。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#502F#3P呷咕～呷咕～呷咕……咕咚。\x02\x03",
            "#501F嗯～太好吃啦㈱\x01",
            "这简直是海岸乡村料理的代表作。\x02\x03",
            "怎么说呢，\x01",
            "这里的花香总能刺激起我的食欲……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F知道啦知道啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#3P怎么听起来这么不情愿啊。\x02\x03",
            "#001F嘿～让你也尝尝我的！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔向约修亚的嘴里\x01",
            "硬塞了一大团吃剩的三明治。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x102,
        (
            "#014F啊。\x02\x03",
            "#015F嚼嚼嚼……嚼嚼嚼……\x02\x03",
            "#018F……好吃是好吃……\x01",
            "不过也不要突然塞这么多给我啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F#3P哼哼哼，我偏要⊙\x02",
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
        "#001F哈～实在是太好吃啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，就连附送的\x01",
            "那杯香草茶也十分甘甜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯，喝了之后很舒服呢，\x01",
            "感觉身体也开始暖和起来了……\x02\x03",
            "#007F海风吹过来也很舒服……\x01",
            "总觉得有点想睡觉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F吃饱了就睡\x01",
            "很容易胖得像小猪一样哦……\x02\x03",
            "不过吃完饭后偶尔午睡一下，\x01",
            "倒也不是什么坏事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯嗯……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F……啊，那是？\x02",
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
            "#004F看，刚才那只鸟！\x01",
            "就算是海鸥也太大了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P是啊。\x01",
            "翅膀的形状也不同，嘴也锋利很多。\x02\x03",
            "应该是鹰吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F白色的鹰……\x01",
            "还真是少见啊。\x02\x03",
            "#001F嘿嘿！\x01",
            "总觉得一会儿会遇到什么好事呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F#4P呵呵，如果是就好了。\x02\x03",
            "#010F对了艾丝蒂尔……\x01",
            "你已经没有睡意了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#008F啊……\x02\x03",
            "嗯……已经不困了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P那么，我们也该出发了。\x02\x03",
            "争取今天下午到达卢安，\x01",
            "然后办理支部的转属手续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F说的也是……\x02\x03",
            "嗯，好吧。\x01",
            "虽然有点舍不得，不过还是赶快出发吧。\x02",
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
        "#774F#4P#12A哇哇！\x05\x02",
    )


    ChrTalk(
        0x101,
        "#004F#1P#12A啊……\x05\x02",
    )

    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F呜……\x01",
            "怎么今天老是和别人撞个正着呢？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0xA, 0x4)
    OP_8E(0xA, 0x114E, 0xF96, 0x2D3C, 0xBB8, 0x0)

    ChrTalk(
        0xA,
        (
            "#771F不好意思啦。\x01",
            "我正在找人，没留意周围。\x02\x03",
            "#770F哎，\x01",
            "姐姐你们好像不是这里的人吧。\x02",
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
            "#000F说得没错。\x01",
            "我们是从别的地方来的。\x02\x03",
            "#004F啊，你难道是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#772F……怎、怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F刚才有个穿校服的女生\x01",
            "说她在找一个戴帽子的男孩子……\x01",
            "　\x02\x03",
            "是不是就是你啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#770F啊……对对。\x01",
            "我刚才也是一直在找她呢。\x02\x03",
            "你们是在哪儿见到她的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F在旅馆附近……\x02\x03",
            "不过这是刚才的事情，\x01",
            "她现在在哪我就不清楚了。\x02\x03",
            "我们也来帮你找那个女生吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#774F不、不用了。\x01",
            "我等一下自己去找就行了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_95(0xA, 0x0, 0x0, 0x0, 0x320, 0x1770)

    ChrTalk(
        0xA,
        "#771F我先走了，拜拜！\x02",
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
            "#501F好活泼的男孩子哦～\x02\x03",
            "感觉他和洛连特的鲁克\x01",
            "在某些方面有点相像呢……\x02\x03",
            "不知道鲁克那小子现在在干什么呢。\x02",
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
        "#004F#2P约修亚，怎么了？\x02",
    )

    CloseMessageWindow()
    OP_63(0x102)
    OP_44(0x102, 0x3)
    OP_8C(0x102, 0, 400)

    ChrTalk(
        0x102,
        (
            "#014F#1P啊……\x01",
            "也许是我多心了吧。\x02\x03",
            "艾丝蒂尔，你有没有丢掉什么东西？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2P丢掉？什么意思？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#1P看看身上有没有什么东西不见了。\x02\x03",
            "钱包或者饰物之类的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2P什么呀，又不是遇到了小偷。\x02\x03",
            "#006F钱包……在啊。\x02\x03",
            "头饰……也在啊。\x02\x03",
            "#501F游击士的徽章……\x02\x03",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#015F#1P果然是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2P啊啊啊啊～～～～？\x01",
            "怎么会这样呢！？\x02\x03",
            "难道是下山的时候\x01",
            "不小心弄丢的吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#1P冷静点，艾丝蒂尔。\x02\x03",
            "刚才吃午餐的时候，\x01",
            "徽章还好好地贴在你左边的胸前。\x02\x03",
            "就算是不见了，\x01",
            "也应该是在这附近弄丢的。\x02",
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
        (
            "#002F#2P可、可是……\x01",
            "会是在哪里弄丢的呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        "#004F#2P难、难道是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P嗯，很可能是刚才那个男孩子做的。\x02\x03",
            "我觉得他撞到你的时候很不自然，\x01",
            "所以才想到会不会是他……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#2P你、你说什么～！？\x02\x03",
            "为、为什么\x01",
            "他要偷我的游击士徽章啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#1P的确……\x01",
            "小孩子拿着那东西也没什么用处。\x02\x03",
            "所以恶作剧的可能性很高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#2P呜呜呜呜～……\x01",
            "这个可恶的调皮蛋，我绝对不放过他！\x02\x03",
            "#005F要是被我抓到的话，\x01",
            "一定要好好教训教训他！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P呵呵，对小孩子可要手下留情哦。\x02\x03",
            "总之，\x01",
            "我们先在这附近找找那孩子吧。\x02",
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
            "#002F话说回来，\x01",
            "这件事还真是不好办……\x02\x03",
            "我们要从哪里开始搜查好呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4P是啊……\x02\x03",
            "总之先回协会\x01",
            "向嘉恩先生报告一下吧。\x02\x03",
            "然后再定出搜查方针。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#049F…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x136, 400)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        (
            "#004F哎？你没事吧？\x01",
            "怎么发起呆来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#045F啊，对不起……\x02\x03",
            "我觉得自己脑子稍微有点乱……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F是吗……\x02\x03",
            "#501F对了，\x01",
            "约瑟夫是特蕾莎院长的丈夫吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#048F是的。\x02\x03",
            "不过他在几年前已经去世了……\x01",
            "　\x02\x03",
            "我小的时候，\x01",
            "他和老师一样也非常疼我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是这样吗……\x02\x03",
            "#004F咦？那就是说……\x01",
            "科洛丝也是在孤儿院长大的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#045F不是呢，并不是这个意思……\x02\x03",
            "其实在很久以前，\x01",
            "因为一些事情受到他们的照顾。\x02\x03",
            "当我进了王立学院，\x01",
            "也就是我来了卢安之后，\x01",
            "就和老师他们越来越亲近了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F原来是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F所以你就常来玩，\x01",
            "也顺便帮忙照顾那些孩子是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#048F是的……\x02\x03",
            "#047F……………………………\x02\x03",
            "#049F和老师还有孩子们比起来，\x01",
            "其实我所受到的打击\x01",
            "根本就不算什么。\x02\x03",
            "所以我也要打起精神来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3P科洛丝姐姐！\x02",
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
            "#044F玛丽。\x01",
            "怎么了，慌成这样子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "那个、那个！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "克拉姆那家伙\x01",
            "不知跑到哪儿去了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F不、不知跑到哪儿去了，\x01",
            "难道是跑出玛诺利亚村了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F能说得详细点吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "啊，好的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "那两个叔叔来了之后，\x01",
            "克拉姆就跑上了二楼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "然后一会儿就下来了，脸涨得通红，\x01",
            "嘴里说着『饶不了他们！』什么的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "气冲冲地跑了出去呢！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F饶不了他们……\x02\x03",
            "这、这难道是指……！\x02",
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
            "【放火烧孤儿院的犯人】\x01",        # 0
            "【戴尔蒙市长和他的秘书】\x01",      # 1
            "【仓库一带的那帮流氓】\x01",        # 2
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
            "#012F那是肯定的，不过……\x02\x03",
            "在这种情况下，\x01",
            "应该是指『渡鸦帮』的那帮家伙吧。\x02\x03",
            "那孩子大概是听见了\x01",
            "基尔巴特秘书所说的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x3B, 0x1)
    Jump("loc_583B")

    label("loc_575D")


    ChrTalk(
        0x102,
        (
            "#017F你怎么会这么想……\x02\x03",
            "#012F在这种情况下，\x01",
            "应该是指『渡鸦帮』的那帮家伙吧。\x02\x03",
            "那孩子大概是听见了\x01",
            "基尔巴特秘书所说的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_583B")

    label("loc_57D7")


    ChrTalk(
        0x102,
        (
            "#013F嗯……\x01",
            "应该就是指『渡鸦帮』的那帮流氓。\x02\x03",
            "那孩子大概是听见了\x01",
            "基尔巴特秘书所说的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x3B, 0x2)
    Jump("loc_583B")

    label("loc_583B")


    ChrTalk(
        0x101,
        (
            "#004F那、那不就糟了！\x02\x03",
            "那孩子该不会是想\x01",
            "闯到那帮流氓的地盘去吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x136, 0xFF)
    OP_8C(0x136, 270, 400)

    ChrTalk(
        0x136,
        (
            "#043F#2P怎、怎么会这样……！\x02\x03",
            "#042F不能让他这么做！\x01",
            "我要立刻去阻止他才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F我们也一起去。\x02\x03",
            "如果快一点的话， \x01",
            "或许能在他到达卢安之前追上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "科洛丝姐姐……\x02",
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
            "#042F不用担心。\x01",
            "我们一定会把克拉姆带回来的。\x02\x03",
            "玛丽你要照顾好\x01",
            "其他的孩子哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "是啊……\x01",
            "哥哥姐姐，拜托了！\x02",
        )
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
        (
            "#002F那我们赶快回卢安吧！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x136, 270, 400)

    ChrTalk(
        0x136,
        "#042F好的……！\x02",
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
        "#004F哇，都已经这么晚了。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x106, 0x1)
    OP_6F(0x4, 30)
    OP_70(0x4, 0x0)

    ChrTalk(
        0x106,
        (
            "#057F嘁……不好办了。\x02\x03",
            "这么暗，\x01",
            "能查出些什么来……\x02",
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
            "此时能听到基库的叫声。\x02",
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
        "#052F那是什么，刚才那声鸟鸣……\x02",
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
        (
            "#044F啊，基库……\x01",
            "你跑到哪儿去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#055F这、这家伙是什么啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4P是科洛丝的朋友，\x01",
            "白隼基库啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#055F哈啊……朋友……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#310F啾！\x02\x03",
            "啾，啾！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F是吗……我知道了。\x02\x03",
            "#042F谢谢呢，基库。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#311F啾☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F还真是优哉游哉啊。\x02\x03",
            "#051F那么，这位小姑娘。\x01",
            "你那位朋友说了些什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F基库应该能帮我们\x01",
            "找到那些袭击老师的犯人。\x02\x03",
            "老师他们受到袭击的时候，\x01",
            "似乎刚好被它看见了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F哈哈哈！\x01",
            "这玩笑真有趣……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#4P好样的！不愧是基库！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#3P嗯，立大功了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#311F啾～⊙\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x106,
        (
            "#055F喂，等等！\x02\x03",
            "你们该不会\x01",
            "连这鸟乱叫的话都信吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#3P因为我们已经\x01",
            "亲眼见识过好几次了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4P你不相信的话，\x01",
            "可以不跟我们一起走哦。\x02\x03",
            "科洛丝、基库，我们走吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#310F啾！\x02",
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
            "#055F………我～说…………………\x02\x03",
            "#054F喂、喂，你们这些小鬼，等等！\x02",
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
            "#830F好了……\x01",
            "那帮家伙由我看着。\x02\x03",
            "你们就赶去卢安，\x01",
            "向嘉恩报告昨天的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#4P我们倒是没关系，不过……\x01",
            "卡露娜姐姐您已经没事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#831F当然啦。只是被人抓住破绽，\x01",
            "熏了点催眠药而已嘛。\x02\x03",
            "#835F不过这次事出突然，\x01",
            "我已经不记得对方是什么样的人了……\x02\x03",
            "还真是丢脸啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这也不能怪您。\x02\x03",
            "我们也是四人联手\x01",
            "才勉强击退那些犯人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F那些孩子们平安无事，\x01",
            "也都多亏了卡露娜小姐啊。\x02\x03",
            "真是太感谢您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#835F哈哈……\x01",
            "是啊，总算是不幸中的大幸。\x02\x03",
            "#833F我听说阿加特\x01",
            "自己一个人去追那帮家伙了……\x02\x03",
            "虽然他的身手不容置疑，\x01",
            "但说到底还是有点担心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#4P嗯、嗯……\x01",
            "要是没捉到他们反而受伤的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F现在也唯有相信阿加特兄了。\x02\x03",
            "从昨天他所说的话判断，\x01",
            "他好像一直在追那些犯人。\x02\x03",
            "#010F对于他们的做事手法似乎也很了解，\x01",
            "我想应该不会那么轻易失手的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4P嗯……也对呢。\x02\x03",
            "所以，我们现在也应该\x01",
            "尽力做好自己能做的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#830F没错，就是这样。\x02\x03",
            "在事情了结之前，\x01",
            "这些属于特蕾莎院长的捐款\x01",
            "就先由我来暂代保管吧。\x02\x03",
            "这次我一定会保护好的，\x01",
            "所以你们就安心出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#041F好的，拜托你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#4P那么，我们走吧！\x02",
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
            "#000F我说，已经中午了。\x01",
            "我们找个地方休息一下吧？\x02\x03",
            "吃过午饭再出发怎么样？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F好啊。\x01",
            "先去找个吃饭的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AF2")

    label("loc_6AA7")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F等会儿再出发，\x01",
            "先去找个吃饭的地方吧。\x02",
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
            "#010F这边是通往街道的出口啊。\x02\x03",
            "了望台应该是在\x01",
            "村子里风车小屋的方向。\x02",
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
            "#012F首先调查一下\x01",
            "那个孩子去哪儿了。\x02\x03",
            "然后再开始追踪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CCA")

    label("loc_6C21")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F首先调查一下\x01",
            "那个孩子去哪儿了。\x02\x03",
            "先向村民询问一下会比较稳妥。\x01",
            "　\x02",
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
            "#050F已经没有时间回卢安去了……\x01",
            "　\x02\x03",
            "嘁，没办法了。\x01",
            "虽然觉得像被捉弄了一样，\x01",
            "不过现在也只有赌在那个基库上了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E31")

    label("loc_6D5C")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(
        0x106,
        (
            "#050F等等，你们要去哪儿呢。\x02\x03",
            "已经没有时间再回卢安去了。\x01",
            "　\x02",
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
            "#012F是啊。\x02\x03",
            "现在只能相信基库，\x01",
            "跟在它后面追踪了。\x02",
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
            "#050F已经没有绕远路的时间了啊。\x01",
            "　\x02\x03",
            "赶快回灯塔去\x01",
            "把这件事搞定吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F14")

    label("loc_6EB9")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(
        0x106,
        (
            "#050F喂，你们去哪儿。\x02\x03",
            "还是快点到灯塔吧。\x02",
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
            "#010F这边是通往街道的出口啊。\x02\x03",
            "了望台应该是在\x01",
            "村子里风车小屋的方向。\x02",
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
            "#012F首先调查一下\x01",
            "那个孩子去哪儿了。\x02\x03",
            "然后再开始追踪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70B2")

    label("loc_703E")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F首先调查一下\x01",
            "那个孩子去哪儿了。\x02\x03",
            "先向村民询问一下会比较稳妥。\x01",
            "　\x02",
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
            "#002F啊……\x01",
            "这边是古罗尼连峰的方向啊。\x02\x03",
            "要回卢安的话\x01",
            "必须走东面那条海道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7260")

    label("loc_7159")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71E1")

    ChrTalk(
        0x102,
        (
            "#012F这边是玛诺利亚间道啊。\x02\x03",
            "要回卢安的话，\x01",
            "必须走东面的那条梅威海道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7260")

    label("loc_71E1")


    ChrTalk(
        0x105,
        (
            "#042F这边是玛诺利亚间道呢。\x02\x03",
            "要去卢安的话，\x01",
            "必须走东面出口的梅威海道。\x02",
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
            "#012F这边是间道的出口。\x02\x03",
            "先去找特蕾莎老师吧，\x01",
            "她一定在玛诺利亚村里的。\x02",
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
