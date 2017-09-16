from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0031   ._SN',
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
        'CH00000艾丝蒂尔',                      # 9
        'CH00010约修亚',                        # 10
        'CH00020雪拉',                          # 11
        'CH00030奥利维尔',                      # 12
        'CH00040科洛丝',                        # 13
        '表情',                                 # 14
        'CH00050阿加特',                        # 15
        'CH00060提妲',                          # 16
        'CH00070金',                            # 17
        'CH02000卡西乌斯老爹',                  # 18
        'CH02010艾莉茜雅女王',                  # 19
        'CH02020Ｄｒ．拉赛尔',                  # 20
        'CH02030理查德上校',                    # 21
        'CH02040莱维',                          # 22
        'CH02050亚鲁瓦教授(怀斯曼)',            # 23
        'CH02060记者奈尔',                      # 24
        'CH02070摄影师·朵洛希',                # 25
        'CH02080摩尔根将军',                    # 26
        'CH02090亲卫队尤莉亚',                  # 27
        'CH02100原特务兵凯诺娜队长',            # 28
        'CH02110空贼团大哥多伦',                # 29
        'CH02120空贼团二哥吉尔',                # 30
        'CH02130空贼团小妹乔丝特',              # 31
        'CH02140杜南公爵',                      # 32
        'CH02190穆拉',                          # 33
        'CH02200洛伦斯',                        # 34
        'CH02210艾丝蒂尔１１岁',                # 35
        'CH02220约修亚１１岁',                  # 36
        'CH02230女佣艾丝蒂尔',                  # 37
        'CH02240女佣约修亚',                    # 38
        'CH02260骑士艾丝蒂尔',                  # 39
        'CH02270骑士科洛丝',                    # 40
        'CH02280公主约修亚',                    # 41
        'CH02290温泉约修亚',                    # 42
        'CH02300温泉艾丝蒂尔',                  # 43
        'CH02310温泉提妲',                      # 44
        'CH02320基库',                          # 45
        'CH02330学生乔丝特',                    # 46
        'CH02340公主科洛丝',                    # 47
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
        'ED6_DT07/CH00000 ._CH',             # 00
        'ED6_DT07/CH00010 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00050 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT07/CH00070 ._CH',             # 07
        'ED6_DT07/CH02000 ._CH',             # 08
        'ED6_DT07/CH02010 ._CH',             # 09
        'ED6_DT07/CH02020 ._CH',             # 0A
        'ED6_DT07/CH02030 ._CH',             # 0B
        'ED6_DT07/CH02040 ._CH',             # 0C
        'ED6_DT07/CH02050 ._CH',             # 0D
        'ED6_DT07/CH02060 ._CH',             # 0E
        'ED6_DT07/CH02070 ._CH',             # 0F
        'ED6_DT07/CH02080 ._CH',             # 10
        'ED6_DT07/CH02090 ._CH',             # 11
        'ED6_DT07/CH02100 ._CH',             # 12
        'ED6_DT07/CH02110 ._CH',             # 13
        'ED6_DT07/CH02120 ._CH',             # 14
        'ED6_DT07/CH02130 ._CH',             # 15
        'ED6_DT07/CH02140 ._CH',             # 16
        'ED6_DT07/CH02190 ._CH',             # 17
        'ED6_DT07/CH02200 ._CH',             # 18
        'ED6_DT07/CH02210 ._CH',             # 19
        'ED6_DT07/CH02220 ._CH',             # 1A
        'ED6_DT07/CH02230 ._CH',             # 1B
        'ED6_DT07/CH02240 ._CH',             # 1C
        'ED6_DT07/CH02250 ._CH',             # 1D
        'ED6_DT07/CH02260 ._CH',             # 1E
        'ED6_DT07/CH02270 ._CH',             # 1F
        'ED6_DT07/CH02280 ._CH',             # 20
        'ED6_DT07/CH02290 ._CH',             # 21
        'ED6_DT07/CH02300 ._CH',             # 22
        'ED6_DT07/CH02310 ._CH',             # 23
        'ED6_DT07/CH02320 ._CH',             # 24
        'ED6_DT07/CH02330 ._CH',             # 25
        'ED6_DT07/CH02340 ._CH',             # 26
    )

    AddCharChipPat(
        'ED6_DT07/CH00000P._CP',             # 00
        'ED6_DT07/CH00010P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00050P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT07/CH00070P._CP',             # 07
        'ED6_DT07/CH02000P._CP',             # 08
        'ED6_DT07/CH02010P._CP',             # 09
        'ED6_DT07/CH02020P._CP',             # 0A
        'ED6_DT07/CH02030P._CP',             # 0B
        'ED6_DT07/CH02040P._CP',             # 0C
        'ED6_DT07/CH02050P._CP',             # 0D
        'ED6_DT07/CH02060P._CP',             # 0E
        'ED6_DT07/CH02070P._CP',             # 0F
        'ED6_DT07/CH02080P._CP',             # 10
        'ED6_DT07/CH02090P._CP',             # 11
        'ED6_DT07/CH02100P._CP',             # 12
        'ED6_DT07/CH02110P._CP',             # 13
        'ED6_DT07/CH02120P._CP',             # 14
        'ED6_DT07/CH02130P._CP',             # 15
        'ED6_DT07/CH02140P._CP',             # 16
        'ED6_DT07/CH02190P._CP',             # 17
        'ED6_DT07/CH02200P._CP',             # 18
        'ED6_DT07/CH02210P._CP',             # 19
        'ED6_DT07/CH02220P._CP',             # 1A
        'ED6_DT07/CH02230P._CP',             # 1B
        'ED6_DT07/CH02240P._CP',             # 1C
        'ED6_DT07/CH02250P._CP',             # 1D
        'ED6_DT07/CH02260P._CP',             # 1E
        'ED6_DT07/CH02270P._CP',             # 1F
        'ED6_DT07/CH02280P._CP',             # 20
        'ED6_DT07/CH02290P._CP',             # 21
        'ED6_DT07/CH02300P._CP',             # 22
        'ED6_DT07/CH02310P._CP',             # 23
        'ED6_DT07/CH02320P._CP',             # 24
        'ED6_DT07/CH02330P._CP',             # 25
        'ED6_DT07/CH02340P._CP',             # 26
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 15000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 32000,
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
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 47,
    )


    ScpFunction(
        "Function_0_6C2",          # 00, 0
        "Function_1_6C3",          # 01, 1
        "Function_2_6C4",          # 02, 2
        "Function_3_6DA",          # 03, 3
        "Function_4_6F0",          # 04, 4
        "Function_5_706",          # 05, 5
        "Function_6_72A",          # 06, 6
        "Function_7_74E",          # 07, 7
        "Function_8_763",          # 08, 8
        "Function_9_784",          # 09, 9
        "Function_10_7EB",         # 0A, 10
        "Function_11_942",         # 0B, 11
        "Function_12_B0B",         # 0C, 12
        "Function_13_BC6",         # 0D, 13
        "Function_14_C73",         # 0E, 14
        "Function_15_D2D",         # 0F, 15
        "Function_16_DFF",         # 10, 16
        "Function_17_EC2",         # 11, 17
        "Function_18_F14",         # 12, 18
        "Function_19_F84",         # 13, 19
        "Function_20_FD6",         # 14, 20
        "Function_21_1038",        # 15, 21
        "Function_22_1099",        # 16, 22
        "Function_23_11CF",        # 17, 23
        "Function_24_124F",        # 18, 24
        "Function_25_12E8",        # 19, 25
        "Function_26_133E",        # 1A, 26
        "Function_27_1381",        # 1B, 27
        "Function_28_13F1",        # 1C, 28
        "Function_29_1431",        # 1D, 29
        "Function_30_14C2",        # 1E, 30
        "Function_31_14E7",        # 1F, 31
        "Function_32_15A9",        # 20, 32
        "Function_33_15FB",        # 21, 33
        "Function_34_1683",        # 22, 34
        "Function_35_1715",        # 23, 35
        "Function_36_173A",        # 24, 36
        "Function_37_176E",        # 25, 37
        "Function_38_1792",        # 26, 38
        "Function_39_1820",        # 27, 39
        "Function_40_1873",        # 28, 40
        "Function_41_1997",        # 29, 41
        "Function_42_1A86",        # 2A, 42
        "Function_43_1B1F",        # 2B, 43
        "Function_44_1C05",        # 2C, 44
        "Function_45_1CC1",        # 2D, 45
        "Function_46_1D33",        # 2E, 46
        "Function_47_1D8C",        # 2F, 47
        "Function_48_1E26",        # 30, 48
    )


    def Function_0_6C2(): pass

    label("Function_0_6C2")

    Return()

    # Function_0_6C2 end

    def Function_1_6C3(): pass

    label("Function_1_6C3")

    Return()

    # Function_1_6C3 end

    def Function_2_6C4(): pass

    label("Function_2_6C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6C4")

    label("loc_6D9")

    Return()

    # Function_2_6C4 end

    def Function_3_6DA(): pass

    label("Function_3_6DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EF")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("Function_3_6DA")

    label("loc_6EF")

    Return()

    # Function_3_6DA end

    def Function_4_6F0(): pass

    label("Function_4_6F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_705")
    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("Function_4_6F0")

    label("loc_705")

    Return()

    # Function_4_6F0 end

    def Function_5_706(): pass

    label("Function_5_706")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_729")
    OP_8D(0xFE, 4000, 20000, 24000, 30000, 1500)
    Jump("Function_5_706")

    label("loc_729")

    Return()

    # Function_5_706 end

    def Function_6_72A(): pass

    label("Function_6_72A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74D")
    OP_8D(0xFE, 22000, 20000, 42000, 30000, 1500)
    Jump("Function_6_72A")

    label("loc_74D")

    Return()

    # Function_6_72A end

    def Function_7_74E(): pass

    label("Function_7_74E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "你好。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_74E end

    def Function_8_763(): pass

    label("Function_8_763")

    TalkBegin(0xFE)
    OP_1D(0x4)

    ChrTalk(
        0xFE,
        "更换ＢＧＭ喵。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_763 end

    def Function_9_784(): pass

    label("Function_9_784")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "减小ＢＧＭ音量喵。\x02",
    )

    OP_1F(0x5A, 0x7D0)
    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "再减小ＢＧＭ音量喵。\x02",
    )

    OP_1F(0x46, 0x7D0)
    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "恢复ＢＧＭ喵。\x02",
    )

    OP_1F(0x64, 0x7D0)
    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_784 end

    def Function_10_7EB(): pass

    label("Function_10_7EB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#000F通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#001F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#002F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#003F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#004F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#005F发怒１\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#006F通常２（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#007F叹气\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#008F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#009F发怒２（哼）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#500F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#501F轻松\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#502F嘿嘿\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#503F害羞２\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#504F喊叫\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#505F唔～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#506F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#507F挑衅\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#508F笑颜２\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#509F眯眼\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_7EB end

    def Function_11_942(): pass

    label("Function_11_942")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#010F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#011F笑颜１（企图）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#012F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#013F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#014F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#015F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#016F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#017F叹气\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#018F害羞（抗议）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#019F笑颜２（发怒）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#510F杀意\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#511F真的害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#512F笑颜３\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#513F痛苦\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#514F暗示解除\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#515F暗示解除后呐喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#516F暗示解除后发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#517FED笑颜４\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#518FED通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#519FED低头\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#590FED低头惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#591F暗示解除后呐喊２\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#592FED笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#593FED瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_942 end

    def Function_12_B0B(): pass

    label("Function_12_B0B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#020F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#021F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#022F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#023F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#024F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#025F叹气\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#026F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#027F诱惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#028F醉酒（高兴）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#029F醉酒（不高兴）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_B0B end

    def Function_13_BC6(): pass

    label("Function_13_BC6")

    TalkBegin(0xFE)
    OP_62(0xB, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    ChrTalk(
        0xFE,
        "#030F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#031F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#032F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#033F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#034F叹气\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#035F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#036F慌张\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#037F醉酒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#038F醉酒晕倒\x02",
    )

    CloseMessageWindow()
    OP_63(0xB)
    TalkEnd(0xFE)
    Return()

    # Function_13_BC6 end

    def Function_14_C73(): pass

    label("Function_14_C73")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#040F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#041F笑颜１\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#042F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#043F悲哀１\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#044F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#045F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#046F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#047F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#048F笑颜２（公主ver）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#049F悲哀２（深刻）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_C73 end

    def Function_15_D2D(): pass

    label("Function_15_D2D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#050F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#051F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#052F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#053F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#054F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#055F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#056F疼\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#057F杀意\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#058F毒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#059F痛苦\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#550F可恶～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#551F笑颜２\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#552F悲哀\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_D2D end

    def Function_16_DFF(): pass

    label("Function_16_DFF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#060F通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#061F笑颜１\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#062F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#063F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#064F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#065F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#066F笑颜２\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#067F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#068F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#069F哭泣\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#560F通常２\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#561F叹气\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_DFF end

    def Function_17_EC2(): pass

    label("Function_17_EC2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#070F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#071F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#072F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#073F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#074F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_EC2 end

    def Function_18_F14(): pass

    label("Function_18_F14")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#080F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#081F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#082F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#083F叹气\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#084F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#085F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#086F发怒\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_F14 end

    def Function_19_F84(): pass

    label("Function_19_F84")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#090F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#091F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#092F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#093F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#094F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_F84 end

    def Function_20_FD6(): pass

    label("Function_20_FD6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#100F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#101F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#102F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#103F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#104F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#105F笑颜２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_FD6 end

    def Function_21_1038(): pass

    label("Function_21_1038")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#110F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#111F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#112F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#113F吃惊\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#114F喊叫\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#115F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_1038 end

    def Function_22_1099(): pass

    label("Function_22_1099")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#120F通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#121F通常２\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#122F侧脸\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#123F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#124F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#280F洛伦斯版本通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#281F洛伦斯版本闭嘴\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#282F洛伦斯版本\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#283F洛伦斯（摘掉头盔）通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#284F洛伦斯（摘掉头盔）通常２\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#285F洛伦斯（摘掉头盔）笑颜\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_1099 end

    def Function_23_11CF(): pass

    label("Function_23_11CF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#130F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#131F慌张\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#132F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#133FED用通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#134FED用笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#135FED用严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#136FED用瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_11CF end

    def Function_24_124F(): pass

    label("Function_24_124F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#140F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#141F笑颜１（呲牙）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#142F怀疑\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#143F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#144F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#145F叹气\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#146F醉酒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#147F笑颜２（满面）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_124F end

    def Function_25_12E8(): pass

    label("Function_25_12E8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#150F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#151F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#152F落泪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#153F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#154F困惑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_12E8 end

    def Function_26_133E(): pass

    label("Function_26_133E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#160F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#161F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#162F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#163F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_133E end

    def Function_27_1381(): pass

    label("Function_27_1381")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#170F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#171F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#172F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#173F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#174F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#175F忧郁\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#176F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_1381 end

    def Function_28_13F1(): pass

    label("Function_28_13F1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#180F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#181F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#182F通常２（优雅）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_13F1 end

    def Function_29_1431(): pass

    label("Function_29_1431")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#190F通常（正常）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#191F笑颜（正常）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#192F惊愕（正常）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#193F通常（发狂）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#194F笑颜（发狂）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#195F发怒（发狂）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_1431 end

    def Function_30_14C2(): pass

    label("Function_30_14C2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#200F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#201F严肃\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_14C2 end

    def Function_31_14E7(): pass

    label("Function_31_14E7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#210F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#211F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#212F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#213F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#214F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#215F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#216F慌张\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#217F化装通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#218F化装笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#219F化装空贼表情\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#410F化装大笑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_14E7 end

    def Function_32_15A9(): pass

    label("Function_32_15A9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#290F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#291F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#292F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#293F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#294F发怒\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_15A9 end

    def Function_33_15FB(): pass

    label("Function_33_15FB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#300F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#301F无表情\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#302F喊叫\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#303F疼\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#304F冷漠\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#305F睡觉\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#306F醒来\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_15FB end

    def Function_34_1683(): pass

    label("Function_34_1683")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#220F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#221F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#222F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#223F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#224F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#225F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#226F慌张\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#227F醉酒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#228F晕倒\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_1683 end

    def Function_35_1715(): pass

    label("Function_35_1715")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#310F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#311F笑颜\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_1715 end

    def Function_36_173A(): pass

    label("Function_36_173A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#270F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#271F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#272F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_173A end

    def Function_37_176E(): pass

    label("Function_37_176E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#280F洛伦斯版本\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_176E end

    def Function_38_1792(): pass

    label("Function_38_1792")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#320F通常１（轻松）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#321F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#322F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#323F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#324F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#325F通常２（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#326F发怒２（哼）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_1792 end

    def Function_39_1820(): pass

    label("Function_39_1820")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#330F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#331F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#332F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#333F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#334F叹气\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_1820 end

    def Function_40_1873(): pass

    label("Function_40_1873")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#340F通常（轻松）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#341F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#342F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#343F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#344F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#345F发怒１（喊叫）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#346F通常（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#347F叹气\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#348F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#349F发怒２（哼）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#840F剧用通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#841F剧用严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#842F剧用惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#843F剧用喊叫\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#844F剧用瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_1873 end

    def Function_41_1997(): pass

    label("Function_41_1997")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#350F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#351F笑颜１\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#352F严肃·剧用通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#353F悲哀１\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#354F惊愕·剧用\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#355F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#356F发怒·剧用\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#357F瞑目·剧用\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#358F笑颜２（公主ver）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#359F悲哀２（深刻）·剧用\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#850F剧用痛苦\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_1997 end

    def Function_42_1A86(): pass

    label("Function_42_1A86")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#360F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#361F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#362F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#363F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#364F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#365F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#366F喊叫\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#367F叹气\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#368F害羞（抗议）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_1A86 end

    def Function_43_1B1F(): pass

    label("Function_43_1B1F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#370F通常１（轻松）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#371F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#372F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#373F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#374F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#375F发怒１（喊叫）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#376F通常２（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#377F叹气\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#378F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#379F发怒２（哼）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#440F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#441F脸红\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_1B1F end

    def Function_44_1C05(): pass

    label("Function_44_1C05")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#380F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#381F笑颜１（企图）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#382F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#383F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#384F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#385F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#386F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#387F叹气\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#388F害羞（抗议）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#389F笑颜２（发怒）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_44_1C05 end

    def Function_45_1CC1(): pass

    label("Function_45_1CC1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#390F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#391F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#392F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#393F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#394F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#395F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#396F通常２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_1CC1 end

    def Function_46_1D33(): pass

    label("Function_46_1D33")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#217F化装通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#218F化装笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#219F化装空贼表情\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#410F化装大笑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_46_1D33 end

    def Function_47_1D8C(): pass

    label("Function_47_1D8C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#400F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#401F笑颜（公主ver）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#402F严肃\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#403F悲哀１\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#404F悲哀２（深刻）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#405F嘿嘿\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#406F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#407F发怒\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_47_1D8C end

    def Function_48_1E26(): pass

    label("Function_48_1E26")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_251A")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "表情测试\x01",              # 0
            "假名注音表示测试\x01",      # 1
            "音量测试\x01",              # 2
            "取消\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1EAE"),
        (1, "loc_21B9"),
        (2, "loc_24A7"),
        (SWITCH_DEFAULT, "loc_250A"),
    )


    label("loc_1EAE")

    OP_62(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F怒\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F郁闷\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F冷汗\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F黑线\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F…………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020FＺｚｚ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F灯泡\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F哇～哇～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F发现\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F慌慌张张\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F大怒！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    OP_22(0x30, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F晕菜\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F闪闪发光\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x0, 1900, 0x33, 0x35, 0xC8, 0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F天旋地转\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x3B, 0x3C, 0xFA, 0x2)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F对话\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x3D, 0x3E, 0xFA, 0x2)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#020F调查点\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2517")

    label("loc_21B9")


    ChrTalk(
        0xFE,
        "#040F假名注音测试。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#040F導力器#6Rオーブメント#。遊撃士#6R ブレイサー#。\x01",
            "拓#2Rひら#かれし時代の物語。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#040F導力機関#8Rオーバルエンジン#、導力砲#8R　 オーバルカノン#（←文中限定）。\x01",
            "遊撃士協会#10R　ブレイサーギルド#、七耀石#6R セプチウム#、身喰らう蛇#10R ウ　ロ　ボ　ロ　ス　#。\x01",
            "七の至宝#8Rセプト＝テリオン#、“七至宝”#10R　セプト＝テリオン　#、七 至 宝#8Rセプト＝テリオン#（←保留中）。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#040F『銀閃#4Rぎんせん#のシェラザード』、女神#4Rエイドス#。\x01",
            "養父#4R と　う #さん、王都#6R　 グランセル#（←文中限定）。\x01",
            "導力魔法#8R オーバルアーツ #、結晶回路#8R ク　オ　ー　ツ #、翠耀石#6R エスメラス#。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#040F如果在一句话开始使用就会造成下面的悲剧。\x01",
            "王都#6R　 グランセル#（←文中限定）。\x01",
            "導力砲#8R　 オーバルカノン#（←文中限定）。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2517")

    label("loc_24A7")


    ChrTalk(
        0xFE,
        "减小ＢＧＭ音量喵。\x02",
    )

    OP_1F(0x5A, 0x7D0)
    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "再减小ＢＧＭ音量喵。\x02",
    )

    OP_1F(0x46, 0x7D0)
    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "恢复ＢＧＭ喵。\x02",
    )

    OP_1F(0x64, 0x7D0)
    CloseMessageWindow()
    Jump("loc_2517")

    label("loc_250A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2517")

    label("loc_2517")

    Jump("loc_1E33")

    label("loc_251A")

    TalkEnd(0xFE)
    Return()

    # Function_48_1E26 end

    SaveToFile()

Try(main)
