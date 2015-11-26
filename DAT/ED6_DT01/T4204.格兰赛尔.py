from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4204   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4204.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '特务兵',                               # 9
        '特务兵',                               # 10
        '希尔丹夫人',                           # 11
        '凯诺娜上尉',                           # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '特务兵',                               # 15
        '特务兵',                               # 16
        '特务兵',                               # 17
        '特务兵',                               # 18
        '特务兵',                               # 19
        '科洛丝',                               # 20
        '奥利维尔',                             # 21
        '阿加特',                               # 22
        '雪拉',                                 # 23
        '金',                                   # 24
        '提妲',                                 # 25
        '拉赛尔博士',                           # 26
        '卡西乌斯',                             # 27
        '奈尔',                                 # 28
        '朵洛希',                               # 29
        '希德少校',                             # 30
        '摩尔根将军',                           # 31
        '尤莉亚中尉',                           # 32
        '艾莉茜雅女王',                         # 33
        '米蕾奴夫人',                           # 34
        '克劳斯市长',                           # 35
        '莉拉',                                 # 36
        '梅贝尔市长',                           # 37
        '科林兹校长',                           # 38
        '玛多克工房长',                         # 39
        '亲卫队员',                             # 40
        '亲卫队员',                             # 41
        '亲卫队员',                             # 42
        '亲卫队员',                             # 43
        '亲卫队员',                             # 44
        '亲卫队员',                             # 45
        '约修亚',                               # 46
        '特务艇',                               # 47
        '特务艇影子',                           # 48
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
        'ED6_DT07/CH01610 ._CH',             # 00
        'ED6_DT07/CH02460 ._CH',             # 01
        'ED6_DT07/CH02230 ._CH',             # 02
        'ED6_DT07/CH02240 ._CH',             # 03
        'ED6_DT07/CH02100 ._CH',             # 04
        'ED6_DT07/CH00100 ._CH',             # 05
        'ED6_DT07/CH00101 ._CH',             # 06
        'ED6_DT07/CH00120 ._CH',             # 07
        'ED6_DT07/CH00121 ._CH',             # 08
        'ED6_DT07/CH00140 ._CH',             # 09
        'ED6_DT07/CH00141 ._CH',             # 0A
        'ED6_DT07/CH02340 ._CH',             # 0B
        'ED6_DT07/CH00030 ._CH',             # 0C
        'ED6_DT07/CH00050 ._CH',             # 0D
        'ED6_DT07/CH00020 ._CH',             # 0E
        'ED6_DT07/CH00070 ._CH',             # 0F
        'ED6_DT07/CH00060 ._CH',             # 10
        'ED6_DT07/CH02020 ._CH',             # 11
        'ED6_DT07/CH02000 ._CH',             # 12
        'ED6_DT07/CH02060 ._CH',             # 13
        'ED6_DT07/CH02070 ._CH',             # 14
        'ED6_DT07/CH02450 ._CH',             # 15
        'ED6_DT07/CH02080 ._CH',             # 16
        'ED6_DT07/CH02090 ._CH',             # 17
        'ED6_DT07/CH02010 ._CH',             # 18
        'ED6_DT07/CH01180 ._CH',             # 19
        'ED6_DT07/CH02350 ._CH',             # 1A
        'ED6_DT07/CH02370 ._CH',             # 1B
        'ED6_DT07/CH02360 ._CH',             # 1C
        'ED6_DT07/CH02600 ._CH',             # 1D
        'ED6_DT07/CH02620 ._CH',             # 1E
        'ED6_DT07/CH01320 ._CH',             # 1F
        'ED6_DT06/CH20030 ._CH',             # 20
        'ED6_DT07/CH00010 ._CH',             # 21
        'ED6_DT07/CH00341 ._CH',             # 22
        'ED6_DT06/CH20042 ._CH',             # 23
        'ED6_DT06/CH20040 ._CH',             # 24
        'ED6_DT06/CH20060 ._CH',             # 25
        'ED6_DT07/CH00004 ._CH',             # 26
        'ED6_DT06/CH20148 ._CH',             # 27
        'ED6_DT06/CH20149 ._CH',             # 28
        'ED6_DT06/CH20150 ._CH',             # 29
        'ED6_DT06/CH20151 ._CH',             # 2A
        'ED6_DT06/CH20152 ._CH',             # 2B
        'ED6_DT06/CH20153 ._CH',             # 2C
        'ED6_DT06/CH20154 ._CH',             # 2D
    )

    AddCharChipPat(
        'ED6_DT07/CH01610P._CP',             # 00
        'ED6_DT07/CH02460P._CP',             # 01
        'ED6_DT07/CH02230P._CP',             # 02
        'ED6_DT07/CH02240P._CP',             # 03
        'ED6_DT07/CH02100P._CP',             # 04
        'ED6_DT07/CH00100P._CP',             # 05
        'ED6_DT07/CH00101P._CP',             # 06
        'ED6_DT07/CH00120P._CP',             # 07
        'ED6_DT07/CH00121P._CP',             # 08
        'ED6_DT07/CH00140P._CP',             # 09
        'ED6_DT07/CH00141P._CP',             # 0A
        'ED6_DT07/CH02340P._CP',             # 0B
        'ED6_DT07/CH00030P._CP',             # 0C
        'ED6_DT07/CH00050P._CP',             # 0D
        'ED6_DT07/CH00020P._CP',             # 0E
        'ED6_DT07/CH00070P._CP',             # 0F
        'ED6_DT07/CH00060P._CP',             # 10
        'ED6_DT07/CH02020P._CP',             # 11
        'ED6_DT07/CH02000P._CP',             # 12
        'ED6_DT07/CH02060P._CP',             # 13
        'ED6_DT07/CH02070P._CP',             # 14
        'ED6_DT07/CH02450P._CP',             # 15
        'ED6_DT07/CH02080P._CP',             # 16
        'ED6_DT07/CH02090P._CP',             # 17
        'ED6_DT07/CH02010P._CP',             # 18
        'ED6_DT07/CH01180P._CP',             # 19
        'ED6_DT07/CH02350P._CP',             # 1A
        'ED6_DT07/CH02370P._CP',             # 1B
        'ED6_DT07/CH02360P._CP',             # 1C
        'ED6_DT07/CH02600P._CP',             # 1D
        'ED6_DT07/CH02620P._CP',             # 1E
        'ED6_DT07/CH01320P._CP',             # 1F
        'ED6_DT06/CH20030P._CP',             # 20
        'ED6_DT07/CH00010P._CP',             # 21
        'ED6_DT07/CH00341P._CP',             # 22
        'ED6_DT06/CH20042P._CP',             # 23
        'ED6_DT06/CH20040P._CP',             # 24
        'ED6_DT06/CH20060P._CP',             # 25
        'ED6_DT07/CH00004P._CP',             # 26
        'ED6_DT06/CH20148P._CP',             # 27
        'ED6_DT06/CH20149P._CP',             # 28
        'ED6_DT06/CH20150P._CP',             # 29
        'ED6_DT06/CH20151P._CP',             # 2A
        'ED6_DT06/CH20152P._CP',             # 2B
        'ED6_DT06/CH20153P._CP',             # 2C
        'ED6_DT06/CH20154P._CP',             # 2D
    )

    DeclNpc(
        X                   = -870,
        Z                   = 19750,
        Y                   = 107200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 910,
        Z                   = 19750,
        Y                   = 107200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -4710,
        Y                   = 18000,
        Z                   = 94670,
        Range               = 5130,
        Unknown_10          = 0x3E80,
        Unknown_14          = 0x16A1C,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -4340,
        Y                   = 19000,
        Z                   = 105990,
        Range               = 4220,
        Unknown_10          = 0x4650,
        Unknown_14          = 0x1933E,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -4280,
        Y                   = 16000,
        Z                   = 78500,
        Range               = 5010,
        Unknown_10          = 0x32C8,
        Unknown_14          = 0x1270A,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -4730,
        Y                   = 18000,
        Z                   = 98010,
        Range               = 4880,
        Unknown_10          = 0x3E80,
        Unknown_14          = 0x17534,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = -33010,
        Y                   = 15000,
        Z                   = 79090,
        Range               = -37530,
        Unknown_10          = 0x4268,
        Unknown_14          = 0x11882,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -4340,
        Y                   = 21000,
        Z                   = 108990,
        Range               = 4220,
        Unknown_10          = 0x4268,
        Unknown_14          = 0x19EF6,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )


    ScpFunction(
        "Function_0_7DA",          # 00, 0
        "Function_1_8D1",          # 01, 1
        "Function_2_966",          # 02, 2
        "Function_3_97C",          # 03, 3
        "Function_4_C04",          # 04, 4
        "Function_5_1BC3",         # 05, 5
        "Function_6_2155",         # 06, 6
        "Function_7_29B9",         # 07, 7
        "Function_8_2E89",         # 08, 8
        "Function_9_2EB2",         # 09, 9
        "Function_10_2EE0",        # 0A, 10
        "Function_11_2F0E",        # 0B, 11
        "Function_12_346F",        # 0C, 12
        "Function_13_36C6",        # 0D, 13
        "Function_14_37FF",        # 0E, 14
        "Function_15_3A35",        # 0F, 15
        "Function_16_3EDF",        # 10, 16
        "Function_17_3FA8",        # 11, 17
        "Function_18_3FAF",        # 12, 18
        "Function_19_5F1D",        # 13, 19
    )


    def Function_0_7DA(): pass

    label("Function_0_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_818")
    SetChrChipByIndex(0x2D, 32)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2D, -42970, 16000, 81320, 270)
    SetChrFlags(0x2D, 0x4)

    def lambda_807():

        label("loc_807")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_807")

    QueueWorkItem2(0x2D, 1, lambda_807)
    Event(0, 17)

    label("loc_818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_829")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_837")
    OP_A3(0x3FA)
    Event(0, 7)

    label("loc_837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_845")
    OP_A3(0x3FB)
    Event(0, 11)

    label("loc_845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_853")
    OP_A3(0x3FC)
    Event(0, 15)

    label("loc_853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_86A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FD)
    Event(0, 16)

    label("loc_86A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_87A"),
        (101, "loc_890"),
        (SWITCH_DEFAULT, "loc_8A6"),
    )


    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88D")
    OP_A2(0x63D)
    Event(0, 3)

    label("loc_88D")

    Jump("loc_8A6")

    label("loc_890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A3")
    OP_A2(0x645)
    Event(0, 6)

    label("loc_8A3")

    Jump("loc_8A6")

    label("loc_8A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D0")
    SetChrChipByIndex(0x0, 1)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_8D0")

    Return()

    # Function_0_7DA end

    def Function_1_8D1(): pass

    label("Function_1_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_8E9")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F9")

    label("loc_8E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_8F9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_965")
    OP_1B(0x0, 0x0, 0xD)
    OP_A1(0x2E, 0x0)
    OP_A1(0x2F, 0x1)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x2)
    OP_71(0x0, 0x400)
    OP_71(0x0, 0x40)
    OP_72(0x1, 0x4)
    OP_72(0x1, 0x2)
    OP_71(0x1, 0x400)
    OP_71(0x1, 0x40)
    SetChrPos(0x2E, 2320, 12050, 57280, 56)
    SetChrPos(0x2F, 2320, 12050, 57280, 56)
    OP_6F(0x0, 1200)

    label("loc_965")

    Return()

    # Function_1_8D1 end

    def Function_2_966(): pass

    label("Function_2_966")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_97B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_966")

    label("loc_97B")

    Return()

    # Function_2_966 end

    def Function_3_97C(): pass

    label("Function_3_97C")

    EventBegin(0x0)
    OP_6D(-43010, 16000, 79950, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(8050, 0)
    OP_6C(69000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 29890, 9500, 76540, 0)
    SetChrPos(0x102, 31020, 9500, 76540, 0)
    FadeToBright(2000, 0)

    def lambda_9EC():
        OP_6D(31020, 10750, 79090, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9EC)

    def lambda_A04():
        OP_6C(45000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A04)
    Sleep(7500)

    def lambda_A19():
        OP_8E(0xFE, 0x733C, 0x2EE0, 0x15306, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A19)
    Sleep(400)

    def lambda_A39():
        OP_8E(0xFE, 0x745E, 0x2EE0, 0x14DDE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A39)
    WaitChrThread(0x101, 0x2)
    Fade(1000)
    OP_6D(29640, 12000, 86120, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x101,
        (
            "#008F哇啊～……好美……\x02\x03",
            "这里就是王城的空中庭园啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊……湖面一览无余，\x01",
            "还可以俯瞰格兰赛尔周围的城邑。\x02\x03",
            "#019F想来参观的人肯定很多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呼～如果不是处于这种关头，\x01",
            "本可以好好欣赏这里的景色的……\x02\x03",
            "#006F现在还是优先完成任务吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    EventEnd(0x0)
    Return()

    # Function_3_97C end

    def Function_4_C04(): pass

    label("Function_4_C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_END)), "loc_C0C")
    Return()

    label("loc_C0C")

    OP_A2(0x63E)
    OP_28(0x49, 0x1, 0x400)
    EventBegin(0x0)
    OP_8C(0x101, 0, 0)
    OP_8C(0x102, 0, 0)

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F看来这里就是女王宫了……\x02",
    )

    CloseMessageWindow()

    def lambda_C64():

        label("loc_C64")

        OP_8C(0xFE, 0, 0)
        OP_48()
        Jump("loc_C64")

    QueueWorkItem2(0x101, 2, lambda_C64)

    def lambda_C75():

        label("loc_C75")

        OP_8C(0xFE, 0, 0)
        OP_48()
        Jump("loc_C75")

    QueueWorkItem2(0x102, 2, lambda_C75)

    def lambda_C86():
        OP_8E(0xFE, 0x370, 0x4650, 0x194BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C86)

    def lambda_CA1():
        OP_8E(0xFE, 0xFFFFFD76, 0x4650, 0x19438, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CA1)

    def lambda_CBC():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_CBC)
    OP_6D(-160, 19000, 105620, 3000)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "唔……你们是什么人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哦……他们是……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)

    ChrTalk(
        0x101,
        (
            "#006F没错……\x02\x03",
            "我们两个是公爵邀请的客人……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x102,
        (
            "#010F这里就是陛下居住的女王宫对吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "……是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过这几天\x01",
            "陛下的身体欠佳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "想要晋见是不行的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F这、这样啊～\x01",
            "没有想到陛下会身体不适呢。\x02\x03",
            "这么说来，\x01",
            "可得小心照料～才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F请问一下，\x01",
            "科洛蒂娅公主也在里面吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不，里面是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 800)

    ChrTalk(
        0x9,
        "……喂。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哦哦，\x01",
            "公主正在细心地看护着陛下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "当然也就没有空闲\x01",
            "来招呼你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, 280, 20000, 111970, 0)

    NpcTalk(
        0xA,
        "女性的声音",
        (
            "#4P……请问，\x01",
            "你们在那里做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0xA, 0x80)

    def lambda_1038():
        OP_8E(0xFE, 0x82, 0x4C2C, 0x1A13A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1038)

    def lambda_1053():

        label("loc_1053")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1053")

    QueueWorkItem2(0x8, 1, lambda_1053)

    def lambda_1064():
        OP_8E(0xFE, 0xFFFFF9FC, 0x4D26, 0x1A22A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1064)

    def lambda_107F():

        label("loc_107F")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_107F")

    QueueWorkItem2(0x9, 1, lambda_107F)

    def lambda_1090():
        OP_8E(0xFE, 0xFFFFFA24, 0x4B32, 0x19EEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1090)
    WaitChrThread(0x9, 0x2)

    ChrTalk(
        0x8,
        "#3P夫人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3P您这就要回去了吗？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x2)
    TurnDirection(0xA, 0x8, 400)

    NpcTalk(
        0xA,
        "中年女性",
        (
            "#710F#2P晚宴很快就要开始了，\x01",
            "我得先回休息室准备一下。\x02\x03",
            "对了，这两位客人是……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3P武术大会优胜组的成员。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3P只不过是些游击士罢了，\x01",
            "但也还算是邀请的客人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F哼，什么叫只不过是游击士……！\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "中年女性",
        "#717F#2P#5S岂能如此无礼！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(200)

    NpcTalk(
        0xA,
        "中年女性",
        (
            "#717F#2P你这就等同于在侮辱\x01",
            "邀请客人的公爵大人！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x9,
        "#3P不……我们不是那个意思……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "中年女性",
        (
            "#717F#2P虽说是由公爵大人邀请而来的，\x01",
            "但只要是王城的来访者，就是陛下的客人！\x02\x03",
            "这一点是绝对不能忘记的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3P明、明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F（好、好惊人的气势……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F（难道这个人就是……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3P可是夫人……\x01",
            "他们要想进去是肯定不行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3P这一点上校说得很清楚了，\x01",
            "您也应该很明白吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "中年女性",
        "#716F#2P……这个我已经听腻了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)

    def lambda_1551():

        label("loc_1551")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_1551")

    QueueWorkItem2(0x101, 1, lambda_1551)

    def lambda_1562():

        label("loc_1562")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_1562")

    QueueWorkItem2(0x102, 1, lambda_1562)
    OP_8E(0xA, 0x8C, 0x4844, 0x19938, 0x7D0, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    NpcTalk(
        0xA,
        "中年女性",
        (
            "#710F#5P非常抱歉，两位客人。\x02\x03",
            "因为加强戒备的缘故，\x01",
            "所以最近禁止其他人接近女王宫。\x02\x03",
            "如果可以的话，\x01",
            "晚宴开始之前请在房间里等候好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……好、好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F明白了。\x01",
            "还是这样比较好一些。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        (
            "#015F……实在是对不起。\x01",
            "我们带来了不少麻烦。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "哼……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        "知道就好，人要知趣。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    NpcTalk(
        0xA,
        "中年女性",
        "#714F#2P……………………（怒视）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……那么\x01",
            "这就请回吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(470, 15250, 86110, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, -620, 15500, 86640, 180)
    SetChrPos(0x102, 1430, 15500, 86590, 180)
    SetChrPos(0xA, 310, 15000, 85930, 180)

    def lambda_180C():

        label("loc_180C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_180C")

    QueueWorkItem2(0x101, 1, lambda_180C)

    def lambda_181D():

        label("loc_181D")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_181D")

    QueueWorkItem2(0x102, 1, lambda_181D)

    def lambda_182E():
        OP_8E(0xFE, 0xFFFFFF24, 0x36B0, 0x139A2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_182E)

    def lambda_1849():
        OP_8E(0xFE, 0xFFFFFC72, 0x36B0, 0x13D4E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1849)

    def lambda_1864():
        OP_8E(0xFE, 0x1EA, 0x36B0, 0x13EAC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1864)

    def lambda_187F():
        OP_6D(-90, 14000, 81270, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_187F)
    WaitChrThread(0xA, 0x1)
    OP_8C(0xA, 0, 400)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x102, 0x2)

    NpcTalk(
        0xA,
        "中年女性",
        (
            "#711F……他们做出那样丢脸的事，\x01",
            "让你们见笑了。\x02\x03",
            "真是对不起，还没有自我介绍。\x01",
            "我的名字叫希尔丹。\x02\x03",
            "我是这个格兰赛尔城的女管家，\x01",
            "主要就是监督侍女的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F果然……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来您就是希尔丹夫人啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#712F哦……\x02\x03",
            "对不起，请问\x01",
            "我们曾经认识吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F哎……\x01",
            "是从别人那里听说的。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0xA, 0x258, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "尤莉亚的介绍信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x36C, 1)
    OP_8F(0x101, 0xFFFFFC72, 0x36B0, 0x13D4E, 0x7D0, 0x0)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#712F这个笔迹是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，凭那个笔迹就可以判断是谁写的了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这封介绍信以及胸前的游击士徽章\x01",
            "就是我们两人身份的证明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#713F我明白了……\x02\x03",
            "#710F在这儿不太方便，\x01",
            "先回侍女的休息室谈谈吧。\x02\x03",
            "到那儿再向你们请教详细的情况。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4254   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_C04 end

    def Function_5_1BC3(): pass

    label("Function_5_1BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BD0")
    Return()

    label("loc_1BD0")

    OP_28(0x4A, 0x1, 0x80)
    EventBegin(0x0)
    Fade(1000)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x138, 1)
    SetChrPos(0x138, 10, 18500, 104700, 0)
    SetChrPos(0x101, -470, 18000, 103350, 0)
    SetChrPos(0x102, 740, 18000, 103280, 0)
    OP_6D(-70, 19000, 105810, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_0D()

    ChrTalk(
        0x8,
        "希尔丹夫人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "都这么晚了，\x01",
            "找陛下还有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F我把陛下吩咐过要送来的\x01",
            "红茶和一些餐具都带来了。\x02\x03",
            "#713F陛下被如此限制了自由，\x01",
            "所以我的工作也相对多了起来。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "很忙碌啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "以前没有见过这两个人啊，\x01",
            "是新来的侍女吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F公爵大人之前说过要招多一些人手，\x01",
            "这两个是新来的实习侍女。\x02\x03",
            "今天才进入城里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔～\x01",
            "的确好可爱哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#474F你、你们好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#336F………………（点头示意）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "怎么总觉得这两个人\x01",
            "好像在哪里见过呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#323F（不好……！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#714F……对年轻的姑娘\x01",
            "那样目不转睛地盯着是什么意思。\x02\x03",
            "难道是在动一些歪念头吗？\x01",
            "　\x02\x03",
            "再这样下去的话，\x01",
            "我可要向公爵大人和上校抗议了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "不、不要这样！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们作为王国军的精英\x01",
            "怎么会那样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#713F没有最好。\x02\x03",
            "#710F我说，你们好了没有，\x01",
            "可以让我们进去了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "刚才对不起！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    OP_8C(0x8, 90, 400)

    def lambda_2096():
        OP_8F(0xFE, 0xFFFFF704, 0x4D26, 0x1A2C0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2096)

    ChrTalk(
        0x9,
        "请进去吧！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)

    def lambda_20D2():
        OP_8F(0xFE, 0x92E, 0x4D26, 0x1A2C0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20D2)
    FadeToDark(2000, 0, -1)

    def lambda_20F7():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_20F7)
    Sleep(50)

    def lambda_2117():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2117)

    def lambda_2132():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2132)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4270   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1BC3 end

    def Function_6_2155(): pass

    label("Function_6_2155")

    EventBegin(0x0)
    OP_6D(-220, 20000, 107550, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x8, -2390, 19750, 107200, 180)
    SetChrPos(0x9, 2290, 19750, 107200, 180)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)

    def lambda_21A2():

        label("loc_21A2")

        TurnDirection(0xFE, 0x138, 0)
        OP_48()
        Jump("loc_21A2")

    QueueWorkItem2(0x8, 2, lambda_21A2)

    def lambda_21B3():

        label("loc_21B3")

        TurnDirection(0xFE, 0x138, 0)
        OP_48()
        Jump("loc_21B3")

    QueueWorkItem2(0x9, 2, lambda_21B3)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x138, 1)
    SetChrPos(0x101, -990, 20000, 110860, 180)
    SetChrPos(0x102, 1070, 20000, 111050, 0)
    SetChrPos(0x138, 120, 20000, 110230, 180)

    def lambda_2206():
        OP_8E(0xFE, 0xBE, 0x4B32, 0x19F64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_2206)

    def lambda_2221():
        OP_8E(0xFE, 0xFFFFFE20, 0x4D26, 0x1A310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2221)

    def lambda_223C():
        OP_8E(0xFE, 0x35C, 0x4D26, 0x1A310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_223C)
    WaitChrThread(0x138, 0x1)
    TurnDirection(0x138, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "希尔丹夫人。\x01",
            "这就要回去了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F嗯，是的。\x02\x03",
            "总之，我希望你们\x01",
            "在陛下面前不要有什么闪失。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦……这么的严肃……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过您请放心。\x01",
            "因为我们都是爱国将士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#713F那就没有什么再要拜托的了。\x02\x03",
            "那么我们这就告辞了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        "#474F再、再～见……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 135, 400)

    ChrTalk(
        0x102,
        "#336F……告辞了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x138, 180, 400)

    def lambda_23D0():
        OP_6D(230, 19000, 105820, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_23D0)

    def lambda_23E8():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_23E8)
    Sleep(100)

    def lambda_2408():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2408)

    def lambda_2423():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2423)

    def lambda_243E():
        OP_8F(0xFE, 0xFFFFFC9A, 0x4D26, 0x1A2C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_243E)
    Sleep(100)

    def lambda_245E():
        OP_8F(0xFE, 0x38E, 0x4D26, 0x1A2C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_245E)
    Sleep(1100)

    ChrTalk(
        0x8,
        "啊，两位姑娘。\x02",
    )

    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x4)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    CloseMessageWindow()

    def lambda_24DE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_24DE)

    def lambda_24EC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24EC)
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        "#324F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "突然想起一件事呢，\x01",
            "就是还没有问你们的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "告诉我们好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#473F嗯，这个嘛……\x02",
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
            "【莱娜】\x01",        # 0
            "【雪拉】\x01",        # 1
            "【朵洛希】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_25D1"),
        (1, "loc_264B"),
        (2, "loc_2731"),
        (SWITCH_DEFAULT, "loc_27C5"),
    )


    label("loc_25D1")

    OP_A2(0x676)

    ChrTalk(
        0x8,
        (
            "哦……？\x01",
            "很不错的名字嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "和你很是般配啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#328F啊，那个……\x01",
            "谢谢你们夸奖了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C5")

    label("loc_264B")

    OP_A2(0x677)

    ChrTalk(
        0x8,
        (
            "哦～\x01",
            "真是个性感的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不过本人好像比名字要逊色一些。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#325F少、少管闲事！\x02\x03",
            "#474F……啊，不是呢，哦呵呵。\x02\x03",
            "我一定会努力的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C5")

    label("loc_2731")

    OP_A2(0x678)

    ChrTalk(
        0x8,
        (
            "唔……\x01",
            "比较流行的名字啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "可是说实话，\x01",
            "这名字感觉和你不是很般配……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#327F（也许是吧……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_27C5")

    label("loc_27C5")


    ChrTalk(
        0x9,
        (
            "那边的那位\x01",
            "黑发的姑娘呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#336F……我的名字叫做卡玲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "叫卡玲……\x01",
            "好可爱的名字哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#331F多谢夸奖。\x02\x03",
            "……我对自己的名字\x01",
            "也是非常的喜欢呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "对、对了。\x01",
            "我是特务部队的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#713F难道又把我刚才的话当作耳边风了？\x02\x03",
            "这种无聊的搭讪方式，\x01",
            "就是居心不良的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "不、我可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#714F……………………（怒视）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……请吧，\x01",
            "回去的路上请注意安全。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0x2)
    OP_44(0x9, 0x2)
    OP_8C(0x8, 180, 0)
    OP_8C(0x9, 180, 0)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    SetChrChipByIndex(0x0, 1)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    Return()

    # Function_6_2155 end

    def Function_7_29B9(): pass

    label("Function_7_29B9")

    EventBegin(0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0xB, 20, 12000, 47110, 180)
    SetChrPos(0x8, 940, 12000, 48110, 180)
    SetChrPos(0x9, -900, 12000, 48050, 180)
    SetChrPos(0xC, -60, 12000, 49430, 180)
    SetChrPos(0xD, 930, 12000, 50530, 180)
    SetChrPos(0xE, 930, 12000, 52440, 180)
    SetChrPos(0xF, 910, 12000, 54110, 180)
    SetChrPos(0x10, -890, 12000, 50560, 180)
    SetChrPos(0x11, -890, 12000, 52310, 180)
    SetChrPos(0x12, -890, 12000, 54310, 180)
    OP_6D(-20, 12000, 47150, 0)
    OP_67(0, 5910, -10000, 0)
    OP_6C(45000, 0)
    OP_6B(3400, 0)
    OP_6E(280, 0)

    ChrTalk(
        0xB,
        (
            "#180F这、这怎么可能……！\x01",
            "为什么城门会自动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "上、上尉！\x01",
            "怎么办！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "这样下去的话\x01",
            "敌人会冲入城内的！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B7F():
        OP_6D(-150, 12000, 49950, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2B7F)

    def lambda_2B97():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B97)

    def lambda_2BA5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2BA5)
    OP_8C(0xB, 0, 400)

    ChrTalk(
        0xB,
        (
            "#180F第一小队留下，\x01",
            "其余的立刻赶往大门！\x02\x03",
            "绝对不能让敌人冲进城内！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "明、明白！！\x02",
    )

    CloseMessageWindow()

    def lambda_2C38():

        label("loc_2C38")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2C38")

    QueueWorkItem2(0xD, 1, lambda_2C38)

    def lambda_2C49():

        label("loc_2C49")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2C49")

    QueueWorkItem2(0xE, 1, lambda_2C49)

    def lambda_2C5A():

        label("loc_2C5A")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2C5A")

    QueueWorkItem2(0xF, 1, lambda_2C5A)

    def lambda_2C6B():

        label("loc_2C6B")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2C6B")

    QueueWorkItem2(0x10, 1, lambda_2C6B)

    def lambda_2C7C():

        label("loc_2C7C")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2C7C")

    QueueWorkItem2(0x11, 1, lambda_2C7C)

    def lambda_2C8D():

        label("loc_2C8D")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2C8D")

    QueueWorkItem2(0x12, 1, lambda_2C8D)
    OP_8E(0xC, 0x906, 0x2EE0, 0xC166, 0x1388, 0x0)
    OP_8E(0xC, 0x906, 0x2EE0, 0xC5F8, 0x1388, 0x0)
    OP_43(0xD, 0x1, 0x0, 0x8)
    OP_43(0x10, 0x1, 0x0, 0x8)
    OP_8E(0xC, 0x906, 0x2EE0, 0xCCA6, 0x1388, 0x0)
    OP_43(0xE, 0x1, 0x0, 0x9)
    OP_43(0x11, 0x1, 0x0, 0x9)
    OP_8E(0xC, 0x906, 0x2EE0, 0xD796, 0x1388, 0x0)
    OP_43(0xF, 0x1, 0x0, 0xA)
    OP_43(0x12, 0x1, 0x0, 0xA)

    def lambda_2D18():
        OP_8E(0xFE, 0x92E, 0x2EE0, 0x11814, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2D18)
    OP_6D(90, 12000, 48130, 1000)

    ChrTalk(
        0xB,
        (
            "#180F可恶，太丢脸了……\x02\x03",
            "在阁下回来之前\x01",
            "无论如何也不能被击败……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2DD8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2DD8)

    def lambda_2DE6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2DE6)
    Sleep(1000)

    ChrTalk(
        0x8,
        "上、上尉！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "特、是特务飞行艇！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#180F糟糕了！\x01",
            "那个才是主力部队吗！？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/E0500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_29B9 end

    def Function_8_2E89(): pass

    label("Function_8_2E89")

    OP_8E(0xFE, 0x92E, 0x2EE0, 0xC5C6, 0x1388, 0x0)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0x11814, 0x1388, 0x0)
    Return()

    # Function_8_2E89 end

    def Function_9_2EB2(): pass

    label("Function_9_2EB2")

    Sleep(800)
    OP_8E(0xFE, 0x8F2, 0x2EE0, 0xCC92, 0x1388, 0x0)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0x11814, 0x1388, 0x0)
    Return()

    # Function_9_2EB2 end

    def Function_10_2EE0(): pass

    label("Function_10_2EE0")

    Sleep(1300)
    OP_8E(0xFE, 0x8F2, 0x2EE0, 0xD3F4, 0x1388, 0x0)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0x11814, 0x1388, 0x0)
    Return()

    # Function_10_2EE0 end

    def Function_11_2F0E(): pass

    label("Function_11_2F0E")

    EventBegin(0x0)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x0, 0xFF)
    AddParty(0x2, 0xFF)
    AddParty(0x4, 0xFF)
    OP_6D(610, 15350, 55470, 0)
    OP_67(0, 5210, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(29000, 0)
    OP_6E(413, 0)
    SetChrPos(0x8, -8650, 12000, 56840, 79)
    SetChrPos(0xB, -8029, 12000, 58490, 125)
    SetChrPos(0x9, -6650, 12000, 57720, 46)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    def lambda_2FA7():

        label("loc_2FA7")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2FA7")

    QueueWorkItem2(0xB, 1, lambda_2FA7)

    def lambda_2FB8():

        label("loc_2FB8")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2FB8")

    QueueWorkItem2(0x8, 1, lambda_2FB8)

    def lambda_2FC9():

        label("loc_2FC9")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2FC9")

    QueueWorkItem2(0x9, 1, lambda_2FC9)
    SetChrPos(0x101, 2880, 15350, 57740, 147)
    SetChrPos(0x103, 2880, 15350, 57740, 147)
    SetChrPos(0x105, 2880, 15350, 57740, 147)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x105, 9)
    FadeToBright(2000, 0)

    def lambda_3025():
        OP_67(0, 7370, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_3025)
    OP_6F(0x0, 241)
    OP_70(0x0, 0x168)
    OP_73(0x0)
    OP_6F(0x0, 1140)
    OP_70(0x0, 0x4B0)
    OP_73(0x0)

    def lambda_305F():

        label("loc_305F")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_305F")

    QueueWorkItem2(0x101, 1, lambda_305F)

    def lambda_3070():

        label("loc_3070")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_3070")

    QueueWorkItem2(0x105, 1, lambda_3070)

    def lambda_3081():

        label("loc_3081")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_3081")

    QueueWorkItem2(0x103, 1, lambda_3081)

    def lambda_3092():
        OP_6D(-7590, 12000, 54940, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3092)

    def lambda_30AA():
        OP_6E(291, 4000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_30AA)

    def lambda_30BA():
        OP_8E(0xFE, 0xFFFFECB4, 0x31A6, 0xD00C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30BA)
    Sleep(400)

    def lambda_30DA():
        OP_8E(0xFE, 0xFFFFE3C2, 0x2EE0, 0xC8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_30DA)
    Sleep(400)

    def lambda_30FA():
        OP_8E(0xFE, 0xFFFFE912, 0x2EE0, 0xCB52, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_30FA)
    WaitChrThread(0x101, 0x2)

    def lambda_311A():
        OP_96(0xFE, 0xFFFFE480, 0x2EE0, 0xCDDC, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_311A)
    WaitChrThread(0x103, 0x2)

    def lambda_313D():
        OP_8E(0xFE, 0xFFFFDE7C, 0x2EE0, 0xCD00, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_313D)
    WaitChrThread(0x105, 0x2)

    def lambda_315D():
        OP_8E(0xFE, 0xFFFFE16A, 0x2EE0, 0xC8E6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_315D)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0xB,
        (
            "#180F艾、艾丝蒂尔·布莱特！？\x02\x03",
            "以及……科洛蒂娅殿下！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F凯诺娜上尉！\x01",
            "又来麻烦你了哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F我们是来……\x01",
            "营救我祖母的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#180F不、不要欺人太甚了，小丫头们！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0x3A8, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_3264"),
        (SWITCH_DEFAULT, "loc_3267"),
    )


    label("loc_3264")

    OP_B4(0x0)
    Return()

    label("loc_3267")

    EventBegin(0x0)
    OP_6D(-7800, 12000, 57810, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(9000, 0)
    OP_6E(280, 0)
    SetChrPos(0xB, -9230, 12000, 57550, 258)
    SetChrPos(0x8, -9060, 12000, 59260, 302)
    SetChrPos(0x9, -7670, 12000, 59020, 103)
    SetChrPos(0x101, -6550, 12000, 56030, 282)
    SetChrPos(0x103, -8180, 12000, 54960, 331)
    SetChrPos(0x105, -7070, 12000, 54530, 325)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 36)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 35)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 35)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 65535)
    OP_51(0x105, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 65535)

    ChrTalk(
        0x103,
        (
            "#020F真令人毛骨悚然……\x01",
            "好一个可怕的女人啊。\x02\x03",
            "到底是谁？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F理查德上校的副官。\x02\x03",
            "是只典型的狐狸精。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F原来如此，这种感觉啊。\x02\x03",
            "接下来……目标女王宫！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F好的，赶快走吧！\x02",
    )

    CloseMessageWindow()
    OP_28(0x4E, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_11_2F0E end

    def Function_12_346F(): pass

    label("Function_12_346F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_347C")
    Return()

    label("loc_347C")

    EventBegin(0x0)
    OP_A2(0x662)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xE, 13020, 14000, 78670, 270)
    SetChrPos(0xF, 14450, 14000, 79840, 270)
    SetChrPos(0x10, 14130, 14000, 77880, 270)

    ChrTalk(
        0xE,
        "来了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "在那儿！\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x101, 1230, 14000, 77770, 90)
    SetChrPos(0x103, -420, 14000, 78370, 90)
    SetChrPos(0x105, -300, 14000, 77020, 90)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x105, 9)
    OP_6D(6360, 14000, 78900, 2000)

    ChrTalk(
        0x101,
        "#000F哇，又来了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F哼，装腔作势的家伙们！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 34)
    SetChrChipByIndex(0xF, 34)
    SetChrChipByIndex(0x10, 34)

    def lambda_35AB():
        OP_6D(2650, 14000, 77790, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35AB)

    def lambda_35C3():
        OP_8E(0xFE, 0xFFFFAFD8, 0x36B0, 0x130EC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_35C3)

    def lambda_35DE():
        OP_8E(0xFE, 0xFFFFAFD8, 0x36B0, 0x130EC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_35DE)

    def lambda_35F9():
        OP_8E(0xFE, 0xFFFFAFD8, 0x36B0, 0x130EC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_35F9)
    Sleep(500)
    Battle(0x3A9, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_362C"),
        (SWITCH_DEFAULT, "loc_362F"),
    )


    label("loc_362C")

    OP_B4(0x0)
    Return()

    label("loc_362F")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrPos(0x101, 1230, 14000, 77770, 90)
    SetChrPos(0x103, -420, 14000, 78370, 90)
    SetChrPos(0x105, -300, 14000, 77020, 90)
    SetChrPos(0xE, 3390, 14000, 79480, 146)
    SetChrPos(0xF, 3080, 14000, 77370, 283)
    SetChrPos(0x10, 5260, 14000, 77990, 28)
    Sleep(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)
    EventEnd(0x0)
    Return()

    # Function_12_346F end

    def Function_13_36C6(): pass

    label("Function_13_36C6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3730")

    ChrTalk(
        0x105,
        (
            "#040F艾丝蒂尔！\x01",
            "这边是去城内的路！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F我们要赶快去女王宫！\x02",
    )

    CloseMessageWindow()
    Jump("loc_37E3")

    label("loc_3730")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_377B")

    ChrTalk(
        0x105,
        (
            "#040F不行……！\x01",
            "必须赶快去女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E3")

    label("loc_377B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37E3")

    ChrTalk(
        0x103,
        (
            "#020F哎呀，这边\x01",
            "不是女王宫！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，在西北方！\x02",
    )

    CloseMessageWindow()

    label("loc_37E3")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_13_36C6 end

    def Function_14_37FF(): pass

    label("Function_14_37FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_380C")
    Return()

    label("loc_380C")

    EventBegin(0x0)
    OP_A2(0x664)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, -870, 19750, 107400, 180)
    SetChrPos(0x9, 910, 19750, 107400, 180)
    Fade(1000)
    SetChrPos(0x101, 100, 17250, 98400, 0)
    SetChrPos(0x103, -1300, 17000, 97610, 0)
    SetChrPos(0x105, 1670, 17000, 97720, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x105, 9)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x103, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    OP_6D(290, 18000, 103070, 0)

    ChrTalk(
        0x8,
        "来、来了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "此路不通！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F但……\x01",
            "我们必须要通过这里！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F再阻拦的话\x01",
            "就把你们打飞！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_392B():
        OP_6D(2650, 14000, 77790, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_392B)

    def lambda_3943():
        OP_8E(0xFE, 0xFFFFFECA, 0x4B32, 0x1F676, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3943)

    def lambda_395E():
        OP_8E(0xFE, 0xFFFFFECA, 0x4B32, 0x1F676, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_395E)

    def lambda_3979():
        OP_8E(0xFE, 0xFFFFFECA, 0x4B32, 0x1F676, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3979)
    Sleep(500)
    Battle(0x3A9, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_39AC"),
        (SWITCH_DEFAULT, "loc_39AF"),
    )


    label("loc_39AC")

    OP_B4(0x0)
    Return()

    label("loc_39AF")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrPos(0x8, -2290, 19000, 105820, 236)
    SetChrPos(0x9, 2930, 18000, 103750, 112)
    SetChrPos(0x101, -10, 18000, 103540, 351)
    SetChrPos(0x103, -1250, 18000, 101680, 4)
    SetChrPos(0x105, 1290, 18000, 101820, 5)
    Sleep(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)
    EventEnd(0x0)
    Return()

    # Function_14_37FF end

    def Function_15_3A35(): pass

    label("Function_15_3A35")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_6D(30, 12000, 67150, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, -6690, 12000, 53510, 0)
    SetChrPos(0x102, -6380, 12000, 54650, 0)
    ClearChrFlags(0x13, 0x80)
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
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    SetChrPos(0x14, -7210, 12000, 58180, 0)
    SetChrPos(0x15, -9680, 12000, 54680, 0)
    SetChrPos(0x16, -7920, 12000, 56380, 0)
    SetChrPos(0x17, -10390, 12000, 56310, 0)
    SetChrPos(0x18, 6170, 12000, 53150, 0)
    SetChrPos(0x19, 6210, 12000, 53870, 0)
    SetChrPos(0x1A, -7990, 12000, 54100, 0)
    SetChrPos(0x1B, -10220, 12000, 52510, 0)
    SetChrPos(0x1C, -6470, 12000, 48980, 0)
    SetChrPos(0x1D, -1110, 12000, 70820, 0)
    SetChrPos(0x1E, 1020, 12000, 70710, 0)
    SetChrPos(0x1F, 10, 12000, 71740, 0)
    SetChrPos(0x20, 20, 12000, 67080, 0)
    SetChrPos(0x13, 650, 12000, 67820, 0)
    SetChrPos(0x21, 6760, 12000, 57310, 0)
    SetChrPos(0x22, 5980, 12000, 57880, 0)
    SetChrPos(0x23, 7530, 12000, 55190, 0)
    SetChrPos(0x24, 6470, 12000, 55570, 0)
    SetChrPos(0x25, 9010, 12000, 57270, 0)
    SetChrPos(0x26, 9250, 12000, 55950, 0)
    SetChrPos(0x27, -4290, 14000, 77250, 180)
    SetChrPos(0x28, 4190, 14000, 77300, 180)
    SetChrPos(0x29, -4270, 12000, 70900, 180)
    SetChrPos(0x2A, 4210, 12000, 70900, 180)

    def lambda_3CC7():
        OP_8E(0xFE, 0xFFFFFBAA, 0x2EE0, 0xD23C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3CC7)

    def lambda_3CE2():
        OP_8E(0xFE, 0x3FC, 0x2EE0, 0xD1CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3CE2)

    def lambda_3CFD():
        OP_8E(0xFE, 0xA, 0x2EE0, 0xD5D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3CFD)

    def lambda_3D18():
        OP_8E(0xFE, 0x14, 0x2EE0, 0xC3A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3D18)

    def lambda_3D33():
        OP_8E(0xFE, 0x28A, 0x2EE0, 0xC684, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3D33)

    def lambda_3D4E():

        label("loc_3D4E")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3D4E")

    QueueWorkItem2(0x101, 1, lambda_3D4E)

    def lambda_3D5F():

        label("loc_3D5F")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3D5F")

    QueueWorkItem2(0x102, 1, lambda_3D5F)

    def lambda_3D70():

        label("loc_3D70")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3D70")

    QueueWorkItem2(0x14, 1, lambda_3D70)

    def lambda_3D81():

        label("loc_3D81")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3D81")

    QueueWorkItem2(0x15, 1, lambda_3D81)

    def lambda_3D92():

        label("loc_3D92")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3D92")

    QueueWorkItem2(0x16, 1, lambda_3D92)

    def lambda_3DA3():

        label("loc_3DA3")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3DA3")

    QueueWorkItem2(0x17, 1, lambda_3DA3)

    def lambda_3DB4():

        label("loc_3DB4")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3DB4")

    QueueWorkItem2(0x18, 1, lambda_3DB4)

    def lambda_3DC5():

        label("loc_3DC5")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3DC5")

    QueueWorkItem2(0x19, 1, lambda_3DC5)

    def lambda_3DD6():

        label("loc_3DD6")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3DD6")

    QueueWorkItem2(0x1A, 1, lambda_3DD6)

    def lambda_3DE7():

        label("loc_3DE7")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3DE7")

    QueueWorkItem2(0x1B, 1, lambda_3DE7)

    def lambda_3DF8():

        label("loc_3DF8")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3DF8")

    QueueWorkItem2(0x1C, 1, lambda_3DF8)

    def lambda_3E09():

        label("loc_3E09")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3E09")

    QueueWorkItem2(0x21, 1, lambda_3E09)

    def lambda_3E1A():

        label("loc_3E1A")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3E1A")

    QueueWorkItem2(0x22, 1, lambda_3E1A)

    def lambda_3E2B():

        label("loc_3E2B")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3E2B")

    QueueWorkItem2(0x23, 1, lambda_3E2B)

    def lambda_3E3C():

        label("loc_3E3C")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3E3C")

    QueueWorkItem2(0x24, 1, lambda_3E3C)

    def lambda_3E4D():

        label("loc_3E4D")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3E4D")

    QueueWorkItem2(0x25, 1, lambda_3E4D)

    def lambda_3E5E():

        label("loc_3E5E")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_3E5E")

    QueueWorkItem2(0x26, 1, lambda_3E5E)

    def lambda_3E6F():
        OP_6D(-1510, 12000, 54280, 9000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3E6F)

    def lambda_3E87():
        OP_6E(342, 9000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3E87)
    WaitChrThread(0x0, 0x2)
    Sleep(1000)

    def lambda_3EA1():
        OP_6D(0, 12000, 47170, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3EA1)
    OP_8E(0x20, 0x1E, 0x2EE0, 0xB87E, 0x3E8, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_3A35 end

    def Function_16_3EDF(): pass

    label("Function_16_3EDF")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    OP_6D(-670, 4500, 47060, 0)
    OP_67(0, 2670, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(338000, 0)
    OP_6E(538, 0)

    def lambda_3F37():
        OP_67(0, 6660, -10000, 16000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F37)

    def lambda_3F4F():
        OP_6B(5000, 16000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F4F)

    def lambda_3F5F():
        OP_6D(390, 14500, 76830, 16000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F5F)
    Sleep(2000)

    def lambda_3F7C():
        OP_6C(50000, 14000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F7C)
    Sleep(10000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4261   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3EDF end

    def Function_17_3FA8(): pass

    label("Function_17_3FA8")

    OP_1F(0x64, 0xC8)
    Return()

    # Function_17_3FA8 end

    def Function_18_3FAF(): pass

    label("Function_18_3FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FB8")
    Return()

    label("loc_3FB8")

    EventBegin(0x0)
    SetChrFlags(0x2D, 0x40)
    SetChrChipByIndex(0x2D, 32)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2D, -42970, 16000, 81320, 270)
    SetChrFlags(0x2D, 0x4)

    def lambda_3FE5():

        label("loc_3FE5")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_3FE5")

    QueueWorkItem2(0x2D, 1, lambda_3FE5)
    Fade(1000)
    OP_6D(-47380, 16000, 81820, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(1470, 0)
    OP_6C(45000, 0)
    OP_6E(532, 0)

    def lambda_403A():
        OP_6D(-44280, 16000, 81720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_403A)
    WaitChrThread(0x101, 0x2)
    OP_20(0x7D0)
    OP_21()
    OP_44(0x2D, 0xFF)
    Sleep(1000)
    SetChrPos(0x101, -34850, 16000, 75130, 0)

    def lambda_4077():
        OP_6D(-42280, 16000, 81720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4077)

    def lambda_408F():
        OP_8E(0xFE, 0xFFFF5EAC, 0x3E80, 0x13C68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_408F)
    Sleep(2000)
    OP_51(0x2D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2D, 33)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x2D, 400)
    Sleep(500)
    TurnDirection(0x2D, 0x101, 400)
    Sleep(500)

    ChrTalk(
        0x2D,
        (
            "#011F……啊，艾丝蒂尔。\x02\x03",
            "今天的夜色真美啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯……\x02\x03",
            "还是这首曲子啊。\x02\x03",
            "『星之所在』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#015F我曾经失去了许多东西……\x02\x03",
            "只有这首曲子、这支口琴，\x01",
            "至今仍陪伴着我……\x02\x03",
            "所以，我会经常吹起它。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#010F我是不是该履行约定了呢。\x02\x03",
            "和你相遇之前……我所经历过的事情……\x01",
            "　\x02\x03",
            "现在，我全部告诉你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F约修亚……\x02\x03",
            "#002F嗯……我知道了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x2D,
        (
            "#013F不过，故事稍微有点长……\x01",
            "即使这样……你也不会介意吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F当然……\x01",
            "我肯定会认真地听到最后的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#019F谢谢……\x02\x03",
            "#011F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x2D, 0xFF)

    def lambda_4317():
        OP_6C(86000, 3000)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_4317)
    Sleep(1500)
    OP_8C(0x2D, 270, 400)
    ClearChrFlags(0x2D, 0x1)
    OP_8E(0x2D, 0xFFFF5600, 0x3E1C, 0x13DDA, 0x320, 0x0)
    SetChrChipByIndex(0x2D, 39)
    SetChrFlags(0x2D, 0x2)
    SetChrSubChip(0x2D, 8)
    WaitChrThread(0x2D, 0x1)
    OP_99(0x2D, 0x8, 0xA, 0x320)
    OP_1D(0x5B)
    Sleep(1000)

    ChrTalk(
        0x2D,
        (
            "#015F很久以前，在某个地方……\x02\x03",
            "在某个地方，有一个男孩。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "一个非常爱撒娇、个性懦弱、\x01",
            "而且没有任何长处的男孩……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "不过，因为和最重要的亲人生活在一起，\x01",
            "男孩每天都过得非常幸福。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x4002F, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "但是，因为某件事的发生，\x01",
            "男孩的心完全地破碎了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "丧失了言语和感情，\x01",
            "连饭也不吃地每天只吹着口琴……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "照顾他的人无论多么地努力，\x01",
            "也只能看着男孩一天比一天衰弱。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_AD(0x40030, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "就在这时，一个魔法师出现在男孩面前。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "『我可以治好这孩子的心。』\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "『不过要向我付出代价。』\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "就这样，男孩被交托给魔法师。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    SetChrName("约修亚")

    AnonymousTalk(
        "破碎的心被重新整合在一起……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "然而，魔法师也将男孩的存在肆意地修改。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "终于，当得到新的心的时候——\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        "男孩变成了一个杀手。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x40031, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "在两年的时间里，\x01",
            "男孩每天都在不断地杀人。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "曾经将几十人的部队暗中全灭。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "曾经潜入守卫森严的某国大臣的住宅，\x01",
            "将大臣的喉咙切断。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "有时还使用炸药，\x01",
            "将无辜的人们卷入灾难之中。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "不知何时起，男孩从一个普通的杀手\x01",
            "化身为一只可怕的怪物……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "不知何时起，男孩被称作『漆黑之牙』，\x01",
            "变成了一个令人恐惧的存在。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "之后，男孩接到了魔法师的命令，\x01",
            "去暗杀某个目标人物。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x40032, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "那是一个曾经守卫了女王治理的国家、\x01",
            "成功地击退了北方大国侵略的英雄。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "同时也是大陆上拥有特别称号的\x01",
            "四个游击士的其中一个。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "——但是，那个人实在太强大了。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "就像小猫被老虎轻松闪避一样，\x01",
            "男孩一下子就被目标人物击退了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "在任务失败的男孩面前，\x01",
            "出现了魔法师派来的手下。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "他们是为了解决\x01",
            "被目标人物看到真面目的男孩而来的。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "但是，有一个人将他们赶走，\x01",
            "还救下了男孩。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x40033, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "他正是男孩暗杀失败的那个目标人物。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "之后，男孩……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "被那个人带到了自己的家里，\x01",
            "而且，还和一个女孩相遇了……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x64)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    Sleep(500)

    ChrTalk(
        0x2D,
        (
            "#015F在那个家里，男孩过着幸福的生活。\x01",
            "是如同梦境一样的、五年的幸福时光。\x02\x03",
            "也许，对那个男孩来说，\x01",
            "那是一场他不被允许去拥有的美梦……\x02\x03",
            "所以，梦终究会消失。\x02\x03",
            "回到现实的时刻也已经迫近。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x2D, 0xA, 0x8, 0x320)
    Sleep(500)
    Fade(500)
    SetChrPos(0x2D, -43500, 16000, 81370, 270)
    SetChrChipByIndex(0x2D, 33)
    ClearChrFlags(0x2D, 0x2)
    SetChrSubChip(0x2D, 0)
    OP_0D()

    def lambda_4DFE():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_4DFE)
    Sleep(1000)
    TurnDirection(0x2D, 0x101, 400)
    WaitChrThread(0x2D, 0x1)

    ChrTalk(
        0x2D,
        (
            "#011F到这里……故事就结束了。\x02\x03",
            "谢谢你……\x01",
            "能够一直坚持着听到最后。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F…………………………………\x02\x03",
            "#506F……哎……啊哈…………\x02\x03",
            "究竟……哪些才是真的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#015F全部，都是真的。\x02\x03",
            "我的心已经破碎了。\x02\x03",
            "我的手沾满了血。\x02\x03",
            "还有暗杀你的父亲失败。\x01",
            "……所有所有的事，都是真的。\x02\x03",
            "#013F而且……\x01",
            "到现在也仍一直在背叛着你们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#590F男孩真的是无可救药的怪物。\x01",
            "　\x02\x03",
            "不管到哪里……\x01",
            "都只会带来不幸和灾厄……\x02\x03",
            "他就是这样污秽的存在……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#011F所以……\x01",
            "男孩决定要踏上旅途。\x02\x03",
            "为了不再使那些让自己做了\x01",
            "如此幸福的美梦的人被卷进来。\x02\x03",
            "也为了阻止那个\x01",
            "制造了自己这种怪物的邪恶魔法师。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x2D, 0x2)
    SetChrFlags(0x2D, 0x1000)
    SetChrChipByIndex(0x2D, 40)

    def lambda_50EA():

        label("loc_50EA")

        OP_99(0xFE, 0x0, 0x7, 0x4B0)
        OP_48()
        Jump("loc_50EA")

    QueueWorkItem2(0x2D, 1, lambda_50EA)

    def lambda_50FD():
        OP_8F(0xFE, 0xFFFF5C0E, 0x3E80, 0x13C68, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_50FD)
    Sleep(500)
    SetChrFlags(0x2D, 0x1)
    WaitChrThread(0x2D, 0x2)
    OP_22(0x8F, 0x0, 0x50)
    OP_44(0x2D, 0x1)
    ClearChrFlags(0x2D, 0x1000)
    ClearChrFlags(0x2D, 0x2)
    SetChrChipByIndex(0x2D, 33)
    SetChrSubChip(0x2D, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 42)
    SetChrFlags(0x101, 0x2)
    Sleep(500)

    def lambda_5158():
        OP_8F(0xFE, 0xFFFF56DC, 0x3E80, 0x13C68, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_5158)
    Sleep(1000)
    ClearChrFlags(0x2D, 0x1)
    WaitChrThread(0x2D, 0x2)
    SetChrSubChip(0x101, 30)
    Sleep(100)
    SetChrSubChip(0x101, 31)
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#580F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#011F这是让我将人的心一直保持到最后的东西。\x01",
            "　\x02\x03",
            "但是，我已经不需要它了……\x02\x03",
            "所以，希望你能收下来。\x02\x03",
            "#019F虽然可能算不上这五年来的谢礼……\x01",
            "　\x02\x03",
            "不过，我想总比什么都没有要好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F………………………………\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x0, 0x2, 0x320)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        "#582F…………你说够了没有。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#014F咦……？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 43)

    def lambda_52F1():

        label("loc_52F1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_52F1")

    QueueWorkItem2(0x101, 1, lambda_52F1)
    SetChrFlags(0x101, 0x1000)
    OP_8F(0x101, 0xFFFF5AC4, 0x3E80, 0x13C68, 0xBB8, 0x0)
    OP_44(0x101, 0x1)
    SetChrSubChip(0x101, 0)

    ChrTalk(
        0x101,
        "#005F#3S#2P你究竟说够了没有！\x02",
    )

    SetChrChipByIndex(0x101, 42)
    OP_99(0x101, 0x3, 0x4, 0x3E8)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#003F#2P说什么在做梦……！\x02\x03",
            "难道……到现在为止的事情，\x01",
            "全部都不是真的吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x12, 0x14, 0x320)
    OP_99(0x101, 0x13, 0x12, 0x320)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#508F#2P过去怎么了！？\x02\x03",
            "心破碎了！？\x01",
            "那又怎么样！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#013F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x6, 0x8, 0x320)
    OP_99(0x101, 0x7, 0x6, 0x320)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#005F#2P看着我！\x02\x03",
            "看着我的眼睛！\x02\x03",
            "#003F我一直……\x01",
            "把那男孩的事情看在眼里！\x02\x03",
            "好的地方、不好的地方我都清楚！\x02\x03",
            "男孩不管承受怎样的痛苦、\x01",
            "都会抱着坚定决心努力下去的地方我也清楚！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#504F#2P#3S因为……\x01",
            "我喜欢那样的约修亚！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#014F！！！\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x9, 0x10, 0x5DC)

    def lambda_55A2():

        label("loc_55A2")

        OP_99(0xFE, 0xE, 0x10, 0x320)
        OP_48()
        Jump("loc_55A2")

    QueueWorkItem2(0x101, 1, lambda_55A2)

    ChrTalk(
        0x101,
        (
            "#583F#2P所以，我绝对不会让你一个人去的！\x02\x03",
            "就这样丢下我、不理会我的感受，\x01",
            "自己一个人背负着痛苦地离开！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    SetChrSubChip(0x101, 17)
    Sleep(50)
    SetChrSubChip(0x101, 18)
    Sleep(150)
    SetChrSubChip(0x101, 19)
    Sleep(50)
    SetChrSubChip(0x101, 20)
    Sleep(50)
    SetChrSubChip(0x101, 18)

    ChrTalk(
        0x101,
        "#583F#3S#2P我绝对不允许！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#012F……艾丝蒂尔………\x02\x03",
            "#015F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5694():
        OP_6D(-41780, 16000, 81720, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5694)
    OP_99(0x101, 0x15, 0x18, 0x4B0)

    def lambda_56B5():
        OP_8E(0xFE, 0xFFFF58E4, 0x3E80, 0x13C68, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_56B5)
    Sleep(500)
    SetChrFlags(0x2D, 0x1)
    WaitChrThread(0x2D, 0x2)
    Fade(500)
    OP_20(0x7D0)
    SetChrPos(0x2D, -42300, 16000, 81000, 90)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x2D, 0x2)
    SetChrChipByIndex(0x2D, 41)
    SetChrSubChip(0x2D, 0)
    OP_0D()
    OP_99(0x2D, 0x0, 0x2, 0x708)
    Sleep(500)

    ChrTalk(
        0x101,
        "#004F#2P啊……？\x02",
    )

    OP_99(0x2D, 0x3, 0x4, 0x5DC)
    CloseMessageWindow()
    OP_21()
    OP_1D(0x50)
    Sleep(1000)
    Fade(1000)

    def lambda_5748():
        OP_6B(1300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5748)
    SetChrSubChip(0x2D, 5)
    Sleep(500)

    ChrTalk(
        0x101,
        "#2P………啊………………\x02",
    )

    CloseMessageWindow()
    OP_99(0x2D, 0x5, 0x6, 0x320)
    Sleep(500)

    ChrTalk(
        0x101,
        "#2P（………约修亚…………）\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    SetChrSubChip(0x2D, 5)
    Sleep(500)
    ClearChrFlags(0x101, 0x80)
    SetChrChipByIndex(0x101, 42)
    SetChrSubChip(0x101, 26)
    SetChrPos(0x101, -42000, 16000, 81000, 270)
    ClearChrFlags(0x2D, 0x2)
    SetChrPos(0x2D, -42780, 16000, 81000, 90)
    SetChrChipByIndex(0x2D, 33)
    SetChrSubChip(0x2D, 0)

    def lambda_5802():
        OP_6B(1500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5802)
    OP_22(0xA4, 0x0, 0x64)
    OP_96(0x101, 0xFFFF5F10, 0x3E80, 0x13C68, 0x12C, 0x1388)
    OP_96(0x101, 0xFFFF60A0, 0x3E80, 0x13C68, 0x64, 0xFA0)
    OP_99(0x101, 0x1A, 0x1D, 0x4B0)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    SetChrSubChip(0x101, 25)
    OP_0D()

    def lambda_585E():
        OP_6C(55000, 60000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_585E)

    def lambda_586E():
        OP_6B(1300, 60000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_586E)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#580F#2P刚才……！\x02\x03",
            "流进嘴里的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#591F……是即时生效的催眠药。\x01",
            "　\x02\x03",
            "没有副作用，放心吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    Sleep(250)
    FadeToBright(250, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#584F#2P啊……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 44)
    OP_22(0xD1, 0x0, 0x50)
    OP_99(0x101, 0x0, 0x3, 0x3E8)
    Sleep(1000)
    OP_99(0x101, 0x3, 0x5, 0x320)

    ChrTalk(
        0x101,
        "#584F#2P为……为什么……？\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x5, 0x7, 0x320)

    ChrTalk(
        0x101,
        "#584F#2P……为什么用那样的东西……！\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x2D,
        (
            "#594F我的艾丝蒂尔……\x01",
            "你就像太阳那样的耀眼、那样的眩目。\x02\x03",
            "和你在一起虽然很幸福、很快乐，\x01",
            "但同时，也会感到很痛苦、很无奈……\x02\x03",
            "就像强光可以产生浓重的影子一样……\x02\x03",
            "越是和你在一起的时候，\x01",
            "我就越会不由得意识到自己可憎的本性……\x01",
            "　\x02\x03",
            "所以，我有时也会想，\x01",
            "如果我们没有相遇过就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x7, 0x9, 0x320)
    Sleep(400)

    ChrTalk(
        0x101,
        "#585F#2P……怎么会………\x02",
    )

    CloseMessageWindow()

    def lambda_5B11():
        OP_6D(-41280, 16000, 81720, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B11)
    OP_8F(0x2D, 0xFFFF5BF0, 0x3E80, 0x13CCC, 0x3E8, 0x0)
    SetChrChipByIndex(0x2D, 45)
    SetChrFlags(0x2D, 0x2)
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_99(0x2D, 0x0, 0x2, 0x4B0)
    Sleep(800)

    ChrTalk(
        0x2D,
        (
            "#592F#6P不过，现在不一样了。\x02\x03",
            "我很感激能和你相遇。\x02\x03",
            "虽然，我不得不从如此珍爱的你身边逃走……\x01",
            "　\x02\x03",
            "但是，我会比任何人都更加地想念你……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x9, 0xB, 0x320)

    ChrTalk(
        0x101,
        "#585F#2P……约修亚……约修亚………\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x2D,
        (
            "#593F#6P一直以来，真的很感谢你。\x02\x03",
            "从第一次见到你的时候起……\x01",
            "我就一直深深地喜欢着你。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_99(0x2D, 0x2, 0x5, 0x4B0)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "——再见了，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0xFA0)
    OP_21()
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_6D(-89960, 14000, -12180, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(0, 0)
    OP_0D()
    OP_21()
    PlayMovie(0x0, "ed6_dt17.dat")

    label("loc_5D89")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F1C")
    Sleep(10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_5F19")
    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "")
    Sleep(500)
    OP_83(0x15, 0x0)
    OP_AD(0x4003A, 0x0, 0x0, 0xC8)
    Sleep(2000)
    OP_56(0x3)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　　　 　　 ～　关于通关存档的保存　～\x01",
            "　　 　　　　建立通关存档后，可以在标题画面中读取，\x01",
            "　　  　　　　 从而继承各项数据，开始二周目游戏。",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        170,
        100,
        0,
        (
            "【保存通关存档】\x01",      # 0
            "【放弃】\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ECB")
    SaveClearData()

    label("loc_5ECB")

    Sleep(1000)
    OP_AE(0x1F4)
    FadeToBright(0, 0)
    PlayMovie(0x0, "ed6_dt18.dat")

    label("loc_5EED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F19")
    Sleep(10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_5F16")
    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "")
    Sleep(1500)
    OP_B4(0x1)

    label("loc_5F16")

    Jump("loc_5EED")

    label("loc_5F19")

    Jump("loc_5D89")

    label("loc_5F1C")

    Return()

    # Function_18_3FAF end

    def Function_19_5F1D(): pass

    label("Function_19_5F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FC5")
    EventBegin(0x1)

    ChrTalk(
        0x8,
        (
            "哦，希尔丹夫人。\x01",
            "还有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们会好好保护陛下的。\x01",
            "请放心吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_604E")

    label("loc_5FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_604E")
    EventBegin(0x1)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        (
            "女王宫附近\x01",
            "禁止无关人等接近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "就算想见陛下\x01",
            "也是不允许的。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8C(0x8, 180, 0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_604E")

    Return()

    # Function_19_5F1D end

    SaveToFile()

Try(main)
