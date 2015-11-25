from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0035   ._SN',
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
        '00400女游击士待机',                    # 9
        '00401女游击士移动',                    # 10
        '00402女游击士攻击',                    # 11
        '00403女游击士挨打',                    # 12
        '00404女游击士倒下',                    # 13
        '00407女游击士魔法咏唱',                # 14
        '00408女游击士魔法发动',                # 15
        '00390男游击士待机',                    # 16
        '00391男游击士移动',                    # 17
        '00392男游击士攻击',                    # 18
        '00393男游击士挨打',                    # 19
        '00394男游击士倒下',                    # 20
        '00395男游击士魔法咏唱',                # 21
        '00396男游击士魔法发动',                # 22
        '00370流氓待机',                        # 23
        '00371流氓移动',                        # 24
        '00372流氓攻击',                        # 25
        '00373流氓挨打',                        # 26
        '00374流氓倒下',                        # 27
        '00360空贼手下待机',                    # 28
        '00361空贼手下移动',                    # 29
        '00362空贼手下攻击',                    # 30
        '00363空贼手下挨打',                    # 31
        '00364空贼手下倒下',                    # 32
        '00310乔丝特待机',                      # 33
        '00311乔丝特移动',                      # 34
        '00312乔丝特攻击',                      # 35
        '00313乔丝特挨打',                      # 36
        '00314乔丝特倒下',                      # 37
        '00315乔丝特魔法咏唱',                  # 38
        '00316乔丝特魔法发动',                  # 39
        '00300吉尔待机',                        # 40
        '00301吉尔移动',                        # 41
        '00302吉尔攻击',                        # 42
        '00303吉尔挨打',                        # 43
        '00304吉尔倒下',                        # 44
        '00305吉尔魔法咏唱',                    # 45
        '00306吉尔魔法发动',                    # 46
        '00290多伦待机',                        # 47
        '00291多伦移动',                        # 48
        '00292多伦攻击',                        # 49
        '00293多伦挨打',                        # 50
        '00294多伦倒下',                        # 51
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
        'ED6_DT07/CH00400 ._CH',             # 00
        'ED6_DT07/CH00401 ._CH',             # 01
        'ED6_DT07/CH00402 ._CH',             # 02
        'ED6_DT07/CH00403 ._CH',             # 03
        'ED6_DT07/CH00404 ._CH',             # 04
        'ED6_DT07/CH00405 ._CH',             # 05
        'ED6_DT07/CH00406 ._CH',             # 06
        'ED6_DT07/CH00300 ._CH',             # 07
        'ED6_DT07/CH00301 ._CH',             # 08
        'ED6_DT07/CH00302 ._CH',             # 09
        'ED6_DT07/CH00303 ._CH',             # 0A
        'ED6_DT07/CH00304 ._CH',             # 0B
        'ED6_DT07/CH00305 ._CH',             # 0C
        'ED6_DT07/CH00306 ._CH',             # 0D
        'ED6_DT07/CH00390 ._CH',             # 0E
        'ED6_DT07/CH00391 ._CH',             # 0F
        'ED6_DT07/CH00392 ._CH',             # 10
        'ED6_DT07/CH00393 ._CH',             # 11
        'ED6_DT07/CH00394 ._CH',             # 12
        'ED6_DT07/CH00395 ._CH',             # 13
        'ED6_DT07/CH00396 ._CH',             # 14
        'ED6_DT07/CH00360 ._CH',             # 15
        'ED6_DT07/CH00361 ._CH',             # 16
        'ED6_DT07/CH00362 ._CH',             # 17
        'ED6_DT07/CH00363 ._CH',             # 18
        'ED6_DT07/CH00364 ._CH',             # 19
        'ED6_DT07/CH00370 ._CH',             # 1A
        'ED6_DT07/CH00371 ._CH',             # 1B
        'ED6_DT07/CH00372 ._CH',             # 1C
        'ED6_DT07/CH00373 ._CH',             # 1D
        'ED6_DT07/CH00374 ._CH',             # 1E
        'ED6_DT07/CH00310 ._CH',             # 1F
        'ED6_DT07/CH00311 ._CH',             # 20
        'ED6_DT07/CH00312 ._CH',             # 21
        'ED6_DT07/CH00313 ._CH',             # 22
        'ED6_DT07/CH00314 ._CH',             # 23
        'ED6_DT07/CH00315 ._CH',             # 24
        'ED6_DT07/CH00316 ._CH',             # 25
        'ED6_DT07/CH00290 ._CH',             # 26
        'ED6_DT07/CH00291 ._CH',             # 27
        'ED6_DT07/CH00292 ._CH',             # 28
        'ED6_DT07/CH00293 ._CH',             # 29
        'ED6_DT07/CH00294 ._CH',             # 2A
    )

    AddCharChipPat(
        'ED6_DT07/CH00400P._CP',             # 00
        'ED6_DT07/CH00401P._CP',             # 01
        'ED6_DT07/CH00402P._CP',             # 02
        'ED6_DT07/CH00403P._CP',             # 03
        'ED6_DT07/CH00404P._CP',             # 04
        'ED6_DT07/CH00405P._CP',             # 05
        'ED6_DT07/CH00406P._CP',             # 06
        'ED6_DT07/CH00300P._CP',             # 07
        'ED6_DT07/CH00301P._CP',             # 08
        'ED6_DT07/CH00302P._CP',             # 09
        'ED6_DT07/CH00303P._CP',             # 0A
        'ED6_DT07/CH00304P._CP',             # 0B
        'ED6_DT07/CH00305P._CP',             # 0C
        'ED6_DT07/CH00306P._CP',             # 0D
        'ED6_DT07/CH00390P._CP',             # 0E
        'ED6_DT07/CH00391P._CP',             # 0F
        'ED6_DT07/CH00392P._CP',             # 10
        'ED6_DT07/CH00393P._CP',             # 11
        'ED6_DT07/CH00394P._CP',             # 12
        'ED6_DT07/CH00395P._CP',             # 13
        'ED6_DT07/CH00396P._CP',             # 14
        'ED6_DT07/CH00360P._CP',             # 15
        'ED6_DT07/CH00361P._CP',             # 16
        'ED6_DT07/CH00362P._CP',             # 17
        'ED6_DT07/CH00363P._CP',             # 18
        'ED6_DT07/CH00364P._CP',             # 19
        'ED6_DT07/CH00370P._CP',             # 1A
        'ED6_DT07/CH00371P._CP',             # 1B
        'ED6_DT07/CH00372P._CP',             # 1C
        'ED6_DT07/CH00373P._CP',             # 1D
        'ED6_DT07/CH00374P._CP',             # 1E
        'ED6_DT07/CH00310P._CP',             # 1F
        'ED6_DT07/CH00311P._CP',             # 20
        'ED6_DT07/CH00312P._CP',             # 21
        'ED6_DT07/CH00313P._CP',             # 22
        'ED6_DT07/CH00314P._CP',             # 23
        'ED6_DT07/CH00315P._CP',             # 24
        'ED6_DT07/CH00316P._CP',             # 25
        'ED6_DT07/CH00290P._CP',             # 26
        'ED6_DT07/CH00291P._CP',             # 27
        'ED6_DT07/CH00292P._CP',             # 28
        'ED6_DT07/CH00293P._CP',             # 29
        'ED6_DT07/CH00294P._CP',             # 2A
    )

    DeclNpc(
        X                   = 4000,
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
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
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
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
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
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
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
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 12,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 13,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
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
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
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
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
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
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 14,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 15,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )


    ScpFunction(
        "Function_0_762",          # 00, 0
        "Function_1_763",          # 01, 1
        "Function_2_764",          # 02, 2
        "Function_3_77A",          # 03, 3
        "Function_4_790",          # 04, 4
        "Function_5_7AB",          # 05, 5
        "Function_6_7C6",          # 06, 6
        "Function_7_7E1",          # 07, 7
        "Function_8_805",          # 08, 8
        "Function_9_81B",          # 09, 9
        "Function_10_852",         # 0A, 10
        "Function_11_868",         # 0B, 11
        "Function_12_89F",         # 0C, 12
        "Function_13_8B5",         # 0D, 13
        "Function_14_8EC",         # 0E, 14
        "Function_15_902",         # 0F, 15
        "Function_16_939",         # 10, 16
    )


    def Function_0_762(): pass

    label("Function_0_762")

    Return()

    # Function_0_762 end

    def Function_1_763(): pass

    label("Function_1_763")

    Return()

    # Function_1_763 end

    def Function_2_764(): pass

    label("Function_2_764")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_779")
    OP_99(0xFE, 0x0, 0x7, 0x9C4)
    Jump("Function_2_764")

    label("loc_779")

    Return()

    # Function_2_764 end

    def Function_3_77A(): pass

    label("Function_3_77A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_78F")
    OP_99(0xFE, 0x0, 0x7, 0xBB8)
    Jump("Function_3_77A")

    label("loc_78F")

    Return()

    # Function_3_77A end

    def Function_4_790(): pass

    label("Function_4_790")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AA")
    OP_99(0xFE, 0x0, 0x0, 0x5DC)
    Sleep(500)
    Jump("Function_4_790")

    label("loc_7AA")

    Return()

    # Function_4_790 end

    def Function_5_7AB(): pass

    label("Function_5_7AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C5")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Sleep(500)
    Jump("Function_5_7AB")

    label("loc_7C5")

    Return()

    # Function_5_7AB end

    def Function_6_7C6(): pass

    label("Function_6_7C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E0")
    OP_99(0xFE, 0x0, 0x7, 0x3E8)
    Sleep(500)
    Jump("Function_6_7C6")

    label("loc_7E0")

    Return()

    # Function_6_7C6 end

    def Function_7_7E1(): pass

    label("Function_7_7E1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_804")
    OP_8D(0xFE, 4000, 20000, 24000, 28000, 1500)
    Jump("Function_7_7E1")

    label("loc_804")

    Return()

    # Function_7_7E1 end

    def Function_8_805(): pass

    label("Function_8_805")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_81A")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_8_805")

    label("loc_81A")

    Return()

    # Function_8_805 end

    def Function_9_81B(): pass

    label("Function_9_81B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_851")
    SetChrChipByIndex(0xFE, 5)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 6)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_9_81B")

    label("loc_851")

    Return()

    # Function_9_81B end

    def Function_10_852(): pass

    label("Function_10_852")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_867")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_10_852")

    label("loc_867")

    Return()

    # Function_10_852 end

    def Function_11_868(): pass

    label("Function_11_868")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_89E")
    SetChrChipByIndex(0xFE, 12)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 13)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_11_868")

    label("loc_89E")

    Return()

    # Function_11_868 end

    def Function_12_89F(): pass

    label("Function_12_89F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8B4")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_12_89F")

    label("loc_8B4")

    Return()

    # Function_12_89F end

    def Function_13_8B5(): pass

    label("Function_13_8B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8EB")
    SetChrChipByIndex(0xFE, 19)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 20)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_13_8B5")

    label("loc_8EB")

    Return()

    # Function_13_8B5 end

    def Function_14_8EC(): pass

    label("Function_14_8EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_901")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_14_8EC")

    label("loc_901")

    Return()

    # Function_14_8EC end

    def Function_15_902(): pass

    label("Function_15_902")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_938")
    SetChrChipByIndex(0xFE, 36)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 37)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_15_902")

    label("loc_938")

    Return()

    # Function_15_902 end

    def Function_16_939(): pass

    label("Function_16_939")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "你好。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_939 end

    SaveToFile()

Try(main)
