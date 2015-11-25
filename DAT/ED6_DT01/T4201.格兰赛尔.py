from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4201   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4201.x',
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
        '亲卫队员',                             # 46
        '亲卫队员',                             # 47
        '亲卫队员',                             # 48
        '亲卫队员',                             # 49
        '约修亚',                               # 50
        '修理员佩顿',                           # 51
        '特务艇',                               # 52
        '特务艇影子',                           # 53
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
        'ED6_DT06/CH20143 ._CH',             # 0B
        'ED6_DT07/CH00030 ._CH',             # 0C
        'ED6_DT07/CH00050 ._CH',             # 0D
        'ED6_DT07/CH00020 ._CH',             # 0E
        'ED6_DT07/CH00070 ._CH',             # 0F
        'ED6_DT07/CH00060 ._CH',             # 10
        'ED6_DT07/CH02020 ._CH',             # 11
        'ED6_DT07/CH02000 ._CH',             # 12
        'ED6_DT07/CH02060 ._CH',             # 13
        'ED6_DT06/CH20064 ._CH',             # 14
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
        'ED6_DT06/CH20127 ._CH',             # 1F
        'ED6_DT06/CH20030 ._CH',             # 20
        'ED6_DT07/CH00010 ._CH',             # 21
        'ED6_DT07/CH00441 ._CH',             # 22
        'ED6_DT06/CH20042 ._CH',             # 23
        'ED6_DT06/CH20040 ._CH',             # 24
        'ED6_DT07/CH00440 ._CH',             # 25
        'ED6_DT07/CH00340 ._CH',             # 26
        'ED6_DT07/CH00341 ._CH',             # 27
        'ED6_DT07/CH00280 ._CH',             # 28
        'ED6_DT07/CH00281 ._CH',             # 29
        'ED6_DT07/CH01330 ._CH',             # 2A
        'ED6_DT06/CH20128 ._CH',             # 2B
        'ED6_DT07/CH01450 ._CH',             # 2C
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
        'ED6_DT06/CH20143P._CP',             # 0B
        'ED6_DT07/CH00030P._CP',             # 0C
        'ED6_DT07/CH00050P._CP',             # 0D
        'ED6_DT07/CH00020P._CP',             # 0E
        'ED6_DT07/CH00070P._CP',             # 0F
        'ED6_DT07/CH00060P._CP',             # 10
        'ED6_DT07/CH02020P._CP',             # 11
        'ED6_DT07/CH02000P._CP',             # 12
        'ED6_DT07/CH02060P._CP',             # 13
        'ED6_DT06/CH20064P._CP',             # 14
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
        'ED6_DT06/CH20127P._CP',             # 1F
        'ED6_DT06/CH20030P._CP',             # 20
        'ED6_DT07/CH00010P._CP',             # 21
        'ED6_DT07/CH00441P._CP',             # 22
        'ED6_DT06/CH20042P._CP',             # 23
        'ED6_DT06/CH20040P._CP',             # 24
        'ED6_DT07/CH00440P._CP',             # 25
        'ED6_DT07/CH00340P._CP',             # 26
        'ED6_DT07/CH00341P._CP',             # 27
        'ED6_DT07/CH00280P._CP',             # 28
        'ED6_DT07/CH00281P._CP',             # 29
        'ED6_DT07/CH01330P._CP',             # 2A
        'ED6_DT06/CH20128P._CP',             # 2B
        'ED6_DT07/CH01450P._CP',             # 2C
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Unknown3            = 43,
        ChipIndex           = 0x2B,
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
        Unknown3            = 43,
        ChipIndex           = 0x2B,
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
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Unknown3            = 43,
        ChipIndex           = 0x2B,
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
        Unknown3            = 43,
        ChipIndex           = 0x2B,
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
        X                   = 1110,
        Z                   = 15350,
        Y                   = 56390,
        Direction           = 235,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -4340,
        Y                   = 19000,
        Z                   = 105990,
        Range               = 4220,
        Unknown_10          = 0x4650,
        Unknown_14          = 0x1933E,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -4280,
        Y                   = 16000,
        Z                   = 78500,
        Range               = 5010,
        Unknown_10          = 0x32C8,
        Unknown_14          = 0x1270A,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -4730,
        Y                   = 18000,
        Z                   = 98010,
        Range               = 4880,
        Unknown_10          = 0x3E80,
        Unknown_14          = 0x17534,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )

    DeclEvent(
        X                   = 32759,
        Y                   = 15500,
        Z                   = 76820,
        Range               = 35080,
        Unknown_10          = 0x4074,
        Unknown_14          = 0x116D4,
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
        "Function_0_872",          # 00, 0
        "Function_1_948",          # 01, 1
        "Function_2_B5B",          # 02, 2
        "Function_3_B71",          # 03, 3
        "Function_4_CD0",          # 04, 4
        "Function_5_F17",          # 05, 5
        "Function_6_1CD5",         # 06, 6
        "Function_7_222F",         # 07, 7
        "Function_8_2A32",         # 08, 8
        "Function_9_2F98",         # 09, 9
        "Function_10_2FC6",        # 0A, 10
        "Function_11_2FF9",        # 0B, 11
        "Function_12_302C",        # 0C, 12
        "Function_13_38FB",        # 0D, 13
        "Function_14_3C2F",        # 0E, 14
        "Function_15_3DAE",        # 0F, 15
        "Function_16_40A2",        # 10, 16
        "Function_17_461C",        # 11, 17
        "Function_18_4695",        # 12, 18
        "Function_19_5D79",        # 13, 19
    )


    def Function_0_872(): pass

    label("Function_0_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_889")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 8)

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_8A0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 12)

    label("loc_8A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_8AE")
    OP_A3(0x3FC)
    Event(0, 16)

    label("loc_8AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_8BC")
    OP_A3(0x3FD)
    Event(0, 17)

    label("loc_8BC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_8CC"),
        (101, "loc_8E2"),
        (SWITCH_DEFAULT, "loc_8F8"),
    )


    label("loc_8CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DF")
    OP_A2(0x63D)
    Event(0, 4)

    label("loc_8DF")

    Jump("loc_8F8")

    label("loc_8E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F5")
    OP_A2(0x645)
    Event(0, 7)

    label("loc_8F5")

    Jump("loc_8F8")

    label("loc_8F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_END)), "loc_909")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_91D")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_947")

    label("loc_91D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_947")
    SetChrChipByIndex(0x0, 1)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_947")

    Return()

    # Function_0_872 end

    def Function_1_948(): pass

    label("Function_1_948")

    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_965")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97A")

    label("loc_965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_97A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5A")
    OP_1B(0x0, 0x0, 0xE)
    OP_A1(0x33, 0x0)
    OP_A1(0x34, 0x1)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x2)
    OP_71(0x0, 0x400)
    OP_71(0x0, 0x40)
    OP_72(0x1, 0x4)
    OP_72(0x1, 0x2)
    OP_71(0x1, 0x400)
    OP_71(0x1, 0x40)
    SetChrPos(0x33, 2320, 12050, 57280, 56)
    SetChrPos(0x34, 2320, 12050, 57280, 56)
    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x4)
    SetChrFlags(0x32, 0x400)
    OP_6F(0x0, 360)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 1)), scpexpr(EXPR_END)), "loc_A5C")
    SetChrPos(0x8, -7920, 12000, 56580, 94)
    SetChrPos(0x9, -9260, 12000, 57540, 284)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 35)
    SetChrChipByIndex(0x9, 35)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_END)), "loc_AF3")
    SetChrPos(0xE, 3890, 14000, 79000, 146)
    SetChrPos(0xF, 3080, 14000, 77370, 283)
    SetChrPos(0x10, 6700, 14000, 78300, 358)
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 35)
    SetChrChipByIndex(0xF, 35)
    SetChrChipByIndex(0x10, 35)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0xE, 0x800)
    SetChrFlags(0xF, 0x800)
    SetChrFlags(0x10, 0x800)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_END)), "loc_B5A")
    SetChrPos(0x11, -2160, 18000, 102100, 309)
    SetChrPos(0x12, 2230, 18000, 101600, 82)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x11, 0x1)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x11, 0x800)
    SetChrFlags(0x12, 0x800)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 35)
    SetChrChipByIndex(0x12, 35)

    label("loc_B5A")

    Return()

    # Function_1_948 end

    def Function_2_B5B(): pass

    label("Function_2_B5B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B70")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_B5B")

    label("loc_B70")

    Return()

    # Function_2_B5B end

    def Function_3_B71(): pass

    label("Function_3_B71")

    TalkBegin(0x32)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "购买道具\x01",        # 2
            "离开\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE0")
    OP_0D()
    OP_A9(0x6C)
    OP_56(0x0)
    TalkEnd(0x32)
    Return()

    label("loc_BE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF9")
    OP_0D()
    OP_A9(0x6D)
    OP_56(0x0)
    TalkEnd(0x32)
    Return()

    label("loc_BF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0A")
    TalkEnd(0x32)
    Return()

    label("loc_C0A")


    ChrTalk(
        0x32,
        (
            "我带了一些可以调整大家的\x01",
            "导力器的工具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "还有，我也准备了一些装备和道具，\x01",
            "虽然种类不算很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        "有需要的话请说一声。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x32)
    Return()

    # Function_3_B71 end

    def Function_4_CD0(): pass

    label("Function_4_CD0")

    EventBegin(0x0)
    OP_6D(31020, 10750, 79090, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 29890, 10750, 79270, 0)
    SetChrPos(0x102, 31020, 10750, 79090, 0)

    def lambda_D37():
        OP_8E(0xFE, 0x6CB6, 0x2EE0, 0x172E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D37)

    def lambda_D52():
        OP_8E(0xFE, 0x722E, 0x2EE0, 0x1730E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D52)

    def lambda_D6D():
        OP_6D(29660, 12000, 100020, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D6D)

    def lambda_D85():
        OP_67(0, 5000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D85)

    def lambda_D9D():
        OP_6C(12000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D9D)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#000F哇啊～……好美……\x02\x03",
            "这里就是王城的空中庭园啊……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F是啊……湖面一览无余，\x01",
            "还可以俯瞰格兰赛尔周围的城邑。\x02\x03",
            "想来参观的人肯定很多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呼～如果不是处于这种时刻，\x01",
            "本可以好好欣赏这里的景色的……\x02\x03",
            "现在还是优先完成任务吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_4_CD0 end

    def Function_5_F17(): pass

    label("Function_5_F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_END)), "loc_F1F")
    Return()

    label("loc_F1F")

    OP_A2(0x63E)
    OP_28(0x49, 0x1, 0x400)
    EventBegin(0x0)
    OP_8C(0x101, 0, 0)
    OP_8C(0x102, 0, 0)

    ChrTalk(
        0x101,
        "#000F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F看来这里就是女王宫了……\x02",
    )

    CloseMessageWindow()

    def lambda_F77():
        OP_8E(0xFE, 0xFFFFFCAE, 0x4650, 0x19438, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F77)

    def lambda_F92():
        OP_8E(0xFE, 0x438, 0x4650, 0x194BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F92)
    OP_6D(0, 20000, 107640, 3000)
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

    ChrTalk(
        0x101,
        (
            "#000F啊……\x02\x03",
            "我们俩是公爵\x01",
            "邀请的客人……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F这里就是陛下居住的\x01",
            "女王宫对吗？\x02",
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
            "#000F讨、讨厌啦～\x01",
            "没有想到陛下会身体不适呢。\x02\x03",
            "这么说来，可得\x01",
            "小心照料～才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，科洛蒂娅公主\x01",
            "也在里面吗？\x02",
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
            "哦哦，公主正在细心的\x01",
            "看护着陛下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "当然也就没有空\x01",
            " \x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, 280, 20000, 111970, 0)

    ChrTalk(
        0xA,
        (
            "……你们在那里\x01",
            "做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)

    def lambda_12BC():
        OP_8E(0xFE, 0x82, 0x4C2C, 0x1A13A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_12BC)

    def lambda_12D7():

        label("loc_12D7")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_12D7")

    QueueWorkItem2(0x8, 1, lambda_12D7)

    def lambda_12E8():
        OP_8E(0xFE, 0xFFFFF9FC, 0x4D26, 0x1A22A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_12E8)

    def lambda_1303():

        label("loc_1303")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1303")

    QueueWorkItem2(0x9, 1, lambda_1303)

    def lambda_1314():
        OP_8E(0xFE, 0xFFFFFA24, 0x4B32, 0x19EEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1314)
    WaitChrThread(0xA, 0x2)

    ChrTalk(
        0x8,
        "夫人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "您这就要回去了吗？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x2)

    ChrTalk(
        0xA,
        (
            "#710F很快晚宴就要开始了，\x01",
            "我得暂且先回休息室去。\x02\x03",
            "对了，这两位客人是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "武术大会优胜组的成员。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "只不过是些游击士罢了，\x01",
            "但也还算是邀请的客人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哼，什么叫只不过是游击士……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(
        0xA,
        "没礼貌的东西！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你这就等于是在侮辱\x01",
            "王城邀请的客人！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x8,
        "不……我们不是那个意思……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "虽说是由公爵大人邀请而来的，\x01",
            "但只要是王城的来访者，就是陛下的客人！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这一点是绝对不能忘记的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "明、明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（好、好惊人的气势……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（难道这个人就是……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "可是夫人……\x01",
            "他们要想进去是肯定不行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这一点上校是说清楚了的，\x01",
            "您也应该很明白的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "……这个我已经听烦了。\x02",
    )

    CloseMessageWindow()
    OP_8E(0xA, 0x8C, 0x493E, 0x19C12, 0x7D0, 0x0)

    ChrTalk(
        0xA,
        "非常抱歉，客人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "因为加强戒备的缘故，\x01",
            "所以接近女王宫是被禁止的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "如果可以的话，晚宴开始之前\x01",
            "请在房间里等候好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊……好、好的。\x02",
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

    ChrTalk(
        0x102,
        (
            "#010F劳您费心了。\x01",
            "我们带来了不少麻烦。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "哼……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "知道就好，人要知趣。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(
        0xA,
        "……………………（怒视）\x02",
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
    SetChrPos(0x101, -620, 15500, 86640, 180)
    SetChrPos(0x102, 1430, 15500, 86590, 180)
    SetChrPos(0xA, 310, 15000, 85930, 180)

    def lambda_197B():

        label("loc_197B")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_197B")

    QueueWorkItem2(0x101, 1, lambda_197B)

    def lambda_198C():

        label("loc_198C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_198C")

    QueueWorkItem2(0x102, 1, lambda_198C)

    def lambda_199D():
        OP_8E(0xFE, 0xFFFFFF24, 0x36B0, 0x139A2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_199D)

    def lambda_19B8():
        OP_8E(0xFE, 0xFFFFFC72, 0x36B0, 0x13D4E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19B8)

    def lambda_19D3():
        OP_8E(0xFE, 0x1EA, 0x36B0, 0x13EAC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_19D3)

    def lambda_19EE():
        OP_6D(-90, 14000, 81270, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19EE)
    WaitChrThread(0xA, 0x1)
    OP_8C(0xA, 0, 400)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0xA,
        (
            "……他们做出那样丢脸的事，\x01",
            "让你们见笑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "请允许我先自我介绍一下。\x01",
            "我的名字叫希尔丹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我是这个格兰赛尔城的女管家，\x01",
            "主要就是监督侍女们工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F果然是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来您就是\x01",
            "希尔丹夫人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#710F哦……\x02\x03",
            "对不起，请问\x01",
            "我们曾经认识吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊……\x01",
            "是从别人那里听说的。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0xA, 0x258, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "尤莉亚的介绍信\x01",
            "交出了给了希尔丹夫人。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x101, 0xFFFFFC72, 0x36B0, 0x13D4E, 0x7D0, 0x0)

    ChrTalk(
        0xA,
        "#710F这个笔迹是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，凭那个笔迹就可以判断是谁写的了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这封介绍信以及游击士徽章\x01",
            "就是我们身份的证明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#710F我明白了……\x02\x03",
            "在这儿不太方便，\x01",
            "先回侍女们的休息室吧。\x02\x03",
            "到那里再向你们请教详细的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4214   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_F17 end

    def Function_6_1CD5(): pass

    label("Function_6_1CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CE2")
    Return()

    label("loc_1CE2")

    OP_A2(0x643)
    OP_28(0x4A, 0x1, 0x80)
    EventBegin(0x0)
    Fade(1000)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x138, 1)
    SetChrPos(0x138, 10, 18500, 104830, 0)
    SetChrPos(0x101, -470, 18000, 103350, 0)
    SetChrPos(0x102, 740, 18000, 103280, 0)
    OP_6D(-70, 19000, 105810, 3000)

    ChrTalk(
        0x8,
        "希尔丹夫人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这么晚了\x01",
            "找陛下还有社么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F我把陛下吩咐过的红茶\x01",
            "和一些食品带来了。\x02\x03",
            "在这样的事态下，\x01",
            "陛下竟然也被如此\x01",
            "的限制了自由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "很严格啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "以前没有见过的生面孔啊，\x01",
            "那边的是侍女吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F遵照公爵大人的命令补充的\x01",
            "新来的实习侍女。\x02\x03",
            "今天才进入城里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔～唔，\x01",
            "的确好可爱哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F你、你们好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F…………………（点头示意）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哎呀……？\x02",
    )

    CloseMessageWindow()
    OP_90(0x8, 0x0, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)

    ChrTalk(
        0x8,
        (
            "怎么总觉得\x01",
            "在哪儿见过呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 800)

    ChrTalk(
        0x101,
        "#000F（不好……！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F……对年轻的姑娘那样\x01",
            "目不转睛的盯着是什么意思。\x02\x03",
            "难不成是在\x01",
            "动一些歪念头吗？\x02\x03",
            "在这样下去我可要向公爵大人\x01",
            "还有上校抗议了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20B3():
        OP_8C(0xFE, 0, 200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20B3)

    ChrTalk(
        0x8,
        "不、不要这样！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "作为王国军精英\x01",
            "的我们怎么会那样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F没有最好。\x02\x03",
            "我说，你们好了没有，\x01",
            "可以让我们进去了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "刚才对不起！\x02",
    )

    CloseMessageWindow()

    def lambda_217A():
        OP_8F(0xFE, 0xFFFFF704, 0x4C2C, 0x1A194, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_217A)

    ChrTalk(
        0x9,
        "请进去吧！\x02",
    )

    CloseMessageWindow()

    def lambda_21AC():
        OP_8F(0xFE, 0x92E, 0x4C2C, 0x1A13A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_21AC)
    FadeToDark(2000, 0, -1)

    def lambda_21D1():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_21D1)
    Sleep(50)

    def lambda_21F1():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21F1)

    def lambda_220C():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_220C)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4230   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1CD5 end

    def Function_7_222F(): pass

    label("Function_7_222F")

    EventBegin(0x0)
    OP_6D(-220, 20000, 107550, 0)
    SetChrPos(0x8, -2390, 19500, 107000, 180)
    SetChrPos(0x9, 2290, 19500, 106980, 180)

    def lambda_226A():

        label("loc_226A")

        TurnDirection(0xFE, 0x138, 0)
        OP_48()
        Jump("loc_226A")

    QueueWorkItem2(0x8, 2, lambda_226A)

    def lambda_227B():

        label("loc_227B")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_227B")

    QueueWorkItem2(0x9, 2, lambda_227B)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x138, 1)
    SetChrPos(0x101, -990, 20000, 110860, 180)
    SetChrPos(0x102, 1070, 20000, 111050, 0)
    SetChrPos(0x138, 120, 20000, 110230, 180)

    def lambda_22CE():
        OP_8E(0xFE, 0xBE, 0x4B32, 0x19F64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_22CE)

    def lambda_22E9():
        OP_8E(0xFE, 0xFFFFFE20, 0x4D26, 0x1A310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22E9)

    def lambda_2304():
        OP_8E(0xFE, 0x35C, 0x4D26, 0x1A310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2304)
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
            "我希望你们\x01",
            "在陛下面前不要有什么闪失。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "很严格啊……\x02",
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
            "#710F那就没有什么再要拜托的了。\x02\x03",
            "那么我们\x01",
            "这就告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        "#000F再、再－见……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 135, 400)

    ChrTalk(
        0x102,
        "#010F……告辞了。\x02",
    )

    CloseMessageWindow()

    def lambda_2491():
        OP_6D(230, 19000, 105820, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2491)

    def lambda_24A9():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_24A9)
    Sleep(100)

    def lambda_24C9():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24C9)

    def lambda_24E4():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24E4)

    def lambda_24FF():
        OP_8F(0xFE, 0xFFFFFC9A, 0x4D26, 0x1A388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_24FF)

    def lambda_251A():
        OP_8F(0xFE, 0x38E, 0x4D26, 0x1A388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_251A)
    Sleep(1300)

    ChrTalk(
        0x8,
        "啊，两位姑娘。\x02",
    )

    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    CloseMessageWindow()

    def lambda_2590():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_2590)

    def lambda_259E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_259E)
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "突然想起还没有询问\x01",
            "你们的名字。\x02",
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
        "#000F嗯，这个……\x02",
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
            "莱娜\x01",        # 0
            "雪拉\x01",        # 1
            "朵洛希\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_267D"),
        (1, "loc_26F7"),
        (2, "loc_27D7"),
        (SWITCH_DEFAULT, "loc_286B"),
    )


    label("loc_267D")

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
            "#000F啊，那个……\x01",
            "真是非常感谢啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_286B")

    label("loc_26F7")

    OP_A2(0x677)

    ChrTalk(
        0x8,
        (
            "哦，是个\x01",
            "不怎么样的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "失败就失败在名字上了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F少、少管闲事！\x02\x03",
            "……好吗，呵呵呵。\x02\x03",
            "我会努力做一个好女人的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_286B")

    label("loc_27D7")

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
            "可说实话，感觉和你\x01",
            "不是很般配……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（也许是吧……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_286B")

    label("loc_286B")


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
        "#010F……我的名字叫做卡玲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "叫卡玲……\x01",
            "好可爱的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F谢谢。\x02\x03",
            "……我对自己的名字\x01",
            "也非常喜欢呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "对、对了。\x01",
            "我是特务部队的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F你还明白这一点。\x02\x03",
            "这一切\x01",
            "就是因为居心不良。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不、我可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#710F……………………（怒视）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……请吧，\x01",
            "这就请回吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    SetChrChipByIndex(0x0, 1)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    Return()

    # Function_7_222F end

    def Function_8_2A32(): pass

    label("Function_8_2A32")

    EventBegin(0x0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_6F(0x2, 450)
    OP_72(0x2, 0x10)
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
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0x9, 0x1)
    SetChrPos(0xB, 20, 12000, 46990, 180)
    SetChrPos(0x8, 940, 12000, 48110, 180)
    SetChrPos(0x9, -900, 12000, 48110, 180)
    SetChrChipByIndex(0x8, 42)
    SetChrChipByIndex(0x9, 42)
    SetChrPos(0xC, -60, 12000, 51430, 180)
    SetChrPos(0xD, 930, 12000, 52730, 180)
    SetChrPos(0xE, 930, 12000, 54640, 180)
    SetChrPos(0xF, 910, 12000, 56310, 180)
    SetChrPos(0x10, -890, 12000, 52760, 180)
    SetChrPos(0x11, -890, 12000, 54510, 180)
    SetChrPos(0x12, -890, 12000, 56510, 180)
    SetChrFlags(0x32, 0x80)
    OP_6D(-1980, 12000, 40200, 0)
    OP_67(0, 4910, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(51000, 0)
    OP_6E(280, 0)
    OP_6D(10, 12000, 46910, 2000)

    ChrTalk(
        0xB,
        (
            "#187F#5P这、这怎么可能……！\x01",
            "为什么城门会自动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P上、上尉！\x01",
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

    def lambda_2C41():
        OP_6D(-10, 12000, 48330, 800)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2C41)
    OP_8C(0xB, 0, 600)
    WaitChrThread(0xB, 0x2)

    ChrTalk(
        0xB,
        (
            "#185F#2P第一小队留下，\x01",
            "其余的立刻赶往大门！\x02\x03",
            "绝对不能让敌人冲进城内！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P明、明白！！\x02",
    )

    CloseMessageWindow()

    def lambda_2CE9():

        label("loc_2CE9")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2CE9")

    QueueWorkItem2(0xD, 1, lambda_2CE9)

    def lambda_2CFA():

        label("loc_2CFA")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2CFA")

    QueueWorkItem2(0xE, 1, lambda_2CFA)

    def lambda_2D0B():

        label("loc_2D0B")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2D0B")

    QueueWorkItem2(0xF, 1, lambda_2D0B)

    def lambda_2D1C():

        label("loc_2D1C")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2D1C")

    QueueWorkItem2(0x10, 1, lambda_2D1C)

    def lambda_2D2D():

        label("loc_2D2D")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2D2D")

    QueueWorkItem2(0x11, 1, lambda_2D2D)

    def lambda_2D3E():

        label("loc_2D3E")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2D3E")

    QueueWorkItem2(0x12, 1, lambda_2D3E)
    SetChrChipByIndex(0xC, 34)
    OP_8E(0xC, 0x906, 0x2EE0, 0xC936, 0x1770, 0x0)
    OP_8E(0xC, 0x906, 0x2EE0, 0xCDC8, 0x1770, 0x0)
    OP_43(0xD, 0x1, 0x0, 0x9)
    OP_43(0x10, 0x1, 0x0, 0x9)
    OP_8E(0xC, 0x906, 0x2EE0, 0xD476, 0x1770, 0x0)
    OP_43(0xE, 0x1, 0x0, 0xA)
    OP_43(0x11, 0x1, 0x0, 0xA)
    OP_8E(0xC, 0x906, 0x2EE0, 0xDF66, 0x1770, 0x0)
    OP_43(0xF, 0x1, 0x0, 0xB)
    OP_43(0x12, 0x1, 0x0, 0xB)

    def lambda_2DCE():
        OP_8E(0xFE, 0x92E, 0x2EE0, 0x11FE4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2DCE)
    OP_6D(10, 12000, 46910, 1000)

    ChrTalk(
        0xB,
        (
            "#186F#2P可恶，太丢脸了……\x02\x03",
            "在上校回来之前，\x01",
            "无论如何也不能让那些人得逞……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "#5P上、上尉！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P是、是特务飞艇！\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0xB, 180, 600)

    ChrTalk(
        0xB,
        (
            "#187F#5P糟糕了！\x01",
            "那个才是主力部队吗！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F44():
        OP_6D(-9190, 19050, 36880, 1500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2F44)

    def lambda_2F5C():
        OP_67(0, 3900, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2F5C)

    def lambda_2F74():
        OP_6B(3220, 1500)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_2F74)
    Sleep(1000)
    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/E0500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2A32 end

    def Function_9_2F98(): pass

    label("Function_9_2F98")

    SetChrChipByIndex(0xFE, 34)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0xCD96, 0x1770, 0x0)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0x11FE4, 0x1770, 0x0)
    Return()

    # Function_9_2F98 end

    def Function_10_2FC6(): pass

    label("Function_10_2FC6")

    Sleep(800)
    SetChrChipByIndex(0xFE, 34)
    OP_8E(0xFE, 0x8F2, 0x2EE0, 0xD462, 0x1770, 0x0)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0x11FE4, 0x1770, 0x0)
    Return()

    # Function_10_2FC6 end

    def Function_11_2FF9(): pass

    label("Function_11_2FF9")

    Sleep(1300)
    SetChrChipByIndex(0xFE, 34)
    OP_8E(0xFE, 0x8F2, 0x2EE0, 0xDBC4, 0x1388, 0x0)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0x11FE4, 0x1388, 0x0)
    Return()

    # Function_11_2FF9 end

    def Function_12_302C(): pass

    label("Function_12_302C")

    EventBegin(0x0)
    SetChrFlags(0x32, 0x80)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x0, 0xFF)
    AddParty(0x4, 0xFF)
    AddParty(0x2, 0xFF)
    OP_6D(1980, 20950, 57340, 0)
    OP_67(0, 9340, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(340000, 0)
    OP_6E(413, 0)
    SetChrPos(0x8, -8810, 12000, 57910, 79)
    SetChrPos(0xB, -7640, 12000, 58590, 125)
    SetChrPos(0x9, -6650, 12000, 57720, 46)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0x9, 0x1)

    def lambda_30D4():

        label("loc_30D4")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_30D4")

    QueueWorkItem2(0xB, 1, lambda_30D4)

    def lambda_30E5():

        label("loc_30E5")

        TurnDirection(0xFE, 0x103, 0)
        OP_48()
        Jump("loc_30E5")

    QueueWorkItem2(0x8, 1, lambda_30E5)

    def lambda_30F6():

        label("loc_30F6")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_30F6")

    QueueWorkItem2(0x9, 1, lambda_30F6)
    SetChrChipByIndex(0xB, 40)
    SetChrChipByIndex(0x8, 38)
    SetChrChipByIndex(0x9, 38)
    OP_A1(0x33, 0x0)
    OP_A1(0x34, 0x1)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x2)
    OP_71(0x0, 0x400)
    OP_71(0x0, 0x40)
    OP_72(0x1, 0x4)
    OP_72(0x1, 0x2)
    OP_71(0x1, 0x400)
    OP_71(0x1, 0x40)
    OP_6F(0x0, 1021)
    SetChrFlags(0x33, 0x4)
    SetChrFlags(0x34, 0x4)
    SetChrFlags(0x33, 0x40)
    SetChrFlags(0x34, 0x40)
    SetChrPos(0x101, 2880, 15350, 57740, 147)
    SetChrPos(0x103, 2880, 15350, 57740, 147)
    SetChrPos(0x105, 2880, 15350, 57740, 147)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x105, 0x80)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    SetChrPos(0x33, 2320, 22050, 57280, 56)
    SetChrPos(0x34, 2320, 12050, 57280, 56)

    def lambda_31DB():
        OP_6D(610, 15350, 55470, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_31DB)

    def lambda_31F3():
        OP_67(0, 5210, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_31F3)

    def lambda_320B():
        OP_6C(29000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_320B)
    FadeToBright(2000, 0)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 1110)
    OP_22(0xCC, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x34, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0x33, 0x0, 0xFFFFF448, 0x0, 0xBB8, 0x0)
    OP_91(0x33, 0x0, 0xFFFFF830, 0x0, 0x9C4, 0x0)
    OP_91(0x33, 0x0, 0xFFFFFC18, 0x0, 0x7D0, 0x0)
    PlayEffect(0x1, 0x2, 0x34, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_91(0x33, 0x0, 0xFFFFF830, 0x0, 0x7D0, 0x0)
    OP_91(0x33, 0x0, 0xFFFFFC18, 0x0, 0x5DC, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_8F(0x33, 0x910, 0x2F12, 0xDFC0, 0x3E8, 0x0)
    OP_22(0xC8, 0x0, 0x64)
    OP_23(0x79)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x105, 9)

    def lambda_3345():
        OP_67(0, 7370, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_3345)
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0x0, 0x78)
    OP_6F(0x0, 61)
    OP_70(0x0, 0xE6)
    OP_73(0x0)
    OP_B0(0x0, 0x3C)
    OP_6F(0x0, 231)
    OP_70(0x0, 0x168)
    OP_73(0x0)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x0, 1140)
    OP_70(0x0, 0x4B0)
    OP_73(0x0)

    def lambda_33A2():

        label("loc_33A2")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_33A2")

    QueueWorkItem2(0x101, 1, lambda_33A2)

    def lambda_33B3():

        label("loc_33B3")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_33B3")

    QueueWorkItem2(0x105, 1, lambda_33B3)

    def lambda_33C4():

        label("loc_33C4")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_33C4")

    QueueWorkItem2(0x103, 1, lambda_33C4)

    def lambda_33D5():
        OP_6D(-7140, 12000, 55690, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_33D5)

    def lambda_33ED():
        OP_6E(577, 3000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_33ED)

    def lambda_33FD():
        OP_67(0, 5360, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_33FD)

    def lambda_3415():
        OP_6C(13000, 3000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3415)

    def lambda_3425():
        OP_6B(1600, 3000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_3425)
    ClearChrFlags(0x101, 0x80)

    def lambda_343A():
        OP_8E(0xFE, 0xFFFFECB4, 0x31A6, 0xD00C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_343A)
    Sleep(300)
    ClearChrFlags(0x103, 0x80)

    def lambda_345F():
        OP_8E(0xFE, 0xFFFFE3C2, 0x2EE0, 0xC8F0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_345F)
    Sleep(300)
    ClearChrFlags(0x105, 0x80)

    def lambda_3484():
        OP_8E(0xFE, 0xFFFFE912, 0x2EE0, 0xCB52, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3484)
    WaitChrThread(0x101, 0x2)

    def lambda_34A4():
        OP_96(0xFE, 0xFFFFE480, 0x2EE0, 0xCDDC, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34A4)
    WaitChrThread(0x103, 0x2)

    def lambda_34C7():
        OP_8E(0xFE, 0xFFFFDE7C, 0x2EE0, 0xCD00, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_34C7)
    WaitChrThread(0x105, 0x2)

    def lambda_34E7():
        OP_8E(0xFE, 0xFFFFE16A, 0x2EE0, 0xC8E6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_34E7)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0xB,
        (
            "#187F艾、艾丝蒂尔·布莱特！？\x02\x03",
            "还有……科洛蒂娅殿下！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F凯诺娜上尉！又来麻烦你了哦！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F我们是来……\x01",
            "营救我的祖母大人的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#186F不、不要欺人太甚了，小丫头！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 6)

    def lambda_35CD():
        OP_92(0xFE, 0x9, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35CD)
    Sleep(10)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x103, 8)

    def lambda_35F1():
        OP_92(0xFE, 0x8, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_35F1)
    Sleep(10)
    SetChrFlags(0x105, 0x1000)
    SetChrChipByIndex(0x105, 10)

    def lambda_3615():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3615)
    Sleep(20)
    SetChrChipByIndex(0x8, 39)

    def lambda_3634():
        OP_92(0xFE, 0x103, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3634)
    Sleep(10)
    SetChrChipByIndex(0x9, 39)

    def lambda_3653():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3653)
    Sleep(10)
    SetChrChipByIndex(0xB, 41)

    def lambda_3672():
        OP_92(0xFE, 0x105, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3672)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x103, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    Battle(0x3A8, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_36C6"),
        (SWITCH_DEFAULT, "loc_36C9"),
    )


    label("loc_36C6")

    OP_B4(0x0)
    Return()

    label("loc_36C9")

    EventBegin(0x0)
    OP_6D(-6850, 12000, 58770, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0xB, -7520, 12000, 58240, 12)
    SetChrPos(0x8, -7920, 12000, 56580, 94)
    SetChrPos(0x9, -9260, 12000, 57540, 284)
    SetChrPos(0x101, -5430, 12000, 58450, 270)
    SetChrPos(0x103, -5750, 12000, 60040, 225)
    SetChrPos(0x105, -4860, 12000, 59500, 270)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
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
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#023F真令人毛骨悚然……\x01",
            "好一个可怕的女人啊。\x02\x03",
            "她究竟是谁？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F理查德上校的副官。\x02\x03",
            "是只典型的母狐狸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F原来如此，可以感觉出来。\x02\x03",
            "#020F接下来……目标女王宫！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#042F好的，赶快走吧！\x02",
    )

    CloseMessageWindow()
    OP_28(0x4E, 0x1, 0x2)
    ClearChrFlags(0x32, 0x80)
    OP_6F(0x0, 360)
    EventEnd(0x0)
    Return()

    # Function_12_302C end

    def Function_13_38FB(): pass

    label("Function_13_38FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3908")
    Return()

    label("loc_3908")

    EventBegin(0x0)
    OP_A2(0x662)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xE, 13020, 14000, 78670, 270)
    SetChrPos(0xF, 14450, 14000, 79840, 270)
    SetChrPos(0x10, 14130, 14000, 77880, 270)
    SetChrChipByIndex(0xE, 38)
    SetChrChipByIndex(0xF, 37)
    SetChrChipByIndex(0x10, 37)

    ChrTalk(
        0xE,
        "#3P来了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#3P在那儿！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 1230, 14000, 77770, 90)
    SetChrPos(0x103, -420, 14000, 78370, 90)
    SetChrPos(0x105, -300, 14000, 77020, 90)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x105, 9)
    OP_6D(6360, 14000, 78900, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#004F#5P哇，又来了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#024F#5P哼，装腔作势的家伙！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 39)
    SetChrChipByIndex(0xF, 34)
    SetChrChipByIndex(0x10, 34)

    def lambda_3A58():
        OP_6D(8500, 14000, 78900, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A58)

    def lambda_3A70():
        OP_92(0xFE, 0xE, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A70)
    Sleep(10)

    def lambda_3A8A():
        OP_92(0xFE, 0x10, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A8A)
    Sleep(10)

    def lambda_3AA4():
        OP_92(0xFE, 0xF, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AA4)
    Sleep(20)

    def lambda_3ABE():
        OP_8E(0xFE, 0xFFFFAFD8, 0x36B0, 0x130EC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3ABE)
    Sleep(10)

    def lambda_3ADE():
        OP_8E(0xFE, 0xFFFFAFD8, 0x36B0, 0x130EC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3ADE)
    Sleep(10)

    def lambda_3AFE():
        OP_8E(0xFE, 0xFFFFAFD8, 0x36B0, 0x130EC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3AFE)
    Sleep(500)
    Battle(0x3B1, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_3B31"),
        (SWITCH_DEFAULT, "loc_3B34"),
    )


    label("loc_3B31")

    OP_B4(0x0)
    Return()

    label("loc_3B34")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrPos(0x101, 1780, 14000, 78680, 90)
    SetChrPos(0x103, 1780, 14000, 78680, 90)
    SetChrPos(0x105, 1780, 14000, 78680, 90)
    OP_6D(1780, 14000, 78680, 0)
    SetChrPos(0xE, 3890, 14000, 79000, 146)
    SetChrPos(0xF, 3080, 14000, 77370, 283)
    SetChrPos(0x10, 6700, 14000, 78300, 358)
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 35)
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 35)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 35)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0xE, 0x800)
    SetChrFlags(0xF, 0x800)
    SetChrFlags(0x10, 0x800)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_13_38FB end

    def Function_14_3C2F(): pass

    label("Function_14_3C2F")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CAE")
    OP_8C(0x101, 180, 0)
    TurnDirection(0x105, 0x101, 0)
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(
        0x105,
        (
            "#043F艾丝蒂尔！\x01",
            "这边是去城内的路！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#022F我们要赶快去女王宫！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D92")

    label("loc_3CAE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D0E")
    OP_8C(0x105, 180, 0)
    TurnDirection(0x101, 0x105, 0)
    TurnDirection(0x103, 0x105, 0)

    ChrTalk(
        0x105,
        (
            "#042F不行……！\x01",
            "必须赶快去女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D92")

    label("loc_3D0E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D92")
    OP_8C(0x103, 180, 0)
    TurnDirection(0x101, 0x103, 0)
    TurnDirection(0x105, 0x103, 0)

    ChrTalk(
        0x103,
        (
            "#023F哎呀，\x01",
            "这边不是女王宫！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F嗯，在北边的高台上！\x02",
    )

    CloseMessageWindow()

    label("loc_3D92")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_14_3C2F end

    def Function_15_3DAE(): pass

    label("Function_15_3DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DBB")
    Return()

    label("loc_3DBB")

    EventBegin(0x0)
    OP_A2(0x664)
    Fade(1000)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -870, 19000, 105680, 180)
    SetChrPos(0x12, 850, 19000, 105680, 180)
    SetChrChipByIndex(0x11, 37)
    SetChrChipByIndex(0x12, 37)
    SetChrPos(0x101, 100, 17250, 98200, 0)
    SetChrPos(0x103, -1300, 17000, 97610, 0)
    SetChrPos(0x105, 1670, 17000, 97720, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x105, 9)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x103, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    OP_6D(290, 18000, 103070, 0)
    OP_67(0, 7390, -10000, 0)
    OP_6B(2280, 0)
    OP_6C(30000, 0)
    OP_6E(420, 0)
    OP_0D()

    ChrTalk(
        0x11,
        "来、来了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "此路不通！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F#2P可是……\x01",
            "我们必须要通过这里！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#2P再阻拦的话就把你们打飞！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F17():
        OP_6D(360, 18750, 105100, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F17)

    def lambda_3F2F():
        OP_8E(0xFE, 0xFFFFFECA, 0x4B32, 0x1F676, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F2F)
    Sleep(50)

    def lambda_3F4F():
        OP_8E(0xFE, 0xFFFFFECA, 0x4B32, 0x1F676, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3F4F)
    Sleep(50)

    def lambda_3F6F():
        OP_8E(0xFE, 0xFFFFFECA, 0x4B32, 0x1F676, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3F6F)
    Sleep(500)
    Battle(0x3B2, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_3FA2"),
        (SWITCH_DEFAULT, "loc_3FA5"),
    )


    label("loc_3FA2")

    OP_B4(0x0)
    Return()

    label("loc_3FA5")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    SetChrPos(0x11, -2160, 18000, 102100, 309)
    SetChrPos(0x12, 2230, 18000, 101600, 82)
    ClearChrFlags(0x11, 0x1)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x11, 0x800)
    SetChrFlags(0x12, 0x800)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 35)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 35)
    SetChrPos(0x101, -90, 18000, 102000, 0)
    SetChrPos(0x103, -90, 18000, 102000, 0)
    SetChrPos(0x105, -90, 18000, 102000, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)
    OP_6D(-90, 18000, 102000, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_15_3DAE end

    def Function_16_40A2(): pass

    label("Function_16_40A2")

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
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    SetChrPos(0x14, -7210, 12000, 58180, 0)
    SetChrPos(0x15, -9680, 12000, 54680, 0)
    SetChrPos(0x16, -7920, 12000, 56380, 0)
    SetChrPos(0x17, -10390, 12000, 56310, 0)
    SetChrPos(0x18, 6170, 12000, 53150, 0)
    SetChrPos(0x19, 6210, 12000, 53870, 0)
    SetChrPos(0x1A, -7990, 12000, 54100, 0)
    SetChrPos(0x1B, -7550, 12000, 49770, 0)
    SetChrPos(0x1C, -6470, 12000, 48980, 0)
    SetChrPos(0x1D, -1110, 12000, 70820, 0)
    SetChrPos(0x1E, 1020, 12000, 70710, 0)
    SetChrPos(0x1F, 10, 12000, 71740, 0)
    SetChrPos(0x20, 20, 12000, 67080, 0)
    SetChrPos(0x13, 650, 12000, 68820, 0)
    SetChrPos(0x21, 6760, 12000, 57310, 0)
    SetChrPos(0x22, 5980, 12000, 57880, 0)
    SetChrPos(0x23, 7530, 12000, 55190, 0)
    SetChrPos(0x24, 6470, 12000, 55570, 0)
    SetChrPos(0x25, 9010, 12000, 57270, 0)
    SetChrPos(0x26, 9250, 12000, 55950, 0)
    SetChrPos(0x27, -2750, 12000, 62800, 90)
    SetChrPos(0x28, -2750, 12000, 61200, 90)
    SetChrPos(0x29, -2750, 12000, 59600, 90)
    SetChrPos(0x2A, -2750, 12000, 58000, 90)
    SetChrPos(0x2B, -2750, 12000, 56400, 90)
    SetChrPos(0x2C, 2750, 12000, 62800, 270)
    SetChrPos(0x2D, 2750, 12000, 61200, 270)
    SetChrPos(0x2E, 2750, 12000, 59600, 270)
    SetChrPos(0x2F, 2750, 12000, 58000, 270)
    SetChrPos(0x30, 2750, 12000, 56400, 270)

    def lambda_43B8():

        label("loc_43B8")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_43B8")

    QueueWorkItem2(0x2A, 0, lambda_43B8)

    def lambda_43CB():

        label("loc_43CB")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_43CB")

    QueueWorkItem2(0x2B, 0, lambda_43CB)

    def lambda_43DE():

        label("loc_43DE")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_43DE")

    QueueWorkItem2(0x2F, 0, lambda_43DE)

    def lambda_43F1():

        label("loc_43F1")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_43F1")

    QueueWorkItem2(0x30, 0, lambda_43F1)

    def lambda_4404():
        OP_8E(0xFE, 0xFFFFFBAA, 0x2EE0, 0xD23C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_4404)

    def lambda_441F():
        OP_8E(0xFE, 0x3FC, 0x2EE0, 0xD1CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_441F)

    def lambda_443A():
        OP_8E(0xFE, 0xA, 0x2EE0, 0xD5D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_443A)

    def lambda_4455():
        OP_8E(0xFE, 0x14, 0x2EE0, 0xC3A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4455)

    def lambda_4470():
        OP_8E(0xFE, 0x28A, 0x2EE0, 0xCA6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4470)

    def lambda_448B():

        label("loc_448B")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_448B")

    QueueWorkItem2(0x101, 1, lambda_448B)

    def lambda_449C():

        label("loc_449C")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_449C")

    QueueWorkItem2(0x102, 1, lambda_449C)

    def lambda_44AD():

        label("loc_44AD")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_44AD")

    QueueWorkItem2(0x14, 1, lambda_44AD)

    def lambda_44BE():

        label("loc_44BE")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_44BE")

    QueueWorkItem2(0x15, 1, lambda_44BE)

    def lambda_44CF():

        label("loc_44CF")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_44CF")

    QueueWorkItem2(0x16, 1, lambda_44CF)

    def lambda_44E0():

        label("loc_44E0")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_44E0")

    QueueWorkItem2(0x17, 1, lambda_44E0)

    def lambda_44F1():

        label("loc_44F1")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_44F1")

    QueueWorkItem2(0x18, 1, lambda_44F1)

    def lambda_4502():

        label("loc_4502")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4502")

    QueueWorkItem2(0x19, 1, lambda_4502)

    def lambda_4513():

        label("loc_4513")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4513")

    QueueWorkItem2(0x1A, 1, lambda_4513)

    def lambda_4524():

        label("loc_4524")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4524")

    QueueWorkItem2(0x1B, 1, lambda_4524)

    def lambda_4535():

        label("loc_4535")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4535")

    QueueWorkItem2(0x1C, 1, lambda_4535)

    def lambda_4546():

        label("loc_4546")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4546")

    QueueWorkItem2(0x21, 1, lambda_4546)

    def lambda_4557():

        label("loc_4557")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4557")

    QueueWorkItem2(0x22, 1, lambda_4557)

    def lambda_4568():

        label("loc_4568")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4568")

    QueueWorkItem2(0x23, 1, lambda_4568)

    def lambda_4579():

        label("loc_4579")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4579")

    QueueWorkItem2(0x24, 1, lambda_4579)

    def lambda_458A():

        label("loc_458A")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_458A")

    QueueWorkItem2(0x25, 1, lambda_458A)

    def lambda_459B():

        label("loc_459B")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_459B")

    QueueWorkItem2(0x26, 1, lambda_459B)

    def lambda_45AC():
        OP_6D(-1510, 12000, 54280, 9000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_45AC)

    def lambda_45C4():
        OP_6E(342, 9000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_45C4)
    WaitChrThread(0x0, 0x2)
    Sleep(1000)

    def lambda_45DE():
        OP_6D(0, 12000, 47170, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_45DE)
    OP_8E(0x20, 0x1E, 0x2EE0, 0xB87E, 0x3E8, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_40A2 end

    def Function_17_461C(): pass

    label("Function_17_461C")

    EventBegin(0x0)
    OP_6D(20, 12000, 70880, 0)
    OP_67(0, -2830, -10000, 0)
    OP_6B(4410, 0)
    OP_6C(359000, 0)
    OP_6E(612, 0)

    def lambda_4661():
        OP_67(0, 6070, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4661)

    def lambda_4679():
        OP_6C(35000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4679)
    Sleep(8000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4221   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_17_461C end

    def Function_18_4695(): pass

    label("Function_18_4695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_469E")
    Return()

    label("loc_469E")

    EventBegin(0x0)
    OP_77(0x41, 0x64, 0x82, 0x0, 0x0)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x4)
    SetChrFlags(0x31, 0x40)
    SetChrChipByIndex(0x31, 32)
    ClearChrFlags(0x31, 0x80)
    SetChrPos(0x31, 43230, 16000, 80440, 270)
    SetChrFlags(0x31, 0x4)

    def lambda_46E2():

        label("loc_46E2")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_46E2")

    QueueWorkItem2(0x31, 1, lambda_46E2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x31, 400)
    Sleep(1000)

    def lambda_4718():
        OP_6D(40260, 16000, 79530, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4718)

    def lambda_4730():
        OP_8E(0xFE, 0x9178, 0x3E80, 0x13344, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4730)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x31, 400)
    Sleep(500)
    Fade(3000)
    OP_6C(69000, 3000)
    Sleep(2000)
    OP_44(0x31, 0xFF)
    Fade(1000)
    OP_51(0x31, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x31, 33)

    ChrTalk(
        0x31,
        (
            "#010F啊……艾丝蒂尔。\x02\x03",
            "真是个美丽的夜晚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x02\x03",
            "还是这首曲子啊。\x02\x03",
            "『星之所在』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F虽然我曾经丢掉了很多东西……\x02\x03",
            "不过，只有这首曲子\x01",
            "和这个口琴一直伴随着我……\x02\x03",
            "所以会经常吹起它。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F我是不是该履行约定了呢。\x02\x03",
            "与你相遇之前\x01",
            "我都做了些什么……\x02\x03",
            "现在我要全部说出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F约修亚……\x02\x03",
            "嗯……我知道了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4925():

        label("loc_4925")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_4925")

    QueueWorkItem2(0x31, 1, lambda_4925)

    def lambda_4936():
        OP_8E(0xFE, 0xA8FC, 0x3E80, 0x13F42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4936)
    Sleep(200)

    def lambda_4956():
        OP_6D(43230, 16000, 81140, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4956)
    WaitChrThread(0x101, 0x2)
    TurnDirection(0x101, 0x31, 300)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x31,
        (
            "#010F不过，故事稍微有点长……\x01",
            "这样也没关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F当然……\x01",
            "我肯定会认真地听到最后的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F谢谢……\x02\x03",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x31, 0xFF)
    OP_8C(0x31, 90, 300)
    Sleep(500)

    ChrTalk(
        0x31,
        (
            "#010F很久以前，在某个地方……\x02\x03",
            "在某个地方\x01",
            "有一个男孩。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    ChrTalk(
        0x31,
        (
            "#010F因为某件事，\x01",
            "心破碎了的男孩。\x02\x03",
            "丧失了言语和感情，饭也不吃，\x01",
            "只是天天在吹着口琴。\x02\x03",
            "照顾他的人努力都是白费，\x01",
            "男孩也日渐衰弱。\x02\x03",
            "这时在这个男孩面前，\x01",
            "出现了一个魔法师。\x02\x03",
            "『让我来把这孩子的心治好吧。』\x02\x03",
            "『只不过需要向我付出代价。』\x02\x03",
            "就这样，\x01",
            "男孩被交给了魔法师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F破碎的心被重新结合在了一起……\x02\x03",
            "可是，魔法师\x01",
            "将男孩的存在肆意地修改。\x02\x03",
            "然后，当得到新的心的时候——\x01",
            "男孩变成了一个杀手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F在两年的时间里，\x01",
            "男孩每天都在不断地杀人。\x02\x03",
            "曾经将几十人的部队\x01",
            "在暗中全灭。\x02\x03",
            "曾经潜入由强壮的护卫\x01",
            "严密看守的某国大臣的住宅，\x01",
            "将大臣的喉咙切断。\x02\x03",
            "有时还使用炸药，\x01",
            "将无辜的人们卷入。\x02\x03",
            "不知何时起，男孩\x01",
            "成为了叫做『漆黑之牙』的，\x01",
            "令人恐惧的存在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F……『漆黑之牙』………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F之后，男孩接到魔法师的命令，\x01",
            "去暗杀某个目标人物。\x02\x03",
            "那是以前守卫了女王治理的国家\x01",
            "不被北方大国侵占的英雄。\x02\x03",
            "拥有整个大陆只有四个人才有的\x01",
            "特别称号的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F但是，那个目标实在太强大了。\x02\x03",
            "像小猫被老虎轻松避开一样，\x01",
            "男孩被击退了。\x02\x03",
            "在落败的男孩面前，\x01",
            "魔法师的手下出现了。\x02\x03",
            "他们是来结果\x01",
            "被目标看到了真面目的男孩的。\x02\x03",
            "但是，有人将他们赶走\x01",
            "并救下了男孩。\x02\x03",
            "他正是男孩暗杀失败的\x01",
            "那个目标人物游击士。\x02\x03",
            "然后，男孩……\x02\x03",
            "被带到了他的家里，\x01",
            "和一个女孩相遇了……\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x31,
        (
            "#010F在那个家里，\x01",
            "男孩在五年间得到了美妙的梦。\x02\x03",
            "真的是对那个男孩来说\x01",
            "不应该拥有的梦……\x02\x03",
            "不过，梦总会醒来。\x02\x03",
            "回到现实的时刻已经迫近。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x31, 0x101, 400)

    ChrTalk(
        0x31,
        (
            "#010F到这里……故事就结束了。\x02\x03",
            "谢谢……\x01",
            "一直坚持着听到最后。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F…………………………………\x02\x03",
            "……哎……哈哈…………\x02\x03",
            "那个……到哪儿为止是真的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F全部——都是真的。\x02\x03",
            "我的心已经破碎了。\x02\x03",
            "我的手沾满了血。\x02\x03",
            "以及暗杀你的父亲失败，\x01",
            "都是真的。\x02\x03",
            "而且……到目前为止\x01",
            "一直在背叛着你们，也是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F男孩是真正意义上的\x01",
            "无可救药的存在。\x02\x03",
            "不管在哪里，\x01",
            "都会带来不幸和灾厄……\x02\x03",
            "就是这样污秽的存在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F所以……\x01",
            "男孩要去旅行。\x02\x03",
            "为了不让使自己作了\x01",
            "如此幸福的美梦的人们被卷进来。\x02\x03",
            "也为了阻止制造自己这样存在的\x01",
            "那个坏魔法师。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x31, 0xA910, 0x3E80, 0x13D26, 0x3E8, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚将自己的口琴\x01",
            "放在了艾丝蒂尔手中。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x31, 0xA8DE, 0x3E80, 0x13A38, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        "#000F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F那是让我将人的心\x01",
            "一直保持到最后的东西。\x02\x03",
            "已经不需要了……\x02\x03",
            "所以请你收下来。\x02\x03",
            "虽然可能算不上\x01",
            "这５年来的礼物……\x02\x03",
            "我想总比什么都没有好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F………………………………\x02\x03",
            "…………给我适可而止吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        "#010F哎……？\x02",
    )

    CloseMessageWindow()

    def lambda_5715():
        OP_6D(43230, 16000, 80820, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5715)

    def lambda_572D():
        OP_6E(259, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_572D)
    OP_8E(0x101, 0xA91A, 0x3E80, 0x13CA4, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        (
            "#000F你有完没完了！\x02\x03",
            "说什么在做梦……！\x02\x03",
            "难道……到现在为止的事情，\x01",
            "不是真的吗！\x02\x03",
            "过去怎么了！？\x02\x03",
            "心破碎了！？\x01",
            "那又怎么样！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        "#010F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F看着我！\x02\x03",
            "看着我的眼睛！\x02\x03",
            "我一直……\x01",
            "看着那个男孩的所做所为！\x02\x03",
            "是好是坏我都知道！\x02\x03",
            "男孩不管有什么样的痛苦，\x01",
            "都会抱着必死的决心努力的事情我也知道！\x02\x03",
            "因为……\x01",
            "我喜欢那样的约修亚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        "#010F！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F所以，绝对不会让你１个人去的！\x02\x03",
            "丢下我，不管我的心情，\x01",
            "就这样消失了？\x02\x03",
            "那是绝对不允许的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F……艾丝蒂尔………\x02\x03",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F………啊………………\x02\x03",
            "（………约修亚…………）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F什么……！\x02\x03",
            "流进嘴里的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F……是及时生效的\x01",
            " \x02\x03",
            "没有副作用，放心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F为……为什么……？\x02\x03",
            "……为什么用那样的东西……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F我的艾丝蒂尔……\x01",
            "你就像太阳一样的眩目，\x02\x03",
            "和你在一起虽然很幸福，\x01",
            "不过同时也感到很痛苦……\x02\x03",
            "就像强光可以产生浓重的影子一样……\x02\x03",
            "和你在一起的时候，\x01",
            "我就会不断想起\x01",
            "自己可憎的本性来……\x02\x03",
            "所以，我有时会想，\x01",
            "如果没有相遇过就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F……怎么会………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F不过，现在不一样。\x02\x03",
            "我很感激能和你相遇。\x02\x03",
            "虽然我不得不从\x01",
            "这样重要的女孩身边逃走……\x02\x03",
            "不过，我会比谁都更想念你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F……约修亚……约修亚………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#010F一直以来，真的很感谢你。\x02\x03",
            "从相遇的时候起……\x01",
            "我也一直喜欢着你。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)

    ChrTalk(
        0x31,
        "#010F——再见了，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_18_4695 end

    def Function_19_5D79(): pass

    label("Function_19_5D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E21")
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
    Jump("loc_5EAA")

    label("loc_5E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EAA")
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

    label("loc_5EAA")

    Return()

    # Function_19_5D79 end

    SaveToFile()

Try(main)
