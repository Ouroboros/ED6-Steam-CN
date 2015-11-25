from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0034   ._SN',
        MapName             = 'map1',
        Location            = 'T0030.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '00130雪拉待机',                        # 9
        '00131雪拉移动',                        # 10
        '00132雪拉攻击',                        # 11
        '00133雪拉挨打',                        # 12
        '00134雪拉倒下',                        # 13
        '00135雪拉魔法咏唱',                    # 14
        '00136雪拉魔法发动',                    # 15
        '00137雪拉胜利',                        # 16
        '00160提妲待机',                        # 17
        '00161提妲移动',                        # 18
        '00162提妲攻击',                        # 19
        '00163提妲挨打',                        # 20
        '00164提妲倒下',                        # 21
        '00165提妲魔法咏唱',                    # 22
        '00166提妲魔法发动',                    # 23
        '00167提妲胜利',                        # 24
        '00140科洛丝待机',                      # 25
        '00141科洛丝移动',                      # 26
        '00142科洛丝攻击',                      # 27
        '00143科洛丝挨打',                      # 28
        '00144科洛丝倒下',                      # 29
        '00145科洛丝魔法咏唱',                  # 30
        '00146科洛丝魔法发动',                  # 31
        '00147科洛丝胜利',                      # 32
        '00110约修亚待机',                      # 33
        '00111约修亚移动',                      # 34
        '00112约修亚攻击',                      # 35
        '00113约修亚挨打',                      # 36
        '00114约修亚倒下',                      # 37
        '00115约修亚魔法咏唱',                  # 38
        '00116约修亚魔法发动',                  # 39
        '00117约修亚胜利',                      # 40
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
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
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00110 ._CH',             # 00
        'ED6_DT07/CH00111 ._CH',             # 01
        'ED6_DT07/CH00112 ._CH',             # 02
        'ED6_DT07/CH00113 ._CH',             # 03
        'ED6_DT07/CH00114 ._CH',             # 04
        'ED6_DT07/CH00115 ._CH',             # 05
        'ED6_DT07/CH00116 ._CH',             # 06
        'ED6_DT07/CH00117 ._CH',             # 07
        'ED6_DT07/CH00113 ._CH',             # 08
        'ED6_DT07/CH00113 ._CH',             # 09
        'ED6_DT07/CH00113 ._CH',             # 0A
        'ED6_DT07/CH00113 ._CH',             # 0B
        'ED6_DT07/CH00120 ._CH',             # 0C
        'ED6_DT07/CH00121 ._CH',             # 0D
        'ED6_DT07/CH00122 ._CH',             # 0E
        'ED6_DT07/CH00123 ._CH',             # 0F
        'ED6_DT07/CH00124 ._CH',             # 10
        'ED6_DT07/CH00125 ._CH',             # 11
        'ED6_DT07/CH00126 ._CH',             # 12
        'ED6_DT07/CH00127 ._CH',             # 13
        'ED6_DT07/CH00123 ._CH',             # 14
        'ED6_DT07/CH00123 ._CH',             # 15
        'ED6_DT07/CH00123 ._CH',             # 16
        'ED6_DT07/CH00123 ._CH',             # 17
        'ED6_DT07/CH00160 ._CH',             # 18
        'ED6_DT07/CH00161 ._CH',             # 19
        'ED6_DT07/CH00162 ._CH',             # 1A
        'ED6_DT07/CH00163 ._CH',             # 1B
        'ED6_DT07/CH00164 ._CH',             # 1C
        'ED6_DT07/CH00165 ._CH',             # 1D
        'ED6_DT07/CH00166 ._CH',             # 1E
        'ED6_DT07/CH00167 ._CH',             # 1F
        'ED6_DT07/CH00163 ._CH',             # 20
        'ED6_DT07/CH00163 ._CH',             # 21
        'ED6_DT07/CH00163 ._CH',             # 22
        'ED6_DT07/CH00163 ._CH',             # 23
        'ED6_DT07/CH00140 ._CH',             # 24
        'ED6_DT07/CH00141 ._CH',             # 25
        'ED6_DT07/CH00142 ._CH',             # 26
        'ED6_DT07/CH00143 ._CH',             # 27
        'ED6_DT07/CH00144 ._CH',             # 28
        'ED6_DT07/CH00145 ._CH',             # 29
        'ED6_DT07/CH00146 ._CH',             # 2A
        'ED6_DT07/CH00147 ._CH',             # 2B
        'ED6_DT07/CH00143 ._CH',             # 2C
        'ED6_DT07/CH00143 ._CH',             # 2D
        'ED6_DT07/CH00143 ._CH',             # 2E
        'ED6_DT07/CH00143 ._CH',             # 2F
    )

    AddCharChipPat(
        'ED6_DT07/CH00110P._CP',             # 00
        'ED6_DT07/CH00111P._CP',             # 01
        'ED6_DT07/CH00112P._CP',             # 02
        'ED6_DT07/CH00113P._CP',             # 03
        'ED6_DT07/CH00114P._CP',             # 04
        'ED6_DT07/CH00115P._CP',             # 05
        'ED6_DT07/CH00116P._CP',             # 06
        'ED6_DT07/CH00117P._CP',             # 07
        'ED6_DT07/CH00113P._CP',             # 08
        'ED6_DT07/CH00113P._CP',             # 09
        'ED6_DT07/CH00113P._CP',             # 0A
        'ED6_DT07/CH00113P._CP',             # 0B
        'ED6_DT07/CH00120P._CP',             # 0C
        'ED6_DT07/CH00121P._CP',             # 0D
        'ED6_DT07/CH00122P._CP',             # 0E
        'ED6_DT07/CH00123P._CP',             # 0F
        'ED6_DT07/CH00124P._CP',             # 10
        'ED6_DT07/CH00125P._CP',             # 11
        'ED6_DT07/CH00126P._CP',             # 12
        'ED6_DT07/CH00127P._CP',             # 13
        'ED6_DT07/CH00123P._CP',             # 14
        'ED6_DT07/CH00123P._CP',             # 15
        'ED6_DT07/CH00123P._CP',             # 16
        'ED6_DT07/CH00123P._CP',             # 17
        'ED6_DT07/CH00160P._CP',             # 18
        'ED6_DT07/CH00161P._CP',             # 19
        'ED6_DT07/CH00162P._CP',             # 1A
        'ED6_DT07/CH00163P._CP',             # 1B
        'ED6_DT07/CH00164P._CP',             # 1C
        'ED6_DT07/CH00165P._CP',             # 1D
        'ED6_DT07/CH00166P._CP',             # 1E
        'ED6_DT07/CH00167P._CP',             # 1F
        'ED6_DT07/CH00163P._CP',             # 20
        'ED6_DT07/CH00163P._CP',             # 21
        'ED6_DT07/CH00163P._CP',             # 22
        'ED6_DT07/CH00163P._CP',             # 23
        'ED6_DT07/CH00140P._CP',             # 24
        'ED6_DT07/CH00141P._CP',             # 25
        'ED6_DT07/CH00142P._CP',             # 26
        'ED6_DT07/CH00143P._CP',             # 27
        'ED6_DT07/CH00144P._CP',             # 28
        'ED6_DT07/CH00145P._CP',             # 29
        'ED6_DT07/CH00146P._CP',             # 2A
        'ED6_DT07/CH00147P._CP',             # 2B
        'ED6_DT07/CH00143P._CP',             # 2C
        'ED6_DT07/CH00143P._CP',             # 2D
        'ED6_DT07/CH00143P._CP',             # 2E
        'ED6_DT07/CH00143P._CP',             # 2F
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 12,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 13,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 14,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 15,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 16,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 17,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 18,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 19,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 20,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 21,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 22,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 27,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 28,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 29,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 30,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )


    ScpFunction(
        "Function_0_62A",          # 00, 0
        "Function_1_62B",          # 01, 1
        "Function_2_62C",          # 02, 2
        "Function_3_642",          # 03, 3
        "Function_4_658",          # 04, 4
        "Function_5_673",          # 05, 5
        "Function_6_68E",          # 06, 6
        "Function_7_6A9",          # 07, 7
        "Function_8_6C4",          # 08, 8
        "Function_9_6DA",          # 09, 9
        "Function_10_711",         # 0A, 10
        "Function_11_72C",         # 0B, 11
        "Function_12_747",         # 0C, 12
        "Function_13_75D",         # 0D, 13
        "Function_14_794",         # 0E, 14
        "Function_15_7AF",         # 0F, 15
        "Function_16_7CA",         # 10, 16
        "Function_17_7E0",         # 11, 17
        "Function_18_817",         # 12, 18
        "Function_19_832",         # 13, 19
        "Function_20_84D",         # 14, 20
        "Function_21_863",         # 15, 21
        "Function_22_89A",         # 16, 22
        "Function_23_8B5",         # 17, 23
        "Function_24_8D0",         # 18, 24
        "Function_25_8E6",         # 19, 25
        "Function_26_91D",         # 1A, 26
        "Function_27_938",         # 1B, 27
        "Function_28_953",         # 1C, 28
        "Function_29_969",         # 1D, 29
        "Function_30_9A0",         # 1E, 30
        "Function_31_9BB",         # 1F, 31
        "Function_32_9D6",         # 20, 32
    )


    def Function_0_62A(): pass

    label("Function_0_62A")

    Return()

    # Function_0_62A end

    def Function_1_62B(): pass

    label("Function_1_62B")

    Return()

    # Function_1_62B end

    def Function_2_62C(): pass

    label("Function_2_62C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_641")
    OP_99(0xFE, 0x0, 0x7, 0x708)
    Jump("Function_2_62C")

    label("loc_641")

    Return()

    # Function_2_62C end

    def Function_3_642(): pass

    label("Function_3_642")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_657")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("Function_3_642")

    label("loc_657")

    Return()

    # Function_3_642 end

    def Function_4_658(): pass

    label("Function_4_658")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_672")
    OP_99(0xFE, 0x0, 0x0, 0x5DC)
    Sleep(500)
    Jump("Function_4_658")

    label("loc_672")

    Return()

    # Function_4_658 end

    def Function_5_673(): pass

    label("Function_5_673")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68D")
    OP_99(0xFE, 0x0, 0x3, 0x7D0)
    Sleep(500)
    Jump("Function_5_673")

    label("loc_68D")

    Return()

    # Function_5_673 end

    def Function_6_68E(): pass

    label("Function_6_68E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A8")
    OP_99(0xFE, 0x0, 0x3, 0x7D0)
    Sleep(500)
    Jump("Function_6_68E")

    label("loc_6A8")

    Return()

    # Function_6_68E end

    def Function_7_6A9(): pass

    label("Function_7_6A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C3")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_7_6A9")

    label("loc_6C3")

    Return()

    # Function_7_6A9 end

    def Function_8_6C4(): pass

    label("Function_8_6C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D9")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_8_6C4")

    label("loc_6D9")

    Return()

    # Function_8_6C4 end

    def Function_9_6DA(): pass

    label("Function_9_6DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_710")
    SetChrChipByIndex(0xFE, 5)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 6)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_9_6DA")

    label("loc_710")

    Return()

    # Function_9_6DA end

    def Function_10_711(): pass

    label("Function_10_711")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72B")
    OP_99(0xFE, 0x0, 0xE, 0x7D0)
    Sleep(500)
    Jump("Function_10_711")

    label("loc_72B")

    Return()

    # Function_10_711 end

    def Function_11_72C(): pass

    label("Function_11_72C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_746")
    OP_99(0xFE, 0x0, 0x9, 0x7D0)
    Sleep(500)
    Jump("Function_11_72C")

    label("loc_746")

    Return()

    # Function_11_72C end

    def Function_12_747(): pass

    label("Function_12_747")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75C")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_12_747")

    label("loc_75C")

    Return()

    # Function_12_747 end

    def Function_13_75D(): pass

    label("Function_13_75D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_793")
    SetChrChipByIndex(0xFE, 17)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 18)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_13_75D")

    label("loc_793")

    Return()

    # Function_13_75D end

    def Function_14_794(): pass

    label("Function_14_794")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AE")
    OP_99(0xFE, 0x0, 0xD, 0x7D0)
    Sleep(500)
    Jump("Function_14_794")

    label("loc_7AE")

    Return()

    # Function_14_794 end

    def Function_15_7AF(): pass

    label("Function_15_7AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C9")
    OP_99(0xFE, 0x0, 0xD, 0x7D0)
    Sleep(500)
    Jump("Function_15_7AF")

    label("loc_7C9")

    Return()

    # Function_15_7AF end

    def Function_16_7CA(): pass

    label("Function_16_7CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DF")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_16_7CA")

    label("loc_7DF")

    Return()

    # Function_16_7CA end

    def Function_17_7E0(): pass

    label("Function_17_7E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_816")
    SetChrChipByIndex(0xFE, 29)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 30)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_17_7E0")

    label("loc_816")

    Return()

    # Function_17_7E0 end

    def Function_18_817(): pass

    label("Function_18_817")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_831")
    OP_99(0xFE, 0x0, 0xE, 0x3E8)
    Sleep(1000)
    Jump("Function_18_817")

    label("loc_831")

    Return()

    # Function_18_817 end

    def Function_19_832(): pass

    label("Function_19_832")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_84C")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_19_832")

    label("loc_84C")

    Return()

    # Function_19_832 end

    def Function_20_84D(): pass

    label("Function_20_84D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_862")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_20_84D")

    label("loc_862")

    Return()

    # Function_20_84D end

    def Function_21_863(): pass

    label("Function_21_863")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_899")
    SetChrChipByIndex(0xFE, 41)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 42)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_21_863")

    label("loc_899")

    Return()

    # Function_21_863 end

    def Function_22_89A(): pass

    label("Function_22_89A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8B4")
    OP_99(0xFE, 0x0, 0x14, 0x7D0)
    Sleep(500)
    Jump("Function_22_89A")

    label("loc_8B4")

    Return()

    # Function_22_89A end

    def Function_23_8B5(): pass

    label("Function_23_8B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8CF")
    OP_99(0xFE, 0x0, 0xC, 0x7D0)
    Sleep(500)
    Jump("Function_23_8B5")

    label("loc_8CF")

    Return()

    # Function_23_8B5 end

    def Function_24_8D0(): pass

    label("Function_24_8D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E5")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_24_8D0")

    label("loc_8E5")

    Return()

    # Function_24_8D0 end

    def Function_25_8E6(): pass

    label("Function_25_8E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_91C")
    SetChrChipByIndex(0xFE, 53)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 54)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_25_8E6")

    label("loc_91C")

    Return()

    # Function_25_8E6 end

    def Function_26_91D(): pass

    label("Function_26_91D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_937")
    OP_99(0xFE, 0x0, 0x13, 0x7D0)
    Sleep(500)
    Jump("Function_26_91D")

    label("loc_937")

    Return()

    # Function_26_91D end

    def Function_27_938(): pass

    label("Function_27_938")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_952")
    OP_99(0xFE, 0x0, 0xC, 0x7D0)
    Sleep(500)
    Jump("Function_27_938")

    label("loc_952")

    Return()

    # Function_27_938 end

    def Function_28_953(): pass

    label("Function_28_953")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_968")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_28_953")

    label("loc_968")

    Return()

    # Function_28_953 end

    def Function_29_969(): pass

    label("Function_29_969")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99F")
    SetChrChipByIndex(0xFE, 5)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 6)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_29_969")

    label("loc_99F")

    Return()

    # Function_29_969 end

    def Function_30_9A0(): pass

    label("Function_30_9A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9BA")
    OP_99(0xFE, 0x0, 0x21, 0x7D0)
    Sleep(500)
    Jump("Function_30_9A0")

    label("loc_9BA")

    Return()

    # Function_30_9A0 end

    def Function_31_9BB(): pass

    label("Function_31_9BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D5")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_31_9BB")

    label("loc_9D5")

    Return()

    # Function_31_9BB end

    def Function_32_9D6(): pass

    label("Function_32_9D6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "你好。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_9D6 end

    SaveToFile()

Try(main)
